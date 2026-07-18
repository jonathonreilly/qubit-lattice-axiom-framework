# Physical M64 reversible event-parity sidecar — Cycle 314

Date: 2026-07-18

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit-status surface is edited or proposed.

Companion runner:

```text
scripts/physical_m64_reversible_event_sidecar_cycle314_2026_07_18.py
```

Methodology freshness: the no-go-discipline instructions were compared with a
freshly fetched `origin/main`; the newer `origin/main` text is followed here.
The dirty worktree was not moved.

## Result up front

Cycle 314 supplies a positive, bounded, physical-M2 input to the Cycle-243
event bridge. Add one additional ordinary M2 `h` per coarse cell to the
Cycle-311 common six-mode fixed seam. On the 510 role-gauge microsectors,
impose the local diagonal matrix-unit constraint

```text
C_hist = P_vac Z_h + P_nonvac Z_f Z_r Z_h = +1.
```

Here `f` is the Cycle-311 stream flag, `r` is its relational gauge companion,
and `P_vac` and `P_nonvac` are the already available local number projectors
on the declared microbasis. The vacuum term is essential: the shared vacuum
has `f=0` in both `r` branches, whereas a nonvacuum code vector obeys
`f xor r = t`, with `t` the logical fixed-seam slice.

The event-sidecar encoder is

```text
E_hist |n,S,t> = E_311 |n,S,t> tensor |h=t>.
```

It is a rank-127 constrained event-sidecar code inside a 1,020-dimensional
literal microbasis. The rank-254 `Cycle-311 shell tensor h` space has exactly
127 `C_hist=+1` directions, and those directions equal the columns of
`E_hist`.

Coin and contact act identically in the two `h` sectors. Literal physical
stream/catch-up flips `h` exactly when `n>0`:

```text
S_hist |q,h> = |S_311 q, h xor 1_(n(q)>0)>.
```

For the declared order coin, then stream/catch-up, then contact,

```text
E_hist G_coarse = G_hist E_hist.
```

The full composition intertwiner is below `2.0e-15`; the stream, contact,
constraint, and event decoder residuals are zero. The construction works at
trained `L=3,4,5`, held `L=6`, all 24 proper-cubic frames, and all 27 `L=3`
translations. It installs twenty-four M2 per cell and has observed total patch
support 45 M2, below the declared at most fifty-seven M2 envelope.

The controlled flip is one fixed local matrix-unit operator, not a host-side
branch instruction. No Jordan-Wigner string, global parity service, nonlocal
ordering, or preferred spatial direction is introduced.

The exact semantic result is a **binary update-parity carrier**. It is
event-ready: on the declared input slice `h=0`, every occupied fixed-seam
crossing reaches `h=1`, while vacuum stays at `h=0`. The readable carrier is
not an accumulated history index, not elapsed time, not occurrence, not a
commit, and not a Record. Two stream updates return `h` to its input value.
That erasure control forbids any claim of past-distinguishing memory or
permanence.

None of PR5469 Legs A, B, or C is closed. Leg A still needs a realized-history
origin and compactification or another physical causal-axis construction. Leg
B still needs an intrinsic axis label. Leg C still needs physical interval
spacing and a calibrated rate map. No axiom pressure follows.

## Exact local construction

### 1. Cycle-311 input and the vacuum-conditioned constraint

Cycle 311 supplies one 64-dimensional local M64 input and its 127-dimensional
fixed-seam closure:

```text
1 vacuum + 2(64-1) occupied comparator slices = 127.
```

Its flagged shell has 255 literal microsectors. The relational `r` lift gives
510 microsectors and one rank-127 constrained code. Index a role-gauge
microsector by `q=(branch,r)` and retain its physical number `n(q)` and flag
value `f(q)`. Add `h in {0,1}` and define the diagonal sign

```text
chi(q,h) = (-1)^h                       if n(q)=0,
           (-1)^(f(q) xor r(q) xor h)  if n(q)>0.
```

