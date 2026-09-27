#!/usr/bin/env python3
"""Run a Karpathy-style Codex autoresearch loop for the atomic lane."""

from __future__ import annotations

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import re


RESULTS_HEADER = (
    "loop\ttimestamp\tstatus\tfull_rms\tone_body_rms\tmax_relative_error\tsource_json\tcommit\n"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
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
    parser.add_argument("--iterations", type=int, default=200)
    parser.add_argument("--start-loop", type=int, default=1)
    parser.add_argument("--per-loop-timeout-minutes", type=int, default=45)
    parser.add_argument(
        "--branch",
        default="autoresearch/atomic-2026-04-19-200",
    )
    parser.add_argument(
        "--codex-bin",
        type=Path,
        default=Path("/Applications/Codex.app/Contents/Resources/codex"),
    )
    parser.add_argument(
        "--model",
        default="gpt-5.4",
    )
    parser.add_argument(
        "--setup-only",
        action="store_true",
    )
    return parser.parse_args()


def run(
    cmd: list[str],
    *,
    cwd: Path,
    stdout=None,
    stderr=None,
    timeout: int | None = None,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd),
        stdout=stdout,
        stderr=stderr,
        text=True,
        timeout=timeout,
        env=env,
        check=False,
        start_new_session=True,
    )


def ensure_run_repo(source_repo: Path, run_repo: Path) -> None:
    if run_repo.exists():
        return
    run_repo.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        source_repo,
        run_repo,
        symlinks=True,
        dirs_exist_ok=False,
        ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"),
    )


def git(
    args: argparse.Namespace,
    *git_args: str,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    result = run(
        ["git", *git_args],
        cwd=args.run_repo,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if check and result.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(git_args)} failed with code {result.returncode}:\n{result.stdout}"
        )
    return result


def ensure_branch_and_identity(args: argparse.Namespace) -> None:
    git(args, "config", "user.name", "Codex Autoresearch")
    git(args, "config", "user.email", "codex-autoresearch@local")
    git(args, "checkout", "-B", args.branch)


def copy_alias_files(args: argparse.Namespace) -> None:
    outputs = args.run_repo / "outputs" / "atomic_lane"
    outputs.mkdir(parents=True, exist_ok=True)
    autoresearch_dir = outputs / "autoresearch"
    autoresearch_dir.mkdir(parents=True, exist_ok=True)
    results = autoresearch_dir / "results.tsv"
    if not results.exists():
        results.write_text(RESULTS_HEADER)
    leader_readout = outputs / "atomic_correlated_readout_shell_radial_local.json"
    leader_candidate = outputs / "atomic_shell_radial_local_selected.json"
    current_readout = outputs / "autoresearch_current_readout.json"
    current_candidate = outputs / "autoresearch_current_candidate.json"
    if not current_readout.exists():
        shutil.copy2(leader_readout, current_readout)
    if not current_candidate.exists():
        shutil.copy2(leader_candidate, current_candidate)


def seed_baseline_commit(args: argparse.Namespace) -> None:
    if not git(args, "status", "--porcelain").stdout.strip():
        return
    git(args, "add", "-A", "--", "ATOMIC_AUTORESEARCH_PROGRAM.md", "outputs/atomic_lane")
    git(args, "reset", "HEAD", "--", "outputs/atomic_lane/autoresearch", check=False)
    if not git(args, "diff", "--cached", "--name-only").stdout.strip():
        return
    git(args, "commit", "-m", "Seed atomic autoresearch baseline")


def current_scores(run_repo: Path) -> tuple[float | None, float | None, float | None, str | None]:
    readout = run_repo / "outputs" / "atomic_lane" / "autoresearch_current_readout.json"
    if not readout.exists():
        return None, None, None, None
    payload = json.loads(readout.read_text())
    scores = payload["accuracy_metrics"]["scores"]
    return (
        float(scores["full_rms_relative_error"]),
        float(scores["one_body_rms_relative_error"]),
        float(scores["max_relative_error"]),
        str(readout),
    )


