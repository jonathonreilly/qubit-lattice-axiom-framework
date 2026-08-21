---
claim_id: perpnn_two_site_seed_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Perp-step incoming-lock formation-tick reverse and face at k=1 on B_3(0) with two-site seed {0,(0,1,0)} and locks +e_1/+e_2 are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/perpnn_two_site_seed_reverse_face_2026_08_15.py
---

# Perp-Step Two-Site Seed Reverse And Face On B_3(0)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed formation-tick reverse and face at `k=1` on the finite
host `B_3(0)`, with lock alphabet `{±e_i}`, perp-step formation, incoming-step
lock, and two-record seed `{0,(0,1,0)}` already formed at tick `0` with
perp-consistent locks `L(0)=+e_1` and `L(0,1,0)=+e_2`. Cardinality-of-seed, not a 1-site clone. Uniqueness is not required. The inequalities are
displayed, not adopted. This note does not write into Admissibility and does
not identify the tick with six-neighbor distance.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/perpnn_two_site_seed_reverse_face_2026_08_15.py`](../scripts/perpnn_two_site_seed_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, and the Record
  sentences that records form and that a present record locks exactly one
  admissible local possibility.

Everything after that quoted input is defined here as a finite displayed
process on `B_3(0)`. The lock letters below are unit nearest-neighbor steps,
not a new axiom alphabet.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite formation on B_3(0) reports the origin tick-1 6-mask and the k=1 reverse and face comparisons for a two-site seed; uniqueness is not claimed and the inequalities are not adopted."
trace_class: upstream_support
target_claim_id: two_site_seed_k1_reverse_face_display
target_blocker_text: "display two-site-seed formation-tick reverse and face at k=1 without adopting a distance identification or an Admissibility edit"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep the inequalities displayed only; do not write them into Admissibility and do not require unique incoming locks."
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

The tick `t` is this formation tick. Seed sites have `t=0`. The tick is not a
weighted path table.

Admissibility is not edited. The process is a displayed Record-like lock on
the six-letter step alphabet, not a derivation of a physical rate.

Probes stay on `x`: `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`.

## Theorem 1 — origin tick-1 6-mask and probe ticks

Order the six neighbors of the origin as

```text
(+e_1, -e_1, +e_2, -e_2, +e_3, -e_3).
```

The origin lock is `+e_1`, so the two axial steps `±e_1` are parallel to `e_1`
and are not allowed from the origin. The four steps `±e_2, ±e_3` are
perpendicular to `e_1` and land in `B_3(0)`. The neighbor `+e_2=(0,1,0)` is
already a seed, so it is not formed at tick `1`. The remaining three
perpendicular neighbors form at tick `1` from the origin and lock the
incoming step:

```text
t(0,1,0)=0,  L includes +e_2  (seed),
t(0,-1,0)=1, L includes -e_2,
t(0,0,1)=1,  L includes +e_3,
t(0,0,-1)=1, L includes -e_3.
```

The axial neighbors of the origin do not form at tick `1`:

```text
t(1,0,0) != 1,  t(-1,0,0) != 1.
```

The origin tick-1 6-mask is therefore

```text
tick-1 6-mask, order (+e_1,-e_1,+e_2,-e_2,+e_3,-e_3): (0,0,0,1,1,1).
```

This is not the four-site perpendicular mask of a 1-site origin seed, which
would have bit `+e_2` set because `(0,1,0)` would then form at tick `1`.
Cardinality-of-seed is load-bearing for the mask.

The same process, grown from this two-site seed, gives defined probe ticks

```text
t(1,0,0)=2,
t(1,1,1)=2,
t(2,0,0)=3,
t(1,1,0)=1.
```

Witness paths (not claimed unique):

- Seed `(0,1,0) --+e_1--> (1,1,0)` at tick `1`, lock `+e_1`. Thus `t(D)=1`.
- `(1,1,0) -- -e_2 --> (1,0,0)` at tick `2`, lock `-e_2`. Thus `t(A)=2`.
- `(1,1,0) --+e_3--> (1,1,1)` at tick `2`, lock `+e_3`; also
  seed-neighbor `(0,1,1)` (formed at tick `1` with lock `+e_3`) steps `+e_1`
  into `(1,1,1)` at the same tick. Thus `t(B)=2` with at least two earliest
  locks `{+e_1,+e_3}`.
- `(1,0,0)` has earliest lock `-e_2`, which is perpendicular to `+e_1`, so
  `(1,0,0) --+e_1--> (2,0,0)` at tick `3`, lock `+e_1`. Thus `t(C)=3`.

Uniqueness is not required: `t(B)` is defined even though two earliest
incoming locks occur.

These values are not six-neighbor distances from a single origin: the
six-neighbor distance of `(1,0,0)` from the origin is `1`, while `t(1,0,0)=2`.

A 1-site origin seed with lock `+e_1` on the same host yields a different
mask and different probe ticks. The two-site display is therefore not a
1-site clone.

## Theorem 2 — displayed k=1 reverse

All four ticks in Theorem 1 are defined, so the `k=1` reverse comparison is
defined. Direct integer arithmetic gives

```text
3 t(1,0,0)^2 = 3 * 4 = 12,
t(1,1,1)^2 = 4,
12 > 4.
```

Thus reverse holds:

```text
3 t(1,0,0)^2 > t(1,1,1)^2.
```

Status: hold.

## Theorem 3 — displayed k=1 face

The face comparison is likewise defined. Direct integer arithmetic gives

```text
t(2,0,0)^2 = 9,
2 t(1,1,0)^2 = 2 * 1 = 2,
9 > 2.
```

Thus face holds:

```text
t(2,0,0)^2 > 2 t(1,1,0)^2.
```

Status: hold.

The reverse and face inequalities are displayed, not adopted. They are not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify `t` with six-neighbor distance or with a weighted
  path table.
- It does not enlarge the host beyond `B_3(0)`.
- It does not replace the two-site seed by a 1-site origin letter.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.

## Primary runner

The paired runner builds `B_3(0)`, seeds the two-record set `{0,(0,1,0)}` at
tick `0` with locks `+e_1` and `+e_2`, runs the perp-step incoming-lock
process, and checks Theorems 1--3 by direct enumeration. It also checks that
the origin-only 1-site seed on the same host is a different mask and a
different probe-tick tuple. No runner cache is written.
