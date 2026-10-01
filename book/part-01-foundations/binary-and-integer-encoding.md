# Binaire, hexadécimal et nombres entiers

> **Statut :** premier jet  
> **Vérification des sources :** 2026-09-28  
> **Prérequis :** comprendre ce qu’est un bit

## Objectifs

À la fin de ce chapitre, tu pourras :

- convertir un entier entre les bases 2, 10 et 16;
- lire un nombre binaire non signé de largeur donnée;
- reconnaître la représentation usuelle des entiers signés en complément à deux;
- expliquer pourquoi une suite de bits n’a pas de valeur sans convention de largeur et de type.

## En une phrase

La base et la convention d’interprétation transforment une suite de bits en nombre; les mêmes bits peuvent représenter des valeurs différentes selon leur largeur et leur type signé ou non signé.

## Intuition

En base 10, les chiffres ont des poids : dans 352, le 3 vaut 3 centaines, le 5 vaut 5 dizaines et le 2 vaut 2 unités. Le système binaire fonctionne sur le même principe, mais les poids sont des puissances de 2. Le système hexadécimal raccourcit l’écriture binaire en remplaçant chaque groupe de quatre bits par un chiffre.

Il faut donc distinguer trois choses :

1. la suite de bits stockée;
2. la convention choisie pour la lire;
3. la valeur obtenue avec cette convention.

## Détails techniques

### Écriture positionnelle

Un nombre en base \(b\) est une somme de chiffres multipliés par les puissances de \(b\). Par exemple :

\[
352_{10} = 3\times10^2 + 5\times10^1 + 2\times10^0
\]

En base 2, les chiffres possibles sont 0 et 1, et les poids sont \(2^0, 2^1, 2^2, \ldots\). Ainsi :

\[
1101_2 = 1\times2^3 + 1\times2^2 + 0\times2^1 + 1\times2^0 = 13_{10}
\]

Pour convertir un entier décimal positif en binaire, on peut le décomposer en puissances de 2. Comme \(13 = 8+4+1\), les poids \(8,4,2,1\) donnent les bits \(1,1,0,1\), donc \(13_{10}=1101_2\).

Les bits après la virgule utilisent des puissances négatives. Par exemple :

\[
0{,}101_2 = 1\times2^{-1} + 0\times2^{-2} + 1\times2^{-3} = 0{,}625_{10}
\]

Certaines fractions décimales n’ont pas d’écriture binaire finie, comme \(0{,}1_{10}\). Leur représentation informatique doit alors être arrondie; les nombres à virgule flottante seront traités séparément.

### Entiers non signés sur N bits

Un entier binaire non signé sur \(N\) bits a la valeur :

\[
x = \sum_{i=0}^{N-1} b_i 2^i
\]

où \(b_i\) vaut 0 ou 1. Son intervalle va de \(0\) à \(2^N-1\), car le plus petit code est composé uniquement de zéros et le plus grand uniquement de uns.

Sur 4 bits, la valeur maximale est \(2^4-1=15\). Le code \(1101_2\) vaut 13. Sur 8 bits, le même motif devient \(00001101_2\) et vaut encore 13 : les zéros ajoutés à gauche conservent la valeur non signée, mais fixent une largeur de représentation.

### Hexadécimal : quatre bits par chiffre

La base 16 utilise les chiffres 0 à 9 puis les lettres A à F, où A vaut 10, B vaut 11, …, F vaut 15. Comme \(16=2^4\), un chiffre hexadécimal correspond exactement à quatre bits :

| Binaire | Hexadécimal | Décimal |
|---|---:|---:|
| 0000 | 0 | 0 |
| 1001 | 9 | 9 |
| 1010 | A | 10 |
| 1111 | F | 15 |

Pour convertir \(0111\ 1101\ 0000_2\), regroupe les bits en paquets de quatre depuis la droite : \(0111=7\), \(1101=D\), \(0000=0\). Le résultat s’écrit \(0x7D0\). Le préfixe `0x` indique généralement qu’un nombre est écrit en hexadécimal.

