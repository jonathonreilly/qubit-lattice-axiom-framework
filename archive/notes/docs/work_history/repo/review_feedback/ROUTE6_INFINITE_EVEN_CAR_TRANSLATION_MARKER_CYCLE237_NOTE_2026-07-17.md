# Route 6 infinite even-CAR and unit-translation marker discriminator — Cycle 237

**Date:** 2026-07-17

**Type:** algebra/state/preparation separation plus constructive translation-orbit code

**Status:** finite global-parity artifact narrowed; full graded local net and
bounded unitary preparation have narrow primary-source obstructions; even-CAR
sector representations and a unit-translation-covariant marker code remain
constructive but do not yet give the requested state compiler

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

**Packaging:** distinct Cycle-237 note and runner only; no commit, push, PR,
foundation, axiom, Qualification, primitive, registry, policy, queue, or audit
change

Companion runner:

```text
scripts/ROUTE6_INFINITE_EVEN_CAR_TRANSLATION_MARKER_CYCLE237_2026_07_17.py
```

## Result up front

The scalar-reference identity `B_r(x)=P_matter` is a finite-code artifact, not
the right infinite-volume observable.  Finite-region parity products fail to
converge in quasi-local norm: enlarging a region by one mode leaves norm gap
exactly `2`.  The infinite CAR algebra and its parity-even local observable
algebra therefore do not contain the finite route's uniform local copy of a
global parity product.

That correction does **not** produce a bounded local state compiler.  Four
notions must remain separate:

| Notion | Cycle-237 disposition |
|---|---|
| local even-algebra morphism | live and supported by exact bosonization; every bounded parity-even Cycle-230 update can in principle have a bounded gauge-invariant image |
| sector representation / state functional | the one-particle and rank-73 fixtures are both odd and can be represented in one odd superselection sector without a runtime parity bus |
| locality-preserving state encoding | not supplied by an observable duality; the full graded CAR net has an exact remote-odd-field contradiction, while an even block code has nonlocal code-state structure |
| finite-depth preparation | unitary preparation from product input is asymptotically excluded for local block codes on graphs with growing overlapping loops under Guaita's exact hypotheses; measurements/feedforward and supplied sector states remain live |

The strongest narrow negative is:

> There is no injective bounded-radius morphism of the **full graded CAR local
> net**, including odd fields, into the ordinary tensor-local bosonic `M_2`
> net.  For two sites farther apart than twice the radius, the two physical
> images have disjoint support and commute, whereas the two odd Majoranas
> anticommute and have nonzero product.

This does not apply to an operational contract restricted by fermion-parity
superselection to the even observable algebra.  It therefore does not prove a
fermion/compiler no-go for the framework.

The spacing-16 translation residual also has a constructive answer at the
**law/code-family** resolution.  A deterministic radius-two classical marker
on the previously blank sites gives all `16^3=4096` offset sectors, while the
27 carrier sites remain arbitrary data qubits.  The local projector family is
unit-translation covariant, invariant under all 24 proper-cubic frames, and
has a unique phase successor across every nearest-neighbor overlap.  One
chosen marker state still breaks unit translation, and no autonomous
preparation from homogeneous translation-invariant input is constructed.

Thus `C_local` is narrowed twice, not closed.  There is no axiom pressure.

## 1. Finite, open, periodic, and infinite parity bookkeeping

Let `N=L^3` be the number of coarse cells.  The Cycle-232 scalar-reference
graph has seven fermion vertices and 24 owned graph edges per periodic cell.
The ordinary superfast code represents the even sector of the seven-mode
graph.  Reference equality has rank `N-1`, so the resulting logical count is

```text
(7N-1) - (N-1) = 6N.
```

The count alone does not say which matter parity sectors occur.  If the common
reference parity is `b`, the finite identity is

```text
P_matter b^N = +1.
```

Consequently:

| `L` | `N` parity | matter-even multiplicity | matter-odd multiplicity |
|---:|---:|---:|---:|
| 3 | odd | 1 | 1 |
| 4 | even | 2 | 0 |
| 5 | odd | 1 | 1 |

