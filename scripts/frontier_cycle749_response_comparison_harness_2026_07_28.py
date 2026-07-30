#!/usr/bin/env python3
"""Cycle 749: bounded response-candidate comparison instrument.

The landed Cycle-320 recoil ledger and Cycle-322 reciprocal transfer are
acceptance fixtures.  Every response kernel below is supplied demonstration
data.  This harness selects and derives no response law or physical meaning.
"""

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/RESPONSE_COMPARISON_HARNESS_CYCLE749_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from dataclasses import dataclass, fields
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from typing import NamedTuple

import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322
import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320


ROOT = Path(__file__).resolve().parents[1]
STRICT_TOLERANCE = Fraction(3, 10_000_000_000)
DRIFT_LIMIT = Fraction(1, 1_000_000)
PASS = 0
FAIL = 0

# Verbatim operative C_source declarations supplied by the W7 scope authority.
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


def check(label: str, condition: bool, detail: object = "") -> None:
    """Emit the only human-readable result-line form used by the harness."""
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def bounded_tail(text: str, limit: int = 2000) -> str:
    return text[-limit:].replace("\x00", "\\0")


def own_run(path: str, expected_result: str, timeout: float) -> dict[str, object]:
    """Run one landed anchor while capturing, rather than relaying, its output."""
    started = time.monotonic()
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "scripts")
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        completed = subprocess.run(
            [sys.executable, str(ROOT / path)],
            cwd=ROOT,
            env=environment,
            capture_output=True,
            text=True,
            timeout=max(1.0, timeout),
            check=False,
        )
        stdout = completed.stdout
        stderr = completed.stderr
        fail_lines = tuple(
            line for line in stdout.splitlines() if line.startswith("FAIL ")
        )
        pass_lines = sum(
            line.startswith("PASS ") for line in stdout.splitlines()
        )
        return {
            "completed": True,
            "exit_code": completed.returncode,
            "expected_result_seen": expected_result in stdout,
            "fail_line_count": len(fail_lines),
            "pass_line_count": pass_lines,
            "runtime_sec": round(time.monotonic() - started, 6),
            "stdout_bytes": len(stdout.encode("utf-8")),
            "stdout_sha256": sha256_bytes(stdout.encode("utf-8")),
            "stderr_bytes": len(stderr.encode("utf-8")),
            "failure_tail": bounded_tail(
                stderr if stderr else "\n".join(fail_lines)
            ),
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
            "expected_result_seen": False,
            "fail_line_count": None,
            "pass_line_count": None,
            "runtime_sec": round(time.monotonic() - started, 6),
            "stdout_bytes": len(stdout.encode("utf-8")),
            "stdout_sha256": sha256_bytes(stdout.encode("utf-8")),
            "stderr_bytes": len(stderr.encode("utf-8")),
            "failure_tail": bounded_tail(stderr or "AUDIT_TIMEOUT"),
        }


def anchor_passed(row: dict[str, object]) -> bool:
    return bool(
        row["completed"]
        and row["exit_code"] == 0
        and row["expected_result_seen"]
        and row["fail_line_count"] == 0
        and isinstance(row["pass_line_count"], int)
        and row["pass_line_count"] > 0
    )


class FrozenFixtures(NamedTuple):
    recoil_rows: tuple[
        tuple[
            tuple[Fraction, Fraction, Fraction],
            tuple[Fraction, Fraction, Fraction],
            tuple[Fraction, Fraction, Fraction],
        ],
        ...,
    ]
    response_rows: tuple[
        tuple[
            int,
            tuple[
                tuple[Fraction, Fraction],
                tuple[Fraction, Fraction],
            ],
            Fraction,
        ],
        ...,
    ]


def fraction_vector(values: object) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(Fraction(int(value)) for value in values)  # type: ignore[return-value]


def extract_frozen_fixtures() -> FrozenFixtures:
    """Extract landed source facts before any candidate is evaluated."""
    recoil_rows = []
    for direction in range(6):
        source = fraction_vector(U320.c210.DIRECTIONS[direction])
        target = fraction_vector(U320.c210.DIRECTIONS[U320.REVERSE[direction]])
        matter = tuple(target[axis] - source[axis] for axis in range(3))
        mediator = source
        auxiliary = source
        recoil_rows.append((matter, mediator, auxiliary))

    coin, fswap, contact, _update, _details = S322.c315.logical_update_controls(
        S322.LABELS
    )
    factors = (coin, fswap, contact)
    response_rows = []
    for length in S322.SIZES:
        matrix, norm_drift = S322.response_matrix(length, factors)
        frozen_matrix = tuple(
            tuple(Fraction(float(matrix[row, column])) for column in range(2))
            for row in range(2)
        )
        response_rows.append(
            (length, frozen_matrix, Fraction(float(norm_drift)))
        )
    return FrozenFixtures(tuple(recoil_rows), tuple(response_rows))


