# Coherent gamma parity-sector doubling — Cycle 264

Date: 2026-07-17
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/coherent_gamma_parity_sector_doubling_cycle264_2026_07_17.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status. It creates only this note and runner.

## Result up front

Cycle 264 constructs and falsifies three concrete ways to supply the one
logical factor missing from Cycle 261's exact degree-six even-sector gamma
code. Several candidates reach the target code exponent `V`, but none supplies
one common full-Fock E satisfying all of locality, both fermion parities,
proper-cubic/coarse-translation covariance, and bounded preparation of an
arbitrary coherent parity superposition.

The important distinction is:

```text
correct code-space exponent V
  != faithful even+odd fermion representation
  != covariant physical placement
  != bounded encoder preparation.
```

The route dispositions are:

| route | exact constructive result | decisive residual |
|---|---|---|
| one direct-sum label | exponent `V`; both parity sectors each exponent `V-1`; local `B_v/A_e` algebra exact | label acts at one marked vertex; 20/24 frame failures, `N-1` translation failures, and global input-parity query |
| distributed Z-equality carrier | exponent `V`; all local dressed `B_v` preserve the code; exact covariance inherited from Cycle 261 | the free carrier bit duplicates the even representation; negative physical parity is phase inconsistent |
| distributed X-equality carrier | exponent `V`; global carrier `Z` is a nontrivial logical parity | every locally dressed `B_v` leaks through the carrier checks; exactly `5V` incidences fail |
| reference-spoke extension with diagonal equality | exact local degree-six CAR; exact exponent `V`; 24 physical M2/cell; both matter parities for odd `N` | for even `N`, `P_m=b^N=+1`; odd matter parity is deleted at `L=4,6` |
| reference-spoke extension with one unfixed root | exact exponent `V` and both parities for every tested size | one coarse cell is marked; `N-1` translation failures |
| aligned/antipodal reference gamma labels | exact bounded algebra and geometric motif covariance | signed-label all-frame systems are inconsistent, ranks `992/993`; general Clifford/product relabelings remain open |

Here `N=L^3` and `V=6N` physical fermionic modes. The held-out L=6 case
replays every failure: it has the right exponent but no odd matter sector in
the covariant diagonal-reference route.

The strongest new constructive object is the reference-spoke code. Add one
reference fermionic mode per coarse cell, join it by six spokes to that cell's
six square-pyramid modes, and use the original physical-physical edges. Every
mode then has degree six. Its exact abstract ranks are

```text
total modes:                         7N
abstract gamma qubits:              21N
bounded loop rank:                  14N - 2
rank after three Wilson loops:      14N + 1
total-even code exponent:            7N - 1.
```

The apparent three-qubit register at a cell center is not called three
physical sites. It is explicitly encoded into six ordinary M2 sites at the
radius-24 `+/-x,+/-y,+/-z` positions, with one local `ZZ` pair code per
opposite axis. The existing Cycle-261 roles occupy radii `6,12,18`, so there
are no collisions. This gives

```text
physical-mode M2 roles/cell:        18
reference M2 roles/cell:             6
total physical M2 roles/cell:       24
local pair-check rank/cell:          3
maximum reference gamma support:     4
maximum expanded bounded loop:      24.
```

All 24 proper-cubic frames preserve the radius-24 shell and its three
unordered opposite pairs. The pair code has exact logical Pauli algebra and
zero gamma/check leakage. Adding the pair checks to the lifted abstract code
preserves the exact exponent `V` through `L=3,4,5,6`.

That geometric success does not repair the logical frame-sign system. Both
the aligned spoke labeling and the only other natural equivariant choice, the
antipodal labeling, give coefficient rank `992` and augmented rank `993` in
the exact 1,008-variable signed-label system. This is a negative only for the
displayed role-dependent signed permutations of six gammas. A more general
local Clifford/product relabeling is not excluded.

For covariant diagonal reference equality, all reference occupations equal a
single bit `b`. The total-even GSE relation is

```text
P_m P_ref = +1,
P_ref = b^N,
therefore P_m = b^N.
```

This gives both matter parities when `N` is odd and only positive matter
parity when `N` is even. The runner extends this beyond nearest-neighbor
equality: any translation-invariant binary diagonal reference code of rank
`N-1` has a one-dimensional invariant kernel. Cell transitivity forces its
nonzero vector to be all ones, so the reference-parity toggle is exactly
`N mod 2`. This statement does not cover non-diagonal quantum reference codes.
In particular, a local even pair-flip/cat reference code can make total
reference parity a logical for even `N` and remains a live route.

