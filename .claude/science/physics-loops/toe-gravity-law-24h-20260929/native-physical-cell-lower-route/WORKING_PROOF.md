# Internal matrix pin capacity on the actual qubit amplitudes

Author derivation, September30. This is a provisional research argument,
awaiting new literal controls and a focused independent proof check. It uses
the unchanged supplied native Hamiltonian at main30a9461, whose source SHA is
7180c065165cb5db45f3405fcc9711ec38145a3d2391962ed767d55f4cc25ee0.
The earlier Neumann report a837bb64 and root check67b6b7e5 provide the exact
isolated-dimer count, scalar lower result and regularized auxiliary gap.
They do not provide the new matrix Green convergence proved below. No
physical law, state, clock, threshold eigenvalue or primitive is selected.

The proposed new conclusion, for arbitrary states of mean density rho, is

    liminf_(rho down0) liminf_(L to infinity) <H0>/(L^3 rho^2)
       >= c_pin/4,
    c_pin=lambda_min(U* G(0)^(-1) U),
    G(x)=integral_BZ exp(ik.x) K(k)^(-1) dk/(2pi)^3.       (1)

The inner lower limit is uniform over states with that mean density; this is
not the fixed-N limit. K is the actual one-pair S+W form on nine forward
bond amplitudes, and U is its five-dimensional normalized constant soft
space. This is a relaxed one-pair pin capacity, not the full15 interacting
threshold T0, a matching EOS, or a physical many-particle cell Hamiltonian.
The stronger compatible full-T0 lower law remains open.

## 1. Exact positive comparison and symbol

Let a=min(tau,mu/12), b=2mu+24tau, mu,tau>0. Forward graph bonds are2e_i
and e_i+eta e_j (i<j, eta=+/-1), each physical graph edge represented once.
For any full physical occupation residual eta, put
f_(eta,d)(x)=<eta|b_x b_(x+d)|psi>. All pair-removal amplitudes retain the
same input state and complete residual. The sum of their actual literal
S/W row energies is <S+W>. The previously proved fifteen-bare-gradient
bound implies, in particular, the nine-forward-gradient comparison

    S+W >= a Egrad_9.

Fix0<epsilon<=1/2. Split S+W into1-epsilon and epsilon portions. On each
anchor cube Lambda of side ell retain complete literal S/W rows whose all
anchors belong to Lambda, with coefficient1-epsilon; add epsilon*a times
every internal nine-component Neumann gradient. Call this K_Lambda,e.
No row is selected twice between disjoint anchor cubes. The diagonal
physical Ddiag, including all original neighbors, remains untouched.
Thus H0 dominates the sum of these residual/cell quadratic forms.
This is an amplitude comparison, with no assumed physical tensor-cell
factorization and no deletion of a physical neighbor.

The infinite operator is K_e=(1-epsilon)K+epsilon*a Delta I9. The earlier
complete argument gives

    a Delta I9 <= K_e <= K <= b I9,
    (1-epsilon)K <= K_e,
    ker K_Lambda,e = constant U,
    Delta_cell >= epsilon*a/(14 ell^2), ell>=3.          (2)

For clarity, the literal symbol can also be computed directly. Put
l(k)=4 sum_i sin^2(k_i/2), v_i=exp(-ik_i). Axial centered pair amplitudes
are v_i f_i, whence

    K_ax=2mu P_v + tau l(I-P_v), P_v=v* v/3.

For plane ij, each forward type eta has two signed centered appearances
-eta exp(-i eta k_j)f_eta and -eta exp(-ik_i)f_eta. Define
q_eta=-eta[exp(-i eta k_j)+exp(-ik_i)]/2. The four-row identity gives

    K_ij=2mu I2+(tau l-mu) q* q,
    ||q||^2=1+cos(k_i)cos(k_j).

Its two eigenvalues are2mu and
mu[1-cos(k_i)cos(k_j)]+tau l[1+cos(k_i)cos(k_j)]. At zero, normalized U
has axial columns(1,-1,0)/sqrt2,(1,1,-2)/sqrt6 and one(-1,+1)/sqrt2
column per plane (order eta=+1,-1). These formulas require the planned
literal-word control; no previous runner builder is imported into it.

