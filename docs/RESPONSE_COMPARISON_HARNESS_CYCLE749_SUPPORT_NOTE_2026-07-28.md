# Cycle-320/322 diagonal-affine regression comparator — Cycle 749 support

Date: 2026-07-29

Authority: none

Audit: unset

Status: exact support (finite regression fixture)

Claim type: meta

Runners:

- [`frontier_cycle749_response_comparison_harness_2026_07_28.py`](../scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py)
- [`frontier_cycle749_response_harness_independent_check_2026_07_28.py`](../scripts/frontier_cycle749_response_harness_independent_check_2026_07_28.py)

Fixture:

- [`response_comparison_harness_cycle749_fixture_2026_07_28.json`](../outputs/response_comparison_harness_cycle749_fixture_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. It is a noncanonical support utility and has no retention effect.

## Result up front

Conditional on one committed finite fixture and two supplied software
thresholds, the primary comparator assigns these software labels:

| supplied diagonal-affine transform | label |
|---|---|
| identity | `ACCEPT` |
| uniform sign reversal | `REJECT` |
| matter-coefficient perturbation producing residual `4e-10` | `DRIFT` |
| uniform magnitude doubling | `REJECT` |

The identity row is true by construction. The other rows demonstrate only
that this fixed comparator distinguishes the listed output transformations
relative to the committed fixture. They do not evaluate a source-to-response
law.

`ACCEPT`, `DRIFT`, and `REJECT` are local software-classification labels.
They are defined by the supplied conventions
`strict_upper_bound = 3e-10` and `drift_upper_bound = 1e-6`; they are not
physical phases or audit statuses. `ACCEPT` requires every direct residual to
be strictly below `3e-10`, so a residual equal to that boundary is `DRIFT`.

## Conditional fixture

The normalized coefficient rows are reconstructed from the current
[Cycle-320 support surface](work_history/repo/review_feedback/UNIT_WEIGHT_CARRIED_LINK_RECOIL_CYCLE320_NOTE_2026-07-18.md).
The common supplied `sin(theta)^2` factor has been removed, leaving the
dimensionless coefficient ledger `(-2d,+d,+d)` for each of six supplied
directions.

The three finite `2 x 2` tables are copied from the current
[Cycle-322 support surface](work_history/repo/review_feedback/TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CYCLE322_NOTE_2026-07-18.md)
at its supplied sizes `L = 3, 4, 6`. They inherit that runner's supplied
`BETA = -0.3`, source law, preparation, update factors, finite geometry, and
completion choices.

The fixture is conditional regression data, not an admitted value registry.
It pins SHA-256 values for the complete current Cycle-320/322 Python source
closure. Both runners fail closed if any pinned source byte changes. A source
change requires deliberate fixture regeneration and a new review; refreshing
a cache cannot silently redefine the expected side.

## Comparator boundary

The comparator accepts seven supplied diagonal multipliers and offsets:
three act on the normalized coefficient vectors and four act on each flattened
response table. It compares transformed entries directly with the committed
entries. The reported zero-sum residual is subordinate diagnostic output; it
does not independently validate a transform. No norm, reciprocity, or
blind-test conclusion is attached.

This interface transforms already-produced fixture outputs. It has no
source-domain candidate input and supplies no scientific interpretation.
Passing it establishes only agreement with this finite regression artifact.

## Independent check and provenance

The second runner does not import the primary. It independently parses the
fixture with exact rational arithmetic, reimplements the transform and
classification rules, checks the equality boundary, exercises an in-memory
fixture mutation, and then compares its results with a clean subprocess run of
the SHA-pinned primary.

Both runners declare the fixture and every member of its pinned source closure
through `AUDIT_INPUT_PATHS`; the second runner additionally declares the
primary. The citation graph registers the separately executable checker.
Cache logs are reproducibility aids only and confer no claim or audit
authority. No self-certifying receipt is part of the package.

## Scope

This package contributes executable software support only. The historical
Cycle-320/322 documents remain provenance for supplied fixtures, not authority
for a wider conclusion. Any later scientific construction must define and
review its own inputs, candidate interface, semantics, and acceptance evidence.
