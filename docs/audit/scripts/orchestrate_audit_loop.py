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
        "--runner-timeout-sec",
        str(args.runner_timeout_sec),
        "--push-retries",
        str(args.push_retries),
    ]
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


def drain_lane(lane: str, args: argparse.Namespace) -> tuple[int, bool]:
    """Drain one lane, paneling after every batch before deciding to stop."""
    made_progress = False
    for cycle in itertools.count(1):
        if args.max_lane_cycles and cycle > args.max_lane_cycles:
            emit(f"STOP lane cycle safety bound reached: lane={lane}")
            return 4, made_progress
        before = git_head()
        batch_rc = run_command(
            f"batch-{lane}-cycle-{cycle}",
            batch_command(lane, args),
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
    parser.add_argument("--max-workers", type=int, default=4)
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
    campaign_dir = args.campaign_workdir or Path(
        tempfile.mkdtemp(prefix="audit_loop_campaign_")
    )
    campaign_dir.mkdir(parents=True, exist_ok=True)
    args.campaign_quarantine_file = campaign_dir / "campaign-row-exclusions.jsonl"
    args.campaign_selection_skip_file = (
        campaign_dir / "campaign-selector-skips.jsonl"
    )
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
                try:
                    exclusions = campaign_exclusion_counts()
                except (OSError, ValueError) as exc:
                    emit(f"invalid campaign state; refusing fixed point: {exc}")
                    return 2
                emit("development fixed point reached: full pass landed nothing new")
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
                break

        if not args.skip_forensic_canary:
            return run_forensic_canary(args)
        return 0
    finally:
        _STOP_HEARTBEAT.set()
        emit(summary_line(final=True))
        if _DRAIN_LOCK_HANDLE is not None:
            _DRAIN_LOCK_HANDLE.close()
            _DRAIN_LOCK_HANDLE = None


if __name__ == "__main__":
    raise SystemExit(main())
