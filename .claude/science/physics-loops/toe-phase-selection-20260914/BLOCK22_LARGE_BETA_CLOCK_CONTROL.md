# Block22: a same-model massive-score control for the local flux repair

Personal active derivation,2026-09-15. Proposed proof, not independently
reviewed. This is a positive exponential-clustering/white-noise limit theorem
for an explicit region of the SAME supplied isotropic finite-clock Villain
law. It is not a no-go for all clock parameters, the principal-penalty
Hamiltonian, emergent gauge theories, or the framework axioms.

The reason to do this control is scientific: exact, covariant, probability-
local Bianchi repair does not yet establish a nonzero Maxwell stiffness.
The regime below obeys the repair hypotheses while its physical score has
short-range correlations. The proposed fixed-coupling Haar result therefore
cannot simply be transferred to a fixed small clock order.

The auxiliary probability construction below uses the classical loss-network
method of Fernandez, Ferrari and Garcia, *Annals of Probability*29(2001),
902–937, especially sections3.4,4.1 and5.1. Those portions were read directly
in the authors' published PDF. The clock-specific polymer law, explicit
constants, free-boundary validity filters and variance witness are derived
here; no novelty is claimed for the general probability method. The proof
does not import their Ising-contour hypotheses without matching them.
Here large beta is the low-temperature/weak-coupling corner of the displayed
Villain law; it is not called strong gauge coupling.

## 1. Exact positive polymer law for physical plaquette residues

Use a finite contractible four-dimensional cubic complex with all its cells
and free boundary. For any integer N>=2, the image of d1 over Z_N is the
kernel of d2. Integer cubical contraction descends modulo N, so no prime-N
hypothesis is needed. Each closed plaquette-residue configuration has the
same number |ker(d1 modN)| of link preimages. After summing link variables,
the normalized law is therefore exactly

 mu(b) proportional to product_p w(b_p), d2 b=0 modN,
 w(r)=phi_beta(2pi r/N)/phi_beta(0), w(0)=1,
 phi_beta(u)=sum_(k in Z) exp[-beta(u-2pi k)²/2].        (1)

Represent residues by the principal integers. Connect nonzero plaquettes
when they share a3-cell. This graph has degree at most Delta=20. Each
connected support component is separately closed modulo N: any nonzero
terms in one3-cell constraint belong to the same component. Thus(1) is an
EXACT positive hard-core polymer gas. A polymer gamma is a connected
nonzero residue field closed modulo N; its activity is

 z_gamma=product_(p in support gamma) w(gamma_p).

Two polymers are incompatible if their supports overlap or have distance
one in the plaquette graph. Compatible families assemble uniquely into b.
This expansion retains physical principal magnetic defects; it does not
replace modulo-N closure by real closure.

Put alpha=sum_(r nonzero modN)w(r). Rooted connected-set counting gives

 sum_(gamma contains p, |gamma|=k) z_gamma
 <=Delta^(2(k-1)) alpha^k.                            (2)

The closure constraint was discarded only in this UPPER bound. Set

 T=alpha e/(1-400 alpha e)²,
 c=21 T.

The conditions400 alpha e<1 and c<1 will be used below. The simpler
sufficient condition1600 e alpha<=1 implies both, since then
c<=84/3600<1. The factor e reserves a spatial exponential weight; it is not
an assumed decay rate extracted from a numerical fit.

## 2. A direct loss-network construction and the dependence estimate

For every connected nonzero residue field gamma, including fields that do
NOT satisfy a closure condition, place an independent Poisson process of
proposed births on an AUXILIARY real time axis with rate z_gamma. Give every
proposal an independent exponential lifetime of mean one. In the
chosen domain, first reject a proposal unless its support is in that domain
and it satisfies the domain's modulo-N closure constraints. Among the valid
types, accept a proposal if no incompatible accepted polymer is alive at
its birth. This auxiliary time constructs a probability measure; it is not
physical or record time.

