#!/usr/bin/env python3
"""Cycle 221: test one supplied mass operator across effective kernels.

Lift the Cycle-219 proper-cubic matter/field family into the fixed Cycle-220
phase register.  Reuse M(S) in separately supplied contact, fixed-force,
M-charged response, and direct static-exchange fixtures.  Distinguish what M
actually controls from what the equal-direction contact geometry controls.

The phase register, its population, Cayley/rest map, spectral preparation,
contact compiler, coordinate kick, charge choice, additive composition, and
static exchange action remain candidate inputs.  This is an effective-kernel
consistency probe, not one autonomous common law, a selected spectrum, or a
gravity theory.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

import active_cubic_source_response_cycle211_2026_07_16 as c211
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import generated_beta_phase_register_cycle220_2026_07_16 as c220
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import virtual_exchange_green_kernel_cycle216_2026_07_16 as c216


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "OPERATOR_MASS_EQUIVALENCE_CYCLE221_NOTE_2026-07-17.md"
)

REGISTER_DIMENSION = 9
COUPLING = 0.05
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
        "one supplied operator",
        "separately supplied effective kernels",
        "rest/dispersion/fixed-force inertia",
        "equal-direction kinematics binds",
        "conditional common acceleration",
        "no beta lookup during the tested update",
        "charge-family ablation",
        "orthogonal redundant records",
        "principal-phase alias",
        "register population remains supplied",
        "not a selected particle spectrum",
        "not a gravity theory",
        "no axiom conclusion",
        "apadula",
        "zych",
        "ahlbrecht",
        "thirring-qca",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves the operator gain and supplied seams", not missing, missing)


def positive_sectors(
    register: np.ndarray, mass: np.ndarray
) -> list[tuple[float, float, np.ndarray]]:
    rows = []
    for beta, _, vector in c220.register_eigenpairs(register):
        eigenmass = float(np.vdot(vector, mass @ vector).real)
        if eigenmass > 1e-8:
            rows.append((eigenmass, beta, vector))
    return sorted(rows, key=lambda row: row[0])


def shared_contact_operator(register_coin: np.ndarray) -> np.ndarray:
    """Abstract shared composite register and two direction factors."""
    dimension = register_coin.shape[0] // 6
    operator = np.eye(dimension * 36, dtype=complex)
    diagonal = [
        register_index * 36 + direction * 6 + direction
        for register_index in range(dimension)
        for direction in range(6)
    ]
    operator[np.ix_(diagonal, diagonal)] = register_coin
    return operator


def apply_register_relative_step(
    state: np.ndarray,
    contact: np.ndarray,
    *,
    interaction: bool,
) -> np.ndarray:
    """Strict relative-coordinate step with no eigensector lookup."""
    length = state.shape[0]
    dimension = state.shape[3]
    flat = state.reshape(length, length, length, dimension, 36)
    independent = np.kron(c210.free_coin(), c210.free_coin())
    mixed = np.einsum("ab,xyzrb->xyzra", independent, flat, optimize=True)
    if interaction:
        mixed[0, 0, 0] = (contact @ flat[0, 0, 0].reshape(-1)).reshape(
            dimension, 36
        )
    mixed = mixed.reshape(length, length, length, dimension, 6, 6)
    output = np.zeros_like(mixed)
    for first in range(6):
        for second in range(6):
            shift = tuple(
                int(value)
                for value in c210.DIRECTIONS[first] - c210.DIRECTIONS[second]
            )
            output[..., first, second] += np.roll(
                mixed[..., first, second], shift, axis=(0, 1, 2)
            )
    return output


def contact_probability(state: np.ndarray) -> float:
    return float(np.sum(np.abs(state[0, 0, 0]) ** 2))


def register_weight(state: np.ndarray, vector: np.ndarray) -> float:
    component = np.einsum("r,xyzrij->xyzij", vector.conj(), state, optimize=True)
    return float(np.linalg.norm(component) ** 2)


def exact_binding_controls(
    register: np.ndarray,
    mass: np.ndarray,
    register_coin: np.ndarray,
    sectors: list[tuple[float, float, np.ndarray]],
) -> None:
    dimension = register.shape[0]
    contact = shared_contact_operator(register_coin)
    check(
        "the abstract shared-register contact operator is exactly unitary",
        np.linalg.norm(contact.conj().T @ contact - np.eye(dimension * 36)) < 8e-12,
    )

    covariance = []
    for frame in c210.proper_cubic_frames():
        direction = c210.direction_permutation(frame)
        representation = np.kron(np.eye(dimension), np.kron(direction, direction))
        covariance.append(
            np.linalg.norm(representation @ contact @ representation.conj().T - contact)
        )
    check(
        "the contact block is covariant in all 24 proper-cubic frames",
        len(covariance) == 24 and max(covariance) < 8e-12,
        max(covariance),
    )

    label = (sectors[0][2] + 1j * sectors[1][2]) / np.sqrt(2)
    length = 9
    initial = np.zeros((length, length, length, dimension, 6, 6), dtype=complex)
    for direction in range(6):
        initial[0, 0, 0, :, direction, direction] = label / np.sqrt(6)
    identity_contact = np.eye(dimension * 36, dtype=complex)
    no_rest_coin = np.kron(
        np.eye(dimension), c210.P_SCALAR - c210.P_EVEN
    ) + np.kron(register, c210.P_VECTOR)
    no_rest_contact = shared_contact_operator(no_rest_coin)
    _, identity_register_coin = c220.common_register_coin(np.eye(dimension))
    identity_register_contact = shared_contact_operator(identity_register_coin)
    bound_variants = {
        "C(S)": initial.copy(),
        "C to identity": initial.copy(),
        "rest factor deleted": initial.copy(),
        "S to identity": initial.copy(),
    }
    contacts = {
        "C(S)": contact,
        "C to identity": identity_contact,
        "rest factor deleted": no_rest_contact,
        "S to identity": identity_register_contact,
    }
    deleted = initial.copy()
    initial_weights = [register_weight(initial, row[2]) for row in sectors[:2]]
    for _ in range(8):
        for label_name in bound_variants:
            bound_variants[label_name] = apply_register_relative_step(
                bound_variants[label_name], contacts[label_name], interaction=True
            )
        deleted = apply_register_relative_step(deleted, contact, interaction=False)
    bound = bound_variants["C(S)"]
    final_weights = [register_weight(bound, row[2]) for row in sectors[:2]]
    check(
        "the supplied C(S) contact block preserves two sector amplitudes",
        abs(np.linalg.norm(bound) - 1) < 8e-12
        and contact_probability(bound) > 1 - 8e-12
        and max(abs(left - right) for left, right in zip(initial_weights, final_weights))
        < 8e-12,
        {
            "contact": contact_probability(bound),
            "initial_weights": initial_weights,
            "final_weights": final_weights,
        },
    )
    ablation_contacts = {
        label_name: contact_probability(state)
        for label_name, state in bound_variants.items()
    }
    check(
        "equal-direction kinematics binds even when M-dependent contact data are deleted",
        min(ablation_contacts.values()) > 1 - 2e-11,
        ablation_contacts,
    )
    check(
        "contact-law deletion releases the same prepared composite",
        abs(np.linalg.norm(deleted) - 1) < 8e-12
        and contact_probability(deleted) < 0.25,
        contact_probability(deleted),
    )

    rng = np.random.default_rng(221)
    raw = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    basis, _ = np.linalg.qr(raw)
    represented_register = basis @ register @ basis.conj().T
    _, represented_coin = c220.common_register_coin(represented_register)
    represented_contact = shared_contact_operator(represented_coin)
    expected = np.kron(basis, np.eye(36)) @ contact @ np.kron(
        basis.conj().T, np.eye(36)
    )
    check(
        "passive register-basis changes preserve the complete contact block",
        np.linalg.norm(represented_contact - expected) < 7e-11,
    )

    check(
        "the contact law commutes with the Cayley mass operator",
        np.linalg.norm(
            contact @ np.kron(mass, np.eye(36))
            - np.kron(mass, np.eye(36)) @ contact
        )
        < 8e-12,
    )


def local_register_step(state: np.ndarray, coin: np.ndarray) -> np.ndarray:
    length, dimension, _ = state.shape
    mixed = (coin @ state.reshape(length, dimension * 6).T).T.reshape(
        length, dimension, 6
    )
    output = np.zeros_like(mixed)
    for direction in range(6):
        output[:, :, direction] = np.roll(
            mixed[:, :, direction], int(c210.DIRECTIONS[direction, 0]), axis=0
        )
    return output


def apply_position_charge(
    state: np.ndarray,
    positions: np.ndarray,
    charge: np.ndarray,
    strength: float,
) -> np.ndarray:
    values, vectors = np.linalg.eigh(charge)
    eigenbasis = np.einsum("rk,xrd->xkd", vectors.conj(), state, optimize=True)
    eigenbasis *= np.exp(
        1j * strength * positions[:, None, None] * values[None, :, None]
    )
    return np.einsum("rk,xkd->xrd", vectors, eigenbasis, optimize=True)


def prepare_register_packet(
    sectors: list[tuple[float, float, np.ndarray]],
    *,
    length: int,
    momentum_width: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    dimension = len(sectors[0][2])
    state = np.zeros((length, dimension, 6), dtype=complex)
    positions = momenta = None
    amplitudes = np.ones(len(sectors), dtype=complex) / np.sqrt(len(sectors))
    for amplitude, (_, beta, vector) in zip(amplitudes, sectors):
        species = c219.common_species(beta)
        branch_positions, branch_momenta, packet = c210.prepare_molecular_packet(
            species, length, momentum_width
        )
        state += amplitude * np.einsum("r,xd->xrd", vector, packet, optimize=True)
        positions, momenta = branch_positions, branch_momenta
    state /= np.linalg.norm(state)
    assert positions is not None and momenta is not None
    return positions, momenta, state


def sector_component(state: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return np.einsum("r,xrd->xd", vector.conj(), state, optimize=True)


def sector_mean_position(
    state: np.ndarray, vector: np.ndarray, positions: np.ndarray
) -> tuple[float, float]:
    component = sector_component(state, vector)
    weight = float(np.linalg.norm(component) ** 2)
    density = np.sum(np.abs(component) ** 2, axis=1)
    return float(np.sum(density * positions).real / weight), weight


@dataclass(frozen=True)
class OperatorResponse:
    ordering: str
    strength: float
    rows: tuple[tuple[float, float, float, float, float], ...]
    norm: float
    final_weight_sum: float
    boundary_probability: float


def operator_response(
    register_coin: np.ndarray,
    charge: np.ndarray,
    sectors: list[tuple[float, float, np.ndarray]],
    strength: float,
    *,
    ordering: str = "symmetric",
    length: int = 2048,
    momentum_width: float = 0.012,
    duration: int = 64,
) -> OperatorResponse:
    positions, momenta, state = prepare_register_packet(
        sectors, length=length, momentum_width=momentum_width
    )
    centres = [[] for _ in sectors]
    weights = [[] for _ in sectors]
    for row_index, (_, _, vector) in enumerate(sectors):
        centre, weight = sector_mean_position(state, vector, positions)
        centres[row_index].append(centre)
        weights[row_index].append(weight)
    for _ in range(duration):
        if ordering == "pre":
            state = local_register_step(
                apply_position_charge(state, positions, charge, strength),
                register_coin,
            )
        elif ordering == "post":
            state = apply_position_charge(
                local_register_step(state, register_coin),
                positions,
                charge,
                strength,
            )
        elif ordering == "symmetric":
            state = apply_position_charge(
                local_register_step(
                    apply_position_charge(
                        state, positions, charge, strength / 2
                    ),
                    register_coin,
                ),
                positions,
                charge,
                strength / 2,
            )
        else:
            raise ValueError(ordering)
        for row_index, (_, _, vector) in enumerate(sectors):
            centre, weight = sector_mean_position(state, vector, positions)
            centres[row_index].append(centre)
            weights[row_index].append(weight)

    times = np.arange(duration + 1, dtype=float)
    response_rows = []
    charge_values = []
    for eigenmass, beta, vector in sectors:
        charge_values.append(float(np.vdot(vector, charge @ vector).real))
    for row_index, ((eigenmass, beta, vector), charge_value) in enumerate(
        zip(sectors, charge_values)
    ):
        displacement = np.asarray(centres[row_index]) - centres[row_index][0]
        acceleration = float(2 * np.polyfit(times, displacement, 2)[0])
        # With the walk/Fourier convention used here exp(+i strength x Q)
        # produces the signed force -strength*Q.
        force = -strength * charge_value
        measured_mass = force / acceleration if abs(acceleration) > 1e-15 else np.inf
        component = sector_component(state, vector)
        component /= np.linalg.norm(component)
        band_probability = c210.branch_probability(
            component, momenta, c219.common_species(beta)
        )
        response_rows.append(
            (
                eigenmass,
                acceleration,
                measured_mass,
                band_probability,
                weights[row_index][-1],
            )
        )
    return OperatorResponse(
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


def four_mass_coordinates(
    register: np.ndarray,
    mass: np.ndarray,
    register_coin: np.ndarray,
    sectors: list[tuple[float, float, np.ndarray]],
) -> None:
    tested = sectors[:3]
    static_rows = []
    for eigenmass, beta, vector in tested:
        block = c220.extract_direction_block(register_coin, vector)
        rest_energy = float(np.angle(np.vdot(c210.UNIFORM, block @ c210.UNIFORM)))
        rest_mass = rest_energy / c219.C_SQUARED
        dispersion_mass = 1 / float(
            np.mean(
                np.diag(c210.curvature_tensor(c219.common_species(beta), step=1e-4))
            )
        )
        static_rows.append((eigenmass, rest_mass, dispersion_mass))
    check(
        "three unaliased M eigenvalues match designed rest and dispersion mass",
        max(abs(row[1] / row[0] - 1) for row in static_rows) < 3e-12
        and max(abs(row[2] / row[0] - 1) for row in static_rows) < 5e-6,
        static_rows,
    )

    alias_rows = []
    for eigenmass, _, vector in sectors:
        block = c220.extract_direction_block(register_coin, vector)
        principal_energy = float(
            np.angle(np.vdot(c210.UNIFORM, block @ c210.UNIFORM))
        )
        lifted_energy = principal_energy
        while lifted_energy < eigenmass * c219.C_SQUARED - np.pi:
            lifted_energy += 2 * np.pi
        alias_rows.append(
            (
                eigenmass,
                principal_energy / c219.C_SQUARED,
                lifted_energy / c219.C_SQUARED,
            )
        )
    check(
        "the largest sector exposes a principal-phase alias and supplied lift",
        abs(alias_rows[-1][1] / alias_rows[-1][0] - 1) > 0.5
        and abs(alias_rows[-1][2] / alias_rows[-1][0] - 1) < 3e-12
        and max(abs(row[1] / row[0] - 1) for row in alias_rows[:-1]) < 3e-12,
        alias_rows,
    )

    fixed_force = operator_response(
        register_coin, np.eye(register.shape[0]), tested, 3.5e-5
    )
    check(
        "one fixed force independently recovers three inertial masses",
        abs(fixed_force.norm - 1) < 8e-12
        and abs(fixed_force.final_weight_sum - 1) < 8e-12
        and fixed_force.boundary_probability < 2e-12
        and max(abs(row[2] / row[0] - 1) for row in fixed_force.rows) < 0.012
        and all(row[1] < 0 and row[2] > 0 for row in fixed_force.rows)
        and min(row[3] for row in fixed_force.rows) > 0.998,
        {
            "rows": fixed_force.rows,
            "boundary": fixed_force.boundary_probability,
        },
    )

    m_charged = operator_response(register_coin, mass, tested, 3.5e-5)
    reversed_m_charged = operator_response(register_coin, mass, tested, -3.5e-5)
    check(
        "the supplied Q=M coupling gives conditional common acceleration with signed reversal",
        max(abs(row[1] / (-m_charged.strength) - 1) for row in m_charged.rows)
        < 0.012
        and max(
            abs(left[1] + right[1]) / abs(left[1])
            for left, right in zip(m_charged.rows, reversed_m_charged.rows)
        )
        < 2e-8,
        {"positive_strength": m_charged.rows, "negative_strength": reversed_m_charged.rows},
    )

    schedules = [
        operator_response(register_coin, mass, tested[:2], 2.5e-5, ordering=ordering)
        for ordering in ("pre", "post", "symmetric")
    ]
    schedule_accelerations = np.asarray(
        [[abs(row[1]) for row in response.rows] for response in schedules]
    )
    check(
        "pre post and symmetric schedules agree at the tested weak strength",
        np.max(np.ptp(schedule_accelerations, axis=0) / np.mean(schedule_accelerations, axis=0))
        < 0.004,
        schedule_accelerations.tolist(),
    )

    identity = np.eye(register.shape[0])
    charge_family = {
        "I": identity,
        "M": mass,
        "2M": 2 * mass,
        "M+I": mass + identity,
        "M^2": mass @ mass,
    }
    ratio_rows = {}
    for label, charge in charge_family.items():
        ratio_rows[label] = [
            float(np.vdot(vector, charge @ vector).real) / eigenmass
            for eigenmass, _, vector in tested
        ]
    check(
        "the charge-family ablation selects Q proportional to M on tested sectors",
        np.ptp(ratio_rows["M"]) < 2e-12
        and np.ptp(ratio_rows["2M"]) < 4e-12
        and abs(np.mean(ratio_rows["2M"]) - 2) < 2e-12
        and np.ptp(ratio_rows["I"]) > 0.7
        and np.ptp(ratio_rows["M+I"]) > 0.7
        and np.ptp(ratio_rows["M^2"]) > 3,
        ratio_rows,
    )


def swap_operator(dimension: int) -> np.ndarray:
    swap = np.zeros((dimension * dimension, dimension * dimension), dtype=complex)
    for left in range(dimension):
        for right in range(dimension):
            swap[right * dimension + left, left * dimension + right] = 1
    return swap


def exchange_and_composition_controls(
    register: np.ndarray,
    mass: np.ndarray,
    register_coin: np.ndarray,
    sectors: list[tuple[float, float, np.ndarray]],
) -> None:
    tested = sectors[:3]
    side = 31
    source = c211.point_source(side)
    coin_field = c216.solve_coin_field(source)
    kernel = c216.scalar_field(coin_field).real
    gradient = float(c211.gradient(kernel, (4, 0, 0))[0])
    source_mass, _, _ = tested[0]
    # exp(+i strength x M) has physical force -strength M.  The minus sign
    # below therefore reproduces +g^2 m_source M grad(K), toward the source.
    exchange_strength = -COUPLING**2 * source_mass * gradient
    response = operator_response(register_coin, mass, tested, exchange_strength)
    check(
        "one host-extracted source eigenvalue gives conditional common response",
        gradient < 0
        and all(row[1] < 0 and row[2] > 0 for row in response.rows)
        and max(abs(row[1] / (-exchange_strength) - 1) for row in response.rows)
        < 0.012
        and max(abs(row[2] / row[0] - 1) for row in response.rows) < 0.012,
        {
            "source_mass": source_mass,
            "gradient": gradient,
            "rows": response.rows,
        },
    )

    separation = (4, 0, 0)
    exchange = -COUPLING**2 * float(kernel[separation]) * np.kron(mass, mass)
    swap = swap_operator(register.shape[0])
    check(
        "one reciprocal M tensor M exchange vertex is Hermitian and swap symmetric",
        np.linalg.norm(exchange - exchange.conj().T) < 2e-12
        and np.linalg.norm(swap @ exchange @ swap - exchange) < 2e-12,
    )

    first_mass, _, first = tested[0]
    second_mass, _, second = tested[1]
    pair = np.kron(first, second)
    pair_energy = float(np.vdot(pair, exchange @ pair).real)
    expected_energy = -COUPLING**2 * float(kernel[separation]) * first_mass * second_mass
    check(
        "the operator exchange reduces to the sector pair potential without lookup",
        abs(pair_energy - expected_energy) < 2e-13 and pair_energy < 0,
        (pair_energy, expected_energy),
    )

    identity = np.eye(register.shape[0])
    total_mass = np.kron(mass, identity) + np.kron(identity, mass)
    total_rest = c220.unitary_function(total_mass, 1 / 3)
    separate_rest = np.kron(
        c220.unitary_function(mass, 1 / 3),
        c220.unitary_function(mass, 1 / 3),
    )
    check(
        "the supplied additive composition makes the rest unitary factorize",
        np.linalg.norm(total_rest - separate_rest) < 2e-11
        and abs(float(np.vdot(pair, total_mass @ pair).real) - first_mass - second_mass)
        < 2e-11,
    )

    coherent = (first + second) / np.sqrt(2)
    coherent_pair = np.kron(coherent, coherent)
    fixed_exposure = 2048.0
    exchange_unitary = c220.unitary_function(exchange, fixed_exposure)
    evolved = (exchange_unitary @ coherent_pair).reshape(
        register.shape[0], register.shape[0]
    )
    schmidt = np.linalg.svd(evolved, compute_uv=False)
    check(
        "the direct exchange vertex entangles a supplied coherent register pair",
        schmidt[1] > 0.04 and abs(np.linalg.norm(schmidt) - 1) < 2e-12,
        {"fixed_exposure": fixed_exposure, "schmidt": schmidt[:4].tolist()},
    )

    zero_record = np.array((1, 0), dtype=complex)
    x_record = np.array(((0, 1), (1, 0)), dtype=complex)
    second_projector = np.outer(second, second.conj())
    write = np.kron(np.eye(register.shape[0]) - second_projector, np.eye(2))
    write += np.kron(second_projector, x_record)
    matter = coherent
    one_record = write @ np.kron(matter, zero_record)
    cnot = np.array(
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)),
        dtype=complex,
    )
    copy = np.kron(np.eye(register.shape[0]), cnot)
    two_records = copy @ np.kron(one_record, zero_record)
    source_values = (
        float(np.vdot(matter, mass @ matter).real),
        float(
            np.vdot(
                one_record,
                np.kron(mass, np.eye(2)) @ one_record,
            ).real
        ),
        float(
            np.vdot(
                two_records,
                np.kron(mass, np.eye(4)) @ two_records,
            ).real
        ),
    )
    one_probabilities = np.sum(
        np.abs(one_record.reshape(register.shape[0], 2)) ** 2, axis=0
    )
    two_probabilities = np.sum(
        np.abs(two_records.reshape(register.shape[0], 2, 2)) ** 2, axis=0
    )
    check(
        "orthogonal redundant records preserve the declared matter source operator",
        np.linalg.norm(write.conj().T @ write - np.eye(2 * register.shape[0]))
        < 2e-12
        and np.linalg.norm(copy.conj().T @ copy - np.eye(4 * register.shape[0]))
        < 2e-12
        and max(abs(value - source_values[0]) for value in source_values) < 2e-12
        and np.max(np.abs(one_probabilities - np.array((0.5, 0.5)))) < 2e-12
        and abs(two_probabilities[0, 1]) < 2e-12
        and abs(two_probabilities[1, 0]) < 2e-12
        and np.max(
            np.abs(
                np.diag(two_probabilities) - np.array((0.5, 0.5))
            )
        )
        < 2e-12,
        {
            "source_values": source_values,
            "one_record": one_probabilities.tolist(),
            "two_records": two_probabilities.tolist(),
        },
    )

    check(
        "the supplied effective kernels conserve rather than generate register population",
        np.linalg.norm(register @ mass - mass @ register) < 3e-12
        and np.linalg.norm(
            register_coin @ np.kron(register, np.eye(6))
            - np.kron(register, np.eye(6)) @ register_coin
        )
        < 4e-12,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    register = c220.cyclic_shift(REGISTER_DIMENSION)
    mass, register_coin = c220.common_register_coin(register)
    sectors = positive_sectors(register, mass)
    check(
        "the probe selects sectors spectrally rather than from a beta table",
        len(sectors) == 4
        and all(sectors[index][0] < sectors[index + 1][0] for index in range(3)),
        [(row[0], row[1]) for row in sectors],
    )
    phases = np.angle(np.linalg.eigvals(register_coin))
    clifford_grid_distance = np.min(
        np.abs(
            np.angle(
                np.exp(
                    1j
                    * (
                        phases[:, None]
                        - np.arange(-4, 5, dtype=float)[None, :] * np.pi / 4
                    )
                )
            )
        ),
        axis=1,
    )
    check(
        "the abstract coin has eigenphases outside the pi-over-four grid",
        np.max(clifford_grid_distance) > 0.08,
        float(np.max(clifford_grid_distance)),
    )
    exact_binding_controls(register, mass, register_coin, sectors)
    four_mass_coordinates(register, mass, register_coin, sectors)
    exchange_and_composition_controls(register, mass, register_coin, sectors)
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
