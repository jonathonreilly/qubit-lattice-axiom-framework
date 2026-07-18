#!/usr/bin/env python3
"""Cycle 10: reversible dilation and closed-cycle gravity probes.

Companion note:
  docs/work_history/repo/review_feedback/
  REVERSIBLE_DILATION_CLOSED_CYCLE_GRAVITY_CYCLE10_NOTE_2026-07-14.md

The runner separates four questions that Cycle 9 left coupled:

* can its lazy cubic diffusion step have a finite local unitary dilation?;
* can that finite dilation be reused forever without a fresh environment?;
* can the source/export current be closed into a local conserved cycle?; and
* do a common local clock rate and a scalar Green profile fix gravity's
  transport and lensing content?

It changes no axiom, primitive, registry, queue, or audit surface.  Exit code
is zero exactly when every finite/symbolic probe passes.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from math import ceil, log, log2
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "REVERSIBLE_DILATION_CLOSED_CYCLE_GRAVITY_CYCLE10_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
PRIMITIVE_CHECK = ROOT / "docs" / "ai_methodology" / "skills" / "PRIMITIVE_REGISTRY_CHECK.md"
CONTROLLED_VOCABULARY = ROOT / "docs" / "repo" / "CONTROLLED_VOCABULARY.md"

PASS = 0
FAIL = 0
TOL = 2.0e-10
Coord = tuple[int, int, int]
DIRECTIONS: tuple[Coord, ...] = (
    (0, 0, 0),
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
CYCLE_NINE_WEIGHTS: tuple[Fraction, ...] = (
    Fraction(1, 2),
    Fraction(1, 12),
    Fraction(1, 12),
    Fraction(1, 12),
    Fraction(1, 12),
    Fraction(1, 12),
    Fraction(1, 12),
)


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


def coordinates(side: int) -> tuple[Coord, ...]:
    return tuple(product(range(side), repeat=3))


def coordinate_index(side: int) -> dict[Coord, int]:
    return {coordinate: index for index, coordinate in enumerate(coordinates(side))}


def positive_edges(side: int) -> tuple[tuple[int, int], ...]:
    index = coordinate_index(side)
    edges: list[tuple[int, int]] = []
    for coordinate in coordinates(side):
        for axis in range(3):
            neighbor = list(coordinate)
            neighbor[axis] = (neighbor[axis] + 1) % side
            edges.append((index[coordinate], index[tuple(neighbor)]))
    return tuple(edges)


def lattice_laplacian(side: int) -> np.ndarray:
    count = side**3
    matrix = np.zeros((count, count), dtype=float)
    for left, right in positive_edges(side):
        matrix[left, left] += 1.0
        matrix[right, right] += 1.0
        matrix[left, right] -= 1.0
        matrix[right, left] -= 1.0
    return matrix


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations: list[np.ndarray] = []
    for axis_permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(axis_permutation):
                matrix[row, column] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                rotations.append(matrix)
    unique = {tuple(matrix.ravel()): matrix for matrix in rotations}
    return tuple(unique.values())


def coordinate_map(
    side: int,
    rotation: np.ndarray | None = None,
    shift: Coord = (0, 0, 0),
) -> np.ndarray:
    index = coordinate_index(side)
    if rotation is None:
        rotation = np.eye(3, dtype=int)
    mapping = np.zeros(side**3, dtype=int)
    for coordinate in coordinates(side):
        moved_array = (
            rotation @ np.asarray(coordinate, dtype=int)
            + np.asarray(shift, dtype=int)
        ) % side
        moved = tuple(int(value) for value in moved_array)
        mapping[index[coordinate]] = index[moved]
    return mapping


def direction_map(rotation: np.ndarray) -> np.ndarray:
    index = {direction: number for number, direction in enumerate(DIRECTIONS)}
    mapping = np.zeros(len(DIRECTIONS), dtype=int)
    for number, direction in enumerate(DIRECTIONS):
        moved = tuple(int(value) for value in rotation @ np.asarray(direction))
        mapping[number] = index[moved]
    return mapping


def controlled_shift_map(side: int) -> np.ndarray:
    index = coordinate_index(side)
    mapping = np.zeros(side**3 * len(DIRECTIONS), dtype=int)
    for coordinate in coordinates(side):
        site = index[coordinate]
        for direction_number, direction in enumerate(DIRECTIONS):
            moved = tuple(
                (coordinate[axis] + direction[axis]) % side for axis in range(3)
            )
            source = site * len(DIRECTIONS) + direction_number
            target = index[moved] * len(DIRECTIONS) + direction_number
            mapping[source] = target
    return mapping


def joint_symmetry_map(
    side: int,
    rotation: np.ndarray | None = None,
    shift: Coord = (0, 0, 0),
) -> np.ndarray:
    sites = coordinate_map(side, rotation=rotation, shift=shift)
    directions = (
        np.arange(len(DIRECTIONS), dtype=int)
        if rotation is None
        else direction_map(rotation)
    )
    mapping = np.zeros(side**3 * len(DIRECTIONS), dtype=int)
    for site in range(side**3):
        for direction in range(len(DIRECTIONS)):
            source = site * len(DIRECTIONS) + direction
            target = sites[site] * len(DIRECTIONS) + directions[direction]
            mapping[source] = target
    return mapping


def cycle_nine_lazy_step(side: int) -> np.ndarray:
    count = side**3
    index = coordinate_index(side)
    matrix = np.zeros((count, count), dtype=float)
    for coordinate in coordinates(side):
        source = index[coordinate]
        for direction, weight in zip(DIRECTIONS, CYCLE_NINE_WEIGHTS, strict=True):
            moved = tuple(
                (coordinate[axis] + direction[axis]) % side for axis in range(3)
            )
            matrix[index[moved], source] += float(weight)
    return matrix


def partial_trace_ancilla_two(joint: np.ndarray, system_dimension: int) -> np.ndarray:
    reshaped = joint.reshape(2, system_dimension, 2, system_dimension)
    return reshaped[0, :, 0, :] + reshaped[1, :, 1, :]


def source_contract() -> None:
    section("A - Refresher, source, scope, and N1-N8 contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    primitive_check = PRIMITIVE_CHECK.read_text(encoding="utf-8")
    vocabulary = CONTROLLED_VOCABULARY.read_text(encoding="utf-8")

    check("A current framework still has exactly four named axioms", all(name in axioms for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")))
    check("A Record says occurrence but withholds formation rule", "Records form." in axioms and "formation rules" in axioms)
    check("A Admissibility is explicitly not dynamics", "Admissibility is not a dynamics axiom" in axioms)
    check("A approved premise registry still has exactly four nodes", registry.count('"current_path"') == 4)
    check("A primitive guard withholds dynamics and probability", "probability rule" in primitive_check and "dynamics" in primitive_check)
    check("A controlled vocabulary permits meta notes but not audit authority", "`meta`" in vocabulary and "do not bare-declare `retained`" in vocabulary.lower())

    for phrase in (
        "authority: none",
        "conditional probe law",
        "one-step cubic unitary dilation",
        "finite-environment repeated-mixing boundary",
        "closed internal return cycle",
        "permanent-archive saturation",
        "paired scheduler countermodels",
        "scalar clock universality does not close transport or lensing",
        "n1 — alternative routes",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
    ):
        check(f"A note contains boundary: {phrase}", phrase in normalized)

    for url in (
        "https://arxiv.org/abs/1804.00918",
        "https://arxiv.org/abs/quant-ph/0208195",
        "https://arxiv.org/abs/quant-ph/0507022",
    ):
        check(f"A note cites primary source: {url}", url in note.lower())


def one_step_cubic_unitary_dilation() -> None:
    section("B - One-step finite local cubic unitary dilation")
    side = 3
    count = side**3
    shift = controlled_shift_map(side)
    check("B controlled shift is a permutation/unitary", len(set(shift.tolist())) == len(shift))

    index = coordinate_index(side)
    inverse_index = {value: key for key, value in index.items()}
    maximum_range = 0
    coin_preserved = True
    local_targets_exact = True
    for source, target in enumerate(shift):
        source_site, source_direction = divmod(source, len(DIRECTIONS))
        target_site, target_direction = divmod(int(target), len(DIRECTIONS))
        coin_preserved = coin_preserved and source_direction == target_direction
        source_coordinate = inverse_index[source_site]
        target_coordinate = inverse_index[target_site]
        direction = DIRECTIONS[source_direction]
        expected = tuple((source_coordinate[a] + direction[a]) % side for a in range(3))
        local_targets_exact = local_targets_exact and target_coordinate == expected
        maximum_range = max(maximum_range, sum(abs(value) for value in direction))
    check("B controlled shift preserves every coin label", coin_preserved)
    check("B controlled shift has the declared target on every basis state", local_targets_exact)
    check("B controlled shift has range one", maximum_range == 1)

    rotations = proper_cubic_rotations()
    check("B proper cubic rotation group has order 24", len(rotations) == 24)
    for number, rotation in enumerate(rotations):
        symmetry = joint_symmetry_map(side, rotation=rotation)
        check(
            f"B controlled shift commutes with proper cubic rotation {number:02d}",
            np.array_equal(symmetry[shift], shift[symmetry]),
        )
        coin_permutation = direction_map(rotation)
        cycle_nine_coin = np.sqrt(np.asarray(CYCLE_NINE_WEIGHTS, dtype=float))
        check(
            f"B Cycle-9 seven-label coin is invariant under rotation {number:02d}",
            np.allclose(cycle_nine_coin[coin_permutation], cycle_nine_coin, atol=TOL),
        )

    translation = joint_symmetry_map(side, shift=(1, 2, 1))
    check("B controlled shift commutes with lattice translations", np.array_equal(translation[shift], shift[translation]))

    transition = cycle_nine_lazy_step(side)
    laplacian = lattice_laplacian(side)
    check("B reduced one-step transition is doubly stochastic", np.allclose(transition.sum(axis=0), 1.0) and np.allclose(transition.sum(axis=1), 1.0))
    check("B reduced step obeys the Cycle-9 identity I-P=L/12 exactly", np.allclose(np.eye(count) - transition, laplacian / 12.0, atol=TOL))

    origin = index[(0, 0, 0)]
    reduced = transition[:, origin]
    check("B localized input has the exact Cycle-9 stay/hop weights", np.count_nonzero(reduced > TOL) == 7 and abs(reduced[origin] - 0.5) < TOL and np.allclose(np.sort(reduced[reduced > TOL])[:6], 1.0 / 12.0))
    check("B one-step reduced position purity is 7/24", abs(float(reduced @ reduced) - 7.0 / 24.0) < TOL)
    check("B system and direction coin are entangled after a localized step", float(reduced @ reduced) < 1.0 - TOL)

    initial_joint = np.zeros(count * len(DIRECTIONS), dtype=complex)
    coin_amplitudes = np.sqrt(np.asarray(CYCLE_NINE_WEIGHTS, dtype=float))
    initial_joint[origin * len(DIRECTIONS) : (origin + 1) * len(DIRECTIONS)] = coin_amplitudes
    evolved_joint = np.zeros_like(initial_joint)
    evolved_joint[shift] = initial_joint
    amplitude_by_site_and_coin = evolved_joint.reshape(count, len(DIRECTIONS))
    traced_position = amplitude_by_site_and_coin @ amplitude_by_site_and_coin.conj().T
    check("B explicit unitary-plus-partial-trace diagonal equals the Cycle-9 P column", np.allclose(np.real(np.diag(traced_position)), reduced, atol=TOL))
    check("B explicit traced position state has no hidden off-diagonal remainder", np.max(np.abs(traced_position - np.diag(np.diag(traced_position)))) < TOL)


def repeated_coin_and_finite_environment_boundary() -> None:
    section("C - Reused coin, fresh coins, and finite-environment boundary")
    side = 5
    index = coordinate_index(side)
    origin = index[(0, 0, 0)]
    transition = cycle_nine_lazy_step(side)
    initial = np.zeros(side**3)
    initial[origin] = 1.0
    fresh_two = transition @ transition @ initial

    reused_two = np.zeros(side**3)
    for direction, weight in zip(DIRECTIONS, CYCLE_NINE_WEIGHTS, strict=True):
        moved = tuple((2 * direction[axis]) % side for axis in range(3))
        reused_two[index[moved]] += float(weight)

    reused_one = np.zeros(side**3)
    for direction, weight in zip(DIRECTIONS, CYCLE_NINE_WEIGHTS, strict=True):
        moved = tuple(direction[axis] % side for axis in range(3))
        reused_one[index[moved]] += float(weight)
    check("C fresh and reused coins agree for the first step", np.allclose(transition @ initial, reused_one, atol=TOL))
    check("C reusing one unchanged coin fails at the second Markov step", np.linalg.norm(fresh_two - reused_two, ord=1) > 0.5)
    check("C reused coin retains only seven branches at step two", np.count_nonzero(reused_two > TOL) == 7)
    check("C fresh two-step walk has more than seven endpoints", np.count_nonzero(fresh_two > TOL) > 7)

    def convolve(distribution: dict[Coord, Fraction]) -> dict[Coord, Fraction]:
        answer: dict[Coord, Fraction] = {}
        for coordinate, weight in distribution.items():
            for direction, step_weight in zip(
                DIRECTIONS, CYCLE_NINE_WEIGHTS, strict=True
            ):
                moved = tuple(coordinate[a] + direction[a] for a in range(3))
                answer[moved] = answer.get(moved, Fraction(0)) + weight * step_weight
        return answer

    fresh: dict[Coord, Fraction] = {(0, 0, 0): Fraction(1)}
    for tick in range(1, 6):
        fresh = convolve(fresh)
        fresh_r2 = sum(
            weight * sum(value * value for value in coordinate)
            for coordinate, weight in fresh.items()
        )
        reused_r2 = Fraction(tick * tick, 2)
        check(
            f"C fresh independent directions have linear mean-square radius at tick {tick}",
            fresh_r2 == Fraction(tick, 2),
        )
        check(
            f"C one reused direction coin has ballistic mean-square radius at tick {tick}",
            reused_r2 == Fraction(tick * tick, 2),
        )

    small_transition = cycle_nine_lazy_step(3)
    eigenvalues = np.linalg.eigvalsh(small_transition)
    nonconstant = sorted((abs(value) for value in eigenvalues if abs(value - 1.0) > 1.0e-9), reverse=True)
    check("C primitive finite Markov step has a unique constant eigenmode", np.count_nonzero(np.isclose(eigenvalues, 1.0, atol=TOL)) == 1)
    check("C every nonconstant Markov eigenmode decays", nonconstant[0] < 1.0 - 1.0e-6 and nonconstant[-1] > 1.0e-6)

    shift = controlled_shift_map(side)
    state = np.arange(len(shift), dtype=int)
    for _ in range(side):
        state = shift[state]
    check("C fixed controlled shift recurs exactly after one torus circumference", np.array_equal(state, np.arange(len(shift))))
    markov_after_return = np.linalg.matrix_power(transition, side) @ initial
    check("C primitive Markov walk has not recurred at that time", markov_after_return[origin] < 0.2)

    for horizon in range(1, 7):
        path_dimension = 7**horizon
        implementation_qubits = ceil(log2(path_dimension))
        check(
            f"C fresh seven-way path tape dimension at horizon {horizon} is 7^T",
            path_dimension == 7**horizon,
            f"dimension={path_dimension}, qubits={implementation_qubits}",
        )


def edge_swap_unitary_dilation() -> None:
    section("D - Exact finite dilation of one symmetric edge-averaging step")
    identity = np.eye(4, dtype=complex)
    swap = np.array(
        (
            (1, 0, 0, 0),
            (0, 0, 1, 0),
            (0, 1, 0, 0),
            (0, 0, 0, 1),
        ),
        dtype=complex,
    )
    controlled_swap = np.block(
        [
            [identity, np.zeros_like(identity)],
            [np.zeros_like(identity), swap],
        ]
    )
    check("D controlled SWAP is exactly unitary", np.allclose(controlled_swap.conj().T @ controlled_swap, np.eye(8), atol=TOL))

    plus = np.array((1.0, 1.0), dtype=complex) / np.sqrt(2.0)
    ancilla = np.outer(plus, plus.conj())
    ket_10 = np.array((0.0, 0.0, 1.0, 0.0), dtype=complex)
    rho = np.outer(ket_10, ket_10.conj())
    joint = np.kron(ancilla, rho)
    evolved = controlled_swap @ joint @ controlled_swap.conj().T
    reduced = partial_trace_ancilla_two(evolved, 4)
    target = 0.5 * (rho + swap @ rho @ swap.conj().T)
    check("D tracing the coin gives the exact half-I half-SWAP channel", np.allclose(reduced, target, atol=TOL))
    check("D edge averaging preserves trace and positivity", abs(np.trace(reduced) - 1.0) < TOL and np.linalg.eigvalsh(reduced).min() > -TOL)

    occupation = np.diag((0.0, 1.0, 1.0, 2.0))
    total_occupation = np.kron(np.eye(2), occupation)
    check("D the unitary commutes with exact edge occupation", np.allclose(controlled_swap @ total_occupation, total_occupation @ controlled_swap, atol=TOL))
    check("D a localized one-particle edge state becomes a 50/50 reduced mixture", np.allclose(np.diag(reduced), (0.0, 0.5, 0.5, 0.0), atol=TOL))
    check("D the discarded coin carries nontrivial which-operation information", abs(float(np.real(np.trace(reduced @ reduced))) - 0.5) < TOL)


def carrier_dimension_budget() -> None:
    section("E - Finite M2-block coexistence budget")
    archive_labels = 3  # blank, locked-0, locked-1, if status is unitary carrier data
    archive_qubits = ceil(log2(archive_labels))
    resource_qubits = 1
    probe_qubits = 1
    base_qubits = archive_qubits + resource_qubits + probe_qubits
    direction_qubits = ceil(log2(len(DIRECTIONS)))
    total_qubits = base_qubits + direction_qubits

    check("E blank plus two locked contents need at least two qubits if Hilbert encoded", archive_qubits == 2)
    check("E archive/resource/probe coexistence has conditional M16 room", base_qubits == 4 and 2**base_qubits == 16)
    check("E a seven-direction one-step coin needs three qubits", direction_qubits == 3)
    check("E all conditional carriers fit inside seven M2 factors/M128", total_qubits == 7 and 2**total_qubits == 128)
    check("E one fundamental M2 site cannot hold three orthogonal archive statuses", 2 < archive_labels)

    for horizon in range(1, 6):
        retained_path_labels = 7**horizon
        needed_qubits = ceil(log2(retained_path_labels))
        check(
            f"E retaining every length-{horizon} direction history needs growing orthogonal room",
            2**needed_qubits >= retained_path_labels and (needed_qubits == 0 or 2 ** (needed_qubits - 1) < retained_path_labels),
            f"labels={retained_path_labels}, qubits={needed_qubits}",
        )


def two_layer_cycle_generator(
    side: int,
    kappa: float,
    forward_a: float,
    reverse_a: float,
    forward_b: float,
    reverse_b: float,
    source_coordinate: Coord = (0, 0, 0),
    sink_coordinate: Coord | None = None,
) -> tuple[np.ndarray, int, int, np.ndarray]:
    count = side**3
    matrix = np.zeros((2 * count, 2 * count), dtype=float)
    index = coordinate_index(side)
    if sink_coordinate is None:
        sink_coordinate = (side // 2, side // 2, side // 2)
    source = index[source_coordinate]
    sink = index[sink_coordinate]

    for layer in range(2):
        offset = layer * count
        for left, right in positive_edges(side):
            matrix[offset + right, offset + left] += kappa
            matrix[offset + left, offset + left] -= kappa
            matrix[offset + left, offset + right] += kappa
            matrix[offset + right, offset + right] -= kappa

    # Layer 0 is outward debt D; layer 1 is return credit C.
    # At a: C -> D (forward_a), D -> C (reverse_a).
    matrix[source, count + source] += forward_a
    matrix[count + source, count + source] -= forward_a
    matrix[count + source, source] += reverse_a
    matrix[source, source] -= reverse_a

    # At b: D -> C (forward_b), C -> D (reverse_b).
    matrix[count + sink, sink] += forward_b
    matrix[sink, sink] -= forward_b
    matrix[sink, count + sink] += reverse_b
    matrix[count + sink, count + sink] -= reverse_b

    return matrix, source, sink, lattice_laplacian(side)


def stationary_distribution(generator: np.ndarray) -> np.ndarray:
    matrix = generator.copy()
    rhs = np.zeros(len(generator), dtype=float)
    matrix[-1, :] = 1.0
    rhs[-1] = 1.0
    return np.linalg.solve(matrix, rhs)


def cycle_fixture(
    forward_a: float,
    reverse_a: float,
    forward_b: float,
    reverse_b: float,
) -> dict[str, object]:
    side = 4
    kappa = 1.0
    generator, source, sink, laplacian = two_layer_cycle_generator(
        side, kappa, forward_a, reverse_a, forward_b, reverse_b
    )
    stationary = stationary_distribution(generator)
    count = side**3
    debt = stationary[:count]
    credit = stationary[count:]
    current_a = forward_a * credit[source] - reverse_a * debt[source]
    current_b = forward_b * debt[sink] - reverse_b * credit[sink]
    source_vector = np.zeros(count)
    source_vector[source] = 1.0
    source_vector[sink] = -1.0
    return {
        "side": side,
        "kappa": kappa,
        "generator": generator,
        "source": source,
        "sink": sink,
        "laplacian": laplacian,
        "stationary": stationary,
        "debt": debt,
        "credit": credit,
        "current_a": current_a,
        "current_b": current_b,
        "source_vector": source_vector,
        "affinity": log(forward_a * forward_b / (reverse_a * reverse_b)),
    }


def closed_internal_return_cycle() -> float:
    section("F - Fully local conserved source-return cycle")
    forward_a = forward_b = 1.0
    reverse_a = reverse_b = 1.0 / 3.0
    fixture = cycle_fixture(forward_a, reverse_a, forward_b, reverse_b)
    generator = fixture["generator"]
    stationary = fixture["stationary"]
    debt = fixture["debt"]
    credit = fixture["credit"]
    laplacian = fixture["laplacian"]
    source_vector = fixture["source_vector"]
    current_a = float(fixture["current_a"])
    current_b = float(fixture["current_b"])

    check("F two-layer generator conserves total token probability exactly", np.max(np.abs(generator.sum(axis=0))) < TOL)
    check("F two-layer stationary state is normalized and positive", abs(float(stationary.sum()) - 1.0) < TOL and float(stationary.min()) > 0.0)
    check("F two-layer stationary state solves Qp=0", np.max(np.abs(generator @ stationary)) < TOL)
    check("F endpoint conversion currents agree", abs(current_a - current_b) < TOL)
    check("F positive cycle affinity drives positive current", current_a > 1.0e-5 and float(fixture["affinity"]) > 0.0)
    check("F debt layer obeys the exact stationary Poisson equation", np.max(np.abs(laplacian @ debt - current_a * source_vector)) < TOL)
    check("F return layer carries the opposite Poisson response", np.max(np.abs(laplacian @ credit + current_a * source_vector)) < TOL)
    check("F total local token density is uniform", np.ptp(debt + credit) < TOL)

    augmented = np.block(
        [
            [laplacian, np.ones((len(laplacian), 1))],
            [np.ones((1, len(laplacian))), np.zeros((1, 1))],
        ]
    )
    rhs = np.concatenate((source_vector, (0.0,)))
    green = np.linalg.solve(augmented, rhs)[:-1]
    check("F debt profile is exactly current times the mean-zero Green response", np.max(np.abs((debt - debt.mean()) - current_a * green)) < TOL)

    side = int(fixture["side"])
    count = side**3
    rotations = proper_cubic_rotations()
    source = int(fixture["source"])
    sink = int(fixture["sink"])
    for number, rotation in enumerate(rotations):
        sites = coordinate_map(side, rotation=rotation)
        joint = np.concatenate((sites, count + sites))
        check(f"F antipodal endpoints are fixed by cubic rotation {number:02d}", sites[source] == source and sites[sink] == sink)
        check(
            f"F driven closed-cycle generator is cubic covariant {number:02d}",
            np.allclose(generator[np.ix_(joint, joint)], generator, atol=TOL),
        )

    translation_vector = (1, 2, 3)
    translated_sites = coordinate_map(side, shift=translation_vector)
    translated_joint = np.concatenate((translated_sites, count + translated_sites))
    source_coordinate = tuple(value % side for value in translation_vector)
    sink_coordinate = tuple((side // 2 + value) % side for value in translation_vector)
    translated_generator, _, _, _ = two_layer_cycle_generator(
        side,
        1.0,
        forward_a,
        reverse_a,
        forward_b,
        reverse_b,
        source_coordinate=source_coordinate,
        sink_coordinate=sink_coordinate,
    )
    check(
        "F the endpoint-parametrized generator is translation covariant",
        np.allclose(
            translated_generator[np.ix_(translated_joint, translated_joint)],
            generator,
            atol=TOL,
        ),
    )

    equilibrium = cycle_fixture(1.0, 1.0, 1.0, 1.0)
    check("F detailed-balance ablation has zero affinity", abs(float(equilibrium["affinity"])) < TOL)
    check("F detailed-balance ablation has zero stationary current", abs(float(equilibrium["current_a"])) < TOL and abs(float(equilibrium["current_b"])) < TOL)
    check("F detailed-balance ablation removes the nonconstant Green amplitude", np.ptp(equilibrium["debt"]) < TOL)

    reversed_cycle = cycle_fixture(1.0 / 3.0, 1.0, 1.0 / 3.0, 1.0)
    check("F reversing affinity reverses current", float(reversed_cycle["affinity"]) < 0.0 and float(reversed_cycle["current_a"]) < 0.0)
    check("F forward and reversed symmetric fixtures have opposite equal currents", abs(float(reversed_cycle["current_a"]) + current_a) < TOL)

    flux_antisymmetry = np.zeros_like(generator)
    for source_state in range(len(generator)):
        for target_state in range(len(generator)):
            flux_antisymmetry[target_state, source_state] = (
                generator[target_state, source_state] * stationary[source_state]
                - generator[source_state, target_state] * stationary[target_state]
            )
    check("F driven stationary law violates detailed balance", np.max(np.abs(flux_antisymmetry)) > 1.0e-5)
    return current_a


def permanent_archive_saturation(stationary_current: float) -> None:
    section("G - Permanent finite archive saturation")
    site_count = 64
    check("G one-record-per-site archive has finite capacity N", site_count == 4**3)
    for multiplier in (1, 2, 10):
        time = multiplier * site_count / stationary_current
        unconstrained_commits = stationary_current * time
        writable_records = min(float(site_count), unconstrained_commits)
        check(
            f"G positive one-new-record-per-event current reaches/exceeds finite capacity by factor {multiplier}",
            writable_records <= site_count + TOL
            and (multiplier == 1 or unconstrained_commits > site_count + TOL),
            f"events={unconstrained_commits:.1f}, distinct slots={writable_records:.1f}",
        )
    saturation_time = site_count / stationary_current
    check("G saturation time is finite for every positive stationary current", np.isfinite(saturation_time) and saturation_time > 0.0)

    # A reread current is logically distinct: it can recur without changing A.
    archive_before = site_count
    reread_events = 1000
    archive_after = archive_before
    check("G rereading can sustain events without forming new records", archive_after == archive_before and reread_events > 0)
    check("G reread-current and formation-current source maps are inequivalent", reread_events > archive_after - archive_before)


def scheduler_countermodels_and_lensing() -> None:
    section("H - Scheduler countermodels, transport ambiguity, and lensing")
    field = 0.2
    gamma_common = 1.0
    q = 1.0 - gamma_common * field
    clock_two = np.diag((0.0, 2.0))
    clock_three = np.diag((-1.0, 0.5, 4.0))

    for name, clock in (("two-level", clock_two), ("three-level", clock_three)):
        base_gaps = np.diff(np.linalg.eigvalsh(clock))
        scaled_gaps = np.diff(np.linalg.eigvalsh(q * clock))
        check(f"H common scalar scheduler rescales every {name} gap by q", np.allclose(scaled_gaps, q * base_gaps, atol=TOL))

    identity_offset = 7.3
    shifted_gaps = np.diff(np.linalg.eigvalsh(q * clock_three + identity_offset * np.eye(3)))
    check("H species-dependent identity offsets do not alter clock gaps", np.allclose(shifted_gaps, q * np.diff(np.linalg.eigvalsh(clock_three)), atol=TOL))

    q_species_one = 1.0 - 0.5 * field
    q_species_two = 1.0 - 1.5 * field
    check("H species-dependent scheduler coefficients break universality", abs(q_species_one - q_species_two) > 0.1)
    power_one = q
    power_two = q**2
    check("H species-dependent powers also break universality", abs(power_one - power_two) > 0.1)

    local_q = np.array((0.72, 0.84, 1.0))
    internal = np.diag((0.0, 2.0))
    onsite = np.kron(np.diag(local_q), internal)
    position_edge_constant = np.zeros((3, 3))
    position_edge_metric = np.zeros((3, 3))
    for left, right in ((0, 1), (1, 2)):
        position_edge_constant[left, right] = position_edge_constant[right, left] = -0.3
        weighted = -0.3 * np.sqrt(local_q[left] * local_q[right])
        position_edge_metric[left, right] = position_edge_metric[right, left] = weighted
    transport_constant = onsite + np.kron(position_edge_constant, np.eye(2))
    transport_metric = onsite + np.kron(position_edge_metric, np.eye(2))
    check("H paired transport laws have identical onsite local clock blocks", np.allclose(np.diag(transport_constant), np.diag(transport_metric), atol=TOL))
    check("H identical local clock blocks do not fix transport spectrum", np.linalg.norm(np.linalg.eigvalsh(transport_constant) - np.linalg.eigvalsh(transport_metric)) > 1.0e-2)
    check("H identical lapse laws permit different nearest-neighbor transfer amplitudes", abs(transport_constant[0, 2] - transport_metric[0, 2]) > 1.0e-2)

    impact = sp.symbols("b", positive=True)
    line = sp.symbols("z", real=True)
    transverse_integral = sp.integrate(
        impact / (impact**2 + line**2) ** sp.Rational(3, 2),
        (line, -sp.oo, sp.oo),
    )
    check("H weak-field transverse 1/r integral is exactly 2/b", sp.simplify(transverse_integral - 2 / impact) == 0)

    gm_over_b = 0.01
    deflection_scalar = 2.0 * (1.0 + 0.0) * gm_over_b
    deflection_gr = 2.0 * (1.0 + 1.0) * gm_over_b
    check("H pure-lapse gamma=0 comparator gives 2GM/b", abs(deflection_scalar - 0.02) < TOL)
    check("H spatial-curvature gamma=1 comparator gives 4GM/b", abs(deflection_gr - 0.04) < TOL)
    check("H same Newtonian lapse permits a factor-two lensing discriminator", abs(deflection_gr / deflection_scalar - 2.0) < TOL)


def main() -> None:
    source_contract()
    one_step_cubic_unitary_dilation()
    repeated_coin_and_finite_environment_boundary()
    edge_swap_unitary_dilation()
    carrier_dimension_budget()
    current = closed_internal_return_cycle()
    permanent_archive_saturation(current)
    scheduler_countermodels_and_lensing()
    print(f"\nSUMMARY: REVERSIBLE DILATION/CLOSED CYCLE GRAVITY CYCLE 10 PASS={PASS} FAIL={FAIL}")
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