Every displayed code also retains three Wilson logicals before the three
noncontractible constraints are imposed. The equality carriers require
system-spanning cat coherence for an arbitrary even/odd superposition. The
nearest-neighbor causal depth lower bound grows from 2 at `L=3` to 5 at
`L=6`. The local opposite-pair encoding is bounded, but it does not prepare
the Wilson or parity-cat data. Code-space rank is therefore not misreported as
bounded preparation.

No candidate meets every compiler condition. The actual Cycle-230
`beta=-0.3`, `g=0.37` coin/A-B FSWAP/contact gates, leakage, one-particle mass,
and rank-73 seam are not synthesized. No downstream gate failure is claimed.

These are route-specific results. There is no shared obstruction, no general
bosonization no-go, no minimum-content conclusion, and no axiom pressure.

## 1. Predecessor and success criterion

Cycle 261's degree-six code places six Clifford gammas on three logical qubits
at every physical mode and fixes all elementary and Wilson loops. With
`V=6N`, it has

```text
physical qubits:       3V
stabilizer rank:       2V + 1
code exponent:         V - 1
physical total parity: +1.
```

Cycle 264 demands an additional coherent logical factor whose two sectors are
the two irreducible physical fermion-parity sectors. A merely free qubit does
not suffice: the product of all encoded occupation parities must act as that
logical bit, every local occupation/edge generator must preserve the code,
and the complete family must be proper-cubic and translation covariant.

The full target remains

```text
E: H_full-Fock -> H_physical-code,
dim H_physical-code = 2^V,
E G_coarse = G_physical E
```

on arbitrary states, including coherent superpositions of even and odd
fermion parity. Bounded/constant M2 overhead and local constraints are
required separately from bounded preparation of `E`.

## 2. Route A — one direct-sum label

Tensor the Cycle-261 even code with one free qubit `h`. Choose one graph vertex
`r=((0,0,0),0)` and replace only

```text
B_r -> B_r Z_h.
```

All edge generators are unchanged. The modified `B_r` still anticommutes with
exactly its five incident physical edges and has support four. On the base
code, the product of the unmodified `B_v` is `+1`, so the new physical total
parity is `Z_h`.

Exact phase-aware results are:

| `L` | `V` | code exponent | positive-sector exponent | negative-sector exponent | local failures |
|---:|---:|---:|---:|---:|---:|
| 3 | 162 | 162 | 161 | 161 | 0 |
| 4 | 384 | 384 | 383 | 383 | 0 |
| 5 | 750 | 750 | 749 | 749 | 0 |
| 6 | 1296 | 1296 | 1295 | 1295 | 0 |

This is the cleanest rank-and-algebra closure in the cycle. It also exposes
why a single copy label is not enough physically. Only four proper-cubic
frames fix the selected direction role; 20 move it. Every nonzero coarse
translation moves the selected cell, giving `N-1` translation failures. A
localized encoder must also set `h` equal to the input's total fermion parity,
which is precisely the forbidden global parity query unless a distributed
coherent mechanism is supplied.

The route is retained as a diagnostic direct sum and rejected as the requested
compiler.

## 3. Route B — distributed equality carriers

Add one ordinary carrier qubit `h_v` at every physical graph vertex, hence six
new M2 roles per coarse cell and 24 total roles/cell. The degree-five physical
graph is connected and proper-cubic/translation covariant.

The runner independently replays the Cycle-261 signed degree-six frame system:
864 variables give equal coefficient/augmented rank `850`, with a
14-dimensional solution family. Permuting the carrier qubits maps every Z- or
X-equality check with positive sign. All 24 frames, the exact group law, and
every coarse translation at `L=3,4,5,6` give zero equality-family failures.
Thus covariance is positively closed for both distributed carrier families;
their residuals below are parity faithfulness and local-code leakage.

### 3.1 Z-equality carrier

Impose every local edge check

```text
Z_(h_u) Z_(h_v) = +1
```

and dress every occupation parity as `B'_v=B_v Z_(h_v)`. The equality checks
have exact rank `V-1`, so adding them to the Cycle-261 even code gives exponent
`V`. Every `B'_v` commutes with every equality check and retains the correct
physical edge incidence.

However, the one logical carrier bit is repeated at all `V=6N` vertices:

```text
product_v B'_v = product_v B_v times product_v Z_(h_v)
               = (+1) times h^V
               = +1.
```

