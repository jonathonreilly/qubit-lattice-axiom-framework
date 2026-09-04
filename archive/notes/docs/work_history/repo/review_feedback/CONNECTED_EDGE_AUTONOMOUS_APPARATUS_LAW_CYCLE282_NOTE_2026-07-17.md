# Connected-edge autonomous apparatus law — Cycle 282

**Date:** 2026-07-17

**Type:** exact bounded autonomous coherent-apparatus episode on the Cycle-278
same-code connected edge construction, with physical program markers, deletion,
recurrence, held-size, and actual-update compatibility controls

**Status:** positive conditional construction for a bounded episode; the role
word, one-hot token origin, apparatus blanks, insertion boundary, read effect,
and episode domain are supplied; contact occurrence, irreversible close,
Record formation, and homogeneous apparatus genesis remain open

**Authority: none**

**Audit: unset**

**Constitutional effect: none**

Companion runner:

```text
scripts/connected_edge_autonomous_apparatus_law_cycle282_2026_07_17.py
```

This cycle creates exactly this note and runner. It changes no axiom,
foundation, Qualification, primitive, registry, policy, queue, or audit-status
surface. It does not use or splice the Cycle-251 compiler.

## Result up front

There is a bounded autonomous local update on the Cycle-278 connected
physical-M2 code which, from a supplied blank apparatus and a supplied
phase/role marker, sequences

```text
pointer initialization/arming (conditional on the supplied blank)
-> contact-pointer coupling
-> coherent amplification
-> one-hot branch fact
-> amplifier clearing
-> pointer clearing
-> clean close
```

without host-side schedule control. The construction uses one fixed repeated
update. A one-hot program token moves through a twelve-position rail. At each
position, an immutable three-M2 physical role word selects one reversible
bounded gate. The first seven roles are

```text
INIT, COUPLE, AMPLIFY, FACT, UNAMPLIFY, UNCOUPLE, CLOSE,
```

followed by five `IDLE` positions. No host chooses a different operation at a
different composition of the update.

On the supplied blank, after seven compositions the two branches are exactly

| contact-active bit `q` | ready | pointer | amplifier | fact NO | fact YES | close |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 0 | 1 | 1 |

The contact-active bit is the Cycle-278 physical scalar

```text
Q_x = 1_(N_x >= 2),
```

on the same Cycle-269/271/275/278 connected edge code. It is the support
projector of the Cycle-230 contact generator, not physical energy. Pointer and
amplifier work registers are clean at close. The full update is an exact
permutation of the complete declared classical basis, and therefore defines a
unitary permutation matrix on the corresponding quantum basis.

This is a genuine improvement over a host-applied list of stage gates: the
sequencing information is carried by physical state and one law is repeated.
It is nevertheless conditional. The nonhomogeneous role word, token origin,
blank registers, apparatus placement, and episode boundary are not generated
from a homogeneously generated state. Covariance carries this supplied block;
it does not derive its genesis.

The strongest warranted label is **bounded autonomous coherent-apparatus
episode**. The pointer is not a Record. The one-hot fact bits and close bit are
also not Records. The close does not certify that the Cycle-230 contact
unitary occurred. Compiler iteration is not physical time. There is no shared
obstruction and no axiom pressure.

## 1. Exact fixed update

Let the six working apparatus bits be

```text
(r, p, a, f_0, f_1, c),
```

for ready, pointer, amplifier, the two one-hot fact candidates, and close. Let
`q` denote the eigenvalue of `Q_x`. At the token's current role site the fixed
update applies the corresponding reversible Boolean map:

```text
INIT:       r   <- r xor 1
COUPLE:     p   <- p xor q                    if r=1
AMPLIFY:    a   <- a xor p                    if r=1
FACT:       f_0 <- f_0 xor (1-a),
            f_1 <- f_1 xor a                  if r=1
UNAMPLIFY:  a   <- a xor p                    if r=1
UNCOUPLE:   p   <- p xor q                    if r=1
CLOSE:      c   <- c xor 1                    if r=1,
                                                  p=a=0,
                                                  f_0 xor f_1=1.
```

