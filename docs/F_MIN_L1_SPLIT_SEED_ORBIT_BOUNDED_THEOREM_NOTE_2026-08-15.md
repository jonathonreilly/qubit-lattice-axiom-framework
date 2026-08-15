---
claim_id: f_min_l1_split_seed_orbit_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The four two-site seeds that distinguish f_min from f_L1 form N_orb orbits under two-cube-preserving proper cube rotations. Here N_orb=1. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_min_l1_split_seed_orbit_2026_08_15.py
---

# Split-Seed Orbit Count Of `f_min` Versus `f_L1`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** orbit count of the four two-site seeds on the twelve-vertex
two-cube `{0,1,2} × {0,1} × {0,1}` that distinguish `f_min` from `f_L1`,
under the proper cube rotations about the box center `(1, 1/2, 1/2)` that
permute those twelve sites. The integer `N_orb` is displayed. No seed is
adopted and no orbit is written into Admissibility.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_min_l1_split_seed_orbit_2026_08_15.py`](../scripts/f_min_l1_split_seed_orbit_2026_08_15.py)
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
lock-history tuples differ. Recomputing every unordered pair on the twelve
sites recovers exactly four splitters, each with `f_L1` history `(2, 8, 12)`
and `f_min` halt unfilled at `(2, 8, 10)`:

`{(0,0,0),(2,1,1)}`, `{(0,0,1),(2,1,0)}`, `{(0,1,0),(2,0,1)}`,
`{(0,1,1),(2,0,0)}`.

These four pairs are the four space diagonals of the long box: opposite
corners through the center `(1, 1/2, 1/2)`.

The ambient proper cubic group about that center has 24 matrices (signed
permutations of the three axes with determinant `+1`). Sixteen of those
matrices send at least one of the twelve sites off the two-cube and are
not used. The remaining eight permute the twelve sites and induce the
group `G` of this note.

`N_orb = 1`

The four split seeds form a single `G`-orbit. The split is one geometric
type — opposite corners of the long box — not four independent extras.
`N_orb` is displayed census output. It is not adopted as a physical
selector, and the orbit is not written into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The four split seeds, the 24 ambient proper cube rotations, the eight two-cube-preserving site-permutations, and the single orbit integer are finite exact statements on a declared twelve-site patch; no seed is selected and no Admissibility clause is added."
trace_class: frontier_discovery
target_claim_id: f_min_l1_split_seed_orbit
target_blocker_text: "whether the four two-site seeds that split f_min from f_L1 form one orbit under two-cube-preserving proper cube rotations"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the twelve-vertex two-cube with off-patch occupancy 0 and the two displayed readiness maps; no selector is adopted"
hypothetical_axiom_status: "none; f_min and the four splitting seeds are displayed and are not proposed as axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded orbit count; do not write an orbit into Admissibility"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** Lattice, Admissibility, and Record are quoted from
  the live axiom memo without rewrite. They identify the cubic nearest-neighbor
  graph, the local-condition domain, and the lock/content/absence wording.
  They do not supply the two readiness maps, the two-cube patch, or an orbit
  of seeds.
- **Explicit theorem-domain condition:** the twelve sites
  `{0,1,2} × {0,1} × {0,1}`, off-patch occupancy identically `0`, the two
  displayed maps `f_L1` and `f_min`, the synchronous lock-step dynamics,
  and the proper cube rotations about `(1, 1/2, 1/2)` that permute those
  twelve sites are supplied mathematical data for this orbit count.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing either map, any of the four splitting
  seeds, or their orbit into Admissibility remains a separate, open
  obligation. This note does not adopt them.

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

A seed is an unordered pair `S ⊂ V` with `|S| = 2`. The run of a map `f`
from `S` begins with `locks_0 = S`. At tick `t ≥ 1` every unlocked
`x ∈ V` with `f(c(x, locks_{t-1})) = 1` locks simultaneously. The history
is `(|locks_0|, |locks_1|, …, |locks_T|)` at the first `T` with no further
ready site. Fill is the boolean `|locks_T| = 12`.

`f_L1(c) = 1` iff `n_unbalanced ≠ 0`. This is not the Hamming weight of the
six occupancy bits: the opposite-pair occupancy at `(1,0,0)` with
`{(0,0,0),(2,0,0)}` locked has Hamming weight `2` and
`(n_unbalanced, n_both, n_empty) = (0,1,2)`, so `f_L1` does not fire.

`f_min(c) = 1` iff `n_both = 0` and `n_unbalanced ≠ 0`.

The ambient group of proper cube rotations about the box center
`c = (1, 1/2, 1/2)` is the set of maps `x ↦ c + R(x − c)` where `R` is a
`3 × 3` signed-permutation matrix with `det R = +1`. There are
`3! × 2^3 / 2 = 24` such matrices. A rotation is used only when it
permutes `V`. The sixteen matrices that send a site of `V` off the
two-cube are discarded. The remaining eight form `G` and act on
unordered pairs by `g · {p, q} = {g(p), g(q)}`.

## Theorem 1 — Four Split Seeds, One Orbit

Recomputing all `C(12,2) = 66` two-site seeds recovers `N_split = 4`.
The four seeds, in lexicographic order, are

`{(0,0,0),(2,1,1)}`, `{(0,0,1),(2,1,0)}`, `{(0,1,0),(2,0,1)}`,
`{(0,1,1),(2,0,0)}`.

Each has `f_L1` history `(2, 8, 12)` and `f_min` halt unfilled at
`(2, 8, 10)`.

The quarter-turn about the long axis through `c`,

`(x, y, z) ↦ (x, 1 − z, y)`,

is one of the eight elements of `G`. It cycles the four seeds

`{(0,0,0),(2,1,1)} → {(0,1,0),(2,0,1)} → {(0,1,1),(2,0,0)} → {(0,0,1),(2,1,0)}`.

Therefore the four seeds lie in a single `G`-orbit:

`N_orb = 1`.

## Theorem 2 — One Geometric Type

Because `N_orb = 1`, the split is one geometric type: opposite corners of
the long box. There is no second orbit to display. The four pairs are the
four space diagonals through `c`. They are not four independent extras.

A rotation that fails to preserve the twelve-set is not used to manufacture
a larger group or a second type.

## Theorem 3 — Display, Do Not Adopt

The integer `N_orb = 1` is the object of the count. The four seeds and the
order `|G| = 8` of the two-cube-preserving subgroup are reported with it.
They are displayed, not adopted: do not adopt a seed, and do not adopt the
orbit. An orbit is not written into Admissibility. A later derivation that
used this orbit as a physical rule would be a different claim.

## What This Does Not Claim

- It does not claim that either map is the Admissibility rule.
- It does not claim that lock-step waves are physical Record formation.
- It does not claim a unique physically preferred two-site seed.
- It does not claim that all 24 proper cube rotations permute the two-cube.
- It does not write the orbit, or any seed, into Admissibility.
- It does not identify `f_min` with Hamming weight, graph distance, or any
  map other than nonempty `n_both = 0`.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the orbit-count question for the four displayed split seeds under two-cube-preserving proper cube rotations. |
| V2 | Current main has the axiom memo and no landed orbit count of these four seeds. |
| V3 | The four seeds, the 24 ambient matrices, the eight preservers, and `N_orb` are independently finite and exact. |
| V4 | The orbit integer is more than a restatement of the four-seed list: it is a new object, the number of geometric types. |
| V5 | It is not a physical compiler and writes no orbit into Admissibility. |

## No-Go Discipline Gate

The negative content is narrow: the four splitters are one `G`-orbit on this
patch, and that orbit is not hereby adopted. No global compiler impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| recompute the 66 pairs | lock-step both maps | `N_split = 4`, same four seeds |
| full 24 about the box center | apply every proper cubic matrix | 16 fail to permute `V` and are unused |
| two-cube-preserving `G` | act with the remaining 8 | one orbit; `N_orb = 1` |
| Hamming-weight predicate | fire on six-bit weight | executed counterexample: opp2 has weight 2 and `f_L1 = 0` |
| adopt the orbit | write `G · S_*` into Admissibility | refused; displayed, not adopted |
| a second geometric type | exhibit a split seed outside the long-box diagonals | none among the four |

### N2 — wall independence

The missing formation mechanism, the missing Admissibility selector, and any
extension off this twelve-site patch are distinct premises. This note claims
no complete wall collection.

### N3 — hidden-condition scan

The two-cube, off-patch occupancy `0`, the two predicates, the synchronous
wave rule, and the restriction to site-permuting proper cube rotations are
declared. Hamming weight is not silently used. No seed or orbit is treated
as axiom content.

### N4 — source residual matching

The current axiom memo supplies the cubic nearest-neighbor substrate, the
local-condition sentence, and the lock/content/absence wording used here.
It does not supply `f_min`, `f_L1`, or a two-site orbit. The residual
matches those sources.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 66 pairs, two maps, 24 ambient rotations, 8 preservers | no continuum or larger-patch census |
| per site | six-neighbor occupancy 3-tuples | no derived kernel values |
| per mode | no mode calculation | no spectral statement |
| per block | two-cube lock-step dynamics and box-center rotations | no physical formation compiler |
| lattice wide | checked and not executed | no infinite-volume claim |

### N6 — live partial-closure paths

Live routes are an independently derived formation mechanism, a derivation
that would force one of the two maps, and any orbit count at a different
seed cardinality or patch. Those routes remain open.

### N7 — hostile steelman

**Steelman:** The two-cube is elongated, so the 24 proper cube rotations
cannot act, and the four space diagonals could be four types under the
surviving group.

**Answer:** Sixteen of the 24 matrices are discarded because they do not
permute the twelve sites. The remaining eight still contain the long-axis
quarter-turn, which cycles all four space diagonals. The four seeds are
one type.

### N8 — cross-cycle echo

A prior displayed computation counted `N_split = 4` and listed the four
seeds. This note does not recycle that count as the orbit integer. It
recomputes the four seeds and reports `N_orb = 1` under the
two-cube-preserving proper cube rotations.

**Gate disposition:** PASS for the orbit count and the displayed integer
`N_orb = 1` above. FAIL / DO NOT SHIP for “Admissibility is `f_min`,”
“adopt this orbit,” or “the 24 ambient rotations all permute the two-cube.”

## Primary Runner

The primary runner recomputes the four split seeds, enumerates the 24
proper cube rotations about the box center, keeps only the eight that
permute the twelve sites, counts `G`-orbits, checks that `f_L1` is
`n_unbalanced ≠ 0` rather than Hamming weight, checks that `f_min` is
nonempty `n_both = 0`, and checks that this note displays `N_orb = 1`
without adopting a seed or writing an orbit into Admissibility. It
authors no audit verdict.
