#!/usr/bin/env python3
"""Run the audit-loop five-judge panel over cross-confirmation disagreements.

For each targeted disagreement row this renders the canonical restricted
packet, appends both recorded seat positions (tuple summaries plus their
archived full rationales), and launches five detached GPT-5.6-sol/xhigh
judges with distinct identities. Each judge votes on the full tuple

    (sided_with, ratified_verdict, ratified_claim_type,
     ratified_claim_scope, ratified_load_bearing_step_class,
     negative_assertion_classes)

and must explain the error in the position it votes against. A majority is
at least three matching full-tuple votes out of five (whitespace-only scope
differences and assertion-class ordering are equivalent). On majority, a
representative judicial JSON is applied through the standard serialized
gates (apply -> pipeline -> strict lint -> diff/scope check -> commit ->
push). Without a majority, the panel record is written to the workdir and
the next invocation may pass it back via --prior-panel for a fresh panel
with the earlier votes in context, per the audit-loop skill.

Run only from a dedicated, clean ``main`` checkout.
"""
from __future__ import annotations

import argparse
import json
import os
import re
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


def archived_rationale(row: dict, invocation_id: str) -> str:
    for archived in reversed(row.get("previous_audits") or []):
        if not isinstance(archived, dict):
            continue
        if invocation_id and archived.get("audit_invocation_id") == invocation_id:
            rationale = str(archived.get("verdict_rationale") or "")
            notes = str(archived.get("notes_for_re_audit_if_any") or "")
            return rationale + (f"\n[re-audit notes] {notes}" if notes else "")
    return "[no archived rationale found for this seat's invocation id]"


def seat_block(label: str, summary: dict, row: dict) -> str:
    lines = [f"=== BEGIN {label.upper()} POSITION ==="]
    for field in (
        "verdict", "claim_type", "claim_scope", "load_bearing_step_class",
        "negative_assertion_classes", "independence", "auditor",
    ):
        lines.append(f"{field}: {json.dumps(summary.get(field))}")
    lines.append("full rationale:")
    lines.append(archived_rationale(row, str(summary.get("audit_invocation_id") or "")))
    lines.append(f"=== END {label.upper()} POSITION ===")
    return "\n".join(lines)


def panel_instructions(judge_no: int, prior_panels: list[dict]) -> str:
    prior_block = ""
    if prior_panels:
        prior_block = (
            "\n### Prior panel outcomes (no majority yet)\n\n"
            "Earlier five-judge panels on this disagreement produced the vote\n"
            "breakdowns below. Weigh their arguments; you are not bound by\n"
            "them.\n\n"
            + json.dumps(prior_panels, indent=1, sort_keys=True)
            + "\n"
        )
    return f"""
### JUDICIAL PANEL SEAT {judge_no} OF {PANEL_SIZE}

The two independent audit seats above DISAGREE. You are one judge on a
five-judge panel resolving the disagreement. Judge ONLY from the restricted
packet plus the two recorded positions. Do not search anything else.
{prior_block}
Return EXACTLY ONE JSON object and nothing else:

{{
  "sided_with": "<first|second|hybrid>",
  "ratified_verdict": "<audited_clean|audited_renaming|audited_conditional|audited_decoration|audited_failed|audited_numerical_match>",
  "ratified_claim_type": "<positive_theorem|bounded_theorem|no_go|open_gate|decoration|meta>",
  "ratified_claim_scope": "<the exact scope sentence you ratify; reuse a seat's scope verbatim unless a hybrid correction is required>",
  "ratified_load_bearing_step_class": "<(A)|(B)|(C)|(D)|(E)|(F)|(G) style class exactly as the seats use>",
  "negative_assertion_classes": [],
  "judgment_rationale": "<why the ratified tuple is correct, grounded in the packet>",
  "first_auditor_error": "<the specific error in the first position, or 'none' if you side with it entirely>",
  "second_auditor_error": "<the specific error in the second position, or 'none' if you side with it entirely>"
}}

Rules: vote the FULL tuple; a factual check against the packet (for
example whether the runner computes a contested quantity) outweighs either
seat's characterization; if you side with a seat, prefer that seat's
claim_scope verbatim; declare negative_assertion_classes honestly for the
tuple you ratify; never leave first_auditor_error and second_auditor_error
both 'none' unless you ratify a hybrid that faults neither.
"""


