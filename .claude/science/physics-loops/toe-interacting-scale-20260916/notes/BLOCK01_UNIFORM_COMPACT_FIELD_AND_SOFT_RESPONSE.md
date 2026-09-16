# Uniform compact-field control and low-energy response

Personal derivation, 2026-09-16. **Provisional author theorem proposal.**
No independent review or audit has been performed. The supplied Hamiltonian
is the same charged compact rotor used in the preceding campaign. This note
does not prove its fixed-coupling Coulomb/Weyl phase.

The new statement is uniform in spatial volume: weak microscopic coupling
forces small average plaquette defects and nonzero inelastic gauge-field
response below an explicit energy scale. For probes of wave number k the
bound has scale k+g+g^2/k. It resolves a mesoscopic window g much smaller
than k, and supplies soft response at energy O(g) by choosing k of order g.
It does not reach k tending to zero at fixed positive g.

## 1. Exact supplied model and state

Let V=L^3, L>=3, on a periodic cubic graph, with 3V oriented links and 3V
elementary plaquettes. D is vertex-link incidence, C is link-plaquette curl,
so D C^*=0. Links are integer rotors with E_l=-i partial_theta_l and
U_l=exp(i theta_l). Work in exact integer Gauss law D E=Q, where
Q_x=N_(+,x)-N_(-,x). There are m plus and m minus CAR orbitals per vertex.

Write the dimensionless Hamiltonian as

    a H = (g^2/2) sum_l e_l E_l^2
          +g^-2 sum_p b_p [1-cos((C theta)_p)]
          +sum_l (A_l+A_l^*) + H_on,
    A_l=c_(x,+)^* T_l U_l c_(y,+)
        +c_(x,-)^* T_l^* U_l^-1 c_(y,-).                 (1)

Here the star on the numerical matrix T in the second species is entrywise
conjugation; stars on operators elsewhere mean adjoints. All e_l,b_p are
positive, constant within each link or plaquette orientation. T_l depends
only on link orientation. The onsite term is a sum of conjugate one-particle
matrices v,v^* in the two species. A nonnegative onsite charge penalty that
vanishes at Q_x=0 can also be included. No pairing term is present.

The matter sector must contain a product of paired onsite ground states:
choose a ground occupation of v and its conjugate for v^*, with equal
occupation numbers at each site. This condition holds in the full physical
Hilbert space and, for the two-orbital Wilson symbol below, in N_+=N_-=V.
Let E_on be the onsite ground energy in dimensionless units. Then
H_on>=E_on and the specified product attains E_on with Q_x=0.

For finite L and g>0 the kinetic form is elliptic on the compact gauge
quotient, with finite-dimensional CAR fibers and smooth bounded potential.
It has compact resolvent, finite-dimensional ground space, and smooth ground
vectors. Let P0 be the entire ground projection in the chosen matter sector,
and use the normalized ground trace rho0=P0/Tr(P0). It is translation
invariant without requiring a unique ground state or unbroken symmetry in
an infinite-volume pure state.

All bounds below concern this actual ground ensemble. The trial vector is
used only in a variational upper bound; it is not identified with the ground
state or with its correlations.

## 2. An exactly Gauss-neutral Gaussian trial

Let Lambda=ker(D) intersect Z^(3V), a lattice of rank r=2V+1 in ker(D).
In particular, harmonic electric loops are included. With W_E=diag(e_l),
define the normalized link vector

    psi_t(n)=Z_t^-1/2 exp[-t n.W_E.n/2],  n in Lambda,
    Z_t=sum_(n in Lambda) exp[-t n.W_E.n],  t>0.          (2)

Tensor it with the paired onsite product just described. The resulting
vector obeys exact integer Gauss law and the stated filling. Hopping has
zero expectation, because each term changes the fixed onsite occupations.

Choose an integer basis R for Lambda and G=R^T W_E R>0. Poisson summation
on this full-rank coordinate lattice gives

    Z_t=(pi/t)^(r/2) (det G)^(-1/2)
          sum_(m in Z^r) exp[-pi^2 m.G^-1.m/t].          (3)

The derivative of the last logarithm is nonnegative. Absolute convergence
justifies differentiation, and hence

    <n.W_E.n>_t = -partial_t log Z_t <= r/(2t).         (4)

