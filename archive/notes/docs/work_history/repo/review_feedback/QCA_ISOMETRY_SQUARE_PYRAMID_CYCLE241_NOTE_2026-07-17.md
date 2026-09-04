# QCA/isometry escape audit for the square-pyramid CAR code — Cycle 241

**Date:** 2026-07-17

**Type:** constructive rank completion plus exact Clifford-QCA and dictionary-extension discriminators

**Status:** the product-ancilla Clifford-QCA route is rejected on closed tori;
non-Clifford QCA and parity-sector gauging isometries remain live

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

**Packaging:** existing draft PR #5389 on the parking branch only

Companion runner:

```text
scripts/qca_isometry_square_pyramid_cycle241_2026_07_17.py
```

This cycle changes no foundation, axiom, Qualification, primitive, registry,
policy, queue, or audit surface.

## Result up front

The nontrivial-QCA escape is real enough that Guaita's finite-depth-unitary
theorem cannot close it.  Three-dimensional locality-preserving QCAs exist
that are not finite-depth Clifford circuits and can disentangle a
long-range-entangled Walker–Wang ground state.  “The gauge code is
long-range entangled” is therefore not a QCA no-go.

Cycle 241 nevertheless rejects two precise promotions of the Cycle-235
square-pyramid code.

First, the exact Chen–Kapustin parity-to-flux dictionary cannot be extended
verbatim to a QCA automorphism of the full tensor-product algebra.  The `6N`
local flux stars have rank `6N-1` and product `I`.  The commutation syndrome of
any finite-support face Pauli is a graph boundary and therefore has even
endpoint number.  It can flip two fluxes but has no singleton flipper.  A full
local matrix algebra would require a bounded conjugate to each independent
onsite parity.  That conjugate does not exist for the displayed flux stars.
This is an exact dictionary-extension result, not a no-go against every
off-code completion or every parity-sector map.

Second, a product-ancilla **Clifford QCA** cannot prepare the natural
rank-matched closed square-pyramid subcode.  Nine product ancillas per coarse
fermionic input cell would give `9N` independent bounded Pauli stabilizers
after a fixed-range Clifford QCA.  The bounded modified-Gauss group has rank
only `9N-2`.  The two missing stabilizer directions have nonzero torus
homology; the displayed cubic-symmetric choices have weights `6L` and cannot
be images of onsite Pauli operators at fixed QCA range.  This rejects the
product-ancilla Clifford-QCA/code-embedding route uniformly in size.

There is also a constructive rank completion.  Impose only

```text
W_x W_y = +1,
W_y W_z = +1,
```

on the three Wilson labels.  The remaining labels are `(0,0,0)` and
`(1,1,1)`, a proper-cubic invariant family, and the code exponent becomes
exactly `6N`, matching the full six-mode Fock space.  The common Wilson bit is
the only available slot for total parity; both the one-particle fixture and
the rank-73 sea would occupy its odd label.  But the two displayed relations
are noncontractible, no bounded local dressing that realizes the parity-to-
common-Wilson operator identity has been constructed, and the fixed
coarse-translation Pauli-dressing census fails at held `L=4`.  This is a
dimension- and covariance-compatible schema, not a physical compiler and not
a global-sector-service retirement.

The best disposition is therefore:

- reject the verbatim full-algebra flux QCA;
- reject product-ancilla Clifford-QCA preparation of the rank-matched closed
  code;
- retain non-Clifford 3-D QCA, locality-preserving subalgebra gauging, and
  open/infinite odd-sector representations as live hypotheses;
- retain the Cycle-237 unit-translation marker as a covariant law/code family,
  while keeping marker-state selection explicit; and
- do not claim
  `E G_coarse = G_physical E` for a bounded causal state encoder.

There is no route-independent obstruction and **no axiom pressure**.

## 1. Five contracts that must remain distinct

