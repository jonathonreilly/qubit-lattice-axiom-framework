#!/usr/bin/env python3
"""Read the landing-review depth of a unit from its delta.

Prints `DEPTH scope` when every changed path is working material, as
WORKING_MATERIAL lists it, and `DEPTH full` for any other delta. The rule is
`docs/ai_methodology/procedures/land.md` step 4. The two depths are defined in
`../references/SCIENCE_LENSES.md` under "Review depth". The table there must
equal WORKING_MATERIAL; `check_review_loop_skill_contract.py` compares them.

The script reads paths, change types and file modes. It reads no content and
judges no science. A reviewer or lander may raise its answer; nobody lowers
it. When the script fails it prints no `DEPTH` line, and the unit then gets
the full read.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from typing import NamedTuple

# (path, change that counts as working material). A path that ends in "/" is
# a folder and covers everything under it. "<name>" is one file name, so
# `docs/<name>.md` is a note directly under `docs/` and nothing deeper.
# "any" accepts every change; "added" accepts only a file the base lacks.
WORKING_MATERIAL = (
    (".claude/science/", "any"),
    ("research/", "any"),
    ("docs/<name>.md", "added"),
    ("scripts/<name>.py", "added"),
    ("logs/runner-cache/", "added"),
)
REGULAR_MODES = frozenset({"100644", "100755"})
LISTED_BY_DEFAULT = 40


class Change(NamedTuple):
    """One changed path: git's status letter, the path and the new file mode."""

    status: str
    path: str
    mode: str = "100644"


def _matches(pattern: str, path: str) -> bool:
    if "<name>" in pattern:
        head, tail = pattern.split("<name>")
        return re.fullmatch(re.escape(head) + r"[^/]+" + re.escape(tail), path) is not None
    return path.startswith(pattern)


def working_pattern(path: str) -> tuple[str, str] | None:
    """Return the WORKING_MATERIAL entry that covers a path, if one does."""
    for pattern, change in WORKING_MATERIAL:
        if _matches(pattern, path):
            return pattern, change
    return None


def full_read_reason(change: Change, base_paths: frozenset[str] = frozenset()) -> str | None:
    """Say why one change needs the full read, or return None for working material."""
    parts = change.path.split("/")
    if not change.path or change.path.startswith("/") or ".." in parts or "" in parts:
        return "not a plain repository path"
    entry = working_pattern(change.path)
    if entry is None:
        if change.status == "A":
            return "new file outside the working-material paths"
        return "changes a file outside the working-material paths"
    if change.status != "D" and change.mode not in REGULAR_MODES:
        return "not a regular file"
    if entry[1] == "any":
        return None
    if change.status != "A":
        return "changes or deletes a file that the base holds"
    if change.path in base_paths:
        return "the base branch now holds this path"
    return None


def classify(changes: list[Change], base_paths: frozenset[str] = frozenset()) -> dict:
    """Return the depth of a delta with the count and reason behind it."""
    if not changes:
        raise ValueError("the delta is empty: there is nothing to read")
    working: dict[str, int] = {pattern: 0 for pattern, _ in WORKING_MATERIAL}
    full: list[dict[str, str]] = []
    for change in sorted(set(changes), key=lambda item: (item.path, item.status)):
        reason = full_read_reason(change, base_paths)
        if reason is None:
            entry = working_pattern(change.path)
            assert entry is not None
            working[entry[0]] += 1
        else:
            full.append({"status": change.status, "path": change.path, "reason": reason})
    return {
        "depth": "full" if full else "scope",
        "paths": len(set(changes)),
        "working_material": {name: count for name, count in working.items() if count},
        "full_read": full,
    }


def _git(repo: str, *args: str) -> bytes:
    return subprocess.run(
        ["git", "-C", repo, *args], check=True, capture_output=True
    ).stdout


def _commit(repo: str, ref: str) -> str:
    return _git(
        repo, "rev-parse", "--verify", "--quiet", "--end-of-options", ref + "^{commit}"
    ).decode().strip()


