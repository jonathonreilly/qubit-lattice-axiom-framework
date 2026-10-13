# Inverse potential and a two-field constant-G expansion trajectory

Direct parent derivation. Type: bounded_theorem. Actual surface status:
conditional-support. This is a candidate extension prompted by the preceding
massless model's distance-order mismatch. The expansion function used below is
the exposed fixed comparison curve, not a new extraction of H(z) from light
curves. The potential and its energy scale are constructed inputs, not a TOE.

## Action, source, and one-field inverse equation

Extend the Einstein action by -4V inside its R-2K(dphi)^2 normalization.
Thus the homogeneous equations, with K=I and positive dust, are

    3H_*^2=8pi G_*rho_*+dot phi^2+2V,
    dot H_*=-4pi G_*rho_*-dot phi^2,
    ddot phi+3H_*dot phi=-grad V-4pi G_*alpha rho_*.

The dot is Einstein proper time. Radiation is omitted in this late-time block.
Keep universal matter metric g_J=A^2g_*, A=exp(alpha.phi). Physical conserved
dust has rho_J=rho_J0 exp(-3n), n=ln R_J, and rho_*=A^4 rho_J. No constituent
sensitivity correction is included in this ideal dust closure.

For one scalar alpha=sqrt(a)>0 set zeta=ln A=sqrt(a)phi and p=dzeta/dn.
Write H_J=H0 E(n), h=dln E/dn. Then

    H_*=A H_J(1-p),       dot phi=A H_J p/sqrt(a).

Supply the particular comparison expansion and density normalization

    E^2=m exp(-3n)+1-m,   0<m<1,
    rho_J0=3H0^2 m/(8pi G_N),   G_N=G_*(1+a),   A(0)=1,
    D=4pi G_* A^2 rho_J/H_J^2
      =3m exp(2zeta-3n)/[2(1+a)E^2].

The G_N relation is a local long-range, weak-body matching premise. A massive
or screened scalar needs that premise checked, not silently reused. The
physical H curve alone does not fix rho_J0 or this source interpretation.

Taking the Einstein Raychaudhuri equation in n yields the inverse system

    zeta'=p,
    p'=(p+h)(1-p)+D+p^2/a
       =h+D+(1-h)p+(1/a-1)p^2.                         (1)

Recover the potential along that trajectory as

    V=(A^2 H_J^2/2)[3(1-p)^2-p^2/a-2D].              (2)

This parameterized expression defines a potential function only where the
field is invertible or repeated-field values and derivatives agree. Equations
(1)-(2) do not automatically grant a globally single-valued C2 potential.

Since D'=D(2p-3-2h), the derivative of(2) and(1) gives

    V_phi=-A^2 H_J^2 C/sqrt(a),
    C=p'+(h+3-2p)p+aD
     =h+(1+a)D+4p+(1/a-3)p^2.                        (3)

Equivalently V'=-(A^2 H_J^2/a)p C. Equation(3) is exactly the scalar
equation, so it is a useful consistency check, not an extra adjustable fit.

## A zero-drift endpoint does not admit a smooth one-field potential

For the displayed target h'=h(-3-2h). At a turning point p=0,
differentiating(3), without dividing by p, gives

    (V_phi)'=-A^2 H_J^2[h+(1-3a)D]/sqrt(a).          (4)

A C2 potential would instead give (V_phi)'=V_phiphi phi'=0 there.
Consequently h+(1-3a)D=0 is a necessary turning-point compatibility
condition. It is not sufficient for a global single-valued potential.

At the supplied present normalization zeta=0, h0=-(1+a)D0 and
D0=3m/[2(1+a)]. If p0=0, equations(1)-(4) give

    p'_0=-a D0,   V_phi(0)=0,
    (V_phi)'_0=4sqrt(a) H0^2 D0 >0.                 (5)

Thus no C2 one-field potential realizes this exact target through this
zero-drift endpoint under the density and local-normalization premises.
This is not an observational exclusion of zero drift or a general scalar
no-go: the exact continuous target, source normalization and one-field
restriction are supplied. With a=0 the derivation dividing by sqrt(a) is
inapplicable, and ordinary constant-potential dust is a regular limit.

The local past branch makes the obstruction explicit:

    phi=-(sqrt(a)D0/2)n^2+O(n^3),
    V_phi=4sqrt(a)H0^2D0 n+O(n^2),
    V=V0+(8H0^2/3)sqrt(2sqrt(a)D0)(-phi)^(3/2)
       +O(phi^2),
    V_phiphi/H0^2=-4/n+O(1),      n approaches0 from below. (6)

The potential can be C1 on this one-sided branch but has divergent curvature.
No numerical smoothing changes the exact endpoint identity.

## A second scalar supplies a constructive alternative

Now use two canonical scalars (u,chi), alpha=(sqrt(a),0), A=exp(sqrt(a)u).
Let V_Lambda>0 be a freely supplied energy scale. Set

    k=sqrt[3(1+a)/(2a)],
    S(chi)=V_Lambda/(1+a) sinh^2[k(chi-chi_c)],
    V(u,chi)=V_Lambda+(S(chi)/2)
                  [(u-sqrt(a))^2+eta u^2].         (7)

Here chi_c is a field-coordinate shift and eta is a dimensionless new theory
choice. For eta>=0, V is globally nonnegative and at least V_Lambda. The
canonical kinetic form is positive. The initial eta=0 form already has the
required background; its transverse stability must still be checked below.

