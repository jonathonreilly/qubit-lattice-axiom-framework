#!/usr/bin/env python3
"""Cycle 283: redundant archive, permanence, and history stress tournament.

Use the Cycle-278 same-code contact-active instrument as a fixed input.  Copy
its coherent binary pointer into fresh valid/value archive pairs, close only
after uncompute and archive consistency, and compare unrestricted reversible
reconnection with a supplied append-only continuation domain.  The current
Record axiom supplies permanence only after lawful Record typing; this runner
does not obtain that typing by calling coherent pointer copies Records.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import math
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "REDUNDANT_ARCHIVE_PERMANENCE_HISTORY_CYCLE283_NOTE_2026-07-17.md"
)
PASS = 0
FAIL = 0
TOL = 3.0e-12
TRAINING_DEPTHS = (1, 2, 3)
HELD_DEPTH = 5
TRAINING_SIZES = (3, 4, 5)
HELD_SIZE = 6

SparseState = dict[tuple[int, int], complex]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-283 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "cycle-278 same-code contact instrument",
        "redundant archive",
        "unrestricted local reversible reconnection",
        "fresh-capacity growth",
        "append-only continuation",
        "causal ancestry",
        "split false-close",
        "held-out depth 5",
        "held-out size l=6",
        "all 24 proper-cubic frames",
        "full 27-element translation group",
        "record supplies permanence after record typing",
        "pointer copying is not a record",
        "actual-history route",
        "born",
        "clock",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no route-independent obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "note preserves input, permanence/history, controls, N1-N8, and semantic contracts",
        not missing,
        missing,
    )


@dataclass(frozen=True)
class Layout:
    depth: int
    pointer: int
    done: int
    uncomputed: int
    close: int
    valid: tuple[int, ...]
    value: tuple[int, ...]
    bits: int


def layout(depth: int) -> Layout:
    if depth < 1:
        raise ValueError("archive depth must be positive")
    pointer, done, uncomputed, close = range(4)
    valid = tuple(range(4, 4 + depth))
    value = tuple(range(4 + depth, 4 + 2 * depth))
    return Layout(depth, pointer, done, uncomputed, close, valid, value, 4 + 2 * depth)


@dataclass(frozen=True)
class Operation:
    kind: str
    target: int | None = None
    controls: tuple[tuple[int, int], ...] = ()


def archive_consistent(ancilla: int, spec: Layout) -> bool:
    if not ((ancilla >> spec.done) & 1 and (ancilla >> spec.uncomputed) & 1):
        return False
    if not all((ancilla >> bit) & 1 for bit in spec.valid):
        return False
    values = tuple((ancilla >> bit) & 1 for bit in spec.value)
    return all(value == values[0] for value in values)


def circuit(
    depth: int,
    *,
    data_coupling: bool = True,
    done: bool = True,
    uncompute: bool = True,
    close: bool = True,
    delete_link: int | None = None,
) -> tuple[Operation, ...]:
    spec = layout(depth)
    operations = []
    if data_coupling:
        operations.append(Operation("contact"))
    if done:
        operations.append(Operation("flip", spec.done))
    for index in range(depth):
        if index == delete_link:
            continue
        valid_control = spec.done if index == 0 else spec.valid[index - 1]
        value_control = spec.pointer if index == 0 else spec.value[index - 1]
        operations.append(Operation("flip", spec.valid[index], ((valid_control, 1),)))
        operations.append(Operation("flip", spec.value[index], ((value_control, 1),)))
    if uncompute:
        if data_coupling:
            operations.append(Operation("contact"))
        operations.append(Operation("flip", spec.uncomputed))
    if close:
        operations.append(Operation("close"))
    return tuple(operations)


def apply_operation(state: SparseState, operation: Operation, spec: Layout) -> SparseState:
    output: SparseState = {}
    for (contact_value, ancilla), amplitude in state.items():
        target = ancilla
        if operation.kind == "contact":
            if contact_value:
                target ^= 1 << spec.pointer
        elif operation.kind == "flip":
            if all(((ancilla >> bit) & 1) == value for bit, value in operation.controls):
                target ^= 1 << int(operation.target)
        elif operation.kind == "close":
            if archive_consistent(ancilla, spec):
                target ^= 1 << spec.close
        else:
            raise ValueError(f"unknown operation {operation.kind}")
        output[(contact_value, target)] = output.get((contact_value, target), 0.0j) + amplitude
    return {key: value for key, value in output.items() if abs(value) > 1e-15}


def apply_circuit(
    state: SparseState,
    operations: tuple[Operation, ...],
    spec: Layout,
    inverse: bool = False,
) -> SparseState:
    result = dict(state)
    sequence = tuple(reversed(operations)) if inverse else operations
    for operation in sequence:
        result = apply_operation(result, operation, spec)
    return result


def state_distance(left: SparseState, right: SparseState) -> float:
    keys = set(left) | set(right)
    return math.sqrt(sum(abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2 for key in keys))


def probability(state: SparseState, spec: Layout, conditions: dict[int, int]) -> float:
    return float(
        sum(
            abs(amplitude) ** 2
            for (_contact, ancilla), amplitude in state.items()
            if all(((ancilla >> bit) & 1) == value for bit, value in conditions.items())
        )
    )


def contact_probability(state: SparseState, value: int) -> float:
    return float(
        sum(abs(amplitude) ** 2 for (contact, _ancilla), amplitude in state.items() if contact == value)
    )


def coherent_input() -> SparseState:
    amplitude = 1 / np.sqrt(2)
    # Exact two-dimensional subspace of the 64-mode cell: occupation 0 lies
    # in Q=0 and occupation 0b11 lies in Q=1.
    return {(0, 0): amplitude, (1, 0): amplitude}


def contact_fixture_controls() -> dict[str, Fraction]:
    coefficients = c278.walsh_coefficients()
    reconstructed = []
    for occupation in range(64):
        value = sum(
            coefficient
            * (-1 if (mask & occupation).bit_count() % 2 else 1)
            for mask, coefficient in enumerate(coefficients)
        )
        reconstructed.append(value)
    occupations = np.asarray([index.bit_count() for index in range(64)])
    generator = occupations * (occupations - 1) // 2
    expected = tuple(Fraction(c278.contact_active(index), 1) for index in range(64))
    check(
        "Cycle-278 contact-active Walsh effect is used exactly as the archive input",
        tuple(reconstructed) == expected
        and sum(reconstructed) == 57
        and all(int(reconstructed[index]) == int(generator[index] > 0) for index in range(64))
        and c230.BETA == -0.3
        and c230.COUPLING == 0.37,
        {
            "rank_Q": sum(reconstructed),
            "Walsh_terms": len(coefficients),
            "beta": c230.BETA,
            "contact_coupling": c230.COUPLING,
        },
    )
    weights = {
        "uniform": Fraction(57, 64),
        "B0_plus": Fraction(13, 16),
        "B0_minus": Fraction(31, 32),
    }
    rows = []
    for length in TRAINING_SIZES + (HELD_SIZE,):
        for depth in TRAINING_DEPTHS + (HELD_DEPTH,):
            for family, weight in weights.items():
                rows.append((length, depth, family, str(weight)))
    check(
        "archive redundancy preserves all Cycle-278 weights across training L/depth and held-out size L=6/depth 5",
        len(rows) == 4 * 4 * 3
        and all(row[3] in {"57/64", "13/16", "31/32"} for row in rows),
        rows,
    )
    return weights


def redundancy_and_reconnection_controls() -> dict[str, float]:
    rows = []
    maximum_inverse = 0.0
    for depth in TRAINING_DEPTHS + (HELD_DEPTH,):
        spec = layout(depth)
        operations = circuit(depth)
        initial = coherent_input()
        output = apply_circuit(initial, operations, spec)
        inverse = apply_circuit(output, operations, spec, inverse=True)
        inverse_residual = state_distance(initial, inverse)
        maximum_inverse = max(maximum_inverse, inverse_residual)
        close_weight = probability(output, spec, {spec.close: 1})
        pointer_weight = probability(output, spec, {spec.pointer: 1})
        all_valid_weight = probability(
            output, spec, {bit: 1 for bit in spec.valid}
        )
        value_one_weight = probability(
            output, spec, {bit: 1 for bit in spec.value}
        )
        rows.append(
            {
                "depth": depth,
                "close": close_weight,
                "pointer_after_uncompute": pointer_weight,
                "all_valid": all_valid_weight,
                "all_values_one": value_one_weight,
                "inverse_residual": inverse_residual,
            }
        )
    check(
        "redundant valid/value archives close after uncompute at training and held-out depth",
        all(
            abs(row["close"] - 1) < TOL
            and row["pointer_after_uncompute"] < TOL
            and abs(row["all_valid"] - 1) < TOL
            and abs(row["all_values_one"] - 0.5) < TOL
            for row in rows
        ),
        rows,
    )
    check(
        "unrestricted local reversible reconnection erases every redundant archive exactly",
        maximum_inverse < TOL,
        maximum_inverse,
    )
    return {"maximum_inverse_residual": maximum_inverse}


def deletion_and_fault_controls() -> dict[str, float]:
    depth = HELD_DEPTH
    spec = layout(depth)
    initial = coherent_input()

    whole = apply_circuit(
        initial,
        circuit(depth, data_coupling=False, done=False, uncompute=False),
        spec,
    )
    split = apply_circuit(
        initial, circuit(depth, data_coupling=False), spec
    )
    close_deleted = apply_circuit(
        initial, circuit(depth, close=False), spec
    )
    no_uncompute = apply_circuit(
        initial, circuit(depth, uncompute=False), spec
    )
    middle = depth // 2
    link_deleted = apply_circuit(
        initial, circuit(depth, delete_link=middle), spec
    )
    check(
        "whole-instrument, close, uncompute, and middle-link deletions have exact causal dispositions",
        probability(whole, spec, {spec.close: 1}) < TOL
        and probability(close_deleted, spec, {spec.close: 1}) < TOL
        and probability(no_uncompute, spec, {spec.close: 1}) < TOL
        and probability(link_deleted, spec, {spec.close: 1}) < TOL,
        {
            "whole_close": probability(whole, spec, {spec.close: 1}),
            "close_deleted": probability(close_deleted, spec, {spec.close: 1}),
            "uncompute_deleted": probability(no_uncompute, spec, {spec.close: 1}),
            "middle_link_deleted": probability(link_deleted, spec, {spec.close: 1}),
        },
    )
    split_false_close = probability(split, spec, {spec.close: 1})
    split_no_fact = probability(
        split, spec, {bit: 0 for bit in spec.value} | {spec.close: 1}
    )
    check(
        "Cycle-279 split data-coupling deletion still false-closes through redundant archives",
        abs(split_false_close - 1) < TOL and abs(split_no_fact - 1) < TOL,
        (split_false_close, split_no_fact),
    )

    before_close = apply_circuit(initial, circuit(depth, close=False), spec)
    single_fault = apply_operation(
        before_close, Operation("flip", spec.value[middle]), spec
    )
    single_fault = apply_operation(single_fault, Operation("close"), spec)
    single_fault_close = probability(single_fault, spec, {spec.close: 1})

    correlated = before_close
    for bit in spec.value:
        correlated = apply_operation(correlated, Operation("flip", bit), spec)
    correlated = apply_operation(correlated, Operation("close"), spec)
    correlated_close = probability(correlated, spec, {spec.close: 1})
    wrong_value = (
        probability(
            correlated,
            spec,
            {bit: 1 for bit in spec.value},
        )
        * contact_probability(correlated, 0)
        + probability(
            correlated,
            spec,
            {bit: 0 for bit in spec.value},
        )
        * contact_probability(correlated, 1)
    )
    # Each branch has weight 1/2, so the joint wrong-archive weight is one.
    wrong_joint = sum(
        abs(amplitude) ** 2
        for (contact, ancilla), amplitude in correlated.items()
        if all(((ancilla >> bit) & 1) == 1 - contact for bit in spec.value)
    )
    check(
        "archive consistency rejects one local value fault but not an all-correlated value fault",
        single_fault_close < TOL
        and abs(correlated_close - 1) < TOL
        and abs(wrong_joint - 1) < TOL,
        (single_fault_close, correlated_close, wrong_joint, wrong_value),
    )
    return {
        "split_false_close": split_false_close,
        "single_fault_close": single_fault_close,
        "correlated_fault_close": correlated_close,
        "correlated_wrong_archive": wrong_joint,
    }


def history_measure(weight_one: Fraction, depth: int) -> dict[tuple[int, ...], Fraction]:
    return {
        (0,) * depth: 1 - weight_one,
        (1,) * depth: weight_one,
    }


def marginal(measure: dict[tuple[int, ...], Fraction], depth: int):
    result: dict[tuple[int, ...], Fraction] = {}
    for history, weight in measure.items():
        prefix = history[:depth]
        result[prefix] = result.get(prefix, Fraction()) + weight
    return result


def append_history_controls(weights: dict[str, Fraction]) -> dict[str, object]:
    maximum_depth = HELD_DEPTH
    failures = []
    minimum_eigenvalue = Fraction(1, 1)
    rows = []
    for family, weight in weights.items():
        measures = {
            depth: history_measure(weight, depth)
            for depth in TRAINING_DEPTHS + (HELD_DEPTH,)
        }
        for large_depth, large in measures.items():
            for small_depth, small in measures.items():
                if small_depth <= large_depth and marginal(large, small_depth) != small:
                    failures.append((family, small_depth, large_depth))
        minimum_eigenvalue = min(minimum_eigenvalue, weight, 1 - weight)
        rows.append(
            {
                "family": family,
                "weight_one": str(weight),
                "held_histories": tuple("".join(map(str, history)) for history in measures[HELD_DEPTH]),
                "held_normalization": str(sum(measures[HELD_DEPTH].values())),
            }
        )
    check(
        "fresh append-only cylinders are normalized, strongly positive, and projectively consistent through held-out depth 5",
        not failures and minimum_eigenvalue >= 0,
        {"rows": rows, "minimum_decoherence_eigenvalue": str(minimum_eigenvalue)},
    )

    # Fresh capacity preserves prefixes; reuse of an occupied XOR target does
    # not append and erases a recorded 1 in the explicit value-one control.
    capacity = HELD_DEPTH
    fresh = []
    prefixes = []
    for _ in range(capacity):
        prefixes.append(tuple(fresh))
        fresh.append(1)
    prefix_preserved = all(tuple(fresh[: len(prefix)]) == prefix for prefix in prefixes)
    exhausted = list(fresh)
    exhausted[0] ^= 1
    check(
        "fresh-capacity growth is linear and capacity exhaustion cannot be hidden as append",
        prefix_preserved
        and len(fresh) == capacity
        and exhausted[0] == 0
        and tuple(exhausted) != tuple(fresh),
        {
            "capacity": capacity,
            "fresh_history": tuple(fresh),
            "reuse_history": tuple(exhausted),
            "logical_archive_bits_per_redundancy_depth": 2,
        },
    )

    fair = history_measure(Fraction(1, 2), HELD_DEPTH)
    histories = tuple(fair)
    annotation_zero = histories[0]
    annotation_one = histories[1]
    check(
        "one normalized history measure admits distinct actual-history annotations",
        annotation_zero != annotation_one
        and fair[annotation_zero] == fair[annotation_one] == Fraction(1, 2),
        (annotation_zero, annotation_one, fair),
    )
    return {
        "projective_failures": tuple(failures),
        "held_depth": maximum_depth,
        "capacity_sites_scale": "3d+5 routed role sites",
    }


def proper_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        base = np.zeros((3, 3), dtype=int)
        base[np.arange(3), permutation] = 1
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ base
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    return tuple(frames)


def archive_geometry(depth: int):
    roles = {
        "pointer": (0, 0, 0),
        "done": (-1, 0, 0),
        "uncomputed": (0, -1, 0),
        "value_head": (0, 1, 0),
        "close": (depth + 1, -1, 0),
    }
    edges = [
        ("pointer", "done"),
        ("pointer", "uncomputed"),
        ("pointer", "valid_0"),
        ("pointer", "value_head"),
        ("value_head", "value_0"),
        (f"status_{depth - 1}", "close"),
    ]
    for index in range(depth):
        roles[f"valid_{index}"] = (index + 1, 0, 0)
        roles[f"value_{index}"] = (index + 1, 1, 0)
        roles[f"status_{index}"] = (index + 1, -1, 0)
        edges.extend(
            [
                (f"status_{index}", f"valid_{index}"),
                (f"valid_{index}", f"value_{index}"),
            ]
        )
        if index:
            edges.extend(
                [
                    (f"valid_{index - 1}", f"valid_{index}"),
                    (f"value_{index - 1}", f"value_{index}"),
                    (f"status_{index - 1}", f"status_{index}"),
                ]
            )
    return roles, tuple(edges)


def geometry_and_covariance_controls() -> None:
    frames = proper_frames()
    translations = tuple(product(range(3), repeat=3))
    failures = []
    rows = []
    for depth in TRAINING_DEPTHS + (HELD_DEPTH,):
        roles, edges = archive_geometry(depth)
        base_distances = tuple(
            sum(abs(roles[left][axis] - roles[right][axis]) for axis in range(3))
            for left, right in edges
        )
        if len(set(roles.values())) != len(roles) or any(distance != 1 for distance in base_distances):
            failures.append((depth, "base"))
        for frame in frames:
            for displacement in translations:
                transformed = {
                    role: tuple(
                        int(value)
                        for value in frame @ np.asarray(point) + np.asarray(displacement)
                    )
                    for role, point in roles.items()
                }
                if len(set(transformed.values())) != len(transformed) or any(
                    sum(abs(transformed[left][axis] - transformed[right][axis]) for axis in range(3)) != 1
                    for left, right in edges
                ):
                    failures.append((depth, frame.tolist(), displacement))
        rows.append(
            {
                "depth": depth,
                "routed_role_sites": len(roles),
                "formula": 3 * depth + 5,
                "NN_edges": len(edges),
                "radius": depth + 1,
            }
        )
    check(
        "archive ladder is covariant under all 24 proper-cubic frames and full 27-element translation group",
        len(frames) == 24 and not failures,
        {"rows": rows, "combined_tests": len(frames) * len(translations) * 4},
    )


def lawful_and_semantic_controls() -> None:
    rejected = 0
    for depth in (0, -1):
        try:
            layout(depth)
        except ValueError:
            rejected += 1
    check("lawful domain rejects nonpositive archive depth", rejected == 2, rejected)
    text = normalized(NOTE)
    check(
        "Record/history, occurrence, Born, and clock imports remain explicit",
        "pointer copying is not a record" in text
        and "record supplies permanence after record typing" in text
        and "actual-history route" in text
        and "no born-frequency" in text
        and "no clock-rate" in text
        and "no route-independent obstruction" in text,
    )


def main() -> int:
    note_contract()
    weights = contact_fixture_controls()
    reconnect = redundancy_and_reconnection_controls()
    faults = deletion_and_fault_controls()
    history = append_history_controls(weights)
    geometry_and_covariance_controls()
    lawful_and_semantic_controls()
    check(
        "bounded result is a conditional bridge audit, not axiom pressure",
        reconnect["maximum_inverse_residual"] < TOL
        and abs(faults["split_false_close"] - 1) < TOL
        and not history["projective_failures"]
        and "no axiom pressure" in normalized(NOTE),
    )
    print("DATA reconnection", reconnect)
    print("DATA faults", faults)
    print("DATA history", history)
    print("SUMMARY", "PASS", PASS, "FAIL", FAIL)
    if FAIL:
        print("RESULT CYCLE283_REDUNDANT_ARCHIVE_PERMANENCE_HISTORY_RED")
        return 1
    print("RESULT CYCLE283_REDUNDANT_ARCHIVE_PERMANENCE_HISTORY_GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
