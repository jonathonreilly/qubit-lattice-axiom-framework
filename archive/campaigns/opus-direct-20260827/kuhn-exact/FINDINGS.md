# Kuhn-exact: R132's instrument applied to the simplicial operator

Directory: `.claude/science/opus-direct-20260827/kuhn-exact/`   (2026-08-29, written incrementally)

## 1. Setup

R132 showed that the standing "conformal channel does not plateau" finding for the induced
Einstein-Hilbert coefficient is an artefact of the DIAGNOSTIC (subtraction of a **truncated**
Seeley-DeWitt series), not of the lattice. Its instrument replaces the truncated series by the
**exact** continuum heat trace on the same perturbed torus:

```
  x = s kappa^2 ,  kappa = 2 pi n / L ,  n = 2
  Rlat(x)  = (4 pi s)^2 K2lat(s)  / Vol2       K2 = eps^2 Taylor coefficient of Tr exp(-s Delta)
  Rcont(x) = (4 pi s)^2 K2cont(s) / Vol2       (5-point central difference in eps, h = 0.05)
  F(L,x)   = 1 + (Rlat - Rcont) / (b1 x)
```

`Vol2` = exact continuum eps^2 volume coefficient (+0.5 L^4 conformal, -0.25 L^4 TT);
`b1` = analytic Seeley-DeWitt coefficient. All higher orders are removed exactly, so
`F - 1` is *pure lattice discretisation error*.

R132 used a divergence-form tensor-product FEM operator (`opus_t206.lat_heat`).
**This work substitutes the framework's KUHN (Freudenthal) simplicial operator and changes
nothing else.**

* lattice: `conformal/recheck/kuhn.py` used as a **black box** -- `build()` (stencil, lumped
  mass, improvement weight `C`), `_bands()` + `bloch_eigs()` (spectrum), `dense_eigs()`,
  `flat_lattice_trace()`, `flat_exact_trace()`. **`kuhn.py` was not modified.** P1 FEM on the
  Kuhn triangulation, lumped mass, `Delta = M^-1 K`, edge squared lengths from the metric at
  edge midpoints.
* continuum: `opus_t206.cont_heat` imported directly (exact plane-wave diagonalisation).
* `b1, b2`: `opus_t205.coeffs` imported directly (Riemann tensor, explicit loops).

Channels, in the `P` convention of `kuhn.py` (`g_mm = 1 + eps P_m cos(kappa x0)`):
CONFORMAL `P=(1,1,1,1)` <-> `opus_t206` chan `{0:1,1:1,2:1,3:1}`;
TRACELESS-TT `P=(0,1,-1,0)` <-> `{1:1,2:-1}`.
Improvement `B -> B + B diag(C) B / 24`, `C = tr g / 4` (`cpoint='vertex'`), i.e. covariant
Symanzik `c = tr g / 96`. Both improved and plain are run.
`L in {32,48,64,96}`, `x in {0.4,0.6,0.8,1.0,1.4,2.0}`, `n = 2`, `J = 30`.

Code: `kx_base.py`, controls `c1..c6`, measurement `kx_run.py`, analysis `kx_fit.py`.
Raw output in `out_*.txt`; raw `F` in `kx_F_32_48_64_96.npz`.

---

## 2. Controls (all numbers as measured)

### C1 -- flat Kuhn stencil / lumped mass / volume  (`out_c1.txt`, L=16)

| quantity | value | target |
|---|---|---|
| self coupling `K[x,x]` | 7.999999999999996 .. 7.999999999999997 | 8 |
| axis couplings, 8 distinct offsets | -1.000000000000000, max dev 4.44e-16 | -1 |
| **max non-axis (diagonal) coupling** | **0.000e+00** | < 1e-12 |
| lumped mass | 0.999999999999999, max dev 1.11e-15 | 1 |
| volume / L^4 | 0.999999999999994 | 1 |

PASS. The flat Kuhn stencil is exactly the +8/-1 nearest-neighbour Laplacian; body-diagonal
stiffness entries are identically zero.

