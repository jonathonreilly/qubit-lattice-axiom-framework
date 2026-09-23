# Exact formation capacity in the supplied compensated rotor target

Independent bounded reconstruction, 2026-09-23. The new formation-capacity
author packet has not been opened. This is a target-level consequence and
countercontrol packet, not an audit disposition or a microscopic/volume
exchange theorem.

The number identity bounds the total expected number of births on a finite
graph. It also forces the finite-graph total formation rate to tend to zero,
using trace-class contractivity in addition to the identity. For a
translation-invariant locally normal infinite state, the corresponding
density identity gives finite integrated formation intensity per cell and
zero long-time average. The volume premise supplied here does not itself
justify a pointwise infinite-volume rate limit.

Stationarity does not force full occupation. There are physical stationary
states with positive vacancy density and uniformly bounded electric fields.
On a seven-site path, the stipulated initially all-A-plus, B-empty,
zero-field state reaches an exactly stationary, partly vacant output with
first-mark probability one third, for either stated creation convention.
These claims and their qualifications are proved below.

## 1. Sources, topology, and scope

The finite target and its local operators are reused from the exact sources
listed in `SOURCE_BINDINGS.json`:

* `LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT.md`, SHA256
  `42ec5430a0f49c9b6e70577be601df72e23d881b7ef152186de2cdb1ff3faba4`.
* `LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS.md`, SHA256
  `5539bbe3171ba21933aa42c4cc191b787029e5f5c9220dc8c3ee255e4906f582`.

For the infinite system the author volume seal
`5da6ab8a81e7f6442a3c63ece190e9119b3c2cdd00c9960465bc01cc963d1f7f`
and independent volume PRE
`6e8bae143d8ee1e0c77c57461c8025143b660709ff89e42c5c072a38d2164d0f`
were provisional dependencies when this task was dispatched. Their bound theorem
and REPORT were read completely to check the hypotheses used below, with
hashes `a0c1389773766c47b41300329cf6b945a8f5e584c2c46853fe34064a9c331bd6`
and `9dee691689889316acea057aa0180c59776315b7fa9499f0c52bccc9f0e6101b`.
The volume theorem is not independently reproved in this packet.

Before PRE, the parent authorized the completed volume comparison update.
Its FINAL seal is
`ad9aa6598563aabe3db38e0ae4bb421aef602782aa9c718daf479056402f8c89`.
The full COMPARISON, F1 acknowledgment and separate root clarification were
read and authenticated in `SOURCE_UPDATE_BINDINGS.json`. The sole correction
explicitly denies that a locally normal representation restores norm time
continuity on the same full local algebra. The source formulas are unchanged,
and this matches the topology used below. The initial pending-comparison
dependency is closed; no new independent volume proof or rerun is claimed.

The needed volume conclusions are these: on the quasi-local algebra built
from full finite-factor algebras B(H_X), the finite induced-graph maps have
a norm limit on each local observable, uniformly on compact time intervals
and over the fixed local unit ball. The limit is a UCP semigroup. Locally
normal states remain locally normal, their local expectations are time
continuous, and local Gauss constraints are preserved. The dynamics is
translation covariant when the coefficients and orientations are identified
covariantly. These are spatial norm-limit and statewise time-continuity
premises. They are not norm time continuity of the full bounded rotor
algebra, global trace-class evolution in an arbitrary representation, or a
global finite-rate jump process on Z^d.

This packet takes the already supplied compensated rotor target first.
It does not derive its compensation or instrument from a reservoir, infer
native dynamics, exchange microscopic and volume limits, or classify all
stationary states. The old finite-spin and unprepared-filter results are
not needed. No inherited physical builder or new author control is imported.

## 2. Operators and the exact finite number identity

