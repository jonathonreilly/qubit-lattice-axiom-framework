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
import math
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
DEFAULT_SERVICE_RETRY_INITIAL_SECONDS = 60
DEFAULT_SERVICE_RETRY_MAX_SECONDS = 15 * 60
FORENSIC_MECHANICS_CIRCUIT_THRESHOLD = 3


class RuntimeLimitReached(Exception):
    """Raised only at a safe phase boundary after the requested runtime."""


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


def forensic_schema_failure_signature(detail: str) -> str | None:
    """Normalize known control-plane schema defects without verdict content."""
    if "evidence_locator must contain at least 12 normalized characters" in detail:
        return "EVIDENCE_LOCATOR_MIN_LENGTH"
    if (
        "N7.argument and N7.resolution must each contain at least 80 "
        "normalized characters"
    ) in detail:
        return "N7_MIN_LENGTH"
    if (
        detail.startswith("N1 route ")
        and ".route_class=" in detail
        and "is not supported by its evidenced" in detail
    ):
        return "N1_ROUTE_CLASS_MARKER_MISMATCH"
    if (
        detail.startswith("N5 statement ")
        and "tested resolution is not evidenced at resolution_evidence_path"
        in detail
    ):
        return "N5_TESTED_RESOLUTION_VERBATIM_MISMATCH"
    return None


def forensic_mechanics_circuit(
    records: list[dict],
    threshold: int = FORENSIC_MECHANICS_CIRCUIT_THRESHOLD,
) -> tuple[str, int] | None:
    """Open after one known schema defect hits enough distinct claims."""
    claims_by_signature: dict[str, set[str]] = {}
    for record in records:
        if record.get("reason") != batch.SCHEMA_QUARANTINE_RESULT:
            continue
        claim_id = record.get("claim_id")
        if not isinstance(claim_id, str) or not claim_id:
            continue
        for failure in record.get("failures") or []:
            if not isinstance(failure, dict):
                continue
            signature = forensic_schema_failure_signature(
                str(failure.get("detail") or "")
            )
            if signature is not None:
                claims_by_signature.setdefault(signature, set()).add(claim_id)
    eligible = [
        (signature, len(claim_ids))
        for signature, claim_ids in claims_by_signature.items()
        if len(claim_ids) >= threshold
    ]
    if not eligible:
        return None
    return sorted(eligible, key=lambda item: (-item[1], item[0]))[0]


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


def remaining_runtime_seconds(args: argparse.Namespace) -> float | None:
    hours = float(getattr(args, "max_runtime_hours", 0) or 0)
    started = PROGRESS.get("started")
    if hours <= 0 or not isinstance(started, (int, float)):
        return None
    return (hours * 60 * 60) - (time.monotonic() - started)


def stop_if_runtime_limit_reached(args: argparse.Namespace) -> None:
    remaining = remaining_runtime_seconds(args)
    if remaining is not None and remaining <= 0:
        emit(
            "STOP requested runtime reached at a completed phase boundary: "
            f"max_runtime_hours={args.max_runtime_hours}"
        )
        raise RuntimeLimitReached


def wait_for_service_retry(
    args: argparse.Namespace,
    context: str,
    consecutive_failures: int,
) -> bool:
    """Back off once and report whether the runtime bound was consumed."""
    delay = min(
        args.service_retry_initial_sec
        * (2 ** min(consecutive_failures - 1, 20)),
        args.service_retry_max_sec,
    )
    remaining = remaining_runtime_seconds(args)
    runtime_consumed = remaining is not None and remaining <= delay
    if remaining is not None:
        delay = min(delay, max(0.0, remaining))
    emit(
        "retryable auditor service outage: "
        f"context={context} consecutive={consecutive_failures} "
        f"backoff_seconds={delay:g}"
    )
    if delay > 0:
        time.sleep(delay)
    return runtime_consumed


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
        "--seat-timeout-sec",
        str(args.codex_timeout_sec),
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


