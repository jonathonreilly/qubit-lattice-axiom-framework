# Cycle 719: recurrent matter-to-history physical-M2 controller

Date: 2026-07-26

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Primary runner:
[frontier Cycle-719 recurrent matter/history controller](../scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py)

Independent compiled-orbit checker:
[frontier Cycle-719 recurrent controller independent check](../scripts/frontier_cycle719_recurrent_matter_history_controller_independent_check_2026_07_27.py)

Load-bearing inherited surfaces:

- [Cycle 718 spatial ACK and Cycle-612 bridge](PHYSICAL_M2_SPATIAL_ACK_CYCLE612_INTERVAL_BRIDGE_CYCLE718_BOUNDED_THEOREM_NOTE_2026-07-26.md);
- [Cycle 715 recurrent directional bank](RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md);
- [Cycle 713 physical endpoint instrument](PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md);
- [Cycle 712 joint physical-M2 update](JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md);
- [Cycle 610 relational duration](work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md); and
- [Cycle 612 causal order](work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md).

## Question

Can the actual Cycle-713 matter-generated endpoint, rather than a presented
direction register, feed the fixed two-rail recurrent controller on one
literal physical-M2 chart and return through the same encoding?

## Constructed joint word

On the declared joint code, the physical event word is

```text
G_physical = Cycle713 physical decode/instrument ; H^130 ; physical re-encode,
H = R Q.
```

The landed Cycle-713 endpoint pointer M2 and the recurrent controller source
pointer are the same assigned site, `(-8,-1,1)`.  There is no register copy or
host direction insertion between the two components.  The physical source cap
reconstructs the exact landed Cycle-713 word: 1,400 primitives, 17,798 routed
nearest-neighbor gates, and routed-word SHA-256
`185fdb5270931877474ef720926bde016ff2fece03c1b8b58588e52e517d04f7`.

The fixed padded controller has 130 stations.  One `H` has 61,562 semantic
controlled gates, 740,226 physical primitives, and 13,315,466 routed
nearest-neighbor gates.  The complete joint event therefore has:

- 96,230,780 physical primitives;
- 1,731,028,378 routed nearest-neighbor gates;
- maximum route distance 45;
- zero route, operand-order, route-return, coordinate, frame-product, or
  translation failures;
- 24 proper-cubic frames and 576 ordered products;
- 240,331 route-swap deletion opportunities (not executed composed-state
  deletions).

The composed structural SHA-256 is
`2ef0c643935b67e41384e15a3ecfceb3e50d1339dc254e33533eb8d1df378254`.
This is a digest of the Cycle-713 cap, orbit count, fixed `H`, and its route
blueprint.  It is not represented as a retained 1.7-billion-gate tuple.

The physical same-E statement is compositional: Cycle 713 supplies the landed
physical decode/instrument/re-encode intertwiner, and the pointer-site and
route certificates bind it to the controller on the same physical chart.  The
primary runner executes the actual 61,562-gate `H` word 130 times on all six
origin-zero Cycle-713 branches: 8,003,060 semantic gate applications per
branch.  It agrees exactly with the algebraic orbit, returns A0/B/work exactly,
and its actual inverse restores every input.  A fresh full encoded vector over
all ambient M2 is not materialized, and the 1.7-billion-gate routed word is
counted rather than retained or fully executed.

The joint transition reference is deliberately derived from the same decoded
matter word used in the joint update.  Its small residual therefore tests the
controller composition, not an independent rederivation of matter.  The
independent matter anchor is the landed Cycle-713 exhaustive instrument:
coarse `exterior_column` is compared with the literal endpoint maps on all
4,096 columns, with maximum residual `8.121767085755588e-16`.  Cycle 719 pins
that runner at SHA-256
`b61f98d0b44c1496883e8ab2ae1db065772ed053c77b6661a0153086acfd0e2f`
and requires both the pin and exhaustive check to pass.

## Coherent recurrence

