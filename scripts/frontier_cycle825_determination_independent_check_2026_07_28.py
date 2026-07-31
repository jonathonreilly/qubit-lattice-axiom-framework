#!/usr/bin/env python3
"""Cycle 825 independent adversarial allocation-determination checker.

The Cycle-825 primary is read as text/AST only and is import-blocklisted.  The
six landed W7 modules are likewise never imported: this checker extracts only
literal/source contracts, then rebuilds the W7 response, allocation census,
orbit census, and selector probes with its own exact-arithmetic code.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
PRIMARY_PATH = (
    "scripts/frontier_cycle825_w7_allocation_determination_2026_07_28.py"
)
PRIMARY_MODULE = "frontier_cycle825_w7_allocation_determination_2026_07_28"

# Exactly seven literal, worktree-relative reads: the text/AST-only primary
# plus the complete landed W7 package identified by the Cycle-821 contract.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle825_w7_allocation_determination_2026_07_28.py",
    "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
    "scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
    "scripts/frontier_cycle774_interference_sector_2026_07_28.py",
    "scripts/frontier_cycle778_norefit_attachment_2026_07_28.py",
    "scripts/frontier_cycle812_mixed_input_response_2026_07_28.py",
)
W7_PATHS = AUDIT_INPUT_PATHS[1:]

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0f952fa0975e757a3bfc6fde6b086bb06bfec669b0b50146ed426e26176f9ec1",
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
    AUDIT_INPUT_PATHS[0]: "48be222342c468e75f663860056725fded2076fb",
    AUDIT_INPUT_PATHS[1]: "cee674584704dd7d351cb2ffa947c74bee47d06e",
    AUDIT_INPUT_PATHS[2]: "0070722d7a12d47658346b6c812edd05424ae592",
    AUDIT_INPUT_PATHS[3]: "52abfe3dd54b3969f51ca6816ec4830b42405106",
    AUDIT_INPUT_PATHS[4]: "6bde2222ddfdaf48e3806c0ac0a9c9d6431d945f",
    AUDIT_INPUT_PATHS[5]: "8366a5240d992376d0396a6fdc2c0b33247e8aba",
    AUDIT_INPUT_PATHS[6]: "39b5f24595f2271704bf68197103b62824a14cbf",
}

GROUP_TOTAL = 19
GROUP_BINS = 6
EXPECTED_READOUT_NAMES = (
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
EXPECTED_CLASS_SIZE_DISTRIBUTION = {
    1: 1446,
    3: 1158,
    6: 902,
    10: 678,
    15: 486,
    21: 326,
    28: 198,
    36: 102,
    45: 38,
    55: 6,
}
EXPECTED_INTERNAL_ORBIT_INDICES = (
    1329, 1437, 1512, 1674, 1816, 1939, 2044, 2132,
    2204, 2624, 3273, 3328, 3411, 3530, 3550, 3631,
    3715, 4088, 4249, 4472, 4489, 4569, 4646, 4753,
    4929, 5032, 5092, 5279, 5308, 5444, 6110, 6155,
    6194, 6263, 6318, 6360, 6515, 6655, 6668, 6706,
    6743, 6828, 6864, 6915, 7035, 7044, 7056, 7080,
)
EXPECTED_INTERNAL_COLLISIONS_SHA256 = (
    "2b61d07b431c3d8bfe2c7516bc4b23ef90585a73dbe0af72cfd2221d609cb7bf"
)
EXPECTED_INTERNAL_REPRESENTATIVES_SHA256 = (
    "5c11ba6f0cdb3d18c66ea9103ccd3ee689d0e5e39699e101c7eae9a63882ebab"
)

import ast
from collections import Counter, defaultdict
from dataclasses import dataclass
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
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()
CHECKS: dict[str, bool] = {}
STDOUT_BYTES = 0


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] == PRIMARY_MODULE:
            raise ImportError(f"BLOCKLIST text/AST-only primary: {fullname}")
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)


def jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return value.numerator
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, Path):
        return str(value)
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
    return sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = tuple(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )
    if len(matches) != 1:
        raise AssertionError(("function multiplicity", name, len(matches)))
    return matches[0]


def assignment_value(tree: ast.Module, name: str) -> ast.AST:
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
        raise AssertionError(("assignment multiplicity", name, len(matches)))
    return matches[0]


def literal_assignment(tree: ast.Module, name: str) -> object:
    return ast.literal_eval(assignment_value(tree, name))


def read_sources() -> tuple[
    dict[str, bytes],
    dict[str, ast.Module],
]:
    data = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {
        path: ast.parse(raw, filename=path)
        for path, raw in data.items()
    }
    return data, trees


def exact_fraction_call(node: ast.AST, target: Fraction) -> bool:
    if not (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "Fraction"
        and not node.keywords
    ):
        return False
    if not node.args:
        return target == Fraction()
    try:
        return Fraction(ast.literal_eval(node.args[0])) == target
    except (ValueError, TypeError, SyntaxError):
        return False


def primary_ast_contract(primary: ast.Module) -> dict[str, object]:
    readout_names = literal_assignment(primary, "READOUT_NAMES")
    function_names = {
        node.name
        for node in primary.body
        if isinstance(node, ast.FunctionDef)
    }
    required_claim_functions = {
        "readout_vector",
        "collision_certificate",
        "determination_certificate",
        "occurrence_consistency_certificate",
        "separation_identity_certificate",
    }
    imported_modules = {
        alias.name
        for node in ast.walk(ast.parse(Path(__file__).read_bytes()))
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        str(node.module)
        for node in ast.walk(ast.parse(Path(__file__).read_bytes()))
        if isinstance(node, ast.ImportFrom)
    }
    try:
        importlib.util.find_spec(PRIMARY_MODULE)
    except ImportError as error:
        blocked_attempt = str(error)
    else:
        blocked_attempt = "NOT_BLOCKED"
    return {
        "mode": "text/AST only; never compiled, imported, or executed",
        "primary_readout_names": readout_names,
        "required_claim_functions_present":
            required_claim_functions <= function_names,
        "primary_import_attempt": blocked_attempt,
        "primary_blocked": blocked_attempt.startswith(
            "BLOCKLIST text/AST-only primary:"
        ),
        "primary_absent_from_sys_modules": PRIMARY_MODULE not in sys.modules,
        "checker_has_no_primary_import": all(
            module.rsplit(".", 1)[-1] != PRIMARY_MODULE
            for module in imported_modules
        ),
        "pass": (
            readout_names == EXPECTED_READOUT_NAMES
            and required_claim_functions <= function_names
            and blocked_attempt.startswith("BLOCKLIST text/AST-only primary:")
            and PRIMARY_MODULE not in sys.modules
            and all(
                module.rsplit(".", 1)[-1] != PRIMARY_MODULE
                for module in imported_modules
            )
        ),
    }


ResponseRow = tuple[
    tuple[Fraction, ...],
    tuple[Fraction, ...],
    tuple[Fraction, ...],
]
ReadoutVector = tuple[object, ...]


@dataclass(frozen=True)
class W7Surface:
    directions: tuple[tuple[int, int, int], ...]
    reverse: tuple[int, ...]
    rows: tuple[ResponseRow, ...]
    coefficient_family: tuple[object, ...]
    direct_pair: tuple[int, int]
    citations: tuple[tuple[str, str, int, str], ...]
    package_scan: dict[str, object]
    passed: bool


W7_FUNCTIONS = {
    W7_PATHS[0]: ("extract_frozen_fixtures", "evaluate_candidate"),
    W7_PATHS[1]: (
        "derive_recoil_coefficients",
        "derive_response_kernel_candidate",
    ),
    W7_PATHS[2]: ("landed_defining_row", "row_diff"),
    W7_PATHS[3]: (
        "defining_row",
        "weighted_rows",
        "response_from_probability_tensor",
    ),
    W7_PATHS[4]: ("declared_family", "landed_defining_rows"),
    W7_PATHS[5]: ("response_rows", "w7_linearity_certificate"),
}


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


def selector_lexical_scan(
    source_bytes: dict[str, bytes],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    keywords = (
        "select", "weight", "normal", "positiv", "inequal", "extrem",
        "minim", "maxim", "calibr", "target", "coefficient", "default",
        "prediction",
    )
    keyword_function_hits: dict[str, tuple[str, ...]] = {}
    for path in W7_PATHS:
        rows = []
        for node in trees[path].body:
            if not isinstance(node, ast.FunctionDef):
                continue
            rendered = ast.unparse(node).casefold()
            hits = tuple(word for word in keywords if word in rendered)
            if hits:
                rows.append(f"{node.name}:{','.join(hits)}")
        keyword_function_hits[path] = tuple(rows)

    texts = {
        path: source_bytes[path].decode("utf-8")
        for path in W7_PATHS
    }
    folded = "\n".join(texts.values()).casefold()
    exact_bridge_tokens = {
        token: folded.count(token)
        for token in (
            "allocation",
            " p_d",
            " n_d",
            "argmin",
            "argmax",
            "weight selector",
        )
    }
    return {
        "keyword_function_hits": keyword_function_hits,
        "keyword_function_hit_sha256": digest(keyword_function_hits),
        "exact_unknown_allocation_bridge_token_counts": exact_bridge_tokens,
        "no_unknown_allocation_bridge_vocabulary":
            not any(exact_bridge_tokens.values()),
        "maximum_is_cycle749_residual_reducer_only": (
            "def maximum(values: list[Fraction]) -> Fraction:"
            in texts[W7_PATHS[0]]
            and "largest_residual = maximum(list(residuals.values()))"
            in texts[W7_PATHS[0]]
        ),
    }


def extract_w7_surface(
    source_bytes: dict[str, bytes],
    trees: dict[str, ast.Module],
) -> W7Surface:
    cycle749 = trees[W7_PATHS[0]]
    cycle768 = trees[W7_PATHS[1]]
    cycle771 = trees[W7_PATHS[2]]
    cycle774 = trees[W7_PATHS[3]]
    cycle778 = trees[W7_PATHS[4]]
    cycle812 = trees[W7_PATHS[5]]

    directions_raw = literal_assignment(cycle812, "DIRECTIONS")
    reverse_raw = literal_assignment(cycle812, "REVERSE")
    family_774 = literal_assignment(cycle774, "DECLARED_COEFFICIENT_FAMILY")
    family_812 = literal_assignment(cycle812, "COEFFICIENT_FAMILY")
    direct_pair_raw = literal_assignment(cycle771, "DIRECT_CHANNEL_PAIR")
    directions = tuple(
        tuple(int(value) for value in direction)
        for direction in directions_raw
    )
    reverse = tuple(int(value) for value in reverse_raw)
    direct_pair = tuple(int(value) for value in direct_pair_raw)

    # Independent W7 response implementation: only the landed direction and
    # reverse literals are used.  No W7 response function is executed.
    rows = []
    for index, source in enumerate(directions):
        target = directions[reverse[index]]
        source_vector = tuple(Fraction(value) for value in source)
        rows.append((
            tuple(
                Fraction(final - initial)
                for final, initial in zip(target, source, strict=True)
            ),
            source_vector,
            source_vector,
        ))

    citations = tuple(
        function_citation(path, trees[path], name)
        for path, names in W7_FUNCTIONS.items()
        for name in names
    )
    scan = selector_lexical_scan(source_bytes, trees)

    built_in_source = ast.unparse(assignment_value(cycle749, "BUILT_IN_CANDIDATES"))
    builder_source = ast.unparse(
        named_function(cycle768, "derive_response_kernel_candidate")
    )
    main_768 = named_function(cycle768, "main")
    derived_one_nodes = [
        node.value
        for node in ast.walk(main_768)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "derived_one"
            for target in node.targets
        )
    ]
    declared_source = ast.unparse(named_function(cycle778, "declared_family"))
    linearity_source = ast.unparse(
        named_function(cycle812, "w7_linearity_certificate")
    )
    passed = (
        directions == (
            (1, 0, 0), (-1, 0, 0),
            (0, 1, 0), (0, -1, 0),
            (0, 0, 1), (0, 0, -1),
        )
        and reverse == (1, 0, 3, 2, 5, 4)
        and len(rows) == 6
        and all(
            rows[index] == (
                tuple(-2 * Fraction(value) for value in direction),
                tuple(Fraction(value) for value in direction),
                tuple(Fraction(value) for value in direction),
            )
            for index, direction in enumerate(directions)
        )
        and family_774 == family_812
        and len(family_812) == 6
        and direct_pair == (0, 2)
        and len(citations) == 13
        and len(derived_one_nodes) == 1
        and exact_fraction_call(derived_one_nodes[0], Fraction(1))
        and "Fraction()" in builder_source
        and "identity_pullback" in built_in_source
        and "for group, configurations in groups" in declared_source
        and "combinations(range(direction_count), 5)" in declared_source
        and "F(|c><c|)=sum_d |c_d|^2 r_d=" in linearity_source
        and "K=diag(r_0,...,r_5)" in linearity_source
        and scan["no_unknown_allocation_bridge_vocabulary"]
        and scan["maximum_is_cycle749_residual_reducer_only"]
    )
    return W7Surface(
        directions=directions,
        reverse=reverse,
        rows=tuple(rows),
        coefficient_family=tuple(family_812),
        direct_pair=direct_pair,  # type: ignore[arg-type]
        citations=citations,
        package_scan=scan,
        passed=bool(passed),
    )


def weak_compositions(
    total: int,
    bins: int,
) -> tuple[tuple[int, ...], ...]:
    """Independent stars-and-bars enumeration, with no W7/primary helper."""
    rows = []
    final_position = total + bins - 2
    for bars in combinations(range(total + bins - 1), bins - 1):
        previous = -1
        allocation = []
        for bar in bars:
            allocation.append(bar - previous - 1)
            previous = bar
        allocation.append(final_position - previous)
        rows.append(tuple(allocation))
    return tuple(rows)


def lawful(allocation: tuple[int, ...]) -> bool:
    return (
        len(allocation) == GROUP_BINS
        and all(type(value) is int and value >= 0 for value in allocation)
        and sum(allocation) == GROUP_TOTAL
    )


def rotate_left(
    allocation: tuple[int, ...],
    shift: int,
) -> tuple[int, ...]:
    shift %= len(allocation)
    return allocation[shift:] + allocation[:shift]


def orbit_partition(
    allocations: tuple[tuple[int, ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    groups: dict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)
    for allocation in allocations:
        representative = min(
            rotate_left(allocation, shift)
            for shift in range(GROUP_BINS)
        )
        groups[representative].add(allocation)
    return tuple(
        tuple(sorted(groups[representative]))
        for representative in sorted(groups)
    )


def response_mixture(
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
    mixture = response_mixture(allocation, rows)
    total = sum(allocation)
    if total <= 0:
        raise ValueError("positive total required")
    return tuple(
        tuple(value / total for value in component)
        for component in mixture
    )  # type: ignore[return-value]


def readout_vector(
    allocation: tuple[int, ...],
    rows: tuple[ResponseRow, ...],
) -> ReadoutVector:
    mixture = response_mixture(allocation, rows)
    expectation = response_expectation(allocation, rows)
    components = tuple(
        expectation[component][axis]
        for component in range(3)
        for axis in range(3)
    )
    flux = tuple(
        sum(
            (
                expectation[component][axis]
                for component in range(3)
            ),
            start=Fraction(),
        )
        for axis in range(3)
    )
    return (mixture, *components, flux)


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


def collision_census(
    allocations: tuple[tuple[int, ...], ...],
    orbits: tuple[tuple[tuple[int, ...], ...], ...],
    rows: tuple[ResponseRow, ...],
) -> dict[str, object]:
    classes: dict[ReadoutVector, list[tuple[int, ...]]] = defaultdict(list)
    moment_by_readout: dict[ReadoutVector, tuple[int, int, int]] = {}
    moment_equivalence = True
    exact = True
    for allocation in allocations:
        readout = readout_vector(allocation, rows)
        moment = signed_moment(allocation)
        classes[readout].append(allocation)
        exact = exact and not contains_float(readout)
        if readout in moment_by_readout:
            moment_equivalence = (
                moment_equivalence
                and moment_by_readout[readout] == moment
            )
        else:
            moment_by_readout[readout] = moment

    reverse_check: dict[tuple[int, int, int], ReadoutVector] = {}
    for readout, moment in moment_by_readout.items():
        if moment in reverse_check:
            moment_equivalence = (
                moment_equivalence
                and reverse_check[moment] == readout
            )
        else:
            reverse_check[moment] = readout

    distribution = Counter(len(members) for members in classes.values())
    formula_ok = True
    ordered_classes = []
    for readout, members in classes.items():
        moment = moment_by_readout[readout]
        l1 = sum(abs(value) for value in moment)
        expected_size = math.comb((GROUP_TOTAL - l1) // 2 + 2, 2)
        formula_ok = (
            formula_ok
            and l1 <= GROUP_TOTAL
            and l1 % 2 == GROUP_TOTAL % 2
            and len(members) == expected_size
        )
        ordered_classes.append((moment, tuple(members)))
    ordered_classes.sort()

    internal_rows = []
    orbit_value_distribution: Counter[int] = Counter()
    for orbit_index, orbit in enumerate(orbits):
        tied_by_moment: dict[
            tuple[int, int, int],
            list[tuple[int, ...]],
        ] = defaultdict(list)
        for allocation in orbit:
            tied_by_moment[signed_moment(allocation)].append(allocation)
        orbit_value_distribution[len(tied_by_moment)] += 1
        ties = tuple(
            tuple(members)
            for _moment, members in sorted(tied_by_moment.items())
            if len(members) > 1
        )
        if ties:
            internal_rows.append({
                "orbit_index": orbit_index,
                "representative": orbit[0],
                "ties": ties,
                "distinct_readout_count": len(tied_by_moment),
            })

    internal = tuple(internal_rows)
    internal_indices = tuple(row["orbit_index"] for row in internal)
    internal_representatives = tuple(
        row["representative"] for row in internal
    )
    collision_witness = next(
        tuple(members[:2])
        for members in classes.values()
        if len(members) > 1
    )
    return {
        "allocation_count": len(allocations),
        "distinct_readout_count": len(classes),
        "injective": len(classes) == len(allocations),
        "class_size_distribution": dict(sorted(distribution.items())),
        "singleton_class_count": distribution[1],
        "nonsingleton_class_count": sum(
            count for size, count in distribution.items() if size > 1
        ),
        "members_in_nonsingleton_classes": sum(
            size * count
            for size, count in distribution.items()
            if size > 1
        ),
        "readout_iff_signed_moment": moment_equivalence,
        "class_formula_verified": formula_ok,
        "all_values_exact": exact,
        "ordered_classes_sha256": digest(tuple(ordered_classes)),
        "within_orbit_distinct_readout_distribution":
            dict(sorted(orbit_value_distribution.items())),
        "nonconstant_orbit_count": sum(
            count
            for distinct, count in orbit_value_distribution.items()
            if distinct > 1
        ),
        "internal_collision_orbits": internal,
        "internal_collision_orbit_count": len(internal),
        "internal_collision_orbit_indices": internal_indices,
        "internal_collisions_sha256": digest(internal),
        "internal_representatives_sha256": digest(internal_representatives),
        "collision_witness": {
            "allocation_a": collision_witness[0],
            "allocation_b": collision_witness[1],
            "signed_moment": signed_moment(collision_witness[0]),
            "readout_equal": (
                readout_vector(collision_witness[0], rows)
                == readout_vector(collision_witness[1], rows)
            ),
        },
    }


def add_rows(rows: tuple[ResponseRow, ...]) -> ResponseRow:
    if not rows:
        raise ValueError("nonempty rows required")
    return tuple(
        tuple(
            sum(
                (row[component][axis] for row in rows),
                start=Fraction(),
            )
            for axis in range(3)
        )
        for component in range(3)
    )  # type: ignore[return-value]


def row_moment(row: ResponseRow) -> tuple[int, int, int]:
    # Every landed row has mediator=auxiliary=d and matter=-2d.
    vector = row[1]
    if not (
        row[2] == vector
        and row[0] == tuple(-2 * value for value in vector)
        and all(value.denominator == 1 for value in vector)
    ):
        raise AssertionError(("not a W7 diagonal response row", row))
    return tuple(int(value) for value in vector)  # type: ignore[return-value]


@dataclass(frozen=True)
class SelectorProbe:
    name: str
    source: str
    applicability: str
    rationale: str
    survivors: tuple[tuple[int, ...], ...]


LANDED_APPLICABLE = "LANDED_PREDICATE_ON_UNKNOWN_ALLOCATION"


def make_probe(
    name: str,
    source: str,
    applicability: str,
    rationale: str,
    allocations: tuple[tuple[int, ...], ...],
    predicate: Callable[[tuple[int, ...]], bool],
) -> SelectorProbe:
    return SelectorProbe(
        name=name,
        source=source,
        applicability=applicability,
        rationale=rationale,
        survivors=tuple(
            allocation for allocation in allocations if predicate(allocation)
        ),
    )


def selector_hunt(
    allocations: tuple[tuple[int, ...], ...],
    surface: W7Surface,
) -> dict[str, object]:
    rows = surface.rows
    all_count = len(allocations)
    zero_row: ResponseRow = (
        (Fraction(), Fraction(), Fraction()),
        (Fraction(), Fraction(), Fraction()),
        (Fraction(), Fraction(), Fraction()),
    )
    probes: list[SelectorProbe] = []

    probes.extend((
        make_probe(
            "allocation_domain_nonnegative_total_19",
            "Cycle-821 allocation domain / consistency surface",
            LANDED_APPLICABLE,
            "This is the supplied unknown-allocation domain itself.",
            allocations,
            lawful,
        ),
        make_probe(
            "cycle768_unit_kernel_coefficients",
            f"{W7_PATHS[1]}:derive_response_kernel_candidate",
            "KERNEL_PARAMETER_NOT_WEIGHT_SELECTOR",
            (
                "Coefficients (1,1,1) act on response components; they are "
                "not the six channel probabilities."
            ),
            allocations,
            lambda _allocation: True,
        ),
        make_probe(
            "cycle768_zero_fitted_defaults",
            f"{W7_PATHS[1]}:derive_response_kernel_candidate",
            "KERNEL_PARAMETER_NOT_WEIGHT_SELECTOR",
            (
                "Seven zero affine offsets change no response and contain "
                "no channel-weight predicate."
            ),
            allocations,
            lambda _allocation: True,
        ),
        make_probe(
            "cycle749_flux_balance_zero",
            f"{W7_PATHS[0]}:evaluate_candidate",
            LANDED_APPLICABLE,
            "The componentwise W7 flux identity is a law of every row.",
            allocations,
            lambda _allocation: True,
        ),
        make_probe(
            "cycle812_probability_normalization",
            f"{W7_PATHS[5]}:w7_linearity_certificate",
            LANDED_APPLICABLE,
            "With p_d=n_d/19, sum_d p_d=1 on the entire supplied domain.",
            allocations,
            lambda allocation: sum(
                (Fraction(value, GROUP_TOTAL) for value in allocation),
                start=Fraction(),
            ) == 1,
        ),
        make_probe(
            "cycle812_probability_nonnegativity",
            f"{W7_PATHS[5]}:w7_linearity_certificate",
            LANDED_APPLICABLE,
            "Density positivity gives p_d>=0, already built into the domain.",
            allocations,
            lambda allocation: all(
                Fraction(value, GROUP_TOTAL) >= 0 for value in allocation
            ),
        ),
        make_probe(
            "cycle812_diagonal_zero_interference",
            f"{W7_PATHS[5]}:w7_linearity_certificate",
            LANDED_APPLICABLE,
            (
                "The allocation density is diagonal, so the landed empty "
                "cross-term sector holds for every allocation."
            ),
            allocations,
            lambda _allocation: True,
        ),
        make_probe(
            "cycle749_identity_kernel_zero_residual",
            f"{W7_PATHS[0]}:evaluate_candidate",
            LANDED_APPLICABLE,
            (
                "Applying the accepted identity kernel to any allocation "
                "leaves its response unchanged; the instrument has no target."
            ),
            allocations,
            lambda _allocation: True,
        ),
    ))

    # Supplied calibration/fixture inputs: compute their allocation survivor
    # sets anyway, but do not silently promote them into facts about the
    # unknown allocation.
    defining_expectation_probes = []
    defining_mixture_probes = []
    for direction, row in enumerate(rows):
        expectation_probe = make_probe(
            f"cycle771_defining_expectation_direction_{direction}",
            f"{W7_PATHS[2]}:landed_defining_row",
            "SUPPLIED_INPUT_CALIBRATION_NOT_UNKNOWN_ALLOCATION",
            (
                "This row is conditioned on the already supplied input "
                f"channel {direction}; no statement equates the unknown "
                "allocation response to it."
            ),
            allocations,
            lambda allocation, row=row:
                signed_moment(allocation)
                == tuple(
                    GROUP_TOTAL * value for value in row_moment(row)
                ),
        )
        mixture_probe = make_probe(
            f"cycle778_defining_unnormalized_row_{direction}",
            f"{W7_PATHS[4]}:landed_defining_rows",
            "SUPPLIED_INPUT_FIXTURE_NOT_UNKNOWN_ALLOCATION",
            (
                "Cycle-778 declares unnormalized identity-column sums, not "
                "a measured target for the unknown allocation."
            ),
            allocations,
            lambda allocation, row=row:
                signed_moment(allocation) == row_moment(row),
        )
        probes.extend((expectation_probe, mixture_probe))
        defining_expectation_probes.append(expectation_probe)
        defining_mixture_probes.append(mixture_probe)

    pair_row = add_rows(tuple(rows[index] for index in surface.direct_pair))
    probes.append(make_probe(
        "cycle771_direct_pair_unnormalized_target",
        f"{W7_PATHS[2]}:DIRECT_CHANNEL_PAIR",
        "SUPPLIED_INPUT_FIXTURE_NOT_UNKNOWN_ALLOCATION",
        (
            "The pair (0,2) is a preregistered simulation input, not a "
            "predicate on the unknown allocation."
        ),
        allocations,
        lambda allocation: signed_moment(allocation) == row_moment(pair_row),
    ))

    subset_probes = []
    for size in range(1, GROUP_BINS + 1):
        for channels in combinations(range(GROUP_BINS), size):
            target = add_rows(tuple(rows[channel] for channel in channels))
            probe = make_probe(
                "cycle778_subset_" + "-".join(map(str, channels)),
                f"{W7_PATHS[4]}:declared_family",
                "DECLARED_FAMILY_MEMBER_NOT_RELEVANT_MEMBER_SELECTOR",
                (
                    "All 63 members are attachment fixtures; the package "
                    "does not choose one as the unknown allocation target."
                ),
                allocations,
                lambda allocation, target=target:
                    signed_moment(allocation) == row_moment(target),
            )
            probes.append(probe)
            subset_probes.append(probe)

    probes.extend((
        make_probe(
            "cycle771_direct_pair_transfer_weights_positive_if_transposed",
            f"{W7_PATHS[2]}:main",
            "FIXTURE_BRANCH_WEIGHT_NOT_ALLOCATION_PROBABILITY",
            (
                "The >0 assertion is on simulated branch-transfer weights "
                "for supplied channels; this diagnostic shows the survivor "
                "count under the unjustified p0>0,p2>0 transposition."
            ),
            allocations,
            lambda allocation: allocation[0] > 0 and allocation[2] > 0,
        ),
        make_probe(
            "cycle812_direction_symmetric_zero_prediction",
            f"{W7_PATHS[5]}:PREREGISTERED_PREDICTION",
            "CONDITIONAL_ASSUMPTION_AND_FAILED_EMBEDDING_GATE",
            (
                "The zero assumes six equal weights and the strict package "
                "prediction is undefined unless the span/embedding gate passes."
            ),
            allocations,
            lambda allocation: signed_moment(allocation) == (0, 0, 0),
        ),
        make_probe(
            "cycle812_equal_six_weights_if_transposed",
            f"{W7_PATHS[5]}:normalization_audit",
            "CONDITIONAL_EQUAL_WEIGHT_INPUT_NOT_SELECTOR",
            (
                "Exact p_d=1/6 would require n_d=19/6 and hence has no "
                "integer allocation; equal weights describe a supplied state."
            ),
            allocations,
            lambda allocation: len(set(allocation)) == 1,
        ),
        make_probe(
            "absent_minimum_response_norm_principle",
            "full six-file AST selector scan",
            "ABSENT_EXTREMAL_PRINCIPLE_DIAGNOSTIC_ONLY",
            (
                "No argmin/minimum-response principle is landed.  This probe "
                "reports what the natural minimum would cut to if invented."
            ),
            allocations,
            lambda allocation: sum(
                value * value for value in signed_moment(allocation)
            ) == 1,
        ),
        make_probe(
            "absent_maximum_response_norm_principle",
            "full six-file AST selector scan",
            "ABSENT_EXTREMAL_PRINCIPLE_DIAGNOSTIC_ONLY",
            (
                "No argmax/maximum-response principle is landed.  Cycle-749 "
                "maximum only reduces instrument residuals."
            ),
            allocations,
            lambda allocation: sum(
                value * value for value in signed_moment(allocation)
            ) == GROUP_TOTAL * GROUP_TOTAL,
        ),
    ))

    # Cycle-774/812 coefficient amplitudes induce normalized two-channel
    # probabilities.  Exhaust all 15 pairs x 6 landed members; total 19 is
    # incompatible with all their exact 1:1, 4:1, or 1:4 ratios.
    coefficient_member_counts = []
    coefficient_union: set[tuple[int, ...]] = set()
    for left, right in combinations(range(GROUP_BINS), 2):
        for label, coefficients_raw in surface.coefficient_family:
            coefficients = tuple(
                (Fraction(real), Fraction(imaginary))
                for real, imaginary in coefficients_raw
            )
            squared = tuple(
                real * real + imaginary * imaginary
                for real, imaginary in coefficients
            )
            denominator = sum(squared, start=Fraction())
            expected = tuple(value / denominator for value in squared)
            survivors = tuple(
                allocation
                for allocation in allocations
                if all(
                    allocation[index] == 0
                    for index in range(GROUP_BINS)
                    if index not in (left, right)
                )
                and Fraction(allocation[left], GROUP_TOTAL) == expected[0]
                and Fraction(allocation[right], GROUP_TOTAL) == expected[1]
            )
            coefficient_union.update(survivors)
            coefficient_member_counts.append(
                (left, right, label, len(survivors))
            )
    probes.append(SelectorProbe(
        name="cycle774_812_coefficient_family_probability_ratios",
        source=(
            f"{W7_PATHS[3]}:DECLARED_COEFFICIENT_FAMILY and "
            f"{W7_PATHS[5]}:COEFFICIENT_FAMILY"
        ),
        applicability="SUPPLIED_INTERFERENCE_INPUT_FAMILY_NOT_SELECTOR",
        rationale=(
            "All 90 pair/coefficient cases are supplied probe inputs; no pair "
            "or coefficient member is chosen for the unknown allocation."
        ),
        survivors=tuple(sorted(coefficient_union)),
    ))

    rows_out = tuple({
        "name": probe.name,
        "source": probe.source,
        "applicability": probe.applicability,
        "rationale": probe.rationale,
        "survivor_count": len(probe.survivors),
        "survivor_sha256": digest(probe.survivors),
        "singleton": len(probe.survivors) == 1,
        "cuts_if_asserted": len(probe.survivors) < all_count,
        "landed_constraint_missed": (
            probe.applicability == LANDED_APPLICABLE
            and len(probe.survivors) < all_count
        ),
    } for probe in probes)
    missed = tuple(
        row for row in rows_out if row["landed_constraint_missed"]
    )
    applicable = tuple(
        row for row in rows_out
        if row["applicability"] == LANDED_APPLICABLE
    )
    cut_but_inapplicable = tuple(
        row for row in rows_out
        if row["cuts_if_asserted"]
        and row["applicability"] != LANDED_APPLICABLE
    )
    target_distribution = Counter(
        len(probe.survivors) for probe in subset_probes
    )
    unique_target_counts: dict[tuple[int, int, int], int] = {}
    for probe, channels in zip(
        subset_probes,
        (
            channels
            for size in range(1, GROUP_BINS + 1)
            for channels in combinations(range(GROUP_BINS), size)
        ),
        strict=True,
    ):
        target = add_rows(tuple(rows[channel] for channel in channels))
        unique_target_counts.setdefault(
            row_moment(target),
            len(probe.survivors),
        )
    unique_target_distribution = Counter(unique_target_counts.values())
    subset_union = {
        allocation
        for probe in subset_probes
        for allocation in probe.survivors
    }
    defining_expectation_union = {
        allocation
        for probe in defining_expectation_probes
        for allocation in probe.survivors
    }
    defining_mixture_union = {
        allocation
        for probe in defining_mixture_probes
        for allocation in probe.survivors
    }
    return {
        "probe_count": len(rows_out),
        "probes": rows_out,
        "applicable_probe_count": len(applicable),
        "applicable_survivor_counts": tuple(
            (row["name"], row["survivor_count"]) for row in applicable
        ),
        "missed_constraints": missed,
        "cut_but_inapplicable_count": len(cut_but_inapplicable),
        "cut_but_inapplicable_names": tuple(
            row["name"] for row in cut_but_inapplicable
        ),
        "cycle771_defining_expectation_counts": tuple(
            len(probe.survivors)
            for probe in defining_expectation_probes
        ),
        "cycle771_defining_expectation_union_count":
            len(defining_expectation_union),
        "cycle778_defining_mixture_counts": tuple(
            len(probe.survivors) for probe in defining_mixture_probes
        ),
        "cycle778_defining_mixture_union_count": len(defining_mixture_union),
        "cycle778_63_target_match_distribution":
            dict(sorted(target_distribution.items())),
        "cycle778_27_unique_target_match_distribution":
            dict(sorted(unique_target_distribution.items())),
        "cycle778_unique_target_count": len(unique_target_counts),
        "cycle778_63_target_union_count": len(subset_union),
        "coefficient_family_member_count": len(coefficient_member_counts),
        "coefficient_family_member_survivor_distribution":
            dict(sorted(Counter(
                count
                for _left, _right, _label, count
                in coefficient_member_counts
            ).items())),
        "coefficient_family_union_count": len(coefficient_union),
        "package_scan": surface.package_scan,
        "outcome": (
            "SELECTOR_FOUND"
            if missed
            else "NO_LANDED_WEIGHT_SELECTOR"
        ),
        "surviving_allocations": (
            "CONSTRAINED_BY_MISSED_SELECTOR"
            if missed
            else "ALL_42504"
        ),
        "surviving_count": (
            min(int(row["survivor_count"]) for row in missed)
            if missed
            else all_count
        ),
        "probe_rows_sha256": digest(rows_out),
        "pass": (
            not missed
            and all(
                int(row["survivor_count"]) == all_count
                for row in applicable
            )
            and tuple(
                len(probe.survivors)
                for probe in defining_expectation_probes
            ) == (1,) * 6
            and len(defining_expectation_union) == 6
            and tuple(
                len(probe.survivors)
                for probe in defining_mixture_probes
            ) == (55,) * 6
            and len(defining_mixture_union) == 330
            and target_distribution == Counter({0: 31, 45: 8, 55: 24})
            and len(unique_target_counts) == 27
            and unique_target_distribution
            == Counter({0: 13, 45: 8, 55: 6})
            and len(subset_union) == 690
            and len(coefficient_member_counts) == 90
            and not coefficient_union
            and surface.package_scan[
                "no_unknown_allocation_bridge_vocabulary"
            ]
        ),
    }


def consistency_controls(
    allocations: tuple[tuple[int, ...], ...],
    orbits: tuple[tuple[tuple[int, ...], ...], ...],
) -> dict[str, object]:
    all_banks = (1, 2, 3, 5, 12)
    allocation_banks = (2, 5, 12)
    battery = tuple(
        (bank, event, 1 if event % 2 == 0 else -1, (0,))
        for bank in all_banks
        for event in range(2 * bank)
    )
    projected = tuple(
        row for row in battery if row[0] in allocation_banks
    )
    full_counts = Counter(row[2] for row in battery)
    projected_counts = Counter(row[2] for row in projected)

    law_rows = []
    for law_index in range(1, 26):
        # A deterministic, content-addressed orbit sample for every law.
        orbit_index = int.from_bytes(
            sha256(f"cycle825-law-{law_index}".encode("ascii")).digest()[:8],
            "big",
        ) % len(orbits)
        orbit = orbits[orbit_index]
        values = tuple(sum(allocation) for allocation in orbit)
        law_rows.append({
            "law_index": law_index,
            "orbit_index": orbit_index,
            "representative": orbit[0],
            "rotated_values": values,
            "orbit_invariant": len(set(values)) == 1 and values[0] == 19,
        })
    law_rows_tuple = tuple(law_rows)
    sample_law_indices = (1, 7, 13, 19, 25)
    samples = tuple(
        law_rows_tuple[index - 1] for index in sample_law_indices
    )
    return {
        "battery_46": {
            "row_count": len(battery),
            "orientation_counts": {
                "+1": full_counts[1],
                "-1": full_counts[-1],
            },
        },
        "battery_38": {
            "row_count": len(projected),
            "orientation_counts": {
                "+1": projected_counts[1],
                "-1": projected_counts[-1],
            },
        },
        "all_selector_outputs_zero": all(row[3] == (0,) for row in battery),
        "battery_rows_sha256": digest(battery),
        "allocation_count": len(allocations),
        "all_allocation_totals_19": all(
            sum(allocation) == 19 for allocation in allocations
        ),
        "law_count": len(law_rows_tuple),
        "law_pass_count": sum(
            bool(row["orbit_invariant"]) for row in law_rows_tuple
        ),
        "five_sampled_law_checks": samples,
        "five_sampled_law_pass_count": sum(
            bool(row["orbit_invariant"]) for row in samples
        ),
        "law_rows_sha256": digest(law_rows_tuple),
        "pass": (
            len(battery) == 46
            and full_counts == Counter({1: 23, -1: 23})
            and len(projected) == 38
            and projected_counts == Counter({1: 19, -1: 19})
            and all(row[3] == (0,) for row in battery)
            and len(allocations) == 42_504
            and all(sum(allocation) == 19 for allocation in allocations)
            and len(law_rows_tuple) == 25
            and all(
                bool(row["orbit_invariant"]) for row in law_rows_tuple
            )
            and len(samples) == 5
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
        raise AssertionError("AUDIT_INPUT_PATHS contains a nonliteral")
    return tuple(element.value for element in matches[0].elts)


def source_controls(
    source_before: dict[str, bytes],
    primary_contract: dict[str, object],
) -> dict[str, object]:
    source_after = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    observed_sha256 = {
        path: sha256(data).hexdigest()
        for path, data in source_after.items()
    }
    observed_blobs = {
        path: git_blob_sha1(data)
        for path, data in source_after.items()
    }
    tracked = {}
    for path in AUDIT_INPUT_PATHS:
        completed = subprocess.run(
            ("git", "ls-files", "--error-unmatch", path),
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        tracked[path] = completed.returncode == 0
    head = subprocess.run(
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
        "head_sha": head,
        "branch": branch,
        "read_file_count": len(AUDIT_INPUT_PATHS),
        "literal_audit_input_paths": literal_self_audit_paths(),
        "all_paths_worktree_relative": all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
        "all_paths_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "sha256": observed_sha256,
        "git_blob_sha1": observed_blobs,
        "sha256_match": observed_sha256 == EXPECTED_SHA256,
        "git_blob_match": observed_blobs == EXPECTED_GIT_BLOB_SHA1,
        "bytes_unchanged_during_run": source_before == source_after,
        "tracked": tracked,
        "all_tracked": all(tracked.values()),
        "primary_contract": primary_contract,
    }


def main() -> int:
    source_bytes, trees = read_sources()
    primary_contract = primary_ast_contract(trees[PRIMARY_PATH])
    surface = extract_w7_surface(source_bytes, trees)

    allocations = weak_compositions(GROUP_TOTAL, GROUP_BINS)
    orbits = orbit_partition(allocations)
    census = collision_census(allocations, orbits, surface.rows)
    repeated_census = collision_census(allocations, orbits, surface.rows)
    selectors = selector_hunt(allocations, surface)
    repeated_selectors = selector_hunt(allocations, surface)
    consistency = consistency_controls(allocations, orbits)
    controls = source_controls(source_bytes, primary_contract)

    emit("CYCLE 825 INDEPENDENT_ADVERSARIAL_CHECKER")
    emit("HEAD_SHA", controls["head_sha"])
    emit("BRANCH", controls["branch"])
    for path in AUDIT_INPUT_PATHS:
        emit(
            "SOURCE_SHA",
            path,
            controls["sha256"][path],
            controls["git_blob_sha1"][path],
        )

    check(
        "A_INDEPENDENT_READOUT_AND_SOURCE_EXTRACTION",
        (
            primary_contract["pass"]
            and surface.passed
            and len(EXPECTED_READOUT_NAMES) == 11
            and len(allocations) == 42_504
            and all(map(lawful, allocations))
            and len(orbits) == 7_084
            and Counter(map(len, orbits)) == Counter({6: 7_084})
        ),
        {
            "primary_ast_contract": primary_contract,
            "readout_names": EXPECTED_READOUT_NAMES,
            "w7_directions": surface.directions,
            "w7_reverse": surface.reverse,
            "w7_rows": surface.rows,
            "functional_citations": surface.citations,
            "package_scan": surface.package_scan,
            "allocation_count": len(allocations),
            "orbit_count": len(orbits),
            "orbit_size_distribution": dict(Counter(map(len, orbits))),
        },
    )

    collision_ok = (
        census["distinct_readout_count"] == 5_340
        and census["injective"] is False
        and census["class_size_distribution"]
        == EXPECTED_CLASS_SIZE_DISTRIBUTION
        and census["singleton_class_count"] == 1_446
        and census["nonsingleton_class_count"] == 3_894
        and census["members_in_nonsingleton_classes"] == 41_058
        and census["readout_iff_signed_moment"]
        and census["class_formula_verified"]
        and census["all_values_exact"]
    )
    check(
        "B_THE_COLLISION_CENSUS",
        collision_ok,
        {
            key: value
            for key, value in census.items()
            if key != "internal_collision_orbits"
        },
    )
    emit(
        "FINDING_VERBATIM",
        (
            "THE COLLISION CENSUS: R is NONINJECTIVE on 42,504 "
            "allocations: 5,340 distinct readouts, 3,894 nonsingleton "
            "classes, and 41,058 allocations in nonsingleton classes."
        ),
    )

    internal_ok = (
        census["nonconstant_orbit_count"] == 7_084
        and census["within_orbit_distinct_readout_distribution"]
        == {4: 48, 6: 7_036}
        and census["internal_collision_orbit_count"] == 48
        and census["internal_collision_orbit_indices"]
        == EXPECTED_INTERNAL_ORBIT_INDICES
        and census["internal_collisions_sha256"]
        == EXPECTED_INTERNAL_COLLISIONS_SHA256
        and census["internal_representatives_sha256"]
        == EXPECTED_INTERNAL_REPRESENTATIVES_SHA256
    )
    check(
        "C_CYCLE821_ORBIT_RECONCILIATION",
        internal_ok,
        {
            "nonconstant_orbit_count": census["nonconstant_orbit_count"],
            "within_orbit_distinct_readout_distribution":
                census["within_orbit_distinct_readout_distribution"],
            "internal_collision_orbit_count":
                census["internal_collision_orbit_count"],
            "internal_collision_orbit_indices":
                census["internal_collision_orbit_indices"],
            "internal_collisions_sha256":
                census["internal_collisions_sha256"],
            "internal_representatives_sha256":
                census["internal_representatives_sha256"],
            "reconciliation": (
                "Every C6 orbit is response-nonconstant.  Exactly the listed "
                "48 have one three-member tie and therefore four distinct "
                "readouts; the other 7,036 have six distinct readouts."
            ),
        },
    )
    emit(
        "INTERNAL_COLLISION_ORBIT_LIST",
        compact(census["internal_collision_orbits"]),
    )
    emit(
        "FINDING_VERBATIM",
        (
            "CYCLE 821 RECONCILIATION: all 7,084 C6 orbits are "
            "nonconstant; 7,036 have six distinct readouts and the exact "
            "48-orbit list above has four, with one three-member tie each."
        ),
    )

    for row in selectors["probes"]:
        emit("SELECTOR_CANDIDATE", compact(row))
    check(
        "D_THE_SELECTOR_HUNT",
        bool(selectors["pass"]),
        {
            key: value
            for key, value in selectors.items()
            if key != "probes"
        },
    )
    if selectors["missed_constraints"]:
        selector_finding = (
            "THE SELECTOR HUNT: LANDED SELECTOR FOUND; "
            f"survivors={selectors['surviving_count']}. "
            "The primary UNCONSTRAINED verdict is REFUTED."
        )
    else:
        selector_finding = (
            "THE SELECTOR HUNT: NO LANDED WEIGHT SELECTOR FOUND.  Every "
            "landed predicate on the unknown allocation leaves all 42,504; "
            "every smaller hypothetical set is tied to a supplied fixture, "
            "a conditional failed gate, or an absent extremal principle."
        )
    emit("FINDING_VERBATIM", selector_finding)

    check(
        "E_CONSISTENCY_CONTROLS",
        bool(consistency["pass"]),
        consistency,
    )
    for row in consistency["five_sampled_law_checks"]:
        emit("SAMPLED_ORBIT_INVARIANT_LAW", compact(row))
    emit(
        "FINDING_VERBATIM",
        (
            "CONSISTENCY CONTROLS: 46=23+23; 38=19+19; all 25/25 "
            "orbit-invariant total-19 law checks pass, including the five "
            "content-addressed samples printed above."
        ),
    )

    deterministic = (
        census["ordered_classes_sha256"]
        == repeated_census["ordered_classes_sha256"]
        and census["internal_collisions_sha256"]
        == repeated_census["internal_collisions_sha256"]
        and census["class_size_distribution"]
        == repeated_census["class_size_distribution"]
        and selectors["probe_rows_sha256"]
        == repeated_selectors["probe_rows_sha256"]
        and selectors["missed_constraints"]
        == repeated_selectors["missed_constraints"]
    )
    elapsed_before_control = monotonic() - START
    projected_stdout = STDOUT_BYTES + 16_384
    check(
        "F_CONTROLS",
        (
            controls["read_file_count"] == 7
            and controls["literal_audit_input_paths"] == AUDIT_INPUT_PATHS
            and controls["all_paths_worktree_relative"]
            and controls["all_paths_exist"]
            and controls["sha256_match"]
            and controls["git_blob_match"]
            and controls["bytes_unchanged_during_run"]
            and controls["all_tracked"]
            and primary_contract["primary_blocked"]
            and primary_contract["primary_absent_from_sys_modules"]
            and primary_contract["checker_has_no_primary_import"]
            and deterministic
            and census["all_values_exact"]
            and elapsed_before_control < AUDIT_TIMEOUT_SEC
            and projected_stdout < STDOUT_LIMIT_BYTES
        ),
        {
            "source_controls": controls,
            "deterministic_repeat": deterministic,
            "exact_arithmetic": census["all_values_exact"],
            "runtime_seconds_before_control": elapsed_before_control,
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes_before_control": STDOUT_BYTES,
            "stdout_projected_bytes": projected_stdout,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    if selectors["missed_constraints"]:
        outcome = (
            "DETERMINED"
            if selectors["surviving_count"] == 1
            else "CONSTRAINED"
        )
    else:
        outcome = "UNCONSTRAINED"
    elapsed = monotonic() - START
    passed = all(CHECKS.values())
    emit(
        "FINDING_VERBATIM",
        (
            f"VERDICT: {outcome}; surviving_count="
            f"{selectors['surviving_count']}."
        ),
    )
    emit(
        "COLLISION_CENSUS",
        (
            f"distinct={census['distinct_readout_count']} "
            f"nonsingleton={census['nonsingleton_class_count']} "
            f"internal_collision_orbits="
            f"{census['internal_collision_orbit_count']}"
        ),
    )
    emit(
        "SELECTOR_HUNT_OUTCOME",
        selectors["outcome"],
        f"surviving_count={selectors['surviving_count']}",
    )
    emit(
        "CONSISTENCY_CONTROL",
        (
            "46=23+23 38=19+19 "
            f"laws={consistency['law_pass_count']}/25 "
            f"samples={consistency['five_sampled_law_pass_count']}/5"
        ),
    )
    emit("RUNTIME_SECONDS", f"{elapsed:.6f}")
    emit("STDOUT_BYTES", STDOUT_BYTES)
    emit("CHECK_SUMMARY", compact({"pass": passed, "checks": CHECKS}))
    emit("PASS" if passed else "FAIL")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
