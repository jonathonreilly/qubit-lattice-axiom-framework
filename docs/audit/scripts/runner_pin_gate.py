#!/usr/bin/env python3
"""Runner-pin gate: a terminal verdict must bind the runner source it names.

A ledger row's `audit_state_snapshot` is what binds a verdict to the content
it was issued against. `invalidate_stale_audits.detect_invalidation` reopens a
row when the runner it names has moved, but it can only do that through two
snapshot fields:

  * `runner_hash` — sha256 of `row["runner_path"]` at audit time. The legacy
    comparator fires only when this is non-null (`blocker_fingerprint_v1`
    snapshots additionally pin `runner_path` and `runner_present`).
  * `helper_runner_hashes` — path -> sha256 for every transitive-import
    helper in `row["helper_runner_paths"]`. The comparator skips the whole
    helper channel when this key is absent.

A snapshot missing either field pins nothing on that channel: the runner can
be rewritten arbitrarily and the verdict never re-enters the queue. The writer
has recorded `runner_hash` since 2026-05-16 and `helper_runner_hashes` since
2026-07-15, so every row audited before those dates carries an unpinned
channel. This module is the single predicate both sides execute:

  * `apply_audit.snapshot_audit_state` calls `verdict_pin_problems` and
    refuses to write a terminal verdict whose snapshot leaves a named runner
    unbound (fail-loud, mirroring `FingerprintV1Invalid`).
  * `audit_lint` calls `classify_row` to report the pre-existing population
    against `runner_pin_baseline.json`.

The baseline is recorded once and is shrink-only. Its `*_at_baseline` shas
state repository content at the moment the debt was recorded — never what an
auditor saw. Re-pinning an old snapshot from current content would assert
exactly the thing the missing pin makes unknowable, so nothing here writes to
the ledger.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
BASELINE_PATH = Path(__file__).resolve().parent / "runner_pin_baseline.json"
BASELINE_SCHEMA = "runner_pin_baseline_v1"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
import runner_cache as rc  # noqa: E402

BLOCKER_FINGERPRINT_V1 = "blocker_fingerprint_v1"

TERMINAL_VERDICTS = {
    "audited_clean",
    "audited_renaming",
    "audited_conditional",
    "audited_decoration",
    "audited_failed",
    "audited_numerical_match",
}

# Verdicts whose snapshot receives the v1 blocker fingerprint. Only those
# snapshots pin `runner_path` / `runner_present`, so only they bind a runner
# that is ABSENT at audit time: the legacy comparator compares two hashes and
# skips whenever either side is null, so an absent->present runner under a
# legacy snapshot produces no invalidation at all (verified directly against
# `invalidate_stale_audits.detect_invalidation`). Must stay in sync with
# `apply_audit.FINGERPRINT_STAMP_VERDICTS`; `test_runner_pin_gate` asserts it.
PRESENCE_PINNED_VERDICTS = {"audited_conditional", "audited_failed"}

_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class RunnerPinIncomplete(ValueError):
    """A terminal verdict write would leave a named runner unpinned.

    Fails loudly for the same reason `FingerprintV1Invalid` does: a writer
    that drops the binding is a bug, and the resulting row is indistinguishable
    from a correctly pinned one until the runner silently moves under it.
    """


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and bool(_SHA256_RE.fullmatch(value))


def declared_runner_path(row: dict) -> str | None:
    path = row.get("runner_path")
    return path if isinstance(path, str) and path else None


def declared_helper_paths(row: dict) -> list[str]:
    return sorted({p for p in (row.get("helper_runner_paths") or []) if isinstance(p, str) and p})


def runner_exists(path: str | None) -> bool:
    return bool(path) and (REPO_ROOT / path).exists()


def current_sha256(path: str | None) -> str | None:
    if not path:
        return None
    return rc.runner_sha256(path)


# ---------------------------------------------------------------------------
# Snapshot generations.
#
# A snapshot is only in violation on a channel it was CAPABLE of pinning. A
# pre-2026-05-16 snapshot has no `runner_hash` key at all; treating that as the
# same defect as a modern writer emitting null would collapse "the field did
# not exist" into "the writer dropped it", and the two need different lanes:
# the first is recorded debt, the second is a live regression.
# ---------------------------------------------------------------------------


def snapshot_pins_runner_channel(snapshot: dict | None) -> bool:
    """True when the snapshot's writer was able to record `runner_hash`."""
    if not isinstance(snapshot, dict):
        return False
    return snapshot.get("schema") == BLOCKER_FINGERPRINT_V1 or "runner_hash" in snapshot


def snapshot_pins_helper_channel(snapshot: dict | None) -> bool:
    """True when the snapshot's writer was able to record helper hashes."""
    if not isinstance(snapshot, dict):
        return False
    return "helper_runner_hashes" in snapshot