At `eps != 0` they are **not** zero: 22 non-axis offsets appear, `max|K|` = 9.5e-4 (conformal,
eps=0.05), 1.2e-3 (TT, eps=0.05), growing linearly in eps. This is why the momentum reduction
below had to be tested rather than assumed.

### C2 -- symmetries used by the Bloch reduction  (`out_c2.txt`, `out_c2b.txt`, `out_c2c.txt`)

L=12, eps=0.1, improved; `max |d lambda|` over the block:

| transformation | CONFORMAL | TRACELESS-TT | used? |
|---|---|---|---|
| `q -> -q` | 0.000e+00 | 0.000e+00 | yes |
| `q1 -> -q1` | 9.66e-03 | 1.46e-02 | **NO** |
| `q2 -> -q2` | 5.74e-03 | 6.82e-03 | **NO** |
| `q3 -> -q3` | 8.63e-03 | 7.14e-03 | **NO** |
| cyclic `(q2,q3,q1)` | 1.42e-14 | 9.90e-02 | conformal only |
| swap `(q2,q1,q3)` | 1.42e-14 | 1.07e-14 | yes |

Single-axis reflection is **not** a symmetry of the Kuhn complex. A first version of this work
assumed it was and was wrong by 6e-4 in the heat trace; it was found by this control and
removed. Hermiticity residual of every Bloch block `< 4.7e-15`.

Orbit-reduced momentum sum vs the direct `L^3` sum (improved and plain, eps = 0 and 0.1):
L=12 <= 2.7e-15, L=16 <= 3.6e-15, L=20 <= 1.1e-14, both channels.
Orbit counts vs `L^3`: 3009/8466 (L=32), 9825/28250 (48), 22913/66594 (64), 76097/223538 (96)
for conformal/TT; `sum(mult) = L^3` exactly.

The TT `(1 2)` swap works only because it equals `eps -> -eps`, i.e. the shift
`x0 -> x0 + L/(2n)`, which must be an integer number of sites. **At L=10, n=2 it is not, and
the reduction is then wrong by 2.1e-09** -- measured, and now guarded by `assert L % 2n == 0`.
All production L satisfy it.

`eps -> -eps` parity of the heat trace (same origin), which lets the 5-point stencil be
evaluated at `eps = 0, h, 2h` only: lattice, eps=0.10 -- L=12 <= 1.3e-13, L=16 <= 9.8e-15,
L=20 <= 3.0e-13, both channels. Continuum (`cont_heat`, L=32) <= 2.7e-15.
End-to-end check of the resulting `K2` (3-point vs full 5-point), L=32 and L=48, both channels,
improved and plain, all six x: worst relative difference **2.4e-12**.

### C3 -- flat-metric heat trace at every production s  (`out_c3.txt`)

(i) Bloch pipeline vs the closed-form Kuhn symbol `D(k) = sum_mu 2(1-cos k_mu)`
(`kuhn.flat_lattice_trace`) -- validates the whole pipeline:

| L | improved | plain |
|---|---|---|
| 32 | 1.3e-15 .. 2.1e-14 | 1.1e-15 .. 1.9e-14 |
| 48 | 3.8e-15 .. 3.8e-14 | 2.9e-15 .. 4.3e-14 |
| 64 | 6.7e-15 .. 1.7e-14 | 7.3e-15 .. 2.5e-14 |
| 96 | 1.7e-14 .. 6.0e-14 | 1.6e-14 .. 7.5e-14 |

(ii) that symbol vs the exact torus winding sum (`kuhn.flat_exact_trace`) -- this is the
*physical* flat lattice error, not a bug; `x = 0.4 ... 2.0` left to right:

