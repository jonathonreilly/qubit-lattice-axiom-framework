# Cycle-720 base extraction: companion geometry and mixed-gauge factorization

Scope: only the two requested source modules were inspected. “Public” below means
locally defined non-underscore constants, aliases, classes, methods, and functions.
Neither module defines `__all__`; imported module/decorator/helper names therefore
also leak through ordinary Python attribute lookup, but they are dependencies, not
locally specified APIs. They are listed under coupling traps rather than treated as
re-exported runner entry points.

## 1. Module M — cell/box/union geometry

Source: `scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py`.

### Module constants and type aliases

| Line | Exact name | Type/value and role |
|---:|---|---|
| 14 | `AUDIT_TIMEOUT_SEC` | `int = 900`; metadata only. |
| 15 | `NOTE_PATH` | `str`; theorem-note path. It is not opened by this module. |
| 16 | `AUDIT_INPUT_PATHS` | `tuple[str, ...]`; declared provenance paths, ending at line 50. It has no computational effect. |
| 51 | `DECLARED_INPUT_PATHS` | Exact object alias of `AUDIT_INPUT_PATHS`. |
| 62 | `Pauli` | Type/class alias `C.Pauli`, imported from the coherent cell-edge-gauge dependency. |
| 63 | `Coord` | Runtime generic alias `tuple[int, int, int]`. |

### `CompanionFixture` and base geometry

`CompanionFixture` (line 93) is a frozen dataclass. It is the only geometry class
defined by M.

| Line | Field | Exact annotated type | Meaning |
|---:|---|---|---|
| 94 | `shape` | `tuple[int, int, int]` | Finite box dimensions supplied by the caller. |
| 95 | `cells` | `tuple[Coord, ...]` | Ordered cell coordinates inherited from `C.CellEdgeGauge`. Tuple position is the cell index used everywhere else. |
| 96 | `edges` | `tuple[tuple[int, int, Coord, int, int, int], ...]` | Ordered records `(left_cell, right_cell, owner_coord, axis, left_mode, right_mode)`. The endpoint modes are global matter-qubit indices when used as Pauli bits; `% 6` recovers their local port/mode. |
| 97 | `matter_qubits` | `int` | Inherited from the base fixture; downstream indexing assumes six matter qubits per cell. |
| 98 | `qubits` | `int` | Total physical qubits, `matter_qubits + 3*len(cells)`. |

Methods:

| Line | Exact signature | Return | Computation/conventions |
|---:|---|---|---|
| 101 | `CompanionFixture.build(cls, shape: tuple[int, int, int]) -> "CompanionFixture"` | `CompanionFixture` | Class method. Calls `C.CellEdgeGauge.build(shape)`, copies its `cells`, `edges`, and `matter_qubits`, then appends three companion qubits per cell. |
| 111 | `matter_gamma(self, cell: int, mode: int, odd: bool) -> Pauli` | `Pauli` | A within-cell Jordan–Wigner Majorana on matter qubit `6*cell+mode`. `odd=False` gives `X` with `Z` on lower local modes; `odd=True` also places `Z` on the endpoint and sets phase exponent 1. No range checks. |
| 120 | `companion_eta(self, cell: int, direction: int) -> Pauli` | `Pauli` | Companion Majorana for numeric port/direction `0..5`: companion qubit local index is `direction//2`, its even/odd Majorana selector is `direction&1`, and its global qubit is `matter_qubits+3*cell+direction//2`. Its Jordan–Wigner prefix covers only earlier companion qubits in the same cell. No range checks. |
| 134 | `endpoint(self, cell: int, direction: int, odd: bool) -> Pauli` | `Pauli` | Product `matter_gamma(cell, direction, odd) @ companion_eta(cell, direction)`. Thus the same numeric direction selects one of six matter modes and one of six companion-port Majoranas. |
| 139 | `physical_terms(self, edge: int) -> tuple[Pauli, ...]` | Four `Pauli` rows | For the selected edge: `(Z_left_mode, Z_right_mode, phase-2 * endpoint(left,local,even) * endpoint(right,local,odd), endpoint(left,local,odd) * endpoint(right,local,even))`. Edge order is inherited. |
| 151 | `target_terms(self, edge: int) -> tuple[Pauli, ...]` | Dependency-defined tuple of logical `Pauli` rows, expected to have four entries | Extracts `(owner, axis)` from the edge, makes a minimal object with `.cells`, and calls `C.R.expected_logical_terms(shell, owner, axis)`. |

