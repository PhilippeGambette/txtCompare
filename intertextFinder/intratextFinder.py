# coding: utf8
#!/usr/sfw/bin/python

"""
    intratextFinder, a script of txtCompare to find common n-grams
    between texts inside a corpus
    Copyright (C) 2018-2024, Philippe Gambette
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

import glob, os, re, sys, time
from io import open

startTime = time.time()
viz = "graph"

#import glob, sys, os, re, string, time, random
#from math import *

"""
Remove all HTML tags to keep only words in the file
"""
def cleanLine(line):
   # Tant que la ligne à nettoyer contient une balise HTML, c'est-à-dire un
   # symbole "<", suivi de n'importe quoi sans ">", suivi d'un symbole ">"
   # on supprime cette partie de la ligne.
   # Pour cela on utilise de nouveau une "expression régulière" :
   res = re.search("([^<]*)<[^>]*>(.*)",line)
   while res:
      # Si on a trouvé une balise HTML, on ne laisse dans line que ce qui précédait :
      # - res.group(1) correspond à ce qu'il y a
      # dans le premier couple de parenthèses de l'expression régulière
      # - res.group(2) correspond à ce qu'il y a
      # dans le second couple de parenthèses de l'expression régulière
      # - "\n" correspond au retour à la ligne, qui sera perdu si on ne l'ajoute pas :
      line = res.group(1)+res.group(2)+"\n"
      
      # On vérifie s'il reste encore des balises HTML à nettoyer :
      res = re.search("([^<]*)<[^>]*>(.*)",line)
   return line
      
   
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
   res = re.search("(.*)[[][0-9]+[]](.*)",string)
   while res:
      string = res.group(1)+res.group(2)
      res = re.search("(.*)[[][0-9]+[]](.*)",string)
   return string


"""
return a table containing the first word of the input string as the first element
and what follows as the second element
"""
def nextWord(string):
   result=[]
   ponctuation = " _/?.,;:!¨«»+=()°*&\[\] '\-\r\n	"
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
def buildNGrams(inputAddress,outputAddress,dicoNext):
   # prepare the 4gram table
   ngram=[]
   text=[]
   ngram.append("")
   ngram.append("")
   ngram.append("")
   ngram.append("")
   
   # Store into variable inputLines the content of the file saved at inputAddress,
   inputFile = open(inputAddress,"r",encoding='utf-8')
   inputLines = inputFile.readlines()
   
   # Open the output file at address outputFile :
   outputFile = open(outputAddress,"w",encoding='utf-8')
   i = 0
   
   # Read all lines
   for lin in inputLines:
      lin = preprocessLine(lin)
      #print("Starting to treat line "+lin)
      resultNextWord=nextWord(lin)
      #print resultNextWord
      while((len(resultNextWord)>0) and (len(resultNextWord[0])>0)):
         #print(resultNextWord[0])
         ngram[i%4]=resultNextWord[0]
         text.append(resultNextWord[0])
         key = str([ngram[(i+1)%4],ngram[(i+2)%4],ngram[(i+3)%4],ngram[i%4]])
         if str(key) not in dicoNext:
             dicoNext[key]=[]
         dicoNext[key].append(i)
         i+=1
         lin=resultNextWord[1]
         resultNextWord=nextWord(lin)
      
   #print dicoNext
   
   for key in sorted(dicoNext):
      outputFile.writelines(key+";"+str(len(dicoNext[key]))+"\n")
                  
            
   # On referme le fichier contenant la page web téléchargée
   # et le fichier texte dans lequel on vient d'écrire. 
   inputFile.close()
   outputFile.close()
   return dicoNext


"""
find the n-grams of dicoNext present in the input text
- dicoNext: list of n-grams
- inputAddress: input text
- outputFile: output file of the found n-grams
"""
def findNGrams(dicoNext,dicoResults,inputAddress,inputFileCode,outputFile):
   
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
   
   # On va stocker le nombre de lignes traitées dans la variable i
   # qui a initialement la valeur 0
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
         if (str([ngram[(i+1)%4],ngram[(i+2)%4],ngram[(i+3)%4],ngram[i%4]]) in dicoNext):
            foundNGram = ngram[(i+1)%4]+" "+ngram[(i+2)%4]+" "+ngram[(i+3)%4]+" "+ngram[(i)%4]
            outputFile.writelines(inputAddress+";"+str(i)+";"+foundNGram+";"+str(len(dicoNext[str([ngram[(i+1)%4],ngram[(i+2)%4],ngram[(i+3)%4],ngram[i%4]])]))+";"+str(dicoNext[str([ngram[(i+1)%4],ngram[(i+2)%4],ngram[(i+3)%4],ngram[i%4]])])+"\n")
            if not foundNGram in dicoResults:
                dicoResults[foundNGram] = []
            dicoResults[foundNGram].append([foundNGram,inputFileCode,i])

         i+=1
         lin=resultNextWord[1]
         resultNextWord=nextWord(lin)
   
   for key in sorted(dicoText):
      outputFile.writelines(inputAddress+";"+nGram+";"+str(len(dicoText[key]))+";"+dicoText[key]+"\n")
   
   #close the output file
   inputFile.close()      
   
   return dicoResults


# store in the folder variable the address of the folder containing this program
folder = (os.path.dirname(os.path.abspath(sys.argv[0])))

dicoNext={}
files = []

# Consider all texts in the TXT folder
for file in glob.glob(folder+"\\TXT\\*.txt"):
   # Display the address of the file being treated
   print("Currently extacting 4-grams from file "+file)
   
   # Extract the file name without the extension
   res = re.search("TXT.(.*).txt",file)
   if res:
      fileName = res.group(1)     
      # Add it to the list of files
      files.append(fileName)
      
      # build the list of n-grams of file and save it to a text file
      dicoNext = buildNGrams(file,folder+"\\"+fileName+".4grams.txt",dicoNext)
      
   print("Finished creating file "+folder+"\\"+fileName+".4grams.txt" )

outputFile = open(folder+"\\"+fileName+".found4grams.txt","w",encoding='utf-8')

dicoResults = {}
fileCode = 0

# Graph of number of common 4grams between texts
graph = [];


# Look for n-grams in other files, in the TXT folder
for file in glob.glob(folder+"\\TXT\\*.txt"):
   # Display the address of the file being treated
   print("Currently checking 4-grams in file "+file)
   graph.append([])
   
   # Extract the file name without the extension
   res = re.search("TXT.(.*).txt",file)
   if res:
      fileName = res.group(1)     
      # find n-grams present in dicoNext in file to add them to outputFile
      dicoResults = findNGrams(dicoNext,dicoResults,file,fileCode,outputFile)      
         
   print("Finished creating file "+folder+"\\"+fileName+".4grams.txt")
   fileCode += 1

currentFileCode = 0

print("Creating file "+os.path.join(folder,"intratextFinder.html"))
globalHtmlFile = open(os.path.join(folder,"intratextFinder.html"),"w",encoding='utf-8')
globalHtmlFile.writelines("""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link href="https://www.d3-graph-gallery.com/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
<style>

