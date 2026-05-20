# D=3 Retention Closure Plan (Phase 4 Work)

**Date:** 2026-05-20
**Status:** tracking note for the D=3 derivation lane closure work
**Type:** meta (plan / scheduling)

## Purpose

Track the work required to take the D=3 spatial-dimension derivation
chain from its current state (six `audited_conditional` rows; chain
does not close clean) to a `retained` (positive_theorem) closure that
would allow `MINIMAL_AXIOMS` A2 to be loosened from "`Z^3`" to "`Z^d`"
with `d=3` derived.

## Current state (2026-05-20 audit pass)

Six audit-conditional rows constitute the in-flight D=3 chain. A
first-pass independent audit returned `audited_conditional` on all
six with named gaps:

| Row | Gap |
|---|---|
| `dimension_selection_note` | Missing analytic bridge from d-dim Poisson + phase-coupling setup to force-sign observable; upper-bound dependency unaudited |
| `dimension_selection_upper_bound_textbook_import_note_2026-05-17` | External textbook imports (Bertrand 1873, Ehrenfest 1917, Tangherlini 1963), not framework-internal derivations |
| `anomaly_forces_time_theorem` | Four bridges not retained: ABJ inconsistency on lattice, matter completion, chirality grading, single-clock |
| `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | No-spatial-RP / no-second-clock uniqueness not closed |
| `lorentz_boost_covariance_3plus1d_theorem_note` | Finite-`a` Lorentz violation suppression, CPT/P/SME protection, Planck pin all imported |
| `a3_route2_single_clock_c3_obstruction_note_2026-05-08_r2` | Bridge "every time primitive commutes with U_C3" missing; no-go discipline incomplete |

## Closure plan

### Repairs that do not depend on open gates (this PR)

These can be done on the existing retained `dimensional_gravity_table`
+ Newton-derived + lattice-QM substrate, independent of the Grassmann
staggered-Dirac and `g_bare = 1` gates.

1. **`DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_NOTE_2026-05-20.md`**
   — supplies the analytic bridge from the d-dim Poisson equation
   plus the framework's phase-coupling rule to the force-sign
   observable, closing the bridge gap on
   `dimension_selection_note`.

2. **`BERTRAND_FRAMEWORK_INTERNAL_DERIVATION_NOTE_2026-05-20.md`**
   — derives the Bertrand-style stable-bounded-orbit upper bound
   `d ≤ 3` framework-internally from the retained
   `dimensional_gravity_table` (d-dim potential law) plus standard
   classical Hamiltonian-mechanics machinery. Replaces the
   external textbook import for the orbital half.

3. **`COULOMB_STABILITY_FRAMEWORK_INTERNAL_DERIVATION_NOTE_2026-05-20.md`**
   — derives the atomic-stability upper bound `d ≤ 4` (with `d = 3`
   the unique canonical-spectrum case) framework-internally from the
   d-dim Coulomb potential plus the framework's lattice quantum
   mechanics. Replaces the external textbook import for the atomic
   half.

4. **`SINGLE_CLOCK_UNIQUENESS_NOTE_2026-05-20.md`**
   — closes the no-spatial-RP / no-second-clock uniqueness gap on
   `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`
   by deriving both from retained framework primitives (microcausality,
   Lieb-Robinson, cluster decomposition, reflection positivity).

### Repairs that depend on open gates (deferred)

These rows can only fully close once one or both of the open gates
(Grassmann, `g_bare = 1`) close, because they touch matter content
and/or gauge dynamics.

5. **`anomaly_forces_time_theorem` four bridges** — ABJ inconsistency,
   matter completion, chirality grading, single-clock bridges. All
   four depend on the Grassmann staggered-Dirac gate closing (matter
   content) and partial dependence on `g_bare = 1`. Deferred to Phase
   4.5 (after Grassmann gate close).

6. **`lorentz_boost_covariance_3plus1d_theorem_note` repairs** —
   finite-`a` Lorentz violation, CPT/P/SME protection, Planck pin. All
   three depend on the gauge structure from `g_bare = 1` gate close.
   Deferred to Phase 4.5.

7. **`a3_route2_single_clock_c3_obstruction_note_2026-05-08_r2`
   commutation bridge** — specific algebraic bridge "all listed time
   primitives commute with `U_C3`". Closeable independent of gates
   in principle, but not in this PR; queued as a follow-up.

### Dependency graph for closure

```
                          ┌─ BERTRAND_FRAMEWORK_INTERNAL ─┐
                          │  (this PR)                    │
        dimensional_      │                                ├─→ DIMENSION_SELECTION
        gravity_table  ───┤                                │   UPPER_BOUND
        (retained_bounded)│                                │   (replaces textbook
                          └─ COULOMB_STABILITY_           ─┘    imports)
                             FRAMEWORK_INTERNAL
                             (this PR)
                                                            ↓
                          DIMENSION_SELECTION_LOWER_   ┐
                          BOUND_BRIDGE (this PR)       │
                                                        ├─→ dimension_selection_note
                          (existing runner +            │   (lower bound, clean)
                           dimensional_gravity_table)   ┘
                                                            ↓
                                           DIMENSION_SELECTION
                                           combined: d = 3 unique
                                                            ↓
                                           (still depends on
                                            single_clock_uniqueness
                                            for d_t = 1)
                                                            ↓
                          SINGLE_CLOCK_UNIQUENESS (this PR)
                          + anomaly_forces_time bridges (deferred)
                          + Lorentz repairs (deferred)
                          + a3_route2 commutation (deferred)
                                                            ↓
                                           FULL D=3+1 CHAIN
                                           (retained, conditional
                                            on the deferred pieces)
```

## Target end state

If all four notes in this PR retain `audited_clean`:

- `dimension_selection_note` lower-bound bridge: closed
- `dimension_selection_upper_bound_textbook_import_note_2026-05-17`:
  superseded by the two framework-internal derivations
- `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`:
  uniqueness gap closed
- Lower bound `d ≥ 3` + upper bound `d ≤ 3` retain via framework-internal
  arguments

Remaining conditional rows (anomaly-forces-time, Lorentz, A3 route 2)
become the only blockers to full chain retention. Each is gate-dependent.

If those eventually close, then `Z^3` → `Z^d` in A2 with `d = 3` as
a retained downstream theorem becomes available. Until then, `Z^3`
stays in the axiom per framework discipline.

## What this file is not

- Not a derivation; it is a scheduling note.
- Not a unilateral audit re-grade; verdicts on individual rows are set
  by the independent audit lane.
- Not a closure of any row by itself; the four new notes in this PR
  carry the load-bearing content.

## Citation-graph note

This note has no upstream load-bearing dependencies. References to the
six audit-conditional rows and the new derivation notes are pointers
for tracking, not load-bearing deps.
