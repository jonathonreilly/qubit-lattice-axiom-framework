#!/usr/bin/env python3
"""Cycle 768 independent checker: attack, recount, and bound one candidate.

The Cycle-768 primary is blocklisted executable material.  This checker reads
it only as text/AST data, constructs its own kernel from U320/S322 objects,
and submits only that independent construction to the unchanged Cycle-749
instrument.
"""

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/RESPONSE_LAW_CANDIDATE_CYCLE768_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
)
BLOCKLIST = (
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
)

import ast
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path
import time

import frontier_cycle749_response_comparison_harness_2026_07_28 as H749
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322
import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_LIMIT_BYTES = 150_000
PASS = 0
FAIL = 0
STDOUT_BYTES = 0
CRITERIA = (
    "diagonal_exchange_residual",
    "flux_balance",
    "norm_drift",
    "reciprocal_transfer_values",
    "reciprocity_residual",
    "recoil_ledger",
)
OWN_CONSTRUCTION_FUNCTIONS = (
    "apply_exchange",
    "construct_independent_candidate",
    "derive_recoil_kernel",
    "derive_transfer_kernel",
    "solve_fraction_system",
)
PRIMARY_CONSTRUCTION_FUNCTIONS = (
    "apply_endpoint_exchange",
    "derive_recoil_coefficients",
    "derive_response_kernel_candidate",
    "derive_transfer_coefficients",
)
CENSUS_DOMAIN = (-2, -1, 0, 1, 2)
BOUNDARY_VERBATIM = "no law claim; prediction unverified; C_source clean"

# Verbatim operative C_source declarations carried by the primary and harness.
C_source = (
    "No physical momentum, work, energy, stress, or gravity meaning is assigned.",
    "dimensionless direction/flux only; not physical momentum, work, energy, stress, gravity, or metric",
    "The result is a bounded common-code response/reciprocity proxy, not physical energy, stress, gravity, metric, or time.",
    "finite occupation response only; not energy, stress, gravity, metric, force, or time",
    "does not splice routes, name occupation probability energy, or promote a selected source-port residual to an autonomous-law obstruction.",
    "probability/configuration current, not energy",
    "not physical energy",
    "nothing here calls it physical energy or stress",
)


@dataclass(frozen=True)
class IndependentKernel:
    recoil_coefficients: tuple[Fraction, ...]
    transfer_coefficients: tuple[Fraction, ...]
    fitted_defaults: tuple[Fraction, ...]


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        return fraction_text(value)
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def emit(line: str) -> None:
    global STDOUT_BYTES
    print(line)
    STDOUT_BYTES += len((line + "\n").encode("utf-8"))


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        prefix = "PASS"
    else:
        FAIL += 1
        prefix = "FAIL"
    rendered = json.dumps(
        detail, sort_keys=True, separators=(",", ":"), default=jsonable
    )
    emit(f"{prefix} {label} :: {rendered}")


def literal_assignment(tree: ast.Module, name: str) -> object:
    matches = []
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in targets
            ):
                matches.append(node.value)
    if len(matches) != 1:
        raise ValueError(f"expected one literal assignment for {name}")
    return ast.literal_eval(matches[0])


