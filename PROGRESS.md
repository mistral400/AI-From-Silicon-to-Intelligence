# État d’avancement

Dernière mise à jour : 2026-09-30

## Statut général

**Phase 0 — infrastructure :** le validateur des citations et liens locaux est ajouté; ses contrôles et le build Web strict réussissent localement. La vérification visuelle du PDF reste ouverte. **Phase 1 — fondations :** deux chapitres précédents sont présents; le chapitre sur les transistors, la logique et les circuits séquentiels est en premier jet.

## Terminé

- Dépôt confirmé : mistral400/AI-From-Silicon-to-Intelligence, branche par défaut main.
- Architecture éditoriale, conventions de contribution, roadmap, suivi de progression, références et politique de figures créés.
- Build Web MkDocs strict réussi localement sur les changements courants.
- Validateur des citations, métadonnées bibliographiques essentielles et liens/ancres locaux ajouté au workflow CI.
- Huit tests unitaires passent : références valides, clé absente, doublon, métadonnées et URL invalides, liens/ancres cassés et exclusion des exemples de code.
- Notice BibTeX de Transformer complétée à partir des métadonnées officielles NeurIPS : auteurs, volume, pages, année, lieu et URL de l’éditeur.
- Les trois chapitres de fond figurent dans la table des matières, la navigation Web et le manifeste PDF.

## En cours / à valider

- Le code Markdown du chapitre binaire a été corrigé pour les formules en ligne. La dernière exécution GitHub Actions disponible a réussi sur le commit de base 866cfd1; son artefact PDF n’a pas pu être téléchargé sans authentification GitHub. Le rendu visuel des équations en ligne reste donc à vérifier.
- L’environnement local ne contient pas Pandoc ni XeLaTeX. Le PDF intégrant les nouveaux liens de citations et le troisième chapitre doit être reconstruit et inspecté en CI.
- Le chapitre « Transistors, portes logiques et circuits séquentiels » est en premier jet. Ses sources et ses ancres de citation sont validées; le build Web passe. La tâche TODO reste ouverte jusqu’à la vérification du PDF.
- Décider séparément des licences du contenu, du code et des figures.

## Chapitres

| Chapitre | Statut | Dernière vérification |
|---|---|---|
| De l’électricité au bit : niveaux logiques et abstraction numérique | Premier jet; source MIT vérifiée; build Web strict réussi; équations en bloc vérifiées dans l’ancien PDF CI | 2026-09-28 |
| Binaire, hexadécimal et nombres entiers | Premier jet; source MIT vérifiée; délimiteurs de maths en ligne corrigés; rendu PDF à vérifier | 2026-09-30 |
| Transistors, portes logiques et circuits séquentiels | Premier jet; sources MIT OCW vérifiées; citations/liens validés; build Web strict réussi; PDF à reconstruire et relire | 2026-09-30 |

La validation automatisée détecte les erreurs structurées, mais ne remplace pas une relecture éditoriale indépendante.

## Références et figures

- Références BibTeX MIT OpenCourseWare 6.004 : encodages et niveaux logiques, CMOS, logique combinatoire et logique séquentielle.
- *Attention Is All You Need* est conservé pour la future partie Transformers.
- Aucune figure originale n’a encore été produite; les chapitres actuels utilisent des tableaux et des calculs textuels.

## Problèmes connus

- Le PDF de la version de travail n’a pas été compilé localement; la CI doit le reconstruire. L’inspection visuelle de l’artefact précédent requiert un accès GitHub authentifié.
- La licence MIT actuelle ne précise pas le statut des textes et des figures. Les droits et le choix des licences restent à clarifier avant publication.
- Material for MkDocs annonce sa fin de maintenance le 5 novembre 2026; choisir un moteur/thème Web à long terme avant publication publique.
- L’hébergement public du site et le format final du livre PDF restent à décider.

## Dernière étape terminée

Le validateur de références/liens, ses huit tests unitaires et le build Web strict passent sur l’arbre de travail courant. L’artefact PDF correspondant reste à valider en CI.

## Prochaine étape

Faire exécuter le workflow CI sur ces changements, télécharger son PDF et vérifier le rendu mathématique et les liens de citations. Ensuite continuer vers le chapitre CPU, GPU, accélérateurs et mémoire.
