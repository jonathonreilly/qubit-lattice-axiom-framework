# Frozen real Gaussian producers for the actual two-step chart

Research derivation, 2026-11-09; independent check pending. This note supplies
covariance and local-remainder estimates, not a density forest identity,
convergent connected logarithm, or full compact response. The law is the actual
zero-source two-step SU(2) chain at terminal I, beta=u, both lambdas=kappa*u,
fixed odd L>=3, kappa>0, with the translated terminal-root fine forest and
all intermediate links retained. No moving critical point, source-dependent
precision, intermediate Wilson action, or bare-first-step transfer is used.
No numerical, network or Git operation. Only this file is written.

Inputs: `nonlinear-chart-response.md` (complete action, local derivative
bounds, chart geometry and covariance method) and `flat-two-step-bound.md`
(actual two-layer flat precision and its gap). Both were read in full during
this worker's coherent task. Their identities are recorded below. These are
provisional mathematical suppliers; this new consequence awaits checking.
The finite-range inverse/weighted argument follows the explicit elementary
Neumann method already used by these sources; no unverified MK engine is
imported. All norms needed here are defined directly.

## 1. Exact action and a uniform frozen precision

Let n be the number of retained group links, q=3n the real coordinate count,
and write U_e=exp(i a_e dot sigma) in the injective identity chart. Probability
Haar has density (2pi^2)^(-1) j(a_e) d^3a_e, where
j(a)=(sin|a|/|a|)^2, continuously extended at zero. Define

    Z(t)=integral_SU(2) exp(t w(Q)) dQ,  h(t)=log Z(t)-t,
    r_c(a)=|M_c(a)|,  psi_c=r_c-<output_c,M_c>,
    Phi_I(a)=W(U_0(a))+kappa sum_{both kernel levels,c} psi_c(a).

Tree links and terminal outputs are fixed I; intermediate outputs remain
variables. If q_u(U_0)=Z_fine(u)^(-1)exp[-u W(U_0)], the exact negative log
joint density relative to da on this chart is

    S_u(a)=log Z_fine(u)+n log(2pi^2)+u Phi_I(a)
               +sum_{both kernel levels,c} h(kappa*u*r_c(a))
               -sum_e log j(a_e).                            (1)

If the fine density is supplied unnormalized, omit only its actual common
constant log Z_fine; none of the estimates silently performs that omission.
Any alternate coordinate-independent convention is carried in S_u(0).
Formula (1) retains both kernel normalizers using the exact identity
-kappa*u<output,M>+log Z(kappa*u*r)=kappa*u*psi+h(kappa*u*r).
No expansion of these normalizers has been substituted in (1).

The density and each local term in (1) are invariant under simultaneous
conjugation. This fixes the identity and acts on its tangent as a direct sum
of adjoint SO(3) representations. There is no invariant linear functional:
restricting to one coordinate at a time proves this. Therefore

    grad S_u(0)=0.                                         (2)

This assertion is about the untruncated density at identity; it does not
require the Cartesian chart itself to be invariant under every rotation.

