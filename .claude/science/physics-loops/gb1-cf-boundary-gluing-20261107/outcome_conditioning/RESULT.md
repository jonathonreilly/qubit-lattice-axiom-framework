# Permanent local outcomes and explicit conditioning

Status: conditional construction; research comparison is recorded in
SOURCE_CHECK.md and DELTA_CHECK.md. Neither is a formal audit or adoption.
Main bf92a1d763030836ed55631d5d7a7ef3b288f284; research parent 8e0c276b60.
This file develops proposed quantum dynamics, not consequences of the four
current axioms. No Born rule, composite state or dynamics is adopted here.

## 1. Exact target and supplied structure

There are two separated finite connected detector blocks A and B on Z3.
Each block has a system qubit and two adjacent pointer qubits: three native
sites on a line suffice. The pointer uses the orthogonal two-qubit states
e=00 (empty), +=01 and -=10; 11 is an unused sector. Thus no native site
has a qutrit algebra. Standard tensor composition and a calibrated mapping
from these pointer bits to permanent site contents 0I and I are supplied.
Blank is absence of a record, never the readable value zero.

A setting n specifies P_a(n)=(I+a n.sigma)/2, a=+/-1. The two-wing source
is the fixed singlet rho_s, prepared and distributed before independent
setting choices. There is no operator acting jointly across A and B after
the choices. Settings and apparatus activation are supplied local controls;
their physical synthesis, timing and calibration are separate assumptions.
The general construction below also acts on arbitrary input density matrices
and untouched reference systems. Finite-region positive quantum states,
instruments, single-outcome sampling and a local occurrence law are added.

Local pointer readout is supplied as a commutative record algebra. In a
realized branch a newly filled pointer appends two nearby site records with
the appropriate bit contents. Those two local writes are one detector event;
there is no indivisible event coupling the distant detector blocks.

## 2. A local absorbing instrument

Let Pi_e=|e><e| and Pi_o=I-Pi_e on the four-dimensional pointer, including
the unused sector in Pi_o for a total operator extension. For 0<=q<=1 set

    D(q)=I_system tensor (sqrt(q) Pi_e+Pi_o),
    J_a(n)=P_a(n) tensor |a><e|,
    K_0=D(q),       K_a=sqrt(1-q) J_a(n).

K_0^*K_0+sum_a K_a^*K_a=I: the first term is
I tensor (q Pi_e+Pi_o) and the remaining sum is
(1-q) I tensor Pi_e. These Kraus operators define a completely positive,
trace-preserving channel Phi_n(q), including with arbitrary passive references.
This proof uses the supplied finite tensor Hilbert structure.

On an empty pointer, the non-formation branch is q rho tensor Pi_e,
and formation branch a is (1-q) P_a rho P_a tensor |a><a|. Its probability
is (1-q) tr(rho P_a); conditional on formation it is the Born probability.
On every already filled legal pointer J_a vanishes and D is identity. Every
old pointer sector and its system/reference correlations are then unchanged.
The same holds under every later application. Site records are appended once
and never overwritten. Repeatability refers to the pointer, not to a claim
that an arbitrary later measurement on the live system has the same outcome.

For q,r in [0,1], Phi_n(q) Phi_n(r)=Phi_n(qr). Decompose a matrix into
empty/occupied pointer blocks. The empty block is multiplied by qr; each
empty/occupied coherence by sqrt(qr); the occupied block is unchanged except
for the accumulated jump contribution [(1-r)+r(1-q)] sum_a J_a X J_a^*,
which equals (1-qr) times that contribution. J_a on an occupied output is
zero. This proves the semigroup identity on all matrices, including unused
and coherence sectors; it is not only a population calculation.

Consequently q(t)=exp(-kappa t), kappa>0, defines an explicit local one-shot
quantum-jump semigroup. Its generator has jumps sqrt(kappa) J_a and is

    L(X)=kappa sum_a J_a X J_a^* - (kappa/2){I tensor Pi_e,X}.

