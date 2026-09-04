# Uncontrolled contact collision-current syndrome — Cycle 289

**Date:** 2026-07-17

**Type:** constructive ordinary-contact spatial interferometer and bounded
physical-M2 collision-current transducer

**Status:** positive conditional construction on a supplied coherent
fixed-total-number collision fixture; no occurrence, Record, clock, Born law,
energy, source, or autonomous reference preparation

**Authority: none**

**Audit: unset**

**Constitutional effect: none**

Companion runner:

```text
scripts/uncontrolled_contact_collision_current_syndrome_cycle289_2026_07_17.py
```

This cycle creates only this note and runner. It changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface. It
does not draft axiom language.

## Result in plain English

Yes, the ordinary unconditional `W_g` update can leave a bounded local
auxiliary collision/current syndrome without a supplied controlled-`W_g`
oracle.

The successful route is a **fixed-total-number collision interferometer** on
three neighboring coarse cells of the Cycle-278/285 connected physical-M2
code. Its two supplied coherent branches both have total number four and
**equal `Q`-support**:

```text
branch A: target N=2, two neighboring N=1 singletons
branch B: target N=4, the same two neighbors empty
```

Both branches have exactly one `Q=1_(N>=2)` cell. A threshold-only update
`exp(i g Q)` or any global phase therefore acts as the same scalar on both.
The actual contact instead gives target pair counts one and six:

```text
W_g |A> = exp(i g)  |A>,
W_g |B> = exp(i 6g) |B>,       g=0.37.
```

After this ordinary matter-only action, a separately supplied bounded
**collision-SWAP transducer** transfers the complete `A/B` phase qubit into
one blank M2 flag. It does not control whether `W_g` acts. On the coherent
input `(|A>+|B>)/sqrt(2)` the flag-one weight is

```text
sin^2(5g/2) = 0.637795123412256,
```

while deletion of the target `W_g`, threshold-only replacement, and
global-phase replacement leave the flag exactly blank. The flag `Y` current
has magnitude

```text
|sin(5g)| = 0.9612752029752998
```

and reverses sign for `W_g^dagger`. Thus the construction distinguishes the
actual number-dependent phase from contact support, a global phase, deletion,
and the adjoint sign on its declared fixture.

This is a real constructive gain over the controlled-process route. It is
also deliberately conditional. The coherent collision-path state, its phase
convention, the blank flag, the comparator/transducer, the insertion window,
and the read basis are supplied. The coherent flag is not occurrence. The
auxiliary flag is not a Record. Circuit order is not physical time. Wrapped
phase is not physical energy.

At the reviewed Cycle-289 evidence scope, there is no route-independent
obstruction and no axiom pressure. This sentence does not quantify over
unreviewed encodings, apparatus laws, or collision preparations.

## 1. The ordinary unconditional contact action

The matter action is exactly the Cycle-230/Cycle-285 onsite contact

```text
W_g(x) = exp(i 0.37 binom(N_x,2)).
```

It is applied to matter without any control qubit, controlled process, Ramsey
oracle, joint `W_g tensor X_flag` call, or host-selected choice between action
and identity. The auxiliary flag remains absent from this action:

```text
matter:  W_g
flag:    I.
```

Only after the action is complete does the collision-SWAP act. Deleting the
target `W_g` means replacing that matter action by identity while leaving the
prepared collision state, transducer, and flag read unchanged.

The two declared branches use target and neighboring occupation patterns

```text
A = {(x,0),(x,1),(x+e_y,3),(x+e_z,5)},
B = {(x,0),(x,1),(x,2),(x,4)}.
```

The outer-edge pairs `(x,2)<->(x+e_y,3)` and
`(x,4)<->(x+e_z,5)` are physical graph edges. Their two actual FSWAPs exchange
`A` and `B` in both directions. Both states have total number four and total
even parity. The separated singleton cells see identity under contact, so
deletion of the target `W_g` removes the complete relative phase.

The threshold replacement has logical restriction

```text
exp(i g Q)|span(A,B) = exp(i g) I_2,
```

whereas the actual restriction is

```text
diag(exp(i g), exp(i 6g)).
```

