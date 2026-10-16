# Neighborhood evolution: historical memory versus a current relation

Date: 2026-10-16. Author: /root, personally in the campaign chat.
Status: exploratory conditional mathematics; no empirical validation, audit
verdict, framework-axiom change, or novelty claim for the parity-game bound.

## Question and observations that constrain it

The user's hypothesis is that missing intermediate neighborhood relationships
make a process look like superposition. The motivating `iy -> diy -> do it
yourself` example concerns changing causal roles, not literal letter operations
in physics. Here the concrete question is whether information accumulated by
local devices across earlier events can replace a relation available during the
current event. This is one candidate family, not an exhaustive formalization of
the user's idea.

Single-particle interferometers produce a phase-dependent distribution of
individual records. For two binary phase settings, the ideal quantum benchmark
encodes their parity in an output port. This benchmark is exposed theoretical
development information, not a newly opened independent dataset. The physical
bridges needed to identify a carrier, settings, output ports and trial boundaries
remain premises. No empirical rejection is claimed below.

Known prior art is explicit. Horvat and Dakic, *Interference as an
information-theoretic game*, Quantum 5, 404 (2021), section IV and equations
(15)-(16), already give the one-classical-carrier parity bound:
https://arxiv.org/abs/2003.12114 . We reconstruct that elementary bound and make
arbitrary earlier memory explicit. De Raedt, De Raedt and Michielsen's learning
networks already simulate interferometers with stored messages and supplied
geometric/output rules: https://arxiv.org/abs/quant-ph/0501141 . Their later
review explicitly discusses failure of a particular neutron model under a
fresh random phase per incident neutron, section 6.4.3:
https://doi.org/10.1142/S0129183114300036 . No new discovery of either fact is
claimed.

## A. Candidate class and an exact bound with arbitrary past history

At trial t let H contain all prior records, network state, device memory and
shared past randomness. Two current input bits X,Y are uniform and independent
of H and of the current route choice J. The route J in {0,1} can depend
arbitrarily on H and fresh internal randomness. Exactly one current input can
influence the receiver before its output Z: X if J=0, Y if J=1. Internal
processing can be nonlinear, stochastic, adaptive and arbitrarily complicated.
There is no second current-setting message, direct setting wire, current
input-dependent routing, or supplied knowledge of the other current bit.
These are information-flow premises, stronger than mere spatial locality.

For a fixed past h, write q_h=P(J=0|h), and let f_0,h(x), f_1,h(y) be the
conditional probabilities of Z=0 after the corresponding route, including all
allowed local processing. Then

    p_h(0|x,y) = q_h f_0,h(x) + (1-q_h) f_1,h(y).

Consequently Delta_h=p_h(0|0,0)+p_h(0|1,1)-p_h(0|0,1)-p_h(0|1,0)=0.
The cancellation survives averaging over an arbitrarily large or evolving H,
because the fresh inputs give the same distribution of H in all four contexts.

Equivalently, with score S=(-1)^(X+Y+Z), E[S|H]=0 and

    P(Z=X xor Y | H)=1/2.

This argument also follows by conditioning on the visited bit: the other bit
remains a fair independent bit. Earlier memory cannot reveal a fresh bit to
which no current influence connects it. It does not rule out a network carrying
two current influences, a spatial field, a setting-dependent environment, or
other candidates outside this class. It is not Bell's theorem.

For n trials, the win indicators form bounded martingale differences around
1/2. Conditional Hoeffding's lemma and iteration give

    P(sample win fraction >= 1/2 + d) <= exp(-2 n d^2).

No independent-output assumption is needed. The setting freshness and declared
information-flow premises are needed on each trial. This is a prospective test
bound, not a p-value applied to observations.

If the joint law of current bits and prior/route variables is within total
variation epsilon of the stipulated fresh-input law, with both laws passed
through the same fixed conditional response kernel (including remaining internal
randomness), any win indicator changes its mean by at most epsilon. For a
stronger reference process, let an
exception eligibility flag be chosen from the past and independent internal
randomness before current X,Y. Require the current bits to remain independent
and uniform conditional on that flag and the other prior/route variables. If
an exceptional fraction lambda is allowed both current inputs, conditioning on
the flag gives P(win) <= 1/2 + lambda/2 + epsilon.

