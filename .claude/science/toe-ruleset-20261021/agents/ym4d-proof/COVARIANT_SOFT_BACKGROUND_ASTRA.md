# A covariant local background for the actual normalized soft step

Author proof unit, Astra/max, in the supplied four-dimensional SU(N) Wilson /
normalized paired S4′ model. **For sufficiently small coarse plaquette
curvature, arbitrary coarse holonomies are allowed: the actual smooth finite-u
coordinate density has a unique critical point in a fixed local block-tree
chart, with a volume-uniform positive quadratic precision.** Its displacement
and first background derivative obey uniform local bounds. The complete
all-fine-good / small-mismatch event lies in this relative chart. An exact
Gaussian representation retains the original sources, cuts and complement.

This is a bounded mathematical producer awaiting independent review. It does
not prove interacting covariance decay, a connected source logarithm, a
multilevel RG construction, full continuum existence or a physical mass gap.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Actual finite-u local coordinate-density critical point and Gaussian reference over curvature-small coarse data, including holonomies; exact strong-good-event chart interface."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Setting, prior work and the exact lift

Fix d=4, N>=2, D=N²−1, odd L>=3, T>=2, u>=1, and
`0<kappa_-<=kappa<=kappa_+`. The fine torus has side LT. Blocks are
`B_X=LX+{-h,...,h}^4`, h=(L−1)/2, with root LX. The Lie algebra has the
HS inner product `Re tr(A*B)`; its D real coordinates are orthonormal.
Adjoints and site sums use counting measure. Coarse V is fixed throughout.
Let

    delta_V=max_(coarse plaquettes P) ||I-V_P||op.

No bound on individual `||V_c-I||` is imposed. Every link carries normalized
probability Haar. The actual density and sources are

    w_0(U,V)=exp[-u sum_p s(U_p)] product_c k_(kappa u)(V_c;M_c(U)),
    s(W)=1-Re tr(W)/N,
    k_t(V;M)=exp[-t(1-Re tr(V^-1 M)/N)]/N_t(M),
    N_t(M)=int exp[-t(1-Re tr(W^-1 M)/N)]dW,
    delta S_epsilon=u sum_p epsilon_p s(U_p).              (CB1)

`M_c` is the arithmetic mean of all `24L^4` paired S4′ transporters: the same
coordinate order is used at both ends. Kernel couplings stay real and fixed.
The original cut is the interior-only cut of H3 in
[SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md](SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md).
It is not the all-fine-good event used below.

Define a background on positive fine links:

    U0(V)_(x,mu)=I                         if x_mu-LX_mu<h,
    U0(V)_(x,mu)=V_(X,mu)                 if x_mu-LX_mu=h,
                         x in B_X.                       (CB2)

All internal links are I. A straight segment from y in B_X to y+L e_mu
crosses precisely the face (X,mu) once. Its root-to-y and endpoint-to-root
legs remain internal, so **each actual S4′ transporter is exactly V_c**.
This holds for every coordinate ordering and every wrapping label. Thus
`M_c(U0)=V_c` without a small-curvature assumption.

A fine (mu,nu) plaquette is I unless its base has both corresponding local
coordinates h. At that intersection it is exactly

    V_(X,mu) V_(X+mu,nu) V_(X+nu,mu)^-1 V_(X,nu)^-1.       (CB3)

Each coarse plaquette occurs L² times. In particular

    w_0(U0,V)=exp[-u L² sum_P s(V_P)] N_t(I)^(-4T^4).

No coarse integration or conditional normalization was used.

The predecessor [identity covariance unit](SOFT_FLUCTUATION_COVARIANCE_ASTRA.md)
already supplies the local tree idea, finite-u variance calculation and
weighted Gaussian mechanism. Existing LINEAR_PACKAGE Lemma6.1,
Propositions6.2–6.4 and PROOF's CT/N5/RW are prior work. The present extension
uses a new exact-flat-brick observation, actual finite-u local critical shift
and strong-good-event interface; it does not rename the old positivity or
Combes–Thomas mechanism as a new theorem. STEP55 §4.1–§4.3, its §10 S5–S7,
and CODEX_REVIEW_STEP R6 supply only the fixed-real-coupling single-normalizer
analytic contract. The fixed-chart limitation in R7 is addressed explicitly
by the product chart and its Hessian bounds below.

