# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Focused check: conditional bulk-host / confined-string Airy resonance

This checks the supplied effective model, not a native bulk spectral theorem. No repository files changed.

## Normalization and host resolvent

With d=(|ex>+|-ex>-|ey>-|-ey>)/2, its norm is one and its Fourier transform is cos x-cos y. Relative hopping -2 has dispersion -4(cos x+cos y). Thus the stated normalized torus average is exactly <d|(E-Hhost+i0)^-1|d>. A coupling -2 to the string endpoint gives Sigma=4Gd. The d-wave subspace makes deletion of the origin immaterial.

For c=cos x, z=E+4c, integration in y gives

(c+z/4)^2 / [sqrt(z-4)sqrt(z+4)] - c/2-z/16.

The x average of its polynomial remainder is -E/16. The two principal square roots, taken from Im z>0, give the correct retarded sign, including negative real denominator for z<-4. Independent split real-integral and on-shell-density evaluation at E=-4 gives

G=-0.2817722049864826-0.08706810029136058 i,
a=-0.9765497711067398-0.7885999750440936 i.

These agree with the supplied values. E=-4 is inside the host band, away from its band edges and van Hove energy, so this boundary value is locally regular enough for the stated leading expansion. A resonance requires continuation of the retarded function onto the outgoing sheet; simply evaluating a physical-sheet resolvent below the real axis would give the wrong boundary prescription.

## Boundary and Airy expansion

For n>=1, E psi_1=-2 psi_2+2f psi_1+Sigma psi_1. Introduce the ghost value psi_0=-Sigma psi_1/2. At the unconfined band bottom E=-4 the linear zero-energy solution is psi_n proportional to n-a. Consequently a=Sigma/(2+Sigma), and b=1-a is the endpoint distance from the extrapolated zero. There is no sign reversal in the proposed a.

The continuum endpoint equation is -2 psi''+f(n+1)psi=(E+4)psi, with extrapolated zero n=a. For a fixed Airy index and f tending to zero,

E_k=-4+2^(1/3) f^(2/3)|a_Airy,k|+f(1+a)+o(f).

This assumes 2+Sigma(-4) nonzero. Lattice dispersion first changes the real expansion at order f^(4/3); finite-energy boundary and smooth self-energy corrections are also subleading to f. These are outgoing resonances of the coupled continuum problem, not normalizable exact bound states. Freezing Sigma at -4 supplies a useful asymptotic control, not an exact energy-dependent Feshbach solution.

For Jperp=lambda Jz and f=lambda^3/16, the full width convention Ephysical=Ereal-i Gamma/2 yields

Gamma=-2 lambda Jz f Im a = 0.0985749968805117 Jz lambda^4 + o(lambda^4).

The spatial scale is (2/f)^(1/3)=32^(1/3)/lambda. The leading Airy spacing in physical energy is order Jz lambda^3. Half-width is Gamma/2, not Gamma.

## Added frozen-boundary residue control

The new script also computes a complex-symmetric pole residue. Normalized Airy endpoint amplitude satisfies psi_1^2/(psi^T psi) ~ b^2 f/2, with analytic rather than absolute-square normalization. Thus the supplied expression 8 lambda^2 G^2 psi_1^2/(psi^T psi) indeed tends to lambda^5 G^2 b^2/4. Its coefficient here is approximately 0.02073497092557+0.09626339064051 i. This complex resonance residue is not a positive spectral weight or a probability. Identifying a measured line area requires the full real-frequency response and continuum background, with the original source dressing justified separately.

## Native-theory boundary

The uniform strong-Z reference, zero-flux transverse host, matching finite column intervals and source-connected first-order channel remain premises of this calculation. Non-nearest-column long intervals form additional states in the same unperturbed energy band; they are frozen at first order, not absent. Higher-order native terms can mix them.

In units Jperp, omitted K2 and K3 terms have orders lambda and lambda^2, while the confinement parameter is order lambda^3. Physical corrections can therefore be larger than the Airy spacing or the proposed width. Common mass shifts may be removed, but momentum-dependent terms, modified endpoint vertices, dark-channel mixing, and competing diagonal string tensions require explicit calculation. A uniform expansion on intervals of length order 1/lambda must also be established: fixed-length coefficient checks do not automatically control this scaling regime. These omissions do not refute the conditional model calculation, but prevent promotion of its width, growing size, residue, or resonance existence to a native bulk result.
