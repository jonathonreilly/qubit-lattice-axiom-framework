#!/usr/bin/env python3
"""Cycle 202: local-force bridge from dispersion to inertial response.

The probe prepares a localized positive-band packet in the two effective
one-dimensional sectors of the Cycle-201 candidates.  It applies a literal
onsite phase gradient, evolves with either the strict range-one QCA step or
the finite-range Dirac Hamiltonian generator, and measures acceleration from
the packet centre.  The measured F/a is compared with the independently
derived low-momentum curvature mass.

The force profile and the mass coefficient remain supplied controls.  The
packet is not claimed to be a self-bound particle or a generated record.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "LOCAL_FORCE_INERTIAL_MASS_BRIDGE_CYCLE202_NOTE_2026-07-16.md"
)

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)

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
        "onsite phase gradient",
        "force remains supplied",
        "dispersion mass",
        "inertial response",
        "not a self-bound particle",
        "spectator record",
        "strict range-one qca",
        "finite-range generator",
        "mass-to-gravity map remains open",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves the conditional force-response boundary", not missing, missing)


def wrapped_momenta(length: int) -> np.ndarray:
    return 2 * np.pi * np.fft.fftfreq(length)


def positive_band_spinor(route: str, momenta: np.ndarray, mass: float) -> np.ndarray:
    """Smooth positive-energy/e^{-i omega} spinor on the x-directed slice."""
    if route == "hamiltonian":
        angle = np.arctan2(np.sin(momenta), mass)
    elif route == "qca":
        normalization = np.sqrt(1 - mass * mass)
        angle = np.arctan2(
            -mass * np.ones_like(momenta), normalization * np.sin(momenta)
        )
    else:
        raise ValueError(route)
    return np.stack((np.cos(angle / 2), np.sin(angle / 2)), axis=-1).astype(complex)


def prepare_packet(
    route: str, length: int, mass: float, momentum_width: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    positions = np.arange(length, dtype=float) - length // 2
    momenta = wrapped_momenta(length)
    amplitude = np.exp(-0.5 * (momenta / momentum_width) ** 2)
    packet_k = amplitude[:, None] * positive_band_spinor(route, momenta, mass)
    packet_k /= np.linalg.norm(packet_k)
    packet_x = np.fft.ifft(packet_k, axis=0, norm="ortho")
    packet_x = np.roll(packet_x, length // 2, axis=0)
    return positions, momenta, packet_x


def qca_bloch(momentum: float, mass: float) -> np.ndarray:
    normalization = np.sqrt(1 - mass * mass)
    return np.array(
        [
            [normalization * np.exp(-1j * momentum), 1j * mass],
            [1j * mass, normalization * np.exp(1j * momentum)],
        ],
        dtype=complex,
    )


def qca_local_step(packet: np.ndarray, mass: float) -> np.ndarray:
    """Literal range-one form of the x-slice paired-Weyl QCA."""
    normalization = np.sqrt(1 - mass * mass)
    result = np.empty_like(packet)
    result[:, 0] = normalization * np.roll(packet[:, 0], 1) + 1j * mass * packet[:, 1]
    result[:, 1] = 1j * mass * packet[:, 0] + normalization * np.roll(packet[:, 1], -1)
    return result


def qca_step_with_force(
    packet: np.ndarray,
    positions: np.ndarray,
    mass: float,
    force: float,
    ordering: str = "symmetric",
) -> np.ndarray:
    full_kick = np.exp(1j * force * positions)[:, None]
    half_kick = np.exp(0.5j * force * positions)[:, None]
    if ordering == "pre":
        return qca_local_step(full_kick * packet, mass)
    if ordering == "post":
        return full_kick * qca_local_step(packet, mass)
    if ordering == "symmetric":
        return half_kick * qca_local_step(half_kick * packet, mass)
    raise ValueError(ordering)


def hamiltonian_bloch_action(
    packet_k: np.ndarray, momenta: np.ndarray, mass: float
) -> np.ndarray:
    sine = np.sin(momenta)
    return np.stack(
        (
            mass * packet_k[:, 0] + sine * packet_k[:, 1],
            sine * packet_k[:, 0] - mass * packet_k[:, 1],
        ),
        axis=1,
    )


def hamiltonian_local_action(packet: np.ndarray, mass: float) -> np.ndarray:
    """Literal range-one stencil for sin(k) SX + m SZ."""
    def sine_action(component: np.ndarray) -> np.ndarray:
        return (np.roll(component, -1) - np.roll(component, 1)) / (2j)

    return np.stack(
        (
            mass * packet[:, 0] + sine_action(packet[:, 1]),
            sine_action(packet[:, 0]) - mass * packet[:, 1],
        ),
        axis=1,
    )


def hamiltonian_step_with_force(
    packet: np.ndarray,
    momenta: np.ndarray,
    positions: np.ndarray,
    mass: float,
    force: float,
    time_step: float,
) -> np.ndarray:
    half_kick = np.exp(0.5j * force * positions * time_step)[:, None]
    packet = half_kick * packet
    packet_k = np.fft.fft(packet, axis=0, norm="ortho")
    sine = np.sin(momenta)
    energy = np.sqrt(sine * sine + mass * mass)
    h_packet = hamiltonian_bloch_action(packet_k, momenta, mass)
    packet_k = (
        np.cos(energy * time_step)[:, None] * packet_k
        - 1j * (np.sin(energy * time_step) / energy)[:, None] * h_packet
    )
    packet = np.fft.ifft(packet_k, axis=0, norm="ortho")
    return half_kick * packet


def position_density(packet: np.ndarray) -> np.ndarray:
    axes = tuple(range(1, packet.ndim))
    return np.sum(np.abs(packet) ** 2, axis=axes)


def mean_position(packet: np.ndarray, positions: np.ndarray) -> float:
    return float(np.sum(position_density(packet) * positions).real)


def position_variance(packet: np.ndarray, positions: np.ndarray) -> float:
    centre = mean_position(packet, positions)
    return float(np.sum(position_density(packet) * (positions - centre) ** 2).real)


def boundary_probability(packet: np.ndarray, positions: np.ndarray) -> float:
    return float(np.sum(position_density(packet)[np.abs(positions) > len(positions) / 4]))


def positive_band_probability(
    route: str, packet: np.ndarray, momenta: np.ndarray, mass: float
) -> float:
    packet_k = np.fft.fft(packet, axis=0, norm="ortho")
    spinors = positive_band_spinor(route, momenta, mass)
    overlaps = np.sum(spinors.conj() * packet_k, axis=1)
    return float(np.sum(np.abs(overlaps) ** 2).real)


@dataclass(frozen=True)
class Response:
    route: str
    mass: float
    force: float
    acceleration: float
    measured_mass: float
    expected_mass: float
    norm: float
    band_probability: float
    boundary_probability: float
    initial_variance: float
    final_variance: float
    displacement: float
    final_packet: np.ndarray
    positions: np.ndarray


def force_response(
    route: str,
    mass: float,
    *,
    force: float = 2e-4,
    length: int = 4096,
    momentum_width: float = 0.025,
    duration: float = 40,
    time_step: float = 0.1,
    qca_ordering: str = "symmetric",
) -> Response:
    positions, momenta, packet = prepare_packet(route, length, mass, momentum_width)
    initial_centre = mean_position(packet, positions)
    initial_variance = position_variance(packet, positions)
    times = [0.0]
    centres = [initial_centre]

    if route == "qca":
        steps = int(duration)
        for step in range(steps):
            packet = qca_step_with_force(packet, positions, mass, force, qca_ordering)
            times.append(float(step + 1))
            centres.append(mean_position(packet, positions))
        expected_mass = mass / np.sqrt(1 - mass * mass)
    elif route == "hamiltonian":
        steps = round(duration / time_step)
        sample_stride = max(1, round(1 / time_step))
        for step in range(steps):
            packet = hamiltonian_step_with_force(
                packet, momenta, positions, mass, force, time_step
            )
            if (step + 1) % sample_stride == 0:
                times.append((step + 1) * time_step)
                centres.append(mean_position(packet, positions))
        expected_mass = mass
    else:
        raise ValueError(route)

    coefficient = np.polyfit(
        np.asarray(times), np.asarray(centres) - initial_centre, 2
    )
    acceleration = float(2 * coefficient[0])
    measured_mass = float(force / acceleration) if force else float("inf")
    return Response(
        route=route,
        mass=mass,
        force=force,
        acceleration=acceleration,
        measured_mass=measured_mass,
        expected_mass=float(expected_mass),
        norm=float(np.linalg.norm(packet)),
        band_probability=positive_band_probability(route, packet, momenta, mass),
        boundary_probability=boundary_probability(packet, positions),
        initial_variance=initial_variance,
        final_variance=position_variance(packet, positions),
        displacement=float(centres[-1] - initial_centre),
        final_packet=packet,
        positions=positions,
    )


def locality_and_domain_controls() -> None:
    rng = np.random.default_rng(202)
    length = 64
    mass = 0.4
    momenta = wrapped_momenta(length)
    packet = rng.normal(size=(length, 2)) + 1j * rng.normal(size=(length, 2))
    packet /= np.linalg.norm(packet)

    sample_momenta = np.array([-0.31, 0.0, 0.27])
    h_spinors = positive_band_spinor("hamiltonian", sample_momenta, mass)
    h_residuals = []
    qca_residuals = []
    for index, momentum in enumerate(sample_momenta):
        hamiltonian = np.sin(momentum) * SX + mass * SZ
        energy = np.sqrt(np.sin(momentum) ** 2 + mass * mass)
        h_residuals.append(
            np.linalg.norm(hamiltonian @ h_spinors[index] - energy * h_spinors[index])
        )
        qca = qca_bloch(momentum, mass)
        q_spinor = positive_band_spinor("qca", sample_momenta, mass)[index]
        phase = np.arccos(np.sqrt(1 - mass * mass) * np.cos(momentum))
        qca_residuals.append(
            np.linalg.norm(qca @ q_spinor - np.exp(-1j * phase) * q_spinor)
        )
    check(
        "prepared Hamiltonian spinors are positive-energy eigenstates",
        max(h_residuals) < 2e-12,
        h_residuals,
    )
    check(
        "prepared QCA spinors are the positive e^{-i omega} branch",
        max(qca_residuals) < 2e-12,
        qca_residuals,
    )

    local_qca = qca_local_step(packet, mass)
    packet_k = np.fft.fft(packet, axis=0, norm="ortho")
    bloch_qca_k = np.stack(
        [qca_bloch(momentum, mass) @ packet_k[index]
         for index, momentum in enumerate(momenta)]
    )
    bloch_qca = np.fft.ifft(bloch_qca_k, axis=0, norm="ortho")
    check(
        "strict QCA Bloch and literal range-one updates agree",
        np.allclose(local_qca, bloch_qca, atol=2e-12),
        np.linalg.norm(local_qca - bloch_qca),
    )
    check("strict QCA local update is norm preserving", abs(np.linalg.norm(local_qca) - 1) < 2e-12)

    delta = np.zeros((length, 2), dtype=complex)
    delta[length // 2, 0] = 1
    support = set(np.where(position_density(qca_local_step(delta, mass)) > 1e-14)[0])
    check(
        "strict QCA one-step support remains onsite or one edge away",
        support <= {length // 2 - 1, length // 2, length // 2 + 1},
        support,
    )

    local_h = hamiltonian_local_action(packet, mass)
    bloch_h = np.fft.ifft(
        hamiltonian_bloch_action(packet_k, momenta, mass), axis=0, norm="ortho"
    )
    check(
        "Hamiltonian Bloch action equals its literal range-one generator stencil",
        np.allclose(local_h, bloch_h, atol=2e-12),
        np.linalg.norm(local_h - bloch_h),
    )
    h_support = set(np.where(position_density(hamiltonian_local_action(delta, mass)) > 1e-14)[0])
    check(
        "Hamiltonian generator support remains onsite or one edge away",
        h_support <= {length // 2 - 1, length // 2, length // 2 + 1},
        h_support,
    )


def response_tournament() -> dict[tuple[str, float], Response]:
    results: dict[tuple[str, float], Response] = {}
    for route in ("qca", "hamiltonian"):
        for mass in (0.25, 0.4, 0.65):
            response = force_response(route, mass)
            results[(route, mass)] = response
            relative_error = abs(response.measured_mass / response.expected_mass - 1)
            check(
                f"{route} m={mass} local-force F/a recovers dispersion mass",
                relative_error < 3e-3,
                {
                    "measured": response.measured_mass,
                    "expected": response.expected_mass,
                    "relative_error": relative_error,
                },
            )
            check(
                f"{route} m={mass} evolution remains normalized and positive",
                abs(response.norm - 1) < 2e-10
                and np.min(position_density(response.final_packet)) >= 0,
                response.norm,
            )
            check(
                f"{route} m={mass} stays in the prepared positive band",
                response.band_probability > 0.99999,
                response.band_probability,
            )
            check(
                f"{route} m={mass} remains far from the periodic boundary",
                response.boundary_probability < 1e-20,
                response.boundary_probability,
            )
            check(
                f"{route} m={mass} is a localized moving packet",
                response.displacement > 0.1
                and response.final_variance < 1.1 * response.initial_variance,
                {
                    "displacement": response.displacement,
                    "variance_ratio": response.final_variance / response.initial_variance,
                },
            )
    return results


def redundancy_and_representation_controls(results: dict[tuple[str, float], Response]) -> None:
    response = results[("hamiltonian", 0.4)]
    packet = response.final_packet
    record_zero = np.array([1, 0], dtype=complex)
    record_plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    one_record = packet[:, :, None] * record_zero[None, None, :]
    one_rotated_record = packet[:, :, None] * record_plus[None, None, :]
    two_records = (
        packet[:, :, None, None]
        * record_zero[None, None, :, None]
        * record_plus[None, None, None, :]
    )
    baseline = mean_position(packet, response.positions)
    check(
        "one decoupled spectator record leaves packet position and norm unchanged",
        abs(mean_position(one_record, response.positions) - baseline) < 2e-12
        and abs(np.linalg.norm(one_record) - np.linalg.norm(packet)) < 2e-12,
    )
    check(
        "a record-basis change leaves the packet observable unchanged",
        abs(mean_position(one_rotated_record, response.positions) - baseline) < 2e-12,
    )
    check(
        "adding a second decoupled spectator record does not add inertial mass",
        abs(mean_position(two_records, response.positions) - baseline) < 2e-12
        and np.allclose(position_density(two_records), position_density(packet), atol=2e-12),
    )

    hadamard = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    transformed = packet @ hadamard.T
    check(
        "constant internal basis change leaves spatial density invariant",
        np.allclose(position_density(transformed), position_density(packet), atol=2e-12),
    )


def weak_force_broad_packet_convergence() -> None:
    settings = ((0.06, 6e-4), (0.04, 4e-4), (0.025, 2e-4), (0.0175, 1e-4))
    for route in ("qca", "hamiltonian"):
        errors = []
        for momentum_width, force in settings:
            response = force_response(
                route,
                0.4,
                momentum_width=momentum_width,
                force=force,
            )
            errors.append(abs(response.measured_mass / response.expected_mass - 1))
        check(
            f"{route} F/a converges as the push weakens and packet broadens",
            all(errors[index + 1] < errors[index] for index in range(len(errors) - 1))
            and errors[-1] < 1e-3,
            errors,
        )


def schedule_ablation_and_phase_controls() -> None:
    mass = 0.4
    predicted_qca_acceleration = 2e-4 * np.sqrt(1 - mass * mass) / mass
    order_responses = {
        ordering: force_response("qca", mass, qca_ordering=ordering).acceleration
        for ordering in ("pre", "post", "symmetric")
    }
    check(
        "QCA pre/post/symmetric local schedules share the low-force inertial limit",
        all(abs(value / predicted_qca_acceleration - 1) < 3e-3 for value in order_responses.values()),
        order_responses,
    )

    coarse = force_response("hamiltonian", mass, time_step=0.2).acceleration
    fine = force_response("hamiltonian", mass, time_step=0.1).acceleration
    check(
        "Hamiltonian Strang force response is stable under time-step refinement",
        abs(coarse / fine - 1) < 1e-5,
        {"dt=0.2": coarse, "dt=0.1": fine},
    )

    for route in ("qca", "hamiltonian"):
        zero = force_response(route, mass, force=0).acceleration
        check(
            f"{route} force deletion removes acceleration",
            abs(zero) < 1e-12,
            zero,
        )

    angle = np.arcsin(mass)
    distance_to_clifford_quarters = min(abs(angle - j * np.pi / 4) for j in range(-4, 5))
    check(
        "tested QCA mixing phase is not a Clifford quarter-turn",
        distance_to_clifford_quarters > 1e-3,
        angle / np.pi,
    )
    force_phase = 2e-4 * 137
    check(
        "onsite force uses a generic complex phase rather than a real/rebit update",
        abs(np.sin(force_phase)) > 1e-6 and abs(np.cos(force_phase)) > 1e-6,
        force_phase,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    locality_and_domain_controls()
    results = response_tournament()
    redundancy_and_representation_controls(results)
    weak_force_broad_packet_convergence()
    schedule_ablation_and_phase_controls()
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "LOCAL_FORCE_INERTIAL_BRIDGE" if FAIL == 0 else "CYCLE202_OPEN")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
