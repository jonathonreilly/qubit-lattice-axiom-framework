# Poisson Response-Kernel and Sign-Normalization Finite-Grid Diagnostic

**Date:** 2026-07-26

**Type:** bounded_theorem

**Scope:** Finite numerical checks of the point-to-point density response and
source-sign-normalized deterministic operator comparison implemented by
`frontier_self_consistent_field_equation.py`.

**Audit status:** This source note does not assign an audit verdict or effective
status.

**Primary runner:**
[`physical_poisson_response_kernel_sign_indefinite_cycle710_2026_07_26.py`](../scripts/physical_poisson_response_kernel_sign_indefinite_cycle710_2026_07_26.py)

## Question

The conditional audit of `self_consistency_forces_poisson_note` requested two
computations before re-audit:

1. compare the propagator's susceptibility with a matched point-to-point
   inverse-Laplacian kernel; and
2. normalize alternative-operator source signs consistently.

This note reports those computations at finite lattice size. It evaluates the
evidence used by the parent construction; it does not derive a continuum field
equation or select a winning operator.

The runner imports
`scripts/frontier_self_consistent_field_equation.py` and fails closed unless
that file has SHA-256
`9e49b83bb9ce50ecdff58092da859dd2ee5b5d2558bf428d0c840b38be4af4f6`,
the reviewed parent source bytes in this repair.

## Protocol and supplied inputs

The shared numerical inputs are the parent's
`k=5.0`, `G=0.5`, `sigma=2.0`, mixing `0.3`, tolerance `1e-4`, and maximum
`30` fixed-point iterations. Dirichlet cubic lattices are used throughout.

For a perturbation site `y`, the point-to-point comparison uses the forward
finite-difference column

```text
K_h(x,y) = [rho(phi + h delta_y)(x) - rho(phi)(x)] / h,
h = 1e-3,
```

not an asserted exact derivative. The inverse-Laplacian column is evaluated at
the same `y`. The best scalar match minimizes the interior Euclidean residual
`norm(K_h-cG)/norm(K_h)`.

For the operator comparison, the source sign is chosen separately so that a
positive unit density produces the same well sign. The coupling `G` is applied
once in the source term for every solver. Eligibility requires fixed-point
convergence as well as the parent runner's attractiveness and one-axis
monotonicity checks.

## Finite-grid results

### Matched point-to-point response

At `N=10`, for perturbation sites one, two, and three lattice steps from the
source:

| diagnostic | finite result |
|---|---:|
| fraction of interior `K_h>0` | `0.14 .. 0.21` |
| fraction of interior `K_h<0` | `0.70 .. 0.78` |
| fraction of interior inverse-Laplacian entries with the reference sign | `1.000000` |
| best-scalar relative residual | `0.9987 .. 0.9996` |
| Pearson correlation `corr(K_h,G)` | `-0.058 .. -0.031` |

Thus the three sampled finite-difference columns are sign-indefinite and are
not close to scalar multiples of the corresponding single-signed
inverse-Laplacian columns. This is a statement about those sites, that grid,
and that finite-difference step.

The mismatch remains in the seven sampled wave numbers
`k in {0.05,0.2,0.5,1,2,5,10}`, a 200-fold range: every sampled
`abs(corr(K_h,G))` is below `0.25`. Disabling only per-layer normalization
while retaining final global normalization also leaves every best-scalar
residual above `0.9`.

The parent propagator fixes every x-layer density marginal to `1/N` when
per-layer normalization is enabled. The signed integrated response therefore
vanishes to numerical precision, whereas the parent's absolute-difference
statistic is nonzero. That statistic measures total-variation reshaping rather
than signed integrated response.

### The reported shape correlation

Recomputing the parent statistic at `N=20` gives:

| quantity | value |
|---|---:|
| `corr(chi,G_finite)` | `0.920038` |
| log-log slope of `chi` | `-2.2420` |
| log-log slope of `G_finite` | `-1.5666` |
| spread of `chi/G_finite` over the seven radii | `10.7x` |