The token then shifts by one position on its cyclic rail. Role selection and
shift are parts of the same repeated update law. The runner exhausts

```text
2 contact values x 12 token positions x 2^6 apparatus words = 1536
```

inputs and obtains 1536 unique outputs for the intended role word and for
each single-role-deleted word. This checks reversibility on the full declared
basis rather than only on the blank trajectory.

The update is local in the bounded-block sense used in this campaign. The
matter support union plus six working registers is a 24-M2 data/working
footprint. The twelve token sites and 36 role-marker M2 sites are also
physical controls, so they must not be omitted from the support accounting.
The conservative declared neighborhood of the full repeated update is the
entire 72-M2 block. Thus

| resource | count |
|---|---:|
| matter support union | 18 M2 |
| working apparatus | 6 M2 |
| one-hot token rail | 12 M2 |
| three-bit role markers | 36 M2 |
| apparatus overhead | 54 M2 |
| full matter-plus-apparatus block | 72 M2 |
| data-plus-working footprint | 24 M2 |
| conservative maximum declared update neighborhood | 72 M2 |

Every count is independent of torus size. This is constant overhead and
bounded support, not a derivation of a preferred microscopic embedding for
the apparatus block.

## 2. Same connected code, states, and leakage

The construction receives the exact Cycle-278 Walsh realization of `Q_x` in
the six physical occupation-parity operators `B_(x,d)`. It does not replace
the code and does not import the Cycle-251 splice.

For every `L=3,4,5` and held-out `L=6`, the runner reconstructs the Cycle-275
fixed-Wilson stabilizer projectors in all eight Wilson sectors and their two
`B_0`-biased variants. There are 24 state rows per size. All state systems are
consistent and reproduce the exact Cycle-278 YES weights:

| state family | `Pr(Q_x=1)` |
|---|---:|
| uniform fixed-Wilson sector | `57/64` |
| fixed sector and `B_0=+1` | `13/16` |
| fixed sector and `B_0=-1` | `31/32` |

All 64 Walsh words commute with all bounded local checks and all three Wilson
operators. The apparatus control is diagonal in `Q_x`, so local-check and
Wilson preservation is exact: local-check leakage is zero and Wilson-sector
transition count is zero. The clean final pointer and amplifier do not erase
the coherent fact correlation.

This state test supplies a quantum trace pairing. It does not select one
branch in realized history and does not derive relative frequencies.

## 3. Proper-cubic covariance

At `L=3`, the runner combines all 24 proper-cubic frames with the full 27
translations, for 648 exact tests. The physical `B_(x,d)` family maps to the
family at the transformed cell, the complete local-check family is
preserved, and the Wilson center maps into itself.

`Q_x` depends only on total occupation, so it is a proper-cubic scalar. The
working apparatus, one-hot program token, physical role word, and phase origin
are carried as one bounded scalar apparatus block attached to the transformed
cell. There is no preferred spatial direction in the gate meanings.

This establishes covariance of the supplied apparatus family under all 24
proper-cubic frames. It explicitly does **not** establish homogeneous
unit-translation generation of a unique apparatus block or a unique token
origin.

## 4. Actual Cycle-230 contact/coin/stream interface

The runner uses the actual Cycle-230 fixture

```text
beta = -0.3,
g    = 0.37,
W_g  = exp(i g binom(N_x,2)),
```

and verifies, at intrinsic 64-dimensional cell resolution,

```text
[Q_x, Gamma(C_beta)] = 0,
[Q_x, W_g]           = 0,
[Q_x, Gamma(A)]      = 0.
```

The printed matrix residuals are zero. `Q_x=0` on `N_x<=1`, so the apparatus
acts as identity on the one-particle local sector and preserves the
Cycle-219/230 one-particle mass fixture to the inherited relative tolerance
below `2e-12`.

An actual three-mode intercell fermionic swap gives

