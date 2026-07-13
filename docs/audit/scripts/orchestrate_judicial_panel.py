#!/usr/bin/env python3
"""Run the audit-loop five-judge panel over cross-confirmation disagreements.

For each targeted disagreement row this renders the canonical restricted
packet, appends both recorded seat positions (tuple summaries plus their
invocation-bound full rationales), and launches five detached GPT-5.6-sol/xhigh
judges with distinct identities. Each judge votes on the full tuple

    (sided_with, ratified_verdict, ratified_claim_type,
     ratified_claim_scope, ratified_load_bearing_step_class,
     negative_assertion_classes)

and must explain the error in the position it votes against. A majority is
at least three matching full-tuple votes out of five (whitespace-only scope
differences and assertion-class ordering are equivalent). On majority, a
representative judicial JSON is applied through the standard serialized
gates (apply -> pipeline -> strict lint -> diff/scope check -> commit ->
push). Without an applyable majority, the panel record is written to the
workdir and a fresh five-judge panel is launched in the same loop with every
earlier vote and rationale in context, per the audit-loop skill.

Run only from a dedicated, clean ``main`` checkout.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import uuid
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import orchestrate_audit_batch as batch  # noqa: E402

audit_runner = batch.audit_runner
REPO_ROOT = batch.REPO_ROOT

PANEL_SIZE = 5
MAJORITY = 3
MIN_VOTE_BYTES = 120

ALLOWED_SIDES = {"first", "second", "hybrid", "neither"}
ALLOWED_VERDICTS = {
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
}

VOTE_FIELDS = (
    "sided_with",
    "ratified_verdict",
    "ratified_claim_type",
    "ratified_claim_scope",
    "ratified_load_bearing_step_class",
    "negative_assertion_classes",
    "judgment_rationale",
    "first_auditor_error",
    "second_auditor_error",
)

SEAT_ARGUMENT_FIELDS = (
    "verdict",
    "claim_type",
    "claim_scope",
    "load_bearing_step_class",
    "negative_assertion_classes",
    "load_bearing_step",
    "chain_closes",
    "chain_closure_explanation",
    "runner_check_breakdown",
    "open_dependency_paths",
    "decoration_parent_claim_id",
    "no_go_discipline",
    "independence",
    "auditor",
    "auditor_family",
    "auditor_model",
    "auditor_reasoning_effort",
    "audit_invocation_id",
)


def norm_scope(value: str) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip())


def vote_tuple(vote: dict) -> tuple:
    classes = vote.get("negative_assertion_classes")
    classes_key = tuple(sorted(classes)) if isinstance(classes, list) else ("<invalid>",)
    return (
        vote.get("sided_with"),
        vote.get("ratified_verdict"),
        vote.get("ratified_claim_type"),
        norm_scope(vote.get("ratified_claim_scope") or ""),
        vote.get("ratified_load_bearing_step_class"),
        classes_key,
    )


def disagreement_fingerprint(row: dict) -> dict:
    """Bind panel history to the exact source and two recorded seats."""
    cross = row.get("cross_confirmation") or {}
    first = copy.deepcopy(cross.get("first_audit") or {})
    second = copy.deepcopy(cross.get("second_audit") or {})
    seat_payload = json.dumps(
        {"first_audit": first, "second_audit": second},
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    return {
        "schema": "judicial_disagreement_fingerprint_v1",
        "claim_id": row.get("claim_id"),
        "note_hash": row.get("note_hash"),
        "first_audit_invocation_id": first.get("audit_invocation_id"),
        "second_audit_invocation_id": second.get("audit_invocation_id"),
        "seat_summaries_sha256": hashlib.sha256(
            seat_payload.encode("utf-8")
        ).hexdigest(),
    }


def vote_schema_error(vote: object) -> str | None:
    if not isinstance(vote, dict):
        return "vote must be a JSON object"
    missing = [field for field in VOTE_FIELDS if field not in vote]
    if missing:
        return f"vote_missing_fields:{','.join(missing)}"
    if vote.get("sided_with") not in ALLOWED_SIDES:
        return "vote has invalid sided_with"
    if vote.get("ratified_verdict") not in ALLOWED_VERDICTS:
        return "vote has invalid ratified_verdict"
    if vote.get("ratified_claim_type") not in ALLOWED_CLAIM_TYPES:
        return "vote has invalid ratified_claim_type"
    for field in (
        "ratified_claim_scope",
        "ratified_load_bearing_step_class",
        "judgment_rationale",
        "first_auditor_error",
        "second_auditor_error",
    ):
        if not isinstance(vote.get(field), str) or not vote[field].strip():
            return f"vote field {field} must be a non-empty string"
    declared = vote.get("negative_assertion_classes")
    if not isinstance(declared, list) or not all(
        isinstance(item, str) and item.strip() for item in declared
    ):
        return "negative_assertion_classes must be a list of non-empty strings"
    for field in (
        "hybrid_resolution_note",
        "ratified_decoration_parent_claim_id",
        "ratified_load_bearing_step",
        "notes_for_re_audit_if_any",
    ):
        if field in vote and vote[field] is not None and not isinstance(vote[field], str):
            return f"vote field {field} must be a string or null"
    if "no_go_discipline" in vote and vote["no_go_discipline"] is not None:
        if not isinstance(vote["no_go_discipline"], dict):
            return "no_go_discipline must be an object or null"
    first_error = str(vote.get("first_auditor_error") or "").strip().lower()
    second_error = str(vote.get("second_auditor_error") or "").strip().lower()
    if vote.get("sided_with") == "first" and second_error == "none":
        return "a first-sided vote must explain the second auditor's error"
    if vote.get("sided_with") == "second" and first_error == "none":
        return "a second-sided vote must explain the first auditor's error"
    if vote.get("sided_with") in {"hybrid", "neither"} and (
        first_error == "none" or second_error == "none"
    ):
        return (
            f"a {vote.get('sided_with')}-sided vote must explain both "
            "auditors' errors"
        )
    return None


def sided_vote_context_error(row: dict, vote: dict) -> str | None:
    """Reject a sided vote that changes the selected seat's full tuple."""
    side = vote.get("sided_with")
    if side not in {"first", "second"}:
        return None
    chosen = ((row.get("cross_confirmation") or {}).get(f"{side}_audit") or {})
    comparisons = (
        ("verdict", vote.get("ratified_verdict"), chosen.get("verdict")),
        ("claim_type", vote.get("ratified_claim_type"), chosen.get("claim_type")),
        (
            "claim_scope",
            norm_scope(vote.get("ratified_claim_scope") or ""),
            norm_scope(chosen.get("claim_scope") or ""),
        ),
        (
            "load_bearing_step_class",
            vote.get("ratified_load_bearing_step_class"),
            chosen.get("load_bearing_step_class"),
        ),
        (
            "negative_assertion_classes",
            tuple(sorted(vote.get("negative_assertion_classes") or [])),
            tuple(sorted(chosen.get("negative_assertion_classes") or [])),
        ),
    )
    mismatches = [name for name, actual, expected in comparisons if actual != expected]
    if mismatches:
        return (
            f"{side}-sided vote changes selected seat tuple fields: "
            f"{','.join(mismatches)}; use sided_with='hybrid' for corrections"
        )
    return None


