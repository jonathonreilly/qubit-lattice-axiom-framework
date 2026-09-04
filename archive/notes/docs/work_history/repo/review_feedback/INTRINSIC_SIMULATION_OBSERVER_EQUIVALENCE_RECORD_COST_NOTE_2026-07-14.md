# Intrinsic Simulation, Observer Equivalence, And Readable Record Cost

**Date:** 2026-07-14

**Type:** meta / Wolfram-adjacent exact-equivalence stress test

**Authority:** none. This note is not an axiom proposal, law selection,
physical-equivalence declaration, retained theorem, observer theory, audit
verdict, or premise registration. It changes no live foundation, registry,
policy, review, or audit surface.

## Question

Could exact microscopic law identity disappear because sufficiently capable
local rules intrinsically simulate one another, with internal observers seeing
only the common computation or common coarse causal history?

This is a serious version of the Wolfram-inspired escape. It is stronger than
ordinary update-order invariance: instead of quotienting two schedules of one
rule, it would quotient different rules related by encodings, spatial blocks,
time dilation, or observer coarse-graining.

Arrighi and Grattage's intrinsic-QCA construction makes this proposal exact in
the relevant computer-science sense: one simulated cell is encoded in an
adjacent block and several simulator steps implement one simulated step
([arXiv:0907.3827](https://arxiv.org/abs/0907.3827)). The Wolfram rule-space
proposal likewise makes translation effort and its computational time part of
the observer's motion through rule space
([technical background](https://wolframphysics.org/technical-introduction/potential-relation-to-physics/multiway-systems-in-the-space-of-all-possible-rules/)).
Those facts motivate rather than defeat the cost test below.

The test here is deliberately exact and minimal. It asks whether simulation of
the same logical map is already physical equivalence under the framework's own
record ontology.

## Result Up Front

No—not by itself.

For any one-step append map, a two-step wrapper can append a permanent phase
certificate before appending the same decoded output. The fast and wrapped
rules compute the same logical map after a time rescaling and have the same
logical start-to-output reachability. But the phase certificate is a formed
record. It is readable, contributes to additive readout, increases causal
depth, and consumes permanent capacity. The full finite record transcripts are
therefore different.

Hiding the phase in an unrecorded cursor does not repair this within the live
ontology. Before and after the hidden phase, the record configurations can be
identical while their next futures differ. Then a state is not a configuration
of records unless the cursor is included in the operational state or proved
future-irrelevant.

Multiway path refinement has the analogous probability defect. One path to
each of two decoded outcomes gives naive weights `1/2,1/2`. Splitting only the
zero path into two permanently distinguishable phase-record paths gives
`2/3,1/3` under path counting while preserving the decoded outcome support.
Collapsing the two zero paths before weighting restores `1/2,1/2`, but that
collapse is the missing physical event quotient. It cannot be inferred from
computational reachability alone when the phase records remain readable.

Thus intrinsic simulation can be a compiler theorem and causal subdivision
can be an observer approximation. Neither is yet an exact physical-equivalence
class for this framework. A valid class must preserve every admitted finite
record protocol, including record content, additive readout, causal relations,
and the statistics assigned to operational events. If duration, capacity, or
gravity later derives from record activity, the resource overhead must also be
shown unobservable or co-transformed.

This closes no universal route against a future observer-equivalence theorem.
It identifies the theorem's minimum burden and prevents “universal” or
“mutually simulable” from replacing the canonical-law referent.

## Exact Fast And Wrapped Rules

Let the supplied input record carry a bit `b`. The logical map is `NOT`:

```text
b -> 1-b.
```

The fast rule appends the output in one causal event:

```text
S_b -> O_(1-b).
```

The wrapped rule first appends a typed phase record and then appends the same
output:

```text
S_b -> P_b -> O_(1-b).
```

The decoder that reads only `O` gives the same answer for both inputs. A
macro-step that contracts `P_b` makes the causal reachability diagrams agree.
That is exact logical simulation.

The framework does not say that only logical output records are readable. It
says only records can be read, and the phase certificate is a record. A legal
full protocol can ask whether `P_b` exists and read its content before `O` is
formed. The two laws then have different transcript lengths, different finite
readout totals, and different causal depths:

```text
fast:    two records including the input, one post-input event;
wrapped: three records including the input, two post-input events.
```

The difference is not removed by renaming `P`. Deleting it is a many-to-one
coarse-graining over a readable physical event.

## Why A Hidden Phase Is Not Free

Suppose the wrapper keeps its phase in an unrecorded internal bit instead.
Consider two moments with the same visible record map `{S_b}`:

```text
h=0: the next event writes the hidden phase;
h=1: the next event appends O_(1-b).
```

Their future one-step transcript laws differ. Therefore the record fibre is
not strongly lumpable. One must either:

1. promote the phase into the predictive state;
2. record it, returning to the visible-cost case; or
3. derive that no legal future protocol can distinguish it.

Calling the bit “simulator state” does not make it physically absent.

## Path Refinement And Weights

Let a multiway rule have decoded terminal outcomes `{0,1}`.

```text
base paths:     z -> 0,  o -> 1;
refined paths:  z_a -> P_a -> 0,
                z_b -> P_b -> 0,
                o   -> 1.
```

Both rules have the same decoded support. Uniform path counting gives:

```text
base:     P(0)=1/2, P(1)=1/2;
refined:  P(0)=2/3, P(1)=1/3.
```

Quotienting `z_a,z_b` as one operational event before weighting gives the base
answer. Keeping their permanent phase records as distinct events gives the
refined answer. The measure therefore depends on an exact physical event
algebra, not merely the multiway graph's computational terminal set.

This is the same presentation test that defeats naive branch counting, now
expressed as a simulation wrapper. Schedule causal invariance can quotient
linear extensions inside one exact event DAG. It does not decide whether
additional readable nodes are gauge, clock ticks, resource events, or distinct
histories.

## Consequence For The Minimum Constitutional Content

The zero-edit route remains open only in its strong form:

> derive one complete future-record equivalence class whose arrows preserve
> every legal finite preparation, intervention, record transcript, readout,
> and claimed clock/resource statistic.

Weaker equivalences do not retire law identity:

- same computable functions;
- mutual universal simulation;
- same continuum limit;
- same causal reachability after subdivision;
- same decoded terminal support; or
- agreement only after an observer is instructed to ignore readable records.

If a theorem proves that all phase certificates are operational gauge and
that their overhead cannot affect any record-defined clock, capacity, matter,
or gravity observable, the wrapped rules may collapse. The present axioms do
not supply that quotient. If the certificates remain legal records, the
rules are physically distinct.

This result adds no new axiom sentence. It sharpens the already identified
minimum: one exact law identity or one exact transcript-preserving physical-
equivalence class, unless a uniqueness theorem derives it.

## No-Go Discipline Gate

The licensed negative is narrow:

> Exact logical simulation, causal-graph contraction, and decoded terminal
> agreement do not imply full physical equivalence for the displayed append
> wrappers when their intermediate certificates are permanent readable
> records.

It is not a no-go against intrinsic universality, observer theory, causal
invariance, coarse-grained emergence, or a future derived transcript quotient.

### N1 — Alternative-route enumeration

Tested routes are direct logical decoding, time dilation, causal subdivision,
visible phase certification, hidden simulator phase, uniform path counting,
event-first quotienting, and full transcript equivalence. Live routes include
relational observer algebras, error-correcting/gauge subsystems, exact
intrinsic-QCA simulation, and resource-normalized equivalence.

### N2 — Wall-independence audit

Logical output, full record transcript, causal depth, additive record readout,
capacity cost, and path weight are separated by explicit pairs. The result
does not count them as independent axiom needs; a complete equivalence theorem
could close them jointly.

### N3 — Hidden-wall scan

The load-bearing terms are `logical decoder`, `record`, `readable`, `phase`,
`macro-step`, `observer`, `path`, `event quotient`, `uniform`, `clock`, and
`resource`. No one is treated as self-defining. The input bit and decoder are
supplied only for the finite control.

### N4 — Exact residual matching

The fast/wrapped pair witnesses transcript, depth, readout, and capacity only.
The hidden-phase pair witnesses record-state insufficiency only. The path-
refinement pair witnesses event-quotient/weight dependence only. None is used
to claim a continuum or gravity failure.

### N5 — Resolution and rhetoric audit

The calculation is finite and exact. It does not prove that every universal
simulator exposes its overhead, that no observer can quotient it, or that all
causal subdivisions are physical. “Not yet equivalent” is not “fundamentally
inequivalent.”

### N6 — Partial-closure paths

An exact law can prove intermediate records are inaccessible to the declared
protocol category, encode phases in a gauge subsystem, make overhead a common
unit conversion, or establish a full-abstraction theorem between two rules.
Any such theorem must be checked against the live content-only additive
readout and every downstream record-defined clock/resource claim.

### N7 — Strongest surviving steelman

The strongest opponent is a physically universal QCA or rewrite system with
an internal observer algebra for which different microscopic programs are
fully abstract: every finite observable record protocol has a corresponding
protocol on the other representation with identical joint statistics, and
simulation overhead is pure coordinate choice. Such a theorem would permit an
exact equivalence-class referent rather than a preferred rule. The displayed
wrappers show why computational universality alone is insufficient; they do
not close this stronger route.

### N8 — Cross-cycle echo

Earlier schedule probes retired total order only after fixed predecessors and
joint record laws were supplied. Weyl conjugacy became conditional only after
state, context, boundary, and decoder were transported. The same pattern holds
here: a simulation becomes physical equivalence only after the complete
operational tuple and its records are transported. This is reconciliation,
not a new independent axiom lower bound.

## Verification

Run:

```bash
python3 scripts/intrinsic_simulation_observer_equivalence_record_cost_probe_2026_07_14.py
```

The runner checks the exact finite wrappers, hidden-phase future separation,
path weights, causal/readout costs, and documentation contracts. It does not
prove universality or select a law.
