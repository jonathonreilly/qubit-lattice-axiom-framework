#!/usr/bin/env python3
"""Verifier for the hydrogen-facing Koide R-eta h-class target."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
R_ETA_RETIREMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
H_UNIT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA_NARROWING = ROOT / "docs" / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
R_ETA_W2 = ROOT / "docs" / "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md"
FIXED_LOCUS = ROOT / "docs" / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
FLAVOR_ASYMMETRY = ROOT / "docs" / "FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md"
OPERATOR_DENSITY = ROOT / "docs" / "FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md"
AMBIENT_FACE = ROOT / "docs" / "ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md"
K_EVEN_PATTERN = ROOT / "docs" / "ACPHILAMBDA_K_EVEN_REGISTRATION_CORRECTION_REGISTERED_PATTERN_2026-07-02.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


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


def closes_h_class(inputs: set[str]) -> bool:
    return H_CLASS_INPUTS <= inputs


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
        R_ETA_RETIREMENT,
        H_UNIT_TARGET,
        R_ETA_NARROWING,
        R_ETA_W2,
        FIXED_LOCUS,
        FLAVOR_ASYMMETRY,
        OPERATOR_DENSITY,
        AMBIENT_FACE,
        K_EVEN_PATTERN,
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
        "Koide R-Eta H-Class Fixed-Locus Target Discriminator",
        "target discriminator / Koide R-eta h-class import-retirement handoff",
        "does not ratify `R_ETA_H_CLASS_RETAINED`",
        "R_ETA_H_CLASS_RETAINED",
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
        "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md",
        "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md",
        "FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md",
        "ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad h-class-retained claim fails; narrowed fixed-locus",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    full_inputs = set(H_CLASS_INPUTS)
    audit.check("full h-class contract accepts handoff", closes_h_class(full_inputs))
    for missing in sorted(H_CLASS_INPUTS):
        reduced = set(H_CLASS_INPUTS)
        reduced.remove(missing)
        audit.check(f"h-class handoff fails without {missing}", not closes_h_class(reduced))
    accepted_subsets = [subset for subset in all_subsets(H_CLASS_INPUTS) if closes_h_class(subset)]
    audit.check("only full h-class subset closes handoff", accepted_subsets == [full_inputs])
    audit.check(
        "h-class supplies one proper input to R-eta retirement",
        {"R_ETA_H_CLASS_RETAINED"} < R_ETA_RETIREMENT_INPUTS,
    )
    audit.check(
        "h-class handoff alone does not close R-eta retirement",
        not closes_r_eta_retirement({"R_ETA_H_CLASS_RETAINED"}),
    )
    audit.check(
        "h-class handoff alone does not close two-ninths subgate",
        not closes_two_ninths_subgate({"R_ETA_H_CLASS_RETAINED"}),
    )
    audit.check(
        "h-class handoff alone does not close K2 exactness",
        not closes_k2_exactness({"R_ETA_H_CLASS_RETAINED"}),
    )
    audit.check(
        "h-class handoff alone does not close electron mass",
        not closes_electron_mass({"R_ETA_H_CLASS_RETAINED"}),
    )
    audit.check(
        "h-class handoff alone does not close hydrogen",
        not closes_hydrogen({"R_ETA_H_CLASS_RETAINED"}),
    )

    section("Authority and source-boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    r_eta_retirement = read(R_ETA_RETIREMENT)
    h_unit_target = read(H_UNIT_TARGET)
    r_eta_narrowing = read(R_ETA_NARROWING)
    r_eta_w2 = read(R_ETA_W2)
    fixed_locus = read(FIXED_LOCUS)
    flavor_asymmetry = read(FLAVOR_ASYMMETRY)
    operator_density = read(OPERATOR_DENSITY)
    ambient_face = read(AMBIENT_FACE)
    k_even_pattern = read(K_EVEN_PATTERN)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    tier_a_text = read(TIER_A_REGISTRY)
    realized_text = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
        ("R-eta retirement target", r_eta_retirement),
    ]:
        audit.check(
            f"{label} references h-class target",
            NOTE.name in container and "R_ETA_H_CLASS_RETAINED" in container,
        )

    audit.check("h-unit target stays independent", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in h_unit_target)
    audit.check("R-eta narrowing splits h-class and h-unit", "h-class" in r_eta_narrowing and "h-unit" in r_eta_narrowing)
    audit.check("R-eta narrowing keeps h-class admitted", "h-class" in r_eta_narrowing and "neither derived here" in r_eta_narrowing)
    audit.check("W2 bridge leaves physical carrier and value open", "physical carrier realization" in r_eta_w2 and "The value atom `A_R-eta` remains admitted" in r_eta_w2)
    audit.check(
        "fixed-locus row forces weights and density",
        "weights `(1,2)`" in fixed_locus and "local density `2/9`" in fixed_locus,
    )
    audit.check("fixed-locus row excludes physical readout", "physical single-summand readout" in fixed_locus)
    audit.check("flavor asymmetry keeps physical readout gate", "forced local density" in flavor_asymmetry and "Physical readout is the one remaining gate" in flavor_asymmetry)
    audit.check("operator density keeps physical readout bridge open", "does not prove the physical readout bridge" in operator_density and "local fixed-point density" in operator_density)
    audit.check("ambient face keeps physical readout open", "fixed-locus density acquires its ambient face" in ambient_face and "No physical-normalization selection is supplied" in ambient_face)
    audit.check("K-even pattern keeps value as registered data", "value is realized-state registered data" in k_even_pattern and "R-eta sub-admission" in k_even_pattern)
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
        "r_eta_h_class_primitive",
        "single_fixed_point_readout_primitive",
        "physical_carrier_context_primitive",
        "r_eta_h_unit_identity_radian_primitive",
        "r_eta_readout_identification_primitive",
        "delta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in primitive_nodes)
    for excluded in ["selector", "readout bridge", "normalization", "value", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_nonclaims = [
        "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.",
        "No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.",
        "No derivation of R-eta from the current retained inventory alone.",
        "No derivation of `delta = 2/9` as a retained physical phase.",
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`, observed",
        "No derivation of K1 occupancy/counting, K3 physical species bridge, K4",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note derives R-eta",
        "R_ETA_H_CLASS_RETAINED is supplied",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is supplied",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
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