def render_judge_prompt(
    row: dict,
    rows: dict[str, dict],
    judge_no: int,
    runner_timeout: int,
    prior_panels: list[dict],
) -> str:
    template = audit_runner.PROMPT_TEMPLATE_PATH.read_text(encoding="utf-8")
    packet = audit_runner.render_prompt(
        row,
        rows,
        template,
        runner_timeout,
        use_cache=False,
        evidence_manifest_out={},
        audit_invocation_id=uuid.uuid4().hex,
    )
    cross = row.get("cross_confirmation") or {}
    first = cross.get("first_audit") or {}
    second = cross.get("second_audit") or {}
    return "\n\n".join(
        [
            packet,
            seat_block("first_audit", first, row),
            seat_block("second_audit", second, row),
            panel_instructions(judge_no, prior_panels),
        ]
    )


def launch_judge(
    row: dict,
    rows: dict[str, dict],
    judge_no: int,
    workdir: Path,
    runner_timeout: int,
    prior_panels: list[dict],
) -> dict:
    cid = row["claim_id"]
    key = batch.artifact_key(cid)
    prompt = render_judge_prompt(row, rows, judge_no, runner_timeout, prior_panels)
    if len(prompt) > audit_runner.CODEX_INPUT_CHAR_LIMIT:
        raise ValueError(
            f"{cid}: judicial packet is {len(prompt)} characters; narrow the "
            "packet rather than converting transport size into a verdict"
        )
    tag = f"{key}-judge{judge_no}"
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
    import subprocess

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
        "auditor": (
            f"codex-judicial-{judge_no}-"
            f"{datetime.now(timezone.utc).strftime('%Y%m%d')}-{uuid.uuid4().hex[:8]}"
        ),
        "last_size": 0,
        "last_progress": now,
        "stalled": False,
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
    missing = [field for field in VOTE_FIELDS if field not in vote]
    if missing:
        return None, f"vote_missing_fields:{','.join(missing)}"
    return vote, "ok"


