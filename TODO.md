# Prochaines tâches

Les tâches sont ordonnées selon leurs dépendances. Les statuts sont mis à jour dans le même commit que le travail correspondant.

## Phase 0 — Infrastructure

- [x] Vérifier le build Web strict dans GitHub Actions.
- [x] Vérifier le rendu des équations en ligne et en bloc dans le PDF de CI. L’artefact du run `36875895430` (commit `94c6dcd`) a été téléchargé; ses 49 pages ont été parcourues et les pages du nouveau chapitre inspectées en détail.
- [x] Inclure les chapitres rédigés dans le manifeste PDF.
- [x] Configurer l’affichage des équations sur le site Web.
- [x] Ajouter une vérification automatique des clés de citation, des métadonnées essentielles et des liens locaux, exécutée par la CI.
- [x] Compléter les métadonnées des références et vérifier les champs bibliographiques essentiels.
- [x] Vérifier dans la CI que les figures générées sont reproductibles et inspecter le PDF construit depuis l’état poussé sur `work` : vérification des figures et build PDF réussis au run `36875895430`.
- [ ] Clarifier séparément les licences du contenu, du code et des figures.
- [ ] Avant GitHub Pages public, choisir un moteur/thème Web maintenu à long terme. L’échéance du 5 novembre 2026 notée dans le dépôt pour Material reste à revalider sur la page de l’éditeur.

## Phase 1 — Fondations

- [x] De l’électricité au bit : niveaux logiques et abstraction numérique.
- [x] Binaire, hexadécimal et nombres entiers.
- [x] Transistors, portes logiques et circuits séquentiels. Sources vérifiées; citations/liens et build Web validés; PDF local reconstruit et pages du chapitre inspectées. Le PDF correspondant de la CI a aussi été parcouru.
- [ ] CPU, GPU, accélérateurs, mémoire et calcul matriciel. [Trois premiers jets ajoutés](book/part-01-foundations/cpu-gpu-accelerators.md) ([mémoire](book/part-01-foundations/memory-hierarchy.md), [calcul matriciel](book/part-01-foundations/matrix-computation.md)); validateur, build Web strict, PDF local et PDF CI réussis. Relecture des sources à faire depuis un environnement qui peut accéder aux références.
- [ ] Vecteurs, matrices, fonctions, dérivées et descente de gradient. [Trois premiers jets ajoutés](book/part-01-foundations/vectors-matrices-tensors.md) ([fonctions et dérivées](book/part-01-foundations/functions-derivatives-gradients.md), [optimisation](book/part-01-foundations/gradient-descent-optimization.md)); validateur, build Web strict, PDF local et PDF CI réussis. Relecture des sources à faire depuis un environnement qui peut accéder aux références.
- [ ] Probabilités, entropie et information. Premier jet ajouté dans [probability-entropy-information.md](book/part-01-foundations/probability-entropy-information.md); validateur, build Web strict, PDF local et PDF CI réussis. Relecture des sources à faire.
- [ ] Réseaux neuronaux : [perceptron, couches, activations, propagation avant et rétropropagation](book/part-02-neural-networks/perceptron-forward-backpropagation.md). Premier jet ajouté; exemples recalculés; rendu PDF local et CI inspecté. Sources externes à vérifier avant de clore.
- [ ] Attention et architecture Transformer : premiers jets ajoutés pour [Q/K/V](book/part-03-transformers/attention-qkv.md) et [l’architecture](book/part-03-transformers/transformer-architecture.md), avec calculs, exercices et deux figures originales. Validateur, figures, build Web strict, tests et PDF local de 58 pages réussis; le PDF CI du nouvel état et les sources externes restent à contrôler.

## Règles de suivi

- Une tâche ne passe à terminée qu’après vérification des fichiers et du build concerné.
- Chaque tâche terminée cite ses sources dans le chapitre et met à jour [PROGRESS.md](PROGRESS.md).
- Les nouveaux sujets sont ajoutés à [book/table-of-contents.md](book/table-of-contents.md) avant leur rédaction.

## Annexes pour la publication

- [ ] Étendre le [glossaire](book/glossary.md) au fil des chapitres et créer un index conceptuel navigable. Les termes attention, clé, requête, valeur, masque causal et Transformer sont ajoutés.
- [ ] Ajouter des exercices et corrigés aux chapitres relus; vérifier chaque solution numériquement lorsqu’elle implique un calcul.
