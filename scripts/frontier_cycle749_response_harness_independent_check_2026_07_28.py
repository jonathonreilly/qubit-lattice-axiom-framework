#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-749 response harness."""

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/RESPONSE_COMPARISON_HARNESS_CYCLE749_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
)

import ast
from copy import deepcopy
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from typing import Any

sys.dont_write_bytecode = True

import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322
import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = (
    ROOT / "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py"
)
PRIMARY_IMPORT_BLOCKLIST = (
    "frontier_cycle749_response_comparison_harness_2026_07_28",
)
BOUNDARY_LANGUAGE = (
    "F boundary keeps W7 open and records both remaining components",
    "F no-refit prediction attachment remains explicitly unclaimed",
    "field/metric response law",
    "no-refit prediction attachment",
)
FOURTH_CANDIDATE = {
    "name": "magnitude_doubled",
    "recoil_coefficients": (2, 2, 2),
    "transfer_coefficients": (2, 2, 2, 2),
    "fitted_defaults": (0, 0, 0, 0, 0, 0, 0),
    "demonstration_role": "deliberately magnitude-doubled structural control",
    "expected_verdict": "REJECT",
}
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def literal_assignment(tree: ast.AST, name: str) -> Any:
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            return ast.literal_eval(node.value)
    raise AssertionError(f"missing literal assignment: {name}")


def assignment_value(tree: ast.AST, name: str) -> ast.AST:
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            return node.value
    raise AssertionError(f"missing assignment: {name}")


def integer_literal(node: ast.AST) -> int:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -integer_literal(node.operand)
    raise AssertionError(f"not an integer literal: {ast.dump(node)}")


def fraction_literal(node: ast.AST) -> Fraction:
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "Fraction"
        and 1 <= len(node.args) <= 2
    ):
        numerator = integer_literal(node.args[0])
        denominator = integer_literal(node.args[1]) if len(node.args) == 2 else 1
        return Fraction(numerator, denominator)
    raise AssertionError(f"not a Fraction literal: {ast.dump(node)}")


def subscript_index(node: ast.AST) -> int | None:
    if not isinstance(node, ast.Subscript):
        return None
    if not isinstance(node.value, ast.Name) or node.value.id != "row":
        return None
    try:
        return integer_literal(node.slice)
    except AssertionError:
        return None


def recoil_coefficient(right: ast.AST) -> int | None:
    if isinstance(right, ast.Name) and right.id == "source":
        return 1
    if not (
        isinstance(right, ast.Call)
        and isinstance(right.func, ast.Name)
        and right.func.id == "tuple"
        and len(right.args) == 1
        and isinstance(right.args[0], ast.GeneratorExp)
    ):
        return None
    element = right.args[0].elt
    if not isinstance(element, ast.BinOp) or not isinstance(element.op, ast.Mult):
        return None
    for candidate, other in ((element.left, element.right), (element.right, element.left)):
        if isinstance(other, ast.Name) and other.id == "value":
            return integer_literal(candidate)
    return None


def check_call(tree: ast.AST, label: str) -> ast.Call:
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "check"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and node.args[0].value == label
        ):
            return node
    raise AssertionError(f"missing check call: {label}")


def certificate_boundary(tree: ast.AST) -> dict[str, object]:
    value = assignment_value(tree, "certificate")
    if not isinstance(value, ast.Dict):
        raise AssertionError("certificate is not a dict")
    pairs = {
        key.value: item
        for key, item in zip(value.keys, value.values)
        if isinstance(key, ast.Constant) and isinstance(key.value, str)
    }
    return {
        "harness_is_instrument_only": ast.literal_eval(
            pairs["harness_is_instrument_only"]
        ),
        "response_law_selected": ast.literal_eval(pairs["response_law_selected"]),
        "w7_closed": ast.literal_eval(pairs["w7_closed"]),
    }


