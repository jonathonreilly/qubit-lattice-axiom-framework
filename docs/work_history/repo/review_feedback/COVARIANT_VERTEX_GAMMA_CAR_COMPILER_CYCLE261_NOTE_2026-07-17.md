# Covariant vertex-gamma CAR compiler — Cycle 261

Date: 2026-07-17
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/covariant_vertex_gamma_car_compiler_cycle261_2026_07_17.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status. It creates only this note and runner.

## Result up front

The degree-five square-pyramid vertex admits the requested exact local
Clifford seed. Six local Clifford Majoranas on three M2 roles provide five
incident edge labels and one missing-gamma occupation parity. The resulting
operators have the exact even-CAR incidence algebra, bounded support, constant
overhead, no Jordan-Wigner string, and a phase-resolved signed-Pauli action of
all 24 proper-cubic frames with the exact group law.

This is a substantive constructive closure of the **local algebra and frame
action**, but it is not yet a physical full-Fock compiler.

Let `N=L^3`, `V=6N`, and place three physical M2 qubits at every graph vertex.
The degree-five loop code has

```text
physical qubits Q:                 18N
bounded elementary-loop rank:      9N - 2
rank after three Wilson loops:      9N + 1
code exponent Q-rank:               9N - 1
target full-Fock exponent V:        6N
exact auxiliary excess:             3N - 1 = V/2 - 1
```

Both total-parity sectors exist, but each retains the same `3N-1` excess over
its target Fock-parity sector. Thus the degree-five chart is an exact local
CAR representation with unremoved auxiliary logical content, not an encoding
`E` of the Cycle-230 full Fock space.

The steelmanned sixth-edge route is also constructive. Inside every coarse
cell, pair opposite direction roles `(0,1),(2,3),(4,5)`. This is an onsite
dummy perfect matching invariant as a set under every proper-cubic frame and
every coarse translation. It uses each vertex's missing gamma as its sixth
edge label and uses three-qubit chirality `Z Z Z` as occupation parity. With
bounded dummy triangles plus the original elementary loops, its ranks are

```text
dummy edges:                       3N
bounded augmented-loop rank:       12N - 2
rank after three Wilson loops:      12N + 1
code exponent:                      6N - 1 = V - 1
```

This is exactly the even-Fock-sector exponent. The stabilizer phase system is
consistent for positive total parity and inconsistent for negative total
parity. The odd sector is deleted. The dummy completion is therefore a
proper-cubic covariant local **even-sector GSE-shaped code**, not a common
full-Fock `E`.

The frame result is phase resolved, not merely symplectic. An initial raw
direction-permutation check does not by itself control Pauli signs. The runner
therefore solves exact affine GF(2) sign systems allowing the sign to depend on
frame, source vertex role, and gamma label:

| chart | variables | equations | coefficient rank | augmented rank | solution dimension |
|---|---:|---:|---:|---:|---:|
| degree five: positive `B_v` and every `A_e` | 864 | 21,276 | 848 | 848 | 16 |
| degree six: positive chirality, original `A_e`, and dummy `A_e` | 864 | 21,348 | 850 | 850 | 14 |

Twelve frames induce odd raw permutations of the six gamma labels. The
degree-six affine solutions supply signs that cancel the resulting chirality
flip while preserving every edge sign and the exact groupoid composition
law. Each signed Pauli automorphism has a local Clifford implementer; scalar
phases of the implementing unitaries may be projective, but do not alter
conjugation. Consequently there is **no chirality-covariance obstruction** in
this displayed signed-label chart.

Neither candidate supplies one common full-Fock encoding, and bounded
elementary constraints leave three topological Wilson logicals. Therefore
bounded autonomous preparation, sector selection, the actual Cycle-230
free-plus-contact update, one-particle mass fixture, and mass/contact/seam
intertwining are not reached. No failure of those downstream gates is claimed.

The narrow route dispositions are:

