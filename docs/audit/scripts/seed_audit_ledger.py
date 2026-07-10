#!/usr/bin/env python3
"""Seed the audit ledger from the citation graph.

For every node in citation_graph.json, ensure an audit ledger row exists
with audit_status=unaudited as the default. If a row already exists,
preserve its audit fields but update graph metadata and dependencies. The
audit-owned `claim_type` drives retained/no-go/bounded classification. If
the source note's hash has changed since the last
audit, reset audit_status to unaudited and archive the prior verdict in
previous_audits. Terminal failed rows whose source notes moved to
archive_unlanded/ are preserved as negative-result history even though
they are no longer active graph nodes.

Writes docs/audit/data/audit_ledger.json.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from fnmatch import fnmatchcase
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = REPO_ROOT / "docs" / "audit" / "data"
GRAPH_PATH = DATA_DIR / "citation_graph.json"
LEDGER_PATH = DATA_DIR / "audit_ledger.json"
EXCLUDED_PATTERNS_FILE = DATA_DIR / "excluded_source_patterns.txt"
NEVER_GATE_PATHS_FILE = DATA_DIR / "never_gate_source_paths.txt"
META_PATTERNS_FILE = DATA_DIR / "meta_source_patterns.txt"
SOURCE_PATH_ALIASES_FILE = DATA_DIR / "source_path_aliases.json"


def _load_pattern_file(path: Path) -> tuple[str, ...]:
    """Read a pattern config file: one entry per line, # comments, blank lines OK."""
    if not path.exists():
        return ()
    out: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        out.append(line)
    return tuple(out)


# Source paths that are documentation or agent infrastructure, not auditable
# claim notes (loaded from data/excluded_source_patterns.txt). Rows are only
# dropped when the safety checks below confirm they are unaudited unknowns.
EXCLUDED_SOURCE_PATTERNS = _load_pattern_file(EXCLUDED_PATTERNS_FILE)

# Exact source paths that must remain in the ledger even if they match a
# broad infrastructure pattern (loaded from data/never_gate_source_paths.txt).
NEVER_GATE_SOURCE_PATHS = frozenset(_load_pattern_file(NEVER_GATE_PATHS_FILE))

# Top-level campaign/infrastructure notes kept as ledger metadata instead of
# dropped from the graph or treated as claims (loaded from
# data/meta_source_patterns.txt).
META_SOURCE_PATTERNS = _load_pattern_file(META_PATTERNS_FILE)

CLAIM_TYPES = {
    "positive_theorem",
    "bounded_theorem",
    "no_go",
    "open_gate",
    "decoration",
    "meta",
}

# Default empty audit fields applied to a freshly seeded row.
# audit_state_snapshot is included so that hash-drift archival also clears
# the snapshot — otherwise stale snapshots survive into unaudited rows and
# fire false lint warnings while invalidate_stale_audits skips them.
EMPTY_AUDIT = {
    "audit_status": "unaudited",
    "audit_date": None,
    "auditor": None,
    "auditor_family": None,
    "auditor_model": None,
    "auditor_reasoning_effort": None,
    "independence": None,
    "load_bearing_step": None,
    "load_bearing_step_class": None,
    "chain_closes": None,
    "chain_closure_explanation": None,
    "verdict_rationale": None,
    "open_dependency_paths": [],
    "decoration_parent_claim_id": None,
    "auditor_confidence": None,
    "runner_check_breakdown": {"A": 0, "B": 0, "C": 0, "D": 0, "total_pass": 0},
    "blocker": None,
    "claim_type": None,
    "claim_scope": None,
    "claim_type_provenance": None,
    "claim_type_last_reviewed": None,
    "notes_for_re_audit_if_any": None,
    # audit_state_snapshot is preserved BY apply_audit.py at audit time so
    # invalidate_stale_audits.py can detect downstream changes. When an audit
    # is reset (note hash drift, archived audit), the snapshot from the prior
    # audit is just historical noise and should be cleared so the lint does
    # not generate false "criticality bumped since audit" warnings against a
    # snapshot that no longer corresponds to an active audit.
    "audit_state_snapshot": None,
    "cross_confirmation": None,
}

