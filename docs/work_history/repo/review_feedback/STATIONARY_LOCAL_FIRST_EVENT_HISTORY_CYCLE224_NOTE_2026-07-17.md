# Stationary local first-event history — Cycle 224

**Date:** 2026-07-17

**Status:** bounded conditional first-event/history construction; audit unset

**Authority:** none

**Constitutional effect:** none

**Packaging:** existing draft parking branch and draft PR #5389 only

Companion runner:

```text
scripts/stationary_local_first_event_history_cycle224_2026_07_17.py
```

## Result up front

Conditional on the supplied Cycle-222 candidate update and one supplied
stationary local first-event instrument, a fixed onsite detector generates a
positive, normalized, and phase-sensitive first-hit branch history. The
causal arrival determines the support of the supplied first-hit branch family,
including its earliest nonzero label, rather than a host selecting a late read
time. No one label is selected or occurs. This is **event-ready history, not a
Record**: the construction retains every click-time branch and the survival
branch, does not select an outcome, and does not make any branch or label
permanent.

For fixed detector projector `P`, `Q=I-P`, candidate update `U`, and initial
vector `psi`, the finite-horizon branches are

```text
h_t = P U (Q U)^(t-1) psi,
s_T = (Q U)^T psi.
```

Conditional on supplied orthogonal labels, they have the coherent-dilation
form

```text
psi -> sum_t |t> tensor h_t + |survive> tensor s_T.
```

Unitarity and `P+Q=I` give the exact first-hit identity

```text
||h_t||^2 = ||s_(t-1)||^2 - ||s_t||^2,
sum_(t=1)^T ||h_t||^2 + ||s_T||^2 = 1.
```

The runner also realizes the corresponding supplied absorbing ready/click
instrument with the same Kraus operators after every candidate update:

```text
A_0 = Q tensor |ready><ready| + I tensor |clicked><clicked|,
A_1 = P tensor |clicked><ready|.
```

It verifies `A_0^dagger A_0 + A_1^dagger A_1 = I`, trace preservation, and
positivity. These are conditional mathematical branch weights. They are not
derived Born frequencies or counts of outcomes that actually occurred.

The completed runner reports **20/20 checks passed**. Its largest finite
first-history normalization error is `2.0e-14`; the largest first-hit versus
survival-loss residual is `2.4e-15`; the ready/click Kraus completeness
residual is exactly zero; and the most negative numerical output eigenvalue
is `-2.5e-16`.

## What stationary and causal mean here

The same local projector-valued instrument is applied after every supplied
candidate update. No detector time is scanned, optimized, or chosen after
inspecting the trajectory. Before the candidate matter state reaches the
detector's causal light cone, the detector branch is exactly zero and the
surviving state equals uninterrupted evolution. The first nonzero branch is
therefore fixed by arrival of support at the detector.

That removes the *chosen late-read time* used by a simpler diagnostic. It does
not remove all timing input. The alternation

```text
candidate update -> supplied instrument -> candidate update -> ...
```

is still protocol structure, and the branch index is an update label. It is
not metric duration, a physical clock reading, a formation rate, or a derived
universal cadence. Cycle 224 does not derive a clock.

## Executable controls

### Phase and normalization

One common phase tester uses equal-diagonal initial states with relative
phases `0`, `pi/2`, and `pi`. Their stationary first-hit distributions differ
in every massive sector, while the same-diagonal comparison process built
from `|U|^2` assigns identical histories. Thus the supplied first-hit process
retains multi-step phase information that Cycle 223's global every-tick
read/reset deletes.

Every click branch and the survival branch remain positive and sum to one.
The survival-loss differences agree with the first-hit branch weights at
machine precision. This tests one finite supplied instrument; it does not
derive squared-modulus weighting or frequency interpretation.

| `C3` character | largest coherent phase-history TV | same-diagonal `|U|^2` TV | cumulative 18-step click weight |
|---:|---:|---:|---:|
| `-2 pi/3` | 0.459957 | 0 | 0.554818 |
| `0` | 0.459230 | 0 | 0.546340 |
| `+2 pi/3` | 0.474518 | 0 | 0.604261 |