@dataclass(frozen=True)
class ResponseKernelCandidate:
    """Supplied diagonal response-kernel data; it has no fitting behavior."""

    name: str
    recoil_coefficients: tuple[Fraction, Fraction, Fraction]
    transfer_coefficients: tuple[Fraction, Fraction, Fraction, Fraction]
    fitted_defaults: tuple[
        Fraction,
        Fraction,
        Fraction,
        Fraction,
        Fraction,
        Fraction,
        Fraction,
    ]
    demonstration_role: str


ZERO_DEFAULTS = (Fraction(0),) * 7
BUILT_IN_CANDIDATES = (
    ResponseKernelCandidate(
        name="identity_pullback",
        recoil_coefficients=(Fraction(1), Fraction(1), Fraction(1)),
        transfer_coefficients=(
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1),
        ),
        fitted_defaults=ZERO_DEFAULTS,
        demonstration_role="reproduces landed facts; demonstration only",
    ),
    ResponseKernelCandidate(
        name="sign_flipped",
        recoil_coefficients=(Fraction(-1), Fraction(-1), Fraction(-1)),
        transfer_coefficients=(
            Fraction(-1),
            Fraction(-1),
            Fraction(-1),
            Fraction(-1),
        ),
        fitted_defaults=ZERO_DEFAULTS,
        demonstration_role="deliberately wrong structural control",
    ),
    ResponseKernelCandidate(
        name="coefficient_drift",
        recoil_coefficients=(
            Fraction(5_000_000_001, 5_000_000_000),
            Fraction(1),
            Fraction(1),
        ),
        transfer_coefficients=(
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1),
        ),
        fitted_defaults=ZERO_DEFAULTS,
        demonstration_role="deliberate tolerance-scale perturbation",
    ),
)
EXPECTED_BUILT_IN_VERDICTS = {
    "identity_pullback": "ACCEPT",
    "sign_flipped": "REJECT",
    "coefficient_drift": "DRIFT",
}


def maximum(values: list[Fraction]) -> Fraction:
    return max(values, default=Fraction(0))


def evaluate_candidate(
    candidate: ResponseKernelCandidate,
    landed: FrozenFixtures,
    expected: FrozenFixtures,
) -> dict[str, object]:
    actual_recoil_rows = []
    for row in landed.recoil_rows:
        transformed = []
        for component_index, vector in enumerate(row):
            coefficient = candidate.recoil_coefficients[component_index]
            offset = candidate.fitted_defaults[component_index]
            transformed.append(
                tuple(coefficient * value + offset for value in vector)
            )
        actual_recoil_rows.append(tuple(transformed))

    recoil_residuals = []
    balance_residuals = []
    for actual, frozen in zip(actual_recoil_rows, expected.recoil_rows):
        for actual_vector, frozen_vector in zip(actual, frozen):
            recoil_residuals.extend(
                abs(actual_vector[axis] - frozen_vector[axis])
                for axis in range(3)
            )
        balance_residuals.extend(
            abs(sum(actual[component][axis] for component in range(3)))
            for axis in range(3)
        )

    transfer_value_residuals = []
    reciprocity_residuals = []
    diagonal_residuals = []
    norm_residuals = []
    for landed_row, expected_row in zip(
        landed.response_rows, expected.response_rows
    ):
        length, matrix, norm_drift = landed_row
        expected_length, frozen_matrix, frozen_norm_drift = expected_row
        if length != expected_length:
            transfer_value_residuals.append(Fraction(1))
        flat = (matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1])
        transformed_flat = tuple(
            candidate.transfer_coefficients[index] * value
            + candidate.fitted_defaults[3 + index]
            for index, value in enumerate(flat)
        )
        actual_matrix = (
            (transformed_flat[0], transformed_flat[1]),
            (transformed_flat[2], transformed_flat[3]),
        )
        transfer_value_residuals.extend(
            abs(actual_matrix[row][column] - frozen_matrix[row][column])
            for row in range(2)
            for column in range(2)
        )
        reciprocity_residuals.append(
            abs(
                (actual_matrix[0][1] - actual_matrix[1][0])
                - (frozen_matrix[0][1] - frozen_matrix[1][0])
            )
        )
        diagonal_residuals.append(
            abs(
                (actual_matrix[0][0] - actual_matrix[1][1])
                - (frozen_matrix[0][0] - frozen_matrix[1][1])
            )
        )
        norm_residuals.append(abs(norm_drift - frozen_norm_drift))

    residuals = {
        "diagonal_exchange_residual": maximum(diagonal_residuals),
        "flux_balance": maximum(balance_residuals),
        "norm_drift": maximum(norm_residuals),
        "reciprocal_transfer_values": maximum(transfer_value_residuals),
        "reciprocity_residual": maximum(reciprocity_residuals),
        "recoil_ledger": maximum(recoil_residuals),
    }
    failed_criteria = tuple(
        name
        for name, residual in sorted(residuals.items())
        if residual > STRICT_TOLERANCE
    )
    largest_residual = maximum(list(residuals.values()))
    if not failed_criteria:
        verdict = "ACCEPT"
    elif largest_residual <= DRIFT_LIMIT:
        verdict = "DRIFT"
    else:
        verdict = "REJECT"
    return {
        "candidate": candidate.name,
        "failed_criteria": list(failed_criteria),
        "largest_residual": float(largest_residual),
        "residuals": {
            name: float(value) for name, value in sorted(residuals.items())
        },
        "strict_tolerance": float(STRICT_TOLERANCE),
        "verdict": verdict,
    }