def extraction(primary_source: str) -> dict[str, object]:
    """AST-extract the primary's fixtures, verdicts, inputs, and boundary."""
    tree = ast.parse(primary_source, filename=str(PRIMARY_PATH))
    audit_inputs = literal_assignment(tree, "AUDIT_INPUT_PATHS")
    verdicts = literal_assignment(tree, "EXPECTED_BUILT_IN_VERDICTS")
    remaining = literal_assignment(tree, "remaining_w7_components")
    strict_tolerance = fraction_literal(assignment_value(tree, "STRICT_TOLERANCE"))
    drift_limit = fraction_literal(assignment_value(tree, "DRIFT_LIMIT"))

    coefficients: dict[int, int] = {}
    exact_recoil_node = None
    exact_balance_node = None
    for node in ast.walk(tree):
        if isinstance(node, ast.AugAssign) and isinstance(node.target, ast.Name):
            if node.target.id == "exact_recoil":
                exact_recoil_node = node.value
            elif node.target.id == "exact_balance":
                exact_balance_node = node.value
    if exact_recoil_node is None or exact_balance_node is None:
        raise AssertionError("frozen recoil/balance AST is missing")
    for node in ast.walk(exact_recoil_node):
        if not isinstance(node, ast.Compare) or len(node.comparators) != 1:
            continue
        index = subscript_index(node.left)
        coefficient = recoil_coefficient(node.comparators[0])
        if index is not None and coefficient is not None:
            coefficients[index] = coefficient
    balance_zero = any(
        isinstance(node, ast.Compare)
        and len(node.ops) == 1
        and isinstance(node.ops[0], ast.Eq)
        and len(node.comparators) == 1
        and isinstance(node.comparators[0], ast.Constant)
        and node.comparators[0].value == 0
        and isinstance(node.left, ast.Call)
        and isinstance(node.left.func, ast.Name)
        and node.left.func.id == "sum"
        for node in ast.walk(exact_balance_node)
    )

    reciprocal_label = (
        "B frozen Cycle-322 reciprocal transfer criteria hold through held L=6"
    )
    reciprocal_call = check_call(tree, reciprocal_label)
    attributes = {
        f"{node.value.id}.{node.attr}"
        for node in ast.walk(reciprocal_call)
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name)
    }
    held_match = re.search(r"held L=(\d+)", reciprocal_label)
    clean_value = assignment_value(tree, "landed_response_clean")
    threshold_nodes = [
        node
        for node in ast.walk(clean_value)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "Fraction"
    ]
    if held_match is None or len(threshold_nodes) != 1:
        raise AssertionError("reciprocal criterion literals are ambiguous")

    extracted = {
        "audit_inputs": audit_inputs,
        "boundary": {
            **certificate_boundary(tree),
            "remaining_w7_components": remaining,
        },
        "criteria": {
            "recoil_coefficients": tuple(coefficients[index] for index in range(3)),
            "zero_flux_balance": 0 if balance_zero else None,
            "reciprocal_transfer": {
                "held_L": int(held_match.group(1)),
                "held_symbol": "S322.HELD_SIZE",
                "off_diagonal_minimum": fraction_literal(threshold_nodes[0]),
                "sizes_symbol": "S322.SIZES",
            },
        },
        "drift_limit": drift_limit,
        "strict_tolerance": strict_tolerance,
        "verdicts": verdicts,
        "tree": tree,
    }
    check(
        "1 extraction recounts the literal AUDIT tuple",
        audit_inputs == AUDIT_INPUT_PATHS and isinstance(audit_inputs, tuple),
        audit_inputs,
    )
    check(
        "1 extraction recounts recoil, balance, and held reciprocal criteria",
        extracted["criteria"]
        == {
            "recoil_coefficients": (-2, 1, 1),
            "zero_flux_balance": 0,
            "reciprocal_transfer": {
                "held_L": 6,
                "held_symbol": "S322.HELD_SIZE",
                "off_diagonal_minimum": Fraction(3, 5000),
                "sizes_symbol": "S322.SIZES",
            },
        }
        and {"S322.HELD_SIZE", "S322.SIZES"} <= attributes,
        extracted["criteria"],
    )
    check(
        "1 extraction recounts all three frozen verdicts",
        verdicts
        == {
            "identity_pullback": "ACCEPT",
            "sign_flipped": "REJECT",
            "coefficient_drift": "DRIFT",
        },
        verdicts,
    )
    check(
        "1 extraction recounts the open boundary keys",
        extracted["boundary"]
        == {
            "harness_is_instrument_only": True,
            "remaining_w7_components": [
                "field/metric response law",
                "no-refit prediction attachment",
            ],
            "response_law_selected": False,
            "w7_closed": False,
        },
        extracted["boundary"],
    )
    return extracted


def remaining_time(deadline: float) -> float:
    return max(1.0, deadline - time.monotonic())


