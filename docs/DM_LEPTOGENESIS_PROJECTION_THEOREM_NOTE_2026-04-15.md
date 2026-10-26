# Conditional leptogenesis matrix projection identity

**Type:** bounded_theorem
**Status:** supplied positive-matrix algebra; physical denominator matching open.
**Script:** `scripts/frontier_dm_leptogenesis_projection_theorem.py`

Supply a positive-definite Hermitian H, Y_+=H^(1/2), and unitary U_M.
Then Y_+^dag Y_+=H and, defining Y_mass=Y_+ U_M,
Y_mass^dag Y_mass=U_M^dag H U_M=K_mass. Taking entry00 proves the
coordinate identity (Y_mass^dag Y_mass)00=(K_mass)00.

Calling that entry the physical leptogenesis denominator additionally requires
identifying this supplied Y_mass with the physical Yukawa matrix and its basis
with the physical heavy channel. Neither the polar identity nor a script's
explicit /K00 division derives that identification. In particular K00=2tau_+
and tau_E=tau_T=1/2 are extra matching/amplitude premises. H=3I gives K00=3
while independently supplied tau_+=1 gives2, preserving the parent's counterexample.

The finite positive-matrix and basis-rotation checks remain; documentary reads
of older kernels record their chosen conventions, not physical closure.
No washout, transport, normalization or whole-package conclusion follows.

- [conditional K00](DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md)
- [polar context](DM_NEUTRINO_POSITIVE_POLAR_H_CP_THEOREM_NOTE_2026-04-15.md)
- [epsilon wrapper context](EPSILON1_FROM_CP_CHAIN_NOTE_2026-05-03.md)
