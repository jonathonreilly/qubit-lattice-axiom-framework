#!/usr/bin/env python3
"""Cycle 778 independent adversarial attachment-completeness checker."""

AUDIT_TIMEOUT_SEC = 1500
OUTPUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
)
PRIMARY_TEXT_PATHS = (
    "scripts/frontier_cycle778_norefit_attachment_2026_07_28.py",
    "scripts/frontier_cycle774_interference_sector_2026_07_28.py",
    "scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
)
BLOCKLISTED_MODULES = (
    "frontier_cycle778_norefit_attachment_2026_07_28",
    "frontier_cycle774_interference_sector_2026_07_28",
    "frontier_cycle771_prediction_verification_2026_07_28",
    "frontier_cycle768_response_law_candidate_2026_07_28",
)
EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706",
    AUDIT_INPUT_PATHS[1]:
        "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75",
    AUDIT_INPUT_PATHS[2]:
        "ab9b852236f73ec4aecad9287e07a4029309159d956a1cb3043f9238342d6807",
}
EXPECTED_PRIMARY_SHA256 = {
    PRIMARY_TEXT_PATHS[0]:
        "033e6442c01eef32efe20e55b025459aa606b92d1a91a4e48e9f795bc3946181",
    PRIMARY_TEXT_PATHS[1]:
        "2f5214633abf7bcc715c88a646ded9bd25dc3fdfbfe09785ddd12a551dc18c25",
    PRIMARY_TEXT_PATHS[2]:
        "6e668efc97a276ce9b0b442cbf7f9eda32c2aa6c722b6f562c5ca4046a4b7ba1",
    PRIMARY_TEXT_PATHS[3]:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
}

import ast
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path
import sys
import time

import frontier_cycle749_response_comparison_harness_2026_07_28 as H749
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322
import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
STDOUT_BYTES = 0

Vector = tuple[Fraction, ...]
ResponseRow = tuple[Vector, ...]
Gaussian = tuple[Fraction, Fraction]


def jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return value.numerator
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def render(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=jsonable
    )


def emit(line: str) -> None:
    global STDOUT_BYTES
    print(line)
    STDOUT_BYTES += len((line + "\n").encode("utf-8"))


def certificate(name: str, passed: bool, finding: object) -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
    else:
        FAIL += 1
    emit(
        f"{'PASS' if passed else 'FAIL'} CERTIFICATE {name} :: "
        + render(finding)
    )


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one function {name!r}")
    return matches[0]


def named_assignment(tree: ast.AST, name: str) -> ast.Assign:
    matches = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one assignment to {name!r}")
    return matches[0]


def extract_literal_tuple(tree: ast.Module, name: str) -> tuple[object, ...]:
    assignment = named_assignment(tree, name)
    value = ast.literal_eval(assignment.value)
    if not isinstance(value, tuple):
        raise ValueError(f"{name} is not a literal tuple")
    return value


def extract_frozen_kernel(source: str) -> tuple[dict[str, object], dict[str, object]]:
    """Extract only asserted frozen data from Cycle 768 text/AST."""
    tree = ast.parse(source, filename=PRIMARY_TEXT_PATHS[3])
    main = named_function(tree, "main")
    builder = named_function(tree, "derive_response_kernel_candidate")
    assignment = named_assignment(main, "derived_one")
    call = assignment.value
    if not (
        isinstance(call, ast.Call)
        and isinstance(call.func, ast.Name)
        and call.func.id == "Fraction"
        and len(call.args) == 1
        and not call.keywords
    ):
        raise ValueError("Cycle 768 frozen coefficient form changed")
    one = Fraction(ast.literal_eval(call.args[0]))
    attributes = {
        node.attr for node in ast.walk(main) if isinstance(node, ast.Attribute)
    }
    defaults = named_assignment(builder, "defaults").value
    zero_default_form = bool(
        isinstance(defaults, ast.Call)
        and isinstance(defaults.func, ast.Name)
        and defaults.func.id == "tuple"
        and len(defaults.args) == 1
        and isinstance(defaults.args[0], ast.GeneratorExp)
        and isinstance(defaults.args[0].elt, ast.Call)
        and isinstance(defaults.args[0].elt.func, ast.Name)
        and defaults.args[0].elt.func.id == "Fraction"
        and not defaults.args[0].elt.args
        and not defaults.args[0].elt.keywords
    )
    recoil_count = len(U320.link_recoil_vertex(U320.ANGLE)[3])
    transfer_count = len(S322.ENDPOINTS) ** 2
    audit = {
        "asserted_fields_present": {
            "recoil_coefficients": "recoil_coefficients" in attributes,
            "transfer_coefficients": "transfer_coefficients" in attributes,
        },
        "extraction": "Cycle 768 text/AST only; never imported or executed",
        "frozen_unit": one,
        "zero_default_generator": zero_default_form,
    }
    if not (
        all(audit["asserted_fields_present"].values())
        and zero_default_form
        and one == Fraction(1)
    ):
        raise ValueError(f"Cycle 768 frozen-kernel contract changed: {audit}")
    kernel = {
        "recoil_coefficients": tuple(one for _ in range(recoil_count)),
        "transfer_coefficients": tuple(one for _ in range(transfer_count)),
        "fitted_defaults": tuple(
            Fraction() for _ in range(recoil_count + transfer_count)
        ),
    }
    return kernel, audit


def extract_cycle771_pair(source: str) -> tuple[int, int]:
    tree = ast.parse(source, filename=PRIMARY_TEXT_PATHS[2])
    value = ast.literal_eval(named_assignment(tree, "DIRECT_CHANNEL_PAIR").value)
    if not (
        isinstance(value, tuple)
        and len(value) == 2
        and all(isinstance(item, int) for item in value)
    ):
        raise ValueError("Cycle 771 pair is not a literal integer pair")
    return value


