# Supplied-block Schur return and separate curvature identification

**Type:** bounded_theorem
**Status:** supplied finite algebra/evidence; physical bridge open
**Primary runner:** `scripts/frontier_dm_neutrino_schur_suppression_theorem.py`

Supply projectors P onto T1 and Q onto O0+T2, the displayed Gamma1, and M=mI+jGamma1 with m!=0. On these sectors P Gamma1 P=Q Gamma1 Q=0 and P Gamma1 Q Gamma1 P=P. Thus the Q block is mI, invertible, and its Schur complement is (m-j²/m)I on P. The return correction is j²/m. This is an exact block identity, not yet a physical Yukawa coupling.

For the separately supplied potential V=32 sum_(i<j) phi_i² phi_j², the Hessian at e1 is diag(0,64,64); its transverse quadratic coefficient is 32. Identifying this coefficient with the heavy block parameter m is an EXTRA curvature-to-block assumption. Units, kinetic normalization and the relation of a potential Hessian (mass-squared after normalization) to the block mass coefficient must be supplied. Curvature alone does not make m=32 a physical theorem.

If additionally m=32 and j=g_weak/sqrt(2), arithmetic gives j²/m=g_weak²/64. The runner's g_weak=.653 and staircase constants are supplied comparison values. Its k_eff near 8.01 is a numerical conversion, not exact level selection or a closed DM denominator. The full effective diagonal remains m-j²/m; the correction alone must not be silently identified with the full physical coupling.

The runner retains numerical Schur checks and curvature checks. Source/bridge selection, physical normalization, curvature-to-block matching and staircase interpretation remain open. Neither a new retained status nor uniqueness of these inputs is asserted.

## Provenance

Prior text is recoverable at Git `f24d17d97d372df977476e4a69674577f31af575` under this path. Related definitions/context (no blanket status endorsement):

- [`DM_NEUTRINO_DIRAC_BRIDGE_THEOREM_NOTE_2026-04-15.md`](DM_NEUTRINO_DIRAC_BRIDGE_THEOREM_NOTE_2026-04-15.md)
- [`DM_NEUTRINO_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md`](DM_NEUTRINO_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md)
