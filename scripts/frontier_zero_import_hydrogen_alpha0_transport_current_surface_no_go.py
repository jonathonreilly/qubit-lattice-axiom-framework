#!/usr/bin/env python3
"""Verifier for the alpha0 transport current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply the low-energy Coulomb coupling needed by the zero-import
hydrogen static-source Rydberg lane. It preserves the positive transport
contract and does not derive alpha(0), m_e, Rydberg, or hydrogen.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ALPHA_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ALPHA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
QED_LOOP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_LEP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
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


def closes_alpha0(inputs: set[str]) -> bool:
    return ALPHA0_INPUTS <= inputs


def closes_static_source_rydberg(inputs: set[str]) -> bool:
    return STATIC_SOURCE_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        ALPHA_PACKET,
        ALPHA_TARGET,
        QED_LOOP_NO_GO,
        R_LEP_NO_GO,
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
        "Alpha0 Transport Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not ratify `alpha(0)`",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
        "ALPHA0_TRANSPORT_RETAINED",
        "ALPHA0_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "ALPHA0_TRANSPORT_TEXT_LOCK",
        "ALPHA_MZ_RETAINED",
        "QED_LOOP_KERNEL_RETAINED",
        "ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "QED loop target remains needed",
        "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "R-Lep threshold target remains needed",
        "R_LEP_THRESHOLDS_RETAINED",
        "R_Q_HEAVY_THRESHOLDS_RETAINED",
        "R_HAD_NP_RETAINED",
        "SCHEME_DECOUPLING_MATCHING_RETAINED",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "alpha(0)^-1 = alpha_EM(M_Z)^-1 + (2/(3 pi)) * T_EM + Delta_match",
        "sum_f N_c(f) Q_f^2 = 8",
        "b_QED = (4/3) * 8 = 32/3",
        "T_EM_target = 44.139",
        "M_eff ~= M_Z * exp(-common log) ~= 0.37 GeV",
        "alpha0_primitive",
        "qed_loop_kernel_primitive",
        "r_lep_thresholds_primitive",
        "r_q_heavy_thresholds_primitive",
        "r_had_np_primitive",
        "scheme_decoupling_matching_primitive",
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
        "broad alpha0 no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Alpha0 transport predicate checks")
    full_inputs = set(ALPHA0_INPUTS)
    audit.check("full alpha0 contract accepts retained handoff", closes_alpha0(full_inputs))
    for missing in sorted(ALPHA0_INPUTS):
        reduced = set(ALPHA0_INPUTS)
        reduced.remove(missing)
        audit.check(f"alpha0 handoff fails without {missing}", not closes_alpha0(reduced))
    accepted_subsets = [subset for subset in all_subsets(ALPHA0_INPUTS) if closes_alpha0(subset)]
    audit.check("only full alpha0 subset closes handoff", accepted_subsets == [full_inputs])
    current_surface = {
        "ALPHA0_TRANSPORT_TEXT_LOCK",
        "ALPHA_MZ_RETAINED",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
    }
    audit.check(
        "current surface without loop/threshold/matching inputs does not close alpha0",
        not closes_alpha0(current_surface),
    )
    audit.check(
        "retained alpha0 alone does not close static-source Rydberg",
        not closes_static_source_rydberg({"RETAINED_ALPHA0_LOW_ENERGY_COULOMB"}),
    )
    audit.check(
        "full static-source predicate still needs more than alpha0",
        closes_static_source_rydberg(set(STATIC_SOURCE_INPUTS)),
    )

    section("Finite alpha target arithmetic checks")
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

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    alpha_packet = read(ALPHA_PACKET)
    alpha_target = read(ALPHA_TARGET)
    qed_loop_no_go = read(QED_LOOP_NO_GO)
    r_lep_no_go = read(R_LEP_NO_GO)
    static_target = read(STATIC_TARGET)
    lane2_firewall = read(LANE2_FIREWALL)
    alpha0_boundary = flat(read(ALPHA0_BOUNDARY))
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

    audit.check("goal packet references alpha0 no-go", NOTE.name in goal and "RETAINED_ALPHA0_LOW_ENERGY_COULOMB" in goal)
    audit.check("alpha packet references current-surface no-go", NOTE.name in alpha_packet and "current retained, primitive, and open-PR surfaces do not" in alpha_packet)
    audit.check("alpha target references current-surface no-go", NOTE.name in alpha_target and "ALPHA0_TRANSPORT_RETAINED" in alpha_target)
    audit.check("static target references alpha0 no-go", NOTE.name in static_target and "RETAINED_ALPHA0_LOW_ENERGY_COULOMB" in static_target)
    audit.check("alpha0 no-go references QED loop no-go", QED_LOOP_NO_GO.name in note and "QED loop target remains needed" in note)
    audit.check("alpha0 no-go references R-Lep no-go", R_LEP_NO_GO.name in note and "R-Lep threshold target remains needed" in note)
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
    audit.check("alpha target names same transport inputs", all(token in alpha_target for token in [
        "QED_LOOP_KERNEL_RETAINED",
        "R_LEP_THRESHOLDS_RETAINED",
        "R_Q_HEAVY_THRESHOLDS_RETAINED",
        "R_HAD_NP_RETAINED",
        "SCHEME_DECOUPLING_MATCHING_RETAINED",
    ]))
    audit.check("Lane 2 firewall names R-Lep/R-Q-Heavy/R-Had-NP", all(token in lane2_firewall for token in ["R-Lep", "R-Q-Heavy", "R-Had-NP"]))
    audit.check("alpha0 boundary keeps high-scale shortcut blocked", "alpha_EM(M_Z)" in alpha0_boundary and "alone does not determine" in alpha0_boundary)
    audit.check("Rydberg firewall names alpha0 transport as load-bearing", "alpha(0)" in rydberg_firewall and "alpha_EM(M_Z)" in rydberg_firewall)
    audit.check("QED threshold firewall keeps threshold placement open", "threshold" in qed_threshold.lower() and "b_QED" in qed_threshold)
    audit.check("threshold-moment runner keeps comparator role", "T_EM" in threshold_moment or "threshold moment" in threshold_moment.lower())
    audit.check("usable values contain retained alpha_EM(M_Z)", "alpha_EM(M_Z)" in usable_values and "127.67" in usable_values)
    audit.check("usable values do not list alpha0 as retained", "alpha(0)" not in usable_values and "ALPHA0" not in usable_values)
    audit.check("static target keeps alpha0 downstream", "RETAINED_ALPHA0_LOW_ENERGY_COULOMB" in static_target)

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    audit.check("minimal axioms exclude downstream observable bridges", "remain outside axiom content" in minimal and "source/action" in minimal)
    audit.check("scale primitive excludes dimensionless physics", "zero dimensionless content" in scale and "coupling" in scale)
    audit.check("kinetic primitive excludes dynamics/couplings", "dynamics" in kinetic and "coupling" in kinetic)
    audit.check("realized primitive excludes state-selection and values", "state-selection rule" in realized and "or value is supplied" in realized)
    for absent in [
        "alpha0_primitive",
        "qed_loop_kernel_primitive",
        "r_lep_thresholds_primitive",
        "r_q_heavy_thresholds_primitive",
        "r_had_np_primitive",
        "scheme_decoupling_matching_primitive",
    ]:
        audit.check(f"no registered alpha shortcut: {absent}", absent not in registry_text)

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
        audit.check(f"latest PR marker present: {marker}", marker in note)

    explicit_non_claims = [
        "No derivation or ratification of `ALPHA0_TRANSPORT_RETAINED`.",
        "No derivation or ratification of `ALPHA0_RETAINED`.",
        "No derivation or ratification of `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`.",
        "No derivation or ratification of the QED loop kernel.",
        "No derivation or ratification of `T_EM` or `Delta_match`.",
        "No derivation or ratification of charged-lepton, heavy-quark, or hadronic",
        "No derivation or ratification of hadronic `R(s)`.",
        "No derivation or ratification of the scheme/decoupling convention.",
        "No derivation of `m_e`, static-source Rydberg, or full hydrogen",
        "No use of observed `alpha(0)`, Rydberg, PDG masses, fitted thresholds, or",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `alpha(0)`",
        "This note ratifies `alpha(0)`",
        "ALPHA0_RETAINED is supplied",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB is supplied",
        "observed alpha(0) is used as proof",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
