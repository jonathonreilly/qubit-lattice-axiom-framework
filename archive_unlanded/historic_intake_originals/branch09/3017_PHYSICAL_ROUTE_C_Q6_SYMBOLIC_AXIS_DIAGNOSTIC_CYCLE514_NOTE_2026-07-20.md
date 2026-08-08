# Cycle 514 — Route-C Q6 exact symbolic all-axis diagnostic

Date: 2026-07-20

Authority: **none**

Audit: **unset**

Status: **conditional pre-collision diagnostic positive; Cycle-513 failing
subpredicate identified; generic update-3 growth and the physical compiler
remain open**

## Result up front

Cycle 514 identifies the exact cause of the Cycle-513 axis-1 compound-gate
failure at the resolution that was instrumented: Cycle 513 froze the axis-0
machine-exact matter-nonzero count for the update-3-pre-collision `II` factor
as `35,857`, whereas axis 1 has `35,815`.  Axis 2 has `35,756`.  The underlying
exact symbolic support is `30,207` on all three axes, and the support above the
declared `1e-14` diagnostic ceiling is also `30,207` on every axis.  The
axis-dependent excess coefficients have combined squared norm only
`1.054e-31`, `1.055e-31`, and `1.072e-31`.

Thus `sum(value != 0j)` was an invalid proper-cubic support fixture.  It was a
floating representation predicate, not an algebraic support invariant.  The
more specific micro-explanation—dictionary insertion or one particular
floating accumulation order—is consistent with the evidence but was not
instrumented and is not claimed.

Every separated prefix and geometry predicate passes on axes 0, 1, and 2.
All `27/27` exact matter and named-mediator factor rows pass.  All `216`
proper-cubic frame/factor comparisons pass with a predetermined exterior-CAR
sign census of `12` positive and `12` negative frames and no fitted phase.

This is a representation decision, not completed update 3.  The next growth
stage must use exact symbolic support for structural support and resource
proofs.  Numerical amplitudes remain the evolution and residual surface, but
machine-zero/nonzero counts cannot select support.  A sparse polynomial/DAG
extension is reserved for the first stage where multiple named monomials
collide or cross-branch cancellation becomes live.

## Frozen evidence

| artifact | SHA-256 |
|---|---|
| Cycle-514 runner | `74d9231d0c78ad6c85c028cea69cc7ac29c7b1b0c04259513d7223c5e8ae19fe` |
| clean dry transcript, `14/14` | `e09d664911f681a3a85f6cf180b744c4c63fb84362fe8232af6b64400903a83f` |
| authorized diagnostic transcript | `48c37e6ec11eb9cb7278e94f825ac5ab1f5569dc6f3c9b1fd247b1fe6c698847` |
| typed receipt | `5def6d3fb1e796341bb76cb51f6eb61a90274ef950a11a8007b7a3585f55c97d` |

The hash-bound invocation reused only the frozen Cycle-511 scout token and
scope.  It introduced no new token or scope.  The runner hash matched, the
single invocation is consumed, and no authorization value appears in the
transcript.

## Exact all-axis support result

For every axis, the matter factor counts are:

| factor class | labels | stored keys | exact support | raw third-coin contributions | support above `1e-14` |
|---|---|---:|---:|---:|---:|
| identity | `II` | 46,425 | 30,207 | 176,286 | 30,207 |
| one nonidentity | `ID, IX, DI, XI` | 1,800 | 1,620 | 3,456 | 1,620 |
| two nonidentity | `DD, DX, XD, XX` | 36 | 36 | 36 | 36 |

The full exact tag sequences are:

- `II`: stored `9,153,4911,4911,46425`; exact
  `9,81,2169,2169,30207`; raw coin contributions `306,5502,176286`;
- one nonidentity: stored `9,153,4911,96,1800`; exact
  `9,81,2169,90,1620`; raw `306,5502,3456`; and
- two nonidentity: stored `9,153,4911,1,36`; exact
  `9,81,2169,1,36`; raw `306,5502,36`.

These are exact in the inherited `Q(zeta_9)[z]` matter-tag representation,
with `z` the formal supplied contact phase.  Collision factors
`cos(theta)-1` and `i sin(theta)` are named nonzero premises.  The tag oracle
does not decide cancellation across the sum of structural branches.

The independent mediator history recurrence gives one named history and one
named monomial per final configuration:

| factor class | update-2 branch support | third-emitter pre-collision support |
|---|---:|---:|
| `II` | 729 | 4,096 |
| one nonidentity | 243 | 1,024 |
| two nonidentity | 81 | 256 |

