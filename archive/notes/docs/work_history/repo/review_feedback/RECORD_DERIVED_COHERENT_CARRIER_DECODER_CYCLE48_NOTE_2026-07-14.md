# Record-Derived Coherent Carrier Decoder — Cycle 48

**Date:** 2026-07-14

**Type:** authority-free exact finite-class construction, reference-extension
test, adaptive-record replay theorem, arbitrary-state boundary, and fresh
N1–N8 gate

**Authority: none.** This note is not an axiom, primitive, framework law,
retained theorem, audit verdict, or authorization to alter a foundation or
registry surface. It makes no commit, push, or PR.

**No live foundation edit is authorized.**

Companion runner:

```text
scripts/record_derived_coherent_carrier_decoder_cycle48_2026_07_14.py
```

## Result Up Front

The construction result is **conditional positive**.

A finite but nontrivial version of Cycle 44's record/decoder exit closes
exactly. The preparation dictionary contains **all 60 pure two-qubit
stabilizer states** of a reference qubit `R` and a transported carrier qubit
`C`: 36 product states and **24 reference-entangled** states. Six permanent
binary preparation records select one entry. Later permanent records carry
the full gate, Pauli-instrument outcome, teleportation syndrome, correction,
and causal lineage. A fixed decoder replays those records into the unique
current `RC` density operator.

For the declared protocol class—two-qubit Clifford gates, the 15 explicitly
declared nonidentity two-qubit Pauli **Born–Lüders instruments**, corrected
carrier teleportation, and arbitrary finite adaptive compositions whose
choices are functions of earlier records—the following statement is exact:

> **Identical complete records imply identical future record statistics.**

The proof is stronger than a lookup-table coincidence. The 60-state class is
closed under every declared unitary and every nonzero instrument branch;
teleporting `C` preserves the joint `RC` state in every recorded syndrome
branch; and induction on an adaptive protocol reconstructs one state after
every finite transcript. Thus the complete permanent record configuration is
a sufficient predictive state for this carrier class. **Qualification remains
unchanged for this declared class.** No additional ontic carrier variable is
needed at the law-evaluation surface.

The result is deliberately finite. **Arbitrary unknown states escape** this
decoder. The product state `|0>_R |T>_C`, with
`|T>=(|0>+exp(i pi/4)|1>)/sqrt(2)`, is outside the 60-state dictionary and has

```text
Pr(X_C=+1) = (1 + 1/sqrt(2))/2,
```

which is not one of the stabilizer probabilities `0, 1/2, 1`. General
non-Clifford operations and unbounded reference systems are likewise outside
the declared closure. This is an escape from this construction, not a proof
that no larger record-derived construction exists.

The exact consequence for Cycle 44 is narrow and useful. Its predictive-state
wall `W_S` is closed for a genuinely quantum, phase-sensitive,
reference-entangled preparation class. The clean-resource wall and collision
wall are untouched. The cycle therefore supplies a tested constitutional
option—record-derived coherent state—without selecting axiom language. **No
axiom wording follows.**

## 1. Scope And Foundation Typing

The current Qualification says `A state is a configuration of records`.
Cycle 44 showed why a readable but unrecorded coherent carrier fails that
typing: two identical record configurations could yield different later read
probabilities. It also named the constructive exit used here: permanent
preparation and lineage records plus a complete decoder.

This cycle does not infer a wavefunction from a bare outcome record. It adds a
fully declared candidate-law sector with four ingredients:

1. a finite preparation dictionary;
2. a physical record code for dictionary entries and later events;
3. a declared operational grammar; and
4. one deterministic replay decoder fixed with that grammar.

Those ingredients are candidate-law content, not content silently borrowed
from the four axioms. The approved realized-state primitive supplies only
pointwise evaluation at a history-fixed state; it does not supply a state,
preparation, probability rule, or decoder. The scale-reference and
kinetic-isotropy primitives are irrelevant to this dimensionless finite
construction. The primitive-registry scopes are therefore respected and no
primitive is treated as a missing premise or as a source of bounded status.

