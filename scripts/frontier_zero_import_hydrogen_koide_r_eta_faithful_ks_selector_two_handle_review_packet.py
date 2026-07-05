#!/usr/bin/env python3
"""Verifier for the faithful-KS selector two-handle review packet."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_SELECTOR_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
DOMAIN_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_TARGET_DISCRIMINATOR_2026-07-05.md"
DOMAIN_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RATIFICATION_DECISION_PACKET_2026-07-05.md"
DOMAIN_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PHYSICAL_SELECTOR_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_ROTATION_ACTION_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_SELECTOR_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_ROTATION_ACTION_SELECTOR_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PHYSICAL_SELECTOR_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_ROTATION_ACTION_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
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
BRIDGE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
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
PR5030 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_MULTISITE_PAULI_PR5030_CARRIER_PROVENANCE_IMPACT_DISCRIMINATOR_2026-07-05.md"
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

PHYSICAL_SELECTOR_INPUTS = {
    "PHYSICAL_ROTATION_ACTION_SELECTOR_TEXT_LOCK",
    "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "OPERATOR_FRAME_MERGER_ACCEPTED",
    "PER_SITE_PAULI_SPIN_HALF_MODULE_ACCEPTED",
    "CL31_EXTENSION_MODULE_BOUNDARY_ACCEPTED",
    "KS_PHASE_FORCING_SURFACE_ACCEPTED",
    "FINITE_SU2_DOUBLE_COVER_ACTION_CHECK",
    "FINITE_ADJOINT_CENTER_BLINDNESS_CHECK",
    "FINITE_TRIVIAL_SCALAR_LIFT_NONSELECTOR_CHECK",
    "FINITE_FAITHFUL_SPINOR_ROTATION_COVARIANCE_CHECK",
    "NO_OPERATOR_FRAME_SELECTOR_INPUT",
    "NO_KS_SCALAR_COMPENSATOR_INPUT",
    "NO_SPINFUL_SCALAR_LIFT_EXCLUSION_INPUT",
    "NO_FAITHFUL_SELECTOR_OR_ACTION_LAW_INPUT",
    "NO_PARENT_BRIDGE_OR_HW1_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

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


def closes_domain(inputs: set[str]) -> bool:
    return DOMAIN_INPUTS <= inputs


def closes_physical_selector(inputs: set[str]) -> bool:
    return PHYSICAL_SELECTOR_INPUTS <= inputs


def closes_selector(inputs: set[str]) -> bool:
    return SELECTOR_INPUTS <= inputs


def closes_action_law(inputs: set[str]) -> bool:
    return ACTION_INPUTS <= inputs


def closes_ks_route(inputs: set[str]) -> bool:
    return KS_ROUTE_INPUTS <= inputs


def closes_scalar(inputs: set[str]) -> bool:
    return SCALAR_INPUTS <= inputs


def closes_bridge(inputs: set[str]) -> bool:
    return BRIDGE_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def pauli_data() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    i2 = np.eye(2, dtype=complex)
    return sx, sy, sz, i2


def omega(site: tuple[int, int, int]) -> np.ndarray:
    sx, sy, sz, i2 = pauli_data()

    def power(matrix: np.ndarray, exponent: int) -> np.ndarray:
        return i2 if exponent % 2 == 0 else matrix

    return power(sx, site[0]) @ power(sy, site[1]) @ power(sz, site[2])


def eta(site: tuple[int, int, int], mu: int) -> int:
    if mu == 0:
        return 1
    if mu == 1:
        return -1 if site[0] % 2 else 1
    if mu == 2:
        return -1 if (site[0] + site[1]) % 2 else 1
    raise ValueError(mu)


def uz(theta: float) -> np.ndarray:
    _, _, sz, i2 = pauli_data()
    return np.cos(theta / 2.0) * i2 - 1j * np.sin(theta / 2.0) * sz


def finite_support_checks(audit: Audit) -> None:
    sx, sy, sz, i2 = pauli_data()
    gammas = [sx, sy, sz]
    samples = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 1)]

    scalarized = []
    scalar_commutes = []
    unitary_omega = []
    for site in samples:
        unitary_omega.append(np.allclose(omega(site).conj().T @ omega(site), i2))
        for mu, gamma in enumerate(gammas):
            shifted = list(site)
            shifted[mu] += 1
            link = omega(site).conj().T @ gamma @ omega(tuple(shifted))
            expected = eta(site, mu) * i2
            scalarized.append(np.allclose(link, expected))
            scalar_commutes.append(all(np.allclose(link @ generator, generator @ link) for generator in gammas))

    audit.check("KS Omega maps are unitary on sampled sites", all(unitary_omega))
    audit.check("KS scalarization yields eta_mu scalar link phases", all(scalarized))
    audit.check("KS scalar link phases commute with Pauli generators", all(scalar_commutes))

    c = np.array([[0, 1], [0, 0]], dtype=complex)
    cdag = c.conj().T
    parity = np.array([[1, 0], [0, -1]], dtype=complex)
    number = cdag @ c
    audit.check("single-pair Grassmann mode is nilpotent", np.allclose(c @ c, np.zeros((2, 2))))
    audit.check("single-pair CAR closes on identity", np.allclose(c @ cdag + cdag @ c, i2))
    audit.check("single-pair number operator is a projection", np.allclose(number @ number, number))
    audit.check("single-pair operator is parity odd", np.allclose(parity @ c + c @ parity, np.zeros((2, 2))))

    edge_flips = []
    for site in samples:
        eps_site = -1 if sum(site) % 2 else 1
        for mu in range(3):
            shifted = list(site)
            shifted[mu] += 1
            eps_shifted = -1 if sum(shifted) % 2 else 1
            edge_flips.append(eps_site + eps_shifted == 0)
    audit.check("staggered chirality flips on sampled coordinate edges", all(edge_flips))

    u_half = uz(np.pi / 2.0)
    u_2pi = uz(2.0 * np.pi)
    u_4pi = uz(4.0 * np.pi)
    scalar = np.exp(1j * np.pi / 5.0) * i2
    up = np.array([1.0 + 0j, 0.0 + 0j])

    audit.check("faithful spin lift has 2pi -> -I", np.allclose(u_2pi, -i2))
    audit.check("faithful spin lift has 4pi -> I", np.allclose(u_4pi, i2))
    audit.check("faithful z rotation sends sigma_x to sigma_y", np.allclose(u_half @ sx @ u_half.conj().T, sy))
    audit.check("faithful z rotation leaves sigma_z fixed", np.allclose(u_half @ sz @ u_half.conj().T, sz))
    audit.check("trivial scalar lift leaves sigma_x fixed", np.allclose(scalar @ sx @ scalar.conj().T, sx))
    audit.check("trivial scalar lift does not rotate sigma_x to sigma_y", not np.allclose(scalar @ sx @ scalar.conj().T, sy))
    audit.check("adjoint action is blind to SU2 center", all(np.allclose(u_half @ op @ u_half.conj().T, (-u_half) @ op @ (-u_half).conj().T) for op in gammas))
    audit.check("center-related spinors differ by sign", np.allclose((-u_half) @ up, -(u_half @ up)))
    audit.check("faithful and scalar actions differ on sigma_x covariance", not np.allclose(u_half @ sx @ u_half.conj().T, scalar @ sx @ scalar.conj().T))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        KOIDE_FIREWALL,
        DOMAIN_TARGET,
        DOMAIN_DECISION,
        DOMAIN_CURRENT,
        PHYSICAL_SELECTOR_TARGET,
        PHYSICAL_SELECTOR_DECISION,
        PHYSICAL_SELECTOR_CURRENT,
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
        BRIDGE_TARGET,
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
        "Faithful KS Selector Two-Handle Review Packet",
        "grouped faithful-KS selector review packet / adjacent child-handle bundling",
        "scripts/frontier_zero_import_hydrogen_koide_r_eta_faithful_ks_selector_two_handle_review_packet.py",
        "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED",
        "PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED",
        "FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "reconstructed KS/Grassmann matter-mode action domain",
        "faithful physical SU(2) spin lift",
        "review compression only",
        "two child handles can be reviewed together",
        "The approved primitive registry was checked",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
        "open, audit-successful at refresh",
        "`#5030` multisite Pauli finite-carrier provenance",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    domain_full = set(DOMAIN_INPUTS)
    physical_full = set(PHYSICAL_SELECTOR_INPUTS)
    selector_full = set(SELECTOR_INPUTS)
    both_child_handles = {
        "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED",
        "PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED",
    }
    selector_handle = {"FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED"}

    audit.check("full action-domain contract closes child handle", closes_domain(domain_full))
    audit.check("action-domain current surface fails without owner/audit", not closes_domain(domain_full - {"OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"}))
    audit.check("full physical selector contract closes child handle", closes_physical_selector(physical_full))
    audit.check("physical selector current surface fails without domain/owner/audit", not closes_physical_selector(physical_full - {"KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED", "OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"}))
    audit.check("physical selector cannot close without action domain", not closes_physical_selector(physical_full - {"KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED"}))
    audit.check("two child handles alone do not close parent faithful selector", not closes_selector(both_child_handles))
    audit.check("full parent faithful selector closes with both child handles", closes_selector(selector_full))

    for missing in both_child_handles | {"OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"}:
        reduced = set(selector_full)
        reduced.remove(missing)
        audit.check(f"parent faithful selector fails without {missing}", not closes_selector(reduced))

    audit.check("domain consequence alone does not close physical selector", not closes_physical_selector({"KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED"}))
    audit.check("physical selector consequence alone does not close parent selector", not closes_selector({"PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED"}))
    audit.check("selector consequence alone does not close action law", not closes_action_law(selector_handle))
    audit.check("selector consequence alone does not close scalar-lift exclusion", not closes_scalar(selector_handle))
    audit.check("selector consequence alone does not close KS child route", not closes_ks_route(selector_handle))
    audit.check("selector consequence alone does not close physical matter-state bridge", not closes_bridge(selector_handle))
    audit.check("selector consequence alone does not close hydrogen", not closes_hydrogen(selector_handle))
    audit.check("full action-law contract closes action law", closes_action_law(set(ACTION_INPUTS)))
    audit.check("full scalar-lift contract closes scalar-lift exclusion", closes_scalar(set(SCALAR_INPUTS)))
    audit.check("full KS child route closes KS route", closes_ks_route(set(KS_ROUTE_INPUTS)))
    audit.check("full bridge route closes physical matter-state bridge", closes_bridge(set(BRIDGE_INPUTS)))

    section("Finite support checks")
    finite_support_checks(audit)

    section("Authority boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    for label, container in [("goal packet", goal), ("Koide firewall", firewall)]:
        audit.check(
            f"{label} references grouped faithful-KS selector two-handle packet",
            NOTE.name in container and "PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED" in container,
        )

    domain_packet = "\n".join([read(DOMAIN_TARGET), read(DOMAIN_DECISION), read(DOMAIN_CURRENT)])
    physical_packet = "\n".join([read(PHYSICAL_SELECTOR_TARGET), read(PHYSICAL_SELECTOR_DECISION), read(PHYSICAL_SELECTOR_CURRENT)])
    selector_packet = "\n".join([read(SELECTOR_TARGET), read(SELECTOR_DECISION), read(SELECTOR_CURRENT)])
    action_packet = "\n".join([read(ACTION_TARGET), read(ACTION_DECISION), read(ACTION_CURRENT)])
    ks_packet = "\n".join([read(KS_TARGET), read(KS_DECISION), read(KS_CURRENT)])
    scalar_packet = "\n".join([read(SCALAR_TARGET), read(SCALAR_DECISION), read(SCALAR_CURRENT)])

    audit.check("domain packet references selector parent target", SELECTOR_TARGET.name in domain_packet)
    audit.check("physical selector packet references action-domain target", DOMAIN_TARGET.name in physical_packet)
    audit.check("selector packet consumes both grouped child handles", all(handle in selector_packet for handle in both_child_handles))
    audit.check("action-law packet still names selector input", "FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED" in action_packet)
    audit.check("KS packet still names action-law and scalar-lift inputs", "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED" in ks_packet and "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED" in ks_packet)
    audit.check("scalar packet keeps action law as sibling non-input", "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED" in scalar_packet)

    matter_flat = flat(read(MATTER_ATTACHMENT))
    carrier_flat = flat(read(CARRIER_ATTACHMENT)).replace("\u00bd", "1/2").replace("C\u00b2", "C^2")
    su2_flat = flat(read(SU2_MERGER))
    per_site_flat = flat(read(PER_SITE_SPIN))
    cl31_flat = flat(read(CL31_EXTENSION)).replace("C\u00b2", "C^2")
    boost_flat = flat(read(BOOST_NO_GO))
    ks_flat = flat(read(KS_FORCING))
    grassmann_text = read(GRASSMANN_FORCING)
    chirality_flat = flat(read(CHIRALITY_PARITY))
    realization_flat = flat(read(REALIZATION_GATE))
    pr5030_flat = flat(read(PR5030))

    audit.check(
        "matter attachment keeps state-law residual separate",
        "unless a KS-to-physical-state-law bridge or an elementary state-law theorem is supplied" in matter_flat,
    )
    audit.check(
        "carrier attachment keeps state law separate",
        "j=1/2 state law is a separate datum" in carrier_flat
        and "does not prove the KS/Grassmann physical-state-law bridge" in carrier_flat,
    )
    audit.check(
        "SU2 merger is operator-level support",
        "operator-level identification" in su2_flat
        and "U(R) sigma_i U(R)^*" in read(SU2_MERGER),
    )
    audit.check(
        "per-site spin source withholds physical matter generator",
        "does not, by itself, identify this action with the physical spin generator" in per_site_flat,
    )
    audit.check(
        "Cl31 extension remains abstract algebra support",
        "abstract finite-dimensional real Clifford" in cl31_flat
        and "per-site site module is `C^2`-valued" in cl31_flat,
    )
    audit.check(
        "boost no-go records action-faith residual",
        "local operator algebra by itself" in boost_flat
        and "live residual is the attachment step" in boost_flat,
    )
    audit.check(
        "KS forcing names scalarization condition",
        "scalarization condition" in ks_flat and "I_2" in read(KS_FORCING),
    )
    audit.check(
        "Grassmann forcing remains bounded/conditional",
        "Claim type:** bounded_theorem" in grassmann_text
        and "Conditional forcing: TRUE given `GL(F)`" in grassmann_text
        and "Unconditional forcing: FALSE" in grassmann_text,
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
    audit.check(
        "PR5030 finite provenance does not close selector route",
        "carrier-provenance" in pr5030_flat.lower()
        and "or hydrogen" in pr5030_flat.lower(),
    )

    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    audit.check("primitive registry contains minimal axioms", "minimal_axioms" in primitive_nodes)
    audit.check("primitive registry contains scale reference", "scale_reference_primitive" in primitive_nodes)
    audit.check("primitive registry contains kinetic isotropy", "kinetic_isotropy_primitive" in primitive_nodes)
    audit.check("primitive registry contains realized-state primitive", "realized_state_primitive" in primitive_nodes)
    absent_primitives = [
        "ks_reconstructed_matter_mode_action_domain_primitive",
        "physical_rotation_action_selector_primitive",
        "faithful_ks_state_action_selector_primitive",
        "ks_spin_lift_physical_action_primitive",
        "ks_to_physical_matter_state_spinor_law_primitive",
        "physical_matter_state_law_primitive",
        "hydrogen_primitive",
    ]
    for primitive in absent_primitives:
        audit.check(f"registry has no shortcut primitive: {primitive}", primitive not in primitive_nodes)

    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    for forbidden in [
        "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED",
        "PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED",
        "FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "hydrogen_primitive",
    ]:
        audit.check(f"approved primitive notes do not supply {forbidden}", forbidden not in primitive_text)

    section("Non-claim checks")
    for phrase in [
        "No derivation or ratification of\n  `KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED`.",
        "No derivation or ratification of\n  `PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED`.",
        "No derivation or ratification of\n  `FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED`.",
        "No R-eta, h-class, h-unit, K1/K2/K3/K4, Koide electron readout, `m_e`,",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]:
        audit.check(f"explicit non-claim present: {flat(phrase)}", flat(phrase) in note_flat)

    forbidden_overclaims = [
        "This packet ratifies",
        "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED is supplied",
        "PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED is supplied",
        "FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED is supplied",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED is supplied",
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