The named basis is `C=cos(theta)`, `S=i sin(theta)`, and
`D=cos(theta)-1`.  No numerical amplitude is consulted by this support
oracle.  Nonzero `C,S,D` remains a supplied conditional, and no interval
certificate is claimed.

## The machine-support witness

| axis | `II` stored | exact | machine nonzero | above `1e-14` | machine excess over exact | below-ceiling norm squared |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 46,425 | 30,207 | 35,857 | 30,207 | 5,650 | `1.0539408857784601e-31` |
| 1 | 46,425 | 30,207 | 35,815 | 30,207 | 5,608 | `1.0552907227680999e-31` |
| 2 | 46,425 | 30,207 | 35,756 | 30,207 | 5,549 | `1.0722512480718073e-31` |

Each one-nonidentity factor has `1,800` machine-nonzero values but only
`1,620` exact and above-ceiling values; its `180` excess values have maximum
combined squared norm `8.768e-36`.  The two-nonidentity factors are clean at
`36/36/36`.

Cycle 513 required the entire axis-0 tuple

```text
("II", 46425, 35857, 4096, 4096, 14)
```

on every axis.  Cycle 514 shows that axis 1 reproduces every field except the
third, which is `35815`.  All separated geometry predicates also pass.
Therefore the Cycle-513 exception is now matched to the axis-0-frozen
machine-nonzero subpredicate, not merely inferred from control flow.

## Geometry and proper-cubic transport

Every axis has exactly `14` actually touched cells, no missing or unexpected
cell, zero omitted-shell nonidentity action, and no omitted witness.  The
per-label rows are

```text
C_j = (14, 12, 11, 12, 0, 0, 11, 0, 0)
P_j = (91, 11,  0, 11, 0, 0,  0, 0, 0)
```

for label order `II,ID,IX,DI,DD,DX,XI,XD,XX`.  The full `3,375`-cell law
remains defining; the fixed 18-cell shell is a compiler optimization whose
omitted actions are checked, not a state-dependent physical selector.

The proper-cubic audit covers `24` frames times nine factors:

| quantity | result |
|---|---:|
| frame/factor comparisons | 216 |
| packet orientation signs | 12 positive / 12 negative |
| exact matter-tag failures | 0 |
| maximum matter exterior-CAR residual | `2.323425094822377e-16` |
| maximum mediator hard-core residual | `1.738403497303146e-17` |
| declared ceiling | `1e-11` |
| fitted phase | false |

Axis reversal swaps the two active-site labels and supplies the predetermined
exterior-CAR sign.  This establishes covariance of the declared
pre-collision factor diagnostic, not covariance of a physical-site compiler.

## Resource and quarantine result

The invocation used `62.50 s` real time, `320,503,808` bytes maximum RSS, and
zero swaps.  It reached all three axis-complete checkpoints without a resource
wall.

Exactly one symbolic diagnostic invocation and `27` exact factor rows were
executed.  The following remained false or zero:

- generic update-3 collision growth and post-collision mediator stream;
- joint Schmidt core/rank, forward/reverse ordering, inverse, and orbit 72;
- depth five, response, deletion, train, and held evaluation;
- packed joint state and dense `X/Y` construction;
- science, response, held, occupation/bond, and state-hash rows;
- selector, refit, and physical compiler covariance.

The historical `461`, `581`, and `453` values remain nonminimal,
representation-specific diagnostics.  None is a physical count, general
resource bound, selector, or gate in Cycle 514.

## Supplied, derived, and open

Supplied:

1. the packaged Cycle-512 prefix and Cycle-513 local certificate/failure;
2. the Cycle-219 coin, Cycle-230 contact, Cycle-501 collision, emitter angle,
   open L15 geometry, Q6 preparation, and update order;
3. the contact phase and nonzero `C,S,D` scalar premises;
4. the bounded diagnostic resource limits and `1e-14` magnitude ceiling; and
5. the inherited single scout authorization and exact Cycle-514 hash.

Derived here:

1. exact all-axis per-factor matter support through the third free word;
2. exact named-mediator configuration support through the third emitter;
3. the axis-dependent machine-support witness and exact Cycle-513 failing
   subpredicate;
4. all-axis touched-set and omitted-shell witnesses; and
5. signed all-24-frame transport for all nine pre-collision factors.

Still open:

1. generic update-3 collision growth and any cross-branch cancellation;
2. final update-3 mediator stream, inverse/order/orbit, joint rank, and depth
   five;
