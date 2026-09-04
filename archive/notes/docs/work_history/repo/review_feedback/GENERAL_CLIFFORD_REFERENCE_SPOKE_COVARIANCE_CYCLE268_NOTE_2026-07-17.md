# General Clifford reference-spoke covariance — Cycle 268

Date: 2026-07-17
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/general_clifford_reference_spoke_covariance_cycle268_2026_07_17.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status. It creates only this note and runner.

## Result up front

The Cycle-264 all-frame failure is not repaired by allowing a general local
Clifford on the fixed six-M2 reference pair motif, stabilizer-equivalent
product representatives, or cell/role coboundaries.

This conclusion is exact but deliberately narrow. It covers code-preserving
onsite Clifford/Pauli-product maps on the declared physical-role blocks that
preserve the physical-edge and spoke logical classes. It does not cover
multi-cell Clifford circuits, different reference bundles, non-Pauli maps,
changed edge classes, orientation-character carriers, or other encodings.

The decisive reduction is the pair-code logical quotient:

```text
physical Paulis on six reference M2 sites:       4096
centralizer of three pair checks:                 512
logical Pauli cosets:                              64
stabilizer-equivalent representatives/coset:        8.
```

All six reference gamma classes have exactly eight physical product
representatives. Original physical edges fix five gamma classes at every
physical role; scalar chirality fixes the sixth. All six spokes fix all six
reference gamma classes modulo the pair stabilizers. Therefore every searched
code-preserving local Clifford/product action descends to the same signed
permutation of the six logical gammas. The broader physical search is not
silently reduced by assumption; the edge, chirality, spoke, and quotient
constraints force the reduction.

At the fixed reference role, the exact all-frame scalar-chirality sign system
has

```text
variables:          144
equations:         3486
coefficient rank 138
augmented rank 139.
```

Thus no signed logical lift preserves scalar reference chirality with the
exact group law of all 24 proper-cubic frames.

There is also a one-frame certificate. For each frame, XOR the seven
chirality equations, fifteen original-edge equations, and six spoke
equations. Every sign variable occurs twice, leaving

```text
0 = parity(permutation of the six direction labels).
```

Twelve frames have even direction-label permutation and solve with rank
`27/27`. Twelve have odd permutation and give rank `27/28`. The complete
1,008-variable positive-chirality/positive-edge system gives `992/993`.

Adding arbitrary products of the three positive pair stabilizers to every
transformed reference gamma does not repair the quotient. The exact extended
system has

```text
variables:             1440
coefficient rank:      1406
augmented rank:        1407.
```

Vertex rephasings and cell/role coboundaries also fail. Each vertex has degree
six, so a vertex coboundary changes six incident edge signs and six gamma
signs. It changes neither total edge-sign parity nor chirality. The same
`27/28` odd-frame contradiction survives.

The strongest result is constructive, not negative: if reference chirality is
allowed to transform as a pseudoscalar under the odd direction permutations,
the complete local system closes exactly:

```text
coefficient rank = augmented rank = 992
solution dimension = 16.
```

Physical-mode chirality, all original edges, all spokes, pair checks, and the
exact group law remain positive. Only reference chirality carries the
nontrivial permutation-sign character. This repair demonstrates that the
wall is representation-specific and supplies the optimal next ingredient: a
coherent orientation-character carrier that can combine with reference
chirality to make a scalar.

The pseudoscalar alone is not the requested compiler. With `N=L^3` reference
modes, total reference parity changes by `(-1)^N` under an odd frame. It maps
the full loop-code sector out of itself at `L=3,5`; it preserves that sector at
`L=4,6`. No single action therefore works on the declared all-size domain.

All Cycle-264 science regressions remain exact: 24 physical M2 roles/cell,
expanded local support at most 24, ranks through held-out L=6, zero `L=3`
reference-equality leakage, and the earlier odd-sector deletion at even
volumes. No common full-Fock E is obtained, so actual Cycle-230 gate, mass,
contact, or rank-73 seam synthesis is not reached.

There is no general local-unitary no-go, no general reference-bundle no-go, no
minimum-content claim, and no axiom pressure.

## 1. Fixed physical and logical domain

The reference register uses six ordinary M2 sites at radius 24 along
`+/-x,+/-y,+/-z`. Three local `ZZ` checks pair opposite sites, leaving three
logical qubits. Proper-cubic frames permute or swap the three pairs without a
marked orientation. The motif is collision-free with the physical-mode shells
at radii `6,12,18`; its constant route bound is 16 inside the period-64 cell.

