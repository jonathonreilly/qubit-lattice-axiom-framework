# Foundational test: which Bell correlations do the record axioms constrain?

Date: 2026-11-09. Claim type: bounded_theorem (application of existing results).
Actual current-surface status: conditional-support. No audit status is claimed.
This is a requested foundational diagnosis, not a new Bell theorem, a new
programmability theorem, or an empirical prediction. Main source revision is
1e0d3b58dcda7f83152b0bb51729260247454d65; research parent is c50d82b2d2.

## 1. Observable and decision criterion

In one declared trial, four fresh target sites record setting bits x,y and
outcome bits a,b. Every setting pair has positive probability. Define

    E_xy = sum_(a,b) (-1)^(a+b) P(a,b | x,y),
    S = |E_00 + E_01 + E_10 - E_11|.

The statistic concerns probabilities, not one observed finite-sample value.
Identifying these mathematical labels with laboratory choices and detectors,
pairing trials, and inferring probabilities from repeated data are separate
experimental assumptions. We compare exact distributions; no experiment or
new fit is performed. The classical and quantum target values were known
before this work; this is not a blind numerical prediction.

Positivity and normalization give |E_xy|<=1, hence 0<=S<=4. This is an
ordinary binary probability bound, not distinctive lattice physics.
The question is whether the current axioms impose a stronger universal bound
on the declared finite record protocols before causal or quantum assumptions.

## 2. A concrete current-axiom witness using the existing program theorem

The complete prior construction is
docs/PROJECTIVE_HISTORY_FIXED_FIRST_TARGET_LOCAL_PROGRAM_BOUNDED_THEOREM_NOTE_2026-09-13.md,
sections 1-5 and 7. Its source and audit-ledger identities are recorded in
source_hashes.json and the search record. It is an unaudited conditional
construction on main. We check the relevant proof rather than treating the
note's historical status wording as authority.

Here is its explicit four-event specialization. Fix P=diag(1,0), Q=I-P and
choose a real parameter r in [-1,1]. Events 1,2,3,4 record x,y,a,b. Supply
conditional zero probabilities

    p_1 = 1/2,
    p_2(x) = 1/2,
    p_3(x,y) = 1/2,
    p_4(x,y,a) = [1 + r (-1)^(a+xy)]/2.

Bits 0 and 1 are the actual contents P and Q. A fixed content readout maps
P to +1 and Q to -1; other record contents have a fixed metadata label.
The location is used to pair a trial and assign its roles, not to determine
the value read from a record. The supplied P is prepared apparatus data;
the content law itself is algebraically covariant.

For every depth j and binary prefix h, prepare the matrix

    X_jh = (2+p_j(h)) I + P.

The same fixed kernel F is used for every r. For a candidate site, inspect
ALL SIX immediate-neighbor record slots, excluding the target itself:

1. If a trigger T=10I and exactly one program-valued neighbor X are present,
   use p(X) delta_P(X) + [1-p(X)] delta_(I-P(X)). Decode
   p(X)=(Tr X-5)/2 and P(X)=X-(2+p(X))I; require real p in [0,1],
   P(X)^2=P(X), Tr P(X)=1.
2. Otherwise, for a nonempty neighborhood use its empirical content measure,
   counting multiplicities; for an empty neighborhood use delta_0.

This defines F on the full M2(C) possibility domain. Its branch predicates
are Borel; all weights are normalized and nonnegative. It varies with the
neighborhood. Translation/proper-rotation covariance follows from its use
of a multiset. Trace and idempotence give similarity covariance as well.
Our exact executable specialization uses diagonal rational matrices, not a
claim that arbitrary M2 matrices were numerically enumerated.

