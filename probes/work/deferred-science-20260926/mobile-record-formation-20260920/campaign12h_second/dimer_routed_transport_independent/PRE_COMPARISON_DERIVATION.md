# Independent routed-transport reconstruction before author controls

2026-09-21. The complete note was read at SHA-256
`5fd0f707110dba04fbebb01a64d3fc1925fca6358c6245cc57f7dfe6e691f479`.
The author checker/results remain unopened. I reconstruct the finite-state
replacement proof here without importing or reading the older primary
fluctuation note. The fixed graph formation theorem is reused only for the
last section, from the previously checked geometric process.

## Preliminary finding

F1: Section3 allows gamma=0, but Section6 states four propagating transverse
modes without qualification. For gamma=0 all thirteen probability-tangent
modes are static. The four-propagating/nine-static count needs gamma!=0 at
the already stipulated nonzero Fourier mode and positive orbit masses. Root
has been notified and has agreed to retain the frozen source until review.
This does not invalidate the main finite-mode propagation formula, which
correctly becomes the identity propagator at gamma=0.

## Routing, local rates and stationarity

Identifying pairs by their black endpoint, q_delta is the composition of a
black-to-white translation with the white-to-pair bijection. It is a
permutation and q_delta^-1(v)=w_v-delta. A nonfixed step has displacement
delta-d_(q_delta u), with forward scalar increment1 or2. Summing these
unwrapped increments around a cycle yields a positive multiple of N. Thus
its length is at least N/2; N>=8 ensures four distinct context pairs. Fixed
points are omitted. Every nonmatching lattice edge gives a channel of the
connected contracted graph. Multiplicity is retained.

Exchanging the two black records and the two white records is an actual
permutation of four distinct occupied sites. The black and white displacement
vectors each have L1 length2, and antipodal partnerships are preserved. This
is an atomic two-step-range event, not a sequential vacancy slide.

S_delta is symmetric in its color arguments and has absolute value at most
|gamma|/2. The drive bound2|gamma| is attained. Endpoint exchange negates h,
so the actual rate has positive floor(k0-|gamma|)/2 and symmetric part k0/2.
On each nontrivial routing cycle the sums of the nearest-position terms and
the distance-two terms cancel separately by shifts. Hence sum h=0 pointwise.
Product weights are invariant under all swaps; the incoming-minus-outgoing
rate sum vanishes. This proves stationarity of every product pi_p and each
uniform fixed-count law. Positive transpositions on the connected contracted
graph generate every arrangement of a fixed multiset, proving sector
irreducibility without any geometric mixing assertion.

After interchanging parity classes, pair labels give
q'_delta=q_(-delta)^-1. Its edge and four-position context are reversed.
Reversal negates the drive while S_delta=-S_(-delta) supplies the second
minus sign. The rates and actual records exchanged agree. Proper cubic
covariance follows from the cross-product transformation and is checked
independently for all24 rotations. No reflection assignment is imported.

Conditioning on endpoint colors a,b gives E[h|a,b]=2[(Sp)_a-(Sp)_b]. The
current before the outer half is therefore2p_a[(Sp)_a-p.Sp], exactly Eq.(5).
The six-direction factor and physical displacement give the matrix identity

    sum_(delta,u) (delta-d_(q_delta u)) delta^T = 2K I.

This verifies Eq.(7), including for maximal winding, but alone is not a
fluctuation replacement argument.

## Uniform block proof

Fix radius l and eventually N>2l+3. C_l is the image of the connected
all-site cube under dimer contraction. Every one of its pair vertices has
an endpoint in that cube, so images of internal lattice edges connect all
of C_l. The actual routing graph contains those edges. C_l has Theta(l^3)
vertices and differs from its contained ordinary black-site cube B_l only
by O(l^2) additional vertices. Radius l>=6 contains every active four-pair
current footprint. Fixed routing points have zero spatial coefficient and
are omitted from the canonical-current step.

Conditional on outside colors and the counts in C_l, pi_p is uniform in the
block count sector. All internal transpositions connect it. The bounded
block size and finitely many matching patterns/count sectors give a finite
maximum Poincare constant A_l, independent of N and the global matching.
No polynomial growth estimate for A_l is required. The global symmetric
generator is exactly the routing swap form with rate k0/2 per channel;
multiple channels add. In particular it dominates this internal form.

