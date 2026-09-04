# Bare-Metal Record Formation: Final Probe Results And Axiom-Need Boundary

**Date:** 2026-07-13

**Type:** meta

**Scope:** source-side probe synthesis and partial narrowing

**Authority:** none. This note changes no axiom, primitive, registry, audit
verdict, or effective-status surface. Its finite constructions are diagnostic
counterexamples and consistency checks, not empirical results or framework
derivations.

**Same-day status:** intermediate synthesis. The later measure-twice packet
and read-twice reconciliation supersede its constitutional and two-register
placement conclusions.

**Primary new runner:**
[`scripts/bare_metal_record_final_probes_2026_07_13.py`](../../../../scripts/bare_metal_record_final_probes_2026_07_13.py)
(`TOTAL: PASS=64 FAIL=0`).

**First-stage runner:**
[`scripts/bare_metal_record_minimum_viable_probes_2026_07_13.py`](../../../../scripts/bare_metal_record_minimum_viable_probes_2026_07_13.py)
(`TOTAL: PASS=54 FAIL=0`).

**Probe map:**
[`BARE_METAL_RECORD_FORMATION_MINIMUM_VIABLE_PROBE_PROGRAM_NOTE_2026-07-13.md`](BARE_METAL_RECORD_FORMATION_MINIMUM_VIABLE_PROBE_PROGRAM_NOTE_2026-07-13.md).

## Result In Plain Language

The probes do not support the proposed picture in which either a second copy
or a clock tick, by itself, turns a possibility into an absolutely permanent
fact.

A physical interaction can copy outcome information into another place. A
second copy makes that information harder to erase locally. A local clock can
be copied into the same transaction and say when it happened. All three steps
can still be one globally reversible quantum operation. They explain
correlation, redundancy, and timestamping. They do not explain the final
one-way step from alternatives to exactly one permanent record.

That one-way step is the remaining bare-metal issue. It can be fundamental, it
can follow from a restriction on which operations are physically possible, it
can be relative to a branch or observer, it can be exported to inaccessible
support, or it might eventually derive from a deeper global/topological law.
The finite probes eliminate none of those complete families. They do show that
the words **read**, **written twice**, **witnessed twice**, **clocked**, and
**resource-limited** do not silently supply the missing step.

The immediate constitutional result is therefore conservative but important:
do not add the proposed two-witness or clock-lock language to the Record axiom.
The present sentence `Records form.` is more honest than either candidate until
the commit mechanism is scientifically selected. A true TOE still needs that
mechanism as either a derivation or explicit foundational physics; this probe
cycle does not decide which.

## The Bare-Metal State Machine That Survived

The minimum non-circular vocabulary is:

```text
OPEN POSSIBILITY
  -> WRITE: reversible outcome-dependent correlation with disjoint support
  -> REDUNDANCY: further disjoint correlations, still globally reversible
  -> TIMESTAMP: correlation with a local reference value, still reversible
  -> COMMIT: one alternative becomes a permanent record
```

The order of redundancy and timestamping is not fixed by this diagram. They can
be parts of one local transaction. The load-bearing distinction is before
versus after **commit**.

- A **write** is not yet a record under the present Record axiom if its complete
  inverse is still a physical operation.
- A **read** cannot be the primitive pre-record word under the present axiom,
  because `Only records are readable.` Calling the formation trigger a read
  would presuppose the thing it is meant to create.
- A not-yet-locked object cannot be called a record. The Record axiom says that
  when a record is present it already locks one possibility.
- A **timestamp** can be formed jointly with the record. The clock label is
  output content of the event, not the source of irreversibility.
- A **commit** is presently a placeholder for unsupplied predictive content,
  not a
  derived operation and not proposed here as a new primitive.

This yields a useful conceptual wording for theorem work, not axiom text:

```text
A write correlates an available local possibility with disjoint support.
A commit forms a record by locking one alternative of that correlation.
A local reference value fixed in the same commit is its timestamp.
```

The three lines intentionally do not say what triggers a commit, which
alternative is selected, with what weight, or at what rate. Filling those
blanks is physics, not polishing.

## Final Probe Results

### F1 — permanence and allowed operations

On a two-witness GHZ representative:

- an operation on the source plus one witness can restore source coherence by
  moving the branch information elsewhere;
- that operation cannot change the untouched witness;
- the complete inverse acting on all write support restores the initial state;
- exporting the branch label to an environment makes the visible state mixed,
  but including the environment restores global reversibility;
- a record-sector flip becomes forbidden only after a commuting
  record-charge/superselection algebra is imposed.

