#!/usr/bin/env python3
"""Verifier for the Koide branch mass-map current-surface no-go.

This runner checks that current Koide algebra, primitive, and open-PR surfaces
do not silently supply the physical branch-to-mass map needed by the
zero-import hydrogen electron-mass lane. It preserves the map as an open route
and does not derive m_e, alpha(0), Rydberg, or hydrogen.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
BRANCH_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ELECTRON_MASS_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
KOIDE_Q_NARROW = ROOT / "docs" / "KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md"
KOIDE_CONE_NARROW = ROOT / "docs" / "CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md"
KOIDE_CHARACTER_NARROW = ROOT / "docs" / "KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md"
KOIDE_SQRTM = ROOT / "docs" / "KOIDE_SQRTM_AMPLITUDE_PRINCIPLE_NOTE_2026-04-18.md"
KOIDE_PARENT = ROOT / "docs" / "KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md"
BRANNEN_OPEN_GATE = ROOT / "docs" / "LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

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
        BRANCH_PACKET,
        ELECTRON_MASS_PACKET,
        STATIC_TARGET,
        KOIDE_Q_NARROW,
        KOIDE_CONE_NARROW,
        KOIDE_CHARACTER_NARROW,
        KOIDE_SQRTM,
        KOIDE_PARENT,
        BRANNEN_OPEN_GATE,
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
        "Koide Branch Mass-Map Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not ratify the Koide branch mass map",
        "KOIDE_BRANCH_MASS_MAP_RETAINED",
        "r_k(delta) = 1 + sqrt(2) cos(delta + 2 pi k / 3)",
        "m_k = a_l^2 r_k(delta)^2",
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
        "formal `m_k := x_k^2`",
        "physical charged-lepton square-root masses",
        "delta = 2/9",
        "r_e(delta)^2 = 0.001628115093",
        "koide_branch_mass_map_primitive",
        "square_root_mass_readout_primitive",
        "positive_chamber_sign_rule_primitive",
        "brannen_circulant_branch_form_primitive",
        "scale_parameter_composition_primitive",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "No-Go Discipline Gate",
        "broad branch mass-map no-go fails; narrowed current-surface non-supply claim passes",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Branch mass-map predicate checks")
    full_inputs = set(BRANCH_MASS_MAP_INPUTS)
    audit.check("full branch mass-map contract accepts retained handoff", closes_branch_mass_map(full_inputs))
    for missing in sorted(BRANCH_MASS_MAP_INPUTS):
        reduced = set(BRANCH_MASS_MAP_INPUTS)
        reduced.remove(missing)
        audit.check(f"branch mass-map handoff fails without {missing}", not closes_branch_mass_map(reduced))
    accepted_subsets = [subset for subset in all_subsets(BRANCH_MASS_MAP_INPUTS) if closes_branch_mass_map(subset)]
    audit.check("only full branch mass-map subset closes handoff", accepted_subsets == [full_inputs])
    current_surface = {
        "KOIDE_BRANCH_MASS_MAP_TEXT_LOCK",
        "PHASE_SCALE_SPECIES_SCOPE_LOCK",
        "NO_LEPTON_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    }
    audit.check(
        "current surface without branch/readout/chamber/scale inputs does not close mass map",
        not closes_branch_mass_map(current_surface),
    )

    section("Finite branch arithmetic checks")
    delta = 2.0 / 9.0
    roots = sorted(branch_ratios(delta))
    expected_roots = [
        0.04034990821920668,
        0.5802119201475365,
        2.3794381716332564,
    ]
    for got, expected, label in zip(roots, expected_roots, ["electron-like", "muon-like", "tau-like"]):
        audit.check(f"delta=2/9 sorted {label} root ratio reproduced", abs(got - expected) < 1e-14, f"{got:.15f}")
    rho_delta = rho_e(delta)
    audit.check("delta=2/9 electron factor reproduced", abs(rho_delta - expected_roots[0] ** 2) < 1e-16, f"{rho_delta:.15f}")
    for test_delta in [delta, 0.0, 0.5, 1.0, 3.0 * math.pi / 4.0]:
        audit.check(
            f"signed Koide Q is 2/3 at delta={test_delta:.6f}",
            abs(signed_koide_q(test_delta) - 2.0 / 3.0) < 1e-14,
            f"Q={signed_koide_q(test_delta):.15f}",
        )
    audit.check("delta=0 same Q but larger smallest squared branch", rho_e(0.0) / rho_delta > 50.0)
    audit.check("delta=3*pi/4 has massless branch edge", rho_e(3.0 * math.pi / 4.0) < 1e-28)
    audit.check(
        "signed and physical Koide Q differ when a branch is negative",
        abs(signed_koide_q(1.0) - physical_mass_koide_q(1.0)) > 0.01,
    )
    scale = 313.841126
    mass = scale * rho_delta
    scaled = 1.01 * scale * rho_delta
    audit.check("scale composition multiplies branch mass", abs(scaled / mass - 1.01) < 1e-14)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    branch_packet = read(BRANCH_PACKET)
    electron_mass_packet = read(ELECTRON_MASS_PACKET)
    static_target = read(STATIC_TARGET)
    koide_q_narrow = read(KOIDE_Q_NARROW)
    koide_cone_narrow = read(KOIDE_CONE_NARROW)
    koide_character_narrow = read(KOIDE_CHARACTER_NARROW)
    koide_sqrtm = read(KOIDE_SQRTM)
    koide_parent = read(KOIDE_PARENT)
    brannen_open_gate = read(BRANNEN_OPEN_GATE)
    minimal = flat(read(MINIMAL))
    scale_note = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    tier_a = read(TIER_A_REGISTRY)
    nodes = registry["nodes"]

    audit.check("goal packet references branch mass-map no-go", NOTE.name in goal and "KOIDE_BRANCH_MASS_MAP_RETAINED" in goal)
    audit.check("Koide firewall references branch mass-map no-go", NOTE.name in koide_firewall and "SQUARE_ROOT_MASS_READOUT_RETAINED" in koide_firewall)
    audit.check("branch mass-map packet references current-surface no-go", NOTE.name in branch_packet and "current surfaces do not supply `KOIDE_BRANCH_MASS_MAP_RETAINED`" in branch_packet)
    audit.check("electron mass packet references branch mass-map no-go", NOTE.name in electron_mass_packet and "KOIDE_BRANCH_MASS_MAP_RETAINED" in electron_mass_packet)
    audit.check("static target keeps branch mass map as upstream input", "KOIDE_BRANCH_MASS_MAP_RETAINED" in static_target and "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in static_target)
    q_flat = flat(koide_q_narrow)
    audit.check("narrow Q theorem refuses physical mass identification", "no physical-mass identification" in q_flat and "Does **not** identify the symbols `x_k` with `sqrt(m_k)`" in q_flat)
    audit.check("Koide cone theorem is abstract algebra only", "abstract positive 3-vectors" in koide_cone_narrow or "positive 3-vectors" in koide_cone_narrow)
    audit.check("Koide character bridge is pure character support", "pure `C_3` character" in koide_character_narrow or "C_3" in koide_character_narrow)
    audit.check("sqrtm amplitude note leaves charged-lepton parent open", "derive the positive parent operator `M`" in koide_sqrtm and "does not yet derive the charged-lepton masses" in koide_sqrtm)
    audit.check("Koide parent note keeps square-root readout open", "square-root readout identification is not retained yet" in koide_parent and "charged-lepton-specific parent `M` itself" in koide_parent)
    audit.check("Brannen open gate excludes phase and scale derivation", "does not derive the Brannen phase" in brannen_open_gate and "dimensionful mass scale" in brannen_open_gate)
    audit.check("minimal axioms keep downstream structure outside axiom content", "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration" in minimal)
    audit.check("scale primitive excludes dimensionless mass-map content", "zero dimensionless content" in scale_note and "mass ratio" in scale_note)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes values and normalization", "normalization rule" in realized and "or value is supplied" in realized)

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    for absent in [
        "koide_branch_mass_map_primitive",
        "square_root_mass_readout_primitive",
        "positive_chamber_sign_rule_primitive",
        "brannen_circulant_branch_form_primitive",
        "scale_parameter_composition_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", marker in note)

    explicit_non_claims = [
        "No derivation or ratification of `KOIDE_BRANCH_MASS_MAP_RETAINED`.",
        "No derivation or ratification of `BRANNEN_CIRCULANT_BRANCH_FORM_RETAINED`.",
        "No derivation or ratification of `SQUARE_ROOT_MASS_READOUT_RETAINED`.",
        "No derivation or ratification of `POSITIVE_CHAMBER_OR_SIGN_RULE_RETAINED`.",
        "No derivation or ratification of `SCALE_PARAMETER_COMPOSITION_RETAINED`.",
        "No derivation of `delta = 2/9`, `rho_e(delta)`, `a_l^2`, or a physical",
        "No use of observed lepton masses, observed `m_W`, fitted `delta`, fitted",
        "No derivation of physical electron mass, `alpha(0)`, static-source Rydberg",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives the Koide branch mass map",
        "Koide branch mass map is retained",
        "KOIDE_BRANCH_MASS_MAP_RETAINED is supplied",
        "square-root mass readout is retained",
        "positive chamber/sign rule is retained",
        "physical electron mass is retained",
        "hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
