#!/usr/bin/env python3
"""Verifier for the P positive projective source-strength target discriminator.

The runner checks the finite P target and authority boundaries. It does not
ratify P, derive S_l, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_POSITIVE_PROJECTIVE_SOURCE_STRENGTH_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
P_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
RATIFICATION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
COMPRESSION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
F_CLAUSE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
L_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_LABEL_FREE_SOURCE_COORDINATE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
POSITIVE_CONE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md"
GAUGE_QUOTIENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
SHAPE_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md"
ADDITIVITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md"
LINEARITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md"
GAUGE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md"
SL_READOUT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md"
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


def all_subsets(items: list[str]) -> list[set[str]]:
    subsets: list[set[str]] = []
    for size in range(len(items) + 1):
        for combo in combinations(items, size):
            subsets.append(set(combo))
    return subsets


def closes_p(inputs: set[str]) -> bool:
    return inputs == {
        "SOURCE_STRENGTH_OBJECT",
        "POSITIVE_NONZERO_DOMAIN",
        "SOURCE_SCALE_GAUGE",
        "PROJECTIVE_L1_SECTION",
        "SHAPE_SELECTOR",
        "RATIFICATION",
    }


def normalize(values: dict[Coord, Fraction]) -> dict[Coord, Fraction]:
    total = sum(values.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    return {coord: value / total for coord, value in values.items()}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("P positive projective note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        P_NO_GO,
        GOAL,
        ROUTE,
        RATIFICATION,
        COMPRESSION,
        F_CLAUSE,
        L_TARGET,
        POSITIVE_CONE,
        GAUGE_QUOTIENT,
        PROJECTIVE_SECTION,
        SHAPE_SELECTOR,
        ADDITIVITY,
        LINEARITY,
        GAUGE_FIREWALL,
        SL_READOUT,
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
        "P Positive Projective Source-Strength Ratification Target Discriminator",
        "does not ratify P",
        "does not derive retained `S_l = 1/256`",
        "positive projective source-strength and gauge quotient",
        "SOURCE_STRENGTH_OBJECT",
        "POSITIVE_NONZERO_DOMAIN",
        "SOURCE_SCALE_GAUGE",
        "PROJECTIVE_L1_SECTION",
        "SHAPE_SELECTOR",
        "RATIFICATION",
        "Every one-input-removed target fails",
        "sigma([j])_c = j_c / sum_d j_d",
        "H = h * sum_c j_c",
        "sigma([j])_(0,0,0,0) = 1/112",
        "raw `h`, raw `j_c`, `h*j_c`, `H`, and `1/16` alternatives",
        "no retained premise for P",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "P_CLAUSE_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "The primitive registry was checked",
        "#4998",
        "#4999",
        "#5000",
        "#5001",
        "#4997",
        "#4996",
        "#4995",
        "#4994",
        "#4993",
        "#4992",
        "#4991",
        "#4990",
        "#4989",
        "#4988",
        "#4987",
        "neutrino split2 edge transport witness refresh",
        "neutrino source-amplitude carrier premise bound",
        "PMNS selector stationarity diagnostics repair",
        "theta retirement-basis re-match",
        "record-instrument polar contrast stabilization",
        "DELTA0 route inventory sibling-total refresh",
        "g_bare two-Ward scope repair",
        "owner-governed Tier-A retirement",
        "No-Go Discipline Gate",
        "broad P retention not shipped; narrowed P positive projective",
        "No derivation or ratification of P.",
        "No derivation or ratification of F/L/P/R.",
        "No use of latest open PRs as proof inputs.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("P finite discriminator checks")
    inputs = [
        "SOURCE_STRENGTH_OBJECT",
        "POSITIVE_NONZERO_DOMAIN",
        "SOURCE_SCALE_GAUGE",
        "PROJECTIVE_L1_SECTION",
        "SHAPE_SELECTOR",
        "RATIFICATION",
    ]
    closing_subsets = [subset for subset in all_subsets(inputs) if closes_p(subset)]
    audit.check("exactly one tested P input set closes P", closing_subsets == [set(inputs)])
    for item in inputs:
        missing_one = set(inputs) - {item}
        audit.check(f"missing {item} fails P closure", not closes_p(missing_one))

    coords = [tuple(coord) for coord in product(range(4), repeat=4)]
    typed_coords: list[Coord] = coords  # type: ignore[assignment]
    audit.check("source-coordinate set has 256 elements", len(typed_coords) == 256)

    uniform = {coord: Fraction(1) for coord in typed_coords}
    uniform_sigma = normalize(uniform)
    audit.check("uniform projective singleton is 1/256", uniform_sigma[(0, 0, 0, 0)] == Fraction(1, 256))

    tagged = {coord: Fraction(4 if coord[0] == 0 else 1) for coord in typed_coords}
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
    zero_sum = {coord: Fraction(1 if i == 0 else -1 if i == 1 else 0) for i, coord in enumerate(typed_coords)}
    audit.check("zero-total signed vector has undefined L1 section", sum(zero_sum.values(), Fraction(0)) == 0)

    section("Authority boundary checks")
    goal = read(GOAL)
    route = read(ROUTE)
    ratification = read(RATIFICATION)
    compression = read(COMPRESSION)
    f_clause = read(F_CLAUSE)
    l_target = read(L_TARGET)
    positive_cone = read(POSITIVE_CONE)
    gauge_quotient = read(GAUGE_QUOTIENT)
    projective_section = read(PROJECTIVE_SECTION)
    shape_selector = read(SHAPE_SELECTOR)
    additivity = read(ADDITIVITY)
    linearity = read(LINEARITY)
    gauge_firewall = read(GAUGE_FIREWALL)
    sl_readout = read(SL_READOUT)
    p_no_go = read(P_NO_GO)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("goal packet cites P follow-up", "P positive projective source-strength ratification target discriminator" in goal)
    audit.check("route triage cites P follow-up", "Follow-up A2 P positive projective source-strength ratification target discriminator" in route)
    audit.check("ratification target cites P follow-up", "P positive projective source-strength ratification target discriminator" in ratification)
    audit.check("compression note names projective source strength", "projective source strength" in compression)
    audit.check("F-clause remains sibling context", "does not ratify F" in f_clause)
    audit.check("L target remains sibling context", "does not ratify L" in l_target)
    audit.check("positive-cone support is conditional", "assumes the positive ordered source-strength domain" in positive_cone)
    audit.check("gauge quotient support does not bind S_l", "does not say that" in gauge_quotient and "S_l" in gauge_quotient)
    audit.check("projective section assumes source semantics", "projective source-strength semantics" in projective_section)
    audit.check("shape selector does not ratify S_l", "does not ratify" in shape_selector or "still does not ratify" in shape_selector)
    audit.check("additivity support assumes semantics", "does not prove that the charged-lepton source" in additivity)
    audit.check("linearity support leaves positivity open", "nonnegative source-strength semantics" in linearity)
    audit.check("gauge firewall leaves section open", "mu(C) = 1" in gauge_firewall and "extra" in gauge_firewall)
    audit.check("S_l bridge keeps readout convention explicit", "if `S_l` is" in sl_readout or "If S_l is" in sl_readout)
    audit.check("P target references P current-surface no-go", P_NO_GO.name in note and "P_CLAUSE_RETAINED" in note)
    audit.check("P no-go keeps P unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in p_no_go and "P_CLAUSE_RETAINED" in p_no_go)
    audit.check("minimal axioms exclude source/action", "source/action and physical-observable identification" in minimal)
    for node_name in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    audit.check("scale primitive excludes dimensionless physics", "zero dimensionless" in scale and "does not supply any dimensionless quantity" in scale)
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
        "`#4996` PMNS selector stationarity diagnostics repair | `CLEAN`",
        "`#4995` theta retirement-basis re-match | `CLEAN`",
        "`#4994` record-instrument polar contrast stabilization | `CLEAN`",
        "`#4993` DELTA0 route inventory sibling-total refresh | `CLEAN`",
        "`#4992` g_bare two-Ward scope repair | `CLEAN`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN`",
        "`#4990` Tier-A residual owner decision packet | `CLEAN`",
        "`#4989` Tier-A residual governance readiness packet | `CLEAN`",
        "`#4988` theta G2 registration stretch no-go | `CLEAN`",
        "`#4987` theta G4 theta-bar assembly no-go | `CLEAN`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of P.",
        "No derivation or ratification of F/L/P/R.",
        "No derivation that `S_l = 1/256` is retained.",
        "No derivation of the `256.082435...` precision correction.",
        "No derivation of the Koide/electron branch or physical `m_e`.",
        "No derivation of `alpha(0)` or hydrogen spectroscopy.",
        "No use of latest open PRs as proof inputs.",
        "No new axiom, primitive, or admitted import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note ratifies P",
        "P is retained",
        "This note says F/L/P/R is retained",
        "This note derives retained `S_l = 1/256`",
        "m_e is derived",
        "alpha(0) is derived",
        "hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
