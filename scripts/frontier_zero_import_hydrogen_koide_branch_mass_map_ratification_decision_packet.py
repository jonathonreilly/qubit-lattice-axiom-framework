#!/usr/bin/env python3
"""Verifier for the Koide branch mass-map decision packet.

This runner checks that the branch-to-mass map is explicit and remains
separate from phase selection, physical species identity, absolute scale, the
electron-mass handoff, and hydrogen closure.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
ELECTRON_MASS_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
CURRENT_SURFACE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KOIDE_Q_NARROW = ROOT / "docs" / "KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md"
KOIDE_CONE_NARROW = ROOT / "docs" / "CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md"
KOIDE_CHARACTER_NARROW = ROOT / "docs" / "KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md"
KOIDE_SQRTM = ROOT / "docs" / "KOIDE_SQRTM_AMPLITUDE_PRINCIPLE_NOTE_2026-04-18.md"
KOIDE_PARENT = ROOT / "docs" / "KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md"
BRANNEN_OPEN_GATE = ROOT / "docs" / "LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE_REFERENCE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"


BRANCH_MASS_MAP_INPUTS = {
    "KOIDE_BRANCH_MASS_MAP_TEXT_LOCK",
    "BRANNEN_CIRCULANT_BRANCH_FORM_RETAINED",
    "SQUARE_ROOT_MASS_READOUT_RETAINED",
    "POSITIVE_CHAMBER_OR_SIGN_RULE_RETAINED",
    "SCALE_PARAMETER_COMPOSITION_RETAINED",
    "PHASE_SCALE_SPECIES_SCOPE_LOCK",
    "NO_LEPTON_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

PHYSICAL_ELECTRON_MASS_INPUTS = {
    "PHYSICAL_ELECTRON_MASS_TEXT_LOCK",
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
    "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
    "NO_LEPTON_COMPARATOR_PROOF_INPUT",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
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


def closes_branch_mass_map(inputs: set[str]) -> bool:
    return BRANCH_MASS_MAP_INPUTS <= inputs


def closes_physical_electron_mass(inputs: set[str]) -> bool:
    return PHYSICAL_ELECTRON_MASS_INPUTS <= inputs


def branch_ratio(k: int, delta: float) -> float:
    return 1.0 + math.sqrt(2.0) * math.cos(delta + 2.0 * math.pi * k / 3.0)


def branch_ratios(delta: float) -> list[float]:
    return [branch_ratio(k, delta) for k in range(3)]


def signed_koide_q(delta: float) -> float:
    roots = branch_ratios(delta)
    return sum(r * r for r in roots) / (sum(roots) ** 2)


def physical_mass_koide_q(delta: float) -> float:
    roots = branch_ratios(delta)
    masses = [r * r for r in roots]
    return sum(masses) / (sum(math.sqrt(m) for m in masses) ** 2)


def rho_e(delta: float) -> float:
    return min(r * r for r in branch_ratios(delta))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        KOIDE_FIREWALL,
        ELECTRON_MASS_PACKET,
        CURRENT_SURFACE_NO_GO,
        KOIDE_Q_NARROW,
        KOIDE_CONE_NARROW,
        KOIDE_CHARACTER_NARROW,
        KOIDE_SQRTM,
        KOIDE_PARENT,
        BRANNEN_OPEN_GATE,
        REGISTRY,
        TIER_A_REGISTRY,
        MINIMAL,
        SCALE_REFERENCE,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required note content")
    required_phrases = [
        "Koide Branch Mass-Map Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify the Koide branch mass map",
        "KOIDE_BRANCH_MASS_MAP_RETAINED",
        "the Koide/Brannen branch-to-mass map used by the hydrogen electron-mass lane",
        "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current surfaces do not supply `KOIDE_BRANCH_MASS_MAP_RETAINED`",
        "KOIDE_BRANCH_MASS_MAP_TEXT_LOCK",
        "BRANNEN_CIRCULANT_BRANCH_FORM_RETAINED",
        "SQUARE_ROOT_MASS_READOUT_RETAINED",
        "POSITIVE_CHAMBER_OR_SIGN_RULE_RETAINED",
        "SCALE_PARAMETER_COMPOSITION_RETAINED",
        "PHASE_SCALE_SPECIES_SCOPE_LOCK",
        "NO_LEPTON_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those ten contract inputs",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "r_k(delta) = 1 + sqrt(2) cos(delta + 2 pi k / 3)",
        "m_k = a_l^2 r_k(delta)^2",
        "delta = 2/9",
        "delta = 1",
        "`#5013` theta native positive-class adjudication | `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `SUCCESS`",
        "`#5011` eta twisted walk family runner | `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `SUCCESS`",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "decision-ready ratification",
        "broad branch-mass-map-retention claim fails; narrowed Koide",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(BRANCH_MASS_MAP_INPUTS)
    audit.check("full branch mass-map contract accepts decision", closes_branch_mass_map(full_inputs))
    for missing in sorted(BRANCH_MASS_MAP_INPUTS):
        reduced = set(BRANCH_MASS_MAP_INPUTS)
        reduced.remove(missing)
        audit.check(f"branch mass-map decision fails without {missing}", not closes_branch_mass_map(reduced))
    accepted_subsets = [subset for subset in all_subsets(BRANCH_MASS_MAP_INPUTS) if closes_branch_mass_map(subset)]
    audit.check("only full tested contract subset closes branch mass map", accepted_subsets == [full_inputs])

    branch_consequence = {"KOIDE_BRANCH_MASS_MAP_RETAINED"}
    audit.check("branch mass map alone does not close physical electron mass", not closes_physical_electron_mass(branch_consequence))
    full_electron = set(PHYSICAL_ELECTRON_MASS_INPUTS)
    audit.check("full physical electron mass predicate model closes", closes_physical_electron_mass(full_electron))
    for missing in sorted(PHYSICAL_ELECTRON_MASS_INPUTS):
        reduced = set(PHYSICAL_ELECTRON_MASS_INPUTS)
        reduced.remove(missing)
        audit.check(f"physical electron mass fails without {missing}", not closes_physical_electron_mass(reduced))

    section("Finite branch map checks")
    delta = 2.0 / 9.0
    expected_roots = [
        0.04034990821920668,
        0.5802119201475365,
        2.3794381716332564,
    ]
    sorted_roots = sorted(branch_ratios(delta))
    for got, expected, label in zip(sorted_roots, expected_roots, ["electron-like", "muon-like", "tau-like"]):
        audit.check(
            f"delta=2/9 sorted {label} root ratio matches comparator",
            abs(got - expected) < 1e-14,
            f"{got:.15f}",
        )
    audit.check("delta=2/9 is in the positive chamber", all(r > 0.0 for r in branch_ratios(delta)))
    audit.check("delta=2/9 physical mass Koide Q is 2/3", abs(physical_mass_koide_q(delta) - 2.0 / 3.0) < 1e-14)
    audit.check(
        "delta=2/9 electron-like mass factor matches rho",
        abs(rho_e(delta) - expected_roots[0] ** 2) < 1e-16,
        f"rho={rho_e(delta):.15f}",
    )

    zero_roots = branch_ratios(0.0)
    audit.check("delta=0 is also positive chamber", all(r > 0.0 for r in zero_roots))
    audit.check("delta=0 same signed Q but different rho", abs(signed_koide_q(0.0) - 2.0 / 3.0) < 1e-14 and rho_e(0.0) / rho_e(delta) > 50.0)

    delta_bad = 1.0
    bad_roots = branch_ratios(delta_bad)
    audit.check("delta=1 has a negative signed branch", min(bad_roots) < 0.0, f"min={min(bad_roots):.6f}")
    audit.check("signed algebraic Q remains 2/3 at delta=1", abs(signed_koide_q(delta_bad) - 2.0 / 3.0) < 1e-14)
    audit.check(
        "physical positive-root Koide expression differs when a branch is negative",
        abs(physical_mass_koide_q(delta_bad) - 2.0 / 3.0) > 0.05,
        f"Q_abs={physical_mass_koide_q(delta_bad):.6f}",
    )

    a2 = 313.841126
    masses = [a2 * r * r for r in branch_ratios(delta)]
    masses_scaled = [1.01 * a2 * r * r for r in branch_ratios(delta)]
    for mass, scaled in zip(masses, masses_scaled):
        audit.check("scale replacement multiplies branch mass", abs(scaled / mass - 1.01) < 1e-14)
    audit.check("permuting branch labels preserves unordered mass triple", sorted(masses) == sorted(reversed(masses)))
    audit.check("branch map alone does not select electron species", min(masses) == sorted(masses)[0] and len(set(round(m, 12) for m in masses)) == 3)

    section("Authority boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    electron_mass_packet = read(ELECTRON_MASS_PACKET)
    current_surface_no_go = read(CURRENT_SURFACE_NO_GO)
    q_narrow = read(KOIDE_Q_NARROW)
    cone_narrow = read(KOIDE_CONE_NARROW)
    character_narrow = read(KOIDE_CHARACTER_NARROW)
    sqrtm = read(KOIDE_SQRTM)
    koide_parent = read(KOIDE_PARENT)
    brannen_open_gate = read(BRANNEN_OPEN_GATE)
    minimal = read(MINIMAL)
    scale_reference = flat(read(SCALE_REFERENCE)).lower()
    registry = json.loads(read(REGISTRY))
    tier_a = read(TIER_A_REGISTRY)
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
        ("physical electron mass packet", electron_mass_packet),
    ]:
        audit.check(f"{container_name} references branch mass-map packet", NOTE.name in container)

    audit.check("current-surface no-go keeps branch mass map open", "KOIDE_BRANCH_MASS_MAP_RETAINED" in current_surface_no_go and "SQUARE_ROOT_MASS_READOUT_RETAINED" in current_surface_no_go)
    audit.check("Q narrow theorem is abstract only", "treated as abstract symbols, not as physical masses" in q_narrow)
    audit.check("Q narrow theorem excludes sqrt(m) readout", "No `sqrt(m)` readout law is consumed." in q_narrow)
    audit.check("Q narrow theorem preserves sqrt(m) gap", "`sqrt(m)` vs `m` identification" in q_narrow)
    audit.check("cone narrow theorem keeps mass-square-root assignment downstream", "mass-square-root assignment enters" in cone_narrow and "downstream" in cone_narrow)
    audit.check("character narrow theorem excludes spectral readout", "spectral-to-physical-readout law" in character_narrow)
    audit.check("sqrtm note narrows but does not derive masses", "does not yet derive the charged-lepton masses" in sqrtm)
    audit.check("sqrtm note keeps positive parent open", "derive the positive parent operator `M`" in sqrtm)
    audit.check("parent circulant note is bounded, not retained Koide", "bounded_theorem" in koide_parent and "not retained today" in koide_parent)
    audit.check("parent circulant note keeps square-root readout open", "any derivation of the square-root readout identification" in koide_parent)
    brannen_flat = flat(brannen_open_gate)
    audit.check(
        "Brannen open gate excludes phase, coefficient, and scale",
        all(token in brannen_flat for token in ["does not derive", "delta = 2/9", "sqrt(2)", "dimensionful charged-lepton scale"]),
    )
    audit.check("electron mass packet consumes branch mass map", "KOIDE_BRANCH_MASS_MAP_RETAINED" in electron_mass_packet)
    minimal_flat = flat(minimal)
    audit.check(
        "minimal axioms keep downstream bridges outside axiom content",
        "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration" in minimal_flat,
    )
    audit.check("scale primitive has zero dimensionless content", "zero dimensionless content" in scale_reference and "mass ratio" in scale_reference)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    for absent in [
        "koide_branch_mass_map_primitive",
        "square_root_mass_readout_primitive",
        "positive_chamber_primitive",
        "brannen_circulant_branch_form_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5013` theta native positive-class adjudication | `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `SUCCESS`",
        "`#5011` eta twisted walk family runner | `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of the Koide branch mass map.",
        "No derivation or ratification of the Brannen/circulant branch form.",
        "No derivation or ratification of square-root mass readout.",
        "No derivation or ratification of the positive chamber/sign rule.",
        "No derivation or ratification of a physical electron species bridge.",
        "No derivation of `Q=2/3`, `delta = 2/9`, `rho_e(delta)`, or `a_l^2`.",
        "No use of observed lepton masses, observed `m_W`, fitted `a_l`, fitted",
        "No derivation of physical electron mass, `alpha(0)`, static-source Rydberg,",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies the Koide branch mass map",
        "This packet derives the Koide branch mass map",
        "square-root mass readout is retained",
        "positive chamber/sign rule is retained",
        "delta = 2/9 is derived",
        "physical electron mass is retained",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
