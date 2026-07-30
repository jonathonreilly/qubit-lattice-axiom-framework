#!/usr/bin/env python3
"""Cycle 774 independent adversarial check of the empty-interference theorem.

This checker deliberately does not import or execute the Cycle 774, 771, or
768 primaries.  It scans the landed Cycle-320 vertex matrix exhaustively and
reconstructs coherent cross terms from exact rational representations of the
matrix's stored complex scalars.
"""

AUDIT_TIMEOUT_SEC = 1500
OUTPUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
)
PRIMARY_TEXT_PATHS = (
    "scripts/frontier_cycle774_interference_sector_2026_07_28.py",
    "scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
)
BLOCKLIST = (
    "frontier_cycle774_interference_sector_2026_07_28",
    "frontier_cycle771_prediction_verification_2026_07_28",
    "frontier_cycle768_response_law_candidate_2026_07_28",
)
EXPECTED_U320_SHA256 = (
    "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706"
)

# Gaussian integers are written as (real, imaginary).  The first six pairs are
# the full primary family; the final four are independent adversarial probes.
DECLARED_COEFFICIENT_PAIRS = (
    ("1,1", ((1, 0), (1, 0))),
    ("1,-1", ((1, 0), (-1, 0))),
    ("1,i", ((1, 0), (0, 1))),
    ("1,-i", ((1, 0), (0, -1))),
    ("2,1", ((2, 0), (1, 0))),
    ("1,2", ((1, 0), (2, 0))),
)
EXTRA_COEFFICIENT_PAIRS = (
    ("3,5", ((3, 0), (5, 0))),
    ("1+i,1", ((1, 1), (1, 0))),
    ("2+i,1-i", ((2, 1), (1, -1))),
    ("5,-3", ((5, 0), (-3, 0))),
)
THREE_CHANNEL_COEFFICIENTS = (
    ("1,1,1", ((1, 0), (1, 0), (1, 0))),
    ("1,i,-1", ((1, 0), (0, 1), (-1, 0))),
)

import ast
from fractions import Fraction
import hashlib
from itertools import combinations
import json
from pathlib import Path
import sys
import time
from typing import Iterable

import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320


ROOT = Path(__file__).resolve().parents[1]
QComplex = tuple[Fraction, Fraction]
Vector = tuple[Fraction, ...]
ResponseRow = tuple[Vector, Vector, Vector]
ZERO_COMPLEX: QComplex = (Fraction(), Fraction())


def jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return value.numerator
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def render_json(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=jsonable,
    )


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def qcomplex_from_pair(value: tuple[int, int]) -> QComplex:
    return Fraction(value[0]), Fraction(value[1])


def qcomplex_from_stored_scalar(value: object) -> QComplex:
    """Represent the binary64 complex matrix entry exactly, without tolerance."""
    scalar = complex(value)
    return Fraction.from_float(scalar.real), Fraction.from_float(scalar.imag)


def qadd(left: QComplex, right: QComplex) -> QComplex:
    return left[0] + right[0], left[1] + right[1]


def qmul(left: QComplex, right: QComplex) -> QComplex:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def qconjugate(value: QComplex) -> QComplex:
    return value[0], -value[1]


def qabs2(value: QComplex) -> Fraction:
    return value[0] * value[0] + value[1] * value[1]


def qsum(values: Iterable[QComplex]) -> QComplex:
    total = ZERO_COMPLEX
    for value in values:
        total = qadd(total, value)
    return total


def direction(index: int) -> Vector:
    return tuple(Fraction(int(value)) for value in U320.c210.DIRECTIONS[index])


def add_response_rows(rows: Iterable[ResponseRow]) -> ResponseRow:
    materialized = tuple(rows)
    if not materialized:
        raise ValueError("cannot add zero response rows")
    return tuple(
        tuple(
            sum(
                (row[component][axis] for row in materialized),
                start=Fraction(),
            )
            for axis in range(len(materialized[0][component]))
        )
        for component in range(len(materialized[0]))
    )  # type: ignore[return-value]


