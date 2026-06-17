# Gauge-Vacuum Plaquette Readout Form: Finite Derived-Time Trace vs Perron Reading

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim boundary:** finite source-sector computation at source `NMAX = 7`,
`MODE_MAX = 200`, `beta = 6`, for the landed rho inputs `rho=1`,
`rho=delta_(0,0)`, and the finite tensor-word `rho^tw` zero-extension. This
note does not compute the physical 3D unmarked spatial Wilson environment, an
untruncated tensor-transfer limit, a full beta-derivative observable, or the
licensed derived-time geometry input.

**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

**Primary runner:** [gauge_vacuum_plaquette_readout_form_trace_vs_perron_bounded_2026_06_12.py](../scripts/gauge_vacuum_plaquette_readout_form_trace_vs_perron_bounded_2026_06_12.py)
**Cached runner output:** [gauge_vacuum_plaquette_readout_form_trace_vs_perron_bounded_2026_06_12.txt](../logs/runner-cache/gauge_vacuum_plaquette_readout_form_trace_vs_perron_bounded_2026_06_12.txt)

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)
  for the source operator `J`, the half-slice multiplier, and the source-sector
  factorization.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the landed source-sector transfer split and the `rho=1` / `rho=delta`
  Perron anchors.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md)
  for the finite `rho^tw` zero-extended composed readout anchor.
- [PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md](PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md)
  only for the geometry-context list `L in {3, 4, 5, 6, 8}`. Its comparator
  values are not inputs here.

No literature value, new axiom, external citation, new comparator number, or
fitted selector is used.

## Insertion Form

The source-sector factorization note fixes the marked operator:

> `J = (chi_(1,0) + chi_(0,1)) / 6`

and identifies it as acting on the marked-plaquette class-function sector. The
same note gives the factorized transfer:

> `T_src(6) = exp(3 J) D_6 exp(3 J)`

The half-slice clause is the load-bearing source of the insertion placement:

> "the marked spatial plaquette enters the Wilson kernel with half weight on the incoming slice and half weight on the outgoing slice"

and therefore

> `M_(beta/2) = exp[(beta / 2) J]`

The landed Perron-solve note supplies the source transfer actually used by the
reference solves:

> `T_src(6) = exp(3 J) D_6^loc C_(Z_6^env) exp(3 J)`

with the pieces named as `exp(3J)`, `D_6^loc`, and the input diagonal
`rho_(p,q)(6)` inside `C_(Z_6^env)`.

For a periodic derived-time cycle of `L_t` source-sector steps, the
repo-convention readout is the raw `J`-density at one slice:

```text
R_raw(L_t) = Tr[J T_src(6)^L_t] / Tr[T_src(6)^L_t].
```

Cyclicity gives the equivalent insertion-position form

```text
Tr[T^r J T^(L_t-r)] / Tr[T^L_t] = R_raw(L_t)
```

for every insertion position `r` on the periodic cycle. The runner verifies
that independence numerically across the reported `L_t` values.

There is also a derivative-form diagnostic. Write
`T_beta = M_beta E_beta M_beta`, with `M_beta = exp(beta J / 2)` and
`E_beta = D_beta^loc C_beta^env`. If the beta derivative is restricted to the
explicit `M_beta` dependence, then

```text
T_beta,explicit' = (1/2) (J T_beta + T_beta J)
```

and

```text
(1/L_t) d/dbeta log Tr[T_beta^L_t] | explicit M only
  = Tr[T_beta,explicit' T_beta^(L_t-1)] / Tr[T_beta^L_t]
  = Tr[J T_beta^L_t] / Tr[T_beta^L_t].
```

So the explicit-multiplier derivative density equals the symmetrized raw `J`
readout by cyclic trace. The full beta derivative differs by the middle-factor
term

```text
Tr[M_beta E_beta' M_beta T_beta^(L_t-1)] / Tr[T_beta^L_t],
```

where `E_beta'` includes the `D_beta^loc` derivative and any environment-beta
dependence. That HF `D_beta prime` term is not evaluated here and remains a
named open target.

## Computation

For each rho input, the runner builds the same symmetric transfer matrix and
diagonalizes it:

```text
T = exp(3J) D_6^loc diag(rho) exp(3J).
```

If `lambda_0` is the Perron eigenvalue and `v_i` are orthonormal eigenvectors,
the finite trace readout is computed as

