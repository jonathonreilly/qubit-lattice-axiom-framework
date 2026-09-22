# Smooth nonlinear Euler limit with autonomous moving matching geometry

**Status:** proposed conditional theorem with complete extension argument;
author controls and selective independent reconstruction pending.
**Date:** 2026-09-21.

This extends DIMER_SMOOTH_NONLINEAR_EULER_LIMIT.md to the actual joint
matching/color process in DIMER_ROUTED_MOVING_GEOMETRY_EXTENSION.md.
It uses the same permanent colors, routed exchanges and equal-rate immutable
plaquette rotations. Geometry may start from an arbitrary law and need not
mix or be stationary. Inhomogeneous color preparation is still supplied.

## 1. Joint process and statement

On the even N-periodic cubic lattice, N>=8, a perfect matching M pairs each
black site u with the white site u+d_M(u), where d_M(u) is a unit coordinate
vector with either sign. A pair's antipodally even fourteen-color label is
indexed by its black endpoint. Define

    q_delta^M(u)=owner_M(u+delta),
    a_delta^M(u)=delta-d_M(q_delta^M(u)).

Every q_delta is a bounded-displacement permutation. A fixed point has
a_delta=0 and no color exchange. Every nonfixed route has the four distinct
contexts used by the original rate. Its rate remains

    k0/2+[S(l,a)+S(a,r)-S(l,b)-S(b,r)]/4,
    S_delta(a,b)=(gamma/2)delta.[e_a cross b_b+e_b cross b_a],

with k0>|gamma| and r_*=(k0-|gamma|)/2. At fixed M, every homogeneous
product color law is invariant. Each flippable plaquette additionally
rotates its four immutable records clockwise at rate nu and counterclockwise
at rate nu, with fixed bounded nu>=0. Geometry has autonomous flip rate
2nu, independent of colors. At black endpoints, one rotation mark is a
two-color-position swap and the other is the identity, as established by
the source's exact record tracking. Thus the joint color/geometry projection
is Markov; unobserved permanent fine keys do not enter its rates.

Use Euler generator N(L_color+L_geo). Let mu_N(t) be its joint law and
rho_N(t) its actual geometry marginal. For a stipulated strictly positive
periodic C3 solution p(t,x) of

    p_t+div F(p)=0,
    F_a(p)=gamma p_a[e_a cross Y+X cross b_a-2X cross Y]

on fixed[0,T], define nu_N^p(t) as follows: draw M from rho_N(t), then
independent colors at black u with probabilities p(t,u/N). This is a
comparison law using the actual geometry marginal, not an assumed evolution
of the physical state. Write

    h_N(t)=H(mu_N(t) | nu_N^p(t)).

If h_N(0)=o(K), K=N^3/2, then

    sup_(t<=T) h_N(t)/K ->0.                         (1)

For each fixed smooth spatial test and color, the weak empirical color
density converges in probability to p uniformly on[0,T], as in the
fixed-winding theorem. The result is uniform over the initial geometry law.
It does not assert later conditional product structure in total variation.
No geometric equilibrium, mixing rate or geometry entropy hypothesis is
needed. It does require the stipulated interior smooth solution, supplied
color preparation, positive routed-rate floor and autonomous geometric law.

## 2. Conditional entropy supplies the mixing energy

Let pi_col be uniform product14^-K on black-site colors and set

    H0_N(t)=H(mu_N(t) | rho_N(t) times pi_col)
           =sum_M rho_N(t,M) H(mu_N(colors|M) | pi_col).

It lies between0 and K log14. For every M of positive marginal mass let
f_M be the conditional density with respect to pi_col, and let D_M be the
bare routed exchange Dirichlet form from the fixed-winding proof, now using
that matching's actual routes. Put D(t)=sum_M rho_N(t,M) D_M(sqrt f_M).

Color dynamics keeps M fixed, preserves pi_col and has rate floor r_*,
so its contribution to H0_N' is at most -2 N r_* D(t). Geometry contributes
a nonpositive quantity. To check the latter without a geometry stationary
law, apply the geometry-only Markov semigroup to both joint measures
mu and rho times pi_col. Each geometry jump applies a color permutation
independent of the colors, and therefore carries the second measure to
rho' times pi_col. The finite log-sum inequality gives relative-entropy
contraction of this pair. Infinitesimal differentiation shows that the
geometry-only contribution to H0_N' is nonpositive. Color and geometry
generator contributions add, including the derivative of rho.

Consequently

    H0_N'(t)<=-2N r_* D(t),
    integral_0^T D(t)dt<=K log14/(2N r_*).            (2)

This is conditional color entropy, not total entropy relative to a uniform
matching ensemble. It holds even when rho initially is a point mass. Zeros
can be handled by the finite-state integrated log-sum inequality and limits.
For clarity, the reference rho(t) times pi_col solves the full joint
forward equation too: the color part annihilates pi_col for each M and
the color-independent geometric permutations preserve it.

