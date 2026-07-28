# CSLT route surfaces — Cycle 725 grounding

Static extraction from only the four requested Python files. “Public” below means a
module-defined name without a leading underscore; imported names are not re-inventoried.
No runner was executed. Line numbers are 1-based in the named source file.

## 1. `scripts/signed_gravity_oriented_tensor_source_lift.py`

### Public constants, types, and data containers

- `ROOT` (line 39): repository-root `str`, derived from `__file__`; also inserted into
  `sys.path` at line 40.
- `TOL` (line 53): `float = 1.0e-10`.
- `PASS_COUNT`, `FAIL_COUNT` (lines 54-55): mutable integer harness counters, initially
  zero.
- `Projectors` (lines 70-84): frozen dataclass with `lapse`, `shift`, `trace`, and
  `shear`, each annotated `np.ndarray`. `Projectors.blocks` (lines 77-84) is a property
  returning `dict[str, np.ndarray]` with those four named matrices.

### Every public function: signature and return shape

- `check(name: str, passed: bool, detail: str = "") -> bool` (lines 58-67): increments
  the counters, prints one status row, and returns `passed`.
- `canonical_projectors() -> Projectors` (lines 87-98): four real `10 x 10`
  projectors, with ranks `1, 3, 1, 5`.
- `block_norms(vec: np.ndarray, projectors: Projectors) -> dict[str, float]`
  (lines 101-102): four Euclidean projected norms.
- `universal_block_operator(a: float = 1.7, b: float = 2.3) -> np.ndarray`
  (lines 105-112): real `10 x 10` block-diagonal matrix.
- `nullspace(mat: np.ndarray, tol: float = 1.0e-12) -> np.ndarray` (lines 115-118):
  for an `m x n` matrix, an `n x (n-rank)` right-nullspace basis.
- `tensor_source_with_constraints() -> tuple[np.ndarray, np.ndarray]`
  (lines 121-141): `(source, constraint)` of shapes `(10,)` and `(4, 10)`.
- `oriented(source: np.ndarray, eta: int) -> np.ndarray` (lines 144-145): the same
  shape as `source`, multiplied by imported `sign_eta(eta)`.
- `scalar_a1_source() -> np.ndarray` (lines 148-152): real shape `(10,)`, with only
  entries 0 and 4 nonzero (`2.0` and `1.0`).
- `projector_algebra_check(projectors: Projectors) -> tuple[bool, str]`
  (lines 155-166).
- `orientation_twist_check(source: np.ndarray, projectors: Projectors) -> tuple[bool, str]`
  (lines 169-179).
- `ward_constraint_check(source: np.ndarray, constraint: np.ndarray) -> tuple[bool, str]`
  (lines 182-187).
- `response_locking_check(source: np.ndarray) -> tuple[bool, str]` (lines 190-213).
- `scalar_only_no_overclaim_check(projectors: Projectors) -> tuple[bool, str]`
  (lines 216-221).
- `free_tensor_carrier_gate(source: np.ndarray) -> tuple[bool, str]` (lines 224-234).
- `no_claim_gate() -> tuple[bool, str]` (lines 237-245).
- `main() -> int` (lines 248-299): complete harness; returns `0` on no failed checks,
  otherwise `1`.

### Harness/check entry points and exact input contract

`main` is the executable harness (lines 248-303). It has **NO input port**. It constructs
`projectors = canonical_projectors()` and the seeded source/constraint fixture from
`tensor_source_with_constraints()` at lines 261-262, then calls every check at lines
264-283. A downstream census cannot enter `main` as an argument.

The individual checks do have the following numerical ports:

| Check | Object actually consumed | Can an external event/census stream enter lawfully? |
|---|---|---|
| `projector_algebra_check` | One `Projectors`; operations require four compatible `10 x 10` matrices whose sum is compared with `eye(10)`. | Not as a stream. A caller may supply a fully materialized `Projectors` object of exactly those shapes. |
| `orientation_twist_check` | `source`, effectively a real/complex length-10 vector, and `Projectors` with `10 x 10` blocks. It requires every projected block norm to exceed `0.05`; there is no unit-norm normalization. | Yes only after a newly supplied census-to-10-vector reduction. Raw events are not accepted. |
| `ward_constraint_check` | A length-10 `source` and a matrix whose last dimension is 10; the harness uses `(4,10)`. It checks `constraint @ oriented(source, eta)` for `eta in (+1,-1,0)`. No normalization is performed. | Yes only as the already-reduced vector and constraint matrix. A raw stream has no lawful port. |
| `response_locking_check` | A length-10 `source`; operator parameters are not arguments and remain the defaults `a=1.7`, `b=2.3`. No normalization is performed. | Yes only as a length-10 reduced source, not as events. |
| `scalar_only_no_overclaim_check` | Only `Projectors`; it always constructs its own fixed `scalar_a1_source()`. | **No source/event input port.** |
| `free_tensor_carrier_gate` | A length-10 `source`; it compares it with a hard-coded scalar `chi_only` vector and demands supplied-source shift/shear norms `>0.05`. | Yes only as a reduced length-10 tensor-source vector. |
| `no_claim_gate` | No arguments; a hard-coded all-`False` claims dictionary. | **No input port.** |

`tensor_source_with_constraints` is also wholly internal: RNG seed `20260426`, a random
`(4,10)` constraint, a nullspace draw, positive `source[0] > 0.5`, and all four block
norms `>0.05` (lines 128-141). Thus the reviewed harness result certifies this fixture,
not an arbitrary external source.

### What is certified, and boundaries

The file states the finite scope exactly (lines 20-26):

> 1. the orientation-line twist commutes with the canonical block projectors;  
> 2. it preserves linear Ward/conservation constraints;  
> 3. it flips every occupied tensor block source with the same chi_eta;  
> 4. the universal block-diagonal GR operator gives a locked tensor response;  
> 5. scalar-only sources remain A1-only, so no overclaim is introduced.

The scalar-only gate is literal: it projects the fixed scalar source onto
`projectors.shift + projectors.shear` and requires norm `< TOL` (lines 216-221).
The adjacent carrier gate says (line 225):

> The lift needs an ordinary tensor source; chi alone cannot create one.

The printed boundary is equally explicit (lines 255-258):

> T_g(Y) = chi_eta(Y) * T_plus  
> chi_eta signs the whole already-existing tensor source bundle; it does  
> not manufacture shift/shear components from a scalar source.

The module-level nonclaim is: “This is not a negative-mass, shielding, propulsion,
reactionless-force, or physical signed-gravity claim.” (lines 28-29). A clean harness
prints `FINAL_TAG: SIGNED_GRAVITY_ORIENTED_TENSOR_SOURCE_LIFT_FINITE_CONDITIONAL`
(line 296), not a physical prediction.

## 2. `scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py`

### Public constants and type aliases

- `ROOT` (line 24): repository `Path`; `NOTE` (lines 34-37): fixed Cycle-322 note path.
- `LEFT=(0,0,0)`, `RIGHT=(1,0,0)`, `ENDPOINTS=(LEFT,RIGHT)` (lines 38-40).
- `BETA=-0.3`, `ANGLE=carried.MEDIATOR_COUPLING * common_species(BETA).analytic_mass`
  (lines 41-42); `TOLERANCE=3e-10`, `SIZES=(3,4,6)`, `HELD_SIZE=6`
  (lines 43-45); `REVERSE=(1,0,3,2,5,4)` (line 46).
- `N1_ROUTES` (lines 48-57): eight route-label strings; `WALLS` (line 58): five
  wall labels; `TRIGGER_PARTS` (lines 59-71): eleven split-string scan triggers.
- `PASS`, `FAIL` (lines 73-74): mutable integer counters.
- `QKey = tuple`, `LogicalState = dict[QKey, np.ndarray]`,
  `PhysicalState = dict[QKey, np.ndarray]` (lines 76-78).
- `LOCAL_LABELS`, `LOCAL_MASKS`, `LOCAL_INDEX` (lines 242-244): imported-code labels,
  corresponding 64 masks, and mask-to-index map. `LABELS` (line 245): 4,096 joint
  labels. `JOINT_INDEX` (lines 246-249): local-index-pair to joint-index map.

### Every public function: signature and return shape

- `check(label: str, condition: bool, detail: object = "") -> None` (lines 81-88);
  `normalized(file_path: Path) -> str` (lines 91-95).