Therefore redundancy establishes an exact access-relative fact: an operation
disjoint from a surviving witness cannot revoke that witness's content. It does
not establish unrestricted global permanence. Strict permanence can still be
fundamental or derived from a deeper restriction, but the restriction must be
named.

### F2 — selective commit laws

Four finite candidate binary rules were swept over two different ensemble
decompositions of the same local density matrix:

| candidate | ensemble-independent here | eigenstate certainty here | result |
|---|---:|---:|---|
| Born-linear | yes | yes | survives this discriminator |
| normalized power-2 | no (`0.100324` split) | yes | rejected by ensemble/steering consistency |
| deterministic maximum | no (`0.200000` split) | yes | rejected by ensemble/steering consistency |
| uniform | yes | no | rejected by preparation certainty |

The surviving Born-linear row is not a Born derivation. The nonselective
Lueders channel is linear, positive, and trace-preserving in the finite check,
but it is an ensemble update, not a rule saying which outcome becomes the one
realized record. It can also change the expectation of a Hamiltonian that does
not commute with the recorded pointer. A physical commit law therefore still
owes selection, energy exchange/accounting, and a covariant physical pointer.

### F3 — two-register tomography and PREP-FRAME

The complete two-qubit Pauli table reconstructs a prepared phase-entangled
state exactly. Pointer-agreement data alone cannot distinguish that state from
its pointer-dephased version. Phase-sensitive tomography separates them by
Frobenius distance `0.674537`.

A seeded `200,000`-trial synthetic control reconstructs the prepared state with
error `0.004375`; the agreement-only candidate is worse by a factor of `154.2`.
Explicit null trials also show that conditioning away failures changes the
reported frequency, so the denominator must be independently specified.

This is a working falsifier for PREP-FRAME and FRAME-EXT, not their derivation
and not real laboratory data. It confirms the repaired read-twice packet's
boundary: two-register agreement supplies neither the full phase-sensitive
frame nor the identification of the frame state with the prepared state.

### F4 — joint outcome and timestamp

A reversible finite map jointly writes an outcome register and a four-phase
timestamp. It reverses exactly. A separately inserted dephasing/commit map is
what blocks coherent restoration.

The same timestamp was attached to both outcome alternatives, proving that an
outcome-blind local clock can label the event without being an outcome witness.
Repeated coincidence records determine the relative affine calibration of two
local clocks, but monotone reparameterizations preserve event order while
changing durations. Periodic phase also aliases distinct events.

The clock can therefore close a transaction's reference label. It does not
select the outcome, cause permanence, or derive a time metric.

### F5 — asynchronous causal schedule

Disjoint writes and disjoint commits commute. Overlapping controlled-copy
updates do not commute, so they need a local causal order or a more restrictive
rule. A nontrivial overlapping diagonal interaction does commute, proving that
schedule-independent local dynamics remains a live route and that a global
sweep is not forced.

Formation language should therefore use a **local event/reference**, never an
unqualified universal locking tick. Lorentz/CPT closure remains a separate
continuum theorem; the finite causal-diamond control does not establish it.

### F6 — capacity topology

On a fixed `N`-site region, one permanent site record per event saturates after
`N` events. Moving records to a finite edge set changes record identity but not
the finite-capacity result. The already-infinite `Z^3` lattice allows a
nonrecurrent process to keep reaching fresh sites without growing the lattice,
but a recurrent local clock or bound system must export an ever-growing event
ledger after its local sites fill.

A reversible working pattern can reuse the same sites indefinitely if those
steps do not all form records. A finite modular clock can also recur, but its
phase is not a permanent history ledger.

Thus record formation must be sparse relative to microscopic evolution, or the
framework needs a derived compression/export/nonlocal-support mechanism. A
record cannot be synonymous with every state update or clock tick.

### F7 — resource, lapse, and moving sources

A periodic discrete Poisson toy separates a conserved moving active source
from an append-only archive. The archive grows total source strength and leaves
a distinct field at an abandoned location (`1.645161` contrast in the toy).
The permanent archive therefore cannot be identified automatically with
gravitating active load.

Linear, exponential, and reciprocal throughput laws are all normalized and
monotone while giving different rate responses. The same potential also admits
different potential-to-clock maps. Distinct clock species show universal
redshift only after the same response law is imposed.

The compute/storage-limited-universe picture remains a useful hypothesis, but
it has at least four separate physical quantities: active load, processing
throughput, free record capacity, and permanent archive. A TOE gravity lane
must derive their conservation and coupling law. Formation alone supplies none
of them.

