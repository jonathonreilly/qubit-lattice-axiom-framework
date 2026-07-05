#!/usr/bin/env python3
"""Verifier for the Koide two-ninths radian-readout current-surface no-go."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
K2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
TWO_NINTHS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
PR5020_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5019_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
FLAVOR_TWO_NINTHS = ROOT / "docs" / "FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md"
NATIVE_RADIAN_SEPARATION = ROOT / "docs" / "KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md"
A1_RADIAN_AUDIT = ROOT / "docs" / "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md"
BRANNEN_OPEN_GATE = ROOT / "docs" / "LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md"
TIER_A_BOUNDED = ROOT / "docs" / "CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md"
ORIENTATION_Z2 = ROOT / "docs" / "KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_NARROW_THEOREM_NOTE_2026-06-08.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


TWO_NINTHS_SUBGATE_INPUTS = {
    "TWO_NINTHS_READOUT_TEXT_LOCK",
    "FINITE_TWO_NINTHS_DENSITY_CONTEXT_ACCEPTED",
    "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
    "RADIAN_READOUT_LICENSE_RETAINED",
    "FOLD_AND_BRANCH_DOMAIN_LOCK",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_SURFACE_INPUTS = {
    "FINITE_TWO_NINTHS_DENSITY_CONTEXT_ACCEPTED",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
}

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


def closes_two_ninths_subgate(inputs: set[str]) -> bool:
    return TWO_NINTHS_SUBGATE_INPUTS <= inputs


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
        K2_TARGET,
        K2_NO_GO,
        TWO_NINTHS_TARGET,
        PR5020_IMPACT,
        PR5019_IMPACT,
        FLAVOR_TWO_NINTHS,
        NATIVE_RADIAN_SEPARATION,
        A1_RADIAN_AUDIT,
        BRANNEN_OPEN_GATE,
        TIER_A_BOUNDED,
        ORIENTATION_Z2,
        PHYSICAL_ELECTRON,
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
        "Koide Two-Ninths Radian Readout Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not ratify `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`",
        "current retained, primitive, and open-PR surfaces do not supply",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED",
        "TWO_NINTHS_READOUT_TEXT_LOCK",
        "FINITE_TWO_NINTHS_DENSITY_CONTEXT_ACCEPTED",
        "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
        "RADIAN_READOUT_LICENSE_RETAINED",
        "FOLD_AND_BRANCH_DOMAIN_LOCK",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md",
        "KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md",
        "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
        "LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md",
        "CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md",
        "KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_NARROW_THEOREM_NOTE_2026-06-08.md",
        "`#5021` primitive-retirement review draft",
        "no primitive retirement and no registry edit",
        "`#5022` audit repair: delta-eta chain R-eta supplied premise | open",
        "declared supplied readout-identification premise",
        "conditional repair only; no retained R-eta derivation, exact theorem, or radian-readout license",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | open",
        "No-Go Discipline Gate",
        "broad `delta = 2/9` no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    full_inputs = set(TWO_NINTHS_SUBGATE_INPUTS)
    audit.check("full subgate contract accepts retained handoff", closes_two_ninths_subgate(full_inputs))
    for missing in sorted(TWO_NINTHS_SUBGATE_INPUTS):
        reduced = set(TWO_NINTHS_SUBGATE_INPUTS)
        reduced.remove(missing)
        audit.check(f"subgate handoff fails without {missing}", not closes_two_ninths_subgate(reduced))
    accepted_subsets = [subset for subset in all_subsets(TWO_NINTHS_SUBGATE_INPUTS) if closes_two_ninths_subgate(subset)]
    audit.check("only full subgate subset closes handoff", accepted_subsets == [full_inputs])
    audit.check("current surface inputs do not close subgate", not closes_two_ninths_subgate(set(CURRENT_SURFACE_INPUTS)))
    audit.check(
        "subgate alone does not close K2 exactness",
        not closes_k2_exactness({"KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED"}),
    )
    audit.check(
        "subgate alone does not close physical electron mass",
        not closes_electron_mass({"KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED"}),
    )

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    k2_target = read(K2_TARGET)
    k2_no_go = read(K2_NO_GO)
    two_ninths_target = read(TWO_NINTHS_TARGET)
    pr5020_impact = read(PR5020_IMPACT)
    pr5019_impact = read(PR5019_IMPACT)
    flavor = read(FLAVOR_TWO_NINTHS)
    native = read(NATIVE_RADIAN_SEPARATION)
    a1_audit = read(A1_RADIAN_AUDIT)
    brannen_open_gate = read(BRANNEN_OPEN_GATE)
    tier_a_bounded = read(TIER_A_BOUNDED)
    orientation = read(ORIENTATION_Z2)
    physical_electron = read(PHYSICAL_ELECTRON)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    tier_a = read(TIER_A_REGISTRY)
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    realized_text = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
        ("K2 exactness target", k2_target),
        ("K2 exactness no-go", k2_no_go),
        ("two-ninths/radian target", two_ninths_target),
    ]:
        audit.check(
            f"{label} references two-ninths/radian current no-go",
            NOTE.name in container and "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in container,
        )

    audit.check("finite 2/9 source keeps readout open", "`2/9` is forced as a local" in flavor and "Physical readout is the one remaining gate" in flavor)
    audit.check("native radian theorem keeps bridge open", "does **not** close the radian-bridge postulate" in flat(native))
    audit.check("A1 radian audit keeps Type-B-to-radian law primitive", "TYPE_B_TO_RADIAN_IDENTIFICATION_REMAINS_PRIMITIVE=TRUE" in a1_audit)
    audit.check("Brannen open gate does not derive delta", "not derive `delta = 2/9`" in brannen_open_gate)
    audit.check(
        "Tier-A bounded theorem is not zero-import retained delta",
        "bounded theorem under explicit Tier-A admission" in tier_a_bounded
        and "Does **not** derive `delta = 2/9` from the framework baseline plus retained content" in tier_a_bounded,
    )
    audit.check(
        "orientation theorem leaves magnitude and handedness open",
        "does **not** supply the realized handedness" in orientation
        and "does **not** select the magnitude `2/9`" in orientation,
    )
    audit.check("#5020 impact keeps exactness residual open", "exactness remains open" in pr5020_impact)
    audit.check("#5019 impact remains premise hygiene", "premise hygiene and audit-readiness context" in pr5019_impact)
    audit.check("physical electron packet keeps K2 context non-mass", "K2 value-face progress only" in physical_electron and "no delta exactness theorem" in physical_electron)

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in primitive_nodes)
    for absent in [
        "koide_two_ninths_radian_readout_primitive",
        "distinguished_two_ninths_theorem_primitive",
        "radian_readout_license_primitive",
        "fold_branch_domain_lock_primitive",
        "delta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in primitive_nodes)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in primitive_nodes)
    audit.check("realized primitive supplies no state-contingent value", "no state" in realized_text and "or value is supplied" in flat(realized_text))
    for excluded in ["mass ratio", "phase", "selector", "readout bridge", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open PR and non-claim boundaries")
    open_markers = [
        "`#5022` audit repair: delta-eta chain R-eta supplied premise | open",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | open",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | open",
        "`#5018`/`#5017` chirality/domain-wall stack | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "clean status is not proof input",
    ]
    for marker in open_markers:
        audit.check(f"open PR marker present: {marker}", flat(marker) in note_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of `DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED`.",
        "No derivation or ratification of `RADIAN_READOUT_LICENSE_RETAINED`.",
        "No derivation or ratification of `FOLD_AND_BRANCH_DOMAIN_LOCK`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No adoption or landing claim for PR `#5020`, PR `#5021`, or PR `#5022`.",
        "No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`, observed",
        "No derivation of K1 occupancy/counting, K3 physical species bridge, K4",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note derives delta = 2/9",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED is supplied",
        "RADIAN_READOUT_LICENSE_RETAINED is supplied",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This note claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