def archived_rationale(row: dict, invocation_id: str) -> str:
    if not invocation_id:
        return (
            "[seat summary has no audit_invocation_id; no invocation-bound "
            "archived rationale is available]"
        )
    for archived in reversed(row.get("previous_audits") or []):
        if not isinstance(archived, dict):
            continue
        if invocation_id and archived.get("audit_invocation_id") == invocation_id:
            rationale = str(archived.get("verdict_rationale") or "")
            notes = str(archived.get("notes_for_re_audit_if_any") or "")
            return rationale + (f"\n[re-audit notes] {notes}" if notes else "")
    return (
        "[no archived rationale found for this seat's invocation id "
        f"{invocation_id}]"
    )


def seat_rationale(summary: dict, row: dict) -> str:
    rationale = str(summary.get("verdict_rationale") or "")
    notes = str(summary.get("notes_for_re_audit_if_any") or "")
    if rationale:
        return rationale + (f"\n[re-audit notes] {notes}" if notes else "")
    return archived_rationale(row, str(summary.get("audit_invocation_id") or ""))


def seat_context_error(row: dict) -> str | None:
    cross = row.get("cross_confirmation") or {}
    for label in ("first_audit", "second_audit"):
        summary = cross.get(label) or {}
        if not summary:
            return f"{label} summary is missing"
        if str(summary.get("verdict_rationale") or "").strip():
            continue
        invocation_id = str(summary.get("audit_invocation_id") or "")
        matched = next(
            (
                archived
                for archived in reversed(row.get("previous_audits") or [])
                if isinstance(archived, dict)
                and invocation_id
                and archived.get("audit_invocation_id") == invocation_id
                and str(archived.get("verdict_rationale") or "").strip()
            ),
            None,
        )
        if matched is None:
            return (
                f"{label} has no invocation-bound full rationale; rerun the "
                "cross-confirmation seats under the rationale-preserving apply contract"
            )
    return None


def seat_block(label: str, summary: dict, row: dict) -> str:
    lines = [f"=== BEGIN {label.upper()} POSITION ==="]
    for field in SEAT_ARGUMENT_FIELDS:
        if field not in {"verdict_rationale", "notes_for_re_audit_if_any"}:
            lines.append(f"{field}: {json.dumps(summary.get(field))}")
    lines.append("full rationale:")
    lines.append(seat_rationale(summary, row))
    lines.append(f"=== END {label.upper()} POSITION ===")
    return "\n".join(lines)