### Coherent pointer copies and history capacity

For a matter-onsite arrival projector `P`, the abstract controlled pointer
writes

```text
W_1 = Q tensor I_2 + P tensor X,
W_2 = Q tensor I_4 + P tensor (X tensor X)
```

are unitary. Starting with blank pointers, tracing out either one pointer or
two redundantly written pointers gives the same reduced matter channel,

```text
rho -> Q rho Q + P rho P.
```

The second coherent copy therefore adds redundancy but neither selects a
branch nor produces a second dephasing event. This reproduces the
bounded redundancy-invariance distinction needed by the mass ontology: one
and two supplied pointer factors induce the same reduced matter channel in
this construction. It is not a general identification of physical mass.

For the 18-update fixture there are 18 possible first-hit labels plus one
survival label. An exactly readable finite history therefore has rank 19 and
requires at least five abstract history-label bits. All 19 branches have
nonzero weight in the tested fixture. Those five bits are in addition to the
ready/click pointer, addressing and routing, blank preparation, and
repeated-run freshness resources. Orthogonal history labels are supplied. One
or two coherent label copies preserve the same Gram matrix and branch weights;
neither supplies an irreversible archive or fresh capacity for repeated runs.

The diagnostic also compares the orthogonally labeled click weight with the
norm obtained by simply coalescing distinct click-time amplitudes. The latter
map is not an isometry and changes the weight. This is not a modeled physical
erasure operation. It demonstrates that distinguishable event-time labels
are load-bearing structure that cannot simply be deleted while retaining the
same pure-state norm.

Before coalescing, every click branch is transported unitarily to the same
final update. Adding those transported branches to the survival branch then
reconstructs uninterrupted evolution to `1.1e-15`. The following comparison
is therefore not an illicit addition of vectors at different times:

| `C3` character | orthogonally labeled click weight | coalesced-amplitude weight |
|---:|---:|---:|
| `-2 pi/3` | 0.554818 | 0.487960 |
| `0` | 0.546340 | 0.535126 |
| `+2 pi/3` | 0.604261 | 0.867167 |

### Locality, deletion, and apparatus covariance

`P` projects onto all six direction modes at one fixed position on an oriented
cardinal slice. The candidate walk has radius one on that slice. A detector
six sites away is exactly inert before the sixth candidate update and has a
nonzero first-arrival branch at the sixth. Deleting the detector restores
uninterrupted coherent evolution.

The three sixth-update arrival weights are `0.007665`, `0.007707`, and
`2.62e-6`; all earlier weights are exactly zero. The largest deletion residual
is `5.3e-16`, translation error is `5.6e-17`, passive direction-recoding error
is `2.0e-15`, and proper-cubic frame error is `1.7e-16`.

Translating state and detector together preserves every first-event weight.
Passive recoding of all six direction modes preserves them as well. Co-rotating
the oriented axis, input direction pair, and detector through all 24 proper
cubic frames also preserves the result. This is **proper-cubic apparatus
covariance**. It is not a full three-dimensional detector derivation, a
law-generated apparatus, or a proof that the matter law selects this
instrument.

### What survives a local click

On the full four-by-six register-direction update, the internal mass operator
commutes with the candidate coin and the site projector is identity on that
internal register. A nonzero click branch therefore retains its input mass
sector eigenlabel and the expectation of the supplied compiled internal mass
operator exactly in all three tested sectors. This follows because the tested
site projector commutes with that operator; it is not a general claim about
physical mass surviving arbitrary measurement.

In the causal point-source fixture, the position-localized branch has only
`0.242`, `0.242`, and `0.267` scalar-band weight. In a separate conditional
test, an initially prepared Cycle-222 low-momentum packet starts with unit
band weight; conditioning on a site click leaves band weights `0.712`,
`0.711`, and `0.594`. Its subsequent fixed-force response estimators no longer
match its dispersion values:

| `C3` character | retained operator eigenvalue | dispersion mass | conditioned force-response estimator | relative mismatch |
|---:|---:|---:|---:|---:|
| `-2 pi/3` | 86.181343 | 86.181279 | 79.613033 | 7.62% |
| `0` | 1449.401859 | 1449.400736 | 1312.428671 | 9.45% |
| `+2 pi/3` | 0.416797 | 0.416813 | 7.684017 | 1743.5% |

This is one site-projection fixture, not a theorem about every detector. Site
projection reduces scalar-band occupancy below `0.8`, so the previously
calibrated low-band inertia interpretation no longer applies. The displayed
quantity is only the same force-response estimator evaluated after supplied
selective conditioning. The runner does not call it a physical post-click
inertial mass. Re-preparing a low-momentum packet would be an additional
operation.

### Target-unfed remote-detector control

In the target-unfed diagnostic, dispersion and force-response routines
receive the frozen Cycle-222 candidate blocks without a target-mass lookup.
Only after their rows are frozen are they compared with the supplied compiled
mass operator. The coin itself was compiled from that supplied operator, so
target-unfed means no target lookup during response extraction, not a
mass-independent candidate law. A remote detector has negligible, but nonzero,
click weight and changes neither the inertia estimate nor its agreement with
the pre-existing block-dispersion estimate within the declared tolerances.

| `C3` character | compiled target | dispersion | remote-detector inertia | maximum click weight |
|---:|---:|---:|---:|---:|
| `-2 pi/3` | 86.181343 | 86.181279 | 86.180382 | `1.24e-18` |
| `0` | 1449.401859 | 1449.400736 | 1449.384819 | `1.19e-18` |
| `+2 pi/3` | 0.416797 | 0.416813 | 0.416779 | `1.68e-17` |

This is a negligible-click remote control; the Gaussian packet has nonzero
tails, so it is not an exact pre-arrival statement. It establishes that the
remote instrument leaves this tested response effectively unchanged, unlike
Cycle 223's global every-tick rank-one reset. It is not a nonzero-click result.

## Bare-metal interpretation

The useful separation is now four-stage rather than two-stage:

```text
available possibility
  -> reversible local correlation
  -> supplied event-ready first-hit history
  -> selected, inaccessible, persistent Record
```

Cycle 224 constructs only the middle two calculational stages, conditional on
a candidate coherent state and an instrument. Causal arrival makes the
supplied click branch nonzero. Cycle 224 establishes no Record-forming
interface and does not determine that one outcome occurs, which outcome
occurs, or that its content becomes permanent.

This matters for the proposed “reading locks it” idea. A reader can be modeled
as a supplied pointer system, and an onsite matter projector can create a
reversible abstract correlation without a chosen late observation time. A
second abstract coherent pointer factor can carry the correlation redundantly
without changing the reduced channel in this model. The pointer factors are
not spatially located or independently generated readers. Neither they nor the
update index supply the missing commit operation. Calling the update index a
clock would rename supplied cadence rather than derive time.

## TOE-lane effect

### O — operational quantum

Advanced: positive normalized finite first-hit weights, phase-sensitive
histories under one common tester, a stationary ready/click instrument, and
an explicit separation between redundant coherent pointers and occurrence.

Open: derivation of the apparatus and pointer context, physical history-label
creation, outcome occurrence, Born frequency, Record formation, and
permanence. Common lawful preparation from a complete record corpus remains
the unmet Cycle-200 target.

### T — time

Advanced: the earliest nonzero branch is determined by causal arrival under
one fixed repeated protocol; no late read time is scanned. Detector deletion
restores uninterrupted evolution.

Open: the background candidate-update/instrument ordering is supplied. No
metric duration, common rate normalization, lapse law, or clock is derived.

### I — inertia and matter

Advanced: a remote detector leaves the target-unfed mass bridge intact; a
local click preserves the internal mass-sector label; redundant pointer count
does not multiply the matter quantity.

