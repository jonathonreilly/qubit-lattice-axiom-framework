# Direct microscopic interaction investigation

Target: derive a dynamical scalar and normalized coupling from existing one-qubit-per-site model terms, without adding an interaction. Main fa841753c1a6296e5ad45518375660b0f1004769; parent response PR9686 is now landed. Root personally authors; old campaigns remain stopped. Other checkout changes preserved.

Read corner-code and fine-site embedding source, exact Pauli definitions, and PR9689 body at06b8f42d9bbf956763f5a3ea90d0992d0e67b145 (scope only: no clean Dirac vacuum established). The new source tests are independent of any claimed Dirac vacuum. Current-main corner code has a guarded runner wrapper; extract only its definitions by AST, without executing review checks.

Routes: virtual loop/repetition excitations; virtual high-energy fermion bands; noncommuting charge/hopping collective response; coherent or statistical flux sectors; relaxing frozen spectators. All must preserve the actual Hamiltonian. Nearby prior art NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08 already states static flux under native hopping. September24 compass carving is a different supplied Hamiltonian, not a derived completion of the corner code. Do not repackage those general observations as new discoveries.

First decisive test: exhaustive exact Pauli centrality at L4 plus a controlled finite Fock-space elimination calculation. The new value is resolving the specific proposed virtual-interaction mechanism for the current scalar consumer, not novelty of quadratic closure or Schur complements.

## Checked result
Root completed14 primary controls including exhaustive centrality,3072 probe syndromes, and exact operator derivations. Independent geometry reproduces2304 classes (1536 singleton,768 pairs), no empty syndrome and diameter1. Three source mutations detected. Independent source review PASS; no scalar derived and no physical assumptions retired. The diagnostic H_V family proves one-particle evidence cannot choose the many-body interaction. Neutral composites remain open. No research jobs remain; final packaging only.