Changing a torus to an open box removes noncontractible Wilson data but does
not change this particular uniform-reference parity equation.  The exact
graph topology is:

| Domain | vertices | edges | full cycle rank | bounded-loop rank | Wilson labels |
|---|---:|---:|---:|---:|---:|
| open `L=3` | 189 | 594 | 406 | 406 | 0 |
| periodic `L=3` | 189 | 648 | 460 | 457 | 3 |
| open `L=4` | 448 | 1440 | 993 | 993 | 0 |
| periodic `L=4` | 448 | 1536 | 1089 | 1086 | 3 |
| open `L=5` | 875 | 2850 | 1976 | 1976 | 0 |
| periodic `L=5` | 875 | 3000 | 2126 | 2123 | 3 |

On a periodic three-torus, the three missing bounded-loop ranks are the three
torus Wilson labels (equivalently the three spin/Wilson labels in this
bookkeeping).  On a simply connected open box they disappear; boundary
conditions replace closed-manifold global identities where relevant.

For the infinite lattice, let `P_Λ` be the product of mode parities in finite
region `Λ`.  If `Λ'` adds at least one mode, then

```text
P_Λ' = P_Λ P_(Λ'\Λ),
||P_Λ' - P_Λ|| = ||P_(Λ'\Λ)-I|| = 2.
```

The runner constructs the products through seven modes and obtains
`[2,2,2,2,2,2]`.  Hence the canonical finite total-parity products are not a
norm-Cauchy sequence in the quasi-local CAR algebra.  Infinite-volume states
are positive functionals on that quasi-local algebra; a chosen representation
may carry a parity sector without a bounded local observable equal to total
parity everywhere.

