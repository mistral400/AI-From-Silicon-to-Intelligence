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

## 2026-10-01 — Thème Web et stratégie de migration

- Conserver MkDocs Material pour le prototype éditorial : le build strict actuel fonctionne et la source Markdown n’est pas liée au thème.
- Ne pas migrer pendant que les fondations et l’architecture restent en mouvement. Avant un hébergement public, comparer des options maintenues sur le rendu des maths et figures, la navigation, la recherche, l’accessibilité et GitHub Pages, puis tester la migration sur une branche.
- Le dépôt note une échéance de maintenance de Material au 5 novembre 2026 et le build local affiche aussi un avertissement de compatibilité pour MkDocs 2.0. Les pages externes n’étant pas accessibles pendant cette session, ces annonces devront être revalidées avant de choisir un remplaçant.

## 2026-10-01 — Périmètre des licences

- Laisser intact le fichier `LICENSE` MIT existant; ne pas supposer qu’il règle à lui seul les droits des nouveaux chapitres et illustrations.
- Garder le code des scripts sous la licence actuelle du dépôt tant que son périmètre est confirmé. Pour le livre et les figures originales, proposer une licence de contenu distincte, par exemple CC BY 4.0, avec attribution claire.
- Avant publication ou acceptation de contributions, le responsable du dépôt doit confirmer la portée du droit d’auteur et le choix de licence pour les textes et figures. Les figures tierces restent exclues tant que leur licence n’est pas vérifiée.

## À revoir

- Réévaluer le thème Web avant publication et revalider l’annonce de maintenance de Material.
- Hébergement public du site et workflow de déploiement.
- Licence du contenu et politique d’acceptation des contributions.
- Format final du PDF et stratégie d’indexation.
