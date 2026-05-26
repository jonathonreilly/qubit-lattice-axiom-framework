#!/usr/bin/env python3
"""Fast certificate for the cached Gate B far-field harness output."""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/GATE_B_FARFIELD_NOTE.md"
CACHE = REPO_ROOT / "logs/runner-cache/gate_b_farfield_harness.txt"
LEDGER = REPO_ROOT / "docs/audit/data/audit_ledger.json"
QUEUE = REPO_ROOT / "docs/audit/data/audit_queue.json"

CLAIM_ID = "gate_b_farfield_note"
RUNNER_PATH = "scripts/gate_b_farfield_harness.py"

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
        "not a physical Gate B bridge theorem",
        "36/36",
        "does not claim",
        "any new axiom or audit verdict",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in text)

    forbidden = [
        "/Users/jonreilly/Projects/Physics",
        "conditional numerical certificate over the admitted bridge inputs",
        "clean Gate B far-field propagation",
        "audited_conditional",
        "primitive-to-physical-gravity bridge is recorded as the upstream D-class",
    ]
    for phrase in forbidden:
        check(f"note omits stale bridge phrase: {phrase}", phrase not in text)


def cache_checks() -> None:
    cache = CACHE.read_text(encoding="utf-8")
    print("\n=== Gate B far-field cached harness ===")
    check("cache runner path matches harness", "runner: scripts/gate_b_farfield_harness.py" in cache)
    check("cache exit code is zero", "exit_code: 0" in cache)
    check("cache status is ok", "status: ok" in cache)
    check("cache declares h=0.5 family", "h=0.5, W=8, NL=25, 12 seeds, z_masses=[3, 4, 5]" in cache)

    row_re = re.compile(
        r"^\s+(?P<label>drift=\d\.\d,rest=\d\.\d|exact grid)\s+:\s+"
        r"(?P<toward>\d+)/(?P<total>\d+) TOWARD \((?P<pct>\d+)%\), F~M=(?P<fm>\d+\.\d+)",
        re.MULTILINE,
    )
    rows = [m.groupdict() for m in row_re.finditer(cache)]
    labels = [row["label"] for row in rows]
    expected = ["drift=0.3,rest=0.5", "drift=0.2,rest=0.7", "drift=0.1,rest=0.9", "exact grid"]
    check("all four declared rows parsed", labels == expected, str(labels))
    check("each row has 36 tests", all(int(row["total"]) == 36 for row in rows), str([row["total"] for row in rows]))
    check("each row is 36/36 TOWARD", all(int(row["toward"]) == 36 for row in rows), str([row["toward"] for row in rows]), kind="C")
    check("each row reports 100 percent TOWARD", all(int(row["pct"]) == 100 for row in rows), str([row["pct"] for row in rows]), kind="C")
    check("each row reports F~M=1.00", all(abs(float(row["fm"]) - 1.0) <= 1e-12 for row in rows), str([row["fm"] for row in rows]), kind="C")


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
    check("no open dependency paths remain", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))
    check("queue marks row ready", queue_entry.get("ready") is True, str(queue_entry.get("ready")))
    check("descendant chain remains material", int(row.get("transitive_descendants") or 0) >= 100, str(row.get("transitive_descendants")), kind="B")


def main() -> int:
    note_boundary_checks()
    cache_checks()
    audit_metadata_checks()
    print("\nGate B far-field cached certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
