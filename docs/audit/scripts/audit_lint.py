#!/usr/bin/env python3
"""Lint the audit ledger for consistency.

Checks (all hard rules from FRESH_LOOK_REQUIREMENTS.md and README.md):

  1. Schema:
     - Every row has the expected fields.
     - audit_status is one of the allowed enum values.
     - claim_type is one of the auditor-owned allowed enum values.
     - legacy source-status fields are absent from generated audit data.

  2. The hard rules:
     - audit_status = audited_clean requires auditor and auditor_family set.
     - audit_status = audited_clean promotes only through claim_type:
       positive_theorem -> retained, no_go -> retained_no_go, and
       bounded_theorem -> retained_bounded, provided the dependency chain is
       already retained-grade.
     - effective_status in a retained-grade bucket requires audit_status =
       audited_clean (or archived audited_failed for legacy retained_no_go)
       AND every dep's effective_status is retained-grade or an accepted
       premise. Tier-A derivation-target premises bound dependents to
       retained_bounded until retired.
     - effective_status = retained_no_go has two paths:
       (a) claim_type = no_go and audit_status = audited_clean ratifies it.
       (b) audit_status = audited_failed AND the note has been moved to
           archive_unlanded/ (legacy path).
       Both paths represent ratified negative results, not active failures.
     - independence = 'weak' cannot land audited_clean. Critical clean
       confirmations must be cross-family, strong/external, or same-family
       fresh_context from a distinct restricted-input session.
     - note_hash on row must equal current note hash on disk.

  3. Graph health:
     - No dangling deps.
     - Cycles reported (notice, not failure).
     - Orphaned ledger rows (no source note) reported.

Exit code 0 if clean, 1 if any error-level issue found. Lint warnings are
reserved for mechanically actionable metadata problems. Audit-backlog items
that require a real re-audit are reported as notices so strict lint stays
useful without implying those rows can be mechanically repaired.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import premise_nodes

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = REPO_ROOT / "docs" / "audit" / "data"
LEDGER_PATH = DATA_DIR / "audit_ledger.json"
GRAPH_PATH = DATA_DIR / "citation_graph.json"
AUDIT_DISPATCH_QUEUE_PATH = DATA_DIR / "audit_dispatch_queue.json"
TIER_A_ADMISSIONS_PATH = DATA_DIR / "tier_a_admissions.json"

ALLOWED_AUDIT_STATUSES = {
    "unaudited",
    "audit_in_progress",
    "audited_clean",
    "audited_renaming",
    "audited_conditional",
    "audited_decoration",
    "audited_failed",
    "audited_numerical_match",
}
ALLOWED_CLAIM_TYPES = {
    "positive_theorem",
    "bounded_theorem",
    "no_go",
    "open_gate",
    "decoration",
    "meta",
    None,
}
RETAINED_GRADES = {"retained", "retained_no_go", "retained_bounded"}


def is_retained_grade(status):
    """Mirror compute_effective_status.is_retained_grade: literal retained-grade
    keywords plus `decoration_under_<parent>` (which is only assigned when the
    parent is itself retained-grade)."""
    if status in RETAINED_GRADES:
        return True
    if isinstance(status, str) and status.startswith("decoration_under_"):
        return True
    return False


def is_chain_satisfying_status(status):
    """Mirror compute_effective_status.is_chain_satisfying_status.

    Metadata rows can satisfy theorem/no-go dependency closure as stable audit
    context, but they are not retained-grade theorem support and do not satisfy
    decoration-parent retention.
    """
    return status == "meta" or is_retained_grade(status)


ALLOWED_EFFECTIVE_STATUSES = {
    "retained",
    "retained_no_go",
    "retained_bounded",
    "retained_pending_chain",
    "open_gate",
    "unaudited",
    "audit_in_progress",
    "meta",
    "audited_decoration",
    "audited_numerical_match",
    "audited_renaming",
    "audited_conditional",
    "audited_failed",
}
ALLOWED_INDEPENDENCE = {"weak", "fresh_context", "cross_family", "strong", "external", "judicial_review", None}
DEPRECATED_LEDGER_FIELDS = {"current_status", "current_status_raw"}

# Vocabulary-drift status, orthogonal to audit_status. See
# docs/repo/VOCABULARY_HYGIENE_DESIGN.md and
# docs/repo/controlled_vocabulary.yaml. prose_status records whether the
# source note's vocabulary is compliant; it does NOT factor into
# effective_status (physics ≠ prose orthogonality invariant).
ALLOWED_PROSE_STATUS = {
    "clean",
    "auto_corrected",
    "needs_human_vocab_decision",
    "not_evaluated_pre_vocab_lint",
    "queue_backpressure_exceeded",
    None,  # legacy rows pre-Cleanup-1 backfill
}

# Repair classes that audited_conditional / audited_renaming rows must prefix
# in notes_for_re_audit_if_any (per docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md).
ALLOWED_REPAIR_CLASSES = {
    "missing_dependency_edge",
    "dependency_not_retained",
    "missing_bridge_theorem",
    "scope_too_broad",
    "runner_artifact_issue",
    "compute_required",
    "other",
}

# Boilerplate scope written by seed_audit_ledger.backfill_scope when the
# auditor never supplied a real scope. Terminal verdicts must replace this
# with a real claim_scope; the lint flags rows that still carry it.
BACKFILL_SCOPE_PREFIX = (
    "Legacy audit row backfilled during scope-aware classification migration"
)

# Canonical auditor families. Anything outside this set is a lint warning;
# legacy strings (codex-current, codex-fresh, codex-fresh-agent, codex-fresh-context)
# are accepted as known-legacy and produce a migration warning rather than a hard
# error so the queue stays open while a one-time migration script normalises them.
CANONICAL_AUDITOR_FAMILIES = {
    # Codex GPT models (current and future): codex-gpt-<version>
    "codex-gpt-5",
    "codex-gpt-5.5",
    "codex-gpt-5.6",
    "codex-gpt-5.7",
    "codex-gpt-6",
    # Other model families
    "claude-opus",
    "claude-sonnet",
    "human",
    "external",
    # Legacy archival summary rows produced by apply_audit's
    # legacy_clean_consensus_summary (collapsed pre-PR291 cross-confirmations).
    "legacy-confirmed-clean",
}
LEGACY_AUDITOR_FAMILIES = {
    "codex-current",
    "codex-fresh",
    "codex-fresh-agent",
    "codex-fresh-context",
}

# audit_status values that are terminal verdicts (not pending/in-progress).
TERMINAL_VERDICTS = {
    "audited_clean",
    "audited_renaming",
    "audited_conditional",
    "audited_decoration",
    "audited_failed",
    "audited_numerical_match",
}

SUPPORTED_DISPATCH_SCHEMAS = {"promotion_reaudit_queue.v1"}

_CODEX_FAMILY_RE = re.compile(r"^codex-gpt-(\d+(?:\.\d+)*)$")


def codex_family_meets_minimum(family: str, minimum: str = "gpt-5.5") -> bool:
    """True iff a codex-gpt family label meets the audit-lane model floor."""
    if not isinstance(family, str) or not family.startswith("codex-gpt-"):
        return True
    fam_match = _CODEX_FAMILY_RE.match(family)
    if not fam_match:
        return True
    min_match = re.match(r"gpt-(\d+(?:\.\d+)*)", minimum)
    if not min_match:
        return True
    fam_rank = tuple(int(part) for part in fam_match.group(1).split("."))
    min_rank = tuple(int(part) for part in min_match.group(1).split("."))
    width = max(len(fam_rank), len(min_rank))
    fam_padded = fam_rank + (0,) * (width - len(fam_rank))
    min_padded = min_rank + (0,) * (width - len(min_rank))
    return fam_padded >= min_padded


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def hash_note_on_disk(note_path_str: str) -> str | None:
    p = REPO_ROOT / note_path_str
    if not p.exists():
        return None
    return hashlib.sha256(p.read_text(encoding="utf-8", errors="replace").encode("utf-8")).hexdigest()


def dispatch_sidecars() -> list[Path]:
    """Machine-readable dispatcher manifests that must feed audit_dispatch_queue."""
    candidates: list[Path] = []
    for pattern in ("*reaudit_queue*.json", "*dispatch_queue*.json"):
        candidates.extend(DATA_DIR.glob(pattern))
    excluded = {"audit_dispatch_queue.json", "audit_queue.json", "reaudit_candidates.json"}
    return sorted({p for p in candidates if p.name not in excluded})


def dispatch_target_live(target: dict, rows: dict[str, dict]) -> bool:
    row = rows.get(target.get("claim_id"))
    if row is None:
        return False
    expected = {
        "claim_type": target.get("current_claim_type"),
        "audit_status": target.get("current_audit_status"),
        "effective_status": target.get("current_effective_status"),
    }
    return all(expected[k] in {None, row.get(k)} for k in expected)


def main() -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--strict", action="store_true", help="Accepted for compatibility; lint is strict by default.")
    args, _ = p.parse_known_args()

    if not LEDGER_PATH.exists():
        print("FAIL: audit_ledger.json missing", file=sys.stderr)
        return 1
    ledger = load_json(LEDGER_PATH)
    graph = load_json(GRAPH_PATH) if GRAPH_PATH.exists() else None
    rows = ledger.get("rows", {})

    errors: list[str] = []
    warnings: dict[str, list[str]] = defaultdict(list)
    notices: dict[str, list[str]] = defaultdict(list)

    def add_warning(category: str, message: str) -> None:
        warnings[category].append(message)

    def add_notice(category: str, message: str) -> None:
        notices[category].append(message)

    if TIER_A_ADMISSIONS_PATH.exists():
        try:
            tier_a = load_json(TIER_A_ADMISSIONS_PATH)
        except Exception as exc:
            errors.append(f"tier_a_admissions.json could not be parsed: {exc}")
            tier_a = {}
        derivation_targets = tier_a.get("derivation_targets") or {}
        conventions = tier_a.get("conventions") or {}
        expected_ids = set(derivation_targets)
        listed_ids = set(tier_a.get("canonical_ids") or [])
        if listed_ids != expected_ids:
            errors.append(
                "tier_a_admissions.json canonical_ids must equal "
                "derivation_targets; conventions are survey metadata, not "
                "accepted premises"
            )
        admitted_count = tier_a.get("genuine_admitted_input_count")
        if admitted_count is not None and admitted_count != len(derivation_targets):
            errors.append(
                "tier_a_admissions.json genuine_admitted_input_count must equal "
                "derivation_targets; conventions and reclassified primitives "
                "are not admitted inputs"
            )
        for dep_id, entry in sorted(derivation_targets.items()):
            if dep_id not in rows:
                errors.append(f"tier_a_admissions.json derivation target {dep_id!r} has no ledger row")
            portfolio = entry.get("no_go_portfolio") or []
            if not portfolio:
                errors.append(f"tier_a_admissions.json derivation target {dep_id!r} lacks no_go_portfolio")
            for witness_id in portfolio:
                witness = rows.get(witness_id)
                if witness is None:
                    errors.append(
                        f"tier_a_admissions.json witness {witness_id!r} for {dep_id!r} "
                        "has no ledger row"
                    )
                elif witness.get("effective_status") != "retained_no_go":
                    errors.append(
                        f"tier_a_admissions.json witness {witness_id!r} for {dep_id!r} "
                        f"has effective_status={witness.get('effective_status')!r}, "
                        "expected 'retained_no_go'"
                    )
        for dep_id in sorted(conventions):
            if dep_id not in rows:
                errors.append(f"tier_a_admissions.json convention {dep_id!r} has no ledger row")

    # Top-level stale timestamp keys cause PR drift-gate noise and were
    # removed by f383ded3d. compute_effective_status now drops them
    # defensively on every run; this lint check guards against regression.
    STALE_TIMESTAMP_KEYS = {
        "generated_at",
        "effective_status_computed_at",
        "invalidation_run_at",
        "load_bearing_computed_at",
    }
    for k in STALE_TIMESTAMP_KEYS & set(ledger):
        errors.append(
            f"audit_ledger.json top-level: stale timestamp key {k!r} present "
            "(should be removed by compute_effective_status; rerun the pipeline)"
        )

    # Schema and hard-rule checks.
    for cid, row in rows.items():
        a = row.get("audit_status")
        e = row.get("effective_status")
        ct = row.get("claim_type")
        ind = row.get("independence")

        for field in DEPRECATED_LEDGER_FIELDS & set(row):
            errors.append(f"{cid}: deprecated ledger field {field!r} must not be present")
        if a not in ALLOWED_AUDIT_STATUSES:
            errors.append(f"{cid}: audit_status={a!r} not in allowed set")
        if ct not in ALLOWED_CLAIM_TYPES:
            errors.append(f"{cid}: claim_type={ct!r} not in allowed set")
        if e not in ALLOWED_EFFECTIVE_STATUSES and not (isinstance(e, str) and e.startswith("decoration_under_")):
            errors.append(f"{cid}: effective_status={e!r} not in allowed set")
        if a not in {None, "unaudited", "audit_in_progress"}:
            if ct is None:
                errors.append(f"{cid}: audited row requires claim_type")
            if not row.get("claim_scope"):
                errors.append(f"{cid}: audited row requires claim_scope")
            scope = row.get("claim_scope") or ""
            if scope.startswith(BACKFILL_SCOPE_PREFIX):
                add_notice(
                    "legacy_backfill_scope",
                    f"{cid}: terminal verdict {a!r} carries seeder backfill scope; "
                    "re-audit required to record a real claim_scope"
                )
        if row.get("claim_type_provenance") == "backfilled_pending_reaudit":
            add_notice(
                "legacy_claim_type_backfill",
                f"{cid}: claim_type was backfilled for a critical legacy audit; queue for re-audit"
            )
        if ind not in ALLOWED_INDEPENDENCE:
            errors.append(f"{cid}: independence={ind!r} not in allowed set")

        # Vocabulary-drift status (orthogonal to audit_status). Pre-Cleanup-1
        # rows may lack the field entirely; backfill_prose_status.py sets
        # them to not_evaluated_pre_vocab_lint. After backfill, every row
        # carries a value.
        if "prose_status" in row:
            ps = row["prose_status"]
            if ps not in ALLOWED_PROSE_STATUS:
                errors.append(
                    f"{cid}: prose_status={ps!r} not in {sorted(s for s in ALLOWED_PROSE_STATUS if s is not None)}"
                )
            pc = row.get("prose_corrections")
            if pc is not None and not isinstance(pc, list):
                errors.append(
                    f"{cid}: prose_corrections must be a list of "
                    "{rule_id, before, after} dicts (got "
                    f"{type(pc).__name__})"
                )
        else:
            add_notice(
                "prose_status_backfill_pending",
                f"{cid}: prose_status missing; run backfill_prose_status.py"
            )

        # Repair-class enforcement on audited_conditional / audited_renaming
        # rows (per docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md and README.md).
        # These terminal repairable verdicts must prefix
        # notes_for_re_audit_if_any with one of the seven allowed repair
        # classes so the repair lane is machine-sortable. Legacy rows lacking
        # the prefix queue for re-audit.
        if a in ("audited_conditional", "audited_renaming"):
            notes = row.get("notes_for_re_audit_if_any") or ""
            prefix_tokens = notes.strip().split(":", 1)[0].strip().split()
            first_token = prefix_tokens[0].lower() if prefix_tokens else ""
            if first_token not in ALLOWED_REPAIR_CLASSES:
                add_warning(
                    "conditional_repair_prefix",
                    f"{cid}: {a} notes_for_re_audit_if_any must start with one of "
                    f"{sorted(ALLOWED_REPAIR_CLASSES)} (got {first_token!r}); re-audit required"
                )

        # Auditor-family canonicalization. Hard-error on unknown strings.
        # Legacy strings produce a migration warning.
        fam = row.get("auditor_family")
        if a in TERMINAL_VERDICTS and fam is not None:
            if fam not in CANONICAL_AUDITOR_FAMILIES and fam not in LEGACY_AUDITOR_FAMILIES:
                # Tolerate codex-gpt-X.Y for any X.Y (forward-compat)
                if not (isinstance(fam, str) and fam.startswith("codex-gpt-")):
                    errors.append(
                        f"{cid}: auditor_family={fam!r} not in canonical set "
                        f"{sorted(CANONICAL_AUDITOR_FAMILIES)} or known-legacy "
                        f"{sorted(LEGACY_AUDITOR_FAMILIES)}"
                    )
            elif fam in LEGACY_AUDITOR_FAMILIES:
                add_warning(
                    "legacy_auditor_family",
                    f"{cid}: auditor_family={fam!r} is legacy; run "
                    "scripts/canonicalize_auditor_family.py migration"
                )
            elif (
                isinstance(fam, str)
                and fam.startswith("codex-gpt-")
                and not codex_family_meets_minimum(fam)
                and not row.get("previous_auditor_family")
            ):
                add_warning(
                    "codex_model_floor",
                    f"{cid}: auditor_family={fam!r} is below the audit-lane "
                    "minimum (gpt-5.5); model provenance is unverified, so "
                    "relabel with explicit operator confirmation or queue for re-audit"
                )

        # Claude-authored note rule (per FRESH_LOOK_REQUIREMENTS.md §1).
        # A note audited only by Claude — at any criticality — records
        # independence='weak' regardless of session restriction. Cross-family
        # confirmation by Codex/human/external is required for retained-grade
        # promotion.
        #
        # We surface this as a WARNING for now (not an error) because a
        # handful of legacy claude-only fresh_context audits exist on
        # leaf/medium rows. Per current lint these are already prevented
        # from landing as retained-grade on critical/high; the warning
        # surfaces them for migration. After all such legacy rows are
        # migrated to independence='weak' or re-audited by a non-Claude
        # auditor, this branch can be promoted to errors.append.
        if a == "audited_clean" and isinstance(fam, str) and fam.startswith("claude-"):
            if ind != "weak":
                xc = row.get("cross_confirmation") or {}
                xc_status = xc.get("status") if isinstance(xc, dict) else None
                other_side_non_claude = False
                if xc_status in {"confirmed", "third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
                    for key in ("first_audit", "second_audit", "third_audit"):
                        side = (xc.get(key) or {}) if isinstance(xc, dict) else {}
                        side_fam = side.get("auditor_family") or ""
                        if side_fam and not side_fam.startswith("claude-"):
                            other_side_non_claude = True
                            break
                if not other_side_non_claude:
                    add_warning(
                        "claude_independence",
                        f"{cid}: claude-only audited_clean should record independence='weak' "
                        "per FRESH_LOOK_REQUIREMENTS.md §1, or carry a non-Claude "
                        f"cross-confirmation; got independence={ind!r}, "
                        f"cross_confirmation_status={xc_status!r}"
                    )

        xc = row.get("cross_confirmation") or {}
        if isinstance(xc, dict) and xc.get("status") in {"third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
            xc_status = xc.get("status")
            expected_side = {
                "third_confirmed_first": "first",
                "third_confirmed_second": "second",
                "third_confirmed_hybrid": "hybrid",
            }[xc_status]
            first = xc.get("first_audit") or {}
            second = xc.get("second_audit") or {}
            winning = first if expected_side == "first" else second
            third = xc.get("third_audit") or {}
            if not third:
                errors.append(f"{cid}: {xc_status} requires third_audit")
            else:
                side = third.get("sided_with")
                if side is not None and side != expected_side:
                    errors.append(
                        f"{cid}: {xc_status} conflicts with third_audit.sided_with={side!r}"
                    )
                if (
                    expected_side != "hybrid"
                    and third.get("verdict")
                    and winning.get("verdict")
                    and third.get("verdict") != winning.get("verdict")
                ):
                    errors.append(
                        f"{cid}: {xc_status} third_audit verdict={third.get('verdict')!r} "
                        f"does not match winning audit {winning.get('verdict')!r}"
                    )
                if row.get("claim_type_provenance") == "judicial_review":
                    for key in ("verdict", "claim_type", "load_bearing_step_class"):
                        row_key = "audit_status" if key == "verdict" else key
                        if third.get(key) is not None and row.get(row_key) != third.get(key):
                            errors.append(
                                f"{cid}: judicial_review row {row_key}={row.get(row_key)!r} "
                                f"does not match third_audit {key}={third.get(key)!r}"
                            )

        if a == "audited_clean":
            if not row.get("auditor"):
                errors.append(f"{cid}: audited_clean requires non-empty auditor")
            if not row.get("auditor_family"):
                errors.append(f"{cid}: audited_clean requires auditor_family")
            expected = {
                "positive_theorem": "retained",
                "no_go": "retained_no_go",
                "bounded_theorem": "retained_bounded",
                "open_gate": "open_gate",
            }.get(ct)
            if expected is None:
                errors.append(
                    f"{cid}: audited_clean claim_type={ct!r} cannot become a retained-grade theorem"
                )
            elif e != expected:
                if e == "retained_pending_chain":
                    add_notice(
                        "pending_dependency_chain",
                        f"{cid}: audited_clean claim_type={ct!r} waiting on upstream retained-grade closure"
                    )
                else:
                    errors.append(
                        f"{cid}: audited_clean claim_type={ct!r} expected effective_status={expected!r} "
                        f"or 'retained_pending_chain', got {e!r}"
                    )
            # Criticality-aware independence rules.
            criticality = row.get("criticality") or "leaf"
            if criticality in {"critical", "high"} and ind == "weak":
                errors.append(
                    f"{cid}: criticality={criticality} requires independence != 'weak' for audited_clean"
                )
            if criticality == "critical":
                xc = row.get("cross_confirmation") or {}
                xc_status = xc.get("status")
                if xc_status not in {"confirmed", "third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
                    errors.append(
                        f"{cid}: critical claim requires confirmed cross-confirmation; "
                        f"got {xc_status!r}"
                    )
                else:
                    first = xc.get("first_audit") or {}
                    second = xc.get("second_audit") or {}
                    if first.get("auditor") and first.get("auditor") == second.get("auditor"):
                        errors.append(
                            f"{cid}: critical cross-confirmation reused auditor identity/session "
                            f"{second.get('auditor')!r}"
                        )
                    if (
                        first.get("auditor_family")
                        and first.get("auditor_family") == second.get("auditor_family")
                        and second.get("independence") != "fresh_context"
                    ):
                        errors.append(
                            f"{cid}: same-family critical cross-confirmation requires "
                            "second_audit.independence='fresh_context'"
                        )
                    if xc_status == "confirmed":
                        if first.get("claim_type") != second.get("claim_type"):
                            errors.append(
                                f"{cid}: critical cross-confirmation claim_type mismatch "
                                f"{first.get('claim_type')!r} vs {second.get('claim_type')!r}"
                            )
                        if first.get("load_bearing_step_class") != second.get("load_bearing_step_class"):
                            errors.append(
                                f"{cid}: critical cross-confirmation load_bearing_step_class mismatch "
                                f"{first.get('load_bearing_step_class')!r} vs "
                                f"{second.get('load_bearing_step_class')!r}"
                            )
                    if xc_status in {"third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
                        third = xc.get("third_audit") or {}
                        if not third:
                            errors.append(f"{cid}: {xc_status} requires third_audit")
                        elif third.get("auditor") in {first.get("auditor"), second.get("auditor")}:
                            errors.append(
                                f"{cid}: third audit reused auditor identity/session "
                                f"{third.get('auditor')!r}"
                            )
                        elif (
                            third.get("auditor_family")
                            and third.get("auditor_family")
                            in {first.get("auditor_family"), second.get("auditor_family")}
                            and third.get("independence") not in {"fresh_context", "judicial_review"}
                        ):
                            errors.append(
                                f"{cid}: same-family third audit requires "
                                "fresh_context or judicial_review independence"
                            )
                        else:
                            if xc_status == "third_confirmed_hybrid":
                                if third.get("sided_with") != "hybrid":
                                    errors.append(
                                        f"{cid}: third_confirmed_hybrid requires "
                                        f"third_audit.sided_with='hybrid'"
                                    )
                            else:
                                winning = first if xc_status == "third_confirmed_first" else second
                                for key in ("verdict", "claim_type", "load_bearing_step_class"):
                                    if third.get(key) != winning.get(key):
                                        errors.append(
                                            f"{cid}: {xc_status} third_audit {key}={third.get(key)!r} "
                                            f"does not match winning audit {winning.get(key)!r}"
                                        )

        if a == "audited_decoration":
            parent = row.get("decoration_parent_claim_id")
            if ct != "decoration":
                errors.append(f"{cid}: audited_decoration requires claim_type='decoration'")
            if not parent:
                msg = f"{cid}: audited_decoration requires decoration_parent_claim_id"
                if row.get("claim_type_provenance") == "backfilled_pending_reaudit":
                    add_notice(
                        "legacy_decoration_parent",
                        msg + "; legacy row queued for re-audit",
                    )
                else:
                    errors.append(msg)
            else:
                parent_eff = rows.get(parent, {}).get("effective_status")
                if not is_retained_grade(parent_eff):
                    add_notice(
                        "decoration_parent_not_retained",
                        f"{cid}: decoration parent {parent!r} is not retained-grade "
                        f"(effective_status={parent_eff!r})"
                    )

        # Criticality bump after audit (warn that re-audit may be needed).
        # Skip rows already at unaudited / audit_in_progress: the warning is
        # only meaningful for an ACTIVE audit verdict whose snapshot might be
        # stale relative to current criticality. Once the row has been reset
        # (e.g. via invalidate_stale_audits.py or note-hash drift), the
        # snapshot is just historical noise and shouldn't generate a warning.
        snap = row.get("audit_state_snapshot")
        if snap is not None and a not in {None, "unaudited", "audit_in_progress"}:
            crit_now = row.get("criticality") or "leaf"
            crit_at_audit = snap.get("criticality") or "leaf"
            crit_rank = {"leaf": 0, "medium": 1, "high": 2, "critical": 3}
            if crit_rank.get(crit_now, 0) > crit_rank.get(crit_at_audit, 0):
                # Mirror invalidate_stale_audits._categorize_criticality_bump
                # so lint and invalidate stay in sync. Three outcomes per
                # FRESH_LOOK_REQUIREMENTS §4:
                #   - meets:      no notice, no warning.
                #   - soft_reset: invalidate.py will move audited_clean ->
                #                 audit_in_progress + awaiting_cross_confirmation
                #                 on the next run. Notice (informational).
                #   - invalidate: audit fundamentally fails the new tier
                #                 (e.g. weak independence at high+). Warning.
                indep = row.get("independence")
                cc = row.get("cross_confirmation") or {}
                cc_status = cc.get("status") if isinstance(cc, dict) else None
                action = "noop"
                if a != "audited_clean":
                    action = "noop"  # terminal verdict, cross-conf doesn't apply
                elif indep is None or indep == "weak":
                    action = "invalidate"  # below independence floor at high+
                elif crit_now == "high":
                    action = "noop"
                elif crit_now == "critical":
                    if cc_status in {"confirmed", "third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
                        action = "noop"
                    else:
                        action = "soft_reset"
                if action == "invalidate":
                    add_warning(
                        "criticality_bumped",
                        f"{cid}: criticality bumped {crit_at_audit}->{crit_now} since audit; "
                        "audit fails new-tier independence floor — invalidate_stale_audits.py "
                        "will hard-reset"
                    )
                elif action == "soft_reset":
                    add_notice(
                        "criticality_bumped_to_critical_awaits_cc",
                        f"{cid}: criticality bumped {crit_at_audit}->{crit_now} since audit; "
                        "first-pass clean stays live, awaiting independent second auditor"
                    )

        # Hash drift.
        on_disk = hash_note_on_disk(row.get("note_path", ""))
        if on_disk is None:
            add_warning(
                "source_note_missing",
                f"{cid}: source note missing on disk: {row.get('note_path')}",
            )
        elif on_disk != row.get("note_hash"):
            # note_hash is a source-content hash, not a verdict. A mismatch means the
            # note was edited since the audit lane last seeded. For a RETAINED-grade row
            # this is a real integrity violation — current text laundered past a stale
            # ratification — so it stays a hard error and must be re-audited before
            # landing. For a NON-retained row (unaudited / audited_conditional / pending)
            # it only means re-audit is pending; per this lint's design (re-audit-required
            # items are notices so strict lint stays useful) and because the nightly
            # audit-lane re-seed refreshes the hash, it is a non-blocking notice — review
            # loops that edit such notes (e.g. formal-carrier repairs on conditional rows)
            # must not be forced to commit audit-lane ledger churn just to clear strict lint.
            msg = f"{cid}: note_hash mismatch — note edited since seeding; re-run seed_audit_ledger.py"
            if is_retained_grade(row.get("effective_status")):
                errors.append(
                    msg + " (RETAINED-grade row: an edited retained note must be re-audited, "
                    "not landed with a stale ratification)"
                )
            else:
                add_notice(
                    "note_hash_drift_reaudit_pending",
                    msg + " (non-retained row: re-audit pending; the audit-lane re-seed "
                    "refreshes the hash — not a strict-lint blocker)",
                )

        # Dangling deps.
        for d in row.get("deps", []):
            if d not in rows:
                add_warning(
                    "dangling_dependency",
                    f"{cid}: dangling dep {d!r} (no ledger row)",
                )

    # Effective-status propagation sanity. A retained-grade row's deps must
    # themselves be retained-grade, metadata context, or accepted premises.
    # Open gates and retained_pending_chain are explicit blockers, not support
    # for downstream theorem retention. Axioms can satisfy a dep without
    # bounding the row.
    # Tier-A derivation targets can satisfy a dep only at the bounded tier until
    # the target is retired by a retained derivation. Convention rows listed in
    # the Tier-A registry are not accepted premises.
    # Metadata deps are chain-satisfying context, not retained-grade theorem
    # support. `decoration_under_<parent>` deps count as retained-grade because
    # decoration_status() only assigns that status when the parent is itself
    # retained-grade.
    # Must stay in sync with compute_effective_status.py's clean_status.
    for cid, row in rows.items():
        if row.get("effective_status") in RETAINED_GRADES:
            for d in row.get("deps", []):
                if (
                    row.get("effective_status") != "retained_bounded"
                    and premise_nodes.is_admitted_derivation_target(d)
                ):
                    errors.append(
                        f"{cid}: effective_status={row.get('effective_status')!r} "
                        f"depends on Tier-A admitted derivation target {d!r}; "
                        "expected retained_bounded until the admission is retired"
                    )
                if premise_nodes.is_accepted_premise_dep(d):
                    continue
                d_eff = rows.get(d, {}).get("effective_status")
                if not is_chain_satisfying_status(d_eff):
                    errors.append(
                        f"{cid}: effective_status={row.get('effective_status')!r} but dep {d!r} "
                        f"has effective_status={d_eff!r}"
                    )

    # Dispatcher manifests are not evidence, but they must be visible to the
    # audit loop. If a sidecar contains live targets and the generated dispatch
    # queue omits them, the process has silently dropped a re-audit request.
    sidecars = dispatch_sidecars()
    if sidecars:
        dispatch_known_ids: set[str] = set()
        if AUDIT_DISPATCH_QUEUE_PATH.exists():
            try:
                dispatch = load_json(AUDIT_DISPATCH_QUEUE_PATH)
                # A target is "known to the dispatch queue" if it appears in
                # live OR resolved_targets OR retired OR resolved_or_invalid.
                # All four buckets represent the dispatch producer having seen
                # and classified the target; only targets that don't appear in
                # any bucket are silently dropped.
                for bucket in ("live", "resolved_targets", "retired", "resolved_or_invalid"):
                    for entry in dispatch.get(bucket, []):
                        cid = entry.get("claim_id")
                        if cid:
                            dispatch_known_ids.add(cid)
            except Exception as exc:  # pragma: no cover - defensive lint path
                add_warning(
                    "audit_dispatch_queue_invalid",
                    f"{AUDIT_DISPATCH_QUEUE_PATH.relative_to(REPO_ROOT)} could not be parsed: {exc}",
                )
        else:
            add_warning(
                "audit_dispatch_queue_missing",
                "dispatcher sidecar exists but docs/audit/data/audit_dispatch_queue.json is missing; "
                "run compute_audit_dispatch_queue.py or the full pipeline"
            )
        for path in sidecars:
            try:
                manifest = load_json(path)
            except Exception as exc:  # pragma: no cover - defensive lint path
                add_warning(
                    "audit_dispatch_sidecar_invalid",
                    f"{path.relative_to(REPO_ROOT)} could not be parsed: {exc}",
                )
                continue
            schema = manifest.get("schema")
            if schema not in SUPPORTED_DISPATCH_SCHEMAS:
                add_warning(
                    "audit_dispatch_sidecar_unsupported",
                    f"{path.relative_to(REPO_ROOT)} schema={schema!r} is not supported by "
                    "compute_audit_dispatch_queue.py"
                )
                continue
            for group in manifest.get("groups") or []:
                for target in group.get("targets") or []:
                    cid = target.get("claim_id")
                    if dispatch_target_live(target, rows) and cid not in dispatch_known_ids:
                        add_warning(
                            "audit_dispatch_queue_stale",
                            f"{path.relative_to(REPO_ROOT)} live target {cid!r} is missing from "
                            "audit_dispatch_queue.json (not present in live, resolved_targets, "
                            "retired, or resolved_or_invalid); rerun the full pipeline before "
                            "relying on audit-loop selection"
                        )

    # Graph health: cycles (informational).
    cycle_count = 0
    if graph:
        # Quick reachability-based cycle detection on the graph adjacency.
        adj = {c: list(n["deps"]) for c, n in graph["nodes"].items()}
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {c: WHITE for c in adj}
        for start in adj:
            if color[start] != WHITE:
                continue
            stack = [(start, iter(adj[start]))]
            color[start] = GRAY
            while stack:
                node, it = stack[-1]
                try:
                    nxt = next(it)
                except StopIteration:
                    color[node] = BLACK
                    stack.pop()
                    continue
                if nxt not in color:
                    continue
                if color[nxt] == GRAY:
                    cycle_count += 1
                    continue
                if color[nxt] == BLACK:
                    continue
                color[nxt] = GRAY
                stack.append((nxt, iter(adj[nxt])))
        if cycle_count:
            add_notice("graph_cycles", f"graph contains {cycle_count} back-edges (cycles)")

    # Output.
    def issue_count(groups: dict[str, list[str]]) -> int:
        return sum(len(items) for items in groups.values())

    def print_issue_groups(
        label: str,
        prefix: str,
        groups: dict[str, list[str]],
        max_items_per_group: int = 3,
    ) -> None:
        total = issue_count(groups)
        if not total:
            return
        print(f"  {total} {label}:")
        for category in sorted(groups):
            items = groups[category]
            print(f"    {category}: {len(items)}")
            for item in items[:max_items_per_group]:
                print(f"      {prefix}: {item}")
            if len(items) > max_items_per_group:
                print(f"      ... and {len(items) - max_items_per_group} more")

    print(f"audit_lint: {len(rows)} rows checked")
    print_issue_groups("warnings", "WARN", warnings)
    print_issue_groups("notices", "NOTICE", notices)
    if errors:
        print(f"  {len(errors)} errors:")
        for e in errors[:30]:
            print(f"    ERROR: {e}")
        if len(errors) > 30:
            print(f"    ... and {len(errors) - 30} more")
        return 1
    print("  OK: no errors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
