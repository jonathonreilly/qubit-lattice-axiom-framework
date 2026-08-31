#!/usr/bin/env python3
"""Validate archive/ledger entries against the schema in archive/README.md.

Light-lane checker: index integrity only. It grants no scientific status and
performs no audit. Exit 0 = all entries valid; 1 = violations (listed);
2 = usage error.

Usage:
  python3 archive/scripts/check_archive_entry.py [entry.json ...]
With no arguments, validates every archive/ledger/*/pr-*.json and the
LEDGER.md 1:1 correspondence.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ARCHIVE_ROOT = Path(__file__).resolve().parents[1]
LEDGER_DIR = ARCHIVE_ROOT / "ledger"
LEDGER_MD = ARCHIVE_ROOT / "LEDGER.md"

REQUIRED = ("id", "title", "science", "source", "carried_by", "review", "status")
OPTIONAL = ("forcing", "verdict_pair", "promotion_candidate", "disputed", "promoted_pr")
# Keys that would smuggle audit authority into the light lane.
FORBIDDEN = ("audit_status", "effective_status", "claim_type", "verdict",
             "retained", "audited_clean")
MIN_SCIENCE = 40


def check_entry(path: Path) -> list[str]:
    errs: list[str] = []
    try:
        e = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: unreadable ({exc})"]

    for k in REQUIRED:
        if k not in e:
            errs.append(f"{path}: missing required key '{k}'")
    for k in e:
        if k not in REQUIRED + OPTIONAL:
            errs.append(f"{path}: unknown key '{k}'")
        if k in FORBIDDEN:
            errs.append(f"{path}: forbidden audit-authority key '{k}'")
    if errs:
        return errs

    m = re.fullmatch(r"pr-(\d+)", e["id"])
    if not m:
        errs.append(f"{path}: id '{e['id']}' not of form pr-<N>")
    elif path.stem != e["id"]:
        errs.append(f"{path}: filename stem != id '{e['id']}'")
    else:
        n = int(m.group(1))
        src = e.get("source") or {}
        if not isinstance(src, dict) or src.get("pr") != n:
            errs.append(f"{path}: source.pr != {n}")
        if not str(src.get("branch", "")).strip():
            errs.append(f"{path}: source.branch empty")
        if path.parent.name != f"{n % 100:02d}":
            errs.append(f"{path}: shard dir '{path.parent.name}' != {n % 100:02d}")
    if len(str(e.get("science", "")).strip()) < MIN_SCIENCE:
        errs.append(f"{path}: science line under {MIN_SCIENCE} chars")
    if not str(e.get("carried_by", "")).strip():
        errs.append(f"{path}: carried_by empty")
    rev = e.get("review") or {}
    if not isinstance(rev, dict) or rev.get("level") != "light" or not rev.get("process"):
        errs.append(f"{path}: review must be {{level: 'light', process: <text>}}")
    if e.get("status") != "archived":
        errs.append(f"{path}: status must be 'archived'")
    for k in ("forcing", "promotion_candidate", "disputed"):
        if k in e and not isinstance(e[k], bool):
            errs.append(f"{path}: {k} must be boolean")
    return errs


def main(argv: list[str]) -> int:
    if argv:
        paths = [Path(a) for a in argv]
        for p in paths:
            if not p.is_file():
                print(f"FAIL: no such file: {p}", file=sys.stderr)
                return 2
    else:
        paths = sorted(LEDGER_DIR.glob("*/pr-*.json"))

    errs: list[str] = []
    for p in paths:
        errs.extend(check_entry(p))

    if not argv and LEDGER_MD.is_file():
        ids = {p.stem for p in paths}
        listed = set(re.findall(r"\bpr-(\d+)\b", LEDGER_MD.read_text()))
        listed = {f"pr-{n}" for n in listed}
        for missing in sorted(ids - listed):
            errs.append(f"LEDGER.md: entry {missing} not listed")
        for extra in sorted(listed - ids):
            errs.append(f"LEDGER.md: lists {extra} with no ledger file")

    for e in errs:
        print(f"FAIL: {e}")
    print(f"{'FAIL' if errs else 'OK'}: {len(paths)} entries checked, "
          f"{len(errs)} violations")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
