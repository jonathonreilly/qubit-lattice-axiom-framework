#!/usr/bin/env python3
"""Validate archive/ledger entries against the schema in archive/README.md.

Light-lane checker: index integrity only. It grants no scientific status and
performs no audit. Exit 0 = valid; 1 = violations (listed); 2 = usage error.

Usage:
  python3 archive/scripts/check_archive_entry.py [entry.json ...]
With no arguments: validates every JSON under archive/ledger/ (flagging any
file that does not match ledger/<xx>/pr-<N>.json). With arguments: each path
must be a ledger entry file under archive/ledger/. The LEDGER.md 1:1 index
correspondence against the FULL discovered entry set runs in BOTH modes.
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
# Keys that would smuggle audit authority into the light lane, at ANY depth.
FORBIDDEN = ("audit_status", "effective_status", "claim_type", "verdict",
             "retained", "audited_clean", "claim_scope", "claim_id")
MIN_SCIENCE = 40
ID_RE = re.compile(r"pr-(\d+)\Z")
INDEX_LINE_RE = re.compile(r"^- (pr-\d+):", re.MULTILINE)


def forbidden_keys(obj, trail="") -> list[str]:
    """Every forbidden key anywhere in the JSON tree."""
    hits: list[str] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            where = f"{trail}.{k}" if trail else str(k)
            if k in FORBIDDEN:
                hits.append(where)
            hits.extend(forbidden_keys(v, where))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits.extend(forbidden_keys(v, f"{trail}[{i}]"))
    return hits


def nonempty_str(v) -> bool:
    return isinstance(v, str) and bool(v.strip())


def check_path(path: Path) -> tuple[int | None, list[str]]:
    """Enforce ledger/<xx>/pr-<N>.json under the archive root."""
    try:
        rel = path.resolve().relative_to(LEDGER_DIR.resolve())
    except ValueError:
        return None, [f"{path}: not under {LEDGER_DIR}"]
    m = ID_RE.fullmatch(path.stem)
    if len(rel.parts) != 2 or path.suffix != ".json" or not m:
        return None, [f"{path}: path is not ledger/<xx>/pr-<N>.json"]
    n = int(m.group(1))
    if rel.parts[0] != f"{n % 100:02d}":
        return n, [f"{path}: shard dir '{rel.parts[0]}' != {n % 100:02d}"]
    return n, []


def check_entry(path: Path) -> list[str]:
    n, errs = check_path(path)
    try:
        e = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return errs + [f"{path}: unreadable ({exc})"]
    if not isinstance(e, dict):
        return errs + [f"{path}: top level is not an object"]

    for k in REQUIRED:
        if k not in e:
            errs.append(f"{path}: missing required key '{k}'")
    for k in e:
        if k not in REQUIRED + OPTIONAL:
            errs.append(f"{path}: unknown key '{k}'")
    for where in forbidden_keys(e):
        errs.append(f"{path}: forbidden audit-authority key at '{where}'")
    if any("missing required" in x for x in errs):
        return errs

    if not nonempty_str(e["id"]) or (n is not None and e["id"] != f"pr-{n}"):
        errs.append(f"{path}: id must equal filename stem 'pr-{n}'")
    if not nonempty_str(e["title"]):
        errs.append(f"{path}: title must be a non-empty string")
    if not isinstance(e["science"], str) or len(e["science"].strip()) < MIN_SCIENCE:
        errs.append(f"{path}: science must be a string of >= {MIN_SCIENCE} chars")
    if not nonempty_str(e["carried_by"]):
        errs.append(f"{path}: carried_by must be a non-empty string")

    src = e["source"]
    if not isinstance(src, dict) or set(src) != {"pr", "branch"}:
        errs.append(f"{path}: source must be exactly {{pr, branch}}")
    else:
        if type(src["pr"]) is not int or (n is not None and src["pr"] != n):
            errs.append(f"{path}: source.pr must be the integer {n}")
        if not nonempty_str(src["branch"]):
            errs.append(f"{path}: source.branch must be a non-empty string")

    rev = e["review"]
    if (not isinstance(rev, dict) or set(rev) != {"level", "process"}
            or rev["level"] != "light" or not nonempty_str(rev["process"])):
        errs.append(f"{path}: review must be exactly {{level: 'light', process: <non-empty str>}}")
    if e["status"] != "archived":
        errs.append(f"{path}: status must be 'archived'")

    for k in ("forcing", "promotion_candidate", "disputed"):
        if k in e and not isinstance(e[k], bool):
            errs.append(f"{path}: {k} must be boolean")
    if "verdict_pair" in e and not isinstance(e["verdict_pair"], str):
        errs.append(f"{path}: verdict_pair must be a string")
    if "promoted_pr" in e and type(e["promoted_pr"]) is not int:
        errs.append(f"{path}: promoted_pr must be an integer")
    return errs


def check_index(entry_ids: set[str]) -> list[str]:
    """LEDGER.md holds exactly one '- pr-<N>:' line per entry."""
    if not LEDGER_MD.is_file():
        if entry_ids:
            return [f"LEDGER.md: missing but {len(entry_ids)} ledger entries exist"]
        return []
    listed = INDEX_LINE_RE.findall(LEDGER_MD.read_text())
    errs = [f"LEDGER.md: duplicate index line for {i}"
            for i in sorted({i for i in listed if listed.count(i) > 1})]
    errs += [f"LEDGER.md: entry {i} not listed" for i in sorted(entry_ids - set(listed))]
    errs += [f"LEDGER.md: lists {i} with no ledger file" for i in sorted(set(listed) - entry_ids)]
    return errs


def main(argv: list[str]) -> int:
    if argv:
        paths = [Path(a) for a in argv]
        for p in paths:
            if not p.is_file():
                print(f"FAIL: no such file: {p}", file=sys.stderr)
                return 2
    else:
        paths = sorted(p for p in LEDGER_DIR.rglob("*.json")) if LEDGER_DIR.is_dir() else []

    errs: list[str] = []
    for p in paths:
        errs.extend(check_entry(p))
    all_entries = (sorted(LEDGER_DIR.rglob("*.json"))
                   if LEDGER_DIR.is_dir() else [])
    if not argv and LEDGER_DIR.is_dir():
        strays = sorted(set(LEDGER_DIR.rglob("*")) - set(all_entries))
        errs.extend(f"{s}: stray non-entry file under ledger/" for s in strays
                    if s.is_file())
    # Index 1:1 runs in BOTH modes, always against the full discovered set.
    errs.extend(check_index({p.stem for p in all_entries
                             if ID_RE.fullmatch(p.stem)}))
    if not all_entries and LEDGER_MD.is_file() and INDEX_LINE_RE.search(LEDGER_MD.read_text()):
        errs.append("LEDGER.md: lists entries but ledger/ holds none")

    for e in errs:
        print(f"FAIL: {e}")
    label = "OK" if not errs else "FAIL"
    detail = " (empty store)" if not paths and not errs else ""
    print(f"{label}: {len(paths)} entries checked, {len(errs)} violations{detail}")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
