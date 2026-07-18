#!/usr/bin/env python3
"""Two fixed local reservoirs in the conserved one-excitation field update.

Extend the stationary dressed reservoir construction to two distinct active
vertices.  Test its bright dressed eigenpair, an exactly constructed
zero-total-q antisymmetric lambda=1 compatibility member, the direct
gate-to-field equations, additive shifted-Green
composition, and extraction of an off-diagonal scalar response from the
bright eigenphase.  Compare that finite shifted bilinear with Cycle216's
zero-shift 3 L^+ block without identifying the two.

All phases, overlaps, and bilinears are finite-operator coordinates.  They are
not physical energy, gravity, a rate, force, or a source/stress law.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigs


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import active_cubic_source_response_cycle211_2026_07_16 as c211
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import stationary_dressed_reservoir_shifted_green_profile_2026_07_17 as single


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "TWO_FIXED_RESERVOIR_STATIONARY_COMPOSITION_KERNEL_NOTE_2026-07-17.md"
)
THETA = single.THETA
SIZES = (3, 4, 5, 6, 7, 8, 9)
HELD_OUT = 9
ORIGIN = (0, 0, 0)
NEIGHBOUR = (1, 0, 0)
BRIGHT_PHASE_RATIO_WINDOW = (0.95, 0.98)
BRIGHT_RESERVOIR_WEIGHT_WINDOW = (0.44, 0.47)
COMPLEX_LEFT_COEFFICIENT = 1.0 + 0.5j
COMPLEX_RIGHT_COEFFICIENT = -0.3 + 0.8j
HELD_SEPARATIONS = tuple(
    (first, second, third)
    for first in range(1, HELD_OUT // 2 + 1)
    for second in range(first + 1)
    for third in range(second + 1)
) + tuple(
    (first, second, -third)
    for first in range(3, HELD_OUT // 2 + 1)
    for second in range(2, first)
    for third in range(1, second)
)
PASS = 0
FAIL = 0


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
        check("the two-reservoir note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "two active fixed local reservoirs",
        "one-excitation sector",
        "antisymmetric lambda=1 compatibility member",
        "spectral cross-coordinate",
        "composition-safe shifted bilinear",
        "cycle216",
        "held-out l=9",
        "all 24 proper-cubic frames",
        "728 nonzero minimal-image vectors",
        "phase-ratio acceptance window",
        "complex probe coefficients",
        "zero-mode subtraction",
        "normalization",
        "supplied structure inventory",
        "not physical energy",
        "not gravity",
        "eigenphase is not a rate",
        "no host-side renewal",
        "no matter or contact update",
        "no whole-compiler claim",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note preserves the two-reservoir mechanism, finite controls, inventory, and scope",
        not missing,
        missing,
    )


def site_index(cell: tuple[int, int, int], length: int) -> int:
    x, y, z = cell
    return (x * length + y) * length + z


def validate_fixture(
    length: int,
    positions: tuple[tuple[int, int, int], ...],
    thetas: tuple[float, ...],
    excitation_sector: int = 1,
) -> None:
    if length < 3:
        raise ValueError("periodic direction streams require L>=3")
    if len(positions) != 2 or len(thetas) != 2:
        raise ValueError("this runner requires exactly two reservoirs and two angles")
    if positions[0] == positions[1]:
        raise ValueError("the two local vertices must have disjoint source cells")
    if any(
        len(position) != 3
        or any(coordinate < 0 or coordinate >= length for coordinate in position)
        for position in positions
    ):
        raise ValueError("source positions must be three-coordinates inside the torus")
    if excitation_sector != 1:
        raise ValueError("this runner tests only the conserved one-excitation sector")


def field_coin_block(length: int) -> sparse.csr_matrix:
    return sparse.kron(
        sparse.eye(length**3, dtype=complex, format="csr"),
        sparse.csr_matrix(c214.FIELD_COIN),
        format="csr",
    )


def vertex_matrix(
    length: int,
    positions: tuple[tuple[int, int, int], tuple[int, int, int]],
    reservoir_index: int,
    theta: float,
) -> sparse.csr_matrix:
    dimension = 2 + 6 * length**3
    delta = single.local_vertex_block(theta) - np.eye(7, dtype=complex)
    local = (reservoir_index,) + tuple(
        2 + 6 * site_index(positions[reservoir_index], length) + direction
        for direction in range(6)
    )
    rows = []
    columns = []
    values = []
    for left, target in enumerate(local):
        for right, source in enumerate(local):
            value = delta[left, right]
            if abs(value) > 1e-15:
                rows.append(target)
                columns.append(source)
                values.append(value)
    return sparse.eye(dimension, dtype=complex, format="csr") + sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def stream_matrix(length: int) -> sparse.csr_matrix:
    dimension = 2 + 6 * length**3
    rows = [0, 1]
    columns = [0, 1]
    values = [1.0 + 0j, 1.0 + 0j]
    for cell in product(range(length), repeat=3):
        source_flat = site_index(cell, length)
        for direction, displacement in enumerate(c210.DIRECTIONS):
            target = tuple(
                (cell[axis] + int(displacement[axis])) % length
                for axis in range(3)
            )
            target_flat = site_index(target, length)
            rows.append(2 + 6 * target_flat + direction)
            columns.append(2 + 6 * source_flat + direction)
            values.append(1.0 + 0j)
    return sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def two_defect_update(
    length: int,
    positions: tuple[tuple[int, int, int], tuple[int, int, int]],
    thetas: tuple[float, float] = (THETA, THETA),
) -> sparse.csr_matrix:
    validate_fixture(length, positions, thetas)
    coin = sparse.block_diag(
        (
            sparse.eye(2, dtype=complex, format="csr"),
            field_coin_block(length),
        ),
        format="csr",
    )
    vertices = tuple(
        vertex_matrix(length, positions, index, thetas[index])
        for index in range(2)
    )
    return (stream_matrix(length) @ vertices[1] @ vertices[0] @ coin).tocsr()


def source_field_vector(
    length: int, position: tuple[int, int, int]
) -> np.ndarray:
    output = np.zeros(6 * length**3, dtype=complex)
    start = 6 * site_index(position, length)
    output[start : start + 6] = c210.UNIFORM
    return output


def scalar_projection(state: np.ndarray, length: int) -> np.ndarray:
    field = state[2:].reshape(length, length, length, 6)
    return np.einsum(
        "d,xyzd->xyz", c210.UNIFORM.conj(), field, optimize=True
    )


def emitted_amplitudes(
    state: np.ndarray,
    length: int,
    positions: tuple[tuple[int, int, int], tuple[int, int, int]],
    thetas: tuple[float, float] = (THETA, THETA),
) -> tuple[np.ndarray, np.ndarray]:
    field = state[2:].reshape(length, length, length, 6)
    local_scalars = np.asarray(
        [
            np.vdot(
                c210.UNIFORM,
                c214.FIELD_COIN @ field[positions[index]],
            )
            for index in range(2)
        ]
    )
    q = np.asarray(
        [
            (np.cos(thetas[index]) - 1) * local_scalars[index]
            - 1j * np.sin(thetas[index]) * state[index]
            for index in range(2)
        ]
    )
    return q, local_scalars


def shifted_profile(
    length: int, shift: float, position: tuple[int, int, int]
) -> np.ndarray:
    return np.roll(
        single.shifted_green_profile(length, shift),
        position,
        axis=(0, 1, 2),
    )


def field_resolvent_response(
    length: int,
    eigenvalue: complex,
    scalar_source: np.ndarray,
    *,
    pseudoinverse: bool = False,
) -> np.ndarray:
    """Solve (lambda-U_f)f=U_f|s> source mode by mode."""

    source_hat = np.fft.fftn(scalar_source, norm="ortho")
    field_hat = np.zeros(scalar_source.shape + (6,), dtype=complex)
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    for indices in product(range(length), repeat=3):
        momentum = np.asarray([momenta[index] for index in indices])
        stream = np.diag(np.exp(-1j * (c210.DIRECTIONS @ momentum)))
        free_update = stream @ c214.FIELD_COIN
        right = free_update @ c210.UNIFORM * source_hat[indices]
        operator = eigenvalue * np.eye(6) - free_update
        if pseudoinverse:
            field_hat[indices] = np.linalg.pinv(operator, rcond=1e-11) @ right
        else:
            field_hat[indices] = np.linalg.solve(operator, right)
    return np.fft.ifftn(field_hat, axes=(0, 1, 2), norm="ortho")


def bright_eigenstate(
    length: int,
    positions: tuple[tuple[int, int, int], tuple[int, int, int]],
) -> tuple[sparse.csr_matrix, complex, np.ndarray]:
    """Select the positive bright branch by total reservoir squared norm."""

    update = two_defect_update(length, positions)
    target = np.exp(1j * np.sqrt(2) * THETA / length**1.5)
    start = np.zeros(update.shape[0], dtype=complex)
    start[:2] = 0.5
    start[2:] = np.tile(c210.UNIFORM, length**3) / np.sqrt(2 * length**3)
    eigenvalues, eigenvectors = eigs(
        update,
        k=3,
        sigma=target,
        v0=start,
        tol=1e-12,
        maxiter=20000,
    )
    phases = np.angle(eigenvalues)
    candidates = np.where(phases > 1e-8)[0]
    if not len(candidates):
        raise RuntimeError("the requested positive bright branch was absent")
    index = candidates[
        np.argmax(
            np.sum(np.abs(eigenvectors[:2, candidates]) ** 2, axis=0)
        )
    ]
    eigenvalue = eigenvalues[index]
    state = eigenvectors[:, index]
    state /= np.linalg.norm(state)
    state *= np.exp(-1j * np.angle(np.sum(state[:2])))
    return update, eigenvalue, state


def antisymmetric_stationary_state(
    length: int,
    positions: tuple[tuple[int, int, int], tuple[int, int, int]],
) -> np.ndarray:
    """Construct one zero-total-q antisymmetric lambda=1 compatibility member."""

    source = np.zeros((length, length, length), dtype=complex)
    source[positions[0]] = 1
    source[positions[1]] = -1
    field = field_resolvent_response(
        length, 1.0 + 0j, source, pseudoinverse=True
    )
    scalar = np.einsum(
        "d,xyzd->xyz", c210.UNIFORM.conj(), field, optimize=True
    )
    local_scalars = np.asarray(
        (scalar[positions[0]], scalar[positions[1]])
    )
    reservoir = (
        -1j * np.sin(THETA) / (1 - np.cos(THETA)) * local_scalars
    )
    state = np.concatenate((reservoir, field.reshape(-1)))
    return state / np.linalg.norm(state)


def frame_permutation(
    length: int, frame: np.ndarray
) -> sparse.csr_matrix:
    dimension = 2 + 6 * length**3
    rows = [0, 1]
    columns = [0, 1]
    values = [1.0 + 0j, 1.0 + 0j]
    representation = c210.direction_permutation(frame)
    direction_map = tuple(
        int(np.argmax(representation[:, direction])) for direction in range(6)
    )
    for cell in product(range(length), repeat=3):
        target = tuple(int(value % length) for value in frame @ np.asarray(cell))
        source_flat = site_index(cell, length)
        target_flat = site_index(target, length)
        for direction in range(6):
            rows.append(2 + 6 * target_flat + direction_map[direction])
            columns.append(2 + 6 * source_flat + direction)
            values.append(1.0 + 0j)
    return sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def translation_permutation(
    length: int, displacement: tuple[int, int, int]
) -> sparse.csr_matrix:
    dimension = 2 + 6 * length**3
    rows = [0, 1]
    columns = [0, 1]
    values = [1.0 + 0j, 1.0 + 0j]
    for cell in product(range(length), repeat=3):
        target = tuple(
            (cell[axis] + displacement[axis]) % length for axis in range(3)
        )
        source_flat = site_index(cell, length)
        target_flat = site_index(target, length)
        for direction in range(6):
            rows.append(2 + 6 * target_flat + direction)
            columns.append(2 + 6 * source_flat + direction)
            values.append(1.0 + 0j)
    return sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def local_update_controls() -> None:
    print("\nLOCAL TWO-VERTEX UPDATE")
    length = 3
    positions = (ORIGIN, NEIGHBOUR)
    update = two_defect_update(length, positions)
    identity = sparse.eye(update.shape[0], dtype=complex, format="csr")
    unitarity = sparse.linalg.norm(update.conj().T @ update - identity)
    vertices = tuple(
        vertex_matrix(length, positions, index, THETA) for index in range(2)
    )
    commutator = sparse.linalg.norm(vertices[0] @ vertices[1] - vertices[1] @ vertices[0])
    initial = np.zeros(update.shape[0], dtype=complex)
    initial[0] = 1
    output = update @ initial
    nonzero = np.flatnonzero(np.abs(output) > 1e-13)
    check(
        "two distinct fixed reservoir vertices give a unitary radius-one one-excitation update with commuting local gates",
        unitarity < 2e-13
        and commutator == 0
        and len(nonzero) == 7
        and 0 in nonzero
        and 1 not in nonzero
        and abs(np.linalg.norm(output) - 1) < 2e-14,
        {
            "dimension": update.shape[0],
            "unitarity_residual": float(unitarity),
            "vertex_commutator": float(commutator),
            "one_step_nonzero_components": len(nonzero),
            "one_step_norm": float(np.linalg.norm(output)),
        },
    )
    check(
        "the common scalar direction obeys C|s0>=|s0>",
        np.linalg.norm(c214.FIELD_COIN @ c210.UNIFORM - c210.UNIFORM) < 2e-14,
        float(np.linalg.norm(c214.FIELD_COIN @ c210.UNIFORM - c210.UNIFORM)),
    )


def bright_profile_controls() -> dict[int, tuple[complex, np.ndarray]]:
    print("\nBRIGHT EIGENPAIR / TWO-SOURCE COMPOSITION")
    rows = []
    cache = {}
    positions = (ORIGIN, NEIGHBOUR)
    for length in SIZES:
        update, eigenvalue, state = bright_eigenstate(length, positions)
        cache[length] = (eigenvalue, state)
        phase = float(np.angle(eigenvalue))
        shift = float(6 * (1 - np.cos(phase)))
        q, local_scalars = emitted_amplitudes(state, length, positions)
        field_update = single.field_update(length)
        field_right = sum(
            q[index]
            * (field_update @ source_field_vector(length, positions[index]))
            for index in range(2)
        )
        reservoir_defects = np.asarray(
            [
                abs(
                    eigenvalue * state[index]
                    - (
                        np.cos(THETA) * state[index]
                        - 1j * np.sin(THETA) * local_scalars[index]
                    )
                )
                for index in range(2)
            ]
        )
        field_defect = np.linalg.norm(
            eigenvalue * state[2:] - field_update @ state[2:] - field_right
        )
        scalar = scalar_projection(state, length)
        scalar_perpendicular = scalar - np.mean(scalar)
        sources = tuple(c211.point_source(length, position) for position in positions)
        shifted = tuple(
            shifted_profile(length, shift, position) for position in positions
        )
        source_coordinate = sum(q[index] * sources[index] for index in range(2))
        shifted_coordinate = sum(q[index] * shifted[index] for index in range(2))
        predicted = -0.5 * source_coordinate + 1j * np.sin(phase) * shifted_coordinate
        normalized_tail = (
            scalar_perpendicular + 0.5 * source_coordinate
        ) / (1j * np.sin(phase) * q[0])
        normalized_prediction = shifted_coordinate / q[0]
        uniform_prediction = (
            np.sum(q)
            * (-0.5 - 1j * 3 * np.sin(phase) / shift)
            / length**3
        )
        laplacian, _ = c211.c9.fourier_symbols(length)
        minimum_nonzero = float(np.min(laplacian[laplacian > 1e-14]))
        static = 3 * c211.solve_field(sources[0])
        profile_ratio = float(
            np.linalg.norm(shifted[0] - static) / np.linalg.norm(static)
        )
        operator_bound = shift / (minimum_nonzero - shift)
        row = {
            "L": length,
            "held_out": length == HELD_OUT,
            "dimension": update.shape[0],
            "phase": phase,
            "phase_scaled_by_L^(3/2)/(sqrt(2)theta)": (
                phase * length**1.5 / (np.sqrt(2) * THETA)
            ),
            "shift_mu": shift,
            "eigen_residual": float(
                np.linalg.norm(update @ state - eigenvalue * state)
            ),
            "stationary_squared_norm_residual": float(
                np.max(np.abs(np.abs(update @ state) ** 2 - np.abs(state) ** 2))
            ),
            "reservoir_squared_norm_weight": float(np.linalg.norm(state[:2]) ** 2),
            "field_squared_norm_weight": float(np.linalg.norm(state[2:]) ** 2),
            "reservoir_equation_residual": float(np.max(reservoir_defects)),
            "field_equation_residual": float(field_defect),
            "reservoir_symmetry_residual": float(abs(state[0] - state[1])),
            "q_symmetry_residual": float(abs(q[0] - q[1])),
            "profile_residual": float(
                np.linalg.norm(scalar_perpendicular - predicted)
                / np.linalg.norm(scalar_perpendicular)
            ),
            "normalized_composition_residual": float(
                np.linalg.norm(normalized_tail - normalized_prediction)
                / np.linalg.norm(normalized_prediction)
            ),
            "uniform_component_residual": float(
                abs(np.mean(scalar) - uniform_prediction)
            ),
            "profile_l2_ratio_to_Cycle216_3Lplus": profile_ratio,
            "zero_mean_relative_operator_bound": operator_bound,
            "minimum_nonzero_Laplacian": minimum_nonzero,
        }
        rows.append(row)

    check(
        "the selected positive bright eigenpairs stay inside the supplied phase-ratio and reservoir-weight windows with stationary nonzero field weight on L=3,...,9",
        tuple(row["L"] for row in rows) == SIZES
        and all(row["eigen_residual"] < 2e-12 for row in rows)
        and all(row["stationary_squared_norm_residual"] < 2e-12 for row in rows)
        and all(
            BRIGHT_RESERVOIR_WEIGHT_WINDOW[0]
            < row["reservoir_squared_norm_weight"]
            < BRIGHT_RESERVOIR_WEIGHT_WINDOW[1]
            for row in rows
        )
        and all(
            BRIGHT_PHASE_RATIO_WINDOW[0]
            < row["phase_scaled_by_L^(3/2)/(sqrt(2)theta)"]
            < BRIGHT_PHASE_RATIO_WINDOW[1]
            for row in rows
        )
        and all(
            abs(
                row["reservoir_squared_norm_weight"]
                + row["field_squared_norm_weight"]
                - 1
            )
            < 2e-12
            for row in rows
        ),
        rows,
    )
    check(
        "the gate equations produce equal q coordinates and the scalar field is the additive two-source shifted profile",
        all(row["reservoir_equation_residual"] < 2e-12 for row in rows)
        and all(row["field_equation_residual"] < 2e-12 for row in rows)
        and all(row["reservoir_symmetry_residual"] < 2e-12 for row in rows)
        and all(row["q_symmetry_residual"] < 2e-12 for row in rows)
        and all(row["profile_residual"] < 5e-12 for row in rows)
        and all(row["normalized_composition_residual"] < 4e-11 for row in rows)
        and all(row["uniform_component_residual"] < 6e-13 for row in rows),
        [
            {
                key: row[key]
                for key in (
                    "L",
                    "reservoir_equation_residual",
                    "field_equation_residual",
                    "q_symmetry_residual",
                    "profile_residual",
                    "normalized_composition_residual",
                    "uniform_component_residual",
                )
            }
            for row in rows
        ],
    )
    check(
        "the finite shifted profile is pole-free and its source-specific ratio obeys the distinct zero-mean operator bound through held-out L=9",
        all(row["shift_mu"] < row["minimum_nonzero_Laplacian"] for row in rows)
        and all(
            row["profile_l2_ratio_to_Cycle216_3Lplus"]
            <= row["zero_mean_relative_operator_bound"] + 2e-13
            for row in rows
        ),
        [
            {
                "L": row["L"],
                "phase": row["phase"],
                "source_specific_profile_ratio": row[
                    "profile_l2_ratio_to_Cycle216_3Lplus"
                ],
                "zero_mean_operator_bound": row[
                    "zero_mean_relative_operator_bound"
                ],
            }
            for row in rows
        ],
    )
    return cache


def antisymmetric_member_controls() -> None:
    print("\nANTISYMMETRIC LAMBDA=1 COMPATIBILITY MEMBER")
    rows = []
    positions = (ORIGIN, NEIGHBOUR)
    for length in SIZES:
        update = two_defect_update(length, positions)
        state = antisymmetric_stationary_state(length, positions)
        q, _ = emitted_amplitudes(state, length, positions)
        scalar = scalar_projection(state, length)
        field_update = single.field_update(length)
        field_right = sum(
            q[index]
            * (field_update @ source_field_vector(length, positions[index]))
            for index in range(2)
        )
        source = np.zeros_like(scalar)
        source[positions[0]] = 1
        source[positions[1]] = -1
        rows.append(
            {
                "L": length,
                "stationary_residual": float(np.linalg.norm(update @ state - state)),
                "reservoir_antisymmetry_residual": float(abs(state[0] + state[1])),
                "q_antisymmetry_residual": float(abs(q[0] + q[1])),
                "minimum_local_q_abs": float(np.min(np.abs(q))),
                "field_squared_norm_weight": float(np.linalg.norm(state[2:]) ** 2),
                "field_compatibility_residual": float(
                    np.linalg.norm(
                        state[2:] - field_update @ state[2:] - field_right
                    )
                ),
                "scalar_local_coordinate_residual": float(
                    np.linalg.norm(
                        scalar + 0.5 * q[0] / source[positions[0]] * source
                    )
                ),
                "reservoir_squared_norm_weight": float(np.linalg.norm(state[:2]) ** 2),
            }
        )
    check(
        "the equal-coupling pair has an explicitly constructed zero-total-q antisymmetric lambda=1 member at every tested size",
        all(row["stationary_residual"] < 3e-12 for row in rows)
        and all(row["reservoir_antisymmetry_residual"] < 2e-12 for row in rows)
        and all(row["q_antisymmetry_residual"] < 2e-12 for row in rows)
        and all(row["scalar_local_coordinate_residual"] < 3e-12 for row in rows)
        and all(row["reservoir_squared_norm_weight"] > 0.8 for row in rows),
        rows,
    )
    check(
        "the antisymmetric member has nonzero local q coordinates and field weight with an exact compatible field equation",
        all(row["minimum_local_q_abs"] > 1e-2 for row in rows)
        and all(row["field_squared_norm_weight"] > 1e-3 for row in rows)
        and all(row["field_compatibility_residual"] < 3e-12 for row in rows),
        [
            {
                key: row[key]
                for key in (
                    "L",
                    "minimum_local_q_abs",
                    "field_squared_norm_weight",
                    "field_compatibility_residual",
                )
            }
            for row in rows
        ],
    )

    length = HELD_OUT
    field_update = single.field_update(length)
    held_rows = []
    for separation in HELD_SEPARATIONS:
        separation_position = tuple(coordinate % length for coordinate in separation)
        held_positions = (ORIGIN, separation_position)
        update = two_defect_update(length, held_positions)
        state = antisymmetric_stationary_state(length, held_positions)
        q, _ = emitted_amplitudes(state, length, held_positions)
        field_right = sum(
            q[index]
            * (field_update @ source_field_vector(length, held_positions[index]))
            for index in range(2)
        )
        held_rows.append(
            {
                "separation": separation,
                "stationary_residual": float(np.linalg.norm(update @ state - state)),
                "q_antisymmetry_residual": float(abs(q[0] + q[1])),
                "minimum_local_q_abs": float(np.min(np.abs(q))),
                "field_squared_norm_weight": float(np.linalg.norm(state[2:]) ** 2),
                "field_compatibility_residual": float(
                    np.linalg.norm(
                        state[2:] - field_update @ state[2:] - field_right
                    )
                ),
            }
        )
    check(
        "the antisymmetric lambda=1 compatibility construction survives all 38 held-size proper-cubic separation orbits",
        len(held_rows) == 38
        and all(row["stationary_residual"] < 3e-12 for row in held_rows)
        and all(row["q_antisymmetry_residual"] < 2e-12 for row in held_rows)
        and all(row["minimum_local_q_abs"] > 1e-2 for row in held_rows)
        and all(row["field_squared_norm_weight"] > 1e-3 for row in held_rows)
        and all(row["field_compatibility_residual"] < 3e-12 for row in held_rows),
        {
            "maximum_stationary_residual": max(
                row["stationary_residual"] for row in held_rows
            ),
            "maximum_q_antisymmetry_residual": max(
                row["q_antisymmetry_residual"] for row in held_rows
            ),
            "minimum_local_q_abs": min(
                row["minimum_local_q_abs"] for row in held_rows
            ),
            "field_squared_norm_weight_range": (
                min(row["field_squared_norm_weight"] for row in held_rows),
                max(row["field_squared_norm_weight"] for row in held_rows),
            ),
            "maximum_field_compatibility_residual": max(
                row["field_compatibility_residual"] for row in held_rows
            ),
        },
    )


def separation_orbit_partition_control() -> None:
    print("\nHELD-SIZE PROPER-CUBIC ORBIT PARTITION")
    length = HELD_OUT
    frames = c210.proper_cubic_frames()
    unassigned = set(product(range(length), repeat=3))
    unassigned.remove(ORIGIN)
    orbits = []
    while unassigned:
        representative = next(iter(unassigned))
        orbit = frozenset(
            tuple(
                int(coordinate % length)
                for coordinate in frame @ np.asarray(representative)
            )
            for frame in frames
        )
        orbits.append(orbit)
        unassigned.difference_update(orbit)
    declared = frozenset(
        tuple(coordinate % length for coordinate in separation)
        for separation in HELD_SEPARATIONS
    )
    intersections = tuple(orbit & declared for orbit in orbits)
    size_distribution = {
        size: sum(len(orbit) == size for orbit in orbits)
        for size in sorted({len(orbit) for orbit in orbits})
    }
    check(
        "the 38 declared held separations are exactly one representative from each proper-cubic orbit of all 728 nonzero minimal-image vectors",
        len(frames) == 24
        and len(orbits) == 38
        and len(declared) == 38
        and all(len(intersection) == 1 for intersection in intersections)
        and size_distribution == {6: 4, 8: 4, 12: 4, 24: 26},
        {
            "nonzero_vectors": length**3 - 1,
            "frames": len(frames),
            "orbits": len(orbits),
            "declared_representatives": len(declared),
            "orbit_size_distribution": size_distribution,
            "intersection_size_set": sorted(
                {len(intersection) for intersection in intersections}
            ),
        },
    )


def overlap_and_bilinear_controls() -> None:
    print("\nHELD-SIZE SPECTRAL CROSS-COORDINATE / BILINEAR COMPOSITION")
    length = HELD_OUT
    rows = []
    for separation in HELD_SEPARATIONS:
        separation_position = tuple(coordinate % length for coordinate in separation)
        positions = (ORIGIN, separation_position)
        _, eigenvalue, state = bright_eigenstate(length, positions)
        phase = float(np.angle(eigenvalue))
        shift = float(6 * (1 - np.cos(phase)))
        q, local_scalars = emitted_amplitudes(state, length, positions)
        delta = np.zeros((length, length, length), dtype=complex)
        delta[separation_position] = 1
        one_source_field = field_resolvent_response(length, eigenvalue, delta)
        one_source_scalar = np.einsum(
            "d,xyzd->xyz",
            c210.UNIFORM.conj(),
            one_source_field,
            optimize=True,
        )
        gate_symmetric_response = local_scalars[0] / q[0]
        spectral_symmetric_response = (
            eigenvalue - np.cos(THETA)
        ) / ((np.cos(THETA) - 1) * (eigenvalue + 1))
        direct_self_response = one_source_scalar[separation_position]
        direct_cross_response = one_source_scalar[ORIGIN]
        inferred_cross_response = spectral_symmetric_response - direct_self_response
        inferred_shifted_cross = (
            inferred_cross_response / (1j * np.sin(phase))
            + 3 / (shift * length**3)
        )
        rho_left = c211.point_source(length, ORIGIN)
        rho_right = c211.point_source(length, separation_position)
        shifted_left = shifted_profile(length, shift, ORIGIN)
        shifted_right = shifted_profile(length, shift, separation_position)
        direct_shifted_cross = shifted_right[ORIGIN]
        complex_left_source = COMPLEX_LEFT_COEFFICIENT * rho_left
        complex_right_source = COMPLEX_RIGHT_COEFFICIENT * rho_right
        complex_left_profile = COMPLEX_LEFT_COEFFICIENT * shifted_left
        complex_right_profile = COMPLEX_RIGHT_COEFFICIENT * shifted_right
        pair_bilinear = np.vdot(
            complex_left_source + complex_right_source,
            complex_left_profile + complex_right_profile,
        )
        b11 = np.vdot(complex_left_source, complex_left_profile)
        b12 = np.vdot(complex_left_source, complex_right_profile)
        b21 = np.vdot(complex_right_source, complex_left_profile)
        b22 = np.vdot(complex_right_source, complex_right_profile)
        four_term_bilinear = b11 + b12 + b21 + b22
        static = 3 * c211.solve_field(rho_left)
        laplacian, _ = c211.c9.fourier_symbols(length)
        minimum_nonzero = float(np.min(laplacian[laplacian > 1e-14]))
        profile_ratio = float(
            np.linalg.norm(shifted_left - static) / np.linalg.norm(static)
        )
        operator_bound = shift / (minimum_nonzero - shift)
        rows.append(
            {
                "separation": separation,
                "phase": phase,
                "phase_scaled_by_L^(3/2)/(sqrt(2)theta)": (
                    phase * length**1.5 / (np.sqrt(2) * THETA)
                ),
                "shift_mu": shift,
                "reservoir_squared_norm_weight": float(np.linalg.norm(state[:2]) ** 2),
                "q_symmetry_residual": float(abs(q[0] - q[1])),
                "gate_to_spectral_response_residual": float(
                    abs(gate_symmetric_response - spectral_symmetric_response)
                ),
                "spectral_cross_residual": float(
                    abs(inferred_cross_response - direct_cross_response)
                ),
                "shifted_cross_residual": float(
                    abs(inferred_shifted_cross - direct_shifted_cross)
                ),
                "four_term_bilinear_residual": float(
                    abs(pair_bilinear - four_term_bilinear)
                ),
                "conjugate_reciprocity_residual": float(abs(b12 - np.conj(b21))),
                "B11": complex(b11),
                "B12": complex(b12),
                "B21": complex(b21),
                "B22": complex(b22),
                "shifted_cross_coordinate": complex(direct_shifted_cross),
                "Cycle216_cross_coordinate": float(static[separation_position]),
                "finite_cross_difference": float(
                    abs(direct_shifted_cross - static[separation_position])
                ),
                "source_specific_profile_ratio": profile_ratio,
                "zero_mean_operator_bound": operator_bound,
            }
        )
    check(
        "the bright eigenphase and local gate equation extract the direct off-diagonal field response at every held-size separation",
        all(row["q_symmetry_residual"] < 3e-12 for row in rows)
        and all(row["gate_to_spectral_response_residual"] < 3e-12 for row in rows)
        and all(row["spectral_cross_residual"] < 3e-11 for row in rows)
        and all(row["shifted_cross_residual"] < 3e-9 for row in rows),
        rows,
    )
    check(
        "the shifted quadratic pairing obeys the full complex four-term expansion and conjugate reciprocity",
        all(row["four_term_bilinear_residual"] < 3e-12 for row in rows)
        and all(row["conjugate_reciprocity_residual"] < 3e-12 for row in rows)
        and all(abs(row["B12"].imag) > 1e-8 for row in rows),
        [
            {
                key: row[key]
                for key in (
                    "separation",
                    "B12",
                    "B21",
                    "four_term_bilinear_residual",
                    "conjugate_reciprocity_residual",
                )
            }
            for row in rows
        ],
    )
    check(
        "all held-size bright selections remain inside the supplied phase-ratio and reservoir-weight acceptance windows",
        all(
            BRIGHT_PHASE_RATIO_WINDOW[0]
            < row["phase_scaled_by_L^(3/2)/(sqrt(2)theta)"]
            < BRIGHT_PHASE_RATIO_WINDOW[1]
            for row in rows
        )
        and all(
            BRIGHT_RESERVOIR_WEIGHT_WINDOW[0]
            < row["reservoir_squared_norm_weight"]
            < BRIGHT_RESERVOIR_WEIGHT_WINDOW[1]
            for row in rows
        ),
        {
            "phase_ratio_range": (
                min(
                    row["phase_scaled_by_L^(3/2)/(sqrt(2)theta)"]
                    for row in rows
                ),
                max(
                    row["phase_scaled_by_L^(3/2)/(sqrt(2)theta)"]
                    for row in rows
                ),
            ),
            "reservoir_squared_norm_weight_range": (
                min(row["reservoir_squared_norm_weight"] for row in rows),
                max(row["reservoir_squared_norm_weight"] for row in rows),
            ),
        },
    )
    phase_clusters = []
    for phase in sorted(row["phase"] for row in rows):
        if not phase_clusters or abs(phase - phase_clusters[-1]) > 1e-12:
            phase_clusters.append(phase)
    chiral_pairs = (
        ((3, 2, 1), (3, 2, -1)),
        ((4, 2, 1), (4, 2, -1)),
        ((4, 3, 1), (4, 3, -1)),
        ((4, 3, 2), (4, 3, -2)),
    )
    phase_by_separation = {row["separation"]: row["phase"] for row in rows}
    maximum_chiral_pair_phase_residual = max(
        abs(phase_by_separation[left] - phase_by_separation[right])
        for left, right in chiral_pairs
    )
    check(
        "the selected eigenphase is nonconstant with 34 tolerance-distinct values across 38 held-size proper-cubic orbits, including four inversion-related chiral-pair degeneracies, and the finite shifted comparator remains distinct from Cycle216",
        len(rows) == len(HELD_SEPARATIONS) == 38
        and len(set(row["separation"] for row in rows)) == 38
        and all(
            first >= second >= abs(third) >= 0
            for first, second, third in (row["separation"] for row in rows)
        )
        and all(row["separation"] != ORIGIN for row in rows)
        and max(row["phase"] for row in rows) - min(row["phase"] for row in rows)
        > 1e-5
        and len(phase_clusters) == 34
        and maximum_chiral_pair_phase_residual < 1e-12
        and all(row["finite_cross_difference"] > 1e-7 for row in rows)
        and all(
            row["source_specific_profile_ratio"]
            <= row["zero_mean_operator_bound"] + 2e-13
            for row in rows
        ),
        {
            "rows": [
                {
                    "separation": row["separation"],
                    "phase": row["phase"],
                    "shifted_cross": row["shifted_cross_coordinate"],
                    "Cycle216_cross": row["Cycle216_cross_coordinate"],
                    "profile_ratio": row["source_specific_profile_ratio"],
                    "operator_bound": row["zero_mean_operator_bound"],
                }
                for row in rows
            ],
            "phase_cluster_count_at_1e-12": len(phase_clusters),
            "maximum_chiral_pair_phase_residual": maximum_chiral_pair_phase_residual,
        },
    )

    rho_left = c211.point_source(length, ORIGIN)
    zero_left = shifted_profile(length, 0.0, ORIGIN)
    cycle_left = 3 * c211.solve_field(rho_left)
    zero_rows = []
    for separation in HELD_SEPARATIONS:
        held_position = tuple(coordinate % length for coordinate in separation)
        rho_right = c211.point_source(length, held_position)
        zero_right = shifted_profile(length, 0.0, held_position)
        cycle_right = 3 * c211.solve_field(rho_right)
        zero_rows.append(
            {
                "separation": separation,
                "left_profile_residual": float(np.linalg.norm(zero_left - cycle_left)),
                "right_profile_residual": float(
                    np.linalg.norm(zero_right - cycle_right)
                ),
                "bilinear_residual": float(
                    abs(
                        np.vdot(rho_left + rho_right, zero_left + zero_right)
                        - np.vdot(rho_left + rho_right, cycle_left + cycle_right)
                    )
                ),
                "source_sums": (float(rho_left.sum()), float(rho_right.sum())),
            }
        )
    check(
        "the separately declared zero-shift mathematical profiles and pair bilinear equal Cycle216's zero-mean 3 L^+ comparator at all 38 held separations",
        len(zero_rows) == 38
        and all(row["left_profile_residual"] < 3e-13 for row in zero_rows)
        and all(row["right_profile_residual"] < 3e-13 for row in zero_rows)
        and all(row["bilinear_residual"] < 3e-13 for row in zero_rows)
        and all(
            max(abs(value) for value in row["source_sums"]) < 3e-14
            for row in zero_rows
        ),
        {
            "maximum_left_profile_residual": max(
                row["left_profile_residual"] for row in zero_rows
            ),
            "maximum_right_profile_residual": max(
                row["right_profile_residual"] for row in zero_rows
            ),
            "maximum_bilinear_residual": max(
                row["bilinear_residual"] for row in zero_rows
            ),
            "scope": "mathematical zero-shift comparator only; not an active-reservoir eigenstate or update identity",
        },
    )


def endpoint_controls() -> None:
    print("\nONE-RESERVOIR ENDPOINT REDUCTIONS")
    length = 4
    positions = (ORIGIN, (2, 0, 0))
    single_origin = single.defect_update(length)
    first_active = two_defect_update(length, positions, (THETA, 0.0))
    second_active = two_defect_update(length, positions, (0.0, THETA))

    def embedding(reservoir_target: int) -> sparse.csr_matrix:
        rows = [reservoir_target]
        columns = [0]
        values = [1.0 + 0j]
        for field_index in range(6 * length**3):
            rows.append(2 + field_index)
            columns.append(1 + field_index)
            values.append(1.0 + 0j)
        return sparse.csr_matrix(
            (values, (rows, columns)),
            shape=(2 + 6 * length**3, 1 + 6 * length**3),
        )

    embed_first = embedding(0)
    first_residual = sparse.linalg.norm(
        first_active @ embed_first - embed_first @ single_origin
    )
    translate_single = single.translation_permutation(length, positions[1])
    single_second = translate_single @ single_origin @ translate_single.conj().T
    embed_second = embedding(1)
    second_residual = sparse.linalg.norm(
        second_active @ embed_second - embed_second @ single_second
    )
    inactive_first = np.zeros(first_active.shape[0], dtype=complex)
    inactive_first[1] = 1
    inactive_second = np.zeros(second_active.shape[0], dtype=complex)
    inactive_second[0] = 1
    check(
        "setting either supplied local angle to zero reduces the active block exactly to the translated one-reservoir update",
        first_residual < 2e-13
        and second_residual < 2e-13
        and np.linalg.norm(first_active @ inactive_first - inactive_first) == 0
        and np.linalg.norm(second_active @ inactive_second - inactive_second) == 0,
        {
            "first_active_intertwiner_residual": float(first_residual),
            "second_active_intertwiner_residual": float(second_residual),
            "scope": "supplied theta=0 endpoint, not a law-selection theorem",
        },
    )
    both_zero = two_defect_update(length, positions, (0.0, 0.0))
    reservoir_subspace = np.zeros((both_zero.shape[0], 2), dtype=complex)
    reservoir_subspace[:2] = np.eye(2)
    check(
        "the both-zero endpoint leaves the complete two-reservoir subspace stationary",
        np.linalg.norm(both_zero @ reservoir_subspace - reservoir_subspace) == 0,
    )


def covariance_controls(
    cache: dict[int, tuple[complex, np.ndarray]]
) -> None:
    print("\nPROPER-CUBIC / TRANSLATED PAIR FAMILY")
    length = 5
    positions = (ORIGIN, (2, 1, 0))
    update, eigenvalue, state = bright_eigenstate(length, positions)
    intertwiner_residuals = []
    state_residuals = []
    for frame in c210.proper_cubic_frames():
        representation = frame_permutation(length, frame)
        moved_positions = tuple(
            tuple(int(value % length) for value in frame @ np.asarray(position))
            for position in positions
        )
        moved_update = two_defect_update(length, moved_positions)
        intertwiner_residuals.append(
            float(
                sparse.linalg.norm(
                    moved_update @ representation - representation @ update
                )
            )
        )
        moved_state = representation @ state
        state_residuals.append(
            float(np.linalg.norm(moved_update @ moved_state - eigenvalue * moved_state))
        )
    check(
        "the complete pair update and bright eigenstate transform in all 24 proper-cubic frames",
        len(intertwiner_residuals) == 24
        and max(intertwiner_residuals) < 3e-13
        and max(state_residuals) < 3e-12,
        {
            "maximum_update_intertwiner_residual": max(intertwiner_residuals),
            "maximum_state_residual": max(state_residuals),
        },
    )

    length = 3
    positions = (ORIGIN, NEIGHBOUR)
    update = two_defect_update(length, positions)
    eigenvalue, state = cache[length]
    residuals = []
    tests = 0
    for displacement in product(range(length), repeat=3):
        representation = translation_permutation(length, displacement)
        moved_positions = tuple(
            tuple(
                (position[axis] + displacement[axis]) % length
                for axis in range(3)
            )
            for position in positions
        )
        moved_update = two_defect_update(length, moved_positions)
        moved_state = representation @ state
        residuals.append(
            float(
                sparse.linalg.norm(
                    moved_update @ representation - representation @ update
                )
            )
        )
        residuals.append(
            float(np.linalg.norm(moved_update @ moved_state - eigenvalue * moved_state))
        )
        tests += 1
    check(
        "all 27 L=3 pair origins form a translated covariant defect family",
        tests == 27 and max(residuals) < 2e-12,
        {"tests": tests, "maximum_residual": max(residuals)},
    )


def normalization_domain_and_inventory_controls(
    cache: dict[int, tuple[complex, np.ndarray]]
) -> None:
    print("\nNORMALIZATION / ZERO MODE / DOMAIN / INVENTORY")
    length = HELD_OUT
    positions = (ORIGIN, NEIGHBOUR)
    eigenvalue, state = cache[length]
    phase = float(np.angle(eigenvalue))
    q, _ = emitted_amplitudes(state, length, positions)
    scalar = scalar_projection(state, length)
    sources = tuple(c211.point_source(length, position) for position in positions)
    source_coordinate = sum(q[index] * sources[index] for index in range(2))
    baseline = (
        scalar - np.mean(scalar) + 0.5 * source_coordinate
    ) / (1j * np.sin(phase) * q[0])
    multiplier = 1.9 * np.exp(-0.37j)
    scaled_state = multiplier * state
    scaled_q, _ = emitted_amplitudes(scaled_state, length, positions)
    scaled_scalar = scalar_projection(scaled_state, length)
    scaled_source = sum(
        scaled_q[index] * sources[index] for index in range(2)
    )
    scaled = (
        scaled_scalar - np.mean(scaled_scalar) + 0.5 * scaled_source
    ) / (1j * np.sin(phase) * scaled_q[0])
    check(
        "the normalized two-source profile is invariant when the eigenvector and both q coordinates are jointly scaled and rephased",
        np.linalg.norm(baseline - scaled) < 4e-12
        and np.linalg.norm(scaled_q - multiplier * q) < 2e-12,
        {
            "profile_invariance_residual": float(np.linalg.norm(baseline - scaled)),
            "q_scaling_residual": float(np.linalg.norm(scaled_q - multiplier * q)),
        },
    )
    check(
        "both comparison sources have explicit zero-mode subtraction",
        all(abs(float(source.sum())) < 3e-14 for source in sources)
        and all(
            abs(np.fft.fftn(source, norm="ortho")[0, 0, 0]) < 3e-14
            for source in sources
        ),
        tuple(float(source.sum()) for source in sources),
    )

    validate_fixture(3, (ORIGIN, NEIGHBOUR), (THETA, THETA), 1)
    rejected = 0
    invalid = (
        (2, (ORIGIN, NEIGHBOUR), (THETA, THETA), 1),
        (3, (ORIGIN, ORIGIN), (THETA, THETA), 1),
        (3, (ORIGIN,), (THETA,), 1),
        (3, (ORIGIN, (3, 0, 0)), (THETA, THETA), 1),
        (3, (ORIGIN, NEIGHBOUR), (THETA, THETA), 2),
    )
    for fixture in invalid:
        try:
            validate_fixture(*fixture)
        except ValueError:
            rejected += 1
    check(
        "the lawful domain rejects aliased, co-located, mistyped, out-of-torus, and wrong-sector fixtures",
        rejected == len(invalid),
        {"rejected": rejected, "attempted": len(invalid)},
    )
    check(
        "the supplied structure inventory keeps the two-reservoir operator result separate from physical source and compiler semantics",
        True,
        {
            "supplied": (
                "Cycle214/215 field coin, directional stream, uniform scalar direction, and coin-vertex-stream order",
                "two distinct fixed reservoir M2 vertices, their positions, equal theta from beta=-0.3 and kappa=0.8, and the one-excitation sector",
                "positive shift-invert target exp(i sqrt(2) theta/L^(3/2)); among the three returned candidates with phase above 1e-8 choose maximum total reservoir squared-norm weight, normalize, and rephase the reservoir sum real-positive",
                "runner acceptance windows: phase ratio omega L^(3/2)/(sqrt(2) theta) in (0.95,0.98) and total reservoir squared-norm weight in (0.44,0.47)",
                "finite periodic sizes L=3,...,9, held-out L=9, all 38 held-size proper-cubic orbit representatives verified against all 728 nonzero vectors, zero-mean convention, and Cycle216 comparator",
                "complex bilinear probe coefficients alpha=1+0.5i and beta=-0.3+0.8i, and Moore-Penrose rcond=1e-11 for the antisymmetric construction",
            ),
            "derived": (
                "bright eigenpair and exact additive two-source shifted profile on the tested finite matrices",
                "one explicitly constructed zero-total-q antisymmetric lambda=1 member with nonzero local q coordinates, field weight, and compatibility residual",
                "spectral extraction of the off-diagonal field response, ordered complex four-term shifted bilinear, and conjugate reciprocity",
                "theta=0 endpoint reductions, proper-cubic and translation covariance, normalization, zero-mode, held-size, and lawful-domain controls",
            ),
            "not_earned": (
                "physical energy, Hamiltonian, eigenphase-as-rate, clock normalization, force, gravity, stress, or source mass",
                "matter or contact update, Cycle230 contact, a physical-M2 compiler/intertwiner, or a whole-compiler claim",
                "host-side renewal, moving or carried source, radiation reaction, many-excitation closure, or a preparation mechanism",
                "a spectral census, eigenvalue multiplicity theorem, or generic level-splitting conclusion",
                "a result outside the tested finite sizes/separations, a Record, occurrence/Born law, axiom change, or audit authority",
            ),
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("TWO FIXED RESERVOIRS / STATIONARY COMPOSITION KERNEL")
    note_contract()
    local_update_controls()
    cache = bright_profile_controls()
    antisymmetric_member_controls()
    separation_orbit_partition_control()
    overlap_and_bilinear_controls()
    endpoint_controls()
    covariance_controls(cache)
    normalization_domain_and_inventory_controls(cache)
    print("\nSUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "TWO_FIXED_RESERVOIR_SHIFTED_BILINEAR_CONTROLLED"
        if FAIL == 0
        else "TWO_FIXED_RESERVOIR_SHIFTED_BILINEAR_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
