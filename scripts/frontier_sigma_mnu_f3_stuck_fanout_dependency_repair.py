#!/usr/bin/env python3
"""Dependency-edge repair runner for the Sigma m_nu F3 fan-out synthesis.

The prior audit asked for direct authorities for the Cycle-1 DM cross-bound,
T-4F-alpha-2, current-bank Omega_DM, Lane 5 C1 status, and
eta/leptogenesis status. This runner checks that the source note exposes
those authorities, verifies the live ledger status of the retained support
rows, and recomputes the decisive Sigma m_nu arithmetic.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def row(ledger: dict, claim_id: str) -> dict:
    return ledger["rows"][claim_id]


def main() -> int:
    note = DOCS / "SIGMA_MNU_F3_STUCK_FANOUT_SYNTHESIS_NOTE_2026-04-28.md"
    authority_files = {
        "cycle1": "SIGMA_MNU_F3_DM_CROSS_BOUND_AUDIT_NOTE_2026-04-28.md",
        "functional": "NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md",
        "omega_dm": "DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md",
        "lane5_firewall": "HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md",
        "lane5_a1": "HUBBLE_LANE5_C1_A1_GRASSMANN_NO_GO_NOTE_2026-04-28.md",
        "lane5_a4": "HUBBLE_LANE5_C1_A4_PARITY_GATE_CAR_BOUNDARY_NOTE_2026-04-29.md",
        "lane5_a5": "HUBBLE_LANE5_C1_A5_BOOLEAN_COFRAME_RESTRICTION_OBSTRUCTION_NOTE_2026-04-29.md",
        "lane5_a6": "HUBBLE_LANE5_C1_A6_BILINEAR_ACTIVE_BLOCK_SUPPORT_BOUNDARY_NOTE_2026-04-29.md",
        "lepto_status": "DM_LEPTOGENESIS_TRANSPORT_STATUS_NOTE_2026-05-10.md",
        "eta188": "ETA_188_STRUCTURAL_ORIGIN_PARTIAL_NOTE_2026-05-03.md",
    }

    print("Sigma m_nu F3 stuck-fanout dependency repair")
    print("=" * 72)

    note_text = note.read_text(encoding="utf-8")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))

    print()
    print("A. Authority packet")
    print("-" * 72)
    check("source note exists", note.exists(), str(note.relative_to(ROOT)))
    for label, filename in authority_files.items():
        path = DOCS / filename
        check(f"{label} authority exists", path.exists(), str(path.relative_to(ROOT)))
        check(f"{label} authority is directly cited", filename in note_text)

    print()
    print("B. Ledger status sanity")
    print("-" * 72)
    retained_expectations = {
        "neutrino_lane4_4f_sigma_m_nu_functional_form_theorem_note_2026-04-28": "retained",
        "hubble_lane5_c1_a1_grassmann_no_go_note_2026-04-28": "retained_no_go",
        "hubble_lane5_c1_a4_parity_gate_car_boundary_note_2026-04-29": "retained_no_go",
        "hubble_lane5_c1_a5_boolean_coframe_restriction_obstruction_note_2026-04-29": "retained_no_go",
        "hubble_lane5_c1_a6_bilinear_active_block_support_boundary_note_2026-04-29": "retained_bounded",
        "eta_188_structural_origin_partial_note_2026-05-03": "retained_bounded",
        "dm_leptogenesis_transport_status_note_2026-05-10": "meta",
    }
    for claim_id, expected in retained_expectations.items():
        got = row(ledger, claim_id).get("effective_status")
        check(f"{claim_id} effective_status is {expected}", got == expected, str(got))

    omega_row = row(ledger, "dm_full_closure_same_surface_thermal_bounding_theorem_note_2026-04-17")
    cycle1_row = row(ledger, "sigma_mnu_f3_dm_cross_bound_audit_note_2026-04-28")
    check("current-bank Omega_DM authority is explicitly not over-promoted", omega_row.get("effective_status") == "unaudited", str(omega_row.get("effective_status")))
    check("Cycle-1 cross-bound authority is explicitly not over-promoted", cycle1_row.get("effective_status") == "unaudited", str(cycle1_row.get("effective_status")))

    print()
    print("C. Cross-bound arithmetic")
    print("-" * 72)
    c_nu_ev = 93.14
    l_planck = 0.6847
    omega_b = 0.0493
    h = 0.6736
    omega_r = 9.182e-5
    omega_dm_lo = 0.267709052538
    omega_dm_hi = 0.269717881596
    sigma_lo = (1.0 - l_planck - omega_r - omega_b - omega_dm_hi) * c_nu_ev * h * h
    sigma_hi = (1.0 - l_planck - omega_r - omega_b - omega_dm_lo) * c_nu_ev * h * h
    check("framework current-bank endpoints give negative Sigma m_nu at Planck-style pins", sigma_lo < 0.0 and sigma_hi < 0.0, f"[{sigma_lo:.4f}, {sigma_hi:.4f}] eV")

    omega_m_h2_planck = 0.143
    omega_dm_h2_planck = 0.120
    omega_b_h2_planck = 0.0224
    sigma_cmb = (omega_m_h2_planck - omega_dm_h2_planck - omega_b_h2_planck) * c_nu_ev
    check("CMB h^2 alternate admission gives positive but below NO floor", 0.0 < sigma_cmb < 0.0586, f"{sigma_cmb:.4f} eV")
    check("alternate admission bypasses framework current-bank Omega_DM", "CMB-peak-derived `Ω_DM h²`" in note_text or "CMB peak `Ω_DM h²`" in note_text)

    print()
    print("D. Fan-out boundary")
    print("-" * 72)
    for phrase in (
        "Comparator only",
        "Structural only",
        "Alt admission surface",
        "Kinematic only",
        "Speculative",
    ):
        check(f"route status phrase present: {phrase}", phrase in note_text)
    check("source note preserves no-retention boundary", "not retain Σm_ν" in note_text or "does not claim numerical `Sigma m_nu` retention" in note_text)
    check("source note names research-level pivots", "research-level pivots" in note_text)

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: dependency packet exposed; F3 no-go remains honest and auditable.")
        return 0
    print("VERDICT: dependency repair checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