On those same radii, a `0.93` correlation threshold between the actual finite
Green profile and `r^-p` admits sampled exponents through approximately
`p=4.31`. In particular, it admits `p=2.805`, the susceptibility exponent
recorded in the parent audit rationale. It does not admit the much steeper
local-operator value `p=8.637`. The bounded conclusion is therefore that the
reported correlation is weak evidence against the recorded `2.805` mismatch,
not that correlation has no discriminating power at all.

### Source-sign-normalized deterministic operators

The parent Laplacian solver's response to a positive point source has the
opposite sign from the tested biharmonic, local, and inverse-square-kernel
solvers. Applying the same negative source sign to all four therefore makes
the original cross-operator "attractive" column convention-dependent.

After per-operator sign normalization, all four deterministic fixed-point
iterations converge at `N=20` and `N=24`, are positive over the tested
interior, and pass the parent's one-axis monotonicity diagnostic:

| rank by `abs(beta-1)` | operator | `beta`, N=20 | `beta`, N=24 |
|---:|---|---:|---:|
| 1 | biharmonic | `0.8762` | `0.8669` |
| 2 | inverse-square kernel | `1.2120` | `1.2420` |
| 3 | Poisson | `1.2799` | `1.2861` |
| 4 | local | `8.6371` | `12.2852` |

This table uses the parent's finite-grid beta estimator. It says that this
estimator does not rank Poisson first at either tested size. It does not say
that biharmonic is physically preferred, that any rival wins in a continuum
limit, or that the same result holds for the parent's random-kernel control.
The random control is outside this normalized comparison.

Three robustness checks bound the interpretation:

- the screened-Poisson matrices tested by the parent share the unscreened
  Laplacian's definiteness, so the source-sign defect does not invalidate the
  within-family screened comparison;
- the tested biharmonic matrix is exactly the square of the parent's
  Dirichlet Laplacian, and its dense inverse is positive entrywise at `N=10`;
  this says nothing about other fourth-order boundary-value problems; and
- across the shared sampled coupling range `G=0.05 .. 4.0`, every deterministic
  solver converges, each operator's beta spread is below `0.05`, and Poisson
  remains third by the same finite-grid estimator. This is not an
  amplitude-matching or continuum claim.

## Bounded claims

1. At the three tested `N=10` perturbation sites and `h=1e-3`, the
   finite-difference density-response columns are sign-indefinite and have
   best-scalar residual above `0.998` against matched inverse-Laplacian
   columns.
2. At the parent's seven `N=20` radii, its `0.93` correlation threshold admits
   the audit-recorded susceptibility exponent `2.805`, while the measured
   response and Green profiles have different fitted slopes and a `10.7x`
   ratio spread.
3. With one application of `G`, per-operator source-sign normalization, and the
   parent's convergence and beta diagnostics, the four deterministic solvers
   converge and Poisson ranks third by `abs(beta-1)` at `N=20` and `N=24`.
4. These results remove the submitted numerical support for a broad
   deterministic-operator preference. They leave intact the finite Poisson
   convergence result and the within-screened-family ordering.

## Claim ledger

| ID | Exact claim | Support | Supplied conditions | Falsifier |
|---|---|---|---|---|
| `finite_response_column` | The sampled finite-difference response columns are not close to scalar multiples of matched inverse-Laplacian columns. | runner rows R1-R6 | `N=10`, three sites, `h=1e-3`, parent propagator and pin | residual at or below `0.9`, or loss of both-sign support |
| `finite_shape_selectivity` | The parent's correlation threshold admits the audit-recorded `p=2.805` mismatch on its sampled radii. | R8-R9 | `N=20`, seven radii, Pearson correlation, finite Dirichlet Green profile | correlation below `0.93` at `p=2.805` |
| `normalized_finite_ranking` | The parent beta diagnostic ranks Poisson third among four deterministic converged wells at both tested sizes. | R10-R12, R15 | listed parameters, sign normalization, one application of `G`, parent diagnostics | Poisson ranks first at either size or a listed solver does not converge |
| `screened_scope_preserved` | The sign-convention finding does not cross the tested screened-Poisson family. | R13 | the parent's screened matrices | a screened matrix changes definiteness |
| `tested_biharmonic_positivity` | The exact tested squared-Laplacian inverse is positive entrywise at `N=10`. | R14 | the parent's matrix construction | a nonpositive entry or failure of the inverse-square identity |