Open: site projection lowers scalar-band occupancy enough that the calibrated
inertia interpretation no longer applies. Physical post-click inertia,
recoil, energy accounting, and re-formation of a persistent bound object
remain unproved. The Cycle-222 matter engine remains conditional.

### G — gravity and source

Advanced: translation and proper-cubic apparatus covariance are useful
locality controls, and detector/archive count is kept distinct from the
matter-sector mass label.

Open: no conserved source, field equation, lapse response, equivalence
principle, or rule distinguishing archive storage from gravitational source
is derived. The fixed force kick remains a supplied diagnostic, not gravity.

### B — boundary and capacity

Advanced: exact causal-light-cone and detector-deletion controls, plus an
explicit finite rank/capacity cost for readable event-time history.

Open: no nearest-neighbor compiler for physical history storage, fresh
capacity for repeated events, open-boundary completion, erasure cost,
capacity renewal, or permanent archive is supplied.

## Imports and nonclaims

Cycle 224 imports:

1. the Cycle-222 proper-cubic candidate working update;
2. a wave vector or density state in its working Hilbert space;
3. a fixed onsite detector projector and a ready/click pointer factor;
4. the repeated update/instrument ordering;
5. the first-hit instrument or its coherent dilation;
6. squared-modulus branch weights;
7. orthogonal blank history labels and enough finite capacity;
8. the preparation, periodic finite box, and force protocol used by controls.

It tests the Cycle-222 force-response estimator on one selectively conditioned
site-projected branch; it does not establish a physical or general post-click
inertial mass. It does not select an outcome, derive Born frequency, derive a
physical Record, establish permanence, derive gravity, or support an axiom
change. It makes no simulation or storage-limited-universe claim. There is no
axiom conclusion.

## Prior art and novelty boundary

Cycle 224's matter input is the supplied Cycle-222 proper-cubic six-direction
candidate restricted to an oriented cardinal slice. Cycle 224's
repository contribution is the combined regression fixture on that supplied
candidate: phase retention, deletion, apparatus covariance, finite history
capacity, mass-sector retention, and remote-inertia controls. No novelty is
claimed for the first-hit formula, telescoping identity, absorbing ready/click
flag, coherent pointer dilation, or one-versus-two-pointer reduced-channel
equality.

Stationary arrival detectors, repeated first-detection quantum walks,
collision models, coherent pointer dilations, and survival-amplitude methods
are established operational constructions. Relevant primary sources include:

- J. J. Halliwell, “Arrival Times in Quantum Theory from an Irreversible
  Detector Model,” *Progress of Theoretical Physics* 102, 707–717 (1999),
  <https://doi.org/10.1143/PTP.102.707>. Its spatial detector is effectively
  irreversible because it couples to a large environment; it does not support
  fundamental permanence or a framework Record.
- H. Krovi and T. A. Brun, “Hitting time for quantum walks on the hypercube,”
  *Physical Review A* 73, 032341 (2006),
  <https://doi.org/10.1103/PhysRevA.73.032341>. Its repeated absorbing
  first-detection formula is a close predecessor of the branch family used
  here.
- H. Friedman, D. A. Kessler, and E. Barkai, “Quantum walks: The first
  detected passage time problem,” *Physical Review E* 95 (2017),
  <https://doi.org/10.1103/PhysRevE.95.032141>.
- T. A. Brun, “A simple model of quantum trajectories,” *American Journal of
  Physics* 70 (2002), <https://doi.org/10.1119/1.1475328>.
- S. Attal and Y. Pautrat, “From repeated to continuous quantum
  interactions,” *Annales Henri Poincare* 7 (2006),
  <https://doi.org/10.1007/s00023-005-0242-8>.
- P. Arrighi, V. Nesme, and R. Werner, “Unitarity plus causality implies
  localizability,” *Journal of Computer and System Sciences* 77 (2011),
  <https://doi.org/10.1016/j.jcss.2010.05.004>. That theorem concerns causal
  unitary evolution, with ancillary encoding in the finite-dimensional
  construction. It does not localize this nonunitary ready/click instrument or
  compile it within the framework's fixed one-qubit-per-site capacity.

