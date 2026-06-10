#!/usr/bin/env python3
"""Exact-support verifier for the generation-corner Hartree-Fock Vq bridge.

The audited conditional target
`generation_localization_momentum_corner_delta_ji_protected_narrow_theorem_note_2026-06-06`
was blocked on a missing one-hop theorem:

    derive the periodic translation-invariant Hartree-Fock plane-wave mutual
    energy readout Vq(q)=-G/(eps(q)+mu^2), including boundary/normalization,
    from the retained staggered two-body mediator.

This runner proves and checks the bridge on finite periodic L^3 lattices.  It
does not write audit results and does not claim audit-retained status for the
new bridge.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
BRIDGE_NOTE = ROOT / "docs" / "GENERATION_CORNER_HF_VQ_SCREENED_POISSON_BRIDGE_NARROW_THEOREM_NOTE_2026-06-07.md"
TARGET_NOTE = ROOT / "docs" / "GENERATION_LOCALIZATION_MOMENTUM_CORNER_DELTA_JI_PROTECTED_NARROW_THEOREM_NOTE_2026-06-06.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
TARGET_RUNNER = ROOT / "scripts" / "generation_localization_corner_protected_delta_runner.py"
BRIDGE_CACHE = ROOT / "logs" / "runner-cache" / "generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.txt"

G = 50.0
MU2 = 0.001
CORNERS = {
    1: (np.pi, 0.0, 0.0),
    2: (0.0, np.pi, 0.0),
    3: (0.0, 0.0, np.pi),
}
PAIRS = [(1, 2), (1, 3), (2, 3)]

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def positions(L: int) -> list[tuple[int, int, int]]:
    return [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]


def periodic_laplacian(L: int) -> np.ndarray:
    pos = positions(L)
    idx = {p: a for a, p in enumerate(pos)}
    n = L**3
    lap = np.zeros((n, n), dtype=float)
    for x, y, z in pos:
        a = idx[(x, y, z)]
        for dx, dy, dz in (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ):
            b = idx[((x + dx) % L, (y + dy) % L, (z + dz) % L)]
            lap[a, a] += 1.0
            lap[a, b] -= 1.0
    return lap


def k_grid(L: int) -> list[tuple[float, float, float]]:
    return [
        (2 * np.pi * a / L, 2 * np.pi * b / L, 2 * np.pi * c / L)
        for a in range(L)
        for b in range(L)
        for c in range(L)
    ]


def eps(k: tuple[float, float, float]) -> float:
    return float(sum(2.0 * (1.0 - np.cos(ki)) for ki in k))


def vq(k: tuple[float, float, float]) -> float:
    return -G / (eps(k) + MU2)


def fourier_vector(L: int, k: tuple[float, float, float]) -> np.ndarray:
    pos = positions(L)
    n = L**3
    return np.array(
        [np.exp(1j * (k[0] * x + k[1] * y + k[2] * z)) for x, y, z in pos],
        dtype=complex,
    ) / np.sqrt(n)


def fourier_matrix(L: int) -> np.ndarray:
    return np.column_stack([fourier_vector(L, k) for k in k_grid(L)])


def dense_kernel(L: int) -> np.ndarray:
    lap = periodic_laplacian(L)
    n = L**3
    return -G * np.linalg.inv(lap + MU2 * np.eye(n))


def fourier_kernel(L: int) -> np.ndarray:
    F = fourier_matrix(L)
    multipliers = np.diag([vq(k) for k in k_grid(L)])
    return F @ multipliers @ F.conj().T


def hf_dense_delta(L: int, i: int, j: int) -> float:
    K = dense_kernel(L)
    phi_i = fourier_vector(L, CORNERS[i])
    phi_j = fourier_vector(L, CORNERS[j])
    dens_i = np.abs(phi_i) ** 2
    dens_j = np.abs(phi_j) ** 2
    hartree = float(np.real(dens_i @ K @ dens_j))
    exchange_a = phi_i.conj() * phi_j
    exchange_b = phi_j.conj() * phi_i
    exchange = float(np.real(exchange_a @ K @ exchange_b))
    return hartree - exchange


def hf_formula_delta(L: int, i: int, j: int) -> float:
    n = L**3
    delta_k = tuple(float(a - b) for a, b in zip(CORNERS[i], CORNERS[j]))
    return (vq((0.0, 0.0, 0.0)) - vq(delta_k)) / n


def ledger_rows() -> dict[str, dict[str, object]]:
    data = json.loads(LEDGER.read_text())
    rows = data["rows"]
    if not isinstance(rows, dict):
        raise TypeError("audit ledger rows must be a dictionary")
    return rows


def effective_status(rows: dict[str, dict[str, object]], claim_id: str) -> str:
    row = rows.get(claim_id, {})
    return str(row.get("effective_status") or "")


def source_checks() -> None:
    print("\n-- Source and dependency surface checks --")
    bridge = BRIDGE_NOTE.read_text()
    target = TARGET_NOTE.read_text()
    runner = TARGET_RUNNER.read_text()
    rows = ledger_rows()
    check(
        "retained staggered two-body mediator remains retained_bounded, not widened by this branch",
        effective_status(rows, "staggered_self_consistent_two_body_note_2026-04-11") == "retained_bounded",
        detail=effective_status(rows, "staggered_self_consistent_two_body_note_2026-04-11"),
    )
    gen_statuses = {
        "three_generation_observable_theorem_note": effective_status(rows, "three_generation_observable_theorem_note"),
        "three_generation_structure_note": effective_status(rows, "three_generation_structure_note"),
        "three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10": effective_status(
            rows,
            "three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10",
        ),
    }
    check(
        "generation-corner dependencies are retained or retained_bounded on current main",
        all(status in {"retained", "retained_bounded"} for status in gen_statuses.values()),
        detail=str(gen_statuses),
    )
    check(
        "bridge note declares exact-support source status and independent audit requirement",
        "exact-support source-note proposal" in bridge
        and "independent audit required" in bridge
        and "does not write or imply an audit verdict" in bridge,
    )
    check(
        "bridge note proves boundary and normalization inputs explicitly",
        "Lambda_L = (Z/LZ)^3" in bridge
        and "N = L^3" in bridge
        and "normalized characters" in bridge
        and "mu^2 > 0" in bridge,
    )
    check(
        "conditional target note cites the new one-hop bridge note, runner, and cache",
        BRIDGE_NOTE.name in target
        and "scripts/generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.py" in target
        and "logs/runner-cache/generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.txt" in target,
    )
    check(
        "target runner exposes the bridge as a source check, not only as prose",
        BRIDGE_NOTE.name in runner and "hf_vq_bridge_source_checks" in runner,
    )


def math_checks() -> None:
    print("\n-- Periodic Laplacian Fourier diagonalization --")
    for L in (4, 6):
        lap = periodic_laplacian(L)
        max_residual = 0.0
        for k in k_grid(L):
            phi = fourier_vector(L, k)
            residual = np.linalg.norm(lap @ phi - eps(k) * phi)
            max_residual = max(max_residual, float(residual))
        check(
            f"L={L}: normalized translation characters diagonalize the periodic graph Laplacian",
            max_residual < 1e-10,
            detail=f"max residual {max_residual:.3e}",
        )

    print("\n-- Screened Green kernel multiplier --")
    for L in (4, 6):
        dense = dense_kernel(L)
        spectral = fourier_kernel(L)
        err = np.max(np.abs(dense - spectral))
        check(
            f"L={L}: -G*(Lap+mu^2 I)^-1 equals Fourier multiplier Vq(q)=-G/(eps(q)+mu^2)",
            err < 1e-8,
            detail=f"max entry error {err:.3e}",
        )

    print("\n-- Hartree-Fock plane-wave mutual energy normalization --")
    for L in (4, 6):
        errs = []
        for i, j in PAIRS:
            errs.append(abs(hf_dense_delta(L, i, j) - hf_formula_delta(L, i, j)))
        check(
            f"L={L}: dense Hartree-minus-exchange equals [Vq(0)-Vq(Delta k)]/N for all corner pairs",
            max(errs) < 1e-7,
            detail=f"max pair error {max(errs):.3e}",
        )

    eps_pairs = []
    deltas = []
    for i, j in PAIRS:
        delta_k = tuple(float(a - b) for a, b in zip(CORNERS[i], CORNERS[j]))
        eps_pairs.append(eps(delta_k))
        deltas.append(hf_formula_delta(10, i, j))
    check(
        "all three hw=1 corner transfers have eps(Delta k)=8",
        np.allclose(eps_pairs, 8.0),
        detail=str([round(x, 6) for x in eps_pairs]),
    )
    check(
        "the corner mutual energies are equal and negative for G>0, mu^2>0",
        all(d < 0 for d in deltas) and np.allclose(deltas, deltas[0]),
        detail=str([f"{d:.6e}" for d in deltas]),
    )
    scaled = [abs(hf_formula_delta(L, 1, 2)) * (L**3) for L in (4, 6, 8, 10, 12)]
    check(
        "the pure-corner magnitude scales as 1/N with fixed IR multiplier",
        np.allclose(scaled, scaled[0], rtol=1e-12, atol=1e-8),
        detail=f"|delta|*N={scaled[0]:.6f}",
    )


def main() -> int:
    print("=" * 78)
    print("GENERATION CORNER HF Vq SCREENED-POISSON BRIDGE  [exact support]")
    print("=" * 78)
    source_checks()
    math_checks()
    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("FAILURE: bridge source packet is not green; do not use for re-audit.")
        return 1
    print(
        "FINDING: exact-support bridge packet is internally green. It derives the "
        "periodic screened-Poisson Fourier multiplier and the finite Slater "
        "Hartree-minus-exchange normalization from native finite-lattice linear "
        "algebra, while leaving the new bridge for independent audit."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
