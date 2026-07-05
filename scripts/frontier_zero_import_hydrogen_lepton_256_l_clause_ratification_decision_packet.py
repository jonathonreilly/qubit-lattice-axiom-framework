#!/usr/bin/env python3
"""Verifier for the lepton L-clause ratification decision packet.

This runner checks that the label-free source-coordinate decision handoff is
explicit and remains separate from F/P/R, S_l, m_e, alpha(0), and hydrogen
closure.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
L_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
SOURCE_PROBE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
L_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_LABEL_FREE_SOURCE_COORDINATE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
SOURCE_NATURALITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_NATURALITY_LABEL_FREE_LICENSE_SUPPORT_2026-07-04.md"
UNFIXED_CHOICE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COORDINATE_UNFIXED_CHOICE_LABEL_FREE_SUPPORT_2026-07-04.md"
INVARIANCE_BRIDGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_INVARIANCE_BRIDGE_SUPPORT_2026-07-04.md"
UNIFORM_RAY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md"
SOURCE_SLOT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md"
F_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
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
    "L_CLAUSE_TEXT_LOCK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

L_SUBCLAUSES = {
    "SOURCE_INTERFACE",
    "FRAME_RELABELING",
    "LABEL_FREE_LICENSE",
    "TAG_EXCLUSION",
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


def accepts_contract(inputs: set[str]) -> bool:
    return CONTRACT_INPUTS <= inputs


def closes_l_subdecision(inputs: set[str]) -> bool:
    return L_SUBCLAUSES <= inputs


def closes_l_decision(contract: set[str], subclauses: set[str]) -> bool:
    return accepts_contract(contract) and closes_l_subdecision(subclauses)


def closes_outer_source_side(clauses: set[str]) -> bool:
    return {"F", "L", "P", "R"} <= clauses


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


def swap_value(slot: int, left: int, right: int):
    def apply(coord: Coord) -> Coord:
        values = list(coord)
        if values[slot] == left:
            values[slot] = right
        elif values[slot] == right:
            values[slot] = left
        return tuple(values)  # type: ignore[return-value]

    return apply


def orbit(start: Coord, generators) -> set[Coord]:
    seen = {start}
    frontier = [start]
    while frontier:
        coord = frontier.pop()
        for gen in generators:
            nxt = gen(coord)
            if nxt not in seen:
                seen.add(nxt)
                frontier.append(nxt)
    return seen


def normalize(values: dict[Coord, Fraction]) -> dict[Coord, Fraction]:
    total = sum(values.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    return {coord: value / total for coord, value in values.items()}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        L_NO_GO,
        GOAL,
        SOURCE_PROBE_DECISION,
        L_TARGET,
        SOURCE_NATURALITY,
        UNFIXED_CHOICE,
        INVARIANCE_BRIDGE,
        UNIFORM_RAY,
        SOURCE_SLOT,
        F_DECISION,
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
        "L-Clause Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "the label-free charged-lepton source-coordinate L clause",
        "SOURCE_INTERFACE",
        "FRAME_RELABELING",
        "LABEL_FREE_LICENSE",
        "TAG_EXCLUSION",
        "L_CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those six contract inputs is a retained L decision",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "L_CLAUSE_RETAINED",
        "[j] = [rho_g j] for tensor-frame source relabelings",
        "coordinate-tagged nonuniform rays are not zero-import law-level selectors",
        "sigma([j])_(0,0,0,0) = 1/112",
        "F source/action ratification",
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
        "The broad claim \"L is ratified\" is not",
        "No derivation or ratification of L.",
        "No derivation or ratification of F, P, or R.",
        "No use of latest open PRs as proof inputs.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    audit.check("full contract and all L subclauses accept L decision", closes_l_decision(set(CONTRACT_INPUTS), set(L_SUBCLAUSES)))
    for missing in sorted(CONTRACT_INPUTS):
        reduced = set(CONTRACT_INPUTS)
        reduced.remove(missing)
        audit.check(f"L decision fails without contract input {missing}", not closes_l_decision(reduced, set(L_SUBCLAUSES)))
    for missing in sorted(L_SUBCLAUSES):
        reduced = set(L_SUBCLAUSES)
        reduced.remove(missing)
        audit.check(f"L decision fails without subclause {missing}", not closes_l_decision(set(CONTRACT_INPUTS), reduced))

    audit.check("L alone does not close outer source side", not closes_outer_source_side({"L"}))
    audit.check("F/L/P/R closes outer source-side predicate model", closes_outer_source_side({"F", "L", "P", "R"}))

    section("Finite witness checks")
    coords = coordinates()
    audit.check("full-cell source coordinate set has 4^4 = 256 elements", len(coords) == 256)
    generators = [swap_value(slot, 0, value) for slot in range(4) for value in [1, 2, 3]]
    full_orbit = orbit((0, 0, 0, 0), generators)
    audit.check("local coordinate relabelings act transitively on C", len(full_orbit) == 256)
    uniform = {coord: Fraction(1) for coord in coords}
    uniform_sigma = normalize(uniform)
    audit.check("uniform label-free singleton is 1/256", uniform_sigma[(0, 0, 0, 0)] == Fraction(1, 256))
    tagged = {coord: Fraction(4 if coord[0] == 0 else 1) for coord in coords}
    tagged_sigma = normalize(tagged)
    audit.check("coordinate-tagged singleton is 1/112", tagged_sigma[(0, 0, 0, 0)] == Fraction(1, 112))
    relabeled_tagged = {swap_value(0, 0, 1)(coord): value for coord, value in tagged.items()}
    audit.check("coordinate-tagged ray changes under source-coordinate relabeling", relabeled_tagged != tagged)
    audit.check("coordinate-tagged singleton differs from 1/256", tagged_sigma[(0, 0, 0, 0)] != Fraction(1, 256))

    section("Authority boundary checks")
    goal = read(GOAL)
    source_probe_decision = read(SOURCE_PROBE_DECISION)
    l_target = read(L_TARGET)
    l_no_go = read(L_NO_GO)
    source_naturality = read(SOURCE_NATURALITY)
    unfixed_choice = read(UNFIXED_CHOICE)
    invariance_bridge = read(INVARIANCE_BRIDGE)
    uniform_ray = read(UNIFORM_RAY)
    source_slot = read(SOURCE_SLOT)
    f_decision = read(F_DECISION)
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

    audit.check("goal packet references L decision packet", "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md" in goal)
    audit.check("outer source-probe packet references L decision packet", "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md" in source_probe_decision)
    audit.check("L target remains support-only", "does not ratify L" in l_target)
    audit.check("L decision references L current-surface no-go", L_NO_GO.name in note and "L_CLAUSE_RETAINED" in note)
    audit.check("L no-go keeps L unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in l_no_go and "L_CLAUSE_RETAINED" in l_no_go)
    audit.check("source naturality support remains conditional", "does not prove the interface is label-free" in source_naturality)
    audit.check("unfixed-choice support remains conditional", "#4952" in unfixed_choice and "closed without merge" in unfixed_choice)
    audit.check("invariance bridge assumes naturality", "does not derive that naturality rule" in flat(invariance_bridge))
    audit.check("uniform ray support assumes W5b", "W5b" in uniform_ray and "hypothesis" in uniform_ray)
    audit.check("source-slot support does not derive source family", "derive that source family" in source_slot)
    audit.check("F decision remains sibling only", "No derivation or ratification of L" in f_decision)
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
        "No derivation or ratification of the four L content subclauses.",
        "No derivation or ratification of L.",
        "No derivation or ratification of F, P, or R.",
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
        "This packet ratifies L",
        "L is retained",
        "The L clause is retained",
        "F/L/P/R is retained",
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
