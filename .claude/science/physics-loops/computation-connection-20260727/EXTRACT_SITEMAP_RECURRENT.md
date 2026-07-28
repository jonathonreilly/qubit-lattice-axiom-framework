# Cycle-720 site map: recurrent update and tree/plaquette Choi pump

This is a bounded interface extraction from only:

- `scripts/frontier_cycle720_companion_recurrent_overlap_update_2026_07_27.py` (abbreviated **R**, 838 lines), and
- `scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py` (abbreviated **P**, 1021 lines).

Line references below are source-file line numbers. “Imported/opaque” means the
caller and returned fields are visible here but the implementation is outside
the permitted read set. Neither file defines a class; `Pauli = M.Pauli` and
`Coord = tuple[int, int, int]` are aliases (R107-109, P91-92).

### Defined-symbol index

- **R globals:** `AUDIT_TIMEOUT_SEC`, `NOTE_PATH`, `AUDIT_INPUT_PATHS`, `DECLARED_INPUT_PATHS`, `Pauli`, `Coord`, `TOL` (R21-109). **R functions:** `fields(row) -> tuple[int,int,int]` (R112); `semantic_factor_keys(fixture: M.CompanionFixture) -> set[tuple]` (R116); `overlap_cover_certificate() -> dict[str,object]` (R134); `pauli_expansion_word(rows: tuple[Pauli,...], order: tuple[int,...]) -> dict[tuple[int,int,int],complex]` (R169); `expansion_residual(left,right) -> float` (R194); `schedule_certificate(shape: tuple[int,int,int]) -> dict[str,object]` (R202); `coordinate_intertwiner_certificate(fixture: M.CompanionFixture, factor: O.Factorization) -> dict[str,object]` (R264); `update_covariance_certificate(shape: tuple[int,int,int]) -> dict[str,object]` (R357); `recurrent_box_certificate(shape: tuple[int,int,int], powers=(1,2,3,5,8)) -> dict[str,object]` (R472); `main() -> None` (R603); local `main.<locals>.check(label: str, condition: bool) -> None` (R629). No R class is defined.
- **P globals:** `AUDIT_TIMEOUT_SEC`, `NOTE_PATH`, `AUDIT_INPUT_PATHS`, `DECLARED_INPUT_PATHS`, `Pauli`, `Coord` (P29-92). **P functions:** `pauli_product(rows) -> Pauli` (P95); `direct_graph_basis(fixture: M.CompanionFixture) -> tuple[tuple[Pauli,...],tuple[tuple,...]]` (P102); `repeated_star_basis(fixture: M.CompanionFixture) -> tuple[Pauli,...]` (P130); `incident_port_mask(fixture: M.CompanionFixture, cell: int) -> int` (P150); `solve_private_correction(rows: tuple[Pauli,...], target: int, allowed: tuple[int,...]) -> tuple[Pauli,int,int]` (P160); `local_signature(row: Pauli, allowed: tuple[int,...]) -> tuple[int,int]` (P185); `signature_pauli(signature: tuple[int,int], allowed: tuple[int,...]) -> Pauli` (P191); `onsite_allowed(fixture: M.CompanionFixture, cell: int) -> tuple[int,...]` (P200); `edge_allowed(fixture: M.CompanionFixture, edge: int) -> tuple[int,...]` (P214); `build_private_atlases() -> dict[str,object]` (P224); `correction_from_atlas(fixture: M.CompanionFixture, tag: tuple, atlas: dict[str,object]) -> Pauli` (P298); `coordinate_maps(fixture: M.CompanionFixture, root: Coord, axis_order: tuple[int,int,int]) -> tuple[dict[Coord,tuple[int,int,int]],dict[tuple[int,int,int],Coord]]` (P318); `edge_lookup(fixture: M.CompanionFixture) -> dict[frozenset[Coord],int]` (P337); `schedule_tree_plaquettes(fixture: M.CompanionFixture, root: Coord, axis_order: tuple[int,int,int]) -> tuple[tuple[int,...],tuple[tuple[int,tuple[int,...]],...]]` (P344); `pauli_cells(fixture: M.CompanionFixture, row: Pauli) -> frozenset[Coord]` (P432); `returned_route(anchor: Coord, support: frozenset[Coord]) -> tuple[tuple[Coord,Coord],...]` (P451); `route_execution_failures(anchor: Coord, route: tuple[tuple[Coord,Coord],...]) -> tuple[int,int]` (P477); `schedule_basis(fixture: M.CompanionFixture, root: Coord, axis_order: tuple[int,int,int]) -> tuple[tuple[Pauli,...],tuple[tuple,...],dict[str,object]]` (P499); `schedule_correction(fixture: M.CompanionFixture, tag: tuple, atlas: dict[str,object]) -> Pauli` (P533); `box_certificate(shape: tuple[int,int,int], atlas: dict[str,object]) -> dict[str,object]` (P544); `pump_algebra_certificate() -> dict[str,object]` (P816); `main() -> None` (P848); local `main.<locals>.check(label: str, condition: bool) -> None` (P855). No P class is defined.