```text
||[Q_local, FSWAP]||_F = sqrt(2),
||[Q_local, FSWAP]||_2 = 1.
```

Therefore the stream can change the local contact-active condition. The
apparatus episode must be inserted at a supplied boundary of the actual A/B
stream schedule. The fixed apparatus law removes host selection among its
seven internal roles; it does not derive that external insertion boundary.
The actual Cycle-230 contact/coin/stream compatibility is therefore exact but
conditional.

## 5. Deletion and faithfulness controls

Single-role deletion distinguishes every internal clause. On the active
branch, deleting any one of `INIT`, `COUPLE`, `AMPLIFY`, `FACT`, `UNAMPLIFY`,
`UNCOUPLE`, or `CLOSE` prevents a clean close. In particular, deleting only
`COUPLE` leaves the still-present `UNCOUPLE` to write the pointer; the close
cleanliness check detects that asymmetric defect.

Two sharper deletion controls set the semantic boundary:

1. Deleting **both** `COUPLE` and `UNCOUPLE` leaves the workspace clean,
   writes `fact NO`, and raises close even for an input with `q=1`. This is a
   split-data-coupling false close. The close verifies internal workspace
   consistency, not that a data coupling actually happened.
2. Replacing the actual `W_g` contact phase by identity has matrix residual
   `||W_g-I||_F = 9.750456122278623`, but leaves `Q_x` and the complete active
   apparatus packet unchanged on a tested `N=2` state. Thus the apparatus
   detects the support condition for contact; it does not detect application
   of the physical contact unitary.

Consequently `fact YES` means “the supplied `Q_x` coupling found
`N_x>=2`,” not “the Cycle-230 interaction occurred.” A faithful occurrence
close would need an additional locally checked coupling between the actual
interaction event and close, or a different indivisible update architecture.
That is an open constructive route, not a demonstrated impossibility.

The homogeneous controls also fail as they should: replacing the role word by
all `IDLE` or all `INIT`, moving the initial token phase, starting with a
nonblank pointer, or deleting token motion does not produce the intended
close. These tests explicitly separate a supplied phase/role marker from a
homogeneously generated state.

## 6. Finite-register recurrence and lawful domain

The physical program rail is finite and the update is reversible. Continuing
the same law beyond the declared episode therefore revisits active roles. On
both contact branches:

| event in update-composition count | first composition |
|---|---:|
| clean close appears | 7 |
| fact/close packet first changes | 28 |
| close bit is first lost | 55 |

The twelve-position program has period twelve, but the coupled apparatus
state has the longer displayed recurrence. The construction supports a
bounded read window; it does not provide unrestricted permanent storage.

Possible constructive repairs include an outgoing nonreturning program
carrier, a semi-infinite or freshly extended rail, a dynamically sealed
absorbing sector embedded in a larger reversible system, or transfer into the
actual Record-forming lane. Each imports additional structure and must be
tested. Finite-register recurrence is not a broad no-go against autonomous
apparatus laws.

The runner rejects an invalid contact value, a token outside the declared
rail, and an unknown role word. Its lawful domain is the supplied connected
code, valid one-hot token sector, binary working registers, declared role
alphabet, and finite episode window.

## 7. Supplied-structure inventory

The exact construction supplies all of the following:

| supplied item | use | not derived here |
|---|---|---|
| Cycle-269/271 connected physical-M2 code | physical realization of the six `B` operators | selection or preparation of the code |
| Cycle-275 sector projectors | exact input density operators for tests | bounded preparation of those global states |
| Cycle-278 `Q_x` effect | contact-active control | microscopic selection of this observable |
| twelve-site apparatus rail and its bounded placement | carries program token | apparatus genesis from homogeneous data |
| one-hot token and phase origin | selects the first role | unique origin or spontaneous token production |
| three-M2 role code at every rail position | physical instruction data | homogeneous role-word generation |
| blank ready, pointer, amplifier, fact, and close bits | lawful episode input | autonomous reset from arbitrary state |
| one repeated conditional permutation law | moves token and executes roles | derivation from a more primitive selected law |
| fresh coherent apparatus degrees of freedom | stores correlations | thermodynamic resource account |
| apparatus insertion boundary relative to A/B stream | fixes which `Q_x` is sensed | selection by the law |
| seven-composition close window | defines the bounded episode | unrestricted permanence |
| supplied trace/read effect | interprets branch statistics | occurrence or branch selection |
| Cycle-170/243/255/279 Record interfaces | receiving criteria for later work | an actual close-to-Record map here |

