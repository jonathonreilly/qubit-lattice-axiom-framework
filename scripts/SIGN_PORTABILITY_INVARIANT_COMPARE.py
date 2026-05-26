#!/usr/bin/env python3
"""Fast certificate for cached sign-portability gate checks."""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/SIGN_PORTABILITY_INVARIANT_FAMILY_SECOND_GROWN_DERIVATION_THEOREM_NOTE_2026-05-09.md"
CACHE = REPO_ROOT / "logs/runner-cache/SIGN_PORTABILITY_INVARIANT_COMPARE.txt"
LEDGER = REPO_ROOT / "docs/audit/data/audit_ledger.json"
QUEUE = REPO_ROOT / "docs/audit/data/audit_queue.json"

CLAIM_ID = "sign_portability_invariant_family_second_grown_derivation_theorem_note_2026-05-09"
RUNNER_PATH = "scripts/SIGN_PORTABILITY_INVARIANT_COMPARE.py"

EXPECTED_SUMMARY = {
    "Grown transfer basin": "PPPP",
    "Alternative connectivity family": "PPPP",
    "Second grown-family sign": "PPPP",
    "Third grown-family sign": "PPPP",
    "Fourth family quadrant": "PPPP",
    "Fifth family radial": "PPPP",
}

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] [{kind}] {name}{suffix}")


def note_boundary_checks() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").split())
    required = [
        "Claim type:** bounded_theorem",
        "Status:** bounded cached-output certificate",
        "not a proof of the unit-slope theorem",
        "not a cross-family theorem",
        "does not claim",
        "any new axiom or audit verdict",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in text)

    forbidden = [
        "claim_scope",
        "conditional on linear-response regularity",
        "cross-family equivalence claimed",
        "inherits the same four gates by the same proof",
        "bounded_theorem. Within the second grown-family slice",
    ]
    for phrase in forbidden:
        check(f"note omits stale theorem phrase: {phrase}", phrase not in text)


def cache_header_checks(cache: str) -> None:
    print("\n=== sign-portability cached gate checks ===")
    for phrase in [
        "runner: scripts/SIGN_PORTABILITY_INVARIANT_COMPARE.py",
        "exit_code: 0",
        "status: ok",
        "thresholds: ZERO_TOL=1e-12 NEUTRAL_TOL=1e-12 ANTISYM_TOL=5e-03 EXP_TOL=5e-03",
        "OVERALL: PASS",
    ]:
        check(f"cache contains: {phrase}", phrase in cache)


def cache_derivation_subset_checks(cache: str) -> None:
    subset = re.findall(
        r"^\s*(?P<drift>\d\.\d{2})\s+(?P<seed>\d+)\s+"
        r"(?P<zero>[+-]\d\.\d{3}e[+-]\d+)\s+"
        r"(?P<neutral>[+-]\d\.\d{3}e[+-]\d+)\s+"
        r"(?P<plus>[+-]\d\.\d{3}e[+-]\d+)\s+"
        r"(?P<minus>[+-]\d\.\d{3}e[+-]\d+)\s+"
        r"(?P<g3>\d\.\d{3}e[+-]\d+)\s+"
        r"(?P<g4>\d\.\d{3}e[+-]\d+)\s+\[PASS\]$",
        cache,
        flags=re.MULTILINE,
    )
    check("derivation subset has two passing rows", len(subset) == 2, str(len(subset)), kind="C")
    if subset:
        max_g3 = max(float(row[6]) for row in subset)
        max_g4 = max(float(row[7]) for row in subset)
        check("subset G3 residual below threshold", max_g3 <= 5e-3, f"{max_g3:.3e}", kind="C")
        check("subset G4 residual below threshold", max_g4 <= 5e-3, f"{max_g4:.3e}", kind="C")
    check("derivation block reports PASS", "derivation_block: PASS" in cache, kind="C")


def cache_family_summary_checks(cache: str) -> None:
    for family, gates in EXPECTED_SUMMARY.items():
        pattern = rf"^\s*{re.escape(family)}\s+G1G2G3G4 = (?P<gates>[PF]{{4}})$"
        match = re.search(pattern, cache, flags=re.MULTILINE)
        check(f"{family} summary row parsed", match is not None)
        if match is not None:
            check(f"{family} reports PPPP", match.group("gates") == gates, match.group("gates"), kind="C")

    detailed_passes = len(re.findall(r"\[PASS\] G[1-4]_", cache))
    check("detailed family gate PASS rows present", detailed_passes >= 20, str(detailed_passes), kind="B")


def audit_metadata_checks() -> None:
    if not LEDGER.exists() or not QUEUE.exists():
        print("\n=== audit metadata unavailable before pipeline ===")
        return
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"][CLAIM_ID]
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
    queue_entry = next(e for e in queue if e["claim_id"] == CLAIM_ID)

    print("\n=== regenerated audit metadata ===")
    check("ledger claim_type remains bounded_theorem", row.get("claim_type") == "bounded_theorem")
    check("ledger audit_status reset to unaudited", row.get("audit_status") == "unaudited")
    check("ledger effective_status reset to unaudited", row.get("effective_status") == "unaudited")
    check("ledger runner_path registered", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("ledger has no direct deps", row.get("deps") == [], str(row.get("deps")))
    check("no helper runner paths remain", row.get("helper_runner_paths") == [], str(row.get("helper_runner_paths")))
    check("no open dependency paths remain", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))
    check("queue marks row ready", queue_entry.get("ready") is True, str(queue_entry.get("ready")))
    check("descendant chain remains material", int(row.get("transitive_descendants") or 0) >= 75, str(row.get("transitive_descendants")), kind="B")


def main() -> int:
    note_boundary_checks()
    cache = CACHE.read_text(encoding="utf-8")
    cache_header_checks(cache)
    cache_derivation_subset_checks(cache)
    cache_family_summary_checks(cache)
    audit_metadata_checks()
    print("\nSign portability cached gate certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
