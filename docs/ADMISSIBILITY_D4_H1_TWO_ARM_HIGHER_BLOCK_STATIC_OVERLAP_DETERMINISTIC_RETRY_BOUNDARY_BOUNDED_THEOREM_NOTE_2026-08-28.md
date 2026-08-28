---
claim_id: admissibility_d4_h1_two_arm_higher_block_static_overlap_deterministic_retry_boundary_bounded_theorem_note_2026-08-28
claim_type: bounded_theorem
claim_scope: "On the independently reproduced Block-222 74+54 supplied-normal carrier, an adjacent two-anchor higher-block seam with two exact parent-dart arms gives a nonvacuous static classifier on all 7,113,688 labelled width-two/three forest seams and a single conflict action on all 34,804,719 contacting pairs among 37,978,236 two-query pairs. All 5,040 prior reciprocal scalar-anchor crosswires become contacts. This is a static overlap certificate, not a hostile-schedule transition or CP-instrument proof. The frozen abort-both then immediate-retry grammar also admits a fair symmetric retry cycle; supplied finite geometric backoff has positive escape probability but does not select a physical probability law or a uniform/infinite-volume rate."
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_d4_h1_event_seeded_record_finality_markov_repair_boundary_bounded_theorem_note_2026-08-28
target_blocker_text: "remove the unique supplied event by conflict-safe physical multi-root ancestry arbitration"
source_of_blocker_text: block220_handoff
reachability_to_target: constructive_static_narrowing
artifact_role: theorem
runner: scripts/admissibility_d4_h1_two_arm_higher_block_ancestry_gate_2026_08_28.py
next_trace_action: "compile the seam/contact schema into explicit local rollback and acknowledgement rows, exhaust hostile schedules, then construct the literal CP backoff instrument or pivot to deterministic coalescence"
conditional_surface_status: bounded-support
bare_retained_allowed: false
parent_commit: 4f2a306538
preregistration_commit: b07b4acde5
no_go_discipline_status: broad_gate_fail_scoped_lockstep_retry_only
axiom_amendment: none
obligation_retirement: 0
toe_percentage_movement: 0
---

# Two-Arm Higher-Block Static Overlap and Deterministic-Retry Boundary

**Date:** 2026-08-28

**Type:** bounded theorem / positive static construction plus a scoped
liveness boundary.

Primary executable gate:
[admissibility_d4_h1_two_arm_higher_block_ancestry_gate_2026_08_28.py](../scripts/admissibility_d4_h1_two_arm_higher_block_ancestry_gate_2026_08_28.py).

No-go-discipline packet:
[ADMISSIBILITY_D4_H1_TWO_ARM_HIGHER_BLOCK_STATIC_OVERLAP_DETERMINISTIC_RETRY_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md](ADMISSIBILITY_D4_H1_TWO_ARM_HIGHER_BLOCK_STATIC_OVERLAP_DETERMINISTIC_RETRY_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md).

## Result up front

The two-arm route removes the exact static ambiguity found in Block 222.
It does not yet complete the physical dynamics.

The runner independently reconstructs the Block-222 carrier:

```text
physical C4 character: [37,-3,5,-3]
logical C4 character:  [34,-2,2,-2]
residual multiplicity: [1,0,2,0]
named/default ranks:    74+54
Gram floors:            38.507483548, 22.203469813
carrier digest:         09d24d6a23b5987a9a4e0a6b21052caa1d58ec16b4462019e01da9302dc79a76
```

The new object adds no onsite ray.  It is an overlap-visible radius-two
pattern: two adjacent `A` endpoints on reciprocal collision darts, with one
exact parent-dart front attached to each endpoint.  The pair projective phase
is ordinary, and all 576 source-normal/rotation/port transports preserve the
reciprocal seam.

The exact labelled path-forest census is:

| width | valid forests | seams | same-tree | foreign-tree |
|---:|---:|---:|---:|---:|
| 2 | 225 | 1,240 | 816 | 424 |
| 3 | 614,656 | 7,112,448 | 2,819,628 | 4,292,820 |
| total | 614,881 | 7,113,688 | 2,820,444 | 4,293,244 |

For the frozen static semantics, two arms from a same-tree seam meet and map
to conflict/rollback; two arms from a quiet foreign-tree seam reach distinct
roots and return two acknowledgements to their original adjacent seam.  Thus
the rule is not a reject-all construction.  Every parent, child, launch,
return and collision dart remains labelled, including width-two parallel
ports.

For two simultaneous seams:

| width | unordered pairs | contacting | disjoint | normalized contact signatures |
|---:|---:|---:|---:|---:|
| 2 | 2,844 | 2,772 | 72 | 18 |
| 3 | 37,975,392 | 34,801,947 | 3,173,445 | 47 |
| total | 37,978,236 | 34,804,719 | 3,173,517 | 47 at the larger width |

All eight preregistered unexpected-contact families map to one visible
`CONFLICT` action independent of proof-side query identity.  Most directly,
adding the second ancestry arm to every one of Block 222's 5,040 reciprocal
foreign-probe pairs makes the two marked supports meet at their guarded
roots.  All 5,040 therefore conflict instead of swapping scalar anchors.  The
first intercepted witness remains exactly

```text
[0,2,5,3,4] with ports [3,0,1,1]
[1,7,6]     with ports [2,3].
```

## What has and has not been proved

This is a static overlap/contact certificate.  It shows that an explicit
two-arm seam carries the correlation missing from the one-anchor protocol and
that a conservative, identity-free local action exists for every frozen
contact signature.  It does not yet give the full asynchronous transition
table, exhaust hostile interleavings of launch/front/acknowledgement/erasure,
prove that rollback leaves no orphan under every action order, or construct
literal pair/star Kraus operators.  Those are the next load-bearing tests.

The distinction matters: the count of 37,978,236 static pairs is strong
evidence for the representation and invariant, but it is not a completed
Record-finality law and is not credited as TOE-lane movement.

## Deterministic retry and conditional stochastic escape

If both conflicting probes use the singular retry rule

```text
launch both -> contact -> rollback both -> launch both,
```

the schedule is fair to both probes and can repeat forever.  The static safety
certificate therefore does not supply deterministic size-independent
liveness.

As a mathematical comparator, let each of `n` finite contenders draw an
independent geometric delay with supplied `p=1/2`.  The probability of a
unique minimum in one round is

```text
n p (1-p)^(n-1) / (1-(1-p)^n),
```

giving `2/3, 3/7, 4/15, 5/31, 2/21, 7/127, 8/255` for `n=2,...,8`.
Every finite value is positive, so independent repeated rounds escape almost
surely.  This does not provide an infinite-component or uniform rate, and the
probability law, local coin carrier, Kraus weights, covariance, and connection
to the selected dynamics remain supplied obligations.

## Scope and verification

- primary baseline: `22/22`;
- mutation-meta: `23/23`, rejecting all `19/19` nonidentical mutations;
- all six normals, 24 rotations, both complement parities, exact 74+54
  partition, 576 seam transports and eight contact families checked;
- every width-two/three parent forest, seam and unordered seam pair in the
  declared static domain exhausted;
- no hidden query ID, epoch, coordinate, size, dimer phase, scheduler owner or
  independent edge factor is used;
- N1--N8 rejects every broad deterministic-liveness, Record-finality, or axiom
  no-go and authorizes only the lockstep retry-cycle narrowing.

No event occurrence, event site, rate, renewal, clock, source, selected law,
audit verdict, axiom amendment, obligation retirement, or TOE percentage
movement is claimed.
