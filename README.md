# L'Art de la Multiplication avec Turtle

Ce projet utilise Python et la bibliothèque `turtle` pour générer des figures basées sur les tables de multiplication. Il permet de visualiser les connexions entre les points d'un cercle en fonction d'une table donnée.

## Fonctionnalités
- Création d'un cercle avec un nombre configurable de points.
- Connexion des points selon la table de multiplication choisie.
- Génération interactive des figures.

## Prérequis
Ce programme nécessite `Python` et la bibliothèque `turtle` (incluse par défaut dans Python).

## Installation
Aucune installation spécifique requise. Il suffit d'exécuter le script Python.

## Utilisation
1. Exécutez le script :
   ```bash
   python multiplication_art.py
   ```
2. Entrez le nombre de points du cercle.
3. Entrez la table de multiplication à utiliser.
4. La figure sera générée dans la fenêtre Turtle.

## Explication Technique
1. **Création du cercle** : Un cercle est dessiné avec `turtle`.
2. **Placement des points** : Des points rouges sont répartis régulièrement sur le cercle.
3. **Stockage des coordonnées** : Les positions des points sont enregistrées dans une liste.
4. **Tracé des lignes** : Chaque point est relié à un autre en fonction de la table de multiplication.
