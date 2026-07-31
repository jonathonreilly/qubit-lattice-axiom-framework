#!/usr/bin/env python3
"""Cycle 778: full-family no-refit attachment at fixture scope."""

AUDIT_TIMEOUT_SEC = 1500
OUTPUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
    "scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
    "scripts/frontier_cycle774_interference_sector_2026_07_28.py",
)
PRIMARY_TEXT_PATHS = AUDIT_INPUT_PATHS[3:]
BLOCKLISTED_MODULES = (
    "frontier_cycle768_response_law_candidate_2026_07_28",
    "frontier_cycle771_prediction_verification_2026_07_28",
    "frontier_cycle774_interference_sector_2026_07_28",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706",
    AUDIT_INPUT_PATHS[1]:
        "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75",
    AUDIT_INPUT_PATHS[2]:
        "ab9b852236f73ec4aecad9287e07a4029309159d956a1cb3043f9238342d6807",
    PRIMARY_TEXT_PATHS[0]:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
    PRIMARY_TEXT_PATHS[1]:
        "6e668efc97a276ce9b0b442cbf7f9eda32c2aa6c722b6f562c5ca4046a4b7ba1",
    PRIMARY_TEXT_PATHS[2]:
        "2f5214633abf7bcc715c88a646ded9bd25dc3fdfbfe09785ddd12a551dc18c25",
}

import ast
from fractions import Fraction
import hashlib
from itertools import combinations
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

# Verbatim operative C_source declarations from the landed modules.
C_source = (
    "No physical momentum, work, energy, stress, or gravity meaning is assigned.",
    "dimensionless direction/flux only; not physical momentum, work, energy, stress, gravity, or metric",
    "The result is a bounded common-code response/reciprocity proxy, not physical energy, stress, gravity, metric, or time.",
    "finite occupation response only; not energy, stress, gravity, metric, force, or time",
)


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