## 1. Box/union geometry

### Exact public blocks

- `R.semantic_factor_keys(fixture: M.CompanionFixture) -> set[tuple]` (R116-131): returns unique semantic keys.
- `R.overlap_cover_certificate() -> dict[str, object]` (R134-166): returns the two-view/global-union counts, factor-set differences, and ownership prose.
- `P.coordinate_maps(fixture: M.CompanionFixture, root: Coord, axis_order: tuple[int, int, int]) -> tuple[dict[Coord, tuple[int, int, int]], dict[tuple[int, int, int], Coord]]` (P318-334): oriented cell-coordinate bijection and its inverse.
- `P.edge_lookup(fixture: M.CompanionFixture) -> dict[frozenset[Coord], int]` (P337-341): unordered endpoint-coordinate pair to fixture edge index.

### Construction and enumeration

- Left cube cells are `set(Q.shape_cells((2,2,2), (0,0,0)))`; right cube cells are `set(Q.shape_cells((2,2,2), (1,0,0)))`; the physical box is their set union (R134-140). Each set is passed separately to `O.arbitrary_fixture`, while the operative global fixture is built once from `union_cells`.
- The resulting open rectangular union is `3x2x2`: 8 left cells, 8 right cells, 12 union cells, and the `x=1` overlap plane has 4 shared cells (construction R135-147; asserted R633-638).
- There is no local implementation of `Q.shape_cells` or `O.arbitrary_fixture` in the read set. Consequently, the exact tuple order of `fixture.cells` and exact tuple structure/order of `fixture.edges` are imported/opaque. Visible consumers consistently enumerate cells by `range(len(fixture.cells))` or fixture order and edges by `enumerate(fixture.edges)` (e.g. P108-126, P337-341).
- The shared registry is the single `union` fixture. The certificate reports `9 * len(shared_cells) = 36` shared physical matter+companion M2 registers and exactly `copied_shared_registers = 0` (R147-154). Cube membership is a view, not an allocation or owner (R162-165). Coframe registers are counted separately by the recurrent box certificate and are not included in this “36 shared physical M2” field.
- Recurrent held boxes are created identically as `O.arbitrary_fixture(Q.shape_cells(shape))` for `shape in ((3,2,2),(3,3,2),(5,3,2))` (R202-205, R472-476, R603-612).
- Pump boxes use the same construction for `((2,2,2),(3,2,2),(3,3,2),(5,3,2),(4,4,3))` (P544-550, P848-852). No fit is performed per held box; the correction atlas is built once before all `box_certificate` calls.

## 2. Register ownership and indexing

- Per cell, the recurrent certificate exposes 12 retained M2 sites: 6 matter + 3 physical companion + 3 retained coframe-gauge sites (R531-537). `fixture.qubits = 9N` is matter+companion; coframe is the separate `3N`; total retained is `12N`. For `3x2x2`, these are 108, 36, and 144 respectively.
- The pump’s visible bit layout confirms the matter/companion ordering: physical matter indices are `6*cell + mode` (six per cell), and companion indices are `fixture.matter_qubits + 3*cell + local` (three per cell) (P108-125, P200-221). Thus `fixture.matter_qubits = 6N` and `fixture.qubits = 9N`.
- For a Choi row the extra coarse-input/JW half follows the physical output: `total_qubits = fixture.qubits + fixture.matter_qubits = 15N`; `pauli_cells` maps `[0,6N)` as physical matter, `[6N,9N)` as companion, and `[9N,15N)` as coarse input (P432-448, P547-548). The coframe `3N` is not in this tableau index space in either visible runner.
- Semantic ownership is exact: onsite coin/reverse/contact factors are owned by their cell; each seam factor is keyed by the edge’s `owner` and `axis`, where the prose fixes the owner as the positive-axis lower endpoint (R120-131, R162-165). A covering cube never owns a factor.
- Global semantic keys are: `("coin", cell, factor)`, `("reverse", cell, axis)`, `("contact", cell, left, right)`, and `("seam", owner, axis, factor)` (R116-131).
- Global register numbers are therefore cell-major in the visible Pauli layout. The coordinate-to-cell-index assignment inside `O.arbitrary_fixture`, the `owner` value’s exact type, all coframe bit indices, and the remaining fields in each `fixture.edges` tuple are imported/opaque and must not be guessed.

## 3. Routing and count levels

### Recurrent word

