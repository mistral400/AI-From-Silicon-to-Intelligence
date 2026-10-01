# État d’avancement

Dernière mise à jour : 2026-10-01

## Statut général

**Phase 0 — infrastructure :** le validateur de références/liens et le build Web strict passent localement. Le PDF complet de 26 pages a été compilé avec Pandoc et XeLaTeX; les équations de plusieurs chapitres ont été inspectées visuellement. Il reste à vérifier l’artefact PDF de CI. **Phase 1 — fondations :** trois chapitres initiaux sont présents; six nouveaux chapitres sont intégrés en premiers jets. Les sources de ces six nouveaux chapitres sont à revalider, car cet environnement ne permet pas d’accéder à leurs sites.

## Terminé

- Dépôt confirmé : mistral400/AI-From-Silicon-to-Intelligence, branche par défaut main.
- Architecture éditoriale, conventions de contribution, roadmap, suivi de progression, références et politique de figures créés.
- Six chapitres ajoutés sur les processeurs, la mémoire, le calcul matriciel, les vecteurs et tenseurs, les dérivées et la descente de gradient.
- Les neuf chapitres de fond figurent dans le manifeste PDF; les six nouveaux sont intégrés à la navigation Web et à la table des matières.
- Validateur des citations, métadonnées bibliographiques et liens locaux réussi le 1er octobre 2026.
- Build Web strict réussi avec MkDocs 1.6.1 et Material 9.7.7, conformément à requirements-build.txt.
- Build PDF local réussi sans avertissement de références dupliquées; le script préfixe uniquement les ancres de références dans ses copies temporaires, sans modifier les sources Markdown.
- Inspection visuelle d’équations en ligne et en bloc : chapitres sur l’électricité, le binaire, les transistors, le calcul matriciel, les dérivées et les gradients.

## En cours / à valider

- Vérifier dans GitHub Actions l’artefact PDF et confirmer le rendu dans l’environnement CI. Les pages locales examinées sont lisibles.
- Ouvrir et vérifier les sources externes nouvellement ajoutées pour CPU/GPU/accélérateurs, mémoire, calcul matriciel, algèbre linéaire et optimisation. La politique réseau de l’environnement de rédaction autorise ici les hôtes de paquets, mais pas les sites de documentation ou d’éditeurs utilisés dans ces références; les entrées ne prétendent donc pas avoir été consultées le 1er octobre.
- Décider séparément des licences du contenu, du code et des figures.

## Chapitres

| Chapitre | Statut | Dernière vérification |
|---|---|---|
| De l’électricité au bit : niveaux logiques et abstraction numérique | Premier jet; source MIT vérifiée; build Web strict réussi; équations en bloc inspectées | 2026-10-01 |
| Binaire, hexadécimal et nombres entiers | Premier jet; source MIT vérifiée; build Web strict réussi; équations en ligne et en bloc inspectées | 2026-10-01 |
| Transistors, portes logiques et circuits séquentiels | Premier jet; sources MIT OCW vérifiées; citations/liens et builds Web/PDF validés; pages du chapitre inspectées | 2026-10-01 |
| CPU, GPU et accélérateurs | Premier jet; citations/liens et builds Web/PDF validés; sources à revalider | 2026-10-01 |
| Mémoire, bande passante et latence | Premier jet; citations/liens et builds Web/PDF validés; sources à revalider | 2026-10-01 |
| Calcul matriciel et précision numérique | Premier jet; citations/liens et builds Web/PDF validés; équations inspectées; sources à revalider | 2026-10-01 |
| Vecteurs, matrices et tenseurs | Premier jet; citations/liens et builds Web/PDF validés; sources à revalider | 2026-10-01 |
| Fonctions, dérivées, gradients et règle de chaîne | Premier jet; citations/liens et builds Web/PDF validés; équations inspectées; sources à revalider | 2026-10-01 |
| Optimisation et descente de gradient | Premier jet; citations/liens et builds Web/PDF validés; sources à revalider | 2026-10-01 |

La validation automatisée détecte les erreurs structurées et les liens locaux; elle ne confirme pas qu’une source externe appuie chaque affirmation. La relecture éditoriale reste nécessaire.

## Références et figures

- Références MIT OpenCourseWare 6.004 conservées pour les chapitres sur les bits, le CMOS, la logique combinatoire et les circuits séquentiels.
- Nouvelles entrées ajoutées pour l’architecture des processeurs, CUDA, le TPU, la hiérarchie mémoire, le modèle Roofline, l’algèbre linéaire et l’optimisation.
- *Attention Is All You Need* est conservé pour la future partie Transformers.
- Aucune figure originale n’a encore été produite; les chapitres actuels utilisent des tableaux et des calculs textuels.

## Problèmes connus

- L’artefact PDF de CI n’a pas été téléchargé ni inspecté. La compilation locale passe, mais elle ne remplace pas cette vérification demandée.
- Les nouvelles références externes ne sont pas encore réouvertes dans un environnement donnant accès aux pages d’éditeurs et de documentation.
- La licence MIT actuelle ne précise pas le statut des textes et des figures. Les droits et le choix des licences restent à clarifier avant publication.
- Material for MkDocs annonce sa fin de maintenance le 5 novembre 2026; choisir un moteur/thème Web à long terme avant publication publique.
- L’hébergement public du site et le format final du livre PDF restent à décider.

## Dernière étape terminée

Les neuf chapitres ont été validés par le validateur de références/liens et le build Web strict; le PDF local a été compilé et les équations représentatives inspectées. Les résultats de validation externe et l’artefact PDF de CI restent ouverts.

## Prochaine étape

Revalider les sources des six nouveaux chapitres depuis un accès Web autorisé, puis contrôler l’artefact PDF produit par GitHub Actions.
