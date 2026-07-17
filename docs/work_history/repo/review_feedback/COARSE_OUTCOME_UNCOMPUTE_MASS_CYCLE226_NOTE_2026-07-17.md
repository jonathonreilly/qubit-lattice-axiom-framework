# Coarse outcome, fine-workspace uncompute, and mass — Cycle 226

**Date:** 2026-07-17

**Status:** bounded conditional channel/apparatus discriminator; audit unset

**Authority:** none

**Constitutional effect:** none

**Packaging:** existing draft parking branch and draft PR #5389 only

Companion runner:

```text
scripts/coarse_outcome_uncompute_mass_cycle226_2026_07_17.py
```

## Result up front

Two supplied detector microarchitectures can report the **same coarse outcome
and position statistics** while leaving very different matter states.

Let a patch projector be the sum of orthogonal site projectors,

```text
P_patch = sum_x P_x.
```

The coarse branch is

```text
rho_coarse = P_patch |psi><psi| P_patch / p_patch.
```

It preserves coherence between different sites inside the patch. If an
apparatus instead retains a distinguishable fine label for each site and that
label is exported or dephased, the reduced branch is

```text
rho_site = sum_x P_x |psi><psi| P_x / p_patch.
```

The two branches have the same coarse yes weight and the same position
diagonal. They differ only in within-outcome coherence. `rho_coarse` is pure
for a pure input branch; `rho_site` generally is not.

The runner builds the relevant reversible ordering explicitly. It writes a
fine site workspace, copies only the coarse patch bit, and then **coherently
uncomputes the fine workspace** using the still-present matter position. That
restores the coarse outcome fibre exactly. In the comparison ordering,
archive-before-uncompute exports the fine site label first. Returning the local
workspace to blank afterward does not remove the exported which-site
information, and the reduced matter branch remains site-dephased.

This is standard reversible-channel algebra, not a new measurement theorem.
Its value here is to resolve a bare-metal ambiguity: “two copies of an
outcome” does not say whether an apparatus copied one completed coarse result
or left fine working data in its environment. The latter can change the matter
state even when the visible coarse pointer/output label is identical.

The completed runner reports **12/12 checks passed**.

## Cycle-222 mass discriminator

The same distinction is applied to the supplied Cycle-222 proper-cubic
candidate packets at the reference scale `16` and frozen held-out scale
`16+sqrt(2)`, across all three `C3` sectors. The propagation and band
extractors receive the candidate blocks without a target-mass lookup; the
blocks were still compiled upstream from the supplied mass operator.

At patch half-width `256`, both detector descriptions retain the same branch
weight, more than `0.97045` (the minimum rounds to `0.970455`). If only the coarse patch outcome is retained, the
normalized branch has at least `0.999555` scalar-band weight. If an orthogonal
site label remains archived, the reduced branch has at most `0.712081`
scalar-band weight and purity below `0.002537`.

At half-width `512`, more than `0.999986` of the incoming packet is retained.
The coarse branch has more than `0.9999996` scalar-band weight, but the
site-archived branch still has at most `0.712080` scalar-band weight and purity
below `0.002394`.

| patch half-width | rounded minimum retained branch weight | rounded minimum coarse-band weight | rounded maximum site-archived band weight | rounded maximum site-archived purity |
|---:|---:|---:|---:|---:|
| 256 | 0.970455 | 0.999555 | 0.712081 | 0.002537 |
| 512 | 0.999986 | 0.9999996 | 0.712080 | 0.002394 |

Broadening the patch repairs the coarse branch's band content. It does not
repair a channel that preserves which-site information: across the complete
sampled width grid `0, 16, 64, 128, 256, 512`, the site-archived band value in
each scale/sector changes by less than `5e-5` while the coarse value changes by
more than `0.28`.

This is not a new inertia measurement. Cycle 225 already established that the
force-response calibration belongs to a prepared low-momentum scalar-band
packet. Cycle 226 shows which apparatus microarchitecture preserves or removes
that necessary state condition. Physical post-interaction inertia, detector
recoil, energy conservation, and outgoing packet formation remain open.

At both scales, the branch-weight, coarse-band, and site-archived-band
diagnostics agree when the packet and supplied projectors are co-oriented
along the three positive cardinal axes. This is only **co-oriented
cardinal-axis agreement** of the supplied channel/projector diagnostics, not
physical apparatus covariance, a 24-frame test, a local detector derivation,
or a generally covariant measurement law.

