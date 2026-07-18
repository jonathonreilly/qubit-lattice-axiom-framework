# Redundant archive, permanence, and history — Cycle 283

Date: 2026-07-17

Branch: `codex/bare-metal-mvp-probes-20260713`

PR: existing draft PR #5389 only

Authority: none

Audit: unset

Constitutional effect: none

## Result up front

Cycle 283 takes the Cycle-278 same-code contact instrument as fixed input and
constructs a finite redundant archive and causal-close tournament around it.
The input effect is exactly the physical-M2 contact-active projector

\[
 Q=\mathbf 1_{N_x\ge2},
\]

represented by Cycle 278 as the 64-term Walsh polynomial on the connected
edge code.  Its rank is `57`, it is the support of the actual Cycle-230
contact generator, and its exact pointer-one weights on the three displayed
same-code state families remain

\[
 57/64,\qquad 13/16,\qquad 31/32.
\]

The archive stores each coarse result in fresh `(valid,value)` pairs.  It
closes only after the Cycle-278 pointer has been coherently uncomputed, every
archive pair is valid, and all values agree.  Training archive depths are
`1,2,3`; held-out depth 5 passes.  Training finite-size labels are
`L=3,4,5`; held-out size L=6 passes.  The exact weights are independent of
archive depth and finite-size label because the archive acts only after the
same bounded local effect.

The strongest positive result is a finite, projectively consistent history
candidate:

- every tested archive depth closes with unit support;
- the working pointer returns to blank;
- the value-one archive weight is exactly the Cycle-278 contact weight;
- deleting a middle archive link, the uncompute token, or close prevents
  close;
- a single archive-value fault is rejected by the consistency close;
- fresh append-only continuations preserve every earlier prefix;
- the two-history cylinder measure is normalized, strongly positive, and
  projectively consistent through held-out depth 5; and
- the archive ladder is covariant under all 24 proper-cubic frames and the
  full 27-element translation group at every tested depth.

The adversarial result is equally exact:

1. unrestricted local reversible reconnection erases every archive and close
   at every tested depth;
2. redundancy does not repair the Cycle-279 split false-close—deleting the
   data contact coupling while leaving `DONE` alive writes a consistent `NO`
   archive and closes with unit weight;
3. an all-correlated value flip passes the consistency close while inverting
   every archived value; and
4. finite append capacity grows linearly and target reuse is XOR erasure, not
   append.

These results do not contradict the current Record axiom.  Record supplies
permanence after Record typing: when a lawful Record is present it locks one
admissible possibility, one per site, permanently.  Cycle 283 does not derive
the missing decoder/formation rule that types these coherent archive rails as
Records or makes inverse reconnection an unlawful continuation of that Record
sector.  A supplied controls-only continuation grammar illustrates the needed
compatibility but is not promoted to fundamental law.

Pointer copying is not a Record.  More precisely, these displayed coherent
copies alone do not earn the framework's Record type.

No route-independent obstruction, minimum-content theorem, or axiom pressure
is retained.

## 1. Fixed Cycle-278 input

For occupation words `n in {0,1}^6`, Cycle 278 defines

```text
contact_active(n) = 1 when popcount(n)>=2, else 0.
```

Its exact Walsh expansion is

\[
 Q=\sum_{m\in\{0,1\}^6}c_m\prod_dB_d^{m_d},
 \qquad
 c_m=2^{-6}\sum_n\mathbf1_{|n|\ge2}(-1)^{m\cdot n}.
\]

The Cycle-283 runner imports the Cycle-278 coefficient function, reconstructs
all 64 occupation values exactly as rational numbers, obtains rank `57`, and
checks equality with the support of

\[
 {N_x\choose2}.
\]

It also pins the actual fixture `beta=-0.3`, `g=0.37`.  The contact generator
is not called physical energy.  No rate or source is inferred from its
coefficient.

The reversible archive calculation uses the exact two-dimensional invariant
test subspace spanned by occupation `000000` in `Q=0` and occupation `000011`
in `Q=1`.  This is a witness subspace of the actual 64-dimensional local cell,
not a replacement code.  Exact rational statistics on the three Cycle-278
same-code families are checked separately.

## 2. Redundant valid/value archive

For archive depth `d`, the logical interface contains:

```text
pointer p
DONE
UNCOMPUTED
CLOSE
(valid_0,value_0),...,(valid_(d-1),value_(d-1)).
```

The supplied circuit is:

