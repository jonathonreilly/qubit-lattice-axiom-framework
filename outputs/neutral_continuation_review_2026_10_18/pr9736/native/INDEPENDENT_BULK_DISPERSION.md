# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Focused conditional bulk dispersion check

Mathematical scope: the stated first-order host/arm model and its boundary-scattering expansion. The numerical transverse coefficient is confirmed. This is not a controlled native dispersion through orderlambda^4.

## Longitudinal momentum

For a length-ell interval centered at z_start+(ell-1)/2, extending either end changes its center by ±1/2. Fourier transformation at longitudinal total momentum p therefore adds the two endpoint amplitudes to -2cos(p/2), with the same factor in the endpoint coupling. The arm band bottom is -4cos(p/2). Its expansion is -4+p²/2+O(p^4), giving the coefficient +Jz*lambda/2 multiplying p². If curvature means the second derivative rather than the quadratic coefficient, it is +Jz*lambda. Host states of interval length1 move only transversely at K1, so their host dispersion has no p dependence.

## Transverse derivative

In the fixed normalized d orientation basis, w(k)=(cos kx-cos ky)^2 has Brillouin-zone average1. The host energy is epsilon_Q=-4[cos(Qx/2)cos kx+cos(Qy/2)cos ky]. Since partial_(Qx²)epsilon_Q at0 is cos kx/2,

    G_Q = (1/2) integral w cos(kx)/(E-epsilon_0)^2.

Square symmetry gives integral w cos(kx)/(...)²=-(1/8) integral w epsilon_0/(...)². With G'= -integral w/(E-epsilon_0)^2, this yields exactly

    G_Q=(G+E G')/16.

For a=4G/(2+4G), differentiation gives

    a_Q=(G+E G')/[2(2+4G)^2].

The sign of G' is essential: it is negative the squared-resolvent integral. The root formula has this sign correct.

An independent one-dimensional quadrature analytically integrates ky using the retarded square-root branch, then compares a small finite Q with the energy derivative. At E=-4+i*1e-5 it gives G'=-.0463336400-.0534703044i, a_Q=-.0890128578+.0144906698i, converging toward the supplied boundary values -.04633388128-.05347026042i and -.08901367093+.01449119580i. The direct Q finite difference and derivative formula differ by about1e-8. The control is neutral-bulk-dispersion-independent.py/json; finite regulator values are not claimed as exact certificates.

Thus, accepting the supplied conditional boundary-energy prefactor Jz*lambda^4/16, the real coefficient of Qx² is -.00556335443 Jz*lambda^4. The same holds for Qy². A negative coefficient is a local maximum in that transverse direction for the real part of this model branch, not a positive isotropic effective mass. It must not be replaced by a positive curvature by analogy with the longitudinal direction.

## Hard core and other orientation channel

The removed-origin resolvent is Gdd-Gd0*G0d/G00. At Q=0 the d form factor is odd under x/y interchange, so Gd0=0. The dispersion depends analytically on Qx²,Qy² near0, and Gd0 starts at orderQ². G00 is nonzero at E=-4 on the selected continued/retarded branch. Therefore the hard-core correction starts at total degree4 in Q, and does not change the quadratic coefficient.

This does not mean the other orientation channel can always be omitted. At Q=0 the even orientation channel has the hard-core projected Green function Gss-Gs0²/G00. Independent quadrature at the same regulator gives approximately -.07328753-.22606108i, while Gdd is -.28177167-.08706856i. Their scattering denominators are respectively1.70684989-.90424431i and .87291332-.34827425i, both nonzero and distinct. Hence the boundary-scattering eigenvalues are nondegenerate there. Off-diagonal orientation mixing begins at Q² by symmetry, so its effect on this simple eigenvalue begins at Q^4. Bulk arm thresholds alone are degenerate; it is the distinct boundary scattering data that justify this branchwise quadratic calculation. At a different energy/parameter where the boundary eigenvalues coincide, the argument would require degenerate perturbation theory.

The fixed d orientation basis is appropriate for the branch energy. A physical momentum-dependent source may have additional orientation form factors; those affect overlap/residue and should not be inferred from this dispersion calculation alone.

## Native scope

The endpoint model supplies a conditional complex boundary-scattering correction, not a stable full-H pole. Native K2 and higher operators, extra channels, source dressing, and uniform large-feature remainder estimates are not controlled here; some enter before the displayed transverse lambda^4 coefficient. Consequently that coefficient cannot presently be promoted to the native microscopic transverse curvature. No repository edits or formal audit were performed.

## SHA-256 identities

- `/private/tmp/neutral-bulk-dispersion-independent.py`: `26b577d2490cb3848ea18fc6d994cbf4c92dde56b0a04404d09d589dec6cd09c`

- `/private/tmp/neutral-bulk-dispersion-independent.json`: `1a3da592ba07c4999c6be4b2c280e0e8d6bb93420a77ccae3250620dd4b612f8`