| candidate | constructive content | exact residual |
|---|---|---|
| degree-five missing-gamma chart | both parity sectors; exact local CAR; exact all-frame signed action | `V/2-1` auxiliary logical qubits after full loop fixing |
| opposite-role dummy completion | exact even-sector dimension; exact local CAR; exact all-frame signed action | odd total-parity sector absent |
| bounded elementary constraints alone | supports at most 24; local and translation covariant | three Wilson logicals remain |
| common full-Fock physical compiler | not constructed | no shared `E`, hence `E G_coarse = G_physical E` is not yet testable |

These are chart-specific residuals, not a route-independent obstruction. There
is no general no-go, no minimum-content conclusion, and no axiom pressure.

## 1. Local gamma construction

At every square-pyramid graph vertex use three physical M2 qubits and the
Jordan-Wigner Clifford chart

```text
gamma_0 = X I I
gamma_1 = Y I I
gamma_2 = Z X I
gamma_3 = Z Y I
gamma_4 = Z Z X
gamma_5 = Z Z Y.
```

All six operators are Hermitian, linearly independent as Pauli symplectic
vectors, square to identity, and pairwise anticommute. Their maximum support is
three.

The graph vertex `(cell,d)` has degree five. Its incident neighbors realize
all direction roles `r != d`. Define

```text
B_(cell,d)       = gamma_d^(cell,d),
A_((cell,d),v_r) = gamma_r^(cell,d) gamma_d^v_r.
```

Thus the label missing from the five edge endpoints is used as `B_v`. Direct
replay on the `L=3` graph gives

```text
incident-edge-pair failures: 0
B_v / incident-A_e failures: 0
disjoint-edge failures:      0
maximum support(B_v):        3
maximum support(A_e):        6.
```

This is an exact representation of the local even-CAR generator relations. It
does not assert that the three physical qubits at a vertex are three fermionic
modes, nor does it silently identify their full Hilbert space with one coarse
mode.

## 2. Proper-cubic frame action

Each proper-cubic frame permutes the six signed coordinate directions. The six
gamma symplectic vectors form a basis of the local three-qubit Pauli space, so
permuting them defines a symplectic linear action. The runner checks all 24
frames, all 64 local Pauli vectors, and all `24^2` frame products:

```text
symplectic-form failures:       0
gamma-label-map failures:      0
vector group-law failures:     0
missing-label vector failures: 0.
```

That vector check alone is not called physical covariance because it erases
operator signs. The two affine sign systems then impose:

1. zero signs for the identity frame;
2. exact signed groupoid composition as the source vertex role transforms;
3. positive transformation of the degree-five missing-gamma `B_v` and every
   original edge `A_e`; or
4. for degree six, positive transformation of chirality, all original edges,
   and all dummy edges.

Equal coefficient and augmented ranks prove both systems consistent. The
result is exact operator covariance under conjugation. Only the scalar phase
choice of each implementing Clifford unitary remains projective; this scalar
cannot change an encoded observable or gate under conjugation.

## 3. Degree-five loop code and rank

For an ordered graph cycle `C`, use the Hermitian loop word

```text
S_C = i^|C| product_(e in C) A_e.
```

The elementary cycles are the bounded Cycle-235 primal-edge cycles. Three
additional Wilson cycles span the closed torus homology. At `L=3`, all 300
displayed loop operators (297 elementary and 3 Wilson) are Hermitian, mutually
commuting, and commute with every edge generator.

Exact phase-aware ranks are:

| `L` | `N` | `V` | local rank | full rank | code exponent | Fock exponent | excess |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 162 | 241 | 244 | 242 | 162 | 80 |
| 4 | 64 | 384 | 574 | 577 | 575 | 384 | 191 |
| 5 | 125 | 750 | 1123 | 1126 | 1124 | 750 | 374 |
| 6 held out | 216 | 1296 | 1942 | 1945 | 1943 | 1296 | 647 |

