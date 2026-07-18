# Bare-Metal Record Formation: Minimum Viable Probe Program Before Axiom Language

**Date:** 2026-07-13

**Type:** meta

**Purpose:** planning and source-side probe map

**Authority:** none. This document changes no axiom, primitive, registry,
audit verdict, or effective-status surface.

**New finite harness:**
[`scripts/bare_metal_record_minimum_viable_probes_2026_07_13.py`](../../../../scripts/bare_metal_record_minimum_viable_probes_2026_07_13.py)
(`PASS=54 FAIL=0`).

**Final finite harness:**
[`scripts/bare_metal_record_final_probes_2026_07_13.py`](../../../../scripts/bare_metal_record_final_probes_2026_07_13.py)
(`PASS=64 FAIL=0`).

**Final synthesis:**
[`BARE_METAL_RECORD_FORMATION_FINAL_PROBE_RESULTS_AND_AXIOM_NEED_NOTE_2026-07-13.md`](BARE_METAL_RECORD_FORMATION_FINAL_PROBE_RESULTS_AND_AXIOM_NEED_NOTE_2026-07-13.md).

**Immediate upstream packet:**
[`READ_TWICE_PACKET_DERIVE_FIRST_UNIFICATION_BOUNDED_NOTE_2026-07-13.md`](../../../READ_TWICE_PACKET_DERIVE_FIRST_UNIFICATION_BOUNDED_NOTE_2026-07-13.md)
and its framework-blind panel record.

## Purpose

Do not choose polished language for record formation until the materially
different bare-metal mechanisms have been distinguished by the cheapest probe
that can make each one fail.

The target is not a miniature TOE. The target is a decision-quality result for
five constitutional questions:

1. What exists before a record: an open possibility, a provisional
   correlation, or nothing state-like?
2. What physical event makes a record rather than a reversible trace?
3. Is permanence absolute, or only robust against operations local to one
   register or observer?
4. Does a clock cause formation, merely timestamp it, or emerge from the
   committed-event order?
5. Which content belongs to the formation statement, and which belongs to
   separate probability, dynamics, resource, or counting theorems?

## Architecture routes that must remain live during probing

| Route | Candidate bare-metal reading | Minimum discriminator | Current finite result |
|---|---|---|---|
| A. Unitary write | The first controlled correlation is already a record. | Apply the complete inverse or a quantum eraser. | The finite write and clock-tag circuits reverse exactly. This route does not by itself supply strict global permanence. |
| B. Physical read | A fact forms when a disjoint receiver becomes outcome-dependent. | Define “read” without consciousness, then test Bell, no-signaling, context choice, and atomicity. | Local quantum instruments pass the finite Bell/no-signaling controls; the physical trigger criterion remains open. |
| C. Redundant witnesses | Two or more disjoint outcome copies make the fact robust. | Undo one copy, then undo all copies. | One-copy undo fails while another orthogonal copy remains; coherent global undo succeeds. Redundancy supplies access-relative robustness, not strict permanence. |
| D. Clock-stamped commit | A local clock/reference event closes the transaction. | Compare an outcome-blind tick, an outcome-conditioned clock register, and a nonunitary commit. | An outcome-blind tick carries no outcome; an outcome-conditioned clock is another witness; both unitary versions reverse. A clock alone is not the locking ingredient. |
| E. Sink/export formation | A trace becomes permanent when old information is exported to inaccessible capacity. | Clean and reuse arbitrary old registers with and without a sink; count capacity over repeated cycles. | A sink works conditionally, but blankness/capacity moves outward and grows with repeated reset. This is a thermodynamic boundary route, not free permanence. |
| F. Fundamental append/collapse | A new stochastic, superselected, or append-only law selects and seals one outcome. | Test linearity, no-signaling, energy conservation, pointer covariance, CPT, and outcome weights. | A finite dephasing commit is well formed but changes a noncommuting Hamiltonian expectation. The route remains live, with the extra law carrying the substance. |
| G. Relational/global-history | Records are definite relative to a realized branch/history, while the global state remains reversible or globally constrained. | Wigner-friend reversal, cross-observer consistency, and the meaning of “exactly one.” | A friend has a local classical record that a global inverse erases. This route remains live only with an explicitly relational or realized-history reading of definiteness/permanence. |

