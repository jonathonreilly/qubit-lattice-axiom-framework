# `CFSI-Q7`: Bell-Capable Coherent Causal-Front Law Probe

**Date:** 2026-07-14

**Type:** meta

**Scope:** exact finite Bell-capable causal-front construction, projective
full-lattice cell family, record-state sufficiency test, and exact-law-value
ablation

**Authority:** none. This is a bounded candidate-law construction and
acceptance probe, not the physical law, an axiom proposal, an audit verdict,
or a retained theorem. It changes no axiom, registry, or audit surface.

## Result In Plain Language

There is a concrete Bell-capable upgrade of the earlier causal-front model
that still uses one `M_2(C)` carrier at every physical site. Call the tested
seven-site cell **`CFSI-Q7`**. Four open sites coherently prepare and move a
Bell pair, three neighboring record sites retain the preparation phase and
the two measurement settings, and one atomic local instrument samples a pair
of outcome records onto the propagated front. The exact construction gives:

- coherent pre-front propagation and entanglement;
- physically recorded setting/context inputs;
- normalized local instruments with exact `CHSH = 2 sqrt(2)`;
- exact no-signalling marginals;
- one sampled record branch;
- post-front invariant record sectors for every admitted continuation;
- linear-extension invariance for the two spacelike local commits;
- compatible finite-cylinder laws on an indefinitely fresh `Z^3` allocation;
  and
- coherent source reset plus export of every outcome to fresh support.

This closes the **architecture** gap that made `CFSI-1`
entanglement-breaking. It does not derive the physical law. The Bell state,
gate values, measurement angles, trace-weight rule, sample instruction,
common frame, causal predecessor decoder, and boundary/program records are
all supplied as one exact law-and-boundary package.

The record-state result is the important bare-metal finding. Outcome records
alone are not a predictive state. In the tested family, two preparations can
have the same local reduced states and the same `ZZ` transcript but opposite
future `XX` transcripts. One persistent preparation-phase bit is the minimum
missing process-memory record for that two-member family. An outcome bit also
needs its recorded setting, and an event needs either reconstructible causal
predecessors or a provenance record. Once the complete packet—phase,
settings, common frame, causal program, predecessor completion, and prior
outcomes—is retained, equal complete record configurations give equal tested
future transcript laws at atomic transaction boundaries. Hidden sample-seed
identity then has no remaining predictive effect.

The bare-metal interpretation is therefore not “a later observer creates a
fact.” It is closer to an atomic commit:

```text
coherent open process
  + recorded program and causal readiness
  + one normalized branch selection
  -> permanent record append
```

A later compatible read reveals and preserves that committed sector. If the
coherent microstages are allowed to be interrupted, their current stage is
additional process memory; the four tested stages require at least two bits.
Declaring the prepare-propagate-commit sequence atomic removes that exposed
stage variable but makes atomicity exact law content.

## The Exact Seven-Site Cell

For cell number `n`, let `b=3n` on a boundary-oriented cubic ray. The seven
physical sites are

```text
phase/preparation record: (b-1,  0,0)
source A work qubit:       (b,    0,0)
source B work qubit:       (b,    1,0)
front A work/record site:  (b+1,  0,0)
front B work/record site:  (b+1,  1,0)
setting A record:          (b+1, -1,0)
setting B record:          (b+1,  2,0)
```

Every control or two-site gate used below lies on a cubic nearest-neighbor
edge. Cells are disjoint. The phase record of cell `n>0` is one edge beyond
the previous A-front record, so the outward family has a local predecessor
route. A supplied boundary record anchors the first cell, the ray orientation,
one common relational Bloch frame, and the causal policy. Those boundary
records are not silently counted among the seven local sites.

The four work qubits are ordered

```text
(source A, source B, front A, front B)
```

and start in `|0000>`. For the recorded phase bit `s in {0,1}`, the coherent
part is

```text
U_s = SWAP_(source B,front B)
      SWAP_(source A,front A)
      Z_(source A)^s
      CNOT_(source A -> source B)
      H_(source A).
```

Exactly,

```text
U_s |0000> = |00>_source tensor |Phi_s>_front,

|Phi_s> = (|00> + (-1)^s |11>)/sqrt(2).
```

