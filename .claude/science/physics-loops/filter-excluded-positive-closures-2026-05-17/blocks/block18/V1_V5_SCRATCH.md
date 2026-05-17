# Block 18 V1-V5 Scratch

Row: `frontier_extension_lane_opening_note_2026-04-25`
State: unaudited; 376 descendants. FRESH lane (frontier_extension).
Target: lane-opening note that declares three bounded workstreams
(teleportation, chronology, signed gravity) with first decision gates and a
non-promotion rule.

## Setup

The lane-opening note is meta: it does not state a science theorem. It
records that three bounded workstreams are open and pins their gates.

It does, however, carry several derivation-shaped meta-claims that have not
been individually closed:

(M1) The opening of the three lanes does not alter the retained claim
     surface ("Non-Promotion Rule").
(M2) The three lanes have well-defined and *disjoint* first gates (no gate
     of one lane is the gate of another).
(M3) Lane B (chronology protection) protects the framework from sloppy
     time-travel implications of CPT, U(-t), reversibility, and successful
     teleportation ("Priority Order" §, item 2: "It protects the framework
     from sloppy implications of CPT, reversibility, and teleportation.").
(M4) The three working names (teleportation, chronology, signed-gravity
     response) explicitly reject sensationalist counterparts (matter
     teleportation, time-machine, antigravity).
(M5) Each lane's "first retained-safe statement if the lane works" is a
     conditional, not a present claim.

The brief says: a positive content option is to *derive what the lane
proposes from existing primitives*. The most concrete meta-claim that can
be derived as a positive narrow theorem is (M3): the joint composition of
Lane A's teleportation no-signaling and Lane B's chronology
no-past-signaling forms a strictly stronger past-and-Bob-protected
no-signaling envelope than either lane alone.

## Existing artifacts in lanes (already landed by prior cycles)

- Lane A (teleportation):
  - `scripts/frontier_teleportation_protocol.py` exists.
  - `docs/TELEPORTATION_NO_SIGNALING_AUDIT.md` exists (Apr 25 note).
  - 47 follow-on TELEPORTATION_*.md notes in docs/.

- Lane B (chronology):
  - `docs/CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md`
  - `scripts/frontier_chronology_operational_no_past_signaling.py` exists.
  - Exact CPTP trace-preservation theorem already landed.

- Lane C (signed gravity):
  - `docs/SIGNED_GRAVITY_RESPONSE_LANE_STATUS_NOTE_2026-04-26.md`
  - 32 sibling SIGNED_GRAVITY_*.md notes.
  - Verdict: locked-sign mechanism conditional; selector + source-action
    no-gos for strict local primitives; not closed.

This means the *individual* first gates of A and B are landed (or have
substantial closure). Lane C's first gate is not closed. The cross-lane
composition theorem is NOT in any current note.

## Distinct angles for block 18

This is a fresh lane in the block series; no prior block touched
`frontier_extension`. V1-V5 distinctness rule applies *within* this block.

## V1 — Derive lane-opening "non-promotion rule" (M1) as a strict claim-surface
        identity theorem

Try to prove: the addition of the lane-opening note to the repo does not
add any retained claim-row, theorem-row, or prediction-row.

VERDICT: This is a meta-textual administrative claim about the audit-data
indexing layer, NOT a derivation from framework primitives. Closing it
would mean verifying that no retained row in `audit-data/` cites the
lane-opening note as load-bearing, which is an audit-data-touching task.
The hard rules explicitly forbid audit-data touches. SKIP.

## V2 — Derive (M2) lane-gate disjointness as a partial-order theorem

Try to prove: lane A's first gate (operational no-signaling of an exact
teleportation protocol), lane B's first gate (no operational past
signaling), and lane C's first gate (derived chi_g selector with action-
reaction) are mutually independent — none implies any other.

VERDICT: This is interesting but would require formalizing 3 gate
predicates and showing pairwise that any 2 can fail/succeed independently.
That is 6 independence claims and would not derive *from* framework
primitives; it would derive from gate-text parsing. Substantial work but
the result is procedurally trivial: each gate uses non-overlapping
framework structures (teleportation uses Hilbert+taste; chronology uses
single-clock+causal-order; signed-gravity uses gravity+source-sign). The
theorem is structurally true by inspection of the lane texts; turning
inspection into a numeric runner adds little new science. SKIP — too
close to gate-text parsing, low new content.

## V3 — Derive (M3) the lane-B protection of lane A as a joint composition
        theorem — THIS IS THE ANGLE

Lane-opening note §"Priority Order", item 2:
"Land the chronology boundary second. It protects the framework from
sloppy implications of CPT, reversibility, and teleportation."

This is a derivation-shaped claim. The framework primitives available:

- Lane A no-signaling theorem: Bob's pre-message reduced state ρ_B does
  not depend on Alice's input |ψ⟩. Statement: Tr_ARecord[T_AB(|ψ⟩⟨ψ| ⊗ Φ)]
  equals I/d for all input |ψ⟩ before the classical message arrives.
- Lane B no-past-signaling theorem: on single-clock CPTP, later setting x
  at t_1 cannot alter P(a at t_0) for any record event a at t_0 < t_1.

