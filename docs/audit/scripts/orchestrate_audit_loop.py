#!/usr/bin/env python3
"""Canonical panel-aware backlog orchestrator for the audit lane.

The batch drainer deliberately stops a batch when fresh cross-seat
disagreement appears. This supervisor owns the missing control-flow edge:

    panel pending work -> drain lane -> panel new disagreement -> resume lane

It repeats configured lanes until a complete pass lands no commits, then runs
one forensic no-go canary unless explicitly disabled. Auditor fan-out remains
inside the existing batch and judicial orchestrators; this process never
authors or edits verdict content.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
import re
import signal
import subprocess
import sys
import tempfile
import threading
import time
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
    "baseline_status": {},
    "quarantine_file": None,
}
_STOP_HEARTBEAT = threading.Event()
_STOP_REQUESTED = threading.Event()
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


def campaign_exclusion_count(reason: str) -> int:
    path = PROGRESS.get("quarantine_file")
    if not isinstance(path, Path) or not path.exists():
        return 0
    claim_ids: set[str] = set()
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return 0
    for line in lines:
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        cid = row.get("claim_id") if isinstance(row, dict) else None
        if isinstance(cid, str) and cid and row.get("reason") == reason:
            claim_ids.add(cid)
    return len(claim_ids)


def schema_quarantine_count() -> int:
    return campaign_exclusion_count(batch.SCHEMA_QUARANTINE_RESULT)


def blocked_row_reentry_count() -> int:
    return campaign_exclusion_count(batch.BLOCKED_ROW_QUARANTINE_RESULT)


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
    return (
        f"== audit-loop {'final ' if final else ''}summary "
        f"elapsed={elapsed // 3600}h{(elapsed % 3600) // 60:02d}m "
        f"phase={PROGRESS['phase']} pass={PROGRESS['pass']} "
        f"lane={PROGRESS['lane'] or '-'} attempts={PROGRESS['attempts']} "
        f"failures={sum(failures.values())} top_failure_reasons={failure_text} "
        f"verdicts_landed={verdict_text} panel_reseat={PROGRESS['panel_state']} "
        f"canary={PROGRESS['canary_state']} "
        f"ready_rows={ready if ready is not None else 'unknown'} "
        f"remaining_lane_blockers={blockers if blockers is not None else 'unknown'} "
        f"schema_quarantined={schema_quarantine_count()} "
        f"blocked_row_reentries={blocked_row_reentry_count()}"
    )


def heartbeat() -> None:
    while not _STOP_HEARTBEAT.wait(15 * 60):
        emit(summary_line())


def append_campaign_event(event: dict) -> None:
    campaign_dir = PROGRESS.get("campaign_dir")
    if not isinstance(campaign_dir, Path):
        return
    path = campaign_dir / "campaign-events.jsonl"
    payload = {
        "schema": "audit_loop_campaign_event_v1",
        "at": datetime.now(timezone.utc).isoformat(),
        **event,
    }
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def phase_workdir(kind: str, label: str) -> Path | None:
    campaign_dir = PROGRESS.get("campaign_dir")
    if not isinstance(campaign_dir, Path):
        return None
    parent = campaign_dir / kind
    parent.mkdir(parents=True, exist_ok=True)
    stem = re.sub(r"[^A-Za-z0-9_.-]+", "-", label).strip("-") or "phase"
    candidate = parent / stem
    suffix = 1
    while candidate.exists():
        candidate = parent / f"{stem}-attempt-{suffix}"
        suffix += 1
    return candidate


def prior_panel_workdirs(args: argparse.Namespace) -> list[Path]:
    paths = list(getattr(args, "resume_panel_workdir", []) or [])
    campaign_dir = PROGRESS.get("campaign_dir")
    if isinstance(campaign_dir, Path):
        panel_root = campaign_dir / "panels"
        if panel_root.is_dir():
            paths.extend(path for path in panel_root.iterdir() if path.is_dir())
    unique: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        resolved = path.expanduser().resolve(strict=False)
        if resolved not in seen:
            unique.append(resolved)
            seen.add(resolved)
    return unique


def terminate_phase_process(proc: subprocess.Popen) -> None:
    if proc.poll() is not None:
        return
    try:
        os.killpg(proc.pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    try:
        proc.wait(timeout=10)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        proc.wait()


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
    proc = subprocess.Popen(
        command,
        cwd=REPO_ROOT,
        env=child_env,
        pass_fds=pass_fds,
        start_new_session=True,
    )
    artifact_workdir = child_env.get("AUDIT_BATCH_WORKDIR")
    if "--workdir" in command:
        index = command.index("--workdir")
        if index + 1 < len(command):
            artifact_workdir = command[index + 1]
    append_campaign_event(
        {
            "event": "phase_start",
            "label": label,
            "pid": proc.pid,
            "command": command,
            "artifact_workdir": artifact_workdir,
        }
    )
    timeout = PROGRESS.get("phase_timeout_sec")
    deadline = (
        time.monotonic() + timeout
        if isinstance(timeout, int) and timeout > 0
        else None
    )
    timed_out = False
    try:
        while proc.poll() is None:
            if _STOP_REQUESTED.wait(1):
                terminate_phase_process(proc)
                break
            if deadline is not None and time.monotonic() >= deadline:
                timed_out = True
                emit(f"TIMEOUT {label}: exceeded {timeout}s; terminating phase")
                terminate_phase_process(proc)
                break
    except BaseException:
        terminate_phase_process(proc)
        raise
    returncode = 124 if timed_out else (proc.returncode if proc.returncode is not None else 130)
    if label.startswith("panel-"):
        state = "complete" if returncode == 0 else f"failed_exit_{returncode}"
        PROGRESS["panel_state"] = f"{state}:{label}"
    if label.startswith("forensic-canary-"):
        state = "complete" if returncode == 0 else f"failed_exit_{returncode}"
        PROGRESS["canary_state"] = f"{state}:{label}"
    if returncode != 0:
        PROGRESS["failures"].append(f"{label}:exit={returncode}")
    head = git_head()
    append_campaign_event(
        {
            "event": "phase_end",
            "label": label,
            "pid": proc.pid,
            "exit": returncode,
            "head": head,
            "timed_out": timed_out,
        }
    )
    emit(f"END {label}: exit={returncode} head={head}")
    return returncode


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


def panel_command(
    args: argparse.Namespace,
    *,
    workdir: Path | None = None,
    resume_workdirs: list[Path] | None = None,
) -> list[str]:
    command = [
        sys.executable,
        str(PANEL),
        "--max-workers",
        str(args.max_workers),
        "--stall-minutes",
        str(args.stall_minutes),
        "--seat-timeout-sec",
        str(args.codex_timeout_sec),
        "--runner-timeout-sec",
        str(args.runner_timeout_sec),
        "--push-retries",
        str(args.push_retries),
    ]
    if workdir is not None:
        command.extend(["--workdir", str(workdir)])
    for resume_workdir in resume_workdirs or []:
        command.extend(["--resume-workdir", str(resume_workdir)])
    if args.dry_run:
        command.append("--dry-run")
    return command


def batch_command(lane: str, args: argparse.Namespace) -> list[str]:
    command = [
        sys.executable,
        str(BATCH),
        "--lane",
        lane,
        "--max-workers",
        str(args.max_workers),
        "--rounds",
        str(args.batch_rounds),
        "--stall-minutes",
        str(args.stall_minutes),
        "--seat-timeout-sec",
        str(args.codex_timeout_sec),
        "--runner-timeout-sec",
        str(args.runner_timeout_sec),
        "--push-retries",
        str(args.push_retries),
    ]
    quarantine_file = getattr(args, "campaign_quarantine_file", None)
    if quarantine_file is not None:
        command.extend(["--campaign-quarantine-file", str(quarantine_file)])
    if getattr(args, "dispatch_science_fixes", False):
        command.append("--dispatch-science-fixes")
    if args.dry_run:
        command.append("--dry-run")
    return command


def run_panel(args: argparse.Namespace, label: str) -> int:
    workdir = phase_workdir("panels", label)
    return run_command(
        label,
        panel_command(
            args,
            workdir=workdir,
            resume_workdirs=prior_panel_workdirs(args),
        ),
    )


def drain_lane(lane: str, args: argparse.Namespace) -> tuple[int, bool]:
    """Drain one lane, paneling after every batch before deciding to stop."""
    made_progress = False
    for cycle in itertools.count(1):
        if args.max_lane_cycles and cycle > args.max_lane_cycles:
            emit(f"STOP lane cycle safety bound reached: lane={lane}")
            return 4, made_progress
        before = git_head()
        batch_workdir = phase_workdir("batches", f"batch-{lane}-cycle-{cycle}")
        batch_env = dict(os.environ)
        if batch_workdir is not None:
            batch_env["AUDIT_BATCH_WORKDIR"] = str(batch_workdir)
        batch_rc = run_command(
            f"batch-{lane}-cycle-{cycle}",
            batch_command(lane, args),
            env=batch_env,
        )
        # This is intentionally unconditional, including after a hard batch
        # result: another row in the same batch may already have recorded a
        # panel-eligible disagreement. Preserve the hard result only after the
        # judicial sweep has consumed every resumable handoff.
        panel_rc = run_panel(args, f"panel-after-{lane}-cycle-{cycle}")
        if panel_rc != 0:
            return panel_rc, made_progress
        if batch_rc != 0:
            return batch_rc, made_progress
        after = git_head()
        if after == before:
            return 0, made_progress
        made_progress = True
        if args.dry_run:
            return 0, made_progress


def first_ready_forensic_claim() -> str | None:
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
            if isinstance(claim_id, str) and claim_id:
                return claim_id
    return None


def run_forensic_canary(args: argparse.Namespace) -> int:
    claim_id = first_ready_forensic_claim()
    if not claim_id:
        emit("no ready forensic-tier row available for the forensic canary")
        return 0
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
        "2",
    ]
    if args.dry_run:
        command.append("--dry-run")
    env = dict(os.environ)
    env["AUDIT_FORENSIC_MODE"] = "1"
    return run_command(f"forensic-canary-{claim_id}", command, env=env)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Panel-aware end-to-end audit backlog drainer"
    )
    parser.add_argument("--lane", action="append", help="limit to a configured lane")
    parser.add_argument(
        "--max-workers",
        type=int,
        default=4,
        help=(
            "campaign-wide concurrent Codex seat ceiling; panels run five "
            "judges in bounded waves when the ceiling is below five"
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
    parser.add_argument("--phase-timeout-sec", type=int, default=21600)
    parser.add_argument("--push-retries", type=int, default=3)
    parser.add_argument(
        "--campaign-workdir",
        type=Path,
        default=None,
        help="preserve campaign-scoped quarantine/report artifacts in this directory",
    )
    parser.add_argument(
        "--resume-panel-workdir",
        type=Path,
        action="append",
        default=[],
        help=(
            "prior judicial workdir containing a preserved majority judgment; "
            "the panel revalidates it before replay"
        ),
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
        args.phase_timeout_sec,
        args.push_retries,
    )
    if any(value < 1 for value in positive):
        raise SystemExit("worker, round, timeout, and retry values must be positive")
    if args.max_passes < 0 or args.max_lane_cycles < 0:
        raise SystemExit("pass and cycle safety bounds must be non-negative")
    campaign_dir = args.campaign_workdir or Path(
        tempfile.mkdtemp(prefix="audit_loop_campaign_")
    )
    campaign_dir.mkdir(parents=True, exist_ok=True)
    args.campaign_quarantine_file = campaign_dir / "campaign-row-exclusions.jsonl"
    PROGRESS["quarantine_file"] = args.campaign_quarantine_file
    PROGRESS["campaign_dir"] = campaign_dir
    PROGRESS["phase_timeout_sec"] = args.phase_timeout_sec
    emit(f"campaign artifacts: {campaign_dir}")
    append_campaign_event(
        {
            "event": "campaign_start",
            "head": git_head(),
            "max_workers": args.max_workers,
            "seat_timeout_sec": args.codex_timeout_sec,
            "phase_timeout_sec": args.phase_timeout_sec,
        }
    )
    try:
        validate_requested_lanes(args.lane)
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
    _STOP_HEARTBEAT.clear()
    _STOP_REQUESTED.clear()
    previous_signal_handlers: dict[int, object] = {}

    def request_stop(_signum, _frame) -> None:
        _STOP_REQUESTED.set()

    for signum in (signal.SIGTERM, signal.SIGHUP):
        previous_signal_handlers[signum] = signal.getsignal(signum)
        signal.signal(signum, request_stop)
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
            after = git_head()
            emit(f"development pass {pass_number}: before={before} after={after}")
            if after == before:
                emit("development fixed point reached: full pass landed nothing new")
                if schema_quarantine_count():
                    emit(
                        "fixed point excludes campaign-scoped schema-invalid "
                        f"quarantines: {args.campaign_quarantine_file}"
                    )
                if blocked_row_reentry_count():
                    emit(
                        "fixed point excludes post-verdict rows that immediately "
                        "re-entered dep-ready selection; all other eligible rows "
                        f"were drained: {args.campaign_quarantine_file}"
                    )
                break

        if not args.skip_forensic_canary:
            return run_forensic_canary(args)
        return 0
    finally:
        _STOP_HEARTBEAT.set()
        final_summary = summary_line(final=True)
        emit(final_summary)
        append_campaign_event(
            {
                "event": "campaign_end",
                "head": git_head(),
                "summary": final_summary,
                "stop_requested": _STOP_REQUESTED.is_set(),
            }
        )
        for signum, handler in previous_signal_handlers.items():
            signal.signal(signum, handler)
        _STOP_REQUESTED.clear()
        if _DRAIN_LOCK_HANDLE is not None:
            _DRAIN_LOCK_HANDLE.close()
            _DRAIN_LOCK_HANDLE = None


if __name__ == "__main__":
    raise SystemExit(main())