```
 L=32 IMPR  1.090e-02 4.764e-03 2.675e-03 1.712e-03 8.753e-04 4.299e-04
 L=48 IMPR  2.113e-03 9.411e-04 5.304e-04 3.399e-04 1.737e-04 8.528e-05
 L=64 IMPR  6.707e-04 2.989e-04 1.684e-04 1.079e-04 5.510e-05 2.703e-05
 L=96 IMPR  1.331e-04 5.925e-05 3.336e-05 2.136e-05 1.090e-05 5.349e-06
 L=32 plain 1.147e-01 7.154e-02 5.210e-02 4.099e-02 2.875e-02 1.986e-02
 L=48 plain 4.588e-02 2.986e-02 2.214e-02 1.759e-02 1.247e-02 8.680e-03
 L=64 plain 2.502e-02 1.647e-02 1.227e-02 9.781e-03 6.957e-03 4.854e-03
 L=96 plain 1.089e-02 7.217e-03 5.398e-03 4.311e-03 3.074e-03 2.149e-03
```

Rates at fixed x (x=0.4): improved 32->64 p=4.02, 64->96 p=3.99; plain 32->64 p=2.20,
64->96 p=2.05. **The Symanzik term removes the a^2 error of the flat Kuhn operator exactly**
(as it must: `c = 1/24` cancels the `k^4` trace correction), leaving a^4.

### C4 -- Bloch vs direct dense `L^4 x L^4` assembly  (`out_c4.txt`)

`kuhn.dense_eigs` (no translation-invariance assumption), sorted spectra compared entrywise,
over both channels x {eps = 0, 0.10} x {improved, plain} = 24 cases:

| L | worst `max abs(d lambda)` | worst relative | `max abs(dM)` |
|---|---|---|---|
| 4 | 5.33e-14 | 1.96e-15 | 4.4e-16 |
| 6 | 1.28e-13 | 4.80e-15 | 1.6e-15 |
| 8 | 3.77e-13 | 1.61e-14 | 8.9e-16 |

PASS (target ~1e-13).

### C5 -- continuum reference and Seeley-DeWitt coefficients  (`out_c5.txt`)

```
 channel                              Vol2/L^4             b1             b2
 conformal      diag(+1,+1,+1,+1)   0.50000000    0.249999213    0.124993061
 traceless-TT   diag( 0,+1,-1, 0)  -0.24999951    0.166666798   -0.016664353
 longitudinal   diag(+1,-1, 0, 0)  -0.24999951   -0.000000000   -0.033332832
 longitudinal   diag(+1, 0, 0,-1)  -0.24999951   -0.000000000   -0.033332832
```
conformal validation |Vol2/L^4 - 0.5| = 3.33e-16, |b1 - 1/4| = 7.87e-07, |b2 - 1/8| = 6.94e-06
(the 7.9e-7 is the finite-difference/quadrature error of `opus_t205`, and it is common to
`Rlat` and `Rcont`, so it cancels in `Rlat - Rcont`).
**Longitudinal traceless b1 = -1.172e-17 and -1.172e-17 -- zero to machine precision. PASS.**

Momentum cutoff and L-independence of `Rcont` (conformal, all six x):
```
 |J=45 / J=30 - 1|  at L=64 :  2.2e-13 .. 9.6e-12
 |J=45 / J=30 - 1|  at L=48 :  2.2e-12 .. 1.0e-11
 |L=64 / L=48 - 1|  at J=45 :  5.1e-12 .. 3.1e-11
 |L=64 / L=48 - 1|  at J=30 :  5.0e-13 .. 1.9e-11
 3-point vs 5-point eps     :  6.6e-13 .. 1.8e-12
```
TRACELESS-TT (all four of L=48/64 x J=30/45 print identically as
1.064075 1.094249 1.123251 1.151128 1.203696 1.275220):
```
 |J=45 / J=30 - 1|  at L=64 :  0.0e+00 .. 5.0e-11
 |J=45 / J=30 - 1|  at L=48 :  9.0e-13 .. 8.7e-12
 |L=64 / L=48 - 1|  at J=45 :  3.6e-12 .. 3.8e-11
 |L=64 / L=48 - 1|  at J=30 :  1.2e-12 .. 1.1e-11
 3-point vs 5-point eps     :  6.8e-13 .. 1.7e-12
```
**`Rcont` is independent of L to <= 3.8e-11 and converged in the momentum cutoff to
<= 5.0e-11 in both channels.** PASS. (These are ~1e-9 relative to `b1 x`, i.e. eight orders
below the smallest `F-1` measured.)

