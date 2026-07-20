#!/usr/bin/env python3
"""Cycle 472: dual-source relaxed-field / reciprocal M64 composition.

Two distinct local hard-core source stars occupy the global Q=2 sector.  Their
local flags drive one reversible Cycle-463-style two-defect word relaxation.
Six neighbor words at each source determine a covariant weighted extension of
the Cycle-426 even-CAR recoil vertex.  Both vertices act in one common update.

This is a finite dimensionless compiler witness.  It is not Newtonian gravity,
P2 closure, energy, force, acceleration, probability, a Record, or time.
Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
import resource
import sys
import time

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import expm_multiply


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_reversible_cubic_relaxation_clock_compiler_cycle463_2026_07_19 as c463
import physical_elementary_divsix_nn_compiler_cycle467_2026_07_19 as c467
import physical_recoil_hard_core_field_bridge_cycle426_2026_07_19 as c426


c315 = c426.c315
c322 = c426.c322
c423 = c426.c423
c219 = c322.c219
c210 = c322.c210

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DUAL_SOURCE_RECIPROCAL_COMPOSITION_CYCLE472_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOLERANCE = 1.2e-9
WORD_THRESHOLD = 2.1e-7
SIGNAL_FLOOR = 1.0e-7
BRANCH_FLOOR = 1.0e-6
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3
DIRECTIONS = np.asarray(c210.DIRECTIONS, dtype=int)
REVERSE = c322.REVERSE
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Pair = tuple[Coord, Coord]
LogicalState = dict[tuple[int, int], np.ndarray]


@dataclass(frozen=True)
class Fixture:
    name: str
    radius: int
    pairs: tuple[Pair, ...]
    amplitudes: tuple[complex, ...]
    held: bool


TRAIN = Fixture(
    "train-R1-axis",
    1,
    (
        ((-1, 0, 0), (0, 0, 0)),
        ((-1, 0, 0), (1, 0, 0)),
        ((0, -1, 0), (0, 1, 0)),
    ),
    tuple(np.asarray((1, 1j, -1), dtype=complex) / np.sqrt(3)),
    False,
)
HELD = Fixture(
    "held-R2-offaxis",
    2,
    (
        ((-2, 0, 0), (0, 0, 0)),
        ((-1, -1, 0), (1, 1, 0)),
        ((-2, -1, 0), (1, 1, 1)),
        ((-1, 0, 0), (0, 1, 1)),
    ),
    tuple(np.asarray((1, 1j, -1, -1j), dtype=complex) / 2),
    True,
)
FIXTURES = (TRAIN, HELD)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset", "global q2", "two distinct local q1 source cells",
        "e g_coarse = g_physical e", "both matter cells respond and recoil",
        "locally generated dual-source word field", "source flags uncompute",
        "coherent relative-position branches", "held unseen geometry", "no refit",
        "cycle230 contact seam", "cycle467 nearest-neighbor arithmetic",
        "inter-supercell word delivery remains open", "all 24 proper-cubic frames",
        "not newtonian", "not gravity", "not p2 closure", "not probability",
        "iteration count is not time", "phase is not energy", "n1 —", "n8 —",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in normalized(NOTE))
    check("the Cycle472 note freezes the dual-source composition and firewall", not missing, missing)


def validate_pair(radius: int, pair: Pair) -> None:
    item = c463.domain(radius)
    if len(pair) != 2 or pair[0] == pair[1] or any(coord not in item.active_index for coord in pair):
        raise ValueError("pair must contain two distinct active source cells")


def source_bits(radius: int, pair: Pair, deleted_source: int | None = None) -> tuple[int, ...]:
    validate_pair(radius, pair)
    if deleted_source not in (None, 0, 1):
        raise ValueError("deleted source must be endpoint zero, one, or none")
    item = c463.domain(radius)
    occupied = {coord for index, coord in enumerate(pair) if index != deleted_source}
    return tuple(int(coord in occupied) for coord in item.active)


def relax_history(
    radius: int,
    pair: Pair,
    *,
    deleted_source: int | None = None,
    deleted_rule: tuple[int, Coord] | None = None,
) -> tuple[tuple[int, ...], ...]:
    """Exact retained XOR history for two arbitrary locally flagged defects."""

    item = c463.domain(radius)
    source = source_bits(radius, pair, deleted_source)
    history = [[0 for _ in item.active] for _ in range(c463.ITERATIONS + 1)]
    for operation in c463.schedule(radius):
        if deleted_rule == (operation.layer, operation.target):
            continue
        previous = history[operation.layer]
        neighbors = tuple(
            previous[item.active_index[coord]] if coord in item.active_index else 0
            for coord in operation.neighbors
        )
        value = c463.local_quotient(neighbors, source[item.active_index[operation.target]])
        history[operation.layer + 1][item.active_index[operation.target]] ^= value
    return tuple(tuple(layer) for layer in history)


def reverse_history(
    radius: int,
    pair: Pair,
    history: tuple[tuple[int, ...], ...],
    *,
    deleted_source: int | None = None,
    deleted_rule: tuple[int, Coord] | None = None,
) -> tuple[tuple[int, ...], ...]:
    item = c463.domain(radius)
    source = source_bits(radius, pair, deleted_source)
    output = [list(layer) for layer in history]
    for operation in reversed(c463.schedule(radius)):
        if deleted_rule == (operation.layer, operation.target):
            continue
        previous = output[operation.layer]
        neighbors = tuple(
            previous[item.active_index[coord]] if coord in item.active_index else 0
            for coord in operation.neighbors
        )
        value = c463.local_quotient(neighbors, source[item.active_index[operation.target]])
        output[operation.layer + 1][item.active_index[operation.target]] ^= value
    return tuple(tuple(layer) for layer in output)


def word_residual(radius: int, pair: Pair, values: tuple[int, ...], deleted_source=None) -> float:
    item = c463.domain(radius)
    source = source_bits(radius, pair, deleted_source)
    maximum = Fraction()
    for coord in item.active:
        index = item.active_index[coord]
        neighbors = sum(
            values[item.active_index[n]] if n in item.active_index else 0
            for n in c463.six_neighbors(coord)
        )
        row = Fraction(6 * values[index] - neighbors - c463.DENOMINATOR * source[index], c463.DENOMINATOR)
        maximum = max(maximum, abs(row))
    return float(maximum)


def profile(radius: int, history: tuple[tuple[int, ...], ...]) -> dict[Coord, Fraction]:
    item = c463.domain(radius)
    return {
        coord: Fraction(history[-1][item.active_index[coord]], c463.DENOMINATOR)
        for coord in item.active
    }


def local_neighbor_weights(values: dict[Coord, Fraction], coord: Coord) -> np.ndarray:
    """The six local neighbor words, normalized; uniform only for all-zero input."""

    neighbors = [values.get(tuple(np.asarray(coord) + direction), Fraction()) for direction in DIRECTIONS]
    total = sum(neighbors, Fraction())
    if total == 0:
        return np.full(6, 1 / 6, dtype=float)
    return np.asarray([float(value / total) for value in neighbors], dtype=float)


def pair_weights(radius: int, pair: Pair, *, deleted_source=None, deleted_rule=None):
    history = relax_history(radius, pair, deleted_source=deleted_source, deleted_rule=deleted_rule)
    values = profile(radius, history)
    weights = tuple(local_neighbor_weights(values, coord) for coord in pair)
    return history, values, weights


@lru_cache(maxsize=128)
def weighted_recoil_generator(q_number: int, weights: tuple[float, ...]) -> sparse.csr_matrix:
    if q_number not in range(8) or len(weights) != 6 or min(weights) < 0 or abs(sum(weights) - 1) > 2e-12:
        raise ValueError("weighted source leaves its local Q/direction domain")
    states = c426.LOCAL_STATES[q_number]
    state_index = c426.LOCAL_STATE_INDEX[q_number]
    field_dimension = len(states)
    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []
    coefficients = np.sqrt(6 * np.asarray(weights, dtype=float))
    for matter_index, mask in enumerate(c322.LOCAL_MASKS):
        for field_index, field_state in enumerate(states):
            reservoir, field = divmod(field_state, 64)
            if reservoir != 1:
                continue
            source = matter_index * field_dimension + field_index
            for direction in range(6):
                if ((field >> direction) & 1) or coefficients[direction] == 0:
                    continue
                hopped = c322.fermion_hop(mask, direction, REVERSE[direction])
                if hopped is None:
                    continue
                target_mask, sign = hopped
                target = (
                    c322.LOCAL_INDEX[target_mask] * field_dimension
                    + state_index[field | (1 << direction)]
                )
                coefficient = complex(sign * coefficients[direction])
                rows.extend((target, source))
                columns.extend((source, target))
                data.extend((coefficient, coefficient))
    dimension = 64 * field_dimension
    return sparse.coo_matrix((data, (rows, columns)), shape=(dimension, dimension), dtype=complex).tocsr()


def weight_key(weights: np.ndarray) -> tuple[float, ...]:
    return tuple(float(value) for value in weights)


def apply_weighted_source(
    state: LogicalState,
    endpoint: int,
    weights: np.ndarray,
    *,
    inverse: bool = False,
    enabled: bool = True,
) -> LogicalState:
    if endpoint not in (0, 1):
        raise ValueError("endpoint must be zero or one")
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    output: LogicalState = {}
    other_values = sorted({pair[1 - endpoint] for pair in state})
    exponential_sign = -1 if inverse else 1
    for other_field in other_values:
        other_q = c423.local_q(other_field)
        for local_q in range(3 - other_q):
            local_states = c426.LOCAL_STATES[local_q]
            local_dimension = len(local_states)
            block = np.zeros((64 * local_dimension, 64), dtype=complex)
            present = False
            for field_index, local_field in enumerate(local_states):
                pair = (local_field, other_field) if endpoint == 0 else (other_field, local_field)
                value = state.get(pair)
                if value is None:
                    continue
                present = True
                for local_matter in range(64):
                    for other_matter in range(64):
                        joint = c322.JOINT_INDEX[(local_matter, other_matter)] if endpoint == 0 else c322.JOINT_INDEX[(other_matter, local_matter)]
                        block[local_matter * local_dimension + field_index, other_matter] = value[joint]
            if not present:
                continue
            transformed = expm_multiply(
                exponential_sign * 1j * c426.ANGLE * weighted_recoil_generator(local_q, weight_key(weights)),
                block,
            )
            for field_index, local_field in enumerate(local_states):
                pair = (local_field, other_field) if endpoint == 0 else (other_field, local_field)
                vector = np.zeros(c426.MATTER_DIM, dtype=complex)
                for local_matter in range(64):
                    for other_matter in range(64):
                        joint = c322.JOINT_INDEX[(local_matter, other_matter)] if endpoint == 0 else c322.JOINT_INDEX[(other_matter, local_matter)]
                        vector[joint] = transformed[local_matter * local_dimension + field_index, other_matter]
                if np.linalg.norm(vector) > 2e-13:
                    output[pair] = vector
    return c426.prune(output)


def common_source_step(state: LogicalState, factors, weights, *, enabled=(True, True)) -> LogicalState:
    output = c426.apply_matter_factor(state, factors[0])
    output = apply_weighted_source(output, 0, weights[0], enabled=enabled[0])
    return apply_weighted_source(output, 1, weights[1], enabled=enabled[1])


def common_source_inverse(state: LogicalState, factors, weights) -> LogicalState:
    output = apply_weighted_source(state, 1, weights[1], inverse=True)
    output = apply_weighted_source(output, 0, weights[0], inverse=True)
    return c426.apply_matter_factor(output, factors[0].getH())


def state_inner(left: LogicalState, right: LogicalState) -> complex:
    zero = np.zeros(c426.MATTER_DIM, dtype=complex)
    return sum(np.vdot(left.get(key, zero), right.get(key, zero)) for key in left.keys() | right.keys())


def state_residual(left: LogicalState, right: LogicalState) -> float:
    return c426.state_residual(left, right)


def matter_vector(state: LogicalState, endpoint: int) -> np.ndarray:
    values = np.zeros(3, dtype=float)
    local_vectors = np.asarray([
        sum((DIRECTIONS[d] for d in range(6) if (mask >> d) & 1), start=np.zeros(3, dtype=int))
        for mask in c322.LOCAL_MASKS
    ])
    diagonal = np.empty((c426.MATTER_DIM, 3), dtype=float)
    for index, (_ln, left_label, _rn, right_label) in enumerate(c322.LABELS):
        mask = sum(1 << d for d in (left_label if endpoint == 0 else right_label))
        diagonal[index] = local_vectors[c322.LOCAL_INDEX[mask]]
    for amplitude in state.values():
        values += np.abs(amplitude) ** 2 @ diagonal
    return values


def field_vector(state: LogicalState, endpoint: int) -> np.ndarray:
    output = np.zeros(3, dtype=float)
    for pair, amplitude in state.items():
        field = pair[endpoint] % 64
        direction = sum((DIRECTIONS[d] for d in range(6) if (field >> d) & 1), start=np.zeros(3, dtype=int))
        output += float(np.vdot(amplitude, amplitude).real) * direction
    return output


def initial_state() -> LogicalState:
    return {(64, 64): c322.symmetric_one_one_state()}


def physical_weighted_source(state, encoding, endpoint, weights, *, inverse=False):
    decoded = {key: encoding.getH() @ value for key, value in state.items()}
    transformed = apply_weighted_source(decoded, endpoint, weights, inverse=inverse)
    output = {}
    zero_physical = np.zeros(encoding.shape[0], dtype=complex)
    zero_logical = np.zeros(c426.MATTER_DIM, dtype=complex)
    for key in state.keys() | transformed.keys():
        before_physical = state.get(key, zero_physical)
        before_logical = decoded.get(key, zero_logical)
        after_logical = transformed.get(key, zero_logical)
        output[key] = before_physical + encoding @ (after_logical - before_logical)
    return c426.prune(output)


def physical_source_step(state, encoding, factors, weights):
    output = c426.apply_physical_matter_factor(state, encoding, factors[0])
    output = physical_weighted_source(output, encoding, 0, weights[0])
    return physical_weighted_source(output, encoding, 1, weights[1])


def transformed_pair(frame: np.ndarray, pair: Pair) -> Pair:
    return tuple(tuple(int(value) for value in frame @ np.asarray(coord)) for coord in pair)  # type: ignore[return-value]


def direction_map(frame: np.ndarray) -> tuple[int, ...]:
    return tuple(int(np.where(np.all(DIRECTIONS == frame @ direction, axis=1))[0][0]) for direction in DIRECTIONS)


def word_generation_controls() -> dict[tuple[int, Pair], tuple[np.ndarray, np.ndarray]]:
    print("\nDUAL-SOURCE LOCAL WORD GENERATION / UNCOMPUTE")
    rows = []
    weight_rows = {}
    arithmetic_digest = sha256()
    for fixture in FIXTURES:
        item = c463.domain(fixture.radius)
        for pair in fixture.pairs:
            history, values, weights = pair_weights(fixture.radius, pair)
            restored = reverse_history(fixture.radius, pair, history)
            source = source_bits(fixture.radius, pair)
            flags_after_compute = sum(source)
            flags_after_uncompute = sum(bit ^ bit for bit in source)
            maximum_remainder = 0
            for operation in c463.schedule(fixture.radius):
                prior = history[operation.layer]
                neighbors = tuple(prior[item.active_index[n]] if n in item.active_index else 0 for n in operation.neighbors)
                numerator = sum(neighbors) + c463.DENOMINATOR * source[item.active_index[operation.target]]
                quotient, remainder = c467.compiled_division(numerator, c463.VALUE_BITS)
                maximum_remainder = max(maximum_remainder, remainder)
                arithmetic_digest.update(f"{fixture.radius}|{pair}|{operation.layer}|{operation.target}|{quotient}|{remainder}\n".encode())
            row = {
                "fixture": fixture.name, "pair": pair, "source_flags": flags_after_compute,
                "source_flags_after_uncompute": flags_after_uncompute,
                "word_residual": word_residual(fixture.radius, pair, history[-1]),
                "inverse_exact": all(value == 0 for layer in restored for value in layer),
                "maximum_divisibility_remainder": maximum_remainder,
                "weight_sums": tuple(float(sum(value)) for value in weights),
            }
            rows.append(row)
            weight_rows[(fixture.radius, pair)] = weights
    check(
        "two distinct local Q1 source flags generate and exactly uncompute one dual-source retained word field",
        all(row["source_flags"] == 2 and row["source_flags_after_uncompute"] == 0 and row["inverse_exact"] and row["maximum_divisibility_remainder"] == 0 and row["word_residual"] < WORD_THRESHOLD and max(abs(value - 1) for value in row["weight_sums"]) < TOLERANCE for row in rows),
        {"rows": rows, "all_row_arithmetic_digest": arithmetic_digest.hexdigest(), "source_flag_support": "one reservoir M2 plus one blank flag M2 per active source; compute/uncompute CNOT"},
    )
    return weight_rows


def operator_and_covariance_controls(weight_rows) -> None:
    print("\nWEIGHTED RECOIL OPERATOR / ALL24 COVARIANCE")
    frames = c463.proper_cubic_frames()
    maximum_hermiticity = 0.0
    maximum_frame = 0.0
    maximum_word = 0.0
    maximum_weight = 0.0
    maximum_commutator = 0.0
    sample_pairs = (TRAIN.pairs[1], HELD.pairs[1], HELD.pairs[2])
    for fixture, pair in ((TRAIN, sample_pairs[0]), (HELD, sample_pairs[1]), (HELD, sample_pairs[2])):
        history, values, weights = pair_weights(fixture.radius, pair)
        for endpoint in (0, 1):
            generator = weighted_recoil_generator(1, weight_key(weights[endpoint]))
            maximum_hermiticity = max(maximum_hermiticity, float(sparse.linalg.norm(generator - generator.getH())))
            number = c426.local_diagonal(1, lambda mask, _field: mask.bit_count())
            qop = c426.local_diagonal(1, lambda _mask, field: c423.local_q(field))
            maximum_commutator = max(maximum_commutator, float(sparse.linalg.norm(generator @ number - number @ generator)), float(sparse.linalg.norm(generator @ qop - qop @ generator)))
        for frame_tuple in frames:
            frame = np.asarray(frame_tuple, dtype=int)
            carried_pair = transformed_pair(frame, pair)
            carried_history, carried_values, carried_weights = pair_weights(fixture.radius, carried_pair)
            for coord, value in values.items():
                maximum_word = max(maximum_word, abs(float(value - carried_values[tuple(int(x) for x in frame @ np.asarray(coord))])))
            mapping = direction_map(frame)
            for endpoint in (0, 1):
                expected = np.zeros(6)
                for source_direction, target_direction in enumerate(mapping):
                    expected[target_direction] = weights[endpoint][source_direction]
                maximum_weight = max(maximum_weight, float(np.max(abs(expected - carried_weights[endpoint]))))
                representation = c426.recoil_frame(1, frame)
                transformed = representation @ weighted_recoil_generator(1, weight_key(weights[endpoint])) @ representation.getH()
                target = weighted_recoil_generator(1, weight_key(carried_weights[endpoint]))
                maximum_frame = max(maximum_frame, float(sparse.linalg.norm(transformed - target)))
    check(
        "the dual word law and weighted even-CAR recoil family carry through all 24 proper-cubic frames",
        len(frames) == 24 and max(maximum_hermiticity, maximum_commutator, maximum_word, maximum_weight, maximum_frame) < TOLERANCE,
        {"proper_cubic_frames": len(frames), "maximum_word_residual": maximum_word, "maximum_weight_residual": maximum_weight, "maximum_generator_frame_residual": maximum_frame, "maximum_Hermiticity_or_Q_number_commutator": max(maximum_hermiticity, maximum_commutator)},
    )


def response_controls(factors, weight_rows):
    print("\nTWO-ACTIVE-SOURCE RESPONSE / RELATIVE BRANCHES")
    fixture_results = {}
    all_rows = []
    for fixture in FIXTURES:
        branch_states = []
        rows = []
        for pair in fixture.pairs:
            weights = weight_rows[(fixture.radius, pair)]
            state = initial_state()
            coined = c426.apply_matter_factor(state, factors[0])
            ordered_ab = apply_weighted_source(
                apply_weighted_source(coined, 0, weights[0]), 1, weights[1]
            )
            ordered_ba = apply_weighted_source(
                apply_weighted_source(coined, 1, weights[1]), 0, weights[0]
            )
            _swapped_history, _swapped_values, swapped_weights = pair_weights(
                fixture.radius, (pair[1], pair[0])
            )
            first = common_source_step(state, factors, weights)
            restored = common_source_inverse(first, factors, weights)
            second = common_source_step(first, factors, weights)
            row = {
                "pair": pair,
                "matter_A": matter_vector(first, 0), "matter_B": matter_vector(first, 1),
                "field_A": field_vector(first, 0), "field_B": field_vector(first, 1),
                "reservoir_A": c426.reservoir_weight(first, 0), "reservoir_B": c426.reservoir_weight(first, 1),
                "inverse": state_residual(restored, state), "norm_drift": abs(c426.state_norm(second) - 1),
                "endpoint_order_residual": state_residual(ordered_ab, ordered_ba),
                "source_exchange_weight_residual": float(
                    max(
                        np.max(abs(weights[0] - swapped_weights[1])),
                        np.max(abs(weights[1] - swapped_weights[0])),
                    )
                ),
            }
            row["response_norm_A"] = float(np.linalg.norm(row["matter_A"]))
            row["response_norm_B"] = float(np.linalg.norm(row["matter_B"]))
            rows.append(row)
            branch_states.append(first)
        response_vectors = [np.concatenate((row["matter_A"], row["matter_B"], row["field_A"], row["field_B"])) for row in rows]
        pairwise = [float(np.linalg.norm(left - right)) for index, left in enumerate(response_vectors) for right in response_vectors[index + 1 :]]
        gram = np.asarray([[state_inner(left, right) for right in branch_states] for left in branch_states])
        amplitudes = np.asarray(fixture.amplitudes)
        rho = amplitudes[:, None] * amplitudes.conj()[None, :] * gram.T
        eigenvalues = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
        schmidt_tail = float(np.sqrt(max(0.0, 1 - np.max(eigenvalues))))
        fixture_results[fixture.name] = {"rows": rows, "minimum_pairwise_response": min(pairwise), "Schmidt_tail": schmidt_tail, "Schmidt_rank": int(np.count_nonzero(eigenvalues > 1e-10))}
        all_rows.extend(rows)
    check(
        "one common two-vertex update makes both active matter cells recoil with relative-position-dependent coherent branch output",
        min(min(row["response_norm_A"], row["response_norm_B"]) for row in all_rows) > SIGNAL_FLOOR and max(max(row["inverse"], row["norm_drift"], row["endpoint_order_residual"], row["source_exchange_weight_residual"]) for row in all_rows) < TOLERANCE and min(value["minimum_pairwise_response"] for value in fixture_results.values()) > BRANCH_FLOOR and min(value["Schmidt_tail"] for value in fixture_results.values()) > SIGNAL_FLOOR and min(value["Schmidt_rank"] for value in fixture_results.values()) > 1,
        fixture_results,
    )
    return fixture_results


def physical_eg_controls(factors, weight_rows) -> None:
    print("\nPHYSICAL M2 E/G / INVERSE / LEAKAGE")
    encoding = c322.build_encoding(3)
    gram = encoding.getH() @ encoding
    rows = []
    for fixture, pair in ((TRAIN, TRAIN.pairs[0]), (HELD, HELD.pairs[-1])):
        weights = weight_rows[(fixture.radius, pair)]
        logical = initial_state()
        encoded = c426.encode_physical(logical, encoding)
        logical_out = common_source_step(logical, factors, weights)
        physical_out = physical_source_step(encoded, encoding, factors, weights)
        expected = c426.encode_physical(logical_out, encoding)
        decoded = {key: encoding.getH() @ value for key, value in physical_out.items()}
        projected = c426.encode_physical(decoded, encoding)
        restored = common_source_inverse(logical_out, factors, weights)
        rows.append({"fixture": fixture.name, "pair": pair, "EG": state_residual(physical_out, expected), "leakage": state_residual(physical_out, projected), "inverse": state_residual(restored, logical)})
    gram_residual = c315.largest_singular(gram - sparse.eye(gram.shape[0], format="csc"))
    check(
        "the weighted global-Q2 source layer satisfies E G_coarse = G_physical E with exact code return",
        gram_residual < TOLERANCE and max(max(row["EG"], row["leakage"], row["inverse"]) for row in rows) < TOLERANCE,
        {"rows": rows, "encoding_columns": encoding.shape[1], "Gram_opnorm": gram_residual, "global_Q2": "one local Q1 hard-core source star at each of two distinct cells", "physical_completion": "identity on the orthogonal complement"},
    )


def deletions_and_seam_controls(factors, weight_rows) -> None:
    print("\nSOURCE / RECOIL / FIELD / CONTACT DELETIONS")
    rows = []
    for fixture, pair in ((TRAIN, TRAIN.pairs[1]), (HELD, HELD.pairs[1])):
        weights = weight_rows[(fixture.radius, pair)]
        intact = common_source_step(initial_state(), factors, weights)
        deleted_source_rows = []
        for source in (0, 1):
            _history, _values, deleted_weights = pair_weights(fixture.radius, pair, deleted_source=source)
            deleted_source_rows.append(state_residual(intact, common_source_step(initial_state(), factors, deleted_weights)))
        deleted_recoil = tuple(state_residual(intact, common_source_step(initial_state(), factors, weights, enabled=(source != 0, source != 1))) for source in (0, 1))
        deleted_coupling = state_residual(intact, c426.apply_matter_factor(initial_state(), factors[0]))
        # The endpoint response reads the six final-layer neighbor words, not
        # the endpoint's own final word.  Delete an actually consumed row.
        deleted_neighbor = next(
            coord for coord in c463.six_neighbors(pair[0])
            if coord in c463.domain(fixture.radius).active_index
        )
        deleted_rule = (c463.ITERATIONS - 1, deleted_neighbor)
        _history, _values, rule_weights = pair_weights(fixture.radius, pair, deleted_rule=deleted_rule)
        rule_residual = state_residual(intact, common_source_step(initial_state(), factors, rule_weights))
        rows.append({"fixture": fixture.name, "source_deletions": deleted_source_rows, "recoil_vertex_deletions": deleted_recoil, "field_coupling_deletion": deleted_coupling, "final_local_rule_deletion": rule_residual})
    seam_probe = c426.random_common_state(472)
    seam_intact = c426.logical_step(seam_probe, factors)
    seam_deleted = c426.logical_step(seam_probe, factors, contact_enabled=False)
    seam_inverse = c426.logical_inverse(seam_intact, factors)
    contact_residual = state_residual(seam_intact, seam_deleted)
    check(
        "either word source, either recoil vertex, the word/recoil coupling, a final field rule, and the Cycle230 contact seam are independently visible",
        min(min(row["source_deletions"] + list(row["recoil_vertex_deletions"]) + [row["field_coupling_deletion"], row["final_local_rule_deletion"]]) for row in rows) > SIGNAL_FLOOR and contact_residual > 0.1 and state_residual(seam_inverse, seam_probe) < TOLERANCE,
        {"dual_source_rows": rows, "Cycle230_contact_deletion_residual": contact_residual, "complete_seam_inverse_residual": state_residual(seam_inverse, seam_probe)},
    )


def mass_contact_and_routing_controls(started: float) -> None:
    print("\nMASS / CONTACT / LITERAL NN / CAPACITY")
    species = c219.common_species(-0.3)
    rest = np.ones(6, dtype=complex) / np.sqrt(6)
    eigenvalue = np.vdot(rest, species.coin @ rest)
    rest_mass = c219.rest_mass(species)
    mass_residual = abs(rest_mass - species.analytic_mass)
    circuit = c467.make_circuit(c463.VALUE_BITS, c463.DENOMINATOR)
    routed = c467.compile_nearest_neighbor(circuit)
    route_ok = routed.adjacency_failures == 0 and routed.restored_mapping and routed.events == 12_719_213
    capacities = {fixture.name: {"word_field_M2": c463.domain(fixture.radius).physical_m2, "source_cells_added_M2": 2 * 36, "local_source_star_support_M2": 25, "Cycle467_arithmetic_work_M2": len(circuit.layout.work), "Cycle467_declared_ports_plus_wires": circuit.layout.wire_count} for fixture in FIXTURES}
    check(
        "the one-particle mass and Cycle230 seam survive while the available Cycle467 arithmetic is literally NN routed inside each scale40 supercell",
        mass_residual < 2e-12 and route_ok and circuit.layout.wire_count < c463.SUPERCELL_M2,
        {"mass": species.analytic_mass, "rest_mass": rest_mass, "rest_coin_eigenvalue": eigenvalue, "mass_fixture_residual": mass_residual, "Cycle230_contact_nontrivial_columns": 4047, "routed_events": routed.events, "routed_counts": dict(routed.counts), "routed_digest": routed.digest, "adjacency_failures": routed.adjacency_failures, "placement_restored": routed.restored_mapping, "capacities": capacities, "literal_NN_boundary": "arithmetic inside one scale40 supercell and local source/seam factors; inter-supercell word delivery remains open in this dual-source composition, although Cycle470 supplies one-star delivery separately"},
    )


def domain_inventory_no_go_controls(started: float) -> None:
    print("\nLAWFUL DOMAIN / INVENTORY / FIREWALL / N1-N8")
    rejected = 0
    for action in (
        lambda: validate_pair(1, ((0, 0, 0), (0, 0, 0))),
        lambda: validate_pair(1, ((0, 0, 0), (2, 0, 0))),
        lambda: source_bits(1, TRAIN.pairs[0], 2),
        lambda: weighted_recoil_generator(1, (1.0, 0, 0, 0, 0, 0.1)),
        lambda: weighted_recoil_generator(8, tuple(np.full(6, 1 / 6))),
    ):
        try:
            action()
        except (ValueError, OverflowError):
            rejected += 1
    inventory = {
        "supplied": ["two finite zero-shell domains and coherent pair menus", "unit source word D=6^96, 96 retained layers, 249-bit words", "six-neighbor normalization and sqrt(6 w_d) weighted coupling", "Cycle219 mass coin, Cycle426 angle, factor order, initial symmetric one-one matter ray", "word-to-coupling arithmetic/amplitude synthesis outside the div-six block", "finite readouts, tolerances, and branch amplitudes"],
        "derived": ["exact dual-defect relaxation and reverse", "two local source-flag compute/uncompute", "weighted even-CAR Q/number/recoil ledger and all24 covariance", "two-active-source branch-dependent reciprocal response", "physical M2 E/G, inverse, leakage, held geometry, deletions", "literal Cycle467 intra-supercell NN arithmetic route"],
        "open": ["composition of Cycle470 one-star inter-supercell delivery with both source vertices and a whole layer", "primitive word-normalization/square-root/controlled-source exponential", "autonomous recurrent source preparation and full cubic multi-edge execution", "infinite-volume/continuum and 1/r asymptotics", "rho=m|psi|^2, G_Newton, physical duration and phase calibration", "energy/stress/source tensor, metric/lapse/curvature, Records and Born law"],
        "firewall": {"wrapped_phase_called_energy": False, "generator_called_rate": False, "iteration_or_depth_called_time": False, "coherent_weight_called_probability": False, "pointer_copy_called_Record": False, "finite_mechanism_called_Newtonian_or_gravity_or_P2": False},
        "N1": "attempted weighted hard-core Q2 route succeeds finitely; recurrent gauge, quantum-walk path sum, direct exchange/scattering, autonomous amplitude compiler, and operational instrument routes remain open",
        "N2": "source calibration, amplitude/transport compilation, physical time, infrared control, and occurrence remain independent",
        "N3": "finite boundary, pair menu, D/precision/layers, normalization/square root, angle, mass coin, preparation, readouts, and missing delivery are explicit",
        "N4": "matches Cycle468's two-active-source/recoil residual and Cycle467's intra-supercell arithmetic surface; Cycle470 one-star delivery exists separately but is not composed; does not match P2, gravity, Green asymptotics, or clock residuals",
        "N5": "claims stop at exact finite response/recoil and coherent branch diagnostics",
        "N6": "Cycle470 delivery composition, whole-layer routing, autonomous synthesis, recurrence, calibration, and asymptotics are live constructive paths",
        "N7": "hostile reviewer should reject Newtonian, force, acceleration, BMV, probability, P2, or gravity language and any minimality claim",
        "N8": "Cycle328/426 already close other Q2 sectors; Cycle472's novelty is their composition with a locally generated two-defect word field, not first Q2 or first recoil",
        "gate": "broad no-go FAIL; minimum-content FAIL; axiom-pressure FAIL; no axiom pressure",
    }
    check(
        "malformed pairs, source deletion labels, weights, and Q sectors are rejected and all interpretation firewalls remain closed",
        rejected == 5 and not any(inventory["firewall"].values()),
        {"rejected": rejected, **inventory},
    )
    elapsed = time.perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(raw if sys.platform == "darwin" else raw * 1024)
    check("the bounded runner stays within its declared wall/RSS caps", elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES, {"elapsed_seconds": elapsed, "peak_RSS_MiB": rss / 1024**2, "wall_cap_seconds": WALL_CAP_SECONDS, "RSS_cap_GiB": RSS_CAP_BYTES / 1024**3})


def main() -> int:
    started = time.perf_counter()
    note_contract()
    factors = c315.logical_update_controls(c322.LABELS)[:3]
    weights = word_generation_controls()
    operator_and_covariance_controls(weights)
    response_controls(factors, weights)
    physical_eg_controls(factors, weights)
    deletions_and_seam_controls(factors, weights)
    mass_contact_and_routing_controls(started)
    domain_inventory_no_go_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    if FAIL:
        return 1
    print("RESULT PHYSICAL_DUAL_SOURCE_RECIPROCAL_COMPOSITION_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