At every tested size, positive physical parity is consistent and negative
physical parity has one phase inconsistency. The two carrier states are two
copies of the same even representation. The exponent is right but the algebra
is not faithful to full Fock space.

### 3.2 X-equality carrier

The complementary checks

```text
X_(h_u) X_(h_v) = +1
```

also have rank `V-1`, and now the global carrier word `product_v Z_(h_v)` is a
nontrivial logical operator for every `V`. This repairs the global parity
functional. But each local factor `Z_(h_v)` anticommutes with every incident
X-equality check. The dressed local occupation operators therefore leak:

| `L` | `V` | exact leaking incidences `5V` |
|---:|---:|---:|
| 3 | 162 | 810 |
| 4 | 384 | 1920 |
| 5 | 750 | 3750 |
| 6 | 1296 | 6480 |

Thus the two Pauli-basis equality attempts expose a precise complementarity:
Z equality preserves each local occupation operator but trivializes global
parity; X equality makes global parity logical but removes the local operators
from the code centralizer.

### 3.3 Invariant scalar-dressing control

The group generated by all proper-cubic frames and coarse translations is
transitive on the `V` physical vertices at every tested size. A scalar logical
label dressed onto a covariant subset of `B_v` can therefore use only the
empty subset or the full orbit. Both have even weight because `V=6N`. No odd
invariant subset exists.

This closes only the grammar “one scalar label multiplied into a covariant
subset of local occupations.” It does not close multi-logical, non-Pauli,
subsystem, or local even pair-flip reference codes.

## 4. Route C — reference-spoke degree-six extension

Add one abstract reference fermionic mode `q_c` per coarse cell. Replace the
Cycle-261 opposite-role dummy matching by six spokes joining `q_c` to the six
physical direction modes in cell `c`:

```text
physical vertex degree: 5 original + 1 spoke = 6
reference vertex degree: 6 spokes
total modes:             7N
total edges:             21N.
```

The physical endpoint of a spoke uses its missing gamma `gamma_d`. The
reference endpoint uses `gamma_d` in the aligned chart. The antipodal chart
uses `gamma_(d xor 1)` and is tested separately for frame signs. Chirality is
occupation parity at every physical and reference mode.

Twelve bounded reference triangles per cell, together with the original
Cycle-235 elementary loops, have exact rank `14N-2`. The three original Wilson
loops raise it to `14N+1`. Direct `L=3` replay gives zero incidence, parity,
loop/edge, loop/loop, and phase failures. Exact ranks persist through the
held-out size:

| `L` | `N` | total modes | edges | local rank | full rank | even exponent |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 189 | 567 | 376 | 379 | 188 |
| 4 | 64 | 448 | 1344 | 894 | 897 | 447 |
| 5 | 125 | 875 | 2625 | 1748 | 1751 | 874 |
| 6 | 216 | 1512 | 4536 | 3022 | 3025 | 1511 |

Maximum abstract bounded-loop support is 24.

## 5. Ordinary-M2 reference placement

The three abstract reference qubits are encoded rather than stacked at one
cell-center site. Use six ordinary M2 sites at radius 24 along the six signed
coordinate directions. Pair opposite sites into three `ZZ` repetition codes.
For axis pair `a`, representatives are

```text
S_a       = Z_(a,+) Z_(a,-),
Xbar_a    = X_(a,+) X_(a,-),
Zbar_a    = Z_(a,+).
```

`Xbar_a,Zbar_a` preserve the pair code and have exact logical Pauli algebra.
A frame that swaps the two sites maps `Zbar_a` to the equivalent representative
`Zbar_a S_a`; therefore no sign or oriented endpoint is selected on code
space. The three logical gamma operators expand to maximum support four and
commute with all pair checks.

The runner checks:

```text
local pair rank:                         3
pair/gamma leakage:                      0
logical Pauli failures:                  0
gamma anticommutator failures:           0
collisions with radii 6,12,18:           0
proper-frame shell failures:             0
proper-frame pair failures:              0
periodic opposite-pair distance:         16
maximum expanded local loop support:     24.
```

Lifting every abstract stabilizer and adding `3N` pair checks gives 24 physical
M2 roles/cell and exact code exponent `V` after reference equality:

| `L` | physical M2/cell | pair-check rank | total rank | code exponent |
|---:|---:|---:|---:|---:|
| 3 | 24 | 81 | 486 | 162 |
| 4 | 24 | 192 | 1152 | 384 |
| 5 | 24 | 375 | 2250 | 750 |
| 6 | 24 | 648 | 3888 | 1296 |