def panel_instructions(
    judge_no: int,
    judge_identity: str,
    panel_no: int,
    prior_panels: list[dict],
) -> str:
    prior_block = ""
    if prior_panels:
        prior_block = (
            "\n### Prior panel outcomes\n\n"
            "Earlier five-judge panels on this same disagreement produced the\n"
            "complete vote/rationale breakdowns below but no applyable majority.\n"
            "Weigh their arguments; you are not bound by them.\n\n"
            + json.dumps(prior_panels, indent=1, sort_keys=True)
            + "\n"
        )
    return f"""
### JUDICIAL PANEL ROUND {panel_no}, SEAT {judge_no} OF {PANEL_SIZE}

Your distinct judicial identity is `{judge_identity}`. It is unique to this
seat and will be recorded with your vote.

The two independent audit seats above DISAGREE. You are one judge on a
five-judge panel resolving the disagreement. Judge ONLY from the restricted
packet plus the two recorded positions. Do not search anything else.
{prior_block}
Return EXACTLY ONE JSON object and nothing else:

{{
  "sided_with": "<first|second|hybrid|neither>",
  "ratified_verdict": "<audited_clean|audited_renaming|audited_conditional|audited_decoration|audited_failed|audited_numerical_match>",
  "ratified_claim_type": "<positive_theorem|bounded_theorem|no_go|open_gate|decoration|meta>",
  "ratified_claim_scope": "<the exact scope sentence you ratify>",
  "ratified_load_bearing_step": null,
  "ratified_load_bearing_step_class": "<A|B|C|D|E|F|G exactly as the seats use>",
  "negative_assertion_classes": [],
  "judgment_rationale": "<why the ratified tuple is correct, grounded in the packet>",
  "first_auditor_error": "<the specific error in the first position, or 'none' if you side with it entirely>",
  "second_auditor_error": "<the specific error in the second position, or 'none' if you side with it entirely>",
  "hybrid_resolution_note": null,
  "ratified_decoration_parent_claim_id": null,
  "notes_for_re_audit_if_any": null,
  "no_go_discipline": null
}}

Rules: vote the FULL tuple; a factual check against the packet (for
example whether the runner computes a contested quantity) outweighs either
seat's characterization. If sided_with is `first` or `second`, you MUST copy
that seat's verdict, claim_type, claim_scope (character-for-character),
load_bearing_step_class, negative_assertion_classes, decoration parent, and
No-Go Discipline declaration/packet; any substantive correction MUST use
`hybrid`. A hybrid MUST give a novel explicit scope and a non-empty
hybrid_resolution_note. Use `neither` only when neither original position nor
an applyable hybrid is sufficient; still vote a complete conservative tuple.
Replace the null optional values with the exact sided seat values when present.
For a hybrid or neither vote, supply the complete load-bearing step, decoration
parent, repair note, and N1-N8 object whenever the chosen tuple requires them.
Declare negative_assertion_classes honestly for the tuple you ratify. A first-
sided vote MUST explain the second auditor's error; a second-sided vote MUST
explain the first auditor's error; a hybrid or neither vote MUST explain errors
in both original positions.
"""


def render_panel_packet(
    row: dict,
    rows: dict[str, dict],
    runner_timeout: int,
) -> tuple[str, dict[str, dict], str]:
    template = audit_runner.PROMPT_TEMPLATE_PATH.read_text(encoding="utf-8")
    evidence_manifest: dict[str, dict] = {}
    invocation_id = uuid.uuid4().hex
    packet = audit_runner.render_prompt(
        row,
        rows,
        template,
        runner_timeout,
        use_cache=False,
        evidence_manifest_out=evidence_manifest,
        audit_invocation_id=invocation_id,
    )
    return packet, evidence_manifest, invocation_id


def render_judge_prompt(
    packet: str,
    row: dict,
    judge_no: int,
    judge_identity: str,
    panel_no: int,
    prior_panels: list[dict],
) -> str:
    cross = row.get("cross_confirmation") or {}
    first = cross.get("first_audit") or {}
    second = cross.get("second_audit") or {}
    return "\n\n".join(
        [
            packet,
            seat_block("first_audit", first, row),
            seat_block("second_audit", second, row),
            panel_instructions(judge_no, judge_identity, panel_no, prior_panels),
        ]
    )


def launch_judge(
    packet: str,
    row: dict,
    judge_no: int,
    panel_no: int,
    workdir: Path,
    prior_panels: list[dict],
    invocation_id: str,
    evidence_manifest: dict[str, dict],
) -> dict:
    cid = row["claim_id"]
    key = batch.artifact_key(cid)
    judge_identity = (
        f"codex-judicial-{judge_no}-"
        f"{datetime.now(timezone.utc).strftime('%Y%m%d')}-{uuid.uuid4().hex[:8]}"
    )
    prompt = render_judge_prompt(
        packet, row, judge_no, judge_identity, panel_no, prior_panels
    )
    if len(prompt) > audit_runner.CODEX_INPUT_CHAR_LIMIT:
        raise ValueError(
            f"{cid}: judicial packet is {len(prompt)} characters; narrow the "
            "packet rather than converting transport size into a verdict"
        )
    tag = f"{key}-panel{panel_no}-judge{judge_no}"
    isolated = workdir / f"isolated-{tag}"
    isolated.mkdir(parents=True, exist_ok=False)
    (isolated / "PANEL_TASK.md").write_text(prompt, encoding="utf-8")
    raw_output = workdir / f"raw-{tag}.txt"
    log_path = workdir / f"log-{tag}.txt"
    log_handle = log_path.open("w", encoding="utf-8")
    instruction = (
        "Open PANEL_TASK.md in the current directory and follow it exactly. "
        "It contains the complete restricted packet, both recorded audit "
        "positions, and your panel-seat instructions. Do not inspect any "
        "other file. Return only the single JSON vote object it requires."
    )
    try:
        proc = subprocess.Popen(
            [
                "codex", "exec", "--skip-git-repo-check", "--ignore-rules",
                "--sandbox", "read-only", "--model", batch.MODEL,
                "-c", f"model_reasoning_effort='{batch.REASONING}'",
                "--output-last-message", str(raw_output), instruction,
            ],
            stdin=subprocess.DEVNULL,
            stdout=log_handle,
            stderr=log_handle,
            cwd=isolated,
            start_new_session=True,
        )
    except Exception:
        log_handle.close()
        raise
    now = time.monotonic()
    return {
        "cid": cid,
        "pass": judge_no,
        "judge": judge_no,
        "proc": proc,
        "raw_output": raw_output,
        "log_path": log_path,
        "log_handle": log_handle,
        "isolated": isolated,
        "auditor": judge_identity,
        "panel": panel_no,
        "invocation_id": invocation_id,
        "evidence_manifest": evidence_manifest,
        "last_size": 0,
        "last_progress": now,
        "stalled": False,
        "returncode": None,
    }


