# A metric choice links bending, active source and eccentric radiation

Status: conditional-support. Direct parent derivation, October13 UTC.
All physical identifications below are supplied candidate assumptions. This
note studies a constructive alternative to the conformal zero-bending route.
It neither claims novelty for scalar-metric geometry nor imports an observed
binary-pulsar mass or decay rate as a proof input.

## Explicit isotropic sector and physical metric

Set N=D>0 in the existing local vector action, fix e, and use its sourced
sector u=e phi with no freely specified orthogonal modes. Write G_N=G N and
c_s^2=1/(alpha N). Then

    L_phi = [(phi_t/c_s)^2-|grad phi|^2]/(8 pi G_N),
    (c_s^-2 partial_t^2-Delta)phi = -4 pi G_N rho_active.

Supply the preferred-coordinate physical metric

    ds^2=-A^2 c^2 dt^2+B^2 dx.dx,
    A=exp(psi), B=exp(-lambda psi), psi=phi/c^2.

Here lambda is a constant new candidate parameter, not a fitted response
function or registered framework primitive. lambda=-1 is the conformal
completion. The field action itself is not replaced by an Einstein action.

For a particle set z=(B/A)^2 v^2/c^2<1 and gamma_z=(1-z)^(-1/2). Its action,
canonical momentum, Hamiltonian and exact active source are

    L_a=-m_a c^2 A sqrt(1-z),
    p_a=m_a (B^2/A) gamma_z v_a,
    H_a=m_a c^2 A gamma_z
       =sqrt(m_a^2 c^4 A^2+c^2(A/B)^2 p_a^2),
    rho_active=sum_a m_a A gamma_z(1+lambda z_a) delta^3(x-x_a).

The source is -partial L/partial phi at fixed positions and velocities.
For lambda=-1 it reduces to mA/gamma_z, as in the conformal calculation.
For lambda>=0 it is positive for every timelike particle in this ansatz.
Its sign need not be positive for every other lambda; no such claim is made.
The Hamiltonian is nonnegative for real timelike configurations for any real
lambda and positive m. Adding the positive field energy yields a conserved
finite-energy Hamiltonian under the action's time-translation symmetry and
appropriate boundary conditions. This does not control point self-energy,
global existence, nonlinear stability or gravitational binding sensitivities.

For minimally coupled Maxwell fields the coordinate refractive index is

    n_opt=B/A=exp[-(1+lambda)psi].

In units where flat vacuum Maxwell energy is(E^2+B_em^2)/2, its coordinate
Lagrangian density is(n_opt E^2-n_opt^-1 B_em^2)/2. The canonical electric
momentum is Pi=n_opt E, so H_em=(Pi^2+B_em^2)/(2n_opt)>0. At fixed E,B_em,
-partial L_em/partial phi=(1+lambda)H_em/c^2. Thus the same change that
produces bending also changes the optical field's active source. The binary
calculation below has no electromagnetic fields. The gravitational field's
own energy has no analogous metric coupling in this supplied action; full
strong-equivalence or general-covariance claims would require further work.

## Static optics: a recoverable sector and a new prediction

In a static spherically symmetric vacuum exterior, the linear field equation
gives psi=-m_g/r with m_g=G_N M_g/c^2. The exterior active mass M_g is a
boundary/integrated-source parameter, not an inferred inertial binary mass.
The optical index is exp(a/r), a=(1+lambda)m_g. For positive a and weak
deflection at impact parameter b, put epsilon=a/b and u=b/r. Conservation
of the optical angular momentum gives

    (du/dtheta)^2=exp(2epsilon u)-u^2,
    u0=exp(epsilon u0),
    deflection=2 integral_0^u0 du/sqrt(exp(2epsilon u)-u^2)-pi.

The weak turning point is u0=1+epsilon+3epsilon^2/2+O(epsilon^3).
Substitute u=u0 sin chi and h=epsilon u0. Expansion of the regular integrand
gives

    1+h/(1+sin chi)
      +h^2[ -(1-sin chi)/(1+sin chi)+3/(2(1+sin chi)^2) ]+O(h^3).

The integrals from0 to pi/2 of1/(1+sin chi) and its square are1 and2/3.
Hence the half-angle is pi/2+h+(pi/2-1)h^2+O(h^3), and

    deflection = 2(1+lambda)m_g/b
               +pi(1+lambda)^2 m_g^2/b^2+O((m_g/b)^3).

In the weak exterior metric, g_00=-1-2psi-2psi^2+... and
g_ij=(1-2lambda psi+...)delta_ij. Its static PPN-shaped coefficients are
gamma=lambda and beta=1. This is a statement about this exterior metric;
it is not a complete many-body PPN classification of the preferred-frame
field theory. Choosing lambda=1 recovers the familiar leading bending
coefficient4m_g/b. It also gives a definite next coefficient4pi, rather
than the supplied Schwarzschild comparator15pi/4 at fixed asymptotic b.
The difference pi/4 is a prospective discriminator; no second-order solar
measurement is fitted or claimed decisive here.

The exposed VLBA analysis motivates near-unit leading gamma. It used a
unit-gamma correlator and modeled residual relative positions with atmospheric
and source corrections. Choosing lambda=1 from that context is calibration,
not prediction. Reconstructing the raw candidate likelihood remains open.

## Exact source changes the leading weak radiation

