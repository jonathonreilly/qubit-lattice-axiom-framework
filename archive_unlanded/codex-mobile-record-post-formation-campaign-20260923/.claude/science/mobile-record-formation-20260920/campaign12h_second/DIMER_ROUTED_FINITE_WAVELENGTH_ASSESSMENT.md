# What the finite-wavelength winding calculation explains

2026-09-21. Root exploratory assessment. This comparison was specified after
the original mode-averaged N<=128 results, before inspecting their by-axis
aggregates or any N256 observable. No parameter was fitted. The original
protocol, results and uncertainty calculation remain unchanged.

The exact initial generator projection predicts stronger damping along the
winding direction than across it. Its small-wavevector diffusion coefficient
is 4k0 parallel to the winding and k0 along either transverse coordinate.
This is a property of the fixed matching and the supplied microscopic rates.
It helps account for the large deviations from an undamped Euler propagator
at the simulated volumes.

For the actual gamma=1 dynamics, exponentiating that projection is a
benchmark approximation. A complete exact 14^4-color control on an auxiliary
four-position cycle has a nonzero projection residual with trace 97/196.
The exact second derivative of the covariance is the projected square minus
the positive residual Gram matrix. Thus the exponential is already incorrect
at second order in time on that control. At gamma=0 the linear observable
space closes and the exponential covariance is exact. This positive control
and explicit correction prevent a finite-time closure assumption from being
silently promoted into a theorem.

At quarter period t=7/8, the original three-mode averages on the winding
fixture compare as follows. Values are means; the full comparison preserves
every original per-axis standard error and every original time.

| N | Error: benchmark | Error: observed | Cross: benchmark | Cross: observed | Longitudinal: benchmark | Longitudinal: observed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 1.8753 | 1.8749 | 0.0616 | 0.0754 | 0.0640 | 0.0603 |
| 32 | 1.5866 | 1.6331 | 0.2065 | 0.1803 | 0.2071 | 0.2116 |
| 64 | 1.2012 | 1.2103 | 0.3994 | 0.3949 | 0.3995 | 0.3564 |
| 128 | 0.8056 | 0.7763 | 0.5972 | 0.5455 | 0.5972 | 0.5993 |

The benchmark captures much of the finite damping at this time, but the
agreement is not uniform across observables, axes or times. Some visible
differences remain. No goodness-of-fit statistic, confidence test or fitted
correction exponent was defined. The uncertainty uses independent histories,
with the three modes averaged within each history; the modes are not extra
replicates. The six-panel figure displays all four sizes, all five recorded
times and all three axes for propagation error and signed cross covariance.

The stationary error benchmark uses the exact unchanged equal-time covariance
at both endpoints. It does not treat the dissipative projected propagator as
a deterministic trajectory whose equilibrium variance shrinks. This is why
its mean-square error is 2-Re tr(U^dagger C_proj)/3.

The formula applies only to the translation-invariant winding fixture. No
scalar Fourier symbol or averaged-direction replacement is assigned to the
irregular matching. That case would require a different calculation using
its actual inhomogeneous projected operator.

The result is a mechanistic finite-size diagnostic, alongside the separately
proved conditional Euler theorem. It does not establish a diffusive correction
theorem, a physical photon or an empirical prediction. The calculation and
original aggregate analysis are undergoing a separate selective check; their
completion will be recorded in its sealed packet without rewriting the
original production results.