def read_delta(repo: str, base_sha: str, head_sha: str) -> tuple[str, list[Change]]:
    """Read a head's delta from its merge base with the base, renames split."""
    merge_base = _git(repo, "merge-base", base_sha, head_sha).decode().strip()
    raw = _git(
        repo, "diff", "--raw", "--no-renames", "--no-abbrev", "-z", merge_base, head_sha
    )
    fields = raw.split(b"\0")
    changes: list[Change] = []
    for index in range(0, len(fields) - 1, 2):
        meta = fields[index].decode()
        path = fields[index + 1].decode("utf-8", errors="surrogateescape")
        if not meta.startswith(":"):
            raise ValueError(f"unexpected diff record: {meta!r}")
        _old_mode, new_mode, _old_sha, _new_sha, status = meta[1:].split(" ")
        changes.append(Change(status[0], path, new_mode))
    return merge_base, changes


def paths_on_base(repo: str, base_sha: str, paths: list[str]) -> frozenset[str]:
    """Return which of these paths the base tip already holds."""
    found: set[str] = set()
    for start in range(0, len(paths), 200):
        listed = _git(
            repo, "ls-tree", "-r", "-z", "--name-only", base_sha, "--",
            *paths[start:start + 200],
        )
        found.update(
            item.decode("utf-8", errors="surrogateescape")
            for item in listed.split(b"\0") if item
        )
    return frozenset(found)


def unit_depth(repo: str, base: str, heads: list[str]) -> dict:
    """Read the depth of a unit: one base and one or more constituent heads."""
    base_sha = _commit(repo, base)
    changes: list[Change] = []
    constituents = []
    for head in heads:
        head_sha = _commit(repo, head)
        merge_base, delta = read_delta(repo, base_sha, head_sha)
        changes.extend(delta)
        constituents.append(
            {"head": head, "sha": head_sha, "merge_base": merge_base, "paths": len(delta)}
        )
    # A path that the head adds may have reached the base after the head
    # branched. The merge base cannot show that, so ask the base tip.
    added = sorted({change.path for change in changes if change.status == "A"})
    result = classify(changes, paths_on_base(repo, base_sha, added))
    result.update({"base": base, "base_sha": base_sha, "heads": constituents})
    return result


def render(result: dict, list_all: bool = False) -> str:
    lines = [f"DEPTH {result['depth']}"]
    if "base_sha" in result:
        lines.append(f"base {result['base']} {result['base_sha']}")
        for item in result["heads"]:
            lines.append(
                f"head {item['head']} {item['sha']} merge-base {item['merge_base']} "
                f"paths {item['paths']}"
            )
    counts = ", ".join(f"{name} {count}" for name, count in result["working_material"].items())
    lines.append(f"working material: {counts or 'none'}")
    full = result["full_read"]
    if full:
        lines.append(f"full-read paths: {len(full)} of {result['paths']}")
        shown = full if list_all else full[:LISTED_BY_DEFAULT]
        lines.extend(f"  {item['status']} {item['path']}: {item['reason']}" for item in shown)
        if len(shown) < len(full):
            lines.append(f"  ... {len(full) - len(shown)} more; pass --all to list them")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("heads", nargs="+", help="head commit of each PR in the unit")
    parser.add_argument("--base", default="origin/main", help="base ref (default origin/main)")
    parser.add_argument("--repo", default=".", help="repository path (default: current directory)")
    parser.add_argument("--json", action="store_true", help="print the result as JSON")
    parser.add_argument("--all", action="store_true", help="list every full-read path")
    args = parser.parse_args(argv)
    try:
        result = unit_depth(args.repo, args.base, args.heads)
    except subprocess.CalledProcessError as error:
        detail = error.stderr.decode(errors="replace").strip() or "unknown ref or not a repository"
        print(f"review_depth: git failed: {detail}", file=sys.stderr)
        return 2
    except ValueError as error:
        print(f"review_depth: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2) if args.json else render(result, args.all))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
