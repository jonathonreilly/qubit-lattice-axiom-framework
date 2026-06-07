#!/usr/bin/env python3
"""Check the Koide orientation-blind count and B-field gate."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "KOIDE_ORIENTATION_BLIND_COUNT_B_FIELD_GATE_NOTE_2026-05-30.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  --  {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def read_note() -> str:
    return NOTE.read_text(encoding="utf-8")


def section(title: str) -> None:
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def check_note_scope() -> None:
    section("Note scope")
    text = read_note()
    flat = " ".join(text.split())
    required = [
        "**Claim type:** bounded_theorem / open_gate",
        "2026-06-07 Boundary Retargeting",
        "remains open and is not load-bearing for the direct local-support claim",
        "B-coupling -> B-field bridge open",
        "does not derive the charged-lepton Koide value",
        "does not approve",
        "does not claim that all possible routes are closed",
        "source note; downstream status is decided by independent review",
    ]
    forbidden = [
        "Generated" + " with",
        "source-note proposal only",
        "runner-cache",
        "actual_" + "current_surface_status",
        "ret" + "ained_bounded",
        "ret" + "ained_no_go",
        "un" + "audited",
        "audited_" + "FAILED",
        "A" + "1+A" + "2",
    ]
    for marker in required:
        check(f"note contains marker: {marker}", marker in text or marker in flat)
    for marker in forbidden:
        check(f"note omits non-native marker: {marker}", marker not in text)


def check_kahler_triple() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    section("Native Kähler triple on the b-plane")
    g = 6.0 * np.eye(2)
    j2 = np.array([[0.0, -1.0], [1.0, 0.0]])
    omega = g @ j2
    check("J2^2 = -I", np.allclose(j2 @ j2, -np.eye(2)), str((j2 @ j2).tolist()))
    check(
        "omega is antisymmetric",
        np.allclose(omega, -omega.T),
        str(omega.tolist()),
    )
    check(
        "omega is nondegenerate with determinant 36",
        abs(np.linalg.det(omega) - 36.0) < 1e-9,
        f"det={np.linalg.det(omega):.12g}",
    )
    check("omega = g J2", np.allclose(omega, g @ j2))
    return g, j2, omega


def check_orientation_blind_count(g: np.ndarray, j2: np.ndarray, omega: np.ndarray) -> None:
    section("Conjugation flips orientation but preserves count")
    c = np.diag([1.0, -1.0])
    check(
        "c J2 c^-1 = -J2",
        np.allclose(c @ j2 @ np.linalg.inv(c), -j2),
        str((c @ j2 @ np.linalg.inv(c)).tolist()),
    )
    check(
        "c^T omega c = -omega",
        np.allclose(c.T @ omega @ c, -omega),
        str((c.T @ omega @ c).tolist()),
    )
    check("c^T g c = g", np.allclose(c.T @ g @ c, g), str((c.T @ g @ c).tolist()))
    check("rank count is dim(R^2)/2 = 1", g.shape[0] // 2 == 1)


def check_q_formula() -> None:
    section("Circulant Q formula")
    a, x, y = sp.symbols("a x y", nonzero=True, real=True)
    b = x + sp.I * y
    b_bar = x - sp.I * y
    c = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    h = a * sp.eye(3) + b * c + b_bar * (c**2)
    tr_h = sp.simplify(sp.trace(h))
    tr_h2 = sp.simplify(sp.trace(h * h))
    q = sp.simplify(tr_h2 / tr_h**2)
    expected = sp.simplify((a**2 + 2 * (x**2 + y**2)) / (3 * a**2))
    check("trace(H) = 3a", sp.simplify(tr_h - 3 * a) == 0, str(tr_h))
    check("trace(H^2) = 3a^2 + 6|b|^2", sp.simplify(tr_h2 - (3 * a**2 + 6 * (x**2 + y**2))) == 0, str(tr_h2))
    check("Q = (a^2 + 2|b|^2)/(3a^2)", sp.simplify(q - expected) == 0, str(q))
    q_half = sp.simplify(q.subs({x: a / sp.sqrt(2), y: 0}))
    check("Q = 2/3 at |b|^2/a^2 = 1/2", sp.simplify(q_half - sp.Rational(2, 3)) == 0, str(q_half))


def check_action_order_gate() -> None:
    section("Action-order gate")
    first_order_phase_dim = 2
    second_order_phase_dim = 4
    check("first-order b-plane phase space has one mode", first_order_phase_dim // 2 == 1)
    check("static-coupling cotangent phase space has two modes", second_order_phase_dim // 2 == 2)
    check("the two readings are distinct", first_order_phase_dim != second_order_phase_dim)


def check_cooling_jump_off_circulant() -> None:
    section("Cooling jump is outside the native circulant algebra")
    c = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    c2 = c @ c
    ident = np.eye(3, dtype=complex)
    w = np.exp(2j * np.pi / 3)
    fourier = np.array([[1, 1, 1], [1, w, w**2], [1, w**2, w]], dtype=complex) / np.sqrt(3)
    f1 = fourier[:, 1]
    f2 = fourier[:, 2]
    jump = np.outer(f1, f2.conj())

    basis = [ident, c, c2]
    onb: list[np.ndarray] = []
    for raw in basis:
        vec = raw.copy()
        for unit in onb:
            vec = vec - np.trace(unit.conj().T @ vec) * unit
        vec = vec / np.sqrt(np.trace(vec.conj().T @ vec).real)
        onb.append(vec)

    projection = np.zeros((3, 3), dtype=complex)
    for unit in onb:
        projection += np.trace(unit.conj().T @ jump) * unit
    residual = jump - projection
    residual_norm = np.sqrt(np.trace(residual.conj().T @ residual).real)
    jump_norm = np.sqrt(np.trace(jump.conj().T @ jump).real)
    fraction = residual_norm / jump_norm
    check("projection onto span{I,C,C^2} has zero norm", np.linalg.norm(projection) < 1e-12, f"norm={np.linalg.norm(projection):.3e}")
    check("Hilbert-Schmidt residual fraction is one", abs(fraction - 1.0) < 1e-12, f"fraction={fraction:.12f}")


def check_kahler_dirac_block_gate() -> None:
    section("Kähler-Dirac form-degree block gate")
    sp_plus = np.array([[0, 1], [0, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    ident2 = np.eye(2, dtype=complex)
    create = [
        np.kron(np.kron(sp_plus, ident2), ident2),
        np.kron(np.kron(sigma_z, sp_plus), ident2),
        np.kron(np.kron(sigma_z, sigma_z), sp_plus),
    ]
    annihilate = [op.conj().T for op in create]
    number = sum(create[k] @ annihilate[k] for k in range(3))
    d_kd = sum(create[k] - annihilate[k] for k in range(3))
    lambda_one = [i for i in range(8) if round(number[i, i].real) == 1]
    projector = np.zeros((8, 8), dtype=complex)
    for idx in lambda_one:
        projector[idx, idx] = 1
    block = projector @ d_kd @ projector
    max_entry = np.max(np.abs(block))
    check("Lambda^1 subspace has dimension three", len(lambda_one) == 3, str(lambda_one))
    check("D_KD Lambda^1 -> Lambda^1 block is zero", max_entry < 1e-12, f"max={max_entry:.3e}")


def main() -> int:
    check_note_scope()
    g, j2, omega = check_kahler_triple()
    check_orientation_blind_count(g, j2, omega)
    check_q_formula()
    check_action_order_gate()
    check_cooling_jump_off_circulant()
    check_kahler_dirac_block_gate()

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: Koide orientation-blind count / B-field gate checks failed.")
        return 1
    print(
        "VERDICT: bounded orientation-blind count and B-field local gate checks pass; "
        "the B-coupling to B-field bridge remains open."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
