# Fixed Cycle-719 origin-zero compiled data trace — Cycle 769

Date: 2026-07-29

Authority: none

Audit: unset

Status: conditional / support

Claim type: bounded_theorem

Primary runner:
[`frontier_cycle769_cycle719_origin_zero_compiled_data_trace_2026_07_28.py`](../scripts/frontier_cycle769_cycle719_origin_zero_compiled_data_trace_2026_07_28.py)

Independent checker:
[`frontier_cycle769_cycle719_origin_zero_compiled_data_trace_independent_check_2026_07_28.py`](../scripts/frontier_cycle769_cycle719_origin_zero_compiled_data_trace_independent_check_2026_07_28.py)

Load-bearing source:
[Cycle-719 recurrent matter/history controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md).

Constitutional effect: none. This package changes no axiom, foundation,
primitive, registry, policy, queue, audit result, or audit status.

## Question

What exact data transitions occur when the current Cycle-719 compiled
controller is run on the support keys of its fixed clean origin-zero fixture?

This is a finite software/API question. The result is conditional on the
current Cycle-719 implementation and the fixture listed below.

## Result

The fixed matter word produces exactly six support keys with source-matter
modes `(0, 2, 3, 4, 5, 6)`. Under the fixed 130-station compiled controller:

- modes 0, 2, 3, 4, and 5 have no data transitions;
- mode 6 has exactly three data transitions:
  `(step, program kind, program index, changed data bits)` equals
  `(0, source, 0, 3)`, `(1, bank, 1, 32)`, and
  `(125, finalizer, 125, 3)`;
- the Cycle-719 decoder refuses the data state after the first two
  transitions and, after the finalizer, returns exactly
  `EventCell(identity=0, rotor=15, carry=0, predecessor=None, binder=1,
  valid=1, orientation=1)`; and
- reversing the compiled word over all 130 stations restores every one of the
  six fixed inputs exactly.

The primary runner gates every field above. It also deletes each of the three
active program rows in turn and requires the trace contract to change. The
independent checker uses a separate integer interpreter, reads the final
packed cell fields directly as well as through the Cycle-719 decoder, and
runs the primary only as a black box.

## Supplied fixture

The result uses exactly:

- the current Cycle-719 source and its declared 64-path input closure;
- 12 clean banks and clean links from `chain_genesis(12)`;
- `matter=1` at origin zero before the fixed Cycle-719 matter word;
- the six nonzero support keys of that one output state, without treating
  their unequal amplitudes as equal weights;
- one controller token at `A[0]`, clean `B` and work rails, the fixed
  130-station program, and its compiled X/CNOT/Toffoli word; and
- the current Cycle-719 `unpack_state` and `decode_local_graph` API.

These are fixture inputs, not derived physical selections.

## Derived

- the exact six support modes;
- the complete per-step data-transition trace on those six inputs;
- the two intermediate decoder refusals and exact final API cell;
- controller-register cleanup and exact reverse-word restoration; and
- active sensitivity to deletion of the source, bank, and finalizer rows.

## Boundary

This note makes no claim about framework Law or Admissibility, physical
occurrence, branch probability, weights, rates, Record formation, or
permanence. A Cycle-719 `EventCell` is kept as an API object and is not
identified with a framework Record. The five empty traces are statements
only about the five named support keys under the supplied program.

The source dependency is unaudited. This package therefore remains a bounded
conditional software/API result until independent audit evaluates it.
