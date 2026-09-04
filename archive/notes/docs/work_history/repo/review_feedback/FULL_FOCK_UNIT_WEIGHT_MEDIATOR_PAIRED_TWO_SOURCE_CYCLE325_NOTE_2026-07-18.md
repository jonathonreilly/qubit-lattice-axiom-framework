# Full-Fock unit-weight mediator-paired two-source compiler — Cycle 325

Date: 2026-07-18
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/full_fock_unit_weight_two_source_cycle325_2026_07_18.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status.

## Result up front

Cycle 325 constructs a full-Fock mediator-paired unit-weight auxiliary compiler
on the same complete Cycle-315 `M64 tensor M64` physical seam used in Cycle
322. The source vertex is second-quantized over all 64 local Fock masks at both
endpoints. It preserves local matter number, global Q=1, and

```text
P_matter + P_mediator + P_auxiliary
```

with unit coefficient on each term. It coexists with the actual Cycle-230
contact and the literal edge FSWAP. On the declared code space, for both AB and
BA endpoint roles,

```text
E_unit G_unit = G_physical,unit E_unit.
```

The maximum forward residual is `1.38993e-15`; the conjugate inverse residual
is `2.53556e-15`. The 4,096-column seam remains isometric on `L=3,4` and held
`L=6`.

The full two-source response is nonzero and symmetric:

```text
[[0.7712291018346235,    0.00002429213394509795],
 [0.000024292133945097934, 0.7712291018346235    ]].
```

Its reciprocity residual is `1.69407e-20`. The matrix is unchanged across
`L=3,4,6`. Receiver deletion and pair-stream deletion make the tested
off-diagonal entry exactly zero.

The constructive route has a precise novelty boundary. Cycle 320 carries its
auxiliary direction with the one matter carrier. The complete Fock seam has no
distinguished carrier identity. Cycle 325 therefore uses a different supplied
co-stream program: the auxiliary remains locally paired with the mediator and
the bounded stream translates the pair together. This program is not derived
from Cycle 320's catch-up law and does not establish that a matter-carried
full-Fock extension exists without an extra tag or species.

The direct one-carrier matter-carried extrapolation remains exactly
norm-preserving but gives zero two-update cross-response on this preparation.
That is a route-specific response result. Cycle 320 itself does not fail: its
one-carrier recurrent theorem and catch-up controls remain intact.

The result is a dimensionless occupation-response compiler. It is not energy,
not stress, not gravity, not metric response, and not time. No physical
momentum calibration, source tensor, force law, or clock relation is derived.

## Exact full-Fock unit-weight source

For endpoint `X`, local direction `d`, and its opposite `reverse(d)`, define

```text
T_X = sum_d (
        c^dagger_X,reverse(d) c_X,d
          tensor |F_X,d; A_X,d><R_X|
      + c^dagger_X,d c_X,reverse(d)
          tensor |R_X><F_X,d; A_X,d|
      ),

V_X(theta) = exp(+i theta T_X).
```

`F` is the mediator direction and `A` is the auxiliary direction. The active
endpoint space has dimension `64 * 7 = 448`: one reservoir label plus six
correlated source labels for every local fermion mask. The exchange has rank
112. Pauli signs are calculated for every allowed local hop.

The source changes matter direction `d -> reverse(d)`. Hence its matter-vector
change is `-2 e_d`; the mediator and auxiliary each carry `+e_d`. The three
unit-weight terms balance exactly. The executed operator controls are:

| local control | residual |
|---|---:|
| unitarity | `1.44129e-15` |
| `[V_X,Q]` | `0` |
| `[V_X,N_X]` | `0` |
| `[V_X,P_x]` | `0` |
| `[V_X,P_y]` | `0` |
| `[V_X,P_z]` | `0` |
| maximum 24-frame source covariance | `8.80775e-16` |

For all six one-particle directions the emitted pair weight is
`0.1258992161287137...`; the vector-balance residual is at most
`1.11023e-16`. Deleting `P_auxiliary` raises the three operator commutators to
`2.823561997406967`, `2.8235619974069666`, and
`2.8235619974069666`.

`Q` counts the reservoir or mediator excitation; the auxiliary is a neutral
partner on the declared pair branch. The fixed global-Q1 sector and this
charge assignment are supplied.

## Complete seam, number, and contact

