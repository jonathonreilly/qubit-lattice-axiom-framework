#!/usr/bin/env python3
"""Verifier for the Koide K1 chiral/holomorphic determinant decision packet."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
DETERMINANT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_TARGET_DISCRIMINATOR_2026-07-05.md"
DETERMINANT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SELECTOR_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
SELECTOR_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SELECTOR_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
K1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_TARGET_DISCRIMINATOR_2026-07-05.md"
K1_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
K1_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
COUNTING_SYNTHESIS = ROOT / "docs" / "CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md"
SUPERTRACE_OPEN = ROOT / "docs" / "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md"
FORK_MECHANISM = ROOT / "docs" / "KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md"
WZ_FUJIKAWA = ROOT / "docs" / "AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md"
STAGGERED_GATE = ROOT / "docs" / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
BEREZIN_SUBSUMPTION = ROOT / "docs" / "OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md"
KERNEL_COEFFICIENT = ROOT / "docs" / "KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"


DETERMINANT_INPUTS = {
    "K1_DETERMINANT_TEXT_LOCK",
    "C3_CIRCULANT_FORM_RETAINED",
    "BLOCK_VS_DIMENSION_FORK_REPROVEN",
    "NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT",
    "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED",
    "READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT",
    "CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION",
    "VECTOR_TRACE_DEFAULT_NOT_USED_AS_PROOF",
    "NO_RECORD_OCCUPANCY_PREMISE_INPUT",
    "NO_K2_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

DETERMINANT_CONSEQUENCE = {
    "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
    "CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
}

SELECTOR_INPUTS = {
    "K1_SELECTOR_TEXT_LOCK",
    "C3_CIRCULANT_FORM_RETAINED",
    "BLOCK_VS_DIMENSION_FORK_REPROVEN",
    "CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
    "REAL_VECTOR_TRACE_DEFAULT_EXCLUDED",
    "NO_RECORD_OCCUPANCY_PREMISE_INPUT",
    "NO_K2_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

K1_INPUTS = {
    "K1_COUNTING_TEXT_LOCK",
    "C3_CIRCULANT_FORM_RETAINED",
    "BLOCK_VS_DIMENSION_FORK_REPROVEN",
    "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED",
    "DIMENSION_BORN_DEFAULT_EXCLUSION",
    "NO_K2_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

ELECTRON_MASS_INPUTS = {
    "K1_COUNTING_MEASURE_RETAINED",
    "K2_R_ETA_EXACTNESS_RETAINED",
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


def all_subsets(items: set[str]) -> list[set[str]]:
    ordered = sorted(items)
    subsets: list[set[str]] = []
    for size in range(len(ordered) + 1):
        for combo in combinations(ordered, size):
            subsets.append(set(combo))
    return subsets


def closes_determinant(inputs: set[str]) -> bool:
    return DETERMINANT_INPUTS <= inputs


def closes_selector(inputs: set[str]) -> bool:
    return SELECTOR_INPUTS <= inputs


def closes_k1(inputs: set[str]) -> bool:
    return K1_INPUTS <= inputs


def closes_electron_mass(inputs: set[str]) -> bool:
    return ELECTRON_MASS_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def q_from_r(r: Fraction) -> Fraction:
    return Fraction(1, 3) + Fraction(2, 3) * r


def primitive_source_text(registry: dict[str, object]) -> str:
    nodes = registry["nodes"]
    assert isinstance(nodes, dict)
    chunks: list[str] = []
    for node in nodes.values():
        assert isinstance(node, dict)
        current_path = node["current_path"]
        assert isinstance(current_path, str)
        chunks.append(read(ROOT / current_path))
    return "\n".join(chunks)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        DETERMINANT_TARGET,
        DETERMINANT_NO_GO,
        SELECTOR_TARGET,
        SELECTOR_DECISION,
        SELECTOR_NO_GO,
        K1_TARGET,
        K1_NO_GO,
        K1_DECISION,
        GOAL,
        KOIDE_FIREWALL,
        COUNTING_SYNTHESIS,
        SUPERTRACE_OPEN,
        FORK_MECHANISM,
        WZ_FUJIKAWA,
        STAGGERED_GATE,
        BEREZIN_SUBSUMPTION,
        KERNEL_COEFFICIENT,
        PRIMITIVE_REGISTRY,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required note content")
    required_phrases = [
        "Koide K1 Chiral/Holomorphic Determinant Ratification Decision Packet",
        "decision packet / Koide K1 determinant subhandoff",
        "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
        "CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
        "the Koide K1 chiral/holomorphic determinant theorem for the doublet count",
        "K1_DETERMINANT_TEXT_LOCK",
        "C3_CIRCULANT_FORM_RETAINED",
        "BLOCK_VS_DIMENSION_FORK_REPROVEN",
        "NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT",
        "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED",
        "READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT",
        "CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION",
        "VECTOR_TRACE_DEFAULT_NOT_USED_AS_PROOF",
        "NO_RECORD_OCCUPANCY_PREMISE_INPUT",
        "NO_K2_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those fourteen contract inputs",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md",
        "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md",
        "KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md",
        "The primitive registry was checked",
        "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED is packaged as a",
        "fourteen-input ratification decision contract",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    audit.check("block/orbit count gives Q=2/3", q_from_r(Fraction(1, 2)) == Fraction(2, 3))
    audit.check("dimension count gives Q=1", q_from_r(Fraction(1, 1)) == Fraction(1, 1))
    full_inputs = set(DETERMINANT_INPUTS)
    audit.check("full determinant decision contract accepts handoff", closes_determinant(full_inputs))
    for missing in sorted(DETERMINANT_INPUTS):
        reduced = set(DETERMINANT_INPUTS)
        reduced.remove(missing)
        audit.check(f"determinant decision fails without {missing}", not closes_determinant(reduced))
    accepted_subsets = [subset for subset in all_subsets(DETERMINANT_INPUTS) if closes_determinant(subset)]
    audit.check("only full tested determinant contract subset closes decision", accepted_subsets == [full_inputs])
    audit.check("determinant consequence contains theorem predicate", "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED" in DETERMINANT_CONSEQUENCE)
    audit.check("determinant consequence supplies parent determinant input", "CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED" in DETERMINANT_CONSEQUENCE)
    audit.check("determinant consequence alone does not close selector/default-exclusion", not closes_selector(set(DETERMINANT_CONSEQUENCE)))
    audit.check("determinant consequence alone does not close K1", not closes_k1(set(DETERMINANT_CONSEQUENCE)))
    audit.check("determinant consequence alone does not close electron mass", not closes_electron_mass(set(DETERMINANT_CONSEQUENCE)))
    audit.check("determinant consequence alone does not close hydrogen", not closes_hydrogen(set(DETERMINANT_CONSEQUENCE)))

    section("Authority and primitive boundary checks")
    determinant_target = read(DETERMINANT_TARGET)
    determinant_no_go = read(DETERMINANT_NO_GO)
    selector_target = read(SELECTOR_TARGET)
    selector_decision = read(SELECTOR_DECISION)
    selector_no_go = read(SELECTOR_NO_GO)
    k1_target = read(K1_TARGET)
    k1_no_go = read(K1_NO_GO)
    k1_decision = read(K1_DECISION)
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    counting = read(COUNTING_SYNTHESIS)
    supertrace = read(SUPERTRACE_OPEN)
    fork = read(FORK_MECHANISM)
    wz = read(WZ_FUJIKAWA)
    staggered = read(STAGGERED_GATE)
    berezin = read(BEREZIN_SUBSUMPTION)
    kernel = read(KERNEL_COEFFICIENT)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = primitive_source_text(primitive_registry)

    for label, container in [
        ("determinant target", determinant_target),
        ("determinant current no-go", determinant_no_go),
        ("selector target", selector_target),
        ("selector decision", selector_decision),
        ("selector current no-go", selector_no_go),
        ("K1 target", k1_target),
        ("K1 current no-go", k1_no_go),
        ("K1 decision", k1_decision),
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
    ]:
        audit.check(
            f"{label} references determinant decision lane",
            NOTE.name in container and "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED" in container,
        )
    audit.check("determinant target references decision", NOTE.name in determinant_target)
    audit.check("determinant no-go references decision", NOTE.name in determinant_no_go)
    audit.check("selector target still requires real-vector default exclusion", "REAL_VECTOR_TRACE_DEFAULT_EXCLUDED" in selector_target)
    audit.check(
        "counting synthesis keeps J_cs measure-neutral",
        "A static `J` is measure-neutral" in counting
        and "`J_cs` exists but cannot, by itself, select the value" in counting,
    )
    audit.check("supertrace route remains open", "open_gate" in supertrace and "remains gated" in supertrace)
    audit.check("fork mechanism leaves selector open", "does not adopt the holomorphic polarization" in fork)
    audit.check("WZ/Fujikawa is not Koide determinant closure", "does not retire any external ABJ import" in wz)
    audit.check("staggered gate keeps bounded scope", "not a positive (unbounded) theorem" in staggered)
    audit.check("Berezin subsumption remains conditional", "conditional subsumption" in berezin)
    audit.check("kernel coefficient note keeps cell open", "does not select a cell" in kernel)

    expected_nodes = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    audit.check("primitive registry has expected approved nodes", expected_nodes <= set(primitive_nodes))
    for forbidden_node in [
        "k1_chiral_holomorphic_determinant_primitive",
        "chiral_holomorphic_determinant_theorem_primitive",
        "k1_selector_default_exclusion_primitive",
        "k1_counting_measure_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)
    for phrase in [
        "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
        "CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
        "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED",
        "K1_COUNTING_MEASURE_RETAINED",
        "Q = 2/3",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
    ]:
        audit.check(f"primitive texts do not supply {phrase}", phrase not in primitive_text)

    section("Non-claim boundaries")
    explicit_nonclaims = [
        "`K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED`.",
        "`CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED`.",
        "No derivation or ratification of `REAL_VECTOR_TRACE_DEFAULT_EXCLUDED`.",
        "No derivation or ratification of `K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`.",
        "No derivation or ratification of `K1_COUNTING_MEASURE_RETAINED`.",
        "No derivation of `r = 1/2` or `Q = 2/3`.",
        "No derivation of physical electron mass",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This packet ratifies K1",
        "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED is supplied",
        "CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED is supplied",
        "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED is supplied",
        "K1_COUNTING_MEASURE_RETAINED is supplied",
        "r = 1/2 is derived",
        "Q = 2/3 is derived",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This packet claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
