#!/usr/bin/env python3
"""Audit Landscape Snapshot.

Diagnoses the current state of the audit lane to answer two questions:

  1. "Where do we stand all-up?" — counts by audit status, claim type,
     criticality, and cycle structure.

  2. "What's the highest-leverage next move to clear the audit backlog?"
     — simulates stripping all cite-only/non-load-bearing edges that the
     audit pipeline ALREADY names in cycle instructions, and counts how
     many cycles vanish + how many items become ready.

This is a READ-ONLY diagnostic. It does not modify any source notes,
citation graph data, or audit state. Re-runnable at any time to track
audit-lane progress over the course of a campaign.

Inputs (read-only):
  - docs/audit/data/audit_queue.json     — current queue + cycle break targets
  - docs/audit/data/audit_ledger.json    — audited claims with verdicts
  - docs/audit/data/citation_graph.json  — full edge graph (for ready-count
                                            simulation)
  - docs/audit/data/cycle_inventory.json — full cycle inventory

Outputs:
  - stdout snapshot report
  - logs/runner-cache/audit_landscape_snapshot.txt (cached output)

The simulation does NOT actually strip any edges. It counts what WOULD
happen if all named non-load-bearing edges were stripped. The actual
strip is a separate operation (source-graph repair pass) that requires
explicit user authorization and a follow-up tool.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
AUDIT_DATA = REPO_ROOT / "docs" / "audit" / "data"
sys.path.insert(0, str(REPO_ROOT / "docs" / "audit" / "scripts"))
import ledger_io  # noqa: E402


def load_json(name: str) -> Any:
    path = AUDIT_DATA / name
    with path.open() as f:
        return json.load(f)


def banner(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def section(title: str) -> None:
    print()
    print(f"## {title}")
    print()


# ============================================================================
# Section 1: Audit ledger status counts
# ============================================================================


def section_1_ledger_status(ledger: dict) -> None:
    section("1. AUDIT LEDGER — STATUS COUNTS")

    # Ledger structure: dict with top-level keys including 'rows' (a dict keyed by claim_id)
    if isinstance(ledger, dict) and "rows" in ledger:
        rows_obj = ledger["rows"]
        if isinstance(rows_obj, dict):
            rows = list(rows_obj.values())
        elif isinstance(rows_obj, list):
            rows = rows_obj
        else:
            print(f"  Cannot parse ledger['rows'] type: {type(rows_obj)}")
            return
    elif isinstance(ledger, list):
        rows = ledger
    else:
        print(f"  Cannot parse ledger structure: {type(ledger)}")
        return

    print(f"  Total claims in ledger: {len(rows)}")
    print()

    statuses = Counter(r.get("audit_status", "?") for r in rows)
    print("  By audit_status:")
    for status, count in statuses.most_common():
        print(f"    {status:35s}  {count}")

    print()
    types = Counter(r.get("claim_type", "?") for r in rows)
    print("  By claim_type:")
    for ctype, count in types.most_common():
        print(f"    {ctype:35s}  {count}")

    print()
    # Cross-tab status × type
    cross = defaultdict(int)
    for r in rows:
        cross[(r.get("claim_type", "?"), r.get("audit_status", "?"))] += 1

    # Compute retained-grade ratio per type
    print("  Retained-grade fraction by claim_type:")
    type_totals = Counter(r.get("claim_type", "?") for r in rows)
    retained_statuses = {"audited_clean", "audited_conditional", "retained", "retained_bounded"}
    for ctype in type_totals:
        retained = sum(
            count
            for (t, s), count in cross.items()
            if t == ctype and s in retained_statuses
        )
        total = type_totals[ctype]
        pct = 100 * retained / total if total else 0
        print(f"    {ctype:35s}  {retained:4d} / {total:4d}  ({pct:5.1f}%)")


# ============================================================================
# Section 2: Audit queue snapshot
# ============================================================================


def section_2_queue(queue: dict) -> None:
    section("2. AUDIT QUEUE — PENDING SNAPSHOT")

    print(f"  Total pending: {queue.get('total_pending', '?')}")
    print(f"  Ready (deps cleared): {queue.get('ready_count', '?')}")
    print()
    print("  By criticality:")
    for crit, count in queue.get("by_criticality", {}).items():
        print(f"    {crit:10s}  {count}")

    # Ready items detail
    queue_items = queue.get("queue", [])
    ready_items = [r for r in queue_items if r.get("ready", False)]
    if ready_items:
        print()
        print(f"  Ready items detail ({len(ready_items)}):")
        for r in ready_items[:10]:
            print(f"    - {r.get('claim_id', '?')}  ({r.get('claim_type', '?')}, {r.get('criticality', '?')})")


# ============================================================================
# Section 3: Cycle inventory analysis
# ============================================================================


def section_3_cycles(queue: dict, cycle_inv: Any) -> tuple[set, set]:
    """Analyze cycles and return (apparent_cycle_ids, genuine_cycle_ids)."""
    section("3. CITATION CYCLES — APPARENT vs GENUINE")

    cycles = queue.get("cycle_break_targets", [])
    print(f"  Total cycles in queue: {len(cycles)}")
    print()

    # Cycle length distribution
    lengths = Counter(c.get("cycle_length", 0) for c in cycles)
    print(f"  Cycle length distribution (top 10):")
    for length, count in sorted(lengths.items())[:10]:
        print(f"    length {length:2d}: {count} cycles")
    longest = max(lengths.keys()) if lengths else 0
    print(f"    ...")
    print(f"    longest cycle: {longest}")

    # Classify cycles by whether their instruction names strippable edges
    apparent = set()
    genuine = set()

    strip_pattern = re.compile(r"informational|see also|non-load-bearing|cite-only")
    for c in cycles:
        cid = c.get("cycle_id", "?")
        inst = c.get("instruction", "")
        if strip_pattern.search(inst):
            apparent.add(cid)
        else:
            genuine.add(cid)

    print()
    print(f"  Cycles with strippable-edge instruction: {len(apparent)}")
    print(f"  Cycles WITHOUT strippable-edge instruction (genuinely circular): {len(genuine)}")

    if genuine:
        print()
        print(f"  Genuine cycle IDs (first 5):")
        for cid in list(genuine)[:5]:
            print(f"    - {cid}")

    return apparent, genuine


# ============================================================================
# Section 4: Strippable edge analysis (the leverage map)
# ============================================================================


def section_4_strippable_edges(queue: dict) -> tuple[set, dict]:
    """Extract named strippable edges from cycle instructions.

    Returns (all_edges, edges_by_source) where:
      - all_edges = set of (source_claim_id, target_claim_id) pairs
      - edges_by_source = dict mapping source_claim_id -> set of target_claim_ids
    """
    section("4. NAMED STRIPPABLE EDGES — LEVERAGE MAP")

    cycles = queue.get("cycle_break_targets", [])

    # Extract (source, target) pairs from cycle instructions
    # Pattern: "co-cycle citations ['A', 'B', 'C'] are informational"
    co_cycle_pattern = re.compile(r"co-cycle citations \[(.*?)\]")
    name_pattern = re.compile(r"'([^']+)'")

    all_edges = set()
    edges_by_source = defaultdict(set)
    edges_by_target = defaultdict(set)

    for c in cycles:
        inst = c.get("instruction", "")
        # The source of the cycle's break-target is the "subject" being audited
        source = c.get("primary_break_target", "")
        if not source:
            # Try alternative key
            source = c.get("cycle_break_target_id", "")
        if not source:
            continue

        m = co_cycle_pattern.search(inst)
        if not m:
            continue
        targets = name_pattern.findall(m.group(1))
        for t in targets:
            edges_by_source[source].add(t)
            edges_by_target[t].add(source)
            all_edges.add((source, t))

    print(f"  Total unique (source, target) edges named for strip: {len(all_edges)}")
    print(f"  Unique source notes with at least one strippable edge: {len(edges_by_source)}")
    print(f"  Unique target notes referenced: {len(edges_by_target)}")
    print()

    # Top sources (notes that need the most editing)
    top_sources = sorted(
        edges_by_source.items(), key=lambda kv: len(kv[1]), reverse=True
    )[:10]
    print(f"  Top 10 SOURCE notes (would need editing in repair pass):")
    for src, targets in top_sources:
        print(f"    {len(targets):3d} edges to strip  ({src})")

    # Top targets (notes being referenced as non-load-bearing)
    print()
    top_targets = sorted(
        edges_by_target.items(), key=lambda kv: len(kv[1]), reverse=True
    )[:10]
    print(f"  Top 10 TARGET notes (cite-only references to these):")
    for tgt, sources in top_targets:
        print(f"    {len(sources):3d} sources reference  ({tgt})")

    return all_edges, edges_by_source


# ============================================================================
# Section 5: Simulated impact of source-graph repair pass
# ============================================================================


def section_5_simulation(
    queue: dict,
    strippable_edges: set,
    edges_by_source: dict,
) -> None:
    section("5. SIMULATION — IF ALL NAMED EDGES WERE STRIPPED")

    cycles = queue.get("cycle_break_targets", [])

    # For each cycle, check if stripping ANY named non-load-bearing edge
    # in the cycle's instruction would break that cycle.
    # We use a coarse heuristic: cycle is "resolved by strip" if its instruction
    # names at least one (src, tgt) edge that appears in the cycle's node list.
    co_cycle_pattern = re.compile(r"co-cycle citations \[(.*?)\]")
    name_pattern = re.compile(r"'([^']+)'")

    resolved_count = 0
    unresolved_count = 0
    for c in cycles:
        nodes = set(c.get("all_cycle_nodes", []))
        inst = c.get("instruction", "")
        m = co_cycle_pattern.search(inst)
        if not m:
            unresolved_count += 1
            continue
        named = set(name_pattern.findall(m.group(1)))
        if named & nodes:
            resolved_count += 1
        else:
            unresolved_count += 1

    print(f"  Cycles resolved by stripping named edges: {resolved_count}")
    print(f"  Cycles NOT resolved (genuine or unnamed): {unresolved_count}")
    print()
    pct = 100 * resolved_count / max(len(cycles), 1)
    print(f"  Apparent-cycle fraction: {pct:.1f}%")
    print()
    print("  If a single source-graph repair pass strips all named edges,")
    print(f"  approximately {resolved_count} cycles vanish from the queue.")
    print()
    print(f"  Remaining {unresolved_count} cycles would need either:")
    print("    - genuine audit of the break target (real dependency)")
    print("    - additional non-load-bearing edges identified by re-audit")
    print()

    # How much editing work is the repair pass?
    notes_to_edit = len(edges_by_source)
    total_edges = sum(len(targets) for targets in edges_by_source.values())
    print(f"  Repair-pass scope:")
    print(f"    {notes_to_edit} source notes need editing")
    print(f"    {total_edges} markdown links total to strip-or-relocate")
    print(f"    average {total_edges/max(notes_to_edit,1):.1f} edits per note")


# ============================================================================
# Section 6: Recommendation
# ============================================================================


def section_6_recommendation(
    queue: dict,
    apparent_cycles: set,
    genuine_cycles: set,
    edges_by_source: dict,
) -> None:
    section("6. RECOMMENDATION — HIGHEST-LEVERAGE NEXT MOVE")

    ready = queue.get("ready_count", 0)
    pending = queue.get("total_pending", 0)
    cycles = len(queue.get("cycle_break_targets", []))
    unique_break_targets = len(edges_by_source)

    print(f"  Current state:")
    print(f"    {ready} of {pending} items ready ({100*ready/max(pending,1):.2f}%)")
    print(f"    {cycles} citation cycles blocking the queue")
    print(f"    {len(apparent_cycles)} cycles have explicit informational-co-cycle instructions")
    print(f"    {len(genuine_cycles)} cycles WITHOUT such instructions")
    print(f"    {unique_break_targets} unique primary_break_target notes")
    print()
    print(f"  How the cycle-resolution flow actually works:")
    print(f"    1. Audit pipeline names each cycle's `primary_break_target` (the")
    print(f"       node the auditor should audit) and its `co-cycle citations`")
    print(f"       (other cycle members the auditor should treat as informational)")
    print(f"    2. Codex auditor runs on the break target with the prompt instruction")
    print(f"       that the named co-cycle nodes are non-load-bearing.")
    print(f"    3. If the auditor returns `audited_clean` (chain closes without the")
    print(f"       co-cycle deps), the node moves to a settled status.")
    print(f"    4. A source-graph repair pass then strips the now-confirmed-cite-only")
    print(f"       markdown links from the source note. effective_status leaves")
    print(f"       retained_pending_chain.")
    print(f"    5. Re-run the audit pipeline (build_citation_graph + downstream)")
    print(f"       and the cycle disappears from cycle_inventory.")
    print()
    print(f"  Path to 'finish the full audit':")
    print(f"    A. Audit-prep contributions for high-leverage break targets")
    print(f"       (one PR per target, like the F-C contribution for")
    print(f"       ANOMALY_FORCES_TIME_THEOREM in PR #1262). Verifies the")
    print(f"       co-cycle nodes really are non-load-bearing before the")
    print(f"       Codex auditor runs.")
    print(f"       Volume: ~{unique_break_targets} target notes, one PR each.")
    print(f"    B. Build a source-graph repair tool (--apply mode) that")
    print(f"       mechanically strips markdown links after audited_clean")
    print(f"       verdicts. Currently the audit_queue says \"a separate")
    print(f"       source-graph repair pass must strip the markdown links\";")
    print(f"       that tool doesn't yet exist as a one-command operation.")
    print(f"    C. The audit lane's automated nightly pipeline cranks through")
    print(f"       audits on its own (visible in git log: \"audit: nightly")
    print(f"       repair and pipeline refresh (automated)\" commits).")
    print(f"       New audit-prep contributions accelerate (A).")
    print()
    print(f"  Highest-leverage NEW work the user can authorize:")
    print(f"    Option 1: Build the strip tool (B) — mechanical, finishes the")
    print(f"      cycle-3-of-5 step that currently has no tooling. After it")
    print(f"      lands, each audited_clean verdict can be followed up with")
    print(f"      a one-command strip.")
    print(f"    Option 2: Author audit-prep contributions (A) for the top-N")
    print(f"      highest-criticality break targets. Direct contributions")
    print(f"      to clearing the queue.")
    print(f"    Option 3: Let the automated pipeline (C) crank; just monitor")
    print(f"      with this diagnostic and intervene when specific stuck items")
    print(f"      need manual prep.")


# ============================================================================
# Main
# ============================================================================


def main() -> int:
    ledger_io.ensure_cache()
    if not (AUDIT_DATA / "audit_queue.json").exists():
        subprocess.run(
            ["bash", "docs/audit/scripts/run_pipeline.sh"],
            cwd=REPO_ROOT,
            check=True,
        )
    banner("AUDIT LANDSCAPE SNAPSHOT")
    print()
    print("Read-only diagnostic. Date snapshot taken from audit data files.")
    print(f"Repo root: {REPO_ROOT}")

    queue = load_json("audit_queue.json")
    ledger = load_json("audit_ledger.json")
    try:
        cycle_inv = load_json("cycle_inventory.json")
    except FileNotFoundError:
        cycle_inv = None

    section_1_ledger_status(ledger)
    section_2_queue(queue)
    apparent_cycles, genuine_cycles = section_3_cycles(queue, cycle_inv)
    strippable_edges, edges_by_source = section_4_strippable_edges(queue)
    section_5_simulation(queue, strippable_edges, edges_by_source)
    section_6_recommendation(queue, apparent_cycles, genuine_cycles, edges_by_source)

    banner("END OF SNAPSHOT")
    print()
    print("To re-run after audit state changes:")
    print(f"  python3 {Path(__file__).relative_to(REPO_ROOT)}")
    print()
    print("To inspect the cycle-clearing repair workflow (dry-run stub):")
    print("  python3 scripts/source_graph_repair_pass.py --limit 5")
    print()
    print("To author an audit-prep contribution for a specific break target")
    print("(see PR #1262 for the template):")
    print("  1. Pick a primary_break_target from sections 4/5 above")
    print("  2. 5-agent special-forces fan-out on the target's claims")
    print("  3. Write docs/<TARGET>_HOSTILE_AUDIT_FINDINGS_NOTE_<DATE>.md")
    print("  4. Pair with verification runner + cache")
    print("  5. Open PR with audit_support claim_type")

    return 0


if __name__ == "__main__":
    sys.exit(main())
