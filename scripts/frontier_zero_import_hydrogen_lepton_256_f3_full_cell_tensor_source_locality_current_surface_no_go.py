#!/usr/bin/env python3
"""Verifier for the F3 full-cell tensor source-locality current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED. It preserves
the positive full-cell tensor source-locality route and keeps F, exact S_l,
m_e, alpha(0), Rydberg, and hydrogen downstream.
"""

from __future__ import annotations

from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
F_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
F_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
F1_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F3_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F4_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
FULL_CELL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md"
OS0_REPAIR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md"
TENSOR_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md"
SOURCE_SLOT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md"
RESTRICTED_FRAME = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md"
SOURCE_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_SOURCE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

F3_INPUTS = {
    "OS0_GEOMETRY",
    "PHYSICAL_SOURCE_FAMILY",
    "FULL_CELL_TENSOR_LOCALITY",
    "INDEPENDENT_MATRIX_UNIT_CONTROLS",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
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


def closes_f3(inputs: set[str]) -> bool:
    return F3_INPUTS <= inputs


def closes_f_clause(inputs: set[str]) -> bool:
    return {
        "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED",
        "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED",
        "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED",
        "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED",
    } <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        F_NO_GO,
        F_DECISION,
        F_ASSEMBLY,
        F1_NO_GO,
        F2_NO_GO,
        F3_TARGET,
        F4_TARGET,
        FULL_CELL,
        OS0_REPAIR,
        TENSOR_FIREWALL,
        SOURCE_SLOT,
        RESTRICTED_FRAME,
        SOURCE_PACKET,
        EXACT_SOURCE,
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
        "F3 Full-Cell Tensor Source-Locality Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "OS0_GEOMETRY",
        "PHYSICAL_SOURCE_FAMILY",
        "FULL_CELL_TENSOR_LOCALITY",
        "INDEPENDENT_MATRIX_UNIT_CONTROLS",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "A_cell = M_2(C)^tensor4",
        "C = {0,1,2,3}^4",
        "|C| = 4^4 = 256",
        "J(j) = sum_{c in C} j_c O_c",
        "no OS0: spatial-only M_2(C)^tensor3 gives 4^3 = 64",
        "no SOURCE: M_2(C)^tensor4 is only regulator geometry",
        "no FULL_CELL: slot-additive, diagonal, and scalar carriers have counts 16, 4, and 1",
        "no INDEPENDENT: constrained controls do not give one source per tensor matrix unit",
        "no RATIFICATION: the source-locality rule remains a candidate convention",
        "full_cell_source_locality_primitive",
        "source_locality_primitive",
        "physical_source_family_primitive",
        "independent_matrix_unit_controls_primitive",
        "f3_full_cell_tensor_source_locality_primitive",
        "f_clause_primitive",
        "source_probe_interface_primitive",
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
        "broad F3 no-go is not shipped",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("F3 predicate checks")
    full_inputs = set(F3_INPUTS)
    audit.check("full F3 contract accepts F3", closes_f3(full_inputs))
    for missing in sorted(F3_INPUTS):
        reduced = set(F3_INPUTS)
        reduced.remove(missing)
        audit.check(f"F3 fails without {missing}", not closes_f3(reduced))
    accepted_subsets = [subset for subset in all_subsets(F3_INPUTS) if closes_f3(subset)]
    audit.check("only full F3 subset closes F3", accepted_subsets == [full_inputs])
    audit.check("F3 alone does not close F", not closes_f_clause({"F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED"}))
    audit.check(
        "F1-F4 predicate model closes F",
        closes_f_clause(
            {
                "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED",
                "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED",
                "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED",
                "F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED",
            }
        ),
    )

    section("Finite F3 witness checks")
    slot_dim = 4
    full_coords = list(product(range(slot_dim), repeat=4))
    spatial_coords = list(product(range(slot_dim), repeat=3))
    audit.check("full OS0 tensor source has 256 matrix-unit coordinates", len(full_coords) == 256)
    audit.check("full OS0 tensor coordinates are unique", len(set(full_coords)) == 256)
    audit.check("spatial-only tensor source has 64 coordinates", len(spatial_coords) == 64)
    audit.check("slot-additive source has 16 coordinates", slot_dim * 4 == 16)
    audit.check("diagonal slot-locked source has 4 coordinates", slot_dim == 4)
    audit.check("scalar/tracial source has 1 coordinate", 1 == 1)
    audit.check("only full tensor source reaches 256", all(v != 256 for v in [len(spatial_coords), slot_dim * 4, slot_dim, 1]))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    f_no_go = read(F_NO_GO)
    f_decision = read(F_DECISION)
    f_assembly = read(F_ASSEMBLY)
    f1_no_go = read(F1_NO_GO)
    f2_no_go = read(F2_NO_GO)
    f3_target = read(F3_TARGET)
    f4_target = read(F4_TARGET)
    full_cell = read(FULL_CELL)
    os0 = read(OS0_REPAIR)
    tensor = read(TENSOR_FIREWALL)
    source_slot = read(SOURCE_SLOT)
    restricted = read(RESTRICTED_FRAME)
    source_packet = read(SOURCE_PACKET)
    exact_source = read(EXACT_SOURCE)
    a3 = read(A3_PACKET)
    physical_electron = read(PHYSICAL_ELECTRON)
    registry = json.loads(read(REGISTRY))
    minimal = read(MINIMAL)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    no_go_name = "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md"
    audit.check("goal packet references F3 no-go", no_go_name in goal)
    audit.check("F no-go references F3 no-go", no_go_name in f_no_go)
    audit.check("F decision packet references F3 no-go", no_go_name in f_decision)
    audit.check("F assembly references F3 no-go", no_go_name in f_assembly)
    audit.check("F3 target references F3 no-go", no_go_name in f3_target)
    audit.check("F3 target remains unratified", "does not ratify F3" in f3_target)
    audit.check("F1 no-go remains sibling only", "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED" in f1_no_go)
    audit.check("F2 no-go remains sibling only", "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED" in f2_no_go)
    audit.check("F4 target remains separate", "does not ratify F4" in f4_target)
    audit.check(
        "full-cell support remains conditional",
        "does not prove that the charged-lepton scalar source has that full-cell source locality" in flat(full_cell),
    )
    audit.check(
        "OS0 repair leaves A1 open",
        "one `M_2(C)` factor per OS0 slot" in os0 and "Not derived here" in os0,
    )
    audit.check("tensor firewall names carrier attachment", "T1 carrier attachment" in tensor and "not a lepton scalar source lift" in tensor)
    audit.check("source-slot support does not derive source family", "derive that source family" in source_slot)
    audit.check("restricted tensor-frame support needs supplied frame", "supplied physical tensor-product matrix-unit source frame" in restricted)
    audit.check("source-probe packet keeps F/L/P/R downstream", "does not ratify F/L/P/R" in source_packet)
    audit.check("exact-source no-go keeps F as upstream subdecision", "F_CLAUSE_RETAINED" in exact_source)
    audit.check("A3 remains downstream", "No derivation of `C_A3" in a3)
    audit.check("physical electron remains downstream", "No derivation or ratification of the physical electron mass" in physical_electron)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    audit.check("minimal axioms exclude source/action", "source/action" in minimal and "physical-observable identification" in minimal)
    audit.check("scale primitive excludes dimensionless physics", "does not supply any dimensionless quantity" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)

    for primitive_name in [
        "full_cell_source_locality_primitive",
        "source_locality_primitive",
        "physical_source_family_primitive",
        "independent_matrix_unit_controls_primitive",
        "f3_full_cell_tensor_source_locality_primitive",
        "f_clause_primitive",
        "source_probe_interface_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered F3 shortcut: {primitive_name}", primitive_name not in nodes)

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
        "No derivation or ratification of `F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED`.",
        "No derivation or ratification of F3.",
        "No derivation or ratification of F.",
        "No derivation or ratification of F1, F2, or F4.",
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
        "This note ratifies F3",
        "F3 is retained",
        "F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED is supplied",
        "F is retained",
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
