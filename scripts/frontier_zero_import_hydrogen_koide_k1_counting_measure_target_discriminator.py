#!/usr/bin/env python3
"""Verifier for the hydrogen-facing Koide K1 counting-measure target."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_TARGET_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
COUNTING_SYNTHESIS = ROOT / "docs" / "CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md"
SUPERTRACE_OPEN = ROOT / "docs" / "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md"
OCCUPANCY_INDEPENDENCE = ROOT / "docs" / "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md"
BEREZIN_SUBSUMPTION = ROOT / "docs" / "OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md"
KERNEL_COEFFICIENT = ROOT / "docs" / "KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md"
TWO_GATE = ROOT / "docs" / "CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md"
PR5019_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR4991_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_TIER_A_OWNER_RETIREMENT_PR4991_IMPACT_DISCRIMINATOR_2026-07-04.md"
K2_EXACTNESS = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


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


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        KOIDE_FIREWALL,
        COUNTING_SYNTHESIS,
        SUPERTRACE_OPEN,
        OCCUPANCY_INDEPENDENCE,
        BEREZIN_SUBSUMPTION,
        KERNEL_COEFFICIENT,
        TWO_GATE,
        PR5019_IMPACT,
        PR4991_IMPACT,
        K2_EXACTNESS,
        PHYSICAL_ELECTRON,
        PRIMITIVE_REGISTRY,
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
        "Koide K1 Counting-Measure Target Discriminator",
        "target discriminator / Koide K1 counting-measure handoff",
        "does not ratify K1",
        "K1_COUNTING_MEASURE_RETAINED",
        "K1_COUNTING_TEXT_LOCK",
        "C3_CIRCULANT_FORM_RETAINED",
        "BLOCK_VS_DIMENSION_FORK_REPROVEN",
        "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED",
        "DIMENSION_BORN_DEFAULT_EXCLUSION",
        "NO_K2_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "No proper subset of those ten inputs supplies K1",
        "CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md",
        "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md",
        "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md",
        "OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md",
        "KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md",
        "CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md",
        "open `#4932`",
        "open `#4991`",
        "merged `#5019`",
        "The primitive registry was checked",
        "Registered primitives are approved premise nodes, not walls",
        "no primitive supplies `K1_COUNTING_MEASURE_RETAINED`",
        "current retained surface does not choose the block/orbit count",
        "K1 has an explicit ten-input hydrogen-facing target contract",
        "No-Go Discipline Gate",
        "broad K1-closure claim fails; narrowed counting-measure target",
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
    audit.check("full K1 counting-measure contract accepts target", closes_k1(full_inputs))
    for missing in sorted(K1_INPUTS):
        reduced = set(K1_INPUTS)
        reduced.remove(missing)
        audit.check(f"K1 target fails without {missing}", not closes_k1(reduced))
    accepted_subsets = [subset for subset in all_subsets(K1_INPUTS) if closes_k1(subset)]
    audit.check("only full tested K1 contract subset closes target", accepted_subsets == [full_inputs])
    audit.check("K1 alone does not close electron mass", not closes_electron_mass({"K1_COUNTING_MEASURE_RETAINED"}))
    audit.check("K1 alone does not close hydrogen", not closes_hydrogen({"K1_COUNTING_MEASURE_RETAINED"}))

    section("Authority boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    counting = read(COUNTING_SYNTHESIS)
    supertrace = read(SUPERTRACE_OPEN)
    occupancy = read(OCCUPANCY_INDEPENDENCE)
    berezin = read(BEREZIN_SUBSUMPTION)
    kernel = read(KERNEL_COEFFICIENT)
    two_gate = read(TWO_GATE)
    pr5019 = read(PR5019_IMPACT)
    pr4991 = read(PR4991_IMPACT)
    k2 = read(K2_EXACTNESS)
    physical_electron = read(PHYSICAL_ELECTRON)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
    ]:
        audit.check(
            f"{label} references K1 target",
            NOTE.name in container and "K1_COUNTING_MEASURE_RETAINED" in container,
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
    forbidden_primitive_closures = [
        "K1_COUNTING_MEASURE_RETAINED",
        "ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED",
        "r = 1/2",
        "Q = 2/3",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    ]
    for phrase in forbidden_primitive_closures:
        audit.check(f"primitive texts do not supply {phrase}", phrase not in primitive_text)

    section("Explicit non-claim checks")
    non_claims = [
        "No derivation or ratification of `K1_COUNTING_MEASURE_RETAINED`.",
        "No derivation of `r = 1/2` or `Q = 2/3` from the current retained inventory.",
        "No adoption of orbit-occupancy or any owner-governed occupancy premise.",
        "No derivation or ratification of K2 exactness",
        "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.",
        "No derivation of `S_l`, A3, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    audit.summary()


if __name__ == "__main__":
    main()
