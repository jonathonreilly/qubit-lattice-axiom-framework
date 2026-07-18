# Contact archive finite-process/history law — Cycle 284

Date: 2026-07-17

Authority: none

Audit: unset

Lane: constructive realized-history endpoint probe

Runner: `scripts/contact_archive_finite_process_history_cycle284_2026_07_17.py`

## Result

There is an exact finite-domain process/history extension of the Cycle-278
same-code contact instrument and the Cycle-283 finite archive cylinders.  On a
declared four-dimensional subspace of the physical six-mode cell, a finite
protocol/event domain has:

1. a normalized positive composition functional;
2. identity containment;
3. exact event coarse-graining;
4. a Record decoder candidate which replays a complete finite packet; and
5. record-fibre future-equivalence through a tomographically complete set of
   fifteen two-qubit Pauli tests, including held-out protocol depth 4.

This is a constructive finite endpoint, not a complete history law.  Lawful
Record typing is supplied, as are preparation and instrument availability.
There is no Born-frequency interpretation, no actual member is selected, and
no clock-rate law is supplied.  The result therefore creates no
route-independent obstruction and no axiom pressure.

## Physical input and declared finite domain

Cycle 278 supplied the exact contact-active projector

\[
Q=\mathbf 1_{N_x\geq 2}
\]

on the 64-dimensional six-mode cell and its same-code coherent pointer
instrument.  The rank is 57.  The present runner restricts that exact effect to
the four physical occupation vectors

\[
(000000,000001,000011,000101),\qquad Q=(0,0,1,1).
\]

The first effective bit is the coarse contact value and the second labels a
fine state inside each contact sector.  This is a restriction of the actual
Cycle-278 projector, not a replacement contact oracle.  Cycle 283 supplies the
repeatable coarse archive cylinder at depth five,

\[
\mu(00000)=7/64,\qquad \mu(11111)=57/64.
\]

The finite protocol/event domain is explicit.  Its preparation alphabet is

\[
P=\{\texttt{cross_plus},\texttt{yes_fine_plus},
\texttt{generic_phase},\texttt{contact_basis}\},
\]

and each protocol slot uses one of the following five operations:

| symbol | event maps | meaning |
|---|---|---|
| `I` | \(\rho\mapsto\rho\) | identity |
| `Cs` | \(\rho\mapsto Q_q\rho Q_q\), \(q=0,1\) | selective coarse contact |
| `Cf` | \(\rho\mapsto\sum_q Q_q\rho Q_q\) | coarse outcome forgotten |
| `Fs` | \(\rho\mapsto R_{qr}\rho R_{qr}\), \(q,r=0,1\) | selective fine event |
| `Ff` | \(\rho\mapsto\sum_{qr}R_{qr}\rho R_{qr}\) | fine outcome forgotten |

Here \(R_{qr}\) are the four rank-one occupation projectors and
\(Q_q=\sum_rR_{qr}\).  Only syntactically lawful event labels are admitted.
The runner rejects negative depth and malformed outcomes.

## Normalized positive composition functional

For preparation \(p\), schedule \(s=(s_1,\ldots,s_d)\), compatible event
word \(h=(h_1,\ldots,h_d)\), and terminal effect \(E_t\), define

\[
W_p(t,h\mid s)=
 \operatorname{Tr}\!\left[E_t\,
 \mathcal K_{s_d,h_d}\circ\cdots\circ
 \mathcal K_{s_1,h_1}(\rho_p)\right].
\]

Every branch map is completely positive, every operation family sums to a
trace-preserving map, and each terminal Pauli pair
\(E_{a,\pm}=(I\pm\sigma_a)/2\) is positive and complete.  Thus
\(W_p\geq0\) and, for each fixed \((p,s)\),

\[
\sum_{h,t}W_p(t,h\mid s)=1.
\]

Training depths 1, 2, and 3 and the held-out protocol depth 4 are exhaustively
enumerated.  Depth four contains 26,244 event leaves over 2,500 fixed
preparation/schedule protocols.  The terminal suite is all fifteen nontrivial
two-qubit Paulis.  These trace weights are finite operational probabilities;
the runner makes no Born-frequency claim.

Selective-to-forgotten containment is exact:

\[
\sum_q\mathcal K_{Cs,q}=\mathcal K_{Cf},\qquad
\sum_{qr}\mathcal K_{Fs,qr}=\mathcal K_{Ff}.
\]

Identity containment is also exact: inserting `I` before, between, or after
any event in the complete depth-three domain leaves every unnormalised branch
state unchanged.

## Record decoder candidate and fibre theorem

The candidate complete packet is

\[
C=(p,((s_1,h_1),\ldots,(s_d,h_d))).
\]

The decoder starts from the recorded preparation and replays the named event
maps.  On the declared code space it reconstructs the exact unnormalised branch
state, hence its weight and conditional state.  Two raw archive
microhistories—redundant archive depths 1 and 5—are placed in the same complete
packet fibre.  Their decoded states have identical expectation values for all
fifteen Pauli testers.  Because those testers are tomographically complete for
the four-dimensional domain, this is finite-domain record-fibre
future-equivalence, not merely agreement on one chosen observable.

The word “candidate” matters.  The runner does not derive that such packets are
lawful Records, does not derive their formation, and does not derive their
permanent occurrence.  Lawful Record typing is supplied from the current
framework interface.  Conditional on that typing and on the declared process
alphabet, decoder replay is exact.

## Coarse/fine archive distinction and deletion tests

A visible coarse `YES` alone is not a sufficient history packet.  For

\[
|\psi\rangle=(|10\rangle+|11\rangle)/\sqrt2,
\]

coarse selective `YES` preserves the pure state, whereas fine measurement with
the fine value forgotten returns the incoherent mixture.  They have

\[
D_{\rm tr}=1/2,\qquad
\|\Delta\|_F=1/\sqrt2,
\]

and their future `IX` expectation values differ by exactly 1.  This is the
coarse/fine archive distinction: the same visible coarse value can hide
different future-bearing post-instrument states.

The runner then deletes candidate decoder clauses:

| deletion/merge | exact or bounded witness |
|---|---:|
| instrument status: identity versus coarse-forgotten | trace distance \(1/2\) |
| coarse versus fine forgetting status | trace distance \(1/2\) |
| fine result: `10` versus `11` | trace distance \(1\) |
| preparation record | trace distance greater than \(1/2\) |
| whole event, consistently replaced by `I` | residual \(0\) |
| split fault: physical omission but syntactic coarse-0 packet retained | trace distance \(1/\sqrt2\) |

The whole-deletion result is required by identity containment.  The split-fault
result reproduces the Cycle-279/Cycle-283 lesson: syntax without faithful
physical coupling can false-close, so the candidate decoder is not itself a
Record-formation law.  Record-fibre sufficiency survives held-out depth and
redundant archive depth, but it does not survive deletion of preparation,
instrument status, or fine event data when those data affect the future state.

## Boundary inventory

The construction closes the following fields only on its declared finite
domain:

| field | disposition |
|---|---|
| protocol/event domain | explicit and finite |
| positive normalized composition | exact trace/Kraus functional |
| identity containment | exact at all insertion positions tested |
| event coarse-graining | exact for coarse and fine instruments |
| complete-packet decoder | exact replay on lawful packets |
| record-fibre future equivalence | exact for all fifteen Pauli testers |
| held-out protocol depth 4 | exhaustive pass |

The boundary inventory remains:

1. The four preparations and five operations are supplied apparatus structure;
   the physical M2 compiler does not yet generate this full control alphabet.
2. The trace/Kraus rule is supplied operational quantum structure.  It is not
   derived from the common substrate here.
3. Lawful Record typing, occurrence, permanence, and faithful physical
   formation are supplied rather than derived.
4. The candidate packet contains preparation, program/status, and event value;
   no compression theorem establishes a globally minimal packet.
5. The finite protocol family is not a global projective-limit process, and no
   theorem covers arbitrary apparatuses or arbitrary future interventions.
6. No energy resource, inertial load, gravity/source term, or backreaction is
   attached to archive formation.
7. No clock-rate or waiting-time law is present.
8. The weights have no Born-frequency, typicality, or empirical convergence
   theorem.

## Actuality inventory

For `cross_plus` followed by selective coarse contact, the law assigns two
nonzero cylinders,

\[
W(0)=W(1)=1/2.
\]

