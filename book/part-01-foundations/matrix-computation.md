# Calcul matriciel et précision numérique

> **Statut :** premier jet; sources et rendu PDF à valider. **Date de rédaction :** 2026-10-01
> **Prérequis :** savoir lire les dimensions d’une matrice; voir aussi le chapitre sur la mémoire

## Objectifs

À la fin du chapitre, tu pourras :

- calculer le produit de deux matrices et vérifier la compatibilité de leurs dimensions;
- estimer le nombre d’opérations d’une multiplication matricielle;
- expliquer pourquoi les calculs sont organisés par blocs;
- distinguer le format des entrées du format utilisé pour accumuler les résultats.

## En une phrase

Le calcul matriciel réutilise des multiplications et des additions sur des tableaux réguliers; son débit dépend à la fois des unités de calcul, du mouvement des données et de la précision numérique.

## La règle des dimensions

Soit une matrice A de dimensions \(m \times k\) et une matrice B de dimensions \(k \times n\). Le produit C = AB a les dimensions \(m \times n\). Le nombre de colonnes de A doit égaler le nombre de lignes de B.

Chaque élément du résultat est un produit scalaire d’une ligne de A et d’une colonne de B :

\[
C_{ij} = \sum_{r=1}^{k} A_{ir} B_{rj}
\]

Par exemple :

\[
A =
\begin{bmatrix}
1 & 2 & 0 \\
-1 & 3 & 1
\end{bmatrix},
\qquad
B =
\begin{bmatrix}
2 & 1 \\
0 & -1 \\
4 & 2
\end{bmatrix}
\]

A possède 2 lignes et 3 colonnes; B possède 3 lignes et 2 colonnes. Le produit est donc une matrice 2 × 2 :

\[
AB =
\begin{bmatrix}
1\cdot2 + 2\cdot0 + 0\cdot4 & 1\cdot1 + 2\cdot(-1) + 0\cdot2 \\
(-1)\cdot2 + 3\cdot0 + 1\cdot4 & (-1)\cdot1 + 3\cdot(-1) + 1\cdot2
\end{bmatrix}
=
\begin{bmatrix}
2 & -1 \\
2 & -2
\end{bmatrix}
\]

Le même calcul apparaît dans une couche linéaire d’un réseau de neurones, où une matrice représente souvent les poids appliqués à un lot d’exemples. La convention exacte des axes dépend du logiciel; les dimensions doivent être suivies explicitement.

## Volume de calcul et réutilisation

Pour multiplier une matrice \(m \times k\) par une matrice \(k \times n\), le calcul direct forme \(mn\) produits scalaires de longueur \(k\). En comptant une multiplication et une addition comme deux opérations flottantes, le coût est approximativement :

\[
2mkn \text{ opérations}
\]

La formule est une approximation conventionnelle; elle ignore notamment les additions initiales et les différences de comptage de certaines opérations. Une multiplication de deux matrices carrées de côté \(N\) demande donc environ \(2N^3\) opérations selon cette convention. Le produit de grandes matrices expose beaucoup de travaux indépendants : chaque élément de sortie peut être calculé séparément tant que ses entrées sont disponibles.

