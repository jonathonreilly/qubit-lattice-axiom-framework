#!/usr/bin/env python3
"""Verifier for the Koide R-eta exactness current-surface no-go."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
EXACTNESS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
PR5020_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5022_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
TWO_NINTHS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
TWO_NINTHS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
TWO_NINTHS_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PR5019_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
BRANNEN_OPEN_GATE = ROOT / "docs" / "LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md"
TIER_A_BOUNDED = ROOT / "docs" / "CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
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

CURRENT_SURFACE_INPUTS = {
    "K2_EXACTNESS_TEXT_LOCK",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
}

ELECTRON_MASS_INPUTS = {
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
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


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        KOIDE_FIREWALL,
        EXACTNESS_TARGET,
        PR5020_IMPACT,
        PR5022_IMPACT,
        R_ETA_TARGET,
        TWO_NINTHS_TARGET,
        TWO_NINTHS_DECISION,
        TWO_NINTHS_NO_GO,
        PR5019_IMPACT,
        PHYSICAL_ELECTRON,
        BRANNEN_OPEN_GATE,
        TIER_A_BOUNDED,
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
        "Koide R-Eta Exactness Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not ratify Koide K2 exactness",
        "K2_R_ETA_EXACTNESS_RETAINED",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "nine-input owner/audit decision packet",
        "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, merged-PR, and open-PR surfaces do not supply",
        "K2_EXACTNESS_TEXT_LOCK",
        "REGISTERED_PHI_VALUE_FACE_ACCEPTED",
        "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
        "RADIAN_READOUT_LICENSE_RETAINED",
        "FOLD_AND_BRANCH_DOMAIN_LOCK",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "`#5021` primitive-retirement review draft",
        "no primitive retirement and no registry edit",
        "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED",
        "`#5022` audit repair: delta-eta chain R-eta supplied premise | merged",
        "declared supplied readout-identification premise",
        "conditional repair only; no retained R-eta derivation or K2 exactness",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | open",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | open",
        "No-Go Discipline Gate",
        "broad K2-exactness no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("K2 exactness predicate checks")
    full_inputs = set(K2_EXACTNESS_INPUTS)
    audit.check("full K2 exactness contract accepts retained handoff", closes_k2_exactness(full_inputs))
    for missing in sorted(K2_EXACTNESS_INPUTS):
        reduced = set(K2_EXACTNESS_INPUTS)
        reduced.remove(missing)
        audit.check(f"K2 exactness handoff fails without {missing}", not closes_k2_exactness(reduced))
    accepted_subsets = [subset for subset in all_subsets(K2_EXACTNESS_INPUTS) if closes_k2_exactness(subset)]
    audit.check("only full K2 exactness subset closes handoff", accepted_subsets == [full_inputs])
    audit.check(
        "current surface without value/exactness/readout/domain/owner/audit inputs does not close K2 exactness",
        not closes_k2_exactness(set(CURRENT_SURFACE_INPUTS)),
    )
    audit.check(
        "K2 exactness alone does not close physical electron mass",
        not closes_electron_mass({"K2_R_ETA_EXACTNESS_RETAINED"}),
    )

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    exactness_target = read(EXACTNESS_TARGET)
    pr5020_impact = read(PR5020_IMPACT)
    two_ninths_target = read(TWO_NINTHS_TARGET)
    two_ninths_decision = read(TWO_NINTHS_DECISION)
    two_ninths_no_go = read(TWO_NINTHS_NO_GO)
    pr5019_impact = read(PR5019_IMPACT)
    physical_electron = read(PHYSICAL_ELECTRON)
    brannen_open_gate = read(BRANNEN_OPEN_GATE)
    tier_a_bounded = read(TIER_A_BOUNDED)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    tier_a = read(TIER_A_REGISTRY)
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    realized_text = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
        ("K2 exactness target", exactness_target),
    ]:
        audit.check(f"{label} references K2 exactness current no-go", NOTE.name in container and "K2_R_ETA_EXACTNESS_RETAINED" in container)
    audit.check(
        "current no-go references two-ninths/radian target",
        TWO_NINTHS_TARGET.name in note and "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in note,
    )
    audit.check(
        "two-ninths/radian target keeps subgate partial",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in two_ninths_target
        and "not the full K2 exactness" in two_ninths_target,
    )
    audit.check(
        "two-ninths/radian decision packet keeps subgate conditional",
        TWO_NINTHS_DECISION.name in note
        and "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in two_ninths_decision
        and "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`." in two_ninths_decision,
    )
    audit.check(
        "current no-go references two-ninths/radian current-surface no-go",
        TWO_NINTHS_NO_GO.name in note and "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in note,
    )
    audit.check(
        "two-ninths/radian current no-go keeps subgate open",
        "current retained, primitive, merged-PR, and open-PR surfaces do not supply" in two_ninths_no_go
        and "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in two_ninths_no_go,
    )
    audit.check("#5020 impact keeps exactness open", "exactness remains open" in pr5020_impact and "No derivation or ratification of a Koide R-eta exactness theorem." in pr5020_impact)
    audit.check("#5019 impact remains premise hygiene", "premise hygiene and audit-readiness context" in pr5019_impact)
    audit.check("physical electron packet keeps K2 context non-mass", "K2 value-face progress only" in physical_electron and "no delta exactness theorem" in physical_electron)
    audit.check("Brannen open gate keeps delta as open gate", "not derive `delta = 2/9`" in brannen_open_gate)
    audit.check("Tier-A bounded theorem is not zero-import retained K2", "bounded theorem under explicit Tier-A admission" in tier_a_bounded and "Does **not** derive `delta = 2/9` from the framework baseline plus retained content" in tier_a_bounded)
    audit.check("realized primitive supplies no state-contingent value", "no state" in realized_text and "or value is supplied" in flat(realized_text))
    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in primitive_nodes)
    for absent in [
        "k2_r_eta_exactness_primitive",
        "registered_phi_value_face_primitive",
        "distinguished_two_ninths_theorem_primitive",
        "radian_readout_license_primitive",
        "fold_branch_domain_lock_primitive",
        "delta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in primitive_nodes)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in primitive_nodes)
    for excluded in ["mass ratio", "selector", "readout bridge", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open PR and non-claim boundaries")
    open_markers = [
        "`#5022` audit repair: delta-eta chain R-eta supplied premise | merged",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | open",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | open",
        "`#5018`/`#5017` chirality/domain-wall stack | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "clean/green status is not a proof input",
    ]
    for marker in open_markers:
        audit.check(f"open PR marker present: {marker}", flat(marker) in note_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No derivation or ratification of `REGISTERED_PHI_VALUE_FACE_ACCEPTED`.",
        "No derivation or ratification of `DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED`.",
        "No derivation or ratification of `RADIAN_READOUT_LICENSE_RETAINED`.",
        "No derivation or ratification of `FOLD_AND_BRANCH_DOMAIN_LOCK`.",
        "No claim that PR `#5020`, PR `#5021`, or merged PR `#5022` supplies K2 exactness.",
        "No derivation of `AC_phi_lambda`, `delta = 2/9`, `rho_e(delta)`, or `a_l^2`.",
        "No derivation or ratification of K1 occupancy/counting, K3 physical species",
        "No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`,",
        "No derivation of `S_l`, A3, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note ratifies Koide K2 exactness",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "delta = 2/9 is derived",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
