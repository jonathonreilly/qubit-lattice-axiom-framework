# 3D Factorized-Protocol Selection on the Analyzed Period-2 Classes

**Date:** 2026-07-09
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** Computed selection statement for the named period-2 protocol
inventory on the one-Grassmann-per-site `Z^3` carrier, using site-modulus
one-site-translation covariance, all-axis nonvacuous conditioning, and the
named dispersiveness conditional. G1-G3 give the stated four-member survivor
set. The stronger G4-G5 conclusion is bounded by the three computed
divergences recorded below.
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:**
[`scripts/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.py`](../scripts/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.py)
**Runner cache:**
[`logs/runner-cache/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.txt`](../logs/runner-cache/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.txt)

## Why This Note Exists

The landed 3D note names this underived realization input:

> The load-bearing extra input is the **factorized-realization input**: the realized 3D protocol is the symmetric per-axis decorated-shift cycle. This note does not derive that selection.

This note tests whether two current axiom clauses plus the named
dispersiveness conditional supply that selection on the analyzed period-2
classes. They do compute a narrow G1-G3 survivor set and exclude the named
nonfactorized competitors. The inventory as written does not support the
stronger equivalence claim for every survivor because of `P_WEIGHT`.

## Computed Divergences From The Conjectured Characterization

The runner confirms the constructed property table, the G1-G3 survivor sets,
the factor identities, and the rejector constructions, and it computes three
divergences from the conjectured stronger characterization, namely that every
G3 survivor equals the symmetric cycle up to octant choice, a central sign,
and central quantized whole-cell translations.

1. The constructed `P_WEIGHT = S_1 S_1 S_2 S_3` obeys
   `P_WEIGHT = exp(-i k_1) S_2 S_3`; it is not the symmetric three-axis cycle
   times a central scalar. Therefore the conjectured G4 equivalence does not
   hold for every G3 survivor.
2. The same word has composite site-slope magnitudes `(2,1,1)`, not
   `(1,1,1)`. Every elementary decorated mover still has magnitude one on its
   own axis.
3. `P_MIX4` and `P_STAIR` pass the `L1` variation-only filter, but they do
   not pass a literal ablation of G1 that retains G2 axis-uniformity. Their
   `[1,1,0]` pattern is independently rejected by that condition, and the
   literal ablation leaves the G3 survivor set unchanged on this inventory,
   so the translation clause has no unique kill here; its unique-kill witness
   in this campaign is the flat `UMIX` family in the per-axis sibling note.

## Statement

The two quoted clauses are:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

> For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions.

Translations here are the standard one-site translations of `Z^3`; the
period-2 blocking is an analysis device. A one-component-per-site carrier has
local `U(1)` site frames. Site-level matrix-element moduli are therefore the
translation test data, while the eta phases carry gauge and flux content.
Proper cubic rotations act transitively on the axes, so the nonvacuity pattern
must be constant across axes.

The constructed inventory and full pre-gate probe are:

| Protocol | Constructed word or tick | Factor translation defect | Nonvacuity | Axis-uniform | Dispersive |
|---|---|---:|---:|---:|---:|
| `P_SYM` | `S_1 S_2 S_3` | `0` | `[1,1,1]` | yes | yes |
| `P_SYM_OCT` | `S_1^- S_2 S_3`, with the reverse mover constructed from reversed offsets | `0` | `[1,1,1]` | yes | yes |
| `P_REORDER` | `S_2 S_1 S_3` | `0` | `[1,1,1]` | yes | yes |
| `P_WEIGHT` | `S_1 S_1 S_2 S_3` | `0` | `[1,1,1]` | yes | yes |
| `P_AXIS` | `S_1`, with decorated and bare forms checked | `0` | `[1,0,0]` | no | yes |
| `P_MIX4` | planar mixed four-cycle | `1` | `[1,1,0]` | no | yes |
| `P_STAIR` | planar parity-conditioned staircase | `1` | `[1,1,0]` | no | yes |
| `P_PAIRFLAT` | commuting-pairing product at `theta=pi/5` | `0.38471` | `[1,1,1]` | yes | no |
| `P_CANCEL` | opposite decorated movers paired on every axis | `0` | `[1,1,1]` | yes | no |
| `P_DIAG` | diagonal period-2 phases | `0` | `[0,0,0]` | yes | no |

The computed gates are:

- **G1, one-site translation clause.** The zero-defect set is
  `{P_SYM, P_SYM_OCT, P_REORDER, P_WEIGHT, P_AXIS, P_CANCEL, P_DIAG}`.
- **G2, nonvacuous all-axis-uniform variation.** The set becomes
  `{P_SYM, P_SYM_OCT, P_REORDER, P_WEIGHT, P_CANCEL}`.
- **G3, named dispersiveness conditional.** The set becomes
  `{P_SYM, P_SYM_OCT, P_REORDER, P_WEIGHT}`.
- **G4, survivor structure.** The runner recomputes pairwise decorated
  anticommutation, `P_REORDER = -P_SYM`, and
  `S_i^2 = exp(-i k_i) I`. It also constructs the octant variant directly.
  For the specified weighted word, however,
  `P_WEIGHT = exp(-i k_1) S_2 S_3`, and a scalar-multiple test against
  `P_SYM` is false. Hence the conjectured characterization
  up to octant choice, a central sign, and central quantized whole-cell translations
  is not established for the full G3 set.
