# Non-diagonal reference-cat parity join — Cycle 267

Date: 2026-07-17
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset

## Question and disposition

Can a translation- and proper-cubic-covariant non-diagonal reference code
turn the committed Cycle-261 total-even gamma code into a full-Fock code of
exponent `V=6L^3`, for both odd and even `L^3`, while preserving the local
matter `B/A` algebra and using only bounded, locally enforced constraints and
a bounded arbitrary-input encoder?

Cycle 267 finds a strong but incomplete constructive answer:

1. Cubic `X_iX_j` equality checks give an exact one-logical-qubit reference
   code.  They have rank `N-1` on `N=L^3` cells, exist in both eigenvalue
   sectors of `Z_ref=prod_i Z_i`, are invariant under every translation and
   all 24 proper-cubic frames, and use one ordinary M2 site per cell.
2. The cluster-cat checks `S_ij=K_iK_j`, with
   `K_i=X_i prod_{j~i}Z_j`, give a second exact one-logical-qubit code with
   bounded check support and a bounded logical `X`.
3. Tensoring either code beside the Cycle-261 matter code gives exponent `V`
   only after the three Cycle-261 Wilson sector choices are supplied.  With
   bounded elementary checks alone, the exponent is `V+3`.
4. More decisively, the tensor construction is a **multiplicity**, not a
   parity join.  Cycle-261 matter parity remains fixed to `+1`; no bounded
   relation makes it equal the reference logical `Z`.  The only `Z`-type
   logical representative of the X-cat has support `N`.
5. An independently rebuilt matter-reference **reference-spoke** code does
   make matter parity equal reference parity.  Its full loop rank is
   `14N+1`, both reference-parity sectors exist, and an abstract rank-`N-1`
   pair-flip family would leave exactly exponent `V`.  In the declared local
   three-qubit reference-Pauli grammar, however, every parity-flipping
   endpoint leaks at least one of the six spokes.  A commuting uniform family
   also selects one gamma label and fails 20 of 24 frames; the all-frame
   direction-labelled family has `15N` mutual anticommutators.
6. The exact algebraic cat isometry includes coherent parity superpositions,
   but its nearest-neighbor product-input unitary preparation depth grows with
   `L`.  The lower bounds for `L=3,4,5,6` are `2,3,3,5` layers.  Thus a cat
   with the right rank is kept separate from a bounded physical encoder.

No tested route supplies the required common local encoding `E` or establishes
`E G_coarse = G_physical E`.  The contact and Cycle-230 seam block are not
reproduced in one physical code.  This is a set of route-specific results,
not a general fermionization impossibility result and not axiom pressure.

## Scope and inherited substrate

The runner is
`scripts/nondiagonal_reference_cat_parity_join_cycle267_2026_07_17.py`.
It imports the committed Cycle-261 and Cycle-235 runners.  It does not import
Cycle 264, copy a Cycle-264 rank table, or treat an unreviewed Cycle-264 claim
as authority.

The lawful finite domain is a periodic cubic coarse lattice with `L>=3`.
Cycle 267 evaluates `L=3,4,5`; held-out L=6 is the size-control sample.  All ranks are exact GF(2)
or phase-aware Pauli ranks.  The local gamma chart is

```text
gamma_0 = XII   gamma_1 = YII
gamma_2 = ZXI   gamma_3 = ZYI
gamma_4 = ZZX   gamma_5 = ZZY
```

The committed Cycle-261 degree-six matter code has `V=6N` matter modes,
`3V=18N` physical M2 qubits, bounded elementary-loop rank `2V-2`, and rank
`2V+1` after three Wilson loops are selected.  Its corresponding exponents
are `V+2` and `V-1`.  Total matter parity is already fixed to `+1`.

This distinction is retained throughout:

```text
bounded local Cycle-261 checks + one reference logical: exponent V+3
the same code + three supplied Wilson choices:             exponent V
```

Therefore “exact exponent `V`” below never means that the three topological
sector choices were locally prepared or locally enforced.

## Route 1A — one carrier on every Cycle-261 matter vertex

Put one ordinary carrier qubit `h_v` beside every one of the `V` matter
vertices.  Impose `X_h(u) X_h(v)` on every edge of the degree-six Cycle-261
interaction graph, including its covariant onsite dummy matching.  The graph
is connected and six-regular, so:

```text
carrier qubits                         V
displayed carrier checks              3V
independent carrier-check rank        V-1
reference logical qubits                1
logical Z_ref                         product_v Z_h(v)
```

This route is translation and all-frame covariant because the underlying
degree-six graph and the carrier shell are.  It uses six extra M2 roles per
cell, at radius 24, for 24 M2 roles per cell total.

There are two distinct operator choices:

- Leaving every matter `B_v` and `A_e` unchanged preserves their exact local
  algebra and the cat code, but `product_v B_v=+1` remains fixed.  The new
  qubit is a decoupled multiplicity.
- Defining `B'_v=B_v Z_h(v)` makes `product_v B'_v=Z_ref` and retains the
  formal `B/A` incidence algebra.  Each `B'_v`, however, anticommutes with all
  six carrier checks incident on `v`.  There are exactly `6V` such
  check/operator anticommutators.  `B'_v` is not a codespace-preserving local
  matter observable.

Deleting all six checks incident on one carrier lowers the rank from `V-1`
to `V-2` and creates one extra logical qubit.  This is the leakage/deletion
control rather than a repair.

## Route 1B — one X-cat carrier per coarse cell

Put one reference qubit at each cell center and impose `X_iX_j` on every
nearest-neighbor cubic edge.  The cubic graph is connected, so its incidence
matrix has rank `N-1`.  The stabilizers commute.  The code has logical pair

```text
X_ref = X_i                    for any cell i, modulo checks
Z_ref = product_i Z_i.
```

The two parity-basis codewords are

```text
|0_L> = (|+>^N + |->^N)/sqrt(2)
|1_L> = (|+>^N - |->^N)/sqrt(2).
```

Consequently
`E_cat(alpha|0>+beta|1>)=alpha|0_L>+beta|1_L>` is an exact algebraic
isometry, including coherent parity superpositions.  This is not yet a
bounded preparation circuit.

The decisive centralizer calculation is elementary and exact.  A `Z` mask
commutes with every `X_iX_j` check iff the mask has equal bits at adjacent
vertices.  Connectivity leaves only the zero mask and the all-one mask.
Thus every nontrivial `Z`-type logical has support `N`.  A local `Z_i` leaks
against six checks; trying one at every cell gives `6N` local leakage
incidences.

The cubic torus diameter is `3 floor(L/2)`.  A depth-`d` nearest-neighbor
unitary from a product state can correlate points only within distance `2d`.
The cat therefore obeys

```text
d >= ceil(3 floor(L/2) / 2).
```

This gives `2,3,3,5` at `L=3,4,5,6`.  The code law has no marked endpoint and
does not query global parity, but a bounded arbitrary-input preparation is
not constructed.  Removing the six checks incident on one cell lowers the
rank from `N-1` to `N-2`.

## Route 3 — cluster-cat alternative

For the same cubic graph define

```text
K_i  = X_i product_{j~i} Z_j
S_ij = K_i K_j.
```

All `S_ij` commute, have support at most 12, and span rank `N-1`.  The code is
the bounded-depth cubic-CZ Clifford image of the X-cat code.  It retains
`Z_ref=product_i Z_i` and both `Z_ref` sectors.  Unlike the raw X-cat, it has
a bounded representative `K_i` of logical `X`, of support seven.

This does not localize logical `Z`.  Conjugation by cubic CZ expands the
support of any Pauli by at most seven.  Since the X-cat logical-`Z` coset has
minimum support `N`, the cluster-cat logical-`Z` coset has support at least
`ceil(N/7)`.  A hypothetical constant-depth cluster-cat preparation followed
by the inverse bounded-depth CZ circuit would give a constant-depth X-cat
preparation, contradicting the same light-cone witness.  Deleting all six
edge checks incident on one cell again lowers rank to `N-2`.

## Exact X-cat and cluster-cat size table

Here `k_full` is the combined Cycle-261-plus-reference exponent after the
three Wilson choices; `k_local` uses bounded elementary checks only.

| `L` | `N=L^3` | `V=6N` | cat rank | nonzero X-cat `Z` support | prep-depth lower bound | `k_full` | `k_local` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 162 | 26 | 27 | 2 | 162 | 165 |
| 4 | 64 | 384 | 63 | 64 | 3 | 384 | 387 |
| 5 | 125 | 750 | 124 | 125 | 3 | 750 | 753 |
| 6 held out | 216 | 1296 | 215 | 216 | 5 | 1296 | 1299 |