- `U.placement(fixture)` then `U.physical_word(fixture, placed)` returns `(word, update)`; `U.c707.route_word(word)` returns `(routed, route)` (R475-481). All three implementations and the instruction class are imported/opaque.
- Count levels are deliberately distinct: `update["logical_update_factors"]` is the semantic-factor count; `len(word)` is the literal unrouted physical-instruction count (also reported, somewhat confusingly, as `inverse_word_factor_count`); `len(routed)` is `routed_gate_count`, and power rows call it `routed_primitive_count` after multiplication by the power (R507-528, R564-581).
- The route report fields consumed here are exactly `maximum_route_distance`, `route_return_failures`, and `non_NN_failures` (R577-580); pass requires the latter two to be zero (R740-750). How route distance is computed and how the physical NN word performs and returns work are not visible because `route_word` is imported.

### Pump word

- `P.returned_route(anchor: Coord, support: frozenset[Coord]) -> tuple[tuple[Coord, Coord], ...]` (P451-474). It asks imported `R.route_selector(anchor, support)` for tree links, builds undirected adjacency, and performs a depth-first walk with `sorted(adjacency[cell])`. Every discovery appends `(parent,child)`; every recursion return appends `(child,parent)`. It asserts all support cells were visited and returns the literal down/up word, hence returned work.
- `P.route_execution_failures(anchor: Coord, route: tuple[tuple[Coord,Coord], ...]) -> tuple[int,int]` (P477-496) returns `(forward_failures, inverse_failures)`. Forward execution requires the token to equal each link’s left endpoint and to finish at `anchor`. Literal inverse execution scans `reversed(route)`, toggles across an edge only when the token is at an endpoint, and also must finish at `anchor`.
- Pump locality is the Manhattan-one predicate `sum(abs(a-b) for zip(left,right)) == 1` on every transition; it separately checks that a nonempty route’s final right endpoint is its anchor (P631-646). Counts are total transitions, transitions/cell, maximum transitions for one measurement, locality-or-return failures, and literal reverse failures (P757-763). Plaquette support diameter is delegated to imported `R.support_diameter` (P652-658).
- Pump “semantic rows” are schedule stabilizers; physical controlled-Pauli factors are popcounts of each measured row and its private correction (P629-651, P764-765). The prose gate word is `H_s; controlled-S_j along returned NN route; H_s; controlled-C_j along returned NN route; store s_j in retained local bank` (P793-800).
- No collision counter or collision-free epoch layout exists in either file. Pump output explicitly leaves a “literal collision-free controller layout with the recurrent matter word” open (P1000-1004).

## 4. Recurrent free/reverse/seam/contact word

- `R.semantic_factor_keys` builds, per cell: one key per factor of the Cycle-219 common-coin adjacent-QR schedule; 3 reverse keys (axes 0..2); and 15 unordered contact pairs `(left,right)` with `0 <= left < right < 6`. Per edge it builds four seam keys using the global `(owner,axis)` (R116-131).
- The `3x2x2` box has `N=12`, `E=20`. The task-specified total 428 therefore decomposes as 132 coin factors (`11/cell`), 36 reverse factors, 180 contact factors, and 80 seam factors: `12*(11+3+15)+20*4 = 428`. The 11 coin count is inferred from that supplied total and the visible other loops; `compile_adjacent_qr` itself is opaque.
- Each `2x2x2` view has 280 factors. Their intersection has 132 duplicated view keys (116 onsite keys on four cells plus 16 seam keys on the four in-plane shared edges), and their set union is the 428 globally owned keys. The certificate checks missing/excess are zero and deduplicated cover count equals global count (R141-165, R633-644).
- The four immutable macro layers are, in order: (1) parallel onsite coin net, (2) parallel three-pair reverse net, (3) all seam blocks, and (4) parallel onsite all-pair contact net (R251-260). This is a fixed law schedule, explicitly not time.
- Seam block literal order is factors `(0,1,2,3)`, described as groups 01 then 23. Distinct edge blocks commute but rows within an edge contain noncommuting pairs (R204-226, R251-255).
- `R.pauli_expansion_word(rows: tuple[Pauli,...], order: tuple[int,...]) -> dict[tuple[int,int,int],complex]` (R169-191) expands the ordered product of `exp(-i*pi*P/4)=(I-iP)/sqrt(2)`, drops coefficients `<=1e-13`, and uses phase-free `(0,x,z)` keys while folding Pauli phase into coefficients. `R.expansion_residual(left,right) -> float` (R194-199) is the Euclidean coefficient-map difference over the union of keys.
- `R.schedule_certificate(shape: tuple[int,int,int]) -> dict[str,object]` (R202-261) compares frozen `(0,1,2,3)` against: orientation reversal `(1,0,3,2)` (must have residual `< TOL`); hostile interleave `(0,2,1,3)` (must be `>1e-3`); and deletion `(1,2,3)` (must be `>1e-3`) (R228-250, R697-705). Thus orientation reversal is an allowed block convention; interleaving the anticommuting factor groups or deleting factor 0 is not.
- `R.recurrent_box_certificate(shape: tuple[int,int,int], powers=(1,2,3,5,8)) -> dict[str,object]` (R472-600). It builds the fixture, factorization, parent tensor certificate, factorwise coordinate certificate, placement, physical word, and routed word exactly once. `one_step_exact` is the conjunction of parent-projector equality and six zero coordinate/commutator counters (R496-506).
- For each listed power, it loops over that Boolean certificate rather than rebuilding an encoder or word: `encoder_calls=1`, `physical_update_word_calls=power`, `fresh_encoder_environment_calls_after_genesis=0`, and factor/routed counts are the one-step counts multiplied by power (R507-528). This is executable factorwise induction on the exact generator-coordinate intertwiner and gauge identity, not fresh encoding or dense many-body exponentiation (R590-599).

