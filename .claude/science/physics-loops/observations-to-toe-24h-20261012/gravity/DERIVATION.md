# Finite-source gravity and propagation: working derivation

Author status: conditional-support. Intended claim type: bounded_theorem for
the response construction; its observational identification remains open.
This is a research checkpoint, not a published Cassini reanalysis or an audit.

## Target and premises

Determine how one positive conserved-source spectral response maps into three
distinct channels: static acceleration, null travel time and timelike wave
propagation. The model and test exposure are frozen in `BLOCK01_CONTRACT.json`.
The first model-selection computation used code SHA-256
`5fbd1405a54925ea82daff679397bb534f797d9f7140b0214b8bd831f9a58ef6`.

The supplied physics is linear Lorentz-invariant weak-field exchange, a common
metric for light and matter, positive spin-2/spin-0 measures, spherical static
sources and retarded boundary conditions. These are alternative candidate
premises authorized by the user, not consequences of the repository lattice
axioms and not amendments to its premise registry. For the decomposition,
Niedermann and Padilla, arXiv:1706.04778v2, equations (1), (17) and (20) supply
primary context. The kernels below are derived directly. The familiar tensor
coefficients are controls, not discovery claims.

## Exchange convention and source convolution

Set ds²=−(1−2U/c²)c²dt²+(1+2V/c²)dx². For a source mass M, an exterior
radius r and nonnegative measures dW₂(μ), dW₀(μ), write

    U(r)=G* M/r [Z + (4/3)∫Fρ(μ)e^(−μr)dW₂(μ)
                         + 2∫Fρ(μ)e^(−μr)dW₀(μ)],
    V(r)=G* M/r [Z + (2/3)∫Fρ(μ)e^(−μr)dW₂(μ)
                         − 2∫Fρ(μ)e^(−μr)dW₀(μ)].

The zero-mass pole Z≥0 has the massless tensor projector. The μ→0 limit
of the massive tensor measure keeps its different trace coefficient. Scalar
normalization is conventional; a convention with coefficient A₀/3 has
A₀=6W₀. Finite measures with compact support suffice for all interchanges
here; extension needs convergence of each displayed integral.

For radial nonnegative density supported in 0≤s≤R and M=4π∫s²ρ(s)ds,
angular integration of exp(−μ|x−y|)/|x−y| gives, for r≥R,

    Fρ(μ)=(4π/M)∫₀ᴿs²ρ(s) sinh(μs)/(μs) ds.

Thus 1≤Fρ≤sinh(μR)/(μR), with continuous value 1 at μ=0. For a
uniform sphere, F=3[x cosh(x)−sinh(x)]/x³, x=μR. The runner evaluates
e^(−x)F to avoid overflow, and compares it to direct radial quadrature.
The acceleration kernel is

    K_F(μ,r)=Fρ(μ)(1+μr)e^(−μr),
    ∂r K_F=−Fρ(μ) μ²r e^(−μr).

This is a source convolution, not point-source replacement when μR is large.

## Null response and the operational calibration

At first order, one light leg has excess coordinate time

    δT=c^(−3)∫(U+V) dz
      =(2G* M/c³)[Z I₀(b)+∫Fρ(μ)Iμ(b)dW₂(μ)],
    Iμ(b)=∫_(−z_E)^(z_S) exp(−μ√(b²+z²))/√(b²+z²) dz.

The direct scalar contribution cancels. Reception-clock conversion and the
actual moving endpoints must be included in an experimental Doppler fit. The
benchmark fixes z_E,z_S and computes only the impact-parameter derivative

    K_L(μ,b)=−(b/2)∂b Iμ
      =(b²/2)∫exp(−μr)(1+μr)/r³ dz,
    K_L(0,b)=[z_E/√(b²+z_E²)+z_S/√(b²+z_S²)]/2.

The independent checker differentiates Iμ numerically with the transformed
integration endpoints varied consistently. The author instead integrates the
analytic derivative. For infinite endpoints K_L=μb K₁(μb); its zero-mass
limit is 1. Finite endpoints are used in every benchmark number.

Calibrating one circular acceleration at radius r₀ defines

    D=Z+(4/3)∫K_F(μ,r₀)dW₂+2∫K_F(μ,r₀)dW₀,
    G_N M=G* M D,
    1+γ_bench(b)=2[Z+∫Fρ K_L(μ,b)/K_L(0,b)dW₂]/D.

This gamma-like ratio equals the constant PPN gamma only within its specified
response class. It is not the likelihood-compressed Cassini gamma estimator.
In particular the force and light kernels sample different distance ranges.

## A concrete positive single-pole witness

Take Z=0, W₀=0 and one positive massive tensor pole. Fix r₀=z_E=1 AU,
z_S=8.43 AU and b₀=1.6 nominal solar radii. The source form factor cancels
from the ratio for any common spherical density, so a point source and a
finite sphere give the same root. Solving γ_bench(b₀)=1 gives

    μ AU = 0.9615553289785617,
    μ = 6.427600369438692×10^(−12) m^(−1),
    μ^(−1) = 1.5557905633876984×10^11 m.

No GW quantity was used in this selection. These are model-development
numbers for an idealized geometric equality, not an observed mass estimate.
With this same pole, γ_bench at 2,4,8,16 solar radii is approximately
0.9998653270, 0.9988695243, 0.9955498691, 0.9849087474. Relative static
strength at radii 0.387,0.723,1.524 AU is 1.2611879644,1.1279665705,
0.7593940749. These are forward response targets; no planetary fit is made.

For the retarded propagator k²=(ω/c)²−μ², a propagating monochromatic
narrow packet has group speed c√[1−(μc/ω)²]. Its excess delay is

    δt=(D_source/c)[1/√(1−q)−1], q=(μc/ω)².

At 26 Mpc the selected pole gives 139833.1331,12584.9820,1398.3313 and
125.8498 seconds for 30,100,300,1000 Hz. Interpreting one of these as the
observed GW carrier needs a wave-packet/source/detector bridge, and a timing
comparison additionally needs the emission-delay assumption. A luminal pole
can coexist with unobserved delayed modes; timing its arrival does not measure
the total spectral weight in those other modes.

## Verification and next science

The first author execution reports 13 passing numerical checks and zero
failures. It compares sphere quadrature, the Bessel ray limit and root
residuals. A separate mpmath calculation, delivered by the gravity-measurement
worker, reproduces the root, light/force shape and delays by differentiating
the potential and light-time integral; the exact source and results will be
preserved before review. This is an independent mathematical check of the
declared benchmark, not independent empirical validation.

Next: bind primary timing definitions and a conditional timing rule; derive
the multi-impact-parameter positive-measure envelope and its finite-endpoint
remainder. Develop a surviving massless-metric plus positive scalar-continuum
candidate with both causal response and quantum noise fixed by one action.
The latter is a constructive alternative to independently chosen classical
noise, not a claim that the existing event-model counterexamples apply to it.

Open physical obligations: full Cassini design/covariance and ephemerides;
nonlinear consistency of interacting massive spin-2 modes; spectral measure
selection; source radiation and detector coupling; admissible quantum state;
matter/gauge/fermion content and its interactions. This first calculation
establishes no TOE or nonlinear gravity completion.
