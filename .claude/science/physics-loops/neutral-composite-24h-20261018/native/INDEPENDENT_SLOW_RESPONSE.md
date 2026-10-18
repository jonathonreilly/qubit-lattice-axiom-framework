# Focused slow-model propagation and response check

Disposition: PASS within the stated partial slow coefficient model. Original microscopic higher-order closure and pole control remain unproved. No repository edits or formal audit.

## Independent host and transverse check

I independently integrated the infinite nearest-neighbor lattice Green matrix at E=-2+i*1e-6 by analytically integrating one momentum and numerically integrating the other on the real contour. I removed the five-site cross with the finite-rank Schur formula, then projected normalized axial A, diagonal D, and axial-difference B vectors. This avoids the root's moving branch-point contour implementation. The A/D matrix agrees with the supplied real-axis values at the expected finite-regulator accuracy.

The boundary scattering length is a=GAA/(1+GAA). Independent values are a=-.27965204-.45443176i, approaching the supplied -.2796521331-.4544316488i. The other axial orientation channel has b=.02344997-.78859959i, distinctly different. Its cross Green function with A vanishes at Q=0 to1.5e-14. At Qx=.02 and .01, the cross entry scales by four, confirming orderQ² mixing. Hence this simple boundary eigenvalue's quadratic shift is obtained from the diagonal A projection; mixing corrections begin at Q^4. This argument would fail at a boundary-channel degeneracy, but there is none at the checked energy.

Independent finite differences give Re(a_Q)=.00428041 at Q=.02 and .00428065 at .01 with the small regulator, consistent with the supplied limiting .00428076. The physical coefficient is Re(a_Q)/8 times Jz*lambda^4, about+.0005351 Jz*lambda^4 multiplying Qx², and likewise Qy². This is a quadratic coefficient; a second-derivative convention doubles it. The fixed-puncture Schur correction is fully included, not dropped.

For total longitudinal momentum p, the two endpoint moves contribute -cos(p/2) in second-order slow units. The arm bottom -2cos(p/2)=-2+p²/4+... gives quadratic coefficient+Jz*lambda²/4. Other momentum dependence in the boundary scattering only changes subleading terms of this model.

## Indexing and Airy offset

The host includes ell2. The first separate long-arm site is ell3, labeled n=1 when n=ell-2. Its tension onsite is therefore3f, and subsequent sites have f(n+2), as both continued-fraction scripts implement. With Sigma=GAA, the zero-tension band-edge boundary relation is psi0=-Sigma psi1. Writing its linear solution psi_n proportional to n-a gives a=Sigma/(1+Sigma). The continuum zero is at n=a; thus the Airy energy is

    -2+|z_Ai,1| f^(2/3)+f(2+a)+...

with f=lambda²/8. Both the +2 and the sign of a are correct. The denominator E-3f-GAA-tail, and its derivative1-GAA'-tail', agree with this indexing. The continued-fraction derivative recurrence -g_new²*(1-g_old') also has the correct sign.

The root's complex-energy host routine continues the retarded branch through the local energy window around-2; its lower-half-plane pole evaluation must be described as continuation, not the physical advanced resolvent. The independent upper-half-plane comparison validates its boundary branch in that window, not arbitrary complex energies or all band edges.

## Source and residue

Using the previously checked limiting source u=(A+2D)/sqrt(2), the host-to-arm vertex is u^T G A. The leading boundary residue is f(1-a)^2 in the analytic resonance normalization. Multiplying the original source factorlambda^4 gives

    Res = lambda^6 (u^T G A)^2 (1-a)^2/8 + o(lambda^6)

within the partial model and limiting-source convention. The transpose and complex square are appropriate for this analytic scalar resolvent residue. Replacing them by an absolute square would incorrectly erase its complex phase. Independent quadrature gives coefficient-.03036205-.03638509i at the finite regulator, consistent with -.03036208824-.03638513790i. The real part may be negative: this is a continued-pole residue, not a positive spectral weight.

The normalized endpoint source used here already includes its A/D amplitudes; no additional factor2 is warranted. In physical-energy units the resolvent prefactor and change of pole variable cancel in the residue, leaving the lambda^6 scaling above. Earlier logarithmic corrections to the limiting slow source remain relevant and are not an automatic power-series remainder.

## Real-frequency response

The response formula u^TGu+(u^TGA)^2/(1/g_arm-GAA) is the correct Schur result for a source supported in the host. Its interference term need not be positive separately. For the Hermitian graph with a retarded prescription, the full -Im(response)/pi is nonnegative; it can display a Fano dip. The saved161-point grid has minimum spectral density .0608454, and reaches about.190 of the background near its dip. This supports the displayed lineshape, without interpreting the complex pole residue as an integrated positive weight. The frozen-self-energy eigenvalue only centers that sampling grid; the separate energy-dependent continued-fraction calculation supplies the model pole.

The supplied model pole rows converge toward width coefficient-Im(a)/4=.1136079122 and the stated complex residue. Small root residuals are numerical equation checks, not a uniform finite-arm truncation bound. Missing native K2/higher couplings, complete channel closure and physical state/source identification remain outside this result. None of these partial-model coefficients establishes a native scalar pole.

## SHA-256 identities

- `/private/tmp/neutral_slow_host.py`: `46c5f8680a7d0508dcc834c1291d18fc7b7251f0d6699c0926bc4c7873507656`

- `/private/tmp/neutral_slow_host.json`: `31b91afd082b2db209578c088e71a965bf7c1082dec60d6e5ab8dcb7af3cc4c7`

- `/private/tmp/neutral_slow_dispersion.py`: `2fe94c11ef5a01e2b0d8c3daa37f40a19a0bce9835178d5089c56619bbfd9aae`

- `/private/tmp/neutral_slow_dispersion.json`: `4f511c59724809a6fb43f06a04a959ad3a6fac94679e6f2e330a119c3a4772f0`

- `/private/tmp/neutral_slow_resonance.py`: `05c13f55f4167e5445bcab7a1bb402aedf605461361e38a05a63be1efedc2acf`

- `/private/tmp/neutral_slow_resonance.json`: `79f287a9ba9aa7fef454d5b30e0ae4ca73ed298c4bdac26c802196a3d00ad8c0`

- `/private/tmp/neutral_slow_response.py`: `f72c57bf5145f3e98c5225217a2675459aa07b17b01dd097b4c528cf4e88a5a8`

- `/private/tmp/neutral_slow_response.json`: `ccc8ebce523b144068c29acf700ed1b7a00d13d5d840774053dcc29c00b57dcc`

- `/private/tmp/neutral-slow-response-independent.py`: `74e0567477f2e8ac75cdf6c6fccfec2b8fab32c36f76b4829f668be2527c6700`

- `/private/tmp/neutral-slow-response-independent.json`: `886b05ac864ee6b470710742a96d674b8072c6c7527906e4c2b31a794a64e50c`