The exact formulas are `rank_local=9N-2`, `rank_full=9N+1`, and
`excess=3N-1`. Adding positive or negative total parity increases rank by one
without a phase inconsistency in either case. Each sector exponent is
`9N-2`, compared with target `6N-1`; both sectors therefore retain the same
`3N-1` excess.

The maximum elementary-loop support is 24 for every tested size. Wilson-loop
support is `7L` and total-parity support is `12N`; neither is called bounded.

## 4. Covariant sixth dummy edge

For each cell, pair its opposite direction vertices:

```text
(0,1), (2,3), (4,5).
```

This is a perfect matching of all `6N` vertices with `3N` dummy edges. No
member of a pair is marked. All 24 frame maps and every coarse translation at
`L=3,4,5,6` preserve the matching as an unordered set. The dummy-edge Pauli is
the product of the two endpoints' previously missing gammas and has support at
most six.

Every vertex now has six gamma-labeled edges. Occupation parity is the local
chirality

```text
B_v = Z Z Z,
```

which anticommutes with every local gamma. Four bounded dummy triangles per
dummy edge join the original elementary-loop family. The resulting exact
phase-aware data are:

| `L` | dummy edges | local augmented rank | full rank | code exponent | even target | odd sector |
|---:|---:|---:|---:|---:|---:|---|
| 3 | 81 | 322 | 325 | 161 | 161 | inconsistent |
| 4 | 192 | 766 | 769 | 383 | 383 | inconsistent |
| 5 | 375 | 1498 | 1501 | 749 | 749 | inconsistent |
| 6 held out | 648 | 2590 | 2593 | 1295 | 1295 | inconsistent |

The exact formulas are `rank_local=12N-2`, `rank_full=12N+1`, and code
exponent `6N-1=V-1`. Positive total parity is already generated by the loop
stabilizers and adds no rank. Negative total parity produces one phase
inconsistency. At `L=3`, all augmented loops are Hermitian, mutually commute,
and commute with every original and dummy edge generator.

This matches the generalized-superfast even-sector shape. It does not join the
two physical fermion-parity sectors.

## 5. Physical M2 placement and boundedness

The three qubits at direction vertex `d` are placed at radii `6,12,18` along
direction `d` inside the period-64 coarse cell. This gives 18 distinct
ordinary M2 roles per coarse cell. Every proper-cubic frame permutes each
radial shell, and period-64 coarse translation maps the full placement to
itself on the periodic fixture.

The routing data are constant-size:

```text
physical M2 roles per coarse cell: 18
maximum gamma/B support:            3
maximum original/dummy A support:   6
maximum elementary check support:  24
```

The period-64 macro origin and shell radii are supplied compiler structure.
The runner's unit-translation deletion control changes 972 active points at
`L=3`; therefore the macro marker is not misreported as emergent unit-lattice
covariance.

No global Jordan-Wigner ordering, global parity string, or host-side parity
service appears in either local operator algebra. The remaining Wilson and
preparation issues are stated separately rather than hidden in “local.”

## 6. Preparation, lawful domain, and controls

The lawful tested domain is the closed periodic square-pyramid cellulation at
`L=3,4,5,6`. The held-out L=6 case is not used to construct the formulas and
replays every symbolic rank formula.

Controls include:

- deleting the three Wilson constraints lowers rank by exactly three in both
  charts;
- positive and negative total-parity rows demonstrate that both degree-five
  sectors exist;
- the same rows demonstrate that degree six fixes positive parity and deletes
  negative parity;
- removing the dummy completion returns the exact degree-five `V/2-1`
  auxiliary excess;
- raw symplectic frame covariance is separated from the phase-resolved affine
  sign audit;
- all frame, translation, commutator, Hermiticity, rank, phase-consistency,
  support, macro-marker, and held-out-size checks are exact.