For h_u=j_u-E[j_u|counts(C_l(u))], conditional centering gives
E[h_u|outside,counts(C_l(u))]=0. It also makes h_u orthogonal to every
global-count function. For any test f, conditional Poincare bounds
|<h_u,f>| by a constant times the square root of A_l times the internal
Dirichlet energy. Sum over u with bounded deterministic weights, use
Cauchy--Schwarz, and note that each edge lies in only O(l^3) blocks. The
factor K^-1/2 cancels the number of block centers, giving Eq.(10).

The full chain need not be reversible. On the complement of its
global-count kernel solve -S f=F, S=(L+L*)/2 under the stationary law.
The forward and stationary reversed martingales add to2 integral F. Each
has second moment2t<f,-Sf>, giving

    E|integral_0^t F(eta_s)ds|^2 <= 2t ||F||_(-1,S)^2.

For the N-accelerated chain the right side divides by N. Real and imaginary
parts handle complex Fourier weights. All ingredients are finite-state;
no sector condition on the antisymmetric part or reversibility is assumed.

The canonical conditional law samples the distinct footprint without
replacement from n_C=Theta(l^3) colors. Coupling with replacement shows
a uniform O(1/n_C) difference for any bounded footprint function. The
product current is a fixed polynomial J_delta. Taylor expansion at fixed
full-support p and the fourth moment of its independent empirical average
give a centered remainder W with E|W|^2<=C/n_C^2. Its mean is exactly zero
because E hat j=J_delta(p) and E(q_C-p)=0. Disjoint blocks are independent;
the O(l^3) overlap bound gives C/l^3 for the normalized weighted spatial
sum and C t^2/l^3 for its time integral by stationarity.

For one block, C_l contains B_l and r=O(l^2) extra black pair labels.
For a scalar independent unit-variance color component the exact variance
of q_C-q_l is r/[|C_l||B_l|]=O(l^-4). The general finite color covariance
only changes a constant. A black-cube shift by any allowed displacement
of L1 length<=2 has O(l^2) boundary sites, hence the same O(l^-4) variance.
The normalized weighted sum has squared L2 norm O(l^-1) after the overlap
bound. These estimates need no probability law or regularity of M_N.

## The variable-direction correction

For phi(u)=exp(-iQ.u/N), the exact drift coefficient is
a_(delta,u)=N[phi(q_delta u)-phi(u)], including the outer factor1/2. It
is uniformly bounded, and constant currents cancel exactly under each
permutation. At fixed l its Taylor expansion has remainder O(1/N), since
each unwrapped displacement has length2. The centered linear error has
squared L2 bound C_l/N^2.

The delta part sums to -i A(Q) times the black-cube averaged Fourier field.
Its translation multiplier tends to1 at fixed l. For the dimer-direction
part, setting v=q_delta u puts every dimer direction at the common site v.
Subtract phi(v)[q_l(v)-p] inside the delta sum. Its coefficient is zero by
sum_delta A_delta=0. What remains has two pieces: a phase difference O(1/N)
and a block-average difference across q_delta^-1(v)-v, of length at most2.
The former has squared L2 bound C_l/N^2; the latter has C/l by the preceding
boundary/overlap argument. q_delta being a permutation and having bounded
displacement also keeps these shifted supports' overlaps uniformly O(l^3).
Thus Eq.(15) is controlled for arbitrary deterministic matching patterns,
not just in expectation or after geometry averaging.

Combining the centered-current, canonical and boundary steps gives Eq.(16),
with constants allowed to depend on fixed l,p,Q,gamma,k0,T but not N or M_N.
The jump bracket is O(T/N) because O(K) bounded channels each change the
mode by O(1/(N sqrt(K))). Variation of constants can use the integrated
drift error R(t) by integration by parts. Bounds on sup_(t<=T) E|R(t)|^2
and the corresponding martingale second moments suffice; no expectation
of a time supremum is invoked. First take N->infinity at fixed l, then
l->infinity. This proves matching-uniform fixed-time L2 propagation.

