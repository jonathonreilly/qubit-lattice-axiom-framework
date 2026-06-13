"""Shared downstream boundary checks for teleportation open-gate planning rows."""

from __future__ import annotations

import json
from pathlib import Path


ANCHORS: dict[str, set[str]] = {
    "teleportation_causal_channel_note": {"retained_bounded", "retained"},
    "teleportation_measurement_record_note": {"retained_bounded", "retained"},
    "teleportation_apparatus_dynamics_closure_note": {"retained_bounded", "retained"},
    "teleportation_dynamical_resource_generation_note": {"retained_bounded", "retained"},
    "teleportation_resource_fidelity_note": {"retained_bounded", "retained"},
    "teleportation_retained_axis_operator_algebra_closure_note": {"retained_bounded", "retained"},
    "teleportation_cross_encoding_maps_note": {"retained_bounded", "retained"},
    "teleportation_three_register_cross_encoding_note": {"retained_bounded", "retained"},
    "teleportation_no_signaling_audit": {"retained_bounded", "retained"},
    "teleportation_3d_operator_consistent_end_to_end_note": {"retained_bounded", "retained"},
    "teleportation_conclusion_boundary_note": {"audited_renaming", "retained_bounded", "retained"},
}


def _rows(root: Path) -> dict[str, dict[str, object]]:
    return json.loads((root / "docs" / "audit" / "data" / "audit_ledger.json").read_text())["rows"]


def _compact(text: str) -> str:
    return " ".join(text.split())


def teleportation_boundary_check_results(root: Path, prefix: str = "downstream teleportation boundary") -> list[tuple[str, bool, str]]:
    rows = _rows(root)
    out: list[tuple[str, bool, str]] = []

    for row_id, allowed in ANCHORS.items():
        row = rows.get(row_id, {})
        effective = row.get("effective_status")
        audit = row.get("audit_status")
        out.append(
            (
                f"{prefix}: {row_id} has audited bounded/status support",
                effective in allowed and audit in {"audited_clean", "audited_renaming"},
                f"effective={effective}, audit={audit}",
            )
        )

    conclusion = _compact((root / "docs" / "TELEPORTATION_CONCLUSION_BOUNDARY_NOTE.md").read_text(encoding="utf-8"))
    out.append(
        (
            f"{prefix}: lane remains state-teleportation only with no-transfer boundary",
            all(
                phrase in conclusion
                for phrase in [
                    "ordinary quantum state teleportation only",
                    "No matter, mass, charge, energy, object, or faster-than-light transport is claimed.",
                    "unconditional_closed = False",
                    "nature-grade closure HOLD",
                ]
            ),
            "checked conclusion boundary note",
        )
    )
    out.append(
        (
            f"{prefix}: finite planning support is not nature-grade closure",
            "planning_closed = True" in conclusion
            and "promote_to_nature_grade = False" in conclusion,
            "planning closure and nature-grade hold are distinct",
        )
    )
    return out


def print_boundary_results(results: list[tuple[str, bool, str]]) -> bool:
    ok = True
    print()
    print("Downstream boundary checks:")
    for label, passed, detail in results:
        ok = ok and passed
        print(f"  {label}: {'PASS' if passed else 'FAIL'}" + (f" ({detail})" if detail else ""))
    return ok
