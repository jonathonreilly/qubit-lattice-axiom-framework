# Route 2 scalar-reference local-gauge CAR architecture — Cycle 232

**Date:** 2026-07-17

**Type:** conditional odd-volume even-algebra representation plus two
falsified local-compiler attempts

**Status:** bounded update gates and algebraic exactness on odd finite sectors,
but no bounded-radius local state encoding; even volumes also fail

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

**Packaging:** draft parking branch and existing draft PR #5389 only

Companion runner:

```text
scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py
```

This note and runner change no foundation, axiom, Qualification, primitive,
registry, policy, audit, or queue surface.

## Result up front

Route 2 has one strong but qualified algebraic representation and two useful
falsifications.  It **does not pass the full compiler contract**.

The retained construction adds one cubic-scalar reference fermion `r_x` to the
six Cycle-230 matter modes at every coarse cell.  Nearest-neighbor local
constraints force all reference occupations to agree,

```text
D_(xy) = B_(r_x) B_(r_y) = +1,
B_q = (-1)^(n_q).
```

Apply the Bravyi–Kitaev superfast encoding to the **even sector** of these
`7 N_c` fermion modes.  Full loop stabilization leaves `7 N_c-1` logical
qubits.  The local `D_(xy)` constraints have rank `N_c-1`, so the lawful code
has exactly

```text
(7 N_c - 1) - (N_c - 1) = 6 N_c
```

logical qubits, the dimension of the full original six-mode Fock space.

The dimension count becomes the correct **sectorwise operator representation**
on odd finite volumes.  Let the common local reference parity be `b`.  The superfast
even-sector identity gives

```text
P_matter b^N_c = +1.
```

When `N_c` is odd, `b=P_matter`; the two uniform reference sectors carry the
even and odd matter parity blocks.  Every original parity-even gate acts only
on matter and leaves the reference sector inert.  Therefore, with

```text
E_p |psi_p> = J_BKSF ( |psi_p>_matter tensor |b=p>_r^(tensor N_c) ),
E = E_+ direct_sum E_-,
```

the encoded update satisfies on the declared sectorwise code

```text
E G_coarse = G_physical E.
```

No update gate queries, computes, transports, or broadcasts `P_matter`; all
reference constraints and update gates are bounded and local.  Nevertheless,
the uniform reference field is a **global parity bus implemented by local
repetition constraints**.  More decisively, on the odd-volume lawful code,

```text
B_(r_x) = P_matter                 for every cell x.
```

Suppose `E` were the required bounded-radius locality-preserving state
encoding.  Then `E^dagger B_(r_x) E` would have bounded support near `x`.  Pick
two coarse product states identical throughout that neighborhood and differing
by one occupied matter mode farther away.  Every bounded local observable has
the same expectation in the two states, while `P_matter` differs by sign.
This contradicts the displayed code identity.  The runner instantiates the
witness at radii `0,1,2,4` on successively larger odd tori: every local
expectation gap is `0` and every required parity gap is `2`.  For arbitrary
fixed radius `R`, choose an odd torus with `L>2R+1` and move the occupied mode
outside the `R`-ball; the same contradiction proves the size-independent
claim.

Thus the displayed `E_+ direct_sum E_-` is a sectorwise **global prepared
isometry**, not the local encoding required by the tournament.  Route 2
satisfies only the narrow update-time statement “no runtime nonlocal parity
service.”  It fails the full “bounded local `E`, no global parity service or
carrier” success condition.  Sector preparation is supplied and nonlocal.

The odd-volume qualification is real.  When `N_c` is even, `b^N_c=+1` and the
same code contains two copies of the even matter sector rather than both
parities.  The runner verifies success at `L=3,5,7` and this exact failure at
held-out `L=4`.  Thus this route does **not** provide the requested
held-out-all-sizes compiler.

The rejected alternative doubled every matter mode with a same-port
pair-shadow and used `V|n>=|n,n>`.  For a bounded region `S`, the non-naive lift