def primary_family_contract(source: str, direction_count: int) -> dict[str, object]:
    """Read the declared Cycle 778 family shape without executing it."""
    tree = ast.parse(source, filename=PRIMARY_TEXT_PATHS[0])
    function = named_function(tree, "declared_family")
    combination_sizes = tuple(
        sorted(
            {
                ast.literal_eval(node.args[1])
                for node in ast.walk(function)
                if (
                    isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Name)
                    and node.func.id == "combinations"
                    and len(node.args) == 2
                    and isinstance(node.args[1], ast.Constant)
                    and isinstance(node.args[1].value, int)
                )
            }
        )
    )
    strings = {
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    full_present = "full" in strings and any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "range"
        for node in ast.walk(function)
    )
    sizes = combination_sizes + ((direction_count,) if full_present else ())
    channels = tuple(
        subset
        for occupancy in product((False, True), repeat=direction_count)
        if (subset := tuple(
            index for index, occupied in enumerate(occupancy) if occupied
        ))
        and len(subset) in sizes
    )
    channels = tuple(sorted(channels, key=lambda row: (len(row), row)))
    table_function = named_function(tree, "attachment_table")
    table_keys = {
        node.value
        for node in ast.walk(table_function)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    return {
        "combination_sizes": combination_sizes,
        "composition_literal_present":
            "unnormalized identity-column mixture (sum of rows)" in strings,
        "configuration_count": len(channels),
        "channels": channels,
        "full_present": full_present,
        "printed_table_fields_present": {
            key: key in table_keys
            for key in (
                "channels",
                "exact_match",
                "input_row_variants",
                "member_id",
                "predicted_rows",
                "simulated_rows",
            )
        },
    }


def u320_surface_contract(source: str) -> dict[str, object]:
    """Inventory U320's channel rows and every locally constructed input type."""
    tree = ast.parse(source, filename=AUDIT_INPUT_PATHS[0])
    vertex = named_function(tree, "link_recoil_vertex")
    controls = named_function(tree, "local_route_controls")
    compact_vertex = "".join(ast.unparse(vertex).split())
    compact_controls = "".join(ast.unparse(controls).split())
    required_vertex = (
        "dimension=6+6**3",
        "fordirectioninrange(6):",
        "pair_index=6+36*REVERSE[direction]+6*direction+direction",
        "exchange[pair_index,direction]=1.0",
        "exchange[direction,pair_index]=1.0",
    )
    required_rows = (
        "fordirectioninrange(6):",
        "initial=np.eye(222,dtype=complex)[:,direction]",
        "response_rows.append",
    )
    all_text = "".join(source.split())
    input_types = {
        "basis_identity_column_rows":
            all(fragment in compact_controls for fragment in required_rows),
        "dense_random_six_channel_source":
            "rng.normal(size=6)+1j*rng.normal(size=6)" in all_text,
        "incoming_branch_tensor":
            "local_vertex(carried.zero_vector(),incoming,ANGLE)" in all_text,
        "uniform_six_channel_source":
            "c210.UNIFORM.copy()" in all_text,
    }
    return {
        "channel_count": len(U320.c210.DIRECTIONS),
        "input_configuration_types": input_types,
        "local_route_response_rows": compact_controls.count(
            "response_rows.append"
        ),
        "passed": (
            all(fragment in compact_vertex for fragment in required_vertex)
            and all(input_types.values())
            and compact_controls.count("response_rows.append") == 1
            and tuple(U320.REVERSE) == (1, 0, 3, 2, 5, 4)
        ),
        "reverse": tuple(U320.REVERSE),
        "vertex_fragments": {
            fragment: fragment in compact_vertex for fragment in required_vertex
        },
    }


def size_label(size: int, direction_count: int) -> str:
    labels = {
        1: "single",
        2: "pair",
        3: "triple",
        4: "quadruple",
        5: "quintuple",
        direction_count: "full",
    }
    return labels[size]


def independently_enumerated_family(
    direction_count: int,
) -> tuple[dict[str, object], ...]:
    """Enumerate binary channel occupancy, independently of Cycle 778."""
    configurations = []
    for occupancy in product((False, True), repeat=direction_count):
        channels = tuple(
            index for index, occupied in enumerate(occupancy) if occupied
        )
        if not channels:
            continue
        label = size_label(len(channels), direction_count)
        configurations.append(
            {
                "channels": channels,
                "member_id":
                    f"{label}:" + "-".join(str(value) for value in channels),
                "occupancy": occupancy,
                "subset_size": len(channels),
            }
        )
    return tuple(
        sorted(
            configurations,
            key=lambda member: (
                member["subset_size"],
                member["channels"],
            ),
        )
    )


def direction_vector(channel: int) -> Vector:
    return tuple(
        Fraction(int(value)) for value in U320.c210.DIRECTIONS[channel]
    )


def defining_rows() -> tuple[ResponseRow, ...]:
    rows = []
    for channel in range(len(U320.c210.DIRECTIONS)):
        source = direction_vector(channel)
        target = direction_vector(U320.REVERSE[channel])
        rows.append(
            (
                tuple(
                    final - initial
                    for final, initial in zip(target, source)
                ),
                source,
                source,
            )
        )
    return tuple(rows)


# Prediction lane: it accepts only frozen scalar data and landed defining rows.
def combine_model_rows(rows: tuple[ResponseRow, ...]) -> ResponseRow:
    exemplar = next(iter(rows))
    return tuple(
        tuple(
            sum(
                (row[component][axis] for row in rows),
                start=Fraction(),
            )
            for axis in range(len(exemplar[component]))
        )
        for component in range(len(exemplar))
    )


def weighted_model_rows(
    weights: tuple[Fraction, ...], rows: tuple[ResponseRow, ...]
) -> ResponseRow:
    exemplar = next(iter(rows))
    return tuple(
        tuple(
            sum(
                (
                    weight * row[component][axis]
                    for weight, row in zip(weights, rows)
                ),
                start=Fraction(),
            )
            for axis in range(len(exemplar[component]))
        )
        for component in range(len(exemplar))
    )


def declared_model_weights(
    gaussian_inputs: tuple[Gaussian, ...],
) -> tuple[Fraction, ...]:
    norms = []
    for real, imaginary in gaussian_inputs:
        norms.append(real * real + imaginary * imaginary)
    total = sum(norms, start=Fraction())
    if not total:
        raise ValueError("declared model input has zero norm")
    return tuple(value / total for value in norms)


def apply_frozen_map(
    coefficients: tuple[Fraction, ...],
    defaults: tuple[Fraction, ...],
    row: ResponseRow,
) -> ResponseRow:
    return tuple(
        tuple(
            coefficient * value + default
            for value in vector
        )
        for coefficient, default, vector in zip(coefficients, defaults, row)
    )


def predict_attachment(
    coefficients: tuple[Fraction, ...],
    defaults: tuple[Fraction, ...],
    family: tuple[dict[str, object], ...],
    rows: tuple[ResponseRow, ...],
) -> tuple[dict[str, object], ...]:
    output = []
    for member in family:
        channels = member["channels"]
        if not isinstance(channels, tuple):
            raise TypeError("family channels are malformed")
        inputs = tuple(rows[channel] for channel in channels)
        variants = tuple(
            apply_frozen_map(coefficients, defaults, row) for row in inputs
        )
        output.append(
            {
                "channels": channels,
                "input_row_variants": variants,
                "member_id": member["member_id"],
                "predicted_rows": apply_frozen_map(
                    coefficients, defaults, combine_model_rows(inputs)
                ),
            }
        )
    return tuple(output)


# Simulation lane: it receives the landed surface and never receives kernel data.
def exact_probability(amplitude: complex) -> Fraction:
    real = Fraction.from_float(float(amplitude.real))
    imaginary = Fraction.from_float(float(amplitude.imag))
    return real * real + imaginary * imaginary


def direct_column_response(
    surface: object,
    output_column: object,
    source_channel: int,
) -> tuple[ResponseRow, Fraction, int]:
    directions = surface.c210.DIRECTIONS
    direction_count = len(directions)
    axis_count = len(directions[source_channel])
    shape = tuple(direction_count for _axis in range(axis_count))
    branch = output_column[direction_count:].reshape(shape)
    total = sum(
        (exact_probability(amplitude) for amplitude in branch.flat),
        start=Fraction(),
    )
    matter = [Fraction() for _axis in range(axis_count)]
    mediator = [Fraction() for _axis in range(axis_count)]
    auxiliary = [Fraction() for _axis in range(axis_count)]
    support = int()
    for indices in product(range(direction_count), repeat=axis_count):
        probability = exact_probability(branch[indices])
        support += bool(probability)
        vectors = tuple(directions[index] for index in indices)
        for component, vector in zip(
            (matter, mediator, auxiliary), vectors
        ):
            for axis, value in enumerate(vector):
                component[axis] += probability * Fraction(int(value))
    if not total:
        raise ValueError("landed source column has zero branch transfer")
    source = directions[source_channel]
    row = (
        tuple(
            matter[axis] / total - Fraction(int(source[axis]))
            for axis in range(axis_count)
        ),
        tuple(value / total for value in mediator),
        tuple(value / total for value in auxiliary),
    )
    return row, total, support


def sum_direct_rows(rows: tuple[ResponseRow, ...]) -> ResponseRow:
    exemplar = next(iter(rows))
    return tuple(
        tuple(
            sum(
                (row[component][axis] for row in rows),
                start=Fraction(),
            )
            for axis in range(len(exemplar[component]))
        )
        for component in range(len(exemplar))
    )


def simulate_attachment(
    surface: object,
    family: tuple[dict[str, object], ...],
) -> tuple[dict[str, object], ...]:
    _exchange, vertex, _charge, _momenta = surface.link_recoil_vertex(
        surface.ANGLE
    )
    directions = surface.c210.DIRECTIONS
    dimension = next(iter(vertex.shape))
    identity = surface.np.eye(dimension, dtype=complex)
    output = []
    for member in family:
        channels = member["channels"]
        if not isinstance(channels, tuple):
            raise TypeError("family channels are malformed")
        rows = []
        weights = []
        supports = []
        for channel in channels:
            output_column = vertex @ identity[:, channel]
            row, weight, support = direct_column_response(
                surface, output_column, channel
            )
            rows.append(row)
            weights.append(weight)
            supports.append(support)
        row_tuple = tuple(rows)
        output.append(
            {
                "branch_support": tuple(supports),
                "channels": channels,
                "input_row_variants": row_tuple,
                "member_id": member["member_id"],
                "simulated_rows": sum_direct_rows(row_tuple),
                "transfer_weights": tuple(weights),
            }
        )
    return tuple(output)


def gaussian_multiply(left: Gaussian, right: Gaussian) -> Gaussian:
    left_real, left_imaginary = left
    right_real, right_imaginary = right
    return (
        left_real * right_real - left_imaginary * right_imaginary,
        left_real * right_imaginary + left_imaginary * right_real,
    )


def gaussian_add(left: Gaussian, right: Gaussian) -> Gaussian:
    left_real, left_imaginary = left
    right_real, right_imaginary = right
    return left_real + right_real, left_imaginary + right_imaginary


def gaussian_norm(left: Gaussian) -> Fraction:
    real, imaginary = left
    return real * real + imaginary * imaginary


def complex_fraction(value: complex) -> Gaussian:
    return (
        Fraction.from_float(float(value.real)),
        Fraction.from_float(float(value.imag)),
    )


def coherent_direct_response(
    surface: object,
    channels: tuple[int, ...],
    gaussian_inputs: tuple[Gaussian, ...],
) -> dict[str, object]:
    """Apply actual landed matrix entries with Gaussian-Fraction arithmetic."""
    _exchange, vertex, _charge, _momenta = surface.link_recoil_vertex(
        surface.ANGLE
    )
    directions = surface.c210.DIRECTIONS
    direction_count = len(directions)
    axis_count = len(directions[next(iter(channels))])
    branch_dimension = direction_count ** axis_count
    probabilities = []
    support = int()
    for flat in range(branch_dimension):
        row = direction_count + flat
        amplitude = (Fraction(), Fraction())
        for channel, gaussian_input in zip(channels, gaussian_inputs):
            term = gaussian_multiply(
                complex_fraction(complex(vertex[row, channel])),
                gaussian_input,
            )
            amplitude = gaussian_add(amplitude, term)
        probability = gaussian_norm(amplitude)
        probabilities.append(probability)
        support += bool(probability)
    total = sum(probabilities, start=Fraction())
    if not total:
        raise ValueError("coherent source has zero branch transfer")
    raw = [
        [Fraction() for _axis in range(axis_count)]
        for _component in range(axis_count)
    ]
    shape = tuple(direction_count for _axis in range(axis_count))
    for flat, probability in enumerate(probabilities):
        if not probability:
            continue
        indices = surface.np.unravel_index(flat, shape)
        for component, index in enumerate(indices):
            for axis, value in enumerate(directions[index]):
                raw[component][axis] += probability * Fraction(int(value))
    input_norms = tuple(gaussian_norm(value) for value in gaussian_inputs)
    input_total = sum(input_norms, start=Fraction())
    input_weights = tuple(value / input_total for value in input_norms)
    input_direction = tuple(
        sum(
            (
                weight * Fraction(int(directions[channel, axis]))
                for weight, channel in zip(input_weights, channels)
            ),
            start=Fraction(),
        )
        for axis in range(axis_count)
    )
    matter, mediator, auxiliary = raw
    response = (
        tuple(
            matter[axis] / total - input_direction[axis]
            for axis in range(axis_count)
        ),
        tuple(value / total for value in mediator),
        tuple(value / total for value in auxiliary),
    )
    return {
        "branch_support": support,
        "input_weights": input_weights,
        "response": response,
        "transfer_weight": total,
    }


def empty_direct_probe(surface: object) -> dict[str, object]:
    _exchange, vertex, _charge, _momenta = surface.link_recoil_vertex(
        surface.ANGLE
    )
    dimension = next(iter(vertex.shape))
    empty = tuple()
    inputs = surface.np.zeros((dimension, len(empty)), dtype=complex)
    outputs = vertex @ inputs
    input_column_count = int(next(reversed(inputs.shape)))
    output_column_count = int(next(reversed(outputs.shape)))
    return {
        "input_column_count": input_column_count,
        "output_column_count": output_column_count,
        "response_defined": bool(output_column_count),
        "transfer_weight": Fraction(),
    }


def incoming_branch_direct_probe(surface: object) -> dict[str, object]:
    incoming = surface.zero_tensor()
    for channel in range(len(surface.c210.DIRECTIONS)):
        incoming[
            surface.REVERSE[channel], channel, channel
        ] = surface.c210.UNIFORM[channel]
    excited, remaining = surface.local_vertex(
        surface.carried.zero_vector(), incoming, surface.ANGLE
    )
    excited_weight = sum(
        (exact_probability(value) for value in excited.flat),
        start=Fraction(),
    )
    remaining_weight = sum(
        (exact_probability(value) for value in remaining.flat),
        start=Fraction(),
    )
    return {
        "excited_support": sum(
            bool(complex(value)) for value in excited.flat
        ),
        "excited_weight": excited_weight,
        "input_branch_support": sum(
            bool(complex(value)) for value in incoming.flat
        ),
        "kernel_comparable": False,
        "reason":
            "ground-field-auxiliary branch input is outside the source-column "
            "recoil-row domain",
        "remaining_branch_support": sum(
            bool(complex(value)) for value in remaining.flat
        ),
        "remaining_weight": remaining_weight,
    }


def attachment_table(
    predictions: tuple[dict[str, object], ...],
    simulations: tuple[dict[str, object], ...],
) -> tuple[dict[str, object], ...]:
    if len(predictions) != len(simulations):
        raise ValueError("prediction and simulation lengths differ")
    rows = []
    for predicted, simulated in zip(predictions, simulations):
        if (
            predicted["member_id"] != simulated["member_id"]
            or predicted["channels"] != simulated["channels"]
        ):
            raise ValueError("prediction and simulation ordering differs")
        channels = predicted["channels"]
        predicted_variants = predicted["input_row_variants"]
        simulated_variants = simulated["input_row_variants"]
        if not (
            isinstance(channels, tuple)
            and isinstance(predicted_variants, tuple)
            and isinstance(simulated_variants, tuple)
        ):
            raise TypeError("attachment row is malformed")
        variants = tuple(
            {
                "channel": channel,
                "exact_match": predicted_row == simulated_row,
                "predicted_rows": predicted_row,
                "simulated_rows": simulated_row,
            }
            for channel, predicted_row, simulated_row in zip(
                channels, predicted_variants, simulated_variants
            )
        )
        composition_match = (
            predicted["predicted_rows"] == simulated["simulated_rows"]
        )
        rows.append(
            {
                "channels": channels,
                "exact_match": (
                    composition_match
                    and len(variants) == len(channels)
                    and all(row["exact_match"] for row in variants)
                ),
                "input_row_variants": variants,
                "member_id": predicted["member_id"],
                "predicted_rows": predicted["predicted_rows"],
                "simulated_rows": simulated["simulated_rows"],
            }
        )
    return tuple(rows)


def function_group_audit(
    tree: ast.Module,
    function_names: tuple[str, ...],
    forbidden_fragments: tuple[str, ...],
    other_lane_names: tuple[str, ...],
    kernel_values: set[Fraction] | None = None,
) -> dict[str, object]:
    functions = tuple(named_function(tree, name) for name in function_names)
    forbidden_references = []
    cross_lane_calls = []
    numeric_literals = []
    for function in functions:
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
                forbidden_references.append(
                    {
                        "function": function.name,
                        "identifier": identifier,
                        "line": node.lineno,
                    }
                )
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id in other_lane_names
            ):
                cross_lane_calls.append(
                    {
                        "callee": node.func.id,
                        "function": function.name,
                        "line": node.lineno,
                    }
                )
            if (
                isinstance(node, ast.Constant)
                and isinstance(node.value, (int, float, complex))
                and not isinstance(node.value, bool)
            ):
                numeric_literals.append(
                    {
                        "function": function.name,
                        "line": node.lineno,
                        "value": repr(node.value),
                    }
                )
    kernel_literal_overlap = tuple(
        row
        for row in numeric_literals
        if (
            kernel_values is not None
            and Fraction(row["value"]) in kernel_values
        )
    )
    return {
        "cross_lane_calls": tuple(cross_lane_calls),
        "evaluation_functions": function_names,
        "forbidden_fragments": forbidden_fragments,
        "forbidden_references": tuple(forbidden_references),
        "kernel_literal_overlap": kernel_literal_overlap,
        "numeric_literals": tuple(numeric_literals),
        "passed": (
            not forbidden_references
            and not cross_lane_calls
            and not kernel_literal_overlap
        ),
    }