- **G5, slope content.** `P_SYM` and `P_SYM_OCT` have composite site-slope
  magnitudes `(1,1,1)`. `P_MIX4` and `P_STAIR` have
  `(1/2,1/2,0)`. Each decorated mover has magnitude one on its own axis, but
  the specified `P_WEIGHT` composite has `(2,1,1)`.

## Proof Sketch

The runner copies `comps`, `idx`, `eta_val`, `S_axis`, `mixed_cycle_tick`,
`staircase`, the site-license degree table, and the `P12` plus
`Vg = diag((-1)^(p0*p1))` projective-covariance check. Every inventory member
and every elementary factor is checked for unitarity on both the `8x8` Bloch
cell and the `64x64` site ring. The opposite-axis mover is built directly from
the reversed offset convention before its inverse relation is tested.

For each protocol factor `F`, the runner evaluates
`max_a max_entries ||T_a F T_a^dag|-|F||`. It then scans actual site-level
nearest-neighbor matrix support to obtain the nonvacuity vector. Momentum
dependence is tested through characteristic-polynomial coefficients at fixed
momenta, avoiding band-order assumptions.

For `P_PAIRFLAT`, the three `M_i` are computed to be pairwise commuting
Hermitian unitaries. The product is unitary, has the momentum-independent
bands `exp(i theta (s_1+s_2+s_3))` for `s_i` in `{-1,+1}`, and passes the
`P12` axis-permutation conjugation. Its site-modulus translation defect is
positive, so variation plus axis covariance without the translation clause
does not force dispersiveness.

The exact fourth-power identities give the mixed-cycle and staircase slope
magnitudes `(1/2,1/2,0)`. The central mover-square identities give one edge per
tick for each elementary decorated factor. Direct composite-square identities
give `(1,1,1)` for the symmetric and octant words and `(2,1,1)` for the
specified weighted word.

The rejector legs are also computed:

- **L1.** The variation-only filter admits `P_MIX4` and `P_STAIR`, both with
  nonunit quantized slopes. A literal removal of G1 while retaining
  axis-uniformity does not admit either protocol; this is the third divergence
  recorded above.
- **L2.** Removing axis-uniformity admits `P_AXIS`.
- **L3.** Removing dispersiveness admits flat `P_CANCEL`. The conditional is
  load-bearing at the word level. Its per-axis supplier is the
  [sibling selection note](TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md);
  which words realize the one fixed rule remains named open.
- **L4.** `P_PAIRFLAT` is axis-permutation covariant, all-axis nonvacuous, and
  flat, while failing the one-site translation test.
- **L5.** Replacing eta-decorated factors by bare shifts preserves the
  protocol-level translation, variation, and dispersiveness tests. The bare
  factors commute, while the decorated factors anticommute. Thus these clauses
  test protocol shape; the eta decoration and its flux class come from the
  landed Kawamoto-Smit forcing chain.
- **L6.** Replacing `P_SYM` by `P_MIX4` changes the computed G1-G3 stack; the
  honest G3 set contains `P_SYM`, while the corrupted set does not.

## Consequence And Residual

On the analyzed period-2 inventory, the two clauses plus the named
dispersiveness conditional compute the G3 set
`{P_SYM, P_SYM_OCT, P_REORDER, P_WEIGHT}`. They select the symmetric
decorated per-axis protocol shape for `P_SYM`, its explicitly constructed
octant variant, and its central-sign reorder. The weighted member as specified
prevents extending that statement to every survivor under only the named
central residuals.

The residuals are:

- octant and handedness choice;
- the central sign from factor ordering;
- quantized-translation weights, corresponding to the landed clock/drift
  normalization family with the `r=1` readout conditional; an even extra
  mover pair is central, while the inventory's single extra `S_1` changes the
  composite slope and remains the explicit G4-G5 discrepancy;
- the word-level reading of the dispersiveness conditional;
- periodicity scope: the mod-3 six-cycle staircase variant named in the landed
  3D runner's comments lives outside the period-2 cell and is excluded by the
  periodicity scope, not by these clauses;
- class transport beyond the representatives;
- P2.

This note does not modify the registered kinetic-isotropy primitive. It also
does not alter the eta decoration class supplied by the landed parent.

## Boundaries

- The result covers the constructed analyzed classes on the period-2 cell.
- The landed 3D note's boundary remains exact:

  > It does not claim an exhaustive classification of all non-covariant, amplitude-mixing single ticks. Those remain a named open surface.

- The checks are at representative level. Class transport is a named
  residual.
- Pairing supplies a flat covariant varying witness, but it fails one-site
  translation covariance in site moduli.
- The mod-3 six-cycle staircase variant is outside this periodicity scope.
- There is no Tier-A registry change and no audit status is set here.

## Dependencies

- [KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md](KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  supplies the 3D constructions, factor identities, and bounded-class scope.
- [STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  supplies the per-axis flat/saturating dichotomy.
- [TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md](TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md)
  supplies the per-axis dispersiveness conditional in the same campaign.
- [REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md](REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md)
  supplies the all-axis conditioning-pattern logic.
- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md)
  supplies the two quoted clauses.

Context only: `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`,
`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`.

## Runner And Cache

Primary runner:
[`scripts/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.py`](../scripts/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.py)

Runner cache:
[`logs/runner-cache/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.txt`](../logs/runner-cache/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.txt)

Current local runner result:

```text
TOTAL: PASS=40 FAIL=0
```

## Changelog

- **2026-07-09.** Initial bounded note and deterministic runner. The runner
  reports `TOTAL: PASS=40 FAIL=0` and records the three computed divergences.
