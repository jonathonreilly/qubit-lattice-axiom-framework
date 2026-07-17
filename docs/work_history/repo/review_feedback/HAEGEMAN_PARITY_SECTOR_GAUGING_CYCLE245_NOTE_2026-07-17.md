# Haegeman-style parity-sector gauging on the Cycle-235 dual graph — Cycle 245

Date: 2026-07-17
Type: constructive state-isometry and observable-map instantiation with a bounded compiler discriminator
Status: exact sector gauging retained; ordinary-matter-qubit CAR compilation and autonomous odd-resource preparation remain open
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/haegeman_parity_sector_gauging_cycle245_2026_07_17.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit surface.

## Result up front

The Haegeman state-gauging class is constructive on the **actual Cycle-235
square-pyramid dual graph**. Put one retained matter qubit on each of its
`6L^3` dual vertices and one `Z_2` gauge qubit on each of its `15L^3` dual
edges/primal faces. On a fixed global-parity sector, the runner instantiates
an exact normalized state gauging map and a compatible local
symmetric-observable map. It verifies both Heisenberg locality directions on
the declared gauge-invariant image algebra, exact ranks and isometry at
`L=3,4,5`, local Gauss/flatness constraints, the Cycle-230 onsite coin,
contact, and `A/B` FSWAP factors, deletion/leakage controls, and all 24
proper-cubic frames.

The positive result is substantial but it is not the missing physical-M2 CAR
compiler.

- If the retained matter carriers are still fermionic, gauging makes their
  even observables gauge invariant and local while leaving fermionic matter
  in the target.
- If the retained matter carriers are ordinary qubits, the map locally gauges
  their global `Z_2` symmetry. The local hard-core hopping image then has the
  wrong incident-edge CAR algebra.
- If actual CAR operators are first represented on those qubits by a
  Jordan–Wigner map, the gauge dressing adds one local face operator but does
  not remove the pre-existing matter string. On the repository vertex order,
  the largest shorter-sector stream string is `6L^2 = 54,96,150` at
  `L=3,4,5`.

Thus retaining matter qubits plus edge/face gauge qubits gives constant
overhead—**21 physical M2 factors per coarse cell**—but simply preserves the
original fermion-sign problem unless a separate local CAR-to-matter-qubit map
is supplied.

The closed all-plus state gauging map has a second exact boundary: it is an
isometry only on the globally symmetric, total-even matter sector. The odd
one-particle and rank-73 fixtures are annihilated by that standard closed
projection. A lawful odd state image can be constructed by changing the
contract: give one marked vertex a negative Gauss background and choose the
flat common-Wilson connection `111`. Combining the even `000` and odd `111`
images produces an exact equal-Wilson/common-parity schema of exponent
`6L^3`, matching the full Fock dimension.

That rank-complete direct sum does not yet supply the campaign's required
single physical update. The compatible observable map contains the sector
representative sign `(-1)^(c dot h)`. It is `+1` throughout the even `000`
image, while the odd `111` representative changes it on `3L^2` of the
`3L^3` outer/B hopping faces. Thus the two sectorwise intertwiners use
different seam signs. Joining them by a common-Wilson projector would be
nonlocal; writing the `h_111` membrane signs into the gate table would supply
a preferred membrane/background. A different bounded quantum-controlled
construction remains live, but is not built here.

That odd extension is algebraically exact, so the one-particle mass and the
rank-73 seam remain conditional intertwinable targets when the matter carrier
is still fermionic. It is not an autonomous physical compiler: the selected
reference charge has a six-element proper-frame orbit and is moved by every
nonzero unit translation, the `111` connection uses three noncontractible
`L^2` membranes, and the charge-to-common-Wilson constraint has support
growing with `L`. Reference charge, boundary, and topological resource choices
are supplied, not derived.

State preparation is separate from algebra locality. No bounded-depth or
autonomous preparation of the state gauging sum, marked charge, or common
Wilson sector is claimed. There is no shared no-go and no axiom pressure.

## Primary-source and novelty boundary

