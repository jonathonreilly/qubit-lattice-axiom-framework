# Cycle 727 grounding: TP reference-to-companion code switch

Date: 2026-07-28

Authority: bounded extraction only.

## Scope and decisive finding

This extraction uses only the named common-E script (**C**), overlap/Choi
script (**O**), and landed theorem note (**the note**).

The phrase **“one-reference-M2-per-cell full-sector code” is not a faithful
description of any construction defined in C**. C mentions a “shared
scalar-reference seam carrier” only as the construction being *replaced*
(C:4). Its actual physical fixtures are:

- `CellEdgeGauge`: six matter qubits per cell plus one BKSF gauge qubit per
  coarse-cell edge (C:126-357);
- `EulerMarkerGauge`: that edge-gauge code plus one marker qubit for every
  vertex, edge, face, and cube (C:360-504).

There is no per-cell register named `reference`, no `reference_m2` field, and
no one-reference-M2 fixture constructor in C. The omitted last Gauss row is a
root-charge **diagnostic**, not a reference qubit (C:273-281). The vertex
markers give at least one marker per cell, but C also allocates edge, face, and
cube markers, so they are not a one-reference-per-cell layout (C:377-445).

O is already built on `M.CompanionFixture`, not either C fixture
(O:61-65,79-99,135-233,402-407,585-589). Its C import is an algebra-helper
dependency, not use of a C encoding. The three sources exhibit a C
edge-gauge/Euler common-E surface, an O companion mixed-gauge/Choi surface, and
a note declaring a companion fixed-sector TP/CPTP package whose literal
physical input-coupling leg remains open—not a TP construction awaiting
substitution of a companion fixture for a one-reference fixture.

Any Cycle-727 spec should preserve this distinction rather than silently
calling C a one-reference-M2 code.

## 1. The code actually defined by C

### 1.1 Register layout and local operators

Let `N = len(cells)` and `E = len(edges)` for the open connected box.

`CellEdgeGauge` lays out:

- matter indices `0 .. 6N-1`, six modes per cell (C:153-166);
- edge-gauge indices `6N .. 6N+E-1`, one per positive-axis nearest-neighbor
  cell edge (C:146-166);
- total physical qubits `6N+E` (C:165-166).

Each edge record is
`(left_cell, right_cell, lower_cell_coord, axis, left_mode, right_mode)`,
with endpoint modes `6*left+2*axis+1` and `6*right+2*axis` (C:146-159).
`gauge_b(vertex)` is `Z` on all incident edge gauges (C:168-171).
`gauge_a(source,target)` is `X` on their edge gauge, multiplied by ordered
incident-edge `Z` prefixes and an orientation phase (C:173-189). These two
closures are attached to each built instance as public attributes
(C:309-310).

The stabilizer/tableau content is:

- `logical_z`: one matter `Z` per matter mode (C:273);
- one fundamental `gauge_loop` for every non-tree edge (C:191-240);
- displayed elementary-square `local_plaquettes` (C:242-271);
- Gauss rows `D_c = P_c B_g(c)` on all cells except the last/root cell
  (C:273-282);
- `w_rows = logical_z + gauge_loops + gauss`, completed canonically to
  `v_rows` (C:282-307).

The physical seam family has two endpoint number/parity terms and two
intercell Majorana bilinears. Each bilinear uses only its endpoint cell's
six-mode Jordan-Wigner prefix and is dressed by the same `gauge_a(left,right)`
(C:331-357). `expected_terms` supplies the ordinary coarse-CAR logical target
family (C:326-329).

### 1.2 Sector encoding and the alleged “reference M2”

There is no reference M2 in the constructed register. The only
reference-related statement says:

> “This probe replaces the shared scalar-reference seam carrier by one BKSF
> gauge qubit per coarse-cell edge.” (C:4-5)

For `CellEdgeGauge`, omitting the last cell's Gauss row leaves both total
matter-parity sectors and exposes that cell as the root-charge port
(C:273-281). This is a missing constraint, not a stored reference qubit.

`EulerMarkerGauge` removes the preferred root by extending the register:

- base matter: `6N`;
- base edge gauges: `E`;
- marker qubits: one for every vertex, edge, face, and cube
  (`N+E+F+C_cube`) (C:377-445);
- total: `6N+E+(N+E+F+C_cube)` (C:445,478-479).

