# Causal-Schedule Equivalence: Wolfram-Inspired Exact Probe

**Date:** 2026-07-14

**Type:** meta

**Scope:** exact finite causal-order and update-order controls for sampled
permanent-record laws

**Authority:** none. This is a bounded construction and counterexample, not
the physical law, an axiom proposal, an audit verdict, or a retained theorem.
It changes no live foundation surface.

## Result In Plain Language

The useful Wolfram idea survives, but in a narrower and cleaner form than
"all update orders are physical branches." A law can specify a local causal
partial order and leave the simulator free to execute unrelated events in any
order. All such executions then give the same record probability law. The
execution order is bookkeeping; the causal predecessor relation is physics.

This can remove **maximal synchronous execution** from the payload of the
causal-front candidate. It does not remove the payload that the synchronous
phrase was standing in for. The exact law must still say which already formed
records are causal inputs to a new write. In the tested construction, a
boundary-generated layer rank does that: an event reads only neighboring
records one layer earlier. Every linear extension of the resulting causal
DAG gives exactly the same joint record distribution.

If an asynchronous event instead reads every record present when the computer
happens to execute it, execution order is observable. Two adjacent same-layer
sites give an exact two-event counterexample. Updating left first produces
terminal records `00` or `01`; updating right first produces `01` or `11`.
The extra terminal sectors are permanent and readable, so a causal-trace
quotient cannot identify them. Randomizing the scheduler produces a third
law; it is not a quotient.

The constitutional lesson is therefore precise:

> A canonical law need not prescribe a global update order, but it must
> prescribe the causal input relation—or an exactly equivalent atomic update
> rule—well enough that every allowed execution order gives the same finite
> record-transcript law.

This is law-specification content, not a new standalone Record axiom. The
Wolfram mechanism helps compress the candidate law by replacing a preferred
clocked schedule with a causal equivalence class. It does not select the
weight kernel, actual history, or causal predecessor relation from the four
current sentences.

## Exact Two-Event Discriminator

On one lattice line embedded in `Z^3`, place permanent boundary records

```text
(-1,0,0): 0                         (2,0,0): 1
```

and leave the adjacent sites

```text
x=(0,0,0), y=(1,0,0)
```

open. Both are on the first boundary-distance layer. Under the one-ticket
incidence kernel, the old-front law writes `x=0` and `y=1` with certainty.

Now let a live asynchronous rule read every record present at firing.

```text
x then y:  P(00)=1/2, P(01)=1/2
y then x:  P(01)=1/2, P(11)=1/2
```

The first write becomes an extra neighbor of the second and changes its
kernel. Averaging the two schedules gives

```text
P(00)=1/4, P(01)=1/2, P(11)=1/4,
```

which is neither old-front law. Only the `01` terminal sector is common to
both orders. The `00` and `11` sectors carry different readable permanent
contents and cannot be declared gauge copies.

The obstruction does not depend on choosing the incidence value `1/2` at a
mixed neighborhood. To reproduce the old-front result in the order `x` then
`y`, a live binary kernel must have

```text
q(1 | one 0 and one 1) = 1.
```

To reproduce it in the reverse order, the same label-equivariant kernel must
have

```text
q(0 | one 0 and one 1) = 1.
```

These demands contradict normalization. In this exact fork, no normalized
live-read kernel can make both execution orders equivalent while retaining
the singleton-copy boundary behavior.

## Positive Causal-Trace Construction

Let the supplied finite boundary records have rank zero. For every event site
in the tested front, define its rank by its nearest-neighbor distance from the
boundary. An event of rank `d` reads only recorded nearest neighbors of rank
`d-1`. Those edges form its causal predecessor relation.

For a causal linear extension `e_1,...,e_n`, the joint law is

```text
P(r_1,...,r_n | boundary)
  = product_i p(r_i | records on Pred(e_i)).
```

Each factor is attached to an event and its fixed predecessor set. Swapping
incomparable events only permutes scalar factors, so the joint law is
unchanged. The runner checks a nontrivial diamond:

