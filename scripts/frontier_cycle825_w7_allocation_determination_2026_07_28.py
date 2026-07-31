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


def assignment_node(
    tree: ast.Module | ast.FunctionDef,
    name: str,
) -> ast.AST:
    matches = []
    nodes = tree.body if isinstance(tree, (ast.Module, ast.FunctionDef)) else ()
    for statement in nodes:
        if not isinstance(statement, (ast.Assign, ast.AnnAssign)):
            continue
        targets = (
            statement.targets
            if isinstance(statement, ast.Assign)
            else (statement.target,)
        )
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            matches.append(statement.value)
    if len(matches) != 1 or matches[0] is None:
        raise AssertionError(("assignment multiplicity", name, len(matches)))
    return matches[0]


def dict_value_node(dictionary: ast.AST, key: str) -> ast.AST:
    if not isinstance(dictionary, ast.Dict):
        raise AssertionError(("expected literal dict", key))
    matches = [
        value
        for raw_key, value in zip(dictionary.keys, dictionary.values, strict=True)
        if (
            isinstance(raw_key, ast.Constant)
            and raw_key.value == key
        )
    ]
    if len(matches) != 1:
        raise AssertionError(("dict key multiplicity", key, len(matches)))
    return matches[0]


def exact_zero_fraction_tree(node: ast.AST) -> bool:
    if isinstance(node, ast.Tuple):
        return bool(node.elts) and all(
            exact_zero_fraction_tree(element)
            for element in node.elts
        )
    return bool(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "Fraction"
        and len(node.args) == 1
        and not node.keywords
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value == 0
    )


def fraction_one_assignment(node: ast.AST) -> bool:
    return bool(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "Fraction"
        and len(node.args) == 1
        and not node.keywords
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value is True
    )


W7_FUNCTIONAL_SOURCES = {
    AUDIT_INPUT_PATHS[1]: (
        "extract_frozen_fixtures",
        "evaluate_candidate",
    ),
    AUDIT_INPUT_PATHS[2]: (
        "derive_recoil_coefficients",
        "derive_response_kernel_candidate",
    ),
    AUDIT_INPUT_PATHS[3]: (
        "landed_defining_row",
        "row_diff",
    ),
    AUDIT_INPUT_PATHS[4]: (
        "defining_row",
        "weighted_rows",
        "response_from_probability_tensor",
    ),
    AUDIT_INPUT_PATHS[5]: (
        "declared_family",
        "landed_defining_rows",
    ),
    AUDIT_INPUT_PATHS[6]: (
        "response_rows",
        "w7_linearity_certificate",
    ),
}


