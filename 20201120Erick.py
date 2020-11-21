#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 23:30:39 2020
@author: maison
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine



# A modifier si l'on se connecte depuis MAME ou de l'exterieur
server = "127.0.0.1" 
BDname="grp_movies2" # Nom de la base de donnée
cnx = create_engine(f'mysql+pymysql://reader:Reader@2020@{server}/{BDname}').connect() # Il faut d'abord se connecter au serveur et à mysql sur le serveur avant d'effectuer la commande

print("\nBienvenue dans le moteur de recherche Sql dans la Base de données de IMDB")
# Construction du moteur de recherche sql de façon triangulaire avec comme base les requêtes sql et par couche de sous-menus avec à la pointe le menu principal  
# Placement de toute les fonction de requête sql à allimenter le moteur de recherche ie base du triangle
def t20():# Classement du top 20 des films
    sql1 = 'SELECT `title_basics`.primaryTitle,`title_ratings`.numVotes FROM `title_ratings`, `title_basics` WHERE `title_ratings`.tconst=`title_basics`.tconst ORDER BY numVotes DESC LIMIT 50;' 
    df1 = pd.read_sql(sql1, cnx)
    print(df1)

def crg():# Compte les films en fonction de leur region
    sql2 = 'SELECT COUNT(title), region FROM `title_akas` GROUP BY region' 
    df2 = pd.read_sql(sql2, cnx)
    print(df2)

def ddf():# Affiche le nom des films avec une durée supérieur à :
    time = input("Durée en min ? ")
    sql3 = 'SELECT primaryTitle, runtimeMinutes FROM `title_basics`  WHERE runtimeMinutes = "'+time+'"LIMIT 50;' 
    print("Films dont la durée est de:", time)
    df3 = pd.read_sql(sql3, cnx)
    print(df3)

def anaa():# Affiche les acteurs qui sont nés en :  années 
    year = input("Année ? ")
    sql4 ='SELECT primaryName FROM `name_basics` WHERE birthYear = "'+year+'" LIMIT 50;'  
    df4 = pd.read_sql(sql4, cnx)
    print(df4)
    
def lfja():# Affiche le nom des films où a jouer tel acteur 
    namefirstname1 = input("Prénom et nom de l'acteur : ")
    sql5 ='SELECT title_basics.primaryTitle AS titre, title_principals.category AS productor, name_basics.primaryName FROM name_basics INNER JOIN title_principals ON name_basics.nconst = title_principals.nconst INNER JOIN title_basics ON title_principals.tconst = title_basics.tconst  WHERE name_basics.primaryName = "'+namefirstname1+'" LIMIT 50;'
    df5 = pd.read_sql(sql5, cnx)
    print("Le nom des film ou a jouer"+namefirstname1+" sont :")
    print(df5)
    
def gfr():# Affiche le genre des films que le réalisateur a réalisé et trace le camembert représentant les proportions de sa réalisation 
    namefirstname2 = input("Prénon et nom du realisateur: ")
    sql6 = 'SELECT COUNT(PrimaryTitle), genre FROM film_genres INNER JOIN title_basics ON film_genres.tconst=title_basics.tconst INNER JOIN title_principals ON title_basics.tconst=title_principals.tconst INNER JOIN name_basics ON title_principals.nconst=name_basics.nconst WHERE primaryName = "'+namefirstname2+'" GROUP BY genre ORDER BY COUNT(PrimaryTitle) DESC LIMIT 10;' 
    df6 = pd.read_sql(sql6, cnx)
    print("Les genres de film réalisé par "+namefirstname2+" sont au nombre de :")
    print(df6)
    plt.pie(df6['COUNT(PrimaryTitle)'], startangle=90, autopct='%1.1f%%') 
    plt.suptitle("Proportion des genres de films réalisé par {}".format( namefirstname2))
    plt.legend(df6['genre'], title = "Genres de film", loc = "lower center", ncol = 5, framealpha = 0.20)
    plt.show() 
 