```text
contact-controlled pointer write
 -> DONE
 -> valid/value copy down the fresh archive chain
 -> inverse contact-controlled pointer write
 -> UNCOMPUTED
 -> CLOSE if DONE, UNCOMPUTED, all valid, and all values agree.
```

The close is a reversible predicate flip.  A routed status rail evaluates it
sequentially along the archive ladder.  No timeout, silence, or compiler-step
count creates a `NO` fact.

For the coherent witness

\[
 |\psi\rangle=(|Q=0\rangle+|Q=1\rangle)/\sqrt2,
\]

the final state has the form

\[
 \frac{1}{\sqrt2}
 \left(
 |Q=0\rangle|00\cdots0;C\rangle
 +|Q=1\rangle|11\cdots1;C\rangle
 \right),
\]

with every validity bit one and the working pointer blank.  It is one coherent
pure state, not one selected history.

For the Cycle-278 diagonal state families, tracing the archives gives the same
nonselective contact instrument and each archive's value-one marginal is the
same rational contact weight.  More copies do not create a new instrument or
a second independent interaction.

## 3. Unrestricted reconnection

Every operation in the finite archive circuit is an involutive local logical
gate.  Reversing their order gives an exact inverse.  The runner applies that
inverse at depths `1,2,3,5` and reports the maximum state-vector residual.
Every archive, validity bit, completion token, and close returns to blank.

This is the correct scoped statement:

> Under the displayed unrestricted reversible continuation domain, finite
> redundant archives do not establish permanence; their complete inverse is
> an allowed reconnection.

It is not the broader statement that permanent Records are impossible in a
reversible substrate.  Once a carrier is lawfully a Record, the current Record
axiom supplies permanence.  A candidate physical law may restrict the Record
sector, export the fact beyond the bounded reconnection cone, or make the
inverse initial condition unavailable.  Cycle 283 tests none of those routes
as a selected law.

## 4. Exact deletion and fault controls

### Causal deletions

- **Whole instrument deletion:** deleting the contact coupling and its
  performed token yields no valid archive and no close.
- **Close deletion:** archives may exist but `CLOSE=0`.
- **Uncompute deletion:** the pointer remains working data,
  `UNCOMPUTED=0`, and close is blocked.
- **Middle-link deletion:** later validity cannot propagate, so close is
  blocked at held-out depth.

These show that the displayed close has the declared circuit ancestry.

### Split false-close

The critical Cycle-279 fault removes both data contact-pointer couplings while
leaving `DONE`, archive copying, uncompute token, and close logic alive.  The
pointer remains zero.  Every archive cell receives the mutually consistent
packet `(valid=1,value=0)`, and close forms with unit weight.

Redundancy therefore amplifies the supplied control path; it does not prove
that the Cycle-278 matter interaction occurred.  This remains a conditional
fault grammar.  An indivisible physical update or verified syndrome route is
live and untested.

### Local and correlated archive faults

Flipping one middle value after writing makes neighboring values disagree and
the close rejects it exactly.  Flipping every value is a correlated logical
fault: all values still agree, close has unit support, and every archived
outcome is wrong.  The construction therefore detects the declared single
local value fault, not arbitrary correlated faults.

No minimum redundancy or universal fault-tolerance claim follows.

The cold finite residuals are:

| diagnostic | exact/numerical result |
|---|---:|
| maximum inverse residual over depths `1,2,3,5` | `0.0` |
| whole-instrument close weight | `0.0` |
| middle-link-deletion close weight | `0.0` |
| uncompute-deletion close weight | `0.0` |
| split data-coupling false-close weight | `0.9999999999999998` |
| single local value-fault close weight | `0.0` |
| all-correlated value-fault close weight | `0.9999999999999998` |
| correlated wrong-archive weight | `0.9999999999999998` |
| minimum finite-history decoherence eigenvalue | `1/32` |

## 5. Fresh capacity and append-only continuation

A routed depth-`d` archive motif uses

\[
 3d+5
\]

role sites: pointer, `DONE`, `UNCOMPUTED`, value head, close, and three rails
for validity, value, and sequential status.  The radius is `d+1`.  Each finite
instance is bounded, but indefinite history needs unbounded fresh capacity or
a separate renewal/compression theorem.

Under the supplied append-only continuation grammar, old fact and close rails
are controls only; each continuation targets fresh blank rails.  Exact prefix
values are then unchanged.  At capacity exhaustion, reusing an occupied XOR
target toggles it.  On the explicit all-one history, the earliest value is
erased.  Target reuse is not a hidden append operation.

