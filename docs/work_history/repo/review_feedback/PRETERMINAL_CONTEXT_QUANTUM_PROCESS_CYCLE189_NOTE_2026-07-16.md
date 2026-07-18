# Preterminal context quantum process — Cycle 189

Date: 2026-07-16

Status: exact finite constructive process witness; no constitutional edit

Authority: none

Companion runner:
`scripts/preterminal_context_quantum_process_cycle189_2026_07_16.py`

## Result up front

Cycle 189 constructively closes the finite operational seam identified by
Cycle 181, conditional on an explicit and fully priced quantum process.

The model contains **two system qubits and a two-bit pointer**. A permanent
preparation record selects one of two exact preparations. A later context
record selects one of the six Peres–Mermin commuting joint instruments. The
selected context unitary acts on the system and blank pointer. Pointer records
then form, followed by a terminal tester and terminal result.

The causal order is literal:

```text
blank boundary
    -> preparation record
    -> context-choice record
    -> context unitary and pointer record
    -> terminal tester
    -> terminal record.
```

Thus **the context intervention occurs before the terminal record** and is an
ancestor of it. This is categorically different from Cycle 181, where all six
terminal answers existed before a later classical selector chose one.

The finite model supplies all requested operational fields:

- an **explicit preparation interface** from a common blank;
- six physical context interventions, each with a unitary pointer dilation;
- one **normalized multi-time law** for context-pointer-terminal transcripts;
- **identity containment** for an omitted slot;
- a separate **measure-and-forget** operation obtained by summing actual
  pointer branches;
- a nonzero interference term;
- same-current/different-future instrument behavior;
- a Peres–Mermin shared-answer obstruction; and
- tested **record-fibre future-equivalence** for a tomographically complete
  two-qubit Pauli future repertoire.

For the `prep:X+X+` record and a later `XX` terminal:

```text
slot omitted / identity              -> (+,-) = (1,0)
R1 Z-context measured and forgotten  -> (+,-) = (1/2,1/2)
R2 X-context measured and forgotten  -> (+,-) = (1,0).
```

The R1 history matrix for the `XX+` terminal has total weight `1`. Its
diagonal contributes `1/2`; its off-diagonal interference contributes the
other `1/2`. Writing and then forgetting the R1 pointer removes those cross
terms.

Every physical context gives zero weight to outcome triples with the wrong
Peres–Mermin parity. No assignment of one context-independent value to each
of the nine repeated observables satisfies all six parity sectors. The exact
assignment histogram is:

```text
one satisfied context:    96
three satisfied contexts: 320
five satisfied contexts:  96
six satisfied contexts:    0.
```

This rules out the specific **shared-observable late-lookup model** in which
one context-independent answer for every repeated observable is written
before the context choice and the context merely reveals three entries.

The scope is important. A table that stores a different triple for each
complete context can reproduce the finite one-context marginals. The runner
constructs that comparator exactly. **Context-indexed lookup remains live**
unless shared observable identity, causal independence, and the allowed
memory structure are independently enforced. No unrestricted
hidden-variable or superdeterministic no-go is claimed.

Within the selected model, the complete append-only records are sufficient.
Preparation, context, instrument status, and pointer outcome determine one
future Pauli fingerprint. That fingerprint reconstructs one unique density
operator. The density operator is therefore a derived calculator from the
records and fixed process, not an additional unrecorded physical carrier.

The construction does not derive quantum mechanics from the current
framework. The context instruments, preparation boundary, relative complex
phase, Born pairing, and process category are explicit imports. Actual branch
selection and trial frequencies remain open.

No axiom conclusion follows.

## Frozen input

The runner pins the Cycle-181 seam:

```text
Cycle-181 runner
1431fe5cbbb2f45b17d151b7ed48b5432ca22103dc9e4a26211ae40755bdcb47

Cycle-181 note
606662f96ceae06c13ba413145ccbf389285404dea2dcc4fe1912614beec1ccd
```

Cycle 181 established that its six deterministic context terminals preceded
the choice and hence formed a classical lookup surface. It also isolated the
normalized process, preparation, containment, and instrument fields that were
not supplied by that compiler.

Cycle 189 attacks exactly those finite fields. It does not modify Cycle 181,
the foundation, a registry, an audit result, or a retained claim.

