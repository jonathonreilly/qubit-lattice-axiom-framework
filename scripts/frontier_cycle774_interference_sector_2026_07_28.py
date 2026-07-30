#!/usr/bin/env python3
"""Cycle 774: exact bounded census of the landed recoil interference sector.

The census applies the Cycle-320 vertex to every declared two-channel state,
but decides interference from exact symbolic amplitude products.  Cycle-768
and Cycle-771 are blocklisted text evidence; a Cycle-768 kernel comparator is
extracted only if a genuinely interfering member is found.  No coefficients
are fitted here.
"""

AUDIT_TIMEOUT_SEC = 1500
OUTPUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
)
PRIMARY_TEXT_PATHS = (
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
    "scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
)
BLOCKLIST = (
    "frontier_cycle768_response_law_candidate_2026_07_28",
    "frontier_cycle771_prediction_verification_2026_07_28",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706",
    AUDIT_INPUT_PATHS[1]:
        "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75",
    PRIMARY_TEXT_PATHS[0]:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
    PRIMARY_TEXT_PATHS[1]:
        "6e668efc97a276ce9b0b442cbf7f9eda32c2aa6c722b6f562c5ca4046a4b7ba1",
}

# Gaussian integers are encoded as (real, imaginary).  This is the complete
# coefficient family named by the task, declared before any census work.
DECLARED_COEFFICIENT_FAMILY = (
    ("1,1", ((1, 0), (1, 0))),
    ("1,-1", ((1, 0), (-1, 0))),
    ("1,i", ((1, 0), (0, 1))),
    ("1,-i", ((1, 0), (0, -1))),
    ("2,1", ((2, 0), (1, 0))),
    ("1,2", ((1, 0), (2, 0))),
)

import ast
from fractions import Fraction
import hashlib
from itertools import combinations
import json
import math
from pathlib import Path
import sys
import time

import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322
import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
STDOUT_BYTES = 0

Gaussian = tuple[Fraction, Fraction]
Vector = tuple[Fraction, ...]
ResponseRow = tuple[Vector, Vector, Vector]


def jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return value.numerator
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def emit(line: str) -> None:
    global STDOUT_BYTES
    print(line)
    STDOUT_BYTES += len((line + "\n").encode("utf-8"))


def certificate(name: str, passed: bool, finding: object) -> None:
    global PASS, FAIL
    prefix = "PASS" if passed else "FAIL"
    if passed:
        PASS += 1
    else:
        FAIL += 1
    emit(
        f"{prefix} {name} :: "
        + json.dumps(
            finding, sort_keys=True, separators=(",", ":"), default=jsonable
        )
    )


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def exact_l2_text(squared_norm: Fraction, unit: str) -> str:
    if not squared_norm:
        return "0"
    numerator_root = math.isqrt(squared_norm.numerator)
    denominator_root = math.isqrt(squared_norm.denominator)
    if (
        numerator_root * numerator_root == squared_norm.numerator
        and denominator_root * denominator_root == squared_norm.denominator
    ):
        coefficient = Fraction(numerator_root, denominator_root)
        return f"{fraction_text(coefficient)}*{unit}"
    return (
        f"sqrt({squared_norm.numerator}/{squared_norm.denominator})"
        f"*{unit}"
    )


def gaussian(value: tuple[int, int]) -> Gaussian:
    return Fraction(value[0]), Fraction(value[1])


def gaussian_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gaussian_abs_squared(value: Gaussian) -> Fraction:
    return value[0] * value[0] + value[1] * value[1]


def direction_tuple(index: int) -> Vector:
    return tuple(Fraction(int(value)) for value in U320.c210.DIRECTIONS[index])


def add_rows(rows: tuple[ResponseRow, ...]) -> ResponseRow:
    if not rows:
        raise ValueError("cannot add an empty row collection")
    return tuple(
        tuple(
            sum((row[component][axis] for row in rows), start=Fraction())
            for axis in range(len(rows[0][component]))
        )
        for component in range(len(rows[0]))
    )  # type: ignore[return-value]


def weighted_rows(
    weights: tuple[Fraction, ...], rows: tuple[ResponseRow, ...]
) -> ResponseRow:
    if not rows or len(weights) != len(rows):
        raise ValueError("weighted response rows have inconsistent shape")
    return tuple(
        tuple(
            sum(
                (
                    weight * row[component][axis]
                    for weight, row in zip(weights, rows)
                ),
                start=Fraction(),
            )
            for axis in range(len(rows[0][component]))
        )
        for component in range(len(rows[0]))
    )  # type: ignore[return-value]


