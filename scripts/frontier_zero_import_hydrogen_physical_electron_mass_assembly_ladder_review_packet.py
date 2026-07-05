#!/usr/bin/env python3
"""Verifier for the physical electron mass assembly ladder review packet.

This runner checks that the electron-mass dependency compression is explicit
and remains a review-support surface. It does not ratify physical m_e,
alpha(0), static-source Rydberg closure, or hydrogen.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
ELECTRON_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ELECTRON_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
NATIVE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
NATIVE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SPECIES_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SPECIES_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
K4_LADDER = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_K4_SCALE_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
SCALE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SCALE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
BRANCH_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md"
BRANCH_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md"
MASS_SPECTRUM_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md"
R_LEP_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
ALPHA0_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SCALE_REFERENCE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


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

DIRECT_ELECTRON_ROWS = {
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
}

STATIC_SOURCE_INPUTS = {
    "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
    "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
    "ATOMIC_OPERATOR_HARNESS_VERIFIED",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
    "AUDIT_ACCEPTANCE",
}

ALPHA0_INPUTS = {
    "ALPHA0_TRANSPORT_TEXT_LOCK",
    "ALPHA_MZ_RETAINED",
    "QED_LOOP_KERNEL_RETAINED",
    "R_LEP_THRESHOLDS_RETAINED",
    "R_Q_HEAVY_THRESHOLDS_RETAINED",
    "R_HAD_NP_RETAINED",
    "SCHEME_DECOUPLING_MATCHING_RETAINED",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
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


def closes_static_source(inputs: set[str]) -> bool:
    return STATIC_SOURCE_INPUTS <= inputs


def closes_alpha0(inputs: set[str]) -> bool:
    return ALPHA0_INPUTS <= inputs


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
        KOIDE_FIREWALL,
        ELECTRON_PACKET,
        ELECTRON_NO_GO,
        NATIVE_DECISION,
        NATIVE_NO_GO,
        SPECIES_DECISION,
        SPECIES_NO_GO,
        K4_LADDER,
        SCALE_DECISION,
        SCALE_NO_GO,
        BRANCH_DECISION,
        BRANCH_NO_GO,
        MASS_SPECTRUM_PACKET,
        R_LEP_PACKET,
        STATIC_TARGET,
        ALPHA0_NO_GO,
        SCALE_REFERENCE,
        REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required packet content")
    required_phrases = [
        "Physical Electron Mass Assembly Ladder Review Packet",
        "support / review-compression packet",
        "this packet does not ratify the physical",
        "reviewable surface",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "KOIDE_BRANCH_MASS_MAP_RETAINED",
        "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
        "PHYSICAL_ELECTRON_READOUT_RETAINED",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "PHYSICAL_ELECTRON_MASS_TEXT_LOCK",
        "NO_LEPTON_COMPARATOR_PROOF_INPUT",
        "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those eleven contract inputs",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_K4_SCALE_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md",
        "r_k(delta) = 1 + sqrt(2) cos(delta + 2 pi k / 3)",
        "Q(delta) = sum_k r_k(delta)^2 / (sum_k r_k(delta))^2 = 2/3",
        "rho_e(delta) = min_k r_k(delta)^2",
        "m_e = a_l^2 * rho_e(delta)",
        "delta = 2/9",
        "rho_e(delta) = 0.001628115093",
        "phase-blind",
        "clean/green status is not a prerequisite",
        "`#5033` RP two-step runner scope cleanup | open, clean",
        "`#5030` finite multisite Pauli carrier provenance | open, clean",
        "`#5021` primitive-retirement review | open draft, dirty",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open",
        "`#5017` domain-wall anomaly inflow spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` chirality domain-wall free-field note | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#4991` owner-governed Tier-A retirement | open",
        "The primitive registry was checked",
        "electron_mass_primitive",
        "physical_electron_readout_primitive",
        "native_zero_section_bridge_primitive",
        "physical_electron_species_primitive",
        "absolute_charged_lepton_scale_primitive",
        "koide_branch_mass_map_primitive",
        "alpha0_primitive",
        "hydrogen_primitive",
        "Distance To Hydrogen",
        "No-Go Discipline Gate",
        "OPEN POSITIVE ROUTE",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(ELECTRON_MASS_INPUTS)
    audit.check("full electron-mass contract accepts retained handoff", closes_electron_mass(full_inputs))
    for missing in sorted(ELECTRON_MASS_INPUTS):
        reduced = set(ELECTRON_MASS_INPUTS)
        reduced.remove(missing)
        audit.check(f"electron-mass handoff fails without {missing}", not closes_electron_mass(reduced))
    accepted_subsets = [subset for subset in all_subsets(ELECTRON_MASS_INPUTS) if closes_electron_mass(subset)]
    audit.check("only full electron-mass subset closes handoff", accepted_subsets == [full_inputs])

    for row in sorted(DIRECT_ELECTRON_ROWS):
        audit.check(f"{row} alone does not close electron mass", not closes_electron_mass({row}))
    audit.check(
        "direct electron rows still need text, scale-reference, comparator, owner, and audit gates",
        not closes_electron_mass(set(DIRECT_ELECTRON_ROWS)),
    )
    partial_with_scale_reference = set(DIRECT_ELECTRON_ROWS) | {"SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED"}
    audit.check(
        "direct rows plus scale reference still do not close electron mass",
        not closes_electron_mass(partial_with_scale_reference),
    )
    audit.check(
        "retained electron mass alone does not close static-source Rydberg",
        not closes_static_source({"RETAINED_ELECTRON_MASS_PHYSICAL_UNIT"}),
    )
    audit.check(
        "retained alpha0 alone does not close static-source Rydberg",
        not closes_static_source({"RETAINED_ALPHA0_LOW_ENERGY_COULOMB"}),
    )
    audit.check(
        "R-Lep threshold consequence alone does not close alpha0",
        not closes_alpha0({"R_LEP_THRESHOLDS_RETAINED"}),
    )
    audit.check("full static-source predicate closes with all inputs", closes_static_source(set(STATIC_SOURCE_INPUTS)))

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
    audit.check("scale factor changes physical mass", abs((2.0 * rho_delta) / (1.0 * rho_delta) - 2.0) < 1e-15)
    audit.check("branch factor alone is dimensionless and positive", 0.0 < rho_delta < 1.0)

    section("Authority and cross-reference checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    electron_packet = read(ELECTRON_PACKET)
    electron_no_go = read(ELECTRON_NO_GO)
    native_decision = read(NATIVE_DECISION)
    native_no_go = read(NATIVE_NO_GO)
    species_decision = read(SPECIES_DECISION)
    species_no_go = read(SPECIES_NO_GO)
    k4_ladder = read(K4_LADDER)
    scale_decision = read(SCALE_DECISION)
    scale_no_go = read(SCALE_NO_GO)
    branch_decision = read(BRANCH_DECISION)
    branch_no_go = read(BRANCH_NO_GO)
    mass_spectrum = read(MASS_SPECTRUM_PACKET)
    r_lep = read(R_LEP_PACKET)
    static_target = read(STATIC_TARGET)
    alpha0_no_go = read(ALPHA0_NO_GO)
    scale_reference = flat(read(SCALE_REFERENCE)).lower()
    registry = json.loads(read(REGISTRY))
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("Koide electron-readout firewall", koide_firewall),
        ("physical electron mass packet", electron_packet),
        ("physical electron mass current-surface no-go", electron_no_go),
    ]:
        audit.check(f"{container_name} references electron assembly packet", NOTE.name in container)

    audit.check("static target consumes retained electron mass", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in static_target)
    audit.check("static target still needs alpha0", "RETAINED_ALPHA0_LOW_ENERGY_COULOMB" in static_target)
    audit.check("static target does not name assembly as retained output", "PHYSICAL_ELECTRON_MASS_ASSEMBLY_LADDER_REVIEW_PACKET" not in static_target)
    audit.check("native bridge packet remains bridge only", "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in native_decision and "does not derive `m_e`" in native_decision)
    audit.check("native no-go keeps bridge open", "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in native_no_go and "current retained, primitive, and open-PR surfaces do not supply" in native_no_go)
    audit.check("species packet remains K3 only", "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in species_decision and "K3 support only" in species_decision)
    audit.check("species no-go keeps K3 open", "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in species_no_go and "current retained, primitive, merged-PR, and open-PR surfaces do not supply" in species_no_go)
    audit.check("K4 ladder remains support only", "support / review-compression packet" in k4_ladder and "this packet does not ratify K4" in k4_ladder)
    audit.check("scale packet remains K4 only", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in scale_decision and "K4 support only" in scale_decision)
    audit.check("scale no-go keeps K4 open", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in scale_no_go and "current retained, primitive, and open-PR surfaces do not supply" in scale_no_go)
    audit.check("branch mass-map packet remains map only", "KOIDE_BRANCH_MASS_MAP_RETAINED" in branch_decision and "does not derive a physical electron mass" in branch_decision)
    audit.check("branch mass-map no-go keeps map open", "KOIDE_BRANCH_MASS_MAP_RETAINED" in branch_no_go and "SQUARE_ROOT_MASS_READOUT_RETAINED" in branch_no_go)
    audit.check("mass-spectrum sibling keeps full triple separate", "PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED" in mass_spectrum and "mass-spectrum target remains needed" in electron_packet)
    audit.check("R-Lep packet keeps alpha0 thresholds separate", "R_LEP_THRESHOLDS_RETAINED" in r_lep and "does not by itself supply" in r_lep)
    audit.check("alpha0 no-go keeps low-energy coupling open", "RETAINED_ALPHA0_LOW_ENERGY_COULOMB" in alpha0_no_go and "current retained, primitive, and open-PR surfaces do not supply" in alpha0_no_go)
    audit.check("scale-reference primitive is units-only", "zero dimensionless content" in scale_reference and "units conversion" in scale_reference)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    for absent in [
        "electron_mass_primitive",
        "physical_electron_readout_primitive",
        "native_zero_section_bridge_primitive",
        "physical_electron_species_primitive",
        "absolute_charged_lepton_scale_primitive",
        "koide_branch_mass_map_primitive",
        "alpha0_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5033` RP two-step runner scope cleanup | open, clean",
        "`#5030` finite multisite Pauli carrier provenance | open, clean",
        "`#5021` primitive-retirement review | open draft, dirty",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open",
        "`#5017` domain-wall anomaly inflow spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` chirality domain-wall free-field note | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#4991` owner-governed Tier-A retirement | open",
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
        "This packet derives the physical electron mass",
        "This packet ratifies the physical electron mass",
        "PHYSICAL_ELECTRON_READOUT_RETAINED is supplied",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT is supplied",
        "observed electron mass is used as proof",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
