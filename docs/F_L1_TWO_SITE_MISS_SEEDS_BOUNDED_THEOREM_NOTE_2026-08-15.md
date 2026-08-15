---
claim_id: f_l1_two_site_miss_seeds_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The four two-site seeds on the two-cube from which f_L1 does not fill are listed. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_l1_two_site_miss_seeds_2026_08_15.py
---

# Four Two-Site Seeds From Which `f_L1` Does Not Fill

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exhaustive lock-step census of the 66 unordered two-site seeds on
the twelve-vertex two-cube `{0,1,2} × {0,1} × {0,1}` with off-patch occupancy
`o=0`. The four seeds from which `f_L1` does not fill are listed in
lexicographic order, each with halt lock-count and lock-history. They are
displayed. No seed is adopted and no selector is written into Admissibility.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_l1_two_site_miss_seeds_2026_08_15.py`](../scripts/f_l1_two_site_miss_seeds_2026_08_15.py)
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
`f_L1` fires iff `n_unbalanced ≠ 0` (some axis is unbalanced). This is
not Hamming parity of the six occupancy bits: `n_μ = c_{+μ} − c_{-μ}` is
nonzero on an axis if and only if that axis is unbalanced.

A prior coverage ranking reported `cov(f_L1) = 62` of the 66 two-site seeds
and left the four misses unnamed. A different four, the opposite-corner
pairs on which `f_L1` fills and `f_min` does not, were already listed.
Not leftover-character of #6422: that was the opposite-corner four (L1 fills, f_min does not). This note is the four-seed miss set of `f_L1` itself.

Recomputing every unordered pair under `f_L1` gives

`cov(f_L1) = 62`

and confirms that the four opposite-corner seeds

`{(0,0,0),(2,1,1)}`

`{(0,0,1),(2,1,0)}`

`{(0,1,0),(2,0,1)}`

`{(0,1,1),(2,0,0)}`

are fills, each with history `(2, 8, 12)`, and are not among the misses.

The four miss seeds, in lexicographic order of sorted site pairs, are

`{(0,0,0),(2,0,0)}`

`{(0,0,1),(2,0,1)}`

`{(0,1,0),(2,1,0)}`

`{(0,1,1),(2,1,1)}`.

Each has halt lock-count 8 and history `(2, 6, 8)`. The four-seed set is
displayed census output. It is not adopted as a physical selector.
Do not adopt a seed. Do not write them into Admissibility. A selector is not written into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 66 two-site seeds, the f_L1 lock-step runs, and the four listed misses are finite exact statements on a declared twelve-site patch; no seed is selected and no Admissibility clause is added."
trace_class: frontier_discovery
target_claim_id: f_l1_two_site_miss_seeds
target_blocker_text: "which four two-site seeds on the two-cube does f_L1 fail to fill"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the twelve-vertex two-cube with off-patch occupancy 0 and the displayed readiness map f_L1; no selector is adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
next_trace_action: "independent audit of the four miss-seed list; do not write a selector into Admissibility"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** Lattice, Admissibility, and Record are quoted from
  the live axiom memo without rewrite. They identify the cubic nearest-neighbor
  graph, the local-condition domain, and the lock/content/absence wording.
  They do not supply the readiness map `f_L1` or the two-cube patch.
- **Explicit theorem-domain condition:** the twelve sites
  `{0,1,2} × {0,1} × {0,1}`, off-patch occupancy identically `0`, the
  displayed map `f_L1`, and the synchronous lock-step dynamics above are
  supplied mathematical data for this list.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing `f_L1`, or any of the four miss seeds,
  into Admissibility remains a separate, open obligation. This note does
  not adopt them.

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

The readiness map `f_L1` is a displayed occupancy predicate on the
six-neighbor condition tuple. It is not Admissibility content. Using a
lock-step wave as physical Record formation would require a separately
derived formation mechanism; that mechanism is not supplied here.

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

The run of `f_L1` from `S` begins with `locks_0 = S`. At tick `t ≥ 1`
every unlocked `x ∈ V` with `f_L1(c(x, locks_{t-1})) = 1` locks
simultaneously. The history is `(|locks_0|, |locks_1|, …, |locks_T|)` at
the first `T` with no further ready site. Fill is the boolean
`|locks_T| = 12`. Coverage is
`cov(f_L1) = |{S : |S|=2 and f_L1 fills from S}|`.

`f_L1(c) = 1` iff `n_unbalanced ≠ 0`. This is not the Hamming weight of the
six occupancy bits: the opposite-pair occupancy at `(1,0,0)` with
`{(0,0,0),(2,0,0)}` locked has Hamming weight `2` and
`(n_unbalanced, n_both, n_empty) = (0,1,2)`, so `f_L1` does not fire.

The opposite-corner four of the earlier `f_min` versus `f_L1` split are the
displacement-`(2,1,1)` pairs. They are a different four: `f_L1` fills each
of them.

## Theorem 1 — Coverage And Opposite-Corner Fills

Every one of the 66 seeds is run independently under `f_L1`. The coverage
integer is

`cov(f_L1) = 62`.

The four opposite-corner seeds

`{(0,0,0),(2,1,1)}`,
`{(0,0,1),(2,1,0)}`,
`{(0,1,0),(2,0,1)}`,
`{(0,1,1),(2,0,0)}`

each fill under `f_L1` with history `(2, 8, 12)`. They are fills, not
misses.

## Theorem 2 — The Four Miss Seeds In Lexicographic Order

The four seeds from which `f_L1` does not fill, listed once each in
lexicographic site-pair order, are

`{(0,0,0),(2,0,0)}`,
`{(0,0,1),(2,0,1)}`,
`{(0,1,0),(2,1,0)}`,
`{(0,1,1),(2,1,1)}`.

Each of the four has halt lock-count 8 and history `(2, 6, 8)`. No other
two-site seed is a miss. The four pairs are exactly the long-axis
displacement-`(2,0,0)` pairs of the two-cube.

## Theorem 3 — Display, Do Not Adopt

The four-seed miss set is the object of this note. Display the four. Do not
adopt a seed. Do not write them into Admissibility. A selector is not
written into Admissibility. A later derivation that used one of these seeds
as a physical rule would be a different claim.

## What This Does Not Claim

- It does not claim that `f_L1` is the Admissibility rule.
- It does not claim that lock-step waves are physical Record formation.
- It does not claim a unique physically preferred two-site seed.
- It does not extend the list to `|S| ≠ 2` or to a larger patch.
- It does not identify `f_L1` with Hamming weight, graph distance, or any
  map other than some-axis-unbalanced.
- It does not treat the prior coverage integer `62` as a naming of the four
  misses, and it does not recycle the opposite-corner split four as this
  miss set.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the four-miss-seed identity question for `f_L1` on the declared patch. |
| V2 | Current main has the axiom memo and no landed list of these four two-site misses. |
| V3 | All 66 pairs, the `f_L1` runs, and the four listed misses are independently finite and exact. |
| V4 | The list is more than a restatement of `cov(f_L1) = 62`: it names each miss and its halt history. |
| V5 | It is not a physical compiler and writes no selector into Admissibility. |

## No-Go Discipline Gate

The negative content is narrow: the four listed miss seeds are not hereby
adopted. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| coverage integer | recompute all 66 two-site runs under `f_L1` | `cov(f_L1) = 62`; four misses remain |
| opposite-corner four | run `f_L1` from each displacement-`(2,1,1)` pair | each fills with `(2, 8, 12)`; not the miss set |
| long-axis `(2,0,0)` | run `f_L1` from each `{(0,y,z),(2,y,z)}` | each misses with halt lock-count 8 and history `(2, 6, 8)` |
| Hamming-weight predicate | fire on six-bit weight | executed counterexample: opp2 has weight 2 and `f_L1 = 0` |
| adopt a seed | write one miss into Admissibility | refused; displayed, not adopted |
| count-only coverage | report `cov = 62` without names | leftover-character of the coverage integer; this note lists the set |

### N2 — wall independence

The missing formation mechanism, the missing Admissibility selector, and any
extension off this twelve-site patch are distinct premises. This note claims
no complete wall collection.

### N3 — hidden-condition scan

The two-cube, off-patch occupancy `0`, the predicate `f_L1`, and the
synchronous wave rule are declared. Hamming weight is not silently used.
No seed is treated as axiom content.

### N4 — source residual matching

The current axiom memo supplies the cubic nearest-neighbor substrate, the
local-condition sentence, and the lock/content/absence wording used here.
It does not supply `f_L1` or a two-site selector. The residual matches
those sources.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 66 pairs, `f_L1` lock-count histories | no continuum or larger-patch census |
| per site | six-neighbor occupancy 3-tuples | no derived kernel values |
| per mode | no mode calculation | no spectral statement |
| per block | two-cube lock-step dynamics | no physical formation compiler |
| lattice wide | checked and not executed | no infinite-volume claim |

### N6 — live partial-closure paths

Live routes are an independently derived formation mechanism, a derivation
that would force `f_L1`, and any census at a different seed cardinality or
patch. Those routes remain open.

### N7 — hostile steelman

**Steelman:** Because a prior census already reported `cov(f_L1) = 62` and
another note already listed four two-site seeds, listing four misses adds
no object.

**Answer:** A coverage integer is not a list, and the opposite-corner four
are fills under `f_L1`. The four-seed miss set is a new displayed object:
the lex-ordered long-axis pairs and the common unfilled history
`(2, 6, 8)` with halt lock-count 8. The coverage row did not name the
set. The split-four row named a different four.

### N8 — cross-cycle echo

A prior displayed computation counted `cov(f_L1) = 62` and listed the four
seeds on which `f_min` and `f_L1` disagree. This note does not recycle
either object as the miss-seed identity. It recomputes every two-site run
under `f_L1` and lists the four seeds from which that map does not fill.

**Gate disposition:** PASS for the four-miss list, the reconfirmed coverage
integer, and the opposite-corner fill confirmation above. FAIL / DO NOT
SHIP for “Admissibility is `f_L1`,” “adopt this seed,” or “`f_L1` fills
every two-site seed.”

## Primary Runner

The primary runner recomputes all 66 pairs, reconfirms
`cov(f_L1) = 62` and that the four opposite-corner seeds fill with
history `(2, 8, 12)`, lists the four miss seeds in lexicographic order,
checks that each has halt lock-count 8 and history `(2, 6, 8)`, and
checks that this note displays that list without adopting a seed. It
authors no audit verdict.