3. held-size and arbitrary-volume scaling, leakage, deletion, and response;
4. the bounded physical-`M_2` parity/superselection compiler and the
   intertwining equation on its code space;
5. locally enforced auxiliary/gauge constraints without supplied global
   sector, marker, reference, or parity service;
6. autonomous preparation, interaction selection/protection, and rate;
7. derived causal/proper time, conserved energy/stress/source and gravity;
8. Born occurrence law, genuine Records, and realized-history selection; and
9. a parameter-fixed bridge into an existing prediction surface.

## Six-wall and TOE-lane effect

| wall | Cycle-514 movement | residual |
|---|---|---|
| `C_ref` | none | preparation and law selection remain supplied |
| `C_num` | positive diagnostic movement | machine-exact nonzero counts are rejected as support/covariance gates; probability meaning is untouched |
| `C_wrap` | none | update order is not time, rate, synchronization, or proper time |
| `C_int` | exact conditional pre-collision supports now pass all axes | no completed update 3, interaction selection, rate, or protection |
| `C_local` | the Cycle-513 prefix/geometry/frame suspicion is retired at this bounded surface | physical parity and arbitrary-volume `M_2` compiler remain open |
| `C_source` | none | resource counters are not energy, stress, source, or gravity |

No TOE maturity score changes.  The planning estimates remain:

| lane | integrated / strict / conditional | maturity |
|---|---:|---:|
| operational quantum / Records | `91 / 50 / 99` | `4.7 / 5` |
| causal time / clocks | `65 / 40 / 99` | `4.1 / 5` |
| matter / inertia | `81 / 43 / 99` | `4.5 / 5` |
| gravity / source / resource | `61 / 32 / 94` | `3.7 / 5` |
| Born / probability / realized history | `76 / 44 / 99` | `4.4 / 5` |

These are campaign planning estimates, not probabilities, retained claims, or
audit status.

## No-Go Discipline Gate — N1 through N8

Gate target: any claim that the Cycle-513 failure is a compiler failure,
shared substrate obstruction, minimum-content theorem, or source of axiom
pressure.

Gate result: **FAIL for every broad negative**.  No such claim ships.  The
licensed narrow statement is only that Cycle 513 failed an axis-0-frozen
machine-nonzero fixture for its `II` pre-collision factor.

### N1 — normalized alternative families

The following materially distinct families remain live under the proof-search
registry tuple of object, mechanism, and terminal obligation:

| family | object / mechanism | status and evidence |
|---|---|---|
| exact cyclotomic/contact tags | exact sparse `Q(zeta_9)[z]` coefficients / algebraic cancellation | **ATTEMPTED**; succeeds on all 27 Cycle-514 factor rows |
| retained sparse numerical evolution | complex amplitudes / norm and frame residuals without support pruning | **ATTEMPTED** through the bounded prefix; residuals pass, structural support is not delegated to floats |
| sparse polynomial or DAG | named `C,S,D,zeta_9,z` expressions / exact aggregation before evaluation | **PARTIAL ATTEMPT**; one monomial per current mediator configuration, reopened when collisions merge monomials |
| grouped D/X structural growth | local commuting factor groups / exact local-block structure | **UNTESTED LIVE ROUTE** after Cycle 513 |
| generic matrix-unit growth | 61-term local algebra / dynamic sparse aggregation | **PARTIAL ATTEMPT**; Cycle 513 completed only axis 0 by control-flow implication and retained no row |
| streamed or out-of-core growth | sparse rows / bounded memory aggregation | **UNTESTED LIVE ROUTE** |
| direct even-CAR block encoding | bounded local even algebra / code-space intertwiner | **PARTIAL CONSTRUCTIVE ROUTE**, physical compiler still open |
| local gauge/auxiliary encoding | Gauss constraints / local parity transport | **PARTIAL CONSTRUCTIVE ROUTE**, global sector/reference remains open |
| staggered/time-multiplexed encoding | bounded schedule / covariant phase classes | **PARTIAL CONSTRUCTIVE ROUTE**, autonomous clock/marker remains open |

Because substantially more than five normalized families remain live, a
compiler no-go is premature.

### N2 — wall independence

The raw open list is not advertised as independent.  Exact support semantics
repairs the Cycle-513 numerical fixture but does not complete growth.  Growth
within this Route-C simulator does not by itself supply a physical parity
compiler.  A physical compiler does not derive time, source/gravity, or Born
history.  Conversely those bridges do not repair this numerical
representation.  No inflated independent-wall count is claimed.

### N3 — hidden-condition scan

