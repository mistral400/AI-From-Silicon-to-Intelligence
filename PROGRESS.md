# État d’avancement

Dernière mise à jour : 2026-10-01

## Statut général

**Phase 0 — infrastructure :** le validateur, les tests, le build Web strict, la génération des figures et le build PDF passent localement. Le run CI `36875895430` sur `work` (commit `94c6dcd`) a terminé avec succès et a produit un PDF A4 de 49 pages. Toutes ses pages ont été parcourues en planches contact; le chapitre neuronal et le glossaire ont aussi été inspectés en détail. Le nouvel état Transformer passe les validations locales; il doit encore déclencher son propre run CI.

**Phase 1 — fondations :** treize chapitres sont rédigés en premier jet, du signal électrique à l’architecture Transformer. Un glossaire initial couvre maintenant quelques termes d’attention. Les dix chapitres les plus récents ont encore besoin d’une vérification indépendante de leurs sources externes avant de pouvoir être considérés comme relus.

## Réalisé

- Dépôt confirmé : `mistral400/AI-From-Silicon-to-Intelligence`; branche de travail `work`, branche par défaut `main`.
- Treize chapitres de fond sont reliés à la navigation Web, au manifeste PDF et à la table des matières.
- Chapitre ajouté sur le perceptron, les activations, la propagation avant et la rétropropagation, avec exemples calculés, trois exercices et corrigé.
- Quatre figures originales, sur les réseaux neuronaux et l’attention/architecture Transformer, sont générées par `scripts/generate_figures.py` avec Matplotlib 3.10.8.
- Glossaire initial relié à la navigation et inclus après les chapitres dans le PDF.
- Le PDF utilise maintenant A4, une police de 11 pt, un sommaire limité aux chapitres et des chemins de ressources qui incluent les images du livre.
- Validateur des citations et liens locaux réussi le 1er octobre 2026.
- Quatorze tests du validateur et des renvois PDF réussis le 1er octobre 2026.
- Build Web strict réussi avec MkDocs 1.6.1 et Material 9.7.7. Le build affiche l’avertissement du thème sur les changements annoncés pour MkDocs 2.0, mais termine sans erreur.
- Comparaison des figures régénérées réussie localement; le code et les PNG suivis sont cohérents dans cet environnement.
- PDF local réussi : 58 pages A4. La table des matières tient sur une page. La compilation n’a signalé ni ressource image manquante, ni boîte trop large, ni avertissement LaTeX. L’inspection confirme 101 destinations nommées et 24 liens Web; aucun lien vers un fichier Markdown brut ne reste.
- Toutes les pages du PDF local ont été parcourues en planches contact; les pages imprimées 46–56 ont été inspectées en plus haute résolution. Les quatre figures, les équations d’attention, le tableau de paramètres et le glossaire sont lisibles; aucun débordement visible n’a été relevé.
- Les calculs des deux exemples du nouveau chapitre ont été recalculés avec Python; l’étape de gradient diminue la perte de 0,18 à environ 0,109 pour le taux choisi de 0,01.
- Premiers jets ajoutés sur l’attention Q/K/V et l’architecture Transformer, avec un exemple causal calculé, un comptage illustratif de 172 paramètres, deux figures originales et des exercices. Le calcul d’attention donne des poids arrondis à `[0,33; 0,67; 0]` et une sortie `[0,33; 1,34]`.
- Glossaire étendu avec attention croisée, clés, requêtes, valeurs, masques causaux, encodage de position et Transformer.

## CI et artefacts

- Run `36799442058` sur le commit `bbd6117` de `main` : neuf étapes terminées avec succès, y compris validations, tests, build Web, PDF et upload.
- Artefact CI de ce run téléchargé et inspecté : PDF de 11 pages, couvrant les chapitres présents sur `main` à ce commit. Il ne comprend pas les nouveaux chapitres de `work`.
- Run `36875895430` sur le commit `94c6dcd` de `work` via la PR brouillon #1 : toutes les étapes ont réussi, dont vérification des figures, citations/liens, 14 tests, build Web strict, build PDF et upload.
- Artefact `ai-from-silicon-to-intelligence-pdf-preview` téléchargé : PDF A4 de 49 pages. Les planches contact couvrent l’ensemble du livre; les pages imprimées 43–47 du chapitre neuronal et du glossaire ont été inspectées en haute résolution. Pas de clipping visible; les images, tableaux, équations et liens sont lisibles.
- Les chapitres Transformer ont été ajoutés après ce run; le PDF local correspondant comporte 58 pages et a été inspecté. Le PDF CI du prochain commit reste à produire et inspecter.