- `note_contract() -> None` (lines 98-140); `methodology_controls() -> None`
  (lines 143-239).
- `fermion_hop(mask: int, source: int, target: int) -> tuple[int, int] | None`
  (lines 252-258): `(new_mask, fermionic_sign)` or `None`.
- `local_source_blocks(angle: float)` (lines 261-299): five-tuple
  `(exchange, vertex, charge, number, momenta)`; the first four are complex/diagonal
  `448 x 448` arrays and `momenta` is a tuple of three `448 x 448` diagonal arrays.
- `local_fock_frame(frame: np.ndarray) -> np.ndarray` (lines 302-309): complex
  `64 x 64`; `local_source_frame(frame: np.ndarray) -> np.ndarray` (lines 312-316):
  complex `448 x 448`.
- `q_reservoir(endpoint: int) -> QKey` (lines 319-320): `("R", endpoint)`;
  `q_field(cell: tuple[int,int,int], direction: int) -> QKey` (lines 323-324):
  `("F", cell, direction)`.
- `prune(state: dict, threshold: float = 2e-13) -> dict` (lines 327-328);
  `state_norm(state: dict) -> float` (lines 331-332);
  `state_residual(left: dict, right: dict) -> float` (lines 335-347);
  `normalize_state(state: LogicalState) -> LogicalState` (lines 350-352).
- `apply_matter_factor(state: LogicalState, factor: sparse.spmatrix) -> LogicalState`
  (lines 355-356); `apply_field_coin(state: dict, *, inverse: bool = False) -> dict`
  (lines 359-372); `apply_field_stream(state: dict, length: int, *, inverse: bool = False) -> dict`
  (lines 375-391).
- `apply_source(state: LogicalState, endpoint: int, endpoint_cells=ENDPOINTS, *, angle: float = ANGLE, inverse: bool = False) -> LogicalState`
  (lines 394-433); `apply_two_sources(state: LogicalState, endpoint_cells=ENDPOINTS, *, angles=(ANGLE, ANGLE), enabled=(True, True), inverse: bool = False) -> LogicalState`
  (lines 436-455).
- `logical_step(state: LogicalState, length: int, factors, endpoint_cells=ENDPOINTS, *, angles=(ANGLE, ANGLE), enabled=(True, True), stream_enabled: bool = True) -> LogicalState`
  (lines 458-477); `logical_inverse(state: LogicalState, length: int, factors, endpoint_cells=ENDPOINTS) -> LogicalState`
  (lines 480-492).
- `symmetric_one_one_state() -> np.ndarray` (lines 495-504): normalized complex
  `(4096,)`; `random_logical_state(seed: int = 322) -> LogicalState` (lines 507-520):
  four Q keys, each mapped to a complex `(4096,)` vector, globally normalized.
- `local_operator_controls() -> None` (lines 523-576);
  `seam_number_contact_controls(factors) -> None` (lines 579-633).
- `build_encoding(length: int, reverse_order: bool = False)` (lines 636-644):
  sparse physical-row-by-4096 encoding; `encode_physical(state: LogicalState, encoding) -> PhysicalState`
  (lines 647-648), with each output value of length `encoding.shape[0]`.
- `apply_physical_matter_factor(state: PhysicalState, encoding, factor) -> PhysicalState`
  (lines 651-656); `apply_physical_source(state: PhysicalState, encoding, endpoint: int, endpoint_cells=ENDPOINTS, *, inverse: bool = False) -> PhysicalState`
  (lines 659-679).
- `physical_step(state: PhysicalState, encoding, length: int, factors, endpoint_cells=ENDPOINTS) -> PhysicalState`
  (lines 682-696); `physical_inverse(state: PhysicalState, encoding, length: int, factors, endpoint_cells=ENDPOINTS) -> PhysicalState`
  (lines 699-713).
- `physical_intertwiner_controls(factors)` (lines 716-768): returns
  `(forward_encoding, reverse_encoding, size_rows)`, two sparse matrices with 4,096
  columns plus a list of size-control dictionaries.
- `response_matrix(length: int, factors, *, angles=(ANGLE, ANGLE), enabled=(True, True), stream_enabled=True, endpoint_cells=ENDPOINTS) -> tuple[np.ndarray, float]`
  (lines 771-799): real `2 x 2` response matrix and maximum norm drift.
