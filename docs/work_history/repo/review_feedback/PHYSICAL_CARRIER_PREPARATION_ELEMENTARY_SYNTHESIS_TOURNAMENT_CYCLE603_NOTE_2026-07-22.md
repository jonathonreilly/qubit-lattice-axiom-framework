# Physical carrier preparation / elementary synthesis tournament — Cycle 603

Date: 2026-07-22

Authority: none

Audit: unset

Authority remains none. Audit remains unset. This cycle changes no axiom,
foundation, Qualification, primitive, registry, policy, queue, audit status,
or PR surface.

Runner:

`scripts/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22.py`

## Result up front

Cycle 603 makes two constructive advances and retains three sharp
implementation boundaries.

First, Route A gives an exact bounded M2 synthesis of the structured Cycle 600
local events. It does not materialize an arbitrary `4096 x 4096` onsite
unitary. Instead it:

1. diagonalizes each species' six-direction massive coin with three selective
   pair Hadamards and a three-mode axis transform;
2. lowers the resulting 4-M2 valid-word gates through Gray paths, exact
   controlled-unitary identities, clean reversible scratch, and one-/two-M2
   gates;
3. computes the bound predicate `b(w)=1` exactly for `w=4..9`, applies the
   three pair phases in
   `exp[i g sum_(s<t) b_s b_t]`, and uncomputes every flag; and
4. lowers each crossed-link `(4+d,0)<->(0,4+d)` stream transposition into an
   exact eight-bit Gray network.

The admitted exact alphabet is fixed `X/H/T/T†/CNOT/SWAP` plus parameterized
one-M2 `RY(theta)/RZ(theta)/P(theta)`. Every executed gate has support at most
two, and every two-M2 occurrence has a literal bounded nearest-neighbor
move/apply/restore realization on a line patch. Full-space/off-code behavior,
inverse scratch return, deletion visibility, L3/L6/L7 size accounting, all 24
proper-cubic frames, and all 576 frame products are explicit.

This is an elementary bounded M2 synthesis theorem over that parameterized
alphabet. It is **not** finite exact closure over Cycle 580's
`H/CNOT/CZ/SWAP` alphabet. The inherited `beta=-0.3` coin eigenphases and
`g=0.37` contact phase remain calibrated one-M2 angle data. `T/T†` and
parameterized rotations were not accepted as Cycle 580 primitives. Clean
scratch initialization/renewal also remains supplied. The six independently
compiled endpoint tables are not promoted to one simultaneous global
`G_physical`: a conflict-free whole-torus stream schedule was not compiled.

Second, Route B constructs the translation-invariant local parent

```text
H_L = sum_<xy> (I - SWAP_xy).
```

Inside the exactly supplied `N=1` sector this is the cubic graph Laplacian. Its
uniform W orbital is the unique zero state and its exact finite-size gap is

```text
Delta_L = 4 sin^2(pi/L) ~ 4 pi^2/L^2.
```

The train L3, held L6, and held-out-size L7 cases are measured. Vacuum and the
uniform two-excitation Dicke state are also zero-energy states, so sector
uniqueness is not global genesis. A remote localized two-excitation basis
state has positive boundary energy and is a control, not a proof that the
whole `N=2` sector is excluded. The Hamiltonian provides a parent, not a
preparation law.

Route C constructs local excitation-conserving jumps

```text
J_xy = |psi+><psi-|.
```

Their common kernel has one W ray inside `N=1`; `sum J†J=H_L/2` has gap
`2 sin^2(pi/L)`. Removing all six incident jumps at one vertex grows the
one-excitation common-dark dimension from one to two. Vacuum and symmetric
two-excitation states remain dark. A Lindblad rate, convergence theorem,
finite Kraus recurrence, sector selection, and vacuum genesis are supplied or
open, not derived.

This is a positive tournament with scoped partial dispositions. There is no
broad no-go, no minimum-content claim, no shared obstruction, and no axiom
pressure.

## Exact target contract

The target has two coupled but separable obligations.

### Elementary synthesis obligation

For the accepted Cycle 600 standalone 12-M2/cell carrier presentation,
construct full-space gates of support at most two for:

```text
U_word = 1_absent direct-sum I_3_neutral direct-sum C_6
         direct-sum I_6_invalid,

U_contact = exp[i g sum_(s<t) b(w_s)b(w_t)],

S_d : (4+d,0) <-> (0,4+d), d=0,...,5.
```

