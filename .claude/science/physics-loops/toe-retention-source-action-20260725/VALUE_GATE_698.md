# Promotion Value Gate — Cycle 698

Answered in writing before the PR. Not an audit certificate; predicts no audit
verdict.

## V1 — What specific verdict-identified obstruction does this PR close?

It does not close one; it converts one from a blob into a classified shape.
Verbatim from the audit verdict on
`ac_reta_hclass_hunit_readout_derivation_obligation`:

> "Record additivity and the approved primitives do not themselves determine
> the carrier, source action, or dimensionless readout normalization."

M1 explains why Record additivity cannot itself supply an irreducible
multi-record term in the scalar readout. It does not exclude a separate action
or dynamics and does not assert that every source action is two-body. M2
classifies what the minimal relational pair extension looks like under its
named conditions. The
`gate_b_farfield_note` clause "source field ... propagation/action rule" is the
same object seen from the gravity side.

## V2 — What new derivation does this PR contain?

The prior-art refresh separates applications from new content. Cycle 693 on
`main` already proves the arbitrary-finite singleton factorization, so (1)
intersecting the two-body cluster space with strict additivity is its explicit
interaction-term corollary. The landed proper-cubic kernel classification
already proves the general orbit classification and range-1
`span{I, Delta}` identity, so (2) the one-constant pair shell and (4) the
operator-family agreement are scoped applications/consistency checks. The
durable marginal content here is (3) the relational pair-readout
interpretation, including the exact cross-bond additivity defect and the field
as the marginal readout cost of a test record.

## V3 — Could the audit lane already complete this from retained primitives plus standard math?

Partly, and the note says so. The singleton factorization is already Cycle 693,
the proper-cubic orbit classification and range-1 operator family are already
the landed classification note, and invariants of a finite group action being
functions on its orbits is standard. In particular,
`CUBIC_ORBIT_REYNOLDS_PROJECTOR_NARROW_THEOREM_NOTE_2026-05-10.md` already has
the Reynolds identity for a direction-stabilizer `D_4` action; that note is
cited explicitly in the dependency section. What is not available to the audit
lane is the combined scoped application: the exact semantic boundary between
strict and separated additivity, the cross-bond defect, and the test-record
marginal interpretation. The audit verdicts currently record only that the
source action is undetermined.

## V4 — Is the marginal content non-trivial?

Yes, but narrower than first submitted. "Additivity kills every pair
coefficient" is a finite exact reproduction of Cycle 693's general theorem,
not a new theorem. The new reusable content is the cross-bond defect and
marginal test-record interpretation; M5 is a consistency reproduction of the
landed operator family.

## V5 — Is this a one-step variant of an already-landed cycle?

No, and the closest comparison is the unlanded cycle 697 in the parent branch.
697 was negative: its valid narrow statement says a content-only additive
readout cannot supply a nonzero duplication-invariant/intensive field; the
rejected "cannot be dimensionless" wording was false. 698 is positive: it
classifies the minimal relational object that can supply a site-anchored
marginal and computes its conditional parameter count. 697 contains no two-body object, no
cluster expansion, no marginal-cost identity, and no source-side derivation.
The overlap is the octahedral orbit machinery, which is a shared method, not a
shared result. Against landed cycle 693: 693 has no site index and no
interaction term at all.

**Verdict: PR allowed.** V3 is answered with an explicit partial concession and
a citation rather than a claim of novelty.

## Cluster cap

Second PR in the readout/source-action parent family this campaign. The
cluster-cap evaluator applies from the third; not triggered here. If a third is
proposed, the evaluator must run first.

## Stacking — resolved

This block originally stacked on the campaign's first block. That block was
**rejected as submitted** by review-loop on PR #5620; only its abstract kernel
classification was salvaged and landed, as
`PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25.md`.
As the contingency above anticipated, this block was rebased onto `main` off
the rejected commits, and its citations were repointed at the landed salvage.

The reviewer's findings were then applied to this block as well — see the
repair commit. The most important is that the earlier block's
"no nonzero Record readout is dimensionless" was an overclaim: the record count
is a dimensionless extensive counterexample, and only the intensive
(duplication-invariant) statement was ever proved. Nothing in M1-M5 depended on
the overclaimed form; the wording is corrected and the correction is stated in
the note so it is not repeated downstream.
