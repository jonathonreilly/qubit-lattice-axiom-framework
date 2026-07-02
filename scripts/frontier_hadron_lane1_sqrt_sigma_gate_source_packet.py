#!/usr/bin/env python3
"""Source-packet verifier for the Lane 1 sqrt(sigma) retention gate.

This runner is intentionally not an audit verdict and not a promotion of the
parent row.  It verifies the source-side packet requested by the conditional
audit: registered dependencies, replayable budget arithmetic, and an honest
B2/B5 open-gate boundary for the current repo surface.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0

PARENT = "docs/HADRON_LANE1_SQRT_SIGMA_RETENTION_GATE_AUDIT_SUPPORT_NOTE_2026-04-27.md"
RUNNER = "scripts/frontier_hadron_lane1_sqrt_sigma_gate_source_packet.py"
CACHE = "logs/runner-cache/frontier_hadron_lane1_sqrt_sigma_gate_source_packet.txt"

DEPENDENCIES = {
    "confinement_string_tension_note": "docs/CONFINEMENT_STRING_TENSION_NOTE.md",
    "alpha_s_derived_note": "docs/ALPHA_S_DERIVED_NOTE.md",
    "hadron_mass_lane1_theorem_plan_support_note_2026-04-27": (
        "docs/HADRON_MASS_LANE1_THEOREM_PLAN_SUPPORT_NOTE_2026-04-27.md"
    ),
    "minimal_axioms": "docs/MINIMAL_AXIOMS_2026-06-05.md",
}

SIBLING_BOUNDARIES = {
    "b2_gate_repair": "docs/HADRON_LANE1_SQRT_SIGMA_B2_GATE_REPAIR_AUDIT_NOTE_2026-04-30.md",
    "b2_static_energy_bridge": (
        "docs/HADRON_LANE1_SQRT_SIGMA_B2_STATIC_ENERGY_BRIDGE_SCOUT_NOTE_2026-04-30.md"
    ),
    "b5_framework_link": "docs/HADRON_LANE1_SQRT_SIGMA_B5_FRAMEWORK_LINK_AUDIT_NOTE_2026-04-30.md",
}

# Method-2 bridge constants as stated in CONFINEMENT_STRING_TENSION_NOTE.md.
R0_FM = 0.472
R0_OVER_A = 5.37
SIGMA_A2_QUENCHED = 0.0465
HBARC_MEV_FM = 197.327
ROUGH_SCREENING_FACTOR = 0.96
NOTE_CENTRAL_MEV = 465.0
PDG_COMPARATOR_MEV = 440.0
PDG_COMPARATOR_SIGMA_MEV = 20.0
ALPHA_PRECISION_FRACTION = 0.002
ALPHA_SENSITIVITY = 6.0


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return condition


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def sqrt_sigma_quenched_mev() -> float:
    a_fm = R0_FM / R0_OVER_A
    return math.sqrt(SIGMA_A2_QUENCHED) / a_fm * HBARC_MEV_FM


def part1_packet_metadata() -> None:
    section("Part 1: parent source-packet metadata")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    check("parent note exists", (ROOT / PARENT).exists(), PARENT)
    check("parent declares this primary runner", RUNNER in parent)
    check("parent declares this runner cache", CACHE in parent)
    check(
        "parent remains support/open-gate, not a theorem promotion",
        "support / open-lane gate-audit note" in parent_norm
        and "no theorem or claim promotion" in parent_norm,
    )
    check(
        "parent boundary refuses sqrt(sigma) promotion",
        "not promote `sqrt(sigma)` from bounded to retained" in parent
        and "the retention promotion must close" in parent,
    )


def part2_registered_dependencies() -> None:
    section("Part 2: dependency links and fingerprints")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    for claim_id, rel in DEPENDENCIES.items():
        check(f"{claim_id}: linked from parent", f"[{claim_id}](" in parent and Path(rel).name in parent)
        check(f"{claim_id}: file exists", (ROOT / rel).exists(), rel)

    conf = read(DEPENDENCIES["confinement_string_tension_note"])
    conf_ascii = (
        conf.replace("\u03b2", "beta")
        .replace("\u2080", "0")
        .replace("\u03c3", "sigma")
    )
    alpha = read(DEPENDENCIES["alpha_s_derived_note"])
    plan = read(DEPENDENCIES["hadron_mass_lane1_theorem_plan_support_note_2026-04-27"])
    axioms = read(DEPENDENCIES["minimal_axioms"])

    check(
        "confinement dependency supplies beta=6 and bounded Method 2 constants",
        "g_bare = 1" in conf_ascii
        and "beta = 6.0" in conf_ascii
        and "r0/a = 5.37" in conf_ascii
        and "0.0465" in conf_ascii,
    )
    check(
        "confinement dependency marks standard lattice inputs as bounded",
        "standard lattice QCD simulations" in conf
        and "bounded through this identification" in conf,
    )
    check(
        "alpha_s dependency exposes alpha_s(M_Z) arithmetic",
        "alpha_s(M_Z) = 0.118067 ~ 0.1181" in alpha
        and "Primary runner" in alpha,
    )
    check(
        "Lane 1 roadmap names target 3E sqrt(sigma) promotion gates",
        "Target 3E" in plan
        and "sqrt(sigma)" in plan
        and "Screening-correction budget" in plan,
    )
    check(
        "minimal axiom note uses current Lattice/Quantum/Record authority",
        "Date:** 2026-06-05" in axioms
        and "Lattice" in axioms
        and "Quantum" in axioms
        and "Record" in axioms,
    )
    check(
        "minimal axiom note chain-satisfies without sourcing bounded status",
        "chain-satisfy without making downstream rows" in normalize(axioms)
        and "must not be treated as a source of bounded status" in normalize(axioms),
    )
    check(
        "parent prose names the four dependency authorities",
        all(Path(rel).name in parent_norm for rel in DEPENDENCIES.values()),
    )


def part3_budget_arithmetic() -> None:
    section("Part 3: replayed residual-budget arithmetic")
    quenched = sqrt_sigma_quenched_mev()
    screened = quenched * ROUGH_SCREENING_FACTOR
    central_gap = (NOTE_CENTRAL_MEV - PDG_COMPARATOR_MEV) / PDG_COMPARATOR_MEV
    alpha_budget = ALPHA_SENSITIVITY * ALPHA_PRECISION_FRACTION
    comparator_factor = PDG_COMPARATOR_MEV / quenched
    comparator_low = (PDG_COMPARATOR_MEV - PDG_COMPARATOR_SIGMA_MEV) / quenched
    comparator_high = (PDG_COMPARATOR_MEV + PDG_COMPARATOR_SIGMA_MEV) / quenched

    print(f"  sqrt(sigma)_quenched(Method 2) = {quenched:.2f} MeV")
    print(f"  rough x0.96 screened value     = {screened:.2f} MeV")
    print(f"  note central gap vs 440 MeV     = {100.0 * central_gap:.2f}%")
    print(f"  alpha precision budget          = {100.0 * alpha_budget:.2f}%")
    print(f"  PDG central factor vs quenched   = {comparator_factor:.4f}")
    print(f"  PDG one-sigma factor band        = [{comparator_low:.4f}, {comparator_high:.4f}]")

    check("Method 2 replay gives the recorded quenched scale", abs(quenched - 484.0) < 1.0)
    check("rough screening replay gives the recorded 465 MeV scale", abs(screened - NOTE_CENTRAL_MEV) < 1.0)
    check("central-value gap is the note's approximately 5.6 percent gap", 0.055 < central_gap < 0.058)
    check("alpha_s precision propagation is about 1.2 percent", abs(alpha_budget - 0.012) < 1e-12)
    check("rough x0.96 remains outside the one-sigma central-factor band", ROUGH_SCREENING_FACTOR > comparator_high)


def part4_b2_b5_gate_model() -> None:
    section("Part 4: B2/B5 retention-gate checks")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    b2_open = (
        "B2" in parent
        and "proper `N_f = 2+1` lattice" in parent
        and "rough x0.96" in parent.replace("\u00d7", "x")
        and "dominant residual" in parent
    )
    b5_open = (
        "B5" in parent
        and "Framework `SU(3)`" in parent
        and "standard `SU(3) YM` identification" in parent
        and "unquantified" in parent
    )
    b3_b4_absorbed = "B3" in parent and "absorbed into the choice of Method 2" in parent_norm
    b1_precision = "B1" in parent and "retained-input precision residual" in parent_norm

    check("B1 is classified as precision propagation", b1_precision)
    check("B2 is named as the dominant open dynamical-screening residual", b2_open)
    check("B3/B4 are methodological, not the load-bearing current residual", b3_b4_absorbed)
    check("B5 is named as the open framework-to-standard-QCD bridge", b5_open)
    check(
        "parent states promotion is gated on B2 plus the B5 bridge budget",
        "gated on (B2) plus a declared (B5) structural bridge budget" in parent,
    )


def part5_existing_boundary_artifacts() -> None:
    section("Part 5: existing sibling boundary artifacts stay non-promotional")
    for name, rel in SIBLING_BOUNDARIES.items():
        check(f"{name}: file exists", (ROOT / rel).exists(), rel)

    b2 = read(SIBLING_BOUNDARIES["b2_gate_repair"])
    static = read(SIBLING_BOUNDARIES["b2_static_energy_bridge"])
    b5 = read(SIBLING_BOUNDARIES["b5_framework_link"])

    check(
        "B2 gate repair forbids rough-factor promotion",
        "rough x0.96" in b2 and "cannot promote" in b2,
    )
    check(
        "static-energy bridge states current-surface no-go",
        "current-surface no-go" in static and "not promote" in static,
    )
    check(
        "B5 framework-link artifact keeps B5 open on current surface",
        "current-surface no-go" in b5 and "not close B5" in b5,
    )


def main() -> int:
    print("=" * 88)
    print("LANE 1 SQRT(SIGMA) RETENTION-GATE SOURCE PACKET")
    print("=" * 88)
    print()
    print("Question:")
    print("  Is the parent sqrt(sigma) gate row now packaged with dependency")
    print("  links and a replayable budget/source verifier for independent re-audit?")
    print()
    print("Answer:")
    print("  Yes for re-audit readiness. No retained promotion is made here;")
    print("  B2 dynamical screening and B5 framework-to-standard-QCD linkage")
    print("  remain explicit gates on the current repo surface.")

    part1_packet_metadata()
    part2_registered_dependencies()
    part3_budget_arithmetic()
    part4_b2_b5_gate_model()
    part5_existing_boundary_artifacts()

    print()
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