Both signs of `Z_ref` are phase-consistent at every displayed size, including
odd `N=27,125` and even `N=64,216`.  All 24 proper-cubic frame images and all
coarse translations preserve the cell X-cat edge set exactly.  The cluster
checks inherit the same covariance.

## Route 2 — bounded Majorana matching constraints

The first matching control puts two reference Majoranas in every cell and
uses the covariant onsite bilinear `i a_i b_i`.  The `N` checks commute and
are independent, but they fix every reference mode and hence total reference
parity.  Omitting one onsite check leaves one logical qubit and has bounded
preparation, but marks one cell.  Exactly `N-1` nontrivial translations move
the omitted check.

The intercell bilinear control uses one Majorana channel on cubic edges.
Two bilinears sharing exactly one Majorana anticommute.  There are `15N`
such unordered conflicts.  A commuting subset is a graph matching of size at
most `floor(N/2)`, leaving at least `ceil(N/2)` logical qubits.  A dimerized
choice also supplies a preferred translation/orientation.

Equivalently, a commuting bilinear matching on all `2N` Majoranas either has
`N` pairs and fixes the reference completely, or has `N-1` pairs and leaves
two explicitly unmatched endpoints.  This does not exclude quartic checks,
dressed bilinears, or broader subsystem gauge constructions.

| `L` | `N` | edge-bilinear conflicts | largest edge matching | residual logical lower bound | translation failures after one onsite deletion |
|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 405 | 13 | 14 | 26 |
| 4 | 64 | 960 | 32 | 32 | 63 |
| 5 | 125 | 1875 | 62 | 63 | 124 |
| 6 held out | 216 | 3240 | 108 | 108 | 215 |

## Subsystem steelman — symmetric XX/ZZ edge gauge

As a fifth alternative, take every cubic `XX` edge and every cubic `ZZ` edge
as subsystem gauge generators.  Each incidence span has rank `N-1`, so the
gauge span has rank `2N-2`.  Each `XX` edge anticommutes with the ten `ZZ`
edges sharing exactly one endpoint, for `30N` cross-family
anticommutators.

For odd `N`, the gauge center has rank zero and one logical qubit remains.
For even `N`, both `X_all` and `Z_all` enter the center, whose rank is two,
and zero logical qubits remain.  Thus the construction has the wrong
odd/even-volume behavior: it gives one logical for `L=3,5` and none for
`L=4,6`.  It is a useful exact gauge control, not a candidate commuting
constraint code.

## Stronger reference-spoke construction

The tensor-cat result does not answer the strongest escape because it never
ties matter parity to the new logical `Z`.  Cycle 267 therefore independently
builds a reference-spoke code from committed Cycle 261.

For each cell, retain the six degree-five matter vertices and add one
three-qubit reference gamma register.  Join matter role `d` to the reference
with

```text
A_spoke(c,d) = gamma_d(matter(c,d)) gamma_d(reference(c)).
```

For each of the 12 within-cell matter edges, add the triangle loop formed by
that edge and its two spokes.  Add the committed matter elementary loops and,
only in the full-sector count, the three Wilson loops.  This construction uses
21 ordinary M2 sites per cell.

The exact ranks are:

| `L` | `N` | reference triangles | local rank | full rank | base full exponent | abstract pair rank | counterfactual `k_full` | counterfactual `k_local` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 324 | 376 | 379 | 188 | 26 | 162 | 165 |
| 4 | 64 | 768 | 894 | 897 | 447 | 63 | 384 | 387 |
| 5 | 125 | 1500 | 1748 | 1751 | 874 | 124 | 750 | 753 |
| 6 held out | 216 | 2592 | 3022 | 3025 | 1511 | 215 | 1296 | 1299 |

The product of all matter and reference chiralities is already `+1` in the
full loop code.  Reference parity itself is an independent logical and both
its signs are consistent.  Hence, on this code,

```text
P_matter = P_reference.
```

This is the desired parity relation.  The remaining problem is to remove the
`N-1` auxiliary reference degrees without destroying the spoke/loop algebra.

### Exhaustive local endpoint search

On a three-qubit reference register there are 32 phase-free Pauli vectors
that anticommute with chirality `ZZZ` and therefore flip reference parity.
Exhaustive enumeration gives the number of gamma spokes leaked by one
endpoint:

| leaked spoke labels | number of parity-flipping Paulis |
|---:|---:|
| 1 | 6 |
| 3 | 20 |
| 5 | 6 |

There is no zero-leakage reference-only Pauli endpoint.  This is an exact
centralizer witness in the displayed three-qubit Pauli chart, not a statement
about dressed, quartic, larger-register, or non-Pauli gauges.

### Uniform commuting pair flips

Choose one of the six best endpoint Paulis `P_r=chirality gamma_r`, which
anticommutes with only `gamma_r`, and put `P_r(i)P_r(j)` on every cubic edge.
These checks commute and have rank `N-1`.  They also commute with total
reference parity.  However:

```text
spoke anticommutators             2 per pair check = 6N total
reference-triangle anticommutators 8 per pair check = 24N total
proper-cubic frame failures       20 of 24
```

Only the four frames fixing the selected directed gamma label preserve the
family.  At `L=3`, direct Pauli enumeration gives pair rank 26, zero mutual
pair anticommutators, 162 spoke anticommutators, and 648 loop
anticommutators.

### Direction-labelled all-frame pair flips

For an oriented cubic bond, use `P_d` at its first endpoint and
`P_opposite(d)` at its second.  Proper-cubic frames now permute the complete
family.  At every cell, however, the six incident endpoint Paulis are the six
distinct `P_d`; every pair anticommutes.  The family therefore has exactly
`15N` mutual anticommutators.  Its spoke and triangle leakage remains `6N`
and `24N`.

The uniform family closes commuting rank but loses covariance and loop/spoke
preservation.  The directional family closes covariance but loses commuting
constraints and loop/spoke preservation.  This is the sharpest negative
result of the cycle, and it remains confined to the declared endpoint-Pauli
grammar.

## Placement, covariance, and supplied structure

The tested physical placement uses the committed period-64 macrocells:

- radii 6, 12, and 18: the 18 Cycle-261 matter M2 roles;
- radius 24: six vertex-carrier roles for Route 1A;
- the cell center: the single X-cat or cluster-cat carrier;
- alternatively, three reference-gamma roles for the reference-spoke code.

The four radial shells and center are collision-free modulo 64.  Every shell
is invariant under all 24 proper-cubic frames.  A coarse edge has fixed
period-64 physical diameter, so check support and routing overhead do not grow
with `L`.  The period-64 macro marker and routing synthesis remain supplied;
the calculation does not derive them from a homogeneous M2 law.

The full supplied-structure inventory is:

1. the Cycle-261 square-pyramid matter graph and six-gamma chart;
2. the covariant dummy matching that makes the matter graph degree six;
3. the three Wilson sector choices used in every exact exponent-`V` count;
4. a period-64 macrocell origin, radial role shells, and bounded routing;
5. the initial code state or an encoder for it;
6. the numerical Cycle-230 values `beta=-0.3` and `g=0.37`;
7. the physical sea/vacuum choice and the predecessor one-particle fixture;
8. for cat routes, the choice of parity-basis logical input;
9. for the reference-spoke search, the displayed three-qubit Pauli endpoint
   grammar and inherited Clifford frame action.

No route uses a Jordan-Wigner ordering or a nonlocal parity service in its
displayed constraints.  The exact-rank counts do use the three extensive
Wilson choices, and the cat encoder is not bounded.  Those are explicit
imports, not hidden successes.

## Cycle-230 fixtures and the missing intertwiner

The runner rechecks the untouched matter-side fixtures:

```text
beta                              -0.3
contact coupling g                 0.37
predecessor rest mass              0.4534056541748851
L=3 principal-sea rank             73
```

The local `B/A` algebra remains exact for the undressed tensor routes.  This
preserves the one-particle mass fixture as a predecessor diagnostic; it does
not show that the cat carriers reproduce the free update, contact update, or
Cycle-230 seam block.  There is no common prepared `E`, no encoded
coin/A-B-FSWAP/contact synthesis, and no verified equality
`E G_coarse = G_physical E`.

## Prior-art boundary