There is **no M-owned cell enumeration algorithm**. `build` delegates enumeration
and neighbor/edge orientation entirely to `C.CellEdgeGauge.build`; this file alone
does not specify lexicographic order, boundary conditions, or axis conventions
beyond the six-field edge record above.

There is also **no box-union API**, no union construction, no site-map constructor,
and no shared-cell merge/deduplication handling in M. A caller needing overlapping
boxes cannot infer a canonical shared-cell policy from this module.

### Geometry-adjacent module functions

| Line | Exact signature | Return | Computation |
|---:|---|---|---|
| 280 | `qubit_cell(fixture: CompanionFixture, qubit: int) -> int` | `int` cell index | Matter qubits map by `qubit//6`; companion qubits map by `(qubit-matter_qubits)//3`. It does not bounds-check and is the only site/register-to-cell map. |
| 286 | `locality_certificate(fixture: CompanionFixture, relations: tuple[Pauli, ...]) -> dict[str, object]` | Certificate dictionary | Maps each supported qubit through `qubit_cell`, measures support-cell diameter with Manhattan distance, and ranks relation rows of diameter at most 0, 1, and 2. Keys: `relation_rank`, `radius_0_relation_rank`, `radius_1_relation_rank`, `radius_2_relation_rank`, `maximum_displayed_relation_weight`, `maximum_displayed_relation_diameter`, and `relations_outside_radius_2`. Empty supports have diameter 0. |
| 370 | `local_centralizer_basis(fixture: CompanionFixture, physical_generators: tuple[Pauli, ...], radius: int) -> tuple[int, ...]` | Independent tuple of binary symplectic row integers | For every cell center, forms the Manhattan-radius ball, solves for all local Paulis commuting with every physical generator, embeds them in the global `x | (z << qubits)` layout, and greedily retains an independent global span. |
| 438 | `local_centralizer_gauge_certificate(fixture: CompanionFixture, physical_generators: tuple[Pauli, ...], relation_rows: tuple[Pauli, ...]) -> dict[str, object]` | Nested certificate dictionary | Repeats local-centralizer construction for radii 0, 1, 2, computes an independent-basis symplectic Gram rank, `gauge_pairs = Gram_rank//2`, `gauge_center_rank = basis_rank-Gram_rank`, and `subsystem_logical_qubits = qubits-center_rank-gauge_pairs`. Each `radius_R` map contains `displayed_local_centralizer_rows`, `local_centralizer_span_rank`, `symplectic_Gram_rank`, `gauge_pairs`, `gauge_center_rank`, `subsystem_logical_qubits`, `target_matter_logical_qubits`, `centralizer_replay_failures`, and `target_relation_rows_outside_local_gauge_span`; top-level extras are `radius_2_generator_maximum_diameter` (hard-coded `2`) and `radius_2_generator_count`. It does not return the radius-two rows. |

## 2. Module M — companion representation and Pauli-row algebra

### Register and mode layout

For `N = len(fixture.cells)`, the represented physical register is ordered as:

1. Matter first: qubits `0 .. matter_qubits-1`, with cell `c` occupying
   `6*c .. 6*c+5`.
2. Companion second: three qubits per cell, with `(cell c, local companion
   qubit j)` at `matter_qubits + 3*c + j`.

There are six numeric matter modes/ports per cell (`0..5`), but this module
provides no symbolic labels such as `±x, ±y, ±z`. Port `d` selects companion
qubit `d//2` and its even/odd Majorana `d&1`. There are no coframe-bit fields,
coframe-origin labels, M2 coordinates, rail names, or separate register objects.
The integer qubit layout above is the complete M-owned “register indexing” API.

### Pauli representation and sign convention

The `Pauli` implementation is imported, so its class declaration is outside the
allowed source scope. Its use in M and F fixes the following interface:

- `Pauli(phase=0, x=0, z=0)` (also positional construction) stores integer
  bitmasks `x` and `z`; qubit `q` is bit `1 << q`.
- `phase` is manipulated modulo 4 as the exponent of the Pauli phase. The
  formulas are consistent with rows represented as `i^phase X^x Z^z`;
  in particular `phase=(x&z).bit_count() mod 2` makes a canonical Hermitian row.