Every higher-dimensional marker is equated to its lower-corner vertex marker;
all neighboring vertex equalities are displayed, with a tree subset retained
in the independent tableau (C:403-429). Every cell now has a Gauss row
containing its six-mode matter parity, all markers owned by that cell, and its
edge-gauge star (C:431-443). Thus no Gauss row is omitted.

The certificate states the sector relation exactly as
`product_c D_c = P_matter times product_all_markers(Z); local equality makes
product_all_markers(Z)=Z_sector because chi(box)=1` (C:920-925). This retains
both matter-parity sectors without a runtime parity query, but the uniform
marker sector and its genesis are supplied (C:920-925,1139-1144). C expressly
does not call it an autonomous full-parity encoder (C:14-19).

### 1.3 Complete public callable inventory in C

Line ranges include each callable's implementation. Inner closures are listed
only where C attaches them as public instance surfaces.

| public callable | signature | lines | role / code binding |
|---|---|---:|---|
| `check` | `check(label: str, condition: bool, detail=None) -> None` | 86-89 | report helper |
| `product` | `product(rows) -> Pauli` | 92-96 | Pauli product helper |
| `gf2_solve` | `gf2_solve(rows: list[tuple[int, int]]) -> tuple[int, int, int]` | 99-123 | free-zero GF(2) solve |
| `CellEdgeGauge.build` | `build(cls, shape: tuple[int, int, int]) -> "CellEdgeGauge"` | 142-311 | constructs the edge-gauge fixture |
| attached `CellEdgeGauge.gauge_b` | `gauge_b(vertex: int) -> Pauli` | 168-171,309 | incident edge-gauge `Z` star |
| attached `CellEdgeGauge.gauge_a` | `gauge_a(source: int, target: int) -> Pauli` | 173-189,310 | oriented edge-gauge dressing |
| `CellEdgeGauge.decoded` | `decoded(self, row: Pauli) -> tuple[Pauli, int, int]` | 313-324 | logical Pauli plus nonmatter `v/w` masks |
| `CellEdgeGauge.expected_terms` | `expected_terms(self, edge: int) -> tuple[Pauli, ...]` | 326-329 | coarse-CAR target seam terms |
| `CellEdgeGauge.physical_terms` | `physical_terms(self, edge: int) -> tuple[Pauli, ...]` | 331-357 | edge-gauge-dressed physical seam terms |
| `EulerMarkerGauge.build` | `build(cls, shape: tuple[int, int, int]) -> "EulerMarkerGauge"` | 372-459 | root-free Euler-marker extension |
| `EulerMarkerGauge.shape` | `shape(self)` property | 461-463 | forwards base shape |
| `EulerMarkerGauge.cells` | `cells(self)` property | 465-467 | forwards base cells |
| `EulerMarkerGauge.edges` | `edges(self)` property | 469-471 | forwards base edges |
| `EulerMarkerGauge.matter_qubits` | `matter_qubits(self)` property | 473-475 | forwards `6N` |
| `EulerMarkerGauge.qubits` | `qubits(self)` property | 477-479 | base plus markers |
| `EulerMarkerGauge.physical_terms` | `physical_terms(self, edge: int)` | 481-482 | forwards physical seam family |
| `EulerMarkerGauge.expected_terms` | `expected_terms(self, edge: int)` | 484-485 | forwards logical seam family |
| `EulerMarkerGauge.decoded` | `decoded(self, row: Pauli)` | 487-498 | Euler-tableau logical/leakage decode |
| `EulerMarkerGauge.gauge_a` | `gauge_a(self, source: int, target: int)` | 500-501 | forwards base edge dressing |
| `EulerMarkerGauge.gauge_b` | `gauge_b(self, vertex: int)` | 503-504 | forwards base gauge star |
| `symmetric_index` | `symmetric_index(left: int, right: int, size: int) -> int` | 507-510 | diagonal-Clifford variable indexing |
| `diagonal_common_e` | `diagonal_common_e(fixture: CellEdgeGauge) -> dict[str, object]` | 513-708 | solves and audits logical common E; also duck-typed on Euler fixture |
| `span_product` | `span_product(target: Pauli, generators: tuple[Pauli, ...], qubits: int) -> bool` | 711-739 | exact signed Pauli-span membership |
| `support` | `support(row: Pauli) -> frozenset[int]` | 742-744 | Pauli support indices |
| `constraint_and_update_certificate` | `constraint_and_update_certificate(fixture: CellEdgeGauge) -> dict[str, object]` | 747-845 | edge-gauge ranks, locality, schedule, deletions |
| `euler_marker_certificate` | `euler_marker_certificate(fixture: EulerMarkerGauge) -> dict[str, object]` | 848-926 | marker/Gauss/full-sector ranks and deletions |
| `frame_tuple` | `frame_tuple(frame) -> tuple[Coord, Coord, Coord]` | 929-930 | integer frame conversion |
| `matvec` | `matvec(frame: tuple[Coord, Coord, Coord], vector: Coord) -> Coord` | 933-937 | frame action |
| `matmul` | `matmul(left, right)` | 940-947 | frame composition |
| `schedule_covariance_certificate` | `schedule_covariance_certificate() -> dict[str, object]` | 950-1007 | 24-frame/576-product color action; transformed common E not run |
| `main` | `main() -> None` | 1010-1195 | builds three root and Euler fixtures and aggregates all C certificates |