The composition claim (M3) takes the form:

  **Joint Protection Theorem.** Let T_AB be any teleportation protocol
  satisfying Lane A's pre-message no-signaling at Bob. Let S_x be any
  later CPTP setting at time t_C > t_B (including but not restricted to:
  Hadamard at Bob, dephasing at Bob, memory reset of Bob's register,
  Loschmidt echo U(-t)·U(t) reconstruction of Bob's branch). Then the
  marginal probability of Alice's outcome record P(a at t_A) is unchanged
  by the choice of x.

This is the **A∧B ⇒ AB-protected** composition that the lane-opening note
posits as the lane-B protection effect on lane A.

The derivation is structurally clean:

  (1) Build a 3-time joint Hilbert circuit: Alice prepares |ψ⟩ and Bell
      half at t_A; Bell measurement and classical record at t_A;
      teleportation channel transports state to Bob at t_B; arbitrary
      CPTP setting S_x at Bob at t_C > t_B.
  (2) Lane A: at t_B, Bob's reduced state ρ_B(input) = I/d for all input,
      pre-classical-message. Hence Bob's branch trace is input-
      independent.
  (3) Lane B: at t_C, S_x is CPTP. By the no-past-signaling theorem, no
      choice of x at t_C can alter the unconditioned probability
      P(a_Alice at t_A) of Alice's earlier record outcome.
  (4) Combined (positive theorem): the *pre-message* teleportation no-
      signaling at Bob is *robust* under all subsequent chronology-
      respecting (CPTP) operations at Bob's location. The operational
      no-FTL envelope holds throughout the joint circuit, not just at the
      single time-slice t_B.

This is what the lane-opening note posits as the "protection" effect.
It is derivable from Lane A + Lane B with zero new framework primitives.

What this *does not* close:

- The lane-opening note itself is not promoted to retained.
- Lane C (signed gravity) is not touched.
- The 4-pair signed-gravity action-reaction table is not affected.
- Postselected past-conditioning is not affected (the note already
  acknowledges this exception via Lane B's theorem).
- The composition is bounded to retained CPTP and retained single-clock;
  any final-boundary or postselected theory remains outside scope.

This is distinct from:

- Lane A's no-signaling audit (single time-slice statement at t_B).
- Lane B's no-past-signaling theorem (single record-event statement, no
  teleportation present).
- The CHRONOLOGY note's own theorem (does not contain a teleportation
  channel in its setup).
- The teleportation no-signaling audit (does not contain a downstream
  CPTP setting at t_C > t_B).

CHOOSE V3.

## V4 — Derive (M4) (sensationalist-name rejection) as a name-only audit

Try to certify that retained docs do not use "matter teleportation",
"time machine", "antigravity" as load-bearing names.

VERDICT: Pure repo-wide textual audit. Not a derivation from primitives.
Some of these names appear in *audit notes* as rejection rhetoric (e.g.
SIGNED_GRAVITY_NON_CLAIM_GATE_NOTE.md), which is *correct usage*.
Distinguishing rejection vs. promotion is a text-parsing job, not
framework derivation. SKIP.

## V5 — Derive (M5) (conditional safe-statement structure) as a syntactic
        modal-logic identity

Try to prove: every "First retained-safe statement if the lane works"
clause in the lane-opening note is in the form of a conditional with the
lane closure as antecedent.

VERDICT: This is a textual implication-pattern audit. Once stated, the
result is trivially true by inspection. Not a derivation from primitives.
SKIP.

## Decision

V3 is the angle: **Joint Protection Theorem — composition of Lane A
teleportation no-signaling with Lane B no-past-signaling gives a
multi-time no-FTL envelope.**

This is a positive narrow derivation theorem from already-landed Lane A
and Lane B primitives, with no new framework axioms, no audit-data
touches, no main push, and source-only deliverables.

The runner builds an explicit 3-time circuit:
  - alice & bell-half ⊗ bob-half resource at t_0
  - alice Bell measurement + classical record a at t_A
  - teleportation channel T_AB completes at t_B (Bob's reduced state
    pre-message)
  - arbitrary CPTP setting S_x at t_C > t_B (Hadamard, dephasing, reset,
    Loschmidt echo)

and checks four cumulative properties:

  (J1) Bob's reduced state at t_B is input-independent (Lane A
       no-signaling, re-checked in the joint circuit).
  (J2) The earlier record P(a at t_A) is invariant under all settings x
       at t_C (Lane B no-past-signaling, re-checked).
  (J3) Bob's reduced state at t_C *can* depend on x (this is *not*
       signaling — it is Bob altering his own future state — and serves
       as a fairness control).
  (J4) The joint circuit forbids any operational past-signaling channel
       from t_C back to t_A even in the presence of teleportation.

(J3) is critical: without showing that some property is *not* trivially
preserved, the no-signaling statement is vacuous. The fairness control
shows Bob's local future state does respond to x (so Bob is doing
*something*), while the earlier record still cannot be biased.

This block does NOT close the lane-opening note itself (it remains a
planning note), does NOT promote Lane C, and does NOT change the
manuscript surface. It adds one derived joint composition theorem and
its runner.
