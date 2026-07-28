# Finite-Grid Self-Consistency Checks for the Poisson Field Equation

**Type:** bounded_theorem

**Scope:** Finite fixed-point convergence and screened-family comparisons for
the declared three-dimensional Dirichlet cubic-lattice protocol.

**Audit status:** This source note does not assign an audit verdict or effective
status.

## Context

This note tests a supplied family of field solvers in the density/field
fixed-point loop implemented by
[`frontier_self_consistent_field_equation.py`](../scripts/frontier_self_consistent_field_equation.py).
It previously treated a shared source sign and an integrated susceptibility
correlation as evidence that Poisson was preferred over a broad operator
family. The conditional audit and the finite diagnostic below show that those
two comparisons do not support that broad preference.

The safe result is narrower: Poisson converges on the declared finite protocol,
and unscreened Poisson is closest to the target beta within the tested
screened-Poisson subfamily. No continuum operator selection or uniqueness
claim is made.

## Supplied fixed-point protocol

The runner uses:

- a 3D cubic lattice with Dirichlet boundaries;
- wave number `k=5.0`, source width `sigma=2.0`, and coupling `G=0.5`;
- fixed-point mixing `0.3`, tolerance `1e-4`, and at most `30` iterations; and
- the runner's finite-grid `check_field_physics` beta estimator and one-axis
  monotonicity diagnostic.

The field equation is supplied to the loop. Convergence of that loop tests
compatibility with the numerical propagation protocol; it does not derive the
operator from the framework axioms.

## Numerical evidence

### 1. Poisson fixed-point convergence

At `N=20` and `N=24`, the Poisson iteration converges in approximately ten
iterations. Its field has the selected well sign, passes the runner's one-axis
monotonicity check, and has raw finite-grid beta near `1.28`.

The beta is a measurement of this finite estimator. It has no established
continuum interpretation. The separate downstream study
`docs/POISSON_SELF_CONSISTENT_BETA_CAVEAT_BOUNDED_DIAGNOSTIC_NOTE_2026-07-26.md`
records finite-fit behavior but is not used here as an upstream authority.

### 2. Deterministic alternatives after source-sign normalization

The Poisson solver's response to a positive source has the opposite sign from
the tested biharmonic, local, and inverse-square-kernel solvers. A shared
negative source therefore makes the old cross-operator attractiveness column
convention-dependent.

The bounded diagnostic
[`POISSON_RESPONSE_KERNEL_AND_SIGN_NORMALIZATION_FINITE_GRID_BOUNDED_NOTE_2026-07-26.md`](POISSON_RESPONSE_KERNEL_AND_SIGN_NORMALIZATION_FINITE_GRID_BOUNDED_NOTE_2026-07-26.md)
applies the coupling once and normalizes the source sign per deterministic
operator. All four iterations converge, have the selected sign throughout the
tested interior, and pass the parent runner's one-axis monotonicity diagnostic:

| rank by `abs(beta-1)` | operator | `beta`, N=20 | `beta`, N=24 |
|---:|---|---:|---:|
| 1 | biharmonic | `0.8762` | `0.8669` |
| 2 | inverse-square kernel | `1.2120` | `1.2420` |
| 3 | Poisson | `1.2799` | `1.2861` |
| 4 | local | `8.6371` | `12.2852` |

This finite table does not rank Poisson first under the supplied beta
diagnostic. It also does not establish that a rival is physically preferred:
the estimator, grids, operator family, and boundary conditions are supplied,
and no continuum ordering is derived. The random positive-definite control
from the original runner has not been included in the sign-normalized
comparison.

### 3. Integrated susceptibility and matched point response

The original integrated susceptibility statistic has Pearson correlation
`0.920038` with the finite Poisson Green profile over seven radii at `N=20`.
The two fitted slopes are nevertheless `-2.2420` and `-1.5666`, and their
pointwise ratio varies by a factor `10.7`.

More directly, the bounded diagnostic compares forward finite-difference
density-response columns with inverse-Laplacian columns at the same
perturbation sites. At three `N=10` sites and step `h=1e-3`, the response
columns are sign-indefinite, the Green columns are single-signed, and their
best-scalar residuals are `0.9987 .. 0.9996`.

These finite observations withdraw the former statement that the density
susceptibility confirms an inverse-Laplacian response kernel. They do not rule
out a different Laplacian-related statement about the amplitude propagator.

### 4. Screened-Poisson subfamily

Within the supplied family

```text
(Laplacian - mu^2 I) phi = source,
```

the original runner reports:

| `mu^2` | raw finite-grid beta |
|---:|---:|
| `0.0` | `1.28` |
| `0.1` | `1.72` |
| `1.0` | `3.55` |
| `2.0` | `4.49` |

These matrices have the same definiteness convention, so the cross-operator
source-sign defect does not affect this within-family comparison. On the
declared finite estimator, the unscreened member is closest to `beta=1` among
the displayed screened cases.

## Bounded claims

1. The supplied Poisson density/field iteration converges at `N=20` and `N=24`
   under the declared parameters and produces the reported finite-grid
   diagnostics.
2. Within the displayed screened-Poisson subfamily, `mu^2=0` is closest to
   `beta=1` under the runner's finite-grid estimator.
3. The broad deterministic-operator preference formerly stated here is not
   supported by the shared-sign attractiveness column or by the integrated
   susceptibility correlation.
4. The point-to-point density-response diagnostic does not establish that the
   measured finite-difference kernel is proportional to the inverse graph
   Laplacian at the sampled sites.

## Explicit limits

- The field operators, source sign convention, boundary conditions, beta
  estimator, and fixed-point protocol are supplied numerical choices.
- The normalized deterministic comparison does not include the random-kernel
  control.
- The monotonicity flag is a short one-axis diagnostic, not a proof of global
  radial monotonicity.
- The point-response result uses three sites, `N=10`, and a forward
  finite-difference step `h=1e-3`.
- The beta values do not establish a continuum ranking.
- The finite operator family is not an exhaustive space of local or nonlocal
  kernels.
- No framework axiom or registered primitive selects Poisson in this note.

## Source-side repair records

- **2026-07-28, PR #5662:** withdrew the unsupported claim that the raw
  `beta≈1.28` is known to approach `1.0`, linked the finite-size beta
  diagnostic, and left the continuum interpretation open.
- **2026-07-28, PR #5656:** linked the matched point-response and
  source-sign-normalization diagnostic, replaced the broad operator-preference
  prose with the finite scope above, corrected the paired runner's summary
  strings without changing its computations, and preserved only the Poisson
  convergence and screened-family results. This source-side change is intended
  to requeue the terminal conditional row for independent audit; it does not
  author or apply an audit grade.

## Reproduction

```bash
python3 scripts/frontier_self_consistent_field_equation.py
python3 scripts/physical_poisson_response_kernel_sign_indefinite_cycle710_2026_07_26.py
```
