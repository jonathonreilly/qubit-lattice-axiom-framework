# Source acceptance harness — exact support tool

Date: 2026-07-28

Authority: none

Audit: unset

Status: exact support

Claim type: meta

Primary runner:

- [`frontier_source_acceptance_harness_2026_07_28.py`](../scripts/frontier_source_acceptance_harness_2026_07_28.py)

Independent checker:

- [`frontier_source_acceptance_harness_independent_check_2026_07_28.py`](../scripts/frontier_source_acceptance_harness_independent_check_2026_07_28.py)

Constitutional effect: none. This tool changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. It has no score or retention effect and derives no physics.

## Scope

This package gives reproducible candidate tests around three already-landed
surfaces:

- the [oriented tensor-source lift](SIGNED_GRAVITY_ORIENTED_TENSOR_SOURCE_LIFT_NOTE.md);
- the [Cycle-322 two-source recoil fixture](work_history/repo/review_feedback/TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CYCLE322_NOTE_2026-07-18.md);
- the [Cycle-294 three-route synthesis](work_history/repo/review_feedback/PHYSICAL_M2_GRAVITY_SOURCE_BRIDGE_TOURNAMENT_SYNTHESIS_CYCLE294_NOTE_2026-07-17.md), whose subprocess contract retains the separate [route A](work_history/repo/review_feedback/DIRECT_GATEWISE_MATTER_MEDIATOR_CURRENT_LEDGER_ROUTE_A_CYCLE293_NOTE_2026-07-17.md), [route B](work_history/repo/review_feedback/LOCAL_M2_MASS_SCALAR_DEFORMATION_RESPONSE_ROUTE_B_NOTE_2026-07-17.md), and [route C](work_history/repo/review_feedback/GRAVITY_ROUTE_C_BOUNDED_DIRECT_CURRENT_SEARCH_NOTE_2026-07-17.md) checks.

The two runners declare the complete mutable repository-input closure used by
these checks. Their caches therefore bind the landed source scripts, imported
helpers, subprocess targets, and notes read by those targets.

## Acceptance surfaces

Each class has a fixed class-level SHA-256 pin for its landed source. Callers
cannot replace that pin. Source drift produces `DRIFT`; malformed candidates,
nonzero child exits, timeouts, malformed child output, and schema or finiteness
failures produce fail-closed records rather than scientific verdicts.

- `TensorLiftAcceptance.accept(source_vector)` is the only candidate input
  port. It requires one real finite numeric vector of length 10 and always uses
  the landed, nonempty Ward-constraint matrix returned by the pinned tensor
  runner. A caller cannot supply a vacuous replacement constraint.
- `RecoilReciprocityAcceptance.accept(fixture_selector)` selects only the
  landed canonical fixture or the fixed `swap_coin_fswap` perturbation. It is
  not an operator-matrix or model-dictionary port. Acceptance requires a
  successful child exit, exactly 20 labeled outcomes, the frozen integer
  fixture invariants, and no child exceptions.
- `TypedBridgeAcceptance.accept()` has no candidate port. It runs the pinned
  Cycle-294 verifier in a subprocess and checks the frozen five outcomes,
  counts, and the literal `ROUTES` contract rows extracted from the pinned
  source.

The self-test checks canonical acceptance, corrupted-input rejection, exact
four-label rejection for the swapped recoil fixture, wrong-pin drift, and the
typed-bridge route table.

## Independent check

The independent checker never imports the harness module. It extracts only
literal frozen data and method predicates from the harness source, recomputes
the tensor and recoil records directly from the landed modules, executes the
pinned Cycle-294 runner independently, and extracts Cycle-294 `ROUTES` directly
from its abstract syntax tree. It pins the complete normalized syntax trees of
all three verdict methods and both candidate-input methods, independently
classifies `ACCEPT`/`REJECT`/`DRIFT` vectors for all three classes, and checks
the exact Tensor field/operator/threshold predicate mapping. Differential
vectors cover malformed objects, malformed outcome rows, non-finite nested
runtime fields, record-carried pin drift, and the fixed recoil perturbation.

## Boundary

This is a non-authoritative testing tool. Passing a fixture test does not
select or establish an energy, stress, resource, reciprocal-response,
sign/scale, gravity, or Born rule. Any later construction remains governed by
its own source note, review gates, and independent audit.