def expected_branch_flat(channel: int) -> int:
    direction_count = len(U320.c210.DIRECTIONS)
    return (
        direction_count * direction_count * U320.REVERSE[channel]
        + direction_count * channel
        + channel
    )


def decode_branch_flat(flat: int) -> tuple[int, int, int]:
    direction_count = len(U320.c210.DIRECTIONS)
    return (
        flat // (direction_count * direction_count),
        (flat // direction_count) % direction_count,
        flat % direction_count,
    )


def defining_row(channel: int) -> ResponseRow:
    source = direction_tuple(channel)
    target = direction_tuple(U320.REVERSE[channel])
    return (
        tuple(final - initial for final, initial in zip(target, source)),
        source,
        source,
    )


def single_channel_row_from_branch(channel: int) -> ResponseRow:
    matter, mediator, auxiliary = decode_branch_flat(
        expected_branch_flat(channel)
    )
    source = direction_tuple(channel)
    matter_vector = direction_tuple(matter)
    return (
        tuple(final - initial for final, initial in zip(matter_vector, source)),
        direction_tuple(mediator),
        direction_tuple(auxiliary),
    )


def response_from_probability_tensor(
    channels: tuple[int, int],
    input_weights: tuple[Fraction, Fraction],
    probabilities: tuple[Fraction, ...],
) -> ResponseRow:
    """Cycle-771 branch-conditional version of U320 displacement bookkeeping."""
    direction_count = len(U320.c210.DIRECTIONS)
    total = sum(probabilities, start=Fraction())
    if not total:
        raise ValueError("coherent branch tensor has zero transfer weight")
    raw = [
        [Fraction() for _axis in range(3)]
        for _component in range(3)
    ]
    for flat, probability in enumerate(probabilities):
        if not probability:
            continue
        indices = decode_branch_flat(flat)
        for component, index in enumerate(indices):
            vector = direction_tuple(index)
            for axis, value in enumerate(vector):
                raw[component][axis] += probability * value
    input_direction = tuple(
        sum(
            (
                weight * direction_tuple(channel)[axis]
                for weight, channel in zip(input_weights, channels)
            ),
            start=Fraction(),
        )
        for axis in range(3)
    )
    return tuple(
        tuple(
            raw[component][axis] / total
            - (input_direction[axis] if component == 0 else Fraction())
            for axis in range(3)
        )
        for component in range(3)
    )  # type: ignore[return-value]


def per_channel_rows_on_coherent_tensor(
    channels: tuple[int, int],
    probabilities: tuple[Fraction, ...],
) -> tuple[ResponseRow, ResponseRow]:
    total = sum(probabilities, start=Fraction())
    if not total:
        raise ValueError("coherent branch tensor has zero transfer weight")
    rows = []
    for channel in channels:
        source = direction_tuple(channel)
        raw = [
            [Fraction() for _axis in range(3)]
            for _component in range(3)
        ]
        for flat, probability in enumerate(probabilities):
            if not probability:
                continue
            matter, mediator, auxiliary = decode_branch_flat(flat)
            vectors = (
                tuple(
                    final - initial
                    for final, initial in zip(direction_tuple(matter), source)
                ),
                direction_tuple(mediator),
                direction_tuple(auxiliary),
            )
            for component, vector in enumerate(vectors):
                for axis, value in enumerate(vector):
                    raw[component][axis] += probability * value
        rows.append(
            tuple(
                tuple(value / total for value in raw[component])
                for component in range(3)
            )
        )
    return tuple(rows)  # type: ignore[return-value]


def exact_census_member(
    vertex: object,
    channels: tuple[int, int],
    coefficient_label: str,
    coefficient_pair: tuple[tuple[int, int], tuple[int, int]],
) -> dict[str, object]:
    """Apply the vertex, then derive every cross cell with Gaussian rationals."""
    direction_count = len(U320.c210.DIRECTIONS)
    branch_dimension = direction_count**3
    coefficients = tuple(gaussian(value) for value in coefficient_pair)
    coefficient_norms = tuple(
        gaussian_abs_squared(value) for value in coefficients
    )
    input_norm_squared = sum(coefficient_norms, start=Fraction())
    weights = tuple(
        value / input_norm_squared for value in coefficient_norms
    )

    # This numerical application is only a landed-matrix consistency control.
    # The cross-term classification below is entirely exact and symbolic.
    numeric_state = U320.np.zeros(int(vertex.shape[0]), dtype=complex)
    normalization = math.sqrt(float(input_norm_squared))
    for channel, value in zip(channels, coefficients):
        numeric_state[channel] = complex(float(value[0]), float(value[1])) \
            / normalization
    numeric_branch = (vertex @ numeric_state)[direction_count:]

    supports = tuple({expected_branch_flat(channel)} for channel in channels)
    overlap = supports[0] & supports[1]
    numeric_support = {
        flat for flat, amplitude in enumerate(numeric_branch)
        if complex(amplitude) != 0j
    }
    expected_union = supports[0] | supports[1]

    coherent_probabilities = []
    mixture_probabilities = []
    cross_terms = []
    cross_nonzero = []
    for flat in range(branch_dimension):
        coherent_amplitude = (Fraction(), Fraction())
        mixture_probability = Fraction()
        for coefficient, coefficient_norm, support in zip(
            coefficients, coefficient_norms, supports
        ):
            if flat in support:
                coherent_amplitude = gaussian_add(
                    coherent_amplitude, coefficient
                )
                mixture_probability += coefficient_norm / input_norm_squared
        coherent_probability = (
            gaussian_abs_squared(coherent_amplitude) / input_norm_squared
        )
        cross_term = coherent_probability - mixture_probability
        coherent_probabilities.append(coherent_probability)
        mixture_probabilities.append(mixture_probability)
        cross_terms.append(cross_term)
        if cross_term:
            cross_nonzero.append(
                {
                    "branch_cell": decode_branch_flat(flat),
                    "branch_flat": flat,
                    "coefficient_of_sin_angle_squared": cross_term,
                }
            )

    l1_coefficient = sum((abs(value) for value in cross_terms), Fraction())
    l2_squared_coefficient = sum(
        (value * value for value in cross_terms), Fraction()
    )
    coherent_tensor = tuple(coherent_probabilities)
    actual_response = response_from_probability_tensor(
        channels, weights, coherent_tensor
    )
    member_id = f"{channels[0]}-{channels[1]}:{coefficient_label}"
    return {
        "actual_response": actual_response,
        "applied_branch_support_matches_symbolic":
            numeric_support == expected_union,
        "channels": channels,
        "classification": (
            "IDENTICALLY_ZERO" if not cross_nonzero else "NONZERO"
        ),
        "coefficient_pair": coefficient_label,
        "coherent_probability_tensor_units_sin2": coherent_tensor,
        "cross_l1_exact": (
            "0" if not l1_coefficient
            else f"{fraction_text(l1_coefficient)}*sin(ANGLE)^2"
        ),
        "cross_l2_exact": exact_l2_text(
            l2_squared_coefficient, "sin(ANGLE)^2"
        ),
        "cross_l2_squared_coefficient_sin4": l2_squared_coefficient,
        "cross_term_tensor": {
            "cell_count": branch_dimension,
            "nonzero_cells": tuple(cross_nonzero),
            "representation":
                "sparse exact coefficients of sin(ANGLE)^2; all omitted cells are 0",
            "zero_cell_count": branch_dimension - len(cross_nonzero),
        },
        "input_norm_squared_before_normalization": input_norm_squared,
        "member_id": member_id,
        "mixture_probability_tensor_units_sin2":
            tuple(mixture_probabilities),
        "overlap_cells": tuple(sorted(overlap)),
        "overlap_count": len(overlap),
        "weights": weights,
    }


def run_interference_census(vertex: object) -> tuple[dict[str, object], ...]:
    direction_count = len(U320.c210.DIRECTIONS)
    rows = []
    for channels in combinations(range(direction_count), 2):
        for label, coefficients in DECLARED_COEFFICIENT_FAMILY:
            rows.append(
                exact_census_member(
                    vertex, channels, label, coefficients
                )
            )
    return tuple(rows)


def mixture_baselines() -> tuple[dict[str, object], ...]:
    """The unnormalized two-column convention tested in Cycle 771."""
    rows = []
    direction_count = len(U320.c210.DIRECTIONS)
    for channels in combinations(range(direction_count), 2):
        channel_rows = tuple(
            single_channel_row_from_branch(channel) for channel in channels
        )
        supports = tuple(
            {expected_branch_flat(channel)} for channel in channels
        )
        rows.append(
            {
                "branch_support_overlap": len(supports[0] & supports[1]),
                "channels": channels,
                "composition":
                    "unnormalized identity-column mixture (sum of rows)",
                "cross_term_norm_exact": "0",
                "response_row": add_rows(channel_rows),
            }
        )
    return tuple(rows)


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one function {name!r}")
    return matches[0]


def fraction_assignment(function: ast.FunctionDef, name: str) -> Fraction:
    matches = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one assignment to {name!r}")
    call = matches[0].value
    if not (
        isinstance(call, ast.Call)
        and isinstance(call.func, ast.Name)
        and call.func.id == "Fraction"
        and len(call.args) == 1
        and not call.keywords
    ):
        raise ValueError(f"{name!r} is not a one-argument Fraction call")
    return Fraction(ast.literal_eval(call.args[0]))


def extract_cycle771_pair(source: str) -> tuple[int, int]:
    tree = ast.parse(source, filename=PRIMARY_TEXT_PATHS[1])
    assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "DIRECT_CHANNEL_PAIR"
            for target in node.targets
        )
    ]
    if len(assignments) != 1:
        raise ValueError("Cycle-771 direct pair assignment is not unique")
    value = ast.literal_eval(assignments[0].value)
    if not (
        isinstance(value, tuple)
        and len(value) == 2
        and all(isinstance(item, int) for item in value)
    ):
        raise ValueError("Cycle-771 direct pair is not a literal integer pair")
    return value