## 5. Logical/gauge/parity/center/coframe coordinate checks

- `R.coordinate_intertwiner_certificate(fixture: M.CompanionFixture, factor: O.Factorization) -> dict[str,object]` (R264-354) obtains `(family, physical, target)` rows from imported `M.operator_rows(fixture)`. Each physical row is decoded in `(factor.physical_w, factor.physical_v)` at `fixture.qubits`; its target is decoded in `(factor.target_w, factor.target_v)` at `fixture.matter_qubits` (R285-294).
- Logical coordinates occupy bit positions `[0,factor.logical)` in both decoded `v_mask` and `w_mask`. A logical failure means either physical mask differs from the target mask on those positions (R268, R295-298).
- Gauge coordinates occupy `[factor.logical, factor.logical+factor.gauge)`. A gauge-coordinate failure is counted separately for nonzero physical `v_mask` and nonzero physical `w_mask` in this range; the target gauge mask is not compared (R269, R299-300). Thus “zero gauge coordinate failures” concretely means every physical operator generator has identity action on both canonical gauge halves.
- The physical parity coordinate is the `w_mask` bit at `factor.logical + factor.gauge + factor.center - 1`; target parity is target `w_mask` bit `factor.logical` (R301-306). They must agree.
- Phase is tested in both parity sectors `odd in (0,1)` as `(pc.phase + 2*odd*physical_parity) mod 4 == (tc.phase + 2*odd*target_parity) mod 4` (R307-311). Therefore sign/phase, not merely binary Pauli support, is load-bearing.
- Gauge commutators are tested against both physical canonical halves, `physical_w[logical:logical+gauge] + physical_v[logical:logical+gauge]`; center commutators are tested against physical `w` rows in the following `factor.center` slots (R276-283, R312-327). Zero means every generator symplectically commutes with every such row.
- The returned shape is seven public fields: `operator_generators`, `logical_coordinate_failures`, `gauge_coordinate_failures`, `parity_coordinate_failures`, `both_sector_phase_failures`, `physical_generator_gauge_commutator_failures`, `physical_generator_center_commutator_failures`, plus `coordinate_signature_sha256` over ordered family/coordinate/phase tuples (R328-354).
- Coframe checks are separate, not part of that decoder: imported `Q.coframe_constraint_certificate(shapes)` must report `rank_failures`, `contradictions`, `seed_formula_failures`, and `flipped_rhs_detection_failures` all zero (R603-615, R740-745). Its equations and coordinate index convention are not visible.

## 6. Tree/plaquette Choi pump

### Basis and private corrections

- `P.pauli_product(rows) -> Pauli` (P95-99): left-folds `Pauli()` with `@`.
- `P.direct_graph_basis(fixture: M.CompanionFixture) -> tuple[tuple[Pauli,...], tuple[tuple,...]]` (P102-127): returns `(rows,tags)`. Per cell it emits six signed Choi rows of physical/target single-mode `Z`, tagged `("onsite_Z",cell,mode)`, then five adjacent physical/target `XX` rows on modes `(0,1)..(4,5)`, tagged `("onsite_XX",cell,mode)`. It then emits one row per edge: exactly seam factor index 2 on both `fixture.physical_terms(edge)` and `fixture.target_terms(edge)`, tagged `("edge",edge)`.
- Hence the direct stabilizer basis has exactly `11N+E` rows and that many independent generators; `box_certificate` checks direct rank, count, commutation, and signed two-way span equality with the repeated-star basis (P724-747, P867-875).
- `P.repeated_star_basis(fixture) -> tuple[Pauli,...]` (P130-147) constructs each center plus in-box nearest neighbours, factorizes each patch, collects imported channel-graph entries, and returns imported independent tagged rows. It is a comparison oracle, not the pump schedule.
- `P.incident_port_mask(fixture,cell) -> int` (P150-157) uses six bits: a cell that is an edge’s `left` sets `2*axis+1`, while a `right` endpoint sets `2*axis`. This signed-port convention is part of every atlas key.
- `P.solve_private_correction(rows: tuple[Pauli,...], target: int, allowed: tuple[int,...]) -> tuple[Pauli,int,int]` (P160-182) builds GF(2) equations whose two variables per allowed qubit are correction X and Z. X sees stabilizer Z; Z sees stabilizer X. RHS is one only on `target`. It returns `(Hermitian Pauli correction, solve_rank, contradictions)`; the correction phase is `(x & z).bit_count() & 1`.
- `P.onsite_allowed(fixture,cell) -> tuple[int,...]` (P200-211) is the nine physical output qubits of that cell (six matter then three companion). `P.edge_allowed(fixture,edge) -> tuple[int,...]` (P214-221) is only the three companion qubits at each endpoint, left endpoint first.
- `P.local_signature(row,allowed) -> tuple[int,int]` (P185-188) compresses global X/Z masks into allowed-order local masks. `P.signature_pauli(signature,allowed) -> Pauli` (P191-197) expands them back, again fixing Hermitian phase.
- `P.build_private_atlases() -> dict[str,object]` (P224-295) trains on every rectangular shape in `{1,2,3,4}^3` (64 shapes). Onsite key is `(incident_port_mask, tag_family, mode)`; edge key is `(left_port_mask,right_port_mask,axis)`. Each key must have exactly one local signature. Return keys are `onsite`, `edge`, `training_shapes`, `training_rows`, `solve_contradictions`, `onsite_keys`, `edge_keys`, `onsite_conflicts`, `edge_conflicts`, two distinct-correction counts, and `atlas_sha256`. Main requires 704 onsite keys (`64*11`), no contradictions, and no conflicts (P859-865).
- `P.correction_from_atlas(fixture,tag,atlas) -> Pauli` (P298-315) reconstructs by exactly those keys/allowed orders. `P.schedule_correction(...) -> Pauli` (P533-541) passes onsite tags directly; both `("tree",edge)` and `("plaquette",new_edge,cycle)` reuse the original direct edge correction.