### F8 — coherent matter and thermodynamics

In a 20-step coined quantum walk, committing position after every microscopic
step changes the variance from `117.595` (coherent) to `20.000` (dephased).
A single final read preserves the pre-read position statistics, and the
uncommitted walk reverses exactly. Universal per-step formation would therefore
destroy the coherent propagation the matter lane needs.

A separate detailed-balance Markov kernel converges to the Gibbs state for its
supplied `beta`, and relative entropy to that state decreases. The same
transition grammar with another `beta` has another equilibrium. Equal record
counts can also carry unequal ensemble entropies.

Record accumulation can orient an event history. It does not by itself supply
energy, temperature, equilibrium, hydrodynamics, or the past boundary.

## Effect On The TOE Lanes

| lane | what the formation architecture may supply | what remains separate |
|---|---|---|
| measurement / fixed reality | a local commit event and permanent outcome, if a commit law is supplied | trigger, physical pointer, allowed-operation algebra, actual selection |
| probability | an arena of repeated committed events | FRAME-EXT, PREP-FRAME, trial denominator, weight/selection law |
| time | locally ordered events and joint timestamps | metric duration, rate normalization, universal clock response |
| arrow | monotone record inclusion after commits | low-entropy boundary, entropy measure, thermodynamic kernel |
| matter | sparse reads of otherwise coherent dynamics | Hamiltonian/action, stable motifs, fermion statistics, mass generation |
| causality / Lorentz / CPT | commuting spacelike commits and local causal order | overlap rule, continuum cone, Lorentz recovery, CPT of the commit law |
| gauge | content can be stated presentation-neutrally | physical pointer/context selector and gauge-covariant instrument |
| gravity | a measurable local formation-rate observable, conditionally | conserved resource, source identity, field equation, lapse map, equivalence principle |
| cosmology | capacity/frontier variables that can be measured in a model | initial boundary, expansion law, vacuum energy, dark-sector abundance |
| action / source | transaction histories on which a weight could be defined | history measure, intervention map, source/action/readout identification |
| mass / counting / chirality | no result from formation alone | possibility individuation, mirror selection, exchange sign, mass ratios |

The architecture is therefore useful: it organizes the interfaces. It is not a
shortcut that closes all lanes with one resource slogan.

## What This Says About The Proposed Axiom Language

### Phrases rejected at present

- **`A record forms when it is read.`** Circular under `Only records are
  readable.` A pre-record interaction needs another name.
- **`A record forms, then a read locks it.`** Inconsistent with the current
  meaning of record: when present, it already locks one possibility.
- **`The second witness locks it.`** The second witness adds redundancy. It
  remains globally reversible in the finite carrier.
- **`The clock locks it.`** A clock tags or serializes a local event. The
  commit map remains separate.
- **`A record forms exactly when two disjoint witnesses exist.`** Not forced by
  the probes, and it conflates a robustness architecture with strict
  permanence. Fundamental append and superselection routes remain live.
- **`Records are counted by possibility ...`** This is a separate
  individuation/weighting question. It does not belong inside formation merely
  because two registers were used.

### Language that is safe for the next theorem pass

Use **write**, **redundancy**, **timestamp**, and **commit** as distinct typed
objects. Require every candidate commit law to fill these slots explicitly:

```text
trigger:        under what local condition does a commit occur?
selection:      which available possibility is locked, and by what rule?
persistence:    relative to which allowed operations can it never change?
support:        where is the permanent content carried, and how is capacity renewed?
reference:      what local timestamp/order content is fixed with it?
schedule:       how do overlapping and spacelike commits compose?
```

Weights, trial probabilities, physical duration, thermodynamic cost, and
gravitational response remain separate fields even if one eventual law relates
them.

## Axiom Need

There are two different questions that should not be collapsed.

### Does the present axiom text need an edit now?

**No probe-backed edit is justified now.** The current Record block already
states the ontology the framework has chosen: records occur, lock exactly one
admissible possibility, and are permanent. The new probes do not derive a
shorter or more specific formation sentence. In particular, they do not force
two witnesses, a clock, a sink, a probability rule, or a counting rule.

During the current fixed-foundation audit posture, the correct home for each
candidate is a conditional theorem with its complete import stated. No change
to `MINIMAL_AXIOMS`, the primitive registry, or the audit surface is made here.

### Does a finished TOE need more than the current text?

**Yes, unless the commit mechanism is later derived.** `Records form.` asserts
that formation occurs; it does not give a law that generates predictions for
when, where, which outcome, or how persistence is physically enforced. A final
TOE cannot use record formation to derive probability, local time, or gravity
while leaving that load-bearing mechanism forever as an unnamed verb.