def primary_firewall_audit(
    source: str, kernel: dict[str, object]
) -> dict[str, object]:
    tree = ast.parse(source, filename=PRIMARY_TEXT_PATHS[0])
    prediction_source = ast.literal_eval(
        named_assignment(tree, "PREDICTION_SOURCE").value
    )
    simulation_source = ast.literal_eval(
        named_assignment(tree, "SIMULATION_SOURCE").value
    )
    if not isinstance(prediction_source, str) or not isinstance(
        simulation_source, str
    ):
        raise ValueError("Cycle 778 embedded evaluation source is not text")
    prediction_tree = ast.parse(
        prediction_source, filename="<cycle778-primary-prediction>"
    )
    simulation_tree = ast.parse(
        simulation_source, filename="<cycle778-primary-simulation>"
    )
    prediction_names = tuple(
        node.name
        for node in prediction_tree.body
        if isinstance(node, ast.FunctionDef)
    )
    simulation_names = tuple(
        node.name
        for node in simulation_tree.body
        if isinstance(node, ast.FunctionDef)
    )
    kernel_values = {
        value
        for key in (
            "recoil_coefficients",
            "transfer_coefficients",
            "fitted_defaults",
        )
        for value in kernel[key]  # type: ignore[union-attr]
    }
    prediction = function_group_audit(
        prediction_tree,
        prediction_names,
        (
            "amplitude",
            "angle",
            "link_recoil",
            "probability",
            "simulate",
            "simulation",
            "surface",
            "vertex",
        ),
        simulation_names,
    )
    simulation = function_group_audit(
        simulation_tree,
        simulation_names,
        (
            "coefficient",
            "comparator",
            "default",
            "frozen",
            "kernel",
            "predict",
            "768",
        ),
        prediction_names,
        kernel_values,
    )
    return {
        "mode": "embedded source text/AST only; functions not executed",
        "passed": bool(prediction["passed"]) and bool(simulation["passed"]),
        "prediction_path": prediction,
        "simulation_path": simulation,
    }