To determine acceptance, trace UNIVERSAL proposals backward: a possible
ancestor is an incompatible earlier proposal alive at the later proposal's
birth, even if its type will ultimately be rejected by a domain constraint. For
a fixed gamma, the expected number of such proposals of type eta is z_eta,
since the integral of exp(-u) over the positive age u is one. The same
identity iterates along a strictly backward sequence of proposal times.
All proposals on one path are distinct. The Poisson factorial-moment
formula hence bounds the expected number of any prescribed ancestral-type
paths by the product of their activities, without assuming different paths
are independent.

Weighted by polymer size, (2) gives

 sum_(eta incompatible gamma) z_eta e^|eta| |eta|
 <=21 |gamma| T = c |gamma|.                          (3)

The initial expected weighted family of proposals alive at time zero and
covering p is at most T. A path with n ancestors has total exponential-size
weighted expectation at most T c^n, with its last size as a positive weight.
In particular there is almost surely no infinite backward path. Each
proposal has finitely many ancestors almost surely, because the total
ancestor intensity is finite. The initial family is also finite. A locally
finite tree with no infinite ray is finite, so the complete dependency clan
for b_p is finite almost surely. Acceptance can be resolved from its oldest
members. This defines the stationary infinite-volume gas.
Overlapping clans assign the same accept/reject status: a proposal's complete
ancestor set is included in either clan that asks for its status, so induction
in birth-time order agrees. All relevant proposal times are distinct almost
surely. Time translation of the marked processes preserves their law and the
acceptance rule, giving stationarity. These consistency facts are separate
from the finite-dimensional detailed-balance computation below.

For a dependence path reaching plaquette-graph distance R from p, the union
of its successive incompatible connected supports is connected and contains
at most the sum of their sizes. Therefore that sum is at least R. Discarding
the final size weight only decreases the bound, and summing over path lengths
proves

 Pr(the dependency clan for b_p reaches distance R)
 <= [T/(1-c)] exp(-R).                                (4)

A finite-volume version of the birth/death process is reversible for the
hard-core gas: adding gamma has rate z_gamma and removing it has rate one,
whose detailed-balance ratio is precisely its activity. Its unique stationary
law is(1). Use the same universal proposals for the finite and infinite laws. A
free-boundary polymer can end at the boundary and need not be closed after
zero extension; it is not silently identified with an infinite-lattice
polymer. Instead, the two validity filters agree for every proposal whose
support and closure neighborhood are strictly inside the box. If the
universal clan stays that far inside, both constructions agree. A fixed
one-cell collar is absorbed into the distance in(4). Thus(4) identifies the
unique free-box bulk limit and bounds its boundary error.
No arbitrary-boundary uniqueness theorem is needed here.

For bounded functions F,G of plaquette sets S,T separated by distance d,
truncate their proposal constructions to disjoint neighborhoods of radius
floor(d/3). The truncated functions use disjoint collections of independent
Poisson processes and are independent. A union bound in(4), followed by
the bounded-function covariance estimate, gives

 |Cov(F,G)| <= C0 ||F||_infinity ||G||_infinity
                  (|S|+|T|) exp[-floor(d/3)],          (5)

with C0=4T/(1-c). Indeed replacing either bounded function changes its
expectation or a bounded product expectation by at most twice its supremum
norm times its replacement-error probability. Apply this separately to
the product expectation and the product of expectations. Each plaquette-graph
step changes its base coordinate by at most one in each direction. Therefore
graph distance is at least the l_infinity separation of the bases; coordinate
corridors below need no hidden adverse distance conversion. In particular all
component score covariances are absolutely summable. This is an actual
coupling proof; low defect density alone was not used as a mixing theorem.

## 3. A concrete overlap with the repair regime: N=3, beta>=20

For |u|<=pi, grouping the two outward image sequences gives

 phi_beta(u)<=2 exp[-beta dist(u,2pi Z)²/2]
                         /(1-exp[-2pi²beta]).

