#!/usr/bin/env python3
"""Audit-companion runner for the YT Microscopic Schur-Class
Admissibility parent note
`docs/YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md`, recording
criticality-bump readiness after the prior `audited_clean` verdict was
invalidated by `criticality_increased:medium->critical`.

Companion source note:
  docs/YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_CRITICALITY_BUMP_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  yt_microscopic_schur_class_admissibility_note

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion.
  - Provides audit-friendly evidence that the parent's note hash,
    primary runner output, and registered dependency edges are
    consistent with the conditions under which the prior 2026-05-01
    `audited_clean` verdict was issued.

The runner walks 21 read-only checks against the live filesystem and
audit ledger. It does NOT write to the ledger, does NOT call
`apply_audit`, and does NOT edit the parent note or parent runner.

Block plan:
  Block  1 : Parent note file exists.
  Block  2 : Ledger row exists with the expected runner_path.
  Block  3 : Current parent file hash matches the ledger's note_hash.
  Block  4 : Hash matches the expected hex string from the ledger row.
  Block  5 : Ledger declares at least one archived audited_clean entry.
  Block  6 : Archived clean entry's invalidation reason is
             criticality_increased:medium->critical.
  Block  7 : Archived clean entry recorded a positive runner pass total.
  Block  8 : Current row criticality matches the clean entry's
             criticality snapshot.
  Block  9 : Current row claim_type matches the clean entry's claim_type.
  Block 10 : Every entry in the row's deps[] is a known claim_id in the
             ledger.
  Block 11 : Parent runner's imported upstream module names correspond
             bijectively to the row's helper_runner_paths.
  Block 12 : Parent runner exits 0 under `subprocess.run`.
  Block 13 : Parent runner reports "FINAL TALLY: 5 PASS / 0 FAIL".
  Block 14 : Parent runner reports max response gap 5.144895e-03.
  Block 15 : Parent runner reports conservative budget 1.214751e-02.
  Block 16 : max response gap is strictly inside the budget.
  Block 17 : Parent runner reports 576 microscopic operators tested.
  Block 18 : "Coarse reductions in Schur class" equals the operator
             count.
  Block 19 : This companion runner filename uses the audit_companion_*
             meta convention.
  Block 20 : Static-source scan: companion runner issues no writes to
             audit_ledger.json and no apply_audit invocations.
  Block 21 : Parent note text names both registered deps in its
             "Audit dependency repair links" section.

The exact PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

# -----------------------------------------------------------
# Configuration
# -----------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT_NOTE_REL = "docs/YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md"
PARENT_RUNNER_REL = "scripts/frontier_yt_microscopic_schur_class_admissibility.py"
LEDGER_REL = "docs/audit/data/audit_ledger.json"
THIS_RUNNER_REL = "scripts/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.py"

CLAIM_ID = "yt_microscopic_schur_class_admissibility_note"
EXPECTED_NOTE_HASH = "b35c7d4f431d3ecabc3098a4266bf7c9aa901cf2be1e3c989b62a1519fc21956"
EXPECTED_INVALIDATION_REASON = "criticality_increased:medium->critical"
EXPECTED_AT_CLEAN_CRITICALITY = "medium"
EXPECTED_CLAIM_TYPE = "bounded_theorem"
EXPECTED_TOTAL_PASS_RUNNER = 5
EXPECTED_MAX_RESPONSE_GAP = "5.144895e-03"
EXPECTED_BUDGET = "1.214751e-02"
EXPECTED_OPERATOR_COUNT = 576

EXPECTED_DEPS = (
    "yt_exact_coarse_grained_bridge_operator_note",
    "yt_exact_schur_normal_form_uniqueness_note",
)
EXPECTED_HELPER_RUNNERS = (
    "scripts/frontier_yt_exact_coarse_grained_bridge_operator.py",
    "scripts/frontier_yt_exact_schur_normal_form_uniqueness.py",
)

# -----------------------------------------------------------
# Logging
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


def section(title: str) -> None:
    log("")
    log("=" * 78)
    log(title)
    log("=" * 78)


# -----------------------------------------------------------
# Helpers
# -----------------------------------------------------------


def load_ledger() -> dict:
    p = REPO_ROOT / LEDGER_REL
    with p.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def get_row(ledger: dict) -> dict:
    return ledger["rows"][CLAIM_ID]


def file_hash(rel_path: str) -> str:
    p = REPO_ROOT / rel_path
    with p.open("rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def archived_clean_entry(row: dict) -> dict | None:
    for entry in row.get("previous_audits", []) or []:
        if entry.get("audit_status") == "audited_clean":
            return entry
    return None


def parse_imports_from_runner(runner_text: str) -> set[str]:
    """Return module names imported by the parent runner that match
    the frontier_yt_* prefix (its upstream deps)."""
    found: set[str] = set()
    for line in runner_text.splitlines():
        line = line.strip()
        m = re.match(r"^import\s+(frontier_yt_[A-Za-z0-9_]+)", line)
        if m:
            found.add(m.group(1))
            continue
        m = re.match(r"^from\s+(frontier_yt_[A-Za-z0-9_]+)\s+import\b", line)
        if m:
            found.add(m.group(1))
    return found


def helper_runners_to_module_names(helper_paths: list[str]) -> set[str]:
    return {Path(p).stem for p in helper_paths}


def runner_stdout() -> tuple[int, str]:
    cmd = [sys.executable, str(REPO_ROOT / PARENT_RUNNER_REL)]
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
        timeout=300,
    )
    return proc.returncode, proc.stdout


def parse_final_tally(stdout: str) -> tuple[int, int] | None:
    m = re.search(r"FINAL\s+TALLY:\s*(\d+)\s+PASS\s*/\s*(\d+)\s+FAIL", stdout)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def parse_named_value(stdout: str, label: str) -> str | None:
    """Find a `label ... = <value>` line and return the trailing value
    (whitespace-trimmed). The runner uses `=` alignment, so we anchor
    on the label and read after the first `=`."""
    for raw in stdout.splitlines():
        line = raw.strip()
        if line.startswith(label):
            if "=" in line:
                return line.split("=", 1)[1].strip()
    return None


# -----------------------------------------------------------
# Blocks
# -----------------------------------------------------------


def block_1_parent_note_exists() -> None:
    section("Block 1 :: Parent note file exists at expected path")
    p = REPO_ROOT / PARENT_NOTE_REL
    ok = p.is_file()
    record(
        "parent note file is present at the expected path",
        ok,
        f"path={PARENT_NOTE_REL}",
    )


def block_2_ledger_row_present(ledger: dict) -> dict | None:
    section("Block 2 :: Ledger row exists with expected runner_path")
    rows = ledger.get("rows", {})
    if CLAIM_ID not in rows:
        record(
            "ledger row present for parent claim",
            False,
            f"missing claim_id={CLAIM_ID}",
        )
        return None
    row = rows[CLAIM_ID]
    record(
        "ledger row present for parent claim",
        True,
        f"claim_id={CLAIM_ID}",
    )
    rp_ok = row.get("runner_path") == PARENT_RUNNER_REL
    record(
        "ledger row's runner_path matches expected parent runner",
        rp_ok,
        f"runner_path={row.get('runner_path')}",
    )
    return row


def block_3_note_hash_matches_ledger(row: dict) -> None:
    section("Block 3 :: Parent note hash matches the ledger note_hash")
    on_disk = file_hash(PARENT_NOTE_REL)
    ledger_hash = row.get("note_hash")
    ok = on_disk == ledger_hash
    record(
        "on-disk sha256 of parent note equals ledger note_hash",
        ok,
        f"on_disk={on_disk[:16]}..., ledger={str(ledger_hash)[:16]}...",
    )


def block_4_note_hash_matches_expected() -> None:
    section("Block 4 :: Parent note hash matches the audited hex string")
    on_disk = file_hash(PARENT_NOTE_REL)
    ok = on_disk == EXPECTED_NOTE_HASH
    record(
        "on-disk sha256 of parent note equals expected hex string",
        ok,
        f"on_disk={on_disk[:16]}..., expected={EXPECTED_NOTE_HASH[:16]}...",
    )


def block_5_clean_entry_present(row: dict) -> dict | None:
    section("Block 5 :: Ledger declares an archived audited_clean entry")
    entry = archived_clean_entry(row)
    if entry is None:
        record(
            "archived audited_clean entry present in previous_audits",
            False,
            "no audited_clean entry found",
        )
        return None
    record(
        "archived audited_clean entry present in previous_audits",
        True,
        (
            f"auditor_family={entry.get('auditor_family')}, "
            f"audit_date={entry.get('audit_date')}, "
            f"chain_closes={entry.get('chain_closes')}, "
            f"independence={entry.get('independence')}, "
            f"confidence={entry.get('auditor_confidence')}"
        ),
    )
    return entry


def block_6_invalidation_is_criticality_bump(clean_entry: dict) -> None:
    section(
        "Block 6 :: Archived clean entry invalidation reason is the "
        "criticality_increased event"
    )
    reason = clean_entry.get("invalidation_reason")
    ok = reason == EXPECTED_INVALIDATION_REASON
    record(
        "archived clean entry invalidation_reason matches expected",
        ok,
        f"reason={reason}",
    )


def block_7_clean_runner_pass_total(clean_entry: dict) -> None:
    section("Block 7 :: Archived clean entry recorded a positive runner pass total")
    breakdown = clean_entry.get("runner_check_breakdown") or {}
    total_pass = breakdown.get("total_pass", 0)
    ok = isinstance(total_pass, int) and total_pass >= 1
    record(
        "archived clean entry runner_check_breakdown.total_pass is positive",
        ok,
        f"total_pass={total_pass}",
    )


def block_8_current_criticality_matches(row: dict, clean_entry: dict) -> None:
    section(
        "Block 8 :: Current criticality matches the criticality at which "
        "the clean verdict was issued"
    )
    current = row.get("criticality")
    snapshot = clean_entry.get("audit_state_snapshot") or {}
    clean_crit = snapshot.get("criticality")
    ok_eq = current == clean_crit
    ok_expected = current == EXPECTED_AT_CLEAN_CRITICALITY
    record(
        "current row criticality equals clean snapshot criticality",
        ok_eq,
        f"current={current}, clean={clean_crit}",
    )
    record(
        "current row criticality equals expected baseline value",
        ok_expected,
        f"current={current}, expected={EXPECTED_AT_CLEAN_CRITICALITY}",
    )


def block_9_current_claim_type_matches(row: dict, clean_entry: dict) -> None:
    section("Block 9 :: Current claim_type is unchanged from the clean entry")
    current = row.get("claim_type")
    clean_ct = clean_entry.get("claim_type")
    ok_eq = current == clean_ct
    ok_expected = current == EXPECTED_CLAIM_TYPE
    record(
        "current row claim_type equals clean entry claim_type",
        ok_eq,
        f"current={current}, clean={clean_ct}",
    )
    record(
        "current row claim_type equals expected baseline value",
        ok_expected,
        f"current={current}, expected={EXPECTED_CLAIM_TYPE}",
    )


def block_10_deps_resolve(ledger: dict, row: dict) -> None:
    section("Block 10 :: Every entry in deps[] is a known claim_id in the ledger")
    rows = ledger.get("rows", {})
    deps = row.get("deps") or []
    missing = [d for d in deps if d not in rows]
    record(
        "all deps[] entries are present as ledger rows",
        len(missing) == 0,
        f"deps={deps}, missing={missing}",
    )
    expected_set = set(EXPECTED_DEPS)
    have_set = set(deps)
    record(
        "deps[] equals the expected upstream-dep set for this parent",
        expected_set == have_set,
        f"have={sorted(have_set)}, expected={sorted(expected_set)}",
    )


def block_11_runner_imports_match_helpers(row: dict) -> None:
    section(
        "Block 11 :: Parent runner's upstream imports bijectively match "
        "the row's helper_runner_paths"
    )
    runner_text = (REPO_ROOT / PARENT_RUNNER_REL).read_text(encoding="utf-8")
    imported = parse_imports_from_runner(runner_text)
    helpers = row.get("helper_runner_paths") or []
    expected_modules = helper_runners_to_module_names(helpers)
    ok = imported == expected_modules
    record(
        "runner-imported frontier_yt_* modules equal helper_runner_paths basenames",
        ok,
        f"imported={sorted(imported)}, helpers={sorted(expected_modules)}",
    )
    expected_set = set(Path(p).stem for p in EXPECTED_HELPER_RUNNERS)
    record(
        "helper_runner_paths equals the expected upstream-runner set",
        expected_modules == expected_set,
        f"have={sorted(expected_modules)}, expected={sorted(expected_set)}",
    )


def block_12_to_18_runner_replay() -> str:
    section("Block 12 :: Parent runner exits 0")
    code, stdout = runner_stdout()
    record(
        "subprocess.run on parent runner returns exit code 0",
        code == 0,
        f"exit_code={code}",
    )

    section("Block 13 :: Parent runner reports FINAL TALLY: 5 PASS / 0 FAIL")
    tally = parse_final_tally(stdout)
    if tally is None:
        record(
            "FINAL TALLY line is present in runner stdout",
            False,
            "no FINAL TALLY line found",
        )
    else:
        p, f = tally
        ok = (p, f) == (EXPECTED_TOTAL_PASS_RUNNER, 0)
        record(
            "FINAL TALLY equals 5 PASS / 0 FAIL",
            ok,
            f"FINAL TALLY: {p} PASS / {f} FAIL",
        )

    section("Block 14 :: Parent runner reports max response gap 5.144895e-03")
    gap_str = parse_named_value(stdout, "Max response-vs-kernel gap")
    ok = gap_str is not None and gap_str.startswith(EXPECTED_MAX_RESPONSE_GAP)
    record(
        "Max response-vs-kernel gap matches expected value",
        ok,
        f"reported={gap_str}, expected_prefix={EXPECTED_MAX_RESPONSE_GAP}",
    )

    section("Block 15 :: Parent runner reports conservative budget 1.214751e-02")
    budget_str = parse_named_value(stdout, "Conservative package budget")
    ok = budget_str is not None and budget_str.startswith(EXPECTED_BUDGET)
    record(
        "Conservative package budget matches expected value",
        ok,
        f"reported={budget_str}, expected_prefix={EXPECTED_BUDGET}",
    )

    section("Block 16 :: Max response gap is strictly inside the budget")
    try:
        gap_val = float(gap_str) if gap_str is not None else float("inf")
        budget_val = float(budget_str) if budget_str is not None else 0.0
        ok = gap_val < budget_val
        record(
            "max_response_gap < conservative_budget",
            ok,
            f"gap={gap_val:.6e} < budget={budget_val:.6e}",
        )
    except (TypeError, ValueError) as exc:
        record(
            "max_response_gap < conservative_budget",
            False,
            f"parse error: {exc}",
        )

    section("Block 17 :: Parent runner reports 576 microscopic operators tested")
    ops_str = parse_named_value(stdout, "Microscopic operators tested")
    ops_ok = ops_str is not None and ops_str.strip() == str(EXPECTED_OPERATOR_COUNT)
    record(
        "Microscopic operators tested equals expected count",
        ops_ok,
        f"reported={ops_str}, expected={EXPECTED_OPERATOR_COUNT}",
    )

    section(
        "Block 18 :: 'Coarse reductions in Schur class' equals the "
        "operator count"
    )
    coarse_str = parse_named_value(stdout, "Coarse reductions in Schur class")
    coarse_ok = (
        coarse_str is not None
        and ops_str is not None
        and coarse_str.strip() == ops_str.strip()
    )
    record(
        "Coarse reductions in Schur class equals Microscopic operators tested",
        coarse_ok,
        f"coarse={coarse_str}, operators={ops_str}",
    )

    return stdout


def block_19_companion_naming_convention() -> None:
    section(
        "Block 19 :: Companion runner filename uses the audit_companion_* "
        "meta convention"
    )
    name = Path(__file__).name
    ok = name.startswith("audit_companion_")
    record(
        "this runner's filename starts with audit_companion_",
        ok,
        f"name={name}",
    )


def block_20_no_writes_to_ledger() -> None:
    section(
        "Block 20 :: Static-source scan: companion runner issues no writes "
        "to audit_ledger.json"
    )
    src = Path(__file__).read_text(encoding="utf-8")
    forbidden = [
        "apply_audit",
        "json.dump",
        "json.dumps",
    ]
    # We require that none of these tokens appear except inside string
    # literals that name THIS check itself. A simple substring scan is
    # too aggressive (it would flag e.g. "json.dumps" in this very
    # forbidden list literal). Use a token-aware scan: look for
    # function-call patterns rather than bare token mentions.
    call_patterns = [
        r"\bapply_audit\s*\(",
        r"\bjson\.dump\s*\(",
        r"\bjson\.dumps\s*\(",
    ]
    hits = []
    for pat in call_patterns:
        if re.search(pat, src):
            hits.append(pat)
    record(
        "no call-site of apply_audit / json.dump / json.dumps in this runner",
        len(hits) == 0,
        f"forbidden_call_hits={hits}",
    )
    # Also confirm we never open the ledger in write mode anywhere.
    write_pat = r"open\(\s*[^\)]*audit_ledger\.json[^\)]*['\"](w|a|w\+|a\+|x)['\"]"
    write_hit = re.search(write_pat, src)
    record(
        "no write-mode open() on audit_ledger.json in this runner",
        write_hit is None,
        f"write_open_hit={bool(write_hit)}",
    )


def block_21_parent_dep_repair_section() -> None:
    section(
        "Block 21 :: Parent note's audit-dependency-repair section names "
        "both registered deps"
    )
    text = (REPO_ROOT / PARENT_NOTE_REL).read_text(encoding="utf-8")
    coarse_named = "yt_exact_coarse_grained_bridge_operator_note" in text
    schur_named = "yt_exact_schur_normal_form_uniqueness_note" in text
    record(
        "parent note mentions yt_exact_coarse_grained_bridge_operator_note",
        coarse_named,
        f"present={coarse_named}",
    )
    record(
        "parent note mentions yt_exact_schur_normal_form_uniqueness_note",
        schur_named,
        f"present={schur_named}",
    )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------


def main() -> int:
    log("=" * 78)
    log("YT MICROSCOPIC SCHUR CLASS ADMISSIBILITY")
    log("Criticality-bump hygiene companion runner (claim_type=meta)")
    log("=" * 78)
    log(f"REPO_ROOT     = {REPO_ROOT}")
    log(f"Parent note   = {PARENT_NOTE_REL}")
    log(f"Parent runner = {PARENT_RUNNER_REL}")
    log(f"Ledger        = {LEDGER_REL}")
    log("")

    block_1_parent_note_exists()
    ledger = load_ledger()
    row = block_2_ledger_row_present(ledger)
    if row is None:
        # Without the row, the remaining blocks are meaningless. Print
        # the tally and exit non-zero so the audit lane sees the
        # missing-row condition explicitly.
        finalize()
        return 1

    block_3_note_hash_matches_ledger(row)
    block_4_note_hash_matches_expected()
    clean_entry = block_5_clean_entry_present(row)
    if clean_entry is None:
        finalize()
        return 1

    block_6_invalidation_is_criticality_bump(clean_entry)
    block_7_clean_runner_pass_total(clean_entry)
    block_8_current_criticality_matches(row, clean_entry)
    block_9_current_claim_type_matches(row, clean_entry)
    block_10_deps_resolve(ledger, row)
    block_11_runner_imports_match_helpers(row)
    block_12_to_18_runner_replay()
    block_19_companion_naming_convention()
    block_20_no_writes_to_ledger()
    block_21_parent_dep_repair_section()

    finalize()
    return 0 if FAIL == 0 else 1


def finalize() -> None:
    log("")
    log("=" * 78)
    log(f"FINAL TALLY: {PASS} PASS / {FAIL} FAIL")
    log("=" * 78)


if __name__ == "__main__":
    raise SystemExit(main())