## Exact finite architecture

### System and pointer

The system is:

```text
H_S = C^2 tensor C^2.
```

The pointer is:

```text
H_A = C^2 tensor C^2.
```

Two pointer bits are enough because every maximal commuting Peres–Mermin
context has four nonzero joint outcomes. The third observable value is fixed
by the signed context product.

This is the smallest pointer used by this construction. No theorem of
absolute Hilbert-space or apparatus minimality is claimed.

### Preparation interface

Both preparations begin from the same declared blank:

```text
|00>_S.
```

The preparation record selects:

```text
prep:Z0Z0  -> I_4 |00> = |00>
prep:X+X+  -> (H tensor H)|00> = |++>.
```

The runner also supplies the same vectors directly as a duplicate
implementation control. Direct and unitary implementations with the same
preparation record give identical future laws.

The preparation mapping is not inferred from the word “record.” **The
preparation boundary is imported** as exact process data.

### Contexts

The selected nine two-qubit observables are:

```text
ZI, IZ, ZZ,
IX, XI, XX,
ZX, XZ, YY.
```

The six contexts are:

```text
R1: ZI, IZ, ZZ  -> +II
R2: IX, XI, XX  -> +II
R3: ZX, XZ, YY  -> +II
C1: ZI, IX, ZX  -> +II
C2: IZ, XI, XZ  -> +II
C3: ZZ, XX, YY  -> -II.
```

Every observable appears in exactly two contexts. Each context contains three
pairwise commuting Hermitian involutions. Their product is checked exactly.

The `Y` matrix contains the relative phase `i`, and the final column carries
the `-II` product. **The relative Y phase and C3 sign are imported** as part
of the selected context law. They are not derived from cubic adjacency or
record permanence.

### Joint projectors

For a context `(A,B,C)` and outcome triple `(a,b,c)`, define:

```text
P_(a,b,c)
  = [(I+aA)/2][(I+bB)/2][(I+cC)/2].
```

Exactly four projectors are nonzero. Each is rank one and trace one. They are
orthogonal, sum to identity, and obey:

```text
a b c = signed context product.
```

Wrong-parity projectors vanish algebraically. Their zero probability is not a
host-entered target table.

### Pointer dilation

Use the first two outcome signs as a two-bit word:

```text
u = 1 when a=-1, otherwise 0
v = 1 when b=-1, otherwise 0.
```

For context `c`, define:

```text
U_c
  = sum_(a,b,c lawful)
      P_(a,b,c) tensor X^u tensor X^v.
```

Because the four system projectors are orthogonal and complete, every `U_c`
is Hermitian, involutive, and unitary. With the pointer blank `|00>`, its
pointer Kraus blocks are exactly the four joint projectors:

```text
<uv|U_c|00> = P_(a,b,c).
```

The Lüders branch map therefore follows from the imported context projectors,
the constructed unitary, the blank pointer, and pointer readout. It is not
entered separately as a probability table.

**The context instrument family is imported** in the sense that Nature's
choice of these six projectors and their availability as physical
interventions is not derived. Once that family is granted, the displayed
pointer dilations and branch maps are algebraic consequences.

## Normalized multi-time process

For preparation record `p`, context `c`, pointer outcome `j`, terminal Pauli
tester `T`, and terminal result `d`, the process is:

```text
W(d,j | T,c,p)
  = Tr[ Q_(T,d) P_(c,j) rho_p P_(c,j) ].
```

Here:

```text
Q_(T,d) = (I+dT)/2.
```

The runner evaluates:

```text
2 preparations
x 6 contexts
x 15 nonidentity two-qubit Pauli testers
x 4 pointer outcomes
x 2 terminal outcomes
= 1,440 exact transcript weights.
```

Every weight is nonnegative and every fixed
`(preparation,context,tester)` table sums to one.

This normalization is derived only after the process atoms are supplied.
**The Born trace pairing is imported.** The runner computes its consequences;
it does not derive why physical frequencies must use that pairing.

The physical dilation gives the same nonselective state as summing the branch
maps:

```text
Tr_pointer[
  U_c (rho_p tensor |00><00|) U_c^dagger
]
= sum_j P_(c,j) rho_p P_(c,j).
```

Thus the finite CP instrument is internally complete.

