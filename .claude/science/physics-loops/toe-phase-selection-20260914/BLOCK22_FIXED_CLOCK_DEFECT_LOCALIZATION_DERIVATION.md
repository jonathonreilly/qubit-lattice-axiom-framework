# Block22: actual clock defect localization and a local flux repair

Personal derivation begun2026-09-15 03:51UTC. Active proof candidate; no
independent review, retained status, fixed-clock Gaussian limit or axiom
update is claimed. The campaign deadline remains2026-09-15 13:30:44UTC.

## Premises, provenance and the new obligation

The minimum framework premises are Lattice, Qubit, Admissibility and Record,
as stated in docs/MINIMAL_AXIOMS_2026-06-29.md at main
5deabeb698a27c2c3f68c5df685af2521ef15307. The approved primitive registry at
that revision contains minimal_axioms, scale_reference_primitive,
kinetic_isotropy_primitive and realized_state_primitive. The approved kinetic
primitive fixes structural space/time graining for the identified regulator;
the scale primitive fixes units and the realized-state primitive permits
pointwise evaluation. The Villain probability law, clock order, coupling,
selected Gibbs measure and physical photon identification are additional
downstream inputs or open bridges. The proof uses a four-dimensional Euclidean
cubic model consistent with that structural graining, without deriving its
identification with native formed records. No new axiom,
primitive, selected parameter or empirical target value is introduced.

The exact full-rank image/Fourier duality is already in blocks7,10–12 and18.
Re-deriving it alone would repeat existing support. The new question is
whether its multivariate centered bound controls connected defects in the
ACTUAL fixed-clock law and permits a local, gauge-invariant real lift of
its compact plaquette flux. Such a lift does not itself prove Gaussianity.

The earlier attempt to get the full Gaussian limit just by duality terminates
at the dual model's equivalent Gaussian-limit obligation. The conditional
coset route instead leaves the distribution of the conditional mean and
covariance to be controlled under the coupled magnetic marginal. Conditional
Gaussian approximations are not preserved by arbitrary mixtures. These
routes remain open at those specific estimates; no no-go is asserted.

Primary reading this block: Froehlich–Spencer preprint P/81/40, portions of
extracted pages15–18 and the discussion on pages44–70 (plus selected
preceding introduction text), and Ukawa–Windey–Guth PRD21(1980), sectionsV–VI
on pages8–13 plus part of sectionVII on page14. FS section2.11 proves
nonsummable two-point decay via covariance bounds; its page52 scaling-limit
remark is not a full Gaussian-limit theorem. UWG sectionVI explicitly labels
the low-density expansion unproved there and warns that rare defects can
change infrared physics. Those limitations inform the target; neither paper
is a hidden proof input to the finite estimates below. Exact scan formulae
will be visually checked before any formula is imported.

## 1. Exact full-flux image lattice, with multiplicities retained

Let D:C1->C2 be any finite integer incidence matrix, N>=1 an integer, and
beta>0. The normalized clock Villain law on theta=(2pi/N)ell,
ell in (Z/N)^E, has joint image weights

 exp[-beta||Dtheta-2pi k||²/2], k in Z^P.

Set X=s y with s=2pi sqrt(beta)/N and y=Dell-Nk. Its support is the
full-rank lattice Lambda=s Gamma_N, Gamma_N=D Z^E+N Z^P. For any y in
Gamma_N, the congruence Dell=y modN has exactly |ker(D modN)| solutions
ell moduloN; k is then uniquely determined. This multiplicity is independent
of y. Thus X is EXACTLY the centered lattice Gaussian with density
proportional to exp[-||X||²/2] on Lambda. No topology or prime-N condition
is used in this argument. A degenerate E=0 case still gives a full-rank
image lattice because N Z^P is included.

For an arbitrary full-rank Euclidean lattice Lambda and real h, Gaussian
Poisson summation after completing the square gives

 E exp<h,X> = exp(||h||²/2) Theta_Lambda(h)/Theta_Lambda(0),
 Theta_Lambda(h)=sum_(x in Lambda)exp[-||x-h||²/2].       (1)

The Fourier series of Theta has strictly positive Gaussian coefficients.
Pair opposite frequencies or apply the triangle inequality to obtain
0<Theta(h)<=Theta(0). Hence

 E exp<h,X> <= exp(||h||²/2).                           (2)

All series converge absolutely, as do their fixed finite-order derivatives.
The result is centered, not an all-tilt covariance estimate.

The dual lattice is Lambda*=(1/(2pi sqrt(beta)))L_N where
L_N={m in Z^P:D^T m in N Z^E}. Indeed N Z^P inclusion first forces
Gamma_N* subset (1/N)Z^P, and pairing with D Z^E gives the congruence.
Poisson with an imaginary source then yields

 E exp[i<h,X>]=exp[-||h||²/2] E exp<h,m/sqrt(beta)>,     (3)