These sources support the mechanism class and its limitations; they do not
derive this framework's Record semantics. Global novelty has not been
established.

## No-go discipline gate — FAIL for every broad negative

Cycle 224 retains only the bounded positive first-hit construction above. The
broad claims “causal arrival derives measurement,” “two pointers make a
Record,” and “a record-only theory cannot recover the candidate state” all
have status **FAIL — live untested or partially tested routes remain**.

### N1 — alternative routes

| route | honesty marker | evidence and unresolved part |
|---|---|---|
| stationary onsite first-hit instrument | **ATTEMPTED HERE** | removes a scanned late-read time, but supplies the apparatus, cadence, instrument, weights, pointer, and working state |
| relational contact-to-close/DONE process | **LIVE — PRIOR PARTIAL ATTEMPT** | [Cycle 209](./COHERENT_CAUSAL_CLOSE_DETECTOR_COMPILER_CYCLE209_NOTE_2026-07-16.md) compiles a coherent finite classifier and explicit close, but its loading/arming and final occurrence are supplied |
| record-derived coherent decoder | **LIVE — PRIOR PARTIAL ATTEMPT** | [Cycle 48](./RECORD_DERIVED_COHERENT_CARRIER_DECODER_CYCLE48_NOTE_2026-07-14.md) closes a finite stabilizer grammar, not this non-Clifford matter process |
| direct global history/process law | **LIVE — PRIOR PARTIAL ATTEMPT** | [Cycle 30](./GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md) passes finite process controls without a homogeneous local compiler |
| append-only growing history | **LIVE — PRIOR PARTIAL ATTEMPT** | [Cycle 32](./LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md) supplies an expanding tape and exposes finite-region capacity exhaustion |
| reversible export or environmental dilation | **LIVE — PRIOR/LITERATURE ROUTE** | [Cycle 11](./INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md) and Halliwell-type environmental detectors export information but do not derive fundamental occurrence or permanence |
| autonomous metastable detector | **LIVE — LITERATURE, NOT EXECUTED HERE** | can internalize switching through detector resources; whether the fixed one-qubit nearest-neighbor law can generate those resources remains open |

Only the first row is attempted by Cycle 224. The live rows prevent a broad
no-go or a minimum-axiom conclusion.

### N2 — wall independence

The conditions are bundled into seven operational walls rather than inflated
into every syntactic input:

- `W_L`: candidate matter law, compiled mass operator, and working state;
- `W_I`: detector instrument, pointer frame, and squared-norm branch weights;
- `W_A`: physical apparatus generation and a one-qubit nearest-neighbor
  pointer/history implementation;
- `W_O`: one-history occurrence/selection and typing the result as a framework
  Record;
- `W_C`: the physical continuation restriction meant to underwrite
  nonreconnection/locking beyond the semantic Record label;
- `W_H`: repeated history export, blank capacity, freshness, and cost; and
- `W_T`: update/instrument order, event opportunity, metric rate, clock
  comparison, and normalization.

Instrument and mathematical squared-norm weights are deliberately bundled in
`W_I`; finite label capacity is separated from one-event apparatus generation
because one compiler need not be reusable.