# Audit fields that are preserved across re-seeds when the note hash is
# unchanged. If the hash changes, these are archived and reset.
AUDIT_FIELDS = list(EMPTY_AUDIT.keys())

DEFAULT_PROSE_STATUS = "not_evaluated_pre_vocab_lint"


def reset_prose_defaults(row: dict) -> None:
    """Mark source prose as unevaluated after new row creation or source drift."""
    row["prose_status"] = DEFAULT_PROSE_STATUS
    row["prose_corrections"] = []


def ensure_prose_defaults(row: dict) -> None:
    """Backfill prose fields without overwriting evaluated rows."""
    row.setdefault("prose_status", DEFAULT_PROSE_STATUS)
    row.setdefault("prose_corrections", [])


def reset_unaudited_audit_fields(row: dict) -> None:
    """Clear stale audit-owned residue from rows already back in the queue."""
    if row.get("audit_status") != "unaudited":
        return
    history = list(row.get("previous_audits") or [])
    exact_fields = {
        field: row.get(field)
        for field in ("auditor_model", "auditor_reasoning_effort")
        if row.get(field)
    }
    if history and exact_fields:
        identity_fields = {
            field: row.get(field)
            for field in ("auditor", "auditor_family")
            if row.get(field)
        }
        matches = [
            index
            for index, archived in enumerate(history)
            if all(archived.get(field) == value for field, value in identity_fields.items())
        ]
        target_index: int | None = None
        if len(history) == 1:
            # A sole archived audit is an unambiguous owner even when an older
            # reset already cleared the live auditor name/family.
            target_index = 0
        elif identity_fields and len(matches) == 1:
            target_index = matches[0]

        if target_index is not None:
            archived = dict(history[target_index])
            for field, value in exact_fields.items():
                if not archived.get(field):
                    archived[field] = value
            history[target_index] = archived
            row["previous_audits"] = history
        else:
            # Multiple archived audits plus no unique live identity cannot be
            # safely attributed. Preserve the exact legacy residue separately
            # instead of guessing or leaving it on the live unaudited row.
            residue = {
                **identity_fields,
                **exact_fields,
                "reason": "legacy_unaudited_exact_provenance_without_unique_history_match",
            }
            unattributed = list(row.get("unattributed_audit_provenance") or [])
            if residue not in unattributed:
                unattributed.append(residue)
            row["unattributed_audit_provenance"] = unattributed
    for k, v in EMPTY_AUDIT.items():
        row[k] = v if not isinstance(v, (list, dict)) else (list(v) if isinstance(v, list) else dict(v))


def is_excluded_source_path(path: str) -> bool:
    return any(fnmatchcase(path, pattern) for pattern in EXCLUDED_SOURCE_PATTERNS)


def should_gate_node(node: dict, prior: dict | None) -> bool:
    """Return True when a graph node should not become a ledger row.

    Exclusion is history-preserving, exactly as
    data/excluded_source_patterns.txt documents: a row under an excluded
    pattern is dropped only when it is an unaudited unknown — no terminal
    or in-flight audit_status AND no archived previous_audits. Rows
    carrying audit history are never auto-dropped (retroactive exclusion
    must not erase audit evidence); they stay in the ledger and surface as
    `excluded_path_row_grandfathered` lint notices, and retiring them is
    an owner/audit-lane decision. Exact paths in
    data/never_gate_source_paths.txt always stay.

    (The pre-2026-07 guard also kept any row whose effective_status was
    set — which after one pipeline run is every row, making retroactive
    exclusion a silent no-op. Citers of the droppable unaudited-unknown
    rows are themselves unaudited, so enforcing the documented rule fires
    no deps_changed re-audit cascade; the seeder strips gated ids from
    dependents' dep lists.)
    """
    path = node["path"]
    if not is_excluded_source_path(path):
        return False
    if path in NEVER_GATE_SOURCE_PATHS:
        return False

    if prior is not None:
        audit_status = prior.get("audit_status")
        if audit_status and audit_status != "unaudited":
            return False
        if prior.get("previous_audits"):
            return False

    return True