The inner helpers `gamma` (C:338-347), `restricted_coordinate_system`
(C:567-598), `cell` (C:671-672), and `colour_map` (C:963-975) are
implementation closures, not public module/class surfaces.

## 2. Companion code visible in O and the note

### 2.1 Registers

O's `arbitrary_fixture` constructs `M.CompanionFixture` with:

- the same six matter modes per cell;
- three companion qubits per cell;
- `matter_qubits = 6N`;
- `qubits = 9N`;
- the same positive-axis edge records and endpoint-mode convention as C
  (O:79-99).

`shared_qubits` confirms that a retained local region contains six matter plus
three companion indices per cell (O:236-247). The definition and Pauli meaning
of the three companion ports live in imported module `M` and are not visible
within the permitted sources.

The note adds a separate recurrent-surface layer: “six matter M2 and three
companion M2 per cell,” plus “Three additional coframe-gauge M2 per cell,” for
12 retained M2 per cell (note:121-124). Those coframe registers are not part of
O's `9N` fixture.

### 2.2 Gauge and sector carriage

`build_factorization` obtains the represented physical/target operator
dictionary from `M.operator_rows`, relations from `M.relation_certificate`,
and the gauge subspace from `U.gauge_structure` (O:135-149). It symplectically
splits logical and gauge pairs, forms a bounded local center basis, and appends
total matter parity as the final center coordinate (O:151-181).

The physical tableau is ordered as logical pairs, gauge pairs, and center
rows. The target tableau contains the logical pairs plus total parity, with no
target gauge pair (O:159-181). This is the visible algebra behind the note's
“logical tensor identity-gauge action” and maximally mixed gauge factor.
Phase signs are solved against the signed target dictionary while local center
signs vary and total parity remains the explicit sector label (O:183-233).

`reduced_channel_domain` excludes physical gauge and center `w` coordinates
and gauge `v` coordinates from the retained local domain (O:259-280).
`target_pullback` reconstructs the logical target and either retains the patch
parity operator or scalarizes its sector sign (O:300-335). The overlap
certificates explicitly compare both even and odd sector images
(O:409-439,480-514,591-645). Scalarizing patch parity is an active deletion
failure, so local patch parity is a real bounded virtual rail
(O:703-707,719-730).

This companion channel is **fixed total parity and fixed local center**, with a
maximally mixed gauge factor; it is not C's simultaneous root-free
Euler-marker full-sector code. The note's channel formula is
`V_s [rho_logical tensor I_gauge/2^g tensor
|center=+; parity=s><...|] V_s^dagger` (note:194-199). The eight coframe
origins are carried as a locally constrained mixed direct sum
(note:95-104,121-146), not as C's Euler-marker sector.

## 3. The switch, surface by surface

### 3.1 Literal dependency audit

O imports C at O:64, but every physical fixture in O is
`M.CompanionFixture`. O uses C only at:

- `C.gf2_solve` for factorization phase equations (O:204-206);
- `C.R.F.base.gf2_rank` for local-center rank (O:230), patch domain/image
  ranks and transition rank (O:450,454,513), and held domain rank (O:606).

Replacing those calls by a directly imported GF(2) solver/rank provider would
remove the C module dependency without changing any encoded object. The local
variables named `reference` mean “first comparison entry” (`star_A` at
O:473; the `2x2x2` held fixture at O:624), not a reference-code register.

Thus both O certificates—`comparison_certificate` (O:387-579) and
`held_edge_certificate` (O:582-653)—are already companion-code certificates.
They are regression anchors for a switch, not reference-code certificates
awaiting conversion.

