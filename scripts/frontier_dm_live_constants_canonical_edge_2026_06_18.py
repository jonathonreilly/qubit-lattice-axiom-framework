#!/usr/bin/env python3
"""DM live constants canonical edge certificate.

This runner verifies a bounded source-side edge for the DM thermal helper
constants. It does not audit, retag, derive observed values, or close the DM
selector/completeness premise.
"""

from __future__ import annotations

import math
from pathlib import Path

from canonical_plaquette_surface import (
    CANONICAL_ALPHA_BARE,
    CANONICAL_ALPHA_LM,
    CANONICAL_ALPHA_S_V,
    CANONICAL_PLAQUETTE,
    CANONICAL_U0,
)
import dm_leptogenesis_exact_common as lep
from dm_full_closure_minimal_reduced_cycle_extension_map_common import (
    H_PARAM,
    omega_b_from_eta,
    plaquette_supported_alpha_short_distance,
)
from dm_full_closure_same_surface_thermal_support_common import (
    ALPHA_HI,
    ALPHA_LO,
    OMEGA_DM_OBS,
)


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "DM_LIVE_CONSTANTS_CANONICAL_EDGE_CERTIFICATE_NOTE_2026-06-18.md"
PARENT_DM_NOTE = ROOT / "docs" / "DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md"
CANONICAL_NOTE = ROOT / "docs" / "CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md"
PLAQUETTE_HELPER = ROOT / "scripts" / "canonical_plaquette_surface.py"
LEP_HELPER = ROOT / "scripts" / "dm_leptogenesis_exact_common.py"
MAP_HELPER = ROOT / "scripts" / "dm_full_closure_minimal_reduced_cycle_extension_map_common.py"
THERMAL_HELPER = ROOT / "scripts" / "dm_full_closure_same_surface_thermal_support_common.py"

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
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def compact(text: str) -> str:
    return " ".join(text.split())


def close(a: float, b: float, tol: float) -> bool:
    return abs(float(a) - float(b)) <= tol


