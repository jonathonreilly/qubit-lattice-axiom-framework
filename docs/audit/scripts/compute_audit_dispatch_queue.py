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

Optional `retired_targets` entries document dispatch requests that should no
longer re-enter the live queue, for example a promotion request that resolved
as bounded-terminal unless future source work changes the claim.

Resolution semantics (in addition to retired_targets):

  - **Provenance re-audit resolution.** A dispatch target whose row has been
    re-audited after the manifest's `generated_date` AND whose recorded
    `independence` is no longer `weak` is treated as **resolved** even if its
    {claim_type, audit_status, effective_status} tuple matches the manifest
    guard. Re-auditing with stronger independence is exactly what the
    dispatcher asked for; the row should not loop the queue forever just
    because the verdict happened to confirm the prior status.

  - **Bounded-terminal resolution.** When the post-manifest re-audit confirms
    `claim_type == bounded_theorem` (i.e., the bounded-to-retained promotion
    request resolved as still-bounded), the resolution reason is recorded as
    `bounded_terminal_after_reaudit` so the operator can promote the entry to
    `retired_targets` if the bounded result should be considered terminal
    until the source note changes.

Resolved targets appear in the `resolved_targets` bucket of the output. They
are kept visible for provenance but excluded from `live_count` / `ready_count`.

