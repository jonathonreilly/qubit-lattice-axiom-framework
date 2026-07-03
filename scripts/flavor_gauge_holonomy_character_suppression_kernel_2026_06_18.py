#!/usr/bin/env python3
"""Finite character-suppression kernel for the flavor holonomy no-go.

This runner isolates the framework-native part of the holonomy argument.  On
the retained finite link surface, a gauge-invariant fibre average multiplies
the generation hop coefficient by chi_R(U)/d_R.  For every finite-dimensional
unitary link representation, |chi_R(U)/d_R| <= 1, so the holonomy can suppress
the Koide r-ratio but cannot enhance it.

The runner deliberately does not derive the physical sector-to-representation
readout.  That bridge remains open in the parent flavor holonomy note.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "FLAVOR_GAUGE_HOLONOMY_CHARACTER_SUPPRESSION_KERNEL_NARROW_THEOREM_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "FLAVOR_GAUGE_HOLONOMY_SUPPRESSES_R_BELOW_LEPTONIC_WRONG_ORDERING_NARROW_NO_GO_NOTE_2026-06-15.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if detail:
        print(f"       {detail}")
    PASS += int(ok)
    FAIL += int(not ok)


def ledger_status(claim_id: str) -> str | None:
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    row = rows.get(claim_id, {})
    return row.get("effective_status") or row.get("audit_status")


def phases(root_count: int, d: int) -> list[np.ndarray]:
    roots = [np.exp(2j * np.pi * k / root_count) for k in range(root_count)]
    return [np.array(zs, dtype=complex) for zs in itertools.product(roots, repeat=d)]


def character_gap(zs: np.ndarray) -> tuple[float, float]:
    """Return both sides of d^2 - |sum z_i|^2 = sum_{i<j}|z_i-z_j|^2."""
    d = len(zs)
    left = float(d * d - abs(np.sum(zs)) ** 2)
    right = float(
        sum(abs(zs[i] - zs[j]) ** 2 for i in range(d) for j in range(i + 1, d))
    )
    return left, right


def effective_generation_matrix(a: float, b: complex, evals: np.ndarray) -> np.ndarray:
    """Fibre-average the three-generation hop over a diagonalized link."""
    d = len(evals)
    U = np.diag(evals)
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    Cd = C.conj().T
    H = a * np.kron(np.eye(3), np.eye(d))
    H = H + b * np.kron(C, U) + np.conj(b) * np.kron(Cd, U.conj().T)
    M = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            block = H[i * d : (i + 1) * d, j * d : (j + 1) * d]
            M[i, j] = np.trace(block) / d
    return M


def main() -> int:
    print("FLAVOR GAUGE HOLONOMY CHARACTER-SUPPRESSION KERNEL")
    print("=" * 72)

    retained_sources = {
        "matter_gauge_minimal_coupling_fiber_frame_forces_connection_narrow_theorem_note_2026-06-08":
            ledger_status("matter_gauge_minimal_coupling_fiber_frame_forces_connection_narrow_theorem_note_2026-06-08"),
        "fiber_frame_local_redundancy_bridge_narrow_theorem_note_2026-06-09":
            ledger_status("fiber_frame_local_redundancy_bridge_narrow_theorem_note_2026-06-09"),
        "koide_gamma_axis_covariant_full_cube_orbit_law_note_2026-04-18":
            ledger_status("koide_gamma_axis_covariant_full_cube_orbit_law_note_2026-04-18"),
        "koide_circulant_character_bridge_narrow_theorem_note_2026-05-09":
            ledger_status("koide_circulant_character_bridge_narrow_theorem_note_2026-05-09"),
        "koide_kappa_spectrum_operator_bridge_theorem_note_2026-04-19":
            ledger_status("koide_kappa_spectrum_operator_bridge_theorem_note_2026-04-19"),
        "three_generation_observable_theorem_note":
            ledger_status("three_generation_observable_theorem_note"),
    }
    retained_ok = {"retained", "retained_bounded"}
    check(
        "kernel dependencies are retained-grade in the live ledger",
        all(status in retained_ok for status in retained_sources.values()),
        ", ".join(f"{cid}={status}" for cid, status in retained_sources.items()),
    )

    max_identity_error = 0.0
    min_gap = 1e9
    equality_violations = 0
    for d in range(1, 6):
        for zs in phases(root_count=5, d=d):
            left, right = character_gap(zs)
            max_identity_error = max(max_identity_error, abs(left - right))
            min_gap = min(min_gap, left)
            normalized = abs(np.sum(zs) / d)
            all_equal = bool(np.allclose(zs, zs[0]))
            if normalized > 1 + 1e-12:
                equality_violations += 1
            if abs(normalized - 1) < 1e-12 and not all_equal:
                equality_violations += 1
    check(
        "finite triangle-identity proof certificate is nonnegative on phase grid",
        max_identity_error < 1e-10 and min_gap > -1e-10 and equality_violations == 0,
        f"max_identity_error={max_identity_error:.3e}, min_gap={min_gap:.3e}, equality_violations={equality_violations}",
    )

    a = 1.0
    b = np.sqrt(0.5)
    r0 = abs(b) ** 2 / (a * a)
    max_formula_error = 0.0
    max_bound_excess = 0.0
    for d in [1, 2, 3, 4, 5, 8]:
        probes = phases(root_count=7, d=min(d, 4))
        if d > 4:
            probes = [np.resize(zs, d) for zs in probes[:200]]
        for zs in probes:
            M = effective_generation_matrix(a, b, zs)
            a_eff = M[0, 0].real
            b_eff = M[1, 0]
            r_eff = abs(b_eff) ** 2 / (a_eff * a_eff)
            predicted = r0 * abs(np.sum(zs) / len(zs)) ** 2
            max_formula_error = max(max_formula_error, abs(r_eff - predicted))
            max_bound_excess = max(max_bound_excess, r_eff - r0)
    check(
        "fibre-averaged hop coefficient is exactly character-normalized",
        max_formula_error < 1e-10,
        f"max_formula_error={max_formula_error:.3e}",
    )
    check(
        "normalized character multiplier cannot enhance r",
        max_bound_excess < 1e-10,
        f"max_bound_excess={max_bound_excess:.3e}",
    )

    for free_r0 in [0.11, 0.31, 0.5, 0.87]:
        b_free = np.sqrt(free_r0)
        zs = np.array([1, np.exp(2j * np.pi / 5), np.exp(4j * np.pi / 5)])
        M = effective_generation_matrix(1.0, b_free, zs)
        r_eff = abs(M[1, 0]) ** 2 / (M[0, 0].real ** 2)
        check(
            f"bound propagates an arbitrary free r0={free_r0:.2f}",
            r_eff <= free_r0 + 1e-12,
            f"r_eff={r_eff:.6f}",
        )

    note = NOTE.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8")
    flat_note_lower = " ".join(note.lower().split())
    flat_parent = " ".join(parent.split())
    check(
        "kernel note records framework-native proof and no new axiom",
        "character-suppression kernel" in flat_note_lower
        and "No new axiom" in note
        and "d^2 - |sum z_i|^2" in note
        and "sum_{i<j}|z_i-z_j|^2" in note,
    )
    check(
        "parent note cites the kernel note, runner, and cache",
        "FLAVOR_GAUGE_HOLONOMY_CHARACTER_SUPPRESSION_KERNEL_NARROW_THEOREM_NOTE_2026-06-18.md" in parent
        and "flavor_gauge_holonomy_character_suppression_kernel_2026_06_18.py" in parent
        and "flavor_gauge_holonomy_character_suppression_kernel_2026_06_18.txt" in parent,
    )
    check(
        "physical sector-to-representation readout remains open",
        "physical sector-to-representation/readout bridge remains open" in flat_parent
        and "does not derive the colourless-lepton/trivial-representation or coloured-quark/nontrivial-representation assignment" in flat_parent,
    )
    check(
        "source change does not promote audit status",
        "audited_clean" not in parent
        and "proposed_retained" not in parent
        and "source note awaiting independent audit handling" in parent,
    )

    print()
    print(
        "VERDICT: the character-suppression kernel is a finite framework-native "
        "support theorem; the flavor sector readout/representation assignment "
        "remains open for the parent no-go."
    )
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
