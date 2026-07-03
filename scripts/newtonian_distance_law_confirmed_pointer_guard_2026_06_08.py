#!/usr/bin/env python3
"""Guard the historical Newtonian distance-law pointer repair.

The audited row is a historical pointer. The load-bearing replay evidence lives
in VALLEY_LINEAR_WIDE_TAIL_NOTE plus its frozen raw log and verifier cache.
This guard checks that the pointer row no longer relies on stale absolute paths
and exposes the SHA-pinned replay evidence.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "NEWTONIAN_DISTANCE_LAW_CONFIRMED.md"
REPLAY_NOTE = ROOT / "docs" / "VALLEY_LINEAR_WIDE_TAIL_NOTE.md"
RUNNER = ROOT / "scripts" / "valley_linear_wide_tail_replay.py"
FROZEN_LOG = ROOT / "logs" / "2026-04-04-valley-linear-wide-tail-replay.txt"
CACHE = ROOT / "logs" / "runner-cache" / "valley_linear_wide_tail_replay.txt"

EXPECTED_SHA = "2047f12a5143ac9501bacac31cc895fc278e47cf61372c8504d1ef1059a3d409"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {name}{suffix}")


def main() -> int:
    note = NOTE.read_text(encoding="utf-8")
    replay = REPLAY_NOTE.read_text(encoding="utf-8")
    cache = CACHE.read_text(encoding="utf-8")
    frozen = FROZEN_LOG.read_text(encoding="utf-8")

    print("NEWTONIAN DISTANCE-LAW HISTORICAL POINTER GUARD 2026-06-08")

    for path in (NOTE, REPLAY_NOTE, RUNNER, FROZEN_LOG, CACHE):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    check("pointer declares historical pointer status", "historical pointer note" in note)
    check("pointer has local replay note link", "(VALLEY_LINEAR_WIDE_TAIL_NOTE.md)" in note)
    check("pointer has local runner link", "(../scripts/valley_linear_wide_tail_replay.py)" in note)
    check("pointer has local frozen log link", "(../logs/2026-04-04-valley-linear-wide-tail-replay.txt)" in note)
    check("pointer has local cache link", "(../logs/runner-cache/valley_linear_wide_tail_replay.txt)" in note)
    check("pointer removes stale absolute project paths", "/Users/jonreilly/Projects/Physics" not in note)
    check("pointer exposes frozen log sha", EXPECTED_SHA in note)
    check("pointer states bounded finite replay only", "not, by itself, a universal theorem" in note)
    check("replay note contains verifier repair", "2026-06-07 verifier repair" in replay)
    check("replay note exposes same frozen sha", EXPECTED_SHA in replay)
    check(
        "cache is fresh successful verifier",
        "VALLEY-LINEAR WIDE-TAIL FROZEN LOG VERIFIER" in cache
        and "SCORECARD PASS=9 FAIL=0" in cache,
    )
    check("pointer contains raw-row inventory repair", "Raw-row inventory for strict formula review" in note)
    rows = re.findall(
        r"^\s+z=\s*(\d+)\s+delta=([+-]\d+\.\d+)\s+(TOWARD|AWAY)\s*$",
        frozen,
        re.MULTILINE,
    )
    check("frozen log has nine raw distance rows", len(rows) == 9, f"rows={len(rows)}")
    check(
        "pointer includes all raw distance rows",
        len(rows) == 9
        and all(
            f"| `{int(z)}` | `{float(delta):+0.6f}` | `{direction}` |" in note
            for z, delta, direction in rows
        ),
        "all parsed z/delta/direction rows are present in pointer table",
    )
    check("pointer records recomputed far-tail fit", "slope `-1.1685`" in note and "R^2 = 0.9972" in note)

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