Let G=(A union B,E) be a finite simple bipartite graph. The effective space
has every A site occupied, q_a=+/-1, while q_b=0,+/-1. A physical vector
satisfies div E=q-1_A. Orient edges A to B for definiteness; reversing an
orientation just changes its electric-coordinate sign. Fix K>0 and
delta,kappa>=0; the nontrivial birth conclusions use kappa>0. Put n_x=q_x^2,

    N = sum_x n_x = |A| I + sum_(b in B) n_b,
    D = sum_(e=(a,b)) (1-n_b) E_e(E_e-q_a),
    S_ac = F_c F_a P,
    h = K D - 2 delta sum_(a<c sharing a B neighbor) S_ac^* S_ac.

Here F_a is the unsigned sum of legal outward hops from a to vacant B
neighbors. The local compression P is as in the permitted source. The
rotor shifts have unit amplitude. A resolved channel is

    L_(e,sigma) = sqrt(kappa) B_(e,sigma),
    B_(e,sigma) = P j_(e,sigma) F_a P.

It first moves the old A record to a B neighbor c distinct from b, then
creates q_a=sigma and q_b=-sigma. A coherent edge channel is
sqrt(kappa)(B_(e,+)+B_(e,-)), with no extra 1/sqrt(2). Define

    Gamma = sum_mu L_mu^* L_mu,
    ell_a = sum_(channels anchored at a) L_mu^* L_mu.

The final A charges of B_(e,+) and B_(e,-) are orthogonal. Consequently

    B_(e,+)^* B_(e,-) = 0,
    Gamma_coherent = Gamma_resolved,
    ||ell_a|| <= 2 kappa z_a (z_a-1)^2,
    ||Gamma|| <= 2 kappa sum_a z_a (z_a-1)^2.                 (1)

This equality concerns the instantaneous loss operator, not the recycling
maps or evolved states of the two instruments. Every balance statement
below applies separately to the evolution under either convention.

Hops preserve N, births add exactly two, and D is diagonal. Thus

    [h,N]=0,   [N,L_mu]=2 L_mu,   [Gamma,N]=0.                (2)

The unbounded diagonal h causes no hidden moment assumption in (2). D is
selfadjoint multiplication on its maximal domain, with finite-field vectors
as a core. The bounded diagonal N preserves that domain and commutes with
D. The remaining Hamiltonian is bounded and preserves N, so the unitary
group of h commutes with N. All jumps are bounded. The finite target is a
strongly continuous CPTP semigroup T_(t,*) on trace class, including initial
densities with no electric moments.

For any function f on the finite number spectrum, the bounded weak
Heisenberg identity is

    L^* f(N) = Gamma [f(N+2)-f(N)].                          (3)

Values beyond the maximal number are immaterial because the corresponding
jump is zero. In particular L^* N=2 Gamma. For every initial density rho,

    Tr(N rho_t)-Tr(N rho_0)
       = 2 int_0^t Tr(Gamma rho_s) ds.                       (4)

One can prove (4) directly from the mild evolution: the Hamiltonian leaves
N fixed, and the bounded jump perturbation supplies (3). Neither an
unbounded energy expectation nor a trace-class commutator [h,rho_0] is
required. The integrand is continuous by trace-class continuity.

If rho_0 has a definite number N_0, the density conditioned on m recorded
births has number N_0+2m. This follows from the bounded-jump Dyson expansion:
the no-mark generator preserves each N sector and each recycling operation
raises N by two. Therefore the usual finite-graph counting instrument obeys

    E J_t = [Tr(N rho_t)-N_0]/2,
    J_t <= floor((|V|-N_0)/2) almost surely.                 (5)

The bound holds for all times and hence for J_infinity. For general initial
rho, the expectation identity uses Tr(N rho_0), while a pathwise bound uses
the smallest N in its number support. Initial coherences between number
sectors do not change count probabilities: the trace of each off-diagonal
number block is zero and the marked evolution preserves its number
difference. It is sufficient to dephase the initial number for that counting
calculation. No dephasing of the actual density is being asserted.

For a closed finite physical graph, total charge is |A|, so N-|A| is even.
The physical upper number is at most |A|+2 floor(|B|/2). In particular an
odd |B| can already forbid full occupancy by parity. Our decisive examples
below also leave unused, parity-allowed birth capacity.