def should_preserve_archived_failed_row(row: dict) -> bool:
    """Keep terminal failed audit rows for archived notes out of docs/."""
    if row.get("audit_status") != "audited_failed":
        return False
    note_path = row.get("note_path") or ""
    if not note_path.startswith("archive_unlanded/"):
        return False
    return (REPO_ROOT / note_path).exists()


def hash_existing_note_path(note_path: str | None) -> str | None:
    if not note_path:
        return None
    path = REPO_ROOT / note_path
    if not path.exists():
        return None
    body = path.read_text(encoding="utf-8", errors="replace")
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


# Infrastructure directory families whose hint-less notes seed as `meta`
# (documentation, not claims). Kept in sync with the directory families in
# data/excluded_source_patterns.txt: rows under these paths that predate
# their exclusion are grandfathered into the ledger by should_gate_node,
# and while grandfathered they must at least be typed as metadata rather
# than falling through to the positive_theorem default.
INFRA_META_PATH_PREFIXES = (
    "docs/repo/",
    "docs/work_history/",
    "docs/lanes/",
    "docs/publication/",
    "docs/ai_methodology/",
)


def default_claim_type_for(node: dict) -> tuple[str, str]:
    """Return a provisional claim type for legacy rows.

    The auditor owns the final value. This backfill exists so the new
    propagation rule is total over old ledger rows before their next audit.

    Precedence:
      1. data/meta_source_patterns.txt — curated per-file registry for
         catalog/index/infrastructure docs; applies even over author hints.
      2. Explicit author `Type:`/`Claim type:` header, else the legacy
         Status-line migration hint.
      3. INFRA_META_PATH_PREFIXES — hint-less notes under the
         infrastructure directory families seed as meta.
      4. Fallback positive_theorem with provenance
         `default_positive_theorem`. This tier is visible debt, not a
         hidden state: audit_lint surfaces every such row as a
         `claim_type_defaulted` warning, and pre_commit_audit_check.sh
         (via check_staged_claim_typing.py) refuses staged notes in the
         defaulted class, so the backlog can only shrink.
    """
    path = node.get("path") or ""
    if any(fnmatchcase(path, pattern) for pattern in META_SOURCE_PATTERNS):
        return "meta", "backfilled_from_path"

    hint = node.get("claim_type_author_hint") or node.get("claim_type_seed_hint")
    if hint in CLAIM_TYPES:
        provenance = "author_hint" if node.get("claim_type_author_hint") else "migration_hint"
        return hint, provenance

    if path.startswith(INFRA_META_PATH_PREFIXES):
        return "meta", "backfilled_from_path"

    return "positive_theorem", "default_positive_theorem"


def backfill_scope(row: dict) -> str | None:
    if row.get("audit_status") in {None, "unaudited", "audit_in_progress"}:
        return None
    return (
        "Legacy audit row backfilled during scope-aware classification migration; "
        "re-audit may narrow this scope."
    )


def needs_critical_type_reaudit(row: dict, prior: dict | None) -> bool:
    if prior is None:
        return False
    if prior.get("claim_type") in CLAIM_TYPES:
        return False
    if prior.get("audit_status") in {None, "unaudited", "audit_in_progress"}:
        return False
    return (prior.get("criticality") or row.get("criticality")) == "critical"