### Rooted tree and plaquette order

- `P.schedule_tree_plaquettes(fixture,root,axis_order) -> tuple[tuple[int,...], tuple[tuple[int,tuple[int,...]],...]]` (P344-429) returns `(tree_edges, fill)`, where each fill item is `(new_edge, four_edge_cycle)`.
- `coordinate_maps` chooses sign + when root is at that physical axis’s minimum and - otherwise, then orders oriented distances by `axis_order` (P323-334). The canonical box schedule uses `root=min(fixture.cells)` and `axis_order=(2,1,0)` (P551-554): oriented `u[0]` is physical z (“fast”), `u[1]` y (“middle”), and `u[2]` x (“slow”).
- Tree parent priority is first nonzero coordinate in `u[0],u[1],u[2]`, decrementing exactly that coordinate (P369-384). It gives `N-1` rooted-tree seam edges and prepares them first.
- An elementary plaquette at `base` and coordinate axes `(a,b)` is ordered: `(base->base+a, base->base+b, base+a->base+a+b, base+b->base+a+b)` (P357-367). `add_new` asserts the nominated new edge is unprepared and every other cycle edge is already prepared (P385-395).
- Fill order is exact: middle-axis edges off fast=0, nested `slow,middle,fast=1..`; then slow-axis edges on middle=0 off fast=0, nested `slow,fast=1..`; then remaining slow-axis edges growing in middle, nested `slow,middle=1..,fast` (P396-426). Final prepared edge set must equal every fixture edge.
- `P.schedule_basis(fixture,root,axis_order) -> tuple[tuple[Pauli,...],tuple[tuple,...],dict[str,object]]` (P499-530) returns `(rows,tags,report)`: all 11N onsite direct rows first, then original direct seam row 2 for every tree edge, then the Pauli product of the four direct seam rows for every fill cycle. Tags are original onsite tags, `("tree",edge)`, then `("plaquette",new_edge,cycle)`. Report has `tree_edges`, `plaquette_fill_rows`, `edge_coverage_failures`, and `triangular_predecessor_failures`.
- The plaquette products cancel long seam strings to support on at most four cells with diameter at most two (checked P652-658, P900-906). The triangular correction test requires each schedule correction to anticommute with its own row and commute with every earlier row (P610-620).

### Channel and retained syndrome

- `P.pump_algebra_certificate() -> dict[str,object]` (P816-845) uses the canonical pair `S=Z`, `C=X`. Its exact Kraus convention is `K_plus=P_plus`, `K_minus=C P_minus`; completeness is `P_plus+P_minus=I`, and anticommuting `C` maps both input eigensigns to the plus sector.
- The reduced channel is `Phi_j(rho)=P_j+ rho P_j+ + C_j P_j- rho P_j- C_j`; commuting triangular private corrections produce `rho_J=2^(-Q) product_j(I+S_j)` (P802-805).
- The dilation is Hadamard, controlled signed Pauli, Hadamard, controlled correction (P838-840). There is no reset or postselection: each syndrome bit is stored in a retained local bank, all syndrome and Bell purifiers are retained, and the mobile rail is returned to its anchor (P793-811, P841-844).
- `box_certificate` reports retained resources as `total_qubits` local Bell reference M2, `len(schedule)` retained syndrome-bank M2, and `N` reusable mobile-route-rail M2; the initial system is one local Bell pair per Choi-system M2 with the other half purifying the maximally mixed system (P785-796).
- Active deletion controls remove schedule rows 0, `onsite_count-1`, and the last row; each survivor set must have rank `len(schedule)-1`. They also delete the least significant active Pauli factor from those three rows and require literal row inequality (P701-720, P772-777, P936-942).
- Larger-box reuse is literal: one atlas is built, frozen, and supplied to all five box calls (P848-852). Every box must have zero atlas syndrome, triangular pump, and off-declared-cell failures; correction weights are bounded by 8 overall and 3 for edges (P889-898). Every 8 corners times 6 axis permutations (48 contexts) must reproduce the same signed projector with zero schedule failures (P660-688, P919-924).

