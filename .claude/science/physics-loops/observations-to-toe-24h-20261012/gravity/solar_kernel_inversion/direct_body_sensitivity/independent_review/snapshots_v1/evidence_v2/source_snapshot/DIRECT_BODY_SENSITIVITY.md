# Gravitational self-energy as an observed-source bridge

Direct parent research, October13,2026. Type: bounded_theorem. Status:
conditional-support. This is a conventional weak-body calculation inside the
supplied tensor/scalar candidate, not a new fundamental theory or a claim that
the repository axioms produce matter. Its purpose is to replace one explicit
missing input of the preceding calculation: the body's scalar sensitivity.

## 1. Observation first, candidate premises second

The historical lunar-ranging summary is the Earth-minus-Moon fractional
differential acceleration toward the Sun, (-1.0 +/-1.4)e-13. The primary paper
also supplies the geophysical difference in gravitational self-energy per
total mass, U_E/(M_E c^2)-U_M/(M_M c^2)=-4.45e-10. These are exposed development
inputs. The latter is a supplied Earth/Moon structure calculation; the
polytropes below do not reconstruct those bodies. The observation can constrain
a relation between external acceleration and internal gravitational energy.
It cannot, by itself, establish the field action or microscopic matter.

Keep the earlier supplied action: an Einstein metric g_*, massless scalars
phi^A with positive constant kinetic matrix K_AB, and a universal physical
metric g_J=A(phi)^2 g_* with A=exp(alpha_A phi^A), constant alpha. Define

    a = alpha^T K^-1 alpha >=0,   f=a/(1+a),   zeta=alpha.phi.

Use fixed physical nongravitational constants and baryon number/entropy,
isolated nonrotating weak Newtonian bodies, zero external pressure, no other
macroscopic long-range force, and a slowly varying asymptotic scalar.
At leading exterior order match each body to

    S_B=-c integral m_B*(phi_infinity) ds_*,
    m_B*=A M_J,   M_J=E_equilibrium/c^2.

This matching and the Newtonian matter energy are new explicit assumptions.
No charge-neutrality theorem or microscopic chiral phase is silently imported.
The preceding scalar clock vacuum/profile construction is not needed here.

## 2. Physical gravitational coefficient and equilibrium derivative

For two weak constituents with physical proper masses M1,M2, their Einstein
masses are A M_i and their physical separation is R_J=A R_*. Einstein-frame
tensor plus scalar exchange has energy -G_*(1+a)A^2 M1 M2/R_*.
Dividing by A to express a physical energy gives

    U_J=-G_J M1 M2/R_J,   G_J=G_* A^2(1+a).

This is the local coefficient for negligibly self-gravitating test masses.
Finite bodies have different effective mutual coefficients below. Holding
G_* and alpha,K fixed gives partial_A ln G_J=2 alpha_A. Merely replacing an
Einstein coordinate radius by a fixed proper radius would miss this distinction.

Let X denote physical matter configurations at fixed conserved baryon number
and entropy. Assume a differentiable stationary branch of

    E[X,G]=E_0[X]+G W[X],   U_G=G W[X],

where E_0 includes rest and internal energy and has no explicit G dependence.
At a constrained stationary point, the configuration derivative of E
vanishes along the allowed variations. The envelope derivative therefore is

    dE_eq/dG = W[X_eq],
    s := -d ln M_J/d ln G = -U_G/(M_J c^2),
    b_A := partial_A ln m_B* = alpha_A(1-2s).                  (1)

U_G is the gravitational potential energy, not total binding energy. The
configuration may contract as G changes; its first variation cancels in the
envelope identity. No fixed-radius approximation was made. These identities
are exact within the defined Newtonian energy plus rest-energy wrapper.
Their interpretation as physical scalar charges has only the stated weak
self-gravity accuracy; the denominator is not a full relativistic resummation.

There is also a useful response theorem. Remove symmetry zero modes and
suppose the constrained Hessian H=E_XX is strictly positive with the needed
inverse, and the branch is smooth. Differentiating stationarity gives

    dX_eq/dG = -H^-1 grad W,
    E_eq''(G) = -(grad W)^T H^-1 grad W <=0,
    ds/d ln G = s+s^2-G^2 E_eq''/E_eq >= s+s^2,               (2)
    partial_B b_A = -4 alpha_A alpha_B (ds/d ln G).

E_eq>0 is required. Equation(2) is a local stable-branch statement, not
existence or uniqueness of a global minimum. Its scalar response matrix is
negative semidefinite. It establishes neither compact-star scalarization nor
nonlinear stability of the full metric/scalar/matter equations.

## 3. A material equilibrium with a solved density profile

Supply a Newtonian barotropic polytrope

    P=K_EOS rho^(1+1/n),   internal energy density u=nP,
    dP/dr=-G m(r)rho/r^2,   dm/dr=4 pi r^2 rho.