def apply_claim_type_defaults(row: dict, node: dict, prior: dict | None) -> None:
    row.pop("current_status", None)
    row.pop("current_status_raw", None)
    row["claim_type_author_hint_raw"] = node.get("claim_type_author_hint_raw")
    row["claim_type_author_hint"] = node.get("claim_type_author_hint")

    audited_type = row.get("claim_type")
    provenance = row.get("claim_type_provenance")
    if audited_type in CLAIM_TYPES and provenance == "audited":
        return

    if row.get("audit_status") == "audited_decoration" and audited_type != "decoration":
        row["claim_type"] = "decoration"
        row["claim_type_provenance"] = "backfilled_pending_reaudit"
        row["claim_scope"] = row.get("claim_scope") or backfill_scope(row)
        return

    if audited_type not in CLAIM_TYPES:
        claim_type, inferred_provenance = default_claim_type_for(node)
        row["claim_type"] = claim_type
        row["claim_type_provenance"] = inferred_provenance
        if needs_critical_type_reaudit(row, prior):
            row["claim_type_provenance"] = "backfilled_pending_reaudit"
        if not row.get("claim_scope"):
            row["claim_scope"] = backfill_scope(row)
    elif provenance in {None, "author_hint", "backfilled", "backfilled_from_status", "backfilled_from_path", "migration_hint", "default_positive_theorem"}:
        # Only rewrite when the recomputed defaults actually disagree with
        # what's on the row. Repeated identical writes obscure the precedence
        # rule and produce noise in audit-data diffs.
        claim_type, inferred_provenance = default_claim_type_for(node)
        if row.get("claim_type") != claim_type or row.get("claim_type_provenance") != inferred_provenance:
            row["claim_type"] = claim_type
            row["claim_type_provenance"] = inferred_provenance


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def load_source_path_aliases() -> dict[str, str]:
    """Load non-semantic source-note path migrations.

    The audit ledger key is derived from the note path. Mechanical path
    cleanup can therefore rename a source note without changing its scientific
    content. In that case the old audit row should move to the new claim id
    instead of being dropped and re-seeded as unaudited.
    """
    data = load_json(SOURCE_PATH_ALIASES_FILE, {"aliases": {}})
    aliases = data.get("aliases", {}) if isinstance(data, dict) else {}
    return {str(old): str(new) for old, new in aliases.items()}


def source_path_alias_replacements(aliases: dict[str, str]) -> list[tuple[str, str]]:
    """Return current->legacy replacements for non-semantic path rewrites."""
    replacements: set[tuple[str, str]] = set()
    for old_path, new_path in aliases.items():
        old = str(old_path)
        new = str(new_path)
        replacements.add((new, old))
        replacements.add((Path(new).name, Path(old).name))
    return sorted(replacements, key=lambda item: len(item[0]), reverse=True)


def note_hash_change_is_path_alias_only(
    note_path: str,
    prior_hash: str | None,
    replacements: list[tuple[str, str]],
) -> bool:
    """True when source drift is only canonical path/link text replacement."""
    if not prior_hash or not replacements:
        return False
    path = REPO_ROOT / note_path
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    normalized = normalize_alias_text(text, replacements)
    if hashlib.sha256(normalized.encode("utf-8")).hexdigest() == prior_hash:
        return True
    prior_text = prior_note_text_by_hash(note_path, prior_hash)
    if prior_text is None:
        return False
    prior_normalized = normalize_alias_text(prior_text, replacements)
    return normalized == prior_normalized


def rewrite_alias_strings(value, replacements: list[tuple[str, str]]):
    """Recursively update legacy source-path strings inside preserved metadata."""
    if not replacements:
        return value
    if isinstance(value, str):
        out = value
        for current, legacy in replacements:
            out = out.replace(legacy, current)
        return out
    if isinstance(value, list):
        return [rewrite_alias_strings(item, replacements) for item in value]
    if isinstance(value, dict):
        return {
            key: rewrite_alias_strings(item, replacements)
            for key, item in value.items()
        }
    return value


def normalize_alias_text(text: str, replacements: list[tuple[str, str]]) -> str:
    """Normalize current path aliases back to their legacy spellings."""
    out = text
    for current, legacy in replacements:
        out = out.replace(current, legacy)
    return out