```text
R(L_t) =
  sum_i (lambda_i/lambda_0)^L_t <v_i, J v_i>
  / sum_i (lambda_i/lambda_0)^L_t.
```

The `L_t -> infinity` gate reproduces the landed Perron readings:

| rho input | `lambda_0` | `R(infinity)` | landed anchor |
|---|---:|---:|---:|
| `rho=1` | `3.812630482036766` | `0.452407159044564` | `0.4524071590` |
| `rho=delta` | `3.441440354984265` | `0.422531739647131` | `0.4225317396` |
| `rho^tw` | `3.577553737908293` | `0.434215413259920` | `0.434215413260` |

The spectral convergence rates are:

| rho input | `lambda_1/lambda_0` | max sub-Perron absolute ratio |
|---|---:|---:|
| `rho=1` | `3.232915110912132e-02` | `3.232915110912132e-02` |
| `rho=delta` | `1.215755007559722e-16` | `4.081804711979037e-16` |
| `rho^tw` | `1.334766448637066e-02` | `1.334766448637066e-02` |

Thus the finite-trace correction is controlled on these finite matrices by
powers of the listed sub-Perron ratio.

## Requested Trace Corrections

| rho | `L_t` | `R_trace(L_t)` | `R(infinity)` | `R(L_t)-R(infinity)` |
|---|---:|---:|---:|---:|
| `rho=1` | 2 | `0.452226106739933` | `0.452407159044564` | `-1.810523046317791e-04` |
| `rho=1` | 4 | `0.452406983482971` | `0.452407159044564` | `-1.755615933740629e-07` |
| `rho=1` | 8 | `0.452407159044373` | `0.452407159044564` | `-1.911804048404520e-13` |
| `rho=1` | 16 | `0.452407159044564` | `0.452407159044564` | `0.000000000000000e+00` |
| `rho=1` | 32 | `0.452407159044564` | `0.452407159044564` | `0.000000000000000e+00` |
| `rho=1` | 64 | `0.452407159044564` | `0.452407159044564` | `0.000000000000000e+00` |
| `rho=delta` | 2 | `0.422531739647131` | `0.422531739647131` | `0.000000000000000e+00` |
| `rho=delta` | 4 | `0.422531739647131` | `0.422531739647131` | `0.000000000000000e+00` |
| `rho=delta` | 8 | `0.422531739647131` | `0.422531739647131` | `0.000000000000000e+00` |
| `rho=delta` | 16 | `0.422531739647131` | `0.422531739647131` | `0.000000000000000e+00` |
| `rho=delta` | 32 | `0.422531739647131` | `0.422531739647131` | `0.000000000000000e+00` |
| `rho=delta` | 64 | `0.422531739647131` | `0.422531739647131` | `0.000000000000000e+00` |
| `rho^tw` | 2 | `0.434188775481347` | `0.434215413259920` | `-2.663777857242478e-05` |
| `rho^tw` | 4 | `0.434215408871765` | `0.434215413259920` | `-4.388154783985243e-09` |
| `rho^tw` | 8 | `0.434215413259920` | `0.434215413259920` | `-2.220446049250313e-16` |
| `rho^tw` | 16 | `0.434215413259920` | `0.434215413259920` | `0.000000000000000e+00` |
| `rho^tw` | 32 | `0.434215413259920` | `0.434215413259920` | `0.000000000000000e+00` |
| `rho^tw` | 64 | `0.434215413259920` | `0.434215413259920` | `0.000000000000000e+00` |

## Geometry-Context `L` Rows

These rows use the FSS geometry-context list `L in {3, 4, 5, 6, 8}` only as
reported input sizes. No MC value is used, no fit is performed, and no `L_t` is
selected to match any comparator.

