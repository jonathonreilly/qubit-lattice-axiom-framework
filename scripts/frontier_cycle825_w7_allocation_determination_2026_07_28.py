#!/usr/bin/env python3
"""Cycle 825: does the landed W7 kernel determine the allocation?

The Cycle-821 checker and all six W7 lineage modules are SHA-pinned,
text/AST-only inputs.  This runner independently reconstructs the eleven
allocation readouts with exact Fraction arithmetic and exhausts all 42,504
lawful per-origin allocations.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024

# Literal, existing, worktree-relative paths.  Every entry is text/AST only.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle821_observability_independent_check_2026_07_28.py",
    "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
    "scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
    "scripts/frontier_cycle774_interference_sector_2026_07_28.py",
    "scripts/frontier_cycle778_norefit_attachment_2026_07_28.py",
    "scripts/frontier_cycle812_mixed_input_response_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "63336e900ea1f1df838500087d85b9bd2f960e695dbd16555c36883d819c68db",
    AUDIT_INPUT_PATHS[1]:
        "ab9b852236f73ec4aecad9287e07a4029309159d956a1cb3043f9238342d6807",
    AUDIT_INPUT_PATHS[2]:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
    AUDIT_INPUT_PATHS[3]:
        "6e668efc97a276ce9b0b442cbf7f9eda32c2aa6c722b6f562c5ca4046a4b7ba1",
    AUDIT_INPUT_PATHS[4]:
        "2f5214633abf7bcc715c88a646ded9bd25dc3fdfbfe09785ddd12a551dc18c25",
    AUDIT_INPUT_PATHS[5]:
        "033e6442c01eef32efe20e55b025459aa606b92d1a91a4e48e9f795bc3946181",
    AUDIT_INPUT_PATHS[6]:
        "fe35718b8f5e84cfafed74026a5634e722da757782f04d536a756d7273d3ee9b",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "411370e1140bc39c5365c0f7ee911ac29cee79ca",
    AUDIT_INPUT_PATHS[1]: "cee674584704dd7d351cb2ffa947c74bee47d06e",
    AUDIT_INPUT_PATHS[2]: "0070722d7a12d47658346b6c812edd05424ae592",
    AUDIT_INPUT_PATHS[3]: "52abfe3dd54b3969f51ca6816ec4830b42405106",
    AUDIT_INPUT_PATHS[4]: "6bde2222ddfdaf48e3806c0ac0a9c9d6431d945f",
    AUDIT_INPUT_PATHS[5]: "8366a5240d992376d0396a6fdc2c0b33247e8aba",
    AUDIT_INPUT_PATHS[6]: "39b5f24595f2271704bf68197103b62824a14cbf",
}
BLOCKLISTED_MODULES = tuple(
    path.removeprefix("scripts/").removesuffix(".py")
    for path in AUDIT_INPUT_PATHS
)

GROUP_TOTAL = 19
GROUP_BINS = 6
READOUT_NAMES = (
    "w7.response_mixture_sum",
    "w7.response_expectation.matter[0]",
    "w7.response_expectation.matter[1]",
    "w7.response_expectation.matter[2]",
    "w7.response_expectation.mediator[0]",
    "w7.response_expectation.mediator[1]",
    "w7.response_expectation.mediator[2]",
    "w7.response_expectation.auxiliary[0]",
    "w7.response_expectation.auxiliary[1]",
    "w7.response_expectation.auxiliary[2]",
    "w7.response_flux_balance",
)

import ast
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
import importlib.abc
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()
CHECKS: dict[str, bool] = {}
STDOUT_BYTES = 0

Vector = tuple[Fraction, Fraction, Fraction]
ResponseRow = tuple[Vector, Vector, Vector]
ReadoutVector = tuple[object, ...]


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    """Make every source primary unavailable as an import."""

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            raise ImportError(f"BLOCKLIST text/AST-only primary: {fullname}")
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        return fraction_text(value)
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Counter):
        return dict(value)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def compact(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=jsonable,
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def emit(*parts: object) -> None:
    global STDOUT_BYTES
    line = " ".join(str(part) for part in parts)
    encoded = (line + "\n").encode("utf-8")
    STDOUT_BYTES += len(encoded)
    if STDOUT_BYTES > STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit exceeded", STDOUT_BYTES))
    print(line)


def check(label: str, condition: bool, detail: object) -> bool:
    CHECKS[label] = bool(condition)
    emit(
        "CERTIFICATE",
        label,
        "PASS" if condition else "FAIL",
        compact(detail),
    )
    return bool(condition)


def git_blob_sha1(data: bytes) -> str:
    prefix = f"blob {len(data)}\0".encode("ascii")
    return sha1(prefix + data).hexdigest()


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = tuple(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )
    if len(matches) != 1:
        raise AssertionError(("function multiplicity", name, len(matches)))
    return matches[0]


def literal_assignment(tree: ast.Module, name: str) -> object:
    matches = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            matches.append(node.value)
    if len(matches) != 1 or matches[0] is None:
        raise AssertionError(("literal assignment multiplicity", name))
    return ast.literal_eval(matches[0])


def function_citation(
    path: str,
    tree: ast.Module,
    name: str,
) -> tuple[str, str, int, str]:
    node = named_function(tree, name)
    return (
        path,
        name,
        node.lineno,
        sha256(
            ast.dump(
                node,
                annotate_fields=True,
                include_attributes=False,
            ).encode("utf-8")
        ).hexdigest(),
    )


def read_sources() -> tuple[dict[str, bytes], dict[str, ast.Module]]:
    source_bytes = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(data, filename=path)
        for path, data in source_bytes.items()
    }
    return source_bytes, trees


def checker_readout_contract(
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    checker_path = AUDIT_INPUT_PATHS[0]
    checker = trees[checker_path]
    citations = tuple(
        function_citation(checker_path, checker, name)
        for name in (
            "response_mixture_sum",
            "response_expectation",
            "w7_observables",
        )
    )
    observable_function = named_function(checker, "w7_observables")
    observable_source = ast.unparse(observable_function)
    string_literals = {
        node.value
        for node in ast.walk(observable_function)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    core_names_present = {
        "w7.response_mixture_sum",
        "w7.response_expectation",
        "w7.response_flux_balance",
    } <= string_literals
    component_labels_present = (
        "component_labels = ('matter', 'mediator', 'auxiliary')"
        in observable_source
    )
    scalar_name_template_present = (
        "w7.response_expectation." in observable_source
        and "[{axis}]" in observable_source
    )
    names_present = (
        core_names_present
        and component_labels_present
        and scalar_name_template_present
    )
    redundant_whole_present = "w7.response_expectation" in string_literals
    return {
        "checker_path": checker_path,
        "checker_sha256": EXPECTED_SHA256[checker_path],
        "citations": citations,
        "exact_selection_rule": (
            "Cycle-821 checker W7 list, excluding only its redundant whole "
            "response_expectation because all nine exact scalar components "
            "are retained"
        ),
        "readout_count": len(READOUT_NAMES),
        "readout_names": READOUT_NAMES,
        "all_selected_names_present": names_present,
        "redundant_whole_expectation_present": redundant_whole_present,
        "pass": (
            len(READOUT_NAMES) == 11
            and names_present
            and redundant_whole_present
            and len(citations) == 3
        ),
    }


def extract_response_surface(
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    cycle812_path = AUDIT_INPUT_PATHS[6]
    cycle812 = trees[cycle812_path]
    directions_raw = literal_assignment(cycle812, "DIRECTIONS")
    reverse_raw = literal_assignment(cycle812, "REVERSE")
    directions = tuple(
        tuple(int(value) for value in direction)
        for direction in directions_raw
    )
    reverse = tuple(int(value) for value in reverse_raw)
    rows = tuple(
        (
            tuple(Fraction(-2 * value) for value in direction),
            tuple(Fraction(value) for value in direction),
            tuple(Fraction(value) for value in direction),
        )
        for direction in directions
    )
    citations = tuple(
        function_citation(cycle812_path, cycle812, name)
        for name in ("response_rows", "w7_linearity_certificate")
    )
    response_source = ast.unparse(named_function(cycle812, "response_rows"))
    passed = (
        directions
        == (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        )
        and reverse == (1, 0, 3, 2, 5, 4)
        and all(
            directions[reverse[index]]
            == tuple(-value for value in direction)
            for index, direction in enumerate(directions)
        )
        and "for direction in DIRECTIONS" in response_source
        and "-2 * value" in response_source
    )
    return {
        "directions": directions,
        "reverse": reverse,
        "rows": rows,
        "citations": citations,
        "pass": passed,
    }


def response_mixture_sum(
    allocation: tuple[int, ...],
    rows: tuple[ResponseRow, ...],
) -> ResponseRow:
    return tuple(
        tuple(
            sum(
                (
                    Fraction(allocation[direction])
                    * rows[direction][component][axis]
                    for direction in range(GROUP_BINS)
                ),
                start=Fraction(),
            )
            for axis in range(3)
        )
        for component in range(3)
    )  # type: ignore[return-value]


def response_expectation(
    allocation: tuple[int, ...],
    rows: tuple[ResponseRow, ...],
) -> ResponseRow:
    total = sum(allocation)
    if total <= 0:
        raise ValueError("response expectation requires positive total")
    mixture = response_mixture_sum(allocation, rows)
    return tuple(
        tuple(value / total for value in component)
        for component in mixture
    )  # type: ignore[return-value]


def readout_vector(
    allocation: tuple[int, ...],
    rows: tuple[ResponseRow, ...],
) -> ReadoutVector:
    mixture = response_mixture_sum(allocation, rows)
    expectation = response_expectation(allocation, rows)
    scalar_components = tuple(
        expectation[component][axis]
        for component in range(3)
        for axis in range(3)
    )
    flux_balance = tuple(
        sum(
            (
                expectation[component][axis]
                for component in range(3)
            ),
            start=Fraction(),
        )
        for axis in range(3)
    )
    return (mixture, *scalar_components, flux_balance)


def signed_moment(allocation: tuple[int, ...]) -> tuple[int, int, int]:
    return (
        allocation[0] - allocation[1],
        allocation[2] - allocation[3],
        allocation[4] - allocation[5],
    )


def contains_float(value: object) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, dict):
        return any(
            contains_float(key) or contains_float(item)
            for key, item in value.items()
        )
    if isinstance(value, (tuple, list, set, frozenset)):
        return any(contains_float(item) for item in value)
    return False


def stars_and_bars_allocations(
    total: int,
    bins: int,
) -> tuple[tuple[int, ...], ...]:
    """Independent, nonrecursive stars-and-bars construction."""
    output = []
    string_last = total + bins - 2
    for bars in combinations(range(total + bins - 1), bins - 1):
        previous = -1
        row = []
        for bar in bars:
            row.append(bar - previous - 1)
            previous = bar
        row.append(string_last - previous)
        output.append(tuple(row))
    return tuple(output)


def lawful_allocation(allocation: tuple[int, ...]) -> bool:
    return (
        len(allocation) == GROUP_BINS
        and all(type(value) is int and value >= 0 for value in allocation)
        and sum(allocation) == GROUP_TOTAL
    )


def rotation_image(
    allocation: tuple[int, ...],
    shift: int,
) -> tuple[int, ...]:
    shift %= len(allocation)
    if not shift:
        return allocation
    return allocation[-shift:] + allocation[:-shift]


def orbit_partition(
    allocations: tuple[tuple[int, ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    grouped: dict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)
    for allocation in allocations:
        representative = min(
            rotation_image(allocation, shift)
            for shift in range(GROUP_BINS)
        )
        grouped[representative].add(allocation)
    return tuple(
        tuple(sorted(grouped[representative]))
        for representative in sorted(grouped)
    )


def collision_certificate(
    allocations: tuple[tuple[int, ...], ...],
    rows: tuple[ResponseRow, ...],
) -> dict[str, object]:
    classes: dict[ReadoutVector, list[tuple[int, ...]]] = defaultdict(list)
    readout_moments: dict[ReadoutVector, tuple[int, int, int]] = {}
    exact = True
    for allocation in allocations:
        readout = readout_vector(allocation, rows)
        moment = signed_moment(allocation)
        exact = exact and not contains_float(readout)
        if readout in readout_moments and readout_moments[readout] != moment:
            raise AssertionError("one exact readout has two signed moments")
        readout_moments[readout] = moment
        classes[readout].append(allocation)

    ordered = tuple(
        (
            readout_moments[readout],
            tuple(classes[readout]),
        )
        for readout in sorted(
            classes,
            key=lambda value: readout_moments[value],
        )
    )
    distribution = Counter(len(members) for members in classes.values())
    formula_ok = True
    for moment, members in ordered:
        l1 = sum(abs(value) for value in moment)
        formula_ok = formula_ok and (
            l1 <= GROUP_TOTAL
            and l1 % 2 == GROUP_TOTAL % 2
            and len(members)
            == math.comb((GROUP_TOTAL - l1) // 2 + 2, 2)
        )
    largest_moment, largest_members = max(
        ordered,
        key=lambda item: (len(item[1]), tuple(-x for x in item[0])),
    )
    witness = (largest_members[0], largest_members[1])
    return {
        "allocation_count": len(allocations),
        "distinct_readout_count": len(classes),
        "injective": len(classes) == len(allocations),
        "singleton_class_count": distribution[1],
        "nonsingleton_class_count": sum(
            count for size, count in distribution.items() if size > 1
        ),
        "members_in_nonsingleton_classes": sum(
            size * count
            for size, count in distribution.items()
            if size > 1
        ),
        "class_size_distribution": dict(sorted(distribution.items())),
        "exact_class_rule": (
            "R(a)=R(b) iff "
            "(a0-a1,a2-a3,a4-a5)=(b0-b1,b2-b3,b4-b5); "
            "for signed moment s with m=|s|_1 odd and m<=19, "
            "|class(s)|=C((19-m)/2+2,2)"
        ),
        "formula_verified_for_every_class": formula_ok,
        "all_values_exact": exact,
        "collision_witness": {
            "allocation_a": witness[0],
            "allocation_b": witness[1],
            "signed_moment": largest_moment,
            "readout_a": readout_vector(witness[0], rows),
            "readout_b": readout_vector(witness[1], rows),
        },
        "ordered_collision_classes_sha256": digest(ordered),
    }


def main() -> int:
    source_bytes, trees = read_sources()
    checker_contract = checker_readout_contract(trees)
    response_surface = extract_response_surface(trees)
    rows = response_surface["rows"]
    if not isinstance(rows, tuple):
        raise AssertionError("response rows are malformed")

    allocations = stars_and_bars_allocations(GROUP_TOTAL, GROUP_BINS)
    orbits = orbit_partition(allocations)
    allocation_control = {
        "allocation_count": len(allocations),
        "all_lawful": all(map(lawful_allocation, allocations)),
        "allocation_sha256": digest(allocations),
        "orbit_count": len(orbits),
        "orbit_size_distribution": dict(Counter(map(len, orbits))),
        "partition_member_count": sum(map(len, orbits)),
    }
    collisions = collision_certificate(allocations, rows)

    emit("CYCLE 825 W7_ALLOCATION_DETERMINATION")
    emit("READOUT_NAMES", compact(READOUT_NAMES))
    check(
        "A_READOUT_MAP",
        (
            checker_contract["pass"]
            and response_surface["pass"]
            and len(READOUT_NAMES) == 11
            and allocation_control["allocation_count"] == 42_504
            and allocation_control["all_lawful"]
            and allocation_control["orbit_count"] == 7_084
            and allocation_control["orbit_size_distribution"] == {6: 7_084}
            and allocation_control["partition_member_count"] == 42_504
        ),
        {
            "checker_contract": checker_contract,
            "response_surface": response_surface,
            "allocation_control": allocation_control,
        },
    )
    check(
        "B_INJECTIVITY",
        (
            not collisions["injective"]
            and collisions["distinct_readout_count"] == 5_340
            and collisions["class_size_distribution"]
            == {
                1: 1_446,
                3: 1_158,
                6: 902,
                10: 678,
                15: 486,
                21: 326,
                28: 198,
                36: 102,
                45: 38,
                55: 6,
            }
            and collisions["nonsingleton_class_count"] == 3_894
            and collisions["members_in_nonsingleton_classes"] == 41_058
            and collisions["formula_verified_for_every_class"]
            and collisions["all_values_exact"]
        ),
        collisions,
    )

    elapsed = monotonic() - START
    passed = all(CHECKS.values())
    emit(
        "INJECTIVITY",
        (
            f"NONINJECTIVE distinct={collisions['distinct_readout_count']} "
            f"allocations={collisions['allocation_count']} "
            f"collision_classes={collisions['nonsingleton_class_count']}"
        ),
    )
    emit("RUNTIME_SECONDS", f"{elapsed:.6f}")
    emit("STDOUT_BYTES", STDOUT_BYTES)
    emit("CHECK_SUMMARY", compact({"pass": passed, "checks": CHECKS}))
    emit("PASS" if passed else "FAIL")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