`C_hist` is the diagonal operator with eigenvalue `chi`. On every nonvacuum
encoded column, `f xor r=t`, so `chi=+1` selects `h=t`. On the vacuum column,
the first line selects `h=0` in both gauge branches. Using the unconditioned
product `Z_f Z_r Z_h` would reject half of the encoded vacuum and gives
residual `sqrt(2)`; the runner retains this as a deletion control.

This is a bounded matrix-unit constraint on one Cycle-311 patch plus one M2.
It is not presented as a one- or two-M2 primitive synthesis. Its complete
coefficient table, local number conditioning, and zero-initialized `h` state
are supplied structure.

### 2. Physical update and exact event decoder

Let `K_311`, `S_311`, and `D_311` be the physical coin, stream/catch-up, and
Cycle-230 contact operators of Cycle 311. Define

```text
K_hist = K_311 tensor I_h,
D_hist = D_311 tensor I_h,
S_hist : (q,h) -> (S_311 q, h xor 1_(n(q)>0)).
```

`K_hist` and `D_hist` preserve `C_hist` because they preserve number and
gauge-invariant slice. `S_hist` flips both the nonvacuum gauge-invariant slice
and `h`; it fixes both on vacuum. Thus all three physical components preserve
the constrained plus-space and satisfy their separate intertwiners.

Define the readable projector

```text
Q_h = |1><1|_h.
```

On the declared code,

```text
Q_h E_hist = E_hist Q_t,
```

where `Q_t` selects the occupied separated slice. This is a physical local
event-parity decoder. Its stable event label is the occupied crossing attached
to the supplied body patch, not the array position of an operation in a host
schedule.

The `n=1` Cycle-219 mass fixture is unchanged, including held
`beta=-0.35`. The sidecar neither changes the six-mode coin nor reinterprets
contact. Wrapped phase is not physical energy, a generator element is not a
rate, a copied readable pointer is not a Record, and a supplied update
orientation is not a derived time direction.

### 3. Proper-cubic covariance and the Z3 surface

`h` transforms as a scalar under every proper-cubic frame. The runner extends
each Cycle-311 signed physical representation by identity on `h` and tests:

```text
R_phys E_hist = E_hist R_log,
R_phys C_hist = C_hist R_phys,
R_phys S_hist = S_hist R_phys,
R_phys Q_h = Q_h R_phys.
```

All 24 frames, all 576 frame products, and all 27 `L=3` translations pass.
All six one-particle directions read `h=1` after the occupied stream. Hence
the sidecar selects no cubic direction.

The Z3 spatial surface is unchanged. `h` is one internal M2 at each existing
three-dimensional cell; it is not a fourth graph direction, a continuum tick,
or a compact coordinate.

## Independent-swap quotient on actual bounded supports

Cycle 312 replaces the one-pair recurrence's volume-wide projector formula by
bounded coin, reverse, and edge factors. Each factor carries a literal local
support, so support overlap supplies a dependency relation and disjoint
support certifies an independent swap.

The Cycle-314 runner selects five actual `L=3` Cycle-312 coin/edge blocks with
both overlapping and disjoint support pairs. An execution label is the stable
triple `(block kind, block index, physical block label)`. Starting from one
execution, the runner enumerates every sequence reachable through adjacent
swaps of disjoint supports. For every such sequence it constructs the
transitive dependency relation from overlapping pairs. Host positions change,
but the labeled causal dependency poset is identical.

This is a constructive `J`-map fixture of the Cycle-243 type:

```text
lawful bounded-block execution / certified independent swaps
    -> labeled causal dependency poset.
```

It does not count swap classes as time and does not turn graph depth, coloring,
or factor order into a clock. It is also not yet glued to `E_hist`: Cycle 312
is a recurrent one-pair compiler fragment, while Cycle 311 and this sidecar
are a common M64 fixed seam. A recurrent overlap-aware M64 compiler remains
the physical join required for a multi-event M64 event-poset square.

## What the construction supplies to the three time legs