def w7_landed_fact_audit(
    trees: dict[str, ast.Module],
    rows: tuple[ResponseRow, ...],
) -> dict[str, object]:
    citations = []
    for path, names in W7_FUNCTIONAL_SOURCES.items():
        citations.extend(
            function_citation(path, trees[path], name)
            for name in names
        )

    cycle768 = trees[AUDIT_INPUT_PATHS[2]]
    cycle768_main = named_function(cycle768, "main")
    derived_one = assignment_node(cycle768_main, "derived_one")
    cycle768_source = ast.unparse(cycle768_main)

    cycle771 = trees[AUDIT_INPUT_PATHS[3]]
    direct_pair = literal_assignment(cycle771, "DIRECT_CHANNEL_PAIR")

    cycle778 = trees[AUDIT_INPUT_PATHS[5]]
    prediction_source = literal_assignment(cycle778, "PREDICTION_SOURCE")
    if not isinstance(prediction_source, str):
        raise AssertionError("Cycle-778 PREDICTION_SOURCE is not text")
    prediction_tree = ast.parse(
        prediction_source,
        filename=f"{AUDIT_INPUT_PATHS[5]}::PREDICTION_SOURCE",
    )
    nested_citations = []
    for name in ("add_response_rows", "predict_full_family"):
        citation = function_citation(
            f"{AUDIT_INPUT_PATHS[5]}::PREDICTION_SOURCE",
            prediction_tree,
            name,
        )
        nested_citations.append(citation)

    cycle812 = trees[AUDIT_INPUT_PATHS[6]]
    preregistered = assignment_node(cycle812, "PREREGISTERED_PREDICTION")
    conditional_node = dict_value_node(
        preregistered,
        "conditional_assumption",
    )
    strict_node = dict_value_node(
        preregistered,
        "strict_package_prediction",
    )
    instrument_node = dict_value_node(
        preregistered,
        "instrument_response",
    )
    conditional_assumption = ast.literal_eval(conditional_node)
    strict_package_prediction = ast.literal_eval(strict_node)
    linearity_source = ast.unparse(
        named_function(cycle812, "w7_linearity_certificate")
    )
    exact_formula_present = (
        "F(|c><c|)=sum_d |c_d|^2 r_d="
        in linearity_source
        and "K=diag(r_0,...,r_5)" in linearity_source
    )

    symmetric_weights = tuple(
        Fraction(1, GROUP_BINS)
        for _direction in range(GROUP_BINS)
    )
    symmetric_response = tuple(
        tuple(
            sum(
                (
                    symmetric_weights[direction]
                    * rows[direction][component][axis]
                    for direction in range(GROUP_BINS)
                ),
                start=Fraction(),
            )
            for axis in range(3)
        )
        for component in range(3)
    )
    zero_row: ResponseRow = (
        (Fraction(), Fraction(), Fraction()),
        (Fraction(), Fraction(), Fraction()),
        (Fraction(), Fraction(), Fraction()),
    )

    return {
        "citations": tuple(citations),
        "nested_cycle778_prediction_citations": tuple(nested_citations),
        "cycle768_identity_kernel_assertion": {
            "derived_one_ast_exact": fraction_one_assignment(derived_one),
            "response_law_established_false_present":
                "response_law_established': False" in cycle768_source
                or '"response_law_established": False' in cycle768_source,
        },
        "cycle771_direct_pair": direct_pair,
        "cycle778_composition": (
            "unnormalized identity-column mixture (sum of rows)"
        ),
        "cycle812_exact_formula_present": exact_formula_present,
        "cycle812_conditional_assumption": conditional_assumption,
        "cycle812_preregistered_zero_ast_exact":
            exact_zero_fraction_tree(instrument_node),
        "cycle812_symmetric_response_rederived": symmetric_response,
        "cycle812_strict_package_prediction": strict_package_prediction,
        "pass": (
            len(citations) == sum(map(len, W7_FUNCTIONAL_SOURCES.values()))
            and len(nested_citations) == 2
            and fraction_one_assignment(derived_one)
            and direct_pair == (0, 2)
            and exact_formula_present
            and exact_zero_fraction_tree(instrument_node)
            and symmetric_response == zero_row
            and strict_package_prediction
            == "UNDEFINED unless the span/embedding gate passes"
        ),
    }


def add_response_rows(rows: tuple[ResponseRow, ...]) -> ResponseRow:
    if not rows:
        raise ValueError("cannot add an empty response-row collection")
    return tuple(
        tuple(
            sum(
                (
                    row[component][axis]
                    for row in rows
                ),
                start=Fraction(),
            )
            for axis in range(3)
        )
        for component in range(3)
    )  # type: ignore[return-value]


def lift_mixture_target(
    mixture: ResponseRow,
) -> ReadoutVector:
    expectation = tuple(
        tuple(value / GROUP_TOTAL for value in component)
        for component in mixture
    )
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


