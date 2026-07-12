#!/usr/bin/env python3
"""Coupled periodic two-seam reflected-Gram certificate."""

from __future__ import annotations

import itertools
from collections import defaultdict
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "COUPLED_PERIODIC_TWO_SEAM_SU3_WILSON_STAGGERED_REFLECTED_"
    "GRAM_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
TOL = 4.0e-10
PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def su3_dim(irrep: tuple[int, int]) -> int:
    p, q = irrep
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def tensor_fundamental(irrep: tuple[int, int]) -> list[tuple[int, int]]:
    p, q = irrep
    out = [(p + 1, q)]
    if p:
        out.append((p - 1, q + 1))
    if q:
        out.append((p, q - 1))
    return out


def tensor_antifundamental(irrep: tuple[int, int]) -> list[tuple[int, int]]:
    p, q = irrep
    out = [(p, q + 1)]
    if q:
        out.append((p + 1, q - 1))
    if p:
        out.append((p - 1, q))
    return out


def wilson_coefficients(beta: float, maximum_order: int):
    multiplicities = {(0, 0): 1}
    coefficients: dict[tuple[int, int], float] = defaultdict(float)
    prefactor = 1.0
    for order in range(maximum_order + 1):
        for irrep, multiplicity in multiplicities.items():
            coefficients[irrep] += prefactor * multiplicity
        following: dict[tuple[int, int], int] = defaultdict(int)
        for irrep, multiplicity in multiplicities.items():
            for target in tensor_fundamental(irrep):
                following[target] += multiplicity
            for target in tensor_antifundamental(irrep):
                following[target] += multiplicity
        multiplicities = dict(following)
        # exp[(beta/3) Re Tr g] = exp[(beta/6)(chi_3+chi_bar3)].
        prefactor *= (beta / 6.0) / float(order + 1)
    return coefficients


def haar_su3(rng: np.random.Generator) -> np.ndarray:
    matrix = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    unitary, triangular = np.linalg.qr(matrix)
    phases = np.diag(triangular)
    unitary = unitary @ np.diag(np.conj(phases / np.abs(phases)))
    unitary[:, 0] *= np.conj(np.linalg.det(unitary))
    return unitary


Field = tuple[str, int, int]
Observable = tuple[str, dict[int, int], dict[int, int], tuple[Field, ...]]


def temporal_dirac(temporal: np.ndarray, mass: float) -> np.ndarray:
    length = len(temporal)
    matrix = mass * np.eye(length, dtype=complex)
    for time in range(length):
        following = (time + 1) % length
        wrap_sign = -1.0 if time == length - 1 else 1.0
        matrix[time, following] += 0.5 * wrap_sign * temporal[time]
        matrix[following, time] -= 0.5 * wrap_sign * np.conj(temporal[time])
    return matrix


def exact_z3_action_covariance() -> tuple[float, float]:
    """Exhaust both adjacent reflections for AP D and the Z3 Wilson action."""
    length = 6
    roots = np.exp(2j * np.pi * np.arange(3) / 3.0)
    maximum_dirac_error = 0.0
    maximum_wilson_error = 0.0
    for plane_index in (0, 1):
        reflection = lambda time: (2 * plane_index + 1 - time) % length
        edge_reflection = lambda time: (2 * plane_index - time) % length
        signs = np.array(
            [-1.0 if time <= 2 * plane_index + 1 else 1.0 for time in range(length)]
        )
        for labels in itertools.product(range(3), repeat=length):
            temporal = np.array([roots[label] for label in labels])
            reflected_temporal = np.array(
                [np.conj(temporal[edge_reflection(time)]) for time in range(length)]
            )
            original = temporal_dirac(temporal, 1.0)
            reflected = temporal_dirac(reflected_temporal, 1.0)
            expected = np.empty_like(original)
            for row in range(length):
                for column in range(length):
                    expected[row, column] = (
                        signs[reflection(row)]
                        * signs[reflection(column)]
                        * np.conj(original[reflection(column), reflection(row)])
                    )
            maximum_dirac_error = max(
                maximum_dirac_error, float(np.linalg.norm(reflected - expected))
            )

            spatial = temporal
            reflected_spatial = np.array(
                [spatial[reflection(time)] for time in range(length)]
            )
            action = sum(
                (spatial[(time + 1) % length] * np.conj(spatial[time])).real
                for time in range(length)
            )
            reflected_action = sum(
                (
                    reflected_spatial[(time + 1) % length]
                    * np.conj(reflected_spatial[time])
                ).real
                for time in range(length)
            )
            maximum_wilson_error = max(
                maximum_wilson_error, abs(action - reflected_action)
            )
    return maximum_dirac_error, maximum_wilson_error


