# Gauge-Vacuum Plaquette Hellmann-Feynman Identification Diagnostic

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim boundary:** finite source-sector diagnostic at `beta = 6`, source
`NMAX = 7`, source `MODE_MAX = 200`, with three supplied residual
environment choices: `rho = 1`, `rho = delta_(p,q),(0,0)`, and the finite
one-word `rho^tw` packet zero-extended from tensor-word `NMAX = 4`,
`MODE_MAX = 80`. The bounded claim is only the measured Hellmann-Feynman
decomposition on those finite surfaces. It does not prove a per-plaquette
normalization theorem, compute the physical 3D unmarked spatial Wilson
environment, or repin a canonical plaquette value.

**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

**Primary runner:** scripts/gauge_vacuum_plaquette_hf_identification_diagnostic_2026_06_12.py

## Inputs

One-hop authorities:

- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the source-sector factorization
  `T_src(6) = exp(3J) D_6^loc C_(Z_6^env) exp(3J)`, the reference Perron
  anchors, the normalization `J = (chi_(1,0) + chi_(0,1))/6`, and the
  `M_beta = exp((beta/2)J)` scaling.
- [GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)
  for the exact half-slice multiplier statement on the source sector.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md)
  for the finite `rho^tw` construction and zero-extension convention.
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the finite tensor-word carrier machinery.
- [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the admitted comparison/reuse-number license used only in the fenced
  comparator block.

No literature value, new axiom, external citation, fitted selector, or new
comparator number is introduced. Existing repo-internal reference anchors are
reproduced as gates, not used as fit targets.

## Question

The standing identification checkpoint says the assertion

```text
Perron J-readout = licensed <P>* = 1 + f'(6)
```

is unproven. The computable object now available is the
Hellmann-Feynman beta derivative of the landed source-sector transfer. The
diagnostic question is: when `f` is hypothetically read as a per-step
`log(lambda_0(beta))`, how large is the derivative contribution omitted by
using only the Perron `J` readout?

This note answers only that finite diagnostic question. The identification
theorem itself remains an open target.

## Decomposition

The source-sector operator used here is

```text
T_src(beta) = M_beta D_beta^loc C_rho(beta) M_beta,
M_beta = exp((beta/2) J),
J = (chi_(1,0) + chi_(0,1))/6.
```

At `beta = 6`, this gives `M_6 = exp(3J)`, matching the reference Perron
solves.

Let `psi` be the normalized Perron vector of `T_src(beta)` with Perron
eigenvalue `lambda_0`. Hellmann-Feynman gives

```text
d_beta log(lambda_0) = <psi, T'_src psi> / lambda_0.
```

The two multiplier derivative terms are

```text
M'_beta D C M_beta + M_beta D C M'_beta,
M'_beta = (1/2) J M_beta = (1/2) M_beta J.
```

Since `T_src` is self-adjoint on the finite source box and
`T_src psi = lambda_0 psi`,

```text
(1/lambda_0)<psi, (M'DCM + MDCM') psi>
  = (1/2)<psi,J psi> + (1/2)<psi,J psi>
  = <psi,J psi>.
```

So the multiplier contribution is exactly the Perron `J` readout for the same
finite Perron state. The diagnostic issue is not this factor of two; the
issue is the remaining derivative terms.

The local marked-link factor is

```text
D_beta^loc chi_(p,q) = a_(p,q)(beta)^4 chi_(p,q),
a_(p,q)(beta) = c_(p,q)(beta) / (d_(p,q)c_(0,0)(beta)).
```

The runner differentiates the same Bessel determinant mode sums term by term:

```text
c_(p,q)(beta) = sum_n det[I_(n + lambda_j + i - j)(beta/3)]_(i,j=1)^3,
d_beta I_m(beta/3) = (I_(m-1)(beta/3) + I_(m+1)(beta/3)) / 6.
```

The determinant derivative is evaluated by row multilinearity, replacing one
row at a time by its beta derivative. Then

```text
(D_beta^loc)' chi_(p,q) = 4 a_(p,q)(beta)^3 a'_(p,q)(beta) chi_(p,q).
```

For the two reference environments, `rho = 1` and `rho = delta` are
beta-independent by construction, so there is no environment-derivative term.
For `rho^tw`, the finite tensor-word builder is beta-dependent; its
environment derivative is computed by central finite differences with a
multi-step Richardson sweep.

## Numbers at beta = 6

The runner reports:

| rho | `lambda_0` | `d_beta log(lambda_0)` | multiplier `<J>` | `D'_loc` term | env term | correction `D'+env` | correction / `<J>` | hypothetical `1+f'` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `rho=1` | `3.812630482037` | `0.515193988472` | `0.452407159045` | `0.062786829428` | `0.000000000000` | `0.062786829428` | `0.138783898911` | `1.515193988472` |
| `rho=delta` | `3.441440354984` | `0.422531739647` | `0.422531739647` | `0.000000000000` | `0.000000000000` | `0.000000000000` | `0.000000000000` | `1.422531739647` |
| `rho^tw` | `3.577553737908` | `0.468343775233` | `0.434215413260` | `0.023823742365` | `0.010304619608` | `0.034128361973` | `0.078597767216` | `1.468343775233` |

Thus, on these finite surfaces:

- `rho=1`: the omitted local derivative term is `0.062786829428`, about
  `13.8784%` of the multiplier/J readout.
- `rho=delta`: the correction is zero in this normalized reference solve,
  because the only surviving diagonal channel is `(0,0)` and `a_(0,0)=1`
  has zero beta derivative.
- `rho^tw`: the omitted correction is `0.034128361973`, about `7.8598%` of
  the multiplier/J readout; the environment derivative contributes
  `0.010304619608` of that amount.

These are correction scales for the finite diagnostic. They are not a
per-plaquette identification.

## Gates

Reference anchors:

```text
rho=1:     lambda0=3.812630482037, <J>=0.452407159045
rho=delta: lambda0=3.441440354984, <J>=0.422531739647
rho^tw:    lambda0=3.577553737908, <J>=0.434215413260
rho^tw tensor Perron residual=1.665e-16, min=2.287e-23, swap=5.551e-17
```

Reference exact-vs-FD validation:

```text
rho=1:
h          central FD       Richardson       |Richardson - assembly|
0.01000000 0.515193970637   n/a              n/a
0.00500000 0.515193984013   0.515193988472   8.549e-14
0.00250000 0.515193987358   0.515193988472   2.371e-13
0.00125000 0.515193988194   0.515193988472   3.730e-14
0.00062500 0.515193988403   0.515193988472   1.705e-13
Richardson noise floor: 1.332e-13

rho=delta:
h          central FD       Richardson       |Richardson - assembly|
0.01000000 0.422531607447   n/a              n/a
0.00500000 0.422531706597   0.422531739647   2.370e-14
0.00250000 0.422531731385   0.422531739647   1.644e-13
0.00125000 0.422531737582   0.422531739647   5.884e-15
0.00062500 0.422531739131   0.422531739647   3.050e-13
Richardson noise floor: 3.109e-13
```

This validates the finite-difference machinery on the two beta-independent
reference environments before using it for `rho^tw`.

`rho^tw` step stability:

```text
h          env central      env Richardson   full central     full Richardson   full - assembled central
0.01000000 0.010304605540   n/a              0.468344012402   n/a               2.512e-07
0.00500000 0.010304616091   0.010304619608   0.468343834526   0.468343775233    6.281e-08
0.00250000 0.010304618728   0.010304619608   0.468343790056   0.468343775233    1.570e-08
0.00125000 0.010304619388   0.010304619608   0.468343778939   0.468343775233    3.925e-09
0.00062500 0.010304619553   0.010304619608   0.468343776160   0.468343775233    9.815e-10
Environment Richardson noise floor: 7.129e-14
Full-derivative Richardson noise floor: 5.181e-13
```

The assembled `rho^tw` derivative is

```text
<J> + D'_loc term + env term
= 0.434215413260 + 0.023823742365 + 0.010304619608
= 0.468343775233,
```

matching the full beta finite-difference Richardson derivative at the printed
precision.

## Fenced Hypothetical Context

The block below is context only. The comparison number is admitted by the
reuse license cited above; it is not used in the construction, initialization,
fit, derivative assembly, or gate thresholds.

```text
These are context distances only. The per-plaquette normalization theorem is open.
rho=1: |<J> - 0.5934| = 0.140992840955; |d_beta log(lambda0) - 0.5934| = 0.078206011528; hypothetical 1+f' = 1.515193988472
rho=delta: |<J> - 0.5934| = 0.170868260353; |d_beta log(lambda0) - 0.5934| = 0.170868260353; hypothetical 1+f' = 1.422531739647
rho^tw: |<J> - 0.5934| = 0.159184586740; |d_beta log(lambda0) - 0.5934| = 0.125056224767; hypothetical 1+f' = 1.468343775233
```

If `f` were identified with the per-step `log(lambda_0)`, the
`1+f'` values would be the last numbers in that block. This is a
hypothetical map only; the per-plaquette normalization theorem is not supplied
here.

## Named Residuals

Open target: prove or refute the per-plaquette normalization map linking the
licensed plaquette readout to a beta derivative of the source-sector Perron
value.

Residuals left open:

- physical 3D `rho_(p,q)(6)`;
- untruncated tensor-transfer limit;
- multi-word and `L_perp` limits;
- the identification theorem
  `Perron J-readout = licensed <P>* = 1 + f'(6)`.

## Runner Summary

Command:

```bash
python3 scripts/gauge_vacuum_plaquette_hf_identification_diagnostic_2026_06_12.py
```

Completed runner summary:

```text
TOTAL: PASS=15, FAIL=0
```
