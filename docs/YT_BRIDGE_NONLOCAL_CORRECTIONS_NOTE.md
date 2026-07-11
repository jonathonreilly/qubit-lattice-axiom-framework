# Endpoint-Response Affine-Remainder Theorem for the `y_t` Bridge Model

**Date:** 2026-04-15 (analytic replacement 2026-07-11)
**Claim type:** bounded_theorem
**Status:** proposed_retained bounded theorem on the stated scalar transport
surface; independent audit is required before effective retained-grade status
**Primary runner:**
[frontier_yt_bridge_affine_remainder_theorem.py](../scripts/frontier_yt_bridge_affine_remainder_theorem.py)
**Diagnostic companion:**
[frontier_yt_bridge_nonlocal_corrections.py](../scripts/frontier_yt_bridge_nonlocal_corrections.py)

## Claim-state declaration

```yaml
actual_current_surface_status: proposed_retained
target_claim_type: bounded_theorem
claim_type_reason: "Uniform endpoint-kernel and affine-remainder inequalities over explicitly stated scalar-transport hypotheses."
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: true
proposal_allowed_reason: "Review-loop passed the calibration-free bounded scalar theorem with no open imports on its claim surface; physical YT reuse is excluded and independent audit remains required."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## The problem with the old claim

The old version called the residual after an affine fit a “nonlocal
correction” and attached the number `5.024e-3` to it. Two separate issues
prevent that statement from carrying theorem authority.

First, subtracting an affine function does not distinguish local physics from
nonlocal physics. It only measures the failure of an affine approximation.
The residual is therefore called the **affine-projection remainder** below.

Second, the old runner used the wrong adjoint sign. For a scalar initial-value
problem `y' = F(s,y,q)`, the derivative of the terminal value with respect to a
source perturbation is

`K(s) = exp(integral_s^T F_y(u) du) F_q(s)`,

not the same expression with a negative exponent. A direct central finite
difference agrees with the positive exponent and rejects the old sign.

This note replaces the calibrated residual claim with an analytic theorem
uniform over its stated inputs. No target `y_t`, Standard Model boundary value,
bridge-profile family, profile grid, or fitted selector appears in the proof.

## The stated transport surface

Let `I = [s_0,T]` have length `h = T-s_0`, let `G` and `q` lie in `C(I)`,
and fix `y(s_0)=y_0>0`. Consider the scalar transport equation

`y' = F(s,y,q) = c y [-d y^2 + G(s) + e q(s)]`,

where `c,d,e > 0`. The terminal map below is defined on an open neighborhood
`U` of the base source `q` in `C(I)` on which the corresponding solutions exist
on `I`. For the positivity/convexity part of the theorem, the base trajectory
obeys `G(s)+e q(s) >= 0` and `y(s)>0` on `I`.

This is an explicitly stated mathematical surface. The theorem does **not**
claim that the minimal lattice axioms derive this scalar equation, its
coefficients, its source `q`, or its identification with the exact interacting
lattice bridge. That action-to-transport bridge remains open.

## Theorem

Let `D_T:U -> R` denote the terminal map `q -> y(T)`, with `C(I)` carrying its
sup norm. Then:

1. `D_T` is Fréchet differentiable. For every `phi` in `C(I)`,

   `D D_T[q](phi) = integral_I K(s) phi(s) ds`,

   where

   `K(s) = c e y(s) exp(integral_s^T F_y(u) du)`.

   This derivative extends uniquely to a bounded linear functional on
   `L2(I)`.

2. At every base trajectory with `G+e q >= 0`, the kernel is positive,
   increasing, and convex. More precisely,

   `K'/K = 2 c d y^2`,

   `K''/K = 4 c^2 d y^2 [G + e q]`.

3. Let `Pi_1 K` be the continuous `L2(I)` orthogonal projection of `K` onto
   the affine subspace `span{1,s}`, and let `R = K-Pi_1 K`. Then

   `integral_I R ds = integral_I s R ds = 0`,

   and the residual endpoint functional has exact operator norm

   `sup_{||phi||_2=1} |integral_I R phi ds| = ||R||_2`.

   If `R` is nonzero, equality is attained by `phi = R/||R||_2`.

4. The remainder has the analytic curvature bound

   `||R||_2 <= h^(5/2)/sqrt(120) * ||K''||_infinity`

   `          = h^(5/2)/sqrt(120)`

   `            * ||4 c^2 d y^2 (G+e q) K||_infinity`.

5. If `Y = ||y||_infinity` and `H = ||G+e q||_infinity`, then a fully
   explicit relative form is

   `||R||_2 / ||K||_2`

   `  <= [4 c^2 d Y^2 H h^2/sqrt(120)] exp(2 c d Y^2 h)`.

These statements hold for the entire stated transport class. They do not use
a target endpoint or select a bridge profile.

## Proof

Linearizing `y'=F(s,y,q)` in a source direction `phi` gives

`z' = F_y z + F_q phi`, with `z(s_0)=0`.

Variation of constants therefore gives

`z(T) = integral_I exp(integral_s^T F_y(u)du) F_q(s) phi(s) ds`,