.node {
  stroke: #fff;
  stroke-width: 1.5px;
}

.link {
  stroke: #999;
  stroke-opacity: .6;
}

</style>
</head>

<!-- Load d3.js -->
<script src="https://d3js.org/d3.v3.js"></script>
<script src="https://d3js.org/d3-array.v1.min.js"></script>
<script src="https://d3js.org/d3-path.v1.min.js"></script>
<script src="https://d3js.org/d3-chord.v1.min.js"></script>
<body>
""")


if viz=="graph":
   globalHtmlFile.writelines('<h1>Réseau de similarité</h1><div id="graph"></div>\n')


globalHtmlFile.writelines("<h1>Repérage d'intertextualité dans les documents</h1><ul>\n")


# Consider all texts in the TXT folder
for file in glob.glob(folder+"\\TXT\\*.txt"):
   for s in graph:
      s.append(0);
   # Display the address of the file being treated
   print("Currently building results from file "+file) 
   htmlFile = open(file+".html","w",encoding='utf-8')
   htmlFile.writelines("<html>\n  <head>\n  <title>"+os.path.basename(file)+"</title>\n  <meta charset=\"UTF-8\">\n  </head>\n<body>\n")
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
   globalHtmlFile.writelines('<li><a href="'+file+'.html">'+files[currentFileCode]+'</a></li>\n')
   for lin in inputLines:
      lin = preprocessLine(lin)
      resultNextWord=nextWord(lin)
      while((len(resultNextWord)>0) and (len(resultNextWord[0])>0)):
      #print(resultNextWord[0])
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
            for foundNGram in dicoResults[theNgram]:
               if foundNGram[1] != currentFileCode:
                  nbFound += 1
                  pos = foundNGram[2]
                  foundNgramPositions.append(pos)
                  if pos-1 in previouslyFoundNgramPositions:
                        combinesWithPreviouslyFoundNgram = True
                  infoAboutFoundNGrams += foundNGram[0]+" "+files[foundNGram[1]]+" "+str(foundNGram[2])+"&#10;"
            if nbFound >0:
               if combinesWithPreviouslyFoundNgram:
                  htmlFile.writelines("<span style=\"color:red;opacity:"+str(1.0/nbFound)+"\"><u><a title=\""+infoAboutFoundNGrams+"\">"+word+"</u></a></span>\n")
               else:
                  htmlFile.writelines("<span style=\"color:red;opacity:"+str(1.0/nbFound)+"\"><a title=\""+infoAboutFoundNGrams+"\">"+word+"</a></span>\n")
            else:
               htmlFile.writelines(word+"\n")
         else:
            htmlFile.writelines(word+"\n")
         i+=1
         lin=resultNextWord[1]
         resultNextWord=nextWord(lin)
   currentFileCode += 1
   inputFile.close()
   htmlFile.writelines("</body></html>")
   htmlFile.close()

outputFile.close()

# Build the graph of shared ngrams
for ngram in dicoResults:
   foundTextsForNgram = []
   for foundNGram in dicoResults[ngram]:
       if foundNGram[1] not in foundTextsForNgram:
          foundTextsForNgram.append(foundNGram[1])
   if len(foundTextsForNgram)>0:
      i=0
      while i<len(foundTextsForNgram):
         j=i+1
         while j<len(foundTextsForNgram):
            graph[foundTextsForNgram[i]][foundTextsForNgram[j]] += 2/len(dicoResults[ngram])
            graph[foundTextsForNgram[j]][foundTextsForNgram[i]] = graph[foundTextsForNgram[i]][foundTextsForNgram[j]]
            j+=1
         i+=1

globalHtmlFile.writelines("</ul>\n")



if viz=="graph":
   globalHtmlFile.writelines("""
