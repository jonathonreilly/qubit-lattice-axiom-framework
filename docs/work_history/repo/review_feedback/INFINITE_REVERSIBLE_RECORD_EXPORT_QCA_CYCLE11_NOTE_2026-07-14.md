# Infinite Reversible Record-Export QCA — Cycle 11

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is an exact enlarged-cell construction and bounded
assumptions exercise. It is not an axiom proposal, audit verdict, retained
theorem, cosmology, or claim that the universe is literally a computer. It
changes no axiom, primitive, premise registry, review queue, or audit surface.

Companion runner:

```text
scripts/infinite_reversible_record_export_qca_cycle11_2026_07_14.py
```

## Framework and Sibling Refresher

This cycle reuses the same current-turn framework refresher as Cycle 10:

- the current Lattice, Qubit, Admissibility, and Record text in
  `docs/MINIMAL_AXIOMS_2026-06-29.md`;
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, the live
  `axiom_premise_nodes.json`, and the source notes for the scale-reference,
  kinetic-isotropy, and realized-state primitives;
- the current `origin/main` exercise, review-loop, and no-go-discipline
  instructions; and
- `docs/repo/CONTROLLED_VOCABULARY.md`.

The conclusion does not enlarge any of those surfaces. In particular, Qubit
still supplies one `M2` possibility algebra per fundamental site, Record still
says records form and are permanent, and no supplied premise gives a unitary,
event trigger, blank tape, branch selector, source current, scheduler, or
metric.

This cycle also read and independently executed the assumptions slice's
`CFSI-QB16` result:

- `docs/work_history/repo/review_feedback/AUTONOMOUS_HOMOGENEOUS_BINARY_NUCLEATION_NOTE_2026-07-14.md`;
- `scripts/autonomous_homogeneous_binary_nucleation_probe_2026_07_14.py`.

Its current deterministic run gives `PASS=127, FAIL=0`. The narrow cross-check
agrees: equality/complement encoding relative to a physically recorded
rank-one effect is invariant under global label exchange and simultaneous
unitary conjugation; separated packets with different relational references
reject hybrids. That result is a sound relational decoder under its stated
conditions. It explicitly does not derive cross-site reference transport,
generated finite composition, or nearest-neighbor compilation of the initial
finite-radius atomic write. This note does not edit that sibling.

## Result Up Front

The infinite reversible steelman is mathematically real. It can be made exact
on an enlarged lattice cell.

At each macrocell, provide:

```text
signal S                         1 qubit
record marker M and content R    2 qubits
one active event register A      1 qubit
six spent-event rails B_d        6 qubits
six witness-presence rails P_d   6 qubits
six witness-content rails C_d    6 qubits
                                 ---------
                                 22 qubits
```

There is an onsite proper-cubic-invariant unitary that swaps

```text
active event + blank record
    <->
committed record + symmetric one-particle spent shell.
```

For signal value `s`, its forward face is

```text
|S=s,A=1,M=0,R=0,B=vac>
  -> |S=s,A=0,M=1,R=s> (1/sqrt(6)) sum_d |B_d=1>.
```

Linearity makes an input `(|S=0>+|S=1>)/sqrt(2)` into a Bell-capable
relational record. A second onsite unitary writes, on every fresh direction
rail,

```text
P_d = 1,                 C_d = R.
```

Then every `B_d,P_d,C_d` rail shifts one lattice edge in direction `d`. All
onsite gates are identical at every translate, the six directions are treated
as one proper-cubic orbit, and the rail shifts are range one. The runner checks
the local unitaries, all 24 proper cubic rotations, translations, and global
rail permutation exactly.

On infinite initially blank rails and for one isolated event, this works:

- the local marker and content remain unchanged;
- a norm-one spent shell moves outward and never returns;
- six new relational witnesses leave per tick;
- record `0` is distinguished from blank by `P=1,C=0`;
- record `1` is `P=1,C=1`; and
- the full state remains pure and reversible.

That is the strongest positive result so far. It gives bare-metal meaning to
“the read locks it” under a reversible interpretation: the local read is the
commit correlation, and the information needed to reverse it is carried away
by a spent shell and the witness rails. The clock can count fresh rail layers
crossing the commit front. It does not select a branch.

The integration is not a TOE closure. The classification is sharp:

```text
exact object constructed:
    an enlarged-cell, nearest-macrocell QCA architecture

not constructed:
    a finite-block nearest-neighbor compilation on the fundamental
    one-qubit-per-site lattice with unit-translation and proper-cubic covariance
```

The apparent irreversible shift is not produced by the unitary. It is
relocated to the initial blank-tape/no-return boundary: the full QCA remains
reversible, while a local observer ignores the outgoing inverse information.

Seven exact failures remain.

1. **Fundamental-carrier mismatch.** The law uses 22 qubits per macrocell, not
   one `M2` per fundamental site. A finite block has enough dimension, but no
   unit-translation-covariant block code into the current one-qubit `Z3`
   substrate has been derived.
2. **Permanence is sector-relative.** On a side-`L` torus, the spent shell
   returns after `L` ticks and the same unitary erases the record. On the
   infinite lattice, six properly arranged incoming spent pulses reconstruct
   the inverse precursor. The record is stable only in an isolated no-return
   sector.
3. **Witness rails collide.** A downstream record XORs an upstream presence
   bit from `1` to `0`; the fixed six-rail architecture is not append-only for
   arbitrary positive-density histories.
4. **One-history actuality does not follow.** The exported state is a pure GHZ
   superposition. Its local record density is diagonal, but both branches
   remain nonzero. Tracing rails gives branch-relative consistent records to a
   conditioned observer; it does not produce one observer-independent actual
   history.
5. **Record-only future sufficiency does not follow.** Opposite Bell phases
   have identical equality records. A Bell recombination maps them to distinct
   later records. Record sufficiency holds only if the law permanently forbids
   all phase-sensitive continuations, which is an additional superselection
   clause.
6. **Renewal is a boundary resource.** Infinite blank incoming rails and
   polarized source/sink tapes are special state data. A finite tape exhausts
   or recurs. Homogeneity of the unitary does not prepare its low-record
   environment.
7. **Causal schedule covariance, Green relaxation, and common coupling do not
   follow.** Noncommuting local gate orders differ. A coherent resource rail is
   ballistic; the Green profile appears only after fresh/traced direction
   information. A common QCA tick still permits species-dependent phase and
   transport laws.

The smallest exact obstruction is therefore not “infinite unitary record
formation is impossible.” It is this:

> In finite dimension, a record subspace invariant under a reversible unitary
> cannot receive amplitude from its blank complement. Formation plus absolute
> forward permanence needs either fundamental irreversibility, an infinite
> proper invariant sector, or an explicit restriction excluding every inverse
> precursor.

An infinite bilateral shift shows why the infinite route stays open: the
half-line `n>=0` is forward invariant under `n->n+1`, while `-1` enters it and
the full shift remains reversible. The construction above is a local physical
version of that escape, but only on the no-return state sector. It does not yet
show that the current Record axiom's unqualified permanence follows for every
law-admissible history.

## Exercise Zero — Exact Target and Stop Conditions

The target was one exact law that simultaneously:

1. is local, translation covariant, and proper-cubic covariant;
2. carries coherent Bell-capable interaction;
3. exports inverse/branch information to ever-fresh outward degrees;
4. leaves a stable relational record decoder;
5. sustains conservative resource current and the Green response without an
   external sink; and
6. derives actuality, renewal, schedule covariance, and common clock/transport
   response rather than adding them in prose.

The enlarged-cell QCA closes items 1–4 for one isolated no-return event. It
does not close them for arbitrary record histories, and it does not close
items 5–6. A decisive positive would need a one-qubit fundamental QCA with a
collision-safe append code and an internal resource return path whose reduced
Green law and tensor coupling follow without a prepared infinite bath. A
decisive negative would have to rule out infinite superselection, topological
or error-correcting archives, and nonlinear collision-safe QCAs. This cycle
does not do that.

## Assumptions Ledger

