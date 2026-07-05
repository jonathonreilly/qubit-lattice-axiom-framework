#!/usr/bin/env python3
"""Verifier for the lepton P-clause current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply P_CLAUSE_RETAINED. It preserves the positive projective
source-strength route and keeps exact S_l, m_e, alpha(0), Rydberg, and
hydrogen downstream.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
SOURCE_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
L_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
P_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_POSITIVE_PROJECTIVE_SOURCE_STRENGTH_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
POSITIVE_CONE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md"
GAUGE_QUOTIENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
SHAPE_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md"
ADDITIVITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md"
LINEARITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md"
GAUGE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md"
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
    "P_CLAUSE_TEXT_LOCK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

P_SUBCLAUSES = {
    "SOURCE_STRENGTH_OBJECT",
    "POSITIVE_NONZERO_DOMAIN",
    "SOURCE_SCALE_GAUGE",
    "PROJECTIVE_L1_SECTION",
    "SHAPE_SELECTOR",
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


def closes_p_clause(contract: set[str], subclauses: set[str]) -> bool:
    return CONTRACT_INPUTS <= contract and P_SUBCLAUSES <= subclauses


def closes_outer_source_side(clauses: set[str]) -> bool:
    return {"F", "L", "P", "R"} <= clauses


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


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
        GOAL,
        SOURCE_PACKET,
        EXACT_SOURCE_NO_GO,
        F_NO_GO,
        L_NO_GO,
        P_DECISION,
        P_TARGET,
        POSITIVE_CONE,
        GAUGE_QUOTIENT,
        PROJECTIVE_SECTION,
        SHAPE_SELECTOR,
        ADDITIVITY,
        LINEARITY,
        GAUGE_FIREWALL,
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
        "P-Clause Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "P_CLAUSE_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "SOURCE_STRENGTH_OBJECT",
        "POSITIVE_NONZERO_DOMAIN",
        "SOURCE_SCALE_GAUGE",
        "PROJECTIVE_L1_SECTION",
        "SHAPE_SELECTOR",
        "P_CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "source-shape singleton = sigma([j])_c",
        "sigma([j])_c = j_c / sum_d j_d",
        "C = {0,1,2,3}^4",
        "|C| = 4^4 = 256",
        "sigma([1])_c = 1/256",
        "sigma([j])_(0,0,0,0) = 1/112",
        "P alone does not force uniformity",
        "h*j_c",
        "`1/16` projection/RN/Fisher alternatives",
        "source_strength_weighting_primitive",
        "projective_source_strength_primitive",
        "p_clause_primitive",
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
        "broad P no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("P-clause predicate checks")
    full_contract = set(CONTRACT_INPUTS)
    full_subclauses = set(P_SUBCLAUSES)
    audit.check("full P contract accepts P clause", closes_p_clause(full_contract, full_subclauses))
    for missing in sorted(CONTRACT_INPUTS):
        reduced = set(CONTRACT_INPUTS)
        reduced.remove(missing)
        audit.check(f"P clause fails without contract input {missing}", not closes_p_clause(reduced, full_subclauses))
    for missing in sorted(P_SUBCLAUSES):
        reduced = set(P_SUBCLAUSES)
        reduced.remove(missing)
        audit.check(f"P clause fails without subclause {missing}", not closes_p_clause(full_contract, reduced))

    accepted_subsets = [
        (contract, subclauses)
        for contract in all_subsets(CONTRACT_INPUTS)
        for subclauses in all_subsets(P_SUBCLAUSES)
        if closes_p_clause(contract, subclauses)
    ]
    audit.check("only full P contract/subclause subset closes P", accepted_subsets == [(full_contract, full_subclauses)])
    audit.check("P alone does not close outer source side", not closes_outer_source_side({"P"}))
    audit.check("F/L/P/R closes outer source-side predicate model", closes_outer_source_side({"F", "L", "P", "R"}))

    section("Finite P witness checks")
    coords = coordinates()
    audit.check("source-coordinate set has 4^4 = 256 elements", len(coords) == 256)
    uniform = {coord: Fraction(1) for coord in coords}
    uniform_sigma = normalize(uniform)
    audit.check("uniform projective singleton is 1/256", uniform_sigma[(0, 0, 0, 0)] == Fraction(1, 256))
    tagged = {coord: Fraction(4 if coord[0] == 0 else 1) for coord in coords}
    tagged_sigma = normalize(tagged)
    audit.check("positive nonuniform singleton is 1/112", tagged_sigma[(0, 0, 0, 0)] == Fraction(1, 112))
    audit.check("P alone does not force uniformity", tagged_sigma[(0, 0, 0, 0)] != Fraction(1, 256))

    h = Fraction(5, 1)
    lam = Fraction(7, 1)
    coord = (0, 0, 0, 0)
    j_coord = tagged[coord]
    total = sum(tagged.values(), Fraction(0))
    h_prime = h / lam
    tagged_prime = {c: lam * value for c, value in tagged.items()}
    total_prime = sum(tagged_prime.values(), Fraction(0))
    audit.check("raw h changes under source-scale gauge", h_prime != h)
    audit.check("raw j_c changes under source-scale gauge", tagged_prime[coord] != j_coord)
    audit.check("H is gauge invariant", h_prime * total_prime == h * total)
    audit.check("sigma is gauge invariant", tagged_prime[coord] / total_prime == tagged[coord] / total)
    audit.check("h*j_c is gauge invariant", h_prime * tagged_prime[coord] == h * tagged[coord])
    audit.check("h*j_c is not normalized singleton", h * tagged[coord] != tagged_sigma[coord])
    audit.check("H is not singleton source shape", h * total != tagged_sigma[coord])
    audit.check("RN/Fisher 1/16 differs from L1 singleton 1/256", Fraction(1, 16) != Fraction(1, 256))

    signed = dict(uniform)
    signed[coord] = Fraction(-1)
    signed_total = sum(signed.values(), Fraction(0))
    audit.check("signed vector can have positive total", signed_total > 0)
    audit.check("signed vector gives negative normalized singleton", signed[coord] / signed_total < 0)
    zero_sum = {c: Fraction(1 if i == 0 else -1 if i == 1 else 0) for i, c in enumerate(coords)}
    audit.check("zero-total signed vector has undefined L1 section", sum(zero_sum.values(), Fraction(0)) == 0)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    source_packet = read(SOURCE_PACKET)
    exact_source = read(EXACT_SOURCE_NO_GO)
    f_no_go = read(F_NO_GO)
    l_no_go = read(L_NO_GO)
    p_decision = read(P_DECISION)
    p_target = read(P_TARGET)
    positive_cone = read(POSITIVE_CONE)
    gauge_quotient = read(GAUGE_QUOTIENT)
    projective_section = read(PROJECTIVE_SECTION)
    shape_selector = read(SHAPE_SELECTOR)
    additivity = read(ADDITIVITY)
    linearity = read(LINEARITY)
    gauge_firewall = read(GAUGE_FIREWALL)
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

    audit.check("P decision remains support-only", "does not ratify P" in p_decision and "P_CLAUSE_RETAINED" in p_decision)
    audit.check("P target remains unratified", "does not ratify P" in p_target and "raw `h`, raw `j_c`, `h*j_c`, `H`" in p_target)
    audit.check("positive-cone support remains conditional", "assumes the positive ordered source-strength domain" in positive_cone)
    audit.check("gauge quotient support does not bind S_l", "does not say that" in gauge_quotient and "S_l" in gauge_quotient)
    audit.check("projective section assumes source semantics", "projective source-strength semantics" in projective_section)
    audit.check("shape selector does not ratify S_l", "does not ratify" in shape_selector or "still does not ratify" in shape_selector)
    audit.check("additivity support assumes semantics", "does not prove that the charged-lepton source" in additivity)
    audit.check("linearity support leaves positivity open", "nonnegative source-strength semantics" in linearity)
    audit.check("gauge firewall leaves section open", "mu(C) = 1" in gauge_firewall and "extra" in gauge_firewall)
    audit.check("F no-go remains sibling context", "F_CLAUSE_RETAINED" in f_no_go)
    audit.check("L no-go remains sibling context", "L_CLAUSE_RETAINED" in l_no_go)
    audit.check("R decision remains downstream", "does not ratify R" in r_decision)
    audit.check("A3 remains downstream", "A3_PRECISION_PLACEMENT_RETAINED" in a3_packet)
    audit.check("physical electron remains downstream", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in physical_electron)

    audit.check("goal packet can reference P decision", "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md" in goal)
    audit.check("source-probe packet can reference P decision", "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md" in source_packet)
    audit.check("exact source no-go can reference P decision", "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md" in exact_source)

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
        "source_strength_weighting_primitive",
        "projective_source_strength_primitive",
        "p_clause_primitive",
        "source_probe_interface_primitive",
        "source_strength_normalization_primitive",
        "s_l_readout_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered P shortcut: {absent}", absent not in registry_text)

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
        "No derivation or ratification of `P_CLAUSE_RETAINED`.",
        "No derivation or ratification of the five P content subclauses.",
        "No derivation or ratification of F, L, or R.",
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
        "This note ratifies P",
        "This note derives P",
        "P_CLAUSE_RETAINED is supplied",
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