The controls-only grammar is a conditional continuation domain, not a
fundamental principle.  It shows how Record-compatible dynamics might be
specified.  It does not prove that the current admissibility rule generates
fresh sites, forbids all reconnecting gates, or supplies thermodynamic cost.

This is the explicit fresh-capacity growth result: routed role count is
`3d+5`, and no finite `d` is silently treated as an infinite tape.

## 6. Finite history cylinders

For each Cycle-278 contact weight `p`, define the repeatable coarse history
measure at depth `d` by

\[
 \mu_d(00\cdots0)=1-p,
 \qquad
 \mu_d(11\cdots1)=p.
\]

All other words have zero weight.  This is the repeated-projective-instrument
history of one fixed contact value.  The finite decoherence matrix is diagonal
and positive.  Marginalizing any tested larger depth to a smaller prefix gives
exactly the smaller measure.  The runner verifies this for all three rational
weights through held-out depth 5.

This is a legitimate projectively consistent finite history candidate.  It is
not an actual-history route.  For the fair comparator, the same normalized
measure admits distinct annotations `00000` and `11111`; the measure alone
does not select either member.  The current realized-state interface licenses
pointwise reference, while a complete history must be derived, uniquely
law-realized, reconstructed from Records, or supplied as contingent history
data.

No Born-frequency, typicality, or sampling conclusion is obtained from these
one-shot weights.

## 7. Covariant routed motif

The displayed archive ladder has three parallel nearest-neighbor rails:

```text
status_i -- status_(i+1)
   |              |
valid_i  -- valid_(i+1)
   |              |
value_i  -- value_(i+1).
```

The pointer attaches to the first validity and a value-head site; the final
status attaches to close.  All declared edges have Manhattan length one and
role sites are collision-free.  At depths `1,2,3,5`, the runner carries the
entire apparatus under all 24 proper-cubic frames and the full 27-element
translation group and rechecks collisions and every edge.

This is covariance of a supplied archive apparatus.  It is not a proof that
the Cycle-278 19-M2 contact neighborhood and this role ladder are generated
autonomously without routing conflicts by the one microscopic law.  That
combined placement remains a compiler task.

## 8. Repository Record/history endpoint comparison

### Current Record axiom

The current minimal framework says:

```text
Records form.
When present, a record locks exactly one admissible local possibility.
A site never carries more than one record; records are permanent.
Only records are readable.
```

Therefore generic occurrence, one-site locking, permanence, and content-only
readability are already ontology premises.  Cycle 283 must not demand a new
permanence axiom.  What it still owes is a retained bridge showing which
archive site becomes a Record, which admissible value it locks, and why the
split-spoofed close is rejected by the physical formation rule.

### Actuality/history endpoint

Cycle 27 separates one actual record/state reference from a complete history.
It requires a complete-history route when a law makes stochastic history
claims: derivation, law realization, Record reconstruction, or explicit
contingent data.  Cycle 283 supplies only consistent finite cylinders and no
distinguished member.

### Global process endpoint

Cycle 30 identifies the global-law fields needed beyond local copying:
protocol/event domain, positive normalized composition functional, identity
containment, Record decoder, record-fibre future-equivalence, boundary, and
actuality interface.  The Cycle-283 two-history measure covers only a tiny
closed repeatable protocol.  It supplies neither arbitrary intervention slots
nor a record-fibre future theorem.

### Record-derived replay endpoint

Cycle 48 proves replay on a declared finite class once preparation, program,
syndrome, and outcome records are already permanent and complete.  Cycle 283
does not supply that corpus.  Its archive packet could become an input to such
a replay theorem only after lawful Record typing and a complete decoder.

The exact bridge status is therefore:

```text
Cycle-278 same-code instrument
 -> Cycle-283 coherent redundant archive and consistent finite cylinders
 -> [open] fault-faithful Record decoder/formation rule
 -> [open] complete-history route and future-equivalence law.
```

## 9. Supplied-structure ledger

