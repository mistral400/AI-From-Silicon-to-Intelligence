# Prochaines tâches

Les tâches sont ordonnées selon leurs dépendances. Les statuts sont mis à jour dans le même commit que le travail correspondant.

## Phase 0 — Infrastructure

- [x] Vérifier le build Web strict dans GitHub Actions.
- [ ] Vérifier le rendu des équations en ligne et en bloc dans le PDF de CI. Le PDF local a été reconstruit et les équations des chapitres binaire, matériel, matriciel et mathématiques ont été inspectées; l’artefact CI reste à contrôler.
- [x] Inclure les chapitres rédigés dans le manifeste PDF.
- [x] Configurer l’affichage des équations sur le site Web.
- [x] Ajouter une vérification automatique des clés de citation, des métadonnées essentielles et des liens locaux, exécutée par la CI.
- [x] Compléter les métadonnées des références et vérifier les champs bibliographiques essentiels.
- [ ] Clarifier séparément les licences du contenu, du code et des figures.
- [ ] Avant GitHub Pages public, choisir un moteur/thème Web maintenu à long terme. Material for MkDocs annonce sa fin de maintenance le 5 novembre 2026.

## Phase 1 — Fondations

- [x] De l’électricité au bit : niveaux logiques et abstraction numérique.
- [x] Binaire, hexadécimal et nombres entiers.
- [x] Transistors, portes logiques et circuits séquentiels. Sources vérifiées; citations/liens et build Web validés; PDF local reconstruit et pages du chapitre inspectées. La vérification du PDF de CI reste suivie en phase 0.
- [ ] CPU, GPU, accélérateurs, mémoire et calcul matriciel. [Trois premiers jets ajoutés](book/part-01-foundations/cpu-gpu-accelerators.md) ([mémoire](book/part-01-foundations/memory-hierarchy.md), [calcul matriciel](book/part-01-foundations/matrix-computation.md)); validateur, build Web strict et PDF local réussis. Relecture des sources à faire depuis un environnement qui peut accéder aux références; artefact PDF CI à contrôler.
- [ ] Vecteurs, matrices, fonctions, dérivées et descente de gradient. [Trois premiers jets ajoutés](book/part-01-foundations/vectors-matrices-tensors.md) ([fonctions et dérivées](book/part-01-foundations/functions-derivatives-gradients.md), [optimisation](book/part-01-foundations/gradient-descent-optimization.md)); validateur, build Web strict et PDF local réussis. Relecture des sources à faire depuis un environnement qui peut accéder aux références; artefact PDF CI à contrôler.
- [ ] Probabilités, entropie et information. Premier jet ajouté dans [probability-entropy-information.md](book/part-01-foundations/probability-entropy-information.md); validateur, build Web strict et PDF local réussis. Relecture des sources et vérification de l’artefact PDF de CI restent à faire.
- [ ] Perceptrons, couches, activations et rétropropagation.
- [ ] Attention et architecture Transformer, avec calculs et figures originales.

## Règles de suivi

- Une tâche ne passe à terminée qu’après vérification des fichiers et du build concerné.
- Chaque tâche terminée cite ses sources dans le chapitre et met à jour [PROGRESS.md](PROGRESS.md).
- Les nouveaux sujets sont ajoutés à [book/table-of-contents.md](book/table-of-contents.md) avant leur rédaction.