## 2. Uniform finite-cell L6 energy estimate

For f orthogonal to the constant-U kernel, write f=m+q with q having zero
spatial mean and m in U-perp. There is an ell-independent scalar/vector
Neumann Sobolev estimate

    ||q||_6 <= C ||grad q||_2.                            (3)

One direct proof reflects a mean-zero cube function into a three-times
larger cube, multiplies by a cutoff of derivative O(ell^-1), and extends
by zero to Z3. Its gradient is bounded by
C(||grad q||_2+ell^-1||q||_2); the Neumann Poincare bound absorbs the last
term. The infinite discrete Sobolev inequality follows from the elementary
BV estimate ||g||_(3/2)<=C sum_i||D_i g||_1: along each coordinate, the
telescoping line sum bounds |g|, and applying Cauchy-Schwarz successively
to the three products proves the discrete Loomis-Whitney inequality.
Apply this BV estimate to g=|q|^4; the edge difference is bounded by
4(|q_x|^3+|q_y|^3)|q_x-q_y|. Holder then gives
||q||_6^4<=C||q||_6^3||grad q||_2. The same proof uses the vector norm.

All centered S rows in the inner cube are present. The already established
literal row estimate (S<=2mu I on the infinite nine-component space) is

    ell^3 |m|^2 <=27 S_inner(f)/mu+54||q||_2^2.           (4)

Since ||m||_6=ell^(1/2)|m|, multiplying (4) by ell^-2 and using Poincare
and (2) controls its L6 norm by C_e E(f)^1/2. Equation(3) does likewise
for q. Therefore, uniformly in ell,

    ||f||_6 <= C_e <f,K_Lambda,e f>^1/2,
    f perpendicular constant U.                         (5)

The infinite energy completion has the analogous L6 embedding from
K_e>=a Delta. Point evaluation, or any fixed finite linear combination
of evaluations, is continuous there. Its Riesz solution and Green
compression are consequently defined without assuming an l2 inverse.

## 3. Uniform matrix Green convergence away from faces

Write G_Lambda,e(x,y) for the point blocks of K_Lambda,e^+, with its
constant-U kernel removed. Consider a source r supported at at most two
points, each at distance w from every face. Constants below are uniform
in their separation and in ell>=w; w is sufficiently large for fixed row
diameter. For each point choose a radial cutoff equal to1 through
r_-=w^(1/4), zero beyond r_+=w^(1/2), and linear in log radius between.
Use eta=1-(1-eta_1)(1-eta_2) for two points. It equals1 at both sources,
has support of volume O(w^(3/2)), and

    ||grad eta||_3 <= C (log w)^(-2/3).                  (6)

Indeed its cubed gradient sum is O[(log(r_+/r_-))^-3
sum_(r_-<=r<=r_+) r^-1]=O((log w)^-2). Fixed translates and finite row
differences obey the same bound. All rows meeting its support are genuine
interior rows when w is large. For any literal finite-range row R, choose
one anchor x_R; expand R(eta f)=eta(x_R)Rf+[R,eta]f. The bounded number
of terms per row and Holder imply

    sum_R ||[R,eta]f||^2
       <= C ||grad eta||_3^2 ||f||_6^2.

Thus, for the finite mean-soft-complement function or the infinite energy
function, the cutoff energy in the other domain satisfies

    E(eta f) <= [1+C_e(log w)^(-2/3)] E(f).              (7)

This follows by the triangle inequality for the vector of all row outputs,
then squaring. It does not divide a pointwise residual by the ell^-2 gap.
Terms with all anchors outside the cutoff have zero output; rows crossing
the cell faces have all cutoff values zero.

Let q_L(r)=<r,K_Lambda,e^+r>, q_inf(r)=<r,K_e^-1 r>. In the finite
variational problem the source is automatically projected off constant U.
Use f=K_Lambda,e^+r, cut it, and optimize its scalar coefficient in the
infinite energy variational principle. Its source pairing is exactly q_L,
so (7) gives q_L<= (1+s_w)q_inf, s_w=C_e(log w)^(-2/3).

Conversely cut the infinite Riesz response and project the result off
constant U in the cell. Projection changes no finite energy. The pairing
changes by at most

    C ||r|| ell^-3 ||eta f||_1
      <= C ||r|| ell^-3 w^(5/4)||f||_6
      <= C w^(-7/4)||r||^2.                             (8)

