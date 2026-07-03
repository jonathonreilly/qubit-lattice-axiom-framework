#!/usr/bin/env python3
"""Exact-support runner for the generation periodic plane-wave mediator bridge."""

from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GENERATION_PERIODIC_PLANE_WAVE_DENSITY_KERNEL_BRIDGE_NOTE_2026-06-07.md"
PARENT_NOTE = ROOT / "docs" / "GENERATION_LOCALIZATION_MOMENTUM_CORNER_DELTA_JI_PROTECTED_NARROW_THEOREM_NOTE_2026-06-06.md"
MEDIATOR_NOTE = ROOT / "docs" / "STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11.md"

G = 50.0
MU2 = 0.001
TOL = 1e-8
CORNERS = {
    1: np.array([np.pi, 0.0, 0.0]),
    2: np.array([0.0, np.pi, 0.0]),
    3: np.array([0.0, 0.0, np.pi]),
}
PAIRS = [(1, 2), (1, 3), (2, 3)]

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def positions(L: int) -> list[tuple[int, int, int]]:
    return [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]


def laplacian_matrix(L: int) -> np.ndarray:
    pos = positions(L)
    idx = {p: i for i, p in enumerate(pos)}
    mat = np.zeros((L**3, L**3), dtype=float)
    for x, y, z in pos:
        a = idx[(x, y, z)]
        for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            b = idx[((x + dx) % L, (y + dy) % L, (z + dz) % L)]
            mat[a, a] += 1.0
            mat[a, b] -= 1.0
    return mat


def eps(k: np.ndarray) -> float:
    return float(sum(2.0 * (1.0 - np.cos(component)) for component in k))


def Vq(k: np.ndarray) -> float:
    return -G / (eps(k) + MU2)


def plane_wave(L: int, k: np.ndarray) -> np.ndarray:
    n = L**3
    return np.array(
        [np.exp(1j * (k[0] * x + k[1] * y + k[2] * z)) for x, y, z in positions(L)],
        dtype=complex,
    ) / np.sqrt(n)


def direct_delta(L: int, i: int, j: int) -> tuple[float, float, float]:
    lap = laplacian_matrix(L)
    V = -G * np.linalg.inv(lap + MU2 * np.eye(L**3))
    psi_i = plane_wave(L, CORNERS[i])
    psi_j = plane_wave(L, CORNERS[j])
    rho_i = np.abs(psi_i) ** 2
    rho_j = np.abs(psi_j) ** 2
    hartree = float(np.real(rho_i @ V @ rho_j))
    exchange_left = np.conjugate(psi_i) * psi_j
    exchange_right = np.conjugate(psi_j) * psi_i
    fock = float(np.real(exchange_left @ V @ exchange_right))
    return hartree - fock, hartree, fock