Araki and Moriya formulate infinite fermion lattice systems precisely as CAR
`C*`-dynamical systems, emphasize that disjoint full local algebras do not
tensor-commute, and treat even interactions and translation-invariant
dynamics directly:
[arXiv:math-ph/0211016](https://arxiv.org/abs/math-ph/0211016),
[Rev. Math. Phys. 15, 93 (2003)](https://doi.org/10.1142/S0129055X03001606).
This source supports the algebraic formulation; it is not a physical `M_2`
state compiler.

## 2. Full graded net, even observable algebra, and state isometry

For two odd Majoranas `γ_x,γ_y` at distinct fermion sites,

```text
{γ_x,γ_y}=0,
||[γ_x,γ_y]||=2.
```

If a radius-`R` tensor-local bosonic morphism sent each to a physical operator
within its `R`-ball, sites separated by more than `2R` would have disjoint
images.  Those images commute.  Since each Majorana is a unitary, their
physical anticommutator has norm `2`, contradicting preservation of the CAR
product.  The runner instantiates the exact two-mode matrices and repeats the
geometric witness at `R=0,1,2,4`.

Parity-even operators are different.  Even operators in disjoint regions
commute exactly; the runner verifies a four-mode representative with zero
commutator.  All factors of the Cycle-230 update—onsite coin, FSWAP transport,
and occupation-polynomial contact—are parity even.  Therefore the odd-field
contradiction does not reject the actual update algebra.

A state-only Hilbert isometry without an operator-locality condition is also
not excluded: occupation-basis/Jordan-Wigner identification is an isometry.
It is nonlocal at the update-operator interface and does not satisfy the
compiler contract.  Conversely, a local observable map need not provide a
bounded causal map that prepares its code states.

### Guaita theorem: exact hypotheses and scope

Tommaso Guaita, “On the locality of qubit encodings of local fermionic modes,”
*Quantum* **9**, 1644 (2025),
[doi:10.22331/q-2025-02-25-1644](https://doi.org/10.22331/q-2025-02-25-1644),
[arXiv:2401.10077](https://arxiv.org/abs/2401.10077), proves two relevant graph
theorems.

1. **Theorem 1** concerns a finite connected locality graph.  An exact local
   encoding represents the even generators `A_jk` on graph edges and `B_k` on
   vertices on the **full** tensor-product Hilbert space, with each
   representative supported only at its incident sites and with all fermionic
   algebra and cycle relations exact.  Such an encoding exists iff the graph
   is a tree.  This is graph-general, not a theorem restricted to 2-D or 3-D.
   Both the scalar-reference graph and the Cycle-230 six-mode matter graph
   contain many cycles, so they fall on the negative side of these precise
   hypotheses.
2. **Theorem 2** concerns a local **block** encoding whose fermionic relations
   need hold only on a code subspace.  If the graph contains an “8-shaped”
   subgraph—three edge-disjoint paths with common endpoints—of size `d`, no
   state in that code subspace can be prepared from a product state by local
   two-body unitaries of depth at most `d`.  The paper gives
   `d=floor((L-2)/4)` for an open `L×L` square lattice.  The runner verifies
   two fixture-specific embeddings.  First, each coordinate plane of the
   scalar-reference graph contains the literal square theta/8-shaped paths.
   Second, the Cycle-230 six-mode matter graph tiles each coordinate plane by
   8-edge plaquettes: four intercell stream edges and four intracell
   nonopposite turns.  The runner explicitly lifts all three square-theta paths
   into that matter graph, inserting at most one port mode when a straight
   passage encounters opposite ports; their only shared vertices are the two
   endpoints.  Every edge in either full fixture graph changes the coarse-cell
   coordinate by at most one, so the central-corridor separation and hence the
   Definition-5 size remain `Omega(L)` despite spokes or intracell shortcuts.
   The held-size reference value is `0` at `L=3,4,5` and becomes `1,2,3,4` at
   `L=6,10,14,18`; the held sizes alone do not demonstrate the asymptotic.

   Applying that asymptotic statement to bounded-radius physical blocks is a
   fixture-specific coarse-graining inference, not text of the theorem:
   constant overhead and constant block radius can change those graph
   distances and the resulting depth coefficient only by a fixed factor.

Theorem 2 assumes product input and local two-body **unitary** circuits.  The
paper explicitly leaves local measurements plus feedforward as a possible
faster preparation route.  A nontrivial locality-preserving QCA/isometry that
is not a bounded-depth unitary preparation circuit is also outside this stated
theorem.  It also does not say that an algebraic sector representation fails
to exist.  Cycle 237 makes none of those promotions.

## 3. Exact-bosonization flux logic

Yu-An Chen, “Exact bosonization in arbitrary dimensions,” *Phys. Rev.
Research* **2**, 033527 (2020),
[doi:10.1103/PhysRevResearch.2.033527](https://doi.org/10.1103/PhysRevResearch.2.033527),
[arXiv:1911.00017](https://arxiv.org/abs/1911.00017), gives a local kinematic
duality from the parity-even fermionic algebra in `n` spatial dimensions to an
`(n-1)`-form `Z_2` gauge theory with modified Gauss law.  It requires a spin
structure.  In 3-D its dictionary contains

```text
W_t = product_(faces f in boundary t) Z_f  <->  P_t,
U_f                                             <->  fermion hopping S_f,
product_t W_t = I                              <->  product_t P_t = +1
```

on the closed finite manifold used by the construction.  Thus the cited
closed-manifold duality is an **even-total-parity** duality, not a simultaneous
local encoding of the full finite Fock space.

The runner instantiates the cubic incidence version on periodic `L=3,4,5`.
There are `3L^3` faces; each face belongs to exactly two cells, the product of
all cell fluxes is identity, and the cell-flux incidence rank is `L^3-1`.
A product of face flips along a dual path has exactly two flux endpoints.  At
separations `1,2,4,8`, the shortest displayed string uses `1,2,4,8` faces.

On an open box a string may terminate at the boundary.  On the infinite
lattice every finite-support string still has an even number of endpoints; a
single flux/fermion is a superselection excitation represented by a string to
infinity or by changing representation sector.  It is not locally creatable
from the vacuum by a bounded operator.  Likewise, two distant occupied sites
can be represented but a preparation from vacuum carries a connecting face
string whose support grows with separation.  Exact bosonization therefore
supports a local even-algebra duality while independently rejecting a bounded
endpoint-factorized state preparation.

The spin structure and the three periodic Wilson labels remain boundary data.
The untwisted label is proper-cubic invariant, but choosing it is not a local
state encoder.  Open and infinite formulations remove the three torus labels,
not the sector/preparation distinction.

## 4. Superselection and the one-particle/rank-73 fixtures

The one-particle fixture has odd parity.  The Cycle-230 principal sea has rank
73 and is also odd.  All tested update gates preserve parity.  Therefore both
fixtures can be evaluated in one odd sector representation; no local update
needs to query, transport, copy, or broadcast total parity.

This is the exact sense in which superselection can remove the scalar
reference **runtime parity bus**.  It does not provide one bounded isometry
from the full Fock Hilbert space into one finite bosonic code:

- the vacuum is in the even sector;
- coherent even/odd superpositions are excluded by the superselection stance;
- creating the one-particle or rank-73 sector from the even vacuum requires a
  fermionic reservoir, a boundary/string endpoint, or supplied odd-sector
  preparation; and
- on a closed finite torus Chen's exact bosonization sector has total parity
  even, so an odd fixture requires a compensating excitation or a different
  sector construction.

Vidal et al., “Quantum Operations in an Information Theory for Fermions,”
[arXiv:2102.09074](https://arxiv.org/abs/2102.09074), formulate parity
superselection as block-diagonal physical states, observables, and operations.
This is primary support for the contract split, not authority to alter the
framework's current state space silently.  Adopting parity superselection as
the physical operational contract would be an explicit falsifiable framework
choice.

## 5. Unit-translation-covariant spacing-16 marker

The original carrier motif has 27 active residues in a `16^3=4096` physical
period:

```text
12 octahedral carriers
 6 scalar-matter spokes
 3 scalar-bond midpoints
 6 matter-stream repetition carriers
```

The other 4069 M2 sites were blank routing sites.  Cycle 237 assigns a fixed
classical marker bit to every blank residue and treats every active residue as
an arbitrary data wildcard.  The marker is generated with deterministic seed
`237000`, constant on each of the 200 proper-cubic point orbits in
`(Z/16Z)^3`.  Hence the marker and carrier wildcard set are invariant under all
24 proper-cubic frames.

For every phase `s in (Z/16Z)^3`, translate the marker and wildcard pattern by
`s`.  A radius-two neighborhood contains `5^3=125` physical M2 sites.  The
runner proves:

| Test | Exact result |
|---|---:|
| translated local subspaces | 4096 |
| pairwise ambiguous phase pairs | 0 |
| maximum data wildcards in one radius-two window | 12 |
| proper-frame template tests | 98,304 |
| proper-frame mismatches | 0 |
| directed neighbor phase tests | 12,288 |
| missing intended successors | 0 |
| extra compatible successors | 0 |
| active/marker collisions | 0 by wildcard construction |
| marker-one sites among the 4069 fixed blanks | 2092 |
| unit-shift Hamming distances for one chosen sector | 2184, 2184, 2184 |

The diagonal radius-two projectors therefore commute and locally enforce one
globally consistent translated phase on each connected lawful configuration.
The physical update can decode roles from the local marker window, act on the
27 data residues, and leave marker qubits fixed.  No host chooses a physical
origin during the update, and a physical unit translation permutes lawful
sectors exactly.  Proper rotations act within the same allowed family.

This construction has sharp costs and limits:

- physical-site overhead is still the existing spacing-16 block: 4096 M2
  sites per 27 carrier qubits; it adds no sites but fixes all 4069 blanks;
- constraint support is a radius-two, 125-site neighborhood;
- the local rule contains a supplied 200-orbit marker word and 4096 phase-role
  templates;
- the 4096 sectors form a direct-sum/code orbit, not 4096 independent compiler
  copies—literal overlay would demand 27 carrier roles per physical residue;
- a single selected marker product state is not unit-translation invariant;
  only the law/code family, the equal sector mixture, or a symmetry-restored
  sector superposition is invariant; and
- translation-covariant deterministic dynamics maps a translation-invariant
  input state to a translation-invariant output state, so it cannot select one
  definite symmetry-broken offset without supplied boundary/realized-state
  data, stochastic/measurement branching, or spontaneous sector selection.

Thus the old period-16 origin is no longer a preferred-site requirement of the
**law**.  Marker-sector preparation and why one realized history occupies a
particular crystal sector remain open and are not renamed physical time or a
Record.

## 6. Contract disposition

Cycle 237 supports the following precise disposition:

1. **Retire the claim that finite total parity must appear as a quasi-local
   infinite observable.**  The finite products have norm gap 2 and no
   quasi-local limit by this construction.
2. **Retain a local even-algebra route.**  Exact bosonization and the BKSF
   update algebra both show why parity-even dynamics can remain bounded.
3. **Reject a full graded bounded-radius net morphism.**  The remote odd-field
   contradiction is exact at that resolution.
4. **Do not equate algebra duality with a state encoder.**  Flux strings and
   Guaita's block-code theorem keep preparation nonlocal under their stated
   hypotheses.
5. **Represent the two odd fixtures sectorwise without a runtime bus.**  Do
   not claim bounded preparation from the vacuum.
6. **Retain the marker as a constructive compiler component.**  It gives a
   covariant law/code family, not a selected translation-invariant state.

The equation

```text
E G_coarse = G_physical E
```

is still not established for a bounded causal state encoder `E`.  Cycle 237
does not rerun the mass/contact/seam matrices because it changes no parity-even
update matrix; Cycles 230, 232, and 234 remain the regression authorities for
those conditional fixtures.

## 7. Supplied-structure and novelty inventory

Supplied here:

1. parity superselection as an audited alternative operational contract;
2. a chosen even or odd infinite-volume representation/sector;
3. boundary/reservoir/string data if an odd sector is prepared from vacuum;
4. spin structure and three Wilson labels on a periodic torus;
5. Chen's triangulated higher-form gauge presentation if used;
6. spacing 16 and the existing 27 carrier residues;
7. the seed-237000 proper-cubic marker word;
8. all 4096 translated marker sectors and radius-two local projectors;
9. local role-decoder/update lookup and static marker preservation; and
10. marker-sector initial/boundary/realized-state selection if one sector is
    required.

This cycle does not claim a new general fermion-to-qubit theorem.  Its new
fixture-specific results are the exact infinite/finite contract split, the
closed/infinite flux-state accounting applied to the one-particle and rank-73
fixtures, and the executable proper-cubic radius-two marker for the exact
27-residue layout.  Thirring machinery is not used.

## 8. TOE dependency ledger

| Wall | Cycle-237 effect | Remaining dependency |
|---|---|---|
| `C_ref` | marker sector and fermion sector are exposed as preparation/reference data | physical sea, phase origin, and realized sector selection remain supplied |
| `C_num` | finite global parity bus is demoted to a route artifact; odd fixtures share a superselection sector | the framework has not derived parity superselection or a physical fermionic reservoir |
| `C_wrap` | spin/Wilson and marker sectors are separated cleanly from time | none is a clock, elapsed time, winding history, or rate |
| `C_int` | unchanged | the supplied contact remains represented only conditionally; selection and protection remain open |
| `C_local` | materially narrowed | local even algebra and covariant marker family exist; bounded state encoding/preparation and exact 3-D fixture compiler remain open |
| `C_source` | unchanged | no energy, stress, action, or gravitational source is selected |

Maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, Born/probability `1/5`.  The marker
is compiler structure, not a Record; the circuit/string depth is not physical
time; no occurrence probability is derived.

## No-Go Discipline Gate

The fresh `origin/main` no-go procedure was applied.  **N1–N8 PASS** for the
narrow full-graded-net contradiction and for Guaita's unitary-preparation
consequence under its exact hypotheses.  **N1–N8 FAIL** for a broad fermion
compiler impossibility, an even-algebra impossibility, a measurement-assisted
preparation impossibility, uniqueness/minimality, or axiom pressure.

### N1 — alternative-route enumeration

| Route against the narrow negative | Marker | Disposition |
|---|---|---|
| bounded odd-field images with bounded auxiliary/gauge qubits | **ATTEMPTED** | choose sites farther than twice the enlarged fixed radius; disjoint bosonic supports still commute |
| constant-size blocking of physical sites | **ATTEMPTED** | changes the constant radius only; the remote Majorana witness survives |
| spin/Wilson labels or a local port gauge | **ATTEMPTED** | these change sector/presentation data but not commutation of disjoint tensor factors |
| exact higher-form bosonization | **ATTEMPTED** | successfully maps the even observable algebra; it evades rather than refutes the full-graded premise and exposes flux strings for states |
| parity-superselected sector representation | **ATTEMPTED** | removes odd fields from the physical observable contract and carries both odd fixtures; it is a live partial closure, not a full-graded morphism |
| nonlocal Jordan-Wigner or face string | **RULED OUT BY CONTRACT** | algebraically works but violates bounded radius |
| native fermionic physical sites | **RULED OUT BY CONTRACT** | would preserve graded locality but changes the bosonic `M_2` target |
| local measurements plus feedforward for block-state preparation | **LIVE, NOT RULED OUT** | Guaita explicitly leaves this route open; it does not repair a full-Hilbert exact local operator encoding |

The live even-sector and measurement routes block every broader negative.

### N2 — wall-independence audit

The raw conditions collapse to four:

- `W_graded`: whether the contract includes odd CAR fields or only physical
  even observables;
- `W_prepare`: whether a code-sector state must arise by bounded unitary
  preparation from clean product auxiliaries;
- `W_spin`: periodic spin/Wilson boundary data; and
- `W_marker`: preparation/selection of one translation-marker sector.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---:|---:|---:|
| `W_graded`, `W_prepare` | no | no | yes |
| `W_graded`, `W_spin` | no | no | yes |
| `W_graded`, `W_marker` | no | no | yes |
| `W_prepare`, `W_spin` | no | no | yes |
| `W_prepare`, `W_marker` | no | no | yes |
| `W_spin`, `W_marker` | no | no | yes |

Finite odd/even volume failure is downstream of the scalar-reference design,
not a fifth independent wall.  The three Wilson labels are one topological
boundary-data condition, not three physics axioms.

### N3 — hidden-condition scan

The mandatory phrase scan is resolved as follows:

| Potential hidden phrase/condition | Classification |
|---|---|
| “by construction” of the marker | avoided as authority; seed, orbit rule, radius, wildcard set, and projector costs are explicit supplied structure |
| “standard” parity superselection | not silently assumed; it is an explicit alternative contract supported by a primary source |
| “background” spin structure | explicit `W_spin` boundary data |
| clean product auxiliaries/local two-body unitaries | explicit hypothesis of the Guaita preparation result |
| infinite sector at spatial infinity | explicit representation/boundary condition, not a quasi-local observable |
| translation-invariant state | explicitly distinguished from a translation-covariant law/code family |

No schedule is called time, no flux is called energy, and no marker copy is
called a Record.

### N4 — residual matching

| Witness | Witness residual | Cycle-237 use | Match? |
|---|---|---|---:|
| Cycle 232 scalar reference | `B_r(x)=P_matter`, odd-size state isometry, even-size loss | tests whether the finite parity carrier survives quasi-locally | yes |
| Cycle 234 `C_local` residual | bounded all-size `E`, spin sector, and translation marker open | attacks precisely sector/state and marker parts | yes |
| Araki–Moriya 2003 | quasi-local CAR dynamics and non-tensor local structure | supports infinite algebra formulation only | yes, scoped |
| Guaita 2025 Theorem 1 | full-Hilbert exact local encoding iff tree | used only for the cyclic full-Hilbert encoding claim | yes |
| Guaita 2025 Theorem 2 | block-code product-to-code unitary depth lower bound from 8-shaped subgraph | used only for bounded unitary preparation | yes |
| Chen 2020 | local even-sector bosonization with modified Gauss law and spin structure | supports even-algebra route and flux/string state distinction | yes |
| Cycle-237 marker runner | period-16 origin under unit physical translations | constructs a translation-orbit code for that exact residual | yes |

No source is cited as proving the full Cycle-230 compiler equation.

### N5 — rhetoric and resolution audit

| Resolution | Tested | Not established |
|---|---|---|
| two remote odd fields | exact full-graded contradiction | even-algebra failure |
| disjoint even observables | zero commutator | a complete 3-D fixture map |
| finite scalar reference | `L=3,4,5`, open/periodic topology | alternative all-size reference code |
| quasi-local parity product | norm gap 2 under every finite enlargement | all possible representation-sector implementers |
| exact bosonization flux | closed product identity and finite-string endpoints | bounded odd-sector state preparation |
| block-code unitary preparation | Guaita hypotheses and growing square subgraphs | measurement/feedforward preparation |
| marker local projector | radius 2, all 4096 phases, 24 frames, unique overlaps | dynamical nucleation/selection from homogeneous input |
| code-family translation | exact sector permutation | invariance of one chosen sector state |

Every negative is stated at the narrow tested resolution.

### N6 — partial-closure paths

| Path | Status | What it closes |
|---|---|---|
| parity-superselected operational contract | explicit alternative, not adopted silently | removes the unphysical demand to localize odd fields and lets both odd fixtures share one sector |
| infinite quasi-local state functional | algebraically available | removes the finite product-parity observable, not state preparation |
| Chen exact bosonization | primary-source construction | supplies local even observables with spin/gauge data; leaves state strings/sectors |
| measurement/feedforward gauge-code preparation | live | may evade Guaita's unitary-depth hypothesis |
| open boundary or physical fermion reservoir | live supplied resource | can terminate a flux string and prepare an odd sector |
| radius-two translation marker | constructed here | removes a privileged physical origin from the law/code family |
| symmetry-restored mixture/superposition of marker sectors | unbuilt operationally | could give a translation-invariant state while retaining local sector decoding |

These are import-retirement and constructive routes.  No new axiom is
requested.

### N7 — steelman

> A hostile reviewer should reject any broad no-go here.  The actual Cycle-230
> dynamics is parity even, and Chen gives an exact locality-preserving
> bosonization of precisely that observable class in arbitrary dimension.
> Infinite CAR theory has no quasi-local total-parity product, so the uniform
> scalar bus is not fundamental.  The one-particle and rank-73 fixtures occupy
> the same odd superselection sector and do not require a runtime parity query.
> Guaita's state-depth theorem assumes local two-body unitaries from product
> input and explicitly leaves measurement/feedforward open.  Finally, the
> executable marker proves that unit-translation covariance of the law can be
> restored with local M2 constraints.  What remains is a hard state-sector and
> preparation compiler, not evidence that bosonic M2 cannot carry operational
> fermion physics.

This steelman is convincing and blocks a broad no-go or axiom claim.

### N8 — cross-cycle echo

Repository searches for prior no-go/wall language and `NO_GO_LEDGER.md` files
were rerun.  The exact relevant echoes are:

| Earlier cycle | Earlier boundary | Mechanism applied here |
|---|---|---|
| Cycle 229 | finite spectral Fock matrices are not a spatial compiler | retain algebra/state/interface separation |
| Cycle 230 | intrinsic CAR/contact stops before physical M2 state compiler | attack only the parity/translation sub-residuals |
| Cycle 232 | local gauge update gates coexist with nonlocal scalar-reference state isometry | replace finite total parity by sectorwise infinite algebra, but retain preparation wall |
| Cycle 234 | exact bosonization, infinite volume, and translation marker remained live | instantiate their flux logic and a concrete marker |
| prior macrocompiler campaigns | supplied periodic roles can become local code/admissibility data | use a local marker orbit rather than call the pattern a new axiom |

The same constructive-retirement mechanism that closed earlier implementation
gaps is live here.  A no-go remains premature.

## Verification

```text
python3 scripts/ROUTE6_INFINITE_EVEN_CAR_TRANSLATION_MARKER_CYCLE237_2026_07_17.py
```

Expected result: all checks pass.  The runner is deterministic and uses only
the Python standard library plus NumPy already used by the retained science
runners.
