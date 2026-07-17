# Open-boundary actual-contact action detector — Cycle 291

**Date:** 2026-07-17

**Type:** bounded same-connected-code constructor for generating and exporting
an actual-`W_g` phase-sensitive coherent carrier with explicit open-sink
resource accounting

**Status:** positive fixed-total-number actual-action carrier and finite open
export; the reference/recombiner, rail, origin, blanks, and forward domain are
supplied, comparator-split faithfulness fails, and no outcome is selected

**Authority: none**

**Audit: unset**

**Constitutional effect: none**

Companion runner:

```text
scripts/open_boundary_actual_contact_action_detector_cycle291_2026_07_17.py
```

This cycle creates exactly this note and runner. It changes no axiom,
foundation, Qualification, primitive, registry, policy, queue, or audit
surface. It neither stages nor packages files and does not splice the Cycle-251
code into the Cycle-278/269/271 connected code.

## Result up front

Cycle 291 closes a sharper part of the Cycle-286 `W_g`-blindness residual.
It generates a phase-sensitive carrier **before** exporting it.

The supplied three-cell co-located-versus-separated reference has fixed total
particle number four:

```text
|C> : (N_x,N_y,N_z)=(4,0,0),  total pair count 6,
|S> : (N_x,N_y,N_z)=(2,1,1),  total pair count 1,
|r> = (|C>+|S>)/sqrt(2).
```

Both arms contain exactly one contact-active cell. Therefore identity, any
common phase, and the `Q`-only surrogate give the two arms the same phase. The
ordinary unconditional Cycle-230 action

```text
W_g = product_u exp(i g binom(N_u,2)),  g=0.37,
```

instead gives relative phase `5g`. A supplied local recombiner and code-to-
carrier transfer produce the bright/dark coherent carrier

```text
|psi_g> = cos(5g/2)|B> + i sin(5g/2)|D>
```

up to a common phase and a fixed sign convention. Its exact diagnostics are:

| diagnostic | exact numerical result |
|---|---:|
| actual `W_g` dark weight | `0.6377951234122565` |
| `I` dark weight | `0` |
| any common phase dark weight | `0` |
| `Q`-only surrogate dark weight | `0` |
| environment trace distance, `W_g` versus `I` | `0.7986207631988143` |
| carrier quadrature magnitude | `0.9612752029752999` |
| full-carrier trace distance, `W_g` versus `W_g^dagger` | `0.9612752029752999` |

Dark occupancy alone is inverse-sign blind. The full coherent carrier is not:
its `Y_(BD)` expectation flips sign under `W_g -> W_g^dagger`.

The carrier is transferred into an open dual-rail sink under one repeated
bounded fresh-target shift. Training `(R,h)` pairs are `(9,8)`, `(17,16)`, and
`(31,30)`; held out is `(47,46)`. The full carrier reaches every successive
slice without change and never returns before the supplied boundary.

The exact resource law is

```text
mapped three-cell matter support = 52 M2,
open sink                    = 3R M2,
total declared block         = 52+3R M2,
maximum collision/launch support = 54 M2,
propagation support          = 6 M2 per step,
fresh outward capacity       = R-1 shifts.
```

This is bounded per-step support with an exact resource and capacity ledger.

At held `R=47`, this is 193 M2 and 46 allocated fresh outward targets. The
actual diagonal action has maximum mapped Pauli-term weight 36 and zero local-
check/Wilson leakage at `L=3,4,5` and held-out `L=6`.
It preserves the one-particle mass fixture. The reduced-channel control below
is an explicit occupancy-only dephasing test.

The result is deliberately split into two claims:

1. the co-located/separated reference plus recombiner generates an
   actual-action-sensitive coherent carrier; and
2. the open sink exports that already-generated carrier with exact finite
   forward nonreturn.

The sink does not create the distinction. Full export leaves the local launch
register blank while the environment retains the pure carrier. Tracing an
occupancy-only sink dephases the carrier and makes `W_g` and `W_g^dagger`
identical at that reduced resolution.

