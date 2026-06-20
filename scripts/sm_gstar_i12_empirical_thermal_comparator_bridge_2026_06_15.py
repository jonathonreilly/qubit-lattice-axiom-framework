#!/usr/bin/env python3
"""Companion bridge for SM gstar I12 empirical/thermal comparators."""

from __future__ import annotations

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/SM_GSTAR_I12_EMPIRICAL_THERMAL_COMPARATOR_BRIDGE_BOUNDED_NOTE_2026-06-15.md"
PARENT = ROOT / "docs/SM_GSTAR_I12_NUR_THERMAL_EXCLUSION_BOUNDED_NOTE_2026-05-29.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{tag}: {label}{suffix}")


GSTAR = 427.0 / 4.0
MPL_GEV = 1.22e19
H_PREF = 1.66
HVEV_GEV = 174.0
EV_TO_GEV = 1.0e-9


def y_from_mnu(mnu_ev: float) -> float:
    return (mnu_ev * EV_TO_GEV) / HVEV_GEV


def y_threshold(temp_gev: float) -> float:
    return math.sqrt(H_PREF * math.sqrt(GSTAR) * temp_gev / MPL_GEV)


def gamma_over_h(y_nu: float, temp_gev: float) -> float:
    return y_nu * y_nu * MPL_GEV / (H_PREF * math.sqrt(GSTAR) * temp_gev)


def gamma_over_h_with_enhancement(y_nu: float, temp_gev: float, enhancement: float) -> float:
    return enhancement * gamma_over_h(y_nu, temp_gev)


def y_threshold_with_enhancement(temp_gev: float, enhancement: float) -> float:
    return y_threshold(temp_gev) / math.sqrt(enhancement)


def mass_from_y(y_nu: float) -> float:
    return y_nu * HVEV_GEV / EV_TO_GEV