For a plaquette boundary d_p=C^* 1_p in Lambda, the literal electric-basis
shift has overlap

    <psi_t,U^(d_p) psi_t>
      = exp[-t d_p.W_E.d_p/2]
          E_t exp[t n.W_E.d_p]
      >= exp[-t d_p.W_E.d_p/2].                        (5)

Symmetry gives E_t n=0, so the last inequality is Jensen's inequality.
The overlap is real and positive; its upper bound by one also follows from
unitarity. Using 1-exp(-x)<=x and t=alpha g^2, alpha>0, gives

    a E_ground <= E_on + G_L(alpha),
    G_L(alpha)=r/(4alpha)
                +(alpha/2) sum_p b_p d_p.W_E.d_p.       (6)

This is an upper bound in the physical Hilbert space, valid for every g>0.
It does not require a small-field approximation or an electric cutoff.

## 3. Ground-state field concentration, uniformly in L

At any fixed link phase the one-particle matrix of its Hermitian hopping
has eigenvalues plus and minus the singular values of T_l. Second
quantization therefore has minimum -||T_l||_* for each species, where
||.||_* is the nuclear norm. The two species imply the operator bounds

    -(2||T_l||_*) I <= A_l+A_l^* <= (2||T_l||_*) I.    (7)

The bound is uniform in link phase and thus holds on the rotor Hilbert
space and its physical subspace. In particular, a one-particle operator
norm cannot silently replace the nuclear norm.

Let K_L=2 sum_l ||T_l||_* and epsilon_L=(G_L+K_L)/V. Combining the onsite
lower bound, (6), and positivity of both gauge terms yields

    rho0[(g^2/2) sum_l e_l E_l^2
                +g^-2 sum_p b_p(1-cos theta_p)]
       <= epsilon_L V.                                (8)

There are V plaquettes of each orientation. Translation invariance gives,
for orientation j and a link direction i,

    rho_j:=rho0(1-cos theta_(x,j)) <= epsilon_L g^2/b_j,
    g^2 rho0(E_(x,i)^2) <= 2 epsilon_L/e_i.             (9)

With bounded fixed local coefficients, epsilon_L has a finite uniform
upper bound. These are state bounds, not statements that compact defects
are absent. They control their average density, not arbitrary large-field
events, long-range correlations, or a photon self-energy.

For the paired Wilson symbol

    h0(k)=sin kx sigma1+sin ky sigma2
            +(2+zeta-cos kx-cos ky-cos kz) sigma3,
    h_+(k)=h0(k-b xhat),   h_-(k)=h_+(-k)^*,            (10)

with 0<zeta<1 and fixed real b,
all three directed hopping matrices have nuclear norm one. The onsite
paired product fills one negative orbital in each species. For unit electric
and magnetic weights and alpha=1/sqrt(12),

    epsilon_L=6+2 sqrt(3)+sqrt(3)/(2V) < 10,  L>=3.    (11)

This estimate does not select zeta,b,g or the Hamiltonian. Positive matched
anisotropic weights from the prior comparator also satisfy (8)--(9), with
their displayed coefficients retained in G_L.

## 4. Two-observable spectral lower bound

For real finitely supported or finite-box arrays v,w define physical probes

    F=g sum_l v_l E_l,      B=g^-1 sum_p w_p sin theta_p. (12)

For either probe A, its positive inelastic excitation measure is

    mu_A(I)=Tr[rho0 A 1_I(H-E0) (1-P0) A],
    M_A=int_(0,infinity) nu dmu_A(nu)
        =(1/2)rho0([A,[H,A]]).                          (13)

Ground smoothness supplies the domains for F. Direct commutation gives

    2a M_F = sum_p b_p (Cv)_p^2 rho0(cos theta_p)
                +g^2 sum_l v_l^2 rho0(D_l),
    D_l=-(A_l+A_l^*),
    2a M_B = rho0 ||W_E^(1/2) C^*(w cos theta)||^2,
    rho0([F,B])=-i sum_p w_p (Cv)_p rho0(cos theta_p).   (14)

Both charge species contribute with q^2=1 to the electric double
commutator. The compact cosine in the magnetic expression remains an
operator, even for a slowly varying w.