| ID | Layer | Assumption | Explicit/implicit | Why needed | What if wrong? | First test | Confidence |
|---|---|---|---|---|---|---|---|
| F1 | framework | current four axioms and three approved primitives | supplied | target ontology and symmetry | future constitutional text changes target | live source needles | high |
| Q1 | representation | 22 independent qubits per macrocell | explicit conditional enlargement | signal, marker/content, spent, and witness rails coexist | fundamental Qubit gives only one local `M2` | block-code search | low as framework realization |
| Q2 | dynamics | onsite commit swap plus export then directional shift | explicit conditional law | exact reversible event | another layer order gives another transcript | order ablation | high as construction |
| Q3 | preparation | one active event at a blank record | explicit state input | initiates the tested event | homogeneous law does not choose it | QB16 nucleation comparison | low as derivation |
| Q4 | boundary | all incoming rails are blank and have no inverse shell | implicit no-return sector, now explicit | local permanence and fresh witnesses | returning/colliding pulses erase or corrupt | torus and collision probes | high |
| Q5 | archive | marker/content and witness pairs are the readable record algebra | explicit decoder | distinguishes blank, record 0, record 1 | another relational code may survive collisions | CFSI-QB16 comparison | medium |
| Q6 | composition | macrocell qubits compose as a tensor product | explicit conditional representation | defines the unitary block | generated finite composition is not supplied by Qubit alone | composition theorem/bridge | medium |
| A1 | actuality | partial trace may be interpreted as one actual record | implicit claim attacked | would solve measurement | trace gives mixture, not branch selection | GHZ branch projectors | low/false in tested model |
| S1 | sufficiency | decoded equality records determine every future record | implicit claim attacked | framework state is records | hidden Bell phase changes a later recombination record | phase discriminator | low without superselection |
| R1 | renewal | infinite blank rails remain available | explicit initial boundary | indefinite writes | finite tape exhausts; positive-density waves collide | horizon and collision counts | low as derivation |
| T1 | time | one fixed QCA layer order is the physical tick | explicit law value | causal order | covariance does not select ordering of noncommuting gates | CNOT order pair | low as derived fact |
| G1 | resource | fresh polarized tapes implement source and sink collisions | explicit conditional state | unitary dilation of birth/death | polarization is fuel and depletes in finite volume | partial-iSWAP | high as construction |
| G2 | diffusion | direction information is traced into fresh rails | explicit reduction | Markov relaxation and Green fixed point | coherent reuse is ballistic/recurrent | `t` versus `t^2` variance | high |
| G3 | source | record activity prepares or modulates the resource tape | open bridge | connect records/mass to field current | amplitude remains free | paired current maps | open |
| C1 | coupling | one QCA tick implies one common matter scheduler | implicit claim attacked | equivalence/time lane | species phase coefficients remain independent | paired phase gates | low/false in tested model |
| C2 | transport | common onsite clock fixes edge transport | implicit claim attacked | trajectories/lensing | equal clock blocks admit different edge laws | paired Hamiltonians | low/false in tested model |

The most dangerous assumptions are Q4 and A1. “The tape is fresh forever” is
the arrow/past boundary in computational language. “The environment was
traced” is not one-history actuality.

## The Enlarged-Cell QCA

### Local coherent commit

For each signal value `s=0,1`, define orthogonal local states

```text
|i_s> = |S=s,A=1,M=0,R=0,B=vac>,
|o_s> = |S=s,A=0,M=1,R=s> (1/sqrt(6)) sum_d |B_d=1>.
```

Let `W` swap `|i_s>` and `|o_s>` for both `s` and act as identity on their
orthogonal complement. In the 14-dimensional subspace containing the two
input labels and twelve signal/direction spent labels,

```text
W = I + sum_s[-|i_s><i_s|-|o_s><o_s|
              +|i_s><o_s|+|o_s><i_s|].
```

The states are orthonormal, so `W=W*` and `W^2=I`. A proper cubic rotation
fixes `|i_s>` and permutes the six terms in `|o_s>`, leaving `W` invariant.
The runner constructs the matrix and checks all 24 rotations.

For a coherent signal,

```text
W (|i_0> + exp(i phi)|i_1>)/sqrt(2)
 = (|o_0> + exp(i phi)|o_1>)/sqrt(2).
```

The `S/R` relation is equality, while `phi` remains coherent global data.

### Relational witness export

For each direction `d`, apply the commuting reversible gates

```text
P_d <- P_d XOR M,
C_d <- C_d XOR (M AND R).
```

With fresh zero rails, the pair is `(P,C)=(1,R)`. Presence prevents record 0
from being confused with unwritten blank. Because all six directions receive
the same relation, the gate is proper-cubic invariant. It is an involutive
basis permutation, not a nonunitary copy.