## 2. Local quotient and exactly flat lifted bricks

Use the complete axial tree inside each block: the parent of a nonroot site
moves its highest nonzero coordinate toward zero. The unique root-pinned
gauge transform makes all tree links I. Successive tree integrations give

    product_b dU_b=product_(nonroot x) dg_x product_(free e) dW_e,
    m0=3L^4+1,                  number of free links=m0 T^4. (CB4)

This is the same triangular group/Haar identity, with FP factor one. There
is no orthogonal-slice Gram determinant. Root gauge modes and holonomy modes
remain in the free links; none is deleted. At fixed V a nonconstant coarse
root gauge is not generally a symmetry with V held unchanged.

For a coarse link c=(X,mu), use the **lifted rectangular brick** consisting
of B_X and B_(X+mu), with only the edges and plaquettes inside that lift.
Only the mu coarse face occurs internally. Every plaquette in that brick
is exactly flat by (CB3), for arbitrary V. The constant gauge I on B_X and
V_c on B_(X+mu) makes every brick link I. At T=2 the union of vertex sets
also has a far periodic seam if one takes its torus-induced graph. That
extra seam is excluded from the lifted brick: its holonomy need not be I.
The paths and fillings here never use it. This distinction is essential.

Let J insert zeros on the tree links. In left coordinates

    W_e=exp(A_e) U0_e,                       A=Ja,

write `D_V A(p)=(d/ds) U_p(s) U_p(0)^-1|_0`, and let theta_(c,tau)^V
be the analogous left derivative of a contour, in its starting-root frame.
A negative edge contributes minus A transported through its inverse;
all prefixes act by the unitary adjoint representation. Put

    Q_V=average_tau theta_(c,tau)^V,
    <A,B_V A>=sum_c average_tau ||theta_(c,tau)^V-Q_V A(c)||²,
    H_V=J*(D_V*D_V+kappa Q_V*Q_V)J.                         (CB5)

B_V in subsequent formulas denotes its J compression. It is positive.
These are colour-coupled operators; they are not scalar matrices tensored
with I_D unless the background permits that reduction.

The elementary grid-combing proof of the identity unit works isometrically
inside each flat brick. An internal free edge is recovered from curvature
in its block. A crossing edge is recovered from Q_V plus curvature in its
brick, transported back to its starting frame. For completeness, contract a
closed edge chain coordinate by coordinate in a rectangular box. The area
is at most `(sum of widths)*(edge-chain length)`. The relevant width sum is
<5L and each loop has length <6L. Subtracting the averaged contour filling
from the free-edge filling gives norm at most b_L=60L². Ad transports have
norm one and cause no curvature error on these supports. Therefore

    ||A||² <= C_F||D_V A||²+C_Q||Q_V A||²,
    C_F=4L³(L+4)b_L²,       C_Q=2L³,
    H_V>=a I,       a=1/max(C_F,C_Q/kappa_-)>0.             (CB6)

There are at most 4L⁴ internal edges per block and L³ crossing edges per
positive coarse link. A plaquette in an endpoint brick is charged by at most
eight incident coarse-link labels, including at T=2. These are the counts
behind C_F. The argument uses only flat filling plaquettes; D_V on the
remaining plaquettes contributes nonnegatively. It proves (CB6) for every V,
not only small-curvature V, and also on the infinite periodically extended
lattice. It retains all root and harmonic directions in the tree metric.

## 3. Exact finite-u Hessian and the nonzero gradient

Use the explicit exponential image of a traceless su(N) HS ball. Every chart
radius below is less than `min(injectivity radius, pi/sqrt(N))`. A matrix
principal logarithm is required to lie in this traceless ball; the principal
log alone is not a sufficient SU(N) chart condition.

Write `dHaar(exp A)=h_N j_N(A)d^D A`, j_N(0)=1. Then

    log j_N(A)=-N||A||²/12+O(||A||^4).

Define the actual coordinate-density action, rescaled only for convenience:

    F_u^V(a)=(N/u){S_eff(exp(Ja)U0;V)-S_eff(U0;V)
                          -sum_(free e) log j_N(a_e)},
    S_eff=-log w_0.                                         (CB7)

Its critical point is a maximum of the density with respect to this fixed
Lebesgue chart. It is not asserted to be a coordinate-free Haar-density
critical point or a global minimizer on the compact configuration space.