def decode_branch(flat: int, direction_count: int) -> tuple[int, int, int]:
    return (
        flat // (direction_count * direction_count),
        (flat // direction_count) % direction_count,
        flat % direction_count,
    )


def exact_vertex_matrix(vertex: object) -> tuple[tuple[QComplex, ...], ...]:
    row_count, column_count = (int(value) for value in vertex.shape)
    return tuple(
        tuple(
            qcomplex_from_stored_scalar(vertex[row, column])
            for column in range(column_count)
        )
        for row in range(row_count)
    )


def matrix_exhaustion(
    matrix: tuple[tuple[QComplex, ...], ...],
    direction_count: int,
) -> dict[str, object]:
    """Scan every matrix entry, then invert branch reachability by source."""
    row_count = len(matrix)
    column_count = len(matrix[0])
    nonzero_coordinates = []
    source_branch_cells = []
    branch_sources: dict[tuple[int, int, int], list[int]] = {}
    for row in range(row_count):
        for column in range(column_count):
            if matrix[row][column] != ZERO_COMPLEX:
                nonzero_coordinates.append((row, column))

    for source in range(direction_count):
        cells = []
        for flat in range(direction_count**3):
            row = direction_count + flat
            if matrix[row][source] != ZERO_COMPLEX:
                cell = decode_branch(flat, direction_count)
                cells.append(cell)
                branch_sources.setdefault(cell, []).append(source)
        source_branch_cells.append(
            {
                "branch_cells": tuple(cells),
                "source_channel": source,
            }
        )

    shared = tuple(
        {
            "branch_cell": cell,
            "source_channels": tuple(sources),
        }
        for cell, sources in sorted(branch_sources.items())
        if len(sources) > 1
    )
    expected = tuple(
        (int(U320.REVERSE[source]), source, source)
        for source in range(direction_count)
    )
    observed = tuple(
        tuple(row["branch_cells"]) for row in source_branch_cells
    )
    expected_singletons = tuple((cell,) for cell in expected)
    coordinates_blob = render_json(tuple(nonzero_coordinates)).encode("utf-8")
    return {
        "branch_target_formula_matches":
            observed == expected_singletons,
        "every_matrix_entry_examined":
            row_count * column_count
            == sum(len(row) for row in matrix),
        "matrix_entry_count": row_count * column_count,
        "matrix_nonzero_coordinates": tuple(nonzero_coordinates),
        "matrix_nonzero_coordinates_sha256": sha256_bytes(coordinates_blob),
        "matrix_nonzero_entry_count": len(nonzero_coordinates),
        "matrix_shape": (row_count, column_count),
        "shared_branch_cells": shared,
        "source_branch_cells": tuple(source_branch_cells),
        "structural_claim": (
            "REFUTED_SHARED_BRANCH_CELL"
            if shared
            else (
                "SURVIVED_MATRIX_EXHAUSTION"
                if observed == expected_singletons
                else "REFUTED_BRANCH_TARGET_FORMULA"
            )
        ),
    }


def coherent_cross_terms(
    matrix: tuple[tuple[QComplex, ...], ...],
    channels: tuple[int, ...],
    coefficients: tuple[QComplex, ...],
    direction_count: int,
) -> dict[str, object]:
    """Construct one coherent input and compute cellwise products exactly."""
    if len(channels) != len(coefficients) or len(set(channels)) != len(channels):
        raise ValueError("coherent input channels/coefficients are malformed")
    norm_squared = sum(
        (qabs2(coefficient) for coefficient in coefficients),
        start=Fraction(),
    )
    if not norm_squared:
        raise ValueError("coherent input has zero norm")

    nonzero_cross_terms = []
    support = []
    exact_identity_failures = []
    for flat in range(direction_count**3):
        row = direction_count + flat
        contributions = tuple(
            qmul(matrix[row][channel], coefficient)
            for channel, coefficient in zip(channels, coefficients)
        )
        if any(value != ZERO_COMPLEX for value in contributions):
            support.append(decode_branch(flat, direction_count))
        coherent_probability = qabs2(qsum(contributions)) / norm_squared
        mixture_probability = (
            sum((qabs2(value) for value in contributions), start=Fraction())
            / norm_squared
        )
        cross_term = coherent_probability - mixture_probability
        pairwise_cross = sum(
            (
                2
                * qmul(contributions[left], qconjugate(contributions[right]))[0]
                / norm_squared
                for left, right in combinations(range(len(contributions)), 2)
            ),
            start=Fraction(),
        )
        if cross_term != pairwise_cross:
            exact_identity_failures.append(
                {
                    "branch_cell": decode_branch(flat, direction_count),
                    "difference_form": cross_term,
                    "pairwise_product_form": pairwise_cross,
                }
            )
        if cross_term:
            nonzero_cross_terms.append(
                {
                    "branch_cell": decode_branch(flat, direction_count),
                    "cross_term": cross_term,
                    "pairwise_amplitude_product_sum": pairwise_cross,
                }
            )

    return {
        "channels": channels,
        "input_coefficients": coefficients,
        "input_norm_squared": norm_squared,
        "nonzero_cross_terms": tuple(nonzero_cross_terms),
        "pairwise_identity_failures": tuple(exact_identity_failures),
        "reachable_branch_cells": tuple(support),
    }


def conditional_single_channel_row(
    matrix: tuple[tuple[QComplex, ...], ...],
    source: int,
    direction_count: int,
) -> dict[str, object]:
    """Reproduce a defining row by exact branch-probability bookkeeping."""
    numerators = [
        [Fraction() for _axis in range(3)]
        for _component in range(3)
    ]
    weight = Fraction()
    branch_cells = []
    source_vector = direction(source)
    for flat in range(direction_count**3):
        amplitude = matrix[direction_count + flat][source]
        probability = qabs2(amplitude)
        if not probability:
            continue
        cell = decode_branch(flat, direction_count)
        branch_cells.append(cell)
        matter, mediator, auxiliary = cell
        vectors = (
            tuple(
                final - initial
                for final, initial in zip(direction(matter), source_vector)
            ),
            direction(mediator),
            direction(auxiliary),
        )
        weight += probability
        for component, vector in enumerate(vectors):
            for axis, value in enumerate(vector):
                numerators[component][axis] += probability * value
    if not weight:
        raise ValueError(f"source channel {source} has no branch transfer")
    row: ResponseRow = tuple(
        tuple(value / weight for value in component)
        for component in numerators
    )  # type: ignore[assignment]
    reverse_vector = direction(int(U320.REVERSE[source]))
    expected: ResponseRow = (
        tuple(
            final - initial
            for final, initial in zip(reverse_vector, source_vector)
        ),
        source_vector,
        source_vector,
    )
    return {
        "branch_cells": tuple(branch_cells),
        "branch_weight_exact_stored_matrix": weight,
        "channel": source,
        "expected_defining_row": expected,
        "match": row == expected,
        "recounted_row": row,
    }


def two_channel_census(
    matrix: tuple[tuple[QComplex, ...], ...],
    direction_count: int,
) -> dict[str, object]:
    family = DECLARED_COEFFICIENT_PAIRS + EXTRA_COEFFICIENT_PAIRS
    members = []
    counterexamples = []
    for left in range(direction_count):
        for right in range(left + 1, direction_count):
            for label, raw_coefficients in family:
                coefficients = tuple(
                    qcomplex_from_pair(value) for value in raw_coefficients
                )
                row = coherent_cross_terms(
                    matrix,
                    (left, right),
                    coefficients,
                    direction_count,
                )
                member = {
                    "channels": (left, right),
                    "coefficient_pair": label,
                    "input_norm_squared": row["input_norm_squared"],
                    "nonzero_cross_terms": row["nonzero_cross_terms"],
                    "pairwise_identity_failures":
                        row["pairwise_identity_failures"],
                    "reachable_branch_cells":
                        row["reachable_branch_cells"],
                }
                members.append(member)
                if row["nonzero_cross_terms"]:
                    counterexamples.append(member)
    declared_count = (
        len(tuple(combinations(range(direction_count), 2)))
        * len(DECLARED_COEFFICIENT_PAIRS)
    )
    extra_count = (
        len(tuple(combinations(range(direction_count), 2)))
        * len(EXTRA_COEFFICIENT_PAIRS)
    )
    return {
        "all_pairwise_product_identities_exact":
            all(not row["pairwise_identity_failures"] for row in members),
        "channel_pair_count":
            len(tuple(combinations(range(direction_count), 2))),
        "counterexamples": tuple(counterexamples),
        "declared_coefficient_pairs":
            tuple(label for label, _values in DECLARED_COEFFICIENT_PAIRS),
        "declared_member_count": declared_count,
        "extra_coefficient_pairs":
            tuple(label for label, _values in EXTRA_COEFFICIENT_PAIRS),
        "extra_member_count": extra_count,
        "member_count": len(members),
        "members": tuple(members),
        "theorem_on_recounted_family": (
            "REFUTED_NONZERO_CROSS_TERM"
            if counterexamples
            else "NO_COUNTEREXAMPLE_EXACTLY_ZERO"
        ),
    }


def three_channel_probe(
    matrix: tuple[tuple[QComplex, ...], ...],
    direction_count: int,
) -> dict[str, object]:
    members = []
    counterexamples = []
    for first in range(direction_count):
        for second in range(first + 1, direction_count):
            for third in range(second + 1, direction_count):
                channels = (first, second, third)
                for label, raw_coefficients in THREE_CHANNEL_COEFFICIENTS:
                    coefficients = tuple(
                        qcomplex_from_pair(value)
                        for value in raw_coefficients
                    )
                    row = coherent_cross_terms(
                        matrix,
                        channels,
                        coefficients,
                        direction_count,
                    )
                    member = {
                        "channels": channels,
                        "coefficient_triple": label,
                        "input_norm_squared": row["input_norm_squared"],
                        "nonzero_cross_terms": row["nonzero_cross_terms"],
                        "pairwise_identity_failures":
                            row["pairwise_identity_failures"],
                        "reachable_branch_cells":
                            row["reachable_branch_cells"],
                    }
                    members.append(member)
                    if row["nonzero_cross_terms"]:
                        counterexamples.append(member)
    return {
        "all_pairwise_product_identities_exact":
            all(not row["pairwise_identity_failures"] for row in members),
        "channel_triple_count":
            len(tuple(combinations(range(direction_count), 3))),
        "coefficient_triples":
            tuple(label for label, _values in THREE_CHANNEL_COEFFICIENTS),
        "counterexamples": tuple(counterexamples),
        "member_count": len(members),
        "members": tuple(members),
        "structural_generality": (
            "REFUTED_THREE_CHANNEL_CROSS_TERM"
            if counterexamples
            else "NO_COUNTEREXAMPLE_EXACTLY_ZERO"
        ),
    }


def literal_assignment(tree: ast.Module, name: str) -> object:
    assignments = [
        node
        for node in tree.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        and (
            any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
            if isinstance(node, ast.Assign)
            else isinstance(node.target, ast.Name) and node.target.id == name
        )
    ]
    if len(assignments) != 1:
        raise ValueError(f"expected one top-level assignment to {name}")
    return ast.literal_eval(assignments[0].value)


def root_name(node: ast.AST) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def primary_vertex_identity_guard(
    primary_source: str,
    u320_digest: str,
) -> dict[str, object]:
    tree = ast.parse(primary_source, filename=PRIMARY_TEXT_PATHS[0])
    import_rows = tuple(
        {
            "alias": alias.asname,
            "module": alias.name,
        }
        for node in tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.asname == "U320"
    )
    expected_module = (
        "unit_weight_carried_link_recoil_cycle320_2026_07_18"
    )
    expected_calls = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not (
            isinstance(node.func, ast.Attribute)
            and node.func.attr == "link_recoil_vertex"
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "U320"
        ):
            continue
        exact_argument = (
            len(node.args) == 1
            and not node.keywords
            and isinstance(node.args[0], ast.Attribute)
            and node.args[0].attr == "ANGLE"
            and isinstance(node.args[0].value, ast.Name)
            and node.args[0].value.id == "U320"
        )
        expected_calls.append(
            {
                "argument_is_U320_ANGLE": exact_argument,
                "line": node.lineno,
            }
        )

    local_constructors = tuple(
        {
            "line": node.lineno,
            "name": node.name,
        }
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == "link_recoil_vertex"
    )
    module_mutations = []
    vertex_mutations = []
    allowed_vertex_binding_lines = {
        row["line"] for row in expected_calls
    }
    for node in ast.walk(tree):
        targets: list[ast.AST] = []
        if isinstance(node, ast.Assign):
            targets.extend(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            targets.append(node.target)
        for target in targets:
            if root_name(target) == "U320":
                module_mutations.append(
                    {"kind": type(node).__name__, "line": node.lineno}
                )
            target_nodes = (
                tuple(target.elts)
                if isinstance(target, (ast.Tuple, ast.List))
                else (target,)
            )
            for target_node in target_nodes:
                if root_name(target_node) != "vertex":
                    continue
                if (
                    isinstance(target_node, ast.Name)
                    and node.lineno in allowed_vertex_binding_lines
                    and isinstance(node, ast.Assign)
                    and isinstance(node.value, ast.Call)
                ):
                    continue
                vertex_mutations.append(
                    {"kind": type(node).__name__, "line": node.lineno}
                )
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"setattr", "delattr"}
            and node.args
            and root_name(node.args[0]) in {"U320", "vertex"}
        ):
            target = root_name(node.args[0])
            row = {"kind": node.func.id, "line": node.lineno}
            if target == "U320":
                module_mutations.append(row)
            else:
                vertex_mutations.append(row)

    call_contract = (
        len(expected_calls) == 1
        and bool(expected_calls[0]["argument_is_U320_ANGLE"])
    )
    return {
        "ast_identity_contract": (
            len(import_rows) == 1
            and import_rows[0]["module"] == expected_module
            and call_contract
            and not local_constructors
            and not module_mutations
            and not vertex_mutations
        ),
        "expected_u320_sha256": EXPECTED_U320_SHA256,
        "landed_u320_sha256": u320_digest,
        "local_vertex_constructors": local_constructors,
        "module_import": import_rows,
        "module_mutations": tuple(module_mutations),
        "primary_vertex_calls": tuple(expected_calls),
        "sha_anchor_matches": u320_digest == EXPECTED_U320_SHA256,
        "vertex_mutations": tuple(vertex_mutations),
    }


