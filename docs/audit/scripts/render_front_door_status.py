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


SHADOW_TOP_N = 10  # 'top segment' size; a stated assumption, not a rate claim


def _banded_interleave(queue_entries: list, lane_ids: set) -> list:
    """OFF-ONLY simulation of the design note's banded interleave: within
    each criticality band of the READY-filtered pending queue, alternate
    lane / non-lane starting lane-first; sub-order within each stream is the
    main-queue order. Selection assumptions: ready-only rows, top-N segment
    reported, no re-queue dynamics modeled."""
    ready = [e for e in queue_entries if e.get("ready")]
    out: list = []
    idx = 0
    while idx < len(ready):
        band_rank = ready[idx].get("criticality_rank", 0)
        band = []
        while idx < len(ready) and ready[idx].get("criticality_rank", 0) == band_rank:
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
    would-park counts, per-row named membership churn (from the TRACKED
    dispatch_shadow_state.json the shadow stage maintains across nightly
    checkouts), top-segment overlap, hypothetical banded-interleave top
    segment vs actual, advanced-lane and deferred-non-lane displacement, the
    manifest pending lifecycle, and loud gap/prior-state warnings.
    Reporting only; no dispatch effect."""
    lane_path = DATA_DIR / "audit_publication_lane.json"
    queue_path = DATA_DIR / "audit_queue.json"
    lane_shadow = load_json(lane_path) if lane_path.exists() else None
    queue_summary = (load_json(queue_path) if queue_path.exists() else {}) or {}
    lines = ["", "## Dispatch Shadow Report (no dispatch effect)", ""]
    if not lane_shadow:
        lines.append("- Shadow lane file unavailable (stage 16 has not run).")
        return lines

    lane_entries = lane_shadow.get("lane", [])
    lane_ids = {e["claim_id"] for e in lane_entries}
    queue_entries = queue_summary.get("queue", [])

    if not lane_shadow.get("gap_available"):
        lines.append(
            "**WARNING: publication gap unavailable this pass — the lane "
            "below is cycle-targets-only and NOT the full shadow lane.**")
        lines.append("")
    if not lane_shadow.get("prior_state_available"):
        lines.append(
            "NOTE: no prior shadow state was available (first pass, or state "
            "file absent) — added/removed churn is empty by definition this "
            "pass and removals cannot be detected until state exists.")
        lines.append("")

    added = lane_shadow.get("added_since_prior", [])
    removed = lane_shadow.get("removed_since_prior", [])
    pending_adds = lane_shadow.get("pending_adds", [])
    pending_removes = lane_shadow.get("pending_removes", [])
    unmanifested = lane_shadow.get("unmanifested_candidates", [])
    absent = lane_shadow.get("admitted_absent_from_lane_candidates", [])

    actual_ready = [e for e in queue_entries if e.get("ready")]
    actual_top = [e["claim_id"] for e in actual_ready[:SHADOW_TOP_N]]
    overlap = sum(1 for cid in actual_top if cid in lane_ids)
    simulated = _banded_interleave(queue_entries, lane_ids)
    sim_top = [e["claim_id"] for e in simulated[:SHADOW_TOP_N]]
    actual_pos = {e["claim_id"]: i for i, e in enumerate(actual_ready)}
    sim_pos = {e["claim_id"]: i for i, e in enumerate(simulated)}
    advanced = []
    deferred = []
    for cid, apos in actual_pos.items():
        spos = sim_pos.get(cid)
        if spos is None:
            continue
        if cid in lane_ids and spos < apos:
            advanced.append((cid, apos - spos))
        elif cid not in lane_ids and spos > apos:
            deferred.append((cid, spos - apos))
    advanced.sort(key=lambda x: -x[1])
    deferred.sort(key=lambda x: -x[1])

    lines.append(
        table(
            [
                ("Publication-lane size (shadow, admitted only)",
                 lane_shadow.get("lane_size", 0)),
                ("Manifest state", lane_shadow.get("manifest_state", "?")),
                ("Manifest pending additions", len(pending_adds)),
                ("Manifest pending removals", len(pending_removes)),
                ("Unmanifested candidates (need pending entries)",
                 len(unmanifested)),
                ("Admitted ids absent from lane candidates", len(absent)),
                ("Live conditional/failed rows that would park",
                 queue_summary.get("shadow_would_park_count", 0)),
                ("Live rows fail-open (no snapshot dep map)",
                 queue_summary.get("shadow_conditional_fail_open_count", 0)),
                (f"Lane rows already in actual ready top-{SHADOW_TOP_N}", overlap),
                ("Lane rows added since prior pass", len(added)),
                ("Lane rows removed since prior pass", len(removed)),
                ("Non-lane rows deferred by simulated interleave", len(deferred)),
            ]
        )
    )
    lines.append("")
    if added or removed:
        lines.append("Named lane membership churn since the prior pass:")
        for cid in added:
            lines.append(f"- added: `{cid}`")
        for cid in removed:
            lines.append(f"- removed: `{cid}`")
        lines.append("")
    if pending_adds:
        lines.append("Manifest pending ADDITIONS (objection window open):")
        for p in pending_adds:
            lines.append(f"- `{p['claim_id']}` (first report {p['first_report_date']})")
        lines.append("")
    if pending_removes:
        lines.append("Manifest pending REMOVALS (objection window open; row "
                     "stays laned until the removal is review-landed):")
        for p in pending_removes:
            lines.append(f"- `{p['claim_id']}` (first report {p['first_report_date']})")
        lines.append("")
    if unmanifested:
        lines.append("Unmanifested candidates (visible gaming surface; need "
                     "review-landed pending entries before admission):")
        for cid in unmanifested:
            lines.append(f"- `{cid}`")
        lines.append("")
    if absent:
        lines.append("Admitted ids currently absent from lane candidates:")
        for cid in absent:
            lines.append(f"- `{cid}`")
        lines.append("")
    lines.append(
        f"Hypothetical next dispatch top-{SHADOW_TOP_N} under OFF-ONLY banded "
        f"interleave (ready rows, lane-first within equal criticality bands) "
        f"vs actual queue order:")
    for i in range(SHADOW_TOP_N):
        sim = f"`{sim_top[i]}`" if i < len(sim_top) else "—"
        act = f"`{actual_top[i]}`" if i < len(actual_top) else "—"
        marker = "" if (i < len(sim_top) and i < len(actual_top) and sim_top[i] == actual_top[i]) else " ← differs"
        lines.append(f"- {i + 1}. sim {sim} / actual {act}{marker}")
    if advanced:
        lines.append("")
        lines.append("Lane rows advanced by the simulated interleave "
                     "(positions gained; complete list):")
        for cid, moved in advanced:
            lines.append(f"- `{cid}`: +{moved}")
    if deferred:
        lines.append("")
        lines.append("Non-lane rows deferred by the simulated interleave "
                     "(positions lost; complete list):")
        for cid, moved in deferred:
            lines.append(f"- `{cid}`: -{moved}")
    lines.append("")
    lines.append(
        "Simulation assumptions: ready-only rows, banded lane-first 1:1 "
        "alternation, no re-queue dynamics. Lane and gap come from THIS "
        "pipeline pass (stage 16 runs after the publication renderer); churn "
        "state persists in the tracked dispatch_shadow_state.json. Cutover "
        "flags remain OFF; see the dispatch-retarget design note's "
        "Ratification Log."
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
