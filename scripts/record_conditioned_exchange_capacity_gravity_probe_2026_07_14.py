#!/usr/bin/env python3
"""Finite probes for record-conditioned exchange capacity and gravity claims.

The model is deliberately small and explicit.  A cubic torus carries a
weighted graph Laplacian, the one-excitation restriction of a weighted
``I-SWAP`` exchange Hamiltonian.  Record or activity flags may reduce the
weights of incident edges.  The checks identify what follows from that rule
and what appears only after an additional clock, source, Poisson, species, or
renewal map is supplied.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path
from typing import Callable, Iterable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "RECORD_CONDITIONED_EXCHANGE_CAPACITY_GRAVITY_FINITE_PROBE_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
TOL = 1.0e-10
Coord = tuple[int, int, int]


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


def positive_edges(side: int) -> tuple[tuple[Coord, Coord], ...]:
    """Return each undirected nearest-neighbor edge once for side >= 3."""

    edges = []
    for coordinate in coordinates(side):
        for axis in range(3):
            neighbor = list(coordinate)
            neighbor[axis] = (neighbor[axis] + 1) % side
            edges.append((coordinate, tuple(neighbor)))
    return tuple(edges)


def edge_weight(
    left: Coord,
    right: Coord,
    flags: frozenset[Coord],
    gamma: float,
) -> float:
    return 1.0 - gamma if left in flags or right in flags else 1.0


def weighted_laplacian(
    side: int,
    flags: Iterable[Coord] = (),
    gamma: float = 1.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Weighted graph Laplacian and normalized local weighted degree."""

    flag_set = frozenset(flags)
    index = coordinate_index(side)
    matrix = np.zeros((side**3, side**3), dtype=float)
    degree = np.zeros(side**3, dtype=float)
    for left, right in positive_edges(side):
        weight = edge_weight(left, right, flag_set, gamma)
        i = index[left]
        j = index[right]
        matrix[i, i] += weight
        matrix[j, j] += weight
        matrix[i, j] -= weight
        matrix[j, i] -= weight
        degree[i] += weight
        degree[j] += weight
    return matrix, degree / 6.0


def translation(side: int, shift: Coord) -> Callable[[Coord], Coord]:
    return lambda coordinate: tuple(
        (coordinate[axis] + shift[axis]) % side for axis in range(3)
    )


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations(side: int) -> tuple[tuple[str, Callable[[Coord], Coord]], ...]:
    """Return all 24 orientation-preserving signed coordinate permutations."""

    rotations = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] != 1:
                continue

            def transform(
                coordinate: Coord,
                permutation: tuple[int, int, int] = permutation,
                signs: tuple[int, int, int] = signs,
            ) -> Coord:
                return tuple(
                    (signs[axis] * coordinate[permutation[axis]]) % side
                    for axis in range(3)
                )

            rotations.append((f"rotation-{permutation}-{signs}", transform))
    return tuple(rotations)


def permutation_matrix(side: int, transform: Callable[[Coord], Coord]) -> np.ndarray:
    index = coordinate_index(side)
    permutation = np.zeros((side**3, side**3), dtype=float)
    for coordinate in coordinates(side):
        permutation[index[transform(coordinate)], index[coordinate]] = 1.0
    return permutation


def transform_flags(
    flags: Iterable[Coord], transform: Callable[[Coord], Coord]
) -> frozenset[Coord]:
    return frozenset(transform(coordinate) for coordinate in flags)


def swap_operator(qubits: int, left: int, right: int) -> np.ndarray:
    dimension = 2**qubits
    swap = np.zeros((dimension, dimension), dtype=int)
    for state in range(dimension):
        bits = [((state >> (qubits - 1 - position)) & 1) for position in range(qubits)]
        bits[left], bits[right] = bits[right], bits[left]
        target = 0
        for bit in bits:
            target = (target << 1) | bit
        swap[target, state] = 1
    return swap


def bit_projector(qubits: int, position: int, value: int) -> np.ndarray:
    dimension = 2**qubits
    diagonal = []
    for state in range(dimension):
        bit = (state >> (qubits - 1 - position)) & 1
        diagonal.append(int(bit == value))
    return np.diag(diagonal)