def append_result(
    run_repo: Path,
    *,
    loop_index: int,
    status: str,
    full_rms: float | None,
    one_body_rms: float | None,
    max_relative_error: float | None,
    source_json: str | None,
    commit: str,
) -> None:
    results = run_repo / "outputs" / "atomic_lane" / "autoresearch" / "results.tsv"
    ts = datetime.now().isoformat(timespec="seconds")
    row = "\t".join(
        [
            str(loop_index),
            ts,
            status,
            "" if full_rms is None else f"{full_rms:.12f}",
            "" if one_body_rms is None else f"{one_body_rms:.12f}",
            "" if max_relative_error is None else f"{max_relative_error:.12f}",
            "" if source_json is None else source_json,
            commit,
        ]
    )
    with results.open("a", encoding="utf-8") as handle:
        handle.write(row + "\n")


def logged_loop_indices(run_repo: Path) -> set[int]:
    results = run_repo / "outputs" / "atomic_lane" / "autoresearch" / "results.tsv"
    if not results.exists():
        return set()
    indices: set[int] = set()
    for line in results.read_text().splitlines()[1:]:
        if not line.strip():
            continue
        first_field = line.split("\t", 1)[0]
        try:
            indices.add(int(first_field))
        except ValueError:
            continue
    return indices


def commit_loop_entries(args: argparse.Namespace) -> list[tuple[int, str, str]]:
    result = git(
        args,
        "log",
        "--format=%H%x09%s",
        "--grep=loop [0-9]",
        check=True,
    )
    entries: list[tuple[int, str, str]] = []
    pattern = re.compile(
        r"^(?:atomic autoresearch\s+)?loop\s+0*(\d+)(?::\s+keep\b|:\s+full RMS\b)"
    )
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        commit_hash, subject = line.split("\t", 1)
        match = pattern.match(subject)
        if match:
            entries.append((int(match.group(1)), commit_hash, subject))
    return sorted(entries)


def reconcile_committed_results(args: argparse.Namespace) -> None:
    logged = logged_loop_indices(args.run_repo)
    current_full, current_one_body, current_max, current_source = current_scores(args.run_repo)
    for loop_index, commit_hash, _subject in commit_loop_entries(args):
        if loop_index in logged:
            continue
        append_result(
            args.run_repo,
            loop_index=loop_index,
            status="kept",
            full_rms=current_full,
            one_body_rms=current_one_body,
            max_relative_error=current_max,
            source_json=current_source,
            commit=commit_hash,
        )
        logged.add(loop_index)


def write_status(run_repo: Path, payload: dict) -> None:
    status_path = run_repo / "outputs" / "atomic_lane" / "autoresearch" / "status.json"
    status_path.write_text(json.dumps(payload, indent=2) + "\n")


def clean_to_head(args: argparse.Namespace) -> None:
    git(args, "reset", "--hard", "HEAD")
    git(
        args,
        "clean",
        "-fd",
        "-e",
        "outputs/atomic_lane/autoresearch",
        "-e",
        "outputs/atomic_lane/autoresearch_current_readout.json",
        "-e",
        "outputs/atomic_lane/autoresearch_current_candidate.json",
    )


