# Gauge-Vacuum Plaquette Word-Count Rung Four Deep-Rim Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem

**Claim boundary:** finite word-count measurement on the existing tensor-word
packet at `beta = 6`, tensor `NMAX = 4`, tensor `MODE_MAX = 80`, source
`NMAX = 7`, source `MODE_MAX = 200`, under the FULLY-DERIVED convention:
matrix-element adjacent bond `delta_(lambda,mu) / d_lambda` and the
tensor-word Perron vector `eta_inf` on every unmarked slot. This note gives
the requested `k = 4` rung and the finite-rank `k = 5..20` continuation on
the same packet. It does not compute the physical 3D unmarked spatial Wilson
environment, an all-weight or untruncated tensor-transfer limit, an `L_perp`
limit, analytic `P(6)`, or a canonical repinning.

**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.

Primary runner: scripts/gauge_vacuum_plaquette_word_count_rung_four_deep_rim_bounded_2026_06_12.py

Runner cache: logs/runner-cache/gauge_vacuum_plaquette_word_count_rung_four_deep_rim_bounded_2026_06_12.txt

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the finite tensor-transfer language and open boundary-character target.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `tensor_word`, `boundary0`, and `amp` packet.
- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  and [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the matrix-element adjacent bond `delta_(lambda,mu) / d_lambda`.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the source-sector Perron machinery with `rho` supplied as input.
- [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the admitted comparison/reuse number `0.5934`, used only in fenced
  distance reporting.

No literature value, new axiom, external citation, fitted selector, or new
comparator number is used. Existing finite inputs are restated only on their
scoped surfaces.

## Route A

Route A solves the full `25^4 = 390625` dimensional Perron problem with
`eigsh`, but applies the fusion Kronecker factor-wise. It does not materialize
the `k = 4` fusion Kronecker.

Memory estimate:

```text
k=4 dimension = 390625
dense k=4 matrix bytes = 1.110 TiB
one vector bytes = 2.980 MiB
eigsh basis bytes at ncv=30 = 89.407 MiB
diag bytes = 2.980 MiB
middle bytes = 2.980 MiB
materialized fusion kron nnz estimate = 157351936
materialized fusion kron CSR rough bytes = 1.760 GiB
```

The runner first checks the factor-wise Kronecker matvec against a materialized
`k = 2` control. Then the full `k = 4` solve gives:

```text
Route A k=4 eig = 0.016255508920
Route A k=4 residual = 1.735e-18
Route A k=4 rho10 = 41.459926615660
Route A k=4 rho11 = 0.162260434667
Route A k=4 P = 0.603630724651
```

## Route B

The slice lemma's finite-rank reduction starts from the matrix-element
middle-bond collapse:

```text
T_k = A_k C_k A_k^T
C_k(mu,mu) = D_mu^k / d_mu^(k-1)
G(mu,nu) = sum_w D_w^2 M(w,mu) M(w,nu)
```

The nonzero spectrum is computed from

```text
C_k^(1/2) G^(entrywise k) C_k^(1/2).
```

For the deep-rim readout, the Perron vector has a channel expansion

```text
psi_k(x_1,...,x_k)
  = D_(x_1) ... D_(x_k)
    sum_mu b_mu M(x_1,mu) ... M(x_k,mu),
```

with the channel vector `b_mu` recovered from the 25-channel reduced Perron
eigenvector. Contracting the unmarked slots against `eta_inf` gives

```text
L_eta(mu) = sum_w eta_inf(w) D_w M(w,mu)

S_eta,k(a)
  = sum_(x_2,...,x_k) psi_k(a,x_2,...,x_k)
      eta_inf(x_2) ... eta_inf(x_k)

  = D_a sum_mu b_mu M(a,mu) L_eta(mu)^(k-1).
```

Thus the eta-weighted readout also closes at rank at most 25. The runner
validates this formula against direct full-vector `k = 2` and `k = 3`
deep-rim values to better than `1e-11` in `rho`, and against Route A at
`k = 4`.

Validation gates:

```text
k=2 direct P = 0.433061880380; Route B P = 0.433061880380
k=3 direct P = 0.543142610051; Route B P = 0.543142610051
k=4 Route A P = 0.603630724651; Route B P = 0.603630724651
```

## Word-Count Table

| `k` | route | eigenvalue | `rho10` | `rho11` | `P_k` | `P_k - P_(k-1)` |
|---:|---|---:|---:|---:|---:|---:|
| 1 | one-word | `1.012369912748e+00` | `0.378514922317` | `0.171042019092` | `0.434215413260` | n/a |
| 2 | Route B | `1.560785137725e-01` | `0.339861706025` | `0.162317777309` | `0.433061880380` | `-0.001153532880` |
| 3 | Route B | `4.555339948442e-02` | `6.888685671846` | `0.162275288429` | `0.543142610051` | `+0.110080729672` |
| 4 | Route A/B | `1.625550891997e-02` | `41.459926615661` | `0.162260434667` | `0.603630724651` | `+0.060488114600` |
| 5 | Route B | `5.804215471004e-03` | `183.909449904561` | `0.162259818306` | `0.612857835719` | `+0.009227111068` |
| 6 | Route B | `2.072488037619e-03` | `743.745131383680` | `0.162259799987` | `0.614633873361` | `+0.001776037642` |
| 7 | Route B | `7.400152989660e-04` | `2900.917483465650` | `0.162259799493` | `0.615050158856` | `+0.000416285495` |
| 8 | Route B | `2.642344077319e-04` | `11140.692852837070` | `0.162259799480` | `0.615155144956` | `+0.000104986100` |
| 9 | Route B | `9.434916055731e-05` | `42489.586214521885` | `0.162259799480` | `0.615182336693` | `+0.000027191737` |
| 10 | Route B | `3.368889076332e-05` | `161540.936388086935` | `0.162259799480` | `0.615189452932` | `+0.000007116239` |
| 11 | Route B | `1.202916225390e-05` | `613268.553253235179` | `0.162259799480` | `0.615191323349` | `+0.000001870417` |
| 12 | Route B | `4.295206557773e-06` | `2326617.383061388042` | `0.162259799480` | `0.615191815890` | `+0.000000492541` |
| 13 | Route B | `1.533672834777e-06` | `8823925.430827725679` | `0.162259799480` | `0.615191945702` | `+0.000000129812` |
| 14 | Route B | `5.476226422397e-07` | `33460630.898450482637` | `0.162259799480` | `0.615191979928` | `+0.000000034226` |
| 15 | Route B | `1.955375041491e-07` | `126874974.299764677882` | `0.162259799480` | `0.615191988953` | `+0.000000009025` |
| 16 | Route B | `6.981982222739e-08` | `481064592.355801641941` | `0.162259799480` | `0.615191991333` | `+0.000000002380` |
| 17 | Route B | `2.493029455949e-08` | `1823996404.723642110825` | `0.162259799480` | `0.615191991961` | `+0.000000000628` |
| 18 | Route B | `8.901764097860e-09` | `6915782210.485126495361` | `0.162259799480` | `0.615191992127` | `+0.000000000166` |
| 19 | Route B | `3.178518563624e-09` | `26221552203.928749084473` | `0.162259799480` | `0.615191992170` | `+0.000000000044` |
| 20 | Route B | `1.134941360863e-09` | `99419769486.012619018555` | `0.162259799480` | `0.615191992182` | `+0.000000000012` |

The first three values are:

```text
P1 = 0.434215413260
P2 = 0.433061880380
P3 = 0.543142610051
```

So the start is not monotone: `P2 < P1 < P3`. This is load-bearing for any
finite-word bracketing claim and is not smoothed here.

The requested new rung is:

```text
P4 = 0.603630724651
```

The next finite-rank rung is:

```text
P5 = 0.612857835719
```

## Increment Sequence

```text
P2 - P1  = -1.153532880268e-03
P3 - P2  = +1.100807296718e-01
P4 - P3  = +6.048811459958e-02
P5 - P4  = +9.227111068407e-03
P6 - P5  = +1.776037641605e-03
P7 - P6  = +4.162854949616e-04
P8 - P7  = +1.049860996934e-04
P9 - P8  = +2.719173732912e-05
P10 - P9 = +7.116238870175e-06
P11 - P10 = +1.870417299377e-06
P12 - P11 = +4.925412734336e-07
P13 - P12 = +1.298115075432e-07
P14 - P13 = +3.422564442968e-08
P15 - P14 = +9.025432623488e-09
P16 - P15 = +2.380240116118e-09
P17 - P16 = +6.277564024160e-10
P18 - P17 = +1.655655612609e-10
P19 - P18 = +4.366684791535e-11
P20 - P19 = +1.151656547904e-11
```

Empirical diagnosis: the displayed sequence is non-monotone at the start.
After `k = 2`, the displayed increments are positive and shrink rapidly. The
absolute increment ratios after the large early transient approach about
`0.26374` in the `k = 15..20` window. This is a finite-table observation, not
an analytic convergence proof or an untruncated limit.

## Fenced Comparator Distances

The canonical comparison number below is admitted only as a comparison/reuse
number, not as a derived value, fit target, or repinning input.

```text
k=1:  P = 0.434215413260; |P - 0.5934| = 0.159184586740
k=2:  P = 0.433061880380; |P - 0.5934| = 0.160338119620
k=3:  P = 0.543142610051; |P - 0.5934| = 0.050257389949
k=4:  P = 0.603630724651; |P - 0.5934| = 0.010230724651
k=5:  P = 0.612857835719; |P - 0.5934| = 0.019457835719
k=6:  P = 0.614633873361; |P - 0.5934| = 0.021233873361
k=7:  P = 0.615050158856; |P - 0.5934| = 0.021650158856
k=8:  P = 0.615155144956; |P - 0.5934| = 0.021755144956
k=9:  P = 0.615182336693; |P - 0.5934| = 0.021782336693
k=10: P = 0.615189452932; |P - 0.5934| = 0.021789452932
k=11: P = 0.615191323349; |P - 0.5934| = 0.021791323349
k=12: P = 0.615191815890; |P - 0.5934| = 0.021791815890
k=13: P = 0.615191945702; |P - 0.5934| = 0.021791945702
k=14: P = 0.615191979928; |P - 0.5934| = 0.021791979928
k=15: P = 0.615191988953; |P - 0.5934| = 0.021791988953
k=16: P = 0.615191991333; |P - 0.5934| = 0.021791991333
k=17: P = 0.615191991961; |P - 0.5934| = 0.021791991961
k=18: P = 0.615191992127; |P - 0.5934| = 0.021791992127
k=19: P = 0.615191992170; |P - 0.5934| = 0.021791992170
k=20: P = 0.615191992182; |P - 0.5934| = 0.021791992182
```

## Named Residuals

- finite word count only;
- finite dominant-weight box and finite Bessel mode support only;
- no physical 3D unmarked spatial Wilson environment computation;
- no all-weight or untruncated tensor-transfer convergence proof;
- no `L_perp` limit;
- no analytic `P(6)`;
- no canonical repinning;
- no claim that the finite-rank `k = 20` table value is an analytic
  `k -> infinity` value.
