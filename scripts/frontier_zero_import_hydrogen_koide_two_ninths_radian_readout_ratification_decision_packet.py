#!/usr/bin/env python3
"""Verifier for the Koide two-ninths radian-readout decision packet."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
TWO_NINTHS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
TWO_NINTHS_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
K2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
H_CLASS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
H_UNIT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PR5020_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5022_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
FLAVOR_TWO_NINTHS = ROOT / "docs" / "FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md"
NATIVE_RADIAN_SEPARATION = ROOT / "docs" / "KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md"
A1_RADIAN_AUDIT = ROOT / "docs" / "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md"
BRANNEN_OPEN_GATE = ROOT / "docs" / "LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md"
TIER_A_BOUNDED = ROOT / "docs" / "CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md"
ORIENTATION_Z2 = ROOT / "docs" / "KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_NARROW_THEOREM_NOTE_2026-06-08.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


TWO_NINTHS_INPUTS = {
    "TWO_NINTHS_READOUT_TEXT_LOCK",
    "FINITE_TWO_NINTHS_DENSITY_CONTEXT_ACCEPTED",
    "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
    "RADIAN_READOUT_LICENSE_RETAINED",
    "FOLD_AND_BRANCH_DOMAIN_LOCK",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

K2_INPUTS = {
    "K2_EXACTNESS_TEXT_LOCK",
    "REGISTERED_PHI_VALUE_FACE_ACCEPTED",
    "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
    "RADIAN_READOUT_LICENSE_RETAINED",
    "FOLD_AND_BRANCH_DOMAIN_LOCK",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

SUBGATE_K2_SUPPLIES = {
    "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
    "RADIAN_READOUT_LICENSE_RETAINED",
    "FOLD_AND_BRANCH_DOMAIN_LOCK",
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


def all_subsets(items: set[str]) -> list[set[str]]:
    ordered = sorted(items)
    subsets: list[set[str]] = []
    for size in range(len(ordered) + 1):
        for combo in combinations(ordered, size):
            subsets.append(set(combo))
    return subsets


def closes_two_ninths(inputs: set[str]) -> bool:
    return TWO_NINTHS_INPUTS <= inputs


def closes_k2(inputs: set[str]) -> bool:
    return K2_INPUTS <= inputs


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
        KOIDE_FIREWALL,
        TWO_NINTHS_TARGET,
        TWO_NINTHS_NO_GO,
        K2_TARGET,
        K2_NO_GO,
        R_ETA_TARGET,
        R_ETA_DECISION,
        H_CLASS_DECISION,
        H_UNIT_DECISION,
        PR5020_IMPACT,
        PR5022_IMPACT,
        PHYSICAL_ELECTRON,
        FLAVOR_TWO_NINTHS,
        NATIVE_RADIAN_SEPARATION,
        A1_RADIAN_AUDIT,
        BRANNEN_OPEN_GATE,
        TIER_A_BOUNDED,
        ORIENTATION_Z2,
        PRIMITIVE_REGISTRY,
        TIER_A_REGISTRY,
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
        "Koide Two-Ninths Radian Readout Ratification Decision Packet",
        "decision packet / Koide K2 two-ninths radian-readout import-retirement handoff",
        "does not ratify `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED",
        "TWO_NINTHS_READOUT_TEXT_LOCK",
        "FINITE_TWO_NINTHS_DENSITY_CONTEXT_ACCEPTED",
        "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
        "RADIAN_READOUT_LICENSE_RETAINED",
        "FOLD_AND_BRANCH_DOMAIN_LOCK",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those nine contract inputs",
        "Phi = (1/3) arccos(cos 3delta)",
        "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md",
        "KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md",
        "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
        "LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md",
        "CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md",
        "KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_NARROW_THEOREM_NOTE_2026-06-08.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation",
        "`#5021` primitive-retirement review draft",
        "The primitive registry was checked",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED is packaged as a nine-input",
        "No-Go Discipline Gate",
        "broad `delta = 2/9` retained claim fails; narrowed",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(TWO_NINTHS_INPUTS)
    audit.check("full two-ninths/radian decision contract accepts handoff", closes_two_ninths(full_inputs))
    for missing in sorted(TWO_NINTHS_INPUTS):
        reduced = set(TWO_NINTHS_INPUTS)
        reduced.remove(missing)
        audit.check(f"two-ninths/radian decision fails without {missing}", not closes_two_ninths(reduced))
    accepted_subsets = [subset for subset in all_subsets(TWO_NINTHS_INPUTS) if closes_two_ninths(subset)]
    audit.check("only full tested two-ninths contract subset closes decision", accepted_subsets == [full_inputs])

    consequence = {"KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED"}
    audit.check("subgate consequence alone does not close K2 exactness", not closes_k2(consequence))
    audit.check("subgate consequence alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("subgate consequence alone does not close hydrogen", not closes_hydrogen(consequence))
    audit.check(
        "subgate K2 supplies alone do not close K2 exactness",
        not closes_k2(set(SUBGATE_K2_SUPPLIES)),
    )
    audit.check(
        "subgate plus value face still needs full K2 owner/audit gates",
        not closes_k2(SUBGATE_K2_SUPPLIES | {"REGISTERED_PHI_VALUE_FACE_ACCEPTED"}),
    )

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    two_ninths_target = read(TWO_NINTHS_TARGET)
    two_ninths_no_go = read(TWO_NINTHS_NO_GO)
    k2_target = read(K2_TARGET)
    k2_no_go = read(K2_NO_GO)
    r_eta_target = read(R_ETA_TARGET)
    r_eta_decision = read(R_ETA_DECISION)
    h_class_decision = read(H_CLASS_DECISION)
    h_unit_decision = read(H_UNIT_DECISION)
    pr5020 = read(PR5020_IMPACT)
    pr5022 = read(PR5022_IMPACT)
    physical_electron = read(PHYSICAL_ELECTRON)
    flavor = read(FLAVOR_TWO_NINTHS)
    native = read(NATIVE_RADIAN_SEPARATION)
    a1_audit = read(A1_RADIAN_AUDIT)
    brannen_open_gate = read(BRANNEN_OPEN_GATE)
    tier_a_bounded = read(TIER_A_BOUNDED)
    orientation = read(ORIENTATION_Z2)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    tier_a = read(TIER_A_REGISTRY)
    realized = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
        ("two-ninths target", two_ninths_target),
        ("K2 target", k2_target),
    ]:
        audit.check(
            f"{label} references two-ninths/radian decision packet",
            NOTE.name in container and "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in container,
        )

    audit.check(
        "current no-go keeps subgate open",
        "current retained, primitive, merged-PR, and open-PR surfaces do not supply" in two_ninths_no_go
        and "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in two_ninths_no_go,
    )
    audit.check(
        "K2 no-go keeps K2 exactness open",
        "current retained, primitive, merged-PR, and open-PR surfaces do not supply" in k2_no_go
        and "K2_R_ETA_EXACTNESS_RETAINED" in k2_no_go,
    )
    audit.check("R-eta target remains upstream support", "R_ETA_READOUT_IDENTIFICATION_RETAINED" in r_eta_target)
    audit.check("R-eta decision remains upstream support", "R_ETA_READOUT_IDENTIFICATION_RETAINED" in r_eta_decision and "does not ratify" in r_eta_decision)
    audit.check("h-class decision remains one R-eta subinput", "R_ETA_H_CLASS_RETAINED" in h_class_decision and "does not ratify" in h_class_decision)
    audit.check("h-unit decision remains one R-eta subinput", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in h_unit_decision and "does not ratify" in h_unit_decision)
    audit.check("#5020 impact keeps exactness residual open", "exactness remains open" in pr5020)
    audit.check("#5022 impact keeps R-eta supplied, not derived", "supplied" in pr5022 and "no retained R-eta derivation" in pr5022)
    audit.check("physical electron packet remains downstream", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in physical_electron)
    audit.check("finite 2/9 source remains density/readout split", "`2/9` is forced as a local" in flavor and "Physical readout is the one remaining gate" in flavor)
    audit.check("native radian theorem does not close bridge", "does **not** close the radian-bridge postulate" in flat(native))
    audit.check("A1 radian audit keeps Type-B primitive open", "TYPE_B_TO_RADIAN_IDENTIFICATION_REMAINS_PRIMITIVE=TRUE" in a1_audit)
    audit.check("Brannen open gate does not derive delta", "not derive `delta = 2/9`" in brannen_open_gate)
    audit.check(
        "Tier-A bounded theorem is not zero-import retained delta",
        "bounded theorem under explicit Tier-A admission" in tier_a_bounded
        and "Does **not** derive `delta = 2/9` from the framework baseline plus retained content" in tier_a_bounded,
    )
    audit.check(
        "orientation theorem leaves magnitude and handedness open",
        "does **not** supply the realized handedness" in orientation
        and "does **not** select the magnitude `2/9`" in orientation,
    )
    audit.check("Tier-A registry keeps AC_phi_lambda separate from primitives", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in primitive_nodes)
    audit.check("realized-state primitive supplies no value", "no state" in realized and "or value is supplied" in flat(realized))

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "koide_two_ninths_radian_readout_primitive",
        "distinguished_two_ninths_theorem_primitive",
        "radian_readout_license_primitive",
        "fold_branch_domain_lock_primitive",
        "delta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["mass ratio", "selector", "readout bridge", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open PR and non-claim boundaries")
    open_markers = [
        "`#5022` audit repair: delta-eta chain R-eta supplied premise | merged",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | open, clean",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | open, clean",
        "`#5018`/`#5017` chirality/domain-wall stack | open, clean",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "Clean/green status is not proof input",
    ]
    for marker in open_markers:
        audit.check(f"open PR marker present: {marker}", flat(marker) in note_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of `DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED`.",
        "No derivation or ratification of `RADIAN_READOUT_LICENSE_RETAINED`.",
        "No derivation or ratification of `FOLD_AND_BRANCH_DOMAIN_LOCK`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No derivation of `AC_phi_lambda`, `R_ETA_READOUT_IDENTIFICATION_RETAINED`,",
        "No claim that PR `#5020`, PR `#5021`, or merged PR `#5022` supplies the",
        "No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`, observed",
        "No derivation of K1 occupancy/counting, K3 physical species bridge, K4",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This packet ratifies two-ninths",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED is supplied",
        "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED is supplied",
        "RADIAN_READOUT_LICENSE_RETAINED is supplied",
        "FOLD_AND_BRANCH_DOMAIN_LOCK is supplied",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This packet claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
