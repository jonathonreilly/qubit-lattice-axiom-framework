# Exact smoothing and filtering of a finite-clock Villain law

Personal campaign derivation, 2026-09-15. Provisional author result, not
independently reviewed or retained. Frozen main for the exercise:
5deabeb698a27c2c3f68c5df685af2521ef15307. This construction does not use the
proposed quantum Hamiltonian result in PR8135. The microscopic probability law
below is supplied; no axiom selects it in this note.

## 1. Domain and exact target

Let a finite free four-dimensional cubic box have oriented vertex, edge,
plaquette and three-cell cochain spaces, with coboundaries G, D and B. Thus
DG=0 and BD=0. Transposes use counting inner products. There are E edges and
P plaquettes. The free box is contractible. Harmonic sectors on a torus are
outside this statement.

Fix an integer N>=2 and beta>0. Both remain fixed in every proposed
thermodynamic or scaling limit. Put delta=2pi/N. For link representatives
a in {0,delta,...,(N-1)delta}^E and image integers k in Z^P, define

    F = D a - 2pi k,       X = sqrt(beta) F,
    Z_clock = N^(-E) sum_a sum_k exp(-||X||^2/2).

The probability measure uses the displayed weight divided by Z_clock.
The physical lifted magnetic defect is Bk; BX=-2pi sqrt(beta) Bk. The
integer image is part of the measure. No replacement by principal angles
or an image-summed observable is implicit.

We construct a probability-kernel pushforward to continuous links with the
same magnetic defects, an exact positive electric correction, and the same
limiting smooth flux tests if either limit exists. Uniform smooth local
bounds on an extension of the correction are a separate step below. A
photon limit and state identification are further obligations.

## 2. Add link noise with the full folding correction

Let xi be an independent centered edge Gaussian with covariance s^2 I,
s>0. Write a+xi=theta+2pi ell, with theta in [0,2pi)^E and ell integer.
Set k'=k-D ell. Then, exactly,

    F_s = D theta - 2pi k' = F + D xi,
    X_s = X + sqrt(beta) D xi,       Bk'=Bk.

