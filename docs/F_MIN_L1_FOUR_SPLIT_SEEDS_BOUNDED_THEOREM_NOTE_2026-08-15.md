---
claim_id: f_min_l1_four_split_seeds_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The four two-site seeds on the two-cube that distinguish f_min from f_L1 are listed. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_min_l1_four_split_seeds_2026_08_15.py
---

# Four Two-Site Seeds That Split `f_min` From `f_L1`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exhaustive lock-step census of the 66 unordered two-site seeds on
the twelve-vertex two-cube `{0,1,2} × {0,1} × {0,1}` with off-patch occupancy
`o=0`. The four seeds that distinguish `f_min` from `f_L1` are listed in
lexicographic order. They are displayed. No seed is adopted and no selector
is written into Admissibility.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_min_l1_four_split_seeds_2026_08_15.py`](../scripts/f_min_l1_four_split_seeds_2026_08_15.py)
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

A prior count-only census reported `N_split = 4` of the 66 two-site seeds and
named one splitter `{(0,0,0),(2,1,1)}`. Not leftover-character of #6422: that only counted. This note is the four-seed set.

Recomputing every unordered pair gives

`N_split = 4`

`N_fill_L1 = 62`

`N_fill_min = 58`

and confirms that `{(0,0,0),(2,1,1)}` is one split.

The four seeds, in lexicographic order of sorted site pairs, are

`{(0,0,0),(2,1,1)}`

`{(0,0,1),(2,1,0)}`

`{(0,1,0),(2,0,1)}`

`{(0,1,1),(2,0,0)}`.

Each has `f_L1` history `(2, 8, 12)` and fills, and each has `f_min` halt
unfilled at history `(2, 8, 10)`. The four-seed set is displayed census
output. It is not adopted as a physical selector.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 66 two-site seeds, both lock-step runs, and the four listed splitters are finite exact statements on a declared twelve-site patch; no seed is selected and no Admissibility clause is added."
trace_class: frontier_discovery
target_claim_id: f_min_l1_four_split_seeds
target_blocker_text: "which four two-site seeds on the two-cube distinguish f_min from f_L1"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the twelve-vertex two-cube with off-patch occupancy 0 and the two displayed readiness maps; no selector is adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
next_trace_action: "independent audit of the four-seed list; do not write a selector into Admissibility"
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
  above are supplied mathematical data for this list.
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

A seed is an unordered pair `S ⊂ V` with `|S| = 2`. There are exactly
`C(12,2) = 66` such seeds. Lexicographic order of a seed is the ordered pair
of its two sites after each site is written in coordinate order
`(x,y,z)` and the two sites are then sorted.

The run of a map `f` from `S` begins with `locks_0 = S`. At tick `t ≥ 1`
every unlocked `x ∈ V` with `f(c(x, locks_{t-1})) = 1` locks simultaneously.
The history is `(|locks_0|, |locks_1|, …, |locks_T|)` at the first `T` with
no further ready site. Fill is the boolean `|locks_T| = 12`.

`f_L1(c) = 1` iff `n_unbalanced ≠ 0`. This is not the Hamming weight of the
six occupancy bits: the opposite-pair occupancy at `(1,0,0)` with
`{(0,0,0),(2,0,0)}` locked has Hamming weight `2` and
`(n_unbalanced, n_both, n_empty) = (0,1,2)`, so `f_L1` does not fire.

`f_min(c) = 1` iff `n_both = 0` and `n_unbalanced ≠ 0`. The maps therefore
disagree exactly when at least one axis is unbalanced and at least one axis
is doubly occupied.

## Theorem 1 — Census Reconfirmation

Every one of the 66 seeds is run independently under both maps. The census
integers are

`N_split = 4`,
`N_fill_L1 = 62`,
`N_fill_min = 58`.

The named pair `S_* = {(0,0,0),(2,1,1)}` is one split: `f_L1` fills with
history `(2, 8, 12)` and `f_min` halts unfilled at `(2, 8, 10)`.

## Theorem 2 — The Four Seeds In Lexicographic Order

The four splitters, listed once each in lexicographic site-pair order, are

`{(0,0,0),(2,1,1)}`,
`{(0,0,1),(2,1,0)}`,
`{(0,1,0),(2,0,1)}`,
`{(0,1,1),(2,0,0)}`.

Each of the four has the same displayed pair of runs: `f_L1` history
`(2, 8, 12)` and fill, `f_min` history `(2, 8, 10)` and unfilled halt at ten
locks. No other two-site seed splits the maps. The four pairs are exactly
the displacement-`(2,1,1)` pairs of the two-cube.

## Theorem 3 — Display, Do Not Adopt

The four-seed set is the object of this note. Display the four seeds. Do not adopt a selector. Do not write them into Admissibility. A selector is not written into Admissibility. A later derivation
that used one of these seeds as a physical rule would be a different claim.

## What This Does Not Claim

- It does not claim that either map is the Admissibility rule.
- It does not claim that lock-step waves are physical Record formation.
- It does not claim a unique physically preferred two-site seed.
- It does not extend the list to `|S| ≠ 2` or to a larger patch.
- It does not identify `f_min` with Hamming weight, graph distance, or any
  map other than nonempty `n_both = 0`.
- It does not treat the prior count `N_split = 4` as a naming of the four
  seeds.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the four-seed identity question for the two displayed maps on the declared patch. |
| V2 | Current main has the axiom memo and no landed list of these four two-site splitters. |
| V3 | All 66 pairs, both runs, and the four listed seeds are independently finite and exact. |
| V4 | The list is more than a restatement of the integer `N_split = 4`: it names each seed. |
| V5 | It is not a physical compiler and writes no selector into Admissibility. |

## No-Go Discipline Gate

The negative content is narrow: the four listed seeds are not hereby adopted.
No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| named splitter | run both maps from `{(0,0,0),(2,1,1)}` | split; L1 `(2, 8, 12)` fills, min `(2, 8, 10)` does not |
| remaining three displacement `(2,1,1)` pairs | run both maps from each | the same split pattern; they complete the list of four |
| long-axis `(2,0,0)` | run both maps from `{(0,y,z),(2,y,z)}` | neither fills; same history; not a split |
| Hamming-weight predicate | fire on six-bit weight | executed counterexample: opp2 has weight 2 and `f_L1 = 0` |
| adopt a seed | write one splitter into Admissibility | refused; displayed, not adopted |
| count-only census | report `N_split` without names | leftover-character of the count; this note lists the set |

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

**Steelman:** Because a prior census already reported `N_split = 4` and
named one splitter, listing the four seeds adds no object.

**Answer:** A count is not a list. The four-seed set is a new displayed
object: the lex-ordered pairs and the common history pair
`(2, 8, 12)` versus `(2, 8, 10)`. The count-only row did not name the
set.

### N8 — cross-cycle echo

A prior displayed computation counted four two-site splits. This note does
not recycle that integer as the four-seed identity. It recomputes every
two-site run and lists the four seeds.

**Gate disposition:** PASS for the four-seed list and the reconfirmed census
integers above. FAIL / DO NOT SHIP for “Admissibility is `f_min`,” “adopt
this seed,” or “the maps agree on every two-site seed.”

## Primary Runner

The primary runner recomputes all 66 pairs, reconfirms
`N_split = 4`, `N_fill_L1 = 62`, `N_fill_min = 58`, and that
`{(0,0,0),(2,1,1)}` is one split, lists the four seeds in lexicographic
order, checks that each has `f_L1` history `(2, 8, 12)` and `f_min`
unfilled `(2, 8, 10)`, and checks that this note displays that list without
adopting a selector. It authors no audit verdict.
