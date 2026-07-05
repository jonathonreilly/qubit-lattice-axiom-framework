#!/usr/bin/env python3
"""Verifier for the Koide R-eta KS spin-lift physical action-law lane."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
KS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
KS_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SCALAR_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
SCALAR_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SCALAR_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PARENT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
PARENT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PARENT_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
HW1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_CARRIER_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
MATTER_ATTACHMENT = ROOT / "docs" / "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md"
CARRIER_ATTACHMENT = ROOT / "docs" / "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md"
SU2_MERGER = ROOT / "docs" / "INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md"
PER_SITE_SPIN = ROOT / "docs" / "PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md"
CL31_EXTENSION = ROOT / "docs" / "CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md"
BOOST_NO_GO = ROOT / "docs" / "QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md"
KS_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
GRASSMANN_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md"
CHIRALITY_PARITY = ROOT / "docs" / "STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md"
REALIZATION_GATE = ROOT / "docs" / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


ACTION_INPUTS = {
    "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_TEXT_LOCK",
    "MATTER_ATTACHMENT_KS_REDUCTION_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "OPERATOR_FRAME_MERGER_ACCEPTED",
    "PER_SITE_PAULI_SPIN_HALF_MODULE_ACCEPTED",
    "CL31_EXTENSION_MODULE_BOUNDARY_ACCEPTED",
    "KS_PHASE_FORCING_SURFACE_ACCEPTED",
    "GRASSMANN_CAR_SURFACE_ACCEPTED",
    "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
    "FINITE_SU2_DOUBLE_COVER_ACTION_CHECK",
    "FINITE_ADJOINT_CENTER_BLINDNESS_CHECK",
    "FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED",
    "NO_SPINFUL_SCALAR_LIFT_EXCLUSION_INPUT",
    "NO_KS_ROUTE_CLOSURE_INPUT",
    "NO_PARENT_BRIDGE_OR_HW1_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_SURFACE_INPUTS = ACTION_INPUTS - {
    "FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED",
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


def closes_action_law(inputs: set[str]) -> bool:
    return ACTION_INPUTS <= inputs


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


def finite_spin_lift_checks(audit: Audit) -> None:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    i2 = np.eye(2, dtype=complex)
    state = np.array([1, 0], dtype=complex)

    theta = np.pi / 2
    uz = np.cos(theta / 2) * i2 - 1j * np.sin(theta / 2) * sz
    rotated_sx = uz @ sx @ uz.conj().T

    full_turn = np.cos(np.pi) * i2 - 1j * np.sin(np.pi) * sz
    minus_full_turn = -full_turn
    full_turn_state = full_turn @ state
    trivial_state = i2 @ state

    audit.check("faithful quarter-turn co-rotates sigma_x to sigma_y", np.allclose(rotated_sx, sy))
    audit.check("faithful 2pi spin lift is minus identity", np.allclose(full_turn, -i2))
    audit.check("state action distinguishes faithful 2pi from trivial lift", not np.allclose(full_turn_state, trivial_state))
    audit.check("adjoint action is blind to the SU2 center", np.allclose(full_turn @ sx @ full_turn.conj().T, minus_full_turn @ sx @ minus_full_turn.conj().T))
    audit.check("trivial lift does not supply the faithful quarter-turn action", not np.allclose(i2 @ state, uz @ state))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        TARGET,
        DECISION,
        CURRENT,
        KS_TARGET,
        KS_DECISION,
        KS_CURRENT,
        SCALAR_TARGET,
        SCALAR_DECISION,
        SCALAR_CURRENT,
        GOAL,
        KOIDE_FIREWALL,
        PARENT_TARGET,
        PARENT_DECISION,
        PARENT_CURRENT,
        HW1_TARGET,
        PHYSICAL_CARRIER_TARGET,
        MATTER_ATTACHMENT,
        CARRIER_ATTACHMENT,
        SU2_MERGER,
        PER_SITE_SPIN,
        CL31_EXTENSION,
        BOOST_NO_GO,
        KS_FORCING,
        GRASSMANN_FORCING,
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
        "Koide R-Eta KS Spin-Lift Physical Action-Law Target Discriminator",
        "Koide R-Eta KS Spin-Lift Physical Action-Law Ratification Decision Packet",
        "Koide R-Eta KS Spin-Lift Physical Action-Law Current-Surface No-Go",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_TEXT_LOCK",
        "MATTER_ATTACHMENT_KS_REDUCTION_ACCEPTED",
        "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
        "OPERATOR_FRAME_MERGER_ACCEPTED",
        "PER_SITE_PAULI_SPIN_HALF_MODULE_ACCEPTED",
        "CL31_EXTENSION_MODULE_BOUNDARY_ACCEPTED",
        "KS_PHASE_FORCING_SURFACE_ACCEPTED",
        "GRASSMANN_CAR_SURFACE_ACCEPTED",
        "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
        "FINITE_SU2_DOUBLE_COVER_ACTION_CHECK",
        "FINITE_ADJOINT_CENTER_BLINDNESS_CHECK",
        "FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED",
        "NO_SPINFUL_SCALAR_LIFT_EXCLUSION_INPUT",
        "NO_KS_ROUTE_CLOSURE_INPUT",
        "NO_PARENT_BRIDGE_OR_HW1_INPUT",
        "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md",
        "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md",
        "INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md",
        "PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md",
        "CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md",
        "QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md",
        "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md",
        "STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md",
        "STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md",
        "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "open `#5016`",
        "merged `#5023`",
        "merged `#5024`",
        "merged `#5026`",
        "open `#5021`",
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
    full_route = set(ACTION_INPUTS)
    audit.check("full action-law contract closes target", closes_action_law(full_route))
    audit.check("current surface does not close action-law target", not closes_action_law(CURRENT_SURFACE_INPUTS))

    for missing in sorted(ACTION_INPUTS):
        reduced = set(full_route)
        reduced.remove(missing)
        audit.check(f"action-law contract fails without input {missing}", not closes_action_law(reduced))

    accepted_subsets = [subset for subset in all_subsets(ACTION_INPUTS) if closes_action_law(subset)]
    audit.check("only one minimal full action-law subset closes", accepted_subsets == [ACTION_INPUTS])

    action_consequence = {"KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED"}
    ks_with_action = set(KS_ROUTE_INPUTS)
    ks_without_scalar = ks_with_action - {"SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED"}
    audit.check("action consequence alone does not close KS route", not closes_ks_route(action_consequence))
    audit.check("action consequence plus full KS inputs closes KS route", closes_ks_route(ks_with_action))
    audit.check("action consequence cannot close KS route without scalar-lift sibling", not closes_ks_route(ks_without_scalar))
    audit.check("action consequence alone does not close parent bridge", not closes_parent_bridge(action_consequence))
    audit.check("action consequence alone does not close HW1", not closes_hw1(action_consequence))
    audit.check("action consequence alone does not close charged carrier theorem", not closes_charged_carrier(action_consequence))
    audit.check("action consequence alone does not close physical carrier context", not closes_physical_carrier(action_consequence))
    audit.check("action consequence alone does not close R-eta", not closes_r_eta(action_consequence))
    audit.check("action consequence alone does not close electron mass", not closes_electron_mass(action_consequence))
    audit.check("action consequence alone does not close hydrogen", not closes_hydrogen(action_consequence))

    section("Finite spin-lift checks")
    finite_spin_lift_checks(audit)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    ks_packet = "\n".join([read(KS_TARGET), read(KS_DECISION), read(KS_CURRENT)])
    scalar_packet = "\n".join([read(SCALAR_TARGET), read(SCALAR_DECISION), read(SCALAR_CURRENT)])
    parent_packet = "\n".join([read(PARENT_TARGET), read(PARENT_DECISION), read(PARENT_CURRENT)])
    matter_attachment = read(MATTER_ATTACHMENT)
    carrier_attachment = read(CARRIER_ATTACHMENT)
    su2_merger = read(SU2_MERGER)
    per_site_spin = read(PER_SITE_SPIN)
    cl31_extension = read(CL31_EXTENSION)
    boost_no_go = read(BOOST_NO_GO)
    ks_forcing = read(KS_FORCING)
    grassmann_forcing = read(GRASSMANN_FORCING)
    chirality_parity = read(CHIRALITY_PARITY)
    realization_gate = read(REALIZATION_GATE)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("KS target packet", ks_packet),
    ]:
        audit.check(
            f"{label} references action-law lane",
            TARGET.name in container
            and DECISION.name in container
            and CURRENT.name in container
            and "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED" in container,
        )

    audit.check("action packet references KS parent target", KS_TARGET.name in packet)
    audit.check("action packet references scalar-lift sibling target", SCALAR_TARGET.name in packet)
    audit.check("KS packet still names scalar-lift sibling", "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED" in ks_packet)
    audit.check("scalar packet keeps action law as sibling non-input", "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED" in scalar_packet)
    audit.check("parent packet still names physical matter bridge", "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED" in parent_packet)
    audit.check("HW1 target still consumes parent bridge only", "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED" in read(HW1_TARGET))
    audit.check("physical carrier target keeps charged carrier downstream", "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED" in read(PHYSICAL_CARRIER_TARGET))

    matter_flat = flat(matter_attachment)
    carrier_flat = flat(carrier_attachment)
    carrier_norm = carrier_flat.replace("\u00bd", "1/2").replace("C\u00b2", "C^2")
    su2_flat = flat(su2_merger)
    per_site_flat = flat(per_site_spin)
    cl31_flat = flat(cl31_extension)
    cl31_norm = cl31_flat.replace("C\u00b2", "C^2")
    boost_flat = flat(boost_no_go)
    ks_flat = flat(ks_forcing)
    grassmann_flat = flat(grassmann_forcing)
    chirality_flat = flat(chirality_parity)
    realization_flat = flat(realization_gate)

    audit.check(
        "matter attachment localizes KS state-law residual",
        "unless a KS-to-physical-state-law bridge or an elementary state-law theorem is supplied" in matter_flat
        and "physical matter-state law still requiring its own bridge statement" in matter_flat,
    )
    audit.check(
        "carrier attachment keeps state law separate",
        "j=1/2 state law is a separate datum" in carrier_norm
        and "does not prove the KS/Grassmann physical-state-law bridge" in carrier_norm,
    )
    audit.check(
        "SU2 merger is operator-level support",
        "operator-level identification" in su2_flat
        and "U(R) sigma_i U(R)^*" in su2_merger,
    )
    audit.check(
        "per-site spin source withholds physical matter generator",
        "does not, by itself, identify this action with the physical spin generator" in per_site_flat,
    )
    audit.check(
        "Cl31 extension is abstract algebra support",
        "abstract finite-dimensional real Clifford" in cl31_norm
        and "classification statement" in cl31_norm
        and "per-site site module is `C^2`-valued" in cl31_norm,
    )
    audit.check(
        "boost no-go records action-faith residual",
        "local operator algebra by itself" in boost_flat
        and "live residual is the attachment step" in boost_flat,
    )
    audit.check(
        "KS forcing remains bounded",
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
        "chirality parity remains narrow support",
        "does not force Grassmann/CAR statistics" in chirality_flat
        and "does not close the BZ-corner species-label bridge" in chirality_flat,
    )
    audit.check(
        "realization gate remains bounded synthesis",
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
        "ks_spin_lift_physical_action_primitive",
        "faithful_ks_state_action_selector_primitive",
        "ks_to_physical_matter_state_spinor_law_primitive",
        "physical_matter_state_law_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "state-selection rule", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open/merged PR and non-claim boundaries")
    current_flat = flat(current)
    pr_markers = [
        "`#5016` zero-import hydrogen retained lane bundle | open, audit in progress at refresh",
        "`#5023` Koide W4 audit-readiness repairs | merged, audit success",
        "`#5024` Koide W4 gate-note premise minimization + substep1-bridge rebase | merged, audit success",
        "`#5026` Koide custody L4 retained-successor re-point | merged, audit success",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft, audit success",
        "`#5014` record-formation front is the domain wall | open, audit success",
        "`#5017` domain-wall anomaly inflow spectral flow | open, audit success",
        "`#5018` domain-wall edge content vs SM chiral map | open, audit success",
        "clean/dirty/check labels are not proof inputs",
    ]
    for marker in pr_markers:
        audit.check(f"PR marker present: {marker}", flat(marker) in current_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED`.",
        "`FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED`.",
        "`SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`.",
        "`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "retained hydrogen",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
        "No claim that #5014, #5017, #5018, #5023, #5024, or #5026 supplies the KS",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden = [
        "This note ratifies KS spin-lift physical action law",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED is supplied",
        "FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED is supplied",
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