- `response_reciprocity_controls(factors)` (lines 802-851): implicit `None`;
  `emission_absorption_controls()` (lines 854-894): implicit `None`.
- `translate_q_state(state: LogicalState, displacement, length: int) -> LogicalState`
  (lines 897-908).
- `covariance_translation_support_controls(factors)` (lines 911-978),
  `deletion_mass_contact_domain_controls(factors)` (lines 981-1043), and
  `inventory_controls()` (lines 1046-1073): implicit `None`.
- `main() -> int` (lines 1076-1096): full harness, `0` for certified and `1` for open.

### Harness/check entry points and exact input contract

`main` is the harness. It has **NO event/source argument**. It reads/checks the fixed
`NOTE`; obtains `(coin, fswap, contact, ...)` from imported Cycle-315 code for fixed
`LABELS`; calls all controls; and uses module constants for angles, endpoints, sizes,
seeds, and prepared states (lines 1076-1090).

- `note_contract()`, `methodology_controls()`, `local_operator_controls()`,
  `emission_absorption_controls()`, and `inventory_controls()` have no parameters.
  The first two consume the hard-coded `NOTE` (and `methodology_controls` also reads
  hard-coded witness files and this script); the numerical controls construct their
  fixtures internally. **No external census stream can enter as an argument.**
- `seam_number_contact_controls`, `physical_intertwiner_controls`,
  `response_reciprocity_controls`, `covariance_translation_support_controls`, and
  `deletion_mass_contact_domain_controls` accept only `factors`, unpacked as
  `(coin, fswap, contact)` and expected to be compatible 4,096-dimensional operators.
  `main` supplies the imported Cycle-315 factors. An event stream is not a lawful
  `factors` value.
- `response_matrix` is parameterized over `length`, the operator tuple, two numeric
  angles, two booleans, one stream boolean, and two endpoint cells, but it always
  constructs `symmetric_one_one_state()` and the two reservoir-column preparations
  internally (lines 780-798). It is not a census-state port.
- Lower helpers `logical_step`/`physical_step` do accept typed states. A lawful
  `LogicalState` is a Q-keyed dictionary whose values are same-sized complex
  `(4096,)` vectors; a normalized state has total squared norm 1. A lawful
  `PhysicalState` has the same Q-key grammar and vectors of
  `encoding.shape[0]`. These helpers are not the reviewed check entry points.
  Feeding census-derived states through them would therefore be a new supplied test,
  not an invocation of the Cycle-322 certification surface.

### What is certified, OPEN/UNTESTED language, and boundaries

The control labels certify, for the internal fixtures: local proper-cubic unitary
Q/number/coefficient-two vector balance (lines 558-576); commuting endpoint sources,
number preservation, retained contact, and rejection of the naive one-one sector
(lines 610-633); physical/logical intertwining and isometry through held `L=6`
(lines 747-767); nonzero reciprocal two-update transfer and deletions (lines 818-851);
matched emission/absorption (lines 877-894); 24 frames, 27 translations, and bounded
support (lines 943-978); and mass/contact/domain firewalls (lines 1010-1043).

The interpretation boundary is verbatim:

> The result is a bounded common-code response/reciprocity proxy, not physical  
> energy, stress, gravity, metric, or time. (lines 7-8)

The exact unit-weight-lift strings present in this allowed file are:

- `"full-Fock Cycle-320 unit-weight auxiliary sources"` (`N1_ROUTES`, line 52).
- `"open": "global Q=2, Cycle320 unit-weight full-Fock lift, multi-edge recurrence, alternate mediator, energy/stress/metric"` (line 1056).

`methodology_controls` permits only the literal status values `"ATTEMPTED"`,
`"RULED OUT BY PRIOR RESULT"`, and `"OPEN / UNTESTED"` (lines 146-150), but obtains
the route-specific marker by regex from the hard-coded external `NOTE` (lines 153-161).
Therefore this file itself does **not** contain a route row assigning
`OPEN / UNTESTED`, nor the phrase “sharpest next test.” Within the four-file reading
boundary, the exact defensible “what it consists of” is only the combination of the
route label “full-Fock Cycle-320 unit-weight auxiliary sources” and the open inventory
label “Cycle320 unit-weight full-Fock lift.” Any fuller quoted row or priority claim
requires newly supplied out-of-scope note text.

