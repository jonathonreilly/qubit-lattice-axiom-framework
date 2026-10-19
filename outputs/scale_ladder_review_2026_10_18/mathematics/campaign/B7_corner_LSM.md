> Live supporting mathematical source with scope corrections. Historical run tables and numerical values below are submitted evidence, not a fresh capture or independent validation. The cross-rung primary does not execute these campaign producers. Exact displayed algebra retains its stated hypotheses. Terminal exclusions beyond the explicitly active constructive results remain deferred scientific proposals; their full arguments are preserved here for inspection and are not adopted by historical verdict labels.

# B7 findings: filling constraints (LSM type) for the corner fermion



## Reduction (exact)

- Every dressed symmetry acts as G_g|v,c⟩ = (−1)^(λ_g·v + τ_g(c)) |gv, gc⟩.
- In momentum space it maps k → gk + πs_g by one 12×12 matrix U_g, the same at every k.
- The site shell and the full-group fixed Bloch spaces carry the displayed decomposition. A generic Bloch momentum is mapped to other momenta, so it is not itself a full-O invariant space.
- Only ±k* are fixed by all 24 rotations; Γ is fixed by one C3 only.

## Free fermions

- **Theorem: odd filling is forced gapless** (`b7_free_fermion_filling.py`, PASS=14).
  - Hypothesis: translations plus any subgroup of dressed rotations containing three mutually commuting C2s (O, T, D4, D2, or D2′).
  - At k* the lifts of two commuting C2s anticommute, so every level at k* is even.
- The submitted constructions provide even-filling candidates for ν = 2…10; their original certification arguments remain source-specific, not a new exhaustive classification by the cross-rung primary.
- **Inversion** (`b7_inversion_wannier.py`): on-site insulators exist only at ν ≡ 0 mod 4. For ν = 2, 6 and 10, a certified Wannier doublet at the cube centre works.
- **Minimal symmetry** (`b7_subgroups.py`): with only C4, C3 or a single C2, ν = 1 insulators exist (gaps 0.52–0.61). The Wyckoff positions 1a, 1b, 3c and 3d carry the nontrivial class.
- **The node filling is ν = 1.** The Weyl node is the touching of bands 1 and 2 at k*, so it is forced gapless.
  - At the runner point, ν = 1 is a compensated metal (0.40 states per site below the node).
  - ν = 2 is not forced (bands 2 and 3 overlap by 0.015).
- **A Dirac mass at ν = 1** needs translation breaking or loss of the commuting C2s. The A2 staggered mass doubles the cell.

## Many-body

`b7_many_body_lsm.py`, PASS=13.

- **Exact finite-size result.**
  - On odd-L tori with U(1) twist θ = ±k*, all 24 dressed rotations are symmetries.
  - The two commuting C2s commute only up to (−1)^N, so odd ν gives even degeneracy of every eigenvalue.
  - With θ = 0, the 21 shifted rotations fail.
  - Checked by exact diagonalisation on L=3 (one particle) and L=1 (interacting).
- **Conditional.** Assume a symmetric short-range-entangled (SRE) phase has a unique gapped ground state on large odd twisted tori (the standard hypothesis: Oshikawa 2000; Watanabe–Po–Vishwanath–Zaletel 2015). Then no symmetric SRE state exists at odd ν. The block-state counting of Po–Watanabe–Jian–Zaletel 2017 and Else–Thorngren agrees.
- **Even ν** has symmetric product states with commuting-projector parents.
- **Doubled-cell class** (`b7_staggered_class.py`, PASS=5):
  - Free fermions: folded k* levels are multiples of 4, so odd ν has no Slater insulator.
  - Many-body: an entangled O_h-covariant pair state on the even sublattice is a symmetric SRE insulator at ν = 1.
  - So the quartet protection is free-fermion only.

## Caveats

- Antiunitary symmetries, superconductors, other flux patterns and the qubit-code realisation are not covered.
- Whether a symmetric interacting gap actually occurs is not shown.
- The mechanism is the standard double-group filling constraint for electrons with spin-orbit coupling and no time reversal. New here:
  - its origin in the gauge PSG;
  - the k* twist;
  - the Wyckoff table;
  - the minimal symmetry (commuting C2s);
  - the node filling;
  - the free-fermion versus many-body split.