where the last expectation is the positive Fourier law on L_N with weights
exp[-||m||²/(2beta)]. In particular Cov(X)+Cov(m/sqrt(beta))=I.
This is prior duality support, not the new result of the block. The image
and Fourier variables in(3) are DIFFERENT positive representations, not
jointly sampled electric/magnetic physical random fields.

## 2. A multivariate support bound and its connected-cluster consequence

Let Q be an integer field indexed by vertices of a graph of maximum degree
Delta>=1. Suppose every finitely supported real h obeys

 E exp<h,Q> <= exp[v||h||²/2], v>0.                    (4)

For a fixed finite set S of k sites and m>=k, sign decomposition and
Chernoff optimization give

 Pr(Q nonzero on S, sum_S |Q_i|>=m)
 <=2^k exp[-m²/(2vk)].                                (5)

For each sign choice use h=t sign on S; on the event the scalar projection
is at least m, and optimize t=m/(vk). No independence, conditional
probability or stochastic domination is assumed. The bound applies to all
integer magnitudes at once.

A connected set of k vertices containing a fixed root has at most
Delta^(2(k-1)) possibilities: choose a deterministic spanning tree and its
ordered depth-first walk of length2(k-1); the walk visits the set, so a
fixed canonical walk encoding is injective into the possible walks.
For the occupied component C(o), let M(C)=sum_C |Q_i|, with M=0 if the
root is empty. An infinite component is handled first by its connected
finite subsets. In finite volume, summing(5) over possible exact component
sets, while discarding the absence constraint outside the set, gives

 Pr(M(C(o))>=M)
 <=sum_(k>=1) Delta^(2(k-1))2^k
          exp[-max(M,k)²/(2vk)].                      (6)

For M,k>=1,
max(M,k)²/(2k)>=(M+k)/4. Thus if

 r=2 Delta² exp[-1/(4v)]<1,
 A=2 exp[-1/(4v)]/(1-r),

then

 Pr(M(C(o))>=M)<=min(1,A exp[-M/(4v)]).                (7)

This uniform bound passes to any local limit: a component of size at least
k contains a connected occupied set of size exactly k containing its root;
these are finite-cylinder events. Their bounds tend to zero. Hence there
is almost surely no infinite occupied component, and(7) follows for finite
components by increasing finite observations. The proof concerns the stated
law, not every boundary condition or real tilt.

## 3. Both exact defect marginals at fixed parameters

On a free four-dimensional cubic cochain complex, write B=d2 and d0 for
the vertex-edge map. The image magnetic charge is

 q=-B X/(2pi sqrt(beta)) in Z^(3-cells), d3q=0.

The Fourier electric current is

 a=D^T m/N in Z^edges, d0^T a=0.

Equation(2) for X and its Fourier analogue for m give covariance proxies
BB^T/(4pi²beta) and beta D^T D/N² respectively. The finite cubic Hodge bound
is ||B||²,||D||²<=16. To see the uniformity at free boundaries, write the
cubical complex as the graded tensor product of four finite interval
complexes. Each one-dimensional incidence has norm at most two. The
anticommutation of derivatives in different directions cancels the cross
terms in dd*+d*d, leaving a sum of four nonnegative interval Hodge
Laplacians, each bounded by four. Each d*d is bounded by the degree-specific
Hodge Laplacian. Consequently(4) holds with

 v_m=4/(pi²beta),
 v_e=16beta/N²=4/(pi²beta_dual),
 beta_dual=N²/(4pi²beta).                              (8)

The magnetic closure graph joins two3-cells sharing a4-cell, of degree at
most14. The electric closure graph joins edges sharing a vertex, also of
degree at most14. Boundary cells only reduce these maxima. Therefore(7)
applies separately to both exact marginals when

 392 exp[-pi²beta/16]<1,
 392 exp[-pi²beta_dual/16]<1.                           (9)

These are sufficient conservative conditions, not critical couplings.
The one-species threshold is16 log392/pi², about9.680. Fixed N and beta can
satisfy both. This controls connected defect mass in each positive marginal;
it does not remove either gas or their phase coupling in the partition
function. It does not assert a joint positive gas of both species.

## 4. Physical principal-flux clusters

The image q depends on the auxiliary Villain image. For a physical local
repair use instead u_p=principal((Dtheta)_p) in [-pi,pi), and
q_pr=B u/(2pi). Because u differs from Dtheta by integer multiples of2pi,
q_pr is integer and closed. The half-open convention fixes the pi tie;
oddness at this tie is not assumed. For any chosen image, |u_p|<=|X_p|/sqrt(beta).

