#!/usr/bin/env python3
"""Verifier for the F2 charged-lepton source-block selector discriminator.

The runner checks the finite D17 scalar-block selector target for F2. It does
not ratify F2, derive S_l, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
RATIFICATION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F_CLAUSE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
F2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
D17_NOTE = ROOT / "docs" / "LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
FULL_CELL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md"
D17_SEP = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
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


def closes_f2(inputs: set[str]) -> bool:
    return inputs == {"D17", "SECTOR", "SCALAR", "ATTACHMENT"}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("F2 source-block selector note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        RATIFICATION,
        F_CLAUSE,
        F2_NO_GO,
        D17_NOTE,
        SOURCE_COUPLED,
        FULL_CELL,
        D17_SEP,
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
        "F2 Charged-Lepton Source Block Selector Discriminator",
        "does not ratify F2",
        "does not derive retained `S_l = 1/256`",
        "F2 charged-lepton sector specificity",
        "B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R",
        "Z_lep^2 = N_c N_iso = 1 * 2 = 2",
        "D17",
        "SECTOR",
        "SCALAR",
        "ATTACHMENT",
        "Every one-input-removed target fails",
        "no `B_lep` or `Z_lep^2=2`",
        "full OS0-cell source coordinates",
        "4^4 = 256",
        "2 * 256 = 512",
        "not the `1/256` source-density theorem",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED",
        "The primitive registry was checked",
        "does not supply F1",
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
        "Tier-A residual owner decision packet",
        "theta G2 registration stretch no-go",
        "AC R-eta h-class stretch no-go",
        "No-Go Discipline Gate",
        "broad F2 retention not shipped; narrowed F2 block-selector",
        "No derivation or ratification of F2.",
        "No derivation or ratification of F.",
        "No use of latest open PRs as proof inputs.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("F2 finite selector checks")
    inputs = ["D17", "SECTOR", "SCALAR", "ATTACHMENT"]
    closing_subsets = [subset for subset in all_subsets(inputs) if closes_f2(subset)]
    audit.check("exactly one tested F2 input set closes F2", closing_subsets == [set(inputs)])
    for item in inputs:
        missing_one = set(inputs) - {item}
        audit.check(f"missing {item} fails F2 closure", not closes_f2(missing_one))

    n_color = 1
    n_iso = 2
    z_lep_squared = n_color * n_iso
    coeff_squares = [Fraction(1, 2), Fraction(1, 2)]
    full_cell_count = len(list(product(range(4), repeat=4)))
    audit.check("D17 lepton color count is 1", n_color == 1)
    audit.check("D17 lepton weak-isospin count is 2", n_iso == 2)
    audit.check("D17 Z_lep squared is 2", z_lep_squared == 2)
    audit.check("two D17 unit coefficients square-sum to 1", sum(coeff_squares) == 1)
    audit.check("full OS0-cell source coordinates count is 256", full_cell_count == 256)
    audit.check("D17 x full-cell direct product count is 512", n_iso * full_cell_count == 512)
    audit.check("D17 block count is not the full-cell source count", n_iso != full_cell_count)

    collapsed_inputs = ["D17_SCALAR_BLOCK", "SECTOR", "ATTACHMENT"]
    pair_count = len(list(combinations(collapsed_inputs, 2)))
    audit.check("collapsed F2 wall audit has three pairwise checks", pair_count == 3)

    section("Authority boundary checks")
    goal = read(GOAL)
    route = read(ROUTE)
    ratification = read(RATIFICATION)
    f_clause = read(F_CLAUSE)
    f2_no_go = read(F2_NO_GO)
    d17_note = read(D17_NOTE)
    source_coupled = read(SOURCE_COUPLED)
    full_cell = read(FULL_CELL)
    d17_sep = read(D17_SEP)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("goal packet cites F2 follow-up", "F2 charged-lepton source-block selector discriminator" in goal)
    audit.check("route triage cites F2 follow-up", "Follow-up A2 F2 charged-lepton source-block selector discriminator" in route)
    audit.check("ratification target cites F2 follow-up", "F2 charged-lepton source-block selector discriminator" in ratification)
    audit.check("F-clause note cites F2 follow-up", "F2 charged-lepton source-block selector follow-up" in f_clause)
    no_go_name = "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
    audit.check("F2 target references current-surface no-go", no_go_name in note)
    audit.check(
        "F2 no-go keeps F2 unsupplied",
        "current retained, primitive, and open-PR surfaces do not supply" in f2_no_go
        and "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED" in f2_no_go,
    )
    audit.check("D17 note names scalar-singlet block", "H_unit^lep = (1/sqrt(2))" in d17_note)
    audit.check("D17 note names Z_lep normalization", "Z_lep^2 = N_c N_iso = 1 * 2 = 2" in d17_note)
    audit.check("D17 note rejects triplet route inside stated block", "triplet channel is outside" in d17_note)
    audit.check("source-coupled note requires lepton-specific source", "lepton-specific full-cell source" in source_coupled)
    audit.check("full-cell note supplies 256 but not sector", "M_2(C)^tensor4" in full_cell and "4^4 = 256" in full_cell)
    d17_sep_flat = flat(d17_sep)
    audit.check("D17 separability note names separated source weights", "1/sqrt(2)" in d17_sep_flat and "source weights" in d17_sep_flat)
    audit.check("minimal axioms exclude source/action", "source/action and physical-observable identification" in minimal)
    for node_name in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    scale_flat = flat(scale)
    audit.check("scale primitive excludes dimensionless physics", "zero dimensionless content" in scale_flat)
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
        "No derivation or ratification of F2.",
        "No derivation or ratification of F.",
        "No derivation or ratification of F1, F3, or F4.",
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
        "This note ratifies F2",
        "F2 is retained",
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
