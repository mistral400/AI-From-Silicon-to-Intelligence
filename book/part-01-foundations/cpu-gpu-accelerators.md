# CPU, GPU et accélérateurs

> **Statut :** premier jet; sources et rendu PDF à valider.\
> **Date de rédaction :** 2026-10-01\
> **Prérequis :** bits, portes logiques, registres et circuits séquentiels

## Objectifs

À la fin du chapitre, tu pourras :

- décrire le cycle simplifié d’exécution d’une instruction par un CPU;
- expliquer pourquoi un GPU exécute beaucoup de travaux indépendants en parallèle;
- distinguer un processeur généraliste d’un accélérateur spécialisé;
- repérer les coûts qui empêchent de déduire la vitesse réelle d’une puce à partir de son nombre d’opérations théorique.

## En une phrase

CPU, GPU et accélérateurs sont des processeurs conçus avec des compromis différents entre flexibilité, latence, débit, consommation d’énergie et accès aux données.

## Du circuit au processeur

Le chapitre sur les [transistors et circuits séquentiels](transistors-logic-sequential.md) a présenté les briques matérielles : portes pour calculer, registres pour conserver les valeurs et horloge pour ordonner les mises à jour. Un processeur rassemble ces briques afin d’exécuter une suite d’instructions.

Dans un modèle pédagogique simple, le compteur ordinal indique l’adresse de la prochaine instruction. Le processeur lit cette instruction en mémoire, la décode, récupère ses opérandes, effectue l’opération demandée puis écrit le résultat dans un registre ou en mémoire. Les processeurs réels chevauchent ces étapes et peuvent exécuter plusieurs instructions en parallèle; le cycle décrit ici expose seulement les fonctions de base. [Hennessy et Patterson (2019)](#ref-hennessypatterson2019)

## CPU : flexibilité et réponse rapide

Un processeur central (CPU, *central processing unit*) est généraliste : son jeu d’instructions couvre des opérations entières, logiques, de contrôle et, selon le processeur, vectorielles ou flottantes. Un programme peut changer l’ordre des instructions, suivre des branches conditionnelles et traiter des tâches qui ne sont pas identiques les unes aux autres.

Pour réduire le temps d’attente, un cœur moderne peut utiliser des caches, prédire certaines branches, exécuter des instructions hors de leur ordre apparent et exploiter plusieurs unités fonctionnelles. Ces techniques ajoutent de la logique de contrôle et cherchent notamment à réduire la latence d’une tâche ou à maintenir le cœur occupé. Elles ne garantissent pas que toute suite d’instructions s’exécute en parallèle : les dépendances entre résultats et les décisions de contrôle peuvent limiter le parallélisme. [Hennessy et Patterson (2019)](#ref-hennessypatterson2019)

Le CPU convient donc à la coordination du système, aux tâches séquentielles ou irrégulières et aux opérations où la faible latence compte. Cette description est une tendance d’architecture, pas une règle absolue : un CPU comprend souvent lui aussi des unités vectorielles et plusieurs cœurs.

## GPU : débit sur des travaux parallèles

Un processeur graphique (GPU, *graphics processing unit*) comporte de nombreuses unités de calcul organisées pour exécuter un grand nombre de travaux. Une même opération peut être appliquée aux éléments d’un tableau, d’une image ou d’une matrice. Le GPU vise souvent un débit total élevé : le nombre de résultats produits sur une durée donnée.

Dans le modèle de programmation CUDA, le programme lance une grille de blocs et de threads. Les threads d’un groupe sont exécutés selon un modèle SIMT (*single instruction, multiple threads*) : ils suivent une instruction commune sur des données différentes, même si le matériel peut masquer des détails d’ordonnancement. Si les threads d’un groupe prennent des branches différentes, le processeur peut devoir exécuter les chemins séparément. Des accès mémoire mal regroupés peuvent aussi réduire le débit. Les détails varient selon le GPU et son modèle de programmation. [Guide de programmation CUDA](#ref-nvidiacudaguide)

Le GPU n’est donc pas automatiquement plus rapide pour chaque tâche. Le travail doit exposer assez de parallélisme, et le gain doit dépasser les coûts de lancement, de synchronisation et de circulation des données. Un petit calcul isolé peut prendre plus de temps sur un GPU si ces coûts dominent.

## Accélérateurs : circuits adaptés à une classe de calcul

Un accélérateur matériel est un processeur spécialisé pour certaines opérations ou contraintes. Il peut être un composant indépendant ou une unité intégrée à une puce. Son matériel et son logiciel peuvent accélérer un domaine précis, par exemple la multiplication de matrices, le traitement du signal ou le décodage vidéo, au prix d’une flexibilité différente de celle d’un CPU généraliste.

Le TPU de Google est un exemple documenté d’accélérateur conçu pour des opérations de réseaux neuronaux. L’article décrivant sa première génération en centre de données présente notamment une unité de calcul matriciel. Ce cas illustre un compromis d’ingénierie et ne décrit pas tous les TPU, GPU ou accélérateurs actuels. [Jouppi et al. (2017)](#ref-jouppi2017tpu)

Pour utiliser un accélérateur, le logiciel doit sélectionner ou compiler un calcul adapté, rendre les données accessibles au périphérique, lancer le travail puis récupérer ou consommer le résultat. La copie peut être évitée si le calcul et les données restent déjà dans une mémoire partagée ou locale au périphérique; les architectures diffèrent. Dans tous les cas, il faut comparer le coût total du chemin à la quantité de calcul effectivement accélérée. [Guide de programmation CUDA](#ref-nvidiacudaguide)

## Mesurer sans confondre débit et latence

Deux mesures répondent à des questions différentes :

- **Latence :** combien de temps une tâche ou une requête prend de son début à son résultat.
- **Débit :** combien de tâches ou de résultats sont produits par unité de temps.

Un processeur peut augmenter le débit en traitant plusieurs tâches simultanément sans diminuer la latence d’une tâche isolée. De même, une fréquence d’horloge plus haute ne garantit pas une accélération proportionnelle : le nombre d’instructions par cycle, les dépendances, les accès mémoire, la puissance et le logiciel comptent aussi. [Hennessy et Patterson (2019)](#ref-hennessypatterson2019)

Pour un calcul matriciel, le volume d’opérations peut être grand et régulier, ce qui en fait une cible naturelle pour le parallélisme. Mais les matrices doivent être chargées, les blocs de travail distribués et les résultats écrits. Le chapitre sur le [calcul matriciel et la précision numérique](matrix-computation.md) décrira ces opérations; celui sur la [mémoire et sa hiérarchie](memory-hierarchy.md) expliquera les échanges de données qui bornent les performances.

## Limites et pièges

- Un GPU ou un accélérateur n’est pas plus rapide pour toute charge de travail.
- Le nombre d’unités de calcul ne suffit pas à prédire la performance d’un programme.
- La latence, le débit et le temps d’exécution total sont des mesures différentes.
- Les noms de familles de puces cachent des générations et des configurations variées; les caractéristiques doivent être vérifiées pour un modèle précis.
- Le matériel peut exécuter une même opération à des précisions différentes. Le choix doit tenir compte de la qualité numérique attendue.

## À retenir

Le CPU privilégie la flexibilité et l’exécution efficace de tâches variées. Le GPU vise un débit élevé lorsque de nombreux travaux indépendants peuvent être exécutés ensemble. Un accélérateur specialise davantage son matériel et son logiciel pour certaines opérations. Pour comparer ces processeurs, il faut inclure l’algorithme, le parallélisme disponible et le trajet des données.

## Références

### Hennessy et Patterson (2019) {#ref-hennessypatterson2019}

- John L. Hennessy et David A. Patterson. *Computer Architecture: A Quantitative Approach*, 6e édition. Morgan Kaufmann, 2019. ISBN 978-0-12-811905-1.

### Guide de programmation CUDA {#ref-nvidiacudaguide}

- NVIDIA. *CUDA C++ Programming Guide*. Documentation technique en ligne sur le modèle d’exécution, les threads et les mémoires CUDA. [Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/). Version et date de consultation à confirmer lors de la relecture des sources.

### Jouppi et al. (2017) {#ref-jouppi2017tpu}

- Norman P. Jouppi et al. « In-Datacenter Performance Analysis of a Tensor Processing Unit ». *Proceedings of the 44th Annual International Symposium on Computer Architecture*, 2017, p. 1–12. [DOI : 10.1145/3079856.3080246](https://doi.org/10.1145/3079856.3080246).
