#!/usr/bin/env python3
"""Supervise atomic autoresearch by running one driver loop at a time."""

from __future__ import annotations

import argparse
from datetime import datetime
import fcntl
import json
import os
from pathlib import Path
import signal
import subprocess
import time


RESULTS_HEADER = (
    "loop\ttimestamp\tstatus\tfull_rms\tone_body_rms\tmax_relative_error\tsource_json\tcommit\n"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--driver",
        type=Path,
        default=Path("/Users/jonBridger/CI3Z2 Main-atomic-lane/scripts/atomic_autoresearch_driver.py"),
    )
    parser.add_argument(
        "--source-repo",
        type=Path,
        default=Path("/Users/jonBridger/CI3Z2 Main-atomic-lane"),
    )
    parser.add_argument(
        "--run-repo",
        type=Path,
        default=Path("/Users/jonBridger/CI3Z2 Main-atomic-autoresearch-2026-04-19"),
    )
    parser.add_argument("--branch", default="autoresearch/atomic-2026-04-19-200")
    parser.add_argument("--iterations", type=int, default=200)
    parser.add_argument("--start-loop", type=int, default=1)
    parser.add_argument("--per-loop-timeout-minutes", type=int, default=30)
    parser.add_argument("--orphan-grace-minutes", type=int, default=5)
    parser.add_argument("--idle-sleep-seconds", type=float, default=5.0)
    parser.add_argument(
        "--supervisor-log",
        type=Path,
        default=Path(
            "/Users/jonBridger/CI3Z2 Main-atomic-autoresearch-2026-04-19/"
            "outputs/atomic_lane/autoresearch/supervisor.log"
        ),
    )
    return parser.parse_args()


def run(
    cmd: list[str],
    *,
    cwd: Path,
    log_path: Path | None = None,
    start_new_session: bool = False,
) -> int:
    if log_path is None:
        result = subprocess.run(
            cmd,
            cwd=str(cwd),
            check=False,
            start_new_session=start_new_session,
        )
        return int(result.returncode)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"\n[{datetime.now().isoformat(timespec='seconds')}] $ {' '.join(cmd)}\n")
        log.flush()
        result = subprocess.run(
            cmd,
            cwd=str(cwd),
            stdout=log,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
            start_new_session=start_new_session,
        )
        log.write(f"[exit {result.returncode}]\n")
    return int(result.returncode)


def results_path(run_repo: Path) -> Path:
    return run_repo / "outputs" / "atomic_lane" / "autoresearch" / "results.tsv"


def supervisor_lock_path(run_repo: Path) -> Path:
    return run_repo / "outputs" / "atomic_lane" / "autoresearch" / "supervisor.lock"


def acquire_supervisor_lock(run_repo: Path):
    lock_path = supervisor_lock_path(run_repo)
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = lock_path.open("w", encoding="utf-8")
    try:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        raise RuntimeError(f"another atomic autoresearch supervisor is active: {lock_path}") from exc
    handle.write(f"{os.getpid()}\n")
    handle.flush()
    return handle


def logged_loop_indices(run_repo: Path) -> set[int]:
    path = results_path(run_repo)
    if not path.exists():
        return set()
    indices: set[int] = set()
    for line in path.read_text().splitlines()[1:]:
        if not line.strip():
            continue
        try:
            indices.add(int(line.split("\t", 1)[0]))
        except ValueError:
            continue
    return indices


def write_supervisor_status(args: argparse.Namespace, payload: dict[str, object]) -> None:
    path = args.run_repo / "outputs" / "atomic_lane" / "autoresearch" / "supervisor_status.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n")


def parse_etime_seconds(raw: str) -> int | None:
    parts = raw.strip().split(":")
    try:
        if "-" in parts[0]:
            days_raw, hours_raw = parts[0].split("-", 1)
            if len(parts) != 3:
                return None
            return (
                int(days_raw) * 86400
                + int(hours_raw) * 3600
                + int(parts[1]) * 60
                + int(parts[2])
            )
        if len(parts) == 3:
            return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
        if len(parts) == 2:
            return int(parts[0]) * 60 + int(parts[1])
    except ValueError:
        return None
    return None


def process_rows() -> list[dict[str, object]]:
    result = subprocess.run(
        ["ps", "-axo", "pid=,ppid=,etime=,command="],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        check=False,
    )
    rows: list[dict[str, object]] = []
    for line in result.stdout.splitlines():
        fields = line.strip().split(None, 3)
        if len(fields) < 4:
            continue
        try:
            pid = int(fields[0])
            ppid = int(fields[1])
        except ValueError:
            continue
        rows.append(
            {
                "pid": pid,
                "ppid": ppid,
                "etime": fields[2],
                "elapsed_seconds": parse_etime_seconds(fields[2]),
                "command": fields[3],
            }
        )
    return rows


