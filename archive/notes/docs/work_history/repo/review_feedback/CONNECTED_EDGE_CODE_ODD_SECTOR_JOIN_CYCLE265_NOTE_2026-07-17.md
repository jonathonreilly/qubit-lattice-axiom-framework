# Connected edge-code odd-sector join — Cycle 265

**Date:** 2026-07-17

**Type:** complete connected-graph constructive rank closure with an exact
parity-functional and preparation failure

**Status:** bounded connected even-CAR algebra retained; the tested unmarked
distributed field does not furnish a bounded-preparable full-Fock `E`

**Authority: none**

**Audit: unset**

**Constitutional effect: none**

Companion runner:

```text
scripts/connected_edge_code_odd_sector_join_cycle265_2026_07_17.py
```

This cycle creates only this note and runner. It changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface.

## Result up front

Cycle 265 runs the odd-sector join on the **complete degree-five graph** of all
`6L^3` Cycle-230 matter modes. It does not tensor isolated alternating-cycle
codes and it does not splice Cycle 263's prefix state map into edge-code
gates.

The retained connected substrate is the Cycle-235 square-pyramid edge code:
one ordinary `M_2` factor on each of `15N` primal faces, where `N=L^3`. Its
bounded generators are

```text
B_v = product_(e incident v) Z_e,                       weight 5,
A_uv = epsilon_uv X_(uv) times bounded incident Z dress, weight <= 9.
```

The graph has `V=6N`, `E=15N`, degree five, local elementary cycle-check rank
`9N-2`, and full cycle rank `9N+1`. Three torus Wilsons complete the local
cycle checks. The resulting edge code has exponent `6N-1`, exactly the total-
even connected matter sector.

The new attempt adds **one cell-center M2** `R_c` per coarse cell and the
proper-cubic, coarse-translation-invariant local equalities

```text
D_(c,a) = Z_(R_c) Z_(R_(c+e_a)) = +1,    a=x,y,z.
```

Their rank on the periodic connected cell graph is `N-1`. Therefore the
literal physical count closes:

```text
physical M2:       15N + N = 16N,
constraint rank:   (9N+1) + (N-1) = 10N,
code exponent:     16N - 10N = 6N = 6L^3.
```

That is a genuine constructive improvement over the raw total-even code, but
it is not yet a full-Fock compiler. The extra exponent can be a multiplicity
qubit rather than the missing odd sector. The decisive discriminator is the
exact image of total matter parity, not dimension alone.

Two local dressings expose the issue.

1. The genuinely unmarked all-six dressing uses
   `Bhat_(c,d)=B_(c,d) Z_(R_c)` for all six direction roles. It is covariant
   under all 24 proper-cubic frames and coarse translations, but

   ```text
   product_(c,d) Bhat_(c,d) = product_c Z_(R_c)^6 = I.
   ```

   Thus it remains a total-even matter representation with one multiplicity
   qubit. It has exponent `6N`, but the matter algebra has only the
   `12N-2` noncentral Pauli directions of one parity sector.

2. The one-port dressing multiplies one selected direction parity per cell by
   `Z_(R_c)`. On the equality code all `Z_(R_c)` have a common eigenvalue
   `b`, so its exact total-parity functional is

   ```text
   P_m = product_v Bhat_v = product_c Z_(R_c) = b^N.
   ```

   It supplies both parity blocks when `N` is odd, but fixes `P_m=+1` when
   `N` is even. Hence `L=4` and held-out `L=6` lose the one-particle and every
   other odd state. Moreover, a fixed selected port is a direction marker.
   Its proper-cubic orbit contains all six ports.

There is no third invariant odd port subset hidden between those choices.
The runner enumerates all 64 subsets of the six direction roles under the 24
proper rotations. The only invariant subsets are the empty set and all six;
both have even cardinality. An odd subset can give `P_m=b^N`, but no fixed odd
subset is unmarked.

The field also fails bounded preparation in this grammar. Switching its
logical branch while preserving every local `Z` equality requires
`product_c X_(R_c)`, of exact weight `N`; a single local `X` violates six
equalities and a nearest-neighbor pair violates ten. Equivalently, mapping a
vacuum and a state differing by one local occupation to branches `b=+1` and
`b=-1` changes a local field observable at every distant cell. A bounded-
radius encoder from product auxiliary inputs cannot do that. Choosing coherent
`CAT+/-` branches moves the problem to long-range connected correlations and
still does not give a bounded product-input preparation circuit.

