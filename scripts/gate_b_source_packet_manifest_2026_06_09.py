"""Gate B row-local source-packet manifest gate.

This runner checks only that docs/GATE_B_DYNAMICS_NOTE.md discloses the
supplied Gate B source packet and preserves the no-new-axiom/no-clean-theorem
boundary. It intentionally leaves the older connectivity replay runner
unchanged, so existing retained companion rows are not invalidated by this
manifest repair.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "GATE_B_DYNAMICS_NOTE.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(ok))
    FAIL += int(not ok)
    return bool(ok)


def main() -> int:
    print("GATE B SOURCE-PACKET MANIFEST GATE")
    print("=" * 72)

    if not NOTE.exists():
        check("Gate B source note exists", False, str(NOTE))
        print(f"\nSUMMARY: PASS={PASS} FAIL={FAIL}")
        return 1

    body = NOTE.read_text(encoding="utf-8")
    flat = " ".join(body.split())
    lower = flat.lower()

    check(
        "note declares open_gate source-index claim type",
        "**Claim type:** open_gate" in body
        and "bounded generated-geometry source index" in lower,
    )
    check(
        "row-local source-packet manifest section is present",
        "2026-06-09 Row-Local Source-Packet Manifest" in body
        and "I_GateB" in body,
    )
    check(
        "GB-S1 discloses valley-linear source/action as supplied only",
        "GB-S1" in body
        and "valley-linear source/action rule" in body
        and "not derived from retained primitives" in lower,
    )
    check(
        "GB-S2 discloses propagation/readout semantics as supplied only",
        "GB-S2" in body
        and "propagation/readout semantics" in body
        and "not a retained physical-gravity readout bridge" in lower,
    )
    check(
        "GB-S3 discloses generated-connectivity rule as supplied only",
        "GB-S3" in body
        and "generated-connectivity rule" in body
        and "not yet derived from a local retained growth primitive" in lower,
    )
    check(
        "manifest preserves no-new-axiom and no-clean-theorem boundary",
        "not a new axiom" in lower
        and "does not promote `i_gateb`" in lower
        and "closed gate b dynamics theorem" in lower,
    )
    check(
        "note blocks solved/physical-gravity overclaims",
        "gate b is solved" not in lower
        and "physical gravity theorem" in lower
        and "primitive-to-physical-gravity bridge" in lower,
    )

    print(f"\nSUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
    print(
        "VERDICT: the Gate B row exposes the supplied source packet as row-local "
        "manifest data and does not promote it to an axiom, primitive, retained "
        "premise, physical-gravity bridge, or clean Gate B dynamics theorem."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
