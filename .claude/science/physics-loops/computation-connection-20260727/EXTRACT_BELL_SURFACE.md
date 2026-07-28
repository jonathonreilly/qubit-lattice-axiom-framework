# Cycle-720 Bell / live-input surface extract

Scope is strictly the following two sources:

- `B` = `scripts/frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27.py`
- `L` = `scripts/frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27.py`

Line numbers below are source line numbers. “Delegated” means that the named
operation is called here but defined in an imported runner, which was outside
the permitted read set. Such behavior is not reverse-engineered or guessed.

Neither source defines a class. Both import `M.Pauli` (aliased `Pauli`) and
type against imported `M.CompanionFixture`. Top-level certificate entry points
are `B.box_certificate(shape: tuple[int,int,int], atlas: dict[str,object])
-> dict[str,object]` (`B:158-304`),
`L.box_certificate(shape: tuple[int,int,int]) -> dict[str,object]`
(`L:437-638`), and each file's `main() -> None` (`B:381-508`;
`L:641-768`). Their relevant dictionary fields are named in the sections
below; nested return shapes are explicit where constructed locally.

## 1. Cell/mode labeling

### Types and coordinates

- `L:89` defines `Coord = tuple[int, int, int]`. Cells are stored as `fixture.cells`; a cell identifier used in mode formulas and edge tuples is its zero-based index in that sequence. A geometric cell is the corresponding three-integer coordinate `fixture.cells[cell]` (`B:197-201`, `L:240-242,506,511-512`).
- Fixtures for rectangular boxes are made by the delegated composition `O.arbitrary_fixture(Q.shape_cells(shape))` (`B:158-162`, `L:437-439`), where `shape: tuple[int, int, int]`.
- Cell ordering is semantically significant. Corners/roots use lexicographic `max(fixture.cells)` and convert back with `.index(...)` (`L:138-153`, `L:240-242`). The spatial tree is requested with axis order `(2, 1, 0)` (`L:139-141`).

### Six matter modes per cell

- Global raw-mode index is exactly `6 * cell + local`, with `local in range(6)` (`B:96-101`; `L:127-133,153`).
- The five onsite adjacent pairs use local pairs `(0,1),...,(4,5)`; `mode_tree(fixture)` emits global endpoints `left = 6*cell + local`, `right = left+1` (`L:122-154`).
- `tag_modes(fixture, tag) -> frozenset[tuple[int,int]]` (`B:113-121`) returns `(cell_index, local_mode)`. For an edge it reads `fixture.edges[tag[1]]` and reduces the two endpoint mode labels modulo six.

### Tags, edges, ports, center/parity/coframe labels

- Bell tags are tuples. Exact local discriminants are: `("onsite_Z", cell, local)`, `("onsite_XX", cell, local_left)`, and `("edge", edge_index, ...)` as consumed by `target_rows`/`tag_modes` (`B:91-121,187-201`). Only `tag[0]` and the stated positions are consumed here; the full tuple produced by `P.direct_graph_basis` is delegated.
- An edge record is destructured as `(left_cell, right_cell, owner, axis, left_mode, right_mode)` (`B:120-121`; `L:142-145`). The first two entries index `fixture.cells`; the last two are global raw-mode endpoints in `L:143-152` and are normalized modulo six only when producing CAR support in `B:120-121`. `owner` and `axis` are retained but not interpreted locally.
- Physical companion-port allocation is visible only through the corner `allowed` tuple: three indices per cell, `fixture.matter_qubits + 3*cell ... +2` (`L:242-251`). Port names, orientations, and the mapping from edge `(owner,axis)` to those three ports are not defined in these files.
- The fixed parity label is integer `parity in (0,1)` / strings `("even","odd")` (`L:280-301`). It signs a Pauli by phase `2*parity` modulo four (`L:280-293`). The input parity row is all-Z on the resource input half (`L:235-239`).
- Center coordinates are not individually labeled here. Center rows are a contiguous factorization slice `[logical+gauge : logical+gauge+center]` of `factor.physical_w` (`L:269-278,475-482`); the last center row is the parity-signed row (`L:287-293`).
- Coframe coordinate/origin representation is not local. The even-CAR runner passes an atlas to delegated `V.frame_certificate` and `V.product_certificate` only (`B:386-387`).

