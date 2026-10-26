# NN Lattice Rescaled-Lane C_arm NNLO Saddle Note (2026-05-10)

**Claim type:** bounded_theorem (a separate aperture q^2 Gaussian comparator matches
the four-point C_arm alpha fit inside the scoped deterministic-rescale harness;
does not change authority for the unaudited upstream chain)
**Status authority:** source-note proposal only; audit verdict and effective
status are set by the independent audit lane.
**Primary runner:** [`scripts/lattice_nn_rescaled_C_arm_NNLO_saddle.py`](../scripts/lattice_nn_rescaled_C_arm_NNLO_saddle.py)
**Cached log:** [`logs/runner-cache/lattice_nn_rescaled_C_arm_NNLO_saddle.txt`](../logs/runner-cache/lattice_nn_rescaled_C_arm_NNLO_saddle.txt)

## Status

`bounded`: the separate aperture q^2 Gaussian comparator reduces the fit-window
residual to `|alpha_aperture - 0.5256| = 0.0009 <= 0.005`, closing the 33%
alpha gap left by the NLO saddle note inside this scoped empirical
comparison. This does not change authority for the upstream notes or the
dependency chain.

## Companion work

| Source note | Outcome |
| ------ | ---------------------------------------------------------- |
| [`NN_LATTICE_RESCALED_CONTINUUM_IDENTIFICATION_NOTE_2026-05-10.md`](NN_LATTICE_RESCALED_CONTINUUM_IDENTIFICATION_NOTE_2026-05-10.md) | Numerical fit: `sigma_arm(h) = 2.7107 * h^{0.5256}` on the 4-point window `h <= 0.25`. |
| [`NN_LATTICE_RESCALED_C_ARM_DERIVATION_NOTE_2026-05-10.md`](NN_LATTICE_RESCALED_C_ARM_DERIVATION_NOTE_2026-05-10.md) | LO saddle: `alpha_LO = 0.5000`, `C_arm_LO = 2.4855`. |
| [`NN_LATTICE_RESCALED_C_ARM_ALPHA_CONSTRAINED_REFIT_NOTE_2026-05-10.md`](NN_LATTICE_RESCALED_C_ARM_ALPHA_CONSTRAINED_REFIT_NOTE_2026-05-10.md) | Alpha-constrained refit: per-h residual <1% at h = 0.015625; is consistent with the LO value at that finite point. |
| [`NN_LATTICE_RESCALED_C_ARM_NLO_SADDLE_NOTE_2026-05-10.md`](NN_LATTICE_RESCALED_C_ARM_NLO_SADDLE_NOTE_2026-05-10.md) | NLO phase+q^4: `alpha_NLO = 0.5170`, residual `|delta alpha| = 0.0086` (closes 67%). |
| This note | Separate aperture q^2 Gaussian: `alpha_aperture = 0.5247`, residual `|delta alpha| = 0.0009` on the same fit window. |

## Task statement

Compare linearized bulk q^4/q^6 corrections with a separate aperture q^2
Gaussian model. This is not a complete NNLO expansion. Three comparisons:

1. NNLO phase: cos(omega h) to O(h^4) and beyond.
2. Linearized bulk saddle: q^6 cumulant of the lateral random walk.
3. Finite-slit-aperture correction: truncation of the pre-slit wavefunction
   to the physical aperture `y in [SLIT_Y, SLIT_Y + W] = [3, 5]`.

Compare the bulk corrections and the separate aperture q^2 model using
the same fit protocol; they are not combined additively. Acceptance bands:
- **strong-closure**: `|alpha_aperture - 0.5256| <= 0.005` inside this bounded
  empirical comparison.
- **bounded**: `|alpha_aperture - 0.5256| <= 0.012` and >=30% improvement over NLO.
- **null**: the aperture comparator does not improve the finite fit.

This note registers the strong-closure numerical outcome as bounded science.

## Setup recap