Let eta=pi/3 and call a plaquette bad if |u_p|>=eta. For every finite S,

 Pr(S all bad)<=2^|S| exp[-beta eta² |S|/2].            (10)

This follows by sign decomposition of X using(2). A charged3-cell has six
boundary plaquettes and |sum signed u|>=2pi, so at least one is bad.
Join bad plaquettes whenever they share a4-cell. Each plaquette belongs to
at most four4-cells; each4-cell has24 plaquettes. Thus the maximum graph
degree is at most92. If adjacent charged3-cells share a4-cell, ANY chosen
bad plaquette from each also shares that4-cell. A bad plaquette belongs to
at most four3-cells. A connected charge component of k3-cells therefore
maps to a connected bad-plaquette set containing at least k/4 distinct
plaquettes. Each |q_pr|<=3, so a component of charge mass M requires at
least M/12 bad plaquettes in that same bad component.

For a root bad plaquette, animal counting in(10) gives

 Pr(|C_bad(p)|>=k)<=2 exp[-beta pi²/18]
                    [2*92² exp(-beta pi²/18)]^(k-1),  (11)

provided the displayed ratio is below1. A large component contains a
connected occupied set of size exactly k; that suffices for this bound.
The conservative threshold is18 log(2*92²)/pi², about17.758. The ratio is
less than1/2 for beta>18 log(4*92²)/pi², about19.022.

Put a_beta=beta pi²/18, p_beta=2 exp(-a_beta), and
r_beta=92²p_beta<1. A charged root3-cell c has a bad plaquette among its
six boundary faces. If its charge component has mass at least M, the
selected bad plaquette belongs to a bad component of size at least
ceil(M/12). Union over those six plaquettes in(11) gives

 Pr(M(C_q(c))>=M)<=min(1,6 p_beta r_beta^(ceil(M/12)-1))
                 <=min(1,C_q exp[-b_beta M]),          (12)
 C_q=6/92², b_beta=-log(r_beta)/12>0.

The bound |q_pr|<=3 used in M<=3|C_q| is conservative. On a consistently
oriented six-face cube the half-open convention actually excludes the two
extreme values +-3; that sharper fact is not needed. The selected bad
plaquettes form a connected SET, because an adjacent pair of charged
3-cells has its selected pair in a common4-cell; repeated selections are
allowed and only improve the cardinality lower bound using multiplicity4.

Every fixed-N free-box sequence has subsequential local limits on the
compact finite-alphabet link space. The bounded finite-range Villain
interaction gives the DLR condition by passing its finite conditional
identity against cylinder tests. Here no uniqueness or mixing is claimed.
All the estimates above pass to every such local limit. Fixed N makes the
principal-value map a function on a finite alphabet, so the pi tie creates
no discontinuity issue in this passage. On the full Z4 complex, q_pr is
closed and almost surely has only finite components.

## 5. An explicit local integer filling on the infinite lattice

This section concerns the full Z4 local-limit field, not a replacement of
finite free boundaries by a periodic Hodge operator. Fix a coordinate-axis
order for a mathematical representative. Dualize a finite closed integer
3-form component gamma to an integer1-cycle j on the dual cubic lattice.
Use the shifted dual lattice Z4+(1/2,1/2,1/2,1/2). The dual1-edge of a
primal3-cell (x,I) has complementary axis k, integer base x-e_k, and sign
epsilon(I,k). Closure d3 gamma=0 is equivalent to boundary j=0.
Let M=||gamma||_1=||j||_1 and let a be the coordinatewise minimum of all
vertices incident on j. A connected component has coordinate span at most
M+2, allowing the primal/dual offset.

Here is a direct integer chain contraction. Starting with j, successively
project coordinates i=0,1,2,3 to a_i. At step i all surviving edges have
axis k>=i. Edges of axis i project to zero. For an edge of axis k>i at
base x with coefficient c, add to the filling every oriented(i,k)square
at bases x with coordinate i running from a_i to x_i-1, each with
coefficient c; then project that edge's base coordinate i to a_i.
Coincident coefficients are summed. This is a finite operation.

For one edge e, the boundary of its strip equals

 e - P_i e - H_i(boundary e).

This is verified from the four oriented edges of a square. Since the
current chain is a cycle, the last term sums to zero. Thus each step
changes the cycle by the boundary of its added strips. After all four
projections no1-chain survives, and the total2-chain S obeys boundary S=j.
Projections contract the l1 norm; each strip has length at most M+2.
Conservative bounds are

 ||S||_1<=16M², ||S||_infinity<=4M,
 support in the coordinate box of j's vertices.        (13)

