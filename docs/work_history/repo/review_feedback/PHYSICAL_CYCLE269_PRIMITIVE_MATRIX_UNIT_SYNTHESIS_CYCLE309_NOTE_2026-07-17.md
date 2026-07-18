# Physical Cycle-269 primitive matrix-unit synthesis — Cycle 309

Date: 2026-07-17
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/physical_cycle269_primitive_matrix_unit_synthesis_cycle309_2026_07_17.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status.

## Result up front

Cycle 309 constructs three finite factorizations of the accepted Cycle-306
role-constrained comparator inside the repository's declared local
Pauli-transition, projector, and matrix-unit grammar.

The strongest results are two covariant spectral presentations on the
`C_role=+1` code. The staged presentation is:

```text
coin       8 nonidentity eigenspace-phase layers
stream     1 nonidentity eigenspace-phase layer
contact    1 nonidentity eigenspace-phase layer
total     10 nonidentity layers.
```

Every layer commutes with `C_role`, preserves the 42-column code, and is
covariant under all 24 proper-cubic frames. At `beta=-0.2,-0.3,-0.4` and held
`beta=-0.35`, the staged maximum separate or composed code-action residual is
`1.61e-14`. Layers for one operator commute and need no internal ordering, but
the outer coin-stream-contact order remains supplied.

The complete logical update

```text
G = contact @ stream @ coin
```

has 16 distinct nonidentity eigenspaces at all four beta values. Its 16
commuting layers reconstruct the fixed `G` directly with maximum code-action
residual `7.81e-14`. This presentation removes a runtime choice among the
three suboperators. The complete `G` coefficient block is supplied input, not
a newly selected or derived physical law, and applying the fixed update still
requires an external occurrence/application instruction.

This is a finite factorization inside the existing dense bounded local
grammar. It is not a decomposition into one- or two-M2 gates and not an
autonomous law. One staged spectral layer uses as many as 3,600 nonzero raw
matrix units; one complete-`G` layer uses as many as 14,400. The declared
180-sector ceiling is 32,400. Each raw term still uses a fourteen-bit local
tag/flag/`r` projector and a bounded Pauli transition.

The other exact results delimit what was gained:

1. **Direct conditional-Pauli QR.** The full 180-sector completed coin,
   stream, and contact factor exactly into 2,690 raw two-level/phase
   primitives. Every one of those ordered primitives fails to commute with
   `C_role`, and none is individually all-frame covariant. The final products
   commute and are covariant. This is a route-specific intermediate-layer
   failure.
2. **Local gauge-generator QR.** Factoring the 42-dimensional logical blocks
   and lifting each gate with `I+E_306(V-I)E_306^dagger` gives 379 primitives.
   Every primitive preserves `C_role` and the code, and the physical code
   residual is `2.65e-15`. Each primitive uses at most 400 raw matrix units.
   The reverse-lexicographic QR order is a host schedule, and none of these
   individual gates is all-frame covariant.
3. **Finite covariant spectral layers.** Degenerate eigenspace projectors
   repair the layerwise covariance loss and reduce the three target blocks to
   ten staged nonidentity layers, or factor the supplied complete `G` into 16
   unordered layers. Their dense local coefficients and application are still
   supplied compiler structure.

The role constraint itself has a separate exact factorization:

```text
C_role = K_exchange X_r
       = product of ninety commuting, coefficient-disjoint conditional swaps.
```

In short, the constraint has ninety commuting swaps.

The full unordered family is proper-cubic covariant, although no individual
swap is. Deleting one factor is invisible on the `C_role=+1` code because each
pair is symmetric there. It is detected with residual 2 on the corresponding
declared `C_role=-1` syndrome vector. That distinction is retained rather
than reporting a false code-action deletion.

All routes use the existing twenty-three M2 per cell, one forty-four-M2 patch,
and maximum Pauli-transition support 29. Training L=3 and held L=6 have zero
inherited port-constraint or fixed-sector failures. All 27 L=3 translations
and all 24 proper-cubic frames pass for the complete target products; every
spectral layer also passes all frames.

Cycle 309 narrows `W_prim`: it replaces one opaque 180-by-180 completion by
explicit finite matrix-unit factorizations and exact counts. It does not
retire the wall because dense local projectors, their coefficients, their
application, and the outer coin-stream-contact schedule remain supplied. A
finite circuit schedule is not physical time or an autonomous law.

Every positive factorization claim is exact on the Cycle-306 code.

## Declared local grammar

Let `|a>` denote one of the 180 local face/tag/flag/`r` representatives and
`Pi_a` its fourteen-bit projector. The inherited matrix unit is

