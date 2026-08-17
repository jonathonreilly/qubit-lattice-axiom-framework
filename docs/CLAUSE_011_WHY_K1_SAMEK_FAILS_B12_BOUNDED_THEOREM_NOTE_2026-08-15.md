---
claim_id: clause_011_why_k1_samek_fails_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Lex-first shortest paths to (1,0,0) and (1,1,1) under the named (0,1,1) hop-cost on B_12(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_why_k1_samek_fails_b12_2026_08_15.py
---

# Why The Named (0,1,1) Same-k Reverse Fails At k=1 On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one Dijkstra for the named (0,1,1) hop-cost on the finite ball
`B_12(0)`. Lex-first shortest paths to `(1,0,0)` and `(1,1,1)` are named.
The same-k reverse comparison and first-hop costs are displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/clause_011_why_k1_samek_fails_b12_2026_08_15.py`](../scripts/clause_011_why_k1_samek_fails_b12_2026_08_15.py)

## Result Up Front

On the finite cubic box

`B_12(0) = { x in Z^3 : max(|x_1|,|x_2|,|x_3|) <= 12 }`,

equip nearest-neighbor hops with the named `(0,1,1)` hop-cost: the weight of a
site is its support size, and a hop costs `3` if and only if both weights are
`1` or the hop is a support drop; otherwise the hop costs `1`. One Dijkstra
from the origin yields

`t(1,0,0)=1`, `t(1,1,1)=3`.

A lex-first shortest path to each target is

`(0,0,0)->(1,0,0)`

and

`(0,0,0)->(0,0,1)->(0,1,1)->(1,1,1)`.

Uniqueness is not required: six shortest paths reach `(1,1,1)`. The residual
names the lex-first path only.

The displayed same-k reverse

`t(1,0,0)^2 / 1 > t(1,1,1)^2 / 3`

fails because `1 > 3` is false. Both lex-first first hops have cost `1`. That
cheap seed-exit is why the k=1 comparison fails. The same displayed comparison
holds at `k=2,3,4` on this ball (`16>12`, `49>27`, `64>48`). Those later
values are comparison context only.

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

The named `(0,1,1)` hop-cost is a separately supplied finite comparison rule
on `B_12(0)`. It is not an edit of that Admissibility sentence and is not
written into the axiom memo.

## Exact Objects

Sites are points of `Z^3` restricted to `B_12(0)`. Adjacency is the six-neighbor
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
search is executed once. Paths are sequences of sites in `B_12(0)`. Among
shortest paths to a named target, the lex-first path is the lexicographically
least vertex sequence, using ordinary integer order on coordinate triples.

## Theorem 1 — Named Distances And Lex-First Paths

The single origin Dijkstra on `B_12(0)` returns

`t(1,0,0)=1`, `t(1,1,1)=3`.

The unique shortest path to `(1,0,0)` is the seed-exit hop
`(0,0,0)->(1,0,0)`.

The six shortest paths to `(1,1,1)` are the six increasing coordinate orders.
The lex-first among them is

`(0,0,0)->(0,0,1)->(0,1,1)->(1,1,1)`.

No uniqueness claim is made for general targets.

## Theorem 2 — Displayed Same-k Reverse And First-Hop Costs

Write the displayed comparison

`t(1,0,0)^2 / 1 > t(1,1,1)^2 / 3`.

Substituting the Theorem 1 values gives `1 > 3`, which fails. The first hop of
each lex-first path has cost `1`. Replacing the cheap seed-exit by a cost-`3`
origin hop would change those first-hop costs; that mutation is not the named
rule.

On the same Dijkstra output the displayed comparison holds at `k=2,3,4`:

| `k` | `t(k,0,0)` | `t(k,k,k)` | left | right | holds |
|---:|---:|---:|---:|---:|:---:|
| 1 | 1 | 3 | 1 | 3 | no |
| 2 | 4 | 6 | 16 | 12 | yes |
| 3 | 7 | 9 | 49 | 27 | yes |
| 4 | 8 | 12 | 64 | 48 | yes |

Displayed, not adopted. The table is not a selected law, not an Admissibility
clause, and not a continuum kernel.

## Theorem 3 — No Admissibility Write And No L1 Attachment

Do not write (0,1,1) into Admissibility. The current axiom already names one
fixed nearest-neighbor admissibility rule and does not name this hop-cost.

Do not attach L1. The taxicab length of `(4,0,0)` is `4`, while
`t(4,0,0)=8` under the named rule, because axis continuation after the seed
exit has both weights `1`. The residual is the lex-first `(0,1,1)` paths on
`B_12(0)`, not a taxicab identification.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_12(0) names t(1,0,0), t(1,1,1), and the lex-first shortest paths. The same-k reverse and first-hop costs are displayed, not adopted."
trace_class: residual_naming
target_claim_id: clause_011_why_k1_samek_fails_b12
target_blocker_text: "name the lex-first (0,1,1) paths that make the k=1 same-k reverse fail"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the (0,1,1) hop-cost displayed only; do not write it into Admissibility and do not attach L1."
conditional_surface_status: "exact on B_12(0) for the named hop-cost; not an axiom clause"
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
| one Dijkstra on B_12(0) | executed by the primary runner |
| t(1,0,0) and t(1,1,1) | named |
| lex-first shortest paths | named |
| uniqueness of shortest paths | not required |
| same-k reverse at k=1 | displayed failure |
| first-hop costs | displayed; both 1 |
| write (0,1,1) into Admissibility | refused |
| attach L1 | refused |

## Boundary And Imports

No observation, fitted prefactor, continuum limit, or axiom edit is imported.
The comparison table at `k=2,3,4` is the same Dijkstra readout, not a second
search and not a selected continuum law.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It names the k=1 residual: cheap seed-exit makes t(1,0,0)=1 while t(1,1,1)=3. |
| V2 | Current main does not land these lex-first (0,1,1) paths on B_12(0). |
| V3 | Distances and paths are finite exact Dijkstra output. |
| V4 | The note is more than a restatement of Admissibility because the hop-cost is an extra named rule. |
| V5 | Displayed, not adopted: no axiom write and no L1 attachment. |

## No-Go Discipline Gate

The negative content is narrow: the displayed k=1 reverse fails, and the named
rule is not an Admissibility clause. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| named (0,1,1) hop-cost | cost 3 on both-weights-1 or support drop | executed; t(1,0,0)=1, t(1,1,1)=3 |
| unit hop-cost | every hop costs 1 | different rule; reverse fails at every k |
| forced expensive seed-exit | charge 3 to leave the origin | not the named rule; first-hop costs would change |
| taxicab attachment | set t(x)=||x||_1 | refused; t(4,0,0)=8 != 4 |
| write into Admissibility | treat the hop-cost as the axiom rule | refused |
| infinite lattice | drop the B_12(0) cutoff | outside this theorem |

### N2 — wall independence

The missing axiom write, the refused L1 attachment, and the unadopted reverse
comparison are distinct refusals. This note claims no complete wall collection.

### N3 — hidden-condition scan

The ball, the six-neighbor graph, the support-weight hop-cost, the single
Dijkstra, and lex order are declared. Uniqueness is not assumed.

### N4 — source residual matching

The residual is the lex-first paths that make the k=1 reverse fail under the
named rule. It matches that handoff and does not replace it by a taxicab claim.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | named hops and first-hop costs | no continuum kernel |
| per site | t values and lex-first paths | no uniqueness theorem |
| per mode | no mode calculation | no spectral claim |
| per block | k=1 reverse; k=2,3,4 context | no adopted law |
| lattice wide | B_12(0) only | no axiom edit |

### N6 — live partial-closure paths

Live routes are a separately derived hop-cost, a later comparison at larger
`k` still inside a declared ball, or an independent reason to reject or keep
the displayed reverse. None of those is adopted here.

### N7 — hostile steelman

**Steelman:** Because the reverse holds at `k=2,3,4`, the k=1 failure is a
ball artifact or a taxicab restatement.

**Answer:** The k=1 values are the two-step and six-path listings on the
nearest-neighbor graph. The cheap seed-exit costs `1` by the named rule, so
`t(1,0,0)=1` is forced. `t(4,0,0)=8` is already not the taxicab length.
Displayed, not adopted.

### N8 — cross-cycle echo

This note does not import a prior L1 residual and does not feed the named
hop-cost back into the axiom memo.

**Gate disposition:** PASS for the named distances, lex-first paths, displayed
k=1 failure, and the two refusals. FAIL / DO NOT SHIP for “the reverse is a
law,” “Admissibility is (0,1,1),” or “t is taxicab length.”

## Primary Runner

The primary runner executes one Dijkstra on `B_12(0)`, names the two distances
and lex-first paths, displays the reverse and first-hop costs, checks that the
current axiom memo does not contain the hop-cost, and writes no cache. It
authors no audit verdict.
