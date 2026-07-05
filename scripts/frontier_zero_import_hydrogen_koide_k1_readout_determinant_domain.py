#!/usr/bin/env python3
"""Verifier for the Koide K1 readout determinant domain sublane."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_READOUT_DETERMINANT_DOMAIN_TARGET_DISCRIMINATOR_2026-07-05.md"
NO_GO = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_READOUT_DETERMINANT_DOMAIN_CURRENT_SURFACE_NO_GO_2026-07-05.md"
DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_READOUT_DETERMINANT_DOMAIN_RATIFICATION_DECISION_PACKET_2026-07-05.md"
OBJECT_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_FLUCTUATION_DETERMINANT_OBJECT_TARGET_DISCRIMINATOR_2026-07-05.md"
OBJECT_NO_GO = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_FLUCTUATION_DETERMINANT_OBJECT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
OBJECT_DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_FLUCTUATION_DETERMINANT_OBJECT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PARENT_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_TARGET_DISCRIMINATOR_2026-07-05.md"
SELECTOR_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
K1_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_TARGET_DISCRIMINATOR_2026-07-05.md"
GOAL = DOCS / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
SUPERTRACE_OPEN = DOCS / "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md"
YUKAWA_BINARY = DOCS / "KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md"
FORK_MECHANISM = DOCS / "KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md"
DYNAMIC_PRUNING = DOCS / "KOIDE_R_HALF_DYNAMICAL_DETERMINANT_ROUTE_PRUNING_NO_GO_NOTE_2026-06-08.md"
STAGGERED_GATE = DOCS / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
PRIMITIVE_REGISTRY = DOCS / "audit" / "data" / "axiom_premise_nodes.json"


DOMAIN_INPUTS = {
    "K1_READOUT_DOMAIN_TEXT_LOCK",
    "C3_CIRCULANT_FORM_RETAINED",
    "BLOCK_VS_DIMENSION_FORK_REPROVEN",
    "NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT",
    "STAGGERED_DIRAC_REALIZATION_SURFACE_NAMED",
    "GENERATION_YUKAWA_FLUCTUATION_TARGET_NAMED",
    "READOUT_DOMAIN_IS_KOIDE_GENERATION_DETERMINANT",
    "EFFECTIVE_POTENTIAL_VECTOR_TRACE_NOT_USED_AS_DOMAIN",
    "DYNAMIC_VECTOR_MODULUS_PRUNING_RESPECTED",
    "NO_GENERIC_C3_STATIC_ALGEBRA_SUBSTITUTION",
    "NO_RECORD_OCCUPANCY_PREMISE_INPUT",
    "NO_K2_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_DOMAIN_INPUTS = DOMAIN_INPUTS - {
    "READOUT_DOMAIN_IS_KOIDE_GENERATION_DETERMINANT",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

EXPECTED_DOMAIN_MISSING = {
    "READOUT_DOMAIN_IS_KOIDE_GENERATION_DETERMINANT",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

DOMAIN_CONSEQUENCE = {
    "K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED",
    "KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED",
}

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

EXPECTED_PRIMITIVES = {
    "minimal_axioms",
    "scale_reference_primitive",
    "kinetic_isotropy_primitive",
    "realized_state_primitive",
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


def closes_domain(inputs: set[str]) -> bool:
    return DOMAIN_INPUTS <= inputs


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


def primitive_source_text(registry: dict[str, object]) -> str:
    nodes = registry["nodes"]
    assert isinstance(nodes, dict)
    chunks: list[str] = []
    for key in sorted(EXPECTED_PRIMITIVES):
        node = nodes[key]
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
        OBJECT_TARGET,
        OBJECT_NO_GO,
        OBJECT_DECISION,
        PARENT_TARGET,
        SELECTOR_TARGET,
        K1_TARGET,
        GOAL,
        KOIDE_FIREWALL,
        SUPERTRACE_OPEN,
        YUKAWA_BINARY,
        FORK_MECHANISM,
        DYNAMIC_PRUNING,
        STAGGERED_GATE,
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
        "Koide K1 Readout Determinant Domain Target Discriminator",
        "Koide K1 Readout Determinant Domain Current-Surface No-Go",
        "Koide K1 Readout Determinant Domain Ratification Decision Packet",
        "K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED",
        "KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED",
        "K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED",
        "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED",
        "READOUT_DOMAIN_IS_KOIDE_GENERATION_DETERMINANT",
        "EFFECTIVE_POTENTIAL_VECTOR_TRACE_NOT_USED_AS_DOMAIN",
        "DYNAMIC_VECTOR_MODULUS_PRUNING_RESPECTED",
        "No proper subset of those sixteen",
        "plain effective potential/vector trace",
        "current retained, primitive, merged-PR, and open-PR surfaces do not supply",
        "does not derive the physical electron mass",
        "does not claim hydrogen is retained",
        "No new axiom, primitive, Tier-A admission, or empirical import",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", phrase in combined)

    for input_name in sorted(DOMAIN_INPUTS):
        audit.check(f"domain contract input appears: {input_name}", input_name in combined)
    audit.check("domain contract has sixteen inputs", len(DOMAIN_INPUTS) == 16)

    for doc_name, doc_text in [
        ("target", target),
        ("current no-go", no_go),
        ("decision", decision),
    ]:
        for item in [f"N{i}" for i in range(1, 9)]:
            audit.check(f"{doc_name} has {item}", item in doc_text)
        audit.check(
            f"{doc_name} excludes downstream hydrogen overclaim",
            "hydrogen" in doc_text and "No derivation" in doc_text,
        )

    section("Current-surface and logical-closure checks")
    audit.check("current domain inputs do not close domain", not closes_domain(CURRENT_DOMAIN_INPUTS))
    audit.check(
        "expected missing domain inputs match current complement",
        DOMAIN_INPUTS - CURRENT_DOMAIN_INPUTS == EXPECTED_DOMAIN_MISSING,
        detail=str(sorted(DOMAIN_INPUTS - CURRENT_DOMAIN_INPUTS)),
    )
    audit.check("full domain inputs close domain", closes_domain(DOMAIN_INPUTS))

    improper_domain_closures = [
        subset for subset in all_subsets(DOMAIN_INPUTS) if subset != DOMAIN_INPUTS and closes_domain(subset)
    ]
    audit.check("no proper subset closes domain", not improper_domain_closures)

    object_with_domain = CURRENT_OBJECT_INPUTS | {"KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED"}
    audit.check("accepted domain alone does not close object", not closes_object(object_with_domain))
    audit.check(
        "accepted domain alone does not close parent determinant",
        not closes_parent_determinant(DOMAIN_CONSEQUENCE),
    )
    audit.check("accepted domain alone does not close selector", not closes_selector(DOMAIN_CONSEQUENCE))
    audit.check("accepted domain alone does not close K1", not closes_k1(DOMAIN_CONSEQUENCE))
    audit.check("accepted domain alone does not close electron mass", not closes_electron_mass(DOMAIN_CONSEQUENCE))
    audit.check("accepted domain alone does not close hydrogen", not closes_hydrogen(DOMAIN_CONSEQUENCE))

    missing_text = no_go[no_go.find("## Current Missing Inputs") :]
    for missing in sorted(EXPECTED_DOMAIN_MISSING):
        audit.check(f"current no-go names missing input: {missing}", missing in missing_text)

    section("Source authority checks")
    supertrace = read(SUPERTRACE_OPEN)
    yukawa = read(YUKAWA_BINARY)
    fork = read(FORK_MECHANISM)
    pruning = read(DYNAMIC_PRUNING)
    staggered = read(STAGGERED_GATE)
    supertrace_flat = flat(supertrace)
    yukawa_flat = flat(yukawa)
    fork_flat = flat(fork)
    pruning_flat = flat(pruning)
    staggered_flat = flat(staggered)

    audit.check(
        "supertrace note keeps antecedent open",
        "does not show that the framework's generation fluctuation determinant is chiral" in supertrace_flat,
    )
    audit.check(
        "supertrace note marks plain effective potential as vector trace",
        "plain effective potential is still the vector trace" in supertrace_flat,
    )
    audit.check(
        "Yukawa binary note names computation target",
        "compute the generation Yukawa fluctuation determinant" in yukawa_flat,
    )
    audit.check(
        "fork mechanism does not adopt holomorphic polarization",
        "It does not adopt the holomorphic polarization." in fork_flat,
    )
    audit.check(
        "dynamic pruning note keeps statement narrow",
        "The supported statement is narrow" in pruning_flat,
    )
    audit.check(
        "dynamic pruning note leaves live domain alternatives outside no-go",
        "remain outside this no-go" in pruning_flat,
    )
    audit.check(
        "staggered gate is realization context, not Koide closure",
        "bounded synthesis" in staggered_flat and "staggered-Dirac realization" in staggered_flat,
    )

    section("Primitive registry checks")
    registry = json.loads(read(PRIMITIVE_REGISTRY))
    nodes = registry["nodes"]
    audit.check("primitive registry uses dict nodes", isinstance(nodes, dict))
    assert isinstance(nodes, dict)
    audit.check("expected primitive ids present", EXPECTED_PRIMITIVES <= set(nodes))
    primitive_text = primitive_source_text(registry)
    primitive_flat = flat(primitive_text)
    primitive_forbidden = [
        "K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED",
        "KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED",
        "K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED",
        "K1_COUNTING_MEASURE_RETAINED",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "ALPHA0_RETAINED",
        "STATIC_SOURCE_RYDBERG_RETAINED",
    ]
    for forbidden in primitive_forbidden:
        audit.check(f"primitive sources do not supply {forbidden}", forbidden not in primitive_flat)
    audit.check("scale primitive says no dimensionless readout content", "no mass ratio, coupling, mixing angle, phase, selector, readout" in primitive_flat)
    audit.check("kinetic primitive says no readout bridge", "no mass ratio, coupling, mixing angle, phase, selector, readout bridge" in primitive_flat)
    audit.check("realized-state primitive says no state-selection rule", "not a state-selection rule" in primitive_flat)

    section("Wiring checks")
    object_target = read(OBJECT_TARGET)
    object_no_go = read(OBJECT_NO_GO)
    object_decision = read(OBJECT_DECISION)
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    wiring_text = "\n".join([object_target, object_no_go, object_decision, goal, firewall])
    wiring_required = [
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_READOUT_DETERMINANT_DOMAIN_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_READOUT_DETERMINANT_DOMAIN_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_READOUT_DETERMINANT_DOMAIN_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED",
        "KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED",
        "plain effective-potential vector trace",
        "vector/modulus determinant routes",
    ]
    for phrase in wiring_required:
        audit.check(f"wired phrase present: {phrase}", phrase in wiring_text)

    for pr in ["#5030", "#5021", "#5018", "#5017", "#5014", "#5012", "#5007", "#5029", "#5016"]:
        audit.check(f"PR alignment mentions {pr}", pr in no_go or pr in decision)

    section("Non-claim checks")
    forbidden_overclaims = [
        "K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED is retained",
        "KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED is retained",
        "K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED is retained",
        "hydrogen is retained.",
    ]
    for phrase in forbidden_overclaims:
        audit.check(
            f"artifact avoids bare overclaim phrase: {phrase}",
            phrase not in combined.replace("does not claim hydrogen is retained.", ""),
        )
    audit.check(
        "domain consequence listed without object consequence",
        "That consequence does not supply the positive determinant object" in target,
    )
    audit.check(
        "decision consequence excludes object and hydrogen",
        "That consequence is partial support only" in decision
        and "K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED" in decision
        and "STATIC_SOURCE_RYDBERG_RETAINED" in decision,
    )

    audit.summary()


if __name__ == "__main__":
    main()