def extract_cycle768_kernel(source: str) -> dict[str, object]:
    """Conditional text/AST extraction; called only for a nonzero sector."""
    tree = ast.parse(source, filename=PRIMARY_TEXT_PATHS[0])
    main = named_function(tree, "main")
    recoil = named_function(tree, "derive_recoil_coefficients")
    transfer = named_function(tree, "derive_transfer_coefficients")
    derived_one = fraction_assignment(main, "derived_one")
    main_attributes = {
        node.attr
        for node in ast.walk(main)
        if isinstance(node, ast.Attribute)
    }
    evidence = {
        "main_asserts_recoil_coefficients":
            "recoil_coefficients" in main_attributes,
        "main_asserts_transfer_coefficients":
            "transfer_coefficients" in main_attributes,
        "recoil_function_present": recoil.name == "derive_recoil_coefficients",
        "transfer_function_present":
            transfer.name == "derive_transfer_coefficients",
    }
    if not all(evidence.values()):
        raise ValueError(f"Cycle-768 kernel AST contract changed: {evidence}")
    return {
        "extraction_mode": "text/AST only; primary never imported or executed",
        "recoil_coefficients": tuple(derived_one for _component in range(3)),
        "structural_evidence": evidence,
        "transfer_coefficients": tuple(
            derived_one for _entry in range(len(S322.ENDPOINTS) ** 2)
        ),
    }


