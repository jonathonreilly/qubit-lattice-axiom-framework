# Autonomous finite record clock and explicit axiom models

2026-11-08 local date. Source parent 9213a55c3636c8bdbf4a1f692e902d4d6d7ac44a;
main 1e0d3b58dcda7f83152b0bb51729260247454d65.
**Claim type:** bounded_theorem. **Actual status:** conditional-support.
This is a research result, not independent retained audit.
The supervisor developed the jump-clock argument while a fresh checker worked
from the original five sources. Early checker messages disclosed its fixed-seed
counterexample and jump-clock route before this file was frozen; no claim of
two blind discoveries is made. The complete independent proof and later source check are preserved separately.

## 1. Exact target and what is a choice

Replace the external gate index and unspecified formation schedule in the
finite compiled gauge experiment by a fixed Markov record process. The strongest
positive statement here is an explicitly chosen autonomous finite-neighborhood
model. The four axioms do not themselves select its quantum instruments or
rates. A separate short-range physical realization of its joint gate/tick
channels is not proved by naming a Markov generator.

The finite program consists of T phases. A phase is an elementary native gate,
a binary pointer instrument, or a deterministic completion append; halted
branches use an absorbing continuation. Adaptive choices are fixed functions
of previous record contents. Each phase has known operators K_(j,b), with
sum_b K_(j,b)^dagger K_(j,b)=I on its declared legal input subspace. For a gate
there is one K=U. For the reader's terminal instrument K_b=P_b on its pointer.
Keep actual intermediate data/work states; do not replace them by basis bits
or by a table of final probabilities. Old records are never changed by K.

The initial live/work density is a specified function of initial preparation
records. An alternative domain begins after a logged successful rank-one
herald, whose post-state is fixed. Arbitrary unobserved pre-herald states are
NOT one record state: identical R with Omega versus an orthogonal vector gives
herald success probabilities 1 versus 0. This explicit witness says nothing
against a fixed seed, a certified post-herald domain or a different state space.

## 2. A permanent clock tape

Retain the native data box, the seven frame markers, header and output records.
Reserve T fresh clock qubits plus a recorded start bit outside that box, on a
straight tape in the recovered marker frame. For example for L=5n use

    c_j = a + (L+10)e1 + j e2,  j=0,...,T.

c_0 is a permanent 1; later c_j initially have blank |0>. At phase j, exactly
c_0,...,c_j are recorded 1. The record geometry, NOT an external counter,
identifies j. The new tape makes distance-five chains, each of degree at most
two; the original marker remains the unique degree-three component root with
arms of lengths 1,2,3. The old claim that it is the sole nontrivial component
is no longer used. A missing marker cannot be replaced by part of this tape. Program sites and the tape are fixed by the prepared marker/frame;
all translated and properly rotated copies are in the domain. Terminal j=T
is absorbing. Failure halt may occur earlier and leaves its finite prefix.

This is a declared encoding/resource enlargement. It does not fit an arbitrary
T into the earlier n^3 vertex outputs: there are T+1 additional physical sites.
No old gauge qubit or record is reset or overwritten. The active native gauge
code is unchanged at the earlier completed boundaries; its ambient apparatus
now includes this clock. The prepared domain has one selected origin/frame.

## 3. Fixed jump operators and no hidden waiting-time state

On a legal clock prefix j define the next jump operators by

    L_(j,b) = sqrt(gamma_j) |1><0|_(c_(j+1))
              [K_(j,b) tensor I_clock] Pi_j,    gamma_j>0.

Pi_j is the diagonal projector onto the legal old clock/header/output controls
of that phase, excluding its new tick and live targets. It includes the full
prefix and the failure/terminal guard, and commutes with K on shared old basis
controls. Vacancy of c_(j+1) is enforced by its raising factor. Only the current
legal phase is enabled. After a failed herald, its pointer-completion flip and
registration still execute; thereafter every Pi is zero on that history.
The simpler adjacent boundary test c_j=1,c_(j+1)=0 alone would miss this halt.
An adaptive finite program may control K on already recorded values. Data-record formation
is attached to the corresponding b branch; the clock tick is always recorded 1.
A binary-read phase can therefore append the value record and its tick together,
at two sites fixed before b. The axioms do not require one new site per event.
This theorem uses that simultaneous append. A sequential physical decomposition
requires its own phase/formation proof. Never leave an unlogged gate between phases.

