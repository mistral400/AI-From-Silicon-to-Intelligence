# De l’électricité au bit : niveaux logiques et abstraction numérique

> **Statut :** premier chapitre de fond  
> **Vérification des sources :** 2026-09-28  
> **Prérequis :** tension électrique, notion de circuit

## Objectifs

À la fin de ce chapitre, tu pourras :

- expliquer pourquoi un bit est une abstraction et non une tension précise;
- distinguer les niveaux logiques bas, haut et indéterminé;
- calculer une marge au bruit à partir de spécifications d’entrée et de sortie;
- relier une suite de bits à un nombre quand une convention de représentation est fixée.

## En une phrase

Un bit est une unité d’information qui distingue deux états; dans un circuit numérique, des plages de tension servent à représenter ces états de façon assez fiable malgré le bruit.

## Intuition

Imagine qu’un circuit envoie un message avec deux mots possibles : « 0 » et « 1 ». Le fil ne porte pas directement les symboles 0 et 1. Il porte une tension électrique, qui peut prendre beaucoup de valeurs et varier un peu à cause de la température, des composants, de l’alimentation et du bruit.

Le circuit qui reçoit le signal applique une règle : les tensions suffisamment basses comptent comme 0; les tensions suffisamment hautes comptent comme 1. Entre les deux, la valeur n’est pas garantie. Cette zone tampon évite d’exiger une tension parfaitement exacte.

## Détails techniques

### Le bit ne dicte pas son support physique

Un bit peut représenter l’un de deux états distincts, souvent notés 0 et 1. Ces symboles sont abstraits : ils ne signifient pas intrinsèquement « absence de courant » et « présence de courant », ni « 0 V » et « 5 V ». La convention dépend du système physique. Les circuits logiques numériques utilisent souvent des plages de tension pour encoder ces états.

Cette distinction est essentielle pour comprendre l’informatique : l’information est représentée par un signal physique selon une convention, puis traitée par des composants qui doivent respecter cette convention. Le matériel peut changer; l’abstraction du bit reste la même.

### Plages de tension valides

Un circuit réel ne lit pas une tension avec une précision infinie. Une spécification logique définit plutôt des seuils. Pour un récepteur donné :

- une tension inférieure ou égale à **VIL** est reconnue comme un 0 valide;
- une tension supérieure ou égale à **VIH** est reconnue comme un 1 valide;
- entre **VIL** et **VIH**, le niveau est indéterminé : le fabricant ne garantit pas si l’entrée sera lue comme 0 ou 1.

Le circuit émetteur possède aussi des garanties de sortie :

- **VOL** : tension maximale garantie pour une sortie basse;
- **VOH** : tension minimale garantie pour une sortie haute.

Les seuils précis changent selon la famille logique, l’alimentation, le composant et parfois les conditions d’utilisation. Il faut consulter la fiche technique du composant plutôt que supposer qu’un 0 vaut toujours 0 V ou qu’un 1 vaut toujours une tension donnée.

### Marge au bruit

Lorsqu’une sortie basse est connectée à une entrée, la marge entre la sortie maximale garantie et le seuil d’entrée bas indique la perturbation tolérable :

\[
NM_L = V_{IL} - V_{OL}
\]

Pour le niveau haut :

\[
NM_H = V_{OH} - V_{IH}
\]

Une marge positive signifie qu’un peu de bruit peut modifier la tension sans faire franchir le seuil reconnu par le récepteur. Les niveaux de sortie et d’entrée sont choisis pour laisser ces marges, ce qui rend les circuits composés plus robustes. L’analyse par seuils et marges est au cœur de l’abstraction numérique enseignée dans le cours *Computation Structures* du MIT. [MIT OpenCourseWare (2017)](#ref-mitcompstruct2017)

### Exemple numérique illustratif

Supposons un système **fictif** avec ces spécifications :

| Paramètre | Valeur |
|---|---:|
| Sortie basse maximale, VOL | 0,4 V |
| Seuil d’entrée bas maximal, VIL | 0,8 V |
| Seuil d’entrée haut minimal, VIH | 2,0 V |
| Sortie haute minimale, VOH | 2,4 V |

Alors :

\[
NM_L = 0{,}8 - 0{,}4 = 0{,}4\ \text{V}
\]

\[
NM_H = 2{,}4 - 2{,}0 = 0{,}4\ \text{V}
\]

Une perturbation de 0,2 V sur l’une de ces sorties resterait dans la marge prévue par cet exemple. Une perturbation assez grande pour faire franchir le seuil peut rendre l’interprétation non garantie. Ces chiffres sont choisis pour illustrer le calcul; ils ne décrivent pas une famille logique commerciale.

### Des bits aux nombres

Une suite de bits n’est pas un nombre sans convention supplémentaire. En représentation binaire non signée, chaque position correspond à une puissance de deux. Par exemple :

\[
101_2 = 1\times2^2 + 0\times2^1 + 1\times2^0 = 5_{10}
\]

La même suite de bits peut avoir une autre signification si le système choisit une autre interprétation : nombre signé, caractère, instruction, pixel, ou partie d’une autre structure de données. Le matériel transporte des états; le format détermine comment les interpréter.

## Limites et pièges

- Un niveau situé dans la zone indéterminée n’a pas une interprétation numérique garantie par la spécification.
- Les seuils de logique ne sont pas universels : vérifie la fiche technique et les conditions d’alimentation.
- Un circuit numérique s’appuie sur des tensions analogiques. « Numérique » décrit la manière de traiter les états, pas la nature parfaitement discrète du signal physique.
- Les marges au bruit ne disent pas à elles seules si le signal est assez rapide. Le délai de propagation et les comportements temporels seront étudiés avec les portes et circuits séquentiels.

## À retenir

Le bit est une abstraction d’information. Dans un circuit, on représente souvent ses deux états par des plages de tension séparées par une zone non garantie. Les marges entre sorties et seuils d’entrée donnent une tolérance au bruit. Enfin, une suite de bits n’a de sens qu’avec une convention d’encodage.

## Références

### MIT OpenCourseWare (2017) {#ref-mitcompstruct2017}

- MIT OpenCourseWare. « 2 The Digital Abstraction », *Computation Structures*, cours 6.004, printemps 2017. Seuils de tension, zone interdite, spécifications combinatoires et marges au bruit. Consulté le 28 septembre 2026. [Page du cours](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c2/). Clé bibliographique : `mitcompstruct2017`.
