# What records can select about their hidden evolution

Personal author: /root, 2026-10-16. Actual status: conditional-support.
Trace: frontier discovery. These are inverse characterizations and explicit
counterfamilies, not an adopted detector model, an initial-state selection,
or a derivation of the Born rule. Standard distribution-function conjugacy
and full-branch interval dynamics are prior mathematics; no historical novelty
is claimed. The generalized-baker construction was identified in block04.

## Observation-facing question

A candidate must account for sequences of exclusive detector records, not
only an average fringe. Block02's count accumulator fails the iid benchmark;
block04's explicitly chosen reservoir meets it. Does imposing the complete
sequence law now derive the reservoir, its physical coordinate, or its initial
state? Answer this within an explicit one-coordinate class, and distinguish
unconditional preparation relaxation from conditioning on an observed history.
The iid law below is a mathematical target. Neither the published anticoincidence
summary nor its visibility establishes every finite joint distribution.

## A conditional inverse characterization

Let u lie in [0,1], with a nonatomic full-support probability measure mu. Its
cumulative distribution F is continuous and strictly increasing, F(0)=0 and
F(1)=1. Endpoints carry no mass. For each supplied target p in (0,1), posit:

1. Outcome 0 occurs on [0,a), outcome 1 on [a,1].
2. Each branch state update T_b is continuous, strictly increasing, and maps
   the closure of its branch onto [0,1]. Endpoint values on branch boundaries
   are understood as one-sided limits; the output tie convention is fixed.
3. Conditional on either outcome, the updated coordinate has the SAME law mu
   when the incoming coordinate has law mu.
4. The probability of outcome 0 is p.

Premise 3 is a strong conditional renewal assumption on the hidden coordinate.
An iid output record by itself does not establish it for a full physical state.
Premise 4 uses the target probability as an input. Identifying p with an incoming
flux fraction or squared amplitude is an additional measurement bridge.

The four premises force

    a = F^(-1)(p),
    T_0(u) = F^(-1)[F(u)/p],
    T_1(u) = F^(-1)[(F(u)-p)/(1-p)].

Proof: mu([0,a))=F(a)=p. For y in [0,1], monotonicity and conditional renewal
give F(T_0^(-1)(y))/p=F(y). Thus T_0^(-1)(y)=F^(-1)(p F(y)); invert this identity.
For branch 1 the corresponding relation is
[F(T_1^(-1)(y))-p]/(1-p)=F(y). Conversely these formulas directly satisfy the
four premises. The maps are the block04 full-branch maps conjugated by F.

Consequently those premises determine a map ONCE mu and the coordinate are
specified, but do not choose them. For every r>0, F_r(u)=u^r gives

    a_r=p^(1/r),
    T_0(u)=u/p^(1/r),
    T_1(u)=[(u^r-p)/(1-p)]^(1/r),
    dmu_r=r*u^(r-1)du.

All have the same iid records at a fixed p, and the same prescribed/adaptive
control record laws, when initialized with their respective mu_r. A physical
measurement of u could distinguish them; the output law alone cannot. These
are changes of a hidden representation until such a physical calibration is
specified, not automatically different experimentally distinguishable theories.
Atomic measures and measures without full support are outside this theorem;
it says nothing against fractal state spaces or singular initial ensembles.

Nor does record renewal select the increasing-branch premise. After either
standard branch map, apply any measurable Lebesgue-preserving map V on [0,1).
The resulting coordinate remains uniform conditional on each outcome, so
all the same record laws follow. For example V(v)=2v modulo 1 gives two
folds per branch. At p=1/2 the state update is 4u modulo 1, while the output
still reads the first binary digit of u. It skips every second digit instead
of shifting one digit per record. This is a different supplied microscopic
rule that the iid output sequence does not distinguish. Choosing smoothness,
monotonicity, minimal entropy or a preferred coordinate to remove this freedom
would add a selector; no such selector is derived here.

## An evolving record can be invisible to future statistics

Block04's two-coordinate reversible extension already stores prior outcomes
in a second coordinate while the first coordinate gives the iid future law.
More generally attach a variable m which appends each outcome and let the
outcome-generating coordinate evolve independently of m. The complete hidden
state then retains and changes with history although the observed future is
independent of that history under the selected ensemble. This is a direct
counterexample to inferring physical erasure or absence of intermediate causal
structure from iid output records. It also shows why premise 3 cannot be
silently applied to all unobserved degrees of freedom.

