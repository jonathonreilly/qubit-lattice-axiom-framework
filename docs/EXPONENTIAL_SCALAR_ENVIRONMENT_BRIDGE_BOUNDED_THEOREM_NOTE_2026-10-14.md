# Revised scalar finite-body and matter-environment bounded theorem

Status: conditional support, not a derived action or observed environmental fit.
Claim type: bounded_theorem. Scientific author: /root.
Primary runner: `scripts/exponential_scalar_environment_bridge_check.py`.

The observed-gravity bridge requires a finite instrument response and a local
scalar environment. The finite-body measure argument derives a geometry-dependent
calibration envelope from a stipulated stable weak-source Green function. The
supplied action determines a stationary relation for a prescribed nonrelativistic
density, but the density prescription and stability must be distinguished: one
negative-field root at fixed physical density need not have positive scalar mass.
At fixed particle data the allowed action can support two local minima. This
removes an algebraic assumption in a specified domain while preserving the actual
history, apparatus and state-selection gaps.

## Inputs and claim boundaries

The supplied action is in [the full-action note](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md).
Weak local normalization is conditional as derived in [the local-response note](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md).
The entropy-dependent consequence reuses [the thermal-bounce theorem](EXPONENTIAL_SCALAR_THERMAL_BOUNCE_BOUNDED_THEOREM_NOTE_2026-10-14.md)
with its complete ideal-bath and strict-bounce hypotheses. No temperature,
material density or force data are fitted here. All numerical examples and
accessed theoretical sources are exposed development material; no independent
empirical test is claimed. The potential, coupling, field metric, scales and
matter action remain supplied.

## I. Finite-body force and readout geometry

Scientific author /root. Derivation frozen before executable controls. This addresses the remaining laboratory-gravity bridge: actual gravitational measurements use finite source/test bodies and instrument geometries. It asks which point-source ceiling survives such geometry, without treating a laboratory uncertainty as a response-model error. It is a conditional linear response theorem, not a nonlinear environment solution or a fit to a particular gravimeter.

### Supplied linear response and explicit premises

Reuse the action-normalized, locally frozen weak-source response already checked in the campaign: in one common finite scalar background, the potential between two nonrelativistic point masses is

 V(r)=-G_bare m1 m2/r [1+sum_j omega_j exp(-mu_j r)],
 omega_j>=0, sum_j omega_j=q, mu_j>=0,
 q=b^T K^-1 b<1/3, G_bare=C/(8piQ).

The nonnegative omega_j follow from a positive kinetic metric and self-adjoint nonnegative mass matrix in the stated linear regime. Stability, frozen coefficients, universal nonrelativistic scalar charges, weak fields and negligible source backreaction beyond this linearization are premises. Body density profiles must be supplied in physical units. Arbitrary screening, relativistic pressure, strong self-gravity, varying background or negative effective charges lie outside this result.

Differentiating the potential gives the exact pair-force ratio

 F_pair/F_Newton =1+sum_j omega_j f(mu_j r),
 f(z)=(1+z) exp(-z), 0<=f(z)<=1 for z>=0,
 f'(z)=-z exp(-z)<=0.                                      (1)

Let K(x,y) be the Newtonian contribution to a chosen scalar force component or linear instrument readout, including nonnegative mass densities, projection or instrument weights, and 1/r^2. Assume finite integrals, nonzero Newtonian normalization I0=integral K, and body supports separated from coincidence. The calibrated ratio for exactly this measurement model is

 gamma_obs = 1+sum_j omega_j I_j/I0,
 I_j=integral K(x,y) f(mu_j |x-y|).                        (2)

This is a forward prediction after specifying geometry, not a derivation of the experimental calibration method.

### Positive geometry removes the point-source premise

If K has one sign almost everywhere (reverse the readout orientation if needed), equation (1) implies 0<=I_j/I0<=1. Therefore

 1<=gamma_obs<=1+q.                                       (3)

The result holds for finite nonuniform bodies; point particles are unnecessary. For the component of the mutual attractive force along a direction n, it suffices that n.(y-x)>0 for every source/test pair. Supports separated by parallel planes provide this condition. Disjoint spheres with center separation d>R_s+R_t satisfy it along their center axis. Any densities>=0 and finite masses are allowed under the linear-response premises. Coincident/touching singular cases are not needed for the proof.

For homogeneous spheres, Green-function angular integration gives

 gamma_obs=1+sum_j omega_j S(mu_j R_s) S(mu_j R_t)
                        (1+mu_j d) exp(-mu_j d),
 S(z)=3[z cosh(z)-sinh(z)]/z^3, S(0)=1.                   (4)