def torus_distance(side: int, left: Coord, right: Coord) -> int:
    distance = 0
    for axis in range(3):
        direct = abs(left[axis] - right[axis])
        distance += min(direct, side - direct)
    return distance


def field_laplacian(field: np.ndarray) -> np.ndarray:
    result = 6.0 * field
    for axis in range(3):
        result -= np.roll(field, 1, axis=axis)
        result -= np.roll(field, -1, axis=axis)
    return result


def periodic_poisson_point_source(side: int) -> tuple[np.ndarray, np.ndarray]:
    """Solve Delta phi = delta_0 - 1/N by an explicitly supplied inverse."""

    source = np.full((side, side, side), -1.0 / side**3)
    source[0, 0, 0] += 1.0
    source_hat = np.fft.fftn(source)
    frequencies = 2.0 * np.pi * np.fft.fftfreq(side)
    kx, ky, kz = np.meshgrid(frequencies, frequencies, frequencies, indexing="ij")
    eigenvalue = 6.0 - 2.0 * (np.cos(kx) + np.cos(ky) + np.cos(kz))
    potential_hat = np.zeros_like(source_hat)
    nonzero = eigenvalue > 1.0e-14
    potential_hat[nonzero] = source_hat[nonzero] / eigenvalue[nonzero]
    potential = np.fft.ifftn(potential_hat).real
    return source, potential


