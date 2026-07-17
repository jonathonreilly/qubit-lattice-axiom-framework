#!/usr/bin/env python3
"""Shadow dispatch computation (dispatch-retarget design note, 2026-07-16).

Runs LATE in the pipeline — after the publication renderer has written this
pass's publication_gap.json — so the lane always consumes the SAME pass's
gap (a fresh CI checkout has no previous pass; an early consumer would see
no gap at all, which is exactly the failure this stage exists to avoid).

Emits (gitignored, regenerated every pass):
  docs/audit/data/audit_publication_lane.json

Updates (TRACKED, generated data landed only by the audit lane's nightly
auto-commit, like ledger_meta.json — PRs never ship it):
  docs/audit/data/dispatch_shadow_state.json
    {"lane_ids": [...], "as_of_utc": ...}  — the prior-pass lane used for
    night-over-night churn in the front-door shadow report.

Reads (never modifies): audit_queue.json, publication_gap.json, the tracked
publication_lane_manifest.json.

Everything here is reporting metadata with zero evidentiary weight and zero
dispatch effect; no dispatch consumer reads any of it while the design
note's cutover flags remain unset.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = REPO_ROOT / "docs" / "audit" / "data"
QUEUE_JSON = DATA_DIR / "audit_queue.json"
PUBLICATION_GAP_PATH = DATA_DIR / "publication_gap.json"
LANE_MANIFEST_PATH = DATA_DIR / "publication_lane_manifest.json"
LANE_JSON = DATA_DIR / "audit_publication_lane.json"
SHADOW_STATE_PATH = DATA_DIR / "dispatch_shadow_state.json"


def _load_json_or_none(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def validate_manifest(manifest) -> tuple[bool, str]:
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
                and isinstance(item.get("first_report_date"), str)
                and item.get("action") in ("add", "remove")):
            return False, "manifest_pending_entry_malformed"
    return True, "ok"


def build_lane(queue: dict, gap, manifest) -> dict:
    """Lane = pending ∩ (this pass's publication gap ∪ primary cycle-break
    targets), restricted to manifest-ADMITTED ids; unadmitted candidates are
    reported, never laned. Ordering inherited from the queue (the full
    main-queue key). admitted_absent is computed against the CANDIDATE ∩
    PENDING set (an admitted id that is retained or no longer pending/cited
    is individually named)."""
    manifest_ok, manifest_state = validate_manifest(manifest)
    pending_entries = queue.get("queue", [])
    gap_ids = {e["claim_id"] for e in (gap or {}).get("entries", []) if e.get("claim_id")}
    target_ids = {
        t["primary_break_target"]
        for t in queue.get("cycle_break_targets", [])
        if t.get("primary_break_target")
    }
    candidate_ids = gap_ids | target_ids
    admitted = set(manifest.get("admitted", [])) if manifest_ok else set()
    manifest_pending = manifest.get("pending", []) if manifest_ok else []
    pending_adds = {p["claim_id"]: p for p in manifest_pending if p["action"] == "add"}
    pending_removes = {p["claim_id"]: p for p in manifest_pending if p["action"] == "remove"}

    lane = []
    unmanifested = []
    lane_candidate_ids = set()
    for e in pending_entries:
        cid = e["claim_id"]
        if cid not in candidate_ids:
            continue
        lane_candidate_ids.add(cid)
        if cid in admitted:
            # a pending REMOVAL keeps the row laned during its objection
            # window but is named in the report (both membership directions
            # get the same visible window)
            lane.append({
                "claim_id": cid,
                "criticality": e["criticality"],
                "ready": e["ready"],
                "transitive_descendants": e["transitive_descendants"],
                "load_bearing_score": e["load_bearing_score"],
                "in_publication_gap": cid in gap_ids,
                "is_primary_cycle_break_target": cid in target_ids,
                "would_park": e.get("would_park"),
                "pending_removal": cid in pending_removes,
            })
        elif cid in pending_adds:
            pass  # reported via pending_adds below
        else:
            unmanifested.append(cid)

    return {
        "schema_version": 2,
        "shadow_only": True,
        "gap_available": gap is not None,
        "gap_source": "same pipeline pass (this stage runs after the renderer)",
        "manifest_state": manifest_state,
        "manifest_frozen_commit": (manifest or {}).get("frozen_commit")
        if isinstance(manifest, dict) else None,
        "lane_size": len(lane),
        "pending_adds": sorted(pending_adds.values(), key=lambda p: p["claim_id"]),
        "pending_removes": sorted(pending_removes.values(), key=lambda p: p["claim_id"]),
        "unmanifested_candidates": sorted(unmanifested),
        "admitted_absent_from_lane_candidates": sorted(
            admitted - lane_candidate_ids
        ),
        "lane": lane,
    }


def main() -> int:
    queue = _load_json_or_none(QUEUE_JSON) or {}
    gap = _load_json_or_none(PUBLICATION_GAP_PATH)
    manifest = _load_json_or_none(LANE_MANIFEST_PATH)
    lane_shadow = build_lane(queue, gap, manifest)

    prior = _load_json_or_none(SHADOW_STATE_PATH) or {}
    prior_ids = prior.get("lane_ids")
    lane_ids = sorted(e["claim_id"] for e in lane_shadow["lane"])
    if isinstance(prior_ids, list):
        lane_shadow["added_since_prior"] = sorted(set(lane_ids) - set(prior_ids))
        lane_shadow["removed_since_prior"] = sorted(set(prior_ids) - set(lane_ids))
        lane_shadow["prior_state_available"] = True
    else:
        lane_shadow["added_since_prior"] = []
        lane_shadow["removed_since_prior"] = []
        lane_shadow["prior_state_available"] = False
    lane_shadow["prior_state_date"] = prior.get("as_of_date")

    LANE_JSON.write_text(json.dumps(lane_shadow, indent=1, sort_keys=True) + "\n")
    # DAY-KEYED update: the tracked state advances at most once per UTC day
    # (whichever pass runs first). Per-verdict pipeline runs later the same
    # day leave it untouched, so audit-batch commits that stage all of
    # docs/audit/data cannot consume churn between nightly reports.
    today = datetime.now(timezone.utc).date().isoformat()
    if prior.get("as_of_date") != today:
        SHADOW_STATE_PATH.write_text(json.dumps(
            {"schema_version": 2, "lane_ids": lane_ids, "as_of_date": today},
            indent=1, sort_keys=True) + "\n")
    print(f"dispatch shadow: lane={lane_shadow['lane_size']} "
          f"gap_available={lane_shadow['gap_available']} "
          f"manifest={lane_shadow['manifest_state']} "
          f"prior_state={lane_shadow['prior_state_available']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