### 3.2 Object/certificate map

| C edge-gauge/Euler surface | companion counterpart visible in O/note | concrete switch work | gap status |
|---|---|---|---|
| `CellEdgeGauge.build`: `6N+E` matter/edge-gauge fixture | `M.CompanionFixture` via `arbitrary_fixture`: `9N`; note recurrent surface: `12N` with coframe | freeze the same cells, edges, endpoint modes, companion-port ownership, and coframe extension on every tested box | companion-port Pauli definition is imported and unavailable here |
| attached `gauge_a`, `gauge_b`; `gauge_loops`; `local_plaquettes`; Gauss rows | `M.operator_rows`, `M.relation_certificate`, `U.gauge_structure`, `F.local_center_basis` | supply an explicit row-by-row dictionary: edge dressing/star/loop/Gauss or state that no semantic one-to-one map is intended, then prove equal logical operator relations | no row-level map is present in the three sources |
| `logical_z`, `w_rows`, `v_rows` | `Factorization.physical_w/physical_v` and `target_w/target_v` | rebuild signed companion tableaux, require full rank, zero phase contradictions, and exact signed target replay | executable construction exists in O |
| `expected_terms` ordinary coarse-CAR seam target | target members of `M.operator_rows`; `target_w/target_v` | identify the exact shared logical generator dictionary and compare signed phases, not merely ranks | `M.operator_rows` contents are outside scope |
| `physical_terms` edge-gauge seam | physical members of `M.operator_rows`; note's represented seam/reverse factors | rerun seam intertwining, locality, ownership, gauge-coordinate-zero, hostile order, and deletion controls on companion ports | note reports positives; O does not expose the full-word certificate |
| `decoded` | `T.decode` plus `target_pullback` | compare logical, gauge, center, and parity coordinates on every retained generator and channel-domain basis row | available for O's factorization/overlap domain |
| root omission retaining both parities | fixed explicit total parity in `center`; even/odd certificate runs | run both fixed sectors and preserve the active local patch-parity rail; do not call this a simultaneous full-sector encoder | no equivalent full-sector companion object is shown |
| Euler marker objects/equalities/all-cell Gauss | fixed center signs, parity label, mixed gauge, and three coframe bits/cell | either define an isometry/channel from Euler sector to companion center/parity/coframe data or retire the Euler claim from the switched package | **named gap: no mapping or equivalence exists here** |
| `diagonal_common_e` on root and Euler fixtures | signed `build_factorization`, companion channel `E_s`, and `target_pullback` | rerun the complete seam plus onsite-even family through the companion channel and prove exact signed Heisenberg equivalence/identity gauge; audit locality separately | a CPTP mixed-gauge factorization is not automatically C's common logical Clifford E |
| `constraint_and_update_certificate` | note's recurrent `G_physical`, shared ownership, exact factorwise intertwiner | rerun rank/capacity, all constraints/relations, physical support, collision colors, delete-one-port/relation controls, and recurrence powers on the companion fixture | counterpart is reported by the note but not constructed in O |
| `euler_marker_certificate` | fixed-sector companion factorization and parity/coframe genesis | split the claim: fixed-sector channel tests may switch; root-free simultaneous full-parity capacity/genesis may not | **new physics required** for autonomous/full-sector equivalence |
| `schedule_covariance_certificate` | note's 24-frame, 576-product, eight-coframe-origin covariance | execute transformed companion `E`/operator/channel covariance, not only color or constraint covariance; retain returned routes | note reports companion covariance; O itself has no covariance runner |
| C `main` aggregation, including root/Euler common E and mass/contact anchor | O axis/held Choi certificates plus note's recurrent/Choi/TP package | replace the aggregate schema explicitly, rerun common logical fixtures, and retain old C results as cross-code regressions rather than mixing dictionaries | no combined cross-code runner is visible |

The generic helpers `check`, `product`, `gf2_solve`, `symmetric_index`,
`span_product`, `support`, `frame_tuple`, `matvec`, and `matmul` carry no
encoded-register semantics and require no physics switch. O's `product`,
`parity_complement`, `local_equation`, `embed_local_vector`,
`global_majorana`, and `pauli_cells` are likewise algebra/coordinate helpers.

## 4. Verbatim note language about references, TP, and open interfaces

The note contains **no phrase `reference code`, no standalone acronym `TP`,
and no statement that a `reference-to-companion switch` is open**. Its
reference-bearing passages are:

> “A separate local broadcast-control-unbroadcast circuit realizes `D(rho) = (rho + P_total rho P_total) / 2` using one Bell reference and a contour that controls each matter mode exactly once. The one-cell Pauli basis is exhaustive and the tensor extension is explicit. There is no runtime global parity query or parity service.” (note:148-156)

> “The finite open box, boundary root, shape-specific spanning tree/router, clean target M2, Bell references, one-time epoch/token, and permission to trace typed semantic environments remain supplied.” (note:158-163)

Also: “Auxiliary density approaches approximately 29 M2 per cell when Bell references, one retained syndrome per independent row, and a route rail are included.” (note:186-188), and “local center-sector signs and a maximally mixed gauge factor or reference purification;” (note:275-278).

The note's most direct teleportation boundary is:

> “Standard coherent qubit teleportation is not automatically a bounded local realization of this map: raw intercell Pauli-X corrections can reintroduce an order-dependent Jordan-Wigner cleanup string. A bounded local live-input correction word must therefore be demonstrated rather than inferred from the Choi theorem.” (note:201-205)

> “The growing support comes from the raw-X Jordan--Wigner cleanup. This is a route-specific failure of raw-mode Bell corrections, not a failure of even-CAR Bell bases, local gauge teleportation, the recurrent update, or the substrate.” (note:220-222)

The fixed-sector/live-input ceiling is:

> “This is a positive fixed-sector CPTP encoding map at the CAR-domain/physical-output boundary; it is not yet a literal physical-M2 input-coupling circuit, a sector law, or autonomous genesis.” (note:240-243)

The exact dependency rows relevant to the alleged switch say:

> “`C_ref` | no runtime exterior-order query or global parity service; the coframe and parity channels have explicit local circuits | root/boundary, parity label, center signs, gauge reference, epoch, mode labels, parameters, and finite router remain supplied” (note:317)

> “`C_num` | exact full fixed-parity mixed-gauge channel algebra, all-factor identity-gauge action, and a CAR-local fixed-sector live-input CPTP map | physical selection/enforcement of the parity and center sector, plus literal M2 compilation of the input Bell operations” (note:318)

> “`C_local` | shared-register overlap, constant-density recurrence, local Choi pumping, one-cell live-input corrections, bounded conflict colors, returned routing, and active covariance close on finite open boxes | physical input-Bell compilation, collision-free controller composition, autonomous genesis/enforcement, boundary-free recurrence, and periodic/fault-tolerant family remain open” (note:321)

The package-inventory and proposed next experiment are:

> “Within this PR's submitted note, runners, reports, and receipt, no literal physical-M2 input-Bell compiler is constructed. That is an explicit package inventory statement, not a registry-wide negative or a new-axiom inference.” (note:402-406)

> “1. compile the positive CAR-local Bell rows into M2 input hardware on the same
> site map as the prepared resource and recurrent update;
> 2. compile a direct local encoded-input Clifford on the companion/center code;
> 3. stagger preparation, Bell coupling, retained correction banks, and
> recurrent `G` with an explicit collision-free fixed schedule.”
> (note:447-451)

Therefore the only grounded “open switch” reading is operational: complete the
literal input Bell/encoded-input leg and joint epoch **on the already declared
companion/center code**. The note does not ground a pending replacement of a
one-reference-per-cell code.

## 5. Cycle-727 synthesis: smallest honest switch package

### 5.1 Minimum executable package

1. **Name both encodings precisely.** If “reference code” means C, call it
   `CellEdgeGauge` or `EulerMarkerGauge`, not one-reference-M2-per-cell. If
   another fixture is intended, newly supply its absent source/register definition.
2. **Freeze a common logical dictionary:** identical cell/mode labels, oriented
   edges, endpoint convention, signed free/seam/reverse/contact/coin generators,
   and total-parity convention.
3. **Construct companion factors on every regression box.** Rebuild the fixture,
   physical/target tableaux, logical/gauge/center split, parity complement, and
   signed phase solution; require full ranks, zero phase contradictions, exact
   targets, zero gauge coordinates, and identity action on mixed gauge.
4. **Rerun update certificates** on C's `2x2x2`, `3x2x2`, `3x3x2` and held
   `5x3x2`: all factors, ownership, locality/routes/return, order, deletion,
   mass/contact, and recurrence powers.
