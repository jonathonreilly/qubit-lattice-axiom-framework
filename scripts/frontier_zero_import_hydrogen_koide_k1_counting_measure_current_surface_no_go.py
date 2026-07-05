#!/usr/bin/env python3
"""Verifier for the Koide K1 counting-measure current-surface no-go."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
K1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_TARGET_DISCRIMINATOR_2026-07-05.md"
K1_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
K1_SELECTOR_DEFAULT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
K1_SELECTOR_DEFAULT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
K1_SELECTOR_DEFAULT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
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

CURRENT_SURFACE_INPUTS = {
    "K1_COUNTING_TEXT_LOCK",
    "C3_CIRCULANT_FORM_RETAINED",
    "BLOCK_VS_DIMENSION_FORK_REPROVEN",
    "NO_K2_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
}

EXPECTED_MISSING = {
    "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED",
    "DIMENSION_BORN_DEFAULT_EXCLUSION",
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
    "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
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
        K1_DECISION,
        K1_SELECTOR_DEFAULT,
        K1_SELECTOR_DEFAULT_DECISION,
        K1_SELECTOR_DEFAULT_NO_GO,
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
        "Koide K1 Counting-Measure Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not ratify K1",
        "K1_COUNTING_MEASURE_RETAINED",
        "current retained, primitive, merged-PR, and open-PR surfaces do not supply",
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
        "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED",
        "DIMENSION_BORN_DEFAULT_EXCLUSION",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED",
        "two missing K1 inputs",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "eleven-input owner/audit contract",
        "current retained, primitive, merged-PR, and open-PR surfaces do not supply `K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`",
        "ten-input owner/audit decision packet",
        "not accepted on the current surface",
        "CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md",
        "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md",
        "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md",
        "OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md",
        "KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md",
        "CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md",
        "`#4932` AC measure binary axiom shortcut no-go",
        "`#4991` owner-governed Tier-A retirement",
        "merged `#5019` Koide `AC_phi_lambda` axiom-surface rebase",
        "merged `#5020` Koide R-eta value-face PR",
        "open draft `#5021` primitive-retirement review",
        "merged `#5022` delta-eta audit repair",
        "The primitive registry was checked",
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
        "no registered primitive supplies `K1_COUNTING_MEASURE_RETAINED`",
        "no primitive retirement and no registry edit",
        "Open PR Alignment",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | merged",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | merged",
        "`#5022` delta-eta chain R-eta supplied-premise audit repair | merged, audit success",
        "clean/green status is not a proof input",
        "No-Go Discipline Gate",
        "broad K1 no-go fails; narrowed current-surface non-supply",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("K1 arithmetic and predicate checks")
    audit.check("block/orbit count gives Q=2/3", q_from_r(Fraction(1, 2)) == Fraction(2, 3))
    audit.check("dimension count gives Q=1", q_from_r(Fraction(1, 1)) == Fraction(1, 1))
    audit.check("the two cells are distinct", q_from_r(Fraction(1, 2)) != q_from_r(Fraction(1, 1)))
    full_inputs = set(K1_INPUTS)
    audit.check("full K1 counting-measure contract accepts handoff", closes_k1(full_inputs))
    for missing in sorted(K1_INPUTS):
        reduced = set(K1_INPUTS)
        reduced.remove(missing)
        audit.check(f"K1 handoff fails without {missing}", not closes_k1(reduced))
    accepted_subsets = [subset for subset in all_subsets(K1_INPUTS) if closes_k1(subset)]
    audit.check("only full tested K1 subset closes handoff", accepted_subsets == [full_inputs])
    audit.check(
        "current surface inputs do not close K1",
        not closes_k1(set(CURRENT_SURFACE_INPUTS)),
    )
    audit.check(
        "current missing K1 inputs match packet",
        K1_INPUTS - CURRENT_SURFACE_INPUTS == EXPECTED_MISSING,
        ", ".join(sorted(K1_INPUTS - CURRENT_SURFACE_INPUTS)),
    )
    audit.check("K1 alone does not close electron mass", not closes_electron_mass({"K1_COUNTING_MEASURE_RETAINED"}))
    audit.check("K1 alone does not close hydrogen", not closes_hydrogen({"K1_COUNTING_MEASURE_RETAINED"}))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    k1_target = read(K1_TARGET)
    k1_decision = read(K1_DECISION)
    k1_selector_default = read(K1_SELECTOR_DEFAULT)
    k1_selector_default_decision = read(K1_SELECTOR_DEFAULT_DECISION)
    k1_selector_default_no_go = read(K1_SELECTOR_DEFAULT_NO_GO)
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
        ("K1 decision", k1_decision),
        ("K1 selector/default-exclusion target", k1_selector_default),
        ("K1 selector/default-exclusion decision", k1_selector_default_decision),
        ("K1 selector/default-exclusion current no-go", k1_selector_default_no_go),
    ]:
        audit.check(
            f"{label} references K1 current no-go or target boundary",
            NOTE.name in container and "K1_COUNTING_MEASURE_RETAINED" in container,
        )
    audit.check(
        "K1 selector/default-exclusion packet keeps current surface as target work",
        "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED" in k1_selector_default
        and "does not supply `K1_COUNTING_MEASURE_RETAINED`" in k1_selector_default,
    )
    audit.check(
        "K1 selector/default-exclusion current no-go keeps two inputs unsupplied",
        "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED" in k1_selector_default_no_go
        and "CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED" in k1_selector_default_no_go
        and "REAL_VECTOR_TRACE_DEFAULT_EXCLUDED" in k1_selector_default_no_go
        and "OWNER_RATIFICATION" in k1_selector_default_no_go
        and "AUDIT_ACCEPTANCE" in k1_selector_default_no_go,
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
    audit.check(
        "#5019 impact is premise-hygiene not K1 closure",
        "premise hygiene" in pr5019
        and "does not derive `AC_phi_lambda`" in pr5019,
    )
    audit.check(
        "#4991 impact is owner-governed premise standing not theorem closure",
        "owner-governed chain-satisfying premises" in pr4991
        and "not theorem closure" in pr4991,
    )
    audit.check(
        "#5020 impact keeps K2 exactness open",
        "exactness remains open" in pr5020
        and "No derivation or ratification of a Koide R-eta exactness theorem." in pr5020,
    )
    audit.check(
        "#5022 impact is K2 conditionality only",
        "conditionality progress" in pr5022
        and "no retained R-eta derivation" in pr5022,
    )
    audit.check(
        "K2 exactness target keeps K1 separate",
        "NO_K1_K3_K4_OR_MASS_INPUT" in k2
        and "K1 occupancy/counting" in k2,
    )
    audit.check(
        "physical electron packet requires more than K1",
        "PHYSICAL_ELECTRON_MASS_TEXT_LOCK" in physical_electron
        and "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in physical_electron
        and "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in physical_electron,
    )

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
    forbidden_primitive_nodes = [
        "k1_counting_measure_primitive",
        "orbit_holomorphic_count_selector_primitive",
        "dimension_born_default_exclusion_primitive",
        "koide_q_two_thirds_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]
    for absent in forbidden_primitive_nodes:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in primitive_nodes)
    forbidden_primitive_closures = [
        "K1_COUNTING_MEASURE_RETAINED",
        "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED",
        "DIMENSION_BORN_DEFAULT_EXCLUSION",
        "Q = 2/3",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    ]
    for phrase in forbidden_primitive_closures:
        audit.check(f"primitive texts do not supply {phrase}", phrase not in primitive_text)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in primitive_nodes)
    for excluded in ["weighting", "normalization", "probability", "selector", "readout bridge"]:
        audit.check(f"primitive notes exclude or do not grant {excluded}", excluded in primitive_text)

    section("Open PR and non-claim boundaries")
    open_markers = [
        "`#4932` AC measure binary axiom shortcut no-go | open, clean",
        "`#4991` owner-governed Tier-A retirement | open, clean",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | merged",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | merged",
        "`#5021` primitive-retirement review | open draft",
        "`#5022` delta-eta chain R-eta supplied-premise audit repair | merged, audit success",
        "`#5017`/`#5018` chirality/domain-wall stack | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "clean/green status is not a proof input",
    ]
    for marker in open_markers:
        audit.check(f"open PR marker present: {marker}", flat(marker) in note_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `K1_COUNTING_MEASURE_RETAINED`.",
        "No derivation of `r = 1/2` or `Q = 2/3` from the current retained inventory.",
        "No adoption of orbit-occupancy or any owner-governed occupancy premise.",
        "No claim that `#4932`, `#4991`, merged `#5019`, `#5020`, `#5021`, or merged",
        "No derivation or ratification of K2 exactness",
        "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.",
        "No derivation of `S_l`, A3, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note ratifies K1",
        "K1_COUNTING_MEASURE_RETAINED is supplied",
        "r = 1/2 is derived",
        "Q = 2/3 is derived",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
