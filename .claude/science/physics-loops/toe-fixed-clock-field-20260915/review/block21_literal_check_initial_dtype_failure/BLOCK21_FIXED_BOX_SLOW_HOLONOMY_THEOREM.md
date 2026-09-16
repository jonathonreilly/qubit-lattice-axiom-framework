# Fixed-box slow holonomy levels with the fast gauge modes retained

Provisional author derivation, 2026-09-16 UTC. No independent audit. This supplies
a fixed-volume leading slow spectrum under explicit isolated-minimum hypotheses.
Its constants depend on the box. It does not supply an interacting thermodynamic
phase, a joint volume/coupling limit, or a fixed finite-payload theorem.

## 1. Exact model and hypotheses

Start with the exact integer-Gauss representation in the periodic-holonomy parent
on main e0ef7cf4633034a8c1e6d57f5812cc4275bf1349, reread in full. On a fixed finite
connected graph with c independent cycles and finite neutral matter space M,

    a H_g = (g^2/2)(C D_theta+E0)^T W_E(C D_theta+E0)
                 +V(theta)/g^2 +h(theta),
    D_theta=-i partial_theta, theta in T^c,
    K=C^T W_E C>0, V=sum_p w_p[1-cos(z_p.theta)].                 (1)

The original CAR hopping signs, charge-dependent integer E0 and matter sector
are retained. This is the untruncated rotor operator. The same representation
works for paired opposite charges: rho_f=Q_f instead of N_f-eta, with the
integer-neutral finite matter space and corresponding hopping shifts. The fixed
matrix h is smooth/analytic. An onsite Q^2 term may be included generally, but
it is set to zero in the free-Wilson application below.

Assume the magnetic minima form one connected flat d-torus Mflat, with constant
positive normal Hessian and no other zero set. The periodic cubic case has d=3.
Assume the lowest eigenvalue e(t) of h restricted to Mflat has a unique global
minimum t_*, is simple with a positive matter gap in a neighborhood of t_*, and
has positive definite Hessian B there. Matter degeneracies elsewhere on Mflat
are allowed. All these are fixed-volume hypotheses, not assumed uniform in L.

In linear normal/tangent coordinates (q,t), block the constant kinetic matrix as
K0=[[Kqq,Kqt],[Ktq,Ktt]]. The shear t'=t-Ktq Kqq^-1 q leaves q and V unchanged
and diagonalizes the kinetic matrix into Kqq and

    S=Ktt-Ktq Kqq^-1 Kqt>0.                                      (2)

On Mflat, t'=t. The NORMAL coefficient is Kqq, not the opposite Schur complement.
The latter mistake changes the fast oscillator floor, as the parent warns.
Let Aqq be the normal Hessian of V and

    Eperp=(1/2) tr sqrt(Kqq^(1/2) Aqq Kqq^(1/2)).                 (3)

Let mu_j, counted WITH multiplicity from j=0, be the eigenvalues on R^d of

    Hslow=-(1/2)partial_y^T S partial_y+(1/2)y^T B y.              (4)

The proposed fixed-volume theorem is

    a E_j(g)=Eperp+e(t_*)+g mu_j+o(g)                            (5)

for every fixed j as g->0. The first gap divided by g tends to the smallest
square root of an eigenvalue of S^(1/2) B S^(1/2), divided by a. Degenerate
slow levels are permitted; no preferred basis or higher series is asserted.

## 2. Exact local connection and the even normal well

Complete the electric square: A_f=K^-1 C^T W_E E0(f), with a nonnegative
longitudinal remainder. The connection components are diagonal in occupations
and commute. On a simply connected chart exp(-i A_f.theta) removes them exactly.
The transformed h remains smooth and has the SAME pointwise eigenvalues on Mflat.
The longitudinal term is bounded times g^2. No global periodic gauge is asserted.
Subsequent matter eigenvectors can have a Berry connection; it is controlled below.

