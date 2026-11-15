# Independent reasoning frozen before author packaging

Review scope: the 617-line original-law local-coercivity and conditional-tail
unit in CUT_SECTOR_COERCIVITY_ASTRA.md, source SHA256 4e6c70786aa4458293c4fe7294767128253477176f9eea87b7720254d62a159e.
Freeze time: 2026-10-29T23:11:08.262725+00:00.

I did not author this unit. This is same-family/fresh-context review. Astra/max
was requested by the owner; the worker cannot independently observe the
serving backend. No nested worker or numerical experiment was launched.
The producer source and necessary mathematical inputs were read before this
freeze. Its receipt, read manifest, mechanical checker and outputs have NOT
been inspected. This file freezes mathematical reconstruction and provisional
findings before those author artifacts can influence the review. It is not a
final review verdict and does not confer audit standing.

## Exact target and proof dependencies

The target is a finite-volume theorem uniform in coarse torus side T, with
fixed N>=2, odd L>=3, kappa in a compact positive interval, u>=1, arbitrary
fixed real V, and real original Wilson sources |e_p|<=rho<1. It supplies
all-compact absolute energy coercivity, Haar normalizer bounds, a conditional
excess-energy tail under the additional explicit interior-cut ceiling, and
an alternative local-reference tail for any positive interior cut. The latter
retains its actual exterior/source/V cost. The SA/H consumers have their own
explicitly narrower domains. The full Yang--Mills construction is not the
statement being reviewed.

The original model and paired S4-prime path conventions match H1--H5,
CB1--CB4, F1--F2, LINEAR_PACKAGE 1.2--1.3 and the original Decision-4 formula.
The all-compact proof and two caps are reconstructed below rather than taken
from those predecessors. CS30--32 use the actual SA fixed white cube, scalar
row estimates, small critical branch, and CB good-to-chart map. CS33 uses the
H24 full-reader cluster expansion on its actual source/u/completion domain.
Prior CC or SA review is not a proof of these new consumers.

## Independent reconstruction

1. Exact group quotient and conditional. For each block, reconstruct the
original tree links recursively from one group variable per nonroot vertex;
reconstruct each non-tree link as g_x^{-1} W_e g_y. This is triangular in the
tree variables, and left/right Haar translations preserve every conditional
link measure. Thus there are 4L^4-(L^4-1)=3L^4+1 free positive links per block,
with no determinant and unit integrated tree volume. Root-pinned gauge
transformations leave all root-to-root paired words unchanged and conjugate
plaquettes. Original sources/cuts are invariant. Fixing the free exterior is
a genuine disintegration of this quotient law; it is not the same operation
as freezing the original ungauged exterior. Only interior plaquettes in R
remain in the conditional cut. Original action and normalizer factors with
no reader in J_R cancel. A small cap with all interior free links near I
proves the conditional denominator positive for every admissible exterior.

A free edge meets six plaquettes. An internal edge can only be read by a
kernel with its own block as endpoint; a crossing edge is read only by its
labelled coarse face. Thus |P_R|<=6m_R and |C_R|<=8|R|. Endpoints of links
owned by R lie in R or its four outgoing neighbors, giving |K_R|<=5|R|.
Full factor readers lie within sup-distance one, hence at most 81|R| blocks.
Inverse occurrences count as readers. At T=2 two opposite labelled faces
remain different; the extra periodic seam is excluded from each lifted brick.

2. All-compact nonabelian filling. In a rectangular lift choose sorted
coordinate root paths. For a directed edge, move its step through all later
coordinate steps. Each interchange introduces one conjugated oriented
plaquette, and at most the sum of the box widths is needed. The cancellations
are exact ordered group identities, including negative steps. Multiplying
these identities along a loop cancels all intermediate root paths. For the
actual paired word P and straight root path S, length(P S^{-1})<6L and
width-sum<5L. The same bound covers each dressed internal/crossing edge
comparison. Hence B=30L^2 is a safe multiplicity count without abelianization.
The actual word uses the same coordinate permutation at its endpoints and
has length at most 2*4h+L=5L-4; every path stays in its specified lifted brick.

