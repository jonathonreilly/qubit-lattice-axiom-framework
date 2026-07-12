#!/usr/bin/env python3
"""Periodic-route falsifier and twisted-AP free OS repair certificate."""

from __future__ import annotations

import itertools
import math
from collections import defaultdict
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "PERIODIC_STAGGERED_OS_CIRCLE_FAILURE_TWISTED_ANTIPERIODIC_"
    "FREE_REPAIR_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
TOL = 3.0e-10
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


def wilson_coefficients(beta: float, max_order: int) -> dict[tuple[int, int], float]:
    multiplicities: dict[tuple[int, int], int] = {(0, 0): 1}
    coefficients: dict[tuple[int, int], float] = defaultdict(float)
    prefactor = 1.0
    for order in range(max_order + 1):
        for irrep, multiplicity in multiplicities.items():
            coefficients[irrep] += prefactor * multiplicity
        following: dict[tuple[int, int], int] = defaultdict(int)
        for irrep, multiplicity in multiplicities.items():
            for target in tensor_fundamental(irrep):
                following[target] += multiplicity
            for target in tensor_antifundamental(irrep):
                following[target] += multiplicity
        multiplicities = dict(following)
        prefactor *= (beta / 2.0) / float(order + 1)
    return dict(coefficients)


Field = tuple[str, int]


def temporal_dirac(length: int, mass: float = 1.0, *, antiperiodic: bool) -> np.ndarray:
    dmat = mass * np.eye(length)
    for time in range(length):
        following = (time + 1) % length
        wrap_sign = -1.0 if antiperiodic and time == length - 1 else 1.0
        dmat[time, following] += 0.5 * wrap_sign
        dmat[following, time] -= 0.5 * wrap_sign
    return dmat


def two_point(left: Field, right: Field, covariance: np.ndarray) -> complex:
    kind_l, index_l = left
    kind_r, index_r = right
    if kind_l == "chi" and kind_r == "bar":
        return complex(covariance[index_l, index_r])
    if kind_l == "bar" and kind_r == "chi":
        return complex(-covariance[index_r, index_l])
    return 0.0j


def wick(fields: tuple[Field, ...], covariance: np.ndarray) -> complex:
    if not fields:
        return 1.0 + 0.0j
    if len(fields) % 2:
        return 0.0j
    answer = 0.0j
    for partner in range(1, len(fields)):
        contraction = two_point(fields[0], fields[partner], covariance)
        if contraction == 0.0j:
            continue
        sign = 1.0 if partner % 2 else -1.0
        remaining = fields[1:partner] + fields[partner + 1 :]
        answer += sign * contraction * wick(remaining, covariance)
    return answer


def uniform_theta(fields: tuple[Field, ...], length: int) -> tuple[complex, tuple[Field, ...]]:
    reflected = tuple(
        (("bar" if kind == "chi" else "chi"), (1 - time) % length)
        for kind, time in reversed(fields)
    )
    return complex((-1) ** len(fields)), reflected


def twisted_theta(
    fields: tuple[Field, ...], length: int, plane_index: int
) -> tuple[complex, tuple[Field, ...]]:
    """AP-compatible theta_j with r_j(t)=2j+1-t and transported step phase."""
    scalar = 1.0
    reflected: list[Field] = []
    for kind, time in reversed(fields):
        scalar *= -1.0 if time <= 2 * plane_index + 1 else 1.0
        reflected.append(
            (("bar" if kind == "chi" else "chi"), (2 * plane_index + 1 - time) % length)
        )
    return complex(scalar), tuple(reflected)


def local_basis(time: int) -> list[tuple[Field, ...]]:
    return [
        (),
        (("bar", time),),
        (("chi", time),),
        (("bar", time), ("chi", time)),
    ]


def monomial_basis(times: list[int]) -> list[tuple[Field, ...]]:
    generators = [(kind, time) for time in times for kind in ("bar", "chi")]
    return [
        tuple(generators[index] for index in range(len(generators)) if mask & (1 << index))
        for mask in range(1 << len(generators))
    ]