## Context before terminal formation

The protocol record graph is:

| stage | permanent record | parents |
|---:|---|---|
| 0 | blank boundary | none |
| 1 | preparation label | blank |
| 2 | context choice | preparation |
| 3 | pointer outcome | context choice |
| 4 | terminal tester | pointer outcome |
| 5 | terminal outcome | pointer outcome and tester |

The context label is not appended after six terminal results. It chooses
which `U_c` acts before either pointer or terminal outcome exists.

The terminal law changes under that earlier intervention. With
`prep:X+X+`:

- omission retains the `XX` coherence and gives `XX+` with certainty;
- R1 records the two `Z` values and makes the later `XX` result fair; and
- R2 measures the already sharp `X` context and leaves `XX+` certain.

This simultaneously proves context dependence and prevents the unsafe slogan
that every measurement necessarily disturbs.

## Identity containment and omission

The omitted intervention slot is evaluated on the identity map:

```text
rho -> I rho I.
```

For both preparations and every one of the 15 terminal Pauli testers, the
runner checks:

```text
no slot = identity insertion.
```

A performed context measurement followed by loss of its displayed pointer
outcome is instead:

```text
rho -> sum_j P_j rho P_j.
```

For R1 on `prep:X+X+`, these maps give different `XX` records:

```text
identity:               (1,0)
R1 measure-and-forget:  (1/2,1/2).
```

For R2 on that same preparation, the nonselective channel happens to fix the
state and matches identity on the tested future:

```text
R2 measure-and-forget:  (1,0).
```

Therefore:

- omission is typed by identity containment;
- forgetting is outcome coarse-graining after a real intervention; and
- equality or inequality of a particular nonselective channel with identity
  is a process theorem, not a definition.

## Exact interference

Fix the R1 four-projector refinement and terminal event `XX+`. Define:

```text
D_(j,k) = Tr[ Q_(XX,+) P_j rho_(X+X+) P_k ].
```

The exact matrix is Hermitian and positive semidefinite, with eigenvalues:

```text
1/4, 1/4, 0, 0.
```

Its complete-event sum is:

```text
sum_(j,k) D_(j,k) = 1.
```

Its diagonal sum is:

```text
sum_j D_(j,j) = 1/2.
```

The off-diagonal terms contribute:

```text
1 - 1/2 = 1/2.
```

Omitting the R1 interaction preserves the coherent sum. Creating an
orthogonal pointer record and then forgetting its displayed value leaves the
diagonal sum. This is genuine finite interference within the imported
process, not a classical source-bit average.

## Shared-observable lookup obstruction

Every nonzero quantum context branch obeys its signed parity. Suppose instead
that one context-independent table prewrites values:

```text
v(ZI), v(IZ), ..., v(YY) in {-1,+1}
```

and a later context choice merely looks up the relevant three values.

Multiplying the six required context products gives a contradiction:

- each of the nine values appears exactly twice on the left, so the product
  is `+1`;
- the five positive context signs and one negative sign multiply to `-1`.

The exhaustive runner gives the sharper histogram stated above: every table
violates one, three, or five contexts.

The quantum process also passes the operational identity control appropriate
to this narrow claim. For each preparation, every repeated observable has
the same immediate marginal in its row and column contexts. The process does
not evade the contradiction by giving `ZI`, for example, different
single-observable frequencies in R1 and C1.

Accordingly no positive mixture over context-independent shared-observable
tables can match the zero wrong-parity support of all six contexts. Every
table would need zero weight, contradicting normalization.

### Exact limit of that result

If the table is allowed to store six separate context-specific triples, the
contradiction disappears. The runner forms the product of the six supplied
context distributions. It is a normalized context-indexed table and has
exactly the correct one-context marginals.

That comparator does not preserve one shared answer for repeated observables.
It may also carry arbitrary context memory. It nevertheless defeats any
broader statement that “no precomputation can reproduce the finite data.”

The result is therefore:

```text
ruled out:
    one choice-independent shared-observable answer table;

not ruled out:
    context-indexed tables,
    contextual hidden memory,
    measurement-dependent boundaries,
    superdeterministic complete-history encodings.
```

## Record-fibre future-equivalence

The complete current packet distinguishes:

```text
preparation record;
identity, selective, or forgotten instrument status;
context record when an intervention occurred;
pointer outcome when it was retained.
```

The runner deliberately includes multiple raw histories per packet:

1. each preparation is implemented both directly and through its priced
   unitary; and
2. every selective or nonselective commuting context is applied in all six
   component orders.

For each complete packet, all raw histories yield one vector of expectation
values for the 15 nonidentity two-qubit Pauli testers.

Together with normalization, that vector reconstructs:

```text
rho_R
  = (1/4) sum_(P in {I,X,Y,Z}^{tensor 2})
      Tr(P rho_R) P.
```

Thus one complete append-only record packet and the fixed law determine one
future density calculator. Equal complete packets have equal probabilities
for every declared future Pauli test.

The clause-delete controls behave correctly:

- dropping the preparation record merges the two omitted-slot states and
  gives unequal future fingerprints;
- dropping context from selective records merges equal-looking outcome
  triples with unequal future states; and
- dropping identity-versus-instrument status merges omission with
  measure-and-forget and gives unequal futures.

At this tested scope, no separate unrecorded density state is required.
The operator is reconstructed from records plus the fixed process.

This is a finite theorem for the declared two-qubit process and its complete
Pauli tester repertoire. It is not yet a lattice-wide record-fibre theorem.
If a local implementation needs a contingent environment or phase carrier
not recoverable from complete records and fixed law, Qualification pressure
would return.

## Exact import ledger

| ID | imported atom | exact content | what is derived after import |
|---|---|---|---|
| `Q-COMP` | finite composition | two system qubits and two pointer qubits use the generated tensor product | matrix domains and partial traces |
| `B0` | blank boundary | system `|00>` and pointer `|00>` | initial normalized density |
| `P` | preparation selector | records choose `I_4` or `H tensor H` | `|00>` or `|++>` preparation |
| `C` | context family | the nine Pauli words grouped into the six signed contexts | commuting products and rank-one joint PVMs |
| `PH` | relative phase/sign | `Y` carries `i`; C3 has product `-II` | the Peres–Mermin parity contradiction |
| `U` | intervention coupling | context record selects the constructed `U_c` | unitarity, exact pointer Kraus maps, nonselective channel |
| `M` | measure | pointer/terminal PVMs pair with states through `Tr(E rho)` | all 1,440 normalized transcript weights |
| `ID` | containment | an omitted slot inserts identity; outcome erasure sums real branches | projective protocol consistency |
| `R` | record decoder | maps prep/context/pointer/tester events to permanent packets | finite record-fibre sufficiency |
| `A/T` | not supplied | actual branch and repeated-trial process | nothing here; **actuality and frequency remain open** |

Several displayed objects are not independent imports:

- the four Lüders branch maps follow from `C`, `U`, the pointer blank, and
  pointer readout;
- normalization follows from the complete projectors and `M`;
- the interference value follows from the same process contraction; and
- the density operator after a packet is a reconstructed calculator, not an
  extra state atom.

The imported atoms are fields of one candidate exact law contract. The table
does not recommend ten new axioms.

## TOE-lane consequence

The finite process closes a type-level bridge:

```text
preparation records
    + preterminal context instrument
    + pointer records
    + normalized composition
    -> coherent and contextual terminal statistics.
```

It advances:

- formation: an exact instrument can write branch-labelled pointer records;
- probability: the supplied trace process normalizes every finite protocol;
- context: context is a prior physical intervention, not a late decoder;
- state: complete records reconstruct the future operator calculator; and
- memory: omitted, selective, and forgotten histories remain physically
  distinct.

It does not close:

- why this process is Nature's microscopic law;
- how the four-axiom lattice generates the two-qubit and pointer composition;
- how a homogeneous nearest-neighbour rule compiles the context selector and
  dilation;
- why the preparation boundary obtains;
- which weighted branch becomes actual;
- why long-run frequencies follow the one-shot weights;
- continuum locality, matter, gravity, or law selection.

## Constitutional diagnosis

No axiom conclusion follows.

The constructive success weakens the case for putting readout, a second
witness, or a clock into Record as the missing quantum-process principle. The
finite quantum work is done by the exact process law: context instruments,
composition, containment, preparation, and measure.

