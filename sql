Recherches SQL Caesar

On veux par exemple pouvoir trouver
- Les films en fonction de leur titre, nationalité, date
SELECT title_basics.primaryTitle AS Film, title_akas.region AS nationalité, title_basics.startYear AS Date
FROM title_basics
INNER JOIN title_akas ON title_basics.tconst = title_akas.titleId
WHERE title_basics.primaryTitle = '' AND title_basics.startYear = '' AND title_akas.region = 'FR'

SELECT title_basics.primaryTitle, title_akas.region, title_basicsstartYear
FROM title_basics
INNER JOIN title_akas ON title_basics.tconst = title_akas.tconst


- Les séries, par années
title_basics.titleType = tvSeries AND title_basics.titleType = tvMiniSeries

SELECT `title_basics`.`tconst` AS `tconst`, `title_basics`.`titleType` AS `titleType`, `title_basics`.`primaryTitle` AS `primaryTitle`, `title_basics`.`originalTitle` AS `originalTitle`, `title_basics`.`isAdult` AS `isAdult`, `title_basics`.`startYear` AS `startYear`, `title_basics`.`endYear` AS `endYear`, `title_basics`.`runtimeMinutes` AS `runtimeMinutes`, `title_basics`.`genres` AS `genres`
FROM `title_basics`
WHERE ((`title_basics`.`titleType` = 'tvSeries'
    OR `title_basics`.`titleType` = 'tvMiniSeries')
   AND `title_basics`.`startYear` = 1980)


Classement par votes
FROM title_basics
INNER JOIN title_ratings ON title_basics.tconst = title_ratings.tconst
ORDER BY title_ratings.averageRating DESC
LIMIT 20

1)Quel est le top 20 des films les mieux notés ?
SELECT `title.basics`.primaryTitle,`title.ratings`.numVotes 
FROM `title.ratings`, `title.basics` 
WHERE `title.ratings`.tconst=`title.basics`.tconst 
ORDER BY numVotes DESC LIMIT 20;

2)Quels sont les films réalisés par ‘nm0525910’
2) SELECT * FROM `title.principals` 
WHERE nconst = 'nm0525910' AND category = 'director';

2) Mas especifica
SELECT `title.basics`.primaryTitle
FROM `title.principals`, `title.basics`
WHERE nconst = 'nm0525910' AND category = 'director' AND `title.principals`.tconst=`title.basics`.tconst;


3)Quels sont les différents genres de films
3) SELECT DISTINCT `genres` FROM `title.basics`;

4)Quels sont les films réalisés après 2000 ?
4)SELECT primaryTitle, startYear FROM `title.basics` WHERE startYear>2000 ORDER BY startYear;

5)Quels sont les films réalisés entre 2000 et 2010 ?
5)SELECT primaryTitle, startYear FROM `title_basics` WHERE startYear>=2000 AND startYear<2010 ORDER BY startYear ;
++ 5) SELECT primaryTitle, startYear FROM title_basics WHERE startYear BETWEEN 1900 AND 1990;
[entre 1892 y 1936 (para el archivo pequeno)]

++**++ 5) SELECT primaryTitle, startYear FROM title_basics  WHERE startYear BETWEEN 1920 AND 1936  AND titleType IN ('movie')  ORDER BY startYear ASC;

```
SELECT primaryTitle, startYear FROM title_basics 
WHERE startYear BETWEEN 1900 AND 1990
AND titleType IN movie;
```

6)Quels sont les films produits par ‘nm0249379’ ?
6)SELECT *
FROM `title.principals`
WHERE nconst = 'nm0249379' AND category = 'producer';

++6)SELECT `title.basics`.primaryTitle
FROM `title.principals`, `title.basics`
WHERE nconst = 'nm0249379' AND category = 'producer' AND `title.principals`.tconst=`title.basics`.tconst;

7)Qui sont les acteurs nés en 2000 ?
7)SELECT primaryName FROM `name.basics` WHERE deathYear = 2000 

8)Quelle est le langage du film « Dragon Kid » ?
*8)SELECT language FROM `title.akas` WHERE title='Dragon Kid' 

9)Quelles sont les différente régions présentées par les films ?
9)SELECT DISTINCT region FROM `title.akas`;




