# Glossaire

Ce glossaire définit les termes déjà utilisés dans les chapitres disponibles. Il sera complété avec les parties sur les Transformers, l’inférence, l’entraînement et l’infrastructure.

## A–C

**Activation, fonction d’ —** fonction non linéaire appliquée au résultat d’une transformation affine dans un neurone, par exemple ReLU ou GELU.

**Additionneur —** circuit combinatoire qui additionne des bits et produit les bits de somme et de retenue.

**ALU (*arithmetic logic unit*, unité arithmétique et logique) —** partie d’un processeur qui effectue des opérations arithmétiques et booléennes.

**Bande passante mémoire —** quantité de données qu’une interface mémoire peut transférer par unité de temps, souvent exprimée en octets par seconde.

**Biais —** paramètre ajouté au produit pondéré des entrées d’un neurone; il permet de décaler la transformation ou son seuil.

**Bit —** unité d’information binaire qui distingue deux états, conventionnellement notés 0 et 1.

**Cache —** mémoire de petite capacité et d’accès rapide qui conserve des données susceptibles d’être réutilisées.

**Circuit combinatoire —** circuit dont la sortie dépend des entrées présentes, sans état mémorisé par le circuit lui-même.

**Circuit séquentiel —** circuit qui combine logique et état mémorisé; son état suivant dépend des entrées et de l’état actuel.

**CMOS (*complementary metal-oxide-semiconductor*) —** famille de circuits logiques qui associe des transistors pMOS et nMOS complémentaires.

**CPU (*central processing unit*, processeur central) —** processeur polyvalent qui exécute des instructions et coordonne des calculs et transferts de données.

## D–G

**Dérivée —** taux de variation local d’une fonction par rapport à une variable; elle donne sa pente instantanée lorsque la fonction est dérivable.

**Format (*shape*) —** suite des dimensions des axes d’un tableau numérique, par exemple 3 × 2 pour trois lignes et deux colonnes.

**Fonction de perte —** quantité numérique qui mesure l’écart entre une prédiction et la cible selon un objectif défini.

**GELU (*Gaussian Error Linear Unit*) —** fonction d’activation \(x\Phi(x)\), où \(\Phi\) est la fonction de répartition normale standard.

**Gradient —** vecteur des dérivées partielles d’une fonction par rapport à ses variables; pour une perte, il décrit sa variation locale avec les paramètres.

**GPU (*graphics processing unit*, processeur graphique) —** processeur conçu pour exécuter en parallèle de nombreuses opérations, aujourd’hui aussi utilisé pour le calcul scientifique et l’IA.

## L–P

**Latence —** durée entre une demande ou un événement et l’obtention de sa réponse ou de son effet.

**Logit —** score réel produit avant normalisation probabiliste, souvent par la dernière couche d’un classifieur.

**Matrice —** tableau de nombres à deux axes, décrits par le nombre de lignes et de colonnes.

**Mémoire vive (RAM) —** mémoire de travail accessible par les processeurs; son contenu est généralement perdu à la coupure de l’alimentation.

**Neurone artificiel —** unité de calcul qui combine une somme pondérée de ses entrées, un biais et une fonction d’activation.

**NPU (*neural processing unit*) —** nom générique de certains accélérateurs pour des opérations courantes en apprentissage automatique; les capacités dépendent du produit.

**Perceptron —** classifieur à seuil fondé sur une combinaison affine des entrées; sa frontière de décision est linéaire.

**Propagation avant —** calcul successif des activations d’un réseau, des entrées vers la sortie.

## R–T

**Rétropropagation —** application de la règle de chaîne de la sortie vers les premières couches pour calculer les gradients des paramètres d’un réseau.

**ReLU (*rectified linear unit*) —** fonction d’activation \(\max(0,x)\).

**Taux d’apprentissage —** taille du pas utilisé par une règle d’optimisation pour modifier les paramètres à partir d’un gradient.

**Tenseur —** tableau numérique à un ou plusieurs axes; le nombre d’axes est distinct du rang d’une matrice au sens de l’algèbre linéaire.