Put c=|rho0([F,B])|. For every lambda>0,

    mu_F((0,lambda])+mu_B((0,lambda])
        >= c-2 sqrt(M_F M_B)/lambda.                   (15)

Proof: the trace of the commutator of P0 F P0 and P0 B P0 vanishes in the
finite-dimensional ground space. Thus c is bounded by twice the absolute
inelastic cross matrix element. Split it at lambda. Cauchy--Schwarz bounds
the low-energy part by sqrt(mu_F mu_B), at most (mu_F+mu_B)/2. On energies
above lambda insert (H-E0)^(1/2) on both vectors and its inverse between
them. This part is at most sqrt(M_F M_B)/lambda. The same argument applies
to Hilbert--Schmidt vectors for the normalized ground trace. This proves
(15), including degeneracy.

The use of rho0 is material: for an arbitrary pure vector in a degenerate
ground space the elastic commutator need not vanish. Replacing inelastic
weight by ordinary connected variance would conceal this issue.

If c>0, set Delta=2 sqrt(M_F M_B)/c. At lambda=2 Delta, (15) gives total
inelastic weight at least c/2. Upper bounds for the moments and a lower
bound for c may replace them here. This establishes weight at an energy
scale, not a pole, sharp dispersion, particle interpretation or Gaussianity.

## 5. Explicit homogeneous transverse mode

Choose wave number k=2pi m/L in the z direction, with k neither 0 nor pi,
and s=2|sin(k/2)|. Use a normalized cosine w on xz plaquettes and a
normalized sine v on x links such that Cv=s w. Concretely for 0<k<pi,

    w_(xz,x)=sqrt(2/V) cos(k z),
    v_(x,x)= -sqrt(2/V) sin[k(z-1/2)].                 (16)

The xz curl convention is v_x(x)-v_x(x+zhat) when v_z=0.
Let rho=rho_(xz), c_x=cos theta_(xz,x), and
Gamma_z=rho0(c_0 c_zhat). Translation invariance gives exactly

    2a M_B=e_x {s^2 Gamma_z+rho0[(c_0-c_zhat)^2]}
                  +e_z rho0[(c_0-c_xhat)^2].           (17)

For a,b in [-1,1], (a-b)^2<=2[(1-a)+(1-b)]. Therefore Gamma_z<=1 and

    2a M_B <= e_x s^2+4(e_x+e_z)rho,
    2a M_F <= b_(xz) s^2+d_x g^2,
    d_x=2||T_x||_*,    c=s(1-rho) if rho<1.            (18)

Consequently, when rho_bar:=epsilon_L g^2/b_(xz)<1, define

    D_L(k,g)= sqrt[(b_(xz)s^2+d_x g^2)
                      (e_x s^2+4(e_x+e_z)rho_bar)]
                  /[a s(1-rho_bar)].                  (19)

At energy lambda=2 D_L, the combined inelastic measure in (15) is at
least s(1-rho_bar)/2. All constants are independent of volume except the
explicit bounded epsilon_L and allowed momentum grid.

For unit weights in (10), the simpler valid expression is

    D_L <= sqrt[(s^2+2g^2)(s^2+80g^2)]
                  /[a s(1-10g^2)],  10g^2<1.          (20)

The right side is O(s/a) when g/s is small. Its minimum over continuous s
is O(g/a); a sufficiently fine momentum grid attains that order. No bound
here tends to zero with k at fixed g. In particular the charged response
and compact fluctuations in (18) have not been discarded.

## 6. Local wave packets rather than a plane-wave limit

Let integer R>=3 and set

    h_R(n)=sqrt[8/(3R)] sin^2(pi n/R),  0<=n<=R,
    h_R(n)=0 otherwise.

Place the support away from periodic wrapping. Let v have only an x-link
component v_x(x,y,z)=h_R(x)h_R(y)h_R(z), and put w=Cv/s_R, where s_R=||Cv||.
The required geometry is a finite patch, contained in any L>=R+3 torus.
Direct difference sums give

    ||v||=||w||=1,
    s_R^2=(8/3)sin^2(pi/R),
    t_R^2:=||C^* w||^2=(20/3-4/R)sin^2(pi/R).          (21)

