#!/usr/bin/env python3
"""Verifier for the lepton R-clause ratification decision packet.

This runner checks that the S_l source-readout identity decision handoff is
explicit and remains separate from F/L/P, retained S_l, m_e, alpha(0), and
hydrogen closure.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
SOURCE_PROBE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_S_L_READOUT_IDENTITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
SL_BRIDGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
D17_SEP = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
SHAPE_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md"
P_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
F_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
L_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
SCHUR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SCHUR_TWO_SCALE_FIREWALL_2026-07-04.md"
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
    "R_CLAUSE_TEXT_LOCK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

R_SUBCLAUSES = {
    "SCALE_SYMBOL_CONTEXT",
    "SOURCE_COEFFICIENT_CONTEXT",
    "COMMON_FRONT_NONZERO",
    "NORMALIZED_SINGLETON_CANDIDATE",
    "SOURCE_READOUT_LICENSE",
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


def closes_r_subdecision(inputs: set[str]) -> bool:
    return R_SUBCLAUSES <= inputs


def closes_r_decision(contract: set[str], subclauses: set[str]) -> bool:
    return accepts_contract(contract) and closes_r_subdecision(subclauses)


def closes_outer_source_side(clauses: set[str]) -> bool:
    return {"F", "L", "P", "R"} <= clauses


def normalize(values: dict[Coord, Fraction]) -> dict[Coord, Fraction]:
    if any(value < 0 for value in values.values()):
        raise ValueError("nonnegative values required")
    total = sum(values.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    return {coord: value / total for coord, value in values.items()}


def solve_s_l(front: Fraction, coeff: Fraction) -> Fraction:
    if front == 0:
        raise ValueError("nonzero front required")
    return coeff / front


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        SOURCE_PROBE_DECISION,
        R_TARGET,
        SL_BRIDGE,
        LEPTON_SCALE,
        D17_SEP,
        SOURCE_COUPLED,
        SHAPE_SELECTOR,
        P_DECISION,
        F_DECISION,
        L_DECISION,
        R_NO_GO,
        PROJECTIVE_SECTION,
        SCHUR,
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
        "R-Clause Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "the charged-lepton S_l source-readout identity R clause",
        "SCALE_SYMBOL_CONTEXT",
        "SOURCE_COEFFICIENT_CONTEXT",
        "COMMON_FRONT_NONZERO",
        "NORMALIZED_SINGLETON_CANDIDATE",
        "SOURCE_READOUT_LICENSE",
        "R_CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those six contract inputs is a retained R decision",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "source-readout target remains needed",
        "R_CLAUSE_RETAINED",
        "S_l = sigma([j])_c",
        "y_scale(c)  = g_2 * (1/sqrt(2)) * S_l",
        "y_source(c) = g_2 * (1/sqrt(2)) * sigma([j])_c",
        "S_l = (3/2) * sigma([j])_c",
        "lattice `y_0 = 1/256`",
        "empirical comparator reciprocal `1/256.082435...`",
        "F source/action ratification",
        "L label-free source-coordinate ratification",
        "P positive projective source-strength ratification",
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
        "The broad claim \"R is ratified\" is not",
        "No derivation or ratification of R.",
        "No derivation or ratification of F, L, or P.",
        "No use of latest open PRs as proof inputs.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    audit.check("full contract and all R subclauses accept R decision", closes_r_decision(set(CONTRACT_INPUTS), set(R_SUBCLAUSES)))
    for missing in sorted(CONTRACT_INPUTS):
        reduced = set(CONTRACT_INPUTS)
        reduced.remove(missing)
        audit.check(f"R decision fails without contract input {missing}", not closes_r_decision(reduced, set(R_SUBCLAUSES)))
    for missing in sorted(R_SUBCLAUSES):
        reduced = set(R_SUBCLAUSES)
        reduced.remove(missing)
        audit.check(f"R decision fails without subclause {missing}", not closes_r_decision(set(CONTRACT_INPUTS), reduced))

    audit.check("R alone does not close outer source side", not closes_outer_source_side({"R"}))
    audit.check("F/L/P/R closes outer source-side predicate model", closes_outer_source_side({"F", "L", "P", "R"}))

    section("Finite witness checks")
    coords: list[Coord] = list(product(range(4), repeat=4))
    audit.check("full-cell source coordinate set has 4^4 = 256 elements", len(coords) == 256)
    uniform = {coord: Fraction(1) for coord in coords}
    sigma = normalize(uniform)
    coord = (0, 0, 0, 0)
    audit.check("uniform normalized singleton is 1/256", sigma[coord] == Fraction(1, 256))

    front = Fraction(7, 11)
    source_coeff = front * sigma[coord]
    audit.check("nonzero common front cancellation gives S_l", solve_s_l(front, source_coeff) == Fraction(1, 256))
    projection_coeff = front * Fraction(1, 16)
    audit.check("projection/RN coefficient solves 1/16 instead", solve_s_l(front, projection_coeff) == Fraction(1, 16))
    audit.check("projection/RN witness differs from source singleton", Fraction(1, 16) != Fraction(1, 256))
    mismatched_source_front = front * Fraction(3, 2)
    mismatched_coeff = mismatched_source_front * sigma[coord]
    audit.check("mismatched front rescales solved S_l", solve_s_l(front, mismatched_coeff) == Fraction(3, 2) * sigma[coord])
    try:
        solve_s_l(Fraction(0), source_coeff)
        zero_front_rejected = False
    except ValueError:
        zero_front_rejected = True
    audit.check("zero front cannot be cancelled", zero_front_rejected)

    h = Fraction(5, 1)
    lam = Fraction(7, 1)
    tagged = {c: Fraction(4 if c[0] == 0 else 1) for c in coords}
    total = sum(tagged.values(), Fraction(0))
    tagged_scaled = {c: lam * value for c, value in tagged.items()}
    total_scaled = sum(tagged_scaled.values(), Fraction(0))
    audit.check("raw h changes under source-scale gauge", h / lam != h)
    audit.check("raw j_c changes under source-scale gauge", tagged_scaled[coord] != tagged[coord])
    audit.check("h*j_c is front-bearing, not normalized singleton", h * tagged[coord] != tagged[coord] / total)
    audit.check("H is global front, not singleton", h * total != tagged[coord] / total)
    audit.check("sigma survives source-scale gauge", tagged_scaled[coord] / total_scaled == tagged[coord] / total)

    y0_lattice = Fraction(1, 256)
    comparator = Fraction(1_000_000, 256_082_435)
    audit.check("lattice y0 is numerically 1/256 but separate route", y0_lattice == Fraction(1, 256))
    audit.check("empirical comparator reciprocal differs from exact 1/256", comparator != Fraction(1, 256))

    section("Authority boundary checks")
    goal = read(GOAL)
    source_probe_decision = read(SOURCE_PROBE_DECISION)
    r_target = read(R_TARGET)
    sl_bridge = read(SL_BRIDGE)
    lepton_scale = read(LEPTON_SCALE)
    d17_sep = read(D17_SEP)
    source_coupled = read(SOURCE_COUPLED)
    shape_selector = read(SHAPE_SELECTOR)
    p_decision = read(P_DECISION)
    f_decision = read(F_DECISION)
    l_decision = read(L_DECISION)
    r_no_go = read(R_NO_GO)
    projective_section = read(PROJECTIVE_SECTION)
    schur = read(SCHUR)
    a3 = read(A3_TARGET)
    koide = read(KOIDE_TARGET)
    alpha = read(ALPHA_TARGET)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("goal packet references R decision packet", "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md" in goal)
    audit.check("outer source-probe packet references R decision packet", "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md" in source_probe_decision)
    audit.check("R target remains support-only", "does not ratify R" in r_target)
    audit.check("S_l bridge remains conditional", "If `S_l` is" in sl_bridge or "if `S_l` is" in sl_bridge)
    audit.check(
        "lepton scale probe names y_scale open 1/256 target",
        "y_scale" in lepton_scale and "1/256" in lepton_scale and "residual open gate" in lepton_scale,
    )
    audit.check("D17 separability names 1/sqrt(2)", "1/sqrt(2)" in d17_sep)
    audit.check("source-coupled support names derivative attachment", "dS_lep/dj_c = h * B_lep * O_c" in source_coupled)
    audit.check("shape selector chooses sigma", "(h*j_c)/H" in shape_selector and "Q1-Q4" in shape_selector)
    audit.check("P decision remains sibling only", "No derivation or ratification of F, L, or R" in p_decision)
    audit.check("F decision remains sibling only", "No derivation or ratification of L, P, or R" in f_decision)
    audit.check("L decision remains sibling only", "No derivation or ratification of F, P, or R" in l_decision)
    audit.check("R decision references R no-go", R_NO_GO.name in note and "source-readout target remains needed" in note)
    audit.check("R no-go keeps R unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in r_no_go and "R_CLAUSE_RETAINED" in r_no_go)
    audit.check("projective section names L1 sigma", "sigma([j])_c = j_c / sum_d j_d" in projective_section)
    audit.check("Schur route keeps y0 separate", "y_0" in schur and "does not derive" in schur)
    audit.check("A3 remains downstream", "C_A3" in a3 and "source readout" in a3)
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
        "No derivation or ratification of the five R content subclauses.",
        "No derivation or ratification of R.",
        "No derivation or ratification of F, L, or P.",
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
        "This packet ratifies R",
        "R is retained",
        "The R clause is retained",
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
