# Bloch-projector acceptance fixture for the Cycle-317 support surface

Date: 2026-07-28

Authority: none

Audit: unset

Status: exact support (projector fixture)

Claim type: meta

Runners:

- [`frontier_born_acceptance_harness_2026_07_28.py`](../scripts/frontier_born_acceptance_harness_2026_07_28.py)
- [`frontier_born_acceptance_independent_check_2026_07_28.py`](../scripts/frontier_born_acceptance_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. It adds a support-only regression fixture.

## Result up front

The primary runner checks four supplied axis directions against the landed
Cycle-317 `projector_bloch` helper and freezes four malformed-feed behaviors.
The independent checker derives the closed-form projector

`P(n) = [[1+n_z, n_x-i n_y], [n_x+i n_y, 1-n_z]] / 2`

without importing the primary. It matches the landed helper on six axes and
96 non-axis rational unit vectors, for 102 vectors total.

This is deliberately not a test of the wider Cycle-317 ternary-menu,
split/merge, dilation, trace-functional, or release surface. It is not a
standing or canonical Born-lane acceptance surface.

## Exact fixture boundary

The four lawful fixtures are the supplied directions `+x`, `-x`, `+y`, and
`+z`. They exercise only `projector_bloch`. The four refusal fixtures are:

- wrong arity, refused by the harness schema;
- a non-normalized direction, refused by the landed helper;
- an out-of-domain direction, refused by the landed helper;
- a Boolean entry, refused by the harness schema.

The schema checks exact keys and kind, a three-entry list, finite JSON numeric
entries, and Boolean exclusion before dispatch. Cross-ID tests show that the
schema result depends on the feed content rather than on the fixture name,
including integers too large for finite floating-point coercion. Schema and
fixture-registry refusals have distinct signatures, and each observation's
origin agrees exactly with the component named by its enforcement label.

## Reproducibility and adversarial controls

- Every mutable repository file in the reconstructed runtime closure is
  declared literally in `AUDIT_INPUT_PATHS`; the independent checker also
  declares the primary runner.
- Child processes run from `scripts/` with inherited `PYTHONPATH` removed.
- The landed bridge has an independently repeated SHA-256 pin.
- The complete normalized child-driver AST is pinned. Alias mutation, dynamic
  lookup, explicit synthesis, and extra-statement variants all change that
  pin.
- The comparator requires exact outer and nested key sets, finite numeric
  values, and the declared tolerance. Its mutation census covers feed, origin,
  status, matrix, every summary family, exception type, message, missing and
  extra keys, nonfinite/type cases, oversized integers, and the tolerance
  boundary. Oversized numeric observations fail closed as `DRIFT`.
- A one-byte sandbox copy reaches `DRIFT` through the same production pin
  predicate used for live inputs. Both runners check that the real bridge hash
  and filesystem stat token remain unchanged.
- The independent checker hard-codes the complete primary source hash together
  with the bridge and driver pins, pins the normalized AST of five production
  functions, and explicitly rejects a frozen-table mutation that leaves the
  child driver dead. It uses an exact-rational projector oracle, repeats
  malformed type/finite/provenance probes, and runs the primary under the clean
  environment contract without importing it.

Cache logs are reproducibility aids only. They confer no claim or audit
authority. No separate receipt or self-certificate is part of this package.

## Physics and support boundary

All directions and expected fixture identities are supplied apparatus data.
The runners select no Born law, weight map `w(E)`, normalization rule,
probability content, outcome, occurrence, calibration, or Record. They do not
move the Born lane's open physics and make no Nature- or retained-grade claim.

The only positive statement here is executable agreement between a narrow
landed projector helper and independently fixed support fixtures. Historical
Cycle-317 results remain context, not newly admitted premises.

## Audit compatibility

This note is infrastructure-only `meta` material. Such rows do not enter the
ordinary claim-audit queue, so this note promises no later audit verdict. The
citation graph exposes the independent checker and the dynamic landed helper
for restricted-packet review. Review-loop validation may assess this support
package; it does not apply an audit verdict.

## Open boundary

Candidate-input coverage of the actual ternary-menu, split/merge, dilation,
trace-functional, and release surfaces remains absent. A future package would
need independently derived fixtures for those surfaces and separate,
appropriately typed source claims. No such coverage or physics conclusion is
inferred here.
