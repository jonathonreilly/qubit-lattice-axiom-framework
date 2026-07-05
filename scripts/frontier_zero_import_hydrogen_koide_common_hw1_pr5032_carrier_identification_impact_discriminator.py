#!/usr/bin/env python3
"""Verifier for the hydrogen-facing PR #5032 common hw1 carrier impact note."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_COMMON_HW1_PR5032_CARRIER_IDENTIFICATION_IMPACT_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
HW1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
HW1_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
HW1_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PHYSICAL_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PHYSICAL_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
H_CLASS = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
K2 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
MOMENTUM_TYPE = ROOT / "docs" / "FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md"
HAMMING = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md"
AC_LAMBDA = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP4_AC_LAMBDA_SIMULTANEOUS_DIAGONALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md"
SPECIES_REDUCTION = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


PR5032_CONTEXT_INPUTS = {
    "PR5032_MERGED_MAIN_CONTEXT",
    "COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED",
    "HAMMING_AC_LAMBDA_C3_REPRESENTATIVE_IDENTIFIED",
    "SPECIES_REDUCTION_NONIDENTIFICATION_PRESERVED",
    "NO_DOWNSTREAM_RETAINED_STATUS_SPEND",
}

HW1_INPUTS = {
    "HW1_PHYSICAL_GENERATION_LOCUS_TEXT_LOCK",
    "MOMENTUM_TYPE_THEOREM_ACCEPTED",
    "STAGGERED_KS_REALIZATION_SURFACE_ACCEPTED",
    "K1_FLUX_SELECTOR_WITHIN_SURFACE_ACCEPTED",
    "HW1_C3_TRIPLET_ALGEBRA_ACCEPTED",
    "COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED",
    "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
    "NO_SPECIES_LABEL_BIJECTION_INPUT",
    "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CHARGED_CARRIER_INPUTS = {
    "CHARGED_LEPTON_CARRIER_REALIZATION_TEXT_LOCK",
    "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
    "SUPPLIED_ACPHILAMBDA_R_ETA_CONTEXT_LOCK",
    "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

PHYSICAL_CARRIER_INPUTS = {
    "PHYSICAL_CARRIER_CONTEXT_TEXT_LOCK",
    "SUPPLIED_C3_CIRCULANT_CONTEXT_ACCEPTED",
    "RECORD_REGISTRABILITY_CONTEXT_ACCEPTED",
    "REDUCED_CARRIER_OBSTRUCTION_ACCOUNTED",
    "CARRIER_GATE_COLLAPSE_MAP_ACCEPTED",
    "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED",
    "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
    "NO_H_UNIT_OR_R_ETA_VALUE_INPUT",
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


def closes_pr5032_context(inputs: set[str]) -> bool:
    return PR5032_CONTEXT_INPUTS <= inputs


def closes_hw1_locus(inputs: set[str]) -> bool:
    return HW1_INPUTS <= inputs


def closes_charged_carrier(inputs: set[str]) -> bool:
    return CHARGED_CARRIER_INPUTS <= inputs


def closes_physical_carrier(inputs: set[str]) -> bool:
    return PHYSICAL_CARRIER_INPUTS <= inputs


def closes_h_class(inputs: set[str]) -> bool:
    return H_CLASS_INPUTS <= inputs


def closes_r_eta(inputs: set[str]) -> bool:
    return R_ETA_INPUTS <= inputs


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
        HW1_TARGET,
        HW1_DECISION,
        HW1_CURRENT,
        PHYSICAL_TARGET,
        PHYSICAL_DECISION,
        PHYSICAL_CURRENT,
        H_CLASS,
        R_ETA,
        K2,
        MOMENTUM_TYPE,
        HAMMING,
        AC_LAMBDA,
        SPECIES_REDUCTION,
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

    section("Required note content")
    required_phrases = [
        "Koide Common hw1 PR #5032 Carrier-Identification Impact Discriminator",
        "merged-PR impact discriminator / common `hw=1` carrier-identification boundary",
        "records PR `#5032` as merged with audit",
        "0f827c303fd15ec2ccdb5a4494c0c79bfb51c4f8",
        "PR5032_COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_CONTEXT",
        "COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED",
        "the common finite representative identifying Hamming hw=1, AC_lambda, and",
        "not the physical charged-lepton generation-locus theorem",
        "does not identify the species-reduction surface",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad `hw=1`/carrier/hydrogen closure claim fails; narrowed",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    pr5032_inputs = set(PR5032_CONTEXT_INPUTS)
    audit.check("#5032 context predicate accepts all support inputs", closes_pr5032_context(pr5032_inputs))
    audit.check("#5032 context alone does not close hw1 locus", not closes_hw1_locus(pr5032_inputs))
    audit.check("#5032 context alone does not close charged carrier theorem", not closes_charged_carrier(pr5032_inputs))
    audit.check("#5032 context alone does not close physical carrier context", not closes_physical_carrier(pr5032_inputs))
    audit.check("#5032 context alone does not close h-class", not closes_h_class(pr5032_inputs))
    audit.check("#5032 context alone does not close R-eta", not closes_r_eta(pr5032_inputs))
    audit.check("#5032 context alone does not close K2", not closes_k2(pr5032_inputs))
    audit.check("#5032 context alone does not close electron mass", not closes_electron_mass(pr5032_inputs))
    audit.check("#5032 context alone does not close hydrogen", not closes_hydrogen(pr5032_inputs))
    audit.check("full hw1 predicate closes only with the new common-carrier input present", closes_hw1_locus(set(HW1_INPUTS)))
    without_common = set(HW1_INPUTS)
    without_common.remove("COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED")
    audit.check("hw1 predicate fails without common carrier input", not closes_hw1_locus(without_common))

    section("Wiring and authority boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    hw1_target = read(HW1_TARGET)
    hw1_decision = read(HW1_DECISION)
    hw1_current = read(HW1_CURRENT)
    physical_target = read(PHYSICAL_TARGET)
    physical_decision = read(PHYSICAL_DECISION)
    physical_current = read(PHYSICAL_CURRENT)
    h_class = read(H_CLASS)
    r_eta = read(R_ETA)
    k2 = read(K2)
    momentum = read(MOMENTUM_TYPE)
    hamming = read(HAMMING)
    ac_lambda = read(AC_LAMBDA)
    species = read(SPECIES_REDUCTION)
    registry_text = read(REGISTRY)
    registry = json.loads(registry_text)
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("HW1 target", hw1_target),
        ("HW1 decision", hw1_decision),
        ("HW1 current no-go", hw1_current),
        ("physical carrier target", physical_target),
        ("physical carrier decision", physical_decision),
        ("physical carrier current no-go", physical_current),
    ]:
        audit.check(
            f"{label} references #5032 impact note",
            NOTE.name in container and "#5032" in container,
        )

    for label, container in [
        ("HW1 target", hw1_target),
        ("HW1 decision", hw1_decision),
        ("HW1 current no-go", hw1_current),
    ]:
        audit.check(
            f"{label} includes common carrier contract input",
            "COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED" in container
            and "all fifteen" in container,
        )

    audit.check("h-class remains downstream", "R_ETA_H_CLASS_RETAINED" in h_class)
    audit.check("R-eta remains downstream", "R_ETA_READOUT_IDENTIFICATION_RETAINED" in r_eta)
    audit.check("K2 remains downstream", "K2_R_ETA_EXACTNESS_RETAINED" in k2)
    audit.check("momentum type records the concrete representative", "2 x 2 x 2" in momentum and "hw=1" in momentum)
    audit.check(
        "Hamming note supplies finite orbit algebra",
        "(1, 3, 3, 1)" in hamming and "Hamming weight" in hamming,
    )
    audit.check(
        "AC_lambda note disclaims physical carrier identification",
        "**no** claim" in ac_lambda
        and "physical lattice" in ac_lambda
        and "3-dim complex space" in ac_lambda,
    )
    audit.check(
        "species reduction keeps reduction realization open",
        "is **not** forced" in species and "is **not** the same as a derivation" in species,
    )

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive node present: {node_name}", node_name in registry["nodes"])
    for absent in [
        "common_hw1_carrier_primitive",
        "hw1_physical_generation_locus_primitive",
        "physical_carrier_context_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered shortcut primitive: {absent}", absent not in registry_text)
    for excluded in ["selector", "readout bridge", "state-selection rule", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_nonclaims = [
        "No downstream retained-theorem verdict from merged PR `#5032`.",
        "No retained-theorem verdict or status change.",
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "No derivation or ratification of `CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.",
        "No species-reduction realization, no `e`/`mu`/`tau` labeling convention, no",
        "No derivation or ratification of K1 occupancy/counting, K3 physical species",
        "No derivation of `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note ratifies #5032",
        "COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED supplies HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED is supplied",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED is supplied",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
        "hydrogen retained theorem",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