```text
M_ab = W_a W_b^dagger Pi_b,
```

where the Pauli transition changes the face and every matching auxiliary bit
together. Cycle 309 uses only finite sums of these units and local diagonal
projectors.

For a two-level unitary `v` on representatives `a,b`, the direct primitive is

```text
T_ab(v)
  = I
  + (v_aa-1) M_aa + v_ab M_ab
  + v_ba M_ba + (v_bb-1) M_bb.
```

It contains at most four raw matrix units. A one-state phase contains one.
Complex QR elimination produces the coefficients rather than importing a
second physical coin. The runner reconstructs every target from the displayed
two-level and phase factors.

The local projectors distinguish all 180 patterns:

```text
12 occupation-matched port bits
 1 Cycle-304 slice flag
 1 Cycle-306 r bit.
```

They are local controls on physical M2 factors, not direction queries outside
the substrate.

## Route 1 — direct conditional-Pauli QR

QR acts on the complete 180-sector Cycle-306 physical matrices. At
`beta=-0.3` the exact counts are:

| block | two-level rotations | one-state phases | total |
|---|---:|---:|---:|
| coin | 312 | 8 | 320 |
| stream/catch-up | 2,250 | 90 | 2,340 |
| contact | 0 | 30 | 30 |
| total | 2,562 | 128 | 2,690 |

The maximum full-matrix reconstruction residual is `5.28e-15`. The final
coin, stream, and contact each commute with `C_role` exactly at coefficient
resolution.

The primitive census is different:

```text
C_role-noncommuting primitives          320 / 2340 / 30
individually all-frame primitives         0 /    0 /  0
maximum primitive constraint residual      3.998770931800777
maximum primitive frame residual           3.998770931800777.
```

Thus a raw lexicographic QR circuit is an exact off-code completion but is not
a lawful constraint-preserving primitive path. Paired or orbit-grouped direct
gates remain an open refinement; this route does not support a broader
primitive negative.

## Constraint factor — ninety swaps

`C_role` is a signless permutation of the 180 local representatives. It has no
fixed points and therefore partitions them into ninety disjoint pairs. For a
pair `(a,C_role a)`, let `S_a` be the direct conditional swap. Then:

```text
[S_a,S_b] = 0,
[S_a,C_role] = 0,
C_role = product_a S_a.
```

The executed product residual is zero. The ninety factors have disjoint
coefficient support, even though their physical Pauli/projector expressions
share M2 sites. Algebraic commutation, not spatial disjointness, makes the
order irrelevant.

No single swap is all-frame covariant. The complete unordered set is mapped
to itself, and the full product has zero frame residual. This is one
homogeneous local constraint grammar, not ninety selected direction laws.

On `E_306`, every factor is already `+1`, so removing one leaves the code
action unchanged. For the normalized local negative-syndrome vector

```text
(|a>-|C_role a>)/sqrt(2),
```

the same deletion changes the action with norm 2. This supplies the lawful
deletion witness for the constraint-enforcement surface.

## Route 2 — local gauge-generator QR

Let `F=E_306`. For a logical two-level gate `v`, define

```text
Gamma(v) = I_180 + F (v-I_42) F^dagger.
```

Because `C_role F=F`, every `Gamma(v)` commutes with the role constraint and
preserves `F F^dagger`. It is identity on the orthogonal complement. Expanding
`F(v-I)F^dagger` in raw local matrix units yields at most 400 nonzero terms per
primitive: each `n=1` logical column has ten raw branches, while each `n=2`
column has two.

The exact counts are:

| block | two-level rotations | one-state phases | total |
|---|---:|---:|---:|
| coin | 78 | 4 | 82 |
| stream/catch-up | 261 | 21 | 282 |
| contact | 0 | 15 | 15 |
| total | 339 | 40 | 379 |

The maximum logical reconstruction residual is `2.57e-15`; the completed
physical code-action residual is `2.65e-15`. Primitive unitarity residual is
below `7e-16`. Constraint and code leakage are zero to the printed precision.

This retires the direct route's intermediate constraint leakage. It does not
remove its supplied ordering: all 379 gates use a reverse-lexicographic QR
schedule, and zero individual gates commute with all 24 frames. The complete
products remain covariant.

## Route 3 — finite covariant spectral layers

For each logical target `U`, collect each complete degenerate eigenspace
projector `P_lambda`. Then

```text
U = product_lambda [I + (lambda-1) P_lambda].
```

Complete eigenspace projectors commute with the proper-cubic representation
because `U` does. Lifting each factor through `F` preserves `C_role` and the
code. Within one `U`, the factors commute.