## 2. Physical M2 register allocation

- `m = fixture.matter_qubits`, `q = fixture.qubits`, and a Choi/stabilizer tableau spans `total = q + m` qubits (`B:167-169`; `L:256`).
- Physical output M2 indices are `0..q-1`; the Choi resource input half is `q..q+m-1`. This is explicit in the all-Z input parity mask `((1<<m)-1) << q` (`L:235-239`) and in the corner input-half range `q+6*cell ... q+6*cell+5` (`L:248-251`).
- Within physical output M2, the first `m=6N` indices are the six matter images per cell. `physical_z(fixture, mask) -> Pauli` truncates `mask` to these first `m` bits (`L:114-115`). The visible companion allocation is the following `3N` indices, `m+3*cell ... m+3*cell+2` (`L:245-247`). Consequently the visible layout is `[6N matter][3N companion]` inside `fixture.qubits`, followed in augmented tableaux by `[6N Choi input]`. These files do not independently assert `q == 9N`; code using this layout assumes the imported fixture provides it.
- `target_z(mask) -> Pauli` leaves an `m`-mode target mask unshifted (`L:118-119`). `operator_syndrome(fixture, physical, target) -> tuple[int,...]` compares a `q`-qubit physical row and an `m`-qubit target row against each triple from delegated `M.operator_rows(fixture)` (`L:96-111`).
- The one-cell allowed solve support is ordered exactly as a tuple of: six physical matter indices, three physical companion indices, then six resource-input indices (`L:242-255`). `P.solve_private_correction` receives that tuple unchanged.
- No explicit “site map” object is created here. Shared mapping is embodied by `fixture.cells`, `fixture.edges`, the arithmetic above, and delegated `P.pauli_cells(fixture,row)` (`B:204`; `L:226-229`).

## 3. CAR/Majorana and Pauli representation

### Representation and signs

- Both runners alias `Pauli = M.Pauli` (`B:84`; `L:88`). Rows have integer fields `phase`, `x`, `z`; support uses `(row.x | row.z)` and binary symplectic vectors use `row.symplectic(number_of_qubits)`.
- `canonical(row: Pauli) -> Pauli` is identical in both runners: `Pauli((row.x & row.z).bit_count() & 1, row.x, row.z)` (`B:87-88`; `L:92-93`). Thus canonical phase is the parity of X/Z overlap: phase 1 for an odd number of Y sites, otherwise phase 0. Multiplication is `left @ right`; products are canonicalized at the boundary (`B:106-110`; `L:150-151,216-223`).
- Commutation is binary symplectic: `M.symplectic(v,w,n)` returns the bit tested/summed as a failure (`B:180-186,223-226`; `L:99-110,257-262,487-500`).
- Concrete matrices exist only in `B.sector_matrix`; the scalable CAR surface is a binary Pauli/tableau surface, not dense matrices.

### Local even-CAR generators

- Onsite parity is `Z_j = Pauli(z=1<<j)`.
- An onsite adjacent-Majorana-pair coordinate is represented as `X_j X_(j+1) = Pauli(x=(1<<j)|(1<<(j+1)))` (`B:96-101,327-333`; `L:127-133`). The source describes these as adjacent Majorana-pair rows; it does not construct creation/annihilation operators.
- A seam row is the third term (`[2]`) of `fixture.target_terms(edge_index)` (`B:101-103`). The raw-mode runner pairs it with `fixture.physical_terms(edge)[2]` (`L:142-152`).
- For a raw spatial correction, the seam target's Z mask is used as the Jordan--Wigner cleanup. `cleanup_physical = physical_z(fixture, seam_target.z)` and `cleanup_target = target_z(seam_target.z)` are multiplied into the seam rows, yielding the raw `X_u X_v` target (`L:135-152`).
- Fixed-superselection convention: allowed live/resource inputs share one total computational-basis parity sector. Same-sector Bell X outcome `a` has even Hamming weight; an odd `a` is detected at the decoder root (`L:351-417,420-434,542-544`). The exact dense certificate in `B` selects parity `0` only (`B:320-324,339`).

