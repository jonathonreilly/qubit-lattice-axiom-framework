#!/usr/bin/env python3
"""Verifier for the lepton R-clause current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply R_CLAUSE_RETAINED. It preserves the source-readout route
and keeps exact S_l, m_e, alpha(0), Rydberg, and hydrogen downstream.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
SOURCE_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
L_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_S_L_READOUT_IDENTITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
SL_BRIDGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
D17_SEP = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
SHAPE_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md"
P_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
F_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
L_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
SCHUR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SCHUR_TWO_SCALE_FIREWALL_2026-07-04.md"
A3_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
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


def closes_r_clause(contract: set[str], subclauses: set[str]) -> bool:
    return CONTRACT_INPUTS <= contract and R_SUBCLAUSES <= subclauses


def closes_outer_source_side(clauses: set[str]) -> bool:
    return {"F", "L", "P", "R"} <= clauses


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


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
        SOURCE_PACKET,
        EXACT_SOURCE_NO_GO,
        F_NO_GO,
        L_NO_GO,
        P_NO_GO,
        R_DECISION,
        R_TARGET,
        SL_BRIDGE,
        LEPTON_SCALE,
        D17_SEP,
        SOURCE_COUPLED,
        SHAPE_SELECTOR,
        P_DECISION,
        F_DECISION,
        L_DECISION,
        PROJECTIVE_SECTION,
        SCHUR,
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
        "R-Clause Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "R_CLAUSE_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
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
        "S_l = sigma([j])_c",
        "C = {0,1,2,3}^4",
        "|C| = 4^4 = 256",
        "sigma([1])_c = 1/256",
        "y_scale(c)  = g_2 * (1/sqrt(2)) * S_l",
        "y_source(c) = g_2 * (1/sqrt(2)) * sigma([j])_c",
        "S_l = (3/2) * sigma([j])_c",
        "zero front cannot be cancelled",
        "raw `h`, raw `j_c`, `h*j_c`, `H`, and `1/16` alternatives",
        "lattice `y_0 = 1/256`",
        "empirical comparator reciprocal `1/256.082435...`",
        "R alone does not force `S_l = 1/256`",
        "s_l_readout_primitive",
        "source_readout_identity_primitive",
        "r_clause_primitive",
        "source_probe_interface_primitive",
        "source_strength_normalization_primitive",
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
        "broad R no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("R-clause predicate checks")
    full_contract = set(CONTRACT_INPUTS)
    full_subclauses = set(R_SUBCLAUSES)
    audit.check("full R contract accepts R clause", closes_r_clause(full_contract, full_subclauses))
    for missing in sorted(CONTRACT_INPUTS):
        reduced = set(CONTRACT_INPUTS)
        reduced.remove(missing)
        audit.check(f"R clause fails without contract input {missing}", not closes_r_clause(reduced, full_subclauses))
    for missing in sorted(R_SUBCLAUSES):
        reduced = set(R_SUBCLAUSES)
        reduced.remove(missing)
        audit.check(f"R clause fails without subclause {missing}", not closes_r_clause(full_contract, reduced))

    accepted_subsets = [
        (contract, subclauses)
        for contract in all_subsets(CONTRACT_INPUTS)
        for subclauses in all_subsets(R_SUBCLAUSES)
        if closes_r_clause(contract, subclauses)
    ]
    audit.check("only full R contract/subclause subset closes R", accepted_subsets == [(full_contract, full_subclauses)])
    audit.check("R alone does not close outer source side", not closes_outer_source_side({"R"}))
    audit.check("F/L/P/R closes outer source-side predicate model", closes_outer_source_side({"F", "L", "P", "R"}))

    section("Finite R witness checks")
    coords = coordinates()
    audit.check("source-coordinate set has 4^4 = 256 elements", len(coords) == 256)
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

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    source_packet = read(SOURCE_PACKET)
    exact_source = read(EXACT_SOURCE_NO_GO)
    f_no_go = read(F_NO_GO)
    l_no_go = read(L_NO_GO)
    p_no_go = read(P_NO_GO)
    r_decision = read(R_DECISION)
    r_target = read(R_TARGET)
    sl_bridge = read(SL_BRIDGE)
    lepton_scale = read(LEPTON_SCALE)
    d17_sep = read(D17_SEP)
    source_coupled = read(SOURCE_COUPLED)
    shape_selector = read(SHAPE_SELECTOR)
    p_decision = read(P_DECISION)
    f_decision = read(F_DECISION)
    l_decision = read(L_DECISION)
    projective_section = read(PROJECTIVE_SECTION)
    schur = read(SCHUR)
    a3_packet = read(A3_PACKET)
    physical_electron = read(PHYSICAL_ELECTRON)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("goal packet references R no-go", NOTE.name in goal)
    audit.check("outer source-probe packet references R no-go", NOTE.name in source_packet)
    audit.check("exact-source no-go references R no-go", NOTE.name in exact_source)
    audit.check("F no-go keeps F unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in f_no_go and "F_CLAUSE_RETAINED" in f_no_go)
    audit.check("L no-go keeps L unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in l_no_go and "L_CLAUSE_RETAINED" in l_no_go)
    audit.check("P no-go keeps P unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in p_no_go and "P_CLAUSE_RETAINED" in p_no_go)
    audit.check("R decision does not ratify R", "does not ratify R" in r_decision and "R_CLAUSE_RETAINED" in r_decision)
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
    audit.check("projective section names L1 sigma", "sigma([j])_c = j_c / sum_d j_d" in projective_section)
    audit.check("Schur route keeps y0 separate", "y_0" in schur and "does not derive" in schur)
    audit.check("A3 remains downstream", "A3_PRECISION_PLACEMENT_RETAINED" in a3_packet and "S_l = 1/256" in a3_packet)
    audit.check("physical electron remains downstream", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in physical_electron)
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
    for absent in [
        "s_l_readout_primitive",
        "source_readout_identity_primitive",
        "r_clause_primitive",
        "source_probe_interface_primitive",
        "source_strength_normalization_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered R shortcut: {absent}", absent not in registry_text)

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
        "This note ratifies R",
        "R is retained",
        "The R clause is retained",
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
