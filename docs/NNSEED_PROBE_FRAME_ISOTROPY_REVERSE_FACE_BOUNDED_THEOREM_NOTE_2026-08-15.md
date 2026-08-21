---
claim_id: nnseed_probe_frame_isotropy_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "nnseed formation-tick reverse and face in z and y probe frames on Euclidean B_3(0) are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_probe_frame_isotropy_reverse_face_2026_08_15.py
---

# Nnseed Formation-Tick Reverse And Face In z And y Probe Frames On Euclidean B_3(0)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed formation-tick reverse and face in the z and y probe
frames on the finite Euclidean host `B_3(0)`, for the two-site nnseed process
with seed `{0,(0,1,0)}` locking `+e_1` and `+e_2`. Uniqueness is not required.
The inequalities are displayed, not adopted. This note does not write into
Admissibility and does not identify the tick with nearest-neighbor hop count.
The reported ticks are the z-frame and y-frame probes, not a reprint of the
x-frame probes `(1,0,0)`, `(2,0,0)`, `(1,1,0)`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_probe_frame_isotropy_reverse_face_2026_08_15.py`](../scripts/nnseed_probe_frame_isotropy_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, and the Record
  sentences that records form and that a present record locks exactly one
  admissible local possibility.

Everything after that quoted input is defined here as a finite displayed
process on Euclidean `B_3(0)`. The lock letters below are unit
nearest-neighbor steps, not a new axiom alphabet.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite formation on Euclidean B_3(0) reports z-frame and y-frame formation ticks and the reverse and face comparisons; uniqueness is not claimed and the inequalities are not adopted."
trace_class: upstream_support
target_claim_id: formation_tick_z_y_probe_frame_reverse_face_display
target_blocker_text: "display formation-tick reverse and face in z and y probe frames without adopting the inequalities or an Admissibility edit"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep the inequalities displayed only; do not write them into Admissibility and do not require unique incoming locks."
conditional_surface_status: "exact on Euclidean B_3(0) for the declared two-site nnseed perp-step incoming-lock process"
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

Seed at tick `0`: the origin is recorded with lock letter `+e_1`, and
`(0,1,0)` is recorded with lock letter `+e_2`.

From a recorded site `p` with lock `L(p)=±e_i`, a six-neighbor step `s in NN`
to `q=p+s` is allowed if and only if `s` is perpendicular to `e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms at tick `t(p)+1` and locks the incoming step `s` (the unit vector from
`p` to `q`). If several allowed parents reach `q` at the same earliest tick,
each such incoming step is recorded as a possible lock. Uniqueness is not
required. A later parent does not re-form `q`. The already-recorded seed site
`(0,1,0)` is not re-formed by a later step from the origin.

The tick `t` is this formation tick. It is not a weighted path table.

Admissibility is not edited. The process is a displayed Record-like lock on
the six-letter step alphabet, not a derivation of a physical rate.

z-probes:

```text
A_z = (0,0,1),  B = (1,1,1),  C_z = (0,0,2),  D_z = (0,1,1).
```

y-probes:

```text
A_y = (0,1,0),  B = (1,1,1),  C_y = (0,2,0),  D_y = (1,1,0).
```

`A_y` is a seed site, so `t(A_y)=0` by the seed rule. Reverse and face are
the integer comparisons

```text
reverse:  3 t(A)^2 > t(B)^2,
face:     t(C)^2 > 2 t(D)^2,
```

in each named frame, or undefined if a needed tick is absent.

## Theorem 1 — formation ticks of the z-probes and y-probes

All eight named probe evaluations are defined on Euclidean `B_3(0)`:

```text
t(A_z)=t(0,0,1)=1,
t(B)=t(1,1,1)=2,
t(C_z)=t(0,0,2)=4,
t(D_z)=t(0,1,1)=1,
t(A_y)=t(0,1,0)=0,
t(C_y)=t(0,2,0)=3,
t(D_y)=t(1,1,0)=1.
```

Witness paths (not claimed unique):

