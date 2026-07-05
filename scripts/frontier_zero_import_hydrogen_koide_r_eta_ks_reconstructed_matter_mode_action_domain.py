#!/usr/bin/env python3
"""Verifier for the Koide R-eta KS reconstructed matter-mode action-domain lane."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_TARGET_DISCRIMINATOR_2026-07-05.md"
DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SELECTOR_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_STATE_ACTION_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md"
SELECTOR_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_STATE_ACTION_SELECTOR_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SELECTOR_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_STATE_ACTION_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
ACTION_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
ACTION_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
ACTION_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
KS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
KS_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SCALAR_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
SCALAR_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SCALAR_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PARENT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
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


DOMAIN_INPUTS = {
    "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_TEXT_LOCK",
    "MATTER_ATTACHMENT_KS_REDUCTION_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "OPERATOR_FRAME_MERGER_ACCEPTED",
    "PER_SITE_PAULI_SPIN_HALF_MODULE_ACCEPTED",
    "CL31_EXTENSION_MODULE_BOUNDARY_ACCEPTED",
    "KS_PHASE_FORCING_SURFACE_ACCEPTED",
    "GRASSMANN_CAR_SURFACE_ACCEPTED",
    "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
    "STAGGERED_REALIZATION_GATE_SURFACE_ACCEPTED",
    "FINITE_KS_SCALARIZATION_DOMAIN_CHECK",
    "FINITE_GRASSMANN_SINGLE_PAIR_MODE_CHECK",
    "FINITE_CHIRALITY_PARITY_ACTION_DOMAIN_CHECK",
    "NO_PHYSICAL_ROTATION_ACTION_SELECTOR_INPUT",
    "NO_FAITHFUL_SELECTOR_OR_ACTION_LAW_INPUT",
    "NO_SPINFUL_SCALAR_LIFT_EXCLUSION_INPUT",
    "NO_PARENT_BRIDGE_OR_HW1_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_SURFACE_INPUTS = DOMAIN_INPUTS - {"OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"}

SELECTOR_INPUTS = {
    "FAITHFUL_KS_STATE_ACTION_SELECTOR_TEXT_LOCK",
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
    "FINITE_KS_SCALAR_COMPENSATOR_NONSELECTOR_CHECK",
    "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED",
    "PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED",
    "NO_OPERATOR_FRAME_SELECTOR_INPUT",
    "NO_SCALAR_COMPENSATOR_INPUT",
    "NO_SPINFUL_SCALAR_LIFT_EXCLUSION_INPUT",
    "NO_ACTION_LAW_OR_KS_ROUTE_CLOSURE_INPUT",
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


def closes_domain(inputs: set[str]) -> bool:
    return DOMAIN_INPUTS <= inputs


def closes_selector(inputs: set[str]) -> bool:
    return SELECTOR_INPUTS <= inputs


def closes_action_law(inputs: set[str]) -> bool:
    return ACTION_INPUTS <= inputs


def closes_ks_route(inputs: set[str]) -> bool:
    return KS_ROUTE_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def pauli_data() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    i2 = np.eye(2, dtype=complex)
    return sx, sy, sz, i2


def omega(x: tuple[int, int, int]) -> np.ndarray:
    sx, sy, sz, i2 = pauli_data()

    def power(matrix: np.ndarray, exponent: int) -> np.ndarray:
        return i2 if exponent % 2 == 0 else matrix

    return power(sx, x[0]) @ power(sy, x[1]) @ power(sz, x[2])


def eta(x: tuple[int, int, int], mu: int) -> int:
    if mu == 0:
        return 1
    if mu == 1:
        return -1 if x[0] % 2 else 1
    return -1 if (x[0] + x[1]) % 2 else 1


def finite_domain_checks(audit: Audit) -> None:
    sx, sy, sz, i2 = pauli_data()
    gammas = [sx, sy, sz]

    samples = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 1)]
    scalarized = []
    unitary_omega = []
    scalar_commutes = []
    for x in samples:
        unitary_omega.append(np.allclose(omega(x).conj().T @ omega(x), i2))
        for mu, gamma in enumerate(gammas):
            xp = list(x)
            xp[mu] += 1
            y = tuple(xp)
            link = omega(x).conj().T @ gamma @ omega(y)
            expected = eta(x, mu) * i2
            scalarized.append(np.allclose(link, expected))
            scalar_commutes.append(all(np.allclose(link @ g, g @ link) for g in gammas))

    audit.check("KS Omega maps are unitary on sampled sites", all(unitary_omega))
    audit.check("KS scalarization yields eta_mu scalar link phases", all(scalarized))
    audit.check("KS scalar link phases are operator-scalar support only", all(scalar_commutes))

    c = np.array([[0, 1], [0, 0]], dtype=complex)
    cdag = c.conj().T
    parity = np.array([[1, 0], [0, -1]], dtype=complex)
    number = cdag @ c
    audit.check("single-pair Grassmann mode is nilpotent", np.allclose(c @ c, np.zeros((2, 2))))
    audit.check("single-pair CAR closes on identity", np.allclose(c @ cdag + cdag @ c, i2))
    audit.check("single-pair matter mode has two-state number spectrum", np.allclose(number @ number, number) and np.isclose(np.trace(i2), 2))
    audit.check("single-pair operator is parity odd", np.allclose(parity @ c + c @ parity, np.zeros((2, 2))))

    edges = []
    anticommutes = []
    for x in samples:
        eps_x = -1 if sum(x) % 2 else 1
        for mu in range(3):
            xp = list(x)
            xp[mu] += 1
            y = tuple(xp)
            eps_y = -1 if sum(y) % 2 else 1
            edges.append(eps_y == -eps_x)
            anticommutes.append(eps_x + eps_y == 0)

    audit.check("staggered chirality flips on every sampled coordinate edge", all(edges))
    audit.check("nearest-neighbor epsilon grading anticommutes edgewise", all(anticommutes))


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
        ACTION_TARGET,
        ACTION_DECISION,
        ACTION_CURRENT,
        KS_TARGET,
        KS_DECISION,
        KS_CURRENT,
        SCALAR_TARGET,
        SCALAR_DECISION,
        SCALAR_CURRENT,
        GOAL,
        KOIDE_FIREWALL,
        PARENT_TARGET,
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
        "Koide R-Eta KS Reconstructed Matter-Mode Action-Domain Target Discriminator",
        "Koide R-Eta KS Reconstructed Matter-Mode Action-Domain Ratification Decision Packet",
        "Koide R-Eta KS Reconstructed Matter-Mode Action-Domain Current-Surface No-Go",
        "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED",
        "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_TEXT_LOCK",
        "MATTER_ATTACHMENT_KS_REDUCTION_ACCEPTED",
        "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
        "OPERATOR_FRAME_MERGER_ACCEPTED",
        "PER_SITE_PAULI_SPIN_HALF_MODULE_ACCEPTED",
        "CL31_EXTENSION_MODULE_BOUNDARY_ACCEPTED",
        "KS_PHASE_FORCING_SURFACE_ACCEPTED",
        "GRASSMANN_CAR_SURFACE_ACCEPTED",
        "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
        "STAGGERED_REALIZATION_GATE_SURFACE_ACCEPTED",
        "FINITE_KS_SCALARIZATION_DOMAIN_CHECK",
        "FINITE_GRASSMANN_SINGLE_PAIR_MODE_CHECK",
        "FINITE_CHIRALITY_PARITY_ACTION_DOMAIN_CHECK",
        "NO_PHYSICAL_ROTATION_ACTION_SELECTOR_INPUT",
        "NO_FAITHFUL_SELECTOR_OR_ACTION_LAW_INPUT",
        "NO_SPINFUL_SCALAR_LIFT_EXCLUSION_INPUT",
        "NO_PARENT_BRIDGE_OR_HW1_INPUT",
        "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED",
        "FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
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
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_STATE_ACTION_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
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
    full_route = set(DOMAIN_INPUTS)
    audit.check("full action-domain contract closes target", closes_domain(full_route))
    audit.check("current surface does not close action-domain target", not closes_domain(CURRENT_SURFACE_INPUTS))

    removed_failures = []
    for missing in sorted(DOMAIN_INPUTS):
        reduced = set(full_route)
        reduced.remove(missing)
        failed = not closes_domain(reduced)
        removed_failures.append(failed)
        audit.check(f"domain contract fails without input {missing}", failed)
    audit.check("every one-input-removed domain subset fails", all(removed_failures))

    domain_consequence = {"KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED"}
    selector_with_domain = set(SELECTOR_INPUTS)
    selector_without_physical = selector_with_domain - {"PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED"}
    selector_without_domain = selector_with_domain - {"KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED"}
    audit.check("domain consequence alone does not close selector", not closes_selector(domain_consequence))
    audit.check("domain consequence plus full selector inputs closes selector", closes_selector(selector_with_domain))
    audit.check("selector cannot close without physical rotation action selector", not closes_selector(selector_without_physical))
    audit.check("selector cannot close without action-domain input", not closes_selector(selector_without_domain))
    audit.check("domain consequence alone does not close action law", not closes_action_law(domain_consequence))
    audit.check("domain consequence alone does not close KS route", not closes_ks_route(domain_consequence))
    audit.check("domain consequence alone does not close hydrogen", not closes_hydrogen(domain_consequence))

    section("Finite action-domain support checks")
    finite_domain_checks(audit)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    selector_packet = "\n".join([read(SELECTOR_TARGET), read(SELECTOR_DECISION), read(SELECTOR_CURRENT)])
    action_packet = "\n".join([read(ACTION_TARGET), read(ACTION_DECISION), read(ACTION_CURRENT)])
    ks_packet = "\n".join([read(KS_TARGET), read(KS_DECISION), read(KS_CURRENT)])
    scalar_packet = "\n".join([read(SCALAR_TARGET), read(SCALAR_DECISION), read(SCALAR_CURRENT)])
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
        ("selector packet", selector_packet),
    ]:
        audit.check(
            f"{label} references action-domain lane",
            TARGET.name in container
            and DECISION.name in container
            and CURRENT.name in container
            and "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED" in container,
        )

    audit.check("domain packet references selector parent target", SELECTOR_TARGET.name in packet)
    audit.check("selector packet still names action-domain input", "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED" in selector_packet)
    audit.check("selector packet still names physical action-selector sibling", "PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED" in selector_packet)
    audit.check("action packet still names faithful selector", "FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED" in action_packet)
    audit.check("KS packet still names action-law input", "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED" in ks_packet)
    audit.check("scalar packet keeps action law as sibling non-input", "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED" in scalar_packet)
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
        "KS forcing names scalarization condition",
        "scalarization condition" in ks_flat
        and "eta" in ks_flat
        and "I_2" in ks_forcing,
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
        "ks_reconstructed_matter_mode_action_domain_primitive",
        "physical_rotation_action_selector_primitive",
        "faithful_ks_state_action_selector_primitive",
        "ks_spin_lift_physical_action_primitive",
        "physical_matter_state_law_primitive",
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
        "`#5021` primitive-retirement review: meta gate map, no retirements",
        "`#5014` record-formation front domain wall",
        "`#5017` domain-wall edge anomaly inflow spectral flow",
        "`#5018` domain-wall edge content vs SM chiral map",
        "clean/dirty/check labels are not proof inputs",
    ]
    for marker in pr_markers:
        audit.check(f"PR marker present: {marker}", marker in packet)

    explicit_nonclaims = [
        "`KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED`.",
        "`PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED`.",
        "`FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED`.",
        "No derivation or ratification of `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED`.",
        "`SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`.",
        "`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "retained hydrogen",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
        "No claim that #5014, #5017, #5018, #5023, #5024, #5026, or #5027 supplies",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden_overclaims = [
        "This note ratifies KS reconstructed matter-mode action domain",
        "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED is supplied",
        "PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED is supplied",
        "FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED is supplied",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED is supplied",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED is supplied",
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
