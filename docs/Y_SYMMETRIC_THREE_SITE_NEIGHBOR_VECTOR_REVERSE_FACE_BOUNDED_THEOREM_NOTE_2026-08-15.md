---
claim_id: y_symmetric_three_site_neighbor_vector_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from unique already-recorded 6-NN lock vectors on the four y-probes of the y-symmetric three-site seed are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/y_symmetric_three_site_neighbor_vector_reverse_face_2026_08_15.py
---

# Y-Symmetric Three-Site Unique Neighbor-Vector Reverse And Face

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact finite growth of one declared y-symmetric three-site seed in
the Euclidean integer ball `B_3(0)={n:n·n<=9}`, with reverse and face read
from unique already-recorded six-neighbor lock vectors on four named
y-probes.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/y_symmetric_three_site_neighbor_vector_reverse_face_2026_08_15.py`](../scripts/y_symmetric_three_site_neighbor_vector_reverse_face_2026_08_15.py)

Displayed, not adopted. Do not write into Admissibility. Do not attach L1.

## Result Up Front

Host the integer points of Euclidean `B_3(0)={n:n·n<=9}`. At tick 0 record the
y-symmetric three-site seed

- origin `0=(0,0,0)` with formation lock `+e_1`,
- `(0,1,0)` with formation lock `-e_1`,
- `(0,-1,0)` with formation lock `-e_1`.

The third site is the y-mirror of the two-site opposite-lock partner
`(0,1,0)`. It is not the three-site opposite-lock third site `(1,0,0)` with
lock `+e_2`.

Grow by the declared perp-step rule: from a recorded site `p` whose formation
lock is `L(p)=±e_i`, a nearest-neighbor step `s` is allowed if and only if
`s·e_i=0`; the child `q=p+s` forms at tick `t(p)+1` and records incoming step
`s`. Incoming-step uniqueness is not required. A child reached by several
allowed parents at the same tick still forms.

The four y-probes are `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, and `D=(1,1,0)`.
These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`.
At the formation tick of a probe `q`, collect the formation locks of
already-recorded six-neighbors of `q` (strictly earlier ticks; at tick 0, the
other tick-0 recorded neighbors). If that set of lock vectors is a singleton
`{v}` inside `{±e_i}`, the unique letter is `v`. Otherwise the letter is
`UNDEFINED`.

`A` is a seed site. Reverse holds if and only if the unique letters of `A` and
`B` are defined and sum to `(0,0,0)`. Face holds if and only if the unique
letters of `C` and `D` are defined and sum to `(0,0,0)`.

The computed letters are `A=+e_1`, `B=+e_3`, `C` unique letter `-e_1`, and `D` is `UNDEFINED`.
Therefore reverse fails and face is `UNDEFINED`. This is a y-symmetric
three-site seed computation on the named y-probes, not leftover of the
three-site opposite-lock seed whose third site is `(1,0,0)` with lock `+e_2`,
and not the two-site opposite-lock y-probes. The predicates are reported. They
are not an Admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact neighbor-lock lists and reverse/face predicates on one declared y-symmetric three-site seed in B_3(0); displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact for the declared seed, perp-step grow, and unique already-recorded 6-NN letter"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Current Premise Boundary

Lattice and Record are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

When present, a record locks exactly one admissible local possibility.

The six-neighbor set used below is the Lattice nearest-neighbor set
`{±e_1,±e_2,±e_3}`. The seed, the perp-step grow, and the unique-letter
readout are declared host rules for this finite exhibit. They are not axiom
edits. Admissibility remains the existing nearest-neighbor probability rule
and is not rewritten here.

## Exact Objects

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, `e_3=(0,0,1)`. The host is the Euclidean
integer ball

`B_3(0)={n in Z^3: n·n<=9}`.

No larger ball is used. Formation is refused outside this ball. Shortest-path
search is not used: children form only by an allowed perp-step from an already
recorded parent.

Seed at tick 0:

| site | formation lock |
|---|---|
| `(0,0,0)` | `+e_1` |
| `(0,1,0)` | `-e_1` |
| `(0,-1,0)` | `-e_1` |

Perp-step grow. If `L(p)=±e_i`, the allowed steps are the four nearest-neighbor
vectors orthogonal to `e_i`. Incoming-step uniqueness is not required.

Already-recorded neighbor locks of a probe at its formation tick are formation
locks of six-neighbors recorded strictly earlier, except that `A` is a seed
site: at tick 0 its already-recorded 6-NN are other tick-0 recorded sites.

The unique letter is read from those already-recorded neighbor lock vectors.
It is not the probe's own incoming lock.

## Theorem 1 — Neighbor Lock Lists And Unique Letters

Each probe is recorded inside `B_3(0)`. The already-recorded six-neighbor
lock list and unique letter are:

| probe | site | formation tick | already-recorded 6-NN and formation locks | unique letter |
|---|---|---:|---|---|
| `A` | `(0,1,0)` | 0 | `(0,0,0)` at tick 0 with `+e_1` | `+e_1` |
| `B` | `(1,1,1)` | 2 | `(0,1,1)` at tick 1 with `+e_3` | `+e_3` |
| `C` | `(0,2,0)` | 1 | `(0,1,0)` at tick 0 with `-e_1` | `-e_1` |
| `D` | `(1,1,0)` | 3 | `(0,1,0)` tick 0 `-e_1`; `(1,2,0)` tick 2 `+e_1`; `(1,1,1)` tick 2 `+e_1`; `(1,1,-1)` tick 2 `+e_1` | `UNDEFINED` |

`A` therefore has unique letter `+e_1`. The other tick-0 seed `(0,-1,0)` is
not a six-neighbor of `A`. `B` has unique letter `+e_3`. `C` has unique
letter `-e_1`. The letter of `D` is `UNDEFINED` because the set of
already-recorded neighbor locks is `{+e_1,-e_1}`, not a singleton.

`B` itself has a single incoming step `+e_1` from `(0,1,1)`. That own-incoming
vector is not the unique letter. The unique letter of `B` is the neighbor-lock
singleton `{+e_3}`. `D` has three incoming steps `{+e_3,-e_3,-e_2}`; incoming
uniqueness is not required.

The four-tuple of unique letters is not leftover of the three-site
opposite-lock y-probes on seed `{0,(0,1,0),(1,0,0)}`: there `B` has two
already-recorded neighbors `(0,1,1)` and `(1,0,1)`, both `+e_3`, and `D`'s
neighbor-lock set includes `+e_2`. Here `B` has the single already-recorded
neighbor `(0,1,1)`, and `D`'s neighbor-lock set is `{+e_1,-e_1}`. Shared
probes `A,B,C,D` do not make this display a reprint.

## Theorem 2 — Reverse

Reverse holds if and only if the unique letters of `A` and `B` are defined and

`L(A)+L(B)=(0,0,0)`.

Here `L(A)=+e_1` and `L(B)=+e_3`, both defined, and

`(+e_1)+(+e_3)=(1,0,1)≠(0,0,0)`.

So reverse fails.

## Theorem 3 — Face

Face holds if and only if the unique letters of `C` and `D` are defined and

`L(C)+L(D)=(0,0,0)`.

Here `L(C)=-e_1` is defined and the letter of `D` is `UNDEFINED`. So face is
`UNDEFINED`. Displayed, not adopted.

## Non-Claims

This note does not adopt reverse or face as an Admissibility rule, does not
attach L1, does not edit the axiom memo, and does not identify the unique
letters with a physical Record readout beyond the declared host locks. It does
not claim a two-site remainder, a leftover of the `(1,0,0)` three-site seed,
or a larger ball.

Uniqueness of incoming steps is not required. Uniqueness of the neighbor-lock
set is required only to name a letter; otherwise the letter is `UNDEFINED`.
