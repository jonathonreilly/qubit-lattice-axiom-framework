#!/usr/bin/env python3
"""Verifier for the hydrogen-facing Koide R-eta value-face PR #5020 impact note."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PR5019 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


PR5020_CONTEXT_INPUTS = {
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


def closes_pr5020_context(inputs: set[str]) -> bool:
    return PR5020_CONTEXT_INPUTS <= inputs


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
        PHYSICAL_ELECTRON,
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
        "Koide R-Eta Value-Face PR #5020 Impact Discriminator",
        "PR impact discriminator / Koide K2 value-face boundary",
        "does not use merged PR `#5020` as exactness closure",
        "does not derive `AC_phi_lambda`",
        "does not derive `delta = 2/9`",
        "registered-angle functional",
        "Phi = (1/3) arccos(cos 3delta)",
        "counterfactual test",
        "law-freeness",
        "unit-face dissolution",
        "exactness residual",
        "K2 R-eta value face",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | merged",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | merged",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad K2/hydrogen closure claim fails; narrowed #5020",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    pr5020_inputs = set(PR5020_CONTEXT_INPUTS)
    audit.check("full #5020 context predicate accepts impact context", closes_pr5020_context(pr5020_inputs))
    audit.check("#5020 context alone does not close electron mass", not closes_electron_mass(pr5020_inputs))
    audit.check("#5020 context alone does not close hydrogen", not closes_hydrogen(pr5020_inputs))
    audit.check("electron mass predicate closes only with mass inputs", closes_electron_mass(set(ELECTRON_MASS_INPUTS)))
    audit.check("hydrogen predicate closes only with hydrogen inputs", closes_hydrogen(set(HYDROGEN_INPUTS)))
    for missing in sorted(ELECTRON_MASS_INPUTS):
        reduced = set(ELECTRON_MASS_INPUTS)
        reduced.remove(missing)
        audit.check(f"electron mass fails without {missing}", not closes_electron_mass(reduced))

    section("Authority boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    physical_electron = read(PHYSICAL_ELECTRON)
    pr5019 = read(PR5019)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    tier_a_text = read(TIER_A_REGISTRY)
    realized_text = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
        ("physical electron packet", physical_electron),
    ]:
        audit.check(f"{label} references #5020 impact note", NOTE.name in container and "#5020" in container)
    audit.check("#5019 remains companion premise hygiene", "premise hygiene and audit-readiness context" in pr5019)
    audit.check("Koide firewall still keeps K1-K4 separate", all(token in koide_firewall for token in ["K1", "K2", "K3", "K4"]))
    audit.check("realized-state primitive supplies no values", "no state" in realized_text and "or value is supplied" in flat(realized_text))
    audit.check("Tier-A registry still names AC_phi_lambda", "AC_phi_lambda" in tier_a_text)
    audit.check("AC_phi_lambda is not a primitive node", "AC_phi_lambda" not in primitive_nodes)
    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive node present: {node_name}", node_name in primitive_nodes)
    for absent in [
        "r_eta_exactness_primitive",
        "delta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered shortcut primitive: {absent}", absent not in primitive_nodes)
    for excluded in ["mass ratio", "selector", "readout bridge", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_non_claims = [
        "No claim that merged PR `#5020` supplies K2 exactness, electron mass, alpha,",
        "No audit verdict or status change.",
        "No derivation of `AC_phi_lambda`.",
        "No derivation of `delta = 2/9`.",
        "No derivation or ratification of a Koide R-eta exactness theorem.",
        "No derivation or ratification of K1 occupancy/counting, K3 physical species",
        "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.",
        "No derivation of `S_l`, A3, `C_A3`, `alpha(0)`, static-source Rydberg, or",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "PR #5020 derives hydrogen",
        "PR #5020 derives `m_e`",
        "delta = 2/9 is derived",
        "AC_phi_lambda retained theorem",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