Required controls are valid/off-code rows, scratch return, inverse and gate
deletion, exact gate/depth/SWAP counts, literal NN placement, all-frame
covariance, held size, and reproduction of Cycle 600 `E G = G_physical E`
fixtures. A generic multi-controlled table, arbitrary two-level gate, or
controlled phase does not count as elementary closure unless it is lowered
and its admitted angle data are inventoried.

A separate full-torus obligation is a collision-free circuit family whose
composition is the Cycle 600 abstract stream permutation. Independent local
endpoint gates do not by themselves discharge it.

### Preparation obligation

Construct a translation-invariant local parent or dissipative law selecting
the uniform one-excitation orbital, then distinguish:

- uniqueness inside `N=1`;
- uniqueness across all number sectors;
- state preparation versus static conservation;
- vacuum genesis versus relaxation of a declared nonempty sector; and
- a compile parameter/rate versus causal physical time.

Completion of global genesis would require the exactly-one sector itself to
be locally generated or selected without a global counter, root, boundary
seed, or host query. Cycle 603 does not complete that obligation.

## Accepted shore and representation boundary

The runner exact-pins the accepted Cycle 600 runner, parent-appended note,
receipt, and cold transcript at commit `a300290fb2361c4b0a2eef7da3ab27a70b9abc69`.
It inherits only the accepted standalone theorem:

```text
E_L : Fock_(N<=3)(C^(6V))
      -> wedge^3(C^(6V) direct-sum span{chi_0,chi_1,chi_2}).
```

There are three 4-M2 words per cell. Word `0` is absent, `1..3` are neutral,
`4..9` are six bound directions, and `10..15` are rejected by the Cycle 600
code. This remains a standalone carrier presentation replacing the Cycle 590
matter representation. It is not a `53+12` tensor composition.

## Route A — structured event compiler

### Coin structure

Write the six directions as three opposite pairs. A selective Hadamard on each
pair separates pair-symmetric and pair-antisymmetric sectors. The three
antisymmetric modes have one common eigenphase. The symmetric sector is a
three-axis matrix with a uniform eigenvector and a degenerate transverse
plane. The runner uses the explicit orthogonal basis

```text
u = (1,1,1)/sqrt(3),
v = (1,-1,0)/sqrt(2),
w = (1,1,-2)/sqrt(6).
```

It QR-factorizes only this `3 x 3` real axis transform into two-level Givens
rotations. Together with the pair Hadamards and six eigenphases, the resulting
18 high-level word operations reconstruct the entire 16-word extension. The
absent, neutral, and invalid rows remain identity. Thus the construction
exploits the physical coin symmetry rather than feeding the full table to a
generic unitary synthesizer.

Each basis-selective four-bit operation is then lowered as follows:

1. a Gray path moves the selected pair to adjacent Boolean words;
2. a three-controlled single-M2 unitary acts on that edge;
3. the Gray path is reversed;
4. one clean work M2 is returned exactly to zero.

The `C^3 U` uses a clean conjunction, the standard square-root `C^2 U`
identity, and exact ZYZ decompositions of every controlled one-M2 matrix.
Toffoli is explicitly lowered to six CNOT, seven `T/T†`, and two H gates.
No arbitrary multi-M2 gate survives.

### Contact structure

For bits `q3 q2 q1 q0`, the exact matter predicate is

```text
b(w) = (not q3 and q2)
       XOR (q3 and not q2 and not q1).
```

The clauses are disjoint and select precisely `4..9`; `q0` is a spectator.
Three flags and one shared conjunction work M2 are clean at the boundary.
After computing all flags, three two-flag controlled phases produce one phase
for every bound pair, hence phase `1`, `e^(ig)`, or `e^(i3g)` for bound number
zero/one, two, or three. Each controlled phase is lowered to two CNOT and
three one-M2 phase gates. The flag computation is then exactly inverted.

All `16^3=4096` rows are exhausted. Invalid labels have predicate zero. If an
invalid label accompanies two other valid bound words, those two valid words
still acquire their mutual contact phase; this is the declared off-code
extension, rather than a hidden all-identity invalid sector.

### Crossed-link stream structure

For direction `d`, the only nontrivial eight-bit endpoint exchange is

```text
(4+d,0) <-> (0,4+d).
```

