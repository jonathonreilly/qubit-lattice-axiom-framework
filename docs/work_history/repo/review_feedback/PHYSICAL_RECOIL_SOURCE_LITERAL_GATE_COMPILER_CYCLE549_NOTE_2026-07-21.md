# Physical recoil/source literal gate compiler — Cycle 549

Date: 2026-07-21

Authority: none

Audit: unset

Constitutional effect: none

Companion runner:

`scripts/physical_recoil_source_literal_gate_compiler_cycle549_2026_07_21.py`

## Result

Cycle 549 compiles the Cycle-426 coefficient-two recoil/source exponential on
the complete local Q<=2 code into literal nearest-neighbor one-/two-M2 gates.
It then replaces Cycle 429's old dense matter source lift and direction
readout, on the Cycle-539 selected three-cell path code, by

```text
W_path SOURCE_q W_path^dagger
```

with direction read directly from the persistent physical q M2.  `W_path` is
Cycle 539's strict-pinned explicit compute/select/uncompute isometry and its
literal nearest-neighbor macro router.  The source compiler is new here.

For local resource number `Q=0`, the source is identity.  For `Q=1` and `Q=2`,
the runner builds the actual Cycle-426 sparse generator, finds every connected
component, exponentiates each component at the frozen angle, and performs an
explicit complex Givens elimination.  The resulting physical-application list
contains only basis-state phases and two-level rotations.  Each two-level
factor is compiled by a 13-bit Gray path into equality-controlled X gates and
one equality-controlled one-M2 core.  Every equality macro has the exact
Cycle-523 15-call Toffoli decomposition, and every resulting two-M2 pair is
routed on an explicit bounded integer microgrid by ordinary adjacent SWAP,
the core, and reverse SWAP.

The source coefficient, `theta=0.8m`, angle sign, normalization, invocation,
and complex compiler angles remain supplied.  The current-correlated input
preparation remains supplied.  The Cycle-539 selected and Cycle-540 rough
carriers remain distinct; no transducer is inferred.

On the Q1 receiver sector, the compiled physical circuit reproduces the exact
Cycle-322/Cycle-426 vertex and all three Cycle-429 embedded source operators.
The current-selected NULL/PLUS/MINUS apparatus therefore retains the Cycle-434
frozen values without refit, current=0 null, the odd receiver coordinate,
source/receiver resource and direction ledgers, inverse, deletions, train L5,
held L6, all 24 frames, and all 576 frame products.

The Python dictionaries used for current sectors and sparse resource states
are sparse direct-sum bookkeeping only.  The physical current circuit remains
Cycle 546's exhaustive fixed tensor-product Fredkin circuit on literal
`EDGE_PASSED/J_plus/J_minus` M2.

This is a bounded positive compiler result.  It does not identify direction
as force, momentum, energy, stress, or gravity; coherent weights are not Born
probabilities; compiler order is not time; and there is no axiom pressure.

## Exact target contract

| field | contract |
|---|---|
| Target | Replace the Cycle-426 bounded source exponential and Cycle-429 dense source lift/readout by literal NN one-/two-M2 gates on Cycle 546's current-selected interface. |
| Domain | One six-mode matter cell plus seven resource M2 for local Q=0,1,2; Cycle-539 three-cell path matter code with total matter `n<=3`; Cycle-546 Q1 receiver histories at L5 and held L6. |
| Allowed | Strict-pinned Cycles 426, 396, 429, 523, 539, 540, and 546; supplied coefficient/angle/sign; finite truth tables and exact complex compiler angles; blank work and route M2. |
| Forbidden | No 13-M2 source exponential called primitive, dense `E_429 U E_429^dagger` source lift, non-NN two-M2 call, host current branch, parameter refit, carrier conflation, or physics interpretation of direction/schedule/weight. |
| Required controls | Complete Q<=2 factorization, inverse, work return, factor deletion, local lift, current tensor preservation, NULL, frozen response/odd ledgers, causal deletions, mass/contact/seams, held size, all24/576 covariance, and explicit supplies. |
| Completion witness | Exact finite factor list plus Gray/Toffoli/NN compilation and `W_path SOURCE_q W_path^dagger` code intertwiner. |
| Not closure | Q>2 source sectors, autonomous current-correlated preparation, route-resource economy, selected-to-rough transducer, Cycle-420 host join, energy/stress source selection, gravity, time, Record, or Born law. |