For completeness the actual Z3 allocation is as follows. Let e_i be the
prepared frame and c_j=(20*2^j,0,0), j=1,...,4. A prefix h has bank index
l=1+sum_(k=1)^(j-1) h_k 2^(j-1-k). Place a matching pair of X_jh records
at c_j+(-3l,3,0) and c_j+(-3l,3,1). Put T at c_j+e_1 and c_j+2e_1.
The data target c_j is initially blank. With f=(-10,-10,-10), the frame
records are 20I at f,f-e_1; 21I at f+e_1,f+2e_1; 22I at f+2e_2,
f+2e_2+e_1; and 23I at f+3e_3,f+3e_3+e_1.

After decoding the previous data records, route the selected program along
the previously blank sites

    c_j+(-3l,2,0), c_j+(-3l,1,0), c_j+(-3l,0,0),
    then c_j+(z,0,0), z=-3l+1,...,-1.

Every forming path site sees only its predecessor; it therefore copies X
with probability one. At the fixed data target the complete neighborhood
is exactly {X,T}, so its two outcome probabilities are p_j(h),1-p_j(h).
Only positive-probability branches form. The target is chosen before the
current outcome, independently of that outcome. The process then advances
to j+1 and absorbs after event 4.

All old records remain supported. Bank and frame records have same-content
buddies. Trigger pairs never acquire an adjacent program. A path record has
its predecessor; the final port can acquire a data neighbor but no trigger.
Data sites retain their unchanged program/trigger menu. Paths never revisit
a site. Separate event cells have x separation at least 17*2^(j-1)-2>1;
no neighbor outside the declared condition has been discarded. The frame
is unique because no generated content has eigenvalue 20,21,22 or 23.
It reconstructs the axes, the four event cells, the prefix and the next
partly filled path from the current records. Include all translations and
proper rotations of these preparations and prefixes in the law's domain.
Thus no physical site or unrecorded external counter is privileged.

This is a well-defined record-state transition rule on a supplied legal
domain, including its absorbing states. Preparation and the next-site rule
are explicit model choices, not axioms. No finite-speed physical mechanism
for the record-dependent route selection is supplied. Old records, blank
sites and all off-apparatus local conditions are accounted for by F.

The allocation uses 46 initial records: 30 program records, 8 triggers and
8 frame records. At most 57 new records form, so at most 103 are required.
These are resources of this construction, not optimality claims. No new
quantum register composition, Born law or Hamiltonian is needed for it.

Multiplying the four event probabilities gives, exactly,

    P(x,y,a,b) = [1 + r (-1)^(a+b+xy)]/16,
    P(a,b | x,y) = [1 + r (-1)^(a+b+xy)]/4.

Consequently P(x,y)=1/4, each outcome marginal is 1/2 for every setting
pair, E_xy=r(-1)^xy, and S=4|r|. Every S in [0,4] is attained on this
declared family. In particular r=0,1/2,3/4,1 give S=0,2,3,4 with one
unchanged F. At r=3/4 every joint outcome has positive conditional weight
(1/16 or 7/16), so the score above 2sqrt2 is not a zero-support artifact.

This proves a precise limitation: the four axioms plus this four-record
protocol, without a causal-separation requirement, do not impose a universal
CHSH bound below 4. Adding observable no-signalling alone does not change
that example: its two marginals are already no-signalling. This concerns
output marginals, not every readable controller/program record.
The preparation stores r and all the probabilities. We have neither selected
r nor derived a superquantum physical law. Even ordinary communicating
devices can produce such a score; this is NOT a spacelike Bell experiment.

## 3. The causal-record hypothesis has an additional, sharp constraint

Bell/CHSH and the existing records-only formation note already prove the
relevant conditional theorem. Suppose a trial has a finite directed acyclic
causal graph, including its scheduler, stopping, routing and setting sources.
Each variable is a function of its parent records and exogenous random input.
The settings are independent of the complete pre-choice/common source
variables; each setting pair has positive probability. Neither setting has
a directed path to the opposite outcome. Independent private randomness on
the two wings and their shared causes gives a screening variable lambda with

    P(a,b | x,y) = integral rho(d lambda)
                         P_A(a | x,lambda) P_B(b | y,lambda),
    rho(d lambda | x,y) = rho(d lambda).