## Bare-metal consequence

The thought experiment now has three distinct stages:

```text
working correlation:
  reversible fine information may exist temporarily

causal completion and uncompute:
  copy the completed outcome class; return unnecessary fine workspace to blank

archive or Record candidate:
  export only the information intended to remain physically distinguishable
```

If “locking” means the first reversible correlation, it is too early for this
candidate architecture: the apparatus would freeze disposable workspace and
over-measure the matter state. If a later physical process can prove the
comparison complete, copy its coarse class, and uncompute the fine workspace,
then a redundant coarse output can coexist with within-class coherence.

That is a design discriminator, not a formation law. Cycle 226 does not prove
that the universe performs the uncompute, decide when one history occurs, or
show that the later output becomes permanent. Occurrence remains supplied,
Born frequency remains supplied, and continuation nonreconnection remains
open.

The strongest current bare-metal candidate is therefore not “a second witness
locks the first copy.” It is narrower:

```text
a completed outcome may be exported after irrelevant working distinctions
have been closed within the supplied apparatus and coherently uncomputed.
```

Even that sentence is not proposed as axiom text. The remaining work must ask
whether the candidate law autonomously generates the apparatus, completion
certificate, uncompute ordering, outcome occurrence, and nonreconnecting
continuation.

## TOE-lane effect

### O — operational quantum

Advanced: the visible outcome alphabet is separated from its physical
instrument. Two channels with identical coarse weights and position diagonals
are distinguished by later phase-sensitive band content. Copying a completed
coarse pointer and independently retaining fine which-site information are
not the same operation.

Open: physical instrument selection, actual outcome occurrence, Born
frequency, Record typing, and continuation nonreconnection.

### T — time

Advanced: the modeled channel depends on the operation order—compute, copy the
coarse class, uncompute, and retain or omit a fine archive. No physical
completion rule or timeout rule is derived.

Open: autonomous close facts, opportunity cadence, metric duration, relative
clock rates, and any law connecting archive formation to a clock. Cycle 226
does not derive a clock.

### I — inertia and matter

Advanced: a coarse outcome can preserve the prepared scalar band while a
fine-site archive with the same visible result lowers the tested scalar-band
weight below `0.72`.
The internal compiled label, packet band, detector information resolution,
and Record copy count remain distinct coordinates.

Open: physical outgoing inertia, recoil, conserved energy, autonomous binding,
mass-spectrum selection, and empirical species parameters.

### G — gravity and source

Advanced: detector information is not treated as a cost-free shadow of matter.
The uncomputed fine workspace and the exported archive are physically
different candidates for energy/source accounting.

Open: no law assigns energy or gravitational source to workspace clearing,
pointer export, or permanent archive. No field equation, metric response, or
universal coupling is derived. Cycle 226 does not derive gravity.

### B — boundary and capacity

Advanced: fine workspace, completed coarse output, redundant copy, and an
exported/dephased fine-label comparator are explicitly separated. Local
workspace can still be uncomputed after export, but it cannot remove the
exported fine label or restore reduced matter coherence without also acting on
that carrier.

Open: blank-carrier supply, archive growth, reset thermodynamics, cosmological
boundary conditions, and repeated-run capacity.

## Imports and nonclaims

Cycle 226 imports:

1. the reference and frozen held-out Cycle-222 candidate laws and packets;
2. the patch family and its site decomposition;
3. the supplied detector microarchitecture, fine workspace, coarse output,
   blank factors, and compute/copy/uncompute ordering;
4. selective branch normalization and squared-modulus weights;
5. an ideal dephasing/export operation for the archive-before-uncompute
   comparison;
6. the finite periodic cardinal slices and numerical tolerances; and
7. all preparation, routing, causal-close, and fresh-capacity resources.

It does not derive a Record, select an outcome, derive Born frequency, derive a
clock, establish physical post-interaction mass, derive gravity, or support an
axiom change. It makes no simulation or storage-limited-universe claim. There
is no axiom conclusion.

## Prior art and novelty boundary