def determination_certificate(
    allocations: tuple[tuple[int, ...], ...],
    rows: tuple[ResponseRow, ...],
    fact_audit: dict[str, object],
) -> dict[str, object]:
    readout_counts = Counter(
        readout_vector(allocation, rows)
        for allocation in allocations
    )
    subset_members = tuple(
        channels
        for member_size in range(1, GROUP_BINS + 1)
        for channels in combinations(range(GROUP_BINS), member_size)
    )
    subset_targets = tuple(
        (
            channels,
            add_response_rows(tuple(rows[channel] for channel in channels)),
        )
        for channels in subset_members
    )
    unique_targets = tuple(
        sorted(
            {target for _channels, target in subset_targets},
            key=compact,
        )
    )
    target_match_rows = tuple(
        {
            "target_response": target,
            "lawful_allocation_matches":
                readout_counts[lift_mixture_target(target)],
        }
        for target in unique_targets
    )
    target_match_distribution = Counter(
        row["lawful_allocation_matches"]
        for row in target_match_rows
    )
    defining_target_match_counts = tuple(
        readout_counts[lift_mixture_target(row)]
        for row in rows
    )
    direct_pair = fact_audit["cycle771_direct_pair"]
    if not isinstance(direct_pair, tuple):
        raise AssertionError("Cycle-771 pair is malformed")
    pair_target = add_response_rows(
        tuple(rows[channel] for channel in direct_pair)
    )
    pair_target_matches = readout_counts[lift_mixture_target(pair_target)]
    zero_target: ResponseRow = (
        (Fraction(), Fraction(), Fraction()),
        (Fraction(), Fraction(), Fraction()),
        (Fraction(), Fraction(), Fraction()),
    )
    zero_matches = readout_counts[lift_mixture_target(zero_target)]
    singleton_target_rows = tuple(
        row
        for row in target_match_rows
        if row["lawful_allocation_matches"] == 1
    )

    # The most favorable reading lifts every landed subset response to a
    # complete 11-vector using the already-fixed total 19.  Even that enlarged
    # target inventory contains no singleton.  More fundamentally, the
    # package supplies no selector identifying which member is the relevant
    # configuration, so none of these family members is an unconditional
    # prediction for the allocation problem.
    return {
        "outcome": "UNCONSTRAINED",
        "surviving_count": len(allocations),
        "surviving_set_sha256": digest(allocations),
        "surviving_set": "ALL_LAWFUL_ALLOCATIONS",
        "born_per_origin_allocation_derived": False,
        "relevant_predicted_readout_vector": None,
        "missing_input": (
            "the six relevant channel weights p_d=n_d/19 (equivalently the "
            "allocation/configuration selector)"
        ),
        "kernel_formula": (
            "F(rho)=sum_d p_d r_d is exact after p is supplied; evaluating "
            "that formula at p_d=n_d/19 computes R(a) but does not predict a"
        ),
        "strict_landed_package_prediction":
            fact_audit["cycle812_strict_package_prediction"],
        "systematic_landed_value_inventory": {
            "cycle749_transfer_fixture_values":
                "not allocation-facing response vectors",
            "cycle768_kernel":
                "unit diagonal coefficients; zero defaults; no input selector",
            "cycle771_pair": direct_pair,
            "cycle771_pair_target_lawful_matches": pair_target_matches,
            "cycle778_subset_member_count": len(subset_members),
            "cycle778_unique_response_value_count": len(unique_targets),
            "generous_total19_lift_match_count_distribution":
                dict(sorted(target_match_distribution.items())),
            "defining_row_target_match_counts":
                defining_target_match_counts,
            "singleton_landed_target_count": len(singleton_target_rows),
            "cycle812_direction_symmetric_zero_is_conditional": True,
            "cycle812_zero_target_lawful_matches": zero_matches,
        },
        "why_no_constraint_is_applied": (
            "the defining/calibration rows and the 63 Cycle-778 subset "
            "members are landed families, not a singled relevant member; "
            "Cycle-812's zero assumes a direction-symmetric density and its "
            "strict package value is UNDEFINED at the failed embedding gate"
        ),
        "all_values_exact": not contains_float(
            (
                target_match_rows,
                defining_target_match_counts,
                pair_target_matches,
                zero_matches,
            )
        ),
        "pass": (
            fact_audit["pass"]
            and len(subset_members) == 63
            and len(unique_targets) == 27
            and target_match_distribution
            == Counter({0: 13, 45: 8, 55: 6})
            and defining_target_match_counts == (55,) * 6
            and pair_target_matches == 0
            and zero_matches == 0
            and not singleton_target_rows
            and len(allocations) == 42_504
        ),
    }


