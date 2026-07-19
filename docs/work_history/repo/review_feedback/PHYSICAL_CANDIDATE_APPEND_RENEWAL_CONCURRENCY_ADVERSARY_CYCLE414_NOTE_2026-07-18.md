# Physical candidate-append renewal/concurrency adversary — Cycle 414

Date: 2026-07-18

Authority: none

Audit: unset

Constitutional effect: none. This cycle changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface and
drafts no axiom language.

Companion runner:

```text
scripts/physical_candidate_append_renewal_concurrency_adversary_cycle414_2026_07_18.py
```

## Result up front

Cycle 414 constructs a bounded reversible renewal/concurrency adversary for
the Cycle-406 coherent candidate append.

Two adjacent preallocated target blocks are mirrored around one shared
95-M2 physical source/predicate spine. The spine contains one Cycle-399
response M2, one lawful Cycle-364 predecessor and payload, and one copy of the
readiness, freshness, presence, and provenance interfaces. The two logical
targets are distinct proper-cubic neighbors of the same predecessor. Each
target retains its own blank detector, reversible conjunction work, content,
occupied bit, and allocation-history bit.

They therefore use one shared lawful predecessor and response, not duplicated
predecessor/response preparations.

For distinct target requests, the fixed circuit coherently fills both target
registers. The two local calculations commute exactly. They share one cause:
there is one physical response M2, not two response preparations. Fanout of
that one control does not turn the two labels into independent confirmations;
a copied response is not independent confirmation.

For a same-target request, one supplied physical alias bit drives a local
collision latch. A reversible suppression bus temporarily clears the one
response control while both fixed append calculations run, then restores it.
Both candidate writes remain blank and a coherent collision label remains.
The inverse clears that label and returns the entire input exactly. There is
no priority query or host branch query.

No host branch query occurs anywhere in the physical update.

Occupied and dirty refusal remains target-local. If one target is already
occupied or contains dirty content with occupied zero, that target is
unchanged while the other lawful blank target still computes. All four A/B
occupied and dirty cases reverse exactly.

Finally, one preallocated blank 32-M2 shadow reversibly swaps with target A's
30 content bits, occupied bit, and allocation-history bit. The filled
candidate moves into the shadow, target A becomes blank, and the same fixed
append block can run once more. Reversing the second calculation, exchange,
and first calculation restores every bit. This is one explicit blank-register
exchange candidate. It consumes one supplied blank reserve and creates no new
capacity.

The coherent reusable candidate labels are not actual Records. The collision
label and allocation histories are not Records. Exact reversibility is not
permanence. One preallocated exchange is not a renewal law and is not resource
conservation. Repeated labels controlled by the same response are not
independent confirmations. No law, branch, actual member, Record, edge, or
history is selected. Actual dependency depth remains four.

All squared-norm quantities are sector weight, not probability or Born
weight. Compiler layers and dependency depth are not time, rate, interval, or
proper time. All 24 proper-cubic frames are spatial. No physical energy,
stress, source, resource, gravity, or axiom content is inferred.

## Bounded physical construction

The represented installation has 388 M2:

| component | represented M2 |
|---|---:|
| first complete Cycle-406 block, including the shared response | 224 |
| second mirrored block after sharing the 95-M2 source spine | 129 |
| alias, collision, and response-suppression bits | 3 |
| target-A blank reserve shadow | 32 |
| total | 388 |

One response M2 is already counted in Cycle 399, so Cycle 414 adds 387 M2 to
the 4,855-M2 common installation, for 5,242 represented M2 in the composed
test. These are exact construction counts, not minimum-content claims.

The distinct/collision circuit has 549 layers and 969 primitive gates. The
exchange-and-one-repeat route has 824 layers and 1,547 primitive gates:

```text
549-layer two-target/collision circuit
+ 3-layer, 96-CNOT exchange
+ 272-layer target-A repeat calculation
= 824 layers and 1,547 gates.
```

Every gate is X, CNOT, or Toffoli. Maximum primitive support is three M2 and
every support is connected nearest-neighbor in the declared micro-layout.
Every layer is conflict-free. The same schedule is applied to every binary
basis input of a declared route; no gate list is selected from the state.
Ordered layers are compiler schedule, not physical time.

The shared spine is literal. The second block does not contain another
response M2, predecessor payload, proposal payload, readiness/freshness
packet, presence packet, or provenance bit. Both mirrored conjunctions read
the same physical indices.

## Distinct-target and collision truth table

With the common predecessor, payload, predicates, and response equal to one:

| request/target state | target A | target B | collision | inverse |
|---|---|---|---:|---|
| two distinct blank targets | candidate payload, occupied 1, history 1 | candidate payload, occupied 1, history 1 | 0 | exact |
| same-target alias, both blank | blank | blank | 1 | exact |
| A occupied, B blank | A unchanged | B candidate | 0 | exact |
| A dirty/unoccupied, B blank | A unchanged | B candidate | 0 | exact |
| A blank, B occupied | A candidate | B unchanged | 0 | exact |
| A blank, B dirty/unoccupied | A candidate | B unchanged | 0 | exact |