Equation (4), boundedness of N, and positivity give a limit of the mean
number and

    int_0^infinity Tr(Gamma rho_s) ds
        <= [|V|-Tr(N rho_0)]/2.                             (6)

This inequality may be sharpened by the physical maximum number. Count
probabilities have limits because a bounded nondecreasing integer count
has an almost-sure terminal value. No formula for those limiting probabilities
or for a full density limit follows from this accounting.

## 3. Finite pointwise extinction, and what it does not imply

There is a useful finite-graph consequence beyond the time average. Write
r(t)=Tr(Gamma rho_t). For h>=0, trace-norm contraction gives

    |r(t+h)-r(t)|
      <= ||Gamma|| ||T_(h,*) rho_0-rho_0||_1,   uniformly t>=0.  (7)

Strong continuity at zero makes r uniformly continuous on the whole half
line. A nonnegative integrable uniformly continuous function tends to zero:
otherwise intervals of a fixed positive width around a subsequence of
positive-height peaks can be chosen disjoint, contradicting integrability.
Hence

    lim_(t->infinity) Tr(Gamma rho_t)=0                       (8)

for every finite-graph initial density, without an electric-moment
assumption. Each individual channel intensity is bounded above by r(t)
and also tends to zero. There is no universal late-time decay rate in this
argument; (6) supplies the explicit average bound proportional to 1/T.

If rho is stationary, (4) gives Tr(Gamma rho)=0. Positivity implies
L_mu rho^(1/2)=0 for each actual channel. Thus all dissipative terms vanish
on rho. The bounded-perturbation mild formula then says that rho must be
invariant under exp(-ith). Conversely, a density annihilated by all jumps
and invariant under this unitary group is stationary. This is a statement
about the semigroup, not an unjustified everywhere-defined commutator with
an unbounded Hamiltonian. For kappa>0 the resolved B operators also
annihilate rho^(1/2) in the coherent convention, by the orthogonal-range
loss identity in (1).

Complete occupancy is sufficient here: every F_a, every birth, and every
diagonal D_e is then zero on that sector. It is not necessary. Moreover,
zero formation does not imply convergence to a stationary density. Section 6
gives an exact physical two-energy superposition inside a jump-free sector
whose density oscillates forever.

## 4. Infinite density balance under translation invariance

Use Z^d, d>=2, z=2d, A of even coordinate parity and B of odd parity. The
translation group here is the group of integer vectors with even coordinate
sum, which preserves the staggered background and is transitive on each
sublattice. A-to-B edge orientation makes covariance explicit. Assume the
initial physical state omega is locally normal and invariant under this
group. The checked volume premise then supplies omega_t=omega T_t
with the same properties. Define

    b(t)=omega_t(n_b),             for any b in B,
    r(t)=omega_t(ell_a),           for any a in A,
    n(t)=[1+b(t)]/2.                                      (9)

Thus r is rate per A anchor, or per two-site cell; the formation rate per
lattice vertex is r/2. It is a local bounded expectation. No infinite total
number operator or first global event clock is used.

Here is the boundary argument establishing the exact balance, rather than
postulating a product-state closure. For a large cubic site set Lambda let
N_(B,Lambda)=sum_(b in B intersect Lambda) n_b. It commutes with every D_e.
Its weak generator image is a bounded local observable. A pair Hamiltonian
whose support lies completely inside Lambda preserves the total B number
on that support and contributes zero to its number derivative. A birth whose
star is completely inside contributes 2 L_mu^* L_mu by (2). Terms outside
are zero; all discrepancies from assigning anchors to Lambda are in a fixed
boundary strip. Bounded ranges, norms and number of terms per cell yield

    L^* N_(B,Lambda)
       = 2 sum_(a in A intersect Lambda) ell_a + R_Lambda,
    ||R_Lambda|| <= C |boundary_R Lambda|,                  (10)

with constants depending only on d, delta and kappa, not electric amplitudes
or Lambda. For example the commutator bound is 2||V_Z|| times the number
of B sites in a fixed support, and the dissipator bound is 2||L_Z||^2 times
that number. The diagonal unbounded part contributes nothing.

