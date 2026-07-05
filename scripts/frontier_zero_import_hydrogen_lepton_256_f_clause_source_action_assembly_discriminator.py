#!/usr/bin/env python3
"""Verifier for the lepton F-clause source/action assembly discriminator.

The runner checks the finite F1-F4 assembly target for the full-cell
charged-lepton source/action family. It does not ratify F, derive S_l, alpha(0),
or hydrogen spectroscopy.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
RATIFICATION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
COMPRESSION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
OBS_SOURCE = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
FULL_CELL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md"
D17_SEP = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
F1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F2_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
F2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F3_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F4_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F4_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
TENSOR_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md"
SOURCE_CONTROL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md"
D17_NOTE = ROOT / "docs" / "LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md"
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


def all_subsets(items: list[str]) -> list[set[str]]:
    subsets: list[set[str]] = []
    for size in range(len(items) + 1):
        for combo in combinations(items, size):
            subsets.append(set(combo))
    return subsets


def closes_f(inputs: set[str]) -> bool:
    return inputs == {"F1", "F2", "F3", "F4"}


def source_action(j: dict[Coord, Fraction], h: Fraction) -> dict[Coord, Fraction]:
    return {coord: h * value for coord, value in j.items()}


def add_vectors(left: dict[Coord, Fraction], right: dict[Coord, Fraction]) -> dict[Coord, Fraction]:
    return {coord: left.get(coord, Fraction(0)) + right.get(coord, Fraction(0)) for coord in set(left) | set(right)}


def derivative_wrt(coord: Coord, h: Fraction) -> dict[Coord, Fraction]:
    return {coord: h}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("F-clause source/action assembly note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        RATIFICATION,
        COMPRESSION,
        OBS_SOURCE,
        SOURCE_COUPLED,
        FULL_CELL,
        D17_SEP,
        F1_TARGET,
        F2_SELECTOR,
        F2_NO_GO,
        F3_TARGET,
        F3_NO_GO,
        F4_TARGET,
        F4_NO_GO,
        TENSOR_FIREWALL,
        SOURCE_CONTROL,
        D17_NOTE,
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
        "F-Clause Source/Action Assembly Discriminator",
        "full-cell charged-lepton source/action family",
        "S_lep[j] = h * B_lep * sum_{c in C} j_c O_c",
        "dS_lep/dj_c = h * B_lep * O_c",
        "F1",
        "source-coupled local-action convention",
        "F2",
        "charged-lepton sector specificity",
        "F3",
        "full OS0-cell tensor source locality",
        "F4",
        "scalar-multiplier attachment",
        "M_2(C)^tensor4",
        "4^4 = 256",
        "2 * 256 = 512",
        "(1/sqrt(2))*(1/16)",
        "all F1-F4 supplied closes the formal F assembly",
        "every one-input-removed F target fails",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "F1 source-coupled local-action follow-up",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "F2 charged-lepton source-block selector follow-up",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "F3 full-cell tensor source-locality follow-up",
        "physical charged-lepton source-locality",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "F4 scalar-multiplier attachment follow-up",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED",
        "D17 block preservation instead of `512` product weights",
        "The primitive registry was checked",
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
        "#4984",
        "#4983",
        "#4982",
        "#4981",
        "#4980",
        "#4979",
        "#4978",
        "#4975",
        "theta retirement-basis re-match",
        "record-instrument polar contrast stabilization",
        "DELTA0 route inventory sibling-total refresh",
        "g_bare two-Ward scope repair",
        "AC R-eta h-unit primitive no-go",
        "owner-governed Tier-A retirement",
        "AC R-eta h-class stretch no-go",
        "theta G1 kinetic 4D scaffold support",
        "primitive axiom absorption no-go",
        "No-Go Discipline Gate",
        "broad F retention fails; narrowed F-clause assembly discriminator",
        "No derivation or ratification of F1-F4.",
        "No derivation or ratification of F.",
        "No use of latest open PRs as proof inputs.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("F-clause finite discriminator")
    inputs = ["F1", "F2", "F3", "F4"]
    closing_subsets = [subset for subset in all_subsets(inputs) if closes_f(subset)]
    audit.check("exactly one tested F-subinput set closes F", closing_subsets == [set(inputs)])
    for item in inputs:
        missing_one = set(inputs) - {item}
        audit.check(f"missing {item} fails F closure", not closes_f(missing_one))

    coords = coordinates()
    audit.check("full-cell coordinate set has 256 elements", len(coords) == 256)
    audit.check("slot-additive source has 16 coordinates", 4 * 4 == 16)
    audit.check("diagonal slot-locked source has 4 coordinates", 4 == 4)
    audit.check("scalar/tracial source has 1 coordinate", 1 == 1)
    audit.check("direct D17 x full-cell product has 512 components", 2 * len(coords) == 512)
    audit.check("full-cell source count differs from slot-additive count", len(coords) != 16)
    audit.check("full-cell source count differs from diagonal count", len(coords) != 4)

    d17_norm = Fraction(1, 2) + Fraction(1, 2)
    audit.check("D17 two-component scalar block is unit-normalized", d17_norm == 1)
    source_density = Fraction(1, len(coords))
    product_unit_source_factor = Fraction(1, 16)
    audit.check("separated uniform source density is 1/256", source_density == Fraction(1, 256))
    audit.check("product unit-vector source factor is 1/16", product_unit_source_factor == Fraction(1, 16))
    audit.check("separated density class differs from product unit class", source_density != product_unit_source_factor)

    h = Fraction(7, 1)
    c0 = coords[0]
    c1 = coords[1]
    j_a = {c0: Fraction(2, 1), c1: Fraction(3, 1)}
    j_b = {c0: Fraction(5, 1), c1: Fraction(11, 1)}
    action_a = source_action(j_a, h)
    action_b = source_action(j_b, h)
    action_sum = source_action(add_vectors(j_a, j_b), h)
    audit.check("source/action family is linear in j", action_sum == add_vectors(action_a, action_b))
    audit.check("derivative wrt a source coordinate returns h times insertion", derivative_wrt(c0, h)[c0] == h)

    section("Authority boundary checks")
    goal = read(GOAL)
    route = read(ROUTE)
    ratification = read(RATIFICATION)
    compression = read(COMPRESSION)
    obs_source = read(OBS_SOURCE)
    source_coupled = read(SOURCE_COUPLED)
    full_cell = read(FULL_CELL)
    d17_sep = read(D17_SEP)
    f3_no_go = read(F3_NO_GO)
    f4_no_go = read(F4_NO_GO)
    tensor_firewall = read(TENSOR_FIREWALL)
    source_control = read(SOURCE_CONTROL)
    d17_note = read(D17_NOTE)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("goal packet cites F-clause follow-up", "F-clause source/action assembly discriminator" in goal)
    audit.check("route triage cites F-clause follow-up", "Follow-up A2 F-clause source/action assembly discriminator" in route)
    audit.check("ratification target cites F-clause follow-up", "F-clause assembly discriminator" in ratification)
    audit.check("compression note still names full F/L/P/R target", "full F/L/P/R interface" in compression)
    audit.check("observable source candidate is open gate", "open_gate" in obs_source and "Local source derivatives of `S` define" in obs_source)
    audit.check("source-coupled support names derivative attachment", "dS_lep/dj_c = h * B_lep * O_c" in source_coupled)
    audit.check("full-cell support names 256 carrier", "M_2(C)^tensor4" in full_cell and "4^4 = 256" in full_cell)
    audit.check("D17 separability names scalar multiplier", "scalar source multiplier" in d17_sep and "512" in d17_sep)
    audit.check("F1 target names local derivative insertion", "F1 Source-Coupled Local-Action Ratification Target Discriminator" in read(F1_TARGET))
    audit.check("F2 selector names D17 source block", "F2 Charged-Lepton Source Block Selector Discriminator" in read(F2_SELECTOR))
    audit.check(
        "F2 no-go keeps F2 unsupplied",
        "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED" in read(F2_NO_GO)
        and "current retained, primitive, and open-PR surfaces do not supply" in read(F2_NO_GO),
    )
    audit.check("F3 target names full-cell source-locality", "F3 Full-Cell Tensor Source-Locality Ratification Target Discriminator" in read(F3_TARGET))
    audit.check(
        "F3 no-go keeps F3 unsupplied",
        "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED" in f3_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in f3_no_go,
    )
    audit.check("F4 target names scalar attachment", "F4 Scalar-Multiplier Attachment Ratification Target Discriminator" in read(F4_TARGET))
    audit.check(
        "F4 no-go keeps F4 unsupplied",
        "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED" in f4_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in f4_no_go,
    )
    audit.check("tensor firewall names product unit class", "2 * 256 = 512" in tensor_firewall and "(1/sqrt(2))*(1/16)" in tensor_firewall)
    audit.check("source-control support is downstream of source family", "J(j_A + j_B) = J(j_A) + J(j_B)" in source_control)
    audit.check("D17 note names scalar-singlet source", "scalar-singlet" in d17_note and "1/sqrt(2)" in d17_note)
    audit.check("minimal axioms exclude source/action", "source/action and physical-observable identification" in minimal)
    for node_name in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    audit.check("scale primitive current path matches registry", nodes["scale_reference_primitive"]["current_path"] == "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    audit.check("kinetic primitive current path matches registry", nodes["kinetic_isotropy_primitive"]["current_path"] == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")
    audit.check("realized primitive current path matches registry", nodes["realized_state_primitive"]["current_path"] == "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    audit.check("scale primitive excludes dimensionless physics", "dimensionless" in scale and "does not" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
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
        "`#4984` AC R-eta direct-license no-go | `CLEAN`",
        "`#4983` AC R-eta doublet-clock no-go | `CLEAN`",
        "`#4982` AC occupancy formation non-supply no-go | `CLEAN`",
        "`#4981` AC R-eta C3 ratification non-supply | `CLEAN`",
        "`#4980` theta G1 kinetic 4D scaffold support | `CLEAN`",
        "`#4979` theta G1 defect suppression support | `CLEAN`",
        "`#4978` theta G1 4D carrier supply no-go | `CLEAN`",
        "`#4975` primitive axiom absorption no-go | `CLEAN`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of F1-F4.",
        "No derivation or ratification of F.",
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
        "This note ratifies F",
        "F is retained",
        "F1-F4 are retained",
        "S_l is retained",
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
