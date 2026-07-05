#!/usr/bin/env python3
"""Verifier for the zero-import hydrogen Koide/electron-readout firewall.

This is a support runner. It verifies the phase-blind Koide arithmetic and
the hydrogen-facing electron-readout dependency boundary. It does not derive a
charged-lepton mass or hydrogen spectroscopy.
"""

from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"

M_W = 80369.2


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


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def brannen_root_ratio(k: int, delta: float) -> float:
    return 1.0 + math.sqrt(2.0) * math.cos(delta + 2.0 * math.pi * k / 3.0)


def root_ratios(delta: float) -> list[float]:
    return [brannen_root_ratio(k, delta) for k in range(3)]


def koide_q(delta: float) -> float:
    xs = root_ratios(delta)
    return sum(x * x for x in xs) / (sum(xs) ** 2)


def electron_factor(delta: float) -> float:
    return min(x * x for x in root_ratios(delta))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("Koide electron-readout firewall note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_PR5007_IMPACT_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_TARGET_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_W4C_PR5028_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_TIER_A_OWNER_RETIREMENT_PR4991_IMPACT_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_AC_R_ETA_UPSTREAM_CLUSTER_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_K1_DETERMINANT_COUNT_LADDER_REVIEW_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_ROUTE_FORK_REVIEW_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_CARRIER_REALIZATION_CHAIN_REVIEW_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_STATE_ACTION_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_STATE_ACTION_SELECTOR_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_STATE_ACTION_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_ROTATION_ACTION_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_ROTATION_ACTION_SELECTOR_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_ROTATION_ACTION_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_SELECTOR_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_STATE_LAW_TWO_INPUT_REVIEW_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SIGMA_P_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_LADDER_REVIEW_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "docs/LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md",
        "docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md",
        "docs/SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md",
        "docs/LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md",
        "docs/CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md",
        "docs/CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md",
        "docs/LEPTON_MASS_SCALE_MW_OVER_256_EMPIRICAL_OPEN_GATE_NOTE_2026-05-26.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/audit/data/tier_a_admissions.json",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Required note content")
    required_phrases = [
        "E_H = m_e alpha(0)^2",
        "m_e = a_l^2 * rho_e(delta)",
        "rho_e(delta) = min_k [1 + sqrt(2) cos(delta + 2 pi k / 3)]^2",
        "Q=2/3` is a shape-surface condition, not yet an electron eigenvalue",
        "K1 | Counting-measure bit",
        "K2 | Radian/readout identification",
        "K3 | Species/electron branch",
        "K4 | Absolute scale",
        "AC_phi_lambda",
        "Open PR Alignment",
        "#5011",
        "#5020",
        "#5022",
        "#5019",
        "#5009",
        "#5010",
        "#5008",
        "#5007",
        "#5006",
        "#4991",
        "#5027",
        "#5028",
        "#5029",
        "Koide custody AC gate-edge repair",
        "W4c labeling/species repairs",
        "Koide substep4 labeling no-go runner strengthening",
        "labeling/species dependency-surface readiness",
        "89768b461c",
        "e2d1dec095",
        "occurrence-axiom and measure-binary shortcuts",
        "ZERO_IMPORT_HYDROGEN_KOIDE_W4C_PR5028_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_AC_R_ETA_UPSTREAM_CLUSTER_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "S3 spacetime tensor primitive runner repair",
        "YT P1 I_s re-audit packet bridge repair",
        "eta twisted walk family runner repair",
        "Koide native zero-section route-guard repair",
        "Koide R-eta value-face registered-angle/exactness relocation",
        "value-face standing",
        "exactness residual",
        "readout-identification premise",
        "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "K1_COUNTING_MEASURE_RETAINED",
        "block-vs-dimension fork",
        "orbit/holomorphic count selector",
        "not K1 closure",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, merged-PR, and open-PR surfaces do",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ten-input owner/audit contract",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED",
        "selector theorem and dimension/Born default-exclusion inputs",
        "does not close K1",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "selector lane reviewable",
        "not supply `K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`",
        "ZERO_IMPORT_HYDROGEN_KOIDE_K1_DETERMINANT_COUNT_LADDER_REVIEW_PACKET_2026-07-05.md",
        "K1 determinant-count ladder review packet",
        "review compression only",
        "sibling inputs, not a single chain",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_ROUTE_FORK_REVIEW_PACKET_2026-07-05.md",
        "route-fork review packet",
        "bundles the parent state-law bridge route alternatives",
        "the parent bridge needs either route theorem, not both",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_CARRIER_REALIZATION_CHAIN_REVIEW_PACKET_2026-07-05.md",
        "carrier-realization chain review packet",
        "downstream sequential carrier chain",
        "support-only inputs",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED",
        "elementary route owner/audit contract",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED",
        "field-index spin-lift privilege owner/audit contract",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_RETAINED",
        "privileging the faithful Pauli",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
        "action-law owner/audit contract",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_STATE_ACTION_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_STATE_ACTION_SELECTOR_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_STATE_ACTION_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "FAITHFUL_KS_STATE_ACTION_SELECTOR_RETAINED",
        "selector owner/audit contract",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "KS_RECONSTRUCTED_MATTER_MODE_ACTION_DOMAIN_RETAINED",
        "action-domain owner/audit contract",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_ROTATION_ACTION_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_ROTATION_ACTION_SELECTOR_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_ROTATION_ACTION_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "PHYSICAL_ROTATION_ACTION_SELECTOR_RETAINED",
        "physical action-selector owner/audit contract",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_SELECTOR_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md",
        "groups the action-domain owner/audit contract and physical action-selector",
        "review compression only",
        "does not ratify",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "subinput under the KS child route",
        "KS physical spin-lift action law",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_STATE_LAW_TWO_INPUT_REVIEW_PACKET_2026-07-05.md",
        "groups the scalar-lift-exclusion owner/audit contract and KS spin-lift",
        "review compression only",
        "does not ratify",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED",
        "subinput under the scalar-lift exclusion lane",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED",
        "finite covariance-failure",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED",
        "Pauli-vector and Kawamoto-Smit support stack",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED",
        "narrower child subinput under the spinful sigma-dot-p KS-route kernel lane",
        "P-FLUX and Kawamoto-Smit support stack",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SIGMA_P_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md",
        "groups the route momentum/link-phase input and the spinful kernel-object",
        "review compression only",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED",
        "h-class plus h-unit",
        "not retained derivation or electron readout",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, merged-PR, and open-PR surfaces do",
        "eleven-input owner/audit contract",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED",
        "identity-radian conversion coefficient",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "h-unit identity-radian ratification decision packet",
        "c = 1",
        "Phi = 2/3",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md",
        "R_ETA_H_CLASS_RETAINED",
        "fixed-point readout bridge",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "h-class fixed-locus ratification decision packet",
        "thirteen-input owner/audit contract",
        "physical carrier realization",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_LADDER_REVIEW_PACKET_2026-07-05.md",
        "R-eta readout ladder review packet",
        "review compression only",
        "sibling inputs, not a single chain",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "K2_R_ETA_EXACTNESS_RETAINED",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED",
        "current retained, primitive, and open-PR surfaces do not",
        "ten-input owner/audit contract",
        "nine-input owner/audit contract",
        "retained exact `2/9` theorem",
        "fold/branch domain-lock inputs",
        "registered Phi",
        "No claim that PR `#5020` or merged PR `#5022` derives or ratifies a Koide",
        "KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_TARGET_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "BRIDGE_TEXT_LOCK",
        "ZERO_SOURCE_READOUT_RETAINED",
        "REAL_PRIMITIVE_BRANNEN_ENDPOINT_RETAINED",
        "BASED_DETERMINANT_LINE_READOUT_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "native bridge target remains needed",
        "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "Koide branch mass-map ratification decision packet",
        "KOIDE_BRANCH_MASS_MAP_TEXT_LOCK",
        "BRANNEN_CIRCULANT_BRANCH_FORM_RETAINED",
        "SQUARE_ROOT_MASS_READOUT_RETAINED",
        "POSITIVE_CHAMBER_OR_SIGN_RULE_RETAINED",
        "SCALE_PARAMETER_COMPOSITION_RETAINED",
        "PHASE_SCALE_SPECIES_SCOPE_LOCK",
        "PHYSICAL_ELECTRON_READOUT_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current Koide algebra, primitive, and open-PR surfaces do not",
        "SQUARE_ROOT_MASS_READOUT_RETAINED",
        "POSITIVE_CHAMBER_OR_SIGN_RULE_RETAINED",
        "SCALE_PARAMETER_COMPOSITION_RETAINED",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "PHYSICAL_ELECTRON_MASS_TEXT_LOCK",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "species bridge target remains needed",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "K4 scale target remains needed",
        "KOIDE_BRANCH_MASS_MAP_RETAINED",
        "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
        "NO_LEPTON_COMPARATOR_PROOF_INPUT",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "PHYSICAL_ELECTRON_READOUT_RETAINED",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "Z1 zero-source readout",
        "Z2 real-primitive Brannen endpoint",
        "Z3 based determinant-line readout",
        "Tier-A owner-retirement `#4991` impact discriminator",
        "ZERO_IMPORT_HYDROGEN_TIER_A_OWNER_RETIREMENT_PR4991_IMPACT_DISCRIMINATOR_2026-07-04.md",
        "owner-governed chain-satisfying premise language",
        "not theorem closure, not an axiom, not an approved primitive",
        "zero-source readout",
        "real-primitive Brannen endpoint",
        "based determinant-line readout",
        "not a retained electron readout",
        "#4897",
        "#4906",
        "#4928",
        "#4929",
        "#4930",
        "#4931",
        "#4932",
        "species-bridge partial-retirement",
        "occurrence-axiom shortcut",
        "measure-side binary",
        "generator-channel Hilbert-Schmidt",
        "dimension/per-mode",
        "R-eta",
        "Phi = S_sum = 2/3",
        "angle-native",
        "event-law",
        "activation/rate normalization",
        "measure-side/dynamical occupancy realization",
        "R-eta",
        "does not derive full electron readout",
        "realized-state registered data",
        "does not derive or force `r = 1/2`",
        "Koide native zero-section `#5007` route guard",
        "Tier-A owner-retirement `#4991` route",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed electron-readout firewall passes",
    ]
    for phrase in required_phrases:
        audit.check(f"required note phrase present: {phrase}", phrase in note)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Phase-blind Koide arithmetic")
    expected_delta = 2.0 / 9.0
    expected_sorted = [
        0.04034990821920668,
        0.5802119201475365,
        2.3794381716332564,
    ]
    sorted_delta = sorted(root_ratios(expected_delta))
    for got, expected, label in zip(sorted_delta, expected_sorted, ["electron-like", "muon-like", "tau-like"]):
        audit.check(
            f"delta=2/9 sorted {label} root ratio matches comparator",
            abs(got - expected) < 1e-14,
            f"{got:.15f}",
        )

    for delta in [expected_delta, 0.0, 0.5, 1.0, 3.0 * math.pi / 4.0]:
        audit.check(
            f"Koide Q remains 2/3 at delta={delta:.6f}",
            abs(koide_q(delta) - 2.0 / 3.0) < 1e-14,
            f"Q={koide_q(delta):.15f}",
        )

    rho_delta = electron_factor(expected_delta)
    rho_zero = electron_factor(0.0)
    rho_zero_branch = electron_factor(3.0 * math.pi / 4.0)
    audit.check(
        "delta=2/9 electron factor is the sharp comparator value",
        abs(rho_delta - expected_sorted[0] ** 2) < 1e-16 and 0.0016 < rho_delta < 0.0017,
        f"rho={rho_delta:.15f}",
    )
    audit.check(
        "delta=0 has same Q but much larger electron-like factor",
        rho_zero > 0.08,
        f"rho={rho_zero:.15f}",
    )
    audit.check(
        "delta=0 electron-like factor is more than 50x delta=2/9",
        rho_zero / rho_delta > 50.0,
        f"ratio={rho_zero / rho_delta:.2f}",
    )
    audit.check(
        "delta=3*pi/4 can make one branch zero while preserving Q",
        rho_zero_branch < 1e-28,
        f"rho={rho_zero_branch:.3e}",
    )

    a2_open = M_W / 256.0
    me_open = a2_open * rho_delta
    me_zero_delta = a2_open * rho_zero
    audit.check(
        "open comparator scale with delta=2/9 gives electron-scale comparator",
        0.510 < me_open < 0.512,
        f"m={me_open:.6f} MeV",
    )
    audit.check(
        "same open scale with delta=0 gives non-electron mass scale",
        me_zero_delta > 25.0,
        f"m={me_zero_delta:.6f} MeV",
    )

    section("Registry boundary")
    primitive_registry = read(PRIMITIVE_REGISTRY)
    tier_a_registry = read(TIER_A_REGISTRY)
    audit.check("AC_phi_lambda is present in Tier-A registry", "AC_phi_lambda" in tier_a_registry)
    audit.check("AC_phi_lambda is not a primitive registry node", "AC_phi_lambda" not in primitive_registry)
    for primitive in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive registry names {primitive}", primitive in primitive_registry)
    audit.check("primitive registry distinguishes Tier-A admissions", "Tier-A derivation-target admissions live in tier_a_admissions.json" in primitive_registry)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `m_e`.",
        "No derivation of `Q=2/3` from the current retained inventory alone.",
        "No derivation of `delta = 2/9`.",
        "No zero-import determination of `rho_e(delta)`.",
        "No derivation of the physical electron species bridge.",
        "No derivation of `a_l^2`, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `m_e`",
        "hydrogen is retained",
        "Q=2/3 is derived zero-import",
        "delta = 2/9 is derived",
        "rho_e(delta) is derived",
        "electron species bridge is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
