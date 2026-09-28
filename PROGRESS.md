# État d’avancement

Dernière mise à jour : 2026-09-28

## Statut général

**Phase 0 — infrastructure : validée par GitHub Actions.** **Phase 1 — fondations : en cours.**

## Terminé

- Dépôt confirmé : `mistral400/AI-From-Silicon-to-Intelligence`, branche par défaut `main`.
- Architecture éditoriale, conventions de contribution, roadmap, suivi de progression, système de références et système de figures créés.
- Build Web MkDocs strict réussi.
- PDF en français généré avec Pandoc/XeLaTeX et téléversé comme artefact CI.
- Affichage des équations Web configuré avec Arithmatex et MathJax 3.2.2.
- Deux chapitres de fond rédigés, sourcés et intégrés à la navigation.
- Les builds du commit de contenu `405eddf` ont réussi dans le [workflow CI](https://github.com/mistral400/AI-From-Silicon-to-Intelligence/actions/runs/36489010150).

## Chapitres

| Chapitre | Statut | Dernière vérification |
|---|---|---|
| De l’électricité au bit : niveaux logiques et abstraction numérique | Premier jet; source primaire vérifiée; builds Web et PDF réussis | 2026-09-28 |
| Binaire, hexadécimal et nombres entiers | Premier jet; source primaire vérifiée; builds Web et PDF réussis | 2026-09-28 |

Les builds valident la compilation et les liens locaux, mais ne remplacent pas une relecture éditoriale indépendante.

## Références et figures

- BibTeX : notices MIT OpenCourseWare 6.004, printemps 2017; représentation numérique et niveaux logiques vérifiés sur les pages de cours.
- Attention Is All You Need conservé dans la bibliographie de départ pour la future partie Transformers.
- Aucune figure originale n’a encore été produite.

## Problèmes connus

- La licence MIT actuelle ne précise pas clairement le statut des textes et figures.
- Material for MkDocs annonce sa fin de maintenance le 5 novembre 2026; choisir un moteur/thème maintenu avant publication Web publique.
- Le format final du livre PDF et l’hébergement du site ne sont pas encore décidés.
- Le PDF actuel est un aperçu de l’accueil, du plan et des chapitres rédigés; il ne constitue pas encore le livre complet.

## Dernière étape terminée

Deux chapitres de fondation ajoutés à la table des matières et à la navigation, puis validés par les builds Web et PDF.

## Prochaine étape

Rédiger et sourcer « Transistors, portes logiques et circuits séquentiels », puis mettre à jour la table des matières et ce fichier.
