#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 23:30:39 2020
@author: Groupe 2 / Eric Domas, Julien Garcia, Xavier Boué, César Parra
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine



# A modifier si l'on se connecte depuis MAME ou de l'exterieur
server = "127.0.0.1" 
BDname="grp_movies2" # Nom de la base de données
cnx = create_engine(f'mysql+pymysql://reader:Reader@2020@{server}/{BDname}').connect() # Il faut d'abord se connecter au serveur et à mysql sur le serveur avant d'effectuer la commande

# Construction du moteur de recherche sql de façon triangulaire avec comme base les requêtes sql et par couche de sous-menus avec à la pointe le menu principal  
# Placement de toutes les fonctions de requêtes sql à alimenter le moteur de recherche ie base du triangle

def t20():# Classement du top 20 des films  
    sql1 = 'SELECT primaryTitle AS Nom, averageRating AS Rating \
    FROM mieux_notes_movie \
    ORDER BY averageRating DESC \
    LIMIT 20;'
    
    #print("\nSQL1:", sql1)
    df1 = pd.read_sql(sql1, cnx)
    print(df1)

def crg():# Compte les films en fonction de leur region
    sql2 = 'SELECT COUNT(title), region FROM `title_akas` GROUP BY region' 
    
    #print("\nSQL2:", sql2)
    df2 = pd.read_sql(sql2, cnx)
    print(df2)

def ddf():# Affiche le nom des films avec une durée supérieure à :
    time = input("Durée en min ? ")
    
    sql3 = 'SELECT primaryTitle, runtimeMinutes \
    FROM `title_basics`  \
    WHERE runtimeMinutes = "'+time+'" \
    LIMIT 50;'
    
    #print("\nSQL3:", sql3)
    print("Films dont la durée est de:", time)
    df3 = pd.read_sql(sql3, cnx)
    print(df3)

def anaa():# Affiche les acteurs qui sont nés en :  années 
    year = input("Année ? ")
    
    sql4 ='SELECT primaryName \
    FROM `name_basics` \
    WHERE birthYear = "'+year+'" \
    LIMIT 50;'
    
    #print("\nSQL4:", sql4)
    df4 = pd.read_sql(sql4, cnx)
    print(df4)
    
def lfja():# Affiche le nom des films où a joué tel acteur 
    namefirstname1 = input("Prénom et nom de l'acteur : ")
    
    sql5 ='SELECT title_basics.primaryTitle AS titre, title_principals.category AS productor, name_basics.primaryName \
    FROM name_basics \
    INNER JOIN title_principals ON name_basics.nconst = title_principals.nconst \
    INNER JOIN title_basics ON title_principals.tconst = title_basics.tconst  \
    WHERE name_basics.primaryName = "'+namefirstname1+'" \
    LIMIT 50;'
    
    #print("\nSQL5:", sql5)
    df5 = pd.read_sql(sql5, cnx)
    print("Le nom des films où a joué"+namefirstname1+" sont :")
    print(df5)
    
def gfr():# Affiche le genre des films que le réalisateur a réalisé et trace le camembert représentant les proportions de ses réalisations 
    namefirstname2 = input("Prénom et nom du realisateur: ")
    
    sql6 = 'SELECT COUNT(PrimaryTitle), genre \
    FROM film_genres \
    INNER JOIN title_basics ON film_genres.tconst=title_basics.tconst \
    INNER JOIN title_principals ON title_basics.tconst=title_principals.tconst \
    INNER JOIN name_basics ON title_principals.nconst=name_basics.nconst \
    WHERE primaryName = "'+namefirstname2+'" \
    GROUP BY genre \
    ORDER BY COUNT(PrimaryTitle) DESC \
    LIMIT 10;' 
    
    #print("\nSQL6:", sql6)
    df6 = pd.read_sql(sql6, cnx)
    print("Les genres de film réalisé par "+namefirstname2+" sont au nombre de :")
    print(df6)
    plt.pie(df6['COUNT(PrimaryTitle)'], startangle=90, autopct='%1.1f%%') 
    plt.suptitle("Proportion des genres de films réalisé par {}".format( namefirstname2))
    plt.legend(df6['genre'], title = "Genres de film", loc = "lower center", ncol = 5, framealpha = 0.20)
    plt.show() 
 
def gfj():# Affiche les genres de films où a joué :
    namefirstname3 = input("Prénom et nom de l'acteur: ")
    
    sql7 = 'SELECT COUNT(PrimaryTitle), genre \
    FROM film_genres \
    INNER JOIN title_basics ON film_genres.tconst=title_basics.tconst \
    INNER JOIN title_principals ON title_basics.tconst=title_principals.tconst \
    INNER JOIN name_basics ON title_principals.nconst=name_basics.nconst \
    WHERE primaryName = "'+namefirstname3+'" \
    GROUP BY genre'
    
    #print("\nSQL7:", sql7)
    df7 = pd.read_sql(sql7, cnx)
    print("Les genres de films joués par "+namefirstname3+" sont au nombre de :")
    print(df7)    
    