After the shear, V depends only on q and is even. Fix a sufficiently small
symmetric normal ball, with Dirichlet boundary, on which V>=c|q|^2. The scalar
exact normal operator is

    N_g=-(g^2/2)partial_q^T Kqq partial_q+V(q)/g^2.                (6)

It has a positive even normalized ground function chi_g, and, for small g,

    lambda0(N_g)=Eperp+O(g^2),
    lambda1(N_g)-lambda0(N_g)>=delta_perp>0,
    integral |q|^(2r)|chi_g|^2 <=C_r g^(2r), r=1,2,... .          (7)

For completeness rescale q=g x. The quadratic lower bound confines x. A cutoff
oscillator Gaussian gives a bounded ground energy. The ground-state transform
with |x|^r, regularized at zero as needed, bounds the next even moment by lower
moments and a derivative term controlled by the largest eigenvalue of Kqq.
Induction bounds all fixed moments. Dirichlet boundary values make these form
tests admissible. Positivity and simplicity make chi_g even on the symmetric ball.
The cosine remainder satisfies
|V(gx)/g^2-x^T Aqq x/2|<=C g^2 |x|^4 there. Moments and a cutoff of the ground
vector compare it with the full oscillator with O(g^2) error; cutoff errors are
arbitrarily high powers of g by higher moments. The Gaussian gives the converse
bound. Rellich, confinement and smooth recovery functions give convergence of
the first two normal eigenvalues, leaving a positive normal gap.

Using the EXACT normal ground avoids a coarse O(delta^2) floor error that would
overwhelm the order-g term. This is essential in this two-scale problem.

## 3. Normal matter coupling costs order g^2 in energy

Use h(q,t) for the locally transformed/sheared matrix. Uniformly in a fixed chart,

    h(q,t)=h(0,t)+sum_i q_i h_i(t)+O(|q|^2).                     (8)

For P=|chi_g><chi_g| tensor I_M and Q=1-P, parity and (7) give

    ||P[h(q,t)-h(0,t)]P||<=C g^2,
    ||Q[h(q,t)-h(0,t)]P||<=C g.                                 (9)

On the fixed normal ball the full perturbation norm is at most C delta. Choose
the radius small relative to the fixed normal gap, then take g small. Pointwise
in t, completing the P/Q block square gives the form bound

 N_g+h(q,t) >= lambda0(N_g)+e(t)
       +P[h(0,t)-e(t)]P+(delta_perp/4)Q-C' g^2 P.                (10)

Retain part of the Q gap to absorb the O(g) off-diagonal block, at cost
O(g^2/delta_perp). Bounded longitudinal terms change only O(g^2). This needs
neither commuting matter matrices nor a matter gap everywhere on Mflat.
A scalar bound linear in |q| would give O(g), which is insufficient; evenness
and the block estimate are the missing improvement.

The tangent kinetic term commutes with P because chi_g is t-independent. It can
be added before integrating (10) over t. Outside a chart around t_*, e(t)-e(t_*)
has a positive minimum. States of excess energy O(g) therefore concentrate near
that chart and in P.

## 4. Slow min-max convergence with the matter connection retained

Near t_* choose a smooth normalized ground eigenvector u(t). Decompose the P
component as u(t) f(t)+eta(t), with u^*eta=0. The local matter gap controls eta.
A derivative projected on u is

    u^* partial_t[u f+eta]=partial_t f+(u^*partial_t u)f
                                           -(partial_t u)^* eta. (11)

Both connection coefficients are bounded. Applying
|a+b|^2>=(1-epsilon)|a|^2-C epsilon^-1|b|^2 with epsilon=sqrt(g) bounds the
tangent kinetic form below by (1-sqrt(g)) times the scalar principal form on f,
minus C g^(3/2) times the norm. Berry and off-band derivative terms are thus
o(g), not assumed absent from a future g^2 coefficient. The unused forms are
nonnegative. Equations (7),(10), the matter gap and a scalar partition with
IMS cost O(g^2) give the localized lower estimate.

