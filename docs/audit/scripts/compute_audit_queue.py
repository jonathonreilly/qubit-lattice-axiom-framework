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

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import classify_runner_passes
import no_go_discipline_gate
import premise_nodes
import ledger_io

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = REPO_ROOT / "docs" / "audit" / "data"
LEDGER_PATH = DATA_DIR / "audit_ledger.json"
CYCLE_INVENTORY_PATH = DATA_DIR / "cycle_inventory.json"
QUEUE_JSON = DATA_DIR / "audit_queue.json"
QUEUE_MD = REPO_ROOT / "docs" / "audit" / "AUDIT_QUEUE.md"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
import runner_cache  # noqa: E402


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


BLOCKER_FINGERPRINT_V1 = "blocker_fingerprint_v1"
AUDIT_TUPLE_AGREEMENT_SCHEMA = "audit_tuple_v2"
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_POLICY_VERSION_KEYS = {
    "audit_tuple_agreement_schema",
    "n8_source_corpus_version",
    "no_go_discipline_gate_sha256",
    "audit_prompt_template_sha256",
}
_RUNNER_CACHE_ENTRY_KEYS_LEGACY = {
    "cache_freshness",
    "cache_runner_sha256",
    "cache_status",
    "cache_exit_code",
}
_RUNNER_CACHE_ENTRY_KEYS = _RUNNER_CACHE_ENTRY_KEYS_LEGACY | {
    "cache_input_fingerprint_sha256",
}
_CLASSIFIER_COUNT_KEYS = {"A", "B", "C", "D"}

# A v1 marker promises a complete, internally consistent baseline. Keep the
# public table for callers/tests, but put all substantive validation in
# fingerprint_v1_problems() so writer and comparator execute one predicate.
FINGERPRINT_V1_REQUIRED_KEYS = {
    "dep_effective_status": dict,
    "dep_claim_type": dict,
    "dep_claim_scope": dict,
    "dep_axiom_premise_note_hash": dict,
    "runner_path": (str, type(None)),
    "runner_present": bool,
    "runner_hash": (str, type(None)),
    "helper_runner_hashes": dict,
    "runner_cache_state": dict,
    "artifact_classifier_state": dict,
    "policy_versions": dict,
    "premise_registry_epoch": str,
}
# The second element is retained as a compatibility label for older test and
# report consumers. The comparator no longer trusts synthetic row projections;
# it recomputes every channel from the current repository state.
FINGERPRINT_V1_OPAQUE_CHANNELS = (
    ("runner_cache_state", "runner_cache_state_current"),
    ("artifact_classifier_state", "artifact_classifier_state_current"),
    ("policy_versions", "policy_versions_current"),
    ("premise_registry_epoch", "premise_registry_epoch_current"),
)


class FingerprintV1Invalid(ValueError):
    """A snapshot marked blocker_fingerprint_v1 is incomplete or malformed.
    Per the design note's validation matrix this fails LOUDLY (a v1 writer
    that omits a required baseline is a bug, never a silent fail-open)."""


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and bool(_SHA256_RE.fullmatch(value))


def _sha256_file(path: Path) -> str:
    """Read a required policy/input surface and return its content identity.

    OSError intentionally propagates: a v1 snapshot must never turn an
    unreadable required surface into a valid-looking parked baseline.
    """
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fingerprint_policy_versions(repo_root: Path | None = None) -> dict:
    root = REPO_ROOT if repo_root is None else repo_root
    return {
        "audit_tuple_agreement_schema": AUDIT_TUPLE_AGREEMENT_SCHEMA,
        "n8_source_corpus_version": no_go_discipline_gate.N8_SOURCE_CORPUS_VERSION,
        "no_go_discipline_gate_sha256": _sha256_file(
            Path(no_go_discipline_gate.__file__)
        ),
        "audit_prompt_template_sha256": _sha256_file(
            root / "docs" / "audit" / "AUDIT_AGENT_PROMPT_TEMPLATE.md"
        ),
    }


def fingerprint_premise_registry_epoch(repo_root: Path | None = None) -> str:
    root = REPO_ROOT if repo_root is None else repo_root
    return _sha256_file(
        root / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
    )


def fingerprint_runner_cache_state(row: dict) -> dict:
    state: dict[str, dict] = {}
    paths = [
        path
        for path in [
            row.get("runner_path"),
            *(row.get("helper_runner_paths") or []),
        ]
        if isinstance(path, str) and path
    ]
    for path in sorted(set(paths)):
        _cache_path, header, _body = runner_cache.load_cache(path)
        header = header or {}
        state[path] = {
            "cache_freshness": runner_cache.cache_status(path),
            "cache_runner_sha256": header.get("runner_sha256"),
            "cache_input_fingerprint_sha256": header.get(
                "input_fingerprint_sha256"
            ),
            "cache_status": header.get("status"),
            "cache_exit_code": header.get("exit_code"),
        }
    return state