| Contract | Exact meaning | What it does not imply |
|---|---|---|
| finite-depth circuit | `O(1)` layers of bounded local gates, independent of `L` | every QCA is such a circuit |
| QCA automorphism | an invertible `*`-automorphism of the full quasi-local tensor algebra with bounded forward and inverse range | a product-ancilla code state, a selected topological sector, or finite-depth implementation |
| isometry/code embedding | an isometry `V:H_in -> H_phys` whose image is a code; Heisenberg locality asks that physical local pullbacks and represented input local observables remain bounded | surjectivity on the full physical algebra or preparation from product ancillas |
| algebra duality | a locality-preserving isomorphism of the parity-even observable algebra with a constrained gauge algebra | a full graded/tensor-algebra QCA or a bounded state preparation |
| state preparation | a specified operation and input resource producing one code/sector state | locality of the observable dictionary |

For an isometry, two locality directions must also be stated separately:

```text
causal pullback:        V^dagger O_X V is supported near X,
logical representation: O'_X V = V O_X for a bounded O'_X.
```

Neither direction alone proves that `V` is a QCA restriction or that `V` can
be applied to clean product ancillas in bounded depth/range.

## 2. Primary-source boundary

Gross, Nesme, Vogts, and Werner, [“Index theory of one dimensional quantum
walks and cellular automata”](https://arxiv.org/abs/0910.3675),
[Commun. Math. Phys. **310**, 419 (2012)](https://doi.org/10.1007/s00220-012-1423-1),
define the QCA information-flow index.  A qubit shift has index `2` and is a
range-one QCA with range-one inverse, but it is not locally implementable by a
finite-depth partitioned circuit.  The runner instantiates its finite support
permutation only; the nontrivial-index conclusion is the cited theorem.

Haah, Fidkowski, and Hastings, [“Nontrivial Quantum Cellular Automata in
Higher Dimensions”](https://arxiv.org/abs/1812.01625),
[Commun. Math. Phys. **398**, 469 (2023)](https://doi.org/10.1007/s00220-022-04528-1),
construct a 3-D Clifford QCA that disentangles the Walker–Wang three-fermion
ground state and prove that it is not a finite-depth **Clifford** circuit.
They do not construct the Cycle-230 compiler, but their example directly
blocks the inference from long-range code entanglement to QCA impossibility.

Haah, [“Clifford Quantum Cellular Automata: Trivial group in 2D and Witt group
in 3D”](https://arxiv.org/abs/1907.02075),
[J. Math. Phys. **62**, 092202 (2021)](https://doi.org/10.1063/5.0022185),
describes translation-invariant Clifford QCAs through symplectic Laurent-
polynomial data and exhibits nontrivial 3-D classes.  Cycle 241 uses that as
the motivation for a future symplectic-completion search.  It does not apply a
classification theorem to this mixed cellulation, to non-Clifford QCAs, or to
the marker-sector family.

Haegeman, Van Acoleyen, Schuch, Cirac, and Verstraete,
[“Gauging quantum states: from global to local symmetries in many-body
systems”](https://arxiv.org/abs/1407.1025),
[Phys. Rev. X **5**, 011024 (2015)](https://doi.org/10.1103/PhysRevX.5.011024),
construct a state gauging map on a globally symmetric subspace and a
compatible locality-preserving operator map; gauging an injective PEPS can
produce a `G`-injective PEPS with topological order.  This is primary evidence
that a subspace isometry plus local symmetric-observable map is a genuine
live class.  It is not a full-algebra QCA and its symmetry-sector and gauge-
field inputs must not be erased from the ledger.

Ma, Li, and Cheng, [“Quantum Cellular Automata on Symmetric
Subalgebras”](https://arxiv.org/abs/2411.19280), prove in one dimension that
Kramers–Wannier duality is a QCA of a `Z_2`-symmetric subalgebra with generalized
index `sqrt(2)` and cannot extend to a QCA of the full operator algebra.  That
is an exact example of the same **contract distinction**, not a theorem about
the 3-D square-pyramid fixture.

Chen and Xu, [“Equivalence between fermion-to-qubit mappings in two spatial
dimensions”](https://arxiv.org/abs/2201.05153), use local separators/flippers,
generalized local unitaries, and the triviality structure of 2-D QCAs to relate
2-D fermion mappings.  Their result is dimension-specific.  Cycle 241 borrows
only the separator/flipper diagnostic and does not transfer their 2-D
classification to 3-D.

## 3. Exact closed-torus rank budget

For the Cycle-235 square-pyramid dual graph, there are `6N` pyramid/matter
vertices and `15N` face qubits.  The executable ranks are:

| `L` | face qubits | bounded Gauss rank | plus two Wilson relations | full cycle/spin rank | code exponents: local / two / three |
|---:|---:|---:|---:|---:|---:|
| 3 | 405 | 241 | 243 | 244 | 164 / 162 / 161 |
| 4 | 960 | 574 | 576 | 577 | 386 / 384 / 383 |
| 5 | 1875 | 1123 | 1125 | 1126 | 752 / 750 / 749 |

Thus:

```text
local Gauss code:              2^(6N+2),
two Wilson relations:          2^(6N),
all three Wilson relations:    2^(6N-1),
full Cycle-230 Fock space:      2^(6N),
one fixed matter-parity sector: 2^(6N-1).
```

Exactly two additional independent code conditions are required to match a
full-Fock isometry without adding or deleting a finite global qubit.  The
equal-Wilson pair is one proper-cubic way to meet that count.  Rank matching
is necessary, not sufficient.

### Exact dictionary-extension obstruction

Let `W_t` be the face-`Z` flux star at pyramid `t`.  On every connected closed
domain,

```text
rank{W_t}=6N-1,
product_t W_t=I.
```

For any face Pauli `P`, its commutation syndrome against all `W_t` is the
boundary of the `X/Y` face support.  Every finite edge-chain boundary has even
cardinality.  The runner verifies the full boundary rank `6N-1`, an
unreachable singleton, and a reachable adjacent pair at `L=3,4,5`; it repeats
bounded light-cone subspace checks at radii `0,1,2,4` in an `L=11` control.

If a full-algebra QCA mapped every input onsite `Z_t` exactly to the displayed
`W_t`, it would already violate injectivity because `product_t W_t=I` whereas
the product of the input onsite `Z_t` is a nontrivial operator.  The conjugate
test gives the local version of the same contradiction: the image of `X_t`
would have to anticommute with only `W_t`, but no bounded operator has that
syndrome.  For a non-Pauli operator, expand it in the finite Pauli basis of its
bounded support: every component still has even syndrome, so the singleton
eigenspace is empty.  If one instead deletes a reference parity or fixes total
parity, the required flippers have paired endpoints and generally growing
strings; that is a sector/subalgebra map, not this verbatim full-algebra map.

This proof rejects only the verbatim assignments `Z_t -> W_t` on the **full**
tensor algebra.  On a fixed parity sector there is no independent odd operator
`X_t`, and an off-code completion may dress `W_t` with auxiliary syndrome
operators.  Those are different hypotheses.

## 4. Product-ancilla Clifford-QCA discriminator

To embed `6N` arbitrary input qubits into `15N` face qubits by restricting a
full QCA, initialize `9N` input ancillas in fixed onsite Pauli eigenstates.  A
Clifford QCA of range `R` sends their `9N` independent onsite stabilizers to
`9N` independent Pauli stabilizers of support bounded by `R`.

The rank-matched target code has stabilizer rank `9N`, but only `9N-2` of
those directions lie in the bounded Gauss group.  Any stabilizer outside that
span has nonzero first homology and must wind around the torus.  The displayed
proper-cubic pair constraints have weights

| `L` | `wt(W_x W_y)` | `wt(W_y W_z)` | `wt(W_z W_x)` |
|---:|---:|---:|---:|
| 3 | 18 | 18 | 18 |
| 4 | 24 | 24 | 24 |
| 5 | 30 | 30 | 30 |
| 7 | 42 | 42 | 42 |

and any nonzero homology representative needs support growing at least with
`L`.  No fixed-range image of an onsite ancilla Pauli can generate the two
missing directions.  Hence the natural rank-matched square-pyramid code is
not the image of product ancillas under a fixed-range Clifford QCA.

Exact hypotheses:

1. closed periodic domains;
2. the Cycle-235 square-pyramid Pauli/Gauss code;
3. clean onsite product ancillas;
4. a Clifford QCA with range independent of `L`; and
5. exact image equality with the rank-matched code.

The result does not cover a non-Clifford QCA, a QCA supplied with a
topologically entangled ancilla state, measurement/feedforward, a non-
stabilizer code deformation, or an open/infinite charge-sector isometry.

## 5. Translation-orbit dressing and the live equal-Wilson schema

The common-Wilson family

```text
(w_x,w_y,w_z) in {(0,0,0),(1,1,1)}
```

is invariant under every signed axis permutation, hence all 24 proper-cubic
frames.  It leaves one bit that could label even versus odd matter.  The
mapped Cycle-230 update is parity even and commutes with every Wilson label,
so such a label would be a spectator during the update rather than a runtime
parity query.

What is missing is a bounded local operator map with

```text
product_t B_hat_t = W_common
```

and the correct local fermionic even-algebra relations.  The runner tests the
most direct Clifford possibility.  Multiplying any fixed bounded coarse-
translation-covariant Pauli dressing over all cells reduces its face-chain
component to one of `2^15` unions of the 15 face-type orbits.  Exactly 1024
templates are closed cycles at each held size.  At odd `L=3,5` they realize
all eight homology labels; at even `L=4` every one is homologically trivial.
No fixed template has the same nonzero Wilson class at all three sizes.

This falsifies a fixed one-cell Pauli-orbit dressing.  It does not cover a
non-Clifford image, a larger-period/staggered sector family, a data-dependent
dressing, or a nontrivial Laurent-polynomial symplectic completion with added
off-code factors.  Any larger-period route must separately recover unit-
translation covariance and autonomous sector preparation.

## 6. One-particle/rank-73 fixtures and the state-map boundary

Both required fixtures have odd total parity:

```text
(-1)^1  = -1,
(-1)^73 = -1.
```

They can share one odd infinite-volume or common-Wilson sector.  Because the
coin, FSWAP stream, and contact are parity even, they do not require a runtime
parity service once that sector and a correct local representation are
provided.  That statement does not prepare the sector.

The closed Cycle-235 map with all three Wilson labels fixed represents the
total-even sector as written and contains neither fixture.  The equal-Wilson
rank completion has enough dimension, but the local central-parity operator
map and its QCA/isometry are unbuilt.  Therefore Cycle 241 reports neither a
one-particle mass intertwining residual nor a physical rank-73 seam residual.
The predecessor numerical fixtures remain conditional regression targets;
they are not silently declared preserved.

## 7. Proper-cubic placement and unit-translation marker family

The 15 square-pyramid face carriers are a subset of the Cycle-237 27-wildcard
spacing-16 marker layout:

```text
12 internal triangular faces at 2(D_a+D_b),
 3 shared square faces at 8 e_mu modulo 16.
```

The runner verifies that this 15-site set is invariant in all 24 proper-cubic
frames.  It independently reruns the inherited radius-two marker tests:

| Test | Result |
|---|---:|
| translated phase templates | 4096 |
| ambiguous phase pairs | 0 |
| proper-frame template tests | 98,304 with 0 failures |
| neighbor-successor tests | 12,288 with 0 missing/extra |
| unit-shift Hamming distance of one chosen phase | 2184 on each axis |

Thus the physical **law/code family** can remain unit-translation covariant;
a local QCA rule could in principle decode the marker phase and act on the
face carriers.  No such QCA rule is constructed here.  The inherited layout
also leaves 12 additional data wildcards beyond the 15 face carriers; fixing,
using, or deleting them is supplied compiler structure.

A chosen marker product state breaks unit translation.  A deterministic
translation-covariant QCA maps a translation-invariant input state to another
translation-invariant state and therefore cannot select that phase from a
homogeneous input.  An equal mixture or coherent superposition of phases is
translation invariant but has long-range sector correlation.  A product-fed
range-`R` QCA factorizes observables with disjoint inverse light cones, so it
cannot prepare the cat-like restoration without a correlated input resource.
Supplying one symmetry-broken marker product state remains live, but it is a
state/reference import, not an autonomous selection theorem.

Physical overhead remains constant: the square-pyramid algebra uses 15 face
qubits per coarse cell; the inherited strict physical placement uses one
`16^3=4096`-site marker macroperiod.  Bounded support and constant overhead do
not by themselves close sector preparation.

## 8. Route disposition and live hypotheses

| Route | Evidence | Disposition |
|---|---|---|
| finite-depth local unitary preparation | Guaita growing-loop theorem | asymptotically excluded under its product-input/two-body-unitary hypotheses; not a QCA result |
| verbatim full-algebra flux QCA | flux rank and singleton-flipper contradiction | rejected exactly |
| product-ancilla Clifford QCA into the rank-matched closed code | bounded rank is short by two topological stabilizers | rejected exactly |
| non-Clifford 3-D QCA with an off-code completion | no exact fixture theorem or candidate symplectic/nonlinear rule | **live, unconstructed** |
| parity-even subalgebra QCA/gauging isometry | supported as a real class by Haegeman et al. and subalgebra-QCA work | **live; odd sector and bidirectional locality untested** |
| QCA supplied with a topological resource state | evades clean-product stabilizer premise | **live but resource preparation remains supplied** |
| open/infinite odd-sector representation | removes the closed product-flux identity as a local observable | **live; boundary/infinity and finite controls unbuilt** |
| measurement/feedforward gauging | outside unitary-QCA and Guaita hypotheses | **live; autonomous local decoder not built** |
| larger-period/staggered QCA | may evade the one-cell Pauli-orbit census | **live; covariance and phase selection must be redone** |

The decisive unresolved hypotheses are:

```text
H_nonClifford:
  a bounded-range non-Clifford automorphism has an off-code completion of the
  even algebra and a rank-matched image code;

H_subalgebra:
  a gauging isometry on one odd sector is causal in both Heisenberg directions
  and intertwines every Cycle-230 local even gate;

H_charge:
  total odd parity is carried by a boundary/infinite/common-Wilson label
  without a global preparation or runtime service;

H_covariance:
  the actual QCA/isometry, not just the cellulation and marker family,
  intertwines all 24 proper-cubic frames and unit translations;

H_resource:
  every nonproduct gauge/marker resource used by the encoding has an admitted
  physical preparation and leakage/deletion control.
```

No tested result decides all five.

## 9. Supplied-structure and novelty inventory

Supplied in this route:

1. the Cycle-235 square-pyramid cellulation and face-Pauli presentation;
2. closed periodic domains and their three Wilson labels;
3. the proposed two equal-Wilson relations and parity-label interpretation;
4. clean product ancillas in the rejected Clifford-QCA route;
5. Clifford and coarse-translation invariance in the Pauli dressing census;
6. the Cycle-237 seed-237000 marker, spacing 16, 4096 phase templates, and 27
   wildcard roles;
7. a chosen marker and charge sector if one realized state is required;
8. the Cycle-219 coin, Cycle-230 contact, coupling, and gate schedule; and
9. any topological, boundary, measurement, or PEPS resource used by a future
   live route.

Primary prior art supplies the QCA/circuit distinction, nontrivial 3-D QCAs,
state gauging maps, and subalgebra QCAs.  The new fixture-specific content is
the exact `9N-2 -> 9N` Clifford-QCA stabilizer deficit, the `6L` Wilson-pair
weights, the all-`2^15` held-size orbit-homology census, the cubic equal-Wilson
rank completion, and their joint comparison with the two odd fixtures and
the existing marker family.  No new general QCA classification is claimed.
Thirring machinery is not used.

## 10. TOE dependency ledger

| Wall | Cycle-241 effect | Remaining dependency |
|---|---|---|
| `C_ref` | marker and Wilson/charge sector selection are separated from law covariance | physical sea, phase origin, marker phase, and realized charge sector remain supplied |
| `C_num` | a cubic common-Wilson parity slot is dimensionally identified; verbatim local flux extension fails | no bounded all-size operator map or physical derivation of the odd sector |
| `C_wrap` | QCA index, Wilson labels, circuit layers, and marker phases remain explicitly non-temporal | none is a clock, rate, physical energy, or winding history |
| `C_int` | unchanged conditional representation | the supplied contact can be mapped only after a lawful state encoder; selection/protection/rate remain open |
| `C_local` | narrowed | product-ancilla Clifford QCA and verbatim flux QCA rejected; non-Clifford/subalgebra/open-sector encoders remain live |
| `C_source` | unchanged | no energy, stress, action, resource ledger, or gravitational source is selected |

Maturity remains operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, Born/probability `1/5`.  A QCA
light cone is not causal time, a marker bit is not a Record, a Wilson label is
not energy, and a normalized code state does not supply occurrence weights.

## Spatial-dimension and time firewall

The QCA range, application count, circuit depth, marker phase, stabilizer
measurement round, compiler layer, and macrostep are implementation
coordinates.  None is called physical elapsed time, a clock normalization, a
generator rate, physical energy, a transition probability, or a Record.  The
`Z^3` spatial substrate and proper-cubic action are supplied predecessor
structure and are not derived in this cycle.

## No-Go Discipline Gate

The fresh `origin/main` no-go procedure was applied.  **N1–N8 PASS** for the
narrow verbatim-dictionary and product-ancilla Clifford-QCA negatives.
**N1–N8 FAIL** for a non-Clifford-QCA impossibility, a subalgebra-isometry
impossibility, a general state-preparation no-go, uniqueness/minimality, or
axiom pressure.

### N1 — alternative-route enumeration

| Route against the negative | Marker | Disposition |
|---|---|---|
| exact `B_t -> W_t` full-algebra QCA | **ATTEMPTED** | rank/product relation and singleton-flipper syndrome reject the verbatim extension |
| local auxiliary/off-code Pauli dressing | **ATTEMPTED** | all `2^15` fixed translation-orbit chain templates fail to leave one nonzero Wilson class at `L=3,4,5`; more general completion remains live |
| product-ancilla Clifford QCA | **ATTEMPTED** | `9N` bounded image stabilizers cannot span the two growing homology directions beyond rank `9N-2` |
| non-Clifford 3-D QCA | **LIVE, NOT RULED OUT** | Haah–Fidkowski–Hastings prove this is a genuinely larger class; no fixture theorem closes it |
| parity-sector state-gauging isometry | **LIVE, NOT RULED OUT** | Haegeman et al. give locality-preserving symmetric-subspace gauging maps; odd charge and this cellulation remain unbuilt |
| topologically entangled input resource | **LIVE, NOT RULED OUT** | evades clean product ancillas but moves the burden to resource preparation |
| open/infinite odd representation | **LIVE, NOT RULED OUT** | a boundary or sector at infinity can carry odd flux; uniform finite controls are absent |
| local measurement and feedforward | **LIVE, NOT RULED OUT** | outside both unitary-QCA and Guaita circuit hypotheses |
| staggered/larger-unit-cell QCA with translation-orbit sectors | **LIVE, NOT RULED OUT** | may evade the one-cell census but must restore unit translation and autonomous phase selection |

The live routes block every broad negative.

### N2 — wall-independence audit

The raw conditions collapse to four walls.  Update-gate locality is downstream
of a valid even-algebra/state interface because Cycle 235 already supplies the
bounded mapped update algebra.  The mass/seam fixture is downstream of the
odd-sector state map.  They are not counted independently.

- `W_full`: extend or replace the even-subalgebra map by a lawful full/code
  isometry with both Heisenberg locality directions;
- `W_charge`: carry the odd sector and finite topological labels without a
  global service;
- `W_prepare`: prepare every nonproduct gauge/marker resource admitted by the
  encoder; and
- `W_cov`: make the actual encoder/QCA covariant, not only its architecture.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---:|---:|---:|
| `W_full`, `W_charge` | no | no | yes |
| `W_full`, `W_prepare` | no | no | yes |
| `W_full`, `W_cov` | no | no | yes |
| `W_charge`, `W_prepare` | no | no | yes |
| `W_charge`, `W_cov` | no | no | yes |
| `W_prepare`, `W_cov` | no | no | yes |

### N3 — hidden-condition scan

| Potential hidden condition | Classification |
|---|---|
| “QCA” | full-algebra automorphism, subalgebra map, and isometry are defined separately |
| clean product ancillas | explicit load-bearing hypothesis of the Clifford negative |
| Clifford | explicit; non-Clifford QCA remains live |
| closed torus | explicit; open/infinite sectors remain live |
| translation invariant | explicit in the orbit census; staggered families remain live |
| “topological order” | used only at the primary sources' stated resolution, never as a universal QCA obstruction |
| marker background | seed, radius, templates, overhead, and phase-selection cost are explicit supplied structure |
| physical time | explicitly firewalled from QCA/circuit coordinates |

No phrase “by construction,” “standard,” “naturally,” or “obviously” carries
an unlisted physical premise.

### N4 — residual matching

| Witness | Exact residual | Cycle-241 use | Match? |
|---|---|---|---:|
| Cycle 230 | intrinsic CAR cell lacks physical `M_2` state compiler | QCA/isometry is one candidate for that interface | yes |
| Cycle 235 | local even algebra, closed total-even state code, and three Wilson labels | exact square-pyramid target audited here | yes |
| Cycle 237 | nontrivial QCA/isometry and marker state remained live | tests the original two residuals | yes |
| Cycle 238 | QCA must construct both sector and local Heisenberg action | this cycle's exact assigned discriminator | yes |
| Cycle 239 | distinguishable-walker QCA has growing type multiplicity and global antisymmetrizer | different realization; used only as a route-separation control | no as square-pyramid witness |
| Cycle 240 | bounded measurements project locally but displayed decoder/spin preparation is global | separates nonunitary preparation/resource routes from QCA preparation | yes, scoped |
| Guaita 2025 | product-to-code preparation by local two-body unitary circuits | used only to separate finite-depth circuits from QCAs | yes, scoped |
| GNVW 2012 | 1-D QCA index and shift/noncircuit distinction | shows QCA is a larger contract, not a fixture compiler | yes, scoped |
| Haah–Fidkowski–Hastings 2023 | nontrivial 3-D Clifford QCA | blocks broad long-range-entanglement rhetoric | yes, counter-witness |
| Haegeman et al. 2015 | state/operator gauging on symmetric subspace | supports the live isometry class only | yes, scoped |
| Ma–Li–Cheng 2024 | 1-D symmetric-subalgebra QCA nonextension | contract analogy only, not a 3-D no-go | no as fixture theorem; not counted |

No cited source is promoted to a theorem about the unconstructed Cycle-241
non-Clifford rule.

### N5 — rhetoric and resolution audit

| Resolution | Tested | Not established |
|---|---|---|
| exact local flux dictionary | full closed-torus rank and all finite-support Pauli syndromes | every auxiliary/off-code dictionary |
| bounded light cones | radii `0,1,2,4`, plus analytic even-boundary rule | quasi-local tails or unbounded resources |
| closed sizes | `L=3,4,5`; Wilson growth also at `L=7` | open/infinite uniform compiler |
| Clifford product-ancilla QCA | stabilizer rank and homology | non-Clifford QCA/isometry |
| fixed translation Pauli dressing | all `2^15` orbit templates | staggered, nonlinear, or non-Pauli dressing |
| QCA versus circuit | exact range-one shift plus primary index theorem | classification of this 3-D code |
| architecture covariance | 15 carriers, 24 frames, 4096 marker phases | covariance of an actual encoder |
| product-fed marker preparation | disjoint inverse-light-cone factorization | supplied correlated or symmetry-broken input |

Every negative is stated at the narrow tested resolution.

### N6 — partial-closure paths

| Path | Status | Possible closure |
|---|---|---|
| cubic equal-Wilson family | constructed at rank/covariance level | gives the exact missing full-Fock dimension and a parity slot |
| non-Clifford symplectic/nonlinear completion | live | may realize the off-code full-algebra completion |
| Haegeman-style odd-sector gauging isometry | live | may close bidirectional Heisenberg locality without product preparation |
| supplied topological resource state | live, import-bearing | can evade product-ancilla rank obstruction |
| open/infinite charge sector | live | can terminate odd flux outside the local algebra |
| measurement/feedforward gauge preparation | live | may prepare constraints outside unitary-QCA hypotheses |
| Cycle-237 marker orbit | constructed as code/admissibility | closes law-level physical-origin preference, not state selection |

These are constructive/import-retirement routes.  No new axiom is requested.

### N7 — steelman

> The Cycle-241 negative is far too narrow to threaten the QCA route.  A
> nontrivial 3-D QCA can disentangle a Walker–Wang state even though no
> finite-depth Clifford circuit can, so Guaita's depth lower bound is not the
> relevant classification.  Haegeman and collaborators explicitly construct
> state gauging maps whose symmetric-observable maps preserve locality and
> whose outputs can be topologically ordered.  The square-pyramid rank ledger
> itself exposes a proper-cubic two-Wilson completion with exactly the full
> Fock dimension and one common charge bit.  The runner rejects only Clifford
> product ancillas and one-cell Pauli dressings.  A non-Clifford QCA, a
> subalgebra isometry, or a topological input resource could still realize the
> Cycle-230 even dynamics and both odd fixtures without a runtime parity
> query.  Until those routes are constructed or theorem-matched, a general
> QCA/isometry no-go would be an overclaim.

This steelman is convincing and forces the broad gate to fail.

### N8 — cross-cycle echo

Repository searches for prior QCA, state-isometry, topological-resource, and
compiler-wall language were rerun.  The relevant echoes are:

| Earlier cycle | Earlier boundary | Mechanism retained here |
|---|---|---|
| Cycle 229 | finite Fock matrices are not a spatial state compiler | keep operator algebra and state map distinct |
| Cycle 232 | bounded gauge updates coexist with a nonlocal sectorwise isometry | test QCA preparation rather than infer it from update locality |
| Cycle 234 | exact bosonization and auxiliary/QCA-style encoders remained live | attack one live route without promoting its failure |
| Cycle 235 | square-pyramid code has exact even algebra but absent odd state sector | add the rank-matched Wilson schema and audit its locality |
| Cycle 237 | QCA/isometry and autonomous marker preparation explicitly remained open | instantiate their finite rank, light-cone, and marker discriminators |
| Cycle 238 | QCA/isometry named as the independent escape outside Guaita | test it without inheriting the unitary-circuit theorem |
| Cycle 239 | local distinguishable-walker QCA can coexist with a global state isometry | preserve the QCA/state-map distinction and do not splice routes |
| Cycle 240 | local measurement succeeds while sign/spin decoding remains global | keep measurement, QCA, and supplied-resource preparation as separate routes |
| earlier QCA/Record campaigns | QCA locality does not itself create Records or physical time | preserve the same semantic firewall |

The recurring successful mechanism is to replace a broad compiler claim by a
sector/subalgebra map plus explicit resources.  That mechanism remains live,
so a broad no-go is premature.

## Verification

```text
python3 scripts/qca_isometry_square_pyramid_cycle241_2026_07_17.py
```

Expected result: every check passes.  The runner uses the retained Cycle-235
cellulation and Cycle-237 marker implementations and introduces no stochastic
or host-side state selection.