In these conventions boundary(star n)=-star(d n) for a primal2-form n.
Therefore take n_gamma=-star^-1 S. Then d2 n_gamma=gamma, its coefficients
are integers, and the same bounds hold. Its primal support lies within
l_infinity distance6M of a chosen primal root of gamma. The constants
allow all one-cell offsets and M>=1. This construction is translation
covariant for the fixed axis order and is odd under gamma->-gamma. It is
not claimed to be a canonical representative under all cubic rotations.
Different integer fillings leave the compact flux invariant.

## 6. The infinite sum is finite locally and has a finite-window estimate

Choose one deterministic root for each finite charge component, e.g. its
lexicographically least oriented3-cell. Define n=sum_gamma n_gamma.
For a fixed plaquette p, a component whose filling can contribute at p
has its root within distance6M of p. There are at most
4(12M+3)^4 possible oriented3-cell roots in this box. By(12),

 Pr(some contributing component has mass>=m)
 <=4 C_q sum_(M>=m) (12M+3)^4 exp[-b_beta M].          (14)

Here an event of exact mass M is bounded by the mass-at-least-M estimate;
requiring that the candidate root is the selected root only reduces it.
The sum is finite, and the corresponding sum with m=1 bounds the expected
number of contributing components. Hence n_p is a finite sum almost surely.
The same holds simultaneously at all countably many plaquettes. With(13),
Minkowski and the exponential tail imply n_p has every finite absolute
moment. Explicitly, for a root at distance d, its contribution is bounded
by4M 1_{M>=d/6}; (12) bounds its L^r norm by a polynomial in d times
exp[-b_beta d/(12r)]. Summing over O(d³) roots is finite for every r>=1.

A finite-window approximation is constructive. Observe u in a box of
radius R about p, calculate q on the3-cells whose whole boundaries are
visible, and retain only occupied components separated from the edge of
that observed q-domain by a complete one-cell collar. Such components are
true full-lattice components. Apply the same filling algorithm to them and
sum their contributions at p, defining n_p^(R). A true component of mass
M<= (R-4)/12 whose filling reaches p lies strictly inside this domain,
including its closure neighbors, and is retained. Thus for R>=16,

 Pr(n_p^(R)!=n_p)
 <=4 C_q sum_(M>(R-4)/12)(12M+3)^4 exp[-b_beta M]
 <=C_beta exp[-b_beta(R-4)/24],                        (15)
 C_beta=4 C_q sum_(M>=1)(12M+3)^4 exp[-b_beta M/2]<infinity.

A fixed one-cell interpretation of R and the collar must be used in the
runner. The loose factor12 and offset4 reserve more than the primal/dual
and boundary-computation offsets; no sharp localization radius is claimed.
This is an exponential error-probability approximation, not a deterministic
finite-range rule or an operator-norm locality theorem.

## 7. Gauge-invariant real flux repair and exact Wilson preservation

Set

 u_hat=u-2pi n(q_pr).                                  (16)

The local finiteness just proved permits applying the finite incidence
operator d2 term by term. Therefore d2 u_hat=0 exactly almost surely.
Each n coefficient is integer, so exp(i u_hat_p)=exp(i u_p) on every
plaquette. Both u and q_pr are functions of compact plaquette holonomies;
the fixed filling prescription makes u_hat a gauge-invariant measurable
function of those physical observables. It has all finite local moments
and the finite-window approximation(15).

For any finite integer link cycle C, choose a finite integer plaquette
chain Sigma with boundary Sigma=C. Contractibility of the full cubical
lattice supplies such a chain. The actual clock Wilson character satisfies

 W(C)=exp[i<u,Sigma>]=exp[i<u_hat,Sigma>].               (17)

Since d2 u_hat=0, the REAL number <u_hat,Sigma> is independent of the
finite spanning surface: two choices differ by a finite integer2-cycle,
which bounds a finite integer3-chain. This constructs a surface-independent
real holonomy lifting the compact character. Existence of a real connection
A with d1 A=u_hat follows from the same cubical contraction; no local or
canonical A is asserted.

The finite-clock aliases remain exact. Every u_hat_p is still a multiple
of2pi/N, so exp(iN u_hat_p)=1. The repaired law is not replaced by a
continuous Gaussian measure. Choosing another integer filling can change
the real holonomy by2pi times an integer while leaving(17) unchanged.
The construction preserves every original Wilson character and does not
select a new microscopic law or eliminate defects from its probability
weights.

## 8. Remaining inference boundary

Finite defect components do not imply independence of their locations,
orientations or densities. A local integer repair would preserve compact
Wilson characters but need not create Gaussian statistics. The current
fixed-N full-score limit still requires covariance homogenization and higher
cumulant control under the coupled law. No assertion that these estimates
follow from nonpercolation alone is intended.