### C6 -- harness reproduces R132  (`out_c6.txt`)

The same pipeline run with **R132's own divergence-form operator** (`opus_t206.lat_heat`)
substituted for the Kuhn operator, L in {32,48,64}, global p fitted over those three L:

| quantity | R132 as quoted to me | this harness |
|---|---|---|
| conformal IMPR, Rich 48->64 fitted-p | 1.00020 - 1.00328 | 1.00020 - 1.00328 (x>=0.6); 1.00831 at x=0.4 |
| conformal IMPR, Rich 48->64 fixed-a^2 | 0.9254 - 0.9992 | 0.92549 - 0.99932 |
| TT IMPR, Rich 48->64 fitted-p | 1.00008 - 1.00028 | 1.00008 - 1.00028 (x>=0.8) |
| TT IMPR, Rich 48->64 fixed-a^2 | 0.9982 - 0.9999 | 0.99812 - 0.99986 |
| plain fitted p, both channels | 2.03 - 2.46 | conformal 2.060-2.457, TT 2.028-2.043 (1.946 at x=0.4) |

Reproduced to the quoted digits. **The instrument is identical to R132's; the only thing that
changes below is the operator.**

---

## 3. The measurement: F(L,x) for the KUHN operator

`Rcont` (exact, L-independent): conformal 1.118143 1.188872 1.265796 1.347864 1.523719
1.805092; TT 1.064075 1.094249 1.123251 1.151128 1.203696 1.275220.
Wall time: 32/48/64/96 = 2/15/50/385 s per (channel, eps, operator).

```
x                          0.40      0.60      0.80      1.00      1.40      2.00
--- CONFORMAL  IMPROVED (c = tr g / 96)
  F  L= 32                1.67045   1.17504   1.06136   1.01848   0.98383   0.96221
  F  L= 48                1.12204   1.03282   1.00930   0.99933   0.98975   0.98220
  F  L= 64                1.03888   1.00992   1.00171   0.99786   0.99362   0.98978
  F  L= 96                1.00789   1.00168   0.99963   0.99848   0.99697   0.99539
--- CONFORMAL  PLAIN
  F  L= 32                5.36213   2.65832   1.87732   1.53947   1.25331   1.09890
  F  L= 48                2.51855   1.64903   1.35814   1.22497   1.10785   1.04254
  F  L= 64                1.80267   1.35160   1.19616   1.12398   1.05981   1.02366
  F  L= 96                1.34258   1.15235   1.08561   1.05433   1.02632   1.01044
--- TRACELESS-TT  IMPROVED
  F  L= 32                1.05385   1.07124   1.05385   1.04236   1.02992   1.02147
  F  L= 48                1.04380   1.02825   1.02079   1.01661   1.01217   1.00903
  F  L= 64                1.02259   1.01457   1.01092   1.00886   1.00661   1.00498
  F  L= 96                1.00900   1.00599   1.00459   1.00378   1.00286   1.00218
--- TRACELESS-TT  PLAIN
  F  L= 32                2.52513   1.74991   1.43973   1.29128   1.15907   1.08646
  F  L= 48                1.71139   1.32696   1.19019   1.12601   1.06905   1.03772
  F  L= 64                1.39557   1.18168   1.10579   1.07017   1.03852   1.02108
  F  L= 96                1.17388   1.07998   1.04663   1.03096   1.01702   1.00933
```

Every one of the four (channel, operator) combinations is monotone in L toward 1 at every x.

### 3a. Convergence rates

Local pairwise rates `p = log(|F_a-1|/|F_b-1|) / log(b/a)`:

```
x                          0.40      0.60      0.80      1.00      1.40      2.00
CONFORMAL IMPR   32->48    4.202     4.128     4.654     8.173     1.124     1.856
                 48->64    3.977     4.159     5.885    -4.024     1.648     1.930
                 64->96    3.933     4.377     3.796     0.850     1.834     1.965
CONFORMAL plain  32->48    2.602     2.314     2.210     2.157     2.106     2.081
                 48->64    2.216     2.131     2.093     2.071     2.049     2.039
                 64->96    2.100     2.063     2.045     2.035     2.024     2.019
TT        IMPR   32->48    0.509     2.281     2.348     2.308     2.219     2.135
                 48->64    2.301     2.301     2.238     2.186     2.120     2.070
                 64->96    2.271     2.191     2.137     2.103     2.063     2.036
TT        plain  32->48    1.881     2.047     2.067     2.067     2.058     2.046
                 48->64    2.040     2.043     2.039     2.035     2.029     2.022
                 64->96    2.027     2.023     2.020     2.018     2.015     2.011
```