The local pair-code centralizer has symplectic dimension nine. Quotienting its
three stabilizer directions leaves the six-dimensional symplectic space of
three logical qubits. Explicit enumeration gives 64 cosets of eight physical
Paulis each. The six gamma-coset support ranges are

```text
(2..6), (2..6), (3..5), (3..5), (4), (4).
```

Hence every stabilizer-equivalent product representative remains bounded.
All 24 frames preserve the three pair checks as an unordered set.

The search assumes:

1. each fixed physical three-qubit role block maps locally to its transformed
   role block;
2. the six-site reference pair motif maps locally to itself;
3. every pair check remains in the positive pair-stabilizer group;
4. physical occupation chirality is a scalar;
5. reference occupation chirality is initially demanded to be a scalar;
6. original physical edges and spokes map to their transformed logical
   classes with positive sign; and
7. frame composition obeys the exact group law.

These assumptions are the exact scope of the negative.

## 2. Why general local Clifford actions collapse to the quotient search

At physical role `d`, original edges use the five gammas `gamma_r`, `r != d`.
Their transformed tensor factors fix five target gamma symplectic classes. A
Pauli on one endpoint cannot be canceled by a different class on the disjoint
endpoint. The five fixed gammas plus scalar chirality have rank six.

For each missing label, exactly two local Pauli vectors anticommute with the
five fixed target gammas. Requiring the product of all six gammas to be target
chirality selects exactly the missing target gamma. The runner verifies this
for all six labels.

At the reference motif, all six spokes constrain all six logical gamma
classes. A code-preserving Clifford maps logical Paulis to logical Paulis. Its
physical representative may differ by any pair-stabilizer word, but quotienting
by the positive pair checks leaves the same six forced gamma classes.

Consequently an arbitrary searched local symplectic Clifford does not retain
an untested product freedom at logical level. Its only remaining data are the
signs of the six forced gamma images and stabilizer representative choices.

This argument does not cover a Clifford whose support spans multiple cells or
changes the declared edge/spoke logical classes.

## 3. Scalar-chirality sign obstruction

For a proper-cubic frame `g`, let `p_g` permute the six direction labels. At
the fixed reference role, write

```text
gamma_a -> (-1)^t(g,a) gamma_(p_g(a)).
```

Identity and exact composition impose

```text
t(1,a) = 0,
t(gh,a) = t(h,a) + t(g,p_h(a)) mod 2.
```

Because an odd gamma permutation reverses the ordered gamma product, positive
scalar chirality requires

```text
sum_a t(g,a) = parity(p_g) mod 2.
```

The resulting reference-only system has coefficient rank 138 and augmented
rank 139. This obstruction exists before edge, placement, or preparation
conditions are added.

The full per-frame edge certificate is even more local. Summing all seven
chirality equations accounts for every sign on seven six-gamma roles. The 15
original-edge and six spoke equations account for the same 42 variables once
each. Their XOR cancels every variable and leaves the permutation parity.
Odd frames therefore demand `0=1`.

The full all-frame system has 1,008 variables, 24,906 equations, coefficient
rank 992, and augmented rank 993.

## 4. Stabilizer-equivalent product lift audit

Each transformed reference gamma is allowed an arbitrary multiplier from the
eight-word positive pair-stabilizer group. Multiplier choices depend on frame
and gamma label. The runner imposes identity and exact composition while the
frames permute the three pair axes.

This adds 432 variables and 10,386 equations. The multiplier subsystem is
consistent with rank 414. The combined system remains inconsistent at
`1406/1407` because projection to the logical quotient reproduces the
`992/993` scalar-chirality system.

Thus stabilizer-equivalent product representatives enlarge physical support
and gauge choice but cannot change the logical sign obstruction.

## 5. Cell/role coboundary audit

A vertex sign `q_v` changes an edge sign by the coboundary `q_u+q_v`. The
runner permits independent role coboundaries in every one-frame system. Odd
frames remain `27/28` inconsistent.

The closed reference-spoke graph has `7N` vertices, `21N` edges, and degree
six at every vertex. Summing any vertex coboundary over all edges gives

```text
sum_edges (q_u+q_v) = 6 sum_vertices q_v = 0 mod 2.
```

The same is true for cell-dependent vertex rephasings. Flipping all six gamma
signs at one vertex also leaves chirality unchanged. Therefore neither role
nor cell coboundaries can provide the odd sign required by an odd direction
permutation.

