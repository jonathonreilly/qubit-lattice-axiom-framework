#!/usr/bin/env python3
"""Verifier for the R S_l readout identity ratification target discriminator.

The runner checks the finite R target and authority boundaries. It does not
ratify R, derive S_l, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_S_L_READOUT_IDENTITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
RATIFICATION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
COMPRESSION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
SL_BRIDGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
D17_SEP = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
SHAPE_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md"
P_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_POSITIVE_PROJECTIVE_SOURCE_STRENGTH_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
R_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
SCHUR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SCHUR_TWO_SCALE_FIREWALL_2026-07-04.md"
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


def all_subsets(items: list[str]) -> list[set[str]]:
    subsets: list[set[str]] = []
    for size in range(len(items) + 1):
        for combo in combinations(items, size):
            subsets.append(set(combo))
    return subsets


def closes_r(inputs: set[str]) -> bool:
    return inputs == {
        "SCALE_SYMBOL_CONTEXT",
        "SOURCE_COEFFICIENT_CONTEXT",
        "COMMON_FRONT_NONZERO",
        "NORMALIZED_SINGLETON_CANDIDATE",
        "SOURCE_READOUT_LICENSE",
        "RATIFICATION",
    }


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
    audit.check("R S_l readout target note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        RATIFICATION,
        COMPRESSION,
        SL_BRIDGE,
        LEPTON_SCALE,
        D17_SEP,
        SOURCE_COUPLED,
        SHAPE_SELECTOR,
        P_TARGET,
        R_NO_GO,
        PROJECTIVE_SECTION,
        SCHUR,
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
        "R S_l Readout Identity Ratification Target Discriminator",
        "does not ratify R",
        "does not derive retained `S_l = 1/256`",
        "SCALE_SYMBOL_CONTEXT",
        "SOURCE_COEFFICIENT_CONTEXT",
        "COMMON_FRONT_NONZERO",
        "NORMALIZED_SINGLETON_CANDIDATE",
        "SOURCE_READOUT_LICENSE",
        "RATIFICATION",
        "Every one-input-removed target fails",
        "S_l = sigma([j])_c",
        "sigma([j])_c = (h*j_c)/H",
        "sigma([j])_c = j_c / sum_d j_d",
        "raw `h`, raw `j_c`, `h*j_c`, `H`, and `1/16` alternatives",
        "lattice `y_0 = 1/256`",
        "empirical comparator reciprocal `1/256.082435...`",
        "no source-readout identity",
        "no retained R",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_POSITIVE_PROJECTIVE_SOURCE_STRENGTH_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "source-readout target remains needed",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SCHUR_TWO_SCALE_FIREWALL_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md",
        "The primitive registry was checked",
        "#5004",
        "#5003",
        "#5002",
        "#5001",
        "#5000",
        "#4999",
        "#4998",
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
        "hadron lane1 record-invariance companion refresh",
        "axiom-first record-invariance companion refresh",
        "Wilson descendant Schur entropy witness stabilization",
        "neutrino split2 edge transport witness refresh",
        "No-Go Discipline Gate",
        "broad R retention not shipped; narrowed R `S_l` readout identity",
        "No derivation or ratification of R.",
        "No derivation or ratification of F/L/P/R.",
        "No use of latest open PRs as proof inputs.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("R finite discriminator checks")
    inputs = [
        "SCALE_SYMBOL_CONTEXT",
        "SOURCE_COEFFICIENT_CONTEXT",
        "COMMON_FRONT_NONZERO",
        "NORMALIZED_SINGLETON_CANDIDATE",
        "SOURCE_READOUT_LICENSE",
        "RATIFICATION",
    ]
    closing_subsets = [subset for subset in all_subsets(inputs) if closes_r(subset)]
    audit.check("exactly one tested R input set closes R", closing_subsets == [set(inputs)])
    for item in inputs:
        missing_one = set(inputs) - {item}
        audit.check(f"missing {item} fails R closure", not closes_r(missing_one))

    coords = [tuple(coord) for coord in product(range(4), repeat=4)]
    typed_coords: list[Coord] = coords  # type: ignore[assignment]
    audit.check("source-coordinate set has 256 elements", len(typed_coords) == 256)

    uniform = {coord: Fraction(1) for coord in typed_coords}
    sigma = normalize(uniform)
    coord = (0, 0, 0, 0)
    audit.check("uniform normalized singleton is 1/256", sigma[coord] == Fraction(1, 256))

    front = Fraction(7, 11)
    source_coeff = front * sigma[coord]
    audit.check("common front times singleton forms source coefficient", source_coeff == front * Fraction(1, 256))
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
    tagged = {c: Fraction(4 if c[0] == 0 else 1) for c in typed_coords}
    total = sum(tagged.values(), Fraction(0))
    tagged_scaled = {c: lam * value for c, value in tagged.items()}
    total_scaled = sum(tagged_scaled.values(), Fraction(0))
    audit.check("raw h changes under source-scale gauge", h / lam != h)
    audit.check("raw j_c changes under source-scale gauge", tagged_scaled[coord] != tagged[coord])
    audit.check("h*j_c is front-bearing, not normalized singleton", h * tagged[coord] != tagged[coord] / total)
    audit.check("H is global front, not singleton", h * total != tagged[coord] / total)
    audit.check("sigma survives source-scale gauge", tagged_scaled[coord] / total_scaled == tagged[coord] / total)

    y0_lattice = Fraction(1, 4) / Fraction(64)
    comparator = Fraction(1_000_000, 256_082_435)
    audit.check("lattice y0 is numerically 1/256 but separate route", y0_lattice == Fraction(1, 256))
    audit.check("empirical comparator reciprocal differs from exact 1/256", comparator != Fraction(1, 256))

    section("Authority boundary checks")
    goal = read(GOAL)
    route = read(ROUTE)
    ratification = read(RATIFICATION)
    compression = read(COMPRESSION)
    sl_bridge = read(SL_BRIDGE)
    lepton_scale = read(LEPTON_SCALE)
    d17_sep = read(D17_SEP)
    source_coupled = read(SOURCE_COUPLED)
    shape_selector = read(SHAPE_SELECTOR)
    p_target = read(P_TARGET)
    r_no_go = read(R_NO_GO)
    projective_section = read(PROJECTIVE_SECTION)
    schur = read(SCHUR)
    a3 = read(A3)
    koide = read(KOIDE)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("goal packet cites R target", "R `S_l` readout identity ratification target discriminator" in goal)
    audit.check("route triage cites R bridge", "Follow-up A2 `S_l` readout identity bridge support" in route)
    audit.check("ratification target cites R target", "R `S_l` readout identity ratification target discriminator" in ratification)
    audit.check("compression note names S_l readout target", "S_l" in compression and "source-readout clause" in compression)
    audit.check("S_l bridge remains conditional", "If `S_l` is" in sl_bridge or "if `S_l` is" in sl_bridge)
    audit.check("lepton scale probe names y_scale", "y_scale" in lepton_scale and "1/256" in lepton_scale)
    audit.check("D17 separability names 1/sqrt(2)", "1/sqrt(2)" in d17_sep)
    audit.check("source-coupled support names derivative attachment", "dS_lep/dj_c = h * B_lep * O_c" in source_coupled)
    audit.check("shape selector chooses sigma", "(h*j_c)/H" in shape_selector and "Q1-Q4" in shape_selector)
    audit.check("P target remains sibling context", "does not ratify P" in p_target)
    audit.check("R target references R no-go", R_NO_GO.name in note and "source-readout target remains needed" in note)
    audit.check("R no-go keeps R unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in r_no_go and "R_CLAUSE_RETAINED" in r_no_go)
    audit.check("projective section names L1 sigma", "sigma([j])_c = j_c / sum_d j_d" in projective_section)
    audit.check("Schur route keeps y0 separate", "S_l = y_0_lattice" in schur and "does not derive" in schur)
    audit.check("A3 remains downstream", "C_A3" in a3 and "source readout" in a3)
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
        "No derivation or ratification of R.",
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
        "This note ratifies R",
        "R is now retained",
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