## 3. `scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py`

### Public constants, types, and data containers

- `ROOT` (line 24), fixed `NOTE` (lines 37-40); `BETA=-0.3`, derived `ANGLE`
  (lines 41-42); `SIZES=(3,4,6)`, `HELD_SIZE=6`, `TOLERANCE=3e-10`
  (lines 43-45); `REVERSE=(1,0,3,2,5,4)` (line 46).
- `N1_ROUTES` (lines 48-57), `WALLS` (line 58), `TRIGGER_PARTS` (lines 59-71);
  `PASS`, `FAIL` mutable counters (lines 73-74).
- `Position = tuple[int,int,int]`, `PhysicalKey = tuple[int,int,int,int,int]`,
  `PhysicalState = dict[PhysicalKey, complex]` (lines 76-78).
- `LinkState` (lines 245-256): dataclass with
  `excited: dict[Position, np.ndarray]` (values are complex `(6,)`) and
  `pair: dict[tuple[Position,Position], np.ndarray]` (values are complex
  `(6,6,6)`). `copy(self) -> "LinkState"` (lines 252-256) deep-copies arrays.

### Every public function: signature and return shape

- `check(label: str, condition: bool, detail: object = "") -> None` (lines 81-88);
  `normalized(file_path: Path) -> str` (lines 91-95);
  `note_contract() -> None` (lines 98-139); `methodology_controls() -> None`
  (lines 142-238).
- `zero_tensor() -> np.ndarray` (lines 241-242): complex `(6,6,6)`.
- `state_norm(state: LinkState) -> float` (lines 259-263);
  `state_residual(left: LinkState, right: LinkState) -> float` (lines 266-278);
  `normalize_state(state: LinkState) -> LinkState` (lines 281-286);
  `wrap_state(state: LinkState, length: int) -> LinkState` (lines 289-297);
  `test_state(length: int) -> LinkState` (lines 300-313): seeded, normalized fixture.
- `link_recoil_vertex(angle: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, tuple[np.ndarray, ...]]`
  (lines 316-346): `(exchange, vertex, charge, momenta)` with three `222 x 222`
  arrays followed by a three-element tuple of `222 x 222` momentum arrays.
- `active_frame_222(frame: np.ndarray) -> np.ndarray` (lines 349-354):
  complex `222 x 222`; `vector_expectation(excited: np.ndarray, pair: np.ndarray) -> np.ndarray`
  (lines 357-366): real shape `(3,)`.
- `local_vertex(excited: np.ndarray, contact_pair: np.ndarray, angle: float) -> tuple[np.ndarray, np.ndarray]`
  (lines 369-375): complex shapes `(6,)` and `(6,6,6)`.
- `vertex_gate(state: LinkState, angle: float) -> tuple[LinkState, dict[str, object]]`
  (lines 378-406); report keys are `local_Q_residual`, `local_P_residual`, and
  `source_current`.
- `coin_gate(state: LinkState, matter_coin: np.ndarray, field_coin: np.ndarray) -> LinkState`
  (lines 409-420).
- `body_stream(state: LinkState) -> tuple[LinkState, dict[tuple[Position,int],float], dict[tuple[Position,int],float]]`
  (lines 423-448); `field_stream(state: LinkState) -> tuple[LinkState, dict[tuple[Position,int],float]]`
  (lines 451-466).
- `matter_density(state: LinkState) -> dict[Position,float]` (lines 469-475);
  `q_density(state: LinkState) -> dict[Position,float]` (lines 478-485).
- `logical_step(state: LinkState, model: c307.GlobalModel) -> tuple[LinkState, dict[str,float]]`
  (lines 488-511).
- `add_state_value(state: PhysicalState, key: PhysicalKey, value: complex) -> None`
  (lines 514-519); `physical_norm(state: PhysicalState) -> float` (lines 522-523);
  `physical_residual(left: PhysicalState, right: PhysicalState) -> float`
  (lines 526-534).
- `extended_column(model: c307.GlobalModel, matter_mode: int, *, excited: bool, field_mode: int = -1, auxiliary_direction: int = -1) -> PhysicalState`
  (lines 537-555); `encode_state(state: LinkState, model: c307.GlobalModel) -> PhysicalState`
  (lines 558-588).