def prior_note_text_by_hash(note_path: str, prior_hash: str | None) -> str | None:
    """Find the prior committed text for note_path matching prior_hash.

    Alias-only migrations can touch rows that already contain older alias
    replacements. Comparing current-normalized text to the raw prior hash can
    over-normalize those older canonical spellings. When git history is
    available, compare current and prior text after the same normalization.
    """
    if not prior_hash:
        return None
    try:
        result = subprocess.run(
            ["git", "log", "--format=%H", "--", note_path],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    for commit in result.stdout.splitlines()[:200]:
        try:
            blob = subprocess.run(
                ["git", "show", f"{commit}:{note_path}"],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
                check=True,
            ).stdout
        except (OSError, subprocess.CalledProcessError):
            continue
        if hashlib.sha256(blob.encode("utf-8")).hexdigest() == prior_hash:
            return blob
    return None


def archive_prior_audit(row: dict) -> dict:
    """Snapshot the audit fields into previous_audits and return the cleared row."""
    prior = {k: row.get(k) for k in AUDIT_FIELDS}
    prior["archived_at"] = datetime.now(timezone.utc).isoformat()
    prior["archived_for_note_hash"] = row.get("note_hash")
    history = list(row.get("previous_audits", []))
    history.append(prior)
    new_row = dict(row)
    new_row["previous_audits"] = history
    for k, v in EMPTY_AUDIT.items():
        new_row[k] = v if not isinstance(v, (list, dict)) else (list(v) if isinstance(v, list) else dict(v))
    return new_row


def seed() -> dict:
    graph = load_json(GRAPH_PATH, None)
    if graph is None:
        raise SystemExit(
            "citation_graph.json missing; run build_citation_graph.py first"
        )

    existing = load_json(LEDGER_PATH, {"rows": {}})
    existing_rows: dict[str, dict] = existing.get("rows", {})
    source_path_aliases = load_source_path_aliases()
    alias_replacements = source_path_alias_replacements(source_path_aliases)
    existing_by_path = {
        row.get("note_path"): (cid, row)
        for cid, row in existing_rows.items()
        if row.get("note_path")
    }
    alias_old_paths_by_new: dict[str, list[str]] = {}
    for old_path, new_path in source_path_aliases.items():
        alias_old_paths_by_new.setdefault(new_path, []).append(old_path)
    used_alias_prior_cids: set[str] = set()

    out_rows: dict[str, dict] = {}
    seeded = 0
    preserved = 0
    migrated_path_aliases = 0
    re_audit_required = 0

    included_cids = {
        cid
        for cid, node in graph["nodes"].items()
        if not should_gate_node(node, existing_rows.get(cid))
    }
    gated = [cid for cid in graph["nodes"] if cid not in included_cids]
    archived_failed_rows = {
        cid: dict(row)
        for cid, row in existing_rows.items()
        if cid not in graph["nodes"] and should_preserve_archived_failed_row(row)
    }

    for cid, node in graph["nodes"].items():
        if cid not in included_cids:
            continue

        deps = [dep for dep in node["deps"] if dep in included_cids]
        prior = existing_rows.get(cid)
        prior_from_path_alias = False
        if prior is None:
            for old_path in alias_old_paths_by_new.get(node["path"], []):
                alias_hit = existing_by_path.get(old_path)
                if alias_hit is None:
                    continue
                old_cid, old_row = alias_hit
                if old_cid in used_alias_prior_cids:
                    continue
                prior = old_row
                prior_from_path_alias = True
                used_alias_prior_cids.add(old_cid)
                break
        if prior is None:
            row = {
                "claim_id": cid,
                "note_path": node["path"],
                "title": node["title"],
                "claim_type_author_hint_raw": node.get("claim_type_author_hint_raw"),
                "claim_type_author_hint": node.get("claim_type_author_hint"),
                "runner_path": node["runner_path"],
                "helper_runner_paths": node.get("helper_runner_paths", []),
                "deps": deps,
                "note_hash": node["note_hash"],
                "previous_audits": [],
            }
            for k, v in EMPTY_AUDIT.items():
                row[k] = v if not isinstance(v, (list, dict)) else (list(v) if isinstance(v, list) else dict(v))
            reset_prose_defaults(row)
            apply_claim_type_defaults(row, node, prior)
            seeded += 1
        else:
            row = dict(prior)
            row["claim_id"] = cid
            row["note_path"] = node["path"]
            row["title"] = node["title"]
            row["claim_type_author_hint_raw"] = node.get("claim_type_author_hint_raw")
            row["claim_type_author_hint"] = node.get("claim_type_author_hint")
            row["runner_path"] = node["runner_path"]
            row["helper_runner_paths"] = node.get("helper_runner_paths", [])
            row["deps"] = deps
            if prior_from_path_alias:
                row["note_hash"] = node["note_hash"]
                ensure_prose_defaults(row)
                migrated_path_aliases += 1
            elif (
                prior.get("note_hash") != node["note_hash"]
                and note_hash_change_is_path_alias_only(
                    node["path"],
                    prior.get("note_hash"),
                    alias_replacements,
                )
            ):
                row["note_hash"] = node["note_hash"]
                ensure_prose_defaults(row)
                migrated_path_aliases += 1
            elif prior.get("note_hash") != node["note_hash"] and prior.get("audit_status") in {None, "unaudited"}:
                row["note_hash"] = node["note_hash"]
                reset_prose_defaults(row)
                preserved += 1
            elif prior.get("note_hash") != node["note_hash"]:
                row = archive_prior_audit(row)
                row["note_hash"] = node["note_hash"]
                reset_prose_defaults(row)
                re_audit_required += 1
            else:
                ensure_prose_defaults(row)
                preserved += 1
            reset_unaudited_audit_fields(row)
            apply_claim_type_defaults(row, node, prior)
        row = rewrite_alias_strings(row, alias_replacements)
        out_rows[cid] = row

    for cid, row in archived_failed_rows.items():
        row.pop("current_status", None)
        row.pop("current_status_raw", None)
        current_hash = hash_existing_note_path(row.get("note_path"))
        if current_hash is not None:
            row["note_hash"] = current_hash
        if row.get("claim_type") not in CLAIM_TYPES:
            row["claim_type"] = "no_go"
            row["claim_type_provenance"] = "backfilled_from_archived_failed"
            row["claim_scope"] = row.get("claim_scope") or backfill_scope(row)
        ensure_prose_defaults(row)
        out_rows[cid] = row

    # Drop ledger rows whose source note no longer exists, plus rows
    # intentionally gated out as non-claim infrastructure.
    dropped = [
        cid
        for cid in existing_rows
        if cid not in included_cids and cid not in archived_failed_rows
    ]
    missing = [
        cid
        for cid in existing_rows
        if cid not in graph["nodes"] and cid not in archived_failed_rows
    ]

    return {
        "schema_version": 1,
        "stats": {
            "row_count": len(out_rows),
            "seeded_new": seeded,
            "preserved_existing": preserved,
            "migrated_path_aliases": migrated_path_aliases,
            "preserved_archived_failed": len(archived_failed_rows),
            "re_audit_required": re_audit_required,
            "dropped_missing_notes": len(missing),
            "dropped_gated_sources": len(gated),
            "dropped_total": len(dropped),
        },
        "rows": out_rows,
    }


def main() -> int:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    ledger = seed()
    LEDGER_PATH.write_text(json.dumps(ledger, indent=2, sort_keys=True) + "\n")
    s = ledger["stats"]
    print(f"Wrote {LEDGER_PATH.relative_to(REPO_ROOT)}")
    print(f"  rows: {s['row_count']}")
    print(f"  newly seeded: {s['seeded_new']}")
    print(f"  preserved (audit kept): {s['preserved_existing']}")
    print(f"  migrated path aliases: {s['migrated_path_aliases']}")
    print(f"  preserved archived failed: {s['preserved_archived_failed']}")
    print(f"  re-audit required (hash changed): {s['re_audit_required']}")
    print(f"  dropped (note removed): {s['dropped_missing_notes']}")
    print(f"  dropped (gated source): {s['dropped_gated_sources']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
