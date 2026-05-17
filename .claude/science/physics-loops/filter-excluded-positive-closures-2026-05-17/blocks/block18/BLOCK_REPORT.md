# Block 18 Report

**Date:** 2026-05-17
**Lane:** `frontier_extension` (FRESH; first block on this lane)
**Target:** `frontier_extension_lane_opening_note_2026-04-25` — desc=376,
unaudited

## Status

POSITIVE NARROW COMPOSITION THEOREM landed.

The lane-opening note remains a planning record. This block delivers a
narrow positive composition theorem on a derivation-shaped claim inside
the lane-opening note (its "Priority Order" rationale that Lane B
protects Lane A from sloppy time-travel implications), derived from two
already-landed framework results.

## Deliverable

1. **Source theorem note:**
   `docs/FRONTIER_EXTENSION_LANE_B_PROTECTS_LANE_A_JOINT_COMPOSITION_NARROW_NOTE_2026-05-17.md`

2. **Paired runner:**
   `scripts/frontier_extension_lane_b_protects_lane_a_joint_composition_narrow.py`
   THEOREM PASS=355 FAIL=0

3. **Cached output:**
   `logs/runner-cache/frontier_extension_lane_b_protects_lane_a_joint_composition_narrow.txt`
   exit_code=0, status=ok, elapsed ~0.17s.

4. **Block artifacts:** this report and `V1_V5_SCRATCH.md`.

## What it derives

Composition theorem: under the retained single-clock joint circuit, a
successful native taste-qubit teleportation at `t_B` followed by an
arbitrary CPTP setting at Bob's location at `t_C > t_B` cannot alter the
operational marginal of Alice's earlier record at `t_A < t_B`.

The runner builds a 3-time joint circuit (Alice + Bell + Bob taste
qubits) and verifies six joint properties (J1, J1b, J2, J3, J4a, J4b)
across 14 input states (6 axis probes + 8 random) and 6 later settings
(identity, Hadamard, dephasing, memory reset, Loschmidt echo,
depolarizing).

(J1) Bob pre-message reduced state = I/2 for every input (Lane A
no-signaling, re-verified in the joint circuit).

(J1b) Teleportation channel delivers the input deterministically
(protocol is real, not a vacuous "Bob ignores everything" construction).

(J2) P(a at t_A) is uniform 1/4 on the 4 Bell outcomes and is invariant
under every later CPTP setting at t_C.

(J3) Bob's local state at t_C does respond to choice of x (fairness
witness: trace distance 1.0 between Bob H vs Bob I applied to |+>;
no-signaling at t_A is therefore not vacuous).

(J4a) Conditional P(a|x) equals marginal P(a) for every input and every
setting.

(J4b) Positive control: future postselection (Bob projected on |0>)
DOES bias the retrodicted record distribution (bias 0.15). This is the
standard postselection exception explicitly excluded by Lane B's
theorem; it is included as a control to show the protection statement
is doing real work, not a tautology of trace preservation.

## V1-V5 distinctness

V1, V2, V4, V5 ruled out in scratch (audit-data-touching meta-claim,
gate-text parsing exercise, name-only audit, syntactic modal-logic
identity). V3 chosen: joint composition theorem.

Distinct from:

- Lane A no-signaling audit (single-slice statement at t_B; no t_C
  setting).
- Lane B no-past-signaling theorem (no teleportation channel in setup).
- Prior blocks 01-17 (none touched the frontier_extension lane).

## What it does NOT close

- Lane-opening note itself (still planning).
- Lane C (signed gravity) — verdict unchanged.
- Postselected / final-boundary / directed-cycle theories.
- Lane A no-signaling derivation (imported as hypothesis).
- Single-clock surface itself (imported as hypothesis).
- Interacting CPT, advanced fields, matter teleportation.
- Manuscript-surface or claim-row status.

## Hard rules compliance

- A_min only: no new framework primitives. Imports only the two
  already-landed lane theorems (teleportation no-signaling, chronology
  no-past-signaling) and the retained single-clock + Hilbert + Bell
  surfaces.
- Source-only PR: no CANONICAL_HARNESS_INDEX, DERIVATION_ATLAS,
  DERIVATION_VALIDATION_MAP, audit-data, README, lane-registry, or
  STATE.yaml touches.
- No main push; PR is non-merging.

## Honest status string

`positive_narrow_composition_theorem`

The lane-opening note advances from "unaudited" toward "audited
sub-claims landed" but is not closed by this block.