- `left @ right` is signed Pauli multiplication. `Pauli()` is identity.
- `row.symplectic(qubits)` returns the packed phase-free integer
  `x | (z << qubits)`. Phase is deliberately absent from that vector.
- Public fields used by these modules are `.phase`, `.x`, and `.z`.

M’s own phase-free helper `symplectic` (line 363) confirms the packed order and
returns the commutation bit. Signed equality and multiplication details beyond
the usages above remain owned by the imported `C.Pauli`.

### Generator dictionary

`operator_rows` (line 157), exact signature
`operator_rows(fixture: CompanionFixture)` (no return annotation), returns
`tuple[tuple[str, Pauli, Pauli], ...]`. Each entry is
`(family, physical_row, target_row)`, in this fixed order:

1. For every edge in inherited edge order, four `"seam"` rows, zipping
   `physical_terms(edge)` with `target_terms(edge)`.
2. For matter-mode indices `0 .. matter_qubits-1`, one `"onsite_B"` row
   `(Z_mode, Z_mode)`.
3. For each cell in cell-index order and each
   `combinations(range(6), 2)` pair `(left_local,right_local)`, two
   `"onsite_even"` rows. With global endpoint bits `e_l,e_r` and the strict
   between-string `b`, these are
   `Pauli(phase=2,x=e_l|e_r,z=b|e_l|e_r)` and
   `Pauli(x=e_l|e_r,z=b)`, each identical to its target.

The result has `4*len(edges) + matter_qubits + 30*len(cells)` entries.
It is the only complete local-operator encoding dictionary exposed by M.

### Algebra, parity, center, and gauge helpers

| Line | Exact signature | Return | Computation/conventions |
|---:|---|---|---|
| 66 | `product(rows) -> Pauli` | One `Pauli` | Left-folds an iterable with signed `@`, starting at identity. Empty input returns identity. |
| 73 | `kernel_relations(vectors: tuple[int, ...]) -> tuple[int, ...]` | Tuple of integer coefficient masks | Incremental GF(2) elimination using each row’s highest set bit. Every returned mask selects an input subset whose XOR is zero. This is an insertion-order-dependent kernel generating set, not a canonical RREF. |
| 190 | `relation_certificate(fixture: CompanionFixture) -> dict[str, object]` | Certificate dictionary, including actual relation rows | Builds `operator_rows`, compares physical and target commutator Grams, computes target-kernel words, and orients each corresponding physical relation so the target signed relation is enforced in its `+1` sector. Keys are `generator_rows`, `physical_rank`, `target_even_rank`, `expected_target_even_rank`, `physical_minus_target_rank`, `commutator_Gram_failures`, `non_Hermitian_physical_generators`, `target_kernel_generators`, `relation_stabilizer_rank`, `relation_centralizer_failures`, `relation_mutual_commutator_failures`, `relation_phase_contradictions`, `target_relation_phase_parity_failures`, and `relation_rows: tuple[Pauli,...]`. |
| 326 | `cell_parity_constraints(fixture: CompanionFixture) -> tuple[Pauli, ...]` | One `Z`-only `Pauli` per cell | For each cell, returns `Z` on all six matter qubits and all three companion qubits. These are proposed local constraints; the function does not project a state or assign eigenvalues. |
| 338 | `homogeneous_nullspace(equations: tuple[int, ...], variables: int) -> tuple[int, ...]` | Tuple of integer solution masks | GF(2) homogeneous nullspace basis for equations encoded as coefficient masks over `variables` bits. Uses highest-bit pivots, emits free-variable solutions in increasing bit order, and asserts replay. |
| 363 | `symplectic(left: int, right: int, qubits: int) -> int` | `0` or `1` | Splits each packed row as low-`qubits` X bits and high Z bits and computes `(lx·rz + lz·rx) mod 2`. |
| 415 | `span_failures(targets: tuple[int, ...], generators: tuple[int, ...]) -> int` | `int` | Counts target rows not in the GF(2) span of generators. Multiplicity counts: every failing target adds one. |
| 530 | `fixture_certificate(shape: tuple[int, int, int]) -> dict[str, object]` | Aggregate dictionary | Builds a fixture and composes relation, locality, cell-parity, and local-gauge certificates. It removes `relation_rows` from the nested relation map before returning. Keys: `shape`, `cells`, `matter_qubits`, `companion_qubits`, `physical_qubits`, `constant_overhead_qubits_per_cell`, `relation_algebra`, `relation_locality`, `cell_parity_constraint_rank`, `cell_parity_constraint_centralizer_failures`, `cell_plus_relation_rank`, `required_stabilizer_rank_for_6N_code`, `code_exponent_if_all_commuting_constraints_imposed`, and `local_centralizer_subsystem_gauge`. |
| 573 | `main() -> None` | Normally `None`; may raise `SystemExit(1)` | Audit CLI over shapes `(2,2,2)`, `(3,2,2)`, `(3,3,2)`, `(5,3,2)`. Prints checks, one `SUMMARY_JSON`, and a verdict. It is not a reusable geometry constructor. |