def runner_unpinned(row: dict, snapshot: dict | None) -> bool:
    """The row names a primary runner that the snapshot does not bind."""
    if not declared_runner_path(row):
        return False
    if not isinstance(snapshot, dict):
        return True
    return not _is_sha256(snapshot.get("runner_hash"))


def helpers_unpinned(row: dict, snapshot: dict | None) -> bool:
    """The row declares helper runners the snapshot does not bind.

    A recorded map binds the channel even when its key set no longer matches
    the current import closure: `detect_invalidation` returns
    `helper_runner_paths_changed` on ANY key-set difference (including an
    empty recorded map against a non-empty closure), so the verdict is
    reopened. Only an absent or non-dict map makes the comparator skip the
    channel outright. Treating a key-set mismatch as "unpinned" would report a
    routine closure change — an import added to a helper, with no note edit —
    as a retained-grade writer regression and hard-fail every commit and
    pipeline run until an audit-lane re-audit, which is a false positive with
    no drain path.
    """
    helpers = declared_helper_paths(row)
    if not helpers:
        return False
    if not isinstance(snapshot, dict):
        return True
    return not isinstance(snapshot.get("helper_runner_hashes"), dict)


# ---------------------------------------------------------------------------
# Writer side.
# ---------------------------------------------------------------------------


def verdict_pin_problems(row: dict, snapshot: dict) -> list[str]:
    """Baseline problems for a terminal-verdict snapshot about to be written.

    Empty list means the snapshot binds every runner source the row names.
    Non-terminal writes are unconstrained: `unaudited` / `audit_in_progress`
    rows carry no verdict for a stale runner to invalidate.
    """
    verdict = row.get("audit_status")
    if verdict not in TERMINAL_VERDICTS:
        return []
    problems: list[str] = []

    path = declared_runner_path(row)
    if path:
        if "runner_hash" not in snapshot:
            problems.append("runner_hash:missing_key")
        elif not _is_sha256(snapshot.get("runner_hash")):
            # A runner absent from disk cannot be hashed. That is a legitimate
            # state only for a verdict whose snapshot carries the v1 blocker
            # fingerprint, because `runner_present` binds the absence itself
            # and a later absent->present move reopens the row. Every other
            # terminal verdict — clean, renaming, decoration, numerical_match —
            # would be recorded with a null hash that no comparator can ever
            # act on: the runner may appear, change, and change again with the
            # verdict standing. Refuse those rather than mint a permanently
            # unbindable row.
            if runner_exists(path):
                problems.append(f"runner_hash:required_sha256_for_present_runner:{path}")
            elif verdict not in PRESENCE_PINNED_VERDICTS:
                problems.append(
                    f"runner_hash:{verdict}_names_absent_runner_without_presence_pin:{path}"
                )

    helpers = declared_helper_paths(row)
    recorded = snapshot.get("helper_runner_hashes")
    if not isinstance(recorded, dict):
        if helpers:
            problems.append("helper_runner_hashes:missing_map")
    elif sorted(recorded) != helpers:
        missing = sorted(set(helpers) - set(recorded))
        extra = sorted(set(recorded) - set(helpers))
        if missing:
            problems.append(f"helper_runner_hashes:missing:{','.join(missing[:3])}")
        if extra:
            problems.append(f"helper_runner_hashes:unexpected:{','.join(extra[:3])}")
    else:
        for helper_path in helpers:
            if not _is_sha256(recorded.get(helper_path)) and runner_exists(helper_path):
                problems.append(
                    f"helper_runner_hashes:required_sha256_for_present_runner:{helper_path}"
                )
    return problems


# ---------------------------------------------------------------------------
# Baseline (shrink-only record of the pre-pin population).
# ---------------------------------------------------------------------------


def load_baseline(path: Path | None = None) -> dict:
    target = BASELINE_PATH if path is None else path
    if not target.exists():
        return {}
    data = json.loads(target.read_text(encoding="utf-8"))
    if data.get("schema") != BASELINE_SCHEMA:
        raise ValueError(
            f"{target} schema={data.get('schema')!r}, expected {BASELINE_SCHEMA!r}"
        )
    entries = data.get("entries")
    return entries if isinstance(entries, dict) else {}


def baseline_source_drift(
    entry: dict, row: dict, *, check_helper_membership: bool = False
) -> list[str]:
    """Runner sources that have moved away from their recorded baseline sha.

    `check_helper_membership` additionally reports helpers that have ENTERED
    or LEFT the row's import closure since the baseline. On an unpinned helper
    channel nothing watches membership — the recorded shas cover only the
    helpers that existed when the debt was recorded — so a helper added later
    is source the verdict has never been compared against.
    """
    drifted: list[str] = []
    path = entry.get("runner_path")
    if path and entry.get("runner_sha256_at_baseline") != current_sha256(path):
        drifted.append(path)
    recorded = entry.get("helper_runner_sha256_at_baseline")
    if isinstance(recorded, dict):
        for helper_path, sha in sorted(recorded.items()):
            if sha != current_sha256(helper_path):
                drifted.append(helper_path)
    if check_helper_membership:
        recorded_helpers = set(recorded or {})
        for helper_path in declared_helper_paths(row):
            if helper_path not in recorded_helpers and runner_exists(helper_path):
                drifted.append(helper_path)
    return drifted