The finite-volume weak identity for this bounded number observable passes
to the infinite dynamics by compact-time uniform norm convergence on its
local generator image. Scalar expectations then obey its integral form.
Use translation invariance in (10), divide by |B intersect Lambda|, and
take a cubic Foelner limit at each fixed t. The A/B ratio tends to one and
the boundary term is at most C t times boundary/volume. This proves

    b(t)-b(0)=2 int_0^t r(s) ds,
    n(t)-n(0)=int_0^t r(s) ds.                            (11)

Local statewise continuity makes r continuous and hence b differentiable
with b'=2r. It does not close r as a function of b. Finite translation
unit cells with more than one site of each type give the same identity
after averaging over that cell.

Since 0<=b<=1,

    int_0^infinity r(s) ds <= [1-b(0)]/2,
    (1/T) int_0^T r(s) ds <= [1-b(0)]/(2T) -> 0.           (12)

The mean density has a limit at most one. Every fixed-length late-time
integrated intensity tends to zero; liminf r(t)=0. Thus the closed target
cannot sustain a positive long-time averaged formation rate per cell in
this class of states. This is finite local storage accounting. Infinitely
many sites do not turn it into a finite total global event bound; an
infinite lattice may have infinitely many events in space. No global jump
unravelling is claimed.

For the all-A-plus, B-empty, zero-field state the familiar initial
normalization is consistent with (11): there are z edges per A, two sign
channels per edge and z-1 outward destinations. Thus r(0)=2 kappa z(z-1),
b'(0)=4 kappa z(z-1) and n'(0)=2 kappa z(z-1). These are initial derivatives,
not a constant rate law. Equation (12) has right side 1/2 for the integrated
rate per A anchor from this initialization. It does not prove complete
occupation at late times.

## 5. Pointwise and stationary infinite-volume claims

Equation (7) cannot be copied to an arbitrary locally normal infinite state:
the premise supplies no global trace-class density with a C0 orbit in
functional norm. Nor is the full local bounded rotor algebra norm C0.
The loss operators can contain shifts, so norm continuity of T_h(ell_a)
also cannot be silently assumed. The exact infinite conclusions asserted
here are (11)-(12), continuity, vanishing averages and vanishing integrals
over fixed late-time windows. An unconditional pointwise limit r(t)->0 for
every supplied infinite state is **not established in this packet**. This
is a remaining possible strengthening, not a claimed counterexample to
that pointwise statement in the physical model.

Continuity and the accounting identity alone cannot supply it. For example,
put disjoint triangular peaks of height one at integer n>=1 with half-width
w_n=2^(-n-4), and set f=0 elsewhere. The resulting f is continuous,
int f=sum w_n=1/16, and f(n)=1. The function b(t)=2 int_0^t f(s) ds stays
between zero and 1/8 and obeys precisely the scalar positive balance.
This is a logical countercontrol to that inference, not a proposed target
trajectory or a replacement for the physical counterexamples below.

A sufficient extra hypothesis for a pointwise conclusion is trace-norm
precompactness of the local reduced-density orbit on every finite factor
region. In that case approximate T_h(ell_a) by a fixed sufficiently large
finite-volume map, using the volume bound uniformly for 0<=h<=1. That finite
map is strongly continuous against trace-class vectors; uniform boundedness
upgrades convergence to uniformity on a compact set of local densities.
Consequently omega_t(T_h(ell_a)-ell_a)->0 uniformly in t as h->0. The rate
is then uniformly continuous, and (12) gives r(t)->0 as in Section 3.
Uniform electric-cutoff tightness of all those local marginals is a concrete
sufficient precompactness condition; a uniform full-electric second-moment
bound on each finite region would imply it. No such uniform-in-time bound
is imported from the volume theorem, from initial local normality, or from
the possibly noncoercive gated electric energy D.

If omega is translation-invariant and stationary, r is constant, so (12)
forces r=0 without any extra pointwise theorem. Positivity implies

    omega(L_mu^*L_mu)=0, or equivalently L_mu Omega_omega=0   (13)