The route is not split-fault faithful: if the recombiner is deleted while raw
arm transfer survives, nominal dark occupancy is `1/2`; deleting only one arm
of the phase action also gives false dark support. An exact inverse reconnects
the held carrier, and one bounded backward retarget moves it one slice toward
the apparatus. These are honest controls, not a shared substrate obstruction.

Sink export is not occurrence. Sink export is not a Record. Rail step count is
not physical time. No energy or source connector is constructed. Within the
reviewed Cycle-291 routes and exact declared domains, no route-independent
shared obstruction is established and no evidence-based axiom pressure
follows. That conclusion excludes unreviewed encodings, apparatus laws, and
preparations.

## 1. Fixed-total-number action reference

Cycle 285 used a one-cell `N=2/N=4` cross-number reference. Cycle 291 removes
that number-superselection vulnerability from the displayed phase comparison:
both arms have total `N=4`. Their local distributions differ.

The contact pair counts are

```text
p_C = binom(4,2)=6,
p_S = binom(2,2)+binom(1,2)+binom(1,2)=1.
```

The binary contact supports agree:

```text
q_C=q_S=1 active cell.
```

Consequently the physical alternatives act on the declared reference as

```text
I:                 diag(1,1),
exp(i phi) I:      exp(i phi) diag(1,1),
W_Q:               exp(i g) diag(1,1),
W_g:               diag(exp(i6g),exp(ig)),
W_g^dagger:        diag(exp(-i6g),exp(-ig)).
```

The phase-sensitive input is still supplied. The law does not prepare the
coherent superposition, choose the three cells or occupied directions, or
generate the recombiner.

## 2. Bright/dark transducer

On the two-dimensional declared reference span, the recombiner is

```text
H_CS = 2^(-1/2) [[1,1],[1,-1]].
```

A supplied code-preserving transfer sends its two outputs to one ordinary
dual-rail carrier. The reference-span map is an isometry; a unitary extension
on the bounded 52-M2 matter neighborhood plus two carrier M2 exists as a
finite-dimensional extension. This cycle does not synthesize that extension
from a selected nearest-neighbor microscopic gate law.

For `theta=5g`,

```text
P_D(W_g)=sin^2(theta/2),
P_D(I)=P_D(exp(i phi)I)=P_D(W_Q)=0.
```

The full pure carrier gives

```text
D_tr(rho_W,rho_I)       = |sin(theta/2)|,
<Y_BD>_W                = +/- sin(theta),
<Y_BD>_(W dagger)       = -<Y_BD>_W,
D_tr(rho_W,rho_Wdagger) = |sin(theta)|.
```

These are coherent state/effect diagnostics. No branch becomes actual.

## 3. Deletion, split, inverse, and retarget controls

| control | dark weight or result | disposition |
|---|---:|---|
| delete whole `W_g` action, retain recombiner | `0` | desired action-deletion control passes |
| replace by common phase | `0` | rejects global phase |
| replace by `Q`-only phase | `0` | rejects threshold support surrogate |
| replace by `W_g^dagger` | same `0.637795...` dark weight | dark occupation alone fails sign |
| retain full carrier quadrature under `W_g^dagger` | sign flips | coherent carrier resolves inverse |
| delete recombiner, raw transfer survives | `1/2` nominal dark | split false close |
| delete co-located-arm phase only | positive dark | split false close |
| delete separated-arm phase only | positive dark | split false close |
| exact reverse of 46 outward shifts | returns launch state | unrestricted irreversibility fails |
| one adjacent backward retarget | moves carrier inward one slice | intended-forward protection only |

Thus the whole-action deletion claim is stronger than Cycle 286, but the
comparator/transfer factorization remains a named fault seam. The result is a
positive constructor with a split residual, not an indivisible selected law.

## 4. Open dual-rail sink

Each sink slice contains three physical M2 roles:

```text
one synchronized frontier-token bit,
one bright carrier bit,
one dark carrier bit.
```

The carrier occupies the one-excitation dual-rail subspace. One repeated
fresh-target update swaps the token and both carrier rails from slice `i` to
slice `i+1`. Its support is six M2. The target must be blank and `i+1` must
exist. At `R-1`, the next call raises a boundary error rather than wrapping.

For both actual and deleted actions, positions are exactly `0,1,...,h`, every
complete state is distinct, and the two-component carrier is unchanged. The
full-state overlap and distinguishability are therefore conserved along the
rail.

The open rail, orientation, origin token, blank targets, repeated forward
grammar, and boundary are supplied. A fresh target slice is allocated at each
outward step. Globally the shift is reversible; this is spatial capacity
accounting, not a thermodynamic consumption theorem.

## 5. Environment and reduced-channel audit

Full SWAP export sends the entire bright/dark carrier to the environment. The
local launch pair is blank for both `W_g` and `I`, while the retained
environment states remain separated by trace distance
`0.7986207631988143`. Information is moved, not selected.

If only dark occupancy is copied and the copy is traced, the retained carrier
is dephased in the bright/dark basis. The `W_g` and `W_g^dagger` reduced
density operators then agree exactly. Discarding the full environment leaves
the local apparatus in the same blank state for every action.

Accordingly:

- environment distinguishability is not an actual outcome;
- reduced nonreturn is not destruction of global information;
- dephasing is not a Born selection law; and
- an open boundary is not a Record-formation map.

## 6. Same connected physical-M2 code, mass, and covariance

The three-cell action uses the Cycle-278 mapped occupation-parity generators
on the same Cycle-269/271 connected physical-M2 code. For `L=3,4,5,6`:

| item | exact result |
|---|---:|
| mapped matter support union | `52 M2` |
| maximum product-contact Pauli weight | `36` |
| local-check/Wilson action-algebra leakage | `0` |
| Wilson transition count | `0` |
| carrier overhead at launch | `2 M2` |
| complete collision/launch neighborhood | `54 M2` |

This is zero action-algebra leakage. The comparator is a declared
code-preserving isometry on the supplied two-dimensional even reference span;
its nearest-neighbor physical synthesis remains an explicit import.

The contact action is identity whenever every local occupation is zero or
one. All three one-particle placements therefore remain identity fixtures,
and the imported Cycle-219 rest/analytic mass equality is unchanged. The odd
one-particle state is still not prepared inside the fixed total-even code.

At `L=3`, all 24 proper-cubic frames and all 27 translations preserve the
three-cell mapped operator family, local checks, Wilson center, particle-count
pattern `(4,0,0)/(2,1,1)`, common active-cell count, and pair-count difference
five. Separately, all 24 frames and 27 translations carry the held open
three-lane sink without internal collisions and preserve longitudinal unit
edges. The family is covariant; selection of one member, orientation, and
placement remain supplied.

## 7. Exact resource and capacity ledger

| resource | formula | held `R=47` |
|---|---:|---:|
| mapped matter support | `52` | `52 M2` |
| token/bright/dark sink | `3R` | `141 M2` |
| total declared block | `52+3R` | `193 M2` |
| fresh outward shifts | `R-1` | `46` |
| launch support | `52+2` | `54 M2` |
| propagation support | `2+4` | `6 M2` |

Training and held rows exhaust their available forward capacity without wrap.
No finite rail is called an infinite sink. M2 count and blank allocation are
not called entropy, physical energy, stress, source, lapse, or gravity.

## 8. Finite/open lawful domain and supplied imports

The theorem domain is exactly:

1. the Cycle-269/271/278 connected total-even code at `L>=3`;
2. three distinct cells in the displayed bounded motif;
3. the supplied fixed-total-`N=4` coherent reference `(|C>+|S>)/sqrt(2)`;
4. the actual dimensionless `g=0.37` contact action at the motif cells;
5. the displayed reference-span recombiner and code-to-dual-rail transfer;
6. blank ordinary M2 token/bright/dark sink roles;
7. one unique origin token, supplied orientation, collision-free placement,
   fresh outward targets, and a non-wrapping finite boundary;