At all four tested beta values:

| block | distinct eigenspaces including identity | nonidentity layers |
|---|---:|---:|
| coin | 9 | 8 |
| stream/catch-up | 2 | 1 |
| contact | 2 | 1 |

The supplied complete `G` has 16 distinct eigenspaces and all 16 eigenvalues
are nonidentity. Its unordered product therefore has 16 layers. This replaces
the supplied three-stage runtime order by one fixed local update block, at the
cost of a denser eigenspace expansion.

Spectral clustering uses the supplied numerical tolerance `2e-8`. Across all
coin, stream, contact, and complete-`G` operators at all four beta values, the
maximum within-group eigenvalue spread is `3.2270575502077454e-15`, while the
minimum inter-eigenspace gap is `6.693441584059668e-4`. These are respectively
`1.6135287751038728e-7` and `3.3467207920298344e4` times the tolerance. The
tolerance is explicit compiler-side numerical structure, not a physical
threshold or law.

The exact executable controls give:

```text
maximum projector idempotence residual       8.87e-16
maximum distinct-projector overlap            2.08e-14
maximum layer proper-cubic commutator          3.40e-14
maximum layer C_role commutator                0
maximum layer code leakage                     2.55e-15
maximum staged action residual                  1.61e-14
maximum complete-G action residual              7.81e-14
observed staged raw units in one layer          3,600
observed complete-G raw units in one layer     14,400
declared 180-sector raw ceiling               32,400.
```

This is the strongest Cycle-309 factorization. The eigenspace coefficients
are derived from the supplied Cycle-219 coin, declared wedge coin, stream,
and `g=0.37` contact. They are not an independently selected law. The staged
route retains the supplied coin-stream-contact order. The complete-`G` route
uses the supplied `G` coefficient block and no runtime suboperator branch,
but applying its unordered layer family is still supplied. Layer labels are
compiler resources, not clock readings.

## Locality, covariance, translations, and held size

Every raw transition used by all routes is a product of two accepted
Cycle-306 representatives. Training and held controls give:

| route | distinct raw matrix-unit pairs | transition union | maximum transition support |
|---|---:|---:|---:|
| direct QR | 176 | 43 M2 | 27 M2 |
| constraint swaps | 90 | 44 M2 | 22 M2 |
| gauge QR | 3,752 | 44 M2 | 27 M2 |
| spectral layers, including complete `G` | 17,520 | 44 M2 | 29 M2 |

The installed overhead stays 23 M2/cell. No new site is added. All 180
tag/flag/`r` projectors are distinct. Every basis representative commutes with
the inherited `B_v Z_port(v)` checks and fixed local/Wilson-sector rows at
both L=3 and held L=6, so every transition between them preserves those
constraints.

All complete target operators, `C_role`, and `E_306` commute with all 24
proper-cubic frames. The spectral layers do so individually. Translation
tests map every one of the ninety underlying face/tag/flag representatives
and the homogeneous `r` site through all 27 L=3 displacements with zero
failures. Held L=6 repeats 180 local projectors and 216 distinct homogeneous
`r` sites.

## Leakage, deletion, and lawful domain

The runner separately deletes:

- the strongest direct coin rotation: operator-norm residual
  `1.9993854659003876`;
- the strongest gauge coin rotation: code operator-norm residual
  `1.8477580786791181`;
- the largest nonidentity coin spectral layer: residual
  `1.9999987112800985`;
- one complete-`G` spectral layer: residual `1.9996735703840478`;
- one constraint swap on its negative-syndrome vector: residual `2`; and
- contact by setting `g=0`: residual `0.3678930670560824`.

Deleting one constraint swap has exactly zero residual on the positive code;
that is an expected stabilizer-sector identity, not a failed control.

Lawful-domain controls reject a nonsquare target, a nonunitary target, and the
aliased `L=2` geometry. QR/spectral factorization is not extended silently to
nonunitary channels or invalid cellulations.

## Supplied structure and autonomy boundary

Supplied are:

1. the accepted Cycle-306 42-column isometry, `C_role`, common-shell
   projector, fixed Wilson ray, and initial code state;
2. the Cycle-302/304 Pauli-transition, fourteen-bit projector, and local
   matrix-unit grammar;
3. Cycle-219 `C`, the declared `wedge^2 C`, Cycle-230 `g=0.37`, the
   coin-stream-contact outer order, and the complete fixed `G` coefficient
   block;
4. the spectral eigenspace clustering tolerance `2e-8`;
5. dense local QR or eigenspace coefficients and an instruction to apply the
   resulting finite gate list;
6. the macrocell origin and framing repair.

