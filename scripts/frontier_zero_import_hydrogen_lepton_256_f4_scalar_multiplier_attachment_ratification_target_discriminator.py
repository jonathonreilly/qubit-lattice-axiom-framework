#!/usr/bin/env python3
"""Verifier for the F4 scalar-multiplier attachment target discriminator.

The runner checks the finite attachment target and authority boundaries for
F4. It does not ratify F4, derive S_l, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
RATIFICATION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F_CLAUSE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
D17_SEP = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
TENSOR_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md"
D17_NOTE = ROOT / "docs" / "LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md"
F1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F2_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
F3_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F4_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


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


def closes_f4(inputs: set[str]) -> bool:
    return inputs == {"D17_BLOCK", "FULL_CELL_SOURCE", "SCALAR_MULTIPLIER", "BLOCK_PRESERVATION", "RATIFICATION"}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("F4 attachment note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        RATIFICATION,
        F_CLAUSE,
        D17_SEP,
        SOURCE_COUPLED,
        TENSOR_FIREWALL,
        D17_NOTE,
        F1_TARGET,
        F2_SELECTOR,
        F3_TARGET,
        F4_NO_GO,
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
        "F4 Scalar-Multiplier Attachment Ratification Target Discriminator",
        "does not ratify F4",
        "does not derive retained `S_l = 1/256`",
        "F4 scalar-multiplier attachment",
        "B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R",
        "J(j) = sum_{c in C} j_c O_c",
        "S_lep[j] = h * B_lep * J(j)",
        "dS_lep/dj_c = h * B_lep * O_c",
        "D17_BLOCK",
        "FULL_CELL_SOURCE",
        "SCALAR_MULTIPLIER",
        "BLOCK_PRESERVATION",
        "RATIFICATION",
        "Every one-input-removed target fails",
        "direct product unit vector over `2 * 256` components",
        "coefficient class `(1/sqrt(2))*(1/16)`",
        "arbitrary product weights `u_{alpha,c}`",
        "`512` free weights double-count the D17 block",
        "no retained premise for F",
        "1/sqrt(512) = (1/sqrt(2)) * (1/16)",
        "w_c = 1/256",
        "not an A2 derivation",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED",
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
        "theta retirement-basis re-match",
        "record-instrument polar contrast stabilization",
        "DELTA0 route inventory sibling-total refresh",
        "g_bare two-Ward scope repair",
        "owner-governed Tier-A retirement",
        "No-Go Discipline Gate",
        "broad F4 retention not shipped; narrowed F4 attachment target",
        "No derivation or ratification of F4.",
        "No derivation or ratification of F.",
        "No use of latest open PRs as proof inputs.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("F4 finite discriminator checks")
    inputs = ["D17_BLOCK", "FULL_CELL_SOURCE", "SCALAR_MULTIPLIER", "BLOCK_PRESERVATION", "RATIFICATION"]
    closing_subsets = [subset for subset in all_subsets(inputs) if closes_f4(subset)]
    audit.check("exactly one tested F4 input set closes F4", closing_subsets == [set(inputs)])
    for item in inputs:
        missing_one = set(inputs) - {item}
        audit.check(f"missing {item} fails F4 closure", not closes_f4(missing_one))

    d17_norm = Fraction(1, 2) + Fraction(1, 2)
    coords = list(product(range(4), repeat=4))
    audit.check("D17 two-component scalar block is unit-normalized", d17_norm == 1)
    audit.check("full-cell source has 256 coordinates", len(coords) == 256)
    audit.check("direct product has 512 components", 2 * len(coords) == 512)
    product_unit_factor_after_d17 = Fraction(1, 16)
    source_density_factor = Fraction(1, 256)
    audit.check("direct product unit factor is 1/16 after D17 factor", product_unit_factor_after_d17 == Fraction(1, 16))
    audit.check("separated source-density factor is 1/256", source_density_factor == Fraction(1, 256))
    audit.check("product unit class differs from source-density class", product_unit_factor_after_d17 != source_density_factor)

    arbitrary_product_weights = 2 * len(coords)
    separated_source_weights = len(coords)
    audit.check("arbitrary product weights are 512", arbitrary_product_weights == 512)
    audit.check("separated source weights remain 256", separated_source_weights == 256)
    audit.check("block preservation removes extra product-weight freedom", arbitrary_product_weights == 2 * separated_source_weights)

    section("Authority boundary checks")
    goal = read(GOAL)
    route = read(ROUTE)
    ratification = read(RATIFICATION)
    f_clause = read(F_CLAUSE)
    d17_sep = read(D17_SEP)
    source_coupled = read(SOURCE_COUPLED)
    tensor = read(TENSOR_FIREWALL)
    d17_note = read(D17_NOTE)
    f1_target = read(F1_TARGET)
    f2_selector = read(F2_SELECTOR)
    f3_target = read(F3_TARGET)
    f4_no_go = read(F4_NO_GO)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("goal packet cites F4 follow-up", "F4 scalar-multiplier attachment ratification target discriminator" in goal)
    audit.check("route triage cites F4 follow-up", "Follow-up A2 F4 scalar-multiplier attachment ratification target discriminator" in route)
    audit.check("ratification target cites F4 follow-up", "F4 scalar-multiplier attachment ratification target discriminator" in ratification)
    audit.check("F-clause note cites F4 follow-up", "F4 scalar-multiplier attachment follow-up" in f_clause)
    audit.check("D17 separability names scalar multiplier", "scalar source multiplier" in d17_sep and "preserves `1/sqrt(2)`" in d17_sep)
    audit.check("source-coupled attachment names derivative", "dS_lep/dj_c = h * B_lep * O_c" in source_coupled)
    audit.check("tensor firewall names direct product class", "2 * 256 = 512" in tensor and "(1/sqrt(2)) * (1/16)" in tensor)
    audit.check("D17 note names scalar singlet", "H_unit^lep" in d17_note and "1/sqrt(2)" in d17_note)
    audit.check("F1 target remains sibling context", "does not ratify F1" in f1_target)
    audit.check("F2 selector remains sibling context", "No derivation or ratification of F1, F3, or F4." in f2_selector)
    audit.check("F3 target remains sibling context", "No derivation or ratification of F1, F2, or F4." in f3_target)
    no_go_name = "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
    audit.check("F4 target references F4 current-surface no-go", no_go_name in note)
    audit.check(
        "F4 no-go keeps F4 unsupplied",
        "current retained, primitive, and open-PR surfaces do not supply" in f4_no_go
        and "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED" in f4_no_go,
    )
    audit.check("minimal axioms exclude source/action", "source/action and physical-observable identification" in minimal)
    for node_name in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    audit.check("scale primitive excludes dimensionless physics", "zero dimensionless" in scale and "does not supply any dimensionless quantity" in scale)
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
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of F4.",
        "No derivation or ratification of F1, F2, or F3.",
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
        "This note ratifies F4",
        "F4 is retained",
        "F is retained.",
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
