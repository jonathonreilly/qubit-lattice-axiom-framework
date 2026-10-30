#!/usr/bin/env python3
"""Fail when science replay depends on mutable process documents.

A runner that declares a live workflow file as an input, or a runner manifest
that hash-pins one, ties historical science to process text: an unrelated
process edit then stales or blocks the replay. Preserve the bytes in the input
package instead, as outputs/control_landing_2026_10_17/PROCESS_INPUT_SNAPSHOTS.json
does, and resolve the pinned path to that snapshot.

KNOWN_LIVE_INPUTS preserves exact existing runner/input pairs, not permission
to add inputs. REVIEWED_REPLAY_PACKAGES binds the three reviewed routing
implementations to their own snapshot map. A snapshot elsewhere is no evidence
that a runner uses it. This checks declared inputs and the two standard package
filenames below; it is not an analysis of arbitrary Python file reads.
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
KNOWN_LIVE_INPUTS = {runner: ("docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md",)
                     for runner in (
    "scripts/frontier_admissibility_axis_separable_barycenter_selector_2026_08_14.py",
    "scripts/frontier_admissibility_finite_state_markov_completion_2026_08_14.py",
    "scripts/frontier_admissibility_six_neighbor_affine_cq_channel_classifier_2026_08_14.py",
    "scripts/frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.py",
    "scripts/frontier_record_native_marked_pure_birth_resource_generator_2026_08_14.py",
    "scripts/min_time_step_is_planck_time_from_scale_reference_primitive_runner.py",
)}

# These exact source revisions were reviewed for routing every manifest/input-
# map read through this snapshot map. Changed routing requires renewed review;
# neither the mapping's presence nor a declaration alone proves its use.
REVIEWED_REPLAY_PACKAGES = {
    f"outputs/{name}_2026_10_17_inputs": {
        "runner": f"scripts/{name}_2026_10_17.py",
        "runner_sha256": sha,
        "snapshots": "outputs/control_landing_2026_10_17/PROCESS_INPUT_SNAPSHOTS.json",
    }
    for name, sha in (
        ("emitter_coupling_family", "b71a2d8d82d5566627dedc804a2b765da76085727e66485453d3073c571f60d8"),
        ("real_control_autonomous_output", "b6ad1bee429187fe4f70750a1fc63ec313d8928054535b2f426bd355f070d4b6"),
        ("thermal_resonance_halt", "ebdd1e3bc925269472e867afcafabab7d0b606e8feb97baa2307253850809737"),
    )
}


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
        # Identifier-only shortcut preserves all declaration syntax and escaped
        # path literals; the actual declaration is still parsed by runner_cache.
        if "AUDIT_INPUT_PATHS" not in (repo_root / rel).read_text(encoding="utf-8", errors="replace"):
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


def unexpected_live_inputs(declared: dict[str, list[str]]) -> list[str]:
    problems = []
    for runner in sorted(set(declared) | set(KNOWN_LIVE_INPUTS)):
        actual = set(declared.get(runner, ()))
        known = set(KNOWN_LIVE_INPUTS.get(runner, ()))
        if actual - known:
            problems.append(f"{runner}: declares live {', '.join(sorted(actual - known))}")
        if known - actual:
            problems.append(f"{runner}: remove stale KNOWN_LIVE_INPUTS entries: {', '.join(sorted(known - actual))}")
    return problems


def unresolved_manifest_pins(repo_root: Path) -> list[str]:
    """Runner-package pins of process documents with no matching preserved snapshot."""
    problems: list[str] = []
    tracked_snapshots = set(_tracked(repo_root, "outputs/"))
    packages = _tracked(
        repo_root, "outputs/*_inputs/ARTIFACT_MANIFEST.json", "outputs/*_inputs/INPUT_MAP.json"
    )
    for rel in packages:
        document = json.loads((repo_root / rel).read_text(encoding="utf-8"))
        rows = [row for row in _pinned_rows(document) if PROCESS_PATH_RE.match(row['path'])]
        if not rows:
            continue
        contract = REVIEWED_REPLAY_PACKAGES.get(Path(rel).parent.as_posix())
        if contract is None:
            problems.append(f"{rel}: pins live process input without reviewed package routing")
            continue
        runner = repo_root / contract['runner']
        if not runner.is_file() or hashlib.sha256(runner.read_bytes()).hexdigest() != contract['runner_sha256']:
            problems.append(f"{rel}: reviewed routing source changed or missing")
            continue
        snapshot_map = repo_root / contract['snapshots']
        if not snapshot_map.is_file():
            problems.append(f"{rel}: snapshot map missing")
            continue
        snapshots = json.loads(snapshot_map.read_text(encoding='utf-8'))['files']
        for row in rows:
            path = row["path"]
            snapshot = snapshots.get(path)
            if snapshot is None:
                problems.append(f"{rel}: pins live {path}")
                continue
            target = snapshot["original_snapshot"]
            target_path = Path(target)
            if (target_path.is_absolute() or '..' in target_path.parts
                    or target_path.as_posix() != target or not target.startswith('outputs/')
                    or target not in tracked_snapshots):
                problems.append(f"{rel}: snapshot of {path} is not tracked package storage")
                continue
            preserved = repo_root / target
            if any((repo_root / Path(*target_path.parts[:i])).is_symlink()
                   for i in range(1, len(target_path.parts) + 1)):
                problems.append(f"{rel}: snapshot of {path} follows a symlink")
                continue
            digest = hashlib.sha256(preserved.read_bytes()).hexdigest() if preserved.is_file() else None
            if digest != row["sha256"]:
                problems.append(f"{rel}: snapshot of {path} does not match its pin")
    return problems


def main() -> int:
    argparse.ArgumentParser(description=__doc__.splitlines()[0]).parse_args()
    declared = declared_process_inputs(REPO_ROOT)
    problems = unexpected_live_inputs(declared)
    problems += unresolved_manifest_pins(REPO_ROOT)
    for problem in problems:
        print(f"FAIL: {problem}")
    print(f"check_runner_process_inputs: {'FAIL' if problems else 'OK'} "
          f"({len(declared)} known declarations)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
