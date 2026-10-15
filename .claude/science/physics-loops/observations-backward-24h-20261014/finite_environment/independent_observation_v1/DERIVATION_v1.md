# Independent physical-frame and metric-input derivation

This handwritten source/admission check precedes exposure to the parent's new M17 working note or implementation. It uses only the existing FUTURE_CONFINEMENT, LOCAL_RESPONSE and FINITE_BODY notes as supplied candidate premises. It is not a complete finite-body solution, a formal audit or a proof of an observed environment. Units are c=1 and signature is (-+++).

## Physical-frame action and curvature source

Write the inherited action as

    S = integral sqrt(-g_E) [Q R_E/2 - Q K_AB dphi^A.dphi^B - 2Q H_v^2 U]
        + S_m[g_J,psi],       g_J = C(phi) g_E.

Here Q is constant for a fixed candidate, and C is strictly positive at finite fields. Put c_A=partial_A ln C. The four-dimensional conformal transformation gives

    sqrt(-g_E)=C^(-2) sqrt(-g_J),
    R_E=C [R_J + 3 box_J ln C - (3/2)(d ln C)^2_J].

Integrating the box term by parts for compactly supported variations yields the bulk Jordan action

    S = integral sqrt(-g_J) [F_J R_J/2 - Z_AB dphi^A.dphi^B/2 - W]
        + S_m[g_J,psi],
    F_J=Q/C,
    Z_AB=(2Q/C) [K_AB-(3/4)c_A c_B],
    W=2Q H_v^2 U/C^2.                                      (A)

The subtraction in Z is essential. Starting with a conventional half-normalized Einstein scalar while retaining this candidate's K would change the theory. This is a field-dependent metric transformation, not a coordinate change. Boundary/junction conditions remain separate obligations; dropping a bulk total derivative does not provide them.

For general Z, scalar variation at fixed physical metric gives

    Z_AB box phi^B + Gamma^(Z)_{A,BC} dphi^B.dphi^C
        + (1/2) F_J,A R_J - W_,A = 0,                    (B)
    Gamma^(Z)_{A,BC}=(Z_AB,C+Z_AC,B-Z_BC,A)/2.

There is no explicit matter variation in (B) because S_m is minimally coupled to g_J. This does not remove matter from the solution. Metric variation instead gives

    F_J G_mn = T^m_mn + Z_AB partial_m phi^A partial_n phi^B
               - g_mn [Z_AB dphi^A.dphi^B/2+W]
               + nabla_m nabla_n F_J - g_mn box F_J,
    F_J R_J = -T_m + Z_AB dphi^A.dphi^B + 4W + 3 box F_J. (C)

The physical curvature therefore cannot be replaced by the GR matter-trace formula unless the scalar/derivative terms have been controlled. Conversely, imposing (B) on a prescribed metric is a necessary scalar consistency condition, not proof of (C), the matter equations or boundary matching. The single canonical-scalar specialization agrees with Salgado's Jordan-frame equations (12) and (17), after identifying his f with F_J.

## A one-sided candidate certificate that shows the route is possible

This is an independently obtained illustration of a conditional curvature route, not a claim that the entire environment or all three fields have been reconstructed. Use the inherited definitions

    a=(1-k)(1+3k)/4, alpha=sqrt(a), s=(1+k)/(k(1-3k)),
    0<k<1/3, nu>0, Q>0, H_v>0,
    z=exp(-alpha u)>0,
    D=1+2(1+k)(x^2+y^2)/3.

The new z is a scalar coordinate, not the observed photon redshift. Substitution into (A) gives

    C=(1+s)/(z^2+s),
    F_J=Q(z^2+s)/(1+s),
    Z_zz=2Q(1-3a)/(a(1+s))=:Z0>0,
    Z_xx=8Q k z^2/(9D),       Z_yy=2Q k z^2/(3D),
    W=3Q H_v^2(z^4+s)/(1+s)
      +Q H_v^2 nu z^4 (ln z)^2/[a(1+s)]
      +Q H_v^2 k x^2 z^((1-k)/a)(z^2+s)^2/(1+s)^2
      +(2Q H_v^2 k/3) y^2 z^((1+k)/a)(z^2+s)^2/(1+s)^2.

All displayed kinetic components are positive at finite fields in the open parameter domain. No assertion uniform at k=1/3 is intended. The exact z equation is

    Z0 box_J z = W_z + (8Q k z/(9D))(dx)^2_J
                          + (2Q k z/(3D))(dy)^2_J
                          - [Q z/(1+s)] R_J.             (D)

Consider a regular compact spatial domain with a static physical metric

    ds_J^2=-N(X)^2 dt^2+h_ij(X)dX^i dX^j,

with N>0, h positive definite, and **all three scalars time independent**. Then

    box_J z = [1/(N sqrt(h))] partial_i(N sqrt(h) h^ij partial_j z)

is elliptic. At an interior maximum of z, its value is nonpositive; the transverse gradient terms in (D) are nonnegative. If that maximum has z>=1, the regulator derivative is nonnegative because it is proportional to z^3[4(ln z)^2+2 ln z]. The transverse potential derivatives are also nonnegative. Thus

    W_z >= 12 Q H_v^2 z^3/(1+s),
    R_J >= 12 H_v^2 z^2                                  (E)

