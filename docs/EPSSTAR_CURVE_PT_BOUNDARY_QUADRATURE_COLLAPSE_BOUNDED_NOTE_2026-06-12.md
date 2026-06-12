# PT Boundary eps*(T) Curve: Quadrature Collapse Persists on the Fixed Grid (Draft)

**Date:** 2026-06-12
**Script:** `scripts/frontier_epsstar_curve_pt_boundary_2026_06_12.py`
**Status:** draft note. The audit lane grades.

## Claim

On the fixed one-particle two-band Harper/PT surface, the full PT boundary root
`mu*_PT(m,T)` satisfies the same MEAN quadrature collapse within the bounded spread (not an exact relation)

`mu*_PT(m,T)^2 = m^2 + eps*(T)^2`

on `m in {0, 0.2, 0.3, 0.5}` and `T in {0.15, 0.2, 0.3, 0.4}`. The runner extracts
`eps*(T)`, verifies that it is monotone increasing on the sampled temperatures, and
**discloses the systematic residual structure** (the same `m`-trend the landed
finite-difference note disclosed): at every `T` the per-`m` residual signs are
`(+, +, +, -)` and the per-`m` collapse values `mu*^2 - m^2` strictly DECREASE
with `m` — the collapse is a bounded mean description with a coherent `m`-trend
inside the spread, not an exact `m`-independence. It also
reports two regression characterizations. This is not a closed-form derivation.

## Runner Result

The runner mirrors the fetched two-band Harper cell and full PT response, uses fixed
bisection on `[1.2, 2.4]` for 60 steps, and gates against frozen tolerances. The
landed finite-flux mass-collapse anchor is recomputed first: at `m=0`, `T=0.2`, the
positive boundary root is `1.699119804762`, within `2e-2` of the frozen landed
`1.708`. The PT interband term at the `m=0`, `T=0.2` PT root is nonzero
(`|interband| = 0.888793614915`).

Extracted `eps*(T)` at `GL=20`:

| T | eps*(T) | max relative spread over m |
| --- | ---: | ---: |
| 0.15 | 1.612643530678 | 0.012503159991 |
| 0.20 | 1.624656494801 | 0.012977017247 |
| 0.30 | 1.657294308376 | 0.013286828513 |
| 0.40 | 1.699862096939 | 0.015311361354 |

The measured maximum per-temperature collapse spread is `1.5312%`, gated below the
frozen `2%` bound.

## Curve Characterization

Two fixed regression forms are tested as characterizations only:

| form | coefficients | max relative residual |
| --- | --- | ---: |
| `eps*(T) = a + b*T` | `a=1.556668656138`, `b=0.350268386898` | `0.002688034230` |
| `eps*(T)^2 = c + d*T^2` | `c=2.555130272657`, `d=2.098439570228` | `0.000959210359` |

The better sampled characterization is `eps*(T)^2 = c + d*T^2`, with residual below
the `2e-3` gate (frozen post hoc, after the `GL=20` calibration run — stated as such). This is a regression description of the extracted curve, not
a derivation of a continuum law.