M does **not** expose a decoder from a Pauli row to logical/gauge/center
coordinates. It exposes relation and cell-parity rows plus gauge rank
certificates; the only actual gauge-basis-returning function is
`local_centralizer_basis`, whose output is a phase-free integer basis and is
not symplectically split into gauge pairs versus center rows.

## 3. Module M — routing and counting

No routing API is present. M defines no nearest-neighbor route constructor,
route/schedule class, route return format, graph-distance path, FSWAP expansion,
or primitive counter.

The only distance convention is the Manhattan **support-cell diameter** used by
`locality_certificate`, `local_centralizer_basis`, and
`local_centralizer_gauge_certificate`. It is not a routed path length.
Consequently M has no distinction or conversion among semantic factors,
physical factors, physical primitives, and routed NN primitives. The only
generator count exposed is the row count described under `operator_rows`;
certificate fields named “generator” count algebra rows, not gates.

## 4. Module M — covariance

No covariance implementation is present. In particular M has no 24-frame
enumeration, no 576 frame-pair/product enumeration, no coframe-origin sectors,
and no row/word/schedule transport function. The module imports the bounded
Clifford-orbit dependency as `O` at line 59 but never reads `O` afterward.
That unused import must not be mistaken for a covariance re-export.

## 5. Module F — exact mixed-gauge factorization

Source:
`scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py`.

### Module constants and alias

| Line | Exact name | Type/value and role |
|---:|---|---|
| 18 | `AUDIT_TIMEOUT_SEC` | `int = 900`; metadata only. |
| 19 | `NOTE_PATH` | `str`; theorem-note path, not opened here. |
| 20 | `AUDIT_INPUT_PATHS` | `tuple[str, ...]`; provenance paths, ending at line 58. |
| 59 | `DECLARED_INPUT_PATHS` | Exact object alias of `AUDIT_INPUT_PATHS`. |
| 71 | `Pauli` | Type/class alias `M.Pauli`. |

### Public factorization helpers

| Line | Exact signature | Return | Computation/conventions |
|---:|---|---|---|
| 74 | `canonical_pauli(vector: int, qubits: int) -> Pauli` | Hermitian `Pauli` | Decodes `vector` as `x = low qubits`, `z = remaining high bits`; sets phase to `(x&z).bit_count()&1`. It does not truncate high Z bits beyond the right shift. |
| 80 | `independent_paired_basis(physical: tuple[int, ...], target: tuple[int, ...]) -> tuple[tuple[int, int, int], ...]` | Tuples `(independent_physical_row, corresponding_target_row, source_combination_mask)` | Highest-pivot GF(2) elimination of `physical`. When a physical combination becomes a new pivot, the same coefficient mask is XORed over `target` via `U.xor_rows`. Input order selects the basis. |
| 106 | `symplectic_split_paired(rows: tuple[tuple[int, int, int], ...], qubits: int) -> tuple[tuple[tuple[int, int, int], ...], tuple[tuple[tuple[int, int, int], tuple[int, int, int]], ...]]` | `(radicals, hyperbolic_pairs)` | Symplectic Gram–Schmidt driven by the physical component `[0]`; every XOR row operation is simultaneously applied to physical row, target row, and source-combination mask. It pops from the end, chooses the first remaining anticommuting partner, and is ordering-dependent. |
| 135 | `symplectic_split_vectors(rows: tuple[int, ...], qubits: int) -> tuple[tuple[int, ...], tuple[tuple[int, int], ...]]` | `(radical_rows, hyperbolic_pairs)` | Same end-pop/first-partner symplectic split for packed integer rows. |
| 163 | `local_center_basis(fixture: M.CompanionFixture, gauge: tuple[int, ...], radius: int) -> tuple[int, ...]` | Independent tuple of packed integer rows | Finds combinations in the symplectic radical of `gauge` whose physical support lies inside at least one Manhattan-radius cell ball. It accumulates displayed rows over all centers, then greedily retains an independent basis in discovery order. |
| 213 | `row_diameter(fixture: M.CompanionFixture, row: Pauli) -> int` | `int` | Manhattan diameter of the set of cells touched by `row.x | row.z`, using `M.qubit_cell`; empty support returns 0. |
| 227 | `span_equal(left: tuple[int, ...], right: tuple[int, ...]) -> bool` | `bool` | True iff ranks agree and each tuple lies in the other’s GF(2) span. |
| 235 | `conjugate_diagonal(row: Pauli, diagonal_rows: tuple[int, ...], z_signs: int, matter: int) -> Pauli` | New `Pauli` | Applies an encoded diagonal Clifford description to `row`: a set bit of `z_signs` on an X-supported matter index adds phase 2; a set bit `right` in `diagonal_rows[left]` applies the corresponding pairwise diagonal/CZ update to phase and Z mask. Only pairs `right < left < matter` are inspected. |

