---
claim_id: admissibility_d4_h1_multiroot_five_colour_ancestry_dart_alias_boundary_note_2026-08-28
claim_type: bounded_theorem
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_d4_h1_event_seeded_record_finality_markov_repair_boundary_bounded_theorem_note_2026-08-28
target_blocker_text: "remove the unique supplied event by conflict-safe physical multi-root ancestry arbitration"
source_of_blocker_text: block220_handoff
reachability_to_target: narrows
artifact_role: theorem
next_trace_action: "construct an explicit higher-block oriented-edge ancestry carrier that preserves tangent pointer and zipper phase simultaneously"
conditional_surface_status: bounded-support
bare_retained_allowed: false
parent_commit: c2da0af7f9
preregistration_commit: e77a50eeb8
no_go_discipline_status: broad_gate_fail_scoped_partial_narrowing_only
axiom_amendment: none
obligation_retirement: 0
toe_percentage_movement: 0
---

# Multiroot Five-Colour Ancestry-Dart Alias Boundary

**Date:** 2026-08-28

**Type:** bounded theorem / partial narrowing.

Primary executable gate:
[admissibility_d4_h1_multiroot_five_colour_ancestry_alias_gate_2026_08_28.py](../scripts/admissibility_d4_h1_multiroot_five_colour_ancestry_alias_gate_2026_08_28.py).

No-go-discipline packet:
[ADMISSIBILITY_D4_H1_MULTIROOT_FIVE_COLOUR_ANCESTRY_DART_ALIAS_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md](ADMISSIBILITY_D4_H1_MULTIROOT_FIVE_COLOUR_ANCESTRY_DART_ALIAS_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md).

## Result

The preregistered depth-only five-colour one-site ancestry zipper fails its
first training gate. It cannot preserve an exact physical tangent dart when a
width-two parity-component edge has two labelled ports with the same endpoint.

The first deterministic witness uses width-two vertices

`0 -> 2 -> 3 -> 1`

with path ports `[0,1,0]`, root 0, launch port 0 and noninverse root-collision
port 1. During backward zipping, site 2's original P pointer must be restored
toward child site 3 through port 1. After replacing that tangent P state by a
normal-direction depth marker, both ports 1 and 3 are locally compatible and
both reach site 3. The marker retained the endpoint but erased the labelled
dart. That is load bearing: Block 220's inverse-return and width-two safety
distinguish the two ports even when their endpoint agrees.

Exhaustive training enumeration finds:

```text
width 2 candidate root-cross cycles: 144
width 2 ambiguous cycles:            128
width 3 candidate root-cross cycles: 4356
width 3 ambiguous cycles:            1440
```

The width-three failures include next-colour path chords in addition to the
width-two parallel-dart loss. Because a training falsifier exists, the
preregistered gate stops before held L8 inspection and before a full
classical/Kraus grammar. No retuning is allowed.

As a control, the same runner reconstructs the unchanged Block 220 L4
two-root census: 96/576 same-bit mixed starts can reach a false Record,
whereas 0/768 opposite-bit starts reach a Record. Its first five-action trace
exactly matches the frozen Block 221 entry witness. Thus the campaign did not
trade away or misstate the motivating safety defect.

## Scope

This is not a no-go for one-site time multiplexing, ancestry arbitration,
permanent Records or the axioms. The frozen mapping used one normal-direction
state as an anchor and assigned the remaining five states by depth modulo
five. It did not test a port-aware assignment, a two-site relational phase
pattern, a different embedded alphabet, rollback-first coalescence,
stochastic liveness, coherent arbitration or a continuous-time generator.

The exact lesson is narrower and constructive: ancestry phase cannot overwrite
the load-bearing tangent pointer unless the replacement representation stores
both. The preauthorized next route therefore keeps Block 220's onsite P/H/R
direction intact and puts zipper/freeze phase on an explicit oriented edge or
higher block.

## Verification

- baseline: `17/17`;
- mutation-meta run: `18/18`, rejecting `10/10` nonidentical mutations;
- exact Block 220 L4 two-root census reproduced, including maximum reachable
  set 51 and maximum shortest false-Record trace 5;
- every simple candidate root-cross cycle on training widths two and three
  enumerated with periodic wrap and labelled parallel darts preserved;
- N1--N8 returns FAIL for every broad negative and permits only this partial
  narrowing;
- independent reconstruction remains required before packaging any Block 221
  result.

No axiom amendment, formal audit verdict, obligation retirement or TOE
percentage movement is claimed.
