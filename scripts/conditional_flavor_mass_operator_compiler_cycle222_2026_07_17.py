#!/usr/bin/env python3
"""Cycle 222: compile a supplied conditional C3 mass ansatz into dynamics.

Start from the repo's audit-unset Hermitian circulant signed-root ansatz H and
separately supply its positive-root chamber, r, phase, scale, carrier meaning,
and M_flavor=H^2.  Adjoin a zero block and apply the exact inverse Cayley map
to obtain one phase register S.  Test whether the Cycle-220 coin then carries
the same conditional spectrum into direct-block dispersion, fixed-force
inertia, and M-charged response without a species lookup in the update.

This is a spectrum-to-dynamics compiler.  It neither selects H nor derives
its scale, r=1/2 condition, bare-radian hierarchy phase, H-to-mass map,
field/matter interpretation, contact compiler, charge law, or Record process.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

import active_cubic_source_response_cycle211_2026_07_16 as c211
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import generated_beta_phase_register_cycle220_2026_07_16 as c220
import operator_mass_equivalence_cycle221_2026_07_17 as c221
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import virtual_exchange_green_kernel_cycle216_2026_07_16 as c216


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CONDITIONAL_FLAVOR_MASS_OPERATOR_COMPILER_CYCLE222_NOTE_2026-07-17.md"
)

REFERENCE_SCALE = 16.0
# Frozen before evaluation as an irrational offset from the reference scale.
HELD_OUT_SCALE = REFERENCE_SCALE + np.sqrt(2)
# Frozen after the 64-tick held-out miss, but before testing the long-window repair.
POST_REPAIR_HELD_OUT_SCALE = REFERENCE_SCALE + np.pi
R_VALUE = 0.5
DELTA = 2 / 9
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


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "spectrum-to-dynamics compiler",
        "inverse cayley",
        "conditional flavor mass operator",
        "r=1/2 remains supplied",
        "bare-radian hierarchy phase remains supplied",
        "overall mass scale remains supplied",
        "positive-root chamber",
        "m_flavor=h^2 remains supplied",
        "all finite hermitian mass operators",
        "principal phase does not determine the winding",
        "fixed-force inertia",
        "conditional common acceleration",
        "equal-direction kinematics",
        "orthogonal redundant pointers",
        "qualification remains open",
        "no species lookup during propagation or force update",
        "not a mass-spectrum derivation",
        "not a gravity theory",
        "no axiom conclusion",
        "apadula",
        "koide",
        "brannen",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves compiler gain and supplied spectrum boundary", not missing, missing)


def cyclic_shift_three() -> np.ndarray:
    return np.array(((0, 1, 0), (0, 0, 1), (1, 0, 0)), dtype=complex)


def signed_root_operator(scale: float, delta: float, r_value: float = R_VALUE) -> np.ndarray:
    shift = cyclic_shift_three()
    amplitude = scale * np.sqrt(r_value)
    return (
        scale * np.eye(3)
        + amplitude * np.exp(1j * delta) * shift
        + amplitude * np.exp(-1j * delta) * shift.conj().T
    )


def embed_positive_block(block: np.ndarray) -> np.ndarray:
    mass = np.zeros((4, 4), dtype=complex)
    mass[1:, 1:] = block
    return mass


def embed_mass(root: np.ndarray) -> np.ndarray:
    return embed_positive_block(root @ root)


def inverse_cayley(mass: np.ndarray) -> np.ndarray:
    identity = np.eye(mass.shape[0], dtype=complex)
    return (identity - 1j * mass / 3) @ np.linalg.inv(identity + 1j * mass / 3)


@dataclass(frozen=True)
class Compiled:
    scale: float
    root: np.ndarray
    mass: np.ndarray
    register: np.ndarray
    recovered_mass: np.ndarray
    coin: np.ndarray
    sectors: tuple[tuple[float, float, np.ndarray], ...]


def compile_operator(scale: float, delta: float = DELTA) -> Compiled:
    root = signed_root_operator(scale, delta)
    mass = embed_mass(root)
    register = inverse_cayley(mass)
    recovered_mass, coin = c220.common_register_coin(register)
    values, vectors = np.linalg.eigh(recovered_mass)
    sectors = []
    for value, vector in zip(values, vectors.T):
        if value > 1e-8:
            beta = float(np.angle(np.vdot(vector, register @ vector)))
            sectors.append((float(value), beta, vector))
    return Compiled(
        scale,
        root,
        mass,
        register,
        recovered_mass,
        coin,
        tuple(sectors),
    )


def koide_q(masses: np.ndarray) -> float:
    roots = np.sqrt(np.maximum(np.asarray(masses, dtype=float), 0))
    return float(np.sum(masses) / np.sum(roots) ** 2)


def block_branch_eigenpair(
    block: np.ndarray, momentum: np.ndarray
) -> tuple[float, np.ndarray]:
    """Track the scalar band directly from an extracted compiled block."""
    values, vectors = np.linalg.eig(c210.molecular_bloch(momentum, block))
    overlaps = np.abs(vectors.conj().T @ c210.UNIFORM)
    index = int(np.argmax(overlaps))
    vector = vectors[:, index]
    vector *= np.exp(-1j * np.angle(np.vdot(c210.UNIFORM, vector)))
    return float(np.angle(values[index])), vector / np.linalg.norm(vector)


def block_phase_near_origin(block: np.ndarray, momentum: np.ndarray) -> float:
    rest = float(np.angle(np.vdot(c210.UNIFORM, block @ c210.UNIFORM)))
    phase, _ = block_branch_eigenpair(block, momentum)
    return rest + c210.angular_difference(phase, rest)


def block_curvature_tensor(block: np.ndarray, step: float = 1e-3) -> np.ndarray:
    """Numerical Hessian without reconstructing an analytic target species."""
    origin = np.zeros(3)
    rest = block_phase_near_origin(block, origin)
    hessian = np.zeros((3, 3))
    for first in range(3):
        for second in range(3):
            if first == second:
                displacement = np.zeros(3)
                displacement[first] = step
                hessian[first, first] = (
                    block_phase_near_origin(block, displacement)
                    - 2 * rest
                    + block_phase_near_origin(block, -displacement)
                ) / step**2
            else:
                pp = np.zeros(3)
                pm = np.zeros(3)
                mp = np.zeros(3)
                mm = np.zeros(3)
                pp[first] = pp[second] = step
                pm[first], pm[second] = step, -step
                mp[first], mp[second] = -step, step
                mm[first] = mm[second] = -step
                hessian[first, second] = (
                    block_phase_near_origin(block, pp)
                    - block_phase_near_origin(block, pm)
                    - block_phase_near_origin(block, mp)
                    + block_phase_near_origin(block, mm)
                ) / (4 * step**2)
    return hessian


def prepare_block_packet(
    block: np.ndarray,
    length: int,
    momentum_width: float,
    *,
    axis: int = 0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    packet_k = np.zeros((length, 6), dtype=complex)
    for index, momentum in enumerate(momenta):
        envelope = np.exp(-0.5 * (momentum / momentum_width) ** 2)
        if envelope < 1e-14:
            continue
        vector_momentum = np.zeros(3)
        vector_momentum[axis] = momentum
        _, vector = block_branch_eigenpair(block, vector_momentum)
        packet_k[index] = envelope * vector
    packet_k /= np.linalg.norm(packet_k)
    packet = np.fft.ifft(packet_k, axis=0, norm="ortho")
    packet = np.roll(packet, length // 2, axis=0)
    positions = np.arange(length, dtype=float) - length // 2
    return positions, momenta, packet


def block_branch_probability(
    packet: np.ndarray,
    momenta: np.ndarray,
    block: np.ndarray,
    *,
    axis: int = 0,
) -> float:
    packet_k = np.fft.fft(packet, axis=0, norm="ortho")
    probability = 0.0
    for index, momentum in enumerate(momenta):
        if np.linalg.norm(packet_k[index]) < 1e-12:
            continue
        vector_momentum = np.zeros(3)
        vector_momentum[axis] = momentum
        _, vector = block_branch_eigenpair(block, vector_momentum)
        probability += abs(np.vdot(vector, packet_k[index])) ** 2
    return float(probability)


def local_register_step_axis(
    state: np.ndarray, coin: np.ndarray, *, axis: int = 0
) -> np.ndarray:
    length, dimension, _ = state.shape
    mixed = (coin @ state.reshape(length, dimension * 6).T).T.reshape(
        length, dimension, 6
    )
    output = np.zeros_like(mixed)
    for direction in range(6):
        output[:, :, direction] = np.roll(
            mixed[:, :, direction],
            int(c210.DIRECTIONS[direction, axis]),
            axis=0,
        )
    return output


def prepare_compiled_register_packet(
    register_coin: np.ndarray,
    sectors: tuple[tuple[float, float, np.ndarray], ...],
    *,
    length: int,
    momentum_width: float,
    axis: int = 0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    dimension = len(sectors[0][2])
    state = np.zeros((length, dimension, 6), dtype=complex)
    positions = momenta = None
    amplitudes = np.ones(len(sectors), dtype=complex) / np.sqrt(len(sectors))
    for amplitude, (_, _, vector) in zip(amplitudes, sectors):
        block = c220.extract_direction_block(register_coin, vector)
        branch_positions, branch_momenta, packet = prepare_block_packet(
            block, length, momentum_width, axis=axis
        )
        state += amplitude * np.einsum("r,xd->xrd", vector, packet, optimize=True)
        positions, momenta = branch_positions, branch_momenta
    state /= np.linalg.norm(state)
    assert positions is not None and momenta is not None
    return positions, momenta, state


def direct_operator_response(
    register_coin: np.ndarray,
    charge: np.ndarray,
    sectors: tuple[tuple[float, float, np.ndarray], ...],
    strength: float,
    *,
    ordering: str = "symmetric",
    length: int = 2048,
    momentum_width: float = 0.012,
    duration: int = 64,
    axis: int = 0,
) -> c221.OperatorResponse:
    """Packet response using only extracted compiled blocks, not target species."""
    positions, momenta, state = prepare_compiled_register_packet(
        register_coin,
        sectors,
        length=length,
        momentum_width=momentum_width,
        axis=axis,
    )
    centres = [[] for _ in sectors]
    weights = [[] for _ in sectors]
    for row_index, (_, _, vector) in enumerate(sectors):
        centre, weight = c221.sector_mean_position(state, vector, positions)
        centres[row_index].append(centre)
        weights[row_index].append(weight)
    for _ in range(duration):
        if ordering == "pre":
            state = local_register_step_axis(
                c221.apply_position_charge(state, positions, charge, strength),
                register_coin,
                axis=axis,
            )
        elif ordering == "post":
            state = c221.apply_position_charge(
                local_register_step_axis(state, register_coin, axis=axis),
                positions,
                charge,
                strength,
            )
        elif ordering == "symmetric":
            state = c221.apply_position_charge(
                local_register_step_axis(
                    c221.apply_position_charge(
                        state, positions, charge, strength / 2
                    ),
                    register_coin,
                    axis=axis,
                ),
                positions,
                charge,
                strength / 2,
            )
        else:
            raise ValueError(ordering)
        for row_index, (_, _, vector) in enumerate(sectors):
            centre, weight = c221.sector_mean_position(state, vector, positions)
            centres[row_index].append(centre)
            weights[row_index].append(weight)

    times = np.arange(duration + 1, dtype=float)
    response_rows = []
    for row_index, (eigenmass, _, vector) in enumerate(sectors):
        charge_value = float(np.vdot(vector, charge @ vector).real)
        displacement = np.asarray(centres[row_index]) - centres[row_index][0]
        acceleration = float(2 * np.polyfit(times, displacement, 2)[0])
        force = -strength * charge_value
        measured_mass = force / acceleration if abs(acceleration) > 1e-15 else np.inf
        component = c221.sector_component(state, vector)
        component /= np.linalg.norm(component)
        block = c220.extract_direction_block(register_coin, vector)
        response_rows.append(
            (
                eigenmass,
                acceleration,
                measured_mass,
                block_branch_probability(component, momenta, block, axis=axis),
                weights[row_index][-1],
            )
        )
    return c221.OperatorResponse(
        ordering,
        strength,
        tuple(response_rows),
        float(np.linalg.norm(state)),
        float(sum(row[-1] for row in weights)),
        float(
            np.sum(
                np.sum(np.abs(state) ** 2, axis=(1, 2))[
                    np.abs(positions) > length / 4
                ]
            )
        ),
    )


def response_is_healthy(
    response: c221.OperatorResponse, *, band_floor: float = 0.999
) -> bool:
    return (
        abs(response.norm - 1) < 2e-10
        and abs(response.final_weight_sum - 1) < 2e-10
        and response.boundary_probability < 2e-12
        and min(row[3] for row in response.rows) > band_floor
        and min(row[4] for row in response.rows) > 0
    )


def operator_and_compiler_controls(compiled: Compiled) -> None:
    root_values = np.linalg.eigvalsh(compiled.root)
    mass_values = np.linalg.eigvalsh(compiled.mass)[1:]
    check(
        "the supplied C3 signed-root operator is Hermitian and positive at the reference point",
        np.linalg.norm(compiled.root - compiled.root.conj().T) < 2e-12
        and np.min(root_values) > 0,
        root_values.tolist(),
    )
    check(
        "the supplied candidate mass block is the positive square of the signed-root operator",
        np.min(np.linalg.eigvalsh(compiled.mass)) > -2e-10
        and np.linalg.norm(compiled.mass[1:, 1:] - compiled.root @ compiled.root) < 2e-10,
        mass_values.tolist(),
    )
    check(
        "the conditional r=1/2 positive-root spectrum has Koide Q=2/3",
        abs(koide_q(mass_values) - 2 / 3) < 2e-13
        and abs(R_VALUE - 0.5) < 2e-15,
        koide_q(mass_values),
    )

    delta_rows = []
    for delta in (0.05, 0.10, DELTA):
        root = signed_root_operator(1.0, delta)
        values = np.linalg.eigvalsh(root)
        masses = values**2
        delta_rows.append(
            (delta, float(np.min(values)), koide_q(masses), tuple(masses / np.min(masses)))
        )
    check(
        "inside the positive-root chamber the phase changes both nontrivial ratios but not Q",
        min(row[1] for row in delta_rows) > 0
        and max(abs(row[2] - 2 / 3) for row in delta_rows) < 2e-13
        and all(
            len({round(row[3][ratio_index], 6) for row in delta_rows}) == 3
            for ratio_index in (1, 2)
        ),
        delta_rows,
    )

    boundary = np.pi / 12
    boundary_rows = []
    for delta in (boundary - 1e-7, boundary, boundary + 1e-7):
        boundary_rows.append(
            (delta, float(np.min(np.linalg.eigvalsh(signed_root_operator(1.0, delta)))))
        )
    check(
        "the selected positive-root chamber ends at pi/12",
        boundary_rows[0][1] > 0
        and abs(boundary_rows[1][1]) < 3e-12
        and boundary_rows[2][1] < 0,
        boundary_rows,
    )

    mirror_rows = []
    for delta in (0.05, 0.10, DELTA):
        positive = np.linalg.eigvalsh(signed_root_operator(1.0, delta)) ** 2
        negative = np.linalg.eigvalsh(signed_root_operator(1.0, -delta)) ** 2
        mirror_rows.append((delta, float(np.max(np.abs(positive - negative)))))
    check(
        "the mass spectrum cannot distinguish the delta-sign mirror",
        max(row[1] for row in mirror_rows) < 2e-12,
        mirror_rows,
    )

    outside_delta = 0.3
    outside_root_values = np.linalg.eigvalsh(
        signed_root_operator(1.0, outside_delta)
    )
    outside_q = koide_q(outside_root_values**2)
    check(
        "outside the positive-root chamber squaring destroys the r-only Koide identity",
        outside_delta > np.pi / 12
        and np.min(outside_root_values) < 0
        and abs(outside_q - 2 / 3) > 0.02,
        {
            "delta": outside_delta,
            "pi/12": np.pi / 12,
            "signed_roots": outside_root_values.tolist(),
            "Q(H^2)": outside_q,
        },
    )

    function_rows = {}
    for label, block in {
        "H": compiled.root,
        "H^2": compiled.root @ compiled.root,
        "I+H": np.eye(3) + compiled.root,
    }.items():
        candidate_mass = embed_positive_block(block)
        candidate_register = inverse_cayley(candidate_mass)
        candidate_recovered = c220.cayley_mass(candidate_register)
        values = np.linalg.eigvalsh(candidate_mass)[1:]
        function_rows[label] = {
            "error": float(np.linalg.norm(candidate_recovered - candidate_mass)),
            "relative_error": float(
                np.linalg.norm(candidate_recovered - candidate_mass)
                / max(np.linalg.norm(candidate_mass), 1.0)
            ),
            "ratios": tuple(float(value / np.min(values)) for value in values),
        }
    check(
        "the compiler transports but cannot select the supplied positive function of H",
        max(row["relative_error"] for row in function_rows.values()) < 5e-12
        and len(
            {
                tuple(round(value, 6) for value in row["ratios"])
                for row in function_rows.values()
            }
        )
        == len(function_rows),
        function_rows,
    )

    identity = np.eye(compiled.mass.shape[0])
    cayley_relative_error = float(
        np.linalg.norm(compiled.recovered_mass - compiled.mass)
        / max(np.linalg.norm(compiled.mass), 1.0)
    )
    check(
        "the inverse Cayley register is unitary and recovers the supplied mass operator",
        np.linalg.norm(compiled.register.conj().T @ compiled.register - identity) < 3e-11
        and cayley_relative_error < 5e-12,
        {
            "absolute_error": float(np.linalg.norm(compiled.recovered_mass - compiled.mass)),
            "relative_error": cayley_relative_error,
        },
    )

    rng = np.random.default_rng(222)
    raw = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    basis, _ = np.linalg.qr(raw)
    arbitrary_values = np.array((-2.3, 0.17, 4.2, 11.7))
    arbitrary_mass = (basis * arbitrary_values) @ basis.conj().T
    arbitrary_register = inverse_cayley(arbitrary_mass)
    recovered = c220.cayley_mass(arbitrary_register)
    check(
        "the exact compiler accepts an unrelated finite Hermitian spectrum",
        np.linalg.norm(arbitrary_register.conj().T @ arbitrary_register - identity) < 3e-12
        and np.linalg.norm(recovered - arbitrary_mass) < 3e-11,
        np.linalg.norm(recovered - arbitrary_mass),
    )

    embedded_shift = np.zeros((4, 4), dtype=complex)
    embedded_shift[0, 0] = 1
    embedded_shift[1:, 1:] = cyclic_shift_three()
    check(
        "the flavor mass and compiled register retain C3 covariance",
        np.linalg.norm(embedded_shift @ compiled.mass - compiled.mass @ embedded_shift) < 2e-10
        and np.linalg.norm(
            embedded_shift @ compiled.register - compiled.register @ embedded_shift
        )
        < 2e-10,
    )

    check(
        "one compiled coin is unitary and contains one massless plus three massive sectors",
        np.linalg.norm(compiled.coin.conj().T @ compiled.coin - np.eye(24)) < 2e-8
        and len(compiled.sectors) == 3
        and abs(
            float(
                np.vdot(
                    np.eye(4)[0], compiled.recovered_mass @ np.eye(4)[0]
                ).real
            )
        )
        < 2e-10,
        [(row[0], row[1]) for row in compiled.sectors],
    )

    zero_values, zero_vectors = np.linalg.eigh(compiled.recovered_mass)
    zero_vector = zero_vectors[:, int(np.argmin(np.abs(zero_values)))]
    zero_block = c220.extract_direction_block(compiled.coin, zero_vector)
    rng_field = np.random.default_rng(2220)
    field_packet = rng_field.normal(size=(97, 6)) + 1j * rng_field.normal(
        size=(97, 6)
    )
    field_packet /= np.linalg.norm(field_packet)
    register_packet = np.einsum(
        "r,xd->xrd", zero_vector, field_packet, optimize=True
    )
    expected_packet = field_packet.copy()
    for _ in range(11):
        register_packet = local_register_step_axis(register_packet, compiled.coin)
        expected_packet = c210.local_molecular_step(
            expected_packet, c214.FIELD_COIN, axis=0
        )
    recovered_packet = c221.sector_component(register_packet, zero_vector)
    check(
        "the adjoined zero block exactly reproduces the existing field coin and one-axis propagation",
        np.linalg.norm(zero_block - c214.FIELD_COIN) < 2e-10
        and np.linalg.norm(recovered_packet - expected_packet) < 2e-9
        and abs(np.linalg.norm(register_packet) - 1) < 2e-10,
        {
            "coin_error": float(np.linalg.norm(zero_block - c214.FIELD_COIN)),
            "trajectory_error": float(np.linalg.norm(recovered_packet - expected_packet)),
        },
    )

    covariance = []
    for frame in c210.proper_cubic_frames():
        direction = c210.direction_permutation(frame)
        representation = np.kron(np.eye(4), direction)
        covariance.append(
            np.linalg.norm(
                representation @ compiled.coin @ representation.conj().T
                - compiled.coin
            )
        )
    check(
        "the compiled coin commutes with all 24 proper-cubic frames",
        len(covariance) == 24 and max(covariance) < 2e-10,
        max(covariance),
    )

    register_phases = np.angle(np.linalg.eigvals(compiled.register))
    clifford_distances = [
        min(
            abs(c210.angular_difference(float(phase), index * np.pi / 4))
            for index in range(-4, 5)
        )
        for phase in register_phases
    ]
    check(
        "the supplied ansatz and register retain genuinely complex off-Clifford phases",
        np.linalg.norm(compiled.root.imag) > 0.1
        and max(clifford_distances) > 0.05,
        {
            "root_imaginary_norm": float(np.linalg.norm(compiled.root.imag)),
            "phase_grid_distances": clifford_distances,
        },
    )

    sector_errors = []
    for mass, beta, vector in compiled.sectors:
        block = c220.extract_direction_block(compiled.coin, vector)
        sector_errors.append(np.linalg.norm(block - c219.common_species(beta).coin))
    check(
        "every spectral sector realizes the common matter coin without a species table",
        max(sector_errors) < 2e-9,
        sector_errors,
    )

    condition_number = float(np.linalg.cond(compiled.register + identity))
    analytic_condition = float(
        np.sqrt(1 + (max(row[0] for row in compiled.sectors) / 3) ** 2)
    )
    sensitivity_rows = []
    epsilon = 1e-6
    for mass, beta, _ in compiled.sectors:
        analytic = (mass**2 + 9) / 6
        shifted_plus = -3 * np.tan((beta + epsilon) / 2)
        shifted_minus = -3 * np.tan((beta - epsilon) / 2)
        numeric = abs((shifted_plus - shifted_minus) / (2 * epsilon))
        sensitivity_rows.append(
            (mass, beta, analytic, numeric, 0.01 * mass / analytic)
        )
    check(
        "inverse-Cayley recovery exposes the phase precision carried by the hierarchy",
        condition_number > 400
        and abs(condition_number / analytic_condition - 1) < 2e-9
        and sensitivity_rows[-1][2] / sensitivity_rows[0][2] > 1e5
        and max(
            abs(row[3] / row[2] - 1) for row in sensitivity_rows
        )
        < 0.002,
        {
            "cond(S+I)": condition_number,
            "analytic_cond(S+I)": analytic_condition,
            "rows=(mass,beta,|dm/dbeta| analytic,numeric,phase_for_1pct)": sensitivity_rows,
        },
    )


def phase_dispersion_and_inertia(
    compiled: Compiled,
    held_out: Compiled,
    post_repair_held_out: Compiled,
) -> None:
    coordinate_rows = []
    for mass, beta, vector in compiled.sectors:
        block = c220.extract_direction_block(compiled.coin, vector)
        principal_energy = float(
            np.angle(np.vdot(c210.UNIFORM, block @ c210.UNIFORM))
        )
        winding = int(round((mass / 3 - principal_energy) / (2 * np.pi)))
        lifted_mass = 3 * (principal_energy + 2 * np.pi * winding)
        dispersion_mass = 1 / float(
            np.mean(np.diag(block_curvature_tensor(block, step=0.003)))
        )
        coordinate_rows.append(
            (mass, principal_energy * 3, winding, lifted_mass, dispersion_mass)
        )
    check(
        "M-informed supplied phase lifts recover rest mass while direct-block dispersion tracks M",
        max(abs(row[3] / row[0] - 1) for row in coordinate_rows) < 3e-10
        and max(abs(row[4] / row[0] - 1) for row in coordinate_rows) < 0.001,
        coordinate_rows,
    )
    check(
        "principal rest phase alone aliases at least two hierarchy sectors",
        sum(row[2] != 0 for row in coordinate_rows) >= 2
        and max(abs(row[1] / row[0] - 1) for row in coordinate_rows) > 0.5,
        [(row[0], row[1], row[2]) for row in coordinate_rows],
    )

    fixed_force = direct_operator_response(
        compiled.coin,
        np.eye(4),
        compiled.sectors,
        1e-5,
        length=4096,
        momentum_width=0.006,
        duration=64,
    )
    check(
        "one fixed identity force recovers all three inertial masses",
        response_is_healthy(fixed_force)
        and max(abs(row[2] / row[0] - 1) for row in fixed_force.rows) < 0.005,
        fixed_force.rows,
    )

    held_out_short = direct_operator_response(
        held_out.coin,
        np.eye(4),
        held_out.sectors,
        1e-5,
        length=4096,
        momentum_width=0.006,
        duration=64,
    )
    check(
        "the frozen 64-tick held-out scale exposes light-sector window sensitivity",
        response_is_healthy(held_out_short)
        and abs(held_out_short.rows[0][2] / held_out_short.rows[0][0] - 1) > 0.005
        and max(abs(row[2] / row[0] - 1) for row in held_out_short.rows[1:])
        < 0.001,
        held_out_short.rows,
    )

    long_windows = (128, 160, 192, 256)
    convergence_rows = {}
    convergence_health = {}
    for label, candidate in (("reference", compiled), ("initial held-out", held_out)):
        responses = [
            direct_operator_response(
                candidate.coin,
                np.eye(4),
                candidate.sectors,
                1e-6,
                length=4096,
                momentum_width=0.006,
                duration=duration,
            )
            for duration in long_windows
        ]
        convergence_rows[label] = [
            [row[2] / row[0] - 1 for row in response.rows]
            for response in responses
        ]
        convergence_health[label] = [
            response_is_healthy(response) for response in responses
        ]
    check(
        "long-window fixed-force estimates remain within 0.2 percent at four tested windows",
        max(
            abs(error)
            for scale_rows in convergence_rows.values()
            for duration_rows in scale_rows
            for error in duration_rows
        )
        < 0.002
        and all(
            healthy
            for scale_rows in convergence_health.values()
            for healthy in scale_rows
        ),
        {"mass_errors": convergence_rows, "healthy": convergence_health},
    )

    post_repair_response = direct_operator_response(
        post_repair_held_out.coin,
        np.eye(4),
        post_repair_held_out.sectors,
        1e-6,
        length=4096,
        momentum_width=0.006,
        duration=160,
    )
    check(
        "the frozen post-repair held-out scale passes the long-window inertia protocol",
        response_is_healthy(post_repair_response)
        and max(
            abs(row[2] / row[0] - 1) for row in post_repair_response.rows
        )
        < 0.002,
        post_repair_response.rows,
    )

    charged = direct_operator_response(
        compiled.coin,
        compiled.recovered_mass,
        compiled.sectors,
        1e-7,
        length=4096,
        momentum_width=0.006,
        duration=64,
    )
    reversed_charged = direct_operator_response(
        compiled.coin,
        compiled.recovered_mass,
        compiled.sectors,
        -1e-7,
        length=4096,
        momentum_width=0.006,
        duration=64,
    )
    check(
        "the supplied Q=M charge gives conditional common acceleration with reversal",
        response_is_healthy(charged)
        and response_is_healthy(reversed_charged)
        and max(abs(row[1] / (-charged.strength) - 1) for row in charged.rows) < 0.004
        and max(
            abs(left[1] + right[1]) / abs(left[1])
            for left, right in zip(charged.rows, reversed_charged.rows)
        )
        < 2e-7,
        {"forward": charged.rows, "reverse": reversed_charged.rows},
    )

    schedules = [
        direct_operator_response(
            compiled.coin,
            compiled.recovered_mass,
            compiled.sectors,
            1e-7,
            ordering=ordering,
            length=4096,
            momentum_width=0.006,
            duration=160,
        )
        for ordering in ("pre", "post", "symmetric")
    ]
    accelerations = np.array(
        [[row[1] for row in response.rows] for response in schedules]
    )
    check(
        "all three healthy schedules agree and recover common acceleration",
        all(response_is_healthy(response) for response in schedules)
        and max(
            abs(row[1] / (-response.strength) - 1)
            for response in schedules
            for row in response.rows
        )
        < 0.004
        and np.max(np.ptp(accelerations, axis=0) / np.abs(np.mean(accelerations, axis=0)))
        < 0.004,
        accelerations.tolist(),
    )

    identity = np.eye(4)
    zero_values, zero_vectors = np.linalg.eigh(compiled.recovered_mass)
    zero_vector = zero_vectors[:, int(np.argmin(np.abs(zero_values)))]
    zero_projector = np.outer(zero_vector, zero_vector.conj())
    charge_family = {
        "I": identity,
        "M": compiled.recovered_mass,
        "2M": 2 * compiled.recovered_mass,
        "M+7P0": compiled.recovered_mass + 7 * zero_projector,
        "M+I": compiled.recovered_mass + identity,
        "M^2": compiled.recovered_mass @ compiled.recovered_mass,
        "f(M)": (
            0.7 * identity
            - 0.2 * compiled.recovered_mass
            + 0.03 * compiled.recovered_mass @ compiled.recovered_mass
        ),
    }
    ratio_rows = {
        label: [
            float(np.vdot(vector, charge @ vector).real) / mass
            for mass, _, vector in compiled.sectors
        ]
        for label, charge in charge_family.items()
    }
    zero_shifted_response = direct_operator_response(
        compiled.coin,
        charge_family["M+7P0"],
        compiled.sectors,
        charged.strength,
        length=4096,
        momentum_width=0.006,
        duration=64,
    )
    response_difference = float(
        np.max(
            np.abs(
                np.asarray(zero_shifted_response.rows, dtype=float)
                - np.asarray(charged.rows, dtype=float)
            )
        )
    )
    check(
        "the listed commuting charge family fixes only Q proportional to M on the massive subspace",
        max(ratio_rows["I"]) / min(ratio_rows["I"]) > 1000
        and np.ptp(ratio_rows["M"]) < 2e-9
        and np.ptp(ratio_rows["2M"]) < 4e-9
        and abs(np.mean(ratio_rows["2M"]) - 2) < 2e-9
        and np.ptp(ratio_rows["M+7P0"]) < 2e-9
        and np.linalg.norm(charge_family["M+7P0"] - compiled.recovered_mass) > 6.9
        and np.ptp(ratio_rows["M+I"]) > 1
        and np.ptp(ratio_rows["M^2"]) > 100
        and np.ptp(ratio_rows["f(M)"]) > 10,
        ratio_rows,
    )
    check(
        "zero-sector charge is invisible to the tested massive packet response",
        response_is_healthy(zero_shifted_response)
        and response_difference < 2e-12,
        {
            "norm(Q-M)": float(
                np.linalg.norm(charge_family["M+7P0"] - compiled.recovered_mass)
            ),
            "maximum_response_difference": response_difference,
        },
    )


def binding_ablation(compiled: Compiled) -> None:
    dimension = 4
    initial = np.zeros((9, 9, 9, dimension, 6, 6), dtype=complex)
    label = (compiled.sectors[0][2] + 1j * compiled.sectors[1][2]) / np.sqrt(2)
    for direction in range(6):
        initial[0, 0, 0, :, direction, direction] = label / np.sqrt(6)

    full_contact = c221.shared_contact_operator(compiled.coin)
    identity_contact = np.eye(dimension * 36, dtype=complex)
    no_rest_coin = np.kron(
        np.eye(dimension), c210.P_SCALAR - c210.P_EVEN
    ) + np.kron(compiled.register, c210.P_VECTOR)
    no_rest_contact = c221.shared_contact_operator(no_rest_coin)
    _, identity_register_coin = c220.common_register_coin(np.eye(dimension))
    identity_register_contact = c221.shared_contact_operator(identity_register_coin)
    variants = {
        "full": (initial.copy(), full_contact),
        "identity coin": (initial.copy(), identity_contact),
        "rest deleted": (initial.copy(), no_rest_contact),
        "register deleted": (initial.copy(), identity_register_contact),
    }
    released = initial.copy()
    for _ in range(8):
        variants = {
            label_name: (
                c221.apply_register_relative_step(state, contact, interaction=True),
                contact,
            )
            for label_name, (state, contact) in variants.items()
        }
        released = c221.apply_register_relative_step(
            released, full_contact, interaction=False
        )
    probabilities = {
        label_name: c221.contact_probability(state)
        for label_name, (state, _) in variants.items()
    }
    check(
        "equal-direction kinematics retains the object after every mass-contact deletion",
        min(probabilities.values()) > 1 - 3e-10,
        probabilities,
    )
    check(
        "deleting the complete contact replacement releases the prepared object",
        c221.contact_probability(released) < 0.25
        and abs(np.linalg.norm(released) - 1) < 3e-10,
        c221.contact_probability(released),
    )


def representation_composition_pointer_and_field_controls(
    compiled: Compiled, held_out: Compiled
) -> None:
    rng = np.random.default_rng(1222)
    raw = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    basis, _ = np.linalg.qr(raw)
    represented_mass = basis @ compiled.recovered_mass @ basis.conj().T
    represented_register = basis @ compiled.register @ basis.conj().T
    represented_recovered, represented_coin = c220.common_register_coin(
        represented_register
    )
    check(
        "passive register-basis changes preserve mass register and complete coin",
        np.linalg.norm(represented_recovered - represented_mass) < 2e-8
        and np.linalg.norm(
            represented_coin
            - np.kron(basis, np.eye(6))
            @ compiled.coin
            @ np.kron(basis.conj().T, np.eye(6))
        )
        < 2e-8,
    )

    identity = np.eye(4)
    composition_errors = {}
    for label, candidate in (("reference", compiled), ("held-out", held_out)):
        total_mass = np.kron(candidate.recovered_mass, identity) + np.kron(
            identity, candidate.recovered_mass
        )
        total_rest = c220.unitary_function(total_mass, 1 / 3)
        separate_rest = np.kron(
            c220.unitary_function(candidate.recovered_mass, 1 / 3),
            c220.unitary_function(candidate.recovered_mass, 1 / 3),
        )
        composition_errors[label] = float(np.linalg.norm(total_rest - separate_rest))
    check(
        "the supplied additive composition factorizes at reference and held-out scales",
        max(composition_errors.values()) < 3e-8,
        composition_errors,
    )

    first = compiled.sectors[0][2]
    second = compiled.sectors[1][2]
    matter = (first + second) / np.sqrt(2)
    second_projector = np.outer(second, second.conj())
    zero = np.array((1, 0), dtype=complex)
    x_gate = np.array(((0, 1), (1, 0)), dtype=complex)
    write = np.kron(identity - second_projector, np.eye(2)) + np.kron(
        second_projector, x_gate
    )
    one_pointer = write @ np.kron(matter, zero)
    cnot = np.array(
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)),
        dtype=complex,
    )
    copy = np.kron(identity, cnot)
    two_pointers = copy @ np.kron(one_pointer, zero)
    source_values = (
        float(np.vdot(matter, compiled.recovered_mass @ matter).real),
        float(
            np.vdot(
                one_pointer,
                np.kron(compiled.recovered_mass, np.eye(2)) @ one_pointer,
            ).real
        ),
        float(
            np.vdot(
                two_pointers,
                np.kron(compiled.recovered_mass, np.eye(4)) @ two_pointers,
            ).real
        ),
    )
    one_probabilities = np.sum(np.abs(one_pointer.reshape(4, 2)) ** 2, axis=0)
    two_probabilities = np.sum(
        np.abs(two_pointers.reshape(4, 2, 2)) ** 2, axis=0
    )
    mass_one = np.kron(compiled.recovered_mass, np.eye(2))
    mass_two = np.kron(compiled.recovered_mass, np.eye(4))
    check(
        "abstract orthogonal redundant pointers preserve the declared matter mass operator",
        np.linalg.norm(write.conj().T @ write - np.eye(8)) < 3e-10
        and np.linalg.norm(copy.conj().T @ copy - np.eye(16)) < 3e-10
        and np.linalg.norm(write.conj().T @ mass_one @ write - mass_one) < 2e-8
        and np.linalg.norm(copy.conj().T @ mass_two @ copy - mass_two) < 2e-8
        and np.linalg.norm(
            np.kron(compiled.recovered_mass, np.eye(6)) @ compiled.coin
            - compiled.coin @ np.kron(compiled.recovered_mass, np.eye(6))
        )
        < 2e-8
        and max(abs(value - source_values[0]) for value in source_values) < 3e-8
        and np.max(np.abs(one_probabilities - np.array((0.5, 0.5)))) < 3e-10
        and np.max(
            np.abs(two_probabilities - np.array(((0.5, 0.0), (0.0, 0.5))))
        )
        < 3e-10,
        {
            "source": source_values,
            "one_pointer": one_probabilities.tolist(),
            "two_pointers": two_probabilities.tolist(),
        },
    )

    side = 31
    source = c211.point_source(side)
    field = c216.scalar_field(c216.solve_coin_field(source)).real
    gradient = float(c211.gradient(field, (4, 0, 0))[0])
    coupling = 0.001
    source_mass = compiled.sectors[0][0]
    strength = -(coupling**2) * source_mass * gradient
    response = direct_operator_response(
        compiled.coin,
        compiled.recovered_mass,
        compiled.sectors,
        strength,
        length=4096,
        momentum_width=0.006,
        duration=64,
    )
    check(
        "one host-extracted source mass gives conditional response to a sampled scalar-field gradient",
        gradient < 0
        and response_is_healthy(response)
        and max(abs(row[1] / (-strength) - 1) for row in response.rows) < 0.004,
        {"gradient": gradient, "strength": strength, "rows": response.rows},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    compiled = compile_operator(REFERENCE_SCALE)
    held_out = compile_operator(HELD_OUT_SCALE)
    post_repair_held_out = compile_operator(POST_REPAIR_HELD_OUT_SCALE)
    operator_and_compiler_controls(compiled)
    phase_dispersion_and_inertia(compiled, held_out, post_repair_held_out)
    binding_ablation(compiled)
    representation_composition_pointer_and_field_controls(compiled, held_out)
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