### `phase_fixed_factorization`

Line 252 exact signature:

`phase_fixed_factorization(shape: tuple[int, int, int]) -> dict[str, object]`

This is F’s sole high-level factorization entry point. It performs the following
construction:

1. Builds `M.CompanionFixture` and M’s complete physical/target dictionary.
2. Selects a paired basis and splits it into algebra radicals/logical hyperbolic pairs.
3. Gets the commutant/gauge basis from `U.gauge_structure(fixture, physical_paulis, relation_rows)` and splits it into center radicals/gauge pairs.
4. Generates center candidates at radii 0–2, greedily complements parity with radius-two rows, truncates to `len(gauge_radicals)-1`, and appends parity last.
5. Constructs `physical_w = [logical W][gauge W][local-center W][parity W]` and explicit `physical_v = [logical V][gauge V]`; `B.complete_tableau` adds center-dual V rows. The target frame is `[logical W][matter-parity W]` plus explicit logical V.
6. `B.decode` supplies `.phase`, `.v_mask`, `.w_mask`: low logical bits, then gauge bits, then center W bits, with parity the last center W bit.
7. Solves GF(2) sign flips for logical V, logical W, and non-parity center W (never gauge/parity rows), re-decodes, and checks both parity sectors.
8. Audits the failed product-encoder diagonal from `H.holonomy_certificate` against the gauge span.

The dimensions reported are:

- `logical_count = len(logical_pairs)`, interpreted as logical qubits in one
  fixed total-parity sector;
- `gauge_count = len(gauge_pairs)`;
- `center_count = len(local_center) + 1`, with total parity last;
- the constructed canonical frame is required to satisfy
  `logical_count + gauge_count + center_count == fixture.qubits`.

### Exact channel statement and representation of \(V_s\)

The exact formula returned at lines 561–564 is:

\[
E_s(\rho)=V_s\left[
\rho_{\mathrm{logical}}\otimes\frac{I_{\mathrm{gauge}}}{2^g}
\otimes
\lvert\mathrm{local\text{-}center}=+;\mathrm{parity}=s\rangle
\langle\mathrm{local\text{-}center}=+;\mathrm{parity}=s\rvert
\right]V_s^\dagger .
\]

The literal returned string is
`"E_s(rho)=V_s [rho_logical tensor I_gauge/2^g tensor
|local-center=+; parity=s><...|] V_s^dagger"`.

`V_s` is represented **only transiently and implicitly** by the signed canonical
Pauli tableau `(physical_w, physical_v)` aligned to the target tableau. There is
no `V_s` variable, class, matrix, circuit, or Clifford word, and the sector
value `s` is not an argument to `phase_fixed_factorization`; it enters only as
the eigenvalue of the final parity-center coordinate when phases are checked.
The same canonical tableau underlies both sectors.

Internally, the encoded logical generators are exactly
`physical_w[:logical_count]` and `physical_v[:logical_count]`. Gauge generators
are the next `gauge_count` W/V rows; center stabilizers are the remaining W
rows; center-coordinate duals are the remaining V rows. **None of these rows
or decoded coordinate records is returned.** The report provides only metrics
and a SHA-256 digest of all canonical rows. Thus F currently has no public
function that returns:

- the tableau or a matrix/word implementing \(V_s\);
- the encoded logical generators at a requested cell/port;
- logical, gauge, or center coordinates of a supplied Pauli;
- the encoding of an arbitrary local operator.

For the finite dictionary, `M.operator_rows` returns each local physical encoding
next to its target operator; F verifies its coordinates internally but discards
those decoded coordinates.

### Exact return schema

`phase_fixed_factorization` returns this nested report:

- Top: `shape`, `cells`, `physical_qubits`, `logical_qubits_in_fixed_parity_sector`, `gauge_qubits`, `center_sector_bits`, `dimension_identity`, `mutual_commutant`, `phase_fixed_intertwiner`, `product_phase_residual_vs_gauge`, `locality`, `deletion`, `tableau_digest`.
- `mutual_commutant`: `physical_algebra_rank`, `gauge_algebra_rank`, `rank_sum`, `expected_full_symplectic_dimension`, `cross_commutator_failures`, `physical_center_equals_declared_center`, `gauge_center_equals_declared_center`.
- `phase_fixed_intertwiner`: `logical_coordinate_failures`, `gauge_coordinate_failures_for_every_physical_generator`, `parity_coordinate_failures`, `phase_equation_rank`, `phase_equation_variables`, `phase_parity_failures`, `phase_contradictions`, `even_sector_phase_failures`, `odd_sector_phase_failures`, `phase_sign_weight`, `relation_center_coordinate_rank`, `canonical_tableau_rank`, `canonical_tableau_pairing_failures`, `finite_box_mixed_gauge_CPTP_E_constructed`, `factorwise_full_word_intertwiner_exact`, `channel_formula`, `gauge_channel_under_every_factor` (`"identity"`).
- `product_phase_residual_vs_gauge`: `changed_physical_generators`, `changed_generator_differences_outside_R1_gauge_span`, `difference_span_rank`, `verdict`.
- `locality`: `maximum_canonical_encoder_row_diameter`, `maximum_logical_coordinate_row_diameter`, `maximum_gauge_Bell_coordinate_row_diameter`, `maximum_center_dual_row_diameter`, `maximum_canonical_encoder_row_weight`, `locally_generated_center_ranks` (keys `"0"`, `"1"`, `"2"`), `full_center_rank`, `local_R2_center_rank_plus_supplied_parity`, `canonical_tableau_bounded_R2`.
- `deletion`: `remove_one_local_center_row_rank_loss` tests `center_vectors[1:]`; `remove_parity_row_rank_loss` tests `center_vectors[:-1]`.
- `tableau_digest`: SHA-256 of ordered `"phase:xhex:zhex"` rows joined by `|`; not reconstructive.

`main` (line 592), exact signature `main() -> None`, runs factorization on four
required shapes and three smaller patches, prints audit checks, a
`SUMMARY_JSON`, and a verdict, and may raise `SystemExit(1)`. It returns no
factorization object.

## 6. Module F — sector matrices

F contains no NumPy import and no exact two-mode or three-mode matrix builder.
It constructs and checks only packed Pauli rows, GF(2) tableaus, coordinate
masks, integer ranks, and phase residuals. Neither sector density matrices nor
machine-residual matrices are returned. `canonical_pauli` and
`conjugate_diagonal` are row builders/transformers, not small-matrix APIs.

## 7. Fixtures and factor entry points

There are no named coin, contact, mass, or FSWAP fixture classes/functions in
either module, and neither module deliberately re-exports such entry points.
The available pieces are:

| Family | Entry point | What is actually exposed |
|---|---|---|
| Generic box | `M.CompanionFixture.build` (line 101) | One companion fixture for one shape. |
| Seam | `CompanionFixture.physical_terms` (line 139), `target_terms` (line 151), or `M.operator_rows` (line 157) | Four physical/target Pauli rows per inherited edge. |
| Onsite number/mass-like row | `M.operator_rows` (line 157) | Family label `"onsite_B"` with one `Z` row per matter mode. There is no parameterized mass coefficient or update schedule. |
| Onsite even/coin/contact algebra | `M.operator_rows` (line 157) | A complete set of pairwise within-cell even Majorana rows under family label `"onsite_even"`. It does not distinguish coin from contact or build their linear combinations/exponentials. |
| Geometry audit fixture | `M.fixture_certificate` (line 530) | Rank/locality report; actual relation rows are removed from this aggregate return. |
| Factorization audit fixture | `F.phase_fixed_factorization` (line 252) | Factorization certificate and tableau digest, not the factorization tableau. |
| FSWAP | None | No FSWAP generator, word, schedule, route, matrix, or fixture. |