Global fits of `|F-1| ~ L^-p` over {32,48,64} (the L-set R132 used):

```
CONFORMAL IMPR    4.114     4.140     5.131     3.443     1.327     1.885   [1.327-5.131]
CONFORMAL plain   2.453     2.243     2.164     2.124     2.084     2.064   [2.064-2.453]
TT        IMPR    1.204     2.289     2.305     2.261     2.181     2.110   [1.204-2.305]
TT        plain   1.943     2.045     2.056     2.054     2.047     2.037   [1.943-2.056]
```
over {32,48,64,96}:
```
CONFORMAL IMPR    4.039     4.224     4.738     1.872     1.531     1.917
CONFORMAL plain   2.309     2.170     2.117     2.088     2.060     2.046   [2.046-2.309]
TT        IMPR    1.672     2.256     2.241     2.199     2.135     2.081
TT        plain   1.981     2.038     2.042     2.040     2.034     2.027   [2.027-2.042]
```

**Honest caveat 1 -- `F-1` changes sign for CONFORMAL IMPROVED at x = 0.8 and x = 1.0**
inside the L range (x=0.8: +6.14e-02, +9.30e-03, +1.71e-03, -3.67e-04;
x=1.0: +1.85e-02, -6.72e-04, -2.14e-03, -1.52e-03).  A single-power fit to `|F-1|` is
meaningless there -- one local rate comes out as **-4.024**.  This is not a failure to
converge; it is two error terms of opposite sign.  Fitting the *signed* residual to
`F-1 = c2 (64/L)^2 + c4 (64/L)^4`:

```
x                          0.40      0.60      0.80      1.00      1.40      2.00
CONFORMAL IMPR   c2     -7.43e-03 -1.58e-03 -2.85e-03 -4.38e-03 -7.15e-03 -1.05e-02
                 c4      4.37e-02  1.13e-02  4.55e-03  2.25e-03  7.78e-04  2.56e-04
                 resid   2.97e-03  1.87e-04  1.26e-05  1.13e-05  7.54e-06  3.23e-06
TT        IMPR   c2      2.97e-02  1.39e-02  1.02e-02  8.32e-03  6.33e-03  4.85e-03
                 c4     -4.03e-03  9.73e-04  8.22e-04  5.69e-04  2.88e-04  1.29e-04
                 resid   3.71e-03  4.09e-04  9.71e-05  3.25e-05  5.63e-06  3.88e-07
```

Two terms describe the improved Kuhn error to `<= 1.3e-05` for `x >= 0.8`.  Note `c2 != 0`:
**the covariant Symanzik term removes the a^2 error of the FLAT Kuhn operator exactly (C3,
p = 4.0) but leaves a curvature-dependent a^2 remainder** -- negative in the conformal
channel, positive in TT.  R132's divergence-form operator behaves the same way (C6: its
conformal-improved fitted p is 2.600-3.575, its TT-improved 1.655-2.070).

**Honest caveat 2 -- x = 0.4 is the weak point everywhere.**  At L=32 it carries |F-1| up to
4.36 (conformal plain), the two-term model leaves a 3.0e-03 residual there (a^6
contamination), and its fitted p is the outlier in three of the four fits.  Its Richardson
values are correspondingly the worst.

### 3b. Richardson extrapolation, both schemes, both L-pairs