## 3. Physical cubes with complete-pair ownership

Take an even integer L>=16, fixed before N tends to infinity, and N>10L.
For each physical site z, black or white, let

    C_z=z+{0,...,L-1}^3,
    B_z(M)={owner_M(x): x in C_z},  m_z=|B_z(M)|,
    w_L=L^3+L^2.

A black anchor is in B_z iff at least one endpoint of its pair is in C_z.
Every anchor belongs to exactly w_L translated blocks: the sets of cube
origins containing either of its nearest-neighbor endpoints have sizes L^3
and intersection L^3-L^2. This count is independent of the matching
direction. In particular

    sum_z m_z=K w_L,
    (L^3/2)<=m_z<=L^3,   0<m_z/w_L<=1.             (3)

The lower bound follows because every even-sided cube contains L^3/2
black sites. Owner blocks lie within a fixed one-step enlargement of the
physical cube and have diameter O(L).

Map every nearest-neighbor edge inside C_z to the edge between its owners,
discarding loops. This connected multigraph on B_z is a contraction of
the connected cube graph. Every nonloop is an actual routed swap: if its
physical black endpoint is u and its white endpoint is u+delta, its owners
are u and q_delta(u). Thus these internal bare swaps connect every color
arrangement with the same block counts. For fixed L only finitely many
local matching patterns, connected graphs and fourteen-color count sectors
occur. The minimum nontrivial Poincare gap g_L is positive. No uniform
lower bound as L grows is asserted.

Use the Dirichlet form of all internal physical cube edges, retaining their
multiplicities under contraction. A given nonmatching nearest-neighbor
physical edge lies inside exactly L^3-L^2 translated cubes. Hence summing
these internal forms over z is (L^3-L^2) times the full bare routed form.
An upper bound O(L^3) would already suffice.

Condition successively on M, outside colors and block counts. The same
Cauchy-Schwarz proof as in the fixed-winding note gives for bounded V_z
of zero uniform count-sector mean

    |E_mu V_z| <=2||V_z||_infinity g_L^-1/2
               sqrt(sum_M rho(M) E_pi D_(C_z,M)(sqrt f_M)). (4)

It remains valid when V_z and B_z depend on M. The density is normalized
only after averaging all count/exterior sectors at that M, and
sum_M rho(M)=1. Summing (4) over N^3=2K origins with weights m_z/w_L<=1,
then using (2), gives time-integrated total error

    K C_(L,T)/sqrt N.                               (5)

## 4. One-block current replacement and the geometric tensor

Write pbar_z for the empirical color probability in B_z(M). The four
contexts of a nonfixed routed channel remain within a bounded physical
distance of its black anchor, uniformly in M. All channels anchored farther
than a fixed distance from the cube boundary have their contexts in B_z.
The number of excluded anchors is O(L^2), uniformly in M.

For the routed log-profile drift, average the exact global sum over all
owner blocks using the exact multiplicity w_L. Move the smooth gradient
coefficient from u/N to z/N at cost O(K L/N), but retain the bounded
geometry-dependent displacement a_delta(u) in each summand. Conditional
on block counts, any four distinct positions are draws without replacement.
The product expectation of the outgoing current is F_delta(pbar_z)/2;
the bounded four-draw discrepancy is O(1/m_z). Fixed routes have a_delta=0,
so they contribute zero and need no four-distinct-site assertion.

Apply (4) to each normalized, displacement-weighted internal block current.
Restore its O(L^2) excluded anchors. The expectation-level integrated
replacement errors divided by K are bounded by

    C_T(1/L+1/L^3+L/N)+C_(L,T)/sqrt N.              (6)

The remaining displacement sum has the uniform local identity

    T_z=(1/2)sum_delta sum_(u in B_z)
                       a_delta(u) tensor delta
        = m_z I+O(L^2).                             (7)

To prove (7), substitute a_delta=delta-d_M(q_delta u). A bounded-displacement
permutation q_delta changes the set B_z only at O(L^2) boundary anchors:
B_z agrees with the ordinary black anchors of C_z except in a fixed-width
boundary strip, and q_delta displaces each point by at most two steps.
Therefore

    sum_(u in B_z) d_M(q_delta u)
          =sum_(v in B_z) d_M(v)+O(L^2).

Its leading term is independent of delta, and sum_delta delta=0, while
(1/2)sum_delta delta tensor delta=I. This proves (7), including arbitrary
rough microscopic matchings. The tensor need not equal m_z I at finite
block size. No pointwise or isotropic matching assumption is made.

The routed entropy drift thus becomes, up to (6),

    -(1/w_L)sum_z m_z sum_j
                     partial_j theta(t,z/N).F_j(pbar_z). (8)

The indicator term similarly becomes
-(1/w_L)sum_z m_z theta_t(t,z/N).pbar_z with O(K L/N) error.