F calls `H.holonomy_certificate` internally to audit a failed product-state
diagonal, but does not alias or return that fixture. F’s
`"factorwise_full_word_intertwiner_exact"` field is a Boolean over M’s generator
dictionary, not a returned free/seam/contact word.

The only intentional type re-export is `Pauli`: `M.Pauli = C.Pauli` and
`F.Pauli = M.Pauli`.

## 8. Coupling traps and call ordering

### Dependencies and leaked namespace

Neither module defines `__all__`. Ordinary Python lookup therefore also exposes import bindings:

- M lines 53–59: `dataclass`, `sha256`, `combinations`, `json`, `C`, and `O`.
- F lines 61–68: `sha256`, `json`, `M`, `U`, `C`, `H`, and `B`.

These have no signatures specified here and are not stable re-exports. `M.O` is unused. F is coupled to `U.xor_rows`, `U.gauge_structure`, `C.R.F.base.gf2_rank`, `C.gf2_solve`, `H.holonomy_certificate`, `B.complete_tableau`, and `B.decode`.

### Global state and memoization

There is no mutable computational global, singleton fixture, cache, memoization, random source, or environment lookup. Every high-level call rebuilds its data. Importing either module still imports its dependencies, so their import-path setup and side effects remain external coupling.

### Ordering and representation assumptions

- Cell/edge order, ownership, axis/boundary conventions, and six-port geometry come entirely from `C.CellEdgeGauge.build`; M does not validate them.
- Registers are hard-coded as six contiguous matter bits/cell followed by three contiguous companion bits/cell. Edge endpoint modes serve as both global bits and local directions via `% 6`.
- Jordan–Wigner prefixes are cell-local. Reordering cells, matter modes, companions, or even/odd companion Majoranas changes signed rows.
- Packed rows need the exact width: X occupies the low `qubits` bits and Z the next block. Matter-width rows cannot be decoded at physical width.
- Bases are order-dependent: highest-bit pivots in M, end-pop/first-partner splitting in F, then dependency-owned tableau completion. Digests and logical bases are convention-dependent.
- F assumes physical/target tuples are positionally aligned and does not check equal lengths.
- The phase solve uses `delta//2`; require zero `phase_parity_failures` and `phase_contradictions` plus passing Boolean fields.
- Center choice is greedy/noncanonical; parity is appended last and all later mask slicing assumes that position.
- Local-center `+1` and maximally mixed gauge are supplied sector/state conventions, not prepared outcomes.
- Locality is support diameter, not an NN-circuit certificate; the canonical tableau may exceed radius two.
- No charts/coframes exist; chart origins, frame/coframe bits, and transformed-port conventions must be external.

### Required call sequence

There is no hidden initialization call. Low-level data flow is:

1. `fixture = M.CompanionFixture.build(shape)`.
2. `rows = M.operator_rows(fixture)`.
3. For relations, use `M.relation_certificate(fixture)["relation_rows"]`, not `M.fixture_certificate`, which removes them.
4. For an M-owned local commutant, use `M.local_centralizer_basis(fixture, tuple(r[1] for r in rows), radius)`.
5. Split a supplied packed basis with `F.symplectic_split_vectors(basis, fixture.qubits)`.

`F.phase_fixed_factorization(shape)` needs no prior call but returns no intermediate object. Either `main()` is an audit CLI, never a prerequisite.

## 9. REUSE PLAN for three Cycle-721 runners

### Shared API map