Mettre en œuvre les commandes SQL sur les données IMDB – Niveau 2 :
• Quel est la note du film ‘Autour d'une cabine’ ?


SELECT title_ratings.averageRating, title_basics.primaryTitle
FROM title_ratings
INNER JOIN title_basics ON title_basics.tconst = title_ratings.tconst
WHERE title_basics.primaryTitle = ‘Autour d'une cabine’;


• Quels sont la note et le nombre de votes du film ‘The Sea’ ?


SELECT title_basics.primaryTitle, title_ratings.averageRating, title_ratings.numVotes
FROM title_ratings
INNER JOIN title_basics ON title_basics.tconst = title_ratings.tconst
WHERE title_basics.primaryTitle = "The Sea";


• Quel sont les noms des films ayant obtenu une note supérieure à 9 ?

SELECT title_basics.primaryTitle,title_ratings.averageRating
FROM title_ratings
INNER JOIN title_basics ON title_basics.tconst = title_ratings.tconst
WHERE title_ratings.averageRating > 9 
ORDER BY title_ratings.averageRating DESC

• Quel est le nom du film ayant obtenu la note maximale

SELECT title_basics.primaryTitle,title_ratings.averageRating
FROM title_ratings
INNER JOIN title_basics ON title_basics.tconst = title_ratings.tconst
WHERE title_ratings.averageRating = Max(title_ratings.averageRating);
**** + preguntara Remi
al parecer el max genenera una esecie de promedio maxiomo
tambien cuando hago join o iner join, veo que desaparece el valor maximo que es de 9.7, en las tablas pequenas

---
1 Combien y-a-t-il de films par régions ?
SELECT region, COUNT(title) FROM `title_akas` GROUP BY region ORDER BY COUNT(title) DESC;

2 Combien y-a-t-il de films de plus de 3h ?
SELECT COUNT(primaryTitle) FROM `title_basics` WHERE runtimeMinutes  > 180;


SELECT COUNT(title), region
FROM `title_akas`
GROUP BY region
HAVING COUNT(CustomerID) > 5
ORDER BY COUNT(CustomerID) DESC;


SELECT COUNT(primaryTitle)
FROM `title_basics`
WHERE runtimeMinutes  > 180;

2 count     where     *** otra opcion puede ser por categoria y por hora

3 Combien y-a-t-il de films par genre ?
```
#Combien de films de plus de 3h par genre
```

```
SELECT COUNT(tconst), genres
FROM title_basics
WHERE runtimeMinutes > 180
GROUP BY genres
ORDER BY COUNT(tconst) DESC;
```

SELECT COUNT(tconst), genres
FROM `title_basics`
GROUP BY genres
HAVING COUNT(tconst)  > 50
ORDER BY COUNT(tconst) DESC;

La diferencia entre WHERE y HAVING (aparte de que uno se coloca primero en la jerarquia)
es que con WHERE filtro tomando en cuenta todos los datos de base
y con HAVING filtro los datos luego de haberlos agrupado

---
Mettre en œuvre les commandes SQL (JOIN) sur les données IMDB :

•4)Quel sont les noms de films du top 20 les mieux notés ?
SELECT title_basics.primaryTitle, title_ratings.averageRating
FROM title_basics
INNER JOIN title_ratings ON title_basics.tconst = title_ratings.tconst
ORDER BY title_ratings.averageRating DESC
LIMIT 20

• 5)Quels sont les noms de films réalisés par ‘nm0525910’ ?

SELECT title_basics.primaryTitle AS titre, title_principals.category AS directeur, name_basics.primaryName
FROM title_basics
INNER JOIN title_principals ON title_principals.tconst = title_basics.tconst
INNER JOIN name_basics ON name_basics.nconst = title_principals.nconst
WHERE name_basics.nconst = "nm0525910" AND title_principals.category = 'director'
**** Hay que probar esto en las tablas grandes

•6)Quels sont les noms de films produits par ‘nm0249379’ ?

SELECT title_basics.primaryTitle AS titre, title_principals.category AS productor, name_basics.primaryName
FROM title_basics
INNER JOIN title_principals ON title_principals.tconst = title_basics.tconst
INNER JOIN name_basics ON name_basics.nconst = title_principals.nconst
WHERE title_principals.category = 'productor'