Finally shift `B_d,P_d,C_d` from `x` to `x+d`. Each shift is a permutation of
the infinite tensor factors. Rotations act by `x->Rx,d->Rd`, so the whole
layer is covariant. The update order

```text
commit W -> relational export V -> rail shift
```

is part of the candidate law, not derived from covariance.

### Isolated no-return sector

After `t` ticks, the spent pulse is

```text
|B(t)> = (1/sqrt(6)) sum_d |rail d, position t d>.
```

Its norm is one, its support is a proper-cubic orbit, and on `Z3` no component
returns to the source for `t>0`. Meanwhile the source emits relational witness
pairs at positions `k d`, for `k=1,...,t`. The marker/content controls are not
changed by export, so the local record is stable in this sector.

This is the precise positive construction. “Ever fresh” means the incoming
rail states in this sector are blank. It is not a consequence of the unitary.

## The Finite Reversible Permanence Boundary

Let `H_R` be a finite-dimensional record subspace and `U` a unitary. Absolute
forward permanence says

```text
U H_R subset H_R.
```

Because `U` is injective and `H_R` is finite dimensional,
`dim(U H_R)=dim(H_R)`, hence `U H_R=H_R`. The record subspace is therefore
reducing: `U` also maps its orthogonal complement to itself. No blank state in
that complement can form a record.

The runner exhausts all 24 permutations of a four-state carrier with two
blank and two record states. Every permutation that preserves the record set
has zero blank-to-record transitions.

This is not an infinite-dimensional no-go. On `ell2(Z)`, the bilateral shift

```text
U|n> = |n+1>
```

is reversible. The subspace spanned by `n>=0` is forward invariant, and
`|-1>` enters it. Infinite dimension permits a proper invariant subspace with
the same Hilbert dimension. The outgoing QCA rails exploit exactly this room.

### Why the current construction is not absolutely permanent

On a periodic side-`L` lattice, every spent component returns to the source
after `L` rail shifts, reconstructing `|o_s>`. At the next commit layer, the
same `W` maps it back to `|i_s>`: the record is erased and the active event
returns. On infinite `Z3`, six spent components launched by other sources can
be arranged to converge on the same record and do the same thing.

Therefore the construction proves local stability only when the history
excludes inverse precursors. Absolute Record permanence would require one of:

1. fundamental nonunitary append;
2. a derived infinite superselection/no-return sector;
3. a collision-safe topological or error-correcting archive; or
4. an explicit law-domain restriction declaring inverse histories physically
   inadmissible.

The last option is not free. Under the current law qualification, the domain
is supplied content and must be named.

## Collision Countermodel

Suppose an upstream record has already put `(P,C)=(1,r_up)` on a rail. At a
downstream record with content `r_local`, the same reversible export gate gives

```text
P' = 1 XOR 1 = 0,
C' = r_up XOR r_local.
```

The presence certificate disappears. This happens for either record value.
The six fixed rails therefore do not implement append-only witness traffic for
arbitrary positive-density records.

The `CFSI-QB16` sibling avoids false logical hybrids for separated finite
packets with their own relational references. That is complementary, not a
repair of this transport collision. QB16 explicitly leaves physical
cross-site reference transport and nearest-neighbor compilation open. A
collision-safe QCA would need packet addressing, dynamically allocated lanes,
hard-core spacetime separation, solitonic scattering, or an error-correcting
code. Each route adds structure beyond the 22-qubit isolated-event block.

## One-History Actuality Does Not Follow

After copying the content to six witnesses, the two phase variants are

```text
|Psi_+> = (|0,0,0...0> + |1,1,1...1>)/sqrt(2),
|Psi_-> = (|0,0,0...0> - |1,1,1...1>)/sqrt(2).
```

They are orthogonal pure global states. Their local `S/R` record density is
identical:

```text
rho_SR = (|00><00|+|11><11|)/2.
```

The equality decoder accepts both with probability one. Both branch
projectors still have weight `1/2`; no branch has been selected. Partial trace
explains why the other phase is locally inaccessible in the isolated forward
sector. It does not explain why one record is actual.

The unitary therefore produces observer-independent **correlations**, not an
observer-independent one-history record. Conditional on either branch, an
observer reads a consistent branch-relative record. The realized-state
primitive allows pointwise evaluation after an actual history is supplied. It
does not turn either component into that supplied history or assign its
weight.

## Record-Only Future Sufficiency Does Not Follow