The intensity on any empty-pointer state is kappa, independent of its
quantum state and the setting. Once filled it is zero. This supplies
occurrence with a finite mean waiting time; it does not derive physical time
or kappa. Finite-step q is sufficient if no continuous clock is assumed.

## 3. Two local events, either order, and genuine intermediate states

Tensor the A and B channels and extend them by identity on any reference.
Every A Kraus operator commutes with every B Kraus operator. Thus selected
branch maps as well as nonselective maps commute. Start from rho_AB with
both pointers empty. For local survival probabilities q_A,q_B the sectors are

    empty,empty: q_A q_B rho_AB;
    a,empty: (1-q_A) q_B (P_a tensor I) rho_AB (P_a tensor I);
    empty,b: q_A (1-q_B) (I tensor P_b) rho_AB (I tensor P_b);
    a,b: (1-q_A)(1-q_B) (P_a tensor P_b) rho_AB (P_a tensor P_b).

Tensor the indicated pointer projectors onto each expression. Taking traces
gives a normalized classical distribution over actual record sectors. For
0<q_A,q_B<1 there are positive one-wing-recorded sectors. They are part of
the legal model, unlike the previous distant atomic-pair domain.

For rho_s, p(a,b|n,m)=(1-ab n.m)/4 and both marginals are 1/2. Conditioning
on both detectors eventually forming introduces no outcome/setting-dependent
selection: the probability is one for positive rates, and by a common finite
deadline its factor (1-q_A)(1-q_B) is independent of the outcomes and axes.
Different supplied positive setting-dependent rates would require a separate
sampling discussion; they are not used here. Either event order gives the
same joint probabilities and final quantum state for each a,b.

The six-site allocation is the dynamic system/pointer carrier, not a count
of prepared setting/source records, controller sites, reservoirs or repeated
trial storage. It is not a claim that the earlier twelve-record apparatus
implements this channel or that an infinite supply of events fits six sites.

## 4. The no-message theorem and the conditional collision coexist

For any trace-preserving A channel and any observable X_BR on B and a
passive reference,

    tr[(Phi_A tensor id)(rho) (I_A tensor X_BR)]
      =tr[rho (Phi_A^*(I_A) tensor X_BR)]
      =tr[rho (I_A tensor X_BR)].

This covers all input states, not just a singlet with fair marginals. Local
choice or application of A's nonselective instrument cannot change any B
record distribution. No A setting is an argument of the B Kraus operators,
rate or control. The common source is established before setting choices.
Lattice influence can propagate through additional local channels when
allowed; during this two-wing test their supports do not connect the wings.
No physical speed in metres per second follows from this finite construction.

An outcome message is not automatically free of setting information. In bit
notation, let the wings share a fair r independent of settings x,y. Alice
outputs a=r xor x and relays only a; Bob computes x=a xor r and outputs
b=a xor ((a xor r)y). Then a xor b=xy, so the completed outputs give the PR
score 4 with uniform one-wing marginals. Nevertheless Bob's available pair
(a,r) determines x. The relayed outcome carries the remote setting given his
side information. This counterexample, supplied by the independent checker,
rules out using message labels or final fair marginals as the no-message test.

The spatial allocation is a family of translated and properly rotated finite
blocks. Transporting the Hilbert factors, controls and pointer dictionary by
the corresponding site permutation conjugates every Kraus map and preserves
all stated probabilities. No chosen coordinate origin is used by that family.
The Pauli-axis calibration is supplied; identifying it with a physical spatial
spin direction would require the corresponding calibration/covariance bridge.

If A has actually formed a and B is still unformed, the full-history
conditional state of B before its own outcome is

    rho_B | (a,n) = (I-a n.sigma)/2,
    p(b | a,n,m) = (1-ab n.m)/2.