def fingerprint_artifact_classifier_state(
    row: dict, repo_root: Path | None = None
) -> dict:
    root = REPO_ROOT if repo_root is None else repo_root
    runner_path = row.get("runner_path")
    if not runner_path:
        return {}
    path = root / runner_path
    if not path.exists():
        return {"runner_path": runner_path, "exists": False}
    source = path.read_text(encoding="utf-8", errors="replace")
    counts = classify_runner_passes.classify_source(source)
    dominant = max(counts, key=lambda key: counts[key]) if any(counts.values()) else None
    return {
        "runner_path": runner_path,
        "exists": True,
        "counts": counts,
        "assert_count": classify_runner_passes.count_assert_pass_lines(source),
        "dominant_class": dominant,
        "decoration_candidate": (
            counts["D"] == 0
            and counts["C"] == 0
            and counts["A"] + counts["B"] > 0
        ),
    }


def fingerprint_runner_state(
    row: dict, repo_root: Path | None = None
) -> tuple[str | None, bool, str | None]:
    root = REPO_ROOT if repo_root is None else repo_root
    runner_path = row.get("runner_path") or None
    if runner_path is None:
        return None, False, None
    path = root / runner_path
    if not path.exists():
        return runner_path, False, None
    return runner_path, True, _sha256_file(path)


def fingerprint_v1_current_channels(
    row: dict, repo_root: Path | None = None
) -> dict:
    root = REPO_ROOT if repo_root is None else repo_root
    return {
        "runner_cache_state": fingerprint_runner_cache_state(row),
        "artifact_classifier_state": fingerprint_artifact_classifier_state(row, root),
        "policy_versions": fingerprint_policy_versions(root),
        "premise_registry_epoch": fingerprint_premise_registry_epoch(root),
    }