```text
U_hat_S = V_S U_S V_S^dagger + (I-P_S)
```

is locally unitary, even, constraint preserving, and has zero local
intertwining residual.  But those local lifts do not assemble into a single
global encoding on a graph with non-contiguous edges.  The runner expands the
exact two-mode lift into even Majorana monomials and embeds a swap of original
modes 0 and 2 across spectator mode 1.  Its local residual is zero while the
global residual is

```text
|| U_hat_(0,2) V_3 - V_3 Gamma(swap_(0,2)) || = sqrt(8)
                                                  = 2.8284271247461903.
```

The duplicated spectator has even parity, so it erases the original single
fermion crossing sign.  Correct dimension alone was not enough.  That route is
falsified at this exact assembly resolution; it is not used in the theorem.

The scalar-reference representation carries the odd `L=3` one-particle and
rank-73 sea sectors, preserves the one-particle mass fixture, and reproduces
the Cycle-230 contact seam block once its nonlocal sectorwise isometry is
supplied.  It does not select a local compiler, coin, coupling, gate order,
sea, clock, energy, record, probability law, or gravitational source.  No
axiom conclusion follows.

## Interaction graph and local code

Each coarse cell has six matter vertices in the proper-cubic octahedral mode
graph and one scalar reference vertex.  The graph has:

```text
12 nonopposite matter edges/cell,
 6 reference-to-matter spokes/cell,
 3 matter stream edges/cell,
 3 reference lattice edges/cell,
24 abstract BKSF edge qubits/cell.
```

Every bulk matter vertex has degree 6; every reference vertex has degree 12.
The graph is connected, translation invariant, and invariant under all 24
proper-cubic frames.

For one qubit on each abstract graph edge, choose a local orientation and a
local ordering of incident ports and use

```text
B_tilde_v = product_(e incident v) Z_e,
A_tilde_uv = epsilon_uv X_uv
             product_(e <_u uv) Z_e
             product_(e <_v uv) Z_e.
```

The runner instantiates every `A,B` Pauli on periodic `L=3` and verifies the
endpoint CAR commutation rules.  For any graph loop `zeta`, the BKSF loop
operator commutes with this even algebra.  The local reference constraint is

```text
D_tilde_(xy) = B_tilde_(r_x) B_tilde_(r_y),
```

with weight at most 22.  It commutes with every matter update and every loop
stabilizer.

The genuine bounded loop family is:

1. twelve `r-m_a-m_b` triangles per cell, one for every nonopposite pair;
2. one four-edge reference/matter rectangle per coarse bond; and
3. elementary **eight-edge** matter plaquettes: four stream edges plus four
   intracell perpendicular port turns.

The four turn edges are load bearing.  Omitting them produces a collection of
eight degree-one port endpoints, not a graph cycle.  The runner checks zero
boundary for every retained loop before computing ranks.

The exact ranks are:

| Domain | Local loop rank | Full cycle rank | Unfixed Wilson labels |
|---|---:|---:|---:|
| open `L=3` | 406 | 406 | 0 |
| periodic `L=3` | 457 | 460 | 3 |
| periodic `L=4` | 1086 | 1089 | 3 |
| periodic `L=5` | 2123 | 2126 | 3 |
| periodic `L=7` | 5829 | 5832 | 3 |

On periodic `L=3`, the actual loop Paulis and `D` constraints have zero
commutator failures, combined independent rank 483, and maximum Pauli weight
36.  Every redundant stabilizer relation reduces to `+I`, never `-I`.  They
also have zero commutator failures against every mapped matter update
generator.  Three explicit noncontractible reference Wilson loops raise
the combined rank to 486 with zero update commutator failures.  The three
cycles missing from the bounded family are the torus Wilson/spin-structure
labels.  If
only bounded local constraints are imposed, the lawful space is

```text
Fock_coarse tensor C^8_Wilson.
```