For the normalized one-link tilt at t=kappa u, let
`E_t W=c_N(t)I`. Then `0<c_N(t)<1` and `c_N'(t)=Var_t(Re tr W/N)>0`.
Multiplying every contour by V_c^-1 reduces its expansion at U0 to the
identity calculation. Haar invariance of the one-link normalizer gives

    Hess(kernel contribution to F_u^V)
              =kappa[Q_V*Q_V+(1-c_N(t))B_V].

Its first derivative is zero even at finite u. The Haar term has zero first
derivative and Hessian `N²/(6u)I`. The Wilson part is the only nonzero first
derivative at U0. Precisely,

    g_V=gradient F_u^V(0),        ||g_V||_(infinity,HS)<=G delta_V,
    G=6 sqrt(N),
    K0=Hess F_u^V(0)
       =H_V+E_V+kappa(1-c_N(t))B_V+N²/(6u)I,
    ||E_V||_(row,HS), ||E_V||_(column,HS) <=24 delta_V.      (CB8)

Here a matrix entry is a D-by-D colour block; row/column norms sum its
operator norm. E_V is real self-adjoint. To prove its bound, write a
plaquette variation as `prod_(i=1)^4 exp(s B_i) P0`, with transported signed
B_i and P0=U0_p. Its second derivative is
`[sum_i B_i²+2 sum_(i<j) B_i B_j]P0`. At P0=I its negative real trace is
`||sum_i B_i||²`. Each colour-block Hessian error has norm at most
`||P0-I||op`; there are four entries per plaquette row and six plaquettes
per link. The first derivative is bounded by sqrt(N) delta_V per incident
plaquette. Both errors vanish on every flat plaquette. This proves (CB8)
without turning the nonstationary lift into a minimizer by assertion.

Let

    delta0=min(1/24,a/48),       gamma=a/2,
    P=5L,   b1=25+24 kappa_+ P²+N²/6.

If delta_V<=delta0, K0>=gamma I and its block row/column norm is at most b1.
Its range is at most two coarse block steps. This uses the same explicit
path counts: a contour has length <=P, a fine link is read by at most eight
coarse means, and the two path Gram terms cost <=16P² in B_V.

## 4. Uniform local analytic constants and the actual critical shift

Here are explicit finite constants sufficient for a volume-uniform
contraction. They are deliberately very conservative; no numerical
curvature sample is certified by them without checking the inequalities.

Use the corrected STEP55 constants
`C_N=N(N²-N+2)/2`, `A_N=sup_(t>0)t E_t s<infinity`, and
`K_N=A_N 2^(A_N+1)`. Set

    r_N=min{1/160, 1/[32 K_N(1+C_N/N)]},
    alpha=min{1/(100N), pi/(4sqrt(N)), injectivity_radius/4,
                         log(1+r_N/2)/P},
    q=alpha/(4sqrt(D)),      nloc=(8L^4+8)D,
    Mloc=20N(1+kappa_+),
    C=720D nloc² Mloc/q³.                                  (CB9)

For complex fields use the explicit continuations
`s^C(W)=1-[tr W+tr W^-1]/(2N)` and
`Phi(W;M,Mtilde)=1-[tr(W^-1 M)+tr(Mtilde W)]/(2N)`, where
`Mtilde=average_tau T_tau^-1`. No conjugation of a complex variable occurs.
The polar stationary value is the holomorphic SU(N) continuation supplied
by PR, not an ordinary U(N) polar replacement.

These constants have no u, V or volume dependence. A local term reads at
most 8L⁴ fine links; the eight extra slots allow all coarse data occurring
in that term. Each fine coordinate belongs to at most six Wilson terms,
eight kernel terms and one Haar term. On complex coordinate polydiscs of
radius q, every fine/coarse HS displacement is <=alpha/4. Relative to its
unitary V_c, each contour changes by at most an exponential of its bounded
path length. The doubled mean displacement is within r_N. STEP55 PR/NZ,
with its real t>0 and its corrected normalizer, gives a single centered
logarithm bounded by one there, uniformly in t. No complex coupling is used.