## 5. Plaquette color drift has zero canonical mean

For Theta=sum_u theta(t,u/N).I_u, the actual geometry contribution is

    L_geo Theta=nu sum_(P flippable)
               [theta(v_P/N)-theta(u_P/N)].(I_(u_P)-I_(v_P)). (9)

The other equal-rate rotation mark has identity color action. Its rate and
flippability depend only on M. The two black square vertices are a bounded
distance apart and form an actual contracted-graph edge.

Choose either black vertex as the anchor of each square, consistently.
Average each such channel over the w_L blocks containing that anchor.
Excluding channels whose endpoints or local square lie outside the block
loses O(L^2) per block. Taylor expansion of theta after multiplying by N
has O(K/N) error. In the remaining normalized block sum, the coefficient
is bounded and geometry-dependent but independent of colors. Uniform
count-sector sampling gives exactly

    E_count(I_(u_P)-I_(v_P))=0.

Apply (4)-(5). The integrated expectation of N L_geo Theta, divided by K,
is O_T(1/L+L/N)+C_(L,T)/sqrt N. Thus geometry adds no leading nonlinear
Euler flux. This conclusion comes from conditional color mixing; it does
not set each realization's plaquette current to zero.

## 6. Entropy closure for a nonstationary geometry marginal

The exact decomposition, with theta=log p, is

    h_N=H0_N-E_mu Theta-K log14,
    h_N'<=-N E_mu(L_color+L_geo)Theta-E_mu partial_t Theta. (10)

There is no missing derivative of an assumed stationary geometry density:
H0_N includes the actual rho(t), and its full derivative is bounded in (2).
Use (6),(8),(9), and put omega_z=m_z/w_L. The entropy calculation from the
fixed-winding proof becomes a sum weighted by omega_z.

The constant theta_t.p is zero. For any fixed smooth scalar function f,

    sum_z omega_z f(z/N)=sum_(black u) f(u/N)+O(K L/N), (11)

by the exact coverage in (3) and translation of f over a block diameter.
Apply this to the entropy-flux divergence, whose continuum integral is zero.
The linear Taylor term vanishes at each z on the simplex tangent by the
same symmetrizer and PDE as before; multiplication by omega_z changes
nothing. The remaining error is bounded by

    C sum_z omega_z |pbar_z-p(t,z/N)|^2.             (12)

To close (12), condition the comparison law nu_N^p on M. Owner-block
overlap is possible only for origins at displacement in a cube of side
2L+3. Hence its graph is colorable with chi=32L^3 slots for L>=16,
including empty slots. Disjoint owner blocks have independent colors
conditional on M. Every m_z>=L^3/2. The previous coordinate Hoeffding and
tail-integration bound gives

    E exp[(m_z/14)|pbar_z-E pbar_z|^2] <=29.

Choose alpha=1/1792, independent of L. Since omega_z<=1 and
2alpha chi=L^3/28<=m_z/14, Holder and the smooth mean shift O(L/N) yield,
uniformly for every M and therefore after averaging rho(t),

    log E_(nu_N^p) exp[alpha sum_z omega_z |pbar_z-p(t,z/N)|^2]
       <= (2K/chi) log29+C alpha K L^2/N^2.          (13)

The entropy inequality bounds the expectation of (12)'s sum by

    h_N/alpha+C K/L^3+C K L^2/N^2.

Combining the integrated estimates,

    h_N(t)/K <=h_N(0)/K+C integral_0^t h_N(s)/K ds
          +C_T(1/L+1/L^3+L/N+L^2/N^2+1/N)
          +C_(L,T)/sqrt N.                          (14)

The coefficient of h_N is independent of L. Gronwall, N tending to infinity
at each fixed even L, and then L tending to infinity prove (1).

## 7. Empirical conclusion and scope

The reference's color marginal is the stated product profile regardless
of rho(t), so fixed-time concentration transfers by the same entropy event
inequality. Each routed or plaquette jump changes a normalized smooth
empirical test by O(1/(NK)). Their total microscopic rate is O(K), with
constant depending on k0,gamma,nu. Under Euler acceleration the martingale
bracket is O_T(1/(NK)) and drift is uniformly bounded. The fixed mesh and
Doob argument give uniform-time weak empirical convergence.

Taking nu=0 includes every fixed matching, not just the winding one.
For nu>0 this is the actual autonomous moving matching process. It supplies
no nonlinear evolution law for the geometric Gauss field, no birth-produced
inhomogeneous profile, no shock continuation and no quantum completion.
The unchanged homogeneous formation result still initializes only its
specified color ensemble. Arbitrary geometry here does not mean arbitrary
color-dependent geometry rates; autonomy and color permutations are
load-bearing. All conclusions concern the color projection and stipulated
smooth positive continuum solution. Independent reconstruction is required
before publishing this extension as a checked milestone.

