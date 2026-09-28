# AI From Silicon to Intelligence

**Une encyclopédie technique de l’intelligence artificielle moderne, des transistors aux systèmes qui l’utilisent.**

Le projet explique comment l’IA moderne est conçue, entraînée, exécutée et déployée. Il relie les bases matérielles et mathématiques aux Transformers, aux modèles locaux et cloud, à leurs outils et à leurs limites. Le contenu principal est en français; les termes anglais usuels sont conservés et définis à leur première occurrence.

## État du projet

Le projet est en phase de fondation. L’infrastructure de départ est validée par GitHub Actions : les builds Web strict et PDF passent, et le PDF d’aperçu est conservé comme artefact CI. Deux chapitres des fondations sont rédigés en premier jet.

- Avancement détaillé : [PROGRESS.md](PROGRESS.md)
- Prochaines tâches : [TODO.md](TODO.md)
- Table des matières : [book/table-of-contents.md](book/table-of-contents.md)
- Roadmap : [ROADMAP.md](ROADMAP.md)
- Guide de contribution : [CONTRIBUTING.md](CONTRIBUTING.md)

## Lire et construire

La version Web est générée avec MkDocs Material à partir des fichiers Markdown dans `book/`. Le PDF est assemblé avec Pandoc et XeLaTeX à partir des mêmes sources.

Les deux builds tournent dans GitHub Actions; aucun ordinateur personnel n’est requis. Le PDF produit par la CI est un artefact de validation, pas encore une édition complète du livre.

## Principes

- Expliquer les concepts à plusieurs niveaux, avec intuition, détails techniques et exemples.
- Séparer faits vérifiés, estimations, mesures et hypothèses.
- Dater les informations qui dépendent d’une version de logiciel ou de modèle.
- Privilégier les diagrammes originaux et citer les sources.
- Ajouter du contenu seulement lorsqu’il apporte une explication, une preuve ou un outil utile.

## Licence

Le dépôt contient une licence MIT préexistante. La portée de cette licence sur le texte et les figures doit être clarifiée avant la première publication substantielle. La décision de licence est suivie dans [DECISIONS.md](DECISIONS.md).