def Nmfp(): #  Affiche la Notation d'un film spécifique
    film2 = input("Quel est le nom du film ? ")
    
    sql8 = f"SELECT B.primaryTitle AS Nom,  R.averageRating AS Rating, B.startYear AS Année \
    From title_basics AS B \
    INNER JOIN title_ratings AS R ON B.tconst = R.tconst \
    WHERE MATCH(B.primaryTitle) AGAINST ('{film2}') AND B.titleType = 'movie' \
    ORDER BY R.averageRating DESC \
    LIMIT 20"
    
    #print("\nSQL8:", sql8)
    df8 = pd.read_sql(sql8, cnx)
    print(df8)
    
def nsup():# Affiche la liste des films avec une note supérieure à :
    np = input("Rechercher les films dont la note est supérieure à : ")
    
    sql9 = 'SELECT title_basics.primaryTitle, title_ratings.averageRating \
    FROM title_basics \
    INNER JOIN title_ratings ON title_basics.tconst = title_ratings.tconst \
    WHERE averageRating > "'+np+'" \
    ORDER by averageRating DESC \
    LIMIT 50;'
    
    #print("\nSQL9:", sql9)
    print("La liste des films dont la note est supérieure à "+np+" est :")
    df9 = pd.read_sql(sql9, cnx)
    print(df9)

def grfm():# Affiche les titres de films du genre : 
    gf = input("Rechercher les titre des films du genre : ")
    
    sql10 = 'SELECT primaryTitle,genre \
    FROM title_basics \
    INNER JOIN film_genres ON title_basics.tconst = film_genres.tconst \
    Where genre ="'+gf+'" \
    LIMIT 50 ;'
    
    #print("\nSQL10:", sql10)
    print("La liste des films du genre  "+gf+" est : ")
    df10 = pd.read_sql(sql10, cnx)
    print(df10)

def cfg():#  Affiche le nombre de genres de films réalisés puis trace le diagramme en barre associé à cette recherche:  #***********
    sql11 = 'SELECT  genre, COUNT(tconst) \
    FROM film_genres \
    GROUP BY genre \
    ORDER BY COUNT(tconst) DESC \
    LIMIT 20;'
    
    #print("\nSQL11:", sql11)
    print("Voici le nombre de films par genre :")
    df11 = pd.read_sql(sql11, cnx)
    print(df11)
    sns.barplot(x="COUNT(tconst)", y="genre", data=df11)
    plt.suptitle("Graphe représentant le nombre de films en fonction de son genre")
    # Il faut quitter le moteur de recherche pour afficher le graphe
    
def lf():# Affiche les langues du film :
    lfm = input("De quel film voudriez-vous cannaître les langues ? ")
    
    sql12='SELECT DISTINCT language \
    FROM `title_akas` \
    WHERE title="'+lfm+'" \
    ORDER BY language DESC \
    LIMIT 50;'
    
    #print("\nSQL12:", sql12)
    df12 = pd.read_sql(sql12, cnx)
    print(df12)
    
def npd(): # Affiche le nom des films que ... a réalisé  
    nfpd = input("De quel réalisateur voudriez vous voir le nom des films produits ? ")
    
    sql13= 'SELECT title_basics.primaryTitle AS titre, title_principals.category AS productor, name_basics.primaryName \
    FROM name_basics \
    INNER JOIN title_principals ON name_basics.nconst = title_principals.nconst \
    INNER JOIN title_basics ON title_principals.tconst = title_basics.tconst \
    WHERE name_basics.primaryName = "'+nfpd+'" \
    LIMIT 50;'
    
    #print("\nSQL13:", sql13)
    df13 = pd.read_sql(sql13, cnx)
    print(df13)

def t20tt(): # Affiche Top 20 de tous les titres
    sql14 = 'SELECT primaryTitle AS Nom, averageRating AS Rating , titleType AS Type \
    FROM mieux_notes_tout \
    ORDER BY averageRating DESC \
    LIMIT 20;'
    
    #print("\nSQL14:", sql14)
    df8 = pd.read_sql(sql14, cnx)
    print(df8)

def t20te(): # Affiche Top 20 d'un type de titre spécifique
    print("Film / Notation / Top 20 d'un type de titre spécifique")
    print("""
    Quel type de titre souhaitez-vous rechercher?
        
    1) short       5) tvEpisode         9) videoGame
	2) tvShort     6) tvMiniSeries
	3) tvMovie     7) tvSpecial
	4) tvSeries    8) video
    """)
    
    list_type = ['short', 'tvShort', 'tvMovie', 'tvSeries', 'tvEpisode', 'tvMiniSeries', 'tvSpecial', 'video', 'videoGame']
    type1 = demander_nombre_entier()
    
    if type1 < 0 or type1 > 9:
        print ("Entrez un nombre compris entre 1 et 9")
    elif type1 == 0:
        Ntn()
    else:
        print (f"Film / Notation / Top 20 d'un type de titre spécifique / {list_type[type1-1]}")
        
        # Ici, nous utilisons des vues pour faciliter cette recherche
        sql15= f'SELECT primaryTitle AS Nom, averageRating AS Rating FROM mieux_notes_{list_type[type1-1]} ORDER BY averageRating DESC LIMIT 20;'
        #print("\nSQL15:", sql15)
        df13 = pd.read_sql(sql15, cnx)
        print(df13)