def certificate(name: str, passed: bool, detail: object) -> None:
    global PASS, FAIL
    prefix = "PASS" if passed else "FAIL"
    if passed:
        PASS += 1
    else:
        FAIL += 1
    emit(
        f"{prefix} CERTIFICATE {name} :: "
        + json.dumps(
            detail, sort_keys=True, separators=(",", ":"), default=jsonable
        )
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


def named_assignment(nodes: object, name: str) -> ast.Assign:
    matches = [
        node
        for node in ast.walk(nodes)  # type: ignore[arg-type]
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one assignment to {name!r}")
    return matches[0]


def one_argument_fraction(assignment: ast.Assign) -> Fraction:
    call = assignment.value
    if not (
        isinstance(call, ast.Call)
        and isinstance(call.func, ast.Name)
        and call.func.id == "Fraction"
        and len(call.args) == 1
        and not call.keywords
    ):
        raise ValueError("frozen coefficient is not a one-argument Fraction")
    return Fraction(ast.literal_eval(call.args[0]))


def extract_frozen_kernel(source: str) -> tuple[dict[str, object], dict[str, object]]:
    """Extract the asserted Cycle-768 kernel from text/AST; never import it."""
    tree = ast.parse(source, filename=PRIMARY_TEXT_PATHS[0])
    main = named_function(tree, "main")
    builder = named_function(tree, "derive_response_kernel_candidate")
    frozen_one = one_argument_fraction(named_assignment(main, "derived_one"))
    main_attributes = {
        node.attr for node in ast.walk(main) if isinstance(node, ast.Attribute)
    }
    defaults_assignment = named_assignment(builder, "defaults")
    defaults_value = defaults_assignment.value
    zero_default_form = bool(
        isinstance(defaults_value, ast.Call)
        and isinstance(defaults_value.func, ast.Name)
        and defaults_value.func.id == "tuple"
        and len(defaults_value.args) == 1
        and isinstance(defaults_value.args[0], ast.GeneratorExp)
        and isinstance(defaults_value.args[0].elt, ast.Call)
        and isinstance(defaults_value.args[0].elt.func, ast.Name)
        and defaults_value.args[0].elt.func.id == "Fraction"
        and not defaults_value.args[0].elt.args
        and not defaults_value.args[0].elt.keywords
    )
    return_calls = [
        node
        for node in ast.walk(builder)
        if isinstance(node, ast.Return)
        and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name)
        and node.value.func.id == "DerivedKernel"
    ]
    returned_keywords = (
        {keyword.arg for keyword in return_calls[0].value.keywords}
        if len(return_calls) == 1
        else set()
    )
    recoil_count = len(U320.c210.DIRECTIONS[0])
    transfer_count = len(S322.ENDPOINTS) ** 2
    evidence = {
        "builder_returns_all_kernel_fields": returned_keywords
        >= {
            "recoil_coefficients",
            "transfer_coefficients",
            "fitted_defaults",
        },
        "main_asserts_recoil_coefficients":
            "recoil_coefficients" in main_attributes,
        "main_asserts_transfer_coefficients":
            "transfer_coefficients" in main_attributes,
        "zero_default_form": zero_default_form,
    }
    if not all(evidence.values()):
        raise ValueError(f"Cycle-768 frozen-kernel AST contract changed: {evidence}")
    kernel = {
        "recoil_coefficients": tuple(
            frozen_one for _component in range(recoil_count)
        ),
        "transfer_coefficients": tuple(
            frozen_one for _entry in range(transfer_count)
        ),
        "fitted_defaults": tuple(
            Fraction() for _entry in range(recoil_count + transfer_count)
        ),
    }
    audit = {
        "evidence": evidence,
        "extraction_mode": "text/AST only; primary never imported or executed",
        "frozen_unit_coefficient": frozen_one,
        "recoil_count": recoil_count,
        "transfer_count": transfer_count,
    }
    return kernel, audit


def extract_cycle771_pair(source: str) -> tuple[int, int]:
    tree = ast.parse(source, filename=PRIMARY_TEXT_PATHS[1])
    assignment = named_assignment(tree, "DIRECT_CHANNEL_PAIR")
    value = ast.literal_eval(assignment.value)
    if not (
        isinstance(value, tuple)
        and len(value) == 2
        and all(isinstance(item, int) for item in value)
    ):
        raise ValueError("Cycle-771 direct pair is not a literal integer pair")
    return value


def extract_cycle774_structure(source: str) -> dict[str, object]:
    tree = ast.parse(source, filename=PRIMARY_TEXT_PATHS[2])
    function = named_function(tree, "vertex_structure_audit")
    strings = tuple(
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    )
    joined = " ".join(strings)
    fragments = (
        "(matter,mediator,auxiliary)=(REVERSE[d],d,d)",
        "distinct source columns cannot share a branch cell",
    )
    return {
        "ast_function": function.name,
        "fragments": {
            fragment: fragment in joined for fragment in fragments
        },
        "mode": "text/AST evidence only",
        "passed": all(fragment in joined for fragment in fragments),
    }


def extract_u320_row_contract(source: str) -> dict[str, object]:
    tree = ast.parse(source, filename=AUDIT_INPUT_PATHS[0])
    function = named_function(tree, "local_route_controls")
    loops = []
    for node in ast.walk(function):
        if (
            isinstance(node, ast.For)
            and isinstance(node.target, ast.Name)
            and node.target.id == "direction"
            and isinstance(node.iter, ast.Call)
            and isinstance(node.iter.func, ast.Name)
            and node.iter.func.id == "range"
            and len(node.iter.args) == 1
        ):
            loops.append(ast.literal_eval(node.iter.args[0]))
    append_count = sum(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "response_rows"
        and node.func.attr == "append"
        for node in ast.walk(function)
    )
    direction_count = len(U320.c210.DIRECTIONS)
    return {
        "direction_count": direction_count,
        "range_bounds": tuple(loops),
        "response_rows_append_sites": append_count,
        "passed": direction_count in loops and append_count == 1,
    }


def declared_family() -> tuple[dict[str, object], ...]:
    direction_count = len(U320.c210.DIRECTIONS)
    groups = (
        ("single", tuple(combinations(range(direction_count), 1))),
        ("pair", tuple(combinations(range(direction_count), 2))),
        ("triple", tuple(combinations(range(direction_count), 3))),
        ("quadruple", tuple(combinations(range(direction_count), 4))),
        ("quintuple", tuple(combinations(range(direction_count), 5))),
        ("full", (tuple(range(direction_count)),)),
    )
    rows = []
    for group, configurations in groups:
        for channels in configurations:
            rows.append(
                {
                    "channels": channels,
                    "composition":
                        "unnormalized identity-column mixture (sum of rows)",
                    "input_row_variants": channels,
                    "member_id":
                        f"{group}:" + "-".join(str(value) for value in channels),
                    "subset_size": len(channels),
                }
            )
    return tuple(rows)


def landed_defining_rows() -> tuple[tuple[tuple[Fraction, ...], ...], ...]:
    directions = U320.c210.DIRECTIONS
    rows = []
    for channel in range(len(directions)):
        source = tuple(Fraction(int(value)) for value in directions[channel])
        target = tuple(
            Fraction(int(value))
            for value in directions[U320.REVERSE[channel]]
        )
        rows.append(
            (
                tuple(
                    final - initial for final, initial in zip(target, source)
                ),
                source,
                source,
            )
        )
    return tuple(rows)


PREDICTION_FUNCTION_NAMES = (
    "add_response_rows",
    "apply_frozen_recoil",
    "predict_full_family",
)
PREDICTION_SOURCE = """
def add_response_rows(rows):
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


def apply_frozen_recoil(coefficients, defaults, response_row):
    return tuple(
        tuple(
            coefficient * value + default
            for value in vector
        )
        for coefficient, default, vector in zip(
            coefficients, defaults, response_row
        )
    )


def predict_full_family(coefficients, defaults, family, defining_rows):
    output = []
    for member in family:
        channels = member["channels"]
        input_rows = tuple(defining_rows[channel] for channel in channels)
        variant_rows = tuple(
            apply_frozen_recoil(coefficients, defaults, row)
            for row in input_rows
        )
        composition_row = add_response_rows(input_rows)
        output.append(
            {
                "channels": channels,
                "configuration_rows": composition_row,
                "input_row_variants": variant_rows,
                "member_id": member["member_id"],
                "predicted_rows": apply_frozen_recoil(
                    coefficients, defaults, composition_row
                ),
            }
        )
    return tuple(output)
"""


SIMULATION_FUNCTION_NAMES = (
    "probability_fraction",
    "simulate_full_family",
)
SIMULATION_SOURCE = """
def probability_fraction(amplitude):
    real = float(amplitude.real)
    imaginary = float(amplitude.imag)
    return Fraction.from_float(real * real + imaginary * imaginary)


def simulate_full_family(surface, family):
    exchange, vertex, charge, momenta = surface.link_recoil_vertex(surface.ANGLE)
    directions = surface.c210.DIRECTIONS
    direction_count = len(directions)
    axis_count = len(next(iter(directions)))
    dimension = next(iter(vertex.shape))
    identity = surface.np.eye(dimension, dtype=complex)
    shape = tuple(direction_count for axis in range(axis_count))
    output = []
    for member in family:
        channels = member["channels"]
        input_columns = identity[:, channels]
        output_columns = vertex @ input_columns
        rows_by_channel = []
        transfer_weights = []
        branch_support = []
        for column_index, source_channel in enumerate(channels):
            output_column = output_columns[:, column_index]
            branch = output_column[direction_count:].reshape(shape)
            weight = sum(
                (probability_fraction(amplitude) for amplitude in branch.flat),
                start=Fraction(),
            )
            matter = [Fraction() for axis in range(axis_count)]
            mediator = [Fraction() for axis in range(axis_count)]
            auxiliary = [Fraction() for axis in range(axis_count)]
            support = Fraction()
            for matter_channel in range(direction_count):
                for mediator_channel in range(direction_count):
                    for auxiliary_channel in range(direction_count):
                        probability = probability_fraction(
                            branch[
                                matter_channel,
                                mediator_channel,
                                auxiliary_channel,
                            ]
                        )
                        support += bool(probability)
                        for axis in range(axis_count):
                            matter[axis] += probability * Fraction(
                                int(directions[matter_channel, axis])
                                - int(directions[source_channel, axis])
                            )
                            mediator[axis] += probability * Fraction(
                                int(directions[mediator_channel, axis])
                            )
                            auxiliary[axis] += probability * Fraction(
                                int(directions[auxiliary_channel, axis])
                            )
            rows_by_channel.append(
                (
                    tuple(value / weight for value in matter),
                    tuple(value / weight for value in mediator),
                    tuple(value / weight for value in auxiliary),
                )
            )
            transfer_weights.append(weight)
            branch_support.append(support)
        exemplar = next(iter(rows_by_channel))
        combined = tuple(
            tuple(
                sum(
                    (row[component][axis] for row in rows_by_channel),
                    start=Fraction(),
                )
                for axis in range(len(exemplar[component]))
            )
            for component in range(len(exemplar))
        )
        output.append(
            {
                "branch_support": tuple(branch_support),
                "channels": channels,
                "input_row_variants": tuple(rows_by_channel),
                "member_id": member["member_id"],
                "simulated_rows": combined,
                "transfer_weights": tuple(transfer_weights),
            }
        )
    return tuple(output)
"""


def path_ast_audit(
    source: str,
    function_names: tuple[str, ...],
    forbidden_fragments: tuple[str, ...],
    filename: str,
) -> dict[str, object]:
    tree = ast.parse(source, filename=filename)
    selected = tuple(named_function(tree, name) for name in function_names)
    numeric_literals = []
    forbidden_references = []
    for function in selected:
        for node in ast.walk(function):
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
    return {
        "evaluation_functions": function_names,
        "forbidden_fragments": forbidden_fragments,
        "forbidden_references": tuple(forbidden_references),
        "numeric_literals": tuple(numeric_literals),
        "passed": (
            len(selected) == len(function_names)
            and not numeric_literals
            and not forbidden_references
        ),
    }


def compile_prediction():
    audit = path_ast_audit(
        PREDICTION_SOURCE,
        PREDICTION_FUNCTION_NAMES,
        (
            "amplitude",
            "angle",
            "evaluate",
            "link_recoil",
            "probability",
            "simulation",
            "surface",
            "vertex",
        ),
        "<cycle778-prediction-path>",
    )
    namespace = {
        "__builtins__": {
            "iter": iter,
            "len": len,
            "next": next,
            "range": range,
            "sum": sum,
            "tuple": tuple,
            "zip": zip,
        },
        "Fraction": Fraction,
    }
    exec(
        compile(
            ast.parse(PREDICTION_SOURCE),
            "<cycle778-prediction-path>",
            "exec",
        ),
        namespace,
    )
    return namespace["predict_full_family"], audit


def compile_simulation(kernel: dict[str, object]):
    audit = path_ast_audit(
        SIMULATION_SOURCE,
        SIMULATION_FUNCTION_NAMES,
        (
            "coefficient",
            "comparator",
            "default",
            "kernel",
            "prediction",
            "768",
        ),
        "<cycle778-simulation-path>",
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
    literal_overlap = tuple(
        row
        for row in audit["numeric_literals"]  # type: ignore[union-attr]
        if Fraction(row["value"]) in kernel_values
    )
    audit["literal_kernel_overlap"] = literal_overlap
    audit["passed"] = bool(audit["passed"]) and not literal_overlap
    namespace = {
        "__builtins__": {
            "bool": bool,
            "complex": complex,
            "enumerate": enumerate,
            "float": float,
            "int": int,
            "iter": iter,
            "len": len,
            "next": next,
            "range": range,
            "sum": sum,
            "tuple": tuple,
        },
        "Fraction": Fraction,
    }
    exec(
        compile(
            ast.parse(SIMULATION_SOURCE),
            "<cycle778-simulation-path>",
            "exec",
        ),
        namespace,
    )
    return namespace["simulate_full_family"], audit


def self_import_and_mutation_audit(source: str) -> dict[str, object]:
    tree = ast.parse(source, filename=str(Path(__file__)))
    imported_aliases = {}
    imported_roots = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_roots.append(alias.name)
                if alias.asname in {"H749", "S322", "U320"}:
                    imported_aliases[alias.asname] = alias.name
    assignment = named_assignment(tree, "AUDIT_INPUT_PATHS")
    literal_paths = ()
    if (
        isinstance(assignment.value, ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in assignment.value.elts
        )
    ):
        literal_paths = tuple(
            element.value for element in assignment.value.elts
        )
    writes = []
    imported_surface_names = {"H749", "S322", "U320"}
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
            if isinstance(root, ast.Name) and root.id in imported_surface_names:
                writes.append(
                    {"kind": "write", "line": node.lineno, "module": root.id}
                )
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"delattr", "setattr"}
            and node.args
        ):
            root = node.args[0]
            while isinstance(root, (ast.Attribute, ast.Subscript)):
                root = root.value
            if isinstance(root, ast.Name) and root.id in imported_surface_names:
                writes.append(
                    {
                        "kind": node.func.id,
                        "line": node.lineno,
                        "module": root.id,
                    }
                )
    expected_aliases = {
        "H749": "frontier_cycle749_response_comparison_harness_2026_07_28",
        "S322": "two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18",
        "U320": "unit_weight_carried_link_recoil_cycle320_2026_07_18",
    }
    return {
        "blocked_imports": tuple(
            name for name in imported_roots if name in BLOCKLISTED_MODULES
        ),
        "imported_landed_aliases": imported_aliases,
        "literal_audit_input_paths": literal_paths,
        "passed": (
            literal_paths == AUDIT_INPUT_PATHS
            and imported_aliases == expected_aliases
            and not writes
            and not any(
                name in BLOCKLISTED_MODULES for name in imported_roots
            )
        ),
        "surface_writes": tuple(writes),
    }


