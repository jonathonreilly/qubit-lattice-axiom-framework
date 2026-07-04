---
claim_id: record_pointer_broadcast_hamiltonian_conditional_2026-06-05
claim_type_author_hint: bounded_support_map
---

# Record Pointer Broadcast Hamiltonian Conditional

**Date:** 2026-06-05
**Claim type:** bounded_theorem — bounded support map and conditional finite construction.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_pointer_broadcast_hamiltonian_2026_06_05.py`](../scripts/frontier_record_pointer_broadcast_hamiltonian_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_pointer_broadcast_hamiltonian_2026_06_05.txt`](../logs/runner-cache/frontier_record_pointer_broadcast_hamiltonian_2026_06_05.txt).

**Local support inputs:**

- [`RECORD_POINTER_BROADCAST_CIRCUIT_INTERFACE_2026-06-05.md`](RECORD_POINTER_BROADCAST_CIRCUIT_INTERFACE_2026-06-05.md)
- [`RECORD_LOCAL_OBSERVABILITY_DECODER_CRITERION_2026-06-05.md`](RECORD_LOCAL_OBSERVABILITY_DECODER_CRITERION_2026-06-05.md)
- [`RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`](RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md)
- [`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md)

## Purpose

The pointer-broadcast circuit witness supplies a finite target gate. This note
adds the next conditional layer: if controlled pointer-fragment interactions and
a time unit are supplied, a Hermitian pointer-preserving Hamiltonian generates
that fanout.

The construction is useful, but it is not a physical derivation of the
Hamiltonian or its coupling scale.

## Result

For one pointer qubit `S` and three fragments, let `C_i` be the CNOT with
control `S` and target fragment `i`. Each `C_i` is Hermitian, involutive, and
commutes with the other `C_j`. Define

```text
H(T) = sum_i (pi / (2T)) (I - C_i).
```

Then

```text
exp(-i H(T) T) = C_1 C_2 C_3,
```

the fanout unitary from the pointer-broadcast circuit witness. The Hamiltonian
commutes with the pointer `Z_S`, so it is pointer non-demolition.

The residual is explicit: the formula assumes the controlled interactions and
the duration/coupling normalization. Choosing `T=1` or `T=2` gives different
Hamiltonian scales and the same endpoint gate at the chosen time.

## Negative route pruning

| route | verdict | reason |
|---|---|---|
| fanout gate derives its physical Hamiltonian | pruned | the construction chooses the controlled terms |
| Hamiltonian construction fixes the rate scale | pruned | `H(T)` rescales with the supplied duration `T` |
| pointer preservation selects the pointer basis | pruned | the pointer basis is an input to the controlled terms |
| finite generator supplies blank fragments | pruned | initial blankness remains a boundary/input |
| finite generator selects a dial location | pruned | it is only a record-production interface |

## What remains open

- Deriving the controlled interaction terms from the framework dynamics.
- Deriving the pointer basis and blank-fragment boundary condition.
- Selecting the physical duration/coupling normalization.
- Probabilities before realization.
- Any generation/Koide dial selection.

## What this unlocks

- Production proposals now have a concrete Hamiltonian target, not just a gate
  target.
- Review can separate "there exists a Hermitian generator for the witness" from
  "the framework derives that generator and scale."
- The no-cloning firewall from the circuit witness remains intact, because this
  Hamiltonian generates the same fanout.

## Boundaries

- Does not derive the physical Hamiltonian, controlled interactions, pointer
  basis, blank fragments, rates, clock, probabilities, or a dial setting.
- Does not apply audit verdicts.

## Runner summary

The runner verifies that the controlled terms are Hermitian involutions, commute,
generate the fanout through `exp(-i H T)`, preserve the pointer observable, and
rescale with `T` while leaving the endpoint gate fixed.

Expected result:

```text
SCORECARD PASS=37 FAIL=0
```

```yaml
claim_id: record_pointer_broadcast_hamiltonian_conditional_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact finite construction given controlled terms and a time normalization"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
