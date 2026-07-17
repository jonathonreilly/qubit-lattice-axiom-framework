#!/usr/bin/env python3
"""Exact checks for the finite marked piecewise-affine structural theorem."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Sequence


NOTE_PATH = Path("docs/ALPHA_S_HEAVY_THRESHOLD_MATCHING_KERNEL_THEOREM_NOTE_2026-06-18.md")
QCD_LOW_NOTE_PATH = Path("docs/QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md")
EXPECTED = {
    "normal": (32, 0),
    "independent": (12, 0),
    "hostile": (23, 0),
}
MUTATIONS = (
    "coefficient",
    "coefficient_match",
    "composition",
    "inverse",
    "identity_carry",
    "ordering",
    "source_scope",
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" :: {detail}" if detail else ""
    print(f"[{status}] {name}{suffix}")


def require_fraction(name: str, value: object, *, positive: bool = False) -> Fraction:
    if type(value) is not Fraction:
        raise TypeError(f"{name} must be an exact Fraction")
    if positive and value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def coefficient_for_index(index: int) -> Fraction:
    if type(index) is not int:
        raise TypeError("index must be an exact integer")
    if index < 0:
        raise ValueError("index must be nonnegative")
    result = Fraction(11, 1) - Fraction(2 * index, 3)
    if result <= 0:
        raise ValueError("defined coefficient must be positive")
    return result


def affine_step(x: Fraction, coefficient: Fraction, length: Fraction) -> Fraction:
    require_fraction("x", x)
    c = require_fraction("coefficient", coefficient, positive=True)
    interval = require_fraction("length", length, positive=True)
    return x - c * interval


def affine_inverse(y: Fraction, coefficient: Fraction, length: Fraction) -> Fraction:
    require_fraction("y", y)
    c = require_fraction("coefficient", coefficient, positive=True)
    interval = require_fraction("length", length, positive=True)
    return y + c * interval


@dataclass(frozen=True)
class Segment:
    index: int
    coefficient: Fraction
    length: Fraction


@dataclass(frozen=True)
class MarkerEvent:
    left_index: int
    right_index: int
    value_before: Fraction
    value_after: Fraction


def validate_segment(segment: object) -> Segment:
    if type(segment) is not Segment:
        raise TypeError("path entries must be Segment objects")
    expected = coefficient_for_index(segment.index)
    supplied = require_fraction("segment coefficient", segment.coefficient, positive=True)
    require_fraction("segment length", segment.length, positive=True)
    if supplied != expected:
        raise ValueError("segment coefficient must equal c(index) exactly")
    return segment


def validate_path(segments: Sequence[Segment]) -> tuple[Segment, ...]:
    if type(segments) not in (list, tuple):
        raise TypeError("path must be a list or tuple")
    path = tuple(validate_segment(segment) for segment in segments)
    if not path:
        raise ValueError("path must contain at least one segment")
    for left, right in zip(path, path[1:]):
        if right.index != left.index - 1:
            raise ValueError("adjacent path indices must decrease by exactly one")
    return path


def apply_path(x: Fraction, segments: Sequence[Segment]) -> tuple[Fraction, tuple[MarkerEvent, ...]]:
    require_fraction("x", x)
    path = validate_path(segments)
    current = x
    events: list[MarkerEvent] = []
    for position, segment in enumerate(path):
        current = affine_step(current, segment.coefficient, segment.length)
        if position + 1 < len(path):
            right = path[position + 1]
            events.append(MarkerEvent(segment.index, right.index, current, current))
    return current, tuple(events)


def path_closed_form(x: Fraction, segments: Sequence[Segment]) -> Fraction:
    require_fraction("x", x)
    path = validate_path(segments)
    return x - sum((segment.coefficient * segment.length for segment in path), Fraction(0, 1))


def reverse_path(y: Fraction, segments: Sequence[Segment]) -> Fraction:
    require_fraction("y", y)
    path = validate_path(segments)
    current = y
    for segment in reversed(path):
        current = affine_inverse(current, segment.coefficient, segment.length)
    return current


def apply_path_with_jumps(
    x: Fraction,
    segments: Sequence[Segment],
    jumps: Sequence[Fraction],
) -> Fraction:
    require_fraction("x", x)
    path = validate_path(segments)
    if type(jumps) not in (list, tuple):
        raise TypeError("jumps must be a list or tuple")
    if len(jumps) != len(path) - 1:
        raise ValueError("one jump is required per marker")
    exact_jumps = tuple(require_fraction("jump", jump) for jump in jumps)
    current = x
    for position, segment in enumerate(path):
        current = affine_step(current, segment.coefficient, segment.length)
        if position < len(exact_jumps):
            current += exact_jumps[position]
    return current


def rejects(call: Callable[[], object]) -> bool:
    try:
        call()
    except (TypeError, ValueError):
        return True
    return False


def sample_path() -> list[Segment]:
    return [
        Segment(6, coefficient_for_index(6), Fraction(3, 5)),
        Segment(5, coefficient_for_index(5), Fraction(7, 11)),
        Segment(4, coefficient_for_index(4), Fraction(5, 13)),
        Segment(3, coefficient_for_index(3), Fraction(2, 7)),
    ]


def run_normal() -> None:
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    qcd_text = QCD_LOW_NOTE_PATH.read_text(encoding="utf-8")
    theorem_surface = note_text.split("## 1. Purpose", maxsplit=1)[1].split("## 8. Physical nonclaims", maxsplit=1)[0]

    print("=== Source and scope ===")
    check("claim type is positive_theorem", "**Claim type:** positive_theorem" in note_text)
    check("defined affine map is stated exactly", "T_{c,L}(x) := x - c L" in note_text)
    check("note declares dependency-free exact arithmetic", "**Dependencies:** none; definitions and exact rational arithmetic only" in note_text)
    check("identity carry is explicitly a definition", "The identity carry is part of the definition" in note_text)
    check("physical semantics are absent from the theorem surface", not any(token in theorem_surface for token in ("alpha_s", "QCD", "threshold", "coupling", "beta function", "Lambda parameter")))
    check("QCD context denies physical authority from the formal lemma", "supplies no QCD beta" in qcd_text and "cannot substitute for threshold" in qcd_text)

    print("\n=== Defined coefficient sequence ===")
    check("c(6) = 7", coefficient_for_index(6) == Fraction(7, 1))
    check("c(5) = 23/3", coefficient_for_index(5) == Fraction(23, 3))
    check("c(4) = 25/3", coefficient_for_index(4) == Fraction(25, 3))
    check("c(3) = 9", coefficient_for_index(3) == Fraction(9, 1))
    check("c(n-1) - c(n) = 2/3 on the full adjacent domain", all(coefficient_for_index(n - 1) - coefficient_for_index(n) == Fraction(2, 3) for n in range(1, 17)))
    check("positive domain is exactly indices 0 through 16", coefficient_for_index(16) == Fraction(1, 3) and rejects(lambda: coefficient_for_index(17)))
    check("every admissible coefficient is a positive exact Fraction", all(type(coefficient_for_index(n)) is Fraction and coefficient_for_index(n) > 0 for n in range(17)))

    print("\n=== Fixed-coefficient affine identities ===")
    x = Fraction(137, 17)
    c = Fraction(23, 3)
    first = Fraction(7, 11)
    second = Fraction(5, 13)
    forward = affine_step(x, c, first)
    check("segment formula is exact", forward == x - c * first)
    check("U after T is the identity", affine_inverse(forward, c, first) == x)
    backward_first = affine_inverse(x, c, first)
    check("T after U is the identity", affine_step(backward_first, c, first) == x)
    split = affine_step(affine_step(x, c, first), c, second)
    check("same-coefficient intervals concatenate", split == affine_step(x, c, first + second))
    c2 = Fraction(25, 3)
    c3 = Fraction(9, 1)
    left_grouped = affine_step(affine_step(affine_step(x, c, first), c2, second), c3, Fraction(2, 7))
    right_closed = x - c * first - c2 * second - c3 * Fraction(2, 7)
    check("three-step composition is associative", left_grouped == right_closed)
    check("segment validation preserves an exact supplied triple", validate_segment(Segment(5, c, first)) == Segment(5, c, first))

    print("\n=== Finite marked paths ===")
    path = sample_path()
    one_segment = path[:1]
    one_value, no_events = apply_path(x, one_segment)
    check("one segment realizes the empty marker list", len(no_events) == 0 and one_value == path_closed_form(x, one_segment))
    two_value, one_event = apply_path(x, path[:2])
    check("two segments emit one identity marker", len(one_event) == 1 and one_event[0].value_before == one_event[0].value_after)
    many_value, events = apply_path(x, path)
    check("four segments emit three ordered markers", [(event.left_index, event.right_index) for event in events] == [(6, 5), (5, 4), (4, 3)])
    check("every marker carries its value exactly", all(event.value_before == event.value_after for event in events))
    check("sequential path equals exact summed closed form", many_value == path_closed_form(x, path))
    check("reverse inverse maps recover the initial value", reverse_path(many_value, path) == x)
    check("path output has exact Fraction type", type(many_value) is Fraction)
    prefix_value, _ = apply_path(x, path[:2])
    suffix_value, _ = apply_path(prefix_value, path[2:])
    check("prefix then suffix grouping equals the full path", suffix_value == many_value)

    print("\n=== Marker-jump counterexamples ===")
    zero_jumps = [Fraction(0, 1)] * 3
    check("empty marker list accepts an empty jump tuple", apply_path_with_jumps(x, one_segment, []) == one_value)
    check("zero-jump realization equals defined identity carries", apply_path_with_jumps(x, path, zero_jumps) == many_value)
    jump = Fraction(5, 19)
    single_jump_value = apply_path_with_jumps(x, path, [jump, Fraction(0, 1), Fraction(0, 1)])
    check("one nonzero jump changes the result by exactly that jump", single_jump_value - many_value == jump)
    cancelling = [Fraction(2, 9), Fraction(-5, 21), Fraction(1, 63)]
    check("arbitrary jumps change the result by their exact sum", apply_path_with_jumps(x, path, cancelling) - many_value == sum(cancelling, Fraction(0, 1)))
    check("nonzero cancelling jumps can preserve only the final value", sum(cancelling, Fraction(0, 1)) == 0 and any(event != 0 for event in cancelling))


def run_independent() -> None:
    print("=== Independent exact reconstruction ===")

    def independent_c(index: int) -> Fraction:
        return Fraction(33 - 2 * index, 3)

    indices = (6, 5, 4, 3)
    lengths = (Fraction(3, 5), Fraction(7, 11), Fraction(5, 13), Fraction(2, 7))
    coefficients = tuple(independent_c(index) for index in indices)
    start = Fraction(137, 17)
    direct = start - sum((coefficient * length for coefficient, length in zip(coefficients, lengths)), Fraction(0, 1))
    primary, events = apply_path(start, sample_path())

    check("independent formula reconstructs c(6)", coefficients[0] == Fraction(7, 1))
    check("independent formula reconstructs c(5)", coefficients[1] == Fraction(23, 3))
    check("independent formula reconstructs c(4)", coefficients[2] == Fraction(25, 3))
    check("independent formula reconstructs c(3)", coefficients[3] == Fraction(9, 1))
    check("independent coefficients match the primary definition", coefficients == tuple(coefficient_for_index(index) for index in indices))
    check("independent direct sum matches sequential application", direct == primary)
    check("independent marker count is length minus one", len(events) == len(indices) - 1)
    check("independent ordering reconstruction is consecutive", all(right == left - 1 for left, right in zip(indices, indices[1:])))
    independently_restored = direct + sum((coefficient * length for coefficient, length in reversed(tuple(zip(coefficients, lengths)))), Fraction(0, 1))
    check("independent reverse sum restores the start", independently_restored == start)
    first_half = start - coefficients[0] * lengths[0] - coefficients[1] * lengths[1]
    second_half = first_half - coefficients[2] * lengths[2] - coefficients[3] * lengths[3]
    check("independent two-block grouping matches the direct sum", second_half == direct)
    jumps = (Fraction(4, 23), Fraction(-1, 7), Fraction(2, 13))
    jumped = direct + sum(jumps, Fraction(0, 1))
    check("independent jump formula matches primary jump application", jumped == apply_path_with_jumps(start, sample_path(), list(jumps)))
    check("all reconstructed values remain exact", all(type(value) is Fraction for value in coefficients + lengths + (direct, independently_restored, jumped)))


def run_hostile() -> None:
    print("=== Hostile domain and structure inputs ===")
    c6 = Fraction(7, 1)
    length = Fraction(1, 2)
    good = Segment(6, c6, length)
    cases: tuple[tuple[str, Callable[[], object]], ...] = (
        ("boolean index", lambda: coefficient_for_index(True)),
        ("fractional index", lambda: coefficient_for_index(Fraction(6, 1))),
        ("negative index", lambda: coefficient_for_index(-1)),
        ("index with nonpositive coefficient", lambda: coefficient_for_index(17)),
        ("integer state", lambda: affine_step(1, c6, length)),
        ("float state", lambda: affine_step(1.0, c6, length)),
        ("boolean state", lambda: affine_step(False, c6, length)),
        ("integer coefficient", lambda: affine_step(Fraction(1, 1), 7, length)),
        ("float coefficient", lambda: affine_step(Fraction(1, 1), 7.0, length)),
        ("zero coefficient", lambda: affine_step(Fraction(1, 1), Fraction(0, 1), length)),
        ("negative coefficient", lambda: affine_step(Fraction(1, 1), Fraction(-7, 1), length)),
        ("integer length", lambda: affine_step(Fraction(1, 1), c6, 1)),
        ("float length", lambda: affine_step(Fraction(1, 1), c6, 0.5)),
        ("zero length", lambda: affine_step(Fraction(1, 1), c6, Fraction(0, 1))),
        ("negative length", lambda: affine_step(Fraction(1, 1), c6, Fraction(-1, 2))),
        ("mismatched defined coefficient", lambda: validate_segment(Segment(6, Fraction(23, 3), length))),
        ("empty path", lambda: validate_path([])),
        ("repeated labels", lambda: validate_path([good, Segment(6, c6, length)])),
        ("ascending labels", lambda: validate_path([Segment(5, Fraction(23, 3), length), good])),
        ("skipped labels", lambda: validate_path([good, Segment(4, Fraction(25, 3), length)])),
        ("non-sequence path", lambda: validate_path("not-a-path")),
        ("wrong jump count", lambda: apply_path_with_jumps(Fraction(1, 1), sample_path(), [Fraction(0, 1)])),
        ("inexact jump", lambda: apply_path_with_jumps(Fraction(1, 1), sample_path(), [Fraction(0, 1), 0.0, Fraction(0, 1)])),
    )
    for name, call in cases:
        check(f"rejects {name}", rejects(call))


def mutation_condition(name: str) -> bool:
    x = Fraction(137, 17)
    path = sample_path()
    correct, _ = apply_path(x, path)
    if name == "coefficient":
        return coefficient_for_index(5) + Fraction(1, 1) == Fraction(23, 3)
    if name == "coefficient_match":
        return not rejects(lambda: validate_segment(Segment(6, Fraction(23, 3), Fraction(1, 2))))
    if name == "composition":
        return correct + Fraction(1, 97) == path_closed_form(x, path)
    if name == "inverse":
        return reverse_path(correct, path) - Fraction(1, 89) == x
    if name == "identity_carry":
        jumped = apply_path_with_jumps(x, path, [Fraction(1, 31), Fraction(0, 1), Fraction(0, 1)])
        return jumped == correct
    if name == "ordering":
        return not rejects(lambda: validate_path([path[0], path[2]]))
    if name == "source_scope":
        note_text = NOTE_PATH.read_text(encoding="utf-8")
        theorem_surface = note_text.split("## 8. Physical nonclaims", maxsplit=1)[0] + " QCD"
        return "QCD" not in theorem_surface
    raise ValueError(f"unknown mutation: {name}")


def run_mutations(selection: str) -> None:
    selected = MUTATIONS if selection == "all" else (selection,)
    print("=== Intentional-failure fixtures ===")
    for name in selected:
        check(f"mutation {name} must be detected", mutation_condition(name))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--independent", action="store_true")
    mode.add_argument("--hostile", action="store_true")
    mode.add_argument("--intentional-failure", action="store_true")
    parser.add_argument("--mutation", choices=("all",) + MUTATIONS, default="all")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.intentional_failure:
        run_mutations(args.mutation)
        print(f"\nSUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
        return 1 if FAIL_COUNT > 0 else 2

    if args.independent:
        mode = "independent"
        run_independent()
    elif args.hostile:
        mode = "hostile"
        run_hostile()
    else:
        mode = "normal"
        run_normal()

    print(f"\nSUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    expected_pass, expected_fail = EXPECTED[mode]
    return 0 if (PASS_COUNT, FAIL_COUNT) == (expected_pass, expected_fail) else 1


if __name__ == "__main__":
    raise SystemExit(main())