for every local actual channel in the GNS representation. For kappa>0,
orthogonality again gives resolved-channel darkness even when the selected
instrument is coherent. The dissipator's expectation vanishes on every
local bounded test observable, by Cauchy--Schwarz. Remaining stationarity is
a Hamiltonian invariance condition where defined. Equation (13) imposes
jump darkness, not n_b=1. No classification of all dark subspaces is needed
for this distinction.

## 6. Physical countercontrols with unused capacity

### 6.1 A seven-site path reached from the empty-B preparation

Number the sites 0,...,6 along a path, with A={1,3,5} and B={0,2,4,6}.
Orient its six edges A to B. Start with q_a=+1, q_b=0, and E=0. On this
tree the physical field for each charge word is uniquely determined by
Gauss law. The full P-space of total charge three has 52 states: number
sector dimensions 1,30,21 for N=3,5,7.

The exact matrices built in `finite_path_control.py` give

    D Omega=0,   H4^C Omega=-12 Omega,
    Gamma Omega=12 kappa Omega.                            (14)

The first survival probability is therefore exp(-12 kappa t). A resolved
first channel on either edge incident on the middle A site 3 has one legal
old-record destination and rate kappa. There are four such resolved
channels, or two coherent edge channels each of rate 2 kappa. All their
outputs occupy B sites 2 and 4 and leave the two endpoint holes 0 and 6.
Each output is annihilated by D, every S_ac and every later birth. In
particular the normalized coherent output, including its sign coherence,
also lies in this common zero subspace.

For example the mark e=(3,4), sigma=+ produces

    q = (0,1,1,1,-1,1,0),
    E = (0,0,-1,+1,0,0)

in edge order (1,0),(1,2),(3,2),(3,4),(5,4),(5,6). This is physical:
div E=q-1_A. The empty-endpoint fields are zero, so D=0. No A star contains
two holes. No pair of overlapping A stars can send two old records to
distinct holes at distance six. Hence jumps and H4 vanish as operators on
this vector, not just in expectation.

For kappa>0, the exact first-mark probability of entering this stationary
N=5 subspace is 4/12=1/3. At finite time its accumulated probability is
(1-exp(-12 kappa t))/3 and remains there forever. Consequently

    liminf_(t->infinity) Pr(N_t=5) >= 1/3,
    Pr(N_t=7) <= (2/3)(1-exp(-12 kappa t)) <= 2/3.           (15)

N=7 is physically allowed, so this leaves one possible birth unused;
it is not the odd-|B| parity obstruction. This is an actual event from the
specified initial state of this compensated finite graph, not merely an
abstract stationary state. It does not assert the same trapping probability
on Z^d or determine the other histories on the path.

### 6.2 Stationary infinite states with positive vacancy density

The geometric sufficient condition is simple. Put all A sites in charge
+1 and choose B holes at mutual graph distance greater than four. A birth
requires two distinct holes in one A star, which would be distance two.
An overlapping-star S_ac requires distinct hole destinations b,d and a
common B neighbor e of a,c. The path b-a-e-c-d has length at most four.
Thus every birth and every S_ac annihilates any electric basis word with
this occupancy pattern. The pair-form identity is essential: a hypothetical
uncancelled distant-star term would not obey this argument.

Here is a charge- and field-compatible periodic realization for every d>=2.
Use period 12 in every coordinate. In each cell place holes at
(1,0,...,0) and (7,0,...,0). Their distinct images have mutual distance at
least six. Keep all A charges +1. For each transverse coordinate
y=(x_2,...,x_d), the six B sites in its x_1 row are

    (r+2j,y), j=0,...,5,   r=1-sum(y) modulo 2.

For y nonzero modulo 12, pair indices (0,1),(2,3),(4,5). For y=0, omit
the holes j=0,3 and pair (1,2),(4,5). In each pair put charge +1 on the
left B site and -1 on the right. Let a be their intervening A site. Set
E_(a,left)=-1 and E_(a,right)=+1, with every other field zero.

