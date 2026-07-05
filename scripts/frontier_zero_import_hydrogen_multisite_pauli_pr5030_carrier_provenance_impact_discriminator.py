#!/usr/bin/env python3
"""Verifier for the hydrogen-facing PR #5030 carrier-provenance impact note."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_MULTISITE_PAULI_PR5030_CARRIER_PROVENANCE_IMPACT_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PHYSICAL_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PHYSICAL_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
H_CLASS = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
K2 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
ELECTRON_MASS = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
MULTISITE = ROOT / "docs" / "MULTISITE_PAULI_GROUP_THEOREM_NOTE_2026-05-02.md"
CL3_SITE = ROOT / "docs" / "CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


PR5030_CONTEXT_INPUTS = {
    "PR5030_OPEN_PR_CONTEXT",
    "FINITE_MULTISITE_PAULI_CARRIER_PROVENANCE_PROPOSED",
    "RETAINED_CL3_PER_SITE_CARRIER_PROVIDER_NAMED",
    "PHYSICAL_FOCK_CARVEOUT_PRESERVED",
    "NO_RETAINED_STATUS_SPEND",
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

H_CLASS_INPUTS = {
    "R_ETA_H_CLASS_TEXT_LOCK",
    "FIXED_LOCUS_WEIGHT_DENSITY_ACCEPTED",
    "FINITE_KS_LOCAL_DENSITY_OPERATOR_FACE_ACCEPTED",
    "SUPPLIED_CONTEXT_REGISTRABILITY_ACCEPTED",
    "AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_ACCEPTED",
    "PHYSICAL_CARRIER_CONTEXT_RETAINED",
    "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED",
    "NO_H_UNIT_OR_RADIAN_INPUT",
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


def closes_pr5030_context(inputs: set[str]) -> bool:
    return PR5030_CONTEXT_INPUTS <= inputs


def closes_physical_carrier(inputs: set[str]) -> bool:
    return PHYSICAL_CARRIER_INPUTS <= inputs


def closes_h_class(inputs: set[str]) -> bool:
    return H_CLASS_INPUTS <= inputs


def closes_r_eta(inputs: set[str]) -> bool:
    return R_ETA_INPUTS <= inputs


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
        PHYSICAL_TARGET,
        PHYSICAL_DECISION,
        PHYSICAL_CURRENT,
        H_CLASS,
        R_ETA,
        K2,
        ELECTRON_MASS,
        MULTISITE,
        CL3_SITE,
        REGISTRY,
        TIER_A,
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
        "Multisite Pauli PR #5030 Carrier-Provenance Impact Discriminator",
        "open-PR impact discriminator / finite carrier-provenance boundary",
        "does not adopt PR `#5030`",
        "does not ratify `PHYSICAL_CARRIER_CONTEXT_RETAINED`",
        "PR5030_FINITE_MULTISITE_PAULI_CARRIER_PROVENANCE_CONTEXT",
        "finite multisite Pauli algebra can cite a retained Cl(3) per-site tensor",
        "not the physical charged-lepton carrier-context theorem",
        "MULTISITE_PAULI_GROUP_THEOREM_NOTE_2026-05-02.md",
        "CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad carrier/hydrogen closure claim fails; narrowed #5030",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    pr5030_inputs = set(PR5030_CONTEXT_INPUTS)
    audit.check("#5030 context predicate accepts all support inputs", closes_pr5030_context(pr5030_inputs))
    audit.check("#5030 context alone does not close physical carrier", not closes_physical_carrier(pr5030_inputs))
    audit.check("#5030 context alone does not close h-class", not closes_h_class(pr5030_inputs))
    audit.check("#5030 context alone does not close R-eta", not closes_r_eta(pr5030_inputs))
    audit.check("#5030 context alone does not close K2", not closes_k2(pr5030_inputs))
    audit.check("#5030 context alone does not close electron mass", not closes_electron_mass(pr5030_inputs))
    audit.check("#5030 context alone does not close hydrogen", not closes_hydrogen(pr5030_inputs))
    audit.check("physical carrier predicate closes only with its full inputs", closes_physical_carrier(set(PHYSICAL_CARRIER_INPUTS)))
    audit.check("h-class predicate closes only with its full inputs", closes_h_class(set(H_CLASS_INPUTS)))
    audit.check("R-eta predicate closes only with its full inputs", closes_r_eta(set(R_ETA_INPUTS)))
    audit.check("K2 predicate closes only with its full inputs", closes_k2(set(K2_INPUTS)))
    audit.check("electron mass predicate closes only with its full inputs", closes_electron_mass(set(ELECTRON_MASS_INPUTS)))
    audit.check("hydrogen predicate closes only with its full inputs", closes_hydrogen(set(HYDROGEN_INPUTS)))

    section("Wiring and authority boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    physical_target = read(PHYSICAL_TARGET)
    physical_decision = read(PHYSICAL_DECISION)
    physical_current = read(PHYSICAL_CURRENT)
    multisite = read(MULTISITE)
    cl3_site = read(CL3_SITE)
    registry_text = read(REGISTRY)
    registry = json.loads(registry_text)
    tier_a = read(TIER_A)
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("physical carrier target", physical_target),
        ("physical carrier decision", physical_decision),
        ("physical carrier current no-go", physical_current),
    ]:
        audit.check(f"{label} references #5030 impact note", NOTE.name in container and "#5030" in container)

    audit.check("multisite note is finite Pauli algebra", "Multi-Site Pauli Group" in multisite and "4^{N+1}" in multisite)
    audit.check("multisite note preserves physical carrier boundary", "physical" in multisite.lower() and "carrier" in multisite.lower())
    audit.check("Cl3 site note supplies finite block tensor dimension", "D3" in cl3_site and "2^" in cl3_site)
    audit.check("Cl3 site note does not supply physical readout", "mass" not in cl3_site.lower() and "hydrogen" not in cl3_site.lower())
    audit.check("Tier-A registry still separate from primitives", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in registry_text)
    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive node present: {node_name}", node_name in registry["nodes"])
    for absent in [
        "multisite_pauli_carrier_primitive",
        "physical_carrier_context_primitive",
        "r_eta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered shortcut primitive: {absent}", absent not in registry_text)
    for excluded in ["selector", "readout bridge", "normalization", "mass ratio"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_nonclaims = [
        "No adoption, landing, or audit verdict claim for PR `#5030`.",
        "No retained-theorem verdict or status change.",
        "No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.",
        "No derivation or ratification of `CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`.",
        "No derivation or ratification of `SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`.",
        "No derivation or ratification of h-class, h-unit, R-eta, two-ninths/radian,",
        "No derivation or ratification of K1 occupancy/counting, K3 physical species",
        "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.",
        "No derivation of `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    audit.summary()


if __name__ == "__main__":
    main()
