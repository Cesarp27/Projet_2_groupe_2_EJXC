# Projet_2_groupe_2_EJXC
Projet films

## OBJECTIF DU PROJET

Générer un moteur de recherche qui vous permet de trouver un film particulier et obtenir des informations spécifiques et relatives.

## Définition du plan de travail

Lors d’un brainstorming, nous avons discuté de la façon dont nous pourrions mener à bien le développement du projet. Nous nous sommes rendu compte que si dès le début nous divisions le travail en parties, cela permettrait à chacun de pratiquer et d'assimiler une partie des processus nécessaires au projet, mais ce serait au détriment du reste du contenu, donc la plupart d'entre nous avons convenu que ce pourrait être une bonne idée de développer tout le projet en parallèle, puis à la fin du projet nous divisons la mise en œuvre de certaines étapes.

## Base de données MySQL

Via le terminal, nous chargeons d'abord une version récapitulative de 10.000 lignes des tables d'origine dans la base de données MySQL À partir de là, nous avons commencé le processus d'optimisation du modèle de base relationnel, pour cela, nous avons dû modifier le modèle, supprimer les tables et en charger à nouveau dans la base de données MySQL plusieurs fois, lorsque nous avons finalement trouvé la configuration appropriée, nous avons chargé les grandes tables et avons commencé par mettre le SQL en pratique.

## SQL

Nous en avons appris un peu plus sur SQL et avons commencé à mieux comprendre son fonctionnement Nous avons commencé à faire des recherches sur les données qui pourraient être exploitées dans notre base de données Grâce aux exercices vus en classe et avec la pratique, nous avons commencé à comprendre comment traduire une question de langage commun sur notre ensemble de données en une recherche SQL, telle que: Quels sont les 20 films les mieux notés? À un moment donné, nous avons réalisé que certaines recherches prenaient beaucoup de temps Sachant que dans ce cas, nous n'ajouterions ni ne supprimerions des données de notre ensemble de données, nous avons décidé d'ajouter des index dans les colonnes les plus utilisées dans nos recherches, prises en charge par la commande SQL EXPLAIN

## Entracte

Lors du développement de toutes ces étapes nous avons vu en classe et appliqué à notre base de données différents processus de conception et d'optimisation de la base de données:

    Nous avons vu comment ajouter des Triggers pour enregistrer les modifications dans nos tables,
    Nous avons vu comment créer un script qui, une fois exécuté, remplissait toutes nos tables avec les données les plus récentes disponibles sur le site de téléchargement
    Nous avons vu comment créer un script pour supprimer les lignes des différentes tables qui n'avaient aucune relation avec la table principale appelée title_basics
    Nous avons vu comment créer un code python pour connaître la longueur maximale des différents champs dans les tables et avec ces informations, nous avons pu ajuster les Datatype dans workbench avec le but d'optimiser l'espace de stockage de nos données
    avec un programme python nous avons obtenu les différentes valeurs de certaines colonnes et avec cette liste de valeurs nous avons mis un Dataype Set() dans le modèle
    Nous avons compris l'utilité des index FULLTEXT dans les colonnes contenant du texte et comment effectuer des recherches dans les colonnes qui ont ce type de données.
    Nous avons compris l'importance d'accéder aux données avec notre programme python en utilisant un user "reader" avec des autorisations uniquement de lecture pour éviter des modifications inattendues.

## Python

À ce stade, il était nécessaire de réfléchir à ce qu'un utilisateur à la recherche d'informations sur les films pourrait rechercher dans notre interface. Avec ces informations, nous avons développé un code python qui a généré une sorte de navigateur offrant à l'utilisateur différentes options à chaque étape pour ensuite générer une recherche SQL puis afficher les informations.

## Conclusion

La mise en œuvre de ce projet nous a permis de comprendre et de réaliser des processus qui paraissaient au premier abord très difficiles voire incompréhensibles. Nous avons pu vérifier que pour apprendre à programmer ce que vous devez faire est d'écrire du code.

## Bonus

Un peu en dehors de ce qui était initialement demandé comme objectif du projet, nous avons décidé de voir si avec les données dont nous disposions il était possible de générer une prédiction en utilisant le Machine Learning. Nous avons pu l'implémenter et obtenu un score de prédiction de 35%.