Per-edge amplitudes at lattice spacing `h`:
```
a_0(h)  = exp(i k h)         / sqrt(F)
a_pm(h) = c * exp(i k h sqrt(2)) / sqrt(2 F)
```
with the common amplitude scale removed, `F = FANOUT = 3`, `c = exp(-BETA * pi^2 / 16) ~ 0.6105`,
`k = K_PHYS = 5`, `BETA = 0.8`. The lateral characteristic function is
```
g(q; h) = a_0(h) + 2 a_pm(h) cos(q h).
```

Let `A := |a_pm| |a_0| = c / (F sqrt(2))`, `B := 2 |a_pm|^2 = c^2 / F`,
`omega := k (sqrt(2) - 1) = 2.07107`, `r := A/(A+B) = 0.53666`.

The leading-order saddle gives `sigma^2_LO(h) = C_LO^2 h` with
```
C_LO^2 = L_2 (c^2 / (2 F)) / (A + B) = 6.17786,    C_LO = 2.48553
```
where `L_2 = 2 L_total / 3 = 26.667` is the post-slit propagation length.

The NLO saddle note supplemented the saddle with the cos(omega h) phase factor in the
denominator `A cos(omega h) + B` (the real part of `a_pm conj(a_0)`):
```
sigma^2_NLO(h) = C_LO^2 h * (1 + delta_a(h)),
delta_a(h)     = (A+B) / (A cos(omega h) + B) - 1.
```

The NLO runner already uses the exact cos(omega h), so further orders of
this expansion contribute zero. (This is documented below as a sharp null on
candidate 1.)

---

## 1) NNLO phase (cos(omega h) to O(h^4) and beyond)

### Expansion

Let `x := (omega h)^2`. Then
```
A cos(omega h) + B = (A+B) - A x/2 + A x^2/24 - A x^3/720 + A x^4/40320 - ...
                   = (A+B) [1 - r x/2 + r x^2/24 - r x^3/720 + r x^4/40320 - ...]
```
so
```
delta_a(h) = (A+B) / (A cos(omega h) + B) - 1
           = 1 / (1 - u) - 1
           = u + u^2 + u^3 + u^4 + ...
```
with
```
u(x) = c_1 x + c_2 x^2 + c_3 x^3 + c_4 x^4 + ...
c_1  = r/2,  c_2 = -r/24,  c_3 = r/720,  c_4 = -r/40320,  ...
```

Collecting powers of `x` in `u + u^2 + u^3 + u^4`:
```
[x^1]:  c_1                                              = r/2
[x^2]:  c_2 + c_1^2                                       = -r/24 + r^2/4
[x^3]:  c_3 + 2 c_1 c_2 + c_1^3                           = r/720 - r^2/24 + r^3/8
[x^4]:  c_4 + 2 c_1 c_3 + c_2^2 + 3 c_1^2 c_2 + c_1^4
     = -r/40320 + r^2/720 + r^2/576 - r^3/32 + r^4/16
```

Since `x^k = (omega h)^{2k}`, this gives a power series in `h^2`:
```
delta_a(h) = d2 h^2 + d4 h^4 + d6 h^6 + d8 h^8 + ...
```

### Closed-form coefficients (NEW; the rest of the cos series)

| Coefficient | Closed form                                                          | Numerical    |
| ----------- | -------------------------------------------------------------------- | ------------ |
| `d2`        | `(r/2) omega^2`                                                       | `1.150955`   |
| `d4`        | `(r^2/4 - r/24) omega^4`                                              | `0.913297`   |
| `d6`        | `(r^3/8 - r^2/24 + r/720) omega^6`                                    | `0.636480`   |
| `d8`        | `(r^4/16 - r^3/32 + r^2/576 + r^2/720 - r/40320) omega^8`             | `0.420024`   |

(The `d2` value matches the NLO saddle note exactly.)

### Numerical check: truncated series vs exact (the cos closed form)