- Origin `-- +e_3 -->` `(0,0,1)` at tick `1`, lock `+e_3`. The origin lock
  `+e_1` is perpendicular to `+e_3`.
- Seed `(0,1,0)` `-- +e_3 -->` `(0,1,1)` at tick `1`, lock `+e_3`. The seed
  lock `+e_2` is perpendicular to `+e_3`.
- Seed `(0,1,0)` `-- +e_1 -->` `(1,1,0)` at tick `1`, lock `+e_1`.
- `(0,1,1)` `-- +e_1 -->` `(1,1,1)` at tick `2`, lock `+e_1`. A second
  earliest parent is `(1,1,0) -- +e_3 --> (1,1,1)` at the same tick, lock
  `+e_3`. So uniqueness is not required at `B`.
- `(0,0,1)` cannot step by `+e_3` to `(0,0,2)` because that step is parallel
  to its lock. One earliest route is
  `(0,0,1) -- +e_1 --> (1,0,1)` at tick `2`, lock `+e_1`;
  `(1,0,1) -- +e_3 --> (1,0,2)` at tick `3`, lock `+e_3`;
  `(1,0,2) -- -e_1 --> (0,0,2)` at tick `4`, lock `-e_1`. Other earliest
  parents give locks `+e_1` and `+e_2` at the same tick.
- Seed `(0,1,0)` cannot step by `+e_2` to `(0,2,0)` because that step is
  parallel to the seed lock. One earliest route is
  `(0,1,0) -- +e_1 --> (1,1,0)` at tick `1`;
  `(1,1,0) -- +e_2 --> (1,2,0)` at tick `2`, lock `+e_2`;
  `(1,2,0) -- -e_1 --> (0,2,0)` at tick `3`, lock `-e_1`. Other earliest
  parents give four locks at that tick.

These values are not a reprint of the x-frame probes `(1,0,0)`, `(2,0,0)`,
`(1,1,0)`: the z-axis pair is `(0,0,1)` and `(0,0,2)`, and `t(A_z)=1` is not
the axial x-tick of this same process.

## Theorem 2 — z-reverse and z-face

All four z-frame ticks in Theorem 1 are defined, so both z-frame comparisons
are defined. Direct integer arithmetic gives

```text
3 t(A_z)^2 = 3 * 1 = 3,
t(B)^2 = 4,
3 > 4 is false,
```

and

```text
t(C_z)^2 = 16,
2 t(D_z)^2 = 2 * 1 = 2,
16 > 2.
```

Thus on this host the z-frame display is

```text
z-reverse fails:  3 t(A_z)^2 > t(B)^2  is false,
z-face holds:     t(C_z)^2 > 2 t(D_z)^2.
```

They are displayed, not adopted. They are not written into Admissibility.

## Theorem 3 — y-reverse and y-face

All four y-frame ticks in Theorem 1 exist, including the seed tick
`t(A_y)=0`, so both y-frame comparisons are defined. Direct integer
arithmetic gives

```text
3 t(A_y)^2 = 3 * 0 = 0,
t(B)^2 = 4,
0 > 4 is false,
```

and

```text
t(C_y)^2 = 9,
2 t(D_y)^2 = 2 * 1 = 2,
9 > 2.
```

Thus on this host the y-frame display is

```text
y-reverse fails:  3 t(A_y)^2 > t(B)^2  is false,
y-face holds:     t(C_y)^2 > 2 t(D_y)^2.
```

They are displayed, not adopted. They are not written into Admissibility.
The y-frame is reported because every named y-probe forms; it is not adopted
as a selection rule.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify `t` with a hop count or with a shortest-path cost.
- It does not enlarge the host beyond Euclidean `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not reprint the x-frame probe ticks as the theorem content.
- It does not supply a physical rate or a continuum kernel.

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site nnseed
perp-step incoming-lock process from the seed `{0,(0,1,0)}` with locks
`+e_1/+e_2`, and checks Theorems 1--3 by direct enumeration. It also checks
that dropping the second seed changes the z-frame ticks, and that the z-frame
quadruples are not the x-frame probes. No runner cache is written.
