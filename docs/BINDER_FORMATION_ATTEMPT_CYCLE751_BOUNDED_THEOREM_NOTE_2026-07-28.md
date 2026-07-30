# Canonical controller net-endpoint-delta census and conditional Cycle-610 gate adapter

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle751_binder_formation_attempt_2026_07_28.py`](../scripts/frontier_cycle751_binder_formation_attempt_2026_07_28.py)

Independent reconstruction:

- [`frontier_cycle751_binder_independent_check_2026_07_28.py`](../scripts/frontier_cycle751_binder_independent_check_2026_07_28.py)

Pinned executable dependency:

- [`RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md`](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)

Current-main adapter boundary:

- [`CYCLE332_RECEIVER_SUCCESS_CYCLE610_GATE_ADAPTER_BOUNDED_THEOREM_NOTE_2026-07-30.md`](CYCLE332_RECEIVER_SUCCESS_CYCLE610_GATE_ADAPTER_BOUNDED_THEOREM_NOTE_2026-07-30.md)

Framework vocabulary boundary:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

Constitutional effect: none. This package changes no axiom, primitive,
registry, policy, audit result, or audit status. Its authority is `none`; the
bounded theorem remains unaudited until the independent audit lane evaluates
it.

## Exact supplied domain

For each

```text
n in {2, 5, 12},
```

the runner supplies the Cycle-719 genesis state, takes exactly `2*n` complete
controller orbits, and supplies direction `(1,0)` on even steps and `(0,1)` on
odd steps. Endpoint preparation is part of each supplied transition recipe.
For persistent state `s_t` and the post-orbit state `s_(t+1)`, define

```text
D_t = {wire w : s_t[w] != s_(t+1)[w]}
net_delta_nonempty(t) = 1 if D_t is nonempty, else 0.
```

`net_delta_nonempty` is a newly defined finite indicator. It is not imported
from the framework and is not assigned a physical interpretation here.

## Exact finite result

The complete endpoint-support cardinalities on the three supplied trajectories
are

```text
n=2:  [32, 22, 18, 17]
n=5:  [32, 22, 18, 17, 22, 19, 22, 19, 26, 21]
n=12: [32, 22, 18, 17, 22, 19, 22, 19, 26, 21, 22, 19,
       26, 21, 26, 21, 30, 22, 18, 17, 22, 19, 22, 19]
```

There are 38 transitions and 829 net endpoint bit changes in total, split as
`89 + 218 + 522`. The minimum support cardinality is 17 and the maximum is 32.
Consequently `net_delta_nonempty(t)=1` on every one of these 38 enumerated
rows.

This is a census of the named trajectories. It is not an exhaustion of all
controller states, direction schedules, gate-level touches, or Cycle-610 event
labels.

## Conditional lower-case API adapter

On the same 38 rows, use a fresh tick, sufficient bank capacity, and the
explicitly supplied Cycle-610 inputs

```text
certificate = actuality = admissibility = law_domain = 1.
```

Passing `net_delta_nonempty(t)` to the Cycle-610 method parameter named
`binder` produces byte-identical statuses and cell rows to passing the literal
`1`, because the finite census proves the indicator is `1` on each selected
row. A synthetic empty-support non-fixture control sends zero to that Boolean
parameter and returns `no_opportunity`; it only confirms that the API input is
live.

The lower-case method parameter is an executable API name. This theorem does
not identify `net_delta_nonempty` with framework `BINDER`, derive a physical
binding predicate, or establish that a net endpoint change is a physical
write.

## Proof-obligation graph

```text
supplied genesis + supplied alternating directions + exactly 2*n full orbits
    -> exact endpoint supports for 38 transitions

exact endpoint supports
    -> cardinality sequence, total 829, and minimum cardinality 17

minimum cardinality 17
    -> net_delta_nonempty = 1 on the 38 rows

net_delta_nonempty = 1
  + fresh ticks and sufficient capacity
  + certificate=actuality=admissibility=law_domain=1
    -> exact equality with the literal-one Cycle-610 traces
```

Every left-hand item is a condition. No step selects the genesis state,
direction schedule, event boundary, or physical meaning of the API inputs.

## Independent reconstruction

The primary runner executes the Cycle-719 controller orbit and independently
cross-checks each endpoint against the controller's closed-form allocator
word. The independent checker imports neither the primary nor any symbol from
it. It reconstructs the same endpoints directly from that closed-form word,
checks the complete count sequence, exhausts the indicator identity on all 64
three-bit before/after pairs, reconstructs the Cycle-610 Boolean decision
tree, and then executes the primary only as a clean black-box subprocess.

Both runners declare this note, the framework vocabulary boundary, and the
complete observed repository-Python runtime closure. The independent checker
also declares the primary source as an input.

## Import and support boundary

- The Cycle-719 controller note is an unaudited executable dependency. It
  supplies the controller, genesis trajectory, fixed program, and original
  literal-one admission calls; it does not supply objective binding semantics.
- The bank counts, initial states, alternating directions, event boundaries,
  and number of steps are supplied finite inputs.
- `D_t` records net endpoint bit differences. It does not enumerate transient
  gate touches or changes that cancel before the endpoint.
- No wire-to-Record-site map or bit-to-Record-content injection is used.
- The minimal Record premise supplies no record-production or update rule.
  This package constructs no framework `Record` and makes no permanence claim.
- The current-main Cycle-747 note is linked for its matching API boundary:
  a lower-case parameter name does not promote a Boolean identity to framework
  Admissibility or objective physical admission.
- No measured, fitted, observational, phenomenological, cosmological, or
  literature-derived numerical input appears.

## Claim boundary

The theorem proves one exact finite endpoint-delta census and one conditional
Boolean API corollary. It does not derive framework `BINDER`, Record formation,
physical writes, spatial locality, objective admission, a law-domain value,
actuality, Admissibility, a probability law, or an occurrence rule. It does
not claim that the selected trajectories exhaust lawful events or that
transport events are impossible. It makes no R-eta, inherited-wall, W3, or
multi-flag closure claim.

No separate physical naming convention is introduced:
`net_delta_nonempty` denotes only the explicit endpoint-support indicator.
Identifying that indicator with framework `BINDER` remains a supplied
labeling convention or an open semantic bridge outside this result.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 scripts/frontier_cycle751_binder_formation_attempt_2026_07_28.py

PYTHONDONTWRITEBYTECODE=1 \
  python3 scripts/frontier_cycle751_binder_independent_check_2026_07_28.py
```

Runner caches may be generated by audit infrastructure for reproducibility.
This source package ships no authored PASS transcript or claim-status receipt.
