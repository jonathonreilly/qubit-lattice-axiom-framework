#!/usr/bin/env python3
"""Produce the next-up audit queue.

Reads the ledger and writes a sorted list of claims awaiting audit. The
queue is the input that an auditor (the current best Codex GPT model at
maximum reasoning by default) pulls from.

Sorting key (descending priority):
  1. criticality (critical -> high -> medium -> leaf)
  2. all deps already at retained-grade ('ready')
     ahead of those waiting on an upstream audit
  3. transitive_descendants
  4. load_bearing_score

Each queue entry includes everything the auditor needs to construct the
prompt via AUDIT_AGENT_PROMPT_TEMPLATE.md without further repo access.

Writes:
  - data/audit_queue.json: full queue, machine-readable
  - AUDIT_QUEUE.md: top-50 human-readable view
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import premise_nodes
import ledger_io

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = REPO_ROOT / "docs" / "audit" / "data"
LEDGER_PATH = DATA_DIR / "audit_ledger.json"
CYCLE_INVENTORY_PATH = DATA_DIR / "cycle_inventory.json"
QUEUE_JSON = DATA_DIR / "audit_queue.json"
QUEUE_MD = REPO_ROOT / "docs" / "audit" / "AUDIT_QUEUE.md"
PUBLICATION_GAP_PATH = DATA_DIR / "publication_gap.json"
LANE_MANIFEST_PATH = DATA_DIR / "publication_lane_manifest.json"
LANE_JSON = DATA_DIR / "audit_publication_lane.json"

CRITICALITY_RANK = {"critical": 3, "high": 2, "medium": 1, "leaf": 0}

# Effective statuses considered stable inputs for an auditor.
READY_DEP_STATUSES = {
    "retained",
    "retained_no_go",
    "retained_bounded",
    "meta",
}


def dep_ready(status: str | None) -> bool:
    if status in READY_DEP_STATUSES:
        return True
    return bool(status and status.startswith("decoration_under_"))


def is_ready(row: dict, rows: dict[str, dict]) -> bool:
    """All deps are stable auditor inputs.

    A dep is a stable input when its effective_status is retained-grade /
    meta / decoration_under_*, or when it is a supplied axiom or approved
    primitive per `premise_nodes.is_accepted_premise_dep`. Open derivation
    obligations and historical admissions are not ready evidence.
    """
    for d in row.get("deps", []):
        if premise_nodes.is_non_evidence_context_dep(d):
            return False
        if premise_nodes.is_accepted_premise_dep(d):
            continue
        d_eff = rows.get(d, {}).get("effective_status") or "unknown"
        if not dep_ready(d_eff):
            return False
    return True


def needs_audit(row: dict) -> tuple[bool, str]:
    if row.get("claim_type") == "meta":
        return False, "metadata"
    audit_status = row.get("audit_status", "unaudited")
    if audit_status in {"unaudited", "audit_in_progress"}:
        return True, audit_status
    if row.get("claim_type_provenance") == "backfilled_pending_reaudit":
        return True, "claim_type_backfill_reaudit"
    # Owner rule (2026-06-15): terminal verdicts are bound/unbound/nogo only.
    # `audited_conditional` and `audited_failed` are non-terminal resting
    # states — each such row must be driven to a terminal verdict (repair +
    # re-audit, narrowing, or no-go conversion), so it stays in the pending
    # queue instead of resting as settled. Repair-side prompts for the same
    # rows (MISSING_DERIVATION_PROMPTS.md, dispatch queue) remain valid; the
    # queue_reason lets dispatchers separate re-audit from first audit.
    if audit_status == "audited_conditional":
        return True, "non_terminal_conditional"
    if audit_status == "audited_failed" and not row.get("note_path", "").startswith("archive_unlanded/"):
        return True, "non_terminal_failed"
    return False, "not_pending"


def cycle_break_targets(rows: dict[str, dict]) -> list[dict]:
    """Surface cycle-break repair targets from cycle_inventory.json.

    A citation cycle in the graph forces every node in the cycle to
    retained_pending_chain regardless of audit verdict. Each cycle needs
    one auditor-designated 'see also' edge stripped (or one node promoted
    via cycle_break_required). We surface, per cycle, the highest-impact
    node — the one most worth re-auditing with explicit cycle-break
    instructions in its prompt — so the queue carries an actionable repair
    target for each cycle, not just the bare cycle list.
    """
    if not CYCLE_INVENTORY_PATH.exists():
        return []
    inventory = json.loads(CYCLE_INVENTORY_PATH.read_text(encoding="utf-8"))
    cycles = inventory.get("cycles") or []
    targets: list[dict] = []
    for cycle in cycles:
        nodes = cycle.get("nodes") or []
        if not nodes:
            continue
        # Pick the node with the largest transitive_descendants - that's
        # the highest-leverage cycle break. Tie: smallest claim_id (stable).
        best = min(
            nodes,
            key=lambda n: (
                -(rows.get(n["claim_id"], {}).get("transitive_descendants") or 0),
                n.get("claim_id") or "",
            ),
        )
        cid = best["claim_id"]
        row = rows.get(cid, {})
        targets.append(
            {
                "cycle_id": cycle.get("cycle_id"),
                "cycle_length": cycle.get("length"),
                "max_transitive_descendants": cycle.get("max_transitive_descendants"),
                "primary_break_target": cid,
                "primary_break_target_audit_status": row.get("audit_status"),
                "primary_break_target_criticality": row.get("criticality") or "leaf",
                "all_cycle_nodes": [n["claim_id"] for n in nodes],
                "repair_class": "cycle_break_required",
                "instruction": (
                    "Re-audit this node with the prompt instruction that "
                    f"its co-cycle citations {sorted(set(n['claim_id'] for n in nodes if n['claim_id'] != cid))} "
                    "are informational/'see also' references, not load-bearing "
                    "dependencies. If the chain truly closes without those "
                    "citations, return audited_clean and name the non-load-bearing "
                    "co-cycle links in the rationale; a separate source-graph "
                    "repair pass must then strip or rewrite those markdown links "
                    "before effective_status can leave retained_pending_chain. Otherwise "
                    "return audited_conditional with repair_class="
                    "missing_dependency_edge naming the node that should be "
                    "promoted upstream."
                ),
            }
        )
    targets.sort(key=lambda t: (-(t["max_transitive_descendants"] or 0), t["cycle_length"] or 0))
    return targets


def _live_conditional_would_park(row: dict, rows: dict[str, dict]) -> tuple[bool, str]:
    """Shadow-only would-park CLASSIFICATION for a LIVE audited_conditional /
    non-archived audited_failed row (dispatch-retarget design note,
    2026-07-16); it carries no audit-verdict authority of any kind.
    Lifecycle projection: live rows carry their verdict-time snapshot at the
    row's top-level audit_state_snapshot (never previous_audits). Fail-open:
    no or empty snapshot dependency map -> not parked. Affects no dispatch
    decision; reporting only."""
    snapshot = row.get("audit_state_snapshot") or {}
    deps_then = snapshot.get("dep_effective_status") or {}
    if not deps_then:
        return False, "fail_open_no_snapshot_dep_map"
    for dep, then_status in deps_then.items():
        now = (rows.get(dep) or {}).get("effective_status", "MISSING")
        if now != then_status:
            return False, f"dep_effective_status_changed:{dep}"
    for field, snap_field in (
        ("claim_type", "dep_claim_type"),
        ("claim_scope", "dep_claim_scope"),
        ("note_hash", "dep_axiom_premise_note_hash"),
    ):
        then_values = snapshot.get(snap_field) or {}
        for dep, then_value in then_values.items():
            if dep in rows and rows[dep].get(field) != then_value:
                return False, f"{snap_field}_changed:{dep}"
    return True, "no_recorded_blocker_movement"


def _load_json_or_none(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _validate_manifest(manifest) -> tuple[bool, str]:
    """Schema validation for the tracked lane manifest. Invalid or missing
    manifest -> lane is empty (nothing is eligible without the tracked
    authority)."""
    if not isinstance(manifest, dict):
        return False, "manifest_missing_or_unreadable"
    if manifest.get("schema_version") != 1:
        return False, "manifest_schema_version_unsupported"
    if not isinstance(manifest.get("frozen_commit"), str) or not manifest["frozen_commit"]:
        return False, "manifest_frozen_commit_missing"
    if not isinstance(manifest.get("admitted"), list) or not all(
        isinstance(x, str) for x in manifest["admitted"]
    ):
        return False, "manifest_admitted_malformed"
    pending = manifest.get("pending")
    if not isinstance(pending, list):
        return False, "manifest_pending_malformed"
    for item in pending:
        if not (isinstance(item, dict) and isinstance(item.get("claim_id"), str)
                and isinstance(item.get("first_report_date"), str)):
            return False, "manifest_pending_entry_malformed"
    return True, "ok"


def build_publication_lane(pending: list[dict], cycle_targets: list[dict]) -> dict:
    """Shadow-only publication lane (dispatch-retarget design note,
    2026-07-16). Candidates = pending ∩ (publication gap ∪ primary
    cycle-break targets); the LANE itself contains only candidates ADMITTED
    by the tracked manifest (the manifest is the eligibility authority —
    unadmitted candidates appear only in the pending_admission report
    bucket, never in the lane). Ordered by the FULL main-queue key. The gap
    file is produced later in the same pipeline pass (renderer runs after
    the queue), so candidates consume the PREVIOUS pass's gap — a one-pass
    lag, labeled here. Generated, gitignored, affects no dispatch decision."""
    gap = _load_json_or_none(PUBLICATION_GAP_PATH)
    manifest = _load_json_or_none(LANE_MANIFEST_PATH)
    manifest_ok, manifest_state = _validate_manifest(manifest)
    gap_ids = {e["claim_id"] for e in (gap or {}).get("entries", []) if e.get("claim_id")}
    # cycle_break_targets() emits the id as primary_break_target.
    target_ids = {
        t["primary_break_target"]
        for t in cycle_targets
        if t.get("primary_break_target")
    }
    candidate_ids = gap_ids | target_ids
    admitted = set(manifest.get("admitted", [])) if manifest_ok else set()

    def _entry(e):
        return {
            "claim_id": e["claim_id"],
            "criticality": e["criticality"],
            "ready": e["ready"],
            "transitive_descendants": e["transitive_descendants"],
            "load_bearing_score": e["load_bearing_score"],
            "in_publication_gap": e["claim_id"] in gap_ids,
            "is_primary_cycle_break_target": e["claim_id"] in target_ids,
            "would_park": e.get("would_park"),
        }

    lane = [
        _entry(e) for e in pending
        if e["claim_id"] in candidate_ids and e["claim_id"] in admitted
    ]
    pending_admission = sorted(
        e["claim_id"] for e in pending
        if e["claim_id"] in candidate_ids and e["claim_id"] not in admitted
    )
    # pending is already sorted by the full main-queue key; lane inherits it.
    return {
        "schema_version": 1,
        "shadow_only": True,
        "gap_source_lag": "previous pipeline pass (renderer runs after queue)",
        "gap_available": gap is not None,
        "manifest_state": manifest_state,
        "manifest_frozen_commit": (manifest or {}).get("frozen_commit")
        if isinstance(manifest, dict) else None,
        "lane_size": len(lane),
        "pending_admission": pending_admission,
        "admitted_absent_from_candidates": sorted(admitted - candidate_ids),
        "lane": lane,
    }


def main() -> int:
    ledger_io.ensure_cache()
    if not LEDGER_PATH.exists():
        raise SystemExit("audit_ledger.json missing")
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    rows = ledger.get("rows", {})

    pending: list[dict] = []
    for cid, row in rows.items():
        include, queue_reason = needs_audit(row)
        if not include:
            continue
        a = row.get("audit_status", "unaudited")
        criticality = row.get("criticality") or "leaf"
        ready = is_ready(row, rows)
        entry = {
            "claim_id": cid,
            "note_path": row.get("note_path"),
            "claim_type": row.get("claim_type"),
            "claim_scope": row.get("claim_scope"),
            "claim_type_provenance": row.get("claim_type_provenance"),
            "audit_status": a,
            "effective_status": row.get("effective_status"),
            "queue_reason": queue_reason,
            "criticality": criticality,
            "criticality_rank": CRITICALITY_RANK.get(criticality, 0),
            "transitive_descendants": row.get("transitive_descendants", 0),
            "direct_in_degree": row.get("direct_in_degree", 0),
            "load_bearing_score": row.get("load_bearing_score", 0.0),
            "runner_path": row.get("runner_path"),
            "helper_runner_paths": list(row.get("helper_runner_paths") or []),
            "deps": list(row.get("deps", [])),
            "ready": ready,
            "blocker": row.get("blocker"),
            "cross_confirmation_status": (row.get("cross_confirmation") or {}).get("status"),
            "audit_independence_required": (
                "fresh_context_or_stronger_with_cross_confirmation"
                if criticality == "critical"
                else "fresh_context_or_stronger"
                if criticality == "high"
                else "any_non_self"
            ),
        }
        if queue_reason in ("non_terminal_conditional", "non_terminal_failed"):
            parked, park_reason = _live_conditional_would_park(row, rows)
            entry["would_park"] = parked
            entry["would_park_reason"] = park_reason
        pending.append(entry)

    pending.sort(
        key=lambda e: (
            -e["criticality_rank"],
            0 if e["ready"] else 1,
            -e["transitive_descendants"],
            -e["load_bearing_score"],
        )
    )

    cycle_targets = cycle_break_targets(rows)

    lane_shadow = build_publication_lane(pending, cycle_targets)
    LANE_JSON.write_text(json.dumps(lane_shadow, indent=1, sort_keys=True) + "\n")

    queue = {
        "total_pending": len(pending),
        "ready_count": sum(1 for e in pending if e["ready"]),
        "shadow_would_park_count": sum(
            1 for e in pending if e.get("would_park") is True
        ),
        "shadow_conditional_fail_open_count": sum(
            1
            for e in pending
            if e.get("would_park") is False
            and e.get("would_park_reason") == "fail_open_no_snapshot_dep_map"
        ),
        "shadow_publication_lane_size": lane_shadow["lane_size"],
        "by_criticality": {
            c: sum(1 for e in pending if e["criticality"] == c)
            for c in ("critical", "high", "medium", "leaf")
        },
        "cycle_break_targets": cycle_targets,
        "cycle_break_target_count": len(cycle_targets),
        "queue": pending,
    }
    QUEUE_JSON.write_text(json.dumps(queue, indent=2, sort_keys=True) + "\n")

    # Top-50 human view.
    top = pending[:50]
    md_lines = [
        "# Audit Queue",
        "",
        f"**Total pending:** {queue['total_pending']}",
        f"**Ready (all deps at retained-grade/metadata tiers or supplied axioms/approved primitives):** {queue['ready_count']}",
        "",
        "By criticality:",
    ]
    for c in ("critical", "high", "medium", "leaf"):
        md_lines.append(f"- `{c}`: {queue['by_criticality'][c]}")
    md_lines.append("")
    md_lines.append(
        "Auditor (current best Codex GPT model at maximum reasoning by "
        "default) should pull from the top of "
        "this list. Critical claims require cross-confirmation by a "
        "second independent clean-room auditor before `audited_clean` lands."
    )
    md_lines.append("")
    md_lines.append("## Top 50")
    md_lines.append("")
    md_lines.append(
        "| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |"
    )
    md_lines.append("|---:|---|---|---|---|---:|---:|:---:|---|---|")
    for i, e in enumerate(top, 1):
        md_lines.append(
            f"| {i} | `{e['claim_id']}` | {e.get('claim_type') or '-'} | "
            f"{e['queue_reason']} | {e['criticality']} | "
            f"{e['transitive_descendants']} | "
            f"{e['load_bearing_score']:.2f} | "
            f"{'Y' if e['ready'] else ''} | "
            f"{e['audit_independence_required']} | "
            f"{'`' + e['runner_path'] + '`' if e['runner_path'] else '-'} |"
        )
    md_lines.append("")
    if cycle_targets:
        md_lines.append("## Citation cycle break targets")
        md_lines.append("")
        md_lines.append(
            f"{len(cycle_targets)} citation cycles in the graph. Each cycle "
            "permanently blocks every member from `retained` until one node is "
            "re-audited with explicit cycle-break instructions or a 'see also' "
            "edge is stripped. Top 25 below; full list in "
            "`data/audit_queue.json` under `cycle_break_targets`."
        )
        md_lines.append("")
        md_lines.append("| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |")
        md_lines.append("|---:|---|---:|---:|---|---|---|")
        for i, t in enumerate(cycle_targets[:25], 1):
            md_lines.append(
                f"| {i} | `{t['cycle_id']}` | {t['cycle_length']} | "
                f"{t['max_transitive_descendants']} | `{t['primary_break_target']}` | "
                f"{t['primary_break_target_criticality']} | "
                f"{t['primary_break_target_audit_status'] or 'unaudited'} |"
            )
        md_lines.append("")
    md_lines.append("Full queue lives in `data/audit_queue.json`.")
    QUEUE_MD.write_text("\n".join(md_lines) + "\n")

    print(f"Wrote {QUEUE_JSON.relative_to(REPO_ROOT)}")
    print(f"Wrote {QUEUE_MD.relative_to(REPO_ROOT)}")
    print(f"  total pending: {queue['total_pending']}")
    print(f"  ready: {queue['ready_count']}")
    print(f"  by criticality: {queue['by_criticality']}")
    print(f"  cycle break targets: {queue['cycle_break_target_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
