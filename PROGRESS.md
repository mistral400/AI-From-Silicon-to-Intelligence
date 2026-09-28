# État d’avancement

Dernière mise à jour : 2026-09-28

## Statut général

**Phase 0 — infrastructure : validation visuelle du PDF en cours.** Le build Web strict et la génération PDF réussissent dans GitHub Actions. **Phase 1 — fondations : deux chapitres rédigés.**

## Terminé

- Dépôt confirmé : `mistral400/AI-From-Silicon-to-Intelligence`, branche par défaut `main`.
- Architecture éditoriale, conventions de contribution, roadmap, suivi de progression, système de références et système de figures créés.
- Build Web MkDocs strict réussi.
- Le PDF inclut les deux chapitres selon `book/book-order.txt` et est téléversé comme artefact CI.
- Équations en bloc rendues dans le PDF avec Pandoc et XeLaTeX.
- Affichage des équations Web configuré avec Arithmatex et MathJax 3.2.2.
- Deux chapitres de fond rédigés, sourcés et intégrés à la navigation.

## En cours / à valider

- Les formules mathématiques en ligne du chapitre binaire n’étaient pas délimitées correctement dans le Markdown et s’affichaient en texte brut dans le PDF.
- Les délimiteurs `\\(...\\)` sont corrigés dans le chapitre; vérifier le nouvel artefact et les indices, exposants, bases et nombres hexadécimaux.

## Chapitres

| Chapitre | Statut | Dernière vérification |
|---|---|---|
| De l’électricité au bit : niveaux logiques et abstraction numérique | Premier jet; source primaire vérifiée; build Web réussi; équations en bloc vérifiées en PDF | 2026-09-28 |
| Binaire, hexadécimal et nombres entiers | Premier jet; source primaire vérifiée; formules en ligne en correction et à revalider | 2026-09-28 |

Les builds valident la compilation et les liens locaux, mais ne remplacent pas une relecture éditoriale indépendante.

## Références et figures

- BibTeX : notices MIT OpenCourseWare 6.004, printemps 2017; représentation numérique et niveaux logiques vérifiés sur les pages de cours.
- Attention Is All You Need conservé dans la bibliographie de départ pour la future partie Transformers.
- Aucune figure originale n’a encore été produite.

## Problèmes connus

- Le manifeste PDF et l’affichage des mathématiques en ligne nécessitent une dernière vérification visuelle.
- La licence MIT actuelle ne précise pas clairement le statut des textes et figures.
- Material for MkDocs annonce sa fin de maintenance le 5 novembre 2026; choisir un moteur/thème maintenu avant publication Web publique.
- Le format final du livre PDF et l’hébergement du site ne sont pas encore décidés.

## Dernière étape terminée

Le PDF de six pages comprend les deux chapitres; les équations en bloc sont rendues.

## Prochaine étape

Valider visuellement les équations en ligne. Ensuite rédiger et sourcer « Transistors, portes logiques et circuits séquentiels ».