The current Record/Qualification ontology can host this finite model because
all contingent preparation, context, instrument, pointer, and terminal data
are retained as records, while the density operator is a derived future-law
summary.

The next constitutional discriminator is local derivation:

```text
if a compact nearest-neighbour law derives C, U, M, ID, and R,
    no new state or Record atom is forced;

if a global process is irreducible,
    it is candidate Law content;

if complete physical records fail future sufficiency in the local model,
    Qualification must be reconsidered.
```

The finite witness licenses none of those placements by itself.

## No-Go Discipline Gate

**No-Go-discipline status: PASS for the narrow claim** that a normalized
mixture of context-independent shared-observable answer tables cannot
reproduce the displayed six zero-wrong-parity context laws.

Status is **FAIL for any general no-precomputation, no-hidden-variable,
no-memory, or framework-derived contextuality claim**. Those broader claims
are not shipped.

## N1 — Alternative-route enumeration

| route | marker | exact result |
|---|---|---|
| one context-independent value per repeated observable | `ATTEMPTED` | all 512 tables violate at least one signed context |
| positive mixture of shared-observable tables | `ATTEMPTED` | zero wrong-parity probability forces support only on all-six tables, of which there are none |
| six context-specific precomputed triples | `ATTEMPTED` | succeeds; the runner constructs a normalized product table with the correct one-context marginals |
| identify omission with measured-and-forgotten | `ATTEMPTED` | fails for `prep:X+X+`, R1, and the `XX` future: `1` versus `1/2` |
| claim every measurement must disturb | `ATTEMPTED` | fails: R2 is a real pointer intervention but leaves the selected `XX` future sharp |
| hide context implementation order as memory | `ATTEMPTED` | all six orders of each commuting context give one complete-record future fingerprint |
| hide the preparation behind one coarse “ready” label | `ATTEMPTED` | omitted-slot `prep:Z0Z0` and `prep:X+X+` have different Pauli futures |
| derive the same process from a homogeneous lattice rule | `UNTESTED LIVE ROUTE` | Cycle 189 supplies no local compiler or gluing theorem |

The successful context-indexed route blocks a broad no-go. The shipped
negative is narrowed to the shared-observable table class.

## N2 — Wall-independence audit

After collapsing branch maps and normalization into the one process contract,
the open set is:

```text
W  exact intervention/process/measure/containment contract;
B  preparation and cosmological boundary interface;
F  physical record decoder plus universal future-sufficiency theorem;
L  microscopic local generator and local-to-global gluing;
A  actual-history and repeated-frequency semantics.
```

| pair | first closes second? | second closes first? | independent at current scope? |
|---|---|---|---|
| `W,B` | no | no | yes |
| `W,F` | no; a process may need hidden state | no; lumpability does not choose weights | yes |
| `W,L` | no; a global process does not give a local generator | no; a support rule need not give normalized quantum composition | yes |
| `W,A` | no | no | yes |
| `B,F` | no | no | yes |
| `B,L` | no | no | yes |
| `B,A` | no | no | yes |
| `F,L` | no | no | yes |
| `F,A` | no | no | yes |
| `L,A` | no | no | yes |

`C`, `U`, `M`, and `ID` are not listed as four independent walls. They are
fields of `W`. The branch maps and normalization are derived once those
fields are fixed.

## N3 — Hidden-wall scan

The proof and note were scanned for common hiding phrases.

| phrase | classification |
|---|---|
| “by construction” | used only for algebraic consequences of explicitly displayed matrices; no omitted physical premise |
| “physical context” | means a supplied context-dependent unitary plus pointer record, not derivation from the lattice |
| “preparation” | explicit boundary import `B`, not a state silently supplied by Record |
| “measure” | explicit trace-pairing import `M`, not a theorem from additivity |
| “same observable” | exact equality of one matrix/effect in two contexts; instrument-future equality is not assumed |
| “complete records” | complete only for the declared finite protocol category; universal completeness remains `F` |
| “contextual” | conditional property of the imported process; not a framework-derived law claim |

No hidden condition was promoted after the wall collapse.

## N4 — Residual matching