def collect_vote(job: dict) -> tuple[dict | None, str]:
    if job["stalled"]:
        return None, "stall_killed"
    raw = job["raw_output"]
    if job.get("returncode") != 0:
        return None, f"judge_exit_{job.get('returncode')}"
    if not raw.exists() or raw.stat().st_size <= MIN_VOTE_BYTES:
        return None, "no_size_qualified_vote"
    reply = audit_runner.extract_response(raw.read_text(encoding="utf-8"))
    vote = audit_runner.parse_verdict_json(reply or "")
    if vote is None:
        return None, "malformed_vote_json"
    schema_error = vote_schema_error(vote)
    if schema_error:
        return None, schema_error
    return vote, "ok"


def public_vote(vote: dict) -> dict:
    return {
        "judge": vote.get("_panel_judge"),
        "auditor": vote.get("_panel_auditor"),
        **{key: value for key, value in vote.items() if not key.startswith("_")},
    }


def judicial_blob(
    row: dict,
    representative: dict,
    votes: list[dict],
    majority: int,
    invocation_id: str | None = None,
) -> dict:
    context_error = sided_vote_context_error(row, representative)
    if context_error:
        raise ValueError(context_error)
    if representative.get("sided_with") == "neither":
        raise ValueError(
            "a neither majority must be recorded and sent to a fresh panel, "
            "not converted into judicial apply JSON"
        )
    breakdown = [
        {
            "judge": vote.get("_panel_judge", index + 1),
            "auditor": vote.get("_panel_auditor"),
            "tuple": list(vote_tuple(vote)[:5]) + [list(vote_tuple(vote)[5])],
            "rationale": str(vote.get("judgment_rationale") or "")[:600],
        }
        for index, vote in enumerate(votes)
    ]
    rationale = (
        f"Five-judge panel majority ({majority}/{PANEL_SIZE} matching full "
        "tuples) resolved the cross-confirmation disagreement. "
        f"Representative rationale: {representative.get('judgment_rationale')}"
        f"\n[panel breakdown] {json.dumps(breakdown, sort_keys=True)}"
    )
    side = representative.get("sided_with")
    cross = row.get("cross_confirmation") or {}
    chosen = (
        (cross.get(f"{side}_audit") or {})
        if side in {"first", "second"}
        else {}
    )

    if chosen:
        ratified_verdict = chosen.get("verdict")
        ratified_claim_type = chosen.get("claim_type")
        ratified_scope = chosen.get("claim_scope")
        ratified_class = chosen.get("load_bearing_step_class")
        negative_classes = chosen.get("negative_assertion_classes")
    else:
        ratified_verdict = representative.get("ratified_verdict")
        ratified_claim_type = representative.get("ratified_claim_type")
        ratified_scope = representative.get("ratified_claim_scope")
        ratified_class = representative.get("ratified_load_bearing_step_class")
        negative_classes = representative.get("negative_assertion_classes")

    blob = {
        "claim_id": row["claim_id"],
        "third_auditor": representative.get("_panel_auditor") or (
            f"codex-judicial-panel-"
            f"{datetime.now(timezone.utc).strftime('%Y%m%d')}-{uuid.uuid4().hex[:8]}"
        ),
        "auditor_family": batch.AUDITOR_FAMILY,
        "auditor_model": batch.MODEL,
        "auditor_reasoning_effort": batch.REASONING,
        "independence": "judicial_review",
        "audit_invocation_id": invocation_id or uuid.uuid4().hex,
        "sided_with": side,
        "ratified_verdict": ratified_verdict,
        "ratified_claim_type": ratified_claim_type,
        "ratified_claim_scope": ratified_scope,
        "ratified_load_bearing_step_class": ratified_class,
        "negative_assertion_classes": negative_classes,
        "judgment_rationale": rationale,
        "first_auditor_error": representative.get("first_auditor_error"),
        "second_auditor_error": representative.get("second_auditor_error"),
    }
    optional_sources = (chosen, representative) if chosen else (representative,)
    for source in optional_sources:
        if source.get("load_bearing_step"):
            blob["ratified_load_bearing_step"] = source["load_bearing_step"]
            break
    for source in optional_sources:
        if "notes_for_re_audit_if_any" in source:
            blob["notes_for_re_audit_if_any"] = source.get(
                "notes_for_re_audit_if_any"
            )
            break
    for source in optional_sources:
        parent = source.get("decoration_parent_claim_id") or source.get(
            "ratified_decoration_parent_claim_id"
        )
        if parent:
            blob["ratified_decoration_parent_claim_id"] = parent
            break
    for source in optional_sources:
        if isinstance(source.get("no_go_discipline"), dict):
            blob["no_go_discipline"] = copy.deepcopy(source["no_go_discipline"])
            break
    if side == "hybrid":
        blob["hybrid_resolution_note"] = (
            representative.get("hybrid_resolution_note")
            or representative.get("judgment_rationale")
        )
    return blob