1. one mixed event samples from two oppositely labelled boundary records;
2. two incomparable children copy it;
3. a later join reads both children.

The two causal linear extensions give the same exact distribution: all four
event records are `0` with probability `1/2`, and all four are `1` with
probability `1/2`.

The construction is exactly translation covariant, covariant under all 24
proper cubic rotations, and equivariant under global outcome-name exchange.
It needs no preferred coordinate time or simulator order.

## What Was Removed And What Was Not

| candidate content | result |
|---|---|
| execute the whole front simultaneously | removable as implementation detail |
| causal antichain / predecessor relation | remains exact law content |
| boundary-generated event ranks | one positive way to define predecessors |
| a separate external clock | not needed for causal ordering |
| one-ticket outcome kernel | not selected by causal invariance |
| one actual realization | not selected by causal invariance |
| permanent append semantics | used to make inequivalent terminal sectors readable |
| all-path multiway support | does not determine a measure or realized path |

Boundary-distance rank is not claimed as the final mechanism. It works for
the tested fill-all-sites causal front. A more general law with skipped,
blocked, migratory, or context-programmed events may instead need locally
recoverable provenance, a phase certificate, or an atomic multi-site update.
Those are alternative realizations of the same semantic job.

There is also a state-sufficiency condition. If future predictions require a
causal tag that cannot be reconstructed from the current record configuration
and supplied boundary, that tag is hidden process state and conflicts with
the live qualification that a state is a configuration of records. A final
law must either make the predecessor relation reconstructible from records
and boundary or include the relevant causal provenance in record content.

## Wolfram Mechanism Assessment

The retained inspiration is:

- multiway support cleanly separates possible continuations from a measure;
- causal traces identify execution-order refinements of the same physical
  event structure;
- causal invariance can make incomparable-event scheduling nonphysical; and
- equivalence should be tested on complete future record transcripts.