The protocol is quantum-operational mathematics used to test the record-state
interface. It does not derive Born weighting, autonomous preparation,
formation rate, clock rate, mass, charge, gravity, clean resource generation,
or collision dynamics.

## 2. The Complete Recorded Preparation Class

Let `P_2` be the 15 nonidentity two-qubit Pauli operators. A pure two-qubit
stabilizer state is the rank-one projector

```text
rho(g,h;s,t) = (I + s g)(I + t h)/4,
```

where `g,h in P_2` are independent and commute and `s,t in {+1,-1}`. Removing
duplicate generator descriptions leaves exactly 60 projectors. The runner
constructs rather than imports this census and verifies:

```text
60 total = 36 product + 24 reference-entangled.
```

The entangled cases matter. A decoder tested only on the six single-qubit
Pauli eigenstates could hide failure under extension by a reference. Here the
reference is carried explicitly, and later operations can probe joint Pauli
correlations.

### Permanent code

Index the 60 projectors by `j=0,...,59`. Six permanent binary records contain
the ordinary six-bit word for `j`; words `60,...,63` are invalid. One bit per
site respects the one-`M_2(C)` site presentation: two fixed record contents
stand for `0` and `1`, while the spatial/causal arrangement supplies ordering.
The candidate law contains the public dictionary `j -> rho_j`.

These records do not copy an unknown wavefunction. They record which public
preparation program ran. The state is generated from the program and is then
recoverable from the permanent program record. This distinction is why the
finite construction survives the no-cloning overlap test.

For later events, the complete transcript stores, either explicitly or by a
fixed spatial role code,

```text
(teleport syndrome bit 1,
 teleport syndrome bit 2,
 Clifford generator id,
 Pauli instrument id,
 outcome bit).
```

Causal position links the tuples into an ordered lineage. An economical
autonomous implementation can derive the gate and instrument ids from the
earlier record prefix; keeping them in the abstract transcript makes the
replay claim insensitive to that compression.

## 3. Declared Legal Protocol Grammar

The exact legal generators are:

```text
Clifford gates:
H_R, H_C, S_R, S_C, CNOT_(R->C), CNOT_(C->R), SWAP_(R,C)

record instruments, supplied by the candidate law:
for every nonidentity P in P_2 and s in {+1,-1},
Pi_s=(I+sP)/2, p_s=Tr(Pi_s rho), and, when p_s>0,
rho_s=Pi_s rho Pi_s/p_s

transport primitive:
standard Bell teleportation of C, two recorded syndrome bits,
and their deterministic Pauli correction

composition:
any finite adaptive tree whose next legal generator is a fixed
function of the complete earlier permanent transcript.
```

This is a nontrivial readable-matter sector. It includes interference basis
changes, entanglement creation/removal, joint parity reads, incompatible
measurement contexts, recorded corrections, and adaptive syndrome lineage.
It is not universal quantum computation because no non-Clifford resource is
included.

The displayed probability and state-update formulas are load-bearing
candidate-law content. A two-qubit Pauli effect is degenerate and does not by
itself select the Lüders state update; another instrument with the same effect
can leave the stabilizer class. This cycle neither derives the Born weights
nor claims closure for every instrument implementing the same Pauli effects.

## 4. Exact Closure Lemmas

### Lemma 1 — Clifford closure

Conjugation by a Clifford gate permutes signed Pauli operators. It therefore
maps two independent commuting stabilizer generators to two independent
commuting generators, so every `rho_j` maps to one of the same 60 projectors.
The runner checks all `60 x 7 = 420` generator images directly.

### Lemma 2 — Born–Lüders Pauli-instrument closure

