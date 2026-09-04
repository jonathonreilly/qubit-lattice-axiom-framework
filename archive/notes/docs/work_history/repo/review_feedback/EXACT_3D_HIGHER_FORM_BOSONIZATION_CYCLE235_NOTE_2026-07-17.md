# Exact 3-D higher-form bosonization on the six-mode CAR cell — Cycle 235

**Date:** 2026-07-17

**Type:** primary-source-bounded constructive instantiation with an exact
lawful-domain failure

**Status:** local total-even algebra compiler constructed; full-Fock local
state compiler rejected on closed finite domains

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

**Packaging:** existing draft PR #5389 on the parking branch only

Companion runner:

```text
scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py
```

This note and runner change no foundation, axiom, Qualification, primitive,
registry, policy, queue, or audit surface.

## Result up front

Exact 3-D higher-form bosonization gives the cleanest local **even-algebra**
compiler in the tournament, but it does not give the requested full-Fock,
bounded-radius state encoding `E`.

The constructive geometry is exact.  Subdivide every coarse cube into the six
square pyramids from its center to its boundary faces.  The pyramids are the
six direction modes.  Two nonopposite pyramids share one internal triangular
face, giving the 12 onsite octahedral links.  Matching pyramids in neighboring
coarse cubes share the outer square face, giving the three stream links per
cell.  The dual adjacency graph is therefore precisely the Cycle-230 matter
graph.

The cellulation has, on a periodic domain with `N=L^3` coarse cells,

```text
primal vertices:   2 N   (coarse corners and cube centers),
primal edges:     11 N   (3 N coarse edges and 8 N center-corner spokes),
primal faces:     15 N   (3 N shared squares and 12 N internal triangles),
primal 3-cells:    6 N   (the six matter modes),
Euler:                 0.
```

Put one physical `M_2` factor on every primal face.  Thus the abstract gauge
code uses **15 face qubits per coarse cell**.  The modified Gauss constraints
live on primal edges: eight triangular dual loops per cell surround the
center-corner spokes, and three eight-edge dual loops per cell surround the
coarse cubic edges.  Every constraint has bounded support.

The executable ranks are:

| `L` | face qubits | local modified-Gauss rank | full dual-cycle rank | topological spectators |
|---:|---:|---:|---:|---:|
| 3 | 405 | 241 | 244 | 3 |
| 4 | 960 | 574 | 577 | 3 |
| 5 | 1875 | 1123 | 1126 | 3 |

Three noncontractible Wilson constraints select a spin/topological sector;
these are the three topological spectators before sector selection.
After that selection, the code exponent is

```text
15 N - (9 N + 1) = 6 N - 1.
```

That is exactly the **total-even** six-mode Fock sector and one logical qubit
short of the full `6N`-qubit Fock space.  This is not a runner accident.  On a
closed cellulation the mapped local parity is the cell flux

```text
P_t <-> W_t = product_(f subset boundary(t)) Z_f,
```

and every face belongs to two 3-cells, so

```text
product_t W_t = I.
```

Yu-An Chen's arbitrary-dimensional construction states the same restriction
explicitly: its Eq. (47) imposes total fermion parity `product_t P_t=1`, and
the paper's conclusion defines locality only for local **even fermionic
observables**.  Therefore the published duality supplies a global
spin-sector Hilbert-space isomorphism, which this note calls `J_CK`, not a
bounded-radius state isometry for both parity sectors.

The failure is uniform in size.  At `L=3,4,5`, the vacuum/even sectors exist,
but the one-particle sector does not.  The Cycle-230 principal sea has rank 73
and is also odd, so its entire 2p2h seam block lives in an absent total-parity
sector.  The local coin, `A/B` FSWAP layers, and contact are parity even and
map into bounded gauge operators, but there is no full-code identity

```text
E G_coarse = G_physical E
```

because the required `E` has no image for the odd half of the declared coarse
space.  Consequently this route does not preserve the Cycle-219 one-particle
mass or the Cycle-230 rank-73 contact seam **as a state compiler**, even though
it exactly represents their parity-even update operators.