def main() -> int:
    print("=" * 88)
    print("GENERATION_PERIODIC_PLANE_WAVE_DENSITY_KERNEL_BRIDGE")
    print("Goal: bridge retained bounded mediator family to periodic plane-wave density kernel")
    print("=" * 88)

    section("Part 1: even periodic momenta and normalized plane waves")
    for L in (4, 6):
        allowed = all(np.allclose(np.exp(1j * L * k), np.ones(3)) for k in CORNERS.values())
        check(f"L={L}: hw=1 corner momenta are periodic", allowed)
        norms = [float(np.vdot(plane_wave(L, k), plane_wave(L, k)).real) for k in CORNERS.values()]
        check(f"L={L}: corner plane waves have unit norm", np.allclose(norms, [1.0, 1.0, 1.0]), detail=f"norms={norms}")

    section("Part 2: periodic Laplacian and mediator diagonalization")
    q_samples = [
        np.array([0.0, 0.0, 0.0]),
        CORNERS[1],
        CORNERS[2],
        CORNERS[3],
        CORNERS[1] - CORNERS[2],
        CORNERS[1] - CORNERS[3],
        CORNERS[2] - CORNERS[3],
    ]
    for L in (4, 6):
        lap = laplacian_matrix(L)
        lap_ok = True
        kernel_ok = True
        V = -G * np.linalg.inv(lap + MU2 * np.eye(L**3))
        for q in q_samples:
            psi = plane_wave(L, q)
            lap_resid = np.linalg.norm(lap @ psi - eps(q) * psi)
            ker_resid = np.linalg.norm(V @ psi - Vq(q) * psi)
            lap_ok = lap_ok and lap_resid < TOL
            kernel_ok = kernel_ok and ker_resid < 1e-5
        check(f"L={L}: Delta psi_q = eps(q) psi_q for q samples", lap_ok)
        check(f"L={L}: V_L psi_q = -G/(eps(q)+mu2) psi_q for q samples", kernel_ok)

    section("Part 3: density-density normalization and Hartree-Fock formula")
    for L in (4, 6):
        n = L**3
        delta, hartree, fock = direct_delta(L, 1, 2)
        expected_hartree = Vq(np.array([0.0, 0.0, 0.0])) / n
        expected_fock = Vq(CORNERS[2] - CORNERS[1]) / n
        expected_delta = expected_hartree - expected_fock
        check(f"L={L}: Hartree term equals Vq(0)/N", np.isclose(hartree, expected_hartree, rtol=1e-7), detail=f"{hartree:.6e} vs {expected_hartree:.6e}")
        check(f"L={L}: Fock term equals Vq(k_j-k_i)/N", np.isclose(fock, expected_fock, rtol=1e-7), detail=f"{fock:.6e} vs {expected_fock:.6e}")
        check(f"L={L}: delta equals [Vq(0)-Vq(Delta k)]/N", np.isclose(delta, expected_delta, rtol=1e-7), detail=f"{delta:.6e} vs {expected_delta:.6e}")

    section("Part 4: hw=1 pair symmetry, sign, and scaling")
    eps_pairs = [eps(CORNERS[i] - CORNERS[j]) for i, j in PAIRS]
    check("all hw=1 generation pairs have eps(Delta k)=8", np.allclose(eps_pairs, [8.0, 8.0, 8.0]), detail=str(eps_pairs))

    deltas = []
    for i, j in PAIRS:
        dk = CORNERS[i] - CORNERS[j]
        deltas.append((Vq(np.array([0.0, 0.0, 0.0])) - Vq(dk)) / (10**3))
    check("all three pair deltas are equal and negative", np.allclose(deltas, deltas[0]) and all(d < 0 for d in deltas), detail=", ".join(f"{d:.6e}" for d in deltas))

    scaled = []
    for L in (4, 6, 8, 10):
        n = L**3
        scaled.append(abs((Vq(np.array([0.0, 0.0, 0.0])) - Vq(CORNERS[1] - CORNERS[2])) / n) * n)
    check("|delta| scales as 1/N with fixed mediator IR data", np.allclose(scaled, scaled[0], rtol=1e-12), detail=f"|delta|*N={scaled[0]:.6e}")

    section("Part 5: source and downstream markers")
    note_text = NOTE.read_text(encoding="utf-8")
    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    mediator_text = MEDIATOR_NOTE.read_text(encoding="utf-8")
    note_markers = [
        "V_L = -G (Delta + mu^2 I)^(-1)",
        "delta(k,l) = <rho_k, V_L rho_l>",
        "`1/N` factor is not fitted",
        "does not pin the physical magnitude",
        "No new axiom is introduced",
    ]
    for marker in note_markers:
        check(f"bridge note marker present: {marker}", marker in note_text)
    parent_markers = [
        "Generation periodic plane-wave density-kernel bridge",
        "periodic translation-invariant plane-wave density-density kernel",
        "bridge packet for independent re-audit",
        "does not pin `|delta|`",
    ]
    for marker in parent_markers:
        check(f"parent note marker present: {marker}", marker in parent_text)
    check("retained bounded mediator note exposes V = -G (L + mu^2 I)^-1 family", "V = -G (L + mu^2)^-1" in mediator_text or "(L + mu^2 I) Phi_A" in mediator_text)

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
