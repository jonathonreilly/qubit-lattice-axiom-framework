#!/usr/bin/env python3
"""Verifier for the KS-route sigma.p two-handle review packet."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SIGMA_P_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
LINK_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_TARGET_DISCRIMINATOR_2026-07-05.md"
LINK_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
LINK_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KERNEL_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_TARGET_DISCRIMINATOR_2026-07-05.md"
KERNEL_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RATIFICATION_DECISION_PACKET_2026-07-05.md"
KERNEL_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SIGMA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md"
SIGMA_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SIGMA_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
TRIVIAL_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
SCALAR_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
SCALAR_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SCALAR_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
ACTION_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
KS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
BRIDGE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
HW1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
PR5011 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ETA_TWISTED_WALK_PR5011_IMPACT_DISCRIMINATOR_2026-07-05.md"
CHIRALITY_K2 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_MATTER_STATE_CHIRALITY_DOMAIN_WALL_IMPACT_DISCRIMINATOR_2026-07-05.md"
MATTER_ATTACHMENT = ROOT / "docs" / "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md"
CARRIER_ATTACHMENT = ROOT / "docs" / "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md"
CARRIER_RUNNER = ROOT / "scripts" / "carrier_attachment_chirality_gate_consolidation_runner.py"
KS_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
KINETIC_CLASS = ROOT / "docs" / "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
P_FLUX = ROOT / "docs" / "P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md"
Z_CERT = ROOT / "docs" / "STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


LINK_INPUTS = {
    "KS_ROUTE_MOMENTUM_LINK_PHASE_TEXT_LOCK",
    "TWO_FLUX_CLASS_KINETIC_SURFACE_ACCEPTED",
    "P_FLUX_WITHIN_SURFACE_SELECTION_ACCEPTED",
    "KAWAMOTO_SMIT_LINK_PHASE_REPRESENTATIVE_ACCEPTED",
    "FINITE_LINK_PHASE_AND_BLOCH_MOMENTUM_SUPPORT_CHECK",
    "WRAP_HOLONOMY_BOUNDARY_LOCK",
    "NO_FULL_KINETIC_SURFACE_RETIREMENT_INPUT",
    "NO_SPINFUL_KERNEL_OBJECT_THEOREM_INPUT",
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

KERNEL_INPUTS = {
    "KS_ROUTE_SPINFUL_KERNEL_OBJECT_TEXT_LOCK",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "SCALAR_KERNEL_COMPATIBILITY_ACCEPTED",
    "STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED",
    "KS_PHASE_FORCING_SURFACE_ACCEPTED",
    "KINETIC_TWO_RAY_SURFACE_ACCEPTED",
    "FINITE_SIGMA_DOT_P_OBJECT_SUPPORT_CHECK",
    "PAULI_VECTOR_KERNEL_OBJECT_BOUNDARY_LOCK",
    "NO_ROUTE_MOMENTUM_LINK_PHASE_INPUT",
    "NO_SIGMA_DOT_P_ROUTE_HANDOFF_INPUT",
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

SIGMA_INPUTS = {
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


def closes_link(inputs: set[str]) -> bool:
    return LINK_INPUTS <= inputs


def closes_kernel(inputs: set[str]) -> bool:
    return KERNEL_INPUTS <= inputs


def closes_sigma(inputs: set[str]) -> bool:
    return SIGMA_INPUTS <= inputs


def closes_scalar(inputs: set[str]) -> bool:
    return SCALAR_INPUTS <= inputs


def closes_ks(inputs: set[str]) -> bool:
    return KS_ROUTE_INPUTS <= inputs


def closes_bridge(inputs: set[str]) -> bool:
    return BRIDGE_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def eta(site: tuple[int, int, int], mu: int) -> int:
    if mu == 0:
        return 1
    if mu == 1:
        return -1 if site[0] % 2 else 1
    if mu == 2:
        return -1 if (site[0] + site[1]) % 2 else 1
    raise ValueError(mu)


def shift(site: tuple[int, int, int], mu: int, n: int) -> tuple[int, int, int]:
    values = list(site)
    values[mu] = (values[mu] + 1) % n
    return tuple(values)  # type: ignore[return-value]


def plaquette_flux(site: tuple[int, int, int], mu: int, nu: int, n: int) -> int:
    return eta(site, mu) * eta(shift(site, mu, n), nu) * eta(shift(site, nu, n), mu) * eta(site, nu)


def finite_support_checks(audit: Audit) -> None:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    i2 = np.eye(2, dtype=complex)
    sigma = [sx, sy, sz]

    p = np.array([2.0, -1.0, 3.0])
    kernel = sum(p[index] * sigma[index] for index in range(3))
    scalar_part = (np.trace(kernel) / 2.0) * i2
    noncentral = any(not np.allclose(kernel @ generator, generator @ kernel) for generator in sigma)
    eigvals = np.linalg.eigvalsh(kernel)
    norm_p = np.linalg.norm(p)

    audit.check("finite Pauli-vector object is traceless", np.allclose(np.trace(kernel), 0.0))
    audit.check("finite Pauli-vector object is noncentral", noncentral)
    audit.check("finite Pauli-vector object is not scalar", not np.allclose(kernel, scalar_part))
    audit.check("finite Pauli-vector eigenvalues are plus/minus |p|", np.allclose(sorted(eigvals), sorted([-norm_p, norm_p])))

    theta = np.pi / 2.0
    uz = np.cos(theta / 2.0) * i2 - 1j * np.sin(theta / 2.0) * sz
    audit.check("faithful z quarter-turn sends sigma_x to sigma_y", np.allclose(uz @ sx @ uz.conj().T, sy))
    audit.check("trivial scalar lift leaves sigma_x fixed", np.allclose(i2 @ sx @ i2, sx))

    n = 4
    sites = [(x, y, z) for x in range(n) for y in range(n) for z in range(n)]
    fluxes = [plaquette_flux(site, mu, nu, n) for site in sites for mu in range(3) for nu in range(mu + 1, 3)]
    audit.check("finite Kawamoto-Smit representative has uniform -1 plaquette flux", all(value == -1 for value in fluxes))
    audit.check("finite eta_1 representative is identically one", all(eta(site, 0) == 1 for site in sites))
    audit.check("finite eta_2 representative flips with x1", eta((0, 0, 0), 1) == 1 and eta((1, 0, 0), 1) == -1)
    audit.check("finite eta_3 representative flips with x1+x2", eta((0, 0, 0), 2) == 1 and eta((1, 0, 0), 2) == -1 and eta((1, 1, 0), 2) == 1)

    for t in [0.0, 0.13, -0.27]:
        zero_line = math.cos(math.pi / 2.0 + t) + math.cos(math.pi / 2.0 - t) + math.cos(math.pi / 2.0)
        audit.check(f"K0 Bloch zero-line support identity holds at t={t}", abs(zero_line) < 1e-12)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        KOIDE_FIREWALL,
        LINK_TARGET,
        LINK_DECISION,
        LINK_CURRENT,
        KERNEL_TARGET,
        KERNEL_DECISION,
        KERNEL_CURRENT,
        SIGMA_TARGET,
        SIGMA_DECISION,
        SIGMA_CURRENT,
        TRIVIAL_TARGET,
        SCALAR_TARGET,
        SCALAR_DECISION,
        SCALAR_CURRENT,
        ACTION_TARGET,
        KS_TARGET,
        BRIDGE_TARGET,
        HW1_TARGET,
        PR5011,
        CHIRALITY_K2,
        MATTER_ATTACHMENT,
        CARRIER_ATTACHMENT,
        CARRIER_RUNNER,
        KS_FORCING,
        KINETIC_CLASS,
        P_FLUX,
        Z_CERT,
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
        "KS Route Sigma.p Two-Handle Review Packet",
        "grouped KS-route review packet / adjacent child-handle bundling",
        "scripts/frontier_zero_import_hydrogen_koide_r_eta_ks_route_sigma_p_two_handle_review_packet.py",
        "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED",
        "KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED",
        "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED",
        "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "route momentum/link-phase input",
        "spinful kernel-object theorem",
        "review compression only",
        "two child handles can be reviewed together",
        "The approved primitive registry was checked",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    link_full = set(LINK_INPUTS)
    kernel_full = set(KERNEL_INPUTS)
    sigma_full = set(SIGMA_INPUTS)
    both_child_handles = {
        "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED",
        "KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED",
    }
    sigma_handle = {"SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED"}

    audit.check("full route momentum/link-phase contract closes child handle", closes_link(link_full))
    audit.check("route momentum/link-phase current surface fails without owner/audit", not closes_link(link_full - {"OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"}))
    audit.check("full spinful kernel-object contract closes child handle", closes_kernel(kernel_full))
    audit.check("spinful kernel-object current surface fails without owner/audit", not closes_kernel(kernel_full - {"OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"}))
    audit.check("two child handles alone do not close parent sigma.p route", not closes_sigma(both_child_handles))
    audit.check("full parent sigma.p route closes with both child handles", closes_sigma(sigma_full))

    for missing in both_child_handles | {"OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"}:
        reduced = set(sigma_full)
        reduced.remove(missing)
        audit.check(f"parent sigma.p route fails without {missing}", not closes_sigma(reduced))

    audit.check("sigma.p consequence alone does not close scalar-lift exclusion", not closes_scalar(sigma_handle))
    audit.check("sigma.p consequence alone does not close KS child route", not closes_ks(sigma_handle))
    audit.check("sigma.p consequence alone does not close physical matter-state bridge", not closes_bridge(sigma_handle))
    audit.check("sigma.p consequence alone does not close hydrogen", not closes_hydrogen(sigma_handle))
    audit.check("full scalar-lift contract closes scalar-lift exclusion", closes_scalar(set(SCALAR_INPUTS)))
    audit.check("full KS child route closes KS route", closes_ks(set(KS_ROUTE_INPUTS)))
    audit.check("full bridge route closes physical matter-state bridge", closes_bridge(set(BRIDGE_INPUTS)))

    section("Finite support checks")
    finite_support_checks(audit)

    section("Authority boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    for label, container in [("goal packet", goal), ("Koide firewall", firewall)]:
        audit.check(
            f"{label} references grouped sigma.p two-handle packet",
            NOTE.name in container and "KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED" in container,
        )

    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    audit.check("primitive registry contains minimal axioms", "minimal_axioms" in primitive_nodes)
    audit.check("primitive registry contains scale reference", "scale_reference_primitive" in primitive_nodes)
    audit.check("primitive registry contains kinetic isotropy", "kinetic_isotropy_primitive" in primitive_nodes)
    audit.check("primitive registry contains realized-state primitive", "realized_state_primitive" in primitive_nodes)
    absent_primitives = [
        "ks_route_momentum_link_phase_primitive",
        "ks_route_spinful_kernel_object_primitive",
        "spinful_sigma_dot_p_kernel_primitive",
        "scalar_lift_exclusion_primitive",
        "ks_to_physical_matter_state_spinor_law_primitive",
        "physical_matter_state_law_primitive",
        "hydrogen_primitive",
    ]
    for primitive in absent_primitives:
        audit.check(f"registry has no shortcut primitive: {primitive}", primitive not in primitive_nodes)

    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    for forbidden in [
        "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED",
        "KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED",
        "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "hydrogen_primitive",
    ]:
        audit.check(f"approved primitive notes do not supply {forbidden}", forbidden not in primitive_text)

    section("Non-claim checks")
    for phrase in [
        "No derivation or ratification of\n  `KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED`.",
        "No derivation or ratification of\n  `KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED`.",
        "No derivation or ratification of\n  `SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`.",
        "No R-eta, h-class, h-unit, K1/K2/K3/K4, Koide electron readout, `m_e`,",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]:
        audit.check(f"explicit non-claim present: {flat(phrase)}", flat(phrase) in note_flat)

    audit.summary()


if __name__ == "__main__":
    main()