## Local source algebra

On one local six-mode CAR cell and one physical reservoir/field star, Cycle
426 supplies

```text
H_rec = sum_d [
    a^dagger_bar(d) a_d sigma_R^- sigma_d^+
  + a_d^dagger a_bar(d) sigma_R^+ sigma_d^-
],

V_rec(theta) = exp(+i theta H_rec),
theta = 0.8 m = 0.3627245233399082.
```

The local physical register is 13 M2: six matter-occupation M2, one reservoir
M2, and six directional field M2.  Cycle 549 uses Cycle 426's exact raw M2 bit
ordering, not an abstract seven-label source.

The connected-component census is load bearing.  Q1 has 448 states and Q2
has 1,344 states.  The generator decomposes into small components rather than
one dense block:

| sector | component sizes |
|---|---|
| Q1 | 296 size-1, 24 size-2, 24 size-3, 8 size-4 |
| Q2 | 600 size-1, 168 size-2, 72 size-3, 24 size-5, 8 size-9 |

Every size-1 component is identity.  Each other component is exponentiated
independently and reduced to two-level rotations and diagonal phases by
complex Givens elimination.  This is an exact bounded direct-sum theorem, not
a numerical fit and not a claim that the direction terms commute.

## Literal gate compiler

### Two-level and phase factors

For each component unitary `U`, left Givens elimination produces

```text
D = G_N ... G_1 U,
U = G_1^dagger ... G_N^dagger D.
```

The physical application list is the basis phases in `D`, followed by
`G_N^dagger,...,G_1^dagger`.  The runner independently reconstructs the full
Q1 and Q2 matrices, their reverse-dagger inverses, and their unitarity.  A
deleted nontrivial two-level factor must leave a finite residual.

### Gray equality macros

Each source/target basis pair is a pair of 13-bit physical M2 words.  A fixed
least-significant-bit-first Gray path connects them.  Equality-controlled X
transpositions carry the first basis ray to the penultimate path word, one
equality-controlled one-M2 core applies the explicit `2 x 2` factor, and the
transpositions reverse.  Every intermediate basis ray is restored.

An adjacent-state transposition is a 12-control X.  With ten clean conjunction
M2 it uses the standard `2k-3=21` Toffoli chain.  An equality-controlled
arbitrary one-M2 core uses a clean flag, exact compute/core/uncompute, and at
most eleven clean work M2.  Every Toffoli uses Cycle 523's exact 15-call
one-/two-M2 decomposition.  The arbitrary two-M2 controlled-core matrices and
their analog angles are explicit compiler data, not new primitive physics.

Intermediate excursions outside Q<=2 are allowed inside the declared compiler
workspace.  The completed factor list preserves Q and the coefficient-two
direction ledger exactly because it equals the target source unitary.

### Nearest-neighbor routing

The 13 data M2 and eleven reused clean work M2 receive distinct integer
coordinates.  Matter directions lie at radius two, field directions at radius
six, the reservoir at the origin, and work M2 at explicit off-axis points.
All integer sites in the invariant cube `[-6,6]^3` are supplied route M2.  This
is 2,197 sites per source cell, deliberately generous and not minimal.

Every possible live-wire pair is routed by a fixed Manhattan path.  A two-M2
primitive uses ordinary adjacent SWAP along the path, the core, then reverse
SWAP.  The runner checks all live-wire pairs and maps every actual route edge
through all 24 proper-cubic frames.  The cube and each mapped route remain
nearest-neighbor.  L5 and held L6 are nonaliased under the supplied period-32
macrocell placement.