The science now exposes a genuine three-way fork:

1. **Objective fundamental commit.** Exactly one outcome and strict
   permanence are basic. Then the final foundation needs a commit/selection
   law, either as a carefully tested refinement of Record or as a distinct
   dynamics principle. Two witnesses and a clock can be consequences or parts
   of its implementation, not substitutes for it.
2. **Derived superselection/global constraint.** A deeper local, topological,
   or global law restricts the allowed operation algebra so that record sectors
   cannot reconnect. Then permanence and formation may become theorems, and no
   new axiom is needed if that derivation succeeds.
3. **Relational/thermodynamic permanence.** Global evolution remains reversible
   while records are permanent only relative to accessible support or a
   realized history. Then the present unrestricted words `exactly one` and
   `permanent` require a relational/access-qualified reading or a future axiom
   clarification.

This is not a request for a ruling. Each branch now has a discriminator. The
fundamental branch owes no-signaling, energy, covariance, and empirical
collapse bounds. The derived branch owes an actual superselection/topological
theorem. The relational branch owes cross-observer consistency and an exact
account of why the framework's one realized configuration is legitimate.

## No-Go Discipline Gate

**Gate result:** the exact finite controls remain usable at their stated scope.
No universal no-go is claimed, so a No-Go Discipline verdict for that broader
proposition is not applicable. No claim is made that no formation derivation
is possible or that a new axiom is already proved necessary. Live routes
remain and are named.

### N1 — alternative routes

| route | marker | result against the narrow claim |
|---|---|---|
| one controlled unitary write | ATTEMPTED | complete inverse restores the pre-write state; correlation alone supplies no strict commit |
| two disjoint outcome copies | ATTEMPTED | surviving witness is locally robust, while the complete fan-out remains globally reversible |
| joint local clock tag | ATTEMPTED | timestamping reverses exactly until an independent commit channel is inserted |
| environment/sink export | ATTEMPTED | visible irreversibility is obtained only by excluding exported support; including it restores the inverse |
| restricted record algebra / superselection | ATTEMPTED | this can protect sectors, but the restriction is additional physical structure not supplied by the write |
| fundamental stochastic append | ATTEMPTED as finite candidate family | it remains live; candidate rules must pass ensemble, energy, covariance, and selection controls |
| relational/global-history record | ATTEMPTED on Wigner-friend carrier | it remains live only with explicitly access-relative definiteness/permanence |

### N2 — collapsed wall set and independence

The raw questions collapse to five walls:

- `C`: commit/persistence mechanism;
- `S`: outcome selection, weighting, and PREP-FRAME;
- `T`: trigger/rate/physical time metric;
- `K`: support identity and long-run capacity;
- `D`: covariant causal dynamics, including energy and schedule consistency.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| C / S | no | no | yes |
| C / T | no | no | yes |
| C / K | no | no | yes |
| C / D | no | no | yes |
| S / T | no | no | yes |
| S / K | no | no | yes |
| S / D | no | no | yes |
| T / K | no | no | yes |
| T / D | no | no | yes |
| K / D | no | no | yes |

The runner gives explicit separations: a valid timestamp without commit; a
commit channel without an actual selected outcome; a fresh frontier without a
rate; and covariant commuting dynamics without permanence.

### N3 — hidden-wall scan

- `by construction` in the finite models means a stated test fixture, never a
  framework premise.
- `prepared` is not silently identified with the Gleason frame; the entire F3
  probe tests that identification and retains PREP-FRAME as separate.
- `standard quantum` machinery is used only inside declared finite controls;
  no laboratory frequency or Born derivation is claimed.
- the local tensor-product carrier, clock phases, Hamiltonians, Markov kernels,
  resource laws, and Poisson map are explicit supplied toy choices.
- no approved primitive is enlarged: kinetic isotropy supplies only
  `c_t=c_s` form, realized state supplies only pointwise evaluation, and scale
  reference supplies only units.

### N4 — residual matching

| witness | residual it actually addresses | residual used here | match |
|---|---|---|---:|
| `MINIMAL_AXIOMS_2026-06-29.md` open gates | formation rule/process, persistence dynamics, time metric | current foundation does not state the commit mechanism or rate | yes |
| repaired read-twice packet, lines 155–167 | local robustness versus strict permanence; FRAME-EXT/PREP-FRAME | redundancy does not supply global permanence or probability | yes |
| single-clock split, lines 161–172 | transfer/count does not fix absolute time unit | timestamps/order do not fix metric duration | yes |
| formation-rate chain rule, lines 34–60 | calculus does not select physical `A` or `F` | resource story does not select rate/lapse law | yes |
| dynamics-content sort, lines 166–170 | saturation and per-step production | permanent record at every update is not viable on the tested recurrent support | yes |
| AC occupancy non-supply note | count-once/count-twice dictionary | objective commit mechanism | **no — dropped for commit claims** |

