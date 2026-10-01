# Vecteurs, matrices et tenseurs

> **Statut :** premier jet; sources et rendu PDF à valider. **Date de rédaction :** 2026-10-01
> **Prérequis :** savoir lire les nombres binaires; aucune algèbre linéaire avancée requise

## Objectifs

À la fin du chapitre, tu pourras :

- distinguer un scalaire, un vecteur, une matrice et un tenseur;
- écrire et vérifier la forme (*shape*) d’un tableau;
- calculer un produit scalaire et un produit matrice-vecteur;
- reconnaître comment ces objets décrivent des données et des transformations.

## En une phrase

Scalaires, vecteurs, matrices et tenseurs sont des tableaux de nombres organisés selon un nombre défini d’axes; leurs dimensions déterminent quelles opérations sont compatibles.

## Des nombres seuls aux tableaux

Un **scalaire** est une seule valeur, comme une température ou un taux. Un **vecteur** est une suite ordonnée de valeurs; un **vecteur-colonne** de dimension \(n\) s’écrit :

\[
\mathbf{x} =
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}
\]

Une **matrice** est un tableau à deux axes, souvent des lignes et des colonnes. Un **tenseur** généralise ce rangement à d’autres nombres d’axes : une matrice a deux axes, et un lot de matrices peut en avoir trois ou plus. Ici, le mot « ordre » désigne le nombre d’axes afin de ne pas le confondre avec le rang d’une matrice en algèbre linéaire. [Strang (2016)](#ref-strang2016) [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

La **forme** indique la taille de chaque axe. Une matrice avec trois lignes et deux colonnes a la forme 3 × 2. Une image couleur peut être représentée par les axes hauteur, largeur et canal de couleur; un lot d’images ajoute un axe de lot. La forme décrit la disposition mathématique des valeurs, pas leur unité ni leur signification.

## Opérations élémentaires sur les vecteurs

Deux vecteurs de même dimension peuvent être additionnés coordonnée par coordonnée. Un scalaire peut multiplier chaque coordonnée. Le **produit scalaire** de deux vecteurs de dimension \(n\) additionne les produits des coordonnées correspondantes :

\[
\mathbf{x}\cdot\mathbf{y} = \sum_{i=1}^{n} x_i y_i
\]

Pour \(\mathbf{x}=[2, -1, 3]\) et \(\mathbf{y}=[4, 5, 2]\), le produit scalaire vaut \(2\cdot4 + (-1)\cdot5 + 3\cdot2 = 9\). Il réduit deux vecteurs de même dimension à un seul scalaire. Un produit scalaire intervient, par exemple, lorsqu’on pondère des caractéristiques pour produire un score.

Les vecteurs ont une orientation. Le produit d’une ligne par une colonne peut produire un scalaire; le produit d’une colonne par une ligne produit plutôt une matrice. Il faut donc suivre les dimensions et la convention utilisée, pas seulement compter les valeurs. [Strang (2016)](#ref-strang2016)

## Une matrice transforme un vecteur

Une matrice \(A\) de forme \(m \times n\) peut multiplier un vecteur-colonne \(\mathbf{x}\) de dimension \(n\). Le résultat est un vecteur de dimension \(m\). Par exemple :

\[
A =
\begin{bmatrix}
1 & 2 \\
-1 & 3
\end{bmatrix},
\qquad
\mathbf{x} =
\begin{bmatrix}
4 \\
1
\end{bmatrix}
\]

\[
A\mathbf{x} =
\begin{bmatrix}
1\cdot4 + 2\cdot1 \\
(-1)\cdot4 + 3\cdot1
\end{bmatrix}
=
\begin{bmatrix}
6 \\
-1
\end{bmatrix}
\]

Chaque ligne de \(A\) prend un produit scalaire avec \(\mathbf{x}\). De façon équivalente, le résultat est une combinaison des colonnes de \(A\), pondérées par les coordonnées de \(\mathbf{x}\). Cette interprétation relie la multiplication matricielle aux transformations linéaires : la matrice encode comment les coordonnées d’entrée contribuent à celles de sortie. [Strang (2016)](#ref-strang2016)

Dans une couche dense d’un réseau neuronal, un tableau d’entrées est multiplié par des poids, puis un biais est souvent ajouté; une fonction d’activation peut ensuite être appliquée. Selon le logiciel, les exemples du lot se rangent en lignes ou en colonnes, ce qui change l’ordre d’écriture des matrices sans changer l’idée du calcul. Le chapitre sur le [calcul matriciel](matrix-computation.md) approfondit la multiplication de matrices.

## Forme et compatibilité

Avant une opération, compare les formes :

- l’addition coordonnée par coordonnée exige des formes compatibles, souvent identiques;
- le produit de \(A\) de forme \(m \times n\) par \(B\) de forme \(n \times p\) donne une matrice de forme \(m \times p\);
- si les dimensions intérieures ne correspondent pas, le produit matriciel n’est pas défini.

Les bibliothèques numériques peuvent autoriser la diffusion (*broadcasting*) de certaines dimensions. Cette facilité obéit à des règles précises; elle ne signifie pas que toutes les formes peuvent être additionnées ou multipliées.

## Limites et pièges

- Une forme comme 2 × 3 donne les dimensions, mais ne dit pas ce que représentent les valeurs.
- Un vecteur-colonne et un vecteur-ligne contiennent le même nombre de valeurs, mais ne sont pas interchangeables dans les produits matriciels.
- Le mot « tenseur » décrit ici un tableau multi-axe; il ne désigne pas nécessairement un objet physique ou un format de fichier particulier.
- Des opérations de diffusion peuvent cacher une dimension incorrecte si l’on ne vérifie pas la forme du résultat.
- Les conventions d’axes changent entre bibliothèques et modèles; il faut suivre les dimensions à chaque étape.

## À retenir

Un scalaire possède une valeur, un vecteur un axe, une matrice deux axes et un tenseur peut en avoir plusieurs. Les formes indiquent quelles opérations sont compatibles. Une matrice-vecteur transforme des coordonnées par combinaisons linéaires et fournit l’un des motifs de calcul fondamentaux des réseaux neuronaux.

## Références

### Strang (2016) {#ref-strang2016}

- Gilbert Strang. *Introduction to Linear Algebra*, 5e édition. Wellesley-Cambridge Press, 2016.

### Goodfellow, Bengio et Courville (2016) {#ref-goodfellow2016}

- Ian Goodfellow, Yoshua Bengio et Aaron Courville. *Deep Learning*. MIT Press, 2016. Chapitre 2, « Linear Algebra ». [Livre et chapitres en ligne](https://www.deeplearningbook.org/contents/linear_algebra.html).