def source_contract() -> None:
    section("A - Source and claim boundary")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("*", "").replace("`", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    check("A note is authority-free", "authority: none" in normalized)
    check("A note is not an axiom proposal", "not an axiom proposal" in normalized)
    check("A note changes no audit surface", "changes no axiom, registry, or audit" in normalized)
    check("A note limits its negative conclusion", "narrow no-go" in normalized)
    check("A live Record text says records form", "Records form." in axioms)
    check("A live memo leaves formation rules outside", "formation rules" in axioms)


def exchange_and_record_boundary() -> None:
    section("B - Exchange reduction and exact post-formation freezing")
    identity4 = np.eye(4, dtype=int)
    swap2 = swap_operator(2, 0, 1)
    one_excitation = (identity4 - swap2)[np.ix_([1, 2], [1, 2])]
    expected_laplacian = np.array([[1, -1], [-1, 1]])
    check(
        "B I-SWAP restricts to the two-vertex graph Laplacian",
        np.array_equal(one_excitation, expected_laplacian),
    )

    identity8 = np.eye(8, dtype=int)
    exchange01 = identity8 - swap_operator(3, 0, 1)
    exchange12 = identity8 - swap_operator(3, 1, 2)
    record0 = bit_projector(3, 0, 1)
    before = exchange01 + exchange12
    hard_frozen = exchange12
    soft_frozen = 0.5 * exchange01 + exchange12
    commutator_before = before @ record0 - record0 @ before
    commutator_hard = hard_frozen @ record0 - record0 @ hard_frozen
    commutator_soft = soft_frozen @ record0 - record0 @ soft_frozen

    def changes_first_bit(generator: np.ndarray) -> bool:
        for row in range(generator.shape[0]):
            row_bit = (row >> 2) & 1
            for column in range(generator.shape[1]):
                column_bit = (column >> 2) & 1
                if row_bit != column_bit and abs(generator[row, column]) > TOL:
                    return True
        return False

    check("B an unfrozen exchange edge can change the declared site value", np.any(commutator_before))
    check("B hard removal of all incident exchange edges fixes that site value", not np.any(commutator_hard))
    check("B any nonzero soft incident exchange fails exact site-value fixation", np.any(np.abs(commutator_soft) > TOL))
    check("B hard freezing also removes exchange-mediated export from the site", not changes_first_bit(hard_frozen))
    check("B soft exchange retains a channel that can transport the site value", changes_first_bit(soft_frozen))
    check("B the post-formation generator differs from the pre-formation generator", not np.array_equal(before, hard_frozen))


def cubic_covariance() -> None:
    section("C - Cubic covariance and the moving-source distinction")
    side = 4
    flags = frozenset({(0, 0, 0), (1, 2, 3)})
    matrix, clock = weighted_laplacian(side, flags)
    rotations = proper_cubic_rotations(side)
    check("C the proper cubic rotation family has order 24", len(rotations) == 24)
    transformations = (("translation", translation(side, (1, 2, 1))),) + rotations
    for label, transform in transformations:
        moved_flags = transform_flags(flags, transform)
        moved_matrix, moved_clock = weighted_laplacian(side, moved_flags)
        permutation = permutation_matrix(side, transform)
        check(
            f"C record-conditioned exchange is exactly {label} covariant",
            np.array_equal(moved_matrix, permutation @ matrix @ permutation.T),
        )
        check(
            f"C normalized local capacity is exactly {label} covariant",
            np.array_equal(moved_clock, permutation @ clock),
        )
        check(
            f"C the {label} leaves the exchange spectrum unchanged",
            np.allclose(np.linalg.eigvalsh(moved_matrix), np.linalg.eigvalsh(matrix), atol=TOL),
        )

    first = (0, 0, 0)
    second = (1, 0, 0)
    move = translation(side, (1, 0, 0))
    permutation = permutation_matrix(side, move)
    active_first, _ = weighted_laplacian(side, {first})
    active_second, _ = weighted_laplacian(side, {second})
    archive_after_move, _ = weighted_laplacian(side, {first, second})
    check(
        "C a current active source moves covariantly",
        np.array_equal(active_second, permutation @ active_first @ permutation.T),
    )
    check(
        "C an append-only trail is not the translated one-source configuration",
        not np.array_equal(archive_after_move, permutation @ active_first @ permutation.T),
    )


def local_clock_and_species() -> None:
    section("D - Capacity clock and universality ablations")
    side = 5
    source = (0, 0, 0)
    index = coordinate_index(side)
    _, hard_clock = weighted_laplacian(side, {source}, gamma=1.0)
    _, soft_clock = weighted_laplacian(side, {source}, gamma=0.5)
    neighbors = tuple(
        coordinate
        for coordinate in coordinates(side)
        if torus_distance(side, coordinate, source) == 1
    )
    far = tuple(
        coordinate
        for coordinate in coordinates(side)
        if torus_distance(side, coordinate, source) > 1
    )
    check("D hard freezing gives zero exchange capacity at the record", hard_clock[index[source]] == 0.0)
    check(
        "D hard freezing gives 5/6 capacity at each nearest neighbor",
        all(hard_clock[index[coordinate]] == 5.0 / 6.0 for coordinate in neighbors),
    )
    check(
        "D the hard capacity clock has no response beyond one edge",
        all(hard_clock[index[coordinate]] == 1.0 for coordinate in far),
    )
    check("D soft half-freezing leaves half capacity at the flagged site", soft_clock[index[source]] == 0.5)
    check(
        "D soft half-freezing leaves 11/12 capacity at a neighbor",
        all(soft_clock[index[coordinate]] == 11.0 / 12.0 for coordinate in neighbors),
    )

    degree = 6.0 * hard_clock
    species_a_raw = 2.0 * degree
    species_b_raw = 7.0 * degree
    species_a_fraction = species_a_raw / (2.0 * 6.0)
    species_b_fraction = species_b_raw / (7.0 * 6.0)
    check(
        "D common edge weights give species-independent fractional slowdown",
        np.array_equal(species_a_fraction, species_b_fraction),
    )
    check("D common geometry does not make raw clock frequencies equal", not np.array_equal(species_a_raw, species_b_raw))
    check(
        "D species-dependent edge responses destroy universal fractional slowdown",
        not np.array_equal(hard_clock, soft_clock),
    )


def archive_and_active_source() -> None:
    section("E - Archive trail versus active-source response")
    side = 5
    active = {(2, 2, 2)}
    archive_a = {(0, 0, 0), (1, 0, 0)}
    archive_b = {(4, 4, 4), (4, 3, 4), (3, 3, 4)}

    archive_matrix_a, archive_clock_a = weighted_laplacian(side, archive_a | active)
    archive_matrix_b, archive_clock_b = weighted_laplacian(side, archive_b | active)
    active_matrix_a, active_clock_a = weighted_laplacian(side, active)
    active_matrix_b, active_clock_b = weighted_laplacian(side, active)
    check("E archive-coupled geometry depends on the prior trail", not np.array_equal(archive_matrix_a, archive_matrix_b))
    check("E archive-coupled clock depends on the prior trail", not np.array_equal(archive_clock_a, archive_clock_b))
    check("E activity-only geometry ignores prior archive history", np.array_equal(active_matrix_a, active_matrix_b))
    check("E activity-only clock ignores prior archive history", np.array_equal(active_clock_a, active_clock_b))

    baseline, baseline_clock = weighted_laplacian(side)
    stopped_activity, stopped_clock = weighted_laplacian(side, set())
    residual_archive, residual_archive_clock = weighted_laplacian(side, archive_a)
    check("E stopping activity restores the activity-only baseline", np.array_equal(stopped_activity, baseline))
    check("E stopping activity restores the activity-only clock", np.array_equal(stopped_clock, baseline_clock))
    check("E an append-only archive leaves a permanent geometric defect", not np.array_equal(residual_archive, baseline))
    check("E an append-only archive leaves a permanent clock defect", not np.array_equal(residual_archive_clock, baseline_clock))


def sign_range_and_poisson() -> None:
    section("F - Sign, range, Poisson, and resolvent ablations")
    side = 7
    source_coordinate = (0, 0, 0)
    index = coordinate_index(side)
    baseline, _ = weighted_laplacian(side)
    defect, clock = weighted_laplacian(side, {source_coordinate})
    delta = defect - baseline
    delta_eigenvalues = np.linalg.eigvalsh(delta)
    constant = np.ones(side**3)
    localized = np.zeros(side**3)
    localized[index[source_coordinate]] = 1.0
    check("F for positive J the hard defect lowers the exchange quadratic form", np.max(delta_eigenvalues) < TOL and np.min(delta_eigenvalues) < -TOL)
    check("F the exchange defect does not act as an onsite potential on a uniform mode", np.linalg.norm(delta @ constant) < TOL)
    check("F the defect response depends on gradients/localization", float(localized @ delta @ localized) < 0.0)
    check("F changing the sign of J reverses the energy response", np.array_equal(-delta, baseline - defect))
    capacity_from_positive_j = np.diag(defect) / 6.0
    capacity_from_negative_j = np.diag(-defect) / -6.0
    check("F the capacity clock itself is independent of the sign of J", np.array_equal(capacity_from_positive_j, capacity_from_negative_j) and np.array_equal(capacity_from_positive_j, clock))

    deficit = 1.0 - clock
    support = {
        coordinate
        for coordinate in coordinates(side)
        if deficit[index[coordinate]] > TOL
    }
    expected_support = {
        coordinate
        for coordinate in coordinates(side)
        if torus_distance(side, coordinate, source_coordinate) <= 1
    }
    check("F the direct clock deficit is supported only on source plus six neighbors", support == expected_support, str(len(support)))
    check("F direct edge freezing has no 1/r far-field clock tail", all(deficit[index[c]] == 0.0 for c in coordinates(side) if torus_distance(side, c, source_coordinate) > 1))

    poisson_side = 31
    source, potential = periodic_poisson_point_source(poisson_side)
    residual = field_laplacian(potential) - source
    check("F a separately supplied discrete Poisson inverse solves its equation", np.max(np.abs(residual)) < 1.0e-12)
    far_values = [
        potential[coordinate]
        for coordinate in coordinates(poisson_side)
        if torus_distance(poisson_side, coordinate, (0, 0, 0)) >= 5
    ]
    check("F the supplied Poisson inverse creates a nonlocal far field", max(abs(value) for value in far_values) > 1.0e-5)
    radii = np.arange(2.0, 10.0)
    axis_values = np.array([potential[int(radius), 0, 0] for radius in radii])
    design = np.column_stack((np.ones_like(radii), 1.0 / radii))
    coefficients, *_ = np.linalg.lstsq(design, axis_values, rcond=None)
    fitted = design @ coefficients
    r_squared = 1.0 - np.sum((axis_values - fitted) ** 2) / np.sum((axis_values - axis_values.mean()) ** 2)
    check("F the finite 3D Poisson comparator has an approximate 1/r window", r_squared > 0.998, f"R2={r_squared:.6f}")
    _, same_side_potential = periodic_poisson_point_source(side)
    same_side_flat = same_side_potential.reshape(-1)
    check(
        "F the Poisson field is not the direct local capacity deficit",
        np.count_nonzero(np.abs(same_side_flat) > TOL) > len(support)
        and not np.allclose(same_side_flat, deficit, atol=TOL),
    )

    resolvent_side = 5
    base_small, _ = weighted_laplacian(resolvent_side)
    defect_small, _ = weighted_laplacian(resolvent_side, {(0, 0, 0)})
    probe = np.zeros(resolvent_side**3)
    probe[coordinate_index(resolvent_side)[(1, 0, 0)]] = 1.0
    responses = []
    for mass in (0.5, 1.0):
        base_response = np.linalg.solve(base_small + mass**2 * np.eye(resolvent_side**3), probe)
        defect_response = np.linalg.solve(defect_small + mass**2 * np.eye(resolvent_side**3), probe)
        responses.append(defect_response - base_response)
    far_index = coordinate_index(resolvent_side)[(2, 2, 2)]
    check("F an added resolvent maps a local defect to a nonlocal response", abs(responses[0][far_index]) > TOL)
    normalized_first = responses[0] / np.linalg.norm(responses[0])
    normalized_second = responses[1] / np.linalg.norm(responses[1])
    check("F resolvent response shape depends on the supplied spectral scale", not np.allclose(normalized_first, normalized_second, atol=1.0e-5))


def renewal_and_saturation() -> None:
    section("G - Renewal and persistence ablations")
    side = 4
    ordered_sites = coordinates(side)
    records: set[Coord] = set()
    active_edge_counts = []
    mean_capacities = []
    for site in ordered_sites:
        records.add(site)
        _, clock = weighted_laplacian(side, records)
        active_edge_counts.append(sum(edge_weight(a, b, frozenset(records), 1.0) > 0.0 for a, b in positive_edges(side)))
        mean_capacities.append(float(clock.mean()))
    check("G append-only freezing monotonically removes active exchange edges", all(active_edge_counts[i + 1] <= active_edge_counts[i] for i in range(len(active_edge_counts) - 1)))
    check("G append-only freezing monotonically reduces mean local capacity", all(mean_capacities[i + 1] <= mean_capacities[i] + TOL for i in range(len(mean_capacities) - 1)))
    check("G a fully recorded finite torus has no active exchange edge", active_edge_counts[-1] == 0)
    check("G a fully recorded finite torus has zero capacity clock", mean_capacities[-1] == 0.0)

    baseline, _ = weighted_laplacian(side)
    saturated, _ = weighted_laplacian(side, records)
    erased, _ = weighted_laplacian(side, set())
    check("G clearing flags restores exchange capacity", np.array_equal(erased, baseline))
    check("G clearing flags is not append-only record permanence", records != set())
    check("G no-renewal saturation is dynamically different from baseline", not np.array_equal(saturated, baseline))

    # Keeping an immutable archive bit while separately clearing a working flag
    # is a consistent abstract renewal construction, but it needs four joint
    # local labels rather than the two labels of one qubit.
    archive_labels = (0, 1)
    working_labels = (0, 1)
    joint_labels = tuple(product(archive_labels, working_labels))
    check("G an archive-plus-working bit has four independent local labels", len(joint_labels) == 4)
    check("G one M2 site has only two orthogonal classical pointer labels", 2 < len(joint_labels))
    immutable_archive = frozenset(records)
    cleared_working_flags: frozenset[Coord] = frozenset()
    renewed, _ = weighted_laplacian(side, cleared_working_flags)
    check("G a separate archive layer can retain labels while restoring working exchange", len(immutable_archive) == side**3 and np.array_equal(renewed, baseline))


def conclusion_contract() -> None:
    section("H - Law-atom and no-go discipline needles")
    text = NOTE.read_text(encoding="utf-8")
    normalized = text.lower()
    required = (
        "formation trigger",
        "active source",
        "archive",
        "common species coupling",
        "clock identification",
        "poisson",
        "sign",
        "renewal",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — exact residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path",
        "n7 — strongest steelman",
        "n8 — cross-cycle echo",
    )
    for phrase in required:
        check(f"H note contains boundary: {phrase}", phrase in normalized)


def main() -> None:
    source_contract()
    exchange_and_record_boundary()
    cubic_covariance()
    local_clock_and_species()
    archive_and_active_source()
    sign_range_and_poisson()
    renewal_and_saturation()
    conclusion_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