def attachment_table(
    predictions: tuple[dict[str, object], ...],
    simulations: tuple[dict[str, object], ...],
) -> tuple[dict[str, object], ...]:
    if len(predictions) != len(simulations):
        raise ValueError("prediction and simulation table lengths differ")
    rows = []
    for predicted, simulated in zip(predictions, simulations):
        if (
            predicted["member_id"] != simulated["member_id"]
            or predicted["channels"] != simulated["channels"]
        ):
            raise ValueError("prediction and simulation member order differs")
        channels = predicted["channels"]
        predicted_variants = predicted["input_row_variants"]
        simulated_variants = simulated["input_row_variants"]
        if not (
            isinstance(channels, tuple)
            and isinstance(predicted_variants, tuple)
            and isinstance(simulated_variants, tuple)
        ):
            raise TypeError("attachment member has malformed variant rows")
        variant_rows = tuple(
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
                    and len(variant_rows) == len(channels)
                    and all(row["exact_match"] for row in variant_rows)
                ),
                "input_row_variants": variant_rows,
                "member_id": predicted["member_id"],
                "predicted_rows": predicted["predicted_rows"],
                "simulated_rows": simulated["simulated_rows"],
            }
        )
    return tuple(rows)


def instrument_reverdict(kernel: dict[str, object]) -> dict[str, object]:
    submitted = H749.ResponseKernelCandidate(
        name="cycle778_frozen_cycle768_kernel",
        recoil_coefficients=kernel["recoil_coefficients"],  # type: ignore[arg-type]
        transfer_coefficients=kernel["transfer_coefficients"],  # type: ignore[arg-type]
        fitted_defaults=kernel["fitted_defaults"],  # type: ignore[arg-type]
        demonstration_role=(
            "Cycle-778 text/AST-extracted frozen kernel; no-refit sweep"
        ),
    )
    fixtures = H749.extract_frozen_fixtures()
    evaluation = H749.evaluate_candidate(submitted, fixtures, fixtures)
    residuals = evaluation["residuals"]
    if not isinstance(residuals, dict):
        raise TypeError("Cycle-749 evaluation residuals are malformed")
    per_criterion = {
        name: (
            "ACCEPT"
            if Fraction(float(value)) <= H749.STRICT_TOLERANCE
            else "FAIL"
        )
        for name, value in sorted(residuals.items())
    }
    return {
        "accept_count": sum(
            verdict == "ACCEPT" for verdict in per_criterion.values()
        ),
        "criterion_count": len(per_criterion),
        "evaluation": evaluation,
        "overall_verdict": evaluation["verdict"],
        "per_criterion": per_criterion,
    }


