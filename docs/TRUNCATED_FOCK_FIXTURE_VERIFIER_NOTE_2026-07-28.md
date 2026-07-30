# Truncated-Fock fixture verifier

Date: 2026-07-28

Authority: none

Audit: unset

Status: exact support

Claim type: meta

Primary runner:

- [`frontier_truncated_fock_fixture_verifier_2026_07_28.py`](../scripts/frontier_truncated_fock_fixture_verifier_2026_07_28.py)

Independent checker:

- [`frontier_truncated_fock_fixture_verifier_independent_check_2026_07_28.py`](../scripts/frontier_truncated_fock_fixture_verifier_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
qualification, primitive, registry, policy, queue, audit result, or audit
status. It is non-authoritative test infrastructure and derives no physics.

## Scope

This package is a standalone fixed-pin verifier for the already-landed
[truncated-Fock equal-split support](TRUNCATED_FOCK_EQUAL_SPLIT_SUPPORT_NOTE_2026-07-28.md)
and its clean-room checker. It is context beside, not a registration in, the
[source acceptance harness](SOURCE_ACCEPTANCE_HARNESS_SUPPORT_NOTE_2026-07-28.md).
It exposes no candidate scientific input and adds no surface to that parent
harness.

The verifier reruns both landed scripts with immutable source hashes, extracts
their bounded contract, and classifies that exact record using an internal
fixed expectation. Its public classification mode accepts a JSON record on
standard input only so the independent checker can exercise the verdict path.
The record is evidence data, not a physical input to the truncated-Fock
calculation.

The independent checker does not import the verifier or either landed
scientific runner. It reconstructs the six-mode mask and reversal-channel
counts, checks the strict truncated/full column distinction, reruns the landed
scripts directly, differentially exercises the public classifier, and proves
its test would catch an always-accept classifier mutation.

## Exact boundary

- Certified science remains only the supplied
  `n_left,n_right <= 2` two-cell slice: 22 local masks and 6,776 columns.
  Number layers `n=3,4,5,6` and the 57,344-column complete six-mode space are
  outside this verifier.
- This is not a full-Fock construction, a full-Fock acceptance port, or a
  campaign-completion result. A genuine candidate input port and broader
  full-Fock coverage remain open.
- The equal `(1,1)` split is supplied, not selected by conservation. Every
  real split `(alpha,2-alpha)` has the same conserved total.
- The neutral labels are `matter`, `component_1`, and `component_2`. Optional
  names described by the separate
  [component-naming note](TRUNCATED_FOCK_COMPONENT_NAMING_NOTE_2026-07-28.md)
  do not construct distinct carrier degrees of freedom.
- Static source checks below are exact syntax and immutable-pin checks. They
  are not a semantic firewall and do not prove the absence of an unnamed
  physical law.
- No audit verdict is authored here. The underlying bounded theorem keeps its
  own audit and retention path.
