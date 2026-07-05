#!/usr/bin/env python3
"""Verifier for the lepton L-clause current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply L_CLAUSE_RETAINED. It preserves the positive label-free
source-coordinate route and keeps exact S_l, m_e, alpha(0), Rydberg, and
hydrogen downstream.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
SOURCE_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
L_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
L_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_LABEL_FREE_SOURCE_COORDINATE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
SOURCE_NATURALITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_NATURALITY_LABEL_FREE_LICENSE_SUPPORT_2026-07-04.md"
UNFIXED_CHOICE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COORDINATE_UNFIXED_CHOICE_LABEL_FREE_SUPPORT_2026-07-04.md"
UNIFORM_RAY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md"
SOURCE_SLOT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md"
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


def closes_l_clause(contract: set[str], subclauses: set[str]) -> bool:
    return CONTRACT_INPUTS <= contract and L_SUBCLAUSES <= subclauses


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
    if any(value < 0 for value in values.values()):
        raise ValueError("nonnegative values required")
    return {coord: value / total for coord, value in values.items()}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        SOURCE_PACKET,
        EXACT_SOURCE_NO_GO,
        F_NO_GO,
        L_DECISION,
        L_TARGET,
        SOURCE_NATURALITY,
        UNFIXED_CHOICE,
        UNIFORM_RAY,
        SOURCE_SLOT,
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
        "L-Clause Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "L_CLAUSE_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
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
        "[j] = [rho_g j] for tensor-frame source relabelings",
        "coordinate-tagged nonuniform rays are not zero-import law-level selectors",
        "C = {0,1,2,3}^4",
        "|C| = 4^4 = 256",
        "sigma([1])_c = 1/256",
        "sigma([j])_(0,0,0,0) = 1/112",
        "source_coordinate_convention_primitive",
        "label_free_source_coordinate_primitive",
        "l_clause_primitive",
        "source_probe_interface_primitive",
        "source_strength_normalization_primitive",
        "s_l_readout_primitive",
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
        "broad L no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("L-clause predicate checks")
    full_contract = set(CONTRACT_INPUTS)
    full_subclauses = set(L_SUBCLAUSES)
    audit.check("full L contract accepts L clause", closes_l_clause(full_contract, full_subclauses))
    for missing in sorted(CONTRACT_INPUTS):
        reduced = set(CONTRACT_INPUTS)
        reduced.remove(missing)
        audit.check(f"L clause fails without contract input {missing}", not closes_l_clause(reduced, full_subclauses))
    for missing in sorted(L_SUBCLAUSES):
        reduced = set(L_SUBCLAUSES)
        reduced.remove(missing)
        audit.check(f"L clause fails without subclause {missing}", not closes_l_clause(full_contract, reduced))

    accepted_subsets = [
        (contract, subclauses)
        for contract in all_subsets(CONTRACT_INPUTS)
        for subclauses in all_subsets(L_SUBCLAUSES)
        if closes_l_clause(contract, subclauses)
    ]
    audit.check("only full L contract/subclause subset closes L", accepted_subsets == [(full_contract, full_subclauses)])
    audit.check("L alone does not close outer source side", not closes_outer_source_side({"L"}))
    audit.check("F/L/P/R closes outer source-side predicate model", closes_outer_source_side({"F", "L", "P", "R"}))

    section("Finite L witness checks")
    coords = coordinates()
    audit.check("source-coordinate set has 4^4 = 256 elements", len(coords) == 256)
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

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    source_packet = read(SOURCE_PACKET)
    exact_source = read(EXACT_SOURCE_NO_GO)
    f_no_go = read(F_NO_GO)
    l_decision = read(L_DECISION)
    l_target = read(L_TARGET)
    source_naturality = read(SOURCE_NATURALITY)
    unfixed_choice = read(UNFIXED_CHOICE)
    uniform_ray = read(UNIFORM_RAY)
    source_slot = read(SOURCE_SLOT)
    p_decision = read(P_DECISION)
    r_decision = read(R_DECISION)
    a3_packet = read(A3_PACKET)
    physical_electron = read(PHYSICAL_ELECTRON)
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    minimal = read(MINIMAL)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("L decision remains support-only", "does not ratify L" in l_decision and "L_CLAUSE_RETAINED" in l_decision)
    audit.check("L target remains unratified", "does not ratify L" in l_target and "1/112" in l_target)
    audit.check("source naturality support assumes label-free interface", "does not prove the interface is label-free" in source_naturality)
    audit.check("unfixed-choice support remains conditional", "#4952" in unfixed_choice and "closed without merge" in unfixed_choice)
    audit.check("uniform-ray support assumes W5b/projective semantics", "W5b" in uniform_ray and "hypothesis" in uniform_ray)
    audit.check("source-slot support does not derive source family", "derive that source family" in source_slot)
    audit.check("F no-go remains sibling context", "F_CLAUSE_RETAINED" in f_no_go and "No derivation or ratification of L" in f_no_go)
    audit.check("P decision remains downstream", "does not ratify P" in p_decision)
    audit.check("R decision remains downstream", "does not ratify R" in r_decision)
    audit.check("A3 remains downstream", "A3_PRECISION_PLACEMENT_RETAINED" in a3_packet)
    audit.check("physical electron remains downstream", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in physical_electron)

    audit.check("goal packet can reference L decision", "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md" in goal)
    audit.check("source-probe packet can reference L decision", "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md" in source_packet)
    audit.check("exact source no-go can reference L decision", "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md" in exact_source)

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
    for absent in [
        "source_coordinate_convention_primitive",
        "label_free_source_coordinate_primitive",
        "l_clause_primitive",
        "source_probe_interface_primitive",
        "source_strength_normalization_primitive",
        "s_l_readout_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered L shortcut: {absent}", absent not in registry_text)

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
        audit.check(f"latest PR marker present: {marker}", marker in note)

    explicit_non_claims = [
        "No derivation or ratification of `L_CLAUSE_RETAINED`.",
        "No derivation or ratification of the four L content subclauses.",
        "No derivation or ratification of F, P, or R.",
        "No derivation or ratification of F/L/P/R.",
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
        "This note ratifies L",
        "This note derives L",
        "L_CLAUSE_RETAINED is supplied",
        "F/L/P/R is retained",
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
