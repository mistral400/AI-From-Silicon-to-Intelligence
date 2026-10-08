# Inventaire provisoire des concepts

> **Version :** 0.1 — inventaire de repérage, pas fiches techniques finales.  
> **Date :** 2026-10-08.

Les noms et regroupements proviennent du résumé de mémoire fourni à cette session et de la demande actuelle. Les noms listés dans la demande ne prouvent pas à eux seuls que toutes les variantes ont été effectivement discutées auparavant. Toute entrée issue uniquement de cette liste est donc à confirmer à partir des archives.

## ORB — Orbit, orchestration de projets IA

- **ORB-001 — Orbit** : concept d’orchestrateur de projets complexes et de longue durée. L’utilisateur précise qu’il s’agit d’une idée qu’il pourrait offrir gratuitement à OpenAI; aucune transmission ni adoption n’est établie.
- **ORB-002 — Nexus** : composant de dialogue initial, collecte des besoins, clarification et planification avec l’utilisateur.
- **ORB-003 — Prism** : découpage en tâches, dépendances, exécution parallèle, sélection dynamique des modèles et coordination.
- **ORB-004 — Aion** : continuité d’exécution sur de longues périodes, checkpoints, reprises et suivi.
- **ORB-005 — Orbit Core** : mémoire persistante, orchestration, permissions, journalisation, communication et optimisation des ressources.
- **ORB-006 — Nexy, Prismo, Aio** : mascottes évoquées dans la demande; spécifications visuelles et interactionnelles à retrouver.
- **À documenter :** interface, rôles exacts, autorisations, stratégie de sélection de modèles, limites et états d’exécution.

## LIIX-APP — Liix, application et écosystème logiciel

- **LIIX-APP-001 — Liix (versions précoces)** : versions SwiftUI mentionnées dans la demande; dépôts et captures à retrouver.
- **LIIX-APP-002 — Liix avec LM Studio** : intégration locale rapportée; versions, protocole et contraintes à documenter.
- **LIIX-APP-003 — Liix avec LiteLLM / passerelles API** : piste listée pour l’historique; état réel non confirmé.
- **LIIX-APP-004 — Liix Desktop Electron/React** : dépôt Liix privé ou local mentionné dans la mémoire, distinct du dépôt de ce livre.
- **LIIX-APP-005 — Liix Web et Desktop partagés** : objectif de réutilisation de composants et d’un cœur React commun, code Electron natif conservé dans Desktop.
- **LIIX-APP-006 — Mémoire de session Markdown** : organisation mémorielle et continuité de session.
- **LIIX-APP-007 — Gestion du contexte** : inspecteur, budget, compression et télémétrie décrits comme objectifs du produit.
- **LIIX-APP-008 — Providers et identifiants** : fournisseurs locaux/cloud, profils, secrets via safeStorage, redaction, santé des providers.
- **LIIX-APP-009 — Agents, plans et tâches** : exécution d’outils ou tâches, à distinguer selon versions implémentées et souhaitées.
- **LIIX-APP-010 — Liix MVP / Provider UI** : contexte rapporte commits `0e209b2` et `996f7d0`, et tests (40 puis 87). Les commits et suites doivent être vérifiés dans le dépôt source.
- **Problèmes rapportés :** installation Electron échouée sur macOS en octobre 2026; Vite démarrait malgré l’échec Electron.

## LIIX-MOD — Modèles Liix et architectures d’agents

Les gammes suivantes sont à traiter comme noms historiques à confirmer, sans présumer d’un modèle entraîné :

- **LIIX-MOD-001 — Gamme de taille** : Nano, Mini, Standard, Pro, Alpha Pro.
- **LIIX-MOD-002 — Gamme générale** : Core, Flash Lite, Flash, Flash+, Ultra.
- **LIIX-MOD-003 — Spécialisations** : Code, Dev, Math, STEM, Vision.
- **LIIX-MOD-004 — Autres spécialisations** : Plan, Apple, Finance, Stats, Literature, Opti, OS, TA.
- **LIIX-MOD-005 — Agents nommés** : Voice, Imagine, Research, Analyst, Browser, Operator, Critic, Scholar, Tutor.
- **LIIX-MOD-006 — MoE/MoM/MoMA** : architectures proposées; définitions, tailles et routage à récupérer.
- **LIIX-MOD-007 — R⁵ et apprentissage autonome** : nom et détails à retrouver.
- **LIIX-MOD-008 — Neural Context Cache** : notion évoquée; fonctionnement et différence avec cache KV inconnus.
- **LIIX-MOD-009 — offres / budgets** : abonnements, multiplicateurs et budgets de tokens listés dans la demande, paramètres source manquants.
- **Règle :** spécifications imaginées, simulations et modèles véritablement entraînés seront séparés explicitement.