5. **Rerun O's companion Choi anchors:** all three axes, two seven-cell stars,
   twelve-cell union, rank-23 domain on 18 overlap qubits, exact signed maps in
   both parities, zero phase contradictions, active parity-rail deletion, and
   four held completions.
6. **Rerun TP/live input on the same companion site map:** fixed parity/center,
   mixed gauge, even-CAR Bell characters, one-cell private duals, syndromes,
   returned work, deletion, and 24/576/eight-origin covariance. Add literal M2
   input-Bell compilation and the joint collision-free schedule or retain the
   CAR-domain/physical-output ceiling.
7. **Give cross-code equivalence:** compare exact signed Heisenberg pullbacks for
   every common generator in each parity. Separate rank, phase, gauge identity,
   center/parity supply, and locality; dimensions or a Choi resource do not suffice.

### 5.2 Newly supplied data that must stay explicit

From the note, the companion package continues to require:

- six-mode labels and companion-port convention;
- fixed total-parity label and local center signs;
- maximally mixed gauge state or its reference purification;
- three coframe bits per cell and the uniform eight-origin channel;
- finite open box, boundary root, axis order, spanning tree/router, and
  one-time epoch;
- clean Bell, syndrome, route, and non-root preparation registers;
- Cycle-219/230 parameters and fixed factor order.

For Cycle 727, also freeze the imported-but-not-visible companion operator and
relation dictionaries, the literal input M2 site map, Bell-measurement
primitive decomposition, controller ownership, and collision schedule.

### 5.3 Equivalence and regression anchors

- Same `cells`, oriented `edges`, six-mode indexing, and coarse-CAR target
  generators.
- Exact signed logical coordinates, zero gauge leakage, fixed center/parity
  behavior, and identity gauge action.
- Separate even and odd fixed-sector runs; the local patch-parity rail may not
  be scalarized.
- Free/seam/reverse/contact/coin/FSWAP and one-particle mass residual anchors.
- C's deletion/locality/covariance controls, translated to explicit companion
  relations rather than assumed row names.
- O's rank-23/two-star/three-axis/four-held-box signed Choi equality.
- Note's 24 frames, 576 products, eight coframe origins, returned routes, and
  hostile-order/deletion controls.

### 5.4 Cannot be switched without new physics or a new construction

- **Full-sector mismatch:** C's Euler code retains both matter-parity sectors
  in one root-free register, whereas the companion channel visible here fixes
  `parity=s` and center signs. Running `s=+/-` separately is not an isometry
  between the two full-sector codes. A sector-summed/direct-sum companion
  channel or an autonomous local sector law is new work.
- **Marker-to-center/coframe map:** no isometry maps Euler vertex/edge/face/cube
  marker equalities and Gauss rows to companion ports, gauge pairs, center
  signs, and coframe bits. This cannot be declared by nomenclature.
- **Autonomous genesis/enforcement:** parity, center, mixed gauge, coframe,
  root, clean ancillas, and epoch remain supplied/open.
- **Bounded physical E:** C's solved common E has growing-distance logical CZ
  structure, while O's canonical factorization is algebraic and not itself a
  bounded preparation circuit. Cross-code exactness does not close local
  preparation.
- **Literal TP input leg:** the even-CAR Bell rows are CAR-local, but their
  physical-M2 input-coupling circuit and joint collision-free epoch are absent.
- **Global channel tensor:** O closes pairwise two-star overlap, not a tiled
  global PEPO/Stinespring tensor, triple overlaps, or closed-loop consistency.
- Periodic topology, autonomous repair, fault tolerance, renewal, and
  boundary-free recurrence remain outside the switch package.

## COMPLETENESS

- [x] All public C callables have signatures and exact line ranges, including attached `gauge_a/gauge_b`.
- [x] C's actual registers, gauge operators, sectors, and lack of a one-reference-M2 object are explicit.
- [x] O's companion registers, logical/gauge/center/parity split, two-sector handling, and coframe distinction are explicit.
- [x] Every encoding-bound C construction/certificate has a companion mapping or named gap; helpers are switch-free.
- [x] Every literal C use by O is listed; both O certificates are identified as companion-native.
- [x] Relevant note language is quoted verbatim; absent “reference code,” standalone “TP,” and switch language are recorded.
- [x] The minimum package, supplied data, regression anchors, and new-physics gaps are separated.
- [x] Imported `M`, `U`, `F`, `T`, and `R` definitions were not inspected or silently reconstructed.
