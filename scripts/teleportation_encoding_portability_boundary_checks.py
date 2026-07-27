"""Checkout-portable boundary checks for the encoding-portability runner."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ANCHORS = (
    "teleportation_causal_channel_note",
    "teleportation_measurement_record_note",
    "teleportation_apparatus_dynamics_closure_note",
    "teleportation_dynamical_resource_generation_note",
    "teleportation_resource_fidelity_note",
    "teleportation_retained_axis_operator_algebra_closure_note",
    "teleportation_cross_encoding_maps_note",
    "teleportation_three_register_cross_encoding_note",
    "teleportation_no_signaling_audit",
    "teleportation_3d_operator_consistent_end_to_end_note",
    "teleportation_conclusion_boundary_note",
)

AUDITED_STATUSES = {
    "audited_clean",
    "audited_conditional",
    "audited_failed",
    "audited_renaming",
}


def _rows(root: Path) -> dict[str, dict[str, object]]:
    """Load the exact anchor rows from tracked shards or a legacy monolith."""
    ledger_io_path = root / "docs" / "audit" / "scripts" / "ledger_io.py"
    spec = importlib.util.spec_from_file_location(
        "_teleportation_portability_ledger_io", ledger_io_path
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load canonical ledger reader: {ledger_io_path}")
    ledger_io = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ledger_io)

    if ledger_io.sharded():
        rows = {}
        for row_id in ANCHORS:
            row_path = ledger_io.shard_path(row_id)
            row = json.loads(row_path.read_text(encoding="utf-8"))
            if not isinstance(row, dict) or row.get("claim_id") != row_id:
                raise ValueError(f"audit ledger shard identity mismatch: {row_path}")
            rows[row_id] = row
        return rows

    rows = ledger_io.load_ledger().get("rows")
    if not isinstance(rows, dict):
        raise ValueError("canonical audit ledger does not contain a rows mapping")
    return rows


def _compact(text: str) -> str:
    return " ".join(text.split())


def teleportation_boundary_check_results(
    root: Path,
    prefix: str = "downstream teleportation boundary",
) -> list[tuple[str, bool, str]]:
    rows = _rows(root)
    out: list[tuple[str, bool, str]] = []

    for row_id in ANCHORS:
        row = rows.get(row_id, {})
        effective = row.get("effective_status")
        audit = row.get("audit_status")
        out.append(
            (
                f"{prefix}: {row_id} has a recorded audited boundary status",
                row.get("claim_id") == row_id
                and audit in AUDITED_STATUSES
                and isinstance(effective, str),
                f"effective={effective}, audit={audit}",
            )
        )

    conclusion = _compact(
        (root / "docs" / "TELEPORTATION_CONCLUSION_BOUNDARY_NOTE.md").read_text(
            encoding="utf-8"
        )
    )
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
        print(
            f"  {label}: {'PASS' if passed else 'FAIL'}"
            + (f" ({detail})" if detail else "")
        )
    return ok
