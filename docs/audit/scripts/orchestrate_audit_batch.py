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
import fcntl
import hashlib
import json
import math
import os
import queue
import re
import shutil
import signal
import stat
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from collections import Counter
from collections.abc import Callable
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS.parents[2]
DATA = REPO_ROOT / "docs" / "audit" / "data"
SCIENCE_FIX = REPO_ROOT / "scripts" / "science_fix_loop.py"
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import codex_audit_runner as audit_runner  # noqa: E402
import ledger_io  # noqa: E402
import static_pipeline_checkpoint as static_checkpoint  # noqa: E402

MODEL = "gpt-5.6-sol"
AUDITOR_FAMILY = "codex-gpt-5.6"
REASONING = "xhigh"
RETAINED = {"retained", "retained_bounded", "retained_no_go", "meta"}
AUDITABLE_TYPES = {"positive_theorem", "bounded_theorem", "open_gate"}
SUCCESS_RESULTS = {
    "audited_clean", "audited_renaming", "audited_conditional",
    "audited_decoration", "audited_numerical_match", "audited_failed",
    "compute_required",
}
_COMMAND_CONTEXT = threading.local()


def _command_cancel_event() -> threading.Event | None:
    return getattr(_COMMAND_CONTEXT, "cancel_event", None)


def _command_cancelled() -> bool:
    event = _command_cancel_event()
    return event is not None and event.is_set()
RESUMABLE_HANDOFF_RESULTS = {"judicial_panel_required"}
SCHEMA_INVALID_RESULTS = {"malformed_json", "validation_failed"}
SCHEMA_QUARANTINE_RESULT = "schema_invalid_quarantined"
SCHEMA_DEFERRED_RESULT = "schema_invalid_peer_deferred"
SCHEMA_SUPERSEDED_RESULT = "schema_invalid_attempt_superseded"
BLOCKED_ROW_QUARANTINE_RESULT = "blocked_row_reentry_quarantined"
COMPUTE_QUARANTINE_RESULT = "compute_required_quarantined"
CLAIM_TRANSACTION_QUARANTINE_RESULT = "claim_transaction_quarantined"
SCHEMA_RECOVERY_RESULTS = {
    SCHEMA_QUARANTINE_RESULT,
    SCHEMA_DEFERRED_RESULT,
    SCHEMA_SUPERSEDED_RESULT,
}
CAMPAIGN_EXCLUSION_RESULTS = {
    BLOCKED_ROW_QUARANTINE_RESULT,
    COMPUTE_QUARANTINE_RESULT,
    CLAIM_TRANSACTION_QUARANTINE_RESULT,
}
CAMPAIGN_EXCLUSION_REASONS = {
    SCHEMA_QUARANTINE_RESULT,
    *CAMPAIGN_EXCLUSION_RESULTS,
}
SELECTION_SKIP_REASONS = {
    "missing_ledger_row",
    "audit_status_not_unaudited",
    "forensic_no_go",
    "non_batch_claim_type",
    "forensic_source_shape",
    "dependencies_not_retained",
    "note_hash_drift",
    "awaiting_science_repair",
    "unclassified_selector_skip",
}
SCIENCE_FIX_RESULTS = {"science_fix_dispatched", "science_fix_dispatch_failed"}
MIN_DELIVERY_BYTES = 200
PACKET_COMPLETION_STALL_SECONDS = 20 * 60
PACKET_COMPLETION_POLL_SECONDS = 15
PACKET_COMPLETION_EXIT_GRACE_SECONDS = 10
COMMAND_TERMINATION_GRACE_SECONDS = 5
INHERITED_DRAIN_LOCK_FD_ENV = "AUDIT_DRAIN_LOCK_FD"
LANE_CERTIFICATION_PATH = "docs/audit/data/lane_certification.json"


