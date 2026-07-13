#!/usr/bin/env python3
"""One-shot backfill: write prose_status / prose_corrections on existing ledger rows.

Cleanup-1 introduced the prose_status and prose_corrections fields on
audit ledger rows (see docs/repo/VOCABULARY_HYGIENE_DESIGN.md). Existing
rows pre-date the field. This script writes the canonical pre-Cleanup-1
default ("not_evaluated_pre_vocab_lint" + empty corrections list) onto
every row that does not already carry the fields.

Usage:
  python3 docs/audit/scripts/backfill_prose_status.py [--dry-run]

After this runs, audit_lint.py's prose_status_backfill_pending notice
goes silent. New audits write prose_status via apply_audit.py.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import ledger_io

REPO_ROOT = Path(__file__).resolve().parents[3]
LEDGER_PATH = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

BACKFILL_VALUE = "not_evaluated_pre_vocab_lint"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would change without writing the ledger.",
    )
    args = parser.parse_args()

    ledger_io.ensure_cache()
    ledger = ledger_io.load_ledger()
    rows = ledger.get("rows", {})
    if not rows:
        print("audit_ledger.json has no rows; nothing to backfill")
        return 0

    backfilled = 0
    already_present = 0
    for cid, row in rows.items():
        if "prose_status" in row:
            already_present += 1
            continue
        row["prose_status"] = BACKFILL_VALUE
        row["prose_corrections"] = []
        backfilled += 1

    print(f"backfill_prose_status: {len(rows)} total rows")
    print(f"  already had prose_status: {already_present}")
    print(f"  backfilled with {BACKFILL_VALUE!r}: {backfilled}")

    if args.dry_run:
        print("dry-run: no changes written")
        return 0

    if backfilled == 0:
        print("no rows needed backfill; ledger unchanged")
        return 0

    ledger_io.save_ledger(ledger)
    print(f"wrote {LEDGER_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