More explicitly the local normalized kernel action splits exactly into
`N kappa psi_M(V)+(N/u)[log Ntilde_t(M)-log N_t(I)]` after its constant is
removed. The holomorphic polar maximizer defines psi on this domain.
The Wilson term, this kernel term and the Haar term are each bounded by
Mloc. For Haar, the series for
`det[sinh(ad A/2)/(ad A/2)]` has a nonzero logarithm: its matrix deviation
from I is <=alpha², and D alpha²<1/1000. These arguments give the bound,
rather than assuming uniform smoothness of an uncentered lognormalizer.

Cauchy's inequality bounds each scalar third derivative on the smaller
polydisc by `48 Mloc/q³`. Summing at most 15 incident terms, nloc² pairs of
indices, and the D colour rows gives, for `||a||_(infinity,HS)<=q/4`,

    ||Hess F_u^V(a)-K0||_(row,HS) <= C ||a||_(infinity,HS),
    ||gradient F_u^V(a)-g_V-K0 a||_(infinity,HS)
                                      <=(C/2)||a||².       (CB10)

The same constants, increased only by the already included local slots,
bound joint local derivatives in a coarse datum. No total-volume Cauchy
norm is used. The product HS ball is invariant under blockwise adjoint
gauges, unlike a fixed choice of componentwise real cube.

For a weighted inverse of K0 take

    m=(1/2)log(1+gamma/(2b1)),
    R=(2m0/gamma)coth(m/2)^4.                               (CB11)

Schur conjugation gives `||(K0+t)^-1||` with exponential rate m and point
prefactor `2/(gamma+t)`; summing the complete colour-block row gives
`||K0^-1||_(infinity,HS)<=R`. This is the previous CT mechanism, now for the
colour-coupled precision. The coth sum counts every periodic image and
m0 free links per coarse cell. In particular R>=1/gamma.

Choose

    r=min{q/4, gamma/(4C), 1/(4RC)},
    delta_star=min{delta0, r/(8RG)}.                        (CB12)

For delta_V<=delta_star, the map

    T(a)=-K0^-1 g_V
         -K0^-1[gradient F_u^V(a)-g_V-K0 a]

maps the closed HS sup ball of radius r into itself and has Lipschitz
constant at most 1/4. Its unique fixed point a_u(V) satisfies

    ||a_u(V)||_(infinity,HS)<=2RG delta_V<=r/4,
    gradient F_u^V(a_u)=0,
    Hess F_u^V(a)>=3gamma/4 I       throughout the real r ball. (CB13)

Thus a_u is the unique real minimizer of the smooth uncut density action
in this convex local coordinate ball. Hard indicators are retained separately.
In particular a_u is not asserted to belong to the stronger good event G
below; no fixed-V nonemptiness or concentration of G follows from this
critical-point construction.
Existence is a uniform Banach contraction, not a fixed-volume implicit
function theorem with an untracked radius. At a flat coarse V it is exactly
zero, however large its holonomies. Joint coarse gauge covariance follows
from uniqueness and the adjoint invariance of the HS ball.

For a complex local coarse change `V_c -> exp(v_c)V_c`, the joint Cauchy
bounds in (CB9) give a uniform contraction neighborhood, for example after
shrinking to `||v||_(infinity,HS)<min(q/4,r/(8RC))`. The fixed point is a
uniformly convergent sequence of holomorphic maps. Thus it is locally real
analytic in arbitrary real coarse data in the stated curvature class.
Uniformity concerns a chart about each real V; no common global logarithm
of every V_c is chosen.

A real source version and a holomorphic critical-point branch are also
available without moving the integration contour. The normalized source
is `N sum_p epsilon_p s(U_p)`. On the same chart its Hessian row is bounded
by `B_epsilon ||epsilon||infinity`, where the conservative choice
`B_epsilon=1000 N D²/q²` follows from four links per plaquette and six
incident plaquettes. Its gradient at zero is at most
`G delta_V ||epsilon||infinity`. For

    ||epsilon||infinity < rho_star=min{1,1/(4R B_epsilon)}, (CB14)

the same map with this source added is a contraction of the r ball with
constant <=1/2, and `||a_(u,epsilon)||<=4RG delta_V`. For real epsilon its
Hessian is >=gamma/2. For complex epsilon it is a holomorphic critical
point, not a claimed complex probability law or a nonvanishing integrated
partition function. The Gaussian representation below uses the real
zero-source point and retains the original source exactly.

