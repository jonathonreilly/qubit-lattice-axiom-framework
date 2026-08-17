---
claim_id: clause_011_why_samek_k6_fails_b18_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Lex-first shortest paths to (6,0,0) and (6,6,6) under the named (0,1,1) hop-cost on B_18(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_why_samek_k6_fails_b18_2026_08_15.py
---

# Why The Named (0,1,1) Same-k Reverse Fails At k=6 On B_18(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one Dijkstra for the named (0,1,1) hop-cost on the finite ball
`B_18(0)`. Lex-first shortest paths to `(6,0,0)` and `(6,6,6)` are named.
The same-k reverse comparison is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/clause_011_why_samek_k6_fails_b18_2026_08_15.py`](../scripts/clause_011_why_samek_k6_fails_b18_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

On the finite cubic neighborhood

`B_18(0) = { x in Z^3 : |x|_1 <= 18 }`,

which has exactly `8473` sites, equip nearest-neighbor hops with the named
`(0,1,1)` hop-cost: the weight of a site is its support size, and a hop costs
`3` if and only if both weights are `1` or the hop is a support drop;
otherwise the hop costs `1`. Seed-exit is therefore cheap. One Dijkstra from
the origin yields

`t(6,0,0)=10`, `t(6,6,6)=18`.

A lex-first shortest path to each target is

`(0,0,0)->(0,-1,0)->(1,-1,0)->(2,-1,0)->(3,-1,0)->(4,-1,0)->(5,-1,0)->(6,-1,0)->(6,0,0)`

with hop-cost list `(1,1,1,1,1,1,1,3)` summing to `10`, and

`(0,0,0)->(0,0,1)->(0,1,1)->(0,1,2)->(0,1,3)->(0,1,4)->(0,1,5)->(0,1,6)->(0,2,6)->(0,3,6)->(0,4,6)->(0,5,6)->(0,6,6)->(1,6,6)->(2,6,6)->(3,6,6)->(4,6,6)->(5,6,6)->(6,6,6)`

with hop-cost list `(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)` summing to `18`.

Uniqueness is not required. Eight shortest paths reach `(6,0,0)`. The residual
names the lex-first path only. Naming the two walks is not leftover of the no
bit: the axis walk is an eight-hop face detour, not the single cheap seed-exit
that already makes the k=1 comparison fail, and the axis-only competitor
`1+3+3+3+3+3=16` is strictly more expensive than `t(6,0,0)=10`.

The displayed same-k reverse

`t(6,0,0)^2 / 36 > t(6,6,6)^2 / 108`

fails because `100/36 > 324/108` is `300 > 324`, which is false. Both
lex-first first hops have cost `1`. The body-diagonal site `(6,6,6)` has
nearest-neighbor graph length `18`, so it is absent from `B_16(0)` and sits
on the boundary of `B_18(0)`.

Do not write (0,1,1) into Admissibility. Do not attach L1. Displayed, not
adopted.

## Current Premise Boundary

The Lattice and Admissibility sentences used only as domain language are
quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.

Only records are readable. A readout value is determined by record content
alone. A site with no record cannot be read.

The named `(0,1,1)` hop-cost is a separately supplied finite comparison rule
on `B_18(0)`. It is not an edit of that Admissibility sentence and is not
written into the axiom memo. Admissibility does not supply the formation site,
probability, or rate.

## Exact Objects

Sites are points of `Z^3` restricted to `B_18(0)`. Adjacency is the six-neighbor
relation. The support of `x` is the set of coordinates with `x_i != 0`. The
weight of `x` is the support size `s(x)`. A hop `u -> v` is a support drop
when `s(v) < s(u)`.

The named `(0,1,1)` hop-cost is

```text
c(u,v) = 3  if s(u)=s(v)=1 or s(v)<s(u),
c(u,v) = 1  otherwise.
```

Every origin-adjacent hop has `s(0)=0` and `s(v)=1`, so it costs `1`. That is
the cheap seed-exit.

`t(x)` is the Dijkstra distance from the origin in this weighted graph. The
search is executed once. Paths are sequences of sites in `B_18(0)`. Among
shortest paths to a named target, the lex-first path is the lexicographically
least vertex sequence, using ordinary integer order on coordinate triples.

## Theorem 1 — Named Distances And Lex-First Paths

The single origin Dijkstra on `B_18(0)` returns

`t(6,0,0)=10`, `t(6,6,6)=18`.

The lex-first shortest path to `(6,0,0)` is the face detour

`(0,0,0)->(0,-1,0)->(1,-1,0)->(2,-1,0)->(3,-1,0)->(4,-1,0)->(5,-1,0)->(6,-1,0)->(6,0,0)`

with hop-costs `(1,1,1,1,1,1,1,3)`. The closing hop is a support drop and
costs `3`. The axis-only walk of graph length `6` costs `16` and is not
shortest.

The lex-first shortest path to `(6,6,6)` is the support-nondecreasing walk

`(0,0,0)->(0,0,1)->(0,1,1)->(0,1,2)->(0,1,3)->(0,1,4)->(0,1,5)->(0,1,6)->(0,2,6)->(0,3,6)->(0,4,6)->(0,5,6)->(0,6,6)->(1,6,6)->(2,6,6)->(3,6,6)->(4,6,6)->(5,6,6)->(6,6,6)`

with hop-costs `(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)`. That walk uses only
cost-`1` hops and has the same length as the nearest-neighbor graph length
`18`.

No uniqueness claim is made for general targets.

## Theorem 2 — Displayed Same-k Reverse Fails

Write the displayed comparison

`t(6,0,0)^2 / 36 > t(6,6,6)^2 / 108`.

Substituting the Theorem 1 values gives `100/36` versus `324/108`, or
`300 > 324`, which fails. Equivalently `3 t(6,0,0)^2 > t(6,6,6)^2` is false.
Displayed, not adopted.

The first hop of each lex-first path has cost `1`. That cheap seed-exit is the
no bit of the named toggle. The k=6 residual is not leftover of the no bit:
removing the opening hop still leaves an eight-hop axis reconstruction and an
eighteen-hop body reconstruction, and the displayed products `100` and `324`
are not the k=1 leftover pair `1` and `3`.

## Theorem 3 — No Admissibility Write And No L1 Attachment

Do not write (0,1,1) into Admissibility. The current axiom already names one
fixed nearest-neighbor admissibility rule and does not name this hop-cost.

Do not attach L1. The taxicab length of `(6,0,0)` is `6`, while
`t(6,0,0)=10` under the named rule. The residual is the lex-first `(0,1,1)`
paths on `B_18(0)`, not a taxicab identification.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_18(0) names t(6,0,0), t(6,6,6), and the lex-first shortest paths. The same-k reverse is displayed and fails. Displayed, not adopted."
trace_class: residual_naming
target_claim_id: clause_011_why_samek_k6_fails_b18
target_blocker_text: "name the lex-first (0,1,1) paths that make the k=6 same-k reverse fail"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the (0,1,1) hop-cost displayed only; do not write it into Admissibility and do not attach L1."
conditional_surface_status: "exact on B_18(0) for the named hop-cost; not an axiom clause"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility wording | quoted; no edit |
| named (0,1,1) hop-cost | separately supplied; displayed only |
| one Dijkstra on B_18(0) | executed by the primary runner |
| t(6,0,0) and t(6,6,6) | named `10` and `18` |
| lex-first shortest paths | named |
| uniqueness of shortest paths | not required |
| same-k reverse at k=6 | displayed failure |
| leftover of the no bit | refused |
| write (0,1,1) into Admissibility | refused |
| attach L1 | refused |

## Boundary And Imports

No observation, fitted prefactor, continuum limit, or axiom edit is imported.
The separately named support-drop rule that holds same-k reverse at `k=6` is
not scored here and is not a second Dijkstra.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It names the k=6 residual: lex-first (0,1,1) paths give t(6,0,0)=10 and t(6,6,6)=18, so reverse fails. |
| V2 | Current main does not land these lex-first (0,1,1) paths on B_18(0). |
| V3 | Distances and paths are finite exact Dijkstra output. |
| V4 | The note is more than a restatement of Admissibility because the hop-cost is an extra named rule. |
| V5 | Displayed, not adopted: no axiom write and no L1 attachment. |

## No-Go Discipline Gate

The negative content is narrow: the displayed k=6 reverse fails, the walks are
not leftover of the no bit, and the named rule is not an Admissibility clause.
No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| named (0,1,1) hop-cost | cost 3 on both-weights-1 or support drop | executed; t(6,0,0)=10, t(6,6,6)=18 |
| axis-only competitor | stay on the x-axis after seed-exit | costs 16, not shortest |
| unit hop-cost | every hop costs 1 | different rule; t would be graph length |
| taxicab attachment | set t(x)=||x||_1 | refused; t(6,0,0)=10 != 6 |
| write into Admissibility | treat the hop-cost as the axiom rule | refused |
| infinite lattice | drop the B_18(0) cutoff | outside this theorem |

### N2 — wall independence

The missing axiom write, the refused L1 attachment, and the unadopted reverse
comparison are distinct refusals. This note claims no complete wall collection.

### N3 — hidden-condition scan

The ball, the six-neighbor graph, the support-weight hop-cost, the single
Dijkstra, and lex order are declared. Uniqueness is not assumed.

### N4 — source residual matching

The residual is the lex-first paths that make the k=6 reverse fail under the
named rule. It matches that handoff and is not leftover of the no bit.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | named hops and first-hop costs | no continuum kernel |
| per site | t values and lex-first paths | no uniqueness theorem |
| per mode | no mode calculation | no spectral claim |
| per block | k=6 reverse displayed failure | no adopted law |
| lattice wide | B_18(0) only | no axiom edit |

### N6 — live partial-closure paths

Live routes are a separately derived hop-cost, a later comparison at another
declared ball, or an independent reason to reject or keep the displayed
reverse. None of those is adopted here.

### N7 — hostile steelman

**Steelman:** Because seed-exit is already cheap, the k=6 failure is leftover
of the no bit, or is a taxicab restatement.

**Answer:** The lex-first axis walk has eight hops and closes by a cost-`3`
support drop. The axis-only taxicab walk costs `16`. The displayed products
are `300` and `324`, not the k=1 pair. Displayed, not adopted.

### N8 — cross-cycle echo

This note does not import a prior L1 residual and does not feed the named
hop-cost back into the axiom memo.

**Gate disposition:** PASS for the named distances, lex-first paths, displayed
k=6 failure, and the two refusals. FAIL / DO NOT SHIP for “the reverse is a
law,” “Admissibility is (0,1,1),” or “t is taxicab length.”

## Primary Runner

The primary runner executes one Dijkstra on `B_18(0)`, names the two distances
and lex-first paths, displays the reverse, checks that the current axiom memo
does not contain the hop-cost, and writes no cache. It authors no audit
verdict.

## Reproducibility

```text
python3 scripts/clause_011_why_samek_k6_fails_b18_2026_08_15.py
```

The runner prints the two times, the two lex-first walks, the displayed
comparison, and `TOTAL: PASS=<n> FAIL=<n>`.
