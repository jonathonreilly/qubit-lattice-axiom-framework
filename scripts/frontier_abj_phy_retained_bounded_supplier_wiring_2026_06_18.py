#!/usr/bin/env python3
"""Exact formal trace arithmetic for the narrowed ABJ packet boundary.

All multiplicities, eigenvalues, and representation indices below are supplied
formal data.  This module neither reads mutable audit state nor infers a
physical P-HY/hypercharge identification.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Callable


PASS = 0
FAIL = 0


class PacketMismatch(ValueError):
    """Raised when a changed trace packet is presented as the stated packet."""


class PhysicalInference(ValueError):
    """Raised when formal traces are asked to supply physical semantics."""


@dataclass(frozen=True)
class FormalEntry:
    label: str
    weak_multiplicity: int
    color_multiplicity: int
    y: Fraction
    color_quadratic_index: Fraction
    color_cubic_index: Fraction


PACKET = (
    FormalEntry("A", 2, 3, Fraction(1, 3), Fraction(1, 2), Fraction(1)),
    FormalEntry("B", 2, 1, Fraction(-1), Fraction(0), Fraction(0)),
)
WEAK_QUADRATIC_INDEX = Fraction(1, 2)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: [A] {name}{suffix}")


def trace_packet(
    packet: tuple[FormalEntry, ...],
) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction]:
    tr_y = sum(
        entry.weak_multiplicity * entry.color_multiplicity * entry.y
        for entry in packet
    )
    tr_y3 = sum(
        entry.weak_multiplicity * entry.color_multiplicity * entry.y**3
        for entry in packet
    )
    tr_color2_y = sum(
        entry.weak_multiplicity * entry.color_quadratic_index * entry.y
        for entry in packet
    )
    tr_weak2_y = sum(
        entry.color_multiplicity * WEAK_QUADRATIC_INDEX * entry.y
        for entry in packet
    )
    tr_color3 = sum(
        entry.weak_multiplicity * entry.color_cubic_index for entry in packet
    )
    return tr_y, tr_y3, tr_color2_y, tr_weak2_y, tr_color3


def validate_packet(packet: tuple[FormalEntry, ...]) -> None:
    if packet != PACKET:
        raise PacketMismatch("multiplicity, eigenvalue, or index packet changed")


def infer_physical_hypercharge(
    traces: tuple[Fraction, Fraction, Fraction, Fraction, Fraction],
) -> None:
    raise PhysicalInference(
        f"formal traces {traces!r} do not identify a physical U(1)_Y readout"
    )


def expect_rejection(
    name: str, exception_type: type[Exception], operation: Callable[[], object]
) -> None:
    caught: Exception | None = None
    try:
        operation()
    except Exception as exc:  # the exact type is checked below
        caught = exc
    detail = str(caught) if caught is not None else "mutation was incorrectly accepted"
    check(name, isinstance(caught, exception_type), detail)


def main() -> int:
    print("ABJ FORMAL LEFT-HANDED TRACE ARITHMETIC")
    traces = trace_packet(PACKET)
    tr_y, tr_y3, tr_color2_y, tr_weak2_y, tr_color3 = traces
    check("Tr[y] is zero", tr_y == Fraction(0), str(tr_y))
    check("Tr[y^3] is -16/9", tr_y3 == Fraction(-16, 9), str(tr_y3))
    check("Tr[C2*y] is 1/3", tr_color2_y == Fraction(1, 3), str(tr_color2_y))
    check("Tr[W2*y] is zero", tr_weak2_y == Fraction(0), str(tr_weak2_y))
    check("Tr[C3] is 2", tr_color3 == Fraction(2), str(tr_color3))

    reversed_cubic = FormalEntry(
        "Abar", 2, 3, Fraction(0), Fraction(1, 2), Fraction(-1)
    )
    check(
        "reversing the supplied cubic index reverses its trace contribution",
        reversed_cubic.weak_multiplicity * reversed_cubic.color_cubic_index
        == Fraction(-2),
    )

    mutant = (
        FormalEntry("A", 2, 3, Fraction(1, 2), Fraction(1, 2), Fraction(1)),
        PACKET[1],
    )
    expect_rejection(
        "a changed y packet is rejected",
        PacketMismatch,
        lambda: validate_packet(mutant),
    )
    expect_rejection(
        "a physical hypercharge inference is rejected",
        PhysicalInference,
        lambda: infer_physical_hypercharge(traces),
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: supplied formal trace packet verified; no physical P-HY "
            "or hypercharge readout inferred."
        )
        return 0
    print("VERDICT: formal trace packet FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
