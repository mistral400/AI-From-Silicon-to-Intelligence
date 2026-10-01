# Transistors, portes logiques et circuits séquentiels

> **Statut :** premier jet; vérification du PDF en attente  
> **Vérification des sources :** 2026-09-30  
> **Prérequis :** niveaux logiques, bits et nombres entiers

## Objectifs

À la fin du chapitre, tu pourras :

- expliquer comment un MOSFET sert d’interrupteur commandé par une tension;
- décrire comment deux types de MOSFET forment un inverseur CMOS;
- lire des portes logiques à partir de leur fonction booléenne;
- distinguer logique combinatoire, latch et bascule;
- expliquer pourquoi un registre et une horloge sont nécessaires pour construire un processeur.

## En une phrase

Des transistors MOSFET assemblés en circuits CMOS réalisent les fonctions logiques; des latches et des bascules ajoutent la mémoire qui permet à un circuit de conserver un état entre deux calculs.

## Intuition : du signal au calcul puis à l’état

Le chapitre précédent a montré qu’un bit est une convention appliquée à des plages de tension. Il reste à voir comment le matériel transforme ces tensions. Un transistor agit comme un interrupteur commandé par un signal; plusieurs transistors forment une porte logique, plusieurs portes forment un calcul, et des circuits avec rétroaction peuvent conserver un résultat.

Cette progression explique pourquoi le processeur n’est pas un composant mystérieux séparé des portes. Un registre est construit à partir de circuits qui gardent un bit; une unité arithmétique et logique (ALU) combine des portes pour additionner, comparer ou appliquer des opérations bit à bit. Plus tard, les mêmes idées de registres et de calcul combinatoire réapparaissent dans les processeurs graphiques et les accélérateurs d’IA.

## Le transistor MOSFET

### Un interrupteur commandé électriquement

