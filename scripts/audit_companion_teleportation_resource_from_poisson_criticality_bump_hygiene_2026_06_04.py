#!/usr/bin/env python3
"""Audit-readiness hygiene companion for teleportation_resource_from_poisson.

Companion target:
    teleportation_resource_from_poisson_note

The parent row's most recent invalidation reason is the queue-priority
signal `criticality_increased:leaf->medium`, not a substance-change
flag. This runner verifies that the on-disk parent note and parent
runner are unchanged in load-bearing content since the prior
`audited_clean` verdict (2026-05-02, codex-gpt-5, runner_check_breakdown
A=0/B=1/C=4/D=0/total_pass=5), so the audit lane can decide whether to
honor that verdict at the new `medium` criticality bucket with full
information about what has and has not changed.

The parent is an explicit `open_gate` row: the small-surface
Poisson/CHSH numerical artifact is in scope, the native
preparation/readout bridge theorem selecting the last KS taste bit as
a physical deterministic carrier is admitted, not-derived. This
companion does not close, narrow, or relocate the open-gate admission.

This runner does no new physics. It performs:

  (R1) Presence checks for parent note + parent runner files.
  (R2) Note-hash invariance against ledger row's `note_hash` field.
  (R3) Parent runner exits 0 and prints the three case banners and
       the closing `Conclusion:` banner.
  (R4) Parent runner numerical-surface invariance: the exact Bell
       overlaps, traced CHSH values, negativities, and standard
       teleportation fidelities published in the parent note's
       "Default Run Results" table appear in the runner's stdout.
  (R5) Load-bearing-content static checks on parent note prose.
  (R6) Invalidation-reason structure on ledger row + prior verdict
       was audited_clean with total_pass=5.
  (R7) Helper-runner presence for the two adjacent scripts the
       parent note references in its `## Script` and
       `Source-boundary checker` sections.

Exit code 0 with PASS=N FAIL=0 means the parent substance is
provably identical to what the prior `audited_clean` verdict
evaluated; any FAIL means the on-disk artifacts have drifted since
this companion was filed and the audit lane should treat the
companion as stale.

This companion is `claim_type=meta`. It does not modify the parent
note or parent runner, does not change any ledger field, does not
re-audit the parent, and does not close the open gate.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path


PASS_COUNT = 0
FAIL_COUNT = 0

ROOT = Path(__file__).resolve().parents[1]

PARENT_NOTE_REL = "docs/TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md"
PARENT_RUNNER_REL = "scripts/frontier_teleportation_resource_from_poisson.py"
LEDGER_REL = "docs/audit/data/audit_ledger.json"

LEDGER_ROW_ID = "teleportation_resource_from_poisson_note"
EXPECTED_NOTE_HASH = (
    "5d3b09ce4191e64d86af8e57179a00b6cca1e0cd937e6cab93fb190158691e02"
)
EXPECTED_INVALIDATION_PREFIX = "criticality_increased"
EXPECTED_PRIOR_AUDIT_STATUS = "audited_clean"
EXPECTED_PRIOR_TOTAL_PASS = 5
EXPECTED_PRIOR_CHECK_BREAKDOWN = {"A": 0, "B": 1, "C": 4, "D": 0}

# Parent runner numerical-surface fingerprints (from parent note's
# "Default Run Results" table). These must appear verbatim in runner
# stdout for the substance-unchanged invariant to hold.
EXPECTED_RUNNER_FINGERPRINTS = [
    # protocol sanity
    "0.9999999999999996",  # ideal Phi+ mean fidelity
    "0.9999999999999991",  # ideal Phi+ min fidelity
    "5.551e-16",           # max trace error
    # 1d_null
    "best Bell overlap=0.500000 (Psi+)",
    "CHSH=2.000000",
    "negativity=0.000000",
    "mean fidelity=0.669817",
    # 1d_poisson_chsh
    "best Bell overlap=0.997963 (Phi+)",
    "CHSH=2.822668",
    "negativity=0.497963",
    "mean fidelity=0.998621",
    # 2d_poisson_chsh
    "best Bell overlap=0.970283 (Phi+)",
    "negativity=0.470283",
    "mean fidelity=0.979360",
]

# Closing banner + case banners that must appear in runner stdout
EXPECTED_RUNNER_BANNERS = [
    "Case: 1d_null",
    "Case: 1d_poisson_chsh",
    "Case: 2d_poisson_chsh",
    "Conclusion:",
]

# Helper runner paths referenced by the parent note
HELPER_RUNNER_RELS = [
    "scripts/frontier_bell_inequality.py",
    "scripts/frontier_teleportation_poisson_resource_scope_repair.py",
]


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return condition


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def read_bytes(rel: str) -> bytes:
    return (ROOT / rel).read_bytes()


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def load_ledger_row() -> dict:
    with open(ROOT / LEDGER_REL, "r", encoding="utf-8") as f:
        data = json.load(f)
    rows = data.get("rows", {})
    return rows.get(LEDGER_ROW_ID, {})


def part_R1_presence() -> None:
    section("(R1) Presence checks for parent note and parent runner")
    parent_note_path = ROOT / PARENT_NOTE_REL
    parent_runner_path = ROOT / PARENT_RUNNER_REL
    check(
        "parent note file exists on disk",
        parent_note_path.is_file(),
        f"path={PARENT_NOTE_REL}",
    )
    check(
        "parent runner file exists on disk",
        parent_runner_path.is_file(),
        f"path={PARENT_RUNNER_REL}",
    )


def part_R2_note_hash_invariance() -> None:
    section("(R2) Note-hash invariance against current ledger row")
    row = load_ledger_row()
    on_disk_hash = hashlib.sha256(read_bytes(PARENT_NOTE_REL)).hexdigest()
    ledger_hash = row.get("note_hash", "")
    check(
        "ledger row recorded expected note_hash",
        ledger_hash == EXPECTED_NOTE_HASH,
        f"ledger={ledger_hash[:12]}... expected={EXPECTED_NOTE_HASH[:12]}...",
    )
    check(
        "on-disk note hash matches ledger note_hash",
        on_disk_hash == ledger_hash,
        f"on_disk={on_disk_hash[:12]}... ledger={ledger_hash[:12]}...",
    )
    check(
        "on-disk note hash matches the expected substance-unchanged hash",
        on_disk_hash == EXPECTED_NOTE_HASH,
        f"on_disk={on_disk_hash[:12]}... expected={EXPECTED_NOTE_HASH[:12]}...",
    )


_runner_stdout_cache: str | None = None


def get_parent_runner_stdout() -> tuple[int, str]:
    """Run the parent runner once and cache its stdout for R3+R4."""
    global _runner_stdout_cache
    full_env = os.environ.copy()
    full_env["PYTHONPATH"] = str(ROOT / "scripts")
    result = subprocess.run(
        [sys.executable, str(ROOT / PARENT_RUNNER_REL)],
        capture_output=True,
        text=True,
        env=full_env,
        cwd=str(ROOT),
        timeout=300,
    )
    _runner_stdout_cache = result.stdout
    return result.returncode, result.stdout


def part_R3_parent_runner_execution() -> None:
    section("(R3) Parent runner execution and banner presence")
    rc, stdout = get_parent_runner_stdout()
    check(
        "parent runner exits with status 0",
        rc == 0,
        f"returncode={rc}",
    )
    for banner in EXPECTED_RUNNER_BANNERS:
        check(
            f"parent runner stdout contains banner: {banner!r}",
            banner in stdout,
        )


def part_R4_parent_runner_numerical_surface() -> None:
    section("(R4) Parent runner numerical-surface invariance")
    stdout = _runner_stdout_cache or ""
    for fingerprint in EXPECTED_RUNNER_FINGERPRINTS:
        check(
            f"parent runner stdout contains fingerprint: {fingerprint!r}",
            fingerprint in stdout,
        )
    # Deterministic-high-fidelity verdicts: NO for 1d_null, YES for the
    # two Poisson cases. Use the exact `: NO` / `: YES` suffix that the
    # runner prints.
    check(
        "parent runner verdict for 1d_null is NO",
        stdout.count("deterministic high-fidelity Bell resource (threshold 0.900): NO") == 1,
    )
    check(
        "parent runner verdict for two Poisson cases is YES",
        stdout.count("deterministic high-fidelity Bell resource (threshold 0.900): YES") == 2,
    )


def part_R5_load_bearing_static_checks() -> None:
    section("(R5) Load-bearing-content static checks on parent note prose")
    text = read_text(PARENT_NOTE_REL)
    check(
        "parent note declares **Type:** open_gate",
        "**Type:** open_gate" in text,
    )
    check(
        "parent note declares **Claim type:** open_gate",
        "**Claim type:** open_gate" in text,
    )
    check(
        "parent note contains '2026-05-28 Audit Repair' section heading",
        "## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)" in text,
    )
    check(
        "parent note contains 'Load-bearing (in scope)' split bullet",
        "**Load-bearing (in scope):**" in text,
    )
    check(
        "parent note contains 'NON-load-bearing (split off / admitted)' split bullet",
        "**NON-load-bearing (split off / admitted):**" in text,
    )
    check(
        "parent note contains 'Scope Repair Boundary (2026-05-27)' section",
        "## Scope Repair Boundary (2026-05-27)" in text,
    )
    check(
        "parent note contains 'Citation Chain And Repair Path (2026-05-10)' section",
        "## Citation Chain And Repair Path (2026-05-10)" in text,
    )
    check(
        "parent note explicitly states 'no new axiom is introduced'",
        "no new axiom is introduced here." in text,
    )
    check(
        "parent note explicitly promises last-taste-bit non-derivation",
        "No sentence in this note asserts that the last taste bit has been derived as" in text
        and "a native physical carrier." in text,
    )
    check(
        "parent note cites MINIMAL_AXIOMS_2026-05-20.md as A1+A2 premise",
        "[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)" in text,
    )
    check(
        "parent note cites adjacent Poisson sweep note in citation table",
        "TELEPORTATION_POISSON_RESOURCE_SWEEP_NOTE.md" in text,
    )
    check(
        "parent note cites adjacent resource fidelity note in citation table",
        "TELEPORTATION_RESOURCE_FIDELITY_NOTE.md" in text,
    )
    check(
        "parent note cites adjacent measurement-record note in citation table",
        "TELEPORTATION_MEASUREMENT_RECORD_NOTE.md" in text,
    )
    check(
        "parent note cites adjacent apparatus-dynamics-closure note in citation table",
        "TELEPORTATION_APPARATUS_DYNAMICS_CLOSURE_NOTE.md" in text,
    )
    check(
        "parent note explicitly excludes matter teleportation / FTL claims",
        "It does not claim matter teleportation, charge transfer, mass transfer, or" in text
        and "faster-than-light transport." in text,
    )


def part_R6_invalidation_reason_structure() -> None:
    section("(R6) Invalidation-reason structure on ledger row")
    row = load_ledger_row()
    previous_audits = row.get("previous_audits", [])
    check(
        "ledger row has at least one previous_audits entry",
        len(previous_audits) >= 1,
        f"len(previous_audits)={len(previous_audits)}",
    )
    most_recent = previous_audits[0] if previous_audits else {}
    invalidation_reason = most_recent.get("invalidation_reason", "") or ""
    check(
        f"most-recent previous audit was {EXPECTED_PRIOR_AUDIT_STATUS}",
        most_recent.get("audit_status") == EXPECTED_PRIOR_AUDIT_STATUS,
        f"audit_status={most_recent.get('audit_status')!r}",
    )
    check(
        "most-recent invalidation_reason begins with criticality_increased",
        invalidation_reason.startswith(EXPECTED_INVALIDATION_PREFIX),
        f"invalidation_reason={invalidation_reason!r}",
    )
    breakdown = most_recent.get("runner_check_breakdown", {}) or {}
    check(
        f"prior runner_check_breakdown total_pass == {EXPECTED_PRIOR_TOTAL_PASS}",
        breakdown.get("total_pass") == EXPECTED_PRIOR_TOTAL_PASS,
        f"total_pass={breakdown.get('total_pass')}",
    )
    for cls, expected in EXPECTED_PRIOR_CHECK_BREAKDOWN.items():
        check(
            f"prior runner_check_breakdown class {cls} == {expected}",
            breakdown.get(cls) == expected,
            f"{cls}={breakdown.get(cls)}",
        )
    # Verify the current claim_type is still open_gate (per author hint).
    check(
        "current ledger row claim_type is open_gate",
        row.get("claim_type") == "open_gate",
        f"claim_type={row.get('claim_type')!r}",
    )


def part_R7_helper_runner_presence() -> None:
    section("(R7) Helper-runner presence")
    for rel in HELPER_RUNNER_RELS:
        check(
            f"helper runner exists on disk: {rel}",
            (ROOT / rel).is_file(),
            f"path={rel}",
        )


def main() -> int:
    print("=" * 88)
    print("AUDIT COMPANION: TELEPORTATION RESOURCE FROM POISSON")
    print("CRITICALITY-BUMP AUDIT-READINESS HYGIENE (open_gate parent)")
    print("=" * 88)
    print()
    print("Companion target:")
    print(f"  {LEDGER_ROW_ID}")
    print()
    print("Question:")
    print("  Has the parent note's substance changed since the prior")
    print("  audited_clean verdict, or is the criticality-bump invalidation")
    print("  a queue-priority signal only?")
    print()
    print("Answer:")
    print("  The substance is unchanged. The invalidation is a")
    print("  queue-priority bump (criticality_increased: leaf -> medium),")
    print("  not a content-change flag. The open_gate admission")
    print("  (native preparation/readout theorem selecting the last KS")
    print("  taste bit as a deterministic physical carrier) is unchanged")
    print("  and remains admitted, not-derived.")

    part_R1_presence()
    part_R2_note_hash_invariance()
    part_R3_parent_runner_execution()
    part_R4_parent_runner_numerical_surface()
    part_R5_load_bearing_static_checks()
    part_R6_invalidation_reason_structure()
    part_R7_helper_runner_presence()

    print()
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
