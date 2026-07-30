#!/usr/bin/env python3
"""Cycle 771: direct no-refit verification of the Cycle-768 extension probe."""

AUDIT_TIMEOUT_SEC = 1500
OUTPUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
)
COMPARATOR_PATH = (
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py"
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706",
    AUDIT_INPUT_PATHS[1]:
        "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75",
    COMPARATOR_PATH:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle768_response_law_candidate_2026_07_28",
)
DIRECT_CHANNEL_PAIR = (0, 2)

import ast
from fractions import Fraction
import hashlib
from itertools import combinations
import json
from pathlib import Path
from types import SimpleNamespace
import sys
import time

import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322
import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
STDOUT_BYTES = 0

# Verbatim operative declarations from the two landed modules.
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


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    prefix = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    rendered = json.dumps(
        detail, sort_keys=True, separators=(",", ":"), default=jsonable
    )
    emit(f"{prefix} {label} :: {rendered}")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def extract_frozen_comparator(
    source: str,
) -> tuple[dict[str, object], dict[str, object]]:
    """Execute only the comparator-producing AST, never the Cycle-768 module."""
    tree = ast.parse(source, filename=COMPARATOR_PATH)
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }
    selected_names = (
        "fraction_text",
        "vector_tuple",
        "recoil_configuration",
        "extension_probe",
    )
    selected = [functions[name] for name in selected_names]
    main_node = functions["main"]
    one_assignments = [
        node
        for node in ast.walk(main_node)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "derived_one"
            for target in node.targets
        )
    ]
    if len(one_assignments) != 1:
        raise ValueError("Cycle-768 frozen unit-coefficient assertion is not unique")
    one_call = one_assignments[0].value
    if not (
        isinstance(one_call, ast.Call)
        and isinstance(one_call.func, ast.Name)
        and one_call.func.id == "Fraction"
        and len(one_call.args) == 1
    ):
        raise ValueError("Cycle-768 frozen unit coefficient has changed form")
    frozen_one = Fraction(ast.literal_eval(one_call.args[0]))
    assertion_names = {
        node.id for node in ast.walk(main_node) if isinstance(node, ast.Name)
    }
    assertion_attributes = {
        node.attr
        for node in ast.walk(main_node)
        if isinstance(node, ast.Attribute)
    }
    if (
        "derived_one" not in assertion_names
        or "recoil_coefficients" not in assertion_attributes
    ):
        raise ValueError("Cycle-768 unit-coefficient assertion is absent")

    extracted_module = ast.Module(body=selected, type_ignores=[])
    ast.fix_missing_locations(extracted_module)
    safe_builtins = {
        "all": all,
        "any": any,
        "bool": bool,
        "dict": dict,
        "float": float,
        "int": int,
        "isinstance": isinstance,
        "len": len,
        "object": object,
        "range": range,
        "reversed": reversed,
        "str": str,
        "sum": sum,
        "tuple": tuple,
        "zip": zip,
    }
    namespace = {
        "__builtins__": safe_builtins,
        "combinations": combinations,
        "DerivedKernel": object,
        "Fraction": Fraction,
        "U320": U320,
    }
    exec(
        compile(
            extracted_module,
            filename=f"{COMPARATOR_PATH}:text-ast-only",
            mode="exec",
        ),
        namespace,
    )
    first_channel = next(iter(range(len(U320.c210.DIRECTIONS))))
    component_count = len(namespace["recoil_configuration"](first_channel))
    frozen_candidate = SimpleNamespace(
        recoil_coefficients=tuple(
            frozen_one for _component in range(component_count)
        )
    )
    extension = namespace["extension_probe"](frozen_candidate)
    if not (
        extension["reached"]
        and extension["determinate"]
        and extension["outside_defining_set"]
        and not extension["prediction_verified"]
    ):
        raise ValueError("Cycle-768 extension probe is no longer frozen/unverified")
    comparator = {
        "channel_pair": tuple(extension["selected_channel_pair"]),
        "configuration": tuple(
            tuple(Fraction(value) for value in row)
            for row in extension["configuration"]
        ),
        "prediction": tuple(
            tuple(Fraction(value) for value in row)
            for row in extension["prediction"]
        ),
    }
    audit = {
        "blocklisted_module": BLOCKLISTED_MODULES[0],
        "extracted_functions": selected_names,
        "frozen_recoil_coefficient": frozen_one,
        "mode": "text/AST comparator extraction only",
        "module_imported": BLOCKLISTED_MODULES[0] in sys.modules,
    }
    return comparator, audit


