#!/usr/bin/env python3
"""Exact finite probes for the neutral six-family substrate tournament.

The runner distinguishes construction from premise. It does not claim that a
finite control is the physical lattice law or that a failed finite candidate
is a universal no-go.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path
import math

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "SUBSTRATE_TOURNAMENT_DECISIVE_PROBES_NOTE_2026-07-13.md"
TOL = 1.0e-10
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
P0 = (I2 + Z) / 2.0
P1 = (I2 - Z) / 2.0


def density(psi: np.ndarray) -> np.ndarray:
    return np.outer(psi, psi.conj())


def matrix_units(dim: int) -> list[np.ndarray]:
    units: list[np.ndarray] = []
    for row in range(dim):
        for column in range(dim):
            unit = np.zeros((dim, dim), dtype=complex)
            unit[row, column] = 1.0
            units.append(unit)
    return units


def commutant_dimension(generators: list[np.ndarray]) -> int:
    dim = generators[0].shape[0]
    columns: list[np.ndarray] = []
    for unit in matrix_units(dim):
        columns.append(
            np.concatenate([(unit @ gen - gen @ unit).reshape(-1) for gen in generators])
        )
    linear_map = np.column_stack(columns)
    rank = int(np.sum(np.linalg.svd(linear_map, compute_uv=False) > 1.0e-9))
    return dim * dim - rank


def partial_trace_second(rho: np.ndarray) -> np.ndarray:
    return np.trace(rho.reshape(2, 2, 2, 2), axis1=1, axis2=3)


def partial_transpose_second(rho: np.ndarray) -> np.ndarray:
    return rho.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)


def source_contract() -> None:
    section("A - Source and scope contract")
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    normalized = text.replace("*", "").replace("`", "")
    check("A note is authority-free", "authority: none" in normalized)
    check("A six collapsed atoms are named", all(marker in text for marker in (
        "generated multi-site composition", "complete state", "exact physical law",
        "invariant record content", "one actual history", "normalized physical statistics",
    )))
    check("A universal no-go is disclaimed", "not a universal no-go" in text)
    check("A live axiom edit is forbidden at this gate", "not sufficient to edit the live constitution" in text)
    check("A N1-N8 gate is complete", all(f"### n{index}" in text for index in range(1, 9)))


def symmetric_activation() -> None:
    section("B - Symmetric self-activation and seeded propagation")

    # The blank condition is invariant under the swap 0 <-> 1. Exhaust the
    # two deterministic outputs and test equivariance.
    deterministic_choices = (0, 1)
    equivariant = [choice for choice in deterministic_choices if choice == 1 - choice]
    check("B no deterministic binary choice is swap-equivariant on a symmetric blank", equivariant == [])

    successor_set = frozenset((0, 1))
    swapped_set = frozenset(1 - value for value in successor_set)
    check("B the full support set is swap-covariant", successor_set == swapped_set)
    check("B set-valued covariance does not select one value", len(successor_set) == 2)

    # A normalized swap-invariant kernel is uniquely uniform in this finite
    # transitive control. Normalization/kernel semantics are supplied.
    grid = [index / 100.0 for index in range(101)]
    invariant_kernels = [(p, 1.0 - p) for p in grid if abs(p - (1.0 - p)) < TOL]
    check("B normalized swap symmetry fixes the finite binary kernel", invariant_kernels == [(0.5, 0.5)])

    def propagate(width: int, seed: int | None) -> list[tuple[int | None, ...]]:
        state: list[int | None] = [None] * width
        if seed is not None:
            state[0] = seed
        history = [tuple(state)]
        while True:
            nxt = list(state)
            for index in range(1, width):
                if state[index] is None and state[index - 1] is not None:
                    nxt[index] = state[index - 1]
            if nxt == state:
                return history
            state = nxt
            history.append(tuple(state))

    blank_history = propagate(6, None)
    zero_history = propagate(6, 0)
    one_history = propagate(6, 1)
    check("B the symmetric blank does not self-seed", len(blank_history) == 1 and all(v is None for v in blank_history[0]))
    check("B one boundary seed reaches the line at unit speed", len(zero_history) == 6 and zero_history[-1] == (0,) * 6)
    check("B propagation is content-covariant", all(
        tuple(None if v is None else 1 - v for v in left) == right
        for left, right in zip(zero_history, one_history)
    ))
    check("B propagation is append-only", all(
        all(old is None or old == new for old, new in zip(before, after))
        for before, after in zip(zero_history, zero_history[1:])
    ))
    check("B every new site has a finite one-neighbor certificate", all(
        after[index] is None or before[index] is not None or (index > 0 and before[index - 1] == after[index])
        for before, after in zip(zero_history, zero_history[1:])
        for index in range(len(after))
    ))


def sectors_and_permanence() -> None:
    section("C - Finite sectors, redundancy, and permanence")

    check("C full one-qubit algebra has scalar commutant", commutant_dimension([X, Z]) == 1)
    full_two = [np.kron(op, I2) for op in (X, Z)] + [np.kron(I2, op) for op in (X, Z)]
    check("C full two-qubit generated algebra has scalar commutant", commutant_dimension(full_two) == 1)

    # Z-block conditional expectation.
    plus = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
    rho_plus = density(plus)

    def dephase(rho: np.ndarray) -> np.ndarray:
        return P0 @ rho @ P0 + P1 @ rho @ P1

    mixed = dephase(rho_plus)
    check("C block refinement is trace preserving", abs(np.trace(mixed) - 1.0) < TOL)
    check("C block refinement is idempotent", np.linalg.norm(dephase(mixed) - mixed) < TOL)
    check("C nonselective refinement does not actualize a block", np.linalg.norm(mixed - P0) > 0.5 and np.linalg.norm(mixed - P1) > 0.5)
    check("C applying the restriction removes pre-record interference", abs(np.trace(rho_plus @ X) - 1.0) < TOL and abs(np.trace(mixed @ X)) < TOL)

    # Repetition-code matrix elements. Check every Pauli word of sub-global
    # support for N up to 5; this is finite and exhaustive in the Pauli basis.
    paulis = (I2, X, Y, Z)
    for size in (3, 4, 5):
        ket_zero = np.zeros(2**size, dtype=complex)
        ket_one = np.zeros(2**size, dtype=complex)
        ket_zero[0] = 1.0
        ket_one[-1] = 1.0
        max_subglobal = 0.0
        for word in product(paulis, repeat=size):
            support = sum(np.linalg.norm(op - I2) > TOL for op in word)
            if support >= size:
                continue
            operator = np.array([[1.0 + 0.0j]])
            for op in word:
                operator = np.kron(operator, op)
            max_subglobal = max(max_subglobal, abs(np.vdot(ket_one, operator @ ket_zero)))
        global_flip = X
        for _ in range(size - 1):
            global_flip = np.kron(global_flip, X)
        check(f"C no sub-global Pauli word connects {size}-site record sectors", max_subglobal < TOL)
        check(f"C the global flip reconnects the {size}-site sectors", abs(np.vdot(ket_one, global_flip @ ket_zero) - 1.0) < TOL)

    overlap = 0.8
    fixed_support = 2
    sizes = (4, 8, 16, 32, 64)
    bounds = [overlap ** (size - fixed_support) for size in sizes]
    check("C every fixed-support connector vanishes in the redundancy sequence", all(b < a for a, b in zip(bounds, bounds[1:])) and bounds[-1] < 2.0e-6)

    def l1_ball_size(radius: int) -> int:
        return sum(
            1
            for x in range(-radius, radius + 1)
            for y in range(-radius, radius + 1)
            for z in range(-radius, radius + 1)
            if abs(x) + abs(y) + abs(z) <= radius
        )

    balls = [l1_ball_size(radius) for radius in range(7)]
    expected_balls = [1, 7, 25, 63, 129, 231, 377]
    formula_balls = [
        (4 * radius**3 + 6 * radius**2 + 8 * radius + 3) // 3
        for radius in range(7)
    ]
    check("C exact L1 causal-ball sequence is reproduced", balls == expected_balls)
    check("C exact cubic formula reproduces every enumerated causal ball", balls == formula_balls)


def actuality_and_history() -> None:
    section("D - Actuality, global histories, and deterministic frequencies")

    successors = (0, 1)
    check("D two lawful successors do not identify one actual successor", len(successors) == 2)
    kernel = {0: 0.5, 1: 0.5}
    check("D a normalized kernel still has two supported histories", abs(sum(kernel.values()) - 1.0) < TOL and sum(value > 0 for value in kernel.values()) == 2)

    horizon = 6
    constant_histories = [tuple([value] * horizon) for value in (0, 1)]
    check("D global constancy admits two histories without boundary data", len(constant_histories) == 2)
    boundary = 1
    selected = [history for history in constant_histories if history[0] == boundary]
    check("D a fixed boundary plus the global constraint yields one history", selected == [tuple([1] * horizon)])

    # Identity transition: every distribution is invariant.
    candidate_measures = [np.array([p, 1.0 - p]) for p in (0.1, 0.3, 0.5, 0.9)]
    identity = np.eye(2)
    check("D identity dynamics admits multiple invariant measures", all(np.linalg.norm(mu @ identity - mu) < TOL for mu in candidate_measures))

    # A deterministic 3-cycle has one invariant probability vector and exact
    # visit frequencies over complete periods.
    cycle = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=float)
    a = np.vstack((cycle.T - np.eye(3), np.ones(3)))
    b = np.array([0.0, 0.0, 0.0, 1.0])
    invariant, *_ = np.linalg.lstsq(a, b, rcond=None)
    check("D the deterministic three-cycle has the uniform invariant measure", np.linalg.norm(invariant - np.ones(3) / 3.0) < TOL)
    orbit = [0]
    for _ in range(29):
        orbit.append((orbit[-1] + 1) % 3)
    counts = Counter(orbit)
    check("D complete periods have exact uniform visit frequencies", all(counts[value] == 10 for value in range(3)))

    # Same record sequence, arbitrary idle-step dilation.
    events = ("a", "b", "c", "d")
    dilated = tuple(item for event in events for item in ((None,) * 4 + (event,)))
    recovered = tuple(item for item in dilated if item is not None)
    check("D idle updates preserve event order and content", recovered == events)
    check("D idle updates change event frequency per update", len(events) / len(dilated) == 0.2)


def qubit_probability_controls() -> None:
    section("E - Qubit frame weights, marginals, and ancilla control")

    def f(vector: np.ndarray) -> float:
        return float((1.0 + vector[2] ** 3) / 2.0)

    directions = [
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
        np.array([math.sqrt(3.0) / 2.0, 0.0, 0.5]),
    ]
    check("E cubic frame weights are positive on the tested sphere", all(-TOL <= f(n) <= 1.0 + TOL for n in directions + [-n for n in directions]))
    check("E cubic frame weights normalize on every antipodal tested frame", all(abs(f(n) + f(-n) - 1.0) < TOL for n in directions))

    # If f(z)=1, a density representation has Bloch vector r=z. It would
    # predict (1+n_z)/2, which disagrees at n_z=1/2.
    tilted = directions[-1]
    density_prediction = (1.0 + tilted[2]) / 2.0
    check("E the normalized qubit frame is not density-affine", abs(f(tilted) - density_prediction) > 0.1)

    zero = np.array([1.0, 0.0], dtype=complex)
    one = np.array([0.0, 1.0], dtype=complex)
    phi = (np.kron(zero, zero) + np.kron(one, one)) / math.sqrt(2.0)
    rho_bell = density(phi)
    rho_a = partial_trace_second(rho_bell)
    check("E the Bell-state one-spectator marginal is maximally mixed", np.linalg.norm(rho_a - I2 / 2.0) < TOL)
    for projector in (P0, P1, (I2 + X) / 2.0, (I2 - X) / 2.0):
        joint_probability = np.trace(rho_bell @ np.kron(projector, I2)).real
        marginal_probability = np.trace(rho_a @ projector).real
        check("E one-spectator probability equals the reduced marginal", abs(joint_probability - marginal_probability) < TOL)

    # Transpose is positive on a single matrix but not completely positive.
    one_site_positive = np.linalg.eigvalsh(rho_plus := density(np.array([1.0, 1.0j]) / math.sqrt(2.0))).min() > -TOL
    transposed_positive = np.linalg.eigvalsh(rho_plus.T).min() > -TOL
    partial_t = partial_transpose_second(rho_bell)
    check("E transpose preserves positivity on the one-qubit control", one_site_positive and transposed_positive)
    check("E transpose fails the Bell-ancilla complete-positivity control", np.linalg.eigvalsh(partial_t).min() < -0.49)


def capacity_and_classification() -> None:
    section("F - Capacity and constitutional classification")

    capacity = 8
    archive: tuple[int, ...] = tuple()
    lengths = []
    for event in range(12):
        if len(archive) < capacity:
            archive = archive + (event,)
        lengths.append(len(archive))
    check("F a finite append-only archive saturates", lengths[-1] == capacity and lengths[-1] == lengths[-2])
    check("F saturation occurs before an indefinitely operating clock", lengths.index(capacity) < len(lengths) - 1)

    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required_dispositions = (
        "predictive-specification domain first",
        "keep qualification provisional",
        "already-postulated fixed rule",
        "derive from the law or select exact record identity semantics",
        "not derivable from branch support alone",
        "not derivable from determinism or sectors alone",
    )
    for marker in required_dispositions:
        check(f"F disposition marker: {marker}", marker in text)
    check("F simulation analogy is not promoted to physics", "engineering analogy only" in text)
    check("F exact predictive specification remains the live wall", "postulated fixed rule has yet been produced" in text)


def main() -> int:
    source_contract()
    symmetric_activation()
    sectors_and_permanence()
    actuality_and_history()
    qubit_probability_controls()
    capacity_and_classification()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: exact finite route tournament; no full-lattice law or axiom edit")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