Haegeman, Van Acoleyen, Schuch, Cirac, and Verstraete,
[“Gauging quantum states: from global to local symmetries in many-body
systems”](https://arxiv.org/abs/1407.1025), construct a map from globally
invariant matter states to locally gauge-invariant matter-plus-gauge states
and a compatible operator map satisfying

```text
G O |psi> = mathscr_G[O] G |psi>.
```

They show that the operator map preserves locality and gives the usual
minimal coupling for hopping terms. Their input state is globally invariant;
the paper does not claim that the standard closed projector retains a charged
sector, compiles fermionic matter into ordinary qubits, or supplies a bounded
state-preparation circuit for this Cycle-235 graph.

Cycle 245 instantiates the `G=Z_2` formula, rather than citing the class
abstractly. The fixture-specific content is:

1. the exact map on the square-pyramid graph at `L=3,4,5`;
2. its `6L^3 + 15L^3` matter/face rank ledger;
3. a proper-cubic minimal-chain average for the six-mode onsite algebra;
4. exact images of the Cycle-219/230 coin, contact, and `A/B` FSWAP factors;
5. a marked-charge/common-Wilson direct sum carrying both parity sectors;
6. the charge-Wilson constraint rank, all-frame covariance, and two-sector
   update-sign mismatch audit; and
7. the direct comparison between ordinary symmetric-qubit locality and the
   unresolved fermionic sign algebra.

This `Z_2` gauge presentation uses star Gauss operators and `Z`-flatness loops
on the Cycle-235 dual graph. It must not be silently identified with every
phase/framing choice in the Cycle-235 Chen–Kapustin face-Pauli presentation;
the shared graph and rank complex are exact, while the operator dictionaries
are distinct.

## Explicit state gauging map

Let the connected dual graph have vertex set `V`, edge set `E`, and binary
incidence coboundary `delta:F_2^V -> F_2^E`. Matter parity is

```text
Q = product_(v in V) Z^m_v.
```

Choose a parity sector `p in {0,1}`, so `Q=(-1)^p`, a binary charge-background
word `r` with

```text
sum_v r_v = p mod 2,
```

and a flat edge word `h`. The instantiated state gauging map is

```text
V_(r,h)|psi> = 2^(-(abs(V)-1)/2)
  sum_[s in F_2^V / <all-ones>]
  (-1)^(r dot s) Z_m^s |psi> tensor |h + delta s>_g .
```

The quotient is well defined precisely because `sum r=p` on the declared
input sector. The `2^(|V|-1)` cut words are distinct, so their normalization
gives

```text
V_(r,h)^dagger V_(r,h) = I_(Q=(-1)^p).
```

The local Gauss operators are

```text
A_v = Z^m_v product_(e incident v) X^g_e,
A_v V_(r,h) = (-1)^(r_v) V_(r,h).
```

For every dual cycle `c`,

```text
Z^g(c) V_(r,h) = (-1)^(c dot h) V_(r,h).
```

The Cycle-235 local primal-edge cycles have rank `9L^3-2`; adding its three
noncontractible Wilson cycles gives rank `9L^3+1`. Together with the `6L^3`
Gauss constraints, a fixed-parity/fixed-Wilson image inside the `21L^3`
matter-plus-gauge qubits has exponent

```text
21L^3 - 6L^3 - (9L^3+1) = 6L^3-1,
```

exactly the input parity-sector exponent.

| `L` | matter qubits | face gauge qubits | incidence rank | local-flat rank | full-flat rank | sector/image exponent |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 162 | 405 | 161 | 241 | 244 | 161 |
| 4 | 384 | 960 | 383 | 574 | 577 | 383 |
| 5 | 750 | 1875 | 749 | 1123 | 1126 | 749 |

The runner checks zero cut/cycle pairing failures at every size.

## Compatible local symmetric-observable map

Write an ordinary matter-qubit Pauli monomial as

```text
O(a,b) = X_m^a Z_m^b.
```

It commutes with global parity exactly when `|a|` is even. In a connected
bounded region `Gamma` containing its flipped endpoints, choose edge chains
`c subset Gamma` with graph boundary

```text
partial c = a.
```

Cycle 245 uses the proper-cubic set of every minimum-weight such chain and
defines the image term by term as

```text
mathscr_G_h[O(a,b)] = average_c [
  (-1)^(c dot h) X_m^a Z_m^b Z_g^c
].
```

Every summand commutes with every Gauss operator because its matter-flip
syndrome and gauge-chain boundary are the same. On the flat image code all
chains with the same boundary agree, and the `h` sign cancels the selected
flat-connection phase. Hence

```text
mathscr_G_h[O] V_(r,h) = V_(r,h) O,
V_(r,h)^dagger mathscr_G_h[O] V_(r,h) = O.
```

These are the two Heisenberg locality directions on the declared image
algebra:

- **logical representation:** a local symmetric matter operator has a local
  gauge-invariant representative;
- **causal pullback:** its local representative, local matter `Z`, local
  Gauss stars, and local flatness generators pull back to the corresponding
  bounded matter operator or a scalar.

More generally, a gauge-invariant Pauli with gauge-`X` word `d` preserves all
fixed flatness constraints only when `d` is a cut. A bounded product of local
star cuts pulls back to the matching bounded product of matter `Z` operators.
No claim is made for a physical operator that changes the selected Wilson
sector or violates the declared code constraints.

The exact two-vertex/one-edge matrix fixture—embedded in every outer-square
edge—tests even, reference-charged odd, and odd-`h=1` sectors. Its isometry,
logical-representation, causal-pullback, local-`Z` pullback, and Gauss
residuals are all below `3.2e-16`.

## Exact Cycle-230 operator images

### Onsite coin and contact

The actual `64 x 64` Fock-lifted Cycle-219 coin has 792 nonzero six-qubit
Pauli coefficients at the runner tolerance; the contact has 64. Their
reconstruction residuals are respectively `2.48e-15` and `3.87e-15`. Every
term has even matter-flip parity.

The six direction vertices inside a cell form the octahedron `K_6` minus the
three opposite pairs, with 12 internal face edges and diameter two. Averaging
over every minimum chain gives:

```text
coin image support:    at most 6 matter + 12 face qubits,
contact image support: the 6 matter qubits (diagonal; no chain),
maximum chosen chain:  3 internal faces.
```

The full set of minimum-chain images is carried into itself in all
`24 x 32 = 768` proper-frame/endpoint tests. There is no preferred port path.

### A/B FSWAP layers

For two ordinary matter qubits,

```text
FSWAP_(u,v) = (Z_u + Z_v + X_u X_v + Y_u Y_v)/2.
```

The symmetric-qubit gauged image along a chain `c` is

```text
(Z_u + Z_v
 + (-1)^(c dot h) (X_u X_v + Y_u Y_v) Z_g(c))/2.
```

Cycle 230's `A` layer pairs opposite onsite directions. Each has four
proper-cubic-equivalent length-two paths in the octahedron; the symmetric
minimum-path set stays inside the 18-carrier onsite region. Its `B` layer
pairs the endpoints of one outer-square dual edge, so its chain is that
single face qubit. The runner reconstructs FSWAP from its four Pauli terms at
machine zero and verifies every displayed boundary/Gauss syndrome.

This is an exact image of the **ordinary symmetric-qubit** FSWAP. It is also
the correct minimal-coupling formula if the matter input remains an abstract
fermionic algebra. It is not, by itself, a qubit representation of that CAR
algebra.

## The retained fermion-sign discriminator

A fixed-order qubit representation of the CAR hopping across modes `u<v`
contains the matter parity interval:

```text
c_u^dagger c_v + c_v^dagger c_u
  <-> (X_u Z_(u+1)...Z_(v-1) X_v
      +Y_u Z_(u+1)...Z_(v-1) Y_v)/2.
```

Applying the state-gauging observable map dresses the endpoint flip with
`Z_g(c)`; it does not delete any diagonal matter `Z` in the interval. Even
after using fixed total parity to choose the shorter cyclic interval, the
actual Cycle-235 ordering gives:

| `L` | outer/B edges | minimum string | maximum string | gauged off-diagonal Pauli weight |
|---:|---:|---:|---:|---:|
| 3 | 81 | 6 | 54 | 57 |
| 4 | 192 | 6 | 96 | 99 |
| 5 | 375 | 6 | 150 | 153 |

The held law is `max string = 6L^2`, so this particular actual-CAR image is
not bounded radius.

Deleting the strings and using only local hard-core images does not repair
the algebra. Two edge operators `X_u X_v Z_e` and `X_v X_w Z_f` commute when
they share one matter endpoint. The Cycle-235 framed even-CAR hopping
generators anticommute for the same one-endpoint incidence. The runner checks
this exact pair on the actual `L=3` graph.

This is a narrow discriminator. It rejects neither every fermion-to-qubit
code nor every ordering/dressing; it shows that **this Haegeman map applied to
retained ordinary matter qubits does not itself supply the missing sign
compiler**.

## Closed symmetry, odd charge, and equal-Wilson/common-parity schema

For the standard all-plus closed map, `r=0`. Multiplying all Gauss operators
gives

```text
product_v A_v = Q.
```

Therefore all `A_v=+1` implies `Q=+1`. The normalized projection has norm one
on the even sector and zero on the odd sector. Closed global symmetry excludes
odd fixtures under this standard contract.

An odd sector becomes lawful after an explicit contract change:

```text
r_(v_ref)=1,  r_(v != v_ref)=0,
h_odd = M_x + M_y + M_z,
```

where `M_mu` is the Cycle-240 `L x L` membrane dual to Wilson cycle `W_mu`.
Then `sum r=1`, every local-flat cycle has eigenvalue `+1`, and

```text
(W_x,W_y,W_z) = (1,1,1).
```

Use `r=0,h=0` for even matter. The two sector images are orthogonal and obey
the equal-Wilson relations

```text
W_x W_y=+1,  W_y W_z=+1.
```

The direct-sum image can be specified by:

1. all local flatness constraints;
2. the two equal-Wilson relations;
3. all Gauss constraints away from `v_ref`; and
4. the charge-parity link `A_(v_ref) W_x=+1`.

At `L=3,4,5` these commuting conditions have ranks `405,960,1875` inside
`567,1344,2625` matter-plus-gauge qubits, leaving exponents `162,384,750 =
6L^3`. This is an exact full-Fock **rank and sector isometry schema**.

It is not an `E G_coarse = G_physical E` certificate on that full direct sum.
For the displayed Haegeman observable map, the even and odd images require
different `h`-dependent signs on the outer/B seam faces. The runner checks
that the disagreements number `3L^2 = 27,48,75`, while all outer/B faces
number `3L^3 = 81,192,375`. No single bounded sector-blind `G_physical` is
inferred from the matching rank.

Its supplies are equally exact:

| `L` | `h_111` membrane weight | charge-Wilson constraint weight |
|---:|---:|---:|
| 3 | 27 | 15 |
| 4 | 48 | 18 |
| 5 | 75 | 21 |

The common Wilson cohomology class is preserved under all 24 proper-cubic
frames: every rotated `h_111` differs from the displayed representative by a
cut. But the chosen direction-mode reference has a six-element frame orbit.
Rotating the reference produces a covariant family; one selected reference is
not invariant. It is also moved by each of the six nonzero unit translations.
The noncontractible charge-Wilson link and reference selection are supplied
global/topological structure, not locally enforced auxiliary constraints.

A boundary, puncture, ungauged vertex, or auxiliary reference matter charge
can play the same charge-sink role only after its placement and physical
status are supplied. This cycle does not relabel any such resource as local.

## Mass and seam disposition

The reference-charged odd `V_(r,h)` is a lawful normalized state image on the
declared **fermion-plus-gauge** domain. All Cycle-230 update factors are parity
even, so the observable intertwiner applies sectorwise. The runner therefore
retains, conditionally:

- the Cycle-219 rest-mass identity at `beta=-0.35`, with relative residual
  below `2e-12`;
- the Cycle-230 principal sea rank `73`, hence odd total parity; and
- the held shrinking-seam block with singular values
  `[0.9998884863600149,1]`.

These are not reported as a physical-M2 CAR intertwining residual. The state
image is lawful only with a supplied reference charge and common-Wilson
resource, and the matter carrier has not been compiled from CAR to bounded
ordinary qubits. If either the odd reference twist or `h_111` is deleted, the
standard projection has norm zero or the common-parity label reverts to
`000`; the odd fixture claim is then withdrawn.

## Constraint, leakage, deletion, and held-size controls

- Every mapped Pauli term satisfies `partial c=a`; its Gauss leakage is zero.
- Deleting the single-face dressing from a `B` hopping term creates exactly
  two endpoint Gauss violations.
- Every state image satisfies all local-flat and selected Wilson constraints.
- Deleting one independent Gauss or flatness constraint adds exactly one
  spurious logical qubit.
- Deleting the marked negative Gauss background makes the closed odd
  projection zero.
- Deleting the three-membrane `h_111` changes the odd Wilson label to `000`.
- Deleting the `h`-dependent observable prefactors makes the odd sector see a
  seam-twisted update; using them as a fixed gate table supplies the membrane.
- `L=3,4` ranks, overhead, membrane weights, charge-link weights, and sign
  strings predict the held `L=5` values exactly.
- The all-frame test covers the graph, onsite chain sets, common Wilson
  cohomology, and reference orbit. The translation control moves the selected
  reference under all six nonzero unit translations. Neither control calls a
  selected reference invariant.

## State preparation versus algebra locality

The operator map is local because every declared symmetric operator is
dressed inside a bounded graph neighborhood. That fact does not prepare

```text
2^(-(6L^3-1)/2) sum_[s] (-1)^(r dot s)
Z_m^s |psi> |h+delta s>_g.
```

The state sum has cut-orbit exponents `161,383,749` at `L=3,4,5`. The
selected `111` representative has membrane weights `27,48,75`. A product of
parallel local `X` gates could write a **known** membrane pattern, but its
noncontractible support, origin, common label, correlation with the input
parity, and marked charge would all remain supplied. Cycle 240's local
projection/global-decoder split is not erased by rewriting the projector as
an isometry.

No state-preparation theorem, occurrence law, or host-free sector-selection
law is claimed.

## Supplied-structure inventory

This cycle supplies:

1. the Cycle-235 square-pyramid graph and a `Z_2` gauge qubit on every edge;
2. one retained matter carrier on every six-mode vertex;
3. a global parity sector for each sectorwise map;
4. the charge-background word `r` and its marked reference in the odd sector;
5. the flat representative `h`, including three noncontractible membranes
   for `111`;
6. local-flat and equal-Wilson constraints plus the nonlocal charge-Wilson
   link;
7. the minimum-chain averaging prescription for onsite observables;
8. the within-cell matter-mode Pauli/Jordan–Wigner convention;
9. the Cycle-219 coin and mass parameter;
10. the Cycle-230 contact, coupling, torus, sea cut, seam sample, and `A/B`
    order; and
11. any preparation of the charge, Wilson, gauge, marker, or matter state.

None is promoted to a framework law or axiom.

## No-go discipline gate

The negative claims under review are deliberately narrow:

1. the standard all-plus closed state-gauging map annihilates the odd sector;
2. on the tested Cycle-235 ordering, gauging the actual Jordan–Wigner image
   does not remove its growing matter strings; and
3. replacing those strings by the displayed hard-core local image does not
   reproduce the incident-edge even-CAR algebra.

N1–N8 passes those finite statements. It fails a general fermion-to-qubit
no-go, a minimum-resource theorem, or axiom pressure.

### N1 — alternative-route enumeration

| Route | Honesty marker | Attempt and disposition |
|---|---|---|
| standard all-plus closed gauging | ATTEMPTED | exact cut-rank/isometry works for `Q=+1`; the odd projector norm is exactly zero |
| marked negative Gauss charge | ATTEMPTED | restores an exact odd sector isometry, but supplies a reference with a six-frame orbit |
| equal-Wilson direct sum | ATTEMPTED | restores the exact `6L^3` rank and cubic sector label, but its charge-Wilson link grows with `L` |
| retain fermionic matter | ATTEMPTED | gives a valid local gauged even-CAR map and conditional odd fixtures, but the target still contains fermionic matter rather than only physical M2 sites |
| ordinary hard-core matter qubits | ATTEMPTED | local gauged FSWAP exists, but incident edge generators commute instead of obeying the tested CAR anticommutation graph |
| Jordan–Wigner matter followed by gauging | ATTEMPTED | exact observable map retains maximum strings `54,96,150` and adds one gauge face |
| boundary/ungauged charge sink | ATTEMPTED | at contract level it removes the closed-neutrality premise, but boundary placement and distance/resource obligations replace it; no bounded all-frame fixture was constructed |
| supplied topological/PEPS preparation | ATTEMPTED | at contract level it can provide a gauged state resource, but it does not by itself turn the retained matter carrier into bounded M2 CAR or derive the reference/sector selection |

The successful marked-charge construction blocks a broad parity-sector
no-go. The live boundary, auxiliary, and non-Clifford possibilities block a
general compiler no-go.

### N2 — condition-independence audit

After collapsing downstream fixture claims, three open conditions remain:

- `K_CAR`: a bounded ordinary-M2 representation of the retained even CAR
  matter algebra;
- `K_charge`: a physical, covariant odd charge/reference/common-Wilson
  resource rather than the supplied marked/topological data here;
- `K_prepare`: an autonomous physical preparation of the gauged code and its
  selected resource state.
- `K_join`: one bounded physical update intertwining both the `000` even and
  `111` odd sector maps without a Wilson projector or supplied membrane signs.

| Pair | First closes second? | Second closes first? | Independent counterfixture |
|---|---:|---:|---|
| `K_CAR` / `K_charge` | no | no | Cycle-235 local even algebra lacks odd state / this cycle's odd state retains fermionic or JW matter |
| `K_CAR` / `K_prepare` | no | no | local operator dictionary need not prepare its code / an even gauge state can be prepared without solving CAR signs |
| `K_charge` / `K_prepare` | no | no | algebraic marked odd isometry has no autonomous prep / a prepared even code does not choose an odd reference |

`K_join` is downstream of choosing both sector maps but is not closed by their
rank equality: the explicit `3L^2` stream-sign disagreement is its independent
counterfixture. It could be closed by a different local dynamical control, so
it is not merged into a no-go claim.

Conditional fixture intertwining is downstream and is not inflated into a
separate wall.

### N3 — hidden-condition scan

The mandatory phrase scan exposes: connected closed periodic graph, retained
matter type, fixed input parity, charge-background word, flat connection,
marked reference, local-cycle basis, Wilson representatives, minimum-chain
average, mode order, torus origin, and preparation. “By construction” is used
only for displayed finite definitions. “Standard” refers only to the cited
Haegeman globally invariant input contract. No “framework provides,”
“naturally,” “obviously,” or “canonical” phrase carries a hidden condition.

### N4 — residual matching

| Witness and exact surface | Witness residual | Cycle-245 residual | Match? |
|---|---|---|---:|
| Haegeman et al., arXiv:1407.1025, main-text state/operator-map construction | state gauging and local symmetric-observable map on globally invariant input | standard `Z_2` even-sector map and operator image | yes |
| `EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md:74,96-107` | closed face code has exact local even algebra but absent total-odd state sector | standard all-plus closed gauging also enforces total neutrality | yes, only at odd-sector boundary |
| `QCA_ISOMETRY_SQUARE_PYRAMID_CYCLE241_NOTE_2026-07-17.md:66-70,184` | equal-Wilson rank schema has a parity slot but no state/operator map | sector maps and charge-Wilson link are now instantiated | yes |
| `SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md:45-56` plus Cycle 235 `:96-107` | update factors are parity even; required one-particle and rank-73 sectors are odd | odd reference image exists conditionally and operators intertwine sectorwise | yes |
| `MEASUREMENT_FEEDFORWARD_SQUARE_PYRAMID_PREPARATION_CYCLE240_NOTE_2026-07-17.md:130-145,233-235` | local constraint projection does not derive covariant global correction/sector preparation | isometry formula still leaves reference/Wilson preparation supplied | yes |
| `DISTINGUISHABLE_ANTISYMMETRIC_FOCK_COMPILER_CYCLE239_NOTE_2026-07-17.md:472,488-489` | global algebraic state isometry need not be bounded physical-site encoding | gauging isometry with retained matter is not silently called physical M2 `E` | yes, contract distinction only |

No citation about even-sector locality is used as evidence for a full state
compiler.

### N5 — resolution/rhetoric audit

| Resolution | Tested negative | Not established |
|---|---|---|
| one edge | hard-core gauged FSWAP matrix and both Heisenberg directions | every possible local fermionic code |
| incident edge pair | hard-core pair commutes; Cycle-235 framed CAR pair anticommutes | arbitrary non-Pauli/off-code dressings |
| one six-mode cell | coin/contact/A images bounded in 18 carriers | complete physical state preparation |
| `L=3,4,5` | ranks, odd sector, Wilson resources, and the stated JW order | every ordering, boundary, or encoder family |
| all 24 frames and six unit translations | onsite chain family and common cohomology exact; selected reference orbit six and no nonzero unit translation fixes it | impossibility of a covariant auxiliary reference |
| lattice-wide closed map | all-plus Gauss product fixes total parity even | open, punctured, or generalized gauging maps |

Accordingly the note says “this map/order/presentation does not close the
compiler,” never “gauging cannot encode fermions.”

### N6 — partial-closure paths

The constructive partial closures are explicit. Retaining fermionic matter
closes state gauging and even-observable locality. A marked reference plus
`111` closes the algebraic odd-sector rank. A boundary or ungauged vertex can
replace the marked closed charge. A separate auxiliary-Majorana,
Chen–Kapustin, non-Clifford, or subsystem compiler could close `K_CAR`. A
measurement, PEPS, or cellular preparation rule could close `K_prepare`.
These are import-retirement targets, not proposed axioms.

No claim that “no retained primitive supplies this” is made, so no primitive
registry promotion or governance inference is needed.

### N7 — steelman

> The negative compiler disposition is much narrower than the constructive
> result. The state gauging map is an exact isometry, its symmetric-observable
> map is local in both declared Heisenberg directions, and the marked-charge
> common-Wilson direct sum already carries both parity sectors at exact full
> rank. Haegeman et al. explicitly allow fermionic PEPS matter as a future
> implementation class, while Cycle 235 already has a local even-CAR face
> algebra. A generalized gauging map that leaves a charge sink ungauged, or a
> non-Clifford/subsystem map that replaces the retained matter qubits, could
> join these pieces without Jordan–Wigner strings. The present runner tests
> only the ordinary-qubit hard-core substitution and one explicit JW order;
> it cannot support a general fermion-to-qubit no-go.

The steelman is convincing. Broad impossibility and minimum-resource claims
are therefore rejected.

### N8 — cross-cycle echo

- Cycle 230 separates intrinsic CAR dynamics and odd fixtures from a physical
  site compiler.
- Cycle 235 constructs local even algebra but fixes total parity even on a
  closed domain.
- Cycle 240 separates local projection from global decoding/preparation.
- Cycle 241 identifies the equal-Wilson rank slot while leaving its state map
  live.
- Cycle 242 retains Haegeman-style sector gauging as the next constructive
  discriminator rather than treating prior failures as a no-go.
- Cycle 243 keeps compiler/update order separate from causal event order and
  physical clock comparison.

Cycle 245 advances the live route: the state and operator maps now exist, and
the remaining CAR, charge-resource, and preparation conditions are more
sharply separated. The recurring sector/resource mechanism is a partial
closure path, not constitutional evidence.

## TOE dependency ledger after Cycle 245

| Wall | Change | Remaining dependency |
|---|---|---|
| `C_ref` | marked charge, flat representative, and common Wilson label are explicit | physical covariant selection/preparation remains supplied |
| `C_num` | exact even/odd sector isometries and a full-rank common-parity direct sum are constructive | parity is not derived as a physical local matter observable/resource |
| `C_wrap` | unchanged | Wilson/holonomy label, gauging sum, and update count are not time or realized winding history |
| `C_int` | coin/contact and conditional odd seam intertwine in the fermion-plus-gauge map | physical M2 CAR image, coupling selection, and phase-to-rate bridge remain open |
| `C_local` | materially clarified | exact 21-site/cell sector gauging and local symmetric algebra; a single two-sector physical update, retained-matter sign compiler, and autonomous state preparation remain open |
| `C_source` | unchanged | no energy/stress/action source or gravitational response is selected |

Maturity remains operational quantum/records `2/5`, causal time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.

## Time firewall

The graph is spatial and the gauging map is an algebraic isometry. Its sum
index, projector factors, constraint-measurement rounds, circuit depth,
membrane-writing layer, `A/B` schedule, QCA range, and update opportunity are
compiler coordinates. None is a causal occurrence, Record, clock count,
metric duration, or physical rate. The contact phase is not energy and no
generator element is called a rate.

## Verification

```bash
python3 scripts/haegeman_parity_sector_gauging_cycle245_2026_07_17.py
```

The runner executes the finite ranks/isometry, exact edge matrices, full
six-mode Pauli images, all-frame chain and cohomology tests, common-Wilson
constraint ranks, fermion-sign discriminator, deletion/leakage controls, odd
mass/seam eligibility, held sizes, state-preparation separation, and note
contract.
