# State-local fermionization and topological-sector tournament — Cycle 238

**Date:** 2026-07-17

**Type:** adversarial synthesis of three constructive follow-on routes with a
theorem-scoped state-preparation boundary

**Status:** local parity-even dynamics and a covariant physical code family
are constructible; no route supplies the full compiler because state/sector
preparation remains nonlocal or incomplete

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

**Packaging:** existing draft PR #5389 on the parking branch only

Companion runner:

```text
scripts/state_local_fermionization_topological_sector_tournament_cycle238_2026_07_17.py
```

This note and runner change no axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit surface.

## Result up front

The post-Cycle-234 campaign has located the physical content of the remaining
compiler wall more sharply.

The six-mode Cycle-230 fermion cell can be represented by bounded physical
`M_2` operators in three independent ways:

1. A square-pyramid higher-form code gives the exact local parity-even algebra
   with 15 face qubits per coarse cell, bounded Gauss constraints, and exact
   proper-cubic covariance.  On a closed domain it has only total-even parity,
   so the one-particle mass state and odd rank-73 sea are absent.
2. Farrelly–Short auxiliary Majoranas retain both matter parities, the mass
   fixture, and the seam block.  Their dressed stream has maximum dressed
   update weight `14` at `L=3,4,5`.  The literal Jordan–Wigner link constraints,
   initialization, and qubit-frame action grow with system size.
3. Infinite even-CAR sector bookkeeping removes the need to treat finite total
   parity as a quasi-local runtime observable.  A radius-two marker also makes
   the entire spacing-16 law/code family unit-translation and proper-cubic
   covariant.  An odd superselection sector and one marker crystal sector
   still have to be prepared or selected.

No one of these is the requested local state encoding `E`.  Passing pieces
from different routes cannot be spliced together and called an intertwiner.
The full identity

```text
E G_coarse = G_physical E
```

therefore remains unestablished under the frozen bounded-state contract.

The evidence does support one shared conditional state-preparation
obstruction.  Guaita's theorem applies to a local fermionic block encoding on
a graph with growing overlapping loops: no code state can be prepared from a
product input by a bounded-depth circuit of local two-body unitary gates.  The
Cycle-230 six-mode graph contains explicit growing overlapping-loop
subgraphs.  Constant physical blocking changes only the constant in that
depth bound.

That is not a full compiler no-go.  Measurement plus feedforward remains
live, a nontrivial locality-preserving QCA/isometry remains live, and the
distinguishable-walker antisymmetric sector remains live.  An algebraic
superselection-sector representation also exists at a different resolution.
The theorem creates **contract pressure**—the framework must say what kind of
state encoder and preparation it physically requires—but not axiom pressure.
There is no axiom pressure from this campaign.

The strongest physics reading is constructive: operational fermions on a
bosonic `M_2` substrate are naturally topological/long-range-entangled code
excitations, not independent onsite tensor factors.  This is a testable
structural consequence if the framework adopts the parity-even operational
contract.  It does not derive CAR statistics, select a spin sector, or explain
how the required entangled sector is realized.

## Route-by-route disposition

| Route | Strongest exact result | Load-bearing failure | Disposition |
|---|---|---|---|
| Cycle 235 higher-form | square-pyramid dual graph exactly matches six modes; `15N` face qubits; bounded weights `5,9,28`; all 24 frames and group law | closed identity `product W_t=I`; code exponent `6N-1`; odd mass/sea states absent | retain as strongest local even-algebra compiler |
| Cycle 236 auxiliary Majorana | all `6N` matter logical qubits and both parities; FSWAP residual `3.2078929115721493e-16`; update weight 14; mass/seam retained | site-major `M_e` weights `216,576,1200`; preparation about `36N^2`; link-major update weights `112,292,604`; JW frame mismatch grows | retain as strongest conditional all-parity update compiler |
| Cycle 237 infinite/marker | finite parity products have norm gap 2; both odd fixtures share a sector; 4096 marker phases locally decoded at radius 2 with zero ambiguity/covariance/successor failures | sector state is supplied; closed odd flux needs boundary/string; one marker state breaks translation | retain even-sector interpretation and covariant law/code family |

