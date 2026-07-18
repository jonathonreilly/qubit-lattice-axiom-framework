# Physical Cycle-269 paired-direct orbit factorization — Cycle 310

Date: 2026-07-17
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/physical_cycle269_paired_direct_orbit_factorization_cycle310_2026_07_17.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status.

## Result up front

Cycle 310 gives an exact sparse paired-direct factorization of the accepted
Cycle-306 fixed-seam comparator. It starts from each ninety-sector Cycle-304
block, factors that block, and pairs every factor with its `C_role` conjugate
on the other physical `r` branch.

The exact census is:

| block | ninety-sector factor | paired layers | raw branch factors | maximum raw matrix units per paired layer |
|---|---|---:|---:|---:|
| coin | sparse QR | 160 | 320 | 8 |
| stream/catch-up | disjoint signed swaps | 45 | 90 | 8 |
| contact | one-state phases | 15 | 30 | 2 |
| total |  | 220 | 440 | 8 |

In words, this is two hundred twenty paired layers. Every paired layer
commutes with `C_role` exactly and uses at most eight raw matrix units. The
complete products have exact final code action: they reconstruct coin,
stream, contact, and the supplied outer composition with maximum full-matrix
residual `5.90e-15`, maximum code-action residual `3.85e-15`, and maximum
complete-product frame residual `9.00e-15`. The counts and constraint result
repeat at beta `-0.2,-0.3,-0.4` and held beta=-0.35.

This is a much sparser point on the Cycle-309 compiler tradeoff:

| route | layers | maximum raw matrix units/layer | every intermediate preserves code? | every intermediate all-frame? |
|---|---:|---:|---:|---:|
| paired-direct Cycle 310 | 220 | 8 | no | no |
| gauge QR Cycle 309 | 379 | 400 | yes | no |
| staged spectral Cycle 309 | 10 | 3,600 | yes | yes |
| complete-`G` spectral Cycle 309 | 16 | 14,400 | yes | yes |

The sparsity gain has two measured costs. First, one hundred nineteen
intermediate layers leak from the common shell: 89 coin factors and 30
stream factors. The maximum intermediate leakage is `0.9797508507304228`.
The final product returns exactly to the code. Contact's 15 phase factors
preserve it individually.

Second, zero of the 220 paired layers is individually covariant under all 24
proper-cubic frames. Closing the coefficient-bearing coin factors under the
frame group gives one hundred fifty-nine coin orbit types under the unrounded
floating-coefficient census after retaining each term whose absolute
coefficient exceeds `1e-12`. Forty-six have commuting members; one hundred
thirteen have noncommuting members. Their overlap and noncommutation graphs
each admit a verified deterministic eight-color upper bound. Coloring
minimality is not claimed.

The minimum coefficient-multiset completion of the scheduled coin factors has
3,609 paired layers, requiring three thousand four hundred forty-nine added
layers. Appending those missing orbit members in the declared deterministic
order changes the target with operator residual `1.9990260188134212` and still
has frame residual `1.9999966433411136`. This falsifies that specific orbit-
append schedule. It is not evidence that every symmetry-adapted sparse
factorization fails.

Stream and contact behave differently. Their four and two orbit types are
already coefficient-complete, pairwise support-disjoint within each orbit,
commuting, and exactly covariant as unordered orbit products. No completion
factor is added and both target and frame residuals are zero.

All scheduled and orbit-closed raw terms stay inside the same forty-four-M2
patch with twenty-three M2 per cell. Training L=3 and held L=6 have zero
inherited port-constraint or fixed-sector failures. All 27 L=3 translations
pass. The one-particle mass fixture and Cycle-230 contact seam are unchanged.

The strongest Cycle-310 result is therefore an exact, bounded, sparse,
constraint-preserving final compiler with an explicit sparsity-versus-
intermediate-code/covariance tradeoff. It is not a code-preserving path at
every layer, not an individually covariant layer list, not a one-/two-M2 gate
decomposition, and not an autonomous law. The host schedule and application
remain supplied.

## Paired-direct algebra

Let `K=K_exchange` on the ninety Cycle-304 microsectors and let a sparse
ninety-sector factor be `A=I+Delta`. Define its physical pairing by

```text
Pair(A) = A |0><0|_r + K A K |1><1|_r
        = block_diag(A,KAK).
```

The accepted role constraint is

```text
C_role = X_r tensor K.
```

Direct block multiplication gives

```text
[Pair(A),C_role] = 0,
Pair(A) Pair(B) = Pair(AB).
```

