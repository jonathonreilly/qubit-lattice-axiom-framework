#!/usr/bin/env python3
"""Repo-invariants harness: snapshot, diff, and check structural invariants.

Purpose. Landing hygiene/tooling changes safely requires a mechanical
before/after ruler. This tool measures the repository's structural
invariants from TRACKED sources only (it never runs the audit pipeline and
never mutates anything), so any PR can demonstrate "nothing changed except
what the PR declares."

Modes
  --snapshot [PATH]        write a canonical JSON snapshot (default: stdout)
  --diff A B [--allow k1,k2]
                           compare two snapshots; exit 1 on differences in
                           fields not named in --allow
  --check [--enforce-links]
                           run absolute integrity checks; broken/gitignored
                           authority links are WARN by default, errors with
                           --enforce-links

Invariants measured
  ledger.shard_count           number of tracked ledger shard JSON files
  ledger.claim_ids_sha256      hash of the sorted claim-id set
  ledger.duplicate_claim_ids   must be empty
  ledger.effective_status_histogram
  ledger.retained_grade_total  retained + retained_bounded + retained_no_go
                               + decoration_under_* rows
  ledger.rows_with_missing_note_path  informational count
  premises.ids                 registered axiom/primitive premise node ids
  obligations.ids              open derivation-obligation ids
  docs.md_count                markdown files directly under docs/
  docs.duplicate_basenames     basename collisions across docs/** (row ids
                               derive from filename stems)
  authority_links.violations   markdown links on authority surfaces whose
                               target is missing from the working tree or
                               gitignored (a gitignored target 404s for any
                               fresh clone or GitHub reader)

This is a read-only measurement tool. It sets no audit status, writes no
generated surface, and is not part of verdict minting.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter

REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
)

LEDGER_DIR = os.path.join("docs", "audit", "data", "ledger")
PREMISE_NODES = os.path.join("docs", "audit", "data", "axiom_premise_nodes.json")
OBLIGATIONS = os.path.join("docs", "audit", "data", "derivation_obligations.json")

# Authority surfaces: the reading path an external reader or agent follows.
AUTHORITY_SURFACE_GLOBS = [
    "README.md",
    os.path.join("docs", "repo"),
    os.path.join("docs", "publication", "ci3_z3"),
    os.path.join("docs", "audit"),
    os.path.join("docs", "lanes", "README.md"),
    os.path.join("docs", "lanes", "open_science", "README.md"),
]

MD_LINK_RE = re.compile(r"\]\(([^)#\s]+)(?:#[^)\s]*)?\)")

RETAINED_GRADE_PREFIXES = ("decoration_under_",)
RETAINED_GRADE_EXACT = {"retained", "retained_bounded", "retained_no_go"}


def _rel(path: str) -> str:
    return os.path.relpath(path, REPO_ROOT)


def _iter_ledger_shards():
    base = os.path.join(REPO_ROOT, LEDGER_DIR)
    for dirpath, _dirnames, filenames in os.walk(base):
        for name in sorted(filenames):
            if name.endswith(".json"):
                yield os.path.join(dirpath, name)


def collect_ledger() -> dict:
    claim_ids = []
    histogram: Counter = Counter()
    missing_note_paths = 0
    parse_errors = []
    for shard in _iter_ledger_shards():
        try:
            with open(shard, "r", encoding="utf-8") as fh:
                row = json.load(fh)
        except (json.JSONDecodeError, OSError) as exc:
            parse_errors.append(f"{_rel(shard)}: {exc}")
            continue
        claim_id = row.get("claim_id") or os.path.splitext(os.path.basename(shard))[0]
        claim_ids.append(claim_id)
        histogram[str(row.get("effective_status", "MISSING"))] += 1
        note_path = row.get("note_path")
        if note_path and not os.path.exists(os.path.join(REPO_ROOT, note_path)):
            missing_note_paths += 1

    dupes = sorted(cid for cid, n in Counter(claim_ids).items() if n > 1)
    ids_sha = hashlib.sha256("\n".join(sorted(claim_ids)).encode()).hexdigest()
    retained_total = sum(
        count
        for status, count in histogram.items()
        if status in RETAINED_GRADE_EXACT or status.startswith(RETAINED_GRADE_PREFIXES)
    )
    return {
        "shard_count": len(claim_ids) + len(parse_errors),
        "claim_ids_sha256": ids_sha,
        "duplicate_claim_ids": dupes,
        "effective_status_histogram": dict(sorted(histogram.items())),
        "retained_grade_total": retained_total,
        "rows_with_missing_note_path": missing_note_paths,
        "shard_parse_errors": parse_errors,
    }


def collect_premises() -> dict:
    path = os.path.join(REPO_ROOT, PREMISE_NODES)
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, dict):
        nodes = data.get("nodes", data)
        ids = sorted(nodes.keys()) if isinstance(nodes, dict) else sorted(
            str(node.get("id", node.get("premise_id", "?"))) for node in nodes
        )
    else:
        ids = sorted(str(node.get("id", node.get("premise_id", "?"))) for node in data)
    with open(path, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    return {"ids": ids, "file_sha256": digest}


def collect_obligations() -> dict:
    path = os.path.join(REPO_ROOT, OBLIGATIONS)
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    entries = data.get("nodes", data.get("obligations", data)) if isinstance(data, dict) else data
    if isinstance(entries, dict):
        ids = sorted(entries.keys())
    else:
        ids = sorted(str(entry.get("id", "?")) for entry in entries)
    return {"ids": ids}


def collect_docs() -> dict:
    docs_dir = os.path.join(REPO_ROOT, "docs")
    top_level_md = sorted(
        name for name in os.listdir(docs_dir) if name.endswith(".md")
    )
    basenames: Counter = Counter()
    for dirpath, _dirnames, filenames in os.walk(docs_dir):
        for name in filenames:
            if name.endswith(".md"):
                basenames[name] += 1
    dupes = sorted(name for name, n in basenames.items() if n > 1)
    return {"md_count": len(top_level_md), "duplicate_basenames": dupes}


def _authority_surface_files() -> list:
    files = []
    for entry in AUTHORITY_SURFACE_GLOBS:
        full = os.path.join(REPO_ROOT, entry)
        if os.path.isfile(full):
            files.append(full)
        elif os.path.isdir(full):
            for name in sorted(os.listdir(full)):
                if name.endswith(".md"):
                    files.append(os.path.join(full, name))
    return files


def _gitignored(paths: list) -> set:
    """Return the subset of repo-relative paths that are gitignored."""
    if not paths:
        return set()
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "check-ignore", "--stdin"],
        input="\n".join(paths),
        capture_output=True,
        text=True,
    )
    # exit 0: some ignored; 1: none ignored; >1: real error
    if proc.returncode > 1:
        raise RuntimeError(f"git check-ignore failed: {proc.stderr.strip()}")
    return set(proc.stdout.splitlines())


def collect_authority_links() -> dict:
    surface_files = _authority_surface_files()
    candidates = {}  # repo-relative target -> [source files]
    scanned = 0
    for path in surface_files:
        scanned += 1
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for match in MD_LINK_RE.finditer(text):
            target = match.group(1)
            if "://" in target or target.startswith("mailto:"):
                continue
            resolved = os.path.normpath(
                os.path.join(os.path.dirname(path), target)
            )
            if not resolved.startswith(REPO_ROOT + os.sep):
                continue
            rel = _rel(resolved)
            candidates.setdefault(rel, set()).add(_rel(path))

    ignored = _gitignored(sorted(candidates))
    violations = []
    for rel in sorted(candidates):
        missing = not os.path.exists(os.path.join(REPO_ROOT, rel))
        if rel in ignored or missing:
            violations.append(
                {
                    "target": rel,
                    "reason": "gitignored" if rel in ignored else "missing",
                    "sources": sorted(candidates[rel]),
                }
            )
    return {"surfaces_scanned": scanned, "violations": violations}


def build_snapshot() -> dict:
    return {
        "invariants_version": 1,
        "ledger": collect_ledger(),
        "premises": collect_premises(),
        "obligations": collect_obligations(),
        "docs": collect_docs(),
        "authority_links": collect_authority_links(),
    }


def _flatten(prefix: str, value, out: dict):
    if isinstance(value, dict):
        for key, sub in value.items():
            _flatten(f"{prefix}.{key}" if prefix else str(key), sub, out)
    else:
        out[prefix] = value


def run_diff(path_a: str, path_b: str, allow: set) -> int:
    with open(path_a, "r", encoding="utf-8") as fh:
        snap_a = json.load(fh)
    with open(path_b, "r", encoding="utf-8") as fh:
        snap_b = json.load(fh)
    flat_a: dict = {}
    flat_b: dict = {}
    _flatten("", snap_a, flat_a)
    _flatten("", snap_b, flat_b)
    diffs = []
    for key in sorted(set(flat_a) | set(flat_b)):
        if flat_a.get(key) != flat_b.get(key):
            diffs.append((key, flat_a.get(key), flat_b.get(key)))
    blocked = []
    for key, before, after in diffs:
        allowed = any(key == a or key.startswith(a + ".") for a in allow)
        marker = "ALLOWED" if allowed else "CHANGED"
        if not allowed:
            blocked.append(key)
        print(f"{marker}: {key}\n    before: {before!r}\n    after:  {after!r}")
    if not diffs:
        print("IDENTICAL: snapshots match on every invariant.")
    if blocked:
        print(f"\nFAIL: {len(blocked)} undeclared invariant change(s).")
        return 1
    print(f"\nOK: {len(diffs)} change(s), all declared via --allow." if diffs else "OK")
    return 0


def run_check(enforce_links: bool) -> int:
    snapshot = build_snapshot()
    failures = []
    warnings = []

    ledger = snapshot["ledger"]
    if ledger["shard_parse_errors"]:
        failures.append(f"ledger shard parse errors: {ledger['shard_parse_errors']}")
    if ledger["duplicate_claim_ids"]:
        failures.append(f"duplicate claim ids: {ledger['duplicate_claim_ids']}")
    known_dupes = {"README.md", "SKILL.md"}
    unexpected = [
        name for name in snapshot["docs"]["duplicate_basenames"] if name not in known_dupes
    ]
    if unexpected:
        failures.append(f"unexpected duplicate doc basenames: {unexpected}")

    link_violations = snapshot["authority_links"]["violations"]
    if link_violations:
        lines = [
            f"  {item['target']} ({item['reason']}) <- {', '.join(item['sources'])}"
            for item in link_violations
        ]
        message = "authority-surface links to missing/gitignored targets:\n" + "\n".join(lines)
        if enforce_links:
            failures.append(message)
        else:
            warnings.append(message)

    for warning in warnings:
        print(f"WARN: {warning}")
    for failure in failures:
        print(f"FAIL: {failure}")
    summary = (
        f"rows={ledger['shard_count']} retained_grade={ledger['retained_grade_total']} "
        f"link_violations={len(link_violations)} "
        f"({'enforced' if enforce_links else 'warn-only'})"
    )
    print(("FAIL " if failures else "PASS ") + summary)
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--snapshot", nargs="?", const="-", metavar="PATH")
    mode.add_argument("--diff", nargs=2, metavar=("A", "B"))
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--allow", default="", help="comma-separated invariant keys allowed to differ in --diff")
    parser.add_argument("--enforce-links", action="store_true")
    args = parser.parse_args()

    if args.snapshot is not None:
        snapshot = build_snapshot()
        text = json.dumps(snapshot, indent=1, sort_keys=True)
        if args.snapshot == "-":
            print(text)
        else:
            with open(args.snapshot, "w", encoding="utf-8") as fh:
                fh.write(text + "\n")
            print(f"wrote {args.snapshot}")
        return 0
    if args.diff:
        allow = {item.strip() for item in args.allow.split(",") if item.strip()}
        return run_diff(args.diff[0], args.diff[1], allow)
    return run_check(args.enforce_links)


if __name__ == "__main__":
    sys.exit(main())
