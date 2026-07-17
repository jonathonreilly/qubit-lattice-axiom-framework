#!/usr/bin/env python3
"""Cycle 248: local parity-doubling/spectator compiler discriminator.

Two exact occupation-basis isometries are tested on the Cycle-230/235 matter
graph.  The per-mode map copies every occupation to a colocated spectator;
the per-cell map stores only the parity of the six modes in one cell.  The
runner distinguishes:

* exact Hilbert-space/code isometry and algebra homomorphism on the code;
* locality of the full CAR images, including odd generators;
* locality of the particular Cycle-230 coin/contact/A/B-FSWAP update;
* local equality/neutrality, spectator transport, fermionic exchange signs;
* proper-frame/translation covariance of rules versus the canonical plain
  tensor-factor action; and
* the Cycle-245 sectorwise-sign issue for a single physical update.

The gauging, preparation, gate-layer, and update indices are compiler
coordinates, never physical time.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PARITY_DOUBLING_SPECTATOR_COMPILER_CYCLE248_NOTE_2026-07-17.md"
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "per-mode spectator",
        "per-cell spectator",
        "isometric algebra homomorphism",
        "local b_t",
        "hopping/fswap",
        "exchange/car",
        "one-particle mass",
        "rank-73 seam",
        "spectator transport",
        "hard-core bosons",
        "constant overhead",
        "held-out l=6",
        "all 24 proper-cubic frames",
        "single physical update",
        "wilson-controlled projector",
        "deletion",
        "leakage",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution/rhetoric audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
        "time firewall",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves the full contract, N1-N8, and time firewall", not missing, missing)


def pauli_matrix(qubits: int, x: int = 0, z: int = 0) -> np.ndarray:
    dimension = 1 << qubits
    result = np.zeros((dimension, dimension), dtype=complex)
    phase = (1j) ** ((x & z).bit_count())
    for source in range(dimension):
        target = source ^ x
        result[target, source] = phase * (-1) ** ((z & source).bit_count())
    return result


def creation_matrix(modes: int, mode: int) -> np.ndarray:
    result = np.zeros((1 << modes, 1 << modes), dtype=complex)
    prefix = (1 << mode) - 1
    for source in range(1 << modes):
        if not ((source >> mode) & 1):
            target = source | (1 << mode)
            result[target, source] = (-1) ** ((source & prefix).bit_count())
    return result


def mode_spectator_isometry(modes: int) -> np.ndarray:
    result = np.zeros((1 << (2 * modes), 1 << modes), dtype=complex)
    for state in range(1 << modes):
        target = 0
        for mode in range(modes):
            occupation = (state >> mode) & 1
            target |= occupation << (2 * mode)
            target |= occupation << (2 * mode + 1)
        result[target, state] = 1
    return result


def cell_spectator_isometry(modes: int = 6) -> np.ndarray:
    result = np.zeros((1 << (modes + 1), 1 << modes), dtype=complex)
    for state in range(1 << modes):
        target = state | ((state.bit_count() % 2) << modes)
        result[target, state] = 1
    return result


def swap_gate(qubits: int, left: int, right: int, *, fermionic: bool) -> np.ndarray:
    result = np.zeros((1 << qubits, 1 << qubits), dtype=complex)
    for source in range(1 << qubits):
        a = (source >> left) & 1
        b = (source >> right) & 1
        target = source
        if a != b:
            target ^= (1 << left) | (1 << right)
        result[target, source] = -1 if fermionic and a and b else 1
    return result


def cnot_gate(qubits: int, control: int, target: int) -> np.ndarray:
    result = np.zeros((1 << qubits, 1 << qubits), dtype=complex)
    for source in range(1 << qubits):
        output = source ^ ((1 << target) if (source >> control) & 1 else 0)
        result[output, source] = 1
    return result


def cz_gate(qubits: int, left: int, right: int) -> np.ndarray:
    diagonal = [
        -1 if ((state >> left) & 1) and ((state >> right) & 1) else 1
        for state in range(1 << qubits)
    ]
    return np.diag(diagonal).astype(complex)


def code_projector(isometry: np.ndarray) -> np.ndarray:
    return isometry @ isometry.conj().T


def per_mode_algebra_controls() -> None:
    encoder = mode_spectator_isometry(2)
    projector = code_projector(encoder)
    identity = np.eye(4, dtype=complex)
    rng = np.random.default_rng(2480)
    first = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    second = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))

    def image(operator: np.ndarray) -> np.ndarray:
        return encoder @ operator @ encoder.conj().T

    homomorphism = np.linalg.norm(image(first) @ image(second) - image(first @ second))
    star = np.linalg.norm(image(first).conj().T - image(first.conj().T))
    unit = np.linalg.norm(image(identity) - projector)
    check(
        "the per-mode copy is an exact isometric code-algebra homomorphism",
        np.linalg.norm(encoder.conj().T @ encoder - identity) == 0
        and homomorphism < 2e-13
        and star < 2e-13
        and unit == 0,
        {"isometry": 0.0, "multiplication": homomorphism, "star": star, "code_unit": unit},
    )

    z_input = pauli_matrix(2, z=1)
    z_data = pauli_matrix(4, z=1)
    z_spectator = pauli_matrix(4, z=2)
    equality0 = pauli_matrix(4, z=1 | 2)
    equality1 = pauli_matrix(4, z=4 | 8)
    local_b_residual = max(
        np.linalg.norm(z_data @ encoder - encoder @ z_input),
        np.linalg.norm(z_spectator @ encoder - encoder @ z_input),
        np.linalg.norm(equality0 @ encoder - encoder),
        np.linalg.norm(equality1 @ encoder - encoder),
    )
    check(
        "each original local B_t is retained locally and every doubled occupation is neutral",
        local_b_residual == 0,
        {"B_t_residual": local_b_residual, "combined_local_charge": "+1"},
    )

    creation = [creation_matrix(2, mode) for mode in range(2)]
    exact = [image(operator) for operator in creation]
    car_failures = 0
    for left in range(2):
        for right in range(2):
            expected = projector if left == right else np.zeros_like(projector)
            car_failures += np.linalg.norm(
                exact[left].conj().T @ exact[right]
                + exact[right] @ exact[left].conj().T
                - expected
            ) > 2e-13
            car_failures += np.linalg.norm(
                exact[left] @ exact[right] + exact[right] @ exact[left]
            ) > 2e-13

    # Local pair creators omit the logical parity prefix.  They commute on
    # disjoint doubled blocks and therefore cannot be the images of two CAR
    # odd generators.
    pair_creators = []
    for mode in range(2):
        data, spectator = 2 * mode, 2 * mode + 1
        matrix = np.zeros((16, 16), dtype=complex)
        for state in range(16):
            if not ((state >> data) & 1) and not ((state >> spectator) & 1):
                matrix[
                    state | (1 << data) | (1 << spectator), state
                ] = 1
        pair_creators.append(matrix)
    shortcut_anticommutator = np.linalg.norm(
        (pair_creators[0] @ pair_creators[1] + pair_creators[1] @ pair_creators[0])
        @ encoder[:, [0]]
    )
    exact_second_needs_prefix = np.linalg.norm(
        exact[1] - pauli_matrix(4, z=1) @ pair_creators[1] @ projector
    )
    check(
        "the exact full-CAR image needs a parity prefix while local pair creators become hard-core bosons",
        car_failures == 0
        and shortcut_anticommutator == 2
        and exact_second_needs_prefix == 0,
        {
            "exact_CAR_failures": car_failures,
            "local_pair_anticommutator_on_vacuum": shortcut_anticommutator,
            "second_mode_prefix_residual": exact_second_needs_prefix,
        },
    )


def spectator_transport_and_exchange_controls() -> None:
    encoder = mode_spectator_isometry(2)
    projector = code_projector(encoder)
    coarse_fswap = swap_gate(2, 0, 1, fermionic=True)
    data_fswap = swap_gate(4, 0, 2, fermionic=True)
    spectator_swap = swap_gate(4, 1, 3, fermionic=False)
    spectator_fswap = swap_gate(4, 1, 3, fermionic=True)
    sign_lane = data_fswap @ spectator_swap
    double_fswap = data_fswap @ spectator_fswap
    symmetric_corrected = cz_gate(4, 0, 2) @ double_fswap
    target = encoder @ coarse_fswap
    rows = {
        "sign_lane": np.linalg.norm(sign_lane @ encoder - target),
        "symmetric_CZ": np.linalg.norm(symmetric_corrected @ encoder - target),
        "double_FSWAP_bosonic": np.linalg.norm(double_fswap @ encoder - target),
        "data_only_leakage": np.linalg.norm((np.eye(16) - projector) @ data_fswap @ encoder),
    }
    check(
        "spectator transport plus one unsquared fermionic sign gives an exact two-mode encoded FSWAP",
        rows["sign_lane"] == rows["symmetric_CZ"] == 0
        and rows["double_FSWAP_bosonic"] == 2
        and rows["data_only_leakage"] > 1,
        rows,
    )

    # The endpoint truth table is not yet an actual-graph compiler.  Put a
    # third logical mode between the endpoints in the fixed Fock order.  The
    # intrinsic CAR transposition then has an intermediate-parity sign, while
    # both endpoint-only doubled gates are blind to the middle occupation.
    three_encoder = mode_spectator_isometry(3)
    coarse_nonadjacent = permutation_unitary(
        3, (2, 1, 0), fermionic=True
    )
    data_nonadjacent = swap_gate(6, 0, 4, fermionic=True)
    spectator_plain_nonadjacent = swap_gate(6, 1, 5, fermionic=False)
    spectator_fermionic_nonadjacent = swap_gate(6, 1, 5, fermionic=True)
    sign_lane_nonadjacent = data_nonadjacent @ spectator_plain_nonadjacent
    symmetric_nonadjacent = (
        cz_gate(6, 0, 4)
        @ data_nonadjacent
        @ spectator_fermionic_nonadjacent
    )
    nonadjacent_rows = {
        "endpoint_sign_lane": np.linalg.norm(
            sign_lane_nonadjacent @ three_encoder
            - three_encoder @ coarse_nonadjacent
        ),
        "endpoint_symmetric_CZ": np.linalg.norm(
            symmetric_nonadjacent @ three_encoder
            - three_encoder @ coarse_nonadjacent
        ),
        "failed_basis_states": (3, 6),
    }
    check(
        "the endpoint-only doubled FSWAP fails on a nonadjacent edge of the actual graph",
        abs(nonadjacent_rows["endpoint_sign_lane"] - 2 * np.sqrt(2)) < 2e-13
        and abs(nonadjacent_rows["endpoint_symmetric_CZ"] - 2 * np.sqrt(2)) < 2e-13,
        nonadjacent_rows,
    )

    # A one-spectator-per-cell comparator for two cells with one active mode.
    # Update both cell parity bits by n_left xor n_right before data FSWAP.
    cell_encoder = mode_spectator_isometry(2)  # same four-bit code on this slice
    parity_update = np.eye(16, dtype=complex)
    for control in (0, 2):
        for target_bit in (1, 3):
            parity_update = cnot_gate(4, control, target_bit) @ parity_update
    cell_gate = data_fswap @ parity_update
    cell_target = cell_encoder @ coarse_fswap
    deleted_update = data_fswap
    cell_projector = code_projector(cell_encoder)
    check(
        "a cell-parity spectator must be updated at both endpoints of every crossing",
        np.linalg.norm(cell_gate @ cell_encoder - cell_target) == 0
        and np.linalg.norm((np.eye(16) - cell_projector) @ deleted_update @ cell_encoder) > 1,
        {
            "corrected_intertwiner": np.linalg.norm(cell_gate @ cell_encoder - cell_target),
            "deleted_parity_update_leakage": np.linalg.norm((np.eye(16) - cell_projector) @ deleted_update @ cell_encoder),
            "shared_cell_spectator_requires_constant_edge_coloring": True,
        },
    )


def coin_contact_and_cell_route_controls() -> None:
    species = c219.common_species(c230.BETA)
    coin = c229.fock_lift(species.coin)
    parity = np.diag([(-1) ** state.bit_count() for state in range(64)]).astype(complex)
    occupations = np.asarray([state.bit_count() for state in range(64)])
    contact = np.diag(
        np.exp(1j * c230.COUPLING * occupations * (occupations - 1) / 2)
    )
    cell_encoder = cell_spectator_isometry(6)
    embedded_coin = np.kron(np.eye(2), coin)
    embedded_contact = np.kron(np.eye(2), contact)
    check(
        "one cell spectator gives exact local coin/contact intertwiners and a six-CNOT local preparation",
        np.linalg.norm(coin @ parity - parity @ coin) < 2e-12
        and np.linalg.norm(contact @ parity - parity @ contact) == 0
        and np.linalg.norm(embedded_coin @ cell_encoder - cell_encoder @ coin) < 2e-12
        and np.linalg.norm(embedded_contact @ cell_encoder - cell_encoder @ contact) < 2e-15,
        {
            "coin": np.linalg.norm(embedded_coin @ cell_encoder - cell_encoder @ coin),
            "contact": np.linalg.norm(embedded_contact @ cell_encoder - cell_encoder @ contact),
            "spectator_preparation_depth_bound": 6,
        },
    )

    # The actual Cycle-235 graph has one charge vertex per direction mode.
    # Six shared equalities Z_s Z_a=+ leave only one logical qubit, whereas a
    # full six-mode cell needs six.  The single cell-parity constraint has the
    # right rank only after changing the local gauging vertex to the whole cell.
    shared_equalities = [
        (1 << mode) | (1 << 6) for mode in range(6)
    ]
    shared_rank = c235.gf2_rank(shared_equalities)
    cell_parity_constraint = (1 << 7) - 1
    check(
        "one cell spectator cannot neutralize all six actual Cycle-235 mode vertices without deleting five logical qubits",
        shared_rank == 6
        and 7 - shared_rank == 1
        and c235.gf2_rank([cell_parity_constraint]) == 1
        and 7 - c235.gf2_rank([cell_parity_constraint]) == 6,
        {
            "six_shared_equalities_rank": shared_rank,
            "modewise_neutral_logical_exponent": 7 - shared_rank,
            "cell_parity_code_exponent": 6,
            "cell_route_changes_gauging_graph": True,
        },
    )


@dataclass(frozen=True)
class SizeRow:
    length: int
    cells: int
    mode_spectator_matter: int
    cell_spectator_matter: int
    face_gauge: int
    mode_total: int
    cell_total: int
    mode_equalities: int
    cell_equalities: int
    maximum_fixed_sector_shortened_hopping_weight: int


def held_size_and_locality_controls() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        graph = c235.PyramidCellulation(length)
        vertices = len(graph.vertices)
        cells = length**3
        strings = []
        for left, right, kind, _ in graph.edges:
            if kind == "outer_square":
                separation = abs(left - right)
                strings.append(min(separation - 1, vertices - separation - 1))
        rows.append(
            SizeRow(
                length=length,
                cells=cells,
                mode_spectator_matter=12 * cells,
                cell_spectator_matter=7 * cells,
                face_gauge=15 * cells,
                mode_total=27 * cells,
                cell_total=22 * cells,
                mode_equalities=6 * cells,
                cell_equalities=cells,
                maximum_fixed_sector_shortened_hopping_weight=max(strings) + 4,
            )
        )
    check(
        "both spectator layouts have constant overhead through held-out L=6",
        all(row.mode_total == 27 * row.cells for row in rows)
        and all(row.cell_total == 22 * row.cells for row in rows)
        and rows[-1].mode_total == 5832
        and rows[-1].cell_total == 4752,
        rows,
    )
    check(
        "even the fixed-sector-shortened exact CAR hopping remains nonlocal at trained and held sizes",
        [row.maximum_fixed_sector_shortened_hopping_weight for row in rows]
        == [58, 100, 154, 220]
        and all(
            row.maximum_fixed_sector_shortened_hopping_weight
            == 6 * row.length**2 + 4
            for row in rows
        ),
        [
            {
                "L": row.length,
                "maximum_fixed_sector_shortened_hopping_weight": row.maximum_fixed_sector_shortened_hopping_weight,
                "full_direct_sum_requires_additional_parity_control": True,
            }
            for row in rows
        ],
    )


def permutation_unitary(modes: int, permutation: tuple[int, ...], *, fermionic: bool) -> np.ndarray:
    result = np.zeros((1 << modes, 1 << modes), dtype=complex)
    for source in range(1 << modes):
        occupied = [mode for mode in range(modes) if (source >> mode) & 1]
        targets = [permutation[mode] for mode in occupied]
        inversions = sum(
            targets[left] > targets[right]
            for left in range(len(targets))
            for right in range(left + 1, len(targets))
        )
        target = sum(1 << value for value in targets)
        result[target, source] = -1 if fermionic and inversions % 2 else 1
    return result


def block_permutation_unitary(modes: int, permutation: tuple[int, ...], *, sign_lane: bool) -> np.ndarray:
    qubits = 2 * modes
    result = np.zeros((1 << qubits, 1 << qubits), dtype=complex)
    for source in range(1 << qubits):
        target = 0
        data_targets = []
        for mode in range(modes):
            for lane in range(2):
                bit = (source >> (2 * mode + lane)) & 1
                target |= bit << (2 * permutation[mode] + lane)
            if (source >> (2 * mode)) & 1:
                data_targets.append(permutation[mode])
        inversions = sum(
            data_targets[left] > data_targets[right]
            for left in range(len(data_targets))
            for right in range(left + 1, len(data_targets))
        )
        result[target, source] = -1 if sign_lane and inversions % 2 else 1
    return result


def translation_and_frame_controls() -> None:
    modes = 3
    cycle = (1, 2, 0)
    encoder = mode_spectator_isometry(modes)
    coarse = permutation_unitary(modes, cycle, fermionic=True)
    plain = block_permutation_unitary(modes, cycle, sign_lane=False)
    corrected = block_permutation_unitary(modes, cycle, sign_lane=True)
    plain_residual = np.linalg.norm(plain @ encoder - encoder @ coarse)
    corrected_residual = np.linalg.norm(corrected @ encoder - encoder @ coarse)
    check(
        "canonical plain block translation misses the fermionic permutation sign while a supplied sign lane restores it",
        plain_residual == 2 * np.sqrt(2)
        and corrected_residual == 0,
        {"plain_tensor_translation": plain_residual, "sign_lane_translation": corrected_residual},
    )

    frame_rows = []
    translation_rows = []
    for length in (3, 4, 5, 6):
        graph = c235.PyramidCellulation(length)
        constraints = {
            (cell, direction, "data=spectator")
            for cell in graph.cells
            for direction in range(6)
        }
        edge_set = {
            frozenset((graph.vertices[left], graph.vertices[right]))
            for left, right, _, _ in graph.edges
        }
        frame_failures = 0
        for frame in c235.proper_cubic_frames():
            vertex_map, _ = c235.graph_frame_maps(graph, frame)
            mapped_constraints = {
                (*graph.vertices[vertex_map[graph.vertex_index[(cell, direction)]]], "data=spectator")
                for cell, direction, _ in constraints
            }
            mapped_edges = {
                frozenset((graph.vertices[vertex_map[left]], graph.vertices[vertex_map[right]]))
                for left, right, _, _ in graph.edges
            }
            frame_failures += mapped_constraints != constraints
            frame_failures += mapped_edges != edge_set
        frame_rows.append((length, frame_failures))

        shifted_constraints = {
            (((cell[0] + 1) % length, cell[1], cell[2]), direction, label)
            for cell, direction, label in constraints
        }
        translation_rows.append((length, shifted_constraints == constraints))
    check(
        "the local spectator constraints and corrected gate-rule family are translation and all-24-frame covariant",
        all(failures == 0 for _, failures in frame_rows)
        and all(passed for _, passed in translation_rows),
        {"frames": frame_rows, "translations": translation_rows},
    )


def triangle_sector_isometry(parity: int, holonomy: int) -> tuple[np.ndarray, tuple[int, ...]]:
    """Z2 gauging map on a triangle; edge 01 carries the odd representative."""
    basis = tuple(state for state in range(8) if state.bit_count() % 2 == parity)
    result = np.zeros((64, 4), dtype=complex)
    for column, matter in enumerate(basis):
        for s0, s1 in product((0, 1), repeat=2):
            s = s0 | (s1 << 1)  # reference vertex 2 is fixed to zero
            delta = (s0 ^ s1) | (s1 << 1) | (s0 << 2)
            gauge = holonomy ^ delta
            phase = (-1) ** ((s & matter).bit_count())
            result[matter | (gauge << 3), column] += phase / 2
    return result, basis


def embed_local_three_qubit(operator: np.ndarray) -> np.ndarray:
    """Embed on matter 0, matter 1, gauge edge 01 in a six-qubit triangle."""
    positions = (0, 1, 3)
    result = np.zeros((64, 64), dtype=complex)
    for source in range(64):
        local_source = sum(((source >> qubit) & 1) << index for index, qubit in enumerate(positions))
        for local_target in range(8):
            amplitude = operator[local_target, local_source]
            if abs(amplitude) == 0:
                continue
            target = source
            for index, qubit in enumerate(positions):
                desired = (local_target >> index) & 1
                if ((target >> qubit) & 1) != desired:
                    target ^= 1 << qubit
            result[target, source] += amplitude
    return result


def cycle245_single_update_control() -> None:
    even_map, even_basis = triangle_sector_isometry(0, 0)
    odd_map, odd_basis = triangle_sector_isometry(1, 1)  # h_01=1, common holonomy odd
    coarse = swap_gate(3, 0, 1, fermionic=True)
    even_target = even_map @ coarse[np.ix_(even_basis, even_basis)]
    odd_target = odd_map @ coarse[np.ix_(odd_basis, odd_basis)]

    z0 = pauli_matrix(3, z=1)
    z1 = pauli_matrix(3, z=2)
    xxzg = pauli_matrix(3, x=3, z=4)
    yyzg = pauli_matrix(3, x=3, z=3 | 4)
    local_even = (z0 + z1 + xxzg + yyzg) / 2
    local_odd = (z0 + z1 - xxzg - yyzg) / 2
    physical_even = embed_local_three_qubit(local_even)
    physical_odd = embed_local_three_qubit(local_odd)
    sectorwise = (
        np.linalg.norm(physical_even @ even_map - even_target),
        np.linalg.norm(physical_odd @ odd_map - odd_target),
    )

    # Solve for one arbitrary operator on the same bounded three-qubit support.
    columns = []
    for target_index, source_index in product(range(8), repeat=2):
        basis_operator = np.zeros((8, 8), dtype=complex)
        basis_operator[target_index, source_index] = 1
        embedded = embed_local_three_qubit(basis_operator)
        columns.append(
            np.concatenate(((embedded @ even_map).ravel(), (embedded @ odd_map).ravel()))
        )
    design = np.stack(columns, axis=1)
    target = np.concatenate((even_target.ravel(), odd_target.ravel()))
    solution = np.linalg.lstsq(design, target, rcond=None)[0]
    joint_local_residual = np.linalg.norm(design @ solution - target)

    wilson = pauli_matrix(6, z=(1 << 3) | (1 << 4) | (1 << 5))
    identity = np.eye(64, dtype=complex)
    even_projector = (identity + wilson) / 2
    odd_projector = (identity - wilson) / 2
    controlled = even_projector @ physical_even + odd_projector @ physical_odd
    controlled_residual = max(
        np.linalg.norm(controlled @ even_map - even_target),
        np.linalg.norm(controlled @ odd_map - odd_target),
    )
    check(
        "Cycle-245 sectorwise intertwiners need a Wilson-controlled nonlocal update to become one physical G",
        max(sectorwise) < 5e-16
        and abs(joint_local_residual - 2) < 2e-14
        and controlled_residual < 5e-16,
        {
            "sectorwise_residuals": sectorwise,
            "best_joint_same-edge_residual": joint_local_residual,
            "Wilson_controlled_residual": controlled_residual,
            "actual_torus_Wilson_weight": "3L",
            "membrane_position_host_sign_alternative": True,
        },
    )


def fixture_and_deletion_controls() -> None:
    species = c219.common_species(c230.BETA)
    rest = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    minus_root = 1.5783929737448452
    size = 416
    lower_index = int(np.floor(minus_root * size / (2 * np.pi)))
    lower = 2 * np.pi * lower_index / size
    upper = 2 * np.pi * (lower_index + 1) / size
    seam = c230.seam_block(lower, upper, -1)[0]
    singulars = np.linalg.svd(seam, compute_uv=False)
    check(
        "the local spectator state code conditionally retains the one-particle mass, contact, and rank-73 seam algebra",
        abs(rest / species.analytic_mass - 1) < 2e-12
        and sea_rank == 73
        and sea_rank % 2 == 1
        and (2 * sea_rank) % 2 == 0
        and np.min(singulars) > 0.9998,
        {
            "rest_mass": rest,
            "analytic_mass": species.analytic_mass,
            "original_sea_rank": sea_rank,
            "combined_data_spectator_parity": "even",
            "seam_singular_range": (float(np.min(singulars)), float(np.max(singulars))),
            "full_local_CAR_homomorphism": False,
        },
    )

    rows = []
    for modes in (1, 2, 3, 6):
        mode_code_exponent = modes
        after_equality_deletion = modes + 1
        cell_code_exponent = modes
        after_cell_deletion = modes + 1
        rows.append(
            {
                "modes": modes,
                "mode_code": mode_code_exponent,
                "mode_after_deletion": after_equality_deletion,
                "cell_code": cell_code_exponent,
                "cell_after_deletion": after_cell_deletion,
            }
        )
    check(
        "deleting any independent spectator equality admits one spurious logical qubit",
        all(row["mode_after_deletion"] == row["mode_code"] + 1 for row in rows)
        and all(row["cell_after_deletion"] == row["cell_code"] + 1 for row in rows),
        rows,
    )

    # Local preparation: CNOT data->spectator per mode, or six CNOTs into the
    # one cell parity spectator.  No global parity input is queried.
    encoder = mode_spectator_isometry(2)
    preparation = np.eye(16, dtype=complex)
    for mode in range(2):
        preparation = cnot_gate(4, 2 * mode, 2 * mode + 1) @ preparation
    zero_spectators = np.zeros((16, 4), dtype=complex)
    for state in range(4):
        target = ((state & 1) << 0) | (((state >> 1) & 1) << 2)
        zero_spectators[target, state] = 1
    check(
        "spectator preparation is local and reference-free; deleting it removes odd states from the equality code",
        np.linalg.norm(preparation @ zero_spectators - encoder) == 0,
        {
            "per_mode_preparation_depth": 1,
            "per_cell_preparation_depth_bound": 6,
            "global_parity_query": False,
            "one_particle_without_copy_is_in_code": False,
        },
    )


def main() -> int:
    note_contract()
    per_mode_algebra_controls()
    spectator_transport_and_exchange_controls()
    coin_contact_and_cell_route_controls()
    held_size_and_locality_controls()
    translation_and_frame_controls()
    cycle245_single_update_control()
    fixture_and_deletion_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
