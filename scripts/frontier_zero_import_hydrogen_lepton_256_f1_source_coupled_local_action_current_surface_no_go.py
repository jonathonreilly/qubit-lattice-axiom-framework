#!/usr/bin/env python3
"""Verifier for the F1 source-coupled local-action current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED. It preserves the
positive convention-ratification route and keeps F, exact S_l, m_e, alpha(0),
Rydberg, and hydrogen downstream.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
F_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
F_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
F1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
F3_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F4_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
OBS_SOURCE = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
SOURCE_CONTROL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md"
SOURCE_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_SOURCE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

F1_INPUTS = {
    "LOCAL_LINEAR_ACTION_SOURCE",
    "DERIVATIVE_INSERTION_LICENSE",
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


def closes_f1(inputs: set[str]) -> bool:
    return F1_INPUTS <= inputs


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
        F1_TARGET,
        F2_TARGET,
        F3_TARGET,
        F4_TARGET,
        OBS_SOURCE,
        SOURCE_COUPLED,
        SOURCE_CONTROL,
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
        "F1 Source-Coupled Local-Action Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "ACTION + LINEAR + DERIVATIVE + RATIFICATION",
        "LOCAL_LINEAR_ACTION_SOURCE",
        "DERIVATIVE_INSERTION_LICENSE",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "S[j] = S_0 + sum_{c in C} j_c A_c",
        "dS/dj_c = A_c",
        "open_gate",
        "no ACTION: W = log Z responses are downstream response data",
        "no LINEAR: S[j] = S_0 + sum_c j_c^2 A_c gives dS/dj_c = 2 j_c A_c",
        "no DERIVATIVE: J(j) = sum_c j_c O_c remains formal algebra",
        "no RATIFICATION: the rule remains a candidate convention",
        "source_action_convention_primitive",
        "local_action_source_primitive",
        "derivative_insertion_license_primitive",
        "f1_source_coupled_local_action_primitive",
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
        "broad F1 no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("F1 predicate checks")
    full_inputs = set(F1_INPUTS)
    audit.check("full F1 contract accepts F1", closes_f1(full_inputs))
    for missing in sorted(F1_INPUTS):
        reduced = set(F1_INPUTS)
        reduced.remove(missing)
        audit.check(f"F1 fails without {missing}", not closes_f1(reduced))
    accepted_subsets = [subset for subset in all_subsets(F1_INPUTS) if closes_f1(subset)]
    audit.check("only full F1 subset closes F1", accepted_subsets == [full_inputs])
    audit.check("F1 alone does not close F", not closes_f_clause({"F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED"}))
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

    section("Finite F1 witness checks")
    coefficients = {"c0": Fraction(3, 1), "c1": Fraction(5, 1)}
    source_zero = {"c0": Fraction(0, 1), "c1": Fraction(0, 1)}
    source_nonzero = {"c0": Fraction(7, 1), "c1": Fraction(11, 1)}
    linear_derivative = coefficients["c0"]
    nonlinear_zero = 2 * source_zero["c0"] * coefficients["c0"]
    nonlinear_nonzero = 2 * source_nonzero["c0"] * coefficients["c0"]
    mixed_derivative = coefficients["c0"] + coefficients["c1"]
    audit.check("linear derivative returns selected insertion", linear_derivative == Fraction(3, 1))
    audit.check("linear derivative separates coordinates", coefficients["c0"] != coefficients["c1"])
    audit.check("nonlinear derivative vanishes at zero source", nonlinear_zero == 0)
    audit.check("nonlinear derivative depends on source strength", nonlinear_nonzero == Fraction(42, 1))
    audit.check("mixed-control derivative is a sum, not one insertion", mixed_derivative == Fraction(8, 1))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    f_no_go = read(F_NO_GO)
    f_decision = read(F_DECISION)
    f_assembly = read(F_ASSEMBLY)
    f1_target = read(F1_TARGET)
    f2 = read(F2_TARGET)
    f3 = read(F3_TARGET)
    f4 = read(F4_TARGET)
    obs_source = read(OBS_SOURCE)
    source_coupled = read(SOURCE_COUPLED)
    source_control = read(SOURCE_CONTROL)
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

    no_go_name = "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
    audit.check("goal packet references F1 no-go", no_go_name in goal)
    audit.check("F no-go references F1 no-go", no_go_name in f_no_go)
    audit.check("F decision packet references F1 no-go", no_go_name in f_decision)
    audit.check("F assembly references F1 no-go", no_go_name in f_assembly)
    audit.check("F1 target references F1 no-go", no_go_name in f1_target)
    audit.check("F1 target remains unratified", "does not ratify F1" in f1_target)
    audit.check("observable source candidate remains open gate", "Claim type:** open_gate" in obs_source)
    audit.check(
        "observable source candidate denies retained derivation",
        "does not claim that convention is derived from retained primitives" in obs_source,
    )
    audit.check(
        "source-coupled attachment remains conditional",
        "If the source-coupled local-action convention is adopted" in source_coupled
        and "does not prove the source-coupled local-action convention" in source_coupled
        and "dS_lep/dj_c = h * B_lep * O_c" in source_coupled,
    )
    audit.check(
        "source-control linearity remains conditional",
        "The conditional answer is yes" in source_control
        and "source-coupled local-action convention is" in source_control
        and "adopted" in source_control
        and "slot-resolved" in source_control
        and "This proves only the algebraic source-control linearity part" in source_control
        and "derive the source-coupled convention" in source_control
        and "J(j_A + j_B) = J(j_A) + J(j_B)" in source_control,
    )
    audit.check("F2 target remains sibling only", "does not supply F1" in f2)
    audit.check("F3 target remains separate", "does not ratify F3" in f3)
    audit.check("F4 target remains separate", "does not ratify F4" in f4)
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
    audit.check("kinetic primitive excludes source/action and selectors", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)

    for primitive_name in [
        "source_action_convention_primitive",
        "local_action_source_primitive",
        "derivative_insertion_license_primitive",
        "f1_source_coupled_local_action_primitive",
        "f_clause_primitive",
        "source_probe_interface_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered F1 shortcut: {primitive_name}", primitive_name not in nodes)

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
        "No derivation or ratification of `F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED`.",
        "No derivation or ratification of F1.",
        "No derivation or ratification of F.",
        "No derivation or ratification of F2, F3, or F4.",
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
        "This note ratifies F1",
        "F1 is retained",
        "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED is supplied",
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