Supply no intervening background Hamiltonian. On legal phase j,

    sum_b L_(j,b)^dagger L_(j,b) = gamma_j I.

Thus no-jump propagation for elapsed time u is exp(-gamma_j u/2) I.
The normalized conditional live state is unchanged until the next record.
The waiting time is exponential with rate gamma_j, and outcome b has
probability Tr(K_(j,b) rho_R K_(j,b)^dagger). There is no hidden elapsed-age
parameter in the normalized state or next-event odds. The Markov process is
time-homogeneous: the same R always gives the same rate, target and content law.

Define sigma_(Rb)=K_(j,b) sigma_R K_(j,b)^dagger, normalizing by its trace.
Induction reconstructs every intermediate data/work state from complete R,
including off-code temporary states and partial controller operations. Zero
trace branches are excluded. The normalized recursion agrees exactly with
the original finite circuit instrument, including passive references, provided
the specified initial reference extension is fixed or only its system marginal
is queried. Old records remain fixed at each phase. The unconditional Lindblad
equation alone does not identify literal Records: this model specifies its
birth/jump interpretation explicitly rather than deriving an unraveling.

Every nonterminal phase waits finitely almost surely. The phase count is at
most T, so termination is almost sure and E[completion time]<=T/gamma_min for
T>0. An empty remaining program T=0 is already absorbing.
Changing positive scalar gamma_j changes waiting times but not event-order
or outcome cylinder probabilities. No measured physical time unit is predicted.

## 4. Neighborhood and physical-actuation boundary

For each fixed n,T and finite prepared program, choose a radius containing
the entire finite apparatus from each eligible forming site; with the tape
above and the earlier marker geometry, R=10T+15n+30 is a loose sufficient
bound when the finite program is a fixed law table rather than an extra
unbounded spatial bank. The rule is one finite-neighborhood functional on
the full prepared orbit. To complete the one-site content law without inferring
admissibility merely from a preserved quantum eigenstate, omit the candidate
site x from its radius-R record condition. If that condition exactly matches
a legal PRE-EVENT record configuration for an enabled event that forms at x,
assign its proved marginal content distribution: delta_1 at a clock target,
or the Born probabilities at its value target. Otherwise assign the strictly positive fallback

    F_fallback(eta) = q(eta) delta_P1 + [1-q(eta)] delta_P0,
    q(eta) = (1/2 + l)/(1+k),

where k counts recorded sites in the finite ball excluding x and l counts
those with content P1. The prepared pointer reference identifies P0,P1.
Both weights are positive for every finite condition, and the fallback varies
when a 0 or 1 record is added. This also covers T=0 without claiming that a
constant fair kernel satisfies the variation clause. No fallback formation is enabled.
The targets are fixed before the current outcome. Two matching predecessors
are the same full record configuration in the unique recovered frame, so the
answer is single-valued. The entire apparatus lies in the ball; initial marker,
header and start-tick records are mandatory parts of a predecessor.

Every old record remains supported under this rule. Removing an initial
marker destroys the unique typed marker, while removing an initial header or
start tick leaves a mandatory hole; these use the positive fallback. Removing a
clock tick from a later prefix leaves a clock hole. Removing the most recent
tick either restores its exact predecessor (which assigned tick=1) or, when
that event also formed a value, leaves an impossible phase/value pattern and
uses the fallback. Removing a value or completion record leaves a hole in the
phase's mandatory output pattern, again using the fallback. New values are
formed only on positive-probability branches. This checks support as well as
operator preservation. The kernel is nonconstant: its fallback varies with k,l, and a deterministic
clock event has a different measure from any of these strictly positive mixtures.

This radius grows with the program budget. A gate may act on an adjacent data
pair, but its JOINT clock/gate jump also touches the distant tape. Therefore
the construction does NOT prove a uniform bounded-range microscopic actuator
or derive the joint jump from the earlier driven pair gates. It is compatible
with the broad finite-neighborhood reading, with a named chosen transition law.
It is not evidence that neighborhood-mediated actuation has been physically
derived from the four axioms. A conveyor encoding can bring clock and moving
data together, but requires its own full relocation, record, program and
quantum-probability locality proof; that stronger result is not asserted here.