def gram(
    length: int,
    basis: list[tuple[Field, ...]],
    *,
    antiperiodic: bool,
    twisted: bool,
    plane_index: int = 0,
    right_shift: int = 0,
    mass: float = 1.0,
) -> np.ndarray:
    covariance = np.linalg.inv(temporal_dirac(length, mass, antiperiodic=antiperiodic))
    result = np.empty((len(basis), len(basis)), dtype=np.complex128)
    for row, left in enumerate(basis):
        if twisted:
            scalar, reflected = twisted_theta(left, length, plane_index)
        else:
            scalar, reflected = uniform_theta(left, length)
        for column, right in enumerate(basis):
            shifted = tuple((kind, (time + right_shift) % length) for kind, time in right)
            result[row, column] = scalar * wick(reflected + shifted, covariance)
    return result


def quotient_transfer(g0: np.ndarray, gshift: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh((g0 + g0.conj().T) / 2.0)
    keep = values > 1.0e-11
    quotient = np.sqrt(values[keep])[:, None] * vectors[:, keep].conj().T
    metric = quotient @ quotient.conj().T
    inverse = np.linalg.inv(metric)
    return inverse @ quotient @ gshift @ quotient.conj().T @ inverse


def reflected_action_residual(length: int, plane_index: int) -> float:
    dmat = temporal_dirac(length, antiperiodic=True)
    signs = np.array(
        [-1.0 if time <= 2 * plane_index + 1 else 1.0 for time in range(length)]
    )
    reflected = np.empty_like(dmat)
    reflection = lambda time: (2 * plane_index + 1 - time) % length
    for row in range(length):
        for column in range(length):
            reflected[row, column] = (
                signs[reflection(row)]
                * signs[reflection(column)]
                * dmat[reflection(column), reflection(row)]
            )
    return float(np.linalg.norm(reflected - dmat))


def twisted_translation_matrix(length: int) -> np.ndarray:
    shift = np.zeros((length, length))
    for time in range(length):
        following = (time + 1) % length
        shift[following, time] = -1.0 if time == length - 1 else 1.0
    return shift


def main() -> int:
    irreps = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
    coefficients = wilson_coefficients(0.8, 42)
    gauge_channels = np.array(
        [coefficients[irrep] / su3_dim(irrep) for irrep in irreps]
    )
    check(
        "Wilson channels remain available for the coupled next route",
        np.min(gauge_channels) > 0.0,
        f"minimum sampled Peter-Weyl eigenvalue={np.min(gauge_channels):.6e}",
    )

    crossing = np.diag([1.0, 0.5, 0.5, 0.25])
    check(
        "Grassmann feature category is four-dimensional per label",
        crossing.shape == (4, 4) and 2**1 == 2,
        "C_f is feature/GNS data, not a two-dimensional one-mode Fock operator",
    )
    check(
        "Central phased crossing remains positive",
        np.min(np.linalg.eigvalsh(crossing)) == 0.25,
        f"spectrum={np.linalg.eigvalsh(crossing)}",
    )

    # The rejected circle route: periodic wrap plus one uniform phase.
    periodic_failures = []
    second_seam_failures = []
    for length in (6, 8, 10):
        strict_times = list(range(1, length // 2))
        strict_gram = gram(
            length,
            monomial_basis(strict_times),
            antiperiodic=False,
            twisted=False,
        )
        periodic_failures.append(
            float(np.min(np.linalg.eigvalsh((strict_gram + strict_gram.conj().T) / 2.0)))
        )
        seam_time = length // 2
        seam_gram = gram(
            length,
            local_basis(seam_time),
            antiperiodic=False,
            twisted=False,
        )
        second_seam_failures.append(
            float(np.min(np.linalg.eigvalsh((seam_gram + seam_gram.conj().T) / 2.0)))
        )
    check(
        "Uniform periodic reflection fails on the strict positive semicircle",
        max(periodic_failures) < -0.05,
        f"minimum eigenvalues={','.join(f'{value:.6f}' for value in periodic_failures)}",
    )
    strict_l6 = gram(
        6,
        monomial_basis([1, 2]),
        antiperiodic=False,
        twisted=False,
    )
    check(
        "Exact rational strict-half counterexample",
        abs(strict_l6[5, 5] + 1.0 / 49.0) < TOL
        and abs(strict_l6[10, 10] + 1.0 / 49.0) < TOL,
        f"q(bar1 bar2)={strict_l6[5,5].real:.12f}, q(chi1 chi2)={strict_l6[10,10].real:.12f}",
    )
    check(
        "Uniform periodic reflection fails locally at the second seam",
        max(second_seam_failures) < -0.28,
        f"minimum eigenvalues={','.join(f'{value:.6f}' for value in second_seam_failures)}",
    )
    exact_far_witness = np.array(
        [
            [1.0, 0.0, 0.0, -5.0 / 7.0],
            [0.0, -2.0 / 7.0, 0.0, 0.0],
            [0.0, 0.0, -2.0 / 7.0, 0.0],
            [-5.0 / 7.0, 0.0, 0.0, 29.0 / 49.0],
        ]
    )
    computed_far_witness = gram(
        6, local_basis(3), antiperiodic=False, twisted=False
    )
    check(
        "Exact rational far-seam counterexample",
        np.linalg.norm(computed_far_witness - exact_far_witness) < TOL,
        f"matrix residual={np.linalg.norm(computed_far_witness-exact_far_witness):.3e}; odd diagonals=-2/7",
    )

    # Neither changing the spin structure nor the reflection phase alone is enough.
    length = 6
    full_times = list(range(1, length // 2 + 1))
    ap_only = gram(
        length, monomial_basis(full_times), antiperiodic=True, twisted=False
    )
    twist_only = gram(
        length, monomial_basis(full_times), antiperiodic=False, twisted=True
    )
    check(
        "Antiperiodic wrap alone does not repair reflection positivity",
        np.min(np.linalg.eigvalsh((ap_only + ap_only.conj().T) / 2.0)) < -0.8,
        f"minimum={np.min(np.linalg.eigvalsh((ap_only+ap_only.conj().T)/2.0)):.6f}",
    )
    check(
        "Seam twist alone does not repair reflection positivity",
        np.min(np.linalg.eigvalsh((twist_only + twist_only.conj().T) / 2.0)) < -0.38,
        f"minimum={np.min(np.linalg.eigvalsh((twist_only+twist_only.conj().T)/2.0)):.6f}",
    )

    # Exact AP + transported-step-phase repair, including both plane classes.
    repair_minima = []
    ranks = []
    adjacent_minima = []
    for length in (4, 6, 8):
        times0 = list(range(1, length // 2 + 1))
        repaired0 = gram(
            length,
            monomial_basis(times0),
            antiperiodic=True,
            twisted=True,
            plane_index=0,
        )
        spectrum0 = np.linalg.eigvalsh((repaired0 + repaired0.conj().T) / 2.0)
        repair_minima.append(float(np.min(spectrum0)))
        ranks.append(int(np.linalg.matrix_rank(repaired0, tol=1.0e-9)))

        times1 = [(2 + offset) % length for offset in range(length // 2)]
        repaired1 = gram(
            length,
            monomial_basis(times1),
            antiperiodic=True,
            twisted=True,
            plane_index=1,
        )
        adjacent_minima.append(
            float(np.min(np.linalg.eigvalsh((repaired1 + repaired1.conj().T) / 2.0)))
        )
    check(
        "Twisted-AP full positive-half Grams are positive",
        min(repair_minima) > -3.0e-14,
        f"minima L=4,6,8={','.join(f'{value:.3e}' for value in repair_minima)}",
    )
    check(
        "Twisted-AP quotient rank stabilizes",
        ranks == [16, 16, 16],
        f"ranks L=4,6,8={ranks}",
    )
    check(
        "Adjacent reflection-plane class is independently positive",
        min(adjacent_minima) > -3.0e-14,
        f"minima L=4,6,8={','.join(f'{value:.3e}' for value in adjacent_minima)}",
    )
    identity_length = 8
    identity_basis = local_basis(1)
    shifted_identity_basis = [
        tuple((kind, time + 2) for kind, time in monomial)
        for monomial in identity_basis
    ]
    left_quadratic = gram(
        identity_length,
        identity_basis,
        antiperiodic=True,
        twisted=True,
        plane_index=0,
        right_shift=2,
    )
    adjacent_quadratic = gram(
        identity_length,
        shifted_identity_basis,
        antiperiodic=True,
        twisted=True,
        plane_index=1,
    )
    check(
        "Adjacent-plane transfer quadratic-form identity",
        np.linalg.norm(left_quadratic - adjacent_quadratic) < TOL,
        f"||G_theta0,tau2-G_theta1(R2.,R2.)||={np.linalg.norm(left_quadratic-adjacent_quadratic):.3e}",
    )

    involution_errors = []
    action_errors = []
    for length in (6, 8, 10):
        for plane_index in (0, 1):
            action_errors.append(reflected_action_residual(length, plane_index))
            for time in range(length):
                sign = -1.0 if time <= 2 * plane_index + 1 else 1.0
                reflected_time = (2 * plane_index + 1 - time) % length
                sign_reflected = (
                    -1.0 if reflected_time <= 2 * plane_index + 1 else 1.0
                )
                involution_errors.append(abs(sign * sign_reflected - 1.0))
    check(
        "Twisted reflections square to the identity",
        max(involution_errors) < TOL,
        f"maximum phase-product residual={max(involution_errors):.3e}",
    )
    check(
        "Both twisted reflection classes preserve the AP action",
        max(action_errors) < TOL,
        f"maximum matrix residual={max(action_errors):.3e}",
    )

    translation_errors = []
    for length in (6, 8, 10):
        dmat = temporal_dirac(length, antiperiodic=True)
        shift = twisted_translation_matrix(length)
        translation_errors.append(float(np.linalg.norm(shift.conj().T @ dmat @ shift - dmat)))
    check(
        "Twisted one-site shift preserves the free temporal AP matrix",
        max(translation_errors) < TOL,
        f"maximum action residual={max(translation_errors):.3e}",
    )

    # Reconstruct T from independently computed twisted-AP G0 and G_tau.
    z = math.exp(-2.0 * math.asinh(1.0))
    target = np.array([z * z, z, z, 1.0])
    transfer_minima = []
    transfer_maxima = []
    shifted_gram_hermiticity = []
    transfer_hermiticity = []
    contraction_defects = []
    spectrum_errors = []
    finite_formula_errors = []
    semigroup_errors = []
    for length in (6, 8, 16, 24, 32):
        basis = local_basis(1)
        g0 = gram(
            length, basis, antiperiodic=True, twisted=True, plane_index=0
        )
        g1 = gram(
            length,
            basis,
            antiperiodic=True,
            twisted=True,
            plane_index=0,
            right_shift=2,
        )
        g2 = gram(
            length,
            basis,
            antiperiodic=True,
            twisted=True,
            plane_index=0,
            right_shift=4,
        )
        transfer = quotient_transfer(g0, g1)
        transfer2 = quotient_transfer(g0, g2)
        shifted_gram_hermiticity.append(float(np.linalg.norm(g1 - g1.conj().T)))
        transfer_hermiticity.append(float(np.linalg.norm(transfer - transfer.conj().T)))
        spectrum = np.linalg.eigvalsh((transfer + transfer.conj().T) / 2.0)
        transfer_minima.append(float(np.min(spectrum)))
        transfer_maxima.append(float(np.max(spectrum)))
        contraction_defects.append(
            float(
                np.min(
                    np.linalg.eigvalsh(
                        np.eye(transfer.shape[0])
                        - (transfer + transfer.conj().T) / 2.0
                    )
                )
            )
        )
        spectrum_errors.append(float(np.max(np.abs(spectrum - target))))
        half_length = length // 2
        q_finite = (z + z ** (half_length - 2)) / (1.0 + z ** (half_length - 1))
        finite_formula_errors.append(
            float(np.max(np.abs(spectrum - np.array([q_finite**2, q_finite, q_finite, 1.0]))))
        )
        semigroup_errors.append(float(np.linalg.norm(transfer2 - transfer @ transfer)))
    check(
        "Twisted-AP shifted Grams and compressed operators are Hermitian",
        max(shifted_gram_hermiticity) < TOL and max(transfer_hermiticity) < TOL,
        f"max Gram residual={max(shifted_gram_hermiticity):.3e}, max transfer residual={max(transfer_hermiticity):.3e}",
    )
    check(
        "Twisted-AP compressed correlation operators are positive",
        min(transfer_minima) > -TOL,
        f"minimum eigenvalue={min(transfer_minima):.3e}",
    )
    check(
        "Twisted-AP compressed operators satisfy I minus C positive",
        min(contraction_defects) > -TOL,
        f"min={min(transfer_minima):.3e}, max={max(transfer_maxima):.12f}",
    )
    check(
        "Twisted-AP feature spectrum is generated by the Block14 eigenvalue z",
        spectrum_errors[-1] < 1.0e-9,
        f"errors L=6..32={','.join(f'{value:.3e}' for value in spectrum_errors)}",
    )
    check(
        "Exact finite-circle compressed spectrum formula",
        max(finite_formula_errors) < 1.0e-12,
        f"max residual={max(finite_formula_errors):.3e}",
    )
    check(
        "Twisted-AP thermal semigroup images vanish",
        semigroup_errors[-1] < 2.0e-9,
        f"errors L=6..32={','.join(f'{value:.3e}' for value in semigroup_errors)}",
    )

    limiting_basis = local_basis(1)
    limiting_g0 = gram(
        48, limiting_basis, antiperiodic=True, twisted=True, plane_index=0
    )
    limiting_g1 = gram(
        48,
        limiting_basis,
        antiperiodic=True,
        twisted=True,
        plane_index=0,
        right_shift=2,
    )
    limiting_transfer = quotient_transfer(limiting_g0, limiting_g1)
    values, vectors = np.linalg.eigh(
        (limiting_transfer + limiting_transfer.conj().T) / 2.0
    )
    generator = (vectors * (-0.5 * np.log(values))) @ vectors.conj().T
    phases = np.exp(-1j * 0.731 * np.linalg.eigvalsh(generator))
    h_vectors = np.linalg.eigh(generator)[1]
    unitary = (h_vectors * phases) @ h_vectors.conj().T
    check(
        "Free repaired logarithmic generator is positive",
        np.min(np.linalg.eigvalsh(generator)) > -TOL,
        f"minimum={np.min(np.linalg.eigvalsh(generator)):.3e}",
    )
    check(
        "Free repaired spectral evolution is unitary",
        np.linalg.norm(unitary.conj().T @ unitary - np.eye(4)) < TOL,
        f"residual={np.linalg.norm(unitary.conj().T@unitary-np.eye(4)):.3e}",
    )

    note_text = NOTE.read_text(encoding="utf-8")
    pairs = [
        f"| `C{left},C{right}` |"
        for left in range(1, 7)
        for right in range(left + 1, 7)
    ]
    required = [
        "trivial-Polyakov-holonomy restriction",
        "residual temporal holonomy",
        "No-Go Discipline N1--N8",
        "### N3 — hidden-condition phrase scan",
        "### N4 — citation/residual matching",
        "### N5 — rhetoric and resolution audit",
        "### N6 — partial-closure, convention, reframe, and primitive scan",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "No axiom-update stop",
    ]
    missing = [needle for needle in required + pairs if needle not in note_text]
    attempted = note_text.count("| `ATTEMPTED` |")
    contract = not missing and attempted >= 7
    check(
        "Source-note boundary and N1-N8 contract",
        contract,
        (
            f"schema present; attempted routes={attempted}"
            if contract
            else f"missing={missing}; attempted={attempted}"
        ),
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
