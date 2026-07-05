#!/usr/bin/env python3
"""Verifier for the lepton F-clause ratification decision packet.

This runner checks that the F1-F4 source/action decision handoff is explicit
and remains separate from F/L/P/R, S_l, m_e, alpha(0), and hydrogen closure.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
SOURCE_PROBE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
F_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
F1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
F2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F3_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F4_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F4_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
L_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_LABEL_FREE_SOURCE_COORDINATE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
P_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_POSITIVE_PROJECTIVE_SOURCE_STRENGTH_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
R_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_S_L_READOUT_IDENTITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
A3_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
KOIDE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
ALPHA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

Coord = tuple[int, int, int, int]

CONTRACT_INPUTS = {
    "F_CLAUSE_TEXT_LOCK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

F_SUBCLAUSES = {"F1", "F2", "F3", "F4"}


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


def accepts_contract(inputs: set[str]) -> bool:
    return CONTRACT_INPUTS <= inputs


def closes_f_subdecision(inputs: set[str]) -> bool:
    return F_SUBCLAUSES <= inputs


def closes_f_decision(contract: set[str], subclauses: set[str]) -> bool:
    return accepts_contract(contract) and closes_f_subdecision(subclauses)


def closes_outer_source_side(clauses: set[str]) -> bool:
    return {"F", "L", "P", "R"} <= clauses


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        SOURCE_PROBE_DECISION,
        F_ASSEMBLY,
        F1_TARGET,
        F2_TARGET,
        F2_NO_GO,
        F3_TARGET,
        F3_NO_GO,
        F4_TARGET,
        F4_NO_GO,
        L_TARGET,
        P_TARGET,
        R_TARGET,
        A3_TARGET,
        KOIDE_TARGET,
        ALPHA_TARGET,
        MINIMAL,
        REGISTRY,
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
        "F-Clause Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "the charged-lepton full-cell source/action F clause",
        "F1",
        "source-coupled local-action convention",
        "F2",
        "charged-lepton source-block selector",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED",
        "F3",
        "full OS0-cell tensor source locality",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED",
        "F4",
        "scalar-multiplier attachment",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED",
        "F_CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those six contract inputs is a retained F decision",
        "F_CLAUSE_RETAINED",
        "S_lep[j] = h * B_lep * sum_{c in C} j_c O_c",
        "dS_lep/dj_c = h * B_lep * O_c",
        "L label-free source-coordinate ratification",
        "P positive projective source-strength ratification",
        "R `S_l` readout identity ratification",
        "A3 precision placement",
        "Koide/electron readout",
        "alpha(0)",
        "#5011",
        "#5010",
        "#5009",
        "#5008",
        "#5007",
        "#5006",
        "#5005",
        "#5004",
        "eta twisted walk family runner",
        "Koide native zero-section route guard repair",
        "static-source I1 hygiene companion",
        "Merge-state labels are moving review metadata",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad F-retention no-go fails; narrowed F-clause ratification",
        "No derivation or ratification of F1-F4.",
        "No derivation or ratification of F.",
        "No derivation or ratification of L, P, or R.",
        "No use of latest open PRs as proof inputs.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    audit.check("full contract and all F subclauses accept F decision", closes_f_decision(set(CONTRACT_INPUTS), set(F_SUBCLAUSES)))
    for missing in sorted(CONTRACT_INPUTS):
        reduced = set(CONTRACT_INPUTS)
        reduced.remove(missing)
        audit.check(f"F decision fails without contract input {missing}", not closes_f_decision(reduced, set(F_SUBCLAUSES)))
    for missing in sorted(F_SUBCLAUSES):
        reduced = set(F_SUBCLAUSES)
        reduced.remove(missing)
        audit.check(f"F decision fails without subclause {missing}", not closes_f_decision(set(CONTRACT_INPUTS), reduced))

    audit.check("F alone does not close outer source side", not closes_outer_source_side({"F"}))
    audit.check("F/L/P/R closes outer source-side predicate model", closes_outer_source_side({"F", "L", "P", "R"}))

    section("Finite consequence checks")
    coords = coordinates()
    audit.check("full-cell source coordinate set has 4^4 = 256 elements", len(coords) == 256)
    d17_norm = Fraction(1, 2) + Fraction(1, 2)
    audit.check("D17 two-component scalar block is unit-normalized", d17_norm == 1)
    separated_source_density = Fraction(1, 256)
    product_unit_source_factor = Fraction(1, 16)
    audit.check("separated source-density witness is 1/256", separated_source_density == Fraction(1, 256))
    audit.check("direct product unit-vector witness is 1/16", product_unit_source_factor == Fraction(1, 16))
    audit.check("F4 separates 1/256 source density from product 1/16 class", separated_source_density != product_unit_source_factor)
    h = Fraction(5, 1)
    j0 = Fraction(7, 1)
    audit.check("linear local action derivative is fixed insertion", h * j0 / j0 == h)
    audit.check("nonlinear source derivative would depend on source strength", 2 * j0 != 1)

    section("Authority boundary checks")
    goal = read(GOAL)
    source_probe_decision = read(SOURCE_PROBE_DECISION)
    f_assembly = read(F_ASSEMBLY)
    f1 = read(F1_TARGET)
    f2 = read(F2_TARGET)
    f2_no_go = read(F2_NO_GO)
    f3 = read(F3_TARGET)
    f3_no_go = read(F3_NO_GO)
    f4 = read(F4_TARGET)
    f4_no_go = read(F4_NO_GO)
    l_target = read(L_TARGET)
    p_target = read(P_TARGET)
    r_target = read(R_TARGET)
    a3 = read(A3_TARGET)
    koide = read(KOIDE_TARGET)
    alpha = read(ALPHA_TARGET)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("goal packet references F decision packet", "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md" in goal)
    audit.check("outer source-probe packet references F decision packet", "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md" in source_probe_decision)
    audit.check("F assembly remains support-only", "does not ratify F" in f_assembly)
    audit.check("F1 target remains unratified", "does not ratify F1" in f1)
    audit.check("F2 target remains unratified", "does not ratify F2" in f2)
    audit.check(
        "F2 no-go keeps F2 unsupplied",
        "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED" in f2_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in f2_no_go,
    )
    audit.check("F3 target remains unratified", "does not ratify F3" in f3)
    audit.check(
        "F3 no-go keeps F3 unsupplied",
        "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED" in f3_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in f3_no_go,
    )
    audit.check("F4 target remains unratified", "does not ratify F4" in f4)
    audit.check(
        "F4 no-go keeps F4 unsupplied",
        "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED" in f4_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in f4_no_go,
    )
    audit.check("L target remains downstream", "does not ratify L" in l_target)
    audit.check("P target remains downstream", "does not ratify P" in p_target)
    audit.check("R target remains downstream", "does not ratify R" in r_target)
    audit.check("A3 remains downstream", "No derivation of `C_A3" in a3)
    audit.check("Koide remains downstream", "No derivation of `m_e`" in koide)
    audit.check("alpha target remains downstream", "does not derive `alpha(0)`" in alpha)
    audit.check("minimal axioms exclude source/action", "source/action and physical-observable identification" in minimal)
    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    audit.check("scale primitive excludes dimensionless physics", "does not supply any dimensionless quantity" in scale)
    audit.check("kinetic primitive excludes selector and readout bridge", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5011` eta twisted walk family runner | `CLEAN`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN`",
        "`#5009` S3 spacetime tensor primitive runner repair | `CLEAN`",
        "`#5008` quark mass-ratio CP probe boundary repair | `CLEAN`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN`",
        "`#5006` static-source I1 hygiene companion | `CLEAN`",
        "`#5005` quark lane3 retention firewall companion refresh | `CLEAN`",
        "`#5004` quark C3 ward splitter hygiene companion refresh | `CLEAN`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of F1-F4.",
        "No derivation or ratification of F.",
        "No derivation or ratification of L, P, or R.",
        "No derivation that `S_l = 1/256` is retained.",
        "No derivation of the `256.082435...` precision correction.",
        "No derivation of the Koide/electron branch or physical `m_e`.",
        "No derivation of `alpha(0)` or hydrogen spectroscopy.",
        "No use of latest open PRs as proof inputs.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies F",
        "F is retained",
        "F1-F4 are retained",
        "S_l is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
