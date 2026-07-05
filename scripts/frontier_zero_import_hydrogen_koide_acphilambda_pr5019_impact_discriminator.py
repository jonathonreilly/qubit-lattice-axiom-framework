#!/usr/bin/env python3
"""Verifier for the hydrogen-facing Koide/AC_phi_lambda PR #5019 impact note."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PR4991 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_TIER_A_OWNER_RETIREMENT_PR4991_IMPACT_DISCRIMINATOR_2026-07-04.md"
PR5007 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_PR5007_IMPACT_DISCRIMINATOR_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
KOIDE_BRIDGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SPECIES_BRIDGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


PR5019_CONTEXT_INPUTS = {
    "PR5019_OPEN",
    "ACPHILAMBDA_FOUR_AXIOM_REBASE",
    "T1_DEPENDENCY_ATTRIBUTION",
    "NO_CLAIM_STRENGTH_CHANGE",
    "NO_AUDIT_STATUS_CHANGE",
}

ELECTRON_MASS_INPUTS = {
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
}

HYDROGEN_INPUTS = ELECTRON_MASS_INPUTS | {
    "ALPHA0_RETAINED",
    "STATIC_SOURCE_RYDBERG_RETAINED",
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


def closes_pr5019_context(inputs: set[str]) -> bool:
    return PR5019_CONTEXT_INPUTS <= inputs


def closes_electron_mass(inputs: set[str]) -> bool:
    return ELECTRON_MASS_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        PHYSICAL_ELECTRON,
        PR4991,
        PR5007,
        KOIDE_FIREWALL,
        KOIDE_BRIDGE,
        SPECIES_BRIDGE,
        K4_PACKET,
        TIER_A_REGISTRY,
        PRIMITIVE_REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required note content")
    required_phrases = [
        "Koide `AC_phi_lambda` PR #5019 Impact Discriminator",
        "open-PR impact discriminator / Koide dependency hygiene",
        "does not adopt PR `#5019`",
        "does not derive `AC_phi_lambda`",
        "does not derive the physical electron mass",
        "current four-axiom surface",
        "KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04",
        "Koide dependency hygiene",
        "audit-readiness context",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#4991` owner-governed Tier-A retirement | open",
        "The primitive registry was checked",
        "AC_phi_lambda",
        "No-Go Discipline Gate",
        "broad Koide/hydrogen closure claim fails; narrowed #5019",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    pr5019_inputs = set(PR5019_CONTEXT_INPUTS)
    audit.check("full #5019 context predicate accepts impact context", closes_pr5019_context(pr5019_inputs))
    audit.check("#5019 context alone does not close electron mass", not closes_electron_mass(pr5019_inputs))
    audit.check("#5019 context alone does not close hydrogen", not closes_hydrogen(pr5019_inputs))
    audit.check("electron mass predicate closes only with mass inputs", closes_electron_mass(set(ELECTRON_MASS_INPUTS)))
    audit.check("hydrogen predicate closes only with hydrogen inputs", closes_hydrogen(set(HYDROGEN_INPUTS)))
    for missing in sorted(ELECTRON_MASS_INPUTS):
        reduced = set(ELECTRON_MASS_INPUTS)
        reduced.remove(missing)
        audit.check(f"electron mass fails without {missing}", not closes_electron_mass(reduced))

    section("Authority boundary checks")
    goal = read(GOAL)
    physical_electron = read(PHYSICAL_ELECTRON)
    pr4991 = read(PR4991)
    pr5007 = read(PR5007)
    koide_firewall = read(KOIDE_FIREWALL)
    koide_bridge = read(KOIDE_BRIDGE)
    species_bridge = read(SPECIES_BRIDGE)
    k4_packet = read(K4_PACKET)
    tier_a = json.loads(read(TIER_A_REGISTRY))
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    primitive_nodes = primitive_registry["nodes"]

    audit.check("goal packet references #5019 impact note", NOTE.name in goal and "#5019" in goal)
    audit.check("physical electron packet references #5019 impact note", NOTE.name in physical_electron and "#5019" in physical_electron)
    audit.check("#4991 impact note keeps theorem closure separate", "not theorem closure" in pr4991 and "No theorem derivation" in pr4991)
    audit.check("#5007 impact note keeps physical readout separate", "not a retained electron readout" in pr5007 and "physical electron species bridge" in pr5007)
    audit.check("Koide firewall separates K1-K4", all(token in koide_firewall for token in ["K1", "K2", "K3", "K4"]))
    audit.check("native bridge packet remains conditional", "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in koide_bridge and "does not ratify" in koide_bridge)
    audit.check("species bridge packet remains conditional", "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in species_bridge and "does not ratify" in species_bridge)
    audit.check("K4 packet remains separate", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in k4_packet and "does not ratify" in k4_packet)
    audit.check("Tier-A registry still names AC_phi_lambda on current branch", "AC_phi_lambda" in read(TIER_A_REGISTRY))
    audit.check("AC_phi_lambda is not a primitive node", "AC_phi_lambda" not in primitive_nodes)
    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive node present: {node_name}", node_name in primitive_nodes)
    for excluded in ["mass ratio", "selector", "readout bridge", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_non_claims = [
        "No adoption or landing claim for PR `#5019`.",
        "No audit verdict or status change.",
        "No derivation of `AC_phi_lambda`.",
        "No derivation or ratification of Koide native zero-section closure.",
        "No derivation or ratification of a physical electron species bridge.",
        "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.",
        "No derivation of `S_l`, A3, `C_A3`, `alpha(0)`, static-source Rydberg, or",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note adopts PR `#5019`",
        "PR #5019 derives hydrogen",
        "PR #5019 derives `m_e`",
        "AC_phi_lambda retained theorem",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
