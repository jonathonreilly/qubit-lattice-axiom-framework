#!/usr/bin/env python3
"""Verifier for the Koide R-eta trivial scalar-lift covariance lane."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SCALAR_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
SCALAR_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SCALAR_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SIGMA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md"
SIGMA_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SIGMA_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
KS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
KS_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PARENT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
PARENT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PARENT_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
HW1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
MATTER_ATTACHMENT = ROOT / "docs" / "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md"
CARRIER_ATTACHMENT = ROOT / "docs" / "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md"
CARRIER_RUNNER = ROOT / "scripts" / "carrier_attachment_chirality_gate_consolidation_runner.py"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


TRIVIAL_INPUTS = {
    "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_TEXT_LOCK",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "SCALAR_KERNEL_COMPATIBILITY_ACCEPTED",
    "STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED",
    "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED",
    "FINITE_FAITHFUL_SPIN_LIFT_COVARIANCE_CHECK",
    "FINITE_TRIVIAL_LIFT_COVARIANCE_FAILURE_CHECK",
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

CURRENT_SURFACE_INPUTS = TRIVIAL_INPUTS - {
    "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

SCALAR_PARENT_INPUTS = {
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


def closes_trivial_covariance(inputs: set[str]) -> bool:
    return TRIVIAL_INPUTS <= inputs


def closes_scalar_parent(inputs: set[str]) -> bool:
    return SCALAR_PARENT_INPUTS <= inputs


def closes_ks_route(inputs: set[str]) -> bool:
    return KS_ROUTE_INPUTS <= inputs


def closes_parent_bridge(inputs: set[str]) -> bool:
    return FIXED_PARENT_BRIDGE_INPUTS <= inputs and bool(PARENT_ROUTE_INPUTS & inputs)


def closes_hw1(inputs: set[str]) -> bool:
    return HW1_INPUTS <= inputs


def closes_electron_mass(inputs: set[str]) -> bool:
    return ELECTRON_MASS_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def finite_covariance_checks(audit: Audit) -> None:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    i2 = np.eye(2, dtype=complex)

    theta = np.pi / 2
    faithful_z = np.cos(theta / 2) * i2 - 1j * np.sin(theta / 2) * sz
    spinful_kernel_px = sx
    faithful_rotated = faithful_z @ spinful_kernel_px @ faithful_z.conj().T
    trivial_rotated = i2 @ spinful_kernel_px @ i2

    h_scalar = 1.7 * i2
    scalar_faithful = faithful_z @ h_scalar @ faithful_z.conj().T
    scalar_trivial = i2 @ h_scalar @ i2

    audit.check("faithful spin lift is unitary", np.allclose(faithful_z.conj().T @ faithful_z, i2))
    audit.check("faithful z quarter-turn sends sigma_x to sigma_y", np.allclose(faithful_rotated, sy))
    audit.check("trivial scalar lift leaves sigma_x fixed", np.allclose(trivial_rotated, sx))
    audit.check("trivial scalar lift fails spinful covariance", not np.allclose(trivial_rotated, sy))
    audit.check("spin-blind scalar kernel remains compatible with both lifts", np.allclose(scalar_faithful, h_scalar) and np.allclose(scalar_trivial, h_scalar))


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
        SIGMA_TARGET,
        SIGMA_DECISION,
        SIGMA_CURRENT,
        KS_TARGET,
        KS_DECISION,
        KS_CURRENT,
        GOAL,
        KOIDE_FIREWALL,
        PARENT_TARGET,
        PARENT_DECISION,
        PARENT_CURRENT,
        HW1_TARGET,
        MATTER_ATTACHMENT,
        CARRIER_ATTACHMENT,
        CARRIER_RUNNER,
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
        "Koide R-Eta Trivial Scalar-Lift Covariance Exclusion Target Discriminator",
        "Koide R-Eta Trivial Scalar-Lift Covariance Exclusion Ratification Decision Packet",
        "Koide R-Eta Trivial Scalar-Lift Covariance Exclusion Current-Surface No-Go",
        "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED",
        "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_TEXT_LOCK",
        "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
        "SCALAR_KERNEL_COMPATIBILITY_ACCEPTED",
        "STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED",
        "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED",
        "FINITE_FAITHFUL_SPIN_LIFT_COVARIANCE_CHECK",
        "FINITE_TRIVIAL_LIFT_COVARIANCE_FAILURE_CHECK",
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
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md",
        "scripts/carrier_attachment_chirality_gate_consolidation_runner.py",
        "The approved primitive registry was checked",
        "open `#5016`",
        "open `#5026`",
        "merged `#5023`",
        "merged `#5024`",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in packet_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in packet)

    section("Predicate checks")
    full_route = set(TRIVIAL_INPUTS)
    audit.check("full trivial-lift covariance contract closes target", closes_trivial_covariance(full_route))
    audit.check("current surface does not close target", not closes_trivial_covariance(CURRENT_SURFACE_INPUTS))

    for missing in sorted(TRIVIAL_INPUTS):
        reduced = set(full_route)
        reduced.remove(missing)
        audit.check(f"trivial-lift covariance contract fails without input {missing}", not closes_trivial_covariance(reduced))

    accepted_subsets = [subset for subset in all_subsets(TRIVIAL_INPUTS) if closes_trivial_covariance(subset)]
    audit.check("only one minimal full trivial-lift subset closes", accepted_subsets == [TRIVIAL_INPUTS])

    consequence = {"TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED"}
    scalar_parent_full = set(SCALAR_PARENT_INPUTS)
    scalar_parent_without_sigma = scalar_parent_full - {"SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED"}
    audit.check("trivial-lift consequence alone does not close scalar-lift parent", not closes_scalar_parent(consequence))
    audit.check("trivial-lift consequence plus full scalar parent inputs closes parent", closes_scalar_parent(scalar_parent_full))
    audit.check("trivial-lift consequence cannot close parent without sigma-dot-p route input", not closes_scalar_parent(scalar_parent_without_sigma))
    audit.check("trivial-lift consequence alone does not close KS route", not closes_ks_route(consequence))
    audit.check("trivial-lift consequence alone does not close parent bridge", not closes_parent_bridge(consequence))
    audit.check("trivial-lift consequence alone does not close HW1", not closes_hw1(consequence))
    audit.check("trivial-lift consequence alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("trivial-lift consequence alone does not close hydrogen", not closes_hydrogen(consequence))

    section("Finite Pauli covariance checks")
    finite_covariance_checks(audit)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    scalar_packet = "\n".join([read(SCALAR_TARGET), read(SCALAR_DECISION), read(SCALAR_CURRENT)])
    sigma_packet = "\n".join([read(SIGMA_TARGET), read(SIGMA_DECISION), read(SIGMA_CURRENT)])
    ks_packet = "\n".join([read(KS_TARGET), read(KS_DECISION), read(KS_CURRENT)])
    parent_packet = "\n".join([read(PARENT_TARGET), read(PARENT_DECISION), read(PARENT_CURRENT)])
    matter_attachment = read(MATTER_ATTACHMENT)
    carrier_attachment = read(CARRIER_ATTACHMENT)
    carrier_runner = read(CARRIER_RUNNER)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("scalar-lift target", read(SCALAR_TARGET)),
        ("scalar-lift decision", read(SCALAR_DECISION)),
        ("scalar-lift current no-go", read(SCALAR_CURRENT)),
    ]:
        audit.check(
            f"{label} references trivial scalar-lift child lane",
            TARGET.name in container
            and DECISION.name in container
            and CURRENT.name in container
            and "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED" in container,
        )

    audit.check("new packet references sigma-dot-p lane", SIGMA_TARGET.name in packet and SIGMA_DECISION.name in packet and SIGMA_CURRENT.name in packet)
    audit.check("new packet references scalar-lift parent", SCALAR_TARGET.name in packet and "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED" in packet)
    audit.check("scalar parent still names scalar-lift target", "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED" in scalar_packet)
    audit.check("sigma packet still names route-defined kernel target", "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED" in sigma_packet)
    audit.check("KS packet still names KS child theorem", "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED" in ks_packet)
    audit.check("parent packet still names physical matter bridge", "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED" in parent_packet)
    audit.check("HW1 target still consumes parent bridge only", "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED" in read(HW1_TARGET))

    matter_flat = flat(matter_attachment)
    carrier_flat = flat(carrier_attachment)
    carrier_runner_flat = flat(carrier_runner)
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
        "displayed kernel excluding the scalar" in carrier_flat
        and "spinful" in carrier_flat
        and "selector must be supplied on the staggered/Kawamoto-Smit route" in carrier_flat,
    )
    audit.check(
        "carrier runner computes scalar compatibility and spinful exclusion",
        "spin-blind scalar mass-shell kernel H*I commutes with sigma_i" in carrier_runner_flat
        and "only the spinful sigma.p kernel excludes the scalar" in carrier_runner_flat,
    )

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "trivial_scalar_lift_covariance_exclusion_primitive",
        "spinful_sigma_dot_p_kernel_primitive",
        "spinful_staggered_kernel_primitive",
        "ks_to_physical_matter_state_spinor_law_primitive",
        "physical_matter_state_law_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "dynamics", "full Lorentz restoration", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open/merged PR and non-claim boundaries")
    current_flat = flat(current)
    pr_markers = [
        "`#5016` zero-import hydrogen retained lane bundle | open, audit in progress",
        "`#5026` Koide custody L4 retained-successor re-point | open, audit in progress",
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
        "No derivation or ratification of",
        "`TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`.",
        "`SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`.",
        "`SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`.",
        "No derivation or ratification of `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED`.",
        "`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "retained hydrogen",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
        "#5026 supplies the trivial scalar-lift covariance-failure theorem",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden = [
        "This note ratifies trivial scalar-lift covariance exclusion",
        "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED is supplied",
        "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED is supplied",
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
