#!/usr/bin/env python3
"""Verifier for the zero-import hydrogen Koide native bridge target note.

This is a support runner. It verifies that the native zero-section bridge
target is explicit and remains separate from a retained physical electron
mass, alpha(0), and hydrogen calculation.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_TARGET_DISCRIMINATOR_2026-07-04.md"
BRIDGE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PR5007_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_PR5007_IMPACT_DISCRIMINATOR_2026-07-04.md"
GOAL_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
SOURCE_DECISION_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_PLACEMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
ALPHA_QED_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
STATIC_RYDBERG_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
KOIDE_ROUTE_NOTE = ROOT / "docs" / "KOIDE_NATIVE_ZERO_SECTION_CLOSURE_ROUTE_NOTE_2026-04-24.md"
KOIDE_ROUTE_RUNNER = ROOT / "scripts" / "frontier_koide_native_zero_section_closure_route.py"
KOIDE_REVIEW_NOTE = ROOT / "docs" / "KOIDE_NATIVE_ZERO_SECTION_NATURE_REVIEW_NOTE_2026-04-24.md"
KOIDE_REVIEW_RUNNER = ROOT / "scripts" / "frontier_koide_native_zero_section_nature_review.py"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE_PRIMITIVE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC_PRIMITIVE = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED_PRIMITIVE = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


NATIVE_BRIDGE_INPUTS = {
    "ZERO_SOURCE_READOUT_RETAINED",
    "REAL_PRIMITIVE_BRANNEN_ENDPOINT_RETAINED",
    "BASED_DETERMINANT_LINE_READOUT_RETAINED",
    "NO_COMPARATOR_PROOF_INPUT",
    "AUDIT_ACCEPTANCE",
}

PHYSICAL_ELECTRON_READOUT_INPUTS = NATIVE_BRIDGE_INPUTS | {
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
}

ZERO_IMPORT_HYDROGEN_INPUTS = PHYSICAL_ELECTRON_READOUT_INPUTS | {
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


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def closes_native_bridge(inputs: set[str]) -> bool:
    return NATIVE_BRIDGE_INPUTS <= inputs


def closes_physical_electron_readout(inputs: set[str]) -> bool:
    return PHYSICAL_ELECTRON_READOUT_INPUTS <= inputs


def closes_zero_import_hydrogen(inputs: set[str]) -> bool:
    return ZERO_IMPORT_HYDROGEN_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        BRIDGE_DECISION,
        KOIDE_FIREWALL,
        PR5007_IMPACT,
        GOAL_PACKET,
        SOURCE_DECISION_PACKET,
        A3_PLACEMENT,
        ALPHA_QED_TARGET,
        STATIC_RYDBERG_TARGET,
        KOIDE_ROUTE_NOTE,
        KOIDE_ROUTE_RUNNER,
        KOIDE_REVIEW_NOTE,
        KOIDE_REVIEW_RUNNER,
        PRIMITIVE_REGISTRY,
        TIER_A_REGISTRY,
        MINIMAL_AXIOMS,
        SCALE_PRIMITIVE,
        KINETIC_PRIMITIVE,
        REALIZED_PRIMITIVE,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = " ".join(note.split())
    bridge_decision = read(BRIDGE_DECISION)
    koide_firewall = read(KOIDE_FIREWALL)
    pr5007_impact = read(PR5007_IMPACT)
    goal_packet = read(GOAL_PACKET)
    source_decision = read(SOURCE_DECISION_PACKET)
    route_note = read(KOIDE_ROUTE_NOTE)
    route_runner = read(KOIDE_ROUTE_RUNNER)
    review_runner = read(KOIDE_REVIEW_RUNNER)
    primitive_registry = read(PRIMITIVE_REGISTRY)
    primitive_data = json.loads(primitive_registry)
    tier_a_registry = read(TIER_A_REGISTRY)
    primitive_sources = "\n".join(
        [
            read(MINIMAL_AXIOMS),
            read(SCALE_PRIMITIVE),
            read(KINETIC_PRIMITIVE),
            read(REALIZED_PRIMITIVE),
        ]
    )

    section("Required note content")
    required_phrases = [
        "Zero-Import Hydrogen: Koide Native Zero-Section Bridge Target Discriminator",
        "KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "BRIDGE_TEXT_LOCK",
        "ZERO_SOURCE_READOUT_RETAINED",
        "REAL_PRIMITIVE_BRANNEN_ENDPOINT_RETAINED",
        "BASED_DETERMINANT_LINE_READOUT_RETAINED",
        "NO_COMPARATOR_PROOF_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "PHYSICAL_ELECTRON_READOUT_RETAINED",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_RETAINED",
        "ALPHA0_RETAINED",
        "STATIC_SOURCE_RYDBERG_RETAINED",
        "observed lepton masses",
        "observed `m_W`",
        "fitted `delta = 2/9`",
        "`#5011` eta twisted walk family runner | `CLEAN`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN`",
        "Merge-state labels are moving review metadata",
        "The progress value is narrow but real",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed Koide native zero-section bridge",
    ]
    for phrase in required_phrases:
        audit.check(f"required note phrase present: {phrase}", " ".join(phrase.split()) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Source boundary checks")
    for phrase in [
        "physical Koide closure",
        "No physical charged-lepton zero-source readout is derived.",
        "No physical Brannen endpoint identification is derived.",
        "No physical determinant-line based readout is derived.",
        "KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE",
    ]:
        audit.check(f"route note preserves boundary: {phrase}", phrase in route_note)

    for phrase in [
        "Need physical proof of zero-source readout, real-primitive Brannen endpoint, and unit-preserving determinant-line readout.",
        "No physical Brannen endpoint, determinant-line unit, or charged-lepton zero-source identification is derived here.",
        "KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE",
    ]:
        audit.check(f"route runner preserves boundary: {phrase}", phrase in route_runner)

    for phrase in [
        "KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE",
        "PASSED: 12/12",
        "zero-source readout",
        "real-primitive Brannen endpoint",
        "based determinant-line readout",
    ]:
        audit.check(f"review runner / #5007 surface preserves: {phrase}", phrase in review_runner or phrase in pr5007_impact)

    for phrase in [
        "K1 | Counting-measure bit",
        "K2 | Radian/readout identification",
        "K3 | Species/electron branch",
        "K4 | Absolute scale",
        "Q=2/3` is a shape-surface condition, not yet an electron eigenvalue",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_TARGET_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
    ]:
        audit.check(f"Koide firewall boundary present: {phrase}", phrase in koide_firewall)

    for phrase in [
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_TARGET_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "Koide native zero-section bridge target",
        "Z1-Z3",
    ]:
        audit.check(f"goal packet references bridge target: {phrase}", phrase in goal_packet)

    for phrase in [
        "BRIDGE_TEXT_LOCK",
        "ZERO_SOURCE_READOUT_RETAINED",
        "REAL_PRIMITIVE_BRANNEN_ENDPOINT_RETAINED",
        "BASED_DETERMINANT_LINE_READOUT_RETAINED",
        "No derivation or ratification of the native zero-section bridge.",
    ]:
        audit.check(f"bridge decision packet boundary present: {phrase}", phrase in bridge_decision)

    audit.check(
        "source decision packet remains scale-side only",
        "source-side `S_l = 1/256`" in source_decision and "does not derive `m_e`" in source_decision,
    )

    section("Closure predicate checks")
    audit.check(
        "all native bridge inputs close native bridge predicate",
        closes_native_bridge(set(NATIVE_BRIDGE_INPUTS)),
    )
    for missing in sorted(NATIVE_BRIDGE_INPUTS):
        reduced = set(NATIVE_BRIDGE_INPUTS)
        reduced.remove(missing)
        audit.check(
            f"native bridge predicate fails without {missing}",
            not closes_native_bridge(reduced),
        )

    audit.check(
        "native bridge alone does not close physical electron readout",
        not closes_physical_electron_readout(set(NATIVE_BRIDGE_INPUTS)),
    )
    audit.check(
        "all physical electron inputs close electron predicate",
        closes_physical_electron_readout(set(PHYSICAL_ELECTRON_READOUT_INPUTS)),
    )
    for missing in sorted(PHYSICAL_ELECTRON_READOUT_INPUTS):
        reduced = set(PHYSICAL_ELECTRON_READOUT_INPUTS)
        reduced.remove(missing)
        audit.check(
            f"physical electron predicate fails without {missing}",
            not closes_physical_electron_readout(reduced),
        )

    audit.check(
        "physical electron readout alone does not close zero-import hydrogen",
        not closes_zero_import_hydrogen(set(PHYSICAL_ELECTRON_READOUT_INPUTS)),
    )
    audit.check(
        "all hydrogen inputs close zero-import hydrogen predicate model",
        closes_zero_import_hydrogen(set(ZERO_IMPORT_HYDROGEN_INPUTS)),
    )
    for missing in sorted(ZERO_IMPORT_HYDROGEN_INPUTS):
        reduced = set(ZERO_IMPORT_HYDROGEN_INPUTS)
        reduced.remove(missing)
        audit.check(
            f"zero-import hydrogen predicate model fails without {missing}",
            not closes_zero_import_hydrogen(reduced),
        )

    section("Registry boundary")
    nodes = primitive_data["nodes"]
    for node, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"primitive registry node exists: {node}", node in nodes)
        audit.check(
            f"primitive registry current_path for {node}",
            nodes.get(node, {}).get("current_path") == path,
            nodes.get(node, {}).get("current_path", ""),
        )

    audit.check("AC_phi_lambda remains a Tier-A registry row", "AC_phi_lambda" in tier_a_registry)
    audit.check("AC_phi_lambda is not an axiom/primitive node", "AC_phi_lambda" not in nodes)
    for phrase in [
        "selector",
        "readout bridge",
        "source/action",
        "normalization rule",
        "probability rule",
        "empirical fit",
    ]:
        audit.check(f"primitive/minimal sources do not silently supply {phrase}", phrase in primitive_sources)
    audit.check("bridge note keeps empirical match separate", "empirical match" in note)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `m_e`.",
        "No derivation that `#5007` is retained, merged, or sufficient for electron",
        "No derivation of Z1 zero-source readout.",
        "No derivation of Z2 real-primitive Brannen endpoint.",
        "No derivation of Z3 based determinant-line readout.",
        "No derivation of the physical electron species bridge.",
        "No derivation of `a_l^2`, `S_l`, `C_A3`, `alpha(0)`, or hydrogen",
        "No new axiom, primitive, or admitted import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `m_e`",
        "This note derives hydrogen",
        "#5007 closes hydrogen",
        "#5007 derives the electron",
        "Z1 is derived",
        "Z2 is derived",
        "Z3 is derived",
        "alpha(0) is retained",
        "hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