<script>

var width = 960,
    height = 500;

var color = d3.scale.category20();

var force = d3.layout.force()
    .charge(-400)
    .linkDistance(100)
    .size([width, height]);

var svg = d3.select("#graph").append("svg")
    .attr("width", width)
    .attr("height", height);

var graph = {nodes:[],links:[]};
""");
   nodes = "["
   i=0
   for f in files:
      if i>0:
         nodes += ",\n"
      nodes += '{"name":"'+f+'","group":"1"}'
      i+=1
   nodes += "];"

   links = "["
   i=0
   first=1
   for lin in graph:
      j=0
      for c in lin:
         if j>i and c>=5 :
            if first != 1:
               links += ",\n"
            first = 0
            links += '{"source":'+str(i)+',"target":'+str(j)+',"value":'+str(c)+'}'
         j+=1
      i+=1
   links += "];"


   globalHtmlFile.writelines("graph.nodes = "+nodes+"\n")
   globalHtmlFile.writelines("graph.links = "+links+"\n")
   globalHtmlFile.writelines("""
   
   force
      .nodes(graph.nodes)
      .links(graph.links)
      .start();

  graph.links.forEach(function (d) {
    d.group = Math.floor(Math.random() * 6)
  });

  var link = svg.selectAll(".link")
      .data(graph.links)
    .enter().append("line")
      .attr("class", "link")
      .style("stroke-width", function(d) { return Math.sqrt(d.value); })
      .style("stroke", function(d) { return color(d.group); });

  var node = svg.selectAll(".node")
      .data(graph.nodes)
    .enter().append("circle")
      .attr("class", "node")
      .attr("r", 5)
      .style("fill", function(d) { return color(d.group); })
      .call(force.drag);

  node.append("title")
      .text(function(d) { return d.name; });

  force.on("tick", function() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
  });