def run_subprocess(
    path: Path | None,
    deadline: float,
    *,
    stdin_source: str | None = None,
) -> dict[str, object]:
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "scripts")
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    command = [sys.executable, "-"] if path is None else [sys.executable, str(path)]
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            env=environment,
            input=stdin_source,
            capture_output=True,
            text=True,
            timeout=remaining_time(deadline),
            check=False,
        )
        return {
            "completed": True,
            "exit_code": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
            "runtime_sec": time.monotonic() - started,
        }
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", "replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", "replace")
        return {
            "completed": False,
            "exit_code": None,
            "stdout": stdout,
            "stderr": stderr,
            "runtime_sec": time.monotonic() - started,
        }


def run_passed(row: dict[str, object], result_marker: str) -> bool:
    stdout = str(row["stdout"])
    return bool(
        row["completed"]
        and row["exit_code"] == 0
        and result_marker in stdout
        and not any(line.startswith("FAIL ") for line in stdout.splitlines())
    )


def payload_after_pass(stdout: str, label: str) -> object:
    marker = f"PASS {label} :: "
    start = stdout.find(marker)
    if start < 0:
        raise AssertionError(f"own-run PASS payload missing: {label}")
    start += len(marker)
    stops = [
        position
        for token in ("\nPASS ", "\n\n")
        if (position := stdout.find(token, start)) >= 0
    ]
    payload = stdout[start : min(stops) if stops else len(stdout)].strip()
    payload = re.sub(r"\bnp\.float64\(([^()]*)\)", r"\1", payload)
    payload = re.sub(r"\barray\((\[\[.*?\]\])\)", r"\1", payload, flags=re.DOTALL)
    return ast.literal_eval(payload)


def own_recoil_rows() -> tuple[list[dict[str, object]], bool]:
    exchange, _vertex, _charge, _momenta = U320.link_recoil_vertex(U320.ANGLE)
    rows = []
    clean = True
    for direction in range(6):
        targets = [
            index
            for index, value in enumerate(exchange[:, direction])
            if abs(value) > 0.5
        ]
        clean &= len(targets) == 1
        if not targets:
            continue
        flat = targets[0] - 6
        matter_direction, remainder = divmod(flat, 36)
        field_direction, auxiliary_direction = divmod(remainder, 6)
        source = tuple(int(value) for value in U320.c210.DIRECTIONS[direction])
        matter_target = tuple(
            int(value) for value in U320.c210.DIRECTIONS[matter_direction]
        )
        matter = [
            matter_target[axis] - source[axis] for axis in range(3)
        ]
        mediator = [
            int(value) for value in U320.c210.DIRECTIONS[field_direction]
        ]
        auxiliary = [
            int(value) for value in U320.c210.DIRECTIONS[auxiliary_direction]
        ]
        clean &= (
            matter == [-2 * value for value in source]
            and mediator == list(source)
            and auxiliary == list(source)
            and all(
                matter[axis] + mediator[axis] + auxiliary[axis] == 0
                for axis in range(3)
            )
        )
        rows.append(
            {
                "auxiliary": auxiliary,
                "direction": direction,
                "matter": matter,
                "mediator": mediator,
            }
        )
    return rows, clean and len(rows) == 6


def own_response_rows() -> list[dict[str, object]]:
    coin, fswap, contact, _update, _details = S322.c315.logical_update_controls(
        S322.LABELS
    )
    factors = (coin, fswap, contact)
    rows = []
    for length in S322.SIZES:
        matrix, norm_drift = S322.response_matrix(length, factors)
        frozen = tuple(
            tuple(Fraction(float(matrix[row, column])) for column in range(2))
            for row in range(2)
        )
        frozen_norm = Fraction(float(norm_drift))
        rows.append(
            {
                "L": length,
                "diagonal_exchange_residual": float(
                    abs(frozen[0][0] - frozen[1][1])
                ),
                "held_out": length == S322.HELD_SIZE,
                "norm_drift": float(frozen_norm),
                "off_diagonal_minimum": float(min(frozen[0][1], frozen[1][0])),
                "reciprocity_residual": float(
                    abs(frozen[0][1] - frozen[1][0])
                ),
                "response_matrix": [
                    [float(value) for value in row] for row in frozen
                ],
            }
        )
    return rows