Thus the paired factor list reconstructs the Cycle-306 completion whenever
the ninety-sector factors reconstruct the Cycle-304 block. No host query of
`r`, direction, or parity occurs. Both terms are local matrix-unit operations
controlled by the physical fourteen-bit tag/flag/`r` projectors.

A two-level ninety-sector factor uses at most four raw matrix units. Pairing
it uses at most eight. A one-state phase uses two after pairing. The two
branch factors have coefficient-disjoint support and commute, so they form
one paired layer without an internal order.

## Block factorizations

### Coin

The physical ninety-sector coin is the Cycle-304 shell coin on the onsite
`n=1` slice, the declared `wedge^2 C` on onsite `n=2`, and identity on the
separated slices. Complex QR gives 156 two-level factors and four one-state
phases. Their ordered product has residual at most `5.90e-15` over all four
beta values.

The QR pivot order is supplied compiler structure. Pairing repairs the
Cycle-309 direct route's `C_role` leakage, but 89 of the 160 paired coin layers
leave the common shell. None is individually all-frame. The final coin
preserves the code and is all-frame.

### Stream/catch-up

Generic QR is unnecessary for the ninety-sector stream. It is a fixed-point-
free signed involution: 30 negative `n=1` exchanges and 15 positive `n=2`
exchanges. These are 45 disjoint two-level factors. Their paired lifts commute
with each other and reconstruct the completed stream exactly.

The factors split into four complete frame orbits of sizes `6,24,3,12`.
Every orbit is support-disjoint and commuting. Thirty individual `n=1`
factors leave the common shell because one exchanged reference branch does
not preserve the five-ray logical superposition. The complete `n=1` family
restores it. The fifteen one-hot `n=2` factors preserve the code individually.

### Contact

The ninety-sector contact has 15 onsite `n=2` phases and identity elsewhere.
Their paired lifts are 15 commuting two-state phase layers. They form complete
proper-cubic orbits of sizes `3` and `12`, preserve the common shell one by
one, and reconstruct contact exactly.

## Proper-cubic orbit closure and coloring

For a paired factor `L` the runner forms the coefficient-bearing set

```text
Orbit(L) = {R L R^dagger : R in the 24 proper-cubic frames}.
```

Every computed orbit set is closed under every frame. Coefficients are part of
the key; support equality alone is not counted as closure. The executable key
uses unrounded binary floating values after the declared `abs(value)>1e-12`
sparsity cutoff. Thus 165 is an unrounded floating-coefficient census, not an
algebraically exact orbit-count theorem.

The executed census at beta `-0.3` is:

| block | orbit types | orbit-size distribution | commuting types | noncommuting types | minimum coefficient-complete layer count | additions |
|---|---:|---|---:|---:|---:|---:|
| coin | 159 | `143x24, 14x12, 1x6, 1x3` | 46 | 113 | 3,609 | 3,449 |
| stream/catch-up | 4 | `1x24, 1x12, 1x6, 1x3` | 4 | 0 | 45 | 0 |
| contact | 2 | `1x12, 1x3` | 2 | 0 | 15 | 0 |

For each orbit the runner builds two graphs:

- a support-overlap graph, joining factors that touch a common 180-sector
  representative;
- a noncommutation graph, joining factors whose sparse commutator is nonzero.

A deterministic DSATUR pass supplies verified colorings for both graphs. The
maximum edge count in one coin orbit is 96 for each graph, and the maximum
verified color count is eight. Same-color factors are checked to be disjoint
or commuting according to the relevant graph. The eight-color result is an
upper bound and schedule certificate, not a chromatic-number theorem.

Color labels and their application order are supplied compiler resources.
A frame-invariant multiset does not imply a frame-invariant ordered product
when members do not commute. The explicit coin append-completion residuals
show that coefficient closure alone neither preserves the target nor repairs
the ordering problem. A symmetry-adapted factorization could still choose
different factors and remains open.

## Intermediate leakage and exact final action

The accepted code projector is `P_306=E_306 E_306^dagger`. For every paired
layer `L`, the runner evaluates

```text
||(I-P_306) L E_306||_2.
```

At every tested beta the census is:

| block | leaking layers | maximum leakage |
|---|---:|---:|
| coin | 89 / 160 | at most `0.9797508507304228` |
| stream/catch-up | 30 / 45 | `0.8` |
| contact | 0 / 15 | below `9e-17` |
| total | 119 / 220 | at most `0.9797508507304228` |

This leakage is from the Cycle-304 common shell, not from `C_role`: every
layer has zero `C_role` commutator. The gauge QR and spectral Cycle-309 routes
already show that common-shell-preserving paths exist, so this is a route-
specific sparsity tradeoff rather than a shared substrate obstruction.

