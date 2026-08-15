---
claim_id: f_min_l1_three_site_split_census_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 220 three-site seeds on the two-cube with off-patch o=0, 60 distinguish f_min from f_L1 by fill or lock history. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_min_l1_three_site_split_census_2026_08_15.py
---

# Three-Site Split Census Of `f_min` Versus `f_L1`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exhaustive lock-step census of the 220 unordered three-site seeds on
the twelve-vertex two-cube `{0,1,2} × {0,1} × {0,1}` with off-patch occupancy
`o=0`. The integer `N_split3` is displayed. No seed is adopted and no selector
is written into Admissibility.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_min_l1_three_site_split_census_2026_08_15.py`](../scripts/f_min_l1_three_site_split_census_2026_08_15.py)
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

A three-site seed *splits* the two maps when the fill bits differ or the
lock-history tuples differ.

The census of all `C(12,3) = 220` unordered triples is

`N_split3 = 60`

`N_fill_L1_3 = 220`

`N_fill_min_3 = 160`

Every three-site seed fills under `f_L1`. The sixty splits are exactly the
sixty seeds that halt unfilled under `f_min`. No history-only split occurs:
whenever the histories differ, the fill bits differ, and conversely. The
long-axis line seed `{(0,0,0),(1,0,0),(2,0,0)}` does not split: both maps fill
with history `(3, 9, 12)`. These integers are displayed census output. They
are not adopted as a physical selector.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 220 three-site seeds, both lock-step runs, and the three census integers are finite exact statements on a declared twelve-site patch; no seed is selected and no Admissibility clause is added."
trace_class: frontier_discovery
target_claim_id: f_min_l1_three_site_split_census
target_blocker_text: "how many three-site seeds on the two-cube distinguish f_min from f_L1 by fill or lock history"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the twelve-vertex two-cube with off-patch occupancy 0 and the two displayed readiness maps; no selector is adopted"
hypothetical_axiom_status: "none; f_min and the sixty splitting seeds are displayed and are not proposed as axiom content"
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
- **Open physical bridge:** writing either map, or any of the sixty splitting
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

A seed is an unordered triple `S ⊂ V` with `|S| = 3`. There are exactly
`C(12,3) = 220` such seeds. The run of a map `f` from `S` begins with
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

## Theorem 1 — Line Seed Does Not Split

From the long-axis line `S_line = {(0,0,0),(1,0,0),(2,0,0)}` both maps
produce the lock-history `(3, 9, 12)` and fill. The first wave locks the
remaining three sites of the `y = 0` face together with the three sites of
the `z = 0` face that are not already locked, reaching nine locks. The
second wave locks the last three sites. Every ready neighborhood in this
run has `n_both = 0`, so the two predicates agree at every unlocked site.
The line seed is therefore not a split.

## Theorem 2 — Exhaustive Three-Site Census

Every one of the 220 seeds is run independently under both maps. The three
census integers are

`N_split3 = 60`,
`N_fill_L1_3 = 220`,
`N_fill_min_3 = 160`.

The complementary counts are displayed, not selected: no three-site seed
fails to fill under `f_L1`, sixty fail under `f_min`, and those sixty are
exactly the splits. One explicit splitter is
`{(0,0,0),(0,0,1),(2,0,0)}`, which fills under `f_L1` with history
`(3, 8, 11, 12)` and halts unfilled under `f_min` at `(3, 8, 10)`.

Every split seed meets both end faces of the two-cube (it contains at least
one site with `x = 0` and one with `x = 2`). The 108 seeds that miss an end
face never split. Every split seed also contains at least one pair of
displacement `(2,0,0)` or `(2,1,1)`: twenty-eight contain only a long-axis
pair, twenty-four contain only an opposite-corner pair, and eight contain
both. These partition statements classify the sixty seeds; they do not
adopt any one of them.

The six observed split history pairs, with multiplicities, are

| `f_L1` history | `f_min` history | count | fill L1 / min |
|---|---|---:|---|
| `(3, 8, 11, 12)` | `(3, 8, 10)` | 16 | yes / no |
| `(3, 10, 12)` | `(3, 10, 11)` | 16 | yes / no |
| `(3, 8, 11, 12)` | `(3, 8, 9)` | 8 | yes / no |
| `(3, 9, 12)` | `(3, 8, 10)` | 8 | yes / no |
| `(3, 9, 12)` | `(3, 9, 11)` | 8 | yes / no |
| `(3, 11, 12)` | `(3, 11)` | 4 | yes / no |

## Theorem 3 — Display, Do Not Adopt

The integer `N_split3 = 60` is the object of the census. The two fill counts
are reported with it. They are displayed, not adopted: do not adopt a seed,
and do not adopt either map. A selector is not written into Admissibility.
A later derivation that used one of these seeds as a physical rule would be
a different claim.

## What This Does Not Claim

- It does not claim that either map is the Admissibility rule.
- It does not claim that lock-step waves are physical Record formation.
- It does not claim a unique physically preferred three-site seed.
- It does not extend the census to `|S| ≠ 3` or to a larger patch.
- It does not identify `f_min` with Hamming weight, graph distance, or any
  map other than nonempty `n_both = 0`.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the three-site split-count question for the two displayed maps on the declared patch. |
| V2 | Current main has the axiom memo and no landed exhaustive three-site split census of these two maps. |
| V3 | All 220 triples, both runs, and the three integers are independently finite and exact. |
| V4 | The census is more than a restatement of the line-seed non-split or of the two-site count of four: it enumerates every three-site seed. |
| V5 | It is not a physical compiler and writes no selector into Admissibility. |

## No-Go Discipline Gate

The negative content is narrow: most three-site seeds do not split these two
maps, and the sixty that do are not hereby adopted. No global compiler
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| long-axis 3-site line | run both maps from `{(0,0,0),(1,0,0),(2,0,0)}` | no split; both fill with `(3, 9, 12)` |
| end-face plus far long-axis site | run both maps from `{(0,0,0),(0,0,1),(2,0,0)}` | splits by fill and history |
| seeds missing an end face | run both maps from each of the 108 | none split |
| Hamming-weight predicate | fire on six-bit weight | executed counterexample: opp2 has weight 2 and `f_L1 = 0` |
| adopt a seed | write one splitter into Admissibility | refused; displayed, not adopted |
| two-site leftover | recycle the four displacement-`(2,1,1)` pairs as the three-site count | refused; this is a new cardinality |

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
It does not supply `f_min`, `f_L1`, or a three-site selector. The residual
matches those sources.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 220 triples, two maps, lock-count histories | no continuum or larger-patch census |
| per site | six-neighbor occupancy 3-tuples | no derived kernel values |
| per mode | no mode calculation | no spectral statement |
| per block | two-cube lock-step dynamics | no physical formation compiler |
| lattice wide | checked and not executed | no infinite-volume claim |

### N6 — live partial-closure paths

Live routes are an independently derived formation mechanism, a derivation
that would force one of the two maps, and any census at a different seed
cardinality or patch. Those routes remain open.

### N7 — hostile steelman

**Steelman:** Because the two-site census already found four splitters, every
three-site seed that contains one of those pairs should split, and the
three-site count should therefore be a leftover character of the two-site
orbit.

**Answer:** Containment of a two-site splitter is neither necessary nor the
object counted here. Twenty-eight of the sixty three-site splits contain a
long-axis pair and no opposite-corner pair. Eight of the forty three-site
seeds that do contain an opposite-corner pair still fill under both maps.
The integer `N_split3 = 60` is a new cardinality on `|S| = 3`.

### N8 — cross-cycle echo

A prior displayed computation isolated the four two-site splitters as one
opposite-corner orbit and showed that the line seed does not split. This
note does not recycle that two-site count as the three-site census. It
enumerates every three-site seed and reports `N_split3 = 60`.

**Gate disposition:** PASS for the 220-seed census and the three displayed
integers above. FAIL / DO NOT SHIP for “Admissibility is `f_min`,” “adopt
this seed,” or “the maps agree on every finite seed.”

## Primary Runner

The primary runner recomputes the line seed, enumerates all 220 triples,
checks that `f_L1` is `n_unbalanced ≠ 0` rather than Hamming weight, checks
that `f_min` is nonempty `n_both = 0`, and checks that this note displays
`N_split3 = 60` without adopting a selector. It authors no audit verdict.
