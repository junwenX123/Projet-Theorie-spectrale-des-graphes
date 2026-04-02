# Projet LU3MA101 : Théorie Spectrale des Graphes et Partitionnement

[![Institution](https://img.shields.io/badge/Institution-Sorbonne_Université-blue.svg)](https://www.sorbonne-universite.fr/)
[![Language](https://img.shields.io/badge/Language-Python-green.svg)]()
[![Math](https://img.shields.io/badge/Math-Algèbre_Linéaire-orange.svg)]()
Ce dépôt présente les travaux réalisés dans le cadre du projet **LU3MA101** à **Sorbonne Université*Il porte sur l'étude et l'implémentation algorithmique de la **théorie spectrale des graphes** afin de résoudre le problème complexe du partitionnement de données (Clustering) dans de grands réseaux.

## Contexte et Objectifs

À l'ère du Big Data, où des systèmes comme les réseaux sociaux génèrent des quantités astronomiques de données (ex: 250 millions d'utilisateurs quotidiens sur X) , il est indispensable d'utiliser la théorie des graphes pour analyser ces connexions. 

L'objectif de ce projet est de modéliser des objets par des sommets et leurs relations par des arêtes, puis d'appliquer des méthodes d'algèbre linéaire (théorie spectrale) sur leurs représentations matricielles pour identifier des communautés ou partitions optimales.

##  Fondements Mathématiques et Algorithmiques

Ce projet explore plusieurs concepts mathématiques avancés et les confronte à la réalité computationnelle :

* **Représentation Matricielle :** Utilisation de la matrice d'adjacence $M$ et de la matrice Laplacienne $L = D - M$ (où $D$ est la matrice diagonale des degrés).
* **Analyse de la Conductance :** Implémentation d'une métrique pour évaluer la qualité d'une partition. Nous avons d'abord étudié un algorithme "brute force" ayant une complexité temporelle en $O(2^n)$.
* **Limites Computationnelles :** Mise en évidence de l'inefficacité de l'approche brute force pour des graphes réels (ex: un réseau de $n \approx 1500$ génère une complexité impraticable d'environ $10^{451}$ opérations).
* **Optimisation Spectrale (Vecteur de Fiedler) :** Pour contourner ces limites, nous avons implémenté une méthode basée sur le **Vecteur de Fiedler** (vecteur propre associé à la deuxième plus petite valeur propre de la Laplacienne). 
* **Méthodes Numériques :** Recherche de valeurs propres via la méthode de la puissance inverse et localisation avec les disques de Gerschgörin.Utilisation de la méthode de Jacobi (complexité en $O(n^3)$) pour la diagonalisation.

## Résultats et Cas d'Application

Nous avons appliqué notre algorithme de partitionnement spectral sur des jeux de données réels, importés via la lecture de fichiers `.mtx` en Python:

1.  **Graphe Exemple (8 sommets) :** Validation théorique de l'algorithme.
2.  **Club de Karaté de Zachary :** Identification réussie et satisfaisante des deux factions du club.
3.  **Réseau des Blogs Politiques (Polblogs) :** Partitionnement d'un réseau dense d'environ 1500 nœuds, illustrant la scalabilité et l'efficacité de l'approche spectrale face aux limites du brute force.
