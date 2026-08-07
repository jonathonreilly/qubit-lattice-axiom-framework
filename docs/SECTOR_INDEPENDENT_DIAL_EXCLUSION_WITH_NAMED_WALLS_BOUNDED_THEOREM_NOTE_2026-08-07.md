# No Sector-Independent Value of `r` Agrees With the Common-Scale Dial Comparators, Subject to Four Named Walls (Bounded Theorem)

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

> **Unlanded dependency — read before anything else.** Every number in T1 and
> T2 is consumed from
> `SECTOR_DIAL_SCALE_INVARIANCE_AND_COMMON_SCALE_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-08-07.md`,
> which is **in flight and unaudited** and is **not present in this repository
> yet**. The link to it below **does not resolve on this branch**, so the
> citation graph cannot seed that edge and the comparators cannot be checked
> against their source here. This note must not be landed or audited before that
> companion note lands. If its comparators move, T1 and T2 must be re-run.

## This is not a no_go

It was drafted as one — "no sector-blind supply of the occupancy grain is
admissible" — and it failed the `/no-go-gate` N1–N8 stress test at N1, N5 and
N7. Two attack routes against it are open, and a hostile reviewer can write a
convincing steelman using either. Per the gate's own instruction, the claim is
demoted rather than shipped in its original framing.

What ships is the narrow, honest version: a **bounded exclusion of one named
class of candidate supplies, with four walls stated as load-bearing
conditions rather than as caveats.** The full N1–N8 checklist is in the PR
body.

A fourth wall (W4) and the prior-art section below were added in review; the
PR body's N1 route table and its "three walls" count predate them.

## Claim

Let a *candidate sector-independent supply* be any axiom, primitive, or
theorem whose output is **one numerical value** `r*` of the C₃ dial
coordinate, the same for every fermion sector.

**T1 (exact).** No such `r*` exists within 5σ of all three common-scale dial
comparators. The three 5σ intervals are pairwise disjoint and their triple
intersection is empty. The **exact** minimax — the `r*` minimising the largest
pull over the three sectors, computed by envelope-breakpoint enumeration, not
by a grid scan — still sits **149.4807σ** from at least one sector. So T1 does
not depend on the choice of `K`: it holds for every `K < 149.48`.

Two honesty notes on that σ figure. It is large mainly because the
charged-lepton dial is pinned to `1.0 × 10⁻⁵`, three orders of magnitude
tighter than the quark dials; the *physical* separation at the minimax is
`Δr ≈ 0.33`, not something 149 times any physical width. And a σ-distance is
only as good as the σ — see "Robustness" below.

Comparator inputs (frozen as exact rationals in the runner):

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

## The four walls

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
2)." That quote is verbatim and in context. The same note also labels its T3
"support-only arithmetic, not a bijection of physical grains," and is itself an
unaudited `bounded_theorem`. T2 therefore consumes an **unadopted, support-only**
dictionary. **T1 does not depend on W3** — but see W4 before reading that as
"T1 is dictionary-free."

**W4 — mass-to-dial dictionary (T1 and T2).** The comparators are not measured
values of `r`. They are computed from PDG masses through the C₃-circulant
(Brannen) ansatz `H = aI + bC + b̄C²` together with the identification of its
eigenvalues as one-leg amplitudes `√m` rather than masses.
[`QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md`](QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md)
records both as **non-retained inputs** — the Frobenius/equal-block-energy
selection and the one-leg-amplitude reading of the eigenvalues — and
[`KOIDE_BAE_PROBE_HW_SECTOR_IDENTIFICATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe27.md`](KOIDE_BAE_PROBE_HW_SECTOR_IDENTIFICATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe27.md)
treats the circulant ansatz as an ansatz, not retained content. If that
dictionary is not the framework's, T1 excludes values of a quantity the
framework never computes.

W4 matters for how W3 is read. T1 escaping W3 does **not** make T1 free of
dictionary dependence — it means T1 rides a *different* non-retained dictionary
of the same kind. The earlier framing "T1 stands if T2 falls" is true only in
the narrow sense that T1 does not use the weight-to-dial coordinate.

W1, W2, W3 and W4 are pairwise independent: closing any one closes no other.

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

## Prior art — what is actually new here

T1's *qualitative* content is already in the repo. This note does not claim it
as new.

- [`FOURTH_AXIOM_RG_SCALE_DYNAMICS_SCOPING_2026-06-05.md`](FOURTH_AXIOM_RG_SCALE_DYNAMICS_SCOPING_2026-06-05.md)
  §2.1 already states it and already does the minimax in absolute units: "The
  best single universal value (mid-range `r* = 0.637`) still misses a sector by
  `0.137`… a single scale-invariant fixed point gives one number and is
  falsified by the quark sectors." Its §5 already states T1's forward
  constraint: the distinct sector values "argue that whatever selects `r` is
  sector-structured by a non-color label — a constraint on any future selection
  principle, scale-based or otherwise." That note is `Type: meta`, explicitly
  historical/provenance banking and a **non-claim source**, so the content is
  present in the repo but not as a claim.