- Chen and Kapustin, [*Bosonization in three spatial dimensions and a 2-form
  gauge theory*](https://arxiv.org/abs/1807.07081), construct a locality-
  preserving 3D bosonization with an unusual Gauss law and explicit spin-
  structure dependence.  It is evidence that a broader 2-form gauge route is
  live; it is not the reference-cat or reference-spoke construction tested
  here.
- Setia, Bravyi, Mezzacapo, and Whitfield,
  [*Superfast encodings for fermionic quantum simulation*](https://arxiv.org/abs/1810.05274),
  give bounded-degree graph encodings with local Pauli weight `O(d)` and
  generalized superfast codes.  Cycle 261 is GSE-shaped prior art territory;
  Cycle 267's novelty, if retained, is the exact odd/even-volume reference-cat
  and spoke-compatibility tournament on this specific proper-cubic graph.
- Nys and Carleo,
  [*Quantum circuits for solving local fermion-to-qubit mappings*](https://arxiv.org/abs/2208.07192),
  exhibit local mapped evolution and exact constraint circuits for a 2D
  square lattice.  Their periodic system has additional noncontractible
  constraints, and their vacuum construction applies plaquette circuits
  sequentially with `O(N)` two-qubit gates.  This is a useful preparation and
  Wilson-sector comparator, not a 3D answer for the present code.

No result here uses the Thirring engine.

## Leakage and deletion summary

| route | exact constructive gain | leakage/deletion witness | disposition |
|---|---|---|---|
| vertex X-equality | rank `V-1`, both `Z_ref` sectors, all-frame graph | `B_v Z_h(v)` leaks six checks; deleting one star gives rank `V-2` | right rank, multiplicity or leakage |
| cell X-cat | rank `N-1`, both sectors, all frames/translations | local `Z_i` leaks six checks; deleting one star gives rank `N-2`; growing prep | strongest simple reference code, not a join |
| cluster-cat | rank `N-1`, bounded checks and logical `X` | logical `Z` support `>=ceil(N/7)`; deletion gives rank `N-2`; growing prep | constructive alternative, not a join |
| onsite Majorana | commuting and locally preparable | full matching fixes parity; one deletion marks a cell | rank/prep versus covariance control |
| edge Majorana | bounded even checks | `15N` conflicts; matching leaves extensive residual | route-specific failure |
| XX/ZZ subsystem | symmetric local gauge family | `30N` gauge anticommutators; logical count jumps with volume parity | steelman control |
| uniform spoke pair | commuting rank `N-1` | `6N` spoke, `24N` triangle, 20 frame failures | invalid spoke-code constraint family |
| directional spoke pair | all-frame orbit | `15N` mutual, `6N` spoke, `24N` triangle anticommutators | invalid commuting family |

## No-go discipline audit

### N1 — Alternative-route enumeration

Eight concrete attempts or controls were evaluated: vertex X-equality,
cell X-cat, cluster-cat, onsite Majorana matching, intercell Majorana
matching, symmetric XX/ZZ subsystem gauge, uniform reference-spoke pair
flips, and direction-labelled reference-spoke pair flips.  The first three
construct the requested single reference logical; the spoke construction
constructs the desired parity relation before its pair constraints are
imposed.  Therefore a failure of one route is not being substituted for a
shared substrate obstruction.

### N2 — Wall-independence audit

The residuals are not all independent.  Extensive logical `Z` and growing
cat preparation are two faces of the same long-range cat order.  The three
Wilson degrees are inherited from Cycle 261, not caused by the reference
code.  Multiplicity versus matter-parity identification is independent of
both: it persists even if a cat state and Wilson sector are supplied.  The
reference-spoke Pauli centralizer witness is local and size-independent, but
only within its endpoint grammar.

### N3 — Hidden-wall scan

Hidden or supplied conditions were made explicit: periodic `L>=3`, the
period-64 macro origin, the gamma chart, three Wilson choices, a sea/vacuum,
the parity-basis logical input, product-state/unitary assumptions in the
preparation bound, no measurements or global classical feed-forward, the
three-qubit Pauli endpoint grammar, a Clifford frame action, and bounded
routing between coarse-neighbor roles.  The use of full-rank Wilson rows is
not described as local enforcement.

### N4 — Residual matching

Every scoped negative is paired to an exact witness: X-cat rank `N-1` versus
logical-`Z` support `N`; cluster rank `N-1` versus support lower bound
`ceil(N/7)`; dressed vertex `B` versus six incident anticommutators; onsite
matching rank `N` or marked rank `N-1`; edge matching versus `15N` conflicts;
subsystem gauge versus the odd/even logical-count table; uniform spoke pairs
versus `6N/24N/20`; directional spoke pairs versus `15N/6N/24N`.  The
held-out `L=6` values obey every claimed formula.

### N5 — Rhetoric audit

“Right rank” is not called a physical compiler.  “Abstract isometry” is not
called bounded preparation.  “Counterfactual exponent `V`” is not called a
valid stabilizer code when the added rows anticommute.  The local Pauli
centralizer result is not promoted to a general gauge or bosonization no-go.
The three Wilson rows are not called locally enforced.  No impossibility,
minimum-content, or axiom-necessity claim is made beyond the explicitly
enumerated grammar and preparation model.

### N6 — Partial-closure path scan

Several partial closures are worth retaining.  X-cat closes rank, both
volume parities, covariance, placement, and deletion controls.  Cluster-cat
also supplies a bounded logical `X`.  One-deleted onsite matching closes rank
and local preparation if a marked cell is accepted.  Reference-spoke closes
the matter/reference parity relation and both sectors before auxiliary
reduction.  These pieces suggest concrete next routes instead of a negative
constitutional conclusion.

### N7 — Steelman

The best escape is a dressed or quartic gauge constraint whose matter factor
cancels the endpoint spoke anticommutator while a complete all-frame orbit
remains commuting.  A larger local Clifford register may also have a
parity-flipping centralizer absent from the three-qubit chart.  A 2-form gauge
construction may treat the three Wilson sectors as lawful topological data.
Measurement-assisted, dissipative, or feed-forward cat preparation could
change the unitary product-input bound, but would introduce new physical
operations that must be compiled rather than silently assumed.  None of
these escapes was exhausted here.

### N8 — Cross-cycle echo

Cycle 261 established the exact even-sector gamma code and isolated its three
Wilson sectors.  Cycle 267 shows that adding one logical qubit is easy at the
rank level but insufficient at the operator and preparation levels.  The
independent reference-spoke reconstruction shows that a parity relation can
be obtained without importing Cycle 264, while locating the next local
constraint problem sharply.  Cycle 230's numerical fixtures remain
untouched.  This is unfinished compiler work, not a repeated route-independent
substrate contradiction.

## Six-wall ledger and maturity

| wall | Cycle-267 gain | residual |
|---|---|---|
| `C_ref` | exact covariant X-cat and cluster reference codes; all supplied reference structure inventoried | bounded coherent preparation, Wilson sectors, sea/vacuum, and macro origin remain supplied |
| `C_num` | both parity sectors for odd/even volumes; reference-spoke gives `P_matter=P_reference` before auxiliary reduction | no zero-leakage rank-`N-1` reduction in the tested spoke-Pauli grammar; tensor cats remain multiplicities |
| `C_wrap` | three Wilson logicals remain exactly separated from the parity logical | local/topological sector preparation or lawful subsystem treatment remains open |
| `C_int` | local matter `B/A` algebra and numerical fixture preserved for undressed tensor routes | no common `E`, encoded free/contact/seam update, iteration, or rate/protection result |
| `C_local` | bounded M2 placements, constant overhead, all-frame cell/cluster checks, exact deletion and held-size controls | bounded arbitrary-input encoder and faithful parity join remain open; exact `V` rank still uses Wilson choices |
| `C_source` | unchanged | no energy, action, stress, source, or gravity coupling is selected |

Maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.
Each carrier cat is a coherent code degree, not a Record.  Circuit layers and
preparation depth are compiler resources, not physical time.  No physical
time, realized history, energy, or source interpretation is introduced.

## Next campaign

The highest-value next probe is the local dressed-spoke centralizer problem:

1. enumerate bounded Pauli products on one reference register plus its six
   adjacent matter gamma registers;
2. demand chirality pair flip, commutation with every spoke and elementary
   loop, and a commuting translation/all-frame orbit;
3. compute exact rank, leakage, and frame-group closure at `L=3,4,5`, holding
   out `L=6`;
4. in parallel, test whether a local 2-form/subsystem treatment can absorb
   the three Wilson sectors without selecting extensive rows;
5. only after those close, synthesize the Cycle-230 free-plus-contact update
   in the same prepared code and test the actual intertwiner.

If dressed/quartic Pauli searches fail, the result must remain scoped until a
larger-register and non-Pauli gauge route are also constructively attempted
under the same N1-N8 discipline.  There is no axiom pressure from Cycle 267.
