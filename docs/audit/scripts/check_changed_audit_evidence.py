#!/usr/bin/env python3
"""Review-time evidence-readiness gate for changed scientific surfaces.

Run after the audit pipeline.  It maps the branch diff to ledger rows and
fails when a changed source/runner/helper is mechanically incapable of
supplying the forensic packet expected after merge.  This is not an audit and
never grants a verdict: the audit lane re-executes the runner live.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import forensic_evidence_readiness
import ledger_io


REPO_ROOT = Path(__file__).resolve().parents[3]
LEDGER_PATH = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"


def _git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip())
    return proc.stdout


def changed_paths(base: str) -> set[str]:
    merge_base = _git("merge-base", base, "HEAD").strip()
    if not merge_base:
        raise RuntimeError(f"cannot resolve merge-base against {base}")
    return {
        line.strip()
        for line in _git("diff", "--name-only", f"{merge_base}...HEAD").splitlines()
        if line.strip()
    }


def affected_rows(
    rows: dict[str, dict],
    paths: set[str],
) -> list[tuple[str, dict, list[str]]]:
    affected: list[tuple[str, dict, list[str]]] = []
    for claim_id, row in rows.items():
        surfaces = {
            str(row.get("note_path") or ""),
            str(row.get("runner_path") or ""),
            *(str(path) for path in row.get("helper_runner_paths") or []),
        }
        overlap = sorted((surfaces - {""}) & paths)
        if not overlap:
            continue
        claim_type = row.get("claim_type") or row.get("claim_type_author_hint")
        if claim_type in {"meta", "open_gate", "decoration"}:
            continue
        affected.append((claim_id, row, overlap))
    return affected


def build_report(base: str) -> dict:
    ledger_io.ensure_cache()
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    rows = ledger.get("rows") or {}
    paths = changed_paths(base)
    checked: list[dict] = []
    failures: list[dict] = []
    for claim_id, row, overlap in affected_rows(rows, paths):
        issue = forensic_evidence_readiness.cached_row_readiness_issue(
            {**row, "claim_id": claim_id},
            rows,
            REPO_ROOT,
        )
        record = {
            "claim_id": claim_id,
            "changed_surfaces": overlap,
            "runner_path": row.get("runner_path"),
            "helper_runner_paths": list(row.get("helper_runner_paths") or []),
            "forensic_evidence_ready": issue is None,
            "issue": issue,
        }
        checked.append(record)
        if issue is not None:
            failures.append(record)
    return {
        "schema": "changed_audit_evidence_readiness_v1",
        "base": base,
        "changed_path_count": len(paths),
        "checked": checked,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        report = build_report(args.base)
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"changed-audit-evidence: ERROR: {exc}")
        return 2
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(
            "changed-audit-evidence: "
            f"checked={len(report['checked'])} failures={len(report['failures'])}"
        )
        for failure in report["failures"]:
            print(f"  {failure['claim_id']}: {failure['issue']}")
    return 1 if report["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