- [`FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md`](FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md)
  states the `r* = 1/2` special case: a universal selector "would weight-leak to
  a universal Koide `Q = 2/3` and miss the registered quark comparators."
- [`FLAVOR_GAUGE_REPRESENTATION_CHANNEL_CANNOT_SOURCE_THE_SECTOR_R_SPREAD_NARROW_NO_GO_NOTE_2026-06-15.md`](FLAVOR_GAUGE_REPRESENTATION_CHANNEL_CANNOT_SOURCE_THE_SECTOR_R_SPREAD_NARROW_NO_GO_NOTE_2026-06-15.md)
  uses the same non-coincidence (`r_up ≠ r_down` at equal colour) as its
  load-bearing step.

**What is new is only the quantification, and it is narrow:** exact 5σ interval
arithmetic instead of a bare distance, an exact minimax instead of a midpoint,
the statement that the result is `K`-independent below 149.48σ, and the use of
the common-scale comparators rather than mixed-scale ones. A reader should size
this note as *putting error bars on an already-recorded observation*, not as
establishing the observation.

## The comparators moved, and in the direction that helps

The prior-art notes above register the down-type and up-type dials as
`r ≈ 0.597` and `r ≈ 0.773`–`0.774`. This note uses `0.621090` and `0.830971`.
That is not a re-selection of friendlier numbers: the older values mix mass
conventions (light quarks quoted at 2 GeV, `m_b` at `m_b`, `m_t` at `m_t`), and
the companion note removes the mixing by bringing each sector to one scale.
The Koide ratio `Q = Σm / (Σ√m)²` is homogeneous of degree zero, so a *common*
rescaling of a sector's three masses cannot move the dial at all; the entire
shift is therefore the mixed-convention artifact, and nothing in it is physics.
This is the mass-scheme/mixed-convention route in the PR body's alternative-route
table.

It must be said plainly that the corrected comparators sit **further apart**
than the ones they replace, which makes T1 stronger than it would have been on
the previously registered values. On the old values T1 still holds, but with
less margin. Until the companion note lands, four landed notes continue to
carry `0.597` / `0.773`; reconciling them is downstream work this note does not
do and does not claim to have done.

## Robustness — the uncertainties are symmetrised, and that needs a number

The 5σ intervals use symmetric, Gaussian, linearly-propagated uncertainties.
Several PDG inputs behind them (`m_u`, `m_d`, `m_s`) have strongly asymmetric
published errors, so symmetrisation is a real modelling choice and could
flatter the result. The runner therefore reports the exact factor by which the
quoted σ would have to grow before each conclusion fails:

```text
charged lepton / down-type   disjoint up to  sigma x 3.30
charged lepton / up-type     disjoint up to  sigma x 29.90
down-type / up-type          disjoint up to  sigma x 4.40
down-type off-rung (T2)      holds    up to  sigma x 3.30
up-type   off-rung (T2)      holds    up to  sigma x 15.34
```

The binding case is the down-type sector, at **3.3×**. Published asymmetries on
`m_d` and `m_s` are at the tens-of-percent level between the two arms, so the
worst-arm σ is well under 3.3× the symmetrised σ, and the down-type conclusion
survives. But the margin is 3.3×, not a hundred-fold, so the symmetrisation is
a stated condition of T1 and T2 rather than a harmless convenience. A reader
who rejects the symmetrisation should re-run with an asymmetric propagation
before relying on the down-type numbers; the σ-counts (16.5σ, 149.48σ) would
move, though the sign of the conclusion would not.

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
  class of candidate supplies subject to four named walls.
- No `r`, `Q`, `δ`, mass, mass scale, mixing angle, probability rule, Born
  weight, species map, or sector weight is derived. Every number in T1 and T2
  is an external comparator.
- The dial values are consumed from a companion note that is **in flight,
  unaudited, and absent from this branch**; its link here does not resolve. See
  the banner at the top.
- **The observation is not new.** T1 quantifies a fact already recorded in the
  repo (see "Prior art"). Only the error bars, the exact minimax, the
  `K`-independence, and the common-scale comparators are new.
- T1 is not dictionary-free. It escapes W3 and rides W4.
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

Three-generation charged fermion sectors of the Standard Model as registered
(neutrinos carry no registered dial and are out of scope). Real-valued dials.
Gaussian, symmetric, linearly-propagated input uncertainties as published by
the companion note; `K = 5σ` intervals, with T1 shown `K`-independent below
149.48σ. The comparators are mass-derived through the non-retained dictionary
named in W4.

The exactness claim is downstream of the comparator declaration: the interval
construction, disjointness, intersection emptiness, the minimax, the σ-inflation
break-even factors, and the ladder distances are all exact `Fraction`
arithmetic, and the frozen input rationals are the only external numbers. No
float reaches any load-bearing comparison; floats appear only inside `print`
formatting.

## Reproduce

```bash
python3 scripts/frontier_sector_independent_dial_exclusion_bounded_2026_08_07.py
```

Standard library only. No floating point and no randomness after the comparator
input declaration.
