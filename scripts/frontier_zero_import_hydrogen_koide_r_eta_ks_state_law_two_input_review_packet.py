#!/usr/bin/env python3
"""Verifier for the KS state-law two-input review packet."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_STATE_LAW_TWO_INPUT_REVIEW_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
KS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
KS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
KS_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SCALAR_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
SCALAR_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SCALAR_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
ACTION_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
ACTION_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
ACTION_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SIGMA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md"
TRIVIAL_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
FAITHFUL_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_STATE_ACTION_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md"
SIGMA_BUNDLE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SIGMA_P_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md"
FAITHFUL_BUNDLE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_SELECTOR_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md"
PARENT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
PARENT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PARENT_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
HW1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_CARRIER_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
MATTER_ATTACHMENT = ROOT / "docs" / "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md"
CARRIER_ATTACHMENT = ROOT / "docs" / "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md"
KS_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
GRASSMANN_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md"
CHIRALITY_PARITY = ROOT / "docs" / "STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md"
PR5030 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_MULTISITE_PAULI_PR5030_CARRIER_PROVENANCE_IMPACT_DISCRIMINATOR_2026-07-05.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


SCALAR_INPUTS = {
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

BRIDGE_INPUTS = {
    "PHYSICAL_MATTER_STATE_LAW_BRIDGE_TEXT_LOCK",
    "OPERATOR_FRAME_MERGER_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "NATIVE_D_SPIN_BLINDNESS_ACCEPTED",
    "KS_SCALARIZATION_SURFACE_ACCEPTED",
    "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
    "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
    "NO_HW1_LOCUS_OR_CARRIER_CLOSURE_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

HYDROGEN_INPUTS = {
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
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


def closes_scalar(inputs: set[str]) -> bool:
    return SCALAR_INPUTS <= inputs


def closes_action(inputs: set[str]) -> bool:
    return ACTION_INPUTS <= inputs


def closes_ks_route(inputs: set[str]) -> bool:
    return KS_ROUTE_INPUTS <= inputs


def closes_bridge(inputs: set[str]) -> bool:
    return BRIDGE_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def finite_support_checks(audit: Audit) -> None:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    i2 = np.eye(2, dtype=complex)
    sigma = [sx, sy, sz]

    p = np.array([2.0, -1.0, 3.0])
    kernel = sum(p[index] * sigma[index] for index in range(3))
    scalar_kernel = (np.trace(kernel) / 2.0) * i2
    audit.check("finite sigma.p kernel is noncentral", any(not np.allclose(kernel @ op, op @ kernel) for op in sigma))
    audit.check("finite sigma.p kernel is not a scalar lift", not np.allclose(kernel, scalar_kernel))

    theta = np.pi / 2.0
    uz = np.cos(theta / 2.0) * i2 - 1j * np.sin(theta / 2.0) * sz
    u2pi = np.cos(np.pi) * i2 - 1j * np.sin(np.pi) * sz
    scalar = np.exp(1j * np.pi / 5.0) * i2
    audit.check("faithful action sends sigma_x to sigma_y", np.allclose(uz @ sx @ uz.conj().T, sy))
    audit.check("trivial scalar action leaves sigma_x fixed", np.allclose(scalar @ sx @ scalar.conj().T, sx))
    audit.check("faithful 2pi spin lift is minus identity", np.allclose(u2pi, -i2))
    audit.check("adjoint action is blind to SU2 center", np.allclose(u2pi @ sx @ u2pi.conj().T, (-u2pi) @ sx @ (-u2pi).conj().T))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        KOIDE_FIREWALL,
        KS_TARGET,
        KS_DECISION,
        KS_CURRENT,
        SCALAR_TARGET,
        SCALAR_DECISION,
        SCALAR_CURRENT,
        ACTION_TARGET,
        ACTION_DECISION,
        ACTION_CURRENT,
        SIGMA_TARGET,
        TRIVIAL_TARGET,
        FAITHFUL_TARGET,
        SIGMA_BUNDLE,
        FAITHFUL_BUNDLE,
        PARENT_TARGET,
        PARENT_DECISION,
        PARENT_CURRENT,
        HW1_TARGET,
        PHYSICAL_CARRIER_TARGET,
        MATTER_ATTACHMENT,
        CARRIER_ATTACHMENT,
        KS_FORCING,
        GRASSMANN_FORCING,
        CHIRALITY_PARITY,
        PR5030,
        PRIMITIVE_REGISTRY,
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
        "KS State-Law Two-Input Review Packet",
        "grouped KS state-law review packet / adjacent parent-input bundling",
        "scripts/frontier_zero_import_hydrogen_koide_r_eta_ks_state_law_two_input_review_packet.py",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SIGMA_P_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_SELECTOR_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md",
        "`#5033` reflection-positivity runner scope cleanup",
        "`#5030` multisite Pauli finite-carrier provenance",
        "review compression only",
        "The approved primitive registry was checked",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    scalar_full = set(SCALAR_INPUTS)
    action_full = set(ACTION_INPUTS)
    ks_full = set(KS_ROUTE_INPUTS)
    grouped_inputs = {
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
    }
    ks_consequence = {"KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED"}

    audit.check("full scalar-lift exclusion contract closes scalar input", closes_scalar(scalar_full))
    audit.check("scalar-lift exclusion fails without sigma.p parent", not closes_scalar(scalar_full - {"SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED"}))
    audit.check("scalar-lift exclusion fails without trivial scalar covariance exclusion", not closes_scalar(scalar_full - {"TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED"}))
    audit.check("full action-law contract closes action input", closes_action(action_full))
    audit.check("action-law contract fails without faithful selector", not closes_action(action_full - {"FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED"}))
    audit.check("two grouped inputs alone do not close KS state-law route", not closes_ks_route(grouped_inputs))
    audit.check("full KS state-law contract closes parent KS theorem", closes_ks_route(ks_full))

    for missing in grouped_inputs | {"OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"}:
        reduced = set(ks_full)
        reduced.remove(missing)
        audit.check(f"KS state-law route fails without {missing}", not closes_ks_route(reduced))

    audit.check("scalar input alone does not close KS state-law route", not closes_ks_route({"SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED"}))
    audit.check("action input alone does not close KS state-law route", not closes_ks_route({"KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED"}))
    audit.check("KS consequence alone does not close physical matter-state bridge", not closes_bridge(ks_consequence))
    audit.check("KS consequence with full bridge inputs closes physical matter-state bridge", closes_bridge(set(BRIDGE_INPUTS)))
    audit.check("KS consequence alone does not close hydrogen", not closes_hydrogen(ks_consequence))

    section("Finite support checks")
    finite_support_checks(audit)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    for label, container in [("goal packet", goal), ("Koide firewall", firewall)]:
        audit.check(
            f"{label} references grouped KS state-law two-input packet",
            NOTE.name in container and "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED" in container,
        )

    ks_packet = "\n".join([read(KS_TARGET), read(KS_DECISION), read(KS_CURRENT)])
    scalar_packet = "\n".join([read(SCALAR_TARGET), read(SCALAR_DECISION), read(SCALAR_CURRENT)])
    action_packet = "\n".join([read(ACTION_TARGET), read(ACTION_DECISION), read(ACTION_CURRENT)])
    parent_packet = "\n".join([read(PARENT_TARGET), read(PARENT_DECISION), read(PARENT_CURRENT)])
    sigma_bundle = read(SIGMA_BUNDLE)
    faithful_bundle = read(FAITHFUL_BUNDLE)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    audit.check("KS packet consumes both grouped inputs", all(handle in ks_packet for handle in grouped_inputs))
    audit.check("scalar packet references sigma.p and trivial scalar children", SIGMA_TARGET.name in scalar_packet and TRIVIAL_TARGET.name in scalar_packet)
    audit.check("action packet references faithful selector target", FAITHFUL_TARGET.name in action_packet)
    audit.check("parent bridge packet references KS child route", KS_TARGET.name in parent_packet)
    audit.check("HW1 target still consumes physical matter bridge", "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED" in read(HW1_TARGET))
    audit.check("physical carrier target remains downstream of charged carrier", "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED" in read(PHYSICAL_CARRIER_TARGET))
    audit.check("sigma.p child bundle is review compression only", "review compression only" in sigma_bundle and "does not ratify" in sigma_bundle)
    audit.check("faithful selector child bundle is review compression only", "review compression only" in faithful_bundle and "does not ratify" in faithful_bundle)

    matter_flat = flat(read(MATTER_ATTACHMENT))
    carrier_flat = flat(read(CARRIER_ATTACHMENT)).replace("\u00bd", "1/2")
    ks_flat = flat(read(KS_FORCING))
    grassmann_text = read(GRASSMANN_FORCING)
    chirality_flat = flat(read(CHIRALITY_PARITY))
    pr5030_flat = flat(read(PR5030)).lower()
    audit.check(
        "matter attachment keeps KS state-law bridge separate",
        "unless a KS-to-physical-state-law bridge or an elementary state-law theorem is supplied" in matter_flat,
    )
    audit.check(
        "carrier attachment keeps state law separate",
        "does not prove the KS/Grassmann physical-state-law bridge" in carrier_flat,
    )
    audit.check(
        "KS forcing remains bounded support",
        "Within the declared kinetic class" in read(KS_FORCING)
        and "What is NOT claimed: that the kinetic class itself" in ks_flat,
    )
    audit.check(
        "Grassmann forcing remains bounded/conditional",
        "Claim type:** bounded_theorem" in grassmann_text
        and "Conditional forcing: TRUE given `GL(F)`" in grassmann_text
        and "Unconditional forcing: FALSE" in grassmann_text,
    )
    audit.check(
        "chirality parity remains support only",
        "does not force Grassmann/CAR statistics" in chirality_flat
        and "does not close the BZ-corner species-label bridge" in chirality_flat,
    )
    audit.check(
        "PR5030 finite provenance does not close KS state-law route",
        "carrier-provenance" in pr5030_flat and "or hydrogen" in pr5030_flat,
    )

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "spinful_staggered_kernel_scalar_lift_exclusion_primitive",
        "ks_spin_lift_physical_action_primitive",
        "ks_to_physical_matter_state_spinor_law_primitive",
        "physical_matter_state_law_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for forbidden in [
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "hydrogen_primitive",
    ]:
        audit.check(f"approved primitive notes do not supply {forbidden}", forbidden not in primitive_text)

    section("Non-claim checks")
    for phrase in [
        "No derivation or ratification of\n  `SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`.",
        "No derivation or ratification of `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED`.",
        "No derivation or ratification of\n  `KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.",
        "No R-eta, h-class, h-unit, K1/K2/K3/K4, Koide electron readout, `m_e`,",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]:
        audit.check(f"explicit non-claim present: {flat(phrase)}", flat(phrase) in note_flat)

    forbidden_overclaims = [
        "This packet ratifies",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED is supplied",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED is supplied",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED is supplied",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED is supplied",
        "hydrogen retained theorem",
        "This packet claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