</script>

""");







if viz=="chord":

   globalHtmlFile.writelines("""
<!-- Create a div where the graph will take place -->
<div id="my_dataviz"></div>

<div id="tooltip"></div>

<script>
// 
// https://www.d3-graph-gallery.com/graph/chord_interactive.html
// create the svg area
var svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", 1200)
    .attr("height", 1200)
  .append("g")
    .attr("transform", "translate(600,600)")

// create a matrix
var matrix = """)


   globalHtmlFile.writelines(str(graph))


   globalHtmlFile.writelines(""";

// 4 groups, so create a vector of 4 colors
var colors = [];// "#440154ff", "#31668dff", "#37b578ff", "#fde725ff", "#015444ff", "#668d31ff", "#b57837ff", "#e725fdff"];
""")

   globalHtmlFile.writelines("var names = "+str(files)+";\n")


   globalHtmlFile.writelines("""

// give this matrix to d3.chord(): it will calculates all the info we need to draw arc and ribbon
var res = d3.chord()
    .padAngle(0.05)
    .sortSubgroups(d3.descending)
    (matrix)

// add the groups on the outer part of the circle
svg
  .datum(res)
  .append("g")
  .selectAll("g")
  .data(function(d) { return d.groups; })
  .enter()
  .append("g")
  .append("path")
    .style("fill", function(d,i){ return colors[i] })
    .style("stroke", "black")
    .attr("d", d3.arc()
      .innerRadius(580)
      .outerRadius(590)
    )
    

// Add a tooltip div. Here I define the general feature of the tooltip: stuff that do not depend on the data point.
// Its opacity is set to 0: we don't see it by default.
var tooltip = d3.select("#my_dataviz")
  .append("div")
  .style("opacity", 0)
  .attr("class", "tooltip")
  .style("background-color", "white")
  .style("border", "solid")
  .style("border-width", "1px")
  .style("border-radius", "5px")
  .style("padding", "10px")

// A function that change this tooltip when the user hover a point.
// Its opacity is set to 1: we can now see it. Plus it set the text and position of tooltip depending on the datapoint (d)
var showTooltip = function(d) {
  tooltip
    .style("opacity", 1)
    .html(names[d.source.index] + " &lt;-&gt; " + names[d.target.index])
    .style("left", (d3.event.pageX + 15) + "px")
    .style("top", (d3.event.pageY - 28) + "px")
}

// A function that change this tooltip when the leaves a point: just need to set opacity to 0 again
var hideTooltip = function(d) {
  tooltip
    .transition()
    .duration(1000)
    .style("opacity", 0)
}



// Add the links between groups
svg
  .datum(res)
  .append("g")
  .selectAll("path")
  .data(function(d) { return d; })
  .enter()
  .append("path")
    .attr("d", d3.ribbon()
      .radius(580)
    )
    .style("fill", function(d){ return(colors[d.source.index]) }) // colors depend on the source group. Change to target otherwise.
    .style("stroke", "black")
  .on("mouseover", showTooltip )
  .on("mouseleave", hideTooltip );

</script>""")

globalHtmlFile.writelines("""
</body>
</html>""")

globalHtmlFile.close()

print(str(time.time()-startTime))