| `h`       | `delta_a` exact | `d2 h^2`   | `d2 h^2 + d4 h^4` | `d2 h^2 + d4 h^4 + d6 h^6` |
| --------- | -------------- | ---------- | ------------------ | --------------------------- |
| 0.50000   | 0.356719       | 0.287739   | 0.344820           | 0.354765                    |
| 0.25000   | 0.075664       | 0.071935   | 0.075502           | 0.075658                    |
| 0.12500   | 0.018209       | 0.017984   | 0.018207           | 0.018209                    |
| 0.06250   | 0.004510       | 0.004496   | 0.004510           | 0.004510                    |
| 0.03125   | 0.001125       | 0.001124   | 0.001125           | 0.001125                    |

The h^2 + h^4 + h^6 partial sum differs from the exact `delta_a(h)` by
about `6.5e-6` at h=0.25 (within the `1e-5` guard). The difference decreases
at the smaller tabulated h; the next series term is of order h^8.

### Verdict (candidate 1)

**Sharp null.** The NLO runner uses the closed-form
`(A+B)/(A cos(omega h) + B) - 1` (not the h^2 truncation), so d4, d6, d8
contribute zero new physics. They are reported as analytic record.

---

## 2) Linearized bulk q^4/q^6 saddle corrections

Per-edge: let `s := a_pm / g(0; h)`. With `u := q h`:
```
g(q; h)/g(0; h) = 1 - s u^2 + (s/12) u^4 - (s/360) u^6 + O(u^8)
```
(using `cos(q h) = 1 - u^2/2 + u^4/24 - u^6/720 + ...` and
`g/g0 = 1 + (2 a_pm/g0)(cos - 1) = 1 - s u^2 + (s/12) u^4 - (s/360) u^6 + ...`).

Then `log(g/g0) = xi - xi^2/2 + xi^3/3 - ...` with
`xi = -s u^2 + (s/12) u^4 - (s/360) u^6`:
```
log(g/g0) = -s u^2
            + (s/12 - s^2/2) u^4
            + (-s/360 + s^2/12 - s^3/3) u^6
            + O(u^8)
```

After `N = L_2 / h` edges:
```
g^N(q)/g(0)^N = exp[ -alpha_2 q^2 - alpha_4 q^4 - alpha_6 q^6 + ... ]
```
with
```
alpha_2 = L_2 s h                            (complex; LO support)
alpha_4 = L_2 (s^2/2 - s/12) h^3              (complex; NLO saddle)
alpha_6 = L_2 (s^3/3 - s^2/12 + s/360) h^5    (complex; NEW)
```

This calculation retains only terms linear in `alpha_4` and `alpha_6`.
It omits the quadratic q^4 contribution, which is of the same asymptotic
order as the linear q^6 contribution. For example, for real coefficients
`a > 0`, `b`, `c` in `exp(-a q^2 - b q^4 - c q^6)`, formal Gaussian-moment
expansion about `b=c=0` of the normalized Parseval variance gives
`a + 3b/(2a) - 9b^2/(4a^3) + 45c/(16a^2) + ...`.
With `a ~ h`, `b ~ h^3`, `c ~ h^5`, the `b^2` and `c` terms are both
absolute `O(h^3)`. This counterexample to complete-NNLO accounting does
not supply the omitted full complex-coefficient expansion or a remainder bound.
The unchanged numerical table below is the linearized calculation only.

Treat `alpha_6` as a perturbation on the LO complex-Gaussian inverse FT.
`|A(y)|^2 = |A_0(y)|^2 (1 - 2 Re[alpha_4 X_4(y)] - 2 Re[alpha_6 X_6(y)] + ...)`.

With `mu := 1/(4 alpha_2)`:
- `X_4(y) = 12 mu^2 - 48 mu^3 y^2 + 16 mu^4 y^4`
- `X_6(y) = 120 mu^3 - 720 mu^4 y^2 + 480 mu^5 y^4 - 64 mu^6 y^6`

(`X_6 = -A_0^{(6)}/A_0`: the negative sign comes from the inverse
Fourier transform of `q^6`. In particular the sixth derivative at `y=0`
is `-120 mu^3 A_0(0)`. The polynomial and variance-correction signs
above are unchanged.)