### N5 — resolution/rhetoric audit

The permanence controls test source-only, source-plus-one-witness, complete
two-witness, and visible-subsystem-versus-exported-ledger scopes on finite
carriers. They do not test every lattice-wide, topological, holographic, or
continuum operation. Accordingly this note says **not supplied by the tested
unitary write/redundancy/clock mechanisms**, never **impossible in the
framework**.

### N6 — partial-closure paths

- Conditional commit theorems with verbatim imports remain the immediate
  legitimate route; no premise registration is performed.
- The approved realized-state primitive can identify the actual realized point
  only after a law permits it; it does not select or weight that state.
- The approved kinetic-isotropy primitive can normalize kinetic form only; it
  supplies no commit rate or physical clock map.
- A relational/access-relative definition could close the apparent global
  reversal conflict without new collapse physics, but it would need to be
  reconciled with the current unrestricted permanence wording.
- A derived superselection/topological theorem would retire the commit import
  without an axiom.
- Prior occurrence and permanence gaps were closed by owner-approved axiom
  clarity, proving that a future axiom route remains possible if derivation
  fails. That history does not pre-authorize an edit now.

### N7 — steelman

A hostile reviewer can reasonably argue that the finite tensor circuits have
tested only ordinary local unitary carriers. A code subspace, topological charge,
global consistency condition, gravitational dressing, or exact superselection
rule derived from the full lattice admissibility law could make record sectors
physically disconnected even though the toy Hilbert space admits a formal
inverse. Likewise, a relational realized-history construction might reproduce
all observable record consistency without objective collapse. Those are strong
live routes. Therefore a universal no-go and a declaration that a new axiom is
required would be premature; this note remains a partial narrowing.

### N8 — cross-cycle echo

- The old occurrence gap was retired by the owner-approved sentence `Records
  form.`; the mechanism/rate residual deliberately survived.
- The persistence wording gap was retired by restoring `records are
  permanent.`; physical persistence dynamics deliberately survived.
- The proposed accumulation/fifth-axiom route was withdrawn after the
  saturation counterexample and replaced by realized-sector conditioning.
- The read-twice branch was repaired from a claimed probability/permanence
  derivation to an access-relative carrier theorem with FRAME-EXT and
  PREP-FRAME explicit.
- Clock/count campaigns repeatedly narrowed internal transfer normalization
  while leaving the physical metric open.

The repeated successful mechanism is not “add every missing sentence.” It is:
name the exact residual, derive the largest conditional theorem, and promote
only content that survives the route competition.

## Verification Ledger

All commands were run in the isolated branch
`codex/bare-metal-mvp-probes-20260713`. No axiom/primitive/audit file was
edited.

| finite surface | result |
|---|---:|
| first-stage bare-metal discriminators | `54/0` |
| final bare-metal probes | `64/0` |
| repaired read-twice/two-register packet | `81/0` |
| admissible one-step controlled-copy class | `33/0` |
| pointer formation dynamics constraint | `56/0` |
| record dephasing/broadcast interface | `33/0` |
| pointer broadcast circuit | `35/0` |
| single-clock blocked-unit split | `37/0` |
| blank/reset boundary | `31/0` |
| composite Gleason controls | `24/0` |
| post-record arrow firewall | `43/0` |
| local observability decoder | `37/0` |
| two-site CHSH/Tsirelson controls | `24/0` |
| color-instrument covariance discriminator | `20/0` |
| minimal-axiom companion | `68/0` |
| axiom/primitive purity guard | all four premise nodes clean |
| saturation/availability census | completed |
| formation-rate chain rule | validated |

These totals are overlapping mechanical assertions, not independent evidence
counts.

## Next Science Step

The planned finite language-blocker suite is complete. The next useful work is
not another wordsmithing round on “two witnesses.” It is to put the three live
ontology families through one common decision packet:

1. objective stochastic/fundamental commit;
2. derived superselection/global constraint;
3. relational/access-relative commit.

Each packet should use the six-slot template above and face the same
no-signaling, energy, covariance, causal-schedule, capacity, tomography, and
clock tests. Only after one branch closes or the others fail should exact axiom
language be frozen.