def _repo_identity() -> str:
    """Canonical identity shared by every git worktree of one clone.

    The lock must not key on the checkout root: two worktrees of the same
    clone would then hold different locks and race pushes anyway. The git
    common directory is shared across a clone's worktrees. Boundary: an
    INDEPENDENT clone of the same remote has its own common dir and its own
    lock — cross-clone coordination stays with the skill's coexistence
    contract, not this lock.
    """
    proc = subprocess.run(
        ["git", "rev-parse", "--git-common-dir"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    common = (proc.stdout or "").strip()
    if proc.returncode != 0 or not common:
        return str(REPO_ROOT.resolve())
    path = Path(common)
    if not path.is_absolute():
        path = REPO_ROOT / path
    return str(path.resolve())


def acquire_exclusive_drain_lock(label: str):
    """One audit-lane orchestrator per clone (all its worktrees) per machine.

    Verdict/reseat commits ship the full regenerated audit-surface set, so
    two concurrent audit-lane orchestrators race every push and each race
    costs a multi-minute pipeline replay. Parallelism belongs in the seats
    INSIDE one orchestrator, never in competing orchestrators. The lock is
    advisory (flock), machine-local, keyed to the repository path, and
    released automatically on process exit. Returns an open handle to keep
    referenced, or None when another orchestrator already holds it.
    """
    inherited_fd = os.environ.get(INHERITED_DRAIN_LOCK_FD_ENV)
    if inherited_fd:
        try:
            fd = int(inherited_fd)
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return os.fdopen(os.dup(fd), "w")
        except (OSError, ValueError):
            print(
                "refusing to run: invalid inherited audit-lane lock fd "
                f"for {label}"
            )
            return None

    key = hashlib.sha256(_repo_identity().encode("utf-8")).hexdigest()[:12]
    lock_path = Path(tempfile.gettempdir()) / f"audit-lane-{key}.lock"
    handle = open(lock_path, "w")
    try:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        handle.close()
        print(
            "refusing to run: another audit-lane orchestrator holds "
            f"{lock_path} for this repository. Join the running drain's "
            "seats (its --max-workers) instead of racing a second "
            f"instance ({label})."
        )
        return None
    handle.write(f"{label} pid={os.getpid()}\n")
    handle.flush()
    return handle


def sh(
    cmd: list[str],
    timeout: int | None = 120,
    *,
    honor_cancel: bool = True,
    text: bool = True,
) -> subprocess.CompletedProcess:
    empty = "" if text else b""
    cancelled_message = (
        "cancelled before launch" if text else b"cancelled before launch"
    )
    cancel_event = _command_cancel_event() if honor_cancel else None
    if cancel_event is not None and cancel_event.is_set():
        return subprocess.CompletedProcess(cmd, 125, empty, cancelled_message)
    proc = subprocess.Popen(
        cmd,
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=text,
        start_new_session=True,
    )
    deadline = time.monotonic() + timeout if timeout is not None else None
    while True:
        remaining = None if deadline is None else max(0.0, deadline - time.monotonic())
        poll_window = 1.0 if remaining is None else min(1.0, remaining)
        try:
            stdout, stderr = proc.communicate(timeout=poll_window)
            if cancel_event is not None and cancel_event.is_set():
                message = (
                    "cancelled during command"
                    if text
                    else b"cancelled during command"
                )
                return subprocess.CompletedProcess(
                    cmd, 125, stdout or empty, stderr or message
                )
            return subprocess.CompletedProcess(cmd, proc.returncode, stdout, stderr)
        except subprocess.TimeoutExpired:
            cancelled = cancel_event is not None and cancel_event.is_set()
            timed_out = deadline is not None and time.monotonic() >= deadline
            if not cancelled and not timed_out:
                continue
        # Give shells a catchable termination first so EXIT traps can remove
        # nonce-bound checkpoint receipts. Escalate only when the whole
        # process group ignores the grace period.
        try:
            os.killpg(proc.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        try:
            stdout, stderr = proc.communicate(
                timeout=COMMAND_TERMINATION_GRACE_SECONDS
            )
        except subprocess.TimeoutExpired:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            stdout, stderr = proc.communicate()
        reason = "cancelled" if cancelled else f"timed out after {timeout}s"
        if not text:
            reason = reason.encode("utf-8")
        return subprocess.CompletedProcess(
            cmd, 125 if cancelled else 124, stdout or empty, stderr or reason
        )


def load_rows() -> dict[str, dict]:
    ledger_io.ensure_cache()
    ledger = json.loads((DATA / "audit_ledger.json").read_text(encoding="utf-8"))
    return ledger.get("rows", {})


def accepted(cid: str) -> bool:
    return audit_runner.premise_nodes.is_accepted_premise_dep(cid)


def dep_ready(row: dict, effective: dict[str, str]) -> bool:
    for dep in row.get("deps") or []:
        if audit_runner.premise_nodes.is_non_evidence_context_dep(dep):
            return False
        if accepted(dep):
            continue
        status = effective.get(dep, "MISSING")
        if status in RETAINED or str(status).startswith("decoration_under_"):
            continue
        return False
    return True


def note_hash_drifted(row: dict) -> bool:
    """Whether the ledger row's note_hash lags the note file on disk.

    A science-fix landing changes the note before seed_audit_ledger.py
    refreshes the row, and apply_audit refuses drifted rows AFTER the seats
    have already run (2026-07-13: two fresh seats audited the
    repaired note and their applies were rejected). Refusing at targeting
    time saves the seats and tells the operator the exact remedy.
    """
    on_disk_path = REPO_ROOT / row.get("note_path", "")
    if not on_disk_path.exists():
        return False
    on_disk = hashlib.sha256(
        on_disk_path.read_text(encoding="utf-8", errors="replace").encode("utf-8")
    ).hexdigest()
    return on_disk != row.get("note_hash")


def source_requires_forensic(row: dict) -> bool:
    note_path = row.get("note_path") or ""
    try:
        note_body = (REPO_ROOT / note_path).read_text(encoding="utf-8") if note_path else ""
    except OSError:
        note_body = ""
    return audit_runner.no_go_discipline_gate.source_requires_no_go_discipline(
        note_path,
        note_body,
        row.get("claim_type") or row.get("claim_type_author_hint"),
    )


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


def last_source_change(row: dict, rows: dict[str, dict] | None = None) -> str:
    """ISO commit time of the newest change to row or dependency sources."""
    source_rows = [row]
    if rows is not None:
        source_rows.extend(
            rows[dep]
            for dep in row.get("deps") or []
            if dep in rows
        )
    paths = sorted({
        path
        for source_row in source_rows
        for path in (
            source_row.get("note_path"),
            source_row.get("runner_path"),
            *(source_row.get("helper_runner_paths") or []),
        )
        if path
    })
    if not paths:
        return ""
    result = sh(["git", "log", "-1", "--format=%cI", "--", *paths])
    return (result.stdout or "").strip()


def awaiting_repair_since_conditional(
    row: dict,
    effective: dict[str, str],
    rows: dict[str, dict] | None = None,
) -> bool:
    """A re-queued conditional row is re-audited only after something moved.

    A non-terminal audited_conditional archives and re-queues the row as
    unaudited immediately, so without this check every orchestrator RUN
    re-audits the unchanged claim toward the same conditional verdict
    (observed: cl3_pauli burned two fresh seats one run after its agreed
    conditional). Movement means either the note/runner sources changed
    after the archived verdict, or a recorded dependency's effective status
    changed since the archived snapshot (e.g. a demanded authority went
    retained-grade).
    """
    archives = row.get("previous_audits") or []
    if not archives or not isinstance(archives[-1], dict):
        return False
    last = archives[-1]
    if last.get("audit_status") != "audited_conditional":
        return False
    archived_note_hash = last.get("archived_for_note_hash")
    if archived_note_hash and archived_note_hash != row.get("note_hash"):
        # Seeder archival records the exact pre-repair note hash.  Prefer this
        # content signal over commit time so an old-dated commit merged after
        # the audit cannot be mistaken for unchanged source.
        return False
    snapshot = last.get("audit_state_snapshot") or {}
    snapshot_deps = snapshot.get("dep_effective_status") or {}
    for dep, then_status in snapshot_deps.items():
        if effective.get(dep, "MISSING") != then_status:
            return False

    repair_reason = str(last.get("invalidation_reason") or "")
    if repair_reason:
        # The invalidation pipeline already decided that this archived audit
        # is stale and deliberately re-queued it.  This repetition guard must
        # not veto that stronger, explicit re-audit signal.
        return False

    # Audit-side dependency repairs can change scope/type without changing the
    # final effective-status string.  Those are movement too.
    if rows is not None:
        for field, snapshot_field in (
            ("claim_type", "dep_claim_type"),
            ("claim_scope", "dep_claim_scope"),
            ("note_hash", "dep_axiom_premise_note_hash"),
        ):
            then_values = snapshot.get(snapshot_field) or {}
            for dep, then_value in then_values.items():
                if dep in rows and rows[dep].get(field) != then_value:
                    return False

    # archived_at distinguishes modern archives, while audit_date is the
    # verdict-time baseline.  A repair can be committed before the pipeline
    # notices it and writes archived_at, so comparing source time to
    # archived_at would hide exactly the repair that caused archival.  Legacy
    # archives without archived_at still use their dependency snapshot, but
    # an empty legacy snapshot must remain targetable rather than stranded.
    source_unchanged = False
    archived_at = str(last.get("archived_at") or "")
    audited_at = str(last.get("audit_date") or "")
    if archived_at and audited_at:
        changed_at = last_source_change(row, rows)
        changed_dt = _iso(changed_at)
        audited_dt = _iso(audited_at)
        if changed_dt is not None and audited_dt is not None:
            # git %cI is second-granularity while audit_date can carry
            # microseconds.  Treat the same second as movement so a repair
            # committed just after the audit cannot be hidden by truncation.
            if changed_dt >= audited_dt.replace(microsecond=0):
                return False
            source_unchanged = True
    return source_unchanged or bool(snapshot_deps)


def _iso(stamp: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(stamp.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def compute_targets(
    scope: set[str],
    rows: dict[str, dict],
    retarget: frozenset[str] = frozenset(),
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
        audit_status = row.get("audit_status") or "unaudited"
        cross_status = (row.get("cross_confirmation") or {}).get("status")
        awaiting_second = (
            audit_status == "audit_in_progress"
            and cross_status == "awaiting_second"
            and row.get("criticality") == "critical"
        )
        if audit_status != "unaudited" and not awaiting_second:
            skipped.append(f"{cid}: audit_status={row.get('audit_status')}")
            continue
        claim_type = row.get("claim_type") or row.get("claim_type_author_hint")
        if claim_type == "no_go":
            skipped.append(f"{cid}: no_go row - forensic tier, run individually")
            continue
        if claim_type not in AUDITABLE_TYPES:
            skipped.append(f"{cid}: claim_type={claim_type} - not batch-auditable")
            continue
        if source_requires_forensic(row):
            skipped.append(f"{cid}: source shape requires forensic tier")
            continue
        if not dep_ready(row, effective):
            skipped.append(f"{cid}: dependencies are not retained-grade")
            continue
        if note_hash_drifted(row):
            skipped.append(
                f"{cid}: ledger note_hash lags the note file; run "
                "seed_audit_ledger.py + pipeline and commit before auditing"
            )
            continue
        if (
            audit_status == "unaudited"
            and cid not in retarget
            and awaiting_repair_since_conditional(row, effective, rows)
        ):
            skipped.append(
                f"{cid}: awaiting repair (sources and deps unchanged since "
                "audited_conditional)"
            )
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


def passes_for_row(row: dict) -> list[int]:
    cross_status = (row.get("cross_confirmation") or {}).get("status")
    if row.get("audit_status") == "audit_in_progress" and cross_status == "awaiting_second":
        return [2]
    return [1, 2] if row.get("criticality") == "critical" else [1]


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
    round_no: int = 1,
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
    clipped_evidence = prompt_has_clipped_evidence(evidence_manifest)
    if clipped_evidence:
        prompt += (
            "\n\n---\nPACKET COMPLETENESS PREFLIGHT (binding):\n"
            "The restricted packet contains clipped load-bearing evidence at "
            f"{json.dumps(clipped_evidence)}. audited_clean is forbidden. "
            "Return the honest non-clean verdict and repair target. On this "
            "development-tier non-no-go row, preserve any negative-boundary "
            "judgment in negative_assertion_classes and rationale prose, but "
            "leave no_go_discipline=null unless you can supply a structurally "
            "valid optional packet from the rendered evidence.\n"
        )
    if len(prompt) > audit_runner.CODEX_INPUT_CHAR_LIMIT:
        raise ValueError(
            f"{cid}: development packet is {len(prompt)} characters; "
            "packet must be narrowed without converting transport size into a verdict"
        )

    # Artifact names carry the round so a claim legitimately re-entering a
    # later round (e.g. a critical row resuming at awaiting_second) never
    # collides with this round's directories.
    tag = f"{key}-r{round_no}-p{pass_no}"
    isolated = workdir / f"isolated-{tag}"
    isolated.mkdir(parents=True, exist_ok=False)
    prompt_path = isolated / "AUDIT_TASK.md"
    prompt_path.write_text(prompt, encoding="utf-8")
    output_schema = audit_runner.write_object_output_schema(
        isolated / "AUDIT_RESPONSE.schema.json"
    )
    raw_output = workdir / f"raw-{tag}.txt"
    delivery = workdir / f"delivery-{tag}.json"
    log_path = workdir / f"log-{tag}.txt"
    log_handle = log_path.open("w", encoding="utf-8")
    instruction = (
        "Open AUDIT_TASK.md in the current directory and follow it exactly. "
        "It is the complete restricted packet. Do not inspect any other file. "
        "Return only the response required by that packet."
    )
    try:
        proc = subprocess.Popen(
            [
                "codex", "exec", "--skip-git-repo-check", "--ignore-rules",
                "--sandbox", "read-only", "--model", MODEL,
                "-c", f"model_reasoning_effort='{REASONING}'",
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
    now_wall = time.time()
    return {
        "cid": cid,
        "row": row,
        "pass": pass_no,
        "proc": proc,
        "raw_output": raw_output,
        "delivery": delivery,
        "log_path": log_path,
        "log_handle": log_handle,
        "isolated": isolated,
        "evidence_manifest": evidence_manifest,
        "invocation_id": invocation_id,
        "transport_bound": None,
        "auditor": f"codex-audit-batch-{ident}",
        "independence": seat_independence(row, pass_no),
        "workdir": workdir,
        "last_size": 0,
        "last_activity": (0, 0.0),
        "last_progress": now,
        "last_progress_wall": now_wall,
        "stalled": False,
    }


PROGRESS = {
    "t0": None, "last": 0.0, "interval_sec": 900,
    "report": None, "round_targets": None, "jobs": None,
}
_TICKER_STARTED = False


def maybe_progress_summary(jobs: list[dict] | None = None, force: bool = False) -> None:
    """Print a one-block session summary at most every 15 minutes.

    Interpretation-free and inert: outcome counts come straight from the
    session report entries, and worker liveness is read from the
    `returncode` field that wait_workers maintains — this function touches
    no process object and mutates nothing but PROGRESS. Console output
    only, so cadence cannot perturb any tracked artifact.
    """
    now = time.monotonic()
    if PROGRESS["t0"] is None:
        PROGRESS["t0"] = now
        PROGRESS["last"] = now
        if not force:
            return
    if not force and now - PROGRESS["last"] < PROGRESS["interval_sec"]:
        return
    PROGRESS["last"] = now
    entries = PROGRESS.get("report") or []
    counts = Counter(str(entry.get("result")) for entry in entries)
    outcomes = ", ".join(f"{key} x{val}" for key, val in counts.most_common(8))
    active = []
    for job in jobs if jobs is not None else (PROGRESS.get("jobs") or []):
        if job.get("returncode") is None:
            minutes = int((now - job.get("started", now)) // 60)
            active.append(f"{job['row']['claim_id']}#p{job.get('pass', '?')}({minutes}m)")
    elapsed = int((now - PROGRESS["t0"]) // 60)
    parts = [
        f"== drain summary [{elapsed // 60}h{elapsed % 60:02d}m]",
        f"outcomes so far: {outcomes or 'none yet'}",
        f"active workers: {len(active)}"
        + (f" [{', '.join(active[:8])}]" if active else ""),
    ]
    if PROGRESS.get("round_targets") is not None:
        parts.append(f"dep-ready at round start: {PROGRESS['round_targets']}")
    print("; ".join(parts), flush=True)


def start_progress_ticker() -> None:
    """Daemon thread giving the 15-minute cadence full-session coverage,
    including the long serialized apply/pipeline/lint/push phases where the
    main thread is busy. Print-only; idempotent."""
    global _TICKER_STARTED
    if _TICKER_STARTED:
        return
    _TICKER_STARTED = True
    import threading

    def _loop() -> None:
        while True:
            time.sleep(max(1.0, PROGRESS["interval_sec"] / 30))
            maybe_progress_summary()

    threading.Thread(target=_loop, daemon=True, name="drain-progress").start()


def wait_workers(
    jobs: list[dict],
    stall_minutes: int = 45,
    on_claim_ready: Callable[[list[dict]], bool] | None = None,
) -> bool | None:
    """Monitor seats and optionally drain each complete claim immediately.

    Critical rows remain atomic because the callback is queued only after every
    launched seat for that claim has exited. One dedicated committer thread
    consumes that queue serially while this thread continues enforcing worker
    stall deadlines.

    Returns ``True``/``False`` when streaming is requested, and ``None`` for
    the legacy wait-only behavior used by judicial-panel callers.
    """
    pending = set(range(len(jobs)))
    dispatched_claims: set[str] = set()
    stall_seconds = stall_minutes * 60
    commit_queue: queue.Queue[list[dict] | object] = queue.Queue()
    commit_stop = object()
    commit_failed = threading.Event()
    commit_cancel = threading.Event()
    commit_errors: list[BaseException] = []
    committer: threading.Thread | None = None

    if on_claim_ready is not None:
        def _commit_loop() -> None:
            _COMMAND_CONTEXT.cancel_event = commit_cancel
            try:
                while True:
                    item = commit_queue.get()
                    try:
                        if item is commit_stop:
                            return
                        if commit_failed.is_set():
                            continue
                        assert isinstance(item, list)
                        if not on_claim_ready(item):
                            commit_failed.set()
                    except BaseException as exc:
                        commit_errors.append(exc)
                        commit_failed.set()
                    finally:
                        commit_queue.task_done()
            finally:
                del _COMMAND_CONTEXT.cancel_event

        committer = threading.Thread(
            target=_commit_loop,
            daemon=True,
            name="audit-serial-committer",
        )
        committer.start()

    PROGRESS["jobs"] = jobs
    try:
        while pending:
            if commit_failed.is_set():
                terminate_workers([jobs[index] for index in pending])
                pending.clear()
                break
            now = time.monotonic()
            now_wall = time.time()
            for index in list(pending):
                job = jobs[index]
                job.setdefault("started", now)
                job.setdefault("last_progress_wall", now_wall)
                job.setdefault("last_activity", (job.get("last_size", 0), 0.0))
                output = job["raw_output"]
                output_stat = output.stat() if output.exists() else None
                log_path = job["log_path"]
                log_stat = log_path.stat() if log_path.exists() else None
                output_size = output_stat.st_size if output_stat else 0
                log_size = log_stat.st_size if log_stat else 0
                size = output_size + log_size
                activity_mtime = max(
                    output_stat.st_mtime if output_stat else 0.0,
                    log_stat.st_mtime if log_stat else 0.0,
                )
                activity = (size, activity_mtime)
                if activity != job["last_activity"]:
                    job["last_activity"] = activity
                    job["last_size"] = size
                    job["last_progress"] = now
                    if activity_mtime:
                        job["last_progress_wall"] = activity_mtime
                returncode = job["proc"].poll()
                if returncode is not None:
                    job["returncode"] = returncode
                    job["proc"].wait()
                    if not job["log_handle"].closed:
                        job["log_handle"].close()
                    pending.remove(index)
                    continue
                if now_wall - job["last_progress_wall"] >= stall_seconds:
                    job["stalled"] = True
                    try:
                        os.killpg(job["proc"].pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    job["returncode"] = job["proc"].wait()
                    if not job["log_handle"].closed:
                        job["log_handle"].close()
                    pending.remove(index)

            if on_claim_ready is not None:
                ready_claims = sorted({
                    job["cid"]
                    for job in jobs
                    if job["cid"] not in dispatched_claims
                    and all(
                        peer.get("returncode") is not None
                        for peer in jobs
                        if peer["cid"] == job["cid"]
                    )
                })
                for cid in ready_claims:
                    claim_jobs = [job for job in jobs if job["cid"] == cid]
                    dispatched_claims.add(cid)
                    commit_queue.put(claim_jobs)
            if pending:
                time.sleep(2)

        if committer is not None:
            commit_queue.put(commit_stop)
            committer.join()
            if commit_errors:
                raise commit_errors[0]
            return not commit_failed.is_set()
        return None
    except BaseException:
        terminate_workers([jobs[index] for index in pending])
        if committer is not None and committer.is_alive():
            commit_failed.set()
            commit_cancel.set()
            commit_queue.put(commit_stop)
            committer.join()
        raise
    finally:
        PROGRESS["jobs"] = None
        for job in jobs:
            if not job["log_handle"].closed:
                job["log_handle"].close()


def terminate_workers(jobs: list[dict]) -> None:
    for job in jobs:
        if job["proc"].poll() is None:
            try:
                os.killpg(job["proc"].pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            job["returncode"] = job["proc"].wait()
        if not job["log_handle"].closed:
            job["log_handle"].close()


def schema_repair_guidance(blob: dict, validator_error: str | None) -> str:
    """Render exact, judgment-preserving guidance for known schema errors."""
    if not validator_error:
        return ""
    match = re.fullmatch(
        r"N8 echo (\d+)\.disposition must name its indexed mechanism",
        validator_error,
    )
    if match:
        index = int(match.group(1)) - 1
        packet = blob.get("no_go_discipline")
        echoes = (
            packet.get("N8_cross_cycle_echo", {}).get("echoes")
            if isinstance(packet, dict)
            else None
        )
        if isinstance(echoes, list) and 0 <= index < len(echoes):
            echo = echoes[index]
            mechanism = echo.get("mechanism") if isinstance(echo, dict) else None
            if isinstance(mechanism, str) and mechanism.strip():
                quoted = json.dumps(mechanism, ensure_ascii=False)
                return (
                    "\nMechanical repair guidance: preserve every judgment and "
                    f"copy the exact mechanism string {quoted} verbatim into "
                    f"N8_cross_cycle_echo.echoes[{index}].disposition. The "
                    "validator requires that exact normalized substring; do not "
                    "paraphrase it or change the mechanism field.\n"
                )
    return ""


def _wait_for_packet_completion(proc: subprocess.Popen) -> tuple[bool, int]:
    """Wait for packet repair, killing promptly when the committer is cancelled."""
    deadline = time.monotonic() + PACKET_COMPLETION_STALL_SECONDS
    polling_failed = False
    cancelled = False
    try:
        while time.monotonic() < deadline and proc.poll() is None:
            cancel_event = _command_cancel_event()
            if cancel_event is not None:
                if cancel_event.wait(PACKET_COMPLETION_POLL_SECONDS):
                    cancelled = True
                    break
            else:
                time.sleep(PACKET_COMPLETION_POLL_SECONDS)
        cancelled = cancelled or _command_cancelled()
        if proc.poll() is None and not cancelled:
            try:
                proc.wait(timeout=PACKET_COMPLETION_EXIT_GRACE_SECONDS)
            except subprocess.TimeoutExpired:
                pass
    except OSError:
        polling_failed = True
    finally:
        if proc.poll() is None:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        returncode = proc.wait()
    return polling_failed, returncode


def packet_completion_pass(
    job: dict,
    blob: dict,
    workdir: Path,
    validator_error: str | None = None,
    attempt: int = 1,
) -> dict | None:
    """Mechanically complete or repair one structural N1-N8 packet.

    The same restricted audit seat sees only its original packet, rejected
    JSON, and exact validator error.  Every top-level judgment remains
    immutable; only ``no_go_discipline`` may be added or replaced.
    """

    cid = job["row"]["claim_id"]
    key = artifact_key(cid)
    attempt_key = f"{key}-p{job['pass']}-a{attempt}"
    blob_path = workdir / f"completion-{attempt_key}.json"
    blob_path.write_text(json.dumps(blob, indent=1), encoding="utf-8")
    out_path = workdir / f"completion-{attempt_key}-out.json"
    out_path.unlink(missing_ok=True)
    output_schema = audit_runner.write_object_output_schema(
        job["isolated"] / "AUDIT_COMPLETION_RESPONSE.schema.json",
        allow_compute_required=False,
    )
    log_path = workdir / f"completion-{attempt_key}.log"
    error_block = (
        "\nThe validator rejected the previous packet with EXACTLY this "
        f"error — fix precisely this, nothing else:\n    {validator_error}\n"
        f"{schema_repair_guidance(blob, validator_error)}"
        if validator_error
        else ""
    )
    spec = (
        f"# FOCUSED COMPLETION (audit seat {job['auditor']}, attempt {attempt})\n\n"
        "Reopen AUDIT_TASK.md in the current directory. It is the complete "
        "restricted packet used by this audit seat; do not inspect any other "
        "evidence. "
        f"Your audit JSON for claim {cid} is at: {blob_path}\n"
        f"{error_block}\n"
        "Your verdict output names walls/negative boundaries, so the apply "
        "gate requires a structural `no_go_discipline` object (development "
        "tier). Use the N1-N8 schema in AUDIT_TASK.md and author it "
        "SCHEMA-HONESTLY:\n"
        "- Claim gate status PASS only if it genuinely passes: at least 5 "
        "DISTINCT route_class values among evidenced N1 routes, every route "
        "closed, complete N2-N8, and a resolved N7 steelman whose route_id "
        "names an N1 route and whose evidence_path MATCHES that route's "
        "evidence_path.\n"
        "- Otherwise set status FAIL with the honest failures list AND the "
        "FAIL-only fields (demotion, prior_claim_scope, narrowed_claim_scope, "
        "corrected_wall_set, next_route). For an existing non-clean verdict, "
        "an honest FAIL gate is legitimate and validates; an unearned PASS "
        "does not. Preserve the existing verdict either way.\n"
        "- Structured judgments with quoted evidence from the note/runner you "
        "already audited (structural validation; no manifest-containment, "
        "live-stdout, transport, or full-universe disposition plumbing).\n"
        "Change NOTHING else — preserve every original field and value. "
        "Return the complete JSON as your final response: one JSON object, "
        "with no code fence or commentary."
    )
    codex_bin = shutil.which("codex")
    if not codex_bin:
        return None
    if _command_cancelled():
        return None
    command = [
        codex_bin, "exec", "--skip-git-repo-check", "--ignore-rules",
        "--ignore-user-config", "--ephemeral",
        "--sandbox", "read-only", "--model", MODEL,
        "-c", f"model_reasoning_effort='{REASONING}'",
        "--output-schema", str(output_schema),
        "--output-last-message", str(out_path), spec,
    ]
    sandbox_exec = Path("/usr/bin/sandbox-exec")
    if sandbox_exec.exists():
        escaped_root = str(REPO_ROOT).replace("\\", "\\\\").replace('"', '\\"')
        profile = (
            '(version 1) (allow default) '
            f'(deny file-write* (subpath "{escaped_root}"))'
        )
        command = [str(sandbox_exec), "-p", profile, *command]
    else:
        try:
            launcher_text = Path(codex_bin).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            launcher_text = ""
        if "dangerously-bypass-approvals-and-sandbox" in launcher_text:
            return None

    with log_path.open("w", encoding="utf-8") as log:
        proc = subprocess.Popen(
            command,
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=log,
            cwd=job["isolated"],
            start_new_session=True,
        )
        polling_failed, returncode = _wait_for_packet_completion(proc)

    if polling_failed or returncode != 0:
        return None
    if not (out_path.exists() and out_path.stat().st_size > MIN_DELIVERY_BYTES):
        return None
    try:
        completed = json.loads(out_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    if not isinstance(completed, dict):
        return None
    if completed.get("compute_required") is None:
        completed.pop("compute_required", None)
    packet = completed.get("no_go_discipline")
    if not isinstance(packet, dict):
        return None

    # This is packet completion, not a second scientific audit: the only
    # permitted delta is adding or replacing the structural packet.
    expected = dict(blob)
    expected["no_go_discipline"] = packet
    canonical_completed = json.dumps(
        completed, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )
    canonical_expected = json.dumps(
        expected, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )
    if canonical_completed != canonical_expected:
        return None
    return completed


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
    validation_args = {
        "source_requires_no_go": source_requires_no_go,
        "evidence_manifest": None,
        "prior_claim_scope": audit_runner.prior_claim_scope_for_row(row),
        "expected_invocation_id": job["invocation_id"],
        "transport_bounded_n8": job["transport_bound"] is not None,
    }
    error = audit_runner.validate_verdict(blob, cid, **validation_args)
    def _packet_error(err: object) -> bool:
        return bool(re.search(
            r"(?:\bN[1-8](?:\b|_)|No-Go Discipline|no_go_discipline)",
            str(err or ""),
        ))

    optional_packet_dropped = False
    forensic_tier = bool(
        source_requires_no_go
        or blob.get("claim_type") == "no_go"
        or audit_runner.no_go_discipline_gate.forensic_mode()
    )
    if (
        error
        and _packet_error(error)
        and isinstance(blob.get("no_go_discipline"), dict)
        and blob.get("verdict") != "audited_clean"
        and not forensic_tier
    ):
        # In the development tier a non-clean verdict on a non-no-go source
        # carries its negative judgment in the declaration/rationale; the
        # heavyweight packet is optional.  A volunteered but schema-invalid
        # optional packet must not consume two 20-minute completion attempts
        # or quarantine an otherwise valid scientific verdict.  Prove that it
        # is optional by removing only that field and rerunning the unchanged
        # canonical validator; clean/no-go/forensic verdicts still fail closed.
        without_optional_packet = dict(blob)
        without_optional_packet["no_go_discipline"] = None
        if audit_runner.validate_verdict(
            without_optional_packet, cid, **validation_args
        ) is None:
            blob = without_optional_packet
            error = None
            optional_packet_dropped = True

    completion_attempt = 0
    while (
        error
        and not source_requires_no_go
        and _packet_error(error)
        and completion_attempt < 2
    ):
        completion_attempt += 1
        completed = packet_completion_pass(
            job, blob, job["workdir"],
            validator_error=str(error), attempt=completion_attempt,
        )
        if completed is None:
            break
        blob = completed
        error = audit_runner.validate_verdict(blob, cid, **validation_args)
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
    result = {**base, "result": "delivery_validated"}
    if optional_packet_dropped:
        result["detail"] = "invalid optional development-tier no_go_discipline dropped"
    return envelope, result


def _file_snapshot_signature(file_stat: os.stat_result) -> tuple:
    """State that must remain unchanged before an in-place byte rewrite."""
    return (
        file_stat.st_dev,
        file_stat.st_ino,
        file_stat.st_nlink,
        file_stat.st_uid,
        file_stat.st_gid,
        file_stat.st_size,
        file_stat.st_mtime_ns,
        file_stat.st_ctime_ns,
        stat.S_IMODE(file_stat.st_mode),
        getattr(file_stat, "st_flags", None),
    )


def recover_lane_certification_provenance_drift(
    status_output: str,
    *,
    honor_cancel: bool = True,
) -> bool:
    """Recognize exact legacy ``repo_head``-only drift at a sync boundary.

    ``lane_certification.json`` used to embed the current commit. A pipeline
    refresh therefore dirtied the file as soon as a later commit changed
    ``HEAD``. This recovery is intentionally narrower than the audit generated
    path allowlist: it accepts one unstaged modified file, requires its bytes to
    be exactly either the committed payload with the obsolete field removed or
    with that field refreshed to the current commit, and refuses every staged,
    untracked, deleted, malformed, metadata, or content-bearing change. The
    verified content-only state is carried through the sync boundary without
    mutating it. The next normal pipeline/commit removes the obsolete field.
    This classifier never writes the file, its metadata, or a neighboring path.
    """
    if status_output.splitlines() != [f" M {LANE_CERTIFICATION_PATH}"]:
        return False

    committed = sh(
        ["git", "show", f"HEAD:{LANE_CERTIFICATION_PATH}"],
        honor_cancel=honor_cancel,
        text=False,
    )
    if committed.returncode != 0:
        return False
    path = REPO_ROOT / LANE_CERTIFICATION_PATH
    try:
        working_bytes = path.read_bytes()
        working_stat = path.lstat()
    except OSError:
        return False
    if not stat.S_ISREG(working_stat.st_mode):
        return False
    if stat.S_IMODE(working_stat.st_mode) != 0o644:
        return False
    if working_stat.st_nlink != 1:
        return False
    if working_stat.st_uid != os.geteuid():
        return False
    if getattr(working_stat, "st_flags", 0):
        return False
    if not os.access(path, os.W_OK):
        return False
    working_signature = _file_snapshot_signature(working_stat)

    provenance_pattern = re.compile(
        rb'(?m)^(  "repo_head": ")([0-9a-f]{40})(",)(\r?\n)'
    )
    provenance_matches = list(provenance_pattern.finditer(committed.stdout))
    if len(provenance_matches) != 1:
        return False
    provenance = provenance_matches[0]
    without_provenance = (
        committed.stdout[: provenance.start()]
        + committed.stdout[provenance.end() :]
    )
    head = sh(["git", "rev-parse", "HEAD"], honor_cancel=honor_cancel)
    if head.returncode != 0:
        return False
    current_head = head.stdout.strip()
    if re.fullmatch(r"[0-9a-f]{40}", current_head) is None:
        return False
    if working_bytes != without_provenance:
        working_matches = list(provenance_pattern.finditer(working_bytes))
        if len(working_matches) != 1:
            return False
        working_provenance = working_matches[0]
        working_head_bytes = working_provenance.group(2)
        with_working_head = (
            committed.stdout[: provenance.start(2)]
            + working_head_bytes
            + committed.stdout[provenance.end(2) :]
        )
        if working_bytes != with_working_head:
            return False
        working_head = working_head_bytes.decode("ascii")
        ancestor = sh(
            ["git", "merge-base", "--is-ancestor", working_head, current_head],
            honor_cancel=honor_cancel,
        )
        if ancestor.returncode != 0:
            return False

    metadata = sh(
        [
            "git",
            "diff",
            "--no-ext-diff",
            "--no-color",
            "--summary",
            "--",
            LANE_CERTIFICATION_PATH,
        ],
        honor_cancel=honor_cancel,
    )
    if metadata.returncode != 0 or metadata.stdout.strip():
        return False

    patch = sh(
        [
            "git",
            "diff",
            "--no-ext-diff",
            "--no-textconv",
            "--no-color",
            "--binary",
            "--src-prefix=a/",
            "--dst-prefix=b/",
            "--",
            LANE_CERTIFICATION_PATH,
        ],
        honor_cancel=honor_cancel,
        text=False,
    )
    if patch.returncode != 0 or not patch.stdout:
        return False
    forbidden_patch_markers = (
        b"old mode ",
        b"new mode ",
        b"new file mode ",
        b"deleted file mode ",
        b"GIT binary patch",
    )
    if any(marker in patch.stdout for marker in forbidden_patch_markers):
        return False
    metadata = sh(
        [
            "git",
            "diff",
            "--no-ext-diff",
            "--no-color",
            "--summary",
            "--",
            LANE_CERTIFICATION_PATH,
        ],
        honor_cancel=honor_cancel,
    )
    if metadata.returncode != 0 or metadata.stdout.strip():
        return False
    try:
        if path.read_bytes() != working_bytes:
            return False
        current_stat = path.lstat()
    except OSError:
        return False
    if not stat.S_ISREG(current_stat.st_mode):
        return False
    if _file_snapshot_signature(current_stat) != working_signature:
        return False

    print(
        "recognized generated certification provenance drift: "
        f"{LANE_CERTIFICATION_PATH}",
        flush=True,
    )
    return True


def clean_main_error(*, honor_cancel: bool = True) -> str | None:
    branch = sh(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        honor_cancel=honor_cancel,
    )
    if branch.returncode != 0:
        return "cannot determine current branch"
    if branch.stdout.strip() != "main":
        return f"not on main (currently {branch.stdout.strip()!r})"
    status = sh(["git", "status", "--porcelain"], honor_cancel=honor_cancel)
    if status.returncode != 0:
        return "cannot determine worktree status"
    if status.stdout.strip():
        path = REPO_ROOT / LANE_CERTIFICATION_PATH
        try:
            recognition_snapshot = (
                path.read_bytes(),
                _file_snapshot_signature(path.lstat()),
            )
        except OSError:
            return "working tree is not clean"
        recognized = recover_lane_certification_provenance_drift(
            status.stdout,
            honor_cancel=honor_cancel,
        )
        if not recognized:
            return "working tree is not clean"
        status_after = sh(
            ["git", "status", "--porcelain"],
            honor_cancel=honor_cancel,
        )
        if status_after.returncode != 0:
            return "cannot determine worktree status after provenance recognition"
        if status_after.stdout.splitlines() != [
            f" M {LANE_CERTIFICATION_PATH}"
        ]:
            return "working tree is not clean after provenance recognition"
        try:
            stable_snapshot = (
                path.read_bytes(),
                _file_snapshot_signature(path.lstat()),
            )
        except OSError:
            return "working tree is not clean after provenance recognition"
        if stable_snapshot != recognition_snapshot:
            return "working tree is not clean after provenance recognition"
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
    names: set[str] = set()
    commands = (
        ["git", "diff", "--name-only"],
        ["git", "diff", "--name-only", "--cached"],
        ["git", "ls-files", "--others", "--exclude-standard"],
    )
    for command in commands:
        result = sh(command)
        if result.returncode != 0:
            raise RuntimeError(
                f"{' '.join(command)} failed: "
                f"{(result.stderr or result.stdout).strip()[:240]}"
            )
        names.update(result.stdout.splitlines())
    return sorted(name for name in names if name)


def allowed_generated_path(path: str) -> bool:
    return any(
        path == allowed or path.startswith(allowed + "/")
        for allowed in audit_runner.AUDIT_DATA_FILES
    )


def verdict_only_generated_path(path: str) -> bool:
    return static_checkpoint.verdict_generated_path(path)


def verdict_only_pipeline_eligibility() -> tuple[bool, str]:
    """Fail-closed wrapper around the shell entry point's shared proof."""
    return static_checkpoint.verify_checkpoint()


def run_generated_gates() -> tuple[bool, str]:
    """Run generated-surface gates once per claim transaction."""
    verdict_only, mode_detail = verdict_only_pipeline_eligibility()
    pipeline_command = ["bash", str(SCRIPTS / "run_pipeline.sh")]
    if verdict_only:
        pipeline_command.append("--verdict-only")
    print(
        "generated gate mode: "
        f"{'verdict-only' if verdict_only else 'full'} ({mode_detail})",
        flush=True,
    )
    pipeline = sh(pipeline_command, timeout=1800)
    if pipeline.returncode != 0:
        return False, f"pipeline failed: {(pipeline.stderr or pipeline.stdout)[-400:]}"
    lint = sh([sys.executable, str(SCRIPTS / "audit_lint.py"), "--strict"], timeout=600)
    if lint.returncode != 0:
        return False, f"strict lint failed: {(lint.stderr or lint.stdout)[-400:]}"
    diff_check = sh(["git", "diff", "--check"])
    if diff_check.returncode != 0:
        return False, f"git diff --check failed: {diff_check.stdout[-400:]}"
    try:
        unexpected = [
            path for path in changed_paths()
            if not allowed_generated_path(path)
        ]
    except RuntimeError as exc:
        return False, f"generated-path inspection failed: {exc}"
    if unexpected:
        return False, f"unexpected generated paths: {unexpected[:8]}"
    return True, "gates passed"


def run_apply_gates(envelope: dict) -> tuple[bool, str]:
    """Compatibility wrapper for one-seat callers and focused tests."""
    ok, message = audit_runner.apply_one(
        envelope["audit"],
        propagate=False,
        evidence_manifest=envelope["evidence_manifest"],
    )
    if not ok:
        return False, f"apply rejected: {message[:400]}"
    return run_generated_gates()


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


def reset_to_origin_main() -> tuple[bool, str]:
    # Rollback must remain available after a cancellation request; otherwise
    # an interrupted commit/push can strand dirty or ahead local main state.
    target = sh(
        ["git", "rev-parse", "origin/main"],
        honor_cancel=False,
    )
    target_oid = target.stdout.strip()
    if target.returncode != 0 or not re.fullmatch(r"[0-9a-f]{40}", target_oid):
        return False, "cannot resolve rollback target origin/main"
    reset = sh(
        ["git", "reset", "--hard", target_oid],
        honor_cancel=False,
    )
    if reset.returncode != 0:
        return False, f"reset failed: {(reset.stderr or reset.stdout).strip()[:240]}"
    branch = sh(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        honor_cancel=False,
    )
    if branch.returncode != 0:
        return False, "cannot determine current branch after rollback"
    if branch.stdout.strip() != "main":
        return False, (
            "rollback did not leave main checked out "
            f"({branch.stdout.strip()!r})"
        )
    status = sh(
        ["git", "status", "--porcelain"],
        honor_cancel=False,
    )
    if status.returncode != 0:
        return False, "cannot determine worktree status after rollback"
    if status.stdout.strip():
        # The normal main guard can tolerate one mechanically recognized
        # lane-certification provenance drift. Transaction rollback cannot:
        # quarantine is permitted only after reset proves literal zero-diff
        # source and generated state.
        return False, "rollback did not leave a literally clean worktree"
    head = sh(["git", "rev-parse", "HEAD"], honor_cancel=False)
    remote = sh(["git", "rev-parse", "origin/main"], honor_cancel=False)
    if head.returncode != 0 or remote.returncode != 0:
        return False, "cannot verify rollback refs"
    if head.stdout.strip() != target_oid or remote.stdout.strip() != target_oid:
        return False, "rollback did not leave HEAD synchronized with origin/main"
    return True, f"reset to origin/main at {target_oid}"


def apply_claim_serialized(
    deliveries: list[tuple[dict, dict]],
    retries: int,
) -> tuple[bool, list[dict]]:
    """Apply every validated seat for one claim as one transaction.

    Critical rows commonly deliver both independent seats together. Applying
    them before one pipeline/lint/commit/push preserves every seat transition
    while amortizing the generated-surface cost. Push-race retries replay the
    complete claim transaction from the refreshed canonical parent.
    """
    ordered = sorted(deliveries, key=lambda item: item[0]["pass"])
    claim_ids = {job["cid"] for job, _ in ordered}
    if len(claim_ids) != 1 or not ordered:
        raise ValueError("one non-empty claim delivery group is required")
    cid = next(iter(claim_ids))

    def fail_after_transaction(
        result: str,
        detail: str | None = None,
        *,
        pass_no: int | None = None,
    ):
        reset, reset_detail = reset_to_origin_main()
        if not reset:
            return False, [{
                "cid": cid,
                "result": "race_reset_failed",
                "detail": f"{result}: {detail or 'transaction failed'}; {reset_detail}",
            }]
        failure = {"cid": cid, "result": result}
        if pass_no is not None:
            failure["pass"] = pass_no
        if detail is not None:
            failure["detail"] = detail
        failure["rollback_verified"] = True
        failure["rollback_detail"] = reset_detail
        return False, [failure]

    for attempt in range(1, retries + 1):
        synced, detail = sync_origin_main()
        if not synced:
            return False, [{"cid": cid, "result": "sync_blocked", "detail": detail}]

        for job, envelope in ordered:
            applied, apply_detail = audit_runner.apply_one(
                envelope["audit"],
                propagate=False,
                evidence_manifest=envelope["evidence_manifest"],
            )
            if not applied:
                return fail_after_transaction(
                    "apply_or_gate_failed",
                    f"apply rejected: {apply_detail[:400]}",
                    pass_no=job["pass"],
                )

        gated, detail = run_generated_gates()
        if not gated:
            return fail_after_transaction("apply_or_gate_failed", detail)
        verdicts = [str(envelope["audit"].get("verdict")) for _, envelope in ordered]
        seats = ["first" if job["pass"] == 1 else "second" for job, _ in ordered]
        committed, detail = stage_and_commit(
            f"audit: {cid} {'+'.join(verdicts)} "
            f"(codex-cli, {MODEL}, {REASONING}, {'+'.join(seats)}/batch)"
        )
        if not committed:
            return fail_after_transaction("commit_failed", detail)
        local_commit = detail
        push = sh(["git", "push", "-q", "origin", "HEAD:main"])
        if push.returncode == 0:
            return True, [
                {
                    "cid": cid,
                    "pass": job["pass"],
                    "result": envelope["audit"].get("verdict"),
                    "commit": local_commit,
                }
                for job, envelope in ordered
            ]

        if _command_cancelled():
            return fail_after_transaction("commit_cancelled")

        fetch = sh(["git", "fetch", "origin", "main", "-q"])
        if fetch.returncode != 0:
            result = "commit_cancelled" if _command_cancelled() else "push_failed"
            detail = None if result == "commit_cancelled" else "push and follow-up fetch failed"
            return fail_after_transaction(result, detail)
        if _command_cancelled():
            return fail_after_transaction("commit_cancelled")
        landed = sh(["git", "merge-base", "--is-ancestor", local_commit, "origin/main"])
        if _command_cancelled():
            return fail_after_transaction("commit_cancelled")
        if landed.returncode == 0:
            return True, [
                {
                    "cid": cid,
                    "pass": job["pass"],
                    "result": envelope["audit"].get("verdict"),
                    "commit": local_commit,
                }
                for job, envelope in ordered
            ]
        if attempt == retries:
            return fail_after_transaction("push_race_exhausted")
        reset, reset_detail = reset_to_origin_main()
        if not reset:
            return False, [{"cid": cid, "result": "race_reset_failed", "detail": reset_detail}]
    return False, [{"cid": cid, "result": "unreachable"}]


def apply_one_serialized(
    job: dict,
    envelope: dict,
    retries: int,
) -> tuple[bool, dict]:
    """Backward-compatible one-seat facade over the claim transaction."""
    ok, results = apply_claim_serialized([(job, envelope)], retries)
    return ok, results[0]


def science_fix_handoff(job: dict, envelope: dict) -> dict | None:
    """Build a source-repair handoff only from a validated non-clean audit."""
    audit = envelope.get("audit")
    if not isinstance(audit, dict):
        return None
    verdict = audit.get("verdict")
    category = {
        "audited_renaming": "renaming",
        "audited_failed": "failed",
        "audited_numerical_match": "numerical_match",
    }.get(verdict)
    notes = str(audit.get("notes_for_re_audit_if_any") or "").strip()
    if verdict == "audited_conditional":
        conditional_categories = {
            "runner_artifact_issue": "conditional_runner_artifact_issue",
            "scope_too_broad": "conditional_scope_too_broad",
            "missing_dependency_edge": "conditional_missing_dependency_edge",
            "missing_bridge_theorem": "conditional_missing_bridge_theorem",
        }
        prefix = notes.split("—", 1)[0].split(":", 1)[0].strip().lower()
        category = conditional_categories.get(prefix)
    if category is None:
        return None

    row = job["row"]
    cid = job["cid"]
    note_path = str(row.get("note_path") or "").strip()
    if not note_path:
        return None
    claim_scope = str(audit.get("claim_scope") or "").strip()
    rationale = str(audit.get("verdict_rationale") or "").strip()
    load_bearing = str(audit.get("load_bearing_step") or "").strip()
    claim_type = str(
        audit.get("claim_type") or row.get("claim_type") or ""
    ).strip()
    step_class = str(
        audit.get("load_bearing_step_class")
        or row.get("load_bearing_step_class")
        or ""
    ).strip()
    invocation_id = str(audit.get("audit_invocation_id") or "").strip()
    # Auto-dispatch is allowed only for a complete, independently checkable
    # action packet.  Successful application alone does not make an empty or
    # vague repair request safe to hand to a source-editing worker.
    if not all(
        (
            invocation_id,
            claim_type,
            step_class,
            claim_scope,
            rationale,
            load_bearing,
            notes,
        )
    ):
        return None
    return {
        "category": category,
        "claim_id": cid,
        "note_path": note_path,
        "descendants": int(row.get("transitive_descendants") or 0),
        "cls": step_class,
        "audit_invocation_id": invocation_id,
        "audit_verdict": verdict,
        "claim_type": claim_type,
        "claim_scope": claim_scope,
        "verdict_rationale": rationale,
        "load_bearing_step": load_bearing,
        "repair_target": notes,
    }


def launch_science_fix_worker(
    handoffs: list[dict], workdir: Path,
) -> tuple[int, Path, Path] | None:
    """Launch one detached PR-producing repair worker for validated handoffs."""
    unique = {row["claim_id"]: row for row in handoffs}
    if not unique:
        return None
    handoff_path = workdir / "science-fix-handoff.json"
    handoff_path.write_text(
        json.dumps(
            {
                "schema": "audit_science_fix_handoff_v1",
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "rows": [unique[cid] for cid in sorted(unique)],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    log_path = workdir / "science-fix-worker.log"
    log = log_path.open("a", encoding="utf-8")
    try:
        proc = subprocess.Popen(
            [
                sys.executable,
                str(SCIENCE_FIX),
                "--handoff-file",
                str(handoff_path),
                "--n",
                str(len(unique)),
                # A newly applied audit is fresh repair evidence. Retry an old
                # no-edit/timeout attempt for these bounded handoff rows while
                # science_fix_loop still excludes active or open-PR claims.
                "--retry-failed",
            ],
            cwd=REPO_ROOT,
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    finally:
        log.close()
    return proc.pid, handoff_path, log_path


def _campaign_json_object(pairs: list[tuple[str, object]]) -> dict:
    record: dict = {}
    for key, value in pairs:
        if key in record:
            raise ValueError(f"duplicate JSON key {key!r}")
        record[key] = value
    return record


def _reject_campaign_json_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON value {value!r}")


def _contains_non_finite_json_number(value: object) -> bool:
    if isinstance(value, float):
        return not math.isfinite(value)
    if isinstance(value, list):
        return any(_contains_non_finite_json_number(item) for item in value)
    if isinstance(value, dict):
        return any(
            _contains_non_finite_json_number(item)
            for item in value.values()
        )
    return False


def _campaign_failure_schema_error(
    claim_id: str,
    reason: str,
    failure: object,
) -> str | None:
    if not isinstance(failure, dict):
        return "campaign exclusion failure is not an object"
    result = failure.get("result")
    if not isinstance(result, str):
        return "campaign exclusion failure has no string result"
    if failure.get("cid") != claim_id:
        return "campaign exclusion failure cid does not match claim_id"

    if reason == SCHEMA_QUARANTINE_RESULT:
        expected = {"cid", "pass", "result"}
        if result == "validation_failed":
            expected.add("detail")
        elif result != "malformed_json":
            return (
                "campaign exclusion failure result is incompatible with "
                f"{reason!r}"
            )
    elif reason == COMPUTE_QUARANTINE_RESULT:
        if result != "compute_required":
            return (
                "campaign exclusion failure result is incompatible with "
                f"{reason!r}"
            )
        expected = {"cid", "pass", "result", "detail"}
    elif reason == CLAIM_TRANSACTION_QUARANTINE_RESULT:
        if result == "apply_or_gate_failed":
            expected = {
                "cid",
                "result",
                "detail",
                "rollback_verified",
                "rollback_detail",
            }
            if "pass" in failure:
                expected.add("pass")
            if failure.get("rollback_verified") is not True:
                return (
                    "claim-transaction failure has no verified rollback proof"
                )
            rollback_detail = failure.get("rollback_detail")
            if (
                not isinstance(rollback_detail, str)
                or not rollback_detail.strip()
            ):
                return (
                    "claim-transaction failure has no rollback detail"
                )
        elif result == CLAIM_TRANSACTION_QUARANTINE_RESULT:
            expected = {"cid", "result", "detail"}
        else:
            return (
                "campaign exclusion failure result is incompatible with "
                f"{reason!r}"
            )
    else:
        return f"unsupported failure-bearing exclusion reason {reason!r}"

    if set(failure) != expected:
        missing = sorted(expected - set(failure))
        unexpected = sorted(set(failure) - expected)
        return (
            "invalid campaign exclusion failure fields "
            f"(missing={missing}, unexpected={unexpected})"
        )
    if "pass" in expected:
        pass_no = failure.get("pass")
        if type(pass_no) is not int or pass_no not in {1, 2}:
            return "campaign exclusion failure pass must be 1 or 2"
    if "detail" in expected:
        detail = failure.get("detail")
        if not isinstance(detail, str) or not detail.strip():
            return "campaign exclusion failure has no detail"
    return None


def load_campaign_exclusion_records(path: Path | None) -> list[dict]:
    if path is None or not path.exists():
        return []
    records: list[dict] = []
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        if not line.strip():
            raise ValueError(
                f"{path}:{line_number}: blank campaign exclusion record"
            )
        try:
            record = json.loads(
                line,
                object_pairs_hook=_campaign_json_object,
                parse_constant=_reject_campaign_json_constant,
            )
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"{path}:{line_number}: invalid campaign exclusion JSON: "
                f"{exc.msg}"
            ) from exc
        except ValueError as exc:
            raise ValueError(
                f"{path}:{line_number}: invalid campaign exclusion JSON: {exc}"
            ) from exc
        if _contains_non_finite_json_number(record):
            raise ValueError(
                f"{path}:{line_number}: campaign exclusion contains a "
                "non-finite JSON number"
            )
        if not isinstance(record, dict):
            raise ValueError(
                f"{path}:{line_number}: campaign exclusion is not an object"
            )
        cid = record.get("claim_id")
        reason = record.get("reason")
        if not isinstance(cid, str) or not cid:
            raise ValueError(
                f"{path}:{line_number}: campaign exclusion has no claim_id"
            )
        if not isinstance(reason, str) or not reason:
            raise ValueError(
                f"{path}:{line_number}: campaign exclusion has no reason"
            )
        if reason not in CAMPAIGN_EXCLUSION_REASONS:
            raise ValueError(
                f"{path}:{line_number}: unrecognized campaign exclusion "
                f"reason {reason!r}"
            )
        common_fields = {"claim_id", "reason", "recorded_at"}
        if reason == BLOCKED_ROW_QUARANTINE_RESULT:
            expected_fields = common_fields | {"invalidation_reason"}
        else:
            expected_fields = common_fields | {"failures"}
        if set(record) != expected_fields:
            missing = sorted(expected_fields - set(record))
            unexpected = sorted(set(record) - expected_fields)
            raise ValueError(
                f"{path}:{line_number}: invalid campaign exclusion fields "
                f"(missing={missing}, unexpected={unexpected})"
            )
        try:
            ledger_io.shard_path(cid)
        except ValueError as exc:
            raise ValueError(
                f"{path}:{line_number}: campaign exclusion claim_id is not "
                f"shard-safe: {cid!r}"
            ) from exc
        recorded_at = record["recorded_at"]
        if not isinstance(recorded_at, str) or not recorded_at:
            raise ValueError(
                f"{path}:{line_number}: campaign exclusion has no recorded_at"
            )
        if not re.fullmatch(
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}"
            r"(?:\.\d{6})?\+00:00",
            recorded_at,
        ):
            raise ValueError(
                f"{path}:{line_number}: campaign exclusion recorded_at "
                "is not canonical UTC ISO-8601"
            )
        try:
            timestamp = datetime.fromisoformat(recorded_at)
        except ValueError as exc:
            raise ValueError(
                f"{path}:{line_number}: campaign exclusion recorded_at "
                "is not ISO-8601"
            ) from exc
        if (
            timestamp.tzinfo is None
            or timestamp.utcoffset() != timezone.utc.utcoffset(timestamp)
        ):
            raise ValueError(
                f"{path}:{line_number}: campaign exclusion recorded_at "
                "is not UTC"
            )
        if reason == BLOCKED_ROW_QUARANTINE_RESULT:
            invalidation_reason = record["invalidation_reason"]
            if (
                not isinstance(invalidation_reason, str)
                or not invalidation_reason.strip()
            ):
                raise ValueError(
                    f"{path}:{line_number}: blocked-row exclusion has no "
                    "invalidation_reason"
                )
        else:
            failures = record["failures"]
            if not isinstance(failures, list) or not failures:
                raise ValueError(
                    f"{path}:{line_number}: campaign exclusion failures "
                    "must be a non-empty list of objects"
                )
            for failure in failures:
                failure_error = _campaign_failure_schema_error(
                    cid,
                    reason,
                    failure,
                )
                if failure_error is not None:
                    raise ValueError(
                        f"{path}:{line_number}: {failure_error}"
                    )
            if (
                reason == CLAIM_TRANSACTION_QUARANTINE_RESULT
                and not any(
                    failure.get("result") == "apply_or_gate_failed"
                    and failure.get("rollback_verified") is True
                    for failure in failures
                )
            ):
                raise ValueError(
                    f"{path}:{line_number}: claim-transaction exclusion has "
                    "no verified apply/gate rollback failure"
                )
        records.append(record)
    return records


def selection_skip_reason(detail: str) -> str:
    """Map the canonical selector diagnostic to a stable repair route."""
    if detail == "missing ledger row":
        return "missing_ledger_row"
    if detail.startswith("audit_status="):
        return "audit_status_not_unaudited"
    if detail == "no_go row - forensic tier, run individually":
        return "forensic_no_go"
    if detail.startswith("claim_type=") and detail.endswith(
        " - not batch-auditable"
    ):
        return "non_batch_claim_type"
    if detail == "source shape requires forensic tier":
        return "forensic_source_shape"
    if detail == "dependencies are not retained-grade":
        return "dependencies_not_retained"
    if detail.startswith("ledger note_hash lags the note file;"):
        return "note_hash_drift"
    if detail.startswith("awaiting repair (sources and deps unchanged"):
        return "awaiting_science_repair"
    return "unclassified_selector_skip"


def selector_skip_record(line: str) -> dict:
    claim_id, separator, detail = line.partition(": ")
    if not separator or not claim_id or not detail:
        raise ValueError(f"invalid selector skip diagnostic: {line!r}")
    try:
        ledger_io.shard_path(claim_id)
    except ValueError as exc:
        raise ValueError(
            f"selector skip claim_id is not shard-safe: {claim_id!r}"
        ) from exc
    return {
        "claim_id": claim_id,
        "reason": selection_skip_reason(detail),
        "detail": detail,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    }


def load_campaign_selection_skip_records(path: Path | None) -> list[dict]:
    """Strictly load durable selector dispositions without excluding rows."""
    if path is None or not path.exists():
        return []
    records: list[dict] = []
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        if not line.strip():
            raise ValueError(
                f"{path}:{line_number}: blank campaign selection-skip record"
            )
        try:
            record = json.loads(
                line,
                object_pairs_hook=_campaign_json_object,
                parse_constant=_reject_campaign_json_constant,
            )
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"{path}:{line_number}: invalid campaign selection-skip JSON: "
                f"{exc.msg}"
            ) from exc
        except ValueError as exc:
            raise ValueError(
                f"{path}:{line_number}: invalid campaign selection-skip JSON: "
                f"{exc}"
            ) from exc
        if _contains_non_finite_json_number(record):
            raise ValueError(
                f"{path}:{line_number}: campaign selection-skip contains a "
                "non-finite JSON number"
            )
        if not isinstance(record, dict):
            raise ValueError(
                f"{path}:{line_number}: campaign selection-skip is not an object"
            )
        expected_fields = {"claim_id", "reason", "detail", "recorded_at"}
        if set(record) != expected_fields:
            missing = sorted(expected_fields - set(record))
            unexpected = sorted(set(record) - expected_fields)
            raise ValueError(
                f"{path}:{line_number}: invalid campaign selection-skip fields "
                f"(missing={missing}, unexpected={unexpected})"
            )
        claim_id = record["claim_id"]
        reason = record["reason"]
        detail = record["detail"]
        if not isinstance(claim_id, str) or not claim_id:
            raise ValueError(
                f"{path}:{line_number}: campaign selection-skip has no claim_id"
            )
        try:
            ledger_io.shard_path(claim_id)
        except ValueError as exc:
            raise ValueError(
                f"{path}:{line_number}: campaign selection-skip claim_id is "
                f"not shard-safe: {claim_id!r}"
            ) from exc
        if reason not in SELECTION_SKIP_REASONS:
            raise ValueError(
                f"{path}:{line_number}: unrecognized campaign selection-skip "
                f"reason {reason!r}"
            )
        if not isinstance(detail, str) or not detail:
            raise ValueError(
                f"{path}:{line_number}: campaign selection-skip has no detail"
            )
        if selection_skip_reason(detail) != reason:
            raise ValueError(
                f"{path}:{line_number}: campaign selection-skip reason does "
                "not match its canonical detail"
            )
        recorded_at = record["recorded_at"]
        if not isinstance(recorded_at, str) or not re.fullmatch(
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}"
            r"(?:\.\d{6})?\+00:00",
            recorded_at,
        ):
            raise ValueError(
                f"{path}:{line_number}: campaign selection-skip recorded_at "
                "is not canonical UTC ISO-8601"
            )
        try:
            timestamp = datetime.fromisoformat(recorded_at)
        except ValueError as exc:
            raise ValueError(
                f"{path}:{line_number}: campaign selection-skip recorded_at "
                "is not ISO-8601"
            ) from exc
        if (
            timestamp.tzinfo is None
            or timestamp.utcoffset() != timezone.utc.utcoffset(timestamp)
        ):
            raise ValueError(
                f"{path}:{line_number}: campaign selection-skip recorded_at "
                "is not UTC"
            )
        records.append(record)
    return records


def persist_campaign_selection_skips(
    path: Path | None,
    skipped: list[str],
) -> None:
    """Append each distinct selector disposition without suppressing it."""
    if path is None or not skipped:
        return
    existing = {
        (record["claim_id"], record["reason"], record["detail"])
        for record in load_campaign_selection_skip_records(path)
    }
    pending = [selector_skip_record(line) for line in skipped]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for record in pending:
            key = (record["claim_id"], record["reason"], record["detail"])
            if key in existing:
                continue
            handle.write(json.dumps(record, sort_keys=True) + "\n")
            existing.add(key)


def load_campaign_quarantine(path: Path | None) -> set[str]:
    return {
        record["claim_id"]
        for record in load_campaign_exclusion_records(path)
    }


def persist_campaign_quarantine(
    path: Path | None,
    claim_ids: set[str],
    report: list[dict],
) -> None:
    persist_campaign_exclusions(
        path,
        claim_ids,
        reason=SCHEMA_QUARANTINE_RESULT,
        report=report,
        companion_results=SCHEMA_INVALID_RESULTS,
    )


def persist_campaign_exclusions(
    path: Path | None,
    claim_ids: set[str],
    *,
    reason: str,
    report: list[dict],
    companion_results: set[str],
) -> None:
    """Append one durable campaign-local exclusion record per claim.

    Exclusions are operational state, never audit verdicts.  The exact
    companion failures stay attached so a later repair campaign can route the
    row without reading prior scientific rationales.
    """
    if path is None or not claim_ids:
        return
    existing = {
        (record["claim_id"], record["reason"])
        for record in load_campaign_exclusion_records(path)
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for cid in sorted(
            candidate
            for candidate in claim_ids
            if (candidate, reason) not in existing
        ):
            failures = [
                item
                for item in report
                if item.get("cid") == cid
                and item.get("result") in companion_results
            ]
            handle.write(
                json.dumps(
                    {
                        "claim_id": cid,
                        "reason": reason,
                        "failures": failures,
                        "recorded_at": datetime.now(timezone.utc).isoformat(),
                    },
                    sort_keys=True,
                )
                + "\n"
            )


def persist_compute_required_skips(
    path: Path | None,
    claim_ids: set[str],
    report: list[dict],
) -> None:
    persist_campaign_exclusions(
        path,
        claim_ids,
        reason=COMPUTE_QUARANTINE_RESULT,
        report=report,
        companion_results={"compute_required"},
    )


def persist_claim_transaction_quarantines(
    path: Path | None,
    claim_ids: set[str],
    report: list[dict],
) -> None:
    persist_campaign_exclusions(
        path,
        claim_ids,
        reason=CLAIM_TRANSACTION_QUARANTINE_RESULT,
        report=report,
        companion_results={
            "apply_or_gate_failed",
            CLAIM_TRANSACTION_QUARANTINE_RESULT,
        },
    )


def _latest_invalidation_reason(row: dict) -> str:
    for archived in reversed(row.get("previous_audits") or []):
        if not isinstance(archived, dict):
            continue
        reason = str(archived.get("invalidation_reason") or "").strip()
        if reason:
            return reason
    return "pipeline_reset_to_unaudited_after_applied_verdict"


def blocked_row_reentries(
    selected_rows: list[dict],
    current_rows: dict[str, dict],
    report: list[dict],
) -> dict[str, str]:
    """Find applied verdicts that the pipeline made immediately selectable.

    The inner batch already skips every attempted row for its own lifetime.
    This detects the narrower cross-process failure mode: an accepted verdict
    was committed, but pipeline invalidation reset the same unchanged row to
    ``unaudited`` and the canonical selector would choose it again.  Such a row
    cannot make further scientific progress inside the same campaign.
    """
    applied = {
        item.get("cid")
        for item in report
        if item.get("result") in SUCCESS_RESULTS - {"compute_required"}
        and item.get("commit")
    }
    reentries: dict[str, str] = {}
    for selected in selected_rows:
        cid = selected["claim_id"]
        row = current_rows.get(cid) or {}
        if cid not in applied or row.get("audit_status") != "unaudited":
            continue
        targets, _ = compute_targets({cid}, current_rows)
        if not any(target.get("claim_id") == cid for target in targets):
            continue
        reason = _latest_invalidation_reason(row)
        reentries[cid] = reason
        report.append(
            {
                "cid": cid,
                "result": BLOCKED_ROW_QUARANTINE_RESULT,
                "detail": (
                    f"{reason}; accepted verdict was reset to unaudited and "
                    "dep-ready, so the row is excluded for this campaign"
                ),
            }
        )
    return reentries


def persist_blocked_row_reentries(
    path: Path | None,
    reentries: dict[str, str],
) -> None:
    if path is None or not reentries:
        return
    existing = {
        (record["claim_id"], record["reason"])
        for record in load_campaign_exclusion_records(path)
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for cid in sorted(
            candidate
            for candidate in reentries
            if (candidate, BLOCKED_ROW_QUARANTINE_RESULT) not in existing
        ):
            handle.write(
                json.dumps(
                    {
                        "claim_id": cid,
                        "reason": BLOCKED_ROW_QUARANTINE_RESULT,
                        "invalidation_reason": reentries[cid],
                        "recorded_at": datetime.now(timezone.utc).isoformat(),
                    },
                    sort_keys=True,
                )
                + "\n"
            )


def apply_serialized(
    jobs: list[dict],
    report: list[dict],
    retries: int = 3,
) -> tuple[bool, set[str], set[str], list[dict]]:
    deliveries: dict[tuple[str, int], tuple[dict, dict]] = {}
    invalid_claims: set[str] = set()
    compute_skips: set[str] = set()
    invalid_results: dict[str, list[dict]] = {}
    science_handoffs: dict[str, dict] = {}
    for job in sorted(jobs, key=lambda item: (item["cid"], item["pass"])):
        envelope, result = finalize_worker(job)
        if envelope is None:
            report.append(result)
            if result["result"] == "compute_required":
                compute_skips.add(job["cid"])
            else:
                invalid_claims.add(job["cid"])
                invalid_results.setdefault(job["cid"], []).append(result)
            continue
        deliveries[(job["cid"], job["pass"])] = (job, envelope)

    schema_invalid_claims = {
        cid
        for cid, failures in invalid_results.items()
        if failures
        and all(item.get("result") in SCHEMA_INVALID_RESULTS for item in failures)
    }
    validated_claims = {cid for cid, _ in deliveries}
    schema_quarantines = schema_invalid_claims - validated_claims
    invalid_claims.difference_update(validated_claims)

    for cid in compute_skips:
        for key in [key for key in deliveries if key[0] == cid]:
            deliveries.pop(key, None)

    fresh_critical = {
        job["cid"]
        for job in jobs
        if job["row"].get("criticality") == "critical"
        and passes_for_row(job["row"]) == [1, 2]
    }
    for cid in fresh_critical:
        available = {seat for delivery_cid, seat in deliveries if delivery_cid == cid}
        if cid in compute_skips:
            continue
        if not available:
            if cid not in schema_quarantines:
                invalid_claims.add(cid)
                report.append({
                    "cid": cid,
                    "result": "critical_peer_delivery_missing",
                    "detail": "validated seats=[]; required=[1, 2]",
                })
        elif available != {1, 2}:
            # Bank the single validated seat instead of discarding it. The
            # apply contract natively supports this: a lone clean seat lands
            # as audit_in_progress/awaiting_second and the next run resumes
            # with only the missing peer (passes_for_row -> [2]); a lone
            # non-clean seat lands in the governed repair queue. Discarding
            # validated xhigh work forced whole-pair reruns (grain wave 4,
            # 2026-07-13: seat 1 validated end-to-end and was thrown away
            # because seat 2 failed packet schema). The failed peer's
            # validation report stands on its own; it must not poison the
            # validated seat's apply.
            invalid_claims.discard(cid)
            report.append({
                "cid": cid,
                "result": "critical_peer_pending",
                "detail": (
                    f"validated seats={sorted(available)}; banking them and "
                    "preserving the incomplete pair signal"
                ),
            })

    for cid in sorted(schema_invalid_claims):
        failures = invalid_results[cid]
        valid = [
            envelope["audit"].get("verdict")
            for (delivery_cid, _), (_, envelope) in deliveries.items()
            if delivery_cid == cid
        ]
        if cid in schema_quarantines:
            result = SCHEMA_QUARANTINE_RESULT
            disposition = "campaign-scoped quarantine after bounded schema repair"
        elif cid in fresh_critical and valid and all(
            verdict == "audited_clean" for verdict in valid
        ):
            result = SCHEMA_DEFERRED_RESULT
            disposition = (
                "validated clean seat banked; missing peer remains eligible in "
                "the next top-level batch cycle"
            )
        else:
            result = SCHEMA_SUPERSEDED_RESULT
            disposition = "validated delivery superseded the malformed attempt"
        report.append({
            "cid": cid,
            "result": result,
            "detail": (
                f"{disposition}; "
                + "; ".join(
                    f"p{item.get('pass', '?')}={item.get('detail') or item.get('result')}"
                    for item in failures
                )
            ),
        })

    for cid in sorted({delivery_cid for delivery_cid, _ in deliveries}):
        if cid in invalid_claims:
            continue
        claim_deliveries = [
            deliveries[key]
            for key in sorted(deliveries)
            if key[0] == cid
        ]
        ok, results = apply_claim_serialized(claim_deliveries, retries)
        report.extend(results)
        if not ok:
            # apply_claim_serialized marks an apply/gate rejection claim-local
            # only after reset_to_origin_main proves both a clean worktree and
            # exact HEAD == origin/main synchronization. Once that explicit
            # rollback proof is present, quarantine the row for this campaign
            # and keep draining unrelated science.
            # Sync, reset, commit, and push failures remain global/uncertain
            # and still stop the batch.
            claim_local = (
                bool(results)
                and all(
                    item.get("result") == "apply_or_gate_failed"
                    and item.get("rollback_verified") is True
                    for item in results
                )
            )
            if claim_local:
                report.append({
                    "cid": cid,
                    "result": CLAIM_TRANSACTION_QUARANTINE_RESULT,
                    "detail": (
                        "apply/pipeline/lint transaction failed after validated "
                        "delivery; rollback to synchronized origin/main was "
                        "verified, so this claim is excluded for the campaign"
                    ),
                })
                continue
            return (
                False,
                compute_skips,
                schema_quarantines,
                list(science_handoffs.values()),
            )
        for job, envelope in claim_deliveries:
            handoff = science_fix_handoff(job, envelope)
            if handoff is not None:
                science_handoffs[job["cid"]] = handoff
    hard_invalid_claims = invalid_claims - schema_quarantines
    return (
        not hard_invalid_claims,
        compute_skips,
        schema_quarantines,
        list(science_handoffs.values()),
    )


def selected_batch(targets: list[dict], max_workers: int) -> list[dict]:
    selected: list[dict] = []
    used = 0
    for row in targets:
        seats = len(passes_for_row(row))
        if seats > max_workers:
            continue
        if used + seats > max_workers:
            continue
        selected.append(row)
        used += seats
    return selected


def scope_for_args(args: argparse.Namespace, rows: dict[str, dict]) -> set[str]:
    if args.lane:
        config = json.loads((DATA / "lane_certification_config.json").read_text(encoding="utf-8"))
        roots: list[str] = []
        for lane in config.get("lanes", []):
            if lane.get("lane") != args.lane:
                continue
            configured_roots = lane.get("roots")
            if isinstance(configured_roots, list):
                roots.extend(
                    root for root in configured_roots
                    if isinstance(root, str) and root
                )
            elif isinstance(lane.get("root"), str) and lane["root"]:
                roots.append(lane["root"])
        if not roots:
            raise ValueError(f"unknown lane {args.lane!r}")
        scope: set[str] = set()
        for root in roots:
            scope.update(lane_closure(root, rows))
        return scope
    return {claim.strip() for claim in args.claims.split(",") if claim.strip()}


def main() -> int:
    drain_lock = None

    def finish(code: int) -> int:
        nonlocal drain_lock
        if drain_lock is not None:
            drain_lock.close()
            drain_lock = None
        return code

    parser = argparse.ArgumentParser(description="Parallel development-tier audit drainer")
    scope_group = parser.add_mutually_exclusive_group(required=True)
    scope_group.add_argument("--lane", help="lane name from lane_certification_config.json")
    scope_group.add_argument("--claims", help="comma-separated claim ids")
    parser.add_argument(
        "--retarget-conditionals",
        action="store_true",
        help=(
            "with --claims only: re-audit named rows even though their "
            "sources and dependency statuses are unchanged since their last "
            "audited_conditional. Use when the remedy for the conditional "
            "was an environment change the repair-wait guard cannot see "
            "(gate/template calibration, packet-policy revision)."
        ),
    )
    parser.add_argument("--max-workers", type=int, default=6)
    parser.add_argument("--rounds", type=int, default=6)
    parser.add_argument("--stall-minutes", type=int, default=45)
    parser.add_argument("--runner-timeout-sec", type=int, default=120)
    parser.add_argument("--push-retries", type=int, default=3)
    parser.add_argument(
        "--campaign-quarantine-file",
        type=Path,
        default=None,
        help=(
            "JSONL file shared by one top-level campaign; exhausted "
            "schema-invalid claims and post-verdict blocked-row reentries are "
            "skipped for the rest of that campaign"
        ),
    )
    parser.add_argument(
        "--campaign-selection-skip-file",
        type=Path,
        default=None,
        help=(
            "append-only JSONL inventory of selector skips for repair routing; "
            "unlike quarantine state, these records never suppress selection"
        ),
    )
    parser.add_argument(
        "--dispatch-science-fixes",
        action="store_true",
        help=(
            "launch PR-producing repair workers for complete validated "
            "non-clean verdicts; use only when source repair was explicitly requested"
        ),
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    PROGRESS["dry_run"] = bool(args.dry_run)
    if not args.dry_run:
        drain_lock = acquire_exclusive_drain_lock("orchestrate_audit_batch")
        if drain_lock is None:
            return finish(3)
    if (
        args.max_workers < 1
        or args.rounds < 1
        or args.stall_minutes < 1
        or args.runner_timeout_sec < 1
        or args.push_retries < 1
    ):
        parser.error("worker, round, stall, runner-timeout, and retry limits must be positive")
    if args.retarget_conditionals and not args.claims:
        parser.error("--retarget-conditionals requires an explicit --claims list")
    retarget = frozenset(
        cid.strip() for cid in (args.claims or "").split(",") if cid.strip()
    ) if args.retarget_conditionals else frozenset()

    if not args.dry_run:
        error = clean_main_error()
        if error:
            print(f"refusing to run: {error}. Use a dedicated clean main checkout.")
            return finish(2)

    workdir = Path(
        os.environ.get("AUDIT_BATCH_WORKDIR")
        or f"/tmp/audit_batch_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}_{uuid.uuid4().hex[:8]}"
    )
    report: list[dict] = []
    PROGRESS["report"] = report
    try:
        session_skipped = load_campaign_quarantine(
            args.campaign_quarantine_file
        )
        load_campaign_selection_skip_records(
            args.campaign_selection_skip_file
        )
    except (OSError, ValueError) as exc:
        print(f"refusing to run with invalid campaign state: {exc}")
        return finish(2)
    science_handoffs: dict[str, dict] = {}
    if not args.dry_run:
        try:
            workdir.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print(
                f"refusing to run: workdir {workdir} already exists. "
                "Each run requires a fresh workdir; remove it or point "
                "AUDIT_BATCH_WORKDIR at a new path."
            )
            return finish(2)

    if not args.dry_run and not (DATA / "citation_graph.json").exists():
        print("derived audit caches missing (fresh clone); running the pipeline once")
        bootstrap = sh(["bash", str(SCRIPTS / "run_pipeline.sh")], timeout=1800)
        if bootstrap.returncode != 0:
            print(f"pipeline bootstrap failed: {(bootstrap.stderr or bootstrap.stdout)[-300:]}")
            return finish(2)

    for round_no in range(1, args.rounds + 1):
        rows = load_rows()
        try:
            scope = scope_for_args(args, rows)
        except ValueError as exc:
            print(str(exc))
            return finish(2)
        existing_disagreements = sorted(
            cid
            for cid in scope
            if (rows.get(cid, {}).get("cross_confirmation") or {}).get("status")
            in {"disagreement", "three_way_disagreement", "disagreement_irresolvable"}
        )
        for cid in existing_disagreements:
            if cid not in session_skipped:
                report.append({"cid": cid, "result": "judicial_panel_required"})
                session_skipped.add(cid)
        scope.difference_update(session_skipped)
        targets, skipped = compute_targets(scope, rows, retarget=retarget)
        print(f"== round {round_no}: {len(targets)} dep-ready targets, {len(skipped)} skipped")
        PROGRESS["round_targets"] = len(targets)
        maybe_progress_summary(force=(round_no == 1))
        if round_no == 1 and not args.dry_run:
            start_progress_ticker()
        for line in skipped:
            print(f"   skip: {line}")
        if not args.dry_run:
            try:
                persist_campaign_selection_skips(
                    args.campaign_selection_skip_file,
                    skipped,
                )
            except (OSError, ValueError) as exc:
                print(
                    "refusing to continue with invalid campaign selection "
                    f"state: {exc}"
                )
                return finish(2)
        missing = [line for line in skipped if line.endswith("missing ledger row")]
        if args.claims and missing:
            return finish(2)
        if not targets:
            break
        batch = selected_batch(targets, args.max_workers)
        if not batch:
            print("no target fits the configured worker limit (critical rows require two seats)")
            return finish(2)
        if args.dry_run:
            for row in batch:
                print(f"   would audit: {row['claim_id']} (passes={len(passes_for_row(row))})")
            deferred = len(targets) - len(batch)
            if deferred:
                print(f"   deferred by worker limit: {deferred}")
            break
        jobs: list[dict] = []
        launch_blocked = False
        try:
            for row in batch:
                for pass_no in passes_for_row(row):
                    try:
                        jobs.append(
                            launch_worker(
                                row, rows, pass_no, workdir,
                                args.runner_timeout_sec, round_no,
                            )
                        )
                    except ValueError as exc:
                        launch_blocked = True
                        report.append({
                            "cid": row["claim_id"],
                            "pass": pass_no,
                            "result": "prompt_transport_blocked",
                            "detail": str(exc),
                        })
                    except Exception as exc:
                        launch_blocked = True
                        report.append({
                            "cid": row["claim_id"],
                            "pass": pass_no,
                            "result": "worker_launch_failed",
                            "detail": f"{type(exc).__name__}: {exc}",
                        })
        except BaseException:
            terminate_workers(jobs)
            raise
        if not jobs:
            break
        print(
            f"   launched {len(jobs)} detached workers; streaming complete "
            f"claims to one committer (stall {args.stall_minutes}m)"
        )
        compute_skips: set[str] = set()
        schema_quarantines: set[str] = set()
        round_science_handoffs_by_claim: dict[str, dict] = {}

        def apply_ready_claim(claim_jobs: list[dict]) -> bool:
            ok, skipped, quarantined, handoffs = apply_serialized(
                claim_jobs, report, args.push_retries
            )
            compute_skips.update(skipped)
            schema_quarantines.update(quarantined)
            round_science_handoffs_by_claim.update(
                {row["claim_id"]: row for row in handoffs}
            )
            return ok

        streamed = wait_workers(
            jobs,
            args.stall_minutes,
            on_claim_ready=apply_ready_claim,
        )
        if streamed is True:
            applied_ok = True
            round_science_handoffs = list(
                round_science_handoffs_by_claim.values()
            )
        elif streamed is False:
            applied_ok = False
            round_science_handoffs = list(
                round_science_handoffs_by_claim.values()
            )
        else:
            # Compatibility for focused tests/mocks that replace the legacy
            # two-argument waiter. Production wait_workers always returns an
            # exact bool when a streaming callback is supplied.
            (
                applied_ok,
                compute_skips,
                schema_quarantines,
                round_science_handoffs,
            ) = apply_serialized(jobs, report, args.push_retries)
        session_skipped.update(compute_skips)
        session_skipped.update(schema_quarantines)
        transaction_quarantines = {
            item["cid"]
            for item in report
            if item.get("result") == CLAIM_TRANSACTION_QUARANTINE_RESULT
            and isinstance(item.get("cid"), str)
        }
        session_skipped.update(transaction_quarantines)
        persist_campaign_quarantine(
            args.campaign_quarantine_file,
            schema_quarantines,
            report,
        )
        persist_compute_required_skips(
            args.campaign_quarantine_file,
            compute_skips,
            report,
        )
        persist_claim_transaction_quarantines(
            args.campaign_quarantine_file,
            transaction_quarantines,
            report,
        )
        science_handoffs.update(
            {row["claim_id"]: row for row in round_science_handoffs}
        )
        # One audit attempt per claim per run. A non-terminal verdict
        # (audited_conditional) re-enters the ledger as unaudited repair-queue
        # work immediately, so without this a conditional row is re-targeted
        # every remaining round and burns seats re-auditing an unchanged
        # claim toward the same outcome. Repair, not repetition, moves it.
        session_skipped.update(row["claim_id"] for row in batch)
        current_rows = load_rows()
        reentries = blocked_row_reentries(batch, current_rows, report)
        session_skipped.update(reentries)
        persist_blocked_row_reentries(args.campaign_quarantine_file, reentries)
        disagreements = append_judicial_handoffs(batch, current_rows, report)
        (workdir / "report.jsonl").write_text(
            "".join(json.dumps(item, sort_keys=True) + "\n" for item in report),
            encoding="utf-8",
        )
        if disagreements or not applied_ok or launch_blocked:
            break

    judicial_claims = {
        item.get("cid")
        for item in report
        if item.get("result") == "judicial_panel_required"
    }
    repair_rows = [
        row
        for cid, row in sorted(science_handoffs.items())
        if cid not in judicial_claims
    ]
    if repair_rows and not args.dry_run and args.dispatch_science_fixes:
        try:
            launched = launch_science_fix_worker(repair_rows, workdir)
            if launched is None:
                raise ValueError("no unique science-fix handoff rows")
            pid, handoff_path, log_path = launched
            for row in repair_rows:
                report.append({
                    "cid": row["claim_id"],
                    "result": "science_fix_dispatched",
                    "detail": (
                        f"pid={pid} handoff={handoff_path} log={log_path}"
                    ),
                })
        except (OSError, ValueError) as exc:
            for row in repair_rows:
                report.append({
                    "cid": row["claim_id"],
                    "result": "science_fix_dispatch_failed",
                    "detail": f"{type(exc).__name__}: {exc}",
                })

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
    blocked = report_has_hard_blocker(report)
    return finish(1 if blocked else 0)


def report_has_hard_blocker(report: list[dict]) -> bool:
    """Return true only for outcomes that cannot be resumed canonically.

    A cross-seat disagreement is not a failed audit round. It is an explicit
    handoff to ``orchestrate_judicial_panel.py``. The top-level audit-loop
    orchestrator consumes that handoff immediately and then resumes the same
    lane, so returning nonzero here would incorrectly collapse a normal
    control-flow edge into a campaign stop.
    """
    accepted = (
        SUCCESS_RESULTS
        | RESUMABLE_HANDOFF_RESULTS
        | SCIENCE_FIX_RESULTS
        | SCHEMA_RECOVERY_RESULTS
        | CAMPAIGN_EXCLUSION_RESULTS
    )
    recovered = {
        item.get("cid")
        for item in report
        if item.get("result") in SCHEMA_RECOVERY_RESULTS
    }
    transaction_quarantined = {
        item.get("cid")
        for item in report
        if item.get("result") == CLAIM_TRANSACTION_QUARANTINE_RESULT
    }
    quarantine_companions = SCHEMA_INVALID_RESULTS | {"critical_peer_pending"}
    return any(
        item.get("result") not in accepted
        and not (
            item.get("cid") in recovered
            and item.get("result") in quarantine_companions
        )
        and not (
            item.get("cid") in transaction_quarantined
            and item.get("result") == "apply_or_gate_failed"
        )
        for item in report
    )


def append_judicial_handoffs(
    selected_rows: list[dict], current_rows: dict[str, dict], report: list[dict]
) -> list[str]:
    """Record every disagreement that became panel-eligible in this batch."""
    existing = {
        item.get("cid")
        for item in report
        if item.get("result") == "judicial_panel_required"
    }
    disagreements = [
        row["claim_id"]
        for row in selected_rows
        if (current_rows.get(row["claim_id"], {}).get("cross_confirmation") or {}).get(
            "status"
        )
        in {"disagreement", "three_way_disagreement", "disagreement_irresolvable"}
    ]
    for cid in disagreements:
        if cid not in existing:
            report.append({"cid": cid, "result": "judicial_panel_required"})
    return disagreements


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    finally:
        # Forced final summary on EVERY exit path (normal completion, early
        # returns, exceptions) except dry-run and pre-baseline aborts.
        if PROGRESS.get("t0") is not None and not PROGRESS.get("dry_run"):
            maybe_progress_summary(force=True)