Every pair has zero total B charge. At its middle A the outgoing fields
sum to zero. At its B endpoints, div E equals the assigned B charge.
All other sites, including the holes, have zero required divergence.
This proves Gauss law exactly. All fields are 0,+/-1, all links incident
on a hole have field zero, and therefore every D_e annihilates the word.
The two hole-support arguments above annihilate the bounded Hamiltonian
terms and both creation conventions. In fact each finite induced-graph
dynamics, acting on the corresponding local marginals, leaves this product
basis state invariant: truncating a star introduces no new hole pair and
every retained D_e is still zero. Its invariance thus passes immediately to
the checked volume limit.

The periodic infinite product of basis states is locally normal and
physical. Average its finitely many translates over the parity-preserving
translation group modulo 12. The resulting finite convex mixture is
translation invariant, locally normal, physical, and stationary. It has

    vacancy density per lattice vertex = 2/12^d > 0,
    mean record density = 1-2/12^d,
    B occupation = 1-4/12^d.                               (16)

These stationary holes survive even though the fields have a uniform
bound and all local electric moments are finite. This does not prove that
the infinite empty-B initial state converges to this mixture. The selected
pairwise birth routes used to write the finite-cell basis word are legal
support paths, not a claim about a full coherent output, its probability,
or an infinite event history.

### 6.3 Zero formation without state convergence

On the two-dimensional period-12 torus just constructed, retain its matter
word and base field E_0. Add one circulation around the plaquette with
vertices a=(0,0), hole=(1,0), c=(1,1), b=(0,1). In A-to-B orientations add
+1 to (a,hole), -1 to (c,hole), +1 to (c,b), and -1 to (a,b). Gauss law is
unchanged. Both field words remain in the same jump- and pair-annihilated
matter sector. Direct substitution gives D(E_0)=0 and D(E_1)=2.

Thus (|q,E_0>+|q,E_1>)/sqrt(2) evolves with relative phase exp(-2iKt),
without any formation. The two electric basis words are normalizable and
have finite field moments. For K>0 the density does not converge in trace
norm: subsequences of times give the orthogonal plus and minus
superpositions. This is an exact target counterexample to inferring a
stationary state limit merely from extinction of formation.

## 7. Independent controls, failures, and open boundaries

`finite_path_control.py` independently constructs all 52 physical tree
states and the actual hop-then-birth maps using only the Python standard
library and exact integers. It checks every intermediate Gauss shift,
the number grading, the full H4 and loss matrices, equality of the two loss
operators, and L^*N=2 Gamma for both instruments on the whole physical
space. It verifies (14), every middle-A output's annihilation, and the
unused capacity. Its results include the full state list and sparse exact
operators, not floating eigenvalue tolerances.

`periodic_dark_control.py` is a separate standalone construction. It checks
the period-12 words in d=2 and d=3: respectively 144 and 1728 vertices,
288 and 5184 edges, and 288 and 7776 overlapping A pairs. It enumerates
zero legal birth paths and zero overlapping-pair double-hop paths, verifies
every Gauss equation, D=0 and |E|<=1, and checks the physical plaquette
countercontrol with D values 0 and 2. The explicit construction and distance
proof, not extrapolation of these two runs, establish the all-d statement.

Both mathematical controls succeeded on their first executions. Complete
stdout, stderr, actual argv, interpreter, wall times, return codes and script
hashes are retained. No failed computational attempt was overwritten. One
combined source-read output was truncated; the full missing volume report
was subsequently read from the stored complete command result. The rejected
scientific routes and their replacements are recorded in `ATTEMPTS.json`.

The initial pending volume-comparison dependency was closed by the
authorized update before PRE. The infinite density consequences still
depend on that source-bound volume theorem and local target; they are not
a new independent volume proof. The finite identities and explicit finite
countercontrols do not require the volume theorem. An unconditional
pointwise infinite formation-rate limit, uniform future field tightness,
late-time density convergence from empty B, and a classification of all
stationary states remain unproved here. No resource-replenishing mechanism,
microscopic transfer at infinite volume, formal retained/no-go status, or
publication conclusion is supplied.