For a pure stabilizer state, the declared Born–Lüders Pauli instrument has
probability `0`, `1/2`, or `1`. A nonzero Lüders branch is again a pure
stabilizer state: a deterministic Pauli is already fixed by the stabilizer,
while a nondeterministic Pauli replaces one anticommuting generator. The runner
checks all `60 x 15 x 2 = 1800` signed branches, their normalization, and the
exact post-state dictionary index.

### Lemma 3 — Reference-safe recorded teleportation

Let `K_ab` be the uncorrected teleportation Kraus map for syndrome
`a,b in {0,1}` and let `U_ab` be its recorded Pauli correction. Up to an
irrelevant branch phase,

```text
U_ab K_ab = I_C/2,
K_ab^* K_ab = I_C/4.
```

Consequently, for every joint state in the dictionary,

```text
(I_R tensor U_ab K_ab) rho_RC
(I_R tensor U_ab K_ab)^*
    = rho_RC/4.
```

Every syndrome has probability `1/4`, and normalization restores exactly
`rho_RC`. The runner checks every one of the 60 states in every branch. The 24
entangled states are a concrete complete-positivity/reference test rather than
an appeal to carrier marginals alone. Before correction, deleting a syndrome
bit leaves different Pauli frames, so the lineage record is load-bearing.

## 5. Complete-Record Replay Theorem

Define a decoder `D` on a complete legal record configuration as follows.

1. Decode the six preparation bits. Invalid words are outside the law domain.
2. Set the working state to the corresponding `rho_j`.
3. Read the event records in causal order.
4. Apply the recorded Clifford table entry.
5. Use the recorded Pauli outcome to select the unique nonzero branch.
6. Use each recorded teleport syndrome to apply its fixed correction.
7. Return the final joint carrier/reference projector.

### Theorem

For every finite legal transcript `r`, `D(r)` exists and is unique. For every
legal finite adaptive continuation `Q`, the probability distribution of all
future record strings is a function only of `r`. Therefore identical complete
records imply identical future record statistics.

### Proof

The preparation record gives one unique base state. Lemmas 1–3 say that each
nonzero legal event has one unique next dictionary state, and its branch
probability is fixed by the current dictionary state and event label. Induct
over the transcript length to obtain a unique replayed state after every
prefix.

Now induct over the depth of a future adaptive tree. At a node, the next
operation is a fixed function of the shared record prefix. Equal prefixes
therefore choose the same operation. Equal decoder states give the same branch
probabilities and equal successor decoder states. The distributions on all
finite descendant record strings agree. This proves the claim for arbitrary
finite depth, not merely for one next Pauli read. `QED`.

The runner supplements the proof with all 60 preparations, two rounds of
syndrome-dependent adaptive gate and measurement selection, exact rational
tree normalization, full transcript replay, and every future Pauli signature.

### Why each record component matters

- Removing the preparation word merges multiple states with different Pauli
  futures.
- Removing a measurement outcome merges distinct conditional states.
- Removing a teleport syndrome before correction loses the Pauli frame.
- Removing causal order can change noncommuting operation composition.
- Omitting an adaptively chosen operation label is safe only if the fixed law
  recomputes it uniquely from the retained prefix.

Thus “complete” is a physical sufficiency requirement, not a claim that every
verbose transcript field must occupy its own site.

## 6. Exact Boundary: Where Arbitrary States Escape

The decoder domain is finite and declared. It has no entry for the carrier
magic state `|T>`. The runner checks the exact separating statistic

```text
Pr(X_C=+1 | |0>_R|T>_C) = (1+1/sqrt(2))/2,
```

so that state cannot be silently identified with a stabilizer dictionary
entry. A `T` gate likewise takes a legal stabilizer input outside the class.

This establishes only the following narrow boundary:

> Six binary preparation records plus the declared 60-entry decoder do not
> represent an arbitrary unknown nonstabilizer `RC` state.