Apply the standard Bell recombination

```text
CNOT(S->R), then H(S).
```

It maps

```text
Phi_+ -> |00>,
Phi_- -> |10>.
```

A later record of `S` distinguishes the two phases exactly. Thus the same
prior equality record packet has two possible phase-sensitive futures.

There is a narrow escape: declare that after commit no law-admissible operation
can ever recombine the rails or couple to the hidden phase. Then the readable
record algebra may be sufficient for its own future. But that is a
superselection/no-return theorem or new law clause, not a consequence of the
record decoder. It must also coexist with the framework's Bell-capable physics
before commit.

QB16's conjugation and complement invariance is not contradicted. It proves
that its logical **classical packet** is relational and basis-neutral. It does
not claim that the packet is a complete pure quantum state or that every
coherent phase is a record.

## Renewal Is a Boundary Resource

The QCA is homogeneous; its useful state is not. All local irreversibility has
been relocated into the blank-tape/no-return boundary plus the observer's
partial trace. The isolated construction
needs:

- one active event at a blank site;
- blank incoming witness rails;
- no converging spent shell;
- enough unused capacity for every later witness; and
- for resource current, occupied source tape and empty sink tape.

A finite tape of length `T` supports at most `T` independent fresh collisions
before reuse. Reuse returns information and permits recoherence. An infinite
tape makes every finite future window look renewed, but only because a
low-record boundary extends arbitrarily far away.

The assumptions sibling offers a positive homogeneous initiation law via
positive-density stochastic local minima. That removes an absolute spatial
origin, but it explicitly imports IID marks, activity, an all-open layer, and
an actual sample; its packets are hard-core separated only in one finite
layer. Feeding that positive-density output into fixed infinite rails creates
the collision problem above. Nucleation and renewal are separate.

## Causal Schedule Covariance Does Not Follow

Two local reversible gates on three bits give a minimal countermodel. Starting
from `100`,

```text
CNOT(1->2) then CNOT(2->3)  gives 111,
CNOT(2->3) then CNOT(1->2)  gives 110.
```

Locality, reversibility, and covariance do not make noncommuting schedules
equivalent. Commuting `CZ` edge gates are a positive control: their order does
not matter and they create phase entanglement, but they do not implement the
commit/export latch by themselves.

Even the exact QCA here gives different first-tick witnesses if export occurs
before rather than after commit. Its layer order is a substantive law value.
A multiway/causal-invariance theorem would have to prove schedule equivalence;
none follows from Admissibility.

## Resource/Green Integration

There is a clean unitary collision model for the source and sink interfaces.
Let a system resource qubit collide with a tape qubit through the
number-conserving partial `iSWAP` rotation

```text
|01> -> cos(theta)|01> + sin(theta)|10>,
|10> ->-sin(theta)|01> + cos(theta)|10>.
```

For diagonal uncorrelated occupations `n` and `p`, tracing the outgoing tape
gives

```text
n' = cos(theta)^2 n + sin(theta)^2 p.
```

An occupied incoming tape (`p=1`) is a source; an empty tape (`p=0`) is a sink.
The joint unitary conserves total occupation exactly. If all tapes are included
in the universe, no token disappears into an external sink.

But the source/sink polarization is fuel. Each collision leaves a hole in the
source tape or a particle in the sink tape. Reusing the same tape qubit gives
coherent oscillation, not another identical reservoir step. An infinite train
of occupied/empty inputs sustains a local reduced current only because that
nonequilibrium boundary was prepared.

Likewise, the exact cubic lazy step

```text
P=I-L/12
```

has the one-step unitary dilation from Cycle 10. Reusing its direction coin is
ballistic,

```text
E[r^2]=t^2/2,
```

while fresh traced directions are diffusive,

```text
E[r^2]=t/2.
```

The local Poisson/Green fixed point is exact for the reduced fresh-information
law. The enlarged full QCA can contain the outgoing tapes and remain globally
unitary, so an “external sink” is unnecessary in a literal bookkeeping sense.
What remains supplied is more important: an infinite polarization/blankness
gradient, direction dephasing, and the record-to-current bridge. A finite
closed return loop equilibrates or recurs unless it carries a nonequilibrium
affinity or an unbounded work register.

Thus the infinite QCA integrates the **dilation** of the resource mechanism,
not a zero-input derivation of the Green source.

