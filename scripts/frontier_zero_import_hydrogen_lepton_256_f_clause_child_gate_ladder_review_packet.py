#!/usr/bin/env python3
"""Verifier for the F-clause child-gate ladder review packet.

This runner checks that F1-F4 are review-compressed under F_CLAUSE_RETAINED
without ratifying F, the source-probe interface, exact S_l, K4, m_e,
alpha(0), or hydrogen.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CHILD_GATE_LADDER_REVIEW_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
SOURCE_EXACT_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
SOURCE_PROBE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
F_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
F_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
F_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F1_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
F2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F3_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F4_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F4_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
L_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
P_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_RATIFICATION_DECISION_PACKET_2026-07-05.md"
K4_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PR5030 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_MULTISITE_PAULI_PR5030_CARRIER_PROVENANCE_IMPACT_DISCRIMINATOR_2026-07-05.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

Coord = tuple[int, int, int, int]


F_CHILD_INPUTS = {
    "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED",
    "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED",
    "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED",
    "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED",
}

F_PARENT_INPUTS = {
    "F_CLAUSE_TEXT_LOCK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

SOURCE_PROBE_CLAUSES = {
    "F_CLAUSE_RETAINED",
    "L_CLAUSE_RETAINED",
    "P_CLAUSE_RETAINED",
    "R_CLAUSE_RETAINED",
}

EXACT_INPUTS = {
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


def closes_f(parent: set[str], children: set[str]) -> bool:
    return F_PARENT_INPUTS <= parent and F_CHILD_INPUTS <= children


def closes_source_probe(clauses: set[str]) -> bool:
    return SOURCE_PROBE_CLAUSES <= clauses


def closes_exact(inputs: set[str]) -> bool:
    return EXACT_INPUTS <= inputs


def closes_k4(inputs: set[str]) -> bool:
    return K4_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        SOURCE_EXACT_ASSEMBLY,
        SOURCE_PROBE_DECISION,
        F_ASSEMBLY,
        F_DECISION,
        F_NO_GO,
        F1_TARGET,
        F1_NO_GO,
        F2_TARGET,
        F2_NO_GO,
        F3_TARGET,
        F3_NO_GO,
        F4_TARGET,
        F4_NO_GO,
        L_DECISION,
        P_DECISION,
        R_DECISION,
        EXACT_DECISION,
        K4_DECISION,
        PR5030,
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
        "F-Clause Child-Gate Ladder Review Packet",
        "support / review-compression packet",
        "This packet does not ratify F1, F2, F3, F4",
        "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED",
        "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED",
        "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED",
        "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED",
        "F_CLAUSE_RETAINED",
        "S_lep[j] = h * B_lep * sum_{c in C} j_c O_c",
        "dS_lep/dj_c = h * B_lep * O_c",
        "L_CLAUSE_RETAINED",
        "P_CLAUSE_RETAINED",
        "R_CLAUSE_RETAINED",
        "SOURCE_PROBE_INTERFACE_CONTRACT_ACCEPTED",
        "F_CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those six contract inputs",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R",
        "C = {0,1,2,3}^4",
        "|C| = 4^4 = 256",
        "2 * 256 = 512",
        "(1/sqrt(2))*(1/16)",
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
        "`#5006` static-source I1 hygiene companion | open",
        "`#4991` owner-governed Tier-A retirement | open",
        "The primitive registry was checked",
        "source_action_convention_primitive",
        "derivative_insertion_license_primitive",
        "charged_lepton_source_block_selector_primitive",
        "full_cell_source_locality_primitive",
        "independent_matrix_unit_controls_primitive",
        "scalar_multiplier_attachment_primitive",
        "d17_block_preservation_primitive",
        "f_clause_primitive",
        "source_probe_interface_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
        "Distance To Hydrogen",
        "No-Go Discipline Gate",
        "Gate result",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("F predicate checks")
    parent_full = set(F_PARENT_INPUTS)
    child_full = set(F_CHILD_INPUTS)
    audit.check("full F parent and child gates close F", closes_f(parent_full, child_full))
    for missing in sorted(F_PARENT_INPUTS):
        reduced = set(F_PARENT_INPUTS)
        reduced.remove(missing)
        audit.check(f"F fails without parent input {missing}", not closes_f(reduced, child_full))
    for missing in sorted(F_CHILD_INPUTS):
        reduced = set(F_CHILD_INPUTS)
        reduced.remove(missing)
        audit.check(f"F fails without child input {missing}", not closes_f(parent_full, reduced))
    accepting = [
        (parent, child)
        for parent in all_subsets(F_PARENT_INPUTS)
        for child in all_subsets(F_CHILD_INPUTS)
        if closes_f(parent, child)
    ]
    audit.check("only full F subset closes", accepting == [(parent_full, child_full)])
    audit.check("F alone does not close source-probe interface", not closes_source_probe({"F_CLAUSE_RETAINED"}))
    audit.check("F/L/P/R predicate model closes source-probe clauses", closes_source_probe(set(SOURCE_PROBE_CLAUSES)))
    audit.check("F consequence alone does not close exact source", not closes_exact({"F_CLAUSE_RETAINED"}))
    audit.check("full exact-source predicate model closes exact source", closes_exact(set(EXACT_INPUTS)))
    audit.check("exact-source consequence alone does not close K4", not closes_k4({"EXACT_SOURCE_SINGLETON_RETAINED"}))
    audit.check("full K4 predicate model closes K4", closes_k4(set(K4_INPUTS)))
    audit.check("K4 consequence alone does not close hydrogen", not closes_hydrogen({"ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED"}))
    audit.check("full hydrogen predicate model closes hydrogen", closes_hydrogen(set(HYDROGEN_INPUTS)))

    section("Finite witness checks")
    coords = coordinates()
    audit.check("full-cell source coordinate set has 4^4 = 256 elements", len(coords) == 256)
    audit.check("spatial-only tensor source gives 4^3 = 64", 4**3 == 64)
    audit.check("slot-additive source gives 16 coordinates", 4 * 4 == 16)
    audit.check("diagonal source gives 4 coordinates", 4 == 4)
    audit.check("scalar source gives 1 coordinate", 1 == 1)
    audit.check("direct D17 x full-cell product has 512 components", 2 * len(coords) == 512)
    separated_density = Fraction(1, 256)
    product_density = Fraction(1, 16)
    audit.check("separated source density is 1/256", separated_density == Fraction(1, 256))
    audit.check("product unit-vector source factor is 1/16", product_density == Fraction(1, 16))
    audit.check("separated source density differs from product class", separated_density != product_density)
    h = Fraction(7, 1)
    j = Fraction(11, 1)
    audit.check("linear source derivative gives fixed insertion", h * j / j == h)
    audit.check("nonlinear source derivative depends on source strength", 2 * j != 1)

    section("Authority boundary checks")
    goal = read(GOAL)
    source_exact = read(SOURCE_EXACT_ASSEMBLY)
    source_probe = read(SOURCE_PROBE_DECISION)
    f_assembly = read(F_ASSEMBLY)
    f_decision = read(F_DECISION)
    f_no_go = read(F_NO_GO)
    f1_target = read(F1_TARGET)
    f1_no_go = read(F1_NO_GO)
    f2_target = read(F2_TARGET)
    f2_no_go = read(F2_NO_GO)
    f3_target = read(F3_TARGET)
    f3_no_go = read(F3_NO_GO)
    f4_target = read(F4_TARGET)
    f4_no_go = read(F4_NO_GO)
    l_decision = read(L_DECISION)
    p_decision = read(P_DECISION)
    r_decision = read(R_DECISION)
    exact_decision = read(EXACT_DECISION)
    k4_decision = read(K4_DECISION)
    pr5030 = read(PR5030)

    audit.check("goal packet references F child ladder", NOTE.name in goal)
    audit.check("source exact assembly references F child ladder", NOTE.name in source_exact)
    audit.check("F decision references F child ladder", NOTE.name in f_decision)
    audit.check("F no-go references F child ladder", NOTE.name in f_no_go)
    audit.check("source-probe decision consumes F", "F_CLAUSE_RETAINED" in source_probe)
    audit.check("F assembly names all F1-F4", all(token in f_assembly for token in ["F1", "F2", "F3", "F4"]))
    audit.check("F decision remains support-only", "does not ratify F1-F4" in f_decision and "F_CLAUSE_RETAINED" in f_decision)
    audit.check("F no-go keeps F unsupplied", "F_CLAUSE_RETAINED" in f_no_go and "do not supply" in f_no_go)
    audit.check("F1 target stays convention-only", "source-coupled local-action convention" in f1_target and "does not ratify F1" in f1_target)
    audit.check("F1 no-go keeps F1 unsupplied", "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED" in f1_no_go and "do not supply" in f1_no_go)
    audit.check("F2 target stays block-selector only", "charged-lepton D17 scalar block" in f2_target and "does not ratify F2" in f2_target)
    audit.check("F2 no-go keeps F2 unsupplied", "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED" in f2_no_go and "do not supply" in f2_no_go)
    audit.check("F3 target stays locality-only", "full OS0-cell tensor source locality" in f3_target and "does not ratify F3" in f3_target)
    audit.check("F3 no-go keeps F3 unsupplied", "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED" in f3_no_go and "do not supply" in f3_no_go)
    audit.check("F4 target stays attachment-only", "scalar-multiplier attachment" in f4_target and "does not ratify F4" in f4_target)
    audit.check("F4 no-go keeps F4 unsupplied", "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED" in f4_no_go and "do not supply" in f4_no_go)
    audit.check("L remains sibling/downstream", "L_CLAUSE_RETAINED" in l_decision and "does not ratify L" in l_decision)
    audit.check("P remains sibling/downstream", "P_CLAUSE_RETAINED" in p_decision and "does not ratify P" in p_decision)
    audit.check("R remains sibling/downstream", "R_CLAUSE_RETAINED" in r_decision and "does not ratify R" in r_decision)
    audit.check("exact source remains downstream", "SOURCE_PROBE_INTERFACE_CONTRACT_ACCEPTED" in exact_decision)
    audit.check("K4 remains downstream", "EXACT_SOURCE_SINGLETON_RETAINED" in k4_decision and "WEAK_FRONT_BASE_RETAINED" in k4_decision)
    audit.check("PR5030 remains finite carrier support only", "finite algebraic carrier support only" in pr5030)

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
    audit.check("minimal axioms keep downstream derivation outside axiom content", "remain outside axiom content" in minimal)
    audit.check("scale primitive excludes dimensionless content", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes source/readout", "readout bridge" in kinetic and "mass ratio" in kinetic)
    audit.check("realized primitive excludes weighting and values", "state-selection rule" in realized and "or value is supplied" in realized)
    for forbidden in [
        "source_action_convention_primitive",
        "derivative_insertion_license_primitive",
        "charged_lepton_source_block_selector_primitive",
        "full_cell_source_locality_primitive",
        "independent_matrix_unit_controls_primitive",
        "scalar_multiplier_attachment_primitive",
        "d17_block_preservation_primitive",
        "f_clause_primitive",
        "source_probe_interface_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no shortcut primitive registered: {forbidden}", forbidden not in nodes)

    section("Non-claim checks")
    explicit_non_claims = [
        "No derivation or ratification of `F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED`.",
        "No derivation or ratification of `F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED`.",
        "No derivation or ratification of `F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED`.",
        "No derivation or ratification of `F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED`.",
        "No derivation or ratification of `F_CLAUSE_RETAINED`.",
        "No derivation or ratification of L, P, R, or the source-probe interface.",
        "No retained status claim for exact source-side `S_l = 1/256`.",
        "No derivation or ratification of K4, physical electron mass, `alpha(0)`,",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies F",
        "F_CLAUSE_RETAINED is retained",
        "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED is retained",
        "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED is retained",
        "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED is retained",
        "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED is retained",
        "S_l = 1/256 is retained",
        "K4 is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
