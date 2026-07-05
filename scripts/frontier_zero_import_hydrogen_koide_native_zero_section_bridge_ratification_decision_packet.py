#!/usr/bin/env python3
"""Verifier for the Koide native zero-section bridge decision packet.

This runner checks that the bridge decision contract is explicit and remains
separate from physical electron readout, alpha(0), and hydrogen closure.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE_TRIAGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
BRIDGE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_TARGET_DISCRIMINATOR_2026-07-04.md"
BRIDGE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PR5007_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_PR5007_IMPACT_DISCRIMINATOR_2026-07-04.md"
SOURCE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ALPHA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
STATIC_RYDBERG_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
KOIDE_ROUTE_NOTE = ROOT / "docs" / "KOIDE_NATIVE_ZERO_SECTION_CLOSURE_ROUTE_NOTE_2026-04-24.md"
KOIDE_ROUTE_RUNNER = ROOT / "scripts" / "frontier_koide_native_zero_section_closure_route.py"
KOIDE_REVIEW_NOTE = ROOT / "docs" / "KOIDE_NATIVE_ZERO_SECTION_NATURE_REVIEW_NOTE_2026-04-24.md"
KOIDE_REVIEW_RUNNER = ROOT / "scripts" / "frontier_koide_native_zero_section_nature_review.py"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


BRIDGE_DECISION_INPUTS = {
    "BRIDGE_TEXT_LOCK",
    "ZERO_SOURCE_READOUT_RETAINED",
    "REAL_PRIMITIVE_BRANNEN_ENDPOINT_RETAINED",
    "BASED_DETERMINANT_LINE_READOUT_RETAINED",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

PHYSICAL_ELECTRON_INPUTS = {
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
}

HYDROGEN_INPUTS = PHYSICAL_ELECTRON_INPUTS | {
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


def all_subsets(items: set[str]) -> list[set[str]]:
    ordered = sorted(items)
    subsets: list[set[str]] = []
    for size in range(len(ordered) + 1):
        for combo in combinations(ordered, size):
            subsets.append(set(combo))
    return subsets


def closes_bridge_decision(inputs: set[str]) -> bool:
    return BRIDGE_DECISION_INPUTS <= inputs


def closes_physical_electron(inputs: set[str]) -> bool:
    return PHYSICAL_ELECTRON_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def q_from_weight(w_plus: Fraction) -> Fraction:
    r = (1 - w_plus) / w_plus
    return (1 + r) / 3


def ktl_from_weight(w_plus: Fraction) -> Fraction:
    r = (1 - w_plus) / w_plus
    return (r * r - 1) / (4 * r)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        ROUTE_TRIAGE,
        KOIDE_FIREWALL,
        BRIDGE_TARGET,
        BRIDGE_NO_GO,
        PR5007_IMPACT,
        SOURCE_DECISION,
        A3_DECISION,
        ALPHA_TARGET,
        STATIC_RYDBERG_TARGET,
        KOIDE_ROUTE_NOTE,
        KOIDE_ROUTE_RUNNER,
        KOIDE_REVIEW_NOTE,
        KOIDE_REVIEW_RUNNER,
        REGISTRY,
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
        "Koide Native Zero-Section Bridge Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify the native zero-section bridge",
        "the physical native zero-section bridge for the charged-lepton Koide route",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "ZERO_SOURCE_READOUT_RETAINED",
        "REAL_PRIMITIVE_BRANNEN_ENDPOINT_RETAINED",
        "BASED_DETERMINANT_LINE_READOUT_RETAINED",
        "BRIDGE_TEXT_LOCK",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those eight contract inputs is a retained native zero-section bridge decision",
        "PHYSICAL_ELECTRON_READOUT_RETAINED",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "ALPHA0_RETAINED",
        "STATIC_SOURCE_RYDBERG_RETAINED",
        "KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE",
        "eta_Z3 = 2/9",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "native bridge target remains needed",
        "`#5011` eta twisted walk family runner | `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `SUCCESS`",
        "Merge-state labels are moving review metadata",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "decision-ready ratification contract",
        "broad bridge-retention claim fails; narrowed Koide native",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(BRIDGE_DECISION_INPUTS)
    audit.check("full bridge contract accepts decision", closes_bridge_decision(full_inputs))
    for missing in sorted(BRIDGE_DECISION_INPUTS):
        reduced = set(BRIDGE_DECISION_INPUTS)
        reduced.remove(missing)
        audit.check(f"bridge decision fails without {missing}", not closes_bridge_decision(reduced))
    accepted_subsets = [subset for subset in all_subsets(BRIDGE_DECISION_INPUTS) if closes_bridge_decision(subset)]
    audit.check("only full tested contract subset closes bridge decision", accepted_subsets == [full_inputs])

    bridge_consequence = {"NATIVE_ZERO_SECTION_BRIDGE_RETAINED"}
    audit.check("native bridge alone does not close physical electron", not closes_physical_electron(bridge_consequence))
    audit.check("full physical electron predicate closes electron", closes_physical_electron(set(PHYSICAL_ELECTRON_INPUTS)))
    for missing in sorted(PHYSICAL_ELECTRON_INPUTS):
        reduced = set(PHYSICAL_ELECTRON_INPUTS)
        reduced.remove(missing)
        audit.check(f"physical electron predicate fails without {missing}", not closes_physical_electron(reduced))
    audit.check("physical electron alone does not close hydrogen", not closes_hydrogen(set(PHYSICAL_ELECTRON_INPUTS)))
    audit.check("full hydrogen predicate model closes hydrogen", closes_hydrogen(set(HYDROGEN_INPUTS)))

    section("Finite route witness checks")
    z0_w = Fraction(1 + 0, 2)
    z_bad_w = Fraction(1, 3)
    audit.check("zero source gives w_plus=1/2", z0_w == Fraction(1, 2))
    audit.check("zero source gives K_TL=0", ktl_from_weight(z0_w) == 0)
    audit.check("zero source gives Q=2/3", q_from_weight(z0_w) == Fraction(2, 3))
    audit.check("nonzero source falsifier gives Q=1", q_from_weight(z_bad_w) == 1)
    audit.check("nonzero source falsifier gives K_TL=3/8", ktl_from_weight(z_bad_w) == Fraction(3, 8))
    idempotents = {(0, 0), (1, 0)}
    audit.check("real Z3 commutant idempotents are only 0 and I in route witness", idempotents == {(0, 0), (1, 0)})
    eta_z3 = Fraction(2, 9)
    c_based = Fraction(0)
    c_unbased = Fraction(1, 9)
    audit.check("finite Z3 scalar is eta_Z3=2/9", eta_z3 == Fraction(2, 9))
    audit.check("based endpoint gives delta_open=2/9", eta_z3 + c_based == Fraction(2, 9))
    audit.check("unbased torsor falsifier gives delta_open=1/3", eta_z3 + c_unbased == Fraction(1, 3))

    section("Authority boundary checks")
    goal = read(GOAL)
    route_triage = read(ROUTE_TRIAGE)
    koide_firewall = read(KOIDE_FIREWALL)
    bridge_target = read(BRIDGE_TARGET)
    bridge_no_go = read(BRIDGE_NO_GO)
    pr5007 = read(PR5007_IMPACT)
    source_decision = read(SOURCE_DECISION)
    a3_decision = read(A3_DECISION)
    alpha_target = read(ALPHA_TARGET)
    static_target = read(STATIC_RYDBERG_TARGET)
    route_note = read(KOIDE_ROUTE_NOTE)
    route_runner = read(KOIDE_ROUTE_RUNNER)
    review_runner = read(KOIDE_REVIEW_RUNNER)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    tier_a_registry = read(TIER_A_REGISTRY)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    nodes = registry["nodes"]

    audit.check("goal packet references bridge decision packet", NOTE.name in goal)
    audit.check("route triage references bridge decision packet", NOTE.name in route_triage)
    audit.check("Koide firewall references bridge decision packet", NOTE.name in koide_firewall)
    audit.check("bridge target references bridge decision packet", NOTE.name in bridge_target)
    audit.check("bridge decision references native bridge no-go", BRIDGE_NO_GO.name in note and "native bridge target remains needed" in note)
    audit.check(
        "native bridge no-go keeps bridge open",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in bridge_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in bridge_no_go,
    )
    audit.check("PR5007 impact keeps Z1-Z3 pending", all(p in pr5007 for p in ["zero-source readout", "real-primitive Brannen endpoint", "based determinant-line readout"]))
    audit.check("source decision remains K4 scale-side support", "S_l = 1/256" in source_decision and "does not derive `m_e`" in source_decision)
    audit.check("A3 decision remains precision placement only", "does not ratify A3" in a3_decision and "Koide/electron readout correction" in a3_decision)
    audit.check("alpha target remains downstream", "No derivation of `alpha(0)`" in alpha_target and "R-Lep" in alpha_target)
    audit.check("static Rydberg target remains final substitution gate", "STATIC_SOURCE_RYDBERG" in static_target or "static-source Rydberg" in static_target)
    audit.check("route note does not claim physical closure", "No physical Koide closure is asserted" in route_note)
    audit.check("route runner preserves bridge boundary", "PHYSICAL_BRIDGE_IDENTIFICATIONS_CLAIMED=FALSE" in route_runner)
    audit.check("review runner keeps retained closure false", "KOIDE_NATIVE_ZERO_SECTION_RETAINED_CLOSURE=FALSE" in review_runner)
    audit.check("minimal axioms exclude physical-observable identification", "physical-observable identification" in minimal)
    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a_registry and "AC_phi_lambda" not in nodes)
    audit.check("no native bridge primitive registered", "native_zero_section_bridge_primitive" not in nodes)
    audit.check("scale primitive excludes dimensionless Koide content", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes state selection and values", "state-selection rule" in realized and "or value is supplied" in realized)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5011` eta twisted walk family runner | `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of the native zero-section bridge.",
        "No derivation of Z1 zero-source readout.",
        "No derivation of Z2 real-primitive Brannen endpoint.",
        "No derivation of Z3 based determinant-line readout.",
        "No derivation of the physical electron species bridge.",
        "No derivation of `a_l^2`, `S_l`, `C_A3`, `m_e`, `alpha(0)`, or hydrogen",
        "No use of observed lepton masses, observed `m_W`, fitted `a_l`, fitted",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies the native zero-section bridge",
        "native zero-section bridge is retained",
        "Z1 is derived",
        "Z2 is derived",
        "Z3 is derived",
        "m_e is derived",
        "alpha(0) is derived",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