The eligibility qualification is essential. Arbitrary input-dependent exceptions
can select only trials that would otherwise lose. If instead one supplies a
coupling to a valid one-input process which agrees with the actual process off
an arbitrary exceptional set of probability lambda, the weaker bound is
P(win) <= 1/2 + lambda + epsilon (capped at one). Without either eligibility
or such a coupling premise, the phrase exceptional fraction alone is not a
sufficient model. These are supplied error budgets, not estimated laboratory
values. Missing detections, setting leakage, trigger selection and physical
routing must be included in an actual protocol.

Version note: the v1 sentence omitted the eligibility qualification. The
focused independent checker found this defect. V1 and its original computation
remain preserved; none of its 17 controls tested that omitted premise.

## B. Constructive binary cache network

Give a receiver two cached bits a,b. One equally likely path is visited per
event. On route 0 it receives X and updates a=X; on route 1 it receives Y and
updates b=Y. It then outputs Z=a xor b. The update and exclusive-output rule
are chosen classical rules. They are not derived from the framework axioms.
They use no quantum amplitude or Born probability. A fixed two-wire layout,
fresh event sequence, route coin and initial cache are supplied.

If X,Y stay fixed for a block and the initial cached missing bit is independent
and fair, then after t>=1 events the only error occurs when the other route has
never been visited and its stale bit is wrong. Thus

    P(error at event t)=2^(-t),
    mean block win fraction(B)=1-(1-2^(-B))/B.

The first event succeeds with probability 1/2; long blocks approach certainty.
With independently fresh X,Y every event, success is exactly 1/2, however long
the device has been learning. Thus an excellent stationary fit can coexist with
failure on the intervention that targets the missing intermediate relationship.

If each setting instead follows an independent stationary binary flip process
with flip probability nu, its lag-k sign correlation is rho^k, rho=1-2nu.
For independent balanced routes, the age K of the unvisited cache is geometric,
P(K=k)=2^(-k), k>=1. For this particular cache rule,

    E[S]=sum_(k>=1) 2^(-k) rho^k = rho/(2-rho),
    P(win)=1/(2-rho)=1/(1+2nu).

For biased routes q=P(J=0), with 0<q<1, the corresponding correlation is
q(1-q)rho[1/(1-q rho)+1/(1-(1-q)rho)]. These statements assume stationary
cache ages and the stated input/route process. They are not optimal bounds for
all adaptive networks. For example a predictable alternating input can be
inferred by a more capable device; the fresh-input theorem is the general claim.

## C. A second current relation changes the result

Let both current bits send local signals to a common future receiver. A classical
XOR gate then wins every trial. No quantum probability is needed for this binary
task. This construction violates the one-current-input premise explicitly; it
does not violate locality if both signals propagate along local paths before
the receiver acts. A single registered output is not a proof that exactly one
physical influence was present. Counting all influences is an observational
bridge, not something to assume from the word particle.

This positive construction is deliberately small: it does not produce the full
continuous interference law, a calibrated single-quantum energy budget,
antibunching, compatible multi-system composition, or the actual record law.
Those requirements are the next constraints on a distributed relational model.

## D. Physical and framework disposition

The current framework supplies an M2(C) one-site possibility algebra and a
nearest-neighbor dependence clause, but neither a numerical update law nor
trace/Born weights. Its selected projective-history sector law supplies those
weights conditionally; it cannot be used as a derivation of them here.

The binary cache description overwrites operational memory. An append-only
history can store each new cache value at a fresh site, with the active frontier
reading its immediate predecessor. That gives equivalent finite computation
if fresh sites, propagation, geometry and a formation schedule are supplied.
It is not yet a covariant one-qubit lattice implementation. Existing records
can keep their content while their later causal roles change; no claim is made
that permanent content itself changes under the current Record axiom.

The distinction suggests a constructive next route: derive a current-trial
relational carrier from local dynamics, then derive its record statistics.
Candidate transport and readout assumptions must remain separately visible.
The cache failure is not a rejection of the user's larger network hypothesis.

## Evidence plan and source boundary

The accompanying author probe will enumerate finite histories and extreme
one-input response tables, simulate declared cache processes with fixed seeds,
and test the two-current-signal control. Expected values above come from the
displayed derivations, independently of implementation. Synthetic data are
development controls. They are not calibrated or independent observational
tests. The full public articles are kept only in the private runtime cache;
their bibliographic sources and precise read scopes are recorded separately.