No host-side schedule chooses the seven internal actions. `INIT` arms a
supplied blank pointer; it does not reversibly reset an arbitrary pointer.
That improvement does not erase the listed boundary conditions.

## 8. Record and causal-time receiving endpoint

Cycle 170 defines causal depth only on a graph of actual Record dependencies.
Cycle 243 requires the typed chain from physical close through commit and
Record before named counts can feed a time matcher or calibration. Cycle 255
keeps macro-role generation and close faithfulness open. Cycle 279 supplies a
useful independent deletion comparator: a coherent close candidate can
survive a split coupling deletion and therefore fail occurrence faithfulness.
Cycle 279 is receiving-endpoint evidence only; its generic apparatus is not
imported into this same-code construction.

This cycle has coherent carriers and a close candidate, but no actual Record,
no Record DAG, no commit law, and no permanent fact. Therefore it claims no
causal depth and no duration. The program position is a physical control
state; it is not a clock reading. The order of update compositions is circuit
ancestry; compiler iteration is not physical time. The pointer is not a
Record, and copying the pointer would not by itself make one.

## 9. Prior-art and novelty boundary

Physical program tapes, moving heads or clock registers, and reversible
computation are established ideas. Relevant bounded prior art includes:

- P. Benioff, “The computer as a physical system: A microscopic quantum
  mechanical Hamiltonian model of computers as represented by Turing
  machines,” *Journal of Statistical Physics* **22**, 563–591 (1980),
  DOI `10.1007/BF01011339`.
- R. P. Feynman, “Quantum mechanical computers,” *Optics News* **11**(2),
  11–20 (1985), DOI `10.1364/ON.11.2.000011`.
- M. A. Nielsen and I. L. Chuang, “Programmable quantum gate arrays,”
  *Physical Review Letters* **79**, 321–324 (1997),
  DOI `10.1103/PhysRevLett.79.321`.

This cycle does not claim novelty for one-hot program control, reversible
gate sequencing, coherent pointers, or programmable quantum dynamics. Its
repo-local contribution is the exact integration of such a bounded physical
sequencer with the Cycle-278 same connected physical-M2 code, including all-24
proper-cubic carried covariance, exact sector-state weights through held-out
`L=6`, actual Cycle-230 contact/coin/stream tests, split-coupling and
contact-deletion controls, and explicit recurrence and Record/time firewalls.

## 10. N1–N8 no-go discipline

No impossibility, minimum-content, or axiom-pressure claim is shipped. The
negative boundaries below receive the full N1–N8 stress test.

### N1 — Alternative-route enumeration

At least eight materially different routes or controls were considered:

1. **Physical role-word route:** succeeds for one bounded episode with one
   fixed repeated update.
2. **Host-applied stage list:** can reproduce the same Boolean maps but is
   rejected as the target because the host supplies each stage selection.
3. **Homogeneous role words:** all-`IDLE` and all-`INIT` words fail to produce
   the intended close; no homogeneous-generation theorem follows.
4. **Wrong or stationary token:** shifted origin, nonblank pointer, and
   deleted token motion fail, demonstrating marker load bearing.
5. **Single-role deletion:** every single active-role deletion prevents clean
   close on the active branch.
6. **Split data-coupling deletion:** deleting both forward and inverse data
   couplings produces a false clean `NO` close; internal cleanliness is not
   occurrence faithfulness.
7. **Actual-contact deletion:** replacing `W_g` by identity leaves the
   `Q_x`-conditioned packet unchanged; support sensing is not contact-event
   sensing.