at such a maximum. For a supplied upper curvature bound R_J<=Rbar throughout the domain and boundary bound z<=z_b, this gives the necessary estimate

    z <= max{z_b,1,sqrt(max(Rbar,0)/(12 H_v^2))}.           (F)

For the constant vacuum z=1,x=y=0, both the scalar equation and the metric trace require R_J=12 H_v^2, checking the normalization and sign. This is not an observational value for R_J or H_v.

The assumptions of (F) matter. A static metric does not itself prove that each scalar is static. Time derivatives make the Lorentzian terms indefinite and invalidate the elliptic maximum argument unless separately bounded. Horizons, singular shells, distributional curvature, an unbounded exterior or unattained extrema require their own boundary/regularity treatment. Exterior-only Rbar is not an interior bound. A boundary value z_b is a supplied scalar matching datum. The estimate is one-sided: it controls negative-u excursion, not z approaching zero or u approaching positive infinity, and it does not bound an arbitrary force gradient, reconstruct x and y, prove existence/uniqueness or select a dynamically realized state.

## What physical static metric functions would have to be supplied

For a spherically symmetric static physical geometry in an areal-radius chart, write

    ds_J^2=-exp(2n(r)) dt^2+exp(2l(r)) dr^2+r^2 dOmega^2.

Direct contraction of the metric curvature gives

    R_J=-2 exp(-2l)[n''+(n')^2-n'l'+2(n'-l')/r]
         +2[1-exp(-2l)]/r^2.                             (G)

This is a geometric identity, without using Einstein's equations or a matter density. Its normalization controls are Minkowski (R=0), Schwarzschild (R=0 outside the source) and the Kottler form f=1-2M/r-Lambda r^2/3, n=ln(f)/2,l=-ln(f)/2 (R=4 Lambda). In particular, a nonzero clock shift, bending or tidal field is not by itself a nonzero Ricci scalar: the Weyl curvature contributes to tidal/lensing effects. With Lambda=3H_v^2, the vacuum normalization matches the preceding action check.

For stationary physical clocks and vacuum photon propagation,

    frequency_received/frequency_emitted
        = exp[n(r_emitted)-n(r_received)].                (H)

These clock ratios supply differences in n, subject to the physical-clock identification and reference congruence. They do not supply l. For an ideal radial null path,

    dt/dr=exp(l-n),
    roundtrip proper time at a stationary emitting radius r0
       =2 exp(n(r0)) integral_(r0)^r1 exp(l-n) dr.          (I)

If the endpoint areal radii are independently calibrated, an exact continuum of such measurements with one fixed emitter can in principle determine the optical factor by differentiation. Finite ranging data supply path integrals with endpoint, motion, propagation and transponder calibration, not an automatically known function l(r). Nonradial deflection and delay likewise sample an optical geometry rather than the Ricci scalar at one point.

As an additional ideal geometric control, a circular geodesic has coordinate angular frequency Omega^2=exp(2n)n'/r and local static-observer speed squared r n'. A measured tracer requires its own geodesic, equilibrium/orbit, distance and velocity assumptions. Faber and Visser provide a concrete first-post-Newtonian construction combining this type of dynamical potential with the lensing potential; their matter-density interpretation adds Einstein equations. It is not a calibrated profile for this candidate or a proof that sparse measurements determine arbitrary exact n,l.

Equation (G) needs n'' and l', not merely small amplitudes of n and l. A small smooth ripple epsilon b(r) cos(r/epsilon) on a compact radial interval, with smooth b, can approach zero uniformly while its second derivative grows. This kinematic example shows why a C0 metric-error bar alone cannot imply a curvature-error bar; it is not a constructed solution of the candidate theory or a universal impossibility theorem. A suitable fitted function class, regularity bound, resolved derivative covariance or direct curvature measurement could supply the missing control.

The reference time normalization cancels from (G), but radius/length units do not. A numerical ratio R_J/H_v^2 still requires the same physical clock/length normalization and candidate H_v scale. Using a measured GM/r as a Ricci bound, identifying F_J^(-1)/(8 pi) with a measured Newton coefficient, or substituting an Einstein-frame curvature for R_J would each need an additional derivation.

## Finite-body matching remains a physical input

The existing flat FINITE_BODY note holds Einstein particle density fixed, uses a local decoupling equation and matches the scalar to a specified vacuum at mathematical infinity. The local-response note omits potential/mixing and time evolution only within a declared regime. The future-confinement theorem is homogeneous and conditional on its basin; it does not determine a local boundary today. None supplies an observed static metric or validates carrying a flat-patch boundary to a cosmological exterior.

An actual environmental application must specify the interior and surrounding domain, scalar boundary or asymptotic state, regularity/possible layers, and either measured geometry with derivative error control or a self-consistent metric/matter solution. The latter needs stress/pressure/support, profile, scales and matching, rather than density alone. A curvature-based necessary bound may reduce reliance on an assumed density profile, but it exchanges that input for calibrated geometric information and does not establish the omitted coupled equations.
