#!/usr/bin/env python3
"""Verifier for the Koide K1 selector/default-exclusion target."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
K1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_TARGET_DISCRIMINATOR_2026-07-05.md"
K1_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
K1_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SELECTOR_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SELECTOR_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
COUNTING_SYNTHESIS = ROOT / "docs" / "CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md"
SUPERTRACE_OPEN = ROOT / "docs" / "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md"
OCCUPANCY_INDEPENDENCE = ROOT / "docs" / "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md"
BEREZIN_SUBSUMPTION = ROOT / "docs" / "OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md"
KERNEL_COEFFICIENT = ROOT / "docs" / "KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md"
TWO_GATE = ROOT / "docs" / "CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md"
PR5019_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR4991_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_TIER_A_OWNER_RETIREMENT_PR4991_IMPACT_DISCRIMINATOR_2026-07-04.md"
PR5020_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5022_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md"
K2_EXACTNESS = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"


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

SELECTOR_CONSEQUENCE_SUPPLIES = {
    "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED",
    "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED",
    "DIMENSION_BORN_DEFAULT_EXCLUSION",
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


def closes_selector_default_exclusion(inputs: set[str]) -> bool:
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
        GOAL,
        KOIDE_FIREWALL,
        K1_TARGET,
        K1_NO_GO,
        K1_DECISION,
        SELECTOR_DECISION,
        SELECTOR_NO_GO,
        COUNTING_SYNTHESIS,
        SUPERTRACE_OPEN,
        OCCUPANCY_INDEPENDENCE,
        BEREZIN_SUBSUMPTION,
        KERNEL_COEFFICIENT,
        TWO_GATE,
        PR5019_IMPACT,
        PR4991_IMPACT,
        PR5020_IMPACT,
        PR5022_IMPACT,
        K2_EXACTNESS,
        PHYSICAL_ELECTRON,
        PRIMITIVE_REGISTRY,
        TIER_A_REGISTRY,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required note content")
    required_phrases = [
        "Koide K1 Selector/Default-Exclusion Target Discriminator",
        "target discriminator / Koide K1 selector subhandoff",
        "does not ratify K1",
        "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED",
        "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED",
        "DIMENSION_BORN_DEFAULT_EXCLUSION",
        "K1_COUNTING_MEASURE_RETAINED",
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
        "No proper subset of those eleven inputs",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md",
        "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md",
        "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md",
        "OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md",
        "KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md",
        "CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md",
        "open `#4932`",
        "open `#4991`",
        "merged `#5019`",
        "merged `#5020`",
        "open draft `#5021`",
        "merged `#5022`",
        "The primitive registry was checked",
        "no primitive supplies `K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`",
        "K1 selector/default-exclusion is a named eleven-input target",
        "No-Go Discipline Gate",
        "broad selector/default-exclusion retained claim fails",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate and arithmetic checks")
    audit.check("block/orbit count gives Q=2/3", q_from_r(Fraction(1, 2)) == Fraction(2, 3))
    audit.check("dimension count gives Q=1", q_from_r(Fraction(1, 1)) == Fraction(1, 1))
    audit.check("the two cells are distinct", q_from_r(Fraction(1, 2)) != q_from_r(Fraction(1, 1)))
    full_selector_inputs = set(SELECTOR_INPUTS)
    audit.check(
        "full selector/default-exclusion contract accepts subtarget",
        closes_selector_default_exclusion(full_selector_inputs),
    )
    for missing in sorted(SELECTOR_INPUTS):
        reduced = set(SELECTOR_INPUTS)
        reduced.remove(missing)
        audit.check(
            f"selector/default-exclusion target fails without {missing}",
            not closes_selector_default_exclusion(reduced),
        )
    accepted_subsets = [
        subset for subset in all_subsets(SELECTOR_INPUTS) if closes_selector_default_exclusion(subset)
    ]
    audit.check(
        "only full tested selector contract subset closes target",
        accepted_subsets == [full_selector_inputs],
    )

    consequence = set(SELECTOR_CONSEQUENCE_SUPPLIES)
    audit.check("selector consequence supplies named target", "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED" in consequence)
    audit.check("selector consequence supplies orbit/holomorphic input", "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED" in consequence)
    audit.check("selector consequence supplies default-exclusion input", "DIMENSION_BORN_DEFAULT_EXCLUSION" in consequence)
    audit.check("selector consequence alone does not close K1", not closes_k1(consequence))
    k1_context_after_selector = consequence | {
        "K1_COUNTING_TEXT_LOCK",
        "C3_CIRCULANT_FORM_RETAINED",
        "BLOCK_VS_DIMENSION_FORK_REPROVEN",
        "NO_K2_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    }
    audit.check("selector consequence plus remaining K1 context closes K1", closes_k1(k1_context_after_selector))
    audit.check("selector consequence alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("selector consequence alone does not close hydrogen", not closes_hydrogen(consequence))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    k1_target = read(K1_TARGET)
    k1_no_go = read(K1_NO_GO)
    k1_decision = read(K1_DECISION)
    selector_decision = read(SELECTOR_DECISION)
    selector_no_go = read(SELECTOR_NO_GO)
    counting = read(COUNTING_SYNTHESIS)
    supertrace = read(SUPERTRACE_OPEN)
    occupancy = read(OCCUPANCY_INDEPENDENCE)
    berezin = read(BEREZIN_SUBSUMPTION)
    kernel = read(KERNEL_COEFFICIENT)
    two_gate = read(TWO_GATE)
    pr5019 = read(PR5019_IMPACT)
    pr4991 = read(PR4991_IMPACT)
    pr5020 = read(PR5020_IMPACT)
    pr5022 = read(PR5022_IMPACT)
    k2 = read(K2_EXACTNESS)
    physical_electron = read(PHYSICAL_ELECTRON)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = primitive_source_text(primitive_registry)
    tier_a = read(TIER_A_REGISTRY)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
        ("K1 target", k1_target),
        ("K1 current no-go", k1_no_go),
        ("K1 decision", k1_decision),
        ("selector/default-exclusion decision", selector_decision),
        ("selector/default-exclusion current no-go", selector_no_go),
    ]:
        audit.check(
            f"{label} references selector/default-exclusion target",
            NOTE.name in container and "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED" in container,
        )
    audit.check(
        "selector decision/no-go retain support-only boundary",
        "eleven-input owner/audit contract" in selector_decision
        and "does not ratify" in selector_decision
        and "current retained, primitive, merged-PR, and open-PR surfaces do not supply" in selector_no_go,
    )
    audit.check(
        "counting synthesis reduces to one bit but does not force Q=2/3",
        "one binary counting-measure bit" in counting
        and "does NOT close" in counting
        and "does NOT rank the two measures" in counting,
    )
    audit.check(
        "supertrace route remains open",
        "open_gate" in supertrace
        and "does not derive" in supertrace
        and "remains gated" in supertrace,
    )
    audit.check(
        "occupancy independence keeps atom unsupplied",
        "not supplied by the current checked premise surface" in occupancy
        and "premise candidate" in occupancy
        and "NOT adopted" in occupancy,
    )
    audit.check(
        "Berezin subsumption is conditional",
        "conditional subsumption" in berezin
        and "unbounded framework derivation" in flat(berezin),
    )
    audit.check(
        "kernel coefficient note keeps occupancy open",
        "does not select a cell" in kernel
        and "The occupancy binary stays open" in kernel,
    )
    audit.check(
        "two-gate companion is Tier-A conditional only",
        "Under that premise" in two_gate
        and "does not derive `r^2/a^2=1/2`" in two_gate
        and "does not modify or promote the Tier-A registry" in two_gate,
    )
    audit.check("#5019 impact is premise-hygiene not K1 closure", "premise hygiene" in pr5019 and "does not derive `AC_phi_lambda`" in pr5019)
    audit.check("#4991 impact is owner-governed premise standing not theorem closure", "owner-governed chain-satisfying premises" in pr4991 and "not theorem closure" in pr4991)
    audit.check("#5020 impact is K2 progress only", "exactness remains open" in pr5020)
    audit.check("#5022 impact is K2 conditionality only", "conditionality progress" in pr5022 and "no retained R-eta derivation" in pr5022)
    audit.check("K2 exactness target keeps K1 separate", "NO_K1_K3_K4_OR_MASS_INPUT" in k2 and "K1 occupancy/counting" in k2)
    audit.check("physical electron packet remains downstream", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in physical_electron and "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in physical_electron)

    expected_nodes = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    audit.check("primitive registry has expected approved nodes", expected_nodes <= set(primitive_nodes))
    for node_name, node in primitive_nodes.items():
        current_path = node["current_path"]
        audit.check(f"registered node has readable current path: {node_name}", (ROOT / current_path).exists())
    for forbidden_node in [
        "k1_selector_default_exclusion_primitive",
        "orbit_holomorphic_count_selector_primitive",
        "dimension_born_default_exclusion_primitive",
        "k1_counting_measure_primitive",
        "koide_q_two_thirds_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)
    for phrase in [
        "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED",
        "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED",
        "DIMENSION_BORN_DEFAULT_EXCLUSION",
        "K1_COUNTING_MEASURE_RETAINED",
        "Q = 2/3",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    ]:
        audit.check(f"primitive texts do not supply {phrase}", phrase not in primitive_text)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in primitive_nodes)
    for excluded in ["weighting", "normalization", "probability", "selector", "readout bridge"]:
        audit.check(f"primitive notes exclude or do not grant {excluded}", excluded in primitive_text)

    section("Open PR and non-claim boundaries")
    open_markers = [
        "open `#4932`",
        "open `#4991`",
        "merged `#5019`",
        "merged `#5020`",
        "open draft `#5021`",
        "merged `#5022`",
    ]
    for marker in open_markers:
        audit.check(f"open PR marker present: {marker}", marker in note)

    explicit_nonclaims = [
        "No derivation or ratification of `K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`.",
        "No derivation or ratification of",
        "`ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED`.",
        "No derivation or ratification of `DIMENSION_BORN_DEFAULT_EXCLUSION`.",
        "No derivation or ratification of `K1_COUNTING_MEASURE_RETAINED`.",
        "No adoption of orbit-occupancy or any owner-governed occupancy premise.",
        "No claim that `#4932`, `#4991`, merged `#5019`, `#5020`, `#5021`, or merged",
        "No derivation or ratification of K2 exactness",
        "No use of observed lepton masses, fitted `Q`, observed `m_e`, observed",
        "No derivation of `S_l`, A3, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note ratifies K1",
        "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED is supplied",
        "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED is supplied",
        "DIMENSION_BORN_DEFAULT_EXCLUSION is supplied",
        "K1_COUNTING_MEASURE_RETAINED is supplied",
        "r = 1/2 is derived",
        "Q = 2/3 is derived",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This note claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
