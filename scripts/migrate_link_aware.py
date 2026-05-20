#!/usr/bin/env python3
"""Link-aware filename migration for the Cleanup-2 sweep.

For each filename matching a forbidden-suffix rewrite rule in
docs/repo/controlled_vocabulary.yaml (rules with
`requires_link_aware_rewrite: true`), this script:

  1. Computes the target filename by applying the rewrite pattern.
  2. Finds every cross-doc reference to the old filename across the
     repo (markdown links, backticked names, bare paths, code
     literals).
  3. Renames the file with `git mv` (preserving git history).
  4. Rewrites every reference to point at the new filename.
  5. Stages all changes for a single atomic commit per migrated file.

Usage:
  scripts/migrate_link_aware.py --dry-run       # report what would change
  scripts/migrate_link_aware.py --apply         # do the rewrites
  scripts/migrate_link_aware.py --apply --commit-per-cluster
                                                # commit each cluster separately

Excluded paths (per YAML) and binary files are skipped automatically.

Exit codes:
  0  success / dry-run clean
  1  no migrations needed
  2  YAML / IO / collision error
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
YAML_PATH = REPO_ROOT / "docs" / "repo" / "controlled_vocabulary.yaml"
SOURCE_PATH_ALIASES_PATH = REPO_ROOT / "docs" / "audit" / "data" / "source_path_aliases.json"

# File extensions that can contain references to the renamed files.
# Anything else (binaries, audio, images, etc.) is skipped.
TEXT_EXTENSIONS = {".md", ".yaml", ".yml", ".json", ".py", ".txt", ".sh"}

# Paths to skip even for text files (archives, work_history, generated
# audit data dumps).
SKIP_PATH_PREFIXES = (
    "docs/work_history/",
    "archive_unlanded/",
    ".git/",
    ".claude/",
    "logs/",
)


def load_yaml() -> dict:
    if not YAML_PATH.exists():
        print(f"FAIL: {YAML_PATH} missing", file=sys.stderr)
        raise SystemExit(2)
    return yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))


def gather_link_aware_rules(yaml_data: dict) -> list[dict]:
    """Filter rewrite_rules to those flagged as link-aware filename renames."""
    out = []
    for rule in yaml_data.get("rewrite_rules") or []:
        if rule.get("requires_link_aware_rewrite"):
            out.append(rule)
    return out


def gather_all_text_files() -> list[Path]:
    out: list[Path] = []
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix not in TEXT_EXTENSIONS:
            continue
        rel = str(path.relative_to(REPO_ROOT))
        if any(rel.startswith(skip) for skip in SKIP_PATH_PREFIXES):
            continue
        out.append(path)
    return out


def compute_rename_plan(rules: list[dict]) -> list[tuple[Path, Path, str]]:
    """For each forbidden-suffix rule, find all matching filenames and
    compute (old_path, new_path, rule_id) tuples."""
    plan: list[tuple[Path, Path, str]] = []
    seen_targets: dict[str, Path] = {}  # for collision detection

    for path in REPO_ROOT.rglob("*.md"):
        if not path.is_file():
            continue
        rel = str(path.relative_to(REPO_ROOT))
        if any(rel.startswith(skip) for skip in SKIP_PATH_PREFIXES):
            continue
        for rule in rules:
            pattern = rule.get("pattern")
            replacement = rule.get("replacement")
            if not pattern or not replacement:
                continue
            # Translate $N → \N for re.sub.
            py_replacement = re.sub(r"\$(\d+)", r"\\\1", replacement)
            filename = path.name
            new_name = re.sub(pattern, py_replacement, filename)
            if new_name == filename:
                continue
            new_path = path.parent / new_name
            target_key = str(new_path)
            if target_key in seen_targets and seen_targets[target_key] != path:
                # Collision: two files rename to the same target.
                print(
                    f"FAIL: rename collision — {path.relative_to(REPO_ROOT)} and "
                    f"{seen_targets[target_key].relative_to(REPO_ROOT)} both target "
                    f"{new_path.relative_to(REPO_ROOT)}",
                    file=sys.stderr,
                )
                raise SystemExit(2)
            if new_path.exists() and new_path != path:
                print(
                    f"FAIL: target {new_path.relative_to(REPO_ROOT)} already exists "
                    f"(would clobber when renaming {path.relative_to(REPO_ROOT)})",
                    file=sys.stderr,
                )
                raise SystemExit(2)
            seen_targets[target_key] = path
            plan.append((path, new_path, rule.get("id", "<anonymous>")))
            break  # one rule per file
    return plan


def find_references(filename: str, text_files: list[Path]) -> dict[Path, list[int]]:
    """For each text file, find line numbers containing the filename."""
    refs: dict[Path, list[int]] = {}
    for f in text_files:
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if filename not in text:
            continue
        line_nums = []
        for i, line in enumerate(text.splitlines(), start=1):
            if filename in line:
                line_nums.append(i)
        if line_nums:
            refs[f] = line_nums
    return refs


def rewrite_references(old_filename: str, new_filename: str, files: Iterable[Path]) -> int:
    """Replace old_filename → new_filename in each given file. Returns the number
    of files actually modified."""
    modified = 0
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if old_filename not in text:
            continue
        new_text = text.replace(old_filename, new_filename)
        if new_text != text:
            f.write_text(new_text, encoding="utf-8")
            modified += 1
    return modified


def run_git(args: list[str], capture: bool = False) -> str:
    """Run a git command from the repo root. Returns stdout when capture=True."""
    result = subprocess.run(
        ["git"] + args,
        cwd=REPO_ROOT,
        check=True,
        text=True,
        capture_output=capture,
    )
    return result.stdout if capture else ""


def update_source_path_aliases(alias_updates: dict[str, str]) -> None:
    """Persist non-semantic source-path migrations for audit-row preservation."""
    if not alias_updates:
        return
    if SOURCE_PATH_ALIASES_PATH.exists():
        data = json.loads(SOURCE_PATH_ALIASES_PATH.read_text(encoding="utf-8"))
    else:
        data = {
            "schema_version": 1,
            "description": (
                "Non-semantic source-note path migrations used by "
                "seed_audit_ledger.py to preserve existing audit rows when "
                "claim ids change because a note was mechanically renamed."
            ),
            "aliases": {},
        }
    aliases = data.setdefault("aliases", {})
    aliases.update(alias_updates)
    data["aliases"] = dict(sorted(aliases.items()))
    SOURCE_PATH_ALIASES_PATH.parent.mkdir(parents=True, exist_ok=True)
    SOURCE_PATH_ALIASES_PATH.write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def apply_rename(old_path: Path, new_path: Path, text_files: list[Path]) -> dict:
    """Rename old_path → new_path and rewrite references. Returns a dict
    describing what changed."""
    old_filename = old_path.name
    new_filename = new_path.name

    # Find references BEFORE the rename so the old file still exists.
    refs = find_references(old_filename, text_files)

    # Rename via git so history is preserved.
    rel_old = str(old_path.relative_to(REPO_ROOT))
    rel_new = str(new_path.relative_to(REPO_ROOT))
    run_git(["mv", rel_old, rel_new])

    # Refresh the text-files list to point at the renamed file.
    refreshed_files = []
    for f in text_files:
        if f == old_path:
            refreshed_files.append(new_path)
        else:
            refreshed_files.append(f)

    # Rewrite references. Include the renamed file itself in case it
    # self-references (e.g. a "see X" comment naming its own filename).
    modified = rewrite_references(old_filename, new_filename, refreshed_files)

    return {
        "old": rel_old,
        "new": rel_new,
        "references_found": sum(len(v) for v in refs.values()),
        "files_with_references": len(refs),
        "files_rewritten": modified,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Link-aware filename migration for Cleanup-2. Applies "
            "requires_link_aware_rewrite: true rules from "
            "docs/repo/controlled_vocabulary.yaml."
        )
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report planned renames and reference counts without modifying anything.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply renames and rewrites. Stages everything for a single commit.",
    )
    parser.add_argument(
        "--commit-per-cluster",
        action="store_true",
        help="With --apply, create a separate commit per rule-id cluster.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional cap on number of renames in this run (debugging aid).",
    )
    args = parser.parse_args()

    if not args.dry_run and not args.apply:
        parser.error("specify --dry-run or --apply")

    yaml_data = load_yaml()
    rules = gather_link_aware_rules(yaml_data)
    if not rules:
        print("no link-aware rewrite rules in YAML; nothing to do")
        return 1

    plan = compute_rename_plan(rules)
    if args.limit is not None:
        plan = plan[: args.limit]

    if not plan:
        print("no files match link-aware rules; nothing to do")
        return 1

    text_files = gather_all_text_files()

    by_cluster: dict[str, list[tuple[Path, Path, str]]] = defaultdict(list)
    for old, new, rule_id in plan:
        by_cluster[rule_id].append((old, new, rule_id))

    print(f"link-aware migration plan: {len(plan)} files across {len(by_cluster)} rules")
    for rule_id, entries in by_cluster.items():
        print(f"  {rule_id}: {len(entries)} files")

    if args.dry_run:
        for old, new, rule_id in plan[:20]:
            rel_old = str(old.relative_to(REPO_ROOT))
            rel_new = str(new.relative_to(REPO_ROOT))
            print(f"  [{rule_id}] {rel_old} → {rel_new}")
        if len(plan) > 20:
            print(f"  ... and {len(plan) - 20} more")
        return 0

    # Apply.
    applied = 0
    cluster_summary: list[dict] = []
    alias_updates: dict[str, str] = {}
    for rule_id, entries in by_cluster.items():
        print(f"applying {rule_id}: {len(entries)} files")
        cluster_alias_updates: dict[str, str] = {}
        for old, new, _ in entries:
            result = apply_rename(old, new, text_files)
            cluster_alias_updates[result["old"]] = result["new"]
            applied += 1
            # Refresh the text_files list for subsequent operations.
            text_files = [new if p == old else p for p in text_files]
        cluster_summary.append({"rule_id": rule_id, "count": len(entries)})
        alias_updates.update(cluster_alias_updates)

        if args.commit_per_cluster:
            update_source_path_aliases(cluster_alias_updates)
            run_git(["add", "-A"])
            # Check there's something to commit.
            staged = run_git(["diff", "--cached", "--name-only"], capture=True).strip()
            if staged:
                message = f"cleanup-2: link-aware rewrite for rule {rule_id} ({len(entries)} files)"
                run_git(["commit", "-m", message])

    if not args.commit_per_cluster:
        update_source_path_aliases(alias_updates)
        run_git(["add", "-A"])

    print(f"applied {applied} renames")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