### Dense sector ordering

- `sector_matrix(row: Pauli, modes: int, parity: int) -> np.ndarray` (`B:307-324`) builds factors in `reversed(range(modes))`, so raw mode 0 is the least-significant computational bit. Single-site selection is exactly `(I,X,Z,Y)[x + 2*z]`; Kronecker factors are accumulated left to right.
- The retained basis is ascending integer state order filtered by `state.bit_count() % 2 == parity`. Return shape is `(2^(modes-1), 2^(modes-1))`.
- `sector_matrix` does not multiply by `row.phase`; callers pass canonical rows and subsequently quotient matrices by phases `(1,-1,1j,-1j)` (`B:339-344`). A new runner must not assume arbitrary signed Pauli phases survive this matrix conversion.

## 4. Doubled even-CAR Bell row family

### Construction APIs and ordering

- `target_rows(fixture: M.CompanionFixture, tags: tuple[tuple,...]) -> tuple[Pauli,...]` (`B:91-103`) preserves tag order. Dispatch is: onsite Z, onsite adjacent XX, otherwise seam target term `[2]`.
- `P.direct_graph_basis(fixture)` returns `(graph, tags)` and is the single ordering authority (`B:161-166`). `targets`, `corrections`, doubled rows, supports, syndromes, and deleted-row tests are all zipped/indexed in this same order. Reordering any one silently breaks private-dual matching.
- The visible family implies `6N` onsite-Z plus `5N` adjacent-XX plus `E` seam rows, i.e. `11N+E`, but neither file explicitly counts or asserts that formula. It depends on the delegated tag producer returning all of those rows in the expected order.
- Doubled Choi rows are `P.R.choi_pauli(row, row, m)` for each target (`B:174-176`): the same even-CAR row on both halves. Return is `tuple[Pauli,...]`.

### Ranks and commutation

- Rank is delegated GF(2) rank of symplectic vectors: `P.C.R.F.base.gf2_rank(row.symplectic(m) for row in targets)` and similarly at width `2*m` for doubled rows (`B:171-179`).
- Expected connected even-algebra rank is exactly `2*m - 1` (`B:278-280,374-378`; `L:594-596`).
- Fixed-sector independent random Bell bits are `target_rank - 1`, checked against `2*(m-1)` (`B:279-281,397-400`). This is the quotient by the fixed total-parity center.
- Doubled rows must retain the target rank and commute pairwise. The commutator counter sums `M.symplectic(...)` over each unordered prior pair (`B:174-186`); the main check requires rank equality and zero failures (`B:401-405`).
- `deterministic_even_samples(modes) -> tuple[Pauli,...]` (`B:139-155`) contains identity, all-Z, each single Z, each `X_0 X_mode`, and 64 SHA-256 seeded rows. Seeded X is masked to `modes` bits and made even by toggling bit 0; Z is unrestricted. Output is deduplicated and sorted by `(row.x,row.z,row.phase)`.

## 5. Private-dual atlas

### API, keys, and lookup

- Atlas construction is exactly `atlas = P.build_private_atlases()` (`B:381-383`). The local static type is only `dict[str, object]` (`B:158-160`).
- Lookup is exactly `P.correction_from_atlas(fixture, tag, atlas)` for each tag in the unchanged `P.direct_graph_basis` ordering (`B:161-166`). There is no local fallback, exception handler, or unseen-key branch: any missing-key behavior is wholly delegated and will propagate out of `box_certificate`.
- The top-level atlas visibly has payload keys `"onsite"` and `"edge"`: report serialization removes precisely those two and retains every other atlas item as metadata (`B:467-471`).
- The requested 704 onsite keys, 192 edge keys, and their serialized key format are not present in either allowed file. They may be products or metadata of `P.build_private_atlases`, but cannot be specified from this surface alone. The only locally visible lookup key is the Bell `tag` tuple described in section 1.

### Duality, support, and diameter