def main() -> int:
    started = time.monotonic()
    self_source = Path(__file__).read_text(encoding="utf-8")
    input_bytes_before = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    shas_before = {
        path: sha256_bytes(data)
        for path, data in input_bytes_before.items()
    }
    blocklist_before = {
        module: module in sys.modules for module in BLOCKLISTED_MODULES
    }
    self_audit = self_import_and_mutation_audit(self_source)
    row_contract = extract_u320_row_contract(
        input_bytes_before[AUDIT_INPUT_PATHS[0]].decode("utf-8")
    )

    # The family is declared and printed before kernel extraction or simulation.
    family = declared_family()
    family_group_counts = {
        group: sum(
            str(member["member_id"]).startswith(group + ":")
            for member in family
        )
        for group in ("single", "pair", "triple",
                      "quadruple", "quintuple", "full")
    }
    input_row_variant_count = sum(
        len(member["input_row_variants"])  # type: ignore[arg-type]
        for member in family
    )
    attachment_case_count = len(family) + input_row_variant_count
    emit(
        "DECLARED FAMILY :: "
        + json.dumps(
            {
                "attachment_case_count":
                    attachment_case_count,
                "composition":
                    "unnormalized identity-column mixture (sum of rows)",
                "configuration_count": len(family),
                "family_size": len(family),
                "group_counts": family_group_counts,
                "input_row_variant_count": input_row_variant_count,
                "members": tuple(
                    {
                        "channels": member["channels"],
                        "input_row_variants":
                            member["input_row_variants"],
                        "member_id": member["member_id"],
                    }
                    for member in family
                ),
                "u320_row_contract": row_contract,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    emit(f"family_size: {len(family)}")
    emit(f"input_row_variant_count: {input_row_variant_count}")

    kernel, kernel_extraction = extract_frozen_kernel(
        input_bytes_before[PRIMARY_TEXT_PATHS[0]].decode("utf-8")
    )
    cycle771_pair = extract_cycle771_pair(
        input_bytes_before[PRIMARY_TEXT_PATHS[1]].decode("utf-8")
    )
    cycle774_structure = extract_cycle774_structure(
        input_bytes_before[PRIMARY_TEXT_PATHS[2]].decode("utf-8")
    )
    kernel_snapshot = tuple(
        (key, kernel[key])
        for key in (
            "recoil_coefficients",
            "transfer_coefficients",
            "fitted_defaults",
        )
    )
    emit(
        "FROZEN KERNEL :: "
        + json.dumps(
            {
                **kernel,
                "extraction": kernel_extraction,
                "no_refit": True,
            },
            sort_keys=True,
            separators=(",", ":"),
            default=jsonable,
        )
    )

    defining_rows = landed_defining_rows()
    predict_full_family, prediction_firewall = compile_prediction()
    simulate_full_family, simulation_firewall = compile_simulation(kernel)
    predictions = predict_full_family(
        kernel["recoil_coefficients"],
        kernel["fitted_defaults"][:len(kernel["recoil_coefficients"])],
        family,
        defining_rows,
    )
    prediction_rerun = predict_full_family(
        kernel["recoil_coefficients"],
        kernel["fitted_defaults"][:len(kernel["recoil_coefficients"])],
        family,
        defining_rows,
    )
    simulations = simulate_full_family(U320, family)
    simulation_rerun = simulate_full_family(U320, family)
    attachments = attachment_table(predictions, simulations)
    for row in attachments:
        emit(
            "ATTACHMENT MEMBER :: "
            + json.dumps(
                row,
                sort_keys=True,
                separators=(",", ":"),
                default=jsonable,
            )
        )

    match_count = sum(bool(row["exact_match"]) for row in attachments)
    attachment_complete = match_count == len(family) and bool(family)
    mismatches = tuple(
        row for row in attachments if not row["exact_match"]
    )
    emit(
        "ATTACHMENT VERDICT :: "
        + json.dumps(
            {
                "complete": attachment_complete,
                "family_size": len(family),
                "match_count": match_count,
                "mismatch_count": len(mismatches),
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    if attachment_complete:
        emit("no_refit_attachment_complete_at_fixture_scope: true")
        emit("response_law_established: false")
        emit(
            'w7_fixture_scope_status: "kernel + structural additivity '
            "reproduce the full bounded family; the remaining W7 content "
            "is scope (other surfaces, extended charts), not fixture-scope "
            'content"'
        )
    else:
        emit(
            "KERNEL REFUTED FULL DIFF :: "
            + json.dumps(
                mismatches,
                sort_keys=True,
                separators=(",", ":"),
                default=jsonable,
            )
        )
        emit(f"kernel_refuted_at: {mismatches[0]['member_id']}")
        emit("no_refit_attachment_complete_at_fixture_scope: false")
        emit("response_law_established: false")

    cycle771_member = next(
        row for row in attachments if row["channels"] == cycle771_pair
    )
    cycle771_control = (
        cycle771_member["exact_match"]
        and str(cycle771_member["member_id"]).startswith("pair:")
    )
    emit(
        "CYCLE 771 PAIR CONTROL :: "
        + json.dumps(
            {
                "channels": cycle771_pair,
                "exact_match": cycle771_control,
                "predicted_rows": cycle771_member["predicted_rows"],
                "simulated_rows": cycle771_member["simulated_rows"],
            },
            sort_keys=True,
            separators=(",", ":"),
            default=jsonable,
        )
    )

    recoil = kernel["recoil_coefficients"]
    perturbed_recoil = tuple(
        -value if index == 0 else value
        for index, value in enumerate(recoil)
    )
    perturbed_predictions = predict_full_family(
        perturbed_recoil,
        kernel["fitted_defaults"][:len(perturbed_recoil)],
        family,
        defining_rows,
    )
    perturbed_attachments = attachment_table(
        perturbed_predictions, simulations
    )
    perturbed_failure = next(
        (
            row
            for row in perturbed_attachments
            if not row["exact_match"]
        ),
        None,
    )
    emit(
        "PERTURBED KERNEL CONTROL :: "
        + json.dumps(
            {
                "coefficient_index_flipped": 0,
                "failed_at": (
                    perturbed_failure["member_id"]
                    if perturbed_failure is not None else None
                ),
                "frozen_recoil_coefficients": recoil,
                "perturbed_recoil_coefficients": perturbed_recoil,
                "sweep_failed": perturbed_failure is not None,
            },
            sort_keys=True,
            separators=(",", ":"),
            default=jsonable,
        )
    )

    instrument = instrument_reverdict(kernel)
    emit(
        "CYCLE 749 INSTRUMENT RE-VERDICT :: "
        + json.dumps(
            instrument,
            sort_keys=True,
            separators=(",", ":"),
            default=jsonable,
        )
    )

    input_bytes_after = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    shas_after = {
        path: sha256_bytes(data)
        for path, data in input_bytes_after.items()
    }
    blocklist_after = {
        module: module in sys.modules for module in BLOCKLISTED_MODULES
    }
    landed_text = " ".join(
        " ".join(
            input_bytes_before[path].decode("utf-8").split()
        )
        for path in AUDIT_INPUT_PATHS[:3]
    )
    c_source_ok = (
        C_source == H749.C_source[:4]
        and all(
            " ".join(statement.split()) in landed_text
            for statement in C_source
        )
    )
    kernel_untouched = kernel_snapshot == tuple(
        (key, kernel[key])
        for key in (
            "recoil_coefficients",
            "transfer_coefficients",
            "fitted_defaults",
        )
    )
    deterministic = (
        predictions == prediction_rerun
        and simulations == simulation_rerun
        and attachment_table(prediction_rerun, simulation_rerun)
        == attachments
    )
    full_simulation_ok = (
        len(simulations) == len(family)
        and all(
            len(row["branch_support"]) == len(row["channels"])  # type: ignore[arg-type]
            and all(
                support == Fraction(True)
                for support in row["branch_support"]  # type: ignore[union-attr]
            )
            and all(
                weight > Fraction()
                for weight in row["transfer_weights"]  # type: ignore[union-attr]
            )
            for row in simulations
        )
    )
    instrument_six_of_six = (
        instrument["overall_verdict"] == "ACCEPT"
        and instrument["accept_count"] == 6
        and instrument["criterion_count"] == 6
        and not instrument["evaluation"]["failed_criteria"]  # type: ignore[index]
    )

    certificate(
        "A anchors + blocklist + AST firewalls",
        (
            shas_before == EXPECTED_SHA256
            and shas_after == EXPECTED_SHA256
            and shas_after == shas_before
            and not any(blocklist_before.values())
            and not any(blocklist_after.values())
            and bool(self_audit["passed"])
            and bool(prediction_firewall["passed"])
            and bool(simulation_firewall["passed"])
            and bool(kernel_extraction["evidence"])
            and bool(cycle774_structure["passed"])
            and c_source_ok
        ),
        {
            "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
            "blocklist_after": blocklist_after,
            "blocklist_before": blocklist_before,
            "C_source": C_source,
            "C_source_verbatim": c_source_ok,
            "cycle774_structure_ast": cycle774_structure,
            "kernel_extraction": kernel_extraction,
            "prediction_path_firewall": prediction_firewall,
            "sha256": shas_after,
            "simulation_path_firewall": simulation_firewall,
            "source_import_and_mutation_ast": self_audit,
        },
    )
    certificate(
        "B declared family + constant-free frozen predictions",
        (
            family_group_counts
            == {"single": 6, "pair": 15, "triple": 20,
                "quadruple": 15, "quintuple": 6, "full": 1}
            and len(family) == 63
            and input_row_variant_count == 192
            and attachment_case_count == 255
            and bool(row_contract["passed"])
            and len(defining_rows) == len(U320.c210.DIRECTIONS)
            and len(predictions) == len(family)
            and not prediction_firewall["numeric_literals"]
            and kernel_untouched
            and all(
                value == Fraction()
                for value in kernel["fitted_defaults"]
            )
        ),
        {
            "attachment_case_count": attachment_case_count,
            "configuration_count": len(family),
            "frozen_kernel_untouched": kernel_untouched,
            "group_counts": family_group_counts,
            "input_row_variant_count": input_row_variant_count,
            "no_refit": True,
            "prediction_path_numeric_literals":
                prediction_firewall["numeric_literals"],
            "u320_row_contract": row_contract,
        },
    )
    certificate(
        "C full direct simulation sweep",
        full_simulation_ok,
        {
            "configuration_count": len(simulations),
            "direct_vertex_applications": len(simulations),
            "input_column_variants": sum(
                len(row["channels"])  # type: ignore[arg-type]
                for row in simulations
            ),
            "probability_bookkeeping": "exact Fraction branch conditioning",
            "simulation_path_has_kernel_constants":
                bool(simulation_firewall["literal_kernel_overlap"]),
            "simulation_path_has_kernel_references":
                bool(simulation_firewall["forbidden_references"]),
        },
    )
    certificate(
        "D attachment table verdict + honest keys",
        (
            attachment_complete
            and match_count == len(family)
            and not mismatches
        ),
        {
            "family_size": len(family),
            "match_count": match_count,
            "no_refit_attachment_complete_at_fixture_scope":
                attachment_complete,
            "response_law_established": False,
            "w7_fixture_scope_status": (
                "kernel + structural additivity reproduce the full bounded "
                "family; the remaining W7 content is scope (other surfaces, "
                "extended charts), not fixture-scope content"
                if attachment_complete else "kernel refuted at fixture scope"
            ),
        },
    )

    runtime = time.monotonic() - started
    projected_stdout_bytes = STDOUT_BYTES + 20_000
    certificate(
        "E instrument + sensitivity + determinism + bounds",
        (
            instrument_six_of_six
            and cycle771_control
            and perturbed_failure is not None
            and deterministic
            and kernel_untouched
            and runtime < AUDIT_TIMEOUT_SEC
            and projected_stdout_bytes < OUTPUT_LIMIT_BYTES
        ),
        {
            "cycle749_instrument_accept_count":
                instrument["accept_count"],
            "cycle749_instrument_criterion_count":
                instrument["criterion_count"],
            "cycle749_instrument_verdict":
                instrument["overall_verdict"],
            "cycle771_pair": cycle771_pair,
            "cycle771_pair_reproduced": cycle771_control,
            "determinism": deterministic,
            "kernel_untouched": kernel_untouched,
            "perturbed_kernel_failed_at": (
                perturbed_failure["member_id"]
                if perturbed_failure is not None else None
            ),
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": runtime,
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
                "family_size": len(family),
                "match_count": match_count,
                "no_refit_attachment_complete_at_fixture_scope":
                    attachment_complete,
                "pass": PASS,
                "response_law_established": False,
                "runtime_sec": final_runtime,
                "stdout_bytes": STDOUT_BYTES,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