A non-coboundary edge orientation, spin-structure line, or coherent
orientation-character carrier is different structure and remains live. No
marked orientation or root is supplied in this cycle.

## 6. Constructive pseudoscalar repair

Relax only the reference scalar condition:

```text
B_reference -> (-1)^parity(p_g) B_reference.
```

Equivalently, require `sum_a t(g,a)=0` at the fixed reference role. Physical
chirality remains scalar. All original edges and spokes remain positive. The
complete sign system becomes consistent at `992/992` with a 16-dimensional
solution space and exact group law.

Reference-equality checks contain two reference chiralities, so their local
signs cancel. Pair checks remain positive. The remaining failure is the full
closed-code sector:

| `L` | `N=L^3` | odd-frame sign of total reference parity | full loop sector preserved? |
|---:|---:|---:|---:|
| 3 | 27 | negative | no |
| 4 | 64 | positive | yes |
| 5 | 125 | negative | no |
| 6 | 216 | positive | yes |

This route is the strongest constructive result of Cycle 268. It proves the
scalar obstruction can be displaced into a one-dimensional orientation
character. It does not by itself give an all-size physical compiler.

## 7. Placement, rank, sector, and leakage regression

Cycle 268 replays the complete reference-spoke code rather than trusting
metadata:

| `L` | local rank | full rank | physical M2/cell | pair rank | expanded rank | exponent | odd sector? |
|---:|---:|---:|---:|---:|---:|---:|---|
| 3 | 376 | 379 | 24 | 81 | 486 | 162 | yes |
| 4 | 894 | 897 | 24 | 192 | 1152 | 384 | no |
| 5 | 1748 | 1751 | 24 | 375 | 2250 | 750 | yes |
| 6 held out | 3022 | 3025 | 24 | 648 | 3888 | 1296 | no |

The formulas remain `rank_local=14N-2`, `rank_full=14N+1`, and pair-check
rank `3N`. All phase inconsistencies vanish. Maximum expanded local support is
24. At `L=3`, physical-generator/reference-equality leakage and pair-check
phase inconsistencies are both zero.

These regressions show that the covariance result is not caused by a broken
code or abstract-site shortcut.

## 8. Preparation and actual-update firewall

Bounded local loops remain rank three below the full displayed code at every
size. The three Wilson supports are `21,28,35,42` for `L=3,4,5,6`. No bounded
preparation of those Wilson data or arbitrary coherent even/odd input is
constructed.

The local six-M2 pair motif retains a constant route bound 16. This bounded
pair initialization does not prepare the global reference/parity or Wilson
state.

No scalar all-frame common full-Fock `E` exists in the searched grammar. The
runner therefore imports but does not synthesize

```text
beta=-0.3
g=0.37
Cycle-219 rest fixture = 0.4534056541748851
Cycle-230 principal sea rank = 73.
```

Actual coin/A-B FSWAP/contact, leakage, iteration, mass, contact, and rank-73
seam intertwining are not reached and are not called failures.

## 9. Supplied-structure inventory

Cycle 268 supplies or inherits:

1. the Cycle-264 7-mode/cell reference-spoke graph and loop code;
2. the six-M2 radius-24 opposite-pair motif and three positive `ZZ` checks;
3. the 18 physical-mode M2 roles at radii `6,12,18`, for 24 roles/cell total;
4. the period-64 macro origin and constant pair route bound 16;
5. the six local gamma classes, physical chirality, and reference chirality;
6. preservation of the original physical-edge and spoke logical classes;
7. onsite code-preserving Clifford/Pauli-product actions on fixed role blocks;
8. all eight stabilizer-equivalent representatives of every reference Pauli
   class;
9. exact proper-cubic frame permutations and multiplication table;
10. role and arbitrary cell vertex-coboundary interpretation;
11. closed periodic sizes `L=3,4,5,6` and three Wilson constraints;
12. fixed `beta=-0.3`, `g=0.37`, mass, and rank-73 seam fixtures; and
13. exact GF(2), Pauli, phase-aware-rank, coset, and affine arithmetic.

No orientation-character carrier, non-coboundary edge orientation, spin-
structure selection, macro formation, state preparation, measurement,
probability, Record semantics, physical clock, update law, energy, source, or
gravity coupling is derived.

## 10. Prior-art and novelty boundary