The matter code contains all 4,096 states of the two six-mode cells, with
total number `0,...,12`. Each source factor preserves both endpoint matter
numbers:

```text
[V_A,N_A] = [V_A,N_B] = [V_B,N_A] = [V_B,N_B] = 0.
```

The two source factors commute exactly. Their commutator with the contact
factor is `7.86448e-17`. Matter coin, edge FSWAP, and contact preserve total
matter number exactly. FSWAP changes the local number split on some states, so
only the source factors preserve each local count separately.

The naive one-one truncation has FSWAP leakage operator norm `1`. The
second-quantized source avoids that truncation and acts on the complete seam.
The actual Cycle-230 contact remains nontrivial on 4,047 columns; deleting it
has operator norm `1.9911500883709052`.

## Supplied mediator-pair program

The global-Q1 source sector contains either reservoir `R_A`, reservoir `R_B`,
or one mediator-plus-auxiliary pair. A lawful link label is

```text
(field cell y, field direction f;
 auxiliary cell y, auxiliary direction a).
```

The field coin acts on `f`; the auxiliary direction receives the identity
coin. Thus `f` and `a` can differ after the coin. The pair remains at one cell.
The supplied bounded stream translates both spatial labels by `e_f` and
retains `a`. The source acts only when the pair is onsite and `f=a=d`.

This gives lawful source-sector dimension

```text
2 + 36 L^3.
```

It enforces one mediator, one neutral auxiliary, and local spatial pairing on
the declared code. Moving only the mediator produces a stale unequal-cell
label outside that code. The runner exposes and rejects such a label.

The pair stream is a local permutation with an explicit inverse. It is a new
supplied auxiliary program. It is not inferred from an indistinguishable
matter carrier and is not evidence that the original matter-carried program
has a tag-free full-Fock lift.

## Physical lift and bounded support

The matter columns and bounded matrix-unit completions are inherited from
Cycle 315. Each physical source label adds one reservoir M2, six mediator M2,
and six auxiliary M2 per matter cell. A lawful pair occupies one mediator and
one auxiliary M2 at the same cell.

| edge role | forward EG | inverse EG | encoded norm | output norm |
|---|---:|---:|---:|---:|
| AB | `1.38993e-15` | `2.53556e-15` | `1.000000000000004` | `0.9999999999999992` |
| BA | `1.38993e-15` | `2.53556e-15` | `1.000000000000004` | `0.9999999999999992` |

The installed resource count is:

| resource | count |
|---|---:|
| inherited Cycle-315 M2 per cell | 29 |
| reservoir M2 per cell | 1 |
| mediator direction M2 per cell | 6 |
| auxiliary direction M2 per cell | 6 |
| total | 42 M2 per cell |
| inherited two-cell patch union | 83 M2 |
| extended two-cell patch union | 111-M2 |

This is bounded constant overhead. The physical factor is the Cycle-315 dense
edge matrix-unit completion with pair labels and off-code identity. The result
does not synthesize those matrix units from a smaller named gate alphabet.

| L | role | columns | physical rays | nonzeros | raw Gram maximum | minimum Gram eigenvalue |
|---:|---|---:|---:|---:|---:|---:|
| 3 | training | 4,096 | 63,488 | 65,536 | `1.77636e-15` | `0.9999999999999981` |
| 4 | training | 4,096 | 63,488 | 65,536 | `1.77636e-15` | `0.9999999999999977` |
| 6 | held | 4,096 | 63,488 | 65,536 | `1.77636e-15` | `0.9999999999999981` |

## Response and coefficient-two comparison

The response preparation is the same as Cycle 322: a symmetric one-one matter
state, one reservoir column at a time, and two complete update depths. The
factor order is matter coin, mediator coin, sources A/B, edge FSWAP, pair
stream, and contact.

| L | role | off-diagonal response | reciprocity residual | diagonal-exchange residual | norm drift |
|---:|---|---:|---:|---:|---:|
| 3 | training | `2.4292133945097934e-05` | `1.69407e-20` | `0` | `3.55271e-15` |
| 4 | training | `2.4292133945097934e-05` | `1.69407e-20` | `0` | `3.55271e-15` |
| 6 | held | `2.4292133945097934e-05` | `1.69407e-20` | `0` | `3.55271e-15` |

The coefficient-two comparison uses the same matter preparation, reservoir
columns, sizes, and update depth. Its off-diagonal entry is
`0.0006446410419510052`, about `26.5370` times the unit-weight pair entry. The
diagonal entries are the same `0.7712291018346235` in both constructions.