A Gray path of endpoint Hamming length `h` realizes this transposition with
`2h-1` adjacent-basis swaps. Each adjacent swap is an exact seven-controlled X
with five clean conjunction M2, explicitly reduced to Clifford+T Toffoli
networks. Every 256-row permutation is exhausted, every scratch returns, and
all other valid and invalid pairs are fixed.

This closes each local crossed-link table. The six-direction global layer is
not claimed: torus shifts have overlapping endpoint calls, and the runner has
not supplied a double buffer, partitioned-QCA layer, or collision-free
schedule implementing their simultaneous composition.

### Gate and resource manifest

The receipt gives exact, machine-derived counts and schedule hashes. The
meaning of each resource class is:

| resource | status | role |
|---|---|---|
| `X/H/T/T†` | explicit fixed one-M2 gates | Boolean and Toffoli lowering |
| `CNOT` | explicit two-M2 gate | controls and phase gadgets |
| `SWAP` | explicit two-M2 routing gate | move/apply/restore on a line |
| `RY/RZ/P(theta)` | explicit parameterized one-M2 gates | exact inherited coin/contact angles |
| clean scratch | supplied zero-state M2, exactly uncomputed | one for coin, four for contact, five for stream |
| gate order | supplied compile-time sequence | finite circuit schedule, not physical time |

The persistent representation remains 12-M2 per cell. An active onsite patch
uses at most four scratch M2, and a stream patch uses five. Allocating the
maximum reusable scratch patch per cell would give 17 live M2/cell; this is
not mislabeled as a 12-M2 scratch-free compiler. Scratch reset and renewal are
not derived.

The literal layouts are finite line patches: 16 sites for onsite events and 13
for a crossed-link event. Before every non-neighbor two-M2 gate, one logical
role is moved next to the other by nearest-neighbor SWAPs; the gate is applied;
the SWAPs are reversed. The receipt counts those SWAPs and the serialized
depth exactly. Rotating either line through all 24 proper-cubic frames
preserves site injection and unit-edge adjacency. This is a bounded event
layout, not a simultaneous tiled global-stream layout.

### Exact controls

The runner checks:

- the 18-operation high-level word coin against the inherited `16 x 16`
  extension;
- the complete lowered coin on all 16 data columns with scratch zero, including
  final scratch leakage;
- the Toffoli and controlled-contact-phase identities;
- every one of 4096 contact rows;
- all six 256-row stream permutations;
- full-space invalid-word behavior;
- inverse uncomputation and visible routing/gate schedules;
- Cycle 600 local coin, contact, stream, seam, and full `N=0..3` E/G fixtures;
- train L3, held L6, and held-out-size L7 counts;
- every translation family inherited by the torus law, all 24 proper-cubic
  frames, and all 576 frame products.

The exact fixed/parameterized circuit is positive. Exact finite
`H/CNOT/CZ/SWAP` closure is false for this executed alphabet comparison because
the runner still lists `T/T†` and inherited parameterized rotations. No
impossibility for every finite or approximate alphabet is claimed.

As a deliberately narrow discrete comparator, the runner also replaces each
coin eigenphase and the contact phase by its nearest exact `P(k*pi/4)` T-power
and records the nonzero unit-complex residual. This is an executed diagonal
phase-grid miss, not a search over all Clifford+T words and not a finite-gate
no-go.

## Route B — cubic W parent

On the binary carrier M2 at each cubic vertex, define one local term for each
unoriented nearest-neighbor edge:

```text
h_xy = I - SWAP_xy.
```

In `N=1`, `h_xy=(|x>-|y>)(<x|-<y|)`. The connected cubic graph therefore has
one zero vector, the normalized uniform W orbital. Fourier modes give the
exact gap `4 sin^2(pi/L)`. The runner diagonalizes the actual L3, L6, and L7
matrices and compares with that formula. `Delta_L L^2` approaches `4 pi^2`,
so the thermodynamic gap closes; no uniform positive-gap preparation theorem
is claimed.

Every translation maps the edge set to itself. All 24 proper-cubic frames map
the edge set to itself, and all 576 frame products close on the tested site
actions. Each term has support two M2 and there are `3L^3` terms.

Deleting one edge changes the parent operator but leaves W dark because every
individual edge already annihilates W. The remaining graph stays connected
and W remains the unique `N=1` zero vector; this is reported instead of a
contrived deletion-failure claim.

The vacuum is a zero-energy state. In every fixed-number sector the completely
symmetric Dicke state is also annihilated by all swaps; the receipt explicitly
records the `N=2` competitor. A remote localized two-excitation basis word has
positive energy, verifying that the parent is nontrivial without confusing
one competitor with sector exclusion.