Une implémentation élémentaire relit souvent les mêmes valeurs de A et B de nombreuses fois. Les algorithmes rapides découpent les matrices en **blocs** (*tiles*) et gardent un bloc de résultats et des portions d’entrées dans des registres ou une mémoire locale pendant plusieurs opérations. Cette réutilisation réduit le trafic vers les mémoires plus lentes; la taille des blocs doit toutefois s’adapter à la mémoire rapide réellement disponible. [Williams, Waterman et Patterson (2009)](#ref-williams2009roofline)

Les GPU et certains accélérateurs fournissent des unités conçues pour ce type de produits. L’article sur le TPU décrit une unité matricielle utilisée pour des opérations de réseaux neuronaux. Il s’agit d’un exemple d’architecture particulière, pas d’une promesse de vitesse valable pour tous les calculs ou tous les appareils. [Jouppi et al. (2017)](#ref-jouppi2017tpu)

## Précision : stocker, calculer, accumuler

Un nombre réel n’est généralement représenté qu’avec un nombre fini de bits. Le format définit les valeurs représentables, les écarts entre valeurs et les règles d’arrondi. Des formats plus courts peuvent réduire la taille des données et, si le processeur les prend en charge, augmenter le débit de certaines opérations. Ils réduisent aussi la plage ou la précision disponibles.

Il faut distinguer :

1. le format dans lequel les entrées et les poids sont stockés;
2. le format des multiplications;
3. le format d’accumulation des sommes;
4. le format final du résultat.

Une méthode en précision mixte peut multiplier des entrées de format court et accumuler les résultats dans un format plus large. La prise en charge exacte varie selon la génération de matériel et les bibliothèques. La précision suffisante se vérifie avec la tâche, l’algorithme et les critères numériques choisis. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

L’arithmétique flottante arrondit les opérations intermédiaires. Comme l’addition n’est pas exactement associative en machine, changer l’ordre de sommation ou la méthode de calcul peut modifier les derniers chiffres du résultat. Deux implémentations qui représentent la même formule réelle peuvent donc produire des sorties proches sans être bit pour bit identiques. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

## Performance : calculer n’est qu’une partie du travail

Une multiplication matricielle fait beaucoup d’opérations, mais doit également charger les entrées, réutiliser les données et écrire le résultat. Le chapitre sur la [mémoire, la bande passante et la latence](memory-hierarchy.md) montre comment l’intensité arithmétique relie le nombre d’opérations aux octets transférés.

Le modèle Roofline fournit une première borne à partir de la bande passante et du débit de calcul maximal. Cette borne ne tient pas lieu de benchmark : le lancement d’un noyau, le choix des blocs, l’occupation du processeur, les conversions de format et la taille des matrices affectent aussi le temps mesuré. [Williams, Waterman et Patterson (2009)](#ref-williams2009roofline)

## Limites et pièges

- Le produit AB n’est défini que si les dimensions internes sont compatibles; en général, AB et BA ont des dimensions différentes et ne sont pas égaux.
- Le compte d’opérations \(2mkn\) est un modèle, pas le nombre exact d’instructions machine.
- Une unité matricielle n’est utile que si l’algorithme, les formes de matrices et le format sont compatibles avec son chemin matériel.
- Une précision plus courte peut changer les arrondis et la qualité du résultat; le gain doit être mesuré sur la tâche visée.
- Les performances annoncées en crête ne sont pas le débit soutenu d’un programme réel.

## À retenir

Le produit matriciel multiplie chaque ligne d’une matrice par chaque colonne de l’autre. Les blocs et la mémoire locale permettent de réutiliser les éléments chargés; les accélérateurs exploitent parfois ce motif avec des unités dédiées. Le coût et le résultat numérique dépendent du format, de l’ordre des opérations et du système mémoire.

## Références

### Jouppi et al. (2017) {#ref-jouppi2017tpu}

- Norman P. Jouppi et al. « In-Datacenter Performance Analysis of a Tensor Processing Unit ». *Proceedings of the 44th Annual International Symposium on Computer Architecture*, 2017, p. 1–12. [DOI : 10.1145/3079856.3080246](https://doi.org/10.1145/3079856.3080246).

### Goodfellow, Bengio et Courville (2016) {#ref-goodfellow2016}

- Ian Goodfellow, Yoshua Bengio et Aaron Courville. *Deep Learning*. MIT Press, 2016. Chapitres sur l’algèbre linéaire, le calcul numérique et les réseaux feedforward. [Livre et chapitres en ligne](https://www.deeplearningbook.org/).

### Williams, Waterman et Patterson (2009) {#ref-williams2009roofline}

- Samuel Williams, Andrew Waterman et David Patterson. « Roofline: An Insightful Visual Performance Model for Multicore Architectures ». *Communications of the ACM*, vol. 52, no 4, 2009, p. 65–76. [DOI : 10.1145/1498765.1498785](https://doi.org/10.1145/1498765.1498785).
