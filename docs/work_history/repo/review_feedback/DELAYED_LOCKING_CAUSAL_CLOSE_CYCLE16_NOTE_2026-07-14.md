# Delayed Locking Behind a Local Causal Close — Cycle 16

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is a conditional exact construction, assumptions
exercise, and tightly bounded no-go stress test. It is not an axiom proposal,
retained theorem, audit verdict, or claim that nature is literally a computer.
It changes no axiom, primitive, premise registry, review queue, or audit
surface.

Companion runner:

```text
scripts/delayed_locking_causal_close_cycle16_2026_07_14.py
```

## Result Up Front

The strongest upstream escape left by Cycle 15 works, with a precise scope.

Its locking trigger is a purely local causal-close certificate; the global
scope of what that certificate can honestly close is the main issue tested.

There is a strict nearest-neighbor, homogeneous, proper-cubic covariant
delayed-locking protocol on one `M2(C)` per actual site. Still-open proposal
qubits move by nearest-neighbor `SWAP` gates. Each moving proposal leaves a
permanent direction-carrying fence trail behind it. The trail, rather than an
unrecorded cursor, identifies the current open tip. A permanent stop marker at
a named input port changes the last action from an ordinary fence write to a
terminal fence write. That terminal record writes a close record across one
nearest-neighbor edge. Two close records occupy orthogonal neighbors of the
merge site.

The merge site writes nothing until both close records exist. It then receives
the two proposal qubits from opposite nearest neighbors, applies the two
commuting controlled-NOT gates

```text
CNOT(left proposal -> output)
CNOT(right proposal -> output),
```

and locks the output parity. On basis inputs the stored value is exactly
`left XOR right`, which is symmetric under proposal exchange. On `|+>|+>`
inputs, recording even versus odd parity leaves the open endpoint pair in
`Phi+` versus `Psi+`. Under the supplied projective/Born instrument the two
alternatives have weight `1/2`. The construction therefore retains
Bell-capable alternatives rather than selecting one proposal as the winner.

Every control condition is visible in permanent records. The rule uses no
global clock, no hidden cursor, no priority, and no future-arrival oracle.
The output's record-only readiness condition is simply the correctly typed
pair of neighboring close certificates. For each fixed input preparation and
physical parity outcome, rewrite order does not matter. The exact finite
fixture has two four-step fronts, two arrivals, two closes, and one output:
eleven appends after a four-record seed. First-action, last-action, and twelve
random schedules are checked for every one of the four basis-input pairs; all
reach the same branch-appropriate fifteen-record terminal map.

What makes this honest is the meaning of “complete.” The close pair certifies
completion over two finite, explicitly named input ports. It does not certify
that no related proposal exists anywhere on the lattice. An input port is
complete because:

1. exactly one proposal carrier is supplied behind one source fence record;
2. the carrier propagates by information-conserving SWAPs;
3. every vacated carrier site becomes a permanent fence record;
4. a permanent stop record terminates the named port; and
5. the close certificate can form only after the conserved front reaches that
   stop.

Within that candidate protocol, a close certificate is a genuine causal
proof, not a timeout. A later proposal on the same one-cell channel encounters
the already-recorded trail and cannot pass. In a general finite region, a
closed surface of fence records with finitely many named ports gives the same
result: before the ports close there is a path from outside to inside; after
all port sites record, graph search proves there is none.

There is also a narrow exact negative result. No finite-radius record-only rule
can infer the absence of all later incompatible proposals on an unbounded,
unclosed input channel. For every finite radius `r`, one history with no later
source and another with an incompatible source at distance `r+2` have the
identical radius-`r` record view. The second source still has a nearest-neighbor
path to the decision. Waiting longer without a new record does not change the
local state. This is the finite-radius silence no-go. It is not a no-go against
bounded causal diamonds, explicit close/fence records, conserved fronts, or a
global-history constraint; those are precisely the live escapes tested here.

The price is new law and boundary content, not a new Record sentence. Front
conservation, typed propagation, stop recognition, arrival/close writing, the
parity gate, and its occurrence condition are candidate law. Source records,
stop markers, finite port geometry, prepared proposal carriers, and blank
corridors are boundary/preparation inputs in the minimum fixture. Born weights,
one-history actuality, and rate remain open.

