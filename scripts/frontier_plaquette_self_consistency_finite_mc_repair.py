#!/usr/bin/env python3
"""Finite MC diagnostic repair for PLAQUETTE_SELF_CONSISTENCY_NOTE.md.

This runner checks only the repaired finite claim:

  * finite SU(3) Wilson plaquette observables are well-defined;
  * a small deterministic Monte Carlo diagnostic evaluates a selected finite
    surface without introducing a fit parameter;
  * the canonical 0.5934 value is explicitly not derived here.

It does not certify an infinite-volume physical plaquette value.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md"
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
CLAIM_ID = "plaquette_self_consistency_note"
RUNNER_PATH = "scripts/frontier_plaquette_self_consistency_finite_mc_repair.py"
N_C = 3

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def project_su3(z: np.ndarray) -> np.ndarray:
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    phases = phases / np.where(np.abs(phases) == 0, 1.0, np.abs(phases))
    q = q @ np.diag(np.conj(phases))
    det_q = np.linalg.det(q)
    q = q * np.exp(-1j * np.angle(det_q) / 3.0)
    return q


def random_su3(rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    return project_su3(z)


def near_identity_su3(rng: np.random.Generator, epsilon: float = 0.18) -> np.ndarray:
    h = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    h = (h + h.conj().T) / 2.0
    h -= np.trace(h) * np.eye(3) / 3.0
    return project_su3(np.eye(3, dtype=complex) + 1j * epsilon * h)


def check_note_boundary() -> None:
    section("Source-note boundary")
    text = NOTE_PATH.read_text()
    required = [
        "bounded-support finite Wilson-plaquette diagnostic",
        "The canonical infinite-volume value `0.5934` is an admitted comparison/reuse number here",
        "That is the entire repaired claim.",
        "a short finite diagnostic run is not the same as an infinite-volume physical certificate",
        "This row does not claim:",
        "a completed same-surface MC certificate for `0.5934`",
    ]
    for needle in required:
        check(f"note contains required boundary: {needle!r}", needle in text)

    forbidden = [
        "`0.5934` is derived",
        "canonical numerical value `0.5934` is derived",
        "this note supplies a completed same-surface MC certificate",
        "runner certifies the physical value",
        "analytic beta=6 closure is supplied by this note",
    ]
    for needle in forbidden:
        check(f"note avoids overclaim phrase: {needle!r}", needle not in text)


def check_su3_construction() -> None:
    section("SU(3) construction")
    rng = np.random.default_rng(2026052501)
    max_unitarity = 0.0
    max_det_phase = 0.0
    for _ in range(50):
        u = random_su3(rng)
        max_unitarity = max(max_unitarity, float(np.linalg.norm(u.conj().T @ u - np.eye(3))))
        max_det_phase = max(max_det_phase, abs(np.linalg.det(u) - 1.0))
    check("random_su3 returns unitary matrices", max_unitarity < 1e-12, f"max={max_unitarity:.2e}")
    check("random_su3 returns determinant-one matrices", max_det_phase < 1e-12, f"max={max_det_phase:.2e}")


def lattice_counts(L: int, ndim: int = 4) -> tuple[int, int]:
    sites = L**ndim
    links = sites * ndim
    plaquettes = sites * (ndim * (ndim - 1) // 2)
    return links, plaquettes


def cold_links(L: int, ndim: int = 4) -> dict[tuple[int, ...], list[np.ndarray]]:
    return {coords: [np.eye(3, dtype=complex) for _ in range(ndim)] for coords in np.ndindex(*([L] * ndim))}


def random_links(L: int, rng: np.random.Generator, ndim: int = 4) -> dict[tuple[int, ...], list[np.ndarray]]:
    return {coords: [random_su3(rng) for _ in range(ndim)] for coords in np.ndindex(*([L] * ndim))}


def plaquette(links: dict[tuple[int, ...], list[np.ndarray]], coords: tuple[int, ...], mu: int, nu: int, L: int) -> np.ndarray:
    x_mu = list(coords)
    x_mu[mu] = (x_mu[mu] + 1) % L
    x_nu = list(coords)
    x_nu[nu] = (x_nu[nu] + 1) % L
    return (
        links[coords][mu]
        @ links[tuple(x_mu)][nu]
        @ links[tuple(x_nu)][mu].conj().T
        @ links[coords][nu].conj().T
    )


def average_plaquette(links: dict[tuple[int, ...], list[np.ndarray]], L: int, ndim: int = 4) -> float:
    total = 0.0
    count = 0
    for coords in np.ndindex(*([L] * ndim)):
        for mu in range(ndim):
            for nu in range(mu + 1, ndim):
                total += float(np.trace(plaquette(links, coords, mu, nu, L)).real / N_C)
                count += 1
    return total / count


def wilson_action(links: dict[tuple[int, ...], list[np.ndarray]], beta: float, L: int, ndim: int = 4) -> float:
    total = 0.0
    for coords in np.ndindex(*([L] * ndim)):
        for mu in range(ndim):
            for nu in range(mu + 1, ndim):
                total += float(N_C - np.trace(plaquette(links, coords, mu, nu, L)).real)
    return beta * total / N_C


def check_finite_lattice_observable() -> None:
    section("Finite Wilson observable")
    rng = np.random.default_rng(2026052502)
    for L in [2, 3]:
        links_count, plaquette_count = lattice_counts(L)
        check(f"L={L}: link count is L^4*4", links_count == L**4 * 4, f"links={links_count}")
        check(f"L={L}: plaquette count is L^4*6", plaquette_count == L**4 * 6, f"plaquettes={plaquette_count}")
        links = random_links(L, rng)
        pbar = average_plaquette(links, L)
        action = wilson_action(links, beta=6.0, L=L)
        check(f"L={L}: average plaquette is finite and bounded", math.isfinite(pbar) and -1.0 <= pbar <= 1.0, f"Pbar={pbar:.6f}")
        check(f"L={L}: Wilson action is finite and nonnegative", math.isfinite(action) and action >= 0.0, f"S={action:.6f}")


def one_plaquette_action(u: np.ndarray, beta: float) -> float:
    return -beta * float(np.trace(u).real / N_C)


def one_plaquette_chain(beta: float, seed: int, steps: int = 1200, burn: int = 200) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    u = random_su3(rng) if beta == 0.0 else np.eye(3, dtype=complex)
    values: list[float] = []
    accepted = 0
    for step in range(steps):
        proposal = near_identity_su3(rng) @ u
        old_s = one_plaquette_action(u, beta)
        new_s = one_plaquette_action(proposal, beta)
        if new_s < old_s or rng.random() < math.exp(-(new_s - old_s)):
            u = proposal
            accepted += 1
        if step >= burn:
            values.append(float(np.trace(u).real / N_C))
    return float(np.mean(values)), accepted / steps


def check_one_plaquette_mc_diagnostic() -> None:
    section("One-plaquette MC diagnostic")
    beta0_mean, beta0_acc = one_plaquette_chain(beta=0.0, seed=2026052503)
    beta6_mean, beta6_acc = one_plaquette_chain(beta=6.0, seed=2026052504)
    check("beta=0 one-plaquette diagnostic stays near Haar mean", abs(beta0_mean) < 0.25, f"mean={beta0_mean:.6f}, acc={beta0_acc:.3f}")
    check("beta=6 one-plaquette diagnostic shifts toward ordered plaquettes", beta6_mean > 0.25, f"mean={beta6_mean:.6f}, acc={beta6_acc:.3f}")
    check("diagnostic distinguishes beta=6 from beta=0", beta6_mean - beta0_mean > 0.30, f"delta={beta6_mean - beta0_mean:.6f}")


def check_audit_metadata_after_pipeline() -> None:
    section("Audit metadata after pipeline regeneration")
    if not LEDGER_PATH.exists():
        check("audit ledger exists", False, str(LEDGER_PATH))
        return
    ledger = json.loads(LEDGER_PATH.read_text())
    row = ledger.get("rows", {}).get(CLAIM_ID)
    check(f"{CLAIM_ID} row exists", row is not None)
    if row is None:
        return
    check("claim_type is bounded_theorem", row.get("claim_type") == "bounded_theorem", str(row.get("claim_type")))
    check("audit_status reset to unaudited", row.get("audit_status") == "unaudited", str(row.get("audit_status")))
    check("effective_status reset to unaudited", row.get("effective_status") == "unaudited", str(row.get("effective_status")))
    check("runner path is finite-MC repair runner", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("direct deps are empty for finite diagnostic theorem", row.get("deps") == [], str(row.get("deps")))
    check("open dependency paths are empty", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))


def main() -> int:
    print("Plaquette self-consistency finite MC diagnostic repair")
    check_note_boundary()
    check_su3_construction()
    check_finite_lattice_observable()
    check_one_plaquette_mc_diagnostic()
    check_audit_metadata_after_pipeline()
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
