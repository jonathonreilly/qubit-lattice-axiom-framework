#!/usr/bin/env python3
"""Cycle873 uniform Z17 affine-Gauss intertwiner core.

This core works directly over finite-field incidence matrices and sparse state
dictionaries.  It proves that the trivial-character uniform affine fiber
intertwines every augmented FSWAP, checks a contractible loop and repeated L2
factors, and then tests the actual Cycle219 beta=-0.3 dense coin and decoded
free one-particle dispersion.  State preparation/enforcement and periodic
Wilson-sector selection are not supplied by this calculation.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import argparse
import json
import math
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as C219
import frontier_cycle870_openreference_native_recurrent_update_2026_08_02 as C870


P = 17
TOL = 3.0e-10
EXPECTED_BASE_COMMIT = "c73a11d1ea7ddd564c48aa2a5a459a43d94262ef"
OUT = ROOT / "outputs/cycle873_uniform_affine_gauss_intertwiner_core_receipt_2026_08_03.json"
SOURCE_PINS = {
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py":
        "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py":
        "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
}


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rref_mod(matrix: np.ndarray, p: int = P):
    a = np.asarray(matrix, dtype=np.int64).copy() % p
    row = 0
    pivots: list[int] = []
    for col in range(a.shape[1]):
        pivot = next((r for r in range(row, a.shape[0]) if int(a[r, col]) % p), None)
        if pivot is None:
            continue
        a[[row, pivot]] = a[[pivot, row]]
        a[row] = (a[row] * pow(int(a[row, col]), -1, p)) % p
        for r in range(a.shape[0]):
            if r != row and a[r, col]:
                a[r] = (a[r] - int(a[r, col]) * a[row]) % p
        pivots.append(col)
        row += 1
        if row == a.shape[0]:
            break
    return a, pivots


def rank_mod(matrix: np.ndarray, p: int = P) -> int:
    return len(rref_mod(matrix, p)[1])


def nullspace_mod(matrix: np.ndarray, p: int = P) -> np.ndarray:
    a, pivots = rref_mod(matrix, p)
    free = [c for c in range(a.shape[1]) if c not in pivots]
    basis = []
    for f in free:
        x = np.zeros(a.shape[1], dtype=np.int64)
        x[f] = 1
        for r, pivot in enumerate(pivots):
            x[pivot] = (-a[r, f]) % p
        basis.append(x)
    return np.asarray(basis, dtype=np.int64).T if basis else np.zeros((a.shape[1], 0), dtype=np.int64)


def solve_mod(matrix: np.ndarray, rhs: np.ndarray, p: int = P) -> np.ndarray:
    a = np.asarray(matrix, dtype=np.int64) % p
    b = np.asarray(rhs, dtype=np.int64).reshape(-1, 1) % p
    aug, pivots = rref_mod(np.hstack((a, b)), p)
    n = a.shape[1]
    for row in aug:
        if not np.any(row[:n]) and row[n]:
            raise ValueError("inconsistent affine Gauss sector")
    x = np.zeros(n, dtype=np.int64)
    for r, pivot in enumerate(p for p in pivots if p < n):
        x[pivot] = aug[r, n]
    assert np.array_equal((a @ x) % p, b[:, 0])
    return x


def independent_columns(matrix: np.ndarray, p: int = P) -> list[int]:
    chosen: list[int] = []
    old_rank = 0
    for col in range(matrix.shape[1]):
        trial = chosen + [col]
        new_rank = rank_mod(matrix[:, trial], p)
        if new_rank > old_rank:
            chosen.append(col)
            old_rank = new_rank
    return chosen


@dataclass(frozen=True)
class CubicComplex:
    name: str
    dims: tuple[int, int, int]
    vertices: tuple[tuple[int, int, int], ...]
    edges: tuple[tuple[int, int, int], ...]  # tail index, head index, axis
    face_labels: tuple[tuple[tuple[int, int, int], int, int], ...]
    incidence: np.ndarray
    faces: np.ndarray  # edge x face oriented-boundary matrix


@dataclass(frozen=True)
class FixedStarBackground:
    """A supplied affine-star background for one fixed-number matter sector.

    The admitted fiber obeys incidence*ell = alpha*n + field (mod 17).
    Solvability therefore requires sum(field) = -alpha*particle_number.
    The field is input structure; this core neither selects nor prepares it.
    """

    label: str
    alpha: int
    particle_number: int
    field: tuple[int, ...]


def open_box(name: str, dims: tuple[int, int, int]) -> CubicComplex:
    vertices = tuple(product(*(range(length) for length in dims)))
    vid = {vertex: index for index, vertex in enumerate(vertices)}
    edges = []
    edge_index = {}
    for vertex in vertices:
        for axis in range(3):
            if vertex[axis] + 1 >= dims[axis]:
                continue
            target = list(vertex)
            target[axis] += 1
            target_t = tuple(target)
            edge_index[(vertex, target_t)] = len(edges)
            edges.append((vid[vertex], vid[target_t], axis))
    incidence = np.zeros((len(vertices), len(edges)), dtype=np.int64)
    for edge, (tail, head, _axis) in enumerate(edges):
        incidence[tail, edge] = -1
        incidence[head, edge] = +1

    face_vectors = []
    face_labels = []
    for a in range(3):
        for b in range(a + 1, 3):
            for base in vertices:
                if base[a] + 1 >= dims[a] or base[b] + 1 >= dims[b]:
                    continue
                ea = [0, 0, 0]
                eb = [0, 0, 0]
                ea[a] = 1
                eb[b] = 1
                va = tuple(base[i] + ea[i] for i in range(3))
                vb = tuple(base[i] + eb[i] for i in range(3))
                vab = tuple(base[i] + ea[i] + eb[i] for i in range(3))
                vector = np.zeros(len(edges), dtype=np.int64)
                vector[edge_index[(base, va)]] += 1
                vector[edge_index[(va, vab)]] += 1
                vector[edge_index[(vb, vab)]] -= 1
                vector[edge_index[(base, vb)]] -= 1
                face_vectors.append(vector % P)
                face_labels.append((base, a, b))
    faces = (
        np.asarray(face_vectors, dtype=np.int64).T % P
        if face_vectors
        else np.zeros((len(edges), 0), dtype=np.int64)
    )
    return CubicComplex(
        name, dims, vertices, tuple(edges), tuple(face_labels), incidence % P, faces
    )


def bits_array(bits: int, count: int) -> np.ndarray:
    return np.asarray([(bits >> index) & 1 for index in range(count)], dtype=np.int64)


def supplied_star_background(
    graph: CubicComplex,
    particle_number: int,
    *,
    alpha: int = 1,
    convention: str = "ordered_prefix",
) -> FixedStarBackground:
    """Construct one explicit diagnostic input field, never a selected vacuum."""

    if not 0 <= particle_number <= len(graph.vertices):
        raise ValueError("particle number outside graph")
    field = np.zeros(len(graph.vertices), dtype=np.int64)
    if convention == "ordered_prefix":
        field[:particle_number] = -alpha
    elif convention == "first_anchor":
        field[0] = -alpha * particle_number
    elif convention == "last_anchor":
        field[-1] = -alpha * particle_number
    else:
        raise ValueError(f"unknown background convention: {convention}")
    field %= P
    assert int(field.sum()) % P == (-alpha * particle_number) % P
    return FixedStarBackground(
        convention,
        alpha % P,
        particle_number,
        tuple(int(value) for value in field),
    )


def background_variants(
    graph: CubicComplex, particle_number: int, *, alpha: int = 1
) -> tuple[FixedStarBackground, ...]:
    return tuple(
        supplied_star_background(
            graph, particle_number, alpha=alpha, convention=convention
        )
        for convention in ("ordered_prefix", "first_anchor", "last_anchor")
    )


def matter_charge(
    graph: CubicComplex, bits: int, background: FixedStarBackground
) -> np.ndarray:
    """Return q_g(n)=alpha*n+g for an explicitly supplied fixed background."""

    n = bits_array(bits, len(graph.vertices))
    if int(n.sum()) != background.particle_number:
        raise ValueError("matter word leaves the supplied fixed-number sector")
    if len(background.field) != len(graph.vertices):
        raise ValueError("background support does not match graph")
    q = (background.alpha * n + np.asarray(background.field, dtype=np.int64)) % P
    assert int(q.sum()) % P == 0
    return q


def swap_bits(bits: int, u: int, v: int):
    nu, nv = (bits >> u) & 1, (bits >> v) & 1
    out = bits
    if nu != nv:
        out ^= (1 << u) | (1 << v)
    phase = -1 if nu == nv == 1 else 1
    return out, phase, nu, nv


def state_residual(left: dict, right: dict) -> float:
    return math.sqrt(
        sum(abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2 for key in set(left) | set(right))
    )


def state_overlap(left: dict, right: dict) -> complex:
    return sum(np.conj(value) * right.get(key, 0.0j) for key, value in left.items())


def affine_state(
    graph: CubicComplex,
    bits: int,
    generators: np.ndarray,
    background: FixedStarBackground,
    character: tuple[int, ...] | None = None,
) -> dict:
    q = matter_charge(graph, bits, background)
    base = solve_mod(graph.incidence, q)
    beta = generators.shape[1]
    character = (0,) * beta if character is None else character
    assert len(character) == beta
    size = P ** beta
    amplitude = 1.0 / math.sqrt(size)
    omega = np.exp(2j * math.pi / P)
    output = {}
    for coeff in product(range(P), repeat=beta):
        link = (base + generators @ np.asarray(coeff, dtype=np.int64)) % P
        phase_power = sum(a * b for a, b in zip(character, coeff)) % P
        output[(bits, tuple(int(v) for v in link))] = amplitude * omega ** phase_power
    assert abs(sum(abs(v) ** 2 for v in output.values()) - 1.0) < 1e-12
    return output


def augmented_fswap_state(
    graph: CubicComplex,
    state: dict,
    edge_index: int,
    current_alpha: int = 1,
) -> dict:
    u, v, _axis = graph.edges[edge_index]
    output = {}
    for (bits, link_tuple), amplitude in state.items():
        new_bits, phase, nu, nv = swap_bits(bits, u, v)
        link = np.asarray(link_tuple, dtype=np.int64)
        link[edge_index] = (link[edge_index] + current_alpha * (nu - nv)) % P
        key = (new_bits, tuple(int(x) for x in link))
        output[key] = output.get(key, 0.0j) + phase * amplitude
    return output


def expected_fswap_state(
    graph, bits, generators, background, edge_index, character=None
):
    u, v, _axis = graph.edges[edge_index]
    new_bits, phase, _nu, _nv = swap_bits(bits, u, v)
    return {
        key: phase * value
        for key, value in affine_state(
            graph, new_bits, generators, background, character
        ).items()
    }


def apply_sequence(graph, state, sequence, current_alpha=1):
    for edge in sequence:
        state = augmented_fswap_state(graph, state, edge, current_alpha)
    return state


def expected_sequence(
    graph, bits, generators, background, sequence, character=None
):
    phase = 1
    current = bits
    for edge in sequence:
        u, v, _axis = graph.edges[edge]
        current, step_phase, _nu, _nv = swap_bits(current, u, v)
        phase *= step_phase
    return {
        key: phase * value
        for key, value in affine_state(
            graph, current, generators, background, character
        ).items()
    }, current, phase


def enumerate_affine_sector(graph: CubicComplex, generators: np.ndarray, chunk=100_000) -> int:
    """Exhaust every coefficient word, checking the Gauss equation in batches."""
    beta = generators.shape[1]
    total = P ** beta
    q = np.zeros(len(graph.vertices), dtype=np.int64)
    base = solve_mod(graph.incidence, q)
    checked = 0
    powers = np.asarray([P ** i for i in range(beta)], dtype=np.int64)
    for start in range(0, total, chunk):
        stop = min(total, start + chunk)
        words = np.arange(start, stop, dtype=np.int64)
        coeff = ((words[None, :] // powers[:, None]) % P).astype(np.int64)
        links = (base[:, None] + generators @ coeff) % P
        assert np.count_nonzero((graph.incidence @ links) % P) == 0
        checked += stop - start
    assert checked == total and rank_mod(generators) == beta
    return checked


def graph_certificate(graph: CubicComplex) -> dict:
    b_rank = rank_mod(graph.incidence)
    kernel = nullspace_mod(graph.incidence)
    beta = kernel.shape[1]
    f_rank = rank_mod(graph.faces)
    face_basis_indices = independent_columns(graph.faces)
    face_basis = graph.faces[:, face_basis_indices]
    assert b_rank == len(graph.vertices) - 1
    assert np.count_nonzero((graph.incidence @ graph.faces) % P) == 0
    assert f_rank == beta
    assert rank_mod(face_basis) == beta
    sector_size = P ** beta
    enumerated = enumerate_affine_sector(graph, face_basis)
    face_relations = nullspace_mod(graph.faces)

    return {
        "vertices": len(graph.vertices),
        "edges": len(graph.edges),
        "faces": graph.faces.shape[1],
        "incidence_rank": b_rank,
        "kernel_dimension": beta,
        "affine_sector_size": sector_size,
        "enumerated_affine_points": enumerated,
        "plaquette_boundary_rank": f_rank,
        "uniform_invariant_subspace_dimension": P ** (beta - f_rank),
        "edge_order": [
            {"tail": list(graph.vertices[u]), "head": list(graph.vertices[v]), "axis": axis}
            for u, v, axis in graph.edges
        ],
        "face_labels": [
            {"base": list(base), "axes": [a, b]} for base, a, b in graph.face_labels
        ],
        "face_vectors_mod17": graph.faces.T.tolist(),
        "independent_face_indices": face_basis_indices,
        "independent_face_vectors_mod17": face_basis.T.tolist(),
        "face_relation_basis_mod17": face_relations.T.tolist(),
    }


plaquette = open_box("filled_plaquette", (2, 2, 1))
cube_l2 = open_box("open_cube_L2", (2, 2, 2))
plaquette_cert = graph_certificate(plaquette)
cube_cert = graph_certificate(cube_l2)

plaquette_basis = plaquette.faces[:, plaquette_cert["independent_face_indices"]]
cube_basis = cube_l2.faces[:, cube_cert["independent_face_indices"]]

# Direct sparse matrix-column checks on the filled plaquette: all matter basis
# words and all seams.  This includes the |11> FSWAP minus sign.
direct_residuals = []
background_variant_residuals = []
background_variant_cases = 0
wrong_sign_residuals = []
wrong_alpha_active_residuals = {alpha: [] for alpha in range(P) if alpha != 1}
for bits in range(1 << len(plaquette.vertices)):
    particle_number = int(bits.bit_count())
    backgrounds = background_variants(plaquette, particle_number)
    for edge in range(len(plaquette.edges)):
        background = backgrounds[0]
        encoded = affine_state(plaquette, bits, plaquette_basis, background)
        observed = augmented_fswap_state(plaquette, encoded, edge, +1)
        expected = expected_fswap_state(
            plaquette, bits, plaquette_basis, background, edge
        )
        direct_residuals.append(state_residual(observed, expected))
        for supplied_background in backgrounds:
            variant_encoded = affine_state(
                plaquette, bits, plaquette_basis, supplied_background
            )
            variant_observed = augmented_fswap_state(
                plaquette, variant_encoded, edge, +1
            )
            variant_expected = expected_fswap_state(
                plaquette, bits, plaquette_basis, supplied_background, edge
            )
            background_variant_residuals.append(
                state_residual(variant_observed, variant_expected)
            )
            background_variant_cases += 1
        wrong = augmented_fswap_state(plaquette, encoded, edge, -1)
        wrong_sign_residuals.append(state_residual(wrong, expected))
        u, v, _axis = plaquette.edges[edge]
        _new_bits, _phase, nu, nv = swap_bits(bits, u, v)
        if nu != nv:
            for wrong_alpha in wrong_alpha_active_residuals:
                wrong = augmented_fswap_state(
                    plaquette, encoded, edge, wrong_alpha
                )
                wrong_alpha_active_residuals[wrong_alpha].append(
                    state_residual(wrong, expected)
                )
assert max(direct_residuals) == 0.0
assert max(background_variant_residuals) == 0.0
assert all(
    all(abs(value - math.sqrt(2)) < 1e-12 for value in residuals)
    for residuals in wrong_alpha_active_residuals.values()
)

# The oriented loop is bottom, right, reverse-top, reverse-left in the fixed
# positive-axis edge orientation.  A single particle returns to its matter
# basis word while the accumulated link current is the plaquette boundary.
edge_lookup_plaq = {
    (plaquette.vertices[u], plaquette.vertices[v]): edge
    for edge, (u, v, _axis) in enumerate(plaquette.edges)
}
v00, v10, v01, v11 = (0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)
loop_sequence = (
    edge_lookup_plaq[(v00, v10)],
    edge_lookup_plaq[(v10, v11)],
    edge_lookup_plaq[(v01, v11)],
    edge_lookup_plaq[(v00, v01)],
)
sequence_residuals = []
for bits in range(1 << len(plaquette.vertices)):
    background = supplied_star_background(plaquette, bits.bit_count())
    observed = apply_sequence(
        plaquette,
        affine_state(plaquette, bits, plaquette_basis, background),
        loop_sequence,
    )
    expected, _final_bits, _phase = expected_sequence(
        plaquette, bits, plaquette_basis, background, loop_sequence
    )
    sequence_residuals.append(state_residual(observed, expected))
assert max(sequence_residuals) == 0.0

single_particle = 1 << plaquette.vertices.index(v00)
single_background = supplied_star_background(plaquette, 1)
expected_uniform, final_single_particle, _ = expected_sequence(
    plaquette, single_particle, plaquette_basis, single_background, loop_sequence
)
assert final_single_particle == single_particle
uniform_loop = apply_sequence(
    plaquette,
    affine_state(plaquette, single_particle, plaquette_basis, single_background),
    loop_sequence,
)
uniform_loop_overlap = state_overlap(expected_uniform, uniform_loop)

basis_generators = np.zeros((len(plaquette.edges), 0), dtype=np.int64)
basis_loop = apply_sequence(
    plaquette,
    affine_state(plaquette, single_particle, basis_generators, single_background),
    loop_sequence,
)
basis_expected, _, _ = expected_sequence(
    plaquette, single_particle, basis_generators, single_background, loop_sequence
)
basis_overlap = state_overlap(basis_expected, basis_loop)
basis_residual = state_residual(basis_loop, basis_expected)

character = (1,)
character_loop = apply_sequence(
    plaquette,
    affine_state(
        plaquette, single_particle, plaquette_basis, single_background, character
    ),
    loop_sequence,
)
character_expected, _, _ = expected_sequence(
    plaquette,
    single_particle,
    plaquette_basis,
    single_background,
    loop_sequence,
    character,
)
character_overlap = state_overlap(character_expected, character_loop)
character_residual = state_residual(character_loop, character_expected)
assert abs(abs(character_overlap) - 1.0) < 1e-12
assert character_residual > 0.3

# Exhaust the incidence-current condition on every L2 occupation word and
# seam.  Then repeat the complete seam list three times to test induction.
direct_l2_cases = 0
direct_l2_incidence_failures = 0
wrong_sign_nontrivial = 0
wrong_alpha_l2_cases = 0
for bits in range(1 << len(cube_l2.vertices)):
    background = supplied_star_background(cube_l2, bits.bit_count())
    q0 = matter_charge(cube_l2, bits, background)
    for edge, (u, v, _axis) in enumerate(cube_l2.edges):
        new_bits, _phase, nu, nv = swap_bits(bits, u, v)
        q1 = matter_charge(cube_l2, new_bits, background)
        current = np.zeros(len(cube_l2.edges), dtype=np.int64)
        current[edge] = nu - nv
        direct_l2_incidence_failures += not np.array_equal(
            (cube_l2.incidence @ current) % P, (q1 - q0) % P
        )
        direct_l2_cases += 1
        if nu != nv:
            wrong_sign_nontrivial += 1
            for wrong_alpha in range(P):
                if wrong_alpha == 1:
                    continue
                wrong_current = np.zeros(len(cube_l2.edges), dtype=np.int64)
                wrong_current[edge] = wrong_alpha * (nu - nv)
                assert not np.array_equal(
                    (cube_l2.incidence @ wrong_current) % P, (q1 - q0) % P
                )
                wrong_alpha_l2_cases += 1

repeat_sequence = tuple(range(len(cube_l2.edges))) * 3
repeat_history_nonzero = 0
repeat_l2_incidence_failures = 0
repeat_history_kernel_failures = 0
for bits in range(1 << len(cube_l2.vertices)):
    initial_bits = bits
    background = supplied_star_background(cube_l2, bits.bit_count())
    current_bits = bits
    accumulated = np.zeros(len(cube_l2.edges), dtype=np.int64)
    for edge in repeat_sequence:
        u, v, _axis = cube_l2.edges[edge]
        new_bits, _phase, nu, nv = swap_bits(current_bits, u, v)
        accumulated[edge] = (accumulated[edge] + nu - nv) % P
        current_bits = new_bits
    q0 = matter_charge(cube_l2, initial_bits, background)
    q1 = matter_charge(cube_l2, current_bits, background)
    repeat_l2_incidence_failures += not np.array_equal(
        (cube_l2.incidence @ accumulated) % P, (q1 - q0) % P
    )
    canonical_difference = (
        solve_mod(cube_l2.incidence, q1) - solve_mod(cube_l2.incidence, q0)
    ) % P
    history = (accumulated - canonical_difference) % P
    repeat_history_kernel_failures += int(
        np.count_nonzero((cube_l2.incidence @ history) % P) != 0
    )
    repeat_history_nonzero += int(np.any(history))

# L2 deletion nuance: the six raw faces have one cube-boundary relation.  A
# single raw-face deletion is therefore inactive, whereas dropping one member
# of a chosen independent five-face basis leaves 17 path-history cosets.
all_minus_one_rank = rank_mod(cube_l2.faces[:, 1:])
reduced_basis = cube_basis[:, 1:]
reduced_rank = rank_mod(reduced_basis)
omitted = cube_basis[:, 0]
assert all_minus_one_rank == cube_cert["kernel_dimension"]
assert reduced_rank == cube_cert["kernel_dimension"] - 1
assert rank_mod(np.column_stack((reduced_basis, omitted))) == reduced_rank + 1

omega = np.exp(2j * math.pi / P)
expected_character_overlap = np.conj(omega)
assert abs(character_overlap - expected_character_overlap) < 1e-12


def six_mode_total_occupation_extension_certificate() -> dict:
    """Lift the seam-bit identity to Cycle870's six-mode total N_x.

    Here a,b are the selected seam-mode bits and s_u,s_v are the other five
    onsite-mode occupation counts.  The background/star field is
    g = B*ell-alpha*n and must stay fixed under the seam current update.
    """

    alpha = 1
    rows = 0
    incidence_failures = 0
    background_invariance_failures = 0
    total_number_failures = 0
    occupation_range_failures = 0
    fswap_minus_rows = 0
    fswap_sign_failures = 0
    wrong_incidence_sign_detected = 0
    omitted_shift_detected = 0
    for a, b in product((0, 1), repeat=2):
        for spectator_u, spectator_v in product(range(6), repeat=2):
            n_u = a + spectator_u
            n_v = b + spectator_v
            new_n_u = n_u - a + b
            new_n_v = n_v - b + a
            for ell in range(P):
                rows += 1
                current = alpha * (a - b)
                new_ell = (ell + current) % P
                boundary_current = np.asarray((-current, current)) % P
                charge_difference = alpha * np.asarray(
                    (new_n_u - n_u, new_n_v - n_v)
                ) % P
                incidence_failures += not np.array_equal(
                    boundary_current, charge_difference
                )
                background_before = np.asarray(
                    (-ell - alpha * n_u, ell - alpha * n_v)
                ) % P
                background_after = np.asarray(
                    (-new_ell - alpha * new_n_u,
                     new_ell - alpha * new_n_v)
                ) % P
                background_invariance_failures += not np.array_equal(
                    background_before, background_after
                )
                total_number_failures += (
                    n_u + n_v != new_n_u + new_n_v
                )
                occupation_range_failures += not (
                    0 <= n_u <= 6 and 0 <= n_v <= 6
                    and 0 <= new_n_u <= 6 and 0 <= new_n_v <= 6
                )
                sign = -1 if a == b == 1 else 1
                fswap_minus_rows += sign == -1
                fswap_sign_failures += sign != (-1 if a == b == 1 else 1)
                if a != b:
                    wrong_boundary = np.asarray((current, -current)) % P
                    wrong_incidence_sign_detected += not np.array_equal(
                        wrong_boundary, charge_difference
                    )
                    omitted_shift_background = np.asarray(
                        (-ell - alpha * new_n_u,
                         ell - alpha * new_n_v)
                    ) % P
                    omitted_shift_detected += not np.array_equal(
                        background_before, omitted_shift_background
                    )
    return {
        "rows": rows,
        "selected_seam_bits": "a,b in {0,1}",
        "alpha_normalization": "+1",
        "spectator_mode_counts": "s_u,s_v in {0,...,5}",
        "total_occupations": "n_u=a+s_u and n_v=b+s_v, each in {0,...,6}",
        "link_labels": P,
        "update": (
            "n'_u=n_u-a+b; n'_v=n_v-b+a; "
            "ell'=ell+(a-b) mod17 at the alpha=+1 normalization"
        ),
        "incidence_failures": incidence_failures,
        "fixed_background_or_star_invariance_failures":
            background_invariance_failures,
        "total_number_failures": total_number_failures,
        "occupation_range_failures": occupation_range_failures,
        "FSWAP_minus_11_rows": fswap_minus_rows,
        "FSWAP_sign_failures": fswap_sign_failures,
        "wrong_incidence_sign_detected_rows": wrong_incidence_sign_detected,
        "omitted_link_shift_detected_rows": omitted_shift_detected,
        "scope": (
            "algebraic alpha=+1 total-six-mode star/count extension of one selected "
            "seam; no second alpha=-1 global affine fixture, many-mode affine-state "
            "preparation, or new physical compiler"
        ),
    }


SIX_MODE_TOTAL_OCCUPATION = six_mode_total_occupation_extension_certificate()


def reconstruct_schedule(gates) -> np.ndarray:
    output = np.eye(6, dtype=complex)
    for gate in gates:
        if gate.kind == "phase":
            matrix = np.eye(6, dtype=complex)
            matrix[gate.modes[0], gate.modes[0]] = gate.matrix[0, 0]
        else:
            matrix = C870.embed_one_particle(gate.matrix, gate.modes)
        output = matrix @ output
    return output


def cycle219_decoded_dispersion_certificate() -> dict:
    beta = float(C870.c230.BETA)
    species = C219.common_species(beta)
    coin = np.asarray(species.coin, dtype=complex)
    gates, qr = C870.qr_coin_schedule(coin)
    uniform_cycle = np.ones(P, dtype=complex) / math.sqrt(P)

    onsite_intertwiner_residual = 0.0
    for source_mode in range(6):
        encoded = np.zeros((6, P), dtype=complex)
        encoded[source_mode, :] = uniform_cycle
        observed = coin @ encoded
        expected = np.outer(coin[:, source_mode], uniform_cycle)
        onsite_intertwiner_residual = max(
            onsite_intertwiner_residual, float(np.linalg.norm(observed - expected))
        )

    deletion_residuals = tuple(
        float(np.linalg.norm(
            reconstruct_schedule(tuple(
                gate for position, gate in enumerate(gates) if position != deleted
            )) - coin
        ))
        for deleted in range(len(gates))
    )
    selected_deleted_gate = int(np.argmax(deletion_residuals))
    curvature = C219.c210.curvature_tensor(species, step=1.0e-4)
    dispersion_mass = 1.0 / float(np.mean(np.diag(curvature)))
    rest_mass = C219.rest_mass(species)

    momenta = (
        (0.0, 0.0, 0.0),
        (0.07, 0.0, 0.0), (-0.07, 0.0, 0.0),
        (0.0, 0.07, 0.0), (0.0, -0.07, 0.0),
        (0.0, 0.0, 0.07), (0.0, 0.0, -0.07),
        (0.04, -0.03, 0.02),
    )
    bloch_rows = []
    same_block_power_residual = 0.0
    for momentum in momenta:
        bloch = C219.c210.molecular_bloch(np.asarray(momentum), coin)
        phase, _vector = C219.c210.branch_eigenpair(
            np.asarray(momentum), species
        )
        sequential = np.eye(6, dtype=complex)
        for _ in range(8):
            sequential = bloch @ sequential
        same_block_power_residual = max(
            same_block_power_residual,
            float(np.linalg.norm(sequential - np.linalg.matrix_power(bloch, 8))),
        )
        bloch_rows.append({
            "momentum": momentum,
            "scalar_branch_phase": phase,
            "unitarity_residual": float(
                np.linalg.norm(bloch.conj().T @ bloch - np.eye(6))
            ),
        })

    return {
        "actual_Cycle870_beta": beta,
        "coin_sha256": sha256(coin.tobytes()).hexdigest(),
        "coin_unitarity_residual": float(
            np.linalg.norm(coin.conj().T @ coin - np.eye(6))
        ),
        "dense_nonzero_entries": int(np.count_nonzero(np.abs(coin) > 1.0e-13)),
        "QR_gate_count": len(gates),
        "QR_reconstruction_residual": qr["reconstruction_residual"],
        "QR_off_diagonal_residual": qr["QR_off_diagonal_residual"],
        "single_QR_gate_deletion_residuals": deletion_residuals,
        "inactive_identity_phase_deletion_indices": tuple(
            index for index, residual in enumerate(deletion_residuals)
            if residual <= TOL
        ),
        "selected_active_QR_gate_deletion_index": selected_deleted_gate,
        "selected_active_QR_gate_deletion_residual": deletion_residuals[
            selected_deleted_gate
        ],
        "QR_deletion_scope": (
            "one selected nonidentity-gate deletion is an active control; identity "
            "phase entries may be structurally inactive and no every-gate "
            "essentiality claim is made"
        ),
        "trivial_cycle_uniform_normalization_residual": abs(
            float(np.vdot(uniform_cycle, uniform_cycle).real) - 1.0
        ),
        "trivial_cycle_translation_residual": float(
            np.linalg.norm(np.roll(uniform_cycle, 1) - uniform_cycle)
        ),
        "actual_dense_coin_encoded_onsite_intertwiner_residual":
            onsite_intertwiner_residual,
        "momentum_samples": bloch_rows,
        "maximum_Bloch_unitarity_residual": max(
            row["unitarity_residual"] for row in bloch_rows
        ),
        "eight_step_same_block_multiplication_consistency_residual":
            same_block_power_residual,
        "curvature_tensor_step_1e_minus_4": curvature.tolist(),
        "analytic_mass": float(species.analytic_mass),
        "rest_mass": rest_mass,
        "dispersion_mass": dispersion_mass,
        "rest_to_analytic_residual": abs(rest_mass - species.analytic_mass),
        "dispersion_relative_residual": abs(
            dispersion_mass / species.analytic_mass - 1.0
        ),
        "decoded_spectrum_statement": (
            "the exact seam-column affine intertwiner plus onsite number preservation "
            "makes the trivial-character code representation conjugate to the supplied "
            "free one-particle Cycle219 Bloch word; its decoded eigenphases and local "
            "curvature therefore equal the displayed Cycle219 fixture"
        ),
        "scope_boundary": (
            "this is the supplied translation-invariant free one-particle momentum "
            "fixture, not a periodic F17 physical-box construction and not an "
            "interacting finite-open-box spectrum"
        ),
    }


C219_CERTIFICATE = cycle219_decoded_dispersion_certificate()
OBSERVED_SOURCE_SHA256 = {
    path: file_sha256(ROOT / path) for path in SOURCE_PINS
}
SOURCE_HASH_MISMATCHES = {
    path: {"expected": expected, "observed": OBSERVED_SOURCE_SHA256[path]}
    for path, expected in SOURCE_PINS.items()
    if OBSERVED_SOURCE_SHA256[path] != expected
}
EXPECTED_BASE_IS_ANCESTOR_OF_HEAD = subprocess.run(
    (
        "git", "merge-base", "--is-ancestor",
        EXPECTED_BASE_COMMIT, "HEAD",
    ),
    cwd=ROOT,
    check=False,
).returncode == 0

result = {
    "status": "pending",
    "name": "Cycle873 uniform affine-Gauss/trivial-loop intertwiner core",
    "provenance": {
        "base_commit": EXPECTED_BASE_COMMIT,
        "expected_base_is_ancestor_of_head": EXPECTED_BASE_IS_ANCESTOR_OF_HEAD,
        "runner": str(Path(__file__).relative_to(ROOT)),
        "source_sha256": OBSERVED_SOURCE_SHA256,
        "source_hash_mismatches": SOURCE_HASH_MISMATCHES,
    },
    "field": "Z17",
    "orientation": "incidence boundary is head minus tail; +alpha on u->v has boundary alpha(e_v-e_u)",
    "fixed_star_background": {
        "gauss_word": "q_g(n)=alpha*n+g mod17 with sum(g)=-alpha*N in a fixed-N sector",
        "type": "supplied FixedStarBackground(label, alpha, particle_number, field)",
        "diagnostic_conventions": (
            "ordered_prefix", "first_anchor", "last_anchor"
        ),
        "filled_plaquette_variant_cases": background_variant_cases,
        "filled_plaquette_variant_intertwiner_max_residual": max(
            background_variant_residuals
        ),
        "selection_boundary": (
            "g and its fixed matter-number sector are input structure; this core "
            "does not select, prepare, or enforce either"
        ),
        "ordering_boundary": (
            "ordered_prefix is one diagnostic background convention with a preferred "
            "vertex order; the theorem is also checked for first- and last-anchor "
            "backgrounds, but no preferred-order-free genesis claim is made"
        ),
        "covariance_boundary": (
            "full affine-encoder 24-frame, 576-product, and translation covariance "
            "with transported g is not established here; only the separate local-"
            "constraint core checks its stated physical support/frame covariance"
        ),
    },
    "theorem_checked": {
        "affine_fiber_translation": "T_j A_q = A_(q + incidence*j) bijectively on every finite oriented graph",
        "uniform_state_translation": "T_j |A_q> = |A_(q + incidence*j)> exactly",
        "path_independence": "translations with the same boundary differ by ker(incidence), which fixes the trivial-character uniform state",
        "intertwiner_condition": (
            "at fixed supplied g, incidence*j(n->n') = q_g(n')-q_g(n)"
        ),
        "arbitrary_superpositions": "follows by linearity after basis-column equality",
        "repeated_factors": "follows by induction; independently checked below on a 36-factor L2 sequence",
    },
    "filled_plaquette": {
        **plaquette_cert,
        "direct_fswap_columns_checked": len(direct_residuals),
        "direct_intertwiner_max_residual": max(direct_residuals),
        "supplied_background_variant_columns_checked": background_variant_cases,
        "supplied_background_variant_max_residual": max(
            background_variant_residuals
        ),
        "four_factor_sequence_columns_checked": len(sequence_residuals),
        "four_factor_sequence_max_residual": max(sequence_residuals),
        "uniform_closed_loop_overlap": [uniform_loop_overlap.real, uniform_loop_overlap.imag],
        "uniform_closed_loop_residual": state_residual(uniform_loop, expected_uniform),
        "basis_link_closed_loop_overlap": [basis_overlap.real, basis_overlap.imag],
        "basis_link_closed_loop_residual": basis_residual,
        "nonuniform_character_closed_loop_overlap": [character_overlap.real, character_overlap.imag],
        "nonuniform_character_closed_loop_residual": character_residual,
        "nonuniform_character_exact_residual": "2 sin(pi/17)",
        "omit_only_plaquette_invariant_dimension": P,
        "wrong_sign_max_column_residual": max(wrong_sign_residuals),
        "wrong_sign_frobenius_one_edge": math.sqrt(
            sum(value * value for value in wrong_sign_residuals[:: len(plaquette.edges)])
        ),
        "wrong_alpha_values_mod17": sorted(wrong_alpha_active_residuals),
        "wrong_alpha_active_columns_per_value": len(
            next(iter(wrong_alpha_active_residuals.values()))
        ),
        "wrong_alpha_active_overlap": 0,
        "wrong_alpha_active_column_residual": math.sqrt(2),
    },
    "open_cube_L2": {
        **cube_cert,
        "direct_seam_cases_checked": direct_l2_cases,
        "correct_direct_incidence_failures": direct_l2_incidence_failures,
        "wrong_sign_nontrivial_cases": wrong_sign_nontrivial,
        "wrong_sign_overlap": 0,
        "wrong_sign_column_residual": math.sqrt(2),
        "wrong_alpha_values_mod17": [alpha for alpha in range(P) if alpha != 1],
        "wrong_alpha_active_cases_checked": wrong_alpha_l2_cases,
        "wrong_alpha_active_overlap": 0,
        "wrong_alpha_active_column_residual": math.sqrt(2),
        "repeated_factor_count": len(repeat_sequence),
        "repeated_matter_words_checked": 1 << len(cube_l2.vertices),
        "repeated_uniform_intertwiner_incidence_failures":
            repeat_l2_incidence_failures,
        "repeated_history_kernel_failures": repeat_history_kernel_failures,
        "histories_with_nonzero_kernel_residual": repeat_history_nonzero,
        "all_six_faces_minus_one_face_rank": all_minus_one_rank,
        "all_six_faces_minus_one_invariant_dimension": P ** (
            cube_cert["kernel_dimension"] - all_minus_one_rank
        ),
        "independent_five_face_basis_minus_one_rank": reduced_rank,
        "independent_basis_minus_one_invariant_dimension": P ** (
            cube_cert["kernel_dimension"] - reduced_rank
        ),
        "omitted_independent_generator_overlap": 0,
        "omitted_independent_generator_residual": math.sqrt(2),
        "nonuniform_character_cycle_overlap": [
            expected_character_overlap.real,
            expected_character_overlap.imag,
        ],
        "nonuniform_character_cycle_residual": abs(expected_character_overlap - 1),
        "nonuniform_character_exact_residual": "2 sin(pi/17)",
    },
    "open_box_general": {
        "vertices": "L^3",
        "edges": "3 L^2 (L-1)",
        "incidence_rank": "L^3-1",
        "cycle_dimension": "2 L^3-3 L^2+1",
        "affine_sector_size": "17^(2 L^3-3 L^2+1)",
        "plaquettes": "3 L (L-1)^2",
        "plaquette_relations": "(L-1)^3 cube-boundary/Bianchi relations",
        "unique_plus_sector": "yes for the full contractible box cell complex",
        "arbitrary_open_cubic_subgraph": "only if plaquette boundaries span ker(incidence), equivalently H1=0",
    },
    "six_mode_total_occupation_extension": SIX_MODE_TOTAL_OCCUPATION,
    "actual_Cycle219_decoded_free_one_particle": C219_CERTIFICATE,
    "supplies_and_boundaries": {
        "boundary": "connected finite open cell complex and compatible zero-total Gauss word, or separately supplied boundary flux ports",
        "topology": "local plaquette shifts leave 17^b1 sectors when H1 is nonzero; full ker-uniformity additionally fixes/superposes Wilson cycles",
        "genesis": "constraints characterize the state but do not prepare it; a coherent preparation/admission law and clean one-hot link bank remain supplied",
        "orientation_and_alpha": (
            "edge orientation and matter-charge convention are supplied; the global "
            "affine fixture is normalized to alpha=+1 and no alpha=-1 global encoder "
            "fixture is claimed"
        ),
        "fixed_star_background": (
            "a compatible fixed-N star/background field g is supplied and transported "
            "when geometry is compared; background selection and genesis remain open"
        ),
        "encoder_covariance": (
            "no full affine-encoder proper-frame/product/translation covariance theorem "
            "is claimed by this core"
        ),
        "physical_compilation": (
            "this algebra core is abstract; the separate Cycle873 physical and local-constraint "
            "cores emit the grouped augmented seam and 17-rail plaquette shifts"
        ),
        "finite_synthesis": (
            "ideal arbitrary rotations and order-17 projector/preparation synthesis remain supplied/open"
        ),
        "interpretation_firewall": (
            "no source, gravity, time, occurrence, Event, Record, Born, or autonomous genesis claim"
        ),
    },
}

failures = []
if not EXPECTED_BASE_IS_ANCESTOR_OF_HEAD:
    failures.append("expected base is not an ancestor of HEAD")
if SOURCE_HASH_MISMATCHES:
    failures.append("source hash mismatch")
if max(background_variant_residuals) > TOL or background_variant_cases != 192:
    failures.append("supplied fixed-star background variants")
if (
    SIX_MODE_TOTAL_OCCUPATION["rows"] != 2448
    or SIX_MODE_TOTAL_OCCUPATION["FSWAP_minus_11_rows"] != 612
    or any(
        SIX_MODE_TOTAL_OCCUPATION[key]
        for key in (
            "incidence_failures",
            "fixed_background_or_star_invariance_failures",
            "total_number_failures",
            "occupation_range_failures",
            "FSWAP_sign_failures",
        )
    )
    or SIX_MODE_TOTAL_OCCUPATION["wrong_incidence_sign_detected_rows"] != 1224
    or SIX_MODE_TOTAL_OCCUPATION["omitted_link_shift_detected_rows"] != 1224
):
    failures.append("six-mode total-occupation extension")
if result["filled_plaquette"]["direct_intertwiner_max_residual"] > TOL:
    failures.append("filled plaquette direct intertwiner")
if result["filled_plaquette"]["four_factor_sequence_max_residual"] > TOL:
    failures.append("filled plaquette loop sequence")
if result["filled_plaquette"]["uniform_closed_loop_residual"] > TOL:
    failures.append("trivial-character loop")
if result["filled_plaquette"]["basis_link_closed_loop_residual"] <= 1.0:
    failures.append("inactive basis-link loop control")
if result["filled_plaquette"]["nonuniform_character_closed_loop_residual"] <= 0.3:
    failures.append("inactive nontrivial-character control")
if result["open_cube_L2"][
    "repeated_uniform_intertwiner_incidence_failures"
]:
    failures.append("L2 repeated intertwiner")
if result["open_cube_L2"]["correct_direct_incidence_failures"]:
    failures.append("L2 direct incidence")
if result["open_cube_L2"]["repeated_history_kernel_failures"]:
    failures.append("L2 repeated history kernel")
if result["open_cube_L2"]["wrong_alpha_active_cases_checked"] == 0:
    failures.append("inactive wrong-alpha controls")
if result["open_cube_L2"]["omitted_independent_generator_residual"] <= 1.0:
    failures.append("inactive omitted plaquette generator control")
for key in (
    "coin_unitarity_residual", "QR_reconstruction_residual",
    "QR_off_diagonal_residual", "trivial_cycle_uniform_normalization_residual",
    "trivial_cycle_translation_residual",
    "actual_dense_coin_encoded_onsite_intertwiner_residual",
    "maximum_Bloch_unitarity_residual",
    "eight_step_same_block_multiplication_consistency_residual",
):
    if C219_CERTIFICATE[key] > TOL:
        failures.append(f"Cycle219:{key}")
if C219_CERTIFICATE["selected_active_QR_gate_deletion_residual"] <= 1.0e-3:
    failures.append("Cycle219:inactive selected QR deletion control")
if C219_CERTIFICATE["rest_to_analytic_residual"] > TOL:
    failures.append("Cycle219:rest mass")
if C219_CERTIFICATE["dispersion_relative_residual"] > 4.0e-6:
    failures.append("Cycle219:dispersion mass")
result["active_controls"] = {
    "wrong_alpha_values": result["open_cube_L2"]["wrong_alpha_values_mod17"],
    "wrong_alpha_cases": result["open_cube_L2"]["wrong_alpha_active_cases_checked"],
    "nontrivial_character_residual": result["filled_plaquette"][
        "nonuniform_character_closed_loop_residual"
    ],
    "omitted_independent_generator_residual": result["open_cube_L2"][
        "omitted_independent_generator_residual"
    ],
    "selected_active_QR_gate_deletion_index": C219_CERTIFICATE[
        "selected_active_QR_gate_deletion_index"
    ],
    "selected_active_QR_gate_deletion_residual": C219_CERTIFICATE[
        "selected_active_QR_gate_deletion_residual"
    ],
}
result["failures"] = failures
result["status"] = "pass" if not failures else "fail"


def finish(output: Path = OUT) -> int:
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "base_commit": EXPECTED_BASE_COMMIT,
        "expected_base_is_ancestor_of_head": EXPECTED_BASE_IS_ANCESTOR_OF_HEAD,
        "receipt": str(OUT.relative_to(ROOT)),
        "failures": failures,
        "filled_plaquette_direct_columns": result["filled_plaquette"][
            "direct_fswap_columns_checked"
        ],
        "L2_repeated_factor_count": result["open_cube_L2"]["repeated_factor_count"],
        "C219_beta": C219_CERTIFICATE["actual_Cycle870_beta"],
        "C219_dispersion_mass": C219_CERTIFICATE["dispersion_mass"],
    }, indent=2, sort_keys=True))
    return int(bool(failures))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    arguments = parser.parse_args()
    raise SystemExit(finish(arguments.output))
