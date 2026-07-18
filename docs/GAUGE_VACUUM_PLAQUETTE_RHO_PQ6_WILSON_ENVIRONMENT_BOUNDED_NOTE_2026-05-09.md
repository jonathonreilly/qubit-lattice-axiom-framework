# Finite Evaluation of a Stipulated SU(3) Character Integral at x=2

**Original date:** 2026-05-09
**Scope repair:** 2026-07-18
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only
**Primary runner:** `scripts/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py`
**Authenticated stdout:** `logs/runner-cache/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.txt`

## Narrow claim

Supply the following mathematical data:

- the compact group `SU(3)` with Haar probability measure `dmu_Haar`;
- the label `beta = 6` and the stipulated exponent parameter `x = beta/3 = 2`;
- the irreducible character `chi_(p,q)` and dimension
  `d_(p,q) = (p+1)(q+1)(p+q+2)/2`;
- the finite weight box `B = {(p,q): 0 <= p,q <= 4}`.

Define, for `(p,q)` in `B`,

```text
c_(p,q)(x) = integral_SU(3) chi_(p,q)(U) exp(x Re tr U) dmu_Haar(U),
rho_(p,q)(x) = c_(p,q)(x) / (d_(p,q) c_(0,0)(x)).
```

The theorem in this note is only the finite evaluation of these stipulated
integrals and normalized values at `x=2`. The runner evaluates all 25 weights
by two separately implemented routes and obtains, in the disclosed float64
run,

```text
max raw-coefficient absolute cross-error    = 1.332e-15
max raw-coefficient relative cross-error    = 1.952e-14
max normalized absolute cross-error         = 1.110e-16
max normalized relative cross-error         = 1.911e-14
```

The numerical certificate uses acceptance tolerances `1e-12` absolute and
`1e-10` relative. These are acceptance thresholds, not analytic error bounds.

Representative normalized values are

```text
rho_(0,0) = 1.000000000000e+00
rho_(1,0) = rho_(0,1) = 4.225317396500e-01
rho_(1,1) = 1.622597994799e-01
rho_(2,0) = rho_(0,2) = 1.359617273634e-01
rho_(2,1) = rho_(1,2) = 4.828805556745e-02
rho_(3,0) = rho_(0,3) = 3.505738045167e-02
rho_(2,2) = 1.350507888830e-02
rho_(4,4) = 2.275225312476e-05
```

## Domain, measure, and analytic reduction

For the direct route, write

```text
U = diag(exp(i theta1), exp(i theta2), exp(-i(theta1+theta2))),
theta1, theta2 in [0,2pi),
Delta(theta) = product_(i<j) (exp(i theta_i) - exp(i theta_j)).
```

For any class function `f`, the supplied Haar probability normalization is

```text
integral_SU(3) f(U) dmu_Haar(U)
  = 1 / (6 (2pi)^2)
    integral_[0,2pi)^2 f(theta) |Delta(theta)|^2 dtheta1 dtheta2.
```

With highest-weight triple `lambda=(p+q,q,0)`, the Weyl character formula is
the quotient of the numerator alternant with exponents
`(lambda_1+2, lambda_2+1, lambda_3)` by the denominator alternant with
exponents `(2,1,0)`. The runner multiplies before dividing:

```text
chi_lambda(theta) |Delta(theta)|^2
  = det(numerator) conjugate(det(denominator)).
```

This identity is exact and removes the apparent `0/0` on Weyl walls.

Expanding each factor `exp(x cos(theta))` in its absolutely convergent Fourier
series and imposing the `SU(3)` determinant-one constraint reduces the same
integral exactly to

```text
c_(p,q)(x)
  = sum_(k in Z) det_[i,j] I_(k + lambda_j + i - j)(x),
```

where `I_n` is the modified Bessel function. Thus the infinite integral and
infinite determinant series are analytically the same object; the committed
finite values are numerical evaluations of that identity.

## Numerical certificate and truncations

The Bessel route truncates the convergent mode sum to `-80 <= k <= 80`. Its
normalized table changes by at most `6.776e-21` when compared with the
separately recomputed `-12 <= k <= 12` table.

The direct Weyl route uses periodic grids `24`, `32`, `40`, and `64` in each
angle. The maximum normalized changes are

```text
24 -> 32: 3.561e-13
32 -> 40: 2.220e-16
40 -> 64: 1.110e-16
```

The `64 x 64` table is the direct value used for the cross-check. The maximum
imaginary residual in its unnormalized coefficients is `1.044e-15`. The
runner discloses Python, NumPy, SciPy, platform, and mantissa information.
No platform-independent enclosure is claimed.

The normalization `rho_(0,0)=1` is exact from the definition once
`c_(0,0)(2)` is nonzero. Conjugation symmetry is exact for this integral from
Haar invariance under `U -> U^dagger` and the relation
`chi_(q,p)=conjugate(chi_(p,q))`; the runner's finite swap residual is
`2.776e-17`. Strict positivity of all 25 printed values, including the minimum
`2.275225312476e-05`, is a conclusion about this evaluated finite box, not an
all-weight theorem.

## Hostile mutations

Each mutation recomputes from formulas rather than importing an expected
table. The unmutated certificate rejects:

| Mutation | Maximum separation |
|---|---:|
| change `x` to `-x` | `6.225e-01` |
| omit `d_(p,q)` from the normalization of `rho` | `1.136e+00` |
| replace the torus domain `[0,2pi)^2` by `[0,pi)^2` | `4.113e-03` |
| replace the Haar density by flat torus measure | `4.978e-01` |
| omit the Weyl factor `1/6` in raw coefficients | `2.234e+01` |
| attach the highest-weight shift to the determinant row instead of its column | `4.225e-01` |

As an independent normalization check, direct quadrature at `x=0` gives
`|c_(0,0)(0)-1| = 2.220e-16` and maximum nontrivial-character magnitude
`6.277e-16`.

A physical-identification relabel is a hostile scope mutation, not a numerical
one: attaching the words "physical environment" to an unchanged array leaves
every integral residual unchanged. It is therefore rejected by the source
boundary and direct-consumer trace below, not counted as mathematical evidence
or as a no-go theorem.

## Scope and downstream hygiene

This row does not identify the stipulated integral or its finite table with a
canonical, actual, or physical Wilson environment; a framework-derived
environment replacement; a local mixed-kernel factor; a compressed unmarked
spatial environment; or a physical plaquette readout. No such bridge is an
input or conclusion here. This is a positive finite evaluation theorem, not a
no-go statement about whether another authority could establish one of those
identifications.

**Downstream hygiene (2026-07-18):** citations to this row may use only the
finite evaluation of the explicitly stipulated integral/data above and must
not treat this row as an identification of those numbers with a canonical,
actual, or physical Wilson environment, a framework-derived replacement, or
a physical plaquette readout.

The row also does not supply an all-weight formula, a uniform truncation-error
bound, an untruncated tensor-transfer/Perron result, or analytic closure of
`P(6)`.

## Machine-readable source metadata

```yaml
claim_id: gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09
note_path: docs/GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md
runner_path: scripts/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py
claim_type: bounded_theorem
deps: []
audit_authority: independent audit lane only
```

## Reproduction

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py
python3 scripts/cached_runner_output.py \
  --refresh \
  scripts/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py
```

Expected summary:

```text
SUMMARY: THEOREM PASS=6 SUPPORT=6 FAIL=0
```
