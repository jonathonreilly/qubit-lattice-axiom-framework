#!/usr/bin/env python3
"""Verifier for the Koide R-eta elementary physical state-rotation lane."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SELECTOR_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md"
SELECTOR_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SELECTOR_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PARENT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
PARENT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PARENT_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KS_CHILD_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
KS_CHILD_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
KS_CHILD_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
HW1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
MATTER_ATTACHMENT = ROOT / "docs" / "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md"
CARRIER_ATTACHMENT = ROOT / "docs" / "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md"
SU2_MERGER = ROOT / "docs" / "INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md"
PER_SITE_SPIN = ROOT / "docs" / "PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md"
CL31_EXTENSION = ROOT / "docs" / "CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md"
BOOST_NO_GO = ROOT / "docs" / "QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


ELEMENTARY_INPUTS = {
    "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_TEXT_LOCK",
    "MATTER_ATTACHMENT_ELEMENTARY_ROUTE_ACCEPTED",
    "OPERATOR_FRAME_MERGER_ACCEPTED",
    "PER_SITE_PAULI_SPIN_HALF_MODULE_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "CL31_EXTENSION_MODULE_BOUNDARY_ACCEPTED",
    "BOOST_ACTION_FAITH_ANALOGY_ACCEPTED",
    "FINITE_SU2_DOUBLE_COVER_ACTION_CHECK",
    "FINITE_ADJOINT_CENTER_BLINDNESS_CHECK",
    "FINITE_TRIVIAL_STATE_LIFT_COUNTERMODEL_CHECK",
    "FINITE_FAITHFUL_SPINOR_STATE_LAW_CHECK",
    "ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED",
    "NO_KS_ROUTE_THEOREM_INPUT",
    "NO_PHYSICAL_MATTER_STATE_BRIDGE_INPUT",
    "NO_HW1_OR_CARRIER_CLOSURE_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_SURFACE_INPUTS = ELEMENTARY_INPUTS - {
    "ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

PARENT_FIXED_INPUTS = {
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


def all_subsets(items: set[str]) -> list[set[str]]:
    ordered = sorted(items)
    subsets: list[set[str]] = []
    for size in range(len(ordered) + 1):
        for combo in combinations(ordered, size):
            subsets.append(set(combo))
    return subsets


def closes_elementary_route(inputs: set[str]) -> bool:
    return ELEMENTARY_INPUTS <= inputs


def closes_parent_bridge(inputs: set[str]) -> bool:
    return PARENT_FIXED_INPUTS <= inputs and bool(PARENT_ROUTE_INPUTS & inputs)


def closes_hw1(inputs: set[str]) -> bool:
    return HW1_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def pauli_data() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    i2 = np.eye(2, dtype=complex)
    return sx, sy, sz, i2


def uz(theta: float) -> np.ndarray:
    _, _, sz, i2 = pauli_data()
    return np.cos(theta / 2.0) * i2 - 1j * np.sin(theta / 2.0) * sz


def finite_elementary_checks(audit: Audit) -> None:
    sx, sy, sz, i2 = pauli_data()
    u_quarter = uz(np.pi / 2.0)
    u_2pi = uz(2.0 * np.pi)
    u_4pi = uz(4.0 * np.pi)
    trivial = i2
    scalar = np.exp(1j * np.pi / 7.0) * i2
    up = np.array([1.0 + 0j, 0.0 + 0j])

    audit.check("faithful state law is unitary", np.allclose(u_quarter.conj().T @ u_quarter, i2))
    audit.check("faithful state law has 2pi -> -I", np.allclose(u_2pi, -i2))
    audit.check("faithful state law has 4pi -> I", np.allclose(u_4pi, i2))
    audit.check("faithful state law rotates sigma_x to sigma_y", np.allclose(u_quarter @ sx @ u_quarter.conj().T, sy))
    audit.check("faithful state law leaves sigma_z fixed", np.allclose(u_quarter @ sz @ u_quarter.conj().T, sz))

    center_blind = all(
        np.allclose(u_quarter @ op @ u_quarter.conj().T, (-u_quarter) @ op @ (-u_quarter).conj().T)
        for op in [sx, sy, sz]
    )
    audit.check("operator-frame adjoint is blind to SU2 center", center_blind)
    audit.check("center-related states differ by sign", np.allclose((-u_quarter) @ up, -(u_quarter @ up)))

    audit.check("trivial state lift is unitary", np.allclose(trivial.conj().T @ trivial, i2))
    audit.check("trivial state lift leaves sigma_x fixed", np.allclose(trivial @ sx @ trivial.conj().T, sx))
    audit.check("trivial state lift fails faithful covariance on sigma_x", not np.allclose(trivial @ sx @ trivial.conj().T, sy))
    audit.check("global scalar lift preserves operator-frame constraints", np.allclose(scalar @ sx @ scalar.conj().T, sx))
    audit.check("faithful and scalar state laws differ on state vector", not np.allclose(u_quarter @ up, scalar @ up))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        TARGET,
        DECISION,
        CURRENT,
        SELECTOR_TARGET,
        SELECTOR_DECISION,
        SELECTOR_CURRENT,
        PARENT_TARGET,
        PARENT_DECISION,
        PARENT_CURRENT,
        KS_CHILD_TARGET,
        KS_CHILD_DECISION,
        KS_CHILD_CURRENT,
        HW1_TARGET,
        GOAL,
        KOIDE_FIREWALL,
        MATTER_ATTACHMENT,
        CARRIER_ATTACHMENT,
        SU2_MERGER,
        PER_SITE_SPIN,
        CL31_EXTENSION,
        BOOST_NO_GO,
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
        "Koide R-Eta Elementary Physical State-Rotation Law Target Discriminator",
        "Koide R-Eta Elementary Physical State-Rotation Law Ratification Decision Packet",
        "Koide R-Eta Elementary Physical State-Rotation Law Current-Surface No-Go",
        "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED",
        "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_TEXT_LOCK",
        "MATTER_ATTACHMENT_ELEMENTARY_ROUTE_ACCEPTED",
        "OPERATOR_FRAME_MERGER_ACCEPTED",
        "PER_SITE_PAULI_SPIN_HALF_MODULE_ACCEPTED",
        "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
        "CL31_EXTENSION_MODULE_BOUNDARY_ACCEPTED",
        "BOOST_ACTION_FAITH_ANALOGY_ACCEPTED",
        "FINITE_SU2_DOUBLE_COVER_ACTION_CHECK",
        "FINITE_ADJOINT_CENTER_BLINDNESS_CHECK",
        "FINITE_TRIVIAL_STATE_LIFT_COUNTERMODEL_CHECK",
        "FINITE_FAITHFUL_SPINOR_STATE_LAW_CHECK",
        "ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "NO_KS_ROUTE_THEOREM_INPUT",
        "NO_PHYSICAL_MATTER_STATE_BRIDGE_INPUT",
        "NO_HW1_OR_CARRIER_CLOSURE_INPUT",
        "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
        "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md",
        "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md",
        "INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md",
        "PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md",
        "CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md",
        "QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md",
        "open `#5016`",
        "merged `#5027`",
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
    full_route = set(ELEMENTARY_INPUTS)
    audit.check("full elementary route contract closes target", closes_elementary_route(full_route))
    audit.check("current surface does not close elementary target", not closes_elementary_route(CURRENT_SURFACE_INPUTS))

    removed_failures = []
    for missing in sorted(ELEMENTARY_INPUTS):
        reduced = set(full_route)
        reduced.remove(missing)
        failed = not closes_elementary_route(reduced)
        removed_failures.append(failed)
        audit.check(f"elementary route contract fails without input {missing}", failed)
    audit.check("every one-input-removed elementary route subset fails", all(removed_failures))

    elementary_consequence = {"ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED"}
    parent_fixed = set(PARENT_FIXED_INPUTS)
    parent_with_elementary = parent_fixed | elementary_consequence
    parent_with_ks = parent_fixed | {"KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED"}
    audit.check("elementary consequence alone does not close parent bridge", not closes_parent_bridge(elementary_consequence))
    audit.check("parent bridge closes with elementary route certificate", closes_parent_bridge(parent_with_elementary))
    audit.check("parent bridge also closes with sibling KS route certificate", closes_parent_bridge(parent_with_ks))
    audit.check("parent bridge fixed inputs alone do not close", not closes_parent_bridge(parent_fixed))
    audit.check("elementary consequence alone does not close HW1", not closes_hw1(elementary_consequence))
    audit.check("elementary consequence alone does not close hydrogen", not closes_hydrogen(elementary_consequence))

    minimal_parent_subsets = [
        subset
        for subset in all_subsets(PARENT_FIXED_INPUTS | PARENT_ROUTE_INPUTS)
        if closes_parent_bridge(subset)
        and not any(other < subset and closes_parent_bridge(other) for other in all_subsets(PARENT_FIXED_INPUTS | PARENT_ROUTE_INPUTS))
    ]
    audit.check(
        "parent bridge minimal closures are KS route or elementary route",
        sorted(map(sorted, minimal_parent_subsets)) == sorted(map(sorted, [parent_with_elementary, parent_with_ks])),
    )

    section("Finite elementary state-law checks")
    finite_elementary_checks(audit)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    parent_packet = "\n".join([read(PARENT_TARGET), read(PARENT_DECISION), read(PARENT_CURRENT)])
    selector_packet = "\n".join([read(SELECTOR_TARGET), read(SELECTOR_DECISION), read(SELECTOR_CURRENT)])
    ks_child_packet = "\n".join([read(KS_CHILD_TARGET), read(KS_CHILD_DECISION), read(KS_CHILD_CURRENT)])
    matter_attachment = read(MATTER_ATTACHMENT)
    carrier_attachment = read(CARRIER_ATTACHMENT)
    su2_merger = read(SU2_MERGER)
    per_site_spin = read(PER_SITE_SPIN)
    cl31_extension = read(CL31_EXTENSION)
    boost_no_go = read(BOOST_NO_GO)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("parent bridge packet", parent_packet),
    ]:
        audit.check(
            f"{label} references elementary route lane",
            TARGET.name in container
            and DECISION.name in container
            and CURRENT.name in container
            and "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED" in container,
        )

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("elementary route packet", packet),
    ]:
        audit.check(
            f"{label} references elementary selector child lane",
            SELECTOR_TARGET.name in container
            and SELECTOR_DECISION.name in container
            and SELECTOR_CURRENT.name in container
            and "ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED" in container,
        )

    audit.check("elementary packet references parent bridge target", PARENT_TARGET.name in packet)
    audit.check("elementary packet references sibling KS child target", KS_CHILD_TARGET.name in packet)
    audit.check("selector child packet references elementary route target", TARGET.name in selector_packet)
    audit.check("selector child packet references sibling KS child target", KS_CHILD_TARGET.name in selector_packet)
    audit.check("KS child packet keeps elementary route as sibling", "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED" in ks_child_packet)
    audit.check("HW1 target still consumes parent bridge only", "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED" in read(HW1_TARGET))

    matter_flat = flat(matter_attachment)
    carrier_norm = flat(carrier_attachment).replace("C\u00b2", "C^2").replace("\u00bd", "1/2")
    su2_flat = flat(su2_merger)
    per_site_flat = flat(per_site_spin)
    cl31_norm = flat(cl31_extension).replace("C\u00b2", "C^2")
    boost_flat = flat(boost_no_go)

    audit.check(
        "matter attachment names elementary route as admitted-not-forced",
        "the elementary route" in matter_flat
        and "admitted-not-forced" in matter_flat
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
        and "does not introduce or approve any new axiom" in su2_flat,
    )
    audit.check(
        "per-site spin source withholds physical matter generator",
        "does not, by itself, identify this action with the physical spin generator" in per_site_flat,
    )
    audit.check(
        "Cl31 extension does not transport state law onto per-site module",
        "abstract finite-dimensional real Clifford" in cl31_norm
        and "per-site site module is `C^2`-valued" in cl31_norm,
    )
    audit.check(
        "boost no-go records action-faith attachment residual",
        "live residual is the attachment step" in boost_flat
        and "local operator algebra by itself" in boost_flat,
    )

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "elementary_physical_state_rotation_law_primitive",
        "elementary_state_attachment_selector_primitive",
        "physical_matter_state_law_primitive",
        "hw1_physical_generation_locus_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    primitive_flat = flat(primitive_text)
    for excluded in ["selector", "readout bridge", "state-selection rule", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_flat)

    section("Open/merged PR and non-claim boundaries")
    pr_markers = [
        "`#5016` zero-import hydrogen retained lane bundle",
        "`#5027` Koide custody AC gate-edge repair",
        "`#5023` Koide W4 audit-readiness repairs",
        "`#5024` Koide W4 gate-note premise minimization + substep1-bridge rebase",
        "`#5026` Koide custody L4 retained-successor re-point",
        "`#5021` primitive-retirement review",
        "`#5014` record-formation front domain wall",
        "`#5017` domain-wall edge anomaly inflow spectral flow",
        "`#5018` domain-wall edge content vs SM chiral map",
        "clean/dirty/check labels are not proof inputs",
    ]
    for marker in pr_markers:
        audit.check(f"PR marker present: {marker}", marker in packet)

    explicit_nonclaims = [
        "No derivation or ratification of",
        "`ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED`.",
        "No derivation or ratification of `ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED`.",
        "`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "`CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`.",
        "No R-eta, h-class, h-unit, `K1`/`K3`/`K4`, Koide mass, electron mass,",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden_overclaims = [
        "This note ratifies elementary physical state-rotation law",
        "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED is supplied",
        "ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED is supplied",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED is supplied",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED is supplied",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This note claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in packet)

    audit.summary()


if __name__ == "__main__":
    main()