## LOG — Logiix et technologies associées

- **LOG-001 — Logiix** : écosystème technologique hypothétique, organisation et divisions à reconstruire.
- **LOG-002 — Universe Engine**.
- **LOG-003 — Universe OS**.
- **LOG-004 — Universe Cloud**.
- **LOG-005 — Nova SSD**.
- **LOG-006 — ExaFusion**.
- **LOG-007 — Logiix Design**.
- **LOG-008 — Logiix/Thales AI Compute Grid** : scénario/partenariat hypothétique selon la demande; ne pas décrire comme contrat existant.
- **LOG-009 — Logiix LOV1** : socket évoqué avec 2 950 broches dans la demande; chiffre historique à retrouver, faisabilité non examinée.
- **LOG-010 — Logiix Context Fabric / Deep Context** : interconnexion ou architecture mémoire à documenter.
- **LOG-011 — L-Link / PhotonLink** : liens d’interconnexion à retrouver.

## CPU — Processeurs et architecture ALIX

- **CPU-001 — Vortex CPU** : famille hypothétique; générations et caractéristiques inconnues ici.
- **CPU-002 — Neura**.
- **CPU-003 — Fusion**.
- **CPU-004 — Aero, Quantum, Thread, Ultra, Titan**.
- **CPU-005 — L-Titan, L-Pioneer, L-Eco, L-Feather, NE Cores**.
- **CPU-006 — familles Vortex V3/V5/V7/V9**.
- **CPU-007 — ALIX** : architecture universelle proposée comme alternative à ARM et x86.
- **CPU-008 — intégration CPU/GPU/NPU**.
- **À retrouver :** ISA, unités d’exécution, mémoire, caches, sockets, chiffres et calculs; ne pas inférer leur existence ni leur compatibilité.

## GPU — Vortex, Vecna, Luuna et Neura

- **GPU-001 — Vortex G1/G2 et G1-110 à G1-195**.
- **GPU-002 — Vortex Vecna**.
- **GPU-003 — Vortex Luuna / Luuna 4.0**.
- **GPU-004 — Neura GPU**.
- **GPU-005 — X3D2 / V-190X3D2 TRINITY**.
- **GPU-006 — Logiix LMX-8 et mini-GPU expérimentaux**.
- **GPU-007 — unités spécialisées** : LVX-C, LTX-C, LRX-C, LMX-C, LNX-C, LEX-C.
- **GPU-008 — groupes VVC, VIC, VMC, VRC, VGC, VPC, VCC, VSC, VCTRL, VDC, Deep Core**.
- **GPU-009 — techniques graphiques** : Neural Super Rendering, Ultra Low Latency Engine, Adaptive Frame Dynamics, reconstruction neuronale, compression de textures, frame/geometry generation et path tracing.
- **GPU-010 — simulateurs GPU Python** : existence rapportée dans la demande; scripts et sorties à retrouver.
- **Statut commun :** les spécifications doivent être marquées hypothétiques jusqu’à vérification par mesure ou prototype.

## NPU — Accélérateurs LNX

- **NPU-001 — LNX1**.
- **NPU-002 — LNX2**.
- **NPU-003 — LNX3** : présence éventuelle à confirmer.
- **NPU-004 — LNX-CPL1 Socrate**.
- **NPU-005 — LNX-H1**.
- **NPU-006 — LNX Forge / Forge Pro**.
- **NPU-007 — Socrate Station**.
- **NPU-008 — LNX-C60 / C75 / C100**.
- **NPU-009 — LNX-Link**.
- **NPU-010 — architectures d’inférence, d’entraînement et MoE distribuées**.
- **À retrouver :** Intel 18A, nombre de transistors, SRAM, HBM/LPDDR, formats numériques, FLOPS, puissance, bande passante, budgets de calcul et hypothèses de rendement.

## HOLO — HoloDenoise et imagerie microfluidique

- **HOLO-001 — débruitage d’hologrammes** : besoin évoqué pour des images d’holographie et des données de microfluidique, potentiellement avec mesures d’impédance.
- **HOLO-002 — HoloDenoise Core v1** : architecture référencée dans le contexte; contenu du fichier source non disponible dans cette session.
- **HOLO-003 — cible FPGA XC7A35T**.
- **HOLO-004 — pipeline 640×480, 10 bits, 25/30 images/s, cible d’horloge 100 MHz**.
- **HOLO-005 — architecture streaming, buffers de lignes, CNN résiduel, INT8/INT32, préservation des franges** : éléments de la demande actuelle, à confirmer dans le document d’architecture.
- **HOLO-006 — cible <0,25 W** : exigence de très basse puissance rapportée; non démontrée sur FPGA.
- **État :** exigences et idées architecturales; contraintes et mesure de puissance non vérifiées ici.

