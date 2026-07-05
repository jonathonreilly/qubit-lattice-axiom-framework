#!/usr/bin/env python3
"""Verifier for the hydrogen-facing Koide R-eta readout-retirement target."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PR5022_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5020_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
K2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
TWO_NINTHS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
TWO_NINTHS_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
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

R_ETA_SUPPLIES_TO_TWO_NINTHS = {
    "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
    "RADIAN_READOUT_LICENSE_RETAINED",
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


def closes_two_ninths_subgate(inputs: set[str]) -> bool:
    return TWO_NINTHS_SUBGATE_INPUTS <= inputs


def closes_k2_exactness(inputs: set[str]) -> bool:
    return K2_EXACTNESS_INPUTS <= inputs


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
        PR5022_IMPACT,
        PR5020_IMPACT,
        K2_TARGET,
        K2_NO_GO,
        TWO_NINTHS_TARGET,
        TWO_NINTHS_NO_GO,
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
        "Koide R-Eta Readout Retirement Target Discriminator",
        "target discriminator / Koide R-eta import-retirement handoff",
        "does not ratify `R_ETA_READOUT_IDENTIFICATION_RETAINED`",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED",
        "A_R-eta = h-class + h-unit",
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
        "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
        "RADIAN_READOUT_LICENSE_RETAINED",
        "The primitive registry was checked",
        "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md",
        "KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md",
        "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md",
        "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md",
        "ACPHILAMBDA_CROSS_ARC_UNIT_CLASSIFICATION_WIRING_2026-07-02.md",
        "No-Go Discipline Gate",
        "broad R-eta-retained claim fails; narrowed readout-retirement",
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
    audit.check(
        "R-eta target supplies only two proof inputs to two-ninths target",
        R_ETA_SUPPLIES_TO_TWO_NINTHS < TWO_NINTHS_SUBGATE_INPUTS,
    )
    audit.check(
        "R-eta supplied inputs alone do not close two-ninths subgate",
        not closes_two_ninths_subgate(set(R_ETA_SUPPLIES_TO_TWO_NINTHS)),
    )
    audit.check(
        "R-eta handoff alone does not close K2 exactness",
        not closes_k2_exactness({"R_ETA_READOUT_IDENTIFICATION_RETAINED"}),
    )
    audit.check(
        "R-eta handoff alone does not close electron mass",
        not closes_electron_mass({"R_ETA_READOUT_IDENTIFICATION_RETAINED"}),
    )
    audit.check(
        "R-eta handoff alone does not close hydrogen",
        not closes_hydrogen({"R_ETA_READOUT_IDENTIFICATION_RETAINED"}),
    )

    section("Authority and source-boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    pr5022 = read(PR5022_IMPACT)
    pr5020 = read(PR5020_IMPACT)
    k2_target = read(K2_TARGET)
    two_ninths_target = read(TWO_NINTHS_TARGET)
    r_eta_narrowing = read(R_ETA_NARROWING)
    r_eta_w2 = read(R_ETA_W2)
    delta_eta_chain = read(DELTA_ETA_CHAIN)
    defect_unit = read(DEFECT_UNIT)
    cycle_holonomy = read(CYCLE_HOLONOMY)
    cross_arc = read(CROSS_ARC)
    physical_electron = read(PHYSICAL_ELECTRON)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    tier_a_text = read(TIER_A_REGISTRY)
    realized_text = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
        ("K2 exactness target", k2_target),
        ("two-ninths target", two_ninths_target),
    ]:
        audit.check(
            f"{label} references R-eta retirement target",
            NOTE.name in container and "R_ETA_READOUT_IDENTIFICATION_RETAINED" in container,
        )

    audit.check(
        "#5022 impact keeps supplied premise conditional",
        "supplied premise" in pr5022
        and (
            "no retained R-eta derivation" in pr5022
            or "no retained theorem deriving R-eta" in pr5022
        ),
    )
    audit.check("#5020 impact keeps exactness residual open", "exactness remains open" in pr5020)
    audit.check("R-eta narrowing keeps A_R-eta admitted", "`A_R-eta` remains genuinely admitted" in r_eta_narrowing)
    audit.check("R-eta narrowing splits h-class and h-unit", "h-class" in r_eta_narrowing and "h-unit" in r_eta_narrowing)
    audit.check("W2 bridge leaves A_R-eta unchanged", "The value atom `A_R-eta` remains admitted" in r_eta_w2)
    audit.check("delta-eta chain keeps R-eta conditional", "R-η remains the explicit readout identification" in delta_eta_chain or "R-eta remains the explicit readout identification" in delta_eta_chain)
    audit.check("defect unit consolidates unit selector with R-eta", "W_defect_identity_unit == R-eta" in defect_unit or "R-eta sub-admission" in defect_unit)
    audit.check(
        "cycle holonomy keeps value wall on R-eta",
        "R-eta" in cycle_holonomy
        and (
            "W_cycle_holonomy_value" in cycle_holonomy
            or "R-eta junction coefficient" in cycle_holonomy
        ),
    )
    audit.check("cross-arc wiring does not derive R-eta", "This note does not derive R-eta." in cross_arc)
    audit.check("physical electron packet remains downstream", "K2 value-face progress only" in physical_electron and "no delta exactness theorem" in physical_electron)
    audit.check("Tier-A registry names R-eta sub-admission", "delta readout identification R-eta" in tier_a_text)
    audit.check("realized-state primitive supplies no value", "no state" in realized_text and "or value is supplied" in flat(realized_text))

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
        "No adoption or landing claim for PR `#5020`, PR `#5021`, or PR `#5022`.",
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
