#!/usr/bin/env python3
"""Render the repo-front-door status snapshot from audit pipeline outputs."""
from __future__ import annotations

import json
import re
from pathlib import Path

import ledger_io

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = REPO_ROOT / "docs" / "audit" / "data"
OUT_PATH = REPO_ROOT / "docs" / "repo" / "FRONT_DOOR_STATUS.md"
DIVERGENCE_PATH = (
    REPO_ROOT
    / "docs"
    / "publication"
    / "ci3_z3"
    / "PUBLICATION_AUDIT_DIVERGENCE.md"
)


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def foundation_surface_lines() -> list[str]:
    """Registry-derived foundation block.

    The front door must never hand-state the foundation surface: this block is
    generated from the premise registry, so an axiom memo re-date or an
    approved-primitive registry change lands here on the next pipeline run
    without anyone editing prose. audit_lint separately warns when a
    front-door surface cites a superseded axiom-memo path.
    """
    premise = load_json(DATA_DIR / "axiom_premise_nodes.json")
    obligations = load_json(DATA_DIR / "derivation_obligations.json")
    nodes = premise.get("nodes", {})
    lines = [
        "## Foundation Surface",
        "",
        "The only supplied premise types are **axioms** and **approved primitives**.",
        "",
        "| Premise (stable id) | Type | Current source |",
        "|---|---|---|",
    ]
    for cid in premise.get("canonical_ids", []):
        node = nodes.get(cid, {})
        path = node.get("current_path") or "-"
        klass = "axiom set" if cid == "minimal_axioms" else "approved primitive"
        link = f"[`{path}`](../../{path})" if path != "-" else "-"
        lines.append(f"| `{cid}` | {klass} | {link} |")
    lines.extend(
        [
            "",
            "Open derivation obligations are tracked separately and carry **zero premise weight**:",
            "",
        ]
    )
    obligation_nodes = obligations.get("nodes") or {}
    for cid in obligations.get("canonical_ids", []):
        node = obligation_nodes.get(cid, {})
        path = node.get("current_path") or "-"
        link = f"[`{path}`](../../{path})" if path != "-" else "-"
        lines.append(f"- `{cid}` — {link}")
    lines.extend(
        [
            "",
            "Owner-approval history for axioms and primitives:",
            "[`docs/audit/AXIOM_MINIMALITY_POLICY.md`](../audit/AXIOM_MINIMALITY_POLICY.md) section 6.",
            "",
        ]
    )
    return lines


def status_counts() -> tuple[dict[str, int], int, int]:
    summary = load_json(DATA_DIR / "effective_status_summary.json")
    counts = summary["effective_status_counts"]
    boxed_decorations = sum(
        value for status, value in counts.items() if status.startswith("decoration_under_")
    )
    retained_grade = (
        counts.get("retained", 0)
        + counts.get("retained_no_go", 0)
        + counts.get("retained_bounded", 0)
        + boxed_decorations
    )
    return counts, boxed_decorations, retained_grade


def publication_gap_summary() -> tuple[int | None, list[tuple[str, str, int]]]:
    if not DIVERGENCE_PATH.exists():
        return None, []
    text = DIVERGENCE_PATH.read_text(encoding="utf-8")
    total_match = re.search(
        r"Total non-retained-grade rows in publication tables:\*\*\s+(\d+)",
        text,
    )
    total = int(total_match.group(1)) if total_match else None
    rows: list[tuple[str, str, int]] = []
    in_summary = False
    for line in text.splitlines():
        if line.startswith("## Summary by criticality"):
            in_summary = True
            continue
        if in_summary and line.startswith("## "):
            break
        if not in_summary or not line.startswith("| "):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) != 3 or parts[0] in {"criticality", "---"}:
            continue
        try:
            rows.append((parts[0], parts[1].strip("`"), int(parts[2])))
        except ValueError:
            continue
    return total, rows


def table(rows: list[tuple[str, str | int]]) -> str:
    out = ["| Metric | Value |", "|---|---:|"]
    for key, value in rows:
        out.append(f"| {key} | {value} |")
    return "\n".join(out)


