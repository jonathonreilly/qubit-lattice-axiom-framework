---
claim_id: perpnn_unique_lock_inversion_parity_b3_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Inversion parity of unique earliest incoming locks on formed pairs {x,−x} in B_3(0) under perpnn is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/perpnn_unique_lock_inversion_parity_b3_2026_08_15.py
---

# Unique-Lock Inversion Parity On B_3(0)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed inversion parity of unique earliest incoming locks on
formed pairs `{x,−x}` in the finite host `B_3(0)`, under the perp-step
incoming-lock process with lock alphabet `{±e_i}` and seed lock `(0)=+e_1`.
Uniqueness is not required of the process. The unique-lock sample is
displayed, not adopted. This note does not write P or V−A into
Admissibility. This is not a 64-row occupancy census and is not a
four-probe letter census.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/perpnn_unique_lock_inversion_parity_b3_2026_08_15.py`](../scripts/perpnn_unique_lock_inversion_parity_b3_2026_08_15.py)

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
claim_type_reason: "Exact finite formation on B_3(0) reports inversion parity of unique earliest incoming locks on formed pairs; uniqueness is not required of the process and the parity is not adopted."
trace_class: upstream_support
target_claim_id: unique_lock_inversion_parity_b3_display
target_blocker_text: "display unique-lock inversion parity on formed pairs in B_3(0) without adopting P or V-A and without an Admissibility edit"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep the unique-lock sample displayed only; do not write P or V-A into Admissibility and do not require unique incoming locks of the process."
conditional_surface_status: "exact on B_3(0) for the declared perp-step incoming-lock process with seed lock +e_1"
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

Seed: the origin is recorded at tick `0` with lock letter `+e_1`.

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

The earliest incoming lock at a formed site is that set of allowed incoming
steps. Unique means the set has size 1. The origin lock is the seed, not an
incoming lock, and is excluded from the pairs below.

The tick `t` is this formation tick. It is not computed by a shortest-path
search and is not a weighted path table.

Admissibility is not edited. The process is a displayed Record-like lock on
the six-letter step alphabet.

## Pair convention

A formed pair is `{x,−x}` with `x ≠ 0`, both sites in `B_3(0)`, and both
formed. Each pair is counted once by taking the representative with

```text
x_1 > 0, or (x_1 = 0 and x_2 > 0), or (x_1 = x_2 = 0 and x_3 > 0).
```

A unique pair is a formed pair whose earliest incoming-lock sets both have
size 1. Write `L(x)` and `L(−x)` for those unique letters.

On a unique pair the displayed inversion classes are:

- odd: `L(−x) = −L(x)`
- even: `L(−x) = L(x)`
- other: neither

Odd here is the vector relation `L(−x)=−L(x)`. It is displayed, not adopted.
Do not write P or V−A into Admissibility.

## Theorem 1 — formed pairs and unique-lock pairs

Direct enumeration of the perp-step incoming-lock process on `B_3(0)` gives
123 host sites, of which 121 form. The two unformed sites are `±(3,0,0)`,
themselves an inversion pair, so they contribute no formed pair.

```text
N_pairs=60
N_unique=25
```

All 120 formed nonzero sites have formed inverses, hence 60 formed pairs.
Uniqueness is not required: 35 of the 60 formed pairs fail uniqueness at one
or both ends. Witness of a non-unique formed site: `(1,0,0)` has four
earliest incoming locks `{±e_2, ±e_3}`.

## Theorem 2 — inversion classes on unique pairs

On the 25 unique pairs the unique letters satisfy

```text
N_odd=25
N_even=0
N_other=0
```

Witness of an odd unique pair: `(0,1,0)` locks `+e_2` and `(0,−1,0)` locks
`−e_2`, so `L(−x)=−L(x)`.

## Theorem 3 — unique sample class

The unique sample is all-odd: every unique pair is odd, none even, none
other. The class is displayed, not adopted. It is not written into Admissibility.

## What this note does not claim

- It does not require unique incoming locks of the process.
- It does not adopt the all-odd sample as a field identification.
- It does not write P or V−A into Admissibility.
- It does not identify `t` with a hop count or with a shortest-path cost.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It is not a 64-row occupancy census and is not a four-probe letter census.

## Primary runner

The paired runner builds `B_3(0)`, runs the perp-step incoming-lock process
from the seed, counts formed pairs and unique pairs under the hemisphere
convention, and classifies unique pairs as odd, even, or other.
No runner cache is written.