The tree phase is a separate function. Its critical point a_tree is
obtained by omitting the centered lognormalizer and Haar terms, with the
same bounds. Their difference has gradient zero at a=0 and Hessian row
at most `C_diff/u`, with the safe choice
`C_diff=100D nloc N/q²`. Consequently

    ||a_u-a_tree||_(infinity,HS)
                       <=4R² G C_diff delta_V/u.         (CB15)

The exact finite-u point is not silently replaced by the tree point.

## 5. Covariance, background locality and full normalization

Put K_*=Hess F_u^V(a_u). It is a real colour-coupled matrix on
`D m0 T^4` coordinates, with range <=2, gap >=3gamma/4 and block row norm
<=b1+gamma/4. Set gamma_*=gamma/2 and b_*=b1+gamma/4. The same resolvent
integral

    S_*=K_*^-1/2=(1/pi)int_0^infinity t^-1/2(K_*+t)^-1 dt

and `m_*=(1/2)log(1+gamma_*/(2b_*))` give exponential inverse/square-root
bounds, with point prefactors `2/gamma_*` and `2/sqrt(gamma_*)`.
The periodic operator is the quotient of its T-periodic infinite lift;
periodizing that lift sums every winding image. For 0<mu<m_*, both weighted
block rows and columns of S_* are bounded by

    (2m0/sqrt(gamma_*)) coth((m_*-mu)/2)^4.                 (CB16)

For chart potentials the map is J S_*. Physical left link tangents also
include the local differential dexp_(a_u), whose real HS operator norm is
<=1. Their map is J dexp_(a_u) S_*. Linearized curvature is
D_(U_*) J dexp_(a_u) S_*; its output density
is 6L^4 plaquettes per block, with row and column multipliers
4 exp(mu) and 6 exp(mu) relative to (CB16). All actual Lie-algebra Gaussian
covariances carry the factor N/u. These potential and curvature maps are
distinct, and neither is an interacting covariance.

D enters all scalar mode counts and determinants. There is no scalar
identity-colour tensor assumption. This is a Gaussian reference covariance,
not the covariance of the interacting conditional measure.

There is also genuine first background locality. Differentiating the
critical equation in one coarse link gives

    D_(V_c) a_u = -K_*^-1 D_(V_c) gradient F_u^V(a_u).       (CB17)

At fixed a, the forcing on the right is supported within distance one of
the two endpoint blocks, at most 18 blocks. The joint local Cauchy estimate
bounds its HS norm per link by C for a unit coarse tangent. Hence

    ||D_(V_c) a_(u,e)|| <=(36m0 C/gamma_*)
                         exp[-m_* distance(X_e,Y_c)],     (CB18)

where Y_c is that support. Here the direct finite-torus CT bound supplies
the geodesic estimate; the exact periodized kernel is not replaced by a
single winding term. This distinguishes background dependence from
entrywise locality of an inverse. Higher connected derivative/activity
norms are not asserted by (CB18).

Let U_*=exp(Ja_u)U0 and sigma=sqrt(N/u). **Shift additively in this same
Lebesgue chart**, `a=a_u+sigma z`. Do not replace this with fresh exponential
coordinates at U_* without their extra Jacobian. With
`L(a)=S_eff(exp(Ja)U0;V)-sum_e log j_N(a_e)`, define

    R_*(z)=L(a_u+sigma z)-L(a_u)-(1/2)<z,K_*z>.

Every derivative up to order two vanishes at z=0. Local third-order
remainders on `sigma max||z_e||<=r/2` are bounded by `C' u^-1/2 p³`
when max||z_e||<=p, uniformly in V,u,T in the stated domain. All local
normalizer and Haar terms remain in R_*. One explicit choice is
`C'=8 Mloc nloc^3 sqrt(N)/q^3`. Local linear Taylor terms cancel only after
summing the critical equation; they are included in each local subtraction.

Take r_ch=r; any radius between r/2 and r also works. For any bounded
root-pinned-gauge-invariant insertion Xi, the restricted actual integral is

    Z_(cut,chart)^epsilon[Xi](V)
      =A_*(V) E_(xi iid N(0,1))[
        Theta_(r_ch)(a_u+sigma S_*xi)
        chi_cut(U(a_u+sigma S_*xi)) Xi(U,V)
        exp{-R_*(S_*xi)-delta S_epsilon(U)}],

    A_*(V)=w_0(U_*,V) h_N^(m0 T^4) product_e j_N(a_(u,e))
               (2pi N/u)^(D m0 T^4/2) det(K_*)^-1/2,
    Theta_(r_ch)(a)=1{all a_e in the traceless HS ball of radius r_ch}. (CB19)