Thus the source work pair is restored to blank while the coherent Bell pair
has moved one nearest-neighbor edge to the record front. No outcome has been
written during this coherent portion.

## Recorded Context And Atomic Bell Instrument

The two setting records contain `x,y in {0,1}`. In the common relational
frame, define

```text
A_0 = Z,                       A_1 = X,
B_0 = (Z+X)/sqrt(2),           B_1 = (Z-X)/sqrt(2),
P_a^x = (I+a A_x)/2,           P_b^y = (I+b B_y)/2,
```

for outcomes `a,b in {+1,-1}`. The ready-cell instrument has branches

```text
J_(a,b)^(x,y)(rho)
  = (P_a^x tensor P_b^y) rho (P_a^x tensor P_b^y),

p(a,b|x,y,s)
  = Tr[J_(a,b)^(x,y)(|Phi_s><Phi_s|)].
```

The setting records are physical inputs to the branch map; changing a setting
changes the instrument. Completeness of both local PVMs gives a normalized
joint instrument. The law samples exactly one `(a,b)` and changes the two
front sites from open work sites into site-addressed outcome records in the
selected context.

For `s=0`, the exact correlations are

```text
E_00 = E_01 = E_10 =  1/sqrt(2),
E_11 =                 -1/sqrt(2),
CHSH = E_00+E_01+E_10-E_11 = 2 sqrt(2).
```

Every local marginal is `1/2` independently of the remote recorded setting.
Alice's and Bob's projectors act on disjoint tensor factors, commute, and give
the same branch state and branch weight in either execution order. This is
exact no-signalling plus linear-extension invariance, not a preferred global
simulator order.

The law is common-frame covariant: simultaneous conjugation of the prepared
state and both instruments is a change of representation and leaves every
trace probability fixed. Conjugating the process while holding the measuring
frame fixed changes transcripts. A mixed-frame neighborhood therefore still
needs an explicit relational frame-transport rule; bare `M_2(C)` does not
select one.

## Commit, Permanence, And Later Reading

After a branch is sampled, the selected projector is the record sector on
each front site. A same-context repeat has probability one. A later admitted
read is nondemolition when its map preserves that sector. The runner gives an
explicit controlled unitary `V` with

```text
V* Q_r V = Q_r.
```

An incompatible-setting projector does not commute with the old record
projector and therefore cannot act on that already-recorded carrier as an
admitted continuation. It may be implemented on new work support while the
old record remains readable.

This separates three operations that informal “read twice” language merges:

1. coherent preparation and propagation on open carriers;
2. atomic sampling and append, which forms the record; and
3. later compatible readout, which preserves the formed record.

The model does not prove that nature uses this commit rule. It does show that,
inside a law that takes sample-and-append as primitive, a second later witness
is not logically required to specify a complete Bell-capable append process.
Conversely, the normalized nonselective channel does not pick an actual
branch; sampled actuality remains explicit physical content.

## Record-Only Predictive Sufficiency

The applicable standard is the natural record decoder in
`FULL_LATTICE_FD_SLIR_COMPATIBILITY_AND_MINIMUM_CONTENT_NOTE_2026-07-14.md`:
equal complete records, under the same future protocol, must imply equal
future record-transcript laws.

`CFSI-Q7` passes that test for its declared binary-phase cell family only when
“complete records” includes the complete boundary/program packet.

### Preparation memory

`|Phi+>` and `|Phi->` have identical one-wing reduced density operators
`I/2` and identical certain `ZZ` correlations. They have opposite `XX`
correlations. Deleting the preparation-phase record therefore identifies two
present descriptions with different future transcript tables. One bit is
both sufficient and information-theoretically minimum for this two-member
preparation family.

This is the same finite residual isolated in
`RECORD_STATE_PHASE_SUFFICIENCY_CONSTRUCTIVE_PROBE_NOTE_2026-07-13.md`. It is
not a claim that arbitrary quantum phase is one classical hidden bit.

### Context memory

The same displayed outcome `+1` following a `Z` setting and following an `X`
setting represents different post-front projectors. A later `Z` test is
certain in the first case and has probability `1/2` in the second. The
setting record is therefore part of record identity for prediction; outcome
value alone is insufficient.

### Randomizer memory