8. intended forward shifts only, with inverse and retarget included as stress
   controls rather than intended continuation;
9. training and held `(L,R,h)` domains stated above; and
10. trace/effect pairing with tolerance `3e-11`.

Not derived: preparation of the reference, selection of cells/modes/coupling,
microscopic nearest-neighbor synthesis of the recombiner/transfer, rail
genesis, origin, orientation, blanks, indefinite capacity, boundary physics,
environment exclusion, outcome selection, lawful Record typing, or a clock.

## 9. Operational and TOE dependency ledger

| interface | Cycle-291 status |
|---|---|
| actual contact action | ordinary unconditional `W_g`, no controlled-`W_g` service |
| reference | fixed total number, but supplied co-location/separation coherence |
| coherent detector | exact bright/dark carrier, `W_g` versus `I/Q/global` |
| inverse information | retained only in full carrier quadrature |
| export | exact finite open nonreturn with environment information ledger |
| occurrence | absent |
| Record | absent |
| time/source/Born | absent |

| wall | Cycle-291 effect | remaining dependency |
|---|---|---|
| `C_ref` | improves from cross-number to fixed-total-number spatial reference | prepare/recombine that reference under one selected law |
| `C_num` | actual pair-count difference five resolved, `Q` surrogate rejected | full-Fock/odd preparation and general data remain open |
| `C_wrap` | full phase carrier has exact finite forward nonreturn | rail genesis, boundary, indefinite capacity/renewal, lawful future |
| `C_int` | real gain: ordinary uncontrolled `W_g` creates the exported syndrome | comparator split fault and unknown-data interface remain |
| `C_local` | 54-M2 maximum step, action leakage zero, all-frame family | microscopic recombiner synthesis and autonomous placement |
| `C_source` | exact `52+3R` resource count only | no source/metric response |

Conservative maturity scores are unchanged from the Cycle-288 planning
baseline except for a narrow `C_int/C_ref` connector gain that is not enough to
move a whole 0–5 band:

| lane | score | reason |
|---|---:|---|
| operational quantum / Records | `2.5/5` | actual action now reaches an open coherent carrier; no occurrence/Record |
| causal time | `1.7/5` | spatial ancestry only |
| inertia / matter | `3.0/5` | fixed-`N` actual contact/mass fixture strengthened |
| gravity / source | `1.7/5` | resources counted, no source law |
| Born / probability / realized history | `1.7/5` | coherent weights and trace distances only |

## 10. Full N1–N8 no-go discipline

The main result is constructive. The narrow negative boundary is only that the
displayed supplied-reference/open-sink route does not itself provide a
split-faithful selected microscopic transducer, unrestricted permanence, or
actualization. No substrate-wide impossibility, minimum-content theorem, or
axiom-pressure claim is made.

### N1 — alternative-route enumeration

Here the honesty marker **ATTEMPTED** means executed by the Cycle-291 runner.
The table uses only the skill's exact permitted marker values.

| route | attack | honesty marker | exact disposition |
|---|---|---|---|
| fixed-total-`N` co-located/separated reference | make actual local pair count relational without controlled `W_g` | **ATTEMPTED** | succeeds: dark `0.637795...`, while `I/Q/global` are dark zero |
| `Q`-only/common-phase replacement | spoof the carrier with activity or scalar phase | **ATTEMPTED** | rejected exactly on the displayed fixed-`N` reference |
| inverse `W_g^dagger` | spoof positive dark occupancy | **ATTEMPTED** | occupancy spoofs; full `Y_BD` carrier flips sign and separates it |
| comparator/transfer split | delete recombiner but keep raw export | **ATTEMPTED** | false dark `1/2`; selected indivisibility remains open |
| full-state open export | move all phase information to a fresh environment | **ATTEMPTED** | succeeds on finite forward domain with exact information conservation |
| occupancy-only traced sink | export only a diagonal marker | **ATTEMPTED** | merely dephases and erases inverse sign; creates no outcome |
| exact inverse and adjacent backward retarget | reconnect the carrier | **ATTEMPTED** | both succeed outside intended forward grammar, defeating unrestricted permanence |

