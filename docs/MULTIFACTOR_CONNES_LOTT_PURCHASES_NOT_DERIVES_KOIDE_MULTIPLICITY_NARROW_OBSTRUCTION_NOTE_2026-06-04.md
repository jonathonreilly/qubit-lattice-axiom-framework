# Flavor-Blind Multi-Factor Connes-Lott Purchases, Does Not Derive, the Koide (1,1) Multiplicity (Narrow Obstruction)

**Date:** 2026-06-04
**Type:** no_go
**Claim type:** no_go (narrow, route-specific) - prunes the flavor-blind
multi-factor Connes-Lott route in the inventoried clean single-qubit Koide
route table. It does not close flavor-structured/admitted NCG models,
eta-phase mass-weighting, or explicit multiplicity-counting admissions.
**Claim scope:** for any extra algebra factor on which the C3 generation action
is trivial, such as chirality `H_L \oplus H_R`, color, or KO/real-structure
doubling, tensoring or direct-summing scales the C3 singlet and doublet
isotypes equally. The `(1,2)` real-dimension weighting (legacy F3, kappa=1,
r=1) is preserved. Reaching the `(1,1)` multiplicity weighting (legacy F1,
kappa=2, r=1/2) requires a C3-equivariant but isotype-distinguishing operator
`W = P_+ + (1/2) P_doublet`, equivalently an explicit flavor-structured
admission or separate derivation target. A flavor-blind factor purchases that
input; it does not derive it.
**actual_current_surface_status:** exact structural pruning of the
flavor-blind multi-factor route; **conditional** on the open
[staggered-Dirac realization gate](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md).
Not retained on the current surface.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_multifactor_cannot_cleanly_give_koide_multiplicity_exact.py`](./../scripts/audit_companion_multifactor_cannot_cleanly_give_koide_multiplicity_exact.py)

## Context

The Koide target `r = 1/2` (Q=2/3) needs the `(1,1)` multiplicity weighting of
the C3 singlet/doublet isotypes (legacy F1, kappa=2). The surfaced
Gaussian/measure route gives the `(1,2)` real-dimension weighting (legacy F3,
kappa=1, r=1):
[Probe 25](KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md)
and
[Probe 29](KOIDE_BAE_PROBE_KAPPA_PREDICTION_TEST_PARTIAL_FALSIFICATION_NOTE_2026-05-09_probe29.md)
record that residue. The
[fermion-determinant companion](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
and the
[taste-normalization companion](STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
pruned two further clean routes.

The
[single-factor C3-equivariant anti-commuting note](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
only addresses the literal identification of the Connes-Lott chirality grading
with the C3 generation grading on the same `R^3` factor; it explicitly does not
close generic Connes-Lott models. The route tested here is narrower and
different: a flavor-blind multi-factor construction whose extra factor carries
trivial C3 action.

## Statement

1. (**isotype weights**) On the generation space `C^3`, the C3 isotypes are a
   singlet of real dimension 1 and a doublet of real dimension 2. For the
   C3-circulant Yukawa `M = aI + bC + b-bar C^2`, the Frobenius split is
   `||aI||^2 = 3a^2` and `||bC + b-bar C^2||^2 = 6|b|^2`.
2. (**flavor-blind tensor**) For any flavor-blind factor `V = C^n` with trivial
   C3 action, the enlarged isotype dimensions are `(n, 2n) = n*(1,2)`. The
   singlet:doublet ratio `1:2` is preserved.
3. (**flavor-blind direct sum**) Chirality `H_L \oplus H_R`, color copies, and
   KO/real-structure doubling are flavor-blind in this sense when they commute
   with the C3 generation action. They also preserve `1:2`.
4. (**the (1,1)-maker is flavor structure**) The operator
   `W = P_+ + (1/2) P_doublet` is C3-equivariant, since it commutes with the C3
   generator, but it is not scalar on the isotype decomposition. It acts by
   different weights on singlet and doublet, so it is a flavor-structured input.
5. (**two balance points**) The per-real-dimension balance gives
   `3a^2 = 3|b|^2`, hence `r=1`. The per-block balance gives
   `3a^2 = 6|b|^2`, hence `r=1/2`. The gap is exactly the relative factor 2
   in `W`.

All runner checks pass exactly.

The reason is Schur-style isotype bookkeeping: tensoring or direct-summing with
a C3-trivial space scales every C3 isotype multiplicity by the same integer, so
it cannot change the singlet:doublet ratio. Only an isotype-distinguishing
operator can change that ratio, and that operator is the admitted
multiplicity-counting structure unless a separate retained derivation supplies
it.

## Synthesis - Inventoried Clean Flavor-Blind Routes

| route | result | status |
|---|---|---|
| free Gaussian measure on Herm_circ(3) | `(1,2)`, legacy F3 -> kappa=1, r=1 | pruned by [Probe 25](KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md) |
| corner fermion determinant `det(M)` | shape-stationary at r=1, r=4 | pruned by the [determinant companion](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md) |
| Z3 scalar potential `V(Tr K)` | `V_eff` minimum does not coincide with the physical point | pruned by the [scalar-potential support note](KOIDE_Z3_SCALAR_POTENTIAL_SUPPORT_NOTE_2026-04-19.md) |
| taste-breaking normalization | tastes span `M_2(C)`, no extra multiplicity | pruned by the [taste-normalization companion](STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md) |
| flavor-blind multi-factor Connes-Lott | flavor-blind factors preserve `(1,2)`; `(1,1)` requires `W` | pruned by this note |

Within this finite table, no clean flavor-blind route derives the `(1,1)`
multiplicity weighting from the
[Lattice + Quantum + Record baseline](MINIMAL_AXIOMS_2026-06-04.md). The honest
residual is explicit: admit the multiplicity-counting principle, or derive a
flavor-structured isotype reweighting in a separate source note. This is not a
universal no-go against NCG, and it is not an empirical claim that Q=2/3 is
wrong.

## NO-GO DISCIPLINE GATE (N1-N8)

| # | Check | Result |
|---|---|---|
| N1 | >= 5 attack routes named | 5: free measure [pruned, [Probe 25](KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md)]; fermion determinant [pruned, [determinant companion](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)]; Z3 scalar potential [pruned, [scalar-potential support note](KOIDE_Z3_SCALAR_POTENTIAL_SUPPORT_NOTE_2026-04-19.md)]; taste-breaking [pruned, [taste-normalization companion](STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)]; flavor-blind multi-factor [pruned here]. Residual: explicit multiplicity-counting admission or separate flavor-structured derivation target. |
| N2 | wall independence | The flavor-blind multi-factor wall is independent of the determinant, measure, scalar-potential, and taste walls: it is an isotype-ratio invariance fact. |
| N3 | hidden-wall scan | The C3-trivial action of the extra factor is a claim-scope restriction, not hidden universal NCG scope. The open staggered-Dirac realization gate is explicit. Literature is comparator only. |
| N4 | residual matching | Matches Probe 25/29: `(1,2)` real-dimension weighting remains kappa=1; `(1,1)` multiplicity is not derived by the cited clean routes. This note adds that flavor-blind extra factors also do not supply it. |
| N5 | rhetoric resolution | Scoped to flavor-blind factors preserving `(1,2)`. It does not say no two-factor model can fit leptons, and does not say no mathematics can generate `r=1/2`. |
| N6 | partial-closure path | The partial-closure path is named rather than dismissed: an explicit multiplicity-counting admission, or a separately audited flavor-structured derivation of `W`, would close the residual. That is not silently supplied by an axiom or primitive. |
| N7 | steelman | A model-specific two-factor triple with nontrivial C3 action, or with an order-one/first-order condition that forces `W` internally, could generate the desired reweighting. That would be a separate flavor-structured theorem or admitted structural input; it is not covered by this flavor-blind no-go and is not claimed impossible here. |
| N8 | cross-cycle echo | Consistent with [Probe 29](KOIDE_BAE_PROBE_KAPPA_PREDICTION_TEST_PARTIAL_FALSIFICATION_NOTE_2026-05-09_probe29.md), the [r=1/2 dynamical-norm-balance no-go](KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md), the [determinant companion](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md), and the [taste-normalization companion](STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md). No prior convention-only reframe supplies the flavor-structured `W`. |

**Verdict:** narrow route-pruning for flavor-blind multi-factor constructions.
Residual: explicit multiplicity-counting admission, or a separate
flavor-structured derivation of `W`.

## What this claims / does NOT claim

- Claims: flavor-blind multi-factor extensions preserve the `(1,2)` weighting;
  the `(1,1)`/r=1/2 weighting requires an isotype-distinguishing input.
- Does **not** claim NCG/Connes-Lott is wrong.
- Does **not** claim no two-factor model can fit the leptons; it says any such
  model must supply flavor structure beyond a C3-trivial factor.
- Does **not** claim Q=2/3 is empirically wrong.
- Conditional on the open staggered-Dirac realization gate.

## Trace gate

```yaml
trace_class: negative_route_pruning
target_blocker_text: "BAE admission |b|^2/a^2=1/2 (r=1/2) on the charged-lepton lane"
source_of_blocker_text: audit_ledger
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "test whether a separately specified flavor-structured derivation of W exists; otherwise keep r=1/2 as an explicit multiplicity-counting admission"
```

## Forbidden imports

- Literature (Connes-Lott NCG, KO-dimension, real structure J) is comparator
  only. The isotype decomposition and ratio-invariance are reproven from the C3
  generation representation. No PDG values as derivation inputs.

## Cross-references

- [KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md](KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md)
  - measure route gives the real-dimension weighting.
- [KOIDE_BAE_PROBE_KAPPA_PREDICTION_TEST_PARTIAL_FALSIFICATION_NOTE_2026-05-09_probe29.md](KOIDE_BAE_PROBE_KAPPA_PREDICTION_TEST_PARTIAL_FALSIFICATION_NOTE_2026-05-09_probe29.md)
  - records the kappa=1 vs kappa=2 residue.
- [CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
  - determinant route pruning.
- [STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md](STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
  - taste-normalization route pruning.
- [KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md](KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md)
  - why r=1/2 must be supplied dynamically or admitted.
- [KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md)
  - isotype Frobenius split and legacy F1/F3 weighting.
- [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  - open gate this note remains conditional on.
