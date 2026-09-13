# Independent two-centre derivation of the stress spectral weight

This is a second analytical route for the linear-cone coefficient in R8.
It uses the exact interband phase space, rather than an expansion at large
internal momentum. The native-lattice remainder still uses BLOCK07_IR_PROOF.

For positive real frequency Omega and spatial transfer Q, let
s0=Omega^2-|Q|^2. The symmetric retarded susceptibility is defined by
continuing R5 from omega to -i(Omega+i0). Its positive spectral density is
rho_AB=-Im chi_R,AB/pi. From the spectral denominator,

    rho_AB(Omega,Q)=sum_nodes int dp/[(2pi)^3 v]
                        J_AB(p,Q) delta(Omega-r_--r_+)/2. (S1)

It vanishes below the two-particle threshold Omega<|Q|. For Omega>|Q|,
take Q=q e3 and use prolate variables

    r_-+r_+=q u,   r_+-r_-=q eta,
    p3=q u eta/2,
    p_perp=q sqrt((u^2-1)(1-eta^2))/2,
    d^3p=q^3(u^2-eta^2) du d eta d phi/8.                (S2)

Here u>=1 and -1<=eta<=1. The delta function sets u=Omega/q and contributes
1/q. Writing J=N/(r_- r_+), the Jacobian, 1/2 in S1 and this delta factor
combine to N/4. On the ellipsoid,

    N=(s0/2)(A p).(B p)-2(p.A p)(p.B p)
                         +(q^2/2)(e3.A p)(e3.B p)
      =1/2 p^T A L B p-2(p^T A p)(p^T B p),
    L=s0 I3+Q Q^T.                                     (S3)

The ellipsoid is p=L^(1/2) n/2 with n uniformly distributed on the unit
sphere under d eta d phi. Therefore

    <p_i p_j>=L_ij/12,
    <p_i p_j p_k p_l>=(L_ij L_kl+L_ik L_jl+L_il L_jk)/240,
    <N>=[tr(A L B L)-tr(A L)tr(B L)/3]/40.               (S4)

All polarizations are retained in this contraction. With two Weyl nodes,
the exact continuum spectral density is

    rho_AB(Omega,Q)=1_(Omega>|Q|)/(160 pi^2 v)
                      [tr(A L B L)-tr(A L)tr(B L)/3].     (S5)

The formula extends continuously to Q=0 by an ordinary spherical-shell
integral. For A=B it is nonnegative: L is positive definite above threshold,
and the bracket is the squared Frobenius norm of the traceless part of
L^(1/2) A L^(1/2). A pure isotropic lapse A=n I gives the constant-in-Omega
weight n^2 |Q|^4/(240 pi^2 v), and has no response at Q=0. This is the
spectral version of the earlier quartic lapse logarithm.

## Dispersion calculation of the logarithm

Introduce a fixed positive upper pair-energy cutoff Lambda only for this
continuum comparator. The Euclidean response is

    chi_AB(i omega,Q)=-int_(|Q|)^Lambda
                       2 Omega rho_AB(Omega,Q)/(Omega^2+omega^2) d Omega.

Set x=Omega^2. The S5 bracket is a degree-two polynomial P_AB(x). Polynomial
division gives

    P(x)/(x+omega^2)=a x+(b-a omega^2)+P(-omega^2)/(x+omega^2).

The first two terms and the upper-limit logarithm supply local terms through
the order of interest. The lower-limit logarithm is

    +P_AB(-omega^2) log(omega^2+|Q|^2)/(160 pi^2 v).        (S6)

At x=-omega^2, L=-(kappa^2 I3-Q Q^T). Thus P_AB(-omega^2) is precisely
the polynomial kappa^4 T_AB(Khat) obtained in the annulus derivation, proving
the same sign and 1/(80 pi^2 v) logarithm coefficient by a different route.
Changing the cutoff affects local terms; no native UV identification or
Newton coefficient follows from this auxiliary cutoff.

This exact spectral density is for the linear continuum cones and the
specified real symmetric stress vertices. The lattice proof transfers its
leading nonanalytic even response. It does not equate the full lattice
spectral density, parity-odd terms or high-frequency behavior with S5.