| pair | closing first closes second? | closing second closes first? | independent control |
|---|---|---|---|
| `W_L/W_I` | no | no | one matter law admits many instruments; an instrument does not select the law |
| `W_L/W_A` | no | no | an abstract update may lack a local apparatus; hardware does not select this update |
| `W_L/W_O` | no | no | unitary working dynamics selects no realized branch; occurrence does not derive the dynamics |
| `W_L/W_C` | no | no | a reversible law need not separate continuations; a restriction does not select this matter law |
| `W_L/W_H` | no | no | one update supplies no fresh archive; an archive does not derive mass dynamics |
| `W_L/W_T` | no | no | a ticked update does not set physical rate; a clock does not choose the law |
| `W_I/W_A` | no | no | a Kraus map can be written without a one-qubit compiler; a local circuit does not uniquely choose that map |
| `W_I/W_O` | no | no | a normalized instrument need not yield one actual history; Record occurrence does not derive this instrument |
| `W_I/W_C` | no | no | a reduced instrument need not forbid recoherence; nonreconnection does not select its pointer frame |
| `W_I/W_H` | no | no | one finite dilation provides no repeated freshness; storage alone supplies no branch weights |
| `W_I/W_T` | no | no | the same instrument can run at different opportunities; cadence does not select its pointer basis |
| `W_A/W_O` | no | no | an autonomous detector can remain reversible/unselected; occurrence semantics does not compile its apparatus |
| `W_A/W_C` | no | no | local hardware need not create nonreconnecting sectors; a sector restriction does not route hardware |
| `W_A/W_H` | no | no | one local detector need not export an unbounded history; a tape need not implement the detector |
| `W_A/W_T` | no | no | locality supplies no metric rate; a rate supplies no local implementation |
| `W_O/W_C` | no | no | selecting/typing one history does not physically prove nonreconnection; a restriction selects no history |
| `W_O/W_H` | no | no | one occurring Record does not supply fresh repeated capacity; capacity does not select an outcome |
| `W_O/W_T` | no | no | an occurrence supplies an event label, not a universal rate; a clock cannot cause its own commits |
| `W_C/W_H` | no | no | one nonreconnecting split supplies no fresh storage; capacity alone does not prevent recoherence |
| `W_C/W_T` | no | no | nonreconnection supplies no metric rate; a cadence does not forbid future reconnection |
| `W_H/W_T` | no | no | storage capacity does not set event rate; slow events do not create blank carriers |

No pairwise collapse is claimed.

### N3 — hidden-condition scan

| scanned wording | hidden atom exposed | disposition |
|---|---|---|
| “local detector” | onsite matter projector versus spatially compiled pointer/history factors | only the projector is called onsite; pointer factors remain abstract |
| “generated first event” | branch-family support versus selected occurring label | narrowed to support and earliest nonzero label; no occurrence claimed |
| “click” | Kraus branch versus physical detector firing versus Record | only the first meaning is used |
| “mass survives” | compiled internal eigenlabel versus calibrated packet inertia versus gravitational source | only the commuting eigenlabel is preserved |
| “target-unfed” | no target lookup during extraction versus a target-independent law | the coin's upstream mass-operator compilation is explicit |
| “probability” | squared norm, occurrence chance, and empirical frequency | only supplied squared-norm branch weights are used |
| “background cadence” | update order, physical clock, and metric rate | update order is explicit; clock and rate remain open |
| “history capacity” | abstract label rank versus total routed hardware and repeated freshness | five bits is stated only as a label-factor lower bound |

The literal scan also covered `we assume`, `by construction`, `as is
standard`, `the framework provides`, `background`, `naturally`, `obviously`,
`registered`, and `canonical`. Load-bearing hits reduce to the explicit
`W_L`, `W_I`, `W_A`, `W_O`, `W_C`, `W_H`, and `W_T` imports above. The periodic box, initial vector,
detector coordinate, ready/click factor, force profile, and selective
conditioning are all named.

### N4 — residual matching

| witness | residual attacked there | Cycle-224 residual | match? |
|---|---|---|---|
| [Cycle 223:176–221](./LOCKING_CADENCE_RECORD_KERNEL_DISCRIMINATOR_CYCLE223_NOTE_2026-07-17.md) | global every-tick reset loses the tested force response | whether a negligible-click remote instrument leaves the response unchanged | no—useful comparison control, not closure of the same encountered-detector residual |
| [Cycle 209:114–145](./COHERENT_CAUSAL_CLOSE_DETECTOR_COMPILER_CYCLE209_NOTE_2026-07-16.md) | relational coherent classifier with causal close | privileged onsite projector and absent physical close | no; Cycle 209 is a live counterroute |
| [Cycle 48:27–58](./RECORD_DERIVED_COHERENT_CARRIER_DECODER_CYCLE48_NOTE_2026-07-14.md) | finite stabilizer record decoder | derivation of this non-Clifford working state from complete records | no; target remains open |
| [Cycle 30:413–426](./GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md) | finite non-Markov process-law target | local generation of the Cycle-224 history | no; constructive counterroute |
| [Cycle 32:698–713](./LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md) | growing archive and finite-region capacity | 19 finite labels plus repeated freshness | yes, for capacity typing only |
| [Cycle 11:54–127](./INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md) | exact reversible information export | coherent pointer/history dilation remains reversible | yes, for reversibility only |
| [Cycle 200 target:5–55](./PHASE_SENSITIVE_RECORD_FIBRE_STATE_DISCRIMINATOR_CYCLE200_TARGET_NOTE_2026-07-16.md) | common record-reachable phase discriminator | legal equal-diagonal vectors in a supplied working space | no; it is an unmet target, not negative authority |