It does not establish that finite regions of `M_2(C)` record contents cannot
encode a continuum, that a growing record corpus cannot approximate or
identify larger classes, or that a universal law cannot generate all physical
preparations from records. A single `M_2(C)` record content itself has a
continuous projector space, and a different candidate could exploit that
structure if it gives an exact physical decoder and record-writing law.

Direct copying is a separate route. If an unknown state is preserved while an
exact second state record is written, inner products would have to satisfy
`<psi|phi> = <psi|phi>^2`. The runner checks the `|0>,|+>` separator. That
excludes exact universal copying, not recorded generation from known programs,
tomographic estimation, approximate coding, or an ontology change.

## 7. Consequence For Cycle 44 And The TOE Lanes

Cycle 44's readable-carrier fork asked for either a record-derived decoder or
a Qualification revision. This cycle constructs the first route at exact
finite scope:

```text
permanent preparation record
  + permanent program/syndrome/outcome lineage
  + fixed decoder
  -> current coherent carrier/reference state
  -> every future legal record statistic.
```

That suffices to make phase-sensitive and entanglement-sensitive matter
readable without adding hidden state for this class. It does not solve:

- the clean `|+>`/Bell-resource factory needed by repeated transport;
- reversible two-input collision/routing;
- autonomous formation of the first preparation records;
- selection of Born weights from the axioms;
- unbounded error correction or universal quantum computation;
- matter interpretation, mass, charge, clock rate, or gravity.

The right constitutional lesson is therefore not “add stabilizers to the
axioms.” It is that record-only state can support coherent readable matter if
a final law makes preparation and every state-changing lineage
record-complete. That is a law-completeness target. Whether a broader exact
law achieves it for the physically required state repertoire remains an open
science task.

## 8. Fresh No-Go Discipline Gate

The positive theorem is exact. The negative claim is only that this particular
finite decoder does not cover arbitrary unknown states. The following fresh
N1–N8 gate prevents that boundary from being inflated into a universal no-go.

### N1 — Alternative Route Enumeration

| route | marker | attack and result |
|---|---|---|
| six single-qubit Pauli eigenstates | **ATTEMPTED** | A six-state dictionary closes ordinary Clifford/Pauli replay but is too weak because it contains no reference-entangled preparation. |
| all 60 two-qubit stabilizer states | **ATTEMPTED** | This succeeds exactly and defeats any claim that coherent record-derived decoding already fails for all quantum states. |
| entangled Bell subset and reference extension | **ATTEMPTED** | All 24 entangled stabilizer states survive every corrected teleport branch, so a carrier-only marginal obstruction fails. |
| full two-qubit Clifford closure | **ATTEMPTED** | All 420 generator images remain in the dictionary; phase-sensitive reversible processing does not force an ontic-state revision here. |
| all 15 declared Born–Lüders Pauli instruments with adaptive choice | **ATTEMPTED** | All 1800 signed branches close, and two-round record-conditioned trees replay and normalize exactly. Other instruments with the same degenerate effects are outside the claim. |
| recorded teleport-syndrome lineage | **ATTEMPTED** | This succeeds after correction and proves the syndrome bits can be permanent causal records rather than hidden frame data. |
| add one magic preparation or `T` gate | **ATTEMPTED** | The displayed `|T>` probability exits the 60-state transition table; this route is open as a larger decoder rather than ruled impossible. |
| exact copying of an arbitrary preserved unknown carrier | **ATTEMPTED** | This runner repeats the `|0>,|+>` inner-product control: universal exact copy-and-preserve fails, while recorded generation and encoded decoders remain live. |
| continuum-valued record contents | **ATTEMPTED** | This is a credible escape from the finite-bit boundary; no exact autonomous decoder was supplied in this cycle, so it remains live. |

There are more than five genuinely distinct routes. Because several broader
routes remain live, the universal no-go fails and the boundary is narrowed.

### N2 — Wall-Independence Audit

The raw escape list collapses to three scope axes for extending this decoder:

- `W_P`: preparation closure beyond the fixed two-qubit stabilizer dictionary,
  exemplified by a magic-state preparation in the same `RC` space;
