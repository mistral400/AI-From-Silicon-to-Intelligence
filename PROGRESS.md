# État d’avancement

Dernière mise à jour : 2026-09-28

## Statut général

**Phase 0 — infrastructure : validée par CI.** **Phase 1 — fondations : commencée.**

## Terminé

- Dépôt confirmé : `mistral400/AI-From-Silicon-to-Intelligence`, branche par défaut `main`.
- Architecture éditoriale, conventions de contribution, roadmap, suivi de progression, système de références et système de figures créés.
- Build Web MkDocs strict réussi dans GitHub Actions.
- Build du PDF Pandoc/XeLaTeX réussi dans GitHub Actions après ajout des paquets LaTeX requis.
- PDF d’aperçu téléversé comme artefact du workflow CI.
- Premier chapitre de fond rédigé et sourcé : « De l’électricité au bit : niveaux logiques et abstraction numérique ».

## Chapitres

| Chapitre | Statut | Dernière vérification |
|---|---|---|
| De l’électricité au bit : niveaux logiques et abstraction numérique | Premier jet, source primaire vérifiée; attente du build de contenu | 2026-09-28 |

Aucun autre chapitre n’est rédigé.

## Références et figures

- BibTeX : entrée ajoutée pour le cours MIT OpenCourseWare 6.004, printemps 2017; informations vérifiées sur la page source le 2026-09-28.
- Attention Is All You Need conservé dans la bibliographie de départ pour la future partie Transformers.
- Aucune figure originale n’a encore été produite.

## Problèmes connus

- La licence MIT actuelle ne précise pas clairement le statut des textes et figures.
- Material for MkDocs annonce sa fin de maintenance le 5 novembre 2026; choisir un moteur/thème maintenu avant publication Web publique.
- Le format final du livre PDF et l’hébergement du site ne sont pas encore décidés.

## Dernière étape terminée

Infrastructure de builds Web et PDF validée dans GitHub Actions.

## Prochaine étape

1. Vérifier que le nouveau chapitre apparaît dans la navigation Web et le PDF.
2. Mettre à jour son statut selon le résultat du build.
3. Ajouter le chapitre suivant : « Binaire, hexadécimal et représentation des nombres ».
