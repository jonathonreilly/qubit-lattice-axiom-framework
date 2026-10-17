# Independent tensor-propagation and reconstruction addendum

This is a conditional derivation and supplier analysis, not an empirical measurement or proof that sirens identify the cosmological scalar background.

## Propagation sign from the action

Let a=a_J, A=e^zeta, Mstar=M/A and B=a Mstar=M a_E. The quadratic tensor action in the question gives

h_etaeta + 2(B_eta/B) h_eta - Laplacian(h)=0.

With v=B h, Fourier modes obey the exact equation

v_etaeta + [k^2-B_etaeta/B]v=0.

In the geometric-optics regime k^2 much larger than |B_etaeta/B|, slowly varying envelopes satisfy h proportional to 1/(B r) for an outgoing spherical wave. Comparing propagation with the same emitted physical strain and the corresponding electromagnetic geometric spreading gives

h_obs/h_GR = Mstar_emit/Mstar_obs,

so the propagation-only distance ratio is

dL_GW/dL_EM = Mstar_obs/Mstar_emit = A_emit/A_obs.

The inverse ratio would be the wrong sign. Here 'same emitted strain' is essential: the transport equation does not predict a binary's intrinsic waveform amplitude.

For the background twins with A_obs=1, a_obs=1 and a(tau)=tau^2,

tau_emit=(1+z)^(-1/2), and dL_GW/dL_EM=(1+z)^(-s/2).

Their common tau interval maps to 0<=z<=3. At z=3 the ratios are 1/sqrt(2) for s=1/2 and 2^(-1/4) for s=1/4.

## What would be reconstructed if the propagation ratio genuinely supplied A/A0?

Write primes for d/dtau. Measured smooth background functions H_J(z), A(z)/A0 and a matter density rho_J(z), plus the normalization combination A0^2/M^2, give

D_tau=-(1+z) H_J d/dz,
q=zeta'=-(1+z) H_J d_z ln A,
ell=H_J-q,
R=A^2 rho_J/M^2.

Within the specified spatially flat Einstein-gravity, one-scalar, conformally coupled dust class, Raychaudhuri gives

F=Q_Y/M^2=[-2(ell'+q ell)-R]/q^2,
G=F q.

This is background reconstruction from the gravity equations, not an assumed scalar trajectory solving a separately selected potential. It requires q nonzero and sufficient regularity. Zeros of q leave only the product F q^2 determined by this equation.

Friedmann additionally determines Q along the background curve:

Q/(M^2 A^2)=F q^2-3ell^2+R.

The scalar equation, equivalently the consistency relation with Einstein equations and conformal dust conservation on regular patches, gives

E=Q_zeta/(M^2 A^2)=(Fq)'+(3H_J-2q)Fq+R.

For the narrower linear kinetic class Q=M^2 F(zeta)Y-V(zeta),

V/(M^2 A^2)=3ell^2-R-Fq^2/2.

A monotonic zeta maps these along-curve functions to F(zeta),V(zeta) on the explored range. It does not specify their extension beyond that range. For general Q(zeta,Y), the data still do not determine off-curve derivatives such as Q_YY; declaring U=0 would adopt the linear kinetic subclass, not derive it. The script independently reconstructs both original twins from their proposed H_J and propagation ratios, including E checked by direct Q_zeta differentiation.

The derivatives required are substantial: q uses a first derivative of ln A; F uses its second derivative and a first derivative of H_J; E uses further derivatives. A finite noisy catalogue does not directly supply these continuous derivatives. Smoothing, interpolation, sampling coverage and derivative error bounds remain suppliers.

## Observation contract that cannot be omitted

1. The tensor action must be the stated two-derivative luminal, effectively massless one, without extra tensor conversion, dispersion, absorption or appreciable beyond-geometric-optics effects. Finite-wavelength corrections are not zero merely because the leading transport formula is simple.
2. The emission waveform amplitude must be independently calibrated or jointly inferred under a specified source-generation model. A GR waveform-distance posterior cannot automatically be reinterpreted as a pure propagation observable in scalar gravity. Scalar charge/radiation, altered binding dynamics, a different source gravitational coupling, binary masses, inclination and detector response can change inferred amplitudes.
3. The electromagnetic distance and source redshift require their own luminosity/geometry/clock calibration. Opacity, lensing magnification, peculiar motion, selection effects and host associations must be controlled. Inferring dL_EM from a chosen scalar cosmology would circularly supply the desired background.
4. The actual amplitude endpoint factors concern the local source and detector scalar environments. To identify them with the cosmological A(z) and A0 requires an environmental matching result or independent measurements. Screened endpoint regions can erase the cosmological Planck-mass-running signature even when the homogeneous propagation calculation contains it. Unknown source/detector transitions must not be set to unity by declaration.
5. R needs the normalization A0^2/M^2 and a genuine rho_J supplier. A locally measured Newton constant includes scalar-force/environment effects in this model class; it is not automatically the inverse tensor Planck coefficient. Choosing A0=1 is a convention, not an independent measurement of M in matter units.

Thus tensor amplitudes offer a concrete extra channel that conditionally breaks the two-background example, but the source/environment/calibration identification remains a real obstacle. They do not by themselves solve perturbation reception-time coverage or reconstruct a general action off the homogeneous trajectory.

## Primary-source scope

The sign and reconstruction above are derived independently. For the environmental caveat I checked the primary abstracts of Dalang and Lombriser, *Limitations on Standard Sirens tests of gravity from screening*, https://arxiv.org/abs/1906.12333, and Dalang, Fleury and Lombriser, *Horndeski gravity and standard sirens*, https://arxiv.org/abs/1912.06117. The latter explicitly places observable deviations at the local effective-Planck-mass values at emission and reception. These sources are prior-art boundaries, not a novelty claim or a substituted proof of the full source-generation problem.

## Artifacts

`tensor_check.py` checks the exact v=B h transformation, reconstructs q,F,V,E for both twins, checks their z=3 ratios and detects the inverse-sign error. `tensor_result.json` records exact symbolic outputs. No repository files were modified.