Le transistor à effet de champ métal-oxyde-semiconducteur (MOSFET, *metal-oxide-semiconductor field-effect transistor*) est un composant dont une tension de commande influence le courant entre deux bornes. Dans le modèle simplifié utilisé pour raisonner sur la logique, on le traite comme un interrupteur : il relie ou isole deux nœuds selon l’état de sa grille. Un MOSFET réel a des comportements analogiques, des délais et des courants de fuite; le modèle d’interrupteur est une abstraction utile, pas la description complète de sa physique. [MIT OpenCourseWare, CMOS (2017)](#ref-mitcompstructcmos2017)

Un MOSFET comporte une grille (*gate*), une source (*source*), un drain (*drain*) et un corps ou substrat (*body*). La grille est séparée du silicium par une couche isolante très mince. Sa tension crée un champ électrique qui peut établir un canal conducteur entre source et drain. Pour un transistor à canal N (*nMOS*), le canal devient conducteur lorsque la tension grille-source dépasse suffisamment son seuil. Pour un transistor à canal P (*pMOS*), la polarité est inversée : il conduit lorsque la grille est assez basse relativement à sa source. La tension de seuil et le courant réel dépendent du procédé et des conditions; il n’existe pas une valeur universelle à appliquer à tous les transistors.

Dans la logique CMOS (*complementary metal-oxide-semiconductor*), les nMOS et pMOS sont utilisés ensemble. Le réseau nMOS relie au besoin la sortie à la masse; le réseau pMOS la relie au besoin à la tension d’alimentation. Les deux réseaux sont construits pour se compléter : en régime stable, l’un fournit un chemin vers un rail tandis que l’autre le bloque. C’est cette complémentarité qui permet de reconstruire une sortie proche d’un niveau logique valide. [MIT OpenCourseWare, CMOS (2017)](#ref-mitcompstructcmos2017)

## Inverseur CMOS : le premier circuit logique

Considérons un inverseur, qui réalise la négation logique. Une même entrée commande les grilles du nMOS et du pMOS; leurs autres bornes forment les chemins entre l’alimentation, la sortie et la masse.

| Entrée A | nMOS côté masse | pMOS côté alimentation | Sortie Y |
|---:|---|---|---:|
| 0 | bloqué | conducteur | 1 |
| 1 | conducteur | bloqué | 0 |

Quand A vaut 0, le nMOS ne relie pas la sortie à la masse et le pMOS la tire vers l’alimentation : Y vaut 1. Quand A vaut 1, le pMOS se bloque et le nMOS relie la sortie à la masse : Y vaut 0. La fonction est donc :

\[
Y = \neg A
\]

Ici, A et Y sont des valeurs logiques; \(\neg\) signifie « non ». Si A vaut 0, \(\neg A\) vaut 1, et inversement. La tension de sortie réelle n’est pas nécessairement exactement égale à 0 V ou à l’alimentation, mais elle doit respecter les seuils garantis du récepteur pour être interprétée sans ambiguïté.

À l’instant où l’entrée change, les transistors ne basculent pas instantanément d’un état parfait à l’autre. Il existe un délai de propagation, et le niveau de sortie traverse une plage transitoire. Le circuit numérique spécifie des bornes de délai et de tension; entre ces bornes, le signal ne doit pas être traité comme une valeur stable. [MIT OpenCourseWare, CMOS (2017)](#ref-mitcompstructcmos2017)

## Des portes à plusieurs entrées

Une porte logique décrit une fonction booléenne sur des entrées 0 et 1. L’inverseur donne NON; la porte ET (*AND*) vaut 1 seulement si toutes ses entrées valent 1; la porte OU (*OR*) vaut 1 si au moins une entrée vaut 1. La table de vérité énumère les cas et fixe la fonction sans dépendre de son implémentation physique.

| A | B | A ET B | A OU B | NON (A ET B) |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

La dernière colonne est la porte NON-ET, ou NAND : \(Y = \neg(A \land B)\). Dans un CMOS simple, deux nMOS en série forment le chemin de sortie vers la masse, qui ne conduit que si A et B valent tous deux 1. Le réseau pMOS complémentaire met ses transistors en parallèle : si l’une des entrées vaut 0, un chemin ramène la sortie vers l’alimentation. La sortie est donc 0 uniquement pour \(A=B=1\). Le raisonnement se généralise en échangeant séries et parallèles et en remplaçant nMOS par pMOS pour construire des fonctions complémentaires. [MIT OpenCourseWare, CMOS (2017)](#ref-mitcompstructcmos2017)

NAND et NON-OU (*NOR*) sont des formes naturellement inversées. Une porte ET peut se construire comme une NAND suivie d’un inverseur; une porte OU peut se construire comme une NOR suivie d’un inverseur. NAND et NOR sont aussi des portes universelles : des assemblages de portes d’un seul de ces types peuvent réaliser toute fonction booléenne. Ce résultat vient notamment des lois de De Morgan, par exemple \(\neg(A \land B) = (\neg A) \lor (\neg B)\). [MIT OpenCourseWare, logique combinatoire (2017)](#ref-mitcompstructcomb2017)

## Logique combinatoire : calculer à partir des entrées présentes

Un circuit combinatoire (*combinational logic*) produit une sortie définie par les entrées courantes. Il ne garde pas, à lui seul, le résultat d’un calcul précédent. Une table de vérité et une équation booléenne sont deux façons équivalentes de décrire cette fonction; les portes réalisent ensuite cette fonction électrique. [MIT OpenCourseWare, logique combinatoire (2017)](#ref-mitcompstructcomb2017)

Un exemple à deux entrées est un demi-additionneur (*half adder*), qui additionne deux bits A et B. Le bit de somme vaut \(S = A \oplus B\), où \(\oplus\) signifie OU exclusif; le bit de retenue vaut \(C = A \land B\). Pour A = 1 et B = 1, la somme vaut 0 et la retenue vaut 1 : en binaire, \(1 + 1 = 10_2\). Des demi-additionneurs et d’autres portes permettent de construire des additionneurs de largeur supérieure, puis l’ALU présentée dans le chapitre sur le CPU.

En pratique, une porte met un temps fini à répondre. Une chaîne de portes peut aussi produire de brèves transitions parasites, appelées glitches, pendant que ses signaux se stabilisent. Dans un circuit combinatoire, on ne doit donc pas supposer qu’une sortie est correcte immédiatement après un changement d’entrée. Il faut laisser passer le délai maximal spécifié par le chemin concerné. [MIT OpenCourseWare, logique combinatoire (2017)](#ref-mitcompstructcomb2017)

## Circuits séquentiels : conserver un résultat

Pour garder un bit après la disparition de son entrée, un circuit doit utiliser de la rétroaction. Une sortie est renvoyée vers l’intérieur du circuit; dans une boucle bistable, cette rétroaction maintient l’un de deux états stables. Un latch (verrou sensible à un niveau) et une bascule D (bascule sensible à un front) sont deux éléments de mémoire utilisés pour créer des circuits séquentiels. [MIT OpenCourseWare, logique séquentielle (2017)](#ref-mitcompstructseq2017)

### Le latch D est sensible à un niveau

Un latch D possède une entrée de donnée D, une sortie Q et une entrée de validation EN (*enable*). Dans la convention active-haute illustrée ici, lorsque EN vaut 1, Q suit D. Lorsque EN revient à 0, le latch conserve la dernière valeur prise par Q. Il est donc transparent pendant une partie du temps où il est ouvert; il ne réagit pas uniquement à un instant. [MIT OpenCourseWare, logique séquentielle (2017)](#ref-mitcompstructseq2017)

| EN | Comportement |
|---:|---|
| 0 | Q garde son état précédent |
| 1 | Q suit D |

### La bascule D échantillonne sur un front

Une bascule D déclenchée par le front montant prélève la valeur de D autour du passage de l’horloge de 0 à 1, puis maintient cette valeur à Q jusqu’au prochain front actif. Une réalisation classique utilise deux latches en série, appelés maître et esclave, commandés pendant des phases opposées de l’horloge. Le premier capture la donnée; le second met à jour la sortie au front prévu. Les termes « bascule » et « registre » varient selon les cours et les bibliothèques : un registre de plusieurs bits regroupe généralement plusieurs éléments de stockage commandés par la même horloge. [MIT OpenCourseWare, logique séquentielle (2017)](#ref-mitcompstructseq2017)

La donnée D doit rester stable pendant une durée minimale avant le front, appelée temps de préparation (*setup time*), et après le front, appelée temps de maintien (*hold time*). Si ces contraintes ne sont pas respectées, le stockage n’est pas garanti; les circuits réels précisent ces limites dans leurs caractéristiques temporelles. [MIT OpenCourseWare, logique séquentielle (2017)](#ref-mitcompstructseq2017)

### Registre et période d’horloge

Un registre de 32 bits peut être construit à partir de 32 bascules D partageant la même horloge. Il mémorise un mot binaire; une autre partie du circuit calcule la prochaine valeur qui devra y être écrite. Cela donne le schéma de base d’un système synchrone : des registres conservent les états, la logique combinatoire calcule entre eux, puis une transition d’horloge met à jour les états.

Pour que la valeur calculée arrive à temps au registre suivant, la période d’horloge doit être assez longue. Dans un exemple simplifié :

\[
T_{\mathrm{clk}} \geq t_{\mathrm{CQ}} + t_{\mathrm{logic,max}} + t_{\mathrm{setup}}
\]

où \(T_{\mathrm{clk}}\) est le temps entre deux fronts actifs, \(t_{\mathrm{CQ}}\) le délai maximal entre le front et une sortie du premier registre, \(t_{\mathrm{logic,max}}\) le délai maximal du chemin combinatoire, et \(t_{\mathrm{setup}}\) le temps de préparation du registre suivant. La relation ignore ici le décalage entre horloges, le jitter et d’autres marges de conception.

Prenons \(t_{\mathrm{CQ}}=1\ \text{ns}\), \(t_{\mathrm{logic,max}}=4\ \text{ns}\) et \(t_{\mathrm{setup}}=1\ \text{ns}\). La période doit être au moins \(6\ \text{ns}\), donc la fréquence correspondante ne peut pas dépasser environ \(1/(6\ \text{ns}) = 166{,}7\ \text{MHz}\) dans ce modèle. Il s’agit d’un calcul illustratif, pas d’une mesure de puce. Ajouter un registre au milieu d’un long chemin peut permettre une horloge plus rapide, au prix d’une étape supplémentaire et d’une latence de plusieurs cycles. [MIT OpenCourseWare, logique séquentielle (2017)](#ref-mitcompstructseq2017)

## Pourquoi cela mène aux processeurs et à l’IA

Le transistor permet de fabriquer des portes; les portes réalisent des opérations booléennes; les circuits séquentiels gardent les bits entre les opérations. Un processeur combine ainsi des registres, une ALU, des chemins de données et du contrôle. Un GPU répète et parallélise une partie de ces opérations. Dans un accélérateur d’IA, des réseaux de portes et de mémoires font exécuter des opérations sur des vecteurs et des matrices, tandis que les registres et les mémoires gardent les opérandes et les résultats disponibles.

Cette chaîne matérielle est le premier lien entre le silicium et l’apprentissage automatique. Le chapitre sur les [CPU, GPU et accélérateurs](cpu-gpu-accelerators.md) présente leurs compromis; ceux sur la [mémoire](memory-hierarchy.md) et le [calcul matriciel](matrix-computation.md) expliquent le mouvement des données et les opérations qui dominent de nombreux modèles.

## Limites et pièges

- Le MOSFET n’est pas un interrupteur idéal : seuil, courant de fuite, capacité et délai dépendent du composant et de ses conditions d’utilisation.
- Les valeurs 0 et 1 sont des plages de tension interprétées selon des seuils; elles ne sont pas des tensions exactes.
- Une sortie combinatoire peut transiter ou glitcher avant de se stabiliser.
- Le latch est sensible à un niveau de validation; la bascule D échantillonne à un front d’horloge.
- Les contraintes de setup et de hold sont essentielles; la fréquence d’une puce ne se déduit pas d’un unique délai de porte.

## À retenir

Un MOSFET commandé par tension sert d’élément de commutation. Le CMOS assemble nMOS et pMOS en réseaux complémentaires pour produire les niveaux logiques; ces transistors construisent des portes comme NAND et NOR. Des latches et des bascules ajoutent l’état, et des registres synchronisés organisent les calculs au rythme d’une horloge. C’est cette combinaison qui permet de passer des bits aux processeurs puis aux accélérateurs utilisés pour l’IA.

## Références

### MIT OpenCourseWare, CMOS (2017) {#ref-mitcompstructcmos2017}

- MIT OpenCourseWare. « 3 CMOS », *Computation Structures*, cours 6.004, printemps 2017. Transistors MOSFET, inverseurs, réseaux complémentaires et délais. Consulté le 30 septembre 2026. [Page du cours](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c3/c3s1/). Clé BibTeX : mitcompstructcmos2017.

### MIT OpenCourseWare, logique combinatoire (2017) {#ref-mitcompstructcomb2017}

- MIT OpenCourseWare. « 4 Combinational Logic », *Computation Structures*, cours 6.004, printemps 2017. Tables de vérité, fonctions booléennes et implémentations par portes. Consulté le 30 septembre 2026. [Page du cours](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/). Clé BibTeX : mitcompstructcomb2017.

### MIT OpenCourseWare, logique séquentielle (2017) {#ref-mitcompstructseq2017}

- MIT OpenCourseWare. « 5 Sequential Logic », *Computation Structures*, cours 6.004, printemps 2017. Latches, registres, fronts d’horloge et contraintes temporelles. Consulté le 30 septembre 2026. [Page du cours](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c5/c5s1/). Clé BibTeX : mitcompstructseq2017.