def active_loop_processes(run_repo: Path, loop_index: int) -> list[dict[str, object]]:
    repo_needle = str(run_repo)
    msg_needle = f"loop_{loop_index:04d}.txt"
    start_needle = f"--start-loop {loop_index}"
    active: list[dict[str, object]] = []
    for row in process_rows():
        command = str(row["command"])
        if int(row["pid"]) == os.getpid() or repo_needle not in command:
            continue
        if "atomic_autoresearch_supervisor.py" in command:
            continue
        if "codex exec" in command and msg_needle in command:
            active.append(row)
        elif "atomic_autoresearch_driver.py" in command and start_needle in command:
            active.append(row)
    return active


def terminate_process_group(pid: int) -> None:
    try:
        pgid = os.getpgid(pid)
    except ProcessLookupError:
        return
    try:
        os.killpg(pgid, signal.SIGTERM)
    except ProcessLookupError:
        return
    time.sleep(5)
    try:
        os.killpg(pgid, signal.SIGKILL)
    except ProcessLookupError:
        return


def wait_for_active_loop(args: argparse.Namespace, loop_index: int) -> bool:
    max_elapsed = (int(args.per_loop_timeout_minutes) + int(args.orphan_grace_minutes)) * 60
    adopted = False
    while True:
        active = active_loop_processes(args.run_repo, loop_index)
        if not active:
            return adopted
        adopted = True
        stale = [
            row
            for row in active
            if row.get("elapsed_seconds") is not None and int(row["elapsed_seconds"]) > max_elapsed
        ]
        if stale:
            for row in stale:
                terminate_process_group(int(row["pid"]))
            write_supervisor_status(
                args,
                {
                    "updated_at": datetime.now().isoformat(timespec="seconds"),
                    "state": "terminated_stale_active_loop",
                    "loop": loop_index,
                    "terminated_pids": [int(row["pid"]) for row in stale],
                    "max_elapsed_seconds": max_elapsed,
                },
            )
            return adopted
        write_supervisor_status(
            args,
            {
                "updated_at": datetime.now().isoformat(timespec="seconds"),
                "state": "waiting_for_active_loop",
                "loop": loop_index,
                "active_processes": active,
                "max_elapsed_seconds": max_elapsed,
                "run_repo": str(args.run_repo),
                "results_tsv": str(results_path(args.run_repo)),
            },
        )
        time.sleep(float(args.idle_sleep_seconds))


def setup_only(args: argparse.Namespace, next_loop: int) -> int:
    return run(
        [
            "python3",
            str(args.driver),
            "--source-repo",
            str(args.source_repo),
            "--run-repo",
            str(args.run_repo),
            "--branch",
            args.branch,
            "--iterations",
            str(args.iterations),
            "--start-loop",
            str(next_loop),
            "--setup-only",
        ],
        cwd=args.source_repo,
        log_path=args.supervisor_log,
    )


def run_one_loop(args: argparse.Namespace, loop_index: int) -> int:
    return run(
        [
            "python3",
            "-u",
            str(args.driver),
            "--source-repo",
            str(args.source_repo),
            "--run-repo",
            str(args.run_repo),
            "--branch",
            args.branch,
            "--iterations",
            str(loop_index),
            "--start-loop",
            str(loop_index),
            "--per-loop-timeout-minutes",
            str(args.per_loop_timeout_minutes),
        ],
        cwd=args.source_repo,
        log_path=args.supervisor_log,
        start_new_session=True,
    )


def main() -> None:
    args = parse_args()
    lock_handle = acquire_supervisor_lock(args.run_repo)
    _ = lock_handle
    args.supervisor_log.parent.mkdir(parents=True, exist_ok=True)
    current_loop = int(args.start_loop)
    while current_loop <= int(args.iterations):
        wait_for_active_loop(args, current_loop)
        setup_only(args, current_loop)
        logged_before = logged_loop_indices(args.run_repo)
        if logged_before:
            current_loop = max(current_loop, max(logged_before) + 1)
        if current_loop > int(args.iterations):
            break
        wait_for_active_loop(args, current_loop)
        write_supervisor_status(
            args,
            {
                "updated_at": datetime.now().isoformat(timespec="seconds"),
                "state": "running",
                "next_loop": current_loop,
                "iterations": int(args.iterations),
                "run_repo": str(args.run_repo),
                "results_tsv": str(results_path(args.run_repo)),
            },
        )
        returncode = run_one_loop(args, current_loop)
        setup_only(args, current_loop + 1)
        logged_after = logged_loop_indices(args.run_repo)
        if logged_after and max(logged_after) >= current_loop:
            current_loop = max(logged_after) + 1
        else:
            current_loop += 1
        write_supervisor_status(
            args,
            {
                "updated_at": datetime.now().isoformat(timespec="seconds"),
                "state": "running",
                "last_driver_returncode": returncode,
                "next_loop": current_loop,
                "iterations": int(args.iterations),
                "run_repo": str(args.run_repo),
                "results_tsv": str(results_path(args.run_repo)),
            },
        )
        time.sleep(float(args.idle_sleep_seconds))
    write_supervisor_status(
        args,
        {
            "updated_at": datetime.now().isoformat(timespec="seconds"),
            "state": "completed",
            "next_loop": current_loop,
            "iterations": int(args.iterations),
            "run_repo": str(args.run_repo),
            "results_tsv": str(results_path(args.run_repo)),
        },
    )


if __name__ == "__main__":
    main()
