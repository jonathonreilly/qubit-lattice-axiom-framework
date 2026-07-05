#!/usr/bin/env python3
"""Verifier for the A3 P2 charged-lepton front-matching current-surface no-go.

This runner checks that the current hydrogen-facing surfaces do not silently
supply the P2 matching theorem needed for C_A3. It preserves P2 as an open
route and does not derive C_A3, m_e, alpha(0), or hydrogen.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
WEAK_FRONT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
A3_P2 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md"
A3_PLACEMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PRECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md"
PLACEMENT_DISCRIMINATOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
SU2_BETA = ROOT / "docs" / "SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md"
EW_HIGGS = ROOT / "docs" / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
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
G_F = 1.1663787e-5
B2 = 19.0 / 6.0

FRONT_MATCHING_INPUTS = {
    "P2_MATCHING_TEXT_LOCK",
    "WEAK_FRONT_BASE_RETAINED",
    "EXACT_SOURCE_SINGLETON_RETAINED",
    "MATCHING_THEOREM_RETAINED",
    "P2_PLACEMENT_SELECTED",
    "NO_SOURCE_DOUBLE_COUNT",
    "NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

P2_CLOSURE_INPUTS = {
    "EXACT_SOURCE_SINGLETON_RETAINED",
    "WEAK_FRONT_BASE_RETAINED",
    "CHARGED_LEPTON_FRONT_MATCHING_RETAINED",
    "NO_SOURCE_DOUBLE_COUNT",
    "NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT",
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


def closes_front_matching(inputs: set[str]) -> bool:
    return FRONT_MATCHING_INPUTS <= inputs


def closes_p2(inputs: set[str]) -> bool:
    return P2_CLOSURE_INPUTS <= inputs


def a_lepton_squared() -> float:
    a = (math.sqrt(M_E) + math.sqrt(M_MU) + math.sqrt(M_TAU)) / 3.0
    return a * a


def weak_front_components() -> tuple[float, float, float]:
    v_mev = (1.0 / (math.sqrt(2.0) * G_F)) ** 0.5 * 1000.0
    g2 = 2.0 * M_W / v_mev
    front = g2 / math.sqrt(2.0)
    alpha2 = g2 * g2 / (4.0 * math.pi)
    return g2, front, alpha2


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        K4_PACKET,
        WEAK_FRONT,
        A3_P2,
        A3_PLACEMENT,
        PRECISION,
        PLACEMENT_DISCRIMINATOR,
        LEPTON_SCALE,
        SU2_BETA,
        EW_HIGGS,
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
        "A3 P2 Charged-Lepton Front-Matching Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not derive `C_A3`",
        "CHARGED_LEPTON_FRONT_MATCHING_RETAINED",
        "P2_MATCHING_TEXT_LOCK",
        "WEAK_FRONT_BASE_RETAINED",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "MATCHING_THEOREM_RETAINED",
        "P2_PLACEMENT_SELECTED",
        "NO_SOURCE_DOUBLE_COUNT",
        "NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "N_A3 = 256.08243522600384",
        "C_A3 = 256 / N_A3 = 0.9996780910571587",
        "delta_front = C_A3 - 1 = -0.0003219089428413424",
        "Delta(1/alpha_2) ~= 0.01899279085",
        "b_2 = 19/6",
        "ell_A3 ~= 0.03768480771",
        "exp(ell_A3) ~= 1.038403884",
        "The primitive registry was checked",
        "weak_front_matching_primitive",
        "a3_correction_primitive",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "No-Go Discipline Gate",
        "broad P2 no-go fails; narrowed current-surface non-supply claim passes",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("P2 matching predicate checks")
    full_inputs = set(FRONT_MATCHING_INPUTS)
    audit.check("full P2 matching contract accepts front matching", closes_front_matching(full_inputs))
    for missing in sorted(FRONT_MATCHING_INPUTS):
        reduced = set(FRONT_MATCHING_INPUTS)
        reduced.remove(missing)
        audit.check(f"P2 matching fails without {missing}", not closes_front_matching(reduced))
    accepted_subsets = [subset for subset in all_subsets(FRONT_MATCHING_INPUTS) if closes_front_matching(subset)]
    audit.check("only full P2 matching subset closes front matching", accepted_subsets == [full_inputs])
    current_surface = {
        "WEAK_FRONT_BASE_RETAINED",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "P2_PLACEMENT_SELECTED",
        "NO_SOURCE_DOUBLE_COUNT",
        "NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    }
    audit.check("current surface without matching theorem does not close front matching", not closes_front_matching(current_surface))
    audit.check("P2 closure fails without CHARGED_LEPTON_FRONT_MATCHING_RETAINED", not closes_p2(P2_CLOSURE_INPUTS - {"CHARGED_LEPTON_FRONT_MATCHING_RETAINED"}))
    audit.check("full P2 closure predicate still closes when matching is retained", closes_p2(set(P2_CLOSURE_INPUTS)))

    section("Target arithmetic checks")
    a2 = a_lepton_squared()
    n_a3 = M_W / a2
    c_a3 = 256.0 / n_a3
    delta_front = c_a3 - 1.0
    g2, front, alpha2 = weak_front_components()
    inv_alpha2 = 1.0 / alpha2
    delta_inv_alpha2 = inv_alpha2 * (1.0 / (c_a3 * c_a3) - 1.0)
    ell_a3 = delta_inv_alpha2 * (2.0 * math.pi) / B2
    scale_ratio = math.exp(ell_a3)
    p2_product = c_a3 * front / 256.0
    uncorrected_product = front / 256.0

    audit.check("repo a_lepton^2 comparator reproduced", abs(a2 - 313.8411267023086) < 1e-10)
    audit.check("A3 empirical divisor reproduced", abs(n_a3 - 256.08243522600384) < 1e-10)
    audit.check("C_A3 target reproduced", abs(c_a3 - 0.9996780910571587) < 1e-15)
    audit.check("front delta target reproduced", abs(delta_front + 0.0003219089428413424) < 1e-15)
    audit.check("weak g2 comparator reproduced only as target arithmetic", abs(g2 - 0.6528252293493516) < 1e-14)
    audit.check("inverse alpha2 shift reproduced", abs(delta_inv_alpha2 - 0.018992790852657246) < 1e-15)
    audit.check("one-loop target log reproduced", abs(ell_a3 - 0.03768480771402659) < 1e-15)
    audit.check("one-loop target scale ratio reproduced", abs(scale_ratio - 1.0384038843982628) < 1e-15)
    audit.check("P2 correction changes uncorrected product", p2_product != uncorrected_product and abs(p2_product / uncorrected_product - c_a3) < 1e-15)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    k4_packet = read(K4_PACKET)
    weak_front = read(WEAK_FRONT)
    a3_p2 = read(A3_P2)
    a3_placement = read(A3_PLACEMENT)
    precision = read(PRECISION)
    placement_discriminator = read(PLACEMENT_DISCRIMINATOR)
    lepton_scale = read(LEPTON_SCALE)
    su2_beta = read(SU2_BETA)
    ew_higgs = read(EW_HIGGS)
    minimal = flat(read(MINIMAL))
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    tier_a = read(TIER_A)
    nodes = registry["nodes"]

    audit.check("goal packet references A3 P2 current-surface no-go", NOTE.name in goal and "CHARGED_LEPTON_FRONT_MATCHING_RETAINED" in goal)
    audit.check("K4 packet keeps A3 matching downstream", "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md" in k4_packet)
    audit.check("weak-front packet explicitly excludes matching", "does not supply the small `C_A3` front/matching" in weak_front)
    audit.check("A3 P2 target says matching theorem is required", "CHARGED_LEPTON_FRONT_MATCHING_RETAINED" in a3_p2 and "No derivation of a finite matching or scheme correction." in a3_p2)
    audit.check("A3 placement packet keeps P2 theorem open", "P2_WEAK_FRONT_MATCHING_RETAINED" in a3_placement and "The target log is known, but the theorem is not supplied here." in a3_placement)
    audit.check("precision firewall keeps running/threshold open", "running/threshold route" in precision and "no retained charged-lepton scale-running law is supplied here" in precision)
    audit.check("placement discriminator keeps P2 open", "no retained charged-lepton threshold theorem is supplied here" in placement_discriminator)
    audit.check("lepton-scale probe factorization is not retained theorem", "audited-clean open-gate relation" in lepton_scale and "g_2 · (1/sqrt(2)) · (1/256)" in lepton_scale)
    audit.check("SU2 beta supplies slope not interval", "`b_2 = 19/6`" in su2_beta and "one structural ingredient" in su2_beta)
    audit.check("EW Higgs keeps numerical values downstream", "numerical values of `g_2(v)`" in flat(ew_higgs) and "remain downstream lanes" in flat(ew_higgs))
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
        "weak_front_matching_primitive",
        "a3_correction_primitive",
        "charged_lepton_scale_primitive",
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
        "No derivation or ratification of `CHARGED_LEPTON_FRONT_MATCHING_RETAINED`.",
        "No derivation or ratification of `P2_WEAK_FRONT_MATCHING_RETAINED`.",
        "No derivation of a finite threshold, pole, or scheme matching theorem.",
        "No use of observed `m_W`, observed charged-lepton masses, fitted `a_l`, or",
        "No derivation of `m_e`, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `C_A3`",
        "charged-lepton front matching is retained",
        "P2 weak-front matching is retained",
        "CHARGED_LEPTON_FRONT_MATCHING_RETAINED is supplied",
        "This note claims hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
