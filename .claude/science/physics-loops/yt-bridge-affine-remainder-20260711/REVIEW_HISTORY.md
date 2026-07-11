# Review history

## Pre-review derivation check

- Reproduced the historical runner.
- Derived the correct positive adjoint exponent from variation of constants.
- Central finite difference: correct-sign relative error `3.8e-7`; old-sign
  relative error `3.25e-1` on the historical trajectory.
- Corrected cutoff-inclusive trapezoidal-projection diagnostic: remainder ratio
  `1.424406e-4`, not `5.023669e-3`.
- Primary theorem runner: `17 PASS / 0 FAIL`.
- Corrected diagnostic runner: `5 PASS / 0 FAIL`.

Formal review-loop disposition: `pass` after four scoped iterations.

## Iteration 1

Disposition: `block` pending narrow fixes.

Findings:

- formal linearization did not yet prove Fréchet differentiability;
- the source domain/regularity needed tightening;
- direct physical consumers still treated the old number as authority;
- the nonlinear cubic derivative needed an epsilon-convergence check;
- diagnostic input taxonomy and status wording needed correction;
- full branch-negative wording triggered the N1--N8 gate.

Fixes applied:

- added the bounded-tube continuous-dependence and quadratic-remainder
  Grönwall proof;
- added nonlinear cubic central-difference and quadratic-remainder checks;
- added `G,q in C(I)`, `y_0>0`, and open-neighborhood hypotheses;
- added the `G+eq=0` convexity boundary test;
- removed six direct physical dependency edges and added dated firewalls;
- inserted the exact diagnostic cutoff and renamed its projection honestly;
- expanded the diagnostic import inventory and added the no-go checklist.

Independent math check: the constant-source cubic equation was solved through
`r=1/y^2`; its exact derivative with respect to the source equals the integral
of the derived kernel to 50-digit arithmetic, and both derivative identities
agree pointwise.

## Iterations 2--4

- Code/runner re-review: load-bearing math and both runners pass. One stale
  publication-atlas meta row remains for later weaving under physics-loop
  policy; it does not chain-satisfy a theorem descendant.
- Physics/import/Nature re-review: `PASS WITH BOUNDED CLAIMS`; the narrow
  scalar theorem meets the author-side `proposed_retained` bar, while physical
  YT reuse remains open.
- Governance/no-go re-review: `PASS` after the N1--N8 evidence, residual
  anchors, primitive-registry link, and code-invalidation classification were
  corrected.

Final local disposition: `pass`. Independent audit is still required before
effective retained-grade status.

## Delivery verification

PR #5179 is open, non-draft, based on `main`, and mergeable. The audit-lane
check was in progress at initial verification. No merge or audit verdict was
performed by this loop.
