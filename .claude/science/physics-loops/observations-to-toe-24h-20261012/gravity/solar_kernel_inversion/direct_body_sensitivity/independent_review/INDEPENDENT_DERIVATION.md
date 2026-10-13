# Independent finite-body derivation

The calculation below checks the parent's stated weak-body EFT and matching
premises. It is not a replacement primary model. The author code was neither
imported nor executed by this reviewer.

## Frame conversion and constrained equilibrium

At a constant asymptotic A, physical lengths and energies obey R_J=A R_*
and E_J=E_*/A, while a constituent's Einstein mass is A times its physical
mass. Substituting both conversions into the Einstein exchange energy gives

    E_J = [-G_*(1+a) A^2 M1 M2/R_*]/A
        = -G_* A^2(1+a) M1 M2/R_J.

Hence G_J=G_* A^2(1+a), with d ln G_J=2 alpha_A d phi^A. Rescaling only
the separation, or only the masses, would give the wrong power of A.

Use coordinates X on the fixed-baryon/entropy constraint manifold. This
avoids replacing a constrained Hessian by an unconstrained one. For
E(X,G)=E0(X)+G W(X), stationarity gives E_X=0 and thus

    dE_eq/dG = E_G + E_X dX/dG = W,
    H dX/dG + grad W = 0,
    E_eq'' = -(grad W)^T H^-1 grad W.

The last equation requires the stated smooth branch, symmetry zero-mode
removal, and positive invertible constrained Hessian. It does not itself
establish these hypotheses. Since M_J=E_eq/c^2,

    s=-G E_eq'/E_eq=-U_G/E_eq,
    b_A=d ln(A M_J)/d phi^A=alpha_A(1-2s).

Differentiating s explicitly yields

    d s/d ln G = s+s^2-G^2 E_eq''/E_eq.

For positive E_eq and the stable-Hessian hypotheses this is at least
s+s^2. For the attractive gravitational energy here, s is nonnegative.
Then d b_A/d phi^B=-4 alpha_A alpha_B d s/d ln G is negative semidefinite.
This is a response on a specified equilibrium branch, not a proof of
global energy positivity or stability of all coupled field/matter modes.

As an independent non-polytropic control, take E=100+X^T H X/2+G w^T X,
H=((3,1),(1,2)), w=(2,-1). The minimizer is -G H^-1 w; its energy is
100-3G^2/2 and E''=-3. It verifies the signs and the envelope/Hessian
identities without using the author's polytropic helper.

## Polytrope energy and response

Let Pi=integral P dV. Integrating hydrostatic balance after multiplication
by 4 pi r^3 gives 3 Pi+U_G=0. The enthalpy relation at zero surface
pressure gives (n+1) Pi+2 U_G=-G M_b^2/R, because integral Phi dm=2U_G.
Eliminating Pi produces

    U_G=-3 G M_b^2/[(5-n)R],
    E_eq=M_b c^2+(1-n/3)U_G.

In particular total binding energy is U_G/p, p=3/(3-n). It is not the
gravitational energy in the sensitivity formula.

From L proportional to G^-1/2 rho_c^((1-n)/(2n)) and fixed
M_b=4 pi L^3 rho_c mu, obtain

    rho_c proportional to G^(3n/(3-n)),
    R proportional to G^(-n/(3-n)),
    U_G proportional to G^(3/(3-n)).

Writing E_eq=B-C G^p makes G E_eq'=U_G and
d s/d ln G=p s+s^2 immediate. These are exact identities of the
Newtonian energy plus rest-energy wrapper. They do not supply all orders
in relativistic compactness. With G changing as exp(2 zeta), the scalar
mass derivative is d ln M_J/d zeta=-2s.

The independent numerical route was a boundary-value problem on x=r/R
in [0,1], with the first Lane-Emden zero lambda as an unknown parameter:

    theta_xx+2 theta_x/x+lambda^2 theta^n=0,
    theta(0)=1, theta_x(0)=0, theta(1)=0.

Collocation replaces the author's initial-value shooting. Here
mu=-lambda theta_x(1). Composite Simpson quadratures on 4,097 and 8,193
points evaluate all mass and energy integrals. All four shapes agree with
the author outputs; n=1 separately agrees with lambda=mu=pi.

The explicit fixed-mass scaling law then predicts every one of the 12
base bodies and 72 shifted equilibria, including the EOS, density, radius,
energy decomposition, sensitivity, all 36 finite-difference triples, and
the Richardson body charge. No observational profile enters this route.

## Full radial identity and its boundary

For a Lagrangian displacement delta r=r eta, fixed shell mass gives
Delta rho/rho=-(3eta+r eta') and Delta P=-Gamma P(3eta+r eta'). Varying
the mass-shell acceleration -4 pi r^2 P_m-Gm/r^2 gives

    rho Delta acceleration = -4 P' eta - (Delta P)'.