- `W_O`: operation closure beyond Clifford gates and the declared
  Born–Lüders Pauli instruments on the already recorded stabilizer class;
- `W_R`: scalable reference closure—arbitrarily many record-derived
  stabilizer reference/carrier qubits with a size-uniform decoder.

These are not Cycle 44's clean-resource and collision walls; those remain
separate downstream tasks. Pairwise collapse audit:

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| `W_P/W_O` | no: adding magic preparations does not provide non-Clifford transition tables | no: adding an operation does not encode every new preparation | yes |
| `W_P/W_R` | no: closing fixed-size magic preparation does not prove a uniform unbounded-reference decoder | no: scalable stabilizer decoding does not include magic states | yes |
| `W_O/W_R` | no: a fixed-size universal operation set does not prove scalable reference coding | no: scalable Clifford/stabilizer reference closure does not add non-Clifford operations | yes |

No pair collapses. Importantly, “arbitrary reference correlation” is not
counted as a fourth wall: at fixed size it belongs to `W_P`; at growing size
it belongs to `W_R`.

### N3 — Hidden-Wall Scan

| scanned phrase | result/classification |
|---|---|
| “we assume” | absent; all legal operations and dictionary choices are declared candidate-law scope |
| “by construction” | absent as a proof substitute; closure is proved algebraically and exhaustively checked |
| “as is standard” / “naturally” / “obviously” | absent |
| “the framework provides” / “bridge context” / “background” / “standard QFT” | absent |
| “registered” / “canonical” | registry language refers only to the cited approved primitive registry; it supplies no decoder content |

The probability rule and instruments are not hidden. They are part of the
declared test grammar, and the note makes no derivation-from-axioms claim for
them. No hidden condition changes the three-axis count.

### N4 — Residual Matching

| cited witness | witness residual | present residual | match? |
|---|---|---|---:|
| `PROTECTED_MATTER_TRANSPORT_CYCLE44_NOTE_2026-07-14.md:73-82` | readable hidden carrier requires record/decoder or Qualification revision | construct exact record/decoder for a controlled family | yes |
| `PROTECTED_MATTER_TRANSPORT_CYCLE44_NOTE_2026-07-14.md:320-378` | syndrome records alone do not derive an arbitrary carrier; recorded preparations remain live | preparation plus complete event lineage derives the finite carrier | yes |
| `RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md:390-400` | record-derived decoder is an honest way to avoid hidden predictive state | exact finite decoder and replay theorem | yes |
| `RECORD_STATE_PHASE_SUFFICIENCY_CONSTRUCTIVE_PROBE_NOTE_2026-07-13.md:83-100` | distinct operational preparations require persistent separation and sufficient continuation records | six-bit preparation separation plus complete lineage | yes |
| `COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md:585-586` | program/outcome corpus can make future laws functions of records on its domain | same record-fibre criterion extended to a coherent finite class | yes, criterion only |

No citation is used as evidence that arbitrary decoding is impossible. Each
citation matches the record-sufficiency residual for which it is invoked.

### N5 — Rhetoric Audit

The narrow negative is checked at these resolutions:

| resolution | tested statement | result |
|---|---|---|
| one carrier with product reference | `|0>|T>` is outside the finite dictionary and has a non-table probability | exact pass |
| one carrier entangled with one reference | all 24 stabilizer-entangled states are inside and teleport exactly | exact positive; no negative claim |
| one two-round adaptive block | complete record replay remains sufficient | exact positive |
| arbitrary finite adaptive depth | follows by the transcript/tree induction for the declared generators | proof-level positive |
| arbitrary nonstabilizer reference state | not exhaustively tested | open under `W_P`, so no universal phrase is used |
| unbounded lattice/reference size | not tested | open under `W_R` |

Accordingly, the note says “the six-bit 60-entry decoder does not represent an
arbitrary unknown state,” not “record state cannot represent arbitrary quantum
matter.” The no-cloning statement is restricted to exact copy-and-preserve of
an unknown state.