All update generators commute with those labels.  The untwisted
`(+,+,+)` sector is invariant under all proper-cubic frames and reproduces the
periodic Cycle-230 fixture.  Selecting that sector is supplied boundary data;
the update does not maintain it through a nonlocal service.  These are **three
torus Wilson spectators**, distinct from the uniform parity reference.

## Exact BKSF interface and off-code unitarity

The scalar-reference construction uses the ordinary superfast even-algebra
map directly; it does not infer an edge-qubit gate merely from a dimension
count.

The Cycle-230 macrostep is

```text
G_coarse = W_g Gamma(B) Gamma(A) Gamma(C),
S = B A.
```

Every factor is parity even and supported on a bounded connected matter
region:

- `Gamma(C)` is an onsite six-mode even unitary;
- every `A` or `B` stream factor is a two-mode FSWAP;
- `W_g` is an onsite occupation polynomial.

The connected octahedral-plus-spoke graph makes the entire onsite even algebra
available.  Opposite matter ports use a two-edge intracell path; no path leaves
the cell.  Replacing its fermionic `A,B` generators with the instantiated
Paulis gives the physical edge-qubit operator on the stabilizer code.

For off-code unitarity, choose a Hermitian logarithm `h_R` of each bounded
parity-even local gate, map `h_R` through the `A,B` algebra, and apply

```text
G_physical,R = exp(-i BKSF(h_R)).
```

This is unitary on the **full** physical-qubit Hilbert space, commutes with the
loop and `D` projectors, and restricts to the desired gate on the code.  The
runner constructs the two-mode FSWAP logarithm explicitly and recovers FSWAP
with residual `3.60e-16`.  The onsite coin and contact are the same
finite-dimensional construction on a fixed 24-edge neighborhood.  This is an
exact bounded algebraic gate representation, not a bounded state encoding or
an executed fault-tolerance protocol.

The matter update never contains `A` with a reference endpoint.  Its mapped
`A` weights are at most 11.  The complete graph has `A` weight at most 23,
`B` weight at most 12, and reference `D` weight at most 22.  An onsite matter
operator touches at most 24 abstract edge qubits.  All bounds are independent
of `L`.

## Physical `M_2` placement

The 24 abstract edge qubits are placed on an explicit proper-cubic set of
physical lattice sites.  This is a candidate physical architecture for the
bounded update gates; it does not repair the nonlocal state isometry.  Use
coarse-cell spacing 16 and direction vectors `D_a`:

```text
octahedral edge (a,b):       2(D_a+D_b)       [12-site orbit],
reference-matter spoke a:    4 D_a            [ 6-site orbit],
reference bond along a:      8 D_a            [ 3 sites/cell after sharing],
matter stream along a:      (8+/-1) D_a       [ 6 sites/cell after sharing].
```

The matter-stream edge qubit uses a two-site repetition code at the last pair;
this avoids oriented bond ownership under a frame.  Its local constraint is
`Z_1 Z_2=+1`, with logical `Z=Z_1` and `X=X_1 X_2`.  The runner constructs the
isometry and obtains zero `X,Z` residual.

The global centered position set has 36 sites because it displays both halves
of all incident bonds.  After bond sharing, the accounting is

```text
12 + 6 + 3 + 6 = 27 physical M2 sites per coarse cell.
```

The runner checks that the full set is invariant under all 24 proper rotations.
Its largest offset is 9 and the macro spacing is 16, so nearest-neighbor
routing through the fixed blank sites of this bounded macrocell is a constant
physical circuit.  The position rule, stream repetition, blank routing, and
gate schedule are supplied compiler structure.  No layer count or compiler
substep is interpreted as physical time.

As a direct geometry control, a `3^3` positive-bond patch contains exactly
`27*27=729` distinct active sites.  Every active site has a blank-only path to
the cell-center routing hub inside the fixed radius-9 cube; the longest tested
path has 11 nearest-neighbor edges.