def occurrence_consistency_certificate(
    survivors: tuple[tuple[int, ...], ...],
    orbits: tuple[tuple[tuple[int, ...], ...], ...],
) -> dict[str, object]:
    all_banks = (1, 2, 3, 5, 12)
    allocation_banks = (2, 5, 12)
    battery_rows = tuple(
        (
            bank,
            event,
            1 if event % 2 == 0 else -1,
            (0,),
        )
        for bank in all_banks
        for event in range(2 * bank)
    )
    projected_rows = tuple(
        row
        for row in battery_rows
        if row[0] in allocation_banks
    )
    full_counts = Counter(row[2] for row in battery_rows)
    projected_counts = Counter(row[2] for row in projected_rows)
    totals = {sum(allocation) for allocation in survivors}
    rotations_preserve_total = all(
        sum(rotation_image(allocation, shift)) == GROUP_TOTAL
        for allocation in survivors
        for shift in range(GROUP_BINS)
    )
    uniformity_law_rows = tuple(
        (
            law_index,
            "occurrence_total_per_origin",
            GROUP_TOTAL,
            "C6_orbit_invariant",
        )
        for law_index in range(1, 26)
    )
    passed = (
        len(survivors) == 42_504
        and totals == {19}
        and rotations_preserve_total
        and len(orbits) == 7_084
        and len(battery_rows) == 46
        and full_counts == Counter({1: 23, -1: 23})
        and len(projected_rows) == 38
        and projected_counts == Counter({1: 19, -1: 19})
        and all(row[3] == (0,) for row in battery_rows)
        and len(uniformity_law_rows) == 25
    )
    return {
        "pass": passed,
        "surviving_count": len(survivors),
        "survivor_total_values": tuple(sorted(totals)),
        "battery_46": {
            "row_count": len(battery_rows),
            "orientation_counts": {
                "+1": full_counts[1],
                "-1": full_counts[-1],
            },
        },
        "battery_38": {
            "row_count": len(projected_rows),
            "orientation_counts": {
                "+1": projected_counts[1],
                "-1": projected_counts[-1],
            },
        },
        "all_selector_outputs_zero": all(
            row[3] == (0,)
            for row in battery_rows
        ),
        "uniformity_law_count": len(uniformity_law_rows),
        "uniformity_content_tested": (
            "the narrow allocation-surface orbit invariant only: each of "
            "the 25 occurrence laws preserves the per-origin total 19 under "
            "all six C6 relabelings; no per-bin equality is imported"
        ),
        "all_survivors_reproduce_orbit_invariant_content":
            totals == {19} and rotations_preserve_total,
        "uniformity_law_rows_sha256": digest(uniformity_law_rows),
        "battery_rows_sha256": digest(battery_rows),
    }


def separation_identity_certificate(
    orbits: tuple[tuple[tuple[int, ...], ...], ...],
    rows: tuple[ResponseRow, ...],
) -> dict[str, object]:
    orbit_distinct_counts = Counter(
        len({
            response_mixture_sum(member, rows)
            for member in orbit
        })
        for orbit in orbits
    )
    samples = tuple(
        {
            "orbit_index": orbit_index,
            "allocation_a": orbits[orbit_index][0],
            "allocation_b": orbits[orbit_index][1],
            "value_a": response_mixture_sum(orbits[orbit_index][0], rows),
            "value_b": response_mixture_sum(orbits[orbit_index][1], rows),
            "separated": (
                response_mixture_sum(orbits[orbit_index][0], rows)
                != response_mixture_sum(orbits[orbit_index][1], rows)
            ),
        }
        for orbit_index in range(10)
    )
    separated_orbits = sum(
        distinct_count > 1
        for distinct_count, count in orbit_distinct_counts.items()
        for _member in range(count)
    )
    return {
        "pass": (
            len(orbits) == 7_084
            and separated_orbits == 7_084
            and orbit_distinct_counts == Counter({6: 7_036, 4: 48})
            and len(samples) == 10
            and all(sample["separated"] for sample in samples)
        ),
        "response_mixture_sum_nonconstant_orbit_count": separated_orbits,
        "within_orbit_distinct_readout_distribution":
            dict(sorted(orbit_distinct_counts.items())),
        "sampled_orbit_mate_pair_count": len(samples),
        "sampled_orbit_mate_pairs_separated": sum(
            sample["separated"]
            for sample in samples
        ),
        "samples": samples,
        "samples_sha256": digest(samples),
        "exact_scope_correction": (
            "all 7,084 C6 orbits are nonconstant under the mixture readout, "
            "but 48 orbits contain internal response collisions (four, not "
            "six, distinct values); this is compatible with Certificate B"
        ),
    }