def function_map(tree: ast.Module) -> dict[str, ast.FunctionDef | ast.AsyncFunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def dotted_call_name(node: ast.Call) -> str:
    parts = []
    value: ast.AST = node.func
    while isinstance(value, ast.Attribute):
        parts.append(value.attr)
        value = value.value
    if isinstance(value, ast.Name):
        parts.append(value.id)
    return ".".join(reversed(parts))


def construction_ast_audit(
    tree: ast.Module,
    names: tuple[str, ...],
) -> dict[str, object]:
    functions = function_map(tree)
    selected = tuple(functions[name] for name in names if name in functions)
    numeric_literals = []
    harness_references = []
    criterion_references = []
    forbidden_attributes = {
        "BUILT_IN_CANDIDATES",
        "DRIFT_LIMIT",
        "STRICT_TOLERANCE",
        "evaluate_candidate",
        "extract_frozen_fixtures",
    }
    calls = set()
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
            if isinstance(node, ast.Name) and node.id == "H749":
                harness_references.append(
                    {"function": function.name, "line": node.lineno}
                )
            if (
                isinstance(node, ast.Attribute)
                and node.attr in forbidden_attributes
            ):
                criterion_references.append(
                    {
                        "attribute": node.attr,
                        "function": function.name,
                        "line": node.lineno,
                    }
                )
            if isinstance(node, ast.Call):
                calls.add(dotted_call_name(node))
    return {
        "calls": tuple(sorted(calls)),
        "criterion_references": criterion_references,
        "functions_found": tuple(sorted(function.name for function in selected)),
        "harness_references": harness_references,
        "numeric_literals": numeric_literals,
        "passed": (
            len(selected) == len(names)
            and not numeric_literals
            and not harness_references
            and not criterion_references
        ),
    }


def extraction() -> dict[str, object]:
    """Extract the primary's static contract without importing or executing it."""
    primary_path = ROOT / BLOCKLIST[0]
    primary_source = primary_path.read_text(encoding="utf-8")
    primary_tree = ast.parse(primary_source, filename=str(primary_path))
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))

    primary_audit_paths = literal_assignment(primary_tree, "AUDIT_INPUT_PATHS")
    own_audit_paths = literal_assignment(own_tree, "AUDIT_INPUT_PATHS")
    primary_note = literal_assignment(primary_tree, "NOTE_PATH")
    primary_timeout = literal_assignment(primary_tree, "AUDIT_TIMEOUT_SEC")
    primary_c_source = literal_assignment(primary_tree, "C_source")
    primary_derivation_names = literal_assignment(
        primary_tree, "DERIVATION_FUNCTIONS"
    )

    own_imports = {
        alias.name
        for node in own_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    forbidden_runtime_calls = tuple(
        sorted(
            {
                node.func.id
                for node in ast.walk(own_tree)
                if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id
                in {"__import__", "compile", "eval", "exec"}
            }
        )
    )
    primary_module = Path(BLOCKLIST[0]).stem
    static_audit = construction_ast_audit(
        primary_tree, PRIMARY_CONSTRUCTION_FUNCTIONS
    )
    calls = set(static_audit["calls"])
    constants = {
        node.value
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    criterion_sets = []
    for node in ast.walk(primary_tree):
        if isinstance(node, ast.Set):
            try:
                value = ast.literal_eval(node)
            except (ValueError, TypeError):
                continue
            if isinstance(value, set):
                criterion_sets.append(value)
    primary_functions = function_map(primary_tree)
    extension_node = primary_functions.get("extension_probe")
    extension_constants = (
        {
            node.value
            for node in ast.walk(extension_node)
            if isinstance(node, ast.Constant)
        }
        if extension_node is not None
        else set()
    )

    static_chain_ok = (
        "U320.link_recoil_vertex" in calls
        and "derive_recoil_coefficients" in calls
        and "derive_transfer_coefficients" in calls
        and "K=R*R=I" in constants
        and "P_axis=D_matter+D_field+D_auxiliary" in constants
    )
    criteria_found = any(set(CRITERIA) == value for value in criterion_sets)
    extension_unverified_found = (
        "prediction_verified" in extension_constants
        and False in extension_constants
    )
    expected_claim = {
        "fitted_defaults": ("0",) * 7,
        "per_criterion_verdicts": {
            name: "ACCEPT" for name in CRITERIA
        },
        "prediction": (("-2", "-2", "0"), ("1", "1", "0"), ("1", "1", "0")),
        "prediction_verified": False,
        "recoil_coefficients": ("1", "1", "1"),
        "residuals": {name: 0.0 for name in CRITERIA},
        "transfer_coefficients": ("1", "1", "1", "1"),
    }
    passed = (
        primary_audit_paths == AUDIT_INPUT_PATHS
        and own_audit_paths == AUDIT_INPUT_PATHS
        and primary_note == NOTE_PATH
        and primary_timeout == AUDIT_TIMEOUT_SEC
        and primary_c_source == C_source
        and tuple(primary_derivation_names) == PRIMARY_CONSTRUCTION_FUNCTIONS
        and primary_module not in own_imports
        and not forbidden_runtime_calls
        and static_chain_ok
        and criteria_found
        and extension_unverified_found
        and bool(static_audit["passed"])
    )
    return {
        "audit_literal_eval": {
            "own": own_audit_paths,
            "primary": primary_audit_paths,
            "pure_literal_equal": own_audit_paths
            == primary_audit_paths
            == AUDIT_INPUT_PATHS,
        },
        "blocklist": BLOCKLIST,
        "blocklist_imported": primary_module in own_imports,
        "chain": (
            "U320 diagonal decomposition -> unit sector weights; "
            "S322 R with R*R=I; recoil (1,1,1); transfer (1,1,1,1); "
            "zero fitted defaults"
        ),
        "criterion_set_found": criteria_found,
        "expected_claim": expected_claim,
        "forbidden_runtime_calls": forbidden_runtime_calls,
        "passed": passed,
        "primary_construction_ast": static_audit,
        "primary_read_mode": "text/AST data only; never imported",
    }


def solve_fraction_system(
    matrix: tuple[tuple[Fraction, ...], ...],
    right_hand_side: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    """Solve a nonsingular exact system by independent Gauss-Jordan steps."""
    size = len(matrix)
    zero = Fraction()
    augmented = [
        list(row) + [right_hand_side[index]]
        for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(
            row
            for row in range(column, size)
            if augmented[row][column] != zero
        )
        augmented[column], augmented[pivot] = (
            augmented[pivot],
            augmented[column],
        )
        divisor = augmented[column][column]
        augmented[column] = [
            value / divisor for value in augmented[column]
        ]
        for row in range(size):
            if row == column:
                continue
            multiplier = augmented[row][column]
            augmented[row] = [
                value - multiplier * pivot_value
                for value, pivot_value in zip(
                    augmented[row], augmented[column]
                )
            ]
    return tuple(row.pop() for row in augmented)


def derive_recoil_kernel() -> tuple[tuple[Fraction, ...], dict[str, object]]:
    """Recover the three diagonal sector weights from U320 itself."""
    directions = U320.c210.DIRECTIONS
    _exchange, _vertex, _charge, momenta = U320.link_recoil_vertex(U320.ANGLE)
    sector_count = len(momenta)
    zero = Fraction()
    gram = [
        [zero for _right in range(sector_count)]
        for _left in range(sector_count)
    ]
    right_hand_side = [zero for _sector in range(sector_count)]
    rows = []
    offset = len(directions)
    configurations = product(range(len(directions)), repeat=sector_count)
    for flat_index, configuration in enumerate(configurations):
        for axis, momentum in enumerate(momenta):
            diagonal_index = offset + flat_index
            target = Fraction(
                round(float(momentum[diagonal_index, diagonal_index].real))
            )
            row = tuple(
                Fraction(int(directions[direction, axis]))
                for direction in configuration
            )
            rows.append((row, target))
            for left in range(sector_count):
                right_hand_side[left] += row[left] * target
                for right in range(sector_count):
                    gram[left][right] += row[left] * row[right]
    coefficients = solve_fraction_system(
        tuple(tuple(row) for row in gram),
        tuple(right_hand_side),
    )
    residuals = tuple(
        target
        - sum(
            (
                coefficient * value
                for coefficient, value in zip(coefficients, row)
            ),
            start=zero,
        )
        for row, target in rows
    )
    return coefficients, {
        "diagonal_rows_recounted": len(rows),
        "gram": tuple(tuple(value for value in row) for row in gram),
        "maximum_diagonal_residual": max(
            (abs(value) for value in residuals), default=zero
        ),
        "normal_equation_rhs": tuple(right_hand_side),
    }


def apply_exchange(
    matrix: tuple[tuple[Fraction, ...], ...],
    permutation: tuple[tuple[Fraction, ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    """Apply R(X)=P X P^T using exact arithmetic."""
    size = len(permutation)
    zero = Fraction()
    return tuple(
        tuple(
            sum(
                (
                    permutation[row][left]
                    * matrix[left][right]
                    * permutation[column][right]
                    for left in range(size)
                    for right in range(size)
                ),
                start=zero,
            )
            for column in range(size)
        )
        for row in range(size)
    )


def derive_transfer_kernel() -> tuple[
    tuple[Fraction, ...], dict[str, object]
]:
    """Build endpoint reversal from S322.ENDPOINTS and square its action."""
    endpoints = tuple(S322.ENDPOINTS)
    reversed_endpoints = tuple(reversed(endpoints))
    size = len(endpoints)
    zero = Fraction()
    permutation = tuple(
        tuple(
            Fraction(endpoints[row] == reversed_endpoints[column])
            for column in range(size)
        )
        for row in range(size)
    )
    identity = tuple(
        tuple(Fraction(row == column) for column in range(size))
        for row in range(size)
    )
    matrix_square = tuple(
        tuple(
            sum(
                (
                    permutation[row][middle] * permutation[middle][column]
                    for middle in range(size)
                ),
                start=zero,
            )
            for column in range(size)
        )
        for row in range(size)
    )
    coefficients = []
    action_residuals = []
    for basis_row in range(size):
        for basis_column in range(size):
            basis = tuple(
                tuple(
                    Fraction(
                        (row, column) == (basis_row, basis_column)
                    )
                    for column in range(size)
                )
                for row in range(size)
            )
            twice = apply_exchange(
                apply_exchange(basis, permutation), permutation
            )
            coefficients.append(twice[basis_row][basis_column])
            action_residuals.append(
                sum(
                    (
                        abs(twice[row][column] - basis[row][column])
                        for row in range(size)
                        for column in range(size)
                    ),
                    start=zero,
                )
            )
    return tuple(coefficients), {
        "R": permutation,
        "R_squared": matrix_square,
        "R_squared_is_identity": matrix_square == identity,
        "basis_action_residuals": tuple(action_residuals),
        "endpoints": endpoints,
    }


def construct_independent_candidate() -> IndependentKernel:
    """Construct a kernel before any harness criterion or fixture is read."""
    recoil, _recoil_trace = derive_recoil_kernel()
    transfer, _transfer_trace = derive_transfer_kernel()
    defaults = tuple(Fraction() for _value in recoil + transfer)
    return IndependentKernel(recoil, transfer, defaults)


def chain_recount(
    candidate: IndependentKernel | None = None,
    extracted: dict[str, object] | None = None,
) -> dict[str, object]:
    """Recount the source-side chain and compare it to the static primary."""
    if candidate is None:
        candidate = construct_independent_candidate()
    if extracted is None:
        extracted = extraction()
    recoil, recoil_trace = derive_recoil_kernel()
    transfer, transfer_trace = derive_transfer_kernel()
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    own_ast = construction_ast_audit(own_tree, OWN_CONSTRUCTION_FUNCTIONS)
    expected = extracted["expected_claim"]
    assert isinstance(expected, dict)
    reproduction = {
        "fitted_defaults": tuple(
            fraction_text(value) for value in candidate.fitted_defaults
        ),
        "recoil_coefficients": tuple(
            fraction_text(value) for value in candidate.recoil_coefficients
        ),
        "transfer_coefficients": tuple(
            fraction_text(value) for value in candidate.transfer_coefficients
        ),
    }
    expected_reproduction = {
        key: expected[key]
        for key in (
            "fitted_defaults",
            "recoil_coefficients",
            "transfer_coefficients",
        )
    }
    passed = (
        candidate.recoil_coefficients == recoil
        and candidate.transfer_coefficients == transfer
        and all(value == 0 for value in candidate.fitted_defaults)
        and reproduction == expected_reproduction
        and recoil_trace["maximum_diagonal_residual"] == 0
        and bool(transfer_trace["R_squared_is_identity"])
        and all(
            value == 0 for value in transfer_trace["basis_action_residuals"]
        )
        and bool(own_ast["passed"])
        and bool(extracted["primary_construction_ast"]["passed"])
    )
    return {
        "candidate_reproduces_primary": reproduction
        == expected_reproduction,
        "independent_candidate": reproduction,
        "own_constant_freedom_and_no_peeking_ast": own_ast,
        "passed": passed,
        "primary_constant_freedom_and_no_peeking_ast": extracted[
            "primary_construction_ast"
        ],
        "recoil_recount": recoil_trace,
        "transfer_recount": transfer_trace,
    }


def harness_candidate(
    name: str,
    recoil: tuple[Fraction, ...],
    transfer: tuple[Fraction, ...],
    defaults: tuple[Fraction, ...],
    role: str,
) -> H749.ResponseKernelCandidate:
    return H749.ResponseKernelCandidate(
        name=name,
        recoil_coefficients=recoil,
        transfer_coefficients=transfer,
        fitted_defaults=defaults,
        demonstration_role=role,
    )


def verdict_recount(
    candidate: IndependentKernel | None = None,
    fixtures: H749.FrozenFixtures | None = None,
) -> dict[str, object]:
    """Submit only the independently derived candidate to the unchanged harness."""
    if candidate is None:
        candidate = construct_independent_candidate()
    if fixtures is None:
        fixtures = H749.extract_frozen_fixtures()
    submitted = harness_candidate(
        "cycle768_independent_recount",
        candidate.recoil_coefficients,
        candidate.transfer_coefficients,
        candidate.fitted_defaults,
        "independently derived from U320/S322 before fixture extraction",
    )
    evaluation = H749.evaluate_candidate(submitted, fixtures, fixtures)
    residuals = evaluation["residuals"]
    assert isinstance(residuals, dict)
    per_criterion = {
        name: "ACCEPT" if residuals[name] == 0.0 else "NONZERO"
        for name in CRITERIA
    }
    passed = (
        evaluation["verdict"] == "ACCEPT"
        and not evaluation["failed_criteria"]
        and set(residuals) == set(CRITERIA)
        and all(residuals[name] == 0.0 for name in CRITERIA)
        and all(value == "ACCEPT" for value in per_criterion.values())
    )
    return {
        "failed_criteria": evaluation["failed_criteria"],
        "overall": evaluation["verdict"],
        "passed": passed,
        "per_criterion_verdicts": per_criterion,
        "residuals": residuals,
    }


def evaluation_summary(evaluation: dict[str, object]) -> dict[str, object]:
    return {
        "failed_criteria": evaluation["failed_criteria"],
        "largest_residual": evaluation["largest_residual"],
        "residuals": evaluation["residuals"],
        "verdict": evaluation["verdict"],
    }


def triviality_attack(
    candidate: IndependentKernel | None = None,
    fixtures: H749.FrozenFixtures | None = None,
) -> dict[str, object]:
    """Attack vacuity with wrong controls and a declared 5^7 census."""
    if candidate is None:
        candidate = construct_independent_candidate()
    if fixtures is None:
        fixtures = H749.extract_frozen_fixtures()
    one = Fraction(1)
    two = one + one
    negative_one = -one
    defaults = tuple(Fraction() for _value in candidate.fitted_defaults)
    _transfer, transfer_trace = derive_transfer_kernel()
    exchange_selector = tuple(
        value for row in transfer_trace["R"] for value in row
    )
    wrong_candidates = (
        harness_candidate(
            "own_sign_flip",
            tuple(negative_one for _value in candidate.recoil_coefficients),
            tuple(negative_one for _value in candidate.transfer_coefficients),
            defaults,
            "own structured wrong control: full sign flip",
        ),
        harness_candidate(
            "own_magnitude_two",
            tuple(two for _value in candidate.recoil_coefficients),
            tuple(two for _value in candidate.transfer_coefficients),
            defaults,
            "own structured wrong control: doubled magnitude",
        ),
        harness_candidate(
            "own_permuted_transfer",
            tuple(one for _value in candidate.recoil_coefficients),
            exchange_selector,
            defaults,
            "own structured wrong control: endpoint-exchange transfer selector",
        ),
    )
    wrong_evaluations = {
        item.name: H749.evaluate_candidate(item, fixtures, fixtures)
        for item in wrong_candidates
    }
    wrong_summary = {
        name: evaluation_summary(row)
        for name, row in wrong_evaluations.items()
    }

    verdict_census = {"ACCEPT": 0, "DRIFT": 0, "REJECT": 0}
    all_six_pass = 0
    all_six_examples = []
    family_size = 0
    zero_defaults = tuple(Fraction() for _value in candidate.fitted_defaults)
    for raw_coefficients in product(
        CENSUS_DOMAIN, repeat=len(zero_defaults)
    ):
        family_size += 1
        coefficients = tuple(Fraction(value) for value in raw_coefficients)
        submitted = harness_candidate(
            "census",
            coefficients[: len(candidate.recoil_coefficients)],
            coefficients[len(candidate.recoil_coefficients) :],
            zero_defaults,
            "declared bounded natural integer/sign family",
        )
        evaluation = H749.evaluate_candidate(submitted, fixtures, fixtures)
        verdict = str(evaluation["verdict"])
        verdict_census[verdict] += 1
        residuals = evaluation["residuals"]
        assert isinstance(residuals, dict)
        if set(residuals) == set(CRITERIA) and all(
            residuals[name] == 0.0 for name in CRITERIA
        ):
            all_six_pass += 1
            if len(all_six_examples) < 8:
                all_six_examples.append(raw_coefficients)

    wrong_controls_caught = all(
        row["verdict"] in {"REJECT", "DRIFT"}
        for row in wrong_evaluations.values()
    )
    unique_expected_pass = (
        all_six_pass == 1
        and all_six_examples
        == [
            tuple(
                int(value)
                for value in (
                    candidate.recoil_coefficients
                    + candidate.transfer_coefficients
                )
            )
        ]
    )
    passed = (
        wrong_controls_caught
        and family_size == len(CENSUS_DOMAIN) ** len(zero_defaults)
        and all_six_pass == verdict_census["ACCEPT"]
        and unique_expected_pass
    )
    return {
        "assessment": (
            "ACCEPT is non-vacuous in the declared bounded family"
            if all_six_pass == 1
            else "ACCEPT is weak in the declared bounded family"
        ),
        "census": {
            "all_six_criteria_pass": all_six_pass,
            "all_six_examples": all_six_examples,
            "coefficient_domain": CENSUS_DOMAIN,
            "family": (
                "three recoil plus four transfer coefficients independently "
                "in {-2,-1,0,1,2}; seven fitted defaults fixed at zero"
            ),
            "family_size": family_size,
            "verdicts": verdict_census,
        },
        "passed": passed,
        "structured_wrong_candidates": wrong_summary,
    }


def direction_tuple(values: object) -> tuple[Fraction, ...]:
    return tuple(Fraction(int(value)) for value in values)  # type: ignore[arg-type]


def single_channel_recoil(direction: int) -> tuple[
    tuple[Fraction, ...], tuple[Fraction, ...], tuple[Fraction, ...]
]:
    source = direction_tuple(U320.c210.DIRECTIONS[direction])
    target = direction_tuple(
        U320.c210.DIRECTIONS[U320.REVERSE[direction]]
    )
    matter = tuple(
        target_value - source_value
        for target_value, source_value in zip(target, source)
    )
    return matter, source, source


def prediction_recount(
    candidate: IndependentKernel | None = None,
) -> dict[str, object]:
    """Recompute the composite prediction without consulting H749 fixtures."""
    if candidate is None:
        candidate = construct_independent_candidate()
    directions = U320.c210.DIRECTIONS
    landed_direction_set = {
        direction_tuple(row) for row in directions
    }
    selected = None
    for left, right in combinations(range(len(directions)), 2):
        combined_source = direction_tuple(directions[left] + directions[right])
        if any(combined_source) and combined_source not in landed_direction_set:
            selected = (left, right)
            break
    if selected is None:
        return {
            "determinate": False,
            "outside_defining_set": False,
            "passed": False,
            "prediction_verified": False,
            "reason": "no outside composite channel found",
        }
    component_rows = tuple(
        single_channel_recoil(direction) for direction in selected
    )
    zero = Fraction()
    configuration = tuple(
        tuple(
            sum(
                (row[component][axis] for row in component_rows),
                start=zero,
            )
            for axis in range(len(directions[0]))
        )
        for component in range(len(candidate.recoil_coefficients))
    )
    prediction = tuple(
        tuple(
            coefficient * value for value in vector
        )
        for coefficient, vector in zip(
            candidate.recoil_coefficients, configuration
        )
    )
    defining_set = {
        single_channel_recoil(direction)
        for direction in range(len(directions))
    }
    expected = (
        (Fraction(-2), Fraction(-2), Fraction(0)),
        (Fraction(1), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(1), Fraction(0)),
    )
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    prediction_node = function_map(own_tree)["prediction_recount"]
    forbidden_names = tuple(
        sorted(
            {
                node.id
                for node in ast.walk(prediction_node)
                if isinstance(node, ast.Name)
                and node.id in {"H749", "extraction"}
            }
        )
    )
    forbidden_calls = tuple(
        sorted(
            {
                dotted_call_name(node)
                for node in ast.walk(prediction_node)
                if isinstance(node, ast.Call)
                and dotted_call_name(node)
                in {
                    "H749.evaluate_candidate",
                    "H749.extract_frozen_fixtures",
                }
            }
        )
    )
    outside = configuration not in defining_set
    determinate = all(
        isinstance(value, Fraction)
        for vector in prediction
        for value in vector
    )
    passed = (
        determinate
        and outside
        and prediction == expected
        and not forbidden_names
        and not forbidden_calls
    )
    return {
        "configuration": configuration,
        "defining_set_kind": "six U320 single-channel recoil rows",
        "determinate": determinate,
        "no_self_test_ast": {
            "forbidden_calls": forbidden_calls,
            "forbidden_names": forbidden_names,
            "passed": not forbidden_calls and not forbidden_names,
        },
        "outside_defining_set": outside,
        "passed": passed,
        "prediction": prediction,
        "prediction_verified": False,
        "selected_channel_pair": selected,
    }


def literal_false_values(tree: ast.Module, key: str) -> tuple[bool, ...]:
    values = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for raw_key, raw_value in zip(node.keys, node.values):
            if (
                isinstance(raw_key, ast.Constant)
                and raw_key.value == key
                and isinstance(raw_value, ast.Constant)
                and raw_value.value is False
            ):
                values.append(False)
    return tuple(values)


def discipline(
    extracted: dict[str, object] | None = None,
    prediction: dict[str, object] | None = None,
) -> dict[str, object]:
    """Pin the exact non-claim boundary and the clean C_source firewall."""
    if extracted is None:
        extracted = extraction()
    if prediction is None:
        prediction = prediction_recount()
    primary_path = ROOT / BLOCKLIST[0]
    primary_tree = ast.parse(primary_path.read_text(encoding="utf-8"))
    primary_c_source = literal_assignment(primary_tree, "C_source")
    response_law_false = literal_false_values(
        primary_tree, "response_law_established"
    )
    prediction_false = literal_false_values(
        primary_tree, "prediction_verified"
    )
    prohibitive = all(
        any(token in statement.lower() for token in ("no ", "not ", "nothing "))
        for statement in C_source
    )
    passed = (
        BOUNDARY_VERBATIM
        == "no law claim; prediction unverified; C_source clean"
        and primary_c_source == C_source == H749.C_source
        and bool(response_law_false)
        and bool(prediction_false)
        and prediction["prediction_verified"] is False
        and prohibitive
        and bool(extracted["passed"])
    )
    return {
        "boundary_verbatim": BOUNDARY_VERBATIM,
        "c_source_clean": primary_c_source == C_source == H749.C_source,
        "c_source_declaration_count": len(C_source),
        "c_source_is_prohibitive": prohibitive,
        "passed": passed,
        "prediction_unverified": prediction["prediction_verified"] is False,
        "primary_literal_false_counts": {
            "prediction_verified": len(prediction_false),
            "response_law_established": len(response_law_false),
        },
        "response_law_claimed": False,
    }


def main() -> int:
    started = time.monotonic()
    deadline = started + AUDIT_TIMEOUT_SEC

    extracted = extraction()
    candidate = construct_independent_candidate()
    chain = chain_recount(candidate, extracted)
    fixtures = H749.extract_frozen_fixtures()
    verdicts = verdict_recount(candidate, fixtures)
    triviality = triviality_attack(candidate, fixtures)
    prediction = prediction_recount(candidate)
    boundary = discipline(extracted, prediction)

    check("extraction certificate", bool(extracted["passed"]), extracted)
    check("chain recount certificate", bool(chain["passed"]), chain)
    check("verdict recount certificate", bool(verdicts["passed"]), verdicts)
    check(
        "triviality attack certificate",
        bool(triviality["passed"]),
        triviality,
    )
    check(
        "prediction recount certificate",
        bool(prediction["passed"]),
        prediction,
    )
    check("discipline certificate", bool(boundary["passed"]), boundary)
    check(
        "runtime remains within the 1800-second audit budget",
        time.monotonic() < deadline,
        {"budget_sec": AUDIT_TIMEOUT_SEC},
    )

    certificate = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "blocklist": BLOCKLIST,
        "boundary": boundary,
        "chain_recount": chain,
        "extraction": extracted,
        "fail": FAIL,
        "note_path": NOTE_PATH,
        "pass": PASS,
        "prediction_recount": prediction,
        "runtime_sec": round(time.monotonic() - started, 6),
        "triviality_attack": triviality,
        "verdict_recount": verdicts,
    }
    preview = json.dumps(
        certificate, sort_keys=True, separators=(",", ":"), default=jsonable
    )
    projected = (
        STDOUT_BYTES
        + len(preview.encode("utf-8"))
        + len("RESULT CYCLE768_RESPONSE_LAW_INDEPENDENT_CHECK_CLEAN\n")
        + 4096
    )
    check(
        "stdout remains below the 150KB contract",
        projected < OUTPUT_LIMIT_BYTES,
        {"limit_bytes": OUTPUT_LIMIT_BYTES, "projected_upper_bound": projected},
    )
    certificate["fail"] = FAIL
    certificate["pass"] = PASS
    certificate["runtime_sec"] = round(time.monotonic() - started, 6)
    emit(
        json.dumps(
            certificate,
            sort_keys=True,
            separators=(",", ":"),
            default=jsonable,
        )
    )
    if FAIL == 0:
        emit("RESULT CYCLE768_RESPONSE_LAW_INDEPENDENT_CHECK_CLEAN")
    else:
        emit("RESULT CYCLE768_RESPONSE_LAW_INDEPENDENT_CHECK_FAILED")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
