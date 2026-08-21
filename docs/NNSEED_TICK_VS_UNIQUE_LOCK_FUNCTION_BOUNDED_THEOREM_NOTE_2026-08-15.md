---
claim_id: nnseed_tick_vs_unique_lock_function_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Whether formation-tick is a function of unique earliest incoming lock on the nnseed unique-lock sites of B_3(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_tick_vs_unique_lock_function_2026_08_15.py
---

# Formation-Tick Versus Unique Lock On The Two-Site Seed In B_3(0)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed question whether formation-tick is a function of the
unique earliest incoming lock on unique-lock sites of the two-site-seed
perp-step incoming-lock process in the finite Euclidean host `B_3(0)`, with
lock alphabet `{±e_i}` and seed `{0,(0,1,0)}` already formed at tick `0`
with locks `L(0)=+e_1` and `L(0,1,0)=+e_2`. Uniqueness is not required of
the process. The map and the witness pair are displayed, not adopted. This
note does not write t or L into Admissibility.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_tick_vs_unique_lock_function_2026_08_15.py`](../scripts/nnseed_tick_vs_unique_lock_function_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, and the Record
  sentences that records form, that a present record locks exactly one
  admissible local possibility, and that a readout value is determined by
  record content alone.

Everything after that quoted input is defined here as a finite displayed
process on `B_3(0)`. The lock letters below are unit nearest-neighbor steps,
not a new axiom alphabet.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite formation on Euclidean B_3(0) with two-site seed {0,(0,1,0)} reports the unique-lock map x |-> (L(x), t(x)) and one witness that t is not a function of L; uniqueness is not required of the process and the map is not adopted."
trace_class: upstream_support
target_claim_id: nnseed_tick_vs_unique_lock_function_display
target_blocker_text: "display whether formation-tick is a function of unique earliest incoming lock on the two-site-seed unique-lock sites of B_3(0) without adopting t or L and without an Admissibility edit"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep the unique-lock map displayed only; do not write t or L into Admissibility and do not require unique incoming locks of the process."
conditional_surface_status: "exact on Euclidean B_3(0) for the declared perp-step incoming-lock process with two-site seed {0,(0,1,0)} and locks +e_1/+e_2"
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

No larger host is used. The host is this Euclidean ball, not a coordinate-sum
ball of radius 3.

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

The earliest incoming lock at a formed site is that set of allowed incoming
steps. Unique means the set has size 1. Write `L(x)` for that unique letter.
The domain is those unique-lock formed sites in `B_3(0)`, including both
seeds, with `L(0)=+e_1`, `t(0)=0`, `L(0,1,0)=+e_2`, and `t(0,1,0)=0`.

The tick `t` is this formation tick. It is not computed by a shortest-path
search and is not a weighted path table.

Admissibility is not edited. The process is a displayed Record-like lock on
the six-letter step alphabet.

## Theorem 1 — unique-lock set and map

Direct enumeration of the perp-step incoming-lock process on Euclidean
`B_3(0)` with the two-site seed gives 123 host sites, of which 121 form.
The unique-lock formed sites, including both seeds, are the 61 sites whose
lock set has size 1. Uniqueness is not required of the process: `(1,1,1)`
forms at tick `2` with two earliest incoming locks `{+e_1,+e_3}` and is
excluded from the domain.

The Euclidean host includes `(2,2,0)` with `n·n=8<=9`. That site is in the
unique-lock set.

The map `x ↦ (L(x), t(x))` on those unique-lock sites is

```text
unique-lock sites N=61
L=+e_1 (14): (0,0,0):0, (1,-1,0):2, (1,0,-1):2, (1,0,1):2, (1,1,0):1,
(2,-2,0):4, (2,-1,-1):4, (2,-1,1):4, (2,0,-2):4, (2,0,0):3, (2,0,2):4,
(2,1,-1):3, (2,1,1):3, (2,2,0):3
L=-e_1 (13): (-2,-2,0):4, (-2,-1,-1):4, (-2,-1,1):4, (-2,0,-2):4,
(-2,0,0):3, (-2,0,2):4, (-2,1,-1):3, (-2,1,1):3, (-2,2,0):3,
(-1,-1,0):2, (-1,0,-1):2, (-1,0,1):2, (-1,1,0):1
L=+e_2 (6): (-1,2,0):2, (0,1,0):0, (0,2,-1):2, (0,2,1):2, (0,3,0):4,
(1,2,0):2
L=-e_2 (10): (-2,-1,0):4, (-1,-2,0):3, (-1,0,0):2, (0,-3,0):5,
(0,-2,-1):3, (0,-2,1):3, (0,-1,0):1, (1,-2,0):3, (1,0,0):2, (2,-1,0):4
L=+e_3 (9): (-1,0,2):3, (-1,1,2):3, (0,-1,2):3, (0,0,1):1, (0,0,3):5,
(0,1,1):1, (0,2,2):3, (1,0,2):3, (1,1,2):3
L=-e_3 (9): (-1,0,-2):3, (-1,1,-2):3, (0,-1,-2):3, (0,0,-3):5,
(0,0,-1):1, (0,1,-1):1, (0,2,-2):3, (1,0,-2):3, (1,1,-2):3
```

This is the unique-lock map. It is not a pair census.

## Theorem 2 — t is not a function of L

There exist unique-lock sites `x≠y` with `L(x)=L(y)` and `t(x)≠t(y)`. One
witness pair is

```text
x=(0,1,0), y=(0,3,0),
L(x)=L(y)=+e_2,
t(x)=0, t(y)=4.
```

Both sites lie in `B_3(0)` and each has a unique earliest incoming lock
`+e_2`. Therefore t is not a function of L on this sample.

The same conclusion holds after dropping both seeds: `+e_2` still occurs at
ticks `2` and `4`. The failure is not an artifact of counting `L(0)=+e_1`
or `L(0,1,0)=+e_2`.

A second pair with the same letter and distinct ticks, neither a seed, is
`x=(0,-1,0)` with `t=1` and `y=(0,-3,0)` with `t=5`, both unique-lock
`-e_2`.

## Theorem 3 — displayed, not adopted

The unique-lock map and the witness that t is not a function of L are
displayed, not adopted. They are not written into Admissibility.
Do not write t or L into Admissibility.

Record readout is content-alone: a readout value is determined by record
content alone. On this sample the unique lock letter is the displayed
record content, and formation-tick is not a function of that letter.
Therefore formation-tick cannot be recovered from Record content-alone.

## What this note does not claim

- It does not require unique incoming locks of the process.
- It does not adopt t or L as a field identification.
- It does not write t or L into Admissibility.
- It does not identify `t` with a hop count or with a shortest-path cost.
- It does not enlarge the host beyond `B_3(0)`.
- It does not replace the Euclidean host by a coordinate-sum ball.
- It does not replace the two-site seed by a 1-site origin letter.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It is not a pair census of unique locks.

## Primary runner

The paired runner builds Euclidean `B_3(0)`, seeds the two-record set
`{0,(0,1,0)}` at tick `0` with locks `+e_1` and `+e_2`, runs the perp-step
incoming-lock process, collects unique-lock sites including both seeds,
writes the map `x ↦ (L(x), t(x))`, and searches for a witness pair with the
same letter and distinct ticks. No runner cache is written.