def judicial_applyability_error(
    blob: dict,
    rows: dict[str, dict],
    evidence_manifest: dict[str, dict],
    workdir: Path,
) -> str | None:
    """Run the exact apply validator on a detached ledger before writing JSON."""
    import apply_audit as audit_apply

    envelope_path = workdir / (
        f"candidate-manifest-{batch.artifact_key(blob['claim_id'])}-"
        f"{blob['audit_invocation_id']}.json"
    )
    envelope_path.write_text(
        json.dumps(
            {
                "schema": "codex_audit_trusted_manifest_v1",
                "claim_id": blob["claim_id"],
                "audit_invocation_id": blob["audit_invocation_id"],
                "issued_at": datetime.now(timezone.utc).isoformat(),
                "entries": evidence_manifest,
            },
            sort_keys=True,
        ),
        encoding="utf-8",
    )
    env_key = "CODEX_AUDIT_TRUSTED_EVIDENCE_MANIFEST"
    old_manifest = os.environ.get(env_key)
    os.environ[env_key] = str(envelope_path)
    try:
        ledger = {"schema_version": 1, "rows": copy.deepcopy(rows)}
        ok, detail = audit_apply.apply_judicial_review(
            ledger, copy.deepcopy(blob)
        )
    finally:
        if old_manifest is None:
            os.environ.pop(env_key, None)
        else:
            os.environ[env_key] = old_manifest
    return None if ok else detail


HARD_APPLY_BLOCKER_PREFIXES = (
    "missing required judicial fields:",
    "unknown claim_id:",
    "audit_invocation_id ",
    "judicial third-auditor review requires independence=",
    "auditor_family=",
    "auditor_model=",
    "auditor_reasoning_effort=",
    "sided_with ",
    "note_hash drift;",
    "judicial review requires cross_confirmation.status",
    "judicial review requires first_audit and second_audit summaries",
    "first_audit cannot be upgraded",
    "second_audit cannot be upgraded",
    "third_audit cannot be upgraded",
    "judicial third auditor must differ",
    "trusted evidence manifest",
    "No-Go Discipline apply requires trusted orchestrator evidence transport",
)


def hard_apply_blocker(detail: str) -> bool:
    """Separate persistent row/tool/policy failures from tuple rejections."""
    return str(detail).startswith(HARD_APPLY_BLOCKER_PREFIXES)


def restore_preapply_state() -> str | None:
    reset = batch.sh(["git", "reset", "--hard", "HEAD"])
    if reset.returncode != 0:
        return f"reset failed: {(reset.stderr or reset.stdout).strip()[-240:]}"
    clean = batch.sh(
        ["git", "clean", "-fd", "--", *audit_runner.AUDIT_DATA_FILES]
    )
    if clean.returncode != 0:
        return f"clean failed: {(clean.stderr or clean.stdout).strip()[-240:]}"
    return None


def failed_after_apply(cid: str, result: str, detail: str) -> tuple[bool, dict]:
    restore_error = restore_preapply_state()
    if restore_error:
        detail = f"{detail}; restore failed: {restore_error}"
    return False, {"cid": cid, "result": result, "detail": detail}


