---
claim_id: admissibility_d4_h1_two_arm_backoff_fairness_quotient_boundary_bounded_theorem_note_2026-08-28
claim_type: bounded_theorem
claim_scope: "On the independently reconstructed Block-223 74+54 carrier and static anchors, the exact six-row retry/contact/rollback quotient distinguishes weak finite-delay fairness from action/support strong fairness. A nonanticipating synchronizer has zero absorption for every supplied 0<p<1 under weak fairness, but it recurrently starves the positive FIRST_GO row and is inadmissible under the preregistered strong-fair class. Exhaustive fair-component closure finds no nonterminal action-strong-fair recurrent class, so the quotient absorbs almost surely. This binds rather than executes local rollback safety and compiles only the retry-projector Kraus identity; no full dynamic CP, expected-time, physical scheduler/law or TOE result is claimed."
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_d4_h1_two_arm_higher_block_static_overlap_deterministic_retry_boundary_bounded_theorem_note_2026-08-28
target_blocker_text: "replace the static retry comparator by hostile-schedule local dynamics and a literal physical instrument"
source_of_blocker_text: block223_handoff
reachability_to_target: positive_quotient_narrowing
artifact_role: theorem
runner: scripts/admissibility_d4_h1_two_arm_dynamic_cp_backoff_gate_2026_08_28.py
next_trace_action: "compile the exact onsite/radius-two rollback and acknowledgement rows, model-check their full reachable fair components, and construct the complete 74+54 Kraus instrument; pivot to deterministic component coalescence on the first physical alias or fair component"
conditional_surface_status: "exact action-strong-fair absorption only on the six-row quotient with supplied 0<p<1; weak-fair synchronizer boundary exact; local rollback safety, full CP, expected time, scheduler selection and physics open"
bare_retained_allowed: false
parent_commit: 607eaba9aa
preregistration_commits: [dc6ee28c37, cee9d562d7]
no_go_discipline_status: broad_gate_fail_weak_fair_synchronizer_only
axiom_amendment: none
obligation_retirement: 0
toe_percentage_movement: 0
---

# Two-Arm Backoff Fairness Quotient Boundary

**Date:** 2026-08-28

**Type:** bounded theorem / positive quotient result plus a scoped fairness
boundary.

Primary executable gate:
[admissibility_d4_h1_two_arm_dynamic_cp_backoff_gate_2026_08_28.py](../scripts/admissibility_d4_h1_two_arm_dynamic_cp_backoff_gate_2026_08_28.py).

No-go-discipline packet:
[ADMISSIBILITY_D4_H1_TWO_ARM_BACKOFF_FAIRNESS_QUOTIENT_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md](ADMISSIBILITY_D4_H1_TWO_ARM_BACKOFF_FAIRNESS_QUOTIENT_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md).

## Result up front

The proposed hostile synchronizer does not refute the preregistered strong-
fair route.  The correction is load-bearing.

The runner independently reconstructs the exact parent anchors:

```text
carrier:                 74 named + rank-54 default
physical character:      [37,-3,5,-3]
logical character:       [34,-2,2,-2]
residual multiplicity:   [1,0,2,0]
carrier digest:           09d24d6a23b5987a9a4e0a6b21052caa1d58ec16b4462019e01da9302dc79a76
width-three forests:      614,656
total static seams:       7,113,688
total static pairs:       37,978,236
width-three buckets:      47
reciprocal interceptions: 5,040/5,040
```

It then constructs the exact quotient

```text
BOTH_RETRY --coin1--> FIRST_GO --coin2--> BOTH_GO
     ^                                      |
     |                                      v
  ROLLBACK <----------- CONTACT <-----------+

FIRST_GO --complete seam 1--> POSITIVE.
```

Both coin rows have supplied weights `p` and `1-p`, with `0<p<1`.
`CONTACT` quenches both participants and `ROLLBACK` returns to `BOTH_RETRY` as
the frozen conditional boundary.  The quotient does not execute the onsite
rollback table.

## The fairness correction

The preregistered synchronizer repeatedly does this:

1. retry seam 1 until `go`;
2. delay seam 1 completion;
3. retry seam 2 until `go`;
4. contact, rollback and repeat.

Each delay is geometric:

```text
Pr[N>n]=(1-p)^n -> 0,
E[N]=1/p,
E[round]=2/p+3.
```

Consequently the policy is nonanticipating and every one of its individual
delays is finite almost surely.  It is weakly fair.  Under that weaker class,
the five nonpositive states form a closed recurrent class and absorption is
exactly zero.

It is not action/support strongly fair.  `FIRST_GO` recurs infinitely, so
`favorable_complete_seam1` is enabled infinitely, but the synchronizer selects
it zero times.  This is the first explicit fairness witness; relabeling finite
delay as strong fairness would be a false result.

For the complete six-row quotient, the runner exhausts every nonempty subset
of the five nonpositive states.  A strong-fair recurrent class must be closed
under every action enabled at a recurrent source and, because `0<p<1`, under
every positive-probability outcome of that action.  No such nonterminal class
exists: any class containing recurrent `FIRST_GO` must include its completion
edge to `POSITIVE`.  Therefore, for every supplied `0<p<1`, every
nonanticipating action/support-strongly-fair scheduler absorbs almost surely
on this quotient.

This does not give a scheduler-uniform rate or finite expected time.  Strong
fairness permits arbitrarily long finite postponements, including supplied
random postponement laws with infinite mean.

## Quantum and physical boundary

The retry row itself has the exact conditional instrument

```text
K_go^dagger K_go   = p P_retry,
K_wait^dagger K_wait = (1-p) P_retry,
K_default          = I-P_retry,
```

so the effects sum to identity.  The environment labels remain separate; no
coherent many-to-one row is used.  `LOCK` and `BG` remain QND Record sectors
and are never scratch states.

This is not the complete physical instrument.  The local advance, contact,
rollback, acknowledgement, quiescence and reuse rows remain uncompiled.  The
six-row quotient assumes their branchwise safety exactly as frozen in the
preregistration; it does not prove it.  It also does not select `p`, the
scheduler, an event, a rate, renewal, clock or physical time.

## Verification and scope

- primary science plus mutation-meta: `22/22`, all `25/25` declared mutations
  rejected;
- full source/scope gate: `22/22`; runner SHA-256
  `c3de1c366ea7ea4d7427388374c9872ff2e27227f24be3be94cb68d35594687c`;
- exact carrier, 24 rotations, complement, six normal frames and transported
  rank-54 defaults reconstructed;
- all width-two/three static forest anchors, 47 buckets and 5,040 reciprocal
  witnesses reconstructed;
- all 31 nonempty candidate nonterminal subsets of the five-state quotient
  are covered by the fair-component enumeration;
- weak-fair zero absorption, strong-fair policy inadmissibility and strong-
  fair quotient absorption are reported separately;
- no full dynamic safety, complete CP, expected-time, uniform-rate,
  infinite-volume, physical-time, law-selection, broad no-go, audit verdict,
  axiom amendment, obligation retirement or TOE percentage movement is
  claimed.

The next result must be the real local compiler, not another fairness slogan.