### Leg A: causal-axis existence, origin, compactification

The positive result is below Leg A. `h=0` is a supplied input condition, and
the choice of `G_hist` rather than its inverse is a supplied update
orientation. Moreover,

```text
S_hist^2 = I.
```

The return `0 -> 1 -> 0` is reversible parity erasure. Calling it a period-two
compact time would add an interpretation not established by the local law.
There is no realized Record history, no physical origin selection, and no
past-distinguishing causal axis.

### Leg B: intrinsic axis label

`h` is a proper-cubic scalar and returns the same readout for all six matter
directions. It therefore carries no intrinsic spatial or time-axis label. A
boundary-condition asymmetry, a recurrence-registration marker, or a
relational history orientation remains a separate constructive target.

### Leg C: physical spacing and rate

One occupied crossing supplies one event-ready parity flip. Assigning that
flip interval `Delta=1` gives count per supplied interval `1`; assigning the
same flip interval `Delta=2` gives `1/2`. Nothing in `h`, `C_hist`, or
`G_hist` chooses between those calibrations. The runner uses this only as a
nonselection control. It does not name a circuit layer, event parity, or
update count as a physical rate.

## Event, occurrence, commit, and Record firewall

The retained typed chain is:

```text
physical event-ready support and readable parity
    -- occurrence/identity criterion --> actual causal event
    -- physical close --> append-only commit
    -- permanence criterion --> framework Record.
```

Cycle 314 constructs only the first object. It does not supply the occurrence
arrow. The local `h` state is coherently reversible, and a controlled copy of
it would also be reversible. Readability and copyability alone do not supply
physical close, branch realization, append-only persistence, or Record
formation.

The Cycle-312 dependency-poset fixture labels supported operations. It does
not turn every supported operation into an actual event. Joining that fixture
to realized history requires both a recurrent M64 compiler and the remaining
occurrence/close/permanence chain.

## Cold tests and decisive controls

| test | cold residual or count |
|---|---:|
| `E_hist` isometry | `2.349899218381e-15` |
| `C_hist E_hist-E_hist` | `0` |
| shell/constraint intertwiner | `2.852214593100e-15` |
| rank of shell-times-`h` | `254` |
| rank of `C_hist=+1` intersection | `127` |
| coin intertwiner, maximum over four betas | below `2.0e-15` |
| stream intertwiner | `0` |
| contact intertwiner | `0` |
| full `DSK` intertwiner, maximum | below `2.0e-15` |
| event decoder | `0` |
| constrained-code leakage | below `2.0e-15` |
| omit nonvacuum `h` flip | intertwiner `15.874507866388` |
| omit nonvacuum `h` flip | constraint-sign residual above `60` |
| wrongly flip vacuum | intertwiner above `0.9` |
| delete event decoder | residual `sqrt(63)` |
| use unconditioned vacuum constraint | residual `sqrt(2)` |
| two physical streams | zero permutation failures; `h` erased |
| sizes | trained `L=3,4,5`; held `L=6` |
| frames and products | `24 / 576` |
| translations | all `27` at `L=3` |
| installed overhead | `24 M2/cell`, one more than Cycle 311 |
| observed patch support | `45 M2`; declared envelope `57 M2` |
| one-particle mass | relative residual below `2e-12` |

Deletion of `h` leaves the Cycle-311 matter compiler exact. It removes only
the new readable event-parity channel. This distinguishes a successful matter
intertwiner from an event decoder. Deleting the stream-controlled `h` flip
instead leaves an M2 present but breaks both the event intertwiner and local
constraint preservation.

The runner rejects aliased `L=2`, invalid bodies, nonbinary event labels,
out-of-range numbers, nonsquare or nonfinite operators, and malformed
permutations.

## Supplied, derived, and open inventory

Supplied:

1. every Cycle-311 item: fixed Wilson/reference ray, body anchor, six cubic
   directions, orientations and frame repair, collision-safe ports, `f`, `r`,
   Cycle-219 coin, Cycle-230 coupling, fixed-seam domain, ordered update,
   dense local matrix-unit completion, and state preparation;
