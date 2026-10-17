# Necessary spectral diagnostics for a candidate universal conformal scalar

Focused conceptual check for the root author. I could not inspect head `16ae120ee46a1186b5ca81cd7d393396089e77d6` in the primary checkout: `git ls-tree` returned `fatal: not a tree object`. Therefore the following independently checks the proposed physical identification and algebra, **not** that PR's actual 12x12 Hamiltonian or numerical spectra. No repository edits, no no-go claim, no empirical validation.

## Answer

The proposed test is valid as a **necessary local diagnostic conditional on an explicit matter/metric dictionary**:

1. The selected excited-band energy differences are genuine internal excitation energies of the same localized matter system, or differences of identified species' rest energies, rather than unrelated hopping modes or particle-number chemical potentials.
2. The lowest-band long-wavelength dispersion describes translation of that matter system with positive inertial mass.
3. Lattice length, energy/time units, hbar and the reference metric are fixed as the candidate scalar direction changes. In particular these are Einstein-frame reference standards, not matter rods/clocks that themselves track the same conformal factor.
4. The regime is adiabatic and homogeneous enough for a local dispersion relation and the same identified modes/minimum to remain meaningful.

Under universal `g_J=A(zeta)^2 g_E`, point-particle rest masses in those Einstein reference units scale as `m_E=A m_0`. If internal rest-energy differences obey the same universal matter law, `Delta_j=A Delta_j0`. In a nonrelativistic isotropic regime, `E(p)=E_rest+p^2/(2m_E)+...`; hence the curvature with respect to fixed physical momentum is proportional to `1/A`. With fixed lattice length and energy unit, the corresponding dimensionless Bloch curvature has the same logarithmic scaling.

Writing `gamma=d ln A/dzeta`, necessary conditions are therefore

    d ln Delta_j/dzeta = gamma for every identified internal gap j,
    d ln K/dzeta = −gamma.

The convention `E=E0+(K/2)k^2` versus `E=E0+K k^2` changes a fixed factor only, not logarithmic derivatives. Require positive nonzero gaps and positive nonzero K. Passing this first-derivative test at one point is not proof of finite-amplitude universality, an emergent metric, equivalence-principle couplings, environmental matching, or a dynamical scalar. Failing it excludes only the stated identification at that point/direction.

## Why internal-gap identification matters

An excited Bloch band is not automatically an internal matter species. It may encode a different propagation channel, sublattice/orbital displacement, winding sector or mode that is not a bound-state excitation. Assigning every band gap the role of a matter clock would supply the bridge being investigated. The gap subtraction also does not identify absolute gravitational rest energy: adding a parameter-dependent identity to H leaves every gap and curvature unchanged while changing the energy zero assigned to a particle sector. If the identity is physically meaningful relative to a vacuum/number sector, that sector must be included before claiming gravitational mass.

For genuinely distinct relativistic species, universal scaling would constrain each species' rest mass **and its own** low-momentum curvature. Checking only lowest-band K is a weak necessary subset. To interpret excitation gaps of one composite object, the center-of-mass inertia of each internal level can differ by its excitation energy/c^2; a single lowest-band inertial response does not settle that relation.

## Matrix and moving-minimum version

For an anisotropic positive Hessian `K_ab`, fixed-coordinate universal scaling requires

    d K_ab/dzeta = −gamma K_ab,

not merely a matching trace. An anisotropic change cannot be hidden in a scalar A if the reference metric is fixed. Coordinate rotations can be tracked separately; eigenvalue ratios are a convenient basis-independent first check, while the full physical spatial frame needs an explicit convention.

If `k0(zeta)` moves, compare gaps and curvature at the tracked minimum, using total derivatives. For `Delta_j=E_j(k0,zeta)−E_0(k0,zeta)`,

    dDelta_j/dzeta = partial_zeta(E_j−E_0)
                     + grad_k(E_j−E_0) dot dk0/dzeta.

Stationarity removes the ground-band gradient but does not automatically remove the excited-band gradient. A symmetry-fixed common stationary point can remove both. Near crossings, use spectral projectors/degenerate perturbation theory and declare which gap is followed; sorting eigenvalues independently at nearby parameters can create false sensitivities. A shift of minimum can also act like an effective vector potential rather than a scalar mass change.

## What is available before fixing absolute standards

Relative-clock ratios give a weaker, operationally cleaner necessary test:

    d ln(Delta_j/Delta_l)/dzeta = 0.

This is invariant under a common change of energy/time normalization. It tests equal response of candidate internal clocks, not their absolute scalar response. If all ratios remain constant, a common gamma can still be zero or merely a unit choice; a nonzero observable scalar coupling needs a separately defined comparison channel.

Likewise ratios of positive curvature eigenvalues or ratios of curvatures for different identified modes can test non-universal anisotropic/species responses without an absolute length/time scale. Under a fixed unit dictionary, `Delta_j K` must be stationary for the proposed gap–inertia condition. This product is **not** invariant under arbitrary independent changes of length and time standards.

## Explicit changing-unit dictionary

Let the Hamiltonian eigenvalues be dimensionless, with physical energy `E=E_unit epsilon`, dimensionless Bloch momentum k, physical momentum `p=hbar k/a`. Then

    Delta_phys = E_unit Delta,
    K_phys = E_unit a^2 K / hbar^2.

Write `e=d ln E_unit/dzeta`, `l=d ln a/dzeta`, `g_j=d ln Delta_j/dzeta`, `kappa=d ln K/dzeta`, and hold hbar fixed. Universal conformal scaling now requires

    e+g_j=gamma,
    e+2l+kappa=−gamma,
    hence g_j+kappa+2e+2l=0.

If `E_unit=hbar/T`, this last condition is

    g_j+kappa+2 d ln a/dzeta−2 d ln T/dzeta=0.

Thus a changing lattice spacing or clock normalization can alter the apparent opposite-slope test. They cannot be adjusted after inspecting the spectrum and then counted as derived. If the spacing and time unit change proportionally, their ratio is fixed and these extra terms cancel, but the common physical gamma still differs from the raw dimensionless gap slope. An independently derived emergent propagation speed or relational rod/clock dictionary could constrain these conversions; simply declaring them is another supplier.

## Suggested precise local computation

For microscopic parameters theta=(t1,t2,lambda), compute gradients at a registered regular point and tracked minimum. Seek a nonzero parameter tangent v satisfying

    [grad ln Delta_j − grad ln Delta_ref] dot v = 0,
    [grad ln K + grad ln Delta_ref] dot v = 0

under fixed standards, with `gamma=grad ln Delta_ref dot v`. For a matrix Hessian use enough component/eigenvalue-shape constraints rather than a trace alone. Separate:
- nonzero solutions with gamma != 0;
- directions with gamma=0, which are spectrally silent at first order;
- rank loss/degeneracies where the chosen logs are invalid.

A tangent solution can be an accidental first-order coincidence. Check second-order residuals or integrate a finite path with the constraints before claiming a robust scalar direction. A nullspace in this small Hamiltonian also does not provide scalar dynamics, a healthy kinetic term, universal coupling to other sectors, or the environmental boundary map. It is a concrete candidate to investigate, not a completed physical identification.