## 7. Signed covariance and frame-sensitive conventions

- `R.fields(row) -> tuple[int,int,int]` returns `(row.phase % 4,row.x,row.z)` (R112-113); signed covariance therefore includes the Pauli phase, while binary covariance drops only that first component.
- `R.update_covariance_certificate(shape: tuple[int,int,int]) -> dict[str,object]` (R357-469) instantiates 24 imported proper cubic frames, 8 affine translation parities, and 8 coframe-origin seeds. For every `(frame,shift)` it rebuilds a target fixture from `Q.affine_cells(source.cells,frame,shift)`, and for every seed applies imported seeded sheet corrections (R369-413). The actual context count is `24*8*8=1536` per shape, not `24*576*8`.
- Transformed operator rows are compared as signed and binary multisets within each family `("seam","onsite_B","onsite_even")`; public failure counters are `operator_family_binary_multiset_failures` and `operator_family_signed_multiset_failures` (R375-443, R458-468).
- Each source edge’s four base-corrected seam rows are looked up in the target and classified only by mapped factor-index tuple. Accepted classes are forward `(0,1,2,3)` and orientation-reversed `(1,0,3,2)`; every other or missing classification increments `seam_block_factor_order_covariance_failures` (R382-402).
- Coin covariance constructs the 6x6 permutation matrix for each frame and reports `max ||P coin P^T - coin||`, required `< TOL` (R448-467, R708-717).
- The separate retained coframe channel is imported as `Q.uniform_origin_direct_sum_certificate(...)` (R615-623). Main checks all 576 proper-rotation products over 8 origin sectors, i.e. 4608 origin blocks, plus 512 translation-product origin blocks (R720-737). Its visible counters are `proper_rotation_density_Choi_product_failures`, `translation_density_Choi_product_failures`, `uniform_origin_density_Choi_product_failures`, and `local_alternation_constraint_transport_failures`, all zero. The requested “24 frames x 576 products x 8 sectors” is thus two adjacent certifications: the 24-frame update test and the 576-product-by-8-origin channel test.
- No counters named tableau-image, stabilizer, private-correction, atlas-key, schedule-key, or returned-route covariance failures occur in these files. The nearest visible pump counters are signed two-way basis replay, atlas private-dual syndrome, triangular schedule pump, corner/axis signed projector, and returned-route locality/inverse counters (P733-768).
- The only visible JW/chart rule is a prohibition: onsite private corrections remain on the physical output cell and off the coarse-input JW half because odd input Paulis acquire chart strings under cubic frame changes, while the companion action is cell-local (P200-204). No chart-route recompiler or explicit JW chart-route recompilation rule is defined/called here.

## 8. Residuals and inherited fixtures

- In `R.recurrent_box_certificate`, every instruction in the *unrouted* `word` supplies `.matrix`. It reports the maximum of `||U†U-I||` and the maximum of `||UU†-I||` (R482-495, R564-576). The latter is named `maximum_instruction_inverse_pair_residual`; no separately constructed inverse is multiplied here. The stated inverse convention is to reverse the literal instruction word and conjugate-transpose every local matrix (R569-575). Both maxima must be below `TOL = 4e-10`.
- The one-particle fixture is imported exactly as `U.C.R.local_free_contact_mass()["mass_contact"]` (R529). Its consumed fields are `one_particle_mass_residual`, `contact_vacuum_and_one_particle_residual`, and `contact_double_occupation_phase_residual`; all must be `< TOL` (R583-589, R751-754).
- Cycle-219 coin data are invoked through `F128.common_coin()`. The coin is compiled by imported `S25.compile_adjacent_qr(coin)` to define semantic coin factor count (R116-123), and is separately tested under all 24 direction permutations by `||P coin P^T-coin||` (R448-457).
- Cycle-230 is invoked exactly as `U.C712.cycle230_semantic_certificate(U.C712.decoded_word(2)[0])` (R624-626). Main checks five fields `< TOL`: `coin_matrix_residual`, `mass_residual`, `FSWAP_matrix_residual`, `onsite_64_state_contact_residual`, and `internal_depth_two_stream_residual` (R756-760).
- Seam-specific active checks in this runner are the ordered exponential orientation/interleave/deletion residuals in section 4. Reverse and seam are not exposed as separately named Cycle-230 residual fields here; any inclusion in `decoded_word(2)` or the semantic certificate is imported and opaque. No other Cycle-219/230 fixture is directly executed in these files.
- Pump algebra and rank/span/deletion checks are exact integer/GF(2)/Pauli equalities, not floating residuals (P964-966).

