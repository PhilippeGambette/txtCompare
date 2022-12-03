import glob, os, re, sys, time
from io import open

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 30 second delay between each comparison
delay = 30

# start with part number 0
start = 0

if len(sys.argv)>1:
   mode = "aligned"
else:
   mode = "pairwise"

driver = webdriver.Firefox()
#assert "Python" in driver.title

folder = os.path.abspath(os.path.dirname(sys.argv[0]))

if mode == "pairwise":
   # Load all texts in the "files" folder contained in the same folder as this script
   files = []
   fileNames = []
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
   
# Compare files f1 and f2 using MEDITE and output the HTML code of a cell to add to the comparison table
def mediteComparison(f1,f2,file1String,file2String):
   global delay,start
   # Display the address of the files being treated
   print("Currently aligning file "+str(f1)+" with file "+str(f2)) 

   # Fill one cell in the table
   row = "<td><a href=\"./c-"+str(f1)+"-"+str(f2)+".html\">&#x1F500;</td>"
   
   if 25==25:
      # Load the MEDITE page
      driver.get("http://obvil.lip6.fr/medite/")
      elem1 = driver.find_element_by_id("etat1")
      elem2 = driver.find_element_by_id("etat2")

      # Load the two versions of the text
      elem1.clear()
      driver.execute_script('document.getElementById("etat1").value="'+file1String.replace('\n',"\\n").replace('"',"''")+'";')
      #elem1.send_keys(file1String)
      driver.execute_script('document.getElementById("etat2").value="'+file2String.replace('\n',"\\n").replace('"',"''")+'";')
      #elem2.send_keys(file2String)

      # Use character mode instead of word mode
      characterButton = driver.find_element_by_css_selector("#pcarOuMot")
      characterButton.click()
         
      # Start MEDITE by clicking the submit button
      submitButton = driver.find_element_by_css_selector("input[type=submit]")
      submitButton.click()
      time.sleep(delay)
            
      # Save the page built by MEDITE
      savePage(driver,os.path.join(folder,"c-"+str(f1)+"-"+str(f2)+".html"))
   return row


# Build an HTML index file
indexFile = open(os.path.join(folder,"index.html"),"w",encoding='utf-8')
indexFile.writelines("""<html><head><style>td{border: 1px solid black; text-align: center;}</style></head>
<body>
<table>
""")

if mode == "pairwise":
   # pairwise comparison: compare every file of fileNames with every other file of fileNames
   headRow = "<tr><th></th>"
   fileNb = 0
   for fileN in fileNames:
      if fileNb > 0:
         headRow += "<th>"+fileN+"</th>\n"
      fileNb += 1
   indexFile.writelines(headRow+"</tr>\n")

   # Start all pairwise comparisons with MEDITE
   for f1 in range(0,len(files)):
      row = "<th>"+fileNames[f1]+"</th>\n"
      for f2 in range(1,f1+1):
         row += "<td></td>\n"
   
      file1String = openFile(files[f1])
      for f2 in range(f1+1,len(files)):   
         file2String = openFile(files[f2])
         row += mediteComparison(f1,f2,file1String,file2String)

      if f1<len(files)-1:
         indexFile.writelines(row+"</tr>\n")
else:
   # linear comparison: compare every file starting with file1 followed by - and a number and .txt
   # with another file starting with file2 followed by - and the same number and .txt   
   fileNb = 0
   file1 = os.path.abspath(sys.argv[1])
   file2 = os.path.abspath(sys.argv[2])
   print("Comparing parts of "+file1+" with parts of "+file2)
   while os.path.isfile(file1+"-"+str(fileNb)+".txt"):
      print("Comparing parts "+str(fileNb))
      row = "<tr>\n<th>"+str(fileNb)+"</th>\n"
      file1String = openFile(file1+"-"+str(fileNb)+".txt")
      file2String = openFile(file2+"-"+str(fileNb)+".txt")
      row += mediteComparison(fileNb,fileNb,file1String,file2String)
      indexFile.writelines(row+"</tr>\n")
      fileNb += 1

indexFile.writelines("""
</table>
</body>""")
indexFile.close()      
driver.close()