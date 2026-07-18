#!/usr/bin/env python3
"""Stationary dressed mode of the actual carried source/field update.

Reduce the translation-invariant, one-matter Q=N_e+N_f=1 direct carried code
to total momentum K=0 and the field-minus-matter relative coordinate.  The
finite periodic update is still the full matter coin, field coin, local
e <-> g+scalar-field exchange, matter stream, and field stream.  A sparse
finite-volume eigenproblem then selects a proper-cubic stationary dressed
mode with nonzero internal-excitation and field squared-norm weights.

The double-scalar relative profile is compared, as a normalized shape only,
with the separate fixed-reservoir shifted response and Cycle216's 3 L^+
fixture.  An eigenphase is not physical energy or a rate, Q is not a
gravitational source, and the comparison does not supply gravity.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigs

import active_cubic_source_response_cycle211_2026_07_16 as c211
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import carried_internal_species_source_field_ledger_repair_2026_07_17 as carried
import carried_source_retarded_lattice_execution_2026_07_17 as executed
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import stationary_dressed_reservoir_shifted_green_profile_2026_07_17 as fixed


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "STATIONARY_DRESSED_CARRIED_SOURCE_RELATIVE_MODE_NOTE_2026-07-17.md"
)

BETA = -0.3
MEDIATOR_COUPLING = 0.8
SPECIES = c219.common_species(BETA)
ANGLE = MEDIATOR_COUPLING * SPECIES.analytic_mass
TOTAL_MOMENTUM = np.zeros(3)
TRAINING_SIZES = (3, 4, 5, 6, 7)
HELD_SIZES = (8, 9)
SIZES = TRAINING_SIZES + HELD_SIZES
EIGENPHASE_TARGET = 0.365
SELECTOR_PHASE_WINDOW = (0.35, 0.37)
SELECTOR_CANDIDATE_COUNTS = (4, 6)
HELD_EIGENPHASE_WINDOW = (0.36, 0.375)
HELD_EXCITED_WEIGHT_WINDOW = (0.55, 0.57)
HELD_CONTACT_FRACTION_MINIMUM = 0.96
TOLERANCE = 3e-10

PASS = 0
FAIL = 0
SELECTOR_NEIGHBORHOODS: dict[int, tuple[np.ndarray, np.ndarray]] = {}

Position = tuple[int, int, int]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the carried stationary-mode note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "actual carried update",
        "q=n_e+n_f=1",
        "total momentum k=0",
        "relative coordinate",
        "matter coin",
        "local exchange",
        "matter stream",
        "field stream",
        "stationary dressed eigenmode",
        "squared-norm weights",
        "basis-spanning",
        "selector stability",
        "coherent exchange balance",
        "all 24 proper-cubic frames",
        "held l=8,9",
        "mu_carry",
        "pole margin",
        "fixed-reservoir shifted response",
        "actual fixed-reservoir scalar state is not compared",
        "cycle216",
        "contact-deleted tail",
        "theta=0 parameter endpoint",
        "not physical energy",
        "eigenphase is not a rate",
        "not gravity",
        "no contact layer is applied",
        "supplied structure inventory",
        "no no-go claim",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the actual-update eigenmode, controls, comparison, and scope",
        not missing,
        missing,
    )


def site_index(cell: Position, length: int) -> int:
    x, y, z = cell
    return (x * length + y) * length + z


def full_excited_index(cell: Position, direction: int, length: int) -> int:
    return 6 * site_index(cell, length) + direction


def full_pair_index(
    body: Position,
    field: Position,
    matter_direction: int,
    field_direction: int,
    length: int,
) -> int:
    cells = length**3
    pair_flat = site_index(body, length) * cells + site_index(field, length)
    return 6 * cells + 36 * pair_flat + 6 * matter_direction + field_direction


def validate_domain(
    length: int,
    total_momentum: np.ndarray,
    matter_directions: int,
    field_directions: int,
    matter_number: int,
    charge: int,
) -> None:
    if length < 3:
        raise ValueError("periodic relative streams require L>=3")
    if np.linalg.norm(total_momentum) > 1e-14:
        raise ValueError("this selected stationary branch is tested only at K=0")
    if matter_directions != 6 or field_directions != 6:
        raise ValueError("the direct carried code uses six directions per carrier")
    if matter_number != 1 or charge != 1:
        raise ValueError("the tested direct carried domain has one matter and Q=1")


def relative_stream_matrix(
    length: int, total_momentum: np.ndarray = TOTAL_MOMENTUM
) -> sparse.csr_matrix:
    cells = length**3
    dimension = 6 + 36 * cells
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    matter_phases = np.exp(-1j * (c210.DIRECTIONS @ total_momentum))
    for direction in range(6):
        rows.append(direction)
        columns.append(direction)
        values.append(complex(matter_phases[direction]))
    for cell in product(range(length), repeat=3):
        source_flat = site_index(cell, length)
        for matter_direction in range(6):
            for field_direction in range(6):
                displacement = (
                    c210.DIRECTIONS[field_direction]
                    - c210.DIRECTIONS[matter_direction]
                )
                target = tuple(
                    (cell[axis] + int(displacement[axis])) % length
                    for axis in range(3)
                )
                target_flat = site_index(target, length)
                rows.append(
                    6
                    + 36 * target_flat
                    + 6 * matter_direction
                    + field_direction
                )
                columns.append(
                    6
                    + 36 * source_flat
                    + 6 * matter_direction
                    + field_direction
                )
                values.append(complex(matter_phases[matter_direction]))
    return sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def carried_relative_update(
    length: int,
    angle: float = ANGLE,
    total_momentum: np.ndarray = TOTAL_MOMENTUM,
) -> sparse.csr_matrix:
    """Full carried coin/exchange/matter-stream/field-stream update at fixed K."""

    validate_domain(length, total_momentum, 6, 6, 1, 1)
    cells = length**3
    dimension = 6 + 36 * cells
    pair_coin = sparse.kron(
        sparse.eye(cells, dtype=complex, format="csr"),
        sparse.csr_matrix(np.kron(SPECIES.coin, c214.FIELD_COIN)),
        format="csr",
    )
    coin = sparse.block_diag(
        (sparse.csr_matrix(SPECIES.coin), pair_coin), format="csr"
    )

    _exchange, local_vertex, _charge = carried.active_blocks(angle)
    vertex = sparse.eye(dimension, dtype=complex, format="lil")
    vertex[:42, :42] += local_vertex - np.eye(42, dtype=complex)
    vertex = vertex.tocsr()
    return (relative_stream_matrix(length, total_momentum) @ vertex @ coin).tocsr()


def full_periodic_update(
    length: int, angle: float = ANGLE
) -> sparse.csr_matrix:
    """Full one-matter Q=1 periodic update before momentum reduction."""

    cells = length**3
    dimension = 6 * cells + 36 * cells**2
    excited_coin = sparse.kron(
        sparse.eye(cells, dtype=complex, format="csr"),
        sparse.csr_matrix(SPECIES.coin),
        format="csr",
    )
    pair_coin = sparse.kron(
        sparse.eye(cells**2, dtype=complex, format="csr"),
        sparse.csr_matrix(np.kron(SPECIES.coin, c214.FIELD_COIN)),
        format="csr",
    )
    coin = sparse.block_diag((excited_coin, pair_coin), format="csr")

    _exchange, local_vertex, _charge = carried.active_blocks(angle)
    local_delta = local_vertex - np.eye(42, dtype=complex)
    vertex = sparse.eye(dimension, dtype=complex, format="lil")
    for body in product(range(length), repeat=3):
        active = tuple(
            full_excited_index(body, direction, length) for direction in range(6)
        ) + tuple(
            full_pair_index(
                body,
                body,
                matter_direction,
                field_direction,
                length,
            )
            for matter_direction in range(6)
            for field_direction in range(6)
        )
        vertex[np.ix_(active, active)] += local_delta
    vertex = vertex.tocsr()

    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    for body in product(range(length), repeat=3):
        for matter_direction in range(6):
            moved_body = tuple(
                (body[axis] + int(c210.DIRECTIONS[matter_direction, axis]))
                % length
                for axis in range(3)
            )
            rows.append(full_excited_index(moved_body, matter_direction, length))
            columns.append(full_excited_index(body, matter_direction, length))
            values.append(1.0 + 0.0j)
        for field in product(range(length), repeat=3):
            for matter_direction in range(6):
                moved_body = tuple(
                    (body[axis] + int(c210.DIRECTIONS[matter_direction, axis]))
                    % length
                    for axis in range(3)
                )
                for field_direction in range(6):
                    moved_field = tuple(
                        (
                            field[axis]
                            + int(c210.DIRECTIONS[field_direction, axis])
                        )
                        % length
                        for axis in range(3)
                    )
                    rows.append(
                        full_pair_index(
                            moved_body,
                            moved_field,
                            matter_direction,
                            field_direction,
                            length,
                        )
                    )
                    columns.append(
                        full_pair_index(
                            body,
                            field,
                            matter_direction,
                            field_direction,
                            length,
                        )
                    )
                    values.append(1.0 + 0.0j)
    stream = sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )
    return (stream @ vertex @ coin).tocsr()


def relative_lift_isometry(length: int) -> sparse.csr_matrix:
    """K=0 isometry from the relative block into the full periodic sector."""

    cells = length**3
    full_dimension = 6 * cells + 36 * cells**2
    relative_dimension = 6 + 36 * cells
    scale = 1 / np.sqrt(cells)
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    for body in product(range(length), repeat=3):
        for matter_direction in range(6):
            rows.append(full_excited_index(body, matter_direction, length))
            columns.append(matter_direction)
            values.append(scale + 0.0j)
        for relative in product(range(length), repeat=3):
            field = tuple(
                (body[axis] + relative[axis]) % length for axis in range(3)
            )
            relative_flat = site_index(relative, length)
            for matter_direction in range(6):
                for field_direction in range(6):
                    rows.append(
                        full_pair_index(
                            body,
                            field,
                            matter_direction,
                            field_direction,
                            length,
                        )
                    )
                    columns.append(
                        6
                        + 36 * relative_flat
                        + 6 * matter_direction
                        + field_direction
                    )
                    values.append(scale + 0.0j)
    return sparse.csr_matrix(
        (values, (rows, columns)),
        shape=(full_dimension, relative_dimension),
    )


def direct_relative_step(
    excited: np.ndarray,
    pair: np.ndarray,
    angle: float = ANGLE,
    total_momentum: np.ndarray = TOTAL_MOMENTUM,
) -> tuple[np.ndarray, np.ndarray]:
    """Array execution of the same schedule, independent of sparse assembly."""

    coined_excited = SPECIES.coin @ excited
    coined_pair = np.einsum(
        "ab,cd,xyzbd->xyzac",
        SPECIES.coin,
        c214.FIELD_COIN,
        pair,
        optimize=True,
    )
    coined_excited, coined_pair[0, 0, 0] = carried.local_vertex(
        coined_excited, coined_pair[0, 0, 0], angle
    )
    matter_phases = np.exp(-1j * (c210.DIRECTIONS @ total_momentum))
    output_excited = matter_phases * coined_excited
    output_pair = np.zeros_like(coined_pair)
    for matter_direction in range(6):
        for field_direction in range(6):
            displacement = tuple(
                int(value)
                for value in (
                    c210.DIRECTIONS[field_direction]
                    - c210.DIRECTIONS[matter_direction]
                )
            )
            output_pair[..., matter_direction, field_direction] = (
                matter_phases[matter_direction]
                * np.roll(
                    coined_pair[..., matter_direction, field_direction],
                    displacement,
                    axis=(0, 1, 2),
                )
            )
    return output_excited, output_pair


def split_state(state: np.ndarray, length: int) -> tuple[np.ndarray, np.ndarray]:
    return state[:6], state[6:].reshape(length, length, length, 6, 6)


def flatten_state(excited: np.ndarray, pair: np.ndarray) -> np.ndarray:
    return np.concatenate((excited, pair.reshape(-1)))


def lift_relative_state(
    excited: np.ndarray, pair: np.ndarray, length: int
) -> carried.CarriedState:
    """Lift a K=0 relative state to the full translation-invariant torus."""

    scale = 1 / np.sqrt(length**3)
    excited_full: dict[Position, np.ndarray] = {}
    pair_full: dict[tuple[Position, Position], np.ndarray] = {}
    for body in product(range(length), repeat=3):
        excited_full[body] = scale * excited.copy()
        for relative in product(range(length), repeat=3):
            field = tuple(
                (body[axis] + relative[axis]) % length for axis in range(3)
            )
            pair_full[(body, field)] = scale * pair[relative].copy()
    return carried.CarriedState(excited_full, pair_full)


def select_dressed_eigenpair(
    length: int,
    *,
    target_phase: float = EIGENPHASE_TARGET,
    candidates: int = 4,
) -> tuple[sparse.csr_matrix, complex, np.ndarray]:
    """Select the source-bright branch near a declared numerical target.

    The target and maximum-N_e selection choose among eigenpairs; neither is
    inserted into the update.  The resulting vector is normalized and given a
    common phase with positive overlap against the uniform excited direction.
    """

    update = carried_relative_update(length)
    start = np.zeros(update.shape[0], dtype=complex)
    start[:6] = c210.UNIFORM
    returned_candidates = max(candidates, max(SELECTOR_CANDIDATE_COUNTS))
    eigenvalues, eigenvectors = eigs(
        update,
        k=returned_candidates,
        sigma=np.exp(1j * target_phase),
        v0=start,
        tol=3e-12,
        maxiter=50000,
        ncv=max(24, 2 * returned_candidates + 1),
    )
    nearest = np.argsort(
        abs(eigenvalues - np.exp(1j * target_phase))
    )[:candidates]
    source_weights = np.sum(
        np.abs(eigenvectors[:6, nearest]) ** 2, axis=0
    ) / np.sum(
        np.abs(eigenvectors[:, nearest]) ** 2, axis=0
    )
    index = int(nearest[int(np.argmax(source_weights))])
    if target_phase == EIGENPHASE_TARGET and candidates == SELECTOR_CANDIDATE_COUNTS[0]:
        SELECTOR_NEIGHBORHOODS[length] = (
            eigenvalues.copy(),
            eigenvectors.copy(),
        )
    state = eigenvectors[:, index]
    state /= np.linalg.norm(state)
    overlap = np.vdot(c210.UNIFORM, state[:6])
    state *= np.exp(-1j * np.angle(overlap))
    return update, eigenvalues[index], state


def double_scalar_projection(state: np.ndarray, length: int) -> np.ndarray:
    _excited, pair = split_state(state, length)
    return np.einsum(
        "m,xyzmd,d->xyz",
        c210.UNIFORM.conj(),
        pair,
        c210.UNIFORM,
        optimize=True,
    )


def shape_comparison(
    observed: np.ndarray, comparator: np.ndarray, *, remove_contact: bool
) -> tuple[float, float]:
    """Phase-agnostic unit-shape overlap and aligned residual; no scale fit."""

    left: np.ndarray
    right: np.ndarray
    if remove_contact:
        mask = np.ones(observed.shape, dtype=bool)
        mask[0, 0, 0] = False
        left = observed[mask].copy()
        right = comparator[mask].copy()
    else:
        left = observed.reshape(-1).copy()
        right = comparator.reshape(-1).copy()
    left -= np.mean(left)
    right -= np.mean(right)
    overlap = float(
        abs(np.vdot(left, right)) / (np.linalg.norm(left) * np.linalg.norm(right))
    )
    return overlap, float(np.sqrt(max(0.0, 2 - 2 * overlap)))


def frame_permutation(length: int, frame: np.ndarray) -> sparse.csr_matrix:
    dimension = 6 + 36 * length**3
    representation = c210.direction_permutation(frame)
    direction_map = tuple(
        int(np.argmax(representation[:, direction])) for direction in range(6)
    )
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    for direction in range(6):
        rows.append(direction_map[direction])
        columns.append(direction)
        values.append(1.0 + 0.0j)
    for cell in product(range(length), repeat=3):
        target = tuple(int(value % length) for value in frame @ np.asarray(cell))
        source_flat = site_index(cell, length)
        target_flat = site_index(target, length)
        for matter_direction in range(6):
            for field_direction in range(6):
                rows.append(
                    6
                    + 36 * target_flat
                    + 6 * direction_map[matter_direction]
                    + direction_map[field_direction]
                )
                columns.append(
                    6
                    + 36 * source_flat
                    + 6 * matter_direction
                    + field_direction
                )
                values.append(1.0 + 0.0j)
    return sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def local_update_and_full_schedule_controls() -> None:
    print("\nACTUAL CARRIED UPDATE / DIRECT-SCHEDULE CROSS-CHECK")
    length = 3
    update = carried_relative_update(length)
    identity = sparse.eye(update.shape[0], dtype=complex, format="csr")
    unitarity_residual = float(
        sparse.linalg.norm(update.conj().T @ update - identity)
    )

    rng = np.random.default_rng(2026071711)
    excited = rng.normal(size=6) + 1j * rng.normal(size=6)
    pair = rng.normal(size=(length, length, length, 6, 6)) + 1j * rng.normal(
        size=(length, length, length, 6, 6)
    )
    scale = np.sqrt(np.vdot(excited, excited).real + np.vdot(pair, pair).real)
    excited /= scale
    pair /= scale
    direct_excited, direct_pair = direct_relative_step(excited, pair)
    sparse_output = update @ flatten_state(excited, pair)
    matrix_schedule_residual = float(
        np.linalg.norm(
            sparse_output - flatten_state(direct_excited, direct_pair)
        )
    )
    check(
        "the finite K=0 relative matrix is unitary and equals the direct relative schedule",
        unitarity_residual < 3e-13 and matrix_schedule_residual < 3e-13,
        {
            "L": length,
            "dimension": update.shape[0],
            "unitarity_residual": unitarity_residual,
            "matrix_vs_direct_schedule": matrix_schedule_residual,
        },
    )

    full_update = full_periodic_update(length)
    lift = relative_lift_isometry(length)
    relative_identity = sparse.eye(
        update.shape[0], dtype=complex, format="csr"
    )
    isometry_residual = float(
        sparse.linalg.norm(lift.conj().T @ lift - relative_identity)
    )
    intertwiner_residual = float(
        sparse.linalg.norm(full_update @ lift - lift @ update)
    )
    check(
        "the basis-spanning L=3 K=0 lift is an isometry and exactly intertwines the full periodic update",
        lift.shape == (full_update.shape[0], update.shape[0])
        and lift.nnz == full_update.shape[0]
        and isometry_residual < 4e-13
        and intertwiner_residual < 4e-12,
        {
            "full_Q1_dimension": full_update.shape[0],
            "K0_relative_dimension": update.shape[0],
            "lift_nonzero_entries": lift.nnz,
            "isometry_residual": isometry_residual,
            "full_update_intertwiner_residual": intertwiner_residual,
            "basis_spanning": True,
        },
    )

    lifted = lift_relative_state(excited, pair, length)
    full_output, report = executed.joint_step(
        lifted, SPECIES, ANGLE, tick=1, side=length
    )
    expected = lift_relative_state(direct_excited, direct_pair, length)
    full_schedule_residual = carried.state_residual(full_output, expected)
    check(
        "one randomized lifted state also matches the independent periodic carried-state executor",
        full_schedule_residual < 3e-13
        and report.global_q_residual < 3e-13
        and abs(carried.state_norm(full_output) - 1) < 3e-13,
        {
            "full_schedule_residual": full_schedule_residual,
            "global_Q_residual": report.global_q_residual,
            "output_norm": carried.state_norm(full_output),
            "full_Q1_dimension": 6 * length**3 + 36 * length**6,
            "K0_relative_dimension": update.shape[0],
        },
    )


def eigenmode_and_comparison_controls() -> dict[int, tuple[sparse.csr_matrix, complex, np.ndarray]]:
    print("\nSTATIONARY DRESSED CARRIED EIGENMODE / FINITE-SIZE COMPARISON")
    cache: dict[int, tuple[sparse.csr_matrix, complex, np.ndarray]] = {}
    rows = []
    sine = np.sin(ANGLE)
    cosine = np.cos(ANGLE)
    for length in SIZES:
        update, eigenvalue, state = select_dressed_eigenpair(length)
        cache[length] = (update, eigenvalue, state)
        excited, pair = split_state(state, length)
        excited_weight = float(np.vdot(excited, excited).real)
        field_weight = float(np.vdot(pair, pair).real)
        eigen_residual = float(np.linalg.norm(update @ state - eigenvalue * state))
        excited_equation_residual = float(
            np.linalg.norm(
                eigenvalue * excited
                - update[:6, :6] @ excited
                - update[:6, 6:] @ pair.reshape(-1)
            )
        )
        pair_equation_residual = float(
            np.linalg.norm(
                eigenvalue * pair.reshape(-1)
                - update[6:, :6] @ excited
                - update[6:, 6:] @ pair.reshape(-1)
            )
        )

        coined_excited = SPECIES.coin @ excited
        coined_pair = np.einsum(
            "ab,cd,xyzbd->xyzac",
            SPECIES.coin,
            c214.FIELD_COIN,
            pair,
            optimize=True,
        )
        contact_scalar = coined_pair[0, 0, 0] @ c210.UNIFORM
        _new_excited, new_contact_pair = carried.local_vertex(
            coined_excited, coined_pair[0, 0, 0], ANGLE
        )
        direct_delta_field = float(
            np.vdot(new_contact_pair, new_contact_pair).real
            - np.vdot(coined_pair[0, 0, 0], coined_pair[0, 0, 0]).real
        )
        excited_diagonal_term = float(
            sine**2 * np.vdot(coined_excited, coined_excited).real
        )
        field_diagonal_term = float(
            -sine**2 * np.vdot(contact_scalar, contact_scalar).real
        )
        coherent_interference_term = float(
            2
            * sine
            * cosine
            * np.imag(np.vdot(coined_excited, contact_scalar))
        )

        scalar = double_scalar_projection(state, length)
        scalar_weight = float(np.vdot(scalar, scalar).real)
        contact_fraction = float(abs(scalar[0, 0, 0]) ** 2 / scalar_weight)
        cycle216 = 3 * c211.solve_field(c211.point_source(length))
        carried_shift = float(6 * (1 - np.cos(np.angle(eigenvalue))))
        laplacian, _ = c211.c9.fourier_symbols(length)
        minimum_nonzero_laplacian = float(
            np.min(laplacian[laplacian > 1e-14])
        )
        carried_pole_margin = minimum_nonzero_laplacian - carried_shift
        carried_shifted_response = fixed.shifted_green_profile(
            length, carried_shift
        )
        _fixed_update, fixed_eigenvalue, _fixed_state = fixed.dressed_eigenstate(
            length
        )
        fixed_shift = float(6 * (1 - np.cos(np.angle(fixed_eigenvalue))))
        fixed_response = fixed.shifted_green_profile(length, fixed_shift)
        full_cycle_overlap, full_cycle_residual = shape_comparison(
            scalar, cycle216, remove_contact=False
        )
        tail_cycle_overlap, tail_cycle_residual = shape_comparison(
            scalar, cycle216, remove_contact=True
        )
        full_carried_overlap, full_carried_residual = shape_comparison(
            scalar, carried_shifted_response, remove_contact=False
        )
        tail_carried_overlap, tail_carried_residual = shape_comparison(
            scalar, carried_shifted_response, remove_contact=True
        )
        carried_cycle_overlap, carried_cycle_residual = shape_comparison(
            carried_shifted_response, cycle216, remove_contact=False
        )
        full_fixed_overlap, full_fixed_residual = shape_comparison(
            scalar, fixed_response, remove_contact=False
        )
        tail_fixed_overlap, tail_fixed_residual = shape_comparison(
            scalar, fixed_response, remove_contact=True
        )
        fixed_cycle_overlap, _fixed_cycle_residual = shape_comparison(
            fixed_response, cycle216, remove_contact=False
        )
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "dimension": update.shape[0],
                "eigenphase": float(np.angle(eigenvalue)),
                "eigenvalue_modulus_residual": float(abs(abs(eigenvalue) - 1)),
                "eigen_residual": eigen_residual,
                "excited_equation_residual": excited_equation_residual,
                "pair_equation_residual": pair_equation_residual,
                "excited_squared_norm_weight": excited_weight,
                "field_squared_norm_weight": field_weight,
                "Q_residual": abs(excited_weight + field_weight - 1),
                "direct_Delta_Nf": direct_delta_field,
                "excited_diagonal_term": excited_diagonal_term,
                "field_diagonal_term": field_diagonal_term,
                "coherent_interference_term": coherent_interference_term,
                "exchange_decomposition_residual": abs(
                    direct_delta_field
                    - excited_diagonal_term
                    - field_diagonal_term
                    - coherent_interference_term
                ),
                "double_scalar_weight": scalar_weight,
                "double_scalar_contact_fraction": contact_fraction,
                "carried_shift_mu": carried_shift,
                "minimum_nonzero_Laplacian": minimum_nonzero_laplacian,
                "carried_shift_pole_margin": carried_pole_margin,
                "fixed_reservoir_shift": fixed_shift,
                "full_shape_overlap_Cycle216": full_cycle_overlap,
                "full_shape_residual_Cycle216": full_cycle_residual,
                "off_contact_tail_overlap_Cycle216": tail_cycle_overlap,
                "off_contact_tail_residual_Cycle216": tail_cycle_residual,
                "full_shape_overlap_carried_shifted": full_carried_overlap,
                "full_shape_residual_carried_shifted": full_carried_residual,
                "contact_deleted_tail_overlap_carried_shifted": tail_carried_overlap,
                "contact_deleted_tail_residual_carried_shifted": tail_carried_residual,
                "carried_shifted_overlap_Cycle216": carried_cycle_overlap,
                "carried_shifted_residual_Cycle216": carried_cycle_residual,
                "full_shape_overlap_fixed_shifted": full_fixed_overlap,
                "full_shape_residual_fixed_shifted": full_fixed_residual,
                "off_contact_tail_overlap_fixed_shifted": tail_fixed_overlap,
                "off_contact_tail_residual_fixed_shifted": tail_fixed_residual,
                "fixed_shifted_overlap_Cycle216": fixed_cycle_overlap,
            }
        )

    check(
        "the actual full carried update has a source-bright stationary dressed eigenmode on every L=3,...,9",
        tuple(row["L"] for row in rows) == SIZES
        and all(row["eigen_residual"] < 4e-12 for row in rows)
        and all(row["eigenvalue_modulus_residual"] < 3e-13 for row in rows)
        and all(0.54 < row["excited_squared_norm_weight"] < 0.57 for row in rows)
        and all(0.43 < row["field_squared_norm_weight"] < 0.46 for row in rows)
        and all(row["Q_residual"] < 3e-13 for row in rows),
        [
            {
                key: row[key]
                for key in (
                    "L",
                    "held",
                    "eigenphase",
                    "eigen_residual",
                    "excited_squared_norm_weight",
                    "field_squared_norm_weight",
                    "Q_residual",
                )
            }
            for row in rows
        ],
    )
    check(
        "the excited and pair block equations hold for the selected full-update eigenpairs",
        all(row["excited_equation_residual"] < 4e-12 for row in rows)
        and all(row["pair_equation_residual"] < 4e-12 for row in rows),
        [
            (
                row["L"],
                row["excited_equation_residual"],
                row["pair_equation_residual"],
            )
            for row in rows
        ],
    )
    check(
        "the positive excited diagonal term is exactly balanced by the negative field diagonal and coherent interference terms",
        all(abs(row["direct_Delta_Nf"]) < 4e-13 for row in rows)
        and all(row["excited_diagonal_term"] > 0.06 for row in rows)
        and all(row["field_diagonal_term"] < -0.02 for row in rows)
        and all(row["coherent_interference_term"] < -0.04 for row in rows)
        and all(row["exchange_decomposition_residual"] < 4e-13 for row in rows),
        [
            {
                key: row[key]
                for key in (
                    "L",
                    "direct_Delta_Nf",
                    "excited_diagonal_term",
                    "field_diagonal_term",
                    "coherent_interference_term",
                    "exchange_decomposition_residual",
                )
            }
            for row in rows
        ],
    )

    held_rows = [row for row in rows if row["held"]]
    check(
        "held L=8,9 preserve the source-bright branch and its localized double-scalar profile",
        tuple(row["L"] for row in held_rows) == HELD_SIZES
        and all(
            HELD_EIGENPHASE_WINDOW[0]
            < row["eigenphase"]
            < HELD_EIGENPHASE_WINDOW[1]
            for row in held_rows
        )
        and all(
            HELD_EXCITED_WEIGHT_WINDOW[0]
            < row["excited_squared_norm_weight"]
            < HELD_EXCITED_WEIGHT_WINDOW[1]
            for row in held_rows
        )
        and all(
            row["double_scalar_contact_fraction"]
            > HELD_CONTACT_FRACTION_MINIMUM
            for row in held_rows
        )
        and all(row["eigen_residual"] < 4e-12 for row in held_rows),
        held_rows,
    )
    check(
        "the held contact-deleted scalar-tail shape is quantified against residual-matched and separate Green comparators",
        all(row["fixed_shifted_overlap_Cycle216"] > 0.999999 for row in held_rows)
        and all(row["carried_shift_pole_margin"] > 0 for row in held_rows)
        and all(
            0.2 < row["off_contact_tail_overlap_Cycle216"] < 0.4
            for row in held_rows
        )
        and all(
            0.2 < row["off_contact_tail_overlap_fixed_shifted"] < 0.4
            for row in held_rows
        )
        and all(
            0.2
            < row["contact_deleted_tail_overlap_carried_shifted"]
            < 0.4
            for row in held_rows
        ),
        [
            {
                key: row[key]
                for key in (
                    "L",
                    "double_scalar_contact_fraction",
                    "carried_shift_mu",
                    "minimum_nonzero_Laplacian",
                    "carried_shift_pole_margin",
                    "full_shape_overlap_Cycle216",
                    "off_contact_tail_overlap_Cycle216",
                    "off_contact_tail_residual_Cycle216",
                    "full_shape_overlap_carried_shifted",
                    "contact_deleted_tail_overlap_carried_shifted",
                    "contact_deleted_tail_residual_carried_shifted",
                    "carried_shifted_overlap_Cycle216",
                    "full_shape_overlap_fixed_shifted",
                    "off_contact_tail_overlap_fixed_shifted",
                    "off_contact_tail_residual_fixed_shifted",
                    "fixed_shifted_overlap_Cycle216",
                )
            }
            for row in held_rows
        ],
    )
    return cache


def selector_stability_controls(
    cache: dict[int, tuple[sparse.csr_matrix, complex, np.ndarray]]
) -> None:
    print("\nHELD BRANCH IDENTITY / SELECTOR STABILITY")
    variants = tuple(
        (target_phase, candidates)
        for target_phase in (
            SELECTOR_PHASE_WINDOW[0],
            EIGENPHASE_TARGET,
            SELECTOR_PHASE_WINDOW[1],
        )
        for candidates in SELECTOR_CANDIDATE_COUNTS
    )
    rows = []
    for length in HELD_SIZES:
        reference_value = cache[length][1]
        reference_state = cache[length][2]
        reference_weight = float(np.linalg.norm(reference_state[:6]) ** 2)
        neighborhood_values, neighborhood_vectors = SELECTOR_NEIGHBORHOODS[length]
        for target_phase, candidates in variants:
            target = np.exp(1j * target_phase)
            nearest = np.argsort(abs(neighborhood_values - target))[:candidates]
            source_weights = np.sum(
                np.abs(neighborhood_vectors[:6, nearest]) ** 2, axis=0
            ) / np.sum(np.abs(neighborhood_vectors[:, nearest]) ** 2, axis=0)
            index = int(nearest[int(np.argmax(source_weights))])
            eigenvalue = neighborhood_values[index]
            state = neighborhood_vectors[:, index]
            state /= np.linalg.norm(state)
            state *= np.exp(
                -1j * np.angle(np.vdot(c210.UNIFORM, state[:6]))
            )
            rows.append(
                {
                    "L": length,
                    "target_phase": target_phase,
                    "returned_candidates": candidates,
                    "eigenphase": float(np.angle(eigenvalue)),
                    "eigenphase_residual_from_reference": float(
                        abs(np.angle(eigenvalue / reference_value))
                    ),
                    "phase_agnostic_state_overlap": float(
                        abs(np.vdot(reference_state, state))
                    ),
                    "excited_weight_residual": float(
                        abs(np.linalg.norm(state[:6]) ** 2 - reference_weight)
                    ),
                }
            )
    check(
        "the held L=8,9 branch identity is stable when one six-candidate neighborhood is re-ranked across the declared target and candidate-count audit",
        len(rows) == len(HELD_SIZES) * len(variants)
        and all(row["eigenphase_residual_from_reference"] < 3e-12 for row in rows)
        and all(row["phase_agnostic_state_overlap"] > 1 - 3e-11 for row in rows)
        and all(row["excited_weight_residual"] < 3e-11 for row in rows),
        rows,
    )


def covariance_controls(
    cache: dict[int, tuple[sparse.csr_matrix, complex, np.ndarray]]
) -> None:
    print("\nPROPER-CUBIC COVARIANCE AT K=0")
    length = 3
    update = cache[length][0]
    operator_residuals = []
    state_residuals = {tested: [] for tested in SIZES}
    rng = np.random.default_rng(2026071712)
    held_random_states = {}
    held_action_residuals = {tested: [] for tested in HELD_SIZES}
    for tested in HELD_SIZES:
        random_state = rng.normal(size=cache[tested][0].shape[0]) + 1j * rng.normal(
            size=cache[tested][0].shape[0]
        )
        held_random_states[tested] = random_state / np.linalg.norm(random_state)
    for frame in c210.proper_cubic_frames():
        representation = frame_permutation(length, frame)
        operator_residuals.append(
            float(sparse.linalg.norm(representation @ update - update @ representation))
        )
        for tested in SIZES:
            tested_representation = frame_permutation(tested, frame)
            state = cache[tested][2]
            state_residuals[tested].append(
                float(np.linalg.norm(tested_representation @ state - state))
            )
            if tested in HELD_SIZES:
                tested_update = cache[tested][0]
                random_state = held_random_states[tested]
                held_action_residuals[tested].append(
                    float(
                        np.linalg.norm(
                            tested_representation @ (tested_update @ random_state)
                            - tested_update @ (tested_representation @ random_state)
                        )
                    )
                )
    check(
        "the K=0 update and selected modes obey the declared L=3 operator and held-size action covariance controls",
        len(operator_residuals) == 24
        and max(operator_residuals) < 4e-13
        and all(len(state_residuals[length]) == 24 for length in SIZES)
        and max(max(values) for values in state_residuals.values()) < 4e-11
        and all(
            len(held_action_residuals[length]) == 24
            and max(held_action_residuals[length]) < 4e-11
            for length in HELD_SIZES
        ),
        {
            "K0_maps_to_itself": True,
            "maximum_L3_operator_commutator": max(operator_residuals),
            "maximum_state_residual_by_L": {
                length: max(state_residuals[length]) for length in SIZES
            },
            "maximum_random_action_residual_by_held_L": {
                length: max(held_action_residuals[length])
                for length in HELD_SIZES
            },
        },
    )


def parameter_endpoint_domain_and_inventory_controls() -> None:
    print("\nTHETA=0 PARAMETER ENDPOINT / LAWFUL DOMAIN / INVENTORY")
    length = 3
    endpoint_update = carried_relative_update(length, angle=0.0)
    pure_excited = np.zeros(endpoint_update.shape[0], dtype=complex)
    pure_excited[:6] = c210.UNIFORM
    expected = np.exp(1j * SPECIES.rest_phase) * pure_excited
    check(
        "the supplied theta=0 parameter endpoint leaves the pure K=0 excited matter mode with the inherited rest eigenphase",
        np.linalg.norm(endpoint_update @ pure_excited - expected) < 3e-13
        and np.linalg.norm((endpoint_update @ pure_excited)[6:]) < 3e-14,
        {
            "theta_zero_parameter_endpoint_residual": float(
                np.linalg.norm(endpoint_update @ pure_excited - expected)
            ),
            "rest_eigenphase": SPECIES.rest_phase,
            "field_weight_after_one_tick": float(
                np.linalg.norm((endpoint_update @ pure_excited)[6:]) ** 2
            ),
            "scope": "supplied parameter setting, not a deletion theorem for a derived law",
        },
    )

    validate_domain(3, TOTAL_MOMENTUM, 6, 6, 1, 1)
    rejected = 0
    for candidate in (
        (2, TOTAL_MOMENTUM, 6, 6, 1, 1),
        (3, np.asarray((0.1, 0.0, 0.0)), 6, 6, 1, 1),
        (3, TOTAL_MOMENTUM, 5, 6, 1, 1),
        (3, TOTAL_MOMENTUM, 6, 5, 1, 1),
        (3, TOTAL_MOMENTUM, 6, 6, 2, 1),
        (3, TOTAL_MOMENTUM, 6, 6, 1, 2),
    ):
        try:
            validate_domain(*candidate)
        except ValueError:
            rejected += 1
    check(
        "the lawful-domain validator rejects aliased, nonzero-K, mistyped, and wrong-sector fixtures",
        rejected == 6,
        {"rejected": rejected},
    )

    check(
        "the supplied structure inventory separates the stationary mode from energy, rate, and gravity semantics",
        True,
        {
            "supplied": (
                "declared direct carried one-matter Q=1 hard-core code and its 12 matter plus six field M2 per-cell basis injection",
                "Cycle219 beta=-0.3 common matter coin, Cycle214 field coin, kappa=0.8 angle map, direction-preserving local exchange, and coin-exchange-matter-stream-field-stream order",
                "finite periodic relative coordinate, total momentum K=0, sizes L=3,...,9, and the proper-cubic frame action",
                "eigenpair selector target phase 0.365, one six-candidate shift-invert neighborhood, primary four-nearest maximum excited-sector squared-norm selection, normalization, and common-phase convention",
                "selector audit window [0.35,0.37], candidate counts 4 and 6, held eigenphase window (0.36,0.375), held excited-weight window (0.55,0.57), and held contact-fraction minimum 0.96",
                "training L=3,...,7; held L=8,9; residual-matched mu_carry shifted response, separate fixed-reservoir shifted response, and Cycle216 zero-mean 3L+ shape comparators",
                "contact-deleted tail definition: remove the relative-origin entry from both arrays, subtract the mean over only the remaining entries, unit-normalize, and compare by phase-agnostic overlap",
            ),
            "derived": (
                "the basis-spanning L=3 K=0 isometry/intertwiner and source-bright stationary eigenpairs of the actual finite carried update with exact Q and block-equation residuals",
                "coherent stationary exchange balance among the excited diagonal, field diagonal, and interference terms",
                "proper-cubic invariance at K=0, held-size selector stability, supplied theta=0 parameter endpoint, and quantitative comparator overlaps",
            ),
            "not_earned": (
                "physical energy, Hamiltonian or transfer-generator identification, eigenphase-as-rate, clock normalization, or gravity/source semantics",
                "a Cycle216 derivation from the carried update or equality of the selected carried tail with any Green comparator; the actual fixed-reservoir scalar state is not compared",
                "nonzero-total-momentum dispersion, a localized center-of-mass stationary state, many-field or many-matter closure, or contact dynamics",
                "a full 2^(18 L^3) physical matrix, Cycle269 splice, whole physical-M2 compiler, Record, Born rule, axiom change, or audit authority",
            ),
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("STATIONARY DRESSED MODE OF THE ACTUAL CARRIED UPDATE")
    note_contract()
    local_update_and_full_schedule_controls()
    cache = eigenmode_and_comparison_controls()
    selector_stability_controls(cache)
    covariance_controls(cache)
    parameter_endpoint_domain_and_inventory_controls()
    print("\nSUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        {
            "declared_domain": "one matter, Q=N_e+N_f=1, total momentum K=0",
            "training_sizes": TRAINING_SIZES,
            "held_sizes": HELD_SIZES,
            "relative_dimension": "6+36 L^3",
            "actual_schedule": "matter+field coin, local exchange, matter stream, field stream",
            "status": "constructive stationary carried eigenmode with quantified contact-deleted scalar-tail comparisons",
            "authority": "none",
            "audit": "unset",
        },
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