def json_certificate(stdout: str) -> dict[str, object]:
    for line in reversed(stdout.splitlines()):
        if line.startswith("{") and line.endswith("}"):
            value = json.loads(line)
            if isinstance(value, dict):
                return value
    raise AssertionError("subprocess JSON certificate is missing")


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def criteria_recount(
    deadline: float, extracted: dict[str, object]
) -> dict[str, object]:
    """Re-derive landed criteria from the two runners and compare the primary."""
    s322_run = run_subprocess(ROOT / AUDIT_INPUT_PATHS[0], deadline)
    u320_run = run_subprocess(ROOT / AUDIT_INPUT_PATHS[1], deadline)
    check(
        "2 criteria recount obtains an all-PASS S322 own run",
        run_passed(
            s322_run,
            "RESULT TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CERTIFIED",
        ),
        {
            "exit": s322_run["exit_code"],
            "runtime_sec": round(float(s322_run["runtime_sec"]), 3),
        },
    )
    check(
        "2 criteria recount obtains an all-PASS U320 own run",
        run_passed(
            u320_run,
            "RESULT UNIT_WEIGHT_CARRIED_LINK_RECOIL_FACTOR_CERTIFIED",
        ),
        {
            "exit": u320_run["exit_code"],
            "runtime_sec": round(float(u320_run["runtime_sec"]), 3),
        },
    )

    recoil_rows, structural_recoil_clean = own_recoil_rows()
    u320_payload = payload_after_pass(
        str(u320_run["stdout"]),
        "the direction-changing carried-link vertex has exact unit-weight Q/P operator balance and nonzero matter recoil",
    )
    stdout_recoil_clean = isinstance(u320_payload, dict)
    raw_recoil_rows = u320_payload.get("response_rows", []) if stdout_recoil_clean else []
    stdout_recoil_clean &= len(raw_recoil_rows) == 6
    for structural, raw in zip(recoil_rows, raw_recoil_rows):
        direction = int(structural["direction"])
        source = [float(value) for value in U320.c210.DIRECTIONS[direction]]
        mediator = [float(value) for value in raw["mediator_flux"]]
        matter = [float(value) for value in raw["matter_recoil"]]
        auxiliary = [float(value) for value in raw["auxiliary_flux"]]
        scale = sum(mediator[axis] * source[axis] for axis in range(3))
        stdout_recoil_clean &= (
            scale > 0
            and max(
                abs(matter[axis] + 2 * scale * source[axis])
                for axis in range(3)
            )
            < 1e-12
            and max(
                abs(mediator[axis] - scale * source[axis])
                for axis in range(3)
            )
            < 1e-12
            and max(
                abs(auxiliary[axis] - scale * source[axis])
                for axis in range(3)
            )
            < 1e-12
            and float(raw["balance_residual"]) == 0.0
        )
    check(
        "2 criteria recount independently derives (-2d,+d,+d) and zero balance",
        structural_recoil_clean and stdout_recoil_clean,
        {"directions": len(recoil_rows), "own_run_rows": len(raw_recoil_rows)},
    )

    response_rows = own_response_rows()
    s322_payload = payload_after_pass(
        str(s322_run["stdout"]),
        "the same-code two-update response has nonzero reciprocal off-diagonal transfer through held L=6",
    )
    stdout_response_clean = (
        isinstance(s322_payload, list)
        and [row["L"] for row in s322_payload] == [3, 4, 6]
        and [row["held_out"] for row in s322_payload] == [False, False, True]
        and min(float(row["off_diagonal_minimum"]) for row in s322_payload) > 6e-4
        and max(
            max(
                float(row["reciprocity_residual"]),
                float(row["diagonal_exchange_residual"]),
                float(row["maximum_norm_drift"]),
            )
            for row in s322_payload
        )
        < S322.TOLERANCE
    )
    exact_response_clean = (
        [row["L"] for row in response_rows] == list(S322.SIZES)
        and S322.HELD_SIZE == 6
        and any(row["L"] == 6 and row["held_out"] for row in response_rows)
        and min(float(row["off_diagonal_minimum"]) for row in response_rows)
        > float(extracted["criteria"]["reciprocal_transfer"]["off_diagonal_minimum"])  # type: ignore[index]
        and max(
            max(
                float(row["reciprocity_residual"]),
                float(row["diagonal_exchange_residual"]),
                float(row["norm_drift"]),
            )
            for row in response_rows
        )
        <= float(extracted["strict_tolerance"])
    )
    check(
        "2 criteria recount independently derives reciprocal transfer at held L=6",
        stdout_response_clean and exact_response_clean,
        {
            "held_L": 6,
            "minimum_transfer": min(
                float(row["off_diagonal_minimum"]) for row in response_rows
            ),
        },
    )

    own_frozen = {"recoil_rows": recoil_rows, "response_rows": response_rows}
    primary_run = run_subprocess(PRIMARY_PATH, deadline)
    primary_ok = run_passed(primary_run, '"w7_closed":false')
    primary_certificate = (
        json_certificate(str(primary_run["stdout"])) if primary_ok else {}
    )
    primary_frozen = primary_certificate.get("frozen_criteria")
    value_agreement = own_frozen == primary_frozen
    byte_agreement = canonical_bytes(own_frozen) == canonical_bytes(primary_frozen)
    check(
        "2 independent frozen criteria have byte and value agreement with the harness",
        primary_ok and value_agreement and byte_agreement,
        {
            "byte_agreement": byte_agreement,
            "own_sha256": sha256_text(canonical_bytes(own_frozen).decode("utf-8")),
            "primary_sha256": sha256_text(
                canonical_bytes(primary_frozen).decode("utf-8")
            ),
        },
    )
    return {
        "own_frozen": own_frozen,
        "primary_certificate": primary_certificate,
        "primary_run": primary_run,
        "source_runs": {"S322": s322_run, "U320": u320_run},
    }