Because nearest-neighbor transpositions generate all site permutations on the
connected torus, the common swap-ground subspace has dimension one in each
fixed sector `N=0,...,V`, hence dimension `V+1` across the full binary-carrier
Hilbert space. The receipt records dimensions one for `N=0,1,2,V` and `V+1`
globally; the parent does not merely exhibit one accidental `N=2` vector.

The result is a sector parent only. `N=1`, the Hamiltonian coupling, boundary,
and state-cooling/preparation law are supplied. Static ground-state
characterization is not an occurrence, Record, realized history, or genesis.

## Route C — dark-jump candidate

For each edge use

```text
|psi+> = (|01>+|10>)/sqrt(2),
|psi-> = (|01>-|10>)/sqrt(2),
J_xy   = |psi+><psi-|.
```

Then `J†J=|psi-><psi-|` and the dark parent is `H_L/2`. Inside `N=1`, the
common-kernel condition says neighboring amplitudes agree. Connectedness
therefore gives one W ray and gap `2 sin^2(pi/L)`. Edge reversal changes J by
only a sign, so its dissipator is orientation independent and proper-cubic
covariant.

This does not yet prove that the full Lindblad generator has a unique
stationary density matrix or a usable convergence rate. It does not compile a
finite scheduled Kraus recurrence. It conserves excitation number, so vacuum
remains vacuum and symmetric `N=2` remains dark. The exact-one input sector is
supplied. Removing all six incident jumps isolates one vertex and makes the
`N=1` common-dark dimension two, providing a deletion control.

The common pure dark-space dimensions mirror the swap parent: one in each
fixed sector and `V+1` across all number sectors. These kernel dimensions are
not promoted to stationary-density-matrix dimensions; that stronger
Lindbladian question is explicitly unproved.

A continuous generator parameter or circuit layer is not causal time. A dark
state is not by itself a prepared physical state. Conservation is not genesis,
and one common dark ray inside `N=1` is not global unique genesis.

## Route dispositions

| route | constructive result | exact residual |
|---|---|---|
| A: structured elementary synthesis | exact support-two parametric coin/contact/link event circuits and bounded NN patches | finite Cycle 580 alphabet, scratch renewal, and conflict-free global stream schedule open |
| B: parent Hamiltonian | W unique with exact measured gap inside supplied `N=1` | vacuum/N2 degeneracy and preparation law remain |
| C: dissipative dark kernel | W is the unique common dark vector inside supplied `N=1` | stationary-state/convergence/rate theorem and sector genesis remain |

No route-specific residual is constitutional evidence.

## Supplied / derived / open inventory

### Supplied

1. Accepted Cycle 600 encoder, 12-M2/cell word representation, `beta=-0.3`
   coin, `g=0.37` contact, seam convention, and abstract torus stream map.
2. Parameterized noiseless one-M2 rotations, fixed `T/T†`, CNOT, H, X, and
   SWAP gates.
3. Zero-state clean scratch, scratch reuse/renewal, compile-time event order,
   and bounded line-patch coordinate charts.
4. Finite periodic L3/L6/L7 cubic boundaries and the `N=1` sector.
5. Candidate parent/jump coupling and any future generator rate.

### Derived

1. An exact symmetry-adapted 18-operation word-coin factorization and complete
   support-two parametric lowering with full-space extension.
2. Exact reversible contact predicate/phase/uncompute and six exact eight-bit
   crossed-link permutations.
3. Exact gate, depth, routing SWAP, scratch, support, held-size, and covariance
   certificates, with Cycle 600 E/G reproduction.
4. A local translation-invariant W parent with exact finite-volume gaps and
   vacuum/N2 controls.
5. A local excitation-conserving dark-jump family, its common `N=1` kernel,
   gap, and deletion control.

### Open

1. Exact finite accepted-alphabet synthesis or a declared approximation/error
   target for all inherited angles.
2. A simultaneous collision-free whole-torus stream circuit, possibly using a
   counted double buffer or partitioned QCA.
3. Genesis and renewal of clean scratch and carrier number sectors.
4. A local number-selecting parent/reservoir making exactly one carrier per
   species global rather than supplied.
5. A complete Lindblad stationary-state/convergence theorem, physical
   recurrence, and empirical rate/time interpretation.