def run_panel(
    args: argparse.Namespace,
    label: str,
    *,
    required_after_batch: bool = False,
) -> int:
    transient_failures = 0
    attempts = 0
    while True:
        if attempts or not required_after_batch:
            try:
                stop_if_runtime_limit_reached(args)
            except RuntimeLimitReached:
                if transient_failures:
                    return batch.TRANSIENT_SERVICE_EXIT_CODE
                raise
        attempts += 1
        rc = run_command(label, panel_command(args))
        if rc != batch.TRANSIENT_SERVICE_EXIT_CODE:
            return rc
        transient_failures += 1
        if wait_for_service_retry(args, label, transient_failures):
            return batch.TRANSIENT_SERVICE_EXIT_CODE


def drain_lane(
    lane: str | None,
    args: argparse.Namespace,
    source: str | None = None,
) -> tuple[int, bool]:
    """Drain one scoped phase and panel after every batch."""
    made_progress = False
    transient_failures = 0
    label = f"{source}-source" if source else (lane or "global-development")
    for cycle in itertools.count(1):
        stop_if_runtime_limit_reached(args)
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
        if batch_rc == batch.CLEANUP_INTEGRITY_EXIT_CODE:
            emit(
                "GLOBAL cleanup integrity failure in development batch; "
                "skipping the post-batch panel sweep and stopping the campaign"
            )
            return batch_rc, made_progress
        # This is intentionally unconditional, including after a hard batch
        # result: another row in the same batch may already have recorded a
        # panel-eligible disagreement. Preserve the hard result only after the
        # judicial sweep has consumed every resumable handoff.
        try:
            panel_rc = run_panel(
                args,
                f"panel-after-{label}-cycle-{cycle}",
                required_after_batch=True,
            )
        except RuntimeLimitReached:
            # The required sweep ran at least once. Do not let a bounded stop
            # erase a hard or typed-temporary batch result.
            if batch_rc != 0:
                return batch_rc, made_progress
            raise
        if panel_rc != 0:
            if batch_rc not in {0, batch.TRANSIENT_SERVICE_EXIT_CODE}:
                return batch_rc, made_progress
            return panel_rc, made_progress
        after = git_head()
        after_exclusions = campaign_exclusion_keys(
            getattr(args, "campaign_quarantine_file", None)
        )
        if after != before or after_exclusions != before_exclusions:
            made_progress = True
        if batch_rc not in {0, batch.TRANSIENT_SERVICE_EXIT_CODE}:
            return batch_rc, made_progress
        try:
            stop_if_runtime_limit_reached(args)
        except RuntimeLimitReached:
            if batch_rc == batch.TRANSIENT_SERVICE_EXIT_CODE:
                return batch_rc, made_progress
            raise
        if batch_rc == batch.TRANSIENT_SERVICE_EXIT_CODE:
            transient_failures += 1
            runtime_consumed = wait_for_service_retry(
                args,
                f"batch-{label}-after-panel",
                transient_failures,
            )
            if runtime_consumed:
                return batch_rc, made_progress
            try:
                stop_if_runtime_limit_reached(args)
            except RuntimeLimitReached:
                return batch_rc, made_progress
            continue
        transient_failures = 0
        if after == before and after_exclusions == before_exclusions:
            return 0, made_progress
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


def forensic_canary_transient_diagnostic(terminal: dict | None) -> str:
    """Return only a pre-authority Codex execution diagnostic.

    Apply, propagation, push, extraction, and verdict payload fields are never
    transport evidence. A bounded validation-repair outage is eligible only
    through the runner's exact no-verdict execution-error prefix.
    """
    if not isinstance(terminal, dict):
        return ""
    phase = terminal.get("phase")
    if phase == "codex_failed":
        return str(terminal.get("stderr") or "")
    if phase == "validate_failed":
        error = str(terminal.get("error") or "")
        if error.startswith(
            (
                "fresh schema retry codex exec failed:",
                "validation repair codex exec failed:",
            )
        ):
            return error
    return ""


