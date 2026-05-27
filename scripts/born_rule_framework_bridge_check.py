#!/usr/bin/env python3
"""Finite-region Born-rule framework bridge check.

This runner verifies the narrow algebraic composition used by
`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` after the
2026-05-27 dependency repair: tracial pre-record probabilities, canonical
projective-record Lüders conditioning, sequential effects, and the rank-one
Born form on finite qubit regions.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def ket(values: list[complex]) -> np.ndarray:
    v = np.array(values, dtype=complex).reshape((-1, 1))
    return v / np.linalg.norm(v)


def projector(v: np.ndarray) -> np.ndarray:
    return v @ v.conj().T


def density_from_ket(v: np.ndarray) -> np.ndarray:
    return projector(v)


def tr(x: np.ndarray) -> complex:
    return np.trace(x)


def is_close(a: complex | float, b: complex | float, tol: float = 1.0e-12) -> bool:
    return abs(a - b) < tol


def retained_like(status: str | None) -> bool:
    return status in {"retained", "retained_bounded", "retained_no_go", "open_gate"} or (
        isinstance(status, str) and status.startswith("decoration_under_")
    )


def test_dependency_statuses() -> None:
    section("T0: direct framework dependencies are retained-grade")
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    required = [
        "gleason_on_qubit_lattice_projection_lattice_narrow_theorem_note_2026-05-20",
        "busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20",
        "pre_record_reference_state_tracial_derivation_note_2026-05-20",
        "kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20",
        "lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22",
        "luders_rule_from_composition_consistency_note_2026-05-20",
        "luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22",
    ]
    for cid in required:
        row = rows.get(cid, {})
        status = row.get("effective_status")
        check(f"{cid} is retained-grade for dependency use", retained_like(status), f"effective_status={status}")


def test_pre_record_tracial_probability() -> None:
    section("T1: pre-record tracial probability on a finite qubit region")
    dim = 4
    rho_ref = np.eye(dim, dtype=complex) / dim
    e0 = ket([1, 0, 0, 0])
    e1 = ket([0, 1, 0, 0])
    p0 = projector(e0)
    p1 = projector(e1)
    effect = p0 + p1
    prob = tr(rho_ref @ effect).real
    check("rho_ref = I/d is normalized", is_close(tr(rho_ref), 1.0), f"Tr rho_ref={tr(rho_ref)}")
    check("rank-2 projector has pre-record probability rank/d", is_close(prob, 0.5), f"p={prob}")
    check("effect is positive and bounded by identity", np.all(np.linalg.eigvalsh(effect) >= -1e-12) and np.all(np.linalg.eigvalsh(np.eye(dim) - effect) >= -1e-12))


def test_busch_single_site_povm_effect() -> None:
    section("T2: single-site POVM effect uses density trace form")
    rho = np.array([[0.7, 0.1], [0.1, 0.3]], dtype=complex)
    effect = np.array([[0.25, 0.0], [0.0, 0.75]], dtype=complex)
    prob = tr(rho @ effect).real
    expected = 0.7 * 0.25 + 0.3 * 0.75
    check("single-site POVM probability is Tr(rho E)", is_close(prob, expected), f"p={prob:.12f}, expected={expected:.12f}")
    check("probability lies in [0,1]", -1e-12 <= prob <= 1 + 1e-12, f"p={prob:.12f}")


def test_projective_record_luders_update() -> None:
    section("T3: canonical projective record conditions tracial state to a pure state")
    psi = ket([1, 1j])
    p = projector(psi)
    rho_ref = np.eye(2, dtype=complex) / 2
    denom = tr(p @ rho_ref @ p)
    rho_post = p @ rho_ref @ p / denom
    check("projector has nonzero pre-record probability", denom.real > 0, f"p(P)={denom.real:.12f}")
    check("Luders update from I/2 through rank-one P gives P", np.max(np.abs(rho_post - p)) < 1e-12)
    check("post-record state remains normalized", is_close(tr(rho_post), 1.0), f"Tr={tr(rho_post)}")


def test_rank_one_born_form() -> None:
    section("T4: rank-one Born form")
    psi = ket([1, 2j])
    phi = ket([1, 1])
    rho = density_from_ket(psi)
    effect = projector(phi)
    p_trace = tr(rho @ effect).real
    p_inner = abs((phi.conj().T @ psi)[0, 0]) ** 2
    check("Tr(|psi><psi| |phi><phi|) = |<phi|psi>|^2", is_close(p_trace, p_inner), f"trace={p_trace:.12f}, inner={p_inner:.12f}")


def test_sequential_projective_effect() -> None:
    section("T5: sequential projective effect P E P")
    psi = ket([1, 0])
    p = projector(psi)
    theta = 0.37
    phi = ket([np.cos(theta), np.sin(theta)])
    e = projector(phi)
    rho_ref = np.eye(2, dtype=complex) / 2
    joint = tr(rho_ref @ p @ e @ p).real
    prior = tr(rho_ref @ p).real
    conditional = joint / prior
    born = abs((phi.conj().T @ psi)[0, 0]) ** 2
    check("sequential joint effect is positive probability", joint >= -1e-12 and prior > 0, f"joint={joint:.12f}, prior={prior:.12f}")
    check("conditional sequential probability equals Born form", is_close(conditional, born), f"conditional={conditional:.12f}, born={born:.12f}")


def test_projective_kraus_tp() -> None:
    section("T6: projective record Kraus family is trace preserving")
    e0 = ket([1, 0])
    e1 = ket([0, 1])
    kraus = [projector(e0), projector(e1)]
    tp = sum(k.conj().T @ k for k in kraus)
    check("sum_r K_r^dagger K_r = I for projective record", np.max(np.abs(tp - np.eye(2))) < 1e-12)


def test_source_firewall() -> None:
    section("T7: source-note firewall")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "2026-05-27 Framework-Dependency Repair",
        "GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md",
        "BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md",
        "LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md",
        "durable/native persistent-record formation",
        "Independent audit owns the effective status",
    ]
    for phrase in required:
        check(f"source contains boundary/dependency phrase: {phrase}", phrase in text)


def main() -> int:
    print("# Born-rule finite framework bridge check")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_dependency_statuses()
    test_pre_record_tracial_probability()
    test_busch_single_site_povm_effect()
    test_projective_record_luders_update()
    test_rank_one_born_form()
    test_sequential_projective_effect()
    test_projective_kraus_tp()
    test_source_firewall()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