## Proper-cubic covariance and local port-order gauge

The raw BKSF Pauli formula contains a local port order and therefore is not a
geometric tensor.  On `L=3`, raw frame permutation produces 12,948 generator
mismatches.  Changing adjacent incident-edge order `e<f` to `f<e` is
conjugation by vertex-local `CZ_(ef)`; an edge-orientation sign is repaired by
local `Z_e`.  For each of all 24 frames, the runner constructs these local
repairs and checks every `A_e` including its phase.  The corrected mismatch
count is zero.  Every `B_v` and the `D` constraint family map directly.

Thus covariance uses a **local port-order gauge**, not a global Jordan–Wigner
ordering or preferred cubic frame.  The reference mode is a proper-cubic
scalar, the Cycle-219 coin commutes with all direction frames, and the contact
depends only on cell number.  The physical layout is separately frame
invariant.

## Mass, sea, contact, leakage, deletion, and held-out controls

On `L=3`, a single matter particle is accompanied by 27 occupied reference
modes, giving extended occupation 28 and even total parity.  The vacuum uses
the empty uniform reference sector.  The Cycle-230 principal sea has occupied
rank 73; with 27 occupied references it has extended occupation 100.  Thus the
one-particle and sea sectors are present in the same physical code family.

Because encoded gates act as the original matter gates tensor the reference
identity, their matrix elements are unchanged.  The runner verifies:

- exact matter FSWAP intertwining in both fixed reference occupations;
- held-out `beta=-0.35` rest/curvature mass residual
  `3.6800564e-08`;
- contact identity on matter `N=0,1` and exact deletion at `g=0`;
- the Cycle-230 contact seam block singular values
  `0.49577141, 0.45566605`;
- exact `1/L^3` spatial normalization and all 24 seam-block frames; and
- zero ideal leakage because the matter update commutes with every reference,
  loop, and stream-repetition constraint.

The size controls are intentionally asymmetric: odd `L=3,5,7` pass the full
matter-parity domain; held-out even `L=4` fails.  Deleting the scalar references
returns the ordinary single-copy BKSF dimension `6N_c-1`, explicitly losing
one parity block.  Deleting a reference-equality constraint admits nonuniform
reference defects and a spurious logical degree.  Arbitrary physical noise,
syndrome extraction, code preparation, and an error threshold are not tested.

## Supplied-structure inventory

The construction supplies:

1. one scalar reference fermion per coarse cell;
2. the nearest-neighbor reference-equality constraint;
3. the odd finite-volume lawful domain;
4. the 24-edge/cell octahedral/reference interaction graph;
5. the BKSF loop presentation, local port ordering, and its gauge repairs;
6. the untwisted torus Wilson/spin sector;
7. the spacing-16, 27-site/cell physical macrocode, stream repetition, blanks,
   routing, and schedule;
8. uniform-sector preparation for each matter parity;
9. a bounded Hermitian-log branch for each local gate; and
10. the Cycle-219 coin, Cycle-230 contact, coupling, and gate order.

No host process chooses gates from the state.  The local reference field is
never read during evolution, but it does carry a redundant global sector label
and is therefore not hidden behind the word “gauge.”  The compiler schedule is
supplied spatial-QCA law structure, not a clock, rate, time metric, or winding
history.

## Prior work and novelty boundary

This route does not claim a new general fermion-to-qubit mapping.

- Setia, Bravyi, Mezzacapo, and Whitfield, “Superfast encodings for fermionic
  quantum simulation,” *Physical Review Research* **1**, 033033 (2019),
  <https://doi.org/10.1103/PhysRevResearch.1.033033>, supply the edge-qubit
  `A,B` representation, loop stabilizers, bounded weights, and the
  even-sector `m-1` logical-qubit theorem used here.
