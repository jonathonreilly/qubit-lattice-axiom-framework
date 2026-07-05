#!/usr/bin/env python3
"""Verifier for the hydrogen-facing Koide W4c PR #5028 impact note."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_W4C_PR5028_IMPACT_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
SPECIES_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SPECIES_REALIZED = ROOT / "docs" / "ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md"
LABELING_BRIDGE = ROOT / "docs" / "STAGGERED_DIRAC_GATE_AC_PHI_LAMBDA_LABELING_CONVENTION_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
LABELING_NO_GO = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md"
PR5019 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5022 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


PR5028_CONTEXT_INPUTS = {
    "PR5028_MERGED_AFTER_LANE_RELEVANT_OPEN_REFRESH",
    "LABELING_SUCCESSOR_REPOINTS",
    "LABELING_BRIDGE_DEPENDENCY_REPAIR",
    "SPECIES_REALIZED_STATE_CONTEXT_DEMOTIONS",
    "NO_CLAIM_CHANGE",
    "NO_RETAINED_STATUS_CHANGE",
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


def closes_pr5028_context(inputs: set[str]) -> bool:
    return PR5028_CONTEXT_INPUTS <= inputs


def closes_k3(inputs: set[str]) -> bool:
    return K3_INPUTS <= inputs


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
        SPECIES_NO_GO,
        SPECIES_REALIZED,
        LABELING_BRIDGE,
        LABELING_NO_GO,
        PR5019,
        PR5022,
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
        "Koide W4c PR #5028 Impact Discriminator",
        "merged-PR impact discriminator / Koide labeling-species dependency",
        "does not promote PR `#5028` beyond its",
        "does not derive a physical electron species bridge",
        "does not derive R-eta",
        "merged on 2026-07-05 at 17:19:24 UTC",
        "STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md",
        "STAGGERED_DIRAC_GATE_AC_PHI_LAMBDA_LABELING_CONVENTION_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md",
        "ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md",
        "occupancy_selection -> labeling_no_go -> labeling_bridge -> gate note",
        "species -> w2_registrability bridge -> r_eta_narrowing",
        "`#5028` W4c labeling/species repairs | merged after open lane-relevant refresh",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad Koide/hydrogen closure claim fails; narrowed #5028",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    pr5028_inputs = set(PR5028_CONTEXT_INPUTS)
    audit.check("full #5028 context predicate accepts impact context", closes_pr5028_context(pr5028_inputs))
    audit.check("#5028 context alone does not close K3", not closes_k3(pr5028_inputs))
    audit.check("#5028 context alone does not close K2", not closes_k2(pr5028_inputs))
    audit.check("#5028 context alone does not close electron mass", not closes_electron_mass(pr5028_inputs))
    audit.check("#5028 context alone does not close hydrogen", not closes_hydrogen(pr5028_inputs))
    audit.check("K3 predicate closes only with K3 inputs", closes_k3(set(K3_INPUTS)))
    audit.check("K2 predicate closes only with K2 inputs", closes_k2(set(K2_INPUTS)))
    audit.check("electron mass predicate closes only with mass inputs", closes_electron_mass(set(ELECTRON_MASS_INPUTS)))
    audit.check("hydrogen predicate closes only with hydrogen inputs", closes_hydrogen(set(HYDROGEN_INPUTS)))

    section("Wiring and authority boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    species = read(SPECIES_NO_GO)
    species_realized = flat(read(SPECIES_REALIZED)).lower()
    labeling_bridge = read(LABELING_BRIDGE)
    labeling_no_go = read(LABELING_NO_GO)
    pr5019 = read(PR5019)
    pr5022 = read(PR5022)
    registry_text = read(REGISTRY)
    registry = json.loads(registry_text)
    tier_a = read(TIER_A)
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("species current-surface no-go", species),
    ]:
        audit.check(f"{label} references #5028 impact note", NOTE.name in container and "#5028" in container)

    audit.check("species realized note is support-only", "does **not** derive" in species_realized)
    audit.check("labeling bridge remains bounded context", "retained_bounded" in labeling_bridge or "bounded" in labeling_bridge.lower())
    audit.check("labeling no-go remains a no-go surface", "NO-GO" in labeling_no_go or "no-go" in labeling_no_go.lower())
    audit.check("#5019 impact keeps premise hygiene separate", "premise hygiene" in pr5019 and "no electron-mass or hydrogen closure" in pr5019)
    audit.check("#5022 impact keeps K2 exactness open", "K2 conditionality progress" in pr5022 and "no retained R-eta derivation" in pr5022)
    audit.check("Tier-A registry still names AC_phi_lambda", "AC_phi_lambda" in tier_a)
    audit.check("AC_phi_lambda is not a primitive registry node", "AC_phi_lambda" not in registry["nodes"])
    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive node present: {node_name}", node_name in registry["nodes"])
    for absent in [
        "ac_phi_lambda_primitive",
        "labeling_convention_primitive",
        "physical_electron_species_bridge_primitive",
        "r_eta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered shortcut primitive: {absent}", absent not in registry_text)
    for excluded in ["selector", "readout bridge", "empirical fit", "mass ratio"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_nonclaims = [
        "No theorem-promotion claim beyond the merged dependency-surface scope of PR",
        "No retained-theorem verdict or status change.",
        "No derivation of `AC_phi_lambda`.",
        "No derivation or ratification of a labeling convention theorem.",
        "No derivation or ratification of `PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.",
        "No derivation of `S_l`, A3, `C_A3`, `alpha(0)`, static-source Rydberg, or",
        "No spending of PR `#5028` as K3 species-bridge closure.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note adopts PR `#5028`",
        "PR #5028 closes Koide",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED is supplied",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "electron mass is retained",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