Here U(a)=exp(Ja)U0. Outside Theta the bracket is defined as zero before evaluating chart-only
functions. The determinant is the full colour-coupled determinant. All
vacuum, Haar, scale and mode factors are present. Neither integration over
V nor normalization of the kernel in its V variable has been invoked.
The coordinate cutoff cannot be replaced by the group image of the chart,
which would include repeated exponential preimages.

Sources have a different background budget from the identity case. If
`Delta_bg=max_p||I-U_*p||op`, then
`Delta_bg<=delta_V+4||a_u||_(infinity,HS)`.
On a canonical fluctuation ball one has per plaquette

    |u epsilon_p s(U_p(a_u+sigma z))|
        <=C'' rho [u Delta_bg²+sqrt(u) Delta_bg p+p²].       (CB20)

Here C''=8N is sufficient by the unitary exponential difference bound.
The vacuum source term and linear fluctuation source are retained. A
constant source width alone does not make these terms small uniformly in u
at fixed nonzero background curvature. A possible source-dependent critical
shift does not justify moving a contour through hard cuts. These are still
explicit obligations for a connected source-return expansion.

## 6. The entire strong good event enters the relative chart

Let S_c(U) be the actual root-to-root straight transporter. Suppose

    max_(all fine p)||I-U_p||op<delta_f,
    max_c ||V_c-S_c(U)||op<eta.                             (CB21)

Both include wrapping labels. Tree-gauge U by the exact pinned transformation
in (CB4). For every internal non-tree edge, the resulting W_e is the
holonomy of a root-tree loop inside one block. For a crossing edge compare
its root-tree path with S_c in the lifted two-block brick. These are
nonabelian word comparisons, not replacements by linear curvature.

A useful nonabelian grid-combing proof is explicit. For an edge x->y,
compare the canonical coordinate-order root paths rho_x and rho_y.
In rho_x followed by that edge, commute its last step past later-coordinate
steps, one elementary plaquette interchange at a time, and cancel inverse
adjacent steps. It becomes rho_y. At most the sum of the box widths
interchanges is needed per edge. Telescoping these dressed-edge loops
along a path gives a product of conjugated plaquette holonomies, with no
commutativity assumption. All intermediate vertices and faces remain in
the same lifted box. An internal tree loop or crossing-versus-straight loop
has length <6L, and width sum <5L; therefore b0=30L² bounds the number of
plaquettes, with multiplicity. For unitaries, the distance of their product
from I is at most the sum of their distances. It follows that

    ||W_e-I||op <=b0 delta_f                    (internal),
    ||W_e-V_c||op <=b0 delta_f+eta              (crossing). (CB22)

If s=b0 delta_f+eta<=1/2, every eigenangle of the relative link is <=2s.
If also `2sqrt(N)s<r_ch<pi/sqrt(N)`, its principal logarithm has HS norm
<r_ch and trace zero: the sum of eigenangles is an integer multiple of
2pi whose absolute value is <pi. Thus **every configuration satisfying
(CB21) lies in the relative chart of (CB19)**. Holonomies are carried by V;
they have not been assumed small or discarded.

There is an independent coarse-curvature consequence. The four straight
root paths bound an L-by-L fine square, so its Wilson loop is a product
of L² conjugated fine plaquettes. Replacing its four links S_c by V_c
costs at most 4eta. Hence

    delta_V <= L² delta_f+4eta.                            (CB23)

One can choose positive fixed delta_f,eta so that

    L² delta_f+4eta <=delta_star,
    2sqrt(N)(b0 delta_f+eta)<r/2,
    delta_f<=epsilon_1,

and, when consuming the Sea estimates, also their stricter Sea9 relations.
These choices are independent of volume and u, though conservative.