Two different uniform sample coordinates that select the same complete
outcome tuple give the same normalized post-front state. Once the branch
record exists, the randomizer coordinate need not be retained as hidden
state.

### Stage memory

The initial, post-Hadamard, entangled-source, and propagated-front states are
pairwise operationally distinct. If external events may interrupt those four
microstages, at least two stage bits—or an equivalent physical phase
certificate—must be reconstructible. In the tested law they are one atomic
transaction. That closes the stage-memory fork conditionally, rather than
deriving atomicity from the current axioms.

### Causal provenance

The complete packet used by the runner contains:

```text
(cell address, phase, setting A, setting B, common frame,
 causal policy, predecessor-complete record).
```

The oriented cell motif and this packet deterministically decode the event
DAG. Preparation precedes propagation; each propagation and its local setting
record precede the corresponding measurement; both local measurements precede
their separate appends; both appends precede cell completion. Alice and Bob
remain incomparable.

This is the schedule/provenance acceptance test supplied by
`CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md`.
In its declared causal-DAG construction, that control removes a global total
execution order while retaining the causal input relation as law content. If
live events instead read whatever happens to be present at execution time,
left-first and right-first schedules produce different permanent `00/01` and
`01/11` laws. `CFSI-Q7` therefore reconstructs causal inputs from
boundary/program records and the cell address; it does not derive the causal
relation from outcome records alone.

Within this restricted decoder, two equal complete packets reconstruct the
same event DAG, branch maps, and every tested finite future cylinder law. The
result is not yet a proof of record-only predictive sufficiency for arbitrary
continuous phases, arbitrary programs, overlapping quantum events, or the
entire physical repertoire.

## Projective Full-Lattice Family And Fresh-Support Export

For any finite recorded context sequence, multiply the normalized cell
kernels. Marginalizing the last cell returns the prior cylinder exactly. The
runner checks all `4^3=64` histories for three cells, every prefix
normalization, a first-cell marginal, and an adaptive second setting selected
from the first outcome record.

Place successive seven-site cells on the boundary-oriented ray above. Every
finite prefix uses distinct sites, and the allocation extends to arbitrarily
large lattice distance. Each outcome is exported to two fresh front sites;
no permanent record is overwritten. Each coherent source pair is exactly
blank after propagation. This supplies a projective full-lattice cell family,
a fresh-support route, and a finite working-register reset.

It does not select the boundary ray, settings, or phase program from a
homogeneous universe. The ray is a boundary-relative construction that
transforms with its anchor, not a privileged bare lattice direction. A final
autonomous law must derive or physically record its allocator and program.

## Exact Law Value Ablation

The architecture does not select its numerical quantum law. Hold fixed the
same sites, record packet, settings, outcome support, sampling semantics,
append rule, causal DAG, and fresh-support allocator. Replace the ideal Bell
state by a Werner state

```text
rho_v = v |Phi+><Phi+| + (1-v) I/4.
```

Both `v=1` and `v=1/2` normalize in every context and give positive support to
every outcome. Yet

```text
CHSH(v=1)   = 2 sqrt(2),
CHSH(v=1/2) = sqrt(2),
```

and a common sample coordinate separates their records. The earlier
`COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md`
independently changes an extensional weight kernel while holding a complete
sampled-append interface fixed. Together these controls show that causal
front, coherence, locality, covariance, permanence, and sampling do not pick
the exact law value.

`CFSI-Q7` packages the exact unitary, angles, visibility, trace weights, and
sample instruction. It does not derive them from “records form,” from a
witness count, or from computational economy.

## Minimum Carrier And Block Accounting

Without explicit source-to-front propagation, the finite Bell commit needs
two work/record sites plus three local program records: five sites. Requiring
an actual coherent preparation region and nearest-neighbor propagation adds
two source work sites, giving `CFSI-Q7`.

Every physical site still has the live one-site possibility algebra `M_2(C)`.
Open-versus-recorded is carried by the existing partial record-map status,
not by a third basis vector. If one site had to autonomously carry a full open
qubit sector plus two orthogonal record sectors, the local carrier would need
dimension at least four. The common frame and causal policy are supplied
boundary records outside the seven-site cell; counting them as free would be
a hidden-wall error.

## What This Does To The TOE Lanes