SHADOW_PRIOR_PATH = DATA_DIR / "dispatch_shadow_prior.json"
SHADOW_TOP_N = 10  # 'top segment' size; a stated assumption, not a rate claim


def _banded_interleave(queue_entries: list, lane_ids: set) -> list:
    """OFF-ONLY simulation of the design note's banded interleave: within
    each (criticality_rank, ready) band of the READY-filtered pending queue,
    alternate lane / non-lane starting lane-first; sub-order within each
    stream is the main-queue order. Selection assumptions: ready-only rows,
    top-N segment reported, no re-queue dynamics modeled."""
    ready = [e for e in queue_entries if e.get("ready")]
    out: list = []
    band_key = lambda e: (-e.get("criticality_rank", 0),)
    idx = 0
    while idx < len(ready):
        band_rank = band_key(ready[idx])
        band = []
        while idx < len(ready) and band_key(ready[idx]) == band_rank:
            band.append(ready[idx])
            idx += 1
        lane_stream = [e for e in band if e["claim_id"] in lane_ids]
        other_stream = [e for e in band if e["claim_id"] not in lane_ids]
        li = oi = 0
        take_lane = True
        while li < len(lane_stream) or oi < len(other_stream):
            if take_lane and li < len(lane_stream):
                out.append(lane_stream[li]); li += 1
            elif oi < len(other_stream):
                out.append(other_stream[oi]); oi += 1
            elif li < len(lane_stream):
                out.append(lane_stream[li]); li += 1
            take_lane = not take_lane
    return out


def shadow_report_lines() -> list:
    """The design note's nightly Dispatch Shadow Report: lane/admission and
    would-park counts, named membership churn vs the prior pass, top-segment
    overlap, hypothetical banded-interleave top segment vs actual, and
    displacement metrics. Persists a gitignored prior snapshot for diffs.
    Reporting only; no dispatch effect."""
    lane_path = DATA_DIR / "audit_publication_lane.json"
    queue_path = DATA_DIR / "audit_queue.json"
    lane_shadow = load_json(lane_path) if lane_path.exists() else None
    queue_summary = (load_json(queue_path) if queue_path.exists() else {}) or {}
    lines = ["", "## Dispatch Shadow Report (no dispatch effect)", ""]
    if not lane_shadow:
        lines.append("- Shadow lane file unavailable (first pass after landing).")
        return lines

    lane_entries = lane_shadow.get("lane", [])
    lane_ids = {e["claim_id"] for e in lane_entries}
    pending_admission = lane_shadow.get("pending_admission", [])
    absent = lane_shadow.get("admitted_absent_from_candidates", [])
    queue_entries = queue_summary.get("queue", [])

    # membership churn vs prior pass
    prior = (load_json(SHADOW_PRIOR_PATH)
             if SHADOW_PRIOR_PATH.exists() else {}) or {}
    prior_ids = set(prior.get("lane_ids", []))
    added = sorted(lane_ids - prior_ids)
    removed = sorted(prior_ids - lane_ids)
    try:
        SHADOW_PRIOR_PATH.write_text(
            json.dumps({"lane_ids": sorted(lane_ids)}, indent=1) + "\n"
        )
    except OSError:
        pass

    # top-segment overlap + simulated interleave + displacement
    actual_ready = [e for e in queue_entries if e.get("ready")]
    actual_top = [e["claim_id"] for e in actual_ready[:SHADOW_TOP_N]]
    overlap = sum(1 for cid in actual_top if cid in lane_ids)
    simulated = _banded_interleave(queue_entries, lane_ids)
    sim_top = [e["claim_id"] for e in simulated[:SHADOW_TOP_N]]
    actual_pos = {e["claim_id"]: i for i, e in enumerate(actual_ready)}
    displacements = []
    for i, cid in enumerate(sim_top):
        if cid in lane_ids:
            moved = actual_pos.get(cid, i) - i
            if moved > 0:
                displacements.append((cid, moved))

    lines.append(
        table(
            [
                ("Publication-lane size (shadow, admitted only)",
                 lane_shadow.get("lane_size", 0)),
                ("Candidates pending manifest admission", len(pending_admission)),
                ("Admitted ids absent from current candidates", len(absent)),
                ("Manifest state", lane_shadow.get("manifest_state", "?")),
                ("Live conditional/failed rows that would park",
                 queue_summary.get("shadow_would_park_count", 0)),
                ("Live rows fail-open (no snapshot dep map)",
                 queue_summary.get("shadow_conditional_fail_open_count", 0)),
                (f"Lane rows already in actual ready top-{SHADOW_TOP_N}", overlap),
                ("Lane rows added since prior pass", len(added)),
                ("Lane rows removed since prior pass", len(removed)),
            ]
        )
    )
    lines.append("")
    if added or removed:
        lines.append("Named lane membership churn since the prior pass:")
        for cid in added[:10]:
            lines.append(f"- added: `{cid}`")
        for cid in removed[:10]:
            lines.append(f"- removed: `{cid}`")
        if len(added) > 10 or len(removed) > 10:
            lines.append(
                f"- … and {max(len(added) - 10, 0) + max(len(removed) - 10, 0)} more"
            )
        lines.append("")
    if pending_admission:
        lines.append("Pending manifest admission (visible gaming surface):")
        for cid in pending_admission[:10]:
            lines.append(f"- `{cid}`")
        if len(pending_admission) > 10:
            lines.append(f"- … and {len(pending_admission) - 10} more")
        lines.append("")
    lines.append(
        f"Hypothetical next dispatch top-{SHADOW_TOP_N} under OFF-ONLY banded "
        f"interleave (ready rows, lane-first within equal criticality bands) "
        f"vs actual queue order:"
    )
    for i in range(SHADOW_TOP_N):
        sim = f"`{sim_top[i]}`" if i < len(sim_top) else "—"
        act = f"`{actual_top[i]}`" if i < len(actual_top) else "—"
        marker = "" if (i < len(sim_top) and i < len(actual_top) and sim_top[i] == actual_top[i]) else " ← differs"
        lines.append(f"- {i + 1}. sim {sim} / actual {act}{marker}")
    if displacements:
        lines.append("")
        lines.append("Lane rows advanced by the simulated interleave (positions gained):")
        for cid, moved in displacements[:10]:
            lines.append(f"- `{cid}`: +{moved}")
    lines.append("")
    lines.append(
        "Simulation assumptions: ready-only rows, banded lane-first 1:1 "
        "alternation, no re-queue dynamics. The candidate set consumes the "
        "previous pipeline pass's publication gap (renderer runs after the "
        "queue). Cutover flags remain OFF; see the dispatch-retarget design "
        "note's Ratification Log."
    )
    return lines