Their Frobenius residual is `1.5972415263976283`. This is the exact sense in
which the flag is action-resolving rather than merely `Q`-support resolving.

## 2. Bounded collision-SWAP transducer

Let

```text
|+>_AB = (|A>+|B>)/sqrt(2),
|->_AB = (|A>-|B>)/sqrt(2).
```

On the declared two-dimensional branch subspace and one blank M2 flag, the
transducer is

```text
T_collision = (H_AB tensor I_F) SWAP_(AB,F) (H_AB tensor I_F).
```

Its full `4 x 4` unitarity residual is numerical zero within `4e-11`. With the
flag initially `|0>`, it maps

```text
(alpha |+>_AB + beta |->_AB) |0>_F
    -> |+>_AB (alpha |0>_F + beta |1>_F).
```

Therefore it resets the declared matter logical to the supplied `|+>` phase
reference while exporting the complete complex phase qubit. The positive
flag weight sees the phase magnitude, and the flag `Y` quadrature sees its
sign.

This comparator is an ordinary post-action matter/auxiliary unitary. It is not
a controlled-`W_g` oracle. Its preparation and selection are nevertheless
real supplied resources; the construction does not pretend that an arbitrary
incoming matter state generates this comparator or the `A/B` coherence.

## 3. Explicit physical-M2 representative

The construction stays on the Cycle-269/271/275/278 connected edge code. It
does not splice the Cycle-251 subsystem code.

For every one of the three cells, the six occupation parities `B_(x,d)` are
the exact mapped physical Pauli operators. The branch projectors are bounded
polynomials

```text
P_A = product_j (I + s_A,j B_j)/2,
P_B = product_j (I + s_B,j B_j)/2
```

over the eighteen modes of the three-cell patch. The two physical graph
FSWAPs use the retained exact polynomial

```text
F_+(u,v) = (B_u+B_v+i B_u A_uv-i B_v A_uv)/2.
```

Their product `R` exchanges the two occupation patterns. On the branch
subspace,

```text
X_AB = P_(A+B) R P_(A+B),
Z_AB = P_A-P_B,
```

so `H_AB`, the controlled logical permutations used in `SWAP_(AB,F)`, and the
unitary extension outside the branch subspace all belong to the bounded
physical even algebra generated by these `B`, `A`, and flag Pauli operators.

Every displayed physical generator commutes with every local check and all
three Wilson operators. Products, sums, projectors, and exponentials of that
algebra preserve the same code. The runner obtains zero leakage at
`L=3,4,5` and held-out `L=6`.

The support is constant with size. The exact runner output gives 52 matter M2
factors for the three-cell `B/A/FSWAP` union and one additional M2 flag, for 53
M2 factors in the full bounded
neighborhood. This is a support-union bound for the explicitly generated
physical algebra, not a nearest-neighbor synthesis depth theorem.

## 4. Deletion, replacement, sign, and coherence controls

The exact fault table is:

| retained fixture | flag-one weight | flag `Y` current | disposition |
|---|---:|---:|---|
| ordinary unconditional `W_g` | `0.637795123412256` | signed magnitude `0.9612752029752998` | constructive success |
| deletion of the target `W_g` | `0` | `0` | detected |
| threshold-only `exp(i g Q)` | `0` | `0` | rejected despite equal active support |
| arbitrary global phase | `0` | `0` | rejected |
| `W_g^dagger` sign control | same positive weight | opposite `Y` current | sign resolved by supplied quadrature |
| dephased `A/B` mixture | actual/deleted flag residual `0` | none | coherence is load bearing |

A separate same-total-`N=2` co-located-versus-separated spatial
interferometer is also run. It distinguishes ordinary `W_g` from deletion but
does not distinguish `W_g` from `exp(i g Q)`, because on that fixture the pair
count and `Q` activity are the same binary condition. This successful partial
route is an explicit counterexample to any claim that unconditional `W_g` is
operationally invisible. The equal-`Q`, total-`N=4` fixture is what closes the
stronger action-versus-support control.

These are declared process interventions and calibration states. They do not
establish that nature selected one branch, that one invocation occurred, or
that the apparatus formed a Record.

