#!/usr/bin/env python3
"""Verifier for the Koide R-eta readout-retirement decision packet."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
H_CLASS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
H_UNIT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md"
PR5022_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5020_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
TWO_NINTHS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


R_ETA_RETIREMENT_INPUTS = {
    "R_ETA_RETIREMENT_TEXT_LOCK",
    "FORM_LAYER_AND_K_ORBIT_AUTHORITY_ACCEPTED",
    "FINITE_FIXED_LOCUS_ARITHMETIC_ACCEPTED",
    "PHYSICAL_CARRIER_CONTEXT_RETAINED",
    "R_ETA_H_CLASS_RETAINED",
    "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED",
    "NO_R_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

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


def closes_r_eta_retirement(inputs: set[str]) -> bool:
    return R_ETA_RETIREMENT_INPUTS <= inputs


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
        R_ETA_TARGET,
        H_CLASS_TARGET,
        H_UNIT_TARGET,
        PR5022_IMPACT,
        PR5020_IMPACT,
        TWO_NINTHS_TARGET,
        K2_TARGET,
        PHYSICAL_ELECTRON,
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
        "Koide R-Eta Readout Retirement Ratification Decision Packet",
        "decision packet / Koide R-eta import-retirement handoff",
        "does not ratify `R_ETA_READOUT_IDENTIFICATION_RETAINED`",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED",
        "R_ETA_RETIREMENT_TEXT_LOCK",
        "FORM_LAYER_AND_K_ORBIT_AUTHORITY_ACCEPTED",
        "FINITE_FIXED_LOCUS_ARITHMETIC_ACCEPTED",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED",
        "R_ETA_H_CLASS_RETAINED",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED",
        "NO_R_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those eleven contract inputs",
        "merged PR `#5022`",
        "`#5021` primitive-retirement review draft",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation",
        "The primitive registry was checked",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is packaged as an eleven-input",
        "No-Go Discipline Gate",
        "broad R-eta-retained claim fails; narrowed ratification",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(R_ETA_RETIREMENT_INPUTS)
    audit.check("full R-eta retirement contract accepts decision", closes_r_eta_retirement(full_inputs))
    for missing in sorted(R_ETA_RETIREMENT_INPUTS):
        reduced = set(R_ETA_RETIREMENT_INPUTS)
        reduced.remove(missing)
        audit.check(f"R-eta retirement decision fails without {missing}", not closes_r_eta_retirement(reduced))
    accepted_subsets = [subset for subset in all_subsets(R_ETA_RETIREMENT_INPUTS) if closes_r_eta_retirement(subset)]
    audit.check("only full tested R-eta contract subset closes decision", accepted_subsets == [full_inputs])

    consequence = {"R_ETA_READOUT_IDENTIFICATION_RETAINED"}
    audit.check("R-eta consequence alone does not close two-ninths subgate", not closes_two_ninths(consequence))
    audit.check("R-eta consequence alone does not close K2 exactness", not closes_k2(consequence))
    audit.check("R-eta consequence alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("R-eta consequence alone does not close hydrogen", not closes_hydrogen(consequence))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    r_eta_target = read(R_ETA_TARGET)
    h_class = read(H_CLASS_TARGET)
    h_unit = read(H_UNIT_TARGET)
    pr5022 = read(PR5022_IMPACT)
    pr5020 = read(PR5020_IMPACT)
    two_ninths = read(TWO_NINTHS_TARGET)
    k2 = read(K2_TARGET)
    physical_electron = read(PHYSICAL_ELECTRON)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    tier_a = read(TIER_A_REGISTRY)
    realized = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
    ]:
        audit.check(f"{label} references decision packet", NOTE.name in container and "R_ETA_READOUT_IDENTIFICATION_RETAINED" in container)
    audit.check("R-eta target names same eleven-input contract", "R_ETA_RETIREMENT_TEXT_LOCK" in r_eta_target and "No proper subset supplies the handoff" in r_eta_target)
    audit.check("h-class target remains one subinput", "R_ETA_H_CLASS_RETAINED" in h_class and "does not ratify" in h_class)
    audit.check("h-unit target remains one subinput", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in h_unit and "does not ratify" in h_unit)
    audit.check("#5022 impact keeps R-eta supplied, not derived", "supplied" in pr5022 and "no retained R-eta derivation" in pr5022)
    audit.check("#5020 impact keeps exactness open", "exactness remains open" in pr5020)
    audit.check("two-ninths target remains downstream consumer", "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in two_ninths and "not the full K2 exactness target" in two_ninths)
    audit.check("K2 target remains downstream consumer", "K2_R_ETA_EXACTNESS_RETAINED" in k2 and "No proper subset of those ten inputs" in k2)
    audit.check("physical electron packet remains downstream", "K2 value-face progress only" in physical_electron and "no delta exactness theorem" in physical_electron)
    audit.check("Tier-A registry still names R-eta admission", "delta readout identification R-eta" in tier_a)
    audit.check("realized-state primitive supplies no value", "no state" in realized and "or value is supplied" in flat(realized))

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in primitive_nodes)
    for absent in [
        "r_eta_readout_identification_primitive",
        "r_eta_h_class_primitive",
        "r_eta_h_unit_primitive",
        "delta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in primitive_nodes)
    for excluded in ["mass ratio", "selector", "readout bridge", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_nonclaims = [
        "No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.",
        "No derivation of R-eta from the current retained inventory alone.",
        "No derivation of `delta = 2/9` as a retained physical phase.",
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No derivation or ratification of K1 occupancy/counting, K3 physical species",
        "No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`, observed",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This packet ratifies R-eta",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
        "R_ETA_H_CLASS_RETAINED is supplied",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is supplied",
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
