# Native Gauge Transfer — Reduced-A2 Spectral Comparison c_D vs c_J (H_spec attempt)

**Date:** 2026-06-12
**Claim type:** open_gate
**Type:** source-side obstruction map

Status authority: independent audit lane only. This source note does not set or predict an audit outcome.

**Claim boundary:** this note attempts H_spec — the reduced-A2 spectral comparison `c_D <= c_J` that Route A (eventual monotonicity of `lambda_1/lambda_0`) requires (per the W86 block-Hellmann split). Honest outcome: the comparison `c_D <= c_J` HOLDS on the tested `beta` range (the margin `c_J - c_D > 0` at every tested `beta`), which is consistent with — and supports — the measured monotone decrease of `lambda_1/lambda_0`. BUT the margin SHRINKS toward 0 as `beta` grows: `c_D/c_J` climbs monotonically toward 1 and the leading-order coefficients `c_J`, `c_D` become near-equal (`~0.857`). Therefore H_spec as a UNIFORM strict domination (margin bounded away from 0) is NOT established; the survival of the strict inequality in the large-`beta` limit is a delicate subleading question. No closure of the half-line gap theorem is claimed and no constant is fitted.

No new axiom, literature estimate, external value, comparator number, fitted constant, rounded anchor, value-from-target step, parity proxy, or fitted prefactor is used. The `c_J`, `c_D` values are WITNESSED spectral quantities of the finite half-slice operator; they are not fitted to any target.

**Primary runner:** [scripts/native_gauge_transfer_reduced_a2_spectral_domination_rung_eleven_bounded_2026_06_12.py](../scripts/native_gauge_transfer_reduced_a2_spectral_domination_rung_eleven_bounded_2026_06_12.py)

**Runner cache:** [logs/runner-cache/native_gauge_transfer_reduced_a2_spectral_domination_rung_eleven_bounded_2026_06_12.txt](../logs/runner-cache/native_gauge_transfer_reduced_a2_spectral_domination_rung_eleven_bounded_2026_06_12.txt)

## One-Hop Authorities

- [NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md) for the exact block-Hellmann split, the `c_J = A_0 - A_1`, `c_D = B_1/mu_1 - B_0/mu_0` definitions, the reduced operator `T_infty = S_(1/2) M_[H exp(-Q)] S_(1/2)`, and the H_spec naming. Quote anchor: "derive or bound `c_D <= c_J` for the reduced spectral pair, then transfer it to the exact Wilson diagonal".
- [NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md) for the saddle profile `H exp(-Q)`, the scaling `a = weight/sqrt(beta)`, and `Q = x^2 + x y + y^2` (the A2 quadratic form).
- [GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md) for the exact source-character recurrence used by the diagonal derivative.

Related context, not one-hop authority: the W88 sufficiency map names H_spec as one of the two remaining lemmas (with H_det) for full closure.

## The Quantities

Per the W86 block-Hellmann split, for the simple top eigenpair `(lambda_i, v_i)` of the
finite half-slice operator `T_beta = E D_beta E`, `E = exp((beta/2) J)`:

```text
d/dbeta log(lambda_i) = <v_i|J|v_i> + <v_i|E D_beta' E|v_i>/lambda_i,
Delta_J = <v_1|J|v_1> - <v_0|J|v_0>  ~ -c_J/beta,
Delta_D = <v_1|E D' E|v_1>/lambda_1 - <v_0|E D' E|v_0>/lambda_0  ~  c_D/beta,
```

so `c_J = lim beta*(-Delta_J)` and `c_D = lim beta*Delta_D`. The diagonal
derivative is exact: `r'_(p,q) = c'_(p,q)/c_(0,0) - c_(p,q) c'_(0,0)/c_(0,0)^2`
with `c' = (1/6) sum_neighbors c` (the character recurrence). Eventual
monotonicity (`lambda_1/lambda_0` decreasing) is equivalent to
`d/dbeta log(lambda_1/lambda_0) = Delta_J + Delta_D ~ -(c_J - c_D)/beta < 0`,
i.e. to `c_D <= c_J`.

## The Finding (witnessed, not fitted)

The runner computes the WITNESSED `c_J`, `c_D` from the finite operator
spectrum across `beta`:

| beta | shell | c_J | c_D | c_J - c_D | c_D/c_J | lambda_1/lambda_0 |
|---:|---:|---:|---:|---:|---:|---:|
| 15 | 16 | 0.811415 | 0.702465 | 0.108950 | 0.86573 | 0.21634 |
| 30 | 21 | 0.834363 | 0.779367 | 0.054996 | 0.93409 | 0.20481 |
| 60 | 28 | 0.847469 | 0.819819 | 0.027651 | 0.96737 | 0.19925 |
| 120 | 37 | 0.854701 | 0.840331 | 0.014369 | 0.98319 | 0.19650 |
| 180 | 45 | 0.857260 | 0.847168 | 0.010093 | 0.98823 | 0.19559 |

Two facts are robust across the range (shells `~3.3-3.8 sqrt(beta)`):