rho is conserved baryon mass density. This neglects internal/gravitational
energy as a source in the Newtonian Poisson equation; those are higher-order
weak-compactness corrections, not hidden exact general-relativistic terms.
Write rho=rho_c theta^n, r=L xi,

    L^2=(n+1)K_EOS rho_c^(1/n-1)/(4 pi G),
    theta''+2 theta'/xi+theta^n=0,
    theta(0)=1, theta'(0)=0.

For the supplied n=1,1.5,2,2.5, the first zero xi1 is finite. Let
mu=-xi1^2 theta'(xi1)>0. Then R=L xi1 and M_b=4 pi L^3 rho_c mu.
The n=1 solution theta=sin(xi)/xi, xi1=mu=pi provides an analytic control.

Multiplying hydrostatic balance by 4 pi r^3 and integrating with P(R)=0
gives 3 integral P dV=-U_G, hence U_int=-n U_G/3. One can derive the
coefficient of U_G without adopting it as a fit. Hydrostatic enthalpy is
(n+1)K_EOS rho^(1/n)+Phi=-GM_b/R with Phi(infinity)=0. Integrating against
dm gives (n+1) integral P dV+2U_G=-GM_b^2/R. Combining the two identities
yields

    U_G=-3 G M_b^2/[(5-n) R],
    E_eq=M_b c^2+(1-n/3) U_G.                               (3)

At fixed M_b and K_EOS, the Lane-Emden shape is fixed, and the mass formula
implies

    rho_c proportional to G^(3n/(3-n)),
    R proportional to G^(-n/(3-n)),
    U_G proportional to G^p,   p=3/(3-n),
    dE_eq/d ln G=U_G,   ds/d ln G=p s+s^2.                   (4)

Thus total binding E_eq-M_b c^2=U_G/p cannot replace U_G in(1). Near n=3
the susceptibility grows and the weak/static approximations need separate
control. This block stays at the frozen n<=2.5 and small supplied compactness.