| supplied item | use | still not derived |
|---|---|---|
| Cycle-278 connected-code contact effect | physical-M2 instrument input | selected microscopic instrument law |
| `beta=-0.3`, `g=0.37` | actual fixture identity | energy, rate, or source meaning |
| three exact local state-family weights | archive marginals | bounded preparation of global same-code states |
| coherent witness across `Q=0/1` | reconnection stress state | physical preparation or parity-sector selection |
| blank pointer/archive/status sites | finite circuit boundary | autonomous freshness/reset |
| `DONE` and `UNCOMPUTED` tokens | causal close | faithful physical generation |
| archive copy and consistency gates | redundancy and fault test | selected nearest-neighbor law |
| all-24/full-27 carried motif | covariance control | autonomous origin/orientation removal |
| controls-only continuation grammar | append-only prefix preservation | fundamental permanence dynamics |
| finite two-history measures | projective history control | Born law, actual member, or arbitrary-process functional |
| split/local/correlated fault families | adversarial domain | universal physical noise model |
| current Record clauses | typing consequence once a Record exists | decoder selecting which candidate becomes a Record |

No pointer preparation rate, branch sampler, Born rule, typicality rule,
physical clock, metric duration, energy, source, stress tensor, gravity law,
or thermodynamic capacity law is supplied.

## 10. All-five-lane bridge consequences

### Operational quantum / Records

Gain: the exact same-code contact instrument now has redundant finite archives,
causal ancestry, local fault detection, inverse controls, and consistent
history cylinders.  Boundary: coherent candidate packets have not earned
Record typing; Record supplies permanence after Record typing, not the decoder
or formation value.

### Causal time / clock

Gain: close follows the partial order `interaction -> copy -> uncompute ->
consistency -> close`, never timeout.  Boundary: archive depth, circuit layer,
prefix length, and Record count are not metric duration or a clock rate.  No
clock-rate or cross-clock law is derived.

### Inertia / matter

Gain: the archive is attached to the actual contact-support observable and
does not rename the one-particle mass fixture.  Boundary: no recoil,
post-interaction packet, inertia shift, or matter preparation law is derived.

### Gravity / source / resource

Gain: fresh capacity cost is exposed as linear routed-site growth `3d+5`.
Boundary: site count is not physical energy, entropy, stress, source, lapse,
or gravity response.  No resource-to-source bridge is supplied.

### Born / probability / realized history

Gain: the three rational one-shot weights extend to normalized projectively
consistent finite cylinders.  Boundary: no Born-frequency law, typicality,
sampler, or actual-history member is selected.

## 11. Fresh N1–N8 discipline

The narrow negative boundary is: the displayed redundant coherent archives,
under the tested unrestricted reversible domain, do not by themselves earn
Record typing or unrestricted permanence.  This is not a universal
permanence/Record no-go.

### N1 — Alternative-route enumeration

| route | marker | attempt and disposition |
|---|---|---|
| one through held-out five redundant valid/value copies | ATTEMPTED | close and marginals succeed, but the exact inverse erases every copy; this matches the reversible-copy boundary of [Cycle 279](./LOCAL_INSTRUMENT_TO_RECORD_CLOSE_TOURNAMENT_CYCLE279_NOTE_2026-07-17.md) |
| causal close with middle-link/uncompute deletion | ATTEMPTED | exact ancestry succeeds; it establishes bounded completion, not Record typing, matching [Cycle 209:118–179](./COHERENT_CAUSAL_CLOSE_DETECTOR_COMPILER_CYCLE209_NOTE_2026-07-16.md) |
| split data-coupling deletion | ATTEMPTED | redundant archives false-close on a consistent `NO`, directly matching [Cycle 279](./LOCAL_INSTRUMENT_TO_RECORD_CLOSE_TOURNAMENT_CYCLE279_NOTE_2026-07-17.md) |
| single local archive-fault detection | ATTEMPTED | consistency rejects one flipped value but the all-correlated flip passes, so no universal fault tolerance is claimed |
| controls-only fresh append continuation | ATTEMPTED | old prefixes are exact invariants, but the continuation restriction and blank capacity are supplied |
| finite projectively consistent history cylinders | ATTEMPTED | normalization and marginals succeed; two actual-member annotations remain compatible with one measure, matching [Cycle 27:132–194](./STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md) |
| finite-capacity target reuse | ATTEMPTED | XOR reuse erases an occupied value and is not append-only growth |

Live routes not misclassified as failures are: a Record-typed absorbing sector,
an indivisible fault-faithful interaction/close, unbounded outward export, a
global actual-history law, and record-derived replay on a complete corpus.
Those routes make a broad no-go premature.

### N2 — Wall-independence audit

