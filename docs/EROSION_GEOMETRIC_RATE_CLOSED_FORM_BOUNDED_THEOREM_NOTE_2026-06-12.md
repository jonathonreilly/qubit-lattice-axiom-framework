# Uniform-Sign Erosion Rate Closed Form for the Landed Path-Product Recurrence (Bounded)

**Date:** 2026-06-12
**Type:** bounded theorem draft
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_erosion_rate_closed_form_2026_06_12.py`
**Status:** source proposal; The audit lane grades.

## Claim

For the uniform-sign geometric branch of the landed erosion recurrence,

`p_j = (p_{j-1} + s epsilon) / (1 + s epsilon p_{j-1})`

and

`c_j = c_{j-1} * (1 - epsilon^2) / (1 + s epsilon p_{j-1})^2`,

the attractive fixed point is `p* = s`. Therefore the asymptotic per-step
branch-correlator decay rate is

`r(epsilon) = (1 - epsilon^2) / (1 + epsilon)^2 = (1 - epsilon) / (1 + epsilon)`.

The `s=+1` branch has `p*=1`; the `s=-1` branch has `p*=-1`; both give the same
closed rate.

## Verification

The runner first anchors to landed machinery: it gates internal consistency of
the recurrence with its closed path product at `1e-14`, reproduces the landed
`epsilon=0.6` first-step branch value `c=0.221453287197...`, and reproduces the
landed finite-window pre-asymptotic estimator at `epsilon=0.8`, namely
`0.3255283695...`, within `1e-3`. That landed `epsilon=0.8` anchor is distinct
from the asymptotic closed-form value `r(0.8)=1/9`. It also gates a nonconstant
`p` trajectory before convergence as an anti-fabrication check.

Sympy derives the fixed-point equation, simplifies the rate difference to zero,
and gates stability by simplifying `f'(p*) - (1-epsilon)/(1+epsilon)` to zero.
On the scoped domain `0 < epsilon < 1`, this is
`|f'(p*)| = (1-epsilon)/(1+epsilon) < 1`. A fixed numerical grid
`epsilon = {0.05, 0.1, 0.2, 0.3, 0.4}` gates the asymptotic recurrence rate
against the closed form at `1e-10`, gates `p_j -> p*` at `1e-12`, and checks the
same stability inequality on the grid.

The landed moderate epsilon window `[0.5, 0.8]` maps under the closed form to the
fixed rate interval `[1/9, 1/3]`, and the rate is decreasing on the checked grid,
matching the landed eta-direction tie.

## Boundary

The formula is not a mixed-sign path law. For the alternating branch starting at
`p=0`, the path oscillates `0 -> epsilon -> 0`, and the alternating two-step
factor product is EXACTLY 1 by algebra: the two `c` factors cancel exactly. Thus
alternation gives zero net erosion per two-cycle on this branch. The runner gates
this as a sympy identity, `factor1*factor2 == 1`, and includes a fixed
alternating counterexample at `epsilon=0.2`: the measured two-step geometric rate
is `1`, while the uniform-sign closed form gives `2/3`. This is the boundary of
validity, not a contradiction of the uniform-sign branch theorem.

## Scope

Scope is the uniform-sign geometric branch of the landed erosion model with
explicit domain `0 < epsilon < 1`. It does not claim a closed form for the
nonlinear threshold-count envelope, mixed-sign paths, finite-lattice scaling,
continuum behavior, or a new physical measurement derivation. The audit lane
grades.
