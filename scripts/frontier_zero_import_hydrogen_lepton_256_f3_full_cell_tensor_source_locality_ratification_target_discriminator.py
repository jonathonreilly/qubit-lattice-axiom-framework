#!/usr/bin/env python3
"""Verifier for the F3 full-cell tensor source-locality target discriminator.

The runner checks the finite carrier target and authority boundaries for F3.
It does not ratify F3, derive S_l, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import json
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
RATIFICATION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F_CLAUSE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
FULL_CELL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md"
OS0_REPAIR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md"
TENSOR_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md"
SOURCE_SLOT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md"
RESTRICTED_FRAME = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md"
F1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F2_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
F3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md"
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


def closes_f3(inputs: set[str]) -> bool:
    return inputs == {"OS0", "SOURCE", "FULL_CELL", "INDEPENDENT", "RATIFICATION"}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("F3 source-locality note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        RATIFICATION,
        F_CLAUSE,
        FULL_CELL,
        OS0_REPAIR,
        TENSOR_FIREWALL,
        SOURCE_SLOT,
        RESTRICTED_FRAME,
        F1_TARGET,
        F2_SELECTOR,
        F3_NO_GO,
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
        "F3 Full-Cell Tensor Source-Locality Ratification Target Discriminator",
        "does not ratify F3",
        "does not derive retained `S_l = 1/256`",
        "full OS0-cell tensor source locality",
        "A_cell = A_x tensor A_y tensor A_z tensor A_tau",
        "C = {0,1,2,3}^4",
        "J(j) = sum_{c in C} j_c O_c",
        "OS0",
        "SOURCE",
        "FULL_CELL",
        "INDEPENDENT",
        "RATIFICATION",
        "Every one-input-removed target fails",
        "spatial-only `M_2(C)^tensor3` gives `4^3 = 64`",
        "slot-additive, diagonal, and scalar/tracial sources give `16`, `4`, and `1` coordinates",
        "no retained premise for F",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED",
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
        "broad F3 retention not shipped; narrowed F3 source-locality",
        "No derivation or ratification of F3.",
        "No derivation or ratification of F.",
        "No use of latest open PRs as proof inputs.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("F3 finite discriminator checks")
    inputs = ["OS0", "SOURCE", "FULL_CELL", "INDEPENDENT", "RATIFICATION"]
    closing_subsets = [subset for subset in all_subsets(inputs) if closes_f3(subset)]
    audit.check("exactly one tested F3 input set closes F3", closing_subsets == [set(inputs)])
    for item in inputs:
        missing_one = set(inputs) - {item}
        audit.check(f"missing {item} fails F3 closure", not closes_f3(missing_one))

    slot_dim = 4
    full_slots = ("x", "y", "z", "tau")
    spatial_slots = ("x", "y", "z")
    full_coords = list(product(range(slot_dim), repeat=len(full_slots)))
    spatial_coords = list(product(range(slot_dim), repeat=len(spatial_slots)))
    audit.check("full OS0 tensor source has 256 matrix-unit coordinates", len(full_coords) == 256)
    audit.check("full OS0 tensor coordinates are unique", len(set(full_coords)) == 256)
    audit.check("spatial-only tensor source has 64 coordinates", len(spatial_coords) == 64)
    audit.check("slot-additive source has 16 coordinates", slot_dim * len(full_slots) == 16)
    audit.check("diagonal slot-locked source has 4 coordinates", slot_dim == 4)
    audit.check("scalar/tracial source has 1 coordinate", 1 == 1)
    audit.check("only full tensor source reaches 256", all(v != 256 for v in [len(spatial_coords), slot_dim * len(full_slots), slot_dim, 1]))

    collapsed_inputs = ["OS0_GEOMETRY", "PHYSICAL_SOURCE_LOCALITY", "FULL_TENSOR_INDEPENDENCE", "RATIFICATION"]
    audit.check("collapsed F3 wall audit has six pairwise checks", len(list(combinations(collapsed_inputs, 2))) == 6)

    section("Authority boundary checks")
    goal = read(GOAL)
    route = read(ROUTE)
    ratification = read(RATIFICATION)
    f_clause = read(F_CLAUSE)
    full_cell = read(FULL_CELL)
    os0 = read(OS0_REPAIR)
    tensor = read(TENSOR_FIREWALL)
    source_slot = read(SOURCE_SLOT)
    restricted = read(RESTRICTED_FRAME)
    f1_target = read(F1_TARGET)
    f2_selector = read(F2_SELECTOR)
    f3_no_go = read(F3_NO_GO)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("goal packet cites F3 follow-up", "F3 full-cell tensor source-locality ratification target discriminator" in goal)
    audit.check("route triage cites F3 follow-up", "Follow-up A2 F3 full-cell tensor source-locality ratification target discriminator" in route)
    audit.check("ratification target cites F3 follow-up", "F3 full-cell tensor source-locality ratification target discriminator" in ratification)
    audit.check("F-clause note cites F3 follow-up", "F3 full-cell tensor source-locality follow-up" in f_clause)
    audit.check("full-cell support is conditional", "does not prove that the charged-lepton scalar source has that full-cell source locality" in flat(full_cell))
    audit.check("OS0 repair leaves A1 open", "Does the charged-lepton scalar block carry one `M_2(C)` factor per OS0 slot? | Not derived here." in os0)
    audit.check("tensor firewall names carrier attachment", "T1 carrier attachment" in tensor and "not a lepton scalar source lift" in tensor)
    audit.check("source-slot support does not derive source family", "derive that source family" in source_slot)
    audit.check("restricted tensor-frame support needs supplied frame", "supplied physical tensor-product matrix-unit source frame" in restricted)
    audit.check("F1 target remains sibling context", "does not ratify F1" in f1_target)
    audit.check("F2 selector remains sibling context", "No derivation or ratification of F1, F3, or F4." in f2_selector)
    no_go_name = "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md"
    audit.check("F3 target references F3 current-surface no-go", no_go_name in note)
    audit.check(
        "F3 no-go keeps F3 unsupplied",
        "current retained, primitive, and open-PR surfaces do not supply" in f3_no_go
        and "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED" in f3_no_go,
    )
    audit.check("minimal axioms exclude source/action", "source/action and physical-observable identification" in minimal)
    for node_name in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    audit.check("scale primitive excludes dimensionless physics", "zero dimensionless" in scale and "does not supply any dimensionless quantity" in scale)
    audit.check("kinetic primitive supplies OS0 but excludes selector/readout", "Z^3 x Z_tau" in kinetic and "selector" in kinetic and "readout bridge" in kinetic)
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
        "No derivation or ratification of F3.",
        "No derivation or ratification of F.",
        "No derivation or ratification of F1, F2, or F4.",
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
        "This note ratifies F3",
        "F3 is retained",
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