Derived are the QR rotations/phases, constraint-pair census, gauge lifts,
degenerate spectral projectors, exact counts, intertwiners, constraint and
frame commutators, translations, held size, support, leakage, deletion, and
lawful-domain controls.

Genuinely local structure consists of the homogeneous `C_role` relation, its
unordered swap grammar, and the bounded projector/matrix-unit support. The
spectral gates are local and covariant, but their application is scheduled.
No host direction or parity query appears; a host schedule remains.

The two-level QR and spectral decompositions are established
finite-dimensional linear algebra. The repository-specific result is the
exact factor and support census on this accepted gauge code. Global novelty is
not established. No result uses or compares with the Thirring engine.

## Six-wall ledger and maturity

| wall | Cycle-309 change | residual |
|---|---|---|
| `C_ref` | unchanged | fixed Wilson/reference ray, absolute preparation, and reference genesis supplied |
| `C_num` | unchanged; every primitive acts on the accepted 42-column `n=1+n=2` code | missing Fock sectors, overlapping patches, and rank-73 sea |
| `C_wrap` | unchanged; factor indices and outer order are not time | event equivalence, clock selection, recurrence, interval, and rate calibration |
| `C_int` | coin, stream, contact, staged composition, and complete fixed `G` now have exact finite code factorizations | actual recurrent separated-cell update and volume-wide intertwiner |
| `C_local` | `W_prim` narrowed: 90 constraint swaps, 379 gauge QR primitives, 10 staged spectral layers, or 16 complete-`G` layers with exact support/covariance controls | no one-/two-M2 gate decomposition; dense projector coefficients, application instruction, initial state, recurrence, and simultaneous patches supplied/open |
| `C_source` | unchanged | no energy, action, stress, source, resource, or gravity response selected |

No maturity score is raised. The Cycle-306 planning values remain:

| lane | integrated | strict floor | conditional | maturity |
|---|---:|---:|---:|---:|
| operational quantum / Records | 59% | 26% | 82% | 3.1/5 |
| causal time / clock | 33% | 17% | 60% | 1.7/5 |
| inertia / matter | 67% | 30% | 87% | 3.6/5 |
| gravity / source / resource | 38% | 15% | 63% | 1.9/5 |
| Born / probability / realized history | 33% | 14% | 82% | 1.8/5 |

The Born conditional ceiling and maturity correction comes from the separate
synced Born PR and is carried forward here. Cycle 309 contributes no Born-lane
evidence.

The bounded algebraic compiler becomes more explicit, but no occurrence,
autonomous recurrence, preparation, Record, source, or probability law is
added.

## No-go discipline gate

The proposed broad negative is: "the Cycle-306 completed blocks cannot be
factored into bounded local declared matrix-unit operations." The gauge and
spectral routes are counterexamples.

**Broad gate status: FAIL / DO NOT SHIP.** There is no shared obstruction and
no axiom pressure. Direct QR's intermediate leakage is route-specific.

### N1 — alternative-route enumeration

| route | status | disposition |
|---|---|---|
| raw 180-sector direct QR | **ATTEMPTED** | exact final products; every primitive leaves `C_role` and none is individually all-frame |
| ninety-swap constraint orbit | **ATTEMPTED** | exact unordered factorization of `C_role`; complete family covariant |
| 42-sector gauge QR lift | **ATTEMPTED** | exact code action and constraint preservation in 379 host-ordered primitives |
| degenerate spectral layers | **ATTEMPTED** | exact code action in ten staged or sixteen complete-`G` individually covariant dense layers |
| paired direct gates closed under the `C_role` orbit | **OPEN / UNTESTED** | could retain four-unit direct sparsity while canceling intermediate constraint leakage |
| one-/two-M2 universal gate decomposition | **OPEN / UNTESTED** | could refine each dense local projector into smaller physical gates |
| autonomous homogeneous update selecting its own layer application | **OPEN / UNTESTED** | would address the remaining host-application import |

Open routes and two positive factorizations reject the broad negative.

### N2 — wall-independence audit

After the finite matrix-unit factorization, the remaining walls are `W_gate`
(one-/two-M2 decomposition), `W_apply` (autonomous application rather than a
host schedule), `W_rec` (actual recurrent-volume closure), and `W_prep`
(absolute/coherent preparation). Their complete directional audit is:

| source | target | automatic? | separator |
|---|---|---:|---|
| `W_gate` | `W_apply` | no | a smaller gate alphabet still needs an application law |
| `W_apply` | `W_gate` | no | autonomy can select a dense bounded block without decomposing it |
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

