#!/usr/bin/env python3
"""Verifier for the Koide R-eta readout ladder review packet."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_LADDER_REVIEW_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
CARRIER_CHAIN = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_CARRIER_REALIZATION_CHAIN_REVIEW_PACKET_2026-07-05.md"
PHYSICAL_CARRIER = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
SINGLE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SINGLE_FIXED_POINT_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
SINGLE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SINGLE_FIXED_POINT_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SINGLE_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SINGLE_FIXED_POINT_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
H_CLASS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
H_CLASS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
H_CLASS_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
H_UNIT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md"
H_UNIT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_RATIFICATION_DECISION_PACKET_2026-07-05.md"
H_UNIT_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
R_ETA_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
TWO_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
TWO_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
TWO_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
K2_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
K2_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PR5020 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5022 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5030 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_MULTISITE_PAULI_PR5030_CARRIER_PROVENANCE_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5032 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_COMMON_HW1_PR5032_CARRIER_IDENTIFICATION_IMPACT_DISCRIMINATOR_2026-07-05.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


READOUT_INPUTS = {
    "SINGLE_FIXED_POINT_READOUT_TEXT_LOCK",
    "FIXED_LOCUS_WEIGHT_DENSITY_ACCEPTED",
    "FINITE_KS_LOCAL_DENSITY_OPERATOR_FACE_ACCEPTED",
    "LOCAL_CAR_DENSITY_READOUT_BRIDGE_ACCEPTED",
    "PHYSICAL_CARRIER_CONTEXT_BOUNDARY_ACCOUNTED",
    "GLOBAL_ETA_EQUIVARIANT_ZERO_EXCLUDED_AS_READOUT",
    "EXTENSIVE_SUM_READOUT_EXCLUDED",
    "OTHER_K_EVEN_FUNCTIONAL_EXCLUDED",
    "NO_H_UNIT_OR_RADIAN_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

H_CLASS_INPUTS = {
    "R_ETA_H_CLASS_TEXT_LOCK",
    "FIXED_LOCUS_WEIGHT_DENSITY_ACCEPTED",
    "FINITE_KS_LOCAL_DENSITY_OPERATOR_FACE_ACCEPTED",
    "SUPPLIED_CONTEXT_REGISTRABILITY_ACCEPTED",
    "AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_ACCEPTED",
    "PHYSICAL_CARRIER_CONTEXT_RETAINED",
    "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED",
    "NO_H_UNIT_OR_RADIAN_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

H_UNIT_INPUTS = {
    "R_ETA_H_UNIT_TEXT_LOCK",
    "DEFECT_IDENTITY_UNIT_NORMAL_FORM_ACCEPTED",
    "ANGLE_SIDE_RIGIDITY_ACCEPTED",
    "TYPE_B_TO_RADIAN_RESIDUAL_ALIGNMENT_ACCEPTED",
    "IDENTITY_UNIT_SELECTION_THEOREM_RETAINED",
    "NO_COUNT_NORMALIZATION_SHORTCUT",
    "NO_H_CLASS_CARRIER_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

R_ETA_INPUTS = {
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

TWO_INPUTS = {
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

R_ETA_TO_TWO = {
    "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
    "RADIAN_READOUT_LICENSE_RETAINED",
}

TWO_TO_K2 = {
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
    "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
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


def closes_readout(inputs: set[str]) -> bool:
    return READOUT_INPUTS <= inputs


def closes_h_class(inputs: set[str]) -> bool:
    return H_CLASS_INPUTS <= inputs


def closes_h_unit(inputs: set[str]) -> bool:
    return H_UNIT_INPUTS <= inputs


def closes_r_eta(inputs: set[str]) -> bool:
    return R_ETA_INPUTS <= inputs


def closes_two(inputs: set[str]) -> bool:
    return TWO_INPUTS <= inputs


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
        PACKET,
        GOAL,
        KOIDE_FIREWALL,
        CARRIER_CHAIN,
        PHYSICAL_CARRIER,
        SINGLE_TARGET,
        SINGLE_DECISION,
        SINGLE_CURRENT,
        H_CLASS_TARGET,
        H_CLASS_DECISION,
        H_CLASS_CURRENT,
        H_UNIT_TARGET,
        H_UNIT_DECISION,
        H_UNIT_CURRENT,
        R_ETA_TARGET,
        R_ETA_DECISION,
        R_ETA_CURRENT,
        TWO_TARGET,
        TWO_DECISION,
        TWO_CURRENT,
        K2_TARGET,
        K2_DECISION,
        K2_CURRENT,
        PR5020,
        PR5022,
        PR5030,
        PR5032,
        PRIMITIVE_REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    packet = read(PACKET)
    packet_flat = flat(packet)

    section("Required packet content")
    required_phrases = [
        "Koide R-Eta Readout Ladder Review Packet",
        "review compression only",
        "sibling inputs, not a single chain",
        "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED",
        "R_ETA_H_CLASS_RETAINED",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED",
        "K2_R_ETA_EXACTNESS_RETAINED",
        "single fixed-point readout feeds h-class only",
        "R-eta readout retirement feeds two proof inputs, not the full subgate",
        "two-ninths/radian subgate feeds three K2 inputs, not full K2 exactness",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SINGLE_FIXED_POINT_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md",
        "`#5020`",
        "`#5022`",
        "`#5030`",
        "`#5032`",
        "`#5021`",
        "Open or green PR metadata is not proof input",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in packet_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in packet)

    section("Predicate checks")
    for universe, predicate, label in [
        (READOUT_INPUTS, closes_readout, "single fixed-point readout"),
        (H_CLASS_INPUTS, closes_h_class, "h-class"),
        (H_UNIT_INPUTS, closes_h_unit, "h-unit"),
        (R_ETA_INPUTS, closes_r_eta, "R-eta retirement"),
        (TWO_INPUTS, closes_two, "two-ninths/radian"),
        (K2_INPUTS, closes_k2, "K2 exactness"),
    ]:
        audit.check(f"full {label} contract closes", predicate(set(universe)))
        accepted = [subset for subset in all_subsets(universe) if predicate(subset)]
        audit.check(f"only full {label} subset closes", accepted == [set(universe)])

    for missing in [
        "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    ]:
        reduced = set(H_CLASS_INPUTS)
        reduced.remove(missing)
        audit.check(f"h-class fails without {missing}", not closes_h_class(reduced))

    for missing in [
        "IDENTITY_UNIT_SELECTION_THEOREM_RETAINED",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    ]:
        reduced = set(H_UNIT_INPUTS)
        reduced.remove(missing)
        audit.check(f"h-unit fails without {missing}", not closes_h_unit(reduced))

    for missing in [
        "R_ETA_H_CLASS_RETAINED",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    ]:
        reduced = set(R_ETA_INPUTS)
        reduced.remove(missing)
        audit.check(f"R-eta retirement fails without {missing}", not closes_r_eta(reduced))

    audit.check(
        "single fixed-point readout alone does not close h-class",
        not closes_h_class({"SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED"}),
    )
    audit.check("h-class alone does not close R-eta", not closes_r_eta({"R_ETA_H_CLASS_RETAINED"}))
    audit.check("h-unit alone does not close R-eta", not closes_r_eta({"R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED"}))
    audit.check(
        "h-class plus h-unit without carrier/owner/audit does not close R-eta",
        not closes_r_eta({"R_ETA_H_CLASS_RETAINED", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED"}),
    )
    audit.check("R-eta proof outputs are proper two-ninths inputs", R_ETA_TO_TWO < TWO_INPUTS)
    audit.check("R-eta proof outputs alone do not close two-ninths", not closes_two(set(R_ETA_TO_TWO)))
    audit.check("two-ninths outputs are proper K2 inputs", TWO_TO_K2 < K2_INPUTS)
    audit.check("two-ninths outputs alone do not close K2", not closes_k2(set(TWO_TO_K2)))

    ladder_consequences = {
        "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED",
        "R_ETA_H_CLASS_RETAINED",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED",
        "K2_R_ETA_EXACTNESS_RETAINED",
    }
    audit.check("K2 exactness alone does not close electron mass", not closes_electron_mass({"K2_R_ETA_EXACTNESS_RETAINED"}))
    audit.check("K2 exactness alone does not close hydrogen", not closes_hydrogen({"K2_R_ETA_EXACTNESS_RETAINED"}))
    audit.check("full ladder consequences do not close electron mass", not closes_electron_mass(ladder_consequences))
    audit.check("full ladder consequences do not close hydrogen", not closes_hydrogen(ladder_consequences))

    section("Authority, overview, and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    for label, container in [("goal packet", goal), ("Koide firewall", firewall)]:
        audit.check(
            f"{label} references R-eta readout ladder review packet",
            PACKET.name in container
            and "R-eta readout ladder review packet" in container
            and "review compression only" in container,
        )

    source_packets = {
        "single fixed-point target": read(SINGLE_TARGET),
        "h-class target": read(H_CLASS_TARGET),
        "h-unit target": read(H_UNIT_TARGET),
        "R-eta target": read(R_ETA_TARGET),
        "two-ninths target": read(TWO_TARGET),
        "K2 target": read(K2_TARGET),
        "carrier-chain packet": read(CARRIER_CHAIN),
        "PR5020 impact": read(PR5020),
        "PR5022 impact": read(PR5022),
        "PR5030 impact": read(PR5030),
        "PR5032 impact": read(PR5032),
    }
    for label, container in source_packets.items():
        audit.check(f"{label} keeps hydrogen nonclosure visible", "hydrogen" in container and "not" in container)

    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "r_eta_readout_ladder_primitive",
        "single_fixed_point_readout_primitive",
        "r_eta_h_class_primitive",
        "r_eta_h_unit_primitive",
        "r_eta_readout_retirement_primitive",
        "two_ninths_radian_readout_primitive",
        "k2_exactness_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "state-selection rule", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open-PR and non-claim boundaries")
    for marker in [
        "`#5016` zero-import hydrogen retained lane bundle",
        "`#5030` multisite Pauli finite-carrier provenance",
        "`#5032` common `hw=1` BZ-corner carrier identification",
        "`#5022` delta-eta supplied-premise audit repair",
        "`#5020` R-eta value-face relocation",
        "`#5021` primitive-retirement review",
        "Open or green PR metadata is not proof input",
    ]:
        audit.check(f"PR marker present: {marker}", flat(marker) in packet_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.",
        "No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.",
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No downstream retained-theorem verdict from open or merged PR metadata.",
        "No derivation or ratification of K1, K3, K4, physical electron mass, alpha",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden = [
        "This packet ratifies",
        "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED is supplied",
        "R_ETA_H_CLASS_RETAINED is supplied",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is supplied",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED is supplied",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This packet claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in packet)

    audit.summary()


if __name__ == "__main__":
    main()