def gfj():# Affiche les genres de films où a jouer :
    namefirstname3 = input("Prénon et nom de l'acteur: ")
    sql7 = 'SELECT COUNT(PrimaryTitle), genre FROM film_genres INNER JOIN title_basics ON film_genres.tconst=title_basics.tconst INNER JOIN title_principals ON title_basics.tconst=title_principals.tconst INNER JOIN name_basics ON title_principals.nconst=name_basics.nconst WHERE primaryName = "'+namefirstname3+'" GROUP BY genre'
    df7 = pd.read_sql(sql7, cnx)
    print("Les genres de film joué par "+namefirstname3+" sont au nombre de :")
    print(df7)    
    
def Nmfp(): #  Affiche la note moyenne obtenue pour les films d'origine :
    Country = input("Quel pays voudriez vous savoir la note moyenne optenue ? ")
    sql8 = 'SELECT AVG(averageRating),region From  title_ratings INNER JOIN title_basics ON title_ratings.tconst = title_basics.tconst INNER JOIN title_akas ON title_basics.tconst = title_akas.titleId WHERE REGION = "'+Country+'";'
    df8 = pd.read_sql(sql8, cnx)
    print(df8)
    
def nsup():# Affiche la liste des films avec une note supérieur à :
    np = input("Rechercher les film dont la note est supérieur à : ")
    sql9 = 'SELECT title_basics.primaryTitle, title_ratings.averageRating FROM title_basics INNER JOIN title_ratings ON title_basics.tconst = title_ratings.tconst WHERE averageRating > "'+np+'" ORDER by averageRating DESC LIMIT 50;'
    print("Voici la liste des film dont la note est supérieur "+np+" sont :")
    df9 = pd.read_sql(sql9, cnx)
    print(df9)

def grfm():# Affiche les titres de films du genre : 
    gf = input("Rechercher les titre des films du genre : ")
    sql10 = 'SELECT primaryTitle,genre FROM title_basics INNER JOIN film_genres ON title_basics.tconst = film_genres.tconst Where genre ="'+gf+'"LIMIT 50 ;'
    print("Voici la liste des film du genre  "+gf+" sont : ")
    df10 = pd.read_sql(sql10, cnx)
    print(df10)

def cfg():# Affiche le nombre de genre de films que à réalisé puis trace le diagramme en barre associé à cette recherche: 
    sql11 = 'SELECT  genre, COUNT(tconst) FROM film_genres GROUP BY genre ORDER BY COUNT(tconst) DESC LIMIT 20;'    
    print("Voici le nombre de film par genre :")
    df11 = pd.read_sql(sql11, cnx)
    print(df11)
    sns.barplot(x="COUNT(tconst)", y="genre", data=df11)
    plt.suptitle("Graphe représentant le nombre de film en fonction de son genre")
    # Faut quitter le moteur de recherche pour afficher le graphe
    
def lf():# Affiche les langues du film :
    lfm = input("Quel film voudriez-vous savoir les langues ? ")
    sql12='SELECT language FROM `title_akas` WHERE title="'+lfm+'"LIMIT 50;'    
    df12 = pd.read_sql(sql12, cnx)
    print(df12)
def npd(): # Affiche le nom des films que ... a réalisé  
    nfpd = input("Quel réalisateur voudriez vous voir le nom des film qu'il a produit ? ")
    sql13= 'SELECT title_basics.primaryTitle AS titre, title_principals.category AS productor, name_basics.primaryName FROM name_basics INNER JOIN title_principals ON name_basics.nconst = title_principals.nconst INNER JOIN title_basics ON title_principals.tconst = title_basics.tconst  WHERE name_basics.primaryName = "'+nfpd+'" LIMIT 50;'
    df13 = pd.read_sql(sql13, cnx)
    print(df13)
    
    
# Placement des sous menus du moteur de recherche qui correspond à une fonction spécifique
# Premiere sous-couche menu
def Gnr():
    sortir = False
    option = 0
    while not sortir:
        print("Film / Genre")
        print("""
    Vous souhaitez rechercher :
    
    1)les films du genre :
    2)Combien il y a t'il de film par genre ?
    """)
        
        option = demander_nombre_entier()
     
        if option == 1:
            return grfm()    
        elif option == 2:
            return cfg()
        elif option ==0:
            return Flm()
        else:
            print('')
            print ("Choississez soit 1 ou 2")
            
