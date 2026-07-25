# Promotion Value Gate — Cycle 698

Answered in writing before the PR. Not an audit certificate; predicts no audit
verdict.

## V1 — What specific verdict-identified obstruction does this PR close?

It does not close one; it converts one from a blob into a classified shape.
Verbatim from the audit verdict on
`ac_reta_hclass_hunit_readout_derivation_obligation`:

> "Record additivity and the approved primitives do not themselves determine
> the carrier, source action, or dimensionless readout normalization."

M1 explains *why* Record additivity cannot determine a source action — a source
action is a two-body object and the clause as read admits none — and M2
classifies what the minimal two-body extension must look like. The
`gate_b_farfield_note` clause "source field ... propagation/action rule" is the
same object seen from the gravity side.

## V2 — What new derivation does this PR contain?

Four results not on `main`: (1) the exact statement that intersecting the
two-body cluster space with strict additivity kills every pair coefficient;
(2) the range-1 pair kernel is exactly one constant under proper cubic
covariance, with displacement reversal shown to be already inside the proper
group; (3) the field is the marginal readout cost of a test record, an identity
the runner verifies exactly; (4) the source route and the law route land on the
same `span{I, Delta}` family.

## V3 — Could the audit lane already complete this from retained primitives plus standard math?

Partly, and the note says so. That the invariants of a finite group action are
functions on its orbits is standard, and
`CUBIC_ORBIT_REYNOLDS_PROJECTOR_NARROW_THEOREM_NOTE_2026-05-10.md` already has
the Reynolds identity for a direction-stabilizer `D_4` action; that note is
cited explicitly in the dependency section. What is not available to the audit
lane is the axiom-side accounting: which clause forbids the pair term, what the
minimal repair is, and that the repair's parameter count at range 1 is one. The
audit verdicts currently record only that the source action is undetermined.

## V4 — Is the marginal content non-trivial?

Yes. "Additivity kills every pair coefficient" is a computed nullspace
intersection with a 10-dimensional negative control, not a restatement. The
marginal-cost identity is a nontrivial exact identity. M5's agreement between
two independent classifications is a real consistency result.

## V5 — Is this a one-step variant of an already-landed cycle?

No, and the closest comparison is the unlanded cycle 697 in the parent branch.
697 is negative: it says a readout cannot be a field and cannot be
dimensionless. 698 is positive: it classifies the minimal object that *can* be
a field and computes its parameter count. 697 contains no two-body object, no
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
