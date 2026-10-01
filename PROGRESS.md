# État d’avancement

Dernière mise à jour : 2026-10-01

## Statut général

**Phase 0 — infrastructure :** le validateur, les tests, le build Web strict, la génération des figures et le build PDF passent localement. Le PDF local de 49 pages a été inspecté en planches contact, puis les pages du nouveau chapitre avec ses équations, figures et tableaux ont été regardées en détail. Un run CI sur `main` est vert et son PDF a été inspecté, mais il précède le contenu récent de `work`; le run déclenché par pull request reste à terminer.

**Phase 1 — fondations :** onze chapitres sont rédigés en premier jet, du signal électrique à la rétropropagation. Un glossaire initial est ajouté. Les huit chapitres les plus récents ont encore besoin d’une vérification indépendante de leurs sources externes avant de pouvoir être considérés comme relus.

## Réalisé

- Dépôt confirmé : `mistral400/AI-From-Silicon-to-Intelligence`; branche de travail `work`, branche par défaut `main`.
- Onze chapitres de fond sont reliés à la navigation Web, au manifeste PDF et à la table des matières.
- Chapitre ajouté sur le perceptron, les activations, la propagation avant et la rétropropagation, avec exemples calculés, trois exercices et corrigé.
- Deux figures originales, un schéma de réseau multicouche et un graphique d’activations, sont générées par `scripts/generate_figures.py` avec Matplotlib 3.10.8.
- Glossaire initial relié à la navigation et inclus après les chapitres dans le PDF.
- Le PDF utilise maintenant A4, une police de 11 pt, un sommaire limité aux chapitres et des chemins de ressources qui incluent les images du livre.
- Validateur des citations et liens locaux réussi le 1er octobre 2026.
- Quatorze tests du validateur et des renvois PDF réussis le 1er octobre 2026.
- Build Web strict réussi avec MkDocs 1.6.1 et Material 9.7.7. Le build affiche l’avertissement du thème sur les changements annoncés pour MkDocs 2.0, mais termine sans erreur.
- Comparaison des figures régénérées réussie localement; le code et les PNG suivis sont cohérents dans cet environnement.
- PDF local réussi : 49 pages A4. La table des matières tient sur une page. La compilation n’a signalé ni ressource image manquante, ni boîte trop large, ni avertissement LaTeX. L’inspection du fichier confirme 92 destinations internes et 22 liens Web; aucun lien vers un fichier Markdown brut ne reste.
- Toutes les pages ont été parcourues en planches contact; les pages 40–49 ont été inspectées en plus haute résolution. Les deux figures, le tableau d’activations, les équations du réseau et de rétropropagation et le glossaire sont lisibles; aucun débordement visible n’a été relevé.
- Les calculs des deux exemples du nouveau chapitre ont été recalculés avec Python; l’étape de gradient diminue la perte de 0,18 à environ 0,109 pour le taux choisi de 0,01.

## CI et artefacts

- Run `36799442058` sur le commit `bbd6117` de `main` : neuf étapes terminées avec succès, y compris validations, tests, build Web, PDF et upload.
- Artefact CI de ce run téléchargé et inspecté : PDF de 11 pages, couvrant les chapitres présents sur `main` à ce commit. Il ne comprend pas les nouveaux chapitres de `work`.
- Une pull request depuis `work` doit déclencher le workflow sur le commit qui contient ce travail; son état, ses logs et son artefact restent à consulter.

## Sources, licences et thèmes

- Les URLs de sources ajoutées pour l’architecture, les mathématiques et les réseaux neuronaux n’ont pas été ouvertes pendant cette session. Une requête Web vers l’article Nature de Rumelhart a échoué avec un refus réseau HTTP 403; les métadonnées doivent être revalidées depuis un accès autorisé.
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

La validation actuelle garantit la structure et le rendu; elle ne remplace pas une relecture pédagogique et bibliographique.

## Problèmes connus et prochaine étape

- Le run CI correspondant à la branche `work` et l’inspection de son artefact sont en attente.
- Les nouvelles références externes restent à ouvrir et à contrôler une par une.
- Le glossaire ne couvre que les termes déjà présentés; aucun index conceptuel n’existe encore.
- Le statut des licences du texte et des figures reste à confirmer.
- Il faut encore rédiger les fondations des Transformers, puis les chapitres d’ingénierie des LLM, d’IA locale, d’entraînement, d’infrastructure et de systèmes modernes décrits dans `ROADMAP.md`.

**Prochaine étape immédiate :** pousser l’état validé sur `work`, ouvrir une pull request pour déclencher la CI, puis télécharger et inspecter le PDF de son artefact. Ensuite, revalider les sources externes et poursuivre avec l’attention et le Transformer.
