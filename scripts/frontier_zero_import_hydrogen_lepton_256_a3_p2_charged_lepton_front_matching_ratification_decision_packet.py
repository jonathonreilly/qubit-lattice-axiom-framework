#!/usr/bin/env python3
"""Verifier for the A3 P2 charged-lepton front-matching decision packet.

This runner checks that the P2 front-matching handoff is explicit and remains
separate from the actual matching theorem, A3 placement, K4 scale assembly,
physical electron mass, alpha(0), static-source Rydberg, and hydrogen.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
WEAK_FRONT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
D17_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_D17_BLOCK_NORMALIZATION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SU2_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_SU2_COUPLING_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
EXACT_SOURCE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_RATIFICATION_DECISION_PACKET_2026-07-05.md"
A3_P2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md"
A3_P2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_NO_DOUBLE_COUNT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_NO_DOUBLE_COUNT_COMPOSITION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SU2_BETA = ROOT / "docs" / "SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md"
EW_HIGGS = ROOT / "docs" / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
PRECISION_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md"
PLACEMENT_DISCRIMINATOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
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


P2_MATCHING_INPUTS = {
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

A3_DECISION_INPUTS = {
    "A3_PLACEMENT_TEXT_LOCK",
    "EXACT_SOURCE_SCAFFOLD_STATUS",
    "ONE_PLACEMENT_SELECTED",
    "PLACEMENT_THEOREM_RETAINED",
    "NO_SOURCE_DOUBLE_COUNT",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

K4_INPUTS = {
    "K4_SCALE_TEXT_LOCK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "WEAK_FRONT_BASE_RETAINED",
    "EXACT_SOURCE_SINGLETON_RETAINED",
    "A3_PRECISION_PLACEMENT_RETAINED",
    "NO_SOURCE_A3_DOUBLE_COUNT",
    "NO_COMPARATOR_PROOF_INPUT",
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


def closes_p2_matching(inputs: set[str]) -> bool:
    return P2_MATCHING_INPUTS <= inputs


def closes_a3_with_p2(inputs: set[str], p2_retained: bool) -> bool:
    return A3_DECISION_INPUTS <= inputs and p2_retained


def closes_k4(inputs: set[str]) -> bool:
    return K4_INPUTS <= inputs


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
        WEAK_FRONT_DECISION,
        D17_DECISION,
        SU2_DECISION,
        EXACT_SOURCE_DECISION,
        A3_P2_TARGET,
        A3_P2_NO_GO,
        A3_DECISION,
        A3_NO_GO,
        A3_NO_DOUBLE_COUNT,
        SU2_BETA,
        EW_HIGGS,
        PRECISION_FIREWALL,
        PLACEMENT_DISCRIMINATOR,
        LEPTON_SCALE,
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

    section("Required packet content")
    required_phrases = [
        "A3 P2 Charged-Lepton Front-Matching Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify charged-lepton front matching",
        "the charged-lepton P2 front-matching theorem",
        "F_phys = C_A3 * F_0",
        "F_0 = g_2 * (1/sqrt(2))",
        "N_A3 = 256.08243522600384",
        "C_A3 = 256 / N_A3 = 0.9996780910571587",
        "delta_front = C_A3 - 1 = -0.0003219089428413424",
        "Delta(1/alpha_2) ~= 0.01899279085",
        "b_2 = 19/6",
        "ell_A3 ~= 0.03768480771",
        "exp(ell_A3) ~= 1.038403884",
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
        "No proper subset of those ten contract inputs",
        "CHARGED_LEPTON_FRONT_MATCHING_RETAINED",
        "P2_WEAK_FRONT_MATCHING_RETAINED",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "PHYSICAL_ELECTRON_READOUT_RETAINED",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
        "STATIC_SOURCE_RYDBERG_RETAINED",
        "(C * F_0) * S_0",
        "F_0 * S_0",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` domain-wall chiral edge from achiral bulk | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#5006` static-source I1 hygiene companion | open",
        "The primitive registry was checked",
        "weak_front_matching_primitive",
        "a3_correction_primitive",
        "charged_lepton_front_matching_primitive",
        "No-Go Discipline Gate",
        "decision-ready ratification contract",
        "broad P2-retention claim fails; narrowed P2 decision-packet",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_p2 = set(P2_MATCHING_INPUTS)
    audit.check("full P2 matching contract accepts handoff", closes_p2_matching(full_p2))
    for missing in sorted(P2_MATCHING_INPUTS):
        reduced = set(P2_MATCHING_INPUTS)
        reduced.remove(missing)
        audit.check(f"P2 matching handoff fails without {missing}", not closes_p2_matching(reduced))
    accepted_subsets = [subset for subset in all_subsets(P2_MATCHING_INPUTS) if closes_p2_matching(subset)]
    audit.check("only full tested P2 subset closes front matching", accepted_subsets == [full_p2])

    p2_consequence = {"CHARGED_LEPTON_FRONT_MATCHING_RETAINED", "P2_WEAK_FRONT_MATCHING_RETAINED"}
    audit.check("P2 consequence alone does not close A3", not closes_a3_with_p2(p2_consequence, True))
    audit.check("A3 contract plus P2 retained closes A3 model", closes_a3_with_p2(set(A3_DECISION_INPUTS), True))
    audit.check("A3 contract without P2 retained stays open", not closes_a3_with_p2(set(A3_DECISION_INPUTS), False))
    audit.check("P2 consequence alone does not close K4", not closes_k4(p2_consequence))
    audit.check("full K4 predicate model closes K4", closes_k4(set(K4_INPUTS)))

    section("Finite target arithmetic checks")
    a2 = a_lepton_squared()
    n_a3 = M_W / a2
    c_a3 = 256.0 / n_a3
    delta_front = c_a3 - 1.0
    g2, front, alpha2 = weak_front_components()
    inv_alpha2 = 1.0 / alpha2
    delta_inv_alpha2 = inv_alpha2 * (1.0 / (c_a3 * c_a3) - 1.0)
    ell_a3 = delta_inv_alpha2 * (2.0 * math.pi) / B2
    scale_ratio = math.exp(ell_a3)
    s0 = 1.0 / 256.0
    corrected = c_a3 * front * s0
    uncorrected = front * s0
    double_count = c_a3 * c_a3 * front * s0

    audit.check("repo a_lepton^2 comparator reproduced", abs(a2 - 313.8411267023086) < 1e-10)
    audit.check("A3 divisor target reproduced", abs(n_a3 - 256.08243522600384) < 1e-10)
    audit.check("C_A3 target reproduced", abs(c_a3 - 0.9996780910571587) < 1e-15)
    audit.check("front delta target reproduced", abs(delta_front + 0.0003219089428413424) < 1e-15)
    audit.check("g2 target arithmetic reproduced", abs(g2 - 0.6528252293493516) < 1e-14)
    audit.check("inverse alpha2 target shift reproduced", abs(delta_inv_alpha2 - 0.018992790852657246) < 1e-15)
    audit.check("A3 target log reproduced", abs(ell_a3 - 0.03768480771402659) < 1e-15)
    audit.check("A3 target scale ratio reproduced", abs(scale_ratio - 1.0384038843982628) < 1e-15)
    audit.check("P2 corrected product differs by one C_A3 factor", abs(corrected / uncorrected - c_a3) < 1e-15)
    audit.check("double-count product differs from one-correction product", double_count != corrected and abs(double_count / corrected - c_a3) < 1e-15)

    section("Authority boundary checks")
    goal = read(GOAL)
    k4_packet = read(K4_PACKET)
    weak_front = read(WEAK_FRONT_DECISION)
    d17 = read(D17_DECISION)
    su2 = read(SU2_DECISION)
    exact_source = read(EXACT_SOURCE_DECISION)
    p2_target = read(A3_P2_TARGET)
    p2_no_go = read(A3_P2_NO_GO)
    a3_decision = read(A3_DECISION)
    a3_no_go = read(A3_NO_GO)
    no_double_count = read(A3_NO_DOUBLE_COUNT)
    su2_beta = read(SU2_BETA)
    ew_higgs = read(EW_HIGGS)
    precision = read(PRECISION_FIREWALL)
    placement = read(PLACEMENT_DISCRIMINATOR)
    lepton_scale = read(LEPTON_SCALE)
    registry = json.loads(read(REGISTRY))
    tier_a = read(TIER_A)
    minimal = flat(read(MINIMAL))
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("K4 packet", k4_packet),
        ("A3 decision packet", a3_decision),
        ("A3 current no-go", a3_no_go),
        ("P2 current no-go", p2_no_go),
    ]:
        audit.check(f"{container_name} references P2 decision packet", NOTE.name in container)

    audit.check("weak-front decision keeps C_A3 out", "does not supply the small `C_A3` front/matching" in weak_front)
    audit.check("D17 decision is below P2 matching", all(token in d17 for token in ["No source singleton", "A3 placement", "K4 scale", "hydrogen result"]))
    audit.check("SU2 context decision is below P2 matching", all(token in su2 for token in ["threshold matching", "D17 normalization", "source singleton", "A3 placement"]))
    audit.check("exact-source decision keeps A3 downstream", "A3 placement, K4 scale assembly" in exact_source)
    audit.check("P2 target identifies target but not theorem", "CHARGED_LEPTON_FRONT_MATCHING_RETAINED" in p2_target and "No derivation of a finite matching or scheme correction." in p2_target)
    audit.check("P2 no-go names missing theorem", "MATCHING_THEOREM_RETAINED" in p2_no_go and "current surfaces do not supply" in p2_no_go)
    audit.check("A3 decision accepts exactly one placement", "ONE_PLACEMENT_SELECTED" in a3_decision and "P2_WEAK_FRONT_MATCHING_RETAINED" in a3_decision)
    audit.check("A3 no-go keeps retained placement unsupplied", "A3_PRECISION_PLACEMENT_RETAINED" in a3_no_go and "current retained, primitive, and open-PR surfaces do not supply" in a3_no_go)
    audit.check("no-double-count packet stays composition-only", "NO_SOURCE_A3_DOUBLE_COUNT" in no_double_count and "does not select P1/P2/P3/P4" in no_double_count)
    audit.check("SU2 beta note supplies slope only", "`b_2 = 19/6`" in su2_beta and "one structural ingredient" in su2_beta)
    audit.check("EW Higgs note keeps numerical values downstream", "numerical values of `g_2(v)`" in flat(ew_higgs) and "remain downstream lanes" in flat(ew_higgs))
    audit.check("precision firewall keeps correction theorem open", "running/threshold route" in precision and "no retained charged-lepton scale-running law is supplied here" in precision)
    audit.check("placement discriminator keeps P2 open", "P2 front-factor/threshold correction" in placement and "no retained charged-lepton threshold theorem is supplied here" in placement)
    audit.check("lepton-scale probe is factorization context", "g_2" in lepton_scale and "1/sqrt(2)" in lepton_scale and "1/256" in lepton_scale)
    audit.check("K4 packet references new P2 handoff", NOTE.name in k4_packet and "MATCHING_THEOREM_RETAINED" in k4_packet)

    audit.check("minimal axioms keep downstream structure outside axiom content", "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration" in minimal)
    audit.check("scale primitive excludes dimensionless correction", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector and empirical fit", "selector" in kinetic and "empirical fit" in kinetic)
    audit.check("realized primitive excludes normalization rule", "normalization rule" in realized and "state-contingent content" in realized)

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
        "charged_lepton_front_matching_primitive",
        "charged_lepton_scale_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)
    audit.check("Tier-A admissions are not primitive shortcuts", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in nodes)

    section("Non-claim boundaries")
    explicit_non_claims = [
        "No derivation or ratification of `CHARGED_LEPTON_FRONT_MATCHING_RETAINED`.",
        "No derivation or ratification of `P2_WEAK_FRONT_MATCHING_RETAINED`.",
        "No derivation or ratification of `A3_PRECISION_PLACEMENT_RETAINED`.",
        "No derivation of `C_A3 = 0.999678091...`.",
        "No derivation of `N_A3 = 256.082435...`.",
        "No derivation of a finite threshold, pole, running-interval, or scheme",
        "No use of observed `m_W`, observed charged-lepton masses, fitted `a_l`,",
        "No derivation or ratification of the absolute charged-lepton scale.",
        "No derivation of `m_e`, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet derives `C_A3`",
        "This packet derives `N_A3`",
        "This packet ratifies charged-lepton front matching",
        "This packet claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
