# Journal des changements

Les changements éditoriaux et techniques importants sont consignés ici. Les entrées de contenu citeront les chapitres concernés; les releases suivront le versionnement sémantique lorsqu’un premier livre publiable existera.

## 2026-10-01 — Réseaux neuronaux et mise en page du livre

- Ajout d’un chapitre de premier jet sur les perceptrons, les fonctions d’activation, la propagation avant et la rétropropagation, avec exemples numériques, exercices et corrigé.
- Ajout d’un schéma de réseau multicouche et d’un graphique d’activations générés par un script reproductible; création du glossaire initial.
- Réorganisation de la table des matières pour éviter de planifier séparément la théorie de l’information déjà couverte et les sous-sujets réunis dans le nouveau chapitre.
- Passage du PDF en A4, 11 pt, avec un sommaire d’une page, des liens colorés et la résolution des images partagées Web/PDF.
- Validateur de références/liens, quatorze tests, build Web strict, vérification des figures et build PDF de 49 pages réussis en local et dans le run CI `36875895430`. Son artefact a été parcouru; la revalidation des sources externes reste ouverte.

## 2026-10-01 — Attention Q/K/V et architecture Transformer

- Ajout de premiers jets sur l’attention à produit scalaire, les masques, les têtes multiples, l’encodeur-décodeur et le décodeur causal.
- Ajout de deux figures originales reproductibles, de calculs à la main, d’exercices et de termes au glossaire.
- Intégration Web/PDF, quatorze tests, validation des références/liens, vérification des quatre figures et build PDF local de 58 pages réussis. Le run CI `36878094080` a aussi réussi; son artefact de 58 pages a été parcouru en planches contact et inspecté en détail dans les chapitres ajoutés. Les pages de sources externes restent à vérifier.

## 2026-10-01 — Probabilités, entropie et information

- Ajout d’un premier jet sur les probabilités conditionnelles, Bayes, surprise, entropie, information mutuelle et entropie croisée.
- Ajout d’une référence à l’article de Shannon et intégration au parcours Web et PDF.
- Le validateur, le build Web strict et le PDF local réussissent; les pages d’équations ont été inspectées. La relecture des sources externes et le contrôle du PDF de CI restent ouverts.

## 2026-10-01 — Premiers jets matériel et mathématiques

- Ajout de chapitres sur CPU/GPU/accélérateurs, hiérarchie mémoire, calcul matriciel, vecteurs/matrices/tenseurs, dérivées et descente de gradient.
- Ajout des entrées bibliographiques correspondantes et intégration des six chapitres à la navigation et au manifeste PDF.
- Le validateur des références/liens, le build Web strict et la construction locale du PDF réussissent; les pages d’équations ont été inspectées.
- La relecture externe des nouvelles sources et la vérification de l’artefact PDF de CI restent ouvertes.

## 2026-09-28 — Chapitre de fondation 2

- Ajout des conversions binaire, décimale et hexadécimale, des entiers non signés et signés, du complément à deux et du débordement.
- Ajout d’exemples calculés et d’une référence au cours MIT OpenCourseWare 6.004, printemps 2017.

## 2026-09-28 — Chapitre de fondation 1

- Ajout de l’explication des niveaux logiques, zones indéterminées et marges au bruit.
- Ajout d’un exemple numérique explicitement fictif et d’une référence au cours MIT OpenCourseWare 6.004.
- Ajout du chapitre à la navigation et activation du rendu des équations Web.

## 2026-09-28 — Phase 0 : fondations

- Inspection du dépôt distant et création de la gouvernance, de la roadmap et du suivi de progression.
- Ajout de l’architecture de documentation, de conventions bibliographiques et de figures.
- Ajout de prototypes de build Web et PDF et de leur validation dans GitHub Actions.
