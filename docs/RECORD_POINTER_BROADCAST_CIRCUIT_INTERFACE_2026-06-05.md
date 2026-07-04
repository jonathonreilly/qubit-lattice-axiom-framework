---
claim_id: record_pointer_broadcast_circuit_interface_2026-06-05
claim_type_author_hint: bounded_support_map
---

# Record Pointer Broadcast Circuit Interface

**Date:** 2026-06-05
**Claim type:** bounded_theorem — bounded support map and conditional finite witness.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_pointer_broadcast_circuit_interface_2026_06_05.py`](../scripts/frontier_record_pointer_broadcast_circuit_interface_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_pointer_broadcast_circuit_interface_2026_06_05.txt`](../logs/runner-cache/frontier_record_pointer_broadcast_circuit_interface_2026_06_05.txt).

**Local support inputs:**

- [`RECORD_LOCAL_OBSERVABILITY_DECODER_CRITERION_2026-06-05.md`](RECORD_LOCAL_OBSERVABILITY_DECODER_CRITERION_2026-06-05.md)
- [`RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md`](RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md)
- [`RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`](RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md)
- [`RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md`](RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md)
- [`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md)

## Purpose

This note gives the finite witness that the production checklist asks for:
if a pointer basis, blank fragments, and a pointer-controlled broadcast unitary
are supplied, then the produced pointer value is locally observable on every
fragment.

It also keeps the pre-record/post-record distinction sharp:

```text
pointer eigenvalue / realized record atom -> can be copied as a label
generic pre-record qubit state          -> is not cloned by the same unitary
```

## Result

On one system qubit `S` and three blank fragment qubits `F_i`, the CNOT-fanout
unitary

```text
|s>|f_1 f_2 f_3> -> |s>|f_1 xor s, f_2 xor s, f_3 xor s>
```

has the following exact finite properties:

1. It is unitary and pointer non-demolition: the system pointer bit `s` is
   unchanged on every computational-basis input.
2. With blank fragments `000`, pointer eigenstates broadcast:
   `|0>|000> -> |0>|000>` and `|1>|000> -> |1>|111>`.
3. Every fragment has a local decoder for the produced pointer value.
4. Blankness matters: nonblank fragments are not a clean produced record of the
   system pointer.
5. A generic superposition becomes a GHZ-style entangled state
   `a|0,000> + b|1,111>`, not four independent copies of
   `a|0> + b|1>`.

So this is a conditional finite production witness for local observability, not
a from-axioms derivation of the production dynamics.

## Negative route pruning

| route | verdict | reason |
|---|---|---|
| pointer broadcast clones the pre-record qubit | pruned | the output from a superposition is entangled, not independent copies |
| local observability follows without blank fragments | pruned | nonblank fragments can fail to encode the pointer value |
| broadcast witness supplies physical rates | pruned | the circuit has no clock or rate normalization |
| broadcast witness selects a dial location | pruned | it is a record-production interface only |
| unitary witness derives the physical Hamiltonian | pruned | the Hamiltonian/production law remains an external dynamics gate |

## What remains open

- Deriving the pointer basis from the framework dynamics.
- Deriving the blank-fragment initial condition.
- Deriving the physical Hamiltonian or production law that implements this
  witness.
- Clock/rate normalization.
- Probability weights over outcomes before realization.
- Any generation/Koide dial selection.

## What this unlocks

- A concrete finite target for production proposals: they must supply a
  pointer-preserving broadcast into locally decodable fragments.
- A clean no-cloning firewall for the user's pre-record/post-record distinction.
- A compositional path from produced pointer atom to local decoders to
  post-record histories, while keeping clock/rate gates separate.

## Boundaries

- Does not derive broadcast dynamics, pointer basis, blank fragments, physical
  Hamiltonian, rates, clock, probabilities, or a dial setting.
- Does not apply audit verdicts.

## Runner summary

The runner verifies unitarity, non-demolition, blank-fragment broadcast, local
decoder existence, blankness necessity, GHZ output from a superposition, reduced
state decoherence relative to the original qubit, and non-equality to a cloned
product state.

Expected result:

```text
SCORECARD PASS=35 FAIL=0
```

```yaml
claim_id: record_pointer_broadcast_circuit_interface_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact finite witness given pointer basis, blank fragments, and broadcast unitary"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