No row is declared the winner. The finite controls narrow what each route can
honestly claim; they do not prove that no more sophisticated version exists.

## Stage A — language-blocking probes

These probes must be resolved before settling formation wording.

### MVP-0 — formation state machine and vocabulary

**Question:** Can the ontology be stated without calling an unlocked object a
record or presupposing a hidden realized outcome?

**Smallest probe:** Exhaustively specify a finite transition system with four
typed stages:

```text
OPEN -> CORRELATED -> REDUNDANT -> COMMITTED
```

For every arrow, state:

- whether an outcome is selected;
- whether the transition is globally reversible;
- whether it consumes a fresh site or register;
- whether Record-axiom permanence already applies;
- whether a clock value is input, output, or merely correlated data.

**Pass condition:** “Record” first appears at exactly one transition, and the
same transition supplies locking. No “record forms, then later locks” state is
allowed under the present axiom meaning.

**Measured result:** The finite syntax filter rejects calling a globally
reversible stage a **strictly permanent** record. It leaves four coherent
families: fundamental append with strict permanence, or redundant,
relational, and sink-export routes with local/access-relative permanence. It
selects none of them.

**Status:** **DONE as a semantic consistency filter; physical permanence scope
OPEN** (new harness P16). This controls every later word but is not a physics
selection theorem.

### MVP-1 — unitary tag versus genuine commit

**Smallest probe:** Three qubits: source, reader, and clock register. Compare
an outcome-blind clock tick, an outcome-conditioned clock correlation, the
complete unitary inverse, and an explicit nonunitary dephasing/commit map.

**Measured result:** The unitary read-plus-clock circuit reverses exactly. An
outcome-blind tick carries no outcome correlation. An outcome-conditioned
clock is another outcome witness. Only the separately inserted commit map
changes the reversal result.

**Language consequence:** Do not write “the clock locks the record” unless the
nonunitary, superselection, or access restriction that performs the locking is
also identified. “Clock-stamped” is presently safer than “clock-caused.”

**Status:** **DONE at finite-model discriminator strength** (new harness P1).

### MVP-2 — local robustness versus absolute permanence

**Smallest probe:** Fan out one coherent source to two disjoint registers.
Undo one write locally; then undo both globally.

**Measured result:** The remaining register keeps the source locally
decohered after one local undo; the complete inverse restores the coherent
source. This agrees with the repaired two-register packet runner
(`PASS=81 FAIL=0`).

**Language consequence:** “Two witnesses” can presently justify “not
revocable by an operation confined to either witness,” not “permanent under
all physical operations.” If the axiom keeps unrestricted “permanent,” another
mechanism or a restriction on allowed physical operations is required.

**Status:** **DONE at finite-model discriminator strength** (new harness P2;
read-twice runner B7).

### MVP-3 — selection, collapse, and relational alternatives

**Smallest probe:** Use the same source/reader circuit in two ways:

1. globally unitary Wigner-friend reversal;
2. selective and nonselective commit maps for pointers commuting and not
   commuting with the model Hamiltonian.

**Measured result:** A local friend record is erased by the coherent global
inverse. A `Z`-commit leaves a `Z` eigenstate fixed but changes the energy of
an `X`-Hamiltonian eigenstate.

**Next minimum extension:** On an entangled pair, test candidate **selective**
commit laws for ensemble linearity, no-signaling, outcome independence,
energy accounting, and CPT/conjugation neutrality.

**Language consequence:** Absolute single-outcome language cannot be borrowed
from the unitary write. It must come from the commit law or be explicitly
realized-history/relational.

**Status:** **PARTIAL** (new harness P11); selective-law sweep remains open.