## 5. Mass, leakage, held size, and covariance

The actual `W_g` remains exactly identity on `N<=1`. The two separated
singletons in branch `A` are therefore undisturbed by contact. At
`beta=-0.3`, the inherited one-particle rest-to-analytic mass ratio remains
`0.9999999999999998`, within the declared `2e-12` relative tolerance. This is
an operator-law fixture; the fixed-total-even code does not acquire an odd
one-particle prepared state.

For `L=3,4,5,6`, the runner rebuilds:

1. the connected local-check code and three Wilson operators;
2. all eighteen cell-parity generators in the three-cell patch;
3. the two mapped transport `A` generators and all eight physical FSWAP
   polynomial terms;
4. the 64-term contact Walsh family at each involved cell; and
5. the carried scalar M2 flag.

Every generator has zero local-check/Wilson leakage. `L=6` is held out.

At `L=3`, every proper-cubic frame is combined with all 27 coarse
translations. The transformed three-cell motif, its two graph edges, mapped
`B/A` family, local-check family, and Wilson center agree in all
648 frame-translation cases (`24*27`). The motif orientation is carried as spatial fixture data;
no fixed direction is declared invariant and no apparatus orientation is
generated from a homogeneous state.

## 6. Lawful domain and exact retained claim

The positive theorem is restricted to:

```text
finite periodic L>=3 connected edge codes;
one declared contractible three-cell patch;
the supplied coherent span of A and B at total N=4;
equal Q-support on those two branches;
ordinary unconditional target W_g at g=0.37;
one supplied collision-SWAP and one blank M2 flag;
the declared deletion/replacement/read grammar.
```

The runner rejects `L<3`, a different total-number fixture, unequal branch
`Q` values, and a non-M2 flag.

The retained claim is:

> On the declared fixed-total-`N=4`, equal-`Q` collision-path reference, the
> ordinary unconditional Cycle-230 contact action produces a bounded
> connected-code auxiliary phase flag that distinguishes deletion,
> threshold-only support phase, global phase, and adjoint sign, while
> preserving local checks, Wilson sectors, the one-particle mass fixture,
> held size, and proper-cubic covariance.

It is not an arbitrary-input action detector, an autonomous apparatus law, an
outcome-selection law, or a statement of empirical occurrence.

## 7. Supplied-structure inventory

| supplied structure | exact role | not derived here |
|---|---|---|
| Cycle-269/271/275/278 connected edge code | physical total-even matter algebra | bounded code preparation or law selection |
| actual `g=0.37`, target `W_g`, and insertion window | unconditional contact process | empirical selection or autonomous scheduling |
| target cell plus two oriented neighboring cells | collision patch | homogeneous origin/orientation generation |
| coherent `(|A>+|B>)/sqrt(2)` at total `N=4` | relational collision-path phase reference | bounded preparation from generic matter |
| branch projectors and two graph FSWAPs | physical logical `X_AB/Z_AB` | selected nearest-neighbor synthesis schedule |
| collision-SWAP transducer | exports the phase qubit | autonomous comparator genesis |
| blank M2 flag and `Y` phase convention | positive/sign readout basis | reset, calibration, or physical reader |
| trace and flag effects | exact diagnostic weights | Born law, frequency, or realized outcome |
| deletion/global/threshold/adjoint grammar | falsification controls | substrate-selected fault process |
| finite periodic geometry and carried frames | held/covariance test domain | continuum limit or unique apparatus placement |

The construction supplies no controlled-`W_g` oracle. It also supplies no
occurrence map, commit, lawful Record typing, permanence law, recurrent clock,
interval calibration, additive energy/stress/source ledger, lapse, metric
response, Born rule, or realized-history member.

## 8. Interpretation and TOE dependency ledger

The coherent flag is not occurrence: it is one reversible component of a
joint state before any actual member is selected. The auxiliary flag is not a
Record: no lawful typing, commit, protection, or continuation theorem is
present. Circuit order is not physical time: no recurrent Record chain,
matcher, or interval calibration exists. Wrapped phase is not physical
energy: `0.37`, the flag weight, and the `Y` current are dimensionless process
fixtures, not an additive source or rate.