Bravyi and Kitaev, *Fermionic quantum computation*, Sec. 8,
arXiv:quant-ph/0003137, and Setia, Bravyi, Mezzacapo, and Whitfield,
*Superfast encodings for fermionic quantum simulation*, arXiv:1810.05274,
establish constructive bounded-degree even-sector encodings with cycle/gauge
structure. They prevent this result from being called a locality no-go.

Chen and Kapustin, arXiv:1807.07081, and Chen, arXiv:1911.00017, exhibit
higher-dimensional local bosonization with explicit spin/topological
structure. Their work is direct prior evidence that an orientation or spin-
structure carrier is ordinary supplied structure, not an axiom-level repair.

Cycle 264 supplies the reference-spoke code, physical placement, diagonal
parity join, and signed-label residual. Cycle 268's new content is limited to:

1. the exhaustive six-M2 pair-code quotient;
2. the forced-gamma-class reduction for general onsite Clifford/product maps;
3. the reference-only `138/139` exact group-law obstruction;
4. the per-frame `27/28` XOR dependency;
5. the `1406/1407` stabilizer-product lift certificate;
6. the degree-six cell/role coboundary parity audit;
7. the constructive pseudoscalar `992/992` repair; and
8. direct all-size physical-code regressions.

No global novelty priority is claimed. No Thirring engine is used or compared.

## 11. TOE dependency ledger after Cycle 268

| Workstream | Cycle-268 effect | Remaining dependency |
|---|---|---|
| `C_ref` | sharpens the missing object to a coherent orientation/sign character at the fixed reference role | derive or physically encode that carrier without a marked orientation, root, or supplied spin sector |
| `C_num` | physical/reference chirality transformation is now exact; scalar and pseudoscalar options are separated | join both matter parities at all sizes while keeping reference chirality scalar overall |
| `C_wrap` | pseudoscalar failure is explicitly the odd-volume total-reference/Wilson sector | bounded preparation or subsystem treatment of spin/Wilson/orientation data |
| `C_int` | gate synthesis remains correctly gated | scalar all-frame common `E`, then actual encoded update and leakage |
| `C_local` | exhaustive onsite Clifford/product/pair-coset/coboundary audit; support and placement regress | changed reference orbit, orientation carrier, or bounded multi-cell Clifford route |
| `C_source` | unchanged | no energy, action, stress, source, or gravity coupling is selected |

Maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.

## 12. No-go discipline N1–N8

The narrow negative is:

> No code-preserving onsite Clifford/Pauli-product action on the fixed Cycle-264
> physical-role blocks and six-M2 reference pair motif, preserving scalar
> chirality and the declared physical-edge/spoke logical classes, implements
> all 24 proper-cubic frames with exact composition.

### N1 — alternative routes

| route | honesty marker | exact disposition |
|---|---|---|
| arbitrary logical symplectic Clifford | **ATTEMPTED** | edge/chirality/spoke data uniquely force all six gamma classes |
| all physical pair-code Pauli representatives | **ATTEMPTED** | 512 centralizer vectors, 64 cosets, eight representatives each |
| stabilizer-equivalent product representatives | **ATTEMPTED** | extended system `1406/1407` |
| independent role coboundaries | **ATTEMPTED** | all twelve odd frames remain `27/28` |
| arbitrary cell vertex rephasings | **ATTEMPTED** | even degree makes total coboundary sign zero |
| pseudoscalar reference chirality | **ATTEMPTED** | constructive `992/992`; odd-volume full-code sector flips |
| scalar even/gauge encodings in general | **RULED OUT BY PRIOR ART as a negative route** | Bravyi-Kitaev, Setia et al., and Chen constructions are positive counterexamples |

Bounded multi-cell Cliffords, changed edge classes, different reference
orbits, non-Pauli maps, non-coboundary spin/orientation lines, and a coherent
orientation-character carrier remain live.

### N2 — condition independence

The remaining conditions are:

- `K_scalar`: scalarize reference chirality;
- `K_sector`: preserve the full loop/parity sector at odd and even volume;
- `K_prep`: prepare orientation, Wilson, and parity data boundedly;
- `K_law`: synthesize the actual update after a common `E`.

The pseudoscalar route closes local covariance without closing `K_scalar` or
`K_sector`. A carrier may close those without preparing Wilson data. These are
independent conditions, not one multiplied impossibility.

### N3 — hidden-condition scan

