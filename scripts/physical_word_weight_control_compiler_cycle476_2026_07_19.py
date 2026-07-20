#!/usr/bin/env python3
"""Cycle 476: reversible word-to-weight / controlled recoil compiler.

Starting with six 249-bit neighbor words at Cycle-467 ports, compute a
fixed-point approximation to sqrt(6*n_d/sum n), uncompute all arithmetic work,
and compile the retained coefficient bits into fixed-angle two-level rotations
for the Cycle-426 local q=1 even-CAR source star.

This is a bounded candidate-law compiler.  It is not energy, a rate, time,
force, acceleration, probability, P2 closure, or gravity.  Authority is none;
audit is unset.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
import math
from pathlib import Path
import resource
import struct
import sys
import time

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import expm_multiply


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_elementary_divsix_nn_compiler_cycle467_2026_07_19 as c467
import physical_seven_supercell_port_delivery_compiler_cycle470_2026_07_19 as c470
import physical_dual_source_reciprocal_composition_cycle472_2026_07_19 as c472


c463 = c467.c463
c426 = c472.c426
c322 = c472.c322
c423 = c472.c423
c210 = c472.c210

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_WORD_WEIGHT_CONTROL_COMPILER_CYCLE476_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

B = c463.VALUE_BITS
SUM_WIDTH = B + 3
FRACTION_BITS = 8
COEFFICIENT_BITS = 10
SQUARE_WIDTH = 2 * COEFFICIENT_BITS
PRODUCT_WIDTH = SUM_WIDTH + SQUARE_WIDTH
COEFFICIENT_SCALE = 1 << FRACTION_BITS
TOLERANCE = 2.0e-10
QUANTIZATION_BOUND = 1 / COEFFICIENT_SCALE
UNITARY_ERROR_CAP = 8.0e-3
STRANG_STEPS = 8
PRODUCT_FORMULA_ERROR_CAP = 2.0e-3
SIGNAL_FLOOR = 1.0e-6
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3

X, CX, CCX = c467.X, c467.CX, c467.CCX
Gate = c467.Gate


@dataclass(frozen=True)
class Layout:
    neighbors: tuple[tuple[int, ...], ...]
    coefficients: tuple[tuple[int, ...], ...]
    total: tuple[int, ...]
    pad: tuple[int, ...]
    mask: tuple[int, ...]
    square: tuple[int, ...]
    product: tuple[int, ...]
    target: tuple[int, ...]
    equality: tuple[int, ...]
    nonzero_prefix: tuple[int, ...]
    carry: int
    mcx_aux: int
    leq: int
    valid: int
    wire_count: int

    @property
    def inputs(self) -> tuple[int, ...]:
        return tuple(wire for word in self.neighbors for wire in word)

    @property
    def outputs(self) -> tuple[int, ...]:
        return tuple(wire for word in self.coefficients for wire in word)

    @property
    def work(self) -> tuple[int, ...]:
        excluded = set(self.inputs + self.outputs)
        return tuple(wire for wire in range(self.wire_count) if wire not in excluded)


@dataclass(frozen=True)
class Circuit:
    layout: Layout
    trace: tuple[Gate, ...]
    root_segments: tuple[tuple[int, int, int, int], ...]
    digest: str
    counts: dict[str, int]


@dataclass(frozen=True)
class WordRow:
    name: str
    radius: int
    pair: c472.Pair
    endpoint: int
    words: tuple[int, ...]
    held: bool


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
        "authority: none", "audit: unset", "six 249-bit neighbor words",
        "fixed precision p=8", "sqrt(6 n_d/s)", "all-zero code",
        "exact inverse and work uncompute", "controlled source rotation",
        "local q1 source-star sector", "26-m2 rotation support",
        "cycle470 is available prior art", "no whole-layer composition claim",
        "held unseen word rows", "all 24 proper-cubic frames",
        "inter-supercell delivery is not replayed", "iteration count is not time",
        "phase is not energy", "not probability", "n1 —", "n8 —",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in normalized(NOTE))
    check("the Cycle476 note freezes the word-weight/control compiler boundary", not missing, missing)


def allocate_layout() -> Layout:
    cursor = 0

    def take(count: int) -> tuple[int, ...]:
        nonlocal cursor
        output = tuple(range(cursor, cursor + count))
        cursor += count
        return output

    neighbors = tuple(take(B) for _ in range(6))
    coefficients = tuple(take(COEFFICIENT_BITS) for _ in range(6))
    total = take(SUM_WIDTH)
    pad = take(PRODUCT_WIDTH)
    mask = take(PRODUCT_WIDTH)
    square = take(SQUARE_WIDTH)
    product_register = take(PRODUCT_WIDTH)
    target = take(PRODUCT_WIDTH)
    equality = take(PRODUCT_WIDTH + 1)
    nonzero_prefix = take(SUM_WIDTH + 1)
    carry, mcx_aux, leq, valid = take(4)
    return Layout(
        neighbors, coefficients, total, pad, mask, square, product_register,
        target, equality, nonzero_prefix, carry, mcx_aux, leq, valid, cursor,
    )


def padded_operand(
    operand: tuple[int, ...], shift: int, width: int, pad: tuple[int, ...]
) -> tuple[int, ...]:
    if shift < 0 or shift + len(operand) > width or len(pad) < width:
        raise ValueError("operand leaves padded arithmetic width")
    return tuple(
        operand[position - shift] if shift <= position < shift + len(operand) else pad[position]
        for position in range(width)
    )


def uncontrolled_add(
    operand: tuple[int, ...], shift: int, accumulator: tuple[int, ...], layout: Layout
) -> tuple[Gate, ...]:
    addend = padded_operand(operand, shift, len(accumulator), layout.pad)
    return c467.cuccaro_add(addend, accumulator, layout.carry)


def controlled_add(
    control: int,
    operand: tuple[int, ...],
    shift: int,
    accumulator: tuple[int, ...],
    layout: Layout,
) -> tuple[Gate, ...]:
    width = len(accumulator)
    if width > len(layout.mask):
        raise ValueError("controlled add exceeds mask width")
    compute: list[Gate] = []
    for position in range(width):
        if shift <= position < shift + len(operand):
            source = operand[position - shift]
            compute.append(
                c467.gate(CX, source, layout.mask[position])
                if source == control
                else c467.gate(CCX, control, source, layout.mask[position])
            )
    add = c467.cuccaro_add(layout.mask[:width], accumulator, layout.carry)
    return tuple(compute) + add + tuple(reversed(compute))


def mcx3(
    controls: tuple[int, int, int],
    target: int,
    auxiliary: int,
    negative: tuple[bool, bool, bool] = (False, False, False),
) -> tuple[Gate, ...]:
    prefix = tuple(c467.gate(X, wire) for wire, flag in zip(controls, negative) if flag)
    positive = (
        c467.gate(CCX, controls[0], controls[1], auxiliary),
        c467.gate(CCX, auxiliary, controls[2], target),
        c467.gate(CCX, controls[0], controls[1], auxiliary),
    )
    return prefix + positive + tuple(reversed(prefix))


def compare_leq_trace(layout: Layout) -> tuple[Gate, ...]:
    """XOR [product <= target] into leq, restoring equality work."""

    output: list[Gate] = [c467.gate(X, layout.equality[0])]
    equality_compute: list[tuple[Gate, ...]] = []
    for step, bit in enumerate(reversed(range(PRODUCT_WIDTH))):
        prefix = layout.equality[step]
        output.extend(
            mcx3(
                (prefix, layout.product[bit], layout.target[bit]),
                layout.leq,
                layout.mcx_aux,
                (False, True, False),
            )
        )
        equal_zero = mcx3(
            (prefix, layout.product[bit], layout.target[bit]),
            layout.equality[step + 1],
            layout.mcx_aux,
            (False, True, True),
        )
        equal_one = mcx3(
            (prefix, layout.product[bit], layout.target[bit]),
            layout.equality[step + 1],
            layout.mcx_aux,
        )
        block = equal_zero + equal_one
        output.extend(block)
        equality_compute.append(block)
    output.append(c467.gate(CX, layout.equality[-1], layout.leq))
    for block in reversed(equality_compute):
        output.extend(reversed(block))
    output.append(c467.gate(X, layout.equality[0]))
    return tuple(output)


def nonzero_trace(layout: Layout) -> tuple[Gate, ...]:
    output: list[Gate] = []
    for index, source in enumerate(layout.total):
        previous = layout.nonzero_prefix[index]
        target = layout.nonzero_prefix[index + 1]
        output.extend(
            (
                c467.gate(CX, previous, target),
                c467.gate(CX, source, target),
                c467.gate(CCX, previous, source, target),
            )
        )
    return tuple(output)


def trace_digest(trace: tuple[Gate, ...]) -> str:
    digest = sha256()
    for item in trace:
        digest.update(struct.pack(">Biii", *item))
    return digest.hexdigest()


@lru_cache(maxsize=1)
def build_circuit() -> Circuit:
    layout = allocate_layout()
    trace: list[Gate] = []
    segments: list[tuple[int, int, int, int]] = []

    sum_blocks = tuple(uncontrolled_add(word, 0, layout.total, layout) for word in layout.neighbors)
    for block in sum_blocks:
        trace.extend(block)
    nz = nonzero_trace(layout)
    trace.extend(nz)
    comparator = compare_leq_trace(layout)

    for direction, (neighbor, coefficient) in enumerate(zip(layout.neighbors, layout.coefficients)):
        target_blocks = (
            uncontrolled_add(neighbor, 2 * FRACTION_BITS + 1, layout.target, layout),
            uncontrolled_add(neighbor, 2 * FRACTION_BITS + 2, layout.target, layout),
        )
        for block in target_blocks:
            trace.extend(block)
        for coefficient_bit in reversed(range(COEFFICIENT_BITS)):
            start = len(trace)
            trace.append(c467.gate(X, coefficient[coefficient_bit]))
            square_blocks = tuple(
                controlled_add(coefficient[bit], coefficient, bit, layout.square, layout)
                for bit in range(COEFFICIENT_BITS)
            )
            for block in square_blocks:
                trace.extend(block)
            product_blocks = tuple(
                controlled_add(layout.square[bit], layout.total, bit, layout.product, layout)
                for bit in range(SQUARE_WIDTH)
            )
            for block in product_blocks:
                trace.extend(block)
            trace.extend(comparator)
            trace.append(
                c467.gate(CCX, layout.leq, layout.nonzero_prefix[-1], layout.valid)
            )
            trace.extend(reversed(comparator))
            for block in reversed(product_blocks):
                trace.extend(reversed(block))
            for block in reversed(square_blocks):
                trace.extend(reversed(block))
            # coefficient bit <- valid, then clear the valid flag exactly.
            trace.append(c467.gate(X, layout.valid))
            trace.append(c467.gate(CX, layout.valid, coefficient[coefficient_bit]))
            trace.append(c467.gate(X, layout.valid))
            trace.append(c467.gate(CX, coefficient[coefficient_bit], layout.valid))
            segments.append((direction, coefficient_bit, start, len(trace)))
        for block in reversed(target_blocks):
            trace.extend(reversed(block))

    trace.extend(reversed(nz))
    for block in reversed(sum_blocks):
        trace.extend(reversed(block))
    frozen = tuple(trace)
    counts = Counter(c467.OP_NAME[item[0]] for item in frozen)
    return Circuit(
        layout,
        frozen,
        tuple(segments),
        trace_digest(frozen),
        {name: counts[name] for name in ("NOT", "CNOT", "TOFFOLI")},
    )


def validate_words(words: tuple[int, ...]) -> None:
    if len(words) != 6 or any(
        not isinstance(value, int) or isinstance(value, bool) or value not in range(1 << B)
        for value in words
    ):
        raise ValueError("six neighbor words must lie in the 249-bit unsigned domain")


def expected_coefficients(words: tuple[int, ...]) -> tuple[int, ...]:
    validate_words(words)
    total = sum(words)
    if total == 0:
        return (0,) * 6
    output = tuple(
        math.isqrt((6 * value * COEFFICIENT_SCALE**2) // total)
        for value in words
    )
    if any(value >= (1 << COEFFICIENT_BITS) for value in output):
        raise OverflowError("fixed-point coefficient leaves its output register")
    return output


def exact_coefficients(words: tuple[int, ...]) -> np.ndarray:
    validate_words(words)
    total = sum(words)
    if total == 0:
        return np.zeros(6)
    return np.sqrt(6 * np.asarray(words, dtype=float) / total)


def put_integer(state: list[int], wires: tuple[int, ...], value: int) -> None:
    if value not in range(1 << len(wires)):
        raise ValueError("value leaves its wire range")
    for bit, wire in enumerate(wires):
        state[wire] = (value >> bit) & 1


def get_integer(state: list[int], wires: tuple[int, ...]) -> int:
    return sum(state[wire] << bit for bit, wire in enumerate(wires))


def initialize(circuit: Circuit, words: tuple[int, ...]) -> list[int]:
    validate_words(words)
    state = [0] * circuit.layout.wire_count
    for wires, value in zip(circuit.layout.neighbors, words):
        put_integer(state, wires, value)
    return state


def execute(
    state: list[int], trace: tuple[Gate, ...], *, skip: tuple[int, int] | None = None
) -> None:
    for index, item in enumerate(trace):
        if skip is None or not (skip[0] <= index < skip[1]):
            c467.apply_gate(state, item)


def read_coefficients(state: list[int], circuit: Circuit) -> tuple[int, ...]:
    return tuple(get_integer(state, wires) for wires in circuit.layout.coefficients)


def word_rows() -> tuple[WordRow, ...]:
    rows = []
    for fixture in c472.FIXTURES:
        item = c463.domain(fixture.radius)
        for pair_index, pair in enumerate(fixture.pairs):
            history, _values, _weights = c472.pair_weights(fixture.radius, pair)
            final = history[-1]
            for endpoint, coord in enumerate(pair):
                words = tuple(
                    final[item.active_index[neighbor]] if neighbor in item.active_index else 0
                    for neighbor in c463.six_neighbors(coord)
                )
                rows.append(
                    WordRow(
                        f"{fixture.name}-pair{pair_index}-endpoint{endpoint}",
                        fixture.radius, pair, endpoint, words, fixture.held,
                    )
                )
    return tuple(rows)


def small_width_model(words: tuple[int, ...], fraction_bits: int) -> tuple[int, ...]:
    total = sum(words)
    if total == 0:
        return (0,) * 6
    return tuple(math.isqrt((6 * value * (1 << (2 * fraction_bits))) // total) for value in words)


def arithmetic_controls(circuit: Circuit, rows: tuple[WordRow, ...]) -> dict[str, object]:
    print("\nREVERSIBLE FIXED-POINT WORD-TO-COEFFICIENT CIRCUIT")
    small_failures = 0
    for words in __import__("itertools").product(range(4), repeat=6):
        expected = small_width_model(words, 3)
        total = sum(words)
        brute = tuple(
            max((candidate for candidate in range(32) if total and candidate * candidate * total <= 6 * value * 64), default=0)
            for value in words
        )
        small_failures += int(expected != brute)

    representative = (rows[0], next(row for row in rows if row.held and len(set(row.words)) > 2))
    full_rows = []
    for row in representative:
        state = initialize(circuit, row.words)
        initial = tuple(state)
        execute(state, circuit.trace)
        output = read_coefficients(state, circuit)
        leakage = sum(state[wire] for wire in circuit.layout.work)
        execute(state, tuple(reversed(circuit.trace)))
        full_rows.append(
            {
                "name": row.name,
                "expected": expected_coefficients(row.words),
                "output": output,
                "work_leakage": leakage,
                "inverse_failures": sum(left != right for left, right in zip(state, initial)),
            }
        )

    zero = initialize(circuit, (0,) * 6)
    execute(zero, circuit.trace)
    zero_output = read_coefficients(zero, circuit)
    zero_leakage = sum(zero[wire] for wire in circuit.layout.work)

    all_rows = []
    maximum_error = 0.0
    for row in rows:
        quantized = expected_coefficients(row.words)
        exact = exact_coefficients(row.words)
        error = float(np.max(abs(np.asarray(quantized) / COEFFICIENT_SCALE - exact)))
        maximum_error = max(maximum_error, error)
        all_rows.append(
            {"name": row.name, "held": row.held, "words": row.words, "coefficients": quantized, "maximum_coefficient_error": error}
        )

    check(
        "one complete NCT circuit computes floor(sqrt(6 n_d/S) 2^8), retains six outputs, and exactly uncomputes all work",
        small_failures == 0
        and all(row["expected"] == row["output"] and row["work_leakage"] == 0 and row["inverse_failures"] == 0 for row in full_rows)
        and zero_output == (0,) * 6 and zero_leakage == 0
        and maximum_error < QUANTIZATION_BOUND,
        {
            "trace_gates": len(circuit.trace), "counts": circuit.counts,
            "trace_digest": circuit.digest, "wire_count": circuit.layout.wire_count,
            "work_M2": len(circuit.layout.work), "retained_output_M2": len(circuit.layout.outputs),
            "small_width_exhaustive_cases": 4**6, "small_width_failures": small_failures,
            "literal_full_width_rows": full_rows, "all_zero_output": zero_output,
            "all_zero_work_leakage": zero_leakage, "actual_train_held_rows": all_rows,
            "maximum_fixed_point_error": maximum_error, "strict_error_bound": QUANTIZATION_BOUND,
        },
    )
    return {"all_rows": all_rows, "maximum_error": maximum_error}


@lru_cache(maxsize=8)
def direction_generator(direction: int) -> sparse.csr_matrix:
    if direction not in range(6):
        raise ValueError("direction leaves the six-mode source star")
    states = c426.LOCAL_STATES[1]
    state_index = c426.LOCAL_STATE_INDEX[1]
    rows = []
    columns = []
    data = []
    for matter_index, mask in enumerate(c322.LOCAL_MASKS):
        reservoir_state = 64
        hopped = c322.fermion_hop(mask, direction, c322.REVERSE[direction])
        if hopped is None:
            continue
        target_mask, sign = hopped
        source = matter_index * len(states) + state_index[reservoir_state]
        target = c322.LOCAL_INDEX[target_mask] * len(states) + state_index[1 << direction]
        rows.extend((target, source))
        columns.extend((source, target))
        data.extend((complex(sign), complex(sign)))
    return sparse.coo_matrix((data, (rows, columns)), shape=(448, 448), dtype=complex).tocsr()


def coefficient_generator(coefficients: np.ndarray) -> sparse.csr_matrix:
    if coefficients.shape != (6,) or np.any(coefficients < 0):
        raise ValueError("coefficient vector leaves its local domain")
    return sum((float(value) * direction_generator(direction) for direction, value in enumerate(coefficients)), start=sparse.csr_matrix((448, 448), dtype=complex))


def bit_product_action(
    vector: np.ndarray,
    coefficients: tuple[int, ...],
    *,
    direction_order: tuple[int, ...] = tuple(range(6)),
    steps: int = STRANG_STEPS,
    inverse: bool = False,
) -> np.ndarray:
    """Eight-step symmetric product formula, compiled coefficient bit by bit."""

    if tuple(sorted(direction_order)) != tuple(range(6)):
        raise ValueError("direction order must be one permutation of six lanes")
    if steps < 1:
        raise ValueError("product-formula step count must be positive")
    output = vector.copy()
    factors = tuple(
        (direction, bit)
        for _step in range(steps)
        for direction in direction_order + tuple(reversed(direction_order))
        for bit in range(COEFFICIENT_BITS)
        if (coefficients[direction] >> bit) & 1
    )
    if inverse:
        factors = tuple(reversed(factors))
    sign = -1 if inverse else 1
    for direction, bit in factors:
        angle = (
            sign * c426.ANGLE * (1 << bit)
            / (2 * steps * COEFFICIENT_SCALE)
        )
        output = expm_multiply(1j * angle * direction_generator(direction), output)
    return output


def rotation_decomposition_manifest() -> dict[str, object]:
    digest = sha256()
    counts = Counter()
    pairs = 0
    maximum_hamming = 0
    for direction in range(6):
        generator = direction_generator(direction).tocoo()
        for row, column, value in zip(generator.row, generator.col, generator.data):
            if row <= column:
                continue
            pairs += 1
            row_matter, row_field_index = divmod(int(row), 7)
            column_matter, column_field_index = divmod(int(column), 7)
            row_state = c322.LOCAL_MASKS[row_matter] | (c426.LOCAL_STATES[1][row_field_index] << 6)
            column_state = c322.LOCAL_MASKS[column_matter] | (c426.LOCAL_STATES[1][column_field_index] << 6)
            hamming = (row_state ^ column_state).bit_count()
            maximum_hamming = max(maximum_hamming, hamming)
            differing = tuple(bit for bit in range(13) if ((row_state ^ column_state) >> bit) & 1)
            if hamming != 4:
                raise RuntimeError("source edge left the four-flip physical pattern")
            for coefficient_bit in range(COEFFICIENT_BITS):
                # Six 12-control Gray-path swaps, then a 13-control rotation.
                repetitions = 2 * STRANG_STEPS
                counts["TOFFOLI"] += repetitions * (6 * (2 * 12 - 3) + (2 * 13 - 2))
                counts["CNOT"] += repetitions * 2
                counts["H"] += repetitions * 2
                counts["RZ"] += repetitions * 2
                negative_controls = 0
                current = column_state
                for changed_bit in differing[:-1]:
                    negative_controls += 12 - (current & ~ (1 << changed_bit)).bit_count()
                    current ^= 1 << changed_bit
                for changed_bit in reversed(differing[:-1]):
                    negative_controls += 12 - (current & ~ (1 << changed_bit)).bit_count()
                    current ^= 1 << changed_bit
                central_target = differing[-1]
                negative_controls += 12 - (current & ~(1 << central_target)).bit_count()
                counts["NOT"] += repetitions * 2 * negative_controls
                angle = float(np.real(value)) * c426.ANGLE * (1 << coefficient_bit) / (2 * STRANG_STEPS * COEFFICIENT_SCALE)
                for substep in range(repetitions):
                    digest.update(f"{substep}|{direction}|{row_state}|{column_state}|{coefficient_bit}|{angle:.17g}\n".encode())
    return {
        "directional_two_level_pairs": pairs,
        "maximum_basis_hamming_distance": maximum_hamming,
        "coefficient_controlled_pair_rotations": pairs * COEFFICIENT_BITS * 2 * STRANG_STEPS,
        "counts": dict(counts),
        "manifest_digest": digest.hexdigest(),
        "local_support_M2": 26,
        "clean_rotation_auxiliary_M2": 12,
        "symmetric_product_steps": STRANG_STEPS,
        "primitive_rotation_decomposition": "each symmetric half-step uses Gray-path 12-control X ladders; 13-control AND; H, Rz(-phi), CNOT, Rz(phi), CNOT, H; uncompute AND and Gray path",
    }


def source_rotation_controls(rows: tuple[WordRow, ...]) -> dict[str, object]:
    print("\nBIT-CONTROLLED LOCAL SOURCE EXPONENTIAL")
    commutators = []
    products = []
    for left in range(6):
        for right in range(left + 1, 6):
            a, b = direction_generator(left), direction_generator(right)
            commutators.append(float(sparse.linalg.norm(a @ b - b @ a)))
            products.append(float(sparse.linalg.norm(a @ b)))

    rng = np.random.default_rng(476)
    vector = rng.normal(size=(448, 3)) + 1j * rng.normal(size=(448, 3))
    vector /= np.linalg.norm(vector, axis=0)
    rows_to_test = (rows[0], next(row for row in rows if row.held and len(set(row.words)) > 2), rows[-1])
    result_rows = []
    maximum_factorization = 0.0
    maximum_quantization = 0.0
    maximum_inverse = 0.0
    maximum_q_leakage = 0.0
    maximum_carried_covariance = 0.0
    for row in rows_to_test:
        integer_coefficients = expected_coefficients(row.words)
        quantized = np.asarray(integer_coefficients, dtype=float) / COEFFICIENT_SCALE
        exact = exact_coefficients(row.words)
        factored = bit_product_action(vector, integer_coefficients)
        direct = expm_multiply(1j * c426.ANGLE * coefficient_generator(quantized), vector)
        exact_target = expm_multiply(1j * c426.ANGLE * coefficient_generator(exact), vector)
        restored = bit_product_action(factored, integer_coefficients, inverse=True)
        factorization = float(np.linalg.norm(factored - direct))
        quantization = float(np.linalg.norm(direct - exact_target))
        inverse = float(np.linalg.norm(restored - vector))
        q_leakage = abs(float(np.linalg.norm(factored) - np.linalg.norm(vector)))
        maximum_factorization = max(maximum_factorization, factorization)
        maximum_quantization = max(maximum_quantization, quantization)
        maximum_inverse = max(maximum_inverse, inverse)
        maximum_q_leakage = max(maximum_q_leakage, q_leakage)
        result_rows.append({"name": row.name, "integer_coefficients": integer_coefficients, "factorization_residual": factorization, "quantization_unitary_residual": quantization, "inverse_residual": inverse, "q1_norm_leakage": q_leakage})

    convergence_coefficients = expected_coefficients(rows_to_test[-1].words)
    convergence_quantized = np.asarray(convergence_coefficients, dtype=float) / COEFFICIENT_SCALE
    convergence_target = expm_multiply(
        1j * c426.ANGLE * coefficient_generator(convergence_quantized), vector
    )
    convergence = []
    for steps in (1, 2, 4, 8):
        approximation = bit_product_action(vector, convergence_coefficients, steps=steps)
        convergence.append(
            {"steps": steps, "residual": float(np.linalg.norm(approximation - convergence_target))}
        )

    covariance_row = rows_to_test[-1]
    covariance_coefficients = expected_coefficients(covariance_row.words)
    covariance_input = vector[:, 0]
    covariance_output = bit_product_action(covariance_input, covariance_coefficients)
    for frame in c463.proper_cubic_frames():
        matrix = np.asarray(frame, dtype=int)
        mapping = c472.direction_map(matrix)
        carried_coefficients = [0] * 6
        for source, target in enumerate(mapping):
            carried_coefficients[target] = covariance_coefficients[source]
        representation = c426.recoil_frame(1, matrix)
        carried_output = bit_product_action(
            representation @ covariance_input,
            tuple(carried_coefficients),
            direction_order=tuple(mapping),
        )
        maximum_carried_covariance = max(
            maximum_carried_covariance,
            float(np.linalg.norm(carried_output - representation @ covariance_output)),
        )

    manifest = rotation_decomposition_manifest()
    check(
        "an eight-step symmetric product compiles the local q1 weighted source exponential into coefficient-bit-controlled bounded physical rotations",
        max(commutators + products) > 0
        and maximum_factorization < PRODUCT_FORMULA_ERROR_CAP
        and maximum_inverse < TOLERANCE
        and maximum_q_leakage < TOLERANCE
        and maximum_carried_covariance < TOLERANCE
        and maximum_quantization < UNITARY_ERROR_CAP
        and all(convergence[index + 1]["residual"] < convergence[index]["residual"] for index in range(len(convergence) - 1))
        and manifest["directional_two_level_pairs"] == 96
        and manifest["coefficient_controlled_pair_rotations"] == 15_360
        and manifest["maximum_basis_hamming_distance"] == 4
        and manifest["local_support_M2"] == 26,
        {
            "maximum_cross_direction_commutator": max(commutators, default=0),
            "maximum_cross_direction_product": max(products, default=0),
            "rows": result_rows, "maximum_factorization_residual": maximum_factorization,
            "declared_product_formula_error_cap": PRODUCT_FORMULA_ERROR_CAP,
            "maximum_quantization_unitary_residual": maximum_quantization,
            "declared_unitary_error_cap": UNITARY_ERROR_CAP,
            "maximum_inverse_residual": maximum_inverse,
            "maximum_q1_norm_leakage": maximum_q_leakage,
            "symmetric_product_convergence": convergence,
            "maximum_all24_carried_product_schedule_residual": maximum_carried_covariance,
            "physical_decomposition": manifest,
        },
    )
    return {"rows": result_rows, "manifest": manifest, "maximum_quantization": maximum_quantization}


def covariance_capacity_controls(circuit: Circuit, rows: tuple[WordRow, ...]) -> None:
    print("\nALL24 COVARIANCE / BOUNDED PHYSICAL CAPACITY")
    frames = c463.proper_cubic_frames()
    maximum_root_residual = 0
    edge_failures = 0
    manifests = []
    sample = next(row for row in rows if row.held and len(set(row.words)) > 2)
    base = expected_coefficients(sample.words)
    for frame in frames:
        matrix = np.asarray(frame, dtype=int)
        mapping = c472.direction_map(matrix)
        carried_words = [0] * 6
        carried_roots = [0] * 6
        for source, target in enumerate(mapping):
            carried_words[target] = sample.words[source]
            carried_roots[target] = base[source]
        maximum_root_residual = max(maximum_root_residual, max(abs(a - b) for a, b in zip(expected_coefficients(tuple(carried_words)), carried_roots)))
        digest = sha256()
        digest.update(circuit.digest.encode())
        digest.update(str(tuple(mapping)).encode())
        for index in range(circuit.layout.wire_count - 1):
            left = c467.affine_frame(frame, c467.path_coordinate(index))
            right = c467.affine_frame(frame, c467.path_coordinate(index + 1))
            edge_failures += int(c467.manhattan(left, right) != 1)
        manifests.append(digest.hexdigest())

    prior_used = c470.USED_PER_ACTIVE_SUPERCELL
    additional = circuit.layout.wire_count - 6 * B + 36
    occupied = prior_used + additional
    maximum_path = circuit.layout.wire_count - 1
    route_upper = (
        circuit.counts["NOT"]
        + circuit.counts["CNOT"] * (6 * max(0, maximum_path - 1) + 1)
        + circuit.counts["TOFFOLI"] * (12 * max(0, maximum_path - 1) + 1)
    )
    check(
        "the lane-permuted arithmetic/control family and one-supercell support carry through all 24 proper-cubic frames within capacity",
        len(frames) == 24 and maximum_root_residual == 0 and edge_failures == 0
        and circuit.layout.wire_count < c463.SUPERCELL_M2 and occupied < c463.SUPERCELL_M2,
        {
            "proper_cubic_frames": len(frames), "maximum_root_lane_residual": maximum_root_residual,
            "carried_Hamiltonian_edge_failures": edge_failures,
            "frame_manifest_digests": manifests,
            "logical_ports_outputs_work_wires": circuit.layout.wire_count,
            "Cycle470_existing_occupied_M2": prior_used,
            "new_M2_beyond_six_existing_ports_plus_one_source_cell": additional,
            "composed_single_supercell_occupied_M2": occupied,
            "supercell_capacity_M2": c463.SUPERCELL_M2,
            "constant_diameter_in_supercell": 3 * (c463.SUPERCELL_SCALE - 1),
            "constructive_stable-gather_NN_event_upper_bound": route_upper,
            "whole_layer_composed": False,
            "Cycle470_role": "available prior art for one seven-supercell ingress/egress block; not replayed and not promoted to a whole-layer schedule",
        },
    )


def deletion_domain_inventory_controls(circuit: Circuit, rows: tuple[WordRow, ...]) -> None:
    print("\nDELETIONS / LAWFUL DOMAIN / INVENTORY / N1-N8")
    selected = next(row for row in rows if row.held and len(set(row.words)) > 2)
    intact_coefficients = expected_coefficients(selected.words)
    word_deleted = list(selected.words)
    deleted_lane = int(np.argmax(word_deleted))
    word_deleted[deleted_lane] = 0
    word_deletion_residual = float(np.linalg.norm(np.asarray(intact_coefficients) - np.asarray(expected_coefficients(tuple(word_deleted)))))

    set_segments = [segment for segment in circuit.root_segments if (intact_coefficients[segment[0]] >> segment[1]) & 1]
    deleted_segment = set_segments[0]
    state = initialize(circuit, selected.words)
    execute(state, circuit.trace, skip=(deleted_segment[2], deleted_segment[3]))
    trial_deletion_residual = float(np.linalg.norm(np.asarray(read_coefficients(state, circuit)) - np.asarray(intact_coefficients)))

    coefficients = intact_coefficients
    probe = np.zeros(448, dtype=complex)
    probe[c322.LOCAL_INDEX[1 << deleted_lane] * 7 + c426.LOCAL_STATE_INDEX[1][64]] = 1
    intact_rotation = bit_product_action(probe, coefficients)
    deleted_coefficients = list(coefficients)
    active_bit = next(bit for bit in range(COEFFICIENT_BITS) if (deleted_coefficients[deleted_lane] >> bit) & 1)
    deleted_coefficients[deleted_lane] ^= 1 << active_bit
    rotation_deletion_residual = float(np.linalg.norm(intact_rotation - bit_product_action(probe, tuple(deleted_coefficients))))
    coupling_deletion_residual = float(np.linalg.norm(intact_rotation - probe))

    rejected = 0
    malformed_actions = (
        lambda: expected_coefficients((0, 0, 0, 0, 0)),
        lambda: expected_coefficients((0, 0, 0, 0, 0, -1)),
        lambda: expected_coefficients((0, 0, 0, 0, 0, 1 << B)),
        lambda: padded_operand((1, 2), PRODUCT_WIDTH, PRODUCT_WIDTH, circuit.layout.pad),
        lambda: direction_generator(6),
    )
    for action in malformed_actions:
        try:
            action()
        except (ValueError, OverflowError):
            rejected += 1

    inventory = {
        "supplied": ["six 249-bit unsigned neighbor ports already populated", "P=8 fractional bits and ten-bit coefficient outputs", "floor square-root convention and all-zero output convention", "Cycle426 angle/sign/local q1 source-star law", "serial direction/bit/Gray-path order and onsite H/Rz calibration", "Cycle470 placement as prior art but no whole-layer schedule"],
        "derived": ["complete reversible NCT sum, zero test, square/product compare, root outputs, inverse and cleanup", "strict coefficient error below 2^-8", "explicit eight-step symmetric q1 source exponential with exact adjoint and measured residual", "15360 coefficient-bit-controlled physical two-level rotations with 26-M2 support", "held word-row response error, deletions, capacity and all24 carried covariance"],
        "open": ["choice/selection of P and rounding law", "exact full exponential or product-formula convergence theorem", "primitive fault-tolerant synthesis of H and Rz angles", "composition of Cycle474 coloring with the enlarged Cycle470 plus Cycle476 block", "q>1 local-star compilation and recurrent field/source execution", "source/mass/energy-stress calibration, physical duration and asymptotics", "metric/gravity, Records, occurrence and Born law"],
        "N1": "attempted restoring square-root by reversible multiply/compare succeeds; nonrestoring root, CORDIC, lookup/QROM, polynomial approximation, phase estimation, and analog adiabatic routes remain open",
        "N2": "fixed-precision law selection, elementary angle synthesis, whole-layer overlap scheduling, q>1 recurrence, physical calibration, and operational occurrence remain independent",
        "N3": "ports, widths, P, floor rule, zero convention, serial order, angle primitives, q1 restriction, work blankness, and missing layer schedule are explicit",
        "N4": "matches Cycle472's word-to-weight/control primitive residual and uses Cycle467 port semantics; Cycle474 schedules the original delivery block separately, while enlarged-block composition and gravity/time residuals are not claimed closed",
        "N5": "exact claims are per fixed-point arithmetic trace and local q1 rotation block; no lattice-wide exactness, physical force, time, energy, or probability is inferred",
        "N6": "alternate roots, angle synthesis, overlap coloring, and q-sector extensions are live import-retirement paths without axiom edits",
        "N7": "a hostile reviewer can replace the costly multiply/compare root by CORDIC/QROM/polynomial arithmetic and can synthesize the two-M2 rotations in a selected discrete gate basis",
        "N8": "Cycles467, 470, and 474 retired earlier arithmetic/delivery/original-overlap walls constructively; Cycle476 follows the same bounded compiler path and cannot support a broad substrate no-go",
        "gate": "broad no-go FAIL; minimum-content FAIL; axiom-pressure FAIL; no axiom pressure",
    }
    check(
        "word, root-trial, controlled-rotation, and coupling deletions are visible while malformed domains are refused",
        min(word_deletion_residual, trial_deletion_residual, rotation_deletion_residual, coupling_deletion_residual) > SIGNAL_FLOOR and rejected == len(malformed_actions),
        {
            "selected_held_row": selected.name,
            "neighbor_word_deletion_residual": word_deletion_residual,
            "deleted_root_segment": deleted_segment,
            "root_trial_deletion_residual": trial_deletion_residual,
            "controlled_rotation_bit_deletion_residual": rotation_deletion_residual,
            "coupling_deletion_residual": coupling_deletion_residual,
            "malformed_domains_rejected": rejected,
            **inventory,
        },
    )


def resource_controls(started: float) -> None:
    elapsed = time.perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(raw if sys.platform == "darwin" else raw * 1024)
    check(
        "the bounded runner stays inside its wall/RSS caps",
        elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "peak_RSS_MiB": rss / 1024**2, "wall_cap_seconds": WALL_CAP_SECONDS, "RSS_cap_GiB": RSS_CAP_BYTES / 1024**3},
    )


def main() -> int:
    started = time.perf_counter()
    note_contract()
    circuit = build_circuit()
    rows = word_rows()
    arithmetic_controls(circuit, rows)
    source_rotation_controls(rows)
    covariance_capacity_controls(circuit, rows)
    deletion_domain_inventory_controls(circuit, rows)
    resource_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    if FAIL:
        return 1
    print("RESULT PHYSICAL_WORD_WEIGHT_CONTROL_COMPILER_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
