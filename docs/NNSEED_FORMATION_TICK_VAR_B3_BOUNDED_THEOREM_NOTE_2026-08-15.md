---
claim_id: nnseed_formation_tick_var_b3_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Arrival-speed variance of nnseed formation-tick on formed nonzero sites of B_3(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_formation_tick_var_b3_2026_08_15.py
---

# Nnseed Formation-Tick Arrival-Speed Variance On B_3(0)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed population variance of `|x|_2/t` on the formed nonzero
sites of the finite host `B_3(0)` under the perp-step incoming-lock process
with two-site seed `{0,(0,1,0)}` and locks `+e_1` and `+e_2`. Uniqueness is
not required. The variance is displayed, not adopted. This note does not
write into Admissibility and does not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_formation_tick_var_b3_2026_08_15.py`](../scripts/nnseed_formation_tick_var_b3_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, and the Record
  sentences that records form and that a present record locks exactly one
  admissible local possibility.

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

The axiom does not supply the formation site, probability, or rate.

The current Record boundary is:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

None of Record is used to select a formation tick. Everything after that quoted
input is defined here as a finite displayed process on `B_3(0)`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite formation on B_3(0) reports the formed nonzero set, the formation ticks, and the population variance of |x|_2/t on the positive-tick subset; uniqueness is not claimed and the variance is not adopted."
trace_class: upstream_support
target_claim_id: nnseed_formation_tick_arrival_speed_var_b3
target_blocker_text: "display var(|x|_2/t) on formed nonzero sites of B_3(0) under the two-site-seed perp-step incoming-lock process"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep the variance displayed only; do not write it into Admissibility and do not attach L1."
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

This set has 123 sites. No larger host is used.

Lock alphabet: `{±e_1, ±e_2, ±e_3}`.

Seed at tick `0`: the origin is already recorded with lock letter `+e_1`, and
`(0,1,0)` is already recorded with lock letter `+e_2`. Both sites are already
formed. The pair is perp-consistent: the connecting step `+e_2` is
perpendicular to the origin lock `+e_1`. This is a two-record set, not a
1-site origin letter.

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

The tick `t` is this formation tick. Seed sites have `t=0`. It is not a hop
count and is not a weighted path table.

Admissibility is not edited. The process is a displayed Record-like lock on
the six-letter step alphabet, not a derivation of a physical rate.

## Theorem 1 — formed nonzero sites and their ticks

The origin is formed at tick `0` and is excluded from the formed-nonzero set.
The second seed `(0,1,0)` is formed at tick `0` and is a formed nonzero site.
Exactly two host sites never form:

```text
unformed = {(3,0,0), (-3,0,0)}.
```

Those two sites lie on the origin-lock axis at Euclidean radius 3. Their only
in-host neighbors are `(2,0,0)` and `(-2,0,0)`, whose unique earliest locks
are `+e_1` and `-e_1` respectively, so the remaining axial step is parallel
to the lock and is not allowed. Uniqueness is not required elsewhere: the
site `(1,1,1)` forms at tick `2` with two earliest locks `{+e_1, +e_3}`.

The formed nonzero set is therefore the 120-element set

```text
B_3(0) \ { (0,0,0), (3,0,0), (-3,0,0) }.
```

The formation ticks on that set, grouped by tick, are:

Tick `0` (1 site):

```text
(0,1,0)
```

Tick `1` (7 sites):

```text
(-1,1,0), (0,-1,0), (0,0,-1), (0,0,1),
(0,1,-1), (0,1,1), (1,1,0)
```

Tick `2` (18 sites):

```text
(-1,-1,0), (-1,0,-1), (-1,0,0), (-1,0,1),
(-1,1,-1), (-1,1,1), (-1,2,0), (0,-1,-1),
(0,-1,1), (0,2,-1), (0,2,1), (1,-1,0),
(1,0,-1), (1,0,0), (1,0,1), (1,1,-1),
(1,1,1), (1,2,0)
```

Tick `3` (33 sites):

```text
(-2,0,0), (-2,1,-1), (-2,1,1), (-2,2,0),
(-1,-2,0), (-1,-1,-1), (-1,-1,1), (-1,0,-2),
(-1,0,2), (-1,1,-2), (-1,1,2), (-1,2,-1),
(-1,2,1), (0,-2,-1), (0,-2,1), (0,-1,-2),
(0,-1,2), (0,2,-2), (0,2,0), (0,2,2),
(1,-2,0), (1,-1,-1), (1,-1,1), (1,0,-2),
(1,0,2), (1,1,-2), (1,1,2), (1,2,-1),
(1,2,1), (2,0,0), (2,1,-1), (2,1,1),
(2,2,0)
```

Tick `4` (46 sites):

```text
(-2,-2,0), (-2,-1,-1), (-2,-1,0), (-2,-1,1),
(-2,0,-2), (-2,0,-1), (-2,0,1), (-2,0,2),
(-2,1,-2), (-2,1,0), (-2,1,2), (-2,2,-1),
(-2,2,1), (-1,-2,-1), (-1,-2,1), (-1,-1,-2),
(-1,-1,2), (-1,2,-2), (-1,2,2), (0,-2,-2),
(0,-2,0), (0,-2,2), (0,0,-2), (0,0,2),
(0,1,-2), (0,1,2), (0,3,0), (1,-2,-1),
(1,-2,1), (1,-1,-2), (1,-1,2), (1,2,-2),
(1,2,2), (2,-2,0), (2,-1,-1), (2,-1,0),
(2,-1,1), (2,0,-2), (2,0,-1), (2,0,1),
(2,0,2), (2,1,-2), (2,1,0), (2,1,2),
(2,2,-1), (2,2,1)
```

Tick `5` (15 sites):

```text
(-2,-2,-1), (-2,-2,1), (-2,-1,-2), (-2,-1,2),
(-1,-2,-2), (-1,-2,2), (0,-3,0), (0,0,-3),
(0,0,3), (1,-2,-2), (1,-2,2), (2,-2,-1),
(2,-2,1), (2,-1,-2), (2,-1,2)
```

The tick histogram on the formed nonzero set is therefore

```text
(t, count) = (0,1), (1,7), (2,18), (3,33), (4,46), (5,15).
```

These ticks are not hop counts: the hop count of `(1,0,0)` is `1`, while
`t(1,0,0)=2`. They are also not the one-site-origin ticks of the same
perp-step incoming-lock process, which would give `t(1,0,0)=3`.

## Theorem 2 — var(|x|_2/t) on the formed nonzero set

Let `|x|_2` denote the Euclidean length `sqrt(x·x)`. The compared statistic
is the population variance of `|x|_2/t` on formed nonzero sites. The seed
site `(0,1,0)` has `t=0`, so `|x|_2/t` is not defined there; it is excluded
for the same reason the origin is excluded. The variance set is therefore the
119 formed nonzero sites with positive formation tick. Write `N=119`. Then

```text
var(|x|_2/t) = (1/N) Σ (|x|_2/t(x) - mean)^2,
```

with `mean = (1/N) Σ |x|_2/t(x)`, the sums running over those 119 sites.
Equivalently, `var = Q - mean^2` where the second moment

```text
Q = (1/N) Σ (x·x) / t(x)^2
```

is rational. Direct enumeration of the Theorem 1 positive ticks gives

```text
Q = 49223/85680.
```

The occupancy of pairs `(x·x, t)` on the 119 sites is

```text
(1,1):3, (1,2):2, (2,1):4, (2,2):8, (3,2):4, (3,3):4, (4,3):3, (4,4):3,
(5,2):4, (5,3):10, (5,4):10, (6,3):12, (6,4):12, (8,3):4, (8,4):8,
(9,4):13, (9,5):15.
```

The tick histogram on the variance set is

```text
(t, count) = (1,7), (2,18), (3,33), (4,46), (5,15).
```

Expanding `mean^2` over square-free kernels yields the exact value

```text
var = 287192/637245
    - (130/2023) sqrt(2)
    - (251/6069) sqrt(3)
    - (235/8092) sqrt(5)
    - (8375/254898) sqrt(6)
    - (2068/127449) sqrt(10)
    - (470/127449) sqrt(15)
    - (47/6069) sqrt(30).
```

Truncated to 18 decimal digits this is

```text
var(|x|_2/t) = 0.034735087770962977.
```

The two unformed sites are not assigned a tick and are not included. The
origin and the seed site `(0,1,0)` are excluded because `t=0`.

## Theorem 3 — displayed, not adopted

The Theorem 2 number is displayed, not adopted. Displayed, not adopted.

Do not write the variance, the formation tick, or the perp-step incoming-lock
process into Admissibility. The current admissibility rule remains the quoted
nearest-neighbor distribution constraint.

Do not attach L1. No formation law, occupancy member, or locked-set filling
rule is identified with this variance.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify `t` with a hop count.
- It does not enlarge the host beyond `B_3(0)`.
- It does not score unformed sites or `t=0` sites.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.

## Primary runner

The paired runner builds `B_3(0)`, seeds the two-record set `{0,(0,1,0)}` at
tick `0` with locks `+e_1` and `+e_2`, runs the perp-step incoming-lock
process, enumerates the formed nonzero set and ticks, and recomputes `Q` and
`var(|x|_2/t)` on the positive-tick subset. It also checks that dropping the
perpendicular rule forms the two origin-axis radius-3 sites, and that a
1-site origin seed is a different tick table. No runner cache is written.
