# In d=3 the Staggered Taste Space IS the Qubit — No Separate Koide Multiplicity (Narrow Obstruction)

**Date:** 2026-06-04
**Type:** no_go
**Claim type:** no_go (narrow, route-specific) — prunes the taste-breaking-normalization
route to the Koide r=1/2; the multi-factor route and the eta-phase mass-weighting residual
stay open.
**Claim scope:** in d=3 the `2^3` staggered taste matrices
`T(x) = sigma_1^{x1} sigma_2^{x2} sigma_3^{x3}` (`x in {0,1}^3`) **span `M_2(C)` = the
on-site qubit** (`Cl(3,0)`), a simple algebra with a unique 2-dimensional irreducible
carrier. So the staggered construction provides **no separate taste multiplicity** beyond
the qubit's own two dimensions. Hence the C3-doublet of the generation triplet keeps its
genuine real-dimension 2, the block-total Frobenius weighting stays `(singlet:doublet) =
(1,2)` (legacy F3, kappa = 1, r=1), and the taste-breaking normalization **cannot**
manufacture the `(1,1)` multiplicity weighting (legacy F1, kappa = 2) that `r = 1/2`
(Q=2/3) requires.
**actual_current_surface_status:** exact structural pruning of the taste-breaking route;
**conditional** on the open staggered-Dirac realization gate (the spatial-hypercube ->
Clifford map). Not retained on the current surface.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_staggered_taste_is_qubit_no_koide_multiplicity_exact.py`](./../scripts/audit_companion_staggered_taste_is_qubit_no_koide_multiplicity_exact.py)

## Context (Koide taste-multiplicity route pruning)

`r = 1/2` needs the `(1,1)` **multiplicity** weighting of the C3 singlet/doublet isotypes
(legacy F1, kappa=2), but the surfaced Gaussian/measure route gives the `(1,2)`
**real-dimension** weighting (legacy F3, kappa=1, r=1): the doublet has two real
dimensions and the Gaussian measure integrates over both
([Probe 25](KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md)
/
[Probe 29](KOIDE_BAE_PROBE_KAPPA_PREDICTION_TEST_PARTIAL_FALSIFICATION_NOTE_2026-05-09_probe29.md);
already on the surface). The remaining hope for this route was that the staggered **taste**
structure supplies a separate multiplicity that re-weights `(1,2) -> (1,1)`.
The
[fermion-determinant companion](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
pruned the determinant route; this note prunes the **taste-breaking** route.

## Statement

1. (**span**) The eight staggered taste matrices `T(x) = sigma_1^{x1} sigma_2^{x2}
   sigma_3^{x3}` are real-linearly independent (real rank 8) and therefore **span `M_2(C)`**
   — the one-qubit operator algebra named by the
   [Quantum axiom](MINIMAL_AXIOMS_2026-06-04.md), equivalently `Cl(3,0)` on the current
   repo baseline.
2. (**closure**) They close projectively, `T(x) T(y) = phase * T(x+y mod 2)` with
   `|phase| = 1`: a `Z_2^3` projective representation, i.e. a basis of the algebra, not an
   extra index space.
3. (**locked C3**) The axis-rotation `sigma_1 -> sigma_2 -> sigma_3` preserves
   `sigma_i sigma_j = i eps_ijk sigma_k`, so it is an automorphism of the taste algebra —
   and it is the **same** C3 that cycles the three hw=1 corners `(pi,0,0),(0,pi,0),(0,0,pi)`
   and hence the three generations. Taste-C3 and generation-C3 are locked.
4. (**no multiplicity**) `M_2(C)` is simple, with a unique 2-dimensional irreducible carrier
   and center = scalars only. So the staggered taste space carries **no multiplicity** beyond
   the qubit's two dimensions; there is no separate isotype-multiplicity index available to
   convert real-dim weighting `(1,2)` into multiplicity weighting `(1,1)`.
5. (**Koide consequence**) `Tr(M^H M) = 3a^2 + 6|b|^2` exactly, so the C3-doublet's genuine
   real-dimension 2 fixes the weighting at `(1,2)` (legacy F3, kappa = 1, r=1). The `(1,1)`
   multiplicity weighting (legacy F1, kappa = 2, r=1/2) would need the doublet weighted as
   one block — a relative factor of **2** the qubit cannot supply through this route.

All six checks pass exactly (sympy).

## Why this also explains the 2^{3/2} taste subtlety

The naive 3-D staggered taste count is `2^{3/2} ~ 2.83` (non-integer); the textbook 4-D count
`2^{4/2}=4` requires a Wick rotation `Z^3 -> Z^4` that is **not** derived from the
[Lattice + Quantum + Record baseline](MINIMAL_AXIOMS_2026-06-04.md) (flagged in
[the hierarchy-formula status note](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)).
This note resolves the puzzle
structurally: the `2^3 = 8` spatial-hypercube taste matrices collapse onto the **2-dimensional**
irreducible carrier of `M_2(C)` (the qubit). The gap between `2^{3/2}` and the actual carrier
dim 2 is exactly that collapse — there is no integer taste multiplicity in genuine d=3 because
the tastes are the qubit.

## Synthesis — the dynamical class is now down to one route

| route | result | status |
|---|---|---|
| free Gaussian measure on Herm_circ(3) | (1,2), legacy F3 -> kappa=1, r=1 | ruled out ([Probe 25](KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md)) |
| corner fermion determinant `det(M)` | shape-stationary at r=1, r=4 | ruled out ([determinant companion](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)) |
| Z3 scalar potential `V(Tr K)` | V_eff min != physical point | ruled out ([scalar-potential support note](KOIDE_Z3_SCALAR_POTENTIAL_SUPPORT_NOTE_2026-04-19.md)) |
| **taste-breaking normalization** | tastes span M_2(C), no extra multiplicity | **ruled out (this note)** |
| multi-factor Connes-Lott | needs a separate `H_L \oplus H_R` factor | **OPEN** |

Within this finite dynamical-class table, the first four routes deliver or preserve the `(1,2)`
real-dimension weighting (kappa=1). Reaching the empirical `(1,1)` multiplicity weighting
(kappa=2, r=1/2) through the clean single-qubit route would therefore require either a separate
algebra factor or an explicit multiplicity-counting admission
([Probe 25](KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md)
/
[Probe 29](KOIDE_BAE_PROBE_KAPPA_PREDICTION_TEST_PARTIAL_FALSIFICATION_NOTE_2026-05-09_probe29.md));
neither is supplied by the Lattice + Quantum + Record baseline. This sharpens Probe 29's
partial falsification without closing the separate-factor or eta-phase mass-weighting residuals.

## NO-GO DISCIPLINE GATE (N1-N8)

| # | Check | Result |
|---|---|---|
| N1 | >= 5 attack routes named | 5: free measure [RULED OUT, [Probe 25](KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md)]; fermion determinant [RULED OUT, [determinant companion](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)]; Z3 scalar potential [RULED OUT, [scalar-potential support note](KOIDE_Z3_SCALAR_POTENTIAL_SUPPORT_NOTE_2026-04-19.md)]; **taste-breaking normalization [RULED OUT, this note]**; multi-factor Connes-Lott [**OPEN**]. 4 ruled out, 1 open -> prune the taste-breaking route; not a universal no-go. |
| N2 | wall independence | The taste-span/`M_2(C)` fact is independent of the determinant and measure walls (it is an algebra-structure fact, not a measure or extremization fact). |
| N3 | hidden-wall scan | Sole admission explicit: CONDITIONAL on the [open staggered-Dirac gate](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md) (the spatial-hypercube -> Clifford map `T(x)`). The taste matrices are reproven from the one-qubit operator algebra; no "standard staggered"/"by construction" import as a proof input. |
| N4 | residual matching | Matches [Probe 25](KOIDE_BAE_PROBE_PHYSICAL_EXTREMIZATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe25.md) / [Probe 29](KOIDE_BAE_PROBE_KAPPA_PREDICTION_TEST_PARTIAL_FALSIFICATION_NOTE_2026-05-09_probe29.md) exactly: (1,2) real-dim weighting -> kappa=1; (1,1) multiplicity weighting "not derivable from cited dynamics" -> here shown the taste space provides no multiplicity to supply it. |
| N5 | rhetoric resolution | Scoped to "the 3D taste space is M_2(C), so no separate multiplicity"; not broadened to "no construction whatsoever can give r=1/2" (the separate-factor route is explicitly open). |
| N6 | partial-closure path | No labeling-convention path closes this algebra-dimension fact. A multiplicity-counting principle would require a retained derivation or an explicitly approved primitive; it is not silently supplied by the current foundation. |
| N7 | steelman | "The eta-phase SIGNS, integrated with the gated mass term, might weight the C3-isotypes unequally even though the taste *space* is the qubit." Valid as a residual: this note prunes the *multiplicity-space* mechanism (the taste space carries none), not a hypothetical phase-weighting that would still need the gated mass term — folded into the open gate, not claimed closed. |
| N8 | cross-cycle echo | Consistent with [Probe 29](KOIDE_BAE_PROBE_KAPPA_PREDICTION_TEST_PARTIAL_FALSIFICATION_NOTE_2026-05-09_probe29.md), the [r=1/2 dynamical-norm-balance no-go](KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md), and the [determinant companion](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md); the same real-dimension residue recurs, now traced to the algebra simplicity of M_2(C). |

**Verdict:** narrow route-pruning (taste-breaking route), embedded in the bounded
obstruction for the dynamical class. Residual: separate-factor route + the gated
eta-phase mass weighting.

## What this claims / does NOT claim

- Claims: in d=3 the staggered tastes span `M_2(C)` (exact); the qubit carries no separate
  multiplicity; so taste-breaking cannot supply the `(1,1)`/r=1/2 weighting via a multiplicity space.
- Does **not** claim a universal no-go: the multi-factor Connes-Lott route is open, and a
  hypothetical eta-phase mass weighting rides the open gate.
- Does **not** claim Q=2/3 is empirically wrong; it locates `r=1/2` as the irreducible
  multiplicity admission, not a clean single-qubit consequence.
- Conditional on the open staggered-Dirac realization gate.

## Trace gate

```yaml
trace_class: negative_route_pruning
target_blocker_text: "BAE admission |b|^2/a^2=1/2 (r=1/2) on the charged-lepton lane"
source_of_blocker_text: audit_ledger
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "test the separate-factor route (multi-factor Connes-Lott: Yukawa D on R^3, chirality on a separate H_L \\oplus H_R factor) and the eta-phase mass-weighting residual"
```

## Forbidden imports

- Literature (Kawamoto-Smit staggered tastes; the textbook `2^{d/2}` taste count) is a
  comparator only; the taste matrices `T(x)` and their algebra are reproven from the
  one-qubit operator algebra. No PDG values as derivation inputs.

## Cross-references

- [CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
  — the fermion-determinant route pruning.
- [KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md)
  — the isotype Frobenius split `Tr(M^H M) = 3a^2 + 6|b|^2` and the legacy F1/F3 weighting.
- [KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md](KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md)
  (#2591) — why r=1/2 must be dynamical.
- [HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
  — the `2^{3/2}` / Wick-rotation taste subtlety this note resolves structurally.
- [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  — the open spatial-hypercube-to-Clifford realization gate this route pruning is conditional on.