def mutated_expectation(fixtures: FrozenFixtures) -> FrozenFixtures:
    rows = list(fixtures.recoil_rows)
    first = list(rows[0])
    first[0] = tuple(-value for value in first[0])
    rows[0] = tuple(first)
    return FrozenFixtures(tuple(rows), fixtures.response_rows)


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


def firewall_ast_audit(source: str) -> dict[str, object]:
    tree = ast.parse(source)
    writes = []
    forbidden_calls = []
    for node in ast.walk(tree):
        targets = []
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            raw_targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in raw_targets:
                targets.extend(target_nodes(target))
        elif isinstance(node, (ast.Delete, ast.NamedExpr)):
            raw_targets = node.targets if isinstance(node, ast.Delete) else [node.target]
            for target in raw_targets:
                targets.extend(target_nodes(target))
        for target in targets:
            root = module_root(target)
            if root in {"S322", "U320"}:
                writes.append(
                    {"line": getattr(node, "lineno", -1), "module": root}
                )
        if isinstance(node, ast.Call):
            if (
                isinstance(node.func, ast.Name)
                and node.func.id in {"setattr", "delattr"}
                and node.args
                and module_root(node.args[0]) in {"S322", "U320"}
            ):
                forbidden_calls.append(
                    {"call": node.func.id, "line": node.lineno}
                )
            if (
                isinstance(node.func, ast.Attribute)
                and node.func.attr
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
                forbidden_calls.append(
                    {"call": node.func.attr, "line": node.lineno}
                )
    return {
        "landed_module_mutation_calls": forbidden_calls,
        "landed_module_write_targets": writes,
        "passed": not writes and not forbidden_calls,
    }


def json_fixture_summary(fixtures: FrozenFixtures) -> dict[str, object]:
    recoil = []
    for direction, row in enumerate(fixtures.recoil_rows):
        recoil.append(
            {
                "auxiliary": [int(value) for value in row[2]],
                "direction": direction,
                "matter": [int(value) for value in row[0]],
                "mediator": [int(value) for value in row[1]],
            }
        )
    response = []
    for length, matrix, norm_drift in fixtures.response_rows:
        response.append(
            {
                "L": length,
                "diagonal_exchange_residual": float(
                    abs(matrix[0][0] - matrix[1][1])
                ),
                "held_out": length == S322.HELD_SIZE,
                "norm_drift": float(norm_drift),
                "off_diagonal_minimum": float(
                    min(matrix[0][1], matrix[1][0])
                ),
                "reciprocity_residual": float(
                    abs(matrix[0][1] - matrix[1][0])
                ),
                "response_matrix": [
                    [float(value) for value in row] for row in matrix
                ],
            }
        )
    return {"recoil_rows": recoil, "response_rows": response}


def main() -> int:
    started = time.monotonic()

    input_bytes = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    input_shas = {
        path: sha256_bytes(data) for path, data in input_bytes.items()
    }
    check(
        "A declared inputs are the two pure landed runner paths",
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and isinstance(AUDIT_INPUT_PATHS, tuple)
        and len(AUDIT_INPUT_PATHS) == 2
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        {"paths": AUDIT_INPUT_PATHS},
    )
    check(
        "A landed runner SHA-256 anchors are complete",
        all(re.fullmatch(r"[0-9a-f]{64}", digest) for digest in input_shas.values()),
        input_shas,
    )

    deadline = time.monotonic() + AUDIT_TIMEOUT_SEC
    anchor_rows = {
        "S322": own_run(
            AUDIT_INPUT_PATHS[0],
            "RESULT TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CERTIFIED",
            deadline - time.monotonic(),
        ),
        "U320": own_run(
            AUDIT_INPUT_PATHS[1],
            "RESULT UNIT_WEIGHT_CARRIED_LINK_RECOIL_FACTOR_CERTIFIED",
            deadline - time.monotonic(),
        ),
    }
    check(
        "A S322 own run is all-PASS",
        anchor_passed(anchor_rows["S322"]),
        anchor_rows["S322"],
    )
    check(
        "A U320 own run is all-PASS",
        anchor_passed(anchor_rows["U320"]),
        anchor_rows["U320"],
    )

    fixtures = extract_frozen_fixtures()
    fixture_summary = json_fixture_summary(fixtures)
    exact_recoil = True
    exact_balance = True
    for direction, row in enumerate(fixtures.recoil_rows):
        source = fraction_vector(U320.c210.DIRECTIONS[direction])
        exact_recoil &= (
            row[0] == tuple(-2 * value for value in source)
            and row[1] == source
            and row[2] == source
        )
        exact_balance &= all(
            sum(row[component][axis] for component in range(3)) == 0
            for axis in range(3)
        )
    check(
        "B frozen Cycle-320 recoil criteria are exactly (-2d,+d,+d)",
        exact_recoil and len(fixtures.recoil_rows) == 6,
        {"directions": len(fixtures.recoil_rows)},
    )
    check(
        "B frozen Cycle-320 flux balance is exact",
        exact_balance,
        {"maximum_balance_residual": 0 if exact_balance else "nonzero"},
    )
    landed_response_clean = all(
        min(matrix[0][1], matrix[1][0]) > Fraction(6, 10_000)
        and abs(matrix[0][1] - matrix[1][0]) <= STRICT_TOLERANCE
        and abs(matrix[0][0] - matrix[1][1]) <= STRICT_TOLERANCE
        and norm_drift <= STRICT_TOLERANCE
        for _length, matrix, norm_drift in fixtures.response_rows
    )
    check(
        "B frozen Cycle-322 reciprocal transfer criteria hold through held L=6",
        landed_response_clean
        and tuple(row[0] for row in fixtures.response_rows) == tuple(S322.SIZES)
        and any(row[0] == S322.HELD_SIZE for row in fixtures.response_rows),
        fixture_summary["response_rows"],
    )
    check(
        "B landed tolerance is shared and frozen before candidate evaluation",
        Fraction(float(S322.TOLERANCE)) == Fraction(float(U320.TOLERANCE))
        and float(STRICT_TOLERANCE) == S322.TOLERANCE,
        {
            "drift_limit": float(DRIFT_LIMIT),
            "strict_tolerance": float(STRICT_TOLERANCE),
        },
    )

    all_fraction_data = all(
        all(isinstance(value, Fraction) for value in candidate.recoil_coefficients)
        and all(
            isinstance(value, Fraction)
            for value in candidate.transfer_coefficients
        )
        and all(
            isinstance(value, Fraction) and value == 0
            for value in candidate.fitted_defaults
        )
        for candidate in BUILT_IN_CANDIDATES
    )
    check(
        "C candidate schema is frozen Fraction data with zero fitted defaults",
        ResponseKernelCandidate.__dataclass_params__.frozen
        and tuple(field.name for field in fields(ResponseKernelCandidate))
        == (
            "name",
            "recoil_coefficients",
            "transfer_coefficients",
            "fitted_defaults",
            "demonstration_role",
        )
        and all_fraction_data,
        {"candidate_count": len(BUILT_IN_CANDIDATES)},
    )
    evaluations = {
        candidate.name: evaluate_candidate(candidate, fixtures, fixtures)
        for candidate in BUILT_IN_CANDIDATES
    }
    actual_verdicts = {
        name: row["verdict"] for name, row in evaluations.items()
    }
    check(
        "C identity pullback reproduces every landed criterion",
        actual_verdicts["identity_pullback"] == "ACCEPT"
        and not evaluations["identity_pullback"]["failed_criteria"],
        evaluations["identity_pullback"],
    )
    check(
        "C sign-flipped kernel is rejected by named frozen criteria",
        actual_verdicts["sign_flipped"] == "REJECT"
        and "recoil_ledger" in evaluations["sign_flipped"]["failed_criteria"]
        and "reciprocal_transfer_values"
        in evaluations["sign_flipped"]["failed_criteria"],
        evaluations["sign_flipped"],
    )
    check(
        "C perturbed coefficient is caught as tolerance-scale drift",
        actual_verdicts["coefficient_drift"] == "DRIFT"
        and "recoil_ledger"
        in evaluations["coefficient_drift"]["failed_criteria"]
        and evaluations["coefficient_drift"]["largest_residual"]
        > float(STRICT_TOLERANCE),
        evaluations["coefficient_drift"],
    )
    check(
        "C built-in candidate verdicts remain frozen demonstration data",
        actual_verdicts == EXPECTED_BUILT_IN_VERDICTS,
        actual_verdicts,
    )

    wrong_expected = mutated_expectation(fixtures)
    adversary = evaluate_candidate(
        BUILT_IN_CANDIDATES[0], fixtures, wrong_expected
    )
    check(
        "D adversary self-test catches a wrong frozen recoil expectation",
        adversary["verdict"] == "REJECT"
        and "recoil_ledger" in adversary["failed_criteria"],
        adversary,
    )

    source = Path(__file__).read_text(encoding="utf-8")
    firewall = firewall_ast_audit(source)
    check(
        "E AST firewall finds no landed-module writes or mutation calls",
        bool(firewall["passed"]),
        firewall,
    )
    landed_text = "\n".join(
        data.decode("utf-8") for data in input_bytes.values()
    )
    normalized_landed_text = " ".join(landed_text.split())
    check(
        "E landed C_source declarations remain verbatim",
        all(
            " ".join(statement.split()) in normalized_landed_text
            for statement in C_source[:4]
        ),
        {"verified_declarations": 4},
    )
    check(
        "E C_source authority is a prohibition set, not candidate content",
        len(C_source) == 8
        and all(
            any(
                token in statement.lower()
                for token in ("not ", "no ", "nothing ")
            )
            for statement in C_source
        )
        and all(
            "C_source" not in candidate.demonstration_role
            for candidate in BUILT_IN_CANDIDATES
        ),
        {"declarations": len(C_source)},
    )

    remaining_w7_components = [
        "field/metric response law",
        "no-refit prediction attachment",
    ]
    supplies = {
        "acceptance_fixtures": "derived from landed S322/U320 source-side structure",
        "candidate_coefficients": "supplied Fraction data",
        "candidate_defaults": "all zero; no fitted values",
        "physical_interpretation": "none supplied",
    }
    check(
        "F boundary keeps W7 open and records both remaining components",
        remaining_w7_components
        == [
            "field/metric response law",
            "no-refit prediction attachment",
        ],
        {
            "harness_is_instrument_only": True,
            "response_law_selected": False,
            "w7_closed": False,
        },
    )
    check(
        "F no-refit prediction attachment remains explicitly unclaimed",
        "no-refit prediction attachment" in remaining_w7_components
        and supplies["candidate_defaults"] == "all zero; no fitted values",
        supplies,
    )

    verdict_census = {
        verdict: sum(value == verdict for value in actual_verdicts.values())
        for verdict in ("ACCEPT", "DRIFT", "REJECT")
    }
    certificate = {
        "adversary_self_test": adversary,
        "anchors": {
            name: {
                **row,
                "input_path": AUDIT_INPUT_PATHS[0 if name == "S322" else 1],
                "input_sha256": input_shas[
                    AUDIT_INPUT_PATHS[0 if name == "S322" else 1]
                ],
            }
            for name, row in anchor_rows.items()
        },
        "candidate_evaluations": evaluations,
        "candidate_verdict_census": verdict_census,
        "declared_input_paths": list(DECLARED_INPUT_PATHS),
        "fail": FAIL,
        "firewall_audits": {
            "ast": firewall,
            "c_source_declarations": list(C_source),
            "verified_landed_declarations": 4,
        },
        "frozen_criteria": fixture_summary,
        "harness_is_instrument_only": True,
        "note_path": NOTE_PATH,
        "pass": PASS,
        "remaining_w7_components": remaining_w7_components,
        "response_law_selected": False,
        "runtime_sec": round(time.monotonic() - started, 6),
        "supplies": supplies,
        "w7_closed": False,
    }
    print(json.dumps(certificate, sort_keys=True, separators=(",", ":")))
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