The displayed `rho_coarse/rho_site` fork is the degenerate Lüders update
versus a fine projective refinement whose site result is forgotten. The
degenerate update is due to G. Lüders, “Über die Zustandsänderung durch den
Meßprozeß,” *Annalen der Physik* 443, 322–328 (1950):

<https://doi.org/10.1002/andp.19504430510>

Davies and Lewis's instrument framework makes the broader attribution boundary
explicit: outcome statistics and conditional state change are jointly supplied
by an instrument, so a visible effect or outcome alphabet alone does not select
the postmeasurement channel. Ozawa supplies the standard indirect-measurement
realization theorem for completely positive instruments:

- E. B. Davies and J. T. Lewis, “An operational approach to quantum
  probability,” *Communications in Mathematical Physics* 17, 239–260 (1970),
  <https://doi.org/10.1007/BF01647093>;
- M. Ozawa, “Quantum measuring processes of continuous observables,” *Journal
  of Mathematical Physics* 25, 79–87 (1984),
  <https://doi.org/10.1063/1.526000>.

The repository's earlier [Record-Instrument Selection and Lüders-Form
Primary-Source Audit](./RECORD_INSTRUMENT_SELECTION_LUDERS_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md)
already establishes the same-effect/different-poststate instrument freedom.
Cycle 226 adds only the explicit fine-workspace ordering and the Cycle-222
packet-band regression.

Reversible compute-copy-uncompute is established prior art. Bennett's “Logical
Reversibility of Computation,” *IBM Journal of Research and Development* 17,
525–532 (1973), gives the foundational reversible-computation construction:

<https://doi.org/10.1147/rd.176.0525>

Unitary measurement dilations, partial traces, coarse-grained projectors, and
the loss or recovery of interference under available which-path information
are standard quantum theory. Scully and Drühl's quantum-eraser proposal is a
close conceptual predecessor for the information/interference distinction:

<https://doi.org/10.1103/PhysRevA.25.2208>

[Cycle 209](./COHERENT_CAUSAL_CLOSE_DETECTOR_COMPILER_CYCLE209_NOTE_2026-07-16.md)
already computes a relational outcome, copies only its final `T/R/X` class,
and reverses the workspace. Cycle 226 does not claim novelty for uncompute,
coarse graining, which-path decoherence, or that detector architecture.

The repository contribution is the combined regression fixture that applies
the coarse-versus-fine channel distinction to the Cycle-222 proper-cubic
mass-sector, packet-band, held-out-scale, and axis controls. Global novelty has
not been established.

The Thirring-QCA molecule remains prior work used only in Cycles 205–209. Cycle
226 uses the separate supplied Cycle-222 proper-cubic candidate and neither
rederives nor modifies the published Thirring automaton.

## No-go discipline gate — FAIL for broad locking claims

Only the exact channel identity and sampled Cycle-222 discriminator are
retained. The broad claims “fine correlation is always a Record,” “uncompute
solves measurement,” “every local read destroys inertia,” and “locking must
occur after uncompute” all fail because live architectures and occurrence
laws remain.

### N1 — alternative routes

| route | honesty marker | result or open part |
|---|---|---|
| direct coarse-pointer coupling | **LIVE — EXACT ALGEBRA** | can avoid a fine workspace in an abstract dilation; local physical compiler remains open |
| fine compute, copy coarse class, then uncompute | **ATTEMPTED/EXACT** | restores within-fibre coherence in the supplied finite construction |
| export/dephase fine label before uncompute | **ATTEMPTED/EXACT** | leaves the site-dephased channel after local workspace clearing |
| smooth scattering detector with recoil | **LIVE — UNTESTED** | may generate an outgoing packet and readable class without a projective patch |
| internal-sector QND detector | **LIVE — PARTIAL** | can preserve the supplied internal label but does not supply event position or occurrence |
| destructive detection followed by lawful re-formation | **LIVE — UNTESTED** | may restore an outgoing calibrated object using physical resources |
| record-derived coherent decoder | **LIVE — PRIOR PARTIAL** | Cycle 48 closes a finite replay subtheory, not arbitrary law/apparatus closure |
| global history/process law | **LIVE — PRIOR PARTIAL** | Cycle 30 can weight histories but does not select the local apparatus or actual history |

### N2 — wall independence

Nine walls are kept distinct:

- `W_L`: candidate matter law, internal operator, and prepared packet;
- `W_D`: detector profile, coarse/fine instrument, and branch weights;
- `W_A`: autonomous one-qubit nearest-neighbor apparatus generation;
- `W_U`: physical completion certificate, workspace closure, and uncompute
  ordering;
- `W_O`: one-history occurrence and typing as a framework Record;
- `W_C`: physical continuation nonreconnection meant to underwrite permanence;
- `W_M`: outgoing packet, recoil, conserved energy, and physical inertia;
- `W_T`: opportunity order, metric rate, and cross-clock comparison; and
- `W_H`: history export, freshness, blank capacity, and repeated-run cost.

| pair | first closes second? | second closes first? | independence control |
|---|---|---|---|
| `W_L/W_D` | no | no | one matter law admits many instruments; a detector does not select the law |
| `W_L/W_A` | no | no | an abstract update need not build an apparatus; hardware does not derive the update |
| `W_L/W_U` | no | no | matter propagation supplies no completion certificate; uncompute does not select matter dynamics |
| `W_L/W_O` | no | no | unitary dynamics selects no actual history; occurrence does not derive the law |
| `W_L/W_C` | no | no | reversible matter need not separate continuations; nonreconnection does not select the law |
| `W_L/W_M` | no | no | an internal label does not guarantee an outgoing packet; recoil does not derive the label |
| `W_L/W_T` | no | no | a candidate update supplies no metric rate; a clock does not choose the update |
| `W_L/W_H` | no | no | one update supplies no fresh archive; capacity does not derive matter dynamics |
| `W_D/W_A` | no | no | a host projector lacks a local compiler; hardware geometry does not uniquely select its channel |
| `W_D/W_U` | no | no | a channel formula does not schedule closure; uncompute ordering does not select the profile |
| `W_D/W_O` | no | no | branch weights select no history; occurrence does not derive an instrument |
| `W_D/W_C` | no | no | a detector channel can recohere; nonreconnection does not choose coarse versus fine content |
| `W_D/W_M` | no | no | equal output statistics can leave different packets; an outgoing packet does not derive the detector |
| `W_D/W_T` | no | no | one detector can run at different opportunities; cadence does not select its content |
| `W_D/W_H` | no | no | one pointer supplies no repeated freshness; capacity supplies no channel weights |
| `W_A/W_U` | no | no | hardware need not know when its task is complete; a close certificate does not route hardware |
| `W_A/W_O` | no | no | autonomous apparatus can remain reversible; occurrence does not compile it |
| `W_A/W_C` | no | no | local hardware need not forbid recoherence; nonreconnection does not build hardware |
| `W_A/W_M` | no | no | local interaction need not produce a calibrated packet; packet dynamics does not build a reader |
| `W_A/W_T` | no | no | locality supplies no metric rate; rate supplies no implementation |
| `W_A/W_H` | no | no | one apparatus need not export a history; a tape does not implement the detector |
| `W_U/W_O` | no | no | blank workspace and a ready output select no history; occurrence does not prove clean uncompute |
| `W_U/W_C` | no | no | completion does not prohibit later reconnection; nonreconnection does not prove computation complete |
| `W_U/W_M` | no | no | uncompute can preserve coherence without recoil accounting; an outgoing packet supplies no close token |
| `W_U/W_T` | no | no | causal order is not metric duration; a clock does not certify logical completion |
| `W_U/W_H` | no | no | recycled workspace is not an append-only archive; fresh capacity does not prove uncompute |
| `W_O/W_C` | no | no | selecting/typing a history does not physically prove nonreconnection; a restriction selects no history |
| `W_O/W_M` | no | no | occurrence does not ensure outgoing inertia; matter formation does not select an outcome |
| `W_O/W_T` | no | no | one event label supplies no universal rate; a clock cannot cause its own occurrence |
| `W_O/W_H` | no | no | one Record supplies no repeated blank capacity; capacity selects no outcome |
| `W_C/W_M` | no | no | nonreconnection does not rebuild matter; a packet can form without permanent history separation |
| `W_C/W_T` | no | no | a continuation restriction supplies no rate; cadence does not forbid reconnection |
| `W_C/W_H` | no | no | one separated history supplies no fresh archive; storage alone does not prevent recoherence |
| `W_M/W_T` | no | no | recoil/outgoing dynamics supplies no clock normalization; timing does not restore a packet |
| `W_M/W_H` | no | no | re-formed matter supplies no archive capacity; storage does not guarantee inertia |
| `W_T/W_H` | no | no | slow cadence creates no blank carriers; capacity sets no metric rate |