6. Noise thresholds, arbitrary horizon, complete N4 interactions, continuum,
   Lorentz/CPT, gravity/source, Born/actuality, occurrence, and Record closure.

## Six-wall dependency ledger and maturity

| wall | Cycle-603 movement | residual |
|---|---|---|
| `C_ref` | W orbital now has an explicit local parent and dark-kernel characterization | `N=1` and clean scratch reference sectors supplied |
| `C_num` | exact gaps and vacuum/N2 competitors distinguish sector uniqueness from genesis | no local exactly-one selector or reservoir |
| `C_wrap` | every crossed-link word table is an exact support-two event circuit | no simultaneous global shift schedule; seam remains the accepted abstract exterior fixture |
| `C_int` | full `N<=3` coin/contact E/G is reproduced by the compiled word restriction | calibrated angles, N4 interactions, and noise open |
| `C_local` | major: arbitrary multi-controlled tables are lowered to bounded one-/two-M2 gates and literal NN patches | finite accepted alphabet, scratch renewal, and tiled global network open |
| `C_source` | scratch, flags, work M2, parent edges, and jumps are counted | carrier bookkeeping is not empirical charge, energy, stress, source, or gravity |

Evidence-planning maturity remains operational quantum/Records `4.80/5`
repository and `4.65/5` strict; causal time `3.95/5` and `3.80/5`;
inertia/matter `4.92/5` repository and rises from `4.94/5` to `4.96/5` strict
for the bounded event synthesis; gravity/source `4.10/5` and `3.85/5`;
Born/probability `4.20/5` and `3.65/5`. These are planning coordinates, not
probabilities, audit grades, or constitutional status.

## Fresh N1–N8 no-go discipline

The current origin/main no-go-discipline skill and proof-search governance were
read before construction. The newer origin/main wording is followed.

### N1 — normalized alternatives

The registry contains six material families normalized by object, mechanism,
and terminal obligation:

1. the attempted structured word-table circuit;
2. the attempted fixed diagonal T-phase-grid comparison;
3. the attempted cubic swap parent;
4. the attempted local dark-jump family;
5. the Cycle 600 attempted topological winding/mark family, prior-scoped only;
6. the live untested fault-tolerant approximation plus autonomous
   number-selecting reservoir.

The sixth family is the strongest live counterroute. Therefore no broad
synthesis or genesis negative can ship.

### N2 — directional condition audit

All ten directional pairs among finite alphabet/calibration, simultaneous
global streaming, exactly-one sector genesis, dark convergence/rate, and clean
scratch renewal are recorded in the receipt. They are current explicit imports,
not asserted route-independent no-go walls. Closing one does not automatically
supply the named mechanism of another.

### N3 — hidden-condition scan

The inherited angles, clean scratch, routing order, global stream order, N=1
sector, parent/dissipator coupling, generator clock, boundary, and off-code
extension are explicit. There is no load-bearing “standard,” “obvious,”
“natural,” registered, canonical, or background step.

### N4 — residual matching

Cycle 600 left elementary 12-role synthesis unexecuted. Route A matches that
residual and partially closes it with an exact parametric event compiler; it
does not claim the finite-alphabet or global-stream subresiduals closed. Cycle
600 explicitly named a one-excitation parent and dissipative W state as live;
Routes B/C match those residuals, closing the sector parent/common-dark
questions while retaining genesis and convergence.

### N5 — rhetoric resolution

- Alphabet language applies only to the executed Cycle 580
  `H/CNOT/CZ/SWAP` comparison, not every exact or approximate gate set.
- Stream language distinguishes a per-endpoint table, bounded event patch,
  and full lattice-wide conflict-free composition.
- W uniqueness is tested only within `N=1`; vacuum and `N=2` are explicit.
- Dark uniqueness means common pure dark vector, not unique stationary density
  matrix or preparation.

No broader resolution is inferred.

### N6 — partial-closure paths

Four live constructive paths are explicit: ratify/calibrate a parameterized
one-M2 alphabet or set a precision-bounded Clifford+T target; add a counted
double buffer/partitioned QCA for global streaming; construct a local
number-selecting reservoir; and prove/compile a complete dark semigroup. These
are import-retirement programs, not new axioms.

### N7 — hostile steelman