The suppression is explained by supplied program content: absorption requires
the mediator direction after its coin to equal the retained auxiliary
direction. It is a tested finite response difference, not a coupling
calibration or continuum prediction.

## Literal matter-carried comparator

The most direct one-carrier extrapolation moves the auxiliary cell by
`-e_a`, while the mediator moves by `+e_f`. It is a unitary permutation of the
source labels and retains norm through the tested updates. On the same two-step
preparation it gives

```text
[[0.7712291018346235, 0],
 [0, 0.7712291018346235]].
```

The zero cross-response occurs because the mediator and auxiliary separate,
so neither remote source receives the required onsite pair at the tested
depth. This comparator does not implement the complete Cycle-320 catch-up: the
one-carrier code also knows the carrier port, whereas an unmarked Fock mask
does not identify which occupied mode owns the auxiliary.

A faithful matter-carried full-Fock route therefore remains open. It can add
an explicit carrier tag, a distinguishable species, or another bounded
attachment mechanism. No claim of impossibility or minimum extra content
follows from the zero response.

## Covariance, translations, and firewalls

The second-quantized source is covariant under all 24 proper-cubic frames. The
Cycle-315 seam tests twelve endpoint-preserving frames and twelve frames with
endpoint reversal. Its processed complete-update covariance residual is zero;
the raw maximum is `2.16778e-16`.

The source/pair family commutes with all L=3 translations: 27 translations and
maximum residual zero. The pair stream rotates as a direction-indexed family;
source and auxiliary directions transform together.

The mass firewall is unchanged:

| control | value |
|---|---:|
| Cycle-219 mass fixture | `0.4534056541748851` |
| two-cell seam mass | `0.4534056541748851` |
| eigenvector residual | `3.85718e-16` |

The contact firewall retains 4,047 nontrivial columns and deletion norm
`1.9911500883709052`. The joint physical EG includes that contact factor.

## Deletions and lawful domain

| deletion or malformed input | result |
|---|---:|
| remove auxiliary vector term | P commutators `2.82356...` |
| delete receiver B | `A -> B = 0` |
| delete pair stream | `A -> B = 0` |
| literal opposite auxiliary catch-up | two-update `A -> B = 0` |
| stale unequal field/auxiliary cells | unit invalid-pair weight detected |
| `L<3`, `Q != 1`, unpaired branch, invalid edge | four rejections |
| delete contact | operator norm `1.99115...` |
| restrict matter to naive one-one product | FSWAP leakage norm `1` |

These controls separate the auxiliary vector content, its co-stream program,
the receiver, and the contact. They do not turn a route-specific response zero
into a substrate obstruction.

## Supplied structure, derived results, and open work

Supplied structure:

- complete Cycle-315 `M64 tensor M64` AB/BA matter code;
- Cycle-219 coin, literal edge FSWAP, and Cycle-230 contact;
- global Q=1 reservoir-or-pair sector;
- two second-quantized direction-reversing source vertices and source angle;
- six auxiliary direction M2 per cell, unit auxiliary vector weight, and
  identity auxiliary coin;
- local mediator/auxiliary pairing and the different supplied co-stream
  program;
- symmetric matter preparation, reservoir columns, two update depths, and
  response observable;
- dense physical completion and periodic sizes `L=3,4,6`.

Derived here:

- exact full-Fock Q, unit-weight vector, and matter-number identities;
- exact AB/BA physical intertwining with actual contact;
- nonzero symmetric response and coefficient-two comparison;
- frame, endpoint-reversal, translation, held-size, support, deletion, mass,
  contact, and lawful-domain controls.

Open:

- explicit full-Fock carrier-tag dynamics;
- a distinguishable auxiliary matter species;
- paired mediators or a matter-rest alternative;
- global Q2 with simultaneous two-source emission;
- multi-edge unit-weight recurrence and overlapping source programs;
- autonomous preparation and operational calibration to physical momentum,
  energy, stress, gravity, metric response, or time.

## TOE dependency ledger and maturity