A bounded-radius pair encoder initializes each opposite pair. The two endpoints
have periodic separation 16, so a nearest-neighbor compilation uses a supplied
constant route of length at most 16 inside the period-64 macrocell; no
nearest-neighbor single-CNOT claim is made. Its Pauli check support is two and
its routing depth is constant in `L`. This prepares only the local pair code,
not the reference cat or Wilson data.

## 6. Reference occupation constraints and volume parity

Impose covariant nearest-neighbor equality on reference chirality:

```text
B_(q_c) B_(q_(c+axis)) = +1.
```

These checks are bounded, have exact rank `N-1`, commute with all loop
stabilizers, and commute with every physical-mode occupation and original
physical edge generator. Adding them gives exact exponent `V`.

The full reference-spoke loop code fixes total physical-plus-reference parity:
`P_m P_ref=+1`. Equality leaves one bit `b`, hence `P_ref=b^N` and
`P_m=b^N`. Exact phase-aware sector data are:

| `L` | `N` | exponent | positive matter parity | negative matter parity |
|---:|---:|---:|---|---|
| 3 | 27 | 162 | consistent, rank +1 | consistent, rank +1 |
| 4 | 64 | 384 | already fixed | phase inconsistent |
| 5 | 125 | 750 | consistent, rank +1 | consistent, rank +1 |
| 6 | 216 | 1296 | already fixed | phase inconsistent |

This is an exact volume-parity law, not a numerical trend.

The runner also audits every translation-invariant binary **diagonal**
reference constraint code of rank `N-1`. Its one-dimensional kernel must be
fixed by translations; cell transitivity makes the nonzero kernel vector all
ones. Total reference parity changes by its weight `N mod 2`. Consequently a
different local stencil or affine presentation in the same diagonal grammar
does not repair even `N`.

Fixing `B_(q_c)=+1` at every cell except one root does repair both matter
parities for every `L`, with exponent `V`. It also produces exactly `N-1`
translation failures. This is the reference-mode counterpart of Route A and
is retained only as a control.

Non-diagonal quantum reference constraints remain live. In particular,
bounded even pair-flip terms can make total reference parity a logical on an
even lattice; their mutual algebra, gamma-code centralizer, covariance, and
preparation were not constructed here.

## 7. Frame-sign audit for the reference extension

Geometric preservation of the radius-24 motif does not prove covariance of
the logical gamma and edge operators. The runner therefore repeats Cycle
261's affine sign audit with seven source roles: six physical direction roles
and one reference role.

For both aligned and antipodal spoke labels, 1,008 binary sign variables allow
dependence on frame, source role, and gamma label. The 24,906 equations impose:

1. identity signs;
2. exact signed groupoid composition and group law;
3. positive chirality at every physical and reference role;
4. positive transformation of all original physical edges; and
5. positive transformation of all six reference spokes.

Both systems give

```text
coefficient rank: 992
augmented rank:   993
odd raw gamma permutations: 12.
```

Thus neither displayed signed-label chart has the required all-frame operator
action. This does not contradict Cycle 261: the new reference role couples all
six missing labels to one additional chirality and adds sign conditions absent
from the opposite-role dummy matching.

The conclusion is deliberately narrow. A general local Clifford that maps a
gamma to a product representative, a different reference bundle, position-
dependent gauge coboundaries, or a non-Pauli reference code is not exhausted.
The reference-spoke route is therefore not called an all-frame physical
compiler, despite its successful geometric placement.

## 8. Preparation and Wilson/subsystem audit

Both the Cycle-261 base code and the reference-spoke code have bounded local
loop rank three below their displayed full rank. Adding the three
noncontractible Wilson constraints increases rank by exactly three at every
tested size. No bounded local preparation of those topological data is
constructed.

The Z-equality and diagonal reference-equality logical bases require a cat
state for a coherent parity superposition. On the coarse three-torus the
Manhattan diameter and the conservative disjoint-lightcone depth lower bound
are:

| `L` | torus diameter | local causal-depth lower bound |
|---:|---:|---:|
| 3 | 3 | 2 |
| 4 | 6 | 3 |
| 5 | 6 | 3 |
| 6 | 9 | 5 |

This lower bound is scoped to bounded-range unitary encoding from a localized
input parity qubit and product carrier ancillas. It establishes that the
displayed equality fanout is not constant-depth bounded preparation. It is not
a theorem against measurement-assisted, dissipative, pre-entangled-resource,
pair-flip, subsystem, or other encoders.

