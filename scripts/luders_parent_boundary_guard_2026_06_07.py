#!/usr/bin/env python3
"""Boundary guard for the Lueders parent note.

This runner verifies that the parent Lueders note does not launder the
finite PEP compression bridge into a framework-native measurement update,
Born rule, or trace-probability derivation.
"""

from pathlib import Path


PASS = 0
FAIL = 0


ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT / "docs/LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md"
BRIDGE = ROOT / "docs/LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def main() -> int:
    parent = PARENT.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")

    print("LUEDERS PARENT BOUNDARY GUARD 2026-06-07")

    check("parent note exists", PARENT.exists(), str(PARENT.relative_to(ROOT)))
    check("PEP bridge note exists", BRIDGE.exists(), str(BRIDGE.relative_to(ROOT)))
    check(
        "parent declares conditional Lueders support boundary",
        "conditional bounded_theorem candidate" in parent
        or "conditional-support assembly over exact finite subclaims" in parent,
    )
    check("parent states trace/effect probability is measurement-side premise", "trace/effect probability interpretation" in parent and "measurement-side premise" in parent)
    check("parent states bridge supplies PEP compression algebra", "`P E P` compression" in parent or "`M_{P,E}=PEP` compression" in parent)
    check("parent states bridge does not supply Born/update semantics", "does not by itself supply the Born rule" in parent)
    check("parent preserves positive-probability domain", "Zero-probability conditioning events are excluded" in parent)
    check("parent names the 2026-06-07 repair section", "2026-06-07 Parent-Boundary Repair" in parent)
    check("parent keeps Born note downstream, not upstream", "Born note is a downstream consumer" in parent)
    check("parent says full Born closure remains conditional", "Full closure of the Born row remains" in parent)
    check("bridge boundary says it does not derive Lueders/Born", "does not obtain the Lüders state update, Born rule" in bridge)
    check(
        "parent explicitly denies trace-probability/instrument derivation",
        "trace/effect probability" in parent
        and "measurement instruments" in parent
        and "does not by itself supply the Born rule" in parent,
    )

    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