For completeness the actual radial linear stability can be checked, rather
than assuming stability from varying only R. For fractional Lagrangian radial
displacement eta(r) exp(i omega t), conserved shell mass gives
Delta rho/rho=-(3eta+r eta'), and adiabatic Delta P=-Gamma P(3eta+r eta'),
with Gamma=1+1/n. Perturbing the mass-shell equation
ddot r=-4 pi r^2 partial_m P-Gm/r^2 gives

    (Gamma P r^4 eta')'
    +r^3[(3Gamma-4)P]' eta+rho r^4 omega^2 eta=0.

Regular center and the free-surface domain must make the integrated boundary
term vanish. Multiplying by eta and integrating gives

    omega^2 integral rho r^4 eta^2 dr
       =integral Gamma P r^4 (eta')^2 dr
        -integral r^3[(3Gamma-4)P]' eta^2 dr >0.              (5)

For constant Gamma>4/3 and P'<0 inside, the second integrand is positive for
any nonzero admissible displacement, and the first is nonnegative. This
establishes linear radial stability for the supplied barotropic Newtonian
polytropes. It is not a proof of every nonradial mode, nonlinear stability,
or a relativistic equation of state. The abstract Hessian result(2) applies
only on a subspace where its own positivity assumptions hold.

## 4. Exterior force and the same body's radiative charge

For constant Einstein masses m_i and scalar charge covectors b_i, use
the positive inner product <b,c>=b^T K^-1 c. Leading exchange yields

    V12=-G12 m1 m2/r,   G12=G_*[1+<b1,b2>].                 (6)

Assume G12>0, slow motion, weak exterior potential, isolated circular motion,
and an orbital period much longer than internal adjustment times. The physical
body radii must be small compared with separation; this is checked for the
synthetic fixtures but not asserted for arbitrary source observations.
Let M=m1+m2, mu=m1m2/M, Omega^2=G12 M/r^3, v=r Omega. In the center of mass,

    D_A=mu (b1_A-b2_A) r_vector,
    I_ij=mu r_i r_j,   I^b_Aij=bQ_A I_ij,
    bQ=(m2 b1+m1 b2)/M.

The retarded scalar wave is, to the displayed multipole order,

    phi_rad^A=-G_* (K^-1)^AB/(c^2 R_wave)
       [Q_B+n_i dot D_Bi/c+n_i n_j ddot I^b_Bij/(2c^2)+...].

The circular monopole and trace are constant at the retained order. Positive
scalar flux is c^3 R_wave^2 integral dot phi^T K dot phi dOmega/(4 pi G_*).
Angular averages <n_i n_j>=delta_ij/3 and
<n_i n_j n_k n_l>=(delta_ij delta_kl+delta_ik delta_jl+delta_il delta_jk)/15
therefore give the separately leading channels

    P_D=G_* mu^2 ||b1-b2||^2 r^2 Omega^4/(3 c^3),
    P_SQ=G_* ||bQ||^2 I'''_ij I'''_ij/(30 c^5),
    P_T=G_* I'''_ij I'''_ij/(5 c^5),
    I'''_ij I'''_ij=32 mu^2 r^4 Omega^6.                     (7)

Dipole/quadrupole interference is odd on the sphere and vanishes. The tensor
formula requires the conserved matter plus Newtonian interaction stress;
using material kinetic stress alone would repeat the earlier factor error.
Equation(6)'s total force enters that stress conservation and the actual orbit.

Normalize the displayed channels to the GR quadrupole expression evaluated
on the same m_i,r,Omega with gravitational coefficient G12:

    R_channels = [1+||bQ||^2/6
                    +(5/96)||b1-b2||^2(c/v)^2]
                   /[1+<b1,b2>].                           (8)

This is a sum of the leading term of each channel. With unequal charges it
is NOT a complete through-c^-5 post-Newtonian power: subleading corrections
to dipole radiation occur at the same order as quadrupoles. They have not
been calculated. No precise binary-period or pulsar prediction follows.
An eccentric source can also have time-dependent monopoles and charges and
is not covered by the circular argument.

For the universal body model b_i=alpha(1-2s_i), the leading dipole relative
to the weak-body GR normalization is

    P_D/P_GR approximately (5/24) f (s1-s2)^2(c/v)^2.         (9)

It vanishes when sensitivities agree. If both sensitivities vanish exactly,
(8) reduces to the preceding result (1+a/6)/(1+a)=1-5f/6. Equal nonzero
sensitivities instead change the effective common coupling. Thus the earlier
zero-sensitivity source condition was real; finite equilibrium bodies do not
automatically inherit its exact radiation ratio.

## 5. Map to the exposed lunar free-fall summary

At a common reference asymptotic A, acceleration toward a solar source is
proportional to 1+<b_i,b_S>. Define the Earth-minus-Moon difference divided
by their mean. Equations(1),(6) give

    Delta = <b_E-b_M,b_S>/[1+< (b_E+b_M)/2,b_S>]
          = -2 f (s_E-s_M)+higher weak-self-gravity terms
          = 2 f [U_E/(M_E c^2)-U_M/(M_M c^2)]+higher terms.

Consequently the supplied geophysical coefficient predicts

    Delta_pred=-8.90e-10 f.                                 (10)

The source-Sun sensitivity cancels from the leading coefficient up to the
discarded products of sensitivities. With the earlier weak optical relation
gamma=(1-a)/(1+a), this candidate has eta_N=2f=1-gamma at this order. This is
the familiar constant-coupling scalar-tensor relation, not a new phenomenology.
It was obtained here from the explicitly matched energy and force.

Keep the earlier exposed working interval0<=f<=1/2500 unchanged. Evaluate
the frozen four f values and signed summary residual
z=(observed mean-Delta_pred)/(reported uncertainty). Display intersections
with one and two reported uncertainties, including the nonnegative f condition.
These rectangles are working comparisons, not confidence bounds or a joint
likelihood with the earlier optical source. The geophysical coefficient's
uncertainty was not supplied; raw normal points and full ephemeris covariance
are not present. No LLR parameter is fitted in the principal comparison.

The total EP summary can also contain composition-dependent force. If a free
composition nuisance d_comp is admitted, the same single observation reads

    Delta=d_comp-8.90e-10 f.

Every f can then fit the mean with a suitable d_comp. The principal candidate
sets d_comp=0 by its universal nongravitational metric premise; the observation
does not prove that premise. The paper's SEP and eta summaries reuse the LLR
data and an external laboratory composition result, and are not new independent
data points. Its Cassini-derived beta estimate is not imported.

The earlier charge EFT concerned specified fixed particle counts. It neither
proves macroscopic bodies retain those counts under charge exchange nor removes
possible electromagnetic forces. This block's no-extra-force premise therefore
cannot be extended to an arbitrary charged matter variant without analysis.

## 6. Controls, provenance and remaining reconstruction

The frozen protocol specifies12 Newtonian profiles and finite differences at
fixed baryon mass and EOS, analytic n=1, direct density-energy quadratures,
radial energy positivity, and refined direct sphere integration of the tensor,
scalar dipole and quadrupole fields. Calibration of synthetic EOS constants
only makes M_b=R_0=1 for each synthetic initial body. It uses no observed
Earth/Moon profile or LLR value. Detailed six binary fixtures are frozen in
NUMERICAL_FIXTURES.json before the first execution.

The primary observational source is Williams, Turyshev and Boggs,
Phys.Rev.Lett.93,261101(2004), DOI10.1103/PhysRevLett.93.261101,
arXiv gr-qc/0411113v2. Relevant text through conclusions and rendered pages2,3
were read. The external PDF remains local with its hash in SOURCE_LEDGER.json.
No raw data, modern-limit survey or independent geophysical inversion is
claimed. Repository binding-energy/velocity notes and the preceding action
block provide trace context only; their narrower premises and unrepeated
runners are listed in the ledger.

This calculation supplies a weak material-source bridge and a cross-domain
free-fall/radiation relation. It leaves the action's origin, matter microphysics,
compact stars, cosmological boundary conditions, actual apparatus likelihoods
and a common TOE open. Numerical execution and independent checking have their
own records; writing these equations is not a report that they have passed.