def launch_loop(args: argparse.Namespace, loop_index: int) -> tuple[str, str]:
    log_dir = args.run_repo / "outputs" / "atomic_lane" / "autoresearch" / "logs"
    msg_dir = args.run_repo / "outputs" / "atomic_lane" / "autoresearch" / "messages"
    log_dir.mkdir(parents=True, exist_ok=True)
    msg_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"loop_{loop_index:04d}.log"
    msg_path = msg_dir / f"loop_{loop_index:04d}.txt"
    prompt = (
        f"Read `ATOMIC_AUTORESEARCH_PROGRAM.md` and execute exactly one atomic autoresearch loop. "
        f"This is loop {loop_index} of {args.iterations}. "
        f"Operate only inside the current run repo at `{args.run_repo}`. "
        f"Do not inspect or modify the source repo at `{args.source_repo}`. "
        "Ignore any absolute paths that point back to the source repo and stay on relative paths under the run repo. "
        "Do not inspect AUTOPILOT files, broad docs, broad scripts, old non-atomic lanes, or repo-wide file lists. "
        "Read only `ATOMIC_AUTORESEARCH_PROGRAM.md`, the atomic alias JSON files, and the specific atomic scripts needed for this one loop. "
        "Do not edit `outputs/atomic_lane/autoresearch/results.tsv`; the Python driver logs loop outcomes. "
        "Stop after one loop."
    )
    env = dict(os.environ)
    env["ATOMIC_AUTORESEARCH_LOOP_INDEX"] = str(loop_index)
    env["ATOMIC_AUTORESEARCH_TOTAL_LOOPS"] = str(args.iterations)
    env["CODEX_UNIFIED_MODE"] = "1"
    timeout_seconds = int(args.per_loop_timeout_minutes) * 60
    with log_path.open("w", encoding="utf-8") as log_handle:
        proc = subprocess.Popen(
            [
                str(args.codex_bin),
                "exec",
                "--dangerously-bypass-approvals-and-sandbox",
                "--color",
                "never",
                "--model",
                args.model,
                "--cd",
                str(args.run_repo),
                "--output-last-message",
                str(msg_path),
                prompt,
            ],
            cwd=str(args.run_repo),
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            text=True,
            env=env,
            start_new_session=True,
        )
        try:
            returncode = proc.wait(timeout=timeout_seconds)
            return ("ok" if returncode == 0 else "error", str(log_path))
        except subprocess.TimeoutExpired:
            try:
                os.killpg(proc.pid, signal.SIGTERM)
                proc.wait(timeout=15)
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(proc.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                proc.wait(timeout=5)
            except ProcessLookupError:
                pass
            return ("timeout", str(log_path))


def main() -> None:
    args = parse_args()
    if not args.source_repo.exists():
        raise FileNotFoundError(f"source repo not found: {args.source_repo}")
    if not args.codex_bin.exists():
        raise FileNotFoundError(f"codex binary not found: {args.codex_bin}")
    ensure_run_repo(args.source_repo, args.run_repo)
    ensure_branch_and_identity(args)
    copy_alias_files(args)
    seed_baseline_commit(args)
    reconcile_committed_results(args)

    status_payload = {
        "started_at": datetime.now().isoformat(timespec="seconds"),
        "source_repo": str(args.source_repo),
        "run_repo": str(args.run_repo),
        "branch": args.branch,
        "iterations": int(args.iterations),
        "start_loop": int(args.start_loop),
        "model": args.model,
        "state": "setup_complete" if args.setup_only else "running",
    }
    write_status(args.run_repo, status_payload)
    if args.setup_only:
        print(json.dumps(status_payload, indent=2))
        return

    for loop_index in range(int(args.start_loop), int(args.iterations) + 1):
        clean_to_head(args)
        before_commit = git(args, "rev-parse", "HEAD").stdout.strip()
        loop_state, log_path = launch_loop(args, loop_index)
        after_commit = git(args, "rev-parse", "HEAD").stdout.strip()
        if after_commit == before_commit:
            clean_to_head(args)
        full_rms, one_body_rms, max_relative_error, source_json = current_scores(args.run_repo)
        if loop_state == "timeout":
            append_result(
                args.run_repo,
                loop_index=loop_index,
                status="error",
                full_rms=full_rms,
                one_body_rms=one_body_rms,
                max_relative_error=max_relative_error,
                source_json=source_json,
                commit=after_commit,
            )
        else:
            status = "kept" if after_commit != before_commit else ("error" if loop_state == "error" else "rejected")
            append_result(
                args.run_repo,
                loop_index=loop_index,
                status=status,
                full_rms=full_rms,
                one_body_rms=one_body_rms,
                max_relative_error=max_relative_error,
                source_json=source_json,
                commit=after_commit,
            )
        status_payload = {
            "updated_at": datetime.now().isoformat(timespec="seconds"),
            "source_repo": str(args.source_repo),
            "run_repo": str(args.run_repo),
            "branch": args.branch,
            "iterations": int(args.iterations),
            "last_completed_loop": loop_index,
            "last_loop_state": loop_state,
            "last_loop_log": log_path,
            "current_head": after_commit,
            "current_scores": {
                "full_rms_relative_error": full_rms,
                "one_body_rms_relative_error": one_body_rms,
                "max_relative_error": max_relative_error,
                "source_json": source_json,
            },
            "state": "running" if loop_index < int(args.iterations) else "completed",
        }
        write_status(args.run_repo, status_payload)
        print(json.dumps(status_payload), flush=True)


if __name__ == "__main__":
    main()
