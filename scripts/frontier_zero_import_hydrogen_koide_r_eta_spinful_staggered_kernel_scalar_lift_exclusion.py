#!/usr/bin/env python3
"""Verifier for the Koide R-eta spinful kernel scalar-lift lane."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SIGMA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md"
SIGMA_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SIGMA_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
TRIVIAL_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
TRIVIAL_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
TRIVIAL_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
KS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
KS_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PARENT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
PARENT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PARENT_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
HW1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_CARRIER_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
MATTER_ATTACHMENT = ROOT / "docs" / "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md"
CARRIER_ATTACHMENT = ROOT / "docs" / "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md"
CARRIER_RUNNER = ROOT / "scripts" / "carrier_attachment_chirality_gate_consolidation_runner.py"
KS_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
GRASSMANN_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md"
KINETIC_CLASS = ROOT / "docs" / "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
CHIRALITY_PARITY = ROOT / "docs" / "STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md"
REALIZATION_GATE = ROOT / "docs" / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


SPINFUL_INPUTS = {
    "SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TEXT_LOCK",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "SCALAR_KERNEL_COMPATIBILITY_ACCEPTED",
    "STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED",
    "KS_PHASE_FORCING_SURFACE_ACCEPTED",
    "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED",
    "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED",
    "NO_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_INPUT",
    "NO_KS_ROUTE_CLOSURE_INPUT",
    "NO_PARENT_BRIDGE_OR_HW1_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_SURFACE_INPUTS = SPINFUL_INPUTS - {
    "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED",
    "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

KS_ROUTE_INPUTS = {
    "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TEXT_LOCK",
    "MATTER_ATTACHMENT_KS_REDUCTION_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "KS_PHASE_FORCING_SURFACE_ACCEPTED",
    "GRASSMANN_CAR_SURFACE_ACCEPTED",
    "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
    "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
    "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
    "NO_ELEMENTARY_STATE_LAW_INPUT",
    "NO_HW1_OR_BRIDGE_CLOSURE_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

FIXED_PARENT_BRIDGE_INPUTS = {
    "PHYSICAL_MATTER_STATE_LAW_BRIDGE_TEXT_LOCK",
    "OPERATOR_FRAME_MERGER_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "NATIVE_D_SPIN_BLINDNESS_ACCEPTED",
    "KS_SCALARIZATION_SURFACE_ACCEPTED",
    "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
    "NO_HW1_LOCUS_OR_CARRIER_CLOSURE_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

PARENT_ROUTE_INPUTS = {
    "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
    "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED",
}

HW1_INPUTS = {
    "HW1_PHYSICAL_GENERATION_LOCUS_TEXT_LOCK",
    "MOMENTUM_TYPE_THEOREM_ACCEPTED",
    "STAGGERED_KS_REALIZATION_SURFACE_ACCEPTED",
    "K1_FLUX_SELECTOR_WITHIN_SURFACE_ACCEPTED",
    "HW1_C3_TRIPLET_ALGEBRA_ACCEPTED",
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


def closes_spinful_exclusion(inputs: set[str]) -> bool:
    return SPINFUL_INPUTS <= inputs


def closes_ks_route(inputs: set[str]) -> bool:
    return KS_ROUTE_INPUTS <= inputs


def closes_parent_bridge(inputs: set[str]) -> bool:
    return FIXED_PARENT_BRIDGE_INPUTS <= inputs and bool(PARENT_ROUTE_INPUTS & inputs)


def closes_hw1(inputs: set[str]) -> bool:
    return HW1_INPUTS <= inputs


def closes_charged_carrier(inputs: set[str]) -> bool:
    return CHARGED_CARRIER_INPUTS <= inputs


def closes_physical_carrier(inputs: set[str]) -> bool:
    return PHYSICAL_CARRIER_INPUTS <= inputs


def closes_r_eta(inputs: set[str]) -> bool:
    return R_ETA_INPUTS <= inputs


def closes_electron_mass(inputs: set[str]) -> bool:
    return ELECTRON_MASS_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def finite_spinful_kernel_checks(audit: Audit) -> None:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    sigma = [sx, sy, sz]
    i2 = np.eye(2, dtype=complex)

    h_scalar = 1.7 * i2
    scalar_commutes = all(np.allclose(h_scalar @ s, s @ h_scalar) for s in sigma)

    p = np.array([1.0, 0.0, 0.0])
    spinful_kernel = sum(p[i] * sigma[i] for i in range(3))
    spinful_noncentral = any(not np.allclose(spinful_kernel @ s, s @ spinful_kernel) for s in sigma)

    theta = np.pi / 2
    uz = np.cos(theta / 2) * i2 - 1j * np.sin(theta / 2) * sz
    faithful_rotated = uz @ sx @ uz.conj().T
    scalar_lift_rotated = i2 @ sx @ i2

    audit.check("scalar mass-shell kernel commutes with Pauli operators", scalar_commutes)
    audit.check("spinful sigma.p kernel is noncentral", spinful_noncentral)
    audit.check("faithful z-rotation sends sigma_x to sigma_y", np.allclose(faithful_rotated, sy))
    audit.check("trivial scalar lift fails the spinful covariance test", not np.allclose(scalar_lift_rotated, sy))
    audit.check("scalar kernel remains invariant under faithful and trivial lifts", np.allclose(uz @ h_scalar @ uz.conj().T, h_scalar) and np.allclose(i2 @ h_scalar @ i2, h_scalar))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        TARGET,
        DECISION,
        CURRENT,
        SIGMA_TARGET,
        SIGMA_DECISION,
        SIGMA_CURRENT,
        TRIVIAL_TARGET,
        TRIVIAL_DECISION,
        TRIVIAL_CURRENT,
        KS_TARGET,
        KS_DECISION,
        KS_CURRENT,
        GOAL,
        KOIDE_FIREWALL,
        PARENT_TARGET,
        PARENT_DECISION,
        PARENT_CURRENT,
        HW1_TARGET,
        PHYSICAL_CARRIER_TARGET,
        MATTER_ATTACHMENT,
        CARRIER_ATTACHMENT,
        CARRIER_RUNNER,
        KS_FORCING,
        GRASSMANN_FORCING,
        KINETIC_CLASS,
        CHIRALITY_PARITY,
        REALIZATION_GATE,
        PRIMITIVE_REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    target = read(TARGET)
    decision = read(DECISION)
    current = read(CURRENT)
    packet = "\n".join([target, decision, current])
    packet_flat = flat(packet)

    section("Required packet content")
    required_phrases = [
        "Koide R-Eta Spinful Staggered Kernel Scalar-Lift Exclusion Target Discriminator",
        "Koide R-Eta Spinful Staggered Kernel Scalar-Lift Exclusion Ratification Decision Packet",
        "Koide R-Eta Spinful Staggered Kernel Scalar-Lift Exclusion Current-Surface No-Go",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TEXT_LOCK",
        "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
        "SCALAR_KERNEL_COMPATIBILITY_ACCEPTED",
        "STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED",
        "KS_PHASE_FORCING_SURFACE_ACCEPTED",
        "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "NO_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_INPUT",
        "NO_KS_ROUTE_CLOSURE_INPUT",
        "NO_PARENT_BRIDGE_OR_HW1_INPUT",
        "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md",
        "scripts/carrier_attachment_chirality_gate_consolidation_runner.py",
        "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md",
        "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md",
        "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md",
        "STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md",
        "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
        "merged `#5023`",
        "merged `#5024`",
        "open `#5021`",
        "merged `#5026`",
        "open `#5014`",
        "open `#5017`",
        "open `#5018`",
        "The approved primitive registry was checked",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in packet_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in packet)

    section("Predicate checks")
    full_route = set(SPINFUL_INPUTS)
    audit.check("full scalar-lift-exclusion contract closes target", closes_spinful_exclusion(full_route))
    audit.check("current surface does not close scalar-lift-exclusion target", not closes_spinful_exclusion(CURRENT_SURFACE_INPUTS))

    for missing in sorted(SPINFUL_INPUTS):
        reduced = set(full_route)
        reduced.remove(missing)
        audit.check(f"scalar-lift-exclusion contract fails without input {missing}", not closes_spinful_exclusion(reduced))

    accepted_subsets = [subset for subset in all_subsets(SPINFUL_INPUTS) if closes_spinful_exclusion(subset)]
    audit.check("only one minimal full scalar-lift-exclusion subset closes", accepted_subsets == [SPINFUL_INPUTS])

    spinful_consequence = {"SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED"}
    ks_with_spinful = set(KS_ROUTE_INPUTS)
    ks_without_action = ks_with_spinful - {"KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED"}
    audit.check("spinful consequence alone does not close KS route", not closes_ks_route(spinful_consequence))
    audit.check("spinful consequence plus full KS inputs closes KS route", closes_ks_route(ks_with_spinful))
    audit.check("spinful consequence cannot close KS route without KS action law", not closes_ks_route(ks_without_action))
    audit.check("spinful consequence alone does not close parent bridge", not closes_parent_bridge(spinful_consequence))
    audit.check("spinful consequence alone does not close HW1", not closes_hw1(spinful_consequence))
    audit.check("spinful consequence alone does not close charged carrier theorem", not closes_charged_carrier(spinful_consequence))
    audit.check("spinful consequence alone does not close physical carrier context", not closes_physical_carrier(spinful_consequence))
    audit.check("spinful consequence alone does not close R-eta", not closes_r_eta(spinful_consequence))
    audit.check("spinful consequence alone does not close electron mass", not closes_electron_mass(spinful_consequence))
    audit.check("spinful consequence alone does not close hydrogen", not closes_hydrogen(spinful_consequence))

    ks_consequence = {"KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED"}
    parent_with_ks = set(FIXED_PARENT_BRIDGE_INPUTS) | ks_consequence
    audit.check("KS consequence alone does not close parent bridge", not closes_parent_bridge(ks_consequence))
    audit.check("KS consequence can feed parent bridge with parent fixed inputs", closes_parent_bridge(parent_with_ks))
    audit.check("KS consequence alone does not close hydrogen", not closes_hydrogen(ks_consequence))

    section("Finite scalar-vs-spinful matrix checks")
    finite_spinful_kernel_checks(audit)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    ks_target = read(KS_TARGET)
    ks_decision = read(KS_DECISION)
    ks_current = read(KS_CURRENT)
    ks_packet = "\n".join([ks_target, ks_decision, ks_current])
    parent_packet = "\n".join([read(PARENT_TARGET), read(PARENT_DECISION), read(PARENT_CURRENT)])
    matter_attachment = read(MATTER_ATTACHMENT)
    carrier_attachment = read(CARRIER_ATTACHMENT)
    carrier_runner = read(CARRIER_RUNNER)
    ks_forcing = read(KS_FORCING)
    grassmann_forcing = read(GRASSMANN_FORCING)
    kinetic_class = read(KINETIC_CLASS)
    chirality_parity = read(CHIRALITY_PARITY)
    realization_gate = read(REALIZATION_GATE)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("KS target", ks_target),
        ("KS decision", ks_decision),
        ("KS current no-go", ks_current),
    ]:
        audit.check(
            f"{label} references spinful scalar-lift lane",
            TARGET.name in container
            and DECISION.name in container
            and CURRENT.name in container
            and "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED" in container,
        )

    for label, container in [
        ("spinful target", target),
        ("spinful decision", decision),
        ("spinful current no-go", current),
        ("goal packet", goal),
        ("Koide firewall", firewall),
    ]:
        audit.check(
            f"{label} references sigma-dot-p child lane",
            SIGMA_TARGET.name in container
            and SIGMA_DECISION.name in container
            and SIGMA_CURRENT.name in container
            and "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED" in container,
        )

    for label, container in [
        ("spinful target", target),
        ("spinful decision", decision),
        ("spinful current no-go", current),
        ("goal packet", goal),
        ("Koide firewall", firewall),
    ]:
        audit.check(
            f"{label} references trivial scalar-lift child lane",
            TRIVIAL_TARGET.name in container
            and TRIVIAL_DECISION.name in container
            and TRIVIAL_CURRENT.name in container
            and "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED" in container,
        )

    audit.check("spinful packet references KS target", KS_TARGET.name in packet)
    audit.check("KS packet still names KS child theorem", "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED" in ks_packet)
    audit.check("parent packet still names physical matter bridge", "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED" in parent_packet)
    audit.check("HW1 target still consumes parent bridge only", "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED" in read(HW1_TARGET))
    audit.check("physical carrier target still keeps charged carrier downstream", "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED" in read(PHYSICAL_CARRIER_TARGET))

    matter_flat = flat(matter_attachment)
    carrier_flat = flat(carrier_attachment)
    carrier_runner_flat = flat(carrier_runner)
    ks_flat = flat(ks_forcing)
    grassmann_flat = flat(grassmann_forcing)
    kinetic_flat = flat(kinetic_class)
    chirality_flat = flat(chirality_parity)
    realization_flat = flat(realization_gate)

    audit.check(
        "matter attachment localizes KS state-law residual",
        "unless a KS-to-physical-state-law bridge or an elementary state-law theorem is supplied" in matter_flat
        and "physical matter-state law still requiring its own bridge statement" in matter_flat,
    )
    audit.check(
        "carrier attachment names scalar compatibility and KS residual",
        "spin-blind scalar kernel remains compatible with the trivial scalar lift" in carrier_flat
        and "does not prove the KS/Grassmann physical-state-law bridge" in carrier_flat,
    )
    audit.check(
        "carrier attachment names spinful exclusion selector",
        "only" in carrier_flat
        and "displayed kernel excluding the scalar" in carrier_flat
        and "spinful" in carrier_flat
        and "selector must be supplied on the staggered/Kawamoto-Smit route" in carrier_flat,
    )
    audit.check(
        "carrier runner computes scalar compatibility and spinful exclusion",
        "spin-blind scalar mass-shell kernel H*I commutes with sigma_i" in carrier_runner_flat
        and "only the spinful sigma.p kernel excludes the scalar" in carrier_runner_flat,
    )
    audit.check(
        "KS forcing remains bounded on declared kinetic class",
        "Within the declared kinetic class" in ks_forcing
        and "What is NOT claimed: that the kinetic class itself" in ks_flat,
    )
    audit.check(
        "Grassmann forcing remains bounded/conditional",
        "Claim type:** bounded_theorem" in grassmann_forcing
        and "Conditional forcing: TRUE given `GL(F)`" in grassmann_forcing
        and "Unconditional forcing: FALSE" in grassmann_forcing,
    )
    audit.check(
        "kinetic class keeps K1 selector open while naming scalar and Dirac rays",
        "specified constraint set does NOT force `K1`" in kinetic_flat
        and "scalar ray and the Dirac ray" in kinetic_flat,
    )
    audit.check(
        "chirality parity remains narrow support",
        "does not force Grassmann/CAR statistics" in chirality_flat
        and "does not close the BZ-corner species-label bridge" in chirality_flat,
    )
    audit.check(
        "realization gate remains bounded synthesis with conditional closure",
        "bounded synthesis closure" in realization_flat
        and "current closure remains bounded/conditional" in realization_flat,
    )

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "spinful_staggered_kernel_primitive",
        "scalar_lift_exclusion_primitive",
        "ks_to_physical_matter_state_spinor_law_primitive",
        "ks_spin_lift_physical_action_primitive",
        "physical_matter_state_law_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "state-selection rule", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open/merged PR and non-claim boundaries")
    current_flat = flat(current)
    pr_markers = [
        "`#5023` Koide W4 audit-readiness repairs | merged, audit success",
        "`#5024` Koide W4 gate-note premise minimization + substep1-bridge rebase | merged, audit success",
        "`#5026` Koide custody L4 retained-successor re-point | merged, audit success",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft, audit success",
        "`#5014` record-formation front is the domain wall | open, audit success",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open, audit success",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open, audit success",
        "clean/dirty/check labels are not proof inputs",
    ]
    for marker in pr_markers:
        audit.check(f"PR marker present: {marker}", flat(marker) in current_flat)

    explicit_nonclaims = [
        "No derivation or ratification of",
        "`SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`.",
        "`SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`.",
        "`TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`.",
        "No derivation or ratification of `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED`.",
        "`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "retained hydrogen",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
        "No claim that #5014, #5017, #5018, #5023, #5024, or #5026 supplies the spinful",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden = [
        "This note ratifies spinful staggered kernel scalar-lift exclusion",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED is supplied",
        "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED is supplied",
        "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED is supplied",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED is supplied",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED is supplied",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED is supplied",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED is supplied",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This note claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in packet)

    audit.summary()


if __name__ == "__main__":
    main()