For unitaries, telescope product(Q_j)-I and use unitary invariance of the
normalized HS norm, then Cauchy--Schwarz. A filling of q<=B plaquettes yields
squared defect <=2B sum_p n_p s(U_p). Averaging yields CS8; replacing each
n_p by B gives 2B^2 times the complete brick curvature sum. No principal log,
small curvature or polar maximizer enters. Variance identity CS9 follows by
expanding mean-square distance; m(M)>=average <P,M>=|M|_n^2 because every P
is an admissible SU(N) competitor. The upper bounds follow from
Cauchy--Schwarz and |P|_n=1.

Independently write d=|S-V|_n. Since m(M)>=<S,M>,
 d^2/2=<S-V,S> <= psi + d |S-M| <= psi + d sqrt(q).
Young's inequality d sqrt(q)<=d^2/4+q gives d^2<=4psi+4q.
This verifies the root-mismatch price with no all-N sign condition inherited
from STEP55's polar estimate. A crossing free link obeys
 |W-V|^2 <= 2|W-S|^2+2|S-V|^2
          <=20B^2 sum_brick s + 8psi.
Internal free edges have 2B^2 times block curvature. There are fewer than
4L^4 internal free edges per block and L^3 crossings per face. Each internal
plaquette is in eight incident labelled bricks, each single-face plaquette
in one, and a double-face plaquette in none. The total curvature coefficient
is 8B^2 L^4+160B^2 L^3=8B^2 L^3(L+20); phase coefficient is 8L^3.
This gives exactly CS12 with the minimum of the two positive coefficients.
Every plaquette contains a non-tree edge because a tree has no cycle. Thus
whole blocks and bricks with both endpoint blocks in R have all their
filling plaquettes in P_R and phases in C_R. No truncated-brick estimate
was used. For distinct fine/face witnesses, op-to-normalized-HS conversion
costs 1/N; fine witnesses contribute at most 2 sum s and face witnesses at
most 64B^2 sum s+4 sum psi. This verifies CS13--14 including overlap counts.

3. Actual SU(N) normalizer. The unnormalized-HS exponential chart of radius
r_H is injective. For eigenangles theta_i, |theta_i-theta_j|/2<=r_H; the
real root-plane Jacobian is sinc^2 of this angle, with N(N-1) scalar root
dimensions. This gives the stated probability-Haar cap constant c_H; no
angular proxy or deletion of a group direction is needed. For any actual
maximizer Q of <Q,M>, tangent stationarity gives f'(0)=0 for
f(s)=<exp(sA)Q,M>. Since ||M||op<=1,
 |f''(s)| <= ||A^2||trace/N = ||A||HS^2/N.
The phase loss is therefore at most ||A||HS^2/(2N). A cap of radius
r_H/sqrt(1+t) gives CS15. This includes M=0, singular means, and nonunique
maximizers, and differentiates no choice of maximizer. CS16 follows from
(1+kappa u)/(1+u)<=max(1,kappa_+). The normalizer remains in the density.

4. Cap near the conditional minimum. Compactness gives a minimizer in the
closed interior-cut domain. Axial tree combing needs at most
A_cut=3h plaquettes for an internal off-tree edge. Hence its principal log
has op norm <=2A_cut epsilon_1. The N-dependent CS17 ceiling puts the sum of
eigenangles strictly inside (-pi,pi), so it is traceless even for N>=3.
For a four-edge plaquette at contracted logs, let s be the sum of log norms;
s<=8A_cut epsilon_1<=1/4. Product differentiation gives ||P'||<=s,
||P''||<=s^2. The matrix log series yields
 ||(log P)''|| <= s^2/(1-s)+s^2/(1-s)^2 <6s^2.