No pairwise collapse is retained. The runner closes only finite channel
identities and sampled `W_D/W_M` state-condition diagnostics.

### N3 — hidden-condition scan

| phrase | hidden content | disposition |
|---|---|---|
| “erase” | coherent uncompute versus thermodynamic deletion versus tracing an environment | only the first is used for workspace closure |
| “uncompute” | inverse on a still-coherent workspace versus removal of an exported copy | the exported-copy counterexample is explicit |
| “which-site information” | orthogonal fine labels versus an observer actually reading them | reduced-channel effect requires distinguishability, not a conscious observer |
| “coarse outcome” | output alphabet versus full apparatus state | equal output weights do not identify the channel |
| “lock” | logical completion, occurrence, nonreconnection, permanence | all four remain separated |
| “Record” | abstract pointer versus occurring permanent framework fact | only a pointer/archive candidate is modeled |
| “mass survives” | internal eigenlabel, scalar-band packet, inertial response, source mass | only the first two are tested here |
| “probability” | squared norm, occurrence, repeated-run frequency | only supplied squared-norm weights are used |
| “time” | causal order, opportunity index, metric rate | only the ordering is modeled |
| “standard” | prior-art attribution versus framework selection | used only for established algebra; no standard instrument is adopted by the framework |
| “by construction” | dependence on the supplied common `P_x` decomposition versus a derived apparatus fact | the runner label was removed; the shared decomposition remains an explicit part of `W_D` |

The target-encoded coin, prepared packet, patch, fine-label basis, coarse map,
blank workspace, uncompute ordering, dephasing/export comparator, periodic box,
and tolerances are explicit.
The mandatory artifact-wide scan found no unclassified load-bearing hits for
“we assume,” “by construction,” “as is standard,” “the framework provides,”
“bridge context,” “background,” “naturally,” “obviously,” “standard QFT,”
“registered,” or “canonical.” The occurrences in this N3 audit and named
prior-art discussion are classifications, not imported premises.

### N4 — residual matching

| anchored predecessor | witness residual | Cycle-226 residual | exact residual match? | unmatched discriminator |
|---|---|---|---|---|
| [Cycle 209:57–67](./COHERENT_CAUSAL_CLOSE_DETECTOR_COMPILER_CYCLE209_NOTE_2026-07-16.md) | final relational class can be copied while position-dependent workspace is reversed | test the same architecture against coarse/fine Cycle-222 packet-band content | **yes — architecture residual** | proper-cubic loading, autonomous completion, occurrence, archive, and physical output coupling |
| [Cycle 209:112–167](./COHERENT_CAUSAL_CLOSE_DETECTOR_COMPILER_CYCLE209_NOTE_2026-07-16.md) | supplied close facts still leave their autonomous physical generation open | supplied logical order still lacks autonomous close facts and a Record transition | **yes — same autonomous-close residual only** | physical generation of close facts, occurrence, and nonreconnection |
| [Cycle 222:298–324](./CONDITIONAL_FLAVOR_MASS_OPERATOR_COMPILER_CYCLE222_NOTE_2026-07-17.md) | redundant pointers preserve the supplied internal operator but lack locality and occurrence | coarse/fine channels are tested against its prepared packet band | **no — supplied input/control only** | it supplies the matter baseline rather than witnessing the apparatus residual |
| [Cycle 224:186–235](./STATIONARY_LOCAL_FIRST_EVENT_HISTORY_CYCLE224_NOTE_2026-07-17.md) | site projection preserves the internal label but loses the low-band calibration | site-resolving archive is the same fine-channel baseline | **yes — fine-channel residual** | physical apparatus, recoil/outgoing packet, occurrence, and Record transition |
| [Cycle 225:139–172](./LOCAL_CLICK_STRENGTH_RESOLUTION_INERTIA_CYCLE225_NOTE_2026-07-17.md) | broad host-supplied patch preserves the calibrated state condition | coarse fibre uses the same patch baseline and exposes hidden fine workspace | **yes — coarse-channel residual** | physical compiler, autonomous completion, and archive content |
| Lüders 1950 and Davies–Lewis 1970 | a degenerate outcome and a forgotten fine refinement can share statistics but differ in poststate | exact `rho_coarse/rho_site` fork uses that instrument distinction | **yes — formula/instrument residual only** | Cycle-222 regression, local apparatus, occurrence, and permanence |
| Bennett 1973 | compute/copy/uncompute can clear reversible workspace | supplied finite detector ordering uses that same algebra | **yes — algebraic architecture only** | quantum detector generation, Cycle-222 matter coupling, occurrence, and permanence |
| Scully–Drühl 1982 | available path information controls interference | fine archive and within-fibre coherence are compared algebraically | **no — conceptual prior art only** | it does not witness this apparatus residual or mass-sector regression |