def judicial_blob(
    row: dict, representative: dict, votes: list[dict], majority: int
) -> dict:
    breakdown = [
        {
            "judge": index + 1,
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
    return {
        "claim_id": row["claim_id"],
        "third_auditor": (
            f"codex-judicial-panel-{datetime.now(timezone.utc).strftime('%Y%m%d')}-"
            f"{uuid.uuid4().hex[:8]}"
        ),
        "auditor_family": batch.AUDITOR_FAMILY,
        "auditor_model": batch.MODEL,
        "auditor_reasoning_effort": batch.REASONING,
        "independence": "judicial_review",
        "audit_invocation_id": uuid.uuid4().hex,
        "sided_with": representative.get("sided_with"),
        "ratified_verdict": representative.get("ratified_verdict"),
        "ratified_claim_type": representative.get("ratified_claim_type"),
        "ratified_claim_scope": representative.get("ratified_claim_scope"),
        "ratified_load_bearing_step_class": representative.get(
            "ratified_load_bearing_step_class"
        ),
        "negative_assertion_classes": representative.get(
            "negative_assertion_classes"
        ),
        "judgment_rationale": rationale,
        "first_auditor_error": representative.get("first_auditor_error"),
        "second_auditor_error": representative.get("second_auditor_error"),
    }


def apply_judgment(blob: dict, workdir: Path, retries: int) -> tuple[bool, dict]:
    cid = blob["claim_id"]
    judgment_path = workdir / f"judgment-{batch.artifact_key(cid)}.json"
    judgment_path.write_text(
        json.dumps(blob, indent=1, sort_keys=True), encoding="utf-8"
    )
    for attempt in range(1, retries + 1):
        synced, detail = batch.sync_origin_main()
        if not synced:
            return False, {"cid": cid, "result": "sync_blocked", "detail": detail}
        apply_result = batch.sh(
            [
                sys.executable,
                str(SCRIPTS / "apply_audit.py"),
                "--file",
                str(judgment_path),
            ]
        )
        if apply_result.returncode != 0:
            return False, {
                "cid": cid,
                "result": "judicial_apply_rejected",
                "detail": (apply_result.stderr or apply_result.stdout)[-400:],
            }
        pipeline = batch.sh(["bash", str(SCRIPTS / "run_pipeline.sh")], timeout=1800)
        if pipeline.returncode != 0:
            return False, {
                "cid": cid,
                "result": "pipeline_failed",
                "detail": (pipeline.stderr or pipeline.stdout)[-400:],
            }
        lint = batch.sh(
            [sys.executable, str(SCRIPTS / "audit_lint.py"), "--strict"], timeout=600
        )
        if lint.returncode != 0:
            return False, {
                "cid": cid,
                "result": "strict_lint_failed",
                "detail": (lint.stderr or lint.stdout)[-400:],
            }
        diff_check = batch.sh(["git", "diff", "--check"])
        if diff_check.returncode != 0:
            return False, {
                "cid": cid,
                "result": "diff_check_failed",
                "detail": diff_check.stdout[-400:],
            }
        unexpected = [
            path
            for path in batch.changed_paths()
            if not batch.allowed_generated_path(path)
        ]
        if unexpected:
            return False, {
                "cid": cid,
                "result": "unexpected_generated_paths",
                "detail": str(unexpected[:8]),
            }
        committed, detail = batch.stage_and_commit(
            f"audit: {cid} judicial panel {blob['ratified_verdict']} "
            f"(codex-cli, {batch.MODEL}, {batch.REASONING}, panel/batch)"
        )
        if not committed:
            return False, {"cid": cid, "result": "commit_failed", "detail": detail}
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
    jobs = []
    try:
        for judge_no in range(1, PANEL_SIZE + 1):
            jobs.append(
                launch_judge(
                    row, rows, judge_no, workdir, runner_timeout, prior_panels
                )
            )
    except BaseException:
        batch.terminate_workers(jobs)
        raise
    print(f"   {cid}: launched {len(jobs)} panel judges; waiting")
    batch.wait_workers(jobs, stall_minutes)
    votes: list[dict] = []
    failures: list[str] = []
    for job in jobs:
        vote, status = collect_vote(job)
        if vote is None:
            failures.append(f"judge{job['judge']}:{status}")
        else:
            votes.append(vote)
    if len(votes) < MAJORITY:
        return {
            "cid": cid,
            "result": "panel_delivery_short",
            "detail": ";".join(failures),
            "votes": votes,
        }
    tally = Counter(vote_tuple(vote) for vote in votes)
    top_tuple, count = tally.most_common(1)[0]
    record = {
        "cid": cid,
        "votes": [
            {key: vote.get(key) for key in VOTE_FIELDS} for vote in votes
        ],
        "failures": failures,
        "tally": [
            {"tuple": [*key[:5], list(key[5])], "count": n}
            for key, n in tally.most_common()
        ],
    }
    (workdir / f"panel-{batch.artifact_key(cid)}.json").write_text(
        json.dumps(record, indent=1, sort_keys=True), encoding="utf-8"
    )
    if count < MAJORITY:
        return {
            "cid": cid,
            "result": "no_majority",
            "detail": f"top tuple has {count}/{len(votes)} votes",
            "votes": votes,
        }
    representative = next(
        vote for vote in votes if vote_tuple(vote) == top_tuple
    )
    blob = judicial_blob(row, representative, votes, count)
    ok, result = apply_judgment(blob, workdir, retries)
    return result


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
        try:
            workdir.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print(
                f"refusing to run: workdir {workdir} already exists. "
                "Each run requires a fresh workdir; remove it or point "
                "AUDIT_PANEL_WORKDIR at a new path."
            )
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

    prior_panels = []
    for path in args.prior_panel:
        prior_panels.append(json.loads(Path(path).read_text(encoding="utf-8")))

    report = []
    for row in targets:
        result = run_panel(
            row,
            rows,
            workdir,
            args.stall_minutes,
            args.runner_timeout_sec,
            args.push_retries,
            prior_panels,
        )
        report.append(result)
        print(f"   {result['cid']}: {result['result']}")
        rows = batch.load_rows()

    (workdir / "report.jsonl").write_text(
        "".join(
            json.dumps(
                {key: value for key, value in item.items() if key != "votes"},
                sort_keys=True,
            )
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
