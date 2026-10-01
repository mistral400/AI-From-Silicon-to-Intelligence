# Probabilités, entropie et information

> **Statut :** premier jet; sources et rendu PDF à valider.\
> **Date de rédaction :** 2026-10-01\
> **Prérequis :** fractions, logarithmes et vecteurs

## Objectifs

À la fin du chapitre, tu pourras :

- lire une probabilité et une probabilité conditionnelle;
- appliquer le théorème de Bayes à un exemple avec un taux de base;
- calculer l’information et l’entropie d’une distribution simple;
- distinguer entropie, surprise et information mutuelle.

## En une phrase

La probabilité décrit l’incertitude sur des résultats possibles; l’entropie mesure l’incertitude moyenne d’une distribution, en bits lorsque le logarithme est en base 2.

## Événements et variables aléatoires

Un modèle probabiliste décrit un ensemble de résultats possibles. Un **événement** est un ensemble de résultats auquel on associe une probabilité comprise entre 0 et 1. Une **variable aléatoire** associe une valeur numérique à chaque résultat; sa distribution indique la probabilité de chaque valeur.

Pour une variable discrète \(X\), notons \(p(x)=P(X=x)\). Les probabilités sont positives et leur somme vaut 1. La probabilité d’un ensemble de valeurs se trouve en additionnant leurs probabilités. L’espérance de \(X\) est sa moyenne théorique :

\[
\mathbb{E}[X] = \sum_x p(x)x
\]

Pour un dé équilibré à six faces, chacune des valeurs a une probabilité \(1/6\), et l’espérance vaut \((1+2+3+4+5+6)/6=3{,}5\). Cela ne signifie pas que le résultat d’un lancer puisse être 3,5 : l’espérance décrit la moyenne à long terme, pas une issue possible. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

## Probabilité conditionnelle et taux de base

La probabilité de A sachant que B s’est produit se définit, lorsque \(P(B)>0\), par :

\[
P(A\mid B) = \frac{P(A\cap B)}{P(B)}
\]

Elle peut différer de \(P(A)\). Deux événements A et B sont indépendants si connaître B ne change pas la probabilité de A; alors \(P(A\cap B)=P(A)P(B)\). La formule de Bayes inverse le conditionnement :

\[
P(A\mid B) = \frac{P(B\mid A)P(A)}{P(B)}
\]

### Exemple synthétique : un résultat positif

Supposons, à titre d’exemple fictif, que 1 % d’une population présente une caractéristique A. Un test est positif pour 90 % des personnes qui la présentent et pour 5 % des personnes qui ne la présentent pas. La proportion de résultats positifs est :

\[
P(+) = 0{,}90\times0{,}01 + 0{,}05\times0{,}99
= 0{,}0585
\]

Parmi les résultats positifs, la probabilité que la personne présente A est donc :

\[
P(A\mid +) = \frac{0{,}90\times0{,}01}{0{,}0585}
\approx 0{,}154
\]

Elle vaut environ 15,4 %, malgré un taux de détection de 90 %. La rareté initiale de A et les faux positifs comptent tous deux. Ces nombres sont inventés pour illustrer le calcul; ils ne décrivent aucun test réel. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

## Surprise et entropie

Dans la théorie de Shannon, l’information propre à un résultat \(x\) de probabilité \(p(x)>0\) est :

\[
I(x) = -\log_2 p(x)
\]

Un résultat rare a une surprise plus grande qu’un résultat fréquent. Un événement de probabilité \(1/2\) apporte 1 bit de surprise; un événement de probabilité \(1/8\) en apporte 3. Cette quantité dépend du modèle probabiliste utilisé : si le modèle se trompe sur les probabilités, ses surprises estimées ne correspondent pas aux fréquences réelles. [Shannon (1948)](#ref-shannon1948communication)

L’entropie est la surprise moyenne d’une variable discrète :

\[
H(X) = -\sum_x p(x)\log_2 p(x)
\]

Le logarithme en base 2 donne une unité en bits. Pour un événement de probabilité nulle, le terme correspondant est défini par la limite \(0\log_2 0=0\).

Pour une pièce équilibrée, \(H=1\) bit : chaque côté a une probabilité \(1/2\). Pour une pièce qui donne pile avec probabilité \(0{,}9\) et face avec probabilité \(0{,}1\), on obtient :

\[
H = -0{,}9\log_2 0{,}9 - 0{,}1\log_2 0{,}1
\approx 0{,}469\ \text{bit}
\]

L’entropie est plus faible parce qu’un côté est beaucoup plus prévisible. Pour un dé équilibré, elle vaut \(\log_2 6 \approx 2{,}585\) bits. Parmi les distributions sur un nombre fixé d’issues, la distribution uniforme a l’entropie maximale. [Shannon (1948)](#ref-shannon1948communication)

## Information mutuelle : dépendance entre variables

L’entropie conditionnelle \(H(X\mid Y)\) mesure l’incertitude moyenne restante sur X lorsqu’on connaît Y. L’information mutuelle compare l’incertitude initiale à celle qui reste :

\[
I(X;Y) = H(X)-H(X\mid Y)
\]

Elle vaut zéro lorsque X et Y sont indépendantes et augmente lorsque connaître Y réduit l’incertitude sur X. Elle est symétrique : \(I(X;Y)=I(Y;X)\). Cette mesure décrit une dépendance statistique; elle ne prouve pas qu’une variable cause l’autre. [Shannon (1948)](#ref-shannon1948communication)

## Pont vers les pertes des modèles

Si une distribution vraie \(p\) est comparée à une distribution prédite \(q\), leur entropie croisée s’écrit :

\[
H(p,q) = -\sum_x p(x)\log_2 q(x)
\]

Elle pénalise les modèles qui attribuent peu de probabilité aux résultats observés. L’entropie croisée est une composante fréquente des fonctions de perte pour la classification et la prédiction du prochain token. Son lien avec l’apprentissage sera étudié avec les fonctions de perte et l’entraînement des réseaux neuronaux. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

## Limites et pièges

- Une probabilité exprime un modèle ou une fréquence à long terme; elle ne garantit pas l’issue d’un essai individuel.
- Une probabilité conditionnelle dépend de l’événement placé après la barre; inverser \(P(A\mid B)\) en \(P(B\mid A)\) est généralement incorrect.
- Un résultat très improbable est surprenant sous le modèle retenu, mais cela ne suffit pas à montrer que le modèle ou l’observation sont erronés.
- L’entropie résume une distribution; elle ne mesure pas directement la signification, la complexité ou l’utilité d’une donnée.
- L’information mutuelle détecte une dépendance statistique, pas une relation de cause à effet.

## À retenir

Les probabilités décrivent les issues possibles et leurs chances. Le conditionnement met à jour ces chances lorsqu’une information est connue; Bayes relie le résultat à son taux de base. L’information propre d’un résultat est liée à sa rareté, et l’entropie en est la moyenne. Ces outils fournissent le langage de l’incertitude et préparent l’étude des pertes probabilistes en apprentissage automatique.

## Références

### Shannon (1948) {#ref-shannon1948communication}

- Claude E. Shannon. « A Mathematical Theory of Communication ». *The Bell System Technical Journal*, vol. 27, no 3, 1948, p. 379–423. [DOI : 10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x).

### Goodfellow, Bengio et Courville (2016) {#ref-goodfellow2016}

- Ian Goodfellow, Yoshua Bengio et Aaron Courville. *Deep Learning*. MIT Press, 2016. Chapitre 3, « Probability and Information Theory ». [Chapitre en ligne](https://www.deeplearningbook.org/contents/prob.html).