def apply_judgment(
    blob: dict,
    evidence_manifest: dict[str, dict],
    workdir: Path,
    retries: int,
) -> tuple[bool, dict]:
    cid = blob["claim_id"]
    judgment_path = workdir / f"judgment-{batch.artifact_key(cid)}.json"
    judgment_path.write_text(
        json.dumps(blob, indent=1, sort_keys=True), encoding="utf-8"
    )
    for attempt in range(1, retries + 1):
        synced, detail = batch.sync_origin_main()
        if not synced:
            return False, {"cid": cid, "result": "sync_blocked", "detail": detail}
        applied, apply_detail = audit_runner.apply_one(
            blob, propagate=False, evidence_manifest=evidence_manifest
        )
        if not applied:
            return failed_after_apply(
                cid, "judicial_apply_rejected", apply_detail[-400:]
            )
        pipeline = batch.sh(["bash", str(SCRIPTS / "run_pipeline.sh")], timeout=1800)
        if pipeline.returncode != 0:
            return failed_after_apply(
                cid, "pipeline_failed", (pipeline.stderr or pipeline.stdout)[-400:]
            )
        lint = batch.sh(
            [sys.executable, str(SCRIPTS / "audit_lint.py"), "--strict"], timeout=600
        )
        if lint.returncode != 0:
            return failed_after_apply(
                cid, "strict_lint_failed", (lint.stderr or lint.stdout)[-400:]
            )
        diff_check = batch.sh(["git", "diff", "--check"])
        if diff_check.returncode != 0:
            return failed_after_apply(
                cid, "diff_check_failed", diff_check.stdout[-400:]
            )
        unexpected = [
            path
            for path in batch.changed_paths()
            if not batch.allowed_generated_path(path)
        ]
        if unexpected:
            return failed_after_apply(
                cid, "unexpected_generated_paths", str(unexpected[:8])
            )
        committed, detail = batch.stage_and_commit(
            f"audit: {cid} judicial panel {blob['ratified_verdict']} "
            f"(codex-cli, {batch.MODEL}, {batch.REASONING}, panel/batch)"
        )
        if not committed:
            return failed_after_apply(cid, "commit_failed", detail)
        local_commit = detail
        push = batch.sh(["git", "push", "-q", "origin", "HEAD:main"])
        if push.returncode == 0:
            return True, {
                "cid": cid,
                "result": blob["ratified_verdict"],
                "sided_with": blob["sided_with"],
                "commit": local_commit,
            }
        fetch = batch.sh(["git", "fetch", "origin", "main", "-q"])
        if fetch.returncode != 0:
            return False, {"cid": cid, "result": "push_failed"}
        landed = batch.sh(
            ["git", "merge-base", "--is-ancestor", local_commit, "origin/main"]
        )
        if landed.returncode == 0:
            return True, {
                "cid": cid,
                "result": blob["ratified_verdict"],
                "sided_with": blob["sided_with"],
                "commit": local_commit,
            }
        if attempt == retries:
            return False, {"cid": cid, "result": "push_race_exhausted"}
        error = batch.clean_main_error()
        if error:
            return False, {"cid": cid, "result": "race_retry_dirty", "detail": error}
        reset = batch.sh(["git", "reset", "--hard", "origin/main"])
        if reset.returncode != 0:
            return False, {"cid": cid, "result": "race_reset_failed"}
    return False, {"cid": cid, "result": "unreachable"}


def write_panel_record(workdir: Path, cid: str, panel_no: int, record: dict) -> None:
    payload = json.dumps(record, indent=1, sort_keys=True)
    key = batch.artifact_key(cid)
    (workdir / f"panel-{key}-round{panel_no}.json").write_text(
        payload, encoding="utf-8"
    )
    (workdir / f"panel-{key}.json").write_text(payload, encoding="utf-8")


def run_panel(
    row: dict,
    rows: dict[str, dict],
    workdir: Path,
    stall_minutes: int,
    runner_timeout: int,
    retries: int,
    prior_panels: list[dict],
) -> dict:
    cid = row["claim_id"]
    context_error = seat_context_error(row)
    if context_error:
        return {"cid": cid, "result": "seat_context_blocked", "detail": context_error}
    try:
        packet, evidence_manifest, invocation_id = render_panel_packet(
            row, rows, runner_timeout
        )
    except Exception as exc:
        return {"cid": cid, "result": "packet_render_blocked", "detail": str(exc)}

    panel_history = copy.deepcopy(prior_panels)
    panel_no = len(panel_history) + 1
    while True:
        jobs = []
        try:
            for judge_no in range(1, PANEL_SIZE + 1):
                jobs.append(
                    launch_judge(
                        packet,
                        row,
                        judge_no,
                        panel_no,
                        workdir,
                        panel_history,
                        invocation_id,
                        evidence_manifest,
                    )
                )
        except Exception as exc:
            batch.terminate_workers(jobs)
            return {
                "cid": cid,
                "result": "panel_launch_blocked",
                "detail": str(exc),
            }
        except BaseException:
            batch.terminate_workers(jobs)
            raise
        identities = {job["auditor"] for job in jobs}
        if len(identities) != PANEL_SIZE:
            batch.terminate_workers(jobs)
            return {
                "cid": cid,
                "result": "judge_identity_collision",
                "detail": "panel judges did not receive five distinct identities",
            }
        print(
            f"   {cid}: launched {len(jobs)} judges for panel {panel_no}; waiting"
        )
        try:
            batch.wait_workers(jobs, stall_minutes)
        except Exception as exc:
            return {
                "cid": cid,
                "result": "panel_wait_blocked",
                "detail": str(exc),
            }
        votes: list[dict] = []
        failures: list[str] = []
        for job in jobs:
            vote, status = collect_vote(job)
            if vote is None:
                failures.append(f"judge{job['judge']}:{status}")
            else:
                context_error = sided_vote_context_error(row, vote)
                if context_error:
                    failures.append(f"judge{job['judge']}:{context_error}")
                else:
                    vote["_panel_judge"] = job["judge"]
                    vote["_panel_auditor"] = job["auditor"]
                    votes.append(vote)

        tally = Counter(vote_tuple(vote) for vote in votes)
        record = {
            "schema": "judicial_panel_record_v1",
            "cid": cid,
            "panel": panel_no,
            "invocation_id": invocation_id,
            "disagreement_fingerprint": disagreement_fingerprint(row),
            "votes": [public_vote(vote) for vote in votes],
            "failures": failures,
            "tally": [
                {"tuple": [*key[:5], list(key[5])], "count": n}
                for key, n in tally.most_common()
            ],
        }
        if len(votes) != PANEL_SIZE:
            record["result"] = "panel_delivery_short"
            write_panel_record(workdir, cid, panel_no, record)
            return {
                "cid": cid,
                "result": "panel_delivery_short",
                "detail": ";".join(failures),
                "votes": record["votes"],
            }

        top_tuple, count = tally.most_common(1)[0]
        if count < MAJORITY:
            record["result"] = "no_majority"
            write_panel_record(workdir, cid, panel_no, record)
            panel_history.append(record)
            print(
                f"   {cid}: panel {panel_no} has no 3/5 majority; "
                "launching a fresh five-judge panel with all prior votes"
            )
            panel_no += 1
            continue

        if top_tuple[0] == "neither":
            record["result"] = "majority_neither"
            record["majority"] = count
            record["detail"] = (
                "a neither majority is recorded but never applied; the "
                "audit-loop skill requires a fresh five-judge panel"
            )
            write_panel_record(workdir, cid, panel_no, record)
            panel_history.append(record)
            print(
                f"   {cid}: panel {panel_no} majority sides with neither; "
                "launching a fresh five-judge panel with all prior votes"
            )
            panel_no += 1
            continue

        apply_errors = []
        blob = None
        for representative in (
            vote for vote in votes if vote_tuple(vote) == top_tuple
        ):
            candidate = judicial_blob(
                row, representative, votes, count, invocation_id=invocation_id
            )
            error = judicial_applyability_error(
                candidate, rows, evidence_manifest, workdir
            )
            if error is None:
                blob = candidate
                break
            rejection = {
                "judge": representative.get("_panel_judge"),
                "auditor": representative.get("_panel_auditor"),
                "error": error,
            }
            apply_errors.append(rejection)
            if hard_apply_blocker(error):
                record["result"] = "applyability_blocked"
                record["apply_errors"] = apply_errors
                record["rejected_candidate"] = candidate
                write_panel_record(workdir, cid, panel_no, record)
                return {
                    "cid": cid,
                    "result": "applyability_blocked",
                    "detail": error,
                    "judgment": candidate,
                    "votes": record["votes"],
                }
        if blob is None:
            record["result"] = "majority_unapplyable"
            record["apply_errors"] = apply_errors
            write_panel_record(workdir, cid, panel_no, record)
            panel_history.append(record)
            print(
                f"   {cid}: panel {panel_no} majority is not applyable; "
                "launching a fresh five-judge panel with all prior votes"
            )
            panel_no += 1
            continue

        record["result"] = "applyable_majority"
        record["majority"] = count
        write_panel_record(workdir, cid, panel_no, record)
        _ok, result = apply_judgment(
            blob, evidence_manifest, workdir, retries
        )
        return result


