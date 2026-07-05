#!/usr/bin/env python3
"""Verifier for the L label-free source-coordinate target discriminator.

The runner checks the finite source-coordinate target and authority boundaries
for L. It does not ratify L, derive S_l, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_LABEL_FREE_SOURCE_COORDINATE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
L_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
RATIFICATION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
COMPRESSION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
F_CLAUSE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
SOURCE_NATURALITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_NATURALITY_LABEL_FREE_LICENSE_SUPPORT_2026-07-04.md"
UNFIXED_CHOICE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COORDINATE_UNFIXED_CHOICE_LABEL_FREE_SUPPORT_2026-07-04.md"
INVARIANCE_BRIDGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_INVARIANCE_BRIDGE_SUPPORT_2026-07-04.md"
UNIFORM_RAY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md"
SOURCE_SLOT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md"
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


def closes_l(inputs: set[str]) -> bool:
    return inputs == {"SOURCE_INTERFACE", "FRAME_RELABELING", "LABEL_FREE_LICENSE", "TAG_EXCLUSION", "RATIFICATION"}


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
    audit.check("L label-free note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        L_NO_GO,
        GOAL,
        ROUTE,
        RATIFICATION,
        COMPRESSION,
        F_CLAUSE,
        SOURCE_NATURALITY,
        UNFIXED_CHOICE,
        INVARIANCE_BRIDGE,
        UNIFORM_RAY,
        SOURCE_SLOT,
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
        "L Label-Free Source-Coordinate Ratification Target Discriminator",
        "does not ratify L",
        "does not derive retained `S_l = 1/256`",
        "label-free source-coordinate convention",
        "C = {0,1,2,3}^4",
        "J(j) = sum_{c in C} j_c O_c",
        "rho_g J(j) = J(rho_g j)",
        "[j] = [rho_g j]",
        "SOURCE_INTERFACE",
        "FRAME_RELABELING",
        "LABEL_FREE_LICENSE",
        "TAG_EXCLUSION",
        "RATIFICATION",
        "Every one-input-removed target fails",
        "coordinate-tagged nonuniform rays are not zero-import law-level selectors",
        "sigma([j])_(0,0,0,0) = 1/112",
        "no retained premise for L",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_NATURALITY_LABEL_FREE_LICENSE_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COORDINATE_UNFIXED_CHOICE_LABEL_FREE_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_INVARIANCE_BRIDGE_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "L_CLAUSE_RETAINED",
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
        "#4986",
        "#4985",
            "neutrino source-amplitude carrier premise bound",
            "neutrino split2 edge transport witness refresh",
            "PMNS selector stationarity diagnostics repair",
        "theta retirement-basis re-match",
        "record-instrument polar contrast stabilization",
        "DELTA0 route inventory sibling-total refresh",
        "g_bare two-Ward scope repair",
        "owner-governed Tier-A retirement",
        "No-Go Discipline Gate",
        "broad L retention not shipped; narrowed L source-coordinate",
        "No derivation or ratification of L.",
        "No derivation or ratification of F/L/P/R.",
        "No use of latest open PRs as proof inputs.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("L finite discriminator checks")
    inputs = ["SOURCE_INTERFACE", "FRAME_RELABELING", "LABEL_FREE_LICENSE", "TAG_EXCLUSION", "RATIFICATION"]
    closing_subsets = [subset for subset in all_subsets(inputs) if closes_l(subset)]
    audit.check("exactly one tested L input set closes L", closing_subsets == [set(inputs)])
    for item in inputs:
        missing_one = set(inputs) - {item}
        audit.check(f"missing {item} fails L closure", not closes_l(missing_one))

    coords = list(product(range(4), repeat=4))
    typed_coords: list[Coord] = [tuple(coord) for coord in coords]  # type: ignore[list-item]
    audit.check("source-coordinate set has 256 elements", len(typed_coords) == 256)
    generators = [swap_value(slot, 0, value) for slot in range(4) for value in [1, 2, 3]]
    full_orbit = orbit((0, 0, 0, 0), generators)
    audit.check("local coordinate relabelings act transitively on C", len(full_orbit) == 256)
    uniform = {coord: Fraction(1) for coord in typed_coords}
    uniform_sigma = normalize(uniform)
    audit.check("uniform label-free singleton is 1/256", uniform_sigma[(0, 0, 0, 0)] == Fraction(1, 256))
    tagged = {coord: Fraction(4 if coord[0] == 0 else 1) for coord in typed_coords}
    tagged_sigma = normalize(tagged)
    audit.check("coordinate-tagged singleton is 1/112", tagged_sigma[(0, 0, 0, 0)] == Fraction(1, 112))
    relabeled_tagged = {swap_value(0, 0, 1)(coord): value for coord, value in tagged.items()}
    audit.check("coordinate-tagged ray changes under source-coordinate relabeling", relabeled_tagged != tagged)
    audit.check("coordinate-tagged singleton differs from 1/256", tagged_sigma[(0, 0, 0, 0)] != Fraction(1, 256))

    section("Authority boundary checks")
    goal = read(GOAL)
    route = read(ROUTE)
    ratification = read(RATIFICATION)
    compression = read(COMPRESSION)
    f_clause = read(F_CLAUSE)
    source_naturality = read(SOURCE_NATURALITY)
    unfixed_choice = read(UNFIXED_CHOICE)
    invariance_bridge = read(INVARIANCE_BRIDGE)
    uniform_ray = read(UNIFORM_RAY)
    source_slot = read(SOURCE_SLOT)
    l_no_go = read(L_NO_GO)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("goal packet cites L follow-up", "L label-free source-coordinate ratification target discriminator" in goal)
    audit.check("route triage cites L follow-up", "Follow-up A2 L label-free source-coordinate ratification target discriminator" in route)
    audit.check("ratification target cites L follow-up", "L label-free source-coordinate ratification target discriminator" in ratification)
    audit.check("compression note names label-free interface", "label-free charged-lepton full-cell source-probe interface" in compression)
    audit.check("F-clause remains sibling context", "does not ratify F" in f_clause)
    audit.check("source naturality support assumes label-free license", "does not prove the interface is label-free" in source_naturality)
    audit.check("unfixed-choice support is conditional", "#4952" in unfixed_choice and "closed without merge" in unfixed_choice)
    audit.check("invariance bridge assumes naturality", "does not derive that naturality rule" in flat(invariance_bridge))
    audit.check("uniform ray support assumes W5b", "W5b" in uniform_ray and "hypothesis" in uniform_ray)
    audit.check("source-slot support does not derive source family", "derive that source family" in source_slot)
    audit.check("L target references L current-surface no-go", L_NO_GO.name in note and "L_CLAUSE_RETAINED" in note)
    audit.check("L no-go keeps L unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in l_no_go and "L_CLAUSE_RETAINED" in l_no_go)
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
        "`#4986` AC R-eta h-class stretch no-go | `CLEAN`",
        "`#4985` AC R-eta h-unit primitive no-go | `CLEAN`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of L.",
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
        "This note ratifies L",
        "L is retained",
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