Ready-blocker detail: when a live target is not ready, the `ready_blocker`
field names the specific reason. Group-readiness blockers continue to use
`blocked_by_live_group:<group_ids>`; dependency-readiness blockers now use
`blocked_by_dependency:<dep_claim_id>:<dep_effective_status>` (comma-separated
for multiple non-retained-grade deps).
"""
from __future__ import annotations

import json
from pathlib import Path

import ledger_io

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

# Dispatcher sidecars may select a target, but they may not widen the
# restricted audit packet arbitrarily.  Keep this process-only allowlist beside
# the producer so both queue generation and queue consumption use one policy.
DISPATCH_ALLOWED_PROCESS_PATHS = frozenset({
    "docs/audit/README.md",
    "docs/audit/FRESH_LOOK_REQUIREMENTS.md",
    "docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md",
    "docs/audit/ALGEBRAIC_DECORATION_POLICY.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/audit/data/derivation_obligations.json",
    "docs/ai_methodology/skills/no-go-discipline/SKILL.md",
    "docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md",
})

# Resolution reasons recorded on entries in `resolved_targets`.
RESOLUTION_REASON_FRESH_CONTEXT = "same_status_fresh_context_reaudit_after_manifest"
RESOLUTION_REASON_BOUNDED_TERMINAL = "bounded_terminal_after_reaudit"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_allowed_context_paths(
    allowed_context_paths,
    *,
    claim_id: str,
    row: dict,
    rows: dict[str, dict],
) -> list[str]:
    """Validate a dispatch manifest's restricted-context declaration.

    The normal packet builder already owns the selected note, its one-hop
    dependency notes, primary/helper runners, registered premise sources, and
    standard audit methodology.  A sidecar may enumerate only those surfaces;
    it cannot inject unrelated science or cached transcripts.  This function
    is intentionally shared by the producer and consumer so a sidecar that
    would stop the drainer instead fails during pipeline generation.
    """
    if not isinstance(allowed_context_paths, list) or not all(
        isinstance(path, str) and path for path in allowed_context_paths
    ):
        raise ValueError(
            f"dispatch target {claim_id} has malformed allowed_context_paths"
        )

    permitted_paths = set(DISPATCH_ALLOWED_PROCESS_PATHS)
    permitted_paths.update(filter(None, (
        row.get("note_path"),
        row.get("runner_path"),
    )))
    permitted_paths.update(row.get("helper_runner_paths") or [])
    for dep_id in row.get("deps") or []:
        dep_path = (rows.get(dep_id) or {}).get("note_path")
        if dep_path:
            permitted_paths.add(dep_path)

    unexpected_paths = set(allowed_context_paths) - permitted_paths
    if unexpected_paths:
        try:
            premise_registry = load_json(DATA_DIR / "axiom_premise_nodes.json")
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(
                "cannot validate dispatch allowed_context_paths"
            ) from exc
        permitted_paths.update(
            str(node.get("current_path"))
            for node in (premise_registry.get("nodes") or {}).values()
            if node.get("current_path")
        )
        unexpected_paths = set(allowed_context_paths) - permitted_paths

    if unexpected_paths:
        raise ValueError(
            f"dispatch target {claim_id} requests nonstandard context paths: "
            + ", ".join(sorted(unexpected_paths))
        )
    return list(allowed_context_paths)


def source_sidecars() -> list[Path]:
    """Return dispatcher source sidecars, excluding generated outputs."""
    candidates: list[Path] = []
    for pattern in ("*reaudit_queue*.json", "*dispatch_queue*.json"):
        candidates.extend(DATA_DIR.glob(pattern))
    excluded = {OUT_JSON.name, "audit_queue.json", "reaudit_candidates.json"}
    return sorted({p for p in candidates if p.name not in excluded})


def _dep_ready_status(status) -> bool:
    """Mirror the retained-grade test used in row_is_ready."""
    if status in DEFAULT_READY_STATUSES:
        return True
    if isinstance(status, str) and status.startswith("decoration_under_"):
        return True
    return False


def row_is_ready(row: dict, rows: dict[str, dict]) -> bool:
    for dep in row.get("deps", []):
        status = (rows.get(dep) or {}).get("effective_status")
        if not _dep_ready_status(status):
            return False
    return True


def row_dep_blockers(row: dict, rows: dict[str, dict]) -> list[tuple[str, str | None]]:
    """Return [(dep_claim_id, dep_effective_status), ...] for non-retained-grade deps.

    Empty list means the row is dep-ready (or has no deps).
    """
    blockers: list[tuple[str, str | None]] = []
    for dep in row.get("deps", []):
        status = (rows.get(dep) or {}).get("effective_status")
        if not _dep_ready_status(status):
            blockers.append((dep, status))
    return blockers


def target_is_live(target: dict, row: dict | None) -> bool:
    if row is None:
        return False
    expected = {
        "claim_type": target.get("current_claim_type"),
        "audit_status": target.get("current_audit_status"),
        "effective_status": target.get("current_effective_status"),
    }
    return all(expected[k] in {None, row.get(k)} for k in expected)


def _audit_date_after(audit_date, manifest_date: str | None) -> bool:
    """Return True iff `audit_date` (string) sorts on/after `manifest_date`.

    Both are ISO-8601 dates (or datetimes). Lexicographic comparison is
    correct for the YYYY-MM-DD prefix. If either is missing, returns False.
    """
    if not isinstance(audit_date, str) or not isinstance(manifest_date, str):
        return False
    return audit_date[:10] >= manifest_date[:10]


def resolve_provenance_reaudit(row: dict, manifest_date: str | None) -> tuple[str, dict] | None:
    """Decide whether a same-status row counts as resolved by a post-manifest re-audit.

    Returns (reason, evidence) when the row has been re-audited on/after the
    manifest's `generated_date` with `independence != "weak"`; otherwise None.

    Evidence includes the row's audit_date, independence, and auditor so the
    rendered surface can show why the entry was retired from the live queue.
    """
    audit_date = row.get("audit_date")
    independence = row.get("independence")
    if not _audit_date_after(audit_date, manifest_date):
        return None
    if independence is None or independence == "weak":
        return None
    if row.get("audit_status") in {None, "unaudited", "audit_in_progress"}:
        # The dispatcher target is live by status-tuple match, but the row
        # is not actually carrying a terminal verdict. Don't auto-resolve;
        # let the audit actually happen.
        return None
    evidence = {
        "audit_date": audit_date,
        "independence": independence,
        "auditor": row.get("auditor"),
        "auditor_family": row.get("auditor_family"),
        "audit_status": row.get("audit_status"),
        "claim_type": row.get("claim_type"),
    }
    if row.get("claim_type") == "bounded_theorem":
        return RESOLUTION_REASON_BOUNDED_TERMINAL, evidence
    return RESOLUTION_REASON_FRESH_CONTEXT, evidence


def normalize_promotion_manifest(
    path: Path, manifest: dict, rows: dict[str, dict]
) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    """Normalise a promotion-reaudit manifest into queue buckets.

    Returns (live, resolved_or_invalid, retired, resolved_targets).
    """
    allowed_context = manifest.get("allowed_context_paths")
    if allowed_context is None:
        allowed_context = []
    if not isinstance(allowed_context, list) or not all(
        isinstance(context_path, str) and context_path
        for context_path in allowed_context
    ):
        raise ValueError(
            f"{path.relative_to(REPO_ROOT)} has malformed allowed_context_paths"
        )
    allowed_context = list(allowed_context)
    forbidden_context = list(manifest.get("forbidden_context") or [])
    manifest_date = manifest.get("generated_date")
    live: list[dict] = []
    resolved_or_invalid: list[dict] = []
    retired: list[dict] = []
    resolved_targets: list[dict] = []

    for target in manifest.get("retired_targets") or []:
        cid = target.get("claim_id")
        row = rows.get(cid)
        retired.append(
            {
                "source_json_path": str(path.relative_to(REPO_ROOT)),
                "source_schema": manifest.get("schema"),
                "claim_id": cid,
                "note_path": target.get("note_path"),
                "audit_question": target.get("audit_question"),
                "retired_reason": target.get("retired_reason"),
                "expected_current_claim_type": target.get("current_claim_type"),
                "expected_current_audit_status": target.get("current_audit_status"),
                "expected_current_effective_status": target.get("current_effective_status"),
                "actual_claim_type": row.get("claim_type") if row else None,
                "actual_audit_status": row.get("audit_status") if row else None,
                "actual_effective_status": row.get("effective_status") if row else None,
                "state": "retired",
            }
        )

    # Group-level live set: a target counts as making its group live only if
    # it survives BOTH the status-tuple match and the new provenance-resolution
    # check. Otherwise a same-status fresh-context re-audited group member
    # would keep its sibling groups stuck behind a "live" group that no longer
    # has any unresolved live members.
    def _target_still_live(target: dict) -> bool:
        row = rows.get(target.get("claim_id"))
        if not target_is_live(target, row):
            return False
        if resolve_provenance_reaudit(row or {}, manifest_date) is not None:
            return False
        return True

    live_group_ids: set[str] = set()
    groups = sorted(manifest.get("groups") or [], key=lambda g: (g.get("order") or 9999, g.get("group_id") or ""))
    for group in groups:
        group_id = group.get("group_id")
        if any(_target_still_live(t) for t in group.get("targets") or []):
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
                continue
            if not target_is_live(target, row):
                base["state"] = "resolved_or_superseded"
                resolved_or_invalid.append(base)
                continue
            resolution = resolve_provenance_reaudit(row, manifest_date)
            if resolution is not None:
                reason, evidence = resolution
                base["state"] = "resolved"
                base["resolution_reason"] = reason
                base["resolution_evidence"] = evidence
                base["resolution_manifest_date"] = manifest_date
                resolved_targets.append(base)
                continue
            try:
                base["allowed_context_paths"] = validate_allowed_context_paths(
                    allowed_context,
                    claim_id=cid,
                    row=row,
                    rows=rows,
                )
            except ValueError as exc:
                raise ValueError(
                    f"{path.relative_to(REPO_ROOT)}: {exc}"
                ) from exc
            base["state"] = "live"
            dep_blockers = row_dep_blockers(row, rows)
            base["ready"] = group_ready and not dep_blockers
            if not group_ready:
                base["ready_blocker"] = f"blocked_by_live_group:{','.join(blocked_by)}"
            elif dep_blockers:
                parts = [f"{dep}:{status or 'missing'}" for dep, status in dep_blockers]
                base["ready_blocker"] = "blocked_by_dependency:" + ",".join(parts)
            else:
                base["ready_blocker"] = None
            live.append(base)

    return live, resolved_or_invalid, retired, resolved_targets


def render_markdown(output: dict) -> str:
    lines = [
        "# Audit Dispatch Queue",
        "",
        "This queue is generated from machine-readable dispatcher manifests. It is a target-selection surface only: dispatcher manifests must not be passed to auditors as evidence.",
        "",
        f"**Live entries:** {output['live_count']}",
        f"**Ready entries:** {output['ready_count']}",
        f"**Resolved (post-manifest re-audit) entries:** {len(output.get('resolved_targets', []))}",
        f"**Resolved/invalid entries:** {len(output['resolved_or_invalid'])}",
        f"**Retired entries:** {len(output['retired'])}",
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
        lines.append("| # | ready | group | claim_id | current | source note | audit question | ready_blocker |")
        lines.append("|---:|:---:|---|---|---|---|---|---|")
        for i, entry in enumerate(output["live"], 1):
            current = (
                f"{entry.get('actual_claim_type')} / "
                f"{entry.get('actual_audit_status')} / "
                f"{entry.get('actual_effective_status')}"
            )
            question = (entry.get("audit_question") or "").replace("|", "\\|")
            blocker = (entry.get("ready_blocker") or "").replace("|", "\\|")
            lines.append(
                f"| {i} | {'Y' if entry.get('ready') else ''} | "
                f"`{entry.get('group_id') or '-'}` | `{entry.get('claim_id')}` | "
                f"{current} | `{entry.get('note_path')}` | {question} | {blocker} |"
            )
        lines.append("")

    if output.get("resolved_targets"):
        lines.append("## Resolved By Post-Manifest Re-Audit")
        lines.append("")
        lines.append(
            "These dispatch targets have been re-audited after their "
            "manifest's `generated_date` with non-weak independence. They are "
            "no longer in the live queue, but kept here for provenance."
        )
        lines.append("")
        lines.append("| # | claim_id | current | resolution_reason | re-audit date | independence | auditor |")
        lines.append("|---:|---|---|---|---|---|---|")
        for i, entry in enumerate(output["resolved_targets"], 1):
            current = (
                f"{entry.get('actual_claim_type')} / "
                f"{entry.get('actual_audit_status')} / "
                f"{entry.get('actual_effective_status')}"
            )
            evidence = entry.get("resolution_evidence") or {}
            audit_date = evidence.get("audit_date") or ""
            independence = evidence.get("independence") or ""
            auditor = evidence.get("auditor") or ""
            lines.append(
                f"| {i} | `{entry.get('claim_id')}` | {current} | "
                f"`{entry.get('resolution_reason')}` | "
                f"{audit_date} | {independence} | {auditor} |"
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

    if output["retired"]:
        lines.append("## Retired Dispatch Targets")
        lines.append("")
        lines.append("| # | claim_id | current | reason |")
        lines.append("|---:|---|---|---|")
        for i, entry in enumerate(output["retired"], 1):
            current = (
                f"{entry.get('actual_claim_type')} / "
                f"{entry.get('actual_audit_status')} / "
                f"{entry.get('actual_effective_status')}"
            )
            reason = (entry.get("retired_reason") or "").replace("|", "\\|")
            lines.append(f"| {i} | `{entry.get('claim_id')}` | {current} | {reason} |")
        lines.append("")

    lines.append("Full machine-readable queue lives in `data/audit_dispatch_queue.json`.")
    return "\n".join(lines) + "\n"


def build_output(rows: dict[str, dict]) -> dict:
    """Recompute the complete generated dispatch payload without writing it."""
    live: list[dict] = []
    resolved_or_invalid: list[dict] = []
    retired: list[dict] = []
    resolved_targets: list[dict] = []
    source_paths: list[str] = []
    unsupported: list[dict] = []

    for path in source_sidecars():
        manifest = load_json(path)
        schema = manifest.get("schema")
        if schema not in SUPPORTED_SCHEMAS:
            unsupported.append({"source_json_path": str(path.relative_to(REPO_ROOT)), "schema": schema})
            continue
        source_paths.append(str(path.relative_to(REPO_ROOT)))
        entries, other, retired_entries, resolved_entries = normalize_promotion_manifest(
            path, manifest, rows
        )
        live.extend(entries)
        resolved_or_invalid.extend(other)
        retired.extend(retired_entries)
        resolved_targets.extend(resolved_entries)

    live.sort(key=lambda e: (not e.get("ready"), e.get("group_order") or 9999, e.get("generated_order") or 9999, e.get("claim_id") or ""))
    for i, entry in enumerate(live, 1):
        entry["queue_order"] = i
    resolved_targets.sort(
        key=lambda e: (e.get("group_order") or 9999, e.get("generated_order") or 9999, e.get("claim_id") or "")
    )

    return {
        "schema": "audit_dispatch_queue.v1",
        "policy": "target_selection_only_not_audit_evidence",
        "source_json_paths": source_paths,
        "unsupported_source_json": unsupported,
        "live_count": len(live),
        "ready_count": sum(1 for e in live if e.get("ready")),
        "live": live,
        "resolved_or_invalid": resolved_or_invalid,
        "resolved_targets": resolved_targets,
        "retired": retired,
    }


def main() -> int:
    ledger_io.ensure_cache()
    if not LEDGER_PATH.exists():
        raise SystemExit("audit_ledger.json missing")
    rows = load_json(LEDGER_PATH).get("rows", {})
    output = build_output(rows)
    OUT_JSON.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(output), encoding="utf-8")

    print(f"Wrote {OUT_JSON.relative_to(REPO_ROOT)}")
    print(f"Wrote {OUT_MD.relative_to(REPO_ROOT)}")
    print(f"  live dispatch entries: {output['live_count']}")
    print(f"  ready dispatch entries: {output['ready_count']}")
    print(f"  resolved (post-manifest re-audit) entries: {len(output['resolved_targets'])}")
    print(f"  retired dispatch entries: {len(output['retired'])}")
    if output["unsupported_source_json"]:
        print(f"  unsupported sidecars: {len(output['unsupported_source_json'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
