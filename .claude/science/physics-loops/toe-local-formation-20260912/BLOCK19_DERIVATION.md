# Fixed first-event projector Records from local probability programs

2026-09-13. Provisional derivation before checker construction. This is a
positive conditional Record-process model, with supplied probability-program
preparation. It does not derive those probabilities or their physical
calibration. No native quantum Hamiltonian implementation is asserted.

## 1. One complete matrix kernel

The one-site possibility space is the full algebra M2(C), with its finite-
dimensional Borel structure. A program matrix has the form

\[
X=(2+p)I+P,\qquad p\in[0,1],\quad P^2=P,\quad\operatorname{Tr}P=1.
\tag{1}
\]

It has a unique decoding

\[
p(X)=\frac{\operatorname{Tr}X-5}{2},\qquad
P(X)=X-(2+p(X))I.
\tag{2}
\]

To recognize a program, require the first expression to be real in[0,1]
and the second to obey the idempotent and trace conditions. These are
Borel conditions defined using the algebra itself. No Hermitian structure
is needed to define this kernel on all possibilities; the quantum-history
specialization uses Hermitian rank-one P. Let the trigger T=10I.

For the complete multiset eta of recorded nearest-neighbor contents, define
the following ONE fixed probability measure on M2(C):

* if eta contains T and exactly one program-valued neighbor X, set
  F_eta=p(X) delta_P(X)+(1-p(X)) delta_(I-P(X));
* otherwise, if eta is nonempty, use its empirical measure, retaining
  multiplicities;
* if eta is empty, use delta_0.

Exactly one counts neighbor occurrences, not distinct values. All cases
are normalized nonnegative Borel probability measures. The condition and
atoms vary measurably with the six finite matrix slots and their Record
occupancy pattern. Translation/proper-rotation covariance follows because
only the neighbor multiset is used. Matrix similarities and complex
conjugation preserve scalar T, trace, the real number p and idempotence,
and conjugate every output atom, so the kernel has those algebraic
covariances too. It distinguishes only structures explicitly definable in
the algebra; the particular numerical rule is a supplied candidate, not
selected by the axioms.

## 2. Supplied binary program tree and physical preparation

Fix N>=1. For each j=1,...,N and each prior binary history
h=(b_1,...,b_(j-1)), supply a program pair (P_j(h),p_j(h)) satisfying(1).
All histories have entries, including zero-probability histories, whose
otherwise unused entries may be chosen arbitrarily within the same domain.
Set B_j=2^(j-1). Index history h in binary order by
l(h)=1+sum_(k=1)^(j-1) b_k 2^(j-1-k), in1,...,B_j.
Prepare X_j,l=(2+p_j(h))I+P_j(h).

All following coordinates are in the actual physical Z3, not a virtual
graph later declared local. Let c_j=(20*2^j,0,0). At each event cell put
the two trigger Records T at c_j+e1 and c_j+2e1. For each l=1,...,B_j,
put X_j,l at c_j+(-3l,3,0) and its matching buddy at
c_j+(-3l,3,1). The data target c_j and all other cell sites begin unrecorded.
The prospective program port is c_j-e1.

A supplied rigid frame consists of eight paired scalar Records. At
f=(-10,-10,-10), put20I at f and f-e1;21I at f+e1 and f+2e1;
22I at f+2e2 and f+2e2+e1;23I at f+3e3 and f+3e3+e1.
Its unique20I Record adjacent to21I is f. That21I displacement recovers e1;
the nearest22I and23I displacements recover2e2 and3e3. Thus the complete
Record configuration intrinsically identifies the frame and orientation.
All nonmarker values have eigenvalues at most10 in this preparation and
its generated histories, so no new marker can arise. Copies retain program
eigenvalues in[2,4], and data idempotents have eigenvalues0,1.

Take the domain to include all lattice translates and proper rotations of
these preparations and the legal prefixes defined below. The marker proof
makes their decoding unique. The numerical frame and roles are prepared
data, not a privileged lattice origin or an added framework primitive.

## 3. Deterministic program routing, then the first data event

After data history h of length j-1, select its bank l=l(h). Form program
Records in this order:

\[
c_j+(-3l,2,0),\quad c_j+(-3l,1,0),\quad c_j+(-3l,0,0),
\]

