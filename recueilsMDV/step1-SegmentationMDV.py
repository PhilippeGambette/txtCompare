#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-

import glob, os, re, sys, time, requests, textdistance, unicodedata, math

# pip3 install selenium
# install "geckodriver" from https://github.com/mozilla/geckodriver/releases
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

"""
<nowiki/>

Dès lors, elles se rendirent quelques petits 
services professionnels, l’une allant chercher 
ou rapporter l’ouvrage de l’autre, et une bonne 
camaraderie s’établit entre elles. Peut-être la 
mère Renaud jugea-t-elle qu’il lui était,
somme toute, avantageux de se faire l’alliée de 
Geneviève, peut-être au fond du cœur, éprouvait-elle 
une honte secrète au souvenir du jour 
où elle enleva à sa misérable voisine, le travail 
douloureusement convoité. Elles firent même 
ensemble une expérience d’une nature toute 
contraire, et dont l’initiative, par un étrange 
retour, remonta à madame Renaud. 

Celle-ci eut un jour vent que le patron se 
proposait de ramener à seize sous la façon d’un 
corsage qui avait été fixée à dix-huit. On était 
à la fin de février, et le travail reprenait ;
l’occasion était bonne pour refuser la diminution 
dont madame Renaud avertit Geneviève 
un après-midi qu’elles se rendaient ensemble 
au Magasin. 

— Faudra pas accepter, insista madame 
Renaud. Il n’a que nous pour bien faire ce 
corsage-là, et il tient à vous. Tenez votre prix ;
"""

def stripAccents(text):
    # code from https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)
    

def preprocessString(string):
   """
   Return the string obtained after preprocessing (lowercase, etc.)
   """
   #strip accents
   string = stripAccents(string)

   #lower case
   string = string.lower()
   
   #for theater or texts with footnotes, remove [5], [10], etc.
   res = re.search("(.*)[\[][0-9]+[\]](.*)", string)
   while res:
      string = res.group(1)+res.group(2)
      res = re.search("(.*)[\[][0-9]+[\]](.*)", string)
   
   """
   # remove HTML tags
   res = re.search("([^<]*)[<][^>]*[>](.*)", string)
   while res:
      string = res.group(1)+res.group(2)
      res = re.search("([^<]*)[<][^>]*[>](.*)",string)
   print("2")   
   """
   return string


def nextWord(string):
   """
   return a list containing the first word of the input string as the first element
   and what follows as the second element
   """
   string = string.replace("\r"," ")
   string = string.replace("\n"," ")
   result=[]
   ponctuation = " _/?.,;:!¨«»+=()°*&\[\] ’'\-\r\n\t"
   res = re.search("^["+ponctuation+"]*([^"+ponctuation+"]+)["+ponctuation+"]*([^\r\n]*)[\r\n]*$",string)
   if res:
      result.append(res.group(1))
      result.append(res.group(2))
   return result


def build4Grams(text):
   """
   return a dictionary associating to each 4gram of the text its number of occurrences
   """
   found4grams = {}
   foundNextWord = nextWord(text)
   circular4gram = ["", "", "", ""]
   startOf4gram = 0
   while((len(foundNextWord) > 0) and (len(foundNextWord[0]) > 0)):
      circular4gram[startOf4gram] = foundNextWord[0]
      startOf4gram = (startOf4gram + 1)%4
      current4gram = circular4gram[startOf4gram] + " " + circular4gram[(startOf4gram + 1)%4] + " " + circular4gram[(startOf4gram + 2)%4] + " " + circular4gram[(startOf4gram + 3)%4] + " "
      if current4gram in found4grams:
         found4grams[current4gram] += 1
      else:
         found4grams[current4gram] = 1
      foundNextWord = nextWord(foundNextWord[1])
   return found4grams
      

def common4gramSimilarity(ngrams1, ngrams2):
   nbNgrams = 0
   nbCommonNgrams = 0
   for sequence in ngrams1:
      nbNgrams += ngrams1[sequence]
      if sequence in ngrams2:
         nbCommonNgrams += min(ngrams1[sequence], ngrams2[sequence])
   if nbNgrams > 0:
      result = nbCommonNgrams / nbNgrams
   else:
      result = 0
   return result


def common4grams(ngrams1, ngrams2):
   commonNgrams = []
   for sequence in ngrams1:
      if sequence in ngrams2:
         commonNgrams.append(sequence)
   return commonNgrams


def maxCommon4gramSimilarity(ngrams1, ngrams2):
   """
   return the maximum among the number of ngrams of ngrams1 contained in ngrams2 and
   the number of ngrams2 contained in ngrams1
   """
   return max(common4gramSimilarity(ngrams1, ngrams2), common4gramSimilarity(ngrams2, ngrams1))
   

def appendToCorpus(corpus, id, text, title):
   """
   change the list inside variable corpus to append a dictionary containing 
   the text, the title and the 4 grams contained in the text
   """
   corpus.append({"id": id, "text": text, "title": title, "4grams": build4Grams(preprocessString(text))})


# Get the current folder
folder = os.path.abspath(os.path.dirname(sys.argv[0]))

segmentationType = "uppercaseTitle"

corpora = []
corpusNumber = 0
corpusNames = ["","R1822","R1830"]

