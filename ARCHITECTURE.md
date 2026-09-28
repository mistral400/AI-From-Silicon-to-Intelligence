# Architecture du dépôt

## Source de vérité

Tous les fichiers nécessaires au projet résident dans GitHub. Le contenu canonique du livre est dans `book/`; les fichiers de suivi et de gouvernance résident à la racine.

```text
.
├── .github/workflows/ci.yml
├── appendices/
├── book/
│   ├── index.md
│   ├── table-of-contents.md
│   ├── chapter-template.md
│   ├── book-order.txt
│   └── part-XX-topic/
├── diagrams/
├── examples/
├── figures/
├── glossary/
├── notebooks/
├── references/references.bib
├── scripts/build_pdf.py
├── datasets/
├── mkdocs.yml
└── README.md, PROGRESS.md, ROADMAP.md, TODO.md, …
```

Les dossiers de contenu seront créés quand ils reçoivent des fichiers utiles; éviter les répertoires vides et les fichiers factices.

## Site Web

MkDocs Material lit `book/` et écrit le site statique dans `site/`. Les formules utilisent l’extension Arithmatex et MathJax 3.2.2, chargé depuis jsDelivr. Cette dépendance au CDN concerne l’affichage Web; le PDF est composé par XeLaTeX. En local, après installation des dépendances de développement : `mkdocs build --strict`. Dans le projet, cette commande s’exécute dans GitHub Actions. L’hébergement n’est pas encore activé.

## PDF

Le manifeste `book/book-order.txt` est la source de l’ordre des chapitres PDF; il contient un chemin Markdown par ligne. Le script `scripts/build_pdf.py` valide les entrées du manifeste, puis utilise Pandoc et XeLaTeX pour produire le PDF d’aperçu avec une table des matières réelle. Les nouveaux chapitres sont ajoutés au manifeste dans le même commit que leur création. Le script applique le français et résout les citations avec citeproc et `references/references.bib`. Le gabarit éditorial n’est pas inclus comme chapitre. Le runner installe Pandoc, XeLaTeX, Latin Modern, les polices PostScript Base 35 et les règles linguistiques françaises.

## CI et artefacts

Le workflow `.github/workflows/ci.yml` s’exécute sur les pushes vers `main` et les pull requests. Il construit le Web en mode strict, construit le PDF, puis conserve le PDF comme artefact téléchargeable. Seuls les artefacts de CI sont générés; aucun fichier de build n’est commité.

## Dépendances

Les dépendances Python sont épinglées dans `requirements-build.txt`. Mettre à jour les versions de manière explicite et vérifier le build complet. Les versions des actions GitHub sont indiquées dans le workflow et doivent être révisées périodiquement.

## Commandes

```sh
python -m pip install -r requirements-build.txt
mkdocs build --strict
python scripts/build_pdf.py --output pdf/preview.pdf
```

Ces commandes sont exécutées sur des runners cloud par la CI; leur présence sert aussi à rendre le build documenté et reproductible.