•7) Quels sont les noms de films produits par ‘Steven Spielberg’ ?

SELECT title_basics.primaryTitle AS titre, title_principals.category AS productor, name_basics.primaryName
FROM title_basics
INNER JOIN title_principals ON title_principals.tconst = title_basics.tconst
INNER JOIN name_basics ON name_basics.nconst = title_principals.nconst
WHERE name_basics.primaryName = "Steven Spielberg" AND title_principals.category = 'productor'
**** Hay que probar esto en las tablas grandes
---
SELECT title_basics.primaryTitle AS titre, title_principals.category AS productor, name_basics.primaryName
FROM name_basics
INNER JOIN title_principals ON name_basics.nconst = title_principals.nconst
INNER JOIN title_basics ON title_principals.tconst = title_basics.tconst 
WHERE name_basics.primaryName = "Steven Spielberg"
---
• 8)Quel sont les ‘nconst’ associés aux films ayant obtenu une note supérieure à 9 ?

SELECT name_basics.nconst, name_basics.primaryName, title_ratings.averageRating
FROM title_ratings
INNER JOIN title_principals ON title_principals.tconst = title_ratings.tconst
INNER JOIN name_basics ON title_principals.nconst = name_basics.nconst
WHERE title_ratings.averageRating > 9 
ORDER BY title_ratings.averageRating DESC

SELECT title_principals.nconst , title_basics.primaryTitle,title_ratings.averageRating
FROM title_ratings
INNER JOIN title_basics ON title_basics.tconst = title_ratings.tconst
INNER JOIN title_principals ON title_principals.tconst = title_basics.tconst
WHERE title_ratings.averageRating > 9 
ORDER BY title_ratings.averageRating DESC

• 9)Quels sont les noms des personnes associées aux films ayant obtenu une note supérieure à 9 ?

SELECT  name_basics.primaryName, title_ratings.averageRating
FROM title_ratings
INNER JOIN title_principals ON title_principals.tconst = title_ratings.tconst
INNER JOIN name_basics ON title_principals.nconst = name_basics.nconst
WHERE title_ratings.averageRating > 9 
ORDER BY title_ratings.averageRating DESC

Création de vue avec jointure principals-films-personnes:

CREATE VIEW `global` AS
select `P`.`job` AS `job`,`F`.`titleType` AS `titleType`,`F`.`primaryTitle` AS `primaryTitle`,`F`.`startYear` AS `startYear`,`F`.`endYear` AS `endYear`,`F`.`genres` AS `genres`,`A`.`primaryName` AS `primaryName`,`A`.`birthYear` AS `birthYear` 
from title_principals AS P 
join title_basics as F 
join name_basics AS A 
on (`P`.`tconst` = `F`.`tconst`) and (`P`.`nconst` = `A`.`nconst`)

• Combien y-a-t-il de films par régions ?

SELECT  region, COUNT(titleId)
FROM title_akas
GROUP BY region
ORDER BY COUNT(titleId)DESC

• Combien y-a-t-il de films de plus de 3h ?

SELECT runtimeMinutes, COUNT(tconst)
FROM title_basics
GROUP BY runtimeMinutes
HAVING runtimeMinutes > 180
ORDER BY COUNT(tconst) DESC;

• Combien y-a-t-il de films par genre ?
***+ aqui falta separar los campos

SELECT  genres, COUNT(tconst)
FROM title_basics
GROUP BY genres
ORDER BY COUNT(tconst) DESC


****+++
con la actualizacion del set() ahora se pueden buscar las peliculas por genero usando el select de abajo
SELECT primaryTitle, genres
FROM title_basics
WHERE genres IN ('Drama', 'Comedy')

SELECT primaryName, primaryProfession
FROM name_basics
WHERE primaryProfession IN ('soundtrack', 'actor')

SELECT genres, COUNT(tconst)
FROM title_basics
WHERE genres IN ('Drama', 'Comedy')
GROUP BY genres DESC

****+++++++++++++++++++++++++*********************************************
test mio (esto no funciona)
SELECT nconst, primaryName, knownForTitles
FROM name_basics
WHERE knownForTitles = 'tt0077975,tt0078723,tt0080455,tt0072562'

SELECT nconst, primaryName, knownForTitles
FROM name_basics
WHERE knownForTitles IN ('tt0077975')