# Consider all txt files in the corpus folder
for file in glob.glob(os.path.join(os.path.join(folder, "corpus"), "*.txt")):
   corpusNumber += 1
   print("Opening file " + file + " for segmentation")
   inputFile = open(file, "r", encoding="utf-8")
   corpus = []
   text = ""
   title = ""
   textNumber = 0
   nbTitle = 0
   for line in inputFile:
      if segmentationType == "uppercaseTitle":
         #res = re.search("^([ '\"«»\(\)-.,;!?·…&\[\]]*[ A-Z\u00C0-\u00DC]+[ A-Z\u00C0-\u00DC'\"«»\(\)-.,;!?·…&\[\]]+)$", line)
         res = re.search("^¤(.*)$", line)
         if res:
            nbTitle += 1
            print("Title #" + str(nbTitle) + " found: " + title)
            appendToCorpus(corpus, corpusNames[corpusNumber]+"-"+str(textNumber), text, title)
            title = res.group(1)
            text = ""
            textNumber += 1
      text += line
   corpora.append(corpus)
   inputFile.close()


# compute distances between texts
for corpusNb in range(0, len(corpora)-1):
   print("Comparing text " + str(corpusNb) + " with text " + str(corpusNb+1))
   corpus1 = corpora[corpusNb]
   corpus2 = corpora[corpusNb + 1]
   similarityMatrix = []
   numText1 = 0
   for i in range(0, len(corpus1)):
      numText2 = 0
      similarityMatrixLine = []
      for j in range(0, len(corpus2)):
         similarityMatrixLine.append(maxCommon4gramSimilarity(corpus1[i]["4grams"], corpus2[j]["4grams"]))
         numText2 += 1
      similarityMatrix.append(similarityMatrixLine)
      numText1 += 1
   print(similarityMatrix)
   
   nbRemoved = 0
   similarText = {}
   # Find most similar texts
   bestSimilarity = 1
   nbAssociations = 0
   while len(corpus1)>nbRemoved and len(corpus2)>nbRemoved:
      nbAssociations += 1
      max = 0
      maxI = 0
      maxJ = 0
      for i in range(0, len(corpus1)):
         for j in range(0, len(corpus2)):
            if similarityMatrix[i][j] > max:
               max = similarityMatrix[i][j]
               bestSimilarity = max
               maxI = i
               maxJ = j
      print("#" + str(nbAssociations) + " " + str(maxI) + " <-> " + str(maxJ))
      print(similarityMatrix[maxI][maxJ])
      print(corpus1[maxI]["title"] + " <-> " + corpus2[maxJ]["title"])
      if bestSimilarity > 0.1:
         similarText[corpus2[maxJ]["id"]] = corpus1[maxI]["id"]
      """
      else:
         print(corpus1[maxI]["text"] + " ====================================================================================== " + corpus2[maxJ]["text"])
         print(str(common4grams(corpus1[maxI]["4grams"],corpus2[maxJ]["4grams"])))
         print(str(common4gramSimilarity(corpus1[maxI]["4grams"],corpus2[maxJ]["4grams"]))+ " OU " + str(common4gramSimilarity(corpus2[maxJ]["4grams"],corpus1[maxI]["4grams"]))+ " =? " + str(similarityMatrix[maxI][maxJ]))
         print(" ")
         print(" ")
         print(" ")
         print(" ")
      """
         
      nbRemoved += 1
      for i in range(0, len(corpus1)):
         similarityMatrix[i][maxJ] = -1
      for j in range(0, len(corpus2)):
         similarityMatrix[maxI][j] = -1
      
      
   # Start creating output file
   outputFile = open(file + ".js", "w", encoding="utf-8")
   outputFile.writelines(',\n')
   outputFile.writelines('{ titreLong : \'<i>Conversations d’Émilie</i> de Louise d’Épinay, dans les éditions <a href="https://books.google.fr/books?id=olZ9vgAACAAJ&hl=fr&pg=PR1#v=onepage&q&f=false">de 1774</a> et <a href="https://fr.wikisource.org/wiki/Les_Conversations_d%E2%80%99%C3%89milie">de 1781</a>\',\n')
   outputFile.writelines('titreCourt : \'<i>' + file + '</i>\',\n')
   outputFile.writelines('ecart : 13,\n')
   outputFile.writelines('pixelsParPage : 0.5,\n')
   outputFile.writelines('sourceData : "https://docs.google.com/spreadsheets/d/1wqyxRS_6LTE5gAPa8qxydS2dHLSUxTUYJ43467Rn6pM/edit?usp=sharing",\n')
   outputFile.writelines('texts : [\n')
   outputFile.writelines('["identifiant","recueil","partie","texte","nb-pages","lien","url"],')
   for element in corpus1:
      outputFile.writelines('["' + element["id"] + '","' + element["id"].split("-")[0] + '","1","' + element["title"] + '","' + str(math.floor(len(element["text"])/300)) + '","","https://www.google.com"],\n')
   for element in corpus2:
      if element["id"] in similarText :
         outputFile.writelines('["' + element["id"] + '","' + element["id"].split("-")[0] + '","1","' + element["title"] + '","' + str(math.floor(len(element["text"])/300)) + '","' + similarText[element["id"]] + '","https://www.google.com"],\n')
      else:
         outputFile.writelines('["' + element["id"] + '","' + element["id"].split("-")[0] + '","1","' + element["title"] + '","' + str(math.floor(len(element["text"])/300)) + '","","https://www.google.com"],\n')
   outputFile.writelines(']\n')
   outputFile.writelines('}\n')
   outputFile.close()