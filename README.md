# Projet-Theorie-spectrale-des-graphes
#  Projet LU3MA101 : Théorie Spectrale des Graphes et Partitionnement

[![Institution](https://img.shields.io/badge/Institution-Sorbonne_Université-blue.svg)](https://www.sorbonne-universite.fr/)
[![Language](https://img.shields.io/badge/Language-Python-green.svg)]()
[![Math](https://img.shields.io/badge/Math-Algèbre_Linéaire-orange.svg)]()

[cite_start]Ce dépôt présente les travaux réalisés dans le cadre du projet **LU3MA101** à **Sorbonne Université**[cite: 2, 4]. [cite_start]Il porte sur l'étude et l'implémentation algorithmique de la **théorie spectrale des graphes** afin de résoudre le problème complexe du partitionnement de données (Clustering) dans de grands réseaux[cite: 2, 30].

##  Contexte et Objectifs

[cite_start]À l'ère du Big Data, où des systèmes comme les réseaux sociaux génèrent des quantités astronomiques de données (ex: 250 millions d'utilisateurs quotidiens sur X) [cite: 25, 26][cite_start], il est indispensable d'utiliser la théorie des graphes pour analyser ces connexions[cite: 27]. 

[cite_start]L'objectif de ce projet est de modéliser des objets par des sommets et leurs relations par des arêtes, puis d'appliquer des méthodes d'algèbre linéaire (théorie spectrale) sur leurs représentations matricielles pour identifier des communautés ou partitions optimales[cite: 28, 29].

##  Fondements Mathématiques et Algorithmiques

Ce projet explore plusieurs concepts mathématiques avancés et les confronte à la réalité computationnelle :

* [cite_start]**Représentation Matricielle :** Utilisation de la matrice d'adjacence $M$ et de la matrice Laplacienne $L = D - M$ (où $D$ est la matrice diagonale des degrés)[cite: 49, 240, 241].
* [cite_start]**Analyse de la Conductance :** Implémentation d'une métrique pour évaluer la qualité d'une partition[cite: 171, 173]. [cite_start]Nous avons d'abord étudié un algorithme "brute force" ayant une complexité temporelle en $O(2^n)$[cite: 222, 223].
* [cite_start]**Limites Computationnelles :** Mise en évidence de l'inefficacité de l'approche brute force pour des graphes réels (ex: un réseau de $n \approx 1500$ génère une complexité impraticable d'environ $10^{451}$ opérations)[cite: 231, 232, 233].
* [cite_start]**Optimisation Spectrale (Vecteur de Fiedler) :** Pour contourner ces limites, nous avons implémenté une méthode basée sur le **Vecteur de Fiedler** (vecteur propre associé à la deuxième plus petite valeur propre de la Laplacienne)[cite: 360, 523]. 
* [cite_start]**Méthodes Numériques :** Recherche de valeurs propres via la méthode de la puissance inverse et localisation avec les disques de Gerschgörin[cite: 547, 564]. [cite_start]Utilisation de la méthode de Jacobi (complexité en $O(n^3)$) pour la diagonalisation[cite: 583, 588].

## Résultats et Cas d'Application

[cite_start]Nous avons appliqué notre algorithme de partitionnement spectral sur des jeux de données réels, importés via la lecture de fichiers `.mtx` en Python[cite: 96, 99]:

1.  [cite_start]**Graphe Exemple (8 sommets) :** Validation théorique de l'algorithme[cite: 184].
2.  [cite_start]**Club de Karaté de Zachary :** Identification réussie et satisfaisante des deux factions du club[cite: 739, 740].
3.  [cite_start]**Réseau des Blogs Politiques (Polblogs) :** Partitionnement d'un réseau dense d'environ 1500 nœuds, illustrant la scalabilité et l'efficacité de l'approche spectrale face aux limites du brute force[cite: 746].

##  Auteurs

Ce projet a été réalisé conjointement par :
* [cite_start]Milan Delmas [cite: 3]
* [cite_start]Xiao Junwen [cite: 3]
* [cite_start]Alexandre de Jaeger [cite: 3]
* [cite_start]Corentin Gratien [cite: 3]

[cite_start]*Soutenance réalisée le 3 décembre 2025.* [cite: 5]