| wall | Cycle-325 effect | remaining import |
|---|---|---|
| `C_ref` | unit-weight and coefficient-two responses now share one preparation and physical seam | reservoir column, symmetric matter state, two-update depth, and readout remain supplied |
| `C_num` | all matter numbers `0,...,12` coexist with one mediator/auxiliary pair | global Q2, local preparation, and multi-edge higher-Q closure remain open |
| `C_wrap` | unchanged | the factor schedule and update count are not clock time or rate |
| `C_int` | coefficient two is replaced on full Fock by two unit-weight direction registers | auxiliary identity, pairing, source angle, and co-stream are supplied candidate content |
| `C_local` | a bounded 42-M2-per-cell, 111-M2 edge-patch lift passes AB/BA EG | primitive synthesis, matter-carried tag, and overlapping multi-edge recurrence remain open |
| `C_source` | a reciprocal unit-weight two-source occupation response is derived | response is suppressed and remains global-Q1, prepared, dimensionless, and uncalibrated |

The result exchanges one supplied relative coefficient for supplied auxiliary
content and a different transport program. Current campaign maturity scores
therefore remain unchanged:

| lane | integrated | strict floor | conditional | maturity |
|---|---:|---:|---:|---:|
| operational quantum / Records | 63% | 29% | 90% | 3.4/5 |
| causal time / clock | 34% | 17% | 62% | 1.8/5 |
| inertia / matter | 75% | 36% | 96% | 4.2/5 |
| gravity / source / resource | 40% | 16% | 67% | 2.1/5 |
| Born / probability / realized history | 34% | 14% | 85% | 2.0/5 |

## No-Go Discipline Gate

The broad candidate negative is that a unit-weight auxiliary source cannot be
second-quantized on the complete Cycle-315 two-source contact seam with a
nonzero reciprocal response. The mediator-paired compiler is a bounded
counterexample. Stronger questions about literal matter carriage, tag-free
attachment, global Q2, alternate species, multi-edge recurrence, and physical
calibration retain live routes.

Gate status: **FAIL / DO NOT SHIP** the broad negative. There is no shared
obstruction and no axiom pressure.

### N1 — alternative routes

| route | marker | actual disposition |
|---|---|---|
| coefficient-two full-Fock sources | **ATTEMPTED** | Cycle 322 succeeds with 36 M2 per cell and off-diagonal response `6.44641e-4`, but supplies relative coefficient two |
| literal Cycle-320 matter-carried extrapolation | **ATTEMPTED** | norm-preserving opposite-direction extrapolation gives zero two-update cross-response; this does not retest or negate Cycle 320's one-carrier theorem |
| mediator-paired unit-weight auxiliary | **ATTEMPTED** | succeeds with exact ledgers, AB/BA EG, actual contact, and reciprocal response `2.42921e-5` |
| explicit full-Fock carrier tag register | **OPEN / UNTESTED** | no tagged occupied-mode Hilbert space or tag coin/FSWAP is compiled |
| distinguishable auxiliary matter species | **OPEN / UNTESTED** | no second species or exclusion rule is supplied |
| paired-mediator without auxiliary | **OPEN / UNTESTED** | no two-mediator Q sector or contact splice is built |
| global-Q2 simultaneous source sector | **OPEN / UNTESTED** | response columns still use one reservoir-or-pair excitation |
| multi-edge unit-weight source network | **OPEN / UNTESTED** | no overlapping source-edge recurrence is compiled |

The successful pair route disproves the broad negative. Five stronger routes
remain genuinely open.

### N2 — wall-independence audit

The collapsed walls for a stronger source theorem are:

- `W_tag`: build a full-Fock attachment/tag law;
- `W_species`: build or select a distinguishable auxiliary/mediator species;
- `W_Q2`: compile simultaneous source-sector occupation;
- `W_multiedge`: extend the unit-weight program over overlapping edges;
- `W_energy`: calibrate an operational energy/stress/source law.

| pair | closing first automatically closes second? | closing second automatically closes first? | independent? |
|---|---|---|---|
| `w_tag`, `w_species` | no | no | yes |
| `w_tag`, `w_q2` | no | no | yes |
| `w_tag`, `w_multiedge` | no | no | yes |
| `w_tag`, `w_energy` | no | no | yes |
| `w_species`, `w_q2` | no | no | yes |
| `w_species`, `w_multiedge` | no | no | yes |
| `w_species`, `w_energy` | no | no | yes |
| `w_q2`, `w_multiedge` | no | no | yes |
| `w_q2`, `w_energy` | no | no | yes |
| `w_multiedge`, `w_energy` | no | no | yes |