| Needed capability | Existing call(s) | Sufficiency |
|---|---|---|
| (a) Site map and registers | `M.CompanionFixture.build(shape)` gives `cells`, `edges`, `matter_qubits`, `qubits`; `M.qubit_cell(fixture,q)` gives inverse qubit-to-cell mapping; direct formulas above give per-cell registers. | Sufficient for one inherited finite box. Not sufficient for box unions, shared cells, named M2 rails, or coframe bits. |
| (b) Pauli-row algebra | `M.Pauli`, `M.product`, `M.symplectic`, `M.kernel_relations`, `M.homogeneous_nullspace`, `M.span_failures`; `F.canonical_pauli`, `F.independent_paired_basis`, and both `F.symplectic_split_*` helpers. | Sufficient for packed GF(2) row manipulation if the caller preserves qubit width, order, and signed `Pauli` rows separately. |
| (c) Encoded generators at one port cell | `fixture.matter_gamma`, `fixture.companion_eta`, and `fixture.endpoint` give local Majorana/endpoint rows; `fixture.physical_terms(edge)` and `M.operator_rows` give dictionary encodings. | Sufficient only for M’s local physical dictionary. The canonical \(V_s\)-encoded logical W/V generators are internal to F and unavailable by public return. |
| (d) Covariance transport of new schedule objects | None. | Missing: no frame enumeration, row transport, word transport, schedule schema, or schedule transport. |

### Runner 1: input-side Bell measurement compilation

Use `M.CompanionFixture.build` for the box and qubit registers, then
`M.operator_rows` plus `M.relation_certificate(...)[ "relation_rows" ]` for the
represented algebra and relation center. If the compiler needs an M-owned
radius-one commutant, obtain it with `M.local_centralizer_basis` and split it
with `F.symplectic_split_vectors`; verify the resulting center independently
with `F.local_center_basis`.

This supports specifying which packed gauge-pair rows a Bell measurement should
measure, but neither module supplies measurement operations, ancilla registers,
outcome-bit conventions, feed-forward corrections, or an NN schedule. The new
runner must define those objects and must not call a phase-free packed row a
signed measurement operator without converting it through
`F.canonical_pauli`.

### Runner 2: encoded-input Clifford via \(V_s\) restriction

Use M’s local endpoint/dictionary rows for the physical observable side and
F’s `phase_fixed_factorization(shape)` as a pass/fail regression certificate.
The requested \(V_s\) restriction itself cannot be implemented from that
report: `physical_w`, `physical_v`, target tableaus, decoded masks, and phase
solution are discarded.

The Cycle-721 spec therefore needs a narrow new F API (or an intentional
refactor of `phase_fixed_factorization`) returning a structured immutable
factorization object containing at least:

- ordered signed `physical_w` and `physical_v`;
- ordered signed target W/V rows;
- `logical_count`, `gauge_count`, `center_count`, with parity-last convention;
- per-dictionary-row decoded logical/gauge/center masks and sector phase;
- the selected local-center rows and total-parity row.

Without that extension, copying lines 252–504 of F or reaching through leaked
`F.B/F.U` dependencies would duplicate convention-sensitive logic and is not
reuse of the public factorization result.

### Runner 3: epoch composition

Use `M.operator_rows` as the stable factor dictionary and
`F.phase_fixed_factorization` to assert factorwise logical/identity-gauge
intertwining for each box. Define epoch words/schedules in the new runner with
explicit counts for semantic factors, unrouted physical primitives, and routed
NN primitives; neither M nor F currently supplies these notions.

Covariant epoch composition also requires a new transport layer. It must define
the 24 frame elements, all 576 ordered frame products if those are required,
coframe-origin/sector bits, transformations of signed Pauli rows, and
transformations of the newly defined word and schedule objects. There is no
existing M/F call for this; the unused `M.O` binding is not an implementation.
Tests should transport both row support and phase, preserve the parity-last
center convention, and compare factor counts separately from route-expanded
primitive counts.

## COMPLETENESS

All locally defined non-underscore module constants/type aliases, the one class
and all of its methods, and every module-level function in the two requested
files are documented above with definition line and exact signature. The
inventory covers M lines 14–573 and F lines 18–592; the later nested `check`
functions are local closures inside `main`, not module APIs. Imported names
visible because neither module defines `__all__` are explicitly inventoried as
coupling rather than misrepresented as locally specified APIs.

Requested-but-absent surfaces are called out explicitly: union boxes/shared-cell
handling, M2/coframe labels, routing and count layers, covariance/frame
transport, returned \(V_s\)/encoded logical generators/coordinate decoders,
small sector matrices, and named coin/contact/mass/FSWAP fixtures. The reuse
plan distinguishes the exact existing calls from the APIs Cycle-721 must add.