def workdir_guard_error(workdir: Path) -> str | None:
    resolved = workdir.expanduser().resolve(strict=False)
    repo = REPO_ROOT.resolve()
    try:
        resolved.relative_to(repo)
    except ValueError:
        return None
    return (
        f"workdir {resolved} is inside the repository; use a fresh external "
        "temporary directory so panel artifacts cannot dirty or hide inside main"
    )


PRIOR_PANEL_RESULTS = {"no_majority", "majority_neither", "majority_unapplyable"}


def load_prior_panels(
    paths: list[str], target_rows: dict[str, dict]
) -> tuple[dict[str, list[dict]], str | None]:
    grouped: dict[str, list[dict]] = {}
    seen_rounds: set[tuple[str, int]] = set()
    for path_text in paths:
        path = Path(path_text)
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            return {}, f"cannot read prior panel {path}: {exc}"
        if not isinstance(record, dict) or not isinstance(record.get("cid"), str):
            return {}, f"prior panel {path} lacks a string cid"
        cid = record["cid"]
        if cid not in target_rows:
            return {}, (
                f"prior panel {path} is bound to {cid!r}, which is not one of "
                "this invocation's targets"
            )
        if record.get("schema") != "judicial_panel_record_v1":
            return {}, f"prior panel {path} has an invalid schema"
        invocation_id = record.get("invocation_id")
        if not isinstance(invocation_id, str) or re.fullmatch(
            r"[0-9a-f]{32}", invocation_id
        ) is None:
            return {}, f"prior panel {path} has an invalid invocation_id"
        panel_no = record.get("panel")
        if not isinstance(panel_no, int) or isinstance(panel_no, bool) or panel_no < 1:
            return {}, f"prior panel {path} has an invalid panel number"
        round_key = (cid, panel_no)
        if round_key in seen_rounds:
            return {}, f"prior panel {path} duplicates {cid} panel {panel_no}"
        seen_rounds.add(round_key)
        expected_fingerprint = disagreement_fingerprint(target_rows[cid])
        if record.get("disagreement_fingerprint") != expected_fingerprint:
            return {}, (
                f"prior panel {path} does not match the current source and "
                "first/second audit-seat fingerprint"
            )
        if record.get("result") not in PRIOR_PANEL_RESULTS:
            return {}, f"prior panel {path} has invalid result {record.get('result')!r}"
        votes = record.get("votes")
        if not isinstance(votes, list) or len(votes) != PANEL_SIZE:
            return {}, f"prior panel {path} does not contain five vote records"
        for vote in votes:
            schema_error = vote_schema_error(vote)
            if schema_error:
                return {}, f"prior panel {path} contains invalid vote: {schema_error}"
            context_error = sided_vote_context_error(target_rows[cid], vote)
            if context_error:
                return {}, f"prior panel {path} contains invalid vote: {context_error}"
        if len({vote.get("judge") for vote in votes}) != PANEL_SIZE:
            return {}, f"prior panel {path} does not preserve five distinct judges"
        if len({vote.get("auditor") for vote in votes}) != PANEL_SIZE:
            return {}, f"prior panel {path} does not preserve five distinct identities"
        tally = Counter(vote_tuple(vote) for vote in votes)
        top_tuple, count = tally.most_common(1)[0]
        result = record["result"]
        if result == "no_majority" and count >= MAJORITY:
            return {}, f"prior panel {path} labels a majority as no_majority"
        if result == "majority_neither" and not (
            count >= MAJORITY and top_tuple[0] == "neither"
        ):
            return {}, f"prior panel {path} has an inconsistent neither result"
        if result == "majority_unapplyable" and not (
            count >= MAJORITY and top_tuple[0] != "neither"
        ):
            return {}, f"prior panel {path} has an inconsistent unapplyable result"
        grouped.setdefault(cid, []).append(record)
    for records in grouped.values():
        records.sort(key=lambda record: record["panel"])
        rounds = [record["panel"] for record in records]
        if rounds != list(range(1, len(records) + 1)):
            return {}, (
                "prior panels must be a contiguous sequence beginning at round 1; "
                f"got {rounds}"
            )
    return grouped, None