8. **Finite cyclic continuation:** preserves a bounded read window but loses
   the close at composition 55.
9. **Outgoing-carrier or fresh-rail route:** remains open and could prevent
   recurrence without changing the successful bounded episode.
10. **Indivisible contact-plus-syndrome route:** remains open and could bind
    close to actual contact application rather than only to `Q_x`.

The first route is a constructive success. The failures of the others are
route-specific controls, not constitutional evidence.

### N2 — Condition-independence audit

Five distinct unresolved conditions are kept separate:

```text
K_role   = physical role word and token origin are supplied,
K_gen    = no homogeneous apparatus-generation law is derived,
K_event  = close is not faithful to actual W_g application,
K_store  = finite reversible recurrence defeats unrestricted permanence,
K_record = no commit, Record, or Record-DAG formation law is supplied.
```

All ten pairs are compared:

| pair | independent witness |
|---|---|
| `K_role/K_gen` | a supplied role word sequences correctly even though its homogeneous genesis is open |
| `K_role/K_event` | correct token sequencing coexists with actual-contact deletion blindness |
| `K_role/K_store` | correct markers give a bounded close but do not stop later recurrence |
| `K_role/K_record` | correct physical roles do not create a commit or Record |
| `K_gen/K_event` | even granting apparatus genesis would not make `Q_x` certify `W_g` |
| `K_gen/K_store` | apparatus genesis does not supply a nonreturning carrier or sink |
| `K_gen/K_record` | homogeneous apparatus formation would still not define Record closure |
| `K_event/K_store` | an occurrence-faithful close could still recur on a finite reversible rail |
| `K_event/K_record` | event faithfulness is necessary but not sufficient for Record formation |
| `K_store/K_record` | nonrecurrence or permanence alone does not provide typed Record dependencies |

None of these walls is inferred from another. The construction closes
host-selected internal staging while leaving five independent conditions
explicit.

### N3 — Hidden-condition scan

Hidden assumptions were searched in locality, initialization, geometry,
resources, semantics, and asymptotics. The scan exposed and now names:

- the twelve-site rail, its bounded placement, and three-bit role coding;
- the supplied phase origin and valid one-hot-token sector;
- five idle positions and the seven-composition episode window;
- blank work registers and fresh coherent storage;
- the external insertion boundary relative to the A/B stream;
- the trace/read pairing and classical labels `NO/YES`;
- carried proper-cubic covariance rather than homogeneous block genesis;
- finite cyclic recurrence after the bounded read window;
- distinction between sensing `Q_x` and witnessing actual `W_g` application;
- absence of a commit, irreversible sink, Record DAG, or probability law.

No resource in this list is renamed as emergent time, occurrence, or Record.

### N4 — Residual matching

Each residual is matched to the actual earlier result it addresses:

| earlier result | Cycle-282 relation |
|---|---|
| Cycle 278 same-code pointer coupling, read/reset open | preserves the exact same code and turns the coherent coupling into an internally sequenced bounded apparatus episode |
| Cycle 279 generic instrument-to-close tournament | independently supports the split-coupling false-close diagnostic; its apparatus is not imported |
| Cycle 243 typed time/Record bridge | supplies the receiving endpoint that this coherent close has not reached |
| Cycle 170 Record-defined causal depth | forbids interpreting program position or gate ancestry as causal duration |
| Cycle 255 macro-role and close-faithfulness residuals | physicalizes the roles conditionally but leaves their genesis and event faithfulness open |
| Cycle 230 actual contact/coin/stream | tested directly; onsite commutators vanish, stream ordering remains supplied, contact deletion is invisible to `Q_x` |
| Cycle 251 alternate code | deliberately excluded; no splice is used |

No generic simulator result is substituted for a same-code physical-M2 test.

### N5 — Resolution and rhetoric audit

The following phrases are permitted:

- “bounded autonomous coherent-apparatus episode”;
- “one fixed repeated reversible update”;
- “physical role word and one-hot program token”;
- “conditional on supplied markers, blanks, and insertion boundary”;
- “close candidate faithful to internal cleanliness and the `Q_x` branch.”

The following stronger phrases are rejected:

- “homogeneously generated apparatus law”;
- “the contact event was recorded”;
- “permanent fact” or “Record”;
- “program phase is time” or “update count is duration”;
- “autonomous realization of the whole Cycle-230 schedule”;
- “minimum apparatus content,” “impossibility,” or “axiom pressure.”

This is a positive bounded construction with named imports, not a broad
negative theorem.

### N6 — Partial-closure path scan

Several partial routes remain scientifically valuable:

1. replace the cyclic token by an outgoing nonreturning carrier and test the
   same exact close packet on growing held-out domains;
2. bind an event syndrome to the actual `W_g` application and make deletion of
   `W_g` prevent close;
3. derive a locally generated role texture from a lawful symmetry-breaking
   state rather than supplying it;
4. construct autonomous blank preparation/reset while retaining exact
   all-24 covariance;
5. couple the clean fact carrier to the Cycle-243 typed physical-close to
   commit to Record chain;
6. combine the apparatus insertion with the actual A/B stream law in one
   bounded autonomous update and rerun seam and held-size controls.

Any one of these could advance the framework without waiting for all five
conditions to close.

### N7 — Steelman

The strongest hostile reading is that the supplied role word is already a
legitimate physical state, so demanding homogeneous genesis may be too
strong; a lawful translationally invariant dynamics could nucleate or carry
such a localized program. Likewise, finite recurrence is an artifact of the
chosen cyclic rail: an outgoing program particle, fresh carrier chain, or
larger reversible environment can preserve a local close for arbitrarily long
lawful windows. Finally, contact faithfulness may be repaired by compiling the
contact and a close syndrome into one indivisible bounded gate rather than by
sensing the support projector afterward.

Those are live constructive alternatives. The present evidence does not rule
them out and therefore cannot support a broad no-go, a minimum-content
theorem, or axiom pressure.

### N8 — Cross-cycle echo

Earlier cycles repeatedly found that external stage lists, role labels, and
close semantics were supplied. Cycle 282 retires one important echo: the
seven internal apparatus stages can be selected by physical program state
under one repeated local update. The same evidence does **not** retire the
deeper echoes of program genesis, actual-event faithfulness, permanent
storage, or Record formation.

Because the remaining residuals separate under N2 and have open constructive
repairs under N6 and N7, they do not form a route-independent obstruction.
The result produces no axiom pressure.

## 11. Dependency-ledger effect and next experiment

This cycle improves the operational instrument/apparatus lane by replacing a
host-controlled internal sequence with one physical, bounded, reversible
sequencer on the same connected code. It does not change the gravity/source,
Born/frequency, inertia/matter, or causal-time receiving endpoints.

| dependency | Cycle-282 effect |
|---|---|
| `C_ref` | unchanged; actual reference/matcher interface remains supplied |
| `C_num` | unchanged; no named physical number or calibration is derived |
| `C_wrap` | unchanged; the apparatus is tested pre-wrap and through held size, not promoted to a wrap theorem |
| `C_int` | improved conditionally; one repeated physical update sequences the coherent instrument, but actual-contact occurrence faithfulness fails deletion |
| `C_local` | improved for a bounded episode; constant M2 overhead, exact code preservation, all-24 carried covariance, and no host-selected internal stage |
| `C_source` | unchanged; no source/resource law or gravity response is derived |

The highest-value next experiment is an **actual-contact-faithful outgoing
carrier**: compile `W_g`, a locally checked event syndrome, and a nonreturning
program/fact carrier into one bounded repeated update on the same code. Require
that deleting `W_g` prevents close, that the carrier does not recur on
held-out lengths, and that all-24 covariance, one-particle identity,
local-check/Wilson preservation, actual stream compatibility, and the typed
Record/time firewalls all remain exact.