- Each correction is a physical `Pauli`. One-hot private duality is enforced against `graph`: for target index `t`, every graph row `r` must satisfy `symplectic(correction_t, graph_r) == int(r == t)` at width `total=q+m` (`B:204-226`).
- Physical support cells are `P.pauli_cells(fixture, correction) -> frozenset[Coord]` (`B:204`; same wrapper at `L:226-229`). Diameter is delegated `P.R.support_diameter(support)` (`B:219-221`; `L:503-505`).
- Declared support is exactly `{fixture.cells[tag[1]]}` for non-edge tags, or the two coordinate cells at `fixture.edges[tag[1]][:2]` for edge tags. Failure is `not support <= declared` (`B:209-217`), so empty/subset support is allowed by the locality predicate; one-hot syndrome prevents an irrelevant empty dual in normal use.
- Report maxima are `len(support)` and delegated graph diameter (`B:218-221,287-291`). Main requires no syndrome/support failures, maximum cells `<=2`, diameter `<=1` (`B:409-417`).
- Branch correction is the ordered Pauli product of all atlas rows whose syndrome bit is one (`B:243-253`). `pauli_product(rows) -> Pauli` starts from identity, multiplies with `@` in generator order, and canonicalizes only the final result (`B:106-110`).
- Syndrome is the target character `s_i = symplectic(error,target_i)`; replay is the physical correction character against graph row `i` (`B:243-257`). Every kernel relation from `M.kernel_relations(target symplectic vectors)` must have even syndrome sum (`B:239-264`).
- The deletion witness selects `len(corrections)//2` and requires its matching correction/graph symplectic residual to be one (`B:266-271,463-466`).

### Separate corner solve in the raw-mode runner

- `sector_resource_certificate(fixture) -> dict[str,object]` (`L:232-348`) augments the graph with all-Z input parity and calls `P.solve_private_correction(augmented, len(rows), allowed)` (`L:235-255`). Return is destructured as `(correction, rank, contradictions)`, with `rank` intentionally unused.
- Its one-hot target is the appended parity row. It reports contradiction count, syndrome failures, physical weight, and support-cell count (`L:253-263,300-317`). This is a direct solve, not an atlas lookup.

## 6. Measurement-conflict and correction layers

- `greedy_layers(supports: tuple[frozenset,...]) -> tuple[int,...]` (`B:124-136`) is deterministic, input-order-dependent first-fit coloring. A support enters the first existing layer in which it is disjoint from every already placed support; otherwise a new layer is appended. Return has one zero-based layer index per input support.
- Measurement vertices use `tag_modes`: supports are sets of `(cell_index, local_mode)`; an onsite Z touches one mode, onsite XX two modes in one cell, and a seam its two endpoint modes (`B:113-121,187,228`).
- Correction vertices use exact physical qubit support: `frozenset(qbit for qbit in range(q) if ((row.x|row.z)>>qbit)&1)`. Notice the range stops at `q`; any resource-half bits at indices `>=q` do not participate in correction coloring (`B:229-234`).
- Layer count is `max(assignment, default=-1)+1` (`B:286,291`). Main requires measurement layers `<=6`, correction layers `<=24`, and exact constancy of each count across `boxes[1:]` (the three held shapes after `(2,2,2)`) (`B:383-385,419-425`).
- Coloring checks support overlap only. They do not directly test Pauli commutation, route collisions, or cross-conflict between measurement and correction epochs.

## 7. Fixed-sector live-input/CPTP surface

### Exact two-/three-mode matrix certificate

