#!/usr/bin/env python3
"""Verifier for the A3 P1 source-readout correction current-surface no-go.

This runner checks that the current hydrogen-facing source surfaces do not
silently supply the P1 theorem needed to turn exact 1/256 into C_A3/256 or
1/N_A3. It preserves P1 as an open route and does not derive C_A3, m_e,
alpha(0), or hydrogen.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SOURCE_PROBE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_CLAUSE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_S_L_READOUT_IDENTITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
P_CLAUSE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SOURCE_SHAPE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md"
UNFIXED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COORDINATE_UNFIXED_CHOICE_LABEL_FREE_SUPPORT_2026-07-04.md"
A3_PLACEMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PLACEMENT_DISCRIMINATOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
PRECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md"
P2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

M_E = 0.51099895
M_MU = 105.6583755
M_TAU = 1776.86
M_W = 80369.2

P1_INPUTS = {
    "P1_SOURCE_READOUT_TEXT_LOCK",
    "EXACT_SOURCE_SINGLETON_RETAINED",
    "SOURCE_READOUT_IDENTITY_RETAINED",
    "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED",
    "P1_PLACEMENT_SELECTED",
    "NO_FRONT_OR_KOIDE_DOUBLE_COUNT",
    "NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
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


def closes_p1(inputs: set[str]) -> bool:
    return P1_INPUTS <= inputs


def a_lepton_squared() -> float:
    a = (math.sqrt(M_E) + math.sqrt(M_MU) + math.sqrt(M_TAU)) / 3.0
    return a * a


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        K4_PACKET,
        SOURCE_PROBE,
        R_CLAUSE,
        R_TARGET,
        P_CLAUSE,
        SOURCE_SHAPE,
        UNFIXED,
        A3_PLACEMENT,
        PLACEMENT_DISCRIMINATOR,
        PRECISION,
        P2_NO_GO,
        REGISTRY,
        TIER_A,
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
        "A3 P1 Source-Readout Correction Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not derive `C_A3`",
        "P1_SOURCE_READOUT_CORRECTION_RETAINED",
        "P1_SOURCE_READOUT_TEXT_LOCK",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "SOURCE_READOUT_IDENTITY_RETAINED",
        "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED",
        "P1_PLACEMENT_SELECTED",
        "NO_FRONT_OR_KOIDE_DOUBLE_COUNT",
        "NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "N_A3 = 256.08243522600384",
        "C_A3 = 256 / N_A3 = 0.9996780910571587",
        "S_0 = 1/256 = 0.00390625",
        "S_P1 = C_A3 * S_0 = 1/N_A3 = 0.003904992543192026",
        "Delta S = S_P1 - S_0",
        "source_readout_correction_primitive",
        "source_nonuniform_ray_primitive",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "No-Go Discipline Gate",
        "broad P1 no-go fails; narrowed current-surface non-supply claim passes",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("P1 correction predicate checks")
    full_inputs = set(P1_INPUTS)
    audit.check("full P1 correction contract accepts source correction", closes_p1(full_inputs))
    for missing in sorted(P1_INPUTS):
        reduced = set(P1_INPUTS)
        reduced.remove(missing)
        audit.check(f"P1 correction fails without {missing}", not closes_p1(reduced))
    accepted_subsets = [subset for subset in all_subsets(P1_INPUTS) if closes_p1(subset)]
    audit.check("only full P1 subset closes source correction", accepted_subsets == [full_inputs])
    current_surface = {
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "SOURCE_READOUT_IDENTITY_RETAINED",
        "P1_PLACEMENT_SELECTED",
        "NO_FRONT_OR_KOIDE_DOUBLE_COUNT",
        "NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    }
    audit.check("current surface without corrected-source theorem does not close P1", not closes_p1(current_surface))

    section("Target arithmetic checks")
    a2 = a_lepton_squared()
    n_a3 = M_W / a2
    c_a3 = 256.0 / n_a3
    s0 = 1.0 / 256.0
    s_p1 = c_a3 * s0
    direct = 1.0 / n_a3
    delta_s = s_p1 - s0

    audit.check("repo a_lepton^2 comparator reproduced", abs(a2 - 313.8411267023086) < 1e-10)
    audit.check("A3 empirical divisor reproduced", abs(n_a3 - 256.08243522600384) < 1e-10)
    audit.check("C_A3 target reproduced", abs(c_a3 - 0.9996780910571587) < 1e-15)
    audit.check("exact source singleton is 1/256", abs(s0 - 0.00390625) < 1e-18)
    audit.check("corrected P1 source equals 1/N_A3", abs(s_p1 - direct) < 1e-18)
    audit.check("P1 correction lowers exact source", s_p1 < s0 and abs(delta_s + 0.000001257456807974003) < 1e-15)
    audit.check("P1 correction ratio is C_A3", abs(s_p1 / s0 - c_a3) < 1e-15)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    k4_packet = read(K4_PACKET)
    source_probe = read(SOURCE_PROBE)
    r_clause = read(R_CLAUSE)
    r_target = read(R_TARGET)
    p_clause = read(P_CLAUSE)
    source_shape = read(SOURCE_SHAPE)
    unfixed = read(UNFIXED)
    a3_placement = read(A3_PLACEMENT)
    placement = read(PLACEMENT_DISCRIMINATOR)
    precision = read(PRECISION)
    p2_no_go = read(P2_NO_GO)
    minimal = flat(read(MINIMAL))
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    tier_a = read(TIER_A)
    nodes = registry["nodes"]

    audit.check("goal packet references P1 current-surface no-go", NOTE.name in goal and "P1_SOURCE_READOUT_CORRECTION_RETAINED" in goal)
    audit.check("K4 packet references P1 current-surface no-go", NOTE.name in k4_packet and "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED" in k4_packet)
    audit.check("source-probe decision supplies exact source only", "S_l = 1/256" in source_probe and "does not place the `256.082435...` precision correction" in source_probe)
    audit.check("R clause supplies source identity only", "S_l = sigma([j])_c" in r_clause and "A3 precision placement" in r_clause)
    audit.check("R target leaves A3-corrected value as alternative, not retained", "A3-corrected value" in r_target and "no source-readout identity" in r_target)
    audit.check("P clause does not supply A3 correction", "For a positive nonuniform ray" in p_clause and "does not supply:" in p_clause)
    audit.check("source-shape selector distinguishes nonuniform from uniform", "nonuniform positive ray" in source_shape and "not `1/256`" in source_shape)
    audit.check("unfixed-choice support guards coordinate-tagged nonuniform laws", "coordinate-tagged nonuniform rays" in unfixed and "not zero-import law-level derivations" in unfixed)
    audit.check("A3 placement packet keeps P1 theorem open", "P1_SOURCE_READOUT_CORRECTION_RETAINED" in a3_placement and "P1 source-readout route" in a3_placement)
    audit.check("placement discriminator keeps P1 open", "S_l = C_A3 * sigma([j])_c" in placement and "OPEN. The source chain currently supports exact" in placement)
    audit.check("precision firewall keeps correction theorem open", "multiplicative correction" in precision and "no retained correction theorem is supplied here" in precision)
    audit.check("P2 no-go remains alternate route only", "P2_WEAK_FRONT_MATCHING_RETAINED" in p2_no_go and "It is not P1" in note)
    audit.check("minimal axioms keep downstream structure outside axiom content", "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration" in minimal)
    audit.check("scale primitive excludes dimensionless correction", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector and empirical fit", "selector" in kinetic and "empirical fit" in kinetic)
    audit.check("realized primitive excludes state-contingent content", "state-contingent content" in realized and "normalization rule" in realized)

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    for absent in [
        "source_readout_correction_primitive",
        "source_nonuniform_ray_primitive",
        "a3_correction_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in nodes)

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
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", marker in note)

    explicit_non_claims = [
        "No derivation of `C_A3 = 0.999678091...`.",
        "No derivation of `N_A3 = 256.082435...`.",
        "No derivation or ratification of `P1_SOURCE_READOUT_CORRECTION_RETAINED`.",
        "No derivation of a corrected source-readout theorem.",
        "No derivation of a nonuniform source ray with singleton `1/N_A3`.",
        "No use of observed `m_W`, observed charged-lepton masses, fitted `a_l`, or",
        "No derivation of `m_e`, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `C_A3`",
        "P1 source-readout correction is retained",
        "P1_SOURCE_READOUT_CORRECTION_RETAINED is supplied",
        "corrected source readout is retained",
        "This note claims hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