## Proper-cubic schedule orbit

Cycle 426's local frame representation is a signed permutation of the Q1/Q2
basis.  Under a frame, every two-level core is moved to the mapped pair and
conjugated by the two inherited basis signs.  Basis phases move to the mapped
ray.  Thus the mapped physical factor list implements

```text
R_frame V_rec R_frame^dagger.
```

The runner applies every mapped factor list to independent complex probes in
all 24 frames and compares with direct conjugation and the invariant target.
It also checks the signed basis permutation on all 576 frame products in both
Q1 and Q2.  This is a compile-time schedule orbit; there is no runtime frame
selector.

## Retiring the Cycle-429 matter lift/readout import

Cycle 429 applied the source through the old Cycle-396 physical matter lift.
On the current selected carrier, Cycle 549 instead uses the exact normal form

```text
physical selected source = W_path SOURCE_q W_path^dagger.
```

`W_path^dagger` removes the selected native representative to Cycle 539's
fixed reference while retaining the eighteen physical q shadows.  The new
local gate compiler acts directly on one cell's six q M2 and seven resource
M2.  `W_path` prepares the synchronized output representative.  Cycle 539's
branch, order, conjunction work, and routes return blank as already
strict-pinned.

The Q1 raw-M2 source is conjugated by Cycle 426's exact one-hot resource
encoding and compared with the original Cycle-322 vertex.  It is then embedded
at A, B, and C on all 988 Cycle-429 matter labels and compared with all three
old Cycle-396 embedded operators.  The physical direction readout needs no
dense lift: it is the diagonal signed sum of the retained q occupation M2.

This removes the old `E_429 U E_429^dagger` source/readout import on the
declared Cycle-539 selected path code.  It does not prepare Cycle 539's fixed
reference and does not map into Cycle 540's rough carrier.

## Current-selected prediction preservation

The compiled source is inserted three times into Cycle 546's fixed current
apparatus.  The engine still uses one fixed A/B/C source order, two matter
edges, two field transports, and contact for every current sector.  Current is
never passed as a role argument.

The runner checks a coherent nonzero NULL/PLUS/MINUS superposition at L5 and
held L6 against the strict-pinned Cycle-546 output, then applies the compiled
reverse dagger.  It separately calculates PLUS and MINUS receiver responses,
odd direction coordinates, source resource balance, source and receiver
direction ledgers, and global Q.

Required deletions are:

- current controls;
- emitter source vertex;
- receiver source vertex;
- either transport edge; and
- contact.

NULL must remain exactly null.  The fixed Cycle-546 current tensor
permutations—256 complete basis states at L5 and 1,024 at L6—are rerun, so the
sparse current representation cannot substitute for a physical rail.

No Cycle-420 host observable or Cycle-432 phase-source value is fitted.  The
Cycle-434 response and odd vector are replayed because the compiled source
operator is the same frozen law.

## Mass, contact, seam, and supplied-law boundary

The source compiler preserves local matter number.  The surrounding selected
path compiler therefore retains the Cycle-219 rest mass, uniform one-particle
fixture, 645 nontrivial three-cell contact columns, both path FSWAPs, and the
strict-pinned Cycle-230 seam/contact fixtures.

Supplied rather than derived are:

1. coefficient two, `theta=0.8m`, angle sign/normalization, and source
   invocation;
2. Cycle 539's selected coefficients/Paulis, explicit `W_path`, fixed reference
   and its preparation, blank branch/order/work M2, and compiler tables;
3. explicit complex one-/two-M2 core matrices produced by the Givens compiler;
4. the exact Cycle-523 Toffoli decomposition and ordinary routing SWAP;
5. the current-correlated NULL/PLUS/MINUS matter/token preparation;
6. the reset route cube and compile-time frame; and
7. the Cycle-219 coin, Cycle-230 contact/order, field coin, transport, and
   three-update receiver fixture.

