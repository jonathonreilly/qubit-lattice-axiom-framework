#!/usr/bin/env python3
"""Verifier for the source-probe interface ratification decision packet.

This runner checks the decision contract for the normalized label-free
charged-lepton full-cell source-probe interface. It does not ratify the
interface, derive m_e, alpha(0), or hydrogen.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
COMPRESSION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
RATIFICATION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
EXACT_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
L_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
L_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
P_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F_CLAUSE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
L_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_LABEL_FREE_SOURCE_COORDINATE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
P_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_POSITIVE_PROJECTIVE_SOURCE_STRENGTH_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
R_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_S_L_READOUT_IDENTITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
A3 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
KOIDE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

Coord = tuple[int, int, int, int]


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


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


def normalize(values: dict[Coord, Fraction]) -> dict[Coord, Fraction]:
    total = sum(values.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    if any(value < 0 for value in values.values()):
        raise ValueError("nonnegative values required")
    return {coord: value / total for coord, value in values.items()}


def accepts_contract(inputs: set[str]) -> bool:
    return inputs == {
        "CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    }


def all_subsets(items: list[str]) -> list[set[str]]:
    subsets: list[set[str]] = []
    for size in range(len(items) + 1):
        for combo in combinations(items, size):
            subsets.append(set(combo))
    return subsets


def closes_source_side(clauses: set[str]) -> bool:
    return clauses == {"F", "L", "P", "R"}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("decision packet exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        COMPRESSION,
        RATIFICATION,
        EXACT_SOURCE_NO_GO,
        F_DECISION,
        L_NO_GO,
        L_DECISION,
        P_NO_GO,
        P_DECISION,
        R_DECISION,
        R_NO_GO,
        F_CLAUSE,
        L_TARGET,
        P_TARGET,
        R_TARGET,
        A3,
        KOIDE,
        MINIMAL,
        REGISTRY,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    section("Required note content")
    required_phrases = [
        "Source-Probe Interface Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify F/L/P/R",
        "the normalized label-free charged-lepton full-cell source-probe interface",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "F-clause ratification decision packet",
        "F1-F4",
        "F_CLAUSE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "L-clause ratification decision packet",
        "L_CLAUSE_RETAINED",
        "SOURCE_INTERFACE",
        "FRAME_RELABELING",
        "LABEL_FREE_LICENSE",
        "TAG_EXCLUSION",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "P-clause ratification decision packet",
        "P_CLAUSE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "SOURCE_STRENGTH_OBJECT",
        "POSITIVE_NONZERO_DOMAIN",
        "SOURCE_SCALE_GAUGE",
        "PROJECTIVE_L1_SECTION",
        "SHAPE_SELECTOR",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "R-clause ratification decision packet",
        "R_CLAUSE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "source-readout target remains needed",
        "SCALE_SYMBOL_CONTEXT",
        "SOURCE_COEFFICIENT_CONTEXT",
        "COMMON_FRONT_NONZERO",
        "NORMALIZED_SINGLETON_CANDIDATE",
        "SOURCE_READOUT_LICENSE",
        "CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those six contract inputs is a retained decision",
        "C = {0,1,2,3}^4",
        "|C| = 256",
        "S_lep[j] = h * B_lep * sum_{c in C} j_c O_c",
        "sigma([j])_c = j_c / sum_d j_d",
        "H = h * sum_c j_c",
        "S_l = sigma([j])_c",
        "S_l = 1/256",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "retained exact source-side",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No-Go Discipline Gate",
        "decision-ready ratification contract",
        "No derivation or ratification of F/L/P/R.",
        "No use of latest open PRs as proof inputs.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "#5007",
        "#5006",
        "#5005",
        "#5004",
        "#5003",
        "#5002",
        "#5001",
        "#5000",
        "#4999",
        "#4998",
        "#4997",
        "Koide native zero-section route guard repair",
        "static-source I1 hygiene companion refresh",
        "quark lane3 retention firewall companion refresh",
        "quark C3 ward splitter hygiene companion refresh",
        "Hubble lane5 two-gate hygiene companion refresh",
        "The primitive registry was checked",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision contract checks")
    inputs = [
        "CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    ]
    closing_contracts = [subset for subset in all_subsets(inputs) if accepts_contract(subset)]
    audit.check("exactly one tested contract input set accepts decision", closing_contracts == [set(inputs)])
    for item in inputs:
        missing_one = set(inputs) - {item}
        audit.check(f"missing {item} fails decision acceptance", not accepts_contract(missing_one))

    clauses = ["F", "L", "P", "R"]
    closing_clauses = [subset for subset in all_subsets(clauses) if closes_source_side(subset)]
    audit.check("exactly one tested clause set closes source side", closing_clauses == [set(clauses)])
    for clause in clauses:
        audit.check(f"missing {clause} fails source-side closure", not closes_source_side(set(clauses) - {clause}))

    coords = coordinates()
    audit.check("full-cell coordinate set has 256 elements", len(coords) == 256)
    uniform = {coord: Fraction(1) for coord in coords}
    sigma = normalize(uniform)
    audit.check("uniform singleton is exact 1/256", sigma[coords[0]] == Fraction(1, 256))
    audit.check("source-side S_l consequence is exact", sigma[coords[0]] == Fraction(1, 256))
    carrier_16 = list(product(range(4), repeat=2))
    audit.check("subclause carrier witness gives 1/16", Fraction(1, len(carrier_16)) == Fraction(1, 16))
    tagged = {coord: Fraction(4 if coord[0] == 0 else 1) for coord in coords}
    tagged_sigma = normalize(tagged)
    audit.check("coordinate-tagged witness gives 1/112", tagged_sigma[(0, 0, 0, 0)] == Fraction(1, 112))
    audit.check("empirical comparator remains nonexact", Fraction(1_000_000, 256_082_435) != Fraction(1, 256))

    section("Authority boundary checks")
    goal = read(GOAL)
    route = read(ROUTE)
    compression = read(COMPRESSION)
    ratification = read(RATIFICATION)
    exact_source_no_go = read(EXACT_SOURCE_NO_GO)
    f_decision = read(F_DECISION)
    l_no_go = read(L_NO_GO)
    l_decision = read(L_DECISION)
    p_no_go = read(P_NO_GO)
    p_decision = read(P_DECISION)
    r_decision = read(R_DECISION)
    r_no_go = read(R_NO_GO)
    f_clause = read(F_CLAUSE)
    l_target = read(L_TARGET)
    p_target = read(P_TARGET)
    r_target = read(R_TARGET)
    a3 = read(A3)
    koide = read(KOIDE)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("goal packet has source-probe ratification lane", "source-probe interface" in goal and "F/L/P/R" in goal)
    audit.check("route triage has source-probe ratification lane", "source-probe interface" in route and "derive or ratify" in route)
    audit.check("source-probe packet references exact-source no-go", EXACT_SOURCE_NO_GO.name in note and "current retained, primitive, and open-PR surfaces do not supply" in note)
    audit.check("exact-source no-go names current retained boundary", "EXACT_SOURCE_SINGLETON_RETAINED" in exact_source_no_go and "retained exact source-side" in exact_source_no_go)
    audit.check("compression supplies conditional exact S_l", "Thus, under the compressed interface" in compression and "S_l = 1/256" in compression)
    audit.check("ratification target names exact decision object", "normalized label-free charged-lepton full-cell source-probe interface" in ratification)
    audit.check("F decision packet packages only F", "F_CLAUSE_TEXT_LOCK" in f_decision and "does not ratify F" in f_decision)
    audit.check("F decision packet does not retain S_l", "does not derive retained `S_l = 1/256`" in f_decision)
    audit.check("source-probe packet references L current-surface no-go", L_NO_GO.name in note and "L_CLAUSE_RETAINED" in note)
    audit.check("L no-go keeps L unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in l_no_go and "L_CLAUSE_RETAINED" in l_no_go)
    audit.check("L decision packet packages only L", "L_CLAUSE_TEXT_LOCK" in l_decision and "does not ratify L" in l_decision)
    audit.check("L decision packet does not retain S_l", "does not derive retained `S_l = 1/256`" in l_decision)
    audit.check("source-probe packet references P current-surface no-go", P_NO_GO.name in note and "P_CLAUSE_RETAINED" in note)
    audit.check("P no-go keeps P unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in p_no_go and "P_CLAUSE_RETAINED" in p_no_go)
    audit.check("P decision packet packages only P", "P_CLAUSE_TEXT_LOCK" in p_decision and "does not ratify P" in p_decision)
    audit.check("P decision packet does not retain S_l", "does not derive retained `S_l = 1/256`" in p_decision)
    audit.check("R decision packet packages only R", "R_CLAUSE_TEXT_LOCK" in r_decision and "does not ratify R" in r_decision)
    audit.check("R decision packet does not retain S_l", "does not derive retained `S_l = 1/256`" in r_decision)
    audit.check("source-probe packet references R current-surface no-go", R_NO_GO.name in note and "source-readout target remains needed" in note)
    audit.check("R no-go keeps R unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in r_no_go and "R_CLAUSE_RETAINED" in r_no_go)
    audit.check("F remains conditional", "does not ratify F" in f_clause)
    audit.check("L remains conditional", "does not ratify L" in l_target)
    audit.check("P remains conditional", "does not ratify P" in p_target)
    audit.check("R remains conditional", "does not ratify R" in r_target)
    audit.check("A3 remains downstream", "C_A3" in a3 and "Koide/electron readout" in a3)
    audit.check("Koide remains downstream", "No derivation of `m_e`" in koide)
    audit.check("minimal axioms exclude source/action", "source/action and physical-observable identification" in minimal)
    for node_name in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    audit.check("scale primitive excludes dimensionless physics", "does not supply any dimensionless quantity" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5007` Koide native zero-section route guard repair | `CLEAN`",
        "`#5006` static-source I1 hygiene companion refresh | `CLEAN`",
        "`#5005` quark lane3 retention firewall companion refresh | `CLEAN`",
        "`#5004` quark C3 ward splitter hygiene companion refresh | `CLEAN`",
        "`#5003` Hubble lane5 two-gate hygiene companion refresh | `CLEAN`",
        "`#5002` Hubble lane5 A2 hygiene companion refresh | `CLEAN`",
        "`#5001` hadron lane1 record-invariance companion refresh | `CLEAN`",
        "`#5000` axiom-first record-invariance companion refresh | `CLEAN`",
        "`#4999` Wilson descendant Schur entropy witness stabilization | `CLEAN`",
        "`#4998` neutrino split2 edge transport witness refresh | `CLEAN`",
        "`#4997` neutrino source-amplitude carrier premise bound | `CLEAN`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of F/L/P/R.",
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
        "This packet ratifies F/L/P/R",
        "F/L/P/R is retained",
        "S_l is retained",
        "This packet derives retained `S_l = 1/256`",
        "m_e is derived",
        "alpha(0) is derived",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