This is stronger than the scalar-reference route in geometric overhead and
all-size consistency, but weaker in lawful-domain capacity: it cleanly exposes
the standard even-sector boundary rather than hiding parity in a bus.  It
creates no route-independent obstruction and no axiom pressure.

## Primary-source equations and exact scope

Only the two primary construction papers are used.

Chen and Kapustin, [“Bosonization in three spatial dimensions and a 2-form
gauge theory”](https://arxiv.org/abs/1807.07081), define on a 3-D lattice:

```text
P_t = -i gamma_t gamma'_t             <-> W_t = product_(f subset t) Z_f,
S_f =  i gamma_L(f) gamma'_R(f)       <-> U_f,
```

in their Eqs. (5) and (6).  On a triangulation their Eq. (24) is

```text
U_f = X_f product_(f') Z_(f')^[ integral f' cup_1 f ],
```

and their Eq. (30) gives the modified Gauss constraint on each primal edge,

```text
G_e = product_(f superset e) X_f
      product_(f') Z_(f')^[ integral delta(e) cup_1 f' ] = 1.
```

Their Eqs. (37)-(39) expose the second Stiefel-Whitney representative and the
choice of spin structure.  The paper proves locality of the Hamiltonian and
the even-observable algebra; it does not present a bounded-depth state
preparation circuit.

Chen, [“Exact bosonization in arbitrary
dimensions”](https://arxiv.org/abs/1911.00017), gives the same 3-D dictionary
in Eq. (22), the general modified Gauss law in Eqs. (44)-(46), and the explicit
total-even condition in Eq. (47).  Its conclusion says that every local even
fermionic observable maps to a local gauge-invariant bosonic operator.  It
does not say that an arbitrary fermionic tensor-product state has a
bounded-radius encoding circuit.

The mixed square-pyramid cellulation is not printed in either paper.  The
runner therefore does not silently treat the published simplicial/cubic
`cup_1` table as if it had been supplied for this cellulation.  Instead it
instantiates a concrete local framing presentation with the same exact
Majorana-generator algebra:

```text
B_t = product_(f incident t) Z_f,
A_(tt') = epsilon_(tt') X_f
          product_(g <_t f) Z_g product_(h <_(t') f) Z_h.
```

Products of these hopping generators around primal edges are the displayed
modified-Gauss/loop operators.  The runner verifies their phases,
commutation, nonempty code, ranks, update commutators, and topological
completion directly.  Relating this port-order framing to a particular
cellular `cup_1` diagonal is supplied presentation work, not attributed to the
papers.

## Square-pyramid geometry and local constraints

Inside one coarse cube, each center-corner spoke is shared by the three
pyramids pointing toward the three faces meeting at that corner.  Its dual
link is a triangle.  The eight such triangles span rank seven of the 12-edge
onsite octahedral cycle space.

Each coarse cubic edge is shared by four coarse cubes.  Its dual link
alternates:

```text
internal triangle, outer square, internal triangle, outer square,
internal triangle, outer square, internal triangle, outer square.
```

These `3N` octagonal loops complete the bounded local Gauss family.  The
runner first checks every loop has zero graph boundary.  Their rank is
`9N-2`, while the connected dual graph cycle rank is `9N+1`.  The difference
is exactly the three first-homology cycles of the torus.

At `L=3`, the actual 405-qubit Pauli constraints have:

- zero mutual commutator failures;
- zero commutator failures with every mapped hopping generator;
- zero non-Hermitian generators;
- zero `-I` redundant products;
- local rank 241;
- rank 244 after three Wilson constraints; and
- logical exponent `405-244=161=6*27-1`.

The mapped support bounds are volume independent: cell flux weight 5,
hopping weight at most 9, modified-Gauss weight at most 28, and one onsite
even-algebra neighborhood within 18 incident face carriers.  Opposite
direction modes use a two-edge path through a nonopposite mode.  Thus the
entire six-mode onsite even algebra is bounded.

## The state-isometry boundary

The source-level word “duality” must not be upgraded to the campaign's local
state encoding without another theorem.

After choosing a spin/Wilson sector, representation theory gives a global
isomorphism

```text
J_CK : H_Fock,total-even -> H_gauge,Gauss,spin.
```

The primary papers define `J_CK` through the operator dictionary and the
constrained Hilbert spaces.  They do not give a product-of-cells or
bounded-depth circuit for `J_CK`.

In the common `Z`-basis picture, an occupation parity configuration `n_t`
must be represented by face bits whose graph divergence is `n_t`.  Two
separated odd cells therefore require a face string joining them.  The
runner's shortest possible string lengths for separated same-port cells at
`L=3,5,7` are `3,6,9`.  This is an exact lower bound for a basis-diagonal
flux encoder and rules out calling that natural construction bounded radius.
It is not promoted to a theorem against every quantum encoder with a supplied
long-range-entangled resource.

More decisively for this campaign, even an arbitrary global `J_CK` omits the
odd sector.  Possible repairs are all additional structure:

- a boundary or puncture lets total flux escape but supplies a marked defect
  and distance-to-boundary structure;
- a global sector qubit restores dimension but is a parity carrier;
- gauging fermion parity, as in Chen-Kapustin Sec. IV, changes the target
  theory to fermions coupled to a `Z_2` gauge field;
- two copies or auxiliary reference matter reopens the assembly/parity-bus
  obligations; and
- declaring total parity even is a superselection restriction, not the full
  Cycle-230 code space.

No one of these is smuggled into the retained result.

## Proper-cubic covariance and physical placement

The square-pyramid cellulation is invariant under all 24 proper rotations:
rotations permute the six pyramids, the 12 internal faces, the six incident
outer faces, and the two primal-edge constraint orbits.

The raw local incident-face order is a presentation gauge.  The runner
constructs the vertex-local `CZ` inversion repairs and edge-local `Z`
orientation repairs.  All rotated hopping generators, including phases, then
match exactly in all frames.  It additionally checks all `24*24` frame
compositions on every face `X/Z` generator, so the repair is a group action,
not a frame table with a hidden cocycle.

An explicit physical placement uses coarse spacing 16:

```text
internal triangular face (a,b):  2(D_a + D_b)    [12-site orbit],
outer square face along a:        8 D_a            [3 sites/cell after sharing].
```

The centered incident set has 18 sites; sharing the six boundary sites gives
15 physical `M_2` sites per coarse cell.  The set is proper-cubic invariant.

This remains a macrocode.  Periodic `L=3,4,5` patches have respectively
`15L^3` active sites.  A unit physical translation has active-set symmetric
difference `30L^3`, while translation by 16 has zero difference.  Therefore a
period-16 origin/marker, a translation-orbit code, or an autonomous marker law
remains supplied.  The construction does not establish a unit-translation
physical law.

Thus the unit translation audit fails while the macro-translation audit
passes.

## Update, mass, contact, and seam disposition

Every Cycle-230 update factor is even:

1. `Gamma(C)` is a number-conserving onsite even gate;
2. every `A/B` stream factor is an even FSWAP;
3. `W_g` is an onsite occupation polynomial.

The mapped local algebra can therefore represent their Hermitian generators
and exponentiate them to bounded physical unitaries on the gauge code.
Constraint commutators vanish, so ideal even-sector leakage is zero.  Contact
deletion at `g=0` is still identity.

That operator statement is not fixture preservation.  The Cycle-219 mass
fixture uses a single particle, and the Cycle-230 principal sea has occupied
rank 73.  Both are total odd.  Neither belongs to the closed bosonized Hilbert
space.  Hence:

```text
one-particle mass intertwining: unavailable,
rank-73 seam-block intertwining: unavailable,
full-Fock leakage test:          failed by absent lawful sector.
```

The coarse numerical values remain valid predecessor fixtures, but this route
does not reproduce them physically and does not report a zero residual where
no encoded state exists.

## Supplied-structure inventory

The construction supplies:

1. the square-pyramid subdivision of every coarse cube;
2. one face qubit on every internal triangle and shared square;
3. the local incident-face order/orientation and its Clifford gauge;
4. the primal-edge modified-Gauss family;
5. one of eight torus spin/topological sectors;
6. the global total-even Hilbert-space restriction;
7. the spacing-16 physical placement, macro origin, blanks, and routing;
8. a Hermitian-log branch and local gate synthesis for each even update;
9. the Cycle-219 coin and Cycle-230 contact, coupling, and gate order; and
10. code and spin-sector preparation.

The framework does not derive any of these in this cycle.  No layer, circuit
depth, or macrostep is physical time.  No wrapped phase is called energy, and
no source or Record is constructed.

## Prior-art and novelty boundary

Chen-Kapustin supply the 3-D face-qubit duality, framed hopping operators,
modified Gauss law, spin-structure dependence, and local even-Hamiltonian
map.  Chen supplies the arbitrary-dimensional theorem and explicit
total-even condition.  This cycle does not claim a new general bosonization.

The fixture-specific construction is the proper-cubic square-pyramid
cellulation, its exact `2N,11N,15N,6N` census, executable local loop and Wilson
ranks, local framing covariance and group law, physical `15 M_2`-site density,
and direct comparison with the odd Cycle-219/Cycle-230 sectors.  Extending a
specific published `cup_1` table to the mixed cellulation is not claimed as
prior art or as completed geometry.

Thirring machinery is neither used nor compared.

## TOE dependency ledger after Cycle 235

| Wall | Cycle-235 effect | Remaining dependency |
|---|---|---|
| `C_ref` | unchanged | phase origin, physical sea, and preparation remain supplied |
| `C_num` | sharpened | total-even superselection is explicit; full number/parity reference remains unselected |
| `C_wrap` | unchanged | Wilson labels, face strings, and macro translations are not clocks or winding carriers |
| `C_int` | even-algebra representation gain | contact can be mapped within even sectors, but its odd principal-sea fixture is absent; selection/rate remain open |
| `C_local` | strong partial gain | exact 15-site face-gauge architecture and local update algebra; full-parity local `E`, spin selection, and unit marker remain open |
| `C_source` | unchanged | no conserved energy/stress/source ledger is selected |

The maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.
This work sharpens representation compatibility but does not form a Record,
derive a clock, select matter statistics, or construct a source.

## No-go discipline gate

The fresh no-go procedure is applied because this route ships a negative at
the full-Fock and bounded-state-encoding resolution.

**N1-N8 result:** **PASS for the narrow statement that the published closed
higher-form duality and this square-pyramid instantiation do not satisfy the
Cycle-234 full local-state contract.  FAIL for a general fermion-to-qubit
no-go, a minimum-content claim, or axiom pressure.**

### N1 — alternative routes

| Route | Marker | Disposition |
|---|---|---|
| closed Chen-Kapustin face code | **ATTEMPTED** | exact bounded even algebra; odd global parity absent at `L=3,4,5` |
| boundary or punctured face code | **LIVE, NOT RULED OUT** | can carry odd flux, but introduces a marked defect/boundary and possible growing strings |
| parity-gauged Chen-Kapustin map | **PRIMARY-SOURCE LIVE, TARGET CHANGED** | removes bosonic constraints by coupling fermions to a dynamical/static `Z_2` gauge field; not the original Cycle-230 system |
| auxiliary-Majorana cancellation | **LIVE, NOT RULED OUT** | separate constructive class not instantiated here |
| generalized superfast/subsystem code | **LIVE, NOT RULED OUT** | may change state encoding and topological preparation obligations |
| antisymmetric distinguishable walkers | **LIVE, NOT RULED OUT** | free construction class; contact and local physical code untested |

The live alternatives block a shared obstruction.

### N2 — condition independence

The route conditions reduce to `K_even` (closed flux identity), `K_spin`
(three Wilson labels), `K_state` (observable duality versus local state
isometry), `K_cell` (mixed-cell framing/`cup_1` presentation), and `K_marker`
(period-16 placement).  They are independent: fixing spin does not restore odd
parity, adding a local state circuit does not select a spin sector, and a
unit-translation marker does not alter the Hilbert-space dimension.  None is
promoted to an axiom.

### N3 — hidden-condition scan

The mandatory scan promotes the following previously easy-to-hide inputs:
closed versus punctured domain, total-even restriction, spin sector, local
framing, mixed-cell diagonal, global code preparation, macro origin, coin,
contact, and schedule.  “Exact duality” is never used as shorthand for a
bounded-radius state circuit.  “Local” is restricted to the even observable
map and bounded physical supports unless explicitly qualified.

### N4 — residual matching

| Witness | Residual | Cycle-235 match |
|---|---|---|
| Cycle 230 | intrinsic `M_64` CAR cell lacks physical `M_2` compiler | face code attacks precisely this interface |
| Cycle 234 | exact 3-D bosonization remained live | instantiated with exact six-mode adjacency and finite ranks |
| Cycle 234 local-`E` contract | local observables are insufficient | primary source supplies only even-observable locality; odd dimension mismatch is exact |
| Cycle 219 mass fixture | one-particle sector required | absent because closed face flux fixes total parity even |
| Cycle 230 seam fixture | rank-73 sea required | absent because 73 is odd |

The negative is therefore at the declared state/code resolution, not inferred
from a failed numerical optimizer.

### N5 — resolution audit

| Resolution | Tested | Not established |
|---|---|---|
| cell geometry | exact face sharing and Euler census | a published mixed-cell `cup_1` table |
| local gauge algebra | actual Pauli phases, commutators, ranks, supports | fault tolerance and syndrome dynamics |
| `L=3,4,5` | both parity sectors explicitly audited | an open/punctured all-size repair |
| torus topology | exactly three Wilson spectators | local selection of a spin sector |
| all 24 frames | graph, constraints, hopping phases, group law, placement | boosts/Lorentz closure |
| state locality | growing basis-flux string witness | a theorem against encoders supplied with topological resource states |
| mass/seam | exact sector-membership audit | physical matrix elements, because the states are absent |
| translation | unit and macro translations | autonomous unit-cell marker law |

### N6 — partial-closure and primitive scan

Scale reference, kinetic isotropy, and realized-state evaluation do not select
the cellulation, parity sector, spin structure, `cup_1` presentation, marker,
coin, or contact.  Live partial closures are a punctured/boundary code with an
explicit locality audit, an auxiliary-Majorana compiler, a parity-gauged
target with a separately justified physical gauge field, or an autonomous
translation-orbit marker.  These are construction paths, not premise edits.

### N7 — steelman

> Exact higher-form bosonization has done exactly what its authors claim: it
> converts every local even fermionic observable to a bounded gauge-invariant
> bosonic operator.  Fermion parity is often physically superselected, so the
> even sector may be sufficient for some Hamiltonian questions.  A boundary,
> puncture, parity-gauged theory, or different auxiliary code may carry the odd
> sector.  The failure to encode the Cycle-230 one-particle and odd sea on a
> closed torus is therefore a mismatch with this campaign's full-Fock contract,
> not evidence that local fermionic physics is impossible.

The steelman is convincing and blocks every broad negative.

### N8 — cross-cycle echo

Cycle 229 separated finite Fock algebra from a spatial local compiler.  Cycle
230 supplied the intrinsic six-mode CAR and odd principal sea.  Cycle 234
showed that the scalar-reference gauge route moved global parity into state
preparation.  Cycle 235 removes that bus and lowers the local carrier count,
but returns to the standard total-even bosonization boundary.  The mechanism
is different and the residual is sharper; neither is constitutional evidence.

No prior convention ratifies an odd-sector defect, a boundary, or a gauge
field as physical.  No axiom pressure survives.

## Route disposition and next discriminator

**Cycle-235 disposition:** retain the square-pyramid 15-face-qubit architecture
as the strongest proper-cubic local even-algebra compiler.  Reject it as the
full Cycle-230 state compiler on closed domains.  Name the published state map
`J_CK` as a global even-sector/spin-sector isomorphism, not a bounded-radius
`E`.

The next discriminator is the independent auxiliary-Majorana route, with the
same square-pyramid geometry available as a comparison.  It must carry both
parities at `L=3,4,5`, construct an actual bounded-radius state map, and avoid
moving odd parity into a marked puncture, boundary, global bit, or prepared
topological service.  The unit-translation marker remains a separate physical
law obligation.

## Verification

```text
python3 scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py
```