The final products give:

```text
maximum separate/composed full-matrix residual      5.90e-15
maximum separate/composed code-action residual      3.85e-15
maximum final proper-cubic frame residual            9.00e-15
maximum paired-layer C_role commutator                0
maximum paired-layer unitarity residual               1.34e-15.
```

The fixed update still uses the supplied coin-stream-contact order. The
factor index is not a clock reading, and factor application is not physical
time or an autonomous law.

## Locality, translations, held controls, and fixtures

The scheduled 220 layers use 532 distinct raw matrix-unit coefficient pairs.
The union of all 165 orbit types uses 1,200. Both occupy 43 transition M2 in
the accepted forty-four-M2 face/port/flag/`r` patch:

| surface | distinct raw matrix units | transition union | maximum transition support |
|---|---:|---:|---:|
| scheduled factors | 532 | 43 M2 | 27 M2 |
| all orbit-closed support | 1,200 | 43 M2 | 29 M2 |

Every raw term uses a fourteen-bit local projector. The installed overhead is
twenty-three M2 per cell. The unused forty-fourth transition site is still a
local projector/control resource in the accepted patch; no support outside
that patch is introduced.

Training L=3 and held L=6 each contain 180 distinct tag/flag/`r` projectors,
zero inherited port-constraint failures, and zero fixed local/Wilson-sector
failures. Held L=6 has 216 homogeneous `r` sites. All ninety representatives
under all 27 L=3 translations give zero phase, tag, or placement failures.

The one-particle mass test returns `0.453405654174885` against the Cycle-219
fixture `0.4534056541748851`. Contact differs from `g=0` by exactly zero on
the one-particle columns. The contact-stream order residual is
`0.36789306705608243`, retaining the Cycle-230 seam block and the supplied
outer order.

## Deletion and lawful domain

Deleting a complete paired layer is detected with operator residuals:

```text
coin       1.9999987112800985
stream     2
contact    0.3678930670560824.
```

Deleting only the conjugate `r=1` partner of the strongest coin factor breaks
`C_role` with operator residual `1.9999987112800988`. Deleting one member of a
complete stream orbit changes the target by `2` and breaks frame covariance
by `2`.

Lawful-domain controls reject a nonsquare QR target, a nonunitary QR target,
a fixed-point stream passed to the disjoint-swap compiler, a nondiagonal
contact passed to the phase compiler, and the aliased L=2 geometry.

## Supplied structure and novelty boundary

Supplied are:

1. Cycle-219 `C`, the declared `wedge^2 C`, Cycle-230 `g=0.37`, and the
   Cycle-304 ninety-sector completed blocks;
2. the Cycle-302/304 Pauli-transition, fourteen-bit projector, and local
   matrix-unit grammar;
3. Cycle-306 `K_exchange`, `r` placement, `C_role`, common-shell projector,
   and constrained encoding;
4. QR elimination tolerance, the `abs(value)>1e-12` orbit sparsity cutoff,
   residual thresholds, and the QR pivot order;
5. the outer coin-stream-contact order, occurrence/application of the finite
   factor list, and any chosen orbit-color order;
6. the initial code state, fixed Wilson ray, common-shell preparation, and
   macrocell framing.

Derived are the 160/45/15 sparse factors, conjugate pairing, executed factor
and support counts, constraint commutators, code leakage census, frame orbits,
overlap/noncommutation graphs, verified DSATUR colorings, translations, held
size, mass/contact fixtures, and deletion controls.

The algebraic QR method, conjugate block pairing, group orbits, and graph
coloring are established finite mathematics. The repository-specific result
is the exact 220-layer sparse census and its measured tradeoff on the accepted
Cycle-306 code. Global novelty is not established. No result uses or compares
with the Thirring engine.

No global parity service, Jordan-Wigner ordering, direction query, or host
`r`-branch control appears. QR/color ordering and factor application remain
host schedule inputs.

## Six-wall ledger and maturity

| wall | Cycle-310 change | residual |
|---|---|---|
| `C_ref` | unchanged | fixed Wilson/reference ray, absolute preparation, and reference genesis supplied |
| `C_num` | unchanged; final action is exact on the accepted 42-column `n=1+n=2` code | missing Fock sectors, overlapping patches, and rank-73 sea |
| `C_wrap` | unchanged; factor and color indices are not time | event equivalence, clock selection, recurrence, interval, and rate calibration |
| `C_int` | 220 sparse paired layers exactly reproduce coin, stream, contact, and the fixed outer composition | actual recurrent separated-cell update and volume-wide intertwiner |
| `C_local` | `W_prim` narrows from dense layers to at most eight raw units per paired layer | 119 route-specific common-shell-leaking layers; coin orbit completion does not preserve the target; one-/two-M2 decomposition, application, recurrence, and simultaneous patches remain supplied/open |
| `C_source` | unchanged | no energy, action, stress, source, resource, or gravity response selected |

