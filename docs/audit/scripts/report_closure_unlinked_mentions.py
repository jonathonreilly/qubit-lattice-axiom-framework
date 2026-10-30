#!/usr/bin/env python3
"""Report notes named inside a dependency closure but outside its edges.

The citation graph counts markdown links only. A note named in backticks or
plain text adds no edge, and some citations were converted to backticks to
break cycles, so a closure built from `deps` can miss a real dependency.

Run this before auditing a TOE candidate or a proof to publish. Each reported
note needs a decision: dependency (add the link, then re-run) or context.

Read-only: it writes no ledger, status or verdict, and is not a pipeline stage.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
NOTE_NAME_RE = re.compile(r"[A-Za-z0-9_\-.]{4,}\.md\b")


def load_rows(repo_root: Path) -> dict[str, dict]:
    rows = {}
    for shard in (repo_root / "docs/audit/data/ledger").glob("*/*.json"):
        row = json.loads(shard.read_text(encoding="utf-8"))
        rows[row["claim_id"]] = row
    return rows


def dependency_closure(rows: dict[str, dict], roots: list[str]) -> set[str]:
    seen: set[str] = set()
    stack = list(roots)
    while stack:
        claim_id = stack.pop()
        if claim_id in seen or claim_id not in rows:
            continue
        seen.add(claim_id)
        stack.extend(rows[claim_id].get("deps") or [])
    return seen


def unreadable_notes(rows: dict[str, dict], closure: set[str], repo_root: Path) -> list[str]:
    """Closure notes absent on disk: a sparse checkout would under-report them."""
    return sorted(
        claim_id
        for claim_id in closure
        if not (repo_root / (rows[claim_id].get("note_path") or "")).is_file()
    )


def unlinked_mentions(
    rows: dict[str, dict], closure: set[str], repo_root: Path
) -> list[dict]:
    """One entry per note named in the closure but outside it, with who named it."""
    by_name = {
        Path(row["note_path"]).name.lower(): claim_id
        for claim_id, row in rows.items()
        if row.get("note_path")
    }
    named_by: dict[str, set[str]] = {}
    for claim_id in closure:
        path = repo_root / (rows[claim_id].get("note_path") or "")
        if not path.is_file():
            continue
        for name in NOTE_NAME_RE.findall(path.read_text(encoding="utf-8", errors="replace")):
            target = by_name.get(Path(name).name.lower())
            if target and target not in closure:
                named_by.setdefault(target, set()).add(claim_id)
    return [
        {
            "claim_id": target,
            "note_path": rows[target].get("note_path"),
            "claim_type": rows[target].get("claim_type"),
            "named_by": sorted(sources),
        }
        for target, sources in sorted(named_by.items())
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", action="append", required=True, help="root claim id; repeatable")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    rows = load_rows(REPO_ROOT)
    unknown = [root for root in args.root if root not in rows]
    if unknown:
        print(f"unknown claim id: {', '.join(unknown)}", file=sys.stderr)
        return 2
    closure = dependency_closure(rows, args.root)
    unreadable = unreadable_notes(rows, closure, REPO_ROOT)
    if unreadable:
        print(
            f"{len(unreadable)} closure notes are not on disk (sparse checkout?): "
            f"{', '.join(unreadable[:5])}",
            file=sys.stderr,
        )
        return 3
    mentions = unlinked_mentions(rows, closure, REPO_ROOT)
    if args.json:
        print(json.dumps({"closure_size": len(closure), "mentions": mentions}, indent=1))
        return 0
    print(f"closure: {len(closure)} notes; named but outside it: {len(mentions)}")
    for entry in mentions:
        print(f"  {entry['note_path']} [{entry['claim_type']}] <- {', '.join(entry['named_by'][:3])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
