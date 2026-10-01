# Contribuer

## Avant une modification

Lire [STYLE_GUIDE.md](STYLE_GUIDE.md), [SOURCES.md](SOURCES.md), [ARCHITECTURE.md](ARCHITECTURE.md) et [DECISIONS.md](DECISIONS.md). Vérifier [TODO.md](TODO.md) pour éviter de dupliquer du travail.

## Chapitres

Créer un fichier dans la partie appropriée, suivre [book/chapter-template.md](book/chapter-template.md), ajouter ses références à `references/references.bib` et mettre à jour la table des matières. Un chapitre terminé doit passer la relecture technique, la vérification des sources et les builds Web/PDF.

## Figures et code

Décrire les figures dans [figures/README.md](figures/README.md). Inclure le fichier source quand il est éditable. Les exemples doivent indiquer prérequis et versions; ne pas inclure de secrets, de données personnelles ni de grands fichiers générés.

## Validation

Avant de proposer une contribution :

```sh
python -m pip install -r requirements-build.txt
python scripts/validate_references.py
python -m unittest discover -s tests
mkdocs build --strict
python scripts/build_pdf.py --output pdf/preview.pdf
```

Les builds équivalents sont exécutés par GitHub Actions. Les modifications de licence doivent être documentées séparément dans une proposition explicite.
