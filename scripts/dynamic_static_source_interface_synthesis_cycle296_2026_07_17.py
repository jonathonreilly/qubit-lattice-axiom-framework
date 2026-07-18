#!/usr/bin/env python3
"""Cycle 296 synthesis for dynamic, stationary, and interface source probes.

Cold-run three independent artifacts and pin the fact that the exact local
dictionary does not transfer the fixed-defect stationary theorem to the moving
source update without an additional stream law.
"""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "DYNAMIC_STATIC_SOURCE_INTERFACE_SYNTHESIS_CYCLE296_NOTE_2026-07-17.md"
)

ROUTES = (
    (
        "moving carried history",
        ROOT / "scripts/carried_source_retarded_lattice_execution_2026_07_17.py",
        13,
        re.compile(r"TOTAL\s+PASS=(\d+)\s+FAIL=(\d+)"),
    ),
    (
        "fixed-reservoir stationary profile",
        ROOT / "scripts/stationary_dressed_reservoir_shifted_green_profile_2026_07_17.py",
        17,
        re.compile(r"SUMMARY\s+PASS\s+(\d+)\s+FAIL\s+(\d+)"),
    ),
    (
        "carried/site interface",
        ROOT / "scripts/carried_site_reservoir_interface_mapping_2026_07_17.py",
        13,
        re.compile(r"TOTAL\s+PASS=(\d+)\s+FAIL=(\d+)"),
    ),
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "delayed colocated recontact",
        "shifted-resolvent",
        "exact local dictionary",
        "fixed reservoir",
        "co-moving repair",
        "staggered catch-up",
        "conditional transposition",
        "norm-preserving involution",
        "not one common source/response theorem",
        "not physical energy",
        "not gravity",
        "no contact gate",
        "c_ref",
        "c_num",
        "c_wrap",
        "c_int",
        "c_local",
        "c_source",
        "n1 — alternative routes",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the synthesis pins route boundaries, ledgers, and N1--N8", not missing, missing)


def cold_routes() -> None:
    rows = []
    for name, path, expected_pass, pattern in ROUTES:
        completed = subprocess.run(
            [sys.executable, str(path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        match = pattern.search(completed.stdout)
        observed = tuple(int(item) for item in match.groups()) if match else None
        rows.append(
            {
                "route": name,
                "returncode": completed.returncode,
                "observed": observed,
                "expected": (expected_pass, 0),
            }
        )
    check(
        "all three independent route runners pass at reviewed totals",
        all(
            row["returncode"] == 0 and row["observed"] == row["expected"]
            for row in rows
        ),
        rows,
    )


def interface_guards() -> None:
    moving = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "CARRIED_SOURCE_RETARDED_LATTICE_EXECUTION_NOTE_2026-07-17.md"
    )
    stationary = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "STATIONARY_DRESSED_RESERVOIR_SHIFTED_GREEN_PROFILE_NOTE_2026-07-17.md"
    )
    interface = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "CARRIED_SITE_RESERVOIR_INTERFACE_MAPPING_NOTE_2026-07-17.md"
    )
    check(
        "the moving history is path-honest and applies no contact layer",
        "no path provenance" in moving and "no contact layer is applied" in moving,
    )
    check(
        "the stationary theorem excludes matter, contact, and a carried-source interface",
        "no matter or contact update is implemented" in stationary
        and "there is no interface to the carried-source code" in stationary,
    )
    check(
        "the interface distinguishes fixed-stream mismatch from repaired macrosteps",
        "fixed-reservoir full stream: mismatch" in interface
        and "co-moving repair: pass exactly" in interface
        and "staggered catch-up repair: pass" in interface
        and "norm-preserving involution" in interface
        and "staggered inverse residual" in interface,
    )


def main() -> int:
    note_contract()
    cold_routes()
    interface_guards()
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
