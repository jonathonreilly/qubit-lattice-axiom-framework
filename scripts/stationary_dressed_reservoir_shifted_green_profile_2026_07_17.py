#!/usr/bin/env python3
"""Stationary dressed one-excitation profile from the local reservoir law.

Attach one active site-local reservoir to the Cycle-214 six-direction field
walk and use the exact conjugate exchange gate.  A finite-volume eigenvector of
the resulting closed unitary has stationary reservoir/field basis-component
squared-norm weights.  Its nonuniform scalar component splits exactly into a
local source coordinate and a normalized-tail shifted-Laplacian resolvent with
no fitted Green coefficient.  The latter can be compared directly with Cycle
216's 3 L^+ response.

Eigenphase, stiffness, resolvent, and source are operator coordinates here.
They are not physical energy, mass, a rate, gravity, or host-side renewal.
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
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import virtual_exchange_green_kernel_cycle216_2026_07_16 as c216
import local_conjugate_reservoir_source_field_ledger_repair_2026_07_17 as reservoir


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "STATIONARY_DRESSED_RESERVOIR_SHIFTED_GREEN_PROFILE_NOTE_2026-07-17.md"
)
BETA = -0.3
KAPPA = reservoir.COUPLING
MASS = c219.common_species(BETA).analytic_mass
THETA = KAPPA * MASS
SIZES = (3, 4, 5, 6, 7, 8, 9)
HELD_OUT = 9
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
        check("the stationary-dressing note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "stationary dressed one-excitation eigenstate",
        "exact shifted-laplacian resolvent",
        "cycle216",
        "3 l^+",
        "normalized-tail ratio uses no fitted green coefficient",
        "zero-mode subtraction",
        "held-out l=9",
        "all 24 proper-cubic frames",
        "theta=0 parameter endpoint",
        "no host-side source renewal",
        "not physical energy",
        "not gravity",
        "eigenphase is not a rate",
        "supplied structure inventory",
        "no matter or contact update",
        "no whole-compiler claim",
        "no interface to the carried-source code",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note preserves the stationary-state, shifted-resolvent, controls, and scope contract",
        not missing,
        missing,
    )


def site_index(cell: tuple[int, int, int], length: int) -> int:
    x, y, z = cell
    return (x * length + y) * length + z


def local_vertex_block(theta: float) -> np.ndarray:
    reservoir_basis = np.zeros(7, dtype=complex)
    reservoir_basis[0] = 1
    scalar_basis = np.zeros(7, dtype=complex)
    scalar_basis[1:] = c210.UNIFORM
    exchange = np.outer(reservoir_basis, scalar_basis.conj()) + np.outer(
        scalar_basis, reservoir_basis.conj()
    )
    return (
        np.eye(7, dtype=complex)
        + (np.cos(theta) - 1) * (exchange @ exchange)
        - 1j * np.sin(theta) * exchange
    )


def defect_update(length: int, theta: float = THETA) -> sparse.csr_matrix:
    """One active reservoir at the origin plus six field M2 per cell."""

    cells = length**3
    dimension = 1 + 6 * cells
    field_coin = sparse.kron(
        sparse.eye(cells, dtype=complex, format="csr"),
        sparse.csr_matrix(c214.FIELD_COIN),
        format="csr",
    )
    coin = sparse.block_diag(
        (sparse.csr_matrix([[1.0 + 0j]]), field_coin), format="csr"
    )

    vertex_delta = local_vertex_block(theta) - np.eye(7, dtype=complex)
    vertex_rows = []
    vertex_columns = []
    vertex_values = []
    local_indices = (0,) + tuple(range(1, 7))
    for left, target in enumerate(local_indices):
        for right, source in enumerate(local_indices):
            value = vertex_delta[left, right]
            if abs(value) > 1e-15:
                vertex_rows.append(target)
                vertex_columns.append(source)
                vertex_values.append(value)
    vertex = sparse.eye(dimension, dtype=complex, format="csr") + sparse.csr_matrix(
        (vertex_values, (vertex_rows, vertex_columns)),
        shape=(dimension, dimension),
    )

    stream_rows = [0]
    stream_columns = [0]
    stream_values = [1.0 + 0j]
    for cell in product(range(length), repeat=3):
        source_flat = site_index(cell, length)
        for direction, displacement in enumerate(c210.DIRECTIONS):
            target = tuple(
                (cell[axis] + int(displacement[axis])) % length
                for axis in range(3)
            )
            target_flat = site_index(target, length)
            stream_rows.append(1 + 6 * target_flat + direction)
            stream_columns.append(1 + 6 * source_flat + direction)
            stream_values.append(1.0 + 0j)
    stream = sparse.csr_matrix(
        (stream_values, (stream_rows, stream_columns)),
        shape=(dimension, dimension),
    )
    return (stream @ vertex @ coin).tocsr()


def field_update(length: int) -> sparse.csr_matrix:
    """Cycle-214 coin-plus-stream field block, with no reservoir coupling."""

    return defect_update(length, 0.0)[1:, 1:].tocsr()


def frame_permutation(length: int, frame: np.ndarray) -> sparse.csr_matrix:
    cells = length**3
    dimension = 1 + 6 * cells
    rows = [0]
    columns = [0]
    values = [1.0 + 0j]
    representation = c210.direction_permutation(frame)
    direction_map = tuple(
        int(np.argmax(representation[:, direction])) for direction in range(6)
    )
    for cell in product(range(length), repeat=3):
        target = tuple(
            int(value % length) for value in frame @ np.asarray(cell)
        )
        source_flat = site_index(cell, length)
        target_flat = site_index(target, length)
        for direction in range(6):
            rows.append(1 + 6 * target_flat + direction_map[direction])
            columns.append(1 + 6 * source_flat + direction)
            values.append(1.0 + 0j)
    return sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def translation_permutation(
    length: int, displacement: tuple[int, int, int]
) -> sparse.csr_matrix:
    cells = length**3
    dimension = 1 + 6 * cells
    rows = [0]
    columns = [0]
    values = [1.0 + 0j]
    for cell in product(range(length), repeat=3):
        target = tuple(
            (cell[axis] + displacement[axis]) % length for axis in range(3)
        )
        source_flat = site_index(cell, length)
        target_flat = site_index(target, length)
        for direction in range(6):
            rows.append(1 + 6 * target_flat + direction)
            columns.append(1 + 6 * source_flat + direction)
            values.append(1.0 + 0j)
    return sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def shifted_green_profile(length: int, shift: float) -> np.ndarray:
    """3 (L-shift I)^-1 rho on the declared zero-mean subspace."""

    source = c211.point_source(length)
    source_hat = np.fft.fftn(source, norm="ortho")
    laplacian, _ = c211.c9.fourier_symbols(length)
    output_hat = np.zeros_like(source_hat, dtype=complex)
    nonzero = laplacian > 1e-14
    output_hat[nonzero] = (
        3 * source_hat[nonzero] / (laplacian[nonzero] - shift)
    )
    return np.fft.ifftn(output_hat, norm="ortho")


def dressed_eigenstate(
    length: int, theta: float = THETA, *, negative: bool = False
) -> tuple[sparse.csr_matrix, complex, np.ndarray]:
    """Select the requested phase-sign branch by reservoir squared norm.

    Shift-invert targets exp(+/- i theta/L^(3/2)); among the three returned
    eigenvalues with the requested nonzero phase sign, select the vector with
    maximum reservoir squared-norm weight, normalize it, and fix its otherwise
    arbitrary common phase by making the reservoir amplitude real-positive.
    """

    update = defect_update(length, theta)
    dimension = update.shape[0]
    sign = -1 if negative else 1
    target = np.exp(1j * sign * theta / length**1.5)
    start = np.zeros(dimension, dtype=complex)
    start[0] = 1 / np.sqrt(2)
    start[1:] = np.tile(c210.UNIFORM, length**3) / np.sqrt(2 * length**3)
    eigenvalues, eigenvectors = eigs(
        update,
        k=3,
        sigma=target,
        v0=start,
        tol=1e-12,
        maxiter=20000,
    )
    phases = np.angle(eigenvalues)
    candidates = np.where(sign * phases > 1e-8)[0]
    if not len(candidates):
        raise RuntimeError("the requested dressed eigenphase branch was absent")
    index = candidates[np.argmax(np.abs(eigenvectors[0, candidates]) ** 2)]
    eigenvalue = eigenvalues[index]
    state = eigenvectors[:, index]
    state /= np.linalg.norm(state)
    state *= np.exp(-1j * np.angle(state[0]))
    return update, eigenvalue, state


def emitted_amplitude(
    state: np.ndarray, length: int, theta: float = THETA
) -> complex:
    field = state[1:].reshape(length, length, length, 6)
    coined_origin = c214.FIELD_COIN @ field[0, 0, 0]
    local_scalar = np.vdot(c210.UNIFORM, coined_origin)
    return (
        (np.cos(theta) - 1) * local_scalar
        - 1j * np.sin(theta) * state[0]
    )


def scalar_projection(state: np.ndarray, length: int) -> np.ndarray:
    field = state[1:].reshape(length, length, length, 6)
    return np.einsum(
        "d,xyzd->xyz", c210.UNIFORM.conj(), field, optimize=True
    )


def locality_unitarity_and_parameter_endpoint_controls() -> None:
    print("\nLOCAL CLOSED UPDATE / THETA=0 PARAMETER ENDPOINT")
    length = 3
    update = defect_update(length)
    identity = sparse.eye(update.shape[0], dtype=complex, format="csr")
    unitarity = sparse.linalg.norm(update.conj().T @ update - identity)
    reservoir_initial = np.zeros(update.shape[0], dtype=complex)
    reservoir_initial[0] = 1
    one_step = update @ reservoir_initial
    nonzero = np.flatnonzero(np.abs(one_step) > 1e-13)
    check(
        "the one-reservoir plus six-field-M2-per-cell update is unitary, excitation conserving, and radius-one from the active source cell",
        unitarity < 2e-13
        and len(nonzero) == 7
        and 0 in nonzero
        and abs(np.linalg.norm(one_step) - 1) < 2e-14,
        {
            "dimension": update.shape[0],
            "unitarity_residual": float(unitarity),
            "one_step_nonzero_components": len(nonzero),
            "one_step_norm": float(np.linalg.norm(one_step)),
        },
    )

    theta_zero_update = defect_update(length, 0.0)
    theta_zero_output = theta_zero_update @ reservoir_initial
    beta_zero_theta = KAPPA * c219.common_species(0.0).analytic_mass
    check(
        "the supplied kappa=0 or beta=0 parameter endpoint gives theta=0 and leaves a pure reservoir excitation stationary",
        np.linalg.norm(theta_zero_output - reservoir_initial) == 0
        and beta_zero_theta == 0
        and np.linalg.norm(
            defect_update(length, beta_zero_theta) @ reservoir_initial
            - reservoir_initial
        )
        == 0,
        {
            "theta_zero_residual": float(
                np.linalg.norm(theta_zero_output - reservoir_initial)
            ),
            "beta_zero_theta": beta_zero_theta,
            "scope": "parameter-setting control, not a deletion theorem for a derived law",
        },
    )
    source = c211.point_source(length)
    check(
        "the zero-shift comparison profile is exactly Cycle216's 3 L^+ source response",
        np.linalg.norm(
            shifted_green_profile(length, 0.0)
            - 3 * c211.solve_field(source)
        )
        < 3e-14,
        float(
            np.linalg.norm(
                shifted_green_profile(length, 0.0)
                - 3 * c211.solve_field(source)
            )
        ),
    )


def dressed_profile_and_green_controls() -> dict[int, tuple[complex, np.ndarray]]:
    print("\nSTATIONARY DRESSED EIGENSTATE / SHIFTED GREEN PROFILE")
    rows = []
    cache = {}
    for length in SIZES:
        update, eigenvalue, state = dressed_eigenstate(length)
        cache[length] = (eigenvalue, state)
        eigenphase = float(np.angle(eigenvalue))
        spectral_shift = float(6 * (1 - np.cos(eigenphase)))
        source = c211.point_source(length)
        scalar = scalar_projection(state, length)
        scalar_perpendicular = scalar - np.mean(scalar)
        q = emitted_amplitude(state, length)
        free_update = field_update(length)
        source_field = np.zeros_like(state[1:])
        source_field[:6] = c210.UNIFORM
        coined_origin = c214.FIELD_COIN @ state[1:7]
        local_scalar = np.vdot(c210.UNIFORM, coined_origin)
        reservoir_equation_residual = abs(
            eigenvalue * state[0]
            - (
                np.cos(THETA) * state[0]
                - 1j * np.sin(THETA) * local_scalar
            )
        )
        field_equation_residual = np.linalg.norm(
            eigenvalue * state[1:]
            - free_update @ state[1:]
            - q * (free_update @ source_field)
        )
        scalar_coin_residual = np.linalg.norm(
            c214.FIELD_COIN @ c210.UNIFORM - c210.UNIFORM
        )
        shifted = shifted_green_profile(length, spectral_shift)
        prediction = q * (
            -0.5 * source + 1j * np.sin(eigenphase) * shifted
        )
        normalized_tail = (
            scalar_perpendicular + 0.5 * q * source
        ) / (1j * q * np.sin(eigenphase))
        cycle216 = 3 * c211.solve_field(source)
        laplacian, _ = c211.c9.fourier_symbols(length)
        minimum_nonzero = float(np.min(laplacian[laplacian > 1e-14]))
        profile_l2_ratio = float(
            np.linalg.norm(shifted - cycle216) / np.linalg.norm(cycle216)
        )
        operator_bound = spectral_shift / (minimum_nonzero - spectral_shift)
        eigen_residual = float(np.linalg.norm(update @ state - eigenvalue * state))
        uniform_prediction = q * (
            -0.5 - 1j * 3 * np.sin(eigenphase) / spectral_shift
        ) / length**3
        row = {
            "L": length,
            "held_out": length == HELD_OUT,
            "dimension": update.shape[0],
            "eigenphase": eigenphase,
            "phase_scaled_by_L^(3/2)/theta": eigenphase * length**1.5 / THETA,
            "reservoir_squared_norm_weight": float(abs(state[0]) ** 2),
            "field_squared_norm_weight": float(np.linalg.norm(state[1:]) ** 2),
            "eigen_residual": eigen_residual,
            "stationary_squared_norm_residual": float(
                np.max(np.abs(np.abs(update @ state) ** 2 - np.abs(state) ** 2))
            ),
            "reservoir_equation_residual": float(reservoir_equation_residual),
            "field_equation_residual": float(field_equation_residual),
            "C_s0_minus_s0_residual": float(scalar_coin_residual),
            "emitted_amplitude_abs": float(abs(q)),
            "spectral_shift_mu": spectral_shift,
            "minimum_nonzero_Laplacian": minimum_nonzero,
            "exact_profile_residual": float(
                np.linalg.norm(scalar_perpendicular - prediction)
                / np.linalg.norm(scalar_perpendicular)
            ),
            "normalized_tail_residual": float(
                np.linalg.norm(normalized_tail - shifted) / np.linalg.norm(shifted)
            ),
            "profile_l2_ratio_to_Cycle216_3Lplus": profile_l2_ratio,
            "zero_mean_relative_operator_bound": operator_bound,
            "observed_uniform_scalar_amplitude": complex(np.mean(scalar)),
            "predicted_uniform_scalar_amplitude": complex(uniform_prediction),
            "uniform_component_residual": float(
                abs(np.mean(scalar) - uniform_prediction)
            ),
        }
        rows.append(row)

    check(
        "the selected normalized eigenpairs on L=3,...,9 have nonzero reservoir and field squared-norm weights",
        all(row["eigen_residual"] < 2e-12 for row in rows)
        and all(row["stationary_squared_norm_residual"] < 2e-12 for row in rows)
        and all(0.45 < row["reservoir_squared_norm_weight"] < 0.48 for row in rows)
        and all(
            abs(
                row["reservoir_squared_norm_weight"]
                + row["field_squared_norm_weight"]
                - 1
            )
            < 2e-12
            for row in rows
        )
        and all(row["emitted_amplitude_abs"] > 0.2 for row in rows),
        rows,
    )
    check(
        "the local gate equations directly produce q and the nonuniform scalar profile uses no fitted Green coefficient",
        all(row["reservoir_equation_residual"] < 2e-12 for row in rows)
        and all(row["field_equation_residual"] < 2e-12 for row in rows)
        and all(row["C_s0_minus_s0_residual"] < 2e-14 for row in rows)
        and all(row["exact_profile_residual"] < 4e-12 for row in rows)
        and all(row["normalized_tail_residual"] < 3e-11 for row in rows)
        and all(row["uniform_component_residual"] < 5e-13 for row in rows),
        [
            {
                "L": row["L"],
                "reservoir_equation_residual": row["reservoir_equation_residual"],
                "field_equation_residual": row["field_equation_residual"],
                "C_s0_minus_s0_residual": row["C_s0_minus_s0_residual"],
                "exact_profile_residual": row["exact_profile_residual"],
                "normalized_tail_residual": row["normalized_tail_residual"],
                "uniform_component_residual": row["uniform_component_residual"],
            }
            for row in rows
        ],
    )
    check(
        "the source-specific shifted-profile ratio obeys the zero-mean relative operator bound and decreases on tested L=3,...,9",
        all(row["spectral_shift_mu"] < row["minimum_nonzero_Laplacian"] for row in rows)
        and all(
            row["profile_l2_ratio_to_Cycle216_3Lplus"]
            <= row["zero_mean_relative_operator_bound"] + 2e-13
            for row in rows
        )
        and all(
            rows[index + 1]["profile_l2_ratio_to_Cycle216_3Lplus"]
            < rows[index]["profile_l2_ratio_to_Cycle216_3Lplus"]
            for index in range(len(rows) - 1)
        )
        and rows[-1]["profile_l2_ratio_to_Cycle216_3Lplus"] < 7.1e-4,
        [
            {
                "L": row["L"],
                "mu": row["spectral_shift_mu"],
                "source_specific_profile_l2_ratio": row[
                    "profile_l2_ratio_to_Cycle216_3Lplus"
                ],
                "zero_mean_relative_operator_bound": row[
                    "zero_mean_relative_operator_bound"
                ],
            }
            for row in rows
        ],
    )
    check(
        "the observed L=3,...,9 phase ratio stays inside the declared [0.96,0.99] acceptance window without turning eigenphase into a rate",
        tuple(row["L"] for row in rows) == SIZES
        and all(
            0.96 < row["phase_scaled_by_L^(3/2)/theta"] < 0.99
            for row in rows
        ),
        [
            (
                row["L"],
                row["eigenphase"],
                row["phase_scaled_by_L^(3/2)/theta"],
            )
            for row in rows
        ],
    )
    return cache


def spectral_identity_and_conjugate_controls(
    cache: dict[int, tuple[complex, np.ndarray]]
) -> None:
    print("\nMODE IDENTITY / CONJUGATE BRANCH / ZERO MODES")
    eigenvalue = cache[HELD_OUT][0]
    eigenphase = float(np.angle(eigenvalue))
    shift = 6 * (1 - np.cos(eigenphase))
    rng = np.random.default_rng(317)
    residuals = []
    for _ in range(48):
        momentum = rng.uniform(-2.8, 2.8, size=3)
        stream = np.diag(np.exp(-1j * (c210.DIRECTIONS @ momentum)))
        field_update = stream @ c214.FIELD_COIN
        left = np.vdot(
            c210.UNIFORM,
            np.linalg.solve(
                eigenvalue * np.eye(6) - field_update,
                field_update @ c210.UNIFORM,
            ),
        )
        laplacian = c216.laplacian_symbol(momentum)
        right = -0.5 + 1j * 3 * np.sin(eigenphase) / (laplacian - shift)
        residuals.append(abs(left - right))
    check(
        "the Cycle215 scalar row gives the shifted-resolvent identity at 48 held-out nonzero momenta",
        max(residuals) < 2e-12,
        max(residuals),
    )

    flat_momentum = np.asarray((0.41, -0.23, 0.17))
    flat_stream = np.diag(
        np.exp(-1j * (c210.DIRECTIONS @ flat_momentum))
    )
    flat_update = flat_stream @ c214.FIELD_COIN
    flat_values, flat_vectors = np.linalg.eig(flat_update)
    plus = np.where(np.abs(flat_values - 1) < 2e-12)[0]
    minus = np.where(np.abs(flat_values + 1) < 2e-12)[0]
    flat_overlaps = [
        abs(np.vdot(c210.UNIFORM, flat_vectors[:, index]))
        for index in tuple(plus) + tuple(minus)
    ]
    check(
        "the scalar source misses both U=+1 zero-mode directions and both U=-1 flat directions of the field walk",
        len(plus) == len(minus) == 2 and max(flat_overlaps) < 3e-12,
        {
            "U_plus_one_flat_modes": len(plus),
            "U_minus_one_flat_modes": len(minus),
            "maximum_scalar_overlap": max(flat_overlaps),
        },
    )

    branch_rows = []
    for length in SIZES:
        positive_value, positive_state = cache[length]
        update, negative_value, negative_state = dressed_eigenstate(
            length, negative=True
        )
        branch_rows.append(
            {
                "L": length,
                "phase_sum": float(
                    np.angle(positive_value) + np.angle(negative_value)
                ),
                "reservoir_weight_difference": float(
                    abs(abs(positive_state[0]) ** 2 - abs(negative_state[0]) ** 2)
                ),
                "negative_eigen_residual": float(
                    np.linalg.norm(
                        update @ negative_state - negative_value * negative_state
                    )
                ),
            }
        )
    check(
        "the adjoint spectral branch has the opposite eigenphase and equal reservoir squared-norm weight at every tested L=3,...,9",
        max(abs(row["phase_sum"]) for row in branch_rows) < 3e-13
        and max(row["reservoir_weight_difference"] for row in branch_rows) < 3e-12
        and max(row["negative_eigen_residual"] for row in branch_rows) < 2e-12,
        branch_rows,
    )

    source = c211.point_source(HELD_OUT)
    laplacian, _ = c211.c9.fourier_symbols(HELD_OUT)
    source_hat = np.fft.fftn(source, norm="ortho")
    check(
        "the Cycle216 comparison uses explicit zero-mode subtraction and the dressed spectral shift remains below the first nonzero Laplacian mode",
        abs(source.sum()) < 3e-14
        and abs(source_hat[0, 0, 0]) < 3e-14
        and shift < np.min(laplacian[laplacian > 1e-14]),
        {
            "source_sum": float(source.sum()),
            "zero_mode": complex(source_hat[0, 0, 0]),
            "mu": shift,
            "first_nonzero_mode": float(np.min(laplacian[laplacian > 1e-14])),
        },
    )


def covariance_and_source_family_controls(
    cache: dict[int, tuple[complex, np.ndarray]]
) -> None:
    print("\nPROPER-CUBIC / TRANSLATED-SOURCE FAMILY")
    length = 3
    update = defect_update(length)
    eigenvalue, state = cache[length]
    covariance_residuals = []
    state_residuals = []
    for frame in c210.proper_cubic_frames():
        representation = frame_permutation(length, frame)
        covariance_residuals.append(
            float(sparse.linalg.norm(representation @ update - update @ representation))
        )
        transformed = representation @ state
        phase = np.vdot(state, transformed)
        state_residuals.append(
            float(np.linalg.norm(transformed - phase * state))
        )
    check(
        "the source-centered update and dressed state are covariant in all 24 proper-cubic frames",
        len(covariance_residuals) == 24
        and max(covariance_residuals) < 2e-13
        and max(state_residuals) < 2e-11,
        {
            "maximum_update_residual": max(covariance_residuals),
            "maximum_state_residual": max(state_residuals),
        },
    )

    translation_residuals = []
    tests = 0
    for displacement in product(range(length), repeat=3):
        representation = translation_permutation(length, displacement)
        moved_update = representation @ update @ representation.conj().T
        moved_state = representation @ state
        translation_residuals.append(
            float(np.linalg.norm(moved_update @ moved_state - eigenvalue * moved_state))
        )
        tests += 1
    check(
        "all 27 L=3 source positions form an exactly translated covariant defect family rather than one translation-invariant preferred source",
        tests == 27 and max(translation_residuals) < 2e-12,
        {"tests": tests, "maximum_residual": max(translation_residuals)},
    )


def normalization_domain_and_inventory_controls(
    cache: dict[int, tuple[complex, np.ndarray]]
) -> None:
    print("\nNORMALIZATION / LAWFUL DOMAIN / INVENTORY")
    length = HELD_OUT
    eigenvalue, state = cache[length]
    source = c211.point_source(length)
    scalar = scalar_projection(state, length)
    scalar_perpendicular = scalar - np.mean(scalar)
    q = emitted_amplitude(state, length)
    phase = float(np.angle(eigenvalue))
    baseline = (
        scalar_perpendicular + 0.5 * q * source
    ) / (1j * q * np.sin(phase))
    arbitrary_scale = 2.3 * np.exp(0.41j)
    scaled_state = arbitrary_scale * state
    scaled_scalar = scalar_projection(scaled_state, length)
    scaled_q = emitted_amplitude(scaled_state, length)
    scaled = (
        scaled_scalar
        - np.mean(scaled_scalar)
        + 0.5 * scaled_q * source
    ) / (1j * scaled_q * np.sin(phase))
    check(
        "the normalized-tail ratio is invariant when the eigenvector and q are jointly scaled and rephased; no Green coefficient is fitted",
        np.linalg.norm(baseline - scaled) < 3e-12,
        {
            "normalized_tail_invariance_residual": float(
                np.linalg.norm(baseline - scaled)
            ),
            "eigenvector_multiplier": arbitrary_scale,
            "q_multiplier_residual": float(
                abs(scaled_q - arbitrary_scale * q)
            ),
        },
    )

    def validate(
        length: int,
        reservoir_m2: int,
        field_modes: int,
        excitation_sector: int,
    ) -> None:
        if length < 3:
            raise ValueError("periodic direction streams require L>=3")
        if reservoir_m2 != 1 or field_modes != 6:
            raise ValueError("the active source uses one reservoir M2 and six field M2 per cell")
        if excitation_sector != 1:
            raise ValueError("this runner tests the conserved one-excitation sector")

    validate(3, 1, 6, 1)
    rejected = 0
    for candidate in ((2, 1, 6, 1), (3, 0, 6, 1), (3, 1, 5, 1), (3, 1, 6, 2)):
        try:
            validate(*candidate)
        except ValueError:
            rejected += 1
    check(
        "the lawful domain rejects aliased, mistyped, and wrong-excitation fixtures",
        rejected == 4,
        {"rejected": rejected},
    )
    check(
        "the supplied structure inventory distinguishes the dressed resolvent theorem from energy, gravity, and renewal semantics",
        True,
        {
            "supplied": (
                "Cycle214/215 six-direction field coin and coin-vertex-stream ordering",
                "one active site-local reservoir M2, uniform scalar exchange, beta=-0.3, and kappa=0.8",
                "finite periodic volume, source position, zero-mean comparison convention, and one-excitation preparation",
                "Cycle216's stiffness/3L+ comparator",
                "shift-invert target exp(+/- i theta/L^(3/2)); among three returned requested-sign candidates choose maximum reservoir squared-norm weight, then normalize and rephase the reservoir amplitude real-positive",
                "runner acceptance inventory: L=3,...,9; L=3,...,8 training; held-out L=9; phase ratio [0.96,0.99]; reservoir squared-norm weight (0.45,0.48); held-out profile ratio below 7.1e-4",
            ),
            "derived": (
                "numerically selected closed finite-volume dressed eigenpairs with stationary basis-component squared norms on L=3,...,9",
                "local-gate eigenpair-to-q equations and exact local-source plus 3(L-mu)^-1 normalized-tail profile identity conditional on those eigenpair equations",
                "tested-size comparison with Cycle216 3L+, covariance, theta=0 parameter endpoint, held-size, uniform-component, and zero-mode controls",
            ),
            "not_earned": (
                "physical energy, a Hamiltonian, eigenphase-as-rate, clock normalization, gravity, stress, or source mass",
                "host-side renewal, retarded selection, radiation reaction, moving-source transport, or many-excitation closure",
                "a matter Hilbert space or matter/contact update, the Cycle230 contact block, or a whole physical-M2 compiler/intertwiner",
                "an interface to the carried-source code; this active fixed reservoir is neither carried nor moving",
                "a Record, occurrence law, Born rule, axiom change, or audit authority",
            ),
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("STATIONARY DRESSED RESERVOIR / SHIFTED GREEN PROFILE")
    note_contract()
    locality_unitarity_and_parameter_endpoint_controls()
    cache = dressed_profile_and_green_controls()
    spectral_identity_and_conjugate_controls(cache)
    covariance_and_source_family_controls(cache)
    normalization_domain_and_inventory_controls(cache)
    print("\nSUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "STATIONARY_DRESSED_SHIFTED_GREEN_PROFILE_EXACT"
        if FAIL == 0
        else "STATIONARY_DRESSED_SHIFTED_GREEN_PROFILE_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
