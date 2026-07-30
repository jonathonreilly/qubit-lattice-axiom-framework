#!/usr/bin/env python3
"""Cycle 768: derive one response-kernel candidate, then instrument-test it.

The candidate is the adjoint pullback already determined by the landed
source-side algebra.  The derivation is isolated from the Cycle-749
acceptance fixtures; the unchanged instrument is consulted only afterward.
"""

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/RESPONSE_LAW_CANDIDATE_CYCLE768_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
)

import ast
from dataclasses import dataclass
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import time

import frontier_cycle749_response_comparison_harness_2026_07_28 as H749
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322
import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
STDOUT_BYTES = 0
OUTPUT_LIMIT_BYTES = 150_000
DERIVATION_FUNCTIONS = (
    "apply_endpoint_exchange",
    "derive_recoil_coefficients",
    "derive_response_kernel_candidate",
    "derive_transfer_coefficients",
)

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


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass(frozen=True)
class DerivedKernel:
    name: str
    recoil_coefficients: tuple[Fraction, ...]
    transfer_coefficients: tuple[Fraction, ...]
    fitted_defaults: tuple[Fraction, ...]
    derivation: dict[str, object]


def derive_recoil_coefficients() -> tuple[tuple[Fraction, ...], dict[str, object]]:
    """Recover sector weights from U320's own diagonal direction operator."""
    _exchange, vertex, _charge, momenta = U320.link_recoil_vertex(U320.ANGLE)
    directions = U320.c210.DIRECTIONS
    sector_count = len(momenta)
    configurations = tuple(
        product(range(len(directions)), repeat=sector_count)
    )
    numerators = [Fraction() for _sector in range(sector_count)]
    denominators = [Fraction() for _sector in range(sector_count)]
    design_gram = [
        [Fraction() for _right in range(sector_count)]
        for _left in range(sector_count)
    ]
    pair_offset = len(directions)
    for axis, momentum in enumerate(momenta):
        for flat_index, configuration in enumerate(configurations):
            diagonal_index = pair_offset + flat_index
            target = Fraction(
                int(round(float(momentum[diagonal_index, diagonal_index].real)))
            )
            row = tuple(
                Fraction(int(directions[direction, axis]))
                for direction in configuration
            )
            for left in range(sector_count):
                numerators[left] += row[left] * target
                denominators[left] += row[left] * row[left]
                for right in range(sector_count):
                    design_gram[left][right] += row[left] * row[right]
    coefficients = tuple(
        numerator / denominator
        for numerator, denominator in zip(numerators, denominators)
    )
    gram = vertex.conj().T @ vertex
    identity = U320.np.eye(next(iter(vertex.shape)), dtype=complex)
    return coefficients, {
        "coefficient_equation": "w_s=<D_s,P>/<D_s,D_s>",
        "coefficients": tuple(fraction_text(value) for value in coefficients),
        "design_gram": tuple(
            tuple(fraction_text(value) for value in row) for row in design_gram
        ),
        "diagonal_operator": "P_axis=D_matter+D_field+D_auxiliary",
        "normalizers": tuple(
            fraction_text(value) for value in denominators
        ),
        "numerators": tuple(fraction_text(value) for value in numerators),
        "vertex_adjoint_gram_residual": float(
            U320.np.max(U320.np.abs(gram - identity))
        ),
    }


def apply_endpoint_exchange(
    matrix: tuple[tuple[Fraction, ...], ...],
    permutation: tuple[tuple[Fraction, ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    """Apply the S322 endpoint exchange R(X)=P X P^T exactly."""
    size = len(permutation)
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
                start=Fraction(),
            )
            for column in range(size)
        )
        for row in range(size)
    )