Bounded elementary checks leave three Wilson logicals. Fixing the displayed
closed-torus code space uses three noncontractible Wilson constraints.
Selecting a degree-five parity sector additionally uses extensive total
parity. Degree six fixes even parity locally/algebraically but has no odd
sector. No bounded autonomous preparation or bounded sector-selection circuit
is constructed.

These are code-space and preparation residuals. A classical stabilizer setup
schedule is not a physical time law.

## 7. Actual-update and fixture firewall

The required gate chain remains

```text
one common full-Fock E
  -> encode Cycle-230 coin / A-B FSWAP / contact gates
  -> prove E G_coarse = G_physical E
  -> replay one-particle mass and contact/seam fixtures.
```

Neither chart closes the first step. The runner therefore imports and checks,
but does not synthesize from,

```text
beta=-0.3
g=0.37
Cycle-219 rest fixture = 0.4534056541748851
Cycle-230 principal sea rank = 73.
```

The coin/A-B FSWAP/contact update, its iteration, leakage under the actual
gate, the one-particle mass fixture, the local contact block, and the rank-73
mass seam are not claimed reproduced or falsified. “Mass seam” remains a
fixture label, not a physical-source derivation.

## 8. Supplied-structure inventory

Cycle 261 supplies or inherits:

1. the Cycle-235 periodic square-pyramid graph, direction roles, elementary
   cycles, and three Wilson cycles;
2. a three-qubit Clifford chart and the assignment of its six gamma labels to
   direction roles;
3. three ordinary M2 roles at every graph vertex, hence 18 per coarse cell;
4. radial shell coordinates `6,12,18` inside a supplied period-64 macrocell;
5. the period-64 macro origin and coarse translation marker;
6. the degree-five missing-label definition of `B_v` and cross-label
   definition of `A_e`;
7. the opposite-role dummy perfect matching and four dummy triangles per
   dummy edge;
8. closed periodic boundaries and sizes `L=3,4,5,6`;
9. exact GF(2), Pauli, phase-aware-rank, and affine sign-system arithmetic;
10. three noncontractible Wilson constraints when the full displayed code
    rank is quoted;
11. fixed `beta=-0.3`, `g=0.37`, predecessor mass, and sea-rank fixtures; and
12. classical enumeration and memory sufficient to execute the certificate.

No macro-marker formation, state preparation, measurement, probability,
Record semantics, physical clock, parameter-selection law, update law,
energy, stress, source, or gravity coupling is derived.

## 9. Prior-art and novelty boundary

Bravyi and Kitaev, *Fermionic quantum computation*, Sec. 8,
arXiv:quant-ph/0003137; *Annals of Physics* **298** (2002), establishes
constant-cost bounded-degree simulation of local even fermionic operations
with edge qubits and cycle stabilizers, explicitly treating the even sector
and code-state preparation separately. This cycle does not claim bounded
local even-sector fermion simulation as new.

Setia, Bravyi, Mezzacapo, and Whitfield, *Superfast encodings for fermionic
quantum simulation*, arXiv:1810.05274; *Physical Review Research* **1**,
033033 (2019), develops generalized superfast encodings on sufficiently
connected graphs. Setia and Whitfield, *Bravyi-Kitaev Superfast simulation of
fermions on a quantum computer*, arXiv:1712.00446, provides the preceding BKSF
context. The dummy-completed degree-six rank is described as GSE-shaped, not as
a new general encoding theorem.

Cycle 235 supplies the repository's exact even-CAR loop comparator. Cycle 252
supplies a coherent even/odd join with different physical content. Cycle 258
supplies the explicit challenge to try a covariant local gamma vertex.

Cycle 261's fixture-specific new content is limited to:

1. the six-gamma degree-five role assignment on this square-pyramid graph;
2. exact local algebra, loop commutator, and all-size rank certificates;
3. the `V/2-1` degree-five excess formula with both sectors retained;
4. the proper-cubic opposite-role dummy matching and dummy-triangle code;
5. its exact even-sector rank and odd-sector phase deletion;
6. the two exact phase-resolved all-frame affine sign-lift certificates; and
7. the explicit 18-role period-64 physical placement and bounded support
   audit.

No global novelty priority is claimed. No Thirring engine is used, extended,
or compared.

## 10. TOE dependency ledger after Cycle 261

| Workstream | Cycle-261 effect | Remaining dependency |
|---|---|---|
| `C_ref` | no global order, parity string, marked dummy pair, or host parity service enters the local algebra | period-64 macro origin, Wilson sector, code state, physical sea, and parameters remain supplied |
| `C_num` | strong gain: exact local `B_v/A_e` CAR incidence; degree five retains both parities and degree six realizes the exact even-sector exponent | remove degree-five excess or coherently join degree-six odd parity; derive physical number preparation/readout |
| `C_wrap` | three Wilson logicals and their exact rank increment are explicit | bounded/local preparation or operational treatment of topological sectors remains open |
| `C_int` | a gate-synthesis-ready even-CAR algebra exists, but no common full-Fock `E` | actual encoded coin/A-B FSWAP/contact, leakage, iteration, and physical rate remain open |
| `C_local` | strong gain: support at most 24, 18 M2 roles/cell, exact all-frame signed covariance, all translations, and held-out `L=6` | full-Fock sector join, bounded preparation, and emergent rather than supplied macro roles remain open |
| `C_source` | unchanged | no energy, action, stress, source, or gravity coupling is selected |

Maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.
This cycle materially advances the local quantum substrate but does not yet
move a cross-lane physical prediction.

## 11. No-go discipline N1–N8

The only narrow negatives are:

> After the declared loop constraints, the displayed degree-five gamma chart
> has exactly `V/2-1` auxiliary logical qubits beyond the full-Fock target.

> The displayed opposite-role degree-six dummy completion has exactly the
> even-Fock-sector dimension and no consistent odd-total-parity sector.

Neither statement ranges over other local Clifford bundles or coherent sector
joins.

### N1 — alternative routes

| route | honesty marker | exact disposition |
|---|---|---|
| degree-five missing-gamma algebra | **ATTEMPTED** | exact local CAR and both parity sectors; `V/2-1` excess remains |
| all bounded elementary loops | **ATTEMPTED** | exact ranks `9N-2` and `12N-2`; three Wilson logicals remain |
| add all three Wilson loops | **ATTEMPTED** | exact rank increment three; degree-five excess remains and degree-six stays even only |
| select either degree-five total parity | **ATTEMPTED** | both signs are consistent; each sector retains `3N-1` excess |
| opposite-role sixth-edge perfect matching | **ATTEMPTED** | removes the rank excess exactly, but fixes even total parity |
| phase-resolved proper-cubic gamma action | **ATTEMPTED** | both affine sign systems are consistent; covariance is not the residual |
| covariant 18-role physical placement | **ATTEMPTED** | bounded and collision free; macro marker remains supplied |
| edge-qubit/GSE even-sector encoding | **RULED OUT BY PRIOR ART as a negative route** | known constructive even-sector locality blocks any universal locality no-go |

A coherent even/odd direct sum of two degree-six sectors, a different gamma
bundle, subsystem/gauge treatment of Wilson logicals, and open boundaries are
not attempted and remain live.

### N2 — condition independence

The degree-five `K_rank` residual and degree-six `K_sector` residual are
alternative-route failures. They are not accumulated into one shared wall.
`K_cov` is closed for both displayed charts.

For a complete physical compiler the remaining conditions are:

- `K_join`: one coherent, local full-Fock sector join with no global parity
  service;
- `K_top`: bounded preparation or lawful subsystem treatment of the three
  Wilson logicals;
