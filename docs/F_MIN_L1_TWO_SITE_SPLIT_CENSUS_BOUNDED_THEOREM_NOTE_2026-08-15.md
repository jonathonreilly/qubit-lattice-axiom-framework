---
claim_id: f_min_l1_two_site_split_census_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 66 two-site seeds on the two-cube with off-patch o=0, 4 distinguish f_min from f_L1 by fill or lock history. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_min_l1_two_site_split_census_2026_08_15.py
---

# Two-Site Split Census Of `f_min` Versus `f_L1`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exhaustive lock-step census of the 66 unordered two-site seeds on
the twelve-vertex two-cube `{0,1,2} × {0,1} × {0,1}` with off-patch occupancy
`o=0`. The integer `N_split` is displayed. No seed is adopted and no selector
is written into Admissibility.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_min_l1_two_site_split_census_2026_08_15.py`](../scripts/f_min_l1_two_site_split_census_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

On the two-cube, a lock-step run of a displayed readiness map from a seed `S`
is the synchronous wave process that begins with `S` locked and, at each tick,
locks every still-unlocked site whose six-neighbor occupancy 3-tuple satisfies
the map. The lock-history tuple is the sequence of lock counts after the seed
and after each nonempty wave, until halt. Fill means `|locks_halt| = 12`.

Write `n_unbalanced`, `n_both`, and `n_empty` for the number of cubic axes
whose two opposite neighbors are occupied on exactly one side, on both sides,
or on neither side. Off-patch neighbors contribute occupancy `0`. Then

- `f_L1` fires iff `n_unbalanced ≠ 0` (some axis is unbalanced; not Hamming
  weight of the six occupancy bits);
- `f_min` fires iff the occupancy is nonempty and `n_both = 0`
  (equivalently `n_unbalanced ≠ 0` and `n_both = 0`).

A two-site seed *splits* the two maps when the fill bits differ or the
lock-history tuples differ.

The census of all `C(12,2) = 66` unordered pairs is

`N_split = 4`

`N_fill_L1 = 62`

`N_fill_min = 58`

`N_fill_both = 58`

Every split is the same displayed pattern: `f_L1` fills with history
`(2, 8, 12)` and `f_min` halts unfilled at `(2, 8, 10)`. The four seeds are
exactly the displacement-`(2,1,1)` pairs

`{(0,0,0),(2,1,1)}`, `{(0,0,1),(2,1,0)}`, `{(0,1,0),(2,0,1)}`,
`{(0,1,1),(2,0,0)}`.

The face-diagonal seed `{(0,0,0),(1,1,0)}` does not split: both maps fill with
history `(2, 7, 11, 12)`. These four integers and four seeds are displayed
census output. They are not adopted as a physical selector.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 66 two-site seeds, both lock-step runs, and the four census integers are finite exact statements on a declared twelve-site patch; no seed is selected and no Admissibility clause is added."
trace_class: frontier_discovery
target_claim_id: f_min_l1_two_site_split_census
target_blocker_text: "how many two-site seeds on the two-cube distinguish f_min from f_L1 by fill or lock history"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the twelve-vertex two-cube with off-patch occupancy 0 and the two displayed readiness maps; no selector is adopted"
hypothetical_axiom_status: "none; f_min and the four splitting seeds are displayed and are not proposed as axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded census; do not write a selector into Admissibility"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** Lattice, Admissibility, and Record are quoted from
  the live axiom memo without rewrite. They identify the cubic nearest-neighbor
  graph, the local-condition domain, and the lock/content/absence wording.
  They do not supply the two readiness maps or the two-cube patch.
- **Explicit theorem-domain condition:** the twelve sites
  `{0,1,2} × {0,1} × {0,1}`, off-patch occupancy identically `0`, the two
  displayed maps `f_L1` and `f_min`, and the synchronous lock-step dynamics
  above are supplied mathematical data for this census.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing either map, or any of the four splitting
  seeds, into Admissibility remains a separate, open obligation. This note
  does not adopt them.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The current Record boundary is:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility

does not supply the formation site, probability, or rate.

The two readiness maps are displayed occupancy predicates on the six-neighbor
condition tuple. They are not Admissibility content. Using a lock-step wave as
physical Record formation would require a separately derived formation
mechanism; that mechanism is not supplied here.

## Exact Objects

The two-cube is the twelve-point set

`V = {0,1,2} × {0,1} × {0,1} ⊂ Z^3`.

The open nearest-neighbor set of a site `x` is
`N(x) = {x ± e_1, x ± e_2, x ± e_3}`. A neighbor in `V` that is already
locked contributes occupancy `1`; a neighbor outside `V` contributes
occupancy `0`. For each of the three axes one records the pair
`(c_{+μ}, c_{-μ}) ∈ {0,1}^2` and tallies

- unbalanced if the pair is `(1,0)` or `(0,1)`,
- both if the pair is `(1,1)`,
- empty if the pair is `(0,0)`.

On this patch, `n_both > 0` is possible only at the middle face `x = 1`, and
only on the long axis: every transverse neighbor in the `-y` or `-z` direction
from `y = 0` or `z = 0` is off-patch.

A seed is an unordered pair `S ⊂ V` with `|S| = 2`. There are exactly
`C(12,2) = 66` such seeds. The run of a map `f` from `S` begins with
`locks_0 = S`. At tick `t ≥ 1` every unlocked `x ∈ V` with `f(c(x, locks_{t-1})) = 1`
locks simultaneously. The history is
`(|locks_0|, |locks_1|, …, |locks_T|)` at the first `T` with no further ready
site. Fill is the boolean `|locks_T| = 12`.

`f_L1(c) = 1` iff `n_unbalanced ≠ 0`. This is not the Hamming weight of the
six occupancy bits: the opposite-pair occupancy at `(1,0,0)` with
`{(0,0,0),(2,0,0)}` locked has Hamming weight `2` and
`(n_unbalanced, n_both, n_empty) = (0,1,2)`, so `f_L1` does not fire.

`f_min(c) = 1` iff `n_both = 0` and `n_unbalanced ≠ 0`. The maps therefore
disagree exactly when at least one axis is unbalanced and at least one axis
is doubly occupied. On this patch that first occurs as mixed type `(1,1,1)`
at a middle-face site.

## Theorem 1 — Two Displayed Seeds

**Face-diagonal non-split.** From `S_face = {(0,0,0),(1,1,0)}` both maps
produce the lock-history `(2, 7, 11, 12)` and fill. The first wave locks
`(1,0,0)`, `(0,1,0)`, `(0,0,1)`, `(1,1,1)`, and `(2,1,0)`; the second wave
locks the remaining four sites except `(2,0,1)`; the third wave locks
`(2,0,1)`. Every ready neighborhood in this run has `n_both = 0`, so the two
predicates agree at every unlocked site.

**Distinguisher split.** From `S_* = {(0,0,0),(2,1,1)}` the first wave is
common and reaches eight locks. At the second wave, the four remaining sites
include two mixed-type middle-face neighborhoods
`(1,1,0)` and `(1,0,1)`, each with `n_both = 1` and `n_unbalanced = 2`.
`f_L1` locks all four remaining sites and fills with history `(2, 8, 12)`.
`f_min` locks only `(0,1,1)` and `(2,0,0)` and then halts at ten locks with
history `(2, 8, 10)`. The fill bits and the histories both differ, so `S_*`
splits.

## Theorem 2 — Exhaustive Two-Site Census

Every one of the 66 seeds is run independently under both maps. The four
census integers are

`N_split = 4`,
`N_fill_L1 = 62`,
`N_fill_min = 58`,
`N_fill_both = 58`.

The complementary counts are displayed, not selected: four seeds fail to fill
under `f_L1`, eight fail under `f_min`, and `N_fill_min = N_fill_both`, so
every `f_min`-filling seed also fills under `f_L1`. No history-only split
occurs: whenever the histories differ, the fill bits differ, and conversely.

Partitioning the 66 pairs by coordinate displacement
`(|Δx|, |Δy|, |Δz|)` isolates the split:

| displacement | count | `f_L1` fill | `f_min` fill | common history | split |
|---|---:|---:|---:|---|---|
| `(1,0,0)`, `(1,0,1)`, `(1,1,0)` | 24 | 24 | 24 | `(2, 7, 11, 12)` | no |
| `(1,1,1)` | 8 | 8 | 8 | `(2, 9, 12)` | no |
| `(0,*,*)` (same `x` face) | 18 | 18 | 18 | `(2, 6, 10, 12)` or `(2, 8, 12)` | no |
| `(2,0,1)`, `(2,1,0)` | 8 | 8 | 8 | `(2, 8, 12)` | no |
| `(2,0,0)` | 4 | 0 | 0 | `(2, 6, 8)` | no |
| `(2,1,1)` | 4 | 4 | 0 | L1 `(2, 8, 12)`; min `(2, 8, 10)` | yes |

The four non-filling long-axis pairs
`{(0,y,z),(2,y,z)}` halt at eight locks under both maps. They are not
splits. The four displacement-`(2,1,1)` pairs are exactly the splits.

## Theorem 3 — Display, Do Not Adopt

The integer `N_split = 4` is the object of the census. The four seeds and
the three fill counts are reported with it. They are displayed, not adopted:
do not adopt a seed, and do not adopt either map. A selector is not written
into Admissibility. A later derivation that used one of these seeds as a
physical rule would be a different claim.

## What This Does Not Claim

- It does not claim that either map is the Admissibility rule.
- It does not claim that lock-step waves are physical Record formation.
- It does not claim a unique physically preferred two-site seed.
- It does not extend the census to `|S| ≠ 2` or to a larger patch.
- It does not identify `f_min` with Hamming weight, graph distance, or any
  map other than nonempty `n_both = 0`.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the two-site split-count question for the two displayed maps on the declared patch. |
| V2 | Current main has the axiom memo and no landed exhaustive two-site split census of these two maps. |
| V3 | All 66 pairs, both runs, and the four integers are independently finite and exact. |
| V4 | The census is more than a restatement of the single distinguisher `{(0,0,0),(2,1,1)}`: it counts every two-site seed. |
| V5 | It is not a physical compiler and writes no selector into Admissibility. |

## No-Go Discipline Gate

The negative content is narrow: most two-site seeds do not split these two
maps, and the four that do are not hereby adopted. No global compiler
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| face-diagonal 2-site seed | run both maps from `{(0,0,0),(1,1,0)}` | no split; both fill with `(2, 7, 11, 12)` |
| displacement `(2,1,1)` | run both maps from each of the four pairs | all four split by fill and history |
| long-axis `(2,0,0)` | run both maps from `{(0,y,z),(2,y,z)}` | neither fills; same history; not a split |
| Hamming-weight predicate | fire on six-bit weight | executed counterexample: opp2 has weight 2 and `f_L1 = 0` |
| adopt a seed | write one splitter into Admissibility | refused; displayed, not adopted |
| larger seed census | enumerate `|S| ≠ 2` | live different object |

### N2 — wall independence

The missing formation mechanism, the missing Admissibility selector, and any
extension off this twelve-site patch are distinct premises. This note claims
no complete wall collection.

### N3 — hidden-condition scan

The two-cube, off-patch occupancy `0`, the two predicates, and the
synchronous wave rule are declared. Hamming weight is not silently used.
No seed is treated as axiom content.

### N4 — source residual matching

The current axiom memo supplies the cubic nearest-neighbor substrate, the
local-condition sentence, and the lock/content/absence wording used here.
It does not supply `f_min`, `f_L1`, or a two-site selector. The residual
matches those sources.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 66 pairs, two maps, lock-count histories | no continuum or larger-patch census |
| per site | six-neighbor occupancy 3-tuples | no derived kernel values |
| per mode | no mode calculation | no spectral statement |
| per block | two-cube lock-step dynamics | no physical formation compiler |
| lattice wide | checked and not executed | no infinite-volume claim |

### N6 — live partial-closure paths

Live routes are an independently derived formation mechanism, a derivation
that would force one of the two maps, and any census at a different seed
cardinality or patch. Those routes remain open.

### N7 — hostile steelman

**Steelman:** Because `f_min` and `f_L1` already disagree on mixed-type
neighborhoods, almost every two-site seed should split.

**Answer:** On this patch, mixed type occurs only at `x = 1` and only after
both long-axis neighbors are locked. Fifty-eight of the 66 two-site seeds
never present such a neighborhood before fill, so the runs agree. Only the
four displacement-`(2,1,1)` seeds produce a mixed-type second wave.

### N8 — cross-cycle echo

A prior displayed computation isolated one distinguishing seed of size at
most three. This note does not recycle that single-seed existence claim as
the census. It enumerates every two-site seed and reports `N_split = 4`.

**Gate disposition:** PASS for the 66-seed census and the four displayed
integers above. FAIL / DO NOT SHIP for “Admissibility is `f_min`,” “adopt
this seed,” or “the maps agree on every finite seed.”

## Primary Runner

The primary runner recomputes both displayed seeds, enumerates all 66 pairs,
checks that `f_L1` is `n_unbalanced ≠ 0` rather than Hamming weight, checks
that `f_min` is nonempty `n_both = 0`, and checks that this note displays
`N_split = 4` without adopting a selector. It authors no audit verdict.