One way to derive S is to integrate the interior source weight sinh(mu r)/(mu r) against 3r^2/R^3; applying the same convolution to the test sphere gives the second S. Although S(z)>1 for z>0, the COMPLETE force factor in (4) is <=1 for nonoverlapping spheres, as proved directly by the positive pair-force integral. S alone must not be used as a force enhancement. Equation (4) assumes fixed spherical profiles, not body equilibrium derived from the scalar action.

### Signed readouts retain a geometry cost

For a differential or torque-like linear readout K may change sign. Let

 kappa_geom = integral |K| / |I0| >=1.

The general triangle estimate gives |I_j/I0|<=kappa_geom, hence

 |gamma_obs-1|<=q kappa_geom.                              (5)

Using 0<=f<=1 gives a tighter signed decomposition. Orient I0>0 and write K=K_plus-K_minus with K_plus,K_minus>=0 and disjoint support. Then their normalized integrals are (kappa_geom+1)/2 and (kappa_geom-1)/2, respectively. Therefore

 -(kappa_geom-1)/2 <= I_j/I0 <= (kappa_geom+1)/2,
 1-q(kappa_geom-1)/2 <= gamma_obs <=1+q(kappa_geom+1)/2. (5a)

These bounds need not be sharp for a single Yukawa range or imply gamma_obs>0. A physically used positive calibrated G still requires gamma_obs>0. The special upper ceiling1+q cannot be asserted for a signed readout merely because each pair interaction is attractive. For example, two positive force measurements combined with Newtonian weights +1 and -9/10 give I0=1/10. At separations1 and10 and mu=1, I/I0=10[f(1)-(9/10)f(10)]>1. This is an explicit synthetic differential observable, not an identified laboratory apparatus.

If a separately justified response error eta>=0 gives positive gamma_cal<=(1+eta)gamma_obs, a usable upper bound is

 gamma_cal<=(1+eta)[1+q(kappa_geom+1)/2]
             <(1+eta)(kappa_geom+7)/6.                    (6)

Laboratory G's statistical uncertainty is not eta. Actual geometry, body response, backgrounds and error terms must be established before applying (6). At a distinct cosmological background, an additional C_local/C_cos factor remains and this same-background relation cannot eliminate it.

### Consequence for the correlated thermal bounce budget

Reusing the separately checked joint total-bath relation P_bare>2 exp(2N)/[R sigma^(4/3)] gives, if positive same-background calibrated gravity satisfies (6),

 P_cal > 12 exp(2N)/[R sigma^(4/3)(1+eta)(kappa_geom+7)]. (7)

For positive geometry kappa_geom=1, this reduces to the improved3/(2R) coefficient without any point-source approximation. More generally N>=0, sigma=1, eta=0 and a unit target P_cal<=1 are incompatible when

 kappa_geom <= 12/R-7, R=(11/4)^(1/3).                 (8)

Equality is excluded because the bounce/coupling bounds are strict. A larger geometry factor does not construct an escaping history or a successful experimental fit. If eta or entropy are nontrivial their explicit factors remain. This implication depends on the separate joint thermal proof, not on body algebra alone.

### Assumption accounting

Finite source/test size is eliminated as an automatic objection to the weak same-background cap for positive readouts. An unrestricted instrument geometry cannot be eliminated; equation(5) quantifies what signed cancellation costs. The assumed linear background, mass spectrum, physical matter profiles, small-field conditions, and any cosmological-to-local environment identification survive. No candidate action, state, mass scale, entropy source, actual laboratory response or primordial-abundance likelihood is selected. Published CODATA G measurements motivate this issue but are not fitted by these synthetic controls.

## II. Matter-density stationary relation and its ambiguity

Direct scientific author /root. Hand derivation frozen before its checker.
The observed-gravity problem requires a local field and scalar mass around a
material apparatus. Earlier response bounds froze that environment. This block
asks what the supplied action itself determines when nonrelativistic matter is
included. No numerical laboratory density, chosen vacuum energy, source profile,
relaxation rate or measured likelihood is supplied as an answer.

### The density held fixed matters

Let A=sqrt(C), 0<k<1/3, nu>0, Q>0, Hv>0, and retain the complete supplied
three-field action. For nonrelativistic particles of fixed Jordan rest mass,
S_particles=-sum m_J integral A(phi) ds_E. At fixed particle number per local Einstein proper three-volume, define
rho_*=m_J n_E, holding the Einstein metric fixed in the scalar variation. A
literal coordinate number density must be divided by the spatial proper-volume
factor; locally orthonormal coordinates give the same number at the event. Its local matter energy is rho_E=A rho_*,
while rho_J=rho_*/A^3. The scalar source in the exact variation is b rho_E/(2Q).
Consequently, at prescribed rho_* and neglecting gradients and time derivatives,
stationarity is that of

    W(phi)=U(phi)+delta_* A(phi),  delta_*=rho_*/(2Q Hv^2).       (1)