The inequality uses (|u|+2pi n)²>=u²+4pi²n for n>=0, and
phi_beta(0)>=1. Hence

 alpha<=2(N-1)exp[-2pi²beta/N²]/(1-exp[-2pi²beta]).      (6)

At N=3,beta>=20, pi>3 bounds this by8 exp(-40), which satisfies
1600 e alpha<1 with a very wide margin. The principal-flux repair condition
also holds:2*92² exp(-beta pi²/18)<1, as established in the companion.
Thus the SAME actual clock law has both the covariant closed real flux
representative and the exponential physical-score correlations(5).
These are conservative sufficient parameters, not transition locations.

The normalized real score is

 Y_p=-beta^(-1/2)(log phi_beta)'(u_p).

For N=3, oddness and the three principal values give exactly

 Y_p=y_beta b_p, y_beta=Y(2pi/3)>0, b_p in{-1,0,1}.    (7)

To check strict positivity without an imported monotonicity theorem, the
k=0 derivative contribution has magnitude
u exp(-beta u²/2) at u=2pi/3. The ratio of ALL opposite-sign contributions
k>=1 to that term is at most

 sum_(n>=1)(3n-1)exp[-2pi²beta(n²-2n/3)]
 <=r(2+r)/(1-r)², r=exp[-2pi²beta/3].

For beta>=1 this is less than one. All k<=-1 terms have the same derivative
sign as k=0 and only strengthen it. Thus phi_beta'(2pi/3)<0 and(7) holds.

## 4. The actual score has a positive white-noise scaling covariance

Exponential summability gives the finite integrated covariance tensor

 Xi_(I,J)=sum_(x in Z4) Cov(Y_I(0),Y_J(x)).             (8)

The free-box bulk state is translation invariant, charge-conjugation
invariant and invariant under signed coordinate permutations, by the unique
bulk construction and the symmetries of the weights. On the six oriented
2-form components, sign flips kill all off-diagonal entries of Xi and
coordinate permutations equate the diagonals. Thus Xi=chi I, chi>=0.

At N=3, chi is strictly positive. Here is a local conditional-variance
argument which avoids inferring positivity from a finite sample. Choose two
original links forming an oriented L on one(0,1)plaquette: a0(0)=1 and
a1(e0)=1. Let P be the finite set of ALL links on plaquettes incident on
these two links. Compare two assignments to P: all values zero, and those
two values one with every other P value zero. Every plaquette changed by
the assignments has its complete boundary in P. Hence the difference of
the sum of b_(0,1) is independent of every exterior link. The unwrapped
integer curl has zero total(0,1)sum. Exactly the common plaquette has curl2
and wraps to-1; all other changed curls lie in{-1,0,1}. The difference of
the principal-flux sum is therefore-3. By(7) the score-sum difference is
-3 y_beta, which is nonzero.

Here m=|P|=30; precisely106 plaquettes meet P, so the bound6m=180 is safe.
Their base-coordinate bounding intervals are[-1,2] in direction0 and[-2,1]
in directions1,2,3. Every interval has width three. Given arbitrary exterior links,
each of the two specified assignments to P has conditional probability at
least

 p_star=N^(-m)(m_beta/M_beta)^(6m)>0.

The variance of the score sum in that patch is at least
p_star²(3y_beta)²: use one pair of terms in
Var(Z)=(1/2)sum_(a,b)P(a)P(b)(Z(a)-Z(b))².
Place translated copies of P on the sublattice8Z4. For two distinct copies,
at least one coordinate translates by at least eight, so the displayed
interaction intervals are disjoint. No plaquette meets two patches. Given
the complement of these patches, their conditional laws
factor, and the full score sum is a sum of their separate contributions
plus an exterior constant. Conditional variances therefore add. In a box
whose side tends to infinity this proves

 chi>=8^(-4) p_star²(3y_beta)²>0.                     (9)