## Sources, licences et thèmes

- Les URLs de sources ajoutées pour l’architecture, les mathématiques et les réseaux neuronaux n’ont pas été ouvertes pendant cette session. Les requêtes vers Nature, l’API arXiv et l’API Crossref ont toutes échoué au tunnel réseau avec HTTP 403; les sources et leurs métadonnées doivent être revalidées depuis un accès autorisé.
- Le nouveau contenu cite également Vaswani et al. (2017); ni l’article ni sa fiche arXiv n’ont pu être consultés depuis cet environnement.
- Le validateur confirme les clés BibTeX, les champs requis et les liens locaux; il ne vérifie ni l’existence des pages externes, ni le soutien d’une affirmation par sa source.
- Le dépôt conserve la licence MIT préexistante. La portée du texte et des figures reste à confirmer par le responsable du dépôt; aucune licence n’a été étendue ou remplacée.
- Material reste le thème de prototype. Le build local affiche un avertissement à propos de MkDocs 2.0; la date de fin de maintenance inscrite précédemment dans le dépôt n’a pas été confirmée sur le Web durant cette session. La stratégie de migration est documentée dans `DECISIONS.md`.

## Chapitres

| Chapitre | État actuel |
|---|---|
| De l’électricité au bit | Premier jet; source MIT déjà vérifiée dans une session antérieure; équations en bloc inspectées |
| Binaire, hexadécimal et entiers | Premier jet; source MIT déjà vérifiée dans une session antérieure; formules inspectées |
| Transistors, portes et circuits séquentiels | Premier jet; sources MIT déjà vérifiées dans une session antérieure; PDF local inspecté |
| CPU, GPU et accélérateurs | Premier jet; liens locaux et builds vérifiés; pages de sources externes à revalider |
| Mémoire, bande passante et latence | Premier jet; liens locaux et builds vérifiés; pages de sources externes à revalider |
| Calcul matriciel et précision numérique | Premier jet; équations et PDF local inspectés; sources à revalider |
| Vecteurs, matrices et tenseurs | Premier jet; liens locaux et builds vérifiés; sources à revalider |
| Fonctions, dérivées et gradients | Premier jet; équations inspectées; sources à revalider |
| Probabilités, entropie et information | Premier jet; équations inspectées; sources à revalider |
| Optimisation et descente de gradient | Premier jet; liens locaux et builds vérifiés; sources à revalider |
| Perceptron, propagation avant et rétropropagation | Premier jet; exemples numériques recalculés; références externes à vérifier |
| Attention : requêtes, clés et valeurs | Premier jet; exemple recalculé, figure et rendu PDF local inspectés; source externe et CI du nouvel état à vérifier |
| Architecture Transformer | Premier jet; comptage de paramètres vérifié, figure et rendu PDF local inspectés; source externe et CI du nouvel état à vérifier |

La validation actuelle garantit la structure et le rendu; elle ne remplace pas une relecture pédagogique et bibliographique.

## Problèmes connus et prochaine étape

- Les nouvelles références externes restent à ouvrir et à contrôler une par une.
- Le prochain run CI doit valider le contenu Transformer ajouté après le commit `94c6dcd`.
- Le glossaire ne couvre que les termes déjà présentés; aucun index conceptuel n’existe encore.
- Le statut des licences du texte et des figures reste à confirmer.
- Il faut encore rédiger les fondations des Transformers, puis les chapitres d’ingénierie des LLM, d’IA locale, d’entraînement, d’infrastructure et de systèmes modernes décrits dans `ROADMAP.md`.

**Prochaine étape immédiate :** pousser le contenu Transformer validé localement sur `work`, puis télécharger et inspecter l’artefact du prochain run CI. Ensuite, revalider les sources externes depuis un accès autorisé et poursuivre les sujets de fondation encore prévus.