Retired on the declared code are the monolithic Cycle-426 Q<=2 source
exponential and Cycle-429 dense source lift/readout.  Open are Q>2 source
sectors, autonomous input/reference preparation, route-resource compression,
selected-to-rough carrier transduction, the host moving-source join, and any
energy/stress/gravity/Born/Record/time interpretation.

## Dependency-ledger effect

- `C_ref`: advances locally.  The source basis, component blocks, factor order,
  Gray convention, wire placement, and mapped schedule are explicit.  The
  coefficient, angle, fixed reference, and input preparation remain supplied.
- `C_num`: advances through exhaustive finite Q1/Q2 factorization and exact
  inverse.  Analog compiler angles and an error/precision theorem remain
  supplied/open.
- `C_wrap`: unchanged.  Factor order and route depth are not time, interval,
  occurrence, Record, or energy.
- `C_int`: advances materially.  Current, source recoil, receiver readout,
  mass/contact/seams, and inverse now sit behind the same selected physical
  gate compiler without the old dense matter lift.
- `C_local`: advances materially.  The bounded source is decomposed into
  explicit NN one-/two-M2 macros with blank return, all24/576 covariance, and
  held L6.  The route cube is supplied and inefficient.
- `C_source`: advances operationally.  The prepared reservoir is depleted and
  restored by a literal source circuit with exact direction ledgers.  No
  energy/stress source selection or gravity response is derived.

Maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.

## No-go discipline N1–N8

The fresh `origin/main` no-go-discipline skill and proof-search governance are
applied because this positive theorem retains named boundaries.  A broad
impossibility/minimum/axiom-pressure gate is **FAIL / DO NOT SHIP**.  Only the
positive bounded compiler and explicit supplies ship.

### N1 — normalized route registry

| route | mechanism / obligation | status |
|---|---|---|
| connected-component Givens | exact sparse generator components / two-level and phase factors / Q<=2 matrix equality | **ATTEMPTED — POSITIVE** |
| direct Pauli expansion | exponentiate physical Pauli words / handle noncommuting direction terms / exact bounded schedule | **OPEN** |
| SELECT over matter/resource words | compute local word label / multiplex exact component unitary / erase selector | **OPEN; equivalent alternative** |
| ancilla bright-state compiler | prepare each star/component bright state / one collective rotation / unprepare | **OPEN; likely compression route** |
| generic full 13-M2 QR | arbitrary unitary synthesis / exact full-space extension / practical bounded count | **OPEN; stronger and unnecessary** |
| rough-carrier native source | construct source directly in Cycle-540 rough variables / preserve current and receiver / avoid selected transducer | **OPEN and carrier-distinct** |

Open materially distinct routes prohibit a minimum or uniqueness claim.

### N2 — wall-independence audit

The collapsed open conditions are:

```text
W_prep: autonomous current-correlated input and fixed-reference preparation.
W_route: retire/compress the supplied 2,197-site route cube.
W_carrier: selected-to-rough transduction or a native rough source compiler.
W_host: derive the Cycle-420 host profile/centroid observable physically.
W_source: identify energy/stress source content and a gravity response.
```

The required pairwise audit is:

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `W_prep`, `W_route` | no | no | yes |
| `W_prep`, `W_carrier` | no | no | yes |
| `W_prep`, `W_host` | no | no | yes |
| `W_prep`, `W_source` | no | no | yes |
| `W_route`, `W_carrier` | no | no | yes |
| `W_route`, `W_host` | no | no | yes |
| `W_route`, `W_source` | no | no | yes |
| `W_carrier`, `W_host` | no | no | yes |
| `W_carrier`, `W_source` | no | no | yes |
| `W_host`, `W_source` | no | no | yes |

