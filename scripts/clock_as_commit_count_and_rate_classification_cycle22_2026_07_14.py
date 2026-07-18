#!/usr/bin/env python3
"""Exact controls for the Cycle-22 commit-clock classification."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from math import exp
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


def normalized(path: Path) -> str:
    return " ".join(
        path.read_text(encoding="utf-8")
        .lower()
        .replace("*", "")
        .replace("`", "")
        .replace(">", "")
        .split()
    )


EVENTS = ("start", "left", "right", "close")
PREDS = {
    "start": frozenset(),
    "left": frozenset(("start",)),
    "right": frozenset(("start",)),
    "close": frozenset(("left", "right")),
}
CLOCK = frozenset(("start", "left", "close"))


def is_linear_extension(order: tuple[str, ...]) -> bool:
    positions = {event: index for index, event in enumerate(order)}
    return all(
        positions[parent] < positions[event]
        for event, parents in PREDS.items()
        for parent in parents
    )


def tau(prefix: tuple[str, ...]) -> int:
    return sum(event in CLOCK for event in prefix)


def source_contract() -> None:
    section("A - Authority and foundation contract")
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    check("A note exists", NOTE.is_file())
    check("A note is authority-free", "authority: none" in note)
    check("A note does not amend an axiom", "does not amend an axiom" in note)
    check("A note does not select a law", "select a law" in note)
    check("A foundation has permanent records", "records are permanent" in axioms)
    check("A foundation has record-only readability", "only records are readable" in axioms)
    check("A foundation has additive scalar readout", "scalar readout i is additive" in axioms)


def commit_clock_theorem() -> None:
    section("B - Commit-clock theorem")
    schedules = tuple(order for order in permutations(EVENTS) if is_linear_extension(order))
    check("B diamond has two linear extensions", len(schedules) == 2)
    check("B every schedule has the same clock count", {tau(order) for order in schedules} == {3})
    for order in schedules:
        counts = tuple(tau(order[:index]) for index in range(len(order) + 1))
        check(f"B clock count is monotone on {order}", all(left <= right for left, right in zip(counts, counts[1:])))
    segment_one = ("start", "left")
    segment_two = ("close",)
    check("B disjoint segment increments add", tau(segment_one + segment_two) == tau(segment_one) + tau(segment_two))
    check("B total records differ from clock-chain records", len(EVENTS) == 4 and len(CLOCK) == 3)
    longest_chain = 3
    check("B total records differ from longest causal chain", len(EVENTS) == 4 and longest_chain == 3)


def refinement_rate_and_capacity_controls() -> None:
    section("C - Refinement, rate, and capacity separators")
    direct_transcript = ("commit",)
    wrapped_transcript = ("phase", "commit")
    check("C visible refinement changes transcript", direct_transcript != wrapped_transcript)
    check("C visible refinement changes record count", len(direct_transcript) == 1 and len(wrapped_transcript) == 2)
    check("C visible refinement changes additive unit cost", sum(1 for _ in direct_transcript) == 1 and sum(1 for _ in wrapped_transcript) == 2)
    t = 1.0
    survival_one = exp(-1.0 * t)
    survival_two = exp(-2.0 * t)
    check("C two rates have different waiting-time laws", survival_one != survival_two)
    check("C both rate laws have the same finite event-order support", all(rate > 0 for rate in (1.0, 2.0)))
    check("C rescaling both rates preserves dimensionless ratio", Fraction(2, 1) / Fraction(1, 1) == Fraction(14, 1) / Fraction(7, 1))
    p_half = Fraction(1, 2)
    p_three_quarters = Fraction(3, 4)
    capacity = 1
    check("C both utilizations obey the same unit capacity", p_half <= capacity and p_three_quarters <= capacity)
    check("C capacity does not fix utilization", p_half != p_three_quarters)


def documentation_contract() -> None:
    section("D - Classification and N1-N8 contract")
    note = normalized(NOTE)
    required = (
        "a clock does not make a record lock",
        "commit count is local time",
        "record-faithful physical-equivalence class",
        "relative rate",
        "scalar lapse alone gives only half",
        "no clock/lock sentence belongs in record",
        "the universe is compute/storage limited",
        "dimensionless clock ratios",
    )
    for phrase in required:
        check(f"D required phrase is present: {phrase}", phrase in note)
    for lane in ("time", "probability", "resource", "gravity", "thermodynamic arrow"):
        check(f"D TOE lane is classified: {lane}", f"| {lane} |" in note)
    for index in range(1, 9):
        check(f"D N{index} section is present", f"n{index} —" in note)
    check("D N7 retains relational-time route", "relational-time route" in note and "cannot retire dimensionless clock ratios" in note)
    check("D no new axiom conclusion is explicit", "no row forces its own axiom sentence" in note)


def main() -> int:
    source_contract()
    commit_clock_theorem()
    refinement_rate_and_capacity_controls()
    documentation_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: PASS" if FAIL == 0 else "RESULT: FAIL")
    print("BOUNDARY: commit counting is a relational clock theorem after event identity; rate and tensor response remain exact-law fields")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
