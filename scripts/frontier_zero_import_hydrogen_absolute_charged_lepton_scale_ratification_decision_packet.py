#!/usr/bin/env python3
"""Verifier for the absolute charged-lepton scale decision packet.

This runner checks that the K4 scale-assembly decision contract is explicit
and remains separate from native Koide bridge closure, physical species
bridge, alpha(0), and hydrogen closure.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE_TRIAGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
WEAK_FRONT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
WEAK_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SOURCE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_P2 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md"
P1_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P2_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P3_KOIDE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P4_DIRECT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_PLACEMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
PRECISION_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
LEPTON_MW_OPEN_GATE = ROOT / "docs" / "LEPTON_MASS_SCALE_MW_OVER_256_EMPIRICAL_OPEN_GATE_NOTE_2026-05-26.md"
LEPTON_YUKAWA_256 = ROOT / "docs" / "LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md"
BRIDGE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SPECIES_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ALPHA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


K4_DECISION_INPUTS = {
    "K4_SCALE_TEXT_LOCK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "WEAK_FRONT_BASE_RETAINED",
    "EXACT_SOURCE_SINGLETON_RETAINED",
    "A3_PRECISION_PLACEMENT_RETAINED",
    "NO_SOURCE_A3_DOUBLE_COUNT",
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


def closes_k4_decision(inputs: set[str]) -> bool:
    return K4_DECISION_INPUTS <= inputs


def closes_physical_electron(inputs: set[str]) -> bool:
    return PHYSICAL_ELECTRON_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        ROUTE_TRIAGE,
        KOIDE_FIREWALL,
        WEAK_FRONT_DECISION,
        WEAK_FRONT_NO_GO,
        SOURCE_DECISION,
        EXACT_SOURCE_NO_GO,
        A3_DECISION,
        A3_NO_GO,
        A3_P2,
        P1_SOURCE_NO_GO,
        P2_FRONT_NO_GO,
        P3_KOIDE_NO_GO,
        P4_DIRECT_NO_GO,
        A3_PLACEMENT,
        PRECISION_FIREWALL,
        LEPTON_SCALE,
        LEPTON_MW_OPEN_GATE,
        LEPTON_YUKAWA_256,
        BRIDGE_DECISION,
        SPECIES_DECISION,
        ALPHA_TARGET,
        STATIC_TARGET,
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
        "Absolute Charged-Lepton Scale Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify the absolute charged-lepton scale",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "the absolute charged-lepton scale assembly for the hydrogen electron-mass lane",
        "y_scale = g_2 * (1/sqrt(2)) * S_l",
        "S_l = 1/256",
        "K4_SCALE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "WEAK_FRONT_BASE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "unsupplied upstream input",
        "WEAK_FRONT_BASE_TEXT_LOCK",
        "SU2_WEAK_COUPLING_CONTEXT_RETAINED",
        "CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED",
        "UNCORRECTED_FRONT_SCOPE_LOCK",
        "NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT",
        "NO_A3_OR_THRESHOLD_MATCHING_INPUT",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "retained exact source-side",
        "unsupplied upstream input",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "A3 placement as an unsupplied upstream input",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "P1_SOURCE_READOUT_CORRECTION_RETAINED",
        "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "CHARGED_LEPTON_FRONT_MATCHING_RETAINED",
        "MATCHING_THEOREM_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED",
        "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED",
        "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED",
        "NO_SOURCE_A3_DOUBLE_COUNT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those ten contract inputs",
        "PHYSICAL_ELECTRON_READOUT_RETAINED",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "ALPHA0_RETAINED",
        "STATIC_SOURCE_RYDBERG_RETAINED",
        "`#5013` theta native positive-class adjudication | `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `SUCCESS`",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "decision-ready ratification contract",
        "broad K4-retention claim fails; narrowed absolute",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(K4_DECISION_INPUTS)
    audit.check("full K4 contract accepts decision", closes_k4_decision(full_inputs))
    for missing in sorted(K4_DECISION_INPUTS):
        reduced = set(K4_DECISION_INPUTS)
        reduced.remove(missing)
        audit.check(f"K4 decision fails without {missing}", not closes_k4_decision(reduced))
    accepted_subsets = [subset for subset in all_subsets(K4_DECISION_INPUTS) if closes_k4_decision(subset)]
    audit.check("only full tested contract subset closes K4 decision", accepted_subsets == [full_inputs])

    k4_consequence = {"ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED"}
    audit.check("K4 alone does not close physical electron", not closes_physical_electron(k4_consequence))
    audit.check("full physical electron predicate closes electron", closes_physical_electron(set(PHYSICAL_ELECTRON_INPUTS)))
    for missing in sorted(PHYSICAL_ELECTRON_INPUTS):
        reduced = set(PHYSICAL_ELECTRON_INPUTS)
        reduced.remove(missing)
        audit.check(f"physical electron predicate fails without {missing}", not closes_physical_electron(reduced))
    audit.check("physical electron alone does not close hydrogen", not closes_hydrogen(set(PHYSICAL_ELECTRON_INPUTS)))
    audit.check("full hydrogen predicate model closes hydrogen", closes_hydrogen(set(HYDROGEN_INPUTS)))

    section("Finite scale witness checks")
    dim_m2 = 4
    full_cell_count = dim_m2**4
    audit.check("M2 complex dimension handle gives 4^4=256", full_cell_count == 256)
    audit.check("uniform source singleton is 1/256", Fraction(1, full_cell_count) == Fraction(1, 256))
    audit.check("front identity sqrt(2)/512 = (1/sqrt(2))/256 after multiplying by sqrt(2)", Fraction(2, 512) == Fraction(1, 256))

    getcontext().prec = 40
    n_a3 = Decimal("256.08243522600384")
    c_a3 = Decimal(256) / n_a3
    audit.check("A3 correction target C_A3 is near 0.999678091", abs(c_a3 - Decimal("0.9996780910571587")) < Decimal("1e-16"), str(c_a3))
    s0 = Decimal(1) / Decimal(256)
    direct = Decimal(1) / n_a3
    audit.check("C_A3 times exact singleton equals direct noninteger singleton", abs(c_a3 * s0 - direct) < Decimal("1e-40"), str(c_a3 * s0))

    f0 = Decimal("0.461616")  # arbitrary nonzero front placeholder; not comparator data.
    r0 = Decimal("0.001628")  # arbitrary nonzero readout placeholder; not proof input.
    p1 = f0 * (c_a3 * s0) * r0
    p2 = (c_a3 * f0) * s0 * r0
    p3 = f0 * s0 * (c_a3 * r0)
    p4 = f0 * direct * r0
    audit.check("A3 placements are product-equivalent only after supplied common correction", max(abs(p1 - p2), abs(p1 - p3), abs(p1 - p4)) < Decimal("1e-35"))
    audit.check("removing correction changes product", f0 * s0 * r0 != p1)

    section("Authority boundary checks")
    goal = read(GOAL)
    route_triage = read(ROUTE_TRIAGE)
    koide_firewall = read(KOIDE_FIREWALL)
    weak_front_decision = read(WEAK_FRONT_DECISION)
    weak_front_no_go = read(WEAK_FRONT_NO_GO)
    source_decision = read(SOURCE_DECISION)
    exact_source_no_go = read(EXACT_SOURCE_NO_GO)
    a3_decision = read(A3_DECISION)
    a3_no_go = read(A3_NO_GO)
    a3_p2 = read(A3_P2)
    p1_source_no_go = read(P1_SOURCE_NO_GO)
    p3_koide_no_go = read(P3_KOIDE_NO_GO)
    p4_direct_no_go = read(P4_DIRECT_NO_GO)
    a3_placement = read(A3_PLACEMENT)
    precision_firewall = read(PRECISION_FIREWALL)
    lepton_scale = read(LEPTON_SCALE)
    lepton_open_gate = read(LEPTON_MW_OPEN_GATE)
    lepton_yukawa = read(LEPTON_YUKAWA_256)
    bridge_decision = read(BRIDGE_DECISION)
    species_decision = read(SPECIES_DECISION)
    alpha_target = read(ALPHA_TARGET)
    static_target = read(STATIC_TARGET)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    tier_a = read(TIER_A_REGISTRY)
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("route triage", route_triage),
        ("Koide firewall", koide_firewall),
    ]:
        audit.check(f"{container_name} references K4 decision packet", NOTE.name in container)

    audit.check(
        "weak-front packet remains base only",
        "WEAK_FRONT_BASE_RETAINED" in weak_front_decision and "does not derive the A3 correction" in weak_front_decision,
    )
    audit.check("K4 packet references weak-front no-go", WEAK_FRONT_NO_GO.name in note and "unsupplied upstream input" in note)
    audit.check("weak-front no-go keeps base unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in weak_front_no_go and "WEAK_FRONT_BASE_RETAINED" in weak_front_no_go)
    audit.check("lepton-scale probe carries front factorization", "y_scale := a_lepton" in lepton_scale and "g_2" in lepton_scale and "1/256" in lepton_scale)
    audit.check("source decision remains source-side only", "This is source-side only" in source_decision and "does not derive" in source_decision)
    audit.check("K4 packet references exact-source no-go", EXACT_SOURCE_NO_GO.name in note and "EXACT_SOURCE_SINGLETON_RETAINED" in note)
    audit.check("exact-source no-go keeps source singleton unsupplied", "EXACT_SOURCE_SINGLETON_RETAINED" in exact_source_no_go and "current retained, primitive, and open-PR surfaces do not supply" in exact_source_no_go)
    audit.check("A3 decision remains placement only", "A3_PRECISION_PLACEMENT_RETAINED" in a3_decision and "does not by itself derive `C_A3`" in a3_decision)
    audit.check("K4 packet references A3 no-go", A3_NO_GO.name in note and "A3 placement as an unsupplied upstream input" in note_flat)
    audit.check("A3 no-go keeps placement unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in a3_no_go and "A3_PRECISION_PLACEMENT_RETAINED" in a3_no_go)
    audit.check("A3 P1 source-readout correction remains open", "P1_SOURCE_READOUT_CORRECTION_RETAINED" in p1_source_no_go and "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED" in p1_source_no_go)
    audit.check("A3 P2 target names weak-front matching", "F_phys = C_A3 * g_2 * (1/sqrt(2))" in a3_p2 and "does not derive" in a3_p2)
    audit.check("A3 P3 Koide/electron readout correction remains open", "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED" in p3_koide_no_go and "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED" in p3_koide_no_go)
    audit.check("A3 P4 direct noninteger divisor remains open", "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED" in p4_direct_no_go and "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED" in p4_direct_no_go)
    audit.check("A3 placement discriminator separates P1-P5", all(token in a3_placement for token in ["P1 source-readout", "P2 front-factor", "P3 Koide", "P4 direct", "P5 empirical"]))
    audit.check("precision firewall quantifies 256.082435 residual", "256.082435" in precision_firewall and "C_A3" in precision_firewall)
    audit.check("mW open gate remains empirical open gate", "open_gate" in lepton_open_gate and "empirical" in lepton_open_gate.lower())
    audit.check(
        "lepton Yukawa structural probe keeps noninteger residual visible",
        "256.08" in lepton_yukawa and "non-integer" in lepton_yukawa.lower(),
    )
    audit.check("bridge decision keeps K4 downstream", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in bridge_decision)
    audit.check("species decision keeps K4 downstream", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in species_decision)
    audit.check("alpha target remains downstream", "No derivation of `alpha(0)`" in alpha_target and "R-Lep" in alpha_target)
    audit.check("static target remains downstream", "STATIC_SOURCE_RYDBERG" in static_target or "static-source Rydberg" in static_target)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    audit.check("minimal axioms keep downstream gates outside axiom content", "remain outside axiom content" in minimal and "AC_phi_lambda" in minimal)
    audit.check("scale primitive excludes dimensionless physics", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes state selection and values", "state-selection rule" in realized and "or value is supplied" in realized)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in nodes)
    audit.check("no K4 primitive registered", "absolute_charged_lepton_scale_primitive" not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5013` theta native positive-class adjudication | `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `SUCCESS`",
        "`#5011` eta twisted walk family runner | `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of the absolute charged-lepton scale.",
        "No derivation or ratification of the weak-front base.",
        "No derivation or ratification of exact source-side `S_l = 1/256`.",
        "No derivation or ratification of A3 precision placement.",
        "No derivation of `C_A3 = 0.999678091...` or `N_A3 = 256.082435...`.",
        "No derivation or ratification of Z1/Z2/Z3 native bridge clauses.",
        "No derivation or ratification of the physical electron species bridge.",
        "No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.",
        "No use of observed lepton masses, observed `m_W`, fitted `a_l`, fitted",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies the absolute charged-lepton scale",
        "absolute charged-lepton scale is retained",
        "weak-front base is retained",
        "S_l = 1/256 is retained",
        "A3 precision placement is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