The held amplitude runner uses the algebraic `run_orbit` form rather than the
equivalent 29,086-gate allocator shortcut.  The independent gate-level check
above establishes exact equality of that orbit with compiled `H^130` on the
six first-event branches.  Longer held recurrence uses the algebraic orbit;
it does not re-execute 8,003,060 compiled gates on every later history branch.

| Test | maximum joint residual | inverse residual | largest support | packets |
|---|---:|---:|---:|---:|
| all 12 one-particle origins, two events | `5.013921050966962e-16` | `4.451712786953815e-16` | 12 | 2 |
| held five events | `1.2564943544027162e-15` | `5.552530333181167e-16` | 30 | 5 |
| full 24-event fill | `4.087754328527302e-15` | `5.826645898322889e-16` | 144 | 24 |

Norm residual is at most `1.1102230246251565e-15`.  Decode, matter-number,
pointer-cleanup, bank/link transient, and token-return failures are all zero.
Thus the declared one-particle joint code obeys, by the explicit composition,

```text
E_joint G_matter+history = G_physical E_joint.
```

The history is a reversible orientation packet chain.  It is not an
inaccessible Record or realized history.

## Controls and deletions

- Deleting the packet station changes the coherent output by
  `0.48693948205126425`.
- Deleting the source finalizer changes it by the same residual and leaves a
  dirty transient row.
- The actual Cycle-713 endpoint prewrite and OR-Toffoli deletions each reach
  residual `sqrt(2)` on its exhaustive 4,096-column instrument surface.
- Deleting the compiled packet station changes 35 data bits on an actual
  endpoint branch; deleting the compiled source finalizer changes three.
- Zero-token, adjacent-two-token, distant-two-token, and token-offset orbits
  each differ from the lawful result by `0.48693948205126425`; controller token
  number and B-rail return remain exact.  These are unlawful-sector controls,
  not a derivation of the unique-token sector.
- The one-particle mass residual remains zero.  Free coin, FSWAP, internal
  stream, reverse, seam, and contact residuals remain at their landed values;
  the largest inherited residual is the coin-stage `6.243831416688722e-15`.

## Local refusal primitive

A separate five-M2 local circuit computes

```text
syndrome := B OR work
data-X only if A AND NOT syndrome.
```

It uses 34 one/two-M2 primitives and 60 routed nearest-neighbor gates with
maximum route distance 4 and zero route failures.  All 16 clean-syndrome truth
rows are exact; all six invalid rows with a live A token are refused and retain
the syndrome; two independent deletions alter six rows.  All 16 dirty-syndrome
rows change the declared action, so clean syndrome is explicit.

This is constructive evidence that dirty B/work need not remain an unchecked
assertion.  It is not yet wrapped around every controlled data macro, and it
replaces neither unique-token genesis nor clean-syndrome genesis.

## Covariance boundary

The landed Cycle-713 endpoint truth supplies the active frame anchor.  The
controller and joint program checks are narrower: physical coordinates,
nearest-neighbor routes, translations, and proper-cubic group closure restore
under all 24 frames and 576 products.  This is passive transported-coordinate
covariance.  Controller program content and the ambient encoded matrix are not
rebuilt and executed independently in every frame.

The 130 controller applications are fixed circuit ordinals.  They are not a
clock, duration, rate, or physical time.

## Supplied / derived / open

Supplied:

- exactly one controller token at the source, a finite oriented program ring,
  and the source boundary;
- clean Cycle-713 code, bank/link/route, controller, and syndrome genesis;
- fixed `Q`-before-`R` and bounded macro order;
- `BINDER/ACTUAL/ADMISS/LAW` acceptance inputs;
- the landed matter law and proper-cubic coframe.

Derived:

- the actual Cycle-713 physical pointer is the controller input site;
- a same-chart compositional physical word from matter input through accepted
  packet output and re-encoding, with actual compiled `H^130` checked on all
  six first-event branches and full routed counts kept distinct;
- coherent amplitude-level recurrence through the full 24-packet capacity;
- exact same-E controller/data return and inverse on the declared code;
- held, compiled-deletion, unlawful-token, route, translation, active endpoint,
  and passive controller-coordinate controls;
