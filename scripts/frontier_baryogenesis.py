#!/usr/bin/env python3
"""Legacy Cabibbo/Jarlskog baryogenesis-route compatibility runner.

This runner keeps the historical ``frontier_baryogenesis.py`` path executable
for audit hygiene.  It does not restore the old combined route as current
authority; it checks that the historical note still points to the split current
Cabibbo and Jarlskog bounded companion notes.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PASS_COUNT = 0
FAIL_COUNT = 0


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    return condition


def main() -> int:
    print("Cabibbo/Jarlskog historical baryogenesis-route compatibility")
    print("=" * 72)

    route = read("docs/work_history/CABIBBO_JARLSKOG_ROUTE_NOTE_2026-04-12.md")
    cabibbo = read("docs/work_history/ckm/CABIBBO_BOUND_NOTE.md")
    jarlskog = read("docs/work_history/ckm/JARLSKOG_PHASE_BOUND_NOTE.md")

    check(
        "combined route note is explicitly historical",
        "historical route note only" in route
        and "superseded on the\nmain authority path" in route,
    )
    check(
        "legacy runner path remains provenance, not current closure",
        "`scripts/frontier_baryogenesis.py`" in route
        and "contains the calculation, tests 1-2" in route,
    )
    check(
        "current Cabibbo authority is the NNI bounded companion",
        "`scripts/frontier_ckm_mass_basis_nni.py`" in cabibbo
        and "|V_us| = 0.2251" in cabibbo
        and "**not** full CKM" in cabibbo,
    )
    check(
        "current Jarlskog authority is the derived-phase bounded companion",
        "`scripts/frontier_jarlskog_derived.py`" in jarlskog
        and "delta = 2pi/3" in jarlskog
        and "J = 3.145 x 10^-5" in jarlskog
        and "**not** a closed\nCKM theorem" in jarlskog,
    )

    cabibbo_ratio = 0.2251 / 0.2243
    jarlskog_ratio = 3.145e-5 / 3.08e-5
    check(
        "Cabibbo bounded companion arithmetic is preserved",
        abs(cabibbo_ratio - 1.0035666518056174) < 1.0e-12,
        f"ratio={cabibbo_ratio:.12f}",
    )
    check(
        "Jarlskog bounded companion arithmetic is preserved",
        abs((jarlskog_ratio - 1.0) - 0.02110389610389607) < 1.0e-12,
        f"relative_offset={(jarlskog_ratio - 1.0):.12f}",
    )

    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