A tag need not define a new species. A species need not compile Q2. Q2 need not
solve overlapping edge programs. Multi-edge recurrence need not calibrate an
energy/source observable. No directed implication collapses another wall.

### N3 — hidden-wall scan

The executable literal scan covers the note and runner and reports zero hits.
The supplied inventory exposes the auxiliary M2, neutral charge, unit vector
weight, identity coin, local pairing, pair stream, source angle, global-Q1
sector, physical completion, factor order, preparation, sizes, and readout.

### N4 — residual matching

| exact witness | inherited boundary | Cycle-325 treatment | match? |
|---|---|---|---|
| `UNIT_WEIGHT_CARRIED_LINK_RECOIL_CYCLE320_NOTE_2026-07-18.md:38` | every direction term has unit weight | exact local target | yes |
| same file, line 30 | auxiliary carried on the matter cell | explicitly not claimed for the retained pair program | yes |
| `TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CYCLE322_NOTE_2026-07-18.md:112` | complete Cycle-315 Fock seam | inherited matter code | yes |
| same file, line 357 | full-Fock Cycle-320 alternative open | constructive pair route plus literal-route comparator | yes |
| same file, line 485 | global-Q2 campaign open | retained as an independent wall | yes |

The literal extrapolation's zero response is used only against that tested
two-update program. It is not used against an explicit tag, a species route,
different update depths, or the existing Cycle-320 one-carrier code.

### N5 — rhetoric audit

“Different supplied co-stream program” is a novelty boundary, not a negative
about matter carriage. “Zero cross-response” refers to one direct
opposite-direction extrapolation, one preparation, and two update depths. The
note does not promote that finite zero to an impossibility statement.

“Not energy” and related phrases are interpretation firewalls. The runner tests
diagonal direction operators and occupation responses. It does not test a
translation generator, physical calibration, stress tensor, metric equation,
or clock law.

### N6 — partial-closure paths

Live constructive paths include:

- add an explicit occupied-mode carrier tag and compile its coin/FSWAP law;
- add a distinguishable matter-rest or auxiliary species;
- build a two-mediator unit-weight source branch;
- enlarge the source sector to global Q2 and test simultaneous emissions;
- tile the pair program on adjacent edges and test overlap commutators;
- derive source preparation or a calibrated response observable.

Each can retire a supplied import without axiom language.

### N7 — hostile steelman

A hostile reviewer should reject any claim that the pair stream, 42 M2 per
cell, 111-M2 patch, or auxiliary species content is necessary. The pair stream
was selected because it gives a bounded full-Fock unit-weight response. A
tagged matter-carried code, a distinguishable species, paired mediators, or a
different schedule could use different support and response values.

The reviewer should also reject a claim that Cycle 320 failed. Its one-carrier
carrier port supplies information absent from an unmarked complete Fock mask.
Cycle 325 tests one extrapolation and then changes the auxiliary program
explicitly.

### N8 — cross-cycle echo

The recent sequence continues to replace the actual residual with explicit
content:

- Cycle 315 compiled the complete two-cell Fock seam and contact;
- Cycle 318 supplied coefficient-two recoil balance;
- Cycle 320 replaced coefficient two by a one-carrier matter-carried auxiliary;
- Cycle 322 placed coefficient-two sources at both full-Fock endpoints;
- Cycle 325 obtains full-Fock unit weights by supplying a mediator-paired
  auxiliary co-stream.

The new program closes one route while leaving matter tags, species, Q2, and
multi-edge recurrence open. The broad gate remains **FAIL / DO NOT SHIP**.

## Optimal next campaign

The sharpest discriminator is an explicit full-Fock carrier tag. Construct a
bounded tagged occupied-mode sector, define its coin and edge-FSWAP action,
and demand the same local ledgers, AB/BA EG, contact, response, frames,
translations, held sizes, support, deletions, and firewalls. That directly
tests whether the mediator-paired program can be replaced by faithful matter
carriage.

The orthogonal high-priority route remains global Q2 simultaneous emission.
Neither result would, by itself, provide energy, gravity, metric response, or
time.

## Verification

```text
python3 scripts/full_fock_unit_weight_two_source_cycle325_2026_07_18.py
```

Expected release result:

```text
RESULT FULL_FOCK_UNIT_WEIGHT_MEDIATOR_PAIRED_TWO_SOURCE_CERTIFIED
```