def cycle771_direct_pair(source: str) -> tuple[int, int]:
    tree = ast.parse(source, filename=PRIMARY_TEXT_PATHS[1])
    value = literal_assignment(tree, "DIRECT_CHANNEL_PAIR")
    if not (
        isinstance(value, tuple)
        and len(value) == 2
        and all(isinstance(item, int) for item in value)
    ):
        raise ValueError("Cycle-771 DIRECT_CHANNEL_PAIR is not two integers")
    return value


def control_recounts(
    matrix: tuple[tuple[QComplex, ...], ...],
    direction_count: int,
    direct_pair: tuple[int, int],
) -> dict[str, object]:
    singles = tuple(
        conditional_single_channel_row(matrix, source, direction_count)
        for source in range(direction_count)
    )
    mixtures = []
    for left in range(direction_count):
        for right in range(left + 1, direction_count):
            actual = add_response_rows(
                (
                    singles[left]["recounted_row"],
                    singles[right]["recounted_row"],
                )  # type: ignore[arg-type]
            )
            expected = add_response_rows(
                (
                    singles[left]["expected_defining_row"],
                    singles[right]["expected_defining_row"],
                )  # type: ignore[arg-type]
            )
            left_cells = set(singles[left]["branch_cells"])  # type: ignore[arg-type]
            right_cells = set(singles[right]["branch_cells"])  # type: ignore[arg-type]
            mixtures.append(
                {
                    "branch_support_overlap":
                        tuple(sorted(left_cells & right_cells)),
                    "channels": (left, right),
                    "expected_sum": expected,
                    "match": actual == expected,
                    "recounted_sum": actual,
                }
            )
    target = next(
        row for row in mixtures if row["channels"] == direct_pair
    )
    return {
        "all_15_mixture_baselines_block_additive":
            len(mixtures) == 15
            and all(row["match"] for row in mixtures)
            and all(not row["branch_support_overlap"] for row in mixtures),
        "cycle771_direct_pair": direct_pair,
        "cycle771_mixture_block_additivity": target,
        "mixture_baseline_count": len(mixtures),
        "mixture_baselines": tuple(mixtures),
        "single_channel_defining_rows": singles,
        "single_channel_rows_all_match":
            all(row["match"] for row in singles),
    }


