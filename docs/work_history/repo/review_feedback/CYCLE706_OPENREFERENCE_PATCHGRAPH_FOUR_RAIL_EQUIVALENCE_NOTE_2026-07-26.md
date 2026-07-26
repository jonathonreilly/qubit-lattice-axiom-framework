# Cycle 706 OpenReferenceGraph 80 ↔ PatchGraph 76+4 equivalence — 2026-07-26

Type: meta

Authority: none

Audit: unset

## Scope and result

This checkpoint resolves the finite `2x2` graph mismatch left open by the
landed [Cycle-703 compiler tournament](../../../RECURRENT_ENDPOINT_INCIDENCE_PHYSICAL_M2_COMPILER_TOURNAMENT_CYCLE703_NOTE_2026-07-25.md).

Two propositions are separated:

1. **Natural direct relabeling — falsified.**  Relabel the 76 graph edges
   common to both constructions identically and call the four extra
   OpenReferenceGraph reference bonds independent X-, Y-, or Z-fixed rails.
   This fixes every matter logical X/Z Pauli but does not map the signed
   stabilizer code.
2. **Finite signed Clifford equivalence — constructed.**  A complete signed
   Pauli-group isomorphism fixes all 24 matter logical pairs, maps the 49
   shared cycle checks and three independent D rows to their PatchGraph
   counterparts, and maps the four Open bond-rectangle checks to four
   prepared `Z_rail=+1` checks.

The second statement is an exact code equivalence on the finite `2x2`, not a
bounded recurrent edge-qubit circuit or literal physical-site implementation.
Its largest edge-generator image has Pauli weight 15 and spans cell diameter
two.  No all-volume support bound is
derived.