For the distinct case, applying A then B and B then A gives identical complete
388-bit outputs. The shared predecessor, payload, response, and all predicate
inputs are spectators. Both candidate labels point to the same predecessor
but to different target sites.

The same-target bit is a supplied physical concurrency-context label. Cycle
414 compiles one falsifiable no-priority collision response to it; the cycle
does not derive the alias bit, choose this arbitration law, or establish
full-lattice same-target arbitration.

## One blank-register exchange and repeat use

The exchange route begins with two distinct blank targets and one blank
32-M2 reserve:

1. the common-response circuit computes candidates A and B;
2. 96 fixed CNOTs implement 32 local SWAPs between A and its reserve;
3. target A is now exactly blank while the reserve carries A's complete
   content/occupied/history candidate label;
4. the unchanged target-A 272-layer calculation runs again from the same
   shared response; and
5. the final state contains target A, target B, and reserve candidate labels
   in the same coherent response sector.

The reverse order erases the repeat label, returns the exchanged candidate to
target A, and reverses the original two-target computation. The enlarged
inverse residual is exactly zero. If the response is zero, all target and
reserve registers remain blank through the same schedule.

This does not triple the evidence. All three final labels have one common
response cause and the joint-label sector has the same squared norm as the
one-response target sector. The construction merely spends one supplied
blank register to make one target blank again. It neither generates another
blank nor proves an indefinite reservoir, autonomous garbage collection,
thermodynamic reset, renewal law, or conserved physical resource.

## L5 and blind held L6

The source laws, source depth, initial column, response projector, dual layout,
payload, predecessor, alias/collision circuit, exchange, repeat calculation,
and readout are frozen before blind held L6.

For both training L5 and blind held L6, and both A-to-C and C-to-A
orientations, the response-sector values are:

| source route | A-to-C sector weight | C-to-A sector weight |
|---|---:|---:|
| unit-weight | `5.958479723237607e-06` | `5.958479723237605e-06` |
| coefficient-two | `3.0046754132975383e-05` | `3.004675413297537e-05` |

On distinct targets, the A-candidate, B-candidate, and joint A-and-B weights
all equal that single target-sector value. On the same-target route, the
response-active collision-label weight equals the target-sector value and the
candidate-label weight is zero. After exchange and repeat, the reserve and
joint A/B/reserve weights again equal the same single target-sector value.
They do not add.

The distinct, collision, and exchange/repeat global inverse residuals are
exactly zero in every route/size/orientation case. L5 and blind held L6 agree
without retuning. Reciprocity and the unit/coefficient distinction survive.

## Proper-cubic covariance and physical fixtures

All 24 proper-cubic frames rotate the shared spine, both target blocks,
predecessor and target labels, collision circuit, and blank shadow. Every
rotated gate support remains connected nearest-neighbor. Payload mapping,
distinct-target labels, collision suppression, exchange/repeat labels, and
all inverses have zero failures.

The inherited source update has zero processed covariance residual, raw
maximum `1.8619006149354548e-16`, 576 frame-group tests with zero failures,
and 4,096 translation tests with zero failures. The frames are spatial
covariance controls, not clock transformations.

Every coherent branch preserves the complete shared Cycle-364 predecessor
payload and both Cycle-399 counter Record identities. The Record hash remains

```text
2bc2b272629ef89db2910d9598e8ef523f4ac3c2d998b8bf5ff1d719c5da11e7
```

The new gates act as identity on the matter factor. Retained fixtures are:

- Cycle-219 mass `0.4534056541748851`;
- global Q one;
- matter number `3.0 -> 3.000000000000002` within tolerance;
- zero coefficient-two and unit-weight vector commutators;
- 645 nontrivial Cycle-230 contact columns;
- six held matter Gram residuals at most `7.771561172376096e-16`; and
- Cycle-396 source intertwiner `9.757364575248792e-15`.

None of these fixtures selects the concurrency, exchange, formation, or
actualization law.

## Deletion, leakage, and lawful-domain controls

The nominal local workspace and response-suppression leakage is zero.

Deletion controls are visibly load-bearing:

- deleting the collision latch or response-suppression CNOT lets both
  same-target candidates write;
- deleting A's allocation-history latch blocks A decoding while B still
  computes;
- deleting B's latch blocks B while A still computes; and
- deleting one load-bearing exchange CNOT prevents the declared complete
  reserve/target-repeat state.

The encoder rejects a nonbinary alias, malformed payload width, unlawful
predecessor, nonblank reserve, and nonbinary enlarged state. Occupied and dirty
targets are lawful refusal cases rather than encoder rejections. A deletion or
route failure would remain an implementation result, not a shared substrate
obstruction.

## Exact intertwiner and semantic boundary

