#!/usr/bin/env python3
"""Clean-room checker for the truncated equal-split support certificate.

The primary is parsed as literal data and never imported.  This checker builds
the six-mode CAR representation from Jordan-Wigner tensor products, then uses
dense matrix exponentiation rather than the primary's analytic star formula.
"""

from __future__ import annotations

import ast
import itertools
import math
from pathlib import Path
import sys
import time
from typing import Any

import numpy as np
from scipy.linalg import expm


AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = "docs/TRUNCATED_FOCK_EQUAL_SPLIT_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_truncated_fock_equal_split_support_2026_07_28.py",
)
CHECKER_KIND = "clean-room-jordan-wigner"
PRIMARY_MODULE = "frontier_truncated_fock_equal_split_support_2026_07_28"
MODE_COUNT = 6
Q_DIMENSION = 7
TOLERANCE = 3e-10

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = ROOT / AUDIT_INPUT_PATHS[0]

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


def literal_assignments(tree: ast.Module) -> dict[str, Any]:
    values: dict[str, Any] = {}
    for node in tree.body:
        name: str | None = None
        expression: ast.expr | None = None
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            if isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                expression = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            name = node.target.id
            expression = node.value
        if name is None or expression is None:
            continue
        try:
            values[name] = ast.literal_eval(expression)
        except (ValueError, TypeError):
            pass
    return values


def extract_primary_contract() -> tuple[bool, dict[str, object], dict[str, Any]]:
    source = PRIMARY_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(PRIMARY_PATH))
    values = literal_assignments(tree)
    required = (
        "NOTE_PATH",
        "AUDIT_INPUT_PATHS",
        "MODE_COUNT",
        "Q_DIMENSION",
        "N_MAX",
        "DIRECTIONS",
        "OPPOSITE",
        "BETA",
        "MEDIATOR_COUPLING",
        "MASS_FACTOR",
        "EQUAL_COMPONENT_WEIGHTS",
        "TOLERANCE",
        "SUPPLIED_SCOPE",
    )
    missing = tuple(name for name in required if name not in values)
    imported_modules = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    forbidden_historical = {
        name
        for name in imported_modules
        if name.startswith(
            (
                "unit_weight_carried_link_recoil",
                "two_cell_two_source_recoil_reciprocity",
                "physical_cycle",
            )
        )
    }
    ok = (
        not missing
        and values.get("NOTE_PATH") == NOTE_PATH
        and values.get("MODE_COUNT") == MODE_COUNT
        and values.get("Q_DIMENSION") == Q_DIMENSION
        and values.get("N_MAX") == 2
        and values.get("DIRECTIONS")
        == (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        )
        and values.get("OPPOSITE") == (1, 0, 3, 2, 5, 4)
        and values.get("EQUAL_COMPONENT_WEIGHTS") == (1.0, 1.0)
        and values.get("TOLERANCE") == TOLERANCE
        and not forbidden_historical
        and (
            "frontier_truncated_fock_equal_split_independent_check_2026_07_28"
            in imported_modules
        )
    )
    detail = {
        "missing": missing,
        "forbidden_historical_imports": sorted(forbidden_historical),
        "primary_imported": PRIMARY_MODULE in sys.modules,
        "registered_checker_import": (
            "frontier_truncated_fock_equal_split_independent_check_2026_07_28"
            in imported_modules
        ),
    }
    return ok and PRIMARY_MODULE not in sys.modules, detail, values


def tensor_product(factors: list[np.ndarray]) -> np.ndarray:
    result = np.array(((1.0 + 0.0j,),))
    for factor in factors:
        result = np.kron(result, factor)
    return result


