#!/usr/bin/env python3
"""Verifier for the Koide R-eta readout-retirement current-surface no-go."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
H_CLASS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
H_CLASS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
H_UNIT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md"
H_UNIT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_RATIFICATION_DECISION_PACKET_2026-07-05.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
K2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
TWO_NINTHS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
TWO_NINTHS_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PR5019_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5020_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5022_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md"
AC_R_ETA_CLUSTER = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_AC_R_ETA_UPSTREAM_CLUSTER_IMPACT_DISCRIMINATOR_2026-07-05.md"
R_ETA_NARROWING = ROOT / "docs" / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
R_ETA_W2 = ROOT / "docs" / "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md"
DELTA_ETA_CHAIN = ROOT / "docs" / "KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md"
DEFECT_UNIT = ROOT / "docs" / "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md"
CYCLE_HOLONOMY = ROOT / "docs" / "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md"
CROSS_ARC = ROOT / "docs" / "ACPHILAMBDA_CROSS_ARC_UNIT_CLASSIFICATION_WIRING_2026-07-02.md"
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

CURRENT_SURFACE_INPUTS = {
    "FORM_LAYER_AND_K_ORBIT_AUTHORITY_ACCEPTED",
    "FINITE_FIXED_LOCUS_ARITHMETIC_ACCEPTED",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
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
        R_ETA_DECISION,
        H_CLASS_TARGET,
        H_CLASS_DECISION,
        H_UNIT_TARGET,
        H_UNIT_DECISION,
        K2_TARGET,
        K2_NO_GO,
        TWO_NINTHS_TARGET,
        TWO_NINTHS_NO_GO,
        PR5019_IMPACT,
        PR5020_IMPACT,
        PR5022_IMPACT,
        AC_R_ETA_CLUSTER,
        R_ETA_NARROWING,
        R_ETA_W2,
        DELTA_ETA_CHAIN,
        DEFECT_UNIT,
        CYCLE_HOLONOMY,
        CROSS_ARC,
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
        "Koide R-Eta Readout Retirement Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not ratify `R_ETA_READOUT_IDENTIFICATION_RETAINED`",
        "current retained, primitive, merged-PR, and open-PR surfaces do not",
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
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "merged `#5022` delta-eta chain R-eta supplied-premise audit repair",
        "ZERO_IMPORT_HYDROGEN_AC_R_ETA_UPSTREAM_CLUSTER_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "`89768b461c`/`e2d1dec095` occurrence/measure boundaries",
        "merged `#5020` Koide R-eta value-face registered-angle/exactness relocation",
        "merged `#5019` Koide `AC_phi_lambda` axiom-surface rebase",
        "`#5021` primitive-retirement review draft",
        "no primitive retirement and no registry edit",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad R-eta-retirement no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    full_inputs = set(R_ETA_RETIREMENT_INPUTS)
    audit.check("full R-eta retirement contract accepts handoff", closes_r_eta_retirement(full_inputs))
    for missing in sorted(R_ETA_RETIREMENT_INPUTS):
        reduced = set(R_ETA_RETIREMENT_INPUTS)
        reduced.remove(missing)
        audit.check(f"R-eta retirement fails without {missing}", not closes_r_eta_retirement(reduced))
    accepted_subsets = [subset for subset in all_subsets(R_ETA_RETIREMENT_INPUTS) if closes_r_eta_retirement(subset)]
    audit.check("only full R-eta retirement subset closes handoff", accepted_subsets == [full_inputs])
    audit.check("current surface inputs do not close R-eta retirement", not closes_r_eta_retirement(set(CURRENT_SURFACE_INPUTS)))

    consequence = {"R_ETA_READOUT_IDENTIFICATION_RETAINED"}
    audit.check("R-eta consequence alone does not close two-ninths subgate", not closes_two_ninths(consequence))
    audit.check("R-eta consequence alone does not close K2 exactness", not closes_k2(consequence))
    audit.check("R-eta consequence alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("R-eta consequence alone does not close hydrogen", not closes_hydrogen(consequence))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    r_eta_target = read(R_ETA_TARGET)
    r_eta_decision = read(R_ETA_DECISION)
    h_class_target = read(H_CLASS_TARGET)
    h_class_decision = read(H_CLASS_DECISION)
    h_unit_target = read(H_UNIT_TARGET)
    h_unit_decision = read(H_UNIT_DECISION)
    k2_target = read(K2_TARGET)
    k2_no_go = read(K2_NO_GO)
    two_ninths_target = read(TWO_NINTHS_TARGET)
    two_ninths_no_go = read(TWO_NINTHS_NO_GO)
    pr5019 = read(PR5019_IMPACT)
    pr5020 = read(PR5020_IMPACT)
    pr5022 = read(PR5022_IMPACT)
    ac_r_eta_cluster = read(AC_R_ETA_CLUSTER)
    narrowing = read(R_ETA_NARROWING)
    w2 = read(R_ETA_W2)
    chain = read(DELTA_ETA_CHAIN)
    defect = read(DEFECT_UNIT)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    tier_a = read(TIER_A_REGISTRY)
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    realized_text = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("R-eta target", r_eta_target),
        ("R-eta decision packet", r_eta_decision),
        ("K2 exactness target", k2_target),
        ("K2 exactness no-go", k2_no_go),
        ("two-ninths target", two_ninths_target),
        ("two-ninths no-go", two_ninths_no_go),
    ]:
        audit.check(
            f"{label} references R-eta retirement current no-go",
            NOTE.name in container and "R_ETA_READOUT_IDENTIFICATION_RETAINED" in container,
        )

    audit.check("h-class target remains one subinput", "R_ETA_H_CLASS_RETAINED" in h_class_target and "does not ratify" in h_class_target)
    audit.check("h-class decision remains one subinput", "R_ETA_H_CLASS_RETAINED" in h_class_decision and "does not ratify" in h_class_decision)
    audit.check("h-unit target remains one subinput", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in h_unit_target and "does not ratify" in h_unit_target)
    audit.check("h-unit decision remains one subinput", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in h_unit_decision and "does not ratify" in h_unit_decision)
    audit.check("#5019 impact remains premise hygiene", "premise-hygiene" in pr5019 or "premise hygiene" in pr5019)
    audit.check("#5020 impact keeps exactness residual open", "exactness remains open" in pr5020)
    audit.check("#5022 impact keeps R-eta supplied, not derived", "supplied" in pr5022 and "no retained R-eta derivation" in pr5022)
    audit.check(
        "AC R-eta cluster keeps readout retirement open",
        "No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`." in ac_r_eta_cluster
        and "No spending of landed-main `89768b461c` or `e2d1dec095` as K1/K2 closure." in ac_r_eta_cluster,
    )
    audit.check("narrowing note decomposes R-eta residual", "A_R-eta" in narrowing and "h-class" in narrowing and "h-unit" in narrowing)
    audit.check("W2 bridge leaves physical carrier/value open", "physical" in w2 and "A_R-eta" in w2)
    audit.check(
        "delta-eta chain uses R-eta conditionally",
        "conditional input" in chain and "readout identification" in chain and "2/9" in chain,
    )
    audit.check("defect unit obstruction blocks rescale shortcut", "rescale" in defect and "R-eta" in defect)

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
        "r_eta_h_unit_identity_radian_primitive",
        "phase_selector_primitive",
        "readout_bridge_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in primitive_nodes)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in primitive_nodes)
    audit.check("realized primitive supplies no value", "no state" in realized_text and "or value is supplied" in flat(realized_text))
    for excluded in ["mass ratio", "phase", "selector", "readout bridge", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open PR and non-claim boundaries")
    open_markers = [
        "`#5022` delta-eta chain R-eta supplied-premise audit repair | merged, audit success",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft, dirty",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | merged",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | merged",
        "`#5018`/`#5017` chirality/domain-wall stack | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "clean/dirty/check labels are not proof inputs",
    ]
    for marker in open_markers:
        audit.check(f"open PR marker present: {marker}", flat(marker) in note_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.",
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "landed-main `#4982`-`#4986`, or landed-main",
        "No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`, observed",
        "No derivation of K1 occupancy/counting, K3 physical species bridge, K4",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note derives R-eta",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
        "R_ETA_H_CLASS_RETAINED is supplied",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is supplied",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED is supplied",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This note claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
