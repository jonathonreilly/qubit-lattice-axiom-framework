#!/usr/bin/env python3
"""Verify the zero-import hydrogen alpha QED loop-kernel target discriminator."""

from __future__ import annotations

from fractions import Fraction
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
QED_LOOP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_LEP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
USABLE_VALUES = ROOT / "docs" / "publication" / "ci3_z3" / "USABLE_DERIVED_VALUES_INDEX.md"

INV_ALPHA_MZ_REPO = 127.67
INV_ALPHA0_COMPARATOR = 137.035999084
M_Z_GEV_COMPARATOR = 91.1876

ALPHA0_REQUIRED_INPUTS = {
    "ALPHA_MZ_RETAINED",
    "QED_LOOP_KERNEL_RETAINED",
    "R_LEP_THRESHOLDS_RETAINED",
    "R_Q_HEAVY_THRESHOLDS_RETAINED",
    "R_HAD_NP_RETAINED",
    "SCHEME_DECOUPLING_MATCHING_RETAINED",
    "NO_COMPARATOR_PROOF_INPUT",
}

HYDROGEN_EXTRA_INPUTS = {
    "RETAINED_ELECTRON_MASS",
    "RETAINED_PHYSICAL_UNIT_NR_LIMIT",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(condition: bool, label: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS {label}")
    else:
        print(f"FAIL {label}")
        failures.append(label)


def require_text(text: str, needle: str, failures: list[str]) -> None:
    text_compact = " ".join(text.split())
    needle_compact = " ".join(needle.split())
    require(
        needle in text or needle_compact in text_compact,
        f"note contains {needle!r}",
        failures,
    )


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
    return ALPHA0_REQUIRED_INPUTS <= inputs


def closes_zero_import_hydrogen(inputs: set[str]) -> bool:
    return closes_alpha0(inputs) and HYDROGEN_EXTRA_INPUTS <= inputs


def main() -> int:
    failures: list[str] = []
    note = read(NOTE)
    qed_loop_no_go = read(QED_LOOP_NO_GO)
    r_lep_no_go = read(R_LEP_NO_GO)
    primitive_registry_text = read(PRIMITIVE_REGISTRY)
    primitive_registry = json.loads(primitive_registry_text)
    usable_values = read(USABLE_VALUES)

    source_paths = [
        "docs/ATOMIC_RYDBERG_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md",
        "docs/ATOMIC_LANE2_QED_RUNNING_DEPENDENCY_FIREWALL_NOTE_2026-04-30.md",
        "scripts/frontier_atomic_qed_threshold_bridge_firewall.py",
        "scripts/frontier_atomic_alpha0_threshold_moment_no_go.py",
        "docs/ATOMIC_LANE2_ALPHA0_RUNNING_BRIDGE_BOUNDARY_NOTE_2026-04-29.md",
        "docs/SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md",
        "docs/ZERO_IMPORT_HYDROGEN_QED_LOOP_KERNEL_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX.md",
    ]
    for rel in source_paths:
        require((ROOT / rel).exists(), f"source path exists: {rel}", failures)

    required_phrases = [
        "Alpha QED Loop-Kernel Target Discriminator",
        "E_H = m_e alpha(0)^2",
        "ALPHA0_TRANSPORT_TARGET",
        "retained QED loop kernel",
        "retained threshold/matching moment",
        "R-Lep",
        "R-Q-Heavy",
        "R-Had-NP",
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
        "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "ALPHA0_TRANSPORT_RETAINED",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
        "support for the target, not as a current low-energy Coulomb",
        "sum_f N_c(f) Q_f^2 = 8",
        "b_QED = (4/3) * 8 = 32/3",
        "T_EM_target",
        "#5010",
        "CLEAN",
        "#5009",
        "CLEAN",
        "#5007",
        "#4991",
        "not alpha(0)",
        "No-Go Discipline Gate",
        "N1 - Alternative Route Enumeration",
        "N2 - Wall-Independence Audit",
        "N3 - Hidden-Wall Scan",
        "N4 - Residual Matching",
        "N5 - Rhetoric Audit",
        "N6 - Partial-Closure Path Scan",
        "N7 - Steelman",
        "N8 - Cross-Cycle Echo",
        "broad no-go fails; narrowed alpha target discriminator passes",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        require_text(note, phrase, failures)

    forbidden_overclaims = [
        "This note derives `alpha(0)`",
        "alpha(0) is retained",
        "retained hydrogen calculation is complete",
        "QED loop kernel is retained",
        "T_EM is derived",
        "hydrogen is derived",
    ]
    for phrase in forbidden_overclaims:
        require(phrase not in note, f"note avoids overclaim {phrase!r}", failures)

    weights = charged_species_weights()
    total_weight = sum(weights, Fraction(0, 1))
    b_qed = Fraction(4, 3) * total_weight
    require(total_weight == Fraction(8, 1), "charged species weight sum is 8", failures)
    require(b_qed == Fraction(32, 3), "b_QED weight algebra gives 32/3", failures)

    delta_inv_alpha = INV_ALPHA0_COMPARATOR - INV_ALPHA_MZ_REPO
    target_moment = delta_inv_alpha * (3.0 * math.pi / 2.0)
    common_log = target_moment / float(total_weight)
    effective_threshold = M_Z_GEV_COMPARATOR / math.exp(common_log)
    reconstructed_alpha0_inv = INV_ALPHA_MZ_REPO + (2.0 / (3.0 * math.pi)) * target_moment

    require(9.36 < delta_inv_alpha < 9.37, "inverse-alpha gap matches comparator scale", failures)
    require(44.1 < target_moment < 44.2, "target threshold moment is in expected band", failures)
    require(5.50 < common_log < 5.53, "common-log equivalent is in expected band", failures)
    require(0.35 < effective_threshold < 0.38, "effective threshold lands near hadronic scale", failures)
    require(
        abs(reconstructed_alpha0_inv - INV_ALPHA0_COMPARATOR) < 1e-12,
        "target moment reconstructs alpha(0) comparator by construction",
        failures,
    )

    alpha_inputs = set(ALPHA0_REQUIRED_INPUTS)
    require(closes_alpha0(alpha_inputs), "all alpha inputs close alpha0 predicate", failures)
    for missing in sorted(ALPHA0_REQUIRED_INPUTS):
        reduced = alpha_inputs - {missing}
        require(not closes_alpha0(reduced), f"alpha0 predicate fails without {missing}", failures)
    require(
        not closes_zero_import_hydrogen(alpha_inputs),
        "alpha0 package without electron mass and atomic NR limit does not close hydrogen",
        failures,
    )
    require(
        closes_zero_import_hydrogen(alpha_inputs | HYDROGEN_EXTRA_INPUTS),
        "hydrogen predicate requires alpha0 plus electron mass and physical-unit NR limit",
        failures,
    )

    require("1/alpha_EM(M_Z)" in usable_values and "127.67" in usable_values, "usable values contain retained alpha_EM(M_Z)", failures)
    require("alpha(0)" not in usable_values, "usable values do not list alpha(0) as retained", failures)
    canonical_ids = set(primitive_registry.get("canonical_ids", []))
    for primitive in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        require(primitive in canonical_ids or primitive in primitive_registry_text, f"primitive registry names {primitive}", failures)
    require("QED_LOOP_KERNEL_RETAINED" not in primitive_registry_text, "primitive registry does not contain QED loop-kernel primitive", failures)
    require("R_LEP_THRESHOLDS_RETAINED" not in primitive_registry_text, "primitive registry does not contain R-Lep thresholds primitive", failures)
    require("R_HAD_NP_RETAINED" not in primitive_registry_text, "primitive registry does not contain hadronic R(s) primitive", failures)
    require(
        "QED_LOOP_KERNEL_RETAINED" in qed_loop_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in qed_loop_no_go,
        "QED loop no-go keeps kernel handoff open",
        failures,
    )
    require(
        "R_LEP_THRESHOLDS_RETAINED" in r_lep_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in r_lep_no_go,
        "R-Lep no-go keeps threshold handoff open",
        failures,
    )

    print(f"SUMMARY failures={len(failures)}")
    if failures:
        for failure in failures:
            print(f"FAILED {failure}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