- Farrelly and Short, “Causal Fermions in Discrete Space-Time,” *Physical
  Review A* **89**, 012302 (2014),
  <https://doi.org/10.1103/PhysRevA.89.012302>, give an auxiliary-Majorana
  qubit-subsector construction for causal fermionic dynamics.  It remains a
  distinct live route; its Jordan–Wigner presentation is not imported here.
- Chen, “Exact bosonization in arbitrary dimensions,” *Physical Review
  Research* **2**, 033527 (2020),
  <https://doi.org/10.1103/PhysRevResearch.2.033527>, gives a local fermion/gauge
  duality in three dimensions with modified Gauss law and explicit spin
  structure.  It supports the torus-sector boundary and remains an alternative
  geometric compiler.

The fixture-specific work is the cubic scalar-reference graph, odd-volume
parity-sector calculation, exact Cycle-230 gate interface, frame gauge and
physical placement, and the executable pair-shadow counterexample.  Global
priority is not claimed.  Thirring machinery is neither used nor compared.

## TOE dependency ledger after Route 2

| Workstream | Route-2 effect | Remaining content |
|---|---|---|
| `C_ref` | unchanged | physical phase origin, sea, and preparation remain unselected |
| `C_num` | supplied parity carrier exposed | odd domains carry both parity blocks, but the reference/superselection meaning is not derived |
| `C_wrap` | unchanged | no compiler layer, Wilson label, or reference bit is a clock or winding carrier |
| `C_int` | representation gain | the supplied contact is compiled; interaction selection and rate/protection remain open |
| `C_local` | narrowed algebraic gain, compiler still open | bounded physical gate representation on supplied odd sectors, but bounded-radius `E` is obstructed for this construction and even sizes fail |
| `C_source` | unchanged | no energy/stress/source ledger is selected |

The evidence does not change the 0–5 TOE scores: operational quantum/records
`2`, time `1`, inertia/matter `3`, gravity/source `2`, Born/probability `1`.
This is substrate compatibility evidence, not Record formation, time, source,
or probability.

## No-go discipline gate

No route-independent compiler impossibility, minimum overhead, or axiom
pressure is claimed.  The pair-shadow failure is narrow, and the scalar
reference construction is conditional.  The current `origin/main` N1–N8 gate
was applied.

**N1–N8 result:** **PASS for the narrow odd-volume scalar-reference algebraic
representation, its bounded-`E` obstruction, and the exact pair-shadow
counterexample.  FAIL for any broad
compiler no-go, full-held-out-size success, no-global-parity-carrier success,
uniqueness, minimality, or axiom-pressure claim.**

### N1 — alternative routes

| Route | Marker | Disposition |
|---|---|---|
| single-copy BKSF | **ATTEMPTED** | bounded and covariant after gauge repair, but exact dimension is `6N-1`; odd matter parity is absent |
| non-naive local pair-shadow lifts | **ATTEMPTED** | local residual zero; global non-contiguous-swap residual `sqrt(8)`, so this assembly is falsified |
| scalar-reference BKSF | **ATTEMPTED** | sectorwise algebra exact for odd `L=3,5,7`, but `B_r(x)=P_matter` obstructs bounded-radius `E`; even `L=4` also fails |
| auxiliary-Majorana cancellation | **LIVE, NOT RULED OUT** | Farrelly–Short establish the general route; no local-constraint instantiation for this fixture was completed |
| exact 3D higher-form bosonization | **LIVE, NOT RULED OUT** | Chen establishes locality with spin-structure data; no fixture-specific gate runner was completed |
| generalized superfast or different cubic edge code | **LIVE, NOT RULED OUT** | could change overhead, constraints, or error properties; not tested here |

At least three live alternatives defeat every route-independent negative or
minimum-content inference.

### N2 — condition independence

