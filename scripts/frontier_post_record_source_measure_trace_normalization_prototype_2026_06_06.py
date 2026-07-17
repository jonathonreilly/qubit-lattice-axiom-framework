#!/usr/bin/env python3
"""Exact finite rational normalization and Radon–Nikodym theorem."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd
from pathlib import Path
import re
import sys
from typing import Callable, TypeAlias


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/POST_RECORD_SOURCE_MEASURE_TRACE_NORMALIZATION_PROTOTYPE_2026-06-06.md"

Label: TypeAlias = str
ExactPacket: TypeAlias = tuple[tuple[Label, Fraction], ...]

PASS = 0
FAIL = 0


class FractionSubclass(Fraction):
    """Hostile fixture: exact-looking subclasses are outside the contract."""


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def section(title: str) -> None:
    print(f"\n{'-' * 78}\n{title}\n{'-' * 78}")


def exact_fraction(value: object, context: str) -> Fraction:
    if type(value) is not Fraction:
        raise TypeError(f"{context} must have exact runtime type Fraction")
    return value


def packet_items(packet: ExactPacket, context: str) -> tuple[tuple[str, Fraction], ...]:
    if type(packet) is not tuple or not packet:
        raise ValueError(f"{context} carrier must be a nonempty finite tuple")
    labels: set[str] = set()
    checked: list[tuple[str, Fraction]] = []
    for item in packet:
        if type(item) is not tuple or len(item) != 2:
            raise TypeError(f"{context} entries must be (label, Fraction) tuples")
        label, raw_value = item
        if type(label) is not str or not label:
            raise TypeError(f"{context} labels must be nonempty strings")
        if label in labels:
            raise ValueError(f"duplicate {context} label: {label}")
        labels.add(label)
        checked.append((label, exact_fraction(raw_value, f"{context}[{label}]")))
    return tuple(checked)


def nonnegative_packet(packet: ExactPacket, context: str) -> tuple[tuple[str, Fraction], ...]:
    checked = packet_items(packet, context)
    if any(value < 0 for _, value in checked):
        raise ValueError(f"{context} values must be nonnegative")
    return checked


def normalize_exact(weights: ExactPacket) -> ExactPacket:
    checked = nonnegative_packet(weights, "weight")
    total = sum((value for _, value in checked), Fraction(0))
    if total <= 0:
        raise ValueError("weight total must be positive")
    return tuple((label, value / total) for label, value in checked)


def probability_map(packet: ExactPacket, context: str) -> dict[str, Fraction]:
    checked = nonnegative_packet(packet, context)
    if sum((value for _, value in checked), Fraction(0)) != 1:
        raise ValueError(f"{context} must sum exactly to one")
    return dict(checked)


def exact_map(packet: ExactPacket, context: str) -> dict[str, Fraction]:
    return dict(packet_items(packet, context))


def same_carrier(left: dict[str, Fraction], right: dict[str, Fraction]) -> bool:
    return set(left) == set(right)


def absolutely_continuous(source: ExactPacket, reference: ExactPacket) -> bool:
    source_map = probability_map(source, "source probability")
    reference_map = probability_map(reference, "reference probability")
    if not same_carrier(source_map, reference_map):
        raise ValueError("source/reference label carriers differ")
    return all(reference_map[label] > 0 or source_map[label] == 0 for label in source_map)


def rn_density(source: ExactPacket, reference: ExactPacket) -> ExactPacket:
    source_map = probability_map(source, "source probability")
    reference_map = probability_map(reference, "reference probability")
    if not same_carrier(source_map, reference_map):
        raise ValueError("source/reference label carriers differ")
    density: list[tuple[str, Fraction]] = []
    for label, source_value in source:
        reference_value = reference_map[label]
        if reference_value == 0:
            if source_value != 0:
                raise ValueError("source is not absolutely continuous")
            density.append((label, Fraction(0)))
        else:
            density.append((label, source_value / reference_value))
    return tuple(density)


def expectation(probability: ExactPacket, observable: ExactPacket) -> Fraction:
    probability_values = probability_map(probability, "probability")
    observable_values = exact_map(observable, "observable")
    if not same_carrier(probability_values, observable_values):
        raise ValueError("probability/observable label carriers differ")
    return sum(
        (probability_values[label] * observable_values[label] for label in probability_values),
        Fraction(0),
    )


def rn_expectation(
    reference: ExactPacket, density: ExactPacket, observable: ExactPacket
) -> Fraction:
    reference_values = probability_map(reference, "reference probability")
    density_values = dict(nonnegative_packet(density, "density"))
    observable_values = exact_map(observable, "observable")
    if not (
        same_carrier(reference_values, density_values)
        and same_carrier(reference_values, observable_values)
    ):
        raise ValueError("reference/density/observable label carriers differ")
    return sum(
        (
            reference_values[label]
            * density_values[label]
            * observable_values[label]
            for label in reference_values
        ),
        Fraction(0),
    )


def compose_density(first: ExactPacket, second: ExactPacket) -> ExactPacket:
    first_values = dict(nonnegative_packet(first, "first density"))
    second_values = dict(nonnegative_packet(second, "second density"))
    if not same_carrier(first_values, second_values):
        raise ValueError("density label carriers differ")
    return tuple(
        (label, value * second_values[label]) for label, value in first
    )


def equal_by_label(left: ExactPacket, right: ExactPacket) -> bool:
    try:
        return exact_map(left, "left packet") == exact_map(right, "right packet")
    except (TypeError, ValueError):
        return False


def verify_density(
    source: ExactPacket, reference: ExactPacket, candidate: ExactPacket
) -> bool:
    try:
        expected = rn_density(source, reference)
        candidate_values = dict(nonnegative_packet(candidate, "candidate density"))
        reference_values = probability_map(reference, "reference probability")
    except (TypeError, ValueError):
        return False
    if not same_carrier(candidate_values, reference_values):
        return False
    integral = sum(
        (reference_values[label] * candidate_values[label] for label in reference_values),
        Fraction(0),
    )
    return equal_by_label(candidate, expected) and integral == 1


def lcm(left: int, right: int) -> int:
    return abs(left * right) // gcd(left, right) if left and right else 0


def independent_exact(value: object, context: str) -> Fraction:
    if type(value) is not Fraction:
        raise TypeError(f"independent {context} is not a strict Fraction")
    return value


def independent_entries(packet: ExactPacket, context: str) -> tuple[tuple[str, Fraction], ...]:
    if type(packet) is not tuple or not packet:
        raise ValueError(f"independent {context} carrier is empty or non-tuple")
    labels: set[str] = set()
    out: list[tuple[str, Fraction]] = []
    for item in packet:
        if type(item) is not tuple or len(item) != 2:
            raise TypeError(f"independent malformed {context} entry")
        label, raw_value = item
        if type(label) is not str or not label or label in labels:
            raise ValueError(f"independent {context} labels must be unique strings")
        labels.add(label)
        out.append((label, independent_exact(raw_value, context)))
    return tuple(out)


def independent_sum(values: tuple[Fraction, ...]) -> Fraction:
    denominator = 1
    for value in values:
        denominator = lcm(denominator, value.denominator)
    numerator = sum(
        value.numerator * (denominator // value.denominator) for value in values
    )
    return Fraction(numerator, denominator)


def normalize_independently(weights: ExactPacket) -> ExactPacket:
    checked = independent_entries(weights, "weight")
    if any(value < 0 for _, value in checked):
        raise ValueError("independent negative weight")
    common_denominator = 1
    for _, value in checked:
        common_denominator = lcm(common_denominator, value.denominator)
    integer_counts = tuple(
        value.numerator * (common_denominator // value.denominator)
        for _, value in checked
    )
    total_count = sum(integer_counts)
    if total_count <= 0:
        raise ValueError("independent nonpositive weight total")
    return tuple(
        (checked[index][0], Fraction(count, total_count))
        for index, count in enumerate(integer_counts)
    )


def independent_probability_map(packet: ExactPacket, context: str) -> dict[str, Fraction]:
    checked = independent_entries(packet, context)
    if any(value < 0 for _, value in checked):
        raise ValueError(f"independent negative {context}")
    if independent_sum(tuple(value for _, value in checked)) != 1:
        raise ValueError(f"independent {context} is not normalized")
    return dict(checked)


def density_independently(source: ExactPacket, reference: ExactPacket) -> ExactPacket:
    source_values = independent_probability_map(source, "source")
    reference_values = independent_probability_map(reference, "reference")
    if set(source_values) != set(reference_values):
        raise ValueError("independent density carrier mismatch")
    result: list[tuple[str, Fraction]] = []
    for label, source_value in source:
        reference_value = reference_values[label]
        if reference_value == 0:
            if source_value != 0:
                raise ValueError("independent unsupported source mass")
            result.append((label, Fraction(0)))
            continue
        numerator = source_value.numerator * reference_value.denominator
        denominator = source_value.denominator * reference_value.numerator
        result.append((label, Fraction(numerator, denominator)))
    return tuple(result)


def expectation_independently(
    probability: ExactPacket, observable: ExactPacket
) -> Fraction:
    probability_values = independent_probability_map(probability, "probability")
    observable_values = dict(independent_entries(observable, "observable"))
    if set(probability_values) != set(observable_values):
        raise ValueError("independent expectation carrier mismatch")
    products = tuple(
        Fraction(
            probability_values[label].numerator * observable_values[label].numerator,
            probability_values[label].denominator * observable_values[label].denominator,
        )
        for label in probability_values
    )
    return independent_sum(products)


def rn_expectation_independently(
    reference: ExactPacket, density: ExactPacket, observable: ExactPacket
) -> Fraction:
    reference_values = independent_probability_map(reference, "reference")
    density_values = dict(independent_entries(density, "density"))
    observable_values = dict(independent_entries(observable, "observable"))
    if not (
        set(reference_values) == set(density_values) == set(observable_values)
    ):
        raise ValueError("independent RN expectation carrier mismatch")
    products: list[Fraction] = []
    for label, reference_value in reference_values.items():
        density_value = density_values[label]
        observable_value = observable_values[label]
        products.append(
            Fraction(
                reference_value.numerator
                * density_value.numerator
                * observable_value.numerator,
                reference_value.denominator
                * density_value.denominator
                * observable_value.denominator,
            )
        )
    return independent_sum(tuple(products))


def compose_independently(first: ExactPacket, second: ExactPacket) -> ExactPacket:
    first_values = dict(independent_entries(first, "first density"))
    second_values = dict(independent_entries(second, "second density"))
    if set(first_values) != set(second_values):
        raise ValueError("independent cocycle carrier mismatch")
    return tuple(
        (
            label,
            Fraction(
                value.numerator * second_values[label].numerator,
                value.denominator * second_values[label].denominator,
            ),
        )
        for label, value in first
    )


def expect_raises(
    error_types: type[Exception] | tuple[type[Exception], ...],
    operation: Callable[[], object],
) -> bool:
    try:
        operation()
    except error_types:
        return True
    except Exception:
        return False
    return False


def source_scope_checks() -> None:
    section("Source theorem and semantic scope checks")
    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    report("source note exists", NOTE.is_file())
    required = (
        "**Claim type:** positive_theorem",
        "**Dependencies:** none.",
        "P << R",
        "0/0 := 0",
        "sum_i P_i f_i = sum_i R_i (dP/dR)_i f_i",
        "dP/dR = (dP/dQ)(dQ/dR)",
        "All algebra aligns entries by label, never by tuple position.",
        "Audit censuses, ledgers, queues, exports, helper runners, and row counts are repository metadata outside the theorem arguments.",
    )
    for phrase in required:
        report(f"source contains theorem anchor: {phrase}", phrase in flat)

    forbidden_patterns = (
        r"\bRecord (?:derives|supplies|selects|fixes)\b",
        r"\bthe normalized packet (?:is|selects) the physical\b",
        r"\bthe trace/reference (?:is|selects) the physical\b",
        r"\bBorn (?:law|rule) follows\b",
        r"\b(?:16|10|26) (?:source|trace|prototype|row)",
        r"frontier_post_record_measure_weight_normalization_subdivision_2026_06_06\.py",
        r"frontier_post_record_selector_dial_bucket_subdivision_2026_06_06\.py",
        r"post_record_stability_dynamics_selector_slice_2026_06_07\.json",
        r"docs/audit/data/",
        r"\baudit_status\s*:",
        r"\beffective_status\s*:",
    )
    for pattern in forbidden_patterns:
        report(
            f"source excludes volatile or physical overclaim: {pattern}",
            re.search(pattern, flat, flags=re.IGNORECASE) is None,
        )


def normal_checks() -> None:
    section("Exact finite normalization")
    reference = normalize_exact(
        (("minus", Fraction(1)), ("plus", Fraction(1)), ("null", Fraction(0)))
    )
    source = normalize_exact(
        (("minus", Fraction(1)), ("plus", Fraction(3)), ("null", Fraction(0)))
    )
    report(
        "reference weights normalize exactly with a zero entry",
        reference
        == (
            ("minus", Fraction(1, 2)),
            ("plus", Fraction(1, 2)),
            ("null", Fraction(0)),
        ),
        str(reference),
    )
    report(
        "source weights normalize exactly with a zero entry",
        source
        == (
            ("minus", Fraction(1, 4)),
            ("plus", Fraction(3, 4)),
            ("null", Fraction(0)),
        ),
        str(source),
    )
    report(
        "both probability packets sum exactly to one",
        sum((value for _, value in reference), Fraction(0)) == 1
        and sum((value for _, value in source), Fraction(0)) == 1,
    )

    section("Finite RN density and expectation identity")
    density = rn_density(source, reference)
    observable = (
        ("null", Fraction(7)),
        ("plus", Fraction(1)),
        ("minus", Fraction(-1)),
    )
    report("source is absolutely continuous with respect to reference", absolutely_continuous(source, reference))
    report(
        "RN density uses exact zero/zero convention",
        density
        == (
            ("minus", Fraction(1, 2)),
            ("plus", Fraction(3, 2)),
            ("null", Fraction(0)),
        ),
        str(density),
    )
    report("RN density verifies semantically", verify_density(source, reference, density))
    report(
        "RN density integrates exactly to one",
        expectation(reference, density) == 1,
    )
    direct = expectation(source, observable)
    changed = rn_expectation(reference, density, observable)
    report("signed source expectation is exactly one half", direct == Fraction(1, 2), str(direct))
    report("exact change-of-reference expectation identity", direct == changed, str(changed))

    zero_source = (
        ("minus", Fraction(0)),
        ("plus", Fraction(1)),
        ("null", Fraction(0)),
    )
    zero_density = rn_density(zero_source, reference)
    report(
        "zero source at positive reference gives zero density",
        dict(zero_density)["minus"] == 0,
        str(zero_density),
    )
    report("zero-source density still integrates to one", expectation(reference, zero_density) == 1)

    section("Exact three-packet density cocycle")
    middle = normalize_exact(
        (("minus", Fraction(2)), ("plus", Fraction(1)), ("null", Fraction(0)))
    )
    d_source_middle = rn_density(source, middle)
    d_middle_reference = rn_density(middle, reference)
    composed = compose_density(d_source_middle, d_middle_reference)
    report("source is absolutely continuous with respect to middle", absolutely_continuous(source, middle))
    report("middle is absolutely continuous with respect to reference", absolutely_continuous(middle, reference))
    report("positive-support RN cocycle is exact", equal_by_label(composed, density), str(composed))

    broad = (
        ("a", Fraction(1, 4)),
        ("b", Fraction(1, 4)),
        ("c", Fraction(1, 4)),
        ("d", Fraction(1, 4)),
    )
    sparse_middle = (
        ("a", Fraction(1, 2)),
        ("b", Fraction(1, 2)),
        ("c", Fraction(0)),
        ("d", Fraction(0)),
    )
    sparse_source = (
        ("a", Fraction(1)),
        ("b", Fraction(0)),
        ("c", Fraction(0)),
        ("d", Fraction(0)),
    )
    sparse_composed = compose_density(
        rn_density(sparse_source, sparse_middle),
        rn_density(sparse_middle, broad),
    )
    report(
        "cocycle handles intermediate zero support",
        equal_by_label(sparse_composed, rn_density(sparse_source, broad)),
        str(sparse_composed),
    )

    section("Label-order permutation semantics")
    permuted_source = tuple(reversed(source))
    permuted_reference = (reference[1], reference[2], reference[0])
    permuted_observable = (observable[1], observable[2], observable[0])
    permuted_density = rn_density(permuted_source, permuted_reference)
    report("density values are permutation-equivariant by label", equal_by_label(permuted_density, density))
    report(
        "expectation is invariant under independent tuple permutations",
        expectation(permuted_source, permuted_observable) == direct,
    )
    report(
        "RN expectation is invariant under independent tuple permutations",
        rn_expectation(permuted_reference, permuted_density, permuted_observable)
        == changed,
    )


def independent_checks() -> None:
    section("Independent integer-count normalization")
    packets = (
        (("a", Fraction(1)), ("b", Fraction(3)), ("z", Fraction(0))),
        (("a", Fraction(1, 2)), ("b", Fraction(1, 3)), ("z", Fraction(1, 6))),
        (("a", Fraction(0)), ("b", Fraction(7, 11))),
    )
    for index, raw in enumerate(packets, start=1):
        rebuilt = normalize_independently(raw)
        report(
            f"packet {index}: independent integer counts agree",
            rebuilt == normalize_exact(raw),
            str(rebuilt),
        )
        report(
            f"packet {index}: independent sum is one",
            independent_sum(tuple(value for _, value in rebuilt)) == 1,
        )

    section("Independent density and expectation reconstruction")
    reference = (
        ("x", Fraction(1, 2)),
        ("y", Fraction(1, 2)),
        ("z", Fraction(0)),
    )
    source = (
        ("z", Fraction(0)),
        ("x", Fraction(1, 4)),
        ("y", Fraction(3, 4)),
    )
    observable = (
        ("y", Fraction(5, 3)),
        ("z", Fraction(-9, 2)),
        ("x", Fraction(-2, 7)),
    )
    density = density_independently(source, reference)
    report("independent density agrees by labels", equal_by_label(density, rn_density(source, reference)), str(density))
    independent_direct = expectation_independently(source, observable)
    independent_changed = rn_expectation_independently(reference, density, observable)
    report("independent expectation agrees with primary", independent_direct == expectation(source, observable))
    report("independent RN expectation agrees with primary", independent_changed == rn_expectation(reference, density, observable))
    report("independent expectation identity closes", independent_direct == independent_changed)

    section("Independent three-packet cocycle")
    middle = (
        ("y", Fraction(1, 3)),
        ("z", Fraction(0)),
        ("x", Fraction(2, 3)),
    )
    direct = density_independently(source, reference)
    composed = compose_independently(
        density_independently(source, middle),
        density_independently(middle, reference),
    )
    report("independent cocycle agrees by labels", equal_by_label(composed, direct), str(composed))

    section("Independent malformed-input reconstruction")
    report("independent route rejects empty carrier", expect_raises(ValueError, lambda: normalize_independently(())))
    report(
        "independent route rejects zero total",
        expect_raises(
            ValueError,
            lambda: normalize_independently((("a", Fraction(0)), ("b", Fraction(0)))),
        ),
    )
    report(
        "independent route rejects negative weight",
        expect_raises(
            ValueError,
            lambda: normalize_independently((("a", Fraction(2)), ("b", Fraction(-1)))),
        ),
    )
    inexact = (("a", Fraction(1)), ("b", 0.5))
    report(
        "independent route rejects float",
        expect_raises(TypeError, lambda: normalize_independently(inexact)),  # type: ignore[arg-type]
    )
    unsupported = (("a", Fraction(0)), ("b", Fraction(1)))
    zero_reference = (("a", Fraction(1)), ("b", Fraction(0)))
    report(
        "independent route rejects unsupported source mass",
        expect_raises(
            ValueError,
            lambda: density_independently(unsupported, zero_reference),
        ),
    )


def hostile_mutation_acceptance(name: str) -> bool:
    """Return whether a false or malformed mutation incorrectly passes."""
    if name == "empty-carrier":
        return not expect_raises(ValueError, lambda: normalize_exact(()))
    if name == "zero-total":
        return not expect_raises(
            ValueError,
            lambda: normalize_exact((("a", Fraction(0)), ("b", Fraction(0)))),
        )
    if name == "negative-weight":
        return not expect_raises(
            ValueError,
            lambda: normalize_exact((("a", Fraction(2)), ("b", Fraction(-1)))),
        )
    if name == "float-weight":
        malformed = (("a", Fraction(1)), ("b", 0.5))
        return not expect_raises(TypeError, lambda: normalize_exact(malformed))  # type: ignore[arg-type]
    if name == "integer-weight":
        malformed = (("a", Fraction(1)), ("b", 1))
        return not expect_raises(TypeError, lambda: normalize_exact(malformed))  # type: ignore[arg-type]
    if name == "bool-weight":
        malformed = (("a", Fraction(1)), ("b", True))
        return not expect_raises(TypeError, lambda: normalize_exact(malformed))  # type: ignore[arg-type]
    if name == "fraction-subclass":
        malformed = (("a", Fraction(1)), ("b", FractionSubclass(1, 2)))
        return not expect_raises(TypeError, lambda: normalize_exact(malformed))  # type: ignore[arg-type]
    if name == "duplicate-label":
        return not expect_raises(
            ValueError,
            lambda: normalize_exact((("a", Fraction(1)), ("a", Fraction(2)))),
        )
    if name == "mismatched-carrier":
        source = (("a", Fraction(1)),)
        reference = (("b", Fraction(1)),)
        return not expect_raises(ValueError, lambda: rn_density(source, reference))
    if name == "unsupported-source-mass":
        source = (("a", Fraction(0)), ("b", Fraction(1)))
        reference = (("a", Fraction(1)), ("b", Fraction(0)))
        return not expect_raises(ValueError, lambda: rn_density(source, reference))
    if name == "nonexact-observable":
        probability = (("a", Fraction(1)),)
        observable = (("a", 0.5),)
        return not expect_raises(
            TypeError,
            lambda: expectation(probability, observable),  # type: ignore[arg-type]
        )
    if name == "mismatched-observable":
        probability = (("a", Fraction(1)),)
        observable = (("b", Fraction(1)),)
        return not expect_raises(ValueError, lambda: expectation(probability, observable))
    if name == "false-density":
        source = (("a", Fraction(1, 4)), ("b", Fraction(3, 4)))
        reference = (("a", Fraction(1, 2)), ("b", Fraction(1, 2)))
        candidate = (("a", Fraction(1)), ("b", Fraction(1)))
        return verify_density(source, reference, candidate)
    if name == "zero-zero-as-one":
        source = (("a", Fraction(1)), ("z", Fraction(0)))
        reference = (("a", Fraction(1)), ("z", Fraction(0)))
        candidate = (("a", Fraction(1)), ("z", Fraction(1)))
        return verify_density(source, reference, candidate)
    if name == "negative-density":
        source = (("a", Fraction(1, 4)), ("b", Fraction(3, 4)))
        reference = (("a", Fraction(1, 2)), ("b", Fraction(1, 2)))
        candidate = (("a", Fraction(-1, 2)), ("b", Fraction(5, 2)))
        return verify_density(source, reference, candidate)
    if name == "renormalized-density":
        source = (("a", Fraction(1, 4)), ("b", Fraction(3, 4)))
        reference = (("a", Fraction(1, 2)), ("b", Fraction(1, 2)))
        candidate = normalize_exact(rn_density(source, reference))
        return verify_density(source, reference, candidate)
    if name == "position-aligned-permutation":
        source = (("a", Fraction(1, 4)), ("b", Fraction(3, 4)))
        reference = (("b", Fraction(1, 4)), ("a", Fraction(3, 4)))
        positional = tuple(
            (source[index][0], source[index][1] / reference[index][1])
            for index in range(len(source))
        )
        return verify_density(source, reference, positional)
    if name == "unweighted-expectation":
        source = (("a", Fraction(1, 4)), ("b", Fraction(3, 4)))
        reference = (("a", Fraction(1, 2)), ("b", Fraction(1, 2)))
        observable = (("a", Fraction(-1)), ("b", Fraction(1)))
        density = rn_density(source, reference)
        mutated = sum(
            (dict(density)[label] * value for label, value in observable),
            Fraction(0),
        )
        return mutated == expectation(source, observable)
    if name == "broken-cocycle":
        reference = (("a", Fraction(1, 2)), ("b", Fraction(1, 2)))
        middle = (("a", Fraction(2, 3)), ("b", Fraction(1, 3)))
        source = (("a", Fraction(1, 4)), ("b", Fraction(3, 4)))
        first = dict(rn_density(source, middle))
        second = dict(rn_density(middle, reference))
        mutated = tuple((label, first[label] + second[label]) for label in first)
        return equal_by_label(mutated, rn_density(source, reference))
    if name == "physical-selection-inference":
        weights = (("a", Fraction(1)),)
        operation = lambda: normalize_exact(  # type: ignore[call-arg]
            weights,
            physical_reference="selected",
        )
        return not expect_raises(TypeError, operation)
    raise KeyError(f"unknown hostile fixture: {name}")


HOSTILE_FIXTURES = (
    "empty-carrier",
    "zero-total",
    "negative-weight",
    "float-weight",
    "integer-weight",
    "bool-weight",
    "fraction-subclass",
    "duplicate-label",
    "mismatched-carrier",
    "unsupported-source-mass",
    "nonexact-observable",
    "mismatched-observable",
    "false-density",
    "zero-zero-as-one",
    "negative-density",
    "renormalized-density",
    "position-aligned-permutation",
    "unweighted-expectation",
    "broken-cocycle",
    "physical-selection-inference",
)


def hostile_checks() -> None:
    section("Hostile mutation rejection")
    for name in HOSTILE_FIXTURES:
        accepted = hostile_mutation_acceptance(name)
        report(f"hostile mutation rejected: {name}", not accepted)


def intentional_failure_checks(fixture: str) -> None:
    section("Intentional hostile failure controls")
    selected = HOSTILE_FIXTURES if fixture == "all" else (fixture,)
    for name in selected:
        accepted = hostile_mutation_acceptance(name)
        report(
            f"intentional false acceptance must fail: {name}",
            accepted,
            "mutation did not satisfy the exact theorem contract",
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile", "intentional-failure"),
        default="normal",
    )
    aliases = parser.add_mutually_exclusive_group()
    aliases.add_argument("--independent", action="store_true", help="alias for --mode independent")
    aliases.add_argument("--hostile", action="store_true", help="alias for --mode hostile")
    parser.add_argument("--fixture", choices=("all",) + HOSTILE_FIXTURES, default="all")
    args = parser.parse_args()
    if args.independent:
        if args.mode != "normal":
            parser.error("--independent cannot combine with explicit non-normal --mode")
        args.mode = "independent"
    if args.hostile:
        if args.mode != "normal":
            parser.error("--hostile cannot combine with explicit non-normal --mode")
        args.mode = "hostile"
    if args.fixture != "all" and args.mode != "intentional-failure":
        parser.error("--fixture requires --mode intentional-failure")
    return args


def main() -> int:
    args = parse_args()
    source_scope_checks()
    if args.mode == "normal":
        normal_checks()
    elif args.mode == "independent":
        independent_checks()
    elif args.mode == "hostile":
        hostile_checks()
    else:
        intentional_failure_checks(args.fixture)
    print(f"\nSUMMARY: MODE={args.mode} PASS={PASS} FAIL={FAIL}")
    print("THEOREM_SCOPE=EXACT_FINITE_RATIONAL_NORMALIZATION_RN_EXPECTATION_AND_DENSITY_COCYCLE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