Either outcome label can consistently annotate an actual run after the fact,
but the functional contains no rule selecting one annotation.  No actual
member is selected.  The actuality inventory is therefore:

| actuality field | disposition |
|---|---|
| admissible finite alternatives | explicit |
| normalized alternative weights | explicit |
| conditional replay after a supplied event label | exact |
| occurrence/selection of one event | open |
| extension to one complete realized history | open |
| reconstruction from already-lawful permanent Records | finite candidate only |

This respects Cycle 27: a normalized measure is not the actual state or the
actual complete history.  It also sharpens Cycle 30 by filling its finite
protocol, composition, containment, decoder, and finite-fibre fields without
claiming the global endpoint.  It agrees with Cycle 48: replay works once
preparation, program/status, and outcome records are already available, while
the law of their formation and actuality remains outside the result.

## Supplied-structure inventory and TOE consequences

Supplied structure is: the Cycle-278 contact projector; the four-state
restriction; Hilbert-space tensor coordinates; four preparation matrices;
Kraus composition and trace evaluation; the five-operation alphabet; the
fine/coarse projectors; classical packet syntax; all fifteen Pauli future
tests; and lawful Record typing.  None is silently promoted to a substrate
derivation.

Consequences for the framework lanes are correspondingly bounded:

- operational quantum/records: a finite exact process and candidate replay
  theorem, with faithful Record formation still open;
- causal time: ordered finite slots are supplied, but no endogenous causal
  clock or rate is derived;
- inertia/matter: the contact-active matter sector is used, but inertia and
  resource cost are untouched;
- gravity/source: no archive source or gravitational response is derived;
- Born/probability: positive normalized finite weights exist, with frequency,
  typicality, and actuality still open.

## Fresh no-go discipline (N1–N8)

No impossibility theorem is claimed.  This audit is included because the
coarse-only and actuality endpoints are negative/boundary statements.

### N1 — Alternative-route enumeration

| route | status | evidence |
|---|---|---|
| complete preparation/program/event packet replay | ATTEMPTED; exact on declared domain | maximum decoder residual tested at depths 1–4 |
| identity containment | ATTEMPTED; exact | all four insertion positions for every depth-three leaf |
| held-depth extension | ATTEMPTED; exact | exhaustive depth 4, not a depth-three fit |
| redundant raw archive depth | ATTEMPTED; exact | depth-1 and depth-5 microhistories share decoded fibre |
| coarse-only archive | ATTEMPTED; insufficient | exact `IX` future witness of 1 |
| decoder clause deletion | ATTEMPTED; insufficient | status, fine value, and preparation witnesses above |
| physical/syntactic split fault | ATTEMPTED; false-close | decoder trace-distance residual \(1/\sqrt2\) |
| normalized functional as actual-member selector | ATTEMPTED; underdetermines | two labels carry weight \(1/2\) with no selection field |

The successful complete-packet and held-depth routes keep any broad no-go
premature.  The failed coarse-only, deletion, and split routes establish only
route-specific insufficiency.

### N2 — Wall-independence audit

Use the wall set

- \(W_L\): physical law selecting preparations and process operations;
- \(W_R\): lawful Record typing, formation, and permanence;
- \(W_H\): extension to arbitrary depth/apparatus and global future fibres;
- \(W_A\): selection or reconstruction of the actual complete history;
- \(W_P\): Born-frequency/typicality bridge;
- \(W_T\): endogenous clock and rate law.

All fifteen pairwise comparisons are non-identities:

| pair | reason they are not the same wall |
|---|---|
| \(W_L,W_R\) | a map can be physically available without forming a lawful permanent Record |
| \(W_L,W_H\) | a finite law alphabet need not extend to arbitrary apparatus/depth |
| \(W_L,W_A\) | specifying alternatives does not select the realized alternative |
| \(W_L,W_P\) | process maps do not imply long-run frequencies |
| \(W_L,W_T\) | operation order does not supply duration or rate |
| \(W_R,W_H\) | local lawful packets do not imply global fibre consistency |
| \(W_R,W_A\) | permanent records may reconstruct part of history without selecting all unrecorded facts |
| \(W_R,W_P\) | record occurrence does not prove a frequency theorem |
| \(W_R,W_T\) | permanence does not specify clock intervals |
| \(W_H,W_A\) | a global process measure can still contain many candidate histories |
| \(W_H,W_P\) | projective consistency does not establish empirical typicality |
| \(W_H,W_T\) | arbitrary-depth consistency does not define physical elapsed time |
| \(W_A,W_P\) | one actual history can exist without a frequency bridge |
| \(W_A,W_T\) | selection of events does not fix their rates |
| \(W_P,W_T\) | frequencies and waiting-time dynamics are logically separable |