All `no` rows are kept as live targets, not cited as no-go support. The exact
Cycle-224 residual ledger is:

| target | result matched | unmatched residual |
|---|---|---|
| late-read timing | one stationary repeated instrument and causal onset | derivation of its opportunity cadence and rate |
| first-hit process | normalized positive branch family | occurrence, selection, Born frequency, and Record formation |
| pointer redundancy | one/two abstract copies share a reduced channel | spatial independence, local generation, inaccessibility, permanence |
| matter | site projection preserves compiled internal eigenlabel | calibrated physical inertia after a nonzero click and detector recoil |
| history | finite rank and live-label count exposed | local routing, repeated freshness, cost, and archive semantics |
| gravity | archive count kept distinct from internal operator label | source law, field equation, geometry, and universal coupling |

### N5 — rhetoric audit

| rejected wording | retained wording |
|---|---|
| “arrival generates the event” | “arrival determines branch-family support and its earliest nonzero label” |
| “the detector fires” | “the supplied click branch is nonzero” |
| “two readers make a Record” | “one/two abstract pointer factors induce the same reduced channel” |
| “mass survives measurement” | “the site projector preserves the supplied internal operator eigenlabel” |
| “the click destroys inertia” | “site projection invalidates this low-band calibration” |
| “remote detector changes nothing” | “its `1e-18`-scale click weight leaves the tested estimator unchanged within tolerance” |

| claim boundary | site/projector | sector/block | finite walk | all-lattice/all-detector |
|---|---|---|---|---|
| causal onset | one supplied site projector | all three supplied blocks | point source, separation six, first eight updates | untested; no universal detector timing claim |
| apparatus covariance | projector co-translated/co-rotated with oriented slice | all three blocks | 31-site periodic cardinal slices, 24 proper frames | untested; no autonomous three-dimensional apparatus |
| internal label retention | site projector is identity on the four-dimensional register | three compiled massive eigenvectors | one four-update point-hit fixture | untested for other instruments, laws, or physical mass notions |
| low-band calibration loss | one selectively normalized site projection | all three blocks | width `0.006`, 160-update force fit | untested for smooth/coarse/scattering detectors or packet re-formation |
| remote response | one detector at coordinate `1000` with nonzero Gaussian-tail overlap | all three blocks | length `4096`, 160 updates, declared force | untested for an encountered detector or infinite-lattice limit |

The positive scope is finite: three supplied sectors, cardinal slices of
periodic boxes, one onsite projector, one 18-update history, one selective
site-projection fixture, and declared force windows. No all-detector,
all-lattice, all-law, physical-occurrence, or fundamental-irreversibility
claim is made.

### N6 — partial closures

| partial path | present status | next discriminator |
|---|---|---|
| stationary arrival opportunity | exact conditional construction here | compile the apparatus and update order from one homogeneous local law |
| relational contact/DONE | bounded Cycle-209 construction | derive loading/close from the proper-cubic matter encounter |
| record-derived decoder | finite stabilizer closure in Cycle 48 | pass this common non-Clifford phase tester |
| non-Markov process law | finite positive Cycle-30 construction | compile it locally and expose physical history carriers |
| append-only history | expanding Cycle-32 architecture | price blank preparation, source response, and long-run renewal |
| environmental/autonomous detector | primary-literature mechanism | realize it within fixed one-qubit sites without hiding a bath or reset |
| continuation separation | candidate permanence semantics | show nonreconnection under the actual selected local law |

