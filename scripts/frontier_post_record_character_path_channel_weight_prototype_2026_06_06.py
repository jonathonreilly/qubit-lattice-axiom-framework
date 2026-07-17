#!/usr/bin/env python3
"""Exact finite normalization and supplied-edge path-product theorem."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from pathlib import Path
import re
import sys
from typing import Callable, TypeAlias


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/POST_RECORD_CHARACTER_PATH_CHANNEL_WEIGHT_PROTOTYPE_2026-06-06.md"

Label: TypeAlias = str
WeightPacket: TypeAlias = tuple[tuple[Label, Fraction], ...]
Rows: TypeAlias = tuple[tuple[Label, WeightPacket], ...]

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Edge:
    edge_id: str
    source: str
    target: str
    weight: Fraction


@dataclass(frozen=True)
class PathWord:
    start: str
    edge_ids: tuple[str, ...]


@dataclass(frozen=True)
class PathValue:
    end: str
    weight: Fraction


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
        raise TypeError(f"{context} must be an exact Fraction")
    return value


def validate_packet(packet: WeightPacket) -> Fraction:
    if type(packet) is not tuple or not packet:
        raise ValueError("weight carrier must be a nonempty finite tuple")
    labels: set[str] = set()
    total = Fraction(0)
    for item in packet:
        if type(item) is not tuple or len(item) != 2:
            raise TypeError("each weight entry must be a (label, Fraction) tuple")
        label, raw_weight = item
        if type(label) is not str or not label:
            raise TypeError("weight labels must be nonempty strings")
        if label in labels:
            raise ValueError(f"duplicate carrier label: {label}")
        labels.add(label)
        weight = exact_fraction(raw_weight, f"weight for {label}")
        if weight < 0:
            raise ValueError(f"negative weight for {label}")
        total += weight
    if total <= 0:
        raise ValueError("weight total must be positive")
    return total


def normalize_exact(packet: WeightPacket) -> WeightPacket:
    total = validate_packet(packet)
    return tuple((label, weight / total) for label, weight in packet)


def verify_normalized(source: WeightPacket, candidate: WeightPacket) -> bool:
    try:
        expected = normalize_exact(source)
        validate_packet(candidate)
    except (TypeError, ValueError):
        return False
    return (
        candidate == expected
        and all(weight >= 0 for _, weight in candidate)
        and sum((weight for _, weight in candidate), Fraction(0)) == 1
    )


def normalize_rows(rows: Rows) -> Rows:
    if type(rows) is not tuple or not rows:
        raise ValueError("row carrier must be a nonempty finite tuple")
    row_labels: set[str] = set()
    expected_columns: tuple[str, ...] | None = None
    normalized: list[tuple[str, WeightPacket]] = []
    for item in rows:
        if type(item) is not tuple or len(item) != 2:
            raise TypeError("each row entry must be a (row, packet) tuple")
        row_label, packet = item
        if type(row_label) is not str or not row_label:
            raise TypeError("row labels must be nonempty strings")
        if row_label in row_labels:
            raise ValueError(f"duplicate row label: {row_label}")
        row_labels.add(row_label)
        columns = tuple(label for label, _ in packet)
        if expected_columns is None:
            expected_columns = columns
        elif columns != expected_columns:
            raise ValueError("every row must use the same ordered column carrier")
        normalized.append((row_label, normalize_exact(packet)))
    return tuple(normalized)


def compile_edges(definitions: tuple[Edge, ...]) -> dict[str, Edge]:
    if type(definitions) is not tuple:
        raise TypeError("edge definitions must be a finite tuple")
    compiled: dict[str, Edge] = {}
    for edge in definitions:
        if type(edge) is not Edge:
            raise TypeError("every edge definition must be an Edge")
        if any(
            type(value) is not str or not value
            for value in (edge.edge_id, edge.source, edge.target)
        ):
            raise TypeError("edge identifiers and endpoints must be nonempty strings")
        if edge.edge_id in compiled:
            raise ValueError(f"duplicate edge definition: {edge.edge_id}")
        exact_fraction(edge.weight, f"edge weight for {edge.edge_id}")
        if edge.weight < 0:
            raise ValueError(f"negative edge weight for {edge.edge_id}")
        compiled[edge.edge_id] = edge
    return compiled


def evaluate_path(path: PathWord, edges: dict[str, Edge]) -> PathValue:
    if type(path) is not PathWord or type(path.start) is not str or not path.start:
        raise TypeError("path must have a nonempty supplied start vertex")
    if type(path.edge_ids) is not tuple or any(
        type(edge_id) is not str or not edge_id for edge_id in path.edge_ids
    ):
        raise TypeError("path edge identifiers must be a finite tuple of strings")
    current = path.start
    product = Fraction(1)
    for edge_id in path.edge_ids:
        edge = edges.get(edge_id)
        if edge is None:
            raise KeyError(f"missing edge definition: {edge_id}")
        if edge.source != current:
            raise ValueError(
                f"broken path incidence at {edge_id}: expected source {current}"
            )
        product *= edge.weight
        current = edge.target
    return PathValue(current, product)


def compose_paths(
    left: PathWord, right: PathWord, edges: dict[str, Edge]
) -> PathWord:
    left_value = evaluate_path(left, edges)
    evaluate_path(right, edges)
    if left_value.end != right.start:
        raise ValueError("paths are not composable")
    return PathWord(left.start, left.edge_ids + right.edge_ids)


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b) if a and b else 0


def normalize_independently(packet: WeightPacket) -> WeightPacket:
    """Independent construction through common-denominator integer counts."""
    if type(packet) is not tuple or not packet:
        raise ValueError("independent carrier must be a nonempty tuple")
    labels: set[str] = set()
    denominator = 1
    for label, raw_weight in packet:
        if type(label) is not str or not label or label in labels:
            raise ValueError("independent labels must be nonempty and unique")
        labels.add(label)
        weight = exact_fraction(raw_weight, f"independent weight for {label}")
        if weight < 0:
            raise ValueError("independent weights must be nonnegative")
        denominator = lcm(denominator, weight.denominator)
    counts = tuple(
        weight.numerator * (denominator // weight.denominator)
        for _, weight in packet
    )
    total_count = sum(counts)
    if total_count <= 0:
        raise ValueError("independent total must be positive")
    return tuple(
        (packet[index][0], Fraction(count, total_count))
        for index, count in enumerate(counts)
    )


def path_product_independently(path: PathWord, edges: dict[str, Edge]) -> PathValue:
    if type(path) is not PathWord or type(path.start) is not str or not path.start:
        raise TypeError("independent path must have a supplied string start vertex")
    if type(path.edge_ids) is not tuple or any(
        type(edge_id) is not str or not edge_id for edge_id in path.edge_ids
    ):
        raise TypeError("independent edge identifiers must be a finite string tuple")
    current = path.start
    numerator = 1
    denominator = 1
    for edge_id in path.edge_ids:
        if edge_id not in edges:
            raise KeyError(f"independent missing edge: {edge_id}")
        edge = edges[edge_id]
        if edge.source != current:
            raise ValueError("independent incidence mismatch")
        numerator *= edge.weight.numerator
        denominator *= edge.weight.denominator
        current = edge.target
    return PathValue(current, Fraction(numerator, denominator))


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
        "p_i = w_i/W",
        "sum_{c in C} P_(r,c) = 1",
        "A(P Q) = A(P) A(Q)",
        "Repeated traversal is counted once per occurrence",
        "normalization cannot choose its own inputs",
        "The theorem has no audit-census, ledger, queue, export, or row-count premise.",
    )
    for phrase in required:
        report(f"source contains theorem anchor: {phrase}", phrase in flat)

    forbidden_patterns = (
        r"\bRecord (?:derives|supplies|selects|fixes)\b",
        r"\bthe normalized packet (?:is|selects) the physical\b",
        r"\bBorn (?:law|rule) follows\b",
        r"\ball \d+ character_path_channel_weight rows\b",
        r"post_record_character_path_channel_weight_slice_2026_06_07\.json",
        r"frontier_post_record_measure_weight_normalization_subdivision_2026_06_06\.py",
        r"docs/audit/data/",
        r"\baudit_status\s*:",
        r"\beffective_status\s*:",
    )
    for pattern in forbidden_patterns:
        report(
            f"source excludes volatile or physical overclaim: {pattern}",
            re.search(pattern, flat, flags=re.IGNORECASE) is None,
        )


def theorem_examples() -> None:
    section("Exact finite normalization theorem")
    path_packet = (("straight", Fraction(4)), ("bend", Fraction(1)))
    normalized = normalize_exact(path_packet)
    report(
        "4:1 packet normalizes exactly",
        normalized == (("straight", Fraction(4, 5)), ("bend", Fraction(1, 5))),
        str(normalized),
    )
    report("normalized entries are nonnegative", all(w >= 0 for _, w in normalized))
    report(
        "normalized packet sums exactly to one",
        sum((w for _, w in normalized), Fraction(0)) == 1,
    )
    with_zero = normalize_exact((("zero", Fraction(0)), ("positive", Fraction(5, 7))))
    report(
        "zero entries are allowed with positive total",
        with_zero == (("zero", Fraction(0)), ("positive", Fraction(1))),
    )
    character = normalize_exact(
        (("trivial", Fraction(6)), ("fundamental", Fraction(3)), ("adjoint", Fraction(1)))
    )
    report(
        "6:3:1 packet normalizes exactly",
        character
        == (
            ("trivial", Fraction(3, 5)),
            ("fundamental", Fraction(3, 10)),
            ("adjoint", Fraction(1, 10)),
        ),
        str(character),
    )

    section("Exact row-stochastic corollary")
    rows = (
        ("A", (("A", Fraction(3)), ("B", Fraction(1)))),
        ("B", (("A", Fraction(1)), ("B", Fraction(1)))),
        ("C", (("A", Fraction(0)), ("B", Fraction(5, 2)))),
    )
    stochastic = normalize_rows(rows)
    report("three supplied rows normalize", len(stochastic) == 3, str(stochastic))
    report(
        "every row sums exactly to one",
        all(sum((w for _, w in row), Fraction(0)) == 1 for _, row in stochastic),
    )
    report(
        "A row is exactly (3/4,1/4)",
        stochastic[0][1] == (("A", Fraction(3, 4)), ("B", Fraction(1, 4))),
    )
    report(
        "B row is exactly (1/2,1/2)",
        stochastic[1][1] == (("A", Fraction(1, 2)), ("B", Fraction(1, 2))),
    )

    section("Supplied-edge path-product theorem")
    edges = compile_edges(
        (
            Edge("s_m", "s", "m", Fraction(2)),
            Edge("m_t", "m", "t", Fraction(3)),
            Edge("s_t", "s", "t", Fraction(1)),
            Edge("loop", "m", "m", Fraction(2, 3)),
        )
    )
    first = PathWord("s", ("s_m",))
    second = PathWord("m", ("m_t",))
    two_step = compose_paths(first, second, edges)
    direct = PathWord("s", ("s_t",))
    report("first path has exact weight 2", evaluate_path(first, edges) == PathValue("m", Fraction(2)))
    report("second path has exact weight 3", evaluate_path(second, edges) == PathValue("t", Fraction(3)))
    report("composed path has exact weight 6", evaluate_path(two_step, edges) == PathValue("t", Fraction(6)))
    report(
        "path concatenation is multiplicative",
        evaluate_path(two_step, edges).weight
        == evaluate_path(first, edges).weight * evaluate_path(second, edges).weight,
    )
    empty = PathWord("m", ())
    report("empty path is the exact identity", evaluate_path(empty, edges) == PathValue("m", Fraction(1)))
    loop_twice = PathWord("m", ("loop", "loop"))
    report("repeated loop traversal counts twice", evaluate_path(loop_twice, edges) == PathValue("m", Fraction(4, 9)))
    raw_paths = (
        ("two_step", evaluate_path(two_step, edges).weight),
        ("direct", evaluate_path(direct, edges).weight),
    )
    report(
        "6:1 path carrier normalizes exactly",
        normalize_exact(raw_paths)
        == (("two_step", Fraction(6, 7)), ("direct", Fraction(1, 7))),
    )


def independent_checks() -> None:
    section("Independent exact reconstruction")
    packets = (
        (("a", Fraction(4)), ("b", Fraction(1))),
        (("a", Fraction(1, 2)), ("b", Fraction(1, 3)), ("c", Fraction(1, 6))),
        (("a", Fraction(0)), ("b", Fraction(7, 11))),
        (("a", Fraction(6)), ("b", Fraction(3)), ("c", Fraction(1))),
    )
    for index, packet in enumerate(packets, start=1):
        rebuilt = normalize_independently(packet)
        report(
            f"packet {index}: common-denominator reconstruction agrees",
            rebuilt == normalize_exact(packet),
            str(rebuilt),
        )
        report(
            f"packet {index}: independent sum is exactly one",
            sum((weight for _, weight in rebuilt), Fraction(0)) == 1,
        )

    rows = (
        ("r0", (("c0", Fraction(2, 5)), ("c1", Fraction(3, 5)))),
        ("r1", (("c0", Fraction(7, 9)), ("c1", Fraction(2, 9)))),
    )
    primary_rows = normalize_rows(rows)
    independent_rows = tuple(
        (row_label, normalize_independently(packet)) for row_label, packet in rows
    )
    report("multiple rows agree by independent construction", independent_rows == primary_rows)

    edges = compile_edges(
        (
            Edge("a", "u", "v", Fraction(2, 3)),
            Edge("b", "v", "w", Fraction(5, 7)),
            Edge("c", "w", "x", Fraction(11, 13)),
            Edge("loop", "x", "x", Fraction(3, 4)),
        )
    )
    paths = (
        PathWord("u", ()),
        PathWord("u", ("a",)),
        PathWord("u", ("a", "b", "c")),
        PathWord("x", ("loop", "loop", "loop")),
    )
    for index, path in enumerate(paths, start=1):
        independent = path_product_independently(path, edges)
        report(
            f"path {index}: numerator/denominator product agrees",
            independent == evaluate_path(path, edges),
            str(independent),
        )
    left = PathWord("u", ("a", "b"))
    right = PathWord("w", ("c",))
    composed = compose_paths(left, right, edges)
    report(
        "independent composition example is multiplicative",
        path_product_independently(composed, edges).weight
        == path_product_independently(left, edges).weight
        * path_product_independently(right, edges).weight,
    )

    section("Independent malformed-input reconstruction")
    report(
        "independent route rejects an empty carrier",
        expect_raises(ValueError, lambda: normalize_independently(())),
    )
    report(
        "independent route rejects zero total",
        expect_raises(
            ValueError,
            lambda: normalize_independently(
                (("a", Fraction(0)), ("b", Fraction(0)))
            ),
        ),
    )
    report(
        "independent route rejects a negative weight",
        expect_raises(
            ValueError,
            lambda: normalize_independently(
                (("a", Fraction(2)), ("b", Fraction(-1)))
            ),
        ),
    )
    inexact = (("a", Fraction(1)), ("b", 0.5))
    report(
        "independent route rejects a float weight",
        expect_raises(
            TypeError,
            lambda: normalize_independently(inexact),  # type: ignore[arg-type]
        ),
    )
    report(
        "independent route rejects duplicate labels",
        expect_raises(
            ValueError,
            lambda: normalize_independently(
                (("a", Fraction(1)), ("a", Fraction(2)))
            ),
        ),
    )
    report(
        "independent route rejects a missing edge",
        expect_raises(
            KeyError,
            lambda: path_product_independently(
                PathWord("u", ("missing",)), edges
            ),
        ),
    )
    report(
        "independent route rejects broken incidence",
        expect_raises(
            ValueError,
            lambda: path_product_independently(PathWord("v", ("a",)), edges),
        ),
    )


def scope_authorizes(conclusion: str) -> bool:
    capabilities = frozenset(
        {
            "exact_finite_normalization",
            "exact_row_stochasticity",
            "supplied_edge_path_product",
            "path_concatenation_multiplicativity",
        }
    )
    return conclusion in capabilities


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
    if name == "duplicate-carrier-label":
        return not expect_raises(
            ValueError,
            lambda: normalize_exact((("a", Fraction(1)), ("a", Fraction(2)))),
        )
    if name == "wrong-total-normalization":
        source = (("a", Fraction(4)), ("b", Fraction(1)))
        mutated = (("a", Fraction(2, 3)), ("b", Fraction(1, 6)))
        return verify_normalized(source, mutated)
    if name == "mismatched-row-carrier":
        rows = (
            ("r0", (("a", Fraction(1)), ("b", Fraction(1)))),
            ("r1", (("a", Fraction(1)), ("c", Fraction(1)))),
        )
        return not expect_raises(ValueError, lambda: normalize_rows(rows))
    if name == "duplicate-edge-definition":
        definitions = (
            Edge("e", "s", "t", Fraction(1)),
            Edge("e", "s", "u", Fraction(2)),
        )
        return not expect_raises(ValueError, lambda: compile_edges(definitions))
    if name == "negative-edge-weight":
        definitions = (Edge("e", "s", "t", Fraction(-1)),)
        return not expect_raises(ValueError, lambda: compile_edges(definitions))
    if name == "float-edge-weight":
        definitions = (Edge("e", "s", "t", 0.5),)
        return not expect_raises(
            TypeError,
            lambda: compile_edges(definitions),  # type: ignore[arg-type]
        )
    if name == "missing-path-edge":
        edges = compile_edges((Edge("e", "s", "t", Fraction(1)),))
        return not expect_raises(KeyError, lambda: evaluate_path(PathWord("s", ("missing",)), edges))
    if name == "broken-incidence":
        edges = compile_edges((Edge("e", "s", "t", Fraction(1)),))
        return not expect_raises(ValueError, lambda: evaluate_path(PathWord("u", ("e",)), edges))
    if name == "noncomposable-paths":
        edges = compile_edges(
            (
                Edge("e", "s", "t", Fraction(2)),
                Edge("f", "u", "v", Fraction(3)),
            )
        )
        return not expect_raises(
            ValueError,
            lambda: compose_paths(PathWord("s", ("e",)), PathWord("u", ("f",)), edges),
        )
    if name == "sum-instead-of-product":
        mutated_path_weight = Fraction(2) + Fraction(3)
        exact_path_weight = Fraction(2) * Fraction(3)
        return mutated_path_weight == exact_path_weight
    if name == "drop-repeated-traversal":
        edges = compile_edges((Edge("loop", "m", "m", Fraction(2, 3)),))
        actual = evaluate_path(PathWord("m", ("loop", "loop")), edges).weight
        mutated = edges["loop"].weight
        return mutated == actual
    if name == "physical-selection-inference":
        return scope_authorizes("physical_measure_selected")
    raise KeyError(f"unknown hostile fixture: {name}")


HOSTILE_FIXTURES = (
    "empty-carrier",
    "zero-total",
    "negative-weight",
    "float-weight",
    "integer-weight",
    "duplicate-carrier-label",
    "wrong-total-normalization",
    "mismatched-row-carrier",
    "duplicate-edge-definition",
    "negative-edge-weight",
    "float-edge-weight",
    "missing-path-edge",
    "broken-incidence",
    "noncomposable-paths",
    "sum-instead-of-product",
    "drop-repeated-traversal",
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
            parser.error("--independent cannot be combined with an explicit non-normal --mode")
        args.mode = "independent"
    if args.hostile:
        if args.mode != "normal":
            parser.error("--hostile cannot be combined with an explicit non-normal --mode")
        args.mode = "hostile"
    if args.fixture != "all" and args.mode != "intentional-failure":
        parser.error("--fixture requires --mode intentional-failure")
    return args


def main() -> int:
    args = parse_args()
    source_scope_checks()
    if args.mode == "normal":
        theorem_examples()
    elif args.mode == "independent":
        independent_checks()
    elif args.mode == "hostile":
        hostile_checks()
    else:
        intentional_failure_checks(args.fixture)
    print(f"\nSUMMARY: MODE={args.mode} PASS={PASS} FAIL={FAIL}")
    print("THEOREM_SCOPE=EXACT_FINITE_RATIONAL_NORMALIZATION_ROW_STOCHASTICITY_AND_SUPPLIED_EDGE_PATH_PRODUCTS")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
