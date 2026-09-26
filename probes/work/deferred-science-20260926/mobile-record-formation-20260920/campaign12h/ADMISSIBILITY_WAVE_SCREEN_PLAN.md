# Declared coherent-wave screen with neighbor-dependent formation

2026-09-21, before the large-lattice runs. Exploratory finite-size test of the
primary smooth-profile reaction-current equation; no fluctuation theorem is
used. Simulator `admissibility_wave_sim.py` SHA
05036372dba1644d281d71658c561ba265108dab4d3e87e8c44cfbedfe33c9d7.
Its four complete-2401-state calibration cases used 8192 trajectories each;
largest estimated standardized discrepancies were 3.44,3.10,2.46,3.38, below
the declared5.5 sanity gate. This is not a confidence certificate.

Rates: the existing axis-balanced minimal exchange rule, alpha1 and floor.05;
per-label birth epsilon times the product of six nearest-neighbor weights
W(a,b)=1+j v_a dot v_b, W(a,vacancy)=1. Epsilon=.04/L, with no rate fitting.
Initial independent site law has density .5+.04cos(2pi x/L), six equally
likely occupied labels. The homogeneous initial vector and quadrupoles vanish.
Macroscopic times tau=t/L are 65 equally spaced values from0 through2.5.
Save modes(0,0,0),(1,0,0),(2,0,0),(3,0,0) for all six measured fields.

Run the following fixed order, with two computation threads:

- L16,j0,.5,.9, each128 trajectories, seeds2026092220 through2026092222.
- L32,j0,.5,.9, each128 trajectories, seeds2026092223 through2026092225.
- L48,j0,.5,.9, each96 trajectories, seeds2026092226 through2026092228.

Resource condition: start each L48 case only if UTC is earlier than08:00 on
2026-09-21. If a case is omitted for that reason, record it explicitly. Do not
select or omit a case based on its result. Preserve all raw amplitudes, seeds,
counts, reconstruction errors and timing. Existing older jobs remain running.

The continuum comparison is the full six-species one-dimensional periodic
equation, with currents differentiated from the supplied potential and
reaction B_a=.04 p0(1+j v_a dot g)^6. Compute it before reading large-lattice
results, on64,128,256 Fourier collocation points, reporting convergence of
the four measured modes, minimum probability and unresolved high-mode tail.
Do not label a spectral numerical solution a PDE existence proof. Compare
with a linearized time-dependent calculation as a small-amplitude diagnostic,
not as an exact finite-amplitude target.

Primary observations: mean density Fourier coefficient, longitudinal vector
coefficient, zero-mode density, generated quadrupoles and second harmonic.
Normalize raw amplitudes by sqrt(L^3) to obtain spatial-average coefficients.
Use4000 whole-trajectory bootstrap resamples for pointwise95% intervals.
Finite-volume damping, higher-gradient corrections, finite-amplitude effects,
sampling uncertainty and reference discretization are distinct. No fitted
speed, discarded transient, phase claim or empirical physical identification.
