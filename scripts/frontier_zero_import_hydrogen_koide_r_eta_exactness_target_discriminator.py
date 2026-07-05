#!/usr/bin/env python3
"""Verifier for the hydrogen-facing Koide R-eta exactness target."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PR5020_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
BRANNEN_OPEN_GATE = ROOT / "docs" / "LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


K2_EXACTNESS_INPUTS = {
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

PR5020_CONTEXT = {
    "PR5020_OPEN",
    "REGISTERED_ANGLE_FUNCTIONAL_CONTEXT",
    "REALIZED_STATE_COUNTERFACTUAL_CLASSIFICATION",
    "LAW_FREENESS_CONTEXT",
    "UNIT_FACE_DISSOLUTION_CONTEXT",
    "EXACTNESS_RESIDUAL_NAMED",
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


def closes_k2_exactness(inputs: set[str]) -> bool:
    return K2_EXACTNESS_INPUTS <= inputs


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
        PR5020_IMPACT,
        PHYSICAL_ELECTRON,
        BRANNEN_OPEN_GATE,
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
        "Koide R-Eta Exactness Target Discriminator",
        "target discriminator / Koide K2 exactness handoff",
        "does not ratify Koide K2 exactness",
        "K2_R_ETA_EXACTNESS_RETAINED",
        "K2_EXACTNESS_TEXT_LOCK",
        "REGISTERED_PHI_VALUE_FACE_ACCEPTED",
        "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
        "RADIAN_READOUT_LICENSE_RETAINED",
        "FOLD_AND_BRANCH_DOMAIN_LOCK",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "No proper subset of those ten inputs",
        "`#5020` value-face PR",
        "Phi = (1/3) arccos(cos 3delta)",
        "value-face registration <-> exactness theorem",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad K2-closure claim fails; narrowed exactness target",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    full_inputs = set(K2_EXACTNESS_INPUTS)
    audit.check("full K2 exactness contract accepts target", closes_k2_exactness(full_inputs))
    for missing in sorted(K2_EXACTNESS_INPUTS):
        reduced = set(K2_EXACTNESS_INPUTS)
        reduced.remove(missing)
        audit.check(f"K2 exactness fails without {missing}", not closes_k2_exactness(reduced))
    accepted_subsets = [subset for subset in all_subsets(K2_EXACTNESS_INPUTS) if closes_k2_exactness(subset)]
    audit.check("only full tested K2 contract subset closes exactness", accepted_subsets == [full_inputs])
    audit.check("#5020 context alone does not close K2 exactness", not closes_k2_exactness(set(PR5020_CONTEXT)))
    audit.check("K2 exactness alone does not close electron mass", not closes_electron_mass({"K2_R_ETA_EXACTNESS_RETAINED"}))
    audit.check("K2 exactness alone does not close hydrogen", not closes_hydrogen({"K2_R_ETA_EXACTNESS_RETAINED"}))

    section("Authority boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    pr5020_impact = read(PR5020_IMPACT)
    physical_electron = read(PHYSICAL_ELECTRON)
    brannen_open_gate = read(BRANNEN_OPEN_GATE)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    realized_text = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
    ]:
        audit.check(f"{label} references K2 exactness target", NOTE.name in container and "K2_R_ETA_EXACTNESS_RETAINED" in container)
    audit.check("physical electron packet remains downstream", "K2 value-face progress only" in physical_electron and "no delta exactness theorem" in physical_electron)
    audit.check("#5020 impact names exactness residual", "exactness remains open" in pr5020_impact and "No derivation or ratification of a Koide R-eta exactness theorem." in pr5020_impact)
    audit.check("Brannen open gate keeps delta open", "not derive `delta = 2/9`" in brannen_open_gate)
    audit.check("realized-state primitive supplies no value", "no state" in realized_text and "or value is supplied" in flat(realized_text))
    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive node present: {node_name}", node_name in primitive_nodes)
    for absent in [
        "k2_r_eta_exactness_primitive",
        "delta_exactness_primitive",
        "r_eta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered shortcut primitive: {absent}", absent not in primitive_nodes)
    for excluded in ["mass ratio", "selector", "readout bridge", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_non_claims = [
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No derivation of `AC_phi_lambda`.",
        "No derivation of `delta = 2/9`.",
        "No adoption or landing claim for PR `#5020`.",
        "No derivation or ratification of K1 occupancy/counting, K3 physical species",
        "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.",
        "No derivation of `S_l`, A3, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note ratifies Koide K2 exactness",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "delta = 2/9 is derived",
        "physical electron mass is retained",
        "This note claims hydrogen is retained",
        "hydrogen retained theorem",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
