#!/usr/bin/env python3
"""Verifier for the Koide R-eta spinful sigma.p KS-route kernel lane."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md"
DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SCALAR_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
SCALAR_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SCALAR_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
MATTER_ATTACHMENT = ROOT / "docs" / "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md"
CARRIER_ATTACHMENT = ROOT / "docs" / "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md"
CARRIER_RUNNER = ROOT / "scripts" / "carrier_attachment_chirality_gate_consolidation_runner.py"
KS_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
KINETIC_CLASS = ROOT / "docs" / "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
REALIZATION_GATE = ROOT / "docs" / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


SIGMA_ROUTE_INPUTS = {
    "SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TEXT_LOCK",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "SCALAR_KERNEL_COMPATIBILITY_ACCEPTED",
    "STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED",
    "KS_PHASE_FORCING_SURFACE_ACCEPTED",
    "KINETIC_TWO_RAY_SURFACE_ACCEPTED",
    "FINITE_SIGMA_DOT_P_NONCENTRALITY_CHECK",
    "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED",
    "KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED",
    "NO_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_INPUT",
    "NO_SCALAR_LIFT_EXCLUSION_HANDOFF_INPUT",
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

CURRENT_SURFACE_INPUTS = SIGMA_ROUTE_INPUTS - {
    "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED",
    "KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

SCALAR_LIFT_INPUTS = {
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

PARENT_BRIDGE_INPUTS = {
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


def closes_sigma_route(inputs: set[str]) -> bool:
    return SIGMA_ROUTE_INPUTS <= inputs


def closes_scalar_lift_exclusion(inputs: set[str]) -> bool:
    return SCALAR_LIFT_INPUTS <= inputs


def closes_ks_route(inputs: set[str]) -> bool:
    return KS_ROUTE_INPUTS <= inputs


def closes_parent_bridge(inputs: set[str]) -> bool:
    return PARENT_BRIDGE_INPUTS <= inputs


def closes_hw1(inputs: set[str]) -> bool:
    return HW1_INPUTS <= inputs


def closes_r_eta(inputs: set[str]) -> bool:
    return R_ETA_INPUTS <= inputs


def closes_electron_mass(inputs: set[str]) -> bool:
    return ELECTRON_MASS_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def finite_sigma_dot_p_checks(audit: Audit) -> None:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    sigma = [sx, sy, sz]
    i2 = np.eye(2, dtype=complex)

    p = np.array([1.0, 2.0, -3.0])
    k_sigma = sum(p[i] * sigma[i] for i in range(3))
    scalar_part = (np.trace(k_sigma) / 2.0) * i2
    noncentral = any(not np.allclose(k_sigma @ s, s @ k_sigma) for s in sigma)
    traceless = np.allclose(np.trace(k_sigma), 0.0)
    eigvals = np.linalg.eigvalsh(k_sigma)
    norm_p = np.linalg.norm(p)

    h_scalar = 1.3 * i2
    scalar_commutes = all(np.allclose(h_scalar @ s, s @ h_scalar) for s in sigma)

    theta = np.pi / 2.0
    uz = np.cos(theta / 2.0) * i2 - 1j * np.sin(theta / 2.0) * sz
    rotated_x = uz @ sx @ uz.conj().T
    scalar_lift_x = i2 @ sx @ i2

    audit.check("finite sigma.p kernel is traceless", traceless)
    audit.check("finite sigma.p kernel is not a scalar multiple of identity", not np.allclose(k_sigma, scalar_part))
    audit.check("finite sigma.p kernel is noncentral", noncentral)
    audit.check("finite sigma.p eigenvalues are plus/minus |p|", np.allclose(sorted(eigvals), sorted([-norm_p, norm_p])))
    audit.check("spin-blind scalar kernel commutes with Pauli operators", scalar_commutes)
    audit.check("faithful z-rotation sends sigma_x to sigma_y", np.allclose(rotated_x, sy))
    audit.check("trivial scalar lift leaves sigma_x unchanged in the finite witness", np.allclose(scalar_lift_x, sx))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        TARGET,
        DECISION,
        CURRENT,
        SCALAR_TARGET,
        SCALAR_DECISION,
        SCALAR_CURRENT,
        KS_TARGET,
        GOAL,
        KOIDE_FIREWALL,
        MATTER_ATTACHMENT,
        CARRIER_ATTACHMENT,
        CARRIER_RUNNER,
        KS_FORCING,
        KINETIC_CLASS,
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
        "Koide R-Eta Spinful Sigma-Dot-P Kernel KS Route Target Discriminator",
        "Koide R-Eta Spinful Sigma-Dot-P Kernel KS Route Ratification Decision Packet",
        "Koide R-Eta Spinful Sigma-Dot-P Kernel KS Route Current-Surface No-Go",
        "scripts/frontier_zero_import_hydrogen_koide_r_eta_spinful_sigma_dot_p_kernel_ks_route.py",
        "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED",
        "SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TEXT_LOCK",
        "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
        "SCALAR_KERNEL_COMPATIBILITY_ACCEPTED",
        "STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED",
        "KS_PHASE_FORCING_SURFACE_ACCEPTED",
        "KINETIC_TWO_RAY_SURFACE_ACCEPTED",
        "FINITE_SIGMA_DOT_P_NONCENTRALITY_CHECK",
        "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED",
        "KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED",
        "NO_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_INPUT",
        "NO_SCALAR_LIFT_EXCLUSION_HANDOFF_INPUT",
        "NO_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_INPUT",
        "NO_KS_ROUTE_CLOSURE_INPUT",
        "NO_PARENT_BRIDGE_OR_HW1_INPUT",
        "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md",
        "scripts/carrier_attachment_chirality_gate_consolidation_runner.py",
        "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md",
        "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md",
        "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md",
        "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "`#5016` zero-import hydrogen retained lane bundle",
        "merged `#5019`",
        "merged `#5020`",
        "merged `#5022`",
        "merged `#5023`",
        "merged `#5024`",
        "open `#5021`",
        "open `#5014`",
        "open `#5017`",
        "open `#5018`",
        "The approved primitive registry was checked",
        "clean/dirty/check labels are not proof inputs",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in packet_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in packet)

    section("Predicate checks")
    full_route = set(SIGMA_ROUTE_INPUTS)
    audit.check("full sigma-dot-p KS-route contract closes target", closes_sigma_route(full_route))
    audit.check("current surface does not close sigma-dot-p KS-route target", not closes_sigma_route(CURRENT_SURFACE_INPUTS))

    for missing in sorted(SIGMA_ROUTE_INPUTS):
        reduced = set(full_route)
        reduced.remove(missing)
        audit.check(f"sigma-dot-p KS-route contract fails without input {missing}", not closes_sigma_route(reduced))

    accepted_subsets = [subset for subset in all_subsets(SIGMA_ROUTE_INPUTS) if closes_sigma_route(subset)]
    audit.check("only one minimal full sigma-dot-p subset closes", accepted_subsets == [SIGMA_ROUTE_INPUTS])

    sigma_consequence = {"SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED"}
    scalar_full = set(SCALAR_LIFT_INPUTS)
    scalar_without_covariance = scalar_full - {"TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED"}
    audit.check("sigma consequence alone does not close scalar-lift exclusion", not closes_scalar_lift_exclusion(sigma_consequence))
    audit.check("sigma consequence plus full scalar-lift contract closes scalar-lift exclusion", closes_scalar_lift_exclusion(scalar_full))
    audit.check("sigma consequence cannot close scalar-lift exclusion without covariance theorem", not closes_scalar_lift_exclusion(scalar_without_covariance))
    audit.check("sigma consequence alone does not close KS route", not closes_ks_route(sigma_consequence))
    audit.check("sigma consequence alone does not close parent bridge", not closes_parent_bridge(sigma_consequence))
    audit.check("sigma consequence alone does not close HW1", not closes_hw1(sigma_consequence))
    audit.check("sigma consequence alone does not close R-eta", not closes_r_eta(sigma_consequence))
    audit.check("sigma consequence alone does not close electron mass", not closes_electron_mass(sigma_consequence))
    audit.check("sigma consequence alone does not close hydrogen", not closes_hydrogen(sigma_consequence))

    scalar_consequence = {"SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED"}
    ks_with_scalar = set(KS_ROUTE_INPUTS)
    ks_without_action = ks_with_scalar - {"KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED"}
    audit.check("scalar-lift consequence plus full KS inputs closes KS route", closes_ks_route(ks_with_scalar))
    audit.check("scalar-lift consequence cannot close KS route without KS action law", not closes_ks_route(ks_without_action))
    audit.check("scalar-lift consequence alone does not close hydrogen", not closes_hydrogen(scalar_consequence))

    section("Finite sigma.p support checks")
    finite_sigma_dot_p_checks(audit)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    scalar_target = read(SCALAR_TARGET)
    scalar_decision = read(SCALAR_DECISION)
    scalar_current = read(SCALAR_CURRENT)
    scalar_packet = "\n".join([scalar_target, scalar_decision, scalar_current])
    matter_attachment = read(MATTER_ATTACHMENT)
    carrier_attachment = read(CARRIER_ATTACHMENT)
    carrier_runner = read(CARRIER_RUNNER)
    ks_forcing = read(KS_FORCING)
    kinetic_class = read(KINETIC_CLASS)
    realization_gate = read(REALIZATION_GATE)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("scalar target", scalar_target),
        ("scalar decision", scalar_decision),
        ("scalar current no-go", scalar_current),
    ]:
        audit.check(
            f"{label} references sigma-dot-p KS-route lane",
            TARGET.name in container
            and DECISION.name in container
            and CURRENT.name in container
            and "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED" in container,
        )

    audit.check("sigma packet references scalar-lift parent target", SCALAR_TARGET.name in packet)
    audit.check("sigma packet references KS target downstream", "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED" in packet)
    audit.check("scalar packet still consumes sigma-dot-p target as subinput", "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED" in scalar_packet)

    matter_flat = flat(matter_attachment)
    carrier_flat = flat(carrier_attachment)
    carrier_runner_flat = flat(carrier_runner)
    ks_flat = flat(ks_forcing)
    kinetic_flat = flat(kinetic_class)
    realization_flat = flat(realization_gate)

    audit.check(
        "matter attachment localizes KS state-law residual",
        "positive bridge surface isolated here is Kawamoto-Smit reconstruction" in matter_flat
        and "physical matter-state law still requiring its own bridge statement" in matter_flat,
    )
    audit.check(
        "carrier attachment names scalar compatibility and KS residual",
        "spin-blind scalar kernel remains compatible with the trivial scalar lift" in carrier_flat
        and "does not prove the KS/Grassmann" in carrier_flat,
    )
    audit.check(
        "carrier attachment names spinful selector location",
        "only" in carrier_flat
        and "displayed kernel excluding the scalar" in carrier_flat
        and "spinful" in carrier_flat
        and "route supplies the live place where such a spinful selector can enter" in carrier_flat,
    )
    audit.check(
        "carrier runner computes sigma.p support",
        "K_spinful = sum(p[i] * sigma[i]" in carrier_runner_flat
        and "only the spinful sigma.p kernel excludes the scalar" in carrier_runner_flat,
    )
    audit.check(
        "KS forcing remains bounded on declared kinetic class",
        "Within the declared kinetic class" in ks_forcing
        and "What is NOT claimed: that the kinetic class itself" in ks_flat,
    )
    audit.check(
        "kinetic class keeps K1 selector open while naming scalar and Dirac rays",
        "specified constraint set does NOT force `K1`" in kinetic_flat
        and "scalar ray and the Dirac ray" in kinetic_flat,
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
        "spinful_sigma_dot_p_kernel_primitive",
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
        "`#5016` zero-import hydrogen retained lane bundle | open; audit running at refresh",
        "`#5019` AC_phi_lambda decomposition chain | merged, audit success",
        "`#5020` AC_phi_lambda value face | merged, audit success",
        "`#5022` delta-eta chain repair | merged, audit success",
        "`#5023` Koide W4 audit-readiness repairs | merged, audit success",
        "`#5024` Koide W4 gate-note premise minimization + substep1-bridge rebase | merged, audit success",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft, audit success",
        "`#5014` record-formation front is the domain wall | open, audit success",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open, audit success",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open, audit success",
        "clean/dirty/check labels are not proof inputs",
    ]
    for marker in pr_markers:
        audit.check(f"PR marker present: {marker}", flat(marker) in current_flat)

    explicit_nonclaims = [
        "`SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`.",
        "`KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED`.",
        "`KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED`.",
        "`TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`.",
        "`SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`.",
        "No derivation or ratification of `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED`.",
        "`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "retained hydrogen",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
        "No claim that #5014, #5017, #5018, #5019, #5020, #5022, #5023, or #5024",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden = [
        "This note ratifies spinful sigma-dot-p KS-route kernel",
        "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED is supplied",
        "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED is supplied",
        "KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED is supplied",
        "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED is supplied",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED is supplied",
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