The last bound uses ell>=w and the uniform point-source energy bound
q_inf<=C||r||^2. Optimize again; for q_inf smaller than the error use
q_L>=0. Otherwise (q_inf-error)^2/[(1+s_w)q_inf] supplies the desired
bound. The finite upper bound is uniform as well by(5). Polarization of
one-point and two-point sources proves

    ||G_Lambda,e(x,y)-G_e(x-y)||
       <= C_e (log w)^(-2/3).                            (9)

The cutoff estimates hold for complex vectors. There is no hidden
restriction to diagonal Green blocks or fixed pin separation.

## 4. Infinite off-diagonal decay and capacity comparison

The literal symbol is analytic. Relative to its zero-momentum soft/high
decomposition, the soft block is O(|k|^2), the cross block O(|k|), and
the high block is boundedly invertible near zero. The first assertion
follows also from positivity and vanishing on the soft space at k=0.
The analytic soft Schur complement has order2 and is bounded below by
c a|k|^2 I: minimize the full quadratic form over the high component and
use K_e>=a l I. Differentiating the Schur inverse and block inverse gives

    ||partial^alpha K_e(k)^-1|| <= C_(e,alpha)|k|^(-2-|alpha|).

Away from zero it is smooth and invertible. A dyadic partition at radius s
has Fourier L1 size O(s) and, after integration by parts J times, bound
C s(1+s|x|)^-J. Summing dyadic s proves

    ||G_e(x)|| <= C_e/(1+|x|).                           (10)

This derivative argument, not scalar ellipticity alone, establishes the
matrix decay. The symbol inverse is integrable in3D.

Set G=G_e(0). It is positive definite, G>=I9/b and G<=g I9/a, where
g=int_BZ l(k)^-1 dk/(2pi)^3. Suppose m physical common pins y_i in a
cell are mutually R-separated and distance w from its faces. Equations
(9)-(10) imply for their block Green matrix Gamma

    ||Gamma-I_m tensor G|| <= zeta,
    zeta=C_e m [R^-1+(log w)^(-2/3)].                    (11)

This is the crude block-row norm; no optimistic cancellation is used.
Write a field vanishing at all pins as f=Uz+q with q orthogonal constant U.
For v=G^-1 Uz, the source at all pins with value v has pairing with q
equal to -m v*Uz. Energy Cauchy-Schwarz and(11) give

    E(f) >= m (z*U*G^-1 Uz)/(1+b zeta)
          >= m c_e |z|^2/(1+b zeta),
    c_e=lambda_min(U*G^-1 U).                           (12)

Explicitly the source Green quadratic form is at most
m[v*Gv+zeta|v|^2]<=m v*Gv(1+b zeta), since ||G^-1||<=b. No inverse
of the entire many-pin Gamma is required. The gap in(2) then yields

    E(f) >= m c_e ||f||^2/[ell^3 D_cell],
    D_cell=1+b zeta_max+M c_e/(ell^3 Delta_cell),
    zeta_max=C_e M[R^-1+(log w)^(-2/3)],
    M=8ell^3/R^3,                                      (13)

where m<=M and the m=0 case is trivial. Also0<c_e<=b. All constants
here may depend on fixed mu,tau,epsilon, never on density or volume.

## 5. Full-carrier extraction and scale order

Use the unchanged physical mesoscopic lemma
<B_R><=C_B R^3 <H0>/a, C_B=28000322, where B_R counts particles outside
R-isolated graph dimers. Its hypotheses are R>=10,L>=10R. Tile complete
anchor cubes, with L>=4ell and ell>=3R. For each residual choose one
endpoint of every residual R-isolated dimer wholly in a cell w-interior.
These are simultaneous common pins of all nine f_(eta,d): annihilation
at an already occupied residual site cannot have produced that residual.
Their separation is>R. Every complete retained row and each internal
gradient is used at most once. The original physical diagonal term is
not changed, and arbitrary bonds reaching outside an anchor cube remain
valid amplitudes with the complete environment retained.