def apply_recoil_kernel(
    row: ResponseRow, coefficients: tuple[Fraction, ...]
) -> ResponseRow:
    if len(row) != len(coefficients):
        raise ValueError("kernel and response component counts differ")
    return tuple(
        tuple(coefficient * value for value in component)
        for coefficient, component in zip(coefficients, row)
    )  # type: ignore[return-value]


def kernel_coverage_table(
    nonzero_members: tuple[dict[str, object], ...],
    kernel: dict[str, object],
) -> tuple[dict[str, object], ...]:
    """No-refit comparison of the two requested composition readings."""
    recoil = kernel["recoil_coefficients"]
    if not isinstance(recoil, tuple):
        raise TypeError("extracted recoil coefficients are not a tuple")
    table = []
    for member in nonzero_members:
        channels = member["channels"]
        weights = member["weights"]
        probabilities = member["coherent_probability_tensor_units_sin2"]
        actual = member["actual_response"]
        if not (
            isinstance(channels, tuple)
            and isinstance(weights, tuple)
            and isinstance(probabilities, tuple)
            and isinstance(actual, tuple)
        ):
            raise TypeError("census member has malformed coverage data")
        single_rows = tuple(defining_row(channel) for channel in channels)
        mixture_reading = apply_recoil_kernel(
            weighted_rows(weights, single_rows), recoil
        )
        direct_per_channel = per_channel_rows_on_coherent_tensor(
            channels, probabilities
        )
        direct_reading = apply_recoil_kernel(
            weighted_rows(weights, direct_per_channel), recoil
        )
        mixture_match = actual == mixture_reading
        direct_match = actual == direct_reading
        table.append(
            {
                "actual_coherent_response": actual,
                "channels": channels,
                "coefficient_pair": member["coefficient_pair"],
                "direct_coherent_per_channel_rows": direct_per_channel,
                "direct_coherent_reading": direct_reading,
                "direct_coherent_reading_matches": direct_match,
                "mixture_reading": mixture_reading,
                "mixture_reading_matches": mixture_match,
                "outcome": (
                    "BOTH_MATCH" if mixture_match and direct_match
                    else "MIXTURE_ONLY" if mixture_match
                    else "DIRECT_COHERENT_ONLY" if direct_match
                    else "NEITHER_MATCH"
                ),
            }
        )
    return tuple(table)