2. one zero-initialized ordinary `h` M2 per coarse cell;
3. the number-conditioned local constraint `C_hist` and its dense coefficient
   table;
4. the declared input slice and update orientation; and
5. the Cycle-312 one-pair block supports and certified support-independence
   relation used in the separate trace-quotient fixture.

No global CAR ordering, parity server, or host branch controller is supplied.

Derived:

1. the exact rank-127 event-sidecar plus-space;
2. physical coin, stream, contact, and composed intertwiners;
3. the local readable parity decoder and nonvacuum input/output truth table;
4. constraint preservation, code leakage bound, inverse/erasure, held size,
   support, frame, translation, deletion, and domain controls; and
5. one stable-label independent-swap quotient on actual Cycle-312 supports.

Open:

1. occurrence and stable physical event identity beyond support labels;
2. physical close, append-only persistence, permanence, and Record formation;
3. recurrent/full-volume M64 overlap and the glue to Cycle 312;
4. a past-distinguishing multi-event memory;
5. causal-axis origin or compactification, intrinsic axis label, physical
   interval spacing, clock selection, and rate calibration; and
6. primitive one-/two-M2 synthesis of the dense local blocks and constraints.

## Prior-art and novelty boundary

Ancilla parity flags, controlled flips, local gauge constraints, trace-monoid
quotients of independent operations, and reversible event markers are broad
prior-art territory. Cycle 314 claims only the explicit vacuum-conditioned
`C_hist`, its exact integration with the repository's Cycle-311 physical M64
fixed seam, the tested residuals, and the careful typed join to the Cycle-243
contract and Cycle-312 support graph. No global novelty priority is asserted.

Thirring is not used by this construction and is not a comparison engine for
this result.

## No-go discipline gate

The candidate broad negative is: “No bounded local physical-M2 event lift can
supply any bridge toward causal time or realized history.” Cycle 314 itself
refutes that wording by supplying a local event-ready parity carrier and an
actual bounded-support execution quotient. At the same time, the present
attempt closes none of Legs A/B/C, and several stronger constructive routes
remain live.

Broad gate status: FAIL / DO NOT SHIP.

The retained output is a positive partial bridge plus an exact list of open
typed arrows. It is not an impossibility, minimum-content, or axiom-pressure
result.

### N1 — alternative-route enumeration

| route | honesty | exact disposition |
|---|---|---|
| event-sidecar relational gauge | **ATTEMPTED** | succeeds exactly as a reversible local parity carrier; does not accumulate history |
| bare Cycle-311 role decoder | **ATTEMPTED** | `f xor r` decodes occupied seam role internally, but vacuum needs separate treatment and no independent readable carrier is installed |
| Cycle-312 bounded-block trace quotient | **ATTEMPTED** | succeeds on five actual one-pair blocks; recurrent M64 glue is absent |
| recurrent unary event front | **OPEN / UNTESTED** | could allocate fresh cells and preserve past distinctions under a local reversible recurrence |
| relational clock/coincidence matcher | **OPEN / UNTESTED** | could derive interval comparisons from two physical recurrent subsystems without treating update count as time |
| physical Record-forming instrument | **OPEN / UNTESTED** | PR 5451 closes copied-pointer and finite one-Kraus shortcuts, not every append-only physical close |
| APBC or registration-axis marker | **OPEN / UNTESTED** | could provide Leg B after a physical recurrence and covariance audit, but a supplied marker must not be relabeled derived |

The successful sidecar and the four live attacks make the broad negative fail.

### N2 — wall-independence audit

The collapsed open-condition set is `W_occurrence`, `W_permanence`,
`W_recurrence`, `W_compact`, `W_axis`, and `W_interval`. These are campaign
fields, not proposed axioms.