def recounted_verdict(
    row: dict[str, object], strict_tolerance: Fraction, drift_limit: Fraction
) -> tuple[str, list[str]]:
    residuals = {
        str(name): Fraction(float(value))
        for name, value in dict(row["residuals"]).items()
    }
    failed = sorted(
        name for name, residual in residuals.items() if residual > strict_tolerance
    )
    largest = max(residuals.values(), default=Fraction(0))
    if not failed:
        verdict = "ACCEPT"
    elif largest <= drift_limit:
        verdict = "DRIFT"
    else:
        verdict = "REJECT"
    return verdict, failed


def fraction_call(value: int) -> ast.Call:
    return ast.Call(
        func=ast.Name(id="Fraction", ctx=ast.Load()),
        args=[ast.Constant(value=value)],
        keywords=[],
    )


def augmented_primary(primary_source: str) -> str:
    tree = ast.parse(primary_source, filename=str(PRIMARY_PATH))
    candidates = assignment_value(tree, "BUILT_IN_CANDIDATES")
    expected = assignment_value(tree, "EXPECTED_BUILT_IN_VERDICTS")
    if not isinstance(candidates, ast.Tuple) or not isinstance(expected, ast.Dict):
        raise AssertionError("primary candidate literals are not augmentable")
    candidates.elts.append(
        ast.Call(
            func=ast.Name(id="ResponseKernelCandidate", ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(
                    arg="name", value=ast.Constant(FOURTH_CANDIDATE["name"])
                ),
                ast.keyword(
                    arg="recoil_coefficients",
                    value=ast.Tuple(
                        elts=[
                            fraction_call(int(value))
                            for value in FOURTH_CANDIDATE["recoil_coefficients"]
                        ],
                        ctx=ast.Load(),
                    ),
                ),
                ast.keyword(
                    arg="transfer_coefficients",
                    value=ast.Tuple(
                        elts=[
                            fraction_call(int(value))
                            for value in FOURTH_CANDIDATE["transfer_coefficients"]
                        ],
                        ctx=ast.Load(),
                    ),
                ),
                ast.keyword(
                    arg="fitted_defaults",
                    value=ast.Name(id="ZERO_DEFAULTS", ctx=ast.Load()),
                ),
                ast.keyword(
                    arg="demonstration_role",
                    value=ast.Constant(FOURTH_CANDIDATE["demonstration_role"]),
                ),
            ],
        )
    )
    expected.keys.append(ast.Constant(FOURTH_CANDIDATE["name"]))
    expected.values.append(ast.Constant(FOURTH_CANDIDATE["expected_verdict"]))
    file_assignment = ast.Assign(
        targets=[ast.Name(id="__file__", ctx=ast.Store())],
        value=ast.Constant(str(PRIMARY_PATH)),
    )
    insertion = 1 if (
        tree.body
        and isinstance(tree.body[0], ast.Expr)
        and isinstance(tree.body[0].value, ast.Constant)
        and isinstance(tree.body[0].value.value, str)
    ) else 0
    tree.body.insert(insertion, file_assignment)
    ast.fix_missing_locations(tree)
    return ast.unparse(tree)