The rejected shortcut is global confluence across distinct outcomes. A
permanent `0` record and a permanent `1` record cannot reconnect without
either changing a record or declaring readable differences unphysical.
Causal invariance itself is weaker: isomorphic causal graphs do not require
terminal states to merge, as Wolfram Research's exact counterexamples stress
([source](https://bulletins.wolframphysics.org/2020/11/confluence-and-causal-invariance/)).
It is therefore viable within a fixed record-outcome sector and may also hold
across distinct sectors with isomorphic causal structure. In neither case is
it an actualization rule or an outcome measure.

### Primary-source boundary

The Wolfram project's own technical presentation makes the same useful
separation, though with a different ontology. Its multiway graph contains the
entire set of possible update sequences, while an observer samples a foliation
or equivalences across that graph; the underlying model does not select one
path stochastically. See [Basic Concepts of Quantum
Mechanics](https://www.wolframphysics.org/technical-introduction/potential-relation-to-physics/basic-concepts-of-quantum-mechanics/)
and [Observer Theory](https://wolframinstitute.org/output/observer-theory).
The latter explicitly makes a perceived single thread depend on the
observer's branch-equivalencing behavior. That is a substantive observer
condition, not a derivation of the present framework's observer-independent
one-record history.

The rigorous causal-invariance result is narrower and directly reusable:
Gorard identifies update-order changes with discrete gauge transformations
when every allowed update order generates an isomorphic causal graph. See
[Some Relativistic and Gravitational Properties of the Wolfram
Model](https://arxiv.org/abs/2004.14810). The hypothesis is a property of a
specified rewrite rule; it neither selects that rule nor a measure or actual
member of its multiway support. The paper's gravity route also assumes a
dimension-preserving continuum regime. Accordingly, Wolfram-style causal
invariance is an excellent **law acceptance test** and a possible source of
schedule compression, but not missing formation, weight, actuality, or
gravity content by itself.

## Constitutional Consequence

This probe weakens the visible candidate-law inventory by one clause. The
final exact referent does not have to say "all ready sites fire at once." It
can instead define an invariant causal event structure and require the finite
record-transcript law to be independent of the chosen linear extension.

It strengthens the acceptance test for a future stable law reference:

> For any two allowed executions of one causal event structure, the exact
> finite readable-record distributions must agree after the declared event
> equivalence. If they do not, the schedule or a measure on schedules is
> additional physical content.

Nothing in the current words "nearest-neighbor," "admissible," or "records
form" identifies that structure. The result supports a single exact law
reference in Admissibility rather than adding clock, witness, scheduler, or
causal-graph prose to Record.

## No-Go Discipline: Narrow Claim

The licensed negative claim is only:

> In the tested adjacent same-layer fork, a normalized live-read binary
> kernel with singleton-copy behavior cannot reproduce the same old-front
> record law in both sequential orders.

It is not a no-go for all causal-invariant local laws.

### N1 — Alternative-route enumeration

| route | status | result |
|---|---|---|
| atomic whole-front update | `POSITIVE` | preserves the old-front law, but makes atomicity part of the exact rule |
| causal predecessor filtering | `POSITIVE` | all linear extensions agree exactly |
| locally stored provenance/phase | `LIVE` | can implement predecessor filtering if the state carrier pays for it |
| boundary-reconstructible rank | `POSITIVE IN TESTED FRONT` | no preferred simulator clock; depends on supplied boundary and fill-all growth |
| random schedule | `NEGATIVE FOR EQUIVALENCE` | creates a third measured law and needs its own weights |
| terminal-record quotient | `NEGATIVE IN COUNTEREXAMPLE` | `00`, `01`, and `11` are readable distinct sectors |
| different confluent rewrite law | `LIVE` | may exist, but must preserve nontrivial permanent outcome sectors and quantum repertoire |
| deterministic/global-history route | `LIVE` | could replace local sampled scheduling; needs its own exact intervention and frequency account |

### N2 — Wall-independence audit

The lattice, boundary, candidate weight kernel, record append rule, and two
event sites are fixed. Only live-read order changes. The positive repair fixes
the same kernel and changes only which causal predecessors it may read.

### N3 — Hidden-wall scan

The boundary seed, event addresses, rank rule, predecessor filter, and sample
law are explicit. A later generalization cannot silently treat an unrecorded
phase or provenance mark as part of the record-only state.

### N4 — Exact residual matching

The `00/01/11` transcript discriminator tests schedule dependence only. It
does not test Born weights, contextual settings, coherent propagation,
renewal, clock calibration, matter, or gravity.

### N5 — Resolution and rhetoric audit

All probabilities are exact fractions. The contradiction is algebraic and
two-event local. The conclusion is confined to live-read singleton-copy
kernels, not elevated to a universal impossibility claim.

### N6 — Partial-closure paths

The causal-DAG construction positively removes total execution order while
retaining only predecessor structure. Event-addressed random variables can
also make the equivalence pathwise; distributional equivalence is sufficient
for the present operational test.

### N7 — Strongest steelman

A final quantum causal law could generate its causal edges from local
algebraic dependencies, prove all linear extensions equivalent, reconstruct
the needed event structure from permanent records, and derive its own
transcript measure. Such a law would make the synchronous-front phrase wholly
dispensable. This probe supplies the acceptance test, not that final law.

### N8 — Cross-cycle echo

The earlier Wolfram probe found path weights and observer paths unselected.
The sampled-law pair found equal branch support with unequal measures. This
probe adds only the independent schedule wall: even after choosing a kernel,
uncontrolled live execution order can alter readable records. It does not
count the repeated measure/actuality walls as new evidence.

## Verification

Run:

```bash
python3 scripts/causal_schedule_equivalence_wolfram_inspiration_probe_2026_07_14.py
```

Expected terminal line:

```text
RESULT PASS=50 FAIL=0
```

The PASS count includes related checks and is not a count of independent
scientific facts.
