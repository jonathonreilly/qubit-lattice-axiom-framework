# eps* Sommerfeld/T=0 Boundary Check on the m = 0 Axis (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** [scripts/frontier_epsstar_sommerfeld_derivation_2026_06_12.py](../scripts/frontier_epsstar_sommerfeld_derivation_2026_06_12.py)
**Runner cache:** [logs/runner-cache/frontier_epsstar_sommerfeld_derivation_2026_06_12.txt](../logs/runner-cache/frontier_epsstar_sommerfeld_derivation_2026_06_12.txt)
**Status authority:** independent audit lane only. This source note does not set,
predict, or change the audit status of any claim or dependency.

## Dependencies

- [EPSSTAR_CURVE_PT_BOUNDARY_QUADRATURE_COLLAPSE_BOUNDED_NOTE_2026-06-12.md](EPSSTAR_CURVE_PT_BOUNDARY_QUADRATURE_COLLAPSE_BOUNDED_NOTE_2026-06-12.md)
  supplies the bounded sampled `(m,T)` PT boundary surface and the wave-10
  `eps*(T)^2` regression characterization.
- [LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md](LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the finite two-band Harper/PT response machinery mirrored here.
- [D2_SIGN_BOUNDARY_MASS_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-06-12.md](D2_SIGN_BOUNDARY_MASS_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the finite-flux sign-boundary anchor used as provenance control.

## Claim Tested

This runner tests whether the landed `eps*(T)` regression can be upgraded to a
native m = 0 derivation from the full two-band Peierls/PT response. The answer is
bounded and partly negative:

- The fixed T = 0 Fermi-surface branch is close to the low-T root extrapolation.
- The naive Sommerfeld coefficient computed from the same T = 0 surface object
  does **not** match the computed finite-T `mu*_PT(0,T)^2` slope.
- The wave-10 `eps*(T)^2 = c + d T^2` slope is also not consistent with that
  fixed analytic coefficient.

The full `(m,T)` surface remains the bounded result in
[EPSSTAR_CURVE_PT_BOUNDARY_QUADRATURE_COLLAPSE_BOUNDED_NOTE_2026-06-12.md](EPSSTAR_CURVE_PT_BOUNDARY_QUADRATURE_COLLAPSE_BOUNDED_NOTE_2026-06-12.md);
this note only addresses the m = 0 axis and the finite-T coefficient attempt.

## Discretization

The PT surface mirrors the landed two-band Harper cell:

- `Q = 24`, `Ly = 2`, `N = 48`, hopping `t = 1`;
- Gauss-Legendre grid `GL = 20` for the PT roots;
- fixed bisection bracket `[1.2, 2.4]`;
- one-particle matrices only.

For the T = 0 object the runner rewrites the PT response as

`R(mu,T) = sum f(E) A(E) + sum f''(E) |H1_nn|^2`,

where

`A_n = 2(H2)_nn + 2 sum_{m != n} |(H1)_nm|^2 / (E_n - E_m)`.

The fixed T = 0 branch uses sharp occupation for the bulk term and a fixed
Gaussian Fermi-surface delta with `eta = 0.05` for the surface term:

`R0(mu) = sum_{E < mu} A(E) - <|H1_nn|^2>_{FS, eta}`.

This is a finite-grid, regularized Fermi-surface quadrature, not a continuum
surface-integral theorem.

## Anchors

The anchor gates run first:

- landed finite-flux root at `m = 0`, `T = 0.2`: `1.699119804762`, within
  `1.5e-2` of frozen `1.7086`;
- PT root at `m = 0`, `T = 0.2`: `1.631150561591`;
- interband term at that PT root: `-0.888793614915`, gated nonzero;
- landed `eps*(0.2)`: `1.624656494801`, within `1e-3` of frozen `1.6247`.

## Results

D1 passes as a bounded branch comparison. The fixed T = 0 branch on
`[1.48, 1.56]` gives

`mu0_surface = 1.515550712171`.

The quadratic-in-`T^2` extrapolation from `T = {0.1, 0.15, 0.2}` gives

`mu(T -> 0) = 1.521712784578`,

with difference `0.006162072408`, below the frozen `1.5e-2` tolerance.

D2 is negative. The computed fit over `T = {0.1, 0.15, 0.2, 0.25}` gives

`mu*_PT(0,T)^2 = 2.487775722248 + 3.877078419951 T^2`

with max relative residual `1.737e-2`. The fixed Sommerfeld calculation from the
same T = 0 object gives

`alpha_analytic = -9.266358431847`.

The sign is opposite and the relative mismatch is `3.390`, so the runner gates
the mismatch as the finding.

D3 is also negative. Recomputing the wave-10 grid gives

`eps*(T)^2 = 2.555130272657 + 2.098439570228 T^2`

with max relative residual `9.592e-4`. Its mismatch with the same fixed
`alpha_analytic` is `5.416`. The m-grid mean slope also differs from the m = 0
slope by `0.459` relative, consistent with the already disclosed m-trend
pollution rather than a clean shared coefficient.

## No-Go Discipline Gate

Scoped negative claim: the fixed-kernel, occupation-smearing Sommerfeld
coefficient tested here does not explain the finite-T boundary slope. This does
not rule out a derivation that keeps the response kernel's explicit
T-dependence.

**N1 alternative routes.**

| Route | Marker | Result |
|---|---|---|
| T = 0 branch route | ATTEMPTED | Locates the m = 0 boundary branch within tolerance, but supplies only the endpoint, not the T^2 coefficient. |
| Fixed-kernel Sommerfeld route | ATTEMPTED | Gives `alpha_analytic = -9.266358431847`, opposite in sign to the computed m = 0 slope. |
| Wave-10 shared-slope route | ATTEMPTED | The sampled `eps*(T)^2` slope is also inconsistent with the fixed coefficient. |
| m-grid averaging route | ATTEMPTED | The disclosed m-trend makes the mean slope a comparator, not a clean coefficient source for m = 0. |
| Full T-differentiation route | ATTEMPTED AS NEXT ROUTE | It may derive the correct coefficient, but it is not the fixed-kernel occupation-smearing route tested here. |

**N2 wall independence.**

There is one collapsed residual: the fixed T = 0 kernel omits explicit
T-dependence of the response. The m = 0 slope mismatch and wave-10 slope
mismatch are two witnesses of that same residual, not independent walls.

**N3 hidden-wall scan.**

The loaded phrases are "measured", "Sommerfeld", "T = 0", "finite-T", and
"derivation". "Measured" means computed from the finite runner grid here, not
observed data. "Sommerfeld" is restricted to the fixed-kernel occupation
smearing coefficient. No continuum limit, Fock-space construction, or physical
readout rule is promoted.

**N4 residual matching.**

| Witness | Witness residual | Current residual | Match |
|---|---|---|---|
| [EPSSTAR_CURVE_PT_BOUNDARY_QUADRATURE_COLLAPSE_BOUNDED_NOTE_2026-06-12.md](EPSSTAR_CURVE_PT_BOUNDARY_QUADRATURE_COLLAPSE_BOUNDED_NOTE_2026-06-12.md) | sampled finite `(m,T)` PT boundary, with disclosed m-trend | comparator surface for wave-10 slope | yes |
| [LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md](LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md) | finite two-band Harper/PT response machinery | source machinery used by the m = 0 coefficient attempt | yes |
| This runner | fixed-kernel coefficient has opposite sign from computed finite-T slope | same fixed-kernel failure | yes |

**N5 rhetoric audit.**

The negative statement is only about the fixed T = 0 occupation-smearing
coefficient on the finite m = 0 axis. It is not a statement about every
Sommerfeld-style derivation, the full `(m,T)` surface, or a future explicit
T-differentiated response calculation.

**N6 partial-closure path scan.**

The partial closure path is explicit: differentiate the full finite-T response,
including the kernel's T-dependence. That path is named as follow-on work and is
not foreclosed.

**N7 steelman.**

A strong reviewer could argue that the T = 0 branch location and the smooth
low-T root sequence show the right boundary object has been found; the sign
failure may only say the held-fixed kernel is the wrong coordinate choice. This
note accepts that objection and narrows the negative to the fixed-kernel
coefficient.

**N8 cross-cycle echo.**

The parent sampled-surface note already treats `eps*(T)^2 = c + d T^2` as a
regression characterization rather than a derivation. This note preserves that
boundary and identifies the next route instead of turning the sign failure into
a global no-go.

Gate result: PASS for the narrowed coefficient-attempt negative.

## Scope

This note does not promote the regression to a Sommerfeld derivation. It locates
precisely where **the naive occupation-smearing picture** breaks: the T = 0
branch location is compatible with the low-T root extrapolation at the bounded
tolerance (so the T = 0 boundary itself IS natively located), but the fixed
**naive Sommerfeld coefficient** — the leading occupation-smearing correction of
the T = 0 kernel — reproduces neither the m = 0 finite-T slope nor the wave-10
mean slope, and in fact carries the **opposite sign**. The positive finding is
the diagnosis: the T^2 growth of the boundary is not captured by occupation
smearing of the fixed T = 0 kernel; a correct derivation must retain the kernel's
own explicit T-dependence. This is a located failure of one specific (naive)
coefficient, **not** evidence that no derivation exists — the next route (full
T-differentiation of the response) is identified, not foreclosed.

One-particle only. No Fock-space construction, no continuum theorem, and no
claim about the full `(m,T)` surface beyond the landed bounded result.
