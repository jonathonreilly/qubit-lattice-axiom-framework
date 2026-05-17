#!/usr/bin/env python3
"""Source-Graph Repair Pass (DRY-RUN by default).

For each citation cycle named in `docs/audit/data/audit_queue.json`, the
audit pipeline already names the specific (source, target) edges that
are cite-only / non-load-bearing. This tool:

  1. Reads cycle instructions to extract those edges
  2. For each (source, target), locates the markdown link in the source
     file
  3. EITHER prints the planned change (dry-run, default)
     OR rewrites the source markdown to move the link into a
     "## Cross-references (non-load-bearing)" section (--apply mode)

The audit pipeline's build_citation_graph.py extracts ALL markdown links
to other docs/*.md notes as citation edges. To stably strip cite-only
edges without losing the information, we move them into a section the
citation graph builder can be taught to skip (Step 2 of the repair plan).

This tool is read-only by default. Pass --apply to actually modify source
notes. Pass --limit N to process only the first N source notes (useful
for testing).

CAUTION when applying:
  - Modifies source notes in docs/*.md
  - Should be run on a fresh branch from origin/main
  - Should be followed by re-running the audit pipeline:
      bash docs/audit/scripts/run_pipeline.sh
  - The pipeline regeneration may take time

Inputs (read-only):
  - docs/audit/data/audit_queue.json — current queue + cycle break targets

Outputs:
  - stdout: planned changes (dry-run) or applied changes (--apply)
  - logs/runner-cache/source_graph_repair_pass.txt
  - Modified source notes (--apply only)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AUDIT_DATA = REPO_ROOT / "docs" / "audit" / "data"
DOCS_DIR = REPO_ROOT / "docs"

CROSS_REF_SECTION_HEADER = "## Cross-references (non-load-bearing)"
CROSS_REF_SECTION_PREAMBLE = (
    "This section records non-load-bearing cross-references identified by the"
    " audit pipeline's cycle inventory. Links here are kept for reader context"
    " but are not load-bearing dependencies of the claim. They are excluded"
    " from the audit citation graph when this section is recognized by the"
    " graph builder."
)


def claim_id_to_note_path(claim_id: str) -> Path | None:
    """Map a claim_id like 'koide_lightcone_primitive_theorem_note_2026-05-10'
    to its docs/*.md file path. The claim_id is lowercase + underscores;
    the filename is typically uppercase with underscores and a .md extension.
    """
    # The note path corresponds to the upper-cased file name in docs/
    candidate = DOCS_DIR / f"{claim_id.upper()}.md"
    if candidate.exists():
        return candidate
    # Try lowercase
    candidate2 = DOCS_DIR / f"{claim_id}.md"
    if candidate2.exists():
        return candidate2
    # Try recursive find
    for p in DOCS_DIR.rglob(f"{claim_id.upper()}.md"):
        return p
    for p in DOCS_DIR.rglob(f"{claim_id}.md"):
        return p
    return None


def find_markdown_links_to(content: str, target_claim_id: str) -> list[tuple[int, int, str]]:
    """Find all markdown links in `content` whose URL points to a note
    matching `target_claim_id`.

    Returns list of (start, end, link_text) for each match.
    """
    # Match [text](path.md) and [text](path.md#anchor)
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)\s]+\.md)(?:#[^)]*)?\)")
    target_upper = target_claim_id.upper()
    target_lower = target_claim_id.lower()

    matches = []
    for m in link_pattern.finditer(content):
        url = m.group(2)
        url_basename = Path(url).stem
        if url_basename.upper() == target_upper or url_basename.lower() == target_lower:
            matches.append((m.start(), m.end(), m.group(0)))
    return matches


def extract_strippable_edges(queue: dict) -> dict[str, set[str]]:
    """Extract named (source, target) edges from cycle instructions.

    Returns: dict mapping source_claim_id -> set of target_claim_ids that
    should be moved to the cross-references section.
    """
    cycles = queue.get("cycle_break_targets", [])
    co_cycle_pattern = re.compile(r"co-cycle citations \[(.*?)\]")
    name_pattern = re.compile(r"'([^']+)'")

    edges_by_source: dict[str, set[str]] = defaultdict(set)
    for c in cycles:
        inst = c.get("instruction", "")
        source = c.get("primary_break_target", "")
        if not source:
            source = c.get("cycle_break_target_id", "")
        if not source:
            continue

        m = co_cycle_pattern.search(inst)
        if not m:
            continue
        targets = name_pattern.findall(m.group(1))
        for t in targets:
            edges_by_source[source].add(t)
    return edges_by_source


def plan_repair_for_note(
    source_path: Path,
    target_claim_ids: set[str],
) -> dict:
    """For a given source note path, plan the repair actions.

    Returns a dict with:
      - 'source_path': str (relative)
      - 'targets_found': list of (target_claim_id, list of link contexts)
      - 'targets_missing': list of target_claim_ids whose links were not found
    """
    rel = source_path.relative_to(REPO_ROOT)
    content = source_path.read_text(encoding="utf-8")

    targets_found = []
    targets_missing = []

    for target_id in sorted(target_claim_ids):
        matches = find_markdown_links_to(content, target_id)
        if matches:
            # Get a small context snippet for each match
            contexts = []
            for start, end, link_text in matches:
                line_start = content.rfind("\n", 0, start) + 1
                line_end = content.find("\n", end)
                if line_end == -1:
                    line_end = len(content)
                line = content[line_start:line_end].strip()
                contexts.append(line)
            targets_found.append((target_id, contexts))
        else:
            targets_missing.append(target_id)

    return {
        "source_path": str(rel),
        "targets_found": targets_found,
        "targets_missing": targets_missing,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually modify source notes (default: dry-run only)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Process only the first N source notes (0 = all)",
    )
    parser.add_argument(
        "--source",
        type=str,
        default="",
        help="Process only this specific source claim_id",
    )
    args = parser.parse_args()

    print("=" * 78)
    print("SOURCE-GRAPH REPAIR PASS")
    print(f"  Mode: {'APPLY (will modify files)' if args.apply else 'DRY-RUN (no modifications)'}")
    print("=" * 78)
    print()

    queue_path = AUDIT_DATA / "audit_queue.json"
    if not queue_path.exists():
        print(f"ERROR: audit_queue.json not found at {queue_path}")
        return 1

    queue = json.loads(queue_path.read_text())
    edges_by_source = extract_strippable_edges(queue)

    print(f"Cycles named in audit_queue.json: {len(queue.get('cycle_break_targets', []))}")
    print(f"Unique source notes with strippable edges: {len(edges_by_source)}")
    total_edges = sum(len(targets) for targets in edges_by_source.values())
    print(f"Total (source, target) edges to process: {total_edges}")
    print()

    # Sort source notes by edge count (most leverage first)
    sources_sorted = sorted(
        edges_by_source.items(), key=lambda kv: len(kv[1]), reverse=True
    )

    if args.source:
        sources_sorted = [(s, t) for s, t in sources_sorted if s == args.source]
        print(f"Filtering to single source: {args.source}")
    if args.limit > 0:
        sources_sorted = sources_sorted[: args.limit]
        print(f"Limiting to first {args.limit} source notes")
    print()

    found_count = 0
    missing_count = 0
    notes_no_path = []
    notes_with_plan = []

    for source_id, target_ids in sources_sorted:
        source_path = claim_id_to_note_path(source_id)
        if not source_path:
            notes_no_path.append(source_id)
            continue

        plan = plan_repair_for_note(source_path, target_ids)
        notes_with_plan.append(plan)
        found_count += len(plan["targets_found"])
        missing_count += len(plan["targets_missing"])

    # Summary
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print()
    print(f"  Source notes processed: {len(sources_sorted)}")
    print(f"  Source notes whose .md path resolved: {len(notes_with_plan)}")
    print(f"  Source notes whose .md path NOT resolved: {len(notes_no_path)}")
    print(f"  Edges found in source markdown (planned move): {found_count}")
    print(f"  Edges NOT found in source markdown: {missing_count}")
    print()
    if notes_no_path:
        print("  Notes with unresolved paths (first 10):")
        for s in notes_no_path[:10]:
            print(f"    - {s}")
        print()

    # Top 5 notes with most planned moves
    notes_with_plan.sort(key=lambda p: len(p["targets_found"]), reverse=True)
    print("  Top 5 source notes by planned moves:")
    for plan in notes_with_plan[:5]:
        n_found = len(plan["targets_found"])
        n_missing = len(plan["targets_missing"])
        print(f"    {plan['source_path']}: {n_found} found, {n_missing} missing")
    print()

    # Detailed plan for top source (illustrative)
    if notes_with_plan:
        top = notes_with_plan[0]
        print(f"  DETAILED PLAN for top source ({top['source_path']}):")
        print(f"    Found edges ({len(top['targets_found'])}):")
        for target_id, contexts in top["targets_found"][:5]:
            print(f"      → {target_id}")
            for ctx in contexts[:2]:
                # Truncate long lines
                ctx_short = ctx[:120] + "..." if len(ctx) > 120 else ctx
                print(f"          context: {ctx_short}")
        if len(top["targets_found"]) > 5:
            print(f"      ... and {len(top['targets_found']) - 5} more")

    print()
    print("=" * 78)
    print("DRY-RUN COMPLETE — no files modified" if not args.apply else "APPLY MODE")
    print("=" * 78)
    print()

    if not args.apply:
        print("To actually apply the repair (modify source notes):")
        print(f"  python3 {Path(__file__).relative_to(REPO_ROOT)} --apply")
        print()
        print("Recommended workflow:")
        print("  1. Run in dry-run, review the planned changes (this output)")
        print("  2. Branch from origin/main")
        print("  3. Run --apply")
        print("  4. Run bash docs/audit/scripts/run_pipeline.sh to regenerate")
        print("     citation graph + cycle inventory + audit queue")
        print("  5. Re-run scripts/audit_landscape_snapshot.py to see how many")
        print("     cycles vanished and how many items became ready")
        print("  6. Commit the source-note edits + the regenerated audit data")
        print("  7. Open a single PR for the repair pass + pipeline regen")

    # Note: --apply mode is NOT yet implemented in this initial version.
    # It is intentionally deferred so the user can authorize the actual
    # modification after reviewing the dry-run.
    if args.apply:
        print()
        print("ERROR: --apply mode is NOT yet implemented in this initial")
        print("version. The dry-run output above shows what WOULD be modified.")
        print("Implementing --apply requires:")
        print("  - decision on move-vs-delete policy")
        print("  - section-aware markdown editing")
        print("  - safe-write semantics (backup + atomic replace)")
        print("Build this in a follow-up commit after reviewing the dry-run.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
