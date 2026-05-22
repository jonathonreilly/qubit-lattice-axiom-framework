#!/usr/bin/env python3
"""Render targeted audit-dispatch queues from machine-readable manifests.

The ordinary audit queue intentionally excludes rows that already have a
terminal clean verdict. Some process notes ask for a fresh-context re-audit of
such rows anyway, for example to decide whether a retained-bounded algebraic
row should be reclassified as a positive theorem after an axiom-surface
clarification. Those requests must be durable and machine-visible without
turning the manifest itself into audit evidence.

This script reads dispatcher sidecars from docs/audit/data and writes:

  - data/audit_dispatch_queue.json
  - AUDIT_DISPATCH_QUEUE.md

Supported sidecar schema:
  - promotion_reaudit_queue.v1
"""
from __future__ import annotations

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
AUDIT_DIR = REPO_ROOT / "docs" / "audit"
DATA_DIR = AUDIT_DIR / "data"
LEDGER_PATH = DATA_DIR / "audit_ledger.json"
OUT_JSON = DATA_DIR / "audit_dispatch_queue.json"
OUT_MD = AUDIT_DIR / "AUDIT_DISPATCH_QUEUE.md"

SUPPORTED_SCHEMAS = {"promotion_reaudit_queue.v1"}
DEFAULT_READY_STATUSES = {
    "retained",
    "retained_bounded",
    "retained_no_go",
    "meta",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def source_sidecars() -> list[Path]:
    """Return dispatcher source sidecars, excluding generated outputs."""
    candidates: list[Path] = []
    for pattern in ("*reaudit_queue*.json", "*dispatch_queue*.json"):
        candidates.extend(DATA_DIR.glob(pattern))
    excluded = {OUT_JSON.name, "audit_queue.json", "reaudit_candidates.json"}
    return sorted({p for p in candidates if p.name not in excluded})


def row_is_ready(row: dict, rows: dict[str, dict]) -> bool:
    for dep in row.get("deps", []):
        status = (rows.get(dep) or {}).get("effective_status")
        if status in DEFAULT_READY_STATUSES:
            continue
        if isinstance(status, str) and status.startswith("decoration_under_"):
            continue
        return False
    return True


def target_is_live(target: dict, row: dict | None) -> bool:
    if row is None:
        return False
    expected = {
        "claim_type": target.get("current_claim_type"),
        "audit_status": target.get("current_audit_status"),
        "effective_status": target.get("current_effective_status"),
    }
    return all(expected[k] in {None, row.get(k)} for k in expected)


def normalize_promotion_manifest(path: Path, manifest: dict, rows: dict[str, dict]) -> tuple[list[dict], list[dict]]:
    allowed_context = list(manifest.get("allowed_context_paths") or [])
    forbidden_context = list(manifest.get("forbidden_context") or [])
    live: list[dict] = []
    resolved_or_invalid: list[dict] = []

    live_group_ids: set[str] = set()
    groups = sorted(manifest.get("groups") or [], key=lambda g: (g.get("order") or 9999, g.get("group_id") or ""))
    for group in groups:
        group_id = group.get("group_id")
        if any(target_is_live(t, rows.get(t.get("claim_id"))) for t in group.get("targets") or []):
            live_group_ids.add(group_id)

    order = 0
    for group in groups:
        group_id = group.get("group_id")
        blocked_by = list(group.get("blocked_by_group_ids") or [])
        group_ready = not any(b in live_group_ids for b in blocked_by)
        for target in group.get("targets") or []:
            order += 1
            cid = target.get("claim_id")
            row = rows.get(cid)
            base = {
                "source_json_path": str(path.relative_to(REPO_ROOT)),
                "source_schema": manifest.get("schema"),
                "generated_order": order,
                "group_id": group_id,
                "group_order": group.get("order"),
                "blocked_by_group_ids": blocked_by,
                "claim_id": cid,
                "note_path": target.get("note_path"),
                "audit_question": target.get("audit_question"),
                "expected_current_claim_type": target.get("current_claim_type"),
                "expected_current_audit_status": target.get("current_audit_status"),
                "expected_current_effective_status": target.get("current_effective_status"),
                "actual_claim_type": row.get("claim_type") if row else None,
                "actual_audit_status": row.get("audit_status") if row else None,
                "actual_effective_status": row.get("effective_status") if row else None,
                "runner_path": row.get("runner_path") if row else None,
                "helper_runner_paths": list((row or {}).get("helper_runner_paths") or []),
                "deps": list((row or {}).get("deps") or []),
                "allowed_context_paths": allowed_context,
                "forbidden_context": forbidden_context,
                "must_not_use_manifest_as_evidence": bool(manifest.get("forbidden_context")),
                "dispatch_kind": "promotion_reaudit",
                "dispatch_instruction": (
                    "Use this entry only to select the target claim. Do not pass "
                    "the dispatcher manifest itself as audit evidence. Audit the "
                    "target source note under restricted context and apply any "
                    "retag through apply_audit.py."
                ),
            }
            if row is None:
                base["state"] = "invalid_missing_claim_id"
                resolved_or_invalid.append(base)
            elif not target_is_live(target, row):
                base["state"] = "resolved_or_superseded"
                resolved_or_invalid.append(base)
            else:
                base["state"] = "live"
                base["ready"] = group_ready and row_is_ready(row, rows)
                base["ready_blocker"] = None if group_ready else f"blocked_by_live_group:{','.join(blocked_by)}"
                live.append(base)

    return live, resolved_or_invalid


def render_markdown(output: dict) -> str:
    lines = [
        "# Audit Dispatch Queue",
        "",
        "This queue is generated from machine-readable dispatcher manifests. It is a target-selection surface only: dispatcher manifests must not be passed to auditors as evidence.",
        "",
        f"**Live entries:** {output['live_count']}",
        f"**Ready entries:** {output['ready_count']}",
        f"**Resolved/invalid entries:** {len(output['resolved_or_invalid'])}",
        "",
    ]
    if output["source_json_paths"]:
        lines.append("Source sidecars:")
        for p in output["source_json_paths"]:
            lines.append(f"- `{p}`")
        lines.append("")

    lines.append("## Live Dispatch Entries")
    lines.append("")
    if not output["live"]:
        lines.append("_No live dispatch entries._")
        lines.append("")
    else:
        lines.append("| # | ready | group | claim_id | current | source note | audit question |")
        lines.append("|---:|:---:|---|---|---|---|---|")
        for i, entry in enumerate(output["live"], 1):
            current = (
                f"{entry.get('actual_claim_type')} / "
                f"{entry.get('actual_audit_status')} / "
                f"{entry.get('actual_effective_status')}"
            )
            question = (entry.get("audit_question") or "").replace("|", "\\|")
            lines.append(
                f"| {i} | {'Y' if entry.get('ready') else ''} | "
                f"`{entry.get('group_id') or '-'}` | `{entry.get('claim_id')}` | "
                f"{current} | `{entry.get('note_path')}` | {question} |"
            )
        lines.append("")

    if output["resolved_or_invalid"]:
        lines.append("## Resolved Or Invalid")
        lines.append("")
        lines.append("| # | state | claim_id | current |")
        lines.append("|---:|---|---|---|")
        for i, entry in enumerate(output["resolved_or_invalid"], 1):
            current = (
                f"{entry.get('actual_claim_type')} / "
                f"{entry.get('actual_audit_status')} / "
                f"{entry.get('actual_effective_status')}"
            )
            lines.append(f"| {i} | {entry.get('state')} | `{entry.get('claim_id')}` | {current} |")
        lines.append("")

    lines.append("Full machine-readable queue lives in `data/audit_dispatch_queue.json`.")
    return "\n".join(lines) + "\n"


def main() -> int:
    if not LEDGER_PATH.exists():
        raise SystemExit("audit_ledger.json missing")
    rows = load_json(LEDGER_PATH).get("rows", {})

    live: list[dict] = []
    resolved_or_invalid: list[dict] = []
    source_paths: list[str] = []
    unsupported: list[dict] = []

    for path in source_sidecars():
        manifest = load_json(path)
        schema = manifest.get("schema")
        if schema not in SUPPORTED_SCHEMAS:
            unsupported.append({"source_json_path": str(path.relative_to(REPO_ROOT)), "schema": schema})
            continue
        source_paths.append(str(path.relative_to(REPO_ROOT)))
        entries, other = normalize_promotion_manifest(path, manifest, rows)
        live.extend(entries)
        resolved_or_invalid.extend(other)

    live.sort(key=lambda e: (not e.get("ready"), e.get("group_order") or 9999, e.get("generated_order") or 9999, e.get("claim_id") or ""))
    for i, entry in enumerate(live, 1):
        entry["queue_order"] = i

    output = {
        "schema": "audit_dispatch_queue.v1",
        "policy": "target_selection_only_not_audit_evidence",
        "source_json_paths": source_paths,
        "unsupported_source_json": unsupported,
        "live_count": len(live),
        "ready_count": sum(1 for e in live if e.get("ready")),
        "live": live,
        "resolved_or_invalid": resolved_or_invalid,
    }
    OUT_JSON.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(output), encoding="utf-8")

    print(f"Wrote {OUT_JSON.relative_to(REPO_ROOT)}")
    print(f"Wrote {OUT_MD.relative_to(REPO_ROOT)}")
    print(f"  live dispatch entries: {output['live_count']}")
    print(f"  ready dispatch entries: {output['ready_count']}")
    if unsupported:
        print(f"  unsupported sidecars: {len(unsupported)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