def vertex_structure_audit(
    source: str, exchange: object, vertex: object
) -> dict[str, object]:
    tree = ast.parse(source, filename=AUDIT_INPUT_PATHS[0])
    function = named_function(tree, "link_recoil_vertex")
    compact = "".join(ast.unparse(function).split())
    fragments = (
        "dimension=6+6**3",
        "fordirectioninrange(6):",
        "pair_index=6+36*REVERSE[direction]+6*direction+direction",
        "exchange[pair_index,direction]=1.0",
        "exchange[direction,pair_index]=1.0",
        "square=exchange@exchange",
        "(np.cos(angle)-1)*square",
        "1j*np.sin(angle)*exchange",
    )
    fragment_presence = {
        fragment: fragment in compact for fragment in fragments
    }
    direction_count = len(U320.c210.DIRECTIONS)
    branch_dimension = direction_count**3
    expected_supports = tuple(
        (expected_branch_flat(channel),)
        for channel in range(direction_count)
    )
    exchange_supports = tuple(
        tuple(
            flat
            for flat in range(branch_dimension)
            if complex(exchange[direction_count + flat, channel]) != 0j
        )
        for channel in range(direction_count)
    )
    vertex_supports = tuple(
        tuple(
            flat
            for flat in range(branch_dimension)
            if complex(vertex[direction_count + flat, channel]) != 0j
        )
        for channel in range(direction_count)
    )
    branch_tuples = tuple(
        decode_branch_flat(support[0]) for support in expected_supports
    )
    conserved = all(
        mediator == source and auxiliary == source
        for source, (_matter, mediator, auxiliary)
        in enumerate(branch_tuples)
    )
    return {
        "ast_fragments": fragment_presence,
        "branch_target_by_source": branch_tuples,
        "exchange_supports": exchange_supports,
        "expected_supports": expected_supports,
        "mechanism": (
            "For source d, the branch target is "
            "(matter,mediator,auxiliary)=(REVERSE[d],d,d). "
            "The mediator and auxiliary tensor indices therefore retain d "
            "as orthogonal source labels; distinct source columns cannot "
            "share a branch cell."
        ),
        "passed": (
            all(fragment_presence.values())
            and tuple(U320.REVERSE) == (1, 0, 3, 2, 5, 4)
            and sorted(U320.REVERSE) == list(range(direction_count))
            and exchange_supports == expected_supports
            and vertex_supports == expected_supports
            and conserved
        ),
        "source_index_conserved_in_mediator_and_auxiliary": conserved,
        "vertex_supports": vertex_supports,
    }


def census_ast_firewall(source: str) -> dict[str, object]:
    tree = ast.parse(source, filename=str(Path(__file__)))
    selected_names = (
        "gaussian",
        "gaussian_add",
        "gaussian_abs_squared",
        "direction_tuple",
        "add_rows",
        "weighted_rows",
        "expected_branch_flat",
        "decode_branch_flat",
        "defining_row",
        "single_channel_row_from_branch",
        "response_from_probability_tensor",
        "per_channel_rows_on_coherent_tensor",
        "exact_census_member",
        "run_interference_census",
        "mixture_baselines",
    )
    selected = tuple(named_function(tree, name) for name in selected_names)
    forbidden_fragments = (
        "kernel", "comparator", "primary_text", "cycle768", "cycle771"
    )
    violations = []
    for function in selected:
        for node in ast.walk(function):
            identifier = None
            if isinstance(node, ast.Name):
                identifier = node.id
            elif isinstance(node, ast.Attribute):
                identifier = node.attr
            if identifier and any(
                fragment in identifier.casefold()
                for fragment in forbidden_fragments
            ):
                violations.append(
                    {
                        "function": function.name,
                        "identifier": identifier,
                        "line": node.lineno,
                    }
                )
    return {
        "evaluation_functions": selected_names,
        "forbidden_fragments": forbidden_fragments,
        "passed": not violations,
        "violations": tuple(violations),
    }


def import_surface_audit(source: str) -> dict[str, object]:
    tree = ast.parse(source, filename=str(Path(__file__)))
    local_imports = {}
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname in {"S322", "U320"}:
                    local_imports[alias.asname] = alias.name
    assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    literal_paths = ()
    if (
        len(assignments) == 1
        and isinstance(assignments[0].value, ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in assignments[0].value.elts
        )
    ):
        literal_paths = tuple(
            element.value for element in assignments[0].value.elts
        )
    return {
        "imported_landed_aliases": local_imports,
        "literal_audit_input_paths": literal_paths,
        "passed": (
            literal_paths == AUDIT_INPUT_PATHS
            and local_imports == {
                "S322":
                    "two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18",
                "U320":
                    "unit_weight_carried_link_recoil_cycle320_2026_07_18",
            }
        ),
    }