## Common Clock and Transport Do Not Follow

One QCA layer gives one causal tick in the candidate law. It does not force
every internal species to accumulate the same phase or couple identically to
the resource field. In one shared tick, both

```text
U_s(phi)=diag[1,exp(-i theta(1-gamma_s phi))]
```

are local unitaries for arbitrary `gamma_s`. Choosing different `gamma_s`
breaks universal redshift without changing the record/export QCA.

Even imposing identical onsite clock blocks leaves edge transport open. The
runner repeats the paired constant-edge versus `sqrt(q_x q_y)`-weighted edge
Hamiltonians: onsite clock gaps agree, spectra and transfer amplitudes differ.
Therefore neither a QCA tick nor a record-formation rate derives the common
scheduler, equivalence principle, spatial metric, or lensing.

## What Actually Integrated

| Requirement | Exact result | Remaining price |
|---|---|---|
| coherent Bell-capable local interaction | yes, local commit swap | active event and enlarged macrocell |
| translation/proper-cubic covariance | yes, macrocell law | no one-qubit fundamental block code |
| outward inverse-information export | yes, six spent rails | isolated no-return sector |
| stable relational decoder | yes for one isolated event | collisions and inverse precursors |
| one-history actuality | no | selector/primitive commit remains |
| record-only future sufficiency | no for Bell-capable continuations | superselection/no-return theorem |
| indefinite renewal | conditional on infinite blank tape | past boundary/capacity supply |
| causal schedule covariance | no | fixed ordering or confluence theorem |
| no external token sink | yes if infinite tapes are counted | polarized tape is fuel |
| stationary Green response | yes only after fresh/traced reduction | dephasing, affinity, source map |
| common clock/transport coupling | no | separate physical law |

## N1 — Alternative Routes

The negative boundaries were tested against these distinct routes:

1. fundamental irreversible append — directly escapes every reversible
   permanence obstruction, at the cost of new primitive dynamics;
2. finite unitary plus finite ancilla — closes one event, fails indefinite
   permanence/mixing by recurrence;
3. infinite bilateral shift/fresh tape — positive mathematical escape and the
   basis of this construction;
4. enlarged-cell symmetric spent shell — positive isolated-event QCA here;
5. relational CFSI-QB16 packet — positive basis-neutral decoder, with transport
   and compilation open;
6. positive-density stochastic nucleation — removes absolute spatial seed,
   imports measure/activity and creates rail collisions;
7. topological/error-correcting archive — live untested route for collision
   resistance;
8. algebraic superselection/disjoint thermodynamic sectors — live route for
   phase inaccessibility and no return;
9. global/two-boundary consistency law — could select only histories without
   inverse precursors, but is outside the tested local initial-value law;
10. collision-model resource tapes — positive unitary source/sink dilation,
    imports polarization/freshness;
11. coherent deterministic lattice gas — supports current, remains ballistic
    rather than Green-relaxing; and
12. commuting-gate causal circuit — schedule independent, does not supply
    append-only actualization.

## N2 — Wall-Independence Audit

| Wall | Independent countermodel |
|---|---|
| fundamental carrier | the 22-qubit macrocell QCA works algebraically while lacking a one-qubit block code |
| permanence | isolated infinite rails preserve a record while actuality remains absent |
| actuality | GHZ branches remain two even when local record is stable |
| record sufficiency | opposite phases share records but later recombine differently |
| renewal | infinite blank tape renews without selecting a branch |
| schedule | commuting CZ closes ordering without forming a record |
| Green relaxation | fresh traced coin diffuses while coherent coin is unitary and ballistic |
| common coupling | same global tick permits different species coefficients |

None may be counted as another name for “formation.”

## N3 — Hidden-Wall Scan

The scan exposes:

- macrocell tensor composition and 22-qubit carrier;
- an active-event initial state;
- infinite blank and polarized tapes;
- an isolated/no-inverse history sector;
- a chosen commit/export/shift layer order;
- partial trace as the reduced observer map;
- the readable marker/content decoder;
- hard-core separation or collision routing;
- source and sink state preparation;
- mass/record-to-resource current identification;
- direction dephasing;
- common matter coupling;
- tensor/spatial gravity; and
- no proof that all permitted histories obey the no-return restriction.

## N4 — Residual Matching

