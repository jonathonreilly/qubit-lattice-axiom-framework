"""One-hop dependency checks for the ideal Bell-measurement circuit row."""

from __future__ import annotations

import json
from pathlib import Path


SUPPLIERS: tuple[tuple[str, str, set[str]], ...] = (
    (
        "ideal encoded Bell resource",
        "teleportation_retained_axis_operator_algebra_closure_note",
        {"retained_bounded", "retained"},
    ),
    (
        "ideal logical gate/parity-measurement algebra",
        "teleportation_retained_axis_operator_algebra_closure_note",
        {"retained_bounded", "retained"},
    ),
    (
        "ideal computational-readout algebra",
        "teleportation_retained_axis_operator_algebra_closure_note",
        {"retained_bounded", "retained"},
    ),
    (
        "classical Bell-record handling",
        "teleportation_causal_channel_note",
        {"retained_bounded", "retained"},
    ),
)

DEPENDENCY_LINKS: tuple[tuple[str, str], ...] = (
    (
        "retained-axis Bell-resource/gate/parity/readout supplier",
        "TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md",
    ),
    (
        "retained classical record-handling supplier",
        "TELEPORTATION_CAUSAL_CHANNEL_NOTE.md",
    ),
)

CONCLUSION_BOUNDARY_CONTEXT = "TELEPORTATION_CONCLUSION_BOUNDARY_NOTE.md"


def _rows(root: Path, row_ids: set[str]) -> dict[str, dict[str, object]]:
    """Load only the requested rows from the canonical tracked ledger shards."""
    ledger_root = root / "docs" / "audit" / "data" / "ledger"
    rows: dict[str, dict[str, object]] = {}
    for row_id in sorted(row_ids):
        path = ledger_root / row_id[:2] / f"{row_id}.json"
        row = json.loads(path.read_text(encoding="utf-8"))
        if row.get("claim_id") != row_id:
            raise ValueError(f"ledger shard claim mismatch: {path}")
        rows[row_id] = row
    return rows


def _compact(text: str) -> str:
    return " ".join(text.split())


def bell_measurement_boundary_check_results(
    root: Path,
    prefix: str = "Bell-measurement dependency boundary",
) -> list[tuple[str, bool, str]]:
    """Check retained suppliers, source edges, and the conclusion boundary."""
    supplier_ids = {row_id for _, row_id, _ in SUPPLIERS}
    supplier_ids.add("teleportation_conclusion_boundary_note")
    rows = _rows(root, supplier_ids)
    out: list[tuple[str, bool, str]] = []

    for role, row_id, allowed in SUPPLIERS:
        row = rows[row_id]
        effective = row.get("effective_status")
        audit = row.get("audit_status")
        out.append(
            (
                f"{prefix}: {role} has retained one-hop support",
                effective in allowed and audit == "audited_clean",
                f"{row_id}: effective={effective}, audit={audit}",
            )
        )

    conclusion_row = rows["teleportation_conclusion_boundary_note"]
    out.append(
        (
            f"{prefix}: conclusion boundary has audited scope support",
            conclusion_row.get("effective_status") == "audited_renaming"
            and conclusion_row.get("audit_status") == "audited_renaming",
            "teleportation_conclusion_boundary_note: "
            f"effective={conclusion_row.get('effective_status')}, "
            f"audit={conclusion_row.get('audit_status')}",
        )
    )

    source = (
        root / "docs" / "TELEPORTATION_BELL_MEASUREMENT_CIRCUIT_NOTE.md"
    ).read_text(encoding="utf-8")
    for role, target in DEPENDENCY_LINKS:
        out.append(
            (
                f"{prefix}: source cites {role}",
                f"]({target})" in source,
                target,
            )
        )
    out.append(
        (
            f"{prefix}: source names non-load-bearing conclusion boundary context",
            f"`{CONCLUSION_BOUNDARY_CONTEXT}`" in source,
            CONCLUSION_BOUNDARY_CONTEXT,
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