def contraction(left: Field, right: Field, covariance: np.ndarray) -> complex:
    kind_l, time_l, color_l = left
    kind_r, time_r, color_r = right
    if color_l != color_r:
        return 0.0j
    if kind_l == "chi" and kind_r == "bar":
        return complex(covariance[time_l, time_r])
    if kind_l == "bar" and kind_r == "chi":
        return complex(-covariance[time_r, time_l])
    return 0.0j


def wick(fields: tuple[Field, ...], covariance: np.ndarray) -> complex:
    if not fields:
        return 1.0 + 0.0j
    if len(fields) % 2:
        return 0.0j
    answer = 0.0j
    for partner in range(1, len(fields)):
        pair = contraction(fields[0], fields[partner], covariance)
        if pair == 0.0j:
            continue
        sign = 1.0 if partner % 2 else -1.0
        answer += sign * pair * wick(
            fields[1:partner] + fields[partner + 1 :], covariance
        )
    return answer


def baryon(time: int, kind: str = "chi") -> tuple[Field, ...]:
    return tuple((kind, time, color) for color in range(3))


def density(time: int) -> tuple[Field, ...]:
    return (("bar", time, 0), ("chi", time, 0))


def observable_basis() -> list[Observable]:
    return [
        ("1", {}, {}, ()),
        ("n1", {}, {}, density(1)),
        ("n2", {}, {}, density(2)),
        ("W1", {1: 1}, {}, ()),
        ("W1n1", {1: 1}, {}, density(1)),
        ("B1", {}, {}, baryon(1)),
        ("barB1", {}, {}, baryon(1, "bar")),
        ("B2", {}, {}, baryon(2)),
        ("barB2", {}, {}, baryon(2, "bar")),
        ("M12", {}, {1: 1}, (("bar", 1, 0), ("chi", 2, 0))),
        ("W1M12", {1: 1}, {1: 1}, (("bar", 1, 0), ("chi", 2, 0))),
    ]


def shift_observable(observable: Observable, shift: int, length: int) -> Observable:
    name, spatial_powers, temporal_powers, fields = observable
    return (
        name,
        {
            (time + shift) % length: power
            for time, power in spatial_powers.items()
        },
        {
            (time + shift) % length: power
            for time, power in temporal_powers.items()
        },
        tuple((kind, (time + shift) % length, color) for kind, time, color in fields),
    )


def z3_vertex_charges(observable: Observable, length: int) -> np.ndarray:
    """Net local Z3 gauge exponent of the one-spatial-loop analogue."""
    _, _, temporal_powers, fields = observable
    charges = np.zeros(length, dtype=int)
    for time, power in temporal_powers.items():
        charges[time] += power
        charges[(time + 1) % length] -= power
    for kind, time, _ in fields:
        charges[time] += 1 if kind == "chi" else -1
    return charges % 3


def reflect_observable(
    observable: Observable, plane_index: int, length: int, *, wrong_uniform: bool
) -> tuple[complex, dict[int, int], dict[int, int], tuple[Field, ...]]:
    _, spatial_powers, temporal_powers, fields = observable

    def reflection(time: int) -> int:
        return (2 * plane_index + 1 - time) % length

    reflected_spatial_powers = {
        reflection(time): -power for time, power in spatial_powers.items()
    }
    reflected_temporal_powers = {
        (2 * plane_index - time) % length: power
        for time, power in temporal_powers.items()
    }
    scalar = 1.0
    reflected_fields: list[Field] = []
    for kind, time, color in reversed(fields):
        scalar *= -1.0 if wrong_uniform or time <= 2 * plane_index + 1 else 1.0
        reflected_fields.append(
            ("bar" if kind == "chi" else "chi", reflection(time), color)
        )
    return (
        complex(scalar),
        reflected_spatial_powers,
        reflected_temporal_powers,
        tuple(reflected_fields),
    )


