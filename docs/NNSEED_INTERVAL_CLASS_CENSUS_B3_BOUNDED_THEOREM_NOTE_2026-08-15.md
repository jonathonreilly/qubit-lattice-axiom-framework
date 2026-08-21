---
claim_id: nnseed_interval_class_census_b3_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Interval s^2 space/null/time counts on formed nonzero sites of B_3(0) under the nnseed two-site process are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_interval_class_census_b3_2026_08_15.py
---

# Nnseed Interval Class Census On Formed Nonzero Sites Of B_3(0)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed space/null/time counts of the interval value
`s^2=t^2-|x|_2^2` on every formed nonzero site of the finite host `B_3(0)`,
under the nnseed two-site perp-step incoming-lock process with seed
`{0,(0,1,0)}` already formed at tick `0` and perp-consistent locks
`L(0)=+e_1`, `L(0,1,0)=+e_2`. Cardinality-of-seed, not a 1-site clone.
Uniqueness is not required. The axis class at `(1,0,0)` is displayed, not
adopted. This note does not write a metric into Admissibility.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_interval_class_census_b3_2026_08_15.py`](../scripts/nnseed_interval_class_census_b3_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, and the Record
  sentences that records form and that a present record locks exactly one
  admissible local possibility.

Everything after that quoted input is defined here as a finite displayed
process on `B_3(0)`. The lock letters below are unit nearest-neighbor steps,
not a new axiom alphabet. The quadratic `Q=|x|_2^2` is the Euclidean square
already used to name the host ball; it is not a second length attached to
the process.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite census of s^2 space/null/time on formed nonzero sites of B_3(0) under the nnseed two-site process; uniqueness is not claimed and the axis class is not adopted."
trace_class: upstream_support
target_claim_id: nnseed_interval_s2_space_null_time_census_b3
target_blocker_text: "display space/null/time counts of s^2=t^2-|x|_2^2 on formed nonzero B_3(0) sites under the two-site seed without adopting a metric or reprinting a four-event table"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep the census and the (1,0,0) class displayed only; do not write a metric into Admissibility."
conditional_surface_status: "exact on B_3(0) for the declared perp-step incoming-lock process with two-site seed {0,(0,1,0)} and locks +e_1/+e_2"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Displayed process

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, `e_3=(0,0,1)`. The six nearest-neighbor
steps are

```text
NN = {+e_1,-e_1,+e_2,-e_2,+e_3,-e_3}.
```

The finite host is the closed Euclidean ball of radius 3 centered at the
origin,

```text
B_3(0) = { n in Z^3 : n·n <= 9 }.
```

No larger host is used.

Lock alphabet: `{±e_1, ±e_2, ±e_3}`.

Seed at tick `0`: the origin is already recorded with lock letter `+e_1`, and
`(0,1,0)` is already recorded with lock letter `+e_2`. Both sites are already
formed. The pair is perp-consistent: the connecting step `+e_2` is
perpendicular to the origin lock `+e_1`. This is a two-record set, not a
1-site origin letter with a cloned second copy of the same lock.

From a recorded site `p` with lock `L(p)=±e_i`, a six-neighbor step `s in NN`
to `q=p+s` is allowed if and only if `s` is perpendicular to `e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms at tick `t(p)+1` and locks the incoming step `s` (the unit vector from
`p` to `q`). If several allowed parents reach `q` at the same earliest tick,
each such incoming step is recorded as a possible lock. Uniqueness is not
required. A later parent does not re-form `q`. A seed site is already formed,
so it is not re-formed.

The tick `t` is this formation tick. Seed sites have `t=0`. The tick is not
computed by a shortest-path search and is not a weighted path table.

On each formed nonzero site `x`, set

```text
Q(x) = |x|_2^2 = x·x,
s^2(x) = t(x)^2 - Q(x).
```

Classify that site as space if `s^2<0`, null if `s^2=0`, and time if `s^2>0`.
The origin is formed and is excluded from the census because the census is
over nonzero sites. The second seed `(0,1,0)` is formed and nonzero, so it
is inside the census.

Admissibility is not edited. The interval value is a displayed pairing of the
formation tick with the host quadratic. It is not a metric written into
Admissibility.

## Theorem 1 — formed nonzero count

The host `B_3(0)` has 123 lattice sites. The origin is formed at tick `0`.
The second seed `(0,1,0)` is formed at tick `0`. Exactly two host sites
remain unformed: `(3,0,0)` and `(-3,0,0)`. Every other host site forms.
Therefore the formed nonzero set has cardinality

```text
N_formed nonzero = 120.
```

The two unformed sites lie on the origin lock axis at Euclidean square `9`.
From the origin, axial steps `±e_1` are parallel to the seed lock `+e_1` and
are not allowed. The neighboring sites that would feed `(±3,0,0)` by a
remaining perpendicular step lie outside `B_3(0)`. Those two sites are
reported only as the complement that makes the formed-nonzero count exact on
this host.

The integer 120 is a cardinality on this two-site process. A 1-site origin
seed on the same host is a different formation history, so this census is
not a 1-site clone.

## Theorem 2 — space, null, and time counts

On the 120 formed nonzero sites the interval classes are

```text
N_space = 9,
N_null = 3,
N_time = 108.
```

These three integers partition the Theorem 1 set:

```text
9 + 3 + 108 = 120.
```

The nine space sites all have `s^2=-1`. They are the second seed and the
eight sites reached from it by one or two allowed perpendicular steps that
remain at `s^2=-1`:

```text
t=0, Q=1: (0,1,0),
t=1, Q=2: (1,1,0), (-1,1,0), (0,1,1), (0,1,-1),
t=2, Q=5: (1,2,0), (-1,2,0), (0,2,1), (0,2,-1).
```

The three null sites are exactly the tick-1 perpendicular neighbors of the
origin that are not the second seed,

```text
{(0,-1,0), (0,0,1), (0,0,-1)},
```

each with `t=1`, `Q=1`, and `s^2=0`. The remaining 108 formed nonzero sites
have `s^2>0`.

This is a census of every formed nonzero site of `B_3(0)` under the nnseed
two-site process. It is not a four-event table. A 1-site origin seed on the
same host yields a different space/null/time split.

## Theorem 3 — displayed class of (1,0,0)

The site `(1,0,0)` is formed. Direct evaluation gives

```text
t(1,0,0)=2,
Q(1,0,0)=1,
s^2(1,0,0)=3.
```

Because `3>0`, the displayed interval class of `(1,0,0)` is

```text
class time.
```

If the same site were scored with nearest-neighbor hop count `1` in place of
the formation tick, one would obtain `s^2=0` and class null. The displayed
class uses the formation tick, not hop count.

The class is displayed, not adopted. It is not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify `t` with a hop count or with a shortest-path cost.
- It does not enlarge the host beyond `B_3(0)`.
- It does not replace the two-site seed by a 1-site origin letter.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not write a metric into Admissibility.
- It does not reprint a four-event interval table as the claim.

## Primary runner

The paired runner builds `B_3(0)`, seeds the two-record set `{0,(0,1,0)}` at
tick `0` with locks `+e_1` and `+e_2`, runs the perp-step incoming-lock
process, and checks Theorems 1--3 by direct enumeration of formed nonzero
sites. It also checks that a 1-site origin seed on the same host is a
different class split, that dropping the perpendicular rule changes the
formed-nonzero count, that `Q` is the Euclidean square, and that a hop count
at `(1,0,0)` would have been null. No runner cache is written.
