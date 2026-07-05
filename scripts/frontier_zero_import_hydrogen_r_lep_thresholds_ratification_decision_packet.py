#!/usr/bin/env python3
"""Verifier for the R-Lep thresholds decision packet."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
R_LEP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
MASS_SPECTRUM_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md"
THRESHOLD_MAP_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLD_MOMENT_MAP_RATIFICATION_DECISION_PACKET_2026-07-05.md"
ALPHA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
ALPHA_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ALPHA0_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
QED_LOOP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PHYSICAL_ELECTRON_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
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

SPECTRUM_CONSEQUENCE = {
    "PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED",
    "PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED",
    "CHARGED_LEPTON_MASS_SPECTRUM_RETAINED",
}

MAP_CONSEQUENCE = {"LEPTON_THRESHOLD_MOMENT_MAP_RETAINED"}

R_LEP_CONSEQUENCE = {
    "R_LEP_THRESHOLDS_RETAINED",
    "T_LEP_THRESHOLD_MOMENT_RETAINED",
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

STATIC_SOURCE_INPUTS = {
    "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
    "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
    "ATOMIC_OPERATOR_HARNESS_VERIFIED",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
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


def closes_static_source(inputs: set[str]) -> bool:
    return STATIC_SOURCE_INPUTS <= inputs


def lepton_weights() -> list[Fraction]:
    q = Fraction(-1, 1)
    return [q * q, q * q, q * q]


def t_lep(m_z: float, masses: list[float]) -> float:
    return sum(math.log(m_z / mass) for mass in masses)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        R_LEP_NO_GO,
        MASS_SPECTRUM_PACKET,
        THRESHOLD_MAP_PACKET,
        ALPHA_TARGET,
        ALPHA_PACKET,
        ALPHA0_NO_GO,
        QED_LOOP_NO_GO,
        PHYSICAL_ELECTRON_PACKET,
        PHYSICAL_ELECTRON_NO_GO,
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
        "R-Lep Thresholds Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify charged-lepton thresholds",
        "the charged-lepton threshold handoff consumed by the zero-import alpha0",
        "RL.1",
        "RL.2",
        "RL.3",
        "RL.4",
        "RL.5",
        "RL.6",
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
        "No proper subset of those eleven contract inputs",
        "R_LEP_THRESHOLDS_RETAINED",
        "T_LEP_THRESHOLD_MOMENT_RETAINED",
        "QED_LOOP_KERNEL_RETAINED",
        "R_Q_HEAVY_THRESHOLDS_RETAINED",
        "R_HAD_NP_RETAINED",
        "SCHEME_DECOUPLING_MATCHING_RETAINED",
        "sum_l N_c(l) Q_l^2 = 3",
        "b_lep = (4/3) * 3 = 4",
        "T_lep(M_Z; m_e,m_mu,m_tau)",
        "log(M_Z^3 / (m_e m_mu m_tau))",
        "Open PRs were refreshed on 2026-07-05 UTC",
        "clean/green status is not a prerequisite",
        "`#5033` reflection-positivity runner-scope cleanup | open",
        "`#5030` finite multisite Pauli carrier provenance | open",
        "`#5021` primitive-retirement review | open draft",
        "`#5018` domain-wall edge content vs SM chiral map | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#4991` owner-governed Tier-A retirement | open",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "decision-ready ratification",
        "narrowed R-Lep ratification decision packet passes",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(R_LEP_INPUTS)
    audit.check("full R-Lep contract accepts handoff", closes_r_lep(full_inputs))
    for missing in sorted(R_LEP_INPUTS):
        reduced = set(R_LEP_INPUTS)
        reduced.remove(missing)
        audit.check(f"R-Lep handoff fails without {missing}", not closes_r_lep(reduced))
    accepted_subsets = [subset for subset in all_subsets(R_LEP_INPUTS) if closes_r_lep(subset)]
    audit.check("only full R-Lep subset closes handoff", accepted_subsets == [full_inputs])

    audit.check("mass-spectrum consequence alone does not close R-Lep", not closes_r_lep(SPECTRUM_CONSEQUENCE))
    audit.check("threshold-map consequence alone does not close R-Lep", not closes_r_lep(MAP_CONSEQUENCE))
    audit.check(
        "mass-spectrum plus map still needs high-scale and governance gates",
        not closes_r_lep(SPECTRUM_CONSEQUENCE | MAP_CONSEQUENCE),
    )
    audit.check("R-Lep consequence alone does not close alpha0", not closes_alpha0(R_LEP_CONSEQUENCE))
    audit.check("full alpha0 predicate closes with all inputs", closes_alpha0(set(ALPHA0_INPUTS)))
    audit.check(
        "alpha0 consequence alone does not close static-source hydrogen",
        not closes_static_source({"RETAINED_ALPHA0_LOW_ENERGY_COULOMB"}),
    )

    section("Finite charged-lepton threshold arithmetic")
    weights = lepton_weights()
    total_weight = sum(weights, Fraction(0, 1))
    b_lep = Fraction(4, 3) * total_weight
    audit.check("three charged-lepton weights are all 1", weights == [Fraction(1, 1)] * 3)
    audit.check("charged-lepton weight sum is 3", total_weight == Fraction(3, 1))
    audit.check("charged-lepton b coefficient is 4", b_lep == Fraction(4, 1))

    m_z = 100.0
    masses_a = [1.0, 2.0, 5.0]
    masses_b = [1.0, 2.0, 10.0]
    moment_a = t_lep(m_z, masses_a)
    moment_b = t_lep(m_z, masses_b)
    audit.check("threshold moment equals log product form", abs(moment_a - math.log(m_z**3 / math.prod(masses_a))) < 1e-12)
    audit.check("moving one mass changes threshold moment", abs((moment_b - moment_a) + math.log(2.0)) < 1e-12)
    audit.check("permuting equal-weight lepton masses leaves one-loop moment", abs(t_lep(m_z, masses_a) - t_lep(m_z, list(reversed(masses_a)))) < 1e-12)
    scale = 11.0
    audit.check("common unit rescale leaves threshold moment", abs(t_lep(scale * m_z, [scale * m for m in masses_a]) - moment_a) < 1e-12)
    common_log = 5.0
    common_moment = 3.0 * common_log
    via_moment = (2.0 / (3.0 * math.pi)) * common_moment
    via_b = float(b_lep) * common_log / (2.0 * math.pi)
    audit.check("lepton moment formula matches b_lep common-threshold running", abs(via_moment - via_b) < 1e-12)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    r_lep_no_go = read(R_LEP_NO_GO)
    mass_spectrum = read(MASS_SPECTRUM_PACKET)
    threshold_map = read(THRESHOLD_MAP_PACKET)
    alpha_target = read(ALPHA_TARGET)
    alpha_packet = read(ALPHA_PACKET)
    alpha0_no_go = read(ALPHA0_NO_GO)
    qed_loop_no_go = read(QED_LOOP_NO_GO)
    physical_electron = read(PHYSICAL_ELECTRON_PACKET)
    physical_electron_no_go = read(PHYSICAL_ELECTRON_NO_GO)
    lane2_firewall = read(LANE2_FIREWALL)
    threshold_runner = read(THRESHOLD_MOMENT)
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    minimal = read(MINIMAL)
    scale_note = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("R-Lep current-surface no-go", r_lep_no_go),
        ("alpha target", alpha_target),
        ("alpha0 packet", alpha_packet),
        ("alpha0 current-surface no-go", alpha0_no_go),
    ]:
        audit.check(f"{container_name} references R-Lep decision packet", NOTE.name in container)

    audit.check("R-Lep no-go names same eleven-input contract", all(token in r_lep_no_go for token in R_LEP_INPUTS))
    audit.check(
        "mass-spectrum packet supplies conditional R-Lep mass inputs",
        "PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED" in mass_spectrum
        and "PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED" in mass_spectrum,
    )
    audit.check(
        "threshold-map packet supplies conditional R-Lep map input",
        "LEPTON_THRESHOLD_MOMENT_MAP_RETAINED" in threshold_map
        and "does not ratify R-Lep thresholds" in threshold_map,
    )
    audit.check("alpha0 packet consumes R-Lep", "R_LEP_THRESHOLDS_RETAINED" in alpha_packet)
    audit.check("alpha target names other alpha blockers", all(token in alpha_target for token in [
        "QED_LOOP_KERNEL_RETAINED",
        "R_Q_HEAVY_THRESHOLDS_RETAINED",
        "R_HAD_NP_RETAINED",
        "SCHEME_DECOUPLING_MATCHING_RETAINED",
    ]))
    audit.check("alpha0 no-go keeps low-energy alpha open", "RETAINED_ALPHA0_LOW_ENERGY_COULOMB" in alpha0_no_go)
    audit.check("QED loop no-go keeps kernel separate", "QED_LOOP_KERNEL_RETAINED" in qed_loop_no_go)
    audit.check("physical electron packet is selected-electron specific", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in physical_electron)
    audit.check("physical electron no-go is not full mass spectrum", "PHYSICAL_ELECTRON_READOUT_RETAINED" in physical_electron_no_go)
    audit.check("Lane 2 firewall names R-Lep as split component", "R-Lep" in lane2_firewall and "R-Q-Heavy" in lane2_firewall and "R-Had-NP" in lane2_firewall)
    audit.check("threshold runner remains target/no-go arithmetic", "threshold" in threshold_runner.lower() and "T_EM" in threshold_runner)

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    for absent in [
        "r_lep_thresholds_primitive",
        "lepton_threshold_moment_primitive",
        "charged_lepton_mass_spectrum_primitive",
        "charged_lepton_threshold_primitive",
        "alpha0_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered R-Lep shortcut: {absent}", absent not in registry_text)
    audit.check("minimal axioms require downstream physical structure", "Further physical\nstructure requires derivation" in minimal)
    audit.check("scale primitive excludes dimensionless masses", "zero dimensionless content" in scale_note and "mass ratio" in scale_note)
    audit.check("kinetic primitive excludes couplings/masses", "mass ratio" in kinetic and "coupling" in kinetic)
    audit.check("realized primitive excludes state-selected values", "state-selection rule" in realized and "or value is supplied" in realized)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5033` reflection-positivity runner-scope cleanup | open",
        "`#5030` finite multisite Pauli carrier provenance | open",
        "`#5021` primitive-retirement review | open draft",
        "`#5018` domain-wall edge content vs SM chiral map | open",
        "`#5017` domain-wall anomaly inflow spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` chirality domain-wall free-field note | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#4991` owner-governed Tier-A retirement | open",
    ]
    for marker in latest_pr_markers:
        audit.check(f"open PR marker present: {marker}", flat(marker) in note_flat)
    audit.check("open PR check does not require clean status", "clean/green status is not a prerequisite" in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of `R_LEP_THRESHOLDS_RETAINED`.",
        "No derivation or ratification of `T_LEP_THRESHOLD_MOMENT_RETAINED`.",
        "No derivation or ratification of a physical charged-lepton mass triple.",
        "No derivation or ratification of `m_e`, `m_mu`, or `m_tau`.",
        "No derivation or ratification of the physical charged-lepton species labels.",
        "No derivation or ratification of `LEPTON_THRESHOLD_MOMENT_MAP_RETAINED`.",
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
        "This packet ratifies charged-lepton thresholds",
        "R_LEP_THRESHOLDS_RETAINED is supplied",
        "T_LEP_THRESHOLD_MOMENT_RETAINED is supplied",
        "ALPHA0_RETAINED is supplied",
        "retained hydrogen calculation is complete",
        "PDG masses are proof inputs",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