- `inner_product(column: PhysicalState, state: PhysicalState) -> complex`
  (lines 591-592); `apply_lifted_block(state: PhysicalState, columns: tuple[PhysicalState,...], matrix: np.ndarray) -> PhysicalState`
  (lines 595-608).
- `lawful_code_leakage(state: PhysicalState, model: c307.GlobalModel) -> float`
  (lines 611-653); `active_field_auxiliary_labels(state: PhysicalState, modes: set[int], model: c307.GlobalModel) -> set[tuple[int,int]]`
  (lines 656-664).
- `apply_matter_block_family(state: PhysicalState, model: c307.GlobalModel, kind: str) -> PhysicalState`
  (lines 667-696); `apply_field_coin(state: PhysicalState, model: c307.GlobalModel) -> PhysicalState`
  (lines 699-713).
- `apply_source_block(state: PhysicalState, model: c307.GlobalModel, cell: Position) -> PhysicalState`
  (lines 716-735); `apply_source_vertices(state: PhysicalState, model: c307.GlobalModel) -> PhysicalState`
  (lines 738-742); `apply_field_stream(state: PhysicalState, model: c307.GlobalModel) -> PhysicalState`
  (lines 745-763); `physical_step(state: PhysicalState, model: c307.GlobalModel) -> PhysicalState`
  (lines 766-772).
- `local_route_controls() -> None` (lines 775-875);
  `recurrent_intertwiner_controls(models: dict[int,c307.GlobalModel]) -> None`
  (lines 878-916);
  `emission_transport_absorption_catchup(models: dict[int,c307.GlobalModel]) -> None`
  (lines 919-1032).
- `rotate_state(state: LinkState, frame: np.ndarray, length: int) -> LinkState`
  (lines 1035-1058); `translate_state(state: LinkState, displacement: Position, length: int) -> LinkState`
  (lines 1061-1076).
- `overlap_covariance_support_controls(models: dict[int,c307.GlobalModel]) -> None`
  (lines 1079-1164); `rest_mass_contact_deletion_controls(models: dict[int,c307.GlobalModel]) -> None`
  (lines 1167-1282); `inventory_controls() -> None` (lines 1285-1312).
- `main() -> int` (lines 1315-1332): `0` for factor-certified, `1` for open.

### Harness/check entry points and exact input contract

`main` has **NO source/event/census argument**. It reads/checks the fixed `NOTE`, builds
`models = {length: c307.build_model(length) for length in SIZES}`, and calls the seven
numerical/inventory/methodology controls (lines 1315-1326).

- `local_route_controls` uses only module/import constants and internally prepared
  `222`-basis columns. `inventory_controls` has a literal dictionary.
  `note_contract` and `methodology_controls` read fixed paths. These checks have
  **NO input port**.
- The remaining controls accept only `models: dict[int, c307.GlobalModel]`; the
  harness supplies keys `3,4,6`. They construct their own `test_state(length)`,
  uniform-at-origin state, source/absorption fixtures, covariance fixtures, rest
  columns, and deletion fixtures. A census stream cannot lawfully occupy the
  `models` argument.
- The lower computational functions do expose a true typed state port:
  `LinkState.excited[position]` must be a complex six-direction vector and
  `LinkState.pair[(body,field)]` a complex `6 x 6 x 6`
  matter/field/auxiliary tensor. `normalize_state` makes the sum of squared array
  norms equal 1. `PhysicalState` is a sparse dictionary from five integer labels
  `(row, matter_mode, source, field_mode, auxiliary_mode)` to complex amplitudes.
  These are helper contracts, not control/harness arguments. A raw epoch census is
  neither type and has no specified conversion or normalization rule.

### What is certified, OPEN/UNTESTED language, and boundaries

The controls certify only the constructed one-carrier route: exact unit-weight Q/P
operator balance with nonzero matter recoil and a direction-preserving no-recoil
comparator (lines 825-875); recurrent logical/physical intertwining through held
`L=6` (lines 902-916); emission, transport, conjugate absorption, and auxiliary
catch-up (lines 1007-1032); overlap, 24-frame/27-translation covariance, and constant
40-M2 support (lines 1137-1164); and rest/mass/contact/deletion firewalls
(lines 1199-1282).