## 9. Output conventions

### Recurrent runner

- `R.main() -> None` (R603-838). Local `check(label: str,condition: bool) -> None` appends `{"label":label,"pass":bool(condition)}` and prints, via two print arguments, exactly `PASS <label>` or `FAIL <label>` (R627-632).
- After checks it prints one compact, key-sorted line `SUMMARY_JSON <json>` (R828-831), then exactly one sentinel line: `RECURRENT_OVERLAP_COMPANION_UPDATE_PASS` or `RECURRENT_OVERLAP_COMPANION_UPDATE_INCOMPLETE` (R832). Failure exits 1.
- The report includes `status`, aggregate `pass`, `authority="none"`, `audit="unset"`, a literal baseline commit, checks/certificates, supplied / derived / open / claim boundary structures, compiler/no-go gates, and `report_sha256` computed over sorted compact JSON *before* adding the digest field (R763-830).

### Pump runner

- `P.box_certificate(shape: tuple[int,int,int], atlas: dict[str,object]) -> dict[str,object]` (P544-813) returns the complete per-box basis, routing, correction, deletion, parent-normalization, and retained-resource report described above.
- `P.main() -> None` (P848-1021) has the same `PASS/FAIL <label>` convention (P853-857), then prints the full report as pretty JSON with `indent=2` and `sort_keys=True` (P983-1015). There is no pump sentinel and no report digest; non-PASS exits 1 (P1015-1017).
- Neither file reads/writes a runner-cache `.txt`, defines a cache path, or produces a receipt record. Visible audit metadata are the identical `AUDIT_TIMEOUT_SEC=900`, `NOTE_PATH`, `AUDIT_INPUT_PATHS`, and `DECLARED_INPUT_PATHS=AUDIT_INPUT_PATHS` globals (R21-74, P29-76). The recurrent report has baseline/digest fields; those are report fields, not a cache receipt.

## 10. Import graph and self-containedness

- **R runtime local imports** (R96-104): `frontier_cycle720_cell_majorana_companion_geometry... as M`; `...companion_subsystem_m2_update... as U`; `...companion_subsystem_mixed_gauge_factorization... as F` (alias visibly unused); `...overlap_star_mixed_gauge_choi... as O`; `...companion_repeated_star_choi_tensor... as R`; `...companion_checkerboard_frame_cocycle... as Q`; `frontier_cycle708_endpoint_cube_tableau_core... as T`; `frontier_full128_cycle_encoder... as F128`; and `frontier_full128_25site_nn_circuit_core... as S25`. It also uses NumPy and stdlib `Counter`, `sha256`, product, JSON, math.
- **R type-check-only imports** (R85-94): fixed-sector even-CAR Bell, fixed-sector live-input teleportation, local Choi pump covariance, this tree/plaquette pump, local genesis broadcast, and three-route adversary. They are citation-graph edges only and do not execute at runtime.
- **P runtime local imports** (P83-88): geometry `M`, coherent common-E `C`, checkerboard cocycle `Q`, repeated-star tensor `R`, subsystem mixed-gauge factorization `F` (alias visibly unused), and overlap Choi `O`; plus stdlib `defaultdict`, `sha256`, permutations/product, and JSON.
- The long `AUDIT_INPUT_PATHS` tuples declare citation/audit dependencies but are not dynamic imports (R23-73, P31-75).
- Neither runner is self-contained. Essential imported surfaces include fixture construction and edge records, Pauli/tableau operations, factorization, physical update construction and NN routing, Choi graph construction/span replay, frame/coframe actions, GF(2) solve/rank, parent tensor normalization, inherited coin/contact fixtures, route selection, and support diameter.

## 11. REUSE PLAN for three Cycle-721 runners

### Reimplement verbatim or call unchanged

