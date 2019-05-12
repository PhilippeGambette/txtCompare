import glob, os, re, sys
from io import open

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
#assert "Python" in driver.title


# Load all texts in the "files" folder contained in the same folder as this script
files = []
fileNames = []
folder = os.path.abspath(os.path.dirname(sys.argv[0]))
for file in glob.glob(os.path.join(folder,os.path.join("files","*.txt"))):
   files.append(file)
   fileNames.append(file)

"""
##################################
# Load texts in the "files" folder contained in the same folder as this script
# in a specific order specified below
fileNames = [
"65-Manuscrit1511.txt",
"65-Manuscrit1512.txt",
"65-Manuscrit1515.txt",
"65-Manuscrit1517.txt",
"65-Manuscrit2155.txt",
"65-BoiastuauGilles1558.txt",
"65-GrugetPrevost1559.txt",
"65-Berne1781.txt",
"65-Delahays1858.txt",
"65-Garnier1862.txt",
"65-Liseux1879.txt",
"65-Eudes1880.txt",
"65-Jouaust1880.txt",
"65-GfFlammarion1982.txt",
"65-Bibliopolis1999.txt"
]
files = []

for fileN in fileNames:
   files.append(os.path.join(folder,os.path.join("files",fileN)))
##################################
"""

def openFile(file):
   file = open(file,"r",encoding='utf-8')
   fileString = ""
   for line in file:
      fileString += line
   return fileString

def savePage(browser,file):
   file = open(file,"w",encoding='utf-8')
   file.write(browser.page_source)
   file.close()

# Build an HTML index file
indexFile = open(os.path.join(folder,"index.html"),"w",encoding='utf-8')
indexFile.writelines("<html><head><style>td{border: 1px solid black; text-align: center;}</style></head><body><table>\n")
headRow = "<tr><th></th>"
fileNb = 0
for fileN in fileNames:
   if fileNb > 0:
      headRow += "<th>"+fileN+"</th>"
   fileNb += 1
indexFile.writelines(headRow+"</tr>\n")

# Start all pairwise comparisons with MEDITE
for f1 in range(0,len(files)):
   row = "<th>"+fileNames[f1]+"</th>"
   for f2 in range(1,f1+1):
      row += "<td></td>"
   
   file1String = openFile(files[f1])
   for f2 in range(f1+1,len(files)):   
      # Display the address of the files being treated
      print("Currently aligning file "+fileNames[f1]+" with file "+fileNames[f2]) 
      
      # Fill one cell in the table
      row += "<td><a href=\"./c-"+str(f1)+"-"+str(f2)+".html\">&#x1F500;</td>"

      # Load the MEDITE page
      driver.get("http://obvil.lip6.fr/medite/")
      elem1 = driver.find_element_by_id("etat1")
      elem2 = driver.find_element_by_id("etat2")
      
      file2String = openFile(files[f2])

      # Load the two versions of the text
      elem1.clear()
      elem1.send_keys(file1String)
      elem2.clear()
      elem2.send_keys(file2String)
      
      # Start MEDITE by clicking the submit button
      submitButton = driver.find_element_by_css_selector("input[type=submit]")
      submitButton.click()
           
      # Save the page built by MEDITE
      savePage(driver,os.path.join(folder,"c-"+str(f1)+"-"+str(f2)+".html"))

   if f1<len(files)-1:
      indexFile.writelines(row+"</tr>\n")

indexFile.writelines("</table></body>")
indexFile.close()      
driver.close()