def main() -> int:
    note = NOTE.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8")
    flat = " ".join(note.split())

    print("SM GSTAR I12 EMPIRICAL THERMAL COMPARATOR BRIDGE")

    required_note_phrases = [
        "Actual current-surface status:** conditional-support arithmetic over explicit",
        "Trace class:** upstream_support",
        "Proposal allowed:** false",
        "Bare retained allowed:** false",
        "2026-06-18 Audit-Scope Repair",
        "the row to be narrowed to pure arithmetic over explicit declared comparator",
        "This source repair takes the second path",
        "None of these comparator premises is derived here",
        "not Tier-A admissions",
        "framework primitives",
        "conditional arithmetic over declared empirical m_nu and thermal-rate",
        "declared empirical small-neutrino-mass comparator",
        "Gamma_nuR ~ y_nu^2 T",
        "H ~ 1.66 sqrt(g_*) T^2 / M_Pl",
        "not a framework-native derivation",
        "does not derive small neutrino mass",
        "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md",
        "`0.6 eV` edge remains more than three decades below it",
        "new approved framework primitive",
        "prefactor-robustness repair",
        "E = c_Gamma / c_H",
        "Gamma_nuR/H < 1e-3",
        "m_nu > 20 eV",
        "new axiom",
    ]
    for phrase in required_note_phrases:
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    # 2026-06-20 narrowing: the row is pure arithmetic over EXPLICITLY ADMITTED
    # premises. These checks verify the note labels the empirical m_nu comparator
    # value and the thermalization estimate as ADMITTED inputs (not derived, not
    # retained) and marks the bridge to retained authority as OPEN.
    required_narrowing_phrases = [
        "2026-06-20 Audit-Scope Repair (pure-arithmetic narrowing)",
        "narrow the row to pure arithmetic over explicitly admitted premises",
        "narrowed to pure arithmetic over explicitly ADMITTED",
        "ADMITTED-1  (empirical m_nu comparator value)",
        "ADMITTED-3  (thermalization estimate)",
        "ADMITTED-4  (radiation-era expansion estimate)",
        "ADMITTED inputs to this packet",
        "not derived here",
        "not retained authorities",
        "not Tier-A admissions",
        "not accepted premise nodes",
        "Bridge to retained authority: OPEN",
        "does **not** supply retained authority",
        "Closing that bridge",
        "is left open",
    ]
    for phrase in required_narrowing_phrases:
        check(f"note contains 2026-06-20 narrowing phrase: {phrase}", phrase in note)

    # The bridge row is now scoped to its own admitted premises, not to the
    # parent's conclusion. We require only that the parent still EXISTS and names
    # the same admitted inputs this packet isolates (the m_nu comparator and the
    # Gamma_nuR estimate). The parent's g_* conclusion is NOT a load-bearing
    # input to this pure-arithmetic row, so it is no longer asserted here.
    check("parent exists and is non-empty", len(parent) > 0)
    required_parent_premise_phrases = [
        "empirical small `m_nu`",
        "Gamma_nu_R  ~  y_nu^2  T",
    ]
    for phrase in required_parent_premise_phrases:
        check(f"parent names shared admitted premise: {phrase}", phrase in parent)

    y_005 = y_from_mnu(0.05)
    y_01 = y_from_mnu(0.1)
    y_06 = y_from_mnu(0.6)
    check("0.05 eV gives y_nu between 2e-13 and 4e-13", 2e-13 < y_005 < 4e-13, f"{y_005:.3e}")
    check("0.1 eV gives y_nu between 5e-13 and 7e-13", 5e-13 < y_01 < 7e-13, f"{y_01:.3e}")
    check("0.6 eV generous edge stays below 4e-12", y_06 < 4e-12, f"{y_06:.3e}")

    y_thr_100 = y_threshold(100.0)
    y_thr_1e9 = y_threshold(1.0e9)
    y_thr_1e12 = y_threshold(1.0e12)
    check("T=100 GeV threshold is order 1e-8", 1e-8 < y_thr_100 < 2e-8, f"{y_thr_100:.3e}")
    check("threshold rises with temperature through 1e12 GeV", y_thr_100 < y_thr_1e9 < y_thr_1e12)
    check("T=1e9 GeV threshold is order 1e-5", 2e-5 < y_thr_1e9 < 6e-5, f"{y_thr_1e9:.3e}")
    check("T=1e12 GeV threshold is order 1e-3", 8e-4 < y_thr_1e12 < 2e-3, f"{y_thr_1e12:.3e}")

    ratio_01_100 = gamma_over_h(y_01, 100.0)
    ratio_06_100 = gamma_over_h(y_06, 100.0)
    check("0.1 eV comparator gives Gamma/H << 1 at 100 GeV", ratio_01_100 < 1e-8, f"{ratio_01_100:.3e}")
    check("0.6 eV generous edge still gives Gamma/H << 1 at 100 GeV", ratio_06_100 < 1e-6, f"{ratio_06_100:.3e}")

    decades_01 = math.log10(y_thr_100 / y_01)
    decades_06 = math.log10(y_thr_100 / y_06)
    check("0.1 eV comparator is more than four decades below threshold", decades_01 > 4.0, f"{decades_01:.2f}")
    check("0.6 eV generous edge is more than three decades below threshold", decades_06 > 3.0, f"{decades_06:.2f}")

    m_required_ev = mass_from_y(y_thr_100)
    check("thermalization at 100 GeV implies m_nu above 1 keV", m_required_ev > 1e3, f"{m_required_ev:.3e} eV")
    check("thermalization at 100 GeV is above 0.6 eV comparator by > 1000x", m_required_ev / 0.6 > 1000)

    masses_ev = [0.05, 0.1, 0.6]
    temps_gev = [100.0, 1.0e9, 1.0e12]
    enhancements = [1.0e-4, 1.0e-2, 1.0, 1.0e2, 1.0e4]
    worst = max(
        (gamma_over_h_with_enhancement(y_from_mnu(m), t, e), m, t, e)
        for m in masses_ev
        for t in temps_gev
        for e in enhancements
    )
    check(
        "prefactor grid has 3 masses x 3 temperatures x 5 enhancements = 45 cases",
        len(masses_ev) * len(temps_gev) * len(enhancements) == 45,
    )
    check(
        "all prefactor-grid cases remain out of equilibrium (Gamma/H < 1)",
        worst[0] < 1.0,
        f"worst={worst[0]:.3e} at m={worst[1]} eV, T={worst[2]:.3e} GeV, E={worst[3]:.1e}",
    )
    check(
        "hostile E=1e4 at 0.6 eV, 100 GeV still has Gamma/H < 1e-3",
        gamma_over_h_with_enhancement(y_06, 100.0, 1.0e4) < 1.0e-3,
        f"{gamma_over_h_with_enhancement(y_06, 100.0, 1.0e4):.3e}",
    )
    y_thr_100_e4 = y_threshold_with_enhancement(100.0, 1.0e4)
    m_required_100_e4 = mass_from_y(y_thr_100_e4)
    check(
        "hostile E=1e4 thermalization at 100 GeV still implies m_nu > 20 eV",
        m_required_100_e4 > 20.0,
        f"{m_required_100_e4:.3e} eV",
    )
    check(
        "hostile E=1e4 thermalization mass remains >30x the 0.6 eV generous edge",
        m_required_100_e4 / 0.6 > 30.0,
        f"{m_required_100_e4 / 0.6:.2f}x",
    )
    check(
        "central 0.1 eV branch survives even E=1e8 at 100 GeV",
        gamma_over_h_with_enhancement(y_01, 100.0, 1.0e8) < 1.0,
        f"{gamma_over_h_with_enhancement(y_01, 100.0, 1.0e8):.3e}",
    )
    check(
        "temperature monotonicity makes 100 GeV the most lenient point for every enhancement",
        all(
            gamma_over_h_with_enhancement(y_from_mnu(m), 100.0, e)
            > gamma_over_h_with_enhancement(y_from_mnu(m), 1.0e9, e)
            > gamma_over_h_with_enhancement(y_from_mnu(m), 1.0e12, e)
            for m in masses_ev
            for e in enhancements
        ),
    )
    check(
        "exact 1.66/rate prefactors are not decisive inside the E<=1e4 robustness box",
        "exact `1.66`, exact rate prefactor" in flat and "E = c_Gamma / c_H" in flat,
    )

    check("note does not claim audit-retained status", "audit-retained" not in flat)
    check("note does not allow bare retained wording", "Bare retained allowed:** false" in note)
    check("note marks the arithmetic as conditional-support", "conditional-support arithmetic" in flat)
    check("note keeps small mnu derivation excluded", "derive the small neutrino mass" in flat and "does **not**" in flat)
    check("note keeps thermal-rate derivation excluded", "derive the Boltzmann collision operator" in flat and "does **not**" in flat)
    check("downstream citation rule prevents retained authority use", "must not cite it as retained authority" in flat)
    check("note denies new axiom", "new axiom" in flat)

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: bounded comparator bridge failed")
        return 1
    print("VERDICT: bounded comparator bridge passes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
