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
  premises.file_sha256 / premises.tracked      registry digest + tracked flag
  obligations.ids              open derivation-obligation ids
  obligations.file_sha256 / obligations.tracked  registry digest + tracked flag
  docs.md_count                tracked markdown files directly under docs/
  docs.duplicate_basenames     tracked basename collisions across docs/**
  authority_links.violations   markdown links on authority surfaces whose
                               target cannot resolve for a fresh clone or
                               GitHub reader; reasons: not-tracked (missing,
                               untracked, or gitignored alike — derived from
                               the tracked set only), absolute-path, and
                               outside-repository. Code spans and fenced code
                               blocks are masked before link extraction.
  authority_links.irregular_surfaces  authority files that are not regular
                               files (never dereferenced)

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
# MISSING_DERIVATION_PROMPTS.md is excluded: its generator
# (generate_conditional_prompts.py) runs in the audit workflow AFTER the
# pipeline, so the in-pipeline guard cannot see its healed state — gating on
# it is circular. The queue surfaces (AUDIT_QUEUE.md, AUDIT_DISPATCH_QUEUE.md)
# are regenerated at pipeline stages 9/11, before the stage-17 guard, so they
# ARE scanned: a queue renderer emitting a dead reader-facing link fails the
# pipeline loudly.
AUTHORITY_EXCLUDE = {
    "docs/audit/MISSING_DERIVATION_PROMPTS.md",
}
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

# The controlled effective-status enum is owned by audit_lint; reuse it so the
# two tools cannot drift (BUG-17).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_lint import ALLOWED_EFFECTIVE_STATUSES  # noqa: E402
from ledger_io import shard_path as _canonical_shard_path  # noqa: E402

_MISSING = object()


def _regular_file(rel_path: str) -> bool:
    """True iff the tracked path is an existing regular file (not a symlink
    or other non-regular object); measured inputs are never dereferenced
    through links (BUG-21)."""
    import stat as _stat
    try:
        mode = os.lstat(os.path.join(REPO_ROOT, rel_path)).st_mode
    except OSError:
        return False
    return _stat.S_ISREG(mode)


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
            # A backtick fence opener may not contain a backtick in its info
            # string (CommonMark 4.5); such a line is inline-code material.
            if m and not (m.group(1)[0] == "`" and "`" in line[m.end():]):
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

    # backtick-run code spans on the fence-masked text; a backslash-escaped
    # backtick is a literal, so it shortens (or removes) its run (BUG-11)
    runs = []
    for m in re.finditer(r"`+", masked):
        start, length = m.start(), len(m.group(0))
        if not _unescaped(masked, start):
            start, length = start + 1, length - 1
        if length > 0:
            runs.append((start, length))
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


def _skip_component_whitespace(text: str, pos: int) -> int:
    """Skip spaces/tabs and AT MOST one line ending (CommonMark permits a
    single line ending inside inline-link component whitespace; unbounded
    skipping would glue prose across paragraphs into false links)."""
    n = len(text)
    newlines = 0
    while pos < n:
        ch = text[pos]
        if ch in " \t":
            pos += 1
        elif ch == "\n" and newlines == 0:
            newlines += 1
            pos += 1
        else:
            break
    return pos


def _parse_destination(text: str, pos: int):
    """Parse a CommonMark inline-link destination starting just after '('.
    Returns (destination, index-after-closing-paren) or None."""
    n = len(text)
    pos = _skip_component_whitespace(text, pos)
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
    pos = _skip_component_whitespace(text, pos)
    if pos < n and text[pos] in "\"'(":
        closer = {"(": ")"}.get(text[pos], text[pos])
        pos += 1
        while pos < n and not (text[pos] == closer and _unescaped(text, pos)):
            pos += 1
        pos += 1
        pos = _skip_component_whitespace(text, pos)
    if pos < n and text[pos] == ")":
        # CommonMark backslash escapes apply to ASCII punctuation only; a
        # backslash before anything else (e.g. C:\Users) is literal (BUG-12).
        dest = re.sub(r"\\([!-/:-@\[-`{-~])", r"\1", dest)
        return dest, pos + 1
    return None


def classify_target(dest: str) -> str:
    """Classify a raw link destination: 'skip' (external URI, mailto,
    scheme-relative, or a prose artifact), 'absolute' (machine-local absolute
    path incl. file: scheme and drive letters), or 'relative'."""
    if dest.startswith("//"):
        return "skip"  # protocol-relative URL, not a filesystem path
    lower = dest.lower()
    if lower.startswith("file:"):
        return "absolute"
    if dest.startswith("/") or re.match(r"[A-Za-z]:[/\\]", dest):
        return "absolute"  # single-letter drive checked before URI schemes
    if re.match(r"[A-Za-z][A-Za-z0-9+.-]+:", dest):
        return "skip"  # any other URI scheme (https, mailto, doi, ...)
    stripped = dest.split("#", 1)[0].split("?", 1)[0]
    if not stripped:
        return "skip"  # pure fragment/query
    # Prose-artifact heuristic: repo paths (with or without an extension —
    # LICENSE is a valid reader path) do not contain commas; expressions like
    # "(h,h)" outside code spans do.
    if "," in stripped:
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



def _git_tracked_modes() -> dict:
    """Repo-relative path -> index mode string (e.g. '100644', '120000').
    Index modes are pure tracked state: worktree mutations cannot perturb
    them, and a fresh clone reproduces exactly these kinds (BUG-26)."""
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "ls-files", "-z", "-s"],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"git ls-files -s failed: {proc.stderr.strip()}")
    modes = {}
    for entry in proc.stdout.split("\0"):
        if not entry:
            continue
        meta, _tab, path = entry.partition("\t")
        modes[path] = meta.split(" ", 1)[0]
    return modes


def _git_tracked_files() -> list:
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "ls-files", "-z"],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"git ls-files failed: {proc.stderr.strip()}")
    return sorted(p for p in proc.stdout.split("\0") if p)



def collect_ledger(tracked: list) -> dict:
    shard_paths = [p for p in tracked if p.startswith(LEDGER_PREFIX) and p.endswith(".json")]
    tracked_set = set(tracked)
    claim_ids = []
    histogram: Counter = Counter()
    missing_note_paths = 0
    parse_errors = []
    for shard in shard_paths:
        if not _regular_file(shard):
            parse_errors.append(f"{shard}: not a regular file")
            continue
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
        stem = os.path.splitext(os.path.basename(shard))[0]
        if not isinstance(claim_id, str) or not claim_id:
            parse_errors.append(f"{shard}: missing/non-string claim_id (filename stem {stem!r})")
            claim_id = stem
        elif claim_id != stem:
            # Canonical shard identity (ledger_io): claim_id must match the
            # shard filename stem (BUG-17).
            parse_errors.append(f"{shard}: claim_id {claim_id!r} != filename stem {stem!r}")
        else:
            # Canonical placement (ledger_io.shard_path): shard-safe id at
            # exactly ledger/<id[:2]>/<id>.json — a moved or mis-fanned shard
            # is unreadable by the canonical loader (BUG-23).
            try:
                # ledger_io owns the shard-safe id rule and the fanout rule;
                # anchor its fanout under our tracked prefix so the check is
                # REPO_ROOT-independent.
                canonical = _canonical_shard_path(claim_id)
                canonical_rel = f"{LEDGER_PREFIX}{canonical.parent.name}/{canonical.name}"
                if shard != canonical_rel:
                    parse_errors.append(
                        f"{shard}: not at canonical shard path {canonical_rel}"
                    )
            except ValueError as exc:
                parse_errors.append(f"{shard}: {exc}")
        claim_ids.append(claim_id)
        status = row.get("effective_status")
        if status is None:
            # Measured AND rejected: None is outside the controlled set the
            # audit linter enforces (BUG-25).
            histogram["MISSING"] += 1
            parse_errors.append(f"{shard}: missing/null effective_status")
        elif isinstance(status, str) and (
            status in ALLOWED_EFFECTIVE_STATUSES or status.startswith("decoration_under_")
        ):
            histogram[status] += 1
        else:
            parse_errors.append(f"{shard}: effective_status {status!r} not in controlled set")
            histogram["SCHEMA_INVALID"] += 1
        note_path = row.get("note_path")
        if isinstance(note_path, str) and note_path:
            if note_path not in tracked_set:
                missing_note_paths += 1
        else:
            # absent, null, empty, or non-string: every form is recorded so a
            # note_path change can never leave the snapshot identical (BUG-20)
            parse_errors.append(f"{shard}: missing/empty/non-string note_path")

    dupes = sorted(cid for cid, n in Counter(claim_ids).items() if n > 1)
    ids_sha = hashlib.sha256(
        json.dumps(sorted(claim_ids), separators=(",", ":")).encode()
    ).hexdigest()
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
    if rel_path not in tracked_set or not _regular_file(rel_path):
        return {"ids": [], "file_sha256": None, "tracked": False}
    path = os.path.join(REPO_ROOT, rel_path)
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError, UnicodeDecodeError) as exc:
        # Fail closed with a structured diagnostic (registry unreadable is
        # treated exactly like registry untracked: run_check fails on it).
        return {"ids": [], "file_sha256": None, "tracked": False,
                "parse_error": f"{rel_path}: {exc}"}
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
    return sorted(set(files) - AUTHORITY_EXCLUDE)


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
    outsiders = {}  # ../-escaping target -> set of source files
    irregular = [rel for rel in surface_files if not _regular_file(rel)]
    surface_files = [rel for rel in surface_files if _regular_file(rel)]
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
            if resolved == ".." or resolved.startswith("../"):
                # Cannot resolve inside a fresh clone: report, never skip.
                outsiders.setdefault(target, set()).add(rel)
                continue
            candidates.setdefault(resolved, set()).add(rel)

    modes = _git_tracked_modes()
    violations = [
        {"target": target, "reason": "absolute-path", "sources": sorted(sources)}
        for target, sources in sorted(absolutes.items())
    ] + [
        {"target": target, "reason": "outside-repository", "sources": sorted(sources)}
        for target, sources in sorted(outsiders.items())
    ]
    for rel in sorted(candidates):
        is_dir_link = rel.rstrip("/") in tracked_dirs
        if rel in tracked_set:
            # A tracked target must also be a regular blob: a symlink or
            # submodule entry renders as a pathname/commit pointer for a
            # GitHub reader and dereferences nothing in a fresh clone
            # (BUG-26). Judged from index modes only.
            if modes.get(rel) not in ("100644", "100755"):
                violations.append({
                    "target": rel,
                    "reason": "irregular-target",
                    "sources": sorted(candidates[rel]),
                })
            continue
        if is_dir_link:
            # A directory target renders as a file listing, not an authority
            # document; every authority citation must dereference to one
            # reviewable tracked file (front-door campaign, 2026-07-17).
            violations.append({
                "target": rel,
                "reason": "directory-target",
                "sources": sorted(candidates[rel]),
            })
            continue
        # The single reason derives from the tracked set ONLY: local ignore
        # rules and untracked scratch files can never change the serialized
        # snapshot (BUG-16, NIT-05). A not-tracked target 404s for any fresh
        # clone or GitHub reader whether it is gitignored or merely absent.
        reason = "not-tracked"
        violations.append(
            {"target": rel, "reason": reason, "sources": sorted(candidates[rel])}
        )
    return {
        "surfaces_scanned": len(surface_files),
        "irregular_surfaces": sorted(irregular),
        "violations": violations,
    }


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
    if isinstance(a, list) and isinstance(b, list):
        for i in range(max(len(a), len(b))):
            yield from _diff_json(
                a[i] if i < len(a) else _MISSING,
                b[i] if i < len(b) else _MISSING,
                path + (str(i),),
            )
        return
    if a is _MISSING and b is _MISSING:
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


DOC_AUTHORITY_REGISTRY_REL = "docs/audit/data/doc_authority_registry.json"
CLASS_F_REQUIRED_PHRASES = (
    "no premise or interpretive weight",
    "citable for orientation and scope discipline only",
)
CITATION_GRAPH_CACHE = os.path.join(
    REPO_ROOT, "docs", "audit", "data", "citation_graph.json"
)
GRAPH_MANIFEST_REL = "docs/audit/data/citation_graph_manifest.json"


def class_f_violations_from(registry: dict, tracked_set: set, read_text) -> list:
    """Pure core of the class-F header check (callers supply IO).

    Class F = orientation memo with no premise or interpretive weight
    (DOCUMENT_AUTHORITY_AND_CITATION_POLICY, 'The Class F header formula').
    Judged on tracked files only; a registered path that is missing or
    untracked is itself a violation.
    """
    violations = []
    for row in registry.get("rows", []):
        if row.get("class") != "F":
            continue
        path = row.get("path")
        if not isinstance(path, str):
            violations.append({"path": repr(path), "problem": "class-F row has no path"})
            continue
        if path not in tracked_set:
            violations.append({"path": path, "problem": "registered class-F doc is not tracked"})
            continue
        try:
            text = read_text(path)
        except OSError as exc:
            violations.append({"path": path, "problem": f"unreadable: {exc}"})
            continue
        missing = [p for p in CLASS_F_REQUIRED_PHRASES if p not in text]
        if missing:
            violations.append({
                "path": path,
                "problem": "missing required class-F header phrase(s): "
                           + "; ".join(repr(m) for m in missing),
            })
    return violations


def collect_class_f_violations(tracked: list) -> list:
    registry_path = os.path.join(REPO_ROOT, DOC_AUTHORITY_REGISTRY_REL)
    try:
        with open(registry_path, "r", encoding="utf-8") as fh:
            registry = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        return [{"path": DOC_AUTHORITY_REGISTRY_REL, "problem": f"registry unreadable: {exc}"}]

    def read_text(path: str) -> str:
        with open(os.path.join(REPO_ROOT, path), "r", encoding="utf-8") as fh:
            return fh.read()

    return class_f_violations_from(registry, set(tracked), read_text)


def graph_manifest_delta(computed: dict, indexed: dict) -> dict | None:
    """Named delta between the computed manifest and the index-tracked one.

    Returns None when identical. Pure function; callers supply both sides.
    """
    if computed == indexed:
        return None
    comp_nodes = computed.get("nodes", {})
    idx_nodes = indexed.get("nodes", {})
    added = sorted(set(comp_nodes) - set(idx_nodes))
    removed = sorted(set(idx_nodes) - set(comp_nodes))
    changed = sorted(
        n for n in set(comp_nodes) & set(idx_nodes) if comp_nodes[n] != idx_nodes[n]
    )
    return {"added": added, "removed": removed, "changed": changed}


def collect_graph_manifest_check() -> dict | None:
    """Compare the in-pass citation graph against the index-tracked manifest.

    The tracked manifest is the acknowledgment surface: any change that adds,
    removes, or rewires graph nodes must ship the refreshed manifest, so the
    delta is visible in the diff instead of silently reshaping audit-lane
    criticality. Returns None (skip) when no in-pass graph cache exists —
    the check is only meaningful inside a pipeline run.
    """
    if not os.path.isfile(CITATION_GRAPH_CACHE):
        return None
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from write_citation_graph_manifest import compute_manifest
    with open(CITATION_GRAPH_CACHE, "r", encoding="utf-8") as fh:
        graph = json.load(fh)
    computed = compute_manifest(graph)
    proc = subprocess.run(
        ["git", "show", f":{GRAPH_MANIFEST_REL}"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if proc.returncode != 0:
        return {"missing_from_index": True, "delta": None}
    try:
        indexed = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"missing_from_index": False, "unparseable": True, "delta": None}
    return {"missing_from_index": False, "delta": graph_manifest_delta(computed, indexed)}


def _format_graph_delta(delta: dict) -> str:
    parts = []
    for key in ("added", "removed", "changed"):
        items = delta.get(key, [])
        if items:
            shown = ", ".join(items[:20]) + (" ..." if len(items) > 20 else "")
            parts.append(f"{len(items)} {key} ({shown})")
    return "; ".join(parts) or "content drift"


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
            detail = snapshot[family].get("parse_error") or "not git-tracked or not a regular file"
            failures.append(f"{family} registry unusable: {detail}")
    known_dupes = {"README.md", "SKILL.md"}
    unexpected = [
        name for name in snapshot["docs"]["duplicate_basenames"] if name not in known_dupes
    ]
    if unexpected:
        failures.append(f"unexpected duplicate doc basenames: {unexpected}")

    irregular = snapshot["authority_links"].get("irregular_surfaces", [])
    if irregular:
        failures.append(
            "authority surfaces are not regular files (unscannable, refusing "
            f"to certify): {irregular}"
        )
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

    class_f_violations = collect_class_f_violations(_git_tracked_files())
    if class_f_violations:
        lines = [f"  {item['path']}: {item['problem']}" for item in class_f_violations]
        message = "class-F registry/header violations:\n" + "\n".join(lines)
        (failures if enforce_links else warnings).append(message)

    graph_check = collect_graph_manifest_check()
    graph_delta_note = "skipped (no in-pass graph cache)"
    if graph_check is not None:
        remedy = (
            "acknowledge by refreshing and staging the manifest: "
            "python3 docs/audit/scripts/write_citation_graph_manifest.py "
            f"&& git add {GRAPH_MANIFEST_REL}"
        )
        if graph_check.get("missing_from_index"):
            message = f"citation-graph manifest missing from the index; {remedy}"
            (failures if enforce_links else warnings).append(message)
            graph_delta_note = "manifest-missing"
        elif graph_check.get("unparseable"):
            message = f"citation-graph manifest in the index is not valid JSON; {remedy}"
            (failures if enforce_links else warnings).append(message)
            graph_delta_note = "manifest-unparseable"
        elif graph_check.get("delta") is not None:
            message = (
                "citation-graph delta not acknowledged in the index: "
                + _format_graph_delta(graph_check["delta"])
                + f"; {remedy}"
            )
            (failures if enforce_links else warnings).append(message)
            graph_delta_note = "delta-unacknowledged"
        else:
            graph_delta_note = "acknowledged"

    for warning in warnings:
        print(f"WARN: {warning}")
    for failure in failures:
        print(f"FAIL: {failure}")
    summary = (
        f"rows={ledger['shard_count']} retained_grade={ledger['retained_grade_total']} "
        f"link_violations={len(link_violations)} "
        f"class_f_violations={len(class_f_violations)} "
        f"graph_delta={graph_delta_note} "
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
            # Snapshots are scratch artifacts: refuse ANY destination inside
            # the repository (kills every alias/traversal overwrite class:
            # symlinks, case folds, unicode normalization, ..-prefixed
            # basenames), and refuse multi-linked existing files anywhere (a
            # hard link outside the repo can alias a tracked inode).
            resolved = os.path.realpath(os.path.abspath(args.snapshot))
            repo_real = os.path.realpath(REPO_ROOT)
            inside = os.path.commonpath([resolved, repo_real]) == repo_real
            if not inside:
                # Spelling-insensitive filesystems (case folds, unicode
                # normalization) can alias the repository under a different
                # string; compare filesystem identity of every existing
                # ancestor against the repository root (BUG-22).
                repo_stat = os.stat(repo_real)
                probe = resolved
                while True:
                    if os.path.exists(probe):
                        try:
                            if os.path.samestat(os.stat(probe), repo_stat):
                                inside = True
                        except OSError:
                            pass
                    parent = os.path.dirname(probe)
                    if parent == probe:
                        break
                    probe = parent
            if inside:
                print("refusing to write a snapshot inside the repository; "
                      "use a scratch directory or '-' for stdout")
                return 2
            if os.path.exists(resolved) and os.stat(resolved).st_nlink > 1:
                print("refusing to overwrite a multi-linked file (possible "
                      "hard-link alias of a repository path)")
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