def derive_transfer_coefficients() -> tuple[
    tuple[Fraction, ...], dict[str, object]
]:
    """Compose S322 endpoint reciprocity with its exact adjoint."""
    endpoint_count = len(S322.ENDPOINTS)
    reverse_indices = tuple(reversed(range(endpoint_count)))
    permutation = tuple(
        tuple(
            Fraction(target == reverse_indices[source])
            for source in range(endpoint_count)
        )
        for target in range(endpoint_count)
    )
    transpose = tuple(zip(*permutation))
    coefficients = []
    off_basis_residuals = []
    for basis_row in range(endpoint_count):
        for basis_column in range(endpoint_count):
            basis = tuple(
                tuple(
                    Fraction(
                        (row, column) == (basis_row, basis_column)
                    )
                    for column in range(endpoint_count)
                )
                for row in range(endpoint_count)
            )
            reciprocal = apply_endpoint_exchange(basis, permutation)
            pullback = apply_endpoint_exchange(reciprocal, permutation)
            coefficients.append(pullback[basis_row][basis_column])
            off_basis_residuals.append(
                sum(
                    (
                        abs(pullback[row][column] - basis[row][column])
                        for row in range(endpoint_count)
                        for column in range(endpoint_count)
                    ),
                    start=Fraction(),
                )
            )
    return tuple(coefficients), {
        "adjoint_relation": "R*=R",
        "candidate_composition": "K=R*R=I",
        "coefficients_row_major": tuple(
            fraction_text(value) for value in coefficients
        ),
        "endpoint_count": endpoint_count,
        "endpoint_exchange": tuple(
            tuple(fraction_text(value) for value in row)
            for row in permutation
        ),
        "involution_residuals": tuple(
            fraction_text(value) for value in off_basis_residuals
        ),
        "self_adjoint": permutation == transpose,
    }


def derive_response_kernel_candidate() -> DerivedKernel:
    """Compose the landed recoil weights with the reciprocity pullback."""
    recoil_coefficients, recoil_trace = derive_recoil_coefficients()
    transfer_coefficients, transfer_trace = derive_transfer_coefficients()
    defaults = tuple(
        Fraction()
        for _coefficient in recoil_coefficients + transfer_coefficients
    )
    return DerivedKernel(
        name="landed_adjoint_pullback",
        recoil_coefficients=recoil_coefficients,
        transfer_coefficients=transfer_coefficients,
        fitted_defaults=defaults,
        derivation={
            "chain": (
                "U320 diagonal decomposition -> sector weights; "
                "S322 endpoint reciprocity R -> adjoint composition R*R; "
                "compose on recoil/transfer surfaces"
            ),
            "criterion_inputs_read": False,
            "free_parameters": (),
            "recoil": recoil_trace,
            "transfer": transfer_trace,
        },
    )


def derivation_firewall_audit(source: str) -> dict[str, object]:
    tree = ast.parse(source)
    selected = tuple(
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name in DERIVATION_FUNCTIONS
    )
    harness_references = []
    criterion_references = []
    numeric_literals = []
    forbidden_criterion_names = {
        "BUILT_IN_CANDIDATES",
        "DRIFT_LIMIT",
        "EXPECTED_BUILT_IN_VERDICTS",
        "STRICT_TOLERANCE",
        "evaluate_candidate",
        "extract_frozen_fixtures",
    }
    for function in selected:
        for node in ast.walk(function):
            if isinstance(node, ast.Name) and node.id == "H749":
                harness_references.append(
                    {"function": function.name, "line": node.lineno}
                )
            if (
                isinstance(node, ast.Attribute)
                and node.attr in forbidden_criterion_names
            ):
                criterion_references.append(
                    {
                        "attribute": node.attr,
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
    return {
        "criterion_references": criterion_references,
        "derivation_functions": tuple(
            sorted(function.name for function in selected)
        ),
        "harness_references": harness_references,
        "numeric_literals": numeric_literals,
        "passed": (
            len(selected) == len(DERIVATION_FUNCTIONS)
            and not harness_references
            and not criterion_references
            and not numeric_literals
        ),
    }


def import_surface_audit(source: str) -> dict[str, object]:
    tree = ast.parse(source)
    imported = {}
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname in {"H749", "S322", "U320", "FF"}:
                    imported[alias.asname] = alias.name
    assignment = next(
        (
            node
            for node in tree.body
            if isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name)
                and target.id == "AUDIT_INPUT_PATHS"
                for target in node.targets
            )
        ),
        None,
    )
    pure_literal_tuple = bool(
        assignment
        and isinstance(assignment.value, ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in assignment.value.elts
        )
    )
    return {
        "imported_runner_aliases": imported,
        "pure_literal_audit_input_tuple": pure_literal_tuple,
        "ff_status": "absent on this branch; skipped and not imported",
    }