No row marked “no” contributes witness support. No predecessor is used to
claim a universal locking boundary or completed measurement theory.

### N5 — rhetoric and multi-resolution scope

| rejected wording | retained wording |
|---|---|
| “uncompute undoes measurement” | “coherent uncompute restores the supplied coarse outcome fibre before fine information is exported” |
| “the same Record causes two futures” | “the same visible coarse output can arise from different supplied channels” |
| “which-site recording destroys mass” | “this fine archive lowers this packet's scalar-band weight” |
| “locking must wait for uncompute” | “this candidate architecture preserves within-class coherence only in that ordering” |
| “a broad detector is nondisturbing” | “the sampled coarse patch retains nearly all of this prepared packet” |

| resolution/domain | retained result | excluded extrapolation |
|---|---|---|
| arbitrary finite pure state and orthogonal fibre projectors | exact coarse-pure versus fine-dephased channel identity | outcome occurrence, permanence, or apparatus selection |
| seven-site/three-internal-state reversible fixture | exact compute/copy/uncompute and archive-order comparator | autonomous nearest-neighbor implementation or thermodynamic cost |
| one/two already-coarse pointer copies | exact same reduced matter channel | spatially independent physical witnesses |
| two scales, three sectors, six patch widths | sampled coarse/fine scalar-band split | continuous optimum, other packets, laws, or detector profiles |
| width `256` and `512` | high-retention coarse branch versus low-band fine archive | physical post-click inertia or recoil |
| three positive co-oriented cardinal axes at both scales | branch-weight and band diagnostics agree | 24-frame covariance, negative-orientation apparatus action, or detector-dynamics covariance |
| all-lattice/all-apparatus level | **not tested** | no universal measurement, locking, or axiom theorem is retained |

### N6 — partial closures

| route or file | status | import partly closed | remaining discriminator |
|---|---|---|---|
| current exact uncompute fixture | **PARTIAL** | finite coarse/fine channel distinction | local apparatus generation, completion facts, occurrence, and archive physics |
| [Cycle 209](./COHERENT_CAUSAL_CLOSE_DETECTOR_COMPILER_CYCLE209_NOTE_2026-07-16.md) | **PRIOR PARTIAL** | bounded relational comparator, close, final-class copy, and uncompute | proper-cubic loading, autonomous close, Record transition, and scalable cost |
| [Cycle 225](./LOCAL_CLICK_STRENGTH_RESOLUTION_INERTIA_CYCLE225_NOTE_2026-07-17.md) | **DIRECT PREDECESSOR** | sampled patch resolution and low-band response condition | fine-workspace content and physical detector |
| [Cycle 48](./RECORD_DERIVED_COHERENT_CARRIER_DECODER_CYCLE48_NOTE_2026-07-14.md) | **PRIOR PARTIAL** | finite record-derived coherent replay | arbitrary-state/law closure and current detector coupling |
| [Cycle 30](./GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md) | **PRIOR PARTIAL** | consistent history-functional route | actual-history law, local apparatus, and metric rate |
| smooth recoil detector | **UNTESTED** | none | autonomous readable scattering output with conserved outgoing inertia |
| internal-sector QND compiler | **UNTESTED LOCALLY** | algebraic commutation only | one-qubit spatial implementation, event position, and occurrence |
| lawful destruction/re-formation | **UNTESTED** | none | resource and energy ledger that recreates the calibrated object |

Each route could retire an import without forcing axiom text. None is silently
converted into a negative conclusion.

### N7 — hostile steelman