The edge code separately retains three selected torus holonomies. Their `X`
support is `3L`, and the actual framed Pauli weights grow as `6L+3` in the
largest direction. That selected Wilson/spin sector is supplied global
preparation, not a local check closure.

Therefore Cycle 265 constructs an exact, covariant, constant-overhead
**rank-matched connected code**, and it proves that the tested scalar
`Z`-equality join mistakes a multiplicity qubit for odd matter. It does not
prove that every distributed reference code fails. X/cat-like reference
codes, local even pair-flip constraint grammars, non-Pauli subsystem codes,
measurement/reset, pre-entangled resources, and open boundaries remain live.

There is no shared obstruction and no axiom pressure.

## 1. Exact connected cellulation and rank census

Every coarse cube is subdivided into its six face pyramids. The pyramid
adjacency graph contains the 12 onsite nonopposite-direction edges and three
shared stream edges per cell. It is connected and degree five. Qubits on its
edges are physical face `M_2` factors.

The local elementary cycle checks are the complete primal-edge family:

- `8N` triangular loops around center-to-corner spokes;
- `3N` octagonal loops around coarse cubic edges; and
- rank `9N-2` after their local dependencies.

Three noncontractible torus Wilson constraints raise the rank to `9N+1`.
Adding the `3N` redundant-but-covariant cell-field equalities raises the rank
by `N-1`. Actual phase-aware Pauli elimination finds no `-I` dependency.

| `L` | `N` | physical `M_2` | local edge-cycle rank | edge rank after 3 Wilsons | field equality rank | total rank | code exponent |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 432 | 241 | 244 | 26 | 270 | 162 |
| 4 | 64 | 1024 | 574 | 577 | 63 | 640 | 384 |
| 5 | 125 | 2000 | 1123 | 1126 | 124 | 1250 | 750 |
| 6 held out | 216 | 3456 | 1942 | 1945 | 215 | 2160 | 1296 |

The exponent is exactly `6L^3` at every size. The total-parity functional is:

| `L` | `N` parity | unmarked all-six | one selected port |
|---:|---:|---|---|
| 3 | odd | `P_m=I` | `P_m=b`, both blocks algebraically present |
| 4 | even | `P_m=I` | `P_m=b^64=I`, odd absent |
| 5 | odd | `P_m=I` | `P_m=b`, both blocks algebraically present |
| 6 held out | even | `P_m=I` | `P_m=b^216=I`, odd absent |

For the unmarked branch, adjoining the mapped `B/A` family to the stabilizers
adds `12N-2` independent logical Pauli directions. For the selected-port
branch it adds `12N-1` at odd `N` and `12N-2` at even `N`. This directly
distinguishes faithful two-parity even algebra from a same-dimension code with
one multiplicity qubit.

## 2. Bounded connected even-CAR update

The field dress is diagonal, so it does not change the local incidence table.
Every `A_uv` anticommutes with precisely `Bhat_u,Bhat_v`. Two `A` generators
anticommute exactly when their graph edges share one endpoint. The runner
checks the complete L=3 table, including phases inherited from the bounded
incident-edge order gauge.

The actual two-mode fermionic swap is still the exact polynomial

```text
FSWAP_uv = (Bhat_u + Bhat_v + i Bhat_u A_uv - i Bhat_v A_uv)/2.
```

Its `4 x 4` matrix residual is zero, and every physical Pauli term has bounded
support independent of `L`. The cell field adds at most the two endpoint cell
centers. Cell parity has weight at most six above the face dressing, modified
Gauss checks retain their Cycle-235 bound, and an onsite six-mode even algebra
fits inside the 18 incident face carriers plus its one cell-center carrier.

This is a connected-algebra result. It does not import the Cycle-263 prefix
encoder. In particular, no state is encoded by one representation and then
updated by another. It uses no global Jordan-Wigner ordering and no nonlocal
parity-query service. The incident-edge order is a bounded local presentation
gauge with the explicit Clifford covariance repair, not a global Fock order.

## 3. Total parity, per-cycle parity, and onsite coin transfers

The isolated alternating-cycle comparator remains useful only as a control.
The Cycle-230 A/B matchings partition `6L^3` modes into `3L^2` cycles of length
`2L`. Fixing each isolated edge code even would leave exponent

```text
6L^3 - 3L^2,
```

whereas the complete connected edge code's total-even sector has exponent

```text
6L^3 - 1.
```

The isolated tensor product therefore deletes `3L^2-1` lawful relative-parity
directions. That is not a harmless topological convention.