The raw conditions collapse to four: `K_parity` (scalar reference plus odd
domain and nonlocal sector preparation), `K_spin` (torus Wilson sector),
`K_frame` (local port gauge), and `K_layout` (physical repetition/macro-routing).
Odd volume is downstream of this specific parity-reference design and is not
inflated into a fifth wall.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---:|---:|---:|
| `K_parity`, `K_spin` | no | no | yes |
| `K_parity`, `K_frame` | no | no | yes |
| `K_parity`, `K_layout` | no | no | yes |
| `K_spin`, `K_frame` | no | no | yes |
| `K_spin`, `K_layout` | no | no | yes |
| `K_frame`, `K_layout` | no: Pauli presentation gauge does not place sites | no | yes |

None is called axiom content.

### N3 — hidden-condition scan

The mandatory scan for “we assume,” “by construction,” “as is standard,” “the
framework provides,” “bridge context,” “background,” “naturally,” “obviously,”
“standard QFT,” “registered,” and “canonical” promotes no new condition.

| Hit | Classification |
|---|---|
| “construction” | non-load-bearing label; all load-bearing choices are in the supplied inventory |
| “approved registry” below | methodology metadata; it supplies no compiler law |
| “background parity/spin” avoided | parity reference and torus spin sector are explicit supplied data |

Odd volume, uniform preparation, local port gauge, Hermitian-log branches,
macro blanks/routing, and gate order are all named.  No substep is renamed
physical time.

### N4 — residual matching

| Cited witness | Witness residual | Route-2 use | Match? |
|---|---|---|---:|
| `SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md:111-125` | `M_64` intrinsic CAR lacks physical `M_2` compiler | constructs a qualified 27-site update-gate architecture, but bounded state `E` fails | yes, partial |
| same file `:553-559` | intrinsic locality/contact stop before onsite-qubit interface | preserves the contact and builds one interface | yes |
| same file `:615` | parity/gauge block encoding unbuilt | executes two attempts; retains only an odd-domain sectorwise algebra representation | yes, partial |
| `FOCK_MODULAR_BOUNDARY_CURRENT_CYCLE229_NOTE_2026-07-17.md:175-187` | spectral JW matrices are not a spatial compiler | uses local edge qubits and genuine stabilizer loops | yes |
| `MINIMAL_AXIOMS_2026-06-29.md:36-40` | each physical site has algebra `M_2(C)` | every active carrier is one physical qubit | yes, interface only |
| Setia et al. 2019 | ordinary superfast code is the even sector | reference repetition repairs both sectors only on odd volume | yes |
| Chen 2020 | spin structure is explicit in local bosonization | three Wilson sectors remain boundary data | yes |
| scalar-reference code identity | `B_r(x)=P_matter` on every odd-volume lawful sector | bounded-radius pullback has local gap `0` while required parity gap is `2` | yes, exact route-specific obstruction |

No citation is used for a uniqueness, minimum overhead, or impossibility claim.

### N5 — resolution audit

| Resolution | Tested | Not established |
|---|---|---|
| local pair shadow | exact local gate | global graph assembly; explicitly fails one three-mode test |
| per BKSF edge | exact `A,B` Paulis and CAR commutators | fault tolerance |
| local loops | zero boundary, Pauli commutation, exact ranks | autonomous syndrome extraction |
| odd `L=3,5,7` | both matter parity sectors | even-volume closure |
| even `L=4` | exact parity-sector failure | an alternative even-size repair |
| bounded-radius `E` | exact contradiction for this scalar-reference full-parity code | other local-gauge encodings or a route-independent compiler obstruction |
| periodic torus | three inert Wilson spectators | bounded local selection of one spin sector |
| all 24 frames | graph, constraints, phases, layout, coin/contact | boosts or Lorentz closure |
| one particle | odd sector and held-out mass | dressed interacting mass |
| rank-73 sea/seam | exact contact block | selected vacuum, rate, or instability |
| physical time | not tested | clock, metric, winding, rate |

"No nonlocal parity service" is therefore used only in the narrow update-time
sense.  The bounded local state-encoding and no-global-carrier readings fail.

### N6 — partial-closure and primitive scan