Formation-as-certified-extension is a theorem of this protocol, not a theorem
of the current four axioms. The `K` certificate is derived only within the
candidate protocol. Its semantics are not contained in permanence, and no new
Record axiom is forced. The live constitutional question is therefore not
whether to define a record as “closed.” It is whether a final TOE law can
derive a physical finite input boundary and close process rather than merely
supply them.

## Framework and Predecessor Refresher

The probe was checked against:

- `docs/MINIMAL_AXIOMS_2026-06-29.md`;
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`;
- `docs/audit/data/axiom_premise_nodes.json`;
- the scale-reference, kinetic-isotropy, and realized-state primitive notes;
- the fresh `origin/main` exercise and no-go-discipline instructions; and
- `docs/repo/CONTROLLED_VOCABULARY.md`.

The foundation remains four axioms and three registered primitives. Lattice
supplies the actual cubic site set and nearest-neighbor relation. Qubit
supplies one local `M2` possibility algebra. Admissibility supplies a fixed
uniform nearest-neighbor availability rule. Record supplies locked local
possibilities, permanence, and record-only readability, while explicitly
withholding formation dynamics. None supplies a proposal carrier, preparation,
propagation gate, causal-close semantics, occurrence, branch selector, Born
weight, or rate.

Cycle 15 proved that compatible same-content record additions form an abelian
grow-only structure. It also isolated the smallest post-write failure:
distinct permanent outputs at one site have no common permanent extension. Its
strongest remaining route was upstream of formation: keep the proposals open,
make a compatible joint value, and write only when a local causal certificate
says the input set is complete.

This cycle attempts that steelman rather than treating “complete” as an
English word.

## Minimum Geometry

Let a merge cell be `(t,d,e)`, where `d` and `e` are perpendicular signed unit
lattice directions and `u=d cross e`. The output is at `t`; the two open
proposal inputs are

```text
L = t-d,
R = t+d.
```

The left front approaches its input sideways with relational frame `(-e,-d)`.
The right approaches with frame `(-u,d)`. Let their terminal fence sites be

```text
Y_L = L+e,
Y_R = R+u.
```

Their stop and close sites are

```text
left stop     Y_L-d      left close     Y_L+d = t+e
right stop    Y_R+d      right close    Y_R-d = t+u.
```

At the last pre-move step, each stop is one edge from the open proposal and the
future terminal fence site is that proposal site. The final SWAP moves the
proposal from `Y_L` to `L` or from `Y_R` to `R`, then records the vacated `Y`
site. Each terminal-to-close write is one edge. Both close sites and both input
qubits are nearest neighbors of the output. All eleven named roles, including
the two source records, are site-disjoint in the minimum fixture.

Each source fence record is four front-steps behind its terminal `Y` site; the
initial proposal qubit is one step forward from that source record. Three
ordinary fence SWAPs and one terminal SWAP move each proposal into `L` or `R`.
The numerical length four is a finite test fixture, not a law constant: the
same local transition works for any blank corridor length.

The rule ranges over every site and every one of the 24 oriented proper-cubic
frames. There is no coordinate origin or law-level axis. The runner checks all
24 proper rotations and six unit translations.

## One `M2` Per Site

`F`, `M`, `T`, and `K` are not extra onsite registers. Each typed content is a
rank-one projector in the site's one `M2`. A generic Bloch vector

```text
v_kind(d,e) = normalize(a_kind d + b_kind e + c_kind (d cross e))
```

encodes both the content kind and transported relational frame. The four
coefficient triples used by the exact runner are

```text
F : (1,2,4)
M : (1,3,7)
T : (2,5,11)
K : (3,8,17).
```

Their proper-cubic orbits are disjoint. Output parity uses the antipodal
pair along the transported output axis. The runner checks 102 distinct
rank-one projectors: four generic 24-member frame orbits plus six parity-axis
projectors. This is a large menu of possible rank-one facts in one qubit
algebra, not a 102-level carrier.

The construction imports the transported frame needed to compare these
possibilities across sites. As in Cycles 13–15, that import is not hidden under
“no possibility is privileged.”

## Strict Nearest-Neighbor Protocol

### P0 — source and blank channel

A source boundary supplies one fence record `F(d,e)`, an arbitrary open
proposal qubit on its forward neighbor, and prepared blank qubits ahead. The
proposal can be `|0>`, `|1>`, a superposition, or part of an entangled state.
The rule does not inspect its value.

Prepared proposal carriers and blank corridors are imported. A blank forward
carrier is load-bearing: SWAP preserves the proposal exactly only while moving
the blank backward. A law-generated reset could replace this boundary input,
but it would carry Cycle 14's explicit irreversibility/archive price.

### P1 — conserved front propagation

Suppose `y` has fence record `F(f,q)`, its forward neighbor `x=y+f` is open,
the next carrier `x+f` is an open prepared blank, and `x+q` is not the matching
stop record. Then:

1. SWAP the states at `x` and `x+f`;
2. locally prepare the now-vacated blank at `x` as the `F(f,q)` possibility;
3. append the permanent `F(f,q)` record at `x`.

The proposal moves one edge and is not copied. The old carrier becomes a fact.
Only the last fence record has an open forward neighbor; every earlier fence
record points into another record. Thus the visible trail locates the front
without a cursor. Direction is carried by the record's relational content, so
the same-content trail does not propagate backward.

Every quantum gate and every write in this step is onsite or nearest-neighbor.
The control pattern is the radius-one neighborhood of the open tip.

### P2 — terminal SWAP rather than continued propagation

If the matching stop record `M(f,q)` exists at `x+q`, the ordinary propagation
rule is disabled. Instead, the protocol SWAPs the proposal from `x` to `x+f`
and appends terminal fence record `T(f,q)` at the now-vacated `x`. These guards
are mutually exclusive. There is no “arrival wins” priority between two
simultaneously legal actions.

The input proposal remains open at `x+f`. Writing `T` does not measure its
internal state. The previous fence and the stop are both nearest neighbors of
the pre-move proposal, so this is a radius-one NN event rather than a
finite-radius atomic certificate write.

### P3 — local close

A terminal record `T(f,q)` appends close record `K(f,q)` at its neighbor
`x-q`. In the two-port geometry these two `K` records land at `t+e` and `t+u`,
both adjacent to the output.

The close record's meaning is causal and protocol-relative:

```text
the one conserved front assigned to this named port reached its permanent
stop, and its permanent wake blocks another front on the same channel.
```

It does not mean “the whole universe has no other proposal.”

### P4 — symmetric joint lock

The output rule recognizes the two typed close records in its nearest-neighbor
set. Only then does it act on the two opposite open input qubits and its blank
output carrier. The two CNOTs commute, so their order is physically irrelevant.
Measuring output parity and appending `J0` or `J1` is the only locking event.

The endpoints remain open. They can later be read into additional permanent
records, but no endpoint read is required for the joint parity fact to exist.

Front propagation is candidate law content. Terminal-arrival and close writes
are candidate law content. The parity instrument is candidate law content.

## Exact Quantum Result

For computational-basis proposals,

```text
|l>|0>|r> -> |l>|l XOR r>|r>.
```

The runner checks all four pairs. Exchanging `l` and `r` leaves the output
unchanged. Neither input is selected or overwritten.

For coherent proposals,

```text
|+>|0>|+>
  -> (|000> + |011> + |110> + |101>)/2.
