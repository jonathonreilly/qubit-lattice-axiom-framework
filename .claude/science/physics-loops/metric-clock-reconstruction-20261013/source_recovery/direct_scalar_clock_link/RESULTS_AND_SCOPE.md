# Scalar clock channel: executed controls and limits

Direct parent execution began2026-10-13T01:00:00.757296Z, ended two seconds
later, exit0 with empty stderr. `evidence_v1/FREEZE.json` binds all three
authored sources before execution; exact copies are preserved under
`evidence_v1/source_snapshot`. No source changed during the run.

All49 frozen time/separation geometries pass for both Ramsey and echo:
98 direct radial/angular field integrals agree with the independently
derived closed expressions. Maximum absolute error in chi/kappa is
4.72511e-13; maximum fractional error for nonzero channels is4.58944e-14.
The zero-separation source cancels exactly. Six quadrature refinements change
nonzero results by at most5.07254e-14 fractionally. The omitted radial tail
has the analytic common bound900 exp(-144), not merely an adaptive estimate.

Seven single-reference integrals, seven static Gaussian source potentials,
seven separation plateaus and their fixed-distance late-time approaches
also pass. Plateau checks at dimensionless times100,300,1000 are finite
diagnostics; the all-time result follows from the integrability proof.

Thirty-two finite-oscillator controls evolve both branches by matrix
exponentials at two Hilbert-space truncations. Their coherence magnitudes
agree with exp[-g^2 |Y|^2/2] within1.49881e-14 absolute. This checks the
Gaussian exponent's normalization through a different calculation. It does
not prove a full field theory from finite matrices or replace the continuum
canonical-normalization derivation. Highest-level populations are recorded.

## Physical relation recovered

The same scalar coefficient that supplies the static force fraction fixes
the vacuum clock exponent's amplitude:

    kappa=G_N f_scalar hbar Omega^2/(pi c^5).

For a balanced identical pair at separation L with Gaussian width ell,
the angular factor2[1-sinc(omega L/c)] removes shared low-frequency noise.
Consequently the conditional Ramsey and echo exponents approach2 kappa J
and6 kappa J, whereas a supplied unaffected single-clock reference has a
logarithmically growing exponent. These are different physical source and
reference specifications, not competing fits to a clock experiment.

The analytic bounds chi_R<=4 kappa J and chi_E<=16 kappa J hold for every
duration in this specified linear model. In the frozen27-case illustrative
SI grid, inserting f_scalar<=1/2500 from the earlier exposed working
rectangle gives maximum upper bounds3.20064e-57 and1.28026e-56, respectively.
They also bound1-V. The largest values use nu=1e15Hz, ell=1nm, L=1km.
The SI computation uses the analytic E1 bound on J, not a large-separation
asymptotic approximation. These values are conditional diagnostic sizes,
not observed constraints, a confidence level or bounds on all gravitational
decoherence. G_N is the CODATA2022 central value.

## What this does and does not reconstruct

There is no fitted noise amplitude or fitted time exponent. The free-field
action, canonical commutator, supplied vacuum and clock source determine
them together. The vacuum, factorized initial preparation, Gaussian source
shape, scalar-only approximation and abstract logical operations remain
new assumptions. Neither static gravity nor the earlier exposed gamma
rectangle establishes those assumptions. Real atomic form factors, tensor
fluctuations, traps, initial dressing and a causal optical apparatus remain
open. The Gaussian profile defines the whole free-field integral; a cutoff
effective theory would need an explicit remainder bound before inheriting
these exact expressions.

A classical Gaussian field with the same symmetric covariance produces the
same longitudinal visibility. These calculations do not identify quantum
noise. Different bath states can change the noise while preserving the
static susceptibility. No actual clock, interferometer or neutrino likelihood
has been evaluated. Focused independent source checking is still pending.
