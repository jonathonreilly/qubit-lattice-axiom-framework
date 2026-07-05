#!/usr/bin/env python3
"""Verifier for the R-Lep threshold-moment map decision packet."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLD_MOMENT_MAP_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
R_LEP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
MASS_SPECTRUM_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md"
ALPHA0_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
QED_LOOP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md"
THRESHOLD_RUNNER = ROOT / "scripts" / "frontier_atomic_alpha0_threshold_moment_no_go.py"
SCALE_REFERENCE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"


MAP_INPUTS = {
    "LEPTON_THRESHOLD_MOMENT_MAP_TEXT_LOCK",
    "CHARGED_LEPTON_QED_WEIGHT_ALGEBRA_RETAINED",
    "PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_DOMAIN_LOCK",
    "PHYSICAL_CHARGED_LEPTON_SPECIES_LABEL_DOMAIN_LOCK",
    "ALPHA_MZ_REFERENCE_SCALE_INTERFACE_LOCK",
    "ONE_LOOP_THRESHOLD_LOG_MAP_RETAINED",
    "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
    "NO_THRESHOLD_VALUE_PROOF_INPUT",
    "NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

R_LEP_INPUTS = {
    "R_LEP_THRESHOLDS_TEXT_LOCK",
    "ALPHA_MZ_SCALE_CONTEXT_RETAINED",
    "PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED",
    "PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED",
    "LEPTON_THRESHOLD_MOMENT_MAP_RETAINED",
    "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
    "NO_PDG_LEPTON_MASS_PROOF_INPUT",
    "NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT",
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


def closes_map(inputs: set[str]) -> bool:
    return MAP_INPUTS <= inputs


def closes_r_lep(inputs: set[str]) -> bool:
    return R_LEP_INPUTS <= inputs


def lepton_weights() -> list[Fraction]:
    q = Fraction(-1, 1)
    return [q * q, q * q, q * q]


def t_lep(m_z: float, masses: list[float]) -> float:
    return sum(math.log(m_z / mass) for mass in masses)


def inv_alpha_lep_shift(moment: float) -> float:
    return (2.0 / (3.0 * math.pi)) * moment


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        R_LEP_NO_GO,
        MASS_SPECTRUM_PACKET,
        ALPHA0_PACKET,
        QED_LOOP_NO_GO,
        THRESHOLD_RUNNER,
        SCALE_REFERENCE,
        REGISTRY,
        MINIMAL,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required note content")
    required_phrases = [
        "R-Lep Threshold-Moment Map Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify R-Lep thresholds",
        "LEPTON_THRESHOLD_MOMENT_MAP_RETAINED",
        "the charged-lepton one-loop threshold-moment map consumed by the zero-import",
        "TM.1",
        "TM.2",
        "TM.3",
        "TM.4",
        "TM.5",
        "TM.6",
        "LEPTON_THRESHOLD_MOMENT_MAP_TEXT_LOCK",
        "CHARGED_LEPTON_QED_WEIGHT_ALGEBRA_RETAINED",
        "PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_DOMAIN_LOCK",
        "PHYSICAL_CHARGED_LEPTON_SPECIES_LABEL_DOMAIN_LOCK",
        "ALPHA_MZ_REFERENCE_SCALE_INTERFACE_LOCK",
        "ONE_LOOP_THRESHOLD_LOG_MAP_RETAINED",
        "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
        "NO_THRESHOLD_VALUE_PROOF_INPUT",
        "NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those twelve contract inputs",
        "R_LEP_THRESHOLDS_TEXT_LOCK",
        "T_LEP_THRESHOLD_MOMENT_RETAINED",
        "R_LEP_THRESHOLDS_RETAINED",
        "sum_l N_c(l) Q_l^2 = 3",
        "b_lep = (4/3) * 3 = 4",
        "T_lep(M_Z; m_e,m_mu,m_tau)",
        "log(M_Z^3 / (m_e m_mu m_tau))",
        "Open PRs were refreshed on 2026-07-05 UTC after `#5015` opened and after",
        "clean/green status is not a prerequisite",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#4991` owner-governed Tier-A retirement | open",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "decision-ready ratification",
        "broad threshold-moment-retention claim fails; narrowed",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(MAP_INPUTS)
    audit.check("full threshold-map contract accepts handoff", closes_map(full_inputs))
    for missing in sorted(MAP_INPUTS):
        reduced = set(MAP_INPUTS)
        reduced.remove(missing)
        audit.check(f"threshold-map handoff fails without {missing}", not closes_map(reduced))
    accepted_subsets = [subset for subset in all_subsets(MAP_INPUTS) if closes_map(subset)]
    audit.check("only full threshold-map subset closes handoff", accepted_subsets == [full_inputs])

    map_consequence = {"LEPTON_THRESHOLD_MOMENT_MAP_RETAINED"}
    audit.check("map consequence alone does not close R-Lep", not closes_r_lep(map_consequence))
    audit.check("full R-Lep predicate closes with all inputs", closes_r_lep(set(R_LEP_INPUTS)))
    for missing in sorted(R_LEP_INPUTS):
        reduced = set(R_LEP_INPUTS)
        reduced.remove(missing)
        audit.check(f"R-Lep still fails without {missing}", not closes_r_lep(reduced))

    section("Finite threshold-map arithmetic")
    weights = lepton_weights()
    audit.check("three charged-lepton weights are all 1", weights == [Fraction(1, 1)] * 3)
    audit.check("charged-lepton weight sum is 3", sum(weights, Fraction(0, 1)) == Fraction(3, 1))
    audit.check("charged-lepton b coefficient is 4", Fraction(4, 3) * sum(weights, Fraction(0, 1)) == Fraction(4, 1))

    m_z = 100.0
    masses_a = [1.0, 2.0, 5.0]
    masses_b = [1.0, 2.0, 10.0]
    moment_a = t_lep(m_z, masses_a)
    moment_b = t_lep(m_z, masses_b)
    audit.check("threshold moment equals log product form", abs(moment_a - math.log(m_z**3 / math.prod(masses_a))) < 1e-12)
    audit.check("moving one mass changes threshold moment", abs((moment_b - moment_a) + math.log(2.0)) < 1e-12)
    audit.check("permuting equal-weight lepton masses leaves one-loop moment", abs(t_lep(m_z, masses_a) - t_lep(m_z, list(reversed(masses_a)))) < 1e-12)
    scale = 7.0
    audit.check("common unit rescale leaves threshold moment", abs(t_lep(scale * m_z, [scale * m for m in masses_a]) - moment_a) < 1e-12)
    common_log = 5.0
    common_moment = 3.0 * common_log
    via_moment = inv_alpha_lep_shift(common_moment)
    via_b = 4.0 * common_log / (2.0 * math.pi)
    audit.check("lepton moment formula matches b_lep common-threshold running", abs(via_moment - via_b) < 1e-12)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    r_lep = read(R_LEP_NO_GO)
    mass_spectrum = read(MASS_SPECTRUM_PACKET)
    alpha0_packet = read(ALPHA0_PACKET)
    qed_loop_no_go = read(QED_LOOP_NO_GO)
    threshold_runner = read(THRESHOLD_RUNNER)
    scale_reference = flat(read(SCALE_REFERENCE)).lower()
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("R-Lep no-go", r_lep),
    ]:
        audit.check(f"{container_name} references threshold-map packet", NOTE.name in container)

    audit.check("R-Lep no-go names map input", "LEPTON_THRESHOLD_MOMENT_MAP_RETAINED" in r_lep)
    audit.check("mass-spectrum packet keeps threshold map separate", "LEPTON_THRESHOLD_MOMENT_MAP_RETAINED" in mass_spectrum and "does not ratify R-Lep thresholds" in mass_spectrum)
    audit.check("alpha0 packet consumes R-Lep, not map directly", "R_LEP_THRESHOLDS_RETAINED" in alpha0_packet)
    audit.check("QED loop no-go keeps loop separate", "QED_LOOP_KERNEL_RETAINED" in qed_loop_no_go)
    audit.check("threshold runner remains no-go/witness", "does not fix the logarithms" in threshold_runner)
    audit.check("scale primitive has zero dimensionless content", "zero dimensionless content" in scale_reference and "mass ratio" in scale_reference)
    audit.check("minimal axioms require downstream bridges", "Further physical\nstructure requires derivation" in minimal)

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    for absent in [
        "lepton_threshold_moment_map_primitive",
        "r_lep_thresholds_primitive",
        "charged_lepton_mass_spectrum_primitive",
        "alpha0_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5015` wave-collapse-block01 measurement-collapse gate | open",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` chirality domain-wall free-field note | open",
        "`#5011` eta twisted walk family runner | open",
        "`#5010` YT P1 I_s re-audit packet bridge repair | open",
        "`#5009` S3 spacetime tensor primitive runner | open",
        "`#5008` quark mass-ratio CP probe repair | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#5006` static-source I1 hygiene companion | open",
        "`#4991` owner-governed Tier-A retirement | open",
    ]
    for marker in latest_pr_markers:
        audit.check(f"opened PR marker present: {marker}", flat(marker) in note_flat)
    audit.check("open PR check does not require clean status", "clean/green status is not a prerequisite" in note)

    explicit_non_claims = [
        "No derivation or ratification of `LEPTON_THRESHOLD_MOMENT_MAP_RETAINED`.",
        "No derivation or ratification of `T_LEP_THRESHOLD_MOMENT_RETAINED`.",
        "No derivation or ratification of `R_LEP_THRESHOLDS_RETAINED`.",
        "No derivation or ratification of a physical charged-lepton mass triple.",
        "No derivation or ratification of `m_e`, `m_mu`, or `m_tau`.",
        "No derivation or ratification of the QED loop kernel.",
        "No derivation or ratification of `ALPHA0_TRANSPORT_RETAINED`.",
        "No derivation or ratification of `ALPHA0_RETAINED`.",
        "No derivation of static-source Rydberg or retained hydrogen.",
        "No use of observed `alpha(0)`, Rydberg, PDG lepton masses, fitted",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies R-Lep thresholds",
        "LEPTON_THRESHOLD_MOMENT_MAP_RETAINED is supplied",
        "T_LEP_THRESHOLD_MOMENT_RETAINED is supplied",
        "R_LEP_THRESHOLDS_RETAINED is supplied",
        "alpha(0) is retained",
        "hydrogen is retained",
        "PDG lepton masses are proof inputs",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