### N6 — Partial-Closure Path Scan

| path | status here | what it could close |
|---|---|---|
| add recorded magic-state programs and Clifford+T transition rules | live next construction | part of `W_P` and `W_O`; potentially universal finite-circuit preparations |
| use continuous `M_2(C)` record contents with an exact decoder | live | continuum preparation labels without a Qualification edit |
| grow a tomography corpus with error/confidence records | live but approximate/statistical | operational estimation, not exact single-history state copying |
| encode stabilizer/QEC blocks with every syndrome record-visible | live | `W_R` and fault-tolerant lineage for a restricted noise model |
| prove operational quotient sufficiency instead of density-state equality | live reframe | could retire unnecessary ontic distinctions without new physics |
| explicitly widen Qualification to open ontic carriers | owner-governed constitutional fork | bypasses decoder sufficiency but changes state ontology |

The approved realized-state primitive does not close these paths because it
supplies a pointwise evaluation slot, never the contingent state or decoder.
None of the live decoder-expansion paths is automatically a new axiom; each can
be tested first as explicit candidate-law content and an import-retirement
derivation route.

### N7 — Hostile Steelman

**Hostile reviewer:** “Your escape example only defeats a deliberately tiny
six-bit code. The physical record alphabet is not binary in the foundation:
one `M_2(C)` record can carry a continuum of rank-one contents, and a growing
append-only corpus can encode arbitrary finite preparation circuits to
arbitrary precision. Clifford circuits plus recorded magic-state injections
already offer a concrete route from your exact stabilizer theorem toward a
universal decoder. Because your induction depends only on closure and a public
transition table, not on stabilizers specifically, any larger record-generated
closed class inherits the same proof. You have therefore demonstrated the
architecture of the escape from your own boundary, not a universal obstruction
to record-derived quantum matter.”

That steelman is convincing against a broad negative. The honest disposition
is:

```text
broad no-go: FAIL
status: partial-narrowing
narrow boundary: PASS
```

The narrow boundary is only the failure of the fixed 60-entry/six-bit decoder
outside its declared class. Universal record-derived state remains live.

### N8 — Cross-Cycle Echo

| prior surface | similar wall | later/available retirement mechanism |
|---|---|---|
| Cycle 26 one-`M_2` fortress | hidden coherent state fails unless fibre-constant or record-derived | this cycle instantiates its record-decoder escape exactly |
| July-13 phase-sufficiency probe | phase-sensitive preparations need persistent reference records | the six-bit preparation corpus separates all 60 finite-class states |
| Cycle 41 complete candidate | record-fibre sufficiency required for transient coherent workspace | deterministic replay supplies it at the declared carrier scope |
| Cycle 44 protected transport | readable carrier creates decoder/Qualification fork | this cycle closes the decoder branch finitely; ontology revision stays optional |
| Cycle 44 no-cloning separator | direct copying fails but generated/encoded families stay live | recorded program generation is precisely the mechanism used here |

The echo changes the conclusion: earlier negative fibres were retired by
adding persistent program records and a decoder, so the same mechanism must
remain live for larger state classes. The broad no-go is not shipped.

## 9. Reproduction And Bounded Disposition

Run:

```bash
python3 scripts/record_derived_coherent_carrier_decoder_cycle48_2026_07_14.py
```

The runner reconstructs the 60-state census, verifies product/entangled
counts, exhausts Clifford and Pauli closure, tests reference-safe teleport
branches, builds adaptive syndrome-dependent trees, replays every generated
complete transcript, compares future Pauli statistics, and checks the magic
state and no-cloning boundaries.

**Disposition:** exact conditional theorem for the declared
stabilizer–Clifford–Pauli–teleport class; partial-narrowing outside it. The
result supports further law construction. It neither edits Qualification nor
licenses an axiom addition.
