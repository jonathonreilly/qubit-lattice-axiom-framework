#!/usr/bin/env python3
"""Independent exact-matrix check of the supplied POVM comparator theorem.

This checker imports neither the primary runner nor the Cycle-317 module. It
uses exact rational complex matrices, then executes the primary as a clean
black-box subprocess.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = (
    "docs/POVM_OBSERVATION_COMPARATOR_EXACT_ARITHMETIC_"
    "BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_povm_observation_comparator_independent_check_2026_07_30.py",
    "scripts/frontier_povm_observation_comparator_exact_arithmetic_2026_07_30.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "docs/POVM_OBSERVATION_COMPARATOR_INPUT_CONVENTION_META_NOTE_2026-07-30.md",
    "docs/POVM_OBSERVATION_COMPARATOR_EXACT_ARITHMETIC_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = AUDIT_INPUT_PATHS[1]
TARGET_PATH = AUDIT_INPUT_PATHS[2]
EXPECTED_PRIMARY_SHA256 = (
    "1c6f766e4a1df3a63c6f0d7085e8c45d9a4454bad227650898ddc88197955865"
)
EXPECTED_TARGET_SHA256 = (
    "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10"
)
BLOCH = (Fraction(21, 100), Fraction(-32, 100), Fraction(41, 100))
MATCHING_COUNTS = (121, 79, 68, 132, 141, 59)
COUNTERFACTUAL_COUNTS = (120, 80, 68, 132, 141, 59)
EXPOSURE = 600
PASS = 0
FAIL = 0

QComplex = tuple[Fraction, Fraction]
Matrix = tuple[tuple[QComplex, QComplex], tuple[QComplex, QComplex]]
ZERO: QComplex = (Fraction(), Fraction())
ONE: QComplex = (Fraction(1), Fraction())
I_UNIT: QComplex = (Fraction(), Fraction(1))


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def declared_hashes() -> dict[str, str]:
    return {relative: digest(ROOT / relative) for relative in AUDIT_INPUT_PATHS}


def q_add(left: QComplex, right: QComplex) -> QComplex:
    return left[0] + right[0], left[1] + right[1]


def q_mul(left: QComplex, right: QComplex) -> QComplex:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def q_scale(value: QComplex, scale: Fraction) -> QComplex:
    return value[0] * scale, value[1] * scale


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(q_add(left[row][column], right[row][column]) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_scale(matrix: Matrix, scale: Fraction) -> Matrix:
    return tuple(
        tuple(q_scale(matrix[row][column], scale) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    rows = []
    for row in range(2):
        output_row = []
        for column in range(2):
            value = ZERO
            for inner in range(2):
                value = q_add(value, q_mul(left[row][inner], right[inner][column]))
            output_row.append(value)
        rows.append(tuple(output_row))
    return tuple(rows)  # type: ignore[return-value]


def matrix_trace(matrix: Matrix) -> QComplex:
    return q_add(matrix[0][0], matrix[1][1])


IDENTITY: Matrix = ((ONE, ZERO), (ZERO, ONE))
X: Matrix = ((ZERO, ONE), (ONE, ZERO))
Y: Matrix = ((ZERO, q_scale(I_UNIT, -1)), (I_UNIT, ZERO))
Z: Matrix = ((ONE, ZERO), (ZERO, q_scale(ONE, -1)))


def exact_matrix_reconstruction() -> tuple[tuple[Fraction, ...], dict[str, str]]:
    rho = matrix_scale(
        matrix_add(
            matrix_add(
                matrix_add(IDENTITY, matrix_scale(X, BLOCH[0])),
                matrix_scale(Y, BLOCH[1]),
            ),
            matrix_scale(Z, BLOCH[2]),
        ),
        Fraction(1, 2),
    )
    effects = []
    for pauli in (X, Y, Z):
        effects.append(matrix_scale(matrix_add(IDENTITY, pauli), Fraction(1, 6)))
        effects.append(
            matrix_scale(
                matrix_add(IDENTITY, matrix_scale(pauli, Fraction(-1))),
                Fraction(1, 6),
            )
        )
    effect_sum = effects[0]
    for effect in effects[1:]:
        effect_sum = matrix_add(effect_sum, effect)
    traces = tuple(matrix_trace(matrix_multiply(rho, effect)) for effect in effects)
    weights = tuple(value[0] for value in traces)
    determinant = q_add(
        q_mul(rho[0][0], rho[1][1]),
        q_scale(q_mul(rho[0][1], rho[1][0]), Fraction(-1)),
    )
    conditions = {
        "rho_trace": str(matrix_trace(rho)[0]),
        "rho_determinant": str(determinant[0]),
        "povm_sum_is_identity": str(effect_sum == IDENTITY),
        "imaginary_trace_terms_zero": str(all(value[1] == 0 for value in traces)),
    }
    return weights, conditions


def clean_environment() -> dict[str, str]:
    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    environment.pop("PYTHONHOME", None)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return environment


def run_primary(root: Path) -> tuple[int | str, str]:
    try:
        completed = subprocess.run(
            [sys.executable, str(root / PRIMARY_PATH)],
            cwd=root,
            env=clean_environment(),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=AUDIT_TIMEOUT_SEC,
            check=False,
        )
        return completed.returncode, completed.stdout
    except subprocess.TimeoutExpired as exc:
        raw = exc.stdout or ""
        output = raw.decode("utf-8", errors="replace") if isinstance(raw, bytes) else raw
        return "timeout", output


def parse_primary(output: str) -> tuple[tuple[int, int] | None, dict | None]:
    matches = re.findall(
        r"^SUMMARY PASS\s+(\d+)\s+FAIL\s+(\d+)\s+RUNTIME_SEC\s+[0-9.]+$",
        output,
        re.MULTILINE,
    )
    summary = tuple(map(int, matches[-1])) if matches else None
    payload = None
    for line in output.splitlines():
        if line.startswith("RESULT_JSON "):
            try:
                payload = json.loads(line.removeprefix("RESULT_JSON "))
            except json.JSONDecodeError:
                payload = None
    return summary, payload


def production_source_pin_mutation_control() -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="povm-comparator-pin-") as temp_name:
        temp_root = Path(temp_name)
        for relative in AUDIT_INPUT_PATHS[1:]:
            destination = temp_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, destination)
        target = temp_root / TARGET_PATH
        text = target.read_text(encoding="utf-8")
        target.write_text(text.replace("Cycle 317:", "Cycle 317 :", 1), encoding="utf-8")
        returncode, output = run_primary(temp_root)
        summary, payload = parse_primary(output)
        return {
            "returncode": returncode,
            "summary": summary,
            "payload_present": payload is not None,
            "source_pin_failure_seen": "source provenance:" in output
            and "FAIL" in output,
        }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()
    hashes_before = declared_hashes()
    primary_sha = digest(ROOT / PRIMARY_PATH)
    target_sha = digest(ROOT / TARGET_PATH)
    check(
        "source pins: the primary and Cycle-317 provenance source match independent hard pins",
        primary_sha == EXPECTED_PRIMARY_SHA256
        and target_sha == EXPECTED_TARGET_SHA256
        and digest(ROOT / __file__) == hashes_before[AUDIT_INPUT_PATHS[0]],
        {"primary": primary_sha, "target": target_sha},
    )

    weights, matrix_detail = exact_matrix_reconstruction()
    expected = tuple(Fraction(value, EXPOSURE) for value in MATCHING_COUNTS)
    check(
        "independent exact matrices: positive density/POVM invariants and all six trace weights are reconstructed",
        weights == expected
        and matrix_detail["rho_trace"] == "1"
        and Fraction(matrix_detail["rho_determinant"]) > 0
        and matrix_detail["povm_sum_is_identity"] == "True"
        and matrix_detail["imaginary_trace_terms_zero"] == "True",
        {"weights": tuple(str(value) for value in weights), **matrix_detail},
    )

    matching = tuple(Fraction(value, EXPOSURE) for value in MATCHING_COUNTS)
    counterfactual = tuple(
        Fraction(value, EXPOSURE) for value in COUNTERFACTUAL_COUNTS
    )
    matching_verdicts = tuple(left == right for left, right in zip(matching, weights))
    counterfactual_verdicts = tuple(
        left == right for left, right in zip(counterfactual, weights)
    )
    census = Counter(matching_verdicts + counterfactual_verdicts)
    check(
        "independent count route: both exact simplexes and the ten-agreement/two-disagreement census follow directly",
        sum(matching, start=Fraction()) == 1
        and sum(counterfactual, start=Fraction()) == 1
        and census == {True: 10, False: 2},
        {
            "matching": tuple(str(value) for value in matching),
            "counterfactual": tuple(str(value) for value in counterfactual),
            "census": {"agreement": census[True], "disagreement": census[False]},
        },
    )

    returncode, output = run_primary(ROOT)
    summary, payload = parse_primary(output)
    expected_strings = [str(value) for value in weights]
    check(
        "black-box primary: clean subprocess agrees with the independent matrices and count census",
        returncode == 0
        and summary is not None
        and summary[1] == 0
        and payload is not None
        and payload.get("candidate_weights") == expected_strings
        and payload.get("matching_simplex") == expected_strings
        and payload.get("counterfactual_simplex")
        == [str(value) for value in counterfactual]
        and payload.get("comparator_census")
        == {"agreement": 10, "disagreement": 2}
        and payload.get("framework_record_identification") is False
        and payload.get("physical_weight_law_selected") is False,
        {"returncode": returncode, "summary": summary, "payload": payload},
    )

    mutation = production_source_pin_mutation_control()
    check(
        "tamper control: a one-byte provenance-source mutation makes the production primary fail closed",
        mutation["returncode"] != 0
        and mutation["summary"] is not None
        and mutation["summary"][1] > 0
        and mutation["source_pin_failure_seen"] is True,
        mutation,
    )
    check(
        "pin predicates: independent hard pins reject source and primary byte mutations",
        sha256((ROOT / TARGET_PATH).read_bytes() + b"x").hexdigest()
        != EXPECTED_TARGET_SHA256
        and sha256((ROOT / PRIMARY_PATH).read_bytes() + b"x").hexdigest()
        != EXPECTED_PRIMARY_SHA256,
        {"mutation": "one-byte suffix"},
    )

    hashes_after = declared_hashes()
    check(
        "declared-input discipline: the complete narrow source/note closure stayed byte-stable",
        hashes_before == hashes_after
        and set(hashes_after) == set(AUDIT_INPUT_PATHS),
        hashes_after,
    )

    runtime = perf_counter() - started
    result = {
        "all_checks_pass": FAIL == 0,
        "candidate_weights": [str(value) for value in weights],
        "check_totals": {"fail": FAIL, "pass": PASS},
        "comparator_census": {"agreement": census[True], "disagreement": census[False]},
        "primary_sha256": primary_sha,
        "runtime_seconds": round(runtime, 6),
        "target_sha256": target_sha,
    }
    print("SUMMARY PASS", PASS, "FAIL", FAIL, "RUNTIME_SEC", f"{runtime:.6f}")
    print("RESULT_JSON", json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
