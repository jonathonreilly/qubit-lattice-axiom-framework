#!/usr/bin/env python3
"""Live current-source packet for the grown-transfer basin repair."""

from __future__ import annotations

import sys
from pathlib import Path

import GROWN_TRANSFER_BASIN_SWEEP as _sweep_packet_source
import GROWN_TRANSFER_BASIN_TARGETED as _targeted_packet_source
import runner_cache as rc


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
PASS_COUNT = 0
FAIL_COUNT = 0
PACKET_SOURCE_MODULES = (_sweep_packet_source, _targeted_packet_source)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"[{status}] {name}")
    if detail:
        print(f"       {detail}")


def cache_text(runner: str) -> str:
    status = rc.cache_status(runner)
    cache_path, header, text = rc.load_cache(runner)
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


def contains(name: str, text: str, *needles: str) -> None:
    missing = [needle for needle in needles if needle not in text]
    check(name, not missing, "missing=" + repr(missing) if missing else "")


def main() -> int:
    print("=" * 96)
    print("GROWN TRANSFER BASIN LIVE PACKET")
    print("=" * 96)
    print("Verifies the repaired targeted and full narrow-basin cache reads.")
    print()

    targeted = cache_text("scripts/GROWN_TRANSFER_BASIN_TARGETED.py")
    sweep = cache_text("scripts/GROWN_TRANSFER_BASIN_SWEEP.py")

    contains(
        "targeted checker reports same-row survival on all four declared rows",
        targeted,
        "H=0.5, K=5.0, BETA=0.8, NL=25, PW=10, MAX_D_PHYS=3",
        "nearby rows surviving both observables: 4/4",
        "gamma=0.5 away-sign survivors require away_count == 3/3 and mean deflection < 0",
        "the prior grown-row positives survive on a narrow nearby basin",
        "(0, 3)    True    True  True",
    )
    contains(
        "full 3x3 sweep reports signed, complex, and same-row survival on all rows",
        sweep,
        "H=0.5, K=5.0, BETA=0.8, NL=25, PW=10, MAX_D_PHYS=3",
        "signed-source survivors: 9/9",
        "complex-action survivors: 9/9",
        "same-row survivors: 9/9",
        "gamma=0.5 away-sign survivors require away_count == 3/3 and mean deflection < 0",
        "narrow basin has rows surviving both observables",
    )
    contains(
        "repair note documents the predicate mismatch and current packet",
        (ROOT / "docs" / "GROWN_TRANSFER_BASIN_TARGETED_REPAIR_NOTE_2026-06-04.md").read_text(encoding="utf-8"),
        "Predicate Repair",
        "Post-audit compute repair",
        "complex_action_survives(row)",
        "away_count(gamma=0.5) == 3/3",
        "same-row intersection",
    )

    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("GROWN_TRANSFER_BASIN_LIVE_PACKET_ASSERTIONS=" + ("TRUE" if FAIL_COUNT == 0 else "FALSE"))
    print("GROWN_TRANSFER_BASIN_GRAPH_LADDER_THEOREM=FALSE")
    print("RESIDUAL_SCOPE=finite_row_grid_and_grown_geometry_helper_dependency")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