| pair | first closes second? | second closes first? | disposition |
|---|---:|---:|---|
| W_occurrence / W_permanence | no | no | independent tasks |
| W_occurrence / W_recurrence | no | no | independent tasks |
| W_occurrence / W_compact | no | no | independent tasks |
| W_occurrence / W_axis | no | no | independent tasks |
| W_occurrence / W_interval | no | no | independent tasks |
| W_permanence / W_recurrence | no | no | independent tasks |
| W_permanence / W_compact | no | no | independent tasks |
| W_permanence / W_axis | no | no | independent tasks |
| W_permanence / W_interval | no | no | independent tasks |
| W_recurrence / W_compact | no | no | independent tasks |
| W_recurrence / W_axis | no | no | independent tasks |
| W_recurrence / W_interval | no | no | independent tasks |
| W_compact / W_axis | no | no | independent tasks |
| W_compact / W_interval | no | no | independent tasks |
| W_axis / W_interval | no | no | independent tasks |

Occurrence can exist without permanence; a persistent memory can be prepared
without selecting occurrence; recurrence does not choose calibration; a
boundary marker does not choose interval size; and compact identification
does not itself select an intrinsic label. No duplicate is collapsed.

### N3 — hidden-condition scan

The source-note trigger scan required by the skill has zero hits. Every
reference, body, direction, auxiliary M2, constraint coefficient, input
condition, update orientation, support certificate, size, and tolerance is in
the inventory. No additional open condition is promoted after N2.

### N4 — residual matching

| exact witness | witness residual | Cycle-314 use | match? |
|---|---|---|---:|
| Cycle-243 note:142 | compiler/update intertwiner required in the event square | exact `E_hist G = G_hist E_hist` | yes |
| Cycle-243 note:183 | coherent pointer writes remain reversible | firewall against calling `h` a Record | yes |
| Cycle-311 note:59 | physical M64 fixed-seam intertwiner | starting physical compiler | yes |
| Cycle-311 note:66 | fixed seam is not recurrent volume | boundary on accumulated history | yes |
| Cycle-311 note:262 | compiler slices are not time | firewall against calling `h=t` elapsed time | yes |
| Cycle-312 note:25 | one-pair recurrence has bounded local factorization | actual support graph for the swap quotient | yes |

PR 5451 and PR 5469 are used only for typed distinctions and open-route
classification. Their finite-instrument or axis-import residuals are not cited
as proof of a shared obstruction.

### N5 — rhetoric and resolution audit

| resolution | tested | exact disposition |
|---|---:|---|
| per physical M2 | one `h` at every tested body type | scalar readable parity with local constraint |
| per fixed-seam block | all 127 columns and coherent states | exact update and decoder intertwiners |
| per bounded support graph | five actual Cycle-312 blocks | independent swaps preserve one dependency poset |
| recurrent M64 volume | no | no negative statement; glue remains open |
| lattice-wide physical time | no | no negative statement |

The only negative retained from the new runner is that this exact reversible
two-state sidecar has no accumulated past distinction: two tested streams
erase it. That statement is not widened to fresh-memory fronts or full
lattices.

### N6 — partial-closure paths

| constructive path | status | what it could close |
|---|---|---|
| recurrent overlap-aware M64 compiler | open | glue the event decoder to a multi-cell execution poset |
| append-only physical close and permanence | open | event-to-commit-to-Record arrows |
| relational coincidence clock | open | physical interval comparison without host counts |
| boundary-condition axis marker | open | Leg B, conditional on physical selection rather than supplied relabeling |
| interval-matching calibration | open | Leg C after actual events and physical clocks exist |

The executed `C_hist` sidecar is itself a partial-closure path: it retires the
missing readable-carrier input without constitutional change. The remaining
paths are physics campaigns, not automatic requests for a new axiom.

### N7 — hostile steelman