On peut retrouver sa valeur décimale : \(7\times16^2 + 13\times16^1 + 0 = 1792+208=2000\). L’hexadécimal est pratique pour lire des masques, des adresses, des registres et de longues suites binaires, car il est compact et se reconvertit directement en bits. [MIT OpenCourseWare (2017)](#ref-mitcompstructinfo2017)

### Entiers signés : complément à deux

Une suite de bits ne précise pas à elle seule si elle est signée. Pour un entier signé sur \(N\) bits, la convention la plus courante dans les ordinateurs modernes est le **complément à deux**. Le bit de poids fort a alors un poids négatif :

\[
x = -b_{N-1}2^{N-1} + \sum_{i=0}^{N-2} b_i2^i
\]

L’intervalle représentable est \(-2^{N-1}\) à \(2^{N-1}-1\). Sur 8 bits, il va de \(-128\) à \(127\). Le code \(11111111_2\) vaut \(-1\), alors qu’en non signé il vaut 255.

Pour obtenir \(-5\) sur 8 bits :

1. écrire \(+5\) : \(00000101\);
2. inverser chaque bit : \(11111010\);
3. ajouter 1 : \(11111011\).

Le résultat \(11111011\) représente donc \(-5\) en complément à deux sur 8 bits. Cette méthode équivaut à prendre le complément bit à bit, puis ajouter 1, en gardant la largeur fixée.

### Débordement : le motif reste, la valeur sort de l’intervalle

L’addition matérielle sur \(N\) bits conserve un résultat de \(N\) bits; une retenue au-delà de cette largeur peut être éliminée. Pour un entier non signé, le résultat correspond alors au calcul modulo \(2^N\). Par exemple, sur 8 bits, \(255+1\) produit le motif \(00000000\), c’est-à-dire 0 en non signé.

En complément à deux sur 8 bits, \(127+1\) produit \(10000000\). Ce motif vaut \(-128\), mais le résultat mathématique \(128\) ne tient pas dans l’intervalle signé \([-128,127]\). C’est un débordement (overflow). Le circuit a produit un motif déterminé; c’est l’interprétation dans le type choisi qui révèle que la valeur attendue n’est plus représentable.

### Vérifications rapides

- \(101101_2 = 32+8+4+1=45_{10}=0x2D\).
- Sur 8 bits, \(11110110_2\) vaut 246 en non signé, mais \(-10\) en complément à deux.
- Sur 5 bits, un non signé va de 0 à 31; un signé en complément à deux va de \(-16\) à 15.

Quand tu lis une donnée, note donc sa largeur, sa base et son type. « 11110110 » ne suffit pas : « 8 bits, binaire, signé en complément à deux » permet de conclure \(-10\).

## Limites et pièges

- Une suite de bits n’est pas automatiquement un nombre, un caractère ou une instruction; il faut connaître son format.
- Le résultat d’une conversion doit préciser la base. Le nombre \(10_2\) vaut deux, tandis que \(10_{10}\) vaut dix.
- En complément à deux, il y a un seul zéro, mais une valeur négative supplémentaire par rapport aux valeurs positives.
- Un débordement signé et une retenue non signée ne sont pas le même diagnostic. Ils dépendent de l’interprétation et de l’intervalle représentable.
- Les entiers, fractions fixes et nombres à virgule flottante suivent des règles distinctes; ce chapitre couvre seulement les entiers et une fraction binaire simple.

## À retenir

La représentation positionnelle utilise des puissances de la base. Le binaire encode les valeurs avec des bits; l’hexadécimal regroupe quatre bits par chiffre. Pour interpréter un motif, précise toujours la largeur et le type. Le complément à deux permet l’arithmétique signée sur une largeur fixe, mais n’élimine pas le débordement.

## Références

### MIT OpenCourseWare (2017) {#ref-mitcompstructinfo2017}

- MIT OpenCourseWare. « 1 Basics of Information », *Computation Structures*, cours 6.004, printemps 2017. Encodages, entiers binaires non signés, hexadécimal et complément à deux. Consulté le 28 septembre 2026. [Page du cours](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/). Clé bibliographique : `mitcompstructinfo2017`.