def fingerprint_v1_problems(snapshot: object) -> list[str]:
    """Return every structural defect in a purported v1 snapshot."""
    if not isinstance(snapshot, dict):
        return ["snapshot:not_object"]
    problems: list[str] = []
    if snapshot.get("schema") != BLOCKER_FINGERPRINT_V1:
        problems.append("schema:not_blocker_fingerprint_v1")
    for key, expected_type in FINGERPRINT_V1_REQUIRED_KEYS.items():
        if key not in snapshot:
            problems.append(f"{key}:missing")
        elif not isinstance(snapshot[key], expected_type):
            problems.append(f"{key}:wrong_type")

    if problems:
        return problems

    dep_status = snapshot["dep_effective_status"]
    dep_type = snapshot["dep_claim_type"]
    dep_scope = snapshot["dep_claim_scope"]
    dep_axiom_hash = snapshot["dep_axiom_premise_note_hash"]
    if not all(isinstance(k, str) and isinstance(v, str) and v for k, v in dep_status.items()):
        problems.append("dep_effective_status:invalid_entry")
    if set(dep_type) != set(dep_status):
        problems.append("dep_claim_type:key_mismatch")
    if set(dep_scope) != set(dep_status):
        problems.append("dep_claim_scope:key_mismatch")
    if not all(
        isinstance(k, str) and (v is None or isinstance(v, str))
        for k, v in dep_type.items()
    ):
        problems.append("dep_claim_type:invalid_entry")
    if not all(
        isinstance(k, str) and (v is None or isinstance(v, str))
        for k, v in dep_scope.items()
    ):
        problems.append("dep_claim_scope:invalid_entry")
    if not set(dep_axiom_hash).issubset(dep_status):
        problems.append("dep_axiom_premise_note_hash:not_dependency_subset")
    if not all(isinstance(k, str) and _is_sha256(v) for k, v in dep_axiom_hash.items()):
        problems.append("dep_axiom_premise_note_hash:invalid_entry")

    runner_path = snapshot["runner_path"]
    runner_present = snapshot["runner_present"]
    runner_hash = snapshot["runner_hash"]
    if runner_path is not None and not runner_path:
        problems.append("runner_path:empty")
    if type(runner_present) is not bool:  # bool must not be admitted as int-like data
        problems.append("runner_present:not_bool")
    if runner_present and not _is_sha256(runner_hash):
        problems.append("runner_hash:required_sha256_when_present")
    if not runner_present and runner_hash is not None:
        problems.append("runner_hash:must_be_null_when_absent")
    if runner_present and runner_path is None:
        problems.append("runner_path:required_when_present")

    helper_hashes = snapshot["helper_runner_hashes"]
    if not all(
        isinstance(path, str)
        and bool(path)
        and (digest is None or _is_sha256(digest))
        for path, digest in helper_hashes.items()
    ):
        problems.append("helper_runner_hashes:invalid_entry")

    cache_state = snapshot["runner_cache_state"]
    expected_cache_paths = set(helper_hashes)
    if runner_path is not None:
        expected_cache_paths.add(runner_path)
    if set(cache_state) != expected_cache_paths:
        problems.append("runner_cache_state:path_set_mismatch")
    for path, entry in cache_state.items():
        if not isinstance(path, str) or not isinstance(entry, dict):
            problems.append("runner_cache_state:invalid_entry")
            continue
        entry_keys = frozenset(entry)
        if entry_keys not in {
            frozenset(_RUNNER_CACHE_ENTRY_KEYS_LEGACY),
            frozenset(_RUNNER_CACHE_ENTRY_KEYS),
        }:
            problems.append(f"runner_cache_state:{path}:wrong_keys")
            continue
        if entry["cache_freshness"] not in {
            "fresh", "missing", "corrupt", "sha_mismatch", "input_mismatch",
            "execution_timeout", "execution_error", "execution_nonzero_exit",
        }:
            problems.append(f"runner_cache_state:{path}:bad_freshness")
        cache_sha = entry["cache_runner_sha256"]
        if cache_sha is not None and not _is_sha256(cache_sha):
            problems.append(f"runner_cache_state:{path}:bad_sha256")
        input_fp = entry.get("cache_input_fingerprint_sha256")
        if input_fp is not None and not _is_sha256(input_fp):
            problems.append(f"runner_cache_state:{path}:bad_input_fingerprint")
        if entry["cache_status"] is not None and not isinstance(entry["cache_status"], str):
            problems.append(f"runner_cache_state:{path}:bad_status")
        if entry["cache_exit_code"] is not None and not isinstance(entry["cache_exit_code"], str):
            problems.append(f"runner_cache_state:{path}:bad_exit_code")

    classifier = snapshot["artifact_classifier_state"]
    if runner_path is None:
        if classifier != {}:
            problems.append("artifact_classifier_state:unexpected_without_runner")
    elif not runner_present:
        if classifier != {"runner_path": runner_path, "exists": False}:
            problems.append("artifact_classifier_state:bad_missing_runner_shape")
    else:
        expected_classifier_keys = {
            "runner_path", "exists", "counts", "assert_count",
            "dominant_class", "decoration_candidate",
        }
        if set(classifier) != expected_classifier_keys:
            problems.append("artifact_classifier_state:wrong_keys")
        else:
            counts = classifier["counts"]
            if classifier["runner_path"] != runner_path or classifier["exists"] is not True:
                problems.append("artifact_classifier_state:runner_mismatch")
            if not isinstance(counts, dict) or set(counts) != _CLASSIFIER_COUNT_KEYS:
                problems.append("artifact_classifier_state:bad_counts")
            elif not all(type(value) is int and value >= 0 for value in counts.values()):
                problems.append("artifact_classifier_state:bad_count_value")
            if type(classifier["assert_count"]) is not int or classifier["assert_count"] < 0:
                problems.append("artifact_classifier_state:bad_assert_count")
            if classifier["dominant_class"] not in _CLASSIFIER_COUNT_KEYS | {None}:
                problems.append("artifact_classifier_state:bad_dominant_class")
            if type(classifier["decoration_candidate"]) is not bool:
                problems.append("artifact_classifier_state:bad_decoration_candidate")

    policy = snapshot["policy_versions"]
    if set(policy) != _POLICY_VERSION_KEYS:
        problems.append("policy_versions:wrong_keys")
    else:
        if not isinstance(policy["audit_tuple_agreement_schema"], str) or not policy["audit_tuple_agreement_schema"]:
            problems.append("policy_versions:bad_audit_tuple_schema")
        if not isinstance(policy["n8_source_corpus_version"], str) or not policy["n8_source_corpus_version"]:
            problems.append("policy_versions:bad_n8_version")
        for key in ("no_go_discipline_gate_sha256", "audit_prompt_template_sha256"):
            if not _is_sha256(policy[key]):
                problems.append(f"policy_versions:{key}:bad_sha256")
    if not _is_sha256(snapshot["premise_registry_epoch"]):
        problems.append("premise_registry_epoch:not_sha256")
    return problems