The runner searches the Cycle-309 runner and note for the prohibited
hidden-premise phrase families. The literal hit count is zero. Dense local
coefficients, fourteen-bit projectors, initial code state, fixed reference,
outer order, QR order, and application instruction are explicit supplied
structure.

### N4 — residual matching

| exact witness | witness residual | Cycle-309 use | match? |
|---|---|---|---:|
| `PHYSICAL_CYCLE269_JOINT_SIX_MODE_COIN_LIFT_CYCLE302_NOTE_2026-07-17.md:46` | local matrix units require bounded Pauli representatives and local tag projectors | identical declared primitive grammar | yes |
| `PHYSICAL_CYCLE269_JOINT_SIX_MODE_COIN_LIFT_CYCLE302_NOTE_2026-07-17.md:53` | projector transport and exact matrix-unit algebra must be checked | inherited algebra used for every raw term | yes |
| `PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_CYCLE306_NOTE_2026-07-17.md:109` | `C_role=X_r K_exchange` defines the accepted constraint | exact operator factored into ninety swaps | yes |
| `PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_CYCLE306_NOTE_2026-07-17.md:141` | `C_role` was supplied as ninety orthogonal matrix units | same ninety-term surface receives an exact product factorization | yes |
| `PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_CYCLE306_NOTE_2026-07-17.md:147` | every constraint transition must preserve port/fixed-sector checks | rerun at L=3 and held L=6 for the enlarged primitive census | yes |
| `PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_CYCLE306_NOTE_2026-07-17.md:169` | total operators and role law require all-frame covariance | total products and every spectral layer tested under all 24 frames | yes |

Cycle 304's recurrent orbit leakage is not cited against primitive
factorization; it is a different residual.

### N5 — resolution audit

| statement | raw term | primitive/layer | complete local block | translated/held domain | outside scope |
|---|---:|---:|---:|---:|---|
| direct constraint leakage | each of 2,690 primitives tested | all fail `C_role` | final targets commute | final targets all-frame/translation covariant | paired/orbit direct grouping untested |
| gauge QR closure | up to 400 raw terms/primitive | all 379 preserve code/constraint | exact separate blocks | complete products covariant; L3/L6 support tested | individual layer covariance absent |
| spectral closure | observed up to 14,400 raw terms/layer | all ten staged and sixteen complete-`G` layers preserve code/constraint/frames | exact separate/staged/complete blocks | all frames, L3 translations, held L6 support | one-/two-M2 decomposition absent |
| constraint deletion | one swap removed | zero on positive code, 2 on matched negative syndrome | full ninety-factor product exact | local at L3/L6 | dynamical preparation of syndrome sectors untested |

### N6 — constructive partial closure

The gauge QR and spectral routes are the partial-closure paths. They turn the
supplied dense completion into explicit finite local matrix-unit lists with
exact counts, covariance, support, and deletion controls. The dense-projector
and host-application imports remain named. No convention or axiom change is
needed.

### N7 — hostile steelman

Reject any primitive no-go. The direct QR failure only shows that a basis-
ordered raw gate list ignores the gauge orbit. Lifting through `E_306`
centralizes the constraint immediately, and grouping complete degenerate
eigenspaces restores layerwise proper-cubic covariance in ten staged factors
or sixteen factors for the supplied complete update.
Paired direct gates, smaller universal gate alphabets, and autonomous local
application remain open, so the evidence supports a constructive narrowing
only.

### N8 — cross-cycle echo

Cycle 302 supplied an opaque dense 30-sector matrix-unit coin and nevertheless
proved exact bounded physical action. Cycle 306 then retired a free role flag
by enlarging the local gauge grammar. Cycle 309 repeats that successful move:
it expands the factor grammar to gauge and spectral projectors and retires the
opaque-single-block presentation without claiming an autonomous update. A
larger local grammar has twice removed a predecessor residual, so no broad
negative or axiom pressure follows.

Gate disposition: **FAIL / DO NOT SHIP for the broad negative.** The direct
QR intermediate-layer failure remains a route-specific diagnostic.

## Optimal next probe

The highest-value primitive follow-on is the open paired-direct route:

1. factor each 90-sector Cycle-304 block rather than the completed 180-sector
   block;
2. pair every raw two-level gate with its `C_role` conjugate on the other `r`
   branch so each paired layer centralizes the constraint;
3. group the paired layers into complete proper-cubic orbits and test whether
   overlapping orbit members commute or require coloring;
4. compare the resulting raw matrix-unit count and maximum support with the
   379-gauge and ten-spectral routes; and
5. keep any coloring/application order explicit rather than calling it time
   or autonomy.
