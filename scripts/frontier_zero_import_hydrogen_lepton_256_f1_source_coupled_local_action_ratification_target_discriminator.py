#!/usr/bin/env python3
"""Verifier for the F1 source-coupled local-action target discriminator.

The runner checks the finite derivative target and authority boundaries for
F1. It does not ratify F1, derive S_l, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
RATIFICATION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F_CLAUSE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
F1_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F2_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
OBS_SOURCE = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
SOURCE_CONTROL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md"
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


def closes_f1(inputs: set[str]) -> bool:
    return inputs == {"ACTION", "LINEAR", "DERIVATIVE", "RATIFICATION"}


def linear_derivative(coefficients: dict[str, Fraction], key: str) -> Fraction:
    return coefficients[key]


def nonlinear_derivative_at(coefficients: dict[str, Fraction], source_values: dict[str, Fraction], key: str) -> Fraction:
    return 2 * source_values[key] * coefficients[key]


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("F1 source-coupled local-action note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        RATIFICATION,
        F_CLAUSE,
        F1_NO_GO,
        F2_SELECTOR,
        OBS_SOURCE,
        SOURCE_COUPLED,
        SOURCE_CONTROL,
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
        "F1 Source-Coupled Local-Action Ratification Target Discriminator",
        "does not ratify F1",
        "does not derive retained `S_l = 1/256`",
        "F1 source-coupled local-action convention",
        "dS_lep/dj_c = h * B_lep * O_c",
        "S[j] = S_0 + sum_{c in C} j_c A_c",
        "dS/dj_c = A_c",
        "ACTION",
        "LINEAR",
        "DERIVATIVE",
        "RATIFICATION",
        "Every one-input-removed target fails",
        "no local action insertion rule",
        "no source/action bridge",
        "no retained premise for F",
        "response-only `W[j]`",
        "not the local action insertion rule",
        "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md",
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
        "source-coupled local-action ratification",
        "No-Go Discipline Gate",
        "broad F1 retention not shipped; narrowed F1 ratification-target",
        "No derivation or ratification of F1.",
        "No derivation or ratification of F.",
        "No use of latest open PRs as proof inputs.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("F1 finite discriminator checks")
    inputs = ["ACTION", "LINEAR", "DERIVATIVE", "RATIFICATION"]
    closing_subsets = [subset for subset in all_subsets(inputs) if closes_f1(subset)]
    audit.check("exactly one tested F1 input set closes F1", closing_subsets == [set(inputs)])
    for item in inputs:
        missing_one = set(inputs) - {item}
        audit.check(f"missing {item} fails F1 closure", not closes_f1(missing_one))

    coeffs = {"c0": Fraction(3, 1), "c1": Fraction(5, 1)}
    sources_zero = {"c0": Fraction(0, 1), "c1": Fraction(0, 1)}
    sources_nonzero = {"c0": Fraction(7, 1), "c1": Fraction(11, 1)}
    audit.check("linear derivative returns selected insertion coefficient", linear_derivative(coeffs, "c0") == Fraction(3, 1))
    audit.check("linear derivative separates source coordinates", linear_derivative(coeffs, "c0") != linear_derivative(coeffs, "c1"))
    audit.check("nonlinear j^2 derivative vanishes at zero source", nonlinear_derivative_at(coeffs, sources_zero, "c0") == 0)
    audit.check("nonlinear j^2 derivative depends on source strength", nonlinear_derivative_at(coeffs, sources_nonzero, "c0") == Fraction(42, 1))
    mixed_derivative = coeffs["c0"] + coeffs["c1"]
    audit.check("mixed-control derivative is a sum, not one insertion", mixed_derivative == Fraction(8, 1) and mixed_derivative != coeffs["c0"])

    collapsed_inputs = ["LOCAL_LINEAR_ACTION_SOURCE", "DERIVATIVE_INSERTION", "RATIFICATION"]
    audit.check("collapsed F1 wall audit has three pairwise checks", len(list(combinations(collapsed_inputs, 2))) == 3)

    section("Authority boundary checks")
    goal = read(GOAL)
    route = read(ROUTE)
    ratification = read(RATIFICATION)
    f_clause = read(F_CLAUSE)
    f1_no_go = read(F1_NO_GO)
    f2_selector = read(F2_SELECTOR)
    obs_source = read(OBS_SOURCE)
    source_coupled = read(SOURCE_COUPLED)
    source_control = read(SOURCE_CONTROL)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("goal packet cites F1 follow-up", "F1 source-coupled local-action ratification target discriminator" in goal)
    audit.check("route triage cites F1 follow-up", "Follow-up A2 F1 source-coupled local-action ratification target discriminator" in route)
    audit.check("ratification target cites F1 follow-up", "F1 source-coupled local-action ratification target discriminator" in ratification)
    audit.check("F-clause note cites F1 follow-up", "F1 source-coupled local-action follow-up" in f_clause)
    audit.check("F1 target references current-surface no-go", "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md" in note)
    audit.check("F1 no-go keeps F1 unsupplied", "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED" in f1_no_go and "current retained, primitive, and open-PR surfaces do not supply" in f1_no_go)
    audit.check("F2 selector remains sibling context only", "does not supply F1" in f2_selector)
    audit.check("observable source candidate is open gate", "Claim type:** open_gate" in obs_source and "Local source derivatives of `S` define" in obs_source)
    obs_source_flat = flat(obs_source)
    audit.check(
        "observable source candidate does not derive convention",
        "does not derive the source-coupling interpretation" in obs_source_flat
        and "retained primitives" in obs_source_flat,
    )
    audit.check("source-coupled attachment names derivative consequence", "dS_lep/dj_c = h * B_lep * O_c" in source_coupled)
    audit.check("source-control linearity depends on source-coupled convention", "source-coupled local-action convention" in source_control)
    audit.check("minimal axioms exclude source/action", "source/action and physical-observable identification" in minimal)
    for node_name in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    audit.check("scale primitive excludes dimensionless physics", "zero dimensionless content" in flat(scale))
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
        "No derivation or ratification of F1.",
        "No derivation or ratification of F.",
        "No derivation or ratification of F2, F3, or F4.",
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
        "This note ratifies F1",
        "F1 is retained",
        "F is retained",
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