| wall | Cycle-289 effect | still open |
|---|---|---|
| `C_ref` | replaces a controlled-process oracle with a fixed-total-number spatial collision reference | prepare the collision coherence, flag blank, phase zero, origin, and comparator from one law |
| `C_num` | fixed total `N=4`; equal `Q` support; actual pair-count phase separated from threshold support | common odd/full-Fock preparation and autonomous physical number/reference process |
| `C_wrap` | bounded contractible patch, zero leakage, held `L=6`, all-frame covariance | global preparation and wrapped/indefinite process |
| `C_int` | strong gain: ordinary unconditional `W_g` deletion and replacements are resolved without controlled `W_g` | arbitrary-input action/current law, indivisible action-plus-syndrome, occurrence |
| `C_local` | bounded three-cell physical algebra plus one M2 flag | selected nearest-neighbor synthesis and homogeneous apparatus generation |
| `C_source` | unchanged | no additive source, normalization, reciprocal clock/metric response, or gravity law |

The inertia/matter lane gains a new same-code operational connector. The
operational/Record lane gains only a conditional coherent flag, not an
occurrence or Record. Time, gravity/source, and Born/realized history do not
move.

## 9. Prior-art and novelty boundary

No novelty is claimed for Ramsey or Mach-Zehnder interferometry, collision
phase shifts, logical SWAPs, occupation-projector polynomials, FSWAPs, or
phase-to-ancilla transduction in general.

The repo-local contribution is the exact integration of all of the following
in one falsifiable fixture: the actual Cycle-230 `binom(N,2)` contact; an
ordinary unconditional rather than controlled action; a fixed-total-number,
equal-`Q` spatial collision reference; an explicit connected-code physical
`B/A/FSWAP` representative; exact deletion/threshold/global/adjoint controls;
zero leakage; bounded M2 support; held `L=6`; all 648 frame-translation cases;
and the Record/time/energy firewalls.

No Thirring engine is used, extended, or compared.

## 10. Full no-go discipline N1–N8

The main result is positive. The narrow negative boundary is only that this
cycle does not remove the prepared collision coherence or supplied
transducer, and does not construct occurrence. No arbitrary-state,
reference-free, substrate-wide, minimum-content, or axiom-pressure theorem is
claimed.

### N1 — alternative-route enumeration

Every route below is executed in the Cycle-289 runner.

| route | attempted attack | honesty marker | exact disposition |
|---|---|---|---|
| fixed-`N=4`, equal-`Q` spatial collision reference | expose the pair-count phase while cancelling total number and support phase | **ATTEMPTED** | succeeds with flag weight `0.637795123412256` and signed current magnitude `0.9612752029752998` |
| same-total-`N=2` co-located/separated reference | detect ordinary unconditional contact without cross-number coherence | **ATTEMPTED** | succeeds against deletion, but `W_g` and threshold `exp(i g Q)` coincide on that fixture |
| target-`W_g` deletion with comparator retained | test whether auxiliary close depends on the actual action | **ATTEMPTED** | flag weight becomes exactly zero |
| threshold-only replacement | test whether contact support alone explains the flag | **ATTEMPTED** | equal `Q` values make it a scalar and the flag stays blank |
| arbitrary global-phase replacement | test whether any wrapped phase produces the result | **ATTEMPTED** | flag stays blank |
| `W_g^dagger` replacement | test sign information rather than positive weight only | **ATTEMPTED** | weight agrees but flag `Y` current reverses sign |
| dephased collision-path mixture | remove the prepared relational coherence while retaining populations | **ATTEMPTED** | actual/deleted flag density residual is zero; the supplied coherence is load bearing |
| physical two-FSWAP branch transport | test a local even-algebra bridge between the spatial configurations | **ATTEMPTED** | exchanges `A` and `B` exactly in both directions on two graph edges |

The successful `N=2` and `N=4` spatial routes explicitly defeat any broader
claim that unconditional `W_g` is operationally invisible. The residual is
preparation and common-law generation, not absence of a constructive route.

