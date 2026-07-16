#!/usr/bin/env python3
"""Repo-invariants harness: snapshot, diff, and check structural invariants.

Purpose. Landing hygiene/tooling changes safely requires a mechanical
before/after ruler. This tool measures a fixed set of structural invariants
from the repository's GIT-TRACKED state (untracked scratch files do not
perturb the snapshot), so any PR can demonstrate "none of the measured
invariants changed except those the PR declares."

Modes
  --snapshot [PATH]        write a canonical JSON snapshot (default: stdout);
                           snapshot mode writes only the explicitly requested
                           output path and refuses tracked repository paths
  --diff A B [--allow k1,k2]
                           compare two snapshots; exit 1 on differences in
                           fields not named in --allow (dot-segment-bounded)
  --check [--enforce-links]
                           run absolute integrity checks; authority-link
                           violations are WARN by default, errors with
                           --enforce-links

Invariants measured (tracked state only)
  ledger.shard_count           tracked ledger shard JSON files
  ledger.claim_ids_sha256      hash of the sorted claim-id set
  ledger.duplicate_claim_ids   must be empty
  ledger.effective_status_histogram
  ledger.retained_grade_total  retained + retained_bounded + retained_no_go
                               + decoration_under_* rows
  ledger.rows_with_missing_note_path  informational count (vs tracked set)
  ledger.shard_parse_errors    unreadable or schema-invalid shards
  premises.ids                 registered axiom/primitive premise node ids
  obligations.ids              open derivation-obligation ids
  docs.md_count                tracked markdown files directly under docs/
  docs.duplicate_basenames     tracked basename collisions across docs/**
  authority_links.violations   markdown links on authority surfaces whose
                               target file is not tracked (missing, untracked,
                               or gitignored — each of which 404s for a fresh
                               clone or GitHub reader). Code spans and fenced
                               code blocks are masked before link extraction.

Repository inputs are read-only; no audit status is set, no generated surface
is written, no verdict is minted.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import posixpath
import re
import subprocess
import sys
import urllib.parse
from collections import Counter

REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
)

LEDGER_PREFIX = "docs/audit/data/ledger/"
PREMISE_NODES = "docs/audit/data/axiom_premise_nodes.json"
OBLIGATIONS = "docs/audit/data/derivation_obligations.json"

# Authority surfaces: the reading path an external reader or agent follows.
AUTHORITY_SURFACES = (
    "README.md",
    "docs/repo/",
    "docs/publication/ci3_z3/",
    "docs/audit/",
    "docs/lanes/README.md",
    "docs/lanes/open_science/README.md",
)

RETAINED_GRADE_PREFIXES = ("decoration_under_",)
RETAINED_GRADE_EXACT = {"retained", "retained_bounded", "retained_no_go"}

_MISSING = object()


# --- markdown scanning -------------------------------------------------------
# Scope claim: this is a conservative reader-path scanner for the authority
# surfaces, implemented as a line/character scan of the CommonMark constructs
# those surfaces actually use (fenced code blocks incl. longer/indented/tilde
# fences and unclosed fences, backtick-run code spans, inline links with
# angle-bracket or balanced-paren destinations and ', ", ( titles, escaped
# openers, fragments/queries). It is not a full CommonMark parser.

_FENCE_OPEN_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")


def mask_code(text: str) -> str:
    """Blank out fenced code blocks (CommonMark 4.5: >=3 markers, <=3-space
    indent, closer at least as long, unclosed runs to end) and backtick-run
    code spans (CommonMark 6.1: closed by the next run of EQUAL length)."""
    out_lines = []
    fence_char, fence_len = None, 0
    for line in text.split("\n"):
        if fence_char is None:
            m = _FENCE_OPEN_RE.match(line)
            if m:
                fence_char, fence_len = m.group(1)[0], len(m.group(1))
                out_lines.append("")
                continue
            out_lines.append(line)
        else:
            stripped = line.strip()
            if (stripped and set(stripped) == {fence_char}
                    and len(stripped) >= fence_len
                    and len(line) - len(line.lstrip()) <= 3):
                fence_char = None
            out_lines.append("")
    masked = "\n".join(out_lines)

    # backtick-run code spans on the fence-masked text
    runs = [(m.start(), len(m.group(0))) for m in re.finditer(r"`+", masked)]
    spans = []
    i = 0
    while i < len(runs):
        start, length = runs[i]
        for j in range(i + 1, len(runs)):
            if runs[j][1] == length:
                spans.append((start, runs[j][0] + runs[j][1]))
                i = j
                break
        i += 1
    chars = list(masked)
    for a, b in spans:
        for k in range(a, b):
            if chars[k] != "\n":
                chars[k] = " "
    return "".join(chars)


def _unescaped(text: str, idx: int) -> bool:
    backslashes = 0
    j = idx - 1
    while j >= 0 and text[j] == "\\":
        backslashes += 1
        j -= 1
    return backslashes % 2 == 0


def _parse_destination(text: str, pos: int):
    """Parse a CommonMark inline-link destination starting just after '('.
    Returns (destination, index-after-closing-paren) or None."""
    n = len(text)
    while pos < n and text[pos] in " \t":
        pos += 1
    if pos < n and text[pos] == "<":
        end = pos + 1
        while end < n and text[end] != "\n":
            if text[end] == ">" and _unescaped(text, end):
                dest = text[pos + 1:end]
                return _finish_after_dest(text, end + 1, dest)
            end += 1
        return None
    depth = 0
    end = pos
    while end < n:
        ch = text[end]
        if ch in " \t\n":
            break
        if ch == "(" and _unescaped(text, end):
            depth += 1
        elif ch == ")" and _unescaped(text, end):
            if depth == 0:
                break
            depth -= 1
        end += 1
    dest = text[pos:end]
    if not dest:
        return None
    return _finish_after_dest(text, end, dest)


def _finish_after_dest(text: str, pos: int, dest: str):
    n = len(text)
    while pos < n and text[pos] in " \t\n":
        pos += 1
    if pos < n and text[pos] in "\"'(":
        closer = {"(": ")"}.get(text[pos], text[pos])
        pos += 1
        while pos < n and not (text[pos] == closer and _unescaped(text, pos)):
            pos += 1
        pos += 1
        while pos < n and text[pos] in " \t\n":
            pos += 1
    if pos < n and text[pos] == ")":
        dest = re.sub(r"\\(.)", r"\1", dest)
        return dest, pos + 1
    return None


def classify_target(dest: str) -> str:
    """Classify a raw link destination: 'skip' (external URL / mailto /
    scheme-relative / not path-shaped), 'absolute' (machine-local absolute
    path incl. file: scheme and drive letters), or 'relative'."""
    if dest.startswith("//"):
        return "skip"  # protocol-relative URL, not a filesystem path
    lower = dest.lower()
    if lower.startswith("file:"):
        return "absolute"
    if "://" in dest or lower.startswith("mailto:"):
        return "skip"
    if dest.startswith("/") or re.match(r"[A-Za-z]:[/\\]", dest):
        return "absolute"
    stripped = dest.split("#", 1)[0].split("?", 1)[0]
    last = stripped.rstrip("/").rsplit("/", 1)[-1]
    if "/" not in stripped and "." not in last:
        return "skip"
    return "relative"


def strip_fragment_query(dest: str) -> str:
    return dest.split("#", 1)[0].split("?", 1)[0]


def scan_markdown_link_targets(text: str) -> list:
    """Extract inline-link destinations (raw, fragment/query intact) from
    markdown text, ignoring code spans/fences and escaped link openers."""
    masked = mask_code(text)
    targets = []
    bracket_stack = []
    i = 0
    n = len(masked)
    while i < n:
        ch = masked[i]
        if ch == "[" and _unescaped(masked, i):
            bracket_stack.append(i)
        elif ch == "]" and _unescaped(masked, i):
            opener = bracket_stack.pop() if bracket_stack else None
            if opener is not None and i + 1 < n and masked[i + 1] == "(":
                parsed = _parse_destination(masked, i + 2)
                if parsed:
                    targets.append(parsed[0])
                    i = parsed[1]
                    continue
        i += 1
    return targets



def _git_tracked_files() -> list:
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "ls-files", "-z"],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"git ls-files failed: {proc.stderr.strip()}")
    return sorted(p for p in proc.stdout.split("\0") if p)


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


def collect_ledger(tracked: list) -> dict:
    shard_paths = [p for p in tracked if p.startswith(LEDGER_PREFIX) and p.endswith(".json")]
    tracked_set = set(tracked)
    claim_ids = []
    histogram: Counter = Counter()
    missing_note_paths = 0
    parse_errors = []
    for shard in shard_paths:
        try:
            with open(os.path.join(REPO_ROOT, shard), "r", encoding="utf-8") as fh:
                row = json.load(fh)
        except (json.JSONDecodeError, OSError, UnicodeDecodeError) as exc:
            parse_errors.append(f"{shard}: {exc}")
            continue
        if not isinstance(row, dict):
            parse_errors.append(f"{shard}: shard is not a JSON object")
            continue
        claim_id = row.get("claim_id")
        if not isinstance(claim_id, str) or not claim_id:
            fallback = os.path.splitext(os.path.basename(shard))[0]
            parse_errors.append(f"{shard}: missing/non-string claim_id (filename stem {fallback!r})")
            claim_id = fallback
        claim_ids.append(claim_id)
        status = row.get("effective_status")
        if status is None:
            histogram["MISSING"] += 1
        elif isinstance(status, str):
            histogram[status] += 1
        else:
            parse_errors.append(f"{shard}: non-string effective_status")
            histogram["SCHEMA_INVALID"] += 1
        note_path = row.get("note_path")
        if isinstance(note_path, str) and note_path and note_path not in tracked_set:
            missing_note_paths += 1
        elif note_path is not None and not isinstance(note_path, str):
            parse_errors.append(f"{shard}: non-string note_path")

    dupes = sorted(cid for cid, n in Counter(claim_ids).items() if n > 1)
    ids_sha = hashlib.sha256("\n".join(sorted(claim_ids)).encode()).hexdigest()
    retained_total = sum(
        count
        for status, count in histogram.items()
        if status in RETAINED_GRADE_EXACT or status.startswith(RETAINED_GRADE_PREFIXES)
    )
    return {
        "shard_count": len(shard_paths),
        "claim_ids_sha256": ids_sha,
        "duplicate_claim_ids": dupes,
        "effective_status_histogram": dict(sorted(histogram.items())),
        "retained_grade_total": retained_total,
        "rows_with_missing_note_path": missing_note_paths,
        "shard_parse_errors": sorted(parse_errors),
    }


def _load_ids(rel_path: str, container_keys: tuple, tracked_set: set) -> dict:
    if rel_path not in tracked_set:
        return {"ids": [], "file_sha256": None, "tracked": False}
    path = os.path.join(REPO_ROOT, rel_path)
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    entries = data
    if isinstance(data, dict):
        for key in container_keys:
            if isinstance(data.get(key), (dict, list)):
                entries = data[key]
                break
    if isinstance(entries, dict):
        ids = sorted(entries.keys())
    elif isinstance(entries, list):
        ids = sorted(str(entry.get("id", "?")) for entry in entries if isinstance(entry, dict))
    else:
        ids = []
    with open(path, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    return {"ids": ids, "file_sha256": digest, "tracked": True}


def collect_docs(tracked: list) -> dict:
    top_level = [
        p for p in tracked
        if p.startswith("docs/") and p.endswith(".md") and p.count("/") == 1
    ]
    basenames: Counter = Counter()
    for p in tracked:
        if p.startswith("docs/") and p.endswith(".md"):
            basenames[posixpath.basename(p)] += 1
    dupes = sorted(name for name, n in basenames.items() if n > 1)
    return {"md_count": len(top_level), "duplicate_basenames": dupes}


def _authority_surface_files(tracked: list) -> list:
    files = []
    for entry in AUTHORITY_SURFACES:
        if entry.endswith("/"):
            files.extend(
                p for p in tracked
                if p.startswith(entry) and p.endswith(".md") and p.count("/") == entry.count("/")
            )
        elif entry in set(tracked):
            files.append(entry)
    return sorted(set(files))


def collect_authority_links(tracked: list) -> dict:
    tracked_set = set(tracked)
    tracked_dirs = set()
    for p in tracked:
        d = posixpath.dirname(p)
        while d:
            tracked_dirs.add(d)
            d = posixpath.dirname(d)

    surface_files = _authority_surface_files(tracked)
    candidates = {}  # repo-relative target -> set of source files
    absolutes = {}  # machine-local absolute target -> set of source files
    for rel in surface_files:
        with open(os.path.join(REPO_ROOT, rel), "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for target in scan_markdown_link_targets(text):
            kind = classify_target(target)
            if kind == "skip":
                continue
            if kind == "absolute":
                # A machine-local absolute path (incl. file: scheme and drive
                # letters) can never resolve for another reader; report it and
                # never hand it to git check-ignore.
                absolutes.setdefault(target, set()).add(rel)
                continue
            cleaned = urllib.parse.unquote(strip_fragment_query(target))
            if not cleaned:
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(rel), cleaned))
            if resolved.startswith(".."):
                continue
            candidates.setdefault(resolved, set()).add(rel)

    ignored = _gitignored(sorted(candidates))
    violations = [
        {"target": target, "reason": "absolute-path", "sources": sorted(sources)}
        for target, sources in sorted(absolutes.items())
    ]
    for rel in sorted(candidates):
        is_dir_link = rel.rstrip("/") in tracked_dirs
        if rel in tracked_set or is_dir_link:
            continue
        if rel in ignored:
            reason = "gitignored"
        elif os.path.exists(os.path.join(REPO_ROOT, rel)):
            reason = "untracked"
        else:
            reason = "missing"
        violations.append(
            {"target": rel, "reason": reason, "sources": sorted(candidates[rel])}
        )
    return {"surfaces_scanned": len(surface_files), "violations": violations}


def build_snapshot() -> dict:
    tracked = _git_tracked_files()
    return {
        "invariants_version": 2,
        "ledger": collect_ledger(tracked),
        "premises": _load_ids(PREMISE_NODES, ("nodes",), set(tracked)),
        "obligations": _load_ids(OBLIGATIONS, ("nodes", "obligations"), set(tracked)),
        "docs": collect_docs(tracked),
        "authority_links": collect_authority_links(tracked),
    }


def _json_equal(a, b) -> bool:
    """JSON-aware equality: bool is never equal to a number."""
    if isinstance(a, bool) != isinstance(b, bool):
        return False
    return a == b


def _diff_json(a, b, path=()):
    """Yield (path_tuple, before, after) for every leaf difference. Missing
    keys are reported as the _MISSING sentinel, distinct from JSON null.
    Paths are tuples, so dotted JSON keys cannot collide with nesting."""
    if isinstance(a, dict) and isinstance(b, dict):
        for key in sorted(set(a) | set(b)):
            yield from _diff_json(
                a.get(key, _MISSING), b.get(key, _MISSING), path + (str(key),)
            )
        return
    if a is _MISSING and b is _MISSING:
        return
    if type(a) is type(b) and isinstance(a, (dict, list)) and _json_equal(a, b):
        return
    if not isinstance(a, (dict, list)) and not isinstance(b, (dict, list)):
        if a is not _MISSING and b is not _MISSING and _json_equal(a, b):
            return
    yield (path,
           "<absent>" if a is _MISSING else json.dumps(a, sort_keys=True),
           "<absent>" if b is _MISSING else json.dumps(b, sort_keys=True))


def run_diff(path_a: str, path_b: str, allow: set) -> int:
    with open(path_a, "r", encoding="utf-8") as fh:
        snap_a = json.load(fh)
    with open(path_b, "r", encoding="utf-8") as fh:
        snap_b = json.load(fh)
    allow_tuples = {tuple(item.split(".")) for item in allow}
    diffs = list(_diff_json(snap_a, snap_b))
    blocked = []
    for path, before, after in diffs:
        display = ".".join(path)
        allowed = any(path[: len(t)] == t for t in allow_tuples)
        marker = "ALLOWED" if allowed else "CHANGED"
        if not allowed:
            blocked.append(display)
        print(f"{marker}: {display}\n    before: {before}\n    after:  {after}")
    if not diffs:
        print("IDENTICAL: snapshots match on every measured invariant.")
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
        failures.append(f"ledger shard parse/schema errors: {ledger['shard_parse_errors']}")
    if ledger["duplicate_claim_ids"]:
        failures.append(f"duplicate claim ids: {ledger['duplicate_claim_ids']}")
    for family in ("premises", "obligations"):
        if not snapshot[family].get("tracked", False):
            failures.append(f"{family} registry file is not git-tracked")
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
        message = "authority-surface links to untracked targets:\n" + "\n".join(lines)
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
        if args.snapshot != "-":
            resolved = os.path.realpath(os.path.abspath(args.snapshot))
            requested = os.path.relpath(resolved, os.path.realpath(REPO_ROOT))
            requested = requested.replace(os.sep, "/")
            if not requested.startswith(".."):
                tracked_fold = {t.casefold() for t in _git_tracked_files()}
                if requested.casefold() in tracked_fold:
                    print(f"refusing to overwrite tracked repository path: {requested}")
                    return 2
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