- `abstract_teleportation_certificate(modes: int) -> dict[str,object]` (`B:327-378`) is called only for `modes in (2,3)` (`B:385`).
- Generator rows, in order, are every onsite Z followed by every adjacent XX (`B:327-333`). Their expected GF(2) rank is `2*modes-1`.
- It exhausts all bit masks `x,z`; only even-Hamming-weight `x` survives. `sector_matrix(canonical(Pauli(x=x,z=z)), modes, 0)` is deduplicated modulo global phases `(1,-1,1j,-1j)` with tolerance `1e-12` (`B:334-344`). The resulting `even` ordering is nested integer `x`, then integer `z`, retaining the first representative of each phase class.
- Fixed-sector dimension is `d=2^(modes-1)`. The normalized vectorized maximally entangled reference is represented as the matrix `phi = I_d/sqrt(d)`. Bell matrices are `error @ phi`; `np.vdot` flattens them for the Gram matrix (`B:345-350`). Return Gram shape is `(d^2,d^2)` once the expected complete basis is obtained.
- For each ordered `(error,bell_matrix)` pair: `kraus = bell_matrix.conj().T/sqrt(d)`, hence `K=U†/d`; `corrected = error @ kraus` is compared with `I_d/d` in Frobenius norm; and completeness accumulates `K†K` (`B:351-361`).
- Returned exact-control fields are: `modes`, `fixed_sector_dimension`, `Bell_outcomes`, `expected_outcomes=d*d`, `Bell_basis_orthonormality_residual`, `corrected_branch_identity_residual` (maximum over branches), `Kraus_completeness_residual`, `generator_rank`, and `expected_even_rank` (`B:362-378`).
- Main requires outcome count/rank equality and all three residuals `<1e-12` (`B:435-445`). This is the only explicit Kraus assembly in either file.

### Raw-mode coherent Bell/correction ceiling

- `bell_parity_certificate(modes: int) -> dict[str,object]` (`L:351-417`) exhausts same/opposite sector pairs for `modes<=6`; larger cases use four generator tests per mode. It also constructs `bell = kron(H,I) @ CNOT` and reports `||bell†bell-I_4||`. The stated coherent operation order is: `CNOT(live,input-half)`, `H(live)`, retain both Bell registers, decode input-half X word, control physical corrections, reverse decoder CNOTs (`L:395-416`).
- Bell outcomes are integer masks `(a,b)`: `a` is the even raw-X word and `b` is the Z word. `outcome_samples(modes) -> tuple[tuple[int,int],...]` includes `(0,0)`, `(0,all_Z)`, each singleton `b`, each `a=X_0X_mode`, plus 64 SHA-256 seeded pairs; seeded `a` is made even by toggling bit zero, and output is deduplicated/sorted (`L:420-434`).
- `mode_tree(fixture) -> (edges, root_mode)` (`L:122-154`) returns a tuple of `(left_mode, right_mode, physical_Pauli, target_Pauli, kind)` and one integer root. It concatenates all `5N` onsite path edges, then delegated spatial cell-tree seams. `kind` is exactly `"onsite"` or `"spatial"`.
- `tree_structure(modes, edges, root)` (`L:157-174`) returns `(parent, order)`, where `parent[root]=None`, all other values are `(parent_vertex, edge_index)`, and breadth-first discovery follows `sorted(adjacency[vertex])`.
- `decode_even_x(a,modes,parent,order) -> tuple[int,int,tuple[tuple[int,int],...]]` (`L:177-194`) walks non-root vertices in reverse discovery order. It returns the edge-coefficient bit mask, final root parity bit, and child-to-parent CNOT word. `modes` is in the signature but unused by the body.
- `apply_cnot_bits(state,word) -> int` applies in tuple order via `state ^= bit(control)<<target` (`L:197-200`). Inversion uses `tuple(reversed(word))` (`L:533-540,566-570`).
- `correction_for_outcome(fixture,edges,parent,order,a,b) -> tuple[Pauli,Pauli,int,int,tuple[tuple[int,int],...]]` (`L:203-223`) initializes physical/target correction with Z mask `b`, then multiplies selected tree-pair rows according to decoded `a`; both Paulis are canonicalized. Remaining outputs are coefficients, root parity, word.
- Exact branch identity here is Heisenberg/symplectic, not a dense Kraus calculation: `operator_syndrome(fixture,physical,expected raw Pauli)` must vanish for `expected=canonical(Pauli(x=a,z=b))` (`L:557-575,632-637`). One-cell branches are exhaustive; larger boxes use deterministic samples (`L:550-556`).
- Fixed-resource augmentation adds one independent parity stabilizer, keeps a mixed gauge factor, and checks both signed parity sectors by changing the last center row phase by `2*parity mod 4` (`L:232-348`). Its normalized input marginal is recorded literally as `"Pi_parity/2^(matter_qubits-1)"` (`L:338-340`).