def _live_conditional_would_park(row: dict, rows: dict[str, dict]) -> tuple[bool, str]:
    """Shadow-only would-park CLASSIFICATION for a LIVE audited_conditional /
    non-archived audited_failed row (dispatch-retarget design note,
    2026-07-16); it carries no audit-verdict authority of any kind.

    Version matrix (the note's rule, one branch per case):
    - snapshot absent OR without the blocker_fingerprint_v1 marker: LEGACY —
      always dispatch-open (would_park False, reason legacy_unversioned);
      its next verdict stamps a complete v1 snapshot.
    - snapshot marked v1 but missing any required baseline: raise
      FingerprintV1Invalid (loud pipeline failure).
    - snapshot marked v1 and complete: compare every recorded channel
      against current state; park only when nothing moved.

    Lifecycle projection: live rows read the row's top-level
    audit_state_snapshot (never previous_audits)."""
    snapshot = row.get("audit_state_snapshot") or {}
    if not snapshot:
        return False, "fail_open_no_snapshot"
    version = snapshot.get("schema")
    if version != BLOCKER_FINGERPRINT_V1:
        return False, "fail_open_legacy_unversioned"
    problems = fingerprint_v1_problems(snapshot)
    if problems:
        raise FingerprintV1Invalid(
            f"v1 snapshot has invalid baselines {problems} on "
            f"{row.get('note_path') or row.get('claim_id')}"
        )
    # dependency MEMBERSHIP: an added or removed dependency is movement
    deps_then = snapshot["dep_effective_status"]
    deps_now = set(row.get("deps") or [])
    if set(deps_then) != deps_now:
        return False, "dep_membership_changed"
    for dep, then_status in deps_then.items():
        now = (rows.get(dep) or {}).get("effective_status", "MISSING")
        if now != then_status:
            return False, f"dep_effective_status_changed:{dep}"
    for field, snap_field in (
        ("claim_type", "dep_claim_type"),
        ("claim_scope", "dep_claim_scope"),
        ("note_hash", "dep_axiom_premise_note_hash"),
    ):
        for dep, then_value in snapshot[snap_field].items():
            if dep in rows and rows[dep].get(field) != then_value:
                return False, f"{snap_field}_changed:{dep}"
    # Primary runner identity includes configured path, presence, and bytes.
    # These distinctions prevent present/missing and byte-identical path
    # replacement from being mistaken for an unchanged blocker surface.
    try:
        now_runner_path, now_runner_present, now_runner_hash = fingerprint_runner_state(
            row
        )
    except OSError as exc:
        raise FingerprintV1Invalid(
            f"cannot read current primary runner for v1 comparison: {exc}"
        ) from exc
    if now_runner_path != snapshot["runner_path"]:
        return False, "runner_path_changed"
    if now_runner_present != snapshot["runner_present"]:
        return False, "runner_presence_changed"
    if now_runner_hash != snapshot["runner_hash"]:
        return False, "runner_hash_changed"

    # Helper-runner membership and bytes are recomputed from the live repo.
    then_helpers = snapshot["helper_runner_hashes"]
    now_helper_paths = set(row.get("helper_runner_paths") or [])
    if set(then_helpers) != now_helper_paths:
        return False, "helper_runner_membership_changed"
    for path, then_hash in then_helpers.items():
        try:
            helper_path = REPO_ROOT / path
            now_hash = _sha256_file(helper_path) if helper_path.exists() else None
        except OSError as exc:
            raise FingerprintV1Invalid(
                f"cannot read current helper runner {path!r}: {exc}"
            ) from exc
        if now_hash != then_hash:
            return False, f"helper_runner_hash_changed:{path}"

    # Recompute every remaining v1 channel. Stored `*_current` row fields are
    # deliberately ignored: no cached/synthetic projection may certify a park.
    try:
        current_channels = fingerprint_v1_current_channels(row)
    except OSError as exc:
        raise FingerprintV1Invalid(
            f"cannot read current v1 blocker surface: {exc}"
        ) from exc
    for snap_key, _compat_current_key in FINGERPRINT_V1_OPAQUE_CHANNELS:
        current_value = current_channels[snap_key]
        snapshot_value = snapshot[snap_key]
        if snap_key == "runner_cache_state":
            # Existing v1 snapshots predate declared-input identity. Preserve
            # their four-field comparison shape instead of failing them as a
            # malformed migration. Newly stamped entries carry the fifth field
            # and therefore detect input movement even after cache refresh.
            current_value = {
                path: (
                    {k: v for k, v in entry.items()
                     if k != "cache_input_fingerprint_sha256"}
                    if path in snapshot_value
                    and "cache_input_fingerprint_sha256"
                    not in snapshot_value[path]
                    else entry
                )
                for path, entry in current_value.items()
            }
        if current_value != snapshot_value:
            return False, f"{snap_key}_changed"
    return True, "no_recorded_blocker_movement"


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
            and str(e.get("would_park_reason", "")).startswith("fail_open")
        ),

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