## DC — Infrastructures de calcul

- **DC-001 — Logiix/Thales AI Compute Grid**.
- **DC-002 — LNX2 en datacenter**.
- **DC-003 — GigaCluster 1**.
- **DC-004 — entraînement/inférence distribués et réseaux de clusters**.
- **DC-005 — scénarios de datacenters québécois / Apple Intelligence**.
- **DC-006 — flexibilité énergétique et surplus électrique**.
- **DC-007 — refroidissement liquide en boucle fermée, récupération et distribution de chaleur**.
- **DC-008 — microcentres de données distribués**.
- **Règle :** scénarios imaginés, calculs d’ordre de grandeur et infrastructures réellement déployées ne seront pas confondus.

## FAB — Procédés de fabrication imaginés

- **FAB-001 — LDPF 3 Medium / High**.
- **FAB-002 — LDPF 2.5**.
- **FAB-003 — LDPF 2.0**.
- **FAB-004 — LDPF 1.5**.
- **FAB-005 — GAAFET, rendement, binning et feuilles de route proposées**.
- **À retrouver :** définitions des noms, dimensions et objectifs; aucune disponibilité industrielle ou valeur de rendement n’est confirmée.

## ELEC — Électronique, refroidissement et embarqué

- **ELEC-001 — AFLC / Adaptive Fan Laminar Control / AFLC 2.0** : contrôle intelligent de ventilateur évoqué.
- **ELEC-002 — CPU Cooler V3**.
- **ELEC-003 — Logiix Lunna Micro**.
- **ELEC-004 — mini-GPU expérimental / processeur simple sur FPGA**.
- **ELEC-005 — cartes multi-MCU** : concepts autour de ds89c450, MSP430, ATmega et d’autres composants; les laboratoires scolaires seront séparés des inventions.
- **ELEC-006 — égaliseur audio de laboratoire** : projet scolaire, étages audio A–F et adaptation mono/stéréo; ne pas le présenter comme invention Logiix.
- **ELEC-007 — STM32 et outils de laboratoire** : bibliothèques et labs rapportés; à classer dans travaux d’apprentissage tant que le contraire n’est pas démontré.

## OS — Systèmes et outils logiciels

- **OS-001 — LiixOS**.
- **OS-002 — Logiix Universe OS**.
- **OS-003 — concepts d’OS hybrides**.
- **OS-004 — diagnostics et outils d’ingénierie assistés par IA**.
- **OS-005 — mémoire locale et télémétrie**.
- **OS-006 — extensions intelligentes pour IDE, KiCad et outils techniques**.

## APPLE — Propositions spéculatives

- **APPLE-001 — OS28** et fonctions proposées : gestion native de conteneurs, mode bureau externe, mises à jour A/B, DiskView, Photos Pro, Aperçu, Notes et relecture IA.
- **APPLE-002 — Apple Scholar Manager** : nom proposé dans le contexte; sens/fonctions à reconstituer.
- **APPLE-003 — gestion d’appareils scolaires/professionnels et sessions séparées pro/perso**.
- **APPLE-004 — HomeKit amélioré**.
- **APPLE-005 — watchOS, tuiles et mesures sportives**.
- **APPLE-006 — SiriLM, SwiftLM, xCodeLM, DevLM**.
- **APPLE-007 — architectures Apple hypothétiques et datacenters Apple Intelligence**.
- **Règle :** ce sont des idées attribuées à des conversations; aucune ne doit être attribuée à Apple comme annonce ou développement.

## MISC — Concepts supplémentaires

- **MISC-001 — appareil polyvalent inspiré du Flipper Zero** avec NFC, Bluetooth et Wi‑Fi.
- **MISC-002 — architectures MoE/MoM de fournisseurs externes**, notamment propositions de tailles évoquées pour Mistral.
- **MISC-003 — scénarios imaginaires de modèles GPT-6 Luna/Sol** : à séparer des modèles annoncés et des tarifs publiés.
- **MISC-004 — débruitage IA sous contrainte <0,25 W** : lien potentiel à HOLO-006, à confirmer.
- **MISC-005 — automatisation de projets IA longue durée** : lien fonctionnel possible entre Orbit et Liix; ne pas fusionner les produits.
- **MISC-006 — autres idées d’IA, électronique, scientifique ou industrielle** : catégorie ouverte; chercher dans les archives.

## À faire avant de transformer les entrées en fiches finales

Pour chaque ID, retrouver au minimum un échange ou fichier source. Puis consigner : nom exact et variantes, date de source, formulation d’origine, statut, chiffres cités, évolutions, contradictions et liens vers les concepts apparentés. Les fiches techniques ne doivent pas compléter les paramètres absents par des valeurs plausibles.