Cycle 284 directly softens the finite parts of \(W_H\) and decoder replay, but
none of the other walls is thereby removed.  Treating them as one common
obstruction would overstate the evidence.

### N3 — Hidden-condition scan

The proof assumes: exact projectors; ideal CP maps; exact preparation labels;
exactly faithful program/status and outcome fields; no archive noise beyond the
tested split case; a fixed tensor coordinate; the declared five-operation
alphabet; finite depth; trace-rule evaluation; and lawful Record typing.  A
global theorem would additionally need compatibility under arbitrary protocol
refinement, apparatus composition, and future intervention.  These are
boundary conditions, not derived facts.

### N4 — Residual matching

The conclusions match the measured residuals:

- Cycle 278 supplies an exact rank-57 contact projector and pointer instrument;
- Cycle 283 supplies exact finite coarse cylinders and exposes correlated
  archive/split false-close;
- Cycle 284 obtains zero decoder and identity residuals on its finite domain;
- Cycle 284 obtains nonzero exact coarse/fine and clause-deletion witnesses;
- Cycle 27 distinguishes normalized history weight from actual history;
- Cycle 30 lists the process fields filled here and the global fields still
  open; and
- Cycle 48 already shows finite replay conditional on complete lawful records.

Nothing in those residuals proves that a different physical formation law,
global-process construction, actuality law, or frequency theorem cannot close
the remaining fields.

### N5 — Resolution and rhetoric audit

The warranted resolution is: “finite exact process/decoder construction with
explicit supplied boundaries.”  The coarse-only result is called
“insufficient on the tested domain,” not impossible.  The absence of a
selection rule is called an unfilled field, not proof that actuality cannot be
derived.  No finite trace weight is renamed a frequency, and a decoded packet
is not called a Record unless lawful typing is separately supplied.

### N6 — Partial-closure path scan

Several live partial-closure routes remain:

1. compile the operation/status alphabet and redundant archive into local M2
   dynamics, then rerun split/noise tests;
2. extend the family by compatible restriction maps and test projective
   consistency at increasing depth;
3. derive a physical record-formation criterion with energy/resource and
   stability bounds;
4. test sufficient-statistic packet compression over larger instrument
   alphabets; and
5. separately probe actuality and typicality without treating either as a
   consequence of finite normalization alone.

The present complete-packet replay and held-depth pass are evidence that these
are constructive routes, not decorative escape clauses.

### N7 — Steelman

The strongest opposing position is that a local substrate law could jointly
generate apparatus programs, faithfully form permanent records, induce a
projectively consistent global process, and make the complete record fibre a
sufficient statistic for every lawful future intervention.  An additional
actuality or reconstruction law could then identify one realized history, and
a separate typicality theorem could connect its records to observed
frequencies.  Cycle 284 does not refute this position; its finite construction
is compatible with it.

### N8 — Cross-cycle echo

- Cycle 27 warns that measure does not choose the actual member.
- Cycle 30 supplies the process/history endpoint checklist used here.
- Cycle 48 shows exact finite replay when complete records are already given.
- Cycle 189 exposes the need for preparation/program/outcome fields in record
  reconstruction.
- Cycle 226 distinguishes coarse values from hidden future-bearing structure.
- Cycle 278 supplies the physical contact instrument.
- Cycles 279 and 283 expose whole-deletion versus split-fault semantics and
  finite archive false-close.

Across these echoes, the new contribution is the exact finite composition,
containment, complete-packet decoder, and held-depth fibre theorem on the
contact sector.  The repeated boundary is faithful Record formation and global
actuality, but constructive alternatives remain live.  Therefore the result
supports no route-independent obstruction and no axiom pressure.

## Disposition

Cycle 284 is green if and only if the runner verifies all exact finite-domain,
held-depth, deletion, split, boundary, actuality, and note-contract checks.
Even on green, authority remains none and audit remains unset.