For any original occupation S, let g_j(S) count its R-isolated dimers in
the jth interior. Removing one leaves the other g_j-1 available pins.
The exact diagonal counting identity therefore supplies

    sum_eta m_(eta,j)||f_(eta,j)||^2 >= <g_j(g_j-1)>.

There is no factor1/2 on the right: this counts ordered choices of a
removed dimer and a surviving pin. Other removed bonds contribute
nonnegatively, and each annihilation output has a unique input. The
argument applies to all superpositions and density matrices.

Average translations of the whole tiling. For at least one translate,
the lost particle expectation is at most theta<N>, with
theta<=3ell/L+6w/ell. Then Gtot=sum_j g_j satisfies
<Gtot>>=(<N>-<B_R>)/2-theta<N>, while Gtot<=N/2. Jensen and the number
of complete cells give sum_j<g_j(g_j-1)> >= <Gtot>^2/n_cells-<N>/2.
Consequently (13) proves the finite-state inequality

    e >= (c_e/D_cell)[rho^2(1-beta)_+^2/4-rho/(2ell^3)],
    beta=C_B R^3 e/(a rho)+2theta,
    e=<H0>/L^3, rho=<N>/L^3.                            (14)

Fix epsilon first. For small rho put h=loglog(1/rho),
ell~rho^(-1/3)h, R~rho^(-1/3)/h, w~rho^(-1/3), with integer rounding.
Then M=O(h^6), rho ell^3~h^3, rho R^3~h^-3, w/ell~h^-1,

    M/R ->0, M(log w)^(-2/3)->0, M/ell ->0.

Hence D_cell->1. For states with e<=b rho^2, beta->0 after L->infinity
and then rho->0. The states with e>b rho^2 already exceed the desired
c_e rho^2/4 because c_e<=b. Thus no low-energy assumption remains in
the resulting bound c_e/4. The lower-order subtraction is retained until
rho ell^3->infinity. This excludes an illicit fixed-N2 limit.

Finally (1-epsilon)K<=K_e<=K implies
G_0<=G_e<=G_0/(1-epsilon). Therefore
(1-epsilon)c_pin<=c_e<=c_pin. Send epsilon down0 only after the two
preceding limits to obtain(1).

## 6. Relation to the older scalar coefficient

The weak comparison G_0<=g I/a already gives c_pin>=a/g, recovering the
older coefficient. In fact the inequality is strict for fixed mu,tau>0.
To verify this, integrate the positive matrix difference
(a l)^-1 I-K(k)^-1. If a<tau, the axial block has strictly larger
eigenvalues than a l for small nonzero k. If a=tau, the difference in
that block is strictly positive on the moving axial singlet for small
nonzero k. No nonzero constant axial vector is orthogonal to v(k) on an
open neighborhood, because its three distinct Fourier monomials are
linearly independent. Each plane block is strictly above a l I for an
open small-k set (use its displayed two eigenvalues, with coski coskj
positive). Every nonzero constant nine-vector therefore has positive
integrated difference. Finite dimension implies G_0<g I/a and

    c_pin>a/g.                                         (15)

This is a strict symbolic improvement, without a claimed certified numeric
gap. For optional diagnostic evaluation, cubic symmetry splits the capacity
into an E doublet and T triplet. If g_diag=int exp[i(ki-kj)]/l, then
gamma_E=(2g+g_diag)/(3tau)+1/(6mu). With
lambda=mu(1-coski coskj)+tau l(1+coski coskj) and
p=(1+cos^2kj+2coski coskj)/2,
gamma_T=1/(2mu)-int (tau l-mu)p/(2mu lambda).
Thus c_pin=min(1/gamma_E,1/gamma_T). The integrals are normalized over
the Brillouin zone; k=0 has an integrable singularity. A finite grid value
would be a diagnostic only, not a certified integral or a threshold value.

## Unproved campaign obligations and check status

This authored argument has not yet received its planned literal symbol/
finite Green controls or a focused independent check. In particular those
checks must verify finite-cell Sobolev extension, complex variational
projection, Green constants uniform over two pins, exact row selection,
all physical counting and the slow scale hierarchy. It does not assert a
compatible full15 T0 interaction lower bound, growing-particle Schur limit,
matching EOS, condensate, record observables or an axiom inconsistency.