PREDICTION_FUNCTIONS = (
    "combine_model_rows",
    "weighted_model_rows",
    "declared_model_weights",
    "apply_frozen_map",
    "predict_attachment",
)
SIMULATION_FUNCTIONS = (
    "exact_probability",
    "direct_column_response",
    "sum_direct_rows",
    "simulate_attachment",
    "gaussian_multiply",
    "gaussian_add",
    "gaussian_norm",
    "complex_fraction",
    "coherent_direct_response",
    "empty_direct_probe",
    "incoming_branch_direct_probe",
)


def self_firewall_audit(
    source: str, kernel: dict[str, object]
) -> dict[str, object]:
    tree = ast.parse(source, filename=str(Path(__file__)))
    kernel_values = {
        value
        for key in (
            "recoil_coefficients",
            "transfer_coefficients",
            "fitted_defaults",
        )
        for value in kernel[key]  # type: ignore[union-attr]
    }
    prediction = function_group_audit(
        tree,
        PREDICTION_FUNCTIONS,
        (
            "amplitude",
            "angle",
            "link_recoil",
            "probability",
            "simulate",
            "simulation",
            "surface",
            "vertex",
            "u320",
        ),
        SIMULATION_FUNCTIONS,
    )
    simulation = function_group_audit(
        tree,
        SIMULATION_FUNCTIONS,
        (
            "coefficient",
            "comparator",
            "default",
            "frozen",
            "kernel",
            "predict",
            "768",
        ),
        PREDICTION_FUNCTIONS,
        kernel_values,
    )
    return {
        "passed": bool(prediction["passed"]) and bool(simulation["passed"]),
        "prediction_path": prediction,
        "simulation_path": simulation,
    }