def t20ae(): # Affiche 20 meilleurs films d'une année spécifique de sortie
    print ("Film / Notation / 20 meilleurs films d'une année spécifique de sortie")
    year = input("Année ? ")
    sql16= f"SELECT primaryTitle, averageRating FROM \
    (SELECT `title_basics`.primaryTitle, `title_ratings`.averageRating, `title_ratings`.numVotes \
    FROM `title_ratings` \
    INNER JOIN `title_basics` ON `title_ratings`.tconst = `title_basics`.tconst \
    WHERE  `title_basics`.startYear = {year} AND `title_basics`.titleType = 'movie' \
    ORDER BY numVotes DESC \
    LIMIT 100) AS uno ORDER BY averageRating DESC \
    LIMIT 20;"

    #print("\nSQL16:", sql16)
    df16 = pd.read_sql(sql16, cnx)
    print(df16)

   
# Placement des sous menus du moteur de recherche qui correspondent à une fonction spécifique

# Premiere sous-couche menu
def Gnr():
    sortir = False
    option = 0
    while not sortir:
        print("Film / Genre")
        print("""
    Vous souhaitez rechercher :
    
    1) les films du genre :
    2) Combien y-a-t'il de films par genre ?
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
            print ("Choississez 1 ou 2")
            
def Ntn():
    sortir = False
    option = 0
    while not sortir:
        print("Film / Notation")
        print("""
    Vous souhaitez rechercher :
    
    1) 20 meilleurs films
    2) Top 20 de tous les titres
    3) Top 20 d'un type de titre spécifique
    4) 20 meilleurs films d'une année spécifique de sortie
    5) Films avec une notation supérieure à :
    6) Notation d'un film spécifique
    """)
            
        option = demander_nombre_entier()
     
        if option == 1: 
            return t20()    
        elif option == 2:
            return t20tt()
        elif option == 3:
            return t20te()
        elif option == 4:
            return t20ae()
        elif option == 5:
            return nsup()
        elif option == 6:
            return Nmfp() # a remplacer
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
    
    1) Le Nombre de films par region
    2) Quelles sont les langues du film :
    3) Durée des films            
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
        print("Personne liée au film / Réalisateur")
        print("""
    Vous souhaitez rechercher par:
    
    1) Genre de film réalisé par
    2) Nom des films réalisés par  
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
             print ("Choississez 1 ou 2 ")
                    
                    
def Actor():
    sortir = False
    option = 0
    while not sortir:
        print("Personne liée au film / Acteur")
        print("""
    Vous souhaitez rechercher par:
    
    1) Quels sont les acteurs nés après telle année ?
    2) Genre de films où a joué:
    3) Nom des films où a joué :          
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
    
    1) Notation
    2) Genre
    3) Autre                  
            """)
        
        option = demander_nombre_entier()
     
        if option == 1:
            return Ntn() 
        elif option == 2:
            return Gnr()    
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
        print("Personne liée au film")
        print("""
    Vous souhaitez rechercher par:
    
    1) Réalisateur
    2) Acteur ou actrice
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
        print("\nBienvenue dans le moteur de recherche Sql de la Base de données de IMDB")
        print("""
    Vous souhaitez rechercher par:
    
    1) Film
    2) Personne liée au film
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
                print("")
                print("Merci beaucoup d'utiliser notre service de recherche de films. \nNous espérons que vous avez eu une expérience agréable.")
                sortir = True   
        elif option == 2:
            Plf()
            autre_rech = input('Voulez-vous faire une autre recherche?(o/n) ')# On lance à nouveau la première recherche en utilisant la fonction section_principale()
            if autre_rech == "o":
                section_principale()    
            else:
                print("")
                print("Merci beaucoup d'utiliser notre service de recherche de films. \nNous espérons que vous avez eu une expérience agréable.")
                sortir = True
                        
        else:
            print('')
            print ("Choississez 1 où 2")
            

# Selecteur des sous menus ou des requêtes sql à effectuer utilisés dans l'ensemble du moteur de recherche
def demander_nombre_entier():
 
    correct=False
    num=0
    while(not correct):
                      
        try:
            num = int(input("Choisissez le numéro d'une option: "))
            correct=True
        except ValueError:
            print('Vous devez entrer un nombre entier')
     
    return num
            
section_principale()