| cited witness | witness residual | Cycle-189 residual | match? |
|---|---|---|---|
| `OPERATIONAL_CONTEXT_PROCESS_SEAM_CYCLE181_NOTE_2026-07-16.md:20` | late choice is classical lookup after six terminals | make context prior to pointer and terminal formation | yes |
| same note, lines `325–337` | normalized process, containment, and instrument transition imported | supply and price those fields in one finite witness | yes |
| `ALL_NINE_SIX_CONTEXT_SHARED_ANCESTRY_CYCLE177_NOTE_2026-07-16.md:255–271` | not yet physical contextuality, memory, instrument, or probability | build a conditional CP instrument/process with explicit memory records | yes at finite imported-law scope |
| `GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md:26,208,337` | identity insertion, measure-and-forget, and record-fibre obligations | implement all three in one two-qubit process | yes |
| `LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md:41–53,341,376` | finite adaptive process can close while boundary and local derivation remain | same distinction retained | yes |
| Cycle 177 local compiler | homogeneous nearest-neighbour quantum process | Cycle 189 has no such construction | no; not cited as closure evidence |

The nonmatching local-derivation residual is explicitly dropped from the
positive closure claim.

## N5 — Rhetoric audit

The phrase “cannot be precomputed” is unsafe without resolution.

| resolution | tested? | result |
|---|---|---|
| one prewritten parity bit per complete context | no obstruction claimed | six bits can trivially store the signed parity pattern |
| one separately prewritten outcome triple per complete context | yes | succeeds; explicit context-indexed comparator |
| one context-independent value per repeated observable | yes | impossible under all six zero-wrong-parity laws |
| positive mixture of those shared-observable tables | yes | impossible by the same support argument |
| arbitrary contextual memory machine | no | live |
| measurement-dependent or superdeterministic complete history | no | live |
| local lattice implementation of the process | no | open construction problem |

The note therefore uses “shared-observable late-lookup model,” never a broad
“all precomputation.”

## N6 — Partial-closure paths

No new axiom is forced by the remaining imports.

1. `W` can remain a named theorem condition while a compact local amplitude
   or CP law is sought.
2. `B` can be carried by permanent preparation/boundary records rather than a
   new state type.
3. The density operator is already retired as an independent import at this
   finite scope: it is reconstructed from the record packet and `W`.
4. `ID` is a containment field of the process category, not a Record axiom.
5. A local-to-global gluing theorem could retire the finite global process
   specification.
6. A deterministic unique-history or ergodic theorem could later retire
   separate actuality/frequency fields.

These are import-retirement paths, not constitutional decisions.

## N7 — Steelman

A hostile classical reviewer can reproduce every finite one-context
distribution here by sampling six context-specific triples in advance and
revealing the triple named by the later choice. The runner itself constructs
that model. If the device may use context-dependent response functions,
unbounded memory, a measurement-dependent boundary, or a complete-history
encoding correlated with the future setting, the Peres–Mermin support
contradiction does not apply. Moreover, Cycle 189 supplies the quantum
process matrices rather than deriving them from the lattice. Therefore the
result is not a no-hidden-variable theorem and not evidence that the current
axioms uniquely select quantum theory. It is a constructive demonstration
that one explicit preterminal process closes the finite operational jobs and
that a much narrower shared-observable lookup class cannot emulate its six
context supports.

That steelman is accepted and fixes the claim scope.

## N8 — Cross-cycle echo

- Cycle 168 produced exact Peres–Mermin support semantics but retained the
  instrument and probability boundary. Cycle 189 supplies one explicit
  conditional process rather than declaring that boundary impossible.
- Cycle 173/177 established shared ancestry but correctly withheld physical
  contextuality and no-memory claims. Cycle 189 uses an actual prior context
  instrument and still preserves the context-indexed-memory escape.
- Cycle 181 proved that late lookup does not select a process. Cycle 189
  supplies a process and moves the context earlier.
- Cycle 20 showed that operational quotients do not create numerical weights.
  Cycle 189 imports the numerical trace law and derives only its consequences.
- Cycle 30 distinguished identity from measure-and-forget. Cycle 189 realizes
  that distinction in the same PM process used for contextuality.
- Cycle 33 showed how a finite process may close while local derivation and
  boundary remain separate. Cycle 189 does not re-label those residuals as an
  axiom no-go.

No prior convention or wording change retires the physical process import.
The strongest live retirement mechanism remains an exact local
amplitude/instrument law plus gluing and record-fibre theorems.