Let G denote (CB21). In the exact Sea history convention it is
`Psi_(empty,empty)`: no defective closed fine cell, and no clean coarse
mismatch. Under the displayed choices it implies the original interior
cut and its entire fixed-V integral is given by (CB19) with chi_cut replaced
by 1_G. Theta is still required to avoid exponential preimages. V outside
the curvature class has an empty G sector by (CB23). The original measure
still has the exact decomposition

    Z_cut^epsilon[Xi](V)=Z_G^epsilon[Xi](V)
                 +int w_0 exp(-delta S_epsilon) chi_cut 1_(G^c) Xi dU. (CB24)

The second term is retained and carries every nonempty (A,C) history,
including dirty collars and correlated original failure insertions.
Sea7/Sea11 price these histories only after their prescribed coarse
integration. No fixed-V probability, logarithm or local-hole estimate
follows from those integrated prices. Interior-only cuts by themselves
imply neither (CB21) nor (CB23). This construction covers the global strong
good sector; arbitrary punctured regions and their frozen collars remain
outside the theorem.

## 7. Evidence, literature and remaining producer

Criteria were written before new checker execution in
`checks/covariant_soft_background_criteria.md`. The independent matrix-group
check uses centered T=2 and T=3 blocks, noncommuting SU(2) coarse matrices,
every fine plaquette, 15,552 actual contour words in each volume, wrapping
lifted bricks and
large flat holonomies. Separate quaternion code generates the actual paths,
computes analytic reverse derivatives of the full normalized density,
checks those derivatives against differences and matrix multiplication,
and constructs finite-u critical shifts. It retains all 244*3 free
coordinates in its period-one coarse sector and in Bloch tests.

Translation-invariant coarse data give a per-cell action independent of
T>=2. A stationary point in that sector is a full-torus stationary point by
translation symmetry. Numerical spectral and shift samples are diagnostics;
the uniform, inhomogeneous statement is proved by (CB6)–(CB18). The numerical
curvatures are not advertised as satisfying the tiny conservative bound
(CB12). Wrong transport, missing finite-u spread/Haar, missing shift,
wrong colour determinant, far-seam, discarded holonomy and SU(3) chart
convention controls are retained with their outputs. The first combined
run reported 46/46 with NumPy LU warnings despite finite log determinants;
its exact source/output/stderr are preserved. The final positive determinant
uses Cholesky and an eigenvalue cross-check, with nonfinite JSON forbidden.
The final main run reports 49/49; the independent matrix geometry reports
16/16 at T=2 and 16/16 at T=3. Earlier overlapping runs are not added again.
The checker's values retain the Wilson background constant while subtracting
the known kernel vacuum constant; its gradients equal (CB7), and its source
vacuum check retains the original Wilson term. Exact bytes and outputs are
bound by the receipt.

Versioned primary pages were checked again on 2026-10-29; matching original
PDF/text caches remain under /tmp and are hash-bound in the primary manifest.
Dimock's [1410.2798v3](https://arxiv.org/abs/1410.2798v3), §§3.7–3.10,
pp.16–21, gives the hard-constraint abelian C-coordinate/resolvent/independent
Gaussian construction already read in the identity unit. It does not supply
this d=4 finite-kappa SU(N) Hessian or the nonlinear critical shift.
Dimock's [1212.5562v2](https://arxiv.org/abs/1212.5562v2), Appendix F,
pp.91–92, starts its integration theorem with ultralocal variables and local
small interactions. Whitening in (CB19) has not yet verified those connected
activity hypotheses. The prior mode-counting warning in
CROSSOVER_LITERATURE_BRIDGE_ASTRA remains binding: operator bounds do not
remove local trace/HS or extensive determinant costs.

The next missing producer is a convergent source-labelled local expansion
of the exact expectation in (CB19), with its pulled-back strong-good/cut
indicators, all vacuum/source terms, determinant mode costs and connected
background derivatives. It must then join the nonempty correlated histories
in (CB24) on their actual required domains. No integrated sea price,
Gaussian mass or local density minimum is a substitute for that bound.
Governance reuses the session's physics-loop/review-loop and applicable
methodology reads at the coordinator-reconfirmed immutable current-main
revision ca2bc7ddf64790da96cd43d42017d000fbfe4808. The axiom memo, primitive
procedure and registry supply no dynamics input here; the Wilson law is
explicit model input. No new axiom, primitive or audit verdict is introduced.
Both continuum targets remain OPEN. Root owns independent review,
publication, shared summaries and audit status; this packet is author work.