def candidate_recount(
    deadline: float,
    primary_source: str,
    extracted: dict[str, object],
    criteria_state: dict[str, object],
) -> dict[str, object]:
    """Recount the three built-ins and a separately supplied fourth candidate."""
    certificate = dict(criteria_state["primary_certificate"])
    evaluations = dict(certificate.get("candidate_evaluations", {}))
    expected_verdicts = dict(extracted["verdicts"])
    recounted = {}
    built_in_clean = set(evaluations) == set(expected_verdicts)
    for name, expected_verdict in expected_verdicts.items():
        row = dict(evaluations.get(name, {}))
        if not row:
            built_in_clean = False
            continue
        verdict, failed = recounted_verdict(
            row,
            extracted["strict_tolerance"],  # type: ignore[arg-type]
            extracted["drift_limit"],  # type: ignore[arg-type]
        )
        recounted[name] = verdict
        built_in_clean &= (
            verdict == expected_verdict
            and row.get("verdict") == expected_verdict
            and list(row.get("failed_criteria", [])) == failed
        )
    check(
        "3 candidate recount independently reproduces ACCEPT/REJECT/DRIFT",
        built_in_clean and recounted == expected_verdicts,
        recounted,
    )

    probe_run = run_subprocess(
        None,
        deadline,
        stdin_source=augmented_primary(primary_source),
    )
    probe_ok = run_passed(probe_run, '"candidate":"magnitude_doubled"')
    probe_certificate = json_certificate(str(probe_run["stdout"])) if probe_ok else {}
    probe_row = dict(
        dict(probe_certificate.get("candidate_evaluations", {})).get(
            FOURTH_CANDIDATE["name"], {}
        )
    )
    if probe_row:
        probe_verdict, probe_failed = recounted_verdict(
            probe_row,
            extracted["strict_tolerance"],  # type: ignore[arg-type]
            extracted["drift_limit"],  # type: ignore[arg-type]
        )
    else:
        probe_verdict, probe_failed = "MISSING", []
    fourth_clean = (
        probe_ok
        and probe_verdict == FOURTH_CANDIDATE["expected_verdict"]
        and probe_row.get("verdict") == FOURTH_CANDIDATE["expected_verdict"]
        and list(probe_row.get("failed_criteria", [])) == probe_failed
        and "recoil_ledger" in probe_failed
        and "reciprocal_transfer_values" in probe_failed
    )
    check(
        "3 fourth magnitude-doubled candidate is rejected by named criteria",
        fourth_clean,
        {"failed_criteria": probe_failed, "verdict": probe_verdict},
    )
    return {
        "built_in_verdicts": recounted,
        "fourth_failed_criteria": probe_failed,
        "fourth_verdict": probe_verdict,
        "probe_run": probe_run,
    }


def adversary_recount(
    extracted: dict[str, object], criteria_state: dict[str, object]
) -> dict[str, object]:
    """Independently mutate one expectation and verify that identity fails."""
    landed = criteria_state["own_frozen"]
    wrong = deepcopy(landed)
    wrong["recoil_rows"][0]["matter"] = [
        -value for value in wrong["recoil_rows"][0]["matter"]
    ]
    recoil_residual = max(
        abs(
            landed["recoil_rows"][direction][component][axis]
            - wrong["recoil_rows"][direction][component][axis]
        )
        for direction in range(6)
        for component in ("matter", "mediator", "auxiliary")
        for axis in range(3)
    )
    own_failed = ["recoil_ledger"] if recoil_residual > extracted["strict_tolerance"] else []
    own_verdict = (
        "ACCEPT"
        if not own_failed
        else "DRIFT"
        if recoil_residual <= extracted["drift_limit"]
        else "REJECT"
    )
    harness_row = dict(
        dict(criteria_state["primary_certificate"]).get("adversary_self_test", {})
    )
    clean = (
        own_verdict == "REJECT"
        and own_failed == ["recoil_ledger"]
        and harness_row.get("verdict") == "REJECT"
        and "recoil_ledger" in harness_row.get("failed_criteria", [])
    )
    check(
        "4 wrong-expectation adversary is caught independently and by the harness",
        clean,
        {
            "failed_criteria": own_failed,
            "largest_residual": recoil_residual,
            "verdict": own_verdict,
        },
    )
    return {"failed_criteria": own_failed, "verdict": own_verdict}


def module_root(node: ast.AST) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def target_nodes(node: ast.AST) -> list[ast.AST]:
    if isinstance(node, (ast.Tuple, ast.List)):
        output = []
        for element in node.elts:
            output.extend(target_nodes(element))
        return output
    return [node]


