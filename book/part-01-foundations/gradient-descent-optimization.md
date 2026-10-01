# Optimisation et descente de gradient

> **Statut :** premier jet; sources et rendu PDF à valider.\
> **Date de rédaction :** 2026-10-01\
> **Prérequis :** fonctions, dérivées, gradients et règle de chaîne

## Objectifs

À la fin du chapitre, tu pourras :

- écrire la mise à jour de base de la descente de gradient;
- effectuer une étape sur une fonction simple;
- expliquer le rôle du taux d’apprentissage;
- distinguer perte d’entraînement, régularisation et garantie de convergence.

## En une phrase

La descente de gradient répète de petits déplacements dans une direction qui réduit localement une fonction objectif, à partir de ses dérivées.

## Une fonction objectif à minimiser

En apprentissage, les paramètres \(\boldsymbol{\theta}\) d’un modèle déterminent ses prédictions. Une fonction de perte \(L(\boldsymbol{\theta})\) mesure leur écart aux cibles sur les données choisies. L’entraînement cherche des paramètres qui réduisent cette perte, parfois avec des termes supplémentaires de régularisation. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

La descente de gradient effectue l’itération :

\[
\boldsymbol{\theta}_{t+1}
=
\boldsymbol{\theta}_{t}
- \eta \nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_{t})
\]

Ici, \(t\) désigne l’étape d’optimisation et \(\eta\) le taux d’apprentissage (*learning rate*). Le gradient indique la direction d’augmentation locale; la soustraction déplace les paramètres dans la direction opposée. Le taux d’apprentissage règle la longueur du déplacement.

## Exemple sur une fonction quadratique

Prenons :

\[
L(w)=(w-3)^2,
\qquad
\frac{dL}{dw}=2(w-3)
\]

Avec \(w_0=0\) et \(\eta=0{,}1\), le gradient initial vaut \(-6\). La première mise à jour donne :

\[
w_1 = 0 - 0{,}1(-6)=0{,}6
\]

La perte passe de \(L(0)=9\) à \(L(0{,}6)=5{,}76\). Pour cette fonction précise, l’erreur \(w_t-3\) est multipliée à chaque étape par \(1-2\eta\); la suite converge vers 3 lorsque \(0<\eta<1\). Cette condition est propre à cette courbe quadratique. Elle ne constitue pas une règle générale pour choisir \(\eta\) dans un réseau neuronal. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

Un taux trop faible peut rendre la progression très lente. Un taux trop élevé peut faire osciller les paramètres ou les éloigner de la zone recherchée. La valeur utile dépend de l’échelle et de la géométrie de la fonction objectif, ainsi que de la méthode d’optimisation.

## Données et mini-lots

Pour un jeu de données de \(N\) exemples, la perte moyenne peut s’écrire :

\[
L(\boldsymbol{\theta})
=
\frac{1}{N}\sum_{i=1}^{N} \ell_i(\boldsymbol{\theta})
\]

Calculer le gradient sur tous les exemples avant chaque mise à jour est appelé descente de gradient par lot complet. En pratique, beaucoup d’entraînements utilisent un mini-lot \(B\) et évaluent la moyenne des gradients sur ses exemples :

\[
\mathbf{g}_B
=
\frac{1}{|B|}\sum_{i\in B}\nabla_{\boldsymbol{\theta}}\ell_i(\boldsymbol{\theta}),
\qquad
\boldsymbol{\theta}_{t+1}
=
\boldsymbol{\theta}_{t}-\eta\mathbf{g}_B
\]

Les mini-lots réduisent le travail nécessaire à chaque mise à jour et exposent un calcul matriciel parallèle. Quand le mini-lot est plus petit que l’ensemble des données, son gradient peut varier d’une étape à l’autre; cette variation affecte la trajectoire d’optimisation. Les algorithmes adaptatifs modifient aussi la manière dont les gradients influencent chaque paramètre. Ils ont leurs propres paramètres et ne suppriment pas les choix de conception. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

## Régularisation : modifier l’objectif

Minimiser seulement la perte mesurée sur les exemples d’entraînement ne garantit pas de bonnes prédictions sur des exemples non vus. Une fonction objectif peut inclure un terme de régularisation :

\[
L_{\mathrm{total}}(\boldsymbol{\theta})
=
L_{\mathrm{données}}(\boldsymbol{\theta})
+ \lambda\,\Omega(\boldsymbol{\theta})
\]

\(\Omega\) pénalise une propriété des paramètres ou du modèle; \(\lambda\) en règle l’importance relative. Par exemple, une pénalité quadratique est proportionnelle à la somme des carrés des paramètres. Cette pénalité modifie la fonction que l’optimiseur minimise; elle ne garantit pas à elle seule une meilleure généralisation. La méthode, les données et le choix de \(\lambda\) comptent. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

## Ce que l’algorithme ne garantit pas

Pour une fonction convexe et sous des conditions adaptées, des résultats théoriques peuvent garantir une convergence vers un minimum. Les pertes des réseaux neuronaux sont généralement non convexes. La descente peut aboutir à des solutions différentes selon l’initialisation, l’ordre des exemples, le taux d’apprentissage et les autres paramètres. Trouver un point où le gradient s’annule ne prouve pas qu’on a trouvé le meilleur minimum global.

L’arrêt de l’entraînement peut donc s’appuyer sur des mesures séparées d’entraînement et de validation, ainsi que sur des critères définis pour la tâche. La baisse de la perte d’entraînement ne suffit pas à établir que le modèle se comporte bien sur de nouvelles données.

## Limites et pièges

- Le gradient donne une information locale; l’itération ne connaît pas la forme entière de la fonction.
- Le taux d’apprentissage agit sur toutes les mises à jour et peut rendre la progression instable s’il est mal choisi.
- La perte calculée sur un mini-lot varie avec les exemples qui le composent.
- La régularisation modifie l’objectif; elle ne remplace ni les données de validation ni l’évaluation.
- Une convergence numérique ne signifie pas automatiquement une bonne qualité de modèle.

## À retenir

La descente de gradient soustrait au paramètre un multiple de son gradient. Les mini-lots rendent les mises à jour plus fréquentes et exploitent les calculs matriciels, au prix d’une estimation variable du gradient complet. Le taux d’apprentissage, la fonction objectif, la régularisation et l’évaluation déterminent ensemble le résultat de l’entraînement.

## Références

### Goodfellow, Bengio et Courville (2016) {#ref-goodfellow2016}

- Ian Goodfellow, Yoshua Bengio et Aaron Courville. *Deep Learning*. MIT Press, 2016. Chapitre 8, « Optimization for Training Deep Models ». [Chapitre en ligne](https://www.deeplearningbook.org/contents/optimization.html).
