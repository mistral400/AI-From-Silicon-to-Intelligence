# État d’avancement

Dernière mise à jour : 2026-09-28

## Statut général

**Phase 0 — infrastructure : en cours de validation.** Le dépôt distant a été inspecté; il contenait le commit initial avec un README minimal et une licence MIT.

## Terminé

- Dépôt GitHub confirmé : `mistral400/AI-From-Silicon-to-Intelligence`, branche par défaut `main`.
- Droits de lecture et d’écriture confirmés par l’intégration GitHub.
- Architecture éditoriale initiale, conventions de contribution, références et suivi de progression créés.
- Build Web MkDocs exécuté avec succès en mode strict par GitHub Actions.
- Le lien local hors du dossier documentaire a été corrigé après le premier échec du build Web.

## En cours / à valider

- Build PDF Pandoc/XeLaTeX. Le premier essai manquait `lmodern.sty`; après ajout de `lmodern`, il manque encore la métrique de police `pzdr`.
- Le paquet `texlive-fonts-recommended` est ajouté au runner pour fournir les polices PostScript Base 35.
- Vérifier les caractères français, les liens du site et la disponibilité de l’artefact PDF.

## Contenu rédigé

Aucun chapitre de fond terminé. Les pages dans `book/` sont une page d’accueil, une table des matières et un gabarit; elles ne comptent pas comme chapitres terminés.

## Références et figures

- Références : système BibTeX et rendu des citations prévu dans le PDF; vérifier les notices au moment de leur emploi.
- Figures : identifiants et traçabilité définis; aucune figure originale n’a encore été produite.

## Problèmes connus

- La licence MIT actuelle ne précise pas clairement le statut des textes et figures.
- Material for MkDocs annonce sa fin de maintenance le 5 novembre 2026; choisir un moteur/thème maintenu avant publication Web publique.
- Le format final du livre PDF et l’hébergement du site ne sont pas encore décidés.

## Prochaine action exacte

1. Vérifier la CI du commit de correction PDF.
2. Si Web et PDF sont verts, noter le résultat et l’artefact dans ce fichier.
3. Rédiger et sourcer « De l’électricité au bit : représentation et logique numérique » dans la partie I.
