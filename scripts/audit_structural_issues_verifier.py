#!/usr/bin/env python3
"""Scan the audit ledger for structural issues in the audit process.

Diagnoses recurring patterns where audit verdicts are driven by
infrastructure / pipeline gaps rather than science chain weaknesses.
Surfaces specific cases so they can be fixed mechanically.

ISSUES SCANNED:

  ISS-1 — Orchestrator not consuming helper_runner_paths.
    Claims whose ledger row has helper_runner_paths populated AND
    were audited after the pipeline fix landed AND whose
    verdict_rationale cites missing-helper / unprovided / not-in-packet
    language. This means the field is in the ledger but the packet
    builder isn't reading it.

  ISS-2 — Stale-numerics pattern.
    Claims where verdict_rationale cites that source-note numbers
    disagree with current runner output. Mechanical fix: regen the
    note's tables from the runner. NOT a science failure — a
    bookkeeping failure.

  ISS-3 — Note hash drift orphan.
    Audited rows whose note_hash doesn't match the current source
    file (note edited but seed_audit_ledger.py hasn't been re-run).

  ISS-4 — Runner file missing for declared runner_path.
    Audited rows whose runner_path declares a script that doesn't
    exist on disk. The audit ran without the runner source available.

This tool is READ-ONLY against the audit data. It does not modify
the ledger, queue, or any source files. Output is a structured
report (stdout + cached log).
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AUDIT_DATA = REPO_ROOT / "docs" / "audit" / "data"
sys.path.insert(0, str(REPO_ROOT / "docs" / "audit" / "scripts"))
import ledger_io  # noqa: E402

# Pipeline-fix landing time (helper_runner_paths first appeared on main).
# Sourced from `git log --format=%aI 860436c2e` = 2026-05-17T13:14:44Z.
PIPELINE_FIX_LANDED = datetime(2026, 5, 17, 13, 14, 44)

# Patterns indicating the auditor referenced a missing-helper / not-in-packet
# situation in its verdict rationale.
HELPER_MISSING_PATTERNS = [
    r"not in the restricted packet",
    r"not in the packet",
    r"\bunprovided\b",
    r"\bunlisted (?:imports?|runners?|infrastructure)\b",
    r"\bmissing helper\b",
    r"imported.{0,50}?not.{0,30}?(?:provided|supplied|in.+packet)",
    r"depends on.{0,80}?scripts/[A-Za-z0-9_./\-]+\.py.{0,40}?not.{0,30}?(?:provided|in.+packet|supplied)",
    r"helper module",
    r"\bunsupplied helper",
]

# Patterns indicating stale-numerics / data-drift issues.
STALE_NUMERICS_PATTERNS = [
    r"stale relative to",
    r"contradict[s]? the (?:source note|note) (?:table|rows|numbers)",
    r"current (?:completed|runner) (?:sweep|stdout) (?:shows|gives|reports)",
    r"note (?:reports|gives) [-\d.e+]+,? .{0,40}?runner (?:gives|reports|shows) [-\d.e+]+",
    r"differs from .+ runner",
    r"\bnumerically stale\b",
    r"frozen rows .{0,30}?(?:no longer|disagree)",
]


def parse_audit_date(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        # Strip timezone for comparison (assume UTC)
        s2 = s.replace("+00:00", "").split("+")[0].rstrip("Z")
        return datetime.fromisoformat(s2)
    except ValueError:
        return None


def search_patterns(text: str, patterns: list[str]) -> str | None:
    """Return the first matching pattern (regex source), or None."""
    if not text:
        return None
    for pat in patterns:
        if re.search(pat, text, re.IGNORECASE | re.DOTALL):
            return pat
    return None


def banner(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def section(title: str) -> None:
    print()
    print(f"## {title}")
    print()


def main() -> int:
    ledger_io.ensure_cache()
    banner("AUDIT-PROCESS STRUCTURAL-ISSUE VERIFIER")
    print()
    print(f"Repo root: {REPO_ROOT}")
    print(f"Pipeline-fix landed at: {PIPELINE_FIX_LANDED.isoformat()}Z")

    ledger = json.loads((AUDIT_DATA / "audit_ledger.json").read_text())
    rows: dict = ledger.get("rows", {})
    print(f"Total ledger rows: {len(rows)}")
    print()

    iss1, iss2, iss3, iss4 = [], [], [], []

    for cid, r in rows.items():
        rat = (r.get("verdict_rationale") or "") + " " + (r.get("blocker") or "")
        ad = parse_audit_date(r.get("audit_date"))
        helpers = r.get("helper_runner_paths") or []

        # ISS-1: orchestrator not consuming helper_runner_paths
        if helpers and ad and ad >= PIPELINE_FIX_LANDED:
            hit = search_patterns(rat, HELPER_MISSING_PATTERNS)
            if hit:
                iss1.append({"cid": cid, "audit_date": r.get("audit_date"),
                             "status": r.get("audit_status"), "helpers": helpers,
                             "signal": hit, "rationale": rat[:300]})

        # ISS-2: stale-numerics pattern (anytime, including pre-fix)
        if r.get("audit_status") in ("audited_failed", "audited_conditional"):
            hit = search_patterns(rat, STALE_NUMERICS_PATTERNS)
            if hit:
                iss2.append({"cid": cid, "audit_date": r.get("audit_date"),
                             "status": r.get("audit_status"),
                             "signal": hit, "rationale": rat[:200]})

        # ISS-3: hash drift orphan
        note_path = r.get("note_path")
        prior_hash = r.get("note_hash")
        if note_path and prior_hash:
            full = REPO_ROOT / note_path
            if full.exists():
                import hashlib
                cur_hash = hashlib.sha256(full.read_bytes()).hexdigest()
                if cur_hash != prior_hash and r.get("audit_status") and r.get("audit_status") != "unaudited":
                    iss3.append({"cid": cid, "note_path": note_path,
                                 "audit_status": r.get("audit_status")})

        # ISS-4: runner file missing
        rp = r.get("runner_path")
        if rp and not (REPO_ROOT / rp).exists() and r.get("audit_status") and r.get("audit_status") != "unaudited":
            iss4.append({"cid": cid, "runner_path": rp,
                         "audit_status": r.get("audit_status")})

    # Report
    section("ISS-1 — Orchestrator not consuming helper_runner_paths")
    print(f"  Count: {len(iss1)}")
    if iss1:
        print(f"  Definition: helpers populated in ledger AND audited after "
              f"pipeline-fix landed AND rationale cites missing-helper language.")
        print(f"  These prove the orchestrator (external Codex caller) is NOT")
        print(f"  reading helper_runner_paths when assembling packets.")
        print()
        for entry in iss1[:10]:
            print(f"  - {entry['cid']}")
            print(f"      audit_date: {entry['audit_date']}")
            print(f"      status:     {entry['status']}")
            print(f"      signal:     {entry['signal']!r}")
            print(f"      helpers:    {entry['helpers'][:3]}{'...' if len(entry['helpers']) > 3 else ''}")
            print(f"      rationale:  {entry['rationale'][:160]}")
            print()
        if len(iss1) > 10:
            print(f"  ... and {len(iss1) - 10} more")
    else:
        print("  None. Orchestrator integration appears complete.")

    section("ISS-2 — Stale-numerics pattern (note tables disagree with runner output)")
    print(f"  Count: {len(iss2)}")
    if iss2:
        print(f"  Definition: verdict rationale cites that source-note numerical")
        print(f"  tables disagree with current runner stdout. Mechanical fix:")
        print(f"  regen the note's tables from the current runner output.")
        print()
        for entry in iss2[:10]:
            print(f"  - {entry['cid']}  ({entry['status']})")
            print(f"      audit_date: {entry['audit_date']}")
            print(f"      signal:     {entry['signal']!r}")
            print(f"      rationale:  {entry['rationale'][:140]}")
            print()
        if len(iss2) > 10:
            print(f"  ... and {len(iss2) - 10} more")
    else:
        print("  None.")

    section("ISS-3 — Hash-drift orphans (note edited; ledger hash stale)")
    print(f"  Count: {len(iss3)}")
    if iss3:
        print(f"  Definition: audited row whose note_hash doesn't match the")
        print(f"  current source file. seed_audit_ledger.py would normally")
        print(f"  archive the prior audit and reset to unaudited; these rows")
        print(f"  are pending that reconciliation.")
        print()
        for entry in iss3[:10]:
            print(f"  - {entry['cid']}  ({entry['audit_status']})")
        if len(iss3) > 10:
            print(f"  ... and {len(iss3) - 10} more")
    else:
        print("  None. seed_audit_ledger.py is in sync with source notes.")

    section("ISS-4 — Audited rows whose declared runner file is missing on disk")
    print(f"  Count: {len(iss4)}")
    if iss4:
        print(f"  Definition: runner_path declared in ledger but file doesn't")
        print(f"  exist. The audit ran without runner source available.")
        print()
        for entry in iss4[:10]:
            print(f"  - {entry['cid']}  ({entry['audit_status']})")
            print(f"      missing runner: {entry['runner_path']}")
        if len(iss4) > 10:
            print(f"  ... and {len(iss4) - 10} more")
    else:
        print("  None.")

    # Summary
    banner("SUMMARY")
    print()
    print(f"  ISS-1 (orchestrator gap):        {len(iss1)}")
    print(f"  ISS-2 (stale numerics):           {len(iss2)}")
    print(f"  ISS-3 (hash-drift orphans):       {len(iss3)}")
    print(f"  ISS-4 (missing runner files):     {len(iss4)}")
    print()
    total_structural = len(iss1) + len(iss2) + len(iss3) + len(iss4)
    print(f"  Total structural-issue instances: {total_structural}")
    print()
    print("Re-run anytime to refresh:")
    print(f"  python3 {Path(__file__).relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