The independence is operational: preparing a code does not compress routes,
change carrier, derive a host observable, or identify stress content; none of
those reverse implications holds.  Likewise a carrier map does not select a
host observable or an energy/stress source law, and either physical-law bridge
can be tested without compressing this deliberately large router.  `Q>2` is an
extension domain, not inflated into a sixth independent constitutional wall.

### N3 — hidden-condition scan

The coefficient, angle/sign, source call, component diagonalization, exact
core matrices, Gray convention, negative controls, clean work, Toffoli,
routing SWAP, route cube, frame, fixed reference, current-correlated input,
factor order, and readout are explicit.  “Exact” is scoped to the finite Q<=2
and selected path codes.  “Standard” refers only to prior-art Givens/Gray/
Toffoli compiler machinery and discharges no physics obligation.

### N4 — residual matching

| witness | residual | Cycle-549 use | match? |
|---|---|---|---:|
| Cycle 426 | primitive source exponential open on physical seven-M2 star | direct target through Q<=2 | yes |
| Cycle 429 | dense physical matter source lift/readout | replaced by selected `W SOURCE_q W^dagger` and q readout | yes on 988 path code |
| Cycle 539 | explicit selected path isometry, fixed reference supplied | exact wrapper used here | yes |
| Cycle 540 | rough FSWAP gate compiler, distinct carrier | routing precedent/comparator only | no; no transducer claimed |
| Cycle 546 | actual current rails and frozen Cycle-434 receiver | exact downstream preservation target | yes |

No nonmatching Cycle-420 or Cycle-432 value supports a negative statement.

### N5 — rhetoric audit

| resolution | tested | disposition |
|---|---:|---|
| one component | every nontrivial Q1/Q2 block | exact factorization |
| one local source | all 448 Q1 and 1,344 Q2 columns | exact |
| one selected path | all three embedded source positions on 988 matter labels | exact |
| current apparatus | coherent NULL/PLUS/MINUS, L5/L6 | exact within tolerance |
| all frames | mapped factors/routes and 576 products | tested |
| Q>2 | not compiled | explicitly open |
| recurrent volume / rough carrier | not tested | no claim |
| energy/stress/gravity/Born/time | not identified | no positive or negative claim |

### N6 — partial-closure paths

The remaining imports have direct retirement paths: replace the route cube by
a bounded Steiner/accumulator network; synthesize the two matter preparations
with current-controlled SELECT/uncompute; use Cycle-542/544 reference work to
reduce fixed-reference preparation; or construct a separate selected-to-rough
isometry.  These are compiler/preparation campaigns, not axiom requests.

### N7 — hostile steelman

> A hostile reviewer should reject any assertion that the retained route,
> preparation, Q>2, or carrier boundaries are fundamental.  The component
> graph is finite and sparse; its size-nine maximum already exposes a bright-
> state or SELECT compiler that could sharply reduce the generic Givens count.
> Cycle 540 demonstrates that a large supplied blank reservoir can later be
> compressed without changing the target algebra, while Cycles 533/539 show
> how selected physical references and branch tables become explicit local
> circuits.  The terminal obligations are concrete factor count, blank return,
> intertwining, and covariance tests—not new axioms.

### N8 — cross-cycle echo

Cycle 530 isolated a dense selected isometry; Cycle 533 replaced it on code by
compute/select/uncompute.  Cycle 539 extended that compiler to shared paths.
Cycle 540 replaced a support-13 primitive FSWAP with literal routed Pauli
rotations.  Cycle 546 then replaced a host current branch with a literal tensor
Fredkin circuit.  Cycle 549 follows the same import-retirement pattern for the
source exponential.  The repeated constructive history argues for further
compression and preparation work, not axiom pressure.

## Cold certificate

The independent cold certificate passed **8/8** declared test families with
authority none and audit unset.  The measured runner section took
`2.5767029160633683` seconds after imports; the complete cold process took
`114.24` timed wall seconds.  Both the runner and external timer reported
`681,951,232` maximum RSS bytes, and process swap count was zero.

