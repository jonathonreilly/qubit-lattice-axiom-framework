---
claim_id: perpnn_seed_minus_e1_x_probe_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Perp-step incoming-lock formation-tick reverse and face at k=1 on B_3(0) with seed lock −e_1 and +x probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/perpnn_seed_minus_e1_x_probe_reverse_face_2026_08_15.py
---

# Perp-Step Incoming-Lock Formation With Seed Lock −e_1 And +x Probes On B_3(0)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed formation-tick reverse and face at `k=1` on the finite
host `B_3(0)`, with lock alphabet `{±e_i}`, perp-step formation, incoming-step
lock, seed lock `(0)=−e_1` (opposite the reverse axis), and the same `+x`
probes as the `+e_1` seed display. Uniqueness is not required. The
inequalities are displayed, not adopted. This note does not write into
Admissibility and does not identify the tick with nearest-neighbor hop count.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/perpnn_seed_minus_e1_x_probe_reverse_face_2026_08_15.py`](../scripts/perpnn_seed_minus_e1_x_probe_reverse_face_2026_08_15.py)

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
claim_type_reason: "Exact finite formation on B_3(0) reports the tick-1 6-mask, the +x probe ticks, and the k=1 reverse and face comparisons for seed lock −e_1; uniqueness is not claimed and the inequalities are not adopted."
trace_class: upstream_support
target_claim_id: formation_tick_k1_reverse_face_display
target_blocker_text: "display formation-tick reverse and face at k=1 for seed lock −e_1 without adopting a hop-count identification or an Admissibility edit"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep the inequalities displayed only; do not write them into Admissibility and do not require unique incoming locks."
conditional_surface_status: "exact on B_3(0) for the declared perp-step incoming-lock process with seed lock −e_1 and +x probes"
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

Seed: the origin is recorded at tick `0` with lock letter `−e_1`. This letter
is opposite the reverse-axis probe direction `+e_1`.

From a recorded site `p` with lock `L(p)=±e_i`, a six-neighbor step `s in NN`
to `q=p+s` is allowed if and only if `s` is perpendicular to `e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms at tick `t(p)+1` and locks the incoming step `s` (the unit vector from
`p` to `q`). If several allowed parents reach `q` at the same earliest tick,
each such incoming step is recorded as a possible lock. Uniqueness is not
required. A later parent does not re-form `q`.

The tick `t` is this formation tick. It is not computed by a shortest-path
search and is not a weighted path table.

Admissibility is not edited. The process is a displayed Record-like lock on
the six-letter step alphabet, not a derivation of a physical rate.

The `k=1` probes remain on `+x`:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

## Theorem 1 — tick-1 6-mask and +x probe ticks

Order the six neighbors of the origin as

```text
(+e_1, -e_1, +e_2, -e_2, +e_3, -e_3).
```

The origin lock is `−e_1`, so both axial steps `±e_1` are parallel to `e_1`
and are not allowed. The four steps `±e_2, ±e_3` are perpendicular to `e_1`
and land in `B_3(0)`. Those four neighbors therefore form at tick `1` and
lock the incoming step:

```text
t(0,1,0)=1,  L includes +e_2,
t(0,-1,0)=1, L includes -e_2,
t(0,0,1)=1,  L includes +e_3,
t(0,0,-1)=1, L includes -e_3.
```

The axial neighbors do not form at tick `1`:

```text
t(1,0,0) != 1,  t(-1,0,0) != 1.
```

The tick-1 6-mask is therefore

```text
tick-1 6-mask, order (+e_1,-e_1,+e_2,-e_2,+e_3,-e_3): (0,0,1,1,1,1).
```

This is the four-site perpendicular mask of the seed axis. The seed letter
is `−e_1`, not `+e_1`; the formed tick-1 set is still the perpendicular
plane of `e_1`.

On `B_3(0)` the earliest formation ticks of the four `+x` probes are
defined and equal to

```text
t(A)=t(1,0,0)=3,
t(B)=t(1,1,1)=3,
t(C)=t(2,0,0)=4,
t(D)=t(1,1,0)=2.
```

Witness paths (not claimed unique):

- `(0,0,0) --+e_2--> (0,1,0)` at tick `1`, lock `+e_2`; then
  `(0,1,0) --+e_1--> (1,1,0)` at tick `2`, lock `+e_1`.
- `(1,1,0) --+e_3--> (1,1,1)` at tick `3`, lock `+e_3`.
- `(1,1,0)` cannot step by `+e_1` because that step is parallel to its lock;
  `(1,0,0)` instead forms from `(1,1,0)` by `-e_2` at tick `3`. Other
  earliest parents give locks `±e_2` and `±e_3` at the same tick.
- Every possible earliest lock at `(1,0,0)` is perpendicular to `+e_1`, so
  `(1,0,0) --+e_1--> (2,0,0)` at tick `4`, lock `+e_1`.

The four possible earliest locks at `(1,0,0)` show that uniqueness is not
required for the tick to be defined.

These values are not nearest-neighbor hop counts: the hop count of `(1,0,0)`
is `1`, while `t(1,0,0)=3`.

## Theorem 2 — displayed k=1 reverse

All of `t(A)` and `t(B)` are defined, so the reverse comparison is defined.
Direct integer arithmetic gives

```text
3 t(A)^2 = 3 * 9 = 27,
t(B)^2 = 9,
27 > 9.
```

Thus the displayed reverse inequality holds on this host:

```text
3 t(A)^2 > t(B)^2  holds.
```

It is displayed, not adopted. It is not written into Admissibility.

## Theorem 3 — displayed k=1 face

All of `t(C)` and `t(D)` are defined, so the face comparison is defined.
Direct integer arithmetic gives

```text
t(C)^2 = 16,
2 t(D)^2 = 2 * 4 = 8,
16 > 8.
```

Thus the displayed face inequality holds on this host:

```text
t(C)^2 > 2 t(D)^2  holds.
```

It is displayed, not adopted. It is not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify `t` with a hop count or with a shortest-path cost.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.
- It does not adopt reverse or face as an Admissibility constraint.

## Primary runner

The paired runner builds `B_3(0)`, runs the perp-step incoming-lock process
from seed lock `−e_1`, and checks Theorems 1--3 by direct enumeration. It also
checks that a parallel-only mutation recovers an axial tick-1 mask and that
dropping the perpendicular rule forms all six neighbors at tick `1`. No runner cache is written.
