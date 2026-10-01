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
9. [Probabilités, entropie et information](part-01-foundations/probability-entropy-information.md)
10. [Optimisation, descente de gradient et régularisation](part-01-foundations/gradient-descent-optimization.md)
## Partie III — Réseaux neuronaux

11. [Perceptron, couches, activations et rétropropagation](part-02-neural-networks/perceptron-forward-backpropagation.md)
12. Généralisation, surapprentissage et évaluation
13. CNN, RNN et architectures antérieures aux Transformers

## Partie IV — Transformers et modèles de langage

14. Tokenisation et vocabulaire
15. Embeddings et représentation positionnelle
16. [Attention : requêtes, clés et valeurs (Q/K/V)](part-03-transformers/attention-qkv.md)
17. [Architecture Transformer, encodeur, décodeur et variantes](part-03-transformers/transformer-architecture.md)
18. Préentraînement causal et prédiction du prochain token
19. Contexte, fenêtres de contexte et limites
20. MoE (Mixture of Experts) et routage
21. Familles de modèles et évolution historique

## Partie V — Inférence et génération

22. Préremplissage (prefill) et décodage token par token
23. KV cache : calcul, mémoire et compromis
24. Sampling : température, top-k, top-p et pénalités
25. Reasoning, sorties structurées et limites observables
26. Latence, débit, batch et concurrence
27. Speculative decoding et autres optimisations

## Partie VI — Quantification et formats

28. Virgule flottante, précision et erreurs numériques
29. Quantification post-training et quantification pendant l’entraînement
30. INT8, INT4 et formats mixtes
31. GGUF : conteneur, métadonnées et tenseurs
32. Quantifications K-quants et IQ : interpréter les noms sans généraliser
33. Calculer poids, mémoire d’exécution et cache

## Partie VII — Modèles locaux et Apple Silicon

34. Exécuter des modèles localement : composants et contraintes
35. llama.cpp et Metal
36. MLX et MLX-LM
37. LM Studio et Ollama
38. Apple Silicon : CPU, GPU, Neural Engine et Unified Memory
39. Pression mémoire, swap, bande passante et mesures
40. Comparer Mac, PC avec GPU et serveurs

## Partie VIII — Entraînement et adaptation

41. Datasets, provenance, licences et contamination
42. Pipeline de données et nettoyage
43. Préentraînement : objectifs, lots et calcul
44. Fine-tuning supervisé et paramètres efficaces
45. Post-training, préférences, alignement et évaluation
46. Distillation et données synthétiques
47. Coûts et reproductibilité des expériences

## Partie IX — Infrastructure cloud et datacenters

48. GPU NVIDIA, AMD, TPU et accélérateurs alternatifs
49. Nœuds, interconnexions, réseaux et stockage
50. Entraînement distribué et parallélismes
51. Serving, ordonnanceurs, batching et moteurs d’inférence
52. Énergie, refroidissement, disponibilité et coûts
53. Mise à l’échelle et goulots d’étranglement

## Partie X — Systèmes augmentés et applications

54. Embeddings et recherche sémantique
55. RAG : indexation, récupération, génération et évaluation
56. Tool calling et interfaces avec les logiciels
57. Agents : boucle, mémoire, planification et contrôles
58. Multimodalité : texte, image, audio et vidéo
59. Génération d’images, diffusion et modèles génératifs

## Partie XI — Qualité, sécurité et société

60. Évaluation des modèles et conception de benchmarks
61. Hallucinations, incertitude et vérification
62. Sécurité, vie privée, risques et limites
63. Modèles ouverts, open-weight et propriétaires
64. Impacts économiques, énergétiques et sociaux

## Partie XII — Annexes de référence

- [Glossaire](glossary.md) et index (à créer)
- Chronologie des jalons et des familles de modèles
- Formats numériques et quantifications
- Paramètres d’inférence et unités
- Calculatrices de mémoire et de coûts
- Exemples reproductibles et fiches de mesure
- Bibliographie commentée
- Tableaux comparatifs datés