The exact local factorization results were:

| quantity | Q1 | Q2 |
|---|---:|---:|
| dimension | 448 | 1,344 |
| nontrivial components | 56 | 272 |
| two-level factors | 136 | 888 |
| basis-phase factors | 0 | 0 |
| maximum factorization residual | `2.914335439641036e-16` | `6.661338147750939e-16` |
| Frobenius factorization residual | `1.9921756540021205e-15` | `5.147522571132738e-15` |
| inverse/unitarity maximum | `4.440892098500626e-16` | `1.3322676295501878e-15` |
| deleted-factor Frobenius residual | `0.5101624372570307` | `0.5101624372570307` |

The exact serialized factor-list digests were
`dfaae68074f15f3828ffbb25791eb36710ffcd1581b3936c9a8dd50f57a6886a`
for Q1 and
`767174d17e1a9f109d044d972c19c18089f39f548135adcdae7170a77fffed62`
for Q2.

Across both sectors the literal compiler used 1,024 two-level cores and 7,496
Gray equality MCX macros.  The maximum source/target Hamming distance was ten.
The conservative upper bound was 200,424 Toffolis and 3,007,384 bare one-/two-
M2 calls before routing.  Gray/core truth failures and terminal work failures
were zero.  The normalized 12-control conjunction was exhausted on 8,192
target/input cases with clean return.  Cycle 523's pinned 15-call Toffoli was
re-executed inside this runner: its reconstruction residual was
`7.346882794269506e-16`, inverse residual was `1.2749064385906742e-15`, and
maximum primitive support was two M2.

All 576 live-wire pairs were routed.  Maximum route length was 24 adjacent
edges; base and mapped route failures were zero.  The maximum all-frame mapped
factor residual was `1.6986308271319277e-16`, and the Q1/Q2 signed
representation had zero failures across all 576 frame products per sector.

The compiled raw-Q1 to Cycle-322 vertex residual was
`2.7755575615628914e-16`.  Each A/B/C embedded operator had shape
`6916 x 6916`, 8,920 nonzeros matching the old operator, raw residual
`2.7755575615628914e-16`, and random-vector residual below
`5.87e-17`.

The current-selected prediction controls gave:

```text
coherent compiled-vs-Cycle546 residual, L5/L6:
    2.32768182394929e-16 / 2.32768182394929e-16
compiled reverse-dagger residual, L5/L6:
    2.7129713093607372e-15 / 2.7129713093607372e-15
maximum branch complete-state residual:
    3.864542011364523e-16
PLUS receiver response:
    0.00013490525789067816
MINUS receiver response:
    0.0001349052578906781
NULL full-state residual:
    0
```

The PLUS/MINUS receiver coordinates retained opposite x components
`+/-1.53739423e-4`.  Source resource-balance residuals were
`-1.5543122344752192e-15` and `-1.1102230246251565e-15`; all source and
receiver direction-ledger residuals were below `5.56e-17`.  Global Q drift was
below `1.6e-15`.  Deleting current, emitter source, receiver source, or either
transport edge gave exactly zero receiver response.  Contact deletion changed
the response to `0.0001299208266517126`.

The Cycle-219/three-cell mass remained `0.4534056541748851` with uniform
one-particle residual `3.534751832054436e-16`; contact retained 645 nontrivial
columns and both path FSWAP unitarity residuals were zero.

## Disposition and next campaign

Retain Cycle 549 only if its cold runner passes.  Its intended result is the
literal bounded source compiler on complete Q<=2 plus the selected-path
source/readout lift needed by Cycle 546.

The optimal next campaign is autonomous preparation: compile the mirror
current-correlated Cycle-434 matter seeds and Q1 token from locally supplied
number-preserving resources, then compose with the new source gates and test
multi-update recurrence.  Route compression and a selected-to-rough
transducer remain independent secondary campaigns.
