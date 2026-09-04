# Fundamental One-Qubit QCA Compilation — Cycle 12

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is a bounded construction, assumptions exercise, and
no-go stress test. It is not an axiom proposal, audit verdict, retained theorem,
or claim that nature is literally a computer. It changes no axiom, primitive,
premise registry, review queue, or audit surface.

Companion runner:

```text
scripts/fundamental_one_qubit_qca_compilation_cycle12_2026_07_14.py
```

## Result Up Front

Cycle 11's exact 22-qubit macrocell record-export QCA has **not** been compiled
into the current fundamental carrier. A smaller positive result and a smaller
wall have been isolated instead.

The positive result is important:

> A translation- and proper-cubic-covariant law can read a finite asymmetric
> pattern of permanent records as a relational program. The pattern, rather
> than the law, selects the gate's anchor, forward direction, and transverse
> frame.

The runner gives one explicit six-record header, scans it at all lattice sites
in all 24 oriented frames, and recovers exactly one nearest-neighbor control
edge. Translating the records translates the decoded gate. Applying any of the
24 proper cubic rotations rotates it. Two separated headers decode as two
disjoint gates. If decoded gates share an endpoint, a deterministic local
collision policy freezes them. Thus an axis, origin, and block boundary need
not be privileged in the law; they can be selected relationally by state.

That does not finish the compiler. Three exact barriers remain between this
decoder and an autonomous repeated fundamental QCA:

1. A nontrivial finite absolute macrocell partition cannot itself be invariant
   under every unit translation of `Z3`. Any 22-site block layout is supplied
   state/program structure or a law-level symmetry break.
2. The orbit of one nearest-neighbor edge under all unit translations and all
   proper cubic rotations is the set of every nearest-neighbor edge. It has
   degree six at every site, so it is not a disjoint gate layer. An axis/parity
   matching works, but the matching is changed by a unit translation and by an
   axis-changing rotation.
3. The relational header selects **which** directed gate is intended, but a
   repeated noncommuting circuit still needs **which layer is next**. A moving
   cursor clears its old site. If the cursor is a record, permanence is broken;
   if it is not a record, state is no longer records alone. An append-only
   clock front preserves old records, but it spends one fresh site per tick and
   therefore imports an unbounded blank boundary or eventually stops.

The smallest exact obstruction found in this cycle is therefore:

> For the tested partitioned CNOT compiler on one qubit per `Z3` site, a
> repeated directed noncommuting update cannot be simultaneously autonomous,
> covariant under unit translations and all proper cubic rotations, and
> scheduled by permanent records alone without either mutable hidden phase or
> an append-only clock front with unbounded fresh capacity.

This statement is deliberately narrow. It does **not** prove a general QCA
no-go. Commuting all-edge gates remain open. Yang-Baxter or other integrable
collision laws remain open. Relational state tilings remain open. An
append-only phase tape remains open as a boundary-conditioned construction. An
intrinsically universal QCA remains open. An asynchronous confluent rewrite
remains open. None has yet supplied all the missing content rather than moved
it into program, preparation, boundary, or law.

This cycle also does not compile the Cycle 11 architecture. Its exact coherent
commit, outward archive, renewal, and collision interfaces would still have to
be encoded after a fundamental scheduler is found. Conditional law clauses
remain distinct from framework premises throughout.

## Framework and Predecessor Refresher

The cycle was run against the current live sources:

- `docs/MINIMAL_AXIOMS_2026-06-29.md`;
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`;
- `docs/audit/data/axiom_premise_nodes.json`;
- the source notes for the scale-reference, kinetic-isotropy, and realized-state
  primitives;
- the current `origin/main` exercise, review-loop, and no-go-discipline
  instructions; and
- `docs/repo/CONTROLLED_VOCABULARY.md`.

The supplied carrier remains one `M2` possibility algebra at each site of
`Z3`. Admissibility supplies a fixed local rule relating a site's available
possibilities to nearest-neighbor conditions. Record supplies realized facts,
permanence, and readout by record content. None of those sentences supplies a
unitary, a gate family, a partition, a phase variable, a boundary preparation,
or an update schedule.

The exact Cycle 11 predecessor was also reread:

```text
docs/work_history/repo/review_feedback/
INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md
```

That construction gives a proper-cubic-covariant reversible record export on
an enlarged 22-qubit macrocell in an isolated no-return sector. Its first named
failure is the mismatch with the one-qubit fundamental carrier. This cycle
attacks that failure directly. It does not inherit the macrocell as if it were
already part of the framework.

## Exercise Zero — Target and Stop Conditions

The target was an exact realization with all of these properties:

1. one `M2` carrier at every fundamental `Z3` site;
2. nearest-neighbor causal propagation;
3. no absolute block tiling, preferred axis, or external layer clock in the
   law;
4. covariance under every unit translation and all 24 proper cubic rotations;
5. a collision policy for simultaneous programs;
6. an update order reconstructible from permanent records alone;
7. enough coherent interaction for Bell-capable physics; and
8. an explicit account of program, preparation, archive, and blank-capacity
   inputs.

A decisive positive would provide the complete local update and prove all
eight properties. A decisive negative would have to exclude commuting,
integrable, asynchronous, intrinsic-universal, topological, and infinite-tape
routes. This cycle reaches neither global endpoint. It constructs a relational
one-shot decoder and proves a scoped scheduling obstruction for the tested
partitioned noncommuting route.

## Assumptions Ledger

| ID | Layer | Assumption or candidate | Status in this cycle | What it buys | What remains |
|---|---|---|---|---|---|
| F1 | framework | current four axioms and three registered primitives | supplied | target ontology and carrier | no update law or scheduler |
| P1 | program | six permanent binary records in the header pattern | explicit state input | relational anchor and frame | framework does not prepare it |
| P2 | program | header bits are readable as a coherent control condition | conditional compiler content | selects a directed CNOT | NN decomposition of the multi-record control is open |
| G1 | gate | nearest-neighbor CNOT on the decoded edge | explicit candidate law | Bell-capable one-shot interaction | repeated application reverses itself |
| C1 | collision | freeze all candidates sharing a data endpoint | explicit candidate law | deterministic disjoint layer | not derived or uniquely selected |
| S1 | schedule | a present phase tells which layer runs | required by noncommuting circuit | ordered computation | phase source/representation is open |
| R1 | record clock | phase is a permanent record | tested | visible schedule | toggling/clearing violates permanence |
| H1 | hidden clock | phase is mutable but unrecorded | tested escape | reversible finite scheduler | future is not fixed by records alone |
| A1 | append clock | each tick writes a fresh permanent certificate | tested escape | record-only reconstructible order | consumes unbounded blank capacity |
| U1 | interpreter | one fixed law can condition on program records | exact finite example | separates law from program | does not choose or prepare the program |
| B1 | boundary | a relational domain/program is present | possible state selection | restores law symmetry | moves structure into initial/boundary state |
| Q1 | compilation | finite-radius header decoder is itself a NN gate circuit | not established | would make the one-shot rule microscopic | needs ancillas and a schedule |

The dangerous conflation is P1 with F1. A covariant law can accept a patterned
state without the pattern being an axiom. That does not mean the framework
derives the pattern, its abundance, or its preparation.

## Exact Probe 1 — Finite Block Tiling Obstruction

Consider a partition of `Z3` that is invariant under every translation. Let
`H` be the block containing the origin. Translation invariance makes the
equivalence relation satisfy

```text
x ~ y  iff  x-y is in H.
```

Therefore `H` is a subgroup of `Z3`. If it contains a nonzero vector `h`, it
contains every integer multiple `n h`, so it is infinite because `Z3` is
torsion-free. Consequently the only finite block of a fully
translation-invariant partition is the singleton `{0}`.

This does not prohibit finite macrocells. It classifies them. A nontrivial
finite macrocell decomposition must be one of:

- an absolute partition written into the law, which reduces unit-translation
  covariance;
- a relational partition written into a physical state/program; or
- a derived transient domain whose formation law and defects still need to be
  supplied.

The runner uses a side-four torus as a finite control. `2x2x2` parity blocks
cover every site exactly once, but every one-site translation changes the
partition. This is the finite shadow of the subgroup proof, not the proof's
premise.

Cycle 11's 22 logical qubits could of course occupy 22 fundamental sites. The
missing object is not dimension. It is a covariant, local, collision-safe way
to say which 22 sites form the current logical cell and which circuit layer is
active.

## Exact Probe 2 — Symmetric Matching Obstruction

A standard finite-depth nearest-neighbor circuit begins with a matching: a set
of disjoint edges on which two-site gates act simultaneously.

Start with one unoriented nearest-neighbor edge. Unit translations move it to
every edge parallel to itself. The 24 proper cubic rotations move its direction
through all six signed coordinate directions. The complete orbit is therefore
the set of every unoriented nearest-neighbor edge. Each site touches six of
them. It is not a matching.

An axis/parity rule such as

```text
pair (2n,y,z) with (2n+1,y,z)
```

is a perfect matching. It is changed by translation through one site, and an
axis-changing rotation changes it into a different matching. A sequence of
six or more such layers can recover symmetry stroboscopically, but the sequence
then needs a phase telling the law which matching is current.

This is not a ban on every symmetric local gate. If the gates on all edges
commute, they can be applied without a matching order. A diagonal `CZ` family
is the runner's positive control: overlapping `CZ` gates commute and one edge
entangles `|++>`. But `CZ^2=I`; blindly repeating the same layer restores the
prior state. More general commuting Hamiltonian flow remains a live route,
while stable fact formation and an internal tick still remain to be shown.

## Exact Probe 3 — Relational Motif Compiler

The law need not carry an axis if records can carry one.

Let a candidate program be an ordered triple `(o,d,t)` where:

- `o` is the anchor/data control site;
- `d` is a unit lattice direction;
- `t` is a perpendicular unit direction; and
- `u=d cross t` completes a right-handed cubic frame.

Place six binary records at

```text
o-3d
o-3d+t
o-3d+3t
o-3d+u
o-3d+2u
o-2d
```

with contents

```text
1, 0, 1, 1, 0, 1.
```

The zeros here are records whose content is zero, not absent sites. Exhaustive
scan over all candidate anchors and all 24 oriented `(d,t)` frames finds
exactly one match for an isolated header. The nominated gate acts on the
nearest-neighbor pair `(o,o+d)`.

Define the candidate one-shot law:

1. At every site and every oriented frame, test the same six-record pattern.
2. Collect every nominated nearest-neighbor pair.
3. If a site belongs to more than one nominated pair, freeze all candidates in
   that collision set.
4. Apply CNOT simultaneously to the remaining disjoint pairs.

The collision policy is deterministic and covariant. Two well-separated
headers survive; two headers sharing an endpoint freeze. Under a translation
or proper cubic rotation, every header, endpoint, and collision relation is
transported together.

This closes only the **relational selection** problem. The six-bit pattern has
finite radius but is not itself a compiled nearest-neighbor circuit. A
microscopic two-site-gate implementation must bring those controls together,
store intermediate results, and uncompute them. On one qubit per site that
requires work sites, a routing program, and a layer schedule—the same resources
under investigation. The motif therefore demonstrates that symmetry breaking
can live in state; it does not hide a completed compiler.

## One-Shot Physics and the Repetition Failure

On the decoded edge, CNOT maps

```text
|+>|0>  ->  (|00>+|11>)/sqrt(2).
```

That is exact coherent Bell-capable interaction on two fundamental sites. It
is enough to refute the claim that the one-qubit carrier cannot host a useful
entangler.

But CNOT is an involution. If the same permanent header causes the law to fire
again, the Bell pair returns to `|+>|0>`. A permanent static program cannot by
itself mean “run exactly once.” It needs either a stage certificate, a moving
program front, or a law whose dynamics make reapplication harmless.

A tempting rule is:

```text
if stage=0: apply U and set stage=1
if stage=1: do nothing
```

As a closed reversible map, this is not injective. Both `(0,x)` and
`(1,Ux)` reach `(1,Ux)`. The missing predecessor bit must be exported to an
archive or destroyed by an irreversible update. Cycle 11 supplied such an
archive only by enlarged rails and a no-return boundary.

## Causal Schedule and the Clock Trilemma

The need for an ordered phase is not cosmetic. On three bits, applying
`CNOT(0->1)` then `CNOT(1->2)` maps `100` to `111`. Reversing the order maps
`100` to `110`. The two schedules produce different records.

There are three direct representations of the missing phase:

### Mutable record phase

A one-hot cursor moves as

```text
10 -> 01.
```

The old site changes from `1` to `0`. If it was a record, the update conflicts
with permanence. A reversible binary phase similarly toggles a previous value.

### Mutable hidden phase

The cursor can be an unrecorded dynamical variable. That makes a reversible
finite scheduler straightforward, but two states with identical records and
different phase have different next records. The framework's state, defined by
records, no longer determines future record evolution without an extra
variable or equivalence restriction.

### Append-only clock front

Write a new certificate and never erase an old one:

```text
00000 -> 10000 -> 11000 -> 11100 -> ...
```

The current phase is reconstructible from the permanent record history. This
is the strongest record-compatible route, and it matches the user's clock-as-
final-lock intuition: a fact is not complete until the causal front has added
the next irreversible certificate.

It has a price. A tape of length `L` supplies exactly `L` new ticks. Indefinite
operation needs unbounded fresh sites, a recycling law that ceases to be
append-only, or a compressed/topological representation whose exact local
update remains to be constructed. Thus the arrow and renewal question move
into the supply of fresh record capacity.

## Fixed Interpreter Does Not Derive Its Program

An intrinsic-universal or autonomous-computation route is a serious steelman.
A single homogeneous QCA can interpret patterns in its state as gates, wires,
and clocks. It can thereby preserve symmetry at the law level while programs
and domains break symmetry physically.

The runner isolates the logical point with one exact controlled interpreter:

```text
U_interpreter = |0><0| tensor I + |1><1| tensor CNOT.
```

It is one fixed unitary. With program `0`, `|+0>` stays a product. With program
`1`, the same data becomes a Bell pair. Universality can make this interpreter
far richer; it cannot make the two program states identical or derive which
one is prepared.

Therefore an intrinsic-universal QCA would be a successful **law compiler**,
not automatically a derivation of:

- the program/domain state;
- its low-defect boundary;
- the initial active front;
- the supply of clean work sites;
- the interpretation of branch-relative records as one actual history; or
- a unique law among universal interpreters.

Those inputs may ultimately be generated by cosmological state selection, but
that is a separate theorem target.

## Recheck Against the TOE Interfaces

### Coherent quantum interaction

**Partial success.** One fundamental nearest-neighbor CNOT creates an exact
Bell pair. A commuting all-edge `CZ` control also entangles. The carrier is not
too small for coherent interaction.

### Actuality

**Still open.** The Bell output has two nonzero branches. Fundamental-site
compilation changes no branch amplitude into one observer-independent actual
history.

### Record-only future sufficiency

**Still open.** `(|00>+|11>)/sqrt(2)` and
`(|00>-|11>)/sqrt(2)` have the same equality record. CNOT followed by a
Hadamard maps them to distinct later computational records. A scheduler built
from records does not remove hidden coherent phase unless a superselection or
dephasing law is added.

### Formation and permanence

**Still open.** A one-shot stage write is irreversible unless predecessor
information is exported. A reversible repeated CNOT erases the correlation.
Absolute permanence still needs irreversibility, an infinite no-return sector,
or a restriction excluding inverse precursors.

### Clock/time

**Concept sharpened, not derived.** An append-only causal front is the only
tested representation that makes the current layer reconstructible from
permanent records alone. Its tick rate and fresh-capacity supply are not fixed
by the current axioms.

### Probability

**No closure.** The compiler preserves amplitudes and correlations. It does not
derive frame weights, outcome selection, or a prepared-state link.

### Matter/counting/chirality

**No closure.** A relational header can encode handedness as state through
`u=d cross t`; that demonstrates a physical chirality selector without a
law-preferred axis. It does not derive which domains occur or the counting rule
used in the mass lane.

### Resource/gravity lane

**No closure.** Append-only scheduling makes record capacity an explicit
consumed resource, strengthening the capacity-pressure picture. No scalar,
metric, tensor response, universal coupling, trajectory law, or lensing law is
derived by the compiler.

### Renewal/cosmology

**Boundary exposed.** A finite program and finite clean tape stop. An infinite
or renewing computation requires a special low-record boundary, an exact
recycling sector, or a self-reproducing relational domain. Homogeneity of the
law does not prepare those states.

## What This Says About Axiom Need

This cycle does not support inserting “the universe updates by blocks,” “CNOT,”
the six-record header, or a computation metaphor into the axioms. Those are
candidate law constructions and state programs, not minimal ontology.

It does establish a constitutional pressure point:

> If the final framework intends records alone to be a complete state for
> future facts, the causal/update phase must itself be recoverable from records.

The append-only front is one exact way to meet that demand conditionally. The
current Record axiom says records form and are permanent; it does not say that
new records extend a causal history, that update order is recoverable from
that history, or that fresh capacity exists. Whether one minimal formation
sentence can supply those consequences remains the language exercise. The
math here prevents a sentence from silently claiming more:

- “read” must identify an exact physical correlation or extension, not a
  spectator;
- “clock locks it” must say whether the clock is a new permanent record or a
  mutable hidden phase;
- “two witnesses” does not by itself choose a causal layer order;
- an append-only history makes the arrow explicit but imports renewal/capacity;
  and
- a symmetric interpreter does not derive its program or boundary.

## N1 — Alternative Routes

The following alternatives were enumerated before retaining the scoped wall.

1. **Absolute finite block compiler.** Enough Hilbert dimension; fails unit
   translation covariance unless block origin is law data.
2. **Relational state tiling.** Live. Permanent records can select domain,
   anchor, and axis while the law stays covariant.
3. **Commuting all-edge gates.** Live. Removes matching order; tested `CZ`
   control entangles but periodic repetition reverses.
4. **Yang-Baxter/integrable collision circuit.** Live. A braid-consistent gate
   could make different local orders equivalent.
5. **Asynchronous confluent rewrite.** Live. If every fair order reaches the
   same record normal form, no external layer phase is needed.
6. **Mutable unrecorded cursor.** Constructively easy; conflicts with records
   as complete state unless hidden phases are quotient-inert for all futures.
7. **Append-only unary clock front.** Live and record-compatible; consumes one
   fresh site per tick.
8. **Compressed or topological clock.** Live. Must update locally without
   changing permanent decoded records and must expose current phase.
9. **Intrinsic-universal autonomous QCA.** Live. Can encode compiler and
   scheduler in a relational program; shifts program/preparation/boundary
   inputs rather than deriving them.
10. **Infinite no-return archive.** Constructed at macrocell level in Cycle 11;
    fundamental compilation and collision-safe renewal remain open.
11. **Irreversible append law.** Directly makes records and stages; this is new
    dynamics, not a unitary derivation.
12. **Self-synchronizing solitonic clock.** Live steelman. Needs an explicit
    one-qubit local rule, collision analysis, and record decoder.

## N2 — Wall-Independence Audit

The three walls are not duplicates.

- The finite-block proof concerns spatial partition covariance and holds even
  before a gate is chosen.
- The matching proof concerns simultaneous two-site gate support and holds
  even if blocks are discarded.
- The clock trilemma concerns repeated noncommuting order and survives a
  successful relational decoder.

Removing one does not automatically remove the others. A relational state
tiling fixes the first but still needs a collision-safe gate schedule. A
commuting gate family fixes the second/third for that family but does not
produce permanent records or choose a program. An append-only clock fixes the
visible schedule while leaving capacity renewal open.

## N3 — Hidden-Wall Scan

The constructive motif carries additional unclosed assumptions:

- explicit zero-records are distinguishable from open sites;
- a finite-radius multi-record predicate can control a coherent data gate;
- the predicate can be decomposed into nearest-neighbor gates with only the
  one-qubit carrier;
- header records remain inert while data evolve;
- overlapping headers are detected before either gate fires;
- freeze is a physically selected collision response;
- a suitable domain/program is prepared; and
- defects do not generate inconsistent frames.

The runner tests the abstract decoder and collision relation. It does not
silently count these compilation obligations as closed.

## N4 — Residual Matching

The result matches the exact residual from Cycle 11:

```text
Cycle 11 residual:
    enlarged-cell QCA, not one-M2 fundamental compilation