## No-Go Discipline stress test

The note contains narrow negative boundaries, so the N1-N8 discipline applies.
The target is only the four bounded claims above.

### N1: alternative attacks

| Attack on the bounded conclusion | Disposition |
|---|---|
| The pointwise mismatch disappears at weak wave number. | **ATTEMPTED:** seven values from `0.05` to `10`; no sampled `abs(corr)` reaches `0.25`. |
| Per-layer normalization projects out the matching component. | **ATTEMPTED:** disabling that step alone leaves residuals above `0.9`. |
| The kernels differ only by a scalar or sign convention. | **ATTEMPTED:** least-squares scaling leaves residuals above `0.998`; a global sign does not change the residual or sign-indefiniteness. |
| The parent's smeared statistic supplies the missing matched comparison. | **ATTEMPTED:** the statistic is reproduced, but the slopes differ and `chi/G` varies by `10.7x`. |
| Consistent source signs still leave rival wells non-attractive. | **ATTEMPTED:** all four deterministic interiors have the reference sign after normalization. |
| The normalized ranking is a nonconvergence artifact. | **ATTEMPTED:** convergence is now an assertion prerequisite at both sizes. |
| A positivity requirement independently excludes the tested biharmonic solver. | **ATTEMPTED:** the implemented squared-Laplacian inverse is entrywise positive at `N=10`. |
| The ranking is specific to `G=0.5`. | **ATTEMPTED:** it is unchanged at all seven shared sampled couplings. |

An alternative decay diagnostic, larger lattices, the random-kernel control,
and a continuum limit are extensions outside the exact finite claims; none is
counted as a closed attack or silently generalized over.

### N2-N8

- **N2, wall independence:** the point-response mismatch, correlation
  selectivity, and source-sign convention are separate numerical questions.
  The normalized beta ranking and attractiveness result share the source-sign
  correction and are presented as consequences of one intervention.
- **N3, hidden walls:** grid size, sites, finite-difference step, parameters,
  convergence, beta estimator, one-axis monotonicity test, and solver subset
  are explicit above.
- **N4, residual matching:** the two computations correspond exactly to the
  parent audit row's named repair targets; no prior no-go is used as a witness.
- **N5, rhetoric:** all negative statements are qualified by the tested grid,
  sites, solver family, statistic, or parameter sweep. No continuum or
  all-operator wording is used.
- **N6, partial closure:** finite Poisson convergence and the screened-family
  result survive and are preserved in the parent repair.
- **N7, steelman:** the phase-amplitude propagator may have a legitimate
  amplitude resolvent even though the measured density response is not a
  Poisson column. That does not rescue the parent's density-response evidence,
  but it prevents this note from claiming that no Laplacian-related amplitude
  relation exists.
- **N8, cross-result echo:** the result is handled as a scope correction to the
  measured observable, not as retirement of Poisson physics or a new field-law
  theorem.

All qualifying attacks are attempted or ruled out by the displayed algebra.
The open extensions are excluded from the bounded claims. The N1-N8 packet
therefore passes for this finite scope.

## Imports, primitives, and open extensions

No external physical constant, fitted observed value, framework axiom, or
registered primitive is load-bearing. The parent code, its numerical
parameters, its diagnostic definitions, NumPy/SciPy linear algebra, and the
declared finite grids are supplied inputs.

Open extensions are:

- a step-size and lattice-size study of the point-response estimator;
- a separately justified decay diagnostic;
- a sign-normalized random-kernel comparison; and
- any continuum-limit operator ranking.

These extensions are not needed to reproduce the finite rows and are not
claimed closed.

## Reproduction

```bash
python3 scripts/physical_poisson_response_kernel_sign_indefinite_cycle710_2026_07_26.py
```

The runner exits nonzero on any failed row and prints its total last.