- `K_marker`: formation or retirement of the supplied period-64 macro roles;
- `K_law`: actual update and parameter realization after a common `E` exists.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---:|
| `K_join`,`K_top` | no | no | yes |
| `K_join`,`K_marker` | no | no | yes |
| `K_join`,`K_law` | enables testing only | no | yes |
| `K_top`,`K_marker` | no | no | yes |
| `K_top`,`K_law` | no | no | yes |
| `K_marker`,`K_law` | no | no | yes |

Actual gate synthesis is downstream of `K_join` here and is not counted as an
independent negative.

### N3 — hidden-condition scan

“Local,” “bounded,” “covariant,” “occupation parity,” “code exponent,” and
“both parity sectors” have executable definitions above. Raw symplectic
covariance is not used as a substitute for positive operator transformation;
the affine sign systems close that gap. “Perfect matching” means a tested
unordered edge set and does not mark one pair. “GSE-shaped” marks a prior-art
comparison, not an identity of every convention.

The periodic boundary, three Wilson constraints, gamma chart, shell placement,
macro marker, fixed parameters, and state-preparation absence are explicit.
No phrase such as “by construction,” “standard QFT,” “naturally,” “obviously,”
“registered,” “canonical,” measurement, Born, Record, energy, or physical rate
bears either narrow conclusion.

### N4 — residual matching

| witness | prior residual | Cycle-261 match |
|---|---|---|
| `RADIUS_TWO_INCIDENT_CAR_QUADRATIC_TOURNAMENT_CYCLE258_NOTE_2026-07-17.md`, N6 and optimal next campaign | try a proper-cubic local gamma register after the radius-two Pauli chart failed | executed directly |
| `EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md`, local algebra and loop sections | exact even-CAR incidence and loop comparator | same graph and exact Pauli relations used |
| `COHERENT_EVEN_ODD_SECTOR_JOIN_CYCLE252_NOTE_2026-07-17.md`, rank/join sections | retaining both parity sectors needs coherent extra content | degree-five retains both with excess; degree six deletes odd parity |
| Cycle 230 free/contact/seam fixture | actual update and rank-73 seam target | retained behind the common-`E` firewall only |
| Bravyi-Kitaev and Setia et al. | bounded local even-sector encodings exist | matches the constructive degree-six disposition and blocks a broad no-go |

The narrow rank and parity statements rest on Cycle 261's phase-aware rank
certificate, not on another route's failure.

### N5 — resolution audit

| resolution | tested | not established |
|---|---|---|
| one vertex | all six gammas and every local CAR relation | arbitrary local Clifford bundles |
| one full `L=3` graph | every edge relation and every loop commutator | every boundary condition |
| all 24 frames and `24^2` products | symplectic action and exact signed groupoid lift | Lorentz/boost covariance |
| every coarse translation | dummy matching and role-family covariance | emergent unit translations |
| `L=3,4,5,6` | exact ranks, parity phases, and supports | thermodynamic theorem beyond the displayed formulas |
| held-out `L=6` | both rank formula families | unrelated graph families |
| actual update | not reached | gate, leakage, mass, contact, or seam failure is not claimed |

The narrow negatives are stated only for the two exhausted displayed charts.

### N6 — partial-closure scan

No axiom edit is indicated. Live constructive closures are:

| path | status | possible closure |
|---|---|---|
| coherent direct sum of two degree-six parity sectors | untested priority | supplies the missing factor of two while retaining exact even-code ranks |
| local coherent parity carrier tied to the two copies | untested | may avoid a global sector selector |
| subsystem treatment of the three Wilson logicals | untested | may make nonlocal stabilizer selection operationally unnecessary |
| different signed gamma bundle or extra bounded role | untested | may realize both parity sectors without duplication |
| separate parity-sector gate compilation | algebraically available | can test local gates, but is not one common full-Fock `E` |
| bounded code-state preparation | separate open task | can close preparation without changing the algebra |