Real variance correction with Gaussian moments
`<y^{2k}>_{G(0, sigma_0)} = (2k-1)!! sigma_0^{2k}`:
```
dV_6 = -2 Re( alpha_6 ( <y^2 X_6> - sigma_0^2 <X_6> ) )
```
where `sigma_0^2 = L_2 h |s|^2 / Re(s)`.

### Numerical magnitude

| `h`       | `sigma_0^2` | `dV_q4`              | `dV_q6`              | `|dV_q6| / sigma_0^2` |
| --------- | ---------- | -------------------- | -------------------- | --------------------- |
| 0.25000   | 1.661325   | +4.184e-3            | +8.889e-6            | 5.4e-6                |
| 0.12500   | 0.786294   | +8.271e-4            | +1.191e-6            | 1.5e-6                |
| 0.06250   | 0.387857   | +1.944e-4            | +1.508e-7            | 3.9e-7                |
| 0.03125   | 0.193275   | +4.786e-5            | +1.891e-8            | 9.8e-8                |
| 0.015625  | 0.096556   | +1.192e-5            | +2.365e-9            | 2.4e-8                |

### Verdict (candidate 2)

**Sharp null.** The q^6 saddle correction is sub-leading by ~10^3 to the
difference from the aperture comparator (candidate 3) on the fit window. It alone
would not detectably move alpha.

---

## 3) Separate finite-slit-aperture q^2 Gaussian comparator

### Setup

The slit at layer `nl // 3` blocks all `y` except the aperture
`y in [SLIT_Y, SLIT_Y + SLIT_W] = [3.0, 5.0]` (physical units). The arm
distance is `sqrt(<y_det^2>)` of the conditional detected distribution.

In the saddle / continuum limit, the lattice propagator from the origin to
the slit layer (length `L_1 = L_total / 3`) is a complex Gaussian
```
psi_pre(y_s) = (2 pi alpha_pre)^{-1/2} exp(-y_s^2 / (4 alpha_pre)),
alpha_pre    = L_1 s h.
```

The post-slit kernel from `y_s` at the slit layer to `y` at the detector
(length `L_2 = 2 L_total / 3`) is also a complex Gaussian
```
K(y, y_s; alpha_post) = (2 pi alpha_post)^{-1/2} exp(- (y - y_s)^2 / (4 alpha_post)),
alpha_post           = L_2 s h.
```

### Closed-form aperture-truncated convolution

The detected amplitude is
```
psi_det(y) = int_{SLIT_Y}^{SLIT_Y + SLIT_W} dy_s  psi_pre(y_s) K(y, y_s; alpha_post).
```

Completing the square in `y_s`:
- Define `M := 1/alpha_pre + 1/alpha_post = (alpha_pre + alpha_post) / (alpha_pre alpha_post)`.
- Define `y_c(y) := y / (alpha_post M)`.
- The y_s exponent becomes `-(M/4) (y_s - y_c)^2` plus a piece quadratic in y.
- That piece simplifies (using `1 - alpha_post M = -alpha_post / alpha_pre`) to
  `-y^2 / (4 (alpha_pre + alpha_post))`.

The `y_s` integral is a complex error function:
```
int_a^b dy_s exp(- (M/4) (y_s - y_c)^2)
    = (sqrt(pi) / sqrt(M)) [ erf((b - y_c) sqrt(M)/2) - erf((a - y_c) sqrt(M)/2) ]
```
(`erf` evaluated at complex argument). Dropping y-independent constants:
```
psi_det(y) propto exp(- y^2 / (4 alpha_total)) * Phi(y)
alpha_total = alpha_pre + alpha_post = L_total s h
Phi(y)      = erf(u_b(y)) - erf(u_a(y))
u_{a,b}(y)  = (SLIT_Y_{a,b} - y/(alpha_post M)) * sqrt(M) / 2
SLIT_Y_a    = SLIT_Y,  SLIT_Y_b = SLIT_Y + SLIT_W.
```