SIMULATION_FUNCTION_NAMES = (
    "probability_fraction",
    "evaluate_channels",
)
SIMULATION_SOURCE = """
def probability_fraction(amplitude):
    real = float(amplitude.real)
    imaginary = float(amplitude.imag)
    return Fraction.from_float(real * real + imaginary * imaginary)


def evaluate_channels(surface, channels):
    exchange, vertex, charge, momenta = surface.link_recoil_vertex(surface.ANGLE)
    directions = surface.c210.DIRECTIONS
    direction_count = len(directions)
    first_channel = next(iter(channels))
    axis_count = len(directions[first_channel])
    dimension = next(iter(vertex.shape))
    identity = surface.np.eye(dimension, dtype=complex)
    input_columns = identity[:, tuple(channels)]
    output_columns = vertex @ input_columns
    rows_by_channel = []
    transfer_weights = []
    branch_support = []
    shape = tuple(direction_count for axis in range(axis_count))
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
    return {
        "branch_support": tuple(branch_support),
        "channel_rows": tuple(rows_by_channel),
        "rows": combined,
        "transfer_weights": tuple(transfer_weights),
    }
"""


def compile_simulation(
    comparator_values: tuple[tuple[Fraction, ...], ...],
):
    tree = ast.parse(SIMULATION_SOURCE, filename="<cycle771-simulation-path>")
    selected = tuple(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name in SIMULATION_FUNCTION_NAMES
    )
    numeric_literals = []
    forbidden_references = []
    forbidden_fragments = ("kernel", "prediction", "comparator", "768")
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
    flat_comparator_values = {
        value
        for row in comparator_values
        for value in row
    }
    literal_value_overlap = [
        row
        for row in numeric_literals
        if Fraction(row["value"]) in flat_comparator_values
    ]
    audit = {
        "evaluation_functions": tuple(
            sorted(function.name for function in selected)
        ),
        "forbidden_references": forbidden_references,
        "literal_value_overlap": literal_value_overlap,
        "numeric_literals": numeric_literals,
        "passed": (
            len(selected) == len(SIMULATION_FUNCTION_NAMES)
            and not forbidden_references
            and not numeric_literals
            and not literal_value_overlap
        ),
    }
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
    exec(compile(tree, "<cycle771-simulation-path>", "exec"), namespace)
    return namespace["evaluate_channels"], audit


def landed_defining_row(
    surface: object, channel: int
) -> tuple[tuple[Fraction, ...], ...]:
    directions = surface.c210.DIRECTIONS
    source = tuple(Fraction(int(value)) for value in directions[channel])
    target = tuple(
        Fraction(int(value))
        for value in directions[surface.REVERSE[channel]]
    )
    return (
        tuple(final - initial for final, initial in zip(target, source)),
        source,
        source,
    )


def row_diff(
    simulated: tuple[tuple[Fraction, ...], ...],
    expected: tuple[tuple[Fraction, ...], ...],
) -> tuple[dict[str, object], ...]:
    labels = ("matter_recoil", "mediator_flux", "auxiliary_flux")
    rows = []
    for index, (actual_row, expected_row) in enumerate(
        zip(simulated, expected)
    ):
        rows.append(
            {
                "component": labels[index],
                "entry_diff": tuple(
                    actual - frozen
                    for actual, frozen in zip(actual_row, expected_row)
                ),
                "match": actual_row == expected_row,
                "simulated": actual_row,
                "frozen_prediction": expected_row,
            }
        )
    return tuple(rows)