### MVP-4 — Bell, no-signaling, and spacelike ordering

**Smallest probe:** Bell pair plus two local read instruments. Check:

- Tsirelson value `2 sqrt(2)`;
- deterministic preassigned-outcome ceiling `2`;
- Alice's marginal under two unread Bob contexts;
- equality of Alice-then-Bob and Bob-then-Alice nonselective channels.

**Measured result:** All four controls pass. Disjoint local instruments commute
and do not signal; naïve local preassignment cannot reproduce the correlation.

**Language consequence:** A read/commit statement must not imply a
pre-existing local value. Formation must remain compatible with contextual
quantum alternatives and order-independent spacelike records.

**Status:** **DONE at two-site finite-model strength** (new harness P3; CHSH
companion `PASS=24 FAIL=0`).

### MVP-5 — clock bootstrap, phase alias, and metric

**Smallest probe:** Assign several monotone clock maps to one fixed record
word; separately tag events with a periodic oscillator phase.

**Measured result:** The same word supports different rates. Periodic phases
alias distinct events; a monotone ledger index distinguishes them. The
existing clock interface independently passes `40/0` on the count-versus-rate
boundary.

**Additional measured construction:** A four-phase reversible local reference
can copy its definite phase into a blank timestamp register without already
being a readable clock; an unresolved phase instead entangles reference and
timestamp. The complete timestamp operation is still globally reversible.

**Next minimum extension:** Show how the first **joint commit** produces both
outcome and timestamp, then compare multiple local clocks and derive, rather
than name, their common normalization.

**Language consequence:** The clock may supply a reference label or ordering
relation. It presently supplies neither the outcome, permanence, nor metric
duration.

**Status:** **PARTIAL** (new harness P4 plus existing clock runner).

### MVP-6 — fixed-site capacity, reset, and recurrent physics

**Smallest probe:** Run recurrent motion on a fixed finite region while every
visit is treated as a permanent first-registration. Compare with an expanding
fresh frontier and with finite sink-assisted reset.

**Measured result:** An `N`-site region admits `N` first registrations and then
halts. Recurrent motion continues only if most process steps do not commit, or
if fresh support/sink capacity is separately supplied. Existing reset and
saturation probes agree.

**Language consequence:** Formation cannot be synonymous with every
microscopic clock step on a fixed lattice. The eventual wording must say what
is sparse, what is fresh, or how record support differs from repeatedly used
physical position.

**Status:** **DONE as a capacity discriminator; ontology remedy OPEN** (new
harness P5; blank-reset `31/0`; saturation census).

### MVP-7 — formation, probability form, and prepared state

**Smallest probe:** Hold the controlled-copy write fixed while varying input
amplitudes; exhibit the one-qubit rogue frame function; compare two valid
density-form frame states for one preparation.

**Measured result:** The same write accepts different weights. One-site menu
normalization does not force density form. Density form on its own does not
identify the representing state with the prepared state. On `M_4`, a normalized
power-law alternative gives different weights to one shared projector in two
contexts, while the Born-linear assignment does not. Two states with identical
agreement-basis data also differ in a phase-sensitive read. These reproduce
the FRAME-EXT and PREP-FRAME boundaries and show why agreement statistics alone
are insufficient.

**Next decisive probe:** Randomized two-register `M_4` tomography over product
and phase-sensitive entangled menus, with trial counts and frequencies defined
independently of the proposed agreement pairing. Test:

- noncontextual frame consistency;
- refinement/coarse-graining consistency;
- preparation-to-frame identification;
- eigenstate certainty and repeatability;
- explicit null/failed trials.

**Language consequence:** Formation wording must contain no weight,
probability, frequency, or “one ticket per possibility” content unless that
separate probe closes it.

**Status:** **PARTIAL; highest-priority physics probe** (new harness P6/P14;
composite-Gleason runner `24/0`; read-twice runner `81/0`).

### MVP-8 — pointer/context and gauge covariance

**Smallest probe:** Compare a fixed-basis dephasing instrument with a
basis-invariant readout under a local basis rotation.