def runtime_arg_error(args: argparse.Namespace) -> str | None:
    for name in ("stall_minutes", "runner_timeout_sec", "push_retries"):
        if getattr(args, name) <= 0:
            return f"--{name.replace('_', '-')} must be positive"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Five-judge panel drainer for cross-confirmation disagreements"
    )
    parser.add_argument(
        "--claims",
        help="comma-separated claim ids (default: every disagreement row)",
    )
    parser.add_argument(
        "--prior-panel",
        action="append",
        default=[],
        help="path to a prior panel-<key>.json record to give the judges",
    )
    parser.add_argument("--stall-minutes", type=int, default=45)
    parser.add_argument("--runner-timeout-sec", type=int, default=120)
    parser.add_argument("--push-retries", type=int, default=3)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    arg_error = runtime_arg_error(args)
    if arg_error:
        print(f"refusing to run: {arg_error}")
        return 2

    if not args.dry_run:
        error = batch.clean_main_error()
        if error:
            print(f"refusing to run: {error}. Use a dedicated clean main checkout.")
            return 2

    workdir = Path(
        os.environ.get("AUDIT_PANEL_WORKDIR")
        or f"/tmp/audit_panel_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}_{uuid.uuid4().hex[:8]}"
    )
    if not args.dry_run:
        guard_error = workdir_guard_error(workdir)
        if guard_error:
            print(f"refusing to run: {guard_error}")
            return 2
        try:
            workdir.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print(
                f"refusing to run: workdir {workdir} already exists. "
                "Each run requires a fresh workdir; remove it or point "
                "AUDIT_PANEL_WORKDIR at a new path."
            )
            return 2

    if not args.dry_run and not (batch.DATA / "citation_graph.json").exists():
        print("derived audit caches missing (fresh clone); running the pipeline once")
        bootstrap = batch.sh(["bash", str(SCRIPTS / "run_pipeline.sh")], timeout=1800)
        if bootstrap.returncode != 0:
            print(f"pipeline bootstrap failed: {(bootstrap.stderr or bootstrap.stdout)[-300:]}")
            return 2
    rows = batch.load_rows()
    if args.claims:
        scope = [cid.strip() for cid in args.claims.split(",") if cid.strip()]
    else:
        scope = sorted(
            cid
            for cid, row in rows.items()
            if (row.get("cross_confirmation") or {}).get("status") == "disagreement"
        )
    targets = []
    for cid in scope:
        row = rows.get(cid)
        if not row:
            print(f"   skip: {cid}: missing ledger row")
            continue
        if (row.get("cross_confirmation") or {}).get("status") != "disagreement":
            print(f"   skip: {cid}: cross_confirmation is not a disagreement")
            continue
        targets.append(row)
    print(f"== judicial panel targets: {len(targets)}")
    if args.dry_run:
        for row in targets:
            print(f"   would panel: {row['claim_id']}")
        return 0

    prior_by_claim, prior_error = load_prior_panels(
        args.prior_panel, {row["claim_id"]: row for row in targets}
    )
    if prior_error:
        print(f"refusing to run: {prior_error}")
        return 2

    report = []
    for row in targets:
        result = run_panel(
            row,
            rows,
            workdir,
            args.stall_minutes,
            args.runner_timeout_sec,
            args.push_retries,
            prior_by_claim.get(row["claim_id"], []),
        )
        report.append(result)
        print(f"   {result['cid']}: {result['result']}")
        rows = batch.load_rows()

    (workdir / "report.jsonl").write_text(
        "".join(
            json.dumps(item, sort_keys=True)
            + "\n"
            for item in report
        ),
        encoding="utf-8",
    )
    print(f"report: {workdir / 'report.jsonl'}")
    applied = {
        "audited_clean", "audited_renaming", "audited_conditional",
        "audited_decoration", "audited_failed", "audited_numerical_match",
    }
    return 0 if all(item.get("result") in applied for item in report) else 1


if __name__ == "__main__":
    raise SystemExit(main())