There is an exact expanding trajectory with u=0, hence A=1, satisfying

    S(chi)=4pi G_*rho_J,
    dot chi=+sqrt(a S),
    3H^2=2(1+a)S+2V_Lambda.                         (8)

Take chi-chi_c<0 so S_chi<0. Since the last equation implies
S_chi=-3H sqrt(S/a), the chi equation gives

    ddot chi=-(3/2)H dot chi,
    ddot chi+3H dot chi=+(3/2)H dot chi=-V_chi.

Meanwhile V_u=-sqrt(a)S exactly cancels the dust source
4pi G_*sqrt(a)rho_J. This makes u=0 a solution of its full scalar equation,
not a imposed frozen-field approximation. Equation(8) obeys
dot S=-3HS, dust conservation, Friedmann, and

    dot H=-(1+a)S=-4pi G_N rho_J.

Therefore H^2=(8pi G_N/3)rho_J+2V_Lambda/3 exactly, while
G_J=G_*A^2(1+a)=G_N is constant along the homogeneous solution. The uncoupled
scalar carries positive kinetic energy even though alpha.dot phi=0. This
extra direction is precisely what the one-field endpoint argument omitted.

To realize the displayed m=.3 comparison, supply

    V_Lambda=(3/2)H0^2(1-m),
    t0=asinh sqrt[m/(1-m)],
    chi(n)=chi_c-(1/k)asinh[sqrt(m/(1-m))exp(-3n/2)]. (9)

The shift can be chosen so chi(0)=0. The magnitude of V_Lambda is not
predicted. The matter fraction is a background initial condition, not a
quantized constant. A continuum of a values remains; matching this
background does not identify the local coupling or select a unique theory.

## Preserve the first curvature failure and a declared repair

Put c=V_Lambda/(1+a)>0, so S=c sinh^2[k(chi-chi_c)],
S_chi^2=4k^2 S(c+S), and S_chichi=2k^2(c+2S). At u=0,

    Hess V = [[(1+eta)S, -sqrt(a)S_chi],
              [-sqrt(a)S_chi, (a/2)S_chichi]],

    det Hess V=a k^2 S[(eta-3)c+(2eta-2)S].         (10)

For eta=0, the determinant is negative whenever S>0. The first positive
potential has a negative-curvature direction; positive kinetic energy and
positive potential alone did not establish its curvature stability. Preserve
that failed candidate instead of reporting the repaired form as the first try.

The explicit choice eta=3 gives det=4a k^2 S^2>0, with positive diagonal
entries, for every S>0. This is a globally sufficient constant choice for
nonnegative curvature along the trajectory; for eta<3 the c term is negative
as S tends to zero, so no smaller constant works for the entire expanding
trajectory down to S=0. At S=0 the Hessian is positive semidefinite. This
coefficient does not affect the exact u=0 background or its matter source.
It is a supplied stabilization parameter fixed by this stated curvature
criterion, not a supernova measurement or a derived framework constant.

The theorem concerns the potential Hessian on the homogeneous trajectory.
It is not global convexity of(7) at arbitrary u, a full metric/dust perturbation
stability theorem, a growth-of-structure calculation, or a global attractor.
Ordinary gravitational density instabilities are not excluded by(10).

## Local force and drift have separate matching conditions

As an explicit local quadratic diagnostic, freeze the Hessian M^2=Hess V
and use a flat nearly static patch. This retains potential masses while
omitting curvature and background dust/metric responses of comparable
cosmological order; it is not a full match through order H^2 r^2. Holding
Einstein-frame particle number fixed would additionally contribute the
positive matrix S alpha alpha^T to the instantaneous scalar mass. Both
choices will be displayed; neither solves the full density/metric response.
For the eta=3 trajectory its eigenvalues mu_j^2 are nonnegative. With
orthonormal eigenvectors e_j, residues a_j=(alpha.e_j)^2>=0 and sum a_j=a.
The static Green response of the canonical scalar equations gives

    Phi_pair=-G_* m1 m2/r [1+sum_j a_j exp(-mu_j r)],
    F_pair=-G_* m1 m2/r^2
              [1+sum_j a_j(1+mu_j r)exp(-mu_j r)].  (11)

Units with c=1 are used; dimensional mu_j is an inverse length, or an inverse
time divided by c. The point-source Green normalization is the same as the
earlier massless scalar equation. These are weak zero-sensitivity static
sources, not a screened nonlinear solution or a complete compact-body match.

For x>=0, 0<=1-(1+x)exp(-x)<=x^2/2, by integrating t exp(-t)
from0 to x. Thus the relative force correction to the massless local limit
is bounded by sum a_j(mu_j r)^2/[2(1+a)]. This bounds only the scalar mass
correction in the supplied local diagnostic, not every cosmological correction.
Positive residues prevent a
hidden cancellation from being needed for this bound. At mu_j r<<1 the
earlier G_N and gamma relations apply to leading local order; they are
not exact identities at arbitrary separation for the massive extension.

The homogeneous coefficient has dln G_J/dt_J=2sqrt(a)du/dt_J=0. The
historical LLR Eq9 can therefore be compared with zero only under the added
local-background-tracking and weak-source approximation. Its correlation
with fitted tidal dissipation and shared data with the EP summary must remain
explicit. The earlier exact free massless Minkowski clock spectrum does not
automatically carry over to a massive field in this cosmological state.

This construction replaces the massless model's forced deceleration with a
specified potential and extra scalar direction. It reproduces an already
chosen expansion, leaving the vacuum-energy scale, matter origin, perturbations,
initial conditions, source luminosity, high-energy completion and uniqueness
unresolved. It is a concrete conditional reconstruction route to test further.