The bounded L15/Q6 domain, inherited preparation, selected coin/contact/
collision word, nonzero `C,S,D`, `1e-14` diagnostic ceiling, fixed shell, and
absence of a cross-branch cancellation oracle are explicit above.  “Exact”
refers to the declared tag algebra only.  “Proper-cubic” refers only to the
pre-collision factor surface.  There is no hidden appeal to standard QFT,
background time, a canonical compiler, or a registered law.

### N4 — residual matching

Cycle 513's cited residual is the axis-1 compound prefix/geometry exception.
Its actual frozen tuple includes the axis-0 machine-nonzero count `35,857`;
Cycle 514 observes `35,815` on axis 1 while every other tuple field and every
separated geometry predicate passes.  This is an exact residual match.
Cycle 512's update-2 residuals and Cycle 513's local certificate are used only
as positive cross-cycle controls; they are not witnesses for a compiler
failure.

### N5 — rhetoric and resolution

Tested: one declared Q6/L15 preparation, three axes, nine update-3-
pre-collision product factors, and 24 proper-cubic frames.  Not tested:
post-collision update 3, arbitrary states, arbitrary volumes, a physical
`M_2` code space, full lattice dynamics, time, source, gravity, Records, or
probability.  Therefore “Cycle 513 failed an axis-0-frozen machine-nonzero
fixture” is licensed; “the compiler failed” and “machine support is never
usable” are not.

### N6 — partial-closure paths

Cycle 512's all-axis update-2 result and Cycle 513's exhaustive local block
certificate remain intact.  Cycle 514 retires the instrumentation ambiguity
without changing an axiom or primitive.  Exact structural support plus
retained numerical amplitudes is the immediate import-retirement path.  A
polynomial/DAG representation remains available when branch aggregation
requires it.

### N7 — hostile steelman

A hostile reviewer can accept every Cycle-514 result and still reject a
physical compiler: later generic collision growth may create multiple
monomials per configuration, held-size support may grow without constant
overhead, a physical qubit encoding may still require a global parity sector
or marked reference, and no clock/source/Born bridge was run.  Direct,
auxiliary/gauge, and staggered constructions remain concrete unclosed
mechanisms.  This steelman is compelling, so no compiler no-go or compiler
closure follows.

### N8 — cross-cycle echo

Cycle 512 passed all-axis update 2; Cycle 513's complete local algebra is
proper-cubic; Cycle 514 now passes the separated exact and frame predicates.
The `matter-cone-larger-cell` no-go ledger remains empty.  Cycle 245's
marked-charge/gauge construction explicitly leaves boundary, auxiliary,
non-Clifford, and subsystem compilers live.  The nearest echoes therefore
support another constructive representation/compiler attempt, not axiom
pressure.

Broad no-go: **FAIL**.  Minimum-content claim: **FAIL**.  Shared substrate
obstruction: **FAIL**.  Axiom pressure: **FAIL**.

## Prior-art and novelty boundary

This cycle makes no literature-priority or novelty claim.  Exact sparse
support, local fermionic encodings, gauge auxiliaries, and proper-cubic
covariance each have broad prior art.  The retained contribution here is the
repo-specific executable diagnosis and exact dependency boundary for the
declared Cycle-219/230/501 construction.  Any external novelty claim requires
a separate current literature comparison and a completed physical compiler or
prediction-level theorem.

## Exact next contract

The next bounded growth runner must be newly hash-bound and separately
reviewed.  It must:

1. use exact symbolic support—not machine zeros or a magnitude cutoff—for
   structural support and work forecasts;
2. retain all numerical amplitudes needed for evolution and use thresholds
   only for declared residual/rank diagnostics;
3. compute descriptor, sparse-entry, and row-multiplicity work dynamically
   for each axis under conservative reviewed caps;
4. promote to sparse polynomial/DAG aggregation if more than one named
   monomial reaches a configuration or cross-branch sums become live;
5. preserve partial rows before every possible resource or predicate failure;
6. compare all three axes with predetermined CAR signs and report exact plus
   numerical residuals;
7. run generic update-3 collision growth before, and separately from, any
   post-collision mediator stream, inverse/order/orbit, joint rank, or held
   evaluation; and
8. keep the physical `M_2` compiler, causal time, source/gravity, Born law,
   Records, and prediction bridge explicitly open until their own defining
   obligations are executed.

Cycle 514 turns the Cycle-513 failure from an ambiguous compound exception
into an exact representation witness and selects the next constructive
growth representation.  It changes no axiom, primitive, audit status, or TOE
maturity score.