## 8. Proper-cubic covariance harness

- The only local calls are `covariance = V.frame_certificate((2,2,2), atlas)` and `products = V.product_certificate(atlas)` (`B:386-387`). Both implementations, their signatures beyond these call shapes, and their return annotations are delegated.
- Main requires `covariance["proper_cubic_frames"] == 24` and `products["ordered_frame_products"] == 576` (`B:446-461`). It does not locally enumerate either set.
- For every single frame, these exact counters must be zero (`B:449-459`): `signed_projector_failures`, `private_correction_syndrome_failures`, `private_correction_support_failures`, `route_locality_support_or_return_failures`, `atlas_key_inverse_transport_failures`, `schedule_key_inverse_transport_failures`, `Bell_reference_conjugate_chart_failures`, `syndrome_register_bijection_failures`, and `oriented_factor_2_or_3_edge_row_failures`.
- For ordered products, every returned item whose key ends with `"failures"` must equal zero (`B:460-461`); exact product counter names are not visible.
- The check label states the compared/transported surface as “projector, atlas, corrections, and schedules” (`B:447`). Counter names additionally expose signed projector replay, inverse atlas/schedule-key transport, Bell reference conjugate chart, syndrome-register bijection, and oriented factor-2-or-3 edge rows. Exact transported object structures/comparison formulas remain delegated.
- The requested eight coframe origins and their enumeration/order are not present in either allowed file. `B` only records a supplied `"coframe-origin gauge sector"` in report prose (`B:481-485`).

## 9. Preregistered support gate

- The exact positive locality predicate is: `maximum_support_cells <= 2 and maximum_support_diameter <= 1`.
- On the accepted even-CAR/private-dual route it is enforced for every held box using fields `maximum_private_dual_support_cells` and `maximum_private_dual_support_diameter` (`B:409-417`). The underlying support is a coordinate-cell set from `P.pauli_cells`; diameter is `P.R.support_diameter` (`B:204-221`).
- On the raw-X route:

```python
nontrivial = boxes[1:]
locality_gate = all(
    box["maximum_generator_support_cells"] <= 2
    and box["maximum_generator_support_diameter"] <= 1
    for box in nontrivial
)
```

  This is `L:720-725`. `boxes[1:]` excludes `(1,1,1)` and includes `(2,2,2),(3,2,2),(4,2,2),(5,2,2),(5,3,2)` (`L:641-646`).
- This raw-route runner is preregistered to certify failure: its check passes only when `not locality_gate` and the last `(5,3,2)` box has both cells `>2` and diameter `>1` (`L:726-731`). Generator support/diameter are accumulated over each physical tree correction row (`L:483-505`).

## 10. Output contract

- Both nested helpers have signature `check(label: str, condition: bool) -> None`. They append `{"label": label, "pass": bool(condition)}` then execute:

```python
print("PASS" if condition else "FAIL", label)
```

  This is `B:390-392` and `L:649-651`. Exact line form is `PASS <label>\n` or `FAIL <label>\n`, with the default single separator.
- Exact `B` labels in print order (`B:394-466`):

    1. `local doubled even-CAR rows give a complete fixed-sector Bell algebra`
    2. `frozen private-dual atlas stays physical-M2 local on the held ladder`
    3. `measurement and correction words admit size-independent conflict coloring`
    4. `lawful even Bell characters are exactly cancelled without changing fixed centers`
    5. `small-sector matrices certify CPTP teleportation rather than a formal syndrome relabeling`
    6. `proper-cubic 24-frame and 576-product action preserves projector, atlas, corrections, and schedules`
    7. `deleting a matching local private dual leaves a nonzero Bell sign residual`

