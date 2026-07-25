# Promotion Value Gate — Cycle 699

Answered before the PR. Not an audit certificate; predicts no audit verdict.
Prior-art sweep evidence is recorded in `ROUTE_PORTFOLIO.md` per the workflow
step that landed on `main` as PR #5611.

## V1 — obstruction

Verbatim, audit verdict on `ac_reta_hclass_hunit_readout_derivation_obligation`:

> "Record additivity and the approved primitives do not themselves determine
> the carrier, source action, or dimensionless readout normalization."

and on `gate_b_farfield_note`:

> "cite or derive retained connections from the accepted framework premises to
> the growth rule, source field, propagation/action rule, and TOWARD/F~M
> physical readout ..."

This cycle does not close either. It converts "source action" from an
unmeasured residual into a counted one: five independent couplings at
nearest-neighbour range, with an exhibited basis.

## V2 — new derivation, with the sweep that establishes it

**Searched commit `ab6e6bd8d96fb5b7f1fe6712a7bb426c8df1c1e1`**, refreshed with
`git fetch origin main:refs/remotes/origin/main` immediately before the sweep.
Eight searches S1–S8 with commands, hits, and per-hit classifications are
tabulated in `ROUTE_PORTFOLIO.md`. Summary: no landed note counts covariant
two-body couplings on the six face displacements; S5 and S8 return nothing;
S1/S2/S4/S6/S7 hits are nonmatching or context-only and are individually
classified there.

One hit is adjacent and is cited in the note itself:
`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_..._2026-07-03.md`
asks the same proper-versus-full-cubic question on the same six directions, for
the admissibility rule rather than a readout kernel, with a complex-antilinear
improper action rather than an axial one. Different object, different answer
shape; the note defers to it on the framework's principled improper action.

New content: the 96 -> 6 -> 5 count with two independent derivations
(exact nullspace over `Q` and a Burnside character average), the channel census
(1 density-density, 1 mixed after exchange, 3 spin-spin), the exhibited
spin-spin basis, and the isolation of the chiral coupling as what the axiom's
word "proper" is responsible for.

## V3 — could the audit lane do it from retained primitives plus standard math?

Partly, and the note concedes it. Character theory and Reynolds averaging are
standard; the note cites the standard-math analogue. What is not available to
the audit lane is the axiom-side setup: which group acts, on what content
space, with which identification, and therefore which number comes out. The
three identifications are named as conditions in the note rather than
presented as axiom content.

## V4 — non-trivial?

Yes. Two independent computations of the same dimension agreeing is not a
restatement, and the exhibited basis is checked against all 24 group elements
at all 54 coefficient positions rather than on sampled inputs. The
proper-versus-improper result is a falsifiable structural finding: it predicts
exactly one coupling is lost, and the runner checks precisely that.

## V5 — one-step variant?

**Checked against `origin/main` at `ab6e6bd8d9`, not only against this
campaign.** No. Against cycle 698 (the parent branch): 698's kernel is scalar
and content-blind, a 6-parameter problem with answer 1; 699 is a 96-parameter
representation problem whose answer is 5, and 698 appears only as the
density-density special case. Against cycle 697: no content space at all.
Against landed `main`: S1–S8 found no counting result for this object.

**Verdict: PR allowed.**

## Post-review revision

The campaign's first block was rejected as submitted on PR #5620. This block
was rebased onto `main` off the rejected commits and revised to apply the same
findings: the supplied conditions (rational scalars, linearity, finite support,
covariance) are now a named fourth condition, the orbit-count theorem is
explicitly credited to the landed Reynolds-projector note rather than presented
as new, and the reference-normalization row is narrowed to intensive targets.

## Cluster cap — evaluator run and recorded

This is the **third** PR in the readout/source-action parent family, so the
cluster-cap evaluator was mandatory and was run before opening it, as an
independent codex `gpt-5.6-sol` xhigh seat in an isolated worktree at the
proposed head, with the skill's evaluator brief and no write access to the
repo.

**Evaluator verdict: `OPEN`** — "though narrowly". Its reasoning: the load-
bearing delta is real because 697/698 use scalar content-blind kernels while
699 introduces the Hermitian real form of `M_2(C)`, the trivial-plus-vector
representation, and the tensor action on two contents; the claim type is a
representation-theoretic census rather than a minimality/compatibility result;
and independent review has substantive new work in checking the three
identifications.

Those three questions the evaluator raised are now named explicitly in the
note as conditions rather than left for a reviewer to discover.
