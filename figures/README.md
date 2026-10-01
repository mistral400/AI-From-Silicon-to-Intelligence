# Figures et diagrammes

## Identifiants

Nommer les figures `fig-<partie>-<sujet>-<numéro>`, par exemple `fig-05-attention-qkv-01.svg`. Les ressources Web/PDF communes résident dans `book/figures/`; conserver leur source éditable ou leur script dans `figures/` ou `scripts/`.

## Figures originales

- `book/figures/fig-03-mlp-01.png` et `book/figures/fig-03-activations-01.png` sont générées par `scripts/generate_figures.py` avec Matplotlib 3.10.8. Reproduction : `python scripts/generate_figures.py`. La CI vérifie que les images suivies correspondent au script avec `python scripts/generate_figures.py --check`.
- Ces figures sont des schémas et courbes mathématiques créés pour ce dépôt; elles n’utilisent pas de données ou d’illustrations tierces.

## Fiche de traçabilité

Pour chaque figure, documenter dans la page qui l’utilise : identifiant, légende, auteur, date, outil ou code source, données et hypothèses. Une figure adaptée d’une source externe doit indiquer la source et la licence; ne pas présumer qu’une illustration trouvée en ligne est réutilisable.

## Qualité

Chaque flèche et chaque unité doit être explicite. Les figures quantitatives doivent pouvoir être reproduites à partir des données ou du code fourni. Préférer SVG ou formats sources vectoriels aux images raster pour les schémas.
