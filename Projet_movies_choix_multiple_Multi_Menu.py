#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 23:30:39 2020

@author: maison
"""
import pandas as pd
import matplotlib.pyplot as plt


from sqlalchemy import create_engine
import IdentifiantServeurDataLab

server = "127.0.0.1" 
BDname="grp_movies2"
cnx = create_engine('mysql+pymysql://' + IdentifiantServeurDataLab.user + ':' + IdentifiantServeurDataLab.password + '@' + server + '/' + BDname).connect() # Il faut d'abord se connecter au serveur et à mysql sur le serveur avant d'effectuer la commande

print("Bienvenue dans le moteur de recherche Sql dans la Base de données de INDB")
#Construction du moteur de recherche sql de façon triangulaire avec comme base les requêtes sql et par couche de sous-menus avec à la pointe le menu principal  
#Placement de toute les fonction de requête sql à allimenter le moteur de recherche ie base du triangle
def t20():
    sql1 = 'SELECT `title_basics`.primaryTitle,`title_ratings`.numVotes FROM `title_ratings`, `title_basics` WHERE `title_ratings`.tconst=`title_basics`.tconst ORDER BY numVotes DESC LIMIT 50;' 
    df1 = pd.read_sql(sql1, cnx)
    print(df1)

def crg():

    sql2 = 'SELECT COUNT(title), region FROM `title_akas` GROUP BY region'
    df2 = pd.read_sql(sql2, cnx)
    print(df2)

def ddf(): 
    time = input("duree en min ?")
    sql3 = 'SELECT primaryTitle, runtimeMinutes FROM `title_basics`  WHERE runtimeMinutes = "'+time+'"LIMIT 50;'
    print("Films dont la durée est de:", time)
    df3 = pd.read_sql(sql3, cnx)
    print(df3)

def anaa():
    year = input("année ?")
    sql4 ='SELECT primaryName FROM `name.basics` WHERE birthYear = "'+year+'" LIMIT 50;'   
    df4 = pd.read_sql(sql4, cnx)
    print(df4)
    
def lfja():
    namefirstname1 = ("nom et prénoms de l'acteur")
    sql5 =''# requete sql pour aller chercher le nom des films où a jouer tel acteur 
    df5 = pd.read_sql(sql5, cnx)
    print("Le nom des film ou a jouer"+namefirstname1+" sont :")
    print(df5)
    
def gfr(): 
    namefirstname2 = input("prénon et nom du realisateur:")
    sql6 = 'SELECT COUNT(PrimaryTitle), genre FROM film_genres INNER JOIN title_basics ON film_genres.tconst=title_basics.tconst INNER JOIN title_principals ON title_basics.tconst=title_principals.tconst INNER JOIN name_basics ON title_principals.nconst=name_basics.nconst WHERE primaryName = "'+namefirstname2+'" GROUP BY genre'
    df6 = pd.read_sql(sql6, cnx)
    print("Les genres de film réalisé par "+namefirstname2+" sont au nombre de :")
    print(df6)
    plt.pie(df6['COUNT(PrimaryTitle)'], startangle=90, autopct='%1.1f%%') # représentation du camembert avec comme argument : la colonne des valeurs associé à chaque catégorie, label qui représente les différentes catégories à représenté,colors : code  couleur de chaque catégorie, explode : permet de séparer une catégorie du camembert, autopct : permet de convertir les valeurs des catégories à représenter en pourcentage
    plt.suptitle("Proportion des genres de films réalisé par {}".format( namefirstname2))
    plt.legend(df6['genre'], title = "Genres de film", loc="best")
    plt.show() 
 
def gfj():
    namefirstname3 = input("prénon et nom de l'acteur:")
    sql7 = 'SELECT COUNT(PrimaryTitle), genre FROM film_genres INNER JOIN title_basics ON film_genres.tconst=title_basics.tconst INNER JOIN title_principals ON title_basics.tconst=title_principals.tconst INNER JOIN name_basics ON title_principals.nconst=name_basics.nconst WHERE primaryName = "'+namefirstname3+'" GROUP BY genre'
    df7 = pd.read_sql(sql8, cnx)
    print("Les genres de film joué par "+namefirstname3+" sont au nombre de :")
    print(df7)    
    
def nfg(): # problème de syntaxe
    sql8 = 'SELECT genre, AVG(averageRating) FROM title_ratings INNER JOIN  title_basics IN title_ratings.tconst = title_basics.tconst INNER JOIN film_genres IN title_basics.tconst = film_genres.tconst GROUP BY genre;'
    df8 = pd.read_sql(sql8, cnx)
    print(df8)
    
def nsup():  
    np = input("Rechercher les film dont la note est supérieur à :")
    sql9 = 'SELECT title_basics.primaryTitle, title_ratings.averageRating FROM title_basics INNER JOIN title_ratings ON title_basics.tconst = title_ratings.tconst WHERE averageRating > "'+np+'" ORDER by averageRating DESC LIMIT 50;'
    print("Voici la liste des film dont la note est supérieur "+np+" sont :")
    df9 = pd.read_sql(sql9, cnx)
    print(df9)

def grfm(): 
    gf = input("Rechercher les titre des films du genre  :")
    sql10 = 'SELECT primaryTitle,genre FROM title_basics INNER JOIN film_genres ON title_basics.tconst = film_genres.tconst Where genre ="'+gf+'"LIMIT 50 ;'
    print("Voici la liste des film du genre  "+gf+" sont :")
    df10 = pd.read_sql(sql10, cnx)
    print(df10)

def cfg(): # graphe qui ne se trace pas ?
    sql11 = 'SELECT  genre, COUNT(tconst) FROM film_genres GROUP BY genre ORDER BY COUNT(tconst) ;'    
    print("Voici le nombre de film par genre :")
    df11 = pd.read_sql(sql11, cnx)
    print(df11)
    
    
    
def lf():
    lfm = input("Quel film voudriez-vous savoir les langues ?")
    sql12='SELECT language FROM `title_akas` WHERE title="'+lfm+'"LIMIT 50;'    
    df12 = pd.read_sql(sql12, cnx)
    print(df12)
def npd():   
    nfpd = input("Quel réalisateur voudriez vous voir le nom des film qu'il a produit ?")
    sql13= 'SELECT title_basics.primaryTitle AS titre, title_principals.category AS productor, name_basics.primaryName FROM name_basics INNER JOIN title_principals ON name_basics.nconst = title_principals.nconst INNER JOIN title_basics ON title_principals.tconst = title_basics.tconst  WHERE name_basics.primaryName = "'+nfpd+'" LIMIT 50;'
    df13 = pd.read_sql(sql13, cnx)
    print(df13)
    
    
# Placement des sous menus du moteur de recherche qui correspond à une fonction spécifique
# Premiere sous couche
def Gnr():
    sortir = False
    option = 0
    while not sortir:
        print("""
    Vous souhaitez rechercher :
    
    1)les films du genre :
    2)Combien il y a t'il de film par genre ?
    """)
        option = demander_nombre_entier()
     
        if option == 1:
            grfm() 
            sortir = True     
        elif option == 2:
            cfg()
            sortir = True
        else:
            print('')
            print ("Choississez soit 1 ou 2")
            
def Ntn():
    sortir = False
    option = 0
    while not sortir:
        print("""
    Vous souhaitez rechercher :
    
    1)Nom des film avec une notation supérieur à :
    2)Notation moyenne des films par genre
    3)Top 20
    """)
        option = demander_nombre_entier()
     
        if option == 1: 
            nsup() 
            sortir = True      
        elif option == 2:
           nfg()
           sortir = True
        elif option == 3:
            t20()
            sortir = True
        else:
            print('')
            print ("Entrez un nombre compris entre 1 et 3")
            
def Atr():
    sortir = False
    option = 0
    while not sortir:
        print("""
    Vous souhaitez rechercher:
    
    1)Le Nombre de film par region
    2)Quelle sont les langues du film :
    3)Durée des films
                 
            """)
        option = demander_nombre_entier()
     
        if option == 1:
            crg() 
            sortir = True  
        elif option == 2:
            lf()
            sortir = True 
        elif option == 3:
            ddf()
            sortir = True    
        else:
            print('')
            print ("Entrez un nombre compris entre 1 et 3 ") 
            
def Director():
    sortir = False
    option = 0
    while not sortir:
        print("""
    Vous souhaitez rechercher par:
    
    1)Genre de film réalisé par
    2)Nom des films réalisé par
                
            """)
        option = demander_nombre_entier()
        
        if option ==1:
            gfr()
            sortir = True    
        elif option ==2:
            npd()
            sortir = True
        else:
             print('')
             print ("Choississez soit 1 ou 2 ")
                    
                    
def Actor():
    sortir = False
    option = 0
    while not sortir:
        print("""
    Vous souhaitez rechercher par:
    
    
    1)Quel sont les acteurs né après tels années ?
    2)Genre de films où a jouer:
    3)Nom des films où a jouer :            
            """)
        option = demander_nombre_entier()
        
        if option ==1:
            anaa()
            sortir = True     
        elif option ==2:
            gfj()
            sortir = True     
        elif option ==3:
            lfja()
            Sortir = True
        else:
             print('')
             print ("Entrez un entier compris entre 1 et 3")
             
#Deuxième sous couche menu
            
def Flm():
    sortir = False
    option = 0
    while not sortir:
        print("""
    Vous souhaitez rechercher par:
    
    1)Genre
    2)Notation
    3)Autre
                 
            """)
        option = demander_nombre_entier()
     
        if option == 1:
            
            Gnr() 
            sortir = True    
        elif option == 2:
            Ntn()
            sortir = True    
        elif option ==3:
            Atr()
            sortir = True     
        else:
            print('')
            print ("Entrez un nombre compris entre 1 et 3")

          

def Plf():
    sortir = False
    option = 0
    while not sortir:
        print("""
    Vous souhaitez rechercher par:
    
    1)Réalisateur
    2)Acteur ou actrice
    """)
        option = demander_nombre_entier()
        
        if option ==1:
            Director()
            sortir = True    
        elif option ==2:
            Actor()
            sortir = True 
        elif option ==2:
            Other()
            sortir = True
        else:
             print('')
             print ("Entrez un entier compris entre 1 et 3")
             
# Moteur de recherche principal ie sommet du triangle

def section_principale(): 
    sortir = False
    option = 0
    while not sortir:
        print("""
    Vous souhaitez rechercher par:
    
    1)Film
    2)Personne lie au film             
            """)
        option = demander_nombre_entier()
     
        if option == 1:
            print("Film")
            Flm()  #exécuter la fonction pour la sélection de type 
            autre_rech = input('Voulez-vous faire une autre recherche?(o/n) ')
            if autre_rech == "o":
                section_principale()
                #Je lance à nouveau la première recherche en utilisant la fonction section_principale()
            else:
                sortir = True   
        elif option == 2:
            print("Personne lie au film")
            Plf()
            autre_rech = input('Voulez-vous faire une autre recherche?(o/n) ')
            if autre_rech == "o":
                section_principale()#Je lance à nouveau la première recherche en utilisant la fonction section_principale()    
            else:
                sortir = True
            
            sortir = True
            
            
        else:
            print('')
            print ("Choississez soit 1 où 2")
            

# Selecteur des sous menus ou des requêtes sqls à effectuer utiliser dans l'ensemble de moteur de recherche
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
            
section_principale()

print("Merci beaucoup d'utiliser notre service de recherche de films spécialisés. Nous espérons que vous avez eu une expérience agréable.")
