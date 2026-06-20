#!/usr/bin/env python3
"""Controlled-copy dynamics to projective record-write isometry.

This runner verifies that the explicit finite controlled-copy kick used in the
record-formation dynamics note induces the ideal pointer-label write isometry
used by the finite Kraus bridge, after a fixed record-register basis
calibration. It does not derive arbitrary persistent dynamics, a physical
Hamiltonian, a Born rule, or any downstream selector.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "record_formation_controlled_copy_write_isometry_2026_06_18.json"

NOTE = DOCS / "RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md"
TARGET_BRIDGE = DOCS / "RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md"
FORMATION_NOTE = DOCS / "RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md"
KRAUS_NOTE = DOCS / "PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md"

TOL = 1e-12
PASS = 0
FAIL = 0

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
P0 = np.array([[1, 0], [0, 0]], dtype=complex)
P1 = np.array([[0, 0], [0, 1]], dtype=complex)
KET0 = np.array([1, 0], dtype=complex)
KET1 = np.array([0, 1], dtype=complex)


def report(label: str, ok: bool, detail: Any = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    if isinstance(detail, np.ndarray):
        has_detail = detail.size > 0
    else:
        has_detail = detail != ""
    suffix = f" :: {detail}" if has_detail else ""
    print(f"{tag} {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def dagger(a: np.ndarray) -> np.ndarray:
    return a.conj().T


def close(a: np.ndarray, b: np.ndarray, tol: float = TOL) -> bool:
    return np.linalg.norm(a - b) < tol


def rot_x(theta: float) -> np.ndarray:
    return np.cos(theta) * I2 - 1j * np.sin(theta) * SX


def controlled_copy(theta: float) -> np.ndarray:
    return np.kron(P0, rot_x(theta)) + np.kron(P1, rot_x(-theta))


def blank_embedding(extra_fragments: int = 1) -> np.ndarray:
    """Map |psi>_S to |psi>_S tensor |0>...|0>."""
    cols = []
    for ket in (KET0, KET1):
        v = ket
        for _ in range(extra_fragments):
            v = np.kron(v, KET0)
        cols.append(v)
    return np.column_stack(cols)


def op_on(single: np.ndarray, pos: int, n: int) -> np.ndarray:
    mats = [I2] * n
    mats[pos] = single
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def controlled_copy_on(env_pos: int, n: int, theta: float) -> np.ndarray:
    p0_s = op_on(P0, 0, n)
    p1_s = op_on(P1, 0, n)
    r_plus = op_on(rot_x(theta), env_pos, n)
    r_minus = op_on(rot_x(-theta), env_pos, n)
    return p0_s @ r_plus + p1_s @ r_minus


def swap_system_record() -> np.ndarray:
    """Swap a two-qubit system-major basis |s>|r> to record-major |r>|s>."""
    swap = np.zeros((4, 4), dtype=complex)
    for s in range(2):
        for r in range(2):
            src = 2 * s + r
            dst = 2 * r + s
            swap[dst, src] = 1.0
    return swap


def basis_label(index: int, n: int) -> np.ndarray:
    out = np.array([1], dtype=complex)
    for bit in range(n):
        out = np.kron(out, KET1 if (index >> (n - bit - 1)) & 1 else KET0)
    return out


def source_checks() -> dict[str, Any]:
    section("Source and authority checks")
    for path in (NOTE, TARGET_BRIDGE, FORMATION_NOTE, KRAUS_NOTE):
        report(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Controlled-Copy Write-Isometry Theorem",
        "U_cc(pi/4)(|psi> tensor |0>_R)",
        "<eta_0|eta_1> = 0",
        "fixed record-register calibration",
        "K_r = <r|W = P_r",
        "What This Does Not Close",
    ):
        report(f"new theorem contains marker: {phrase}", phrase in note)

    target = read(TARGET_BRIDGE)
    report("target bridge cites controlled-copy write-isometry theorem", NOTE.name in target)
    report("target bridge no longer leaves ideal write as an unqualified premise", "ideal pointer-label write is supplied by the controlled-copy" in target)
    report(
        "new theorem names target bridge without markdown back-edge",
        TARGET_BRIDGE.name in note and f"]({TARGET_BRIDGE.name})" not in note,
    )

    formation_note = read(FORMATION_NOTE)
    kraus_note = read(KRAUS_NOTE)
    report("formation source carries controlled-copy construction", "controlled-copy" in formation_note and "pi/(4g)" in formation_note)
    report("finite Kraus source carries isometry-to-Kraus algebra", "normalized linear isometry `W`" in kraus_note and "Kraus/CPTP" in kraus_note)

    return {
        "formation_source": FORMATION_NOTE.name,
        "kraus_source": KRAUS_NOTE.name,
        "target_bridge": TARGET_BRIDGE.name,
    }


def single_fragment_dynamic_write() -> None:
    section("Single fresh-fragment controlled-copy write")
    theta = np.pi / 4.0
    u = controlled_copy(theta)
    emb = blank_embedding(1)

    eta0 = rot_x(theta) @ KET0
    eta1 = rot_x(-theta) @ KET0
    report("controlled-copy U is unitary", close(dagger(u) @ u, np.eye(4)))
    report("eta_0 and eta_1 are normalized", abs(np.vdot(eta0, eta0) - 1) < TOL and abs(np.vdot(eta1, eta1) - 1) < TOL)
    report("eta_0 and eta_1 are orthogonal at theta=pi/4", abs(np.vdot(eta0, eta1)) < TOL, np.vdot(eta0, eta1))

    calibration = np.vstack([eta0.conj(), eta1.conj()])
    report("record calibration C_R is unitary", close(dagger(calibration) @ calibration, I2))
    report("C_R eta_0 = |0>", close(calibration @ eta0, KET0))
    report("C_R eta_1 = |1>", close(calibration @ eta1, KET1))

    w_sys_major = np.kron(I2, calibration) @ u @ emb
    w_record_major = swap_system_record() @ w_sys_major
    ideal_w = np.vstack([P0, P1])
    report("calibrated controlled-copy isometry equals ideal W", close(w_record_major, ideal_w), w_record_major)
    report("dynamic W^dagger W = I", close(dagger(w_record_major) @ w_record_major, I2))

    k0 = w_record_major[0:2, :]
    k1 = w_record_major[2:4, :]
    report("extracted K_0 equals P_0", close(k0, P0))
    report("extracted K_1 equals P_1", close(k1, P1))
    report("Kraus resolution closes", close(dagger(k0) @ k0 + dagger(k1) @ k1, I2))

    ket = np.array([np.sqrt(0.63), np.exp(0.41j) * np.sqrt(0.37)], dtype=complex)
    image = w_record_major @ ket
    expected = np.array([ket[0], 0, 0, ket[1]], dtype=complex)
    report("generic coherent input maps to orthogonal pointer-label superposition", close(image, expected))


def fresh_fragment_chain() -> None:
    section("Fresh-fragment chain and idle completed labels")
    theta = np.pi / 4.0
    n = 3
    u1 = controlled_copy_on(1, n, theta)
    u2 = controlled_copy_on(2, n, theta)
    eta0 = rot_x(theta) @ KET0
    eta1 = rot_x(-theta) @ KET0
    calibration = np.vstack([eta0.conj(), eta1.conj()])
    c1 = op_on(calibration, 1, n)
    c2 = op_on(calibration, 2, n)
    emb = blank_embedding(2)

    ket = np.array([np.sqrt(0.2), -1j * np.sqrt(0.8)], dtype=complex)
    final = c2 @ c1 @ u2 @ u1 @ emb @ ket
    expected = ket[0] * basis_label(0b000, n) + ket[1] * basis_label(0b111, n)
    report("two fresh fragments carry matching pointer labels", close(final, expected), final)

    eta0_projector = np.outer(eta0, eta0.conj())
    eta1_projector = np.outer(eta1, eta1.conj())
    report("later fresh-fragment kick commutes with completed E1 eta_0 label", close(u2 @ op_on(eta0_projector, 1, n), op_on(eta0_projector, 1, n) @ u2))
    report("later fresh-fragment kick commutes with completed E1 eta_1 label", close(u2 @ op_on(eta1_projector, 1, n), op_on(eta1_projector, 1, n) @ u2))


def boundary_controls() -> dict[str, bool]:
    section("Boundary controls")
    flags = {
        "controlled_copy_to_projective_W_derived_for_explicit_model": True,
        "arbitrary_persistent_dynamics_to_W_derived": False,
        "quantum_darwinism_record_reading_derived_from_minimal_axioms": False,
        "physical_hamiltonian_or_coupling_selected": False,
        "born_rule_from_post_record_counts_derived": False,
        "generation_or_koide_dial_selected": False,
        "audit_verdict_applied": False,
    }
    report("controlled-copy to projective W is derived for explicit model", flags["controlled_copy_to_projective_W_derived_for_explicit_model"])
    report("arbitrary persistent dynamics to W remains false", not flags["arbitrary_persistent_dynamics_to_W_derived"])
    report("quantum-Darwinism record reading remains a bounded model bridge", not flags["quantum_darwinism_record_reading_derived_from_minimal_axioms"])
    report("physical Hamiltonian/coupling selection remains false", not flags["physical_hamiltonian_or_coupling_selected"])
    report("Born rule from post-record counts remains false", not flags["born_rule_from_post_record_counts_derived"])
    report("generation/Koide dial selection remains false", not flags["generation_or_koide_dial_selected"])
    report("audit verdict applied remains false", not flags["audit_verdict_applied"])
    return flags


def main() -> int:
    print("=" * 88)
    print("RECORD FORMATION CONTROLLED-COPY WRITE-ISOMETRY THEOREM")
    print("=" * 88)
    statuses = source_checks()
    single_fragment_dynamic_write()
    fresh_fragment_chain()
    flags = boundary_controls()

    result = {
        "status": "exact support: explicit controlled-copy/fresh-fragment dynamics induces the projective record-write isometry after fixed record-basis calibration",
        "proposal_allowed": False,
        "proposal_allowed_reason": "This closes the source-side ideal-write bridge only for the explicit finite controlled-copy model; arbitrary dynamics and framework-wide record-production remain outside scope.",
        "trace_class": "direct_blocker_closure",
        "reachability_to_target": "closes_source_side_blocker",
        "dependency_statuses": statuses,
        "boundary_flags": flags,
        "pass_count": PASS,
        "fail_count": FAIL,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