Every one of the `12N` onsite internal triangular graph edges joins two
different alternating-cycle families. These bounded connected generators
transfer parity between cycle families while conserving total parity. The
actual Cycle-219/Cycle-230 onsite coin has zero commutator with total Fock
parity and nonzero commutator with each of the three opposite-direction pair
parities. The contact is diagonal and total-parity even. Thus the complete
graph repairs the isolated comparator's per-cycle overconstraint at the
operator level.

It does not repair the scalar field's global odd-sector join. Per-cycle parity
and total parity are kept distinct throughout.

## 4. Proper-cubic, signed-operator, translation, and placement audit

At `L=3` the runner applies every one of the 24 proper-cubic frames to:

- every symmetric `Bhat_v`;
- every signed/framed `A_uv`;
- every cell-field equality;
- every local elementary cycle check; and
- all three Wilsons modulo the full stabilizer group.

The bounded vertex-order `CZ` and orientation `Z` repair inherited from the
connected edge presentation matches every signed `A` exactly. The symmetric
field operators and equality family map exactly, and the selected Wilson
sector maps into itself. The runner enumerates the full 27-element `L=3`
coarse-translation group, not only its three unit generators; every element
passes the same generator and sector tests. The translation maps themselves
are defined for arbitrary lawful `L` by modular cell addition.

The one-port branch is not reported as invariant. A frame maps its selected
port to one of a six-element orbit. Allowing that port label to transform
defines a covariant family with supplied orientation data; it is not an
unmarked autonomous branch.

The literal physical placement has coarse spacing 16:

```text
12 internal face sites:  2(D_a+D_b), b not opposite a,
3 shared outer faces:    +8 e_x,+8 e_y,+8 e_z per cell,
1 field site:            the coarse cell center.
```

The center is not an abstract pile of qubits: it is one physical `M_2` site.
It does not collide with a face site. The centered role set is invariant under
all 24 frames, and periodic patches contain exactly `16L^3` active sites. The
placement remains a period-16 macrocode: a unit physical translation changes
the active set, while a spacing-16 translation preserves it. The macro origin,
blank pattern, and routing are supplied structures.

## 5. Preparation, holonomy, deletion, leakage, and lawful domain

The lawful test domains are periodic `L=3,4,5` and held-out `L=6`; `L>=3`
avoids aliased undirected faces.

The `Z`-equality field has one logical bit. An `X` mask commutes with every
equality iff it is constant on the connected cell graph. Therefore the only
two possibilities are the empty mask and the all-cell mask. The minimum
nontrivial switch is exactly

```text
X_field = product_c X_(R_c), weight N.
```

The exact local leakage discriminators are:

- one `X_(R_c)` violates six equality checks;
- `X_(R_c)X_(R_(c+e_a))` violates ten equality checks; and
- `X_field` violates zero but has weight `N`.

The tested separated same-port graph distances for `L=3,4,5,6` are
`3,6,6,9`. If one local input occupation flip changes total parity, a
bounded-radius encoding cannot change the field branch at a cell outside its
light cone. A coherent `CAT` encoding instead has unit long-range connected
`Z_c Z_d` correlation and zero one-point `Z`; a constant-depth local unitary
from product auxiliaries cannot create that correlation at unbounded
separation. These are preparation failures of this declared product-input,
unitary, `Z`-equality grammar, not a theorem against supplied long-range
entanglement.

The three Wilson `X` supports are exactly `3L`. With the incident-order
framing, their full Pauli weights have maxima `21,27,33,39` for `L=3,4,5,6`,
namely `6L+3`. Selecting their signs is explicit spin/topological-sector
structure.

Deletion tests are not hidden by redundant checks:

- deleting one of the three independent Wilson conditions loses rank one;
- deleting all six equalities incident on one cell isolates its field bit,
  creates two cell-graph components, and loses rank one;
- the retained mapped `B/A` algebra commutes with every constraint, so its
  ideal even-sector leakage is zero; and
- a named one-particle odd input projected into the symmetric branch or an
  even-volume selected-port branch has even-projector expectation zero and
  exact norm deficit one in an explicit two-sector projector calculation.

The last number is not disguised as a small numerical residual. The state is
outside the lawful matter image.

## 6. Mass, contact, and seam firewall

The target parameters remain exactly

```text
beta=-0.3,
g=0.37.
```

The predecessor one-particle rest-mass fixture is
`0.4534056541748851`, and the `L=3` principal sea rank is 73. The bounded
connected even algebra can synthesize the onsite coin, edge FSWAPs, and local
contact as even operators. That is not enough to report physical fixture
intertwining:

- the unmarked symmetric branch has no odd state at any size;
- the selected-port branch loses odd states at `L=4,6`;
- its fixed port breaks proper-cubic invariance;
- its parity field is not bounded-prepared; and
- the selected Wilson sector is still supplied.

Therefore the one-particle mass and rank-73 contact/seam block are not
synthesized in this encoding. The numerical predecessor values are controls,
not physical compiler residuals. Only if one common `E` closes rank, both
parities, covariance, preparation, and the update algebra may those fixtures
be promoted.

## 7. Prior-art and novelty boundary

Bravyi and Kitaev, [*Fermionic quantum
computation*](https://arxiv.org/abs/quant-ph/0003137), Sec. 8, supply the
bounded-degree edge-qubit even-fermion algebra and cycle-stabilizer mechanism.
Setia et al., [arXiv:1810.05274](https://arxiv.org/abs/1810.05274), develop the
Bravyi-Kitaev superfast construction for electronic-structure simulation.
Neither source is credited with an unmarked full-Fock odd join on this graph.

Chen and Kapustin, [arXiv:1807.07081](https://arxiv.org/abs/1807.07081), and
Chen, [arXiv:1911.00017](https://arxiv.org/abs/1911.00017), supply the direct
three-dimensional comparison: local bosonization with 2-form gauge structure,
total-even restriction on closed manifolds, and spin-structure dependence.
They do not automatically supply this campaign's unmarked bounded-preparable
full-Fock `E`.

Steudtner and Wehner,
[arXiv:1810.02681](https://arxiv.org/abs/1810.02681), are bounded prior art for
auxiliary-qubit fermion mappings and simple encoding circuits. Their setting
is two-dimensional and hardware-targeted; it does not supply the present
three-dimensional connected odd-sector join, all-24 audit, or selected
holonomy preparation.

Cycle 265 claims no invention of edge bosonization or auxiliary mappings. Its
fixture-specific contribution is narrower:

1. the literal `16N`-M2 connected square-pyramid plus cell-center code;
2. the exact `6N` exponent through held-out `L=6`;
3. the distinction between that exponent and the matter-algebra increment;
4. the exact `P_m=b^N` one-port functional and the `L=4,6` even-volume defect;
5. the all-64 port-subset proper-cubic invariant census;
6. the all-24 signed-operator and coarse-translation audit;
7. the exact field-switch, Wilson, deletion, and odd-projection residuals; and
8. the complete-graph versus isolated-cycle parity-transfer control.

No Thirring engine is used or compared.

## 8. Supplied-structure inventory

The candidate supplies:

1. the three-dimensional cubic coarse lattice and periodic torus;
2. the square-pyramid subdivision and its 15 face roles per cell;
3. the local incident-edge order/orientation framing and Clifford repair;
4. all local elementary primal-edge cycle checks;
5. the signs of three nonlocal torus Wilson constraints;
6. one literal cell-center `M_2` role per coarse cell;
7. the `Z`-equality field grammar and its `+1` constraint signs;
8. either the all-six dress or a selected one-port dress;
9. for the one-port branch, a direction marker or transforming marker orbit;
10. product auxiliary inputs for the bounded-preparation question;
11. the spacing-16 macro origin, blanks, sharing, and routing;
12. the fixed Cycle-219/Cycle-230 coin, stream ordering, `beta`, and `g`;
13. the Hermitian gate-synthesis branches for mapped even operators; and
14. a compiler schedule, which is not physical time.

The field carrier is not a Record. Its copied/equal `Z` label is a gauge or
reference variable, not a selected realized-history fact.

## 9. N1–N8 no-go-discipline audit

The negative shipped here is deliberately scoped to the connected edge code
plus one scalar cell field with local `Z` equalities and product-input unitary
preparation.

### N1 — Alternative-route enumeration

Alternatives explicitly considered are: one marked global parity M2; the
one-port cell field; the unmarked all-six cell field; one field M2 per matter
vertex; X/cat-like reference codes; local even pair-flip constraints;
non-Pauli subsystem encoders; a transforming six-port selector motif;
measurement/reset; supplied long-range entanglement; open boundaries or
punctures; and an auxiliary reference fermion. Several remain live.

### N2 — Condition-independence audit

Four conditions are separate:

1. total-parity faithfulness (`P_m` not fixed);
2. unmarked all-24 covariance;
3. bounded preparation of the field and Wilson sector; and
4. the period-16 physical role marker.

The all-six branch closes covariance but not parity. The one-port branch can
close parity at odd `N` but not even `N`, fixed-frame covariance, or
preparation. Wilson preparation is independent of the scalar parity defect.
The physical macro marker is independent of both.

### N3 — Hidden-condition scan

The result depends on a closed periodic domain, the all-`+1` local equality
sector, one scalar field qubit per coarse cell, diagonal `Z` dressing, product
auxiliary inputs, unitary bounded-radius preparation, three selected Wilson
signs, the local incident-order gauge, the spacing-16 macro origin, and
three-dimensional cubic geometry. None is promoted to a derived necessity.

### N4 — Residual matching

Every negative has a matched discriminator:

- exact exponent: `6N`;
- unmarked parity: `P_m=I`;
- one-port parity: `P_m=b^N`;
- even-volume odd-sector deficit: one full parity block;
- odd input projection norm deficit: `1`;
- one local field flip: six violated equalities;
- one neighboring pair flip: ten violated equalities;
- lawful field switch: weight `N`;
- Wilson support: `3L` in X and at most `6L+3` actual Pauli weight;
- fixed-port proper-cubic orbit: six directions;
- isolated-cycle overconstraint: `3L^2-1` missing relative parities; and
- independent Wilson or isolated-cell deletion: rank loss one.

### N5 — Resolution and rhetoric audit

The conclusion is not “local fermions are impossible,” not a universal
minimum-content theorem, and not an axiom-pressure claim. It is: the declared
scalar `Z`-equality join can close code dimension while failing the total-
parity functional and bounded preparation. “Rank-matched” is not called
“full-Fock.” Compiler schedules are not physical time.

### N6 — Partial-closure path scan

Substantial positive structure survives:

- the complete connected bounded even-CAR algebra;
- local elementary checks and exact ranks;
- three explicit topological sectors;
- actual bounded FSWAP polynomials;
- correct onsite inter-cycle parity transfers;
- constant 16-M2/cell overhead;
- all-24 signed-operator and coarse-translation covariance for the symmetric
  branch; and
- zero ideal even-algebra leakage.

The next path should preserve these rather than restart from isolated cycles.
X/cat-like reference parity codes or local even pair-flip constraints are the
closest steelman because the present failure uses `Z` repetition structure.

### N7 — Steelman

A stronger distributed code could store total parity as a locally
indistinguishable topological logical rather than a locally readable common
`Z` bit. A bounded local encoder might also be possible with a supplied
entangled resource, measurement/reset, a subsystem gauge whose local pair
flips commute with constraints, or an open boundary that absorbs the parity
flux. A six-port covariant quantum selector might avoid a fixed direction if
its own preparation and leakage close. None is ruled out here.

### N8 — Cross-cycle echo

Cycle 235 exposed the closed connected total-even edge code. Cycle 251 found
that covariant equality selectors can rank-match while their parity depends on
volume parity. Cycle 252 moved parity into coherent charge/frame and Wilson
joins but retained nonlocal preparation. Cycle 263 separately closed a local
full-rank prefix preparation and a bounded edge algebra without one common
encoding. Cycle 265 reproduces the equality defect on the complete graph and
adds the exact `P_m=b^N`, all-port covariance, held-size, and connected-vs-
isolated controls.

That echo is valuable evidence about this family of repairs. It is not a
route-independent theorem across the live steelmen. Therefore it creates no
shared obstruction and no axiom pressure.

## 10. Disposition and next probe

| clause | unmarked all-six | one selected port |
|---|---|---|
| complete connected graph | closed | closed |
| constant physical overhead | closed, 16 M2/cell | closed, 16 M2/cell |
| local checks | closed, plus 3 supplied Wilsons | same |
| exact exponent `6L^3` | closed | closed |
| faithful both-parity matter algebra | **fails all sizes** | odd `N` only; **fails L=4,6** |
| no direction marker | closed | **fails** |
| all 24 signed covariance | closed | covariant orbit only |
| bounded field/Wilson preparation | **fails tested grammar** | **fails tested grammar** |
| bounded connected FSWAP/coin/contact algebra | closed | closed |
| mass and rank-73 seam intertwining | not reached | not reached |

The optimal next campaign is a connected-graph, locally indistinguishable
parity-reference code: start with X/cat-like or even-pair-flip constraints,
require a literal all-24 physical motif, and test whether its logical parity
can couple to `product_v B_v` without a selected port or volume-parity defect.
The first discriminator should be a common bounded-preparation/intertwining
circuit, not another dimension count.