which gives the candidate derivative kernel. Here `F_q = c e y > 0`.

To verify that this is a Fréchet derivative rather than only a formal
linearization, write `y_eta` for the solution at `q+eta`, `w=y_eta-y`, and
let `z` solve the displayed linearized equation with `phi=eta`. On a bounded
solution tube around the base trajectory, the polynomial vector field has
bounded first and second derivatives. Continuous-dependence Grönwall gives

`||w||_infinity <= C_1 ||eta||_infinity`.

Taylor's formula for `F(s,y+w,q+eta)` then gives

`r' = F_y r + E`, with `r=w-z`, `r(s_0)=0`,

and

`||E||_infinity <= C_2 (||w||_infinity^2`

`                         + ||w||_infinity ||eta||_infinity)`.

A second Grönwall estimate therefore yields

`||r||_infinity <= C_3 ||eta||_infinity^2`.

Thus

`|D_T[q+eta]-D_T[q]-D D_T[q](eta)|`

`  <= C_3 ||eta||_infinity^2 = o(||eta||_infinity)`,

which proves Fréchet differentiability on `U` and validates the kernel formula.

Differentiate the logarithm of the kernel along the supplied solution:

`(log K)' = (log F_q)' - F_y = y'/y - F_y`.

For the stated cubic flow,

`y'/y = c[-d y^2+G+e q]`,

`F_y   = c[-3d y^2+G+e q]`.

Their difference is `2cdy^2`. A second differentiation gives

`K''/K = (2cdy^2)' + (2cdy^2)^2`

`      = 4c^2 d y^2(G+e q)`.

This proves positivity, monotonicity, and convexity without inserting any
physical boundary value.

The projection identities follow from the normal equations for the
orthogonal projection onto `span{1,s}`. Cauchy–Schwarz gives
`|<R,phi>| <= ||R||_2 ||phi||_2`; the normalized residual is the equality
witness, so this is the exact operator norm, not merely an upper estimate.

For the curvature bound, let `L` be the chord joining the endpoint values of
`K`. The standard interpolation remainder gives

`|K(s)-L(s)| <= (||K''||_infinity/2)(s-s_0)(T-s)`.

Because `Pi_1 K` is the best affine `L2` approximation,

`||K-Pi_1 K||_2 <= ||K-L||_2`.

Finally,

`integral_0^h u^2(h-u)^2 du = h^5/30`,

which yields the factor `h^(5/2)/sqrt(120)`.

For the relative form, `K_max/K_min <= exp(2cdY^2h)`,
`||K||_2 >= sqrt(h) K_min`, and
`||K''||_infinity <= 4c^2dY^2H K_max`. Combining these inequalities proves
the last claim.

## What is now closed

The endpoint-response kernel and its affine-remainder operator bound are now
derived from the stated scalar transport equation. The theorem is uniform in
the source profile and contains no viability filter or family search. It also
fixes two prior mathematical ambiguities:

- the adjoint exponent has the positive sign required by variation of
  constants;
- under a `C1` monotone coordinate bijection `s=s(x)`, the kernel density
  includes the Jacobian `|ds/dx|`.

The primary runner checks the symbolic derivative identities, the exact
projection moments, the curvature constant, the Riesz equality witness, the
coordinate Jacobian, and positive- and negative-control adjoint signs.

## Non-load-bearing regression diagnostic

The diagnostic companion still evaluates the old SM-like/logistic background,
but that evaluation is not evidence for the theorem and is not part of the
claim scope. After correcting the adjoint sign, using a trapezoidal
approximation to the continuous `L2` projection, inserting the exact `x=0.95`
cutoff, and including the coordinate Jacobian, it reports on `x>=0.95`:

- affine-remainder ratio `1.424e-4`;
- affine-remainder operator norm `2.313e-5` with respect to `dx`;
- maximum pointwise relative remainder `3.437e-4`;
- analytic curvature upper bound `7.430e-5`.

These values are a regression diagnostic for one calibrated trajectory. They
are not first-principles physical predictions, are not used by any PASS gate
in the primary runner, and must not be used to identify the remainder as a
nonlocal interaction.

## Exact remaining blocker

The theorem does not derive the scalar transport equation from the exact
interacting lattice action. The remaining Nature-grade question is therefore
sharp:

> derive a retained action-to-transport bridge that identifies the exact
> interacting lattice endpoint derivative with the scalar source equation
> above, or replace that equation by the actual operator derivative and prove
> the corresponding curvature estimate there.

Until that bridge exists, this is candidate bounded-theorem mathematics on the
explicitly stated transport surface, while its physical `y_t` reuse is
conditional support only. Independent audit remains required.

## Claim scope for independent audit

The auditable claim is the calibration-free theorem in “Theorem” above: the
Fréchet kernel formula, its exact derivative identities, the continuous
affine-projection operator norm, and the curvature/relative bounds for the
stated scalar transport class. The calibrated numbers in “Non-load-bearing
regression diagnostic” and every exact-interacting-lattice interpretation are
outside that claim scope.
