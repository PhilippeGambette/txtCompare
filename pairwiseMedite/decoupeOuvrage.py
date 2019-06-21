#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-

import glob, os, re, sys

# On commence par stocker dans la variable folder l'adresse du dossier de ce programme :
folder = os.path.abspath(os.path.dirname(sys.argv[0]))

# On ouvre le fichier dont le nom est fourni en entrée
file = os.path.join(folder,sys.argv[1])
print("opening file "+file)
lines = open(file,"r",encoding="utf-8").readlines()

fileNb = 0;
# On crée un fichier avec le même nom suivi d'un préfixe 0.txt
output = open(file+"-"+str(fileNb)+".txt","w",encoding="utf-8")
for line in lines:
   # On cherche le caractère ¤
   res = re.search("^(.*)¤(.*)$",line)
   if res:
      output.writelines(res.group(1))
      output.close()
      print("Saving part "+str(fileNb))
      fileNb += 1
      output = open(file+"-"+str(fileNb)+".txt","w",encoding="utf-8")
      output.writelines(res.group(2)+"\r\n")
   else:
      output.writelines(line)
      
print("Saving part "+str(fileNb))
output.close()
