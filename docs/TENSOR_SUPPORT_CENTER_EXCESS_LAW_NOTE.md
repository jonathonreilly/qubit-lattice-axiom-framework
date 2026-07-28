# Exact Support-Side Center-Excess Law in the Totally Symmetric Cubic Star-Support Sector (`A1`)

**Date:** 2026-04-14  
**Script:** `scripts/frontier_tensor_support_center_excess_law.py`  
**Type:** bounded_theorem
**Status:** exact finite-Dirichlet center-excess law in the totally symmetric
cubic star-support sector, plus a sampled tensor-compatibility observation
conditional on one chosen numerical observable

## Purpose

This note proves one finite-lattice support identity and records a separate,
strictly sampled tensor observation. It does not import a negative theorem.
It makes no exhaustive statement about any other support, shell, or tensor
observable.

## Exact finite-Dirichlet support statement

Let `H` be the unit-weight nearest-neighbor negative lattice Laplacian on the
`13^3` interior of the runner's size-15 cubic box, with zero Dirichlet boundary
values, and let `G = H^(-1)`. Restrict `G` to the center and its six nearest
neighbors to obtain the seven-site support matrix `G_S`.

In the totally symmetric cubic star-support sector (shorthand `A1`), use

- `e0` for unit charge at the center
- `s` for the normalized sum of the six arm basis vectors
- `q_shell = s / sqrt(6)` for charge `1/6` on every arm

For any support source `q`, define `Q(q) = sum_i q_i` and, when `Q(q) != 0`,

`delta_A1(q) = ((G_S q)[center] - mean((G_S q)[arms])) / Q(q)`.

The center stencil gives

`H e0 = 6 e0 - sum_a e_a`,

so `q_shell = e0 - H e0/6` and therefore

`G q_shell = G e0 - e0/6`.

Cubic symmetry makes the six arm values of `u = G e0` equal. Its center equation
is `6 u_center - 6 u_arm = 1`, so the shell endpoint is constant on the support.
Thus the two unit-charge endpoints have center excesses `1/6` and `0`:
`phi_support(center) - phi_support(arm_mean) = 1/6`.

This equality is exact for the stated operator; the runner's floating-point
residual is only a numerical witness.

## Exact canonical formula

For the `Q = 1` family in the totally symmetric cubic star-support sector,

`q_A1(r) = (e0 + r s) / (1 + sqrt(6) r)`,

the support-side scalar is exactly

`delta_A1(r) = 1 / (6 (1 + sqrt(6) r))`.

### Why this holds for every `r >= 0`

The unnormalized center-excess numerator is a linear functional of `q`. Every
family member is the fixed-charge combination

`q_A1(r) = (1 - t) e0 + t q_shell`,

where `t = sqrt(6) r / (1 + sqrt(6) r)`. Both endpoints have `Q = 1`, so

`delta_A1(q_A1(r)) = (1 - t) delta_A1(e0) + t delta_A1(q_shell)`.

Substituting the exact endpoint values `1/6` and `0` gives the displayed
formula. The runner's seeded linearity check and 201-point log-spaced sweep are
diagnostics of this derivation, not its proof.

## Bounded tensor-compatibility observation

Everything in this section is conditional and sampled. It concerns one chosen
numerical observable at one finite list of backgrounds, not the whole family.

**Chosen observable.** Let `eta(q)` be the nonspectral maximum-entry tensor
envelope returned as the first element of `tensor_metrics(phi(q))`. Its live
implementation path is documented by the
[`QUARK_ROUTE2_ETA_FLOOR_HF_BOUNDARY_NOTE.md`](QUARK_ROUTE2_ETA_FLOOR_HF_BOUNDARY_NOTE.md)
support surface. Let

`c_aniso(q) = reduced_data(phi(q))["anchor_per_Q"]`

on the bounded reduced-shell construction documented by
[`ONE_PARAMETER_REDUCED_SHELL_LAW_NOTE.md`](ONE_PARAMETER_REDUCED_SHELL_LAW_NOTE.md),
and define the actual anisotropic anchor

`A_aniso(q) = c_aniso(q) * Q(q)`.

For `Q(q) != 0`, the reported coefficients are the central finite differences

`gamma_X(q) = (eta(q + EPS v_X) - eta(q - EPS v_X)) / (2 EPS A_aniso(q))`,

with `EPS = 0.005`, `v_E = E_x`, and `v_T = T1x`. Thus the denominator used by
the runner is `anchor_per_Q * Q(q)`, not `anchor_per_Q` alone. The observable,
normalization, finite-difference step, and both cited support surfaces are
support-only conditions; none is promoted here to an axiom-derived tensor law.

**Fitted law.** The runner interpolates an affine function of `delta_A1` through
the two endpoint coefficients at `e0` and `q_shell`. It does not derive the
slope or intercept.

**Tested backgrounds.** The fitted function is evaluated at exactly eight
backgrounds:

1. the six `Q = 1` samples `r = 0.25, 0.5, 0.75, 1.0, 1.5, 2.0`
2. the `exact local O_h` totally symmetric baseline
3. the `finite-rank` totally symmetric baseline

At those eight points, and only there, the observed maximum errors are of order
`1e-8` on the six canonical samples and a few times `1e-6` on the two named
baselines. No error bound is claimed at another `r`, background, finite box,
observable, normalization, or finite-difference step.

## Interpretation and open work

The exact result is the finite-Dirichlet support identity and its
continuous-parameter formula. The tensor result is only numerical compatibility
at the eight listed backgrounds. It leaves open:

1. a framework derivation of the tensor observable
2. exact tensor endpoint coefficients
3. an affine tensor law beyond the tested points
4. a restricted tensor-completion theorem
5. full nonlinear general relativity

The appropriate next question is whether the observable and endpoint
coefficients can be derived independently; only then could an affine tensor law
be promoted beyond the current sampled evidence.

## Downstream hygiene (2026-07-25)

Downstream work may cite the exact finite-Dirichlet endpoint identity and
continuous-parameter `delta_A1(r)` formula with the operator conditions stated
above. The tensor statements remain conditional on the chosen observable,
`anchor_per_Q * Q(q)` normalization, `EPS = 0.005`, six canonical samples, and
two named baselines, and must be re-derived outside that scope.

One pre-existing text reader requires the literal compatibility token
`survives the shell-blindness theorem`. That token is retained here solely as
an inert parser fixture. It is not a scientific assertion, premise, dependency,
authority, or boundary of this note.
