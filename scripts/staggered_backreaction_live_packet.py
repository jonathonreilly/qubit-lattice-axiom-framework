#!/usr/bin/env python3
"""Current-source packet for the staggered-backreaction stale-runner rows.

The archived staggered-backreaction notes failed because their frozen tables
drifted away from the live runners. This wrapper does not recompute new
physics; it asserts the current cached runner facts that the live replacement
notes cite, and keeps the boundary narrower than the archived claims.
"""

from __future__ import annotations

import sys
from pathlib import Path

import runner_cache as rc


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"[{status}] {name}")
    if detail:
        for line in detail.splitlines():
            print(f"       {line}")


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


def require(name: str, text: str, *needles: str) -> None:
    missing = [needle for needle in needles if needle not in text]
    check(name, not missing, "missing=" + repr(missing) if missing else "")


def main() -> int:
    print("=" * 104)
    print("STAGGERED BACKREACTION LIVE PACKET")
    print("=" * 104)
    print("Checks current cached facts for the six stale-runner replacement notes.")
    print()

    prototype = cache_text("scripts/frontier_staggered_backreaction_prototype.py")
    iterative = cache_text("scripts/frontier_staggered_backreaction_iterative.py")
    scale = cache_text("scripts/frontier_staggered_backreaction_scale_closure.py")
    nonlocal_ = cache_text("scripts/frontier_staggered_backreaction_nonlocal_closure.py")
    green = cache_text("scripts/frontier_staggered_backreaction_green_closure.py")
    capture = cache_text("scripts/frontier_staggered_backreaction_capture_closure_harness.py")

    require(
        "prototype live boundary: exact controls survive but cycle-row linearity is weak",
        prototype,
        "source-response linearity: 1/3 families R^2 > 0.99",
        "force gap (external vs solved): mean=9.353e-01",
        "one-step endogenous backreaction: 3/3 families TOWARD",
    )
    require(
        "iterative source-mapping live boundary: invheat_b3p00 is best but self-gap explodes",
        iterative,
        "best cycle-bearing mean gap: 4.314e-01 (invheat_b3p00)",
        "gap improvement factor: 2.23x",
        "best-map self-gap mean: 1.581e+01",
    )
    require(
        "scale-closure live boundary: weaker calibrated cycle reduction with holdout blow-up",
        scale,
        "best cycle-bearing mean gap: 2.053e-01 (invheat_b3p00, gain=0.621)",
        "improvement factor: 4.69x",
        "best holdout gap: 7.249e+00",
    )
    require(
        "nonlocal closure live boundary: alpha=0.40 improves cycle rows but not the holdout",
        nonlocal_,
        "baseline calibrated linear cycle gap: 3.881e-02 (alpha=1.00, gain=16.000)",
        "best calibrated cycle gap: 1.620e-02 (alpha=0.40, gain=16.000)",
        "best holdout gap (layered): 7.035e-01",
        "shell_fit_R2=0.7857",
    )
    require(
        "green closure live boundary: resistance_yukawa is the best current map with calibrated holdout caveat",
        green,
        "promoted cycle-bearing mean gap: 3.425e-01 (resistance_yukawa, raw)",
        "raw improvement factor: 2.81x",
        "promoted holdout gap: 1.534e-02",
        "resistance_yukawa",
        "5.371e-01",
    )
    require(
        "capture closure live boundary: 9/9 cycle batteries and about 2x force-gap improvement",
        capture,
        "cycle battery scores: [9, 9]",
        "cycle mean gap: 9.828e-01 -> 4.734e-01",
        "cycle gap improvement factor: 2.08x",
        "holdout gap: 9.191e-01 -> 4.559e-01 (2.02x)",
    )

    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("STAGGERED_BACKREACTION_LIVE_PACKET_ASSERTIONS=" + ("TRUE" if FAIL_COUNT == 0 else "FALSE"))
    print("STAGGERED_BACKREACTION_FULL_SELF_GRAVITY_CLOSURE=FALSE")
    print("RESIDUAL_SCOPE=universal_source_to_field_scale_and_endogenous_self_refresh")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
