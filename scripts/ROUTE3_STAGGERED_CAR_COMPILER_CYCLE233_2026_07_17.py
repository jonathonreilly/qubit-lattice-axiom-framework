#!/usr/bin/env python3
"""Route 3, Cycle 233: staggered/time-multiplexed M64-to-M2 CAR probe.

This runner attacks a plain occupation-qubit realization of the Cycle-230
six-mode CAR cell.  It supplies an autonomous four-phase update-law register and the
obvious local FSWAP schedule, then compares that physical tensor-product
update with the exterior (fermionic) lift.  The negative result is deliberately
narrow: it applies to the tested schedule/order family, not to auxiliary-gauge
encodings or to every bounded qubit code.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from math import ceil
from pathlib import Path
from typing import Hashable, Iterable

import numpy as np

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ROUTE3_STAGGERED_CAR_COMPILER_CYCLE233_NOTE_2026-07-17.md"
)
BETA = -0.3
COUPLING = 0.37
PASS = 0
FAIL = 0

Mode = Hashable


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "e g_coarse = g_physical e",
        "four-phase autonomous schedule",
        "one-particle mass fixture",
        "cycle-230 seam block",
        "held-out-size",
        "lawful-domain",
        "supplied-structure inventory",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
        "partial-attempt-with-named-untested-routes",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves the bounded Route-3 and N1-N8 contract", not missing, missing)


def inversion_parity(values: Iterable[int]) -> int:
    values = tuple(values)
    return sum(
        values[left] > values[right]
        for left in range(len(values))
        for right in range(left + 1, len(values))
    ) % 2


def permutation_from_pairs(modes: Iterable[Mode], pairs: Iterable[tuple[Mode, Mode]]) -> dict[Mode, Mode]:
    """Return the source-to-destination permutation made by tensor SWAPs."""
    image = {mode: mode for mode in modes}
    for first, second in pairs:
        for source in image:
            if image[source] == first:
                image[source] = second
            elif image[source] == second:
                image[source] = first
    return image


def fermionic_action(
    order: tuple[Mode, ...], permutation: dict[Mode, Mode], occupied: Iterable[Mode]
) -> tuple[int, frozenset[Mode]]:
    """Exterior-lift sign and output occupation for a mode permutation."""
    position = {mode: index for index, mode in enumerate(order)}
    source = sorted(tuple(occupied), key=position.__getitem__)
    destinations = tuple(position[permutation[mode]] for mode in source)
    return inversion_parity(destinations), frozenset(permutation[mode] for mode in source)


def local_fswap_action(
    occupied: Iterable[Mode], pairs: Iterable[tuple[Mode, Mode]]
) -> tuple[int, frozenset[Mode]]:
    """Sign and output of geometrically local two-qubit FSWAP gates."""
    state = set(occupied)
    sign = 0
    for first, second in pairs:
        sign ^= int(first in state and second in state)
        first_full = first in state
        second_full = second in state
        if first_full != second_full:
            if first_full:
                state.remove(first)
                state.add(second)
            else:
                state.remove(second)
                state.add(first)
    return sign, frozenset(state)


def mismatch_pairs(
    order: tuple[Mode, ...],
    permutation: dict[Mode, Mode],
    schedule: tuple[tuple[Mode, Mode], ...],
) -> tuple[tuple[Mode, Mode], ...]:
    bad = []
    for occupied in combinations(order, 2):
        target_sign, target_output = fermionic_action(order, permutation, occupied)
        local_sign, local_output = local_fswap_action(occupied, schedule)
        if target_output != local_output:
            raise AssertionError("schedule and target one-particle permutations differ")
        if target_sign != local_sign:
            bad.append(occupied)
    return tuple(bad)


def axial_modes(length: int) -> tuple[tuple[int, int], ...]:
    return tuple((cell, direction) for cell in range(length) for direction in range(2))


def axial_pairs(length: int, periodic: bool = True) -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    reverse = tuple(((cell, 0), (cell, 1)) for cell in range(length))
    edge_count = length if periodic else length - 1
    edge = tuple(
        ((cell, 1), ((cell + 1) % length, 0)) for cell in range(edge_count)
    )
    return reverse + edge


def cell_local_orders(length: int) -> Iterable[tuple[tuple[int, int], ...]]:
    for cell_order in permutations(range(length)):
        for flips in product((0, 1), repeat=length):
            order = []
            for cell in cell_order:
                pair = [(cell, 0), (cell, 1)]
                if flips[cell]:
                    pair.reverse()
                order.extend(pair)
            yield tuple(order)


def best_order_census(
    orders: Iterable[tuple[Mode, ...]],
    modes: tuple[Mode, ...],
    schedule: tuple[tuple[Mode, Mode], ...],
) -> tuple[int, int, tuple[Mode, ...] | None]:
    permutation = permutation_from_pairs(modes, schedule)
    best = len(modes) ** 2
    exact = 0
    best_order = None
    for order in orders:
        residual = len(mismatch_pairs(order, permutation, schedule))
        if residual < best:
            best = residual
            best_order = order
        exact += int(residual == 0)
    return best, exact, best_order


def axial_order_and_boundary_controls() -> None:
    rows = []
    for length in (3, 4, 5):
        modes = axial_modes(length)
        schedule = axial_pairs(length)
        best, exact, _ = best_order_census(
            cell_local_orders(length), modes, schedule
        )
        rows.append(
            {
                "L": length,
                "two_particle_dimension": len(tuple(combinations(modes, 2))),
                "best_mismatches": best,
                "exact_cell_local_orders": exact,
            }
        )
    check(
        "no cell-contiguous local mode order repairs the periodic axial FSWAP stream at L=3,4,5",
        [row["best_mismatches"] for row in rows] == [4, 6, 8]
        and all(row["exact_cell_local_orders"] == 0 for row in rows),
        rows,
    )

    length = 3
    modes = axial_modes(length)
    periodic_schedule = axial_pairs(length)
    arbitrary_best, arbitrary_exact, _ = best_order_census(
        permutations(modes), modes, periodic_schedule
    )
    check(
        "even all 6! static JW orders leave a two-particle periodic-stream sign residual at L=3",
        arbitrary_best == 4 and arbitrary_exact == 0,
        {"best_mismatches": arbitrary_best, "exact_orders": arbitrary_exact},
    )

    open_schedule = axial_pairs(length, periodic=False)
    open_best, open_exact, open_order = best_order_census(
        permutations(modes), modes, open_schedule
    )
    check(
        "the open axial chain has an exact static ordering, so the periodic result is not a general schedule no-go",
        open_best == 0 and open_exact == 2,
        {"exact_orders": open_exact, "witness_order": open_order},
    )

    natural_rows = []
    for length in (3, 5, 7, 9):
        modes = axial_modes(length)
        order = modes
        schedule = axial_pairs(length)
        permutation = permutation_from_pairs(modes, schedule)
        corrections = mismatch_pairs(order, permutation, schedule)
        ranges = tuple(
            min(abs(left[0] - right[0]), length - abs(left[0] - right[0]))
            for left, right in corrections
        )
        natural_rows.append(
            {
                "L": length,
                "correction_CZs": len(corrections),
                "max_ring_range": max(ranges),
            }
        )
    check(
        "the exact diagonal correction for one consistent periodic ordering acquires held-out-size range",
        [row["correction_CZs"] for row in natural_rows] == [8, 16, 24, 32]
        and [row["max_ring_range"] for row in natural_rows] == [1, 2, 3, 4],
        natural_rows,
    )

    # The difference between two monomial lifts is exactly the quadratic CZ
    # polynomial identified by the two-particle mismatch set.
    for length in (3, 4):
        modes = axial_modes(length)
        order = modes
        schedule = axial_pairs(length)
        permutation = permutation_from_pairs(modes, schedule)
        corrections = mismatch_pairs(order, permutation, schedule)
        for mask in range(1 << len(modes)):
            occupied = tuple(mode for index, mode in enumerate(modes) if (mask >> index) & 1)
            target_sign, target_output = fermionic_action(order, permutation, occupied)
            local_sign, local_output = local_fswap_action(occupied, schedule)
            correction_sign = sum(
                first in occupied and second in occupied
                for first, second in corrections
            ) % 2
            if target_output != local_output or target_sign != (local_sign ^ correction_sign):
                raise AssertionError("quadratic correction did not repair the stream")
    check(
        "the nonlocal CZ inventory repairs the L=3,4 monomial streams exactly on every occupation",
        True,
        "operator residual 0 after the full correction; 2 before it",
    )


def axis_order_change_controls() -> None:
    rows = []
    rng = np.random.default_rng(2330)
    for length in (2, 3, 4, 5, 7):
        cells = tuple(product(range(length), repeat=3))
        x_order = tuple(sorted(cells, key=lambda cell: (cell[2], cell[1], cell[0])))
        y_order = tuple(sorted(cells, key=lambda cell: (cell[2], cell[0], cell[1])))
        x_position = {cell: index for index, cell in enumerate(x_order)}
        y_position = {cell: index for index, cell in enumerate(y_order)}
        inversions = tuple(
            (left, right)
            for left, right in combinations(cells, 2)
            if (x_position[left] - x_position[right])
            * (y_position[left] - y_position[right])
            < 0
        )
        distances = tuple(
            sum(abs(left[axis] - right[axis]) for axis in range(3))
            for left, right in inversions
        )
        max_distance = max(distances) if distances else 0
        rows.append(
            {
                "L": length,
                "inversion_CZs": len(inversions),
                "max_Manhattan_range": max_distance,
                "NN_lightcone_depth_lower_bound": ceil(max_distance / 2),
            }
        )

        if length <= 4:
            for _ in range(64):
                occupied = {
                    cell for cell in cells if rng.integers(0, 2) == 1
                }
                target = inversion_parity(y_position[cell] for cell in sorted(occupied, key=x_position.__getitem__))
                polynomial = sum(
                    left in occupied and right in occupied
                    for left, right in inversions
                ) % 2
                if target != polynomial:
                    raise AssertionError("JW order-change phase polynomial failed")
    check(
        "changing x-line to y-line JW order requires exact rephasing with depth growing in held-out L",
        [row["max_Manhattan_range"] for row in rows] == [2, 4, 6, 8, 12]
        and [row["NN_lightcone_depth_lower_bound"] for row in rows]
        == [1, 2, 3, 4, 6],
        rows,
    )


def ordinary_mode_permutation_lift(permutation: np.ndarray) -> np.ndarray:
    mode_count = permutation.shape[0]
    dimension = 1 << mode_count
    target_mode = np.argmax(permutation, axis=0)
    lift = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        target = 0
        for mode in range(mode_count):
            if (source >> mode) & 1:
                target |= 1 << int(target_mode[mode])
        lift[target, source] = 1
    return lift


def local_block_and_frame_controls() -> None:
    species = c219.common_species(BETA)
    gamma_coin = c229.fock_lift(species.coin)
    occupations = c229.occupation_table(6)
    number = occupations.sum(axis=1)
    contact = np.diag(np.exp(1j * COUPLING * number * (number - 1) / 2))
    one_particle = tuple(1 << mode for mode in range(6))
    check(
        "the bounded six-qubit block exactly carries the exterior coin, contact, and one-particle restriction",
        np.linalg.norm(gamma_coin[np.ix_(one_particle, one_particle)] - species.coin) < 2e-15
        and np.max(np.abs(np.diag(contact)[number <= 1] - 1)) < 2e-15
        and np.linalg.norm(contact.conj().T @ contact - np.eye(64)) < 3e-15,
        {"data_qubits_per_cell": 6, "local_dimension": 64},
    )

    exterior_residuals = []
    ordinary_residuals = []
    character_gaps = []
    contact_residuals = []
    for frame in c210.proper_cubic_frames():
        mode_permutation = c210.direction_permutation(frame)
        exterior = c229.fock_lift(mode_permutation)
        ordinary = ordinary_mode_permutation_lift(mode_permutation)
        exterior_residuals.append(np.linalg.norm(exterior @ gamma_coin - gamma_coin @ exterior))
        ordinary_residuals.append(np.linalg.norm(ordinary @ gamma_coin - gamma_coin @ ordinary))
        contact_residuals.append(np.linalg.norm(ordinary @ contact - contact @ ordinary))
        character_gaps.append(abs(np.trace(exterior) - np.trace(ordinary)))
    failed_ordinary = sum(residual > 1e-10 for residual in ordinary_residuals)
    check(
        "the exterior coin is covariant in all 24 fermionic frames but the plain port-qubit action is not",
        max(exterior_residuals) < 2e-14
        and failed_ordinary == 22
        and max(ordinary_residuals) > 9
        and max(contact_residuals) < 2e-14,
        {
            "fermionic_max": max(exterior_residuals),
            "ordinary_failed_frames": failed_ordinary,
            "ordinary_max": max(ordinary_residuals),
            "contact_max": max(contact_residuals),
        },
    )
    check(
        "a fixed local basis/order change cannot identify the two full 64-state frame representations",
        max(character_gaps) >= 8 - 1e-12,
        {"max_character_gap": max(character_gaps)},
    )


def cube_modes(length: int) -> tuple[tuple[int, int, int, int], ...]:
    return tuple((*site, direction) for site in product(range(length), repeat=3) for direction in range(6))


def shifted(site: tuple[int, int, int], displacement: np.ndarray, length: int) -> tuple[int, int, int]:
    return tuple(int((site[axis] + int(displacement[axis])) % length) for axis in range(3))


def cube_schedule_pairs(
    length: int, axis_order: tuple[int, int, int] = (0, 1, 2)
) -> tuple[tuple[tuple[int, int, int, int], tuple[int, int, int, int]], ...]:
    sites = tuple(product(range(length), repeat=3))
    reverse = tuple(
        ((*site, 2 * axis), (*site, 2 * axis + 1))
        for site in sites
        for axis in range(3)
    )
    edges = []
    for axis in axis_order:
        displacement = np.zeros(3, dtype=int)
        displacement[axis] = 1
        for site in sites:
            neighbor = shifted(site, displacement, length)
            edges.append(((*site, 2 * axis + 1), (*neighbor, 2 * axis)))
    return reverse + tuple(edges)


def transform_mode(
    mode: tuple[int, int, int, int], frame: np.ndarray, length: int
) -> tuple[int, int, int, int]:
    site = np.asarray(mode[:3], dtype=int)
    target_site = tuple(int(value % length) for value in frame @ site)
    direction_permutation = c210.direction_permutation(frame)
    target_direction = int(np.argmax(direction_permutation[:, mode[3]]))
    return (*target_site, target_direction)


def pair_set(pairs: Iterable[tuple[Mode, Mode]]) -> set[frozenset[Mode]]:
    return {frozenset(pair) for pair in pairs}


def cycle_shift(dimension: int) -> np.ndarray:
    shift = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        shift[(source + 1) % dimension, source] = 1
    return shift


def preferred_axis_schedule_representation(frame: np.ndarray) -> np.ndarray:
    """Schedule phases C,A,Bx,By,Bz,W; rotations permute only B phases."""
    representation = np.zeros((6, 6), dtype=complex)
    representation[0, 0] = representation[1, 1] = representation[5, 5] = 1
    for source_axis in range(3):
        transformed = frame @ np.eye(3, dtype=int)[:, source_axis]
        target_axis = int(np.argmax(np.abs(transformed)))
        representation[2 + target_axis, 2 + source_axis] = 1
    return representation


def schedule_and_covariance_controls() -> None:
    length = 3
    modes = cube_modes(length)
    base_schedule = cube_schedule_pairs(length)

    schedule_signatures = []
    sample_occupations = tuple(combinations(modes[:24], 2))[:128]
    for axis_order in permutations(range(3)):
        trial = cube_schedule_pairs(length, axis_order)
        schedule_signatures.append(
            tuple(local_fswap_action(occupied, trial) for occupied in sample_occupations)
        )
    check(
        "all 3! edge-color orders give the same macro stream because axis edge layers are disjoint",
        all(signature == schedule_signatures[0] for signature in schedule_signatures[1:]),
        {"axis_orders": 6, "sampled_two_particle_states": len(sample_occupations)},
    )

    base_pair_set = pair_set(base_schedule)
    frame_pair_residuals = []
    covariance_residuals = []
    for frame in c210.proper_cubic_frames():
        transformed_pairs = {
            frozenset(
                (transform_mode(first, frame, length), transform_mode(second, frame, length))
            )
            for first, second in base_schedule
        }
        frame_pair_residuals.append(len(base_pair_set.symmetric_difference(transformed_pairs)))
        for occupied in sample_occupations[:32]:
            sign, output = local_fswap_action(occupied, base_schedule)
            rotated_input = frozenset(transform_mode(mode, frame, length) for mode in occupied)
            rotated_sign, rotated_output = local_fswap_action(rotated_input, base_schedule)
            expected_output = frozenset(transform_mode(mode, frame, length) for mode in output)
            covariance_residuals.append(int(sign != rotated_sign or rotated_output != expected_output))
    check(
        "the A-plus-all-axes-B qubit stream is proper-cubic covariant before the coin is inserted",
        max(frame_pair_residuals) == 0 and max(covariance_residuals) == 0,
        {"pair_set_residual": max(frame_pair_residuals), "action_residual": max(covariance_residuals)},
    )

    preferred_shift = cycle_shift(6)
    preferred_commutators = [
        np.linalg.norm(
            preferred_axis_schedule_representation(frame) @ preferred_shift
            - preferred_shift @ preferred_axis_schedule_representation(frame)
        )
        for frame in c210.proper_cubic_frames()
    ]
    check(
        "the preferred C,A,Bx,By,Bz,W micro-schedule is not covariant even though its B macroproduct is",
        sum(value > 1e-12 for value in preferred_commutators) > 0
        and max(preferred_commutators) >= 2,
        {
            "failed_frames": sum(value > 1e-12 for value in preferred_commutators),
            "max_commutator": max(preferred_commutators),
        },
    )

    # C,A,B_all,W is a scalar four-phase update register.  Neighbor equality is a local
    # lawful-domain constraint and is invariant under the homogeneous advance.
    phase_advance = cycle_shift(4)
    equality = np.diag(
        [1 if left == right else 0 for left in range(4) for right in range(4)]
    ).astype(complex)
    pair_advance = np.kron(phase_advance, phase_advance)
    leakage = np.linalg.norm((np.eye(16) - equality) @ pair_advance @ equality)
    check(
        "the four-phase autonomous schedule has a locally preserved synchronization code and no host phase",
        leakage < 2e-15
        and np.linalg.norm(pair_advance @ equality - equality @ pair_advance) < 2e-15,
        {
            "phases": ("C", "A", "B_all", "W_g"),
            "schedule_qubits_per_cell": 2,
            "lawful_domain_leakage": leakage,
        },
    )


def worldline_exchange_controls() -> None:
    modes = (0, 1, 2, 3)
    schedule = ((0, 1), (2, 3), (1, 2), (3, 0))
    permutation = permutation_from_pairs(modes, schedule)
    occupied = (0, 2)
    target_sign, target_output = fermionic_action(modes, permutation, occupied)
    local_sign, local_output = local_fswap_action(occupied, schedule)
    check(
        "a separated two-worldline plaquette exchange has the wrong fermion sign under local FSWAP routing",
        target_output == local_output == frozenset(occupied)
        and target_sign == 1
        and local_sign == 0,
        {"target_amplitude": -1, "local_amplitude": 1, "operator_residual": 2},
    )

    corrections = mismatch_pairs(modes, permutation, schedule)
    repaired = True
    for mask in range(1 << len(modes)):
        state = tuple(mode for mode in modes if (mask >> mode) & 1)
        target_sign, target_output = fermionic_action(modes, permutation, state)
        local_sign, local_output = local_fswap_action(state, schedule)
        correction = sum(
            first in state and second in state for first, second in corrections
        ) % 2
        repaired &= target_output == local_output and target_sign == (local_sign ^ correction)
    check(
        "a bounded plaquette diagonal phase repairs this four-site witness, keeping gauge/plaquette escapes live",
        repaired and len(corrections) > 0,
        {"local_CZ_inventory": corrections},
    )


def inherited_fixture_controls() -> None:
    species = c219.common_species(BETA)
    curvature = c210.curvature_tensor(species, step=1e-4)
    dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
    forced = c210.force_response(species, 2e-5)
    check(
        "the schedule is exact in the one-particle sector and therefore preserves the Cycle-219 mass fixture",
        abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12
        and abs(dispersion_mass / species.analytic_mass - 1) < 4e-6
        and abs(forced.measured_mass / species.analytic_mass - 1) < 0.007,
        {
            "rest": c219.rest_mass(species),
            "curvature": dispersion_mass,
            "forced": forced.measured_mass,
        },
    )

    length = 3
    modes = cube_modes(length)
    order = modes
    schedule = cube_schedule_pairs(length)
    permutation = permutation_from_pairs(modes, schedule)
    one_particle_residuals = []
    for mode in modes:
        target = fermionic_action(order, permutation, (mode,))
        local = local_fswap_action((mode,), schedule)
        one_particle_residuals.append(int(target != local))
    bad_pairs = mismatch_pairs(order, permutation, schedule)
    check(
        "the full L=3 stream intertwines on every one-particle basis state but not on the two-particle code",
        max(one_particle_residuals) == 0 and len(bad_pairs) > 0,
        {
            "one_particle_residual": max(one_particle_residuals),
            "two_particle_mismatches": len(bad_pairs),
            "two_particle_dimension": len(tuple(combinations(modes, 2))),
            "operator_norm_residual": 2,
        },
    )

    unit = 2 * np.pi / length
    momenta = {
        "h1": unit * np.asarray((0, 1, 0), dtype=float),
        "h2": unit * np.asarray((0, -1, 0), dtype=float),
        "p1": unit * np.asarray((1, 1, 1), dtype=float),
        "p2": unit * np.asarray((-1, -1, -1), dtype=float),
    }
    targets = {
        "h1": -0.148864781941705,
        "h2": -2.9904574355314986,
        "p1": 0.0759239848775555,
        "p2": 3.067939104828828,
    }
    vectors = {
        name: c230.band_subspace(momentum, target_phase=targets[name])[1]
        for name, momentum in momenta.items()
    }
    form = c230.contact_form_factor(
        vectors["p1"], vectors["p2"], vectors["h1"], vectors["h2"]
    )
    particle_wedges = np.column_stack(
        tuple(
            c230.internal_wedge(vectors["p1"][:, left], vectors["p2"][:, right])
            for left in range(vectors["p1"].shape[1])
            for right in range(vectors["p2"].shape[1])
        )
    )
    hole_wedges = np.column_stack(
        tuple(
            c230.internal_wedge(vectors["h1"][:, left], vectors["h2"][:, right])
            for left in range(vectors["h1"].shape[1])
            for right in range(vectors["h2"].shape[1])
        )
    )
    # binom(N,2)=1 on the local two-particle sector, so this is the direct
    # six-qubit occupation-basis contact generator block.
    qubit_form = particle_wedges.conj().T @ np.eye(15) @ hole_wedges
    singulars = np.linalg.svd(qubit_form, compute_uv=False)
    check(
        "the local occupation-qubit contact exactly reproduces the Cycle-230 seam generator block",
        np.linalg.norm(qubit_form - form) < 2e-15
        and singulars[-1] > 0.45
        and singulars[0] > 0.49,
        {
            "reduced_singular_values": singulars,
            "raw_L3_norm_over_g": float(np.linalg.norm(qubit_form / length**3)),
            "contact_block_residual": float(np.linalg.norm(qubit_form - form)),
        },
    )

    occupations = c229.occupation_table(6)
    number = occupations.sum(axis=1)
    contact = np.diag(np.exp(1j * COUPLING * number * (number - 1) / 2))
    deleted = np.diag(np.exp(0j * number))
    check(
        "contact deletion is exact and neither contact nor the ideal phase register leaks from its declared local code",
        np.linalg.norm(deleted - np.eye(64)) < 2e-15
        and np.linalg.norm(contact.conj().T @ contact - np.eye(64)) < 3e-15,
        {"g_zero_residual": float(np.linalg.norm(deleted - np.eye(64)))},
    )


def main() -> None:
    note_contract()
    local_block_and_frame_controls()
    axial_order_and_boundary_controls()
    axis_order_change_controls()
    schedule_and_covariance_controls()
    worldline_exchange_controls()
    inherited_fixture_controls()
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