### N2 — condition-independence audit

The collapsed condition set is:

```text
P = prepared coherent collision-path state and its phase convention
A = ordinary unconditional actual W_g on the declared target
T = bounded collision-SWAP, blank flag, and read basis
O = law-owned occurrence / one actual outcome and downstream Record typing
```

| pair | closing first automatically closes second? | closing second automatically closes first? | independent? | witness |
|---|---|---|---|---|
| `P,A` | no | no | yes | a prepared superposition applies no contact; `W_g` prepares no `A/B` coherence |
| `P,T` | no | no | yes | the state supplies no comparator; a comparator does not prepare its calibrated input |
| `P,O` | no | no | yes | coherence selects no actual member; occurrence can act on another prepared domain |
| `A,T` | no | no | yes | matter-only `W_g` leaves the flag untouched without the transducer; the transducer can be run after identity |
| `A,O` | no | no | yes | a unitary action does not actualize one branch; occurrence need not certify this contact |
| `T,O` | no | no | yes | a coherent flag/read basis supplies no actuality; an occurrence law need not build this comparator |

No implication was found. The four conditions remain distinct. Record,
permanence, time, Born weights, and source response are downstream interfaces,
not inflated into extra walls of this narrow construction.

### N3 — hidden-condition scan

The required phrase scan found no use of `we assume`, `as is standard`,
`the framework provides`, `bridge context`, `obviously`, `standard QFT`,
`registered`, or `canonical` as proof steps. Uses of “supplied,” “declared,”
“background,” and “by construction” are classified explicitly:

| phrase/context | classification | action |
|---|---|---|
| supplied coherent collision fixture | load-bearing `P` | inventoried; dephased deletion control executed |
| supplied collision-SWAP/flag/read | load-bearing `T` | inventoried; separate from `W_g` |
| declared target/insertion window | load-bearing placement condition | included with `P/T`, not hidden as homogeneous law |
| connected-code background | cited candidate code substrate, not a prepared state | physical generators and leakage rerun at all sizes |
| “by construction” algebra membership | non-load-bearing shorthand only after explicit `B/A/FSWAP` generators | generator commutators and support are executable |

No hidden condition enlarges the collapsed set, so N2 need not be rerun.

### N4 — residual matching

All cited cycles remain authority-none/audit-unset candidate science. They are
used only to identify the exact substrate/operator residual inherited here,
not as audited constitutional authority.

