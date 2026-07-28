# Source acceptance harness — support note (evidence-ceiling program)

Date: 2026-07-28

Authority: none

Audit: unset

Status: exact support (acceptance infrastructure)

Claim type: meta

Runners:

- [`frontier_source_acceptance_harness_2026_07_28.py`](../scripts/frontier_source_acceptance_harness_2026_07_28.py)
- [`frontier_source_acceptance_harness_independent_check_2026_07_28.py`](../scripts/frontier_source_acceptance_harness_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status, and it derives no physics.

## Why

The time lane's evidence ceiling rests on decisive frozen-output decoders
(the Cycle-610/612 interval quadruple and causal-order outcomes) that any
construction can be tested against byte-pinned and unchanged. The
gravity/source lane had no analog: the landed tensor lift is
scalar-only-conditional, the Cycle-294 bridge is a contract verifier with
no input port, and the Cycle-322/320 surfaces certify fixed fixtures
(Cycle 725 recorded the no-input-port findings). This package supplies
the missing acceptance infrastructure — it raises what is decisively
testable, and source-lane scores move only when constructions pass it.

## What it provides

Three acceptance classes over the LANDED surfaces, each carrying the
landed file's SHA-256 pin (construction refuses on drift), a frozen
expected-outcome record, and an `ACCEPT`/`REJECT`/`DRIFT` verdict
classifier whose tolerances are copied verbatim from the landed checks:

- `TensorLiftAcceptance` — a true input port (`accept(source_vector,
  ward_constraints=None)`) running the landed tensor-lift checks
  unchanged on supplied length-10 arrays; frozen canonical record
  (projector ranks `1/3/1/5`, twist residual `0`, Ward at machine scale,
  locking signs);
- `RecoilReciprocityAcceptance` — a partial-argument port (the landed
  certificate entry points accept the operator triple and model dict
  where their contracts allow) with the frozen 20/20 outcome labels and
  exact integer fixture invariants;
- `TypedBridgeAcceptance` — the Cycle-294 verifier run byte-pinned in a
  subprocess with its frozen 5/0 outcome and an ast-extracted pinned copy
  of its `ROUTES` contract rows ("not one combined law" recorded). The
  typed bridge remains no-port; the harness states that limitation
  explicitly rather than pretending an input exists.

Self-test demonstrates ACCEPT on the landed fixtures (and on the
Cycle-725 role-uniform census reduction as a cross-anchor), REJECT on
corrupted inputs with the flipped checks reported, and DRIFT on a wrong
pin. The independent adversary re-derives the frozen records from the
landed modules directly, re-verifies the pins, and re-implements the
verdict classifier from extracted thresholds.

## Boundary

Acceptance infrastructure only, under the campaign's `C_source` firewall:
no energy/stress/resource law, reciprocal response, sign/scale law,
gravity identification, or Born content is selected or implied. New
physics enters the source lane only as constructions that pass these
harnesses, each under its own note, gates, and independent audit.
