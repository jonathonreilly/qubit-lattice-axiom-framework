#!/usr/bin/env python3
"""Exact finite deterministic pushforward and product-kernel transport theorem."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd
from pathlib import Path
import re
import sys
from typing import Callable, TypeAlias


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/POST_RECORD_PERSISTENT_RECORD_PRODUCTION_BRIDGE_PROTOTYPE_2026-06-06.md"

Identifier: TypeAlias = str
ProbabilityPacket: TypeAlias = tuple[tuple[Identifier, Fraction], ...]
TargetCarrier: TypeAlias = tuple[Identifier, ...]
MapPacket: TypeAlias = tuple[tuple[Identifier, Identifier], ...]
ObservablePacket: TypeAlias = tuple[tuple[Identifier, Fraction], ...]
KernelPacket: TypeAlias = tuple[tuple[Identifier, Identifier, Fraction], ...]
CountState: TypeAlias = tuple[int, int, str]

PASS = 0
FAIL = 0


class FractionSubclass(Fraction):
    """Hostile fixture: subclasses are outside the strict numeric contract."""


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


def exact_identifier(value: object, context: str) -> str:
    if type(value) is not str or not value:
        raise TypeError(f"{context} must have exact runtime type str and be nonempty")
    return value


def exact_fraction(value: object, context: str) -> Fraction:
    if type(value) is not Fraction:
        raise TypeError(f"{context} must have exact runtime type Fraction")
    return value


def carrier_labels(carrier: TargetCarrier, context: str) -> tuple[str, ...]:
    if type(carrier) is not tuple or not carrier:
        raise ValueError(f"{context} must be a nonempty tuple")
    labels: list[str] = []
    seen: set[str] = set()
    for raw_label in carrier:
        label = exact_identifier(raw_label, f"{context} label")
        if label in seen:
            raise ValueError(f"duplicate {context} label: {label}")
        seen.add(label)
        labels.append(label)
    return tuple(labels)


def probability_entries(packet: ProbabilityPacket, context: str) -> tuple[tuple[str, Fraction], ...]:
    if type(packet) is not tuple or not packet:
        raise ValueError(f"{context} must be a nonempty tuple")
    entries: list[tuple[str, Fraction]] = []
    seen: set[str] = set()
    for item in packet:
        if type(item) is not tuple or len(item) != 2:
            raise TypeError(f"{context} entries must be (identifier, Fraction) tuples")
        raw_label, raw_value = item
        label = exact_identifier(raw_label, f"{context} identifier")
        value = exact_fraction(raw_value, f"{context}[{label}]")
        if label in seen:
            raise ValueError(f"duplicate {context} identifier: {label}")
        seen.add(label)
        entries.append((label, value))
    return tuple(entries)


def probability_map(packet: ProbabilityPacket, context: str) -> dict[str, Fraction]:
    entries = probability_entries(packet, context)
    if any(value < 0 for _, value in entries):
        raise ValueError(f"{context} values must be nonnegative")
    if sum((value for _, value in entries), Fraction(0)) != 1:
        raise ValueError(f"{context} must sum exactly to one")
    return dict(entries)


def deterministic_map(
    probability: ProbabilityPacket,
    targets: TargetCarrier,
    mapping: MapPacket,
) -> dict[str, str]:
    source_values = probability_map(probability, "source probability")
    target_labels = carrier_labels(targets, "target carrier")
    if type(mapping) is not tuple or not mapping:
        raise ValueError("deterministic map must be a nonempty tuple")
    values: dict[str, str] = {}
    for item in mapping:
        if type(item) is not tuple or len(item) != 2:
            raise TypeError("map entries must be (source, target) tuples")
        raw_source, raw_target = item
        source = exact_identifier(raw_source, "map source identifier")
        target = exact_identifier(raw_target, "map target identifier")
        if source in values:
            raise ValueError(f"map source appears more than once: {source}")
        if target not in target_labels:
            raise ValueError(f"map target is outside supplied carrier: {target}")
        values[source] = target
    if set(values) != set(source_values):
        raise ValueError("deterministic map domain must equal the source carrier")
    return values


def observable_map(targets: TargetCarrier, observable: ObservablePacket) -> dict[str, Fraction]:
    target_labels = carrier_labels(targets, "target carrier")
    if type(observable) is not tuple or not observable:
        raise ValueError("observable must be a nonempty tuple")
    values: dict[str, Fraction] = {}
    for item in observable:
        if type(item) is not tuple or len(item) != 2:
            raise TypeError("observable entries must be (target, Fraction) tuples")
        raw_target, raw_value = item
        target = exact_identifier(raw_target, "observable target identifier")
        value = exact_fraction(raw_value, f"observable[{target}]")
        if target in values:
            raise ValueError(f"duplicate observable target: {target}")
        values[target] = value
    if set(values) != set(target_labels):
        raise ValueError("observable domain must equal the target carrier")
    return values


def kernel_map(targets: TargetCarrier, kernel: KernelPacket) -> dict[tuple[str, str], Fraction]:
    target_labels = carrier_labels(targets, "target carrier")
    if type(kernel) is not tuple or not kernel:
        raise ValueError("kernel must be a nonempty tuple")
    values: dict[tuple[str, str], Fraction] = {}
    for item in kernel:
        if type(item) is not tuple or len(item) != 3:
            raise TypeError("kernel entries must be (left, right, Fraction) tuples")
        raw_left, raw_right, raw_value = item
        left = exact_identifier(raw_left, "kernel left identifier")
        right = exact_identifier(raw_right, "kernel right identifier")
        value = exact_fraction(raw_value, f"kernel[{left},{right}]")
        pair = (left, right)
        if pair in values:
            raise ValueError(f"duplicate kernel pair: {pair}")
        values[pair] = value
    expected = {(left, right) for left in target_labels for right in target_labels}
    if set(values) != expected:
        raise ValueError("kernel domain must equal the full ordered product Y x Y")
    return values


def pushforward(
    probability: ProbabilityPacket,
    targets: TargetCarrier,
    mapping: MapPacket,
) -> ProbabilityPacket:
    source_values = probability_map(probability, "source probability")
    target_labels = carrier_labels(targets, "target carrier")
    images = deterministic_map(probability, targets, mapping)
    masses = {target: Fraction(0) for target in target_labels}
    for source, value in source_values.items():
        masses[images[source]] += value
    return tuple((target, masses[target]) for target in target_labels)


def target_expectation(
    target_probability: ProbabilityPacket,
    targets: TargetCarrier,
    observable: ObservablePacket,
) -> Fraction:
    probabilities = probability_map(target_probability, "target probability")
    target_labels = carrier_labels(targets, "target carrier")
    if set(probabilities) != set(target_labels):
        raise ValueError("target probability carrier mismatch")
    values = observable_map(targets, observable)
    return sum(
        (probabilities[target] * values[target] for target in target_labels),
        Fraction(0),
    )


def source_pullback_expectation(
    probability: ProbabilityPacket,
    targets: TargetCarrier,
    mapping: MapPacket,
    observable: ObservablePacket,
) -> Fraction:
    probabilities = probability_map(probability, "source probability")
    images = deterministic_map(probability, targets, mapping)
    values = observable_map(targets, observable)
    return sum(
        (probabilities[source] * values[images[source]] for source in probabilities),
        Fraction(0),
    )


def target_kernel_expectation(
    target_probability: ProbabilityPacket,
    targets: TargetCarrier,
    kernel: KernelPacket,
) -> Fraction:
    probabilities = probability_map(target_probability, "target probability")
    target_labels = carrier_labels(targets, "target carrier")
    if set(probabilities) != set(target_labels):
        raise ValueError("target probability carrier mismatch")
    values = kernel_map(targets, kernel)
    return sum(
        (
            probabilities[left]
            * probabilities[right]
            * values[(left, right)]
            for left in target_labels
            for right in target_labels
        ),
        Fraction(0),
    )


def source_kernel_expectation(
    probability: ProbabilityPacket,
    targets: TargetCarrier,
    mapping: MapPacket,
    kernel: KernelPacket,
) -> Fraction:
    probabilities = probability_map(probability, "source probability")
    images = deterministic_map(probability, targets, mapping)
    values = kernel_map(targets, kernel)
    return sum(
        (
            probabilities[left]
            * probabilities[right]
            * values[(images[left], images[right])]
            for left in probabilities
            for right in probabilities
        ),
        Fraction(0),
    )


def equal_by_label(left: ProbabilityPacket, right: ProbabilityPacket) -> bool:
    try:
        return probability_map(left, "left probability") == probability_map(
            right, "right probability"
        )
    except (TypeError, ValueError):
        return False


def verify_pushforward(
    probability: ProbabilityPacket,
    targets: TargetCarrier,
    mapping: MapPacket,
    candidate: ProbabilityPacket,
) -> bool:
    try:
        target_labels = carrier_labels(targets, "target carrier")
        candidate_values = probability_map(candidate, "candidate pushforward")
        expected = pushforward(probability, targets, mapping)
    except (TypeError, ValueError):
        return False
    return (
        tuple(label for label, _ in candidate) == target_labels
        and candidate_values == dict(expected)
    )


def kernel_properties(targets: TargetCarrier, kernel: KernelPacket) -> dict[str, bool]:
    labels = carrier_labels(targets, "target carrier")
    values = kernel_map(targets, kernel)
    return {
        "symmetric": all(
            values[(left, right)] == values[(right, left)]
            for left in labels
            for right in labels
        ),
        "positive_unit_bounded": all(Fraction(0) < value <= 1 for value in values.values()),
        "self_one": all(values[(label, label)] == 1 for label in labels),
    }


def lcm(left: int, right: int) -> int:
    return abs(left * right) // gcd(left, right) if left and right else 0


def independent_probability_entries(
    packet: ProbabilityPacket,
) -> tuple[tuple[str, Fraction], ...]:
    if type(packet) is not tuple or len(packet) == 0:
        raise ValueError("independent probability carrier is empty or non-tuple")
    checked: list[tuple[str, Fraction]] = []
    labels: list[str] = []
    for item in packet:
        if type(item) is not tuple or len(item) != 2:
            raise TypeError("independent malformed probability entry")
        raw_label, raw_value = item
        if type(raw_label) is not str or raw_label == "":
            raise TypeError("independent probability identifier is not a strict string")
        if raw_label in labels:
            raise ValueError("independent duplicate probability identifier")
        if type(raw_value) is not Fraction:
            raise TypeError("independent probability value is not a strict Fraction")
        if raw_value < 0:
            raise ValueError("independent probability value is negative")
        labels.append(raw_label)
        checked.append((raw_label, raw_value))
    denominator = 1
    for _, value in checked:
        denominator = lcm(denominator, value.denominator)
    integer_total = sum(
        value.numerator * (denominator // value.denominator)
        for _, value in checked
    )
    if integer_total != denominator:
        raise ValueError("independent probability is not normalized")
    return tuple(checked)


def independent_target_labels(targets: TargetCarrier) -> tuple[str, ...]:
    if type(targets) is not tuple or len(targets) == 0:
        raise ValueError("independent target carrier is empty or non-tuple")
    labels: list[str] = []
    for target in targets:
        if type(target) is not str or target == "":
            raise TypeError("independent target identifier is not a strict string")
        if target in labels:
            raise ValueError("independent duplicate target identifier")
        labels.append(target)
    return tuple(labels)


def independent_mapping_entries(
    probability: ProbabilityPacket,
    targets: TargetCarrier,
    mapping: MapPacket,
) -> tuple[tuple[str, str], ...]:
    source = independent_probability_entries(probability)
    target_labels = independent_target_labels(targets)
    if type(mapping) is not tuple or len(mapping) == 0:
        raise ValueError("independent map is empty or non-tuple")
    checked: list[tuple[str, str]] = []
    mapped_sources: list[str] = []
    for item in mapping:
        if type(item) is not tuple or len(item) != 2:
            raise TypeError("independent malformed map entry")
        raw_source, raw_target = item
        if type(raw_source) is not str or not raw_source:
            raise TypeError("independent map source is not a strict string")
        if type(raw_target) is not str or not raw_target:
            raise TypeError("independent map target is not a strict string")
        if raw_source in mapped_sources:
            raise ValueError("independent map source is repeated")
        if raw_target not in target_labels:
            raise ValueError("independent map target is outside carrier")
        mapped_sources.append(raw_source)
        checked.append((raw_source, raw_target))
    if sorted(mapped_sources) != sorted(label for label, _ in source):
        raise ValueError("independent map is not total on the source carrier")
    return tuple(checked)


def independent_observable_entries(
    targets: TargetCarrier,
    observable: ObservablePacket,
) -> tuple[tuple[str, Fraction], ...]:
    target_labels = independent_target_labels(targets)
    if type(observable) is not tuple or len(observable) == 0:
        raise ValueError("independent observable is empty or non-tuple")
    checked: list[tuple[str, Fraction]] = []
    labels: list[str] = []
    for item in observable:
        if type(item) is not tuple or len(item) != 2:
            raise TypeError("independent malformed observable entry")
        raw_label, raw_value = item
        if type(raw_label) is not str or not raw_label:
            raise TypeError("independent observable target is not a strict string")
        if raw_label in labels:
            raise ValueError("independent duplicate observable target")
        if type(raw_value) is not Fraction:
            raise TypeError("independent observable value is not a strict Fraction")
        labels.append(raw_label)
        checked.append((raw_label, raw_value))
    if sorted(labels) != sorted(target_labels):
        raise ValueError("independent observable domain mismatch")
    return tuple(checked)


def independent_kernel_entries(
    targets: TargetCarrier,
    kernel: KernelPacket,
) -> tuple[tuple[str, str, Fraction], ...]:
    target_labels = independent_target_labels(targets)
    if type(kernel) is not tuple or len(kernel) == 0:
        raise ValueError("independent kernel is empty or non-tuple")
    checked: list[tuple[str, str, Fraction]] = []
    pairs: list[tuple[str, str]] = []
    for item in kernel:
        if type(item) is not tuple or len(item) != 3:
            raise TypeError("independent malformed kernel entry")
        raw_left, raw_right, raw_value = item
        if type(raw_left) is not str or not raw_left:
            raise TypeError("independent kernel left target is not a strict string")
        if type(raw_right) is not str or not raw_right:
            raise TypeError("independent kernel right target is not a strict string")
        if type(raw_value) is not Fraction:
            raise TypeError("independent kernel value is not a strict Fraction")
        pair = (raw_left, raw_right)
        if pair in pairs:
            raise ValueError("independent duplicate kernel pair")
        pairs.append(pair)
        checked.append((raw_left, raw_right, raw_value))
    expected = [(left, right) for left in target_labels for right in target_labels]
    if sorted(pairs) != sorted(expected):
        raise ValueError("independent kernel domain mismatch")
    return tuple(checked)


def independent_common_counts(
    probability: ProbabilityPacket,
) -> tuple[tuple[tuple[str, int], ...], int]:
    entries = independent_probability_entries(probability)
    denominator = 1
    for _, value in entries:
        denominator = lcm(denominator, value.denominator)
    counts = tuple(
        (label, value.numerator * (denominator // value.denominator))
        for label, value in entries
    )
    return counts, denominator


def independent_lookup_image(mapping: tuple[tuple[str, str], ...], source: str) -> str:
    matches = [target for candidate, target in mapping if candidate == source]
    if len(matches) != 1:
        raise ValueError("independent map lookup is not single-valued")
    return matches[0]


def independent_lookup_observable(
    observable: tuple[tuple[str, Fraction], ...], target: str
) -> Fraction:
    matches = [value for candidate, value in observable if candidate == target]
    if len(matches) != 1:
        raise ValueError("independent observable lookup is not single-valued")
    return matches[0]


def independent_lookup_kernel(
    kernel: tuple[tuple[str, str, Fraction], ...], left: str, right: str
) -> Fraction:
    matches = [
        value
        for candidate_left, candidate_right, value in kernel
        if candidate_left == left and candidate_right == right
    ]
    if len(matches) != 1:
        raise ValueError("independent kernel lookup is not single-valued")
    return matches[0]


def pushforward_independently(
    probability: ProbabilityPacket,
    targets: TargetCarrier,
    mapping: MapPacket,
) -> ProbabilityPacket:
    target_labels = independent_target_labels(targets)
    map_entries = independent_mapping_entries(probability, targets, mapping)
    source_counts, denominator = independent_common_counts(probability)
    output: list[tuple[str, Fraction]] = []
    for target in target_labels:
        mass_count = sum(
            count
            for source, count in source_counts
            if independent_lookup_image(map_entries, source) == target
        )
        output.append((target, Fraction(mass_count, denominator)))
    return tuple(output)


def observable_transport_independently(
    probability: ProbabilityPacket,
    targets: TargetCarrier,
    mapping: MapPacket,
    observable: ObservablePacket,
) -> tuple[Fraction, Fraction]:
    map_entries = independent_mapping_entries(probability, targets, mapping)
    observable_entries = independent_observable_entries(targets, observable)
    source_counts, denominator = independent_common_counts(probability)
    pushed = pushforward_independently(probability, targets, mapping)
    target_total = sum(
        (
            mass
            * independent_lookup_observable(observable_entries, target)
            for target, mass in pushed
        ),
        Fraction(0),
    )
    source_numerator = sum(
        (
            Fraction(count, denominator)
            * independent_lookup_observable(
                observable_entries,
                independent_lookup_image(map_entries, source),
            )
            for source, count in source_counts
        ),
        Fraction(0),
    )
    return target_total, source_numerator


def kernel_transport_independently(
    probability: ProbabilityPacket,
    targets: TargetCarrier,
    mapping: MapPacket,
    kernel: KernelPacket,
) -> tuple[Fraction, Fraction]:
    map_entries = independent_mapping_entries(probability, targets, mapping)
    kernel_entries = independent_kernel_entries(targets, kernel)
    source_counts, denominator = independent_common_counts(probability)
    pushed = pushforward_independently(probability, targets, mapping)
    target_total = sum(
        (
            left_mass
            * right_mass
            * independent_lookup_kernel(kernel_entries, left, right)
            for left, left_mass in pushed
            for right, right_mass in pushed
        ),
        Fraction(0),
    )
    source_total = sum(
        (
            Fraction(left_count * right_count, denominator * denominator)
            * independent_lookup_kernel(
                kernel_entries,
                independent_lookup_image(map_entries, left),
                independent_lookup_image(map_entries, right),
            )
            for left, left_count in source_counts
            for right, right_count in source_counts
        ),
        Fraction(0),
    )
    return target_total, source_total


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
    report("source note exists", NOTE.is_file())
    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    required = (
        "**Claim type:** positive_theorem",
        "**Dependencies:** none.",
        "Q(y) = sum_{x in X : F(x)=y} P(x).",
        "sum_{x in X} P(x) h(F(x)).",
        "sum_{x,x' in X} P(x) P(x') K(F(x),F(x')).",
        "The map must be total on `X`; its image may be a proper subset of `Y`.",
        "The legacy path name is an identifier",
        "repository metadata outside the theorem arguments",
    )
    for phrase in required:
        report(f"source contains theorem anchor: {phrase}", phrase in flat)
    forbidden_patterns = (
        r"persistent_record_production_overlap` rows",
        r"production row map has exactly three",
        r"frontier_post_record_audit_evidence_ladder_row_bucketing_2026_06_06\.py",
        r"frontier_post_record_production_dynamics_needed_row_map_2026_06_06\.py",
        r"docs/audit/data/",
        r"\baudit_status\s*:",
        r"\beffective_status\s*:",
        r"\bRecord (?:derives|supplies|selects|fixes)\b",
        r"\bphysical (?:production|record-writing) (?:law|kernel) (?:is|follows)\b",
        r"PERSISTENT_RECORD_PRODUCTION_OVERLAP_ROWS",
        r"SUPPLIED_RECORD_WRITING_BRIDGE_PROTOTYPE",
    )
    for pattern in forbidden_patterns:
        report(
            f"source excludes stale or physical overclaim: {pattern}",
            re.search(pattern, flat, flags=re.IGNORECASE) is None,
        )


def simple_example() -> tuple[
    ProbabilityPacket,
    TargetCarrier,
    MapPacket,
    ObservablePacket,
    KernelPacket,
]:
    probability = (
        ("a", Fraction(1, 2)),
        ("b", Fraction(1, 3)),
        ("c", Fraction(1, 6)),
    )
    targets = ("red", "blue", "unused")
    mapping = (("b", "red"), ("c", "blue"), ("a", "red"))
    observable = (
        ("unused", Fraction(11)),
        ("blue", Fraction(5)),
        ("red", Fraction(-2)),
    )
    kernel = tuple(
        (
            left,
            right,
            Fraction(
                (1 if left <= right else -1) * (left_index + 2 * right_index + 1),
                left_index + right_index + 1,
            ),
        )
        for left_index, left in enumerate(targets)
        for right_index, right in enumerate(targets)
    )
    return probability, targets, mapping, observable, kernel


def word_example() -> tuple[ProbabilityPacket, TargetCarrier, MapPacket, KernelPacket]:
    probability = (
        ("LL", Fraction(1, 2)),
        ("LR", Fraction(1, 4)),
        ("RL", Fraction(1, 8)),
        ("RR", Fraction(1, 8)),
    )
    targets = ("2:0:L", "1:1:L", "1:1:R", "0:2:R")
    mapping = (
        ("LL", "2:0:L"),
        ("LR", "1:1:L"),
        ("RL", "1:1:R"),
        ("RR", "0:2:R"),
    )

    def coordinates(label: str) -> tuple[int, int, str]:
        left, right, marker = label.split(":")
        return int(left), int(right), marker

    kernel_entries: list[tuple[str, str, Fraction]] = []
    for left_label in targets:
        left_count, right_count, left_marker = coordinates(left_label)
        for right_label in targets:
            other_left, other_right, right_marker = coordinates(right_label)
            distance = (
                (left_count - other_left) ** 2
                + (right_count - other_right) ** 2
                + (0 if left_marker == right_marker else 1)
            )
            kernel_entries.append((left_label, right_label, Fraction(1, 1 + distance)))
    return probability, targets, mapping, tuple(kernel_entries)


def update_count_state(state: CountState, symbol: str) -> CountState:
    left, right, marker = state
    if symbol == "L":
        return min(2, left + 1), right, "L" if marker == "none" else marker
    if symbol == "R":
        return left, min(2, right + 1), "R" if marker == "none" else marker
    raise ValueError("count update symbol must be L or R")


def normal_checks() -> None:
    probability, targets, mapping, observable, kernel = simple_example()
    section("Exact finite pushforward")
    pushed = pushforward(probability, targets, mapping)
    expected = (
        ("red", Fraction(5, 6)),
        ("blue", Fraction(1, 6)),
        ("unused", Fraction(0)),
    )
    report("colliding fibers sum exactly", pushed == expected, str(pushed))
    report("pushforward is nonnegative", all(value >= 0 for _, value in pushed))
    report(
        "pushforward is normalized exactly",
        sum((value for _, value in pushed), Fraction(0)) == 1,
    )
    report("unused target is retained with zero mass", dict(pushed)["unused"] == 0)
    report("pushforward verifies by target-label semantics", verify_pushforward(probability, targets, mapping, pushed))

    section("Observable pullback identity")
    target_value = target_expectation(pushed, targets, observable)
    source_value = source_pullback_expectation(probability, targets, mapping, observable)
    report("signed observable target expectation is exact", target_value == Fraction(-5, 6), str(target_value))
    report("observable pullback identity is exact", target_value == source_value, str(source_value))

    section("Arbitrary product-kernel transport")
    target_kernel_value = target_kernel_expectation(pushed, targets, kernel)
    source_kernel_value = source_kernel_expectation(probability, targets, mapping, kernel)
    properties = kernel_properties(targets, kernel)
    report("arbitrary signed asymmetric kernel transports exactly", target_kernel_value == source_kernel_value, str(target_kernel_value))
    report("transport theorem does not require symmetry", not properties["symmetric"])
    report("transport theorem does not require unit bounds", not properties["positive_unit_bounded"])
    report("transport theorem does not require diagonal one", not properties["self_one"])

    section("Defined word/count example")
    word_probability, word_targets, word_mapping, word_kernel = word_example()
    word_pushed = pushforward(word_probability, word_targets, word_mapping)
    word_properties = kernel_properties(word_targets, word_kernel)
    overlap = target_kernel_expectation(word_pushed, word_targets, word_kernel)
    overlap_source = source_kernel_expectation(word_probability, word_targets, word_mapping, word_kernel)
    report("word/count image packet is exact", word_pushed == tuple((target, value) for target, (_, value) in zip(word_targets, word_probability)), str(word_pushed))
    report("defined word kernel is symmetric", word_properties["symmetric"])
    report("defined word kernel is positive and at most one", word_properties["positive_unit_bounded"])
    report("defined word kernel equals one on the diagonal", word_properties["self_one"])
    report("defined word example product expectation is 169/320", overlap == Fraction(169, 320), str(overlap))
    report("word example also closes through source-product transport", overlap == overlap_source)

    state: CountState = (0, 0, "none")
    history = [state]
    for symbol in ("R", "L", "L", "R"):
        state = update_count_state(state, symbol)
        history.append(state)
    report(
        "defined capped counts are componentwise nondecreasing",
        all(
            history[index][0] <= history[index + 1][0]
            and history[index][1] <= history[index + 1][1]
            for index in range(len(history) - 1)
        ),
        str(history),
    )
    report(
        "defined first marker is unchanged after its first assignment",
        history[1][2] == "R" and all(item[2] == "R" for item in history[1:]),
        str(history),
    )

    section("Ordering and carrier permutations")
    permuted_probability = tuple(reversed(probability))
    permuted_targets = (targets[1], targets[2], targets[0])
    permuted_mapping = tuple(reversed(mapping))
    permuted_observable = tuple(reversed(observable))
    permuted_kernel = tuple(reversed(kernel))
    permuted_pushed = pushforward(permuted_probability, permuted_targets, permuted_mapping)
    report("pushforward is permutation-equivariant by target label", equal_by_label(permuted_pushed, pushed))
    report(
        "observable identity is permutation-invariant",
        source_pullback_expectation(permuted_probability, permuted_targets, permuted_mapping, permuted_observable)
        == target_value,
    )
    report(
        "kernel identity is permutation-invariant",
        source_kernel_expectation(permuted_probability, permuted_targets, permuted_mapping, permuted_kernel)
        == target_kernel_value,
    )


def generated_cases() -> tuple[
    tuple[ProbabilityPacket, TargetCarrier, MapPacket, ObservablePacket, KernelPacket], ...
]:
    cases: list[
        tuple[ProbabilityPacket, TargetCarrier, MapPacket, ObservablePacket, KernelPacket]
    ] = []
    for source_size in range(1, 6):
        for target_size in range(1, 5):
            for variant in range(3):
                source_labels = tuple(f"s{source_size}_{index}" for index in range(source_size))
                targets = tuple(f"t{target_size}_{index}" for index in range(target_size))
                counts = [
                    (index + 1) * (variant + 2) + ((source_size + index + variant) % 3)
                    for index in range(source_size)
                ]
                if source_size >= 3:
                    counts[(source_size + variant) % source_size] = 0
                total = sum(counts)
                probability = tuple(
                    (label, Fraction(count, total))
                    for label, count in zip(source_labels, counts)
                )
                mapping = tuple(
                    (
                        source,
                        targets[(index * (variant + 1) + source_size + variant) % target_size],
                    )
                    for index, source in enumerate(source_labels)
                )
                observable = tuple(
                    (
                        target,
                        Fraction(
                            (-1 if (index + variant) % 2 else 1) * (index + variant + 2),
                            variant + 1,
                        ),
                    )
                    for index, target in enumerate(targets)
                )
                kernel = tuple(
                    (
                        left,
                        right,
                        Fraction(
                            (-1 if (left_index + 2 * right_index + variant) % 2 else 1)
                            * (left_index + right_index + variant + 1),
                            left_index + 2 * right_index + 1,
                        ),
                    )
                    for left_index, left in enumerate(targets)
                    for right_index, right in enumerate(targets)
                )
                cases.append((probability, targets, mapping, observable, kernel))
    return tuple(cases)


def independent_checks() -> None:
    section("Independent reconstruction of the defined word/count example")
    word_probability, word_targets, word_mapping, word_kernel = word_example()
    word_primary = pushforward(word_probability, word_targets, word_mapping)
    word_independent = pushforward_independently(
        word_probability, word_targets, word_mapping
    )
    word_target, word_source = kernel_transport_independently(
        word_probability, word_targets, word_mapping, word_kernel
    )
    report(
        "independent word/count pushforward agrees by label",
        equal_by_label(word_independent, word_primary),
        str(word_independent),
    )
    report(
        "independent target-product example equals 169/320",
        word_target == Fraction(169, 320),
        str(word_target),
    )
    report(
        "independent source-product example equals 169/320",
        word_source == Fraction(169, 320),
        str(word_source),
    )

    section("Independent common-denominator finite-family oracle")
    cases = generated_cases()
    primary_independent_pushforward = True
    normalized = True
    observable_primary = True
    observable_independent = True
    kernel_primary = True
    kernel_independent = True
    permutation_equivariance = True
    for probability, targets, mapping, observable, kernel in cases:
        primary = pushforward(probability, targets, mapping)
        independent = pushforward_independently(probability, targets, mapping)
        primary_independent_pushforward &= equal_by_label(primary, independent)
        normalized &= sum((value for _, value in independent), Fraction(0)) == 1

        primary_target_observable = target_expectation(primary, targets, observable)
        primary_source_observable = source_pullback_expectation(
            probability, targets, mapping, observable
        )
        independent_target_observable, independent_source_observable = (
            observable_transport_independently(probability, targets, mapping, observable)
        )
        observable_primary &= primary_target_observable == primary_source_observable
        observable_independent &= (
            independent_target_observable
            == independent_source_observable
            == primary_target_observable
        )

        primary_target_kernel = target_kernel_expectation(primary, targets, kernel)
        primary_source_kernel = source_kernel_expectation(
            probability, targets, mapping, kernel
        )
        independent_target_kernel, independent_source_kernel = (
            kernel_transport_independently(probability, targets, mapping, kernel)
        )
        kernel_primary &= primary_target_kernel == primary_source_kernel
        kernel_independent &= (
            independent_target_kernel
            == independent_source_kernel
            == primary_target_kernel
        )

        permuted_probability = tuple(reversed(probability))
        permuted_targets = tuple(reversed(targets))
        permuted_mapping = tuple(reversed(mapping))
        permuted_observable = tuple(reversed(observable))
        permuted_kernel = tuple(reversed(kernel))
        permuted = pushforward_independently(
            permuted_probability, permuted_targets, permuted_mapping
        )
        permutation_equivariance &= equal_by_label(permuted, primary)
        permuted_observable_pair = observable_transport_independently(
            permuted_probability,
            permuted_targets,
            permuted_mapping,
            permuted_observable,
        )
        permuted_kernel_pair = kernel_transport_independently(
            permuted_probability,
            permuted_targets,
            permuted_mapping,
            permuted_kernel,
        )
        permutation_equivariance &= (
            permuted_observable_pair[0] == primary_target_observable
            and permuted_observable_pair[1] == primary_target_observable
            and permuted_kernel_pair[0] == primary_target_kernel
            and permuted_kernel_pair[1] == primary_target_kernel
        )

    report("independent oracle exercises sixty finite theorem instances", len(cases) == 60)
    report("independent integer-count pushforwards agree by label", primary_independent_pushforward)
    report("all independent pushforwards remain normalized", normalized)
    report("all primary observable identities close", observable_primary)
    report("all independently coded observable identities close", observable_independent)
    report("all primary product-kernel identities close", kernel_primary)
    report("all independently coded product-kernel identities close", kernel_independent)
    report("all independent tuple permutations preserve theorem values", permutation_equivariance)

    section("Independent malformed-domain checks")
    probability, targets, mapping, observable, kernel = simple_example()
    report(
        "independent route rejects incomplete map",
        expect_raises(
            ValueError,
            lambda: pushforward_independently(probability, targets, mapping[:-1]),
        ),
    )
    report(
        "independent route rejects inexact probability",
        expect_raises(
            TypeError,
            lambda: pushforward_independently(
                (("a", Fraction(1, 2)), ("b", 0.5)),  # type: ignore[arg-type]
                ("y",),
                (("a", "y"), ("b", "y")),
            ),
        ),
    )
    report(
        "independent route rejects incomplete observable",
        expect_raises(
            ValueError,
            lambda: observable_transport_independently(
                probability, targets, mapping, observable[:-1]
            ),
        ),
    )
    report(
        "independent route rejects incomplete kernel",
        expect_raises(
            ValueError,
            lambda: kernel_transport_independently(
                probability, targets, mapping, kernel[:-1]
            ),
        ),
    )


def hostile_mutation_acceptance(name: str) -> bool:
    probability, targets, mapping, observable, kernel = simple_example()
    if name == "empty-law":
        return not expect_raises(ValueError, lambda: pushforward((), targets, ()))
    if name == "unnormalized-law":
        bad = (("a", Fraction(1, 2)), ("b", Fraction(1, 3)))
        return not expect_raises(ValueError, lambda: pushforward(bad, ("y",), (("a", "y"), ("b", "y"))))
    if name == "negative-law":
        bad = (("a", Fraction(3, 2)), ("b", Fraction(-1, 2)))
        return not expect_raises(ValueError, lambda: pushforward(bad, ("y",), (("a", "y"), ("b", "y"))))
    if name == "float-law":
        bad = (("a", Fraction(1, 2)), ("b", 0.5))
        return not expect_raises(TypeError, lambda: pushforward(bad, ("y",), (("a", "y"), ("b", "y"))))  # type: ignore[arg-type]
    if name == "integer-law":
        bad = (("a", Fraction(0)), ("b", 1))
        return not expect_raises(TypeError, lambda: pushforward(bad, ("y",), (("a", "y"), ("b", "y"))))  # type: ignore[arg-type]
    if name == "bool-law":
        bad = (("a", Fraction(0)), ("b", True))
        return not expect_raises(TypeError, lambda: pushforward(bad, ("y",), (("a", "y"), ("b", "y"))))  # type: ignore[arg-type]
    if name == "fraction-subclass-law":
        bad = (("a", Fraction(1, 2)), ("b", FractionSubclass(1, 2)))
        return not expect_raises(TypeError, lambda: pushforward(bad, ("y",), (("a", "y"), ("b", "y"))))  # type: ignore[arg-type]
    if name == "duplicate-source":
        bad = (("a", Fraction(1, 2)), ("a", Fraction(1, 2)))
        return not expect_raises(ValueError, lambda: pushforward(bad, ("y",), (("a", "y"),)))
    if name == "empty-target-carrier":
        return not expect_raises(ValueError, lambda: pushforward((("a", Fraction(1)),), (), (("a", "y"),)))
    if name == "duplicate-target-carrier":
        return not expect_raises(ValueError, lambda: pushforward((("a", Fraction(1)),), ("y", "y"), (("a", "y"),)))
    if name == "incomplete-map":
        return not expect_raises(ValueError, lambda: pushforward(probability, targets, mapping[:-1]))
    if name == "map-extra-source":
        bad_map = mapping + (("ghost", "red"),)
        return not expect_raises(ValueError, lambda: pushforward(probability, targets, bad_map))
    if name == "map-target-outside":
        bad_map = (("a", "red"), ("b", "blue"), ("c", "ghost"))
        return not expect_raises(ValueError, lambda: pushforward(probability, targets, bad_map))
    if name == "nonexact-map-source":
        bad_map = ((1, "red"), ("b", "red"), ("c", "blue"))
        return not expect_raises(TypeError, lambda: pushforward(probability, targets, bad_map))  # type: ignore[arg-type]
    if name == "nonexact-map-target":
        bad_map = (("a", 1), ("b", "red"), ("c", "blue"))
        return not expect_raises(TypeError, lambda: pushforward(probability, targets, bad_map))  # type: ignore[arg-type]
    if name == "duplicate-map-source":
        bad_map = (("a", "red"), ("a", "blue"), ("c", "blue"))
        return not expect_raises(ValueError, lambda: pushforward(probability, targets, bad_map))
    if name == "observable-missing-target":
        return not expect_raises(ValueError, lambda: source_pullback_expectation(probability, targets, mapping, observable[:-1]))
    if name == "observable-extra-target":
        bad = observable + (("ghost", Fraction(0)),)
        return not expect_raises(ValueError, lambda: source_pullback_expectation(probability, targets, mapping, bad))
    if name == "observable-inexact":
        bad = (("red", Fraction(0)), ("blue", Fraction(0)), ("unused", 0.0))
        return not expect_raises(TypeError, lambda: source_pullback_expectation(probability, targets, mapping, bad))  # type: ignore[arg-type]
    if name == "kernel-missing-pair":
        return not expect_raises(ValueError, lambda: source_kernel_expectation(probability, targets, mapping, kernel[:-1]))
    if name == "kernel-extra-pair":
        bad = kernel + (("red", "ghost", Fraction(0)),)
        return not expect_raises(ValueError, lambda: source_kernel_expectation(probability, targets, mapping, bad))
    if name == "kernel-duplicate-pair":
        bad = kernel + (kernel[0],)
        return not expect_raises(ValueError, lambda: source_kernel_expectation(probability, targets, mapping, bad))
    if name == "kernel-inexact":
        bad = kernel[:-1] + ((kernel[-1][0], kernel[-1][1], 0.5),)
        return not expect_raises(TypeError, lambda: source_kernel_expectation(probability, targets, mapping, bad))  # type: ignore[arg-type]
    if name == "wrong-pushforward":
        candidate = (("red", Fraction(1, 6)), ("blue", Fraction(5, 6)), ("unused", Fraction(0)))
        return verify_pushforward(probability, targets, mapping, candidate)
    if name == "omitted-collision":
        candidate = (("red", Fraction(1, 2)), ("blue", Fraction(1, 6)), ("unused", Fraction(1, 3)))
        return verify_pushforward(probability, targets, mapping, candidate)
    if name == "wrong-expectation":
        pushed = pushforward(probability, targets, mapping)
        mutated = sum((value for _, value in observable), Fraction(0))
        return mutated == target_expectation(pushed, targets, observable)
    if name == "wrong-pullback":
        values = dict(observable)
        mutated = sum(
            (mass * values[target] for (_, mass), target in zip(probability, targets)),
            Fraction(0),
        )
        return mutated == source_pullback_expectation(probability, targets, mapping, observable)
    if name == "diagonal-only-product":
        pushed = pushforward(probability, targets, mapping)
        masses = dict(pushed)
        values = kernel_map(targets, kernel)
        mutated = sum((masses[target] * values[(target, target)] for target in targets), Fraction(0))
        return mutated == target_kernel_expectation(pushed, targets, kernel)
    if name == "additive-product-probability":
        probabilities = dict(probability)
        images = deterministic_map(probability, targets, mapping)
        values = kernel_map(targets, kernel)
        mutated = sum(
            (
                (probabilities[left] + probabilities[right])
                * values[(images[left], images[right])]
                for left in probabilities
                for right in probabilities
            ),
            Fraction(0),
        )
        return mutated == source_kernel_expectation(probability, targets, mapping, kernel)
    if name == "carrier-permutation-bug":
        small_probability = (("a", Fraction(1, 4)), ("b", Fraction(3, 4)))
        small_targets = ("left", "right")
        permuted_map = (("b", "left"), ("a", "right"))
        broken = tuple(
            (target, mass)
            for (_, mass), (_, target) in zip(small_probability, permuted_map)
        )
        return equal_by_label(
            broken,
            pushforward(small_probability, small_targets, permuted_map),
        )
    if name == "asymmetric-kernel-certified":
        return kernel_properties(targets, kernel)["symmetric"]
    if name == "unbounded-kernel-certified":
        return kernel_properties(targets, kernel)["positive_unit_bounded"]
    if name == "nonself-kernel-certified":
        return kernel_properties(targets, kernel)["self_one"]
    if name == "physical-selection-inference":
        return not expect_raises(
            TypeError,
            lambda: pushforward(
                probability,
                targets,
                mapping,
                physical_record_production="selected",  # type: ignore[call-arg]
            ),
        )
    raise KeyError(f"unknown hostile fixture: {name}")


HOSTILE_FIXTURES = (
    "empty-law",
    "unnormalized-law",
    "negative-law",
    "float-law",
    "integer-law",
    "bool-law",
    "fraction-subclass-law",
    "duplicate-source",
    "empty-target-carrier",
    "duplicate-target-carrier",
    "incomplete-map",
    "map-extra-source",
    "map-target-outside",
    "nonexact-map-source",
    "nonexact-map-target",
    "duplicate-map-source",
    "observable-missing-target",
    "observable-extra-target",
    "observable-inexact",
    "kernel-missing-pair",
    "kernel-extra-pair",
    "kernel-duplicate-pair",
    "kernel-inexact",
    "wrong-pushforward",
    "omitted-collision",
    "wrong-expectation",
    "wrong-pullback",
    "diagonal-only-product",
    "additive-product-probability",
    "carrier-permutation-bug",
    "asymmetric-kernel-certified",
    "unbounded-kernel-certified",
    "nonself-kernel-certified",
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
    print("THEOREM_SCOPE=EXACT_FINITE_DETERMINISTIC_PUSHFORWARD_OBSERVABLE_AND_PRODUCT_KERNEL_TRANSPORT")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