This is the **closed-form aperture q^2 Gaussian wavefunction** at the detector. Both factors
are analytic (complex erf is standard). Moments
`mu_arm = <y>` and `sigma_arm^2 = <y^2> - <y>^2` are then computed by 1D
quadrature on `|psi_det(y)|^2` -- the integrand is closed-form, only the
1D moment integrals are numerical.

### Numerical agreement on the continuum diagnostic four-point fit window

| `h`       | `mu_meas` | `mu_aperture` | `sigma_meas` | `sigma_aperture` | residual (aperture) | residual (NLO only) |
| --------- | --------- | --------- | ------------ | ------------ | --------------- | ------------------- |
| 0.25000   | 3.3168    | 3.4302    | 1.3198       | 1.3171       | -0.205%         | -2.339%             |
| 0.12500   | 3.1701    | 3.2268    | 0.8990       | 0.8996       | +0.063%         | -1.365%             |
| 0.06250   | 3.0895    | 3.1191    | 0.6282       | 0.6281       | -0.020%         | -0.862%             |
| 0.03125   | 3.0467    | 3.0616    | 0.4416       | 0.4417       | +0.023%         | -0.446%             |

**Max sigma residual on fit window: 0.21%** (aperture) vs **2.34%** (NLO only).
The aperture q^2 Gaussian matches each fit-window point to <0.3%.

### Numerical correction and bounded scope (h = 0.015625)

The earlier `sigma_arm=0.2884` was a numerical artifact: subtracting two
complex error functions near one loses the transmitted tail. The identical
expression `erfc(u_a)-erfc(u_b)` gives `sigma_arm=0.3115125955` and
`mu_arm=3.0314537886`, versus the supplied measurements `0.3115` and
`3.0239`. This is not evidence for ballistic or non-Gaussian dominance;
that earlier explanation is withdrawn.

An independent scaled direct aperture convolution agrees on the unchanged
four-point fit window and at `h=0.015625, 0.0078125`, with quadrature-order
controls. The alpha comparison still uses exactly the original four points.
More extreme complex arguments require separate numerical stability checks;
neither the corrected fine point nor agreement with supplied measurements
proves asymptotic validity, a continuum limit, or exact lattice equivalence.

---

## 4) Separate model fits

Applying the continuum diagnostic's log-log linear fit protocol to each model on the fit
window `h in {0.25, 0.125, 0.0625, 0.03125}`:

| Model                          | `alpha_eff` | `C_eff`  | `|alpha - 0.5256|` |
| ------------------------------ | ----------- | -------- | ------------------- |
| LO     (C_arm support)         | 0.5000      | 2.4855   | 0.0256              |
| NLO    (phase note, exact)     | 0.5165      | 2.6186   | 0.0091              |
| Linearized bulk (phase + q^4 + q^6)     | 0.5170      | 2.6234   | 0.0086              |
| **Aperture q^2 comparator**     | **0.5247**  | **2.7041** | **0.0009**       |
| EMPIRICAL  (continuum)         | 0.5256      | 2.7107   | --                  |

**Finite-fit comparison**: the aperture q^2 Gaussian gives residual
`0.0009`, versus `0.0086` for the linearized bulk model, a factor-9.6
reduction. This is not a complete NNLO or additive aperture correction.

Local alpha at the geometric-mean fit-window point `h_geom = sqrt(0.25 * 0.03125) = 0.08839`:
- LO          : `alpha_local = 0.5000`
- NLO (phase) : `alpha_local = 0.5090`
- Aperture q^2 : `alpha_local = 0.5175`

(The fit-window alpha is dominated by the steeper h = 0.25 endpoint.)

---

## Acceptance verdict

`|alpha_aperture - 0.5256| = 0.0009 <= 0.005`. This clears the
strong-closure band inside the bounded fit-window comparison.

All eight bounded-support guards PASS:

