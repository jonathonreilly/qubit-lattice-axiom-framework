#!/usr/bin/env python3
"""Cycle 467: elementary reversible compiler for the Cycle-463 local word law.

The runner enumerates a NOT/CNOT/Toffoli trace for the 249-bit six-input
sum, central D-source addition, exact/floor division by six, target XOR, and
compute-uncompute cleanup.  It also compiles that trace to a nearest-neighbor
Hamiltonian line in one scale-40 M2 supercell.  The finite arithmetic law,
source bit, retained histories, and clock/gravity interpretation remain
supplied.  Authority is none; audit is unset.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
from pathlib import Path
from time import perf_counter
import resource
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_reversible_cubic_relaxation_clock_compiler_cycle463_2026_07_19 as c463


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ELEMENTARY_DIVSIX_NN_COMPILER_CYCLE467_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
DIVISOR = 6
VALUE_BITS = c463.VALUE_BITS
SUM_BITS = VALUE_BITS + 3
DENOMINATOR = c463.DENOMINATOR
SUPERCELL_SCALE = c463.SUPERCELL_SCALE
SUPERCELL_M2 = c463.SUPERCELL_M2
WORK_ALLOWANCE = c463.WORK_BITS
COMPUTATIONAL_WORK = 3 * VALUE_BITS + 15
DECLARED_WORK = COMPUTATIONAL_WORK + 1
WALL_CAP_SECONDS = 240.0
RSS_CAP_MIB = 1536.0

X, CX, CCX = 0, 1, 2
OP_NAME = {X: "NOT", CX: "CNOT", CCX: "TOFFOLI"}
Gate = tuple[int, int, int, int]
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


def normalized(path: Path) -> str:
    value = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        value = value.replace(marker, "")
    return " ".join(value.split())


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset", "cycle 467",
        "249-bit", "762 computational work", "763-m2 allowance",
        "not/cnot/toffoli", "1,191", "all 32",
        "every 14,592", "all 24 proper-cubic frames", "scale-40",
        "iteration count and circuit depth are not time",
        "not energy, stress, lapse, metric, proper time, backreaction, or gravity",
        "n1 — alternative route enumeration", "n8 — cross-cycle echo and claim gate",
        "no axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle467 note freezes the elementary-compiler boundary and N1-N8 gate", not missing, missing)


def gate(op: int, a: int, b: int = -1, c: int = -1) -> Gate:
    return (op, a, b, c)


def inverse_trace(trace: tuple[Gate, ...]) -> tuple[Gate, ...]:
    # NOT, CNOT, and Toffoli are individually self-inverse.
    return tuple(reversed(trace))


def trace_digest(trace: tuple[Gate, ...]) -> str:
    digest = sha256()
    for item in trace:
        digest.update(struct.pack(">Biii", *item))
    return digest.hexdigest()


def trace_counts(trace: tuple[Gate, ...]) -> dict[str, int]:
    counts = Counter(OP_NAME[item[0]] for item in trace)
    return {name: counts[name] for name in ("NOT", "CNOT", "TOFFOLI")}


def asap_depth(trace: tuple[Gate, ...], wires: int) -> int:
    last = [0] * wires
    for op, a, b, c in trace:
        touched = (a,) if op == X else ((a, b) if op == CX else (a, b, c))
        layer = 1 + max(last[index] for index in touched)
        for index in touched:
            last[index] = layer
    return max(last, default=0)


def maj(a: int, b: int, carry: int) -> tuple[Gate, ...]:
    return (gate(CX, a, b), gate(CX, a, carry), gate(CCX, carry, b, a))


def uma(a: int, b: int, carry: int) -> tuple[Gate, ...]:
    return (gate(CCX, carry, b, a), gate(CX, a, carry), gate(CX, carry, b))


def cuccaro_add(addend: tuple[int, ...], accumulator: tuple[int, ...], carry: int) -> tuple[Gate, ...]:
    """Add little-endian addend into accumulator modulo 2**n; restore addend/carry."""
    if len(addend) != len(accumulator) or not addend:
        raise ValueError("adder widths must be equal and positive")
    output: list[Gate] = []
    for index, (a, b) in enumerate(zip(addend, accumulator)):
        output.extend(maj(a, b, carry if index == 0 else addend[index - 1]))
    for index in reversed(range(len(addend))):
        output.extend(uma(addend[index], accumulator[index], carry if index == 0 else addend[index - 1]))
    return tuple(output)


def division_step_permutation() -> tuple[int, ...]:
    """Totalize (remainder, input-bit, blank quotient-bit) -> long division by six."""
    partial: dict[int, int] = {}
    for remainder in range(6):
        for input_bit in (0, 1):
            before = remainder | (input_bit << 3)  # quotient input is zero
            total = 2 * remainder + input_bit
            after = (total % 6) | (input_bit << 3) | ((total // 6) << 4)
            partial[before] = after
    remaining_inputs = [state for state in range(32) if state not in partial]
    remaining_outputs = [state for state in range(32) if state not in partial.values()]
    for before, after in zip(remaining_inputs, remaining_outputs):
        partial[before] = after
    return tuple(partial[state] for state in range(32))


DIVISION_STEP = division_step_permutation()


def positive_mcx(controls: tuple[int, ...], target: int, auxiliaries: tuple[int, int]) -> tuple[Gate, ...]:
    if len(controls) == 0:
        return (gate(X, target),)
    if len(controls) == 1:
        return (gate(CX, controls[0], target),)
    if len(controls) == 2:
        return (gate(CCX, controls[0], controls[1], target),)
    first, second = auxiliaries
    if len(controls) == 3:
        return (
            gate(CCX, controls[0], controls[1], first),
            gate(CCX, first, controls[2], target),
            gate(CCX, controls[0], controls[1], first),
        )
    if len(controls) == 4:
        return (
            gate(CCX, controls[0], controls[1], first),
            gate(CCX, first, controls[2], second),
            gate(CCX, second, controls[3], target),
            gate(CCX, first, controls[2], second),
            gate(CCX, controls[0], controls[1], first),
        )
    raise ValueError("the fixed five-bit synthesizer needs at most four controls")


def adjacent_basis_swap(left: int, right: int, state_wires: tuple[int, ...],
                        auxiliaries: tuple[int, int]) -> tuple[Gate, ...]:
    difference = left ^ right
    if difference == 0 or difference & (difference - 1):
        raise ValueError("basis states must differ in exactly one bit")
    target_bit = difference.bit_length() - 1
    target = state_wires[target_bit]
    controls = tuple(state_wires[index] for index in range(len(state_wires)) if index != target_bit)
    negatives = tuple(
        state_wires[index] for index in range(len(state_wires))
        if index != target_bit and not ((left >> index) & 1)
    )
    output = [gate(X, wire) for wire in negatives]
    output.extend(positive_mcx(controls, target, auxiliaries))
    output.extend(gate(X, wire) for wire in reversed(negatives))
    return tuple(output)


def arbitrary_basis_swap(left: int, right: int, state_wires: tuple[int, ...],
                         auxiliaries: tuple[int, int]) -> tuple[Gate, ...]:
    path = [left]
    cursor = left
    for bit in range(len(state_wires)):
        if ((left ^ right) >> bit) & 1:
            cursor ^= 1 << bit
            path.append(cursor)
    output: list[Gate] = []
    for start, end in zip(path, path[1:]):
        output.extend(adjacent_basis_swap(start, end, state_wires, auxiliaries))
    for index in reversed(range(len(path) - 2)):
        output.extend(adjacent_basis_swap(path[index], path[index + 1], state_wires, auxiliaries))
    return tuple(output)


def synthesize_permutation(permutation: tuple[int, ...], state_wires: tuple[int, ...],
                           auxiliaries: tuple[int, int]) -> tuple[Gate, ...]:
    if sorted(permutation) != list(range(len(permutation))) or len(permutation) != 1 << len(state_wires):
        raise ValueError("not a permutation of the declared basis")
    seen: set[int] = set()
    output: list[Gate] = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        cycle = []
        cursor = start
        while cursor not in seen:
            seen.add(cursor)
            cycle.append(cursor)
            cursor = permutation[cursor]
        for endpoint in cycle[1:]:
            output.extend(arbitrary_basis_swap(cycle[0], endpoint, state_wires, auxiliaries))
    return tuple(output)


@dataclass(frozen=True)
class Layout:
    bits: int
    denominator: int
    width: int
    neighbor: tuple[tuple[int, ...], ...]
    source_mask: tuple[int, ...]
    pad: tuple[int, ...]
    accumulator: tuple[int, ...]
    quotient: tuple[int, ...]
    target: tuple[int, ...]
    remainder: tuple[int, ...]
    auxiliary: tuple[int, ...]
    carry: int
    source: int
    spare: int
    cells: tuple[tuple[int, ...], ...]
    wire_count: int

    @property
    def work(self) -> tuple[int, ...]:
        return (
            self.source_mask + self.pad + self.accumulator + self.quotient
            + self.remainder + self.auxiliary + (self.carry, self.spare)
        )


def make_layout(bits: int, denominator: int) -> Layout:
    if bits < 1 or denominator not in range(1 << bits):
        raise ValueError("denominator must fit the declared value word")
    width = bits + 3
    neighbor_lists = [[] for _ in range(6)]
    source_mask: list[int] = []
    pad: list[int] = []
    accumulator: list[int] = []
    quotient: list[int] = []
    target: list[int] = []
    cells: list[tuple[int, ...]] = []
    cursor = 1  # position zero is the Cuccaro carry bit
    carry = 0
    for bit in range(bits):
        cell = []
        for lane in range(6):
            neighbor_lists[lane].append(cursor)
            cell.append(cursor)
            cursor += 1
        source_mask.append(cursor); cell.append(cursor); cursor += 1
        accumulator.append(cursor); cell.append(cursor); cursor += 1
        quotient.append(cursor); cell.append(cursor); cursor += 1
        target.append(cursor); cell.append(cursor); cursor += 1
        cells.append(tuple(cell))
    for _ in range(3):
        pad.append(cursor); cell = [cursor]; cursor += 1
        accumulator.append(cursor); cell.append(cursor); cursor += 1
        quotient.append(cursor); cell.append(cursor); cursor += 1
        cells.append(tuple(cell))
    remainder = tuple(range(cursor, cursor + 3)); cursor += 3
    auxiliary = tuple(range(cursor, cursor + 2)); cursor += 2
    source = cursor; cursor += 1
    spare = cursor; cursor += 1
    return Layout(
        bits, denominator, width, tuple(tuple(row) for row in neighbor_lists),
        tuple(source_mask), tuple(pad), tuple(accumulator), tuple(quotient),
        tuple(target), remainder, auxiliary, carry, source, spare,
        tuple(cells), cursor,
    )


@dataclass(frozen=True)
class Circuit:
    layout: Layout
    compute: tuple[Gate, ...]
    division_steps: tuple[tuple[Gate, ...], ...]
    copies: tuple[tuple[Gate, ...], ...]
    division_cleanup: tuple[tuple[Gate, ...], ...]
    cleanup: tuple[Gate, ...]
    trace: tuple[Gate, ...]


def make_circuit(bits: int, denominator: int) -> Circuit:
    layout = make_layout(bits, denominator)
    high = layout.pad
    addends = tuple(row + high for row in layout.neighbor) + (layout.source_mask + high,)
    load = tuple(
        gate(CX, layout.source, layout.source_mask[index])
        for index in range(bits) if (denominator >> index) & 1
    )
    adders = tuple(cuccaro_add(addend, layout.accumulator, layout.carry) for addend in addends)
    compute = load + tuple(item for adder in adders for item in adder) + load
    steps = []
    copies = []
    for bit in reversed(range(layout.width)):
        state_wires = layout.remainder + (layout.accumulator[bit], layout.quotient[bit])
        steps.append(synthesize_permutation(DIVISION_STEP, state_wires, layout.auxiliary))
        copies.append((gate(CX, layout.quotient[bit], layout.target[bit]),) if bit < bits else ())
    division_cleanup = tuple(inverse_trace(step) for step in reversed(steps))
    cleanup = load + tuple(
        item for adder in reversed(adders) for item in inverse_trace(adder)
    ) + load
    full = (
        compute
        + tuple(item for step, copy in zip(steps, copies) for item in step + copy)
        + tuple(item for step in division_cleanup for item in step)
        + cleanup
    )
    return Circuit(layout, compute, tuple(steps), tuple(copies), division_cleanup, cleanup, full)


def apply_gate(bits: list[int], item: Gate) -> None:
    op, a, b, c = item
    if op == X:
        bits[a] ^= 1
    elif op == CX:
        bits[b] ^= bits[a]
    else:
        bits[c] ^= bits[a] & bits[b]


def apply_trace(bits: list[int], trace: tuple[Gate, ...]) -> None:
    for item in trace:
        apply_gate(bits, item)


def apply_trace_bitset(bits: list[int], trace: tuple[Gate, ...], mask: int) -> None:
    for op, a, b, c in trace:
        if op == X:
            bits[a] ^= mask
        elif op == CX:
            bits[b] ^= bits[a]
        else:
            bits[c] ^= bits[a] & bits[b]


def put_integer(state: list[int], wires: tuple[int, ...], value: int) -> None:
    for bit, wire in enumerate(wires):
        state[wire] = (value >> bit) & 1


def get_integer(state: list[int], wires: tuple[int, ...]) -> int:
    return sum(state[wire] << bit for bit, wire in enumerate(wires))


def initialize(layout: Layout, neighbors: tuple[int, ...], source: int, target: int = 0) -> list[int]:
    if len(neighbors) != 6 or source not in (0, 1):
        raise ValueError("malformed local input")
    state = [0] * layout.wire_count
    for wires, value in zip(layout.neighbor, neighbors):
        put_integer(state, wires, value)
    put_integer(state, layout.target, target)
    state[layout.source] = source
    return state


def compiled_division(numerator: int, width: int) -> tuple[int, int]:
    remainder = 0
    quotient = 0
    for bit in reversed(range(width)):
        before = remainder | (((numerator >> bit) & 1) << 3)
        after = DIVISION_STEP[before]
        if ((after >> 3) & 1) != ((numerator >> bit) & 1):
            raise AssertionError("division totalization failed to retain its input bit")
        remainder = after & 7
        quotient |= ((after >> 4) & 1) << bit
    return quotient, remainder


def division_totalization_controls() -> tuple[Gate, ...]:
    local_state = tuple(range(5))
    local_aux = (5, 6)
    trace = synthesize_permutation(DIVISION_STEP, local_state, local_aux)
    failures = 0
    aux_failures = 0
    for before in range(32):
        state = [((before >> bit) & 1) if bit < 5 else 0 for bit in range(7)]
        apply_trace(state, trace)
        after = sum(state[bit] << bit for bit in range(5))
        failures += int(after != DIVISION_STEP[before])
        aux_failures += int(any(state[5:]))
    check(
        "the fixed five-bit divide-by-six step is a complete 32-state permutation with clean synthesis auxiliaries",
        sorted(DIVISION_STEP) == list(range(32)) and failures == 0 and aux_failures == 0
        and len(trace) == 1191 and trace_counts(trace) == {"NOT": 656, "CNOT": 0, "TOFFOLI": 535},
        {"permutation": DIVISION_STEP, "gates": len(trace), "counts": trace_counts(trace),
         "basis_failures": failures, "aux_reset_failures": aux_failures, "digest": trace_digest(trace)},
    )
    return trace


def exhaustive_small_width_controls() -> None:
    rows = []
    for width in (1, 2):
        denominator = (1 << width) - 1
        circuit = make_circuit(width, denominator)
        cases = tuple(product(range(1 << width), repeat=6))
        inputs = tuple((values, source, target) for values in cases for source in (0, 1) for target in range(1 << width))
        table = [0] * circuit.layout.wire_count
        for case_index, (values, source, target) in enumerate(inputs):
            marker = 1 << case_index
            for wires, value in zip(circuit.layout.neighbor, values):
                for bit, wire in enumerate(wires):
                    if (value >> bit) & 1:
                        table[wire] |= marker
            for bit, wire in enumerate(circuit.layout.target):
                if (target >> bit) & 1:
                    table[wire] |= marker
            if source:
                table[circuit.layout.source] |= marker
        initial = tuple(table)
        mask = (1 << len(inputs)) - 1
        apply_trace_bitset(table, circuit.compute, mask)
        for step, copy in zip(circuit.division_steps, circuit.copies):
            apply_trace_bitset(table, step + copy, mask)
        forward_failures = 0
        remainder_histogram = Counter()
        for case_index, (values, source, target) in enumerate(inputs):
            numerator = sum(values) + denominator * source
            expected_q, expected_r = divmod(numerator, 6)
            observed_acc = sum(((table[wire] >> case_index) & 1) << bit for bit, wire in enumerate(circuit.layout.accumulator))
            observed_q = sum(((table[wire] >> case_index) & 1) << bit for bit, wire in enumerate(circuit.layout.quotient))
            observed_r = sum(((table[wire] >> case_index) & 1) << bit for bit, wire in enumerate(circuit.layout.remainder))
            observed_target = sum(((table[wire] >> case_index) & 1) << bit for bit, wire in enumerate(circuit.layout.target))
            forward_failures += int((observed_acc, observed_q, observed_r, observed_target) != (
                numerator, expected_q, expected_r, target ^ expected_q,
            ))
            remainder_histogram[observed_r] += 1
        for step in circuit.division_cleanup:
            apply_trace_bitset(table, step, mask)
        apply_trace_bitset(table, circuit.cleanup, mask)
        expected_final = list(initial)
        for case_index, (values, source, target) in enumerate(inputs):
            quotient = (sum(values) + denominator * source) // 6
            for bit, wire in enumerate(circuit.layout.target):
                if (quotient >> bit) & 1:
                    expected_final[wire] ^= 1 << case_index
        final_failures = sum(left != right for left, right in zip(table, expected_final))
        work_leakage = sum(table[wire].bit_count() for wire in circuit.layout.work)
        rows.append({
            "bits": width, "cases": len(inputs), "denominator": denominator,
            "forward_failures": forward_failures, "final_wire_failures": final_failures,
            "work_leakage": work_leakage, "remainder_histogram": dict(sorted(remainder_histogram.items())),
        })
    routed_circuit = make_circuit(1, 1)
    routed = compile_nearest_neighbor(routed_circuit, collect=True)
    assert routed.trace is not None
    routed_cases = tuple((values, source, target)
                         for values in product(range(2), repeat=6)
                         for source in (0, 1) for target in range(2))
    routed_table = [0] * routed_circuit.layout.wire_count
    for case_index, (values, source, target) in enumerate(routed_cases):
        marker = 1 << case_index
        for wires, value in zip(routed_circuit.layout.neighbor, values):
            if value:
                routed_table[wires[0]] |= marker
        if target:
            routed_table[routed_circuit.layout.target[0]] |= marker
        if source:
            routed_table[routed_circuit.layout.source] |= marker
    routed_initial = tuple(routed_table)
    apply_trace_bitset(routed_table, routed.trace, (1 << len(routed_cases)) - 1)
    routed_expected = list(routed_initial)
    for case_index, (values, source, target) in enumerate(routed_cases):
        quotient = (sum(values) + source) // 6
        if quotient:
            routed_expected[routed_circuit.layout.target[0]] ^= 1 << case_index
    routed_failures = sum(left != right for left, right in zip(routed_table, routed_expected))
    routed_work_leakage = sum(routed_table[wire].bit_count() for wire in routed_circuit.layout.work)
    check(
        "the complete totalized compiler is exhaustive at widths one and two, including every input, source bit, target seed, remainder, and cleanup",
        all(not row["forward_failures"] and not row["final_wire_failures"] and not row["work_leakage"] for row in rows)
        and [row["cases"] for row in rows] == [256, 32768]
        and all(set(row["remainder_histogram"]) == set(range(6)) for row in rows)
        and routed_failures == 0 and routed_work_leakage == 0,
        {"logical": rows,
         "literal_nearest_neighbor_width1": {"cases": len(routed_cases), "events": routed.events,
                                               "wire_failures": routed_failures,
                                               "work_leakage": routed_work_leakage,
                                               "mapping_restored": routed.restored_mapping}},
    )


def actual_cycle463_inputs() -> tuple[tuple[int, int, tuple[int, ...], int, int], ...]:
    rows = []
    for radius in (c463.TRAIN_RADIUS, c463.HELD_RADIUS):
        item = c463.domain(radius)
        coarse = c463.coarse_forward(c463.initial_coarse(item), item)
        for operation in c463.schedule(radius):
            previous = coarse.history[operation.layer]
            neighbors = tuple(
                previous[item.active_index[coord]] if coord in item.active_index else 0
                for coord in operation.neighbors
            )
            source = coarse.source[item.active_index[operation.target]]
            expected = coarse.history[operation.layer + 1][item.active_index[operation.target]]
            rows.append((radius, operation.layer, neighbors, source, expected))
    return tuple(rows)


def execute_forward_capture(circuit: Circuit, state: list[int]) -> tuple[int, int, int, int]:
    apply_trace(state, circuit.compute)
    for step, copy in zip(circuit.division_steps, circuit.copies):
        apply_trace(state, step + copy)
    return (
        get_integer(state, circuit.layout.accumulator),
        get_integer(state, circuit.layout.quotient),
        get_integer(state, circuit.layout.remainder),
        get_integer(state, circuit.layout.target),
    )


def execute_cleanup(circuit: Circuit, state: list[int]) -> None:
    for step in circuit.division_cleanup:
        apply_trace(state, step)
    apply_trace(state, circuit.cleanup)


def cycle463_composition_controls(circuit: Circuit) -> None:
    rows = actual_cycle463_inputs()
    digest = sha256()
    failures = 0
    divisibility_failures = 0
    for radius, layer, neighbors, source, expected in rows:
        numerator = sum(neighbors) + DENOMINATOR * source
        quotient, remainder = compiled_division(numerator, SUM_BITS)
        failures += int(quotient != expected)
        divisibility_failures += int(remainder != 0)
        digest.update(f"{radius}|{layer}|{neighbors}|{source}|{quotient}|{remainder}\n".encode())
    representative_indices = (0, 1296, 2591, 2592, 8592, len(rows) - 1)
    literal_failures = 0
    inverse_failures = 0
    literal_rows = []
    for index in representative_indices:
        radius, layer, neighbors, source, expected = rows[index]
        state = initialize(circuit.layout, neighbors, source)
        initial = tuple(state)
        capture = execute_forward_capture(circuit, state)
        numerator = sum(neighbors) + DENOMINATOR * source
        literal_failures += int(capture != (numerator, expected, 0, expected))
        execute_cleanup(circuit, state)
        expected_output = list(initial)
        put_integer(expected_output, circuit.layout.target, expected)
        literal_failures += int(state != expected_output or any(state[wire] for wire in circuit.layout.work))
        apply_trace(state, inverse_trace(circuit.trace))
        inverse_failures += int(state != list(initial))
        literal_rows.append({"index": index, "radius": radius, "layer": layer,
                             "numerator_bits": numerator.bit_length(), "quotient": expected})
    check(
        "every actual Cycle463 train/held local input passes the compiled long-division semantics, with literal full-block E/G and inverse representatives",
        len(rows) == 14_592 and failures == 0 and divisibility_failures == 0
        and literal_failures == 0 and inverse_failures == 0,
        {"actual_rows": len(rows), "train": 2592, "held": 12000,
         "compiled_mismatches": failures, "divisibility_failures": divisibility_failures,
         "literal_representatives": literal_rows, "literal_failures": literal_failures,
         "inverse_failures": inverse_failures, "row_digest": digest.hexdigest(),
         "batch_method": "same fixed 32-state step permutation; elementary synthesis separately exhaustive on all 32 states"},
    )


def invalid_controls(circuit: Circuit) -> None:
    rows = []
    failures = 0
    refusal_failures = 0
    for remainder in range(1, 6):
        neighbors = (remainder, 0, 0, 0, 0, 0)
        state = initialize(circuit.layout, neighbors, 0, target=(1 << VALUE_BITS) - 1)
        initial = tuple(state)
        capture = execute_forward_capture(circuit, state)
        expected_q, expected_r = divmod(remainder, 6)
        failures += int(capture != (remainder, expected_q, expected_r, ((1 << VALUE_BITS) - 1) ^ expected_q))
        execute_cleanup(circuit, state)
        expected = list(initial)
        put_integer(expected, circuit.layout.target, ((1 << VALUE_BITS) - 1) ^ expected_q)
        failures += int(state != expected or any(state[wire] for wire in circuit.layout.work))
        try:
            c463.local_quotient(neighbors, 0, strict=True)
            refusal_failures += 1
        except ValueError:
            pass
        rows.append({"numerator": remainder, "quotient": expected_q, "remainder": expected_r})
    check(
        "seeded nondivisible inputs are totalized reversibly while the Cycle463 lawful decoder still refuses them",
        failures == 0 and refusal_failures == 0 and {row["remainder"] for row in rows} == set(range(1, 6)),
        {"rows": rows, "circuit_failures": failures, "strict_decoder_acceptance_failures": refusal_failures},
    )


def path_coordinate(index: int) -> tuple[int, int, int]:
    if index not in range(SUPERCELL_M2):
        raise ValueError("path index leaves the scale-40 supercell")
    layer, within = divmod(index, SUPERCELL_SCALE * SUPERCELL_SCALE)
    row, column = divmod(within, SUPERCELL_SCALE)
    y = row if layer % 2 == 0 else SUPERCELL_SCALE - 1 - row
    x = column if row % 2 == 0 else SUPERCELL_SCALE - 1 - column
    return (x, y, layer)


def manhattan(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


@dataclass
class RouteResult:
    counts: Counter[str]
    depth: int
    digest: str
    events: int
    swaps: int
    adjacency_failures: int
    restored_mapping: bool
    trace: tuple[Gate, ...] | None


class RouteCompiler:
    """Nearest-neighbor compiler on the first N vertices of a cubic Hamiltonian path."""

    def __init__(self, wires: int, *, collect: bool = False):
        self.wire_at = list(range(wires))
        self.position_of = list(range(wires))
        self.last = [0] * wires
        self.counts: Counter[str] = Counter()
        self.digest = sha256()
        self.events = 0
        self.swaps = 0
        self.adjacency_failures = 0
        self.trace: list[Gate] | None = [] if collect else None

    def emit(self, op: int, positions: tuple[int, ...]) -> None:
        coordinates = tuple(path_coordinate(position) for position in positions)
        if op == CX:
            self.adjacency_failures += int(manhattan(coordinates[0], coordinates[1]) != 1)
        elif op == CCX:
            edges = sorted(manhattan(coordinates[i], coordinates[j]) for i in range(3) for j in range(i + 1, 3))
            self.adjacency_failures += int(edges != [1, 1, 2])
        layer = 1 + max(self.last[position] for position in positions)
        for position in positions:
            self.last[position] = layer
        self.counts[OP_NAME[op]] += 1
        padded = positions + (-1,) * (3 - len(positions))
        self.digest.update(struct.pack(">Biii", op, *padded))
        if self.trace is not None:
            self.trace.append(gate(op, *padded))
        self.events += 1

    def swap(self, left: int, right: int) -> None:
        if abs(left - right) != 1:
            raise ValueError("SWAP endpoints are not adjacent on the physical path")
        self.emit(CX, (left, right)); self.emit(CX, (right, left)); self.emit(CX, (left, right))
        left_wire, right_wire = self.wire_at[left], self.wire_at[right]
        self.wire_at[left], self.wire_at[right] = right_wire, left_wire
        self.position_of[left_wire], self.position_of[right_wire] = right, left
        self.swaps += 1

    def move_wire(self, wire: int, destination: int, swaps: list[tuple[int, int]]) -> None:
        while self.position_of[wire] < destination:
            left = self.position_of[wire]
            self.swap(left, left + 1); swaps.append((left, left + 1))
        while self.position_of[wire] > destination:
            right = self.position_of[wire]
            self.swap(right - 1, right); swaps.append((right - 1, right))

    def routed_gate(self, item: Gate) -> None:
        op, a, b, c = item
        if op == X:
            self.emit(X, (self.position_of[a],))
            return
        if op == CX:
            swaps: list[tuple[int, int]] = []
            target_position = self.position_of[b]
            destination = target_position - 1 if self.position_of[a] < target_position else target_position + 1
            self.move_wire(a, destination, swaps)
            self.emit(CX, (self.position_of[a], self.position_of[b]))
            for left, right in reversed(swaps):
                self.swap(left, right)
            return
        participants = sorted((a, b, c), key=self.position_of.__getitem__)
        p0, p1, p2 = (self.position_of[wire] for wire in participants)
        swaps = []
        self.move_wire(participants[1], p2 - 1, swaps)
        self.move_wire(participants[0], p2 - 2, swaps)
        self.emit(CCX, (self.position_of[a], self.position_of[b], self.position_of[c]))
        for left, right in reversed(swaps):
            self.swap(left, right)

    def routed_trace(self, trace: tuple[Gate, ...]) -> None:
        for item in trace:
            self.routed_gate(item)

    def head_left(self, head: tuple[int, ...], cell: tuple[int, ...]) -> None:
        for offset, wire in enumerate(head):
            destination = min(self.position_of[item] for item in cell) + offset
            swaps: list[tuple[int, int]] = []
            self.move_wire(wire, destination, swaps)

    def head_right(self, head: tuple[int, ...], cell: tuple[int, ...]) -> None:
        for wire in reversed(head):
            destination = max(self.position_of[item] for item in cell)
            swaps: list[tuple[int, int]] = []
            self.move_wire(wire, destination, swaps)

    def finish(self) -> RouteResult:
        return RouteResult(
            self.counts, max(self.last, default=0), self.digest.hexdigest(), self.events,
            self.swaps, self.adjacency_failures,
            self.wire_at == list(range(len(self.wire_at))),
            tuple(self.trace) if self.trace is not None else None,
        )


def compile_nearest_neighbor(circuit: Circuit, *, collect: bool = False) -> RouteResult:
    router = RouteCompiler(circuit.layout.wire_count, collect=collect)
    router.routed_trace(circuit.compute)
    head = circuit.layout.remainder + circuit.layout.auxiliary
    for bit, step, copy in zip(reversed(range(circuit.layout.width)), circuit.division_steps, circuit.copies):
        router.routed_trace(step + copy)
        router.head_left(head, circuit.layout.cells[bit])
    for bit, step in zip(range(circuit.layout.width), circuit.division_cleanup):
        router.routed_trace(step)
        router.head_right(head, circuit.layout.cells[bit])
    router.routed_trace(circuit.cleanup)
    return router.finish()


def affine_frame(frame: c463.Frame, coord: tuple[int, int, int]) -> tuple[int, int, int]:
    output = []
    for row in frame:
        axis = next(index for index, value in enumerate(row) if value)
        output.append(coord[axis] if row[axis] == 1 else SUPERCELL_SCALE - 1 - coord[axis])
    return tuple(output)  # type: ignore[return-value]


def nearest_neighbor_and_covariance_controls(circuit: Circuit) -> RouteResult:
    routed = compile_nearest_neighbor(circuit)
    frames = c463.proper_cubic_frames()
    frame_failures = 0
    manifests = []
    for frame in frames:
        for index in range(circuit.layout.wire_count - 1):
            left = affine_frame(frame, path_coordinate(index))
            right = affine_frame(frame, path_coordinate(index + 1))
            frame_failures += int(manhattan(left, right) != 1)
            frame_failures += int(any(value not in range(SUPERCELL_SCALE) for value in left + right))
        manifest = sha256()
        manifest.update(repr(frame).encode())
        manifest.update(routed.digest.encode())
        manifest.update(str(routed.events).encode())
        manifest.update(b"|affine-image-of-complete-elementary-trace")
        manifests.append(manifest.hexdigest())
    check(
        "the complete gate schedule has a nearest-neighbor scale-40 routing with restored placement",
        circuit.layout.wire_count <= SUPERCELL_M2 and routed.adjacency_failures == 0
        and routed.restored_mapping and sum(routed.counts.values()) == routed.events,
        {"logical_wires_and_ports": circuit.layout.wire_count, "supercell_M2": SUPERCELL_M2,
         "routed_elementary_events": routed.events, "routed_counts": dict(routed.counts),
         "adjacent_SWAPs": routed.swaps, "ASAP_depth": routed.depth,
         "adjacency_failures": routed.adjacency_failures, "mapping_restored": routed.restored_mapping,
         "routed_trace_digest": routed.digest,
         "inverse": "reverse the complete routed event stream; every primitive is self-inverse"},
    )
    check(
        "the entire routed elementary schedule is covariant under all 24 proper-cubic affine frames",
        len(frames) == 24 and frame_failures == 0 and len(set(manifests)) == 24,
        {"frames": len(frames), "carried_path_edge_failures": frame_failures,
         "events_carried_per_frame": routed.events, "frame_manifest_digests": manifests,
         "output_invariance_used_as_gate_covariance_proof": False},
    )
    return routed


def inventory_and_trace_controls(circuit: Circuit, local_step: tuple[Gate, ...]) -> None:
    counts = trace_counts(circuit.trace)
    inverse = inverse_trace(circuit.trace)
    work_breakdown = {
        "accumulator": SUM_BITS, "source_mask": VALUE_BITS, "shared_high_pad": 3,
        "carry": 1, "remainder": 3, "quotient": SUM_BITS,
        "MCX_synthesis_auxiliaries": 2, "computational_total": COMPUTATIONAL_WORK,
        "unused_allowance_bit": 1, "declared_total": DECLARED_WORK,
    }
    check(
        "the literal 249-bit compute/XOR/uncompute trace and its exact inverse are fully enumerated",
        len(circuit.division_steps) == SUM_BITS and all(len(step) == len(local_step) for step in circuit.division_steps)
        and inverse_trace(inverse) == circuit.trace and sum(counts.values()) == len(circuit.trace),
        {"logical_gates": len(circuit.trace), "counts": counts,
         "sequential_depth": len(circuit.trace), "ASAP_depth": asap_depth(circuit.trace, circuit.layout.wire_count),
         "trace_digest": trace_digest(circuit.trace), "inverse_trace_digest": trace_digest(inverse),
         "inverse_rule": "reverse order; NOT/CNOT/Toffoli are self-inverse"},
    )
    check(
        "the Cycle463 763-M2 work allowance suffices without enlargement",
        COMPUTATIONAL_WORK == 762 and DECLARED_WORK == WORK_ALLOWANCE == 763
        and len(circuit.layout.work) == DECLARED_WORK and len(set(circuit.layout.work)) == DECLARED_WORK,
        {"B": VALUE_BITS, "W": SUM_BITS, "work_breakdown": work_breakdown,
         "constant_overhead_per_local_block": True, "enlargement": 0,
         "ports_not_counted_as_work": {"six_retained_neighbor_words": 6 * VALUE_BITS,
                                       "source": 1, "target": VALUE_BITS}},
    )


def boundary_and_no_go_controls() -> None:
    check(
        "the supplied-law, port, source, clock, and gravity boundaries remain explicit",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "supplied": [
                "six retained B-bit neighbor input ports and one local source bit",
                "D=6^96, the six-input plus D*source law, and division by six",
                "249-bit value precision, scale-40 supercell, retained layer schedule",
                "computational-basis word code and blank target/work code constraints",
                "finite train/held domains and blank Dirichlet shells",
            ],
            "constructed": [
                "Cuccaro ripple additions", "total 32-state divide-step permutation",
                "NOT/CNOT/Toffoli synthesis", "compute/XOR/uncompute and inverse",
                "nearest-neighbor Hamiltonian-path routing and all24 carried frames",
            ],
            "not_claimed": [
                "a derivation of the finite law or source scale", "time from circuit depth",
                "energy/stress from a source bit", "lapse, metric, proper time, backreaction, gravity",
                "optimal gate count or a minimum-work theorem", "inter-supercell port transport",
            ],
        },
    )
    check(
        "full N1-N8 rejects no-go, minimum-content, and axiom-pressure promotion",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "N1": "Cuccaro plus totalized long division succeeds; table-lookup, restoring division, carry-save, and Fourier routes remain alternatives",
            "N2": "arithmetic synthesis, inter-supercell port transport, finite law selection, source meaning, clock interpretation, and gravity remain independent",
            "N3": "blank work/target code, supplied D/law/width, computational-basis ports, serial synthesis, and input-port placement are exposed",
            "N4": "the witness exactly matches Cycle463's missing elementary arithmetic trace; it does not match source-law or gravity residuals",
            "N5": "claims stop at this bounded local basis-permutation compiler; no optimum, universal, continuum, or gravity rhetoric",
            "N6": "the primitive-gate boundary closes constructively while law/source/clock/gravity imports remain open",
            "N7": "a reviewer can still reduce depth/work, compile port transport, replace retained history, and derive a dynamical source-response law",
            "N8": "Cycle463's precise missing trace is retired; broader C_source/C_wrap/gravity echoes remain unresolved; no axiom pressure",
        },
    )


def resource_controls(started: float) -> None:
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check(
        "the complete compiler run stays below its explicit wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
         "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB},
    )


def main() -> int:
    started = perf_counter()
    print("Cycle467 physical elementary divide-six nearest-neighbor compiler")
    print("authority", AUTHORITY, "audit", AUDIT)
    note_contract()
    local_step = division_totalization_controls()
    exhaustive_small_width_controls()
    circuit = make_circuit(VALUE_BITS, DENOMINATOR)
    inventory_and_trace_controls(circuit, local_step)
    cycle463_composition_controls(circuit)
    invalid_controls(circuit)
    nearest_neighbor_and_covariance_controls(circuit)
    boundary_and_no_go_controls()
    resource_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
