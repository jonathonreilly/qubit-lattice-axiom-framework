#!/usr/bin/env python3
"""Verifier for the hydrogen-facing PR #5011 eta-twisted walk impact note."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ETA_TWISTED_WALK_PR5011_IMPACT_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
ETA_NOTE = ROOT / "docs" / "ETA_TWISTED_WALK_FAMILY_RIGID_DRIFT_DISCOVERY_BOUNDED_THEOREM_NOTE_2026-06-10.md"
ETA_RUNNER = ROOT / "scripts" / "eta_twisted_walk_family_discovery_2026_06_10.py"
ETA_CACHE = ROOT / "logs" / "runner-cache" / "eta_twisted_walk_family_discovery_2026_06_10.txt"
KS_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
KINETIC_CLASS = ROOT / "docs" / "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
LINK_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_TARGET_DISCRIMINATOR_2026-07-05.md"
LINK_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
LINK_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SIGMA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md"
SIGMA_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KS_STATE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_BRIDGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
K2 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
ELECTRON_MASS = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


PR5011_CONTEXT_INPUTS = {
    "PR5011_OPEN_PR_CONTEXT",
    "ETA_TWISTED_WALK_RUNNER_REPAIR_PROPOSED",
    "ETA_TWISTED_COVARIANT_TRANSPORT_CONTEXT_NAMED",
    "FULL_FAMILY_CLASSIFICATION_OPEN_BOUNDARY_PRESERVED",
    "NO_RETAINED_STATUS_SPEND",
}

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

KS_STATE_INPUTS = {
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

PHYSICAL_BRIDGE_INPUTS = {
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


def closes_pr5011_context(inputs: set[str]) -> bool:
    return PR5011_CONTEXT_INPUTS <= inputs


def closes_link_input(inputs: set[str]) -> bool:
    return LINK_INPUTS <= inputs


def closes_sigma_route(inputs: set[str]) -> bool:
    return SIGMA_ROUTE_INPUTS <= inputs


def closes_ks_state(inputs: set[str]) -> bool:
    return KS_STATE_INPUTS <= inputs


def closes_physical_bridge(inputs: set[str]) -> bool:
    return PHYSICAL_BRIDGE_INPUTS <= inputs


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
        ETA_NOTE,
        ETA_RUNNER,
        ETA_CACHE,
        KS_FORCING,
        KINETIC_CLASS,
        LINK_TARGET,
        LINK_DECISION,
        LINK_CURRENT,
        SIGMA_TARGET,
        SIGMA_CURRENT,
        KS_STATE_TARGET,
        PHYSICAL_BRIDGE,
        K2,
        ELECTRON_MASS,
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
        "Koide Eta-Twisted Walk PR #5011 Impact Discriminator",
        "open-PR impact discriminator / eta-twisted walk context boundary",
        "does not adopt PR `#5011`",
        "a46f45205ec5d67d6b9675ecaa85aea9e9f7f881",
        "PR5011_ETA_TWISTED_COVARIANT_WALK_CONTEXT",
        "not the KS-route momentum/link-phase handoff",
        "not the spinful `sigma.p` kernel-object theorem",
        "not a physical matter-state law",
        "ETA_TWISTED_WALK_FAMILY_RIGID_DRIFT_DISCOVERY_BOUNDED_THEOREM_NOTE_2026-06-10.md",
        "scripts/eta_twisted_walk_family_discovery_2026_06_10.py",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad KS-route/R-eta/hydrogen closure claim fails; narrowed",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    pr5011_inputs = set(PR5011_CONTEXT_INPUTS)
    audit.check("#5011 context predicate accepts all support inputs", closes_pr5011_context(pr5011_inputs))
    audit.check("#5011 context alone does not close route link input", not closes_link_input(pr5011_inputs))
    audit.check("#5011 context alone does not close sigma.p route", not closes_sigma_route(pr5011_inputs))
    audit.check("#5011 context alone does not close KS state law", not closes_ks_state(pr5011_inputs))
    audit.check("#5011 context alone does not close physical matter bridge", not closes_physical_bridge(pr5011_inputs))
    audit.check("#5011 context alone does not close K2", not closes_k2(pr5011_inputs))
    audit.check("#5011 context alone does not close electron mass", not closes_electron_mass(pr5011_inputs))
    audit.check("#5011 context alone does not close hydrogen", not closes_hydrogen(pr5011_inputs))
    audit.check("route link predicate closes only with full inputs", closes_link_input(set(LINK_INPUTS)))
    audit.check("sigma.p predicate closes only with full inputs", closes_sigma_route(set(SIGMA_ROUTE_INPUTS)))
    audit.check("KS state predicate closes only with full inputs", closes_ks_state(set(KS_STATE_INPUTS)))
    audit.check("physical bridge predicate closes only with full inputs", closes_physical_bridge(set(PHYSICAL_BRIDGE_INPUTS)))

    section("Wiring and authority boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    eta_note = read(ETA_NOTE)
    eta_runner = read(ETA_RUNNER)
    eta_cache = read(ETA_CACHE)
    ks_forcing = read(KS_FORCING)
    kinetic_class = read(KINETIC_CLASS)
    link_target = read(LINK_TARGET)
    link_decision = read(LINK_DECISION)
    link_current = read(LINK_CURRENT)
    sigma_target = read(SIGMA_TARGET)
    sigma_current = read(SIGMA_CURRENT)
    registry_text = read(REGISTRY)
    registry = json.loads(registry_text)
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("link target", link_target),
        ("link decision", link_decision),
        ("link current no-go", link_current),
        ("sigma target", sigma_target),
        ("sigma current no-go", sigma_current),
    ]:
        audit.check(f"{label} references #5011 impact note", NOTE.name in container and "#5011" in container)

    eta_surface = "\n".join([eta_note, eta_runner, eta_cache])
    for phrase in [
        "eta-twisted",
        "symmetric-point drift",
        "off-axis FRONT SPEEDS",
        "SCORECARD: PASS=13 FAIL=0",
        "FULL-FAMILY STATUS",
    ]:
        audit.check(f"eta walk surface contains: {phrase}", phrase in eta_surface)
    audit.check("eta walk surface preserves open classification", "remains named" in eta_surface or "remains a NAMED OPEN" in eta_surface)
    audit.check("Kawamoto-Smit forcing supplies eta phase support", "eta" in ks_forcing and "Kawamoto" in ks_forcing)
    audit.check("kinetic class note preserves K0/K1 residual context", "K0" in kinetic_class and "K1" in kinetic_class)

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive node present: {node_name}", node_name in registry["nodes"])
    for absent in [
        "eta_twisted_walk_primitive",
        "ks_route_momentum_link_phase_primitive",
        "spinful_sigma_dot_p_kernel_primitive",
        "physical_matter_state_law_primitive",
        "r_eta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered shortcut primitive: {absent}", absent not in registry_text)
    for excluded in ["selector", "readout bridge", "mass ratio", "probability rule"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_nonclaims = [
        "No adoption, landing, or audit verdict claim for PR `#5011`.",
        "No retained-theorem verdict or status change.",
        "No derivation or ratification of `PR5011_ETA_TWISTED_COVARIANT_WALK_CONTEXT`.",
        "No derivation or ratification of",
        "`KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED`.",
        "`SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`.",
        "`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "No derivation or ratification of h-class, h-unit, R-eta, two-ninths/radian,",
        "No derivation or ratification of K1 occupancy/counting, K3 physical species",
        "No derivation of `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    audit.summary()


if __name__ == "__main__":
    main()