def refutation_sensitivity_control(
    matrix: tuple[tuple[QComplex, ...], ...],
    direction_count: int,
) -> dict[str, object]:
    """Inject one in-memory overlap and demand a loud exact counterexample."""
    source = 0
    intruder = 1
    donor_flat = next(
        flat
        for flat in range(direction_count**3)
        if matrix[direction_count + flat][source] != ZERO_COMPLEX
    )
    donor_row = direction_count + donor_flat
    synthetic = [list(row) for row in matrix]
    synthetic[donor_row][intruder] = matrix[donor_row][source]
    synthetic_matrix = tuple(tuple(row) for row in synthetic)
    structure = matrix_exhaustion(synthetic_matrix, direction_count)
    coherent = coherent_cross_terms(
        synthetic_matrix,
        (source, intruder),
        (qcomplex_from_pair((1, 0)), qcomplex_from_pair((1, 0))),
        direction_count,
    )
    expected_cell = decode_branch(donor_flat, direction_count)
    expected_shared = {
        "branch_cell": expected_cell,
        "source_channels": (source, intruder),
    }
    return {
        "detected_nonzero_cross_terms": coherent["nonzero_cross_terms"],
        "detected_shared_branch_cells": structure["shared_branch_cells"],
        "expected_shared_branch_cell": expected_shared,
        "landed_matrix_modified": False,
        "passed":
            expected_shared in structure["shared_branch_cells"]
            and bool(coherent["nonzero_cross_terms"])
            and not coherent["pairwise_identity_failures"],
        "synthetic_change": (
            "in-memory copy only: source 1 was pointed at source 0's "
            f"branch cell {expected_cell}"
        ),
    }