- Exact `L` labels in print order (`L:653-731`):

    1. `fixed parity adds one independent Choi stabilizer with a bounded corner correction and retained syndrome`
    2. `local Bell coupling makes every same-sector X word even and detects a parity mismatch at the decoder root`
    3. `bounded-degree mode tree spans the complete even Pauli correction algebra and the reversible decoder returns its work`
    4. `every physical correction generator is the exact gauge-and-center-preserving image of its raw Bell Pauli`
    5. `exhaustive one-cell and deterministic larger-box branches satisfy the corrected-channel intertwiner`
    6. `spatial correction deletion is detected`
    7. `held non-collinear ladder detects failure of the bounded two-cell raw-X correction gate`
- Each then prints exactly `json.dumps(report, indent=2, sort_keys=True)` (`B:502`; `L:762`). Residuals have no separate print format; they are JSON numbers under the exact field names given in sections 7/8 or nested box certificates. JSON keys are lexicographically sorted and indented by two spaces.
- `B.report` top-level keys (`B:467-501`): `status`, `checks`, `atlas` (metadata excluding payload keys), `boxes`, `exact_CPTP_controls`, `covariance`, `frame_products`, `derived`, `supplied`, `open`, `claim_boundary`, `input_Bell_measurement_physical_M2_compiled` (literal `False`), `authority` (literal `"none"`), `audit` (literal `"unset"`).
- `L.report` top-level keys (`L:732-761`): `status`, `checks`, `boxes`, `derived`, `supplied`, `open`, `claim_boundary`, `authority` (literal `"none"`), and `audit` (literal `"unset"`).
- `status` is `"PASS"` iff all check records pass, otherwise `"FAIL"`. After JSON, non-PASS exits with `SystemExit(1)`; PASS returns normally (`B:503-504`; `L:763-764`).
- Neither file opens or writes a log, runner-cache `.txt`, or receipt JSON. No paired-log/cache format or receipt-field derivation is visible. They only declare audit globals `AUDIT_TIMEOUT_SEC=900`, `NOTE_PATH`, `AUDIT_INPUT_PATHS`, and alias `DECLARED_INPUT_PATHS=AUDIT_INPUT_PATHS` (`B:21-70`; `L:24-72`); none is consumed by either `main`.

## 11. Import graph and self-containment

### `B`

- Standard library: `from __future__ import annotations`, `hashlib.sha256`, `json` (`B:19,72-73`).
- Third party: `numpy as np` (`B:75`). No SymPy import.
- Runner imports (`B:77-81`): `frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M`; `frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q`; `frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as P`; `frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27 as V`; `frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O`.

### `L`

- Standard library: `from __future__ import annotations`, `collections.defaultdict`, `hashlib.sha256`, `itertools.product as cartesian_product`, `json` (`L:22,74-77`). `cartesian_product` is imported but not used in this file.
- Third party: `numpy as np` (`L:79`). No SymPy import.
- Runner imports (`L:81-85`): `frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as T`; the same `M`, `Q`, `P`, and `O` modules named above. `T` is imported but not used in this file.
- Neither runner is self-contained. Core `Pauli`/fixture/symplectic/span machinery comes from `M`; box cells from `Q`; graph bases, Choi rows, atlas, routing, support, and GF(2) namespace chains from `P`; factorization from `O`; and covariance from `V` in `B`.
- The long `AUDIT_INPUT_PATHS` tuples are declarations, not Python imports.

## 12. REUSE PLAN

### Reimplement verbatim

- Copy `canonical` exactly; both runners already duplicate the same function. Copy `pauli_product`, `target_rows`, and `tag_modes` together so phase, tag dispatch, mode arithmetic, and row order remain aligned (`B:87-121`).
- Copy `greedy_layers` exactly if Cycle-721 claims comparable constant layer counts; a different coloring heuristic changes the certificate surface (`B:124-136`).
- Copy `deterministic_even_samples` exactly for regression continuity, including SHA-256 strings, endian `"little"`, bit-0 parity repair, and sort key (`B:139-155`).
- Copy `sector_matrix` and `abstract_teleportation_certificate` together for the two-/three-mode CPTP control. Preserve reversed tensor-factor order, even sector `0`, phase quotient, `K=U†/d`, Frobenius norms, and `1e-12` thresholds (`B:307-378,435-445`).
- For a raw-route negative/control runner only, copy as one block `physical_z`, `target_z`, `mode_tree`, `tree_structure`, `decode_even_x`, `apply_cnot_bits`, `correction_for_outcome`, and `outcome_samples` (`L:114-223,420-434`). Do not present that block as a bounded compiler.