**Measured result:** Fixed-basis dephasing fails covariance; trace-only content
is invariant. The existing color-instrument probe likewise finds one
frame-naming instrument and one color-blind instrument, with an order-one
instrument footprint (`40/0`).

**Next minimum extension:** Apply each candidate formation criterion under all
local presentation changes treated as gauge. It must either commute with them
or explicitly identify the recorded pointer as physical rather than gauge.

**Language consequence:** A universal formation clause may refer to supplied
record content or physical alternatives, not an unqualified coordinate,
basis, color frame, or presentation.

**Status:** **PARTIAL; finite covariance rejector DONE, selector OPEN** (new
harness P7 plus color-instrument runner).

## Stage B — TOE compatibility probes

These do not determine the English definition alone, but each can reject a
bare-metal interpretation that would poison a downstream TOE lane.

| ID | TOE path | Minimum viable probe | Stop/go criterion | Current status |
|---|---|---|---|---|
| MVP-9 | Arrow / thermodynamics / phases / hydro | Two record-producing kernels with the same append grammar but different stationary states; then add local detailed balance and test Gibbs. Run forward and inverse record circuits from low- and high-record boundaries. | Do not identify record-count growth with thermodynamic entropy or temperature. Proceed only if a measure, conserved energy, detailed balance, and boundary condition are separately visible. | Finite detailed-balance/Gibbs and relative-entropy controls DONE; arrow runner `43/0`; physical energy/temperature law and past boundary OPEN. |
| MVP-10 | Resource / gravity / horizons | Separate storage from throughput. Move a localized load and compare fields sourced by active load versus accumulated archive. Compare multiple monotone rate laws and multiple clock species. | Reject archive sourcing if it leaves an unobserved gravitational trail. Require universal rate coupling before claiming equivalence-principle behavior. | Moving-source discrete-Poisson, trail, rate-law, capacity-ledger, and universality rejectors DONE; physical energy-to-throughput law and Poisson/Einstein recovery OPEN. |
| MVP-11 | Matter / mass / fermions / chirality | Propagate a reversible excitation through reused sites; compare sparse versus every-step commits. Compare bosonic/fermionic exchange paths with identical endpoint records. Mirror an ordered source-reader-reference frame. | Record occupancy must not be used as a fermion-statistics or mass theorem. An ordered transaction may expose chirality only if the dynamics selects one mirror branch. | Coherent quantum-walk/sparse-commit and exchange/mirror rejectors DONE; physical stable-motif classification, Grassmann sign, mass latency, and mirror selection OPEN. |
| MVP-12 | Source / action / observable / gauge | Give independent transaction histories supplied weights and verify `-log` additivity; vary the weights while preserving composition. Define a source as an intervention and test record-response covariance. | Log additivity is not action selection. Proceed only after the history measure and intervention/readout map are physical. | Composition discriminator DONE; source-response/action selection OPEN. |
| MVP-13 | Lorentz / CPT / causal order | Compare disjoint and overlapping local updates under different schedules; repeat with selective commits on a causal diamond and under conjugation/time reversal. | Disjoint events must be order-independent. A global locking tick or preferred sweep must not be inserted silently. | Asynchronous causal-diamond, commuting-overlap, and time-reversal controls DONE; continuum cone, Lorentz, and CPT closure OPEN. |
| MVP-14 | Cosmology / dark sectors / vacuum energy | Compare sparse-beginning, saturated, and expanding-frontier histories. Track free capacity, commit throughput, archive, and active load separately. | Do not infer expansion, dark energy, dark matter, or a low-record beginning from formation alone. A frontier-growth or boundary law must be independently derived or conditional. | Site/edge/frontier/sparse capacity and arrow boundaries DONE; frontier law, abundance, inflation, and vacuum-energy bridge OPEN. |

## Existing-probe reuse ledger

The following were rerun during this planning pass. Totals are mechanical
checks and overlap heavily; they are not independent evidence counts.