# Classification labels consumed by audit_lint. `severity` is advisory: the
# caller applies the repo's retained-grade rule (a retained-grade row's
# integrity violation is a hard error; the same defect on a non-retained row
# is re-audit-pending and must not block strict lint).
PIN_OK = "pin_ok"
PIN_WRITER_REGRESSION = "writer_regression"
PIN_BASELINE_MISSING = "baseline_missing"
PIN_BASELINE_SOURCE_DRIFTED = "baseline_source_drifted"
PIN_BASELINE_NEW_DRIFT = "baseline_new_drift"
PIN_GRANDFATHERED = "grandfathered"


def classify_row(row: dict, baseline: dict) -> tuple[str, str] | None:
    """Classify one ledger row's runner-pin state.

    Returns `(label, detail)` or None when the row is fully pinned and absent
    from the baseline. Only terminal-verdict rows are classified: an unaudited
    row has no verdict to protect.

    A channel counts only when its runner is readable on disk. A pin cannot be
    demanded for source nobody can hash, and a row naming an absent runner is
    already refused at verdict-write time by `verdict_pin_problems` unless the
    verdict carries a v1 presence pin.
    """
    cid = row.get("claim_id")
    if row.get("audit_status") not in TERMINAL_VERDICTS:
        return None
    snapshot = row.get("audit_state_snapshot")
    primary = declared_runner_path(row)
    present_helpers = [p for p in declared_helper_paths(row) if runner_exists(p)]
    unpinned_runner = runner_unpinned(row, snapshot) and runner_exists(primary)
    unpinned_helpers = helpers_unpinned(row, snapshot) and bool(present_helpers)
    if not unpinned_runner and not unpinned_helpers:
        return None

    channels = []
    if unpinned_runner:
        channels.append(f"runner_path={primary}")
    if unpinned_helpers:
        channels.append(f"{len(present_helpers)} helper runners")
    detail = "; ".join(channels)

    # A writer that HAD the field and still left the channel unbound is a live
    # regression, not recorded debt — the baseline must not absorb it.
    writer_regression = (
        (unpinned_runner and snapshot_pins_runner_channel(snapshot))
        or (unpinned_helpers and snapshot_pins_helper_channel(snapshot))
    )
    if writer_regression:
        return (
            PIN_WRITER_REGRESSION,
            f"snapshot records the pin field but leaves it empty ({detail})",
        )

    entry = baseline.get(cid)
    if not isinstance(entry, dict):
        return (
            PIN_BASELINE_MISSING,
            f"pre-pin-shaped snapshot outside runner_pin_baseline.json ({detail})",
        )
    # Movement since the baseline is checked BEFORE the recorded-drift flag.
    # An entry already flagged `source_drifted_since_verdict` is the worst-off
    # population in the file; short-circuiting on the flag would make every
    # later move on those rows report as the old, softer finding forever, so
    # exactly the rows with known drift would be the only ones the ratchet
    # never protects.
    drifted = baseline_source_drift(
        entry, row, check_helper_membership=unpinned_helpers
    )
    if drifted:
        return (
            PIN_BASELINE_NEW_DRIFT,
            f"runner source moved or entered the closure since the baseline while "
            f"the verdict binds nothing: {', '.join(drifted[:3])}",
        )
    if entry.get("source_drifted_since_verdict"):
        evidence = entry.get("drift_evidence") or []
        return (
            PIN_BASELINE_SOURCE_DRIFTED,
            f"runner source already moved after the verdict and no pin caught it "
            f"({detail}; {len(evidence)} recorded commits) — re-audit candidate; "
            "nothing here queues it, and whether to spend audit capacity on it is "
            "an owner/audit-lane decision",
        )
    return (PIN_GRANDFATHERED, f"unpinned terminal verdict, source unchanged ({detail})")


def stale_baseline_entries(rows: dict, baseline: dict) -> dict[str, list[str]]:
    """Baseline claim ids that no longer qualify — the drain signal.

    `drained` are rows still in the ledger that have since been re-pinned or
    reset; each is an actionable one-line removal. `absent` are claim ids the
    ledger no longer carries at all; they are reported in aggregate so a
    partial ledger (a fixture, a sharded subset) cannot bury real findings.
    """
    drained: list[str] = []
    absent: list[str] = []
    for cid in sorted(baseline):
        row = rows.get(cid)
        if not isinstance(row, dict):
            absent.append(cid)
            continue
        if row.get("audit_status") not in TERMINAL_VERDICTS:
            drained.append(cid)
            continue
        snapshot = row.get("audit_state_snapshot")
        if not runner_unpinned(row, snapshot) and not helpers_unpinned(row, snapshot):
            drained.append(cid)
    return {"drained": drained, "absent": absent}