No maturity score is raised. The current planning values remain:

| lane | integrated | strict floor | conditional | maturity |
|---|---:|---:|---:|---:|
| operational quantum / Records | 59% | 26% | 82% | 3.1/5 |
| causal time / clock | 33% | 17% | 60% | 1.7/5 |
| inertia / matter | 67% | 30% | 87% | 3.6/5 |
| gravity / source / resource | 38% | 15% | 63% | 1.9/5 |
| Born / probability / realized history | 33% | 14% | 82% | 1.8/5 |

The Born ceiling and maturity values come from the separate synced Born PR.
Cycle 310 adds no Born-lane evidence.

## No-go discipline gate

The proposed broad negative is: "the accepted bounded grammar has no sparse
`C_role`-preserving exact factorization of the fixed comparator." The paired-
direct route is a counterexample.

**Broad gate status: FAIL / DO NOT SHIP.** There is no shared obstruction and
no axiom pressure. Intermediate common-shell leakage and coin orbit failure
belong to this sparse route.

### N1 — alternative-route enumeration

| route | status | disposition |
|---|---|---|
| full 180-sector direct QR | **ATTEMPTED** | Cycle 309 gives exact final action but every primitive violates `C_role` |
| ninety-sector conjugate-paired QR | **ATTEMPTED** | Cycle 310 gives exact final action in 220 sparse `C_role`-preserving layers |
| disjoint stream/contact orbit factors | **ATTEMPTED** | 45 swaps and 15 phases form complete commuting proper-cubic orbit families |
| 42-sector gauge QR | **ATTEMPTED** | Cycle 309 gives 379 code/constraint-preserving layers with denser raw expansions |
| degenerate spectral factorization | **ATTEMPTED** | Cycle 309 gives ten staged or sixteen complete-update code/frame-preserving layers |
| symmetry-adapted sparse coin factorization | **OPEN / UNTESTED** | could preserve exact target action while selecting complete commuting orbit generators |
| one-/two-M2 gate decomposition | **OPEN / UNTESTED** | could refine each projector-controlled matrix unit into a smaller gate alphabet |
| autonomous homogeneous layer application | **OPEN / UNTESTED** | could replace the supplied factor occurrence and outer schedule |

Five attempted routes, three constructive exact routes, and three open routes
reject the broad negative.

### N2 — wall-independence audit

The surviving shared walls remain `W_gate` (one-/two-M2 decomposition),
`W_apply` (autonomous application), `W_rec` (actual recurrent-volume closure),
and `W_prep` (absolute/coherent preparation). Intermediate shell leakage and
coin orbit noncommutation are not added as shared walls because the Cycle-309
gauge and spectral routes already avoid them.

| source | target | automatic? | separator |
|---|---|---:|---|
| `W_gate` | `W_apply` | no | a smaller gate alphabet still needs an application law |
| `W_apply` | `W_gate` | no | autonomy can apply a dense bounded block without decomposing it |
| `W_gate` | `W_rec` | no | local gate synthesis does not close the separated-cell orbit |
| `W_rec` | `W_gate` | no | recurrent closure can remain a dense local matrix |
| `W_gate` | `W_prep` | no | gate decomposition does not prepare the fixed reference/input |
| `W_prep` | `W_gate` | no | a prepared code does not decompose its update |
| `W_apply` | `W_rec` | no | applying the fixed comparator does not make it recurrent |
| `W_rec` | `W_apply` | no | a recurrent matrix can still need an external trigger |
| `W_apply` | `W_prep` | no | autonomous application does not create the lawful initial code |
| `W_prep` | `W_apply` | no | preparation does not select future updates |
| `W_rec` | `W_prep` | no | orbit closure does not prepare arbitrary inputs |
| `W_prep` | `W_rec` | no | preparation does not close independent separated-cell coins |

### N3 — hidden-wall scan

The runner searches itself and this note for the prohibited hidden-premise
phrase families. The literal hit count is zero. QR pivot order, numerical
tolerances, coefficient matching, color order, outer order, initial state,
fixed reference, common shell, macrocell frame, and application instruction
are explicit supplied structure.

### N4 — residual matching