Symplectic stabilizer-tableau completion and Clifford equivalence are standard
methods; see [Dehaene--De Moor](https://doi.org/10.1103/PhysRevA.68.042318)
and [Aaronson--Gottesman](https://doi.org/10.1103/PhysRevA.70.052328).
The new content claimed here is only the fixture-specific signed
OpenReferenceGraph-to-PatchGraph-plus-rail map, the exhaustive direct-map
falsifier, and their declared finite covariance/support controls.

## Read-only evidence reconstruction

The runner independently reimplements the two graph definitions and verifies
their exact edge-list SHA-256 digests against the landed Cycle-703 definitions:

| Graph | graph-edge qubits | Digest |
|---|---:|---|
| `OpenReferenceGraph(2x2)` | 80 | `324a88a72a23afb0f2d8ac445aa6d3a8709d4a2d4ce0eee6a8fea031f33ea6c4` |
| path-ordered `PatchGraph(2x2)` | 76 | `d9e04aca40f3e2ffeaaf6c6dfa02e5d7066b4891ecd273fe54d537483c6a64b8` |

The distinction between sorted Open cells and the Patch Hamiltonian cell path
is retained.  It changes one coarse-plaquette stabilizer sign and is not
normalized away.

For `N` seven-vertex cells and `M` open coarse adjacencies,

```text
E_open  = 18 N + 2 M,
E_patch = 18 N + M,
E_open - E_patch = M.
```

The difference is exactly one parallel reference-bond edge per coarse
adjacency:

| Fixture | Cells `N` | Adjacencies `M` | Open / Patch / rails | Logical qubits | Stabilizer rank |
|---|---:|---:|---:|---:|---:|
| one cell | 1 | 0 | `18 / 18 / 0` | 6 | 12 |
| one edge | 2 | 1 | `38 / 37 / 1` | 12 | 26 |
| L triomino | 3 | 2 | `58 / 56 / 2` | 18 | 40 |
| held `2x2` | 4 | 4 | `80 / 76 / 4` | 24 | 56 |

All source and target canonical-basis failures are zero on these four
fixtures.

On `2x2`, the Open graph has 28 vertices and cycle rank

```text
80 - 28 + 1 = 53.
```

Those 53 independent cycles are 48 cell triangles, four bond rectangles, and
one coarse plaquette.  The Patch graph has cycle rank

```text
76 - 28 + 1 = 49,
```

comprising the same 48 cell triangles and one coarse plaquette.  Each code
also has three independent local-D constraints.  Thus

```text
Open:             53 loops + 3 D = 56 stabilizers,
Patch:            49 loops + 3 D = 52 stabilizers,
Patch + 4 rails:  49 loops + 3 D + 4 Z_rail = 56 stabilizers.
```

Both sides encode 24 logical qubits.

## Exact falsifier for the direct map

Let `P_nat` be the qubit permutation that maps every shared graph edge by its
endpoint labels and maps each reference bond to its corresponding rail.  It
maps all 24 logical Z rows and all 24 phase-oriented logical X rows exactly.
It also maps every shared loop to the same unsigned Pauli support.

It does **not** map the prepared signed code:

| Independent rail axis | Target rank | Rank after adjoining mapped Open stabilizers | Cross commutator failures |
|---|---:|---:|---:|
| X | 56 | 62 | 16 |
| Y | 56 | 62 | 20 |
| Z | 56 | 60 | 10 |

For the best Z-rail candidate, exact signed target-tableau decoding classifies
the 56 mapped Open stabilizer generators as:

```text
51 positive target stabilizers,
1 negative target stabilizer,
4 outside the target stabilizer group.
```

The negative row is the path-order-sensitive coarse plaquette.  The four
outside rows are not repaired by choosing another independent rail axis.
The runner exhausts all `3^4=81` mixed X/Y/Z axis assignments.  Their union
ranks range from 60 to 63 and their cross-commutator failures from 10 to 20;
none closes.  Including every independent ± character gives `6^4=1,296`
signed rail codes.  All fail either the unsigned support/commutator invariant
or the rail-free coarse-plaquette sign, which no rail-character choice can
change.
This falsifies the declared direct tensor-rail map only.  It is not a no-go
for Clifford equivalence or for a different entangled rail constraint.

## Constructive signed Clifford map

Choose the following 80-row commuting Hermitian W bases.  The source basis is

```text
W_open = (
  24 matter logical Z,
  49 shared cell/coarse loop checks,
  3 independent Open D checks,
  4 bond-rectangle checks
).
```

The target basis is

```text
W_patch+rail = (
  24 matter logical Z,
  49 Patch cell/coarse loop checks,
  3 independent Patch D checks,
  4 Z_rail checks
).
```

Both have GF(2) rank 80.  Their stabilizer suffixes have zero signed-phase
inconsistencies.  The target 49 local loop rows also contain all 49
fundamental PatchGraph loop rows as positive signed stabilizers, so this is
the same Patch loop code rather than a rank-only substitute.

Complete each W basis to a canonical `(W,V)` Pauli tableau.  The first 24 V
rows are the explicit phase-oriented matter logical X rows; the remaining V
rows use one deterministic free-variables-zero symplectic completion.  For
any Open Pauli `P`, define

```text
Phi(P) = encode_patch+rail(decode_open(P)).
```

The phase coordinate is retained exactly.  The inverse exchanges the two
tableaux.

The semantic action is therefore explicit:

```text
Phi(Z_logical[x,a])       = Z_logical[x,a],
Phi(X_logical[x,a])       = X_logical[x,a],
Phi(C_open shared)        = C_patch shared,
Phi(D_open[x])            = D_patch[x],
Phi(bond_rectangle[e])    = Z_rail[e].
```

Every listed equality has zero signed-Pauli residual.

Because the 24 matter logical Z rows are also included positively in W, the
unique prepared-work character maps as

```text
Phi(|vacuum>_Open) = |vacuum>_Patch tensor |0000>_rail
```

at the exact stabilizer-tableau level.  Fixing the logical X/Z pairs then
extends the same map to arbitrary encoded matter states; this is not merely a
vacuum-rank comparison.

## Exhaustive finite controls

The 80 graph-edge X generators and 80 graph-edge Z generators provide a complete
finite certificate:

- their 160 images have symplectic rank 160;
- every image maps back exactly under `Phi^-1`;
- all 25,600 ordered generator products satisfy
  `Phi(PQ)=Phi(P)Phi(Q)`, including Pauli phases;
- deleting any one edge-generator image lowers rank from 160 to 159; and
- deleting any bond-check or target rail-Z basis row lowers W rank from 80 to
  79.

The edge-image weight census is:

```text
weight 1: 126,
weight 2: 20,
weight 3: 10,
weight 9: 1,
weight 10: 1,
weight 14: 1,
weight 15: 1.
```

The maximum cell-Manhattan support diameter is two.  The four high-weight
images are the reference-bond X generators; they are the finite paths that
disentangle bond-rectangle checks into rail Z.  This is why the result is not
promoted to a recurrent local compiler.

Flipping the sign of any of the four Open bond checks maps to `-Z_rail`
rather than the prepared `+Z_rail`; all four mutations are detected.  Empty,
duplicate-cell, and disconnected domains are actively rejected.

## Proper-cubic covariance

For each of the 24 proper-cubic frames, the runner rebuilds both graphs on the
transformed cell path, constructs exact edge-order gauge repairs for every A
generator, and rebuilds the signed equivalence.  It checks the commutative
diagram on 104 semantic rows per frame:

```text
24 logical Z + 24 logical X + 56 source stabilizers = 104.
```

All 2,496 signed diagram comparisons pass.  Both Open and Patch A-generator
transport failure counts are zero, and both transformed tableaus remain
canonical.

All 576 ordered frame products close in the direction representation.  The
four rail endpoint labels give 2,304 additional rail-composition tests, also
with zero failures.

This is covariance of the code/logical equivalence.  The arbitrary ambient V
completion is not asserted to be a uniform local circuit, and no physical-site
preparation schedule is inferred from the frame test.

## Supplied, derived, and open inventory

Supplied:

1. the landed Cycle-703 graph definitions and their pinned edge-list digests;
2. the finite `2x2` cell path and six-mode intra-cell Fock chart;
3. the local edge order entering every BKSF A generator;
4. the positive loop, D, and rail-Z characters; and
5. Cycle-232 Pauli, GF(2), proper-frame, and local order-gauge helper
   conventions; and
6. deterministic free-zero tableau completion.

Derived:

1. the exact 76-edge bijection and four reference-bond rail labels;
2. the signed canonical bases and full Pauli-group isomorphism;
3. the exact direct-map signed-sector falsifier;
4. the 24 individual-frame semantic equivalence diagrams and 576-product
   direction/rail-label composition; and
5. all ranks, inverse/multiplication checks, support census, deletions, and
   unlawful-domain rejections.

Open:

1. a bounded local Clifford circuit implementing the map without a global
   tableau solve;
2. an all-volume constant-support family;
3. composition with the preparation controller, stream repetition, Cycle-232
   placement, and nearest-neighbor physical-M2 routing; and
4. autonomous generation or protection of the rail-Z reference state.

The four rails are sufficient for this construction but are not claimed
minimal.  Stabilizer signs are not called energy, tableau order is not called
time, and no controller copy is called a Record.

## Dependency effect

| Wall | Effect |
|---|---|
| `C_ref` | sharpened: each extra reference bond can be converted exactly to one prepared rail-Z character on `2x2`; rail preparation/genesis remains supplied |
| `C_num` | unchanged: the map fixes the complete 24-qubit logical Pauli algebra and is number-sector independent |
| `C_wrap` | unchanged: tableau and cell-path order are not causal time or realized winding history |
| `C_int` | unchanged: this is a code bridge, not a new interaction result |
| `C_local` | improved finitely: the two graph codes are exactly signed-Clifford equivalent; a uniform bounded implementation remains open |
| `C_source` | unchanged |

No global 0–5 TOE maturity score changes.  No Record, causal time,
gravity/source, or Born/probability result is constructed.

## No-go-discipline N1–N8 boundary

The scoped negative is only “the natural direct edge relabeling plus four
independent same-axis rail checks is not the signed `2x2` code equivalence.”
The constructive Clifford result prevents any broader graph-equivalence
no-go.  The no-go discipline is applied as a guard.

### N1 — normalized route families

| Family | Mechanism / terminal obligation | Status | Evidence |
|---|---|---|---|
| direct edge permutation + arbitrary independent signed X/Y/Z rails | tensor product rail character | **ATTEMPTED / exhaustively falsified** | all 1,296 signed choices fail; uniform X/Y/Z give union ranks `62/62/60` |
| signed semantic tableau equivalence | canonical Pauli coordinates; bond checks become Z rails | **ATTEMPTED / succeeds finitely** | rank 160, exact inverse and 25,600 products |
| bounded bond-elimination Clifford | local check Gaussian elimination per coarse edge | **UNTESTED** | must reproduce `Phi` on the code while keeping size-independent support |
| entangled rail/check code under natural relabeling | retain bond rectangles as rail-coupled stabilizers | **UNTESTED / weaker target** | would not be Patch code tensor prepared rails |
| direct PatchGraph preparation | bypass Open graph rather than conjugate it | **UNTESTED here** | requires controller/preparation composition |

The successful second family blocks any claim that the two finite codes are
inequivalent.

### N2 — condition independence

`W_direct-sign` is the negative coarse-plaquette character;
`W_direct-tensor` is the four mapped rows outside the Z-rail target group;
`W_local-circuit` is the absence of a uniform bounded implementation;
`W_rail-genesis` is preparation of `Z_rail=+1`; and `W_composition` is the
missing controller/placement integration.  The signed tableau map solves the
first two without solving the last three.  They are not collapsed into one
obstruction.

### N3 — hidden-condition scan

The Cycle-703 graph digests, graph ordering, cell path, mode chart, stabilizer characters,
rail axis, basis order, free-zero completion, finite support, and covariance
scope are explicit.  No direct-map support equality is mistaken for signed
code equality.  No finite tableau is silently promoted to an all-volume
circuit.

### N4 — residual matching

The rebuilt edge digests match the landed Cycle-703 graph definitions exactly.  The
edge counts `80` and `76`, cycle ranks `53` and `49`, D increment three,
logical count 24, and stabilizer ranks `56` and `52` reproduce the graph
identities.  The direct Z-rail residual is independently visible as union
rank 60, ten cross commutators, one negative shared cycle, and four outside
rows.  The constructed map removes all semantic residuals and matches all 49
Patch fundamental cycles positively.

### N5 — resolution and rhetoric audit

One cell, one edge, L, and held `2x2` are tested; the full signed graph-edge
Pauli group is certified on `2x2`; the semantic code diagram is tested for 24
individual frames, while the 576-product test covers direction composition and
2,304 rail-label compositions.  `3x3`, arbitrary open volumes, periodic topology,
physical-site controller synthesis, and a constant-depth/radius family are not
tested.  Only the direct map is called falsified.

### N6 — partial closure

The finite code equivalence is complete, fixes every logical Pauli, and is
proper-cubic covariant.  Most edge generators map at weight one to three.
The four reference-bond X images identify the only high-weight portion of the
chosen completion.  A local elimination circuit can target those images
without reopening the logical or signed-stabilizer questions.

### N7 — steelman

The strongest next construction is a covariant bond-elimination Clifford:

1. for each reference bond, choose its bond rectangle as the pivot check;
2. use only Clifford row operations supported on that rectangle to map the
   pivot to `Z_rail`;
3. update the two incident D rows locally so they become Patch D rows;
4. color overlapping bond rectangles by transported coarse-edge direction;
5. prove that the circuit fixes all matter logical X/Z rows and returns no
   work register; and
6. freeze the rule on one edge/L/`2x2`, then test `3x3`, a cube, 24 frames,
   and 576 products without a tableau refit.

Its immediate falsifier is growth of the reference-bond X image or failure of
two adjacent eliminations to commute up to positive Patch stabilizers.

### N8 — cross-cycle echo

The landed Cycle-703 checkpoint explicitly kept OpenReferenceGraph preparation and
PatchGraph scaled scheduling separate because no signed equivalence had been
constructed.  This checkpoint supplies that missing finite equivalence, but
that checkpoint's locality/composition caution remains valid.  Earlier BKSF tableau,
decoder, and controller results use different terminal obligations and do not
establish either minimum rail content or failure of local bond elimination.
There is no shared obstruction and no axiom pressure.

## Disposition

- natural direct tensor-rail map: **falsified on exact signed `2x2` data**;
- finite logical-fixing signed Clifford map: **constructed and exhaustive**;
- 24 individual-frame semantic covariance: **passes**;
- 576-product direction and rail-label composition: **passes**;
- bounded recurrent graph equivalence: **open**;
- broad no-go or minimum-content claim: **not made**.

No audit-status, queue, registry, policy, axiom, foundation, or Qualification
file is modified.

## Reproduction

Runner:

```text
scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py
```

Cached output:

```text
logs/runner-cache/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.txt
```

Expected terminal line:

```text
SUMMARY pass=8 fail=0
```