The framework's permanent record content can be represented by the appended
history. Its downstream role may change through later dynamics without
rewriting an old symbol. Allowing old symbols themselves to change would be
a different candidate than the current Record premise. Neither option alone
selects a Hamiltonian, transport rule, record cadence or actual initial state.

## Conditioning on history: when preparation is forgotten

Return to block04's standard reservoir in the coordinate v=F(u), and let its
initial density rho on [0,1] be Lipschitz with constant K and bounded below by
m>0. Controls may be predetermined or depend on earlier observed outcomes,
but not on the unobserved current coordinate except through that history.

For any fixed finite outcome history, its initial-state cylinder is an interval
I=[l,l+w), where w is the product of the selected branch lengths. Composition
of inverse branches gives v_initial=l+w*v_current. The conditional density of
the current coordinate is therefore

    q_I(v)=rho(l+w*v)/bar_rho_I,
    bar_rho_I=integral_0^1 rho(l+w*z) dz.

The formula normalizes the initial density on that actual cylinder; it is not
an unconditional Perron iteration. Since bar_rho_I>=m,

    TV(q_I,uniform)
      <= [K*w/(2*m)] * integral_0^1 integral_0^1 |v-z| dv dz
      = K*w/(6*m).

This follows by writing rho(l+w*v)-bar_rho_I as its average difference from
rho(l+w*z), bounding that difference by K*w*|v-z|, and integrating. The bound
can be replaced by min(1,K*w/(6*m)). It controls any event in any fixed finite
future record sequence under the same continuation policy, because pushing
two measures through a measurable deterministic map cannot increase TV.

If every possible control satisfies delta<=p<=1-delta for a fixed 0<delta<=1/2,
then w<=(1-delta)^n after n outcomes, uniformly over histories and adaptive
policies. Thus the total-variation error is at most

    min(1, K*(1-delta)^n/(6*m)).

This is a conditional forgetting theorem for a supplied class of initial
densities and supplied full-branch dynamics. It does not choose an actual
microstate, prove a microscopic ensemble is smooth, or identify an experimental
burn-in time. The class restriction m>0 is load-bearing.

For the explicit density rho(v)=2v, take p=1/2 and the history of n zero outputs.
Then I=[0,2^(-n)), its probability is 4^(-n), and q_I(v)=2v for EVERY n. The next
zero output has conditional probability 1/4, although unconditional densities
converge to uniform as established in block04. Thus unconditional relaxation
does not imply uniform convergence after rare-history selection. The failed
inference is a substantive boundary, not a numerical convergence problem.

## Why finite record agreement does not select a typical actual history

At p=1/2, every binary word of length n specifies a nonempty dyadic cylinder.
Its left endpoint has that prefix under the lower-inclusive branch convention
and then evolves to zero forever. Therefore every finite record can be
continued by an eventually all-zero deterministic trajectory. Finite record
agreement alone cannot rule out such exceptional initial points or select
the invariant ensemble. Uniform measure assigns any given such point zero
probability; choosing that measure is precisely an additional premise.

This is an identifiability statement about finite observations in this model,
not a claim that exceptional points are probable, that all experiments are
fraudulent, or that statistical inference is invalid. The same finite-record
limitation applies to ordinary large hidden classical reservoirs.

## Next physical discrimination

The useful intervention is to relate an actual measured preparation or local
detector disturbance to its subsequent record law. The candidate must specify
that coupling before observing the test sequence. Then preparation dependence,
history-conditioned statistics, and response to changing current settings can
separate candidates which share a mean fringe or even an equilibrium record
law. Unobserved state coordinates cannot be treated as controllable laboratory
knobs merely because a simulation exposes them. No such apparatus bridge is
derived in this block, and no observed data were fitted to these examples.

The result removes the temptation to count conditional record-law reconstruction
as a derivation of a physical initial state. A concrete open direction survives:
derive a detector/environment coupling that predicts how measured disturbances
populate the reservoir class, then test a withheld history protocol.