| exact witness | witness residual | Cycle-310 use | match? |
|---|---|---|---:|
| `PHYSICAL_CYCLE269_COIN_STREAM_CONTACT_COMMON_REFINEMENT_CYCLE304_NOTE_2026-07-17.md:58` | fixed comparator requires an exact physical intertwiner | exact final paired product is tested against the same intertwiner | yes |
| `PHYSICAL_CYCLE269_COIN_STREAM_CONTACT_COMMON_REFINEMENT_CYCLE304_NOTE_2026-07-17.md:84` | physical terms use joint local face/tag/flag matrix units | every sparse paired term uses that same grammar plus physical `r` | yes |
| `PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_CYCLE306_NOTE_2026-07-17.md:109` | `C_role=X_r tensor K_exchange` is the accepted local constraint | every paired layer is tested against that operator | yes |
| `PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_CYCLE306_NOTE_2026-07-17.md:131` | the Cycle-306 lift is multiplicative | paired factor products are tested against the same multiplicative lift | yes |
| `PHYSICAL_CYCLE269_PRIMITIVE_MATRIX_UNIT_SYNTHESIS_CYCLE309_NOTE_2026-07-17.md:68` | gauge QR preserves code and constraint in 379 layers | used only as the code-preserving density comparator | yes |
| `PHYSICAL_CYCLE269_PRIMITIVE_MATRIX_UNIT_SYNTHESIS_CYCLE309_NOTE_2026-07-17.md:74` | spectral layers repair layerwise covariance | used only as the covariant density comparator | yes |

Cycle 304's recurrent-volume leakage is not used against paired primitive
synthesis; the residuals differ.

### N5 — resolution audit

| resolution | tested result | untested broader claim | disposition |
|---|---|---|---|
| raw branch factor | at most four matrix units | one-/two-M2 gate realization | open; do not broaden |
| paired layer | at most eight units and exact `C_role` commutation | common-shell or all-frame preservation for every layer | false for this route |
| complete block | exact code action and all-frame covariance | recurrent separated-cell action | outside this comparator |
| orbit family | all sets frame-closed; 113 coin types noncommute | every symmetry-adapted sparse orbit factorization fails | untested; reject |
| translated/held patch | L3 translations and L6 support pass | simultaneous overlapping-volume compiler | untested |

The negative statement is restricted to the explicit coefficient-completion
and append ordering tested here.

### N6 — constructive partial closure

Gauge QR and spectral factors remain the constructive partial-closure paths
for the paired route's intermediate shell and frame residuals. The paired
route separately closes sparse exact final action and `C_role` preservation.
A symmetry-adapted factor basis is another open compiler refinement. None of
these paths requires an axiom or convention change.

### N7 — hostile steelman

Reject any sparse-primitive no-go. The raw QR orbit append is a poor symmetry
strategy: it first selects a basis order and only afterward duplicates its
factors across frames. The accepted coin lies in the proper-cubic commutant,
and Cycle 309 already factors that same operator into complete covariant
eigenspaces. A symmetry-adapted direct algorithm could work inside the cubic
isotypic blocks, factor multiplicity spaces, and expand each resulting factor
into sparse paired orbit sums. The present 3,449-factor completion penalty
therefore diagnoses this QR basis, not the local substrate.

### N8 — cross-cycle echo

Cycle 304 obtained exact bounded action while leaving a free role flag. Cycle
306 enlarged the local gauge grammar and retired that flag. Cycle 309 showed
that direct QR's constraint failure disappears under gauge pairing and that
spectral grouping repairs layerwise covariance. Cycle 310 now pairs the
ninety-sector factors directly and retires `C_role` leakage with far sparser
layers, while its cubic orbit append still fails. Three successive repairs
came from changing factor grammar rather than adding an axiom, so no broad
negative or axiom pressure follows.

Gate disposition: **FAIL / DO NOT SHIP for the broad negative.** The explicit
coin orbit-append schedule is a route-specific negative; the 220-layer paired
factorization is constructive.

## Optimal next probe

The highest-value next step is a symmetry-adapted sparse coin factorization:

1. decompose the ninety-sector coin shell into proper-cubic isotypic blocks;
2. factor only the multiplicity-space unitaries, keeping each irrep identity
   explicit;
3. pair each factor through `A -> block_diag(A,KAK)` before raw expansion;
4. expand each factor into complete cubic matrix-unit orbits and test whether
   each factor preserves the common shell;
5. require exact target/code action, individual all-frame covariance, bounded
   support, held beta/size, deletion, and lawful-domain controls; and
6. compare raw terms and layer count against the 220 paired, 379 gauge, and
   10/16 spectral points without treating factor order as time.