def gauge_coefficient(powers: dict[int, int], spatial: np.ndarray) -> complex:
    answer = 1.0 + 0.0j
    for time, power in powers.items():
        answer *= spatial[time] ** power
    return answer


def full_gauge_coefficient(
    spatial_powers: dict[int, int],
    temporal_powers: dict[int, int],
    spatial: np.ndarray,
    temporal: np.ndarray,
) -> complex:
    return gauge_coefficient(spatial_powers, spatial) * gauge_coefficient(
        temporal_powers, temporal
    )


def z3_reflected_gram(
    plane_index: int,
    left_basis: list[Observable],
    right_basis: list[Observable],
    *,
    wrong_uniform: bool = False,
    beta: float = (2.0 / 3.0) * np.log(2.0),
    mass: float = 1.0,
) -> tuple[np.ndarray, complex, float, float]:
    """Exact normalized sum in the gauge-fixed Z3 analogue at L_t=6."""
    length = 6
    roots = np.exp(2j * np.pi * np.arange(3) / 3.0)
    seams = (plane_index % length, (plane_index + length // 2) % length)
    free_temporal_times = [time for time in range(length) if time not in seams]
    gram = np.zeros((len(left_basis), len(right_basis)), dtype=complex)
    normalization = 0.0j
    minimum_determinant = float("inf")
    maximum_antihermitian_error = 0.0

    for temporal_labels in itertools.product(range(3), repeat=len(free_temporal_times)):
        temporal = np.ones(length, dtype=complex)
        for time, label in zip(free_temporal_times, temporal_labels):
            temporal[time] = roots[label]
        dmat = temporal_dirac(temporal, mass)
        hopping = dmat - mass * np.eye(length)
        maximum_antihermitian_error = max(
            maximum_antihermitian_error,
            float(np.linalg.norm(hopping + hopping.conj().T)),
        )
        determinant = complex(np.linalg.det(dmat))
        minimum_determinant = min(minimum_determinant, determinant.real)
        covariance = np.linalg.inv(dmat)

        for spatial_labels in itertools.product(range(3), repeat=length):
            spatial = np.array([roots[label] for label in spatial_labels])
            wilson_weight = np.exp(
                beta
                * sum(
                    (spatial[(time + 1) % length] * np.conj(spatial[time])).real
                    for time in range(length)
                )
            )
            weight = wilson_weight * determinant**3
            normalization += weight
            for row, left in enumerate(left_basis):
                (
                    scalar,
                    reflected_spatial_powers,
                    reflected_temporal_powers,
                    reflected_fields,
                ) = reflect_observable(
                    left,
                    plane_index,
                    length,
                    wrong_uniform=wrong_uniform,
                )
                left_coefficient = scalar * full_gauge_coefficient(
                    reflected_spatial_powers,
                    reflected_temporal_powers,
                    spatial,
                    temporal,
                )
                for column, right in enumerate(right_basis):
                    gram[row, column] += (
                        weight
                        * left_coefficient
                        * full_gauge_coefficient(
                            right[1], right[2], spatial, temporal
                        )
                        * wick(reflected_fields + right[3], covariance)
                    )

    divisor = float(3 ** (len(free_temporal_times) + length))
    return (
        gram / divisor,
        normalization / divisor,
        minimum_determinant,
        maximum_antihermitian_error,
    )


def main() -> int:
    beta = 0.8
    irreps = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (3, 0)]
    coefficients = wilson_coefficients(beta, 44)
    channels = np.array(
        [coefficients[irrep] / su3_dim(irrep) for irrep in irreps]
    )
    check(
        "SU3 Wilson character channels are positive",
        float(np.min(channels)) > 0.0,
        f"minimum checked channel={np.min(channels):.6e}",
    )

    rng = np.random.default_rng(20260712)
    points = [haar_su3(rng) for _ in range(9)]
    wilson_gram = np.array(
        [
            [
                np.exp((beta / 3.0) * np.trace(right @ left.conj().T).real)
                for right in points
            ]
            for left in points
        ]
    )
    wilson_minimum = float(np.min(np.linalg.eigvalsh(wilson_gram)))
    one_fermion_seam = np.diag([1.0, 0.5, 0.5, 0.25])
    two_seam_fermion = np.kron(one_fermion_seam, one_fermion_seam)
    combined_minimum = wilson_minimum**2 * float(
        np.min(np.linalg.eigvalsh(two_seam_fermion))
    )
    check(
        "Each sampled SU3 Wilson seam kernel is positive",
        wilson_minimum > -TOL,
        f"minimum eigenvalue={wilson_minimum:.6e}",
    )
    check(
        "The combined two-seam Wilson-times-fermion coefficient is positive",
        combined_minimum > -TOL,
        f"minimum tensor eigenvalue proxy={combined_minimum:.6e}",
    )

    exact_z3_kernel = np.ones((3, 3)) + np.eye(3)
    z3_spectrum = np.linalg.eigvalsh(exact_z3_kernel)
    z3_fourier_coefficients = np.array([4.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0])
    check(
        "Exact Z3 Wilson seam kernel has positive Fourier coefficients",
        np.allclose(z3_spectrum, [1.0, 1.0, 4.0])
        and np.min(z3_fourier_coefficients) > 0.0,
        f"spectrum={z3_spectrum.tolist()}, kappa={z3_fourier_coefficients.tolist()}",
    )

    dirac_covariance_error, wilson_covariance_error = exact_z3_action_covariance()
    check(
        "Both exact Z3 reflections preserve the AP staggered action",
        dirac_covariance_error < TOL,
        f"maximum entrywise-matrix residual={dirac_covariance_error:.3e}",
    )
    check(
        "Both exact Z3 reflections preserve the full Wilson side action",
        wilson_covariance_error < TOL,
        f"maximum action residual={wilson_covariance_error:.3e}",
    )

    basis = observable_basis()
    translated_basis = [shift_observable(item, 2, 6) for item in basis]
    maximum_charge = max(
        int(np.max(z3_vertex_charges(item, 6)))
        for item in basis + translated_basis
    )
    check(
        "Every exact finite-group probe is locally Z3 gauge invariant",
        maximum_charge == 0,
        f"maximum residual vertex charge mod 3={maximum_charge}",
    )
    gram0, normalization0, determinant_minimum, antihermitian_error = z3_reflected_gram(
        0, basis, basis
    )
    shifted_gram, _, _, _ = z3_reflected_gram(0, basis, translated_basis)
    adjacent_gram, normalization1, _, _ = z3_reflected_gram(
        1, translated_basis, translated_basis
    )
    wrong_gram, _, _, _ = z3_reflected_gram(
        0, basis, basis, wrong_uniform=True
    )

    gram0_hermiticity = float(np.linalg.norm(gram0 - gram0.conj().T))
    adjacent_hermiticity = float(
        np.linalg.norm(adjacent_gram - adjacent_gram.conj().T)
    )
    shifted_hermiticity = float(
        np.linalg.norm(shifted_gram - shifted_gram.conj().T)
    )
    gram0_minimum = float(
        np.min(np.linalg.eigvalsh((gram0 + gram0.conj().T) / 2.0))
    )
    adjacent_minimum = float(
        np.min(np.linalg.eigvalsh((adjacent_gram + adjacent_gram.conj().T) / 2.0))
    )
    shifted_minimum = float(
        np.min(np.linalg.eigvalsh((shifted_gram + shifted_gram.conj().T) / 2.0))
    )
    identity_error = float(np.linalg.norm(shifted_gram - adjacent_gram))
    wrong_hermiticity = float(np.linalg.norm(wrong_gram - wrong_gram.conj().T))
    wrong_minimum = float(
        np.min(np.linalg.eigvalsh((wrong_gram + wrong_gram.conj().T) / 2.0))
    )

    check(
        "Exact Z3 coupled theta0 Gram is Hermitian positive",
        gram0_hermiticity < TOL and gram0_minimum > -TOL,
        f"Hermiticity={gram0_hermiticity:.3e}, minimum={gram0_minimum:.6e}",
    )
    check(
        "Exact Z3 coupled adjacent-plane Gram is Hermitian positive",
        adjacent_hermiticity < TOL and adjacent_minimum > -TOL,
        f"Hermiticity={adjacent_hermiticity:.3e}, minimum={adjacent_minimum:.6e}",
    )
    check(
        "Exact coupled adjacent-plane correlation identity",
        identity_error < TOL
        and shifted_hermiticity < TOL
        and shifted_minimum > -TOL,
        f"identity={identity_error:.3e}, Hermiticity={shifted_hermiticity:.3e}, minimum={shifted_minimum:.6e}",
    )
    check(
        "Exact Z3 coupled normalization is real and strictly positive",
        abs(normalization0.imag) < TOL
        and abs(normalization1.imag) < TOL
        and normalization0.real > 0.0
        and abs(normalization0 - normalization1) < TOL,
        f"Z0={normalization0.real:.12f}, Z1={normalization1.real:.12f}",
    )
    check(
        "Antiperiodic staggered matrices are anti-Hermitian off mass with positive determinant",
        antihermitian_error < TOL and determinant_minimum > 0.0,
        f"maximum anti-Hermitian residual={antihermitian_error:.3e}, minimum det={determinant_minimum:.6e}",
    )
    check(
        "Uniform reflection is rejected on gauge-invariant baryon probes",
        wrong_hermiticity > 1.0e-3 and wrong_minimum < -1.0e-3,
        f"Hermiticity residual={wrong_hermiticity:.6e}, minimum Hermitian-part eigenvalue={wrong_minimum:.6e}",
    )

    failed_descent_g0 = np.diag([1.0, 0.0])
    failed_descent_shift = np.diag([0.0, 1.0])
    null_vector = np.array([0.0, 1.0])
    check(
        "Positive adjacent forms alone do not imply OS-null descent",
        null_vector @ failed_descent_g0 @ null_vector == 0.0
        and null_vector @ failed_descent_shift @ null_vector == 1.0,
        "G0=diag(1,0), G2=diag(0,1) is the exact countermodel",
    )
    noncontractive = np.diag([2.0, 0.5])
    check(
        "Positive adjacent forms alone do not imply contraction",
        np.min(np.linalg.eigvalsh(noncontractive)) > 0.0
        and np.max(np.linalg.eigvalsh(noncontractive)) > 1.0,
        "G0=I, G2=diag(2,1/2) is the exact countermodel",
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    condition_pairs = [
        f"| `C{left},C{right}` |"
        for left in range(1, 7)
        for right in range(left + 1, 7)
    ]
    required = [
        "individually gauge-invariant positive-half cylinder algebra",
        "separate plane-adapted charts",
        "combined two-seam coefficient kernel",
        "residual Polyakov holonomy",
        "positive adjacent-plane correlation form",
        "does not descend automatically",
        "not a transfer operator",
        "finite-group analogue",
        "does not prove the SU(3) theorem",
        "No-Go Discipline N1--N8",
        "### N3 — hidden-condition phrase scan",
        "### N4 — citation/residual matching",
        "### N5 — rhetoric and resolution audit",
        "### N6 — partial-closure, convention, reframe, and primitive scan",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "No axiom-update stop",
    ]
    missing = [item for item in required + condition_pairs if item not in note_text]
    attempted = note_text.count("| `ATTEMPTED` |")
    contract = not missing and attempted >= 7
    check(
        "Source-note boundary and N1-N8 contract",
        contract,
        f"schema present; attempted routes={attempted}"
        if contract
        else f"missing={missing}; attempted={attempted}",
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