Only patches whose full interaction neighborhoods lie inside the score-sum
box are used. Boundary loss tends to zero. An original-link Gibbs lift of
the free-box bulk flux law exists by compactness and has the same local
conditional probabilities. This justifies the conditioning used here; a
gauge-fixed law is not substituted. The paired runner checks the finite
geometry and the flux-sum change independently of the variance argument.

For smooth compactly supported2-form tests f define

 Y_a(f)=a² sum_(x,I) f_I(a x)Y_I(x), a down to0.

Absolute covariance summability and Riemann sums give
Var(Y_a(f))->chi integral|f|² and the corresponding bilinear limit.
A direct blocking proof gives the Gaussian finite-dimensional limit.
Set L=a^-1, take microscopic block side floor(L^(1/4)), and separate them
by corridors of width ceil(60 log L). The variance of the omitted corridors
tends to zero by(5), since their occupied volume fraction tends to zero.
Use the proposal coupling to replace each retained block by a version whose
clan is restricted to a disjoint neighborhood of one-third the corridor
width. The probability that any replacement differs is bounded by a
constant times L^4 exp(-corridor/3)=O(L^-16), up to the harmless integer
rounding factor. The entire scaled field is bounded by O(L²), so the
replacement has squared L² error O(L^4 L^-16), which tends to zero.
The replacement blocks
are independent. Each scaled block contribution is bounded by a constant
times a²(L^(1/4))^4=O(L^-1), so the Lindeberg condition holds. Their total
variance has the limit above. The independent triangular-array CLT and
Cramer-Wold then yield

 Y_a => centered2-form white noise with covariance chi I, chi>0, (10)

in finite-dimensional distributions on smooth tests. This is the actual
score limit at these fixed clock parameters. It has no Maxwell transverse
projector term. No claim about every microscopic excitation or a full
Hamiltonian gap is needed for this statement.

## 5. The repaired closed flux can have a zero scaling limit

In this overlap regime, the original plaquette field has the probability-
coupling bound(5), while either repair representative has exponential
finite-window approximation in L^r, r finite. Truncated repairs are bounded
by a polynomial in their window radius: charge magnitude is bounded and
the retained components are disjoint, while each filling coefficient is
at most4 times its component mass. Splitting two far-separated repaired
observables into these truncated parts and their L² errors proves
exponential covariance decay for the repaired field as well. For the
covariant version, the coding rate can be very small but remains positive.

The repaired field has mean zero by charge conjugation. Its summable
covariance has a continuous Fourier transform C_hat(k). Exact closure
implies d2(k) C_hat(k)=0. Let k=a p tend to zero in any direction. Dividing
d2(ap) by a gives exterior multiplication by i p in the limit, hence

 p wedge C_hat(0)=0 for EVERY p.

The intersection of these kernels on2-forms in four dimensions is zero:
for any nonzero component, choose a coordinate direction outside its two
indices. Consequently C_hat(0)=0. The same covariance/Riemann argument as
above proves that the scaled repaired field converges to ZERO in L² on
smooth tests. Its pointwise Wilson characters still equal the original
ones exactly. Local unwrapping and a surviving continuum field are separate
obligations.

The white Gaussian score covariance in(10) pairs no strictly positive-time
support with its reflected negative-time support. Its direct Gaussian
reflection reconstruction therefore contributes only the vacuum in this
limiting field algebra. This is a statement about(10), not an identification
of all sectors of the underlying lattice theory.

## 6. What this control changes

The defect repair is useful exact structure, and the state can select its
frame almost surely. Neither result supplies a nonzero Maxwell stiffness.
For the same N=3 isotropic law at beta>=20, the physical score instead has
the strictly positive white-noise limit(10), and the closed repaired field
has the zero limit. This closes a specific inference shortcut, not the
finite-N phase problem in other parameter regions or actions.

Next high-value obligations remain a nonzero infrared stiffness AND Gaussian
source control in an actual candidate Coulomb regime, the separate principal-
penalty Hamiltonian phase, and native law/state/physical-time selection. No
axiom update follows from the controlled massive-score regime above.