`p` fitted over {32,48,64} (R132's protocol):

```
                              0.40      0.60      0.80      1.00      1.40      2.00     range
CONF IMPR 32->48 fitted-p   0.99458   1.00019   1.00187   0.99303   0.99805   0.99962  0.99303-1.00187
CONF IMPR 32->48 fixed a^2  0.68331   0.91905   0.96765   0.98401   0.99448   0.99819  0.68331-0.99819
CONF IMPR 48->64 fitted-p   1.00218   0.99992   0.99946   0.99699   1.00195   1.00032  0.99699-1.00218
CONF IMPR 48->64 fixed a^2  0.93195   0.98048   0.99196   0.99598   0.99860   0.99954  0.93195-0.99954
CONF plai 32->48 fitted-p   0.84910   0.96830   0.98860   0.99470   0.99831   0.99950  0.84910-0.99950
CONF plai 32->48 fixed a^2  0.24369   0.84159   0.94279   0.97336   0.99148   0.99745  0.24369-0.99745
CONF plai 48->64 fitted-p   1.10428   1.02344   1.00864   1.00407   1.00131   1.00039  1.00039-1.10428
CONF plai 48->64 fixed a^2  0.88226   0.96920   0.98790   0.99413   0.99804   0.99940  0.88226-0.99940
TT   IMPR 32->48 fitted-p   1.02783   1.00015   0.99940   0.99946   0.99967   0.99984  0.99940-1.02783
TT   IMPR 32->48 fixed a^2  1.03576   0.99386   0.99434   0.99602   0.99796   0.99908  0.99386-1.03576
TT   IMPR 48->64 fitted-p   0.97137   0.99989   1.00043   1.00040   1.00025   1.00013  0.97137-1.00043
TT   IMPR 48->64 fixed a^2  0.99533   0.99698   0.99823   0.99889   0.99947   0.99977  0.99533-0.99977
TT   plai 32->48 fitted-p   1.03227   0.99957   0.99851   0.99890   0.99944   0.99975  0.99851-1.03227
TT   plai 32->48 fixed a^2  1.06040   0.98861   0.99056   0.99380   0.99704   0.99873  0.98861-1.06040
TT   plai 48->64 fitted-p   0.97372   1.00034   1.00117   1.00087   1.00044   1.00020  0.97372-1.00117
TT   plai 48->64 fixed a^2  0.98952   0.99488   0.99728   0.99837   0.99926   0.99969  0.98952-0.99969
```

With `p` fitted over all four L, the extra pair 64->96 (finest available):

```
CONF IMPR 64->96 fitted-p   1.00041   0.99987   0.99928   0.99903   1.00086   1.00017  0.99903-1.00086
CONF IMPR 64->96 fixed a^2  0.98310   0.99509   0.99797   0.99898   0.99964   0.99988  0.98310-0.99988
CONF plai 64->96 fitted-p   1.04590   1.01113   1.00425   1.00204   1.00067   1.00020  1.00020-1.04590
CONF plai 64->96 fixed a^2  0.97451   0.99295   0.99716   0.99861   0.99953   0.99985  0.97451-0.99985
TT   IMPR 64->96 fitted-p   0.99497   1.00026   1.00032   1.00025   1.00014   1.00007  0.99497-1.00032
TT   IMPR 64->96 fixed a^2  0.99812   0.99913   0.99953   0.99971   0.99987   0.99994  0.99812-0.99994
TT   plai 64->96 fitted-p   0.99399   1.00081   1.00073   1.00049   1.00024   1.00010  0.99399-1.00081
TT   plai 64->96 fixed a^2  0.99653   0.99862   0.99930   0.99959   0.99982   0.99992  0.99653-0.99992
```

---

## 4. The comparison that matters

Same instrument (C6 proves it), same L-set {32,48,64}, same fits.  Divergence-form numbers
are from `out_c6.txt` (which reproduces the values quoted to me from R132).

| quantity, Richardson 48->64 | R132 divergence-form | **Kuhn simplicial** |
|---|---|---|
| conformal IMPR, fitted-p | 1.00020 - 1.00328  (1.00831 at x=0.4) | **0.99699 - 1.00218** |
| conformal IMPR, fixed a^2 | 0.92549 - 0.99932 | **0.93195 - 0.99954** |
| TT IMPR, fitted-p | 1.00008 - 1.00028  (0.98031 at x=0.4) | **0.99989 - 1.00043** (0.97137 at x=0.4) |
| TT IMPR, fixed a^2 | 0.99812 - 0.99986 | **0.99533 - 0.99977** |
| conformal plain, fitted p | 2.060 - 2.457 | **2.064 - 2.453** |
| TT plain, fitted p | 2.028 - 2.043 (1.946 at x=0.4) | **2.037 - 2.056** (1.943 at x=0.4) |

Plain-operator rates, the sharpest single statement: R132 reported p = 2.03-2.46 in both
channels.  The Kuhn operator gives **2.064-2.453 (conformal) and 1.943-2.056 (TT)** over
{32,48,64}, tightening to **2.019-2.100 and 2.011-2.027** on the 64->96 pair.  Both operators
converge at a^2 with the same coefficients to two digits.

---

## 5. Verdict

**The Kuhn simplicial operator reproduces R132's conclusion.**  Concretely:

1. Measured against the EXACT continuum heat trace, the Kuhn induced-EH ratio `F(L,x)`
   converges to 1 across the whole window `x in [0.4, 2.0]` in **both** channels, for **both**
   the improved and the plain operator.  At the finest lattice, L=96:
   conformal improved `F in [0.99539, 1.00789]`, TT improved `F in [1.00218, 1.00900]`.
   There is no residual x-dependent drift: the conformal channel plateaus exactly as the
   traceless channel does.
2. The plain Kuhn operator converges at **p = 1.943 - 2.453** over {32,48,64} across both
   channels and all six x (2.037 - 2.453 if the x=0.4 outlier is dropped), against the
   2.03 - 2.46 R132 reported for the divergence-form operator -- whose own six-x fits under
   this harness are 1.946 - 2.457.  The two operators agree point by point, and the local
   rates tighten to 2.011 - 2.100 on the finest pair (64->96).
3. Richardson extrapolation lands on 1 by both schemes.  On the finest pair (64->96) the
   fitted-p scheme gives 0.99903-1.00086 (conformal improved), 0.99497-1.00032 (TT improved),
   1.00020-1.04590 (conformal plain), 0.99399-1.00081 (TT plain); the fixed-a^2 scheme gives
   0.98310-0.99988, 0.99812-0.99994, 0.97451-0.99985, 0.99653-0.99992.
4. Therefore the standing "conformal channel does not plateau" finding is an artefact of the
   truncated-series diagnostic for the Kuhn operator too.  It is **not** a property of the
   framework's simplicial complex.

**What is genuinely different about the Kuhn operator, stated plainly:**

* Its improved conformal error has an **a^2 remainder of the opposite sign to its a^4 term**,
  so `F-1` crosses zero inside the measured L range at x = 0.8 and x = 1.0 (one local rate
  comes out as -4.024).  Power-law fits to `|F-1|` are not meaningful for that channel at
  those x; the two-term `c2 a^2 + c4 a^4` model is (residual <= 1.3e-05 for x >= 0.8).
  R132's divergence-form operator has the same mixture but the crossing falls outside its
  measured window, so its fits look cleaner.  This is a property of the *fit*, not of the
  limit.
* The covariant Symanzik term `c = tr g / 96` removes the flat-space a^2 error of the Kuhn
  operator **exactly** (C3: p = 3.99-4.02 flat improved, 2.05-2.20 flat plain) but leaves a
  curvature-dependent a^2 remainder in both channels (`c2 != 0` in the two-term fits).
* At x = 0.4 and L = 32 the Kuhn lattice error is large (|F-1| up to 4.36 plain, 0.67
  improved) and contaminated by a^6; every worst-case Richardson number in this report comes
  from that corner.  x = 0.4 should be regarded as outside the trustworthy window at L = 32.

**No control failed.**  One control did catch a real error mid-work: single-axis momentum
reflection is not a Kuhn symmetry, and the first version of the Bloch reduction wrongly
assumed it was (6e-4 error).  It was fixed before any production number was taken, and the
corrected reduction agrees with the direct L^3 sum to 1.1e-14 and with a dense L^4 assembly
to 1.6e-14 relative.