then c_j+(x,0,0) for x=-3l+1,...,-1. This path has3l+2 sites.
Each of these sites has exactly one already recorded neighbor, its
predecessor carrying X_j,l. No trigger is adjacent to a forming program
site. Unselected bank sources are at height3, at least distance3 from
the spine; adjacent bank teeth are separated by3 in x. The source buddy
is distance2 from the first forming site. Thus F is exactly delta_X at
every program append. In particular this routing contains no fresh random
choice and is independent of the current, still unformed data outcome.

Now form the data Record at the SAME target c_j for both possible outcomes.
Its complete recorded nearest-neighbor condition consists of X_j,l at
c_j-e1 and T at c_j+e1. Hence its actual F distribution is

\[
\mathbb P(R(c_j)=P_j(h)\mid h,\text{formation at }c_j)=p_j(h),
\quad
\mathbb P(R(c_j)=I-P_j(h)\mid h,\text{formation at }c_j)=1-p_j(h).
\tag{3}
\]

This is the first data Record for that event, not a copy of an outcome
formed at a different site. The current event's location does not encode
its outcome. The permanent program was chosen from PREVIOUS outcomes only.
Proceed to event j+1; after event N the conditional finite process absorbs.
Formation cadence, a clock and a mechanism that physically executes this
schedule have not been supplied by the theorem.

## 4. Support, one-site uniqueness and state reconstruction

Every initial bank Record has a matching adjacent buddy and no trigger
neighbor, so its empirical local measure supports its content. Each new
program Record has a permanent predecessor with the same content. Later
data formation next to the port adds an idempotent neighbor but no trigger;
the port's empirical measure therefore still supports X. Every trigger
has its trigger buddy and no program neighbor, including after the data
Record forms, so its own empirical law continues to support T.

At a formed data site, the program and trigger neighbors remain fixed.
Its F law therefore remains(3), whose realized atom has positive mass.
The eight frame Records also retain their matching buddies and never gain
a trigger/program condition. Thus EVERY Record remains supported by its
current complete nearest-neighbor law at every later legal prefix.
No site forms twice: the program path is simple, its initial sources and
trigger sites are distinct, and separate event cells are disjoint.

For distinct j, the rightmost cell site is c_j+2e1 and the leftmost is
c_j-3B_j e1. For j>=2 their x separation from the previous cell is
17*2^(j-1)-2>1. Even the first cell lies far from the frame. No cross-cell
nearest-neighbor condition has been suppressed.

The law state is the Record configuration itself. Recover the frame, then
N from the prepared trigger pairs, the program tree from the initial bank
sites, and the completed data prefix from the target Records. Given the
already decoded bits, the selected bank for event j is known; its P and
I-P are distinct, since a trace-one idempotent cannot equal I/2. Its data
content therefore uniquely decodes the next bit. Any partly filled current
program path identifies the next append. This defines one transition
answer on every state in the supplied domain, with no hidden quantum state,
history variable, time index or sampled current-outcome label.

Using the mathematical occupancy pattern to specify a conditional formation
law is not a derived physical instrument for reading an empty site's value.
Only actual Record contents enter its readout values. The data readout can
be the identity map on M2(C), fixed independently of location and history.

## 5. Complete cylinders and horizon consistency

All program steps have conditional probability1. Therefore the data cylinder
for a binary string b=(b_1,...,b_N) is exactly

\[
\mu_N(b)=\prod_{j=1}^N
p_j(b_{<j})^{1-b_j}[1-p_j(b_{<j})]^{b_j},
\tag{4}
\]

with the usual direct branch choice interpretation at p=0 or1. Summing the
two extensions of any prefix gives its previous weight. Positivity and
normalization follow by induction. Zero branches are omitted from realized
histories; their program banks remain legitimate supported preparation.

The same F and the same c_j geometry work for every horizon. For a fixed
infinite specification of finite-prefix programs, the N preparation is a
subset of the N+1 preparation. Future cells are distant, so they change
none of the complete local conditions in earlier cells. Earlier program/
data cylinders agree under restriction. This is an arbitrary finite-horizon
family with nested preparations. No one finite preparation is claimed to
supply an unbounded number of events or its infinitely many future banks.

## 6. Quantum-history specialization and controls

For a finite quantum preparation rho and a specified sequence of binary
rank-one local projective programs, let sigma_h be the unnormalized ordered
projector-product density. At a supported prefix h supply

