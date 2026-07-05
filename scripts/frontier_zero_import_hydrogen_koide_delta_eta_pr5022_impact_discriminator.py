#!/usr/bin/env python3
"""Verifier for the hydrogen-facing Koide delta-eta PR #5022 impact note."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PR5020 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
K2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
TWO_NINTHS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
TWO_NINTHS_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


PR5022_CONTEXT_INPUTS = {
    "PR5022_MERGED_AUDIT_SUCCESS",
    "R_ETA_DECLARED_SUPPLIED_PREMISE",
    "CONDITIONAL_IMPLICATION_CHECKED",
    "RETAINED_K_ORBIT_FORM_AUTHORITY",
    "NO_RETAINED_R_ETA_DERIVATION",
    "NO_RETAINED_STATUS_CHANGE",
}

K2_EXACTNESS_INPUTS = {
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

TWO_NINTHS_SUBGATE_INPUTS = {
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


def closes_pr5022_context(inputs: set[str]) -> bool:
    return PR5022_CONTEXT_INPUTS <= inputs


def closes_k2_exactness(inputs: set[str]) -> bool:
    return K2_EXACTNESS_INPUTS <= inputs


def closes_two_ninths_subgate(inputs: set[str]) -> bool:
    return TWO_NINTHS_SUBGATE_INPUTS <= inputs


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
        PHYSICAL_ELECTRON,
        PR5020,
        R_ETA_TARGET,
        K2_TARGET,
        K2_NO_GO,
        TWO_NINTHS_TARGET,
        TWO_NINTHS_NO_GO,
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
        "Koide Delta-Eta PR #5022 Impact Discriminator",
        "merged-PR impact discriminator / Koide K2 conditionality boundary",
        "does not claim merged PR `#5022` supplies a retained R-eta derivation",
        "does not derive R-eta",
        "does not derive `delta = 2/9`",
        "does not ratify `K2_R_ETA_EXACTNESS_RETAINED`",
        "does not ratify `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`",
        "R-eta supplied-premise declaration",
        "declared supplied readout-identification premise",
        "conditional implication",
        "retained one-hop K-orbit form authority",
        "checks the implication, not the premise",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED",
        "`#5022` delta-eta chain R-eta supplied-premise audit repair | merged",
        "`#5021` primitive-retirement review draft",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | open",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad K2/hydrogen closure claim fails; narrowed #5022",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    pr5022_inputs = set(PR5022_CONTEXT_INPUTS)
    audit.check("full #5022 context predicate accepts impact context", closes_pr5022_context(pr5022_inputs))
    audit.check("#5022 context alone does not close K2 exactness", not closes_k2_exactness(pr5022_inputs))
    audit.check("#5022 context alone does not close two-ninths subgate", not closes_two_ninths_subgate(pr5022_inputs))
    audit.check("#5022 context alone does not close electron mass", not closes_electron_mass(pr5022_inputs))
    audit.check("#5022 context alone does not close hydrogen", not closes_hydrogen(pr5022_inputs))
    audit.check("K2 exactness predicate closes only with target inputs", closes_k2_exactness(set(K2_EXACTNESS_INPUTS)))
    audit.check("two-ninths predicate closes only with subgate inputs", closes_two_ninths_subgate(set(TWO_NINTHS_SUBGATE_INPUTS)))
    audit.check("electron mass predicate closes only with mass inputs", closes_electron_mass(set(ELECTRON_MASS_INPUTS)))
    audit.check("hydrogen predicate closes only with hydrogen inputs", closes_hydrogen(set(HYDROGEN_INPUTS)))

    section("Authority boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    physical_electron = read(PHYSICAL_ELECTRON)
    pr5020 = read(PR5020)
    k2_target = read(K2_TARGET)
    k2_no_go = read(K2_NO_GO)
    two_ninths_target = read(TWO_NINTHS_TARGET)
    two_ninths_no_go = read(TWO_NINTHS_NO_GO)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    tier_a_text = read(TIER_A_REGISTRY)
    realized_text = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
        ("K2 exactness target", k2_target),
        ("K2 exactness no-go", k2_no_go),
        ("two-ninths/radian target", two_ninths_target),
        ("two-ninths/radian no-go", two_ninths_no_go),
    ]:
        audit.check(f"{label} references #5022 impact note", NOTE.name in container and "#5022" in container)

    audit.check("#5020 impact keeps exactness open", "exactness remains open" in pr5020)
    audit.check("K2 target remains ten-input contract", "No proper subset of those ten inputs" in k2_target)
    audit.check("K2 current no-go keeps exactness open", "current retained, primitive, merged-PR, and open-PR surfaces do not supply" in k2_no_go)
    audit.check("two-ninths target remains subgate", "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in two_ninths_target)
    audit.check("two-ninths current no-go keeps subgate open", "current retained, primitive, merged-PR, and open-PR surfaces do not supply" in two_ninths_no_go)
    audit.check("physical electron packet keeps K2 context non-mass", "K2 value-face progress only" in physical_electron and "no delta exactness theorem" in physical_electron)
    audit.check("Koide firewall separates K1-K4", all(token in koide_firewall for token in ["K1", "K2", "K3", "K4"]))
    audit.check("realized-state primitive supplies no values", "no state" in realized_text and "or value is supplied" in flat(realized_text))
    audit.check("Tier-A registry still names AC_phi_lambda", "AC_phi_lambda" in tier_a_text)
    audit.check("R-eta is not a primitive node", "R-eta" not in primitive_nodes and "r_eta" not in primitive_nodes)
    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive node present: {node_name}", node_name in primitive_nodes)
    for absent in [
        "r_eta_exactness_primitive",
        "delta_exactness_primitive",
        "two_ninths_radian_readout_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered shortcut primitive: {absent}", absent not in primitive_nodes)
    for excluded in ["mass ratio", "selector", "readout bridge", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_non_claims = [
        "No claim that merged PR `#5022` supplies a retained R-eta derivation.",
        "No audit verdict or retained-status change.",
        "No derivation or ratification of R-eta.",
        "No derivation of `delta = 2/9` from current retained inventory alone.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of K1 occupancy/counting, K3 physical species",
        "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.",
        "No derivation of `S_l`, A3, `C_A3`, `alpha(0)`, static-source Rydberg, or",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note adopts PR `#5022`",
        "PR #5022 derives hydrogen",
        "PR #5022 derives `m_e`",
        "R-eta is derived from retained inventory",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED is supplied",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