If that remote result is unavailable to B, averaging over it instead gives
rho_B=I/2 and p(b|m)=1/2. These are different conditioning questions, linked
by ordinary coarse-graining of the same positive joint law. Conditional
states may depend on remote records without those records controlling the
local physical instrument or creating an observable message.

If a prediction's conditioning history omits the actual local control, average
the joint control/state ensemble, not a single map applied to an averaged
quantum state. For example, let C be a fair recorded bit, prepare |C>, and
measure Z for C=0 or -Z for C=1. Each branch gives + with certainty. Applying
either fixed measurement to the averaged state I/2 instead gives + with
probability 1/2. The controller register can equivalently be retained in one
controlled instrument. Changing the predictor's information does not change
the actual operation. This checker-supplied witness fixes the control scope.

At n=m=z, after the two positive A outcomes Bob's required full-history
probability of + is respectively 0 and 1. His local apparatus and accessible
record history are identical. One function of that neighborhood cannot equal
both full-history conditionals. Adding an unread global density matrix does
not make them equal. Adding more classical local memory or arbitrarily many
relays before independent choices does not remove Bell factorization when
the complete causal inputs and independent local noise still screen off the
two outcomes. In that case A_x(lambda),B_y(lambda) in [-1,1] give

    |A_0(B_0+B_1)+A_1(B_0-B_1)|<=2,

and averaging gives CHSH<=2. This does not treat no-signalling as screening
off. A shared quantum state is not a local classical response table.

## 5. What information a state must retain

For a known initial preparation rho_0 and a record-labelled instrument
history h, let M_h be its composed completely positive branch map. Whenever
w_h=tr M_h(rho_0)>0,

    rho_h=M_h(rho_0)/w_h.

If the permanent record map uniquely identifies the preparation, choices
and causal order of noncommuting local operations, this is a function of R.
For disjoint operations the order can be omitted because the maps commute.
The next joint quantum probabilities are then functions of R and the fixed
law; rho_h is useful predictive bookkeeping rather than an independent state
coordinate. This does not make that function neighborhood-local when its
conditioning includes remote outcomes. Zero-probability histories are outside
the normalized conditional state's domain.

Without a sufficient preparation/history restriction, the same R may accompany
different quantum states. A blank qubit in |0><0| and in |1><1| has different
Z-record probabilities. More strongly, rho_s and I/4 have identical one-wing
density matrices and empty outcome records, yet E_ZZ is -1 and 0. Thus adding
only one-site quantum marginals to R still loses predictive joint information.

For arbitrary two-qubit states, equality of probabilities for all local Pauli
product measurements forces equality of the full density matrices: the 16
operators sigma_mu tensor sigma_nu, mu,nu=0,x,y,z, span Hermitian M4 and the
measurement probabilities determine every coefficient. A sufficient state
must distinguish those future-distinguishable possibilities. It may encode
them in complete preparation records with a fixed reconstruction law, or
retain a compatible joint quantum state explicitly. No unrestricted proof
that every physical preparation has the first representation is supplied.

The exact sufficiency criterion is equality of all allowed future record
laws whenever two histories have the same R. It is necessary because a
function has one value on one input, and sufficient by defining the predictor
on each record equivalence class. For restricted future tests, equality on
their effect span suffices; full density-matrix equality is not necessary.

Order and instrument calibration matter separately. Starting at I/2, Z+
followed by X+ and X+ followed by Z+ each have probability 1/4. If the
records contain only those two labelled outcomes at fixed sites, they can
coincide while the final states are |+><+| and |0><0|. A future Z+ then has
probability 1/2 or 1. Also P_+ rho P_+ and X P_+ rho P_+ X have the same
outcome effect P_+, but opposite Z predictions after that outcome. Thus a
recorded measurement label must identify the actual instrument, not only its
outcome probabilities. These independent-checker witnesses require neither
the older large ontology construction nor a hidden event counter.
The numeric order diagnostic instead starts at |0><0|. It checks the same
two final states and future odds, not the equal-prefix-mass I/2 fixture above.

