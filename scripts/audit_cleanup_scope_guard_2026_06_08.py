#!/usr/bin/env python3
"""Guard the 2026-06-08 audit cleanup safe narrows."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NEWTON = ROOT / "docs" / "NEWTONIAN_DISTANCE_LAW_CONFIRMED.md"
GATE_B = ROOT / "docs" / "GATE_B_DYNAMICS_NOTE.md"
MESO = ROOT / "docs" / "MESOSCOPIC_SURROGATE_ALTERNATE_FAMILY_SCOUT_NOTE.md"
ORDERED = ROOT / "docs" / "lanes" / "ordered-lattice" / "README.md"

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
    newton = NEWTON.read_text(encoding="utf-8")
    gate_b = GATE_B.read_text(encoding="utf-8")
    meso = MESO.read_text(encoding="utf-8")
    ordered = ORDERED.read_text(encoding="utf-8")

    print("AUDIT CLEANUP SCOPE GUARD 2026-06-08")

    for path in (NEWTON, GATE_B, MESO, ORDERED):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    check("newton pointer is historical only", "historical pointer note" in newton)
    check("newton pointer exposes cache", "logs/runner-cache/valley_linear_wide_tail_replay.txt" in newton)
    check("newton pointer exposes SHA", "2047f12a5143ac9501bacac31cc895fc278e47cf61372c8504d1ef1059a3d409" in newton)

    check("Gate B declares generated-geometry index", "bounded generated-geometry source index" in gate_b)
    check("Gate B denies physical bridge", "not a physical-gravity or" in gate_b)
    check("Gate B names runner-local slice semantics", "runner-local far-field slice" in gate_b)
    check("Gate B removes bold CLOSED overclaim", "**Gate B far-field: CLOSED.**" not in gate_b)
    check("Gate B removes stale absolute project paths", "/Users/jonreilly/Projects/Physics" not in gate_b)

    check("mesoscopic scout is meta/support index", "meta/support planning index" in meso)
    check(
        "mesoscopic scout denies theorem-grade target selection",
        "must not be used as a" in meso and "bounded theorem for target selection" in meso,
    )
    check("mesoscopic scout preserves ranking residual", "registered objective ranking criterion" in meso)

    check("ordered README declares meta index", "historical lane index / meta" in ordered)
    check("ordered README denies authority surface", "not an authority surface" in ordered)
    check("ordered README preserves per-note status", "per-note audit status" in ordered)

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