def write_audit(tree: ast.AST) -> dict[str, object]:
    landed_writes = []
    mutation_calls = []
    file_writes = []
    for node in ast.walk(tree):
        targets = []
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            raw = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in raw:
                targets.extend(target_nodes(target))
        elif isinstance(node, (ast.Delete, ast.NamedExpr)):
            raw = node.targets if isinstance(node, ast.Delete) else [node.target]
            for target in raw:
                targets.extend(target_nodes(target))
        for target in targets:
            if module_root(target) in {"S322", "U320"}:
                landed_writes.append(getattr(node, "lineno", -1))
        if not isinstance(node, ast.Call):
            continue
        if (
            isinstance(node.func, ast.Name)
            and node.func.id in {"setattr", "delattr"}
            and node.args
            and module_root(node.args[0]) in {"S322", "U320"}
        ):
            mutation_calls.append((node.func.id, node.lineno))
        if isinstance(node.func, ast.Attribute):
            if (
                node.func.attr
                in {
                    "append",
                    "clear",
                    "extend",
                    "insert",
                    "pop",
                    "remove",
                    "reverse",
                    "sort",
                    "update",
                }
                and module_root(node.func.value) in {"S322", "U320"}
            ):
                mutation_calls.append((node.func.attr, node.lineno))
            if node.func.attr in {
                "chmod",
                "rename",
                "touch",
                "unlink",
                "write_bytes",
                "write_text",
            }:
                file_writes.append((node.func.attr, node.lineno))
        if isinstance(node.func, ast.Name) and node.func.id == "open":
            modes = [
                argument.value
                for argument in node.args[1:2]
                if isinstance(argument, ast.Constant)
                and isinstance(argument.value, str)
            ]
            modes.extend(
                keyword.value.value
                for keyword in node.keywords
                if keyword.arg == "mode"
                and isinstance(keyword.value, ast.Constant)
                and isinstance(keyword.value.value, str)
            )
            if any(set(mode) & set("wax+") for mode in modes):
                file_writes.append(("open", node.lineno))
    return {
        "file_writes": file_writes,
        "landed_writes": landed_writes,
        "mutation_calls": mutation_calls,
    }


def candidate_ast_is_data(tree: ast.AST) -> bool:
    value = assignment_value(tree, "BUILT_IN_CANDIDATES")
    if not isinstance(value, ast.Tuple):
        return False
    for candidate in value.elts:
        if not (
            isinstance(candidate, ast.Call)
            and isinstance(candidate.func, ast.Name)
            and candidate.func.id == "ResponseKernelCandidate"
            and not candidate.args
        ):
            return False
        for keyword in candidate.keywords:
            allowed = all(
                isinstance(
                    node,
                    (
                        ast.Call,
                        ast.Constant,
                        ast.Load,
                        ast.Name,
                        ast.Tuple,
                        ast.UnaryOp,
                        ast.USub,
                    ),
                )
                and not isinstance(node, (ast.Lambda, ast.comprehension))
                for node in ast.walk(keyword.value)
            )
            if not allowed:
                return False
            for call in (
                node for node in ast.walk(keyword.value) if isinstance(node, ast.Call)
            ):
                if not (
                    isinstance(call.func, ast.Name)
                    and call.func.id == "Fraction"
                    and all(
                        isinstance(argument, (ast.Constant, ast.UnaryOp))
                        for argument in call.args
                    )
                ):
                    return False
    return True


def firewall_recount(
    primary_source: str, primary_tree: ast.AST, own_source: str
) -> dict[str, object]:
    """Apply an independent no-write/data-only interpretation firewall."""
    own_tree = ast.parse(own_source, filename=str(Path(__file__)))
    primary_writes = write_audit(primary_tree)
    own_writes = write_audit(own_tree)
    token = "grav" + "ity"
    candidate_value = assignment_value(primary_tree, "BUILT_IN_CANDIDATES")
    candidate_strings = [
        node.value
        for node in ast.walk(candidate_value)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    ]
    interpretation_strings = [
        node.value
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and token in node.value.lower()
    ]
    prohibitions_only = all(
        any(marker in value.lower() for marker in ("not ", "no ", "nothing "))
        for value in interpretation_strings
    )
    fourth_literal = literal_assignment(own_tree, "FOURTH_CANDIDATE")
    clean = (
        primary_writes
        == {"file_writes": [], "landed_writes": [], "mutation_calls": []}
        and own_writes
        == {"file_writes": [], "landed_writes": [], "mutation_calls": []}
        and candidate_ast_is_data(primary_tree)
        and fourth_literal == FOURTH_CANDIDATE
        and not any(token in value.lower() for value in candidate_strings)
        and prohibitions_only
    )
    check(
        "5 firewall recount finds data-only candidates and zero landed writes",
        clean,
        {
            "candidate_count": len(candidate_value.elts)
            if isinstance(candidate_value, ast.Tuple)
            else None,
            "file_writes": len(primary_writes["file_writes"])
            + len(own_writes["file_writes"]),
            "landed_writes": len(primary_writes["landed_writes"])
            + len(own_writes["landed_writes"]),
            "prohibitions_only": prohibitions_only,
        },
    )
    return {
        "candidates_are_data": candidate_ast_is_data(primary_tree),
        "file_writes": len(primary_writes["file_writes"])
        + len(own_writes["file_writes"]),
        "landed_writes": len(primary_writes["landed_writes"])
        + len(own_writes["landed_writes"]),
        "prohibitions_only": prohibitions_only,
    }


