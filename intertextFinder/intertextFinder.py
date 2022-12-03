# coding: utf8
#!/usr/sfw/bin/python

"""
    intertextFinder, a script of txtCompare to find common n-grams
    between a text and a corpus
    Copyright (C) 2022, Philippe Gambette
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

"""
How to use (with texts provided in the .txt format, UTF-8 encoding):
- put the corpus into a folder named `TXT` in the same folder as this script
- put the texts to analyze into a folder named `todo` in the same folder as this script
- run the script by executing in the console the following command: python intertextFinder.py
- for each text file in the todo folder, a new file with the same name and the extra extension .html is added into the same folder
"""

import glob, os, re, sys, time
from io import open

startTime = time.time()
   
"""
return the string obtained after preprocessing (lowercase, etc.)
"""
def preprocessLine(string):
   #lower case
   string = string.lower()
   
   #better lower case (currently does not work)
   string = string.replace("À","à")
   string = string.replace("É","é")
   string = string.replace("Ô","ô")   
   
   #for theater, remove [5], [10], etc.
   res = re.search("(.*)[\[][0-9]+[\]](.*)",string)
   while res:
      string = res.group(1)+res.group(2)
      res = re.search("(.*)[\[][0-9]+[\]](.*)",string)
   return string


"""
return a table containing the first word of the input string as the first element
and what follows as the second element
"""
def nextWord(string):
   result=[]
   ponctuation = " _/?.,;:!¨«»+=()°*&\[\] ’'\-\r\n	"
   res = re.search("^["+ponctuation+"]*([^"+ponctuation+"]+)["+ponctuation+"]*([^\r\n]*)[\r\n]*$",string)
   if res:
      result.append(res.group(1))
      result.append(res.group(2))
      #print "suit "+res.group(2)
   return result

"""
build the n-grams of the input text
- inputAddress: input text
- outputAddress: output text of the exported ngrams
"""
def buildNGrams(inputAddress,outputAddress):
   dicoNext={}
   ngram=[]
   text=[]
   ngram.append("")
   ngram.append("")
   ngram.append("")
   ngram.append("")
   # On ouvre le fichier à l'adresse inputAddress,
   # et on stocke ses lignes dans la variable inputLines :
   inputFile = open(inputAddress,"r",encoding='utf-8')
   inputLines = inputFile.readlines()
   
   # On se prépare à écrire dans le fichier à l'adresse outputFile :
   outputFile = open(outputAddress,"w",encoding='utf-8')
   
   i = 0
   
   # On enregistre la position des retours à la ligne
   wordNb=0
   linebreaks=[]
   
   # On considère l'une après l'autre
   # chacune des lignes stockées dans inputLines :
   for lin in inputLines:
      lin = preprocessLine(lin)
      #print("Starting to treat line "+lin)
      resultNextWord=nextWord(lin)
      #print resultNextWord
      while((len(resultNextWord)>0) and (len(resultNextWord[0])>0)):
         wordNb+=1
         #print(resultNextWord[0])
         ngram[i%4]=resultNextWord[0]
         text.append(resultNextWord[0])
         if not(ngram[(i+1)%4] in dicoNext):
            dicoNext[ngram[(i+1)%4]]={}
         if not(ngram[(i+2)%4] in dicoNext[ngram[(i+1)%4]]):
            dicoNext[ngram[(i+1)%4]][ngram[(i+2)%4]]={}
         if not(ngram[(i+3)%4] in dicoNext[ngram[(i+1)%4]][ngram[(i+2)%4]]):
            dicoNext[ngram[(i+1)%4]][ngram[(i+2)%4]][ngram[(i+3)%4]]={}
         if not(ngram[i%4] in dicoNext[ngram[(i+1)%4]][ngram[(i+2)%4]][ngram[(i+3)%4]]):
            dicoNext[ngram[(i+1)%4]][ngram[(i+2)%4]][ngram[(i+3)%4]][ngram[i%4]]=[]
         dicoNext[ngram[(i+1)%4]][ngram[(i+2)%4]][ngram[(i+3)%4]][ngram[i%4]].append(i)
         i+=1
         lin=resultNextWord[1]
         resultNextWord=nextWord(lin)
      linebreaks.append(wordNb+4)
   #print dicoNext
   
   for w1 in sorted(dicoNext):
      for w2 in sorted(dicoNext[w1]):
         for w3 in sorted(dicoNext[w1][w2]): 
            for w4 in sorted(dicoNext[w1][w2][w3]):
               #print w4
               outputFile.writelines(w1+";"+w2+";"+w3+";"+w4+";"+str(len(dicoNext[w1][w2][w3][w4]))+"\n")
               #for i in sorted(dicoNext[w1][w2][w3][w4]): 
               #   outputFile.writelines(w1+";"+w2+";"+w3+";"+w4+";"+str(i)+"\n")
   inputFile.close()
   outputFile.close()
   return {"results":dicoNext,"linebreaks":linebreaks}


"""
find the n-grams of dicoNext present in the input text
- dicoNext: list of n-grams
- inputAddress: input text
- outputFile: output file of the found n-grams
"""
def findNGrams(dicoNext,dicoResults,inputAddress,outputFile):
   inputFileName = os.path.basename(inputAddress)
   
   print("Looking for n-grams")
   dicoText={}
   ngram=[]
   text=[]
   ngram.append("")
   ngram.append("")
   ngram.append("")
   ngram.append("")
   # On ouvre le fichier à l'adresse inputAddress,
   # et on stocke ses lignes dans la variable inputLines :
   inputFile = open(inputAddress,"r",encoding='utf-8')
   inputLines = inputFile.readlines()
   
   i = 0
   
   #consider each line
   for lin in inputLines:

         
      #look for n-grams in the line after preprocessing
      lin = preprocessLine(lin)
      #print("Starting to treat line "+lin)
      resultNextWord=nextWord(lin)
      #print resultNextWord
      while((len(resultNextWord)>0) and (len(resultNextWord[0])>0)):
         #print(resultNextWord[0])
         ngram[i%4]=resultNextWord[0]
         text.append(resultNextWord[0])
         if (ngram[(i+1)%4] in dicoNext):
            if (ngram[(i+2)%4] in dicoNext[ngram[(i+1)%4]]):
               if (ngram[(i+3)%4] in dicoNext[ngram[(i+1)%4]][ngram[(i+2)%4]]):
                  if (ngram[i%4] in dicoNext[ngram[(i+1)%4]][ngram[(i+2)%4]][ngram[(i+3)%4]]):
                     #print "found "+ngram[(i+1)%4]+" "+ngram[(i+2)%4]+" "+ngram[(i+3)%4]+" "+ngram[(i)%4]
                     foundNGram = ngram[(i+1)%4]+" "+ngram[(i+2)%4]+" "+ngram[(i+3)%4]+" "+ngram[(i)%4]
                     outputFile.writelines(inputAddress+";"+str(i)+";"+foundNGram+";"+str(len(dicoNext[ngram[(i+1)%4]][ngram[(i+2)%4]][ngram[(i+3)%4]][ngram[(i)%4]]))+";"+str(dicoNext[ngram[(i+1)%4]][ngram[(i+2)%4]][ngram[(i+3)%4]][ngram[(i)%4]])+"\n")
                     if not foundNGram in dicoResults:
                        dicoResults[foundNGram] = []
                     dicoResults[foundNGram].append("'"+foundNGram+"' dans "+inputFileName+" - position "+str(i))

         """
         if (ngram[(i+1)%4] in dicoText):
            dicoText[ngram[(i+1)%4]]={}
         if not(ngram[(i+2)%4] in dicoText[ngram[(i+1)%4]]):
            dicoText[ngram[(i+1)%4]][ngram[(i+2)%4]]={}
         if not(ngram[(i+3)%4] in dicoText[ngram[(i+1)%4]][ngram[(i+2)%4]]):
            dicoText[ngram[(i+1)%4]][ngram[(i+2)%4]][ngram[(i+3)%4]]={}
         if not(ngram[i%4] in dicoText[ngram[(i+1)%4]][ngram[(i+2)%4]][ngram[(i+3)%4]]):
            dicoText[ngram[(i+1)%4]][ngram[(i+2)%4]][ngram[(i+3)%4]][ngram[i%4]]=[]
         dicoText[ngram[(i+1)%4]][ngram[(i+2)%4]][ngram[(i+3)%4]][ngram[i%4]].append(i)
         """
         i+=1
         lin=resultNextWord[1]
         resultNextWord=nextWord(lin)
      
   #print dicoText
   
   for w1 in sorted(dicoText):
      for w2 in sorted(dicoText[w1]):
         for w3 in sorted(dicoText[w1][w2]): 
            for w4 in sorted(dicoText[w1][w2][w3]):
               #print w4
               outputFile.writelines(inputAddress+";"+nGram+";"+str(len(dicoText[w1][w2][w3][w4]))+";"+dicoText[w1][w2][w3][w4]+"\n")
               
                  
               #for i in sorted(dicoText[w1][w2][w3][w4]): 
               #   outputFile.writelines(w1+";"+w2+";"+w3+";"+w4+";"+str(i)+"\n")
                  
   #close the output file
   inputFile.close()      
   
   return dicoResults

# store in the folder variable the address of the folder containing this program
folder = os.path.abspath(os.path.dirname(sys.argv[0]))

filenameQuery = ""
dicoNext={}
fileLinebreaks=[]

# Consider all texts in the todo folder
for file in glob.glob(folder+"\\todo\\*.txt"):
   # Display the address of the file being treated
   print("Currently extacting 4-grams from file "+file)
   
   # Extract the file name without the extension
   res = re.search("todo.(.*).txt",file)
   if res:
      fileName = res.group(1)     
      filenameQuery=fileName
      
      # build the list of n-grams of file and save it to a text file
      results=buildNGrams(file,folder+"\\"+fileName+".4grams.txt")
      dicoNext=results["results"]
      fileLinebreaks.append(results["linebreaks"])
      
   print("Finished creating file "+folder+"\\"+fileName+".4grams.txt" )

outputFile = open(folder+"\\"+filenameQuery+".found4grams.txt","w",encoding='utf-8')

dicoResults = {}
sourceFileList = ""
fileNb = 0

# Look for n-grams in other files, in the TXT folder
#for file in files:
#   file = os.path.join(os.path.join(folder,"TXT"),file)
for file in glob.glob(folder+"\\TXT\\*.txt"):
   sourceFileList += "<li><tt>" + os.path.basename(file) + "</tt></li>"
   # Display the address of the file being treated
   print("Currently checking 4-grams in file "+file)
   
   # Extract the file name without the extension
   res = re.search("TXT.(.*).txt",file)
   if res:
      fileName = res.group(1)     
      # find n-grams present in dicoNext in file to add them to outputFile
      dicoResults = findNGrams(dicoNext,dicoResults,file,outputFile)      
         
   print("Finished creating file "+folder+"\\"+fileName+".4grams.txt")
   fileNb += 1

fileNb  =0

# Consider all texts in the todo folder
for file in glob.glob(folder+"\\todo\\*.txt"):
   # Display the address of the file being treated
   print("Currently building results from file "+file) 
   htmlFile = open(file+".html","w",encoding='utf-8')
   htmlFile.writelines("<!doctype html>\n")
   htmlFile.writelines("<html>\n  <meta charset=\"UTF-8\">\n  <head>\n  <title>" + os.path.basename(file) + "</title>\n  </head>\n<body>\n")
   htmlFile.writelines("<h1>Result of <a href=\"https://github.com/PhilippeGambette/txtCompare\"><tt>intertextFinder</tt></a></h1>")
   htmlFile.writelines("<p>Results of the search for common 4-grams between <tt>" + os.path.basename(file) + "</tt> and the texts of the following corpus:</p>")
   htmlFile.writelines("<ul>" + sourceFileList + "</ul>")
   htmlFile.writelines("<p>Below, the first word of a common 4-gram (sequence of 4 consecutive words, ignoring case and punctuation) is coloured red, the lighter the more frequently this 4-gram was found in the corpus. The word is underlined if one of the corresponding 4-grams in the corpus can be extended to the left, together with previously found common 4-grams (thus forming a 5-gram, or better).</p>")
   htmlFile.writelines("<p>Scroll down the page to find the words in red, and hover over them to display a tooltip indicating where the 4-gram was found.</p>")
   htmlFile.writelines("<hr/>")
   htmlFile.writelines("<h1>Résultats d'<a href=\"https://github.com/PhilippeGambette/txtCompare\"><tt>intertextFinder</tt></a></h1>")
   htmlFile.writelines("<p>Résultats de la recherche de 4-grammes communs entre <tt>" + os.path.basename(file) + "</tt> et les textes du corpus suivant :</p>")
   htmlFile.writelines("<ul>" + sourceFileList + "</ul>")
   htmlFile.writelines("<p>Ci-dessous, le premier mot d'un 4-gramme (suite de 4 mots consécutifs, en ignorant la casse et la ponctuation) commun est coloré en rouge, d'autant plus pâle que ce 4-gramme a été fréquemment trouvé dans le corpus. Le mot est souligné si un des 4-grammes correspondants dans le corpus peut-être prolongé vers la gauche, avec des 4-grammes communs précédemment trouvés (formant ainsi un 5-gramme, ou mieux).</p>")
   htmlFile.writelines("<p>Faites défiler la page pour trouver les mots en rouge, et passez la souris dessus pour afficher une infobulle qui indique où le 4-gramme a été trouvé.</p>")
   htmlFile.writelines("<hr/>")
   inputFile = open(file,"r",encoding='utf-8')
   inputLines = inputFile.readlines()
   ngram=[]
   ngram.append("")
   ngram.append("")
   ngram.append("")
   ngram.append("")
   i=0
   previouslyFoundNgramPositions = []
   foundNgramPositions = []
   
   #variable to extend the ngrams to the left
   previousNgrams=[]
   previousNgram=[]
   currentNgrams=[]
   currentNgram=[]
   
   linebreaks=fileLinebreaks[fileNb]
   fileNb+=1
   wordNb=0
   
   for lin in inputLines:
      lin = preprocessLine(lin)
      resultNextWord=nextWord(lin)
      while((len(resultNextWord)>0) and (len(resultNextWord[0])>0)):
      #print(resultNextWord[0])
         wordNb += 1
         if wordNb in linebreaks:
            htmlFile.writelines("<br/>")
         ngram[i%4]=resultNextWord[0]
         theNgram = ngram[(i+1)%4]+" "+ngram[(i+2)%4]+" "+ngram[(i+3)%4]+" "+ngram[i%4]
         word = ngram[(i+1)%4].replace("&","&amp;").replace("<","&lt;").replace("&","&gt;")
         previouslyFoundNgramPositions = foundNgramPositions
         foundNgramPositions = []
         if theNgram in dicoResults:
            # Sum up the number of times the n-gram was found in the other fles
            nbFound = 0
            combinesWithPreviouslyFoundNgram = False
            infoAboutFoundNGrams = ""
            
            # update the list of previous ngrams
            previousNgrams=currentNgrams
            
            for foundNGram in dicoResults[theNgram]:
               nbFound += 1
               res = re.search("'(.*)' dans (.*) - position ([0-9]+)$",foundNGram)
               if res:
                  currentNgram=res.group(1).split(" ")
                  extendedNgram=res.group(1)
                  for possiblePreviousNgram in previousNgrams:
                     if (possiblePreviousNgram["book"]==res.group(2)) and (int(possiblePreviousNgram["position"])==int(res.group(3))-1):
                        extendedNgram=possiblePreviousNgram["ngram"]+" "+currentNgram[3]
                  currentNgrams.append({"ngram":extendedNgram,"book":res.group(2),"position":res.group(3)})
                  foundNgramPositions.append(res.group(3))
                  if str(int(res.group(3))-1) in previouslyFoundNgramPositions:
                     combinesWithPreviouslyFoundNgram = True
                  infoAboutFoundNGrams += "'"+extendedNgram+"' dans "+res.group(2)+" - position "+res.group(3)+"&#10;"            
            if combinesWithPreviouslyFoundNgram:
               htmlFile.writelines("<span style=\"color:red;opacity:"+str(1.0/nbFound)+"\"><u><a title=\""+infoAboutFoundNGrams+"\">"+word+"</u></a></span>\n")
            else:
               htmlFile.writelines("<span style=\"color:red;opacity:"+str(1.0/nbFound)+"\"><a title=\""+infoAboutFoundNGrams+"\">"+word+"</a></span>\n")
         else:
            htmlFile.writelines(word+"\n")
            foundNgramPositions = []            
         i+=1
         lin=resultNextWord[1]
         resultNextWord=nextWord(lin)
   inputFile.close()
   htmlFile.writelines("</body></html>")
   htmlFile.close()

outputFile.close()

print(str(time.time()-startTime))