A hostile reviewer should say that a broad negative would confuse a
deliberately erasable one-bit comparator with the strongest local-history
architecture. A reversible QCA can move a front into fresh auxiliary cells,
leave a past-distinguishing spatial pattern, and compare that pattern against
a second recurrent subsystem. Cycle 312 already supplies bounded recurrent
supports and certified independent swaps on the one-pair sector, while Cycle
314 supplies the missing physical event-parity decoder on the M64 fixed seam.
An overlap-aware M64 recurrence plus fresh-cell memory could join those
fragments and attack Legs A and C directly. That route has not been tested.

### N8 — cross-cycle echo

| prior result | retirement or lesson | Cycle-314 implication |
|---|---|---|
| Cycle 243 | separated compiler, event, commit, Record, count, interval, and rate types | keep `h` below occurrence and time |
| Cycle 306 | one relational `r` retired a free role flag | use a local relation rather than supplied semantic metadata |
| Cycle 311 | one common constrained M64 seam retired separate number blocks | attach the sidecar to actual far-side physical matter |
| Cycle 312 | bounded factors retired a global one-pair projector formula | test support-based independent swaps constructively |
| PR 5451 | pointer copying did not establish Record formation | readability is not permanence |
| PR 5469 | time-axis imports split into Legs A/B/C | report each leg separately and leave all three open |

Every echo favors a sharper positive construction. None supports a
route-independent obstruction.

Gate disposition: **FAIL / DO NOT SHIP for the broad negative.**

## Six-wall dependency ledger

| wall | Cycle-314 movement | still open |
|---|---|---|
| `C_ref` | unchanged; `h=0`, body anchor, fixed reference, and update orientation are disclosed imports | physical genesis/preparation, cross-reference equivalence, intrinsic origin |
| `C_num` | unchanged from Cycle 311; all `n=0,...,6` sectors share the event-sidecar seam | recurrent/full-volume number sectors, number-changing interactions, sea-state compiler |
| `C_wrap` | advances narrowly: one physical readable parity decoder and one bounded-support independent-swap quotient close two pre-time inputs | occurrence, recurrence glue, permanence, causal-axis A, intrinsic label B, interval/rate C |
| `C_int` | the sidecar exactly preserves Cycle-230 local contact and full `DSK` | recurrent contact, overlapping arrivals, recoil, multi-event process law |
| `C_local` | one rank-127 code, 24 M2/cell, observed 45-M2 support, frames/translations, held `L=6`, leakage and deletions close | primitive synthesis, simultaneous patches, recurrent M64 volume law |
| `C_source` | unchanged; event parity and dependency order are not source, resource, lapse, or realized-history data | source observable, gravity/clock response, actualized persistent history |

## TOE lane update

These are evidence-weighted planning scores, not probabilities or audit
verdicts. The recommended post-Cycle-314 update is deliberately narrow.

| TOE lane | integrated | strict floor | conditional | maturity | Cycle-314 disposition |
|---|---:|---:|---:|---:|---|
| operational quantum / Records | 61% | 27% | 87% | 3.2/5 | conditional edge rises by one physical readable carrier; occurrence and Record remain open |
| causal time / clock | 34% | 17% | 62% | 1.8/5 | rises by a physical event-parity input and support-swap quotient; none of A/B/C closes |
| inertia / matter | 71% | 32% | 92% | 3.8/5 | unchanged; mass and M64 update are preserved |
| gravity / source / resource | 38% | 15% | 63% | 1.9/5 | unchanged |
| Born / probability / realized history | 33% | 14% | 82% | 1.8/5 | unchanged; no occurrence or outcome-selection result |

## Optimal next campaign

The highest-value next target is a fresh-cell reversible event front driven by
the Cycle-312 bounded recurrence supports but carrying the full Cycle-311 M64
code, not only one-pair coefficients. The decisive square should test two or
more overlapping updates, stable event labels under all independent swaps,
fresh-cell past distinction after inverse-local operations, and held-size
growth. If that closes, the next immediate test is a relational two-front
coincidence clock with two different local refinements. That sequence attacks
the recurrent M64 glue first, then Leg A/Leg C, while keeping occurrence and
Record formation separately typed.
