#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:26:23 2020

@author: formateur
"""

#imports
import pandas as pd
from sqlalchemy import create_engine
import config

server = "127.0.0.1" 
#server = "datalab-mame.myconnectech.fr"
BDname="grp_movies2"

# connection à mySQL sur le serveur
cnx = create_engine('mysql+pymysql://' + config.user + ':' + config.password + '@' + server + '/' + BDname).connect()
 
print("Recherche dans la BDD")

def Top_20():

    sql = 'SELECT `title_basics`.primaryTitle,`title_ratings`.numVotes FROM `title_ratings`, `title_basics` WHERE `title_ratings`.tconst=`title_basics`.tconst ORDER BY numVotes DESC LIMIT 20;' 

    print("SQL:", sql)

    # Execution de la requète & récupération dans une dataFrame (pandas)
    df = pd.read_sql(sql, cnx)
    print(df)

def ne_dans_lannée():
    # Il est nécessaire de modifier ce code pour ne montrer que les acteurs, 
    # actuellement il montre tous les personnages qui sont nés cette année-là
 
    sql2 = 'SELECT DISTINCT birthYear FROM name_basics ORDER BY `name_basics`.`birthYear` ASC;' 

    # Execution de la requète & récupération dans une dataFrame (pandas)
    df2 = pd.read_sql(sql2, cnx)
    print(df2)
    
    
    # demande de taper la valeur
    title = input("year? ")

    print("vous avez tapé:", title)

    sql = 'SELECT primaryName FROM `name_basics` WHERE birthYear ="' + title + '";' 

    print("SQL:", sql)

    # Execution de la requète & récupération dans une dataFrame (pandas)
    df = pd.read_sql(sql, cnx)
    print(df)








def demander_nombre_entier():
 
    correct=False
    num=0
    while(not correct):
        try:
            num = int(input("Choisissez le nombre d'une option: "))
            correct=True
        except ValueError:
            print('vous devez entrer un nombre entier')
     
    return num
 
sortir = False
option = 0
 
while not sortir:

    print("""
    1) Top 20 des films les mieux notés
    2) Acteurs nés dans l'année:
    3) Genre
    4) Sortir
    """)
 
    option = demander_nombre_entier()
 
    if option == 1:
        Top_20()
        sortir = True
    elif option == 2:
        ne_dans_lannée()
        sortir = True
    elif option == 3:
        print("Lancer la recherche SQL 3")
        sortir = True
    elif option == 4:
        sortir = True
    else:
        print ("Entrez un nombre entre 1 et 3")
 
print ("Fin")