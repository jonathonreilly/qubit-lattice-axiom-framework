#!/usr/bin/env python3
"""Cycle 771 independent adversarial check of the composite prediction.

The two primary runners are text-only evidence.  This checker constructs its
own coherent input, amplitude support probe, exact bookkeeping, and pair
census against the landed U320/S322 surfaces.
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
FROZEN_PAIR_CENSUS = ((0, 1), (0, 2), (1, 2))

import ast
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import sys
import time

import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322
import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
STDOUT_BYTES = 0


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


def certificate(name: str, faithful: bool, finding: object) -> None:
    global PASS, FAIL
    prefix = "PASS" if faithful else "FAIL"
    if faithful:
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


def direction_tuple(index: int) -> tuple[Fraction, ...]:
    return tuple(Fraction(int(value)) for value in U320.c210.DIRECTIONS[index])


def defining_row(channel: int) -> tuple[tuple[Fraction, ...], ...]:
    source = direction_tuple(channel)
    target = direction_tuple(U320.REVERSE[channel])
    return (
        tuple(final - initial for final, initial in zip(target, source)),
        source,
        source,
    )


def add_rows(
    rows: tuple[tuple[tuple[Fraction, ...], ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    if not rows:
        raise ValueError("cannot add an empty row collection")
    return tuple(
        tuple(
            sum((row[component][axis] for row in rows), start=Fraction())
            for axis in range(len(rows[0][component]))
        )
        for component in range(len(rows[0]))
    )


def _named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one function {name!r}")
    return matches[0]


def _fraction_assignment(function: ast.FunctionDef, name: str) -> Fraction:
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
        raise ValueError(f"expected one assignment to {name!r}")
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


def extract_cycle768_frozen(source: str) -> dict[str, object]:
    """Read Cycle 768 structurally, then reproduce its frozen probe arithmetic."""
    tree = ast.parse(source, filename=PRIMARY_TEXT_PATHS[0])
    main = _named_function(tree, "main")
    recoil_function = _named_function(tree, "recoil_configuration")
    extension_function = _named_function(tree, "extension_probe")
    transfer_function = _named_function(tree, "derive_transfer_coefficients")
    derived_one = _fraction_assignment(main, "derived_one")

    main_attributes = {
        node.attr
        for node in ast.walk(main)
        if isinstance(node, ast.Attribute)
    }
    recoil_names = {
        node.id for node in ast.walk(recoil_function) if isinstance(node, ast.Name)
    }
    extension_names = {
        node.id
        for node in ast.walk(extension_function)
        if isinstance(node, ast.Name)
    }
    transfer_calls = {
        node.func.id
        for node in ast.walk(transfer_function)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    structural_evidence = {
        "main_asserts_recoil_coefficients":
            "recoil_coefficients" in main_attributes,
        "main_asserts_transfer_coefficients":
            "transfer_coefficients" in main_attributes,
        "recoil_reads_reverse_and_directions":
            {"U320", "direction"}.issubset(recoil_names),
        "extension_enumerates_combinations":
            "combinations" in extension_names,
        "transfer_constructs_reversed_endpoint_map":
            {"range", "reversed"}.issubset(transfer_calls),
    }
    if not all(structural_evidence.values()):
        raise ValueError(f"Cycle-768 AST contract changed: {structural_evidence}")

    directions = tuple(direction_tuple(index) for index in range(
        len(U320.c210.DIRECTIONS)
    ))
    landed = set(directions)
    selected = None
    for pair in combinations(range(len(directions)), 2):
        combined_source = tuple(
            left + right for left, right in zip(
                directions[pair[0]], directions[pair[1]]
            )
        )
        if any(combined_source) and combined_source not in landed:
            selected = pair
            break
    if selected is None:
        raise ValueError("Cycle-768 selection has no outside composite")

    component_rows = tuple(defining_row(channel) for channel in selected)
    configuration = add_rows(component_rows)
    recoil_coefficients = tuple(
        derived_one for _component in range(len(configuration))
    )
    transfer_coefficients = tuple(
        derived_one
        for _entry in range(len(S322.ENDPOINTS) ** 2)
    )
    prediction = tuple(
        tuple(coefficient * value for value in row)
        for coefficient, row in zip(recoil_coefficients, configuration)
    )
    return {
        "channel_pair": selected,
        "configuration": configuration,
        "prediction": prediction,
        "recoil_coefficients": recoil_coefficients,
        "transfer_coefficients": transfer_coefficients,
        "derived_one": derived_one,
        "structural_evidence": structural_evidence,
    }


def solve_exact(
    matrix: tuple[tuple[Fraction, ...], ...],
    vector: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    """Small exact Gauss-Jordan solve used for the landed recoil recount."""
    size = len(vector)
    augmented = [
        list(matrix[row]) + [vector[row]]
        for row in range(size)
    ]
    for column in range(size):
        pivot = next(
            (
                row
                for row in range(column, size)
                if augmented[row][column]
            ),
            None,
        )
        if pivot is None:
            raise ValueError("singular exact recoil normal matrix")
        augmented[column], augmented[pivot] = (
            augmented[pivot],
            augmented[column],
        )
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(
                    augmented[row], augmented[column]
                )
            ]
    return tuple(augmented[row][-1] for row in range(size))


def extract_landed_kernel() -> dict[str, object]:
    """Recover kernel weights from landed operators with independent arithmetic."""
    _exchange, _vertex, _charge, momenta = U320.link_recoil_vertex(U320.ANGLE)
    direction_count = len(U320.c210.DIRECTIONS)
    sector_count = len(momenta)
    gram = [
        [Fraction() for _right in range(sector_count)]
        for _left in range(sector_count)
    ]
    rhs = [Fraction() for _sector in range(sector_count)]
    equation_count = 0
    for configuration in product(range(direction_count), repeat=sector_count):
        flat = (
            direction_count
            + direction_count**2 * configuration[0]
            + direction_count * configuration[1]
            + configuration[2]
        )
        for axis, momentum in enumerate(momenta):
            features = tuple(
                Fraction(
                    int(U320.c210.DIRECTIONS[configuration[sector], axis])
                )
                for sector in range(sector_count)
            )
            target = Fraction(
                int(round(float(momentum[flat, flat].real)))
            )
            for left in range(sector_count):
                rhs[left] += features[left] * target
                for right in range(sector_count):
                    gram[left][right] += (
                        features[left] * features[right]
                    )
            equation_count += 1
    recoil = solve_exact(
        tuple(tuple(row) for row in gram), tuple(rhs)
    )

    endpoint_count = len(S322.ENDPOINTS)
    reverse = tuple(reversed(range(endpoint_count)))
    transfer = []
    for row in range(endpoint_count):
        for column in range(endpoint_count):
            first = (reverse[row], reverse[column])
            second = (reverse[first[0]], reverse[first[1]])
            transfer.append(Fraction(second == (row, column)))
    return {
        "recoil_coefficients": recoil,
        "recoil_equation_count": equation_count,
        "recoil_normal_matrix": tuple(tuple(row) for row in gram),
        "recoil_rhs": tuple(rhs),
        "transfer_coefficients": tuple(transfer),
        "transfer_endpoint_count": endpoint_count,
        "transfer_reverse": reverse,
    }


def probability_fraction(amplitude: complex) -> Fraction:
    return Fraction.from_float(
        float(amplitude.real) ** 2 + float(amplitude.imag) ** 2
    )


def evaluate_coherent_channels(
    channels: tuple[int, ...],
) -> dict[str, object]:
    """Apply one explicit normalized state and recount in reverse flat order."""
    if not channels or len(set(channels)) != len(channels):
        raise ValueError("channels must be a nonempty distinct tuple")
    _exchange, vertex, _charge, _momenta = U320.link_recoil_vertex(U320.ANGLE)
    direction_count = len(U320.c210.DIRECTIONS)
    branch_dimension = direction_count**3
    dimension = int(vertex.shape[0])
    coefficient = 1.0 / float(U320.np.sqrt(len(channels)))
    state = U320.np.zeros(dimension, dtype=complex)
    for channel in channels:
        state[channel] = coefficient
    if abs(float(U320.np.vdot(state, state).real) - 1.0) > U320.TOLERANCE:
        raise ValueError("explicit input state failed normalization")
    output = vertex @ state

    transition = vertex[
        direction_count:direction_count + branch_dimension,
        tuple(channels),
    ]
    support_sets = tuple(
        {
            flat
            for flat in range(branch_dimension)
            if abs(transition[flat, source_index]) > U320.TOLERANCE
        }
        for source_index in range(len(channels))
    )
    union_support = set().union(*support_sets)
    overlap_support = set()
    for left, right in combinations(range(len(channels)), 2):
        overlap_support.update(support_sets[left] & support_sets[right])

    raw_by_source = [
        [
            [Fraction() for _axis in range(3)]
            for _component in range(3)
        ]
        for _channel in channels
    ]
    block_weights = [Fraction() for _channel in channels]
    total_raw = [
        [Fraction() for _axis in range(3)]
        for _component in range(3)
    ]
    total_weight = Fraction()
    cross_term_rows = []
    unsupported_nonzero = []

    branch_output = output[direction_count:]
    for flat in range(branch_dimension - 1, -1, -1):
        matter = flat // direction_count**2
        mediator = (flat // direction_count) % direction_count
        auxiliary = flat % direction_count
        amplitude = complex(branch_output[flat])
        coherent_probability = probability_fraction(amplitude)
        diagonal_probability = sum(
            (
                probability_fraction(
                    complex(transition[flat, source_index] * coefficient)
                )
                for source_index in range(len(channels))
            ),
            start=Fraction(),
        )
        cross_term = coherent_probability - diagonal_probability
        contributors = tuple(
            source_index
            for source_index, support in enumerate(support_sets)
            if flat in support
        )
        if cross_term:
            cross_term_rows.append(
                {
                    "branch_flat": flat,
                    "contributors": contributors,
                    "cross_term": cross_term,
                }
            )
        if coherent_probability and not contributors:
            unsupported_nonzero.append(flat)
        if not coherent_probability:
            continue

        vectors = (
            direction_tuple(matter),
            direction_tuple(mediator),
            direction_tuple(auxiliary),
        )
        for component, vector in enumerate(vectors):
            for axis, value in enumerate(vector):
                total_raw[component][axis] += coherent_probability * value
        total_weight += coherent_probability

        if len(contributors) == 1:
            source_index = contributors[0]
            source = direction_tuple(channels[source_index])
            displacement_vectors = (
                tuple(
                    final - initial
                    for final, initial in zip(vectors[0], source)
                ),
                vectors[1],
                vectors[2],
            )
            block_weights[source_index] += coherent_probability
            for component, vector in enumerate(displacement_vectors):
                for axis, value in enumerate(vector):
                    raw_by_source[source_index][component][axis] += (
                        coherent_probability * value
                    )

    if not total_weight or any(not weight for weight in block_weights):
        raise ValueError("missing coherent transfer support")

    # Matter is a displacement, so subtract the input expectation before
    # reporting the normalized coherent-state conditional response.
    input_direction = tuple(
        sum(
            (
                Fraction(1, len(channels)) * direction_tuple(channel)[axis]
                for channel in channels
            ),
            start=Fraction(),
        )
        for axis in range(3)
    )
    physical_conditional = tuple(
        tuple(
            (
                total_raw[component][axis] / total_weight
                - (input_direction[axis] if component == 0 else Fraction())
            )
            for axis in range(3)
        )
        for component in range(3)
    )
    channel_rows = tuple(
        tuple(
            tuple(
                raw_by_source[source_index][component][axis]
                / block_weights[source_index]
                for axis in range(3)
            )
            for component in range(3)
        )
        for source_index in range(len(channels))
    )
    additive_rows = add_rows(channel_rows)
    return {
        "additive_rows": additive_rows,
        "block_additive": (
            not overlap_support
            and not cross_term_rows
            and not unsupported_nonzero
        ),
        "block_weights": tuple(block_weights),
        "channel_rows": channel_rows,
        "coherent_input_norm":
            float(U320.np.vdot(state, state).real),
        "cross_term_rows": tuple(cross_term_rows),
        "normalized_conditional_rows": physical_conditional,
        "overlap_support_count": len(overlap_support),
        "support_counts": tuple(len(support) for support in support_sets),
        "union_support_count": len(union_support),
        "unsupported_nonzero": tuple(unsupported_nonzero),
    }


def kernel_prediction(
    channels: tuple[int, ...],
    recoil_coefficients: tuple[Fraction, ...],
) -> dict[str, object]:
    configuration = add_rows(
        tuple(defining_row(channel) for channel in channels)
    )
    prediction = tuple(
        tuple(coefficient * value for value in row)
        for coefficient, row in zip(recoil_coefficients, configuration)
    )
    return {
        "configuration": configuration,
        "prediction": prediction,
    }


def main() -> int:
    started = time.monotonic()
    blocklist_before = {
        module: module in sys.modules for module in BLOCKLIST
    }
    permitted_bytes_before = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
    }
    primary_bytes_before = {
        path: (ROOT / path).read_bytes()
        for path in PRIMARY_TEXT_PATHS
    }
    shas_before = {
        path: sha256_bytes(data)
        for path, data in {
            **permitted_bytes_before,
            **primary_bytes_before,
        }.items()
    }

    frozen = extract_cycle768_frozen(
        primary_bytes_before[PRIMARY_TEXT_PATHS[0]].decode("utf-8")
    )
    emit(
        "FROZEN EXTRACTION finding: "
        + json.dumps(
            {
                "channel_pair": frozen["channel_pair"],
                "configuration": frozen["configuration"],
                "prediction": frozen["prediction"],
                "recoil_coefficients": frozen["recoil_coefficients"],
                "transfer_coefficients": frozen["transfer_coefficients"],
            },
            sort_keys=True,
            separators=(",", ":"),
            default=jsonable,
        )
    )
    certificate(
        "ATTACK 1 Extraction",
        (
            shas_before == EXPECTED_SHA256
            and not any(blocklist_before.values())
            and frozen["channel_pair"] == (0, 2)
            and frozen["configuration"] == frozen["prediction"]
            and AUDIT_INPUT_PATHS
            == (
                "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
                "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
            )
        ),
        {
            "audit_input_paths": AUDIT_INPUT_PATHS,
            "blocklist": BLOCKLIST,
            "sys_modules_before": blocklist_before,
            "mode": "own text/AST reader; neither primary executed or imported",
            "sha256": shas_before,
            "structural_evidence": frozen["structural_evidence"],
        },
    )

    direct = evaluate_coherent_channels(frozen["channel_pair"])
    direct_rerun = evaluate_coherent_channels(frozen["channel_pair"])
    additive_match = direct["additive_rows"] == frozen["prediction"]
    normalized_match = (
        direct["normalized_conditional_rows"] == frozen["prediction"]
    )
    path_outcome = (
        "ADDITIVE_LEDGER_MATCH"
        if additive_match
        else "ADDITIVE_LEDGER_REFUTES_FROZEN_PREDICTION"
    )
    if not normalized_match:
        path_outcome += "; NORMALIZED_COHERENT_EXPECTATION_MISMATCH"
    emit(
        "PATH-INDEPENDENCE finding: "
        + json.dumps(
            {
                "additive_rows": direct["additive_rows"],
                "frozen_prediction": frozen["prediction"],
                "normalized_conditional_rows":
                    direct["normalized_conditional_rows"],
                "outcome": path_outcome,
            },
            sort_keys=True,
            separators=(",", ":"),
            default=jsonable,
        )
    )
    certificate(
        "ATTACK 2 Path-independence recount (tautology attack)",
        (
            abs(direct["coherent_input_norm"] - 1.0) < U320.TOLERANCE
            and len(direct["channel_rows"]) == len(frozen["channel_pair"])
            and not direct["unsupported_nonzero"]
        ),
        {
            "explicit_normalized_state": True,
            "identity_columns_used": False,
            "loop_order": "reverse flattened branch basis; arithmetic source blocks",
            "primary_771_simulation_source_used": False,
            "additive_exact_match": additive_match,
            "normalized_state_exact_match": normalized_match,
            "finding": path_outcome,
            "rows": {
                "channel_conditioned": direct["channel_rows"],
                "additive": direct["additive_rows"],
                "normalized_coherent_conditional":
                    direct["normalized_conditional_rows"],
                "frozen": frozen["prediction"],
            },
        },
    )

    if direct["block_additive"]:
        cross_finding = (
            "EXACTLY BLOCK-ADDITIVE: the two input channels have disjoint "
            "branch support and no interference cross-terms. This is a "
            "weaker out-of-sample test because the composite result is the "
            "sum of already defining single-channel rows."
        )
    else:
        cross_finding = (
            "NOT BLOCK-ADDITIVE: overlapping support/interference terms are "
            "present; inspect the printed cross-term rows."
        )
    emit(f"CROSS-TERM finding: {cross_finding}")
    certificate(
        "ATTACK 3 Cross-term structure probe",
        (
            len(direct["support_counts"]) == len(frozen["channel_pair"])
            and direct["union_support_count"] > 0
            and not direct["unsupported_nonzero"]
        ),
        {
            "block_additive": direct["block_additive"],
            "branch_support_counts": direct["support_counts"],
            "cross_term_rows": direct["cross_term_rows"],
            "finding": cross_finding,
            "overlap_support_count": direct["overlap_support_count"],
            "union_support_count": direct["union_support_count"],
        },
    )

    landed_kernel = extract_landed_kernel()
    kernel_extraction_agrees = (
        landed_kernel["recoil_coefficients"]
        == frozen["recoil_coefficients"]
        and landed_kernel["transfer_coefficients"]
        == frozen["transfer_coefficients"]
    )
    census_rows = []
    disagreements = []
    for pair in FROZEN_PAIR_CENSUS:
        simulation = evaluate_coherent_channels(pair)
        predicted = kernel_prediction(
            pair, landed_kernel["recoil_coefficients"]
        )
        match = simulation["additive_rows"] == predicted["prediction"]
        row = {
            "channel_pair": pair,
            "configuration": predicted["configuration"],
            "direct_additive_rows": simulation["additive_rows"],
            "kernel_prediction": predicted["prediction"],
            "match": match,
            "normalized_conditional_rows":
                simulation["normalized_conditional_rows"],
        }
        census_rows.append(row)
        if not match:
            disagreements.append(row)
            emit(
                "PAIR-CENSUS DISAGREEMENT — VERIFIED IS PAIR-SPECIFIC: "
                + json.dumps(
                    row,
                    sort_keys=True,
                    separators=(",", ":"),
                    default=jsonable,
                )
            )
    pair_specific = bool(disagreements)
    if not pair_specific:
        emit(
            "PAIR-CENSUS finding: no disagreements across "
            "((0,1),(0,2),(1,2)); the additive-ledger match is not "
            "pair-specific on this full census."
        )
    certificate(
        "ATTACK 4 Full pair census",
        (
            kernel_extraction_agrees
            and tuple(row["channel_pair"] for row in census_rows)
            == FROZEN_PAIR_CENSUS
            and len(census_rows) == len(FROZEN_PAIR_CENSUS)
        ),
        {
            "census": tuple(census_rows),
            "disagreeing_rows": tuple(disagreements),
            "kernel_extraction": landed_kernel,
            "kernel_extraction_matches_cycle768_ast": kernel_extraction_agrees,
            "pair_specific": pair_specific,
            "finding": (
                "VERIFIED verdict is pair-specific"
                if pair_specific
                else "no pair specificity found in the requested full census"
            ),
        },
    )

    defining_channel = frozen["channel_pair"][0]
    defining_simulation = evaluate_coherent_channels((defining_channel,))
    defining_expected = defining_row(defining_channel)
    defining_ok = (
        defining_simulation["additive_rows"] == defining_expected
        and defining_simulation["normalized_conditional_rows"]
        == defining_expected
    )
    perturbed_pair = (
        frozen["channel_pair"][0],
        U320.REVERSE[frozen["channel_pair"][1]],
    )
    perturbed = evaluate_coherent_channels(perturbed_pair)
    perturbation_mismatch = (
        perturbed_pair != frozen["channel_pair"]
        and perturbed["additive_rows"] != frozen["prediction"]
    )
    deterministic = direct_rerun == direct

    permitted_bytes_after = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
    }
    primary_bytes_after = {
        path: (ROOT / path).read_bytes()
        for path in PRIMARY_TEXT_PATHS
    }
    shas_after = {
        path: sha256_bytes(data)
        for path, data in {
            **permitted_bytes_after,
            **primary_bytes_after,
        }.items()
    }
    blocklist_after = {
        module: module in sys.modules for module in BLOCKLIST
    }
    runtime = time.monotonic() - started
    projected_stdout_bytes = STDOUT_BYTES + 32_000
    certificate(
        "ATTACK 5 Control recount",
        (
            defining_ok
            and perturbation_mismatch
            and deterministic
            and shas_after == shas_before == EXPECTED_SHA256
            and not any(blocklist_after.values())
            and runtime < AUDIT_TIMEOUT_SEC
            and projected_stdout_bytes < OUTPUT_LIMIT_BYTES
        ),
        {
            "defining_calibration": {
                "channel": defining_channel,
                "direct": defining_simulation["additive_rows"],
                "expected": defining_expected,
                "match": defining_ok,
            },
            "determinism": deterministic,
            "perturbation": {
                "channel_pair": perturbed_pair,
                "direct_additive_rows": perturbed["additive_rows"],
                "frozen_prediction": frozen["prediction"],
                "mismatch": perturbation_mismatch,
            },
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": runtime,
            "sha256_after": shas_after,
            "stdout_limit_bytes": OUTPUT_LIMIT_BYTES,
            "stdout_projected_bytes": projected_stdout_bytes,
            "sys_modules_after": blocklist_after,
        },
    )

    if not additive_match or pair_specific:
        adversarial_outcome = "REFUTED"
    elif direct["block_additive"] or not normalized_match:
        adversarial_outcome = "WEAKENED"
    else:
        adversarial_outcome = "SURVIVED"
    final_runtime = time.monotonic() - started
    emit(
        "FINAL "
        + json.dumps(
            {
                "adversarial_outcome": adversarial_outcome,
                "fail": FAIL,
                "pair_specific": pair_specific,
                "pass": PASS,
                "path_independent_additive_match": additive_match,
                "normalized_coherent_expectation_match": normalized_match,
                "block_additive": direct["block_additive"],
                "runtime_sec": final_runtime,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