In particular, the sign in k'=k-D ell is fixed by this equality. To compute
the joint density of (theta,k'), put z=a-2pi ell. The pair (a,ell) runs
bijectively through delta Z^E, and the original flux is D z-2pi k'.
Relative to Haar dtheta/(2pi)^E and counting k', the density is

    (2pi)^E / [Z_clock N^E (2pi s^2)^(E/2)]
      times sum_{z in delta Z^E}
      exp[-||theta-z||^2/(2s^2) - beta||D z-2pi k'||^2/2].       (2.1)

Define positive matrices and a real, unwrapped link variable

    tau = beta s^2,
    A = I + tau D*D,
    M = s^(-2) A,
    K = (I + tau DD*)^(-1),
    r = theta - beta M^(-1) D* F_s.

Completion of the square gives

    ||theta-z||^2/s^2 + beta||D z-2pi k'||^2
      = (z-r)*M(z-r) + beta F_s*K F_s.                          (2.2)

Here K=I-beta D M^(-1)D* and D r-2pi k'=K F_s. Poisson summation for the
full-rank lattice delta Z^E gives the strictly positive theta function

    Theta_M(r) = sum_{j in Z^E}
      exp[-N^2 j*M^(-1)j/2] exp[i N j.r]
      = delta^E sqrt(det M)/(2pi)^(E/2)
        sum_{z in delta Z^E} exp[-(z-r)*M(z-r)/2] > 0.

Substituting into (2.1), every volume and Haar factor cancels to give

    rho_s(theta,k') = exp[-beta F_s*K F_s/2] Theta_M(r)
                      / [Z_clock sqrt(det A)].                 (2.3)

The matrix M is strictly positive even on gradient link modes. No gauge
fixing or singular Gaussian determinant is used in this identity.

## 3. Filtering puts the theta on the new links

Fold r=psi+2pi eta and set k''=k'-D eta. Define

    Z = sqrt(beta)(D psi-2pi k'') = K X_s.                      (3.1)

The map is an invertible smooth map of the link/image bundle. On an
unwrapped chart its inverse is

    theta = r + tau D*(D r-2pi k'),

and its forward link Jacobian is det(A)^(-1). Equivariance under
(theta,k') -> (theta+2pi l,k'+D l) proves that chart changes introduce no
multiplicity. Images change by the displayed folding correction. Thus

    rho_filtered(psi,k'') = sqrt(det A)/Z_clock
      exp[- Z*K^(-1) Z/2] Theta_M(psi).                         (3.2)

Since BK=B, BZ=BX exactly. Moreover K^(-1)=I+tau DD* is finite range.
Filtering makes the electric factor depend only on the new continuous
links. It does not assert that the filtered field is Gaussian.

## 4. Gauge averaging and the physical flux carrier

Average (3.2) over Haar vertex angles phi, applying psi -> psi+G phi with
the corresponding folding of images. The flux Z and its Gaussian weight
are unchanged. The averaged electric factor is positive and equals

    Theta_g(psi) = sum_{j in J}
      exp[-N^2 j*M^(-1)j/2] exp[iN j.psi],
    J = {j in Z^E : G*j=0}.                                   (4.1)

The full flux distribution is unchanged by this average. Open charge-N
link observables need not be unchanged. This is a flux-law identification,
not equality of all microscopic link laws.

Each conserved integer edge current on a free cube has an integer face
filling S_j with D*S_j=j. On the physical carrier
Z=sqrt(beta)(D psi-2pi m), therefore,

    exp[iN j.psi] = exp[i g S_j.Z],       g=N/sqrt(beta).        (4.2)

If D*T=0 for an integer T, then g T.Z=-2pi N T.m is an integer multiple
of 2pi. Consequently (4.2) is independent of the filling on this carrier.
It is generally filling-dependent on an arbitrary real plaquette field.
This distinction is needed for the off-carrier smooth extension.

Equations (3.2)-(4.2) keep every magnetic image sector of the continuous
Haar Villain carrier. No magnetic neutrality, small-defect truncation, or
discarding of a complex electric/magnetic pairing is used.

## 5. A fixed smoothing scale and volume-independent massive bounds

For the remaining construction choose s^2=1/(64 beta), so tau=1/64. The
free incidence operator satisfies ||D||^2<=16, by embedding in the full
lattice and using the Fourier exterior-product symbol. On edges D*D has
absolute diagonal row sum at most 6 and off-diagonal sum at most 18. On
faces DD* the corresponding bounds are 4 and 20. Distances refer to the
L-infinity distance between the base vertices of cells. Nonzero matrix
entries connect cells at distance at most one. With weight 2^distance,

    ||tau D*D||_w <= 42/64,
    ||tau DD*||_w <= 44/64 = 11/16.

The weighted row/column Schur norm is submultiplicative. The Neumann series
therefore yields

    ||A^(-1)||_w, ||K||_w <= 16/5,
    ||M^(-1)||_w <= 1/(20 beta),
    (80 beta)^(-1) I <= M^(-1) <= (64 beta)^(-1) I.             (5.1)

Put c_e=1/(128 beta), C=M^(-1)-c_e I and A_e=N^2 C. Then

    3/(640 beta) I <= C <= 1/(128 beta) I,
    ||A_e||_w <= (37/640) g^2,
    a_e=N^2 c_e/2=g^2/256.

For a proper real Gaussian u with covariance A_e,

    exp[-N^2 j*M^(-1)j/2]
      = exp[-a_e||j||^2] E exp[i j.u].                         (5.2)

The Gaussian auxiliary covariance is massive. It is not the physical
flux covariance or a claimed photon state.

## 6. Local integer fillings and a positive extension

### 6.1 Fill each connected current, without a boundary import

Decompose j into components gamma under shared endpoint vertices of its
nonzero edges. Each component is separately conserved. Let
m_gamma=sum_e |j_gamma(e)| and let R_gamma be its coordinate bounding box,
including endpoints. Its diameter in the base-vertex L-infinity metric is
at most m_gamma. There is an integer face filling S_gamma inside R_gamma
with D*S_gamma=j_gamma and ||S_gamma||_1<=4m_gamma^2, as follows.

Let o_i be the minimum coordinate in direction i. At sweep i, replace a
transverse directed edge (x,k), k!=i, by its projection to x_i=o_i. Fill
the strip of (i,k) faces between the edge and its projection, with sign
+ if i<k and - if i>k and with the edge's integer coefficient. Edges in
direction i project to zero. The strip chain homotopy identity is

    boundary S_i = j_i - p_i j_i

for a conserved current j_i: endpoint connector terms cancel by zero
divergence. Projected currents remain conserved and their l1 mass cannot
increase. After four sweeps the current is zero. Each sweep costs at most
(diameter of R_gamma) times m_gamma, which proves the area bound. All
strips stay inside R_gamma, hence inside the original free cube. Negating
the current negates the filling.

For signed cubic covariance on arbitrary real Z, average the phases over
all 384 signed coordinate permutations of this filling rule, pulling each
filling back to the original coordinates. Write these fillings S_{gamma,h}.
Each has the same boundary, area and bounding-box bounds. On the physical
carrier all 384 phases are equal by (4.2). Off that carrier their average
defines an extension; it does not assert filling independence there.

### 6.2 Exact hard-core representation and positivity on all real fields

For real edge u and real face w define

    z_gamma(u,w) = exp[-a_e ||j_gamma||_2^2] exp[i j_gamma.u]
       times (1/384) sum_h exp[i S_{gamma,h}.w].

Two polymers are incompatible precisely when their vertex supports
intersect. Let Xi(u,w) be the sum of products of z_gamma over compatible
collections, including the empty collection with weight one. Every
conserved current has one such component decomposition. Consequently

    E_{u~Gaussian(A_e)} Xi(u,gZ) = Theta_g(psi)                 (6.1)

on the physical carrier in (4.2). The absolute activities satisfy
|z_gamma|<=exp(-a_e m_gamma), because the current coefficients are integers.

Here is an elementary uniform nonzero and positivity bound. An edge is
incident to at most fourteen other edges. The number of connected edge
supports of size s containing a fixed vertex is at most
8*14^(2(s-1)): choose an incident root edge, then encode a canonical
spanning-tree traversal in the line graph. Nonzero signed integer labels
of total mass m on s edges number 2^s binomial(m-1,s-1). Summing over s
gives the convenient upper bound

    number of rooted polymers of mass m <= 16*393^(m-1).       (6.2)

Conservation only decreases this number; |V_gamma|<=2m_gamma. If
a_e>=log(1700), then

    sum_{gamma containing v} |z_gamma| 2^(|V_gamma|-1)
      <= 64 exp(-a_e)/(1-1572 exp(-a_e)) <= 1/2.                (6.3)

The first inequality deliberately enlarges the direct geometric sum.
For a finite vertex region W, site addition gives

    Xi(W)=Xi(W-v)+sum_{gamma containing v, V_gamma subset W}
                     z_gamma Xi(W-V_gamma).

Inductively assume every previously formed deletion ratio lies in the
disk |Xi(W)/Xi(W-v)-1|<=1/2. Successively deleting V_gamma-v bounds
|Xi(W-V_gamma)/Xi(W-v)| by 2^(|V_gamma|-1). Equation (6.3) closes the
induction and keeps each ratio nonzero. The paired activities for j and
-j are conjugates, so each Xi(W) is real. Starting from Xi(empty)=1,
all ratios and all partition functions are strictly positive. One may
first bound the integer labels and then remove the cutoff by absolute
convergence of the finite-region sum. The lower deletion-ratio bound is
uniform in that cutoff. Thus Xi(u,w)>0 for every real u,w.

Define the real extension and its inner logarithm by

    U(u,w)=log Xi(u,w),
    V_e(Z)=log E_{u~Gaussian(A_e)} exp U(u,gZ).                 (6.4)

This is positive before taking its logarithm. It is even and signed-cubic
covariant, and is periodic under Z -> Z+2pi sqrt(beta) n for every integer
face field n. Equations (6.1) and (6.4) identify it with the original electric
correction on the physical flux carrier.

### 6.3 Real marked derivatives with a volume-independent spatial norm

For a tensor indexed by edge/face cells, define ||T||_m as follows: choose
any one index as root, fix it, sum the absolute supremum of each tensor
entry over the other indices with weight exp(m times the minimal connecting
tree length of the marked base vertices), and take the maximum over roots.
Connecting trees may have unmarked intermediate vertices. This convention
is submultiplicative under tensor contractions: concatenating connecting
trees gives an admissible connected network for the remaining marks.
For matrices it is the weighted row/column Schur norm. Take m=log(2)/100.
Every supremum below is over real u,w. No complex strip in w is assumed.

We give explicit loose bounds for orders one through three. Let

    C0 = 58,320,000,000,       epsilon = C0 exp(-a_e/4).

For a_e>=16, the claim is

    ||D_u^r D_w^s U||_m <= epsilon,       1<=r+s<=3.            (6.5)

The hard-core connected expansion is justified by its rooted-tree
majorant. Set rho_gamma=exp(-a_e m_gamma/2). The standard hard-core
tree-graph bound, followed by summing leaves, gives the rooted bound
T_gamma<=exp(m_gamma) provided

    sum_{gamma' incompatible gamma} rho_gamma' exp(m_gamma')
      <= m_gamma.

Indeed the tree generating recursion is T_gamma=exp(sum_{gamma' incompatible
gamma} rho_gamma' T_gamma'), and iteration from 1 proves this majorant.
For the present currents (6.2) bounds the sum at a vertex by

    Q=16 exp(1-a_e/2)/(1-393 exp(1-a_e/2)) <= 1/2

when a_e>=16. Multiplying by |V_gamma|<=2m_gamma verifies the required
condition. Marking a polymer containing v now bounds the sum of absolute
connected-cluster weights rooted at v, evaluated at rho, by Q. This is the
usual abstract-polymer machinery with its current-specific hypotheses
checked; see Bissacot, Fernandez and Procacci (2010), arXiv:1002.3261,
sections 2-3 for the definitions and majorants. No physical theorem is
imported from that reference.

For a connected cluster of total mass M, the union of its edge supports
is connected and every filling lies in the union's bounding box, of
diameter at most M. Each real derivative costs at most the sum of the
absolute phase slopes. For any fixed derivative order k<=3, summing all
marked indices is therefore bounded by (5M^2)^k. Averaging filling rules
does not increase this bound. A connecting tree for k marks has length at
most (k-1)M. Relative to the rho cluster weight, the actual activities
supply exp(-a_e M/2).

If a marked root cell lies in the cluster's bounding box, choose a vertex
v of the cluster; its distance from that cell is at most M. For M>=1 and
a_e>=16,

    (5M^2)^k exp[2mM-a_e M/2]
      <= (5^3 6^6) exp(-a_e/4) exp[-2 distance(v,root)] .       (6.6)

For example M^(2k) exp(-M) <= (2k)^(2k), while
a_e/4-1-2m>2. Sum the rooted rho bound Q over v. The geometric sum is
bounded by sum_{n>=0}(2n+3)^4 exp(-2n)<10,000. This proves (6.5) with
the displayed C0. It also proves uniform convergence of the real marked
series through order three. Boundary and integer-amplitude cutoffs may be
removed in those local derivative sums by dominated convergence.

The estimate does not use Cauchy bounds in a uniform complex w strip:
imaginary w could cost exp(constant M^2), for which the mass majorant
would be inadequate.

### 6.4 Integrating the massive Gaussian: a stochastic response proof

Write L=||A_e||_m <= (37/640)g^2 and q=L epsilon. Suppose q<=1/4.
For fixed w the proper probability measure

    mu_w(du) proportional exp U(u,w) Gaussian(A_e)(du)

is uniformly log-concave: its precision Hessian is A_e^(-1)-U_uu, and
the symmetric Hessian bound in (6.5) gives strict positivity. An explicit
stationary coupling for its parameters is the preconditioned Langevin
equation

    du_t = [-u_t+A_e U_u(u_t,w)]dt + sqrt(2 A_e)dB_t.           (6.7)

This is a stochastic evolution, not a MAP or algebraic fixed-point sampler.
Let zeta_t be the stationary Ornstein-Uhlenbeck process of covariance A_e.
The equivalent causal equation

    u_t=zeta_t+integral_{-infinity}^t exp[-(t-s)] A_e U_u(u_s,w) ds

is a contraction on bounded differences from zeta: U_u is bounded per
coordinate and its weighted Lipschitz constant gives q<1. Iteration
constructs a unique stationary adapted solution. The finite-dimensional
Fokker-Planck identity verifies mu_w as invariant; synchronizing Brownian
noise gives uniqueness. Smooth bounded parameter derivatives follow by
differentiating the causal equation and the same contraction, with all
finite-volume justifications supplied by (6.5).

For R=partial_w u and S=partial_w^2 u, the contracted response equations
give uniform-in-time tensor bounds

    ||R||_m <= r=q/(1-q),
    ||S||_m <= s=q(1+r)^2/(1-q).                               (6.8)

The second equation has terms U_uuu[R,R]+2U_uuw[R]+U_uww and the same
linear resolvent as the first. The connecting-tree norm permits each
contraction without an unaccounted volume factor.

Put Vtilde(w)=log E_Gaussian exp U(u,w). Differentiating this finite
positive integral gives Vtilde_i=E_mu U_i. Differentiating that expectation
through the stationary coupling yields

    Vtilde_ij = E[U_ij + U_ia R_aj],
    Vtilde_ijk = E[U_ijk + U_ija R_ak + U_ika R_aj
                       + U_iab R_aj R_bk + U_ia S_ajk],       (6.9)

where repeated edge indices are summed. Thus the first, second and third
derivative norms are bounded by epsilon, epsilon(1+r), and
epsilon[(1+r)^2+s], respectively. When q<=1/4, r<=1/3 and s<=16/27;
the last factor is at most 64/27<3. Since w=gZ,

    ||D^k V_e||_m <= 3 g^k C0 exp(-g^2/1024),    1<=k<=3.    (6.10)

For example a_e>=256 implies q<4e-14<1/4; monotonicity of
a_e exp(-a_e/4) for a_e>=256 preserves this bound. This is a very loose
sufficient range, not an optimized transition estimate. At any specified
large beta it requires a large but fixed integer N. It does not establish
the desired simultaneous small-defect regime for N=3.

These are finite-volume, uniform, real local derivative bounds on a
positive extension. Exponential locality here means the specified
derivative norm. A full physical infinite-volume state or scaling theorem
is not obtained merely by the existence of the auxiliary stationary
Gaussian-perturbed process.

## 7. Smooth infrared source equivalence

The original X has a centered lattice Gaussian distribution on

    Lambda = (2pi sqrt(beta)/N) (D Z^E + N Z^P).

Every allowed residue has the same number of link preimages under D mod N,
so no X-dependent multiplicity remains. The lattice is full rank because
it contains 2pi sqrt(beta) Z^P. Poisson summation implies that the centered
lattice theta sum is maximal at a lattice point. Completing the square
then gives, for real h,

    E exp(h.X) <= exp(||h||^2/2),       E X=0, Cov X<=I.         (7.1)

Using the same joint construction as (3.1),

    E |(Z-X).h|^2
      <= ||(K-I)h||^2 + tau||D*K h||^2
      = h.(I-K)h <= min(||h||^2, tau||D*h||^2).                (7.2)

The two terms have zero cross expectation by independence of xi and X.
The equality uses tau DD*K=I-K, not a continuum approximation.
For four-dimensional smooth compactly supported tests represented by
h_a(p)=a^2 f_p(a x), away from the boundary,

    ||D*h_a||^2=O(a^2),       ||DD*h_a||^2=O(a^4).

Thus every finite family of such flux tests has the same possible limit
for X and Z, by an explicit L2 coupling. This holds at fixed beta,N, with
box boundaries taken outside the test support. It is an equivalence of
possible limits, not their existence or Gaussianity.

There is also the exact unfiltered characteristic identity

    E exp(i h.X_s)=E exp(i h.X) exp[-tau||D*h||^2/2].            (7.3)

For an integer link current J, the unfiltered angular Wilson character
acquires exp[-s^2||J||^2/2]. This factor refers to theta, not to the
subsequently filtered psi. Filtering has an additional field-dependent
drift. Higher cumulants of X_s equal those of X because the added noise is
independent Gaussian; filtering transforms them linearly and does not
erase them at a fixed finite lattice scale.

There is a local negative-Sobolev coupling statement as well. Represent
each of the six components as the distribution a^2 sum_p X_p delta_{a x_p}
or a^2 sum_p Z_p delta_{a x_p}. Multiply by a fixed smooth compactly
supported cutoff chi and use a Fourier basis on a fixed continuum torus
containing its support. The corresponding lattice test is
h_{n,a}(p)=a^2 chi(a x_p) exp(i n.a x_p), in the selected component.
For each fixed n the right side of (7.2) tends to zero, whereas
||h_{n,a}||^2 is bounded uniformly in n,a. Since
sum_{n in Z^4}(1+|n|^2)^(-s)<infinity for s>2, dominated convergence gives

    E ||chi(Z_a-X_a)||_{H^(-s)}^2 -> 0,       s>2.             (7.4)

The same representation and

    Cov Z = K(Cov X+tau DD*)K <= K <= I

give uniform local H^(-s') second moments for every s'>2. Choosing
2<s'<s and using compact embedding gives tightness in H^(-s), locally.
Thus the two fields have precisely the same subsequential local
distributional scaling limits under this coupling. No uniqueness or
Gaussianity of those limits is supplied by the smoothing identity.

## 8. Status and next discriminator

Sections 1-7 are proposed derivations with uniform finite-volume bounds.
The first runner version checks seven families, including rational folding
and bundle identities, independent real/Fourier density sums, local integer
fillings, gauge projection, massive geometry and smooth-source scaling.
The positivity induction and stochastic-response bounds still need their
dedicated finite falsifiers and a cold proof review. The full physical
score and magnetic-sector stability theorem remains necessary. No finite-
clock photon phase, quantum spin-one phase, axiom failure, matter sector
or TOE completion is claimed here.
