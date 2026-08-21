---
claim_id: opposite_lock_formation_tick_var_b3_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Arrival-speed variance of nsopp formation-tick on formed nonzero sites of B_3(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_formation_tick_var_b3_2026_08_15.py
---

# Opposite-Lock Formation-Tick Arrival-Speed Variance On Formed Nonzero Sites Of B_3(0)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed population variance of `|x|_2/t` on formed nonzero sites
of the finite host `B_3(0)` under the opposite-lock two-site perp-step
incoming-lock process with seed `{0,(0,1,0)}` already formed at tick `0` and
opposite locks `L(0)=+e_1`, `L(0,1,0)=−e_1`. Cardinality-of-seed, not a 1-site clone. Uniqueness is not required. The variance is displayed, not
adopted. This note does not write the variance into Admissibility. This is
not a reprint of the perp two-site formation-tick variance.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_formation_tick_var_b3_2026_08_15.py`](../scripts/opposite_lock_formation_tick_var_b3_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, and the Record
  sentences that records form and that a present record locks exactly one
  admissible local possibility.

Everything after that quoted input is defined here as a finite displayed
process on `B_3(0)`. The lock letters below are unit nearest-neighbor steps,
not a new axiom alphabet. The quadratic `|x|_2^2=x·x` is the Euclidean
square already used to name the host ball; it is not a second length
attached to the process.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite population variance of |x|_2/t on formed nonzero sites of B_3(0) under the opposite-lock two-site process; uniqueness is not claimed and the variance is not adopted."
trace_class: upstream_support
target_claim_id: opposite_lock_formation_tick_var_b3
target_blocker_text: "display var(|x|_2/t) on formed nonzero B_3(0) sites under the opposite-lock two-site seed without adopting a speed or reprinting the perp two-site variance"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep the formed-nonzero ticks and the arrival-speed variance displayed only; do not write the variance into Admissibility."
conditional_surface_status: "exact on B_3(0) for the declared perp-step incoming-lock process with two-site seed {0,(0,1,0)} and locks +e_1/−e_1"
hypothetical_axiom_status: "no edit"
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
`(0,1,0)` is already recorded with lock letter `−e_1`. Both sites are already
formed. The connecting step `+e_2` is perpendicular to both seed locks. This
is a two-record opposite-lock set, not a 1-site origin letter with a cloned
second copy of the same lock.

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
a weighted path table.

On each formed nonzero site `x` with `t(x)>0`, the displayed arrival speed
is `|x|_2/t(x)` with `|x|_2=sqrt(x·x)`. The origin is formed and is
excluded because it is the zero site. The second seed `(0,1,0)` is formed
and nonzero, so it belongs to the Theorem 1 set, but `|x|_2/t` is undefined
at `t=0`, so that one site is excluded from the Theorem 2 average.

The compared statistic on the remaining formed nonzero sites is the
population variance

```text
var(|x|_2/t) = (1/N) sum (|x|_2/t(x) - mean)^2,
```

with `mean=(1/N) sum |x|_2/t(x)`. Equivalently, `var = Q - mean^2` where the
second moment `Q=(1/N) sum |x|_2^2 / t(x)^2` is rational.

Admissibility is not edited. The variance is a displayed pairing of the
formation tick with the host Euclidean length. It is not written into
Admissibility.

## Theorem 1 — formed nonzero sites and ticks

The host `B_3(0)` has 123 lattice sites. The origin is formed at tick `0`.
The second seed `(0,1,0)` is formed at tick `0`. Exactly three host sites
remain unformed: `(3,0,0)`, `(-3,0,0)`, and `(0,3,0)`. Every other host site
forms. Therefore the formed nonzero set has cardinality

```text
N_formed nonzero = 119.
```

The two sites `(±3,0,0)` lie on the origin lock axis at Euclidean square `9`.
From the origin, axial steps `±e_1` are parallel to the seed lock `+e_1` and
are not allowed. From the second seed the same axial steps are parallel to
`−e_1` and are not allowed. The neighboring sites that would feed `(±3,0,0)`
by a remaining perpendicular step lie outside `B_3(0)`.

The third unformed site is `(0,3,0)`. Both seed locks lie on the `e_1` axis,
so the allowed-step plane at `(0,1,0)` includes `+e_2`. That site therefore
forms `(0,2,0)` at tick `1` with incoming lock `+e_2`. The only neighbor of
`(0,3,0)` that lies in `B_3(0)` is `(0,2,0)`, and the connecting step `+e_2`
is parallel to that lock, so it is not allowed.

Formation ticks of the 119 formed nonzero sites, grouped by tick, are

```text
t=0 (1): (0,1,0)
t=1 (6): (0,-1,0), (0,0,-1), (0,0,1), (0,1,-1), (0,1,1), (0,2,0)
t=2 (16): (-1,-1,0), (-1,0,-1), (-1,0,1), (-1,1,-1), (-1,1,1), (-1,2,0),
          (0,-1,-1), (0,-1,1), (0,2,-1), (0,2,1), (1,-1,0), (1,0,-1),
          (1,0,1), (1,1,-1), (1,1,1), (1,2,0)
t=3 (28): (-1,-2,0), (-1,-1,-1), (-1,-1,1), (-1,0,-2), (-1,0,0), (-1,0,2),
          (-1,1,-2), (-1,1,0), (-1,1,2), (-1,2,-1), (-1,2,1), (0,-2,-1),
          (0,-2,1), (0,-1,-2), (0,-1,2), (0,2,-2), (0,2,2), (1,-2,0),
          (1,-1,-1), (1,-1,1), (1,0,-2), (1,0,0), (1,0,2), (1,1,-2),
          (1,1,0), (1,1,2), (1,2,-1), (1,2,1)
t=4 (41): (-2,-2,0), (-2,-1,-1), (-2,-1,1), (-2,0,-2), (-2,0,0), (-2,0,2),
          (-2,1,-2), (-2,1,0), (-2,1,2), (-2,2,-1), (-2,2,1), (-1,-2,-1),
          (-1,-2,1), (-1,-1,-2), (-1,-1,2), (-1,2,-2), (-1,2,2), (0,-2,-2),
          (0,-2,0), (0,-2,2), (0,0,-2), (0,0,2), (0,1,-2), (0,1,2),
          (1,-2,-1), (1,-2,1), (1,-1,-2), (1,-1,2), (1,2,-2), (1,2,2),
          (2,-2,0), (2,-1,-1), (2,-1,1), (2,0,-2), (2,0,0), (2,0,2),
          (2,1,-2), (2,1,0), (2,1,2), (2,2,-1), (2,2,1)
t=5 (27): (-2,-2,-1), (-2,-2,1), (-2,-1,-2), (-2,-1,0), (-2,-1,2),
          (-2,0,-1), (-2,0,1), (-2,1,-1), (-2,1,1), (-2,2,0),
          (-1,-2,-2), (-1,-2,2), (0,-3,0), (0,0,-3), (0,0,3),
          (1,-2,-2), (1,-2,2), (2,-2,-1), (2,-2,1), (2,-1,-2),
          (2,-1,0), (2,-1,2), (2,0,-1), (2,0,1), (2,1,-1),
          (2,1,1), (2,2,0)
```

The integer counts `1+6+16+28+41+27=119` partition the Theorem 1 set.
The integer 119 is a cardinality on this two-site opposite-lock process.
A 1-site origin seed on the same host is a different formation history.
The perp two-site seed `+e_1/+e_2` forms 120 nonzero sites and leaves
`(0,3,0)` formed, so this set is not that census.

## Theorem 2 — population variance of `|x|_2/t`

Exactly 118 of the 119 formed nonzero sites have `t>0`. On that set the
exact second moment is rational,

```text
Q = 3817/7080.
```

The mean is not a rational. It is the exact linear combination

```text
mean = 157/708 + (32/295) sqrt(2) + (5/177) sqrt(3)
       + (113/1770) sqrt(5) + (97/1770) sqrt(6).
```

The population variance `Q - mean^2` is therefore not a rational. The
exact value is

```text
var = (5333757 - 719280 sqrt(2) - 454984 sqrt(3) - 354820 sqrt(5)
       - 381380 sqrt(6) - 173568 sqrt(10) - 45200 sqrt(15)
       - 87688 sqrt(30)) / 12531600.
```

Truncated to 18 decimal digits that value is

```text
var = 0.047614192437711682.
```

This is the arrival-speed variance of the opposite-lock two-site
formation-tick process on formed nonzero sites of `B_3(0)`. It is not
the perp two-site seed `+e_1/+e_2` variance: that process forms 120
nonzero sites, includes `(0,3,0)`, and has a different second moment
`49223/85680`.

## Theorem 3 — displayed, not adopted

The variance is displayed, not adopted. It is not written into Admissibility.

The current admissibility rule remains the quoted nearest-neighbor
distribution constraint. The formation tick and the Euclidean length are
theorem-domain data on `B_3(0)`, not a replacement of that axiom.

This note does not attach a formation member. No occupancy filling rule
is identified with the reported variance.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify `t` with a hop count.
- It does not enlarge the host beyond `B_3(0)`.
- It does not replace the two-site seed by a 1-site origin letter.
- It is not a reprint of the perp two-site formation-tick variance.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not write the variance into Admissibility.
- It does not supply a physical rate or a continuum kernel.

## Current premise boundary

The Lattice, Qubit, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

The Admissibility reading note says the distribution concerns which possibility
a forming record locks, conditional on formation at that site; it does not
supply the formation site, probability, or rate.

This display uses Lattice to name `B_3(0)`. It uses Qubit only as the algebra
of the local possibility domain. It uses Record only as a boundary: a present
lock is content. It does not rewrite Admissibility. The opposite-lock two-site
process, the formed-nonzero ticks, and the arrival-speed variance are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| formed nonzero sites and ticks | Theorem 1; cardinality 119 |
| `var(|x|_2/t)` | Theorem 2; exact non-rational on 118 sites with `t>0` |
| unique incoming lock | not required |
| perp two-site variance reprint | not this seed |
| 1-site origin clone | not this seed |
| variance as Admissibility content | not adopted |
| formation site / probability / rate | open |

## Primary runner

The paired runner builds `B_3(0)`, seeds the two-record set `{0,(0,1,0)}` at
tick `0` with locks `+e_1` and `−e_1`, runs the perp-step incoming-lock
process, enumerates formed nonzero ticks, and checks Theorems 1--3 by exact
population variance of `|x|_2/t`. It also checks that a 1-site origin seed
on the same host is a different speed set, that the perp two-site seed
`+e_1/+e_2` is a different variance, that dropping the perpendicular rule
changes the formed-nonzero count, and that `|x|_2^2` is the Euclidean
square. No runner cache is written.