| lane | result of this probe | remaining load-bearing content |
|---|---|---|
| formation | exact atomic sample-and-append construction | why this commit law, rather than another, is physical |
| reading/witness | later nondemolition read preserves a formed sector | no derivation that a second witness causes formation |
| probability | exact trace-weight Bell instrument and one actual sample | trace/Born value and actualization are supplied |
| quantum repertoire | coherent entanglement, context, CHSH, no-signalling | arbitrary preparations/effects and mixed-frame transport |
| state | restricted complete-record decoder succeeds | general record-Markov sufficiency and phase transport |
| causal order | predecessor DAG; incomparable-order equivalence | physical causal-input decoder and boundary provenance |
| time/clock | event depth orders commits | no metric duration or rate is derived |
| permanence | branch sector plus exhaustive append-only scope | why all physical continuations obey the scope |
| capacity/renewal | fresh `Z^3` export and exact source reset | autonomous allocator; bounded-region reuse if required |
| matter/mass/chirality | no result | exact field/content realization remains open |
| gravity | no result | no capacity-to-curvature law follows from this cell |

The construction is therefore a useful bare-metal candidate **process**, not
a TOE completion. It closes the quantum-compatibility objection to the causal
front, while making the residual physics sharper.

## Constitutional Consequence

This probe does not support adding “read,” “second witness,” or “clock” to the
Record axiom. Those words do not identify the Bell instrument, its weights,
its causal inputs, or its complete predictive state. Nor does “there is one
fixed rule” identify an extensional law value.

The strongest viable constitutional route exposed here is a stable reference
from Admissibility to one exact causal quantum law whose theorems supply
formation, normalized branch weights, causal scheduling, record preservation,
state reconstruction, and renewal. An interface sentence such as

```text
At each causally ready local context, the rule supplies a normalized
record-forming instrument; exactly one branch forms its records, and every
admissible continuation preserves them.
```

describes `CFSI-Q7`, but it is not sufficient by itself: the `v=1`/`v=1/2`
ablation satisfies that prose and changes predictions. Any final axiom add
must either name the exact canonical law referent or be accompanied by a
theorem that selects a unique operational-equivalence class.

The residual atoms to discharge before promotion are:

1. `V`: exact coherent law value—unitaries, measurement repertoire, weights,
   and visibility;
2. `A`: one actual sampled branch, or a deeper deterministic replacement;
3. `F`: common relational frame and mixed-frame transport;
4. `G`: causal predecessor/atomic-transaction domain and provenance decoder;
5. `M`: complete process-memory records and unrestricted record-Markov
   sufficiency;
6. `B`: allowed boundary/program class and actual preparation/settings;
7. `R`: autonomous full-lattice allocator or exact export/renewal; and
8. `T`: any theorem relating commit count to physical clock rate.

These are jobs one exact microscopic law may close together. They are not a
recommendation for eight new axioms.

## No-Go Discipline: Narrow No-Go

The only negative claim licensed by this probe is:

> In the exact binary-phase `CFSI-Q7` family, outcome-site records alone are
> not predictively sufficient: omitting preparation phase, measurement
> context, or nonreconstructible causal provenance can identify present
> descriptions with different future record-transcript laws.

This is not a no-go for complete record configurations, for deterministic
laws, or for all quantum cellular laws.

### N1 — Alternative-route enumeration

| route | status | exact outcome |
|---|---|---|
| outcome records only | `NEGATIVE IN TESTED FAMILY` | `Phi+` and `Phi-` retain different `XX` futures |
| persistent preparation-phase bit | `POSITIVE FOR BINARY FAMILY` | separates the two tested preparation laws |
| recorded measurement settings | `POSITIVE` | distinguishes context-relative post-front projectors |
| complete boundary/program record packet | `POSITIVE IN CFSI-Q7` | deterministically reconstructs the tested DAG and cylinder law |
| operational future-equivalence quotient | `POSITIVE SEMANTIC ROUTE` | can represent state without adding an independent wavefunction |
| external wavefunction/process state | `POSITIVE BUT OUTSIDE LIVE STATE TYPE` | predicts the law while abandoning record-only completeness unless derived as representation |
| atomic prepare-propagate-commit | `POSITIVE CONDITIONAL ROUTE` | removes exposed microstage memory by making atomicity law content |
| interruptible microstages with phase certificate | `POSITIVE WITH COST` | four stages require at least two bits in this circuit |
| causal DAG reconstructed from records/boundary | `POSITIVE IN TESTED CELL` | all Alice/Bob linear extensions agree |
| uncontrolled live-read schedule | `NEGATIVE IN EXACT CONTROL` | `00/01` and `01/11` permanent transcript laws differ |
| hidden sample coordinate after equal branch record | `UNNEEDED` | equal complete branch records give equal post-front states |
| richer contextual/sheaf record | `LIVE` | may generalize phase/context memory without joint incompatible values |