The positive surfaces answer different questions.  Cycle 235 has local
constraints but not the odd sector.  Cycle 236 has the odd sector and exact
fixtures but not local constraints or local initialization.  Cycle 237 has a
covariant admissibility family but not the fermionic state isometry.  Their
union is an architecture agenda, not one constructed `E`.

## Exact combined controls

### Higher-form face code

For `N=L^3`, the square-pyramid cellulation has

```text
primal vertices       2N
primal edges         11N
face qubits          15N
fermion 3-cells       6N
```

The executable ranks are:

| `L` | face qubits | local Gauss rank | Wilson-fixed rank | code exponent | full Fock exponent |
|---:|---:|---:|---:|---:|---:|
| 3 | 405 | 241 | 244 | 161 | 162 |
| 4 | 960 | 574 | 577 | 383 | 384 |
| 5 | 1875 | 1123 | 1126 | 749 | 750 |

Every face occurs in two 3-cells on the closed torus.  Consequently
`product_t W_t=I` at all three sizes.  The difference of one logical qubit is
the total-even restriction, not a capacity accident.  The code exactly maps
local even operators, but no odd state has an image in that closed sector.

### Auxiliary-Majorana update code

The Farrelly–Short instantiation has six matter and six auxiliary endpoint
modes per cell.  The `M_e=+1` and odd-link-parity constraints have ranks
`162,384,750` at `L=3,4,5`, leaving exactly `6L^3` logical matter qubits.
Global matter parity is an independent commuting logical operator at every
size, so both sectors occur.

The same site-major Jordan–Wigner presentation gives:

| `L` | max dressed update weight | max `M_e` constraint weight | Appendix-G prefix touches |
|---:|---:|---:|---:|
| 3 | 14 | 216 | 26,811 |
| 4 | 14 | 576 | 148,800 |
| 5 | 14 | 1,200 | 565,125 |

Thus runtime locality does not imply state/constraint locality.  Making each
auxiliary pair adjacent changes `M_e` to weight 2 but returns a growing string
to the update.  This is an exact tradeoff in the tested presentation, not a
theorem against every gauge presentation.

### Infinite sector and marker code

Finite parity products enlarged by one mode have exact norm difference 2 and
are not norm-Cauchy.  Infinite quasi-local dynamics therefore needs no bounded
observable that broadcasts total parity.  The odd one-particle and rank-73
fixtures can live in the same odd representation sector because all
Cycle-230 updates are parity even.

For the physical layout, all 27 data residues of the spacing-16 macrocell are
wildcards.  A proper-cubic marker word fixes the other 4069 residues.  Its
radius-two, 125-site templates give:

```text
offset sectors                 4096
ambiguous phase pairs             0
proper-cubic template tests   98,304
frame mismatches                   0
neighbor successor tests      12,288
missing/extra successors           0 / 0
```

The local law admits all translated sectors and contains no preferred
physical origin.  Choosing one sector is spontaneous/boundary/realized-state
data; it is not performed by the marker rule itself.

## What the shared theorem does and does not establish

The relevant locality graph has one vertex for every fermion mode, onsite
edges for the dense six-mode coin/even algebra, and stream edges between
neighboring cells.  The Cycle-237 runner constructs `36,108,240` explicit
eight-edge coordinate-plane plaquettes at `L=3,4,5`, and growing three-path
theta/8-shaped subgraphs at `L=6,10,14,18`.  Every graph edge changes a coarse
coordinate by at most one, so their corridor separation grows with `L` even
after bounded onsite shortcuts.