More than five genuinely distinct routes were tested. A law-generated
collision/reference defect that creates the reference, recombiner, and sink
under one homogeneous law was not attempted in Cycle 291. It is a live route
outside the N1 table and is not assigned an honesty marker. That route and the
successful constructor make a broad no-go premature.

### N2 — wall-independence audit

The raw import list collapses to four interfaces:

```text
R = lawful preparation and recombination of the fixed-N spatial reference,
F = split-faithful indivisible action/recombiner/transfer under one law,
O = open rail/origin/orientation/fresh capacity and selected future domain,
A = outcome actualization and lawful Record formation.
```

| pair | first automatically closes second? | second automatically closes first? | independent here? | concrete separation |
|---|---:|---:|---:|---|
| `R,F` | no | no | yes | a prepared reference can feed a split-spoofable comparator; an indivisible transducer may accept another input |
| `R,O` | no | no | yes | local reference preparation supplies no open boundary; a rail supplies no coherent phase reference |
| `R,A` | no | no | yes | coherent preparation selects no outcome; an occurrence law need not prepare this motif |
| `F,O` | no | no | yes | a fault-faithful local detector may remain cyclic; an open rail can export a blind `Q` carrier as in Cycle 286 |
| `F,A` | no | no | yes | faithful coherent detection still selects no branch; actualization does not authenticate the action |
| `O,A` | no | no | yes | environment export is not actualization; a Record law need not use an open sink |

No implication is used to inflate the wall count. These are candidate-law
interfaces, not proposed axioms.

### N3 — hidden-condition scan

The required scan covers `we assume`, `by construction`, `as is standard`,
`the framework provides`, `bridge context`, `background`, `naturally`,
`obviously`, `standard QFT`, `registered`, and `canonical`.

| hit or close variant | classification | action |
|---|---|---|
| “supplied” reference/recombiner/rail | load-bearing input | inventoried in Section 8 and collapsed into `R/O` |
| “ordinary unconditional” `W_g` | exact imported Cycle-230 action, not a control oracle | deletion/replacement tested |
| “open” sink | finite non-wrapping domain, not infinite bath | boundary, inverse, and retarget tested |
| “code-preserving isometry” | declared reference-span map | microscopic synthesis explicitly remains in `R/F` |
| “carried covariance” | transformed family, not origin generation | all frames tested; orientation remains in `O` |
| “detector” | coherent state distinguishability only | occurrence/Record firewall retained |

No load-bearing condition remains hidden. The phrase `by construction` appears
only in this required scan and supplies no premise.

### N4 — residual matching