1. THE COMPARISON HOLDS: `c_D < c_J` at every tested `beta` (margin strictly
   positive). Hence `d/dbeta log(lambda_1/lambda_0) ~ -(c_J - c_D)/beta < 0`:
   the ratio DECREASES, consistent with the independently measured monotone
   trajectory (rung five, `beta = 2..50`). This SUPPORTS Route A monotonicity.

2. THE MARGIN SHRINKS toward 0, consistent with `~const/beta`: `c_J - c_D`
   decreases monotonically (`0.055 -> 0.028 -> 0.014 -> 0.010`) and `c_D/c_J`
   climbs monotonically toward 1 (`0.934 -> 0.967 -> 0.983 -> 0.988`). The
   displayed products `beta*(c_J - c_D)` stay `O(1)` (`1.63 -> 1.82`) across
   `beta = 15..180`. This indicates, but does not prove, equal leading-order
   coefficients `c_J` and `c_D` near `~0.857`; if that trend persists, the
   strict inequality lives at the `1/beta` subleading order. The per-`beta`
   monotone-decrease rate `(c_J - c_D)/beta` then vanishes as `O(beta^-2)`:
   the decrease is real on the tested range but ever slower.

## What This Means For H_spec (the honest revision)

- The naive expectation from W86's finite-`beta` tightness `c_D/c_J -> 0.958`
  was that `c_D <= c_J` holds with a comfortable margin. The `beta`-extrapolation
  here REVISES that: 0.958 was a finite-`beta` value, and the margin actually
  SHRINKS as `beta` grows (`c_D/c_J` climbs toward 1). The leading coefficients
  are near-equal.

- Consequence for Route A: `c_D <= c_J` (margin > 0) gives eventual monotonicity
  pointwise on the tested range, and the ratio's measured decrease is genuine.
  But H_spec as a UNIFORM strict domination — a margin bounded below by a
  positive constant for all `beta >= beta_0`, which is what a clean half-line
  closure would use — is NOT established here. The strict inequality's survival
  in the large-`beta` limit (whether `c_J - c_D -> 0^+` stays positive, or the
  leading coefficients are exactly equal so the sign is decided by the next
  order) is a delicate subleading question.

- THE SHARPENED OBSTRUCTION: the data points toward equal leading limits
  `c_J = c_D -> ~0.857`, because the margin shrinks while
  `beta*(c_J - c_D)` stays `O(1)`. That is not a proof of the limit. It says
  the current witnessed evidence does not decide Route A by a uniform leading
  separation; closing Route A requires deriving the exact reduced-A2 leading
  coefficients (closed-form Gaussian/Hermite moments of `Phi_0`, `Phi_1`) and,
  if they coincide, deriving the `1/beta` subleading coefficient and proving it
  is positive uniformly.

## Two Readings

1. Tested-range reading (used here): `c_D < c_J` on `beta in {30,60,120,180}`
   (margin > 0), so the ratio decreases there. This is a witnessed spectral
   fact, not a uniform theorem.

2. Uniform-limit reading: a half-line closure needs the strict inequality
   uniformly as `beta -> infinity`. The shrinking margin means this is NOT
   supplied by the leading-order comparison; it requires the exact leading
   `c_J`, `c_D` and, if they coincide, the subleading sign.

## Anti-Fabrication

`c_J`, `c_D` are computed from `numpy.linalg.eigh` of the finite half-slice
operator (witnessed spectral quantities); the runner contains no
`curve_fit`/`polyfit`/`lstsq`, no target value, and no closure constant. No
`c_D/c_J` limit is asserted as proven — the runner reports the witnessed trend
only. The extrapolated near-1 limit is an OBSERVATION about the trend, never a
proof input.

## Falsifiers

- Wrong `J` normalization (not the six-neighbor average `/6`) rescales `Delta_J`
  relative to `Delta_D` and changes the comparison.
- Wrong diagonal-derivative `r'` (not the exact character-recurrence form)
  changes `c_D` visibly.

## Honest Outcome

`c_D <= c_J` holds on the tested range (margin positive, monotone decrease
supported), but the margin shrinks toward 0 with `c_J`, `c_D` near-equal, so
H_spec as a uniform strict domination is NOT established. The next path this
opens: the exact leading `c_J`, `c_D` from the reduced-A2 operator's closed-form
spectrum, and the subleading sign if they coincide. The half-line gap theorem's
Route A therefore remains open at this sharpened step; it is not closed by this
note.

## Differentiation From Prior Notes

W86 derived the split and witnessed `c_D/c_J -> 0.958` at finite `beta`, leaving
`c_D <= c_J` open. This note adds the `beta`-extrapolation showing the margin
SHRINKS (the 0.958 was not the limit; `c_D/c_J` climbs toward 1), revising the
expected margin and relocating the obstruction to the exact leading coefficients
and the subleading sign.

## Verification

```bash
python3 scripts/native_gauge_transfer_reduced_a2_spectral_domination_rung_eleven_bounded_2026_06_12.py
```

Expected final line: `TOTAL: PASS=8, FAIL=0`.

Scope: native discrete surface only. No continuum limit, no R^4, no
infinite-volume Yang-Mills mass-gap theorem, no physical `beta = 6`
environment/Perron claim.