For an arbitrary full-Fock input `alpha|even>+beta|odd>`, no route here both
extracts the sector coherently without a global parity query and prepares all
carrier/Wilson data in bounded depth. A rank equality is not used as an
encoder circuit.

## 9. Deletion, leakage, and lawful-domain controls

The lawful tested domain is the closed periodic square-pyramid cellulation at
`L=3,4,5,6`; L=6 is held out from construction.

Controls include:

- deleting the direct label returns the exact Cycle-261 exponent `V-1`;
- moving the marked vertex under 20 frames and every nonzero translation
  exposes the direct route's symmetry dependence;
- swapping Z equality to X equality turns the global parity on while producing
  exactly `5V` local occupation/check anticommutators;
- the all-frame/translation orbit audit excludes an invariant odd scalar-
  dressing subset;
- adding reference equality gives rank `N-1` with zero physical-generator
  leakage;
- even versus odd volumes isolate the exact `b^N` functional;
- fixing all references except one restores both parities and exposes the
  marked root;
- aligned versus antipodal spoke labels both replay the exact signed-lift
  inconsistency;
- expanding each abstract reference register into six physical M2 sites
  preserves ranks, phases, support, and parity results; and
- removing the three Wilson loops lowers rank by exactly three in both gamma
  graphs.

No open boundary, non-diagonal reference code, general Clifford/product
relabeling, measurement-assisted preparation, or thermodynamic extrapolation
is silently included.

## 10. Actual-update and fixture firewall

The required chain remains

```text
one common full-Fock E
  -> bounded preparation on arbitrary parity superpositions
  -> actual Cycle-230 coin / A-B FSWAP / contact
  -> prove E G_coarse = G_physical E
  -> leakage, one-particle mass, contact, and rank-73 seam replay.
```

No route closes the first two steps simultaneously. The runner checks only the
retained predecessor fixtures:

```text
beta=-0.3
g=0.37
Cycle-219 rest fixture = 0.4534056541748851
Cycle-230 principal sea rank = 73.
```

The actual gate matrices are not synthesized in these candidate codes. The
coin/A-B FSWAP/contact update, its leakage, iteration, one-particle mass,
contact block, and rank-73 seam are neither reproduced nor falsified.

## 11. Supplied-structure inventory

Cycle 264 supplies or inherits:

1. the Cycle-261 degree-six gamma algebra, opposite-pair even code, signed
   frame action, 18-role physical placement, and three Wilson cycles;
2. closed periodic sizes `L=3,4,5,6` and supplied period-64 macro origins;
3. one marked free label and one marked physical vertex in Route A;
4. one carrier M2 at every physical vertex and all degree-five graph equality
   edges in Route B;
5. one abstract reference fermion mode per cell and six physical-reference
   spokes in Route C;
6. twelve reference triangles per cell and the original elementary/Wilson
   cycles;
7. six radius-24 physical reference sites per cell and three local opposite-
   axis `ZZ` pair checks;
8. the aligned and antipodal reference gamma labelings;
9. nearest-neighbor diagonal reference equality or, in the deletion control,
   a selected root and `N-1` fixed occupations;
10. exact Pauli, phase-aware rank, affine GF(2), group-orbit, support, and
    physical-expansion arithmetic;
11. bounded-range unitary/product-ancilla assumptions for the displayed cat
    preparation lower bound;
12. fixed `beta=-0.3`, `g=0.37`, predecessor mass, and sea-rank fixtures; and
13. classical computation and memory sufficient to execute the certificate.

No macro-marker formation, state preparation, measurement, probability,
Record semantics, physical clock, parameter-selection law, update law,
energy, stress, source, or gravity coupling is derived.

## 12. Prior-art and novelty boundary

Bravyi and Kitaev, *Fermionic quantum computation*, Sec. 8,
arXiv:quant-ph/0003137; *Annals of Physics* **298** (2002), gives constant-cost
bounded-degree simulation of local even fermionic operations with edge qubits
and cycle constraints, with even-sector scope and preparation treated
separately.

Setia, Bravyi, Mezzacapo, and Whitfield, *Superfast encodings for fermionic
quantum simulation*, arXiv:1810.05274; *Physical Review Research* **1**,
033033 (2019), is the direct generalized-superfast comparator. It supports the
constructive even-sector/gamma route. It does not supply the coherent
full-Fock parity join or bounded preparation demanded here.

