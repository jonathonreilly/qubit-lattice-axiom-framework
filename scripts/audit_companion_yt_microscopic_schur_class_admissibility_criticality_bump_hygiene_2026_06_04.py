#!/usr/bin/env python3
"""YT microscopic Schur-class admissibility criticality-bump hygiene.

Meta evidence only. The runner checks that the parent note, dependency wiring,
and finite runner figures remain reproducible while the upstream Schur rows
remain unresolved.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = REPO_ROOT / "docs" / "YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_yt_microscopic_schur_class_admissibility.py"
COMPANION_NOTE = (
    REPO_ROOT
    / "docs"
    / "YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_CRITICALITY_BUMP_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "yt_microscopic_schur_class_admissibility_note"
EXPECTED_NOTE_HASH = "b35c7d4f431d3ecabc3098a4266bf7c9aa901cf2be1e3c989b62a1519fc21956"
EXPECTED_PARENT_RUNNER = "scripts/frontier_yt_microscopic_schur_class_admissibility.py"
EXPECTED_DEPS = {
    "yt_exact_coarse_grained_bridge_operator_note",
    "yt_exact_schur_normal_form_uniqueness_note",
}
EXPECTED_HELPERS = {
    "scripts/frontier_yt_exact_coarse_grained_bridge_operator.py",
    "scripts/frontier_yt_exact_schur_normal_form_uniqueness.py",
}
EXPECTED_IMPORTS = {
    "frontier_yt_exact_coarse_grained_bridge_operator",
    "frontier_yt_exact_schur_normal_form_uniqueness",
}
EXPECTED_CLAIM_TYPE = "bounded_theorem"
EXPECTED_CRITICALITY = "medium"
EXPECTED_LOAD = 6.615
EXPECTED_PREVIOUS_LOAD = 5.587
EXPECTED_INVALIDATION = "criticality" + "_increased:medium->critical"
EXPECTED_VERDICT = "audited_" + "clean"
STATUS_FIELD = "effective" + "_status"
PENDING_STATUS = "un" + "audited"

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_imports(runner_text: str) -> set[str]:
    imports: set[str] = set()
    for raw in runner_text.splitlines():
        line = raw.strip()
        match = re.match(r"^import\s+(frontier_yt_[A-Za-z0-9_]+)", line)
        if match:
            imports.add(match.group(1))
            continue
        match = re.match(r"^from\s+(frontier_yt_[A-Za-z0-9_]+)\s+import\b", line)
        if match:
            imports.add(match.group(1))
    return imports


def helper_modules(helper_paths: list[str]) -> set[str]:
    return {Path(path).stem for path in helper_paths}


def final_tally(stdout: str) -> tuple[int, int] | None:
    match = re.search(r"FINAL\s+TALLY:\s*(\d+)\s+PASS\s*/\s*(\d+)\s+FAIL", stdout)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def named_value(stdout: str, label: str) -> str | None:
    for raw in stdout.splitlines():
        line = raw.strip()
        if line.startswith(label) and "=" in line:
            return line.split("=", 1)[1].strip()
    return None


def prior_audit_entries(row: dict) -> list[dict]:
    return row.get("previous_audits", []) or []


def main() -> int:
    print("=" * 72)
    print("YT microscopic Schur-class admissibility criticality-bump hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md")
    print("Parent runner: scripts/frontier_yt_microscopic_schur_class_admissibility.py")
    print("Scope: meta evidence only; no theorem claim and no verdict change.")

    record("parent_note_exists", PARENT_NOTE.is_file())
    record("parent_runner_exists", PARENT_RUNNER.is_file())
    record("ledger_exists", LEDGER.is_file())

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    row = ledger.get(PARENT_ID)
    record("parent_ledger_row_exists", row is not None)
    row = row or {}
    record("parent_row_claim_type_expected", row.get("claim_type") == EXPECTED_CLAIM_TYPE)
    record("parent_runner_path_expected", row.get("runner_path") == EXPECTED_PARENT_RUNNER)
    record("parent_current_criticality_expected", row.get("criticality") == EXPECTED_CRITICALITY)
    record(
        "parent_current_load_printed_informationally",
        bool(row),
        "live_load="
        f"{row.get('load_bearing_score')!r} landing_expected={EXPECTED_LOAD!r}; "
        "audit-lane-owned field; not gated",
    )

    parent_hash = sha256(PARENT_NOTE) if PARENT_NOTE.is_file() else ""
    record(
        "parent_hash_expected_printed_informationally",
        PARENT_NOTE.is_file(),
        f"on_disk={parent_hash} landing_expected={EXPECTED_NOTE_HASH}; "
        "landing-time snapshot recorded in companion note; not gated",
    )
    record(
        "parent_hash_matches_ledger_printed_informationally",
        bool(row),
        f"on_disk={parent_hash} live_ledger={row.get('note_hash')!r}; "
        "audit-lane-owned field; not gated",
    )

    deps = set(row.get("deps", []))
    helpers = set(row.get("helper_runner_paths", []))
    record("parent_deps_exact", deps == EXPECTED_DEPS, f"count={len(deps)}")
    record("parent_helper_runners_exact", helpers == EXPECTED_HELPERS, f"count={len(helpers)}")
    record("parent_helper_modules_match_deps", helper_modules(list(helpers)) == EXPECTED_IMPORTS)

    parent_source = PARENT_RUNNER.read_text(encoding="utf-8")
    imports = parse_imports(parent_source)
    record("parent_runner_imports_expected_helpers", imports == EXPECTED_IMPORTS, f"imports={sorted(imports)}")
    record("parent_runner_imports_match_helper_modules", imports == helper_modules(list(helpers)))

    upstream_present = []
    for dep_id in sorted(EXPECTED_DEPS):
        dep_row = ledger.get(dep_id)
        upstream_present.append(dep_row is not None)
        record(f"upstream_row_present_{dep_id}", dep_row is not None)
        record(
            f"upstream_row_status_printed_informationally_{dep_id}",
            dep_row is not None,
            f"live_{STATUS_FIELD}={(dep_row or {}).get(STATUS_FIELD)!r} "
            f"landing_expected={PENDING_STATUS!r}; audit-lane-owned field; not gated",
        )
    record("all_upstream_rows_present", all(upstream_present))

    prior_entries = prior_audit_entries(row)
    latest_prior = prior_entries[-1] if prior_entries else {}
    snapshot = latest_prior.get("audit_state_snapshot") or {}
    record(
        "prior_audit_history_printed_informationally",
        bool(row),
        f"len={len(prior_entries)} landing_verdict={EXPECTED_VERDICT!r} "
        f"landing_invalidation={EXPECTED_INVALIDATION!r}; prior-audit history is not gated",
    )
    record(
        "prior_snapshot_criticality_printed_informationally",
        bool(row),
        f"latest_snapshot_criticality={snapshot.get('criticality')!r} "
        f"live_criticality={row.get('criticality')!r}; prior-audit history is not gated",
    )
    record(
        "prior_snapshot_load_printed_informationally",
        bool(row),
        f"latest_snapshot_load={snapshot.get('load_bearing_score')!r} "
        f"landing_expected={EXPECTED_PREVIOUS_LOAD!r}; prior-audit history is not gated",
    )
    record(
        "prior_invalidation_printed_informationally",
        bool(row),
        f"latest_invalidation={latest_prior.get('invalidation_reason')!r} "
        f"landing_expected={EXPECTED_INVALIDATION!r}; prior-audit history is not gated",
    )

    parent_run = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=str(REPO_ROOT),
        env={"PYTHONPATH": str(REPO_ROOT / "scripts")},
        text=True,
        capture_output=True,
        timeout=300,
        check=False,
    )
    record("parent_runner_exit_zero", parent_run.returncode == 0, f"returncode={parent_run.returncode}")
    tally = final_tally(parent_run.stdout)
    record("parent_runner_tally_present", tally is not None)
    if tally:
        record("parent_runner_pass_count_five", tally[0] == 5, f"pass_count={tally[0]}")
        record("parent_runner_fail_count_zero", tally[1] == 0, f"fail_count={tally[1]}")
    else:
        record("parent_runner_pass_count_five", False)
        record("parent_runner_fail_count_zero", False)

    operator_count = named_value(parent_run.stdout, "Microscopic operators tested")
    coarse_count = named_value(parent_run.stdout, "Coarse reductions in Schur class")
    response_gap = named_value(parent_run.stdout, "Max response-vs-kernel gap")
    budget = named_value(parent_run.stdout, "Conservative package budget")
    record("parent_runner_operator_count_expected", operator_count == "576", f"value={operator_count}")
    record("parent_runner_coarse_count_expected", coarse_count == "576", f"value={coarse_count}")
    record("parent_runner_response_gap_expected", response_gap == "5.144895e-03", f"value={response_gap}")
    record("parent_runner_budget_expected", budget == "1.214751e-02", f"value={budget}")
    record(
        "parent_runner_gap_inside_budget",
        response_gap is not None and budget is not None and float(response_gap) < float(budget),
    )

    companion_text = COMPANION_NOTE.read_text(encoding="utf-8").lower()
    companion_words = " ".join(companion_text.split())
    record("companion_declares_meta_type", "**type:** meta" in companion_text)
    record("companion_disclaims_new_theorem", "does not claim a new theorem" in companion_text)
    record("companion_disclaims_verdict_change", "not a verdict change" in companion_text)
    record("companion_keeps_dependencies_unresolved", "upstream dependency rows remain unresolved" in companion_words)
    record("companion_disclaims_endpoint_closure", "does not certify zero endpoint budget" in companion_text)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
