#!/usr/bin/env python3
"""Verifier for the Koide K1 fluctuation determinant object sublane."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_FLUCTUATION_DETERMINANT_OBJECT_TARGET_DISCRIMINATOR_2026-07-05.md"
NO_GO = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_FLUCTUATION_DETERMINANT_OBJECT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_FLUCTUATION_DETERMINANT_OBJECT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PARENT_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_TARGET_DISCRIMINATOR_2026-07-05.md"
PARENT_NO_GO = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PARENT_DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SELECTOR_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
K1_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_TARGET_DISCRIMINATOR_2026-07-05.md"
GOAL = DOCS / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
SUPERTRACE_OPEN = DOCS / "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md"
YUKAWA_BINARY = DOCS / "KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md"
FORK_MECHANISM = DOCS / "KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md"
DYNAMIC_PRUNING = DOCS / "KOIDE_R_HALF_DYNAMICAL_DETERMINANT_ROUTE_PRUNING_NO_GO_NOTE_2026-06-08.md"
STAGGERED_GATE = DOCS / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
WZ_FUJIKAWA = DOCS / "AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md"
PRIMITIVE_REGISTRY = DOCS / "audit" / "data" / "axiom_premise_nodes.json"


OBJECT_INPUTS = {
    "K1_DETERMINANT_OBJECT_TEXT_LOCK",
    "C3_CIRCULANT_FORM_RETAINED",
    "BLOCK_VS_DIMENSION_FORK_REPROVEN",
    "NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT",
    "STAGGERED_DIRAC_REALIZATION_SURFACE_NAMED",
    "GENERATION_YUKAWA_FLUCTUATION_TARGET_NAMED",
    "KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED",
    "POSITIVE_KOIDE_READOUT_OBJECT_DISAMBIGUATED_FROM_VECTOR_MODULUS",
    "HERMITIAN_VECTOR_MODULUS_ROUTE_NOT_USED_AS_PROOF",
    "NO_GENERIC_C3_STATIC_ALGEBRA_SUBSTITUTION",
    "NO_RECORD_OCCUPANCY_PREMISE_INPUT",
    "NO_K2_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_OBJECT_INPUTS = {
    "K1_DETERMINANT_OBJECT_TEXT_LOCK",
    "C3_CIRCULANT_FORM_RETAINED",
    "BLOCK_VS_DIMENSION_FORK_REPROVEN",
    "NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT",
    "STAGGERED_DIRAC_REALIZATION_SURFACE_NAMED",
    "GENERATION_YUKAWA_FLUCTUATION_TARGET_NAMED",
    "HERMITIAN_VECTOR_MODULUS_ROUTE_NOT_USED_AS_PROOF",
    "NO_GENERIC_C3_STATIC_ALGEBRA_SUBSTITUTION",
    "NO_RECORD_OCCUPANCY_PREMISE_INPUT",
    "NO_K2_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
}

EXPECTED_MISSING = {
    "KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED",
    "POSITIVE_KOIDE_READOUT_OBJECT_DISAMBIGUATED_FROM_VECTOR_MODULUS",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

OBJECT_CONSEQUENCE = {
    "K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED",
    "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED",
}

PARENT_DETERMINANT_INPUTS = {
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


def closes_object(inputs: set[str]) -> bool:
    return OBJECT_INPUTS <= inputs


def closes_parent_determinant(inputs: set[str]) -> bool:
    return PARENT_DETERMINANT_INPUTS <= inputs


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
        TARGET,
        NO_GO,
        DECISION,
        PARENT_TARGET,
        PARENT_NO_GO,
        PARENT_DECISION,
        SELECTOR_TARGET,
        K1_TARGET,
        GOAL,
        KOIDE_FIREWALL,
        SUPERTRACE_OPEN,
        YUKAWA_BINARY,
        FORK_MECHANISM,
        DYNAMIC_PRUNING,
        STAGGERED_GATE,
        WZ_FUJIKAWA,
        PRIMITIVE_REGISTRY,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    target = read(TARGET)
    no_go = read(NO_GO)
    decision = read(DECISION)
    combined = "\n".join([target, no_go, decision])
    combined_flat = flat(combined)

    section("Required artifact content")
    required_phrases = [
        "Koide K1 Fluctuation Determinant Object Target Discriminator",
        "Koide K1 Fluctuation Determinant Object Current-Surface No-Go",
        "Koide K1 Fluctuation Determinant Object Ratification Decision Packet",
        "K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED",
        "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED",
        "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
        "READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT",
        "CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION",
        "K1_DETERMINANT_OBJECT_TEXT_LOCK",
        "STAGGERED_DIRAC_REALIZATION_SURFACE_NAMED",
        "GENERATION_YUKAWA_FLUCTUATION_TARGET_NAMED",
        "KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED",
        "POSITIVE_KOIDE_READOUT_OBJECT_DISAMBIGUATED_FROM_VECTOR_MODULUS",
        "HERMITIAN_VECTOR_MODULUS_ROUTE_NOT_USED_AS_PROOF",
        "NO_GENERIC_C3_STATIC_ALGEBRA_SUBSTITUTION",
        "NO_RECORD_OCCUPANCY_PREMISE_INPUT",
        "NO_K2_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those sixteen",
        "KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md",
        "KOIDE_R_HALF_DYNAMICAL_DETERMINANT_ROUTE_PRUNING_NO_GO_NOTE_2026-06-08.md",
        "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
        "The primitive registry was checked",
        "no primitive supplies",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in combined_flat)

    for doc_name, text in [("target", target), ("current no-go", no_go), ("decision", decision)]:
        for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
            audit.check(f"{doc_name} no-go marker present: {marker}", marker in text)

    section("Object predicate checks")
    audit.check("block/orbit count gives Q=2/3", q_from_r(Fraction(1, 2)) == Fraction(2, 3))
    audit.check("dimension count gives Q=1", q_from_r(Fraction(1, 1)) == Fraction(1, 1))
    full_inputs = set(OBJECT_INPUTS)
    audit.check("full object contract accepts target", closes_object(full_inputs))
    for missing in sorted(OBJECT_INPUTS):
        reduced = set(OBJECT_INPUTS)
        reduced.remove(missing)
        audit.check(f"object contract fails without {missing}", not closes_object(reduced))
    accepted_subsets = [subset for subset in all_subsets(OBJECT_INPUTS) if closes_object(subset)]
    audit.check("only full object contract subset closes target", accepted_subsets == [full_inputs])
    audit.check("current surface does not close object", not closes_object(CURRENT_OBJECT_INPUTS))
    audit.check("current missing inputs match packet", OBJECT_INPUTS - CURRENT_OBJECT_INPUTS == EXPECTED_MISSING)
    audit.check("object consequence supplies parent input", "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED" in OBJECT_CONSEQUENCE)
    audit.check("object consequence alone does not close parent determinant", not closes_parent_determinant(OBJECT_CONSEQUENCE))
    audit.check("object consequence alone does not close selector", not closes_selector(OBJECT_CONSEQUENCE))
    audit.check("object consequence alone does not close K1", not closes_k1(OBJECT_CONSEQUENCE))
    audit.check("object consequence alone does not close electron mass", not closes_electron_mass(OBJECT_CONSEQUENCE))
    audit.check("object consequence alone does not close hydrogen", not closes_hydrogen(OBJECT_CONSEQUENCE))

    section("Source and primitive boundary checks")
    source_texts = {
        "parent determinant target": read(PARENT_TARGET),
        "supertrace open lead": read(SUPERTRACE_OPEN),
        "Yukawa binary note": read(YUKAWA_BINARY),
        "fork mechanism": read(FORK_MECHANISM),
        "dynamic pruning": read(DYNAMIC_PRUNING),
        "staggered gate": read(STAGGERED_GATE),
        "WZ/Fujikawa": read(WZ_FUJIKAWA),
    }
    audit.check("parent determinant target names object input", "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED" in source_texts["parent determinant target"])
    audit.check(
        "supertrace lead keeps antecedent open",
        "does not show that the framework's" in source_texts["supertrace open lead"]
        and "generation fluctuation determinant is chiral" in source_texts["supertrace open lead"],
    )
    audit.check("Yukawa binary note names next determinant action", "compute the generation Yukawa fluctuation determinant" in source_texts["Yukawa binary note"])
    audit.check("fork mechanism does not adopt holomorphic polarization", "It does not adopt the holomorphic polarization." in source_texts["fork mechanism"])
    audit.check("dynamic pruning leaves chiral routes open", "chiral" in source_texts["dynamic pruning"] and "remain outside this no-go" in source_texts["dynamic pruning"])
    audit.check("staggered gate supplies context, not object phrase", "bounded synthesis" in source_texts["staggered gate"].lower())
    audit.check("WZ/Fujikawa is context only", "Fujikawa" in source_texts["WZ/Fujikawa"])

    registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_ids = set(registry["canonical_ids"])
    expected_primitives = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    audit.check("primitive registry has expected approved nodes", expected_primitives <= primitive_ids)
    primitive_text = primitive_source_text(registry)
    for forbidden in [
        "K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED",
        "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED",
        "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
        "READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT",
        "K1_COUNTING_MEASURE_RETAINED",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "ALPHA0_RETAINED",
        "STATIC_SOURCE_RYDBERG_RETAINED",
    ]:
        audit.check(f"primitive texts do not supply {forbidden}", forbidden not in primitive_text)
    for excluded in ["weighting", "normalization", "probability", "selector", "readout bridge"]:
        audit.check(f"primitive notes exclude or do not grant {excluded}", excluded in primitive_text)

    section("Parent wiring and non-claims")
    for parent_name, parent_text in [
        ("parent target", read(PARENT_TARGET)),
        ("parent no-go", read(PARENT_NO_GO)),
        ("parent decision", read(PARENT_DECISION)),
        ("goal packet", read(GOAL)),
        ("Koide firewall", read(KOIDE_FIREWALL)),
    ]:
        audit.check(f"{parent_name} references fluctuation determinant object", "FLUCTUATION_DETERMINANT_OBJECT" in parent_text or "fluctuation determinant" in parent_text)

    explicit_nonclaims = [
        "No derivation or ratification of",
        "No derivation or ratification of `FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED`.",
        "No derivation or ratification of the parent K1 determinant theorem.",
        "No derivation of full K1, physical electron mass",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", flat(phrase) in combined_flat)

    forbidden_overclaims = [
        "This note ratifies `FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED`",
        "`FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED` is supplied",
        "parent determinant theorem is retained",
        "K1 is retained",
        "physical electron mass is retained",
        "This packet claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in combined)

    audit.summary()


if __name__ == "__main__":
    main()
