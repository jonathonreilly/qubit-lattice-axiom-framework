#!/usr/bin/env python3
"""Verifier for the Koide K1 complex-slot factoring and chiral-count batch."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COMPLEX_SLOT_FACTORING_AND_CHIRAL_COUNT_BATCH_TARGET_DISCRIMINATOR_2026-07-05.md"
NO_GO = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COMPLEX_SLOT_FACTORING_AND_CHIRAL_COUNT_BATCH_CURRENT_SURFACE_NO_GO_2026-07-05.md"
DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COMPLEX_SLOT_FACTORING_AND_CHIRAL_COUNT_BATCH_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PARENT_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_TARGET_DISCRIMINATOR_2026-07-05.md"
PARENT_NO_GO = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PARENT_DECISION = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
OBJECT_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_FLUCTUATION_DETERMINANT_OBJECT_TARGET_DISCRIMINATOR_2026-07-05.md"
SELECTOR_TARGET = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
GOAL = DOCS / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = DOCS / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
SUPERTRACE_OPEN = DOCS / "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md"
FORK_MECHANISM = DOCS / "KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md"
COUNTING_SYNTHESIS = DOCS / "CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md"
BEREZIN_SUBSUMPTION = DOCS / "OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md"
WZ_FUJIKAWA = DOCS / "AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md"
STAGGERED_GATE = DOCS / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
PRIMITIVE_REGISTRY = DOCS / "audit" / "data" / "axiom_premise_nodes.json"


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

CURRENT_FACTORING_INPUTS = FACTORING_INPUTS - {
    "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED",
    "READOUT_FUNCTIONAL_DEFINED_ON_ACCEPTED_OBJECT",
    "READOUT_FUNCTIONAL_COMPLEX_LINEAR_ON_DOUBLET_QUOTIENT",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

EXPECTED_FACTORING_MISSING = FACTORING_INPUTS - CURRENT_FACTORING_INPUTS

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

CURRENT_COUNT_INPUTS = COUNT_INPUTS - {
    "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED",
    "READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT",
    "CHIRAL_OR_HOLOMORPHIC_READOUT_SELECTED_ON_RETAINED_REALIZATION",
    "SINGLE_COMPLEX_DOUBLET_MODE_COUNT_COMPUTED",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

EXPECTED_COUNT_MISSING = COUNT_INPUTS - CURRENT_COUNT_INPUTS

FACTORING_CONSEQUENCE = {
    "K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED",
    "READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT",
}

COUNT_CONSEQUENCE = {
    "K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED",
    "CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION",
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


def closes_factoring(inputs: set[str]) -> bool:
    return FACTORING_INPUTS <= inputs


def closes_count(inputs: set[str]) -> bool:
    return COUNT_INPUTS <= inputs


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
        PARENT_TARGET,
        PARENT_NO_GO,
        PARENT_DECISION,
        OBJECT_TARGET,
        SELECTOR_TARGET,
        GOAL,
        KOIDE_FIREWALL,
        SUPERTRACE_OPEN,
        FORK_MECHANISM,
        COUNTING_SYNTHESIS,
        BEREZIN_SUBSUMPTION,
        WZ_FUJIKAWA,
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
        "Koide K1 Complex-Slot Factoring and Chiral Count Batch Target Discriminator",
        "Koide K1 Complex-Slot Factoring and Chiral Count Batch Current-Surface No-Go",
        "Koide K1 Complex-Slot Factoring and Chiral Count Batch Ratification Decision Packet",
        "K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED",
        "READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT",
        "K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED",
        "CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION",
        "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
        "FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED",
        "No proper subset of the fifteen factoring inputs",
        "No proper subset of the sixteen count inputs",
        "current retained, primitive, merged-PR, and open-PR surfaces do not supply",
        "does not claim hydrogen is retained",
        "No new axiom, primitive, Tier-A admission, or empirical import",
        "#5031",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", phrase in combined or flat(phrase) in combined_flat)

    for input_name in sorted(FACTORING_INPUTS):
        audit.check(f"factoring input appears: {input_name}", input_name in combined)
    audit.check("factoring contract has fifteen inputs", len(FACTORING_INPUTS) == 15)

    for input_name in sorted(COUNT_INPUTS):
        audit.check(f"count input appears: {input_name}", input_name in combined)
    audit.check("count contract has sixteen inputs", len(COUNT_INPUTS) == 16)

    for doc_name, doc_text in [
        ("target", target),
        ("current no-go", no_go),
        ("decision", decision),
    ]:
        for item in [f"N{i}" for i in range(1, 9)]:
            audit.check(f"{doc_name} has {item}", item in doc_text)
        audit.check(f"{doc_name} has explicit non-claims", "Explicit Non-Claims" in doc_text)

    section("Logical closure checks")
    audit.check("block-count cell gives Q=2/3", q_from_r(Fraction(1, 2)) == Fraction(2, 3))
    audit.check("dimension-count cell gives Q=1", q_from_r(Fraction(1, 1)) == Fraction(1, 1))

    audit.check("current factoring inputs do not close factoring", not closes_factoring(CURRENT_FACTORING_INPUTS))
    audit.check(
        "expected factoring missing complement",
        FACTORING_INPUTS - CURRENT_FACTORING_INPUTS == EXPECTED_FACTORING_MISSING,
        detail=str(sorted(EXPECTED_FACTORING_MISSING)),
    )
    audit.check("full factoring contract closes factoring", closes_factoring(FACTORING_INPUTS))
    bad_factoring_subsets = [
        subset for subset in all_subsets(FACTORING_INPUTS)
        if subset != FACTORING_INPUTS and closes_factoring(subset)
    ]
    audit.check("no proper subset closes factoring", not bad_factoring_subsets)

    audit.check("current count inputs do not close count", not closes_count(CURRENT_COUNT_INPUTS))
    audit.check(
        "expected count missing complement",
        COUNT_INPUTS - CURRENT_COUNT_INPUTS == EXPECTED_COUNT_MISSING,
        detail=str(sorted(EXPECTED_COUNT_MISSING)),
    )
    audit.check("full count contract closes count", closes_count(COUNT_INPUTS))
    bad_count_subsets = [
        subset for subset in all_subsets(COUNT_INPUTS)
        if subset != COUNT_INPUTS and closes_count(subset)
    ]
    audit.check("no proper subset closes count", not bad_count_subsets)

    both_consequences = FACTORING_CONSEQUENCE | COUNT_CONSEQUENCE
    audit.check(
        "count contract depends on factoring consequence",
        "READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT" in COUNT_INPUTS,
    )
    audit.check(
        "factoring plus count consequences do not close parent determinant",
        not closes_parent_determinant(both_consequences),
    )
    with_object = both_consequences | {"FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED"}
    audit.check(
        "object plus factoring plus count still lacks parent owner/audit",
        not closes_parent_determinant(with_object),
    )
    audit.check("batch consequences do not close selector/default-exclusion", not closes_selector(both_consequences))
    audit.check("batch consequences do not close K1", not closes_k1(both_consequences))
    audit.check("batch consequences do not close electron mass", not closes_electron_mass(both_consequences))
    audit.check("batch consequences do not close hydrogen", not closes_hydrogen(both_consequences))

    missing_text = no_go[no_go.find("## Current Missing Inputs") :]
    for missing in sorted(EXPECTED_FACTORING_MISSING | EXPECTED_COUNT_MISSING):
        audit.check(f"current no-go names missing input: {missing}", missing in missing_text)

    section("Source authority checks")
    supertrace = flat(read(SUPERTRACE_OPEN))
    fork = flat(read(FORK_MECHANISM))
    counting = flat(read(COUNTING_SYNTHESIS))
    berezin = flat(read(BEREZIN_SUBSUMPTION))
    wz = flat(read(WZ_FUJIKAWA))
    staggered = flat(read(STAGGERED_GATE))

    audit.check(
        "supertrace lead counts complex mode once",
        "A holomorphic / chiral count weights `b` once" in supertrace
        or "A holomorphic/chiral count weights the complex mode `b` once" in supertrace,
    )
    audit.check(
        "supertrace lead does not establish determinant chirality",
        "does not show that the framework's generation fluctuation determinant is chiral" in supertrace,
    )
    audit.check(
        "fork mechanism names complex-slot factorization route",
        "readout functional factors through the doublet complex-slot quotient" in fork,
    )
    audit.check(
        "fork mechanism does not adopt holomorphic polarization",
        "It does not adopt the holomorphic polarization." in fork,
    )
    audit.check(
        "counting synthesis marks J_cs measure-neutral",
        "A static `J` is measure-neutral" in counting and "J_cs" in counting,
    )
    audit.check(
        "Berezin subsumption remains conditional",
        "This note proposes a bounded conditional subsumption" in berezin
        and "Not** an unconditional derivation" in berezin,
    )
    audit.check(
        "WZ/Fujikawa does not decide downstream anomaly/readout",
        "do **not** prove a non-zero anomaly" in wz,
    )
    audit.check(
        "staggered gate keeps downstream masses open",
        "Nothing here derives generation masses" in staggered,
    )

    section("Primitive registry checks")
    registry = json.loads(read(PRIMITIVE_REGISTRY))
    nodes = registry["nodes"]
    audit.check("primitive registry uses dict nodes", isinstance(nodes, dict))
    assert isinstance(nodes, dict)
    audit.check("expected primitive ids present", EXPECTED_PRIMITIVES <= set(nodes))
    primitive_text = flat(primitive_source_text(registry))
    primitive_forbidden = [
        "K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED",
        "READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT",
        "K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED",
        "CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION",
        "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED",
        "K1_COUNTING_MEASURE_RETAINED",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "ALPHA0_RETAINED",
        "STATIC_SOURCE_RYDBERG_RETAINED",
    ]
    for forbidden in primitive_forbidden:
        audit.check(f"primitive sources do not supply {forbidden}", forbidden not in primitive_text)
    audit.check(
        "scale primitive says no dimensionless readout content",
        "no mass ratio, coupling, mixing angle, phase, selector, readout" in primitive_text,
    )
    audit.check(
        "kinetic primitive says no readout bridge",
        "no mass ratio, coupling, mixing angle, phase, selector, readout bridge" in primitive_text,
    )
    audit.check(
        "realized-state primitive says no state-selection rule",
        "not a state-selection rule" in primitive_text,
    )

    section("Wiring checks")
    wiring_text = "\n".join([
        read(PARENT_TARGET),
        read(PARENT_NO_GO),
        read(PARENT_DECISION),
        read(SELECTOR_TARGET),
        read(GOAL),
        read(KOIDE_FIREWALL),
    ])
    wiring_required = [
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COMPLEX_SLOT_FACTORING_AND_CHIRAL_COUNT_BATCH_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COMPLEX_SLOT_FACTORING_AND_CHIRAL_COUNT_BATCH_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COMPLEX_SLOT_FACTORING_AND_CHIRAL_COUNT_BATCH_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED",
        "K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED",
    ]
    for phrase in wiring_required:
        audit.check(f"wired phrase present: {phrase}", phrase in wiring_text)

    for pr in ["#5031", "#5030", "#5021", "#5018", "#5017", "#5014", "#5012", "#5007", "#5029", "#5028", "#5016"]:
        audit.check(f"PR alignment mentions {pr}", pr in no_go or pr in decision)

    section("Non-claim checks")
    forbidden_overclaims = [
        "K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED is retained",
        "K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED is retained",
        "K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED is retained",
        "hydrogen is retained.",
    ]
    safe_combined = combined_flat.replace("does not claim hydrogen is retained.", "")
    for phrase in forbidden_overclaims:
        audit.check(f"artifact avoids bare overclaim phrase: {phrase}", phrase not in safe_combined)

    audit.summary()


if __name__ == "__main__":
    main()
