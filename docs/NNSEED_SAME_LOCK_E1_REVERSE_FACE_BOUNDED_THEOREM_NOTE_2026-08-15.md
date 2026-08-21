---
claim_id: nnseed_same_lock_e1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Perp-step incoming-lock formation-tick reverse and face at k=1 on Euclidean B_3(0) with two-site seed {0,(0,1,0)} both locking +e_1 are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_same_lock_e1_reverse_face_2026_08_15.py
---

# Same-Lock `+e_1` Two-Site Seed: Reverse And Face On Euclidean `B_3(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** perp-step incoming-lock formation ticks on the Euclidean host
`B_3(0)={n∈Z^3:n·n≤9}` with two-site seed `{0,(0,1,0)}` both locking `+e_1`
at tick 0. Reverse and face comparisons are displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_same_lock_e1_reverse_face_2026_08_15.py`](../scripts/nnseed_same_lock_e1_reverse_face_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Host Euclidean `B_3(0)`. Seed at tick 0: the origin is recorded with lock
`+e_1`, and `(0,1,0)` is recorded with the same lock `+e_1`. Growth is the
perp-step incoming-lock rule: from a recorded site `p` with lock
`L(p)=±e_i`, a nearest-neighbor step `s` is allowed iff `s·e_i=0`; the
image `q=p+s` forms at `t(p)+1` and takes incoming lock `s`, provided `q`
lies in the host and is not already recorded.

The x-probes are `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`.

On this seed the origin's tick-1 6-mask (occupancy of the six neighbors of
the origin among sites with formation tick at most 1, ordered
`+e_1,-e_1,+e_2,-e_2,+e_3,-e_3`) is `(0,0,1,1,1,1)`. The four probe ticks
are defined:

```text
t(A) = 3,  t(B) = 2,  t(C) = 4,  t(D) = 3.
```

The reverse comparison `3 t(A)^2 > t(B)^2` holds: `27 > 4`. The face
comparison `t(C)^2 > 2 t(D)^2` fails: `16 > 18` is false. Both comparisons
are displayed on this host and seed. They are not adopted as axiom content
and are not written into Admissibility.

The display is not a one-site letter clone: the one-site seed `{0}` locking
`+e_1` occupies `+e_2` only at tick 1 and yields different probe ticks. It
is not in the proper cubic orbit of a mixed-lock two-site seed with letters
`+e_1` and `+e_2`: a proper cubic rotation preserves equality or inequality
of the two seed lock letters.

Uniqueness of the incoming step is not required. First-arrival incoming
locks at `A` and at `D` are not unique; the formation ticks remain defined.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact discrete-time perp-step formation ticks on a finite Euclidean host, with reverse hold and face fail displayed for one two-site same-lock seed."
trace_class: frontier_discovery
target_claim_id: nnseed_same_lock_e1_reverse_face
target_blocker_text: "whether reverse and face formation-tick comparisons hold for the same-lock +e_1 two-site seed on Euclidean B_3(0)"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied Euclidean host and two-site same-lock seed; displayed, not adopted"
hypothetical_axiom_status: "none; the perp-step protocol and the reverse/face comparisons are displayed data, not axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded formation-tick claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** Lattice supplies the cubic nearest-neighbor
  geometry of `Z^3`. Record supplies permanence and single-site locking
  vocabulary. Both are quoted without rewrite.
- **Explicit theorem-domain condition:** the host is the Euclidean ball
  `B_3(0)={n∈Z^3:n·n≤9}` only. The seed, the perp-step incoming-lock rule,
  and the four x-probes are supplied data for this display.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** adopting reverse or face as an Admissibility
  constraint, a formation law, or a spacetime comparison remains a separate
  obligation. This note does not attach that bridge.

## Exact Objects

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, `e_3=(0,0,1)`, and
`S={±e_1,±e_2,±e_3}` for the six nearest-neighbor steps. The host is

```text
B_3(0) = { n ∈ Z^3 : n·n ≤ 9 }.
```

It contains 123 sites. Formation is discrete in the tick. A recorded site
carries a formation tick and a nonempty set of first-arrival incoming
steps. Outgoing continuation uses each first-arrival incoming step as a
lock letter: from recorded `p` with first-arrival letter `L(p)=±e_i`, a
step `s∈S` is allowed iff `s·e_i=0` and `p+s` lies in the host. If several
parents first reach the same site at the same tick, each incoming step is
kept; uniqueness is not required. Later arrivals are ignored. Records are
permanent.

Seed, at tick 0:

```text
t(0) = 0,     L(0) = +e_1,
t(0,1,0) = 0, L(0,1,0) = +e_1.
```

Probes: `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`.

The origin tick-1 6-mask is the 6-tuple of occupancy bits of
`0+s` for `s` in the order `+e_1,-e_1,+e_2,-e_2,+e_3,-e_3`, with bit 1
iff that neighbor is recorded at a formation tick at most 1.

Reverse comparison: `3 t(A)^2 > t(B)^2` if both ticks are defined.
Face comparison: `t(C)^2 > 2 t(D)^2` if both ticks are defined.

## Exact Target And Proof Obligations

The exact target is to report the origin tick-1 6-mask and the four probe
ticks on this host and seed, and to evaluate reverse and face as hold,
fail, or undefined. The obligation graph is:

1. enumerate `B_3(0)` by the Euclidean threshold `n·n≤9`;
2. grow by simultaneous tick, using only perp-step incoming-lock moves,
   without a path-search oracle;
3. read the origin star at tick 1 and the four probe ticks;
4. evaluate the two quadratic comparisons on those ticks;
5. separate the display from the mixed-lock two-site seed and from the
   one-site `+e_1` seed.

All five obligations are closed below and in the runner. The host radius,
the seed, and the perp-step rule are theorem hypotheses. Other hosts,
other seeds, and adoption into Admissibility are outside this theorem.

## Theorem 1 — tick-1 6-mask and probe ticks

The origin cannot step along `±e_1` because those steps are parallel to
its lock. It can step along `±e_2` and `±e_3`. The neighbor `+e_2` is
already recorded as seed, so it is not rewritten. The three new origin
neighbors at tick 1 are `-e_2`, `+e_3`, and `-e_3`. The seed neighbor
`+e_2` is already present at tick 0. Therefore the occupancy 6-mask at
tick 1 is

```text
(0, 0, 1, 1, 1, 1).
```

The three sites that form at tick 1 on the origin star are exactly
`(0,-1,0)`, `(0,0,1)`, and `(0,0,-1)`. The same tick also records
`(0,2,0)`, `(0,1,1)`, and `(0,1,-1)` from the second seed site; those
three are not origin neighbors.

Discrete-time perp-step growth on the host then gives defined probe ticks

```text
t(A) = 3,  t(B) = 2,  t(C) = 4,  t(D) = 3.
```

`B` first arrives from `(0,1,1)` by step `+e_1`. `A` first arrives at
tick 3 from three origin-star parents recorded at tick 2, with incoming
steps `+e_2`, `+e_3`, and `-e_3`. `D` first arrives at tick 3 with three
incoming steps. `C` first arrives at tick 4 from `A` by step `+e_1`. Every
first-arrival letter at `A` is perpendicular to `e_1`, so that last step
is available under each of them.

## Theorem 2 — reverse holds

Both `t(A)` and `t(B)` are defined. Direct integer arithmetic gives

```text
3 t(A)^2 = 3·9 = 27,    t(B)^2 = 4,    27 > 4.
```

So `3 t(A)^2 > t(B)^2` holds on this seed.

## Theorem 3 — face fails

Both `t(C)` and `t(D)` are defined. Direct integer arithmetic gives

```text
t(C)^2 = 16,    2 t(D)^2 = 2·9 = 18,    16 > 18 is false.
```

So `t(C)^2 > 2 t(D)^2` fails on this seed. The failure is displayed. It is
not adopted, and it is not written into Admissibility.

## Comparison Seeds, Not Parents

The mixed-lock two-site seed `{0,(0,1,0)}` with `L(0)=+e_1` and
`L(0,1,0)=+e_2` is a different letter pair. Proper cubic rotations send
that pair to another pair of distinct letters and cannot produce two copies
of `+e_1`. On that mixed seed the same grower yields `t(A)=2`, `t(B)=2`,
`t(C)=3`, `t(D)=1`, so reverse holds and face holds. The same-lock display
is therefore not a cubic copy of the mixed-lock seed.

The one-site seed `{0}` with lock `+e_1` occupies all four perpendicular
origin neighbors at tick 1, including `+e_2`, and yields `t(A)=3`,
`t(B)=3`, `t(C)=4`, `t(D)=2`. Face then holds. The two-site same-lock
seed is therefore not a one-site letter clone.

## Physical-Interpretation Boundary

The proved output is a finite formation-tick table and two displayed
quadratic comparisons. This note does not change Lattice, Qubit,
Admissibility, or Record. The perp-step rule is supplied protocol data for
the display, not an Admissibility rewrite. Reverse hold and face fail are
not proposed as axiom content.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. the origin tick-1 occupancy 6-mask is `(0,0,1,1,1,1)`, not the
   one-site mask that occupies `+e_2` only at tick 1;
2. reverse holds because `27>4`, not because a target constant was
   inserted;
3. face fails because `16>18` is false; the mixed-lock and one-site seeds
   do not reproduce that fail.

## What This Does Not Claim

- Reverse and face are not adopted as physical comparisons, clock maps, or
  Admissibility constraints.
- The perp-step protocol is not claimed to be the unique nearest-neighbor
  law, and it is not written into the axiom memo.
- Incoming-step uniqueness is not required and is not proved.
- No continuum limit, no path-length oracle, and no comparison beyond the
  four x-probes on this host is claimed.
- The mixed-lock seed is a contrast, not a parent theorem.
- Independent leftovers are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

> When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent.

> A site with no record cannot be read.

Their dependency role is limited to cubic nearest-neighbor geometry and
lock/permanence vocabulary. This theorem separately supplies the Euclidean
host, the two-site same-lock seed, and the perp-step protocol. Readout of
unrecorded sites remains outside the target: the four probes are recorded.

## Runner Contract

The companion runner enumerates `B_3(0)` by `n·n≤9`, grows by simultaneous
tick under the perp-step incoming-lock rule, and reports the origin tick-1
6-mask together with `t(A)`, `t(B)`, `t(C)`, and `t(D)`. It evaluates
reverse and face on those computed ticks, checks that the display is not a
one-site letter clone and not in the proper cubic orbit of the mixed-lock
seed, and pins the declared review inputs to this note and the axiom memo
only. It uses no path-search oracle.