def main() -> int:
    started = time.monotonic()
    input_bytes_before = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
    }
    comparator_bytes = (ROOT / COMPARATOR_PATH).read_bytes()
    shas_before = {
        **{
            path: sha256_bytes(data)
            for path, data in input_bytes_before.items()
        },
        COMPARATOR_PATH: sha256_bytes(comparator_bytes),
    }
    blocklist_before = {
        name: name in sys.modules for name in BLOCKLISTED_MODULES
    }

    frozen, extraction_audit = extract_frozen_comparator(
        comparator_bytes.decode("utf-8")
    )
    emit(
        "frozen_configuration: "
        + json.dumps(frozen["configuration"], default=jsonable)
    )
    emit(
        "frozen_prediction: "
        + json.dumps(frozen["prediction"], default=jsonable)
    )
    emit(
        "frozen_channel_pair: "
        + json.dumps(frozen["channel_pair"], default=jsonable)
    )

    evaluate_channels, firewall = compile_simulation(frozen["prediction"])
    simulation = evaluate_channels(U320, DIRECT_CHANNEL_PAIR)
    deterministic_rerun = evaluate_channels(U320, DIRECT_CHANNEL_PAIR)

    defining_channel = next(iter(DIRECT_CHANNEL_PAIR))
    defining_expected = landed_defining_row(U320, defining_channel)
    defining_simulation = evaluate_channels(U320, (defining_channel,))
    defining_ok = (
        defining_simulation["rows"] == defining_expected
        and all(
            support == Fraction(True)
            for support in defining_simulation["branch_support"]
        )
        and all(
            weight > Fraction()
            for weight in defining_simulation["transfer_weights"]
        )
    )

    perturbed_pair = (
        DIRECT_CHANNEL_PAIR[0],
        U320.REVERSE[DIRECT_CHANNEL_PAIR[1]],
    )
    perturbed = evaluate_channels(U320, perturbed_pair)
    perturbed_ok = (
        perturbed_pair != DIRECT_CHANNEL_PAIR
        and perturbed["rows"] != frozen["prediction"]
    )
    deterministic_ok = simulation == deterministic_rerun

    simulated_rows = simulation["rows"]
    comparison_rows = row_diff(simulated_rows, frozen["prediction"])
    prediction_verified = simulated_rows == frozen["prediction"]
    verdict = "VERIFIED" if prediction_verified else "REFUTED"

    input_bytes_after = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
    }
    comparator_bytes_after = (ROOT / COMPARATOR_PATH).read_bytes()
    shas_after = {
        **{
            path: sha256_bytes(data)
            for path, data in input_bytes_after.items()
        },
        COMPARATOR_PATH: sha256_bytes(comparator_bytes_after),
    }
    blocklist_after = {
        name: name in sys.modules for name in BLOCKLISTED_MODULES
    }
    normalized_landed_text = " ".join(
        data.decode("utf-8")
        for data in input_bytes_before.values()
    )
    normalized_landed_text = " ".join(normalized_landed_text.split())

    check(
        "A landed SHA anchors unchanged; Cycle-768 blocklisted text/AST only",
        shas_before == EXPECTED_SHA256
        and shas_after == EXPECTED_SHA256
        and shas_after == shas_before
        and not any(blocklist_before.values())
        and not any(blocklist_after.values())
        and not extraction_audit["module_imported"]
        and callable(U320.link_recoil_vertex)
        and callable(S322.response_matrix)
        and frozen["channel_pair"] == DIRECT_CHANNEL_PAIR,
        {
            "audit_input_paths": AUDIT_INPUT_PATHS,
            "blocklist_after": blocklist_after,
            "blocklist_before": blocklist_before,
            "comparator_extraction": extraction_audit,
            "sha256": shas_after,
        },
    )
    check(
        "B simulation-path AST firewall",
        bool(firewall["passed"]),
        firewall,
    )
    check(
        "C defining-row calibration reproduces landed row",
        defining_ok,
        {
            "channel": defining_channel,
            "landed_row": defining_expected,
            "simulated_row": defining_simulation["rows"],
            "transfer_weights": defining_simulation["transfer_weights"],
        },
    )
    check(
        f"D comparison verdict {verdict}",
        verdict in {"VERIFIED", "REFUTED"}
        and len(comparison_rows) == len(frozen["prediction"]),
        {
            "channel_pair": DIRECT_CHANNEL_PAIR,
            "diff": comparison_rows,
            "frozen_prediction": frozen["prediction"],
            "simulated_rows": simulated_rows,
        },
    )
    check(
        "E perturbation control and determinism",
        perturbed_ok and deterministic_ok,
        {
            "deterministic": deterministic_ok,
            "perturbed_channel_pair": perturbed_pair,
            "perturbed_rows": perturbed["rows"],
            "perturbation_does_not_match": perturbed_ok,
        },
    )
    check(
        "E C_source firewall declarations are verbatim landed text",
        all(
            " ".join(statement.split()) in normalized_landed_text
            for statement in C_source
        ),
        {"C_source": C_source},
    )

    emit(f"prediction_verified: {str(prediction_verified).lower()}")
    emit("response_law_established: false")
    emit("w7_closed: false")

    runtime = time.monotonic() - started
    certificate = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "certificate_A": {
            "blocklisted_text_ast_only": not any(blocklist_after.values()),
            "sha256": shas_after,
        },
        "certificate_B": firewall,
        "certificate_C": {
            "landed_row": defining_expected,
            "passed": defining_ok,
            "simulated_row": defining_simulation["rows"],
        },
        "certificate_D": {
            "diff": comparison_rows,
            "prediction": frozen["prediction"],
            "prediction_verified": prediction_verified,
            "simulated_rows": simulated_rows,
            "verdict": verdict,
        },
        "certificate_E": {
            "deterministic": deterministic_ok,
            "perturbation_passed": perturbed_ok,
            "runtime_sec": runtime,
        },
        "fail": FAIL,
        "no_refit": True,
        "pass": PASS,
        "prediction_verified": prediction_verified,
        "response_law_established": False,
        "runtime_sec": runtime,
        "w7_closed": False,
    }
    preview = json.dumps(
        certificate, sort_keys=True, separators=(",", ":"), default=jsonable
    )
    projected_stdout_bytes = (
        STDOUT_BYTES + len(preview.encode("utf-8")) + 4096
    )
    check(
        "E runtime and stdout bounds",
        runtime < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < OUTPUT_LIMIT_BYTES,
        {
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": runtime,
            "stdout_limit_bytes": OUTPUT_LIMIT_BYTES,
            "stdout_projected_bytes": projected_stdout_bytes,
        },
    )
    certificate["fail"] = FAIL
    certificate["pass"] = PASS
    certificate["runtime_sec"] = time.monotonic() - started
    certificate["certificate_E"]["runtime_sec"] = certificate["runtime_sec"]
    emit(
        json.dumps(
            certificate,
            sort_keys=True,
            separators=(",", ":"),
            default=jsonable,
        )
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