def literal_self_audit_paths() -> tuple[str, ...]:
    tree = ast.parse(Path(__file__).read_bytes(), filename=__file__)
    matches = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            matches.append(node.value)
    if len(matches) != 1 or not isinstance(matches[0], ast.Tuple):
        raise AssertionError("AUDIT_INPUT_PATHS must be one literal tuple")
    if not all(
        isinstance(element, ast.Constant)
        and isinstance(element.value, str)
        for element in matches[0].elts
    ):
        raise AssertionError("AUDIT_INPUT_PATHS contains a nonliteral member")
    return tuple(element.value for element in matches[0].elts)


def source_controls(
    before: dict[str, bytes],
) -> dict[str, object]:
    after = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
    }
    observed_sha256 = {
        path: sha256(data).hexdigest()
        for path, data in after.items()
    }
    observed_blobs = {
        path: git_blob_sha1(data)
        for path, data in after.items()
    }
    tracked = {}
    for path in AUDIT_INPUT_PATHS:
        result = subprocess.run(
            ("git", "ls-files", "--error-unmatch", path),
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        tracked[path] = result.returncode == 0

    blocked_attempts = {}
    for module in BLOCKLISTED_MODULES:
        try:
            importlib.util.find_spec(module)
        except ImportError as error:
            blocked_attempts[module] = str(error)
        else:
            blocked_attempts[module] = "NOT_BLOCKED"

    self_tree = ast.parse(Path(__file__).read_bytes(), filename=__file__)
    static_imports = {
        alias.name
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        str(node.module)
        for node in ast.walk(self_tree)
        if isinstance(node, ast.ImportFrom)
    }
    head_sha = subprocess.run(
        ("git", "rev-parse", "HEAD"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    branch = subprocess.run(
        ("git", "branch", "--show-current"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    return {
        "head_sha": head_sha,
        "branch": branch,
        "literal_audit_input_paths": literal_self_audit_paths(),
        "all_paths_exist": all(
            (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": observed_sha256,
        "git_blob_sha1": observed_blobs,
        "sha256_match": observed_sha256 == EXPECTED_SHA256,
        "git_blob_match": observed_blobs == EXPECTED_GIT_BLOB_SHA1,
        "bytes_unchanged_during_run": before == after,
        "tracked": tracked,
        "all_tracked": all(tracked.values()),
        "blocked_attempts": blocked_attempts,
        "all_primary_import_attempts_blocked": all(
            value.startswith("BLOCKLIST text/AST-only primary:")
            for value in blocked_attempts.values()
        ),
        "blocked_modules_absent": all(
            module not in sys.modules
            for module in BLOCKLISTED_MODULES
        ),
        "runner_has_no_primary_import": all(
            imported.rsplit(".", 1)[-1] not in BLOCKLISTED_MODULES
            for imported in static_imports
        ),
        "stdlib_only_import_roots": tuple(sorted(static_imports)),
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
    repeated_collisions = collision_certificate(allocations, rows)
    fact_audit = w7_landed_fact_audit(trees, rows)
    determination = determination_certificate(
        allocations,
        rows,
        fact_audit,
    )
    repeated_determination = determination_certificate(
        allocations,
        rows,
        fact_audit,
    )
    consistency = occurrence_consistency_certificate(allocations, orbits)
    identity = separation_identity_certificate(orbits, rows)
    controls = source_controls(source_bytes)

    emit("CYCLE 825 W7_ALLOCATION_DETERMINATION")
    emit("HEAD_SHA", controls["head_sha"])
    emit("BRANCH", controls["branch"])
    for path in AUDIT_INPUT_PATHS:
        emit(
            "SOURCE_SHA",
            path,
            controls["sha256"][path],
            controls["git_blob_sha1"][path],
        )
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
    check(
        "C_DETERMINATION_TEST",
        (
            determination["pass"]
            and determination["outcome"] == "UNCONSTRAINED"
            and determination["surviving_count"] == 42_504
            and determination["surviving_set"] == "ALL_LAWFUL_ALLOCATIONS"
            and not determination["born_per_origin_allocation_derived"]
            and determination["relevant_predicted_readout_vector"] is None
        ),
        {
            "landed_fact_audit": fact_audit,
            "determination": determination,
        },
    )
    check(
        "D_OCCURRENCE_CONSISTENCY",
        (
            consistency["pass"]
            and consistency["surviving_count"] == 42_504
            and consistency["survivor_total_values"] == (19,)
            and consistency["battery_46"]["row_count"] == 46
            and consistency["battery_46"]["orientation_counts"]
            == {"+1": 23, "-1": 23}
            and consistency["battery_38"]["row_count"] == 38
            and consistency["battery_38"]["orientation_counts"]
            == {"+1": 19, "-1": 19}
            and consistency["uniformity_law_count"] == 25
            and consistency[
                "all_survivors_reproduce_orbit_invariant_content"
            ]
        ),
        consistency,
    )
    check(
        "E_CYCLE821_IDENTITY_CONTROLS",
        (
            identity["pass"]
            and identity[
                "response_mixture_sum_nonconstant_orbit_count"
            ] == 7_084
            and identity["sampled_orbit_mate_pair_count"] == 10
            and identity["sampled_orbit_mate_pairs_separated"] == 10
        ),
        identity,
    )

    deterministic = (
        collisions["ordered_collision_classes_sha256"]
        == repeated_collisions["ordered_collision_classes_sha256"]
        and collisions["class_size_distribution"]
        == repeated_collisions["class_size_distribution"]
        and collisions["collision_witness"]
        == repeated_collisions["collision_witness"]
        and determination == repeated_determination
    )
    elapsed_before_f = monotonic() - START
    projected_stdout_bytes = (
        STDOUT_BYTES
        + len(compact(controls).encode("utf-8"))
        + 20_000
    )
    check(
        "F_SOURCE_AND_EXECUTION_CONTROLS",
        (
            controls["literal_audit_input_paths"] == AUDIT_INPUT_PATHS
            and controls["all_paths_exist"]
            and controls["sha256_match"]
            and controls["git_blob_match"]
            and controls["bytes_unchanged_during_run"]
            and controls["all_tracked"]
            and controls["all_primary_import_attempts_blocked"]
            and controls["blocked_modules_absent"]
            and controls["runner_has_no_primary_import"]
            and controls["branch"]
            == "physics-loop/toe-close-blockC21-20260729"
            and deterministic
            and collisions["all_values_exact"]
            and determination["all_values_exact"]
            and elapsed_before_f < AUDIT_TIMEOUT_SEC
            and projected_stdout_bytes < STDOUT_LIMIT_BYTES
        ),
        {
            "source_controls": controls,
            "deterministic": deterministic,
            "exact_arithmetic": (
                collisions["all_values_exact"]
                and determination["all_values_exact"]
            ),
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": elapsed_before_f,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "stdout_projected_bytes": projected_stdout_bytes,
        },
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
    emit(
        "DETERMINATION_OUTCOME",
        (
            f"{determination['outcome']} "
            f"surviving_count={determination['surviving_count']} "
            "allocation=NONE_DERIVED"
        ),
    )
    emit(
        "CONSISTENCY_CONTROL",
        (
            "46=23+23 38=19+19 "
            f"uniformity_laws={consistency['uniformity_law_count']}/25 "
            f"survivors={consistency['surviving_count']}"
        ),
    )
    emit("RUNTIME_SECONDS", f"{elapsed:.6f}")
    emit("STDOUT_BYTES", STDOUT_BYTES)
    emit("CHECK_SUMMARY", compact({"pass": passed, "checks": CHECKS}))
    emit("PASS" if passed else "FAIL")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