The zero-endpoint Green kernel has integral t(1-t)/2, giving exactly
192A_cut^2 epsilon_1^2 t(1-t). The cut ceiling bounds this coefficient by
half the maximal endpoint eigenangle theta=2arcsin(epsilon_1/2). Thus
contracting t=1-32r/epsilon_1 creates at least 8r defect slack. Product
geodesic radius-r perturbations lose at most 4r. Crossing centers need no
logarithm or contraction. All m_R variables retain their Haar dimensions.

Moving any integrated link by at most d changes Wilson terms by at most
24(1+rho)m0|R|d and kernel phases by at most
16kappa_+ p_L |R|d: there are 6m_R plaquettes, 8|R| kernels, and phase psi
is two-Lipschitz in M. With d=(C_g+1)r, r=r_*/(1+u), the loss in uE is at
most b_cap|R|. The inverse normalizers in the denominator are >=1.
The cap mass is (c_H r_*^D)^m_R (1+u)^(-D m_R). The numerator has at most
C_norm^k_R(1+u)^(D k_R/2) exp[-u(e_R+Delta)]. Division yields CS21's exact
power D(m_R+k_R/2). The large conditional minimum cancels; no inference
that it is small or attained at U0 occurs.

5. The local replacement reference is a different cap. Setting J_R=U0
makes internal plaquettes in R equal I without changing the exterior. The
comparison phase phi=average |P-V|_n^2/2 satisfies E_R<=A_R since m<=1.
On the radius-s_*/sqrt(1+u) cap, each fine/paired word distance grows by at
most 4r/p_L r. Apply weighted Young to each square. Wilson error is
(1+1/zeta)*8r^2*6m_R(1+rho); kernel error is
(1+1/zeta)*p_L^2 r^2/2*8|R|kappa_+.
This is C_zeta exactly. The cap lies strictly inside the cut for every
positive epsilon_1. Its mass costs Dm_R/2, while the numerator normalizers
cost Dk_R/2. Thus CS25 has power D(m_R+k_R)/2 and retains
+(1+zeta)u A_ref with the correct sign.

For a boundary plaquette compare with its exact U0 word, not only with a
worst-case curvature constant. Its square gives
 (1+e_p)s(U_p(W^R)) <= 2(1+e_p)s(U0_p)+16(1+rho)beta^2.
A boundary kernel has phi<=p_L^2 beta^2/2; a nonboundary kernel has phi=0.
A reader involving an exterior free link must contain a J_R link owned by
partial_1 R. Six plaquettes/eight kernels per owner give CS26. Sum the first
inequality before applying delta_V: only actual local double-face coarse
plaquettes contribute, with their original source coefficients intact.
This proves both lines of CS27 and their constants. Full exterior word
readers, not defect cores alone, determine beta. The boundary can be large.
CS28 requires the displayed reference budget; CS29 follows by conditional
expectation with an exterior-measurable reference event. A source-varying
indicator gives a real inequality only, exactly as stated.

6. Actual SA complement. The scalar coordinates of the admitted CB chart
are HS-orthonormal and W_e=exp(a_e)U0_e. From the actual fixed SA cube,
 y=sigma^{-1}K_* C_0(a-b_0)=sigma^{-1}K_*^(1/2)(a-b_0).
The scalar absolute row sum is at most M_K M_C. Thus |y_i|>p implies some
scalar coordinate |a_j-b_0,j|>sigma p/M_T. Under CS31, some link log has
HS norm >sigma p/(2M_T). For principal angles in [-pi,pi],
 |exp(a)-I|_n >=2||a||HS/(pi sqrt(N)),