- `delta_a(h) > 0` on the fit window.
- Phase series `h^2 + h^4 + h^6` matches the exact `delta_a` to 1e-5 at h = 0.25.
- `|alpha_aperture - 0.5256| <= 0.005` (strong-closure band).
- `alpha_aperture > alpha_NLO` (strict improvement).
- `alpha_aperture <= 0.5256` (no overshoot in this finite comparison).
- Max sigma residual on fit window <= 1.0% (achieved: 0.21%).
- `q^6` saddle term sub-leading (`|dV_q6| / sigma^2 < 1e-2` on the fit window).
- the supplied finer measured point is within 1% of `C_LO` after division
  by `sqrt(h)`; this finite comparison is not a proof of an `h -> 0` limit.

## Comparison of the original 0.0256 alpha residual

| Source                             | `alpha_eff` contribution | running cumulative      |
| ---------------------------------- | ------------------------ | ----------------------- |
| LO   saddle                         | 0.5000                   | residual 0.0256 left    |
| NLO  phase (cos(omega h) resummed) | +0.0165                  | residual 0.0091 left    |
| Linearized q^4 saddle                    | +0.0005                  | residual 0.0086 left    |
| Linearized q^6 saddle                    | < 0.0001                 | residual ~0.0086 left   |
| **Aperture q^2 model versus bulk q^4+q^6 model** | **difference +0.0077** | **residual 0.0009 left**|
| Aperture q^2 model                 | 0.5247                   | clears fit-window band  |

The aperture q^2 Gaussian and the bulk phase+q^4+q^6 calculation are
separate comparators. The displayed +0.0077 is their slope difference,
not a derived additive aperture correction on top of q^4 and q^6. The
runner's `NNLO_full` legacy function identifier denotes the aperture q^2 model only;
`NNLO_q` denotes linearized bulk q^4/q^6, not a complete NNLO result.

## Cross-validation against the alpha-constrained refit

The alpha-constrained refit gives `C_arm(h)` per h:

| `h`       | `C_arm(h) := sigma_arm(h)/sqrt(h)` | predicted C_arm (aperture q^2) |
| --------- | ----------------------------------- | ------------------------------ |
| 0.25000   | 2.6396                              | 2.6342                         |
| 0.12500   | 2.5428                              | 2.5444                         |
| 0.06250   | 2.5128                              | 2.5123                         |
| 0.03125   | 2.4981                              | 2.4986                         |

C_arm(h) per-h matches predicted aperture q^2 to <0.3% on the fit window. The
finer supplied measurement is within 0.3% of `C_LO = 2.4855`. This is
a finite-point comparison, not an asymptotic proof or evidence for a
ballistic-tail mechanism.

## Files

- `scripts/lattice_nn_rescaled_C_arm_NNLO_saddle.py` — linearized bulk q^4/q^6
  calculation and separate aperture q^2 comparator, with finite fit-window
  comparisons against supplied measurements.
- `docs/NN_LATTICE_RESCALED_C_ARM_NNLO_SADDLE_NOTE_2026-05-10.md` (this file).

## What is NOT claimed

- No re-measurement of any sigma_arm value. The empirical data are the
  measurements from the continuum diagnostic and alpha-constrained refit,
  unchanged.
- No fit-protocol change. The same 4-point log-log fit of the continuum
  diagnostic is
  applied to each model uniformly.
- No universal validity below the fit window. The stable evaluation is
  checked at two finer points, but this does not prove the Gaussian
  approximation controls an arbitrarily small-h lattice tail.

## Superseded numerical record and recovery

The original note, runner and cached output are recoverable byte-for-byte at
Git commit `f24d17d97d372df977476e4a69674577f31af575` under their unchanged
repository paths. The intermediate PR receipt is separately recoverable at
`3c90f9860c3bae63ee64949e7178290f789dd982` under the same paths. The linked
cache is the refreshed execution receipt for the corrected runner, not the
base-commit historical execution. Its capture binds the actual source and
inputs; neither receipt changes audit status.

Numerical regression: `python3 -m unittest discover -s tests -p test_lattice_nn_saddle_numerics.py -v`.
The controls compare direct scaled aperture convolution at two quadrature
orders against the error-function evaluator and explicitly recover the
old cancellation failure. They do not remeasure the empirical lattice data.
