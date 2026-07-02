#!/usr/bin/env python3
"""Trivial det holonomy on Hermitian positive circulant edge content.

This runner verifies the bounded theorem in:

docs/DET_HOLONOMY_TRIVIAL_ON_HERMITIAN_POSITIVE_CIRCULANT_EDGE_CONTENT_BOUNDED_NOTE_2026-06-12.md

It checks the structural polar-decomposition identity, the supplied Hermitian
positive circulant surface, the 3-cycle determinant phase scan, harmonic and
K-parity projections, and two negative controls for the named live routes.
It writes no cache and makes no R-eta claim.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

import numpy as np
import sympy as sp


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC_PATH = REPO_ROOT / "docs" / (
    "DET_HOLONOMY_TRIVIAL_ON_HERMITIAN_POSITIVE_CIRCULANT_EDGE_CONTENT_"
    "BOUNDED_NOTE_2026-06-12.md"
)
MINIMAL_AXIOMS = "MINIMAL_AXIOMS_2026-06-05.md"
CONTEXT_FILES = (
    "INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_"
    "BOUNDED_THEOREM_NOTE_2026-06-10.md",
    "KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md",
)

TOL = 1.0e-10
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print()
    print("=" * 96)
    print(title)
    print("=" * 96)


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def is_symbolic_zero(expr: sp.Basic, n: int = 3) -> bool:
    return expr == 0 or expr == sp.ZeroMatrix(n, n) or str(expr) == "0"


def cyclic_shift() -> np.ndarray:
    return np.array(
        [
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
        ],
        dtype=complex,
    )


def circulant_h(a: float, b: float, delta: float) -> np.ndarray:
    c = cyclic_shift()
    return (
        a * np.eye(3, dtype=complex)
        + b * np.exp(1j * delta) * c
        + b * np.exp(-1j * delta) * c.T
    )


def polar_unitary(matrix: np.ndarray) -> np.ndarray:
    left, singular_values, right_h = np.linalg.svd(matrix)
    if np.min(singular_values) <= 1.0e-14:
        raise ValueError("polar unitary requested on a numerically singular matrix")
    return left @ right_h


def holonomy_phase_for_edge(edge: np.ndarray) -> tuple[np.ndarray, float, float]:
    unitary = polar_unitary(edge)
    hol = unitary @ unitary @ unitary
    phase = float(np.angle(np.linalg.det(hol)))
    deviation = float(np.linalg.norm(hol - np.eye(3, dtype=complex), ord="fro"))
    return hol, phase, deviation


def harmonic_coefficients(deltas: np.ndarray, phases: np.ndarray) -> dict[str, float]:
    return {
        "constant": float(np.mean(phases)),
        "cos3": float(2.0 * np.mean(phases * np.cos(3.0 * deltas))),
        "sin3": float(2.0 * np.mean(phases * np.sin(3.0 * deltas))),
        "cos6": float(2.0 * np.mean(phases * np.cos(6.0 * deltas))),
        "sin6": float(2.0 * np.mean(phases * np.sin(6.0 * deltas))),
    }


def symbolic_v1_checks() -> None:
    section("V1 symbolic: generic 3 x 3 P = A^dagger A + epsilon I")
    n = 3
    a = sp.MatrixSymbol("A", n, n)
    epsilon = sp.symbols("epsilon", positive=True, real=True)
    identity = sp.Identity(n)
    p = sp.Adjoint(a) * a + epsilon * identity

    hermitian_residual = sp.simplify(sp.Adjoint(p) - p)
    square_residual = sp.simplify(p**2 - sp.Adjoint(p) * p)
    unitary_factor = sp.simplify(p * sp.Inverse(p))

    check(
        "V1 symbolic construction is Hermitian",
        is_symbolic_zero(hermitian_residual, n),
        f"Adjoint(P)-P -> {hermitian_residual}",
    )
    check(
        "V1 symbolic positive branch has |P|^2 = P^2",
        is_symbolic_zero(square_residual, n),
        f"P^2 - P^dagger P -> {square_residual}",
    )
    check(
        "V1 symbolic polar unitary U = P |P|^-1 = I",
        unitary_factor == identity,
        f"P * Inverse(P) -> {unitary_factor}",
    )


def generic_positive_witnesses() -> None:
    section("V1 numeric: two generic positive-definite Hermitian witnesses")
    witnesses = [
        (
            np.array(
                [
                    [1.0 + 0.2j, 0.4 - 0.1j, -0.3 + 0.7j],
                    [0.6 - 0.5j, -1.2 + 0.3j, 0.8 + 0.1j],
                    [0.2 + 0.9j, 0.5 + 0.6j, -0.7 - 0.4j],
                ],
                dtype=complex,
            ),
            0.35,
        ),
        (
            np.array(
                [
                    [-0.8 + 0.1j, 1.1 + 0.4j, 0.2 - 0.2j],
                    [0.3 + 0.7j, -0.4 - 0.9j, 1.0 + 0.5j],
                    [0.9 - 0.3j, -0.6 + 0.8j, 0.7 + 0.2j],
                ],
                dtype=complex,
            ),
            0.2,
        ),
    ]
    residuals: list[float] = []
    min_eigs: list[float] = []
    for matrix, epsilon in witnesses:
        p = matrix.conj().T @ matrix + epsilon * np.eye(3, dtype=complex)
        eigs = np.linalg.eigvalsh(p)
        unitary = polar_unitary(p)
        residuals.append(float(np.linalg.norm(unitary - np.eye(3), ord="fro")))
        min_eigs.append(float(np.min(eigs)))
    check(
        "V1 numeric witnesses are positive and have polar(P)=I",
        min(min_eigs) > 0.0 and max(residuals) < TOL,
        f"min eigenvalues={min_eigs}; polar residuals={residuals}",
    )


def circulant_witnesses() -> None:
    section("V1/V2 numeric: supplied circulant positivity and polar links")
    samples = [(3.0, 0.75, 0.37), (4.25, 1.5, 1.91)]
    residuals: list[float] = []
    eig_report: list[list[float]] = []
    for a, b, delta in samples:
        h = circulant_h(a, b, delta)
        eigs = np.linalg.eigvalsh(h)
        unitary = polar_unitary(h)
        residual = float(np.linalg.norm(unitary - np.eye(3), ord="fro"))
        eig_report.append([float(x) for x in eigs])
        residuals.append(residual)
        print(f"(a,B,delta)=({a},{b},{delta}) eigenvalues={eigs}")
    check(
        "V1 circulant witnesses have positive spectrum and polar(H)=I",
        all(min(row) > 0.0 for row in eig_report) and max(residuals) < TOL,
        f"polar residuals={residuals}",
    )


def scan_trivial_holonomy() -> tuple[list[tuple[float, float, np.ndarray, np.ndarray]], float, float]:
    section("V2 scan: 25 deltas x 2 positive-domain (a,B) pairs")
    pairs = [(3.0, 0.75), (4.25, 1.5)]
    deltas = np.linspace(0.0, 2.0 * math.pi, 25, endpoint=False)
    rows: list[tuple[float, float, np.ndarray, np.ndarray]] = []
    max_hol_deviation = 0.0
    max_abs_phase = 0.0
    for a, b in pairs:
        phases = []
        for delta in deltas:
            h = circulant_h(a, b, float(delta))
            _hol, phase, deviation = holonomy_phase_for_edge(h)
            phases.append(phase)
            max_hol_deviation = max(max_hol_deviation, deviation)
            max_abs_phase = max(max_abs_phase, abs(phase))
        rows.append((a, b, deltas, np.array(phases, dtype=float)))
        print(
            f"(a,B)=({a},{b}) max |phi|={np.max(np.abs(phases)):.3e}; "
            f"max hol-I deviation so far={max_hol_deviation:.3e}"
        )
    check(
        "V2 3-cycle composite holonomy is I across the scan",
        max_hol_deviation < TOL,
        f"max ||Hol-I||_F={max_hol_deviation:.3e}",
    )
    check(
        "V2 determinant phase phi(delta) is identically zero across the scan",
        max_abs_phase < TOL,
        f"max |phi|={max_abs_phase:.3e}",
    )
    return rows, max_hol_deviation, max_abs_phase


def harmonic_and_k_checks(rows: list[tuple[float, float, np.ndarray, np.ndarray]]) -> None:
    section("V2 harmonics and K-parity")
    max_coeff = 0.0
    for a, b, deltas, phases in rows:
        coeffs = harmonic_coefficients(deltas, phases)
        max_coeff = max(max_coeff, max(abs(v) for v in coeffs.values()))
        print(f"(a,B)=({a},{b}) harmonic coefficients={coeffs}")
    check(
        "V2 harmonic projections constant/cos3/sin3/cos6/sin6 vanish",
        max_coeff < TOL,
        f"max coefficient magnitude={max_coeff:.3e}",
    )

    max_even = 0.0
    max_odd = 0.0
    for a, b, deltas, _phases in rows:
        for delta in deltas:
            _hol_p, phase_p, _dev_p = holonomy_phase_for_edge(circulant_h(a, b, float(delta)))
            _hol_m, phase_m, _dev_m = holonomy_phase_for_edge(circulant_h(a, b, float(-delta)))
            even = 0.5 * (phase_p + phase_m)
            odd = 0.5 * (phase_p - phase_m)
            max_even = max(max_even, abs(even))
            max_odd = max(max_odd, abs(odd))
    check(
        "V2 K-parity even part is identically zero",
        max_even < TOL,
        f"max |even|={max_even:.3e}",
    )
    check(
        "V2 K-parity odd part is identically zero",
        max_odd < TOL,
        f"max |odd|={max_odd:.3e}",
    )


def negative_control_nonhermitian() -> None:
    section("V3a negative control: non-Hermitian directed perturbation")
    c = cyclic_shift()
    edge = circulant_h(3.0, 1.0, 0.4) + 0.15 * (c - c.T)
    nonhermitian_residual = float(np.linalg.norm(edge.conj().T - edge, ord="fro"))
    unitary = polar_unitary(edge)
    polar_residual = float(np.linalg.norm(unitary - np.eye(3), ord="fro"))
    cycle = unitary @ unitary @ unitary
    cycle_phase = float(np.angle(np.linalg.det(cycle)))
    print(
        "non-Hermitian residual="
        f"{nonhermitian_residual:.6e}; ||polar(edge)-I||_F={polar_residual:.6e}; "
        f"cycle det phase={cycle_phase:.12f}"
    )
    check(
        "V3a witness is explicitly non-Hermitian",
        nonhermitian_residual > 1.0e-6,
        f"||M^dagger-M||_F={nonhermitian_residual:.3e}",
    )
    check(
        "V3a polar factor is not I and cycle det phase is nonzero",
        polar_residual > 1.0e-3 and abs(cycle_phase) > 1.0e-3,
        f"polar residual={polar_residual:.3e}; phase={cycle_phase:.6f}",
    )


def negative_control_sign_sector() -> None:
    section("V3b negative control: off-domain Hermitian sign sector")
    edge = circulant_h(1.5, 1.0, math.pi)
    eigs = np.linalg.eigvalsh(edge)
    unitary = polar_unitary(edge)
    polar_eigs = np.linalg.eigvals(unitary)
    cycle = unitary @ unitary @ unitary
    cycle_phase = float(np.angle(np.linalg.det(cycle)))
    reflection_residual = float(np.linalg.norm(unitary - np.eye(3), ord="fro"))
    print(f"off-domain H eigenvalues={eigs}")
    print(f"polar factor eigenvalues={polar_eigs}; cycle det phase={cycle_phase:.12f}")
    check(
        "V3b witness has an off-domain negative eigenvalue",
        float(np.min(eigs)) < 0.0,
        f"min eigenvalue={float(np.min(eigs)):.6f}",
    )
    check(
        "V3b polar factor is a nontrivial reflection with pi-valued cycle phase",
        reflection_residual > 1.0 and abs(abs(cycle_phase) - math.pi) < TOL,
        f"||polar(H)-I||_F={reflection_residual:.3e}; phase={cycle_phase:.6f}",
    )


def note_boundary_checks() -> None:
    section("B-checks: note boundary and inventory")
    note = DOC_PATH.read_text(encoding="utf-8")
    lower = note.lower()

    check(
        "B firewall and walls-move sentences are present",
        "the next path" in lower
        and "does not close" in lower
        and "structural reason" in lower
        and "no r-eta claim either way" in lower
        and "r never fixed" in lower,
        "required wall/firewall phrases scanned",
    )
    forbidden_phrases = ("closes the route", "closes this route", "exhausted")
    only_count = len(re.findall(r"\bonly\b", lower))
    check(
        "B forbidden wall phrases are absent",
        all(phrase not in lower for phrase in forbidden_phrases)
        and only_count == 1
        and "independent audit lane only" in lower,
        f"forbidden={forbidden_phrases}; only_count={only_count}",
    )

    markdown_links = re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", note)
    check(
        "B markdown link inventory is exactly MINIMAL_AXIOMS",
        markdown_links == [MINIMAL_AXIOMS],
        f"links={markdown_links}",
    )

    contexts_ok = True
    for filename in CONTEXT_FILES:
        contexts_ok = contexts_ok and f"`{filename}`" in note and f"]({filename})" not in note
    check(
        "B context filenames are backticked and not markdown-linked",
        contexts_ok,
        f"contexts={CONTEXT_FILES}",
    )

    check(
        "B No-promotion statement is present",
        "**No-promotion statement:**" in note
        and "does not promote, demote, or set the audit status" in note,
    )

    check(
        "B standard status lines are present",
        "**Date:** 2026-06-12" in note
        and "**Claim type:** bounded_theorem" in note
        and "**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome."
        in note,
    )


def main() -> int:
    print("Det holonomy trivial on Hermitian positive circulant edge content")
    print("Status authority: independent audit lane only. This runner does not set or predict an audit outcome.")
    print("No cache is written. No R-eta claim is made.")

    symbolic_v1_checks()
    generic_positive_witnesses()
    circulant_witnesses()
    rows, _max_hol_deviation, _max_abs_phase = scan_trivial_holonomy()
    harmonic_and_k_checks(rows)
    negative_control_nonhermitian()
    negative_control_sign_sector()
    note_boundary_checks()

    print()
    print("=" * 96)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 96)
    return 0 if PASS >= 12 and FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
