#!/usr/bin/env python3
"""Repair concrete missing dependency edges named by conditional audits.

This script is intentionally mechanical. It reads audit ledger metadata only:
claim ids, note paths, direct deps, audit status, and open_dependency_paths.
It does not inspect prior verdict rationales or decide any audit verdict.

When an audited_conditional row names an existing docs/*.md note in
open_dependency_paths, but that note is not a direct dependency, the script can
append an explicit markdown link to the source note. The normal audit pipeline
then picks up the new edge, changes the source note hash, and resets that row
for fresh re-audit.

Two guards stop the script from fighting deliberate human cycle-breaks (an
auditor names what is missing from the chain; it does not know the graph
direction, so the wiring step must resolve it):
  (a) backtick guard — if the target note's filename already appears as a
      backticked plain-text reference in the source note, no live link is
      added. Authors backtick a downstream note's filename to record a
      sideways/back pointer without creating a load-bearing citation edge,
      usually to keep the graph acyclic. A backtick is not an edge to the
      graph builder, so a fresh markdown link would silently override that
      decision and recreate the cycle.
  (b) cycle guard — if adding the source->target edge would close a directed
      cycle in the citation graph, the edge is skipped (reusing
      build_cycle_inventory.detect_cycles, the audit lane's canonical cycle
      walk).
Both guards err toward NOT writing an edge: a missed auto-wire is recoverable
(a human can add it), but a re-created cycle causes nightly bot churn.
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

import ledger_io
from build_cycle_inventory import detect_cycles

REPO_ROOT = Path(__file__).resolve().parents[3]
LEDGER_PATH = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
GRAPH_PATH = REPO_ROOT / "docs" / "audit" / "data" / "citation_graph.json"
MARKER = "## Audit dependency repair links"
# Inline-code spans (`like_this.md`) are NOT citation edges: the graph builder's
# link regex only matches [text](path) links. Authors backtick a note's filename
# to record a sideways/back pointer without creating a load-bearing edge.
BACKTICK_SPAN_RE = re.compile(r"`([^`\n]+)`")
INTRO = (
    "This graph-bookkeeping section records explicit dependency links named by "
    "a prior conditional audit so the audit citation graph can track them. It "
    "does not promote this note or change the audited claim scope."
)


def is_repairable_note_path(path: str) -> bool:
    return (
        path.startswith("docs/")
        and not path.startswith("docs/audit/")
        and not path.startswith("docs/ai_methodology/")
        and (REPO_ROOT / path).exists()
    )


def load_rows() -> dict[str, dict]:
    ledger_io.ensure_cache()
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    return ledger.get("rows", {})


def build_resolvers(
    rows: dict[str, dict],
) -> tuple[dict[str, str], dict[str, list[str]], dict[str, list[str]]]:
    """Return (note_path_to_id, note_stem_to_ids, runner_path_to_ids).

    The third map lets us resolve script paths (e.g. scripts/X.py) cited in
    open_dependency_paths back to the docs/*.md row whose runner_path is
    that script. The audit citation graph operates on docs notes, so the
    correct repair edge is the owning docs note of the missing runner
    script.
    """
    path_to_id: dict[str, str] = {}
    stem_to_ids: dict[str, list[str]] = collections.defaultdict(list)
    runner_to_ids: dict[str, list[str]] = collections.defaultdict(list)
    for cid, row in rows.items():
        note_path = row.get("note_path") or ""
        if not is_repairable_note_path(note_path):
            continue
        path_to_id[note_path.lower()] = cid
        stem_to_ids[PurePosixPath(note_path).stem.lower()].append(cid)
        runner_path = (row.get("runner_path") or "").strip()
        if runner_path:
            runner_to_ids[runner_path.lower()].append(cid)
    return path_to_id, stem_to_ids, runner_to_ids


def resolve_open_dependency_path(
    raw_path: object,
    rows: dict[str, dict],
    path_to_id: dict[str, str],
    stem_to_ids: dict[str, list[str]],
    runner_to_ids: dict[str, list[str]],
) -> str | None:
    raw = str(raw_path).strip()
    if not raw:
        return None
    raw = raw.replace("_not_registered_one_hop", "")
    if " -> " in raw:
        raw = raw.split(" -> ", 1)[0]
    raw_low = raw.lower()

    # Case 1: direct docs/*.md path
    if raw_low.endswith(".md"):
        cid = path_to_id.get(raw_low)
        if cid is None:
            matches = stem_to_ids.get(PurePosixPath(raw).stem.lower(), [])
            if len(matches) != 1:
                return None
            cid = matches[0]
        if not is_repairable_note_path(rows[cid].get("note_path") or ""):
            return None
        return cid

    # Case 2: scripts/*.py path — resolve via runner_path of an existing row
    if raw_low.endswith(".py"):
        normalized = raw_low if raw_low.startswith("scripts/") else f"scripts/{raw_low}"
        matches = runner_to_ids.get(normalized) or runner_to_ids.get(raw_low)
        if not matches or len(matches) != 1:
            return None
        cid = matches[0]
        if not is_repairable_note_path(rows[cid].get("note_path") or ""):
            return None
        return cid

    return None


def candidate_repairs(rows: dict[str, dict]) -> dict[str, list[str]]:
    path_to_id, stem_to_ids, runner_to_ids = build_resolvers(rows)
    repairs: dict[str, list[str]] = {}
    for cid, row in rows.items():
        if row.get("audit_status") != "audited_conditional":
            continue
        if not is_repairable_note_path(row.get("note_path") or ""):
            continue

        direct_deps = set(row.get("deps") or [])
        targets: list[str] = []
        for open_path in row.get("open_dependency_paths") or []:
            target = resolve_open_dependency_path(
                open_path, rows, path_to_id, stem_to_ids, runner_to_ids
            )
            if target and target != cid and target not in direct_deps and target not in targets:
                targets.append(target)
        if targets:
            repairs[cid] = targets
    return repairs


def bullet_for(source_path: Path, target_id: str, target_path: Path) -> str:
    rel = os.path.relpath(target_path, source_path.parent).replace(os.sep, "/")
    return f"- [{target_id}]({rel})"


def load_graph_adjacency() -> dict[str, list[str]]:
    """Return {claim_id: [dep_id, ...]} from the citation graph.

    This is the same dependency structure build_cycle_inventory.detect_cycles
    consumes. The graph records live markdown-link edges only (a backticked
    filename is not an edge), and the pipeline that runs after this script
    rebuilds it, so it is exactly the pre-repair edge set the new edges would be
    added on top of. Returns {} if the graph is absent — the cycle guard then
    no-ops while the backtick guard still applies.
    """
    if not GRAPH_PATH.exists():
        return {}
    graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    return {
        cid: list(node.get("deps") or [])
        for cid, node in graph.get("nodes", {}).items()
    }


def has_backticked_reference(text: str, target_path: Path) -> bool:
    """True if the target note's filename appears inside an inline-code span.

    Authors backtick a filename to record a sideways/back pointer without
    creating a live citation edge (the convention that breaks length-2 cycles).
    Matching on the basename catches every backticked form — bare name,
    relative path, or repo-relative path — because the basename is a substring
    of each, and these dated note filenames do not collide as substrings.
    """
    basename = target_path.name
    return any(basename in span for span in BACKTICK_SPAN_RE.findall(text))


def _canonical_cycle(cycle: list[str]) -> tuple[str, ...]:
    """Rotate a cycle to start at its smallest node id, so the same directed
    cycle has one representation regardless of where the DFS entered it."""
    if not cycle:
        return ()
    pivot = min(range(len(cycle)), key=cycle.__getitem__)
    return tuple(cycle[pivot:] + cycle[:pivot])


def _canonical_cycles(adjacency: dict[str, list[str]]) -> set[tuple[str, ...]]:
    nodes = {cid: {"deps": deps} for cid, deps in adjacency.items()}
    return {_canonical_cycle(cycle) for cycle in detect_cycles(nodes)}


def edge_would_close_cycle(
    adjacency: dict[str, list[str]], source_id: str, target_id: str
) -> bool:
    """True if adding source_id -> target_id introduces a new directed cycle.

    Reuses build_cycle_inventory.detect_cycles and compares the canonical cycle
    set before and after the tentative edge. A genuinely new cycle always shows
    up as a new canonical entry, so there are no false negatives; a false
    positive merely skips one auto-wire, which is the safe direction. Nodes
    unknown to the graph cannot lie on an existing path, so an edge touching one
    is correctly judged cycle-free.
    """
    existing = adjacency.get(source_id, [])
    if target_id in existing:
        return False
    before = _canonical_cycles(adjacency)
    trial = dict(adjacency)
    trial[source_id] = existing + [target_id]
    return bool(_canonical_cycles(trial) - before)


def apply_repairs(
    rows: dict[str, dict],
    repairs: dict[str, list[str]],
    apply: bool,
    adjacency: dict[str, list[str]] | None = None,
) -> dict[str, int]:
    if adjacency is None:
        adjacency = load_graph_adjacency()
    changed_files = 0
    added_edges = 0
    skipped_backticked = 0
    skipped_cycle = 0
    for source_id, targets in sorted(repairs.items()):
        source_path = REPO_ROOT / rows[source_id]["note_path"]
        text = source_path.read_text(encoding="utf-8")
        bullets: list[str] = []
        for target_id in targets:
            target_path = REPO_ROOT / rows[target_id]["note_path"]
            bullet = bullet_for(source_path, target_id, target_path)
            link_fragment = bullet.rsplit("](", 1)[1].rstrip(")")
            # Already wired as a live markdown link: nothing to do.
            if bullet in text or f"]({link_fragment})" in text:
                continue
            # Guard (a): respect a deliberately-backticked sideways/back pointer.
            if has_backticked_reference(text, target_path):
                skipped_backticked += 1
                continue
            # Guard (b): never auto-wire an edge that closes a citation cycle.
            if edge_would_close_cycle(adjacency, source_id, target_id):
                skipped_cycle += 1
                continue
            bullets.append(bullet)
            # Reflect the accepted edge so later candidates this run see it.
            adjacency.setdefault(source_id, []).append(target_id)
        if not bullets:
            continue

        changed_files += 1
        added_edges += len(bullets)
        if not apply:
            continue

        addition = "\n".join(bullets) + "\n"
        if MARKER in text:
            next_text = text.rstrip() + "\n" + addition
        else:
            next_text = text.rstrip() + f"\n\n{MARKER}\n\n{INTRO}\n\n{addition}"
        source_path.write_text(next_text, encoding="utf-8")
    return {
        "changed_files": changed_files,
        "dependency_edges": added_edges,
        "skipped_backticked": skipped_backticked,
        "skipped_cycle": skipped_cycle,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write repair links; without this flag, only report candidates",
    )
    args = parser.parse_args()

    if not GRAPH_PATH.exists():
        subprocess.run(
            [sys.executable, str(Path(__file__).with_name("build_citation_graph.py"))],
            cwd=REPO_ROOT,
            check=True,
        )
    rows = load_rows()
    repairs = candidate_repairs(rows)
    stats = apply_repairs(rows, repairs, args.apply)
    mode = "applied" if args.apply else "dry_run"
    print(f"repair_missing_dependency_edges: {mode}")
    print(f"  candidate_rows: {len(repairs)}")
    print(f"  changed_files: {stats['changed_files']}")
    print(f"  dependency_edges: {stats['dependency_edges']}")
    print(f"  skipped_backticked_reference: {stats['skipped_backticked']}")
    print(f"  skipped_cycle_would_close: {stats['skipped_cycle']}")
    if args.apply:
        print("  next: bash docs/audit/scripts/run_pipeline.sh")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
