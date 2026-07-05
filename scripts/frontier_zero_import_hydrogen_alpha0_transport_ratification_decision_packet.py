#!/usr/bin/env python3
"""Verifier for the zero-import alpha0 transport decision packet.

This runner checks that the Lane 2 alpha0 transport contract is explicit and
kept separate from electron-mass retention, the static-source NR Coulomb
limit, and final hydrogen closure.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ALPHA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
QED_LOOP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_LEP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_LEP_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
ALPHA0_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
LANE2_FIREWALL = ROOT / "docs" / "ATOMIC_LANE2_QED_RUNNING_DEPENDENCY_FIREWALL_NOTE_2026-04-30.md"
ALPHA0_BOUNDARY = ROOT / "docs" / "ATOMIC_LANE2_ALPHA0_RUNNING_BRIDGE_BOUNDARY_NOTE_2026-04-29.md"
RYDBERG_FIREWALL = ROOT / "docs" / "ATOMIC_RYDBERG_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md"
QED_THRESHOLD_FIREWALL = ROOT / "scripts" / "frontier_atomic_qed_threshold_bridge_firewall.py"
THRESHOLD_MOMENT = ROOT / "scripts" / "frontier_atomic_alpha0_threshold_moment_no_go.py"
USABLE_VALUES = ROOT / "docs" / "publication" / "ci3_z3" / "USABLE_DERIVED_VALUES_INDEX.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

INV_ALPHA_MZ_REPO = 127.67
INV_ALPHA0_COMPARATOR = 137.035999084
M_Z_GEV_COMPARATOR = 91.1876

ALPHA0_DECISION_INPUTS = {
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
    "ALPHA0_RETAINED",
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


def charged_species_weights() -> list[Fraction]:
    q_e = Fraction(-1, 1)
    q_u = Fraction(2, 3)
    q_d = Fraction(-1, 3)
    return [
        q_e * q_e,
        q_e * q_e,
        q_e * q_e,
        3 * q_u * q_u,
        3 * q_u * q_u,
        3 * q_u * q_u,
        3 * q_d * q_d,
        3 * q_d * q_d,
        3 * q_d * q_d,
    ]


def closes_alpha0_decision(inputs: set[str]) -> bool:
    return ALPHA0_DECISION_INPUTS <= inputs


def closes_static_source_hydrogen(inputs: set[str]) -> bool:
    return STATIC_SOURCE_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        ALPHA_TARGET,
        QED_LOOP_NO_GO,
        R_LEP_NO_GO,
        R_LEP_PACKET,
        ALPHA0_NO_GO,
        STATIC_TARGET,
        LANE2_FIREWALL,
        ALPHA0_BOUNDARY,
        RYDBERG_FIREWALL,
        QED_THRESHOLD_FIREWALL,
        THRESHOLD_MOMENT,
        USABLE_VALUES,
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
        "Alpha0 Transport Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify `alpha(0)`",
        "the zero-import alpha(0) transport package for the static-source hydrogen lane",
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
        "No proper subset of those eleven contract inputs",
        "ALPHA0_TRANSPORT_RETAINED",
        "ALPHA0_RETAINED",
        "STATIC_SOURCE_RYDBERG_RETAINED",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
        "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
        "ATOMIC_OPERATOR_HARNESS_VERIFIED",
        "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
        "alpha(0)^-1 = alpha_EM(M_Z)^-1 + (2/(3 pi)) * T_EM + Delta_match",
        "sum_f N_c(f) Q_f^2 = 8",
        "b_QED = (4/3) * 8 = 32/3",
        "T_EM_target = 44.136",
        "M_eff ~= M_Z * exp(-common log) ~= 0.37 GeV",
        "ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "QED loop target remains needed",
        "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "R-Lep threshold target remains needed",
        "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "T_LEP_THRESHOLD_MOMENT_RETAINED",
        "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "ALPHA0_TRANSPORT_RETAINED",
        "ALPHA0_RETAINED",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
        "QED loop kernel, charged-lepton thresholds",
        "`#5013` theta native positive-class adjudication | `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `SUCCESS`",
        "`#5011` eta twisted walk family runner | `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `SUCCESS`",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "the Lane 2 alpha0 transport package is packaged as a decision-ready",
        "broad no-go fails; narrowed alpha0 transport decision packet passes",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(ALPHA0_DECISION_INPUTS)
    audit.check("full alpha0 contract accepts decision", closes_alpha0_decision(full_inputs))
    for missing in sorted(ALPHA0_DECISION_INPUTS):
        reduced = set(ALPHA0_DECISION_INPUTS)
        reduced.remove(missing)
        audit.check(f"alpha0 decision fails without {missing}", not closes_alpha0_decision(reduced))
    accepted_subsets = [subset for subset in all_subsets(ALPHA0_DECISION_INPUTS) if closes_alpha0_decision(subset)]
    audit.check("only full tested contract subset closes alpha0 decision", accepted_subsets == [full_inputs])

    alpha_consequence = {"ALPHA0_RETAINED"}
    audit.check("alpha0 alone does not close static-source hydrogen", not closes_static_source_hydrogen(alpha_consequence))
    audit.check("full static-source predicate closes model hydrogen target", closes_static_source_hydrogen(set(STATIC_SOURCE_INPUTS)))
    for missing in sorted(STATIC_SOURCE_INPUTS):
        reduced = set(STATIC_SOURCE_INPUTS)
        reduced.remove(missing)
        audit.check(f"static-source predicate fails without {missing}", not closes_static_source_hydrogen(reduced))

    section("Finite alpha transport arithmetic")
    weights = charged_species_weights()
    total_weight = sum(weights, Fraction(0, 1))
    b_qed = Fraction(4, 3) * total_weight
    audit.check("charged species weight sum is 8", total_weight == Fraction(8, 1))
    audit.check("b_QED weight algebra gives 32/3", b_qed == Fraction(32, 3))

    delta_inv_alpha = INV_ALPHA0_COMPARATOR - INV_ALPHA_MZ_REPO
    target_moment = delta_inv_alpha * (3.0 * math.pi / 2.0)
    common_log = target_moment / float(total_weight)
    effective_threshold = M_Z_GEV_COMPARATOR / math.exp(common_log)
    reconstructed_alpha0_inv = INV_ALPHA_MZ_REPO + (2.0 / (3.0 * math.pi)) * target_moment
    audit.check("inverse-alpha gap is comparator-sized", 9.36 < delta_inv_alpha < 9.37, f"gap={delta_inv_alpha:.9f}")
    audit.check("target threshold moment is in expected band", 44.1 < target_moment < 44.2, f"T={target_moment:.6f}")
    audit.check("common-log equivalent is in expected band", 5.50 < common_log < 5.53, f"log={common_log:.6f}")
    audit.check("effective threshold lands near hadronic scale", 0.35 < effective_threshold < 0.38, f"M_eff={effective_threshold:.6f}")
    audit.check(
        "target moment reconstructs alpha(0) comparator by construction",
        abs(reconstructed_alpha0_inv - INV_ALPHA0_COMPARATOR) < 1e-12,
    )

    section("Authority boundary checks")
    goal = read(GOAL)
    alpha_target = read(ALPHA_TARGET)
    qed_loop_no_go = read(QED_LOOP_NO_GO)
    r_lep_no_go = read(R_LEP_NO_GO)
    r_lep_packet = read(R_LEP_PACKET)
    alpha0_no_go = read(ALPHA0_NO_GO)
    static_target = read(STATIC_TARGET)
    lane2_firewall = read(LANE2_FIREWALL)
    alpha0_boundary = read(ALPHA0_BOUNDARY)
    rydberg_firewall = read(RYDBERG_FIREWALL)
    qed_threshold = read(QED_THRESHOLD_FIREWALL)
    threshold_moment = read(THRESHOLD_MOMENT)
    usable_values = read(USABLE_VALUES)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("alpha target", alpha_target),
        ("static-source target", static_target),
    ]:
        audit.check(f"{container_name} references alpha0 decision packet", NOTE.name in container)
    audit.check(
        "alpha0 no-go keeps transport open",
        "ALPHA0_TRANSPORT_RETAINED" in alpha0_no_go and "RETAINED_ALPHA0_LOW_ENERGY_COULOMB" in alpha0_no_go,
    )
    audit.check(
        "alpha0 packet references QED loop no-go",
        QED_LOOP_NO_GO.name in note and "QED loop target remains needed" in note,
    )
    audit.check(
        "alpha0 packet references R-Lep no-go",
        R_LEP_NO_GO.name in note and "R-Lep threshold target remains needed" in note,
    )
    audit.check(
        "alpha0 packet references R-Lep decision packet",
        R_LEP_PACKET.name in note and "T_LEP_THRESHOLD_MOMENT_RETAINED" in note,
    )
    audit.check(
        "QED loop no-go keeps kernel open",
        "QED_LOOP_KERNEL_RETAINED" in qed_loop_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in qed_loop_no_go,
    )
    audit.check(
        "R-Lep no-go keeps thresholds open",
        "R_LEP_THRESHOLDS_RETAINED" in r_lep_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in r_lep_no_go,
    )
    audit.check(
        "R-Lep packet keeps alpha0 downstream",
        "R_LEP_THRESHOLDS_RETAINED" in r_lep_packet
        and "does not by itself supply" in r_lep_packet,
    )

    audit.check("alpha target names same transport inputs", all(token in alpha_target for token in [
        "QED_LOOP_KERNEL_RETAINED",
        "R_LEP_THRESHOLDS_RETAINED",
        "R_Q_HEAVY_THRESHOLDS_RETAINED",
        "R_HAD_NP_RETAINED",
        "SCHEME_DECOUPLING_MATCHING_RETAINED",
    ]))
    audit.check("Lane 2 firewall names R-Lep/R-Q-Heavy/R-Had-NP", all(token in lane2_firewall for token in ["R-Lep", "R-Q-Heavy", "R-Had-NP"]))
    alpha0_boundary_flat = flat(alpha0_boundary)
    audit.check(
        "alpha0 boundary keeps high-scale shortcut open/blocked",
        "alpha_EM(M_Z)" in alpha0_boundary_flat and "alone does not determine" in alpha0_boundary_flat,
    )
    audit.check("Rydberg firewall names alpha0 transport as load-bearing", "alpha(0)" in rydberg_firewall and "alpha_EM(M_Z)" in rydberg_firewall)
    audit.check("QED threshold firewall is threshold-placement support", "threshold" in qed_threshold.lower() and "b_QED" in qed_threshold)
    audit.check("threshold-moment runner keeps comparator role", "T_EM" in threshold_moment or "threshold moment" in threshold_moment.lower())
    audit.check("usable values contain retained alpha_EM(M_Z)", "alpha_EM(M_Z)" in usable_values and "127.67" in usable_values)
    audit.check("usable values do not list alpha0 as retained", "alpha(0)" not in usable_values and "ALPHA0" not in usable_values)
    audit.check("static target keeps alpha0 downstream", "RETAINED_ALPHA0_LOW_ENERGY_COULOMB" in static_target)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    audit.check("minimal axioms exclude downstream observable bridges", "remain outside axiom content" in minimal and "source/action" in minimal)
    audit.check("scale primitive excludes dimensionless physics", "zero dimensionless content" in scale and "coupling" in scale)
    audit.check("kinetic primitive excludes dynamics/couplings", "dynamics" in kinetic and "coupling" in kinetic)
    audit.check("realized primitive excludes state-selection and values", "state-selection rule" in realized and "or value is supplied" in realized)
    for absent in [
        "qed_loop_kernel_primitive",
        "r_lep_thresholds_primitive",
        "alpha0_primitive",
        "r_had_np_primitive",
        "scheme_decoupling_matching_primitive",
    ]:
        audit.check(f"no registered alpha shortcut: {absent}", absent not in registry_text)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5013` theta native positive-class adjudication | `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `SUCCESS`",
        "`#5011` eta twisted walk family runner | `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of `alpha(0)`.",
        "No derivation or ratification of the QED loop kernel.",
        "No derivation or ratification of `T_EM` or `Delta_match`.",
        "No derivation or ratification of charged-lepton, heavy-quark, or hadronic",
        "No derivation or ratification of hadronic `R(s)`.",
        "No derivation or ratification of the scheme/decoupling convention.",
        "No derivation of `m_e`.",
        "No derivation of the static-source nonrelativistic Coulomb limit.",
        "No retained hydrogen calculation.",
        "No use of observed `alpha(0)`, Rydberg, PDG masses, fitted thresholds, or",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies `alpha(0)`",
        "alpha(0) is retained",
        "QED loop kernel is retained",
        "T_EM is derived",
        "hadronic R(s) is derived",
        "m_e is derived",
        "retained hydrogen calculation is complete",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
