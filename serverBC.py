#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, json, re
os.system("clear")

from flask import Flask
app = Flask(__name__)
app._static_folder = os.path.abspath("./")
   
@app.route('/')  # route qui renvoie la page HTML recherche_1.html
def recherche_1():
   print('/')
   if os.path.isfile("recherche_1.html") :
       return app.send_static_file("recherche_1.html")
   return "recherche_1.html non accessible"

@app.route('/recherche/<criteres>')
def recherche_critere(criteres):
   print("/recherche/"+criteres)
   listecriteres = criteres.split(" ")
   liste = os.listdir("Especes")
   lignes = []
   for critere in listecriteres :
      if len(critere) == 0 :
         continue
      for fichier in liste :
         fd = open("Especes/"+fichier)
         for ligne in fd.readlines() :
            res = re.search(str(critere), ligne, re.IGNORECASE                                                     )        
            if res :
               lignes.append([fichier, ligne])  # Le nom de la page est envoyée avant la ligne dans une sous-liste

   return json.dumps(lignes)

app.run()
#app.run(host="127.0.0.1", port=6000)