“General local Clifford” means onsite block-local, code-preserving Clifford
maps on the fixed motifs, not all bounded local unitaries. “Product
representative” means a Pauli in one of the eight explicitly enumerated pair-
stabilizer coset representatives. Scalar versus pseudoscalar chirality is
stated. Geometric frame covariance is not substituted for logical group law.
The periodic boundary, pair checks, macro origin, Wilson sector, parameters,
and preparation absence are explicit.

### N4 — residual matching

| witness | prior residual | Cycle-268 match |
|---|---|---|
| Cycle 264 signed-label `992/993` | general product/Clifford action left live | quotient reduction and all product representatives now audited |
| Cycle 264 six-M2 motif | abstract placement had to remain physical | full placement/rank/support regression passes |
| Cycle 261 signed covariance | physical-only dummy graph admits scalar lift | isolates the new fixed reference role as the changed condition |
| Chen/Kapustin and Chen | spin/orientation structure can be explicit | matches the live orientation-character repair |
| Cycle 230 fixtures | downstream gates/mass/seam | retained behind firewall only |

### N5 — resolution audit

Tested: all 4,096 local pair Paulis, all 64 logical cosets, every gamma label,
all 24 frames, every frame product, all role coboundaries, cell-coboundary
parity, `L=3` direct leakage, and ranks/sectors through held-out `L=6`.

Not tested: multi-cell Clifford depth, changed reference graphs, non-Pauli
automorphisms, non-coboundary orientation fields, open boundaries, or actual
gate synthesis.

### N6 — partial-closure scan

| path | status | possible closure |
|---|---|---|
| coherent orientation-character qubit | priority | multiply pseudoscalar reference chirality into a scalar |
| even reference orbit per cell | untested | cancel the permutation character locally |
| non-coboundary spin/orientation line | untested supplied structure | repair odd sign without a vertex coboundary |
| bounded multi-cell Clifford | outside exhausted scope | may evade onsite tensor-factor rigidity |
| subsystem Wilson/orientation treatment | untested | may preserve predictions without selecting a pure sector |

No axiom edit is indicated.

### N7 — steelman

> The pseudoscalar repair closes the full local group action at `992/992`, so
> the obstruction is one missing orientation character, not failure of local
> fermionization. The pair quotient proves only that this fixed onsite motif
> cannot manufacture that character internally while keeping chirality scalar.
> Adding a coherent orientation carrier, changing the reference orbit, or
> allowing a multi-cell Clifford can leave the searched grammar. Prior
> bosonization results already show spin/topological supply is constructive.

This steelman is convincing and defeats a broad no-go or axiom claim.

### N8 — cross-cycle echo

Earlier sign, charge, and gauge-frame walls were retired by coherent carriers
or changed representations. Cycle 252 retains a coherent topological join;
Cycle 261 closes physical gamma covariance without a fixed reference role;
Cycle 264 supplies the physical reference motif; Cycle 268 identifies its
missing permutation character. Those precedents make an orientation carrier a
normal next compiler move, not constitutional evidence.

N1-N8 supports only the scoped onsite scalar-chirality negative. It rejects a
shared substrate obstruction, minimum-content theorem, or axiom pressure.

## 13. Record and time firewall

Pair stabilizers, Clifford signs, chirality characters, and orientation
carriers are coherent compiler/code data. They are not measurements or
Records.

The frame group is a supplied 3D spatial input. **3D input is not physical
time.** GF(2) elimination, group multiplication, Clifford composition,
stabilizer routing, runner duration, and Wilson preparation depth are compiler
resources. No generator is called a rate; no clock, event, realized history,
probability, energy, or source is derived.

## Route disposition and optimal next campaign

Retain the pair-code quotient, forced-class theorem, `138/139` reference
obstruction, odd-frame XOR certificate, `1406/1407` product-lift result,
coboundary audit, constructive pseudoscalar `992/992` action, and all physical
regressions.

Reject the fixed scalar reference-spoke motif as an all-frame full-Fock
compiler. Do not synthesize Cycle-230 gates in it.

The optimal next campaign is a bounded coherent orientation-character carrier
or an even reference orbit that converts the pseudoscalar repair into scalar
reference chirality while preserving the loop sector at both odd and even
volume. It must be placed in ordinary M2 roles, obey exact all-frame/group-law
and translation tests, retain bounded preparation as a separate demand, and
only then unlock actual `beta=-0.3`, `g=0.37` gate and mass/rank-73 seam
synthesis.

There is no shared obstruction, no axiom pressure, and no axiom conclusion.

## Verification

```text
python3 scripts/general_clifford_reference_spoke_covariance_cycle268_2026_07_17.py
```