These are compiler and state-preparation routes, not demands for new axioms.

### N7 — steelman

> A hostile reviewer should accept the local-algebra result and reject any
> broader obstruction. The dummy completion already has exactly the right
> dimension for one parity sector, exact bounded checks, and an exact
> proper-cubic signed Clifford action. The missing full-Fock factor is only a
> factor of two. A coherent local parity carrier or direct sum of two
> covariant GSE sectors could restore it. The three Wilson degrees may be
> treated as gauge/subsystem data rather than fixed by nonlocal stabilizers.
> Different Clifford bundles and open-boundary encodings also remain live.
> Bravyi-Kitaev and Setia et al. already demonstrate that bounded-degree even
> fermionic locality is constructive. Therefore neither the degree-five rank
> mismatch nor the degree-six odd-sector deletion is constitutional evidence.

This steelman is convincing. The broad no-go fails. Only the two exact
chart-specific dispositions survive.

### N8 — cross-cycle echo

| earlier boundary | retirement/live mechanism | Cycle-261 response |
|---|---|---|
| Cycle 244 classical sign choice | keep the sign frame coherent | solve exact signed frame actions rather than choose a marked sign |
| Cycle 245 marked charge | coherent carrier rather than classical sector label | introduce no marked dummy pair; keep coherent parity join live |
| Cycle 249 gauge-frame choice | coherent Clifford conjugation | phase-resolve the frame action with affine signs |
| Cycle 251 rough multiplicity | operational subsystem equivalence | keep Wilson logicals as a possible subsystem route |
| Cycle 252 coherent even/odd join | extra coherent carrier | identifies the live repair for the degree-six missing factor two |
| Cycle 258 radius-two negative | change to local Clifford gamma chart | closes the exact local CAR wall constructively |
| Bravyi-Kitaev/Setia even-sector construction | edge/gamma code plus loop checks | blocks any locality or minimum-content no-go |

Earlier representation walls were repeatedly closed by coherent enlargement,
gauge treatment, or a different chart. Those mechanisms remain live here.
N1-N8 therefore supports only the displayed rank/parity statements and rejects
a shared obstruction, minimum-content conclusion, or axiom pressure.

## 12. Record and time firewall

The three M2 gamma carriers are coherent code degrees of freedom. They are not
measured, actualized, permanent, or decoded as Records. Dummy edges are
code-design relations, not realized histories.

GF(2) elimination, Clifford decomposition, sign-lift composition, stabilizer
layers, preparation depth, runner duration, and gate schedule are compiler
resources. **Compiler layers are not physical time.** No generator element is
called a rate, and no clock, duration, event occurrence, probability, Record
formation, energy, or source is derived.

## Route disposition and optimal next campaign

Retain the degree-five local gamma algebra, both exact signed frame lifts, the
opposite-role dummy matching, all-size rank formulas, 18-role placement,
support bounds, parity deletion controls, supplied-structure inventory, and
fixture firewall.

Do not call the degree-five chart a full-Fock encoding; its exact excess is
`V/2-1`. Do not call the degree-six chart a full-Fock encoding; it is exactly
even-sector only. Do not synthesize the Cycle-230 gates as though one common
`E` had been established.

The optimal next campaign is a coherent parity-sector doubling of the
degree-six code: construct two covariant copies or one locally controlled
copy, couple the copy label to a bounded coherent parity carrier, demand total
exponent `V`, and replay all frame signs, elementary loops, Wilson/subsystem
rank, preparation, both parity sectors, and held-out sizes. Only if that gives
one common full-Fock `E` should the actual `beta=-0.3`, `g=0.37` coin/A-B
FSWAP/contact gates and mass/contact/seam fixtures be synthesized.

There is no shared obstruction, no axiom pressure, and no axiom conclusion.

## Verification

```text
python3 scripts/covariant_vertex_gamma_car_compiler_cycle261_2026_07_17.py
```
