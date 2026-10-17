---
claim_id: record_blank_boundary_reset_no_go_2026-06-05
claim_type_author_hint: exact_negative_boundary
---

# Record Blank-Boundary Reset No-Go

**Date:** 2026-06-05
**Claim type:** no_go — exact negative boundary for closed finite-unitary clean
broadcast from arbitrary fragment states.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_blank_boundary_reset_no_go_2026_06_05.py`](../scripts/frontier_record_blank_boundary_reset_no_go_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_blank_boundary_reset_no_go_2026_06_05.txt`](../logs/runner-cache/frontier_record_blank_boundary_reset_no_go_2026_06_05.txt).

**Local support inputs:**

- [`RECORD_POINTER_BROADCAST_HAMILTONIAN_CONDITIONAL_2026-06-05.md`](RECORD_POINTER_BROADCAST_HAMILTONIAN_CONDITIONAL_2026-06-05.md)
- [`RECORD_POINTER_BROADCAST_CIRCUIT_INTERFACE_2026-06-05.md`](RECORD_POINTER_BROADCAST_CIRCUIT_INTERFACE_2026-06-05.md)
- [`RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`](RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md)
- [`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md)

## Question

Can a closed finite unitary turn arbitrary old fragment states into a clean
locally observable broadcast record of the pointer value, without a blank
boundary or an erasure/sink resource?

No. That route is many-to-one and therefore not unitary.

## Result

For one pointer qubit and three fragment qubits, the clean broadcast target is

```text
|0>|anything> -> |0>|000>
|1>|anything> -> |1>|111>.
```

For each pointer value there are eight orthogonal fragment inputs and only one
clean target vector. Mapping all eight to the same target collapses inner
products and has rank `2` rather than `16`. It cannot be a unitary or an
isometry on the closed four-qubit space.

The CNOT-fanout witness therefore needs the fragments to start blank. If they
are not blank, the old fragment state is reversibly XORed into the output and
the result is generally not a clean local record. To clean arbitrary old
fragments, a future production theorem must supply a reset/erasure/sink
resource or a boundary condition that prepares blank fragments.

## Negative route pruning

| route | verdict | reason |
|---|---|---|
| fanout removes old fragment memory by itself | pruned | CNOT fanout preserves old fragment data by XOR |
| closed unitary resets arbitrary fragments to clean broadcast | pruned | many orthogonal inputs would map to one output |
| Hamiltonian witness supplies blank fragments | pruned | the generator acts on whatever state is present |
| local observability removes erasure cost | pruned | local decoders do not reset old memory |
| unbounded retention supplies blank workspace | pruned | retention stores records; it does not erase memory |

This no-go is narrow: it blocks closed finite-unitary clean reset without an
extra sink or blank boundary. It does not block an open-system reset,
thermodynamic erasure process, or a cosmological/low-record boundary.

## What remains open

- A blank-fragment preparation principle.
- An erasure/reset dynamics with an explicit sink/environment.
- A thermodynamic cost or entropy ledger for reset.
- A physical production Hamiltonian plus boundary condition.
- Clock/rate normalization.

## What this unlocks

- Production lanes can no longer hide blank fragments inside "fanout."
- The blank/low-record boundary is identified as a real dynamics input,
  aligned with the past-hypothesis residual in the arrow note.
- Future reset proposals have a precise target: preserve unitarity by carrying
  old fragment information into an explicit sink, or declare an open-system
  erasure process.

## Boundaries

- Does not derive blank fragments, erasure, thermodynamic reset, sink dynamics,
  physical Hamiltonian, rates, clock, probabilities, or a dial setting.
- Does not apply audit verdicts.

## Runner summary

The runner verifies that fanout gives clean broadcast only from blank fragments;
that the hypothetical closed reset map has duplicate output columns, rank `2`,
and fails the isometry condition; and that adding an explicit garbage/sink
label would restore injectivity at the level of finite labels.

Expected result:

```text
SCORECARD PASS=31 FAIL=0
```

```yaml
claim_id: record_blank_boundary_reset_no_go_2026-06-05
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: "exact no-go for closed finite-unitary clean reset without sink"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