Assume two separated, weakly self-gravitating neutral bodies approximated by
the point-particle action, with constant masses and self terms at the order
kept. This formal approximation removes self-field divergences from the
orbital calculation; it is not an extended-body or compact-star theorem.
Let velocities be small compared with both c and c_s, external potentials
be small compared with c^2, and radiation reaction be a slow correction.

At the first needed source order,

    mA gamma_z(1+lambda z)
       =m[1+phi/c^2+(lambda+1/2)v^2/c^2]+higher orders.

Let T=sum m v^2/2 and U=-G_N m1 m2/r in the Newtonian centre of mass. The
leading orbital potential gives sum m phi=2U. With M=m1+m2,

    Q=integral rho_active=M+[2U+(2lambda+1)T]/c^2+constant_self_terms,
    Q_dot=(1-2lambda)U_dot/c^2,

where T+U is conserved at this conservative order. Thus exact rest-mass
conservation cannot remove this source monopole. Source corrections to the
dipole or quadrupole are at higher slow-motion order than the terms retained;
the Newtonian centre-of-mass dipole is constant. Strong-body sensitivities,+preferred-frame motion and higher multipoles are outside this calculation.

For I_ij=sum m x_i x_j, the far field to this order is

    phi_rad=-G_N/r [Q+n_i n_j I_ij''/(2c_s^2)]_(t-r/c_s).

The outgoing scalar energy flux is phi_t^2/(4pi G_N c_s). Sphere moments
<n_i n_j>=delta_ij/3 and <n_i n_j n_k n_l>=
(delta_ij delta_kl+delta_ik delta_jl+delta_il delta_jk)/15 give

    P=(G_N/c_s){[Q_dot+Tr(I''')/(6c_s^2)]^2
                +I_STF''' : I_STF'''/(30c_s^4)}.

The trace and corrected monopole interfere before squaring. Dropping their
cross term is incorrect. Newtonian virial algebra gives Tr(I'')=4T+2U and
Tr(I''')=-2U_dot. The monopole coefficient is therefore

    K_dot=[(1-2lambda)/c^2-1/(3c_s^2)] U_dot.

For circular motion U_dot=0; the earlier circular scalar power survives at
this leading order. This is an explicit check of that special limit, not
permission to transfer the old arbitrary-source result to eccentric systems.

## Eccentric average and the linked-comparator obstruction

Use Kepler semimajor axis a, eccentricity e_orb<1, reduced mass m_red,
k=G_N M, Omega^2=k/a^3. For relative vectors r,v and Newtonian acceleration
a_vec=-k r/r^3, jerk j=-k[v/r^3-3r(r.v)/r^5], differentiating
I=m_red r r^T three times gives

    I'''=m_red[j r^T+r j^T+3(a_vec v^T+v a_vec^T)],
    I_STF''' : I_STF'''=(8/3)m_red^2 k^2/r^4
                        (12v^2-11 r_dot^2).

With r=a(1-e_orb cos E), dt=(1-e_orb cos E)dE/Omega,

    <U_dot^2>=m_red^2 a^4 Omega^6
       e_orb^2(4+e_orb^2)/[8(1-e_orb^2)^(7/2)],
    <I_STF''' : I_STF'''>=32 m_red^2 a^4 Omega^6 f(e_orb),
    f(e_orb)=[1+73 e_orb^2/24+37 e_orb^4/96]/(1-e_orb^2)^(7/2).

For example the first average follows from
<sin^2 E/(1-e_orb cos E)^5>=(4+e_orb^2)/[8(1-e_orb^2)^(7/2)].
The second follows by inserting the velocity/jerk identity, not by assuming
the candidate follows GR. The paired runner checks both averages directly.

Supply, as a comparison only, P_GR=(G_N/(5c^5))<I_STF''' : I_STF'''> for
the same Newtonian trajectory, masses and G_N. With s=c_s/c and
F=1+73e_orb^2/24+37e_orb^4/96, division yields

    R(e_orb)=P/P_GR
      =s^-5 [1/6 + (5/256)((1-2lambda)s^2-1/3)^2
                             e_orb^2(4+e_orb^2)/F].

This is an algebraic conditional prediction. Circular matching fixes
s=6^(-1/5). At lambda=1 the square coefficient cannot vanish for any real
positive s: it is(s^2+1/3)^2. Thus with this calibration R(e_orb)>1 for
every0<e_orb<1. Matching the eccentric dependence as well instead requires

    lambda_cancel=(1-1/(3s^2))/2.

At the circular speed this is(1-6^(2/5)/3)/2, which is not1. This is a
specific conflict between the illustrative bending and same-orbit radiation
calibrations within this isotropic metric family. It is not a data exclusion,
an inference from measured pulsar masses, or a no-go for anisotropic vector,
tensor, screened, nonlocal or other metric constructions. The one-parameter
completion makes new linked predictions and exposes the next missing sector.

## Remaining limits

No tensor radiative degree of freedom has been supplied. The new metric
does not establish generic relativistic source formation, composite-body
equivalence, cosmology, quantum matter or a universal common parameter fit.
The field/Maxwell/particle energy expressions are conditional finite-energy
action consequences, not existence or regularization proofs. The nonlinear
physical light cone also need not coincide with the fixed field cone.
The original anisotropic q calibration is outside this N=D block; it cannot
be combined silently with its spherical exterior and scalar radiation.

Primary observation context: https://arxiv.org/html/0904.3992v1. The stated
GR leading quadrupole and Schwarzschild series are supplied comparison laws,
not observational inputs or proof premises for the candidate's derivation.