- a bounded dirty-B/work local refusal primitive;
- unchanged free/seam/contact/mass fixtures.

Open:

- autonomous preparation or local enforcement of the unique-token, code, and
  clean-syndrome sector;
- integration of the refusal primitive into every controlled macro;
- removal of the unique source boundary and oriented finite program ring if a
  boundary-free translation-invariant law is required;
- objective actuality/admissibility rather than supplied acceptance bits;
- post-capacity renewal and separated multi-source composition;
- inaccessible inverse, permanent Record, Born/history law, source/gravity
  meaning, and attachment to a prediction surface.

## No-go discipline gate

The N1-N8 gate is **FAIL for any no-go**.  The disposition is
`positive-same-chart-composition-with-explicit-genesis-supplies`.

### N1 — alternatives

The same-chart matter/controller route is positive.  Live constructive routes
for the remaining domain supply include local Gauss constraints, boundary
charge sectors, paired controller excitations, local syndrome/refusal layers,
finite-colour wavefronts, and renewal rails.  None is ruled out.

### N2 — wall independence

Matter-to-controller register presentation is closed.  Unique-token genesis,
clean-syndrome genesis, boundary-free program geometry, objective admission,
multi-source composition, renewal, Record, Born, and source meaning remain
distinct walls.

### N3 — hidden-wall scan

The source boundary, oriented ring, unique token, clean work/syndrome, fixed
layer order, finite capacity, accepted-event flags, transported coframe, and
compositional rather than ambient-vector same-E proof are explicit.

### N4 — residual matching

The coherent residuals test the actual Cycle-713 decoded word followed by the
algebraic orbit.  A separate actual compiled `H^130` test covers all six
first-event branches, its inverse, register return, and two compiled deletions.
The landed word digest and shared pointer site bind the physical caps; routing
checks one `H` and supplies explicit multiplied full-orbit counts.  These tests
do not certify later-branch compiled execution, active controller-content
covariance, genesis, objective admission, permanent Record, or physical time.

### N5 — rhetoric resolution

“Actual endpoint composition” means no host supplies direction or copies a
pointer register between matter and controller.  “Same-chart physical word”
means the landed physical cap and fixed routed `H` share one assigned chart and
form the stated finite word.  It does not mean the full routed word is retained
or executed on every held branch, active controller-content covariance, an
autonomous cosmological initial sector, or a materialized ambient state vector.

### N6 — partial-closure paths

The next constructive step is to integrate a local enforcement/refusal layer
around the controller macros and test separated multi-source sectors.  A
parallel route can try local Gauss-law preparation.  No axiom change is
requested.

### N7 — steelman

A hostile reviewer should accept that the former presented endpoint fixture
and runtime host sweep are absent from the joint event: matter writes the
physical pointer, the same fixed `H` processes it, and the code is re-encoded.
The reviewer should reject full autonomy while unique-token, clean-code,
clean-syndrome, source-boundary, and admission supplies remain.

### N8 — cross-cycle echo

Cycle 713 closed the bounded physical endpoint instrument but left its
consumer supplied.  The recurrent controller closed runtime program
selection but left its matter input presented.  Their same-site composition
closes that reciprocal interface.  The repeated remaining echo is genesis and
admission, not evidence for an impossibility or axiom pressure.

## Verdict boundary

The actual landed matter endpoint and the fixed recurrent controller now form
one bounded same-chart compositional physical-M2 event compiler on the declared
code.  The compiled controller closes exactly on all six first-event branches;
the proven-equal algebraic orbit reaches 24 coherent accepted packets with exact
inverse and active controls.  This is a meaningful bounded bridge closure.  It
is not full later-branch compiled execution, active controller-content
covariance, autonomous sector preparation, boundary-free recurrence, objective
admission, Record, Born/history, source/gravity, prediction, minimum-content,
no-go, shared-obstruction, or axiom-pressure evidence.
