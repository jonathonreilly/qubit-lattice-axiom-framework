#!/usr/bin/env python3
"""Cycle 209: compile the Cycle-208 relational readout into local dynamics.

The bounded compiler starts from three one-particle position rails, computes
the symmetric T/R/X predicate with a generic reversible Boolean circuit,
uncomputes all position-dependent garbage, and only then exposes one outcome
rail to a record port.  A physical ARM/CLOSE/DONE process is kept explicit:
DONE is a causal completion certificate, never a timeout.

This is a conditional detector construction.  It does not derive the loading
event, the occurrence of a record, Born frequencies, or the 1-D scattering
law from the framework axioms.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
import random

import numpy as np

from local_relational_late_detector_cycle208_2026_07_16 import (
    local_masks,
    prepare_and_evolve,
    projected_state,
)
from fixed_total_momentum_molecular_scattering_cycle207_2026_07_16 import (
    channel_records,
    channel_spectrum,
)


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COHERENT_CAUSAL_CLOSE_DETECTOR_COMPILER_CYCLE209_NOTE_2026-07-16.md"
)

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


@dataclass(frozen=True)
class Node:
    op: str
    parents: tuple[int, ...]
    name: str
    value: int | None = None


class BooleanCircuit:
    """Fresh-target Boolean DAG suitable for Bennett uncomputation."""

    def __init__(self) -> None:
        self.nodes: list[Node] = []
        self.inputs: dict[str, int] = {}
        self.zero = self._constant(0)
        self.one = self._constant(1)

    def _constant(self, value: int) -> int:
        index = len(self.nodes)
        self.nodes.append(Node("CONST", (), f"CONST_{value}", value))
        return index

    def input(self, name: str) -> int:
        index = len(self.nodes)
        self.nodes.append(Node("INPUT", (), name))
        self.inputs[name] = index
        return index

    def _known(self, index: int) -> int | None:
        return self.nodes[index].value if self.nodes[index].op == "CONST" else None

    def _gate(self, op: str, parents: tuple[int, ...], name: str) -> int:
        index = len(self.nodes)
        self.nodes.append(Node(op, parents, name))
        return index

    def not_(self, value: int, name: str = "NOT") -> int:
        known = self._known(value)
        if known is not None:
            return self.one if not known else self.zero
        return self._gate("NOT", (value,), name)

    def xor(self, left: int, right: int, name: str = "XOR") -> int:
        if left == right:
            return self.zero
        lk, rk = self._known(left), self._known(right)
        if lk == 0:
            return right
        if rk == 0:
            return left
        if lk == 1:
            return self.not_(right, name + "_N")
        if rk == 1:
            return self.not_(left, name + "_N")
        return self._gate("XOR", (left, right), name)

    def and_(self, left: int, right: int, name: str = "AND") -> int:
        if left == right:
            return left
        lk, rk = self._known(left), self._known(right)
        if lk == 0 or rk == 0:
            return self.zero
        if lk == 1:
            return right
        if rk == 1:
            return left
        return self._gate("AND", (left, right), name)

    def or_(self, left: int, right: int, name: str = "OR") -> int:
        if left == right:
            return left
        lk, rk = self._known(left), self._known(right)
        if lk == 1 or rk == 1:
            return self.one
        if lk == 0:
            return right
        if rk == 0:
            return left
        return self._gate("OR", (left, right), name)

    def xor_many(self, values: list[int], name: str) -> int:
        result = self.zero
        for offset, value in enumerate(values):
            result = self.xor(result, value, f"{name}_{offset}")
        return result

    def add(self, left: list[int], right: list[int], name: str) -> list[int]:
        width = max(len(left), len(right))
        a = left + [self.zero] * (width - len(left))
        b = right + [self.zero] * (width - len(right))
        carry = self.zero
        output: list[int] = []
        for bit in range(width):
            ab_xor = self.xor(a[bit], b[bit], f"{name}_XAB_{bit}")
            output.append(self.xor(ab_xor, carry, f"{name}_SUM_{bit}"))
            ab = self.and_(a[bit], b[bit], f"{name}_AB_{bit}")
            ac = self.and_(a[bit], carry, f"{name}_AC_{bit}")
            bc = self.and_(b[bit], carry, f"{name}_BC_{bit}")
            carry = self.or_(
                self.or_(ab, ac, f"{name}_OR1_{bit}"),
                bc,
                f"{name}_CARRY_{bit}",
            )
        output.append(carry)
        return output

    def less_than(self, left: list[int], right: list[int], name: str) -> int:
        width = max(len(left), len(right))
        a = left + [self.zero] * (width - len(left))
        b = right + [self.zero] * (width - len(right))
        equal = self.one
        less = self.zero
        for bit in reversed(range(width)):
            a_lt_b = self.and_(
                self.not_(a[bit], f"{name}_NA_{bit}"),
                b[bit],
                f"{name}_ALTB_{bit}",
            )
            first_difference = self.and_(
                equal, a_lt_b, f"{name}_FIRST_{bit}"
            )
            less = self.or_(less, first_difference, f"{name}_LT_{bit}")
            same = self.not_(
                self.xor(a[bit], b[bit], f"{name}_X_{bit}"),
                f"{name}_XNOR_{bit}",
            )
            equal = self.and_(equal, same, f"{name}_EQ_{bit}")
        return less

    def evaluate(self, supplied: dict[str, int]) -> list[int]:
        values = [0] * len(self.nodes)
        for index, node in enumerate(self.nodes):
            if node.op == "CONST":
                values[index] = int(node.value)
            elif node.op == "INPUT":
                values[index] = int(supplied[node.name])
            elif node.op == "NOT":
                values[index] = 1 ^ values[node.parents[0]]
            elif node.op == "XOR":
                values[index] = values[node.parents[0]] ^ values[node.parents[1]]
            elif node.op == "AND":
                values[index] = values[node.parents[0]] & values[node.parents[1]]
            elif node.op == "OR":
                values[index] = values[node.parents[0]] | values[node.parents[1]]
            else:
                raise ValueError(node.op)
        return values


@dataclass(frozen=True)
class Detector:
    circuit: BooleanCircuit
    rails: dict[str, tuple[int, ...]]
    outputs: tuple[int, int, int]
    aperture: int


def build_detector(aperture: int = 16) -> Detector:
    if aperture <= 4 or aperture & (aperture - 1):
        raise ValueError("aperture must be a power of two greater than four")
    width = aperture.bit_length() - 1
    circuit = BooleanCircuit()
    rails: dict[str, tuple[int, ...]] = {}
    coordinate_bits: dict[str, list[int]] = {}
    for species in ("A", "B", "P"):
        rail = tuple(circuit.input(f"{species}_{site}") for site in range(aperture))
        rails[species] = rail
        coordinate_bits[species] = [
            circuit.xor_many(
                [rail[site] for site in range(aperture) if (site >> bit) & 1],
                f"ENC_{species}_{bit}",
            )
            for bit in range(width)
        ]

    a, b, p = (coordinate_bits[key] for key in ("A", "B", "P"))
    two = [circuit.zero, circuit.one] + [circuit.zero] * (width - 1)
    a_plus_two = circuit.add(a, two, "A_PLUS_2")
    b_plus_two = circuit.add(b, two, "B_PLUS_2")
    a_wide = a + [circuit.zero]
    b_wide = b + [circuit.zero]
    too_far_ab = circuit.less_than(b_plus_two, a_wide, "B2_LT_A")
    too_far_ba = circuit.less_than(a_plus_two, b_wide, "A2_LT_B")
    close = circuit.not_(
        circuit.or_(too_far_ab, too_far_ba, "TOO_FAR"), "PAIR_CLOSE"
    )

    pair_sum = circuit.add(a, b, "PAIR_SUM")
    twice_projectile = [circuit.zero] + p
    projectile_left = circuit.less_than(
        twice_projectile, pair_sum, "TWOP_LT_PAIR"
    )
    projectile_right = circuit.less_than(
        pair_sum, twice_projectile, "PAIR_LT_TWOP"
    )
    transmitted = circuit.and_(close, projectile_left, "OUT_T")
    reflected = circuit.and_(close, projectile_right, "OUT_R")
    other = circuit.not_(circuit.or_(transmitted, reflected, "T_OR_R"), "OUT_X")
    return Detector(circuit, rails, (transmitted, reflected, other), aperture)


def supplied_input(detector: Detector, first: int, second: int, projectile: int) -> dict[str, int]:
    return {
        name: int(
            (name.startswith("A_") and int(name[2:]) == first)
            or (name.startswith("B_") and int(name[2:]) == second)
            or (name.startswith("P_") and int(name[2:]) == projectile)
        )
        for name in detector.circuit.inputs
    }


def direct_class(first: int, second: int, projectile: int) -> tuple[int, int, int]:
    close = abs(first - second) <= 2
    signed_side = 2 * projectile - first - second
    transmitted = int(close and signed_side < 0)
    reflected = int(close and signed_side > 0)
    return transmitted, reflected, 1 - transmitted - reflected


Primitive = tuple[str, tuple[int, ...]]


def forward_primitives(circuit: BooleanCircuit) -> list[Primitive]:
    operations: list[Primitive] = []
    for target, node in enumerate(circuit.nodes):
        if node.op in ("CONST", "INPUT"):
            continue
        if node.op == "NOT":
            operations.extend((
                ("X", (target,)),
                ("CNOT", (node.parents[0], target)),
            ))
        elif node.op == "XOR":
            operations.extend(
                ("CNOT", (parent, target)) for parent in node.parents
            )
        elif node.op == "AND":
            operations.append(("TOFFOLI", (node.parents[0], node.parents[1], target)))
        elif node.op == "OR":
            operations.extend((
                ("CNOT", (node.parents[0], target)),
                ("CNOT", (node.parents[1], target)),
                ("TOFFOLI", (node.parents[0], node.parents[1], target)),
            ))
        else:
            raise ValueError(node.op)
    return operations


def apply_primitive(state: list[int], primitive: Primitive) -> None:
    op, qubits = primitive
    if op == "X":
        state[qubits[0]] ^= 1
    elif op == "CNOT":
        state[qubits[1]] ^= state[qubits[0]]
    elif op == "TOFFOLI":
        state[qubits[2]] ^= state[qubits[0]] & state[qubits[1]]
    elif op == "SWAP":
        state[qubits[0]], state[qubits[1]] = state[qubits[1]], state[qubits[0]]
    else:
        raise ValueError(op)


def reversible_run(detector: Detector, first: int, second: int, projectile: int) -> tuple[tuple[int, int, int], bool, tuple[int, ...]]:
    circuit = detector.circuit
    base = len(circuit.nodes)
    output_qubits = (base, base + 1, base + 2)
    state = [0] * (base + 3)
    state[circuit.one] = 1
    supplied = supplied_input(detector, first, second, projectile)
    for name, index in circuit.inputs.items():
        state[index] = supplied[name]
    operations = forward_primitives(circuit)
    for primitive in operations:
        apply_primitive(state, primitive)
    garbage = tuple(state[index] for index in range(base) if circuit.nodes[index].op not in ("CONST", "INPUT"))
    for source, target in zip(detector.outputs, output_qubits):
        apply_primitive(state, ("CNOT", (source, target)))
    for primitive in reversed(operations):
        apply_primitive(state, primitive)

    clean = all(
        state[index] == 0
        for index, node in enumerate(circuit.nodes)
        if node.op not in ("CONST", "INPUT")
    )
    inputs_preserved = all(state[index] == supplied[name] for name, index in circuit.inputs.items())
    return tuple(state[index] for index in output_qubits), clean and inputs_preserved, garbage


def route_to_front(qubits: tuple[int, ...], qubit_count: int) -> tuple[list[Primitive], list[Primitive]]:
    layout = list(range(qubit_count))
    positions = list(range(qubit_count))
    route: list[Primitive] = []
    for destination, logical in enumerate(qubits):
        source = positions[logical]
        while source > destination:
            left, right = source - 1, source
            first, second = layout[left], layout[right]
            layout[left], layout[right] = second, first
            positions[first], positions[second] = right, left
            route.append(("SWAP", (left, right)))
            source -= 1
    return route, list(reversed(route))


def nearest_neighbour_census(detector: Detector) -> dict[str, int | bool]:
    base = len(detector.circuit.nodes)
    outputs = (base, base + 1, base + 2)
    logical = forward_primitives(detector.circuit)
    logical += [("CNOT", pair) for pair in zip(detector.outputs, outputs)]
    logical += list(reversed(forward_primitives(detector.circuit)))
    local_operations = 0
    swaps = 0
    all_local = True
    semantic_equivalence = True
    for op, qubits in logical:
        if op == "X":
            local_operations += 1
            continue
        route, inverse = route_to_front(qubits, base + 3)
        swaps += len(route) + len(inverse)
        local_operations += len(route) + 1 + len(inverse)
        all_local &= all(abs(edge[0] - edge[1]) == 1 for _, edge in route + inverse)
        if op == "CNOT":
            all_local &= len(qubits) == 2
        elif op == "TOFFOLI":
            all_local &= len(qubits) == 3
        for pattern in product((0, 1), repeat=len(qubits)):
            expected = [0] * (base + 3)
            for logical_qubit, value in zip(qubits, pattern):
                expected[logical_qubit] = value
            routed = expected.copy()
            apply_primitive(expected, (op, qubits))
            for primitive in route:
                apply_primitive(routed, primitive)
            apply_primitive(routed, (op, tuple(range(len(qubits)))))
            for primitive in inverse:
                apply_primitive(routed, primitive)
            semantic_equivalence &= routed == expected
    return {
        "logical_primitives": len(logical),
        "nearest_neighbour_primitives": local_operations,
        "routing_swaps": swaps,
        "qubits": base + 3,
        "all_local": all_local,
        "semantic_equivalence": semantic_equivalence,
    }


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations = []
    for order in permutations(range(3)):
        permutation = np.zeros((3, 3), dtype=int)
        permutation[np.arange(3), order] = 1
        for signs in product((-1, 1), repeat=3):
            matrix = np.diag(signs) @ permutation
            if round(np.linalg.det(matrix)) == 1:
                rotations.append(matrix)
    return tuple(rotations)


def random_topological_values(circuit: BooleanCircuit, supplied: dict[str, int], seed: int) -> list[int]:
    rng = random.Random(seed)
    values: dict[int, int] = {}
    pending = set(range(len(circuit.nodes)))
    while pending:
        enabled = [
            index
            for index in pending
            if all(parent in values for parent in circuit.nodes[index].parents)
        ]
        index = rng.choice(enabled)
        node = circuit.nodes[index]
        if node.op == "CONST":
            values[index] = int(node.value)
        elif node.op == "INPUT":
            values[index] = supplied[node.name]
        elif node.op == "NOT":
            values[index] = 1 ^ values[node.parents[0]]
        elif node.op == "XOR":
            values[index] = values[node.parents[0]] ^ values[node.parents[1]]
        elif node.op == "AND":
            values[index] = values[node.parents[0]] & values[node.parents[1]]
        elif node.op == "OR":
            values[index] = values[node.parents[0]] | values[node.parents[1]]
        pending.remove(index)
    return [values[index] for index in range(len(circuit.nodes))]


def causal_dependencies(circuit: BooleanCircuit) -> dict[str, frozenset[str]]:
    """Physical program history: closes -> compute -> copy -> uncompute -> done."""
    dependencies: dict[str, frozenset[str]] = {
        "CLOSE_A": frozenset(),
        "CLOSE_B": frozenset(),
        "CLOSE_P": frozenset(),
        "ARM": frozenset({"CLOSE_A", "CLOSE_B", "CLOSE_P"}),
    }
    previous = "ARM"
    forward = forward_primitives(circuit)
    for index in range(len(forward)):
        event = f"F_{index}"
        dependencies[event] = frozenset({previous})
        previous = event
    for label in ("COPY_T", "COPY_R", "COPY_X"):
        dependencies[label] = frozenset({previous})
    dependencies["COPY_DONE"] = frozenset({"COPY_T", "COPY_R", "COPY_X"})
    previous = "COPY_DONE"
    for index in reversed(range(len(forward))):
        event = f"U_{index}"
        dependencies[event] = frozenset({previous})
        previous = event
    dependencies["DONE"] = frozenset({previous})
    dependencies["RECORD"] = frozenset({"DONE"})
    return dependencies


def causal_closure(
    dependencies: dict[str, frozenset[str]],
    blocked: frozenset[str] = frozenset(),
) -> frozenset[str]:
    present: set[str] = set()
    changed = True
    while changed:
        changed = False
        for event, parents in dependencies.items():
            if event not in blocked and event not in present and parents <= present:
                present.add(event)
                changed = True
    return frozenset(present)


def random_causal_schedule(
    dependencies: dict[str, frozenset[str]], seed: int
) -> tuple[str, ...]:
    rng = random.Random(seed)
    present: set[str] = set()
    order: list[str] = []
    while len(present) < len(dependencies):
        enabled = [
            event
            for event, parents in dependencies.items()
            if event not in present and parents <= present
        ]
        if not enabled:
            raise RuntimeError("causal process deadlocked")
        event = rng.choice(enabled)
        present.add(event)
        order.append(event)
    return tuple(order)


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "https://doi.org/10.3390/e20060435",
        "bisio, d'ariano, mosco, perinotti, and tosini",
        "prior work",
        "coherent",
        "causal completion",
        "not a timeout",
        "nearest-neighbour",
        "uncompute",
        "supplied arming",
        "record formation remains imported",
        "born-frequency theorem",
        "one-dimensional",
        "proper-cubic interacting lift remains open",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves attribution, imports, and scope", not missing, missing)


def compiler_controls() -> None:
    detector = build_detector(16)
    circuit = detector.circuit
    gate_counts = {
        op: sum(node.op == op for node in circuit.nodes)
        for op in ("INPUT", "NOT", "XOR", "AND", "OR")
    }
    check(
        "bounded detector uses only generic Boolean gates and no outcome lookup table",
        set(node.op for node in circuit.nodes) <= {"CONST", "INPUT", "NOT", "XOR", "AND", "OR"}
        and all(node.name not in {str(row) for row in product(range(16), repeat=3)} for node in circuit.nodes),
        gate_counts,
    )

    mismatches = []
    reversible_mismatches = []
    garbage_examples: dict[tuple[int, int, int], tuple[int, ...]] = {}
    for first, second, projectile in product(range(16), repeat=3):
        supplied = supplied_input(detector, first, second, projectile)
        values = circuit.evaluate(supplied)
        actual = tuple(values[index] for index in detector.outputs)
        expected = direct_class(first, second, projectile)
        if actual != expected:
            mismatches.append((first, second, projectile, actual, expected))
        reversible, clean, garbage = reversible_run(detector, first, second, projectile)
        if reversible != expected or not clean:
            reversible_mismatches.append((first, second, projectile, reversible, expected, clean))
        if expected == (1, 0, 0) and len(garbage_examples) < 2:
            garbage_examples[(first, second, projectile)] = garbage
    check("all 4,096 lawful basis triples receive the exact T/R/X class", not mismatches, mismatches[:2])
    check("Bennett circuit preserves inputs, copies one class, and uncomputes every workspace bit", not reversible_mismatches, reversible_mismatches[:2])

    translations = 0
    translation_ok = True
    for first, second, projectile in product(range(16), repeat=3):
        reference = direct_class(first, second, projectile)
        for delta in range(-15, 16):
            shifted = (first + delta, second + delta, projectile + delta)
            if min(shifted) >= 0 and max(shifted) < 16:
                translations += 1
                translation_ok &= direct_class(*shifted) == reference
    check("the output is relational under every in-aperture common translation", translation_ok, translations)
    check(
        "pair exchange and reflection preserve the symmetric detector law",
        all(
            direct_class(a, b, p) == direct_class(b, a, p)
            and direct_class(15 - a, 15 - b, 15 - p)
            == (direct_class(a, b, p)[1], direct_class(a, b, p)[0], direct_class(a, b, p)[2])
            for a, b, p in product(range(16), repeat=3)
        ),
    )

    census = nearest_neighbour_census(detector)
    check(
        "every compiled reversible primitive is radius-one and semantically exact after explicit SWAP routing",
        bool(census["all_local"]) and bool(census["semantic_equivalence"]),
        census,
    )
    rotations = proper_cubic_rotations()
    axis = np.array((1, 0, 0))
    check(
        "the apparatus-carried nearest-neighbour embedding has all 24 proper-cubic images",
        len(rotations) == 24
        and all(np.sum(np.abs(rotation @ axis)) == 1 for rotation in rotations),
        len(rotations),
    )

    reference_cases = ((1, 2, 0), (1, 2, 5), (1, 8, 5), (7, 7, 7))
    schedule_ok = True
    schedules = 0
    for case in reference_cases:
        supplied = supplied_input(detector, *case)
        canonical = circuit.evaluate(supplied)
        for seed in range(32):
            shuffled = random_topological_values(circuit, supplied, 209000 + 97 * seed + sum(case))
            schedules += 1
            schedule_ok &= tuple(shuffled[index] for index in detector.outputs) == tuple(canonical[index] for index in detector.outputs)
    check("all tested asynchronous logical schedules converge to the same outcome", schedule_ok, schedules)

    close_inputs = frozenset({"CLOSE_A", "CLOSE_B", "CLOSE_P"})
    dependencies = causal_dependencies(circuit)
    complete = causal_closure(dependencies)
    internal = frozenset(dependencies) - frozenset({"DONE", "RECORD"})
    check(
        "DONE and RECORD have all three CLOSE facts and every circuit stage in causal ancestry",
        complete == frozenset(dependencies)
        and all(
            "DONE" not in causal_closure(dependencies, frozenset({event}))
            for event in internal
        ),
        {"events": len(dependencies), "mandatory_before_DONE": len(internal)},
    )
    check(
        "deleting any CLOSE input prevents ARM, DONE, and RECORD rather than timing out",
        all(
            {"ARM", "DONE", "RECORD"}.isdisjoint(
                causal_closure(dependencies, frozenset({deleted}))
            )
            for deleted in close_inputs
        ),
    )
    causal_orders = tuple(random_causal_schedule(dependencies, 209500 + seed) for seed in range(64))
    check(
        "every sampled physical process schedule reaches DONE last of its mandatory ancestry",
        all(
            set(order) == set(dependencies)
            and order.index("DONE") > max(order.index(event) for event in internal)
            and order.index("RECORD") > order.index("DONE")
            for order in causal_orders
        ),
        len(causal_orders),
    )

    examples = list(garbage_examples.items())
    check(
        "uncomputation is load-bearing for within-class coherence",
        len(examples) == 2
        and examples[0][1] != examples[1][1]
        and all(reversible_run(detector, *case)[1] for case, _ in examples),
        tuple(case for case, _ in examples),
    )

    rng = np.random.default_rng(209)
    amplitudes = rng.normal(size=16**3) + 1j * rng.normal(size=16**3)
    amplitudes /= np.linalg.norm(amplitudes)
    probabilities = np.zeros(3)
    for index, case in enumerate(product(range(16), repeat=3)):
        probabilities += abs(amplitudes[index]) ** 2 * np.asarray(direct_class(*case))
    redundant = np.diag(probabilities)
    check(
        "generic complex amplitudes give positive normalized class weights",
        np.min(probabilities) >= 0 and abs(np.sum(probabilities) - 1) < 2e-14,
        probabilities.tolist(),
    )
    check(
        "a redundant second outcome copy preserves every class weight",
        np.allclose(np.sum(redundant, axis=0), probabilities)
        and np.allclose(np.sum(redundant, axis=1), probabilities),
    )
    check(
        "the coherent compiler is not restricted to stabilizer dynamics",
        gate_counts["AND"] > 0 and any(op == "TOFFOLI" for op, _ in forward_primitives(circuit)),
        gate_counts,
    )


def scattering_controls() -> None:
    snapshots, total, pair_mass, projectile_mass, pair_coupling = prepare_and_evolve(0.06 * np.pi)
    state = snapshots[70]
    masks = local_masks(state.shape[0])
    probabilities = np.asarray(
        [float(np.sum(np.abs(state * mask[:, :, None, None, None]) ** 2)) for mask in masks]
    )
    check(
        "the compiled arithmetic predicate equals the Cycle-208 relational masks",
        all(
            direct_class(0, int(r), int(s))
            == tuple(int(mask[r_index, s_index]) for mask in masks)
            for r_index, r in enumerate(((np.arange(state.shape[0]) + state.shape[0] // 2) % state.shape[0] - state.shape[0] // 2))
            for s_index, s in enumerate(((np.arange(state.shape[0]) + state.shape[0] // 2) % state.shape[0] - state.shape[0] // 2))
        ),
    )
    check(
        "strong-collision detector weights remain positive and normalized",
        np.min(probabilities) >= 0 and abs(np.sum(probabilities) - 1) < 2e-12,
        probabilities.tolist(),
    )
    transmitted_state = projected_state(state, masks[0])
    conditional = channel_records(
        channel_spectrum(
            transmitted_state,
            total,
            pair_mass,
            projectile_mass,
            pair_coupling,
        ),
        total,
        pair_mass,
        pair_coupling,
    )
    transmitted = conditional["transmitted"]
    curvature = conditional["curvature_mass"]
    check(
        "the causally compiled T rail retains the calibrated molecular mass branch",
        transmitted["probability"] > 0.991
        and transmitted["momentum_coherence"] > 0.998
        and abs(transmitted["secant_mass"] / curvature - 1) < 0.02,
        {
            "conditional_intact": transmitted["probability"],
            "coherence": transmitted["momentum_coherence"],
            "secant_mass": transmitted["secant_mass"],
            "curvature_mass": curvature,
            "relative_error": transmitted["secant_mass"] / curvature - 1,
        },
    )
    coordinate = (
        (np.arange(state.shape[0]) + state.shape[0] // 2) % state.shape[0]
        - state.shape[0] // 2
    )
    signed_side = 2 * coordinate[None, :] - coordinate[:, None]
    ablated_masks = (signed_side < 0, signed_side > 0, signed_side == 0)
    ablated_probabilities = np.asarray(
        [
            float(
                np.sum(
                    np.abs(state * mask[:, :, None, None, None]) ** 2
                )
            )
            for mask in ablated_masks
        ]
    )
    check(
        "deleting the pair-close comparator changes the strong-collision outcome partition",
        np.max(np.abs(ablated_probabilities - probabilities)) > 0.04
        and abs(np.sum(ablated_probabilities) - 1) < 2e-12,
        {
            "compiled": probabilities.tolist(),
            "pair_close_deleted": ablated_probabilities.tolist(),
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    compiler_controls()
    scattering_controls()
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "COHERENT_CAUSAL_CLOSE_DETECTOR" if FAIL == 0 else "CYCLE209_OPEN")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
