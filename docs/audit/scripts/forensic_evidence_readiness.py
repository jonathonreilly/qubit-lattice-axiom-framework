#!/usr/bin/env python3
"""Deterministic preflight for evidence needed by a forensic audit seat.

This module never makes a scientific judgment.  It detects only mechanical
conditions that make the authenticated N1-N8 contract impossible to satisfy,
so they can be repaired before spending an independent model seat.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import no_go_discipline_gate


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import runner_cache  # noqa: E402


def live_manifest_readiness_issue(
    evidence_manifest: dict[str, dict],
) -> str | None:
    """Return a definite N5 evidence gap in an invocation-bound manifest."""
    required_statements = no_go_discipline_gate.required_phrase_groups(
        evidence_manifest,
        {"source"},
        no_go_discipline_gate.N5_SCAN_PHRASES,
    )
    if not required_statements:
        return None

    runner_text = "\n".join(
        str(entry.get("text") or "")
        for entry in evidence_manifest.values()
        if "runner_stdout" in set(entry.get("roles") or [])
    )
    missing: list[str] = []
    for resolution_class in sorted(no_go_discipline_gate.N5_RESOLUTION_CLASSES):
        marker = f"{resolution_class}:"
        found = False
        for line in runner_text.splitlines():
            normalized = re.sub(r"\s+", " ", line.strip().casefold())
            marker_index = normalized.find(marker)
            if marker_index >= 0 and len(normalized[marker_index:]) >= 40:
                found = True
                break
        if not found:
            missing.append(resolution_class)
    if not missing:
        return None
    return (
        "forensic_n5_execution_certificate_incomplete: current-cycle "
        "runner_stdout lacks substantive canonical resolution lines for "
        f"{','.join(missing)}"
    )


def _runner_source_issue(path: str, repo_root: Path) -> str | None:
    absolute = repo_root / path
    if not absolute.is_file():
        return f"runner_source_missing:{path}"
    declared = runner_cache.declared_input_paths(absolute)
    if declared == ():
        return f"runner_declared_inputs_invalid:{path}"
    for input_path in declared or ():
        if not (repo_root / input_path).is_file():
            return f"runner_declared_input_missing:{path}:{input_path}"
    return None


def cached_row_readiness_issue(
    row: dict,
    rows: dict[str, dict],
    repo_root: Path | None = None,
) -> str | None:
    """Return a deterministic pre-seat gap using the SHA/input-bound cache.

    Cached stdout is only a readiness signal.  The forensic runner still
    executes the current runner live and authenticates that output before
    apply.
    """
    root = REPO_ROOT if repo_root is None else repo_root
    note_path = str(row.get("note_path") or "")
    try:
        note_body = (root / note_path).read_text(encoding="utf-8")
    except OSError:
        return f"target_source_missing:{note_path or '<unset>'}"

    for path in [
        row.get("runner_path"),
        *(row.get("helper_runner_paths") or []),
    ]:
        if not isinstance(path, str) or not path:
            continue
        issue = _runner_source_issue(path, root)
        if issue is not None:
            return issue

    if not no_go_discipline_gate.source_requires_no_go_discipline(
        note_path,
        note_body,
        row.get("claim_type") or row.get("claim_type_author_hint"),
    ):
        return None

    manifest: dict[str, dict] = {}
    no_go_discipline_gate.set_packet_evidence(
        manifest,
        path=note_path,
        role="source",
        text=note_body,
    )
    required_statements = no_go_discipline_gate.required_phrase_groups(
        manifest,
        {"source"},
        no_go_discipline_gate.N5_SCAN_PHRASES,
    )
    if not required_statements:
        return None

    runner_path = row.get("runner_path")
    if not isinstance(runner_path, str) or not runner_path:
        return "forensic_n5_runner_missing"
    # runner_cache is rooted at the live repository.  Queue production uses
    # that root; tests or historical tools with another root conservatively
    # inspect source shape only and report that execution is required.
    if root.resolve() != REPO_ROOT.resolve():
        return "forensic_n5_current_execution_required"
    cached_stdout = runner_cache.cache_excerpt_for_audit(
        runner_path,
        tail_chars=200_000,
    )
    if cached_stdout is None:
        return f"forensic_runner_cache_not_fresh:{runner_path}"
    no_go_discipline_gate.set_packet_evidence(
        manifest,
        path=no_go_discipline_gate.runner_stdout_evidence_path(
            str(row.get("claim_id") or "")
        ),
        role="runner_stdout",
        text=cached_stdout,
    )
    return live_manifest_readiness_issue(manifest)
