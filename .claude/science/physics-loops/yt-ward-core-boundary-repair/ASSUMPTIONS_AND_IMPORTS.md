# Assumptions And Imports

## Load-Bearing Imports

| Input | Role | Status on latest main |
|---|---|---|
| `native_gauge_closure_note` | Supplies the retained nonabelian `SU(2) x SU(3)` surface used for the selected `(2,3)` block dimension. | `audited_clean / retained` |
| `g_bare = 1` canonical bare-action normalization | Admitted context for writing the matrix element as `g_bare/sqrt(6)`. | open derivation target, not closed here |
| staggered-Dirac realization | Admitted context for the bare-action surface. | open derivation target, not closed here |

## Removed As Load-Bearing Imports

- `yt_vertex_power_derivation`: no longer needed because shared tadpole
  power counting is not an auditable claim of this note.
- `yt_ew_color_projection_theorem`: no longer needed because the core
  calculation uses direct finite-dimensional Fierz algebra and does not
  import the EW normalization family.
- `yukawa_color_projection_theorem`: no longer needed because this repair
  defines and normalizes the local scalar-singlet operator directly in the
  source note.
- `left_handed_charge_matching_note`: no longer needed because the core
  uses only the nonabelian `(2,3)` dimension, not the abelian charge ratio.

## Axioms

No new axioms are introduced. The note continues to use only the framework
axioms `Cl(3)` and `Z^3`, plus standard finite-dimensional group and Clifford
algebra.
