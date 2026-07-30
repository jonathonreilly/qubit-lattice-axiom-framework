#!/usr/bin/env python3
"""Exact conditional arithmetic for a supplied six-effect POVM comparator.

The Cycle-317 source is pinned and parsed as text for provenance only. It is
not imported. All mathematics below is exact ``Fraction`` arithmetic under
the supplied finite convention.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = (
    "docs/POVM_OBSERVATION_COMPARATOR_EXACT_ARITHMETIC_"
    "BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_povm_observation_comparator_exact_arithmetic_2026_07_30.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "docs/POVM_OBSERVATION_COMPARATOR_INPUT_CONVENTION_META_NOTE_2026-07-30.md",
    "docs/POVM_OBSERVATION_COMPARATOR_EXACT_ARITHMETIC_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from dataclasses import dataclass, replace
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
TARGET_PATH = AUDIT_INPUT_PATHS[1]
EXPECTED_TARGET_SHA256 = (
    "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10"
)
EXPECTED_BLOCH = (Fraction(21, 100), Fraction(-32, 100), Fraction(41, 100))
OUTCOME_IDS = ("x+", "x-", "y+", "y-", "z+", "z-")
MATCHING_COUNTS = (121, 79, 68, 132, 141, 59)
COUNTERFACTUAL_COUNTS = (120, 80, 68, 132, 141, 59)
EXPOSURE = 600
MENU_ID = "supplied-six-axis-povm"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ObservationRow:
    observation_id: str
    menu_id: str
    exposure_id: str
    outcome_id: str


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


def _direct_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one top-level function {name}")
    return matches[0]


def _direct_assignment(function: ast.FunctionDef, name: str) -> ast.Assign:
    matches = [
        node
        for node in function.body
        if isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one direct assignment to {name}")
    return matches[0]


def source_fixture() -> tuple[Fraction, Fraction, Fraction]:
    path = ROOT / TARGET_PATH
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=TARGET_PATH)
    outer = _direct_function(tree, "mixed_projective_forcing_basis_controls")
    bloch_assignment = _direct_assignment(outer, "bloch")
    sigma_assignment = _direct_assignment(outer, "sigma")
    born_matches = [
        node
        for node in outer.body
        if isinstance(node, ast.FunctionDef) and node.name == "born_weight"
    ]
    if len(born_matches) != 1:
        raise ValueError("expected one nested born_weight")
    born = born_matches[0]
    returns = [
        node
        for node in born.body
        if isinstance(node, ast.Return) and node.value is not None
    ]
    if len(returns) != 1:
        raise ValueError("expected one direct born_weight return")

    if not (
        isinstance(bloch_assignment.value, ast.Call)
        and bloch_assignment.value.args
    ):
        raise ValueError("Bloch assignment changed shape")
    raw_bloch = ast.literal_eval(bloch_assignment.value.args[0])
    bloch = tuple(Fraction(str(value)) for value in raw_bloch)
    sigma_shape = ast.dump(
        ast.parse(
            "(I2 + bloch[0] * X + bloch[1] * Y + bloch[2] * Z) / 2",
            mode="eval",
        ).body,
        include_attributes=False,
    )
    return_shape = ast.dump(
        ast.parse("float(np.trace(sigma @ effect).real)", mode="eval").body,
        include_attributes=False,
    )
    condition = (
        digest(path) == EXPECTED_TARGET_SHA256
        and bloch == EXPECTED_BLOCH
        and ast.dump(sigma_assignment.value, include_attributes=False) == sigma_shape
        and ast.dump(returns[0].value, include_attributes=False) == return_shape
        and tuple(argument.arg for argument in born.args.args) == ("effect",)
    )
    check(
        "source provenance: exact Cycle-317 pin carries the supplied Bloch and trace fixture",
        condition,
        {
            "path": TARGET_PATH,
            "sha256": digest(path),
            "bloch": tuple(str(value) for value in bloch),
            "runtime_imported": False,
        },
    )
    return bloch


def candidate_weights(
    bloch: tuple[Fraction, Fraction, Fraction],
) -> tuple[Fraction, ...]:
    weights = []
    for coordinate in bloch:
        weights.extend(((1 + coordinate) / 6, (1 - coordinate) / 6))
    return tuple(weights)


def make_rows(
    label: str, counts: tuple[int, ...]
) -> tuple[ObservationRow, ...]:
    exposure_id = f"{label}-exposure"
    rows = []
    serial = 0
    for outcome_id, count in zip(OUTCOME_IDS, counts, strict=True):
        for _ in range(count):
            rows.append(
                ObservationRow(
                    observation_id=f"{label}-{serial:03d}",
                    menu_id=MENU_ID,
                    exposure_id=exposure_id,
                    outcome_id=outcome_id,
                )
            )
            serial += 1
    return tuple(rows)


def normalize_rows(
    rows: tuple[ObservationRow, ...],
    exposure_id: str,
    exposure: int,
) -> tuple[Fraction, ...]:
    if type(rows) is not tuple or not rows:
        raise ValueError("rows must be one nonempty tuple")
    if type(exposure) is not int or exposure <= 0:
        raise ValueError("exposure must be one positive integer")
    if len(rows) != exposure:
        raise ValueError("complete exclusive protocol requires one row per trial")
    if any(type(row) is not ObservationRow for row in rows):
        raise ValueError("every row must use ObservationRow")
    identifiers = [row.observation_id for row in rows]
    if any(not identifier for identifier in identifiers):
        raise ValueError("observation identifiers must be nonempty")
    if len(set(identifiers)) != len(identifiers):
        raise ValueError("observation identifiers must be unique")
    if any(row.menu_id != MENU_ID for row in rows):
        raise ValueError("row menu does not match the supplied menu")
    if any(row.exposure_id != exposure_id for row in rows):
        raise ValueError("row exposure does not match the supplied exposure")
    if any(row.outcome_id not in OUTCOME_IDS for row in rows):
        raise ValueError("row outcome is outside the supplied ordered menu")
    counts = Counter(row.outcome_id for row in rows)
    return tuple(Fraction(counts[outcome_id], exposure) for outcome_id in OUTCOME_IDS)


def comparator(
    observed: tuple[Fraction, ...],
    candidate: tuple[Fraction, ...],
) -> tuple[str, ...]:
    if len(observed) != len(candidate):
        raise ValueError("comparator vectors have different lengths")
    return tuple(
        "agreement" if left == right else "disagreement"
        for left, right in zip(observed, candidate, strict=True)
    )


def malformed_controls(base_rows: tuple[ObservationRow, ...]) -> tuple[str, ...]:
    exposure_id = base_rows[0].exposure_id
    probes = (
        (
            "duplicate-id",
            base_rows[:1]
            + (replace(base_rows[1], observation_id=base_rows[0].observation_id),)
            + base_rows[2:],
            exposure_id,
            EXPOSURE,
        ),
        (
            "wrong-menu",
            (replace(base_rows[0], menu_id="other-menu"),) + base_rows[1:],
            exposure_id,
            EXPOSURE,
        ),
        (
            "wrong-exposure-id",
            base_rows,
            "other-exposure",
            EXPOSURE,
        ),
        (
            "wrong-total",
            base_rows,
            exposure_id,
            EXPOSURE + 1,
        ),
        (
            "unknown-outcome",
            (replace(base_rows[0], outcome_id="q+"),) + base_rows[1:],
            exposure_id,
            EXPOSURE,
        ),
    )
    refused = []
    for label, rows, declared_exposure_id, declared_exposure in probes:
        try:
            normalize_rows(rows, declared_exposure_id, declared_exposure)
        except ValueError:
            refused.append(label)
    return tuple(refused)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()
    hashes_before = declared_hashes()
    bloch = source_fixture()
    norm_squared = sum((value * value for value in bloch), start=Fraction())
    weights = candidate_weights(bloch)
    expected_weights = tuple(Fraction(count, EXPOSURE) for count in MATCHING_COUNTS)

    check(
        "exact state and POVM domain: the supplied density fixture and six effects are positive and normalized",
        norm_squared < 1
        and len(weights) == len(OUTCOME_IDS)
        and min(weights) > 0
        and sum(weights, start=Fraction()) == 1,
        {
            "bloch_norm_squared": str(norm_squared),
            "effect_eigenvalues": ("0", "1/3"),
            "effect_sum": "I",
        },
    )
    check(
        "closed-form Pauli trace: six exact candidate values match the supplied rational profile",
        weights == expected_weights
        and tuple(int(value * EXPOSURE) for value in weights) == MATCHING_COUNTS
        and all(value * EXPOSURE == int(value * EXPOSURE) for value in weights),
        tuple(str(value) for value in weights),
    )

    matching_rows = make_rows("matching", MATCHING_COUNTS)
    counterfactual_rows = make_rows("counterfactual", COUNTERFACTUAL_COUNTS)
    matching = normalize_rows(matching_rows, "matching-exposure", EXPOSURE)
    counterfactual = normalize_rows(
        counterfactual_rows, "counterfactual-exposure", EXPOSURE
    )
    check(
        "conditional count theorem: both declared exhaustive row sets normalize exactly into the rational simplex",
        matching == expected_weights
        and sum(matching, start=Fraction()) == 1
        and sum(counterfactual, start=Fraction()) == 1
        and min(counterfactual) >= 0,
        {
            "matching": tuple(str(value) for value in matching),
            "counterfactual": tuple(str(value) for value in counterfactual),
        },
    )

    matching_verdicts = comparator(matching, weights)
    counterfactual_verdicts = comparator(counterfactual, weights)
    census = Counter(matching_verdicts + counterfactual_verdicts)
    check(
        "exact comparator: matching profile gives six agreements and the one-row shift gives four agreements and two disagreements",
        Counter(matching_verdicts) == {"agreement": 6}
        and Counter(counterfactual_verdicts)
        == {"agreement": 4, "disagreement": 2}
        and census == {"agreement": 10, "disagreement": 2},
        dict(sorted(census.items())),
    )

    refused = malformed_controls(matching_rows)
    check(
        "lawful-domain controls: five malformed synthetic row sets are refused",
        len(refused) == 5 and len(set(refused)) == len(refused),
        refused,
    )

    hashes_after = declared_hashes()
    check(
        "declared-input discipline: every mutable source and note stayed byte-stable",
        hashes_before == hashes_after
        and set(hashes_after) == set(AUDIT_INPUT_PATHS),
        hashes_after,
    )

    runtime = perf_counter() - started
    payload = {
        "all_checks_pass": FAIL == 0,
        "audit_input_sha256": hashes_after,
        "candidate_weights": [str(value) for value in weights],
        "check_totals": {"fail": FAIL, "pass": PASS},
        "comparator_census": dict(sorted(census.items())),
        "counterfactual_simplex": [str(value) for value in counterfactual],
        "framework_record_identification": False,
        "matching_simplex": [str(value) for value in matching],
        "occurrence_law_selected": False,
        "physical_weight_law_selected": False,
        "runtime_seconds": round(runtime, 6),
        "source_pin": {TARGET_PATH: EXPECTED_TARGET_SHA256},
        "supplied_protocol_only": True,
    }
    print("SUMMARY PASS", PASS, "FAIL", FAIL, "RUNTIME_SEC", f"{runtime:.6f}")
    print("RESULT_JSON", json.dumps(payload, sort_keys=True, separators=(",", ":")))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
