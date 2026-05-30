#!/usr/bin/env python3
"""Dependency-edge repair runner for the Sigma m_nu F3 fan-out synthesis.

The prior audit asked for direct source rows for the Cycle-1 DM cross-bound,
T-4F-alpha-2, current-bank Omega_DM, Lane 5 C1 status, and
eta/leptogenesis status. This runner checks that the source note exposes
those rows and recomputes the decisive Sigma m_nu arithmetic. It does not
apply or trust generated audit status.
"""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

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

    print()
    print("A. Source packet")
    print("-" * 72)
    check("source note exists", note.exists(), str(note.relative_to(ROOT)))
    check("source note declares no_go", "**Claim type:** no_go" in note_text and "**Type:** no_go" in note_text)
    check("source note has no branch-local status authority", "Status authority" not in note_text)
    check("source note has no branch provenance", "**Provenance:**" not in note_text)
    for label, filename in authority_files.items():
        path = DOCS / filename
        check(f"{label} source exists", path.exists(), str(path.relative_to(ROOT)))
        check(f"{label} source is directly cited", filename in note_text)

    print()
    print("B. Cross-bound arithmetic")
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
    print("C. Fan-out boundary")
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
    check("no-go discipline N1-N8 present", all(f"**N{i}" in note_text for i in range(1, 9)))

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: source packet exposed; F3 no-go remains bounded and auditable.")
        return 0
    print("VERDICT: dependency repair checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
