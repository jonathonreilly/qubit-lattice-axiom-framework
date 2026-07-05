#!/usr/bin/env python3
"""Verifier for the zero-import hydrogen R-Lep threshold no-go."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ALPHA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
ALPHA_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ALPHA0_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
QED_LOOP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md"
MASS_SPECTRUM_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md"
THRESHOLD_MAP_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLD_MOMENT_MAP_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PHYSICAL_ELECTRON_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
BRANCH_MASS_MAP = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ABSOLUTE_SCALE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
LANE2_FIREWALL = ROOT / "docs" / "ATOMIC_LANE2_QED_RUNNING_DEPENDENCY_FIREWALL_NOTE_2026-04-30.md"
THRESHOLD_MOMENT = ROOT / "scripts" / "frontier_atomic_alpha0_threshold_moment_no_go.py"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

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

ALPHA0_INPUTS = {
    "ALPHA0_TRANSPORT_TEXT_LOCK",
    "ALPHA_MZ_RETAINED",
    "QED_LOOP_KERNEL_RETAINED",
    "R_LEP_THRESHOLDS_RETAINED",
    "R_Q_HEAVY_THRESHOLDS_RETAINED",
    "R_HAD_NP_RETAINED",
    "SCHEME_DECOUPLING_MATCHING_RETAINED",
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


def closes_r_lep(inputs: set[str]) -> bool:
    return R_LEP_INPUTS <= inputs


def closes_alpha0(inputs: set[str]) -> bool:
    return ALPHA0_INPUTS <= inputs


def lepton_weights() -> list[Fraction]:
    q_lep = Fraction(-1, 1)
    return [q_lep * q_lep, q_lep * q_lep, q_lep * q_lep]


def threshold_moment(logs: list[float]) -> float:
    weights = lepton_weights()
    return sum(float(weight) * log for weight, log in zip(weights, logs))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        ALPHA_TARGET,
        ALPHA_PACKET,
        ALPHA0_NO_GO,
        QED_LOOP_NO_GO,
        MASS_SPECTRUM_PACKET,
        THRESHOLD_MAP_PACKET,
        PHYSICAL_ELECTRON_PACKET,
        PHYSICAL_ELECTRON_NO_GO,
        BRANCH_MASS_MAP,
        ABSOLUTE_SCALE,
        LANE2_FIREWALL,
        THRESHOLD_MOMENT,
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
        "R-Lep Thresholds Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "R_LEP_THRESHOLDS_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "The R-Lep threshold target remains needed",
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
        "T_LEP_THRESHOLD_MOMENT_RETAINED",
        "T_lep = log(M_Z / m_e) + log(M_Z / m_mu) + log(M_Z / m_tau)",
        "sum_l N_c(l) Q_l^2 = 3",
        "b_lep = (4/3) * 3 = 4",
        "ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "mass-spectrum target remains needed",
        "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLD_MOMENT_MAP_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "threshold-moment map target remains needed",
        "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "primitive registry was checked",
        "Open PRs were refreshed on 2026-07-05 UTC after `#5015` opened and after",
        "clean/green status is not a prerequisite",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#4991` owner-governed Tier-A retirement | open",
        "No-Go Discipline Gate",
        "current-surface R-Lep non-supply boundary passes",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("R-Lep predicate checks")
    full_inputs = set(R_LEP_INPUTS)
    audit.check("full R-Lep contract accepts threshold handoff", closes_r_lep(full_inputs))
    for missing in sorted(R_LEP_INPUTS):
        reduced = set(R_LEP_INPUTS)
        reduced.remove(missing)
        audit.check(f"R-Lep handoff fails without {missing}", not closes_r_lep(reduced))
    accepted_subsets = [subset for subset in all_subsets(R_LEP_INPUTS) if closes_r_lep(subset)]
    audit.check("only full R-Lep subset closes threshold handoff", accepted_subsets == [full_inputs])
    audit.check(
        "R-Lep alone does not close alpha0",
        not closes_alpha0({"R_LEP_THRESHOLDS_RETAINED"}),
    )
    audit.check(
        "full alpha0 input set closes alpha0 predicate",
        closes_alpha0(set(ALPHA0_INPUTS)),
    )
    for missing in sorted(ALPHA0_INPUTS):
        reduced = set(ALPHA0_INPUTS)
        reduced.remove(missing)
        audit.check(f"alpha0 still fails without {missing}", not closes_alpha0(reduced))

    section("Finite charged-lepton threshold arithmetic")
    weights = lepton_weights()
    total_weight = sum(weights, Fraction(0, 1))
    b_lep = Fraction(4, 3) * total_weight
    audit.check("three charged leptons each have weight 1", weights == [Fraction(1, 1)] * 3)
    audit.check("charged-lepton weight sum is 3", total_weight == Fraction(3, 1))
    audit.check("charged-lepton b coefficient is 4", b_lep == Fraction(4, 1))

    logs_a = [4.0, 5.0, 6.0]
    logs_b = [4.0, 5.0, 7.0]
    moment_a = threshold_moment(logs_a)
    moment_b = threshold_moment(logs_b)
    audit.check("lepton moment is sum of three threshold logs", math.isclose(moment_a, 15.0))
    audit.check("moving one lepton threshold changes the moment", moment_b - moment_a == 1.0)
    logs_c = [3.0, 5.0, 7.0]
    logs_d = [4.0, 5.0, 6.0]
    audit.check(
        "equal product/equal log-sum gives same one-loop lepton moment",
        math.isclose(threshold_moment(logs_c), threshold_moment(logs_d)),
    )
    common_log = 5.0
    common_moment = threshold_moment([common_log] * 3)
    inverse_alpha_shift = (2.0 / (3.0 * math.pi)) * common_moment
    via_b = float(b_lep) * common_log / (2.0 * math.pi)
    audit.check(
        "lepton moment formula matches b_lep common-threshold running",
        math.isclose(inverse_alpha_shift, via_b, rel_tol=1e-12, abs_tol=1e-12),
    )

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    alpha_target = read(ALPHA_TARGET)
    alpha_packet = read(ALPHA_PACKET)
    alpha0_no_go = read(ALPHA0_NO_GO)
    qed_loop_no_go = read(QED_LOOP_NO_GO)
    mass_spectrum_packet = read(MASS_SPECTRUM_PACKET)
    threshold_map_packet = read(THRESHOLD_MAP_PACKET)
    physical_electron_packet = read(PHYSICAL_ELECTRON_PACKET)
    physical_electron_no_go = read(PHYSICAL_ELECTRON_NO_GO)
    branch_mass_map = read(BRANCH_MASS_MAP)
    absolute_scale = read(ABSOLUTE_SCALE)
    lane2_firewall = read(LANE2_FIREWALL)
    threshold_runner = read(THRESHOLD_MOMENT)
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()

    for container_name, container in [
        ("goal packet", goal),
        ("alpha target", alpha_target),
        ("alpha0 packet", alpha_packet),
        ("alpha0 no-go", alpha0_no_go),
    ]:
        audit.check(
            f"{container_name} references R-Lep no-go",
            NOTE.name in container and "R-Lep threshold target remains needed" in container,
        )

    audit.check("Lane 2 firewall names R-Lep as Lane 6 blocked", "R-Lep" in lane2_firewall and "Lane 6" in lane2_firewall)
    audit.check("threshold runner names charged-lepton thresholds", "charged-lepton threshold masses" in threshold_runner)
    audit.check("QED loop no-go keeps loop separate", "QED_LOOP_KERNEL_RETAINED" in qed_loop_no_go)
    audit.check("R-Lep no-go references mass-spectrum packet", MASS_SPECTRUM_PACKET.name in note and "mass-spectrum target remains needed" in note)
    audit.check(
        "mass-spectrum packet supplies conditional R-Lep mass inputs",
        "PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED" in mass_spectrum_packet
        and "PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED" in mass_spectrum_packet,
    )
    audit.check("R-Lep no-go references threshold-map packet", THRESHOLD_MAP_PACKET.name in note and "threshold-moment map target remains needed" in note)
    audit.check(
        "threshold-map packet supplies conditional R-Lep map input",
        "LEPTON_THRESHOLD_MOMENT_MAP_RETAINED" in threshold_map_packet
        and "does not ratify R-Lep thresholds" in threshold_map_packet,
    )
    audit.check("physical electron packet is electron-specific", "PHYSICAL_ELECTRON_READOUT_RETAINED" in physical_electron_packet)
    audit.check("physical electron no-go keeps electron mass open", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in physical_electron_no_go)
    audit.check("branch mass map is not species/scale closure", "PHASE_SCALE_SPECIES_SCOPE_LOCK" in branch_mass_map)
    audit.check("absolute scale packet is not branch/species closure", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in absolute_scale)

    nodes = registry["nodes"]
    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    for absent in [
        "r_lep_thresholds_primitive",
        "charged_lepton_mass_spectrum_primitive",
        "alpha0_primitive",
        "qed_loop_kernel_primitive",
    ]:
        audit.check(f"no registered R-Lep shortcut: {absent}", absent not in registry_text)
    audit.check("minimal axioms exclude source/action bridges", "source/action" in minimal)
    audit.check("scale primitive excludes dimensionless masses", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes couplings/masses", "mass ratio" in kinetic and "coupling" in kinetic)
    audit.check("realized primitive excludes values", "or value is supplied" in realized)

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
        "No derivation or ratification of `R_LEP_THRESHOLDS_RETAINED`.",
        "No derivation or ratification of `T_LEP_THRESHOLD_MOMENT_RETAINED`.",
        "No derivation or ratification of a physical charged-lepton mass triple.",
        "No derivation or ratification of `m_e`, `m_mu`, or `m_tau`.",
        "No derivation or ratification of the physical charged-lepton species labels.",
        "No derivation or ratification of the QED loop kernel.",
        "No derivation or ratification of `ALPHA0_TRANSPORT_RETAINED`.",
        "No derivation or ratification of `ALPHA0_RETAINED`.",
        "No derivation or ratification of `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`.",
        "No derivation of static-source Rydberg or retained hydrogen.",
        "No use of observed `alpha(0)`, Rydberg, PDG masses, fitted thresholds, or",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note ratifies charged-lepton thresholds",
        "R_LEP_THRESHOLDS_RETAINED is supplied",
        "T_LEP_THRESHOLD_MOMENT_RETAINED is supplied",
        "alpha(0) is retained",
        "retained hydrogen calculation is complete",
        "PDG masses are proof inputs",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
