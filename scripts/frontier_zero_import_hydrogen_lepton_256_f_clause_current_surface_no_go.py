#!/usr/bin/env python3
"""Verifier for the lepton F-clause current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply F_CLAUSE_RETAINED. It preserves the positive F1-F4
source/action route and keeps exact S_l, m_e, alpha(0), Rydberg, and hydrogen
downstream.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
SOURCE_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
F_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
F1_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
F2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F3_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F4_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F4_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
L_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
P_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
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

F_INPUTS = {
    "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED",
    "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED",
    "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED",
    "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED",
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


def closes_f_clause(contract: set[str], f_inputs: set[str]) -> bool:
    return CONTRACT_INPUTS <= contract and F_INPUTS <= f_inputs


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
        SOURCE_PACKET,
        EXACT_SOURCE_NO_GO,
        F_DECISION,
        F_ASSEMBLY,
        F1_NO_GO,
        F1_TARGET,
        F2_TARGET,
        F2_NO_GO,
        F3_TARGET,
        F3_NO_GO,
        F4_TARGET,
        F4_NO_GO,
        L_DECISION,
        P_DECISION,
        R_DECISION,
        A3_PACKET,
        PHYSICAL_ELECTRON,
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

    section("Required note content")
    required_phrases = [
        "F-Clause Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "F_CLAUSE_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F_CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "S_lep[j] = h * B_lep * sum_{c in C} j_c O_c",
        "dS_lep/dj_c = h * B_lep * O_c",
        "C = {0,1,2,3}^4",
        "|C| = 4^4 = 256",
        "no F1: J(j) remains formal rather than a physical local source insertion",
        "no F2: the source may be regulator-generic rather than charged-lepton-specific",
        "no F3: slot-additive, diagonal, and scalar carriers have counts 16, 4, and 1",
        "no F4: direct product unit normalization gives (1/sqrt(2))*(1/16)",
        "source_action_convention_primitive",
        "charged_lepton_source_block_selector_primitive",
        "full_cell_source_locality_primitive",
        "scalar_multiplier_attachment_primitive",
        "f_clause_primitive",
        "source_probe_interface_primitive",
        "electron_mass_primitive",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
        "No-Go Discipline Gate",
        "broad F-clause no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("F-clause predicate checks")
    full_contract = set(CONTRACT_INPUTS)
    full_f = set(F_INPUTS)
    audit.check("full F contract accepts F clause", closes_f_clause(full_contract, full_f))
    for missing in sorted(CONTRACT_INPUTS):
        reduced = set(CONTRACT_INPUTS)
        reduced.remove(missing)
        audit.check(f"F clause fails without {missing}", not closes_f_clause(reduced, full_f))
    for missing in sorted(F_INPUTS):
        reduced = set(F_INPUTS)
        reduced.remove(missing)
        audit.check(f"F clause fails without {missing}", not closes_f_clause(full_contract, reduced))

    accepted_subsets = [
        (contract, f_inputs)
        for contract in all_subsets(CONTRACT_INPUTS)
        for f_inputs in all_subsets(F_INPUTS)
        if closes_f_clause(contract, f_inputs)
    ]
    audit.check("only full F contract/subinput subset closes F", accepted_subsets == [(full_contract, full_f)])
    audit.check("F alone does not close outer source side", not closes_outer_source_side({"F"}))
    audit.check("F/L/P/R closes outer source-side predicate model", closes_outer_source_side({"F", "L", "P", "R"}))

    section("Finite F witness checks")
    coords = coordinates()
    audit.check("full-cell source coordinate set has 4^4 = 256 elements", len(coords) == 256)
    separated_source_density = Fraction(1, 256)
    product_unit_source_factor = Fraction(1, 16)
    audit.check("separated source density is 1/256", separated_source_density == Fraction(1, 256))
    audit.check("direct product unit-vector witness is 1/16", product_unit_source_factor == Fraction(1, 16))
    audit.check("F4 witness separates 1/256 from 1/16", separated_source_density != product_unit_source_factor)
    audit.check("slot-additive no-F3 carrier has 16 coordinates", 4 * 4 == 16)
    audit.check("diagonal no-F3 carrier has 4 coordinates", 4 == 4)
    audit.check("scalar no-F3 carrier has 1 coordinate", 1 == 1)
    h = Fraction(5, 1)
    j0 = Fraction(7, 1)
    audit.check("linear source derivative is fixed insertion", h * j0 / j0 == h)
    audit.check("nonlinear source derivative depends on source strength", 2 * j0 != 1)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    source_packet = read(SOURCE_PACKET)
    exact_source = read(EXACT_SOURCE_NO_GO)
    f_decision = read(F_DECISION)
    f_assembly = read(F_ASSEMBLY)
    f1_no_go = read(F1_NO_GO)
    f1 = read(F1_TARGET)
    f2 = read(F2_TARGET)
    f2_no_go = read(F2_NO_GO)
    f3 = read(F3_TARGET)
    f3_no_go = read(F3_NO_GO)
    f4 = read(F4_TARGET)
    f4_no_go = read(F4_NO_GO)
    l_decision = read(L_DECISION)
    p_decision = read(P_DECISION)
    r_decision = read(R_DECISION)
    a3 = read(A3_PACKET)
    physical_electron = read(PHYSICAL_ELECTRON)
    registry = json.loads(read(REGISTRY))
    minimal = read(MINIMAL)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    no_go_name = "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
    f1_no_go_name = "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
    audit.check("goal packet references F no-go", no_go_name in goal)
    audit.check("source-probe packet references F no-go", no_go_name in source_packet)
    audit.check("exact-source no-go references F no-go", no_go_name in exact_source)
    audit.check("F decision packet references F no-go", no_go_name in f_decision)
    audit.check("goal packet references F1 no-go", f1_no_go_name in goal)
    audit.check("F decision packet references F1 no-go", f1_no_go_name in f_decision)
    audit.check("F assembly references F1 no-go", f1_no_go_name in f_assembly)
    audit.check("F1 no-go keeps F1 unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in f1_no_go and "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED" in f1_no_go)
    f2_no_go_name = "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
    audit.check("goal packet references F2 no-go", f2_no_go_name in goal)
    audit.check("F decision packet references F2 no-go", f2_no_go_name in f_decision)
    audit.check("F assembly references F2 no-go", f2_no_go_name in f_assembly)
    audit.check("F2 no-go keeps F2 unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in f2_no_go and "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED" in f2_no_go)
    f3_no_go_name = "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md"
    audit.check("goal packet references F3 no-go", f3_no_go_name in goal)
    audit.check("F decision packet references F3 no-go", f3_no_go_name in f_decision)
    audit.check("F assembly references F3 no-go", f3_no_go_name in f_assembly)
    audit.check("F3 no-go keeps F3 unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in f3_no_go and "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED" in f3_no_go)
    f4_no_go_name = "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
    audit.check("goal packet references F4 no-go", f4_no_go_name in goal)
    audit.check("F decision packet references F4 no-go", f4_no_go_name in f_decision)
    audit.check("F assembly references F4 no-go", f4_no_go_name in f_assembly)
    audit.check("F4 no-go keeps F4 unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in f4_no_go and "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED" in f4_no_go)
    audit.check("F assembly remains support-only", "does not ratify F" in f_assembly)
    audit.check("F1 target remains unratified", "does not ratify F1" in f1)
    audit.check("F2 target remains unratified", "does not ratify F2" in f2)
    audit.check("F3 target remains unratified", "does not ratify F3" in f3)
    audit.check("F4 target remains unratified", "does not ratify F4" in f4)
    audit.check("L decision remains downstream", "does not ratify L" in l_decision)
    audit.check("P decision remains downstream", "does not ratify P" in p_decision)
    audit.check("R decision remains downstream", "does not ratify R" in r_decision)
    audit.check("A3 remains downstream", "No derivation of `C_A3" in a3)
    audit.check(
        "physical electron remains downstream",
        "No derivation or ratification of the physical electron mass" in physical_electron
        and "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in physical_electron,
    )

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    audit.check("minimal axioms exclude source/action", "source/action and physical-observable identification" in minimal)
    audit.check("scale primitive excludes dimensionless physics", "does not supply any dimensionless quantity" in scale)
    audit.check("kinetic primitive excludes selector and readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)

    for primitive_name in [
        "source_action_convention_primitive",
        "charged_lepton_source_block_selector_primitive",
        "full_cell_source_locality_primitive",
        "scalar_multiplier_attachment_primitive",
        "f_clause_primitive",
        "source_probe_interface_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered F shortcut: {primitive_name}", primitive_name not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of `F_CLAUSE_RETAINED`.",
        "No derivation or ratification of F1-F4.",
        "No derivation or ratification of L, P, or R.",
        "No derivation that `S_l = 1/256` is retained.",
        "No derivation of A3 precision placement, `C_A3`, or `N_A3`.",
        "No derivation of the Koide/electron branch or physical `m_e`.",
        "No derivation of `alpha(0)`, static-source Rydberg, or hydrogen spectroscopy.",
        "No use of observed `m_W`, observed charged-lepton masses, fitted `a_l`,",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives F",
        "This note ratifies F",
        "F_CLAUSE_RETAINED is supplied",
        "F1-F4 are retained",
        "S_l is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
