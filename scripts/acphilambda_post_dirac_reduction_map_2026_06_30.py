#!/usr/bin/env python3
"""Verify the post-Dirac AC_phi_lambda reduction map.

This runner checks source wiring and overclaim hygiene. It deliberately does not
set audit status or edit the Tier-A registry.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs" / "ACPHILAMBDA_POST_DIRAC_REDUCTION_MAP_2026-06-30.md"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
AXIOM_NODES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
DIRAC_PATH = ROOT / "docs" / "DIRAC_DYNAMICS_UNLOCK_PATH_FROM_AXIOM_RESET_2026-06-30.md"
DIRAC_RUNNER = ROOT / "scripts" / "dirac_dynamics_unlock_path_from_axiom_reset_2026_06_30.py"
STRICT_NN = ROOT / "docs" / "STRICT_NN_COMPOSITION_FLUX_SELECTOR_BRIDGE_THEOREM_NOTE_2026-06-30.md"
OCCUPANCY = ROOT / "docs" / "ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md"
R_ETA = ROOT / "docs" / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
SPECIES = ROOT / "docs" / "ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md"
STATIC_R = ROOT / "docs" / "KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md"
KD_R_ONE = ROOT / "docs" / "KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md"
FLAVOR_PARENT = ROOT / "docs" / "FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def run_dirac_runner() -> str:
    proc = subprocess.run(
        [sys.executable, str(DIRAC_RUNNER)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return proc.stdout + proc.stderr


def main() -> int:
    print("=== AC_phi_lambda post-Dirac reduction map ===")

    paths = [
        NOTE,
        TIER_A,
        AXIOM_NODES,
        DIRAC_PATH,
        DIRAC_RUNNER,
        STRICT_NN,
        OCCUPANCY,
        R_ETA,
        SPECIES,
        STATIC_R,
        KD_R_ONE,
        FLAVOR_PARENT,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    tier_a = read(TIER_A)
    axiom_nodes = read(AXIOM_NODES)
    dirac_path = read(DIRAC_PATH)
    dirac_flat = flat(dirac_path)
    strict_nn = read(STRICT_NN)
    strict_flat = flat(strict_nn)
    occupancy = read(OCCUPANCY)
    occupancy_flat = flat(occupancy)
    r_eta = read(R_ETA)
    r_eta_flat = flat(r_eta)
    species = read(SPECIES)
    species_flat = flat(species)
    static_r = read(STATIC_R)
    static_flat = flat(static_r)
    kd_r_one = read(KD_R_ONE)
    kd_flat = flat(kd_r_one)
    flavor_parent = read(FLAVOR_PARENT)
    flavor_flat = flat(flavor_parent)

    print("\nPART A -- registry and primitive boundaries")
    check("Tier-A registry still has AC_phi_lambda", '"label": "AC_phi_lambda"' in tier_a)
    check("Tier-A registry still has theta", '"label": "theta"' in tier_a)
    check("AC_phi_lambda registry decomposition has three sub-admissions", "reading_occupancy_selection" in tier_a and "delta_readout_identification_R_eta" in tier_a and "species_bridge" in tier_a)
    check("axiom nodes register realized-state primitive", "realized_state_primitive" in axiom_nodes)
    check("axiom nodes register minimal axioms and kinetic-isotropy separately", "minimal_axioms" in axiom_nodes and "kinetic_isotropy_primitive" in axiom_nodes)

    print("\nPART B -- #4748 Dirac bridge moved the kinetic blocker")
    check("strict NN bridge states direct face-diagonal exclusion", "must not create a direct face-diagonal availability influence" in strict_flat)
    check("strict NN bridge derives anticommuting edge coefficients", "Gamma_mu Gamma_nu + Gamma_nu Gamma_mu = 0" in strict_nn)
    check("strict NN bridge selects flux(-1)", "flux `-1`" in strict_nn and "Kawamoto-Smit" in strict_nn)
    check("strict NN bridge preserves non-kinetic boundaries", "probability" in strict_nn and "theta" in strict_nn and "source/action" in strict_nn)
    dirac_output = run_dirac_runner()
    check("Dirac unlock runner still passes", "TOTAL: PASS=43 FAIL=0" in dirac_output)
    check("Dirac path names AC_phi_lambda as still open", "`AC_phi_lambda`" in dirac_path and "What Still Does Not Unlock" in dirac_path)
    check("Dirac path defines dynamics narrowly", "static spatial first-order Dirac/staggered kinetic spine" in dirac_flat)

    print("\nPART C -- old AC_phi_lambda residuals match this reduction")
    check("occupancy note splits value face from measure-side realization", "Value face = registration" in occupancy and "measure-side" in occupancy)
    check("occupancy note names first-order-vs-second-order frontier", "first-order-vs-second-order `det D`" in occupancy or "first-order/second-order `det D`" in occupancy)
    check("static r note leaves dynamical first-order opening", "remaining live opening is dynamical/first-order/index readout" in static_flat)
    check("static r note does not close dynamical gate", "r=1/2 is impossible" in static_flat and "dynamical" in static_flat)
    check("Kahler-Dirac note gives r=1 on explicit realization", "gives `r = |b|²/a² = 1`" in kd_r_one or "gives `r=1`" in kd_flat)
    check("Kahler-Dirac note leaves signed one-slot readout open", "signed / `U(1)_b` one-slot readout" in kd_r_one)
    check("R-eta note isolates A_R-eta", "A_R-eta" in r_eta and "identity-read in radians" in r_eta)
    check("R-eta note says not retired", "Sub-admission (ii) remains a Tier-A admission" in r_eta)
    check("species note names carrier-locus selection as structural residual", "carrier-locus selection" in species_flat)
    check("species note points next path at first-order chiral operator class", "forcing the first-order chiral operator class" in species_flat)
    check("flavor parent says hw=1 locus needs chiral operator class", "Carrier LOCUS = hw=1 triplet" in flavor_parent and "first-order chiral Dirac operator" in flavor_flat)

    print("\nPART D -- new reduction note content")
    check("note says kinetic shortage no longer carries AC_phi_lambda", "kinetic-order shortage no longer carries AC_phi_lambda" in note)
    check("note preserves no registry/status change", "does not set an audit verdict" in note_flat and "edit the Tier-A registry" in note_flat)
    check("note lists W_r", "W_r" in note and "signed/statistics one-slot readout" in note)
    check("note lists W_eta", "W_eta" in note and "A_R-eta" in note)
    check("note lists W_locus", "W_locus" in note and "hw=1 generation record-context" in note)
    check("note ranks AC(i) as next target", "next highest-leverage target is AC_phi_lambda sub-admission (i)" in note)
    check("note says R-eta unchanged", "R-eta Is Unchanged" in note)
    check("note says species bridge reduced not gone", "Species Bridge Is Reduced, Not Gone" in note)
    check("note names theta as later / less direct", "Theta's gauge-side winding account remains later and less directly moved" in note_flat)

    print("\nPART E -- overclaim and no-go discipline hygiene")
    check("note does not claim AC_phi_lambda retired", "claim AC_phi_lambda retirement" in note and "AC_phi_lambda is retired" not in note_flat)
    check("note uses partial narrowing claim type", "partial narrowing" in note)
    check("note includes N1 alternative routes", "N1 - Alternative Route Enumeration" in note and note.count("|") > 20)
    check("note includes N2 collapsed residual set", "N2 - Wall Independence" in note and "collapsed residual set" in note)
    check("note includes N3 hidden-wall scan", "N3 - Hidden-Wall Scan" in note)
    check("note includes N4 residual matching", "N4 - Residual Matching" in note)
    check("note includes N5 rhetoric audit", "N5 - Rhetoric Audit" in note)
    check("note includes N6 partial-closure paths", "N6 - Partial-Closure Path Scan" in note)
    check("note includes N7 steelman", "N7 - Steelman" in note)
    check("note includes N8 cross-cycle echo", "N8 - Cross-Cycle Echo" in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- AC_phi_lambda is narrowed post-Dirac; remaining atoms are explicit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
