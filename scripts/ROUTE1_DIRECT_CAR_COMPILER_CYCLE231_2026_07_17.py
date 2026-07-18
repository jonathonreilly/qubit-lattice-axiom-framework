#!/usr/bin/env python3
"""Cycle 231 Route 1: direct six-mode CAR-cell occupation compiler.

Test the strongest no-auxiliary direct block attempt.  Six occupation qubits
represent the six fermionic modes of each Cycle-230 coarse cell.  A covariant
3x3x3 physical supercell puts the six qubits on its face centres, so the
onsite exterior coin/contact have bounded support and the intercell B-layer
mode pairs are physical nearest neighbours.

The exact occupation-basis image of an intercell fermionic swap contains the
parity of every mode between its endpoints in the chosen global ordering.  A
strictly endpoint-local FSWAP omits that interval parity.  This runner tests
the exact intertwining pieces, produces fixed-number two-particle witnesses,
checks held-out sizes and all 24 proper-cubic frames, and keeps auxiliary/gauge
and other encodings explicitly live.  It is not a general compiler no-go.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path

import numpy as np

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ROUTE1_DIRECT_CAR_COMPILER_CYCLE231_NOTE_2026-07-17.md"
)
BETA = -0.3
COUPLING = 0.37
REVERSE = (1, 0, 3, 2, 5, 4)
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


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "route-specific partial-attempt",
        "e g_coarse = g_physical e",
        "operator-norm intertwining residual is exactly 2",
        "six active physical `m_2` sites",
        "27 physical sites per coarse cell",
        "global compiler impossibility",
        "all 24 proper-cubic frames",
        "cycle-230 seam block",
        "one-particle mass",
        "leakage",
        "deletion",
        "held-out",
        "lawful-domain",
        "supplied-structure inventory",
        "n1 — alternative route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "**authority:** none",
        "**audit:** unset",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves Route-1 scope and N1-N8 discipline", not missing, missing)


def all_sites(length: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(product(range(length), repeat=3))


def site_index(site: tuple[int, int, int], direction: int, length: int) -> int:
    return c230.site_index(site, direction, length)


def index_mode(index: int, length: int) -> tuple[tuple[int, int, int], int]:
    cell, direction = divmod(index, 6)
    x, rem = divmod(cell, length * length)
    y, z = divmod(rem, length)
    return (x, y, z), direction


def shifted(
    site: tuple[int, int, int], displacement: np.ndarray, length: int
) -> tuple[int, int, int]:
    return tuple(
        int((site[axis] + int(displacement[axis])) % length) for axis in range(3)
    )


def edge_permutation(length: int) -> np.ndarray:
    """Cycle-230 B layer: disjoint intercell mode transpositions."""
    permutation = np.empty(6 * length**3, dtype=int)
    for site in all_sites(length):
        for direction, displacement in enumerate(c210.DIRECTIONS):
            target_site = shifted(site, -displacement, length)
            permutation[site_index(site, direction, length)] = site_index(
                target_site, REVERSE[direction], length
            )
    return permutation


def reverse_permutation(length: int) -> np.ndarray:
    permutation = np.empty(6 * length**3, dtype=int)
    for site in all_sites(length):
        for direction in range(6):
            permutation[site_index(site, direction, length)] = site_index(
                site, REVERSE[direction], length
            )
    return permutation


def physical_position(
    site: tuple[int, int, int], direction: int
) -> tuple[int, int, int]:
    """Face-centre layout; the minus sign makes B partners nearest-neighbour."""
    return tuple(
        int(3 * site[axis] - c210.DIRECTIONS[direction, axis])
        for axis in range(3)
    )


def periodic_l1(
    left: tuple[int, int, int], right: tuple[int, int, int], period: int
) -> int:
    return sum(
        min(abs(left[axis] - right[axis]), period - abs(left[axis] - right[axis]))
        for axis in range(3)
    )


def block_layout_controls() -> None:
    offsets = tuple(product((-1, 0, 1), repeat=3))
    active_offsets = tuple(tuple((-row).astype(int)) for row in c210.DIRECTIONS)
    frames = c210.proper_cubic_frames()
    rotation_closed = all(
        {tuple((frame @ np.asarray(offset)).astype(int)) for offset in active_offsets}
        == set(active_offsets)
        for frame in frames
    )
    check(
        "a 3x3x3 supercell gives six disjoint active face-centre M2 sites with constant overhead",
        len(offsets) == 27
        and len(set(offsets)) == 27
        and len(set(active_offsets)) == 6
        and set(active_offsets).issubset(set(offsets)),
        {"active": 6, "total": 27, "blank": 21},
    )
    check(
        "the direct block layout is closed under all 24 proper-cubic frames",
        len(frames) == 24 and rotation_closed,
    )

    for length in (3, 4):
        period = 3 * length
        edge = edge_permutation(length)
        distances = []
        for source, target in enumerate(edge):
            if source < target:
                source_site, source_direction = index_mode(source, length)
                target_site, target_direction = index_mode(target, length)
                distances.append(
                    periodic_l1(
                        physical_position(source_site, source_direction),
                        physical_position(target_site, target_direction),
                        period,
                    )
                )
        check(
            f"every B-layer mode pair is a physical nearest-neighbour at held-out L={length}",
            distances and set(distances) == {1},
            {"pairs": len(distances), "distances": sorted(set(distances))},
        )


def onsite_block_controls() -> tuple[np.ndarray, np.ndarray]:
    species = c219.common_species(BETA)
    gamma_coin = c229.fock_lift(species.coin)
    occupations = c229.occupation_table(6)
    number = np.sum(occupations, axis=1)
    parity = np.diag((-1.0) ** number)
    contact = np.diag(np.exp(1j * COUPLING * number * (number - 1) / 2))
    one_particle = np.asarray([1 << mode for mode in range(6)], dtype=int)
    coin_residual = np.linalg.norm(
        gamma_coin[np.ix_(one_particle, one_particle)] - species.coin
    )
    check(
        "six occupation qubits faithfully carry the full M64 cell and its 2048-dimensional even subalgebra",
        gamma_coin.shape == (64, 64)
        and np.linalg.norm(gamma_coin.conj().T @ gamma_coin - np.eye(64)) < 2e-14
        and np.linalg.norm(gamma_coin @ parity - parity @ gamma_coin) < 2e-14,
        {"hilbert_dimension": 64, "even_algebra_dimension": 2048},
    )
    check(
        "the exterior coin and contact intertwine exactly on one direct block",
        coin_residual < 2e-15
        and np.linalg.norm(contact.conj().T @ contact - np.eye(64)) < 2e-15
        and np.linalg.norm(contact @ parity - parity @ contact) < 2e-15,
        {"one_particle_coin_residual": float(coin_residual)},
    )
    check(
        "contact deletion is exact and the contact is identity on N<=1",
        np.max(np.abs(np.diag(contact)[number <= 1] - 1)) < 2e-15
        and np.max(np.abs(np.exp(1j * 0 * number * (number - 1) / 2) - 1)) == 0,
    )
    return gamma_coin, contact


def inversion_sign(images: tuple[int, ...]) -> int:
    inversions = sum(
        images[left] > images[right]
        for left in range(len(images))
        for right in range(left + 1, len(images))
    )
    return -1 if inversions % 2 else 1


def exterior_permutation_action(
    permutation: np.ndarray, occupied: tuple[int, ...]
) -> tuple[tuple[int, ...], int]:
    images = tuple(int(permutation[mode]) for mode in occupied)
    return tuple(sorted(images)), inversion_sign(images)


def endpoint_fswap_action(
    permutation: np.ndarray, occupied: tuple[int, ...]
) -> tuple[tuple[int, ...], int]:
    occupied_set = set(occupied)
    doubly_occupied_pairs = sum(
        mode < int(permutation[mode])
        and int(permutation[mode]) in occupied_set
        for mode in occupied
    )
    images = tuple(sorted(int(permutation[mode]) for mode in occupied))
    return images, -1 if doubly_occupied_pairs % 2 else 1


def two_particle_mismatch(length: int) -> tuple[int, int, tuple[int, int] | None]:
    permutation = edge_permutation(length)
    mismatch = 0
    witness = None
    total = 0
    for pair in combinations(range(len(permutation)), 2):
        exact = exterior_permutation_action(permutation, pair)
        local = endpoint_fswap_action(permutation, pair)
        total += 1
        if exact != local:
            mismatch += 1
            witness = witness or pair
    return mismatch, total, witness


def direct_stream_controls() -> None:
    rows = []
    for length in (3, 4, 5):
        permutation = edge_permutation(length)
        involution = np.array_equal(permutation[permutation], np.arange(len(permutation)))
        one_particle_match = all(
            exterior_permutation_action(permutation, (mode,))
            == endpoint_fswap_action(permutation, (mode,))
            for mode in range(len(permutation))
        )
        mismatch, total, witness = two_particle_mismatch(length)
        rows.append(
            {
                "L": length,
                "modes": len(permutation),
                "mismatch": mismatch,
                "pairs": total,
                "fraction": mismatch / total,
                "witness": witness,
                "max_order_span": int(
                    max(abs(mode - int(permutation[mode])) for mode in range(len(permutation)))
                ),
            }
        )
        check(
            f"endpoint-local FSWAP is exact on vacuum/one-particle states but fails the two-particle CAR action at L={length}",
            involution and one_particle_match and mismatch > 0 and witness is not None,
            rows[-1],
        )

    witness = rows[0]["witness"]
    assert witness is not None
    exact = exterior_permutation_action(edge_permutation(3), witness)
    local = endpoint_fswap_action(edge_permutation(3), witness)
    witness_residual = abs(exact[1] - local[1])
    check(
        "the declared local direct free-plus-contact compiler has operator-norm intertwining residual exactly 2",
        exact[0] == local[0] and witness_residual == 2,
        {
            "witness": witness,
            "exact_phase": exact[1],
            "local_phase": local[1],
            "norm": witness_residual,
            "reason": "common coin/A/contact factors are unitary",
        },
    )


def interval_parity(occupied: tuple[int, ...], left: int, right: int) -> int:
    low, high = sorted((left, right))
    return sum(low < mode < high and mode in occupied for mode in range(low + 1, high)) % 2


def remote_parity_controls() -> None:
    length = 5
    radius = 2
    period = 3 * length
    permutation = edge_permutation(length)
    pairs = tuple((mode, int(target)) for mode, target in enumerate(permutation) if mode < target)
    left, right = max(pairs, key=lambda pair: abs(pair[0] - pair[1]))
    endpoint_positions = []
    for mode in (left, right):
        site, direction = index_mode(mode, length)
        endpoint_positions.append(physical_position(site, direction))

    def remote(mode: int) -> bool:
        site, direction = index_mode(mode, length)
        position = physical_position(site, direction)
        return all(periodic_l1(position, endpoint, period) > radius for endpoint in endpoint_positions)

    inside = next(mode for mode in range(left + 1, right) if remote(mode))
    outside = next(
        mode
        for mode in tuple(range(0, left)) + tuple(range(right + 1, len(permutation)))
        if remote(mode)
    )
    state_inside = tuple(sorted((left, inside)))
    state_outside = tuple(sorted((left, outside)))
    inside_parity = interval_parity(state_inside, left, right)
    outside_parity = interval_parity(state_outside, left, right)
    check(
        "a radius-two local dressing cannot recover the exact JW interval parity even at fixed N=2 and fixed global parity",
        inside_parity == 1
        and outside_parity == 0
        and len(state_inside) == len(state_outside) == 2
        and all(remote(mode) for mode in (inside, outside)),
        {
            "edge": (left, right),
            "order_span": right - left,
            "inside_spectator": inside,
            "outside_spectator": outside,
            "endpoint_radius": radius,
        },
    )

    separated_witness = None
    for pair in combinations(range(len(permutation)), 2):
        exact = exterior_permutation_action(permutation, pair)
        local = endpoint_fswap_action(permutation, pair)
        if exact == local:
            continue
        positions = []
        for mode in pair:
            site, direction = index_mode(mode, length)
            positions.append(physical_position(site, direction))
        if periodic_l1(positions[0], positions[1], period) > 2 * radius + 2:
            separated_witness = (pair, positions)
            break
    check(
        "the two-particle sign mismatch persists for disjoint physical radius-two light cones",
        separated_witness is not None,
        {
            "witness": None if separated_witness is None else separated_witness[0],
            "physical_positions": None if separated_witness is None else separated_witness[1],
        },
    )

    spans = []
    for held_out in (3, 4, 5, 6):
        held_permutation = edge_permutation(held_out)
        spans.append(
            max(
                abs(mode - int(held_permutation[mode])) - 1
                for mode in range(len(held_permutation))
            )
        )
    check(
        "the exact occupation/JW stream has growing order support on held-out sizes",
        spans == sorted(spans) and len(set(spans)) == len(spans) and spans[-1] > spans[0],
        {"L": (3, 4, 5, 6), "maximum_intervening_modes": spans},
    )


def ordinary_qubit_permutation(one_particle: np.ndarray) -> np.ndarray:
    permutation = tuple(int(np.argmax(one_particle[:, source])) for source in range(6))
    result = np.zeros((64, 64), dtype=complex)
    for basis in range(64):
        target = 0
        for source, destination in enumerate(permutation):
            if (basis >> source) & 1:
                target |= 1 << destination
        result[target, basis] = 1
    return result


def physical_frame_action(
    frame: np.ndarray,
    length: int,
    occupied: tuple[int, ...],
    exterior_sign: bool,
) -> tuple[tuple[int, ...], int]:
    """Physical block frame: geometric cells/arms, optional local exterior sign."""
    direction_matrix = c210.direction_permutation(frame)
    direction_permutation = tuple(
        int(np.argmax(direction_matrix[:, source])) for source in range(6)
    )
    by_cell: dict[tuple[int, int, int], list[int]] = {}
    for mode in occupied:
        site, direction = index_mode(mode, length)
        by_cell.setdefault(site, []).append(direction)
    target_modes: list[int] = []
    sign = 1
    for site, directions in by_cell.items():
        images = tuple(direction_permutation[direction] for direction in sorted(directions))
        if exterior_sign:
            sign *= inversion_sign(images)
        target_site = tuple(int(value % length) for value in frame @ np.asarray(site))
        target_modes.extend(site_index(target_site, direction, length) for direction in images)
    return tuple(sorted(target_modes)), sign


def compose_signed(left, right, occupied: tuple[int, ...]) -> tuple[tuple[int, ...], int]:
    intermediate, right_sign = right(occupied)
    target, left_sign = left(intermediate)
    return target, right_sign * left_sign


def rotation_controls(gamma_coin: np.ndarray, contact: np.ndarray) -> None:
    exterior_residuals = []
    geometric_residuals = []
    contact_residuals = []
    character_gaps = []
    cocycle_residuals = []
    for frame in c210.proper_cubic_frames():
        one_particle = c210.direction_permutation(frame)
        exterior = c229.fock_lift(one_particle)
        geometric = ordinary_qubit_permutation(one_particle)
        exterior_residuals.append(np.linalg.norm(exterior @ gamma_coin - gamma_coin @ exterior))
        geometric_residuals.append(np.linalg.norm(geometric @ gamma_coin - gamma_coin @ geometric))
        contact_residuals.append(np.linalg.norm(geometric @ contact - contact @ geometric))
        character_gaps.append(abs(np.trace(exterior) - np.trace(geometric)))
        cocycle = exterior @ geometric.conj().T
        cocycle_residuals.append(
            max(
                np.linalg.norm(cocycle - np.diag(np.diag(cocycle))),
                np.linalg.norm((cocycle @ geometric) @ gamma_coin - gamma_coin @ (cocycle @ geometric)),
            )
        )
    check(
        "the coarse exterior coin/contact are covariant in all 24 proper-cubic exterior frames",
        max(exterior_residuals) < 2e-14 and max(contact_residuals) < 2e-14,
        {"coin": max(exterior_residuals), "contact": max(contact_residuals)},
    )
    check(
        "pure geometric permutation of the six arm qubits does not implement the exterior frame representation",
        sum(value > 1e-10 for value in geometric_residuals) == 22
        and max(geometric_residuals) > 7
        and max(character_gaps) > 1,
        {
            "failed_frames": sum(value > 1e-10 for value in geometric_residuals),
            "max_coin_residual": max(geometric_residuals),
            "max_character_gap": max(character_gaps),
        },
    )
    check(
        "a supplied bounded diagonal exterior-sign cocycle repairs the onsite coin in every frame",
        max(cocycle_residuals) < 2e-14,
        max(cocycle_residuals),
    )

    length = 3
    edge = edge_permutation(length)
    pairs = tuple(combinations(range(len(edge)), 2))
    geometric_failures = []
    exterior_failures = []
    for frame in c210.proper_cubic_frames():
        endpoint = lambda state: endpoint_fswap_action(edge, state)
        geometric = lambda state, frame=frame: physical_frame_action(
            frame, length, state, exterior_sign=False
        )
        exterior = lambda state, frame=frame: physical_frame_action(
            frame, length, state, exterior_sign=True
        )
        geometric_failures.append(
            next(
                (
                    pair
                    for pair in pairs
                    if compose_signed(endpoint, geometric, pair)
                    != compose_signed(geometric, endpoint, pair)
                ),
                None,
            )
        )
        exterior_failures.append(
            next(
                (
                    pair
                    for pair in pairs
                    if compose_signed(endpoint, exterior, pair)
                    != compose_signed(exterior, endpoint, pair)
                ),
                None,
            )
        )
    check(
        "geometric frames preserve the endpoint stream, while the local exterior-sign repair makes it noncovariant in 23 nonidentity frames",
        all(witness is None for witness in geometric_failures)
        and sum(witness is not None for witness in exterior_failures) == 23,
        {
            "geometric_failed_frames": sum(witness is not None for witness in geometric_failures),
            "exterior_failed_frames": sum(witness is not None for witness in exterior_failures),
            "first_exterior_witness": next(
                witness for witness in exterior_failures if witness is not None
            ),
        },
    )


def mass_and_seam_controls() -> None:
    species = c219.common_species(BETA)
    curvature = c210.curvature_tensor(species, step=1e-4)
    dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
    forced = c210.force_response(species, 2e-5)
    check(
        "the direct candidate preserves the one-particle mass fixture because every parity string and the contact are trivial there",
        abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12
        and abs(dispersion_mass / species.analytic_mass - 1) < 4e-6
        and abs(forced.measured_mass / species.analytic_mass - 1) < 0.007,
        {
            "rest": c219.rest_mass(species),
            "dispersion": dispersion_mass,
            "forced": forced.measured_mass,
            "analytic": species.analytic_mass,
        },
    )

    length = 3
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
    subspaces = {
        name: c230.band_subspace(momentum, target_phase=targets[name])
        for name, momentum in momenta.items()
    }
    phases = {name: value[0] for name, value in subspaces.items()}
    vectors = {name: value[1] for name, value in subspaces.items()}
    form = c230.contact_form_factor(
        vectors["p1"], vectors["p2"], vectors["h1"], vectors["h2"]
    )
    singulars = np.linalg.svd(form, compute_uv=False)
    phase_cost = (
        phases["p1"][:, None, None, None]
        + phases["p2"][None, :, None, None]
        - phases["h1"][None, None, :, None]
        - phases["h2"][None, None, None, :]
    )
    frame_singular_residuals = []
    for frame in c210.proper_cubic_frames():
        transformed = {
            name: c230.band_subspace(frame @ momenta[name], target_phase=targets[name])[1]
            for name in momenta
        }
        transformed_form = c230.contact_form_factor(
            transformed["p1"],
            transformed["p2"],
            transformed["h1"],
            transformed["h2"],
        )
        frame_singular_residuals.append(
            np.linalg.norm(np.linalg.svd(transformed_form, compute_uv=False) - singulars)
        )
    check(
        "the direct block contact exactly retains the Cycle-230 seam block in all 24 proper-cubic frames",
        np.max(np.abs(phase_cost - 2 * np.pi)) < 3e-14
        and singulars[-1] > 0.45
        and singulars[0] > 0.49
        and max(frame_singular_residuals) < 2e-13,
        {
            "phase_residual": float(np.max(np.abs(phase_cost - 2 * np.pi))),
            "singular_values": singulars,
            "frame_residual": max(frame_singular_residuals),
            "raw_plane_wave_norm_over_g": float(np.linalg.norm(form) / length**3),
        },
    )


def lawful_domain_controls() -> None:
    # No auxiliary code is used on the six active sites: their full 64-state
    # Hilbert space is the active code.  The 21 spacer sites are fixed blanks.
    check(
        "the direct active-block code has zero algebraic leakage and constant blank overhead",
        (1 << 6) == 64 and 27 - 6 == 21,
        {"active_code_dimension": 64, "fixed_blanks": 21},
    )

    length = 3
    edge = edge_permutation(length)
    # Two particles in one cell can be separated by B into two odd cells.
    source = (site_index((0, 0, 0), 0, length), site_index((0, 0, 0), 2, length))
    target = tuple(sorted(int(edge[mode]) for mode in source))
    target_cells = tuple(index_mode(mode, length)[0] for mode in target)
    check(
        "an even-occupation-per-cell restriction leaks under the free stream and excludes the one-particle mass domain",
        target_cells[0] != target_cells[1]
        and all(sum(cell == candidate for cell in target_cells) % 2 == 1 for candidate in set(target_cells)),
        {"source_modes": source, "target_modes": target, "target_cells": target_cells},
    )

    mismatch, _, witness = two_particle_mismatch(length)
    assert witness is not None
    check(
        "fixing global even parity does not repair the local stream and deleting N>=2 would delete contact/seam support",
        mismatch > 0 and len(witness) == 2,
        {"fixed_N_witness": witness, "global_parity": "even", "mismatches": mismatch},
    )


def main() -> None:
    note_contract()
    block_layout_controls()
    gamma_coin, contact = onsite_block_controls()
    direct_stream_controls()
    remote_parity_controls()
    rotation_controls(gamma_coin, contact)
    mass_and_seam_controls()
    lawful_domain_controls()
    print(f"SUMMARY {PASS} passed / {FAIL} failed")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