This factor follows from the action's -Q K(partial phi)^2 normalization. A
stationary point is a conditional algebraic solution, not a proof that a real
body, gravity and a pressure-supported density profile reach or sustain it.
Radiation pressure, self-gravity and nonlocal matching are outside this reduction.

For x=y=0, transverse stationarity is automatic, and transverse potential
second derivatives are k exp(-lambda_x u) and (2k/3)exp(-lambda_y u), both positive.
Because A is independent of x,y, it adds no transverse source. At a full stationary
point the field-space covariant Hessian equals the coordinate Hessian. Mixed
entries vanish at x=y=0. Thus the remaining homogeneous stability question is
one dimensional, with positive field metric.

The fixed-particle-density convention agrees with the effective-potential
construction in Khoury and Weltman, Chameleon Cosmology, arXiv:astro-ph/0309411v2,
page5 equations(7)-(10), https://arxiv.org/pdf/astro-ph/0309411. That paper is a
convention cross-check, not evidence that this different candidate screens or
fits an experiment. Its old phenomenological claims are not adopted here.

### Exact physical-density map on the negative-u branch

Use z=A, D=1+s-s z^2, a=(1-k)(1+3k)/4 and s=(1+k)/(k(1-3k)).
For 0<z<1, corresponding precisely to u<0, put

    L=log(D/z^2)>0,
    U0(z)=3/2+(3/2)s(1-z^2)^2+nu D^2 L^2/[8a(1+s)].           (2)

Here u=-L/(2sqrt(a)) and z_u=sqrt(a) z/F>0 with F=(1+s)/D.
Differentiation, using L_z=-2(1+s)/(z D), gives

    d_*(z)=-U0_z
      =6s z(1-z^2)
       +nu D/[2a(1+s)] [s z L^2+(1+s)L/z] >0.                (3)

At a stationary point delta_*=d_*(z). If instead a measured positive physical
density rho_J is specified, define delta_J=rho_J/(2Q Hv^2). Since delta_*=z^3 delta_J,
the same stationary equation becomes

    delta_J=d_J(z)=d_*(z)/z^3
      =6s(z^-2-1)
       +nu D/[2a(1+s)] [s L^2/z^2+(1+s)L/z^4].               (4)

Every positive factor D,L,z^-2,z^-4 strictly decreases on 0<z<1. Their positive
products decrease, and the first term has strictly negative derivative. Hence
d_J'(z)<0. The endpoint limits are d_J(0+)=infinity and d_J(1-)=0. Thus every
specified positive physical density and fixed candidate parameters has exactly
one negative-u stationary solution. This derives a conditional relation; it does
not choose k,nu,Hv,Q or the density, and says nothing about extra u>=0 solutions.

The distinction is operational: changing z at fixed particle density changes
physical volume and rho_J. Holding rho_J fixed instead requires changing the
particle distribution or applying external constraints. One cannot replace the
linearized fixed-particle Hessian by differentiating while artificially holding
rho_J constant. At stationarity,

    U0_zz=-z^3 d_J'(z)-3 z^2 d_J(z),                         (5)

so d_J'<0 alone does not imply U0_zz>0.

### A fixed-particle density need not select one stable branch

An explicit allowed synthetic counterexample will use

    k=1/10, nu=1/10000, delta_*=20.                          (6)

Here s=110/7 and a=117/400. For z->0+, the positive nu term makes d_*(z)->infinity.
At z=1, d_*=0. At z=1/2 the first term alone is 9s/4>20. At z=1/10,
D/z^2=11590/7<exp(8): for instance exp(1)>8/3 by its positive series, and
(8/3)^8>11590/7. Thus 0<L<8. Substituting L<8 in the positive nu term gives an
explicit rational upper bound for d_*(1/10) below20. Therefore W_z=20-d_*(z)
has signs negative, positive, negative, positive as z runs from0 through1/10,
1/2 and1. By continuity and interior extrema on the three intervening intervals,
there are at least two distinct radial local minima separated by a radial local
maximum. In the full three-field potential that radial maximum is a saddle,
since both transverse curvatures are positive; the radial minima are full local
minima.
The function is analytic inside this domain; these sign-separated extrema are
strict. Numerical roots, Hessians and depths are supporting checks to follow,
not the proof of their existence. We do not assert these are all stationary
points, or that their physical densities agree. A prescription to choose the
lowest energy does not prove that a dissipating or gravitational body reaches it.

