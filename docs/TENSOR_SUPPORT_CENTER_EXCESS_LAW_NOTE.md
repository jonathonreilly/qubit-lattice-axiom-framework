# Exact Support-Side `A1` Center-Excess Law and the Remaining Tensor Gap

**Date:** 2026-04-14  
**Script:** `scripts/frontier_tensor_support_center_excess_law.py`  
**Status:** exact support-side center-excess law on the whole canonical `A1`
family, plus a sampled tensor-law compatibility observation conditional on the
current chosen tensor observable

## Purpose

The projective-blindness note proved that the current exact shell/junction
toolbox cannot see the remaining scalar `A1` background datum at fixed total
charge.

That still left one key axiom-first question:

> after leaving the shell side, what exact microscopic scalar on the support
> block actually survives and can carry the last tensor law?

This note answers the support-side half of that question exactly. What it says
about the tensor side is narrower, and is stated as such below.

## Exact support-side statement

Work on the exact seven-site star support with the canonical `A1` basis

- `e0 = A1(center)`
- `s = A1(shell-average)`

and normalize `s` to unit total charge by `s / sqrt(6)`.

Let `phi_support = G_S q` be the exact support potential induced by the exact
support Green matrix `G_S`.

Then:

- the arm-site support potential per unit charge is identical for the two
  unit-charge `A1` endpoint backgrounds
  - `e0`
  - `s / sqrt(6)`
- the only exact difference between those two endpoint backgrounds on the
  support is the center excess

`phi_support(center) - phi_support(arm_mean) = 1/6`

with machine-precision residual.

So after fixing total charge, the exact `A1` support block retains one scalar
microscopic datum:

`delta_A1(q) = phi_support(center)/Q - phi_support(arm_mean)/Q`.

This is the support-side datum that survives the shell-blindness theorem.

## Exact canonical formula

For the canonical `Q = 1` projective `A1` family

`q_A1(r) = (e0 + r s) / (1 + sqrt(6) r)`

the support-side scalar is exactly

`delta_A1(r) = 1 / (6 (1 + sqrt(6) r))`.

### Why this holds for the whole family, not only at sampled `r`

The map `q -> phi_support = G_S q` is linear, so the unnormalized center-excess
numerator

`n(q) = phi_support(center) - phi_support(arm_mean)`

is a linear functional of `q`. Every member of the canonical family is the
fixed-total-charge combination

`q_A1(r) = (1 - t) e0 + t (s / sqrt(6))`, with `t = sqrt(6) r / (1 + sqrt(6) r)`,

of the two unit-charge endpoint backgrounds, and every member carries total
charge `Q = 1`, so the normalization by `Q` is the same at every `r`. Linearity
therefore gives

`delta_A1(q_A1(r)) = (1 - t) delta_A1(e0) + t delta_A1(s / sqrt(6))`,

and the two endpoint values are exactly `1/6` and `0`. Substituting `t` returns
the displayed closed form. So the law holds for every real `r >= 0` on the
canonical family, not only at the values the runner happens to evaluate. The
runner's explicit linearity test and its dense `r` sweep are witnesses of this
derivation, not its source.

So the surviving microscopic scalar is no longer an abstract projective
parameter. It is an explicit exact support-side center-excess observable.

## Bounded tensor-law consequence

Everything in this section is conditional and sampled. It is a statement about
one specific chosen tensor observable, evaluated at one specific finite list of
backgrounds. It is not a statement about the projective `A1` family as such.

**The observable this is conditioned on.** The tensor coefficients `gamma_E`
and `gamma_T` used here are not exact quantities. Each is a central
finite-difference derivative, taken with step `EPS = 0.005`, of the `eta` floor
returned by `tensor_metrics` in
`scripts/frontier_tensor_boundary_drive_two_channel.py`, normalized by the
`anchor_per_Q` value returned by `reduced_data` in
`scripts/frontier_one_parameter_reduced_shell_law.py`. Changing that observable,
that normalization, or that finite-difference step changes the numbers reported
below, and the statement would then have to be re-derived.

**The affine law is fitted, not derived.** The runner fixes an affine law in
`delta_A1` by interpolating the two `A1` support endpoints

- center background `e0`
- shell background `s / sqrt(6)`

and then evaluates that fitted law elsewhere. Nothing in this note derives the
slope or the intercept; both are read off those two endpoints.

**Where the fitted law was actually tested.** It was evaluated at exactly eight
backgrounds:

1. the six canonical `A1` samples `r = 0.25, 0.5, 0.75, 1.0, 1.5, 2.0`
2. the `exact local O_h` `A1` baseline
3. the `finite-rank` `A1` baseline

**What was observed there.** At those eight tested backgrounds, and only there:

- across the six canonical `A1` samples the maximum affine-law error is of
  order `1e-8`
- across the two named baselines the maximum affine-law error is at the
  `few x 1e-6` level already seen in the earlier projective-compatibility note

Those two figures are observed maxima over the eight tested points. This note
makes no claim about the affine law's error at any other `r`, at any other
background, or for any other tensor observable.

## Interpretation

On the support side the statement is exact and holds for the whole canonical
family: after fixing total charge, the microscopic support block retains one
explicit scalar datum,

- center excess at fixed total charge

and the shell side is blind to it.

On the tensor side the statement is much narrower. At the eight tested
backgrounds, with the current chosen tensor observable and finite-difference
step named above, the bright coefficients are numerically compatible with an
affine law in `delta_A1` whose two constants were fitted from the two endpoint
backgrounds. That is a sampled compatibility observation, not a derived tensor
law.

So the forward target keeps its shape and is better organized:

1. derive the exact tensor observable on the support block
2. derive the exact tensor endpoint coefficients at
   - `e0`
   - `s / sqrt(6)`
3. then ask whether an affine support law in `delta_A1` follows for the family,
   rather than holding only at tested backgrounds

## What this narrows, and what it opens

What it narrows: on the support side, the surviving scalar is no longer a
generic function on the projective `A1` manifold. It is an exact center-excess
observable with a closed form valid on the whole canonical family, carried by

- one exact support-side scalar `delta_A1`

What it opens: a sharp, checkable question on the tensor side. The affine
compatibility seen at the eight tested backgrounds is a lead, not a theorem.
The next path this opens is to derive the tensor observable and its two
endpoint coefficients, and then to test the affine form against a continuous
family the way `delta_A1` is now tested.

## What this still does not close

This note still does **not** close:

1. the exact tensor boundary observable itself
2. the exact tensor endpoint coefficients
3. the full restricted tensor completion theorem
4. full nonlinear GR

## Practical conclusion

The current best gravity target is now:

> derive the exact tensor observable on the microscopic `A1 x {E_x, T1x}`
> support block and its two `A1` endpoint coefficients. If that lands, the
> support-side scalar it would be evaluated against is already exact on the
> whole canonical family.

## Downstream hygiene (2026-07-25)

Downstream work may cite the exact support-side statements — the endpoint
center excess `1/6` and the continuous-family `delta_A1(r)` law — without
further conditioning. The tensor-law statements in this note are sampled and
conditional: they hold for the current chosen tensor observable named above, at
the six canonical samples and two baselines actually tested, and must be
re-derived before being used at any other background or with any other tensor
observable.