which gives exactly r_p=p/(pi M_T sqrt(u)). There is no missing sqrt(D)
in this lower bound: one large scalar coefficient already lower-bounds the
link HS norm. SA's upper-bound sqrt(D) has a different direction. One block
or both endpoint blocks supply the full local supports for the resulting
free-edge witness. The charge u c_link r_p^2 equals
c_link p^2/(pi^2 M_T^2). Fixed-size prefactors cost O(log u), and
p=(log(2+u))^alpha, alpha>1/2, beats that particular cost while
u^(-1/2)p^3 tends to zero. SA's source radius must still shrink for growing p.
The row bound supplies no localization of the witnessing scalar index j;
CS32 explicitly loses the white-witness location and pays any all-volume
union. It supplies neither a connected hard-event norm nor SA33.

The finite scalar row bounds consumed here can also be rebuilt from CB:
K_* has a uniform gap, finite range, and uniformly bounded block rows.
Exponential weight conjugation has small Schur norm for a fixed rate;
Neumann inversion bounds weighted resolvents. Summing their matrix entries
on the periodic lattice, with the full colour density, then integrating
s^{-1/2}/pi gives a finite scalar row bound for K_*^{-1/2}. The local analytic
Hessian bounds retain the centered normalizer and Haar term. The O(delta_V)
force plus uniformly invertible Hessian gives the O(delta_V) critical branch
by Banach contraction. This confirms the exact properties consumed here,
without borrowing the entire connected-source theorem as a new premise.

7. H and complex sources. H's successful activities are nonnegative for real
e and its finite returned polynomial contains 1. In H24, changing a link
can affect only cluster terms whose full support contains an endpoint block.
The root-sum bound and a union bound over K_R give
 |log G(W)-log G(W')|<=2|K_R|d_q.
The normalized tilt ratio is therefore bounded by exp(2|K_R|d_q). Failure
factors with complete collars disjoint from K_R are exterior measurable;
intersecting failures are excluded. This remains valid at fixed tree gauges,
then after their exact integration. H's gas source/u/completion restrictions
are essential; |e|<1 alone is not substituted for them.

For the H24 input itself, the animal sum has at most Delta^(2m-2) connected
sets through a root and at most 81 possible roots per collar vertex. The
exp((mu+1)|A(Y)|) majorant gives d_q. The repulsive graph-to-tree estimate
follows by grouping connected subgraphs by their unique ordered Kruskal tree;
the optional-extra-edge sum is either zero or a sign of magnitude one.
The rooted-tree recursion is bounded by exp(|A(Y)|), since the sum of child
weights intersecting A(Y) is <=d_q|A(Y)|<=|A(Y)|. Marking a polymer through
a fixed block cancels the factorial and gives H24. Uniform absolute
convergence identifies the logarithm by continuation from zero activity.
All labels are the full collars. No estimate of the normalized sea average
is supplied by this pointwise gas argument.

Finally |w_epsilon|=w_Re(epsilon). Taking absolute values inside H's local
numerators, retaining its fixed zero-source denominators and source
compensators, gives |t^epsilon|<=t^Re(epsilon); the finite positive gas gives
the matching envelope. CS29 is then an unnormalized complex-integral bound
relative to the actual positive real-source history integral. No complex
conditional probability, nonvanishing or zero-source normalization follows.
An event reading interiors replaced by H8 must be inside H8's joint integral.
Evaluating it afterward on the sea would change the event; CS explicitly
preserves this distinction.

## Provisional finding disposition

No binding mathematical defect found in the complete frozen CS source.
No author fix proposed at this stage. This is not a verdict on the full
4D Yang--Mills existence or physical continuum mass-gap problem. Connected
bad-region organization, absorption of the arbitrary exterior cost, hard
whitened-event support localization, the complex connected complement,
retained failures/holes, nonlinear multilevel flow, continuum existence and
physical gap are still open exactly as the producer states.

No numerical diagnostic was necessary to establish these finite-dimensional
proofs. No author diagnostic or earlier diagnostic has been reclassified as
independent evidence here. Numerical resource/lock execution was not triggered.
Primary Bałaban and Dimock sources were read for attribution and comparison;
no theorem or constant from them is imported into the proof.