Chen and Kapustin, arXiv:1807.07081, and Chen, arXiv:1911.00017, give
locality-preserving bosonization constructions in three and arbitrary spatial
dimensions with explicit spin/topological-structure dependence. They are
prior evidence that local even/gauge encodings exist and that topological
sector supply is known structure. They are not imported as a full-Fock sector
join or a bounded encoder for this fixture.

Cycle 252 supplies a repository-local coherent even/odd sector join with
nonlocal Wilson/parity preparation but without the ordinary-M2 incident CAR
image. Cycle 261 supplies the exact ordinary-M2 local gamma algebra and
even-sector code. Cycle 264 tests three concrete attempts to combine those
virtues.

Cycle 264's fixture-specific new content is limited to:

1. exact marked-label rank/parity closure and covariance failure counts;
2. exact Z/X distributed-carrier rank, parity, and local-leakage complement;
3. the transitive-orbit scalar-dressing control;
4. the 7-mode/cell reference-spoke graph and ranks `14N-2,14N+1`;
5. the six-site opposite-axis physical reference motif and lifted 24-M2/cell
   rank certificate;
6. the exact `P_m=b^N` volume-parity law and its diagonal rank-`N-1`
   generalization;
7. the aligned/antipodal signed-label inconsistencies `992/993`; and
8. the explicit Wilson/cat preparation separation and held-out replay.

No global novelty priority is claimed. No Thirring engine is used, extended,
or compared.

## 13. TOE dependency ledger after Cycle 264

| Workstream | Cycle-264 effect | Remaining dependency |
|---|---|---|
| `C_ref` | reference supply is now explicit: marked root, distributed equality bit, or reference-mode field; no option is hidden | remove root/global parity query and prepare a covariant quantum reference logical without supplied cat/Wilson data |
| `C_num` | strong diagnostic gain: multiple exact exponent-`V` codes and explicit matter-parity action; reference volume law isolated | one faithful even+odd local occupation algebra at every size with zero leakage |
| `C_wrap` | both gamma graphs leave exactly three Wilson logicals; their role is separated from parity doubling | bounded preparation or lawful subsystem treatment of Wilson/spin-structure data |
| `C_int` | actual gate synthesis remains correctly gated; no false mass/contact claim | one common prepared `E`, then encoded coin/A-B FSWAP/contact, leakage, and iteration |
| `C_local` | gain: 24-M2/cell collision-free reference motif, support <=24, all-frame geometry, exact ranks/translations | repair reference signed-frame action and parity join simultaneously; bounded parity-cat preparation |
| `C_source` | unchanged | no energy, action, stress, source, or gravity coupling is selected |

Maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.
The cycle sharpens the quantum compiler dependency but does not yet deliver a
new cross-lane physical prediction.

## 14. No-go discipline N1–N8

The narrow route-specific negatives are:

> A single direct-sum parity label attached to one occupation operator is not
> proper-cubic/translation covariant.

> The displayed Z/X equality-carrier Pauli grammars cannot simultaneously make
> global physical parity logical and keep every local dressed occupation in
> the code centralizer.

> A translation-invariant rank-`N-1` diagonal reference-occupation code has
> parity toggle `N mod 2`.

> The aligned and antipodal reference-spoke signed-label charts have no exact
> positive all-frame lift in the declared affine system.

None is a theorem against non-diagonal pair-flip codes or general Clifford
reference bundles.

### N1 — alternative routes

| route | honesty marker | exact disposition |
|---|---|---|
| one free direct-sum label | **ATTEMPTED** | exact exponent/both parities; marked vertex and global query |
| distributed Z-equality carrier | **ATTEMPTED** | exact exponent/local centralizer; negative parity absent |
| distributed X-equality carrier | **ATTEMPTED** | global parity logical; exactly `5V` local leaks |
| invariant scalar dressing on another vertex subset | **ATTEMPTED** | full space-group orbit is transitive and even |
| aligned reference-spoke extension | **ATTEMPTED** | exact bounded code/rank; signed-label lift inconsistent |
| antipodal reference-spoke labels | **ATTEMPTED** | same exact affine inconsistency |
| covariant diagonal reference equality | **ATTEMPTED** | exact exponent; both parities only for odd `N` |
| fix all reference modes except one | **ATTEMPTED** | both parities all sizes; marked root |
| six-site opposite-axis pair-code placement | **ATTEMPTED** | exact physical placement and local pair preparation; logical route residuals remain |
| bounded local even-sector simulation | **RULED OUT BY PRIOR ART as a negative route** | Bravyi-Kitaev, Setia et al., and Chen constructions block a universal locality no-go |

