#!/usr/bin/env python3
"""Finite-time bounded-generator reset semigroup no-go."""

from __future__ import annotations

from math import exp
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
ATOL = 1e-12


def emit(line: str = "") -> None:
    print(line)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    emit(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    emit()
    emit("-" * 78)
    emit(title)
    emit("-" * 78)


def vec(a: np.ndarray) -> np.ndarray:
    return a.reshape((-1, 1), order="F")


def unvec(v: np.ndarray, d: int) -> np.ndarray:
    return v.reshape((d, d), order="F")


def basis_op(d: int, i: int, j: int) -> np.ndarray:
    a = np.zeros((d, d), dtype=complex)
    a[i, j] = 1.0
    return a


def blank_density(d: int) -> np.ndarray:
    rho = np.zeros((d, d), dtype=complex)
    rho[0, 0] = 1.0
    return rho


def sample_density(d: int) -> np.ndarray:
    psi = np.arange(1, d + 1, dtype=float)
    psi = psi / np.linalg.norm(psi)
    return np.outer(psi, psi).astype(complex)


def superoperator_from_channel(d: int, channel) -> np.ndarray:
    s = np.zeros((d * d, d * d), dtype=complex)
    col = 0
    for j in range(d):
        for i in range(d):
            s[:, col : col + 1] = vec(channel(basis_op(d, i, j)))
            col += 1
    return s


def reset_channel(d: int, a: np.ndarray) -> np.ndarray:
    return blank_density(d) * np.trace(a)


def amplitude_damping_channel(p: float):
    a0 = np.array([[1.0, 0.0], [0.0, np.sqrt(1.0 - p)]], dtype=complex)
    a1 = np.array([[0.0, np.sqrt(p)], [0.0, 0.0]], dtype=complex)

    def channel(rho: np.ndarray) -> np.ndarray:
        return a0 @ rho @ a0.conj().T + a1 @ rho @ a1.conj().T

    return channel


def trace_preserving_on_basis(d: int, channel) -> bool:
    for i in range(d):
        for j in range(d):
            a = basis_op(d, i, j)
            if not np.isclose(np.trace(channel(a)), np.trace(a), atol=ATOL):
                return False
    return True


def main() -> int:
    emit("=" * 78)
    emit("RECORD FINITE-TIME RESET SEMIGROUP NO-GO")
    emit("no-go / singular reset endpoint runner")
    emit("=" * 78)

    section("1. Exact reset superoperator is singular")
    for d in (2, 4, 8):
        s = superoperator_from_channel(d, lambda a, d=d: reset_channel(d, a))
        rank = np.linalg.matrix_rank(s, tol=ATOL)
        sample_out = unvec(s @ vec(sample_density(d)), d)
        check(f"d={d}: reset superoperator has expected shape", s.shape == (d * d, d * d))
        check(f"d={d}: reset superoperator has rank one", rank == 1, str(rank))
        check(f"d={d}: reset superoperator is not invertible", rank < d * d)
        check(f"d={d}: reset channel is trace-preserving", trace_preserving_on_basis(d, lambda a, d=d: reset_channel(d, a)))
        check(f"d={d}: sample density maps to blank", np.allclose(sample_out, blank_density(d), atol=ATOL))

    section("2. Finite damping parameters stay invertible")
    excited = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex)
    for p in (0.0, 0.5, 1.0 - exp(-2.0)):
        s = superoperator_from_channel(2, amplitude_damping_channel(p))
        rank = np.linalg.matrix_rank(s, tol=ATOL)
        det = np.linalg.det(s)
        out = amplitude_damping_channel(p)(excited)
        check(f"p={p:.6f}: finite damping rank is full", rank == 4, str(rank))
        check(f"p={p:.6f}: finite damping determinant is nonzero", abs(det) > ATOL, f"{det.real:.6e}")
        check(f"p={p:.6f}: finite damping does not exactly reset |1>", not np.allclose(out, blank_density(2), atol=ATOL))

    s_endpoint = superoperator_from_channel(2, amplitude_damping_channel(1.0))
    endpoint_out = amplitude_damping_channel(1.0)(excited)
    check("p=1 endpoint reset has rank one", np.linalg.matrix_rank(s_endpoint, tol=ATOL) == 1)
    check("p=1 endpoint reset determinant is zero", abs(np.linalg.det(s_endpoint)) < ATOL)
    check("p=1 endpoint exactly resets |1>", np.allclose(endpoint_out, blank_density(2), atol=ATOL))

    section("3. Finite exponential invertibility marker")
    diag_generator = np.diag([-1.0, -2.0, -3.0, -4.0])
    t = 0.75
    exp_diag = np.diag(np.exp(t * np.diag(diag_generator)))
    check("sample finite exponential has nonzero determinant", abs(np.linalg.det(exp_diag)) > ATOL)
    check("sample finite exponential has explicit inverse", np.allclose(exp_diag @ np.diag(1.0 / np.diag(exp_diag)), np.eye(4), atol=ATOL))
    check("rank-one reset cannot equal invertible exponential", np.linalg.matrix_rank(s_endpoint, tol=ATOL) < 4)

    section("4. Source note sanity")
    doc = Path("docs/RECORD_FINITE_TIME_RESET_SEMIGROUP_NO_GO_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: no-go",
        "trace_class: negative_route_pruning",
        "finite-time bounded-generator semigroup",
        "Does not derive a Hamiltonian",
        "Does not block asymptotic damping",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("rate closure", "finite physical reset rate is " + "derived"),
        ("hamiltonian closure", "Hamiltonian is " + "derived"),
        ("cost closure", "thermodynamic cost is " + "derived"),
        ("boundary closure", "low-record boundary is " + "derived"),
        ("dial closure", "dial location is " + "selected"),
        ("audit verdict", "promoted to " + "retained"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