The independent pair-color central limit theorem is elementary. On the
black subgroup the only extra Fourier alias is the half-period diagonal
character; it cannot meet differences of a fixed finite list of integer
modes once N is sufficiently large. Covariances are C=diag(p)-pp^T, with
the usual opposite-mode conjugacy. Finite lists of times follow from the
L2 approximation. Neither high-mode/time-uniform limits nor an evolving
nonstationary color law follows from this argument.

An independent deterministic countercontrol shows why the direction step
is necessary. In a period-eight irregular matching, the coefficient
r_u=(d_(q_+e1 u))_1-(d_(q_-e1 u))_1 has sum0, but the normalized iid-color
sum has variance65/128. Repeating the matching at larger volumes keeps
that unsmoothed variance. Black-cube averaging gives exact variances1/52
at l=1 and25951/1372554304 at l=10. This is consistent with the proof's
averaging step; it refutes substituting the mean-current cancellation alone
for a fluctuation estimate.

## Color code, spectrum and ordered formation

The polynomial f is even and transforms as a vector under all24 proper
signed-coordinate rotations. The strict9/10 threshold selects a unique
dominant component; the remaining zero/boundary/tie sets are algebraic
null sets. The stated A and B examples lie in interiors of their respective
regions. Proper rotations are transitive on the six A and eight B colors,
and every color region is antipodally even. Thus g0 has the stated color
masses and each color-restricted first moment of n vanishes.

Integrating the birth density gives beta on each vacant edge, and integrating
within each even color gives beta p_a. The mixture over available neighbor
directions gives Eq.(20); its dependence is on nearest-neighbor vacancy
conditions. The |epsilon|<1 assumption supplies positivity. The code is a
classically supplied function of exact projector content, not an asserted
unknown-qubit measurement.

At orbit-isotropy, the full current derivative has X flux
-gamma rho_A delta cross Y/3 and Y flux gamma rho_B delta cross X. These
give the signs in Eq.(17). For gamma!=0 and Q!=0 the thirteen-dimensional
tangent has four propagating modes and nine static modes, retaining the
two longitudinal and seven additional color directions. Gamma=0 is F1.
The site sum differs from sqrt(2) times the pair field by an iid centered
sum whose squared L2 norm is O(N^-2), uniformly in geometry; hence its
limiting covariance is2C, not C. The geometric Gauss field is static during
all full-state pair exchanges and is not the propagating color field.

At partial packing the fallback rule is local and parity independent, but
cycle telescoping can fail; product stationarity there is not used. The
projection onto geometry and accumulated color counts has geometric rates
independent of colors and birth increments with conditional law p. Thus
the final counts are multinomial and independent of the geometric history.
The previously checked finite filling result remains applicable because
these exchanges do not change geometry. At each fixed N, after filling,
each color-count sector is a finite irreducible chain with uniform law.
Its late-time limit, mixed over the multinomial counts, is exactly pi_p,
independent of final geometry. This does not assert independence at first
completion. Fine-key memory need not mix. The order is fixed-volume filling,
additional time tending to infinity, then the stationary N limit; an optional
fixed-volume beta->0 selection limit is separate. No preparation-time or
simultaneous schedule is proved.

## Controls and failed route

The independent programs test maximal-winding and irregular matchings at
N=8,12,16; exact routing/parity identities; connected radius-six footprints;
all bounded cube shifts; all14^4 contexts in each direction for sharp rate
bounds; nonisotropic full-support product currents; all24 proper rotations;
the exact full14 characteristic polynomial and gamma-zero degeneration;
45 complete canonical count profiles; and a complete256-state nonreversible
single-exceptional-color sector. The latter checks exact stationarity and
symmetric forms, with numerical stationary integrated-variance comparisons
against the forward/backward bound. These finite controls support, and do
not replace, the uniform proof above.

The first fixture attempt tried plaquette flips from a maximal-winding
matching. It has no flippable plaquettes, so the purported irregular fixtures
remained unchanged and the deliberately nonzero direction-variance assertion
failed. The source, full logs and receipt are preserved. Irregular fixtures
were then initialized from a separate ordinary columnar matching. The frozen
winding example remains a valid control. No primary source or target was
changed. All corrected runs passed with empty stderr.