### Reuse imported interfaces unchanged

- Construct fixtures only as `O.arbitrary_fixture(Q.shape_cells(shape))`.
- Obtain `(graph,tags)` once from `P.direct_graph_basis(fixture)` and use that exact order for targets, doubled rows, atlas corrections, supports, syndromes, relations, schedules, and deletion witnesses.
- Build atlas once with `P.build_private_atlases()` and look up via `P.correction_from_atlas(fixture,tag,atlas)`. Reuse `P.pauli_cells` and `P.R.support_diameter` for the preregistered gate.
- Reuse `P.R.choi_pauli(row,row,m)`, `M.symplectic`, and `P.C.R.F.base.gf2_rank` with the same widths (`m`, `2m`, or `q+m`).
- If covariance remains a requirement, call the same `V.frame_certificate` and `V.product_certificate` and retain all failure-key checks. Their internal charts/keys cannot safely be reconstructed from these two files.

### Adapt for a new Cycle-721 composition runner

- Adapt shapes, composition-specific target object, report prose, and new failure counters. Keep the `check` record/print/JSON/exit contract if the runner is consumed by the same supervisor.
- Add new generators only by extending the delegated tag/atlas/covariance surface in lockstep. Locally, `target_rows` treats every unknown non-onsite tag as an edge, so an unrecognized family can silently index the wrong term.
- Enforce the two-cell/diameter-one gate positively before claiming a bounded route. The raw-X/Jordan--Wigner tree is a witnessed ceiling/failure and must not leak into the accepted even-CAR correction route.

### Coupling traps

- Six-mode arithmetic, lexicographic `max(cells)` root, axis order `(2,1,0)`, edge tuple positions, and mode-0-as-LSB matrix order are frozen conventions.
- `fixture.edges` endpoint modes are treated as global in `L` but reduced `%6` in `B.tag_modes`; mixing these coordinate levels breaks conflicts.
- Physical output has width `q`; Choi input begins at `q`. Raw target width is `m`; physical matter images begin at bit zero. A missed shift can still produce a well-formed but wrong Pauli.
- `canonical` overwrites phase, while `sector_matrix` ignores it. Preserve the phase-quotient intent; do not use this dense helper for signed-center replay.
- Private duality is index-wise one-hot in `graph/tags` order. First-fit layer numbers are also order-dependent. Sorting tags/corrections independently is a silent semantic break.
- Measurement coloring uses `(cell,local_mode)`; correction coloring uses physical qubit indices only below `q`. They are different conflict graphs.
- Fixed-sector bits are `2(m-1)`, not `2m-1`: total parity is fixed after the full even algebra rank is computed.
- The atlas object is global immutable-by-convention state shared across box and covariance certificates. Rebuilding or mutating per frame could alter lookup/chart consistency.
- The covariance check relies on external inverse key transport and conjugate Bell charts. Recreating only the 24 rotations without those chart actions is insufficient.

## COMPLETENESS

- Item 1: six-mode/cell/edge/register conventions are extracted; named companion-port orientation, individual center labels, and coframe-origin coordinates are delegated and absent.
- Item 3: Pauli/Majorana-pair representation and parity conventions are extracted; explicit gamma and creation/annihilation constructors are absent.
- Item 4: the family implies `11N+E`, but its producer/count assertion is in delegated `P.direct_graph_basis`, so exact tag enumeration is not visible.
- Item 5: atlas API and top-level payload names are visible; the requested 704/192 counts, inner key serialization, and unseen-key policy are absent.
- Item 8: expected counts and failure keys are visible; the 24 frames, 576 product order, eight origins, transport maps, and comparisons are delegated.
- Item 10: stdout and report JSON are complete; paired logs, runner-cache `.txt`, and receipt JSON are not created or described by either source.
- All other requested items are fully extractable at this two-file interface boundary. No source other than `B` and `L` was consulted, and no script was run.