```

Conditioning on the output record gives

```text
J0: endpoints Phi+ = (|00>+|11>)/sqrt(2)
J1: endpoints Psi+ = (|01>+|10>)/sqrt(2).
```

The exact weights are `1/2,1/2` under the supplied Born instrument. The
framework does not derive those weights or select one output. Born weights and
actuality remain open.

This is not a universal quantum-state merger. It computes one symmetric
binary relation in a supplied frame and basis. It does not clone arbitrary
states, choose a representative pure state, or decide every possible proposal
algebra. The runner explicitly checks that SWAP moves an arbitrary qubit and
does not clone it.

## Record-Only Readiness and Schedule Independence

Readiness for output formation uses only:

```text
K(-e,-d) at t+e
K(-u,d) at t+u
open input/output roles fixed by those relational contents.
```

No hidden wavefunction value controls whether the output is ready. The open
qubits carry the physical proposal content, but the control state is the
permanent record pattern. This is record-only readiness, not a claim that an
unrecorded quantum alternative is itself readable.

For each supplied basis-input pair, front movements on the two channels
commute. Arrival and close on one side commute with all actions on the other.
The output is enabled only after both close actions. Every action appends one
record and changes none. The finite protocol terminates after eleven
appends, so all fair schedules reach the same terminal branch.

The four-record boundary seed is

```text
two source fence records + two stop records.
```

The generated records are

```text
6 additional ordinary fence records
+ 2 terminal-arrival fence records
+ 2 close records
+ 1 parity output
= 11.
```

The final count is fifteen. No cleanup transition or mutable phase remains.

## What “Causally Complete” Can Mean Locally

A local certificate can prove closure only for a locally specified finite
interface. In this protocol, the interface is two named ports and the proof
object is the pair of `K` records whose legal ancestry is fixed by the candidate
law.

There are four equivalent positive pictures at increasing scale.

### Bounded causal diamond

A finite diamond declares its incoming faces or ports. A reducer can lock once
each declared incoming branch has supplied a close record. The port list is
finite physical structure, not an inference from silence.

### Explicit close/fence records

A recorded shell around a finite region blocks every lattice path except named
ports. The runner builds a cubic shell of radius three. It has 218 sites. With
a port open, breadth-first search finds an outside-to-center path. With both
port sites recorded, no path exists. This is an exact graph separator and an
explicit storage cost.

### Conserved fronts

One source front moves by unitary SWAP and leaves a recorded wake. No second
same-port front can pass through that wake. The close record therefore certifies
arrival of the one front whose conservation is part of the law. Spontaneous
front creation would invalidate the certificate, so “no creation except named
sources” is part of the causal-close law, not supplied by Record.

### Aggregated finite closure

A larger finite boundary can combine many port-close records through a tree of
same-content, append-only certificates until one local root certificate exists.
That is a direct generalization of the two-port cell. It costs sites and causal
depth but needs neither a global clock nor a future oracle.

These routes establish local physical closure. They do not establish that the
universe has a globally final time or that all relevant causes always fit a
predeclared finite interface.

## Finite-Radius Silence No-Go

The scoped claim is:

> On an unbounded input channel that has no trustworthy close/fence record and
> permits a later source, absence of a later proposal is not decidable from any
> finite-radius record view.

Fix any radius `r` and any candidate local readiness pattern around decision
site `t`. Construct two allowed prefixes:

```text
H_closed: the local pattern and no later source;
H_open:   the identical local pattern plus a source at distance r+2.
```

Their radius-`r` restrictions are identical. The second source lies outside
the inspected ball and has an open nearest-neighbor path toward `t`. Therefore
any radius-`r` function gives the same answer on both prefixes. If it locks on
`H_closed`, it also locks on `H_open`; if it waits on `H_open`, it also waits on
`H_closed`. The argument works for every finite `r`.

A timeout is not additional causal evidence unless ticking itself appends a
physical record with a law that closes the input interface. “Nothing happened
for a while” is unchanged state plus an imported rate convention.

The runner instantiates the indistinguishable pair for radii 1 through 16 and
constructs the later nearest-neighbor path explicitly. The proof is analytic
for every finite radius; the finite sweep checks the implementation.

The claim is deliberately narrow. It says nothing against:

- a bounded input set;
- an explicit close record;
- a physical barrier;
- a conserved finite number of fronts;
- a domain whose causal past is provably finite; or
- a nonlocal/global-history admissibility rule.

## Global-History Escape

A global-history constraint can admit only complete histories, for example:

```text
both named proposal events occur before CLOSE,
and no proposal occurs after CLOSE.
```

This condition admits both proposal orders and rejects late-after-close
histories. It can therefore supply completion without a local future oracle.
But it is a restriction on whole histories. A finite prefix cannot certify the
predicate that constrains its future completion.

Global-history consistency remains a live nonlocal escape. Its exact action or
constraint, boundary class, intervention semantics, and one-history selection
would be law/boundary content. It is not derived by relabeling a local record.

## Science-Lane Ledger

| TOE lane | Positive result | Honest residual |
|---|---|---|
| formation | one parity record forms only after two law-generated local close certificates | the close protocol and occurrence rule are supplied law |
| collision | incompatible open proposals become one symmetric relational value before any conflicting write | not a universal merger; capacity/output-site cost remains |
| locality | every gate/write is onsite or NN and every control is radius one | source/stop geometry and blank channel supplied |
| covariance | site/frame law checked under translations and all 24 proper rotations | transported frame connection imported |
| record readiness | `F/M/T/K/J` phase is wholly visible in records | open proposal wavefunction is deliberately unreadable |
| Bell/probability | parity lock leaves `Phi+` or `Psi+` alternatives | Born weights, instrument uniqueness, actuality open |
| time/clock | causal depth and certificate order are explicit | rate remains open |
| capacity/gravity | closed shell and wake expose exact storage cost | no curvature or gravitational dynamics follows |
| mass/counting | no new result | counting/conjugacy fork untouched |
| matter/chirality | oriented coherent fronts are available | no fermion or chirality theorem follows |

The clock can serve as a close only if a clock record is physically connected
to closure of a finite input interface. A bare elapsed duration cannot prove
that an unbounded channel has no future cause.

## Law, Boundary, and Derivation Classification

### Candidate exact law content

- front propagation is candidate law content;
- no spontaneous proposal-front creation inside a closed channel;
- stop recognition and the mutually exclusive propagate/terminal guard;
- arrival and close writes are candidate law content;
- the parity instrument is candidate law content; and
- the occurrence event that chooses one allowed output record.

### Boundary/preparation content in the minimum fixture

- stop markers and finite port geometry are boundary content;
- two source fence records;
- prepared proposal carriers and blank corridors are imported;
- a transported relational frame; and
- finite open capacity around the cell.

### Derived only after those inputs

- proposal information reaches the port unchanged;
- the recorded wake blocks a later same-port front;
- the `K` certificate is derived only within the candidate protocol;
- two `K` records imply readiness over the two declared ports;
- parity is symmetric; and
- formation-as-certified-extension is a theorem of this protocol.

### Still open

- Born weights and actuality remain open;
- rate remains open;
- autonomous generation of stop/source geometry;
- whether all physical events possess finite closeable input interfaces;
- global-history law versus local sampled occurrence; and
- the downstream mass, gravity, and matter closures.

Finite-radius silence is not causal completeness. The positive result is not a
theorem of the current four axioms. No new Record axiom is forced.

## No-Go Discipline Gate

**No-go discipline status: PASS.** The negative claim is only the
finite-radius silence no-go for unbounded unclosed channels. Positive close
routes are preserved rather than rhetorically absorbed into it.

### N1 — Alternative route enumeration

1. **Wider finite radius — ATTEMPTED.** Let the readiness rule inspect a larger
   ball. For each finite radius the runner places a later source two steps
   outside it, leaving the entire inspected record view unchanged.
2. **Timeout or patient waiting — ATTEMPTED.** Wait longer before locking.
   Without a new physical close record, the local record state is unchanged;
   rate or duration is not evidence that the channel is closed.
3. **Bounded finite ports — ATTEMPTED.** Declare a finite input interface and
   require one close per port. This succeeds and lies outside the negative
   claim's unbounded-unclosed premise.
4. **Explicit closed fence — ATTEMPTED.** Surround a finite region by records
   and close its named ports. This succeeds; the exact cubic-shell graph test
   exhibits the capacity cost.
5. **Conserved proposal front — ATTEMPTED.** Permit exactly one front per port
   and leave a permanent wake. This succeeds conditional on source and
   no-creation law content.
6. **Topological/unitary transport — ATTEMPTED.** Move still-open information
   reversibly instead of recording it early. SWAP succeeds at transport but
   supplies no completeness signal by itself; coupled to a conserved front and
   fence it becomes the positive protocol.
7. **Global-history restriction — ATTEMPTED.** Admit only histories in which
   close is globally final. This remains live and escapes the local no-go, at
   the price of an exact nonlocal law and boundary class.

Seven distinct routes exceed the required five. The negative is not stated
against the four successful/live escapes.

### N2 — Wall-independence audit

The raw conditions collapse into four load-bearing groups:

| Pair/group | Does closing first close second? | Does closing second close first? | Independent? |
|---|---:|---:|---:|
| causal-close law `C` vs quantum carrier/instrument `Q` | no | no | yes |
| `C` vs actuality/weight `A` | no | no | yes |
| `C` vs rate `R` | no | no | yes |
| `Q` vs `A` | no | no | yes |
| `Q` vs `R` | no | no | yes |
| `A` vs `R` | no | no | yes |

`C` already groups finite port geometry, source conservation, fence/stop
semantics, and `F->T->K` transitions because the close certificate would fail
if any were removed; they are components of one causal-close law rather than
inflated as independent walls. `Q` groups prepared carriers, blank transport
sites, parity gates, and measurement basis. `A` is which allowed outcome is
actual and its weight. `R` is physical rate. Boundary seed values are exposed
separately and not counted as independent universal laws.

### N3 — Hidden-wall scan

| Phrase/hit class | Classification |
|---|---|
| “candidate protocol/law” | explicit conditional content `C` or `Q` |
| “prepared blank” | explicit preparation import in `Q` |
| “finite named ports” | explicit boundary component of `C` |
| “transported frame” | explicit frame import in `Q` |
| “supplied Born instrument” | explicit actuality/weight group `A` |
| “registered primitives” in refresher | non-load-bearing inventory; none is enlarged |
| “by construction,” “naturally,” “obviously,” “standard QFT” | absent from load-bearing proof |

No hidden condition was discovered after the four-group collapse.

### N4 — Residual matching

| Prior witness | Prior residual | Current residual | Match/use |
|---|---|---|---|
| Cycle 15 compatible-seed merge | no common extension after distinct permanent writes | knowing completeness before a write | no; motivation only |
| Cycle 14 dynamic collision | first-arrival order changes permanent builder output | future source outside finite local view | no; motivation only |
| Cycle 13/14 Bell cages | exact NN entangling/read capability conditional on preparation/instrument | Bell preservation under parity lock | yes; calculation independently rerun here |
| Cycle 12 finite-radius decoder wall | uncompiled finite-radius program predicate | strict NN causal-close circuit | no; the current transitions are explicitly NN |
| current radius-pair proof | indistinguishable local views with a far later source | same | exact self-contained witness |

No nonmatching prior note is used as authority for the current no-go.

### N5 — Rhetoric audit

The tested negative resolution is one decision site, one unbounded unclosed
input channel, and every finite observation radius. The proof also applies to
any finite block whose exterior channel remains open by placing the source
outside the block. It does not test or deny lattice-wide/global-history
constraints, bounded causal pasts, closed topological sectors, or finite
physical horizons. Accordingly the note never broadens the result to “local
causal completeness is impossible.” Only finite-radius silence on an unclosed
channel is excluded.

### N6 — Partial-closure path scan

The legitimate partial closure is exactly the import-bearing form:

```text
take causal-close law C and quantum law Q as explicit conditions
-> prove the certified parity-formation theorem
-> audit whether source/stop/close structure can be derived and retire C.
```

No naming convention turns silence into closure. No current primitive supplies
front conservation, port finiteness, or `K` semantics. Conversely, because the
bounded protocol succeeds, the note does not claim a new axiom is required.
The candidate stays in conditional-theorem form until an import-retirement
derivation or a deliberate law/axiom placement occurs.

### N7 — Steelman

A hostile reviewer should object that the universe need not decide completion
from an arbitrary open-channel prefix at all. A globally constrained history,
a finite causal past generated by a physical horizon, or a conserved
topological charge could make the full proposal set finite without locally
enumerating future arrivals. That objection is correct. The global-history
route remains live, and a horizon/charge can act as a physical fence. The
present no-go therefore excludes only an unmarked finite-radius silence oracle.
The strongest local version of the objection—conserved fronts plus explicit
stops—is implemented positively in this cycle.

### N8 — Cross-cycle echo

Repository search found several structurally similar but nonidentical routes:

- `DETERMINISTIC_UNIQUE_EXTENSION_RECORD_SECTOR_NOTE_2026-07-14.md` keeps a
  two-boundary/global-consistency route live;
- `APPEND_ONLY_CAUSAL_BELL_WIRE_CYCLE13_NOTE_2026-07-14.md` keeps unique global
  history and finite-radius program recognition live;
- `SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md` keeps global
  consistency live for collisions;
- `CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md` treats an exact
  global-history constraint as law content; and
- Cycle 15 explicitly queued delayed compatible writing upstream of formation.

None has since turned absence into a local fact by convention. Their live
global/boundary mechanism is included here rather than dismissed. The local
conserved-front mechanism is the new partial retirement of the Cycle 15 wall.

## Bottom Line for Formation Language

This cycle gives “locking after closure” a real bare-metal model:

```text
open alternatives propagate coherently
-> permanent wakes delimit a finite causal interface
-> local close records certify every named input
-> a symmetric joint fact is computed
-> only that joint fact locks.
```

That is enough to show the concept is physically coherent, local, covariant,
record-driven, and Bell-capable. It is not enough to put “causally complete”
into the Record axiom as if its meaning were already foundation-supplied. The
certificate works because an exact law gives `F`, `M`, `A`, and `K` their causal
semantics and because the boundary supplies a finite port structure.

The next decisive probe is therefore not another synonym hunt. It is whether
finite closeable causal interfaces can be generated autonomously from the
existing lattice/admissibility structure, or whether causal closure is the
irreducible dynamics the final framework still lacks.
