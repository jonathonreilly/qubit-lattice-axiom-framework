#!/usr/bin/env python3
"""Verifier for the Koide K1 determinant-count ladder review packet."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PACKET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_DETERMINANT_COUNT_LADDER_REVIEW_PACKET_2026-07-05.md"
GOAL = DOCS / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"

K1_COUNT_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_TARGET_DISCRIMINATOR_2026-07-05.md"
K1_COUNT_DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
K1_COUNT_CURRENT = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SELECTOR_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
SELECTOR_DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SELECTOR_CURRENT = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
DETERMINANT_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_TARGET_DISCRIMINATOR_2026-07-05.md"
DETERMINANT_DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
DETERMINANT_CURRENT = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
OBJECT_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_FLUCTUATION_DETERMINANT_OBJECT_TARGET_DISCRIMINATOR_2026-07-05.md"
OBJECT_DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_FLUCTUATION_DETERMINANT_OBJECT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
OBJECT_CURRENT = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_FLUCTUATION_DETERMINANT_OBJECT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
FACTOR_COUNT_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COMPLEX_SLOT_FACTORING_AND_CHIRAL_COUNT_BATCH_TARGET_DISCRIMINATOR_2026-07-05.md"
FACTOR_COUNT_DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COMPLEX_SLOT_FACTORING_AND_CHIRAL_COUNT_BATCH_RATIFICATION_DECISION_PACKET_2026-07-05.md"
FACTOR_COUNT_CURRENT = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COMPLEX_SLOT_FACTORING_AND_CHIRAL_COUNT_BATCH_CURRENT_SURFACE_NO_GO_2026-07-05.md"
DOMAIN_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_READOUT_DETERMINANT_DOMAIN_TARGET_DISCRIMINATOR_2026-07-05.md"
DOMAIN_DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_READOUT_DETERMINANT_DOMAIN_RATIFICATION_DECISION_PACKET_2026-07-05.md"
DOMAIN_CURRENT = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_READOUT_DETERMINANT_DOMAIN_CURRENT_SURFACE_NO_GO_2026-07-05.md"
DISAMBIG_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_POSITIVE_READOUT_OBJECT_DISAMBIGUATION_TARGET_DISCRIMINATOR_2026-07-05.md"
DISAMBIG_DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_POSITIVE_READOUT_OBJECT_DISAMBIGUATION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
DISAMBIG_CURRENT = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_POSITIVE_READOUT_OBJECT_DISAMBIGUATION_CURRENT_SURFACE_NO_GO_2026-07-05.md"

PR5019 = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR4991 = DOCS / "ZERO_IMPORT_HYDROGEN_TIER_A_OWNER_RETIREMENT_PR4991_IMPACT_DISCRIMINATOR_2026-07-04.md"
PR5007 = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_PR5007_IMPACT_DISCRIMINATOR_2026-07-04.md"
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

DISAMBIGUATION_INPUTS = {
    "K1_OBJECT_DISAMBIGUATION_TEXT_LOCK",
    "C3_CIRCULANT_FORM_RETAINED",
    "BLOCK_VS_DIMENSION_FORK_REPROVEN",
    "NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT",
    "STAGGERED_DIRAC_REALIZATION_SURFACE_NAMED",
    "GENERATION_YUKAWA_FLUCTUATION_TARGET_NAMED",
    "KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED",
    "VECTOR_MODULUS_FAMILY_IDENTIFIED_AS_WRONG_OBJECT",
    "POSITIVE_KOIDE_OBJECT_SEPARATED_FROM_VECTOR_MODULUS",
    "NO_GENERIC_C3_STATIC_ALGEBRA_SUBSTITUTION",
    "NO_RECORD_OCCUPANCY_PREMISE_INPUT",
    "NO_K2_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
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

FACTORING_INPUTS = {
    "K1_COMPLEX_SLOT_FACTORING_TEXT_LOCK",
    "C3_CIRCULANT_FORM_RETAINED",
    "BLOCK_VS_DIMENSION_FORK_REPROVEN",
    "NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT",
    "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED",
    "GENERATION_FLUCTUATION_DETERMINANT_READOUT_CONTEXT_NAMED",
    "READOUT_FUNCTIONAL_DEFINED_ON_ACCEPTED_OBJECT",
    "READOUT_FUNCTIONAL_COMPLEX_LINEAR_ON_DOUBLET_QUOTIENT",
    "REAL_VECTOR_TRACE_NOT_USED_AS_FACTORING_PROOF",
    "NO_RECORD_OCCUPANCY_PREMISE_INPUT",
    "NO_K2_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

COUNT_INPUTS = {
    "K1_CHIRAL_COUNT_TEXT_LOCK",
    "C3_CIRCULANT_FORM_RETAINED",
    "BLOCK_VS_DIMENSION_FORK_REPROVEN",
    "NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT",
    "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED",
    "READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT",
    "STAGGERED_DIRAC_REALIZATION_SURFACE_NAMED",
    "CHIRAL_OR_HOLOMORPHIC_READOUT_SELECTED_ON_RETAINED_REALIZATION",
    "SINGLE_COMPLEX_DOUBLET_MODE_COUNT_COMPUTED",
    "VECTOR_REAL_TWO_SLOT_COUNT_NOT_USED_AS_PROOF",
    "NO_RECORD_OCCUPANCY_PREMISE_INPUT",
    "NO_K2_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

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

DOMAIN_TO_OBJECT = {"KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED"}
DISAMBIG_TO_OBJECT = {"POSITIVE_KOIDE_READOUT_OBJECT_DISAMBIGUATED_FROM_VECTOR_MODULUS"}
OBJECT_TO_DET = {"FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED"}
FACTORING_TO_DET = {"READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT"}
COUNT_TO_DET = {"CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION"}
DET_TO_SELECTOR = {"CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED"}
SELECTOR_TO_K1 = {
    "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED",
    "DIMENSION_BORN_DEFAULT_EXCLUSION",
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
    "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
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


def closes_disambiguation(inputs: set[str]) -> bool:
    return DISAMBIGUATION_INPUTS <= inputs


def closes_object(inputs: set[str]) -> bool:
    return OBJECT_INPUTS <= inputs


def closes_factoring(inputs: set[str]) -> bool:
    return FACTORING_INPUTS <= inputs


def closes_count(inputs: set[str]) -> bool:
    return COUNT_INPUTS <= inputs


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


def only_full_contract_closes(name: str, audit: Audit, inputs: set[str], predicate) -> None:
    accepted = [subset for subset in all_subsets(inputs) if predicate(subset)]
    audit.check(f"only full {name} contract subset closes target", accepted == [set(inputs)])


def one_input_removed_fails(name: str, audit: Audit, inputs: set[str], predicate) -> None:
    audit.check(f"full {name} contract closes target", predicate(set(inputs)))
    for missing in sorted(inputs):
        reduced = set(inputs)
        reduced.remove(missing)
        audit.check(f"{name} target fails without {missing}", not predicate(reduced))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        PACKET,
        GOAL,
        KOIDE_FIREWALL,
        K1_COUNT_TARGET,
        K1_COUNT_DECISION,
        K1_COUNT_CURRENT,
        SELECTOR_TARGET,
        SELECTOR_DECISION,
        SELECTOR_CURRENT,
        DETERMINANT_TARGET,
        DETERMINANT_DECISION,
        DETERMINANT_CURRENT,
        OBJECT_TARGET,
        OBJECT_DECISION,
        OBJECT_CURRENT,
        FACTOR_COUNT_TARGET,
        FACTOR_COUNT_DECISION,
        FACTOR_COUNT_CURRENT,
        DOMAIN_TARGET,
        DOMAIN_DECISION,
        DOMAIN_CURRENT,
        DISAMBIG_TARGET,
        DISAMBIG_DECISION,
        DISAMBIG_CURRENT,
        PR5019,
        PR4991,
        PR5007,
        PRIMITIVE_REGISTRY,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    packet = read(PACKET)
    packet_flat = flat(packet)

    section("Required packet content")
    required_phrases = [
        "Koide K1 Determinant-Count Ladder Review Packet",
        "grouped K1 determinant/count ladder review packet",
        "support-only / review compression only",
        "K1 determinant-count ladder review packet",
        "sibling inputs, not a single chain",
        "K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED",
        "K1_POSITIVE_KOIDE_READOUT_OBJECT_DISAMBIGUATION_RETAINED",
        "K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED",
        "K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED",
        "K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED",
        "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
        "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED",
        "K1_COUNTING_MEASURE_RETAINED",
        "KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED",
        "POSITIVE_KOIDE_READOUT_OBJECT_DISAMBIGUATED_FROM_VECTOR_MODULUS",
        "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED",
        "READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT",
        "CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION",
        "CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
        "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED",
        "DIMENSION_BORN_DEFAULT_EXCLUSION",
        "Open, merged, clean, or green PR metadata is not proof input",
        "The primitive registry was checked",
        "Registered primitive nodes are",
        "k1_determinant_count_ladder_primitive",
        "No-Go Discipline Gate",
        "broad K1 ladder closure claim fails",
        "review-compression artifact",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required packet phrase present: {phrase}", flat(phrase) in packet_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in packet)

    section("Contract closure checks")
    contract_checks = [
        ("domain", DOMAIN_INPUTS, closes_domain),
        ("positive-object disambiguation", DISAMBIGUATION_INPUTS, closes_disambiguation),
        ("determinant object", OBJECT_INPUTS, closes_object),
        ("complex-slot factorization", FACTORING_INPUTS, closes_factoring),
        ("chiral/holomorphic count", COUNT_INPUTS, closes_count),
        ("determinant theorem", DETERMINANT_INPUTS, closes_determinant),
        ("selector/default exclusion", SELECTOR_INPUTS, closes_selector),
        ("K1 counting measure", K1_INPUTS, closes_k1),
    ]
    for name, inputs, predicate in contract_checks:
        one_input_removed_fails(name, audit, inputs, predicate)
        only_full_contract_closes(name, audit, inputs, predicate)

    section("Dependency-boundary checks")
    audit.check("domain consequence alone does not close object", not closes_object(DOMAIN_TO_OBJECT))
    audit.check("positive-object consequence alone does not close object", not closes_object(DISAMBIG_TO_OBJECT))
    audit.check("object needs both domain and positive-object consequences", closes_object(OBJECT_INPUTS))
    for missing in sorted(DOMAIN_TO_OBJECT | DISAMBIG_TO_OBJECT):
        reduced = set(OBJECT_INPUTS)
        reduced.remove(missing)
        audit.check(f"object target fails without sibling consequence {missing}", not closes_object(reduced))

    audit.check("object consequence alone does not close determinant theorem", not closes_determinant(OBJECT_TO_DET))
    audit.check("factorization consequence alone does not close determinant theorem", not closes_determinant(FACTORING_TO_DET))
    audit.check("count consequence alone does not close determinant theorem", not closes_determinant(COUNT_TO_DET))
    for missing in sorted(OBJECT_TO_DET | FACTORING_TO_DET | COUNT_TO_DET):
        reduced = set(DETERMINANT_INPUTS)
        reduced.remove(missing)
        audit.check(f"determinant theorem fails without sibling consequence {missing}", not closes_determinant(reduced))

    audit.check("determinant theorem consequence alone does not close selector", not closes_selector(DET_TO_SELECTOR))
    selector_without_default = set(SELECTOR_INPUTS)
    selector_without_default.remove("REAL_VECTOR_TRACE_DEFAULT_EXCLUDED")
    audit.check("selector/default exclusion fails without real-vector default exclusion", not closes_selector(selector_without_default))
    audit.check("selector consequences alone do not close K1", not closes_k1(SELECTOR_TO_K1))
    for missing in sorted(SELECTOR_TO_K1):
        reduced = set(K1_INPUTS)
        reduced.remove(missing)
        audit.check(f"K1 target fails without selector output {missing}", not closes_k1(reduced))

    ladder_consequences = (
        DOMAIN_TO_OBJECT
        | DISAMBIG_TO_OBJECT
        | OBJECT_TO_DET
        | FACTORING_TO_DET
        | COUNT_TO_DET
        | DET_TO_SELECTOR
        | SELECTOR_TO_K1
    )
    audit.check("all ladder consequences alone do not close K1", not closes_k1(ladder_consequences))
    audit.check("K1 retained alone does not close electron mass", not closes_electron_mass({"K1_COUNTING_MEASURE_RETAINED"}))
    audit.check(
        "K1 plus K2 retained still does not close electron mass",
        not closes_electron_mass({"K1_COUNTING_MEASURE_RETAINED", "K2_R_ETA_EXACTNESS_RETAINED"}),
    )
    audit.check("K1 retained alone does not close hydrogen", not closes_hydrogen({"K1_COUNTING_MEASURE_RETAINED"}))
    audit.check("electron mass inputs without alpha/static source do not close hydrogen", not closes_hydrogen(ELECTRON_MASS_INPUTS))

    section("Authority-surface checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    for text_name, text in [("goal", goal), ("Koide firewall", firewall)]:
        text_flat = flat(text)
        for phrase in [
            "ZERO_IMPORT_HYDROGEN_KOIDE_K1_DETERMINANT_COUNT_LADDER_REVIEW_PACKET_2026-07-05.md",
            "K1 determinant-count ladder review packet",
            "review compression only",
            "sibling inputs, not a single chain",
        ]:
            audit.check(f"{text_name} references {phrase}", flat(phrase) in text_flat)

    source_surface = "\n".join(
        read(path)
        for path in [
            K1_COUNT_TARGET,
            SELECTOR_TARGET,
            DETERMINANT_TARGET,
            OBJECT_TARGET,
            FACTOR_COUNT_TARGET,
            DOMAIN_TARGET,
            DISAMBIG_TARGET,
        ]
    )
    source_surface_flat = flat(source_surface)
    for phrase in [
        "does not claim hydrogen is retained",
        "not full K1",
        "does not ratify K1",
        "do not supply the determinant object, the parent determinant theorem",
        "does not supply the readout-domain predicate",
    ]:
        audit.check(f"source K1 surfaces keep nonclosure visible: {phrase}", flat(phrase) in source_surface_flat)

    section("Primitive registry checks")
    registry = json.loads(read(PRIMITIVE_REGISTRY))
    canonical_ids = set(registry["canonical_ids"])
    audit.check("primitive registry canonical ids match expected set", canonical_ids == EXPECTED_PRIMITIVES)
    primitive_text = primitive_source_text(registry)
    for primitive in sorted(EXPECTED_PRIMITIVES):
        audit.check(f"primitive registry names {primitive}", primitive in primitive_text or primitive in read(PRIMITIVE_REGISTRY))

    forbidden_primitives = [
        "k1_determinant_count_ladder_primitive",
        "k1_readout_determinant_domain_primitive",
        "k1_positive_readout_object_primitive",
        "k1_fluctuation_determinant_object_primitive",
        "k1_complex_slot_factorization_primitive",
        "k1_chiral_count_primitive",
        "k1_determinant_theorem_primitive",
        "k1_selector_default_exclusion_primitive",
        "k1_counting_measure_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]
    registry_blob = read(PRIMITIVE_REGISTRY)
    for primitive in forbidden_primitives:
        audit.check(f"unapproved primitive absent from registry: {primitive}", primitive not in registry_blob)
        audit.check(f"unapproved primitive absent from approved source notes: {primitive}", primitive not in primitive_text)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation or ratification of `K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED`.",
        "No derivation or ratification of `K1_POSITIVE_KOIDE_READOUT_OBJECT_DISAMBIGUATION_RETAINED`.",
        "No derivation or ratification of `K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED`.",
        "No derivation or ratification of `K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED`.",
        "No derivation or ratification of `K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED`.",
        "No derivation or ratification of `K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED`.",
        "No derivation or ratification of `K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`.",
        "No derivation or ratification of `K1_COUNTING_MEASURE_RETAINED`.",
        "No derivation or ratification of K2, K3, K4, physical electron mass, alpha,",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden_overclaims = [
        "This packet ratifies `K1_COUNTING_MEASURE_RETAINED`",
        "This packet derives `K1_COUNTING_MEASURE_RETAINED`",
        "This packet derives retained hydrogen",
        "K1 ladder is closed",
        "physical electron mass is retained",
        "hydrogen is retained",
        "approved primitive supplies K1",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in packet)

    audit.summary()


if __name__ == "__main__":
    main()