The strongest alternative is an ordinary finite detector made by the same
homogeneous local law. Matter scatters from it and transfers conserved
momentum. Its internal reversible circuit accumulates only transient fine data,
derives an outbound completion certificate from the scattering itself, copies
one coarse outcome into a protected rail, and uncomputes all unused workspace.
The outgoing matter packet retains a calibrated inertial response. Only then
does a local amplification/export process make the coarse rail
nonreconnecting, with explicit fresh-carrier and energy cost. [Cycle
209](./COHERENT_CAUSAL_CLOSE_DETECTOR_COMPILER_CYCLE209_NOTE_2026-07-16.md)
contains the bounded comparator/uncompute skeleton; Bennett supplies the
reversible-computation predecessor, and Scully–Drühl supplies the close
information/interference analogy. Cycle 226 does not implement or reject this
complete steelman.

### N8 — cross-cycle echo

| earlier echo | status here | possible retirement mechanism | applicability to Cycle 226 |
|---|---|---|---|
| [Cycle 11](./INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md) | **LIVE PARTIAL** | export selected information to fresh outward carriers | could realize the archive comparison, but does not supply occurrence or permanence |
| [Cycle 16](./DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md) | **LIVE PARTIAL** | explicit close facts instead of timeout | could order uncompute and eligibility, but does not generate the current facts |
| [Cycle 22](./CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md) | **UNRETIRED** | independent cross-clock/rate law | prevents causal order from being called metric time |
| [Cycle 30](./GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md) | **LIVE ALTERNATIVE** | global history functional plus actual-history rule | could replace local occurrence semantics, not the apparatus or matter law |
| [Cycle 32](./LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md) | **LIVE PARTIAL** | growing fronts and fresh archive sites | prices repeated export but does not select coarse versus fine content |
| [Cycle 48](./RECORD_DERIVED_COHERENT_CARRIER_DECODER_CYCLE48_NOTE_2026-07-14.md) | **LIVE PARTIAL** | replay complete records into coherent working state | could recover a finite state family, not generic outgoing matter |
| [Cycle 209](./COHERENT_CAUSAL_CLOSE_DETECTOR_COMPILER_CYCLE209_NOTE_2026-07-16.md) | **DIRECT ARCHITECTURE PREDECESSOR** | compute class, copy only class, uncompute workspace | supplies the exact skeleton tested against Cycle-222 packets here |
| [Cycle 223](./LOCKING_CADENCE_RECORD_KERNEL_DISCRIMINATOR_CYCLE223_NOTE_2026-07-17.md) | **COMPARISON ONLY** | endogenous sparse local trigger | rules out identifying global reset with this staged local process |
| [Cycle 224](./STATIONARY_LOCAL_FIRST_EVENT_HISTORY_CYCLE224_NOTE_2026-07-17.md) | **DIRECT PREDECESSOR** | causal first-event family and explicit history labels | supplies event-ready branches while leaving occurrence and Record open |
| [Cycle 225](./LOCAL_CLICK_STRENGTH_RESOLUTION_INERTIA_CYCLE225_NOTE_2026-07-17.md) | **DIRECT PREDECESSOR** | separate strength, resolution, internal label, and packet inertia | supplies the coarse-patch state condition resolved here by apparatus content |

These live mechanisms defeat every broad locking claim. Cycle 226 supports no
axiom conclusion.

## Falsifiers

The bounded result fails if:

- coherent compute/copy/uncompute does not recover the coarse outcome fibre;
- the coarse and site-archived branches differ in their yes weight or position
  diagonal;
- archive-before-uncompute restores within-fibre coherence after the exported
  fine label is retained;
- one and two copies of an already-coarse pointer induce different reduced
  matter channels;
- the width-`256` coarse rows fail the declared weight/band controls or the
  fine-archive rows remain wholly in the scalar band;
- width `512` fails to retain more than `99.998%` of every sampled packet;
- broadening the patch repairs the retained fine-site channel on this grid;
- passive workspace relabeling changes the reduced channel;
- co-oriented positive cardinal axes fail the declared two-scale diagnostic-agreement controls;
  or
- predecessor controls fail.

Failure of this fixture would not prove that direct coarse, smooth scattering,
QND, re-formation, record-derived, or global-history detector routes fail.

## Verification

```bash
python3 scripts/coarse_outcome_uncompute_mass_cycle226_2026_07_17.py
```