def framework_input_probe() -> dict[str, object]:
    """Filename-only search; Cycle-720 files remain unread by the 721-only rule."""
    scripts = ROOT / "scripts"
    hits = tuple(
        sorted(
            path.name
            for path in scripts.glob("*.py")
            if (
                ("cycle720" in path.name.casefold()
                 or "cycle721" in path.name.casefold())
                and ("bell" in path.name.casefold()
                     or "choi" in path.name.casefold())
            )
        )
    )
    eligible = tuple(
        name for name in hits if "cycle721" in name.casefold()
    )
    if eligible:
        return {
            "eligible_cycle721_candidates": eligible,
            "filename_hits": hits,
            "framework_input_status":
                "present_but_not_declared_in_static_audit_inputs",
            "passed": False,
        }
    return {
        "eligible_cycle721_candidates": (),
        "filename_hits": hits,
        "framework_input_status": "absent",
        "passed": True,
        "reason": (
            "no Cycle-721 bell/choi module exists; Cycle-720 filename hits "
            "were not read or imported under the explicit 721-only input rule"
        ),
    }


def main() -> int:
    started = time.monotonic()
    self_source = Path(__file__).read_text(encoding="utf-8")
    blocklist_before = {
        module: module in sys.modules for module in BLOCKLIST
    }
    permitted_before = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    primary_before = {
        path: (ROOT / path).read_bytes() for path in PRIMARY_TEXT_PATHS
    }
    shas_before = {
        path: sha256_bytes(data)
        for path, data in {**permitted_before, **primary_before}.items()
    }
    surface_audit = import_surface_audit(self_source)
    firewall = census_ast_firewall(self_source)
    cycle771_pair = extract_cycle771_pair(
        primary_before[PRIMARY_TEXT_PATHS[1]].decode("utf-8")
    )

    exchange, vertex, _charge, _momenta = U320.link_recoil_vertex(U320.ANGLE)
    structure = vertex_structure_audit(
        permitted_before[AUDIT_INPUT_PATHS[0]].decode("utf-8"),
        exchange,
        vertex,
    )

    emit(
        "DECLARED FAMILY :: "
        + json.dumps(
            {
                "channel_pairs":
                    tuple(combinations(range(len(U320.c210.DIRECTIONS)), 2)),
                "coefficient_pairs":
                    tuple(label for label, _values
                          in DECLARED_COEFFICIENT_FAMILY),
                "member_count":
                    math.comb(len(U320.c210.DIRECTIONS), 2)
                    * len(DECLARED_COEFFICIENT_FAMILY),
                "normalization":
                    "(a|c1>+b|c2>)/sqrt(|a|^2+|b|^2)",
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )

    census = run_interference_census(vertex)
    deterministic_census = run_interference_census(vertex)
    baselines = mixture_baselines()
    deterministic_baselines = mixture_baselines()
    for row in census:
        emit(
            "CENSUS MEMBER :: "
            + json.dumps(
                {
                    "channels": row["channels"],
                    "classification": row["classification"],
                    "coefficient_pair": row["coefficient_pair"],
                    "cross_l1_exact": row["cross_l1_exact"],
                    "cross_l2_exact": row["cross_l2_exact"],
                    "cross_term_tensor": row["cross_term_tensor"],
                    "member_id": row["member_id"],
                    "overlap_cells": row["overlap_cells"],
                    "overlap_count": row["overlap_count"],
                    "weights": row["weights"],
                },
                sort_keys=True,
                separators=(",", ":"),
                default=jsonable,
            )
        )
    for row in baselines:
        emit(
            "MIXTURE BASELINE :: "
            + json.dumps(
                row,
                sort_keys=True,
                separators=(",", ":"),
                default=jsonable,
            )
        )

    zero_members = tuple(
        row for row in census
        if row["classification"] == "IDENTICALLY_ZERO"
    )
    nonzero_members = tuple(
        row for row in census if row["classification"] == "NONZERO"
    )
    zero_ids = tuple(row["member_id"] for row in zero_members)
    nonzero_ids = tuple(row["member_id"] for row in nonzero_members)
    emit(
        "CENSUS ZERO MEMBERS :: "
        + json.dumps(zero_ids, separators=(",", ":"))
    )
    emit(
        "CENSUS NONZERO MEMBERS :: "
        + json.dumps(nonzero_ids, separators=(",", ":"))
    )

    if nonzero_members:
        kernel = extract_cycle768_kernel(
            primary_before[PRIMARY_TEXT_PATHS[0]].decode("utf-8")
        )
        coverage = kernel_coverage_table(nonzero_members, kernel)
        for row in coverage:
            emit(
                "KERNEL COVERAGE ROW :: "
                + json.dumps(
                    row,
                    sort_keys=True,
                    separators=(",", ":"),
                    default=jsonable,
                )
            )
        outcomes = tuple(row["outcome"] for row in coverage)
        coverage_outcome = (
            "kernel extends under both readings"
            if outcomes and all(value == "BOTH_MATCH" for value in outcomes)
            else "kernel extends only under the mixture reading"
            if outcomes and all(value == "MIXTURE_ONLY" for value in outcomes)
            else "kernel extends only under the direct coherent reading"
            if outcomes
            and all(value == "DIRECT_COHERENT_ONLY" for value in outcomes)
            else "kernel does not cover the interference sector"
            if outcomes and all(value == "NEITHER_MATCH" for value in outcomes)
            else "kernel coverage is member-dependent"
        )
        sector_finding = (
            f"NONZERO interference exists in {len(nonzero_members)} members"
        )
        certificate_d_passed = (
            len(coverage) == len(nonzero_members)
            and all(
                row["outcome"] in {
                    "BOTH_MATCH",
                    "MIXTURE_ONLY",
                    "DIRECT_COHERENT_ONLY",
                    "NEITHER_MATCH",
                }
                for row in coverage
            )
        )
        certificate_d_detail = {
            "coverage_outcome": coverage_outcome,
            "kernel": kernel,
            "member_outcomes": outcomes,
            "no_refit": True,
        }
        comparator_status = "extracted_conditionally_from_cycle768_text_ast"
    else:
        coverage = ()
        kernel = None
        coverage_outcome = (
            "not applicable: the bounded family contains no interference "
            "sector on which to test either kernel-composition reading"
        )
        sector_finding = (
            "ALL members have identically zero cross-terms: source channel d "
            "survives as the orthogonal mediator and auxiliary indices "
            "(REVERSE[d],d,d)"
        )
        certificate_d_passed = bool(structure["passed"]) and len(census) > 0
        certificate_d_detail = {
            "coverage_outcome": coverage_outcome,
            "kernel_comparator": "not extracted because step 2 did not run",
            "matrix_formula": (
                "X[6+36*REVERSE[d]+6*d+d,d]=1 and "
                "V=I+(cos(angle)-1)X^2+i*sin(angle)X"
            ),
            "mechanism": structure["mechanism"],
            "orthogonality": (
                "<REVERSE[c1],c1,c1|REVERSE[c2],c2,c2>=0 "
                "whenever c1!=c2"
            ),
        }
        comparator_status = "not_extracted_no_nonzero_interference"

    emit(f"SECTOR FINDING :: {sector_finding}")
    emit(f"KERNEL COVERAGE OUTCOME :: {coverage_outcome}")

    framework = framework_input_probe()
    emit(f"framework_input_status: {framework['framework_input_status']}")
    emit(
        "FRAMEWORK INPUT PROBE :: "
        + json.dumps(
            framework,
            sort_keys=True,
            separators=(",", ":"),
        )
    )

    expected_pairs = tuple(
        combinations(range(len(U320.c210.DIRECTIONS)), 2)
    )
    expected_member_ids = tuple(
        f"{left}-{right}:{label}"
        for left, right in expected_pairs
        for label, _coefficients in DECLARED_COEFFICIENT_FAMILY
    )
    exact_tensor_checks = all(
        row["cross_term_tensor"]["cell_count"]
        == len(U320.c210.DIRECTIONS) ** 3
        and (
            row["cross_term_tensor"]["zero_cell_count"]
            + len(row["cross_term_tensor"]["nonzero_cells"])
            == row["cross_term_tensor"]["cell_count"]
        )
        and (
            row["classification"] == "IDENTICALLY_ZERO"
            if not row["cross_term_tensor"]["nonzero_cells"]
            else row["classification"] == "NONZERO"
        )
        for row in census
    )
    single_channel_controls = tuple(
        {
            "channel": channel,
            "defining_row": defining_row(channel),
            "match":
                single_channel_row_from_branch(channel)
                == defining_row(channel),
            "recounted_row": single_channel_row_from_branch(channel),
        }
        for channel in range(len(U320.c210.DIRECTIONS))
    )
    baseline_771 = next(
        row for row in baselines if row["channels"] == cycle771_pair
    )
    baseline_771_expected = add_rows(
        tuple(defining_row(channel) for channel in cycle771_pair)
    )
    baseline_control = (
        baseline_771["response_row"] == baseline_771_expected
        and baseline_771["branch_support_overlap"] == 0
        and baseline_771["cross_term_norm_exact"] == "0"
    )
    deterministic = (
        census == deterministic_census
        and baselines == deterministic_baselines
    )
    applied_vertex_control = all(
        bool(row["applied_branch_support_matches_symbolic"])
        for row in census
    )

    permitted_after = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    primary_after = {
        path: (ROOT / path).read_bytes() for path in PRIMARY_TEXT_PATHS
    }
    shas_after = {
        path: sha256_bytes(data)
        for path, data in {**permitted_after, **primary_after}.items()
    }
    blocklist_after = {
        module: module in sys.modules for module in BLOCKLIST
    }

    certificate(
        "CERTIFICATE A landed anchors and primary blocklist",
        (
            shas_before == EXPECTED_SHA256
            and shas_after == EXPECTED_SHA256
            and shas_after == shas_before
            and not any(blocklist_before.values())
            and not any(blocklist_after.values())
            and bool(surface_audit["passed"])
            and callable(U320.link_recoil_vertex)
            and callable(S322.response_matrix)
        ),
        {
            "audit_input_paths": AUDIT_INPUT_PATHS,
            "blocklist": BLOCKLIST,
            "comparator_status": comparator_status,
            "primary_access": "text/AST only; never imported or executed",
            "sha256": shas_after,
            "surface_audit": surface_audit,
            "sys_modules_after": blocklist_after,
            "sys_modules_before": blocklist_before,
        },
    )
    certificate(
        "CERTIFICATE B declared exact interference census",
        (
            tuple(row["member_id"] for row in census) == expected_member_ids
            and len(census)
            == len(expected_pairs) * len(DECLARED_COEFFICIENT_FAMILY)
            and exact_tensor_checks
            and applied_vertex_control
            and bool(firewall["passed"])
        ),
        {
            "channel_pair_count": len(expected_pairs),
            "coefficient_pair_count": len(DECLARED_COEFFICIENT_FAMILY),
            "census_member_count": len(census),
            "exact_cross_tensor_cells_per_member":
                len(U320.c210.DIRECTIONS) ** 3,
            "nonzero_member_ids": nonzero_ids,
            "symbolic_decision":
                "Gaussian-rational products times sin(ANGLE)^2",
            "zero_member_ids": zero_ids,
            "ast_firewall": firewall,
        },
    )
    certificate(
        "CERTIFICATE C interference-sector finding",
        (
            len(zero_members) + len(nonzero_members) == len(census)
            and (
                bool(nonzero_members)
                or (
                    len(zero_members) == len(census)
                    and bool(structure["passed"])
                )
            )
        ),
        {
            "nonzero_count": len(nonzero_members),
            "nonzero_members": nonzero_ids,
            "sector_finding": sector_finding,
            "structural_matrix_audit": structure,
            "zero_count": len(zero_members),
        },
    )
    certificate(
        "CERTIFICATE D kernel coverage or structural proof",
        certificate_d_passed,
        certificate_d_detail,
    )

    runtime = time.monotonic() - started
    projected_stdout_bytes = STDOUT_BYTES + 12_000
    certificate(
        "CERTIFICATE E framework probe controls determinism and bounds",
        (
            bool(framework["passed"])
            and all(row["match"] for row in single_channel_controls)
            and baseline_control
            and len(baselines) == len(expected_pairs)
            and deterministic
            and applied_vertex_control
            and runtime < AUDIT_TIMEOUT_SEC
            and projected_stdout_bytes < OUTPUT_LIMIT_BYTES
        ),
        {
            "cycle771_mixture_baseline": {
                "channels": cycle771_pair,
                "expected": baseline_771_expected,
                "match": baseline_control,
                "recounted": baseline_771["response_row"],
            },
            "determinism_rerun": deterministic,
            "framework_probe": framework,
            "landed_vertex_applied_to_every_member": applied_vertex_control,
            "mixture_baseline_count": len(baselines),
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": runtime,
            "single_channel_controls": single_channel_controls,
            "stdout_limit_bytes": OUTPUT_LIMIT_BYTES,
            "stdout_projected_bytes": projected_stdout_bytes,
        },
    )

    final_runtime = time.monotonic() - started
    emit(
        "FINAL :: "
        + json.dumps(
            {
                "fail": FAIL,
                "framework_input_status":
                    framework["framework_input_status"],
                "kernel_coverage_outcome": coverage_outcome,
                "nonzero_count": len(nonzero_members),
                "pass": PASS,
                "runtime_sec": final_runtime,
                "sector_finding": sector_finding,
                "zero_count": len(zero_members),
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