def clean_room_operators(
    values: dict[str, Any],
) -> tuple[
    tuple[np.ndarray, ...],
    np.ndarray,
    np.ndarray,
    tuple[np.ndarray, ...],
    np.ndarray,
]:
    identity_two = np.eye(2, dtype=complex)
    parity_two = np.diag((1.0, -1.0)).astype(complex)
    lowering_two = np.array(
        ((0.0, 1.0), (0.0, 0.0)), dtype=complex
    )

    annihilators = []
    for mode in range(MODE_COUNT):
        factors = []
        for displayed_mode in reversed(range(MODE_COUNT)):
            if displayed_mode < mode:
                factors.append(parity_two)
            elif displayed_mode == mode:
                factors.append(lowering_two)
            else:
                factors.append(identity_two)
        annihilators.append(tensor_product(factors))
    annihilator_tuple = tuple(annihilators)
    creators = tuple(operator.conj().T for operator in annihilator_tuple)
    number_operators = tuple(
        creators[mode] @ annihilator_tuple[mode]
        for mode in range(MODE_COUNT)
    )
    local_number = sum(
        number_operators,
        start=np.zeros((1 << MODE_COUNT, 1 << MODE_COUNT), dtype=complex),
    )

    directions = np.asarray(values["DIRECTIONS"], dtype=float)
    opposite = tuple(values["OPPOSITE"])
    generator = np.zeros(
        (
            (1 << MODE_COUNT) * Q_DIMENSION,
            (1 << MODE_COUNT) * Q_DIMENSION,
        ),
        dtype=complex,
    )
    for direction in range(MODE_COUNT):
        q_raise = np.zeros((Q_DIMENSION, Q_DIMENSION), dtype=complex)
        q_raise[1 + direction, 0] = 1.0
        hop = creators[opposite[direction]] @ annihilator_tuple[direction]
        directed = np.kron(hop, q_raise)
        generator += directed + directed.conj().T

    number = np.kron(local_number, np.eye(Q_DIMENSION, dtype=complex))
    matter_momenta = tuple(
        np.kron(
            sum(
                (
                    directions[direction, axis]
                    * number_operators[direction]
                    for direction in range(MODE_COUNT)
                ),
                start=np.zeros(
                    (1 << MODE_COUNT, 1 << MODE_COUNT), dtype=complex
                ),
            ),
            np.eye(Q_DIMENSION, dtype=complex),
        )
        for axis in range(3)
    )
    return annihilator_tuple, generator, number, matter_momenta, directions


def car_residual(annihilators: tuple[np.ndarray, ...]) -> float:
    creators = tuple(operator.conj().T for operator in annihilators)
    zero = np.zeros_like(annihilators[0])
    identity = np.eye(len(zero), dtype=complex)
    largest = 0.0
    for left, right in itertools.product(range(MODE_COUNT), repeat=2):
        aa = (
            annihilators[left] @ annihilators[right]
            + annihilators[right] @ annihilators[left]
        )
        aad = (
            annihilators[left] @ creators[right]
            + creators[right] @ annihilators[left]
        )
        largest = max(
            largest,
            float(np.linalg.norm(aa)),
            float(
                np.linalg.norm(
                    aad - (identity if left == right else zero)
                )
            ),
        )
    return largest


def layer_indices(number: int) -> np.ndarray:
    return np.asarray(
        [
            Q_DIMENSION * mask + q
            for mask in range(1 << MODE_COUNT)
            if mask.bit_count() == number
            for q in range(Q_DIMENSION)
        ],
        dtype=int,
    )


def q_momentum(
    directions: np.ndarray, scale: float, axis: int
) -> np.ndarray:
    values = np.zeros(Q_DIMENSION)
    values[1:] = scale * directions[:, axis]
    return np.kron(
        np.eye(1 << MODE_COUNT, dtype=complex), np.diag(values)
    )


def commutator_norm(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.linalg.norm(left @ right - right @ left))


