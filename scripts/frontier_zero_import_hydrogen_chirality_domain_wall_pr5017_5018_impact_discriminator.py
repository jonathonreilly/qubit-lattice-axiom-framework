#!/usr/bin/env python3
"""Verifier for the hydrogen-facing chirality/domain-wall PR impact note."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_CHIRALITY_DOMAIN_WALL_PR5017_5018_IMPACT_DISCRIMINATOR_2026-07-05.md"
MATTER_STATE_CHIRALITY_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_MATTER_STATE_CHIRALITY_DOMAIN_WALL_IMPACT_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
SPECIES_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SPECIES_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
SOURCE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
D17_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_D17_BLOCK_NORMALIZATION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PR5019 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


CHIRALITY_CONTEXT_INPUTS = {
    "PR5012_OPEN",
    "PR5014_OPEN",
    "PR5017_OPEN",
    "PR5018_OPEN",
    "FREE_FIELD_DOMAIN_WALL_CONTEXT",
    "RECORD_FORMATION_FRONT_CONTEXT",
    "ANOMALY_INFLOW_CONTEXT",
    "SM_CHIRAL_MAP_CONTEXT",
    "NAMED_GAPS_PRESERVED",
}

K3_INPUTS = {
    "K3_SPECIES_BRIDGE_TEXT_LOCK",
    "C3_GRADE_SCOPE_LOCK",
    "MINIMUM_DECOMPOSITION_RETAINED",
    "RATIFICATION_CLASS_BOUNDARY_RETAINED",
    "PR4929_OWNER_ADOPTION",
    "NO_ABOVE_C3_CONTENT_INPUT",
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


def closes_chirality_context(inputs: set[str]) -> bool:
    return CHIRALITY_CONTEXT_INPUTS <= inputs


def closes_k3(inputs: set[str]) -> bool:
    return K3_INPUTS <= inputs


def closes_electron_mass(inputs: set[str]) -> bool:
    return ELECTRON_MASS_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        MATTER_STATE_CHIRALITY_IMPACT,
        GOAL,
        SPECIES_NO_GO,
        SPECIES_DECISION,
        PHYSICAL_ELECTRON,
        KOIDE_FIREWALL,
        SOURCE_DECISION,
        D17_DECISION,
        K4_PACKET,
        PR5019,
        PRIMITIVE_REGISTRY,
        TIER_A_REGISTRY,
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
        "Chirality Domain-Wall PR #5017/#5018 Impact Discriminator",
        "open-PR impact discriminator / K3 species-bridge boundary",
        "does not adopt PR `#5017` or PR `#5018`",
        "does not ratify the physical electron species bridge",
        "does not derive `m_e`",
        "`#5017` domain-wall edge anomaly inflow via spectral flow",
        "`#5018` domain-wall edge content vs SM chiral fermions map",
        "background-U(1) free-field Callan-Harvey consistency",
        "exact `6+2` chiral-cube map",
        "not full SM `15`-plet",
        "spin-edge/taste-cube bridge",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "above-C3 chirality/domain-wall content",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | merged",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_MATTER_STATE_CHIRALITY_DOMAIN_WALL_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad chirality-to-hydrogen closure claim fails; narrowed",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    chirality_inputs = set(CHIRALITY_CONTEXT_INPUTS)
    audit.check("full chirality-stack context predicate accepts impact context", closes_chirality_context(chirality_inputs))
    audit.check("chirality context alone does not close K3", not closes_k3(chirality_inputs))
    audit.check("chirality context alone does not close electron mass", not closes_electron_mass(chirality_inputs))
    audit.check("chirality context alone does not close hydrogen", not closes_hydrogen(chirality_inputs))
    audit.check("full K3 contract accepts K3 only", closes_k3(set(K3_INPUTS)))
    audit.check("full electron-mass predicate closes electron mass", closes_electron_mass(set(ELECTRON_MASS_INPUTS)))
    audit.check("full hydrogen predicate model closes hydrogen", closes_hydrogen(set(HYDROGEN_INPUTS)))
    for missing in sorted(ELECTRON_MASS_INPUTS):
        reduced = set(ELECTRON_MASS_INPUTS)
        reduced.remove(missing)
        audit.check(f"electron mass fails without {missing}", not closes_electron_mass(reduced))

    section("Authority boundary checks")
    goal = read(GOAL)
    species_no_go = read(SPECIES_NO_GO)
    species_decision = read(SPECIES_DECISION)
    physical_electron = read(PHYSICAL_ELECTRON)
    koide_firewall = read(KOIDE_FIREWALL)
    source_decision = read(SOURCE_DECISION)
    d17_decision = read(D17_DECISION)
    k4_packet = read(K4_PACKET)
    pr5019 = read(PR5019)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    tier_a_text = read(TIER_A_REGISTRY)

    for label, container in [
        ("goal packet", goal),
        ("species no-go", species_no_go),
        ("species decision", species_decision),
        ("physical electron packet", physical_electron),
    ]:
        audit.check(f"{label} references chirality impact note", NOTE.name in container and "#5018" in container and "#5017" in container)

    audit.check("Koide firewall keeps K1-K4 separation", all(token in koide_firewall for token in ["K1", "K2", "K3", "K4"]))
    audit.check("source decision remains source-side", "S_l = 1/256" in source_decision and "does not derive `m_e`" in source_decision)
    audit.check(
        "D17 decision remains weak-front only",
        "CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED" in d17_decision
        and "does not derive\n`m_e`" in d17_decision,
    )
    audit.check("K4 packet remains scale-side", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in k4_packet and "does not ratify" in k4_packet)
    audit.check("#5019 impact stays Koide premise hygiene", "premise hygiene and audit-readiness context" in pr5019 and "does not derive `AC_phi_lambda`" in pr5019)
    audit.check("Tier-A registry still names AC_phi_lambda", "AC_phi_lambda" in tier_a_text)

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive node present: {node_name}", node_name in primitive_nodes)
    for absent in [
        "physical_electron_species_bridge_primitive",
        "chirality_to_species_primitive",
        "hypercharge_normalization_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered shortcut primitive: {absent}", absent not in primitive_nodes)
    for excluded in ["mass ratio", "selector", "readout bridge", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_non_claims = [
        "No adoption or landing claim for PR `#5017` or PR `#5018`.",
        "No audit verdict or status change.",
        "No derivation or ratification of `PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED`.",
        "No derivation of full Standard Model chiral matter content.",
        "No derivation of anomaly-complete `U(1)_Y`, electric charge, or hypercharge",
        "No derivation of spin-edge/taste-cube bridge closure.",
        "No derivation of K1 occupancy/counting, K2 R-eta/phase readout, or native",
        "No derivation of F/L/P/R source-side interface, D17 weak-front normalization",
        "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.",
        "No derivation of `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note adopts PR `#5017`",
        "This note adopts PR `#5018`",
        "PR #5018 derives hydrogen",
        "PR #5017 derives `m_e`",
        "physical electron species bridge is retained",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED is supplied",
        "m_e is derived",
        "alpha(0) is derived",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
