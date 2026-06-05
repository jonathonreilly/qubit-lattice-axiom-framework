#!/usr/bin/env python3
"""Audit-companion hygiene runner for the YT Schur stability-gap narrow
parent note `docs/YT_SCHUR_STABILITY_GAP_NOTE.md` recording
audit-readiness invariants after the
`criticality_increased:medium->critical` invalidation of the prior
`audited_clean` snapshot of `yt_schur_stability_gap_note` (audit date
2026-05-01, archived 2026-05-04).

Companion source note:
  docs/YT_SCHUR_STABILITY_GAP_CRITICALITY_BUMP_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `yt_schur_stability_gap_note`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    `claim_type` and `audit_status` independently).
  - Provides audit-friendly evidence that the parent note's substance
    is unchanged since the prior `audited_clean` snapshot
    (note-hash + runner-hash invariance) and that the prior runner
    result reproduces on the current `origin/main` tree (exit code 0,
    4 PASS / 0 FAIL).
  - Provides audit-friendly evidence that the current ledger row
    state is consistent with a `criticality_increased:*` soft-reset
    invalidation as specified by PR #907 (criticality bump surfaces
    the bumped row for audit-lane follow-up without disturbing the
    archived snapshot content).

Block plan (one check per `record(...)` call):

  Block H1 (parent-note hygiene, 2 checks):
    H1.1 parent note exists at canonical path
    H1.2 parent note content hash matches expected sha256
         `8119a5c437c4a0c5ddcd4be4c786a34cec2b60ff39aded95df915ed3ad7e83fd`

  Block H2 (parent-runner hygiene, 3 checks):
    H2.1 parent runner exists at canonical path
    H2.2 parent runner content hash matches expected sha256
         `b9688ba88dd8dbb7297241ea3163cbd18caeec6f90e99041063ae6f7d7213662`
    H2.3 parent runner module is compile-only importable

  Block H3 (parent-runner substance reproduction, 6 checks):
    H3.1 parent runner exits with status 0
    H3.2 parent runner stdout contains `FINAL TALLY: 4 PASS / 0 FAIL`
    H3.3 parent runner stdout reports the "open stability basin"
         PASS line
    H3.4 parent runner stdout reports the "first escape ... beyond
         the unit branch budget radius" PASS line
    H3.5 parent runner stdout reports the "in-class operators remain
         well separated" PASS line
    H3.6 parent runner stdout reports the "nearest escape ... real
         response-class failure" PASS line

  Block H4 (ledger-state criticality-bump invariants, 13 checks):
    H4.1 ledger row exists for `yt_schur_stability_gap_note`
    H4.2 ledger row audit-status field surfaces the row as unaudited
    H4.3 ledger row effective-status field surfaces the row as unaudited
    H4.4 ledger row effective-status reason is `awaiting_audit`
    H4.5 ledger row `previous_audits` is non-empty
    H4.6 there exists a prior audit on this row with
         audit status `audited_clean` and
         `invalidation_reason` matching `^criticality_increased:`
         (the criticality-bump soft-reset target)
    H4.7 that prior clean snapshot has four runner PASS checks
         (matches the live runner result)
    H4.8 that prior `audited_clean` snapshot has
         `claim_type == "bounded_theorem"`
         (matches the current row class)
    H4.9 ledger row `claim_type == "bounded_theorem"`
    H4.10 ledger row `runner_path` is the parent runner
    H4.11 ledger row `note_path` is the parent note
    H4.12 ledger row `deps` includes
          `yt_exact_schur_normal_form_uniqueness_note`
    H4.13 most-recent prior audit on this row has four runner PASS checks
          (substance reproduces across both prior audits)

Total: 24 checks. Exact PASS/FAIL count is printed at runtime and
recorded in the SHA-pinned cached runner output.

Discipline:
  - Hermetic: standard-library only (`hashlib`, `json`, `pathlib`,
    `re`, `subprocess`, `sys`, `time`).
  - Read-only: never writes to the repo tree.
  - Does not import the parent runner module; executes it in a child
    process exactly as the audit pipeline observes it.

Hostile-reviewer note: the canonical sha256 values for the parent
note and runner are inline literals in this file. They were observed
on origin/main commit 704086250 ("fs-rotation: add record-invariance
companion") and are explicitly verifiable by `shasum -a 256` on the
two canonical paths. They will need updating only if the parent note
or runner is genuinely modified upstream — at which point the
"substance-unchanged" claim of this hygiene companion does not apply
and the companion should be revised or retired in line with the
auditor's preference.
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
PARENT_NOTE_REL = "docs/YT_SCHUR_STABILITY_GAP_NOTE.md"
PARENT_RUNNER_REL = "scripts/frontier_yt_schur_stability_gap.py"
LEDGER_REL = "docs/audit/data/audit_ledger.json"
ROW_ID = "yt_schur_stability_gap_note"

EXPECTED_NOTE_SHA256 = (
    "8119a5c437c4a0c5ddcd4be4c786a34cec2b60ff39aded95df915ed3ad7e83fd"
)
EXPECTED_RUNNER_SHA256 = (
    "b9688ba88dd8dbb7297241ea3163cbd18caeec6f90e99041063ae6f7d7213662"
)
EXPECTED_PASS_COUNT = 4

# Substantive PASS-line fragments that the parent runner emits on a
# clean (4 PASS / 0 FAIL) run. Substring matches.
EXPECTED_PASS_FRAGMENTS = [
    "PASS: the admissible Schur class occupies an open stability basin",
    "PASS: the first escape from the Schur normal-form class occurs beyond the unit branch budget radius",
    "PASS: in-class operators remain well separated from the first normal-form escape",
    "PASS: the nearest escape is marked by a real response-class failure",
]
PASS_FRAGMENT_NAMES = [
    "open stability basin",
    "first escape beyond unit branch budget",
    "in-class well-separated",
    "nearest escape is real response-class failure",
]

EXPECTED_RUNNER_TALLY_RE = re.compile(
    r"FINAL TALLY:\s*(\d+)\s*PASS\s*/\s*(\d+)\s*FAIL"
)
INVALIDATION_PREFIX_RE = re.compile(r"^criticality_increased:")


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
    log(title)
    log("=" * 72)


# -----------------------------------------------------------
# Block H1: parent-note hygiene
# -----------------------------------------------------------


def block_h1() -> None:
    header("Block H1: parent-note hygiene (presence + hash invariance)")
    note_path = REPO_ROOT / PARENT_NOTE_REL

    record(
        "H1.1 parent note exists at canonical path",
        note_path.is_file(),
        f"path={note_path}",
    )

    if note_path.is_file():
        observed = hashlib.sha256(note_path.read_bytes()).hexdigest()
        record(
            "H1.2 parent note content sha256 matches expected canonical hash",
            observed == EXPECTED_NOTE_SHA256,
            f"observed={observed}, expected={EXPECTED_NOTE_SHA256}",
        )
    else:
        record(
            "H1.2 parent note content sha256 matches expected canonical hash",
            False,
            "parent note missing, cannot hash",
        )


# -----------------------------------------------------------
# Block H2: parent-runner hygiene
# -----------------------------------------------------------


def block_h2() -> None:
    header(
        "Block H2: parent-runner hygiene (presence + hash invariance + importability)"
    )
    runner_path = REPO_ROOT / PARENT_RUNNER_REL

    record(
        "H2.1 parent runner exists at canonical path",
        runner_path.is_file(),
        f"path={runner_path}",
    )

    if runner_path.is_file():
        observed = hashlib.sha256(runner_path.read_bytes()).hexdigest()
        record(
            "H2.2 parent runner content sha256 matches expected canonical hash",
            observed == EXPECTED_RUNNER_SHA256,
            f"observed={observed}, expected={EXPECTED_RUNNER_SHA256}",
        )
    else:
        record(
            "H2.2 parent runner content sha256 matches expected canonical hash",
            False,
            "parent runner missing, cannot hash",
        )

    # Compile-only check (no side effects). Use py_compile to avoid
    # accidentally executing the parent runner here; the actual
    # execution is performed in Block H3 as the audit pipeline does.
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
        "Block H3: parent-runner substance reproduction (exit code + tally + PASS lines)"
    )
    runner_path = REPO_ROOT / PARENT_RUNNER_REL

    if not runner_path.is_file():
        for i in range(6):
            record(
                f"H3.{i + 1} parent runner reproduces prior verdict",
                False,
                "parent runner missing; cannot execute",
            )
        return

    log(f"  exec: {sys.executable} {runner_path}")
    proc = subprocess.run(
        [sys.executable, str(runner_path)],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )
    stdout = proc.stdout or ""
    stderr = proc.stderr or ""

    record(
        "H3.1 parent runner exits with status 0",
        proc.returncode == 0,
        f"returncode={proc.returncode}; stderr_tail={stderr[-200:]!r}",
    )

    tally_match = EXPECTED_RUNNER_TALLY_RE.search(stdout)
    if tally_match is None:
        record(
            "H3.2 parent runner stdout reports `FINAL TALLY: 4 PASS / 0 FAIL`",
            False,
            "no FINAL TALLY line found in stdout",
        )
    else:
        n_pass = int(tally_match.group(1))
        n_fail = int(tally_match.group(2))
        record(
            "H3.2 parent runner stdout reports `FINAL TALLY: 4 PASS / 0 FAIL`",
            n_pass == EXPECTED_PASS_COUNT and n_fail == 0,
            f"observed FINAL TALLY: {n_pass} PASS / {n_fail} FAIL",
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
        "Block H4: ledger-state criticality-bump invariants (post-soft-reset shape)"
    )
    row = _load_ledger_row()

    record(
        f"H4.1 ledger row exists for `{ROW_ID}`",
        row is not None,
        f"ledger={LEDGER_REL}",
    )

    if row is None:
        # All remaining H4 checks fail with a single shared cause.
        for i in range(2, 13):
            record(
                f"H4.{i} ledger-state invariant",
                False,
                "ledger row missing; cannot evaluate",
            )
        return

    record(
        "H4.2 ledger row audit-status field surfaces the row as unaudited",
        row.get("audit_status") == "unaudited",
        f"observed={row.get('audit_status')!r}",
    )
    record(
        "H4.3 ledger row effective-status field surfaces the row as unaudited",
        row.get("effective_status") == "unaudited",
        f"observed={row.get('effective_status')!r}",
    )
    record(
        "H4.4 ledger row effective-status reason is awaiting_audit",
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

    # H4.6-H4.8 target the specific audited_clean snapshot that was
    # invalidated by criticality_increased; this snapshot may not be
    # the most recent prior audit on the row, since the row may have
    # been re-audited under audited_conditional after the criticality
    # bump invalidated the earlier audited_clean verdict.
    clean_critbumped: dict | None = None
    if prev_nonempty:
        for entry in prev:
            if not isinstance(entry, dict):
                continue
            invalidation = entry.get("invalidation_reason") or ""
            if (
                entry.get("audit_status") == "audited_clean"
                and INVALIDATION_PREFIX_RE.match(invalidation)
            ):
                clean_critbumped = entry
                break

    record(
        "H4.6 there exists a prior audited_clean snapshot invalidated by "
        "'^criticality_increased:'",
        clean_critbumped is not None,
        (
            f"matched criticality bump reason="
            f"{clean_critbumped.get('invalidation_reason')!r}, "
            f"audit_date={clean_critbumped.get('audit_date')!r}"
        )
        if clean_critbumped is not None
        else "no audited_clean prior audit with criticality_increased invalidation found",
    )

    if clean_critbumped is None:
        for i, suffix in enumerate(
            ("has four runner PASS checks", "has bounded-theorem claim type"),
            start=7,
        ):
            record(
                f"H4.{i} criticality-bumped audited_clean snapshot {suffix}",
                False,
                "no matching prior audit; cannot evaluate",
            )
    else:
        breakdown = clean_critbumped.get("runner_check_breakdown")
        total_pass = (
            breakdown.get("total_pass") if isinstance(breakdown, dict) else None
        )
        record(
            "H4.7 criticality-bumped audited_clean snapshot has "
            "four runner PASS checks",
            total_pass == EXPECTED_PASS_COUNT,
            f"observed={total_pass!r}",
        )
        record(
            "H4.8 criticality-bumped audited_clean snapshot has "
            "bounded-theorem claim type",
            clean_critbumped.get("claim_type") == "bounded_theorem",
            f"observed={clean_critbumped.get('claim_type')!r}",
        )

    record(
        "H4.9 ledger row class remains bounded_theorem",
        row.get("claim_type") == "bounded_theorem",
        f"observed={row.get('claim_type')!r}",
    )
    record(
        "H4.10 ledger row runner_path is the parent runner",
        row.get("runner_path") == PARENT_RUNNER_REL,
        f"observed={row.get('runner_path')!r}",
    )
    record(
        "H4.11 ledger row note_path is the parent note",
        row.get("note_path") == PARENT_NOTE_REL,
        f"observed={row.get('note_path')!r}",
    )
    deps = row.get("deps")
    has_dep = (
        isinstance(deps, list)
        and "yt_exact_schur_normal_form_uniqueness_note" in deps
    )
    record(
        "H4.12 ledger row deps includes `yt_exact_schur_normal_form_uniqueness_note`",
        has_dep,
        f"observed={deps!r}",
    )

    # H4.13: the most-recent prior audit (which may differ from the
    # criticality-bumped audited_clean snapshot) also reproduces the
    # same runner PASS count. This pins that substance reproduction
    # across both prior audits, independent of which one the audit
    # lane chooses to honor.
    if not prev_nonempty:
        record(
            "H4.13 most-recent prior audit has four runner PASS checks",
            False,
            "previous_audits empty or missing; cannot evaluate",
        )
    else:
        last = prev[-1]
        if not isinstance(last, dict):
            record(
                "H4.13 most-recent prior audit has four runner PASS checks",
                False,
                f"most-recent previous_audits entry not a dict: {type(last).__name__}",
            )
        else:
            breakdown = last.get("runner_check_breakdown")
            total_pass = (
                breakdown.get("total_pass") if isinstance(breakdown, dict) else None
            )
            record(
                "H4.13 most-recent prior audit has four runner PASS checks",
                total_pass == EXPECTED_PASS_COUNT,
                f"observed={total_pass!r}",
            )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------


def main() -> int:
    t0 = time.time()
    log("=" * 72)
    log("YT SCHUR STABILITY GAP — CRITICALITY-BUMP HYGIENE COMPANION")
    log("=" * 72)
    log("Companion source note:")
    log(
        "  docs/YT_SCHUR_STABILITY_GAP_CRITICALITY_BUMP_HYGIENE_COMPANION_NOTE_2026-06-04.md"
    )
    log(f"Parent ledger row: {ROW_ID}")
    log(f"Parent note path : {PARENT_NOTE_REL}")
    log(f"Parent runner    : {PARENT_RUNNER_REL}")
    log(f"Ledger snapshot  : {LEDGER_REL}")
    log(f"Repo root        : {REPO_ROOT}")
    log("")

    block_h1()
    block_h2()
    block_h3()
    block_h4()

    elapsed = time.time() - t0
    log("")
    log("-" * 72)
    log(f"FINAL TALLY: {PASS} PASS / {FAIL} FAIL  (elapsed {elapsed:.2f} s)")
    log("-" * 72)

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