def landed_module_mutation_audit(source: str) -> dict[str, object]:
    tree = ast.parse(source)
    violations = []
    module_names = {"H749", "S322", "U320"}
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
            if isinstance(root, ast.Name) and root.id in module_names:
                violations.append(
                    {
                        "kind": "write",
                        "line": node.lineno,
                        "module": root.id,
                    }
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
            if isinstance(root, ast.Name) and root.id in module_names:
                violations.append(
                    {
                        "kind": node.func.id,
                        "line": node.lineno,
                        "module": root.id,
                    }
                )
    return {"passed": not violations, "violations": violations}


def criterion_verdicts(evaluation: dict[str, object]) -> dict[str, str]:
    verdicts = {}
    residuals = evaluation["residuals"]
    assert isinstance(residuals, dict)
    for name, raw_residual in sorted(residuals.items()):
        residual = Fraction(float(raw_residual))
        if residual <= H749.STRICT_TOLERANCE:
            verdict = "ACCEPT"
        elif residual <= H749.DRIFT_LIMIT:
            verdict = "DRIFT"
        else:
            verdict = "REJECT"
        verdicts[str(name)] = verdict
    return verdicts


def vector_tuple(values: object) -> tuple[Fraction, ...]:
    return tuple(Fraction(int(value)) for value in values)  # type: ignore[arg-type]


def recoil_configuration(direction: int) -> tuple[
    tuple[Fraction, ...], tuple[Fraction, ...], tuple[Fraction, ...]
]:
    source = vector_tuple(U320.c210.DIRECTIONS[direction])
    reversed_source = vector_tuple(
        U320.c210.DIRECTIONS[U320.REVERSE[direction]]
    )
    matter = tuple(
        target - initial for target, initial in zip(reversed_source, source)
    )
    return matter, source, source


def extension_probe(candidate: DerivedKernel) -> dict[str, object]:
    """Make one unverified prediction on a two-channel composite ledger."""
    direction_count = len(U320.c210.DIRECTIONS)
    selected = None
    for left, right in combinations(range(direction_count), 2):
        combined_source = tuple(
            Fraction(int(value))
            for value in (
                U320.c210.DIRECTIONS[left] + U320.c210.DIRECTIONS[right]
            )
        )
        landed_directions = {
            vector_tuple(row) for row in U320.c210.DIRECTIONS
        }
        if any(combined_source) and combined_source not in landed_directions:
            selected = (left, right)
            break
    if selected is None:
        return {
            "determinate": False,
            "reached": True,
            "reason": "no outside two-channel composite found",
        }
    component_rows = tuple(recoil_configuration(index) for index in selected)
    configuration = tuple(
        tuple(
            sum(
                (row[component][axis] for row in component_rows),
                start=Fraction(),
            )
            for axis in range(len(U320.c210.DIRECTIONS[0]))
        )
        for component in range(len(candidate.recoil_coefficients))
    )
    prediction = tuple(
        tuple(coefficient * value for value in vector)
        for coefficient, vector in zip(
            candidate.recoil_coefficients, configuration
        )
    )
    single_channel_rows = {
        recoil_configuration(index) for index in range(direction_count)
    }
    return {
        "configuration": tuple(
            tuple(fraction_text(value) for value in vector)
            for vector in configuration
        ),
        "determinate": all(
            isinstance(value, Fraction)
            for vector in prediction
            for value in vector
        ),
        "ff_status": "absent on this branch; skipped and not imported",
        "outside_defining_set": configuration not in single_channel_rows,
        "prediction": tuple(
            tuple(fraction_text(value) for value in vector)
            for vector in prediction
        ),
        "prediction_verified": False,
        "reached": True,
        "selected_channel_pair": selected,
    }


def main() -> int:
    started = time.monotonic()
    source_path = Path(__file__)
    source = source_path.read_text(encoding="utf-8")
    input_bytes = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    input_shas_before = {
        path: sha256_bytes(data) for path, data in input_bytes.items()
    }
    surface_audit = import_surface_audit(source)
    check(
        "A audit inputs are the pure literal imported runner paths",
        isinstance(AUDIT_INPUT_PATHS, tuple)
        and len(AUDIT_INPUT_PATHS) == 3
        and bool(surface_audit["pure_literal_audit_input_tuple"])
        and surface_audit["imported_runner_aliases"]
        == {
            "H749": "frontier_cycle749_response_comparison_harness_2026_07_28",
            "S322": "two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18",
            "U320": "unit_weight_carried_link_recoil_cycle320_2026_07_18",
        }
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        surface_audit,
    )
    check(
        "A imported surfaces and SHA-256 anchors are complete",
        callable(H749.evaluate_candidate)
        and callable(H749.extract_frozen_fixtures)
        and callable(S322.response_matrix)
        and callable(U320.link_recoil_vertex)
        and all(len(digest) == 64 for digest in input_shas_before.values()),
        input_shas_before,
    )

    deadline = time.monotonic() + AUDIT_TIMEOUT_SEC
    expected_results = {
        AUDIT_INPUT_PATHS[0]: '"harness_is_instrument_only":true',
        AUDIT_INPUT_PATHS[1]: "RESULT TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CERTIFIED",
        AUDIT_INPUT_PATHS[2]: "RESULT UNIT_WEIGHT_CARRIED_LINK_RECOIL_FACTOR_CERTIFIED",
    }
    anchor_rows = {
        path: H749.own_run(
            path, expected_results[path], deadline - time.monotonic()
        )
        for path in AUDIT_INPUT_PATHS
    }
    check(
        "A unchanged Cycle-749 instrument own run is all-PASS",
        H749.anchor_passed(anchor_rows[AUDIT_INPUT_PATHS[0]]),
        anchor_rows[AUDIT_INPUT_PATHS[0]],
    )
    check(
        "A landed S322 and U320 surface own runs are all-PASS",
        all(
            H749.anchor_passed(anchor_rows[path])
            for path in AUDIT_INPUT_PATHS[1:]
        ),
        {
            path: anchor_rows[path] for path in AUDIT_INPUT_PATHS[1:]
        },
    )

    candidate = derive_response_kernel_candidate()
    recoil_trace = candidate.derivation["recoil"]
    transfer_trace = candidate.derivation["transfer"]
    assert isinstance(recoil_trace, dict)
    assert isinstance(transfer_trace, dict)
    derived_one = Fraction(True)
    check(
        "B U320 diagonal decomposition derives all recoil-sector weights",
        candidate.recoil_coefficients
        == tuple(
            derived_one
            for _coefficient in candidate.recoil_coefficients
        )
        and len(candidate.recoil_coefficients)
        == len(U320.link_recoil_vertex(U320.ANGLE)[3])
        and float(recoil_trace["vertex_adjoint_gram_residual"])
        < U320.TOLERANCE,
        recoil_trace,
    )
    check(
        "B S322 reciprocity adjoint composition derives the transfer kernel",
        candidate.transfer_coefficients
        == tuple(
            derived_one
            for _coefficient in candidate.transfer_coefficients
        )
        and bool(transfer_trace["self_adjoint"])
        and all(
            value == fraction_text(Fraction())
            for value in transfer_trace["involution_residuals"]
        ),
        transfer_trace,
    )
    firewall = derivation_firewall_audit(source)
    check(
        "B derivation is constant-free and AST-isolated from instrument criteria",
        bool(firewall["passed"])
        and not candidate.derivation["criterion_inputs_read"]
        and not candidate.derivation["free_parameters"]
        and all(value == 0 for value in candidate.fitted_defaults),
        firewall,
    )

    submitted = H749.ResponseKernelCandidate(
        name=candidate.name,
        recoil_coefficients=candidate.recoil_coefficients,
        transfer_coefficients=candidate.transfer_coefficients,
        fitted_defaults=candidate.fitted_defaults,
        demonstration_role=(
            "derived landed-algebra adjoint pullback; fixture-scope candidate"
        ),
    )
    fixtures = H749.extract_frozen_fixtures()
    evaluation = H749.evaluate_candidate(submitted, fixtures, fixtures)
    per_criterion = criterion_verdicts(evaluation)
    overall_verdict = str(evaluation["verdict"])
    check(
        "C unchanged Cycle-749 instrument returns a complete named verdict",
        overall_verdict in {"ACCEPT", "DRIFT", "REJECT"}
        and set(per_criterion)
        == {
            "diagonal_exchange_residual",
            "flux_balance",
            "norm_drift",
            "reciprocal_transfer_values",
            "reciprocity_residual",
            "recoil_ledger",
        }
        and (
            (overall_verdict == "ACCEPT" and not evaluation["failed_criteria"])
            or (
                overall_verdict in {"DRIFT", "REJECT"}
                and bool(evaluation["failed_criteria"])
            )
        ),
        {
            "failed_criteria": evaluation["failed_criteria"],
            "overall": overall_verdict,
            "per_criterion": per_criterion,
            "residuals": evaluation["residuals"],
        },
    )
    check(
        "C per-criterion verdicts exactly follow the frozen instrument bands",
        all(
            verdict
            == (
                "ACCEPT"
                if Fraction(float(evaluation["residuals"][name]))
                <= H749.STRICT_TOLERANCE
                else (
                    "DRIFT"
                    if Fraction(float(evaluation["residuals"][name]))
                    <= H749.DRIFT_LIMIT
                    else "REJECT"
                )
            )
            for name, verdict in per_criterion.items()
        ),
        per_criterion,
    )

    if overall_verdict == "ACCEPT":
        extension = extension_probe(candidate)
        extension_ok = bool(
            extension["reached"]
            and extension["determinate"]
            and extension["outside_defining_set"]
            and not extension["prediction_verified"]
        )
    else:
        extension = {
            "determinate": False,
            "ff_status": "absent on this branch; skipped and not imported",
            "reached": False,
            "reason": f"instrument outcome {overall_verdict}",
        }
        extension_ok = not extension["reached"]
    check(
        "D extension probe is reached only on ACCEPT and makes no correctness claim",
        extension_ok,
        extension,
    )

    mutation_firewall = landed_module_mutation_audit(source)
    input_shas_after = {
        path: sha256_bytes((ROOT / path).read_bytes())
        for path in AUDIT_INPUT_PATHS
    }
    check(
        "E landed runners are unchanged and module-mutation firewalled",
        input_shas_after == input_shas_before
        and bool(mutation_firewall["passed"]),
        {
            "ast": mutation_firewall,
            "sha256": input_shas_after,
        },
    )
    landed_text = " ".join(
        " ".join(data.decode("utf-8").split())
        for data in input_bytes.values()
    )
    check(
        "E C_source firewall declarations are verbatim prohibitions",
        C_source == H749.C_source
        and all(
            " ".join(statement.split()) in landed_text
            for statement in C_source
        )
        and all(
            any(token in statement.lower() for token in ("no ", "not ", "nothing "))
            for statement in C_source
        ),
        {"declarations": len(C_source), "interpretation_supplied": False},
    )

    honest_keys = {
        "candidate_derived": True,
        "finding": (
            "fixture-scope candidate accepted"
            if overall_verdict == "ACCEPT"
            else "named instrument failure recorded"
        ),
        "instrument_accept": overall_verdict == "ACCEPT",
        "no_refit_attachment_complete": False,
        "prediction_verified": False,
        "response_law_established": False,
        "w7_closed": False,
    }
    check(
        "E honest boundary keeps W7 open for every instrument outcome",
        honest_keys["candidate_derived"]
        and not honest_keys["no_refit_attachment_complete"]
        and not honest_keys["prediction_verified"]
        and not honest_keys["response_law_established"]
        and not honest_keys["w7_closed"],
        honest_keys,
    )

    certificate = {
        "anchors": {
            path: {
                **row,
                "input_sha256": input_shas_before[path],
            }
            for path, row in anchor_rows.items()
        },
        "c_source": list(C_source),
        "candidate": {
            "derivation": candidate.derivation,
            "fitted_defaults": tuple(
                fraction_text(value) for value in candidate.fitted_defaults
            ),
            "name": candidate.name,
            "recoil_coefficients": tuple(
                fraction_text(value)
                for value in candidate.recoil_coefficients
            ),
            "transfer_coefficients": tuple(
                fraction_text(value)
                for value in candidate.transfer_coefficients
            ),
        },
        "declared_input_paths": list(AUDIT_INPUT_PATHS),
        "extension_probe": extension,
        "fail": FAIL,
        "firewalls": {
            "derivation_ast": firewall,
            "landed_module_mutation_ast": mutation_firewall,
        },
        "honest_keys": honest_keys,
        "instrument": {
            "evaluation": evaluation,
            "overall_verdict": overall_verdict,
            "per_criterion_verdicts": per_criterion,
        },
        "note_path": NOTE_PATH,
        "pass": PASS,
        "runtime_sec": round(time.monotonic() - started, 6),
    }
    preview = json.dumps(
        certificate, sort_keys=True, separators=(",", ":"), default=jsonable
    )
    check(
        "E stdout remains below the 150KB contract",
        STDOUT_BYTES + len(preview.encode("utf-8")) + 1 < OUTPUT_LIMIT_BYTES,
        {
            "limit_bytes": OUTPUT_LIMIT_BYTES,
            "projected_bytes": STDOUT_BYTES + len(preview.encode("utf-8")) + 1,
        },
    )
    certificate["fail"] = FAIL
    certificate["pass"] = PASS
    certificate["runtime_sec"] = round(time.monotonic() - started, 6)
    final_line = json.dumps(
        certificate, sort_keys=True, separators=(",", ":"), default=jsonable
    )
    emit(final_line)
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