def self_import_audit(source: str) -> dict[str, object]:
    tree = ast.parse(source, filename=str(Path(__file__)))
    literal_paths = extract_literal_tuple(tree, "AUDIT_INPUT_PATHS")
    aliases = {}
    imported_roots = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_roots.append(alias.name)
                if alias.asname in {"H749", "S322", "U320"}:
                    aliases[alias.asname] = alias.name
    expected_aliases = {
        "H749": "frontier_cycle749_response_comparison_harness_2026_07_28",
        "S322": "two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18",
        "U320": "unit_weight_carried_link_recoil_cycle320_2026_07_18",
    }
    writes = []
    for node in ast.walk(tree):
        targets = []
        if isinstance(node, ast.Assign):
            targets.extend(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            targets.append(node.target)
        for target in targets:
            root = target
            while isinstance(root, (ast.Attribute, ast.Subscript)):
                root = root.value
            if isinstance(root, ast.Name) and root.id in expected_aliases:
                writes.append({"line": node.lineno, "module": root.id})
    return {
        "blocked_imports": tuple(
            name for name in imported_roots if name in BLOCKLISTED_MODULES
        ),
        "imported_landed_aliases": aliases,
        "literal_audit_input_paths": literal_paths,
        "passed": (
            literal_paths == AUDIT_INPUT_PATHS
            and aliases == expected_aliases
            and not writes
            and not any(
                name in BLOCKLISTED_MODULES for name in imported_roots
            )
        ),
        "surface_writes": tuple(writes),
    }


def honest_key_audit(source: str) -> dict[str, object]:
    tree = ast.parse(source, filename=PRIMARY_TEXT_PATHS[0])
    main = named_function(tree, "main")
    emitted_strings = tuple(
        node.value
        for call in ast.walk(main)
        if (
            isinstance(call, ast.Call)
            and isinstance(call.func, ast.Name)
            and call.func.id in {"emit", "print"}
        )
        for node in ast.walk(call)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    )
    response_values = []
    scope_values = []
    for dictionary in (
        node for node in ast.walk(main) if isinstance(node, ast.Dict)
    ):
        for key, value in zip(dictionary.keys, dictionary.values):
            if not (
                isinstance(key, ast.Constant)
                and isinstance(key.value, str)
            ):
                continue
            if key.value == "response_law_established":
                response_values.append(ast.dump(value, include_attributes=False))
            if "w7" in key.value.casefold():
                scope_values.append(
                    {
                        "key": key.value,
                        "value_ast": ast.dump(
                            value, include_attributes=False
                        ),
                    }
                )
    normalized = " ".join(source.casefold().split())
    dangerous = tuple(
        fragment
        for fragment in (
            "response_law_established: true",
            '"response_law_established": true',
            "w7_closed: true",
            '"w7_closed": true',
            "global_response_law_established: true",
        )
        if fragment in normalized
    )
    emitted_text = " ".join(emitted_strings).casefold()
    explicit_false = any(
        value == "response_law_established: false"
        for value in emitted_strings
    )
    all_dict_false = bool(response_values) and all(
        value == "Constant(value=False)" for value in response_values
    )
    fixture_status = any(
        "w7_fixture_scope_status:" in value.casefold()
        for value in emitted_strings
    )
    remaining_scope = "the remaining w7 content is scope" in emitted_text
    return {
        "dangerous_printed_closure_fragments": dangerous,
        "explicit_response_law_false": explicit_false,
        "fixture_scope_status_printed": fixture_status,
        "passed": (
            explicit_false
            and all_dict_false
            and fixture_status
            and remaining_scope
            and not dangerous
        ),
        "response_law_dict_value_asts": tuple(response_values),
        "w7_dict_entries": tuple(scope_values),
    }


def instrument_reverdict(kernel: dict[str, object]) -> dict[str, object]:
    candidate = H749.ResponseKernelCandidate(
        name="cycle778_independent_frozen_kernel",
        recoil_coefficients=kernel["recoil_coefficients"],  # type: ignore[arg-type]
        transfer_coefficients=kernel["transfer_coefficients"],  # type: ignore[arg-type]
        fitted_defaults=kernel["fitted_defaults"],  # type: ignore[arg-type]
        demonstration_role="independent text/AST extraction; no refit",
    )
    fixtures = H749.extract_frozen_fixtures()
    evaluation = H749.evaluate_candidate(candidate, fixtures, fixtures)
    residuals = evaluation["residuals"]
    if not isinstance(residuals, dict):
        raise TypeError("Cycle 749 residual dictionary is malformed")
    independent_criteria = {
        str(name): (
            "ACCEPT"
            if Fraction.from_float(float(value)) <= H749.STRICT_TOLERANCE
            else "FAIL"
        )
        for name, value in sorted(residuals.items())
    }
    return {
        "accept_count": sum(
            verdict == "ACCEPT"
            for verdict in independent_criteria.values()
        ),
        "criterion_count": len(independent_criteria),
        "evaluation": evaluation,
        "independent_criteria": independent_criteria,
        "verdict": evaluation["verdict"],
    }


def main() -> int:
    started = time.monotonic()
    self_source = Path(__file__).read_text(encoding="utf-8")
    input_bytes_before = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    primary_bytes_before = {
        path: (ROOT / path).read_bytes() for path in PRIMARY_TEXT_PATHS
    }
    input_shas_before = {
        path: sha256_bytes(data)
        for path, data in input_bytes_before.items()
    }
    primary_shas_before = {
        path: sha256_bytes(data)
        for path, data in primary_bytes_before.items()
    }
    blocklist_before = {
        module: module in sys.modules for module in BLOCKLISTED_MODULES
    }

    u320_source = input_bytes_before[AUDIT_INPUT_PATHS[0]].decode("utf-8")
    primary_source = primary_bytes_before[PRIMARY_TEXT_PATHS[0]].decode(
        "utf-8"
    )
    kernel, kernel_audit = extract_frozen_kernel(
        primary_bytes_before[PRIMARY_TEXT_PATHS[3]].decode("utf-8")
    )
    kernel_snapshot = tuple(
        (key, kernel[key])
        for key in (
            "recoil_coefficients",
            "transfer_coefficients",
            "fitted_defaults",
        )
    )
    direction_count = len(U320.c210.DIRECTIONS)
    surface_contract = u320_surface_contract(u320_source)
    declared_contract = primary_family_contract(
        primary_source, direction_count
    )
    cycle771_pair = extract_cycle771_pair(
        primary_bytes_before[PRIMARY_TEXT_PATHS[2]].decode("utf-8")
    )

    # Independent family: binary occupancy of each landed channel.
    family = independently_enumerated_family(direction_count)
    family_rerun = independently_enumerated_family(direction_count)
    family_channels = tuple(member["channels"] for member in family)
    declared_channels = declared_contract["channels"]
    if not isinstance(declared_channels, tuple):
        raise TypeError("primary declared channels are malformed")
    missed_channels = tuple(
        channels for channels in family_channels
        if channels not in declared_channels
    )
    primary_extras = tuple(
        channels for channels in declared_channels
        if channels not in family_channels
    )
    family_group_counts = {
        str(size): sum(
            member["subset_size"] == size for member in family
        )
        for size in range(1, direction_count + 1)
    }
    missed_ids = tuple(
        member["member_id"]
        for member in family
        if member["channels"] in missed_channels
    )
    empty_probe = empty_direct_probe(U320)
    repeated_family = tuple(
        {
            "channels": (channel, channel),
            "member_id": f"repeated:{channel}-{channel}",
        }
        for channel in range(direction_count)
    )

    emit(
        "HEADLINE FAMILY CENSUS :: "
        + render(
            {
                "independently_derived_nonempty_distinct_subsets":
                    len(family),
                "missed_member_count": len(missed_channels),
                "missed_member_ids": missed_ids,
                "primary_declared": len(declared_channels),
                "primary_extras": primary_extras,
                "size_counts": family_group_counts,
            }
        )
    )

    rows = defining_rows()
    recoil = kernel["recoil_coefficients"]
    defaults = kernel["fitted_defaults"][:len(recoil)]
    if not isinstance(recoil, tuple) or not isinstance(defaults, tuple):
        raise TypeError("frozen recoil data are malformed")

    # All model predictions are completed before any corresponding direct run.
    predictions = predict_attachment(recoil, defaults, family, rows)
    prediction_rerun = predict_attachment(recoil, defaults, family, rows)
    repeated_predictions = predict_attachment(
        recoil, defaults, repeated_family, rows
    )
    repeated_prediction_rerun = predict_attachment(
        recoil, defaults, repeated_family, rows
    )

    pair_channels = tuple(
        member["channels"]
        for member in family
        if member["subset_size"] == 2
    )
    asymmetric_inputs = (
        (Fraction(3), Fraction()),
        (Fraction(1), Fraction(1)),
    )
    asymmetric_predictions = tuple(
        {
            "channels": channels,
            "declared_weights": declared_model_weights(asymmetric_inputs),
            "member_id": (
                f"coherent-asymmetric:{channels[0]}-{channels[1]}:3-(1+i)"
            ),
            "predicted_rows": apply_frozen_map(
                recoil,
                defaults,
                weighted_model_rows(
                    declared_model_weights(asymmetric_inputs),
                    tuple(rows[channel] for channel in channels),
                ),
            ),
        }
        for channels in pair_channels
    )
    uniform_channels = tuple(range(direction_count))
    uniform_inputs = tuple(
        (Fraction(1), Fraction()) for _channel in uniform_channels
    )
    uniform_prediction = {
        "channels": uniform_channels,
        "declared_weights": declared_model_weights(uniform_inputs),
        "member_id": "coherent-uniform:all-six",
        "predicted_rows": apply_frozen_map(
            recoil,
            defaults,
            weighted_model_rows(
                declared_model_weights(uniform_inputs), rows
            ),
        ),
    }

    simulations = simulate_attachment(U320, family)
    simulation_rerun = simulate_attachment(U320, family)
    repeated_simulations = simulate_attachment(U320, repeated_family)
    repeated_simulation_rerun = simulate_attachment(U320, repeated_family)
    table = attachment_table(predictions, simulations)
    table_rerun = attachment_table(
        prediction_rerun, simulation_rerun
    )
    repeated_table = attachment_table(
        repeated_predictions, repeated_simulations
    )
    repeated_table_rerun = attachment_table(
        repeated_prediction_rerun, repeated_simulation_rerun
    )

    asymmetric_direct = tuple(
        {
            "channels": channels,
            "direct": coherent_direct_response(
                U320, channels, asymmetric_inputs
            ),
            "member_id": prediction["member_id"],
        }
        for channels, prediction in zip(
            pair_channels, asymmetric_predictions
        )
    )
    asymmetric_direct_rerun = tuple(
        {
            "channels": channels,
            "direct": coherent_direct_response(
                U320, channels, asymmetric_inputs
            ),
            "member_id": prediction["member_id"],
        }
        for channels, prediction in zip(
            pair_channels, asymmetric_predictions
        )
    )
    asymmetric_table = tuple(
        {
            "channels": predicted["channels"],
            "declared_weights": predicted["declared_weights"],
            "direct_input_weights": direct["direct"]["input_weights"],
            "exact_match": (
                predicted["declared_weights"]
                == direct["direct"]["input_weights"]
                and predicted["predicted_rows"]
                == direct["direct"]["response"]
            ),
            "member_id": predicted["member_id"],
            "predicted_rows": predicted["predicted_rows"],
            "simulated_rows": direct["direct"]["response"],
        }
        for predicted, direct in zip(
            asymmetric_predictions, asymmetric_direct
        )
    )
    uniform_direct = coherent_direct_response(
        U320, uniform_channels, uniform_inputs
    )
    uniform_direct_rerun = coherent_direct_response(
        U320, uniform_channels, uniform_inputs
    )
    uniform_table = {
        **uniform_prediction,
        "direct_input_weights": uniform_direct["input_weights"],
        "exact_match": (
            uniform_prediction["declared_weights"]
            == uniform_direct["input_weights"]
            and uniform_prediction["predicted_rows"]
            == uniform_direct["response"]
        ),
        "simulated_rows": uniform_direct["response"],
    }
    incoming_probe = incoming_branch_direct_probe(U320)
    incoming_probe_rerun = incoming_branch_direct_probe(U320)

    table_by_channels = {
        row["channels"]: row for row in table
    }
    primary_rows = tuple(
        table_by_channels[channels] for channels in declared_channels
    )
    missed_rows = tuple(
        table_by_channels[channels] for channels in missed_channels
    )
    primary_entry_disagreements = tuple(
        {
            "member_id": row["member_id"],
            "predicted_rows": row["predicted_rows"],
            "simulated_rows": row["simulated_rows"],
        }
        for row in primary_rows
        if not row["exact_match"]
    )
    missed_mismatches = tuple(
        row for row in missed_rows if not row["exact_match"]
    )
    full_mismatches = tuple(
        row for row in table if not row["exact_match"]
    )
    all_variant_rows = tuple(
        variant
        for row in table
        for variant in row["input_row_variants"]
    )
    primary_variant_rows = tuple(
        variant
        for row in primary_rows
        for variant in row["input_row_variants"]
    )
    variant_disagreements = tuple(
        variant for variant in all_variant_rows
        if not variant["exact_match"]
    )
    landed_variant_disagreements = tuple(
        variant
        for variant in all_variant_rows
        if (
            variant["predicted_rows"]
            != rows[variant["channel"]]
            or variant["simulated_rows"]
            != rows[variant["channel"]]
        )
    )
    variant_channel_census = {
        str(channel): sum(
            variant["channel"] == channel
            for variant in all_variant_rows
        )
        for channel in range(direction_count)
    }
    primary_variant_channel_census = {
        str(channel): sum(
            variant["channel"] == channel
            for variant in primary_variant_rows
        )
        for channel in range(direction_count)
    }

    headline_outcome = (
        "REFUTED: at least one missed member mismatches"
        if missed_mismatches
        else "EXTENDED: all 21 missed members match exactly"
    )
    emit(
        "HEADLINE COMPLETENESS FINDING :: "
        + render(
            {
                "missed_member_count": len(missed_rows),
                "missed_mismatch_count": len(missed_mismatches),
                "outcome": headline_outcome,
            }
        )
    )
    emit(
        "MISSED-MEMBER CENSUS :: "
        + render(
            tuple(
                {
                    "channels": row["channels"],
                    "exact_match": row["exact_match"],
                    "member_id": row["member_id"],
                    "predicted_rows": row["predicted_rows"],
                    "simulated_rows": row["simulated_rows"],
                }
                for row in missed_rows
            )
        )
    )
    emit(
        "PRIMARY TABLE ENTRY-LEVEL DISAGREEMENTS :: "
        + render(primary_entry_disagreements)
    )
    for row in table:
        emit("INDEPENDENT ATTACHMENT MEMBER :: " + render(row))
    for row in repeated_table:
        emit("REPEATED-CHANNEL PROBE :: " + render(row))
    for row in asymmetric_table:
        emit("ASYMMETRIC COHERENT PROBE :: " + render(row))
    emit("UNIFORM COHERENT PROBE :: " + render(uniform_table))
    emit("EMPTY CONFIGURATION PROBE :: " + render(empty_probe))
    emit("INCOMING-BRANCH CONFIGURATION PROBE :: " + render(incoming_probe))

    primary_firewall = primary_firewall_audit(primary_source, kernel)
    own_firewall = self_firewall_audit(self_source, kernel)
    import_audit = self_import_audit(self_source)
    key_audit = honest_key_audit(primary_source)
    instrument = instrument_reverdict(kernel)
    emit(
        "PRIMARY FIREWALL AUDIT :: " + render(primary_firewall)
    )
    emit("CHECKER FIREWALL AUDIT :: " + render(own_firewall))
    emit("HONEST-KEY AUDIT :: " + render(key_audit))
    emit("CYCLE 749 INSTRUMENT RE-VERDICT :: " + render(instrument))

    cycle771_row = table_by_channels[cycle771_pair]
    emit(
        "CYCLE 771 PAIR-(0,2) CONTROL :: "
        + render(
            {
                "channels": cycle771_pair,
                "exact_match": cycle771_row["exact_match"],
                "member_id": cycle771_row["member_id"],
                "predicted_rows": cycle771_row["predicted_rows"],
                "simulated_rows": cycle771_row["simulated_rows"],
            }
        )
    )

    perturbed_index = len(recoil) - 1
    perturbed_recoil = tuple(
        -value if index == perturbed_index else value
        for index, value in enumerate(recoil)
    )
    perturbed_predictions = predict_attachment(
        perturbed_recoil, defaults, family, rows
    )
    perturbed_table = attachment_table(
        perturbed_predictions, simulations
    )
    perturbed_failure = next(
        (
            row for row in perturbed_table
            if not row["exact_match"]
        ),
        None,
    )
    emit(
        "PERTURBED-KERNEL CONTROL :: "
        + render(
            {
                "coefficient_index_flipped": perturbed_index,
                "different_from_primary_index_zero": perturbed_index != 0,
                "failed_member": (
                    None if perturbed_failure is None
                    else {
                        "member_id": perturbed_failure["member_id"],
                        "predicted_rows":
                            perturbed_failure["predicted_rows"],
                        "simulated_rows":
                            perturbed_failure["simulated_rows"],
                    }
                ),
                "sweep_failed": perturbed_failure is not None,
            }
        )
    )

    input_bytes_after = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    primary_bytes_after = {
        path: (ROOT / path).read_bytes() for path in PRIMARY_TEXT_PATHS
    }
    input_shas_after = {
        path: sha256_bytes(data)
        for path, data in input_bytes_after.items()
    }
    primary_shas_after = {
        path: sha256_bytes(data)
        for path, data in primary_bytes_after.items()
    }
    blocklist_after = {
        module: module in sys.modules for module in BLOCKLISTED_MODULES
    }
    kernel_untouched = kernel_snapshot == tuple(
        (key, kernel[key])
        for key in (
            "recoil_coefficients",
            "transfer_coefficients",
            "fitted_defaults",
        )
    )
    deterministic = (
        family == family_rerun
        and predictions == prediction_rerun
        and simulations == simulation_rerun
        and table == table_rerun
        and repeated_predictions == repeated_prediction_rerun
        and repeated_simulations == repeated_simulation_rerun
        and repeated_table == repeated_table_rerun
        and asymmetric_direct == asymmetric_direct_rerun
        and uniform_direct == uniform_direct_rerun
        and incoming_probe == incoming_probe_rerun
    )
    anchors_ok = (
        input_shas_before == EXPECTED_INPUT_SHA256
        and input_shas_after == EXPECTED_INPUT_SHA256
        and input_shas_before == input_shas_after
        and primary_shas_before == EXPECTED_PRIMARY_SHA256
        and primary_shas_after == EXPECTED_PRIMARY_SHA256
        and primary_shas_before == primary_shas_after
    )
    blocklist_ok = (
        not any(blocklist_before.values())
        and not any(blocklist_after.values())
    )
    instrument_six_of_six = (
        instrument["verdict"] == "ACCEPT"
        and instrument["accept_count"] == 6
        and instrument["criterion_count"] == 6
        and not instrument["evaluation"]["failed_criteria"]  # type: ignore[index]
    )

    certificate(
        "1 FAMILY-COMPLETENESS ATTACK",
        (
            bool(surface_contract["passed"])
            and len(family) == 63
            and len(declared_channels) == 63
            and len(missed_channels) == 0
            and family_group_counts
            == {"1": 6, "2": 15, "3": 20, "4": 15, "5": 6, "6": 1}
            and len(missed_rows) == len(missed_channels)
            and not primary_extras
        ),
        {
            "attack_completed": True,
            "empty_configuration": {
                **empty_probe,
                "family_disposition":
                    "excluded: branch-conditional response is undefined at "
                    "zero transfer",
            },
            "headline": headline_outcome,
            "independent_family_count": len(family),
            "incoming_branch_configuration": incoming_probe,
            "missed_matching_count":
                len(missed_rows) - len(missed_mismatches),
            "missed_member_count": len(missed_rows),
            "missed_member_ids": missed_ids,
            "missed_mismatches": tuple(
                row["member_id"] for row in missed_mismatches
            ),
            "primary_family_count": len(declared_channels),
            "repeated_channel_probes": {
                "count": len(repeated_table),
                "family_disposition":
                    "not binary-occupancy members; evaluated as multiplicity "
                    "extensions",
                "matching": sum(
                    bool(row["exact_match"]) for row in repeated_table
                ),
            },
            "surface_contract": surface_contract,
        },
    )
    certificate(
        "2 SWEEP RECOUNT",
        (
            len(table) == len(family)
            and len(primary_rows) == 63
            and len(all_variant_rows) == 192
            and len(primary_variant_rows) == 192
            and len(primary_entry_disagreements) >= 0
            and len(variant_disagreements) >= 0
            and all(
                key
                in declared_contract["printed_table_fields_present"]
                for key in (
                    "channels",
                    "exact_match",
                    "input_row_variants",
                    "member_id",
                    "predicted_rows",
                    "simulated_rows",
                )
            )
        ),
        {
            "all_63_composition_mismatches": tuple(
                row["member_id"] for row in full_mismatches
            ),
            "all_input_row_variant_count": len(all_variant_rows),
            "all_input_row_variant_disagreements":
                len(variant_disagreements),
            "asymmetric_coherent_count": len(asymmetric_table),
            "asymmetric_coherent_mismatches": tuple(
                row["member_id"] for row in asymmetric_table
                if not row["exact_match"]
            ),
            "landed_single_row_disagreements":
                len(landed_variant_disagreements),
            "primary_42_entry_level_disagreements":
                primary_entry_disagreements,
            "primary_input_row_variant_count":
                len(primary_variant_rows),
            "primary_table_contract": declared_contract,
            "primary_variant_channel_census":
                primary_variant_channel_census,
            "uniform_coherent_match": uniform_table["exact_match"],
            "variant_channel_census": variant_channel_census,
        },
    )
    certificate(
        "3 FIREWALL AUDIT",
        (
            bool(primary_firewall["passed"])
            and bool(own_firewall["passed"])
            and bool(import_audit["passed"])
        ),
        {
            "checker": own_firewall,
            "import_and_mutation": import_audit,
            "primary": primary_firewall,
        },
    )
    certificate(
        "4 HONEST-KEY DISCIPLINE",
        bool(key_audit["passed"]) and instrument_six_of_six,
        {
            "cycle749_accept_count": instrument["accept_count"],
            "cycle749_criterion_count": instrument["criterion_count"],
            "cycle749_verdict": instrument["verdict"],
            "honest_key_audit": key_audit,
            "no_printed_global_w7_closure": key_audit["passed"],
            "response_law_established": False,
        },
    )

    runtime = time.monotonic() - started
    projected_stdout = STDOUT_BYTES + 12_000
    certificate(
        "5 CONTROLS",
        (
            anchors_ok
            and blocklist_ok
            and cycle771_pair == (0, 2)
            and bool(cycle771_row["exact_match"])
            and perturbed_failure is not None
            and perturbed_index != 0
            and deterministic
            and kernel_untouched
            and all(
                bool(row["exact_match"]) for row in repeated_table
            )
            and all(
                bool(row["exact_match"]) for row in asymmetric_table
            )
            and bool(uniform_table["exact_match"])
            and runtime < AUDIT_TIMEOUT_SEC
            and projected_stdout < OUTPUT_LIMIT_BYTES
        ),
        {
            "blocklist_after": blocklist_after,
            "blocklist_before": blocklist_before,
            "cycle771_pair": cycle771_pair,
            "cycle771_reproduced": cycle771_row["exact_match"],
            "determinism": deterministic,
            "input_sha256": input_shas_after,
            "kernel_extraction": kernel_audit,
            "kernel_untouched": kernel_untouched,
            "perturbed_index": perturbed_index,
            "perturbed_kernel_failed_at": (
                None if perturbed_failure is None
                else perturbed_failure["member_id"]
            ),
            "primary_sha256": primary_shas_after,
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": runtime,
            "stdout_limit_bytes": OUTPUT_LIMIT_BYTES,
            "stdout_projected_bytes": projected_stdout,
        },
    )

    final_runtime = time.monotonic() - started
    emit(
        "FINAL :: "
        + render(
            {
                "checker_fail": FAIL,
                "checker_pass": PASS,
                "family_count": len(family),
                "family_exact_match_count":
                    len(table) - len(full_mismatches),
                "headline": headline_outcome,
                "missed_member_count": len(missed_rows),
                "missed_mismatch_count": len(missed_mismatches),
                "primary_entry_disagreement_count":
                    len(primary_entry_disagreements),
                "response_law_established": False,
                "runtime_sec": final_runtime,
                "stdout_bytes": STDOUT_BYTES,
            }
        )
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
