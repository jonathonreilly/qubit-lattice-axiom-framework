#!/usr/bin/env python3
"""
Current second-grown-family battery verifier.

The archived `SECOND_GROWN_FAMILY_NOTE.md` named this script, but the file was
absent.  The old note's broad positive table should not be revived blindly:
current main carries the second-family evidence through separate, auditable
sign, distance/impact, and complex-action packets.

This runner restores the missing executable path as an audit packet verifier:
it checks the current source/caches that actually carry the evidence and keeps
the boundary honest.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import DISTANCE_LAW_BREAKPOINT_COMPARE as distance_law_source
import SECOND_GROWN_FAMILY_COMPLEX as complex_full_source
import SECOND_GROWN_FAMILY_COMPLEX_QUICK as complex_quick_source
import SECOND_GROWN_FAMILY_SIGN_SWEEP as sign_sweep_source
import impact_parameter_portability_probe as impact_source
import runner_cache as rc


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0

SOURCE_MODULES = {
    "scripts/SECOND_GROWN_FAMILY_SIGN_SWEEP.py": sign_sweep_source,
    "scripts/SECOND_GROWN_FAMILY_COMPLEX.py": complex_full_source,
    "scripts/SECOND_GROWN_FAMILY_COMPLEX_QUICK.py": complex_quick_source,
    "scripts/DISTANCE_LAW_BREAKPOINT_COMPARE.py": distance_law_source,
    "scripts/impact_parameter_portability_probe.py": impact_source,
}
EXPECTED_PASS_COUNT_BEFORE_FINAL = len(SOURCE_MODULES) * 3 + 5


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


def cache_text(runner: str) -> str:
    status = rc.cache_status(runner)
    cache_path, header, text = rc.load_cache(runner)
    runner_path = ROOT / runner
    module = SOURCE_MODULES[runner]
    module_path = Path(module.__file__).resolve()
    check(
        f"{runner} source is imported into this restricted packet",
        module_path == runner_path.resolve(),
        f"module={module_path.relative_to(ROOT)}, expected={runner}",
    )
    live_sha = hashlib.sha256(runner_path.read_bytes()).hexdigest() if runner_path.is_file() else None
    header_sha = str(header.get("runner_sha256")) if header is not None else None
    source_ok = runner_path.is_file() and live_sha == header_sha
    check(
        f"{runner} source exists and matches cache SHA",
        source_ok,
        f"source={runner_path.relative_to(ROOT)}, live_sha={live_sha}, cache_sha={header_sha}",
    )
    ok = (
        status == "fresh"
        and header is not None
        and header.get("status") == "ok"
        and str(header.get("exit_code")) == "0"
        and text is not None
    )
    check(
        f"{runner} has a fresh ok cache",
        ok,
        f"cache={cache_path.relative_to(ROOT)}, status={status}, header={header}",
    )
    return text or ""


def contains(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    print("=" * 104)
    print("SECOND GROWN FAMILY CURRENT BATTERY VERIFIER")
    print("=" * 104)
    print()
    print("Question:")
    print("  Does current main contain an auditable replacement battery for the")
    print("  archived second-grown-family missing-runner row?")
    print()

    archived = (ROOT / "archive_unlanded/grown-family-missing-artifacts-2026-04-30/SECOND_GROWN_FAMILY_NOTE.md").read_text()
    sign = cache_text("scripts/SECOND_GROWN_FAMILY_SIGN_SWEEP.py")
    complex_full = cache_text("scripts/SECOND_GROWN_FAMILY_COMPLEX.py")
    complex_quick = cache_text("scripts/SECOND_GROWN_FAMILY_COMPLEX_QUICK.py")
    distance = cache_text("scripts/DISTANCE_LAW_BREAKPOINT_COMPARE.py")
    impact = cache_text("scripts/impact_parameter_portability_probe.py")

    print()
    print("Current evidence packet:")
    print("  sign slice: no-restore geometry-sector second-family sweep")
    print("  distance/impact slice: restored Fam2 row at drift=0.05, restore=0.30")
    print("  complex slice: narrow no-restore anchor-row pass plus quick-window boundary")
    print()

    check(
        "Archived audit blocker names this missing battery path and allows replacement by audit-clean sign/complex notes",
        "scripts/second_grown_family_battery.py" in archived
        and "replace this note with audit-clean sign/complex second-family notes" in archived,
    )
    check(
        "The current sign packet has a complete passing sweep on the no-restore second-family slice",
        contains(sign, "passed rows: 15/15", "drift coverage: [0.0, 0.1, 0.2, 0.3, 0.5]", "mean charge exponent among passes: 1.000072"),
    )
    check(
        "The restored Fam2 distance/impact packet carries the drift=0.05, restore=0.30 distance law evidence",
        contains(distance, "Grown family 2 | drift=0.05, restore=0.30", "-0.947", "5/5 TOWARD", "preserve")
        and contains(impact, "grown family 2", "null control @ b=8: delta=+0.000000e+00", "fit: delta ~= C * b^-0.947", "retained law: grown family 1, grown family 2"),
    )
    check(
        "The current complex packet has an executable narrow anchor-row positive check",
        contains(complex_full, "anchor retained gamma=0 + Born proxy: PASS", "anchor TOWARD@0.1 -> AWAY@0.5: PASS", "OVERALL: PASS"),
    )
    check(
        "The quick complex packet exposes the boundary rather than inflating the result family-wide",
        contains(complex_quick, "anchor retained gamma=0 + Born proxy: True", "anchor TOWARD@0.1 -> AWAY@0.5: False", "does not retain the complex-action companion cleanly"),
    )
    check(
        "Therefore the missing battery path is restored as a current evidence verifier, not as a resurrection of the old broad table",
        PASS_COUNT == EXPECTED_PASS_COUNT_BEFORE_FINAL and FAIL_COUNT == 0,
        (
            f"expected {EXPECTED_PASS_COUNT_BEFORE_FINAL} prior checks before final "
            f"gate; legacy broad status remains for independent audit to decide"
        ),
    )

    print("\n" + "=" * 104)
    print("RESULT")
    print("=" * 104)
    print("  Current-source battery restored:")
    print("    - the missing runner path now exists")
    print("    - it verifies fresh caches for the current sign, distance/impact, and")
    print("      complex second-family evidence")
    print("    - it keeps the complex-action result narrow and boundary-aware")
    print("    - it does not edit audit results or claim ledger status movement")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
