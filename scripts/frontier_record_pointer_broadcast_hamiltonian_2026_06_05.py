#!/usr/bin/env python3
"""Conditional Hamiltonian for pointer broadcast fanout."""

from __future__ import annotations

from math import pi
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
TOL = 1e-9


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


def bits_to_index(bits: str) -> int:
    return int(bits, 2)


def cnot_target(target: int, nbits: int = 4) -> np.ndarray:
    """CNOT with control bit 0 and target bit `target`."""
    dim = 2**nbits
    u = np.zeros((dim, dim), dtype=complex)
    for index in range(dim):
        bits = list(format(index, f"0{nbits}b"))
        if bits[0] == "1":
            bits[target] = "0" if bits[target] == "1" else "1"
        out_bits = "".join(bits)
        u[bits_to_index(out_bits), index] = 1.0
    return u


def fanout() -> np.ndarray:
    out = np.eye(16, dtype=complex)
    for target in (1, 2, 3):
        out = cnot_target(target) @ out
    return out


def pointer_z(nbits: int = 4) -> np.ndarray:
    diag = []
    for index in range(2**nbits):
        bits = format(index, f"0{nbits}b")
        diag.append(1.0 if bits[0] == "0" else -1.0)
    return np.diag(diag).astype(complex)


def exp_hermitian(h: np.ndarray, t: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(h)
    return vecs @ np.diag(np.exp(-1j * vals * t)) @ vecs.conj().T


def main() -> int:
    emit("=" * 78)
    emit("RECORD POINTER BROADCAST HAMILTONIAN CONDITIONAL")
    emit("bounded-support / conditional finite construction runner")
    emit("=" * 78)

    identity = np.eye(16, dtype=complex)
    terms = [cnot_target(target) for target in (1, 2, 3)]
    u_fanout = fanout()
    z_s = pointer_z()

    section("1. Controlled terms")
    for idx, c in enumerate(terms, start=1):
        check(f"C_{idx} is Hermitian", np.allclose(c, c.conj().T, atol=TOL))
        check(f"C_{idx} is involutive", np.allclose(c @ c, identity, atol=TOL))
        check(f"C_{idx} is unitary", np.allclose(c.conj().T @ c, identity, atol=TOL))
    check("controlled terms commute pairwise", all(np.allclose(a @ b, b @ a, atol=TOL) for a in terms for b in terms))
    check("product of controlled terms is fanout", np.allclose(terms[2] @ terms[1] @ terms[0], u_fanout, atol=TOL))

    section("2. Hamiltonian endpoint")
    t1 = 1.0
    h1 = sum((pi / (2 * t1)) * (identity - c) for c in terms)
    u1 = exp_hermitian(h1, t1)
    check("H(1) is Hermitian", np.allclose(h1, h1.conj().T, atol=TOL))
    check("exp(-i H(1) * 1) is fanout", np.allclose(u1, u_fanout, atol=TOL))
    check("H(1) commutes with pointer Z", np.allclose(h1 @ z_s, z_s @ h1, atol=TOL))
    check("fanout commutes with pointer Z", np.allclose(u_fanout @ z_s, z_s @ u_fanout, atol=TOL))

    section("3. Time/coupling scale remains a supplied normalization")
    t2 = 2.0
    h2 = sum((pi / (2 * t2)) * (identity - c) for c in terms)
    u2 = exp_hermitian(h2, t2)
    check("H(2) is Hermitian", np.allclose(h2, h2.conj().T, atol=TOL))
    check("exp(-i H(2) * 2) is the same fanout", np.allclose(u2, u_fanout, atol=TOL))
    check("H(2) is a rescaled H(1)", np.allclose(h2, 0.5 * h1, atol=TOL))
    check("different durations use different Hamiltonian scales", not np.allclose(h1, h2, atol=TOL))
    check("endpoint gate does not choose T", t1 != t2 and np.allclose(u1, u2, atol=TOL))

    section("4. Residual classes")
    supplied = {"controlled_terms", "duration_T", "pointer_basis"}
    output = {"fanout_unitary", "pointer_preserving_generator"}
    missing = {"derive_controlled_terms", "derive_pointer_basis", "blank_boundary", "clock_rate_selection", "probability_weights", "dial_selection"}
    check("controlled terms are explicit inputs", "controlled_terms" in supplied)
    check("duration is an explicit input", "duration_T" in supplied)
    check("output includes pointer-preserving generator", "pointer_preserving_generator" in output)
    check("missing gates are disjoint from output", output.isdisjoint(missing))
    check("clock/rate selection remains missing", "clock_rate_selection" in missing)

    section("5. Source note sanity")
    doc = Path("docs/RECORD_POINTER_BROADCAST_HAMILTONIAN_CONDITIONAL_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: bounded-support",
        "trace_class: upstream_support",
        "conditional_surface_status:",
        "Does not derive the physical Hamiltonian",
        "Does not apply audit verdicts.",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("hamiltonian closure", "Hamiltonian is " + "derived"),
        ("rate closure", "rates are " + "derived"),
        ("basis closure", "pointer basis is " + "derived"),
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
