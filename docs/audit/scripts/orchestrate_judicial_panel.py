#!/usr/bin/env python3
"""Run the audit-loop five-judge panel over cross-confirmation disagreements.

For each targeted disagreement row this renders the canonical restricted
packet, appends both recorded seat positions (tuple summaries plus their
invocation-bound full rationales), and launches five detached GPT-5.6-sol/xhigh
judges with distinct identities. Each judge votes on the full tuple

    (sided_with, ratified_verdict, ratified_claim_type,
     ratified_claim_scope, ratified_load_bearing_step_class,
     ratified_decoration_parent_claim_id, negative_assertion_classes)

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
import ledger_io  # noqa: E402
import audit_contract  # noqa: E402
import orchestrate_audit_batch as batch  # noqa: E402
import seed_audit_ledger as seed_ledger  # noqa: E402

audit_runner = batch.audit_runner
REPO_ROOT = batch.REPO_ROOT

PANEL_SIZE = 5
MAJORITY = 3
MIN_VOTE_BYTES = 120
MAX_FRESH_PANEL_CONTRACT_RETRIES = 2
VOTE_CONTRACT_ERROR_PREFIX = "vote_contract_error:"
PANEL_TRANSIENT_SERVICE_RESULT = "panel_transient_service_unavailable"

ALLOWED_SIDES = audit_contract.JUDICIAL_SIDES
ALLOWED_VERDICTS = audit_contract.TERMINAL_VERDICTS
ALLOWED_CLAIM_TYPES = audit_contract.CLAIM_TYPES
VOTE_FIELDS = audit_contract.JUDICIAL_VOTE_FIELDS
PUBLIC_VOTE_FIELDS = (
    "judge",
    "auditor",
    *VOTE_FIELDS,
    "ratified_load_bearing_step",
    "hybrid_resolution_note",
    "ratified_decoration_parent_claim_id",
    "notes_for_re_audit_if_any",
    "no_go_discipline",
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
    return audit_contract.normalized_scope(value)


def vote_tuple(vote: dict) -> tuple:
    return audit_contract.judicial_vote_tuple(vote)


def serialized_tally(votes: list[dict]) -> list[dict]:
    """Return the canonical JSON form of the complete-tuple vote tally."""
    tally = Counter(vote_tuple(vote) for vote in votes)
    return [
        {"tuple": [*key[:6], list(key[6])], "count": count}
        for key, count in tally.most_common()
    ]


def disagreement_fingerprint(row: dict) -> dict:
    return audit_contract.judicial_disagreement_fingerprint(row)


def vote_schema_error(vote: object) -> str | None:
    return audit_contract.judicial_vote_schema_error(vote)


def sided_vote_context_error(row: dict, vote: dict) -> str | None:
    return audit_contract.sided_judicial_vote_context_error(row, vote)


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
        tuple_error = audit_contract.verdict_claim_type_error(
            summary.get("verdict"),
            summary.get("claim_type"),
            summary.get("decoration_parent_claim_id"),
        )
        if tuple_error:
            return (
                f"{label} has an incompatible verdict/claim_type tuple: "
                f"{tuple_error}; fresh cross-confirmation seats are required"
            )
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


RESEAT_REASON = (
    "cross_confirmation_reseat: the recorded seats do not satisfy the current "
    "rationale-preserving, semantically applyable seat contract; the seats are "
    "archived here with full provenance and the row is reopened for fresh "
    "cross-confirmation before any judicial panel"
)


def reseat_disposition(row: dict) -> str:
    """'blocked' (seats unrecoverable -> reseat), 'resolved' (no longer a
    disagreement), or 'recovered' (seats now back a valid packet -> panel)."""
    if (row.get("cross_confirmation") or {}).get("status") != "disagreement":
        return "resolved"
    if seat_context_error(row) is None:
        return "recovered"
    return "blocked"


def reseat_mutation(row: dict) -> dict:
    """Pure reseat: archive the full audit state (including both recorded
    seats) into previous_audits with the reseat reason, and return the row
    reopened for fresh seating. Nothing is deleted — the broken seats stay
    quotable provenance — and no verdict is minted: the row simply returns
    to `unaudited`, where the normal lane re-runs both cross-confirmation
    seats; fresh agreement lands the row, fresh disagreement reaches a
    panel whose packet is now valid. Either way the audit finishes."""
    new_row = seed_ledger.archive_prior_audit(row)
    new_row["previous_audits"][-1]["invalidation_reason"] = RESEAT_REASON
    return new_row


def panel_scope(args: argparse.Namespace, rows: dict[str, dict]) -> list[str]:
    if args.claims:
        return [cid.strip() for cid in args.claims.split(",") if cid.strip()]
    return sorted(
        cid
        for cid, row in rows.items()
        if (row.get("cross_confirmation") or {}).get("status") == "disagreement"
    )


def collect_panel_targets(
    scope: list[str], rows: dict[str, dict], announce_reseat: bool = True
) -> tuple[list[dict], list[str]]:
    """Split scoped rows into panelable targets and the reseat queue.

    A seat whose rationale cannot be reconstructed produces an invalid
    packet, so that row can never finish through a panel as recorded.
    Instead of retrying (or freezing), it is queued for RESEAT: archive the
    broken seats with full provenance and reopen the row for fresh
    cross-confirmation — the audit then finishes through fresh agreement or
    a validly-seated panel.
    """
    targets: list[dict] = []
    reseat_queue: list[str] = []
    for cid in scope:
        row = rows.get(cid)
        if not row:
            print(f"   skip: {cid}: missing ledger row")
            continue
        if (row.get("cross_confirmation") or {}).get("status") != "disagreement":
            print(f"   skip: {cid}: cross_confirmation is not a disagreement")
            continue
        context_error = seat_context_error(row)
        if context_error:
            reseat_queue.append(cid)
            if announce_reseat:
                print(f"   reseat: {cid}: {context_error}")
            else:
                print(f"   skip: {cid}: still seat-blocked after reseat attempt")
            continue
        targets.append(row)
    return targets, reseat_queue


RESEAT_OK_RESULTS = {"reseated", "resolved", "recovered"}


def _reseat_failure(cid: str, result: str, detail: str) -> dict:
    """Restore preapply state and return the outcome DICT (failed_after_apply
    returns an (ok, dict) tuple shaped for apply callers)."""
    _ok, failure = failed_after_apply(cid, result, detail)
    return failure


def reseat_blocked_row(cid: str, retries: int) -> dict:
    """Persist a reseat through the same per-claim gate ladder as verdicts:
    sync, mutate, pipeline, strict lint, diff check, serialized commit,
    race-retried push."""
    for attempt in range(1, retries + 1):
        synced, detail = batch.sync_origin_main()
        if not synced:
            return {"cid": cid, "result": "sync_blocked", "detail": detail}
        rows = batch.load_rows()
        row = rows.get(cid)
        if row is None:
            return {"cid": cid, "result": "missing_ledger_row"}
        disposition = reseat_disposition(row)
        if disposition != "blocked":
            return {"cid": cid, "result": disposition}
        ledger = ledger_io.load_ledger()
        ledger["rows"][cid] = reseat_mutation(ledger["rows"][cid])
        ledger_io.save_ledger(ledger)
        pipeline = batch.sh(["bash", str(SCRIPTS / "run_pipeline.sh")], timeout=1800)
        if pipeline.returncode != 0:
            return _reseat_failure(
                cid, "reseat_pipeline_failed", (pipeline.stderr or pipeline.stdout)[-400:]
            )
        lint = batch.sh(
            [sys.executable, str(SCRIPTS / "audit_lint.py"), "--strict"], timeout=600
        )
        if lint.returncode != 0:
            return _reseat_failure(
                cid, "reseat_strict_lint_failed", (lint.stderr or lint.stdout)[-400:]
            )
        diff_check = batch.sh(["git", "diff", "--check"])
        if diff_check.returncode != 0:
            return _reseat_failure(
                cid, "reseat_diff_check_failed", diff_check.stdout[-400:]
            )
        unexpected = [
            path
            for path in batch.changed_paths()
            if not batch.allowed_generated_path(path)
        ]
        if unexpected:
            return _reseat_failure(
                cid, "reseat_unexpected_generated_paths", str(unexpected[:8])
            )
        committed, detail = batch.stage_and_commit(
            f"audit-infra: reseat cross-confirmation seats for {cid} "
            "(unrecoverable legacy rationales archived; fresh seating opened)"
        )
        if not committed:
            return _reseat_failure(cid, "reseat_commit_failed", detail)
        local_commit = detail
        push = batch.sh(["git", "push", "-q", "origin", "HEAD:main"])
        if push.returncode == 0:
            return {"cid": cid, "result": "reseated", "commit": local_commit}
        fetch = batch.sh(["git", "fetch", "origin", "main", "-q"])
        if fetch.returncode != 0:
            return {"cid": cid, "result": "reseat_push_failed"}
        landed = batch.sh(
            ["git", "merge-base", "--is-ancestor", local_commit, "origin/main"]
        )
        if landed.returncode == 0:
            return {"cid": cid, "result": "reseated", "commit": local_commit}
        if attempt == retries:
            return {"cid": cid, "result": "reseat_push_race_exhausted"}
        error = batch.clean_main_error()
        if error:
            return {"cid": cid, "result": "reseat_race_retry_dirty", "detail": error}
        reset = batch.sh(["git", "reset", "--hard", "origin/main"])
        if reset.returncode != 0:
            return {"cid": cid, "result": "reseat_race_reset_failed"}
    return {"cid": cid, "result": "unreachable"}


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
            "Earlier panel attempts on this same disagreement produced the\n"
            "vote/rationale and validator-error breakdowns below but no applyable\n"
            "majority. Contract-invalid attempts may contain fewer than five\n"
            "accepted votes because invalid vote tuples carry no authority.\n"
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
    output_schema = audit_runner.write_object_output_schema(
        isolated / "PANEL_RESPONSE.schema.json",
        response_kind="judicial_vote",
    )
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
                "--output-schema", str(output_schema),
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
        "process_group": proc.pid,
        "raw_output": raw_output,
        "log_path": log_path,
        "log_handle": log_handle,
        "isolated": isolated,
        "auditor": judge_identity,
        "panel": panel_no,
        "invocation_id": invocation_id,
        "evidence_manifest": evidence_manifest,
        "started": now,
        "last_size": 0,
        "last_progress": now,
        "stalled": False,
        "deadline_exceeded": False,
        "returncode": None,
    }


def collect_vote(job: dict) -> tuple[dict | None, str]:
    if job.get("deadline_exceeded"):
        return None, "wall_timeout_killed"
    if job["stalled"]:
        return None, "stall_killed"
    raw = job["raw_output"]
    if job.get("returncode") != 0:
        marker = batch.retryable_worker_service_failure(job)
        if marker is not None:
            return None, f"{batch.TRANSIENT_SERVICE_FAILURE_RESULT}:{marker}"
        return None, f"judge_exit_{job.get('returncode')}"
    if not raw.exists() or raw.stat().st_size <= MIN_VOTE_BYTES:
        return None, "no_size_qualified_vote"
    reply = audit_runner.extract_response(raw.read_text(encoding="utf-8"))
    vote = audit_runner.parse_verdict_json(reply or "")
    if vote is None:
        return None, "malformed_vote_json"
    schema_error = vote_schema_error(vote)
    if schema_error:
        return None, f"{VOTE_CONTRACT_ERROR_PREFIX}{schema_error}"
    return vote, "ok"


def public_vote(vote: dict) -> dict:
    stored = {
        **{key: value for key, value in vote.items() if not key.startswith("_")},
        "judge": vote.get("_panel_judge"),
        "auditor": vote.get("_panel_auditor"),
    }
    return {
        key: copy.deepcopy(stored[key])
        for key in PUBLIC_VOTE_FIELDS
        if key in stored
    }


def canonical_prior_vote(vote: dict) -> dict:
    """Strip untrusted prior-history fields before showing them to judges."""
    return {
        key: copy.deepcopy(vote[key])
        for key in PUBLIC_VOTE_FIELDS
        if key in vote
    }


def judicial_blob(
    row: dict,
    representative: dict,
    votes: list[dict],
    majority: int,
    invocation_id: str | None = None,
    panel_no: int = 1,
) -> dict:
    for index, vote in enumerate(votes, 1):
        schema_error = vote_schema_error(vote)
        if schema_error:
            raise ValueError(f"panel vote {index} is invalid: {schema_error}")
        context_error = sided_vote_context_error(row, vote)
        if context_error:
            raise ValueError(f"panel vote {index} is invalid: {context_error}")
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
            "tuple": list(vote_tuple(vote)[:6]) + [list(vote_tuple(vote)[6])],
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
    panel_invocation_id = invocation_id or uuid.uuid4().hex
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
        "audit_invocation_id": panel_invocation_id,
        "sided_with": side,
        "ratified_verdict": ratified_verdict,
        "ratified_claim_type": ratified_claim_type,
        "ratified_claim_scope": ratified_scope,
        "ratified_load_bearing_step_class": ratified_class,
        "negative_assertion_classes": negative_classes,
        "judgment_rationale": rationale,
        "first_auditor_error": representative.get("first_auditor_error"),
        "second_auditor_error": representative.get("second_auditor_error"),
        "judicial_panel_record_v1": {
            "schema": "judicial_panel_record_v1",
            "cid": row["claim_id"],
            "panel": panel_no,
            "invocation_id": panel_invocation_id,
            "result": "majority_candidate",
            "disagreement_fingerprint": disagreement_fingerprint(row),
            "majority_count": majority,
            "votes": [public_vote(vote) for vote in votes],
            "failures": [],
            "tally": serialized_tally(votes),
        },
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
        blob["hybrid_resolution_note"] = representative[
            "hybrid_resolution_note"
        ]
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
    "judicial panel-majority apply requires independence=",
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
    "judicial panel representative must differ",
    "judicial_panel_record_v1",
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
    max_workers: int = PANEL_SIZE,
    seat_timeout_seconds: int = 2700,
) -> dict:
    cid = row["claim_id"]
    if max_workers < 1 or seat_timeout_seconds < 1:
        return {
            "cid": cid,
            "result": "panel_runtime_invalid",
            "detail": "worker and seat-timeout limits must be positive",
        }
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
    consecutive_contract_retries = 0
    for prior in reversed(panel_history):
        if prior.get("result") != "contract_invalid_retry":
            break
        consecutive_contract_retries += 1
    while True:
        jobs = []
        worker_phase = "launch"
        try:
            for wave_start in range(1, PANEL_SIZE + 1, max_workers):
                wave = []
                for judge_no in range(
                    wave_start,
                    min(PANEL_SIZE + 1, wave_start + max_workers),
                ):
                    job = launch_judge(
                        packet,
                        row,
                        judge_no,
                        panel_no,
                        workdir,
                        panel_history,
                        invocation_id,
                        evidence_manifest,
                    )
                    jobs.append(job)
                    wave.append(job)
                print(
                    f"   {cid}: launched judges "
                    f"{wave_start}-{wave_start + len(wave) - 1} "
                    f"for panel {panel_no}; waiting"
                )
                # Do not collect or expose any votes between waves. Every
                # judge receives the same pre-panel packet and prior-panel
                # history; waves only enforce the audit-seat ceiling.
                worker_phase = "wait"
                batch.wait_workers(
                    wave,
                    stall_minutes,
                    wall_timeout_seconds=seat_timeout_seconds,
                )
                worker_phase = "launch"
        except batch.CleanupIntegrityError as cleanup_error:
            try:
                batch.terminate_read_only_seats(
                    [
                        job
                        for job in jobs
                        if job.get("proc") is not None
                        and job["proc"].poll() is None
                    ]
                )
            except BaseException as secondary_error:
                raise batch.CleanupIntegrityError(
                    f"{cleanup_error}; judicial secondary seat cleanup "
                    f"also failed: {secondary_error}"
                ) from secondary_error
            raise
        except Exception as exc:
            batch.terminate_workers(jobs)
            return {
                "cid": cid,
                "result": (
                    "panel_wait_blocked"
                    if worker_phase == "wait"
                    else "panel_launch_blocked"
                ),
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
        votes: list[dict] = []
        failures: list[str] = []
        contract_failures: list[str] = []
        transient_failures: list[str] = []
        transient_prefix = f"{batch.TRANSIENT_SERVICE_FAILURE_RESULT}:"
        for job in jobs:
            vote, status = collect_vote(job)
            if vote is None:
                failure = f"judge{job['judge']}:{status}"
                failures.append(failure)
                if status.startswith(transient_prefix):
                    transient_failures.append(failure)
                elif status.startswith(VOTE_CONTRACT_ERROR_PREFIX):
                    contract_failures.append(failure)
            else:
                context_error = sided_vote_context_error(row, vote)
                if context_error:
                    failure = (
                        f"judge{job['judge']}:{VOTE_CONTRACT_ERROR_PREFIX}"
                        f"{context_error}"
                    )
                    failures.append(failure)
                    contract_failures.append(failure)
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
            "tally": serialized_tally(votes),
        }
        if len(votes) != PANEL_SIZE:
            if transient_failures and len(transient_failures) == len(failures):
                record["result"] = PANEL_TRANSIENT_SERVICE_RESULT
                write_panel_record(workdir, cid, panel_no, record)
                return {
                    "cid": cid,
                    "result": PANEL_TRANSIENT_SERVICE_RESULT,
                    "detail": ";".join(failures),
                    "votes": record["votes"],
                }
            if failures and len(contract_failures) == len(failures):
                consecutive_contract_retries += 1
                if (
                    consecutive_contract_retries
                    <= MAX_FRESH_PANEL_CONTRACT_RETRIES
                ):
                    record["result"] = "contract_invalid_retry"
                    write_panel_record(workdir, cid, panel_no, record)
                    panel_history.append(record)
                    print(
                        f"   {cid}: panel {panel_no} had schema-invalid vote "
                        "deliveries; launching a fresh five-judge panel with "
                        "the exact validator errors"
                    )
                    panel_no += 1
                    continue
                record["result"] = "panel_contract_retries_exhausted"
                write_panel_record(workdir, cid, panel_no, record)
                return {
                    "cid": cid,
                    "result": "panel_contract_retries_exhausted",
                    "detail": ";".join(failures),
                    "votes": record["votes"],
                }
            record["result"] = "panel_delivery_short"
            write_panel_record(workdir, cid, panel_no, record)
            return {
                "cid": cid,
                "result": "panel_delivery_short",
                "detail": ";".join(failures),
                "votes": record["votes"],
            }

        consecutive_contract_retries = 0
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
                row,
                representative,
                votes,
                count,
                invocation_id=invocation_id,
                panel_no=panel_no,
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


PRIOR_PANEL_RESULTS = {
    "no_majority",
    "majority_neither",
    "majority_unapplyable",
    "contract_invalid_retry",
}


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
        result = record["result"]
        votes = record.get("votes")
        if not isinstance(votes, list):
            return {}, f"prior panel {path} has no vote list"
        if result == "contract_invalid_retry":
            failures = record.get("failures")
            if (
                len(votes) >= PANEL_SIZE
                or not isinstance(failures, list)
                or not failures
            ):
                return {}, f"prior panel {path} has an invalid contract-retry record"
        elif len(votes) != PANEL_SIZE:
            return {}, f"prior panel {path} does not contain five vote records"
        elif record.get("failures") != []:
            return {}, f"prior panel {path} has inconsistent failure metadata"
        for vote in votes:
            schema_error = vote_schema_error(vote)
            if schema_error:
                return {}, f"prior panel {path} contains invalid vote: {schema_error}"
            context_error = sided_vote_context_error(target_rows[cid], vote)
            if context_error:
                return {}, f"prior panel {path} contains invalid vote: {context_error}"
        vote_judges = [vote.get("judge") for vote in votes]
        vote_auditors = [vote.get("auditor") for vote in votes]
        if not all(
            isinstance(judge, int) and not isinstance(judge, bool)
            and judge in range(1, PANEL_SIZE + 1)
            for judge in vote_judges
        ):
            return {}, f"prior panel {path} contains an invalid judge seat"
        if len(set(vote_judges)) != len(votes):
            return {}, f"prior panel {path} does not preserve distinct judges"
        if not all(
            isinstance(auditor, str) and auditor.strip()
            for auditor in vote_auditors
        ):
            return {}, f"prior panel {path} contains an invalid auditor identity"
        if len(set(vote_auditors)) != len(votes):
            return {}, f"prior panel {path} does not preserve distinct identities"
        expected_tally = serialized_tally(votes)
        if result == "contract_invalid_retry":
            failure_judges: list[int] = []
            for failure in failures:
                match = re.fullmatch(
                    rf"judge([1-{PANEL_SIZE}]):"
                    rf"{re.escape(VOTE_CONTRACT_ERROR_PREFIX)}.+",
                    str(failure),
                )
                if match is None:
                    return {}, (
                        f"prior panel {path} has an invalid contract-retry record"
                    )
                failure_judges.append(int(match.group(1)))
            if (
                len(votes) + len(failures) != PANEL_SIZE
                or len(set(failure_judges)) != len(failure_judges)
                or set(vote_judges) & set(failure_judges)
                or set(vote_judges) | set(failure_judges)
                != set(range(1, PANEL_SIZE + 1))
            ):
                return {}, (
                    f"prior panel {path} has an invalid contract-retry record"
                )
            if record.get("tally") != expected_tally:
                return {}, f"prior panel {path} has inconsistent tally metadata"
            canonical = {
                "schema": "judicial_panel_record_v1",
                "cid": cid,
                "panel": panel_no,
                "invocation_id": invocation_id,
                "result": result,
                "disagreement_fingerprint": copy.deepcopy(
                    expected_fingerprint
                ),
                "votes": [canonical_prior_vote(vote) for vote in votes],
                "failures": copy.deepcopy(record["failures"]),
                "tally": copy.deepcopy(expected_tally),
            }
            grouped.setdefault(cid, []).append(canonical)
            continue
        if set(vote_judges) != set(range(1, PANEL_SIZE + 1)):
            return {}, f"prior panel {path} does not preserve all five judge seats"
        if record.get("tally") != expected_tally:
            return {}, f"prior panel {path} has inconsistent tally metadata"
        canonical = {
            "schema": "judicial_panel_record_v1",
            "cid": cid,
            "panel": panel_no,
            "invocation_id": invocation_id,
            "result": result,
            "disagreement_fingerprint": copy.deepcopy(expected_fingerprint),
            "votes": [canonical_prior_vote(vote) for vote in votes],
            "failures": [],
            "tally": copy.deepcopy(expected_tally),
        }
        tally = Counter(vote_tuple(vote) for vote in votes)
        top_tuple, count = tally.most_common(1)[0]
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
        if result == "majority_neither":
            if record.get("majority") != count:
                return {}, f"prior panel {path} has inconsistent majority metadata"
            canonical["majority"] = count
            canonical["detail"] = (
                "a neither majority is recorded but never applied; the "
                "audit-loop skill requires a fresh five-judge panel"
            )
        if result == "majority_unapplyable":
            apply_errors = record.get("apply_errors")
            majority_votes = [
                vote for vote in votes if vote_tuple(vote) == top_tuple
            ]
            if not isinstance(apply_errors, list) or len(apply_errors) != count:
                return {}, f"prior panel {path} has invalid apply-error metadata"
            canonical_errors = []
            for rejection, majority_vote in zip(apply_errors, majority_votes):
                expected_identity = (
                    majority_vote.get("judge"),
                    majority_vote.get("auditor"),
                )
                if (
                    not isinstance(rejection, dict)
                    or (rejection.get("judge"), rejection.get("auditor"))
                    != expected_identity
                    or not isinstance(rejection.get("error"), str)
                    or not rejection["error"].strip()
                    or hard_apply_blocker(rejection["error"])
                ):
                    return {}, (
                        f"prior panel {path} has invalid apply-error metadata"
                    )
                canonical_errors.append(
                    {
                        "judge": expected_identity[0],
                        "auditor": expected_identity[1],
                        "error": rejection["error"],
                    }
                )
            canonical["apply_errors"] = canonical_errors
        grouped.setdefault(cid, []).append(canonical)
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
    defaults = {"max_workers": PANEL_SIZE, "seat_timeout_sec": 2700}
    for name in (
        "max_workers",
        "stall_minutes",
        "seat_timeout_sec",
        "runner_timeout_sec",
        "push_retries",
    ):
        if getattr(args, name, defaults.get(name)) <= 0:
            return f"--{name.replace('_', '-')} must be positive"
    return None


def report_exit_code(report: list[dict], reseat_failures: list[dict]) -> int:
    """Return success, typed temporary-service failure, or hard failure."""
    applied = ALLOWED_VERDICTS
    panels_ok = all(item.get("result") in applied for item in report)
    transient = any(
        item.get("result") == PANEL_TRANSIENT_SERVICE_RESULT
        for item in report
    )
    retryable = all(
        item.get("result") in applied | {PANEL_TRANSIENT_SERVICE_RESULT}
        for item in report
    )
    if retryable and transient and not reseat_failures:
        return batch.TRANSIENT_SERVICE_EXIT_CODE
    return 0 if (panels_ok and not reseat_failures) else 1


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
    parser.add_argument(
        "--max-workers",
        type=int,
        default=PANEL_SIZE,
        help=(
            "concurrent judge-seat ceiling; all five distinct votes remain "
            "mandatory and are scheduled in waves when this is below five"
        ),
    )
    parser.add_argument("--stall-minutes", type=int, default=45)
    parser.add_argument(
        "--seat-timeout-sec",
        type=int,
        default=2700,
        help=(
            "absolute wall-clock deadline for each read-only judge seat; "
            "continuous output does not extend it"
        ),
    )
    parser.add_argument("--runner-timeout-sec", type=int, default=120)
    parser.add_argument("--push-retries", type=int, default=3)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--no-reseat",
        action="store_true",
        help=(
            "report seat-blocked disagreement rows without reseating them "
            "(default: archive unrecoverable seats and reopen fresh "
            "cross-confirmation so the audit can finish)"
        ),
    )
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

    if not args.dry_run:
        drain_lock = batch.acquire_exclusive_drain_lock("orchestrate_judicial_panel")
        if drain_lock is None:
            return 3
    if not args.dry_run and not (batch.DATA / "citation_graph.json").exists():
        print("derived audit caches missing (fresh clone); running the pipeline once")
        bootstrap = batch.sh(["bash", str(SCRIPTS / "run_pipeline.sh")], timeout=1800)
        if bootstrap.returncode != 0:
            print(f"pipeline bootstrap failed: {(bootstrap.stderr or bootstrap.stdout)[-300:]}")
            return 2
    rows = batch.load_rows()
    scope = panel_scope(args, rows)
    targets, reseat_queue = collect_panel_targets(scope, rows)
    print(
        f"== judicial panel targets: {len(targets)} "
        f"(reseat queue: {len(reseat_queue)})"
    )
    if args.dry_run:
        for row in targets:
            print(f"   would panel: {row['claim_id']}")
        for cid in reseat_queue:
            print(f"   would reseat: {cid}")
        return 0

    reseat_failures: list[dict] = []
    if reseat_queue and not args.no_reseat:
        print(f"== reseating {len(reseat_queue)} seat-blocked row(s)")
        for cid in reseat_queue:
            outcome = reseat_blocked_row(cid, args.push_retries)
            print(f"   reseat outcome: {json.dumps(outcome, sort_keys=True)}")
            if outcome.get("result") not in RESEAT_OK_RESULTS:
                reseat_failures.append(outcome)
        # Every reseat attempt begins with a main sync, so the ledger may
        # have moved regardless of outcome (reseated, recovered, resolved,
        # or failure). Rebuild the panel view unconditionally so no panel —
        # including a row whose seats turned out recovered — renders from
        # pre-sync rows.
        rows = batch.load_rows()
        scope = panel_scope(args, rows)
        targets, _still_blocked = collect_panel_targets(
            scope, rows, announce_reseat=False
        )
        print(f"== post-reseat panel targets: {len(targets)}")
    elif reseat_queue:
        print(
            f"== --no-reseat: leaving {len(reseat_queue)} seat-blocked row(s) "
            "untouched (they cannot finish through a panel as recorded)"
        )

    prior_by_claim, prior_error = load_prior_panels(
        args.prior_panel, {row["claim_id"]: row for row in targets}
    )
    if prior_error:
        print(f"refusing to run: {prior_error}")
        return 2

    report = []
    for row in targets:
        try:
            result = run_panel(
                row,
                rows,
                workdir,
                args.stall_minutes,
                args.runner_timeout_sec,
                args.push_retries,
                prior_by_claim.get(row["claim_id"], []),
                max_workers=args.max_workers,
                seat_timeout_seconds=args.seat_timeout_sec,
            )
        except batch.CleanupIntegrityError as exc:
            print(
                "GLOBAL cleanup integrity failure; no later panel may launch: "
                f"{exc}"
            )
            return batch.CLEANUP_INTEGRITY_EXIT_CODE
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
    if reseat_failures:
        print(f"== reseat failures: {len(reseat_failures)} (nonzero exit)")
    return report_exit_code(report, reseat_failures)


if __name__ == "__main__":
    raise SystemExit(main())
