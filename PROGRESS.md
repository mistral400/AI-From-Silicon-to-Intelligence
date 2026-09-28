# État d’avancement

Dernière mise à jour : 2026-09-28

## Statut général

**Phase 0 — infrastructure : en cours.** Le dépôt distant a été inspecté : il contenait le commit initial avec un README minimal et une licence MIT. Le contenu de l’encyclopédie n’a pas encore commencé.

## Terminé

- Dépôt GitHub confirmé : `mistral400/AI-From-Silicon-to-Intelligence`, branche par défaut `main`.
- Droits de lecture et d’écriture confirmés par l’intégration GitHub.
- Architecture éditoriale initiale et conventions de contribution définies dans les fichiers de gouvernance.
- Prototype des builds Web et PDF ajouté à la CI.

## En cours / à valider

- Premier passage GitHub Actions : build MkDocs strict et build PDF.
- Vérifier les liens internes, l’affichage des caractères français et la génération du PDF.
- Confirmer que la table des matières couvre toutes les parties prévues dans le cahier des charges.

## Contenu rédigé

Aucun chapitre de fond terminé. Les pages présentes dans `book/` sont des pages d’accueil, une table des matières et un gabarit; elles ne comptent pas comme chapitres terminés.

## Références et figures

- Références : système de clés BibTeX établi; bibliographie de départ à enrichir et vérifier au moment de rédiger.
- Figures : politique d’identifiants et de traçabilité définie; aucune figure originale n’a encore été produite.

## Problèmes connus

- La licence MIT actuelle ne précise pas clairement le statut des textes et figures.
- La publication GitHub Pages et le format du livre PDF final ne sont pas encore configurés.
- La table des matières constitue une structure initiale; son découpage sera ajusté pendant la rédaction.

## Prochaine action exacte

1. Lire le résultat du workflow `CI` déclenché par le commit de fondation.
2. Corriger tout échec de build ou de rendu.
3. Mettre à jour ce fichier avec le SHA et les résultats vérifiés.
4. Une fois la CI verte, rédiger et sourcer le premier chapitre de fondation : « De l’électricité au bit : représentation et logique numérique ».