No outcome-dependent selection or coincidence filter may change that trial
population. The factorization is a hypothesis about a causal mechanism,
not a consequence of one-site marginal locality or of permanent records.
For the fixed causal graph it follows by collecting the common exogenous
ancestors into lambda and integrating the disjoint private noise on each wing.
All scheduler variables must be included; a globally chosen schedule is not
implicitly a local mechanism.

Write A_x(lambda), B_y(lambda) for the conditional means, in [-1,1]. For
each lambda the CHSH magnitude is at most

    |B_0+B_1| + |B_0-B_1| = 2 max(|B_0|,|B_1|) <= 2.

Integrating gives S<=2. Arbitrarily many neighborhood relays are allowed;
the test is the absence of a setting-to-remote-outcome path within the trial.
Before the choices, relays and shared history belong in lambda. If a relay
arrives afterward in time to affect the remote output, causal separation
has failed. Changing the word nearest to neighborhood does not alter this
conditional theorem or by itself create a physical light cone.

Our program witness violates that causal hypothesis: selecting the fourth
program can depend on x and a. It retains independent setting draws and
no-signalling output marginals while permitting internal information transfer.
It is not a counterexample to Bell's theorem.

## 4. What is required for the quantum Bell prediction

Supply a composite Hilbert model with commuting wing observables, self-adjoint
dichotomic A_0,A_1,B_0,B_1 (squares I), and a normalized positive quantum state.
Supply the link E_xy=Tr(rho A_x B_y) between those operators and the actual
record frequencies. Tensor composition is one sufficient realization; it is
not asserted to be logically necessary in this formulation. This link is the
Born/measurement bridge, not the one-site M2(C) algebra alone.

For C=A_0(B_0+B_1)+A_1(B_0-B_1), expansion gives

    C^2 = 4I - [A_0,A_1][B_0,B_1].

Each commutator has norm at most 2, so ||C||^2<=8 and S<=2sqrt2 for every
normalized positive state. This is the standard Tsirelson argument, already
in the repo, not a new lattice derivation. Saturation additionally requires
an appropriate prepared state and calibrated settings. For example, supply
Phi+=(|00>+|11>)/sqrt2, A_0=Z,A_1=X, B_0=(Z+X)/sqrt2,
B_1=(Z-X)/sqrt2. Then E=(1,1,1,-1)/sqrt2 and S=2sqrt2.
A tensor model alone does not prepare that state or identify a detector.

## 5. Implication for the current gauge/record lane

The autonomous-runtime packet gives a finite-radius joint jump law with a
record-indexed seed and supplied quantum instruments. Its complete record
state determines future odds on that prepared domain. Its radius grows with
the experiment budget, and each gate can share an atomic jump with a remote
clock tick. Neither that bound nor the circuit's adjacent gates establishes
causal separation of two physical detectors, a universal speed or Bell
factorization. The Born and preparation inputs are still present.

The axioms therefore have structural content (geometry, one-site algebra,
covariant neighborhood marginals, permanent supported readout) but do not
yet select a Bell prediction for a laboratory experiment. The result does
not say every record-only theory obeys S<=2, that the framework is false,
or that an axiom amendment is necessary. A record-only law with more general
joint formation is a distinct possibility; its physical meaning needs proof.

The next discriminating obligation is to specify a joint record-formation
law and an operational causal structure, and test the complete protocol:
does it reproduce Bell correlations without a setting-to-remote-outcome
communication path or a setting-dependent common cause, and which stated
assumption prevents correlations exceeding the quantum bound? A stored
probability table does not discharge that obligation.

Every extra assumption is itemized in ASSUMPTIONS.md. Research checks and
exact finite replays support this diagnosis; formal audit remains separate.