Each route can advance without forcing axiom text. No primitive-exhaustion or
minimum-content claim follows.

### N7 — hostile steelman

The strongest opposing construction treats the current record corpus as a
compressed program state. One homogeneous reversible nearest-neighbor law
decodes only the coherent working state needed locally, generates a relational
detector-ready motif from ordinary matter, arms on actual contact, waits for
explicit conserved outgoing close tokens, uncomputes every path-revealing
workspace, and exposes one coherent outcome rail. An ordinary environment or
fresh-carrier front exports that rail into a growing history; the framework's
Record typing then supplies permanence, while empirical frequencies emerge
from the long record corpus. Cycles 11, 16, 30, 32, 48, and 209 establish
nontrivial pieces of this steelman. Cycle 224 neither completes nor defeats
their joint locality, occurrence, non-Clifford, capacity, rate, and source-law
requirements.

### N8 — cross-cycle echo

| earlier echo | consequence here |
|---|---|
| [Cycle 11 reversible export](./INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md) | coherent export does not itself establish an occurring Record |
| [Cycle 16 causal close](./DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md) | explicit bounded close can replace silence, but must be generated for this process |
| [Cycle 22 commit clock](./CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md) | event count can order commits; a clock cannot supply their trigger or rate for free |
| [Cycle 30 process law](./GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md) | current-label Markov failure does not defeat history-dependent dynamics |
| [Cycle 32 append architecture](./LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md) | permanent repeated histories require explicit fresh capacity or another semantics |
| [Cycle 48 decoder](./RECORD_DERIVED_COHERENT_CARRIER_DECODER_CYCLE48_NOTE_2026-07-14.md) | record-derived predictive state is possible for a nontrivial finite subtheory |
| [Cycle 209 causal-close classifier](./COHERENT_CAUSAL_CLOSE_DETECTOR_COMPILER_CYCLE209_NOTE_2026-07-16.md) | relational coherent event readiness is possible without final occurrence |
| [Cycle 223 cadence discriminator](./LOCKING_CADENCE_RECORD_KERNEL_DISCRIMINATOR_CYCLE223_NOTE_2026-07-17.md) | ubiquitous read/reset and sparse local opportunity are physically different protocols |

The repository scan for earlier new-axiom, primitive-exhaustion,
underivation, and structural-undecidability claims finds constructive
retirement mechanisms in exactly these decoders, history laws, close tokens,
fresh carriers, and explicit instruments. Their survival is why the broad
negative gate fails. Cycle 224 carries forward only its bounded positive
construction and supports no axiom conclusion.

## Falsifiers

The bounded construction fails if any of the following executable controls
fails:

- first-hit weights cease to telescope or normalize;
- the ready/click map ceases to be completely positive and trace preserving;
- a first-hit branch has nonzero weight outside the detector's causal light
  cone;
- deleting the detector fails to restore coherent evolution;
- the common phase tester ceases to distinguish coherent histories or its
  same-diagonal classical control gains phase sensitivity;
- translating or co-rotating the entire apparatus changes event weights;
- one and two coherent pointer copies induce different reduced channels;
- a site-projected branch mixes the declared internal mass sector;
- the negligible-click remote detector changes the target-unfed inertia
  estimate or its agreement with block dispersion;
- predecessor controls fail.

The next physical tests are stricter: compile a relational detector-ready
motif under one homogeneous nearest-neighbor law; produce explicit causal
close and one-shot `EVENT-READY` output without a host flag; derive or decode
the working state from complete records; export repeated histories without
silent blank capacity; and test continuation nonreconnection after a supplied
commit. Failure of Cycle 224 alone would not prove those routes impossible.

## Verification

```bash
python3 scripts/stationary_local_first_event_history_cycle224_2026_07_17.py
```
