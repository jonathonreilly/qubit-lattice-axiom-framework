# No Sector-Independent Value of `r` Agrees With the Registered Dials, Subject to Three Named Walls (Bounded Theorem)

**Date:** 2026-08-07
**Type:** bounded_theorem
**Claim type:** bounded_theorem (with named walls)
**Status:** proposed_retained
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit outcome, and edits no registry.
**Primary runner:**
[`scripts/frontier_sector_independent_dial_exclusion_bounded_2026_08_07.py`](../scripts/frontier_sector_independent_dial_exclusion_bounded_2026_08_07.py)
**Cached runner output:**
[`logs/runner-cache/frontier_sector_independent_dial_exclusion_bounded_2026_08_07.txt`](../logs/runner-cache/frontier_sector_independent_dial_exclusion_bounded_2026_08_07.txt)

## This is not a no_go

It was drafted as one — "no sector-blind supply of the occupancy grain is
admissible" — and it failed the `/no-go-gate` N1–N8 stress test at N1, N5 and
N7. Two attack routes against it are open, and a hostile reviewer can write a
convincing steelman using either. Per the gate's own instruction, the claim is
demoted rather than shipped in its original framing.

What ships is the narrow, honest version: a **bounded exclusion of one named
class of candidate supplies, with three walls stated as load-bearing
conditions rather than as caveats.** The full N1–N8 checklist is in the PR
body.

## Claim

Let a *candidate sector-independent supply* be any axiom, primitive, or
theorem whose output is **one numerical value** `r*` of the C₃ dial
coordinate, the same for every fermion sector.

**T1 (exact).** No such `r*` exists within 5σ of all three registered
common-scale dials. The three 5σ intervals are pairwise disjoint and their
triple intersection is empty. The best possible single value — the `r*`
minimising the largest pull over the three sectors — still sits **149.5σ**
from at least one sector, because the charged-lepton dial is pinned to
`1.0 × 10⁻⁵`.

Registered inputs (comparators, frozen as exact rationals in the runner):

```text
charged lepton   r = 0.499990767 ± 0.0000102     (0.9σ from exactly 1/2)
down-type quark  r = 0.621090   ± 0.007335
up-type quark    r = 0.830971   ± 0.002204
```

**T2 (exact, but conditional on wall W3).** Uniform occupancy over `n` counted
atoms has singlet weight `w = 1/n`, hence `r = (n−1)/2` — the ladder
`{0, 1/2, 1, 3/2, …}`. The charged-lepton dial sits **on** the `n = 2` rung
(0.9σ). Both quark dials sit **strictly between** rungs: down-type is 16.5σ
from its nearest rung, up-type 76.7σ. So no uniform count of atoms, of any
`n`, reaches either quark sector.

## The three walls

These are load-bearing conditions, not caveats. Any one of them failing voids
the corresponding part of the claim.

**W1 — carrier universality.** T1 compares three dials as if they were the
same observable evaluated on three sectors. That all three sectors register
the *same* C₃ `hw=1` carrier is **not derived**.
[`SPECIES_BRIDGE_MINIMUM_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-13.md`](SPECIES_BRIDGE_MINIMUM_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-13.md)
derives the carrier *structure* for the `hw=1` triplet but explicitly excludes
"a claim about across-fermion-type alignment," and lists that alignment as an
open residual. If the quark sectors do not carry the same C₃ object, `r` is
not one observable across sectors and T1 compares unlike things.

**W2 — registration scale.** The companion invariance theorem
([`SECTOR_DIAL_SCALE_INVARIANCE_AND_COMMON_SCALE_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-08-07.md`](SECTOR_DIAL_SCALE_INVARIANCE_AND_COMMON_SCALE_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-08-07.md),
in flight, unaudited) makes the dial scale-independent **under
flavour-universal QCD running only**. Standard-Model Yukawa contributions to
the mass anomalous dimension are flavour-*dependent*. So a dial supplied at
some other scale — a lattice or unification scale — need not equal the
registered one, and T1 would then be excluding a value the framework never
claimed. T1 holds only if the supplied `r` is the registered `r`.

**W3 — energy dictionary (T2 only).** T2's weight-to-dial coordinate
`r = (1 − w)/(2w)` is prior art
([`ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md`](ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md),
T3) but that note states the coordinate is "supplied only through the
relocation theorem's explicitly unadopted energy dictionary (Residual Atom
2)." T2 therefore consumes an **unadopted** dictionary. **T1 does not depend
on W3** and stands if T2 falls.

W1, W2 and W3 are pairwise independent: closing any one closes neither other.

## What the exclusion does not reach

The excluded class is candidate supplies yielding one sector-independent
**numerical value**. It is *not* a claim about sector-blind **rules**.

A universal rule whose input is sector-dependent registered content is
untouched, and the runner gives the two-line existence proof: inverting
`r = (1 − w)/(2w)` on each sector's registered dial reproduces all three from
one rule and three inputs. Admissibility — the axiom whose content is that the
one-site distribution varies with the nearest-neighbour conditions — is
exactly a rule of that shape. Nothing here bears against it.

This narrowing came out of the gate's N5 rhetoric audit and is load-bearing on
the claim's wording. The broader phrase "no sector-blind supply" was tested
only at the resolution of *values* and is over-broad at the resolution of
*rules*; it does not appear in this note.

## Relation to the standing non-supply no-go

[`ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md`](ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md)
shows the axiom surface does not *entail* a determinant-power grain. That is a
non-entailment result about what the axioms settle.

This note is **not** a witness for it and does not cite it as one: the
residuals differ. That note's residual is "the axioms do not select between
`F_C` and `F_R`"; this note's is "no single numerical `r` fits three
registered sectors." The two are complementary — the first says the axioms are
silent, the second constrains what a future theorem could say — and neither
supports the other. The gate's N4 residual-matching step is why this is spelled
out rather than assumed.

That no-go explicitly leaves open "a future physical CAR/action theorem that
derives a specific Gaussian measure." T1 adds a condition to that opening: any
such theorem must yield a sector-dependent answer, or fail W1 or W2.

## Non-claims

- **This is not a no_go**, does not assert that any route is structurally
  closed, and does not claim a new axiom is required. It excludes one named
  class of candidate supplies subject to three named walls.
- No `r`, `Q`, `δ`, mass, mass scale, mixing angle, probability rule, Born
  weight, species map, or sector weight is derived. Every number in T1 and T2
  is an external comparator.
- The registered dial values are consumed from a companion note that is
  **in flight and unaudited**. If those comparators move, T1 must be re-run.
- No claim is made about *why* the sectors differ, or that Admissibility
  supplies the difference.
- No axiom, approved primitive, registry entry, or audit verdict is added,
  edited, retired, or predicted. The primitive registry check was run: the
  three approved primitives (`scale_reference`, `kinetic_isotropy`,
  `realized_state`) are each declared not to supply any dimensionless
  quantity, weighting rule, or probability rule, so no wall language of the
  form "no retained primitive supplies this" is used here. The Tier-A count is
  unchanged.

## Scope boundary

Three-generation fermion sectors of the Standard Model as registered.
Real-valued dials. Gaussian, symmetric, linearly-propagated input
uncertainties as published by the companion note; `K = 5σ` intervals. The
exactness claim is downstream of the comparator declaration: the interval
construction, disjointness, intersection emptiness, and ladder distances are
all exact `Fraction` arithmetic, and the frozen input rationals are the only
external numbers.

## Reproduce

```bash
python3 scripts/frontier_sector_independent_dial_exclusion_bounded_2026_08_07.py
```

Standard library only. No floating point and no randomness after the comparator
input declaration.