| cited witness | residual attacked there | exact residual used here | match? |
|---|---|---|---|
| [Cycle 230:182–191](./SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md#L182) | actual onsite `W_g=exp(i g binom(N,2))`, identity on `N<=1` | same `g=0.37`, pair counts `1/6`, and one-particle identity | **yes** |
| [Cycle 271:29–60](./CONTRACTIBLE_LIGHTCONE_WILSON_QUOTIENT_CYCLE271_NOTE_2026-07-17.md#L29) | connected-code contractible even observable/process algebra | bounded three-cell total-even `B/A/FSWAP` polynomial, no wrapped claim | **yes** |
| [Cycle 275:76–103](./LOCALLY_MATCHED_WILSON_SECTOR_STATES_CYCLE275_NOTE_2026-07-17.md#L76) | matched algebraic states exist but bounded preparation is absent | collision state is an explicit supplied algebraic fixture, not a preparation theorem | **yes** |
| [Cycle 278:41–64](./CONNECTED_EDGE_SAME_CODE_LOCAL_INSTRUMENT_CYCLE278_NOTE_2026-07-17.md#L41) | bounded mapped `Q` support interface on the connected code | both branches have the same `Q=1`; threshold flag residual is zero | **yes** |
| [Cycle 285:310–380](./ACTUAL_CONTACT_ACTION_SYNDROME_TOURNAMENT_CYCLE285_NOTE_2026-07-17.md#L310) | unconditional cross-number comparator detects `W_g` but supplies its matter reference | fixed-total-`N=4` spatial reference closes the number-reference residual while retaining preparation/transducer imports | **yes**, residual narrowed rather than transferred |

No controlled-Ramsey deletion residual is cited as evidence for this
uncontrolled route. No compiler, time, gravity, or Born residual is borrowed
to condemn the collision construction.

### N5 — resolution and rhetoric audit

Every physics-type negative statement is expanded through the required
per-element, per-site, per-mode, per-block, and lattice-wide resolutions.
`N/A` is used only where the semantic category has no well-defined object at
that resolution, and the reason is stated in the cell. Every untested scope is
marked **unknown/not claimed**.

| statement family | per-element | per-site | per-mode | per-block | lattice-wide | narrow retained meaning |
|---|---|---|---|---|---|---|
| coherent flag is not occurrence | **N/A:** occurrence is an actual-member relation, not a property of one matrix element | **tested:** the one M2 flag site remains a reversible amplitude carrier; no actual-member map is applied | **tested:** both `A/B` logical amplitudes remain in one pure joint state before any read | **tested:** the complete three-cell-plus-flag block has only unitary action/transduction | **unknown/not claimed:** no arbitrary apparatus or realized lattice history was tested | the displayed coherent flag contains no occurrence map; no universal occurrence no-go follows |
| auxiliary flag is not a Record | **N/A:** lawful Record typing is not defined for an isolated matrix element | **tested:** the one flag site has no commit label, lawful typing, or protection rule | **N/A:** no independent “Record mode” is defined; the flag mode is only an auxiliary M2 | **tested:** the finite block has no commit, typing, permanence, or continuation map | **unknown/not claimed:** indefinite lawful continuation and lattice-wide Record formation were not tested | this supplied flag is not promoted to a Record; other Record-forming laws remain live |
| circuit order is not physical time | **N/A:** a matrix element has no event equivalence or interval | **tested:** no site carries a recurrent clock state or calibrated tick | **tested:** matter, logical-collision, and flag modes have an action order but no matcher or interval normalization | **tested:** one finite action-then-transducer block and its 648 spatial carries contain no recurrent Record chain | **unknown/not claimed:** no recurrent lattice ensemble or continuum clock limit was tested | the displayed circuit order is not called time; no possible emergent-clock relation is denied |
| wrapped phase is not physical energy | **tested:** individual amplitudes contain dimensionless phases only, with no energy calibration | **tested:** the target-site pair-count phase has no additive local source assignment | **tested:** the `N=2/N=4` mode phases and flag quadrature have no generator-to-energy normalization | **tested:** the three-cell block has no conserved additive matter/apparatus source ledger | **unknown/not claimed:** lattice-wide stress, empirical normalization, and reciprocal metric response were not tested | the displayed phases/current are not named energy; a future source relation is not excluded |
| construction is not an arbitrary-input detector | **tested:** only matrix elements in the declared two-dimensional `A/B` restriction enter the positive theorem | **tested:** target and two reference sites have fixed declared occupations in each branch | **tested:** all eighteen occupation-parity modes are physically represented, but sensitivity is proved only on the coherent `A/B` mode and fails after its dephasing | **tested:** one three-cell calibration block; the dephased actual/deleted flag residual is zero | **unknown/not claimed:** arbitrary even states, scattering packets, and autonomous collision ensembles were not tested | action sensitivity is retained only on the declared coherent calibration domain |
| `N=2` route does not separate `W_g` from `Q` support | **tested:** the two restricted logical diagonal elements of `W_g` and `exp(i gQ)` coincide | **tested:** one co-located target and its separated singleton sites give the same binary contact condition as pair count | **tested:** the two collision-path logical modes have identical actual/threshold flag densities | **tested:** the complete declared `N=2` two-branch block gives exact residual zero | **unknown/not claimed:** other spatial references and lattice processes were not tested; the Cycle-289 `N=4` block is an explicit counterexample to a broader claim | equality is fixture-specific and cannot support unconditional-invisibility or support-equivalence claims |

No per-element, per-site, per-mode, or per-block negative is promoted to an
untested lattice-wide statement. All lattice-wide entries remain
unknown/not claimed.

### N6 — partial-closure path scan

Constructive import-retirement paths remain live:

1. generate the `A/B` collision coherence by ordinary number-conserving local
   transport from a homogeneous incoming wavepacket;
2. synthesize `H_AB/SWAP` from one selected nearest-neighbor apparatus law;
3. make action and current transduction one indivisible local collision update
   and rerun factor-deletion controls;
4. export the signed flag into the Cycle-286 outgoing carrier while keeping
   its actual-action sensitivity;
5. attach lawful occurrence and Record formation only after that physical
   common-law connector closes; and
6. compare several equal-`Q`, fixed-total-number spatial motifs to remove
   dependence on one calibrated branch pair.

These are physics implementations, not terminology repairs. No current
result requires an axiom edit, and no approved primitive is being silently
reclassified as a wall.

### N7 — steelman

> A hostile constructive reviewer should say that the supplied collision
> reference is close to ordinary scattering rather than an exotic oracle.
> Two number-conserving graph FSWAPs already connect the separated and
> co-located configurations, the actual uncontrolled `W_g` supplies the
> relative phase, and the connected even algebra contains the comparator.
> A local wavepacket splitter/recombiner or collision current could therefore
> prepare and read this motif under one repeated law. The successful `N=2`
> and equal-`Q` `N=4` routes show that unconditional action is visible; the
> remaining imports are implementation targets, not evidence of substrate
> impossibility.

Accepted. The next campaign should build exactly that common-law splitter,
collision, recombiner, and outgoing carrier.

### N8 — cross-cycle echo

| earlier wall | later mechanism | Cycle-289 implication |
|---|---|---|
| fixed-number local density is blind to a scalar contact phase in Cycle 285 | cross-number matter reference and controlled Ramsey supplied phase relations | a same-total-number spatial collision relation also retires scalar blindness |
| Cycle-282 `Q` sequencer is blind to actual `W_g` deletion | Cycle-285 phase comparators resolve actual action conditionally | equal-`Q` spatial branches remove the support-only ambiguity without controlled `W_g` |
| Cycle-281 close is faithful only to declared `Q` calls | Cycle-286 exports that close but retains `W_g` blindness | Cycle 289 supplies an actual-action-sensitive local flag, not yet the common outgoing law |
| Cycle-271 local quotient lacks prepared states | Cycle-275 supplies algebraic matched states but not bounded preparation | Cycle 289 keeps its collision state explicitly supplied and targets preparation next |

The repeated pattern is progressive constructive closure by introducing and
then auditing an explicit relational reference. No stable shared obstruction
survives these counterroutes.

**N1–N8 status: PASS for the narrow conditional construction and its scoped
negative boundaries.**

**N1–N8 status: FAIL for any broad reference-free no-go, minimum-content
theorem, or axiom-pressure claim.**

## 11. Exact verification summary

The runner requires all checks to pass and prints

```text
RESULT CYCLE289_UNCONTROLLED_CONTACT_COLLISION_CURRENT_GREEN
```

The load-bearing outputs are:

- flag-one weight `0.637795123412256` for ordinary `W_g`;
- target-deletion, threshold, and global-phase flag weights `0`;
- signed flag-current magnitude `0.9612752029752998`, reversed by
  `W_g^dagger`;
- dephased actual/deleted flag residual `0`;
- exact two-FSWAP branch exchange;
- zero local-check/Wilson leakage at `L=3,4,5,6` with held-out `L=6`;
- bounded physical-M2 support independent of `L`;
- all `24*27=648` frame-translation cases; and
- one-particle identity and mass-fixture preservation.

Pass counts are executable regression controls, not independent empirical
predictions.

## 12. Optimal next campaign

Build a **common-law collision splitter/recombiner with action-sensitive
outgoing current**. Start from a number-conserving incoming packet, generate
the `A/B` spatial coherence by bounded local transport, apply ordinary
unconditional `W_g`, recombine into the signed M2 current, and launch it on the
Cycle-286 carrier under one repeated local update. Require deletion of the
actual target `W_g` to prevent launch, threshold/global/adjoint controls,
blank/reference genesis accounting, collisions and reverse-law audit,
zero leakage, held sizes, all-24 covariance, and strict occurrence/Record/time/
energy firewalls.