\[
p_j(h)=\frac{\operatorname{Tr}(\Pi_j^+(h)\sigma_h\Pi_j^+(h))}
 {\operatorname{Tr}\sigma_h},\qquad
P_j(h)=\text{the corresponding one-site matching projector}.
\tag{5}
\]

The next calculator is sigma_hb=Pi_j^b sigma_h Pi_j^b. Telescope the trace
ratios in(4): the data histories have precisely the supplied selected trace/
Lueders cylinders. The actual probabilities at the fixed first targets are
functions of their complete physical neighbor Records by(3). Quantum
probabilities are stored in the prepared banks, not derived from copying.

Independent setting choices may be represented as additional metadata
events with P=|0><0| and p=1/2. They update the chosen program, not the
quantum calculator. All bank entries for every setting prefix are present
before the actual settings occur. Apparatus program/trigger/setting Records
are typed metadata, not extra projective measurements of the logical rho.
Thus this construction does not claim that every formed metadata Record
belongs to the selected quantum data-event domain.

For two commuting wings, choose an order and route the conditional program
for the second wing after the first outcome. Summing over the first outcome
gives the usual quantum marginal, independent of the other setting. Reversing
the two-wing order with the corresponding programs gives the same joint
cylinder under its wing/outcome labels. This compares the two programmed
realizations, not identical physical target coordinates across both schedules.
Product input states
factorize, and the singlet with the standard Z,X and(Z±X)/sqrt2 directions
has CHSH magnitude2sqrt2. These are consequences of the supplied program
tree and trace calculus; an actual finite-speed or spacelike-local causal
implementation of the program routing is not asserted. In particular the
law-side selection of a second-wing bank can depend on the first-wing Record.

Arbitrary other binary trees fit exactly the same F with different prepared
programs. This universal programmability is not a uniqueness or physical
selection of quantum weights. A chosen quantum rule still requires the
independent calibration, native realization and law-selection bridges of
the current finite-sector benchmark. No axiom amendment follows here.

## 7. Explicit resources and probability precision

There are sum_j B_j=2^N-1 bank programs, each with one buddy, two trigger
Records per event, and eight frame Records. Thus

\[
R_{\rm prepared}=2(2^N-1)+2N+8.
\tag{6}
\]

Event j forms3l(h)+2 program Records and one data Record, so at most

\[
R_{\rm new}\le3(2^N-1)+3N,\qquad
R_{\rm final}\le5(2^N-1)+5N+8.
\tag{7}
\]

There are precisely N first-event data Records. The bounding-box extent is
O(2^N) in x and constant in y,z. This exponential program-table construction
is an upper bound for this explicit implementation; no optimality or
necessary exponential cost is claimed. The complete probability tree and
its preparation, including exact real numbers, are supplied resources.

For a finite probability precision comparison, keep the projectors and
geometry fixed and replace p_j(h) by values ptilde_j(h) in[0,1] with
sup_h|p_j(h)-ptilde_j(h)|<=delta_j, with0<=delta_j<=1 (larger proposed error
bounds may first be clipped to1). Couple the two binary draws optimally
whenever their preceding histories agree. At step j their split probability
conditional on agreement is at most delta_j. Hence the total variation of
the N data-history laws is at most

\[
1-\prod_{j=1}^N(1-\delta_j)\le\sum_{j=1}^N\delta_j.
\tag{8}
\]

This bounds DATA histories, not the full physical preparation distributions:
different exact program matrices are distinguishable prepared Records.
Nearest rounding to a b-bit dyadic grid gives delta_j<=2^(-b-1), so the
data-history bound is N2^(-b-1). This prices scalar probability precision
only; finite-precision projector calibration and a physical compiler are
additional questions. It does not turn a stored trace table into a derived
probability law.

An explicit off-code comparison illustrates this restricted precision claim.
Take P=diag(1,0),p=1/2 and replace X=diag(7/2,5/2) by
X'=X+diag(1/100,-1/100). Its trace still gives p=1/2, but the decoded
diag(101/100,-1/100) is not idempotent. At the neighbor condition{T,X'},
the stated rule uses its empirical branch, supported on T and X', rather
than the two projectors. These two particular measures have disjoint support
and total variation1. Equation(8) therefore applies to scalar errors that
remain within the declared program code; it is not a bound for arbitrary
matrix perturbations. This finite comparison does not rule out a different
program representation, operational error metric or robust physical compiler.