def run_forensic_canary(
    args: argparse.Namespace,
    extra_excluded: set[str] | None = None,
) -> int:
    PROGRESS["last_canary_claim_id"] = None
    PROGRESS["last_canary_terminal_phase"] = None
    PROGRESS["last_canary_source"] = None
    try:
        exclusion_records = batch.load_campaign_exclusion_records(
            args.campaign_quarantine_file
        )
    except (OSError, ValueError) as exc:
        emit(f"invalid campaign state before forensic canary: {exc}")
        return 2
    circuit = forensic_mechanics_circuit(exclusion_records)
    if circuit is not None:
        signature, count = circuit
        PROGRESS["canary_state"] = (
            f"mechanics_circuit_open:{signature}:{count}"
        )
        emit(
            "forensic mechanics circuit open; refusing to spend another "
            "independent seat on the repeated control-plane defect: "
            f"signature={signature} distinct_claims={count} "
            f"threshold={FORENSIC_MECHANICS_CIRCUIT_THRESHOLD}"
        )
        return 0
    excluded = {
        record["claim_id"]
        for record in exclusion_records
    }
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
            marker = batch.retryable_service_failure_marker(
                forensic_canary_transient_diagnostic(terminal)
            )
            if marker is not None:
                emit(
                    "forensic auditor hit a retryable service outage: "
                    f"claim={claim_id} matched={marker!r}"
                )
                return batch.TRANSIENT_SERVICE_EXIT_CODE
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


def drain_forensic_sequence(
    args: argparse.Namespace,
    forensic_attempted: set[str],
) -> tuple[int, bool]:
    """Drain claim-local forensic outcomes without redundant development scans.

    Returns ``(rc, resume_development)``. A canonical state change or remote
    supersession returns to the full development phases because dependency
    readiness may have changed. A schema/compute quarantine changes only the
    campaign exclusion file, so the next forensic row is selected directly
    while the repository head remains stable.
    """
    service_failures = 0
    while True:
        stop_if_runtime_limit_reached(args)
        forensic_before = git_head()
        rc = run_forensic_canary(args, forensic_attempted)
        if rc == batch.TRANSIENT_SERVICE_EXIT_CODE:
            service_failures += 1
            runtime_consumed = wait_for_service_retry(
                args,
                "forensic-canary",
                service_failures,
            )
            if runtime_consumed:
                return rc, False
            try:
                stop_if_runtime_limit_reached(args)
            except RuntimeLimitReached:
                return rc, False
            continue
        if rc != 0:
            return rc, False
        service_failures = 0
        if args.dry_run:
            return 0, False
        synced, detail = batch.sync_origin_main()
        if not synced:
            emit(f"cannot reconcile forensic result with origin/main: {detail}")
            return 2, False
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
            return 0, True
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
                        return 2, False
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
            return 0, True
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
                "this campaign; advancing directly to the next ready "
                "forensic row"
            )
            continue
        return 0, False


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
            "concurrent primary-seat ceiling for development auditors and "
            "judicial judges; panels run in bounded waves below five"
        ),
    )
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
        "--max-runtime-hours",
        type=float,
        default=0,
        help=(
            "stop successfully at the first completed phase boundary after "
            "this many hours; 0 has no runtime bound"
        ),
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
        "--service-retry-initial-sec",
        type=int,
        default=DEFAULT_SERVICE_RETRY_INITIAL_SECONDS,
        help="initial backoff after a typed transient auditor service outage",
    )
    parser.add_argument(
        "--service-retry-max-sec",
        type=int,
        default=DEFAULT_SERVICE_RETRY_MAX_SECONDS,
        help="maximum backoff between typed transient-service batch retries",
    )
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
        args.service_retry_initial_sec,
        args.service_retry_max_sec,
    )
    if any(value < 1 for value in positive):
        raise SystemExit("worker, round, timeout, and retry values must be positive")
    if args.max_passes < 0 or args.max_lane_cycles < 0:
        raise SystemExit("pass and cycle safety bounds must be non-negative")
    if (
        not math.isfinite(args.max_runtime_hours)
        or args.max_runtime_hours < 0
    ):
        raise SystemExit("runtime bound must be finite and non-negative")
    if args.service_retry_initial_sec > args.service_retry_max_sec:
        raise SystemExit("initial service retry delay cannot exceed its maximum")
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
            stop_if_runtime_limit_reached(args)
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
                rc, resume_development = drain_forensic_sequence(
                    args,
                    forensic_attempted,
                )
                if rc != 0:
                    return rc
                if resume_development:
                    continue
                return 0
    except RuntimeLimitReached:
        return 0
    finally:
        _STOP_HEARTBEAT.set()
        emit(summary_line(final=True))
        if _DRAIN_LOCK_HANDLE is not None:
            _DRAIN_LOCK_HANDLE.close()
            _DRAIN_LOCK_HANDLE = None


if __name__ == "__main__":
    raise SystemExit(main())