- **Shared site map:** preserve `Q.shape_cells -> O.arbitrary_fixture`, the single global union fixture, cell-major 6+3 physical indices, separate 3N coframe allocation, and the exact `semantic_factor_keys` tuples. Copy the overlap set-union/ownership checks; never concatenate two cube fixtures.
- **Input-side Bell compilation:** retain the Choi tableau order `[physical matter 6N][companion 3N][coarse input 6N]`. Reuse `direct_graph_basis`, `pauli_product`, and parity-product convention verbatim. Preserve sign phases from `R.choi_pauli`.
- **Encoded-input Clifford/private corrections:** reuse verbatim `incident_port_mask`, `solve_private_correction`, `local_signature`, `signature_pauli`, `onsite_allowed`, `edge_allowed`, `build_private_atlases`, and `correction_from_atlas`. Build the atlas once, freeze it, and use endpoint order `(left,right,axis)` exactly.
- **Pump schedule:** reuse verbatim `coordinate_maps`, `edge_lookup`, `schedule_tree_plaquettes`, `schedule_basis`, `schedule_correction`, `pauli_cells`, `returned_route`, and `route_execution_failures`. Keep onsite/tree/plaquette row order and retained syndrome semantics.
- **Recurrent G:** call the imported `U.placement`, `U.physical_word`, and `U.c707.route_word` unchanged. Preserve four macro layers and seam 01-before-23 order. Reuse `coordinate_intertwiner_certificate`, `schedule_certificate`, and the unitarity/inverse checks as composition gates.
- **Covariance:** reuse signed `fields`, the accepted seam row classes, and both signed and binary family multiset comparisons. Preserve the split between frame/shift/seed update covariance and the 576-product retained coframe channel.

### Adapt for each new runner

- The input-side Bell runner should adapt `box_certificate` to its new encoded-input map while retaining the exact direct-basis ordering, parity-correlation test, parent signed-span equality, and no-reset retained resources.
- The encoded-input Clifford runner should add its Clifford tableau action and chart routes around the existing basis/private-correction surface. It needs a new explicit JW chart-route compiler and covariance counters; these two files provide only the “do not place onsite corrections on input JW” constraint.
- The collision-free epoch runner must create a new global resource namespace and schedule keys that compose: Bell initialization; ordered onsite/tree/plaquette pump; returned measurement route; private correction; retained syndrome storage; coupling; any frame correction; then recurrent G. It must add collision tests because Cycle-720 explicitly leaves this controller layout open.

### Silent composition traps

- **Fixture identity:** rebuilding per-cover fixtures silently duplicates the 4 shared cells/36 physical registers and changes global indices and edges.
- **Index spaces:** recurrent physical `9N`, coframe `3N`, Choi input `6N`, Bell purifiers, syndrome bank, and mobile rail are distinct spaces. Never interpret pump `total_qubits=15N` as recurrent retained `12N`.
- **Edge orientation:** atlas keys use fixture `(left,right,axis)`, semantic seam ownership uses `(lower-endpoint owner,axis,factor)`, while geometric lookup uses unordered endpoint frozensets. Sorting/reversing one without recompiling all three breaks keys or phases.
- **Order/sign:** Pauli phase mod 4, both parity-sector phase, `@` product order, canonical seam order `(0,1,2,3)`, allowed reversal `(1,0,3,2)`, onsite/tree/plaquette order, and allowed-qubit order are all load-bearing.
- **Atlas scope:** atlas values are unique only under exact six-port masks and exact local-qubit orders. Refitting on a held box defeats the reuse control.
- **Returned work:** the mobile rail must finish at its anchor after every measurement; syndrome/Bell purifiers remain allocated. “Returned route” does not authorize resetting those retained banks.
- **Epoch semantics:** E/pump is one-time genesis; recurrent powers are resource-count induction checks, not clock slots, and no fresh encoder environment may appear after genesis.
- **Global/imported state:** `Q.S`, nested namespaces such as `U.C712` and `C.R.F.base`, imported fixture enumeration, and `Pauli` phase behavior are implicit global contracts. A new runner should pass fixtures/atlases/schedule-key maps explicitly and digest them; module reloads or locally reconstructed orderings can silently fork the convention.
- **Schedule keys/collisions:** no Cycle-720 schedule-key schema or collision counter exists. Cycle-721 must define keys over global register IDs plus epoch/layer/route position and reject simultaneous ownership; it cannot infer safety from commuting stabilizers or returned routes.

## COMPLETENESS

- Fully extracted: every function/global/class name defined in the two files, visible signatures and return shapes, union/ownership/count conventions, recurrent schedule/induction, pump basis/atlas/tree/route/channel, coordinate checks, visible covariance/residual/output/import contracts, and composition traps.
- Imported/therefore not fully extractable under the two-file boundary: `shape_cells` enumeration order, `CompanionFixture`/edge tuple definitions, coframe indices/equations, `physical_word` instruction/`update` schemas, recurrent NN router construction/distance, Choi and factorization internals, inherited fixture internals, and parent normalization.
- Requested but absent from both sources: collision counters and epoch layout; tableau-image/stabilizer/private-correction/atlas-key/schedule-key/returned-route *covariance* counters; an explicit JW chart-route recompilation rule; runner-cache `.txt` and receipt production.
- The literal 428 is not printed as a source constant; its decomposition above uses the task-supplied total plus the visible 3x2x2 geometry/key loops. No script was run, so runtime-produced numeric route loads, atlas digests, report digests, and residual values were not collected.
