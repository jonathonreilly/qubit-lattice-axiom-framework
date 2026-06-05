#!/usr/bin/env python3
"""Audit-readiness hygiene companion for Hubble Lane 5 (C1) A2
action-unit metrology obstruction.

Companion target:
    hubble_lane5_c1_a2_action_unit_metrology_obstruction_note_2026-04-29

The parent row's most recent invalidation is structurally a
deps-changed (dep-added) event: the structured ``deps`` field gained
``staggered_dirac_realization_gate_note_2026-05-03`` since the
2026-05-23 ``audited_conditional`` verdict's snapshot. That gate was
already named in the prior verdict's ``open_dependency_paths`` and
``notes_for_re_audit_if_any`` field, and was already declared an
admitted-context input in the parent's prose at audit time. The
dep-add event is a citation-extractor catch-up to the parent's
explicit ``Hypothesis set used (axiom-reset 2026-05-03)`` section,
not a new dependency surface element.

This runner verifies that:

  (R1)  Parent note and parent runner files exist on disk.
  (R2)  On-disk parent note SHA-256 matches the current ledger row's
        ``note_hash`` field.
  (R3)  On-disk parent runner SHA-256 matches the prior audit's
        ``audit_state_snapshot.runner_hash``.
  (R4)  Parent runner exits with status 0 and ``PASS=8 FAIL=0``
        matching the prior audits' ``A=7, B=1, C=0, D=0,
        total_pass=8`` breakdown.
  (R5)  Parent prose contains the load-bearing rescaling identity,
        dimensionless input table, result/claim-boundary paragraphs,
        missing-import line, and runner-witness fact list.
  (R6)  Parent's ``Hypothesis set used (axiom-reset 2026-05-03)``
        section is present and names both gates.
  (R7)  Parent's ``Admitted context inputs:`` header line names both
        gates in numbered form.
  (R8)  Current ledger row has ``deps`` containing exactly the two
        expected entries, ``criticality=medium``,
        ``load_bearing_score=5.959``, ``transitive_descendants=21``,
        ``effective_status=unaudited``, ``audit_status=unaudited``,
        ``claim_type=bounded_theorem``.
  (R9)  Prior-audit history shape: exactly two prior audits; most
        recent is ``audited_conditional`` (2026-05-23) with
        ``audit_state_snapshot.deps == ['g_bare_derivation_note']``
        (single-element list).
  (R10) Dep-set diff between current and prior-audit snapshot equals
        ``{staggered_dirac_realization_gate_note_2026-05-03}``,
        confirming the invalidation reason is
        ``deps_changed:dep_added:staggered_dirac_realization_gate_note_2026-05-03``.
  (R11) The added dep's canonical filename appears in the parent's
        prose (both the header line and the ``Hypothesis set used``
        section), confirming the prose declared it at audit time.
  (R12) The unchanged dep ``g_bare_derivation_note`` (filename
        ``G_BARE_DERIVATION_NOTE.md``) remains in the prose.
  (R13) Both gate files exist on disk so the audit lane can re-fetch
        their content if needed.
  (R14) Cached log exists on disk and contains the ``TOTAL: PASS=8,
        FAIL=0`` line and the eight per-check ``[PASS]`` lines.
  (R15) Parent header's ``Type:`` line names the ``bounded_theorem
        (axiom-reset retag 2026-05-03; was positive_theorem)``
        retag, consistent with bounded-on-both-gates status.
  (R16) Helper runner ``scripts/canonical_plaquette_surface.py``
        (listed in the ledger row's ``helper_runner_paths``) exists
        on disk.
  (R17) Sister Lane 5 row ``hubble_lane5_two_gate_dependency_firewall_note_2026-04-27``
        is present on disk so the audit lane can cross-reference
        the sister hygiene companion filed 2026-06-04.
  (R18) This companion note itself exists on disk at the canonical
        path advertised in the PR title.
  (R19) This companion note's ``Type:`` header line contains the
        literal token ``meta``, confirming ``claim_type=meta`` per
        the precedent of CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08
        and RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.
  (R20) No-parent-edit self-check: re-asserts the parent note's
        on-disk SHA-256 still matches the current ledger row's
        ``note_hash`` (the companion adds no parent edits).

Exit code 0 with all checks passing (PASS count in the low-50s) means
the parent's substance, runner output, and dependency surface are
provably identical to what the prior ``audited_conditional`` verdict
already evaluated, modulo the single dep-add the prior verdict's
reasoning already named.

This runner does no new physics. It claims no derivation, performs
no re-audit, and writes/modifies no ledger field.
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
EXPECTED_NOTE_HASH = (
    "5708b03f218f00e460f2f643af302db224173bbd2137587a67ab811d00859427"
)
EXPECTED_RUNNER_HASH = (
    "51df6c191e8d2de45fe2be4997cf1a1751a4147ec8e98795358f8d4c0d355fbe"
)
EXPECTED_PARENT_PASS = 8
EXPECTED_BREAKDOWN = {"A": 7, "B": 1, "C": 0, "D": 0, "total_pass": 8}
EXPECTED_DEPS = {
    "g_bare_derivation_note",
    "staggered_dirac_realization_gate_note_2026-05-03",
}
EXPECTED_ADDED_DEP = "staggered_dirac_realization_gate_note_2026-05-03"
EXPECTED_PRIOR_SNAP_DEPS = ["g_bare_derivation_note"]
EXPECTED_PRIOR_AUDIT_COUNT = 2
EXPECTED_CRITICALITY = "medium"
EXPECTED_LOAD_BEARING = 5.959
EXPECTED_TRANSITIVE_DESCENDANTS = 21


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
        "ledger row recorded expected note_hash",
        ledger_hash == EXPECTED_NOTE_HASH,
        f"ledger={ledger_hash[:12]}... expected={EXPECTED_NOTE_HASH[:12]}...",
    )
    check(
        "on-disk note hash matches ledger note_hash to the byte",
        on_disk_hash == ledger_hash,
        f"on_disk={on_disk_hash[:12]}... ledger={ledger_hash[:12]}...",
    )


def part_R3_runner_hash_invariance() -> None:
    section("(R3) Parent runner-hash audit-time invariance")
    on_disk_hash = hashlib.sha256(read_bytes(PARENT_RUNNER_REL)).hexdigest()
    row = load_ledger_row()
    prior = (row.get("previous_audits") or [])[-1] if row else {}
    snap = (prior or {}).get("audit_state_snapshot") or {}
    snap_runner_hash = snap.get("runner_hash") or ""
    check(
        "on-disk parent runner SHA-256 matches expected hash",
        on_disk_hash == EXPECTED_RUNNER_HASH,
        f"on_disk={on_disk_hash[:12]}... expected={EXPECTED_RUNNER_HASH[:12]}...",
    )
    check(
        "prior audit snapshot's runner_hash matches expected hash",
        snap_runner_hash == EXPECTED_RUNNER_HASH,
        f"snap={snap_runner_hash[:12]}... expected={EXPECTED_RUNNER_HASH[:12]}...",
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
    pass_line = next(
        (line for line in tail_lines if "PASS=" in line and "FAIL=" in line),
        "",
    )
    expected_tail = f"PASS={EXPECTED_PARENT_PASS}, FAIL=0"
    check(
        f"parent runner reports TOTAL: PASS={EXPECTED_PARENT_PASS}, FAIL=0",
        expected_tail in pass_line,
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
    section("(R6) `Hypothesis set used (axiom-reset 2026-05-03)` section")
    text = read_text(PARENT_NOTE_REL)
    check(
        "parent has explicit `Hypothesis set used (axiom-reset 2026-05-03)`"
        " section",
        "## Hypothesis set used (axiom-reset 2026-05-03)" in text,
    )
    check(
        "Hypothesis set names Staggered-Dirac realization derivation target",
        "Staggered-Dirac realization derivation target" in text,
    )
    check(
        "Hypothesis set names `g_bare = 1` derivation target",
        "`g_bare = 1` derivation target" in text,
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
        "Admitted-context header names `g_bare = 1` derivation target",
        "g_bare = 1 derivation target" in header_block,
    )


def part_R8_ledger_state_self_consistency() -> None:
    section("(R8) Ledger-row state self-consistency")
    row = load_ledger_row()
    deps = set(row.get("deps") or [])
    check(
        f"ledger row `deps` set equals {sorted(EXPECTED_DEPS)}",
        deps == EXPECTED_DEPS,
        f"deps={sorted(deps)}",
    )
    check(
        f"ledger row `criticality` == {EXPECTED_CRITICALITY!r}",
        row.get("criticality") == EXPECTED_CRITICALITY,
        f"criticality={row.get('criticality')!r}",
    )
    check(
        f"ledger row `load_bearing_score` == {EXPECTED_LOAD_BEARING}",
        abs((row.get("load_bearing_score") or 0.0) - EXPECTED_LOAD_BEARING) < 1e-6,
        f"load_bearing_score={row.get('load_bearing_score')}",
    )
    check(
        f"ledger row `transitive_descendants` == {EXPECTED_TRANSITIVE_DESCENDANTS}",
        row.get("transitive_descendants") == EXPECTED_TRANSITIVE_DESCENDANTS,
        f"transitive_descendants={row.get('transitive_descendants')}",
    )
    check(
        "ledger row `effective_status` == 'unaudited'",
        row.get("effective_status") == "unaudited",
        f"effective_status={row.get('effective_status')!r}",
    )
    check(
        "ledger row `audit_status` == 'unaudited'",
        row.get("audit_status") == "unaudited",
        f"audit_status={row.get('audit_status')!r}",
    )
    check(
        "ledger row `claim_type` == 'bounded_theorem'",
        row.get("claim_type") == "bounded_theorem",
        f"claim_type={row.get('claim_type')!r}",
    )


def part_R9_prior_audit_history_shape() -> None:
    section("(R9) Prior-audit history shape")
    row = load_ledger_row()
    prev = row.get("previous_audits") or []
    check(
        f"ledger row has exactly {EXPECTED_PRIOR_AUDIT_COUNT} previous_audits"
        " entries",
        len(prev) == EXPECTED_PRIOR_AUDIT_COUNT,
        f"len(previous_audits)={len(prev)}",
    )
    if len(prev) >= 2:
        most_recent = prev[-1]
        check(
            "most-recent prior audit is `audited_conditional` (2026-05-23)",
            most_recent.get("audit_status") == "audited_conditional"
            and (most_recent.get("audit_date") or "").startswith("2026-05-23"),
            f"audit_status={most_recent.get('audit_status')!r}"
            f" audit_date={most_recent.get('audit_date')!r}",
        )
        snap = most_recent.get("audit_state_snapshot") or {}
        snap_deps = snap.get("deps") or []
        check(
            "most-recent prior audit snapshot recorded the single-element"
            " deps list ['g_bare_derivation_note']",
            list(snap_deps) == EXPECTED_PRIOR_SNAP_DEPS,
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
            "most-recent prior audit's runner_check_breakdown equals"
            " {A:7, B:1, C:0, D:0, total_pass:8}",
            (most_recent.get("runner_check_breakdown") or {}) == EXPECTED_BREAKDOWN,
            f"breakdown={most_recent.get('runner_check_breakdown')}",
        )


def part_R10_dep_add_detection_self_check() -> None:
    section(
        "(R10) Dep-set diff confirms the invalidation reason"
        " `deps_changed:dep_added:staggered_dirac_realization_gate_note_2026-05-03`"
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
        "dep-set diff: added == {staggered_dirac_realization_gate_note_2026-05-03}",
        added == {EXPECTED_ADDED_DEP},
        f"added={sorted(added)}",
    )
    check(
        "dep-set diff: removed == {} (no deps removed)",
        not removed,
        f"removed={sorted(removed)}",
    )


def part_R11_added_dep_prose_presence() -> None:
    section("(R11) Added dep is prose-declared in parent at audit time")
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
    section("(R12) Unchanged dep `g_bare_derivation_note` is prose-declared")
    text = read_text(PARENT_NOTE_REL)
    check(
        "parent prose mentions the G_BARE_DERIVATION_NOTE.md file",
        "G_BARE_DERIVATION_NOTE.md" in text,
    )
    # Also: the prose names the `g_bare = 1` derivation target by phrase
    check(
        "parent prose names the `g_bare = 1` derivation target by phrase",
        "g_bare = 1` derivation target" in text
        or "g_bare = 1 derivation target" in text,
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
        check(
            "cached log contains the `TOTAL: PASS=8, FAIL=0` line",
            "TOTAL: PASS=8, FAIL=0" in log_text,
        )
        check(
            "cached log contains eight `[PASS]` per-check lines",
            log_text.count("[PASS]") >= 8,
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
        on_disk_hash == ledger_hash == EXPECTED_NOTE_HASH,
        f"on_disk={on_disk_hash[:12]}... ledger={ledger_hash[:12]}...",
    )


def main() -> int:
    print("=" * 88)
    print("AUDIT COMPANION: HUBBLE LANE 5 (C1) A2 ACTION-UNIT METROLOGY")
    print("OBSTRUCTION -- deps-changed (dep-added) AUDIT-READINESS HYGIENE")
    print("=" * 88)
    print()
    print("Companion target:")
    print(f"  {LEDGER_ROW_ID}")
    print()
    print("Question:")
    print("  Did the parent's substance change since the 2026-05-23 prior")
    print("  audited_conditional verdict, or is the dep-add invalidation a")
    print("  citation-graph catch-up to a dep the prior verdict already")
    print("  named in its reasoning?")
    print()
    print("Answer:")
    print("  Citation-graph catch-up. The added dep")
    print("  `staggered_dirac_realization_gate_note_2026-05-03` was already")
    print("  in the prior verdict's `open_dependency_paths` and")
    print("  `notes_for_re_audit_if_any`, and was already declared in the")
    print("  parent's prose as an admitted-context input. Note hash and")
    print("  runner hash are byte-stable; runner PASS=8 FAIL=0 unchanged.")

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