The construction is stated exactly (lines 4-10):

> The retained route extends the Cycle-316 one-carrier physical code by six  
> auxiliary direction M2 per cell. Its source channels are  
> E_d <-> G_reverse(d),F_d,A_d. They conserve Q and the dimensionless  
> unit-weight vector P_matter + P_mediator + P_aux at operator level. The  
> auxiliary direction is transported with matter by the same bounded block  
> catch-up. No physical momentum, work, energy, stress, or gravity meaning is  
> assigned.

This is the exact available content for what a Cycle-320 unit-weight auxiliary
construction consists of. Its own open inventory is:

> `"open": "independent rest column, paired mediator, simultaneous carriers, contact, two sources, physical calibration"` (line 1295).

As in file 2, `"OPEN / UNTESTED"` is merely one allowed marker read from the external
`NOTE` (lines 145-161). No route-specific marker and no phrase “sharpest next test”
is hard-coded in this file. File 3 therefore supports the mechanics quoted above,
while the claimed prioritization/OPEN row would require new supplied note text outside
the permitted four-file extraction.

## 4. `scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py`

### Public constants and every public function

- `ROOT` (line 20): repository `Path`; `NOTE` (lines 21-25): fixed synthesis-note
  path.
- `ROUTES` (lines 27-47): three rows, each shaped
  `(route_name: str, script_path: Path, expected_pass: int, stdout_regex: Pattern)`.
- `PASS`, `FAIL` (lines 49-50): mutable integer counters.
- `check(label: str, condition: bool, detail: object = "") -> None` (lines 53-60).
- `normalized(path: Path) -> str` (lines 63-67).
- `note_contract() -> None` (lines 70-108).
- `cold_routes() -> None` (lines 111-138).
- `route_independence_controls() -> None` (lines 141-171).
- `selected_port_identity() -> None` (lines 174-198).
- `main() -> int` (lines 201-207): returns `int(FAIL != 0)`.

### Harness/check entry points and exact input contract

Every check entry point has **NO input port**:

- `note_contract` reads only the fixed `NOTE` and tests a hard-coded tuple of required
  normalized substrings.
- `cold_routes` uses the fixed `ROUTES`, launches each fixed runner, parses captured
  stdout, and compares fixed pass totals. It accepts no runner row or census object.
- `route_independence_controls` reads three fixed note paths and checks fixed
  substrings. It accepts no route record.
- `selected_port_identity` constructs `rho` internally for sides `(3,5,7,9)` as a
  unit impulse at `[0,0,0]` minus its mean; hence shape is `(side,side,side)`,
  `sum(rho)` is zero up to floating arithmetic, and no external `rho` is accepted.
- `main` simply calls the four routines. A downstream stream can only rerun the
  contract unchanged and bind its own records by a separate exact comparison.

`normalized(path)` is a parameterized text helper, not a bridge-data check. There is
no public function accepting a typed event, source record, route row, or census array.
The script names an “externally supplied additive” semantically but supplies no
argument through which such data can enter.

### What is certified and the “not one combined law” contract rows

The module boundary says (lines 4-7):

> Cold-run the three independent routes, verify their deliberately different  
> physical surfaces, and pin the synthesis/N1--N8 contract. This runner does  
> not splice routes, name occupation probability energy, or promote a selected  
> source-port residual to an autonomous-law obstruction.

`note_contract` requires all of these exact boundary strings (lines 75-84):

- `"axiomatic three-dimensional space is not physical time"`
- `"six hard-core mediator m2"`
- `"global-blockade comparison"`
- `"physical local deformation layer"`
- `"phase-robust positive number current"`
- `"not one combined law"`
- `"not physical energy"`
- `"selected additive port"`
- `"externally supplied additive"`
- `"not the autonomous hard-core vertex history"`

The executable independence row is exactly:

> `"the routes have no common code/update and do not silently form one law"` (line 158).

It checks route A for `"25 retained matter m2 plus 6 mediator m2"` and
`"cycle-251/272"`, route B for `"six additional field m2"` and `"cycle-269"`, and
route C for `"three-m2 onsite block"` and `"cycle-269"` (lines 159-164). The next
row separately requires route-specific energy boundaries (lines 166-170).