def Ntn():
    sortir = False
    option = 0
    while not sortir:
        print("Film / Notation")
        print("""
    Vous souhaitez rechercher :
    
    1)Nom des films avec une notation supérieur à :
    2)Notation moyenne des films suivant un pays
    3)Top 20
    """)
            
        option = demander_nombre_entier()
     
        if option == 1: 
            return nsup()      
        elif option == 2:
            return Nmfp() # a remplacer
        elif option == 3:
            return t20()
        elif option ==0:
            return Flm()
        else:
            print('')
            print ("Entrez un nombre compris entre 1 et 3")
            
def Atr():
    sortir = False
    option = 0
    while not sortir:
        print("Film / Autre")
        print("""
    Vous souhaitez rechercher:
    
    1)Le Nombre de film par region
    2)Quelle sont les langues du film :
    3)Durée des films            
            """)
       
        option = demander_nombre_entier()
     
        if option == 1:
            return crg() 
        elif option == 2:
            return lf()
        elif option == 3:
            return ddf()    
        elif option ==0:
            return Flm()
        else:
            print('')
            print ("Entrez un nombre compris entre 1 et 3 ") 
            
def Director():
    sortir = False
    option = 0
    while not sortir:
        print("Personne lie au film / Réalisateur")
        print("""
    Vous souhaitez rechercher par:
    
    1)Genre de film réalisé par
    2)Nom des films réalisé par   
            """)
        
        option = demander_nombre_entier()
        
        if option ==1:
            return gfr()    
        elif option ==2:
            return npd()
        elif option ==0:
            return Plf()
        else:
             print('')
             print ("Choississez soit 1 ou 2 ")
                    
                    
def Actor():
    sortir = False
    option = 0
    while not sortir:
        print("Personne lie au film / Acteur")
        print("""
    Vous souhaitez rechercher par:
    
    1)Quel sont les acteurs né après tels années ?
    2)Genre de films où a jouer:
    3)Nom des films où a jouer :            
            """)
        
        option = demander_nombre_entier()
        
        if option ==1:
            return anaa()    
        elif option ==2:
            return gfj()    
        elif option ==3:
            return lfja()
        elif option ==0:
            return Plf()
        
        else:
             print('')
             print ("Entrez un entier compris entre 1 et 3")
             
#Deuxième sous-couche menu
            
def Flm():
    sortir = False
    option = 0
    while not sortir:
        print("Film")
        print("""
    Vous souhaitez rechercher par:
    
    1)Genre
    2)Notation
    3)Autre                 
            """)
        
        option = demander_nombre_entier()
     
        if option == 1:
            return Gnr()     
        elif option == 2:
            return Ntn()    
        elif option ==3:
            return Atr()    
        elif option ==0:
            return section_principale()
        
        else:
            print('')
            print ("Entrez un nombre compris entre 1 et 3")

          

def Plf():
    sortir = False
    option = 0
    while not sortir:       
        print("Personne lie au film")
        print("""
    Vous souhaitez rechercher par:
    
    1)Réalisateur
    2)Acteur ou actrice
    """)
        
        option = demander_nombre_entier()
        
        if option ==1:
            return Director()
        elif option ==2:
            return Actor() 
        elif option ==0:
            return section_principale()
        
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
        print('')
        print("A tout moment vous pouvez utiliser 0 pour retourner")
        option = demander_nombre_entier()
     
        if option == 1:
            Flm()  # exécuter la fonction pour la sélection de type 
            autre_rech = input('Voulez-vous faire une autre recherche?(o/n) ')
            if autre_rech == "o":
                section_principale()
                
            else:
                sortir = True   
        elif option == 2:
            Plf()
            autre_rech = input('Voulez-vous faire une autre recherche?(o/n) ')# On lance à nouveau la première recherche en utilisant la fonction section_principale()
            if autre_rech == "o":
                section_principale()    
            else:
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