def certificate_line(
    name: str,
    passed: bool,
    finding: object,
) -> str:
    return (
        ("PASS " if passed else "FAIL ")
        + name
        + " :: "
        + render_json(finding)
    )


def headline_finding(
    census: dict[str, object],
    structure: dict[str, object],
    triples: dict[str, object],
) -> tuple[str, dict[str, object]]:
    two_counterexamples = census["counterexamples"]
    shared_cells = structure["shared_branch_cells"]
    triple_counterexamples = triples["counterexamples"]
    formula_failed = not structure["branch_target_formula_matches"]
    refuted = bool(
        two_counterexamples
        or shared_cells
        or triple_counterexamples
        or formula_failed
    )
    finding = {
        "branch_target_formula_failed": formula_failed,
        "shared_branch_cells": shared_cells,
        "three_channel_counterexamples": triple_counterexamples,
        "two_channel_counterexamples": two_counterexamples,
    }
    if refuted:
        return "HEADLINE *** EMPTY-INTERFERENCE THEOREM REFUTED ***", finding
    return (
        "HEADLINE NO COUNTEREXAMPLE FOUND IN THE REQUIRED ADVERSARIAL ATTACKS",
        finding,
    )


def main() -> int:
    started = time.monotonic()
    blocklist_before = {
        name: name in sys.modules for name in BLOCKLIST
    }
    landed_before = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    primaries_before = {
        path: (ROOT / path).read_bytes() for path in PRIMARY_TEXT_PATHS
    }
    primary_sources = {
        path: data.decode("utf-8")
        for path, data in primaries_before.items()
    }
    primary_ast_parsed = {
        path: isinstance(
            ast.parse(source, filename=path),
            ast.Module,
        )
        for path, source in primary_sources.items()
    }
    u320_sha_before = sha256_bytes(landed_before[AUDIT_INPUT_PATHS[0]])
    primary_shas_before = {
        path: sha256_bytes(data) for path, data in primaries_before.items()
    }
    direct_pair = cycle771_direct_pair(
        primary_sources[PRIMARY_TEXT_PATHS[1]]
    )
    identity = primary_vertex_identity_guard(
        primary_sources[PRIMARY_TEXT_PATHS[0]],
        u320_sha_before,
    )

    _exchange, vertex, _charge, _momenta = U320.link_recoil_vertex(U320.ANGLE)
    direction_count = len(U320.c210.DIRECTIONS)
    matrix = exact_vertex_matrix(vertex)
    structure = matrix_exhaustion(matrix, direction_count)
    census = two_channel_census(matrix, direction_count)
    triples = three_channel_probe(matrix, direction_count)
    controls = control_recounts(matrix, direction_count, direct_pair)
    sensitivity = refutation_sensitivity_control(matrix, direction_count)

    # A genuinely independent second construction catches hidden ordering or
    # statefulness in the landed vertex and in every checker loop.
    _exchange_2, vertex_2, _charge_2, _momenta_2 = (
        U320.link_recoil_vertex(U320.ANGLE)
    )
    matrix_2 = exact_vertex_matrix(vertex_2)
    structure_2 = matrix_exhaustion(matrix_2, direction_count)
    census_2 = two_channel_census(matrix_2, direction_count)
    triples_2 = three_channel_probe(matrix_2, direction_count)
    controls_2 = control_recounts(matrix_2, direction_count, direct_pair)
    sensitivity_2 = refutation_sensitivity_control(
        matrix_2,
        direction_count,
    )
    deterministic = (
        matrix == matrix_2
        and structure == structure_2
        and census == census_2
        and triples == triples_2
        and controls == controls_2
        and sensitivity == sensitivity_2
    )

    landed_after = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    primaries_after = {
        path: (ROOT / path).read_bytes() for path in PRIMARY_TEXT_PATHS
    }
    u320_sha_after = sha256_bytes(landed_after[AUDIT_INPUT_PATHS[0]])
    primary_shas_after = {
        path: sha256_bytes(data) for path, data in primaries_after.items()
    }
    blocklist_after = {
        name: name in sys.modules for name in BLOCKLIST
    }
    imported_path = Path(U320.__file__).resolve()
    declared_import_path = (ROOT / AUDIT_INPUT_PATHS[0]).resolve()

    pair_count = len(tuple(combinations(range(direction_count), 2)))
    triple_count = len(tuple(combinations(range(direction_count), 3)))
    census_execution_passed = (
        census["channel_pair_count"] == pair_count
        and census["declared_member_count"]
        == pair_count * len(DECLARED_COEFFICIENT_PAIRS)
        and census["extra_member_count"]
        == pair_count * len(EXTRA_COEFFICIENT_PAIRS)
        and census["member_count"]
        == pair_count
        * (
            len(DECLARED_COEFFICIENT_PAIRS)
            + len(EXTRA_COEFFICIENT_PAIRS)
        )
        and census["all_pairwise_product_identities_exact"]
    )
    structural_execution_passed = (
        structure["matrix_shape"] == (222, 222)
        and structure["matrix_entry_count"] == 222 * 222
        and structure["every_matrix_entry_examined"]
        and len(structure["source_branch_cells"]) == direction_count
    )
    triple_execution_passed = (
        triples["channel_triple_count"] == triple_count
        and triples["member_count"]
        == triple_count * len(THREE_CHANNEL_COEFFICIENTS)
        and triples["all_pairwise_product_identities_exact"]
    )
    identity_execution_passed = (
        identity["sha_anchor_matches"]
        and identity["ast_identity_contract"]
        and landed_before == landed_after
        and primaries_before == primaries_after
        and primary_shas_before == primary_shas_after
        and all(primary_ast_parsed.values())
        and imported_path == declared_import_path
        and not any(blocklist_before.values())
        and not any(blocklist_after.values())
        and AUDIT_INPUT_PATHS
        == (
            "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
        )
    )
    controls_execution_passed = (
        controls["single_channel_rows_all_match"]
        and controls["all_15_mixture_baselines_block_additive"]
        and controls["mixture_baseline_count"] == pair_count
        and controls["cycle771_mixture_block_additivity"]["match"]
        and not controls["cycle771_mixture_block_additivity"][
            "branch_support_overlap"
        ]
        and sensitivity["passed"]
        and deterministic
    )

    headline, headline_detail = headline_finding(
        census,
        structure,
        triples,
    )
    elapsed = time.monotonic() - started
    certificate_specs: list[tuple[str, bool, object]] = [
        (
            "CERTIFICATE 1 CENSUS RECOUNT WITH EXTRA COEFFICIENT PAIRS",
            bool(census_execution_passed),
            {
                "attack_execution": "COMPLETE",
                "channel_pair_count": census["channel_pair_count"],
                "counterexamples": census["counterexamples"],
                "declared_coefficient_pairs":
                    census["declared_coefficient_pairs"],
                "declared_member_count": census["declared_member_count"],
                "exact_arithmetic": (
                    "stored matrix scalars converted to exact rational "
                    "complex numbers; cross terms computed both as "
                    "|sum z|^2-sum|z|^2 and pairwise amplitude products"
                ),
                "state_construction": (
                    "(a|c1>+b|c2>)/sqrt(|a|^2+|b|^2), represented "
                    "without an inexact square root by exact numerator "
                    "amplitudes and exact norm squared"
                ),
                "extra_coefficient_pairs": census["extra_coefficient_pairs"],
                "extra_member_count": census["extra_member_count"],
                "member_findings": census["members"],
                "mixture_baseline_count":
                    controls["mixture_baseline_count"],
                "theorem_outcome": census["theorem_on_recounted_family"],
            },
        ),
        (
            "CERTIFICATE 2 STRUCTURAL CLAIM MATRIX-EXHAUSTION ATTACK",
            bool(structural_execution_passed),
            {
                "attack_execution": "COMPLETE",
                **structure,
            },
        ),
        (
            "CERTIFICATE 3 BEYOND-TWO-CHANNEL PROBE",
            bool(triple_execution_passed),
            {
                "attack_execution": "COMPLETE",
                "channel_triple_count": triples["channel_triple_count"],
                "coefficient_triples": triples["coefficient_triples"],
                "counterexamples": triples["counterexamples"],
                "member_findings": triples["members"],
                "member_count": triples["member_count"],
                "structural_generality": triples["structural_generality"],
            },
        ),
        (
            "CERTIFICATE 4 VERTEX-IDENTITY GUARD",
            bool(identity_execution_passed),
            {
                "audit_input_paths": AUDIT_INPUT_PATHS,
                "blocklist": BLOCKLIST,
                "blocklist_after": blocklist_after,
                "blocklist_before": blocklist_before,
                "imported_u320_path": imported_path,
                "primary_access": "text/AST only; never imported or executed",
                "primary_ast_parsed": primary_ast_parsed,
                "primary_sha256": primary_shas_after,
                "u320_identity": identity,
                "u320_sha256_after": u320_sha_after,
            },
        ),
    ]

    # Build the final control line after measuring all preceding content.  A
    # short fixed-point loop makes the asserted byte count exact, including
    # the decimal digits of the count itself.
    pass_count = sum(int(passed) for _name, passed, _detail in certificate_specs)
    fail_count = len(certificate_specs) - pass_count
    status = (
        "ATTACK_COMPLETE_CLAIM_REFUTED"
        if (
            census["counterexamples"]
            or structure["shared_branch_cells"]
            or triples["counterexamples"]
            or not structure["branch_target_formula_matches"]
        )
        else "ATTACK_COMPLETE_NO_COUNTEREXAMPLE"
    )
    planned_stdout_bytes = 0
    all_lines: list[str] = []
    for _iteration in range(8):
        runtime_passed = elapsed < AUDIT_TIMEOUT_SEC
        control_finding = {
            "all_15_mixture_baselines":
                controls["mixture_baselines"],
            "cycle771_mixture_block_additivity":
                controls["cycle771_mixture_block_additivity"],
            "determinism_rerun": deterministic,
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": elapsed,
            "synthetic_refutation_sensitivity": sensitivity,
            "single_channel_defining_rows":
                controls["single_channel_defining_rows"],
            "stdout_bytes_exact": planned_stdout_bytes,
            "stdout_limit_bytes": OUTPUT_LIMIT_BYTES,
        }
        control_passed = bool(
            controls_execution_passed
            and runtime_passed
            and planned_stdout_bytes < OUTPUT_LIMIT_BYTES
        )
        specs = certificate_specs + [
            (
                "CERTIFICATE 5 CONTROLS DETERMINISM AND BOUNDS",
                control_passed,
                control_finding,
            )
        ]
        pass_count = sum(int(passed) for _name, passed, _detail in specs)
        fail_count = len(specs) - pass_count
        final = {
            "census_declared_members": census["declared_member_count"],
            "census_extra_members": census["extra_member_count"],
            "fail": fail_count,
            "matrix_structural_claim": structure["structural_claim"],
            "pass": pass_count,
            "runtime_sec": elapsed,
            "status": status,
            "stdout_bytes": planned_stdout_bytes,
            "three_channel_members": triples["member_count"],
        }
        all_lines = [
            headline + " :: " + render_json(headline_detail),
            *[
                certificate_line(name, passed, detail)
                for name, passed, detail in specs
            ],
            "FINAL :: " + render_json(final),
        ]
        measured = sum(
            len((line + "\n").encode("utf-8")) for line in all_lines
        )
        if measured == planned_stdout_bytes:
            break
        planned_stdout_bytes = measured
    else:
        raise RuntimeError("stdout byte-count fixed point did not converge")

    for line in all_lines:
        print(line)
    return 1 if fail_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
