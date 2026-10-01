# Table des matières détaillée

Cette structure initiale organise les sujets du cahier des charges par dépendances. Les pages seront scindées en fichiers au fur et à mesure de la rédaction; un titre du plan ne signifie pas que le chapitre existe déjà.

## Partie I — Des électrons aux ordinateurs

1. [De l’électricité au bit : niveaux logiques et abstraction numérique](part-01-foundations/electricity-to-bit.md)
2. [Binaire, hexadécimal et nombres entiers](part-01-foundations/binary-and-integer-encoding.md)
3. [Transistors, portes logiques et circuits séquentiels](part-01-foundations/transistors-logic-sequential.md)
4. [CPU, GPU, accélérateurs et calcul parallèle](part-01-foundations/cpu-gpu-accelerators.md)
5. [Mémoire, stockage, bande passante et latence](part-01-foundations/memory-hierarchy.md)
6. [Calcul matriciel et précision numérique](part-01-foundations/matrix-computation.md)

## Partie II — Mathématiques pour l’apprentissage automatique

7. [Vecteurs, matrices et tenseurs](part-01-foundations/vectors-matrices-tensors.md)
8. [Fonctions, dérivées, gradients et règle de chaîne](part-01-foundations/functions-derivatives-gradients.md)
9. Probabilités, distributions et entropie
10. [Optimisation, descente de gradient et régularisation](part-01-foundations/gradient-descent-optimization.md)
11. Théorie de l’information et pertes

## Partie III — Réseaux neuronaux

12. Perceptron et neurone artificiel
13. Couches, fonctions d’activation et propagation avant
14. Rétropropagation et entraînement
15. Généralisation, surapprentissage et évaluation
16. CNN, RNN et architectures antérieures aux Transformers

## Partie IV — Transformers et modèles de langage

17. Tokenisation et vocabulaire
18. Embeddings et représentation positionnelle
19. Attention : requêtes, clés et valeurs (Q/K/V)
20. Architecture Transformer, encodeur, décodeur et variantes
21. Préentraînement causal et prédiction du prochain token
22. Contexte, fenêtres de contexte et limites
23. MoE (Mixture of Experts) et routage
24. Familles de modèles et évolution historique

## Partie V — Inférence et génération

25. Préremplissage (prefill) et décodage token par token
26. KV cache : calcul, mémoire et compromis
27. Sampling : température, top-k, top-p et pénalités
28. Reasoning, sorties structurées et limites observables
29. Latence, débit, batch et concurrence
30. Speculative decoding et autres optimisations

## Partie VI — Quantification et formats

31. Virgule flottante, précision et erreurs numériques
32. Quantification post-training et quantification pendant l’entraînement
33. INT8, INT4 et formats mixtes
34. GGUF : conteneur, métadonnées et tenseurs
35. Quantifications K-quants et IQ : interpréter les noms sans généraliser
36. Calculer poids, mémoire d’exécution et cache

## Partie VII — Modèles locaux et Apple Silicon

37. Exécuter des modèles localement : composants et contraintes
38. llama.cpp et Metal
39. MLX et MLX-LM
40. LM Studio et Ollama
41. Apple Silicon : CPU, GPU, Neural Engine et Unified Memory
42. Pression mémoire, swap, bande passante et mesures
43. Comparer Mac, PC avec GPU et serveurs

## Partie VIII — Entraînement et adaptation

44. Datasets, provenance, licences et contamination
45. Pipeline de données et nettoyage
46. Préentraînement : objectifs, lots et calcul
47. Fine-tuning supervisé et paramètres efficaces
48. Post-training, préférences, alignement et évaluation
49. Distillation et données synthétiques
50. Coûts et reproductibilité des expériences

## Partie IX — Infrastructure cloud et datacenters

51. GPU NVIDIA, AMD, TPU et accélérateurs alternatifs
52. Nœuds, interconnexions, réseaux et stockage
53. Entraînement distribué et parallélismes
54. Serving, ordonnanceurs, batching et moteurs d’inférence
55. Énergie, refroidissement, disponibilité et coûts
56. Mise à l’échelle et goulots d’étranglement

## Partie X — Systèmes augmentés et applications

57. Embeddings et recherche sémantique
58. RAG : indexation, récupération, génération et évaluation
59. Tool calling et interfaces avec les logiciels
60. Agents : boucle, mémoire, planification et contrôles
61. Multimodalité : texte, image, audio et vidéo
62. Génération d’images, diffusion et modèles génératifs

## Partie XI — Qualité, sécurité et société

63. Évaluation des modèles et conception de benchmarks
64. Hallucinations, incertitude et vérification
65. Sécurité, vie privée, risques et limites
66. Modèles ouverts, open-weight et propriétaires
67. Impacts économiques, énergétiques et sociaux

## Partie XII — Annexes de référence

- Glossaire et index
- Chronologie des jalons et des familles de modèles
- Formats numériques et quantifications
- Paramètres d’inférence et unités
- Calculatrices de mémoire et de coûts
- Exemples reproductibles et fiches de mesure
- Bibliographie commentée
- Tableaux comparatifs datés