A hostile reviewer should reject both an elementary-synthesis no-go and a
genesis no-go. The exact support-two parametric compiler has already removed
the arbitrary multi-controlled tables, so either a calibrated `RY/RZ/P`
elementary contract or ordinary precision-bounded Clifford+T synthesis could
retire the angle import. A double-buffer partitioned QCA could close the global
shift at constant overhead. The gapped W parent and local dark jumps likewise
give a concrete platform on which a number-selecting reservoir or gauge charge
could select `N=1`. None of those live mechanisms was tested to closure.

### N8 — cross-cycle echo

Cycles 560/563 retired global decoder/order services with bounded tables,
Cycle 580 retired an isometry-only gate/layout gap with explicit circuits, and
Cycle 600 retired the full `N<=3` carrier update. Cycle 603 narrows the next
two imports constructively. That repeated pattern supports another compiler
and preparation cycle, not constitutional language.

Negative claim shipped: **false**.

Minimum-content claim shipped: **false**.

Shared-obstruction claim shipped: **false**.

Axiom-pressure claim shipped: **false**. Exact phrase: no axiom pressure.

## Interpretation firewall

- A schedule is not time; exact phrase: schedule is not time.
- Circuit depth or a Lindblad parameter is not a causal rate.
- Carrier bookkeeping is not empirical charge, energy, stress, source, or
  gravity.
- A ground state or dark ray is not a branch, occurrence, Record, or realized
  history.
- A unique state within `N=1` is not global genesis.
- Conservation is not preparation or genesis.
- A line event patch is not a simultaneous global physical update.
- Proper-cubic covariance is not Lorentz covariance.
- Exact `N<=3` matter action is not complete N4 interactions.
- The standalone 12-M2 representation is not a Cycle 590 composition.

## Prior-art and novelty boundary

Graph-Laplacian W parents, ferromagnetic swap Hamiltonians, symmetric Dicke
states, dark-state jumps, Givens/Gray synthesis, ZYZ controlled-unitary
decomposition, Clifford+T Toffoli circuits, reversible predicates, and
nearest-neighbor SWAP routing are standard methods. No general priority or
novelty claim is made.

The repo-local result is their exact-pinned composition for the Cycle 600
three-species carrier code: the specific six-ray massive coin, `4..9` matter
predicate, three-word contact, six crossed-link tables, exterior E/G fixtures,
cubic frames, and explicit genesis boundary.

## Optimal next campaign

Compile the abstract Cycle 600 torus stream into a constant-overhead
double-buffer or partitioned-QCA physical circuit, including collision-free
layers, scratch renewal, all 24/all 576 covariance, and L3/L6/L7 deletion
controls. In parallel choose either:

1. a calibrated parameterized one-M2 rotation contract with physical error
   tests; or
2. a precision target and a fault-tolerant approximate Clifford+T compiler.

For preparation, add a local number-selecting reservoir or gauge charge to the
W parent/dark family and test vacuum, remote `N=2`, stationary-state dimension,
gap/convergence scaling, and whether exactly-one is selected without size data
or host control.

## Cold verification

Frozen command:

```bash
/usr/bin/time -l python3 -u scripts/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22.py
```

The generated receipt records exact route residuals, gate/depth/SWAP counts,
schedule hashes, L3/L6/L7 rows, all 24/all 576 audits, runtime, maximum RSS,
runner SHA-256, and note SHA-256. Authority remains none and audit remains
unset.

## Independent parent verification

The parent reviewed the distinction among an exact parameterized event
compiler, an exact finite-alphabet compiler, and a simultaneous global stream
before rerunning the frozen executable.  The rerun reproduced `7 PASS / 0
FAIL` in `3.1620211249683052 s` internally and `3.92 s` externally, with
maximum RSS `181,485,568` bytes, peak memory footprint `166,363,712` bytes,
and zero swaps.  Its transcript SHA-256 is
`bce69f75597ef03c8807bf267e708ba406aad12efb9ad41a6581b441acc4a052`.

The parent accepts the support-two `X/H/T/Tdg/CNOT/SWAP` plus parameterized
`RY/RZ/P` compilation of the onsite coin, contact, and individual crossed-link
events; the exact `N=1` W-parent statement and its finite-size gap; and the
local W dark-kernel statement.  It does not accept exact closure in the finite
Cycle-580 alphabet, a conflict-free global carrier shift, scratch renewal,
global one-carrier genesis, a Lindblad convergence/rate theorem, a Record,
time, source/gravity identification, shared obstruction, or axiom pressure.
The rerun refreshed the generated receipt's runtime fields; the worker cold
transcript remains the frozen worker evidence.