### N2 — Wall-independence audit

Three independent information jobs are separated.

| wall | held fixed while varied | discriminator |
|---|---|---|
| preparation/process memory | same carrier, local marginals, settings, and causal law | opposite future `XX` correlations |
| setting/context memory | same displayed outcome and carrier | later `Z` probability `1` versus `1/2` |
| causal provenance | same local append kernel and permanent-record semantics | schedule-dependent `00/01/11` transcripts |

The exposed-stage requirement is conditional, not a fourth independent wall:
it disappears if the full cell transaction is physically atomic. The common
frame is a representation/transport requirement and is not counted again as
preparation memory.

### N3 — Hidden-wall scan

The cell address, phase, settings, common frame, causal policy,
predecessor-completion record, randomizer, branch map, atomic scope, and fresh
allocator are all explicit. The runner deliberately rejects a packet missing
causal policy. The seven-site count does not hide the boundary frame or
provenance inside a work qubit.

### N4 — Exact residual matching

The preparation residual is exactly the `Phi+`/`Phi-` control in
`RECORD_STATE_PHASE_SUFFICIENCY_CONSTRUCTIVE_PROBE_NOTE_2026-07-13.md`. The
same-state/same-future criterion is H5 of
`FULL_LATTICE_FD_SLIR_COMPATIBILITY_AND_MINIMUM_CONTENT_NOTE_2026-07-14.md`.
The schedule residual is exactly the adjacent live-read fork in
`CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md`.
The exact-value residual is independently matched by the one-record
transcript in
`COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md`.
None of those controls is used to claim a result about clock rate, matter, or
gravity.

### N5 — Resolution and rhetoric audit

All Bell identities are exact symbolic expressions. The predictive-state
claim is restricted to two phases, two settings per wing, and finite cylinder
protocols generated by the declared cell. “Minimum” means minimum bits or
sites inside that declared finite encoding, not a universal lower bound on
all ontologies. “Full-lattice” means an indefinitely extendible projective
family embedded in `Z^3`, not a derivation of an autonomous homogeneous
cosmology.

### N6 — Partial-closure paths

The phase token, recorded settings, and causal program positively close all
three finite discriminators. Atomic transaction scope removes stage memory.
Operational future-equivalence can make the reconstructed density operator a
representation of records rather than extra ontology. A more general local
transport theorem could retire explicit per-cell phase tokens. These positive
routes remain open and are not converted into axiom demands.

### N7 — Strongest steelman

A single exact quantum cellular law could encode its preparation and frame in
ordinary persistent boundary records, derive its causal edges locally, make
all linear extensions equivalent, prove that complete records reconstruct
every future instrument, generate Bell correlations and stable frequencies,
and export records without a hand-programmed ray. If constructed, it would
defeat every negative reading broader than the finite omission claim above
and could leave the current Qualification sentence unchanged. `CFSI-Q7` is a
finite proof of compatibility and an acceptance target, not that final law.

### N8 — Cross-cycle echo

The phase-memory issue repeats the 2026-07-13 constructive sufficiency probe;
it is not counted as a new independent wall. The exact-value issue repeats
the paired-law discriminator. The new closure is that one coherent
Bell-capable cell now passes those earlier interfaces simultaneously. The new
independent acceptance item is causal provenance: importing the schedule
control shows exactly what must be reconstructible when the global
synchronous front is removed.

## Verification

Run:

```bash
python3 scripts/cfsi_q_bell_coherent_causal_front_law_probe_2026_07_14.py
```

The PASS count contains related checks and is not a count of independent
scientific facts.