Let `E_414` encode one Cycle-399 bridge state, one shared Cycle-364 source
spine, two target/work blocks, blank collision/suppression bits, one physical
alias label, and one blank reserve. Let `G_414` be the declared distinct,
collision, or exchange/repeat truth-table action, and let
`G_physical,414` be the corresponding fixed X/CNOT/Toffoli schedule. The
runner verifies on every declared basis case and the coherent held source
states

```text
E_414 G_414 = G_physical,414 E_414.
```

The dual-register permutation intertwiner and enlarged inverse residuals are
zero. The inherited Cycle-396 source-factor intertwiner is
`9.757364575248792e-15`.

The exact semantic boundary is:

- a filled target is a coherent candidate payload, not a framework Record;
- a filled reserve is the same kind of reversible candidate label, not an
  archived Record;
- allocation history distinguishes reversible inputs but is not permanence;
- the collision bit is a reversible proposal label, not occurrence or
  actuality;
- two labels driven by one response are not independent confirmations;
- one blank exchange is finite capacity motion, not blank genesis, a renewal
  law, resource conservation, energy, or thermodynamic reset; and
- actual Cycle-170/255 Records, edges, and dependency depth remain unchanged
  at depth four.

No pointer, occupied bit, collision label, reserve label, count, circuit
layer, sector weight, or contact response is promoted to Record, time,
probability, energy, source, resource, stress, gravity, or an approved
primitive.

## Supplied, derived, and open inventory

Supplied:

1. the Cycle-399 coherent source/counter state and exact target-reservoir
   response interface;
2. the Cycle-364 lawful payload, predecessor Record, presence, readiness,
   freshness, and provenance interfaces;
3. two mirrored preallocated target/work blocks and their target addresses;
4. the physical same-target alias bit and the decision to use no-priority
   two-write suppression;
5. one blank 32-M2 reserve and the fixed exchange/repeat invocation;
6. the physical layout, primitive basis, routing, schedules, finite L5/L6
   boundaries, frames, and readout.

Derived:

1. exact distinct-target commutation and two candidate labels from one common
   response cause;
2. exact same-target collision labeling, write suppression, response restore,
   and inverse;
3. target-local occupied/dirty refusal;
4. exact blank exchange, one repeat calculation, and complete reverse cleanup;
5. held reciprocity, covariance, deletion/domain visibility, Record identity,
   and matter-fixture preservation.

Open:

1. selection of the concurrency, exchange, or Record-formation law;
2. autonomous alias/address comparison, priority/arbitration, invocation,
   target allocation, and response/predicate genesis;
3. actual Record formation, irreversible permanence, actual-member selection,
   and dependency-edge admission;
4. unbounded blank genesis, repeated renewal, garbage handling, volume
   collisions, and a physical resource/conservation law;
5. normalized statistics, sampler, frequency theorem, or Born rule;
6. interval/rate/proper time, physical source/stress/energy, reciprocal
   metric/clock response, and gravity.

## Dependency-ledger effect

| wall | Cycle-414 movement | exact residual |
|---|---|---|
| `C_ref` | one common predecessor/response now feeds exact distinct-target, collision, and one exchange/reuse candidate while preserving all prior identities | actual formation/permanence, selected identity law, actual member, autonomous alias/reference/blank genesis, and indefinite renewal |
| `C_num` | unchanged; shared sector weights remain one response coordinate and are not counted as confirmations | selected/calibrated grade, sampler, frequency, Born law, and actuality |
| `C_wrap` | unchanged; collision order, circuit layers, and repeated use are not time | actual history, interval, unit, recurrence, synchronization, rate, lapse, and proper time |
| `C_int` | preserved; the shared response remains contact-sensitive and the 645-column contact fixture survives | interaction-selected occurrence, arbitration, stability, rate, and source meaning |
| `C_local` | narrowed: two target blocks commute, same-target collision is physically labeled/suppressed, occupied/dirty targets refuse locally, and one blank exchange/reuse is exact | autonomous address comparison and law selection, repeated renewal, adjacent-volume allocation/collision policy, primitive genesis, commit, and homogeneous invocation |
| `C_source` | unchanged in meaning; one operational response controls all candidate routes | physical energy/stress/source functional, resource identity, conservation, and reciprocal metric/clock/gravity law |

This is a bounded positive construction. It makes no negative,
minimum-content, shared-obstruction, or axiom-pressure claim. The full N1--N8
negative-claim gate is therefore not invoked to promote a no-go. Ordinary
constructive routes remain open for every listed residual.

No Thirring engine is used or compared.

## Reproduction

```bash
python3 -u \
  scripts/physical_candidate_append_renewal_concurrency_adversary_cycle414_2026_07_18.py
```

Expected cold result:

```text
SUMMARY {'pass': 14, 'fail': 0}
RESULT PHYSICAL_CANDIDATE_APPEND_RENEWAL_CONCURRENCY_CERTIFIED
```