def main() -> None:
    ledger_io.ensure_cache()
    counts, boxed_decorations, retained_grade = status_counts()
    summary = load_json(DATA_DIR / "effective_status_summary.json")
    queue = load_json(DATA_DIR / "audit_queue.json")
    load_bearing = load_json(DATA_DIR / "load_bearing_summary.json")
    ledger = load_json(DATA_DIR / "audit_ledger.json")
    divergence_total, divergence_rows = publication_gap_summary()

    rows = ledger.get("rows", {})
    total_rows = len(rows)
    applied_audits = sum(
        1
        for row in rows.values()
        if row.get("audit_status") not in {None, "unaudited", "audit_in_progress"}
    )
    ready = [row for row in queue.get("queue", []) if row.get("ready")]

    lines: list[str] = [
        "<!-- AUTO-GENERATED by docs/audit/scripts/render_front_door_status.py -->",
        "<!-- generated: pipeline-derived -->",
        "",
        "# Front Door Status Snapshot",
        "",
        "**Auto-generated.** Refresh with `bash docs/audit/scripts/run_pipeline.sh`.",
        "This file summarizes the generated audit state that the root README links to.",
        "It is not a physics claim surface and should not be edited by hand.",
        "",
        *foundation_surface_lines(),
        "## Audit Surface",
        "",
        table(
            [
                ("Ledger rows", total_rows),
                ("Applied audit verdicts", applied_audits),
                ("Retained-grade rows, including boxed decorations", retained_grade),
                ("Retained positive theorems", counts.get("retained", 0)),
                ("Retained no-go rows", counts.get("retained_no_go", 0)),
                ("Retained bounded rows", counts.get("retained_bounded", 0)),
                ("Boxed decorations under retained parents", boxed_decorations),
                ("Open gates", counts.get("open_gate", 0)),
                ("Unaudited rows", counts.get("unaudited", 0)),
                ("Retained-pending-chain rows", summary.get("retained_pending_chain_count", 0)),
                ("Audited conditional rows", counts.get("audited_conditional", 0)),
                ("Audited renaming rows", counts.get("audited_renaming", 0)),
                ("Audited numerical-match rows", counts.get("audited_numerical_match", 0)),
                ("Citation cycles detected", summary.get("cycles_detected", 0)),
            ]
        ),
        "",
        "Source: tracked shards in [`docs/audit/data/ledger/`](../audit/data/ledger/) and",
        "[`docs/audit/data/effective_status_summary.json`](../audit/data/effective_status_summary.json).",
        "",
        "## Audit Queue",
        "",
        table(
            [
                ("Total pending rows", queue.get("total_pending", 0)),
                ("Ready rows", queue.get("ready_count", 0)),
                ("Cycle-break targets", queue.get("cycle_break_target_count", 0)),
                ("Critical pending", queue.get("by_criticality", {}).get("critical", 0)),
                ("High pending", queue.get("by_criticality", {}).get("high", 0)),
                ("Medium pending", queue.get("by_criticality", {}).get("medium", 0)),
                ("Leaf pending", queue.get("by_criticality", {}).get("leaf", 0)),
            ]
        ),
        "",
        "Next ready rows by queue order:",
        "",
    ]
    if ready:
        for row in ready[:8]:
            note_path = row.get("note_path")
            if note_path:
                target = f"[`{row['claim_id']}`](../../{note_path})"
            else:
                target = f"`{row['claim_id']}`"
            lines.append(
                f"- {target} - {row.get('criticality', 'unknown')}; "
                f"{row.get('queue_reason', 'queued')}"
            )
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "Source: [`docs/audit/AUDIT_QUEUE.md`](../audit/AUDIT_QUEUE.md) and",
            "the local pipeline cache `docs/audit/data/audit_queue.json` (gitignored).",
            "",
            "## Publication Gap",
            "",
        ]
    )
    if divergence_total is not None:
        lines.append(
            f"- Non-retained-grade cited rows in publication tables: **{divergence_total}**."
        )
        if divergence_rows:
            lines.append("")
            lines.append("| Criticality | Effective status | Count |")
            lines.append("|---|---|---:|")
            for criticality, status, count in divergence_rows[:12]:
                lines.append(f"| {criticality} | `{status}` | {count} |")
    else:
        lines.append("- Divergence report unavailable.")
    # Dispatch shadow report (dispatch-retarget design note, 2026-07-16).
    # Reporting only: nothing here affects any dispatch decision.
    lines.extend(shadow_report_lines())
    lines.extend(
        [
            "",
            "Source: [`docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md`](../publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md).",
            "",
            "## Load-Bearing Topology",
            "",
            table(
                [
                    ("Citation-graph nodes", load_bearing.get("node_count", 0)),
                    (
                        "Critical nodes",
                        load_bearing.get("criticality_counts", {}).get("critical", 0),
                    ),
                    (
                        "High nodes",
                        load_bearing.get("criticality_counts", {}).get("high", 0),
                    ),
                    (
                        "Medium nodes",
                        load_bearing.get("criticality_counts", {}).get("medium", 0),
                    ),
                    (
                        "Leaf nodes",
                        load_bearing.get("criticality_counts", {}).get("leaf", 0),
                    ),
                ]
            ),
            "",
            "Top load-bearing rows by graph score:",
            "",
        ]
    )
    for row in load_bearing.get("top_25_by_load_bearing_score", [])[:8]:
        lines.append(
            f"- `{row['claim_id']}` - {row['criticality']}; "
            f"{row['transitive_descendants']} descendants; score {row['load_bearing_score']:.3f}"
        )

    lines.append("")
    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