The counterexample targets universal uniqueness at fixed particle data. It does
not contradict the unique negative-u root at fixed measured rho_J: the different
stationary z values in (6) correspond to different physical densities20/z^3.
No observed theory exclusion is inferred from this synthetic example.

### Local mass and the remaining boundary problem

With prescribed rho_*, dimensionless canonical radial coordinate dchi=sqrt(K_uu)du
has kinetic term -Q(partial chi)^2. In a weak nearly flat static domain,

    Laplacian_E chi=Hv^2 W_chi.

At a stationary point,

    m_E^2/Hv^2=W_uu/K_uu=(z_u)^2 U0_zz/K_uu,
    m_J^2=m_E^2/z^2,  m_J^2/Hv^2=(a/J) U0_zz=q U0_zz.       (7)

The matter term is linear in z, so W_zz=U0_zz when delta_* is fixed. Positive
m_E^2 is a local scalar condition under these external-source assumptions; it
is not full gravitating-fluid stability. The finite-body Yukawa bounds need a
stable background and sufficient separation of scales, which (7) can test but
cannot assume. A finite body still requires a density prescription, center and
exterior boundary conditions, and control of gradients, pressure, relaxation
and metric errors. The action supplies this boundary equation, not its solution
or its observed normalization. The selected field state and apparatus bridge
remain open even though (4) removes an algebraic branch ambiguity in its domain.

## III. Stationary density susceptibility and scalar mass

Direct derivation /root, before the addendum checker. Retain all premises and
fixed-particle versus physical-density distinctions of section II of this note.
No new apparatus, density measurement or state-selection premise is added.

On 0<z=A<1 define S_env=-z d_J'(z)/d_J(z). Multiplying the exact physical-density
map by z^2 gives

    z^2 d_J =6s(1-z^2)
     +nu D/[2a(1+s)] [s L^2+(1+s)L/z^2].                 (1)

Each positive product strictly decreases with z; the first derivative is
-12s z<0. Hence (z^2 d_J)'<0, so S_env>2. At fixed action parameters and scales,
the implicit stationary relation then gives

    d log A_stationary / d log rho_J = -1/S_env,         (2)
    -1/2 < d log A_stationary / d log rho_J <0.

This is the slope of a family of stationary points, not an asserted real-time
adiabatic response. A real body's dynamics and boundary matching remain open.

The fixed-particle Hessian identity gives a sharper local condition:

    m_J^2/Hv^2 =q z^2 delta_J (S_env-3),  q=a/J>0.        (3)

Therefore positive radial scalar mass at a stationary point is equivalent to
S_env>3, or to -1/3 < d log A_stationary/d log rho_J <0. The point S_env=3 has
zero radial mass, and 2<S_env<3 has negative radial mass under the prescribed
particle-density perturbation. Positive transverse masses remain as before.
This supplies a derivative-based diagnostic; merely asserting a unique root
or a slowly varying physical density does not establish the required stability.

For fixed s,a,nu>0 as z->0, D->1+s and L=log(D/z^2)->infinity. The dominant term is

    d_J ~ nu(1+s)L/(2a z^4),  S_env ->4,
    d log A_stationary/d log rho_J ->-1/4.               (4)

At z->1-, d_J has a positive first-order zero; S_env->infinity and the logarithmic
susceptibility tends to0 from below. These are local asymptotic branch statements,
not a cosmological trajectory or an allowed route past the chart endpoints.
The synthetic intermediate root already exhibited can have S_env<3 despite the
strict one-to-one physical-density map. Its physical density is different from
those of the two minima. No density or mass scale has been fitted or derived.

## Computational scope and preservation

The canonical runner preserves the finite-body 208 controls, stationary-source
96 controls and affected susceptibility 36 controls as separate units. It retains
all 160 sphere-factor rows, five volume-quadrature comparisons, 54 exposed density
samples, all three stationary root records and their mass/density diagnostics.
The susceptibility unit uses the same newly computed roots rather than re-solving
or loading a stale result. Finite grids corroborate formulas; the all-domain
statements are the analytic arguments above. Parameter values are synthetic.

Original finite-body 202/3 cancellation/resolution failures and their exact
repairs are retained. The first susceptibility normalization stalled and was
terminated without a result; its revised 34/1 check exposed an unjustified fixed
asymptotic-error tolerance. The final calculation uses an exact derived remainder
bound. Neither failure changed the theorem or was erased. Actual altered codes
were executed and rejected separately; their outputs are recoverable evidence,
not additional observations. A homogeneous stationary solution and a scalar mass
are not a solved gravitating body, an adiabatic tracking theorem or an empirically
established screening mechanism. No formal audit or main-branch integration is
asserted by this note.
