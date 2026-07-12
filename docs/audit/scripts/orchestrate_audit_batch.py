#!/usr/bin/env python3
"""Drain routine development-tier audit rows with parallel fresh auditors.

Each round selects dependency-ready unaudited rows from an explicit claim set
or a configured lane closure, renders the canonical restricted packet, starts
detached GPT-5.6-sol/xhigh auditors, and then applies deliveries serially:

    apply -> pipeline -> strict lint -> diff/scope check -> commit -> push

Critical rows receive two simultaneous restricted-context seats with distinct
identities.  ``no_go`` rows are reported and skipped because they require the
forensic tier.  A critical-seat disagreement is preserved and reported for the
audit-loop judicial-panel path; this routine drainer never guesses through it.

Run mutating batches only from a dedicated, clean ``main`` checkout.  The
clean guard is repeated immediately before every mutation and race retry.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS.parents[2]
DATA = REPO_ROOT / "docs" / "audit" / "data"
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import codex_audit_runner as audit_runner  # noqa: E402

MODEL = "gpt-5.6-sol"
AUDITOR_FAMILY = "codex-gpt-5.6"
REASONING = "xhigh"
RETAINED = {"retained", "retained_bounded", "retained_no_go", "meta"}
AUDITABLE_TYPES = {"positive_theorem", "bounded_theorem", "open_gate"}
MIN_DELIVERY_BYTES = 200


def sh(cmd: list[str], timeout: int | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def load_rows() -> dict[str, dict]:
    ledger = json.loads((DATA / "audit_ledger.json").read_text(encoding="utf-8"))
    return ledger.get("rows", {})


def accepted(cid: str) -> bool:
    return audit_runner.premise_nodes.is_accepted_premise_dep(cid)


def dep_ready(row: dict, effective: dict[str, str]) -> bool:
    for dep in row.get("deps") or []:
        if accepted(dep):
            continue
        status = effective.get(dep, "MISSING")
        if status in RETAINED or str(status).startswith("decoration_under_"):
            continue
        return False
    return True


def lane_closure(root: str, rows: dict[str, dict]) -> set[str]:
    seen: set[str] = set()
    frontier = [root]
    while frontier:
        cid = frontier.pop()
        if cid in seen or accepted(cid):
            continue
        seen.add(cid)
        row = rows.get(cid)
        if row:
            frontier.extend(d for d in (row.get("deps") or []) if d not in seen)
    return seen


def compute_targets(
    scope: set[str], rows: dict[str, dict]
) -> tuple[list[dict], list[str]]:
    effective = {cid: row.get("effective_status", "?") for cid, row in rows.items()}
    targets: list[dict] = []
    skipped: list[str] = []
    for cid in sorted(scope):
        row = rows.get(cid)
        if not row:
            skipped.append(f"{cid}: missing ledger row")
            continue
        status = row.get("effective_status")
        if status in RETAINED or str(status or "").startswith("decoration_under_"):
            continue
        if row.get("audit_status") not in {None, "unaudited"}:
            skipped.append(f"{cid}: audit_status={row.get('audit_status')}")
            continue
        claim_type = row.get("claim_type") or row.get("claim_type_author_hint")
        if claim_type == "no_go":
            skipped.append(f"{cid}: no_go row - forensic tier, run individually")
            continue
        if claim_type not in AUDITABLE_TYPES:
            skipped.append(f"{cid}: claim_type={claim_type} - not batch-auditable")
            continue
        if not dep_ready(row, effective):
            continue
        targets.append(row)
    return targets, skipped


def artifact_key(cid: str) -> str:
    prefix = re.sub(r"[^a-zA-Z0-9_.-]+", "_", cid)[:48].rstrip("_.-") or "claim"
    digest = hashlib.sha256(cid.encode("utf-8")).hexdigest()[:16]
    return f"{prefix}-{digest}"


def seat_independence(row: dict, pass_no: int) -> str:
    if pass_no == 2:
        return "fresh_context"
    author_family = row.get("author_family")
    if (
        author_family
        and audit_runner.canonicalize_existing_auditor_family(author_family)
        == audit_runner.canonicalize_existing_auditor_family(AUDITOR_FAMILY)
    ):
        return "fresh_context"
    return "cross_family"


def prompt_has_clipped_evidence(manifest: dict[str, dict]) -> list[str]:
    roles = {
        "source", "authority", "runner", "helper", "runner_stdout",
        "runner_stdout_cache_eligible",
    }
    return sorted(
        path
        for path, entry in manifest.items()
        if set(entry.get("roles") or []) & roles
        and any(
            marker in str(entry.get("text") or "")
            for marker in audit_runner.CLIPPED_EVIDENCE_MARKERS
        )
    )


def launch_worker(
    row: dict,
    rows: dict[str, dict],
    pass_no: int,
    workdir: Path,
    runner_timeout: int,
) -> dict:
    cid = row["claim_id"]
    key = artifact_key(cid)
    seat = "A" if pass_no == 1 else "B"
    ident = f"{seat}-{datetime.now(timezone.utc).strftime('%Y%m%d')}-{uuid.uuid4().hex[:8]}"
    invocation_id = uuid.uuid4().hex
    evidence_manifest: dict[str, dict] = {}
    template = audit_runner.PROMPT_TEMPLATE_PATH.read_text(encoding="utf-8")
    prompt = audit_runner.render_prompt(
        row,
        rows,
        template,
        runner_timeout,
        use_cache=False,
        evidence_manifest_out=evidence_manifest,
        audit_invocation_id=invocation_id,
    )
    prompt, transport_bound = audit_runner.fit_prompt_to_transport_limit(
        prompt, evidence_manifest, cid
    )

    isolated = workdir / f"isolated-{key}-p{pass_no}"
    isolated.mkdir(parents=True, exist_ok=False)
    prompt_path = isolated / "AUDIT_TASK.md"
    prompt_path.write_text(prompt, encoding="utf-8")
    raw_output = workdir / f"raw-{key}-p{pass_no}.txt"
    delivery = workdir / f"delivery-{key}-p{pass_no}.json"
    log_path = workdir / f"log-{key}-p{pass_no}.txt"
    log_handle = log_path.open("w", encoding="utf-8")
    instruction = (
        "Open AUDIT_TASK.md in the current directory and follow it exactly. "
        "It is the complete restricted packet. Do not inspect any other file. "
        "Return only the response required by that packet."
    )
    proc = subprocess.Popen(
        [
            "codex", "exec", "--skip-git-repo-check", "--ignore-rules",
            "--sandbox", "read-only", "--model", MODEL,
            "-c", f"model_reasoning_effort='{REASONING}'",
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
        "row": row,
        "pass": pass_no,
        "proc": proc,
        "raw_output": raw_output,
        "delivery": delivery,
        "log_handle": log_handle,
        "evidence_manifest": evidence_manifest,
        "invocation_id": invocation_id,
        "transport_bound": transport_bound,
        "auditor": f"codex-audit-batch-{ident}",
        "independence": seat_independence(row, pass_no),
        "last_size": 0,
        "last_progress": now,
        "stalled": False,
    }


def wait_workers(jobs: list[dict], stall_minutes: int = 45) -> None:
    pending = set(range(len(jobs)))
    stall_seconds = stall_minutes * 60
    while pending:
        now = time.monotonic()
        for index in list(pending):
            job = jobs[index]
            output = job["raw_output"]
            size = output.stat().st_size if output.exists() else 0
            if size != job["last_size"]:
                job["last_size"] = size
                job["last_progress"] = now
            returncode = job["proc"].poll()
            if returncode is not None:
                job["returncode"] = returncode
                job["proc"].wait()
                pending.remove(index)
                continue
            if now - job["last_progress"] >= stall_seconds:
                job["stalled"] = True
                try:
                    os.killpg(job["proc"].pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                job["returncode"] = job["proc"].wait()
                pending.remove(index)
        if pending:
            time.sleep(2)
    for job in jobs:
        job["log_handle"].close()


def finalize_worker(job: dict) -> tuple[dict | None, dict]:
    cid = job["cid"]
    base = {"cid": cid, "pass": job["pass"]}
    if job["stalled"]:
        return None, {**base, "result": "stall_killed"}
    raw_output = job["raw_output"]
    if job.get("returncode") != 0:
        return None, {**base, "result": f"worker_exit_{job.get('returncode')}"}
    if not raw_output.exists() or raw_output.stat().st_size <= MIN_DELIVERY_BYTES:
        return None, {**base, "result": "no_size_qualified_delivery"}
    reply = audit_runner.extract_response(raw_output.read_text(encoding="utf-8"))
    compute_reason = audit_runner.compute_required_reason(reply)
    if compute_reason:
        return None, {**base, "result": "compute_required", "detail": compute_reason}
    blob = audit_runner.parse_verdict_json(reply or "")
    if blob is None:
        return None, {**base, "result": "malformed_json"}
    if blob.get("claim_type") == "no_go":
        return None, {**base, "result": "forensic_required_final_no_go"}

    row = job["row"]
    note_path = row.get("note_path") or ""
    note_body = ""
    if note_path:
        try:
            note_body = (REPO_ROOT / note_path).read_text(encoding="utf-8")
        except OSError:
            pass
    source_requires_no_go = audit_runner.no_go_discipline_gate.source_requires_no_go_discipline(
        note_path,
        note_body,
        row.get("claim_type") or row.get("claim_type_author_hint"),
    )
    error = audit_runner.validate_verdict(
        blob,
        cid,
        source_requires_no_go=source_requires_no_go,
        evidence_manifest=None,
        prior_claim_scope=audit_runner.prior_claim_scope_for_row(row),
        expected_invocation_id=job["invocation_id"],
        transport_bounded_n8=job["transport_bound"] is not None,
    )
    clipped = prompt_has_clipped_evidence(job["evidence_manifest"])
    if not error and blob.get("verdict") == "audited_clean" and clipped:
        error = f"audited_clean packet has clipped evidence: {clipped}"
    if error:
        return None, {**base, "result": "validation_failed", "detail": error}

    full_blob = audit_runner.add_auditor_metadata(
        blob,
        job["auditor"],
        AUDITOR_FAMILY,
        job["independence"],
        auditor_model=MODEL,
        auditor_reasoning_effort=REASONING,
    )
    envelope = {
        "audit": full_blob,
        "evidence_manifest": job["evidence_manifest"],
    }
    temporary = job["delivery"].with_suffix(".tmp")
    temporary.write_text(json.dumps(envelope, sort_keys=True), encoding="utf-8")
    temporary.replace(job["delivery"])
    return envelope, {**base, "result": "delivery_validated"}


def clean_main_error() -> str | None:
    branch = sh(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    if branch.returncode != 0:
        return "cannot determine current branch"
    if branch.stdout.strip() != "main":
        return f"not on main (currently {branch.stdout.strip()!r})"
    status = sh(["git", "status", "--porcelain"])
    if status.returncode != 0:
        return "cannot determine worktree status"
    if status.stdout.strip():
        return "working tree is not clean"
    return None


def sync_origin_main() -> tuple[bool, str]:
    error = clean_main_error()
    if error:
        return False, error
    fetch = sh(["git", "fetch", "origin", "main", "-q"])
    if fetch.returncode != 0:
        return False, f"fetch failed: {(fetch.stderr or fetch.stdout).strip()[:240]}"
    head = sh(["git", "rev-parse", "HEAD"]).stdout.strip()
    remote = sh(["git", "rev-parse", "origin/main"]).stdout.strip()
    if head == remote:
        return True, head
    ancestor = sh(["git", "merge-base", "--is-ancestor", head, remote])
    if ancestor.returncode != 0:
        return False, "local main is not a clean ancestor of origin/main"
    merge = sh(["git", "merge", "--ff-only", "origin/main"])
    if merge.returncode != 0:
        return False, f"fast-forward failed: {(merge.stderr or merge.stdout).strip()[:240]}"
    return True, remote


def changed_paths() -> list[str]:
    names = set(sh(["git", "diff", "--name-only"]).stdout.splitlines())
    names.update(sh(["git", "diff", "--name-only", "--cached"]).stdout.splitlines())
    names.update(sh(["git", "ls-files", "--others", "--exclude-standard"]).stdout.splitlines())
    return sorted(name for name in names if name)


def allowed_generated_path(path: str) -> bool:
    return any(
        path == allowed or path.startswith(allowed + "/")
        for allowed in audit_runner.AUDIT_DATA_FILES
    )


def run_apply_gates(envelope: dict) -> tuple[bool, str]:
    ok, message = audit_runner.apply_one(
        envelope["audit"],
        propagate=False,
        evidence_manifest=envelope["evidence_manifest"],
    )
    if not ok:
        return False, f"apply rejected: {message[:400]}"
    pipeline = sh(["bash", str(SCRIPTS / "run_pipeline.sh")], timeout=1800)
    if pipeline.returncode != 0:
        return False, f"pipeline failed: {(pipeline.stderr or pipeline.stdout)[-400:]}"
    lint = sh([sys.executable, str(SCRIPTS / "audit_lint.py"), "--strict"], timeout=600)
    if lint.returncode != 0:
        return False, f"strict lint failed: {(lint.stderr or lint.stdout)[-400:]}"
    diff_check = sh(["git", "diff", "--check"])
    if diff_check.returncode != 0:
        return False, f"git diff --check failed: {diff_check.stdout[-400:]}"
    unexpected = [path for path in changed_paths() if not allowed_generated_path(path)]
    if unexpected:
        return False, f"unexpected generated paths: {unexpected[:8]}"
    return True, "gates passed"


def stage_and_commit(message: str) -> tuple[bool, str]:
    paths = [path for path in audit_runner.AUDIT_DATA_FILES if (REPO_ROOT / path).exists()]
    add = sh(["git", "add", "--", *paths])
    if add.returncode != 0:
        return False, f"git add failed: {(add.stderr or add.stdout).strip()[:240]}"
    staged = sh(["git", "diff", "--cached", "--quiet"])
    if staged.returncode == 0:
        return False, "no generated audit change to commit"
    if staged.returncode != 1:
        return False, "cannot inspect staged audit diff"
    commit = sh(["git", "commit", "-q", "-m", message])
    if commit.returncode != 0:
        return False, f"commit failed: {(commit.stderr or commit.stdout).strip()[:240]}"
    committed = sh(["git", "rev-parse", "HEAD"])
    if committed.returncode != 0:
        return False, "cannot resolve created commit"
    return True, committed.stdout.strip()


def apply_one_serialized(
    job: dict,
    envelope: dict,
    retries: int,
) -> tuple[bool, dict]:
    cid = job["cid"]
    pass_no = job["pass"]
    verdict = envelope["audit"].get("verdict")
    for attempt in range(1, retries + 1):
        synced, detail = sync_origin_main()
        if not synced:
            return False, {"cid": cid, "pass": pass_no, "result": "sync_blocked", "detail": detail}
        gated, detail = run_apply_gates(envelope)
        if not gated:
            return False, {"cid": cid, "pass": pass_no, "result": "apply_or_gate_failed", "detail": detail}
        pass_word = "first" if pass_no == 1 else "second"
        committed, detail = stage_and_commit(
            f"audit: {cid} {verdict} (codex-cli, {MODEL}, {REASONING}, {pass_word}/batch)"
        )
        if not committed:
            return False, {"cid": cid, "pass": pass_no, "result": "commit_failed", "detail": detail}
        local_commit = detail
        push = sh(["git", "push", "-q", "origin", "HEAD:main"])
        if push.returncode == 0:
            return True, {"cid": cid, "pass": pass_no, "result": verdict, "commit": local_commit}

        fetch = sh(["git", "fetch", "origin", "main", "-q"])
        if fetch.returncode != 0:
            return False, {"cid": cid, "pass": pass_no, "result": "push_failed", "detail": "push and follow-up fetch failed"}
        landed = sh(["git", "merge-base", "--is-ancestor", local_commit, "origin/main"])
        if landed.returncode == 0:
            return True, {"cid": cid, "pass": pass_no, "result": verdict, "commit": local_commit}
        if attempt == retries:
            return False, {"cid": cid, "pass": pass_no, "result": "push_race_exhausted"}
        error = clean_main_error()
        if error:
            return False, {"cid": cid, "pass": pass_no, "result": "race_retry_dirty", "detail": error}
        reset = sh(["git", "reset", "--hard", "origin/main"])
        if reset.returncode != 0:
            return False, {"cid": cid, "pass": pass_no, "result": "race_reset_failed"}
    return False, {"cid": cid, "pass": pass_no, "result": "unreachable"}


def apply_serialized(
    jobs: list[dict],
    report: list[dict],
    retries: int = 3,
) -> bool:
    for job in sorted(jobs, key=lambda item: (item["cid"], item["pass"])):
        envelope, result = finalize_worker(job)
        if envelope is None:
            report.append(result)
            continue
        ok, result = apply_one_serialized(job, envelope, retries)
        report.append(result)
        if not ok:
            return False
    return True


def selected_batch(targets: list[dict], max_workers: int) -> list[dict]:
    selected: list[dict] = []
    used = 0
    for row in targets:
        seats = 2 if row.get("criticality") == "critical" else 1
        if seats > max_workers:
            continue
        if used + seats > max_workers:
            break
        selected.append(row)
        used += seats
    return selected


def scope_for_args(args: argparse.Namespace, rows: dict[str, dict]) -> set[str]:
    if args.lane:
        config = json.loads((DATA / "lane_certification_config.json").read_text(encoding="utf-8"))
        roots = [lane["root"] for lane in config.get("lanes", []) if lane.get("lane") == args.lane]
        if not roots:
            raise ValueError(f"unknown lane {args.lane!r}")
        return lane_closure(roots[0], rows)
    return {claim.strip() for claim in args.claims.split(",") if claim.strip()}


def main() -> int:
    parser = argparse.ArgumentParser(description="Parallel development-tier audit drainer")
    scope_group = parser.add_mutually_exclusive_group(required=True)
    scope_group.add_argument("--lane", help="lane name from lane_certification_config.json")
    scope_group.add_argument("--claims", help="comma-separated claim ids")
    parser.add_argument("--max-workers", type=int, default=6)
    parser.add_argument("--rounds", type=int, default=6)
    parser.add_argument("--stall-minutes", type=int, default=45)
    parser.add_argument("--runner-timeout-sec", type=int, default=120)
    parser.add_argument("--push-retries", type=int, default=3)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.max_workers < 1 or args.rounds < 1 or args.stall_minutes < 1:
        parser.error("worker, round, and stall limits must be positive")

    if not args.dry_run:
        error = clean_main_error()
        if error:
            print(f"refusing to run: {error}. Use a dedicated clean main checkout.")
            return 2

    workdir = Path(
        os.environ.get("AUDIT_BATCH_WORKDIR")
        or f"/tmp/audit_batch_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}_{uuid.uuid4().hex[:8]}"
    )
    report: list[dict] = []
    if not args.dry_run:
        workdir.mkdir(parents=True, exist_ok=False)

    for round_no in range(1, args.rounds + 1):
        rows = load_rows()
        try:
            scope = scope_for_args(args, rows)
        except ValueError as exc:
            print(str(exc))
            return 2
        targets, skipped = compute_targets(scope, rows)
        print(f"== round {round_no}: {len(targets)} dep-ready targets, {len(skipped)} skipped")
        for line in skipped:
            print(f"   skip: {line}")
        if not targets:
            break
        if args.dry_run:
            for row in targets:
                passes = 2 if row.get("criticality") == "critical" else 1
                print(f"   would audit: {row['claim_id']} (passes={passes})")
            break

        batch = selected_batch(targets, args.max_workers)
        if not batch:
            print("no target fits the configured worker limit (critical rows require two seats)")
            return 2
        jobs: list[dict] = []
        for row in batch:
            passes = 2 if row.get("criticality") == "critical" else 1
            for pass_no in range(1, passes + 1):
                jobs.append(
                    launch_worker(row, rows, pass_no, workdir, args.runner_timeout_sec)
                )
        print(f"   launched {len(jobs)} detached workers; waiting (stall {args.stall_minutes}m)")
        wait_workers(jobs, args.stall_minutes)
        if not apply_serialized(jobs, report, args.push_retries):
            break
        (workdir / "report.jsonl").write_text(
            "".join(json.dumps(item, sort_keys=True) + "\n" for item in report),
            encoding="utf-8",
        )

        current_rows = load_rows()
        disagreements = [
            row["claim_id"]
            for row in batch
            if (current_rows.get(row["claim_id"], {}).get("cross_confirmation") or {}).get("status")
            in {"disagreement", "three_way_disagreement", "disagreement_irresolvable"}
        ]
        if disagreements:
            for cid in disagreements:
                report.append({"cid": cid, "result": "judicial_panel_required"})
            break

    print("== batch report ==")
    for item in report:
        pass_label = f" p{item['pass']}" if "pass" in item else ""
        print(f"   {item['cid']}{pass_label}: {item['result']}")
    if not args.dry_run:
        (workdir / "report.jsonl").write_text(
            "".join(json.dumps(item, sort_keys=True) + "\n" for item in report),
            encoding="utf-8",
        )
        print(f"report: {workdir / 'report.jsonl'}")
    blockers = {
        "stall_killed", "no_size_qualified_delivery", "malformed_json",
        "forensic_required_final_no_go", "validation_failed", "sync_blocked",
        "apply_or_gate_failed", "commit_failed", "push_race_exhausted",
        "race_retry_dirty", "race_reset_failed", "judicial_panel_required",
    }
    return 1 if any(item.get("result") in blockers for item in report) else 0


if __name__ == "__main__":
    raise SystemExit(main())