The finite-subspace theorem addresses only reversible formation plus absolute
permanence in finite carrier dimension. It does not address infinite proper
invariant sectors. The torus and converging-shell probes address the exact
candidate QCA's no-return residual. The GHZ probe addresses actuality, not
decoder correctness. The Bell recombination addresses future sufficiency, not
formation. The collision tapes address token conservation, not the origin of
polarization. The paired phase/transport laws address common coupling, not the
clock's existence.

## N5 — Rhetoric and Resolution

Safe resolution qualifiers are:

- finite carrier versus infinite tensor product;
- one isolated event versus arbitrary positive-density history;
- local record algebra versus full coherent state;
- one-step/reduced Markov channel versus all-time global unitary;
- scalar resource field versus tensor gravity; and
- law covariance versus schedule covariance.

Rejected overstatements include “unitarity cannot form records,” “infinity
solves measurement,” “decoherence selects a branch,” “fresh tape is free,”
“QCA time forces equivalence,” and “closed token bookkeeping derives gravity.”

## N6 — Partial-Closure Paths

No axiom edit is made. The positive QCA can remain a conditional construction.
The next cheapest closures are:

1. search a one-qubit proper-cubic Clifford/non-Clifford QCA for a relational
   no-return code;
2. replace fixed rails with collision-safe solitons or a local error-correcting
   archive;
3. prove an infinite-sector superselection theorem making inverse precursors
   law-inadmissible rather than merely absent initially;
4. compile QB16 reference transport and atomic write into nearest-neighbor
   gates; and
5. connect outgoing information flux to the closed `D/C` resource cycle, then
   test whether its affinity is state-derived or still supplied.

Existing approved primitives supply none of these steps.

## N7 — Steelman

The strongest surviving model is an infinite algebraic QCA, not a finite block
simulation. Records are encoded in disjoint asymptotic sectors of a quasi-local
operator algebra. Local commit sends inverse information into outgoing
topological/solitonic excitations. Lieb-Robinson locality prevents their return
inside any finite future cone, while a conserved return sector carries
resource current. Relational error correction makes local records insensitive
to ordinary collisions. Actuality is a boundary condition selecting one
sector, and the law never permits coherent inter-sector recombination.

Such a model could evade finite recurrence, fixed-rail collisions, and local
phase recombination simultaneously. This note has not built or ruled it out.
It would still need to conform to one `M2` per site, derive or openly state the
sector boundary and branch weights, and produce tensor gravity rather than a
scalar scheduler alone.

## N8 — Cross-Cycle Echo

- The assumptions slice showed that homogeneous positive-density nucleation
  can avoid a privileged origin but must supply occurrence measure, activity,
  actual sample, and an initial layer.
- CFSI-QB16 repaired the relational classical packet and exposed cross-site
  transport and nearest-neighbor compilation.
- Cycle 10 showed one-step unitary dilation, all-time fresh-information cost,
  closed Markov current with supplied affinity, archive saturation, and the
  scalar/tensor split.
- This cycle unifies those positive pieces on one enlarged infinite QCA for an
  isolated event. It then finds the same independent costs in sharper form:
  inverse-shell return, rail collision, phase actuality, tape boundary,
  schedule order, polarization fuel, and species coupling.

The infinite route remains open, but it did not make the law clauses disappear.
It moved them into the choice of physical sector and asymptotic boundary.

## Consequence for Bare-Metal and Axiom Language

This cycle makes the constitutional fork cleaner.

If formation is fundamentally irreversible, say so at the Record/formation
boundary and do not disguise the new physics as ordinary “reading” or as a
clock label. That route naturally supports absolute permanence and one actual
history, but still needs a branch/occurrence law.

If the fundamental law is reversible, a viable formation statement cannot end
at “two witnesses” or “the clock locks it.” It must be backed by a theorem that
the committed relation lies in an infinite no-return/superselection sector,
that inverse information is carried away locally, and that collisions cannot
revoke the record. Otherwise permanence is only an initial-state convention.

The minimum semantic distinction any final wording must preserve is:

```text
event eligibility
    != event occurrence
    != branch/content selection
    != reversible correlation/export
    != one-history actuality
    != permanent public record.
```

The current exact QCA closes reversible correlation/export for one isolated
event. It does not close the other five equalities. That is why no verbatim
axiom addition is recommended from this cycle alone.
