# Fonctions, dérivées, gradients et règle de chaîne

> **Statut :** premier jet; sources et rendu PDF à valider.\
> **Date de rédaction :** 2026-10-01\
> **Prérequis :** opérations sur les nombres, vecteurs et matrices

## Objectifs

À la fin du chapitre, tu pourras :

- décrire une fonction comme une règle qui associe une sortie à une entrée;
- interpréter la dérivée comme un taux de variation local;
- calculer une dérivée partielle et un gradient;
- utiliser la règle de chaîne pour suivre l’effet d’un paramètre sur une perte.

## En une phrase

Une dérivée mesure la variation locale d’une sortie quand une entrée change; le gradient rassemble les dérivées partielles d’une fonction à plusieurs paramètres et la règle de chaîne relie les variations à travers plusieurs calculs.

## Fonctions : des entrées vers des sorties

Une fonction \(f\) associe une sortie \(y\) à une entrée \(x\), selon une règle :

\[
y = f(x)
\]

Par exemple, \(f(x)=3x+2\) associe 11 à \(x=3\). Une fonction peut prendre un vecteur en entrée et rendre un scalaire, un vecteur ou un tableau. En apprentissage automatique, un modèle est une fonction paramétrée : changer ses paramètres change ses sorties. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

## Dérivée : pente locale d’une fonction

Pour une fonction scalaire \(f(x)\), la dérivée en un point \(x\) est la limite de son taux de variation lorsque l’écart entre deux entrées tend vers zéro :

\[
f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}
\]

Géométriquement, elle correspond à la pente de la tangente au graphe, si cette pente est définie. Pour \(f(x)=x^2\), la dérivée vaut \(f'(x)=2x\). Au point \(x=3\), la pente locale vaut 6 : une petite variation \(\Delta x\) produit approximativement une variation \(6\Delta x\) de la sortie, si \(\Delta x\) est assez petit.

Cette approximation est locale. Elle ne dit pas que la fonction entière est une droite; elle décrit ce qui se passe près du point choisi. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

## Dérivées partielles et gradient

Une fonction \(L\) peut dépendre de plusieurs paramètres \(\theta_1,\ldots,\theta_n\). Sa dérivée partielle par rapport à \(\theta_i\) mesure la variation de \(L\) si l’on change ce paramètre en maintenant les autres fixes. Le gradient est le vecteur qui rassemble ces dérivées :

\[
\nabla_{\boldsymbol{\theta}} L =
\begin{bmatrix}
\frac{\partial L}{\partial \theta_1} \\
\frac{\partial L}{\partial \theta_2} \\
\vdots \\
\frac{\partial L}{\partial \theta_n}
\end{bmatrix}
\]

Pour une petite modification \(\Delta\boldsymbol{\theta}\), la variation de la fonction peut être approchée au premier ordre par :

\[
\Delta L \approx \nabla_{\boldsymbol{\theta}} L \cdot \Delta\boldsymbol{\theta}
\]

Sous la géométrie euclidienne usuelle, le gradient indique la direction de plus forte augmentation locale. Le vecteur opposé indique une direction de diminution locale; cela ne garantit pas que suivre cette direction mène au minimum global. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

Les conventions de calcul matriciel peuvent écrire le gradient en ligne ou en colonne. Le contenu reste la collection des dérivées; il faut respecter la convention lorsqu’on multiplie gradients, vecteurs ou jacobiennes.

## Règle de chaîne : suivre une composition

Si une quantité \(z\) dépend de \(w\) par l’intermédiaire de \(y\), la règle de chaîne multiplie les taux de variation locaux :

\[
\frac{\partial z}{\partial w}
=
\frac{\partial z}{\partial y}
\frac{\partial y}{\partial w}
\]

Considérons un calcul simple, proche d’un neurone :

\[
y = wx+b,
\qquad
L = \frac{1}{2}(y-t)^2
\]

Ici, \(x\) est une entrée, \(w\) un poids, \(b\) un biais, \(t\) la valeur cible et \(L\) une perte. D’abord :

\[
\frac{\partial L}{\partial y}=y-t,
\qquad
\frac{\partial y}{\partial w}=x,
\qquad
\frac{\partial y}{\partial b}=1
\]

La règle de chaîne donne alors :

\[
\frac{\partial L}{\partial w}=(y-t)x,
\qquad
\frac{\partial L}{\partial b}=y-t
\]

Avec \(x=2\), \(w=1\), \(b=0\) et \(t=3\), la sortie vaut \(y=2\). Les dérivées sont \(\partial L/\partial w=-2\) et \(\partial L/\partial b=-1\). Elles décrivent comment la perte changerait localement si l’on modifiait un poids ou un biais. Dans un réseau profond, la rétropropagation applique la même règle à une suite de couches; elle calcule ces dérivées sans énumérer chaque combinaison de paramètres. [Goodfellow, Bengio et Courville (2016)](#ref-goodfellow2016)

## Limites et pièges

- Une dérivée décrit une variation locale et dépend du point où elle est calculée.
- Un gradient égal à zéro peut apparaître à un minimum, un maximum ou un point selle; il ne classe pas le point à lui seul.
- La règle de chaîne donne des dérivées de la fonction représentée par le calcul, sous réserve que les opérations concernées soient différentiables ou traitées par une convention définie.
- Les unités des dérivées dépendent de celles de la sortie et du paramètre.
- L’ordre des dimensions et les conventions de gradient changent entre bibliothèques.

## À retenir

La dérivée d’une fonction décrit sa pente locale. Pour plusieurs paramètres, le gradient regroupe toutes les dérivées partielles. La règle de chaîne permet de propager une variation au travers de calculs successifs; c’est la base mathématique du calcul des gradients dans un réseau neuronal.

## Références

### Goodfellow, Bengio et Courville (2016) {#ref-goodfellow2016}

- Ian Goodfellow, Yoshua Bengio et Aaron Courville. *Deep Learning*. MIT Press, 2016. Chapitres sur le calcul différentiel, les réseaux feedforward et l’apprentissage fondé sur le gradient. [Livre et chapitres en ligne](https://www.deeplearningbook.org/).