def main() -> int:
    started = time.monotonic()
    print("TRUNCATED-FOCK CLEAN-ROOM INDEPENDENT CHECK")
    print("primary_mode = literal AST data only; import blocklisted")

    extracted, extraction_detail, values = extract_primary_contract()
    check("the primary contract is explicit and data-only", extracted, extraction_detail)
    if not extracted:
        print("SUMMARY", {"pass": PASS, "fail": FAIL})
        print("FINAL", "HONEST_FAIL")
        return 1

    annihilators, generator, number, matter_momenta, directions = (
        clean_room_operators(values)
    )
    car = car_residual(annihilators)
    check(
        "the clean-room Jordan-Wigner operators satisfy CAR and preserve number",
        (
            car < TOLERANCE
            and float(np.linalg.norm(generator - generator.conj().T)) == 0.0
            and commutator_norm(generator, number) == 0.0
        ),
        {
            "car_residual": car,
            "generator_number_commutator": commutator_norm(generator, number),
        },
    )

    beta = float(values["BETA"])
    coupling = float(values["MEDIATOR_COUPLING"])
    mass_factor = float(values["MASS_FACTOR"])
    angle = coupling * mass_factor * math.tan(-beta / 2.0)
    vertex = expm(1j * angle * generator)

    channels_by_layer = []
    sign_counts = []
    for number_value in range(MODE_COUNT + 1):
        channels = 0
        signs = {-1: 0, 1: 0}
        for mask in range(1 << MODE_COUNT):
            if mask.bit_count() != number_value:
                continue
            column = Q_DIMENSION * mask
            for row in np.flatnonzero(abs(generator[:, column]) > 0.5):
                channels += 1
                signs[int(round(generator[row, column].real))] += 1
        channels_by_layer.append(channels)
        sign_counts.append(signs)
    expected_channels = tuple(
        0 if number_value == 0
        else 6 * math.comb(4, number_value - 1)
        for number_value in range(MODE_COUNT + 1)
    )
    check(
        "independent combinatorics gives the full layer sequence and truncated prefix",
        (
            tuple(channels_by_layer) == expected_channels
            and tuple(channels_by_layer[:3]) == (0, 6, 24)
            and all(row[-1] == 0 for row in sign_counts)
        ),
        {
            "mask_counts": tuple(
                math.comb(MODE_COUNT, n) for n in range(MODE_COUNT + 1)
            ),
            "channel_counts": tuple(channels_by_layer),
            "sign_counts": sign_counts,
        },
    )

    split_residuals = {}
    for alpha in (0.0, 0.25, 1.0, 1.7, 2.0):
        residual = 0.0
        for axis in range(3):
            total = (
                matter_momenta[axis]
                + q_momentum(directions, alpha, axis)
                + q_momentum(directions, 2.0 - alpha, axis)
            )
            residual = max(residual, commutator_norm(generator, total))
        split_residuals[str(alpha)] = residual
    check(
        "the equal split is not selected by conservation",
        max(split_residuals.values()) < TOLERANCE,
        {
            "commutators_by_alpha": split_residuals,
            "conclusion": "only the sum is conserved",
        },
    )

    all_indices = np.arange(len(vertex))
    layer_rows = []
    for number_value in range(3):
        indices = layer_indices(number_value)
        outside = np.setdiff1d(all_indices, indices)
        block = vertex[np.ix_(indices, indices)]
        weights = []
        for mask in range(1 << MODE_COUNT):
            if mask.bit_count() != number_value:
                continue
            column = Q_DIMENSION * mask
            for row in np.flatnonzero(abs(generator[:, column]) > 0.5):
                weights.append(float(abs(vertex[row, column]) ** 2))
        layer_rows.append(
            {
                "number": number_value,
                "active_channels": len(weights),
                "weight_min": min(weights, default=0.0),
                "weight_max": max(weights, default=0.0),
                "off_layer": float(
                    np.max(abs(vertex[np.ix_(outside, indices)]), initial=0.0)
                ),
                "transpose_residual": float(np.linalg.norm(block.T - block)),
            }
        )
    analytic_weight = math.sin(angle) ** 2
    check(
        "dense exponentiation reproduces the truncated layers and layer-1 anchor",
        (
            tuple(row["active_channels"] for row in layer_rows)
            == (0, 6, 24)
            and max(float(row["off_layer"]) for row in layer_rows) == 0.0
            and abs(float(layer_rows[1]["weight_min"]) - analytic_weight)
            < TOLERANCE
            and abs(float(layer_rows[1]["weight_max"]) - analytic_weight)
            < TOLERANCE
        ),
        {"angle": angle, "analytic_weight": analytic_weight, "layers": layer_rows},
    )

    truncated_masks = [
        mask
        for mask in range(1 << MODE_COUNT)
        if mask.bit_count() <= 2
    ]
    columns = 2 * Q_DIMENSION * len(truncated_masks) ** 2
    complete_columns = 2 * Q_DIMENSION * (1 << MODE_COUNT) ** 2
    check(
        "the enumerated domain is the strict 6,776-column truncated slice",
        (
            len(truncated_masks) == 22
            and columns == 6776
            and complete_columns == 57344
            and columns < complete_columns
        ),
        {
            "local_truncated_masks": len(truncated_masks),
            "truncated_columns": columns,
            "complete_columns": complete_columns,
        },
    )

    combined_indices = np.concatenate((layer_indices(1), layer_indices(2)))
    block = vertex[np.ix_(combined_indices, combined_indices)]
    rng = np.random.default_rng(5708)
    real_left = rng.normal(size=len(combined_indices))
    real_right = rng.normal(size=len(combined_indices))
    complex_left = real_left + 1j * rng.normal(size=len(combined_indices))
    complex_right = real_right + 1j * rng.normal(size=len(combined_indices))
    real_left /= np.linalg.norm(real_left)
    real_right /= np.linalg.norm(real_right)
    complex_left /= np.linalg.norm(complex_left)
    complex_right /= np.linalg.norm(complex_right)
    real_residual = float(
        abs(real_left @ block @ real_right - real_right @ block @ real_left)
    )
    generic_complex_residual = float(
        abs(
            np.vdot(complex_left, block @ complex_right)
            - np.vdot(complex_right, block @ complex_left)
        )
    )
    check(
        "reciprocity is correctly limited to transpose and real-bilinear symmetry",
        (
            float(np.linalg.norm(block.T - block)) < TOLERANCE
            and real_residual < TOLERANCE
            and generic_complex_residual > 1e-6
        ),
        {
            "transpose_residual": float(np.linalg.norm(block.T - block)),
            "real_bilinear_residual": real_residual,
            "generic_complex_bra_ket_residual": generic_complex_residual,
        },
    )

    runtime = time.monotonic() - started
    print(
        "SUMMARY",
        {"pass": PASS, "fail": FAIL, "runtime_seconds": round(runtime, 6)},
    )
    print("FINAL", "ALL_PASS" if FAIL == 0 else "HONEST_FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
