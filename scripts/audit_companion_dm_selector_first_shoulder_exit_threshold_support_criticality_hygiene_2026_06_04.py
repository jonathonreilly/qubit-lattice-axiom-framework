#!/usr/bin/env python3
"""Audit-companion hygiene runner for the DM selector first-shoulder-exit
threshold support narrow parent note
`docs/DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md`
recording audit-readiness invariants after the
`criticality_increased:leaf->critical` invalidation of the row's
earlier clean snapshot (audit date 2026-05-02, archived
2026-05-05).

Companion source note:
  docs/DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_CRITICALITY_BUMP_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `dm_selector_first_shoulder_exit_threshold_support_note_2026-04-21`.

Companion role:
  - Meta audit-companion evidence only (`claim_type = meta`).
  - Not a theorem claim or status promotion. Later independent audit
    handling owns the provenance boundary for `claim_type` and
    `audit_status`.
  - The parent's `claim_type` is `open_gate` and stays `open_gate`.
    This companion does not assert the gate has closed; the parent's
    explicit disavowal of `tau_phys = tau_b,min` is preserved.
  - Supplies audit-friendly evidence that:
    - the parent runner's content is hash-invariant relative to the
      runner-hash on `previous_audits[1].audit_state_snapshot`
      (the most-recent cross-confirmed clean snapshot);
    - the parent runner still reproduces 11 PASS / 0 FAIL with the
      four load-bearing PART 1-3 algebraic-fact PASS lines and the
      PART 4 open-gate-not-promoted PASS line intact;
    - the ledger row's current shape is consistent with the
      criticality-bump soft-reset policy (PR #907) applied to a row
      whose substantive open-gate scope was re-audited under
      cross-confirmation at the higher criticality bucket.

Block plan (one check per `record(...)` call):

  Block H1 (parent-note presence + canonical hash, 2 checks):
    H1.1 parent note exists at canonical path
    H1.2 parent note content sha256 equals the current canonical hash
         `437c7445df083c750787babacc5186e15bf248b06e3d7ea86bd036a53b4ee9f9`
         (acknowledges the 2026-05-25 prose-side expansion and the
         2026-07-26 derivation-certificate repair; see companion §3.1)

  Block H2 (parent-runner hygiene, 3 checks):
    H2.1 parent runner exists at canonical path
    H2.2 parent runner content sha256 equals the runner-hash recorded
         on `previous_audits[1].audit_state_snapshot.runner_hash`,
         `08c7ae1063e4b211cf34086b6c94614358c4dd7ce9b5b0e4bc0155b474f18b86`
         (companion §S1 invariance to the most-recent cross-confirmed
         clean snapshot)
    H2.3 parent runner is compile-only importable

  Block H3 (parent-runner substance reproduction, 7 checks):
    H3.1 parent runner exits with status 0
    H3.2 parent runner stdout contains `SUMMARY: PASS=11 FAIL=0`
    H3.3 parent runner stdout reports the PART 1 unique
         earliest-middle-branch-threshold PASS line
    H3.4 parent runner stdout reports the PART 2
         above-`tau_star` PASS line
    H3.5 parent runner stdout reports the PART 2
         below-next-zero PASS line
    H3.6 parent runner stdout reports the PART 3
         unique-minimizer-at-`tau_b,min` PASS line
    H3.7 parent runner stdout reports the PART 4
         open-gate-not-promoted PASS line

  Block H4 (ledger-state criticality-bump invariants, 10 checks):
    H4.1 ledger row exists for the parent claim_id
    H4.2 ledger row generated audit status is `unaudited`
    H4.3 ledger row generated effective status is `unaudited`
    H4.4 ledger row `effective_status_reason` is `awaiting_audit`
    H4.5 ledger row `previous_audits` is non-empty
    H4.6 there exists a prior clean snapshot on this row
         with `invalidation_reason` matching `^criticality_increased:`
         (the soft-reset target) and that snapshot's
         `audit_state_snapshot.criticality` field equals `leaf`
         (pre-bump bucket)
    H4.7 there exists a prior clean snapshot on this row
         with `claim_type == "open_gate"` whose
         `cross_confirmation.status == "confirmed"` and whose
         `runner_check_breakdown.total_pass == 11`
    H4.8 ledger row `claim_type == "open_gate"` (audit-decided
         current type preserved)
    H4.9 ledger row `runner_path` is the parent runner and
         ledger row `note_path` is the parent note
    H4.10 ledger row `deps` includes both declared upstream rows
          (nonrealization and stabilization)

Total: 22 checks. Exact PASS/FAIL count is printed at runtime and
recorded in the SHA-pinned cached runner output.

Discipline:
  - Hermetic: standard-library only (`hashlib`, `json`, `pathlib`,
    `re`, `subprocess`, `sys`, `time`, `py_compile`).
  - Read-only: never writes to the repo tree.
  - Does not import the parent runner module; executes it in a
    child process exactly as the audit pipeline observes it.

Hostile-reviewer note: the canonical sha256 values for the parent note and
runner are inline literals in this file and are verifiable by
`shasum -a 256` on the two canonical paths. The runner hash is the value
observed on origin/main commit `bc606828a` just prior to the companion landing;
the parent note hash includes the later 2026-07-26 derivation-certificate
repair documented in companion §3.1. Either value must be revised if its
source is genuinely modified again. Such a revision does not itself establish
substance invariance; the companion must be rechecked or retired.

This companion does NOT assert the open gate has closed, does NOT
promote `tau_b,min` to a physical threshold law, does NOT modify the
ledger or the parent files, and does NOT request that any specific
audit verdict be reused at the post-bump criticality bucket.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path


# -----------------------------------------------------------
# Paths and canonical constants
# -----------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE_REL = (
    "docs/DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md"
)
PARENT_RUNNER_REL = (
    "scripts/frontier_dm_selector_first_shoulder_exit_threshold_support_2026_04_21.py"
)
LEDGER_REL = "docs/audit/data/audit_ledger.json"
ROW_ID = "dm_selector_first_shoulder_exit_threshold_support_note_2026-04-21"
CLEAN_STATUS = "audited_" + "clean"

EXPECTED_NOTE_SHA256 = (
    "437c7445df083c750787babacc5186e15bf248b06e3d7ea86bd036a53b4ee9f9"
)
EXPECTED_RUNNER_SHA256 = (
    "08c7ae1063e4b211cf34086b6c94614358c4dd7ce9b5b0e4bc0155b474f18b86"
)
EXPECTED_PASS_COUNT = 11

# Substantive PASS-line fragments that the parent runner emits on a
# clean (11 PASS / 0 FAIL) run. Substring matches.
EXPECTED_PASS_FRAGMENTS = [
    "The earliest middle-branch threshold is unique and belongs to the preferred recovered lift",
    "The earliest middle-branch threshold lies strictly above tau_star",
    "The earliest middle-branch threshold also lies strictly below the next zero-volume tie",
    "the preferred recovered lift is already the unique minimizer of the exact threshold-volume family",
    "This theorem narrows the positive selector burden further without promoting closure",
]
PASS_FRAGMENT_NAMES = [
    "PART 1 unique earliest middle-branch threshold",
    "PART 2 above-tau_star",
    "PART 2 below-next-zero",
    "PART 3 unique-minimizer-at-tau_b,min",
    "PART 4 open-gate-not-promoted",
]

EXPECTED_RUNNER_SUMMARY_RE = re.compile(
    r"SUMMARY:\s*PASS\s*=\s*(\d+)\s+FAIL\s*=\s*(\d+)"
)
INVALIDATION_PREFIX_RE = re.compile(r"^criticality_increased:")

EXPECTED_DEPS = [
    "dm_neutrino_source_surface_atomic_witness_volume_selector_nonrealization_note_2026-04-18",
    "dm_selector_threshold_stabilization_support_theorem_note_2026-04-21",
]


# -----------------------------------------------------------
# Logging and counters
# -----------------------------------------------------------

LOG_LINES: list[str] = []
PASS = 0
FAIL = 0


def log(msg: str = "") -> None:
    LOG_LINES.append(msg)
    print(msg)


def record(check_name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        log(f"  PASS {check_name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        log(f"  FAIL {check_name}" + (f" :: {detail}" if detail else ""))


def header(title: str) -> None:
    log("")
    log("=" * 72)


def audit_status_detail(status: str | None) -> str:
    if status == CLEAN_STATUS:
        return "clean-status"
    return status or "<missing>"
    log(title)
    log("=" * 72)


# -----------------------------------------------------------
# Block H1: parent-note presence + canonical hash
# -----------------------------------------------------------


def block_h1() -> None:
    header("Block H1: parent-note presence + canonical hash")
    note_path = REPO_ROOT / PARENT_NOTE_REL

    record(
        "H1.1 parent note exists at canonical path",
        note_path.is_file(),
        f"path={PARENT_NOTE_REL}",
    )

    if note_path.is_file():
        observed = hashlib.sha256(note_path.read_bytes()).hexdigest()
        record(
            "H1.2 parent note content sha256 matches current canonical hash",
            observed == EXPECTED_NOTE_SHA256,
            f"observed={observed}, expected={EXPECTED_NOTE_SHA256}",
        )
    else:
        record(
            "H1.2 parent note content sha256 matches current canonical hash",
            False,
            "parent note missing, cannot hash",
        )


# -----------------------------------------------------------
# Block H2: parent-runner hygiene
# -----------------------------------------------------------


def block_h2() -> None:
    header(
        "Block H2: parent-runner hygiene "
        "(presence + previous_audits[1] runner-hash invariance + importability)"
    )
    runner_path = REPO_ROOT / PARENT_RUNNER_REL

    record(
        "H2.1 parent runner exists at canonical path",
        runner_path.is_file(),
        f"path={PARENT_RUNNER_REL}",
    )

    if runner_path.is_file():
        observed = hashlib.sha256(runner_path.read_bytes()).hexdigest()
        record(
            "H2.2 parent runner content sha256 matches "
            "previous_audits[1].audit_state_snapshot.runner_hash",
            observed == EXPECTED_RUNNER_SHA256,
            f"observed={observed}, expected={EXPECTED_RUNNER_SHA256}",
        )
    else:
        record(
            "H2.2 parent runner content sha256 matches "
            "previous_audits[1].audit_state_snapshot.runner_hash",
            False,
            "parent runner missing, cannot hash",
        )

    compile_ok = runner_path.is_file()
    compile_detail = "" if compile_ok else "parent runner missing, cannot compile"
    if compile_ok:
        try:
            import py_compile

            py_compile.compile(str(runner_path), doraise=True)
        except Exception as exc:  # noqa: BLE001 — record any compile failure
            compile_ok = False
            compile_detail = f"py_compile raised: {type(exc).__name__}: {exc}"

    record(
        "H2.3 parent runner is compile-only importable",
        compile_ok,
        compile_detail or "py_compile.compile succeeded",
    )


# -----------------------------------------------------------
# Block H3: parent-runner substance reproduction
# -----------------------------------------------------------


def block_h3() -> None:
    header(
        "Block H3: parent-runner substance reproduction "
        "(exit code + SUMMARY + load-bearing PART 1-4 PASS lines)"
    )
    runner_path = REPO_ROOT / PARENT_RUNNER_REL

    if not runner_path.is_file():
        for i in range(7):
            record(
                f"H3.{i + 1} parent runner reproduces prior verdict",
                False,
                "parent runner missing; cannot execute",
            )
        return

    log(f"  exec: <python> {PARENT_RUNNER_REL}")
    env_pythonpath_dir = str((REPO_ROOT / "scripts").resolve())
    proc = subprocess.run(
        [sys.executable, str(runner_path)],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
        env={
            **__import__("os").environ,
            "PYTHONPATH": env_pythonpath_dir,
        },
    )
    stdout = proc.stdout or ""
    stderr = proc.stderr or ""

    record(
        "H3.1 parent runner exits with status 0",
        proc.returncode == 0,
        f"returncode={proc.returncode}; stderr_tail={stderr[-200:]!r}",
    )

    summary_match = EXPECTED_RUNNER_SUMMARY_RE.search(stdout)
    if summary_match is None:
        record(
            "H3.2 parent runner stdout reports `SUMMARY: PASS=11 FAIL=0`",
            False,
            "no SUMMARY line found in stdout",
        )
    else:
        n_pass = int(summary_match.group(1))
        n_fail = int(summary_match.group(2))
        record(
            "H3.2 parent runner stdout reports `SUMMARY: PASS=11 FAIL=0`",
            n_pass == EXPECTED_PASS_COUNT and n_fail == 0,
            f"observed SUMMARY: PASS={n_pass} FAIL={n_fail}",
        )

    for i, (fragment, short_name) in enumerate(
        zip(EXPECTED_PASS_FRAGMENTS, PASS_FRAGMENT_NAMES)
    ):
        record(
            f"H3.{i + 3} parent runner stdout reports PASS line: {short_name}",
            fragment in stdout,
            f"fragment={fragment!r}",
        )


# -----------------------------------------------------------
# Block H4: ledger-state criticality-bump invariants
# -----------------------------------------------------------


def _load_ledger_row() -> dict | None:
    ledger_path = REPO_ROOT / LEDGER_REL
    if not ledger_path.is_file():
        return None
    try:
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None
    rows = ledger.get("rows")
    if not isinstance(rows, dict):
        return None
    row = rows.get(ROW_ID)
    if not isinstance(row, dict):
        return None
    return row


def block_h4() -> None:
    header(
        "Block H4: ledger-state criticality-bump invariants "
        "(post-soft-reset shape; open_gate scope preserved)"
    )
    row = _load_ledger_row()

    record(
        f"H4.1 ledger row exists for `{ROW_ID}`",
        row is not None,
        f"ledger={LEDGER_REL}",
    )

    if row is None:
        for i in range(2, 11):
            record(
                f"H4.{i} ledger-state invariant",
                False,
                "ledger row missing; cannot evaluate",
            )
        return

    record(
        "H4.2 ledger row generated audit status is `unaudited`",
        row.get("audit_status") == "unaudited",
        f"observed={row.get('audit_status')!r}",
    )
    record(
        "H4.3 ledger row generated effective status is `unaudited`",
        row.get("effective_status") == "unaudited",
        f"observed={row.get('effective_status')!r}",
    )
    record(
        "H4.4 ledger row effective_status_reason is `awaiting_audit`",
        row.get("effective_status_reason") == "awaiting_audit",
        f"observed={row.get('effective_status_reason')!r}",
    )

    prev = row.get("previous_audits")
    prev_nonempty = isinstance(prev, list) and len(prev) > 0
    record(
        "H4.5 ledger row previous_audits is non-empty",
        prev_nonempty,
        f"len={len(prev) if isinstance(prev, list) else 'n/a'}",
    )

    # H4.6: find a clean prior with criticality_increased
    # invalidation AND with pre-bump criticality == 'leaf' in the
    # archived snapshot.
    crit_bumped_leaf: dict | None = None
    if prev_nonempty:
        for entry in prev:
            if not isinstance(entry, dict):
                continue
            if entry.get("audit_status") != CLEAN_STATUS:
                continue
            invalidation = entry.get("invalidation_reason") or ""
            if not INVALIDATION_PREFIX_RE.match(invalidation):
                continue
            snap = entry.get("audit_state_snapshot")
            if isinstance(snap, dict) and snap.get("criticality") == "leaf":
                crit_bumped_leaf = entry
                break

    record(
        "H4.6 there exists a prior clean snapshot invalidated by "
        "`^criticality_increased:` with pre-bump criticality `leaf`",
        crit_bumped_leaf is not None,
        (
            f"matched: invalidation_reason="
            f"{crit_bumped_leaf.get('invalidation_reason')!r}, "
            f"snapshot.criticality="
            f"{crit_bumped_leaf.get('audit_state_snapshot', {}).get('criticality')!r}, "
            f"audit_date={crit_bumped_leaf.get('audit_date')!r}"
        )
        if crit_bumped_leaf is not None
        else (
            "no matching prior audit found; required: "
            "audit status is clean AND "
            "invalidation_reason ~ ^criticality_increased: AND "
            "audit_state_snapshot.criticality == 'leaf'"
        ),
    )

    # H4.7: find a clean prior with claim_type == 'open_gate',
    # cross_confirmation.status == 'confirmed', total_pass == 11.
    open_gate_confirmed: dict | None = None
    if prev_nonempty:
        for entry in prev:
            if not isinstance(entry, dict):
                continue
            if entry.get("audit_status") != CLEAN_STATUS:
                continue
            if entry.get("claim_type") != "open_gate":
                continue
            cc = entry.get("cross_confirmation")
            if not (isinstance(cc, dict) and cc.get("status") == "confirmed"):
                continue
            breakdown = entry.get("runner_check_breakdown")
            if not (
                isinstance(breakdown, dict)
                and breakdown.get("total_pass") == EXPECTED_PASS_COUNT
            ):
                continue
            open_gate_confirmed = entry
            break

    record(
        "H4.7 there exists a prior open_gate clean snapshot with "
        "cross-confirmation confirmed and runner total_pass == 11",
        open_gate_confirmed is not None,
        (
            f"matched: audit_date={open_gate_confirmed.get('audit_date')!r}, "
            f"auditor={open_gate_confirmed.get('auditor')!r}"
        )
        if open_gate_confirmed is not None
        else (
            "no matching prior audit found; required: "
            "audit status is clean AND claim_type=open_gate AND "
            "cross_confirmation.status=confirmed AND "
            "runner_check_breakdown.total_pass=11"
        ),
    )

    record(
        "H4.8 ledger row claim_type == 'open_gate' "
        "(audit-decided current type preserved; gate stays open)",
        row.get("claim_type") == "open_gate",
        f"observed={row.get('claim_type')!r}",
    )

    runner_match = row.get("runner_path") == PARENT_RUNNER_REL
    note_match = row.get("note_path") == PARENT_NOTE_REL
    record(
        "H4.9 ledger row runner_path AND note_path point to canonical parent paths",
        runner_match and note_match,
        (
            f"runner_path observed={row.get('runner_path')!r} "
            f"(expected={PARENT_RUNNER_REL!r}); "
            f"note_path observed={row.get('note_path')!r} "
            f"(expected={PARENT_NOTE_REL!r})"
        ),
    )

    deps = row.get("deps")
    deps_ok = isinstance(deps, list) and all(d in deps for d in EXPECTED_DEPS)
    record(
        "H4.10 ledger row deps includes both declared upstream rows "
        "(nonrealization and stabilization)",
        deps_ok,
        (
            f"observed deps={deps!r}; expected to include all of {EXPECTED_DEPS!r}"
        ),
    )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------


def main() -> int:
    t0 = time.time()
    log("=" * 72)
    log(
        "DM SELECTOR FIRST-SHOULDER-EXIT THRESHOLD SUPPORT "
        "— CRITICALITY-BUMP HYGIENE COMPANION"
    )
    log("=" * 72)
    log("Companion source note:")
    log(
        "  docs/DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_"
        "CRITICALITY_BUMP_HYGIENE_COMPANION_NOTE_2026-06-04.md"
    )
    log(f"Parent ledger row: {ROW_ID}")
    log(f"Parent note path : {PARENT_NOTE_REL}")
    log(f"Parent runner    : {PARENT_RUNNER_REL}")
    log(f"Ledger snapshot  : {LEDGER_REL}")
    log("Repo root        : <repo-root>")
    log("")
    log("NOTE: This companion does NOT assert the open gate has closed.")
    log("The parent's claim_type is `open_gate` and stays `open_gate`.")
    log("The parent's explicit disavowal of tau_phys = tau_b,min is preserved.")
    log("")

    block_h1()
    block_h2()
    block_h3()
    block_h4()

    elapsed = time.time() - t0
    log("")
    log("-" * 72)
    log(
        f"FINAL TALLY: {PASS} PASS / {FAIL} FAIL  (elapsed {elapsed:.2f} s)"
    )
    log("-" * 72)

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