The fresh `origin/main` no-go skill and
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` were followed.  Scale
reference supplies units only, kinetic isotropy supplies only `c_t=c_s` form,
and realized state supplies only a pointwise evaluation slot.  None selects the
reference graph, odd domain, spin sector, port gauge, layout, coin, or contact.
Their limited grants are not classified as walls.

Live partial-closure paths are:

| Path | Status | Possible effect |
|---|---|---|
| different local parity reservoir valid for every `L` | unbuilt | retire the odd-volume condition |
| direct exact 3D bosonization | primary-source live route | avoid or reclassify the uniform parity carrier |
| auxiliary-Majorana local constraint compiler | primary-source live route | alternative full gate representation |
| formulate one physical infinite-volume representation | unbuilt | replace finite total-parity bookkeeping with a quasi-local sector theorem |
| derive graph/layout from the admissibility law | unbuilt | retire compiler-law selection |

These are construction routes, not proposed premises.

### N7 — steelman

> The scalar-reference result may simply hide the forbidden global parity
> service in a ferromagnetically repeated local bit.  In fact, on the code
> `B_r(x)=P_matter`, so no bounded-radius locality-preserving `E` can encode both
> parity sectors: a remote occupation flips the right side without changing
> any coarse state near `x`.  Preparing `b=-1` at every cell already requires
> knowing that the matter sector is odd, and the exact repair fails every even
> volume.  The three Wilson labels and fixed BKSF port gauge add more supplied
> structure.  Exact 3D bosonization or an
> auxiliary-Majorana compiler may avoid these defects.  Therefore this is a
> useful odd-domain simulator, not the requested volume-independent physical
> compiler and certainly not evidence that the substrate selected fermions.

That steelman is convincing.  It forces the route disposition and blocks a
full success or axiom-pressure claim.  If “encoding” were weakened to a
sectorwise global isometry and only update gates had to be local, the exact
odd-domain intertwining would survive; the tournament explicitly asks for a
local encoding, so that weaker reading is insufficient.

### N8 — cross-cycle echo

The prescribed repository phrase search and physics-loop `NO_GO_LEDGER.md`
walk were rerun.

| Earlier boundary | Mechanism since | Effect here |
|---|---|---|
| Cycle 229 spatial compiler absent | Cycle 230 built intrinsic CAR | this route attacks only the remaining `M_2` interface |
| Cycle 230 grouped capacity, parity locality, and CAR as one compiler obligation | scalar reference addresses them jointly on odd domains | do not inflate one failure into several walls |
| earlier statistics-not-forced work | CAR remains supplied | compatibility does not derive statistics |
| prior winding/phase work | Fock multiplicity did not close winding | Wilson labels and reference repetition are not time |
| earlier macrocompiler campaigns | explicit conditional blocks retired implementation gaps | same mechanism gives partial progress without axiom edits |

No convention-only path removes the even-volume failure.  But live constructive
routes remain, so neither shared obstruction nor axiom pressure follows.

## Route disposition and next discriminator

**Route-2 disposition:** retain a conditional odd-volume even-algebra
representation, a falsified bounded-radius scalar-reference `E`, and a
falsified pair-shadow assembly.  Do not report full tournament success.  The
strongest facts are the exact sectorwise global isometry, the exact
bounded-`E` contradiction, genuine local stabilizer ranks, 24-frame gauge
repair, explicit 27-site physical layout, mass/contact/seam preservation, and
exact `L=4` failure.

The next discriminator is an every-size local parity realization—preferably an
exact 3D bosonization or auxiliary-Majorana construction—tested on the same
`L=3,4,5` runner.  It must remove both the even-volume failure and the global
parity-bus objection without replacing them with a marked site, nonlocal
string, or host controller.

`C_local` is narrowed, not closed.  There is no route-independent obstruction
and no axiom pressure.  No axiom conclusion follows.

## Verification

```text
python3 scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py
```