| Existing finite surface | Result |
|---|---:|
| Controlled-copy write isometry | `33/0` |
| Pre-record/dephasing/post-record split | `33/0` |
| Pointer non-demolition and controlled-copy dynamics | `56/0` |
| Pointer broadcast circuit | `35/0` |
| Single-clock blocked-unit split | `37/0` |
| Closed finite clean-reset boundary | `31/0` |
| Composite Gleason bridge controls | `24/0` |
| Record-arrow boundary controls | `43/0` |
| Local-observability/Darwinism bridge | `37/0` |
| Two-site CHSH/Tsirelson controls | `24/0` |
| Gauge/color instrument covariance split | `20/0` |
| Repaired read-twice/two-register packet | `81/0` |
| New bare-metal discriminator harness | `54/0` |
| Final bare-metal probe harness | `64/0` |

The two census-style runners were also rerun: the saturation/availability
census completed, and the supplied formation-rate chain-rule examples
validated. Neither selects the physical admissibility rule or rate law.

## Completed final campaign

The final runner executes these probes in the planned order. Detailed results
and scope limits are in the final synthesis linked above.

1. **Permanence-scope closure:** promote the completed syntax filter into an
   allowed-operation theorem: strict global permanence versus local/access
   robustness, plus site versus composite-transaction identity.
2. **Selective commit sweep:** Bell pair, Wigner friend, energy accounting,
   ensemble linearity, no-signaling, conjugation/CPT, and pointer covariance.
3. **Two-register tomography/PREP-FRAME:** phase-sensitive `M_4` contexts,
   independent frequencies, null trials, refinement consistency.
4. **Local-clock construction:** reference process plus atomic outcome/time
   commit, multi-clock comparison, no count-to-metric shortcut.
5. **Asynchronous causal-diamond test:** demonstrate schedule independence for
   spacelike commits and identify the local rule for overlapping events.
6. **Capacity topology test:** decide whether records are site objects,
   composite events, frontier objects, or sparse archives; reproduce recurrent
   matter without overwriting a permanent record.
7. **Resource/lapse moving-source test:** active load versus archive, universal
   clock coupling, conserved resource ledger, weak-field response.
8. **Stable-motif and thermal pair:** verify that coherent matter propagation,
   exchange statistics, equilibrium, and transport survive the chosen commit
   architecture.

All eight finite blocks are complete. They narrow the permissible language but
do not select one physical commit architecture.

## Drafting guardrails after the completed finite campaign

Constitutional drafting should obey these restrictions:

- Do not say a record exists before it locks; use a different term for a
  reversible precursor.
- Do not say the clock itself locks an outcome. A clock can presently tag or
  serialize a commit.
- Do not equate two witnesses with absolute permanence. Their demonstrated
  gain is resistance to a local undo.
- Do not make every process step, oscillation, or clock tick a record event.
- Do not place Born weights, trial frequencies, counting conventions, rate
  laws, thermodynamic cost, or gravitational resource content in the
  formation sentence.
- Do not name a coordinate, basis, presentation, or gauge frame unless it is
  already physical record content.
- Do not assume the permanent archive is the gravitational source.
- Do not infer fermionic statistics, chirality selection, or mass from
  one-record-per-site bookkeeping.

These are probe-derived guardrails, not the final axiom language.

## Scope discipline

This program is deliberately not a no-go claim. It enumerates seven live
architecture routes, reports finite counterexamples to specific overbroad
readings, and retains collapse, relational, thermodynamic, redundancy, and
global-history steelmen. In particular, a more complete global constraint,
holographic encoding, topological superselection rule, or lawful stochastic
commit could evade a finite unitary reversal control. Such a route would have
to be written explicitly and run through the same Bell, energy, covariance,
clock, and capacity probes.

The cross-cycle lesson applied here is the repaired two-register panel result:
valid fan-out and local-decoherence algebra must not be promoted into strict
permanence, Born weights, or a full composite-menu ontology. The present
program keeps those as separate probe targets.