Equating it to -rho omega^2 r eta and multiplying by r^3 produces

    (Gamma P r^4 eta')' + r^3[(3Gamma-4)P]' eta
        + rho r^4 omega^2 eta = 0.

The integration-by-parts boundary term is eta Gamma P r^4 eta'. The
regular-center/free-surface domain must make it vanish and the integrals
finite. On that domain the Rayleigh numerator is

    integral Gamma P r^4 (eta')^2 dr
      - integral r^3[(3Gamma-4)P]' eta^2 dr.

For constant Gamma>4/3 and P'<0 in the interior it is strictly positive
for a nonzero admissible radial displacement; the denominator is positive.
This proves positivity of the radial eigenvalues in the specified problem.
It is stronger than a homologous-radius test, but does not establish the
abstract Hessian's positivity on every nonradial configuration direction.
The source explicitly keeps those statements separate.

For each of the 48 trial controls, I differentiated pressure directly from
the independent collocation profile, rather than substituting the author's
enclosed-mass gravity expression. Simpson integration reproduces the
reported numerator, denominator, Rayleigh quotient, and dimensionless
frequency. Finite trial controls supplement, rather than replace, the
general energy-identity proof.

## Body exchange and separately leading circular channels

Expanding the matched mass in the scalar gives a source m_i b_i. Positive
scalar kinetic matrix K contracts these covectors through K^-1. Tensor
plus scalar exchange therefore gives the stated G12=G_*[1+b1^T K^-1 b2].
Attraction of a particular pair still requires G12>0. It is not implied
by positivity of K for arbitrary opposite charge vectors.

For barycentric positions x1=(m2/M)r and x2=-(m1/M)r, direct summation
gives D=mu(b1-b2)r and I^b=bQ I, with
bQ=(m2 b1+m1 b2)/M and I=mu r r. Circular motion makes the displayed
monopole and quadrupole trace constant. Scalar dipole and quadrupole
amplitudes in the flux are respectively n.D''/c and n_i n_j I^b'''_ij/(2c^2).
Their angular product is odd and integrates to zero.

Using the second and fourth unit-sphere moments gives

    P_D=G_* |D''|_(K^-1)^2/(3c^3),
    P_SQ=G_* |bQ|_(K^-1)^2 (I''':I''')/(30c^5),
    P_T=G_* (I''':I''')/(5c^5).

For a circular orbit I''':I'''=32 mu^2 r^4 Omega^6. The tensor coefficient
uses a conserved total source containing Newtonian interaction stress.
Bare matter kinetic stress is insufficient; the same G12 must enter
the orbit and stress conservation.

Dividing by the specified same-orbit GR reference
G12(I''':I''')/(5c^5) yields

    [1+|bQ|^2/6+(5/96)|b1-b2|^2(c/v)^2]/[1+<b1,b2>].

For b_i=alpha(1-2s_i), |b1-b2|^2=4a(s1-s2)^2, so the leading weak-body
dipole ratio is (5/24) f(s1-s2)^2(c/v)^2. Equal sensitivities remove it.
Zero sensitivities give (1+a/6)/(1+a)=1-5f/6; equal nonzero sensitivities
give a different common effective coupling.

For an independent numerical route I sampled the actual two barycentric
source trajectories, formed their dipole and quadrupole moments by summing
over the two bodies, and differentiated them by Fourier modes. A 14-point
sphere rule (six axes of weight 1/15 and eight cube diagonals of weight
3/40, weights normalized to one) integrates the needed degree-four angular
polynomials. Tensor flux was calculated from two transverse polarization
components, not the author's TT projector array. Scalar inner products
used linear solves with K. All 576 reported angular rows were compared.

This channel sum is not a complete expansion through c^-5 when the leading
dipole is nonzero. Its subleading correction interferes with that leading
dipole at the same power order as the quadrupoles. No binary-period or
pulsar likelihood can be inferred by ignoring that missing calculation.
The parent states this limitation explicitly. Weak internal gravity,
small radii, adiabatic response, circular motion, constant charges, and
the point-source expansion are separate premises; the small numerical
fixtures do not certify arbitrary physical binaries.

## LLR sign, intervals, and nuisance rank

The exact leading-exchange acceleration factors toward a solar source
are 1+<b_E,b_S> and 1+<b_M,b_S>. Their fractional difference relative
to their mean is

    -2a(s_E-s_M)(1-2s_S)
       /[1+a(1-s_E-s_M)(1-2s_S)].

Expanding all three weak sensitivities to first order gives
-2 f(s_E-s_M)=2 f[U_E/(M_Ec^2)-U_M/(M_Mc^2)]. Solar sensitivity only
enters at a discarded product of sensitivities. The supplied negative
Earth-minus-Moon geophysical coefficient therefore predicts
Delta=-8.90e-10 f. This agrees with eta_N=2f=1-gamma for the stated
constant-coupling weak-body model.

With mean m=-1e-13 and sigma=1.4e-13, compute the exact rational residual
(m-Delta_pred)/sigma. The four results are -5/7, -11/140, 39/70, and
64/35. Solving |m+8.90e-10 f|<=k sigma and intersecting with
0<=f<=1/2500 gives [0,3/11125] for k=1 and [0,1/2500] for k=2.
These are images of supplied working rectangles, not confidence intervals.

If Delta=d_comp-8.90e-10 f, the one-row design has rank one for the two
unknowns. Every f fits the mean using d_comp=m+8.90e-10 f. Setting
d_comp=0 is the candidate's universality/no-extra-force assumption;
the same LLR summary cannot establish it. The geophysical coefficient
is a separate supplied structure input, and its uncertainty is unavailable.
