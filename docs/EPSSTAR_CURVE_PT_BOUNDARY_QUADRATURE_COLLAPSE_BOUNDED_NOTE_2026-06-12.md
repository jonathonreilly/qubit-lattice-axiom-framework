# PT Boundary eps*(T) Curve: Mean Quadrature Collapse Persists on the Fixed Grid

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit audit-owned registry,
ledger, queue, or publication-status surfaces.
**Primary runner:** [scripts/frontier_epsstar_curve_pt_boundary_2026_06_12.py](../scripts/frontier_epsstar_curve_pt_boundary_2026_06_12.py)
**Runner cache:** [logs/runner-cache/frontier_epsstar_curve_pt_boundary_2026_06_12.txt](../logs/runner-cache/frontier_epsstar_curve_pt_boundary_2026_06_12.txt)

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane owns status.

## Claim

On the fixed one-particle two-band Harper/PT surface, the full PT boundary root
`mu*_PT(m,T)` has a per-temperature mean quadrature-collapse description, with
bounded spread and a disclosed systematic residual, not an exact relation:

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

The better sampled characterization is `eps*(T)^2 = c + d*T^2`, with residual
below the `2e-3` gate (frozen post hoc, after the `GL=20` calibration run).
This is a regression description of the extracted curve, not a derivation of a
continuum law.

## Scope

This is a finite-cell, sampled-grid bounded theorem on the fixed two-band
Harper/PT surface, with `Q=24`, `Ly=2`, `N=48`, `GL=20`, bracket `[1.2, 2.4]`,
the listed masses, and the listed temperatures. It does not claim exact
`m`-independence, a closed-form `eps*(T)` law, continuum behavior,
finite-lattice scaling, a physical measurement/readout derivation, or a
selector for any empirical value. It introduces no new axiom, primitive,
measure, weighting, normalization, probability rule, or value of `r`.

## Dependencies

- [`LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md`](LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the finite two-band Harper/PT response machinery used by the full
  PT boundary root calculation.
- [`D2_SIGN_BOUNDARY_MASS_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-06-12.md`](D2_SIGN_BOUNDARY_MASS_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the bounded mass-collapse comparison surface and the landed
  finite-flux root anchor reproduced here.

The audit lane grades.
