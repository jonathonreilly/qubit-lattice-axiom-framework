#!/usr/bin/env python3
"""Verifier for the Koide R-eta h-unit identity-radian decision packet."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
H_UNIT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
H_CLASS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
TWO_NINTHS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
DEFECT_UNIT = ROOT / "docs" / "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md"
A1_RADIAN = ROOT / "docs" / "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md"
Z3_RADIAN = ROOT / "docs" / "KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md"
BRANNEN_CONVENTION = ROOT / "docs" / "BRANNEN_DELTA_SPECTRAL_ASYMMETRY_CONVENTION_ISOLATION_NOTE_2026-05-31.md"
PHASE_UNIT = ROOT / "docs" / "PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY_NOTE_2026-04-25.md"
CYCLE_HOLONOMY = ROOT / "docs" / "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


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


def closes_h_unit(inputs: set[str]) -> bool:
    return H_UNIT_INPUTS <= inputs


def closes_r_eta(inputs: set[str]) -> bool:
    return R_ETA_INPUTS <= inputs


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
        H_UNIT_TARGET,
        R_ETA_DECISION,
        R_ETA_TARGET,
        H_CLASS_TARGET,
        TWO_NINTHS_TARGET,
        K2_TARGET,
        PHYSICAL_ELECTRON,
        DEFECT_UNIT,
        A1_RADIAN,
        Z3_RADIAN,
        BRANNEN_CONVENTION,
        PHASE_UNIT,
        CYCLE_HOLONOMY,
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
        "Koide R-Eta H-Unit Identity-Radian Ratification Decision Packet",
        "decision packet / Koide R-eta h-unit import-retirement handoff",
        "does not ratify `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED",
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
        "No proper subset of those eleven contract inputs",
        "c = 1 <=> Phi = 2/3",
        "Phi = 2/3",
        "The primitive registry was checked",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is packaged as an eleven-input",
        "No-Go Discipline Gate",
        "broad h-unit-retained claim fails; narrowed h-unit decision",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(H_UNIT_INPUTS)
    audit.check("full h-unit decision contract accepts handoff", closes_h_unit(full_inputs))
    for missing in sorted(H_UNIT_INPUTS):
        reduced = set(H_UNIT_INPUTS)
        reduced.remove(missing)
        audit.check(f"h-unit decision fails without {missing}", not closes_h_unit(reduced))
    accepted_subsets = [subset for subset in all_subsets(H_UNIT_INPUTS) if closes_h_unit(subset)]
    audit.check("only full tested h-unit contract subset closes decision", accepted_subsets == [full_inputs])

    consequence = {"R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED"}
    audit.check("h-unit consequence alone does not close R-eta retirement", not closes_r_eta(consequence))
    audit.check("h-unit consequence alone does not close two-ninths subgate", not closes_two_ninths(consequence))
    audit.check("h-unit consequence alone does not close K2 exactness", not closes_k2(consequence))
    audit.check("h-unit consequence alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("h-unit consequence alone does not close hydrogen", not closes_hydrogen(consequence))

    support_only = {
        "DEFECT_IDENTITY_UNIT_NORMAL_FORM_ACCEPTED",
        "ANGLE_SIDE_RIGIDITY_ACCEPTED",
        "TYPE_B_TO_RADIAN_RESIDUAL_ALIGNMENT_ACCEPTED",
    }
    audit.check("support inputs alone do not close h-unit", not closes_h_unit(support_only))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    h_unit_target = read(H_UNIT_TARGET)
    r_eta_decision = read(R_ETA_DECISION)
    r_eta_target = read(R_ETA_TARGET)
    h_class = read(H_CLASS_TARGET)
    two_ninths = read(TWO_NINTHS_TARGET)
    k2 = read(K2_TARGET)
    physical_electron = read(PHYSICAL_ELECTRON)
    defect_unit = read(DEFECT_UNIT)
    a1_radian = read(A1_RADIAN)
    z3_radian = read(Z3_RADIAN)
    brannen = read(BRANNEN_CONVENTION)
    phase_unit = read(PHASE_UNIT)
    cycle = read(CYCLE_HOLONOMY)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    tier_a = read(TIER_A_REGISTRY)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
        ("R-eta decision packet", r_eta_decision),
    ]:
        audit.check(
            f"{label} references h-unit decision packet",
            NOTE.name in container and "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in container,
        )

    audit.check("h-unit target names same eleven-input contract", H_UNIT_INPUTS <= set(h_unit_target.split()))
    audit.check("R-eta target consumes h-unit as one subinput", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in r_eta_target)
    audit.check(
        "h-class target stays independent",
        "R_ETA_H_CLASS_RETAINED" in h_class
        and "does not supply `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`" in h_class,
    )
    audit.check("two-ninths target remains downstream", "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in two_ninths)
    audit.check("K2 target remains downstream", "K2_R_ETA_EXACTNESS_RETAINED" in k2)
    audit.check("physical electron packet remains downstream", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in physical_electron)

    audit.check("defect-unit note derives normal form", "I_c(R) = c * |R| * L" in defect_unit)
    audit.check(
        "defect-unit note blocks homogeneous c=1 route",
        "no derivation drawn from this scanned surface can single out" in flat(defect_unit),
    )
    audit.check("defect-unit note says count pins wrong member", "c = u / L = 1 / (2/9) = 9/2" in defect_unit)
    audit.check("cycle holonomy note states equivalent coordinate", "c = 1  <=>  Phi = S_sum = 2/3" in cycle)
    audit.check("cycle holonomy note does not derive value", "No derivation is supplied for `Phi = 2/3`." in cycle)
    audit.check("A1 radian bridge keeps Type-B primitive open", "TYPE_B_TO_RADIAN_IDENTIFICATION_REMAINS_PRIMITIVE=TRUE" in a1_radian)
    audit.check("Z3 radian bridge is source path", "KOIDE_Z3_QUBIT_RADIAN_BRIDGE" in Z3_RADIAN.name and len(z3_radian) > 0)
    audit.check("Brannen convention source is present", "2/9" in brannen and len(brannen) > 0)
    audit.check("phase-unit source is present", "U(1)" in phase_unit or "phase" in phase_unit)
    audit.check("Tier-A registry still names R-eta admission", "R-eta" in tier_a and "density-read-as-angle" in tier_a)

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "r_eta_h_unit_primitive",
        "identity_radian_primitive",
        "phase_selector_primitive",
        "delta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for forbidden_grant in ["mass ratio", "selector", "readout bridge", "empirical fit"]:
        audit.check(f"primitive notes exclude {forbidden_grant}", forbidden_grant in primitive_text)

    section("Non-claim boundaries")
    explicit_nonclaims = [
        "No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.",
        "No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.",
        "No derivation of `c = 1` from Record additivity, count normalization, or",
        "No derivation of `Phi = 2/3`.",
        "No derivation of R-eta from the current retained inventory alone.",
        "No derivation of `delta = 2/9` as a retained physical phase.",
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`, observed",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_claims = [
        "This packet ratifies h-unit",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is supplied",
        "R_ETA_H_CLASS_RETAINED is supplied",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
        "Phi = 2/3 is derived",
        "c = 1 is derived",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This packet claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden_claims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
