---
claim_id: ring_model_three_spectral_moments_bound_the_spread_of_the_transverse_weight_and_on_8_cubed_keep_at_least_84_percent_of_it_within_a_factor_two_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Exact inequalities for any positive finite measure mu on (0, inf) with moments m_j = int omega^j dmu, j = -1, 0, 1; R = m0/sqrt(m1 m_-1), omega_g = sqrt(m1/m_-1), p = mu/m0. (I) E_p[omega/omega_g] = E_p[omega_g/omega] = 1/R. (T1) p(omega outside [omega_g/lam, lam omega_g]) <= 2(1 - R)/(R(lam + 1/lam - 2)) for lam > 1, attained (as a supremum) by three-atom measures. (H) If mu has no weight in omega_g (1 - d, 1 + d), 0 < d < 1, then R <= 1 - d^2/2, with equality for two atoms. (G) If mu splits into parts with m0 fractions 1 - eps and eps whose frequency ratios all lie outside (1/r, r), then R^-2 - 1 >= eps(1 - eps)(r + 1/r - 2), with equality for two atoms. Rational-arithmetic checks of the identities and extremal measures and randomized validity checks. Applied to the landed ring-component moments (m1 = 2 u s^2, m_-1 = chi/2, m0 = S) on 8^3 at k = pi/4 with the landed estimates S = 0.4084 +- 0.0144 and sqrt(m1 m_-1) = 0.4243 (R = 0.963; 0.929 one standard error lower), as estimated statements: at least 84 percent of the transverse structure factor's weight lies within a factor two of omega_g = 1.042 s and at least 94 percent within a factor three (69 and 88 percent at R = 0.929); a minority mode at three times or a third of omega_g carries at most 6.4 percent (13.9 percent); but no window narrower than about plus or minus 27 percent of omega_g is guaranteed to hold any weight. So the moments bound the spread of the weight without locating a single mode. No certified moments, single-mode statement, frequency or physical reading."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_on_8_cubed_the_forward_walking_structure_factor_falls_with_the_population_to_within_the_moment_bound_bounded_theorem_note_2026-09-28
runner: scripts/ring_model_three_spectral_moments_bound_the_spread_of_the_transverse_weight_2026_10_01.py
---

# Three spectral moments bound the spread of the transverse weight, and on 8³ keep at least 84 percent of it within a factor two

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact inequalities with an estimated application; unaudited.

## Supplied setting

**Moments.** The landed ring-component note
`RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md`
defines the transverse spectral measure `μ` (weights `a_n` at excitation
energies `ω_n > 0`) and its moments `m₁ = 2us²`, `m₋₁ = χ/2` and `m₀ = S`. By
Cauchy–Schwarz, `R = m₀/√(m₁m₋₁) ≤ 1`, with equality exactly for a single
frequency.

**What prompted this block.** The landed note
`RING_MODEL_ON_8_CUBED_THE_FORWARD_WALKING_STRUCTURE_FACTOR_FALLS_WITH_THE_POPULATION_TO_WITHIN_THE_MOMENT_BOUND_BOUNDED_THEOREM_NOTE_2026-09-28.md`
estimated `R = 0.963 ± 0.034` on 8³ at `k = π/4`. Its review noted that
near-equality alone does not show spectral concentration. This block states
exactly what three moments do imply.

## Theorems

Write `ω_g = √(m₁/m₋₁)`, `x = ω/ω_g` and `p = μ/m₀`.

- **(I) Identity.** `E_p[x] = E_p[1/x] = 1/R`, so `E_p[cosh ln x − 1] = 1/R − 1`.
- **(T1) Ratio window.** For `λ > 1`,
  `p(ω ∉ [ω_g/λ, λω_g]) ≤ 2(1 − R)/(R(λ + 1/λ − 2))`.
  - *Proof:* `cosh ln x − 1 ≥ cosh ln λ − 1` outside the window; apply
    Markov's inequality with (I).
  - *Sharpness:* the three-atom measure on `{1/λ, 1, λ}·ω_g`, with weights
    `(q/2, 1 − q, q/2)` and `q = (1/R − 1)/(cosh ln λ − 1)`, attains the
    bound whenever `q ≤ 1`.
- **(H) Hole.** If `μ` has no weight in `ω_g(1 − d, 1 + d)`, with
  `0 < d < 1`, then `R ≤ 1 − d²/2`.
  - *Proof:* `(x − 1 + d)(x − 1 − d)/x ≥ 0` on the support, and its
    `p`-mean is `(2 − d²)/R − 2`.
  - *Equality:* two atoms at `ω_g(1 ∓ d)`.
- **(G) Gap.** Suppose `μ` splits into two parts with `m₀` fractions `1 − ε`
  and `ε`, and every frequency ratio across the parts lies outside
  `(1/r, r)`. Then `R⁻² − 1 ≥ ε(1 − ε)(r + 1/r − 2)`.
  - *Proof:* Cauchy–Schwarz within each part, and `t + 1/t ≥ r + 1/r` across
    them.
  - *Equality:* two atoms.

The runner checks these as follows:
- (I) and the extremal measures in exact rational arithmetic;
- validity of (T1), (H) and (G) on about 110,000 random positive measures,
  with no violation.

## Application to 8³ at k = π/4 (estimated)

The inputs are the landed `S = 0.4084 ± 0.0144` and `√(m₁m₋₁) = 0.4243`, so
`R = 0.963`. The value one standard error lower is 0.929. Also
`ω_g = √(m₁/m₋₁) = 1.042 s`, with `s = 2 sin(π/8)`.

| statement about the S weight | R = 0.963 | R = 0.929 |
|---|---|---|
| outside a factor 1.5 of `ω_g`, at most | `0.467` | `0.923` |
| outside a factor 2, at most | `0.156` | `0.308` |
| outside a factor 3, at most | `0.058` | `0.115` |
| minority mode at frequency ratio 2 / 3 / 10, at most | `0.198 / 0.064 / 0.0099` | `0.500 / 0.139 / 0.020` |
| empty window about `ω_g` still allowed, half-width | `0.274` | `0.378` |

What follows:
- **The weight is confined to a factor of a few.** At least 84 percent of the
  transverse weight lies within a factor two of `ω_g`, and at least 94
  percent within a factor three. A separate mode at three times or a third
  of `ω_g` carries at most 6.4 percent.
- **No single mode is located.** Spectra with no weight within ±27 percent of
  `ω_g` are compatible with `R = 0.963`, so the moments do not show that a
  mode sits at `ω_g`. Locating one would need `R` closer to one: for example
  `R ≥ 0.99154` puts 80 percent of the weight within ±30 percent. Or it would
  need an extra moment or spectral information.

## Boundary

- The inequalities are exact for any positive measure.
- The application inherits the Monte Carlo errors of `S`, `u` and `χ`; just
  the error of `S` is propagated. The bounds are monotone in `R`, so the
  lower value is the conservative one, but one standard error is not a
  confidence bound.

## Evidence limits and No-Go Discipline Gate

- **N1:** positive measures on `(0, ∞)`; the landed ring-component moments on 8³ at `k = π/4`.
- **N2:** no phase or no-go wall is imported.
- **N3:** the ring component, its sector and the estimators remain supplied.
- **N4:** the landed moment identities and estimates are used as stated there.
- **N5:** exact inequalities; estimated application.
- **N6:** locating a single mode, and larger tori, remain open.
- **N7:** extra moments, spectral bounds and other estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_three_spectral_moments_bound_the_spread_of_the_transverse_weight_2026_10_01.py
```

Five checks; prints `TOTAL: PASS=5 FAIL=0` in a few seconds.
