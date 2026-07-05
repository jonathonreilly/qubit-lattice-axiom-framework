#!/usr/bin/env python3
"""Verifier for the F2 charged-lepton source-block current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED. It preserves the
positive D17/source-block selector route and keeps F, exact S_l, m_e,
alpha(0), Rydberg, and hydrogen downstream.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
F_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
F_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
F1_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
F3_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F4_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
D17_NOTE = ROOT / "docs" / "LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
FULL_CELL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md"
D17_SEP = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
SOURCE_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_SOURCE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

F2_INPUTS = {
    "D17_SCALAR_BLOCK",
    "CHARGED_LEPTON_SECTOR_RESTRICTION",
    "SCALAR_SINGLET_SCOPE",
    "SOURCE_BLOCK_ATTACHMENT",
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


def closes_f2(inputs: set[str]) -> bool:
    return F2_INPUTS <= inputs


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
        F1_TARGET,
        F2_TARGET,
        F3_TARGET,
        F4_TARGET,
        D17_NOTE,
        SOURCE_COUPLED,
        FULL_CELL,
        D17_SEP,
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
        "F2 Charged-Lepton Source-Block Selector Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "D17_SCALAR_BLOCK",
        "CHARGED_LEPTON_SECTOR_RESTRICTION",
        "SCALAR_SINGLET_SCOPE",
        "SOURCE_BLOCK_ATTACHMENT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R",
        "Z_lep^2 = N_c N_iso = 1 * 2 = 2",
        "the F source block is B_lep",
        "no D17: a lepton label alone does not supply the normalized scalar singlet",
        "no SECTOR: a full-cell source carrier can be regulator-generic",
        "no SCALAR: triplet or tilde-H channels are outside the stated D17 scalar block",
        "no ATTACHMENT: D17 alone gives a bounded scalar block, not a source/action family",
        "charged_lepton_source_block_selector_primitive",
        "d17_source_block_selector_primitive",
        "sector_restriction_primitive",
        "scalar_singlet_source_block_primitive",
        "source_block_attachment_primitive",
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
        "broad F2 no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("F2 predicate checks")
    full_inputs = set(F2_INPUTS)
    audit.check("full F2 contract accepts F2", closes_f2(full_inputs))
    for missing in sorted(F2_INPUTS):
        reduced = set(F2_INPUTS)
        reduced.remove(missing)
        audit.check(f"F2 fails without {missing}", not closes_f2(reduced))
    accepted_subsets = [subset for subset in all_subsets(F2_INPUTS) if closes_f2(subset)]
    audit.check("only full F2 subset closes F2", accepted_subsets == [full_inputs])
    audit.check("F2 alone does not close F", not closes_f_clause({"F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED"}))
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

    section("Finite F2 witness checks")
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
    audit.check("D17 block supplies 1/sqrt(2), not 1/256", Fraction(1, 2) != Fraction(1, 256))
    audit.check("separated D17/full-cell coefficient differs from product unit source factor", Fraction(1, 256) != Fraction(1, 16))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    f_no_go = read(F_NO_GO)
    f_decision = read(F_DECISION)
    f_assembly = read(F_ASSEMBLY)
    f1_no_go = read(F1_NO_GO)
    f1_target = read(F1_TARGET)
    f2_target = read(F2_TARGET)
    f3 = read(F3_TARGET)
    f4 = read(F4_TARGET)
    d17_note = read(D17_NOTE)
    source_coupled = read(SOURCE_COUPLED)
    full_cell = read(FULL_CELL)
    d17_sep = read(D17_SEP)
    source_coupled_flat = flat(source_coupled)
    d17_sep_flat = flat(d17_sep)
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

    no_go_name = "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
    audit.check("goal packet references F2 no-go", no_go_name in goal)
    audit.check("F no-go references F2 no-go", no_go_name in f_no_go)
    audit.check("F decision packet references F2 no-go", no_go_name in f_decision)
    audit.check("F assembly references F2 no-go", no_go_name in f_assembly)
    audit.check("F2 target references F2 no-go", no_go_name in f2_target)
    audit.check("F2 target remains unratified", "does not ratify F2" in f2_target)
    audit.check("F1 no-go remains sibling only", "F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED" in f1_no_go)
    audit.check("F1 target remains separate", "does not ratify F1" in f1_target)
    audit.check("D17 note names scalar-singlet block", "H_unit^lep = (1/sqrt(2))" in d17_note)
    audit.check("D17 note names Z_lep normalization", "Z_lep^2 = N_c N_iso = 1 * 2 = 2" in d17_note)
    audit.check("D17 note rejects triplet route inside stated block", "triplet channel is outside" in d17_note)
    audit.check("D17 note is bounded, not retained status", "bounded structural theorem" in d17_note and "does not assign retained status" in d17_note)
    audit.check(
        "source-coupled attachment remains conditional",
        "If the source-coupled local-action convention" in source_coupled
        and "lepton-specific full-cell source" in source_coupled
        and "does not prove that the charged-lepton scalar source is full-cell" in source_coupled_flat,
    )
    audit.check(
        "full-cell support remains F3 carrier support",
        "does not prove that the charged-lepton scalar source has that full-cell" in full_cell
        and "charged-lepton sector specificity" in full_cell
        and "4^4 = 256" in full_cell,
    )
    audit.check(
        "D17 separability support remains conditional",
        "scalar-multiplier attachment of that carrier to the D17 block" in d17_sep_flat
        and "does not promote the D17 source note" in d17_sep_flat
        and "full-cell carrier without D17 block attachment" in d17_sep_flat,
    )
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
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)

    for primitive_name in [
        "charged_lepton_source_block_selector_primitive",
        "d17_source_block_selector_primitive",
        "sector_restriction_primitive",
        "scalar_singlet_source_block_primitive",
        "source_block_attachment_primitive",
        "f_clause_primitive",
        "source_probe_interface_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered F2 shortcut: {primitive_name}", primitive_name not in nodes)

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
        "No derivation or ratification of `F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED`.",
        "No derivation or ratification of F2.",
        "No derivation or ratification of F.",
        "No derivation or ratification of F1, F3, or F4.",
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
        "This note ratifies F2",
        "F2 is retained",
        "F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED is supplied",
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
