#!/usr/bin/env python3
"""Verifier for the physical electron mass current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply the retained physical-unit electron mass needed by the
zero-import hydrogen static-source Rydberg lane. It preserves the positive
contract route and does not derive m_e, alpha(0), Rydberg, or hydrogen.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
ELECTRON_MASS_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
BRIDGE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
NATIVE_BRIDGE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SPECIES_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SPECIES_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SCALE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
BRANCH_MASS_MAP_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md"
BRANCH_MASS_MAP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md"
BRANNEN_OPEN_GATE = ROOT / "docs" / "LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
SCALE_REFERENCE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"

ELECTRON_MASS_INPUTS = {
    "PHYSICAL_ELECTRON_MASS_TEXT_LOCK",
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
    "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
    "NO_LEPTON_COMPARATOR_PROOF_INPUT",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

STATIC_SOURCE_REQUIRED = {
    "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
    "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
    "ATOMIC_OPERATOR_HARNESS_VERIFIED",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
    "AUDIT_ACCEPTANCE",
}


class Audit:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.pass_count += 1
            prefix = "PASS"
        else:
            self.fail_count += 1
            prefix = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"{prefix}: {label}{suffix}")

    def summary(self) -> None:
        print(f"\nSUMMARY: PASS={self.pass_count} FAIL={self.fail_count}")
        if self.fail_count:
            raise SystemExit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def all_subsets(items: set[str]) -> list[set[str]]:
    ordered = sorted(items)
    subsets: list[set[str]] = []
    for size in range(len(ordered) + 1):
        for combo in combinations(ordered, size):
            subsets.append(set(combo))
    return subsets


def closes_electron_mass(inputs: set[str]) -> bool:
    return ELECTRON_MASS_INPUTS <= inputs


def closes_static_source_rydberg(inputs: set[str]) -> bool:
    return STATIC_SOURCE_REQUIRED <= inputs


def branch_ratio(k: int, delta: float) -> float:
    return 1.0 + math.sqrt(2.0) * math.cos(delta + 2.0 * math.pi * k / 3.0)


def branch_ratios(delta: float) -> list[float]:
    return [branch_ratio(k, delta) for k in range(3)]


def koide_q(delta: float) -> float:
    roots = branch_ratios(delta)
    return sum(r * r for r in roots) / (sum(roots) ** 2)


def rho_e(delta: float) -> float:
    return min(r * r for r in branch_ratios(delta))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        STATIC_TARGET,
        KOIDE_FIREWALL,
        ELECTRON_MASS_PACKET,
        BRIDGE_DECISION,
        NATIVE_BRIDGE_NO_GO,
        SPECIES_DECISION,
        SPECIES_NO_GO,
        SCALE_DECISION,
        BRANCH_MASS_MAP_DECISION,
        BRANCH_MASS_MAP_NO_GO,
        BRANNEN_OPEN_GATE,
        LEPTON_SCALE,
        SCALE_REFERENCE,
        REGISTRY,
        TIER_A_REGISTRY,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required note content")
    required_phrases = [
        "Physical Electron Mass Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not ratify the physical electron",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "PHYSICAL_ELECTRON_READOUT_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "PHYSICAL_ELECTRON_MASS_TEXT_LOCK",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "native bridge target remains needed",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "species bridge target remains needed",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "KOIDE_BRANCH_MASS_MAP_RETAINED",
        "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
        "NO_LEPTON_COMPARATOR_PROOF_INPUT",
        "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "r_k(delta) = 1 + sqrt(2) cos(delta + 2 pi k / 3)",
        "rho_e(delta) = min_k r_k(delta)^2",
        "m_e = a_l^2 * rho_e(delta)",
        "delta = 2/9",
        "rho_e(delta) = 0.001628115093",
        "electron_mass_primitive",
        "physical_electron_readout_primitive",
        "koide_branch_mass_map_primitive",
        "native_zero_section_bridge_primitive",
        "physical_electron_species_primitive",
        "absolute_charged_lepton_scale_primitive",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
        "No-Go Discipline Gate",
        "broad physical-electron-mass no-go fails; narrowed",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Electron-mass predicate checks")
    full_inputs = set(ELECTRON_MASS_INPUTS)
    audit.check("full electron-mass contract accepts retained handoff", closes_electron_mass(full_inputs))
    for missing in sorted(ELECTRON_MASS_INPUTS):
        reduced = set(ELECTRON_MASS_INPUTS)
        reduced.remove(missing)
        audit.check(f"electron-mass handoff fails without {missing}", not closes_electron_mass(reduced))
    accepted_subsets = [subset for subset in all_subsets(ELECTRON_MASS_INPUTS) if closes_electron_mass(subset)]
    audit.check("only full electron-mass subset closes handoff", accepted_subsets == [full_inputs])
    current_surface = {
        "PHYSICAL_ELECTRON_MASS_TEXT_LOCK",
        "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
        "NO_LEPTON_COMPARATOR_PROOF_INPUT",
        "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    }
    audit.check(
        "current surface without bridge/species/scale/map inputs does not close electron mass",
        not closes_electron_mass(current_surface),
    )
    audit.check(
        "retained electron mass alone does not close static-source Rydberg",
        not closes_static_source_rydberg({"RETAINED_ELECTRON_MASS_PHYSICAL_UNIT"}),
    )
    audit.check(
        "full static-source predicate still needs more than m_e",
        closes_static_source_rydberg(set(STATIC_SOURCE_REQUIRED)),
    )

    section("Finite Koide target arithmetic checks")
    delta = 2.0 / 9.0
    roots = sorted(branch_ratios(delta))
    expected_roots = [
        0.04034990821920668,
        0.5802119201475365,
        2.3794381716332564,
    ]
    for got, expected, label in zip(roots, expected_roots, ["electron-like", "muon-like", "tau-like"]):
        audit.check(f"delta=2/9 sorted {label} root ratio reproduced", abs(got - expected) < 1e-14, f"{got:.15f}")
    rho_delta = rho_e(delta)
    audit.check("delta=2/9 electron factor reproduced", abs(rho_delta - expected_roots[0] ** 2) < 1e-16, f"{rho_delta:.15f}")
    for test_delta in [delta, 0.0, 0.5, 1.0, 3.0 * math.pi / 4.0]:
        audit.check(
            f"Koide Q is 2/3 at delta={test_delta:.6f}",
            abs(koide_q(test_delta) - 2.0 / 3.0) < 1e-14,
            f"Q={koide_q(test_delta):.15f}",
        )
    audit.check("delta=0 same Q but larger smallest squared branch", rho_e(0.0) / rho_delta > 50.0)
    audit.check("delta=3*pi/4 has massless branch edge", rho_e(3.0 * math.pi / 4.0) < 1e-28)
    scale = 313.841126
    mass_a = scale * rho_delta
    mass_b = 1.01 * scale * rho_delta
    audit.check("scale and branch factor compose by multiplication", abs(mass_b / mass_a - 1.01) < 1e-14)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    static_target = read(STATIC_TARGET)
    koide_firewall = read(KOIDE_FIREWALL)
    electron_packet = read(ELECTRON_MASS_PACKET)
    bridge_decision = read(BRIDGE_DECISION)
    native_bridge_no_go = read(NATIVE_BRIDGE_NO_GO)
    species_decision = read(SPECIES_DECISION)
    species_no_go = read(SPECIES_NO_GO)
    scale_decision = read(SCALE_DECISION)
    branch_decision = read(BRANCH_MASS_MAP_DECISION)
    branch_no_go = read(BRANCH_MASS_MAP_NO_GO)
    brannen_open_gate = read(BRANNEN_OPEN_GATE)
    lepton_scale = read(LEPTON_SCALE)
    scale_reference = flat(read(SCALE_REFERENCE)).lower()
    registry = json.loads(read(REGISTRY))
    tier_a = read(TIER_A_REGISTRY)
    nodes = registry["nodes"]

    audit.check("goal packet references physical electron mass no-go", NOTE.name in goal and "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in goal)
    audit.check("static target references physical electron mass no-go", NOTE.name in static_target and "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in static_target)
    audit.check("Koide firewall references physical electron mass no-go", NOTE.name in koide_firewall and "PHYSICAL_ELECTRON_READOUT_RETAINED" in koide_firewall)
    audit.check("electron mass packet references current-surface no-go", NOTE.name in electron_packet and "current retained, primitive, and open-PR surfaces do not" in electron_packet)
    audit.check("native bridge packet remains bridge only", "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in bridge_decision and "does not derive `m_e`" in bridge_decision)
    audit.check("physical electron no-go references native no-go", NATIVE_BRIDGE_NO_GO.name in note and "native bridge target remains needed" in note)
    audit.check(
        "native no-go keeps bridge open",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in native_bridge_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in native_bridge_no_go,
    )
    audit.check("species packet remains K3 only", "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in species_decision and "K3 support only" in species_decision)
    audit.check("physical electron no-go references species no-go", SPECIES_NO_GO.name in note and "species bridge target remains needed" in note)
    audit.check(
        "species no-go keeps K3 open",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in species_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in species_no_go,
    )
    audit.check("scale packet remains K4 only", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in scale_decision and "K4 support only" in scale_decision)
    audit.check("branch mass-map packet remains map only", "KOIDE_BRANCH_MASS_MAP_RETAINED" in branch_decision and "does not derive a physical electron mass" in branch_decision)
    audit.check("branch mass-map no-go keeps map open", "KOIDE_BRANCH_MASS_MAP_RETAINED" in branch_no_go and "SQUARE_ROOT_MASS_READOUT_RETAINED" in branch_no_go)
    audit.check("Brannen open gate excludes phase and scale derivation", "does not derive the Brannen phase" in brannen_open_gate and "dimensionful mass scale" in brannen_open_gate)
    audit.check("lepton-scale probe keeps scale gate open", "1/256" in lepton_scale and "No derivation of `1/256`; it is the open gate." in lepton_scale)
    audit.check("scale-reference primitive is units-only", "zero dimensionless content" in scale_reference and "units conversion" in scale_reference)

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    for absent in [
        "electron_mass_primitive",
        "physical_electron_readout_primitive",
        "koide_branch_mass_map_primitive",
        "native_zero_section_bridge_primitive",
        "physical_electron_species_primitive",
        "absolute_charged_lepton_scale_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", marker in note)

    explicit_non_claims = [
        "No derivation or ratification of `PHYSICAL_ELECTRON_READOUT_RETAINED`.",
        "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.",
        "No derivation or ratification of `NATIVE_ZERO_SECTION_BRIDGE_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED`.",
        "No derivation or ratification of `ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED`.",
        "No derivation or ratification of `KOIDE_BRANCH_MASS_MAP_RETAINED`.",
        "No derivation of `Q=2/3`, `delta = 2/9`, `rho_e(delta)`, `a_l^2`, or a",
        "No use of observed lepton masses, observed `m_W`, fitted `delta`, fitted",
        "No derivation of `alpha(0)`, static-source Rydberg, or full hydrogen",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives the physical electron mass",
        "This note ratifies the physical electron mass",
        "PHYSICAL_ELECTRON_READOUT_RETAINED is supplied",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT is supplied",
        "observed electron mass is used as proof",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