Local even pair-flip/cat reference constraints, a general Clifford/product
reference action, a Cycle-252-style topological coherent carrier, subsystem
Wilson treatment, and open boundaries remain live.

### N2 — condition independence

The routes fail different conditions and are not accumulated into a shared
obstruction:

- `K_parity`: both physical fermion-parity sectors at every size;
- `K_cov`: positive all-frame and translation action without a root;
- `K_centralizer`: every local encoded occupation/update preserves the code;
- `K_prep`: bounded encoder for arbitrary coherent parity superpositions and
  Wilson data;
- `K_law`: actual update/parameter realization after one common `E`.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---:|
| `K_parity`,`K_cov` | no; marked routes show this | no | yes |
| `K_parity`,`K_centralizer` | no; X equality shows this | no; Z equality shows this | yes |
| `K_parity`,`K_prep` | no | no | yes |
| `K_cov`,`K_prep` | no | no | yes |
| `K_centralizer`,`K_prep` | no | no | yes |
| `K_law`, each compiler condition | downstream only | no | yes |

Actual Cycle-230 gate synthesis is downstream of a common prepared `E` and is
not counted as an independent negative.

### N3 — hidden-condition scan

“Full-Fock exponent,” “both parity sectors,” “local,” “bounded,” “covariant,”
“physical M2,” “reference mode,” and “preparation” have separate executable
definitions. Twenty-one abstract gamma qubits per cell are not called physical
M2; the six-site pair expansion is required before the 24-M2/cell claim.
Geometric shell covariance is not substituted for the signed logical frame
action. Rank equality is not substituted for a preparation circuit.

The periodic boundary, Wilson loops, period-64 macrocell, roots, carrier basis,
reference equality basis, pair-code checks, fixed parameters, and causal-
circuit assumptions are explicit. No “by construction,” “standard QFT,”
“naturally,” “obviously,” measurement, Born, Record, energy, source, or rate
import bears a narrow negative.

### N4 — residual matching

| witness | prior residual | Cycle-264 match |
|---|---|---|
| `COVARIANT_VERTEX_GAMMA_CAR_COMPILER_CYCLE261_NOTE_2026-07-17.md` | exact degree-six even code lacks one parity factor | direct target of all three routes |
| Cycle 261 frame section | signed operator action must be audited beyond symplectic relabeling | repeated with seven source roles and two spoke labelings |
| `COHERENT_EVEN_ODD_SECTOR_JOIN_CYCLE252_NOTE_2026-07-17.md` | coherent sector join exists with Wilson/preparation supply | keeps coherent/topological carrier live; prevents rank-only claims |
| Bravyi-Kitaev and Setia et al. | local even-sector encodings are constructive | matches predecessor/reference even codes and blocks a broad negative |
| Chen/Kapustin and Chen | local higher-dimensional bosonization carries spin/topological structure | identifies Wilson/reference supply as prior-art structure, not new axioms |
| Cycle 230 gate/seam fixture | actual update and rank-73 target | retained behind the common-`E` firewall only |

Every narrow residual is replayed in Cycle 264 itself.

### N5 — resolution audit

| resolution | tested | not established |
|---|---|---|
| direct label | every `L=3..6` rank/sector and all root motions | root-free distributed encoders |
| distributed Pauli carrier | both Z and X equality bases, all local incidences | general stabilizer/non-Pauli carrier codes |
| scalar subset | full proper-cubic/translation orbits | multi-logical/projective actions |
| reference graph | every edge/loop at `L=3`, exact ranks through `L=6` | arbitrary reference graphs |
| reference constraints | nearest-neighbor equality and every rank-`N-1` diagonal invariant kernel | non-diagonal even pair-flip codes |
| frame action | aligned/antipodal signed gamma permutations | general Clifford/product representatives |
| physical placement | all 24 frames, collisions, pair rank, leakage, expanded ranks | emergent rather than supplied macro roles |
| preparation | bounded-range unitary/product-ancilla equality fanout | measurements, dissipation, pre-entanglement, subsystem encoders |
| actual update | not reached | gate/mass/contact/seam failure is not claimed |

The negatives are stated only at the resolutions actually exhausted.

### N6 — partial-closure scan

No axiom edit is indicated. Live constructive paths are:

| path | status | possible closure |
|---|---|---|
| local even pair-flip/cat reference code | priority untested route | can make total reference parity logical for even `N`, unlike diagonal equality |
| general Clifford/product reference relabeling | untested | may repair the `992/993` signed-label inconsistency |
| combine Cycle-252 coherent topological carrier with Cycle-261 gamma algebra | untested synthesis | may join parity without a scalar root dressing |
| subsystem treatment of three Wilson logicals | untested | may avoid nonlocal stabilizer selection |
| measurement-assisted/dissipative reference preparation | outside current unitary grammar | may prepare cat/topological data without constant-depth unitary fanout |
| open boundary/reference sink | target change | may allow an unpaired reference without a periodic marked root |

These are compiler, boundary, and state-preparation routes, not demands for new
axioms.

### N7 — steelman

> A hostile reviewer should reject any universal parity-join obstruction. The
> marked label already proves that the local algebra and Hilbert dimension need
> only one coherent factor. The reference-spoke graph gives a fully bounded
> degree-six code and an explicit collision-free 24-M2/cell placement. Its
> diagonal equality failure is the elementary identity `b^N`, not a theorem
> against quantum reference codes. An even pair-flip/cat code can make total
> reference parity logical on even `N`, and a general Clifford/product
> relabeling can leave the failed signed-permutation chart. Cycle 252 already
> shows a coherent even/odd topological join, while Bravyi-Kitaev, Setia et al.,
> and Chen-type bosonizations show local even/gauge encodings are ordinary
> constructive physics. The remaining preparation and spin/Wilson data are
> real supplied structures, but none forces a new axiom.

This steelman is convincing. The broad no-go fails. Only the four narrow
grammar-specific statements above survive.

### N8 — cross-cycle echo

| earlier boundary | retirement/live mechanism | Cycle-264 response |
|---|---|---|
| Cycle 244 classical sign | coherent sign carrier | keeps pair-flip/general Clifford routes live |
| Cycle 245 marked charge | distribute/coherently orbit the reference | root controls are not accepted as final encoders |
| Cycle 249 gauge-frame choice | coherent conjugation | separates geometric motif from signed operator action |
| Cycle 251 rough multiplicity | operational subsystem | keeps Wilson logicals as a subsystem option |
| Cycle 252 coherent parity join | quantum topological carrier | direct candidate for combining with the gamma algebra |
| Cycle 261 even-sector gamma code | one missing logical factor | Cycle 264 exhausts three concrete factor-supply grammars |
| higher-dimensional bosonization prior art | explicit spin/topological input | prevents topological supply from being mislabeled an impossibility |

Prior walls were retired by coherent enlargement, gauge/subsystem treatment,
or a changed code. Those mechanisms remain live. N1-N8 therefore rejects a
shared obstruction, minimum-content result, or axiom pressure.

## 15. Record and time firewall

The direct label, distributed carriers, reference modes, and opposite-pair
qubits are coherent code degrees of freedom. They are not measured,
actualized, permanent, or decoded as Records. A copied carrier value is not a
Record.

GF(2) rank, Clifford/gamma relabeling, CNOT pair initialization, equality
fanout, stabilizer layers, Wilson selection, causal-depth lower bounds, and
runner duration are compiler resources. **Compiler layers are not physical
time.** No generator element is called a rate, and no clock, duration, event,
realized history, probability, energy, or source is derived.

## Route disposition and optimal next campaign

Retain the marked-label exact rank/parity control, distributed Z/X
complementarity, transitive-orbit result, reference-spoke graph, physical
six-site reference motif, exact volume-parity law, aligned/antipodal affine
certificates, Wilson/preparation separation, and fixture firewall.

Reject all three displayed routes as one common full-Fock physical compiler.
Do not synthesize the Cycle-230 gates in them.

The optimal next campaign is a non-diagonal local reference-code tournament on
the physical reference-spoke substrate. Construct bounded even pair-flip/cat
constraints whose logical `Z` is total reference parity for both even and odd
`N`; demand commutation with the gamma loop code and every physical `B_v/A_e`;
solve the most general bounded Clifford/product frame action rather than only
signed gamma permutations; then audit all translations, three Wilson
logicals/subsystem alternatives, and an explicit encoder for arbitrary
coherent parity input. Only if that produces one common prepared `E` should
the actual `beta=-0.3`, `g=0.37` coin/A-B FSWAP/contact and mass/rank-73 seam
be synthesized.

There is no shared obstruction, no axiom pressure, and no axiom conclusion.

## Verification

```text
python3 scripts/coherent_gamma_parity_sector_doubling_cycle264_2026_07_17.py
```
