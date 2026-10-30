#!/usr/bin/env python3
"""Fail when science replay depends on mutable process documents.

A runner that declares a live workflow file as an input, or a runner manifest
that hash-pins one, ties historical science to process text: an unrelated
process edit then stales or blocks the replay. Preserve the bytes in the input
package instead, as outputs/control_landing_2026_10_17/PROCESS_INPUT_SNAPSHOTS.json
does, and resolve the pinned path to that snapshot.

KNOWN_LIVE_INPUTS lists runners already declaring a process file when this check
was added. They only read it, so an edit stales their cache without failing them.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

PROCESS_PATH_RE = re.compile(
    r"^(docs/ai_methodology/(?!raw/)|\.claude/commands/|AGENTS\.md$|CLAUDE\.md$)"
)
DECLARED_RE = re.compile(r"^AUDIT_INPUT_PATHS\s*=", re.MULTILINE)
KNOWN_LIVE_INPUTS = frozenset({
    "scripts/frontier_admissibility_axis_separable_barycenter_selector_2026_08_14.py",
    "scripts/frontier_admissibility_finite_state_markov_completion_2026_08_14.py",
    "scripts/frontier_admissibility_six_neighbor_affine_cq_channel_classifier_2026_08_14.py",
    "scripts/frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.py",
    "scripts/frontier_record_native_marked_pure_birth_resource_generator_2026_08_14.py",
    "scripts/min_time_step_is_planck_time_from_scale_reference_primitive_runner.py",
})


def _tracked(repo_root: Path, *pathspecs: str) -> list[str]:
    return subprocess.run(
        ["git", "ls-files", "--", *pathspecs],
        cwd=repo_root, capture_output=True, text=True, check=True,
    ).stdout.split("\n")[:-1]


def declared_process_inputs(repo_root: Path) -> dict[str, list[str]]:
    """Runners whose declared input closure names a live process document."""
    import runner_cache

    found: dict[str, list[str]] = {}
    for rel in _tracked(repo_root, "scripts/*.py"):
        text = (repo_root / rel).read_text(encoding="utf-8", errors="replace")
        if not DECLARED_RE.search(text) or not re.search(r"ai_methodology|\.claude/commands|AGENTS\.md|CLAUDE\.md", text):
            continue
        declared = runner_cache.declared_input_paths(repo_root / rel) or ()
        process = sorted(path for path in declared if PROCESS_PATH_RE.match(path))
        if process:
            found[rel] = process
    return found


def _pinned_rows(document: object) -> list[dict]:
    rows: list[dict] = []
    stack = [document]
    while stack:
        item = stack.pop()
        if isinstance(item, dict):
            if isinstance(item.get("path"), str) and isinstance(item.get("sha256"), str):
                rows.append(item)
            stack.extend(item.values())
        elif isinstance(item, list):
            stack.extend(item)
    return rows


def _snapshots(repo_root: Path) -> dict[str, dict]:
    merged: dict[str, dict] = {}
    for rel in _tracked(repo_root, "outputs/**/PROCESS_INPUT_SNAPSHOTS.json"):
        merged.update(json.loads((repo_root / rel).read_text(encoding="utf-8"))["files"])
    return merged


def unresolved_manifest_pins(repo_root: Path) -> list[str]:
    """Runner-package pins of process documents with no matching preserved snapshot."""
    snapshots = _snapshots(repo_root)
    problems: list[str] = []
    packages = _tracked(
        repo_root, "outputs/*_inputs/ARTIFACT_MANIFEST.json", "outputs/*_inputs/INPUT_MAP.json"
    )
    for rel in packages:
        document = json.loads((repo_root / rel).read_text(encoding="utf-8"))
        for row in _pinned_rows(document):
            path = row["path"]
            if not PROCESS_PATH_RE.match(path):
                continue
            snapshot = snapshots.get(path)
            if snapshot is None:
                problems.append(f"{rel}: pins live {path}")
                continue
            preserved = repo_root / snapshot["original_snapshot"]
            digest = hashlib.sha256(preserved.read_bytes()).hexdigest() if preserved.is_file() else None
            if digest != row["sha256"]:
                problems.append(f"{rel}: snapshot of {path} does not match its pin")
    return problems


def main() -> int:
    argparse.ArgumentParser(description=__doc__.splitlines()[0]).parse_args()
    declared = declared_process_inputs(REPO_ROOT)
    problems = [
        f"{rel}: declares live {', '.join(paths)}"
        for rel, paths in sorted(declared.items())
        if rel not in KNOWN_LIVE_INPUTS
    ]
    problems += [
        f"{rel}: no longer declares a process file; remove it from KNOWN_LIVE_INPUTS"
        for rel in sorted(KNOWN_LIVE_INPUTS - set(declared))
    ]
    problems += unresolved_manifest_pins(REPO_ROOT)
    for problem in problems:
        print(f"FAIL: {problem}")
    print(f"check_runner_process_inputs: {'FAIL' if problems else 'OK'} "
          f"({len(declared)} known declarations)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
