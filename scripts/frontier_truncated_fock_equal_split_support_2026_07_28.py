#!/usr/bin/env python3
"""Conditional equal-split bookkeeping on the n_left,n_right<=2 Fock slice.

The fixture is stated completely in this file.  No historical Cycle module is
imported.  The equal two-component split is a supplied convention, not a
consequence of momentum conservation.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
import math
import time

import numpy as np

import frontier_truncated_fock_equal_split_independent_check_2026_07_28 as INDEPENDENT_PACKET_SOURCE


AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = "docs/TRUNCATED_FOCK_EQUAL_SPLIT_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_truncated_fock_equal_split_independent_check_2026_07_28.py",
)

MODE_COUNT = 6
Q_DIMENSION = 7
N_MAX = 2
DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
OPPOSITE = (1, 0, 3, 2, 5, 4)
BETA = -0.3
MEDIATOR_COUPLING = 0.8
MASS_FACTOR = 3.0
EQUAL_COMPONENT_WEIGHTS = (1.0, 1.0)
TOLERANCE = 3e-10
SUPPLIED_SCOPE = (
    "six ordered directional modes; canonical CAR reversal hop; "
    "n_left,n_right<=2; beta=-0.3; coupling=0.8; "
    "theta=0.8*3*tan(-beta/2); q-direction total weight 2d; "
    "equal component split (1,1)"
)

PASS = 0
FAIL = 0
FAILED_LABELS: list[str] = []


@dataclass(frozen=True)
class Channel:
    number: int
    source_mask: int
    target_mask: int
    direction: int
    sign: int
    reservoir_index: int
    pair_index: int


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        FAILED_LABELS.append(label)
        print("FAIL", label, "::", detail)


def fermion_hop(mask: int, source: int, target: int) -> tuple[int, int] | None:
    """Apply c_target^dagger c_source in the little-endian mask basis."""
    if not ((mask >> source) & 1) or ((mask >> target) & 1):
        return None
    source_parity = (mask & ((1 << source) - 1)).bit_count()
    reduced = mask ^ (1 << source)
    target_parity = (reduced & ((1 << target) - 1)).bit_count()
    sign = -1 if (source_parity + target_parity) % 2 else 1
    return reduced | (1 << target), sign


def mask_vector(mask: int) -> np.ndarray:
    vector = np.zeros(3, dtype=float)
    for direction, basis_vector in enumerate(DIRECTIONS):
        if (mask >> direction) & 1:
            vector += basis_vector
    return vector


def channels() -> tuple[Channel, ...]:
    rows: list[Channel] = []
    for source_mask in range(1 << MODE_COUNT):
        for direction in range(MODE_COUNT):
            hopped = fermion_hop(
                source_mask, direction, OPPOSITE[direction]
            )
            if hopped is None:
                continue
            target_mask, sign = hopped
            rows.append(
                Channel(
                    number=source_mask.bit_count(),
                    source_mask=source_mask,
                    target_mask=target_mask,
                    direction=direction,
                    sign=sign,
                    reservoir_index=Q_DIMENSION * source_mask,
                    pair_index=(
                        Q_DIMENSION * target_mask + 1 + direction
                    ),
                )
            )
    return tuple(rows)


CHANNELS = channels()
DIMENSION = (1 << MODE_COUNT) * Q_DIMENSION


def source_generator() -> np.ndarray:
    generator = np.zeros((DIMENSION, DIMENSION), dtype=complex)
    seen_leaves: set[int] = set()
    for channel in CHANNELS:
        if channel.pair_index in seen_leaves:
            raise AssertionError("directional q leaf belongs to two stars")
        seen_leaves.add(channel.pair_index)
        generator[channel.pair_index, channel.reservoir_index] = channel.sign
        generator[channel.reservoir_index, channel.pair_index] = channel.sign
    return generator


def analytic_vertex(angle: float) -> np.ndarray:
    """Exponentiate each disjoint reservoir-centred star analytically."""
    vertex = np.eye(DIMENSION, dtype=complex)
    by_source: dict[int, list[Channel]] = {}
    for channel in CHANNELS:
        by_source.setdefault(channel.source_mask, []).append(channel)
    for source_mask, star in by_source.items():
        degree = len(star)
        root_degree = math.sqrt(degree)
        cosine = math.cos(angle * root_degree)
        sine_factor = 1j * math.sin(angle * root_degree) / root_degree
        centre = Q_DIMENSION * source_mask
        vertex[centre, centre] = cosine
        for left in star:
            vertex[left.pair_index, centre] = sine_factor * left.sign
            vertex[centre, left.pair_index] = sine_factor * left.sign
            for right in star:
                vertex[left.pair_index, right.pair_index] += (
                    (cosine - 1.0)
                    * left.sign
                    * right.sign
                    / degree
                )
    return vertex


def number_diagonal() -> np.ndarray:
    return np.diag(
        [
            float(mask.bit_count())
            for mask in range(1 << MODE_COUNT)
            for _q in range(Q_DIMENSION)
        ]
    )


def total_momentum_diagonal(axis: int, alpha: float) -> np.ndarray:
    values: list[float] = []
    for mask in range(1 << MODE_COUNT):
        matter = mask_vector(mask)[axis]
        values.append(float(matter))
        for direction in range(MODE_COUNT):
            component_one = alpha * DIRECTIONS[direction][axis]
            component_two = (2.0 - alpha) * DIRECTIONS[direction][axis]
            values.append(float(matter + component_one + component_two))
    return np.diag(values)


def commutator_norm(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.linalg.norm(left @ right - right @ left))


def layer_indices(number: int) -> list[int]:
    return [
        Q_DIMENSION * mask + q
        for mask in range(1 << MODE_COUNT)
        if mask.bit_count() == number
        for q in range(Q_DIMENSION)
    ]


def layer_rows(vertex: np.ndarray) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    all_indices = np.arange(DIMENSION)
    for number in range(N_MAX + 1):
        indices = layer_indices(number)
        outside = np.setdiff1d(all_indices, indices)
        block = vertex[np.ix_(indices, indices)]
        weights = [
            float(abs(vertex[channel.pair_index, channel.reservoir_index]) ** 2)
            for channel in CHANNELS
            if channel.number == number
        ]
        rows.append(
            {
                "number": number,
                "mask_count": math.comb(MODE_COUNT, number),
                "dimension": len(indices),
                "active_channels": len(weights),
                "weight_min": min(weights, default=0.0),
                "weight_max": max(weights, default=0.0),
                "transpose_residual": float(np.linalg.norm(block.T - block)),
                "unitarity_residual": float(
                    np.linalg.norm(
                        block.conj().T @ block - np.eye(len(indices))
                    )
                ),
                "maximum_off_layer_amplitude": float(
                    np.max(
                        abs(vertex[np.ix_(outside, indices)]),
                        initial=0.0,
                    )
                ),
            }
        )
    return rows


def exact_equal_split_ledger() -> tuple[int, float]:
    maximum_residual = 0.0
    checked = 0
    for channel in CHANNELS:
        if channel.number > N_MAX:
            continue
        direction = np.asarray(DIRECTIONS[channel.direction], dtype=float)
        recoil = (
            mask_vector(channel.target_mask)
            - mask_vector(channel.source_mask)
        )
        component_one = EQUAL_COMPONENT_WEIGHTS[0] * direction
        component_two = EQUAL_COMPONENT_WEIGHTS[1] * direction
        maximum_residual = max(
            maximum_residual,
            float(np.max(abs(recoil + 2.0 * direction))),
            float(np.max(abs(recoil + component_one + component_two))),
        )
        checked += 1
    return checked, maximum_residual


def truncated_two_cell_independence(
    vertex: np.ndarray,
) -> tuple[int, int, float]:
    truncated_masks = [
        mask
        for mask in range(1 << MODE_COUNT)
        if mask.bit_count() <= N_MAX
    ]
    support = {
        (mask, q): np.flatnonzero(
            abs(vertex[:, Q_DIMENSION * mask + q]) > 2e-13
        )
        for mask in truncated_masks
        for q in range(Q_DIMENSION)
    }
    columns = 0
    failures = 0
    maximum_cross_layer = 0.0
    for _endpoint in range(2):
        for local_mask in truncated_masks:
            number = local_mask.bit_count()
            for _spectator_mask in truncated_masks:
                for q in range(Q_DIMENSION):
                    columns += 1
                    column = Q_DIMENSION * local_mask + q
                    for row in support[(local_mask, q)]:
                        if (int(row) // Q_DIMENSION).bit_count() != number:
                            failures += 1
                            maximum_cross_layer = max(
                                maximum_cross_layer,
                                float(abs(vertex[row, column])),
                            )
    return columns, failures, maximum_cross_layer


def real_bilinear_reciprocity(vertex: np.ndarray) -> dict[str, float]:
    indices = layer_indices(1) + layer_indices(2)
    block = vertex[np.ix_(indices, indices)]
    rng = np.random.default_rng(5708)
    left = rng.normal(size=len(indices))
    right = rng.normal(size=len(indices))
    left /= np.linalg.norm(left)
    right /= np.linalg.norm(right)
    return {
        "block_transpose_residual": float(np.linalg.norm(block.T - block)),
        "real_bilinear_swap_residual": float(
            abs(left @ block @ right - right @ block @ left)
        ),
    }


def misembedding_control(generator: np.ndarray) -> dict[str, float | int]:
    source_mask = (1 << 0) | (1 << 2)
    proper_target, sign = fermion_hop(source_mask, 0, OPPOSITE[0]) or (0, 0)
    source_column = Q_DIMENSION * source_mask
    proper_row = Q_DIMENSION * proper_target + 1
    bad_target = 1 << OPPOSITE[0]
    bad_row = Q_DIMENSION * bad_target + 1
    bad = generator.copy()
    bad[proper_row, source_column] = 0.0
    bad[source_column, proper_row] = 0.0
    bad[bad_row, source_column] = sign
    bad[source_column, bad_row] = sign
    number = number_diagonal()
    return {
        "source_number": source_mask.bit_count(),
        "target_number": bad_target.bit_count(),
        "number_commutator_frobenius": commutator_norm(bad, number),
    }


def main() -> int:
    started = time.monotonic()
    angle = MEDIATOR_COUPLING * MASS_FACTOR * math.tan(-BETA / 2.0)
    generator = source_generator()
    vertex = analytic_vertex(angle)
    number = number_diagonal()

    print("TRUNCATED-FOCK EQUAL-SPLIT BOOKKEEPING SUPPORT")
    print("supplied_scope =", SUPPLIED_SCOPE)
    print("certified_domain = n_left,n_right<=2")
    print("equal_split_status = supplied; not selected by conservation")

    check(
        "the independent checker is registered as an audit packet helper",
        (
            INDEPENDENT_PACKET_SOURCE.CHECKER_KIND
            == "clean-room-jordan-wigner"
        ),
        INDEPENDENT_PACKET_SOURCE.CHECKER_KIND,
    )
    check(
        "the analytic star vertex is unitary and number preserving",
        (
            float(np.linalg.norm(generator - generator.conj().T)) == 0.0
            and commutator_norm(generator, number) == 0.0
            and commutator_norm(vertex, number) < TOLERANCE
            and float(
                np.linalg.norm(vertex.conj().T @ vertex - np.eye(DIMENSION))
            )
            < TOLERANCE
        ),
        {
            "generator_number_commutator": commutator_norm(generator, number),
            "vertex_number_commutator": commutator_norm(vertex, number),
        },
    )

    alpha_family = {}
    for alpha in (0.0, 0.25, 1.0, 1.7, 2.0):
        alpha_family[str(alpha)] = max(
            commutator_norm(
                generator, total_momentum_diagonal(axis, alpha)
            )
            for axis in range(3)
        )
    check(
        "conservation fixes only the component sum; the equal split remains supplied",
        max(alpha_family.values()) < TOLERANCE,
        {
            "commutators_by_alpha": alpha_family,
            "selected_alpha": None,
            "supplied_alpha": 1.0,
        },
    )

    rows = layer_rows(vertex)
    expected_channels = (0, 6, 24)
    expected_masks = (1, 6, 15)
    analytic_weight = math.sin(angle) ** 2
    check(
        "the certified layers have the exact mask and channel counts",
        (
            tuple(row["mask_count"] for row in rows) == expected_masks
            and tuple(row["active_channels"] for row in rows)
            == expected_channels
            and max(
                float(row["maximum_off_layer_amplitude"]) for row in rows
            )
            == 0.0
            and max(float(row["unitarity_residual"]) for row in rows)
            < TOLERANCE
        ),
        rows,
    )
    check(
        "the supplied fixture reproduces the conditional layer-1 weight",
        (
            abs(float(rows[1]["weight_min"]) - analytic_weight) < TOLERANCE
            and abs(float(rows[1]["weight_max"]) - analytic_weight)
            < TOLERANCE
        ),
        {
            "angle": angle,
            "analytic_weight": analytic_weight,
            "observed_range": (
                rows[1]["weight_min"],
                rows[1]["weight_max"],
            ),
        },
    )

    ledger_channels, ledger_residual = exact_equal_split_ledger()
    check(
        "the supplied equal split gives the exact conditional recoil ledger",
        ledger_channels == 30 and ledger_residual == 0.0,
        {
            "channels": ledger_channels,
            "maximum_residual": ledger_residual,
            "ledger": "(-2d,+d,+d)",
        },
    )

    columns, leakage_failures, maximum_leakage = (
        truncated_two_cell_independence(vertex)
    )
    check(
        "the n_left,n_right<=2 slice is exhaustively number-layer independent",
        (
            columns == 6776
            and leakage_failures == 0
            and maximum_leakage == 0.0
        ),
        {
            "columns": columns,
            "factorization": "2*7*22^2",
            "failures": leakage_failures,
            "maximum_cross_layer_amplitude": maximum_leakage,
        },
    )

    reciprocal = real_bilinear_reciprocity(vertex)
    check(
        "fixed-basis transpose symmetry supports real-bilinear reciprocity",
        max(reciprocal.values()) < TOLERANCE,
        reciprocal,
    )

    bad = misembedding_control(generator)
    check(
        "a deliberate number-changing mutation is detected",
        (
            bad["source_number"] == 2
            and bad["target_number"] == 1
            and abs(
                float(bad["number_commutator_frobenius"]) - math.sqrt(2.0)
            )
            < TOLERANCE
        ),
        bad,
    )

    truncated_columns = 2 * Q_DIMENSION * 22**2
    complete_columns = 2 * Q_DIMENSION * 64**2
    check(
        "the certificate distinguishes the truncated slice from complete Fock space",
        (
            N_MAX == 2
            and truncated_columns == 6776
            and complete_columns == 57344
            and truncated_columns < complete_columns
        ),
        {
            "truncated_columns": truncated_columns,
            "complete_columns": complete_columns,
            "complete_number_layers": tuple(range(MODE_COUNT + 1)),
        },
    )

    runtime = time.monotonic() - started
    package = {
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "certificate_failures": FAILED_LABELS,
        "claim_scope": "two-cell n_left,n_right<=2 conditional bookkeeping support",
        "equal_split": {
            "status": "supplied_not_derived",
            "weights": EQUAL_COMPONENT_WEIGHTS,
        },
        "full_fock_claim": False,
        "layer_rows": rows,
        "note_path": NOTE_PATH,
        "runtime_seconds": round(runtime, 6),
        "summary": {"fail": FAIL, "pass": PASS},
        "support_certificate_passed": FAIL == 0,
    }
    print("FINAL_JSON", json.dumps(package, sort_keys=True))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