The selected-port check is only a conditional spectral comparator. Its source is
internally zero-mean, its selected port is `-L rho / 6`, and its response is checked
against `-rho/2` (lines 174-197). The comment closes the scope explicitly:

> this is not the autonomous vertex history. (line 178)

## Cycle-725 synthesis: literal epoch-census feed

| Route | What can literally be fed under these contracts? | Honest Cycle-725 disposition | New supplied data required |
|---|---|---|---|
| **S1 — tensor lift** | Individual file-1 checks can receive a reduced length-10 tensor-source `np.ndarray`; the Ward check additionally receives an `m x 10` constraint (the reviewed fixture is `4 x 10`), and projector checks receive four `10 x 10` matrices. No check accepts raw events. `main` accepts nothing. | A **true parameterized numerical feed** exists only after an external census-to-canonical-10-vector reduction. If Cycle 725 invokes `main`, it instead reduces to **rerun byte-pinned harness + separate exact census binding**. Scalar-only and nonclaim gates remain named no-input-port findings. | Required: epoch-record schema; deterministic record-to-10-component aggregation; units/weights; choice of real/complex dtype; normalization policy (none is imposed by the checks); Ward constraint matrix and provenance; and, if noncanonical, projector matrices. |
| **S2 — unit-weight** | File-3 control functions accept either no arguments or only a model dictionary; file-2 controls accept either no arguments or only the `(coin,fswap,contact)` operator tuple. Lower helpers accept `LinkState`/`PhysicalState`, but those states are not control inputs. | For the retained certification this is **rerun byte-pinned harness + separate exact census binding**. The honest named result is **NO INPUT PORT FOR AN EPOCH CENSUS**. Calling helpers on census-derived states would be a new Cycle-725 test, not the old certificate. | Required: census-to-`LinkState` mapping; position convention; six matter, six field, and six auxiliary direction indexing; complex amplitude/phase rule (counts alone do not supply amplitudes); global norm-one policy; model/volume selection; and a new check defining the comparison. A full-Fock Cycle-320 lift additionally needs the currently absent full-Fock auxiliary-source construction. |
| **S3 — typed bridge/tournament** | File 4 accepts no typed bridge row, source array, or event. Even `rho` is constructed internally at fixed odd sizes. The `ROUTES` rows are constants, not arguments. | **Rerun byte-pinned harness + separate exact census binding**, with the named finding **NO INPUT PORT / NOT ONE COMBINED LAW**. Treating census data as the selected additive would require a new surface and must not be called the autonomous vertex history. | Required: a typed route/event schema; route assignment rule; census-to-zero-mean `rho` transform; lattice side and cell mapping; additive normalization/units; an exact binding comparator; and a rule preserving the three independent route semantics. |

Consequently, an “epoch-census feed” is not one operation shared by S1-S3. S1 alone
has a reusable reduced-array port at its individual checks. S2 and S3 have harness
certificates with no census argument. For them the only contract-preserving use of
new data is: (1) rerun the unchanged, byte-pinned harness, and (2) separately compare
the census-derived object against an explicitly supplied, newly specified binding.

The requested “Cycle-320 unit-weight auxiliary source lift as the sharpest next test”
cannot be quoted as such from the allowed sources. What is grounded is file 2's
`"full-Fock Cycle-320 unit-weight auxiliary sources"` / `"Cycle320 unit-weight
full-Fock lift"` language and file 3's exact one-carrier six-auxiliary-M2 mechanism.
The word “sharpest,” a route-specific `OPEN / UNTESTED` row, and any fuller recipe
would be new supplied data under this four-file boundary.

## COMPLETENESS

- Inventoried every module-defined public function, uppercase constant, public type
  alias, dataclass, and public dataclass property/method in the four allowed files.
- Identified every harness/check entry point, its actual argument object, internal
  fixture use, return shape, and whether an external census has a lawful input port.
- Preserved the scalar-only no-overclaim gate, Cycle-320/full-Fock OPEN-language limit,
  physical-meaning firewalls, and file 4's “not one combined law” rows.
- Distinguished reusable helper parameters from reviewed certification inputs; helper
  parameterization is not represented as a census certificate.
- No script/import was executed, no referenced note/import file was read, and no claim
  was filled in from outside the four-file scope.
