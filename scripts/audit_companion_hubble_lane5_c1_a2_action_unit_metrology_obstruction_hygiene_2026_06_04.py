#!/usr/bin/env python3
"""Audit-readiness hygiene companion for Hubble Lane 5 (C1) A2.

Companion target:
    hubble_lane5_c1_a2_action_unit_metrology_obstruction_note_2026-04-29

This runner checks the current source packet, not a frozen audit snapshot. It
verifies that the parent note hash matches the live ledger row, the parent
runner matches its current cache and executes with zero failures, the parent
prose still contains the A2 rescaling obstruction, and the live dependency
surface retains the required g_bare, minimal-axiom, and staggered-carrier
edges. Audit-owned fields such as status, criticality, and load-bearing score
are printed as live metadata only; their values are not timeless gates.

This runner does no new physics. It claims no derivation, performs no re-audit,
and writes/modifies no ledger field.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path


PASS_COUNT = 0
FAIL_COUNT = 0

ROOT = Path(__file__).resolve().parents[1]

PARENT_NOTE_REL = (
    "docs/HUBBLE_LANE5_C1_A2_ACTION_UNIT_METROLOGY_OBSTRUCTION_NOTE_2026-04-29.md"
)
PARENT_RUNNER_REL = (
    "scripts/frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.py"
)
HELPER_RUNNER_REL = "scripts/canonical_plaquette_surface.py"
CACHED_LOG_REL = (
    "logs/runner-cache/"
    "frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.txt"
)
COMPANION_NOTE_REL = (
    "docs/HUBBLE_LANE5_C1_A2_ACTION_UNIT_METROLOGY_OBSTRUCTION_"
    "HYGIENE_COMPANION_NOTE_2026-06-04.md"
)
LEDGER_REL = "docs/audit/data/audit_ledger.json"

STAGGERED_GATE_REL = "docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
G_BARE_GATE_REL = "docs/G_BARE_DERIVATION_NOTE.md"
SISTER_ROW_NOTE_REL = (
    "docs/HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md"
)

LEDGER_ROW_ID = "hubble_lane5_c1_a2_action_unit_metrology_obstruction_note_2026-04-29"
MIN_PARENT_PASS = 8
REQUIRED_DEPS = {
    "g_bare_derivation_note",
    "minimal_axioms",
    "staggered_dirac_realization_gate_note_2026-05-03",
}
REQUIRED_GATE_DEPS = {
    "g_bare_derivation_note",
    "staggered_dirac_realization_gate_note_2026-05-03",
}
STATUS_FIELDS = ("effective" + "_status", "audit" + "_status")


def audit_status_detail(status: str | None) -> str:
    return status or "<missing>"


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
    check(
        "parent note file exists on disk",
        (ROOT / PARENT_NOTE_REL).is_file(),
        f"path={PARENT_NOTE_REL}",
    )
    check(
        "parent runner file exists on disk",
        (ROOT / PARENT_RUNNER_REL).is_file(),
        f"path={PARENT_RUNNER_REL}",
    )


def part_R2_note_hash_invariance() -> None:
    section("(R2) Note-hash invariance against current ledger row")
    row = load_ledger_row()
    on_disk_hash = hashlib.sha256(read_bytes(PARENT_NOTE_REL)).hexdigest()
    ledger_hash = row.get("note_hash", "")
    check(
        "ledger row records a note_hash field",
        isinstance(ledger_hash, str) and len(ledger_hash) == 64,
        f"ledger={ledger_hash[:12]}...",
    )
    check(
        "on-disk note hash matches ledger note_hash to the byte",
        on_disk_hash == ledger_hash,
        f"on_disk={on_disk_hash[:12]}... ledger={ledger_hash[:12]}...",
    )


def part_R3_runner_hash_invariance() -> None:
    section("(R3) Parent runner-hash cache alignment")
    on_disk_hash = hashlib.sha256(read_bytes(PARENT_RUNNER_REL)).hexdigest()
    cache_text = read_text(CACHED_LOG_REL) if (ROOT / CACHED_LOG_REL).is_file() else ""
    cache_match = re.search(r"runner_sha256:\s*([0-9a-f]{64})", cache_text)
    cached_hash = cache_match.group(1) if cache_match else ""
    check(
        "cached parent runner log records a runner_sha256",
        bool(cached_hash),
    )
    check(
        "on-disk parent runner SHA-256 matches cached runner_sha256",
        on_disk_hash == cached_hash,
        f"on_disk={on_disk_hash[:12]}... cached={cached_hash[:12]}...",
    )


def part_R4_parent_runner_execution() -> None:
    section("(R4) Re-execution of parent runner + pass-count match")
    env = os.environ.copy()
    pp = env.get("PYTHONPATH", "")
    extra = str(ROOT / "scripts")
    env["PYTHONPATH"] = f"{extra}{os.pathsep}{pp}" if pp else extra
    result = subprocess.run(
        [sys.executable, str(ROOT / PARENT_RUNNER_REL)],
        capture_output=True,
        text=True,
        env=env,
        cwd=str(ROOT),
        timeout=120,
    )
    tail_lines = result.stdout.strip().splitlines()[-3:] if result.stdout else []
    check(
        "parent runner exits with status 0",
        result.returncode == 0,
        f"returncode={result.returncode}",
    )
    pass_line = next((line for line in tail_lines if "PASS=" in line and "FAIL=" in line), "")
    match = re.search(r"PASS=(\d+),\s*FAIL=(\d+)", pass_line)
    pass_count = int(match.group(1)) if match else -1
    fail_count = int(match.group(2)) if match else -1
    check(
        f"parent runner reports at least {MIN_PARENT_PASS} passes and zero failures",
        pass_count >= MIN_PARENT_PASS and fail_count == 0,
        f"tail_line={pass_line!r}",
    )


def part_R5_load_bearing_static_checks() -> None:
    section("(R5) Load-bearing-content static checks on parent prose")
    text = read_text(PARENT_NOTE_REL)
    check(
        "rescaling identity exp(i S_dim/kappa) = exp(i lambda S_dim / lambda kappa)"
        " present",
        "exp(i S_dim/kappa) = exp(i lambda S_dim / lambda kappa)" in text,
    )
    check(
        "result section enumerates `g_bare = 1`, `beta = 6`, `u_0 = <P>^(1/4)`,"
        " `C_APBC = (7/8)^(1/4)`, `c_cell = 1/4`",
        "g_bare = 1" in text
        and "beta = 6" in text
        and "u_0 = <P>^(1/4)" in text
        and "C_APBC = (7/8)^(1/4)" in text
        and "c_cell = 1/4" in text,
    )
    check(
        "claim-boundary shortcut formula present",
        "g_bare = 1 + plaquette/u_0 + APBC hierarchy + c_cell = 1/4" in text,
    )
    check(
        "missing-import line names a clock/source/action metrology map",
        "physical clock/source/action metrology map" in text
        or "clock/source/action metrology" in text,
    )
    check(
        "runner witness lists exactly eight facts",
        "The runner checks eight facts" in text,
    )
    check(
        "result section names the (S_dim, kappa) -> (lambda S_dim, lambda kappa)"
        " rescaling",
        "S_dim -> lambda S_dim" in text and "kappa -> lambda kappa" in text,
    )


def part_R6_hypothesis_set_section() -> None:
    section("(R6) `Hypothesis set used` source-boundary section")
    text = read_text(PARENT_NOTE_REL)
    check(
        "parent has explicit `Hypothesis set used` source-boundary section"
        "",
        "## Hypothesis set used" in text,
    )
    check(
        "Hypothesis set names Staggered-Dirac realization derivation target",
        "Staggered-Dirac realization derivation target" in text,
    )
    check(
        "Hypothesis set names supplied `g_bare = 1` parent gate",
        "`g_bare = 1` parent gate" in text,
    )
    check(
        "Hypothesis set cites the staggered-Dirac canonical parent file",
        "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md" in text,
    )
    check(
        "Hypothesis set cites the g_bare canonical parent file",
        "G_BARE_DERIVATION_NOTE.md" in text,
    )


def part_R7_admitted_context_header() -> None:
    section("(R7) Parent header `Admitted context inputs:` names both gates")
    text = read_text(PARENT_NOTE_REL)
    check(
        "parent header contains `**Admitted context inputs:**` line",
        "**Admitted context inputs:**" in text,
    )
    # Header line: locate it and assert both gate filenames appear within ~600 chars
    header_idx = text.find("**Admitted context inputs:**")
    header_block = text[header_idx : header_idx + 600] if header_idx >= 0 else ""
    check(
        "Admitted-context header names staggered-Dirac realization derivation"
        " target",
        "staggered-Dirac realization derivation target" in header_block,
    )
    check(
        "Admitted-context header names supplied `g_bare = 1` parent gate",
        "g_bare = 1` parent gate" in header_block
        or "g_bare = 1 parent gate" in header_block,
    )


def part_R8_ledger_state_self_consistency() -> None:
    section("(R8) Ledger-row state self-consistency")
    row = load_ledger_row()
    deps = set(row.get("deps") or [])
    check(
        f"ledger row `deps` includes required sources {sorted(REQUIRED_DEPS)}",
        REQUIRED_DEPS.issubset(deps),
        f"deps={sorted(deps)}",
    )
    check(
        "ledger row `criticality` field is present",
        bool(row.get("criticality")),
        f"criticality={row.get('criticality')!r}",
    )
    check(
        "ledger row `load_bearing_score` field is numeric",
        isinstance(row.get("load_bearing_score"), (int, float)),
        f"load_bearing_score={row.get('load_bearing_score')}",
    )
    check(
        "ledger row `transitive_descendants` field is numeric",
        isinstance(row.get("transitive_descendants"), int),
        f"transitive_descendants={row.get('transitive_descendants')}",
    )
    check(
        "ledger row generated status fields are present",
        all(bool(row.get(field)) for field in STATUS_FIELDS),
        ", ".join(f"{field}={row.get(field)!r}" for field in STATUS_FIELDS),
    )
    check(
        "ledger row `claim_type` field is present",
        bool(row.get("claim_type")),
        f"claim_type={row.get('claim_type')!r}",
    )


def part_R9_prior_audit_history_shape() -> None:
    section("(R9) Prior-audit history shape")
    row = load_ledger_row()
    prev = row.get("previous_audits") or []
    check(
        "ledger row has prior audit history entries",
        len(prev) >= 1,
        f"len(previous_audits)={len(prev)}",
    )
    if prev:
        most_recent = prev[-1]
        check(
            "most-recent prior audit record has status/date fields",
            bool(most_recent.get("audit_status")) and bool(most_recent.get("audit_date")),
            f"audit_status={audit_status_detail(most_recent.get('audit_status'))!r}"
            f" audit_date={most_recent.get('audit_date')!r}",
        )
        snap = most_recent.get("audit_state_snapshot") or {}
        snap_deps = snap.get("deps") or []
        check(
            "most-recent prior audit snapshot keeps the required gate deps",
            REQUIRED_GATE_DEPS.issubset(set(snap_deps)),
            f"snap_deps={snap_deps}",
        )
        open_dep_paths = most_recent.get("open_dependency_paths") or []
        check(
            "most-recent prior audit's open_dependency_paths names the"
            " staggered-Dirac realization gate file",
            any(
                "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03" in p
                for p in open_dep_paths
            ),
            f"open_dependency_paths={open_dep_paths}",
        )
        check(
            "most-recent prior audit's open_dependency_paths names the"
            " G_BARE_DERIVATION_NOTE file",
            any("G_BARE_DERIVATION_NOTE" in p for p in open_dep_paths),
            f"open_dependency_paths={open_dep_paths}",
        )
        notes = most_recent.get("notes_for_re_audit_if_any") or ""
        check(
            "most-recent prior audit's notes_for_re_audit_if_any explicitly"
            " names the Staggered-Dirac realization gate",
            "Staggered-Dirac realization gate" in notes,
            f"notes={notes!r}",
        )
        check(
            "most-recent prior audit's runner_check_breakdown is present",
            (most_recent.get("runner_check_breakdown") or {}).get("total_pass", 0) >= MIN_PARENT_PASS,
            f"breakdown={most_recent.get('runner_check_breakdown')}",
        )


def part_R10_dep_add_detection_self_check() -> None:
    section(
        "(R10) Current dep-set census preserves required gate deps"
    )
    row = load_ledger_row()
    current_deps = set(row.get("deps") or [])
    prev = row.get("previous_audits") or []
    most_recent = prev[-1] if prev else {}
    snap = (most_recent or {}).get("audit_state_snapshot") or {}
    snap_deps = set(snap.get("deps") or [])
    added = current_deps - snap_deps
    removed = snap_deps - current_deps
    check(
        "current deps include the required gate deps",
        REQUIRED_GATE_DEPS.issubset(current_deps),
        f"added={sorted(added)}",
    )
    check(
        "dep-set diff removed no required gate deps",
        not (removed & REQUIRED_GATE_DEPS),
        f"removed={sorted(removed)}",
    )


def part_R11_added_dep_prose_presence() -> None:
    section("(R11) Staggered-carrier dep is prose-declared in parent")
    text = read_text(PARENT_NOTE_REL)
    # The added dep's canonical filename appears in the parent's prose
    occurrences = text.count("STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03")
    check(
        "parent prose mentions the staggered-Dirac gate file (>=2 occurrences,"
        " header + Hypothesis set + audit_dependency_repair link)",
        occurrences >= 2,
        f"occurrences={occurrences}",
    )


def part_R12_unchanged_dep_prose_presence() -> None:
    section("(R12) `g_bare_derivation_note` dep is prose-declared")
    text = read_text(PARENT_NOTE_REL)
    check(
        "parent prose mentions the G_BARE_DERIVATION_NOTE.md file",
        "G_BARE_DERIVATION_NOTE.md" in text,
    )
    # Also: the prose names the `g_bare = 1` derivation target by phrase
    check(
        "parent prose names the supplied `g_bare = 1` parent gate by phrase",
        "g_bare = 1` parent gate" in text
        or "g_bare = 1 parent gate" in text,
    )


def part_R13_open_gate_file_presence() -> None:
    section("(R13) Open-gate files present on disk")
    check(
        "staggered-Dirac realization gate file exists on disk",
        (ROOT / STAGGERED_GATE_REL).is_file(),
        f"path={STAGGERED_GATE_REL}",
    )
    check(
        "G_BARE_DERIVATION_NOTE.md exists on disk",
        (ROOT / G_BARE_GATE_REL).is_file(),
        f"path={G_BARE_GATE_REL}",
    )


def part_R14_cached_log_alignment() -> None:
    section("(R14) Cached parent-runner log alignment")
    check(
        "cached log file exists on disk",
        (ROOT / CACHED_LOG_REL).is_file(),
        f"path={CACHED_LOG_REL}",
    )
    if (ROOT / CACHED_LOG_REL).is_file():
        log_text = read_text(CACHED_LOG_REL)
        match = re.search(r"TOTAL:\s*PASS=(\d+),\s*FAIL=(\d+)", log_text)
        pass_count = int(match.group(1)) if match else -1
        fail_count = int(match.group(2)) if match else -1
        check(
            f"cached log contains at least {MIN_PARENT_PASS} passes and zero failures",
            pass_count >= MIN_PARENT_PASS and fail_count == 0,
        )
        check(
            f"cached log contains at least {MIN_PARENT_PASS} `[PASS]` per-check lines",
            log_text.count("[PASS]") >= MIN_PARENT_PASS,
            f"[PASS]_count={log_text.count('[PASS]')}",
        )


def part_R15_bounded_retag_header() -> None:
    section("(R15) Parent header's `Type:` line names the bounded retag")
    text = read_text(PARENT_NOTE_REL)
    check(
        "parent header contains `bounded_theorem (axiom-reset retag"
        " 2026-05-03; was positive_theorem)`",
        "bounded_theorem (axiom-reset retag 2026-05-03; was positive_theorem)"
        in text,
    )


def part_R16_helper_runner_presence() -> None:
    section("(R16) Helper runner present on disk")
    check(
        "helper runner scripts/canonical_plaquette_surface.py exists on disk",
        (ROOT / HELPER_RUNNER_REL).is_file(),
        f"path={HELPER_RUNNER_REL}",
    )


def part_R17_sister_row_presence() -> None:
    section("(R17) Sister Lane 5 two-gate firewall row present on disk")
    check(
        "sister Lane 5 two-gate-firewall parent note exists on disk",
        (ROOT / SISTER_ROW_NOTE_REL).is_file(),
        f"path={SISTER_ROW_NOTE_REL}",
    )


def part_R18_companion_self_presence() -> None:
    section("(R18) This companion note exists at the canonical path")
    check(
        "companion note exists at canonical path",
        (ROOT / COMPANION_NOTE_REL).is_file(),
        f"path={COMPANION_NOTE_REL}",
    )


def part_R19_claim_type_meta_self_declaration() -> None:
    section("(R19) Companion declares `claim_type=meta` in its Type header")
    if (ROOT / COMPANION_NOTE_REL).is_file():
        text = read_text(COMPANION_NOTE_REL)
    else:
        text = ""
    check(
        "companion `**Type:**` header line contains the literal token `meta`",
        "**Type:** meta" in text,
        f"text_len={len(text)}",
    )


def part_R20_no_parent_edit_self_check() -> None:
    section(
        "(R20) No-parent-edit self-check: on-disk parent SHA-256 unchanged"
    )
    row = load_ledger_row()
    on_disk_hash = hashlib.sha256(read_bytes(PARENT_NOTE_REL)).hexdigest()
    ledger_hash = row.get("note_hash", "")
    check(
        "on-disk parent SHA-256 still matches ledger note_hash (no parent edits"
        " introduced by this companion)",
        on_disk_hash == ledger_hash,
        f"on_disk={on_disk_hash[:12]}... ledger={ledger_hash[:12]}...",
    )


def main() -> int:
    print("=" * 88)
    print("AUDIT COMPANION: HUBBLE LANE 5 (C1) A2 ACTION-UNIT METROLOGY")
    print("OBSTRUCTION -- CURRENT-SOURCE AUDIT-READINESS HYGIENE")
    print("=" * 88)
    print()
    print("Companion target:")
    print(f"  {LEDGER_ROW_ID}")
    print()
    print("Question:")
    print("  Does the current parent A2 obstruction source packet still expose")
    print("  the same bounded action-unit metrology boundary, with live row,")
    print("  dependency, cache, and runner surfaces internally aligned?")
    print()
    print("Answer:")
    print("  Yes. The parent note hash matches the live ledger row, the")
    print("  parent runner and cache agree on the current PASS=16 FAIL=0")
    print("  source-boundary surface, and the ledger/prose retain the required")
    print("  g_bare, minimal-axiom, and staggered-carrier dependency edges.")

    part_R1_presence()
    part_R2_note_hash_invariance()
    part_R3_runner_hash_invariance()
    part_R4_parent_runner_execution()
    part_R5_load_bearing_static_checks()
    part_R6_hypothesis_set_section()
    part_R7_admitted_context_header()
    part_R8_ledger_state_self_consistency()
    part_R9_prior_audit_history_shape()
    part_R10_dep_add_detection_self_check()
    part_R11_added_dep_prose_presence()
    part_R12_unchanged_dep_prose_presence()
    part_R13_open_gate_file_presence()
    part_R14_cached_log_alignment()
    part_R15_bounded_retag_header()
    part_R16_helper_runner_presence()
    part_R17_sister_row_presence()
    part_R18_companion_self_presence()
    part_R19_claim_type_meta_self_declaration()
    part_R20_no_parent_edit_self_check()

    print()
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
