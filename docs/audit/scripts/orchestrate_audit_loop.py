#!/usr/bin/env python3
"""Canonical panel-aware backlog orchestrator for the audit lane.

The batch drainer deliberately stops a batch when fresh cross-seat
disagreement appears. This supervisor owns the missing control-flow edge:

    panel pending work -> drain lane -> panel new disagreement -> resume lane

It drains authenticated dispatch and cascade sources, prioritizes configured
flagship lanes, then drains every remaining eligible development-tier row.
Every independent clone runs this same complete loop. A per-session worker id
only disperses target ordering; current ``origin/main`` plus the existing
delivery-supersession and fast-forward transaction checks remain the authority.
Duplicate computation is harmless and is discarded when another worker lands
first. Auditor fan-out remains inside the existing batch and judicial
orchestrators; this process never authors or edits verdict content.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import TextIO


SCRIPTS = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS.parents[2]
DATA = REPO_ROOT / "docs" / "audit" / "data"
PANEL = SCRIPTS / "orchestrate_judicial_panel.py"
BATCH = SCRIPTS / "orchestrate_audit_batch.py"
FORENSIC = REPO_ROOT / "scripts" / "codex_audit_runner.py"
CONFIG = DATA / "lane_certification_config.json"
CERTIFICATION = DATA / "lane_certification.json"
QUEUE = DATA / "audit_queue.json"

sys.path.insert(0, str(SCRIPTS))
import orchestrate_audit_batch as batch  # noqa: E402


PROGRESS = {
    "started": time.monotonic(),
    "phase": "startup",
    "pass": 0,
    "lane": None,
    "attempts": 0,
    "failures": [],
    "panel_state": "not_started",
    "canary_state": "not_started",
    "last_canary_claim_id": None,
    "last_canary_terminal_phase": None,
    "last_canary_source": None,
    "worker_id": None,
    "baseline_status": {},
    "quarantine_file": None,
}
_STOP_HEARTBEAT = threading.Event()
_DRAIN_LOCK_HANDLE: TextIO | None = None


def emit(message: str) -> None:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{now}] {message}", flush=True)


def ready_row_count() -> int | None:
    try:
        payload = json.loads(QUEUE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return sum(1 for row in payload.get("queue", []) if row.get("ready"))


def remaining_blocker_count() -> int | None:
    try:
        payload = json.loads(CERTIFICATION.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    lanes = payload.get("lanes", payload) if isinstance(payload, dict) else payload
    if isinstance(lanes, dict):
        rows = lanes.values()
    elif isinstance(lanes, list):
        rows = lanes
    else:
        return None
    return sum(
        len(row.get("blocking", []) or [])
        for row in rows
        if isinstance(row, dict)
    )


def campaign_exclusion_counts() -> Counter:
    path = PROGRESS.get("quarantine_file")
    if not isinstance(path, Path):
        return Counter()
    pairs = {
        (record["claim_id"], record["reason"])
        for record in batch.load_campaign_exclusion_records(path)
    }
    return Counter(reason for _cid, reason in pairs)


def campaign_exclusion_keys(path: Path | None) -> set[tuple[str, str]]:
    return {
        (record["claim_id"], record["reason"])
        for record in batch.load_campaign_exclusion_records(path)
    }


def campaign_exclusion_count(reason: str) -> int:
    return campaign_exclusion_counts()[reason]


def schema_quarantine_count() -> int:
    return campaign_exclusion_count(batch.SCHEMA_QUARANTINE_RESULT)


def blocked_row_reentry_count() -> int:
    return campaign_exclusion_count(batch.BLOCKED_ROW_QUARANTINE_RESULT)


def compute_quarantine_count() -> int:
    return campaign_exclusion_count(batch.COMPUTE_QUARANTINE_RESULT)


def claim_transaction_quarantine_count() -> int:
    return campaign_exclusion_count(batch.CLAIM_TRANSACTION_QUARANTINE_RESULT)


def audit_status_snapshot() -> dict[str, str | None]:
    """Read the materialized ledger without refreshing or rewriting caches."""
    ledger_cache = DATA / "audit_ledger.json"
    try:
        payload = json.loads(ledger_cache.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return {
        cid: row.get("audit_status")
        for cid, row in payload.get("rows", {}).items()
        if isinstance(row, dict)
    }


def landed_verdict_counts() -> Counter:
    baseline = PROGRESS.get("baseline_status") or {}
    if not baseline:
        return Counter()
    current = audit_status_snapshot()
    return Counter(
        str(status)
        for cid, status in current.items()
        if status != baseline.get(cid) and str(status or "").startswith("audited_")
    )


def summary_line(final: bool = False) -> str:
    elapsed = int(time.monotonic() - PROGRESS["started"])
    verdicts = landed_verdict_counts()
    verdict_text = ",".join(
        f"{name}:{count}" for name, count in verdicts.most_common()
    ) or "none"
    failures = Counter(PROGRESS.get("failures") or [])
    failure_text = ",".join(
        f"{reason}:{count}" for reason, count in failures.most_common(3)
    ) or "none"
    ready = ready_row_count()
    blockers = remaining_blocker_count()
    try:
        exclusions = campaign_exclusion_counts()
        schema_count: int | str = exclusions[batch.SCHEMA_QUARANTINE_RESULT]
        compute_count: int | str = exclusions[batch.COMPUTE_QUARANTINE_RESULT]
        transaction_count: int | str = exclusions[
            batch.CLAIM_TRANSACTION_QUARANTINE_RESULT
        ]
        blocked_count: int | str = exclusions[
            batch.BLOCKED_ROW_QUARANTINE_RESULT
        ]
    except (OSError, ValueError):
        # The main control path treats malformed campaign state as a hard stop.
        # Heartbeat/final summaries remain printable without hiding that state.
        schema_count = compute_count = transaction_count = blocked_count = "invalid"
    return (
        f"== audit-loop {'final ' if final else ''}summary "
        f"elapsed={elapsed // 3600}h{(elapsed % 3600) // 60:02d}m "
        f"phase={PROGRESS['phase']} pass={PROGRESS['pass']} "
        f"lane={PROGRESS['lane'] or '-'} attempts={PROGRESS['attempts']} "
        f"worker_id={PROGRESS['worker_id'] or '-'} "
        f"failures={sum(failures.values())} top_failure_reasons={failure_text} "
        f"verdicts_landed={verdict_text} panel_reseat={PROGRESS['panel_state']} "
        f"canary={PROGRESS['canary_state']} "
        f"ready_rows={ready if ready is not None else 'unknown'} "
        f"remaining_lane_blockers={blockers if blockers is not None else 'unknown'} "
        f"schema_quarantined={schema_count} "
        f"compute_quarantined={compute_count} "
        f"transaction_quarantined={transaction_count} "
        f"blocked_row_reentries={blocked_count}"
    )


def heartbeat() -> None:
    while not _STOP_HEARTBEAT.wait(15 * 60):
        emit(summary_line())


def git_head() -> str:
    proc = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return proc.stdout.strip()


def run_command(label: str, command: list[str], env: dict[str, str] | None = None) -> int:
    PROGRESS["phase"] = label
    PROGRESS["attempts"] += 1
    if label.startswith("panel-"):
        PROGRESS["panel_state"] = f"running:{label}"
    if label.startswith("forensic-canary-"):
        PROGRESS["canary_state"] = f"running:{label}"
    emit(f"START {label}: {' '.join(command)}")
    child_env = dict(os.environ) if env is None else dict(env)
    pass_fds: tuple[int, ...] = ()
    if _DRAIN_LOCK_HANDLE is not None:
        lock_fd = _DRAIN_LOCK_HANDLE.fileno()
        child_env[batch.INHERITED_DRAIN_LOCK_FD_ENV] = str(lock_fd)
        pass_fds = (lock_fd,)
    proc = subprocess.run(
        command,
        cwd=REPO_ROOT,
        env=child_env,
        pass_fds=pass_fds,
    )
    if label.startswith("panel-"):
        state = "complete" if proc.returncode == 0 else f"failed_exit_{proc.returncode}"
        PROGRESS["panel_state"] = f"{state}:{label}"
    if label.startswith("forensic-canary-"):
        state = "complete" if proc.returncode == 0 else f"failed_exit_{proc.returncode}"
        PROGRESS["canary_state"] = f"{state}:{label}"
    if proc.returncode != 0:
        PROGRESS["failures"].append(f"{label}:exit={proc.returncode}")
    emit(f"END {label}: exit={proc.returncode} head={git_head()}")
    return proc.returncode


def _lane_names(payload: object) -> list[str]:
    lanes = payload.get("lanes", payload) if isinstance(payload, dict) else payload
    if isinstance(lanes, dict):
        return list(lanes)
    if isinstance(lanes, list):
        return [
            name
            for entry in lanes
            if isinstance(entry, dict)
            for name in [entry.get("name") or entry.get("lane")]
            if isinstance(name, str) and name
        ]
    return []


def configured_lane_names() -> list[str]:
    return _lane_names(json.loads(CONFIG.read_text(encoding="utf-8")))


def validate_requested_lanes(requested: list[str] | None) -> None:
    if not requested:
        return
    known = configured_lane_names()
    unknown = [name for name in requested if name not in known]
    if unknown:
        raise ValueError(f"unknown lane(s): {', '.join(unknown)}")


def blocking_lanes(requested: list[str] | None = None) -> list[tuple[str, int]]:
    certification = json.loads(CERTIFICATION.read_text(encoding="utf-8"))
    names = configured_lane_names()
    if requested:
        validate_requested_lanes(requested)
        names = [name for name in names if name in requested]
    cert_lanes = (
        certification.get("lanes", certification)
        if isinstance(certification, dict)
        else certification
    )
    result: list[tuple[str, int]] = []
    for name in names:
        if isinstance(cert_lanes, dict):
            row = cert_lanes.get(name, {})
        else:
            row = next(
                (
                    entry
                    for entry in cert_lanes
                    if isinstance(entry, dict)
                    and (entry.get("name") or entry.get("lane")) == name
                ),
                {},
            )
        blockers = row.get("blocking", []) or []
        if blockers:
            result.append((name, len(blockers)))
    return result


def panel_command(args: argparse.Namespace) -> list[str]:
    command = [
        sys.executable,
        str(PANEL),
        "--stall-minutes",
        str(args.stall_minutes),
        "--runner-timeout-sec",
        str(args.runner_timeout_sec),
        "--push-retries",
        str(args.push_retries),
    ]
    if args.dry_run:
        command.append("--dry-run")
    return command


def batch_command(
    lane: str | None,
    args: argparse.Namespace,
    source: str | None = None,
) -> list[str]:
    command = [
        sys.executable,
        str(BATCH),
        "--max-workers",
        str(args.max_workers),
        "--rounds",
        str(args.batch_rounds),
        "--stall-minutes",
        str(args.stall_minutes),
        "--runner-timeout-sec",
        str(args.runner_timeout_sec),
        "--push-retries",
        str(args.push_retries),
    ]
    if source == "dispatch":
        command.append("--from-dispatch")
    elif source == "reaudit":
        command.append("--from-reaudit-candidates")
    elif source is not None:
        raise ValueError(f"unknown audit source {source!r}")
    elif lane is None:
        command.append("--all")
    else:
        command.extend(["--lane", lane])
    worker_id = getattr(args, "worker_id", "")
    if worker_id:
        command.extend(["--worker-id", worker_id])
    quarantine_file = getattr(args, "campaign_quarantine_file", None)
    if quarantine_file is not None:
        command.extend(["--campaign-quarantine-file", str(quarantine_file)])
    selection_skip_file = getattr(args, "campaign_selection_skip_file", None)
    if selection_skip_file is not None:
        command.extend(
            ["--campaign-selection-skip-file", str(selection_skip_file)]
        )
    if getattr(args, "dispatch_science_fixes", False):
        command.append("--dispatch-science-fixes")
    if args.dry_run:
        command.append("--dry-run")
    return command


def run_panel(args: argparse.Namespace, label: str) -> int:
    return run_command(label, panel_command(args))


def drain_lane(
    lane: str | None,
    args: argparse.Namespace,
    source: str | None = None,
) -> tuple[int, bool]:
    """Drain one scoped phase and panel after every batch."""
    made_progress = False
    label = f"{source}-source" if source else (lane or "global-development")
    for cycle in itertools.count(1):
        if args.max_lane_cycles and cycle > args.max_lane_cycles:
            emit(f"STOP lane cycle safety bound reached: lane={label}")
            return 4, made_progress
        before = git_head()
        before_exclusions = campaign_exclusion_keys(
            getattr(args, "campaign_quarantine_file", None)
        )
        batch_rc = run_command(
            f"batch-{label}-cycle-{cycle}",
            batch_command(lane, args, source=source),
        )
        # This is intentionally unconditional, including after a hard batch
        # result: another row in the same batch may already have recorded a
        # panel-eligible disagreement. Preserve the hard result only after the
        # judicial sweep has consumed every resumable handoff.
        panel_rc = run_panel(args, f"panel-after-{label}-cycle-{cycle}")
        if panel_rc != 0:
            return panel_rc, made_progress
        if batch_rc != 0:
            return batch_rc, made_progress
        after = git_head()
        after_exclusions = campaign_exclusion_keys(
            getattr(args, "campaign_quarantine_file", None)
        )
        if after == before and after_exclusions == before_exclusions:
            return 0, made_progress
        made_progress = True
        if args.dry_run:
            return 0, made_progress


def first_ready_forensic_claim(
    excluded_claim_ids: set[str] | None = None,
    *,
    include_alternate_sources: bool = False,
) -> str | None:
    PROGRESS["last_canary_source"] = None
    excluded = excluded_claim_ids or set()
    if include_alternate_sources:
        ledger_rows = batch.load_rows()
        for source in ("dispatch", "reaudit"):
            for row in batch.source_queue_rows(source, ledger_rows):
                claim_id = row.get("claim_id")
                if (
                    not isinstance(claim_id, str)
                    or not claim_id
                    or claim_id in excluded
                ):
                    continue
                role, independence = batch.audit_runner.determine_audit_role(
                    ledger_rows.get(claim_id) or {},
                    batch.AUDITOR_FAMILY,
                    is_reaudit_candidate=True,
                    is_dispatch_target=(source == "dispatch"),
                )
                if role == "skip" or independence == "weak":
                    continue
                if batch.source_requires_forensic(
                    ledger_rows.get(claim_id) or row
                ):
                    PROGRESS["last_canary_source"] = source
                    return claim_id
    if not QUEUE.exists():
        return None
    rows = json.loads(QUEUE.read_text(encoding="utf-8")).get("queue", [])
    for row in rows:
        if (
            row.get("ready")
            and row.get("audit_status") in {"unaudited", "audit_in_progress"}
            and batch.source_requires_forensic(row)
        ):
            claim_id = row.get("claim_id")
            if (
                isinstance(claim_id, str)
                and claim_id
                and claim_id not in excluded
            ):
                return claim_id
    return None


def forensic_canary_terminal_record(
    run_log: Path,
    claim_id: str,
) -> dict | None:
    """Return the last target-scoped terminal record from one canary log."""
    if not run_log.is_file():
        return None
    records: list[dict] = []
    for line_number, line in enumerate(
        run_log.read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        if not line.strip():
            raise ValueError(f"{run_log}:{line_number}: blank canary log record")
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"{run_log}:{line_number}: invalid canary log JSON: {exc.msg}"
            ) from exc
        if not isinstance(record, dict):
            raise ValueError(
                f"{run_log}:{line_number}: canary log record is not an object"
            )
        if record.get("claim_id") in {None, claim_id}:
            records.append(record)

    terminal_phases = {
        "applied",
        "apply_failed",
        "applied_propagation_failed",
        "push_failed",
        "codex_failed",
        "extract_failed",
        "json_parse_failed",
        "validate_failed",
        "compute_required",
        "skip_no_runner_log",
        "skip_prompt_transport",
        "skip_role",
        "weak_clean_unratifiable",
        "remote_state_superseded",
        "source_refresh_failed",
        "dry-run",
    }
    return next(
        (
            record
            for record in reversed(records)
            if record.get("phase") in terminal_phases
        ),
        None,
    )


def forensic_canary_claim_local_failure(
    terminal: dict | None,
    claim_id: str,
    run_log: Path,
) -> tuple[str, dict, int] | None:
    """Classify typed claim-local no-verdict outcomes and their expected exit.

    Unknown execution, apply, propagation, and push failures remain hard. A
    malformed or schema-invalid packet minted no verdict and is safe to
    quarantine for this campaign. Missing runner evidence is compute work, not
    negative science.
    """
    if terminal is None:
        return None
    phase = terminal["phase"]
    if phase == "validate_failed":
        detail = str(terminal.get("error") or "").strip()
        if not detail or detail.startswith(
            (
                "fresh schema retry codex exec failed:",
                "validation repair codex exec failed:",
            )
        ):
            return None
        return batch.SCHEMA_QUARANTINE_RESULT, {
            "cid": claim_id,
            "pass": 1,
            "result": "validation_failed",
            "detail": f"{detail}; preserved_run_log={run_log.name}",
        }, 1
    if phase == "json_parse_failed":
        return batch.SCHEMA_QUARANTINE_RESULT, {
            "cid": claim_id,
            "pass": 1,
            "result": "malformed_json",
        }, 1
    if phase == "skip_prompt_transport":
        detail = str(
            terminal.get("reason")
            or "forensic canary prompt exceeded the bounded transport"
        ).strip()
        return batch.SCHEMA_QUARANTINE_RESULT, {
            "cid": claim_id,
            "pass": 1,
            "result": "validation_failed",
            "detail": f"{detail}; preserved_run_log={run_log.name}",
        }, 0
    if phase in {"compute_required", "skip_no_runner_log"}:
        detail = str(
            terminal.get("reason")
            or terminal.get("runner_path")
            or "forensic canary requires a current runner artifact"
        ).strip()
        return batch.COMPUTE_QUARANTINE_RESULT, {
            "cid": claim_id,
            "pass": 1,
            "result": "compute_required",
            "detail": detail,
        }, 0
    return None


def run_forensic_canary(
    args: argparse.Namespace,
    extra_excluded: set[str] | None = None,
) -> int:
    PROGRESS["last_canary_claim_id"] = None
    PROGRESS["last_canary_terminal_phase"] = None
    PROGRESS["last_canary_source"] = None
    try:
        excluded = batch.load_campaign_quarantine(
            args.campaign_quarantine_file
        )
    except (OSError, ValueError) as exc:
        emit(f"invalid campaign state before forensic canary: {exc}")
        return 2
    excluded.update(extra_excluded or set())
    try:
        claim_id = first_ready_forensic_claim(
            excluded,
            include_alternate_sources=True,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        emit(f"cannot authenticate forensic selection sources: {exc}")
        return 2
    if not claim_id:
        PROGRESS["canary_state"] = "no_ready_target"
        emit("no ready forensic-tier row available for the forensic canary")
        return 0
    PROGRESS["last_canary_claim_id"] = claim_id
    run_log = args.campaign_workdir / (
        f"forensic-canary-{batch.artifact_key(claim_id)}-"
        f"{uuid.uuid4().hex[:8]}.jsonl"
    )
    command = [
        sys.executable,
        str(FORENSIC),
        "--claim-id",
        claim_id,
        "--push-mode",
        "none" if args.dry_run else "per-verdict",
        "--codex-timeout-sec",
        str(args.codex_timeout_sec),
        "--runner-timeout-sec",
        str(args.runner_timeout_sec),
        "--validation-repair-attempts",
        "1",
        "--fresh-schema-retry-attempts",
        "3",
        "--run-log-path",
        str(run_log),
    ]
    canary_source = PROGRESS.get("last_canary_source")
    if canary_source == "dispatch":
        command.append("--from-dispatch")
    elif canary_source == "reaudit":
        command.append("--from-reaudit-candidates")
    if args.dry_run:
        command.append("--dry-run")
    env = dict(os.environ)
    env["AUDIT_FORENSIC_MODE"] = "1"
    rc = run_command(f"forensic-canary-{claim_id}", command, env=env)
    try:
        terminal = forensic_canary_terminal_record(run_log, claim_id)
    except (OSError, ValueError) as exc:
        emit(f"invalid forensic canary artifact; refusing quarantine: {exc}")
        return 2
    PROGRESS["last_canary_terminal_phase"] = (
        terminal.get("phase") if terminal else None
    )
    claim_local = forensic_canary_claim_local_failure(
        terminal,
        claim_id,
        run_log,
    )
    if claim_local is None:
        if rc != 0:
            return rc
        terminal_phase = terminal.get("phase") if terminal else None
        if terminal_phase in {"applied", "remote_state_superseded"} or (
            args.dry_run and terminal_phase == "dry-run"
        ):
            return 0
        emit(
            "forensic canary returned success without an applied verdict, "
            "typed quarantine, or dry-run terminal record; failing closed: "
            f"claim={claim_id} terminal={terminal_phase or 'missing'}"
        )
        return 2

    reason, failure, expected_rc = claim_local
    if rc != expected_rc:
        emit(
            "forensic canary terminal/exit mismatch; refusing claim-local "
            f"quarantine: claim={claim_id} terminal={terminal['phase']} "
            f"expected_exit={expected_rc} actual_exit={rc}"
        )
        return rc if rc != 0 else 2
    if reason == batch.SCHEMA_QUARANTINE_RESULT:
        batch.persist_campaign_quarantine(
            args.campaign_quarantine_file,
            {claim_id},
            [failure],
        )
    elif reason == batch.COMPUTE_QUARANTINE_RESULT:
        batch.persist_compute_required_skips(
            args.campaign_quarantine_file,
            {claim_id},
            [failure],
        )
    else:
        emit(f"unsupported forensic canary quarantine reason: {reason}")
        return 2
    try:
        batch.load_campaign_exclusion_records(args.campaign_quarantine_file)
    except (OSError, ValueError) as exc:
        emit(f"forensic canary quarantine did not validate: {exc}")
        return 2
    PROGRESS["canary_state"] = f"quarantined:{reason}:{claim_id}"
    emit(
        "forensic canary minted no verdict and was quarantined claim-locally: "
        f"claim={claim_id} reason={reason} artifact={run_log}"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Panel-aware end-to-end audit backlog drainer"
    )
    parser.add_argument("--lane", action="append", help="limit to a configured lane")
    parser.add_argument("--max-workers", type=int, default=4)
    parser.add_argument(
        "--worker-id",
        default=os.environ.get("AUDIT_WORKER_ID", ""),
        help=(
            "optional session identifier used only to disperse target ordering; "
            "a unique id is generated when omitted"
        ),
    )
    parser.add_argument(
        "--max-passes",
        type=int,
        default=0,
        help="full-pass safety bound; 0 drains to a fixed point (default)",
    )
    parser.add_argument(
        "--max-lane-cycles",
        type=int,
        default=0,
        help="per-lane batch/panel safety bound; 0 drains to a fixed point (default)",
    )
    parser.add_argument("--batch-rounds", type=int, default=6)
    parser.add_argument("--stall-minutes", type=int, default=45)
    parser.add_argument("--runner-timeout-sec", type=int, default=120)
    parser.add_argument("--codex-timeout-sec", type=int, default=2700)
    parser.add_argument("--push-retries", type=int, default=3)
    parser.add_argument(
        "--campaign-workdir",
        type=Path,
        default=None,
        help="preserve campaign-scoped quarantine/report artifacts in this directory",
    )
    parser.add_argument(
        "--dispatch-science-fixes",
        action="store_true",
        help=(
            "launch PR-producing repair workers after complete validated "
            "non-clean verdicts; requires an explicit source-repair request"
        ),
    )
    parser.add_argument("--skip-forensic-canary", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    global _DRAIN_LOCK_HANDLE
    args = build_parser().parse_args(argv)
    positive = (
        args.max_workers,
        args.batch_rounds,
        args.stall_minutes,
        args.runner_timeout_sec,
        args.codex_timeout_sec,
        args.push_retries,
    )
    if any(value < 1 for value in positive):
        raise SystemExit("worker, round, timeout, and retry values must be positive")
    if args.max_passes < 0 or args.max_lane_cycles < 0:
        raise SystemExit("pass and cycle safety bounds must be non-negative")
    args.worker_id = args.worker_id.strip() or f"worker-{uuid.uuid4().hex[:12]}"
    PROGRESS["worker_id"] = args.worker_id
    emit(
        "optimistic worker identity: "
        f"{args.worker_id} (ordering hint only; origin/main is authoritative)"
    )
    campaign_dir = args.campaign_workdir or Path(
        tempfile.mkdtemp(prefix="audit_loop_campaign_")
    )
    campaign_dir.mkdir(parents=True, exist_ok=True)
    args.campaign_quarantine_file = campaign_dir / "campaign-row-exclusions.jsonl"
    args.campaign_selection_skip_file = (
        campaign_dir / "campaign-selector-skips.jsonl"
    )
    args.campaign_workdir = campaign_dir
    PROGRESS["quarantine_file"] = args.campaign_quarantine_file
    emit(f"campaign artifacts: {campaign_dir}")
    try:
        validate_requested_lanes(args.lane)
        batch.load_campaign_exclusion_records(args.campaign_quarantine_file)
        batch.load_campaign_selection_skip_records(
            args.campaign_selection_skip_file
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        emit(str(exc))
        return 2
    if not args.dry_run:
        _DRAIN_LOCK_HANDLE = batch.acquire_exclusive_drain_lock(
            "orchestrate_audit_loop"
        )
        if _DRAIN_LOCK_HANDLE is None:
            return 3
        error = batch.clean_main_error()
        if error:
            emit(f"refusing to run: {error}. Use a dedicated clean main checkout.")
            _DRAIN_LOCK_HANDLE.close()
            _DRAIN_LOCK_HANDLE = None
            return 2
        ok, detail = batch.sync_origin_main()
        if not ok:
            emit(f"refusing to run: {detail}")
            _DRAIN_LOCK_HANDLE.close()
            _DRAIN_LOCK_HANDLE = None
            return 2

    PROGRESS["baseline_status"] = audit_status_snapshot()
    PROGRESS["started"] = time.monotonic()
    PROGRESS["attempts"] = 0
    PROGRESS["failures"] = []
    PROGRESS["panel_state"] = "not_started"
    PROGRESS["canary_state"] = "not_started"
    PROGRESS["last_canary_claim_id"] = None
    PROGRESS["last_canary_terminal_phase"] = None
    PROGRESS["last_canary_source"] = None
    forensic_attempted: set[str] = set()
    _STOP_HEARTBEAT.clear()
    thread = threading.Thread(target=heartbeat, daemon=True)
    thread.start()
    try:
        for pass_number in itertools.count(1):
            if args.max_passes and pass_number > args.max_passes:
                emit("STOP pass safety bound reached")
                return 4
            PROGRESS["pass"] = pass_number
            PROGRESS["lane"] = None
            before = git_head()
            rc = run_panel(args, f"panel-pass-{pass_number}-opening")
            if rc != 0:
                return rc
            if not args.lane:
                for source in ("dispatch", "reaudit"):
                    PROGRESS["lane"] = f"{source}-source"
                    emit(f"draining ready {source} source rows")
                    rc, _ = drain_lane(None, args, source=source)
                    if rc != 0:
                        return rc
            try:
                lanes = blocking_lanes(args.lane)
            except ValueError as exc:
                emit(str(exc))
                return 2
            emit(
                "blocking lanes: "
                + (", ".join(f"{lane}={count}" for lane, count in lanes) or "none")
            )
            for lane, count in lanes:
                PROGRESS["lane"] = lane
                emit(f"draining lane={lane} blockers_at_selection={count}")
                rc, _ = drain_lane(lane, args)
                if rc != 0:
                    return rc
            if not args.lane:
                PROGRESS["lane"] = "global-development"
                emit("draining every remaining eligible development-tier row")
                rc, _ = drain_lane(None, args)
                if rc != 0:
                    return rc
            if not args.dry_run:
                synced, detail = batch.sync_origin_main()
                if not synced:
                    emit(f"cannot verify remote-stable fixed point: {detail}")
                    return 2
            after = git_head()
            emit(f"development pass {pass_number}: before={before} after={after}")
            if after == before:
                try:
                    exclusions = campaign_exclusion_counts()
                except (OSError, ValueError) as exc:
                    emit(f"invalid campaign state; refusing fixed point: {exc}")
                    return 2
                emit(
                    "worker-local development fixed point reached: "
                    "fresh full pass landed nothing new"
                )
                if exclusions[batch.SCHEMA_QUARANTINE_RESULT]:
                    emit(
                        "fixed point excludes campaign-scoped schema-invalid "
                        f"quarantines: {args.campaign_quarantine_file}"
                    )
                if exclusions[batch.BLOCKED_ROW_QUARANTINE_RESULT]:
                    emit(
                        "fixed point excludes post-verdict rows that immediately "
                        "re-entered dep-ready selection; all other eligible rows "
                        f"were drained: {args.campaign_quarantine_file}"
                    )
                if exclusions[batch.COMPUTE_QUARANTINE_RESULT]:
                    emit(
                        "fixed point excludes compute-required rows until their "
                        "runner cache, sliced certificate, or independent "
                        f"derivation is repaired: {args.campaign_quarantine_file}"
                    )
                if exclusions[batch.CLAIM_TRANSACTION_QUARANTINE_RESULT]:
                    emit(
                        "fixed point excludes claim-local apply/gate failures "
                        "whose rollback to origin/main was verified; repair the "
                        "recorded operational cause before a new campaign: "
                        f"{args.campaign_quarantine_file}"
                    )
                if args.campaign_selection_skip_file.exists():
                    emit(
                        "typed selector-skip repair inventory: "
                        f"{args.campaign_selection_skip_file}"
                    )
                if (
                    args.skip_forensic_canary
                    or args.lane
                ):
                    return 0
                forensic_before = after
                rc = run_forensic_canary(args, forensic_attempted)
                if rc != 0:
                    return rc
                if args.dry_run:
                    return 0
                synced, detail = batch.sync_origin_main()
                if not synced:
                    emit(f"cannot reconcile forensic result with origin/main: {detail}")
                    return 2
                forensic_after = git_head()
                canary_claim = PROGRESS.get("last_canary_claim_id")
                if (
                    PROGRESS.get("last_canary_terminal_phase")
                    == "remote_state_superseded"
                ):
                    emit(
                        "forensic seat was superseded by remote source/state "
                        "movement; returning to development for fresh selection"
                    )
                    continue
                if forensic_after != forensic_before:
                    if isinstance(canary_claim, str) and canary_claim:
                        current_rows = batch.load_rows()
                        current_row = current_rows.get(canary_claim) or {}
                        canary_source = PROGRESS.get("last_canary_source")
                        cross_status = (
                            current_row.get("cross_confirmation") or {}
                        ).get("status")
                        awaiting_second = (
                            current_row.get("audit_status") == "audit_in_progress"
                            and cross_status == "awaiting_second"
                        )
                        if not awaiting_second:
                            forensic_attempted.add(canary_claim)
                        reentry_reason = None
                        if canary_source in {"dispatch", "reaudit"}:
                            try:
                                source_ids = {
                                    row.get("claim_id")
                                    for row in batch.source_queue_rows(
                                        str(canary_source),
                                        current_rows,
                                    )
                                }
                            except (
                                OSError,
                                ValueError,
                                json.JSONDecodeError,
                            ) as exc:
                                emit(
                                    "cannot authenticate post-forensic source "
                                    f"state: {exc}"
                                )
                                return 2
                            if canary_claim in source_ids:
                                reentry_reason = (
                                    f"{canary_source}_selection_still_live_"
                                    "after_applied_verdict"
                                )
                        elif (
                            current_row.get("audit_status") == "unaudited"
                            and batch.source_requires_forensic(current_row)
                        ):
                            reentry_reason = batch._latest_invalidation_reason(
                                current_row
                            )
                        if reentry_reason is not None:
                            batch.persist_blocked_row_reentries(
                                args.campaign_quarantine_file,
                                {canary_claim: reentry_reason},
                            )
                            forensic_attempted.add(canary_claim)
                            emit(
                                "forensic verdict re-entered the unchanged "
                                "ready queue and was excluded for this campaign: "
                                f"claim={canary_claim} reason={reentry_reason}"
                            )
                    emit(
                        "forensic row landed; returning to development because "
                        "the new verdict may unblock additional dependencies"
                    )
                    continue
                if isinstance(canary_claim, str) and canary_claim:
                    forensic_attempted.add(canary_claim)
                    if PROGRESS.get("last_canary_terminal_phase") == "applied":
                        reason = (
                            "applied_forensic_verdict_produced_no_canonical_"
                            "state_change"
                        )
                        batch.persist_blocked_row_reentries(
                            args.campaign_quarantine_file,
                            {canary_claim: reason},
                        )
                        emit(
                            "forensic apply produced no canonical commit and "
                            "was excluded for this campaign: "
                            f"claim={canary_claim} reason={reason}"
                        )
                        continue
                    emit(
                        "forensic row minted no verdict and is excluded for "
                        "this campaign; advancing to the next ready forensic row"
                    )
                    continue
                return 0
    finally:
        _STOP_HEARTBEAT.set()
        emit(summary_line(final=True))
        if _DRAIN_LOCK_HANDLE is not None:
            _DRAIN_LOCK_HANDLE.close()
            _DRAIN_LOCK_HANDLE = None


if __name__ == "__main__":
    raise SystemExit(main())