The collapsed open bridge interfaces are:

- `W_I`: select/prepare the same-code instrument and blanks;
- `W_F`: fault-faithful decoder and lawful Record formation/typing;
- `W_H`: complete-history consistency, fresh capacity, and record-fibre
  continuation;
- `W_P`: Born/frequency or other empirical probability bridge; and
- `W_T`: metric clock/rate comparison.

| pair | first closes second? | second closes first? | independent here? |
|---|---:|---:|---:|
| `W_I/W_F` | no | no | yes |
| `W_I/W_H` | no | no | yes |
| `W_I/W_P` | no | no | yes |
| `W_I/W_T` | no | no | yes |
| `W_F/W_H` | no | no | yes |
| `W_F/W_P` | no | no | yes |
| `W_F/W_T` | no | no | yes |
| `W_H/W_P` | no | no | yes |
| `W_H/W_T` | no | no | yes |
| `W_P/W_T` | no | no | yes |

Record permanence is not counted as another wall: it follows from lawful
Record typing already supplied by the Record axiom.  The task is the bridge to
that type and compatible history, represented by `W_F/W_H`.

### N3 — Hidden-condition scan

| phrase/condition | classification |
|---|---|
| “same-code” | exact Cycle-278 contact effect and weights; archive routing is a carried apparatus, not a new code theorem |
| “redundant” | repeated coherent value copies, not independent interactions or observers |
| “valid” | supplied circuit bit, not proof that the matter interaction occurred |
| “close” | reversible consistency predicate with declared ancestry, not branch actuality |
| “append-only” | controls-only target grammar and fresh blanks, not a theorem of the microscopic law |
| “permanent” | foundation consequence after lawful Record typing; not inferred from copy count |
| “history” | finite cylinder family, not a selected complete physical history |
| “capacity” | explicit role-site count, not thermodynamic energy/source |
| “weight” | exact trace/instrument value, not Born frequency or rate |

The required phrases “we assume,” “by construction,” “as is standard,” “the
framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical” carry no hidden
load-bearing premise.  Every scientific input appears in the supplied ledger.

### N4 — Residual matching

| witness | witness residual | Cycle-283 residual | match? |
|---|---|---|---:|
| [Minimal axioms: Record](../../../MINIMAL_AXIOMS_2026-06-29.md) | Records form; when present they lock one admissible possibility permanently; formation value/rule/rate remain outside | do not count permanence as missing; test whether archive earns lawful Record typing | yes |
| [Cycle 278:1–86, 246–318](./CONNECTED_EDGE_SAME_CODE_LOCAL_INSTRUMENT_CYCLE278_NOTE_2026-07-17.md) | same-code contact instrument exists; occurrence/close/permanence remain open | fixed physical input and exact rational archive marginals | yes |
| [Cycle 279](./LOCAL_INSTRUMENT_TO_RECORD_CLOSE_TOURNAMENT_CYCLE279_NOTE_2026-07-17.md) | candidate fact/close is reversible and split-spoofable | repeat the split fault after redundant archive consistency | yes |
| [Cycle 27:90–153, 155–194](./STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md) | actual state reference does not automatically give complete history; measure does not select member | finite consistent cylinders plus two annotations | yes |
| [Cycle 30:96–168, 357–383](./GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md) | global process needs domain, composition, containment, decoder, future-equivalence, boundary, actuality | identify which fields the tiny repeatable history does not supply | yes |
| [Cycle 48:121–181, 227–278](./RECORD_DERIVED_COHERENT_CARRIER_DECODER_CYCLE48_NOTE_2026-07-14.md) | complete permanent preparation/program/outcome records replay a finite class | archive lacks lawful permanent corpus and complete decoder | yes as endpoint, not negative witness |

The compiler, mass, gravity, and Born residuals are not used as evidence
against possible Record formation.

### N5 — Resolution and rhetoric audit

| resolution | tested | not established |
|---|---|---|
| one Cycle-278 contact cell | exact `Q` reconstruction and three weights | bounded preparation or full same-code dynamics |
| one archive pair | coherent copy, close, inverse | Record typing or independent witness |
| depths `1,2,3,5` | redundancy, deletions, inverse, prefix cylinders | arbitrary depth or indefinite capacity |
| one routed apparatus | all-24/full-27 carried covariance | autonomous combined code/apparatus placement |
| single and all-correlated value faults | exact rejection/pass | arbitrary noise or fault-tolerance threshold |
| finite history cylinders | positivity, normalization, consistency | actual complete member or arbitrary interventions |
| full lattice/all continuations | not tested | no universal permanence or Record no-go |