For completeness, in one dimension
||d h_R||^2=(4/3)sin^2(pi/R) and
||d^*d h_R||^2=(16/3)(1-1/R)sin^4(pi/R).
The x component of C^*Cv contains the y and z Laplacians; the other two
components contain mixed x-y and x-z differences. Squaring their product
norms gives (21). The endpoint half contributions to the one-dimensional
second difference must be retained.

Let e_max,b_max,d_max be the corresponding coefficient bounds, and let
rho_bar=max_j epsilon_L g^2/b_j<1. Since w=Cv/s_R,
c>=s_R(1-rho_bar). On a periodic cubic graph ||C^*||^2<=12. Writing
w cos theta=w+w(cos theta-1), the triangle inequality in the ground-state
L2 norm, together with (1-cos theta)^2<=2(1-cos theta), gives

    2a M_F <= b_max s_R^2+d_max g^2,
    2a M_B <= e_max [t_R+sqrt(24 rho_bar)]^2.           (22)

Define

    D_R= sqrt[e_max(b_max s_R^2+d_max g^2)]
                     [t_R+sqrt(24 rho_bar)]
                 /[a s_R(1-rho_bar)].                 (23)

Then the same exact finite-box physical probes have combined inelastic
weight at least s_R(1-rho_bar)/2 below energy 2D_R. This is uniform over
all surrounding volumes L>=R+3. Since s_R,t_R are comparable to R^-1,
D_R is O([R^-1+g+g^2 R]/a). Taking R of order g^-1 gives O(g/a), with
inelastic weight bounded below by a constant times g.

For example, for the unit-weight paired Wilson model, take 0<g<=1/10,
R=ceil(2/g), and any L>=R+3. Equations (11),(21)--(23) imply the explicit
statement

    mu_F((0,60g/a])+mu_B((0,60g/a]) >= g.              (24)

Indeed rho_bar=10g^2<=1/10, s_R<=pi sqrt(8/3) g/2,
t_R<=pi sqrt(20/3) g/2, and, since R>=20,

    s_R >= (99/100) pi sqrt(8/3) g/(2+g).

The last inequality follows from sin x>=x(1-x^2/6) for 0<=x<=pi/20.
These estimates give D_R<27g/a and s_R(1-rho_bar)/2>g (the relaxed
constants follow already from 3.14<pi<22/7). Thus (15) at 60g/a proves
(24). The constants are conservative analytic bounds, not fitted values.

The probes have finite support for every fixed g and R. Nevertheless an
infinite-volume *inelastic* statement still requires control of the limiting
ground projection: finite-volume excitation weight may collapse to zero
energy. No thermodynamic uniqueness, absence of elastic weight, clustering,
massless particle, or fixed-positive-g phase is inferred here.

## 7. What this changes and what remains open

The prior fixed-box oscillator analysis had constants allowed to grow with
L. Here (8), (19), and (23) are bounds on the full interacting compact
Hamiltonian with explicit volume-uniform constants. Their new input is the
exact Gauss-neutral trial and a spectral lower bound using two probes,
instead of an assumed static variance.

The remaining fixed-g infrared task is stronger: control the current and
compact fluctuation contributions at energies and momenta much smaller
than g, in the same physical state, while preventing all proposed photon
weight from being elastic or part of a different low-energy continuum.
The present inequalities do not perform that separation. They also make
no claim of fermion stability, law selection, gravity or an axiom update.

## Verification status

The [finite checker](../evidence/block01_uniform_response_check.py) and
[paired output](../evidence/block01_uniform_response_check.json) challenge
the Poisson normalization and derivative, literal integer Gauss constraint,
shift overlap, CAR hopping norm, sparse cubic curl, translated compact
field ensemble, and spectral inequality with degenerate ground space.
The largest geometric identity error in its initial run was below3e-15;
the direct/dual moment discrepancy was below4e-15. These are floating-point
challenges, not interval certificates or an execution of the general proof.
No cutoff rotor was substituted for the domain statements above.

The accompanying working note records the target before testing. Personal
adversarial review and its exact input hashes are in review/. All checks
are by the same author; independent mathematical review remains required.
Primary-source reading limits are in the campaign ledger.
