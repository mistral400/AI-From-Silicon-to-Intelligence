# Décisions du projet

Les décisions ci-dessous préservent la continuité entre les sessions. Les changements structurants doivent inclure leur date, leur raison et leurs conséquences.

## 2026-09-28 — Dépôt et langue

- Le dépôt GitHub est la source de vérité durable.
- Le contenu principal est en français; les termes techniques anglais usuels sont maintenus et définis à leur première occurrence.
- Les chapitres sont des fichiers Markdown séparés et organisés par partie.

## 2026-09-28 — Source et builds

- Les fichiers éditoriaux canoniques résident dans `book/`.
- MkDocs Material est utilisé uniquement comme prototype de site; le contenu Markdown reste indépendant du thème.
- Pandoc et XeLaTeX assemblent le PDF à partir des mêmes sources Markdown. Le PDF de CI est un aperçu de validation; le format de publication reste à décider.
- La CI vérifie les builds sur GitHub-hosted runners. Aucun ordinateur personnel n’est nécessaire.

## 2026-09-28 — Références et figures

- Les références bibliographiques utilisent des clés BibTeX stables; les chapitres citent ces clés, pas des numéros manuels.
- Les figures du projet reçoivent un identifiant stable et un fichier source éditable lorsque possible.
- Les visuels externes nécessitent une attribution et une vérification de licence avant inclusion.

## 2026-09-28 — Licences (à confirmer)

- Le dépôt initial contient une licence MIT. Elle demeure inchangée pendant la phase d’infrastructure.
- Avant publication substantielle, clarifier séparément les licences du code, du texte et des figures; vérifier le droit de l’auteur avant d’étendre ou de remplacer la licence existante.
- Aucun contenu tiers substantiel ne sera copié dans le projet pendant cette période.

## À revoir

- Choix d’un générateur/thème Web maintenu à long terme avant publication; Material for MkDocs annonce la fin de sa maintenance le 2026-11-05.
- Hébergement public du site et workflow de déploiement.
- Licence du contenu et politique d’acceptation des contributions.
- Format final du PDF et stratégie d’indexation.
