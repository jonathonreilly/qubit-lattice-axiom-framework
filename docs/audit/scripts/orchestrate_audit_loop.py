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
import threading
import time
from datetime import datetime, timezone
from pathlib import Path


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
}
_STOP_HEARTBEAT = threading.Event()


def emit(message: str) -> None:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{now}] {message}", flush=True)


def heartbeat() -> None:
    while not _STOP_HEARTBEAT.wait(15 * 60):
        elapsed = int(time.monotonic() - PROGRESS["started"])
        emit(
            "== audit-loop summary "
            f"elapsed={elapsed // 3600}h{(elapsed % 3600) // 60:02d}m "
            f"phase={PROGRESS['phase']} pass={PROGRESS['pass']} "
            f"lane={PROGRESS['lane'] or '-'}"
        )


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
    emit(f"START {label}: {' '.join(command)}")
    proc = subprocess.run(command, cwd=REPO_ROOT, env=env)
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


def blocking_lanes(requested: list[str] | None = None) -> list[tuple[str, int]]:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    certification = json.loads(CERTIFICATION.read_text(encoding="utf-8"))
    names = _lane_names(config)
    if requested:
        unknown = [name for name in requested if name not in names]
        if unknown:
            raise ValueError(f"unknown lane(s): {', '.join(unknown)}")
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
        rc = run_command(
            f"batch-{lane}-cycle-{cycle}",
            batch_command(lane, args),
        )
        if rc != 0:
            return rc, made_progress
        # This is intentionally unconditional: a no-target panel is cheap,
        # while missing a newly recorded disagreement stops the whole lane.
        rc = run_panel(args, f"panel-after-{lane}-cycle-{cycle}")
        if rc != 0:
            return rc, made_progress
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
            and row.get("claim_type") == "no_go"
        ):
            claim_id = row.get("claim_id")
            if isinstance(claim_id, str) and claim_id:
                return claim_id
    return None


def run_forensic_canary(args: argparse.Namespace) -> int:
    claim_id = first_ready_forensic_claim()
    if not claim_id:
        emit("no ready no_go row available for the forensic canary")
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
    parser.add_argument("--skip-forensic-canary", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
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
    if not args.dry_run:
        error = batch.clean_main_error()
        if error:
            emit(f"refusing to run: {error}. Use a dedicated clean main checkout.")
            return 2
        ok, detail = batch.sync_origin_main()
        if not ok:
            emit(f"refusing to run: {detail}")
            return 2

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
                break

        if not args.skip_forensic_canary:
            return run_forensic_canary(args)
        return 0
    finally:
        _STOP_HEARTBEAT.set()
        elapsed = int(time.monotonic() - PROGRESS["started"])
        emit(
            "== audit-loop final summary "
            f"elapsed={elapsed // 3600}h{(elapsed % 3600) // 60:02d}m"
        )


if __name__ == "__main__":
    raise SystemExit(main())
