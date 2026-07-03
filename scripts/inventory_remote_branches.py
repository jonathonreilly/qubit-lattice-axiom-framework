#!/usr/bin/env python3
"""Read-only compatibility runner for the branch-cleanup inventory note.

The canonical inventory tool lives at ``docs/audit/scripts/inventory_remote_branches.py``
and writes ``docs/audit/data/branch_inventory.json`` when intentionally run by
an operator.  The audit ledger historically registered this shorter
``scripts/`` path, so this runner verifies the inventory surface without
regenerating audit data as a side effect.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    return condition


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def main() -> int:
    print("Branch cleanup inventory compatibility runner")
    print("=" * 72)

    note = read("docs/BRANCH_CLEANUP_RECOMMENDATION_2026-05-03.md")
    tool_path = ROOT / "docs/audit/scripts/inventory_remote_branches.py"
    inventory_path = ROOT / "docs/audit/data/branch_inventory.json"

    check(
        "branch cleanup note cites the canonical audit inventory tool",
        "`docs/audit/scripts/inventory_remote_branches.py`" in note
        and "Always re-inventory first" in note,
    )
    check(
        "canonical inventory tool exists outside scripts/",
        tool_path.exists(),
        tool_path.relative_to(ROOT).as_posix(),
    )

    tool_text = tool_path.read_text(encoding="utf-8")
    check(
        "canonical tool is documented as read-only inventory before execution",
        "Read-only." in tool_text
        and "archive_and_delete_branches" not in tool_text,
    )
    check(
        "canonical tool writes only the branch inventory data file",
        "OUTPUT_PATH = DATA_DIR / \"branch_inventory.json\"" in tool_text
        and "OUTPUT_PATH.write_text" in tool_text,
    )

    payload = json.loads(inventory_path.read_text(encoding="utf-8"))
    branches = payload.get("branches", [])
    category_counts = payload.get("category_counts", {})
    check("checked-in branch inventory has a branch list", isinstance(branches, list) and bool(branches))
    check(
        "checked-in branch inventory has category counts",
        isinstance(category_counts, dict) and bool(category_counts),
        ",".join(sorted(category_counts)[:6]),
    )
    check(
        "branch cleanup note remains documentation only",
        "No remote branches deleted, no local branches\npruned." in note,
    )

    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
