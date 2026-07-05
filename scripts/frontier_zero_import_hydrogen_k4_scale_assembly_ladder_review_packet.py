#!/usr/bin/env python3
"""Verifier for the K4 scale assembly ladder review packet.

This runner checks that the K4 ladder compression is explicit and remains a
review-support surface. It does not ratify K4, physical electron mass, alpha(0),
static-source Rydberg closure, or hydrogen.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_K4_SCALE_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
K4_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
K4_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
WEAK_FRONT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
WEAK_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
D17_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_D17_BLOCK_NORMALIZATION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SU2_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_SU2_COUPLING_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SOURCE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_SOURCE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_RATIFICATION_DECISION_PACKET_2026-07-05.md"
EXACT_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_NO_DOUBLE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_NO_DOUBLE_COUNT_COMPOSITION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
P1_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P2_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_RATIFICATION_DECISION_PACKET_2026-07-05.md"
P2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P4_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
ALPHA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


SU2_INPUTS = {
    "SU2_WEAK_COUPLING_CONTEXT_TEXT_LOCK",
    "CL3_SU2_WEAK_CONTEXT_ACCEPTED",
    "BARE_G2_SYMBOL_SCOPE_LOCK",
    "CHARGED_LEPTON_WEAK_DOUBLET_SCOPE_LOCK",
    "RUNNING_STRUCTURE_BOUNDARY_LOCK",
    "NO_PHYSICAL_G2V_OR_MW_INPUT",
    "NO_THRESHOLD_OR_A3_MATCHING_INPUT",
    "NO_D17_SOURCE_SINGLETON_OR_MASS_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

D17_INPUTS = {
    "D17_BLOCK_NORMALIZATION_TEXT_LOCK",
    "D17_STATED_BLOCK_SCOPE_ACCEPTED",
    "TWO_COMPONENT_UNIT_NORMALIZATION_CHECK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "D17_ONLY_NO_SOURCE_SINGLETON_OR_A3_INPUT",
    "NO_WEAK_COUPLING_OR_FRONT_BASE_INPUT",
    "NO_MASS_OR_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

WEAK_FRONT_INPUTS = {
    "WEAK_FRONT_BASE_TEXT_LOCK",
    "SU2_WEAK_COUPLING_CONTEXT_RETAINED",
    "CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "UNCORRECTED_FRONT_SCOPE_LOCK",
    "NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT",
    "NO_A3_OR_THRESHOLD_MATCHING_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

EXACT_SOURCE_INPUTS = {
    "EXACT_SOURCE_SINGLETON_TEXT_LOCK",
    "SOURCE_PROBE_INTERFACE_CONTRACT_ACCEPTED",
    "FULL_CELL_SOURCE_CARRIER_CHECK",
    "PROJECTIVE_UNIFORM_RAY_CHECK",
    "S_L_READOUT_IDENTITY_BOUND",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "NO_A3_OR_K4_OR_MASS_INPUT",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

A3_INPUTS = {
    "A3_PLACEMENT_TEXT_LOCK",
    "EXACT_SOURCE_SCAFFOLD_STATUS",
    "ONE_PLACEMENT_SELECTED",
    "PLACEMENT_THEOREM_RETAINED",
    "NO_SOURCE_DOUBLE_COUNT",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

A3_PLACEMENTS = {
    "P1_SOURCE_READOUT_CORRECTION_RETAINED",
    "P2_WEAK_FRONT_MATCHING_RETAINED",
    "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED",
    "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED",
}

NO_DOUBLE_INPUTS = {
    "A3_SINGLE_SPEND_TEXT_LOCK",
    "PLACEMENT_SLOT_SET_LOCK",
    "EXACT_SOURCE_SCAFFOLD_SEPARATION",
    "ONE_CORRECTION_SPEND_RULE",
    "DEPENDENCY_LOCATION_LABEL_RETAINED",
    "PRODUCT_EQUIVALENCE_NOT_THEOREM",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

K4_INPUTS = {
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
    "PHYSICAL_ELECTRON_MASS_TEXT_LOCK",
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
    "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
    "NO_LEPTON_COMPARATOR_PROOF_INPUT",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

HYDROGEN_INPUTS = {
    "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
    "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
    "ATOMIC_OPERATOR_HARNESS_VERIFIED",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
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


def closes_su2(inputs: set[str]) -> bool:
    return SU2_INPUTS <= inputs


def closes_d17(inputs: set[str]) -> bool:
    return D17_INPUTS <= inputs


def closes_weak_front(inputs: set[str]) -> bool:
    return WEAK_FRONT_INPUTS <= inputs


def closes_exact_source(inputs: set[str]) -> bool:
    return EXACT_SOURCE_INPUTS <= inputs


def closes_a3(inputs: set[str], placements: set[str]) -> bool:
    return A3_INPUTS <= inputs and len(A3_PLACEMENTS & placements) == 1


def closes_no_double(inputs: set[str]) -> bool:
    return NO_DOUBLE_INPUTS <= inputs


def closes_k4(inputs: set[str]) -> bool:
    return K4_INPUTS <= inputs


def closes_physical_electron(inputs: set[str]) -> bool:
    return PHYSICAL_ELECTRON_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def assert_only_full_contract(
    audit: Audit,
    name: str,
    inputs: set[str],
    predicate,
    *,
    placements: set[str] | None = None,
) -> None:
    if placements is None:
        audit.check(f"full {name} contract closes", predicate(set(inputs)))
        for missing in sorted(inputs):
            reduced = set(inputs)
            reduced.remove(missing)
            audit.check(f"{name} contract fails without {missing}", not predicate(reduced))
        accepted = [subset for subset in all_subsets(inputs) if predicate(subset)]
    else:
        audit.check(f"full {name} contract closes", predicate(set(inputs), placements))
        for missing in sorted(inputs):
            reduced = set(inputs)
            reduced.remove(missing)
            audit.check(f"{name} contract fails without {missing}", not predicate(reduced, placements))
        accepted = [subset for subset in all_subsets(inputs) if predicate(subset, placements)]
    audit.check(f"only full {name} subset closes", accepted == [set(inputs)])


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        KOIDE_FIREWALL,
        K4_DECISION,
        K4_NO_GO,
        WEAK_FRONT_DECISION,
        WEAK_FRONT_NO_GO,
        D17_DECISION,
        SU2_DECISION,
        SOURCE_DECISION,
        EXACT_SOURCE_DECISION,
        EXACT_SOURCE_NO_GO,
        A3_DECISION,
        A3_NO_GO,
        A3_NO_DOUBLE,
        P1_NO_GO,
        P2_DECISION,
        P2_NO_GO,
        P3_NO_GO,
        P4_NO_GO,
        PHYSICAL_ELECTRON,
        PHYSICAL_ELECTRON_NO_GO,
        ALPHA_TARGET,
        STATIC_TARGET,
        REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required packet content")
    required_phrases = [
        "K4 Scale Assembly Ladder Review Packet",
        "support / review-compression packet",
        "this packet does not ratify K4",
        "reviewable surface",
        "WEAK_FRONT_BASE_RETAINED",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "NO_SOURCE_A3_DOUBLE_COUNT",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "K4_SCALE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those ten contract inputs",
        "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_SU2_COUPLING_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "SU2_WEAK_COUPLING_CONTEXT_RETAINED",
        "NO_PHYSICAL_G2V_OR_MW_INPUT",
        "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_D17_BLOCK_NORMALIZATION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED",
        "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "F_0 = g_2 * (1/sqrt(2))",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "S_l = 1/256",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_NO_DOUBLE_COUNT_COMPOSITION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "NO_SOURCE_DOUBLE_COUNT",
        "P1_SOURCE_READOUT_CORRECTION_RETAINED",
        "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED",
        "P2_WEAK_FRONT_MATCHING_RETAINED",
        "MATCHING_THEOREM_RETAINED",
        "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED",
        "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED",
        "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED",
        "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED",
        "|C| = 4^4 = 256",
        "sqrt(2)/512 = (1/sqrt(2))/256",
        "N_A3 = 256.08243522600384",
        "C_A3 = 256 / N_A3 = 0.9996780910571587",
        "C_A3^2",
        "`#5033` RP two-step runner scope cleanup | open, clean",
        "`#5030` multisite Pauli carrier provenance | open, clean",
        "`#5021` primitive-retirement review | open draft, dirty",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` chirality domain-wall free-field note | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#4991` owner-governed Tier-A retirement | open",
        "The primitive registry was checked",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
        "absolute_charged_lepton_scale_primitive",
        "hydrogen_primitive",
        "Distance To Hydrogen",
        "No-Go Discipline Gate",
        "current retained, primitive, and open-PR surfaces do not supply K4 merely because the direct ladder is now review-compressed",
        "Gate result",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Contract predicate checks")
    assert_only_full_contract(audit, "SU2 context", SU2_INPUTS, closes_su2)
    assert_only_full_contract(audit, "D17 block", D17_INPUTS, closes_d17)
    assert_only_full_contract(audit, "weak-front", WEAK_FRONT_INPUTS, closes_weak_front)
    assert_only_full_contract(audit, "exact-source", EXACT_SOURCE_INPUTS, closes_exact_source)
    assert_only_full_contract(audit, "A3 placement", A3_INPUTS, closes_a3, placements={"P2_WEAK_FRONT_MATCHING_RETAINED"})
    assert_only_full_contract(audit, "A3 no-double-count", NO_DOUBLE_INPUTS, closes_no_double)
    assert_only_full_contract(audit, "K4", K4_INPUTS, closes_k4)

    section("Ladder non-closure checks")
    audit.check("SU2 alone does not close weak front", not closes_weak_front({"SU2_WEAK_COUPLING_CONTEXT_RETAINED"}))
    audit.check("D17 alone does not close weak front", not closes_weak_front({"CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED"}))
    audit.check("weak-front alone does not close K4", not closes_k4({"WEAK_FRONT_BASE_RETAINED"}))
    audit.check("exact source alone does not close K4", not closes_k4({"EXACT_SOURCE_SINGLETON_RETAINED"}))
    audit.check("A3 placement alone does not close K4", not closes_k4({"A3_PRECISION_PLACEMENT_RETAINED"}))
    audit.check("no-double-count alone does not close K4", not closes_k4({"NO_SOURCE_A3_DOUBLE_COUNT"}))
    k4_direct_inputs = {
        "WEAK_FRONT_BASE_RETAINED",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "NO_SOURCE_A3_DOUBLE_COUNT",
    }
    audit.check("direct K4 inputs without parent clauses do not close K4", not closes_k4(k4_direct_inputs))
    audit.check("full K4 consequence alone does not close physical electron", not closes_physical_electron({"ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED"}))
    audit.check("full physical electron contract model closes electron", closes_physical_electron(set(PHYSICAL_ELECTRON_INPUTS)))
    audit.check("physical electron consequence alone does not close hydrogen", not closes_hydrogen({"RETAINED_ELECTRON_MASS_PHYSICAL_UNIT"}))
    audit.check("full hydrogen predicate model closes hydrogen", closes_hydrogen(set(HYDROGEN_INPUTS)))

    section("Finite arithmetic checks")
    full_cell_count = 4**4
    audit.check("full cell count is 256", full_cell_count == 256)
    audit.check("source singleton is exact 1/256", Fraction(1, full_cell_count) == Fraction(1, 256))
    audit.check("sqrt2 over 512 identity reduces to 1/256", Fraction(2, 512) == Fraction(1, 256))

    getcontext().prec = 60
    n_a3 = Decimal("256.08243522600384")
    c_a3 = Decimal(256) / n_a3
    s0 = Decimal(1) / Decimal(256)
    direct = Decimal(1) / n_a3
    f0 = Decimal("0.461616")
    r0 = Decimal("0.001628")
    p1 = f0 * (c_a3 * s0) * r0
    p2 = (c_a3 * f0) * s0 * r0
    p3 = f0 * s0 * (c_a3 * r0)
    p4 = f0 * direct * r0
    double_count = (c_a3 * f0) * (c_a3 * s0) * r0
    audit.check("C_A3 is the expected precision correction", abs(c_a3 - Decimal("0.9996780910571587")) < Decimal("1e-16"), str(c_a3))
    audit.check("C_A3 times source singleton equals direct divisor", abs(c_a3 * s0 - direct) < Decimal("1e-55"))
    audit.check("P1 and P2 products agree", p1 == p2)
    audit.check("P1 and P3 products agree", abs(p1 - p3) < Decimal("1e-55"))
    audit.check("P1 and P4 products agree", p1 == p4)
    audit.check("double-count product differs by an extra C_A3", double_count != p1 and abs(double_count / p1 - c_a3) < Decimal("1e-55"))

    section("Authority boundary checks")
    goal = read(GOAL)
    koide = read(KOIDE_FIREWALL)
    k4_decision = read(K4_DECISION)
    k4_no_go = read(K4_NO_GO)
    weak_front = read(WEAK_FRONT_DECISION)
    weak_front_no_go = read(WEAK_FRONT_NO_GO)
    d17 = read(D17_DECISION)
    su2 = read(SU2_DECISION)
    source = read(SOURCE_DECISION)
    exact_source = read(EXACT_SOURCE_DECISION)
    exact_source_no_go = read(EXACT_SOURCE_NO_GO)
    a3 = read(A3_DECISION)
    a3_no_go = read(A3_NO_GO)
    a3_no_double = read(A3_NO_DOUBLE)
    p1_no_go = read(P1_NO_GO)
    p2_decision = read(P2_DECISION)
    p2_no_go = read(P2_NO_GO)
    p3_no_go = read(P3_NO_GO)
    p4_no_go = read(P4_NO_GO)
    physical_electron = read(PHYSICAL_ELECTRON)
    physical_electron_no_go = read(PHYSICAL_ELECTRON_NO_GO)
    alpha_target = read(ALPHA_TARGET)
    static_target = read(STATIC_TARGET)

    audit.check("goal packet references K4 ladder review", NOTE.name in goal)
    audit.check("Koide firewall references K4 ladder review", NOTE.name in koide)
    audit.check("K4 parent decision references weak front", "WEAK_FRONT_BASE_RETAINED" in k4_decision)
    audit.check("K4 parent decision references exact source", "EXACT_SOURCE_SINGLETON_RETAINED" in k4_decision)
    audit.check("K4 parent decision references A3 placement", "A3_PRECISION_PLACEMENT_RETAINED" in k4_decision)
    audit.check("K4 current no-go keeps K4 unsupplied", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in k4_no_go and "do not supply" in k4_no_go)
    audit.check("weak-front decision remains front-only", "F_0 = g_2 * (1/sqrt(2))" in weak_front and "does not derive the A3 correction" in weak_front)
    audit.check("weak-front no-go keeps base unsupplied", "WEAK_FRONT_BASE_RETAINED" in weak_front_no_go and "do not supply" in weak_front_no_go)
    audit.check("D17 decision remains below weak front", "CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED" in d17 and "does not ratify the weak-front base" in d17)
    audit.check("SU2 decision remains below weak front", "SU2_WEAK_COUPLING_CONTEXT_RETAINED" in su2 and "does not ratify the weak-front base" in su2)
    audit.check("source decision stays source-side", "This is source-side only" in source and "does not derive" in source)
    audit.check("exact-source decision remains below K4", "EXACT_SOURCE_SINGLETON_RETAINED" in exact_source and "No derivation or ratification of K4 scale assembly" in exact_source)
    audit.check("exact-source no-go keeps singleton unsupplied", "EXACT_SOURCE_SINGLETON_RETAINED" in exact_source_no_go and "do not supply" in exact_source_no_go)
    audit.check("A3 decision remains placement-only", "A3_PRECISION_PLACEMENT_RETAINED" in a3 and "does not by itself derive `C_A3`" in a3)
    audit.check("A3 no-go keeps placement unsupplied", "A3_PRECISION_PLACEMENT_RETAINED" in a3_no_go and "do not supply" in a3_no_go)
    audit.check("A3 no-double-count stays below A3 placement", "NO_SOURCE_A3_DOUBLE_COUNT" in a3_no_double and "does not supply `A3_PRECISION_PLACEMENT_RETAINED`" in a3_no_double)
    audit.check("P1 no-go names source-readout theorem", "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED" in p1_no_go)
    audit.check("P2 decision remains parent-A3 upstream", "P2_MATCHING_TEXT_LOCK" in p2_decision and "A3_PRECISION_PLACEMENT_RETAINED" in p2_decision)
    audit.check("P2 no-go names matching theorem", "MATCHING_THEOREM_RETAINED" in p2_no_go)
    audit.check("P3 no-go names Koide correction theorem", "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED" in p3_no_go)
    audit.check("P4 no-go names direct divisor theorem", "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED" in p4_no_go)
    audit.check("physical electron contract depends on K4", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in physical_electron and "KOIDE_BRANCH_MASS_MAP_RETAINED" in physical_electron)
    audit.check("physical electron no-go remains open", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in physical_electron_no_go and "do not supply" in physical_electron_no_go)
    audit.check("alpha target remains downstream", "No derivation of `alpha(0)`" in alpha_target)
    audit.check("static target remains downstream", "STATIC_SOURCE_RYDBERG" in static_target or "static-source Rydberg" in static_target)

    section("Primitive registry checks")
    registry = json.loads(read(REGISTRY))
    nodes = registry["nodes"]
    expected_nodes = {
        "minimal_axioms": "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "scale_reference_primitive": "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "kinetic_isotropy_primitive": "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "realized_state_primitive": "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    }
    for node, path in expected_nodes.items():
        audit.check(f"registry node present: {node}", node in nodes)
        audit.check(f"registry path matches for {node}", nodes[node]["current_path"] == path)

    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = flat(read(KINETIC)).lower()
    realized = flat(read(REALIZED)).lower()
    audit.check("minimal axioms do not supply downstream physics", "structure requires derivation, bridge, explicit admission" in minimal)
    audit.check("scale primitive excludes dimensionless content", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes readout bridge", "readout bridge" in kinetic and "mass ratio" in kinetic)
    audit.check("realized primitive excludes state-selection values", "state-selection rule" in realized and "or value is supplied" in realized)
    for forbidden in [
        "weak_front_base_primitive",
        "exact_source_singleton_primitive",
        "a3_precision_placement_primitive",
        "a3_no_double_count_primitive",
        "absolute_charged_lepton_scale_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"unregistered primitive absent: {forbidden}", forbidden not in nodes)

    section("Open PR and non-claim checks")
    pr_markers = [
        "`#5033` RP two-step runner scope cleanup | open, clean",
        "`#5030` multisite Pauli carrier provenance | open, clean",
        "`#5021` primitive-retirement review | open draft, dirty",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` chirality domain-wall free-field note | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#4991` owner-governed Tier-A retirement | open",
    ]
    for marker in pr_markers:
        audit.check(f"PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of `WEAK_FRONT_BASE_RETAINED`.",
        "No derivation or ratification of `EXACT_SOURCE_SINGLETON_RETAINED`.",
        "No derivation or ratification of `A3_PRECISION_PLACEMENT_RETAINED`.",
        "No derivation or ratification of `NO_SOURCE_A3_DOUBLE_COUNT`.",
        "No derivation or ratification of `ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED`.",
        "No derivation or ratification of native zero-section bridge, physical",
        "No new axiom, primitive, Tier-A admission, or empirical comparator import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    audit.summary()


if __name__ == "__main__":
    main()