Set H_u=u^(-1) Hess S_u(0). The flat supplier gives, on the specified forest
slice, H_action=H_min+eta_u diag(V_0,V_1), where

    <a,H_min a>=||d_0 a_0||^2+kappa||a_1-Q_0 a_0||^2
                                      +kappa||Q_1 a_1||^2,
    eta_u=kappa[1-Z'(kappa*u)/Z(kappa*u)] in [0,kappa].

The exact actual-Q gap is g I<=H_min, g=g(L,kappa)>0. Haar contributes
(2/(3u))I, hence

    H_u=H_action+(2/(3u))I,
    g I<=H_u<=M I,  u>=1,                                (3)

with fixed M enlarged from the flat supplier's upper bound. Each factor's
reader owners have nearest-neighbor terminal-cell diameter at most two.
The Haar term is diagonal, so H_u has range <=2 in that metric. Its absolute
scalar row sums are bounded by a fixed K_H: entries arise from a fixed finite
family of factor Hessians, each uniformly bounded after division by u, with
bounded incidence and reader counts. An operator upper bound alone would
not suffice to claim this row bound; the finite-template argument does.
All constants are independent of the periodic torus volume and u>=1.

## 2. Exponential covariance and a positive finite-range core

Let k=3(3L^8+1+4L^4) be the number of scalar retained coordinates per terminal
cell. For scalar index i let X(i) be its owner. Distances d are shortest
periodic nearest-neighbor terminal-cell distances. Choose M'>M, and put
r=1-g/M' in (0,1), gamma=-(log r)/2>0. For C_u=H_u^(-1), the Neumann series
and range two give for cell blocks X,Y

    ||(C_u)_(X,Y)||_op <=g^(-1) r^ceil(d(X,Y)/2).

Indeed powers below ceil(d/2) have zero such block and every remaining power
has operator norm <=r^j. In particular

    |(C_u)_(i,j)|<=g^(-1) exp[-gamma d(X(i),X(j))].       (4)

The deliberately loose count of cells at distance t is at most (2t+1)^4,
uniformly on every torus. Define the weighted absolute row norm

    M_beta(A)=sup_i sum_j exp[beta d(X(i),X(j))]|A_ij|.

For any fixed 0<beta<gamma, (4) bounds M_beta(C_u) uniformly. Fix a desired
small tolerance epsilon>0 and choose an integer R0>=1, to be fixed below,
independent of u and volume. Define by entrywise distance truncation

    (P_u)_ij=(C_u)_ij 1_{d(X(i),X(j))<=R0},
    (E_u)_ij=(C_u)_ij 1_{d(X(i),X(j))>R0}.               (5)

Both are real symmetric, C_u=P_u+E_u, and P_u has range R0. Equation (4)
gives the uniform tail estimate

    M_beta(E_u)<= (k/g) sum_{t>R0}(2t+1)^4 exp[-(gamma-beta)t] ->0. (6)

Truncation is not positivity-preserving in general. Here symmetry and Schur's
test give ||E_u||_op<=M_0(E_u), while C_u>=M^(-1)I by (3). Choose R0 so
M_0(E_u)<=1/(2M). Then

    P_u>=p0 I,  p0=1/(2M),
    ||P_u||_op<=U:=1/g+1/(2M),
    sup_i sum_j |(P_u)_ij|<=M_0(C_u)<=g_row<infinity.     (7)

Thus P_u is a strictly positive covariance core by a quantitative perturbation
argument, not by a claim about truncations in general. Increasing R0 also
makes (6) <=epsilon. P_u may depend on u; all bounds are uniform. E_u need
not be positive and is not here treated as a covariance of an independent
Gaussian field. The positive segment P_u+tE_u=(1-t)P_u+tC_u exists for
0<=t<=1, but no forest interpolation theorem is inferred from that fact.

## 3. Every principal core inverse has a uniform absolute row bound

Let I be any nonempty subset of scalar retained coordinates, with no shape
or connectedness condition, and put G_I=(P_u[I])^(-1). Principal restriction
preserves P_u[I]>=p0 I. We prove a stronger uniformity: the inverse row
constant can be fixed independently of R0 once (7)'s gap is ensured.

Fix a base cell X and diagonal weights W_i=exp(theta*d(X(i),X)), i in I.
The distance function is 1-Lipschitz. Since |P_ij|<=|C_ij|, both absolute row
and column sums of W P_u[I] W^(-1)-P_u[I] are at most

    A(theta)=(k/g) sum_{t>=0}(2t+1)^4 exp(-gamma*t)
                                                   [exp(theta*t)-1].

For 0<theta<=gamma/2, this tends to zero as theta tends to zero: the summand
is bounded by theta*t*exp(-gamma*t/2) times its fixed polynomial factor.
Choose theta>0 with A(theta)<=p0/2, independently of R0, I, u and volume.
Schur's test and the inverse perturbation formula then give

    ||[W P_u[I] W^(-1)]^(-1)||_op<=2/p0.

There is no restriction on the magnitude of the individual finite-volume
weights; only their pairwise ratios enter the perturbation bound. Taking
X=X(j) and looking at the i,j matrix entry yields

    |(G_I)_ij|<= (2/p0) exp[-theta*d(X(i),X(j))].          (8)

Consequently

    sup_{i in I} sum_{j in I}|(G_I)_ij|
       <=(2k/p0) sum_{t>=0}(2t+1)^4 exp(-theta*t)
       =:v_core<infinity.                                (9)

This one bound applies to every I and to all admissible R0, u and volumes.
A weighted row version holds with any exponent less than theta. This is the
weighted inverse/coercivity argument for arbitrary principal covariance
cores. It neither identifies a principal precision with a marginal inverse
nor assumes (P_u[I])^(-1) equals (P_u^(-1))[I]; those generally differ.
The empty I has no rows and the bound is vacuous. In particular increasing
R0 to reduce the remainder below does not force this inverse-row bound to
deteriorate.

## 4. Canonical-path remainder atoms and the pinned reader norm

For each ordered pair of cells X,Y choose a deterministic shortest
nearest-neighbor path: use a fixed coordinate order, the shortest signed
periodic displacement in each coordinate, and a fixed sign at ties. Reverse
paths may differ; their lengths are always d(X,Y). For i,j use that path
between X(i),X(j), denoted Gamma_ij, and the matrix atom

    E_ij e_i e_j^T with reader support Gamma_ij.

Summing ordered atoms gives exactly E_u; one may instead pair transposes
without changing the estimates by more than a fixed factor. The path includes
both endpoint cells and therefore both scalar endpoint readers. It introduces
no omitted quotient/orbit reader: these are matrix entries on already
specified retained coordinates. The separate local action vertices below
keep all original syntactic readers; their support is not replaced by a path.
Define the complete-cell pinned norm

    Pin_beta(E)=sup_x sum_{i,j: x in Gamma_ij}
                                exp[beta |Gamma_ij|]|E_ij|. (10)

If x is on a path of length t, both endpoints lie in N_t(x). There are at
most (2t+1)^8 ordered cell pairs in that ball squared, and at most k^2 scalar
pairs for each. This overcounts pairs with distance t but is a valid upper
bound. Thus, using E_ij=0 unless t>R0,

    Pin_beta(E_u)<= (exp(beta)*k^2/g) sum_{t>R0}(2t+1)^8
                                      exp[-(gamma-beta)t] ->0. (11)

This is uniform over x, u and periodic torus volume. It requires neither
translation invariance of individual entries nor a bound on path congestion
by a constant: the explicitly summed polynomial congestion suffices.
Consequently one fixed R0 makes both M_beta(E_u) and Pin_beta(E_u) arbitrarily
small, while retaining (7)–(9). The inverse-row constant v_core in (9) remains fixed as R0 increases, so
these remainder norms can also be made arbitrarily small relative to any
fixed function of that constant. This still does not check an unspecified
engine's other hypotheses.

## 5. Bounded local remainder vertices in the shrinking chart

Fix a finite exponent a_exp>5/2, p(u)=[log(2+u)]^a_exp, sigma=u^(-1/2),
and rho(u)=sigma*p(u). Define the product scalar chart |a_i|<rho(u), equivalently
|x_i|<p(u) after a=sigma*x. For sufficiently large fixed u_dagger, rho(u)
is inside the supplier's fixed smooth chart, all path means have r_c>=1/2,
and sigma*p(u)^3 is as small as desired. These statements hold for every
fixed finite a_exp; the lower threshold 5/2 is not needed for these producers
and is not used to claim any later engine's exponent condition.

Decompose S_u into its coordinate-independent vacuum constant and complete
local terms s_v: each fine plaquette; each full kernel term
kappa*u*psi_c+h(kappa*u*r_c), including its hidden output and all original
input readers; and each one-link Haar term -log j. Keep syntactic reader
supersets even if some Taylor coefficient happens to vanish. These terms
have bounded arity and incidence, hence finitely many vertices per cell
uniformly in volume (choose a reader cell deterministically as each vertex's
owner). A constant term without readers belongs to the vacuum factor.

Here is the needed third-derivative bound, including both normalizer levels.
The supplier's compact radial calculation gives for j=1,2,3

    |h^(j)(t)|<=K_j(1+t)^(-j),  t>=0.

All derivatives of r_c of orders <=3 are uniformly bounded on the fixed
smooth reader chart where r_c>=1/2. The chain rule for h(kappa*u*r_c)
contains terms h^(j)(kappa*u*r_c)(kappa*u)^j times products of derivatives
of r_c, for j<=3. Their coefficients are uniformly bounded since
(kappa*u)^j/(1+kappa*u*r_c)^j<=2^j. Thus the normalizer remainder's third
derivative costs O(1), not O(u^3). The complete leading psi_c and plaquette
terms have third derivatives O(u) by bounded word length and r_c>=1/2;
the smooth Haar term has O(1) derivatives. Therefore

    sup ||D^3 s_v||_op<=K u, u>=u_dagger,                 (12)

uniformly over vertices and their fixed reader-chart domains. Repeated word
occurrences are derivatives of the same coordinate, and are included in the
finite template bounds. No differentiation at r_c=0 is used or needed here.

Subtract each local term's full Taylor polynomial of degree two at identity:

    R_v(x)=s_v(sigma*x)-s_v(0)-sigma Ds_v(0)x
                                  -(sigma^2/2)D^2s_v(0)[x,x].

Taylor's integral remainder along the straight reader segment and bounded
arity yield, on its reader cube |x_i|<=p(u),

    |R_v(x)| <=K u sigma^3 p(u)^3=K sigma p(u)^3.         (13)

All linear terms sum to zero by (2) (in fact each invariant scalar term has
zero differential here). All quadratic terms sum to (1/2)x^T H_u x exactly.
Define W_v=e^(-R_v)-1 on the reader cube and W_v=0 off that cube. This
extension is measurable and bounded, with no derivative or continuity
assertion across its boundary. For sufficiently large u,

    ||W_v||_infinity<= exp(K sigma p^3)-1<=K' sigma p^3. (14)

It has exactly its declared finite reader support. No smooth cutoff extension
or small derivative norm of this extension is required for (14). An engine
that demands such derivatives would require additional work.

## 6. Exact restricted Gaussian identity and normalization

Let gamma_Cu be normalized real Gaussian measure on R^q with covariance C_u.
Let Box_p denote the product scalar cube. From (1),(2) and the local Taylor
identity, the actual unnormalized integral restricted to this physical chart
is exactly

    Z_chart(u)= e^(-S_u(0)) sigma^q (2pi)^(q/2)
                         (det H_u)^(-1/2)
                  E_gamma_Cu[1_Box_p product_v (1+W_v(x))]. (15)

If the original law includes its separate normalized Haar orbit dh, its
zero-source integral equals one and does not change (15). S_u(0) retains the
fine normalization convention, every h(kappa*u), and the coordinate Haar
constants n log(2pi^2). The scale Jacobian sigma^q and Gaussian determinant
are displayed rather than absorbed into a putative unit normalization.
The identity is only inside the product chart, where every vertex's reader
cube applies. Setting W_v to zero outside its reader cube does not extend
(15) to the full compact law without the indicator or complement sectors.

Equations (3)–(15) supply the requested frozen real producers: actual
uniform precision, exponential covariance, positive finite-range core,
small weighted and pinned remainder atoms, uniformly bounded arbitrary
principal core inverses, and bounded local complete-reader vertices. They
do not certify applicability or convergence of a density-forest/Mayer/log
engine, or other engine-specific geometric, interpolation and summability
hypotheses. Source derivatives, moving centers, complex covariances,
rough-sector gluing and full connected response remain outside this file.
No editable prompt or prior proof was changed.

Source SHA-256 identities:

| Source | SHA-256 |
|---|---|
| nonlinear-chart-response.md | 5edacc8ee78d54b7fb853fb34da3d8cceffd8eb0e476f8510d15048f8f10f2d1 |
| flat-two-step-bound.md | 0f028f694bb686cf4272d8620329f1f2e8535d8af9a2d028bbde6965cab3f03a |

Recovery: (7) uses small unweighted tail to preserve positivity; (8) uses
exponential entries and the principal gap to control weighted inversion;
(11) counts path-endpoint pairs with polynomial congestion; (12) uses the
normalizer's inverse-power derivative bounds on the fixed mean-nonzero
chart. Recheck these points if geometry, coordinate normalization or the
underlying two-step precision changes. No independent check is claimed here.