def imported_names(tree: ast.AST) -> set[str]:
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
    return names


def discipline(
    own_source: str,
    extracted: dict[str, object],
    criteria_state: dict[str, object],
) -> dict[str, object]:
    """Verify the literal header, import blocklist, and verbatim boundary."""
    tree = ast.parse(own_source, filename=str(Path(__file__)))
    imports = imported_names(tree)
    header_clean = (
        literal_assignment(tree, "AUDIT_TIMEOUT_SEC") == 900
        and literal_assignment(tree, "NOTE_PATH") == NOTE_PATH
        and literal_assignment(tree, "AUDIT_INPUT_PATHS") == AUDIT_INPUT_PATHS
    )
    alias_pairs = {
        (alias.name, alias.asname)
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    blocklist_clean = not any(
        blocked == name or name.endswith("." + blocked)
        for blocked in PRIMARY_IMPORT_BLOCKLIST
        for name in imports
    )
    primary_certificate = dict(criteria_state["primary_certificate"])
    boundary = dict(extracted["boundary"])
    boundary_clean = (
        all(text in primary_certificate.get("remaining_w7_components", []) for text in BOUNDARY_LANGUAGE[2:])
        and primary_certificate.get("harness_is_instrument_only") is True
        and primary_certificate.get("response_law_selected") is False
        and primary_certificate.get("w7_closed") is False
        and boundary["response_law_selected"] is False
        and boundary["w7_closed"] is False
    )
    primary_constants = {
        node.value
        for node in ast.walk(extracted["tree"])
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    boundary_clean &= all(text in primary_constants for text in BOUNDARY_LANGUAGE)
    check(
        "6 discipline keeps the primary blocklisted and imports only S322/U320 anchors",
        header_clean
        and blocklist_clean
        and (
            "two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18",
            "S322",
        )
        in alias_pairs
        and (
            "unit_weight_carried_link_recoil_cycle320_2026_07_18",
            "U320",
        )
        in alias_pairs,
        {"blocklist_clean": blocklist_clean, "header_clean": header_clean},
    )
    check(
        "6 boundary language and false closure keys remain verbatim",
        boundary_clean,
        {
            "response_law_selected": primary_certificate.get(
                "response_law_selected"
            ),
            "w7_closed": primary_certificate.get("w7_closed"),
        },
    )
    return {
        "blocklist_clean": blocklist_clean,
        "boundary_verbatim": boundary_clean,
        "header_clean": header_clean,
    }


def main() -> int:
    started = time.monotonic()
    deadline = started + AUDIT_TIMEOUT_SEC
    primary_source = PRIMARY_PATH.read_text(encoding="utf-8")
    own_source = Path(__file__).read_text(encoding="utf-8")

    extracted = extraction(primary_source)
    criteria_state = criteria_recount(deadline, extracted)
    candidates = candidate_recount(
        deadline, primary_source, extracted, criteria_state
    )
    adversary = adversary_recount(extracted, criteria_state)
    firewall = firewall_recount(
        primary_source, extracted["tree"], own_source  # type: ignore[arg-type]
    )
    disciplined = discipline(own_source, extracted, criteria_state)

    runtime = time.monotonic() - started
    certificate = {
        "adversary": adversary,
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "boundary": {
            "response_law_selected": False,
            "w7_closed": False,
        },
        "candidate_verdicts": candidates["built_in_verdicts"],
        "discipline": disciplined,
        "fail": FAIL,
        "firewall": firewall,
        "fourth_candidate": {
            "failed_criteria": candidates["fourth_failed_criteria"],
            "name": FOURTH_CANDIDATE["name"],
            "verdict": candidates["fourth_verdict"],
        },
        "note_path": NOTE_PATH,
        "pass": PASS,
        "runtime_sec": round(runtime, 6),
    }
    print(json.dumps(certificate, sort_keys=True, separators=(",", ":")))
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
