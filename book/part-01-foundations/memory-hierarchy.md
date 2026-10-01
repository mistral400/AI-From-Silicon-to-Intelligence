# Mémoire, bande passante et latence

> **Statut :** premier jet; sources et rendu PDF à valider.\
> **Date de rédaction :** 2026-10-01\
> **Prérequis :** connaître les registres et avoir lu le chapitre sur les processeurs

## Objectifs

À la fin du chapitre, tu pourras :

- situer les registres, caches, mémoires principales et stockages;
- distinguer capacité, latence et bande passante;
- expliquer la localité temporelle et spatiale;
- estimer si un calcul risque d’être limité par les opérations ou par les transferts de mémoire.

## En une phrase

Une hiérarchie de mémoire place de petites mémoires rapides près des unités de calcul et de plus grandes mémoires plus loin; le programme doit déplacer et réutiliser les données efficacement.

## Plusieurs mémoires, plusieurs rôles

Un processeur ne travaille pas directement avec une unique mémoire uniforme. Les registres se trouvent au plus près des unités d’exécution; les caches gardent des données récemment utilisées; la mémoire vive contient les programmes et données actifs; un SSD ou un disque conserve de grands volumes de façon persistante. Les GPU et accélérateurs ont également des registres, des caches et une mémoire locale ou partagée. Les noms et la disposition exacte dépendent de l’architecture. [Hennessy et Patterson (2019)](#ref-hennessypatterson2019)

| Niveau | Rôle typique | Propriété générale |
|---|---|---|
| Registres | Opérandes immédiatement traités par une unité | Très proches du calcul; capacité faible |
| Cache L1/L2/L3 | Réutiliser des lignes de mémoire récemment demandées | Rapide; capacité et partage varient selon le processeur |
| DRAM | Mémoire principale des CPU et de nombreux systèmes | Capacité plus grande; délai d’accès supérieur aux registres et caches |
| HBM ou mémoire locale du GPU | Alimenter certains GPU et accélérateurs avec un débit élevé | Placée près du processeur; capacité et organisation propres au produit |
| SSD ou disque | Conserver les fichiers et jeux de données | Persistant; les données doivent être chargées avant le calcul ordinaire |

Ce tableau décrit des catégories, pas une échelle universelle de temps ou de capacité. Deux processeurs peuvent avoir des tailles de cache, des protocoles de cohérence et des mémoires différentes.

## Capacité, latence et bande passante

La **capacité** est la quantité de données que la mémoire peut garder. La **latence** mesure le délai avant qu’une demande fournisse ses premières données. La **bande passante** mesure le volume de données transféré par unité de temps une fois le transfert en cours. Un système peut offrir une grande bande passante pour de nombreux transferts simultanés tout en conservant une latence notable pour chaque demande.

Ces grandeurs ne se remplacent pas. Ajouter de la capacité n’augmente pas nécessairement le débit; réduire la latence ne garantit pas une bande passante maximale; une large bande passante ne rend pas gratuite une donnée absente de la mémoire locale. Les analyses d’architecture distinguent ainsi le calcul et le coût de déplacement des opérandes. [Wulf et McKee (1995)](#ref-wulfmckee1995)

## Pourquoi les caches fonctionnent

Les caches exploitent deux formes de localité :

- **Localité temporelle :** une donnée récemment utilisée a des chances d’être réutilisée bientôt.
- **Localité spatiale :** après l’accès à une adresse, des adresses voisines ont des chances d’être utilisées.

Le cache transfère généralement des blocs de données plutôt qu’un seul octet. Un parcours séquentiel d’un tableau peut ainsi profiter de la localité spatiale. Réutiliser un élément plusieurs fois avant de le remplacer exploite la localité temporelle. Un accès dispersé peut gaspiller une grande partie des blocs transférés et provoquer davantage d’attentes. [Hennessy et Patterson (2019)](#ref-hennessypatterson2019)

Les caches masquent certains écarts de vitesse; ils ne suppriment pas le coût des accès. Si les données ne tiennent pas dans les niveaux rapides ou sont parcourues dans un ordre défavorable, le processeur peut attendre la mémoire. Cette attente est l’une des raisons pour lesquelles le volume d’opérations seul prédit mal le temps réel d’un programme. [Wulf et McKee (1995)](#ref-wulfmckee1995)

## Intensité arithmétique et modèle Roofline

On appelle **intensité arithmétique** le nombre d’opérations effectuées par octet transféré depuis un niveau de mémoire donné. Elle dépend donc de l’algorithme et du niveau de mémoire observé. Le modèle Roofline compare cette intensité aux capacités maximales de calcul et de bande passante :

\[
P \leq \min(P_{\mathrm{pic}},\ B \times I)
\]

où \(P\) est la performance atteignable, \(P_{\mathrm{pic}}\) la performance de calcul de pointe théorique pour le type d’opération considéré, \(B\) la bande passante du niveau de mémoire et \(I\) l’intensité arithmétique. Ce modèle donne une borne utile; il ne prédit pas exactement l’exécution, qui dépend aussi du parallélisme, des instructions et d’autres coûts. [Williams, Waterman et Patterson (2009)](#ref-williams2009roofline)

Si \(B \times I\) est inférieur à la capacité de calcul, le calcul risque d’être limité par le transfert des données. Si la borne de calcul est inférieure, il risque plutôt d’être limité par le nombre d’opérations réalisables. Réutiliser davantage une donnée peut augmenter \(I\), mais la stratégie doit tenir dans la mémoire rapide disponible.

### Exemple : données d’une multiplication matricielle

Calculons le volume idéal de transferts d’une multiplication de deux matrices carrées de \(1024 \times 1024\) éléments, stockées en format 32 bits :

1. La matrice d’entrée A occupe \(1024^2 \times 4\) octets, soit 4 Mio.
2. La matrice d’entrée B occupe également 4 Mio.
3. La matrice résultat C occupe 4 Mio.
4. Si chaque entrée est lue une fois et chaque résultat écrit une fois, le trafic total est de 12 Mio, soit 12 582 912 octets.

Avec une multiplication et une addition comptées comme deux opérations, le calcul demande environ \(2 \times 1024^3\), soit 2 147 483 648 opérations. Son intensité idéale est alors d’environ 171 opérations par octet. Ce chiffre suppose une réutilisation parfaite des entrées et n’est ni une mesure ni une garantie : un algorithme qui recharge souvent les données transfère davantage d’octets. Les stratégies par blocs cherchent notamment à conserver les sous-matrices en mémoire rapide pendant leur réutilisation. [Williams, Waterman et Patterson (2009)](#ref-williams2009roofline)

## Limites et pièges

- Une valeur en gigaoctets ne renseigne pas à elle seule sur la latence ou le débit.
- « Mémoire GPU » recouvre plusieurs niveaux de mémoire qui n’ont pas les mêmes propriétés.
- L’intensité arithmétique n’est définie qu’en précisant le niveau de mémoire et la manière de compter les opérations.
- L’estimation de 12 Mio ignore les défauts de cache, transferts répétés, alignements, temporaires et surcoûts du système.
- Une performance mesurée dépend de la taille des données, du logiciel, de la charge simultanée et de la configuration matérielle.

## À retenir

Les registres, caches, mémoires principales et stockages forment une hiérarchie de capacités, délais et débits différents. Les performances dépendent de l’endroit où se trouvent les données et du nombre de fois où elles sont réutilisées. L’intensité arithmétique aide à distinguer les calculs limités par le débit mémoire de ceux limités par le calcul, sans remplacer une mesure.

## Références

### Hennessy et Patterson (2019) {#ref-hennessypatterson2019}

- John L. Hennessy et David A. Patterson. *Computer Architecture: A Quantitative Approach*, 6e édition. Morgan Kaufmann, 2019. ISBN 978-0-12-811905-1.

### Wulf et McKee (1995) {#ref-wulfmckee1995}

- Wm. A. Wulf et Sally A. McKee. « Hitting the Memory Wall: Implications of the Obvious ». *Computer*, vol. 28, no 1, 1995, p. 20–24. [DOI : 10.1109/2.375176](https://doi.org/10.1109/2.375176).

### Williams, Waterman et Patterson (2009) {#ref-williams2009roofline}

- Samuel Williams, Andrew Waterman et David Patterson. « Roofline: An Insightful Visual Performance Model for Multicore Architectures ». *Communications of the ACM*, vol. 52, no 4, 2009, p. 65–76. [DOI : 10.1145/1498765.1498785](https://doi.org/10.1145/1498765.1498785).