| cited witness | residual attacked there | residual used here | match? (`yes`/`no`) / disposition |
|---|---|---|---|
| [Cycle 230:182–221](./SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md#L182) | actual `W_g=exp(i g binom(N,2))`, identity on one particle | pair-count difference and mass protection | **yes**, exact same action fixture |
| [Cycle 278:102–124](./CONNECTED_EDGE_SAME_CODE_LOCAL_INSTRUMENT_CYCLE278_NOTE_2026-07-17.md#L102) | `Q_x` is a bounded same-code activity operator | reject the `Q`-only surrogate | **yes**, same mapped `B` algebra |
| [Cycle 285:298–343](./ACTUAL_CONTACT_ACTION_SYNDROME_TOURNAMENT_CYCLE285_NOTE_2026-07-17.md#L298) | direct `N=2/N=4` reference separates `W_g` from `I/Q/global` | same relative `5g`, but fixed total number and three cells | **no**, different reference residual; dropped as a witness for current closure and retained only as prior-art contrast |
| [Cycle 286:299–332](./OUTGOING_CARRIER_NONRECURRENCE_CYCLE286_NOTE_2026-07-17.md#L299) | outgoing `Q_x` carrier is exactly blind to deleting `W_g` | generate phase-sensitive carrier before the same kind of open export | **yes**, exact blindness residual narrowed |
| [Cycle 286:333–384](./OUTGOING_CARRIER_NONRECURRENCE_CYCLE286_NOTE_2026-07-17.md#L333) | finite forward nonreturn permits inverse/retarget | current dual-rail sink has the same scoped boundary | **yes**, no permanence claim |

The Cycle-285 row is dropped from the witness count for current closure. It is
retained only as prior-art lineage and is not used to claim a physical
preparation law. No time, Born, gravity, or Record residual is borrowed as a
detector witness.

### N5 — resolution and rhetoric audit

Each negative semantic statement is expanded through every resolution named by
the fresh `origin/main` skill. Every tested cell is labeled `tested`; every
untested cell says exactly `unknown/not claimed`.

| statement | per-element | per-site | per-mode | per-block | lattice-wide | narrow retained wording |
|---|---|---|---|---|---|---|
| sink export is not occurrence | **tested:** one carrier amplitude; no selection map | **tested:** B/D sites; no actualization gate | **tested:** dual-rail coherence retained | **tested:** full finite circuit; pure state only | **unknown/not claimed** | the displayed finite export circuit contains no occurrence map |
| sink export is not a Record | **tested:** no element is typed | **tested:** no site receives Record typing/protection | **tested:** carrier mode remains reversible | **tested:** inverse/retarget erase/reconnect | **unknown/not claimed** | the displayed finite carrier is untyped and reversible |
| rail step count is not physical time | **tested:** one update has only ancestry | **tested:** position is spatial | **tested:** mode label supplies no duration | **tested:** no matcher/calibration in finite histories | **unknown/not claimed** | no clock/matcher/calibration is present in this circuit |
| dark weight is not a Born frequency | **tested:** one amplitude squared | **tested:** one effect site | **tested:** one dual-rail effect | **tested:** no member/frequency selection in block | **unknown/not claimed** | `0.637795...` is only the displayed coherent effect weight |
| phase coefficient is not called energy/rate | **tested:** gate parameter | **tested:** local action support | **tested:** pair-count spectrum | **tested:** no clock or energy calibration in block | **unknown/not claimed** | no energy/rate connector is constructed here |
| M2 capacity is not called source | **tested:** element count | **tested:** three M2 per sink site | **tested:** B/D/token roles | **tested:** `52+3R` ledger | **unknown/not claimed** | no stress/source/metric response is constructed here |
| finite forward nonreturn is not permanence | **tested:** one shift is invertible | **tested:** adjacent retarget succeeds | **tested:** carrier mode is preserved | **tested:** four finite rails reverse exactly | **unknown/not claimed** | nonreturn means only the supplied finite forward domain |

No untested lattice-wide negative is promoted. Every retained phrase is
narrowed to the displayed finite circuit or to absence of a typed connector.

### N6 — partial-closure path scan

Live constructive import-retirement paths are:

1. generate the co-located/separated fixed-`N` packet through the ordinary
   stream/collision law rather than supply it;
2. compile the recombiner/transfer into the same bounded connected-code even
   algebra and selected nearest-neighbor law;
3. make action, recombination, and launch one indivisible local transition and
   repeat all split controls;
4. use redundant signed carrier ports so inverse and component deletion cannot
   spoof one occupancy;
5. generate an outward defect/boundary and fresh capacity from a homogeneous
   resource law with conserved information/current accounting;
6. retain the full environment and couple it to an independently derived
   occurrence/Record interface; and
7. test unknown parity-even matter rather than the supplied two-state
   calibration reference.

These are constructive physics routes. A vocabulary convention can enforce
the sink/Record/time firewall, but it cannot prepare the reference, synthesize
the transducer, create a boundary, or select an outcome. No new axiom is
requested.

### N7 — steelman

> A hostile reviewer should reject any claim that the remaining imports are
> substrate obstructions. The route already shows that an ordinary
> unconditional contact law can become relational on a fixed-total-number
> spatial packet and that an open channel can carry every phase bit outward.
> The supplied packet and recombiner look exactly like components that a
> local collision interferometer or moving defect could generate. The split
> false close attacks the chosen factorization, not every indivisible update;
> the inverse attacks the admitted global gate grammar, not a selected open
> resource law. Cycle 285 left a local-current route open, and Cycle 286 showed
> that open export retires cyclic recurrence on its declared domain. The next
> constructor could join those mechanisms without changing the axioms.

Accepted. The result remains a positive partial constructor, and the next
campaign should target one-law reference genesis and indivisibility.

### N8 — cross-cycle echo

The required phrase search and available `NO_GO_LEDGER.md` walk were performed.
The packet-memory ledger explicitly warns not to turn finite detector overlap
into derived decoherence or a finite checked window into an infinite-memory
theorem. The directly relevant campaign echoes are:

| prior wall | retired since? | mechanism | applicability here |
|---|---|---|---|
| Cycle-286 `Q_x` carrier blind to `W_g` | **yes on this reference** | generate a pair-count phase carrier before export | direct mechanism used here |
| Cycle-285 cross-number reference import | **partly** | replace it by fixed-total-number co-location/separation | used here; preparation remains supplied |
| Cycle-285 controlled-`W_g` service | **yes on this reference** | let ordinary unconditional contact act differently on two spatial arms | used here; recombiner remains supplied |
| Cycle-286 cyclic recurrence concern | **partly** | open finite rail with explicit boundary | used here; inverse/capacity remain |
| packet-memory finite-window overreach | **not retired universally** | keep environment and finite horizon explicit | enforced here |
| auxiliary split false close | **no** | current comparator split still false-closes | indivisible/redundant route remains live |

The echo is progressive import retirement, not a stable route-independent
obstruction.

**N1–N8 status: PASS for the narrow positive constructor and its exact finite
residuals.**

**N1–N8 status: FAIL for a detector no-go, minimum substrate theorem, or axiom
pressure.**

## 11. Disposition and optimal next route

Retain:

- fixed-total-number ordinary-`W_g` relative phase `5g`;
- exact rejection of `I`, common phase, and `Q`-only replacement;
- full coherent inverse-sign carrier and environment trace distances;
- bounded 54-M2 launch, 6-M2 propagation, `52+3R` total ledger;
- zero action-algebra leakage, mass fixture, `L=3..6`, all-frame covariance;
- held `R=47,h=46` finite forward nonreturn; and
- full trace/dephasing, boundary, inverse, retarget, and semantic controls.

Do not claim:

- autonomous preparation or nearest-neighbor synthesis of the reference and
  recombiner;
- split-fault faithfulness;
- arbitrary-data nondisturbance or a general event detector;
- infinite capacity, global irreversibility, destruction of information, or
  permanence;
- occurrence, Record, time, duration, rate, energy, source, Born frequency, or
  realized history; or
- shared obstruction, minimum content, or axiom pressure.

The optimal next route is an **indivisible law-generated collision
interferometer**: create the fixed-`N` co-location/separation packet during the
ordinary local update, recombine and launch it through one selected bounded
gate, and require whole-action and every component deletion to suppress both
dark occupancy and signed carrier quadrature. Keep the full environment and
derive any occurrence/Record connector separately.

## Verification

Run:

```bash
python3 scripts/open_boundary_actual_contact_action_detector_cycle291_2026_07_17.py
```

The runner must finish with zero failures. PASS totals are contract/regression
controls, not counts of independent predictions.
