# Direct analytic completion: first execution and proof scope

The parent-authored three-field action has an exact ideal dust/radiation
trajectory and a global future vacuum convergence proof within its flat,
homogeneous Einstein-expanding positive-fluid model. The full handwritten
argument was independently checked; the parent read that report and its
derivation and verified all34 source/evidence identities. The two original
wording findings and failed reviewer checks are preserved. V2 explicitly
includes the critical nu=9/4 mode and distinguishes Einstein expansion from
physical-frame expansion.

The first parent execution ran from05:04:06.676470 to05:04:44.475143UTC
on2026-10-13, exit0:1492 internal checks passed,0 failed. All7 frozen inputs
were unchanged. The raw output and source snapshot are in evidence_v1.
An independent implementation/numerical check is pending; the proof review
did not inspect this code and does not supply that separate coverage.

## What was actually computed

- Exact symbolic metric differentiation checked all27 connection components,
  all three scalar equations on the constructed history, Friedmann,
  Raychaudhuri, the off-trajectory energy exchange, the coercive square and
  canonical vacuum masses.
- At72 arbitrary finite states, the implemented N-coordinate force was
  compared with an independently written proper-time momentum formulation.
  Complex-step derivatives checked the actual potential and metric functions.
  The largest full-force discrepancy was3.52e-6 of its declared tolerance;
  the energy-identity discrepancy was1.60e-6 of tolerance. These fixtures
  include zero densities, signed fields and large fields.
- 24 integrations covered redshift1e6 through future N=6: three couplings,
  four nu values including9/4, and two declared refinements. The maximum
  full-state error was0.001441 of tolerance; the maximum refinement
  discrepancy was0.001749. The actual constraint-derived H squared, checked
  at288 time samples, agreed with the supplied expansion to2.51e-6 of
  tolerance. Numerical tracking coordinates are an invertible time-dependent
  rescaling; they do not enforce the background equations or p values.
- 48 disturbed histories were integrated separately with DOP853 in N and
  RK45 in proper time using scaled momenta. Their maximum difference was
  0.000229 of the declared tolerance. All sampled energies decreased within
  tolerance and stayed above the vacuum value1.5 in H_v=1 units. At N=12,
  final energies ranged from1.5 to1.5000343063. Finite-time convergence
  examples support implementation checks; they are not the global proof.
- 25 free-mode values were compared with independent matrix exponentials,
  including the repeated-root limit. No density-forced mode was mislabeled
  as a free mode.

The total is a count of internal assertions, not independent experiments,
independent observations, or proofs of1492 separate physical claims.

## Constructed versus observed

The chosen trajectory exactly realizes the exposed benchmark
H^2/H0^2=m exp(-3N)+Omega_gamma exp(-4N)+1-m-Omega_gamma.
Here m=.3 and H0=70km/s/Mpc are supplied, and the previous photon calibration
gives Omega_gamma=5.046740289227271e-5. The conversion uses the explicitly
imported weak-field convention G_N=(1+a)G_*; local viability of that
identification for the new action remains a separate physical comparison.
The photon temperature is exposed calibration and the posted FIRAS spectrum
is a constructed baseline diagnostic. No new held-out observation is tested.

The metric, extra radiation scalar and nu restoring coefficient are new
candidate assumptions. H_v is supplied by the chosen vacuum fraction; the
field amplitudes are initial conditions fixed from the benchmark. The action
contains no matter or radiation abundance coefficient, but those abundances
have therefore moved into initial data rather than being derived. No photon
microphysics, neutrino content, primordial state or entropy mechanism is
inferred from this construction.

## Mathematical extent

The energy function E=T/2+V+sigma+r=3H^2/2 obeys
E_dot=-3H(T+sigma+4r/3). The exact coercive lower bound confines every finite
initial positive-fluid state to a compact sublevel with positive minimum
kinetic eigenvalue. Smooth continuation and density-boundary invariance give
global future proper-time existence. The only invariant zero-dissipation
state is the unique stationary vacuum, so the full homogeneous state
converges there. Bounded conformal factor also gives physical proper-time
completeness. For unrestricted a>0 physical expansion need not hold at every
intermediate time; H_J nevertheless tends to H_v.

This theorem uses fixed a,nu,H_v>0. It is not uniform at their zero limits.
It addresses homogeneous proper time, not general geodesic completeness,
inhomogeneous spacetime stability or quantum completion. In particular, the
free future y mode exp(-H_v t) decays more slowly than the constructed
exp(-2H_v t) history. The vacuum proof alone therefore supplies no selection
of the observed finite-era trajectory. The new direct_epoch_selection block
examines that dynamical question without assigning an empirical success.