def main() -> int:
    print("=" * 76)
    print("DM live constants canonical edge certificate")
    print("=" * 76)
    print("Claim boundary: bounded support for helper constant wiring only.")
    print("No audit verdict or effective status is changed by this runner.")

    print("\n" + "=" * 76)
    print("BLOCK 1: source surfaces")
    print("=" * 76)
    paths = (
        NOTE,
        PARENT_DM_NOTE,
        CANONICAL_NOTE,
        PLAQUETTE_HELPER,
        LEP_HELPER,
        MAP_HELPER,
        THERMAL_HELPER,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists(), "present" if path.exists() else "missing")

    note = read(NOTE)
    parent = read(PARENT_DM_NOTE)
    canonical = read(CANONICAL_NOTE)
    plaquette_helper = read(PLAQUETTE_HELPER)
    lep_helper = read(LEP_HELPER)
    map_helper = read(MAP_HELPER)
    thermal_helper = read(THERMAL_HELPER)
    note_flat = compact(note)
    parent_flat = compact(parent)
    canonical_flat = compact(canonical)

    print("\n" + "=" * 76)
    print("BLOCK 2: boundary and trace text")
    print("=" * 76)
    check("claim type is bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("status is bounded support only", "**Status:** bounded support only" in note)
    check("independent audit owns status", "Independent audit owns any effective status" in note)
    check("note forbids audit status mutation", "does not change an audit ledger" in note_flat)
    check("note says no new axiom", "No new axiom" in note)
    check("note does not derive plaquette value", "does not derive `CANONICAL_PLAQUETTE = 0.5934`" in note)
    check("note does not derive ETA/Omega observations", "does not derive `ETA_OBS` or `OMEGA_DM_OBS`" in note)
    check("note does not close selector authority", "does not close packet-completeness or selector authority" in note)
    check("note cites canonical certificate", "CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md" in note)
    check("note names parent DM theorem as trace target", "DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md" in note)
    check(
        "note avoids a markdown dependency edge back to parent",
        "](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md)" not in note,
    )
    check("note links source runner", "frontier_dm_live_constants_canonical_edge_2026_06_18.py" in note)
    check("parent records new constants edge certificate", "DM_LIVE_CONSTANTS_CANONICAL_EDGE_CERTIFICATE_NOTE_2026-06-18.md" in parent)
    check("parent preserves conditional boundary", "does not close the selector / packet-completeness premise" in parent_flat)
    check("canonical certificate keeps P underived", "does not derive the Wilson plaquette value" in canonical_flat)
    check("canonical certificate forbids physical coupling derivation", "physical coupling derivation" in canonical)

    print("\n" + "=" * 76)
    print("BLOCK 3: canonical plaquette arithmetic edge")
    print("=" * 76)
    p = CANONICAL_PLAQUETTE
    u0 = CANONICAL_U0
    alpha_bare = CANONICAL_ALPHA_BARE
    alpha_lm = CANONICAL_ALPHA_LM
    alpha_sv = CANONICAL_ALPHA_S_V
    c1 = math.pi**2 / 3.0
    p1 = 1.0 - c1 * alpha_bare
    alpha_hi_formula = -math.log(p1) / c1

    print(f"  P              = {p:.15f}")
    print(f"  u_0            = {u0:.15f}")
    print(f"  alpha_bare     = {alpha_bare:.15f}")
    print(f"  alpha_LM       = {alpha_lm:.15f}")
    print(f"  alpha_s(v)     = {alpha_sv:.15f}")
    print(f"  DM ALPHA_LO    = {ALPHA_LO:.15f}")
    print(f"  DM ALPHA_HI    = {ALPHA_HI:.15f}")

    check("P equals canonical 0.5934", close(p, 0.5934, 1.0e-15))
    check("u_0 equals P^(1/4)", close(u0, p**0.25, 1.0e-15))
    check("u_0^4 equals P", close(u0**4, p, 1.0e-15))
    check("alpha_bare equals 1/(4pi)", close(alpha_bare, 1.0 / (4.0 * math.pi), 1.0e-16))
    check("alpha_LM equals alpha_bare/u_0", close(alpha_lm, alpha_bare / u0, 1.0e-16))
    check("alpha_LM*u_0 equals alpha_bare", close(alpha_lm * u0, alpha_bare, 1.0e-16))
    check("alpha_s(v) equals alpha_bare/u_0^2", close(alpha_sv, alpha_bare / (u0**2), 1.0e-16))
    check("alpha_s(v)*u_0^2 equals alpha_bare", close(alpha_sv * (u0**2), alpha_bare, 1.0e-16))
    check("DM PLAQ_MC equals canonical P", close(lep.PLAQ_MC, p, 1.0e-15))
    check("DM u0 equals canonical u_0", close(lep.u0, u0, 1.0e-15))
    check("DM alpha_bare equals canonical alpha_bare", close(lep.alpha_bare, alpha_bare, 1.0e-16))
    check("DM ALPHA_LM equals canonical alpha_LM", close(lep.ALPHA_LM, alpha_lm, 1.0e-16))
    check("thermal ALPHA_LO equals canonical alpha_LM", close(ALPHA_LO, alpha_lm, 1.0e-16))
    check("short-distance p1 stays in logarithm domain", 0.0 < p1 < 1.0)
    check("thermal ALPHA_HI equals plaquette-supported formula", close(ALPHA_HI, alpha_hi_formula, 1.0e-16))
    check("helper function returns same ALPHA_HI", close(ALPHA_HI, plaquette_supported_alpha_short_distance(), 1.0e-16))
    check("thermal endpoint interval has positive width", ALPHA_HI > ALPHA_LO)
    check("plaquette helper contains canonical constant", "CANONICAL_PLAQUETTE = 0.5934" in plaquette_helper)
    check("leptogenesis helper contains PLAQ_MC constant", "PLAQ_MC = 0.5934" in lep_helper)
    check("thermal helper imports CANONICAL_ALPHA_LM", "from canonical_plaquette_surface import CANONICAL_ALPHA_LM" in thermal_helper)
    check("map helper imports CANONICAL_ALPHA_BARE", "from canonical_plaquette_surface import CANONICAL_ALPHA_BARE" in map_helper)

    print("\n" + "=" * 76)
    print("BLOCK 4: eta/Omega observed-input bookkeeping")
    print("=" * 76)
    eta = lep.ETA_OBS
    omega_b_h2 = 3.6515e-3 * (eta / 1.0e-10)
    omega_b = omega_b_from_eta(eta)
    ratio = OMEGA_DM_OBS / omega_b

    print(f"  ETA_OBS        = {eta:.15e}")
    print(f"  Omega_b h^2    = {omega_b_h2:.15f}")
    print(f"  H_PARAM        = {H_PARAM:.15f}")
    print(f"  Omega_b        = {omega_b:.15f}")
    print(f"  OMEGA_DM_OBS   = {OMEGA_DM_OBS:.15f}")
    print(f"  Omega_DM/Omega_b = {ratio:.15f}")

    check("ETA_OBS equals supplied observed comparator", close(eta, 6.12e-10, 1.0e-24))
    check("OMEGA_DM_OBS equals supplied observed comparator", close(OMEGA_DM_OBS, 0.268, 1.0e-15))
    check("H_PARAM equals helper value", close(H_PARAM, 0.674, 1.0e-15))
    check("Omega_b h^2 arithmetic matches displayed formula", close(omega_b_h2, 0.02234718, 1.0e-14))
    check("omega_b_from_eta divides by H_PARAM^2", close(omega_b, omega_b_h2 / (H_PARAM**2), 1.0e-16))
    check("Omega_DM/Omega_b arithmetic matches displayed value", close(ratio, 5.447934280745940, 5.0e-15))
    check("target ratio is finite and positive", math.isfinite(ratio) and ratio > 0.0)
    check("eta helper source exposes ETA_OBS", "ETA_OBS = 6.12e-10" in lep_helper)
    check("thermal helper source exposes OMEGA_DM_OBS", "OMEGA_DM_OBS = 0.268" in thermal_helper)

    print("\n" + "=" * 76)
    print("BLOCK 5: falsifiers and firewalls")
    print("=" * 76)
    perturbed_p = p + 1.0e-4
    perturbed_alpha_lm = alpha_bare / (perturbed_p**0.25)
    perturbed_eta = eta * (1.0 + 1.0e-3)
    check("perturbing P changes alpha_LM", abs(perturbed_alpha_lm - alpha_lm) > 1.0e-6)
    check("perturbing ETA_OBS changes Omega_b", abs(omega_b_from_eta(perturbed_eta) - omega_b) > 1.0e-5)
    check("ALPHA_LO is not alpha_bare", abs(ALPHA_LO - alpha_bare) > 1.0e-2)
    check("ALPHA_LO is not alpha_s(v)", abs(ALPHA_LO - alpha_sv) > 1.0e-2)
    check("note keeps observed constants supplied", "remain observed inputs, not framework derivations" in note_flat)
    audit_tree = ROOT / "docs" / "audit"
    check("declared source surfaces avoid protected audit tree", all(audit_tree not in path.parents for path in paths))

    print("\n" + "=" * 76)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 76)
    print("\nRESULT:")
    print("  DM live-constant edge certificate is complete iff FAIL=0.")
    print("  Parent DM closure still needs selector/completeness authority and audit.")

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
