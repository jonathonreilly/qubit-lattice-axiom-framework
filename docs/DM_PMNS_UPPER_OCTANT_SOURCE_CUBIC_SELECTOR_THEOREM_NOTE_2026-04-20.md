# DM PMNS supplied-bank upper-octant / source-cubic diagnostic

**Date:** 2026-04-20
**Lane:** DM A-BCC / open imports `I12` and `I5`
**Type:** open_gate
**Status:** conditional algebra and finite supplied-table comparisons; physical selection open
**Primary runner:** `scripts/frontier_dm_pmns_upper_octant_source_cubic_selector_theorem_2026_04_20.py`

## Supplied bank, target and filter

`CHAMBER_ROOTS` is a historical variable name for three supplied decimal points, not a complete exact-root census. The matrix function, ascending eigenvector-column ordering, row labels and angle target `(0.307,0.0218,0.545)` are supplied. The runner evaluates each point under `(2,1,0)` and `(2,0,1)`, then applies two stipulated filters:

```text
s23^2 > 1/2,
I_src(H) = Im(H_12 H_23 H_31) > 0.
```

Neither filter is derived here as a physical law. Selecting a row from this finite table does not fix the physical charged-lepton assignment, a global source or the physical CP sign.

The original numerical functions, full-precision bank entries, target values, bisection steps, solver behavior and all nontrivial predicates are unchanged. For these supplied values the checks compare the following approximate outputs:

| Supplied entry | Upper-octant label | s23² | I_src | computed sin(delta_CP) |
|---|---|---:|---:|---:|
| Basin1 | `(2,1,0)` | .545 | +.30356 | -.98736 |
| Basin2 | `(2,1,0)` | .545 | -225.76 | +.55439 |
| BasinX | `(2,0,1)` | .545 | -99.77 | -.41878 |

The actual cache, not rounded table entries, records current checks and failures. Within this supplied list, the stipulated positive source-cubic filter keeps the Basin1 label. No other point or physical alternative is excluded.

## Conditional row-swap identity

Let U be a unitary 3×3 matrix with the same column ordering in both comparisons. Keep the electron row fixed and interchange only the muon and tau rows. The labeled modulus matrix is permuted, not unchanged. Electron-row moduli remain unchanged.

Write `c13²=1-|U_e3|²>0` and define `s23²=|U_mu3|²/c13²`. Column normalization gives `|U_mu3|²+|U_tau3|²=c13²`; hence the swapped value is `1-s23²`. This is a conditional identity for these labels, not a physical preference for one labeling.

For the runner's convention `J=Im(U_e1*conj(U_e2)*conj(U_mu1)*U_mu2)`, set `z_r=U_r1*conj(U_r2)`. Column orthogonality gives `z_e+z_mu+z_tau=0`, so

```text
Im(z_e*conj(z_tau))
 = Im(-|z_e|²-z_e*conj(z_mu)) = -J.
```

A corresponding sin(delta_CP) sign flip follows only when the chosen angle convention has a nonzero positive normalization denominator `s12*c12*s23*c23*s13*c13²`; mu/tau swapping preserves that denominator. At degenerate angle boundaries the phase can be undefined. The floating helper clamps tiny denominators and clips its reported value; its finite checks are not a general exact phase certificate.

## Numerical branch-threshold candidate

`central_theta23_threshold` calls the supplied `boundary_distance` routine at fixed `(s12²,s13²)=(.307,.0218)`, brackets [.53,.55], and performs 80 bisections with unchanged sign decisions. It reports a numerical branch candidate near .540970 and compares it to the supplied labels. The helper selects a numerical branch; this is not rigorous uniqueness, continuity, monotonicity, an enclosure, whole-rectangle coverage or an exhaustive chamber threshold. No physical upper-octant law follows.

## Context and withdrawn claims

The [finite chamber-candidate diagnostic](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_THEOREM_NOTE_2026-04-20.md) supplies no exact three-basin completeness theorem. The historical [Krawczyk](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md), [threshold](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md), [threshold-surface](PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md), [rectangle](PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md) and [parity-reduction](DM_PMNS_CP_ORIENTATION_PARITY_REDUCTION_NOTE_2026-04-20.md) notes are contextual routes whose full claims are not accepted premises of this finite owner. Their titles and historical status supply no authority for physical selection.

The prior exact-completeness, physical Basin1/negative-CP selection and `I12`-closed conclusions are withdrawn. `I12`, physical source/row/filter selection, target provenance and the CP-sign derivation remain open; `I5` is not reduced to angles alone. Original source/cache are preserved at `f00d5860eff9d8b6fdab9d5c3f2fc1d2fab63409` and in repair evidence. No historical failure or claim is erased or recast as independent success.

## Reproduction

Run `PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_upper_octant_source_cubic_selector_theorem_2026_04_20.py` under the declared 300-second bound. Its canonical cache is a finite diagnostic receipt, not a physical selection theorem.