```text
rho=1
  L_t=3  R=0.452401658677682  correction=-5.500366882238428e-06
  L_t=4  R=0.452406983482971  correction=-1.755615933740629e-07
  L_t=5  R=0.452407153383189  correction=-5.661374979926137e-09
  L_t=6  R=0.452407158861628  correction=-1.829360551930392e-10
  L_t=8  R=0.452407159044373  correction=-1.911804048404520e-13

rho=delta
  L_t=3  R=0.422531739647131  correction=0.000000000000000e+00
  L_t=4  R=0.422531739647131  correction=0.000000000000000e+00
  L_t=5  R=0.422531739647131  correction=0.000000000000000e+00
  L_t=6  R=0.422531739647131  correction=0.000000000000000e+00
  L_t=8  R=0.422531739647131  correction=0.000000000000000e+00

rho^tw
  L_t=3  R=0.434215080260387  correction=-3.329995327261415e-07
  L_t=4  R=0.434215408871765  correction=-4.388154783985243e-09
  L_t=5  R=0.434215413201490  correction=-5.842976102954367e-11
  L_t=6  R=0.434215413259140  correction=-7.795986078917849e-13
  L_t=8  R=0.434215413259920  correction=-2.220446049250313e-16
```

On the requested set `{2, 4, 8, 16, 32, 64}`, the largest correction is
`1.810523046317791e-04` at `rho=1`, `L_t=2`. On the FSS geometry-context set
`{3, 4, 5, 6, 8}`, the largest correction is `5.500366882238428e-06` at
`rho=1`, `L_t=3`. Therefore no reported finite-trace correction reaches the
panel-era residual scale `0.02`. This statement is restricted to the finite
rho inputs and `L_t` values reported above.

## Runner Gates

The runner reports:

```text
PASS: spectral formula matches direct finite traces for all reported L_t values
PASS: cyclic trace makes the raw J insertion independent of insertion position
PASS: explicit-multiplier beta-derivative density equals the symmetrized raw J readout
PASS: no reported finite trace correction exceeds the panel-era residual scale 0.02
TOTAL: PASS=17, FAIL=0
```

## Named Open Targets

- Identification theorem: readout versus per-plaquette `f prime`.
- Full beta derivative: the HF `D_beta prime` term and any environment-beta
  contribution.
- Per-plaquette normalization.
- Licensed `L_t` geometry input for the accepted periodic source surface.
- Physical 3D unmarked spatial Wilson environment and untruncated tensor-transfer
  limits.

## Negative Claim Discipline Gate

This is a source-side rhetoric check for the bounded sentence "no reported
finite-trace correction reaches `0.02`." It is not an audit status.

**N1 alternative routes.**

| route | marker | result |
|---|---|---|
| Try the requested `L_t` set for `rho=1`, the largest-gap landed source transfer. | ATTEMPTED | Max correction `1.810523046317791e-04`. |
| Try the FSS geometry-context `L_t` set for `rho=1`. | ATTEMPTED | Max correction `5.500366882238428e-06`. |
| Try the rank-one `rho=delta` source transfer. | ATTEMPTED | Correction is zero to printed precision for the reported `L_t` values. |
| Try the finite `rho^tw` zero-extended composed readout on the requested `L_t` set. | ATTEMPTED | Max correction `2.663777857242478e-05`. |
| Try the finite `rho^tw` zero-extended composed readout on the FSS geometry-context `L_t` set. | ATTEMPTED | Max correction `3.329995327261415e-07`. |

**N2 wall independence.** The finite walls are the source truncation, the three
landed rho inputs, the raw `J` convention, and the reported `L_t` sets. Closing
one of these would not automatically close the others; the note keeps them
separate.

**N3 hidden-wall scan.** "Accepted" appears only in the imported geometry-context
phrase. "Convention" is explicit in the raw `J` readout statement. "Comparison"
is restricted to the `L` list and residual-scale question. No comparator value
enters the computation.

**N4 residual matching.** The residual tested here is readout-form finite
derived-time trace versus Perron reading. It is not the physical-environment
residual, not the full derivative residual, and not the MC extrapolation
residual.

**N5 rhetoric audit.** The negative sentence is stated only at the reported
finite rho inputs and finite `L_t` rows. It is not phrased as an all-geometry or
all-observable result.

**N6 partial-closure path scan.** A future identification theorem could change
which `L_t`, normalization, or derivative term is licensed. This note leaves
that path open.

**N7 steelman.** A hostile reviewer can correctly object that the full
beta-derivative observable may include a non-negligible `D_beta prime` term, or
that the identification theorem may license a different derived-time geometry.
That objection does not contradict the raw `J` trace table; it limits what the
table can be used to claim.

**N8 cross-cycle echo.** The prior source-sector notes repeatedly name the
physical residual environment and untruncated tensor-transfer limits as open.
This note does not retire those targets; it only changes the readout form on the
same landed finite source transfers.