Tommaso Guaita, [“On the locality of qubit encodings of local fermionic
modes”](https://arxiv.org/abs/2401.10077), proves:

- an exact full-Hilbert local representation of all even generators on the
  same tensor-product graph exists only for a tree; and
- for a local block encoding containing an 8-shaped subgraph of size `d`, no
  state in the code can be obtained from a product input by a circuit of local
  two-body unitary gates of depth at most `d`.

The second result applies to every candidate route that interprets the frozen
bounded state `E` as a fixed-depth local unitary initialization of a local
block code.  It explains why higher-form constraints, auxiliary link states,
and superfast loop codes repeatedly move nonlocality into their code state.

The theorem does **not** cover:

- measurement plus feedforward and outcome-dependent correction;
- a nontrivial locality-preserving QCA/isometry not realizable by a bounded
  depth circuit;
- a state functional already supplied in a superselection sector;
- a physical boundary, reservoir, or puncture;
- a target with native fermionic sites; or
- the distinguishable-walker antisymmetric sector unless it satisfies the
  theorem's local block-code hypotheses.

These exclusions are active construction routes, not rhetorical loopholes.
Cycles 239–241 test the three most relevant ones independently.

## Full graded fields versus physical even observables

There is a separate exact statement that must not be confused with the
preparation theorem.  If odd Majoranas were required to have bounded-radius
images in the ordinary bosonic tensor net, two sufficiently distant images
would commute, while the original odd fields anticommute.  The commutator
norms are respectively `0` and `2`.  Hence the **full graded local net** has
no bounded-radius tensor-bosonic morphism.

The Cycle-230 update is parity even.  Disjoint even CAR observables commute,
and exact higher-form bosonization maps them locally.  Therefore the remote
odd-field contradiction is not a no-go against the update that this campaign
actually needs.  It instead forces a physical choice:

1. require odd field operators as local observables, which is incompatible
   with the bosonic tensor target at bounded radius; or
2. adopt parity superselection and treat fermions as sector excitations of a
   local even observable algebra.

The framework has not yet derived or adopted option 2.  It remains explicit
supplied operational structure under `C_num`/`C_ref`.

## Physics fixtures

The best all-parity conditional representation retains:

| Fixture | Result | Qualification |
|---|---:|---|
| dressed link FSWAP | `3.2078929115721493e-16` | global auxiliary state |
| held mass relative residual | `3.68005641515623e-08` | one-particle odd sector |
| sea rank | `73` | supplied principal sea |
| seam singular values | `0.49577141, 0.45566605` | conditional global isometry |
| direct seam residual | `7.163369603754572e-18` | inherited finite fixture |
| all-24 seam residual | `1.2947314098277875e-15` | inherited proper-cubic frame test |
| ideal constraint leakage | `0` | fixed auxiliary sector |
| contact deletion at `g=0` | `0` | exact |

The higher-form route represents the same parity-even update operators but
cannot evaluate these odd-sector state fixtures on its closed code.  The
infinite route makes an odd sector algebraically legitimate but does not
construct its physical `M_2` state.

## Spatial-dimension and time firewall

The Lattice axiom supplies the three-dimensional spatial adjacency used by
all square-pyramid, link, flux, and marker constructions.  None of this work
derives three spatial dimensions.

Gate order, marker successor, face-string length, circuit depth, update
layer, macrocell phase, and feedforward round are compiler control variables.
They are not physical time, not a clock, not an elapsed tick, not a rate, and
not a winding history.  Any bridge to the separate causal-time derivation
must be explicit.  The kinetic-isotropy primitive `c_t=c_s` does not turn a
compiler schedule into time.

## Supplied-structure inventory

The combined architecture still supplies:

1. CAR statistics and parity-even operational restriction if used;
2. a chosen even/odd representation, reservoir, boundary, or flux endpoint;
3. the square-pyramid cellulation and its face-qubit presentation;
4. local port order, framing gauge, and Hermitian-log branches;
5. spin structure and Wilson/topological sector;
6. auxiliary Majorana endpoints, link parity, and preparation-factor order;
7. the marker word, 4096 phase templates, and one realized crystal sector;
8. spacing, routing, blanks, gate coloring, and code preparation;
9. the Cycle-219 coin/mass interpretation; and
10. the Cycle-230 contact, coupling, sea, and update order.

No item is silently attributed to the scale-reference, kinetic-isotropy, or
realized-state primitives.  Realized state provides a pointwise evaluation
slot, not a mechanism selecting the fermion or marker sector.

## TOE dependency ledger

| Wall | Cycle-238 effect | Remaining dependency |
|---|---|---|
| `C_ref` | sector selection is now explicit rather than hidden in a parity bus or macro origin | physical sea, odd-sector reservoir/boundary, spin sector, marker sector, and preparation remain supplied |
| `C_num` | finite uniform parity carrier is demoted as an infinite-volume necessity | parity superselection and the physical meaning of fermion number are not derived |
| `C_wrap` | unchanged; Wilson, marker, circuit depth, and feedforward labels are not time | phase/winding-to-clock bridge remains open |
| `C_int` | strong representation gain | the supplied contact survives the all-parity conditional route; selection, coupling value, rate, and protection remain open |
| `C_local` | materially narrowed | local even update algebra, bounded physical supports, and covariant marker family exist; no bounded causal all-sector state `E` combines local constraints, fixtures, and preparation |
| `C_source` | unchanged | no physical energy, stress, action, or gravitational source is selected |

Maturity remains:

| Lane | Score | Reason |
|---|---:|---|
| operational quantum / records | `2/5` | local channels and code constraints exist conditionally; no intrinsic code-sector formation or Record law |
| time | `1/5` | compiler controls remain separate from the causal-time bridge |
| inertia / matter | `3/5` | mass and contact fixtures survive one conditional all-parity representation; physical sector formation remains open |
| gravity / source | `2/5` | no source ledger changes |
| Born / probability | `1/5` | measurement-assisted preparation is only a live route and supplies no outcome weights |

These are maturity judgments, not probabilities.

## No-go discipline gate

The fresh no-go procedure and primitive-registry check were applied.

**N1–N8 PASS** for two narrow conclusions:

1. the full graded CAR net cannot have bounded-radius images in disjoint
   bosonic tensor factors; and
2. a local block-code state cannot be prepared from product input by bounded
   depth local two-body unitary circuits on the growing Cycle-230 graph.

**N1–N8 FAIL** for a general even-algebra compiler impossibility, a
measurement-assisted impossibility, a QCA/isometry impossibility, uniqueness,
minimum content, or axiom pressure.

### N1 — alternative-route enumeration

| Route | Marker | Disposition |
|---|---|---|
| exact 3-D higher-form face code | **ATTEMPTED** | local even algebra and constraints pass; closed odd sector absent |
| Farrelly–Short auxiliary Majoranas | **ATTEMPTED** | all parities and fixtures pass; constraints/preparation/order grow |
| infinite even-CAR sector | **ATTEMPTED** | runtime parity bus removed; sector preparation supplied |
| translation-orbit marker | **ATTEMPTED** | local covariant law family passes; one sector selection supplied |
| measurement plus feedforward | **LIVE, IN PROGRESS** | outside Guaita's unitary hypothesis; must audit outcome control and Record imports |
| nontrivial locality-preserving QCA/isometry | **LIVE, IN PROGRESS** | outside the finite-depth theorem; must construct both sector and local Heisenberg action |
| distinguishable-walker antisymmetric sector | **LIVE, IN PROGRESS** | variable-number, contact, label, and locality costs untested |
| boundary/puncture/reservoir | **LIVE, TARGET QUALIFIED** | can terminate odd flux but supplies physical boundary/defect data |
| parity-gauged target | **LIVE, TARGET CHANGED** | adds a physical gauge field rather than compiling the original source unchanged |

The live routes block a full no-go.

### N2 — wall-independence audit

The apparent failures reduce to four independent conditions:

- `K_grade`: whether odd fields or only even physical observables are in the
  compiler contract;
- `K_prepare`: how a long-range-entangled local block-code state is formed;
- `K_sector`: which parity/spin/Wilson sector realizes the mass and sea; and
- `K_marker`: how one translated crystal sector is realized.

None closes another.  Removing odd observables does not prepare a gauge code.
A gauge-code preparation does not select the odd sea.  A spin sector does not
select a marker phase.  The marker does not derive fermion statistics.  These
are not four axioms and do not replace the six TOE walls.

### N3 — hidden-condition scan

The scan promotes every load-bearing input: product input, unitary-only
preparation, parity superselection, reservoir, boundary, spin structure,
Wilson labels, code state, auxiliary parity, marker word, phase sector,
global mode order, coin, contact, and sea.  “Local” is separately qualified
for observable image, update support, constraint support, state isometry, and
preparation circuit.  No compiler phase is called time and no marker is called
a Record.

### N4 — residual matching

| Prior residual | Cycle-238 match |
|---|---|
| Cycle 230: intrinsic CAR is not physical `M_2` locality | all three routes attack this exact interface |
| Cycle 232: scalar reference moves parity into local/global state relation | infinite route demotes the finite bus but retains sector preparation |
| Cycle 234: exact bosonization and auxiliary Majoranas remained live | Cycles 235 and 236 instantiate both with exact finite controls |
| Cycle 234: macro origin/marker remained supplied | Cycle 237 constructs a local translation-orbit code family |
| Cycle 219/230 odd fixtures | higher-form code misses them; auxiliary route carries them conditionally |

The state-preparation boundary is not inferred from a missing implementation
alone; it is matched to the theorem's graph and preparation hypotheses.

### N5 — rhetoric and resolution audit

| Resolution | Established | Not established |
|---|---|---|
| local even algebra | bounded face/link operator images | full state compiler |
| closed finite parity | exact total-even face identity | odd boundary/sector preparation |
| auxiliary update | all-size weight-14 stream and exact fixtures | local constraints or initialization |
| infinite sector | no quasi-local total parity product | physical sector formation |
| unitary preparation | growing-depth consequence under Guaita hypotheses | measurement/QCA lower bound |
| marker | local radius-two law/code covariance | unique homogeneous sector nucleation |
| proper cubic | exact route-specific operator/family tests | Lorentz/boost symmetry |

Every negative is bounded to its exact resolution.

### N6 — partial-closure paths

The active constructive paths are measurement-assisted syndrome preparation,
a coherent autonomous dilation of that protocol, a nontrivial QCA/isometry,
an antisymmetric-walker code, an explicit odd reservoir/boundary, and a
physical mechanism for spontaneous marker-sector realization.  The approved
primitives select none of them.  They remain work, not premise edits.

### N7 — steelman

> A hostile reviewer should not infer that bosonic `M_2` sites cannot support
> fermions.  Exact bosonization already supplies a bounded local map for the
> physical even algebra, and the auxiliary route carries both parities and all
> named fixtures with bounded runtime gates.  Long-range entanglement of the
> code state is expected for emergent fermions.  Guaita excludes bounded-depth
> unitary preparation from product states on the relevant graph, not local
> measurement protocols, nontrivial QCAs, or a supplied superselection sector.
> The marker construction also removes a preferred origin from the law.  The
> remaining question is how the framework physically forms and selects the
> sector, not whether the local even dynamics can exist.

This steelman is convincing.  It blocks a broad no-go and axiom pressure.

### N8 — cross-cycle echo

Cycle 229 separated Fock matrices from spatial compilation.  Cycle 230 built
the intrinsic CAR/contact mechanism.  Cycles 231–234 found route-specific
ordering, parity, and marker failures.  Cycles 235–237 show that those failures
are different presentations of a deeper algebra/state/preparation split,
while also constructing stronger local operators and a covariant marker.
Earlier repository warnings that local evolution does not imply local state
preparation are therefore sharpened by new executable mechanisms and a
primary theorem; no retired convention supplies the missing sector formation.

## Axiom-pressure and next-campaign decision

There is a route-independent **conditional** obstruction to one interpretation
of `E`: bounded-depth local unitary preparation of a fermionic block-code state
from product physical cells.  It survives direct, gauge, auxiliary, and
higher-form constructions and has theorem-level support on the actual graph.

It does not create axiom pressure because the physical success contract has
not excluded measurement/feedforward, nontrivial QCA isometries, or prepared
superselection sectors, and because the current `M_2` substrate positively
supports local even fermionic dynamics.  The correct response is to test those
escape routes and then decide whether `C_local` should demand local unitary
preparation or instead demand a physical formation law for a topological
sector.  No axiom wording is drafted.

The next campaign is therefore Cycles 239–241:

1. distinguishable walkers with an explicit antisymmetric sector;
2. measurement-assisted local gauge-code preparation and coherent dilation;
3. a nontrivial locality-preserving QCA/isometry audit.

Each must preserve the 3-D/time firewall and must not borrow a global sector,
outcome service, or particle-label ordering without inventorying it.

## Verification

```text
python3 scripts/state_local_fermionization_topological_sector_tournament_cycle238_2026_07_17.py
```