There is a physical storage condition behind any compatible quantum pointer.
If m distinct readable values use states tau_a in a d-dimensional pointer
and one fixed readout POVM {F_b} with tr(tau_a F_b)=delta_ab, then each
support of tau_a lies in the eigenvalue-one space of F_a and the kernels
of all other F_b. Indeed a positive operator with zero expectation on a
positive state vanishes on its support. Hence the supports for distinct a
are orthogonal, and m<=d. A k-qubit register therefore has at most 2^k
perfectly distinguishable values in that fixed readout. The explicit model
uses two qubits for its three orthogonal empty/plus/minus control states.
This is not a framework-wide proof that every blank status must be an extra
readable symbol. Symbolic matrix-valued metadata are not automatically a
physical infinite-capacity one-qubit memory; their realization needs a
calibrated finite register or an explicitly declared idealization.

## 6. A sharp quantum-consistency test of the polynomial alternative

The previous control uses h(t)=(3t-t^3)/2 and
p_h(a,b|n,m)=(1-ab h(n.m))/4. Set n=z and condition on A=+.
It requires Bob's Bloch expectations at z,x,y to be -1,0,0. Any normalized
positive qubit functional with the declared Pauli measurement meanings must
therefore be rho_B=(I-Z)/2. At m=(z+x)/sqrt2 it predicts expectation
-1/sqrt2. The control instead requires -5/(4sqrt2). Hence the control cannot
assign a consistent qubit state to this conditional preparation across all
four tested axes. The failure is not lack of marginal no-signalling or failure
to normalize each binary menu. It is lack of one linear positive effect law
across measurement choices, including outcome-conditioned preparations.

A direct general binary-projector bound already follows at this level. For
each Alice setting x, let the conditional Bob Bloch vectors be r_ax, with
probabilities p(a|x), independent of Bob's chosen measurement. Set
v_x=sum_a a p(a|x) r_ax, so ||v_x||<=1. For Bob unit axes m0,m1,

    |S|=|v_0.(m0+m1)+v_1.(m0-m1)|
       <=||m0+m1||+||m0-m1||<=2sqrt2.

This is a sufficient two-wing condition, not a reconstruction of arbitrary
multipartite quantum dynamics. A full positive composite state and local
quantum instruments also give the standard bound for all binary effects,
as proved in the preceding packet. The coefficient 2sqrt2 is a consequence,
not a constraint inserted as the proposed axiom.

Complete positivity also has a concrete role beyond local positivity.
Transposition preserves positivity and trace on one isolated qubit. Applied
to just one half of rho_s, however, it gives expectation -1/2 in
|Phi_+>=(|00>+|11>)/sqrt2. It is not a positive joint state. Thus a merely
positive local update is not an adequate general substitute for a completely
positive map when entangled reference systems are allowed.

## 7. Proposed direction and exact limits

The present Record requirements of definite content, permanence and
content-only readability can remain. The current one-site M2 presentation
does not supply joint quantum states, a probability functional, instruments,
or causal conditioning semantics. An amendment intended to admit general
finite quantum experiments must state these additions and replace any reading
of Admissibility that identifies every full-history conditional with one
local-record function. Merely adding the word quantum to Record is insufficient.

Two legitimate scopes differ: a prepared record-only family with an explicit
quantum reconstruction law, and a general state consisting of R plus a
compatible joint quantum state. The latter openly enlarges the state
description. Neither follows from this construction as an inevitable ontology.
Both change the probability/formation premises relative to the current axioms.

The jump model supplies a normalized law over definite permanent outcomes;
sampling one branch is part of its stochastic instrument premise. A unitary
premeasurement alone does not select one actual outcome, and decoherence alone
does not prove that selection. Rates, physical actuation, entangled preparation,
all unrecorded quantum resources and repeated-trial records remain supplied.
No collapse interpretation, Lorentz invariant dynamics, empirical validation,
gauge theory, continuum limit or mass gap is derived.