Set y=(t-t_*)/sqrt(g). Positive Hessian gives tight second moments in y and the
derivative estimate gives a local H1 bound on scaled f. The Q and eta norms
tend to zero. Rellich on fixed balls plus the moment bound gives strong L2
compactness. Taylor expansion of e, first on fixed y-balls and then by exhaustion,
gives (4). Orthogonality survives the strong limit, so min-max gives the ordered
lower bound with multiplicities. A small residual alone is not used to count levels.

For the upper bound multiply chi_g(q), u(t) and finitely many cutoff Hermite
functions of (4), scaled by sqrt(g). Equation (9) makes the averaged normal
matter error O(g^2), the tangent connection costs o(g), and the tangent cubic
Taylor remainder is O(g^(3/2)). Their finite span has the correct norm and
Rayleigh matrix. Min-max proves (5). No optimal uniform power-law error is asserted.

Globally use finitely many linear tubular charts and fixed-radius partitions,
at IMS cost O(g^2). Off the tube, V/g^2 excludes low energies. The same normal
construction gives the floor in every flat chart, even at matter degeneracies.
The normal radius can be chosen uniformly over this FIXED compact flat torus.
Localized functions have Dirichlet normal boundary values. Upper trials stay
inside the single minimizing chart. The global bundle need not be trivialized.

## 5. Paired Wilson application and the iterated limit

For positive electric weights W_E=diag(w1,w2,w3) by direction on an L^3 cube,
a harmonic connection is A_(x,i)=phi_i/L and conjugate uniform flux is
E_(x,i)=n_i/L^2. Every zero-average transverse or longitudinal part is orthogonal
to this uniform flux in the weighted form: w_i is constant in each direction.
Also sum_links E dA=sum_i n_i dphi_i. Hence the tangent principal matrix is

                       S_L=W_E/L.                              (12)

Charge offsets produce a connection, not a different principal metric.
Positive normal frequencies are the weighted curl frequencies. Their minimum
and the matter gap are positive at each fixed finite L but vanish as L grows.
This is why the preceding proof is not automatically uniform.

Take Block20's paired Wilson coefficients, u=0, b=kappa=pi/3, without another
matter interaction. For all sufficiently large L=6m or6m+3, Block20 gives a
unique minimizing flat twist phi_*, no grid node there, a simple neutral filled
ground, and a positive Hessian B_L of the DIMENSIONLESS free energy. Therefore
(5) applies to the actual coupled integer-rotor/matter Hamiltonian at each such
fixed L. Let nu_i(L) be the square roots of the eigenvalues of
W_E^(1/2) B_L W_E^(1/2)/L. Then

    lim_(g->0) a[E1(g,L)-E0(g,L)]/g =min_i nu_i(L).               (13)

Since L B_L tends to H_F, the Hessian of 4K_G at pi, in either subsequence,

    lim_(L->infinity along either subsequence) lim_(g->0)
       a L [E1(g,L)-E0(g,L)]/g
           =sqrt(lambda_min(W_E^(1/2) H_F W_E^(1/2))).           (14)

For unit weights Block20's quadrature gives
H_F=diag(0.4418297127,0.4418297127,0.1579285375). The exact constants are its
convergent heat integrals. This is an ITERATED limit. No sufficient g(L),
growing-volume error, hard/cyclic cutoff rate, charged-pole statement or local
photon correlation theorem follows.

Block20 left the interacting reduction open when written. This result closes
its leading fixed-volume version under the stated hypotheses. The uniform
version remains substantive. The slow global gap can coexist with a local
phase whose existence and nature have not been established.

## 6. Companion discriminator and inherited status

A two-coordinate matrix fixture retains a fast cosine well, rotating two-state
matter eigenvectors, noncommuting normal coupling, and diagonal charge connections.
Its metric Kqq=4,Kqt=1,Ktt=2 gives Eperp=1 and S=7/4. This is not a cubic gauge
model. Its finite spectra challenge the metric and Berry-order identification;
they do not prove the general min-max argument. The model and tolerances are
frozen before running. All new arguments require independent review before
retention. No framework axiom or primitive is modified.