Cycle 12 partial closure:
    one-M2 relational gate selection and exact one-edge entangler

Cycle 12 residual:
    NN implementation of decoder, autonomous phase, archive, and renewal
```

It also matches the earlier causal-front work: making a history append-only
solves visibility of order but consumes blank capacity. No new label has been
used to count the same boundary as a derivation.

## N5 — Rhetoric and Resolution

Permitted claim:

> The tested partitioned CNOT compiler needs a phase not supplied by permanent
> records unless it grows an append-only clock front.

Not permitted:

> No homogeneous one-qubit QCA can be universal, isotropic, or record-forming.

Permitted claim:

> Relational records can select a local frame while the law remains covariant.

Not permitted:

> The axioms derive the frame, program, or its preparation.

Resolution is therefore “partial construction plus named wall,” not a global
no-go and not a completed TOE law.

## N6 — Partial-Closure Paths

The shortest live programs are:

1. Replace CNOT partition layers with a cubic-covariant commuting or
   Yang-Baxter gate and test whether a stable record subalgebra grows.
2. Compile the six-record predicate into a one-qubit NN reversible circuit on
   a boundary-selected relational domain, accounting for every work bit.
3. Build an append-only moving causal front and measure capacity per stable
   logical record, defect rate, and collision behavior.
4. Search for an asynchronous confluent record rewrite whose terminal records
   are order-independent but whose quantum precursor remains Bell-capable.
5. Instantiate an intrinsic-universal one-qubit QCA with a finite relational
   program and audit exactly which blank-domain and phase resources it imports.
6. Reconnect any successful fundamental scheduler to Cycle 11's commit/export,
   then rerun actuality, record-sufficiency, recurrence, renewal, probability,
   and gravity interfaces.

## N7 — Steelman

The strongest surviving counterproposal is an autonomous intrinsically
universal one-qubit QCA with three features encoded in one relational domain:

- a static, permanent program pattern that defines a local cubic frame;
- a solitonic clock/front whose position is recoverable from records without
  erasing them; and
- collision gates satisfying a braid or confluence relation so microscopic
  update order is observationally irrelevant.

Such a construction could defeat both the partition and external-clock
versions of the wall. It would still need to show how the domain is prepared,
how an indefinite front renews capacity, how opposite coherent phases cease to
affect future records, and how one actual history emerges. No theorem here
excludes it.

## N8 — Cross-Cycle Echo

This cycle deliberately preserves the repeated warnings from earlier work:

- Cycle 9: conservative capacity response needs a source/current law.
- Cycle 10: a reversible dilation relocates irreversibility into environment
  preparation and discard.
- Cycle 11: an infinite no-return archive can stabilize a local record sector,
  but recurrence, collisions, actuality, renewal, and one-qubit compilation
  remain.
- Current Cycle 12: a relational program removes law-level axis/origin choices,
  but the scheduler becomes mutable hidden state or growing permanent history.

The same residual has not been renamed as “clock,” “read,” “program,” or
“universal computation.” The physical question remains: what exact local law
makes one new permanent fact, carries enough inverse/coherent information for
quantum physics, and leaves the next fact determined by the records without an
unrecorded phase or an unexplained infinite blank supply?

## Bottom Line

The one-qubit substrate is expressive enough for exact relational frame
selection and Bell-capable nearest-neighbor interaction. Symmetry is not the
main remaining obstacle: state can break symmetry while the law stays
translation/proper-cubic covariant.

The bare-metal issue is the causal phase. A static permanent record pattern
can name a gate, but it cannot make an involutory gate happen only once. A
finite reversible cursor must change something; a record cursor violates
permanence, and an unrecorded cursor violates record-only state sufficiency.
The cleanest surviving model is an append-only causal front: the clock's next
record is what finally locks the prior interaction into history. That model is
coherent and worth pursuing, but it makes fresh record capacity and boundary
renewal explicit physics obligations rather than free consequences of the four
axioms.