## 8. Continuous outcomes without dividing by zero singleton weights

The finite formation construction does not require discrete-only axioms.
For a finite-dimensional input/output carrier and a standard Borel outcome
space, a measurable quantum instrument I assigns each measurable set B a
CP map, is countably additive entrywise, and has a trace-preserving total.
Here is the instrument-density argument of Chiribella, D'Ariano and Perinotti,
Proposition 2 of [arXiv:0810.3211](https://arxiv.org/abs/0810.3211), specialized
and checked directly, using the scalar Radon-Nikodym theorem.

Let C(B) be its Choi matrix, using the unnormalized maximally entangled
vector on the d-dimensional input. C(B)>=0 and tr C(Omega)=d. Define the
finite probability measure nu(B)=tr C(B)/d. A zero-nu set has positive
C(B) of zero trace, hence C(B)=0. Each complex matrix-entry measure is
absolutely continuous with respect to nu and has finite variation: on every
partition its entry magnitudes are bounded by the sum of the traces. Scalar
Radon-Nikodym gives a measurable matrix density C(x). It is Hermitian and
positive nu-almost everywhere, since the nonnegative quadratic-form measures
for a countable dense set of vectors have nonnegative densities; take a
common full-measure set and use continuity in the vector. Also tr C(x)=d
almost everywhere. Choi inversion gives a measurable CP-map density J_x with

    I(B)(rho)=integral_B J_x(rho) nu(dx).

For completeness, finite Choi positivity is equivalent to a Kraus form:
factor C as a sum |v_k><v_k|, reshape each v_k into a matrix K_k, and the
matrix-entry definition gives J(X)=sum K_k X K_k^*. The reverse follows
by applying J tensor identity to the positive maximally entangled projector.
No positivity theorem on an arbitrary infinite algebra is being imported.

For a supplied input rho>=0 of trace one, put
g_rho(x)=tr J_x(rho). It is nonnegative and integrates to one. Its actual
outcome law is mu_rho(dx)=g_rho(x) nu(dx). Where g_rho>0 the conditional
output is rho_x=J_x(rho)/g_rho(x); choices where g_rho=0 have zero mu_rho
measure. Integrating rho_x against mu_rho over B gives I(B)(rho), so
conditioning on any positive-probability set B agrees with the usual
normalized branch. Exact atomless outcomes use this almost-everywhere
conditional state, never division by a zero singleton probability.
The density and posterior are unique only almost everywhere. A fixed law
that also answers at individual exact histories must specify measurable
versions and its domain convention for null histories; the probability theorem
does not choose those versions. A content map must be measurable to define
its pushforward law.
If c maps instrument outcomes to readable contents, the recorded instrument
is K(C)=I(c^{-1}(C)). Its posterior conditions on that full preimage. For
example, if two equal-weight branches prepare |0> and |1> but carry the same
readable content, conditioning on that content gives I/2, not either hidden
fine-outcome pure state. Finite readout is not permission to use an unavailable
fine outcome in the record-conditioned predictor.

This supplies a mathematically consistent measurable-instrument clause on
finite quantum carriers. It does not construct exact storage of a continuum
of distinct perfectly readable values in a finite pointer; the capacity
lemma above rules out that stronger encoding. Nor does it build an infinite
volume formation dynamics or an instrument for every desired physical law.

## 9. Evidence and source status

The independent finite instrument-tree proof and explicit 12-to-14-record
symbolic patch are in INDEPENDENT.md. They are separate from this six-qubit
system/pointer carrier and its occurrence semigroup. The symbolic patch was
not numerically replayed. Its state-sufficiency, order/instrument and relay
witnesses were checked by hand before integration. The all-axis, all-input,
continuous-time semigroup and measurable-outcome statements are proofs, not
exhaustive numerical results. check.py tests the finite subset and preserves
source-bound streams, including three faults. No empirical data are used.