## 5. Discriminating clock controls

If ticks are omitted, a one-qubit state before versus after H can have the
same outcome records but Z probabilities 1 versus 1/2. Therefore the gate
index cannot silently disappear from the record state.

If different measurement branches have rates 1 and 2, then total intensity
P0+2P1 is not scalar. Starting from |+>, a no-event interval u=log(2) changes
the conditional Z0 probability from 1/2 to 2/3. Recording past jumps alone is
then insufficient for the full-time state unless elapsed age is also handled.
This is a witness for that particular rate choice, not a universal obstruction.

## 6. Two explicit coherent models of the four axioms

This separate construction addresses whether the axioms are a coherent
starting point and whether they force the quantum rule. It is NOT a gauge
implementation or a fit to nature. It uses the full one-site M2(C) domain but
its formed-record law has atoms at its algebraically distinguished 0 and I.
No basis or preferred lattice site is chosen. Readout of those two contents is
the Boolean question whether the content is I.
The legal record domain is {absent,0,I}^Z3. The full possibility domain remains
M2(C); the axioms do not require every possibility to have positive weight.

Let eta be the six immediate neighbors' record conditions, k their number
present and l the number with content I. For any fixed a in (0,1), choose

    p_a(eta) = (a+l)/(1+k),
    F_a(eta) = p_a(eta) delta_I + [1-p_a(eta)] delta_0.

For 0<=l<=k<=6 both weights are strictly positive. They vary with the
neighbor condition. Adding an I neighbor increases p unless it was already 1;
adding a 0 neighbor decreases it unless it was already 0. Thus every previously
formed 0 or I record remains supported under all later neighbor conditions.
All contents are in M2(C); 0 and I are invariant under algebra automorphisms.
The rule is invariant under native translations and proper cubic rotations.

Choose a rate-one birth clock at each unrecorded site, independent uniform
marks to select I with probability p_a, and no further birth at that site.
This is a chosen formation rule, not a consequence of the axioms. To construct
it on literal infinite Z3, sample independent first-event Exp(1) times and
uniform marks at all sites. At a site's event use only neighbors with earlier
times. For a root time <=t, the probability of an ancestral dependency chain
of length m is at most (6t)^m/m!: there are at most 6^m paths and each strict
time ordering has density bounded by 1 on the m-simplex. Such chains cannot
revisit a site. The bound tends to zero, so each finite-time local query has
a finite ancestor set almost surely. Recursive value assignment is therefore
well-defined and consistent, without a global first event on the infinite grid.
Countability extends this conclusion to all site events. Every site records
once almost surely. Exponential memorylessness gives a time-homogeneous
record-only process. Only the resulting records are read.
The same construction starts from any configuration in the stated domain:
initial records are fixed boundary values, and only absent sites receive clocks.
For a cylinder function f depending on a finite site set A, its generator is

    (L_a f)(R) = sum_(x in A absent)
      [p_a(eta_x) f(R union {x:I})
       +(1-p_a(eta_x)) f(R union {x:0}) - f(R)].

This sum is finite. It makes the local state dependence and time homogeneity
explicit without postulating a global first event on the infinite lattice.

In particular a=1/4 and a=3/4 give two explicit candidate models of the same
four axioms. At a forming site with no recorded neighbors their I probabilities
are respectively 1/4 and 3/4. The axioms are therefore not an inconsistent
specification, and these two models do not force a unique probability law.
They are concrete logical examples, not a proof that all further derivations
are impossible or that a framework permitting different models is unscientific.

## 7. What this buys and does not buy

The selected jump model removes an external phase variable and external
formation calendar from the finite experiment, with a finite record budget
and exact preservation of its circuit probabilities. It makes the remaining
physical-law choice visible. It does not derive quantum dynamics or short-range
actuation by defining them as jumps. The two elementary models show coherence
and a specific freedom in the axioms, not empirical adequacy. The next useful
physics target is a justified, discriminating law or bridge; no new axiom is
adopted, and no mass gap, physical vacuum or continuum Yang-Mills result follows.

The explicit witnesses and unclosed stronger routes are scoped in
[NO_GO_DISCIPLINE_CHECKLIST.md](NO_GO_DISCIPLINE_CHECKLIST.md); no general no-go
or negative-packet PASS is claimed. Verification is indexed in HANDOFF.md.
