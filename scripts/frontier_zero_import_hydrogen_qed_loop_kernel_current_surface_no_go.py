#!/usr/bin/env python3
"""Verifier for the QED loop-kernel current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply the QED loop-kernel handoff consumed by Lane 2 alpha0
transport. It preserves the positive retained-kernel route and does not derive
alpha(0), m_e, Rydberg, or hydrogen.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ALPHA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
ALPHA_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ALPHA0_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
LANE2_FIREWALL = ROOT / "docs" / "ATOMIC_LANE2_QED_RUNNING_DEPENDENCY_FIREWALL_NOTE_2026-04-30.md"
ALPHA0_BOUNDARY = ROOT / "docs" / "ATOMIC_LANE2_ALPHA0_RUNNING_BRIDGE_BOUNDARY_NOTE_2026-04-29.md"
QED_THRESHOLD_FIREWALL = ROOT / "scripts" / "frontier_atomic_qed_threshold_bridge_firewall.py"
THRESHOLD_MOMENT = ROOT / "scripts" / "frontier_atomic_alpha0_threshold_moment_no_go.py"
BETA_NOTE = ROOT / "docs" / "SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md"
USABLE_VALUES = ROOT / "docs" / "publication" / "ci3_z3" / "USABLE_DERIVED_VALUES_INDEX.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


QED_KERNEL_INPUTS = {
    "QED_LOOP_KERNEL_TEXT_LOCK",
    "FRAMEWORK_QED_PROPAGATOR_SURFACE_RETAINED",
    "VACUUM_POLARIZATION_INTEGRAND_RETAINED",
    "CHARGE_INSERTION_RULE_RETAINED",
    "RENORMALIZATION_SUBTRACTION_RETAINED",
    "WARD_IDENTITY_OR_CHARGE_CONSERVATION_RETAINED",
    "THRESHOLD_DECOUPLING_INTERFACE_LOCK",
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


def closes_qed_kernel(inputs: set[str]) -> bool:
    return QED_KERNEL_INPUTS <= inputs


def closes_alpha0(inputs: set[str]) -> bool:
    return ALPHA0_INPUTS <= inputs


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


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        ALPHA_TARGET,
        ALPHA_PACKET,
        ALPHA0_NO_GO,
        STATIC_TARGET,
        LANE2_FIREWALL,
        ALPHA0_BOUNDARY,
        QED_THRESHOLD_FIREWALL,
        THRESHOLD_MOMENT,
        BETA_NOTE,
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
        "QED Loop-Kernel Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not ratify the QED loop kernel",
        "QED_LOOP_KERNEL_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "QED_LOOP_KERNEL_TEXT_LOCK",
        "FRAMEWORK_QED_PROPAGATOR_SURFACE_RETAINED",
        "VACUUM_POLARIZATION_INTEGRAND_RETAINED",
        "CHARGE_INSERTION_RULE_RETAINED",
        "RENORMALIZATION_SUBTRACTION_RETAINED",
        "WARD_IDENTITY_OR_CHARGE_CONSERVATION_RETAINED",
        "THRESHOLD_DECOUPLING_INTERFACE_LOCK",
        "NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "alpha(0)^-1 = alpha_EM(M_Z)^-1 + (2/(3 pi)) * T_EM + Delta_match",
        "sum_f N_c(f) Q_f^2 = 8",
        "b_QED = (4/3) * 8 = 32/3",
        "qed_loop_kernel_primitive",
        "vacuum_polarization_primitive",
        "charge_insertion_primitive",
        "renormalization_subtraction_primitive",
        "ward_identity_primitive",
        "alpha0_primitive",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
        "QED loop target remains needed",
        "No-Go Discipline Gate",
        "broad QED loop-kernel no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("QED loop-kernel predicate checks")
    full_inputs = set(QED_KERNEL_INPUTS)
    audit.check("full QED kernel contract accepts retained handoff", closes_qed_kernel(full_inputs))
    for missing in sorted(QED_KERNEL_INPUTS):
        reduced = set(QED_KERNEL_INPUTS)
        reduced.remove(missing)
        audit.check(f"QED kernel handoff fails without {missing}", not closes_qed_kernel(reduced))
    accepted_subsets = [subset for subset in all_subsets(QED_KERNEL_INPUTS) if closes_qed_kernel(subset)]
    audit.check("only full QED kernel subset closes handoff", accepted_subsets == [full_inputs])
    current_surface = {
        "QED_LOOP_KERNEL_TEXT_LOCK",
        "NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
    }
    audit.check("current surface without kernel content does not close QED kernel", not closes_qed_kernel(current_surface))
    audit.check(
        "retained QED kernel alone does not close alpha0",
        not closes_alpha0({"QED_LOOP_KERNEL_RETAINED"}),
    )
    audit.check("full alpha0 predicate still needs more than QED kernel", closes_alpha0(set(ALPHA0_INPUTS)))

    section("Finite QED support arithmetic")
    weights = charged_species_weights()
    total_weight = sum(weights, Fraction(0, 1))
    b_qed = Fraction(4, 3) * total_weight
    audit.check("charged species weight sum is 8", total_weight == Fraction(8, 1))
    audit.check("b_QED weight algebra gives 32/3", b_qed == Fraction(32, 3))
    audit.check("leptonic weight is 3", sum(weights[:3], Fraction(0, 1)) == Fraction(3, 1))
    audit.check("up-type quark weight is 4", sum(weights[3:6], Fraction(0, 1)) == Fraction(4, 1))
    audit.check("down-type quark weight is 1", sum(weights[6:], Fraction(0, 1)) == Fraction(1, 1))
    audit.check(
        "Feynman-parameter kernel shape has positive midpoint",
        Fraction(1, 2) * (1 - Fraction(1, 2)) == Fraction(1, 4),
    )
    audit.check(
        "Feynman-parameter kernel integral is 1/6",
        sum(Fraction(1, n + 2) - Fraction(1, n + 3) for n in [0]) == Fraction(1, 6),
    )

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    alpha_target = read(ALPHA_TARGET)
    alpha_packet = read(ALPHA_PACKET)
    alpha0_no_go = read(ALPHA0_NO_GO)
    static_target = read(STATIC_TARGET)
    lane2_firewall = read(LANE2_FIREWALL)
    alpha0_boundary = flat(read(ALPHA0_BOUNDARY))
    qed_threshold = read(QED_THRESHOLD_FIREWALL)
    threshold_moment = read(THRESHOLD_MOMENT)
    beta_note = read(BETA_NOTE)
    usable_values = read(USABLE_VALUES)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    nodes = registry["nodes"]

    audit.check("goal packet references QED loop no-go", NOTE.name in goal and "QED loop target remains needed" in goal)
    audit.check("alpha target references QED loop no-go", NOTE.name in alpha_target and "QED loop target remains needed" in alpha_target)
    audit.check("alpha packet references QED loop no-go", NOTE.name in alpha_packet and "QED loop target remains needed" in alpha_packet)
    audit.check("alpha0 no-go references QED loop no-go", NOTE.name in alpha0_no_go and "QED loop target remains needed" in alpha0_no_go)
    audit.check("static target keeps alpha0 downstream", "RETAINED_ALPHA0_LOW_ENERGY_COULOMB" in static_target)
    audit.check("Lane 2 firewall names QED loop primitive as open", "QED loop primitive itself" in lane2_firewall and "currently a textbook input" in lane2_firewall)
    audit.check("alpha0 boundary keeps high-scale shortcut blocked", "alpha_EM(M_Z)" in alpha0_boundary and "alone does not determine" in alpha0_boundary)
    audit.check("QED threshold firewall keeps threshold placement open", "threshold" in qed_threshold.lower() and "b_QED" in qed_threshold)
    audit.check("threshold-moment runner does not supply kernel", "threshold moment" in threshold_moment.lower() and "does not fix the logarithms" in threshold_moment)
    audit.check("beta note supplies coefficient only", "b_QED" in beta_note and "above all SM thresholds" in beta_note)
    audit.check("usable values contain retained alpha_EM(M_Z)", "alpha_EM(M_Z)" in usable_values and "127.67" in usable_values)
    audit.check("usable values do not list alpha0 as retained", "alpha(0)" not in usable_values and "ALPHA0" not in usable_values)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    audit.check("minimal axioms exclude source/action and dynamics", "source/action" in minimal and "dynamics" in minimal)
    audit.check("scale primitive excludes couplings", "zero dimensionless content" in scale and "coupling" in scale)
    audit.check("kinetic primitive excludes couplings", "coupling" in kinetic and "dynamics" in kinetic)
    audit.check("realized primitive excludes values", "or value is supplied" in realized)
    for absent in [
        "qed_loop_kernel_primitive",
        "vacuum_polarization_primitive",
        "charge_insertion_primitive",
        "renormalization_subtraction_primitive",
        "ward_identity_primitive",
        "alpha0_primitive",
    ]:
        audit.check(f"no registered QED shortcut: {absent}", absent not in registry_text)

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
        "No derivation or ratification of `QED_LOOP_KERNEL_RETAINED`.",
        "No derivation or ratification of a framework QED propagator/action surface.",
        "No derivation or ratification of the vacuum-polarization integrand.",
        "No derivation or ratification of the charge insertion rule.",
        "No derivation or ratification of the renormalization subtraction rule.",
        "No derivation or ratification of the threshold-decoupling interface.",
        "No derivation or ratification of `ALPHA0_TRANSPORT_RETAINED`.",
        "No derivation or ratification of `ALPHA0_RETAINED`.",
        "No derivation or ratification of `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`.",
        "No derivation of threshold masses, hadronic `R(s)`, `T_EM`, or",
        "No derivation of `m_e`, static-source Rydberg, or full hydrogen.",
        "No use of observed `alpha(0)`, Rydberg, PDG masses, fitted thresholds, or",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `alpha(0)`",
        "This note ratifies the QED loop kernel",
        "QED_LOOP_KERNEL_RETAINED is supplied",
        "alpha0 transport is retained",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