“Pointer copying is not a Record” is explicitly scoped: the displayed
coherent copy operation alone does not satisfy the bridge into the existing
Record type.  It does not say no copied carrier can become a Record after a
lawful formation rule.

### N6 — Partial-closure path scan

| constructive route | could close | remaining audit |
|---|---|---|
| indivisible contact-plus-validity update | `W_F` split fault | physical synthesis and declared fault domain |
| local syndrome tied to actual contact current | `W_F` | information/disturbance and false-negative controls |
| absorbing Record-typed sector under admissibility | typing/permanence bridge | derive which site/value forms without contradicting reversibility domain |
| outward fresh-carrier export | part of `W_H` capacity/reconnection | unbounded growth, collisions, energy/resource ledger |
| compression/renewal with preserved decoder | part of `W_H` | exact information loss and replay theorem |
| global process/history functional | complete-history law | local generation, decoder, actual member, empirical probability |
| Record-derived program/outcome replay | future sufficiency | complete lawful record corpus and process grammar |

These are import-retirement routes.  The current Record axiom already supplies
permanence after typing, so no new permanence axiom is requested.

### N7 — Steelman

> A hostile reviewer should reject any universal negative inference.  The
> runner grants unrestricted inverse gates on coherent candidate rails and
> then observes that they are reversible.  But the framework's Record sector
> is defined to be permanent once a Record forms.  A selected admissibility
> law could make the contact interaction and first validity token one
> indivisible local event, lock the resulting admissible archive value as a
> Record, and export it outward into fresh carriers.  In that sector the
> inverse used here would simply not be a lawful continuation.  Cycle 30 also
> leaves a global process route, and Cycle 48 shows that complete permanent
> record programs can replay coherent finite dynamics.  The missing work is a
> decoder/formation theorem and law synthesis, not evidence that permanence
> or record-only history is impossible.

The steelman is convincing.  The broad no-go fails.  Only the displayed
reconnection, split-fault, capacity, and finite-history dispositions are
retained.

### N8 — Cross-cycle echo

Earlier reversible-export cycles exposed fresh capacity rather than forcing a
Record edit.  The causal-close cycle separated completion from timeout.  The
pointer/archive cycles separated coherent copy, dephasing, uncompute, and fine
archives.  The gate-close and local-instrument cycles then exposed split
faults while retaining indivisible-update routes.  The global-history and
record-derived replay cycles show two constructive endpoints once complete
law/Record fields are supplied.

Cycle 283 follows the same successful pattern: enlarge the finite apparatus,
test the new resource exactly, and keep its selection/typing import visible.
Similar walls have been retired by a local decoder, a restricted lawful
sector, or a richer exact-law object.  Those mechanisms remain live, so there
is no axiom pressure.

## 12. Disposition and next route

Retain:

- exact Cycle-278 contact effect and three rational archive weights;
- redundant valid/value archive with pointer uncompute and causal ancestry;
- held-out size/depth controls;
- exact unrestricted inverse at every tested depth;
- whole, close, uncompute, link, split, local-fault, and correlated-fault
  controls;
- linear fresh-capacity ledger and target-reuse failure;
- positive normalized projectively consistent finite cylinders;
- all-24/full-27 archive-motif covariance; and
- exact comparison with current Record, actuality, global-history, and replay
  endpoints.

Do not claim:

- redundant pointer copies are Records;
- the controls-only continuation grammar is fundamental;
- close proves contact occurrence on the split fault domain;
- local consistency gives universal fault tolerance;
- finite cylinders select an actual member;
- one-shot trace weights yield Born frequencies;
- archive depth is physical time or a clock rate;
- role-site growth is energy or gravity source; or
- a shared obstruction, minimum content, or axiom need.

The optimal next route is a fault-faithful Record decoder: synthesize one
indivisible local contact/validity event on the same physical code, map its
outcome to an admissible Record site under the actual rule, and prove that all
lawful continuations preserve that Record while split faults fail to form it.
Then attach either a complete-history reconstruction theorem or one explicit
global process functional.  Fresh capacity, probability/frequency, and clock
normalization remain separate ledgers.

There is no Born-frequency derivation, no actual-history route, and no
clock-rate law in Cycle 283.  Pointer copying is not a Record.
