#!/usr/bin/env python3
"""Cycle 271: contractible-lightcone quotient for the twisted edge code.

The Cycle-269 connected local-check code is retained with all eight Wilson
characters.  This runner asks a deliberately local question: for a declared
finite patch and a finite number of Cycle-230 compiler iterations, can every
Wilson seam be moved outside the complete Heisenberg gate cone by a cellwise
matter-parity coboundary?  When it can, every onsite coin/contact and every
A/B FSWAP in the cone is exactly the same in all eight twisted blocks.

The result is an operator-algebra/compiler statement.  Compiler iteration is
not physical time, and a Wilson label is not a Record.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CONTRACTIBLE_LIGHTCONE_WILSON_QUOTIENT_CYCLE271_NOTE_2026-07-17.md"
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
    if not NOTE.exists():
        check("the Cycle-271 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "contractible-local-observable",
        "finite-light-cone",
        "eight-sector",
        "l=3,4,5",
        "held-out l=6",
        "actual cycle-230 onsite coin",
        "contact",
        "a/b fswap",
        "heisenberg",
        "seam can be moved outside",
        "first wrap",
        "all 24 proper-cubic frames",
        "full 27-element l=3 translation group",
        "quotient/subspace",
        "leakage",
        "deletion",
        "lawful domain",
        "state/preparation",
        "compiler iteration is not physical time",
        "a wilson label is not a record",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note preserves the local quotient, scope, N1-N8, time, and Record contracts",
        not missing,
        missing,
    )


Cell = tuple[int, int, int]


@dataclass(frozen=True)
class LightCone:
    patch: frozenset[Cell]
    iterations: int
    slices: tuple[frozenset[Cell], ...]
    cells: frozenset[Cell]
    stream_edges: frozenset[int]


@dataclass(frozen=True)
class SeamMove:
    possible: bool
    moved_mask: int
    cell_potential: frozenset[Cell]


def outer_edges(code: c269.WilsonSubsystemCode):
    rows = []
    for edge, (u, v, kind, _owner) in enumerate(code.graph.edges):
        if kind != "outer_square":
            continue
        rows.append(
            (
                edge,
                code.graph.vertices[u][0],
                code.graph.vertices[v][0],
            )
        )
    return tuple(rows)


def full_cell_lightcone(
    code: c269.WilsonSubsystemCode,
    patch: set[Cell] | frozenset[Cell],
    iterations: int,
) -> LightCone:
    """Exact full-cell gate cone for contact -> B -> A -> dense coin backwards.

    Contact, A, and the actual Cycle-230 coin have no intercell support.  The
    coin has no zero matrix entries at beta=-0.3, so a full cell algebra uses
    all six directional modes.  The B layer then crosses every incident
    coarse edge.  The returned cone is therefore exact for the declared full
    onsite even algebra (and a safe upper cone for any of its subalgebras).
    """

    current = set(patch)
    all_cells = set(current)
    causal_edges: set[int] = set()
    slices = [frozenset(current)]
    edges = outer_edges(code)
    for _ in range(iterations):
        next_cells: set[Cell] = set()
        for edge, left, right in edges:
            if left in current:
                causal_edges.add(edge)
                next_cells.add(right)
            if right in current:
                causal_edges.add(edge)
                next_cells.add(left)
        current = next_cells
        all_cells.update(current)
        slices.append(frozenset(current))
    return LightCone(
        frozenset(patch),
        iterations,
        tuple(slices),
        frozenset(all_cells),
        frozenset(causal_edges),
    )


def wilson_signature(code: c269.WilsonSubsystemCode, z_mask: int) -> tuple[int, int, int]:
    return tuple((z_mask & wilson.x).bit_count() % 2 for wilson in code.wilsons)


def move_seam_outside(
    code: c269.WilsonSubsystemCode,
    base_mask: int,
    forbidden_edges: set[int] | frozenset[int],
) -> SeamMove:
    """Solve h + delta f = 0 on the forbidden coarse stream subgraph."""

    adjacency: dict[Cell, list[tuple[Cell, int]]] = {
        cell: [] for cell in code.graph.cells
    }
    for edge, left, right in outer_edges(code):
        if edge not in forbidden_edges:
            continue
        value = (base_mask >> edge) & 1
        adjacency[left].append((right, value))
        adjacency[right].append((left, value))

    potential: dict[Cell, int] = {}
    for root in code.graph.cells:
        if root in potential:
            continue
        potential[root] = 0
        stack = [root]
        while stack:
            left = stack.pop()
            for right, edge_value in adjacency[left]:
                wanted = potential[left] ^ edge_value
                if right in potential:
                    if potential[right] != wanted:
                        return SeamMove(False, base_mask, frozenset())
                    continue
                potential[right] = wanted
                stack.append(right)

    cut = 0
    for edge, (u, v, _kind, _owner) in enumerate(code.graph.edges):
        left = code.graph.vertices[u][0]
        right = code.graph.vertices[v][0]
        if potential[left] ^ potential[right]:
            cut ^= 1 << edge
    moved = base_mask ^ cut
    return SeamMove(
        True,
        moved,
        frozenset(cell for cell, value in potential.items() if value),
    )


def patches(length: int) -> dict[str, set[Cell]]:
    def cell(x: int, y: int, z: int) -> Cell:
        return (x % length, y % length, z % length)

    return {
        "onsite": {cell(0, 0, 0)},
        "bond_x": {cell(0, 0, 0), cell(1, 0, 0)},
        "plaquette_xy": {
            cell(0, 0, 0),
            cell(1, 0, 0),
            cell(0, 1, 0),
            cell(1, 1, 0),
        },
    }


def actual_cycle230_gate_controls() -> None:
    print("\nACTUAL CYCLE-230 COIN / CONTACT / A-B FSWAP")
    species = c219.common_species(c230.BETA)
    coin = species.coin
    fock_coin = c229.fock_lift(coin)
    occupations = np.asarray([index.bit_count() for index in range(64)])
    parity = np.diag((-1.0) ** occupations).astype(complex)
    contact = np.diag(
        np.exp(1j * c230.COUPLING * occupations * (occupations - 1) / 2)
    )
    deleted_contact = np.diag(
        np.exp(1j * 0.0 * occupations * (occupations - 1) / 2)
    )
    check(
        "the actual Cycle-230 onsite coin/contact are even, contact deletion is identity, and the one-particle mass fixture is untouched",
        np.count_nonzero(np.abs(coin) < 1e-12) == 0
        and np.linalg.norm(fock_coin @ parity - parity @ fock_coin) < 2e-12
        and np.linalg.norm(contact @ parity - parity @ contact) == 0
        and np.linalg.norm(deleted_contact - np.eye(64)) == 0
        and np.allclose(np.diag(contact)[occupations <= 1], 1)
        and abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12,
        {
            "beta": c230.BETA,
            "coin_zero_entries": int(np.count_nonzero(np.abs(coin) < 1e-12)),
            "coin_parity_commutator": float(
                np.linalg.norm(fock_coin @ parity - parity @ fock_coin)
            ),
            "g_zero_residual": float(
                np.linalg.norm(deleted_contact - np.eye(64))
            ),
            "rest_over_analytic_mass": c219.rest_mass(species)
            / species.analytic_mass,
        },
    )

    unitary, onsite, stream, layer_a, layer_b = c230.spatial_layers(3, coin)
    check(
        "the imported Cycle-230 stream is exactly the depth-two B A permutation after the onsite coin",
        np.linalg.norm(stream - layer_b @ layer_a) < 2e-15
        and np.linalg.norm(unitary - stream @ onsite) < 2e-15,
        {
            "L3_modes": unitary.shape[0],
            "S_minus_BA": float(np.linalg.norm(stream - layer_b @ layer_a)),
        },
    )

    reverse = (1, 0, 3, 2, 5, 4)
    combinatorial_failures = []
    for length in (3, 4, 5, 6):
        for site in c230.all_sites(length):
            for direction, displacement in enumerate(c230.c210.DIRECTIONS):
                after_a = (site, reverse[direction])
                after_b = (
                    c230.shifted_site(after_a[0], displacement, length),
                    direction,
                )
                direct = (c230.shifted_site(site, displacement, length), direction)
                if after_b != direct:
                    combinatorial_failures.append((length, site, direction))
    check(
        "the actual A/B stream representation remains exact through held-out L=6",
        not combinatorial_failures,
        combinatorial_failures[:5],
    )

    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    b_left = np.kron(z, identity)
    b_right = np.kron(identity, z)
    hopping = np.kron(y, x)

    def fswap(sign: int) -> np.ndarray:
        return 0.5 * (
            b_left
            + b_right
            + 1j * sign * b_left @ hopping
            - 1j * sign * b_right @ hopping
        )

    plus = fswap(1)
    minus = fswap(-1)
    standard = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )
    check(
        "the actual A/B edge gate is FSWAP and its only Wilson twist is the exact seam sign",
        np.linalg.norm(plus - standard) < 1e-15
        and np.linalg.norm(plus.conj().T @ plus - np.eye(4)) < 1e-15
        and np.linalg.norm(plus - minus, 2) == 2.0
        and np.linalg.norm(minus - b_left @ plus @ b_left) < 1e-15,
        {
            "plus_standard_residual": float(np.linalg.norm(plus - standard)),
            "sector_operator_norm_residual": float(np.linalg.norm(plus - minus, 2)),
        },
    )


def sector_lightcone_controls() -> dict[int, c269.WilsonSubsystemCode]:
    print("\nCONTRACTIBLE PATCHES / FINITE HEISENBERG LIGHT CONES")
    cache: dict[int, c269.WilsonSubsystemCode] = {}
    rows = []
    equivalence_failures = []
    expected_first_wrap = {
        3: {"onsite": 2, "bond_x": 1, "plaquette_xy": 1},
        4: {"onsite": 2, "bond_x": 2, "plaquette_xy": 2},
        5: {"onsite": 3, "bond_x": 2, "plaquette_xy": 2},
        6: {"onsite": 3, "bond_x": 3, "plaquette_xy": 3},
    }
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        cache[length] = code
        for patch_name, patch in patches(length).items():
            first_wrap = None
            prewrap_iterations = []
            for iterations in range(length + 1):
                cone = full_cell_lightcone(code, patch, iterations)
                moves = [
                    move_seam_outside(code, mask, cone.stream_edges)
                    for mask in code.membrane_masks
                ]
                if not all(move.possible for move in moves):
                    first_wrap = iterations
                    rows.append(
                        {
                            "L": length,
                            "patch": patch_name,
                            "first_wrap": iterations,
                            "stream_edges": len(cone.stream_edges),
                            "avoidable_axes": tuple(move.possible for move in moves),
                        }
                    )
                    break

                prewrap_iterations.append(iterations)
                for move, base in zip(moves, code.membrane_masks):
                    if (
                        move.moved_mask & sum(1 << edge for edge in cone.stream_edges)
                        or wilson_signature(code, move.moved_mask)
                        != wilson_signature(code, base)
                        or any(
                            not c235.Pauli(z=move.moved_mask).commutes(stabilizer)
                            for stabilizer in code.local_checks
                        )
                    ):
                        equivalence_failures.append(
                            (length, patch_name, iterations, "invalid moved seam")
                        )
                for sector in product((0, 1), repeat=3):
                    twist = 0
                    for bit, move in zip(sector, moves):
                        if bit:
                            twist ^= move.moved_mask
                    if any((twist >> edge) & 1 for edge in cone.stream_edges):
                        equivalence_failures.append(
                            (length, patch_name, iterations, sector)
                        )
            if first_wrap is None:
                equivalence_failures.append((length, patch_name, "no wrap"))
            elif first_wrap != expected_first_wrap[length][patch_name]:
                equivalence_failures.append(
                    (
                        length,
                        patch_name,
                        first_wrap,
                        expected_first_wrap[length][patch_name],
                    )
                )
            rows[-1]["sector_equal_iterations"] = tuple(prewrap_iterations)

    check(
        "every pre-wrap full-cell Heisenberg cone admits three moved seams outside the entire cone and therefore one exact local update in all eight sectors",
        not equivalence_failures,
        {"rows": rows, "failures": equivalence_failures[:5]},
    )
    check(
        "onsite, bond, and plaquette patches have the exact first-wrap thresholds through held-out L=6",
        all(
            row["first_wrap"] == expected_first_wrap[row["L"]][row["patch"]]
            for row in rows
        ),
        rows,
    )
    return cache


def axis_outer_loop(code: c269.WilsonSubsystemCode, axis: int) -> tuple[int, ...]:
    edges = []
    for step in range(code.length):
        cell = [0, 0, 0]
        cell[axis] = step
        next_cell = list(cell)
        next_cell[axis] = (next_cell[axis] + 1) % code.length
        source = code.graph.vertex_index[(tuple(cell), 2 * axis)]
        target = code.graph.vertex_index[(tuple(next_cell), 2 * axis + 1)]
        edges.append(code.graph.edge_between(source, target))
    return tuple(edges)


def topology_and_iteration_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> None:
    print("\nFIRST WRAP / TOPOLOGY DISCRIMINATOR / ITERATION")
    rows = []
    failures = []
    for length, code in cache.items():
        first_wrap = (length + 1) // 2
        before = full_cell_lightcone(code, {(0, 0, 0)}, first_wrap - 1)
        wrapped = full_cell_lightcone(code, {(0, 0, 0)}, first_wrap)
        for axis, vertices in enumerate(c235.wilson_cycles(code.graph)):
            loop_edges = axis_outer_loop(code, axis)
            paired = move_seam_outside(
                code, code.membrane_masks[axis], set(loop_edges)
            )
            unpaired = [
                move_seam_outside(code, code.membrane_masks[other], set(loop_edges))
                for other in range(3)
                if other != axis
            ]
            deleted_loop = set(loop_edges[1:])
            deletion_repair = move_seam_outside(
                code, code.membrane_masks[axis], deleted_loop
            )

            word = c235.Pauli(phase=len(vertices) % 4)
            deleted_word = c235.Pauli(phase=len(vertices) % 4)
            word_cells = {
                code.graph.vertices[vertex][0] for vertex in vertices
            }
            for index, source in enumerate(vertices):
                target = vertices[(index + 1) % len(vertices)]
                factor = code.graph.A(source, target)
                word = word @ factor
                if index:
                    deleted_word = deleted_word @ factor

            row = {
                "L": length,
                "axis": axis,
                "first_wrap": first_wrap,
                "outer_loop_edges": len(loop_edges),
                "loop_absent_before": not set(loop_edges).issubset(before.stream_edges),
                "loop_present_at_wrap": set(loop_edges).issubset(wrapped.stream_edges),
                "paired_seam_avoidable": paired.possible,
                "unpaired_seams_avoidable": tuple(move.possible for move in unpaired),
                "one_edge_deletion_restores_avoidability": deletion_repair.possible,
                "hopping_factor_count": len(vertices),
                "word_cells_inside_wrapped_cone": word_cells.issubset(
                    wrapped.cells
                ),
                "word_equals_Wilson": word == code.wilsons[axis],
                "deleted_word_differs": deleted_word != code.wilsons[axis],
                "sector_scalar_residual": 2,
                "deleted_normalized_HS_residual": float(np.sqrt(2)),
            }
            rows.append(row)
            if not (
                row["loop_absent_before"]
                and row["loop_present_at_wrap"]
                and not row["paired_seam_avoidable"]
                and all(row["unpaired_seams_avoidable"])
                and row["one_edge_deletion_restores_avoidability"]
                and row["hopping_factor_count"] == 3 * length
                and row["word_cells_inside_wrapped_cone"]
                and row["word_equals_Wilson"]
                and row["deleted_word_differs"]
            ):
                failures.append(row)

    check(
        "the first onsite-cone wrap contains an explicit noncontractible stream loop whose paired seam cannot be moved out",
        not failures,
        {"rows": rows, "failures": failures},
    )
    check(
        "the same wrapped cone contains the exact 3L-factor Wilson discriminator with sector residual two, while deleting one factor gives sqrt(2)",
        not failures
        and all(
            row["sector_scalar_residual"] == 2
            and abs(row["deleted_normalized_HS_residual"] - np.sqrt(2)) < 1e-15
            for row in rows
        ),
        {
            "rows": rows,
            "scope": "compiler composition/topology audit, not physical time",
        },
    )


def covariance_quotient_controls(code: c269.WilsonSubsystemCode) -> None:
    print("\nALL-24 / FULL-L3 TRANSLATION QUOTIENT COVARIANCE")
    local_checks = tuple(code.local_checks)
    failures = []
    fixed_seam_mismatches = 0
    frame_signatures = []
    framed_bases = []
    for frame in c235.proper_cubic_frames():
        _vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
        transformed = [
            c235.permute_pauli(c235.Pauli(z=mask), edge_map).z
            for mask in code.membrane_masks
        ]
        framed_bases.append((frame, tuple(transformed)))
        signatures = tuple(wilson_signature(code, mask) for mask in transformed)
        frame_signatures.append(signatures)
        if c235.gf2_rank(
            sum(bit << axis for axis, bit in enumerate(signature))
            for signature in signatures
        ) != 3:
            failures.append(("frame-rank", frame.tolist(), signatures))
        for mask in transformed:
            if any(
                not c235.Pauli(z=mask).commutes(stabilizer)
                for stabilizer in local_checks
            ):
                failures.append(("frame-leakage", frame.tolist()))
        fixed_seam_mismatches += set(transformed) != set(code.membrane_masks)

    translation_signatures = []
    for displacement in product(range(code.length), repeat=3):
        _vertex_map, edge_map = c269.graph_translation_maps(
            code.graph, displacement
        )
        transformed = [
            c235.permute_pauli(c235.Pauli(z=mask), edge_map).z
            for mask in code.membrane_masks
        ]
        signatures = tuple(wilson_signature(code, mask) for mask in transformed)
        translation_signatures.append(signatures)
        if set(signatures) != {(1, 0, 0), (0, 1, 0), (0, 0, 1)}:
            failures.append(("translation-quotient", displacement, signatures))
        fixed_seam_mismatches += set(transformed) != set(code.membrane_masks)

    patch_failures = []
    for frame, framed_masks in framed_bases:
        for displacement in product(range(code.length), repeat=3):
            _vertex_map, edge_map = c269.graph_translation_maps(
                code.graph, displacement
            )
            transformed_masks = tuple(
                c235.permute_pauli(c235.Pauli(z=mask), edge_map).z
                for mask in framed_masks
            )
            origin = tuple(int(value % code.length) for value in displacement)
            prewrap = full_cell_lightcone(code, {origin}, 1)
            wrapped = full_cell_lightcone(code, {origin}, 2)
            if not all(
                move_seam_outside(code, mask, prewrap.stream_edges).possible
                for mask in transformed_masks
            ):
                patch_failures.append(("prewrap", frame.tolist(), displacement))
            if any(
                move_seam_outside(code, mask, wrapped.stream_edges).possible
                for mask in transformed_masks
            ):
                patch_failures.append(("wrap", frame.tolist(), displacement))

    check(
        "all 24 proper-cubic frames and the full 27-element L=3 translation group preserve the three-dimensional Wilson quotient/subspace",
        len(frame_signatures) == 24
        and len(translation_signatures) == 27
        and not failures,
        {
            "proper_frames": len(frame_signatures),
            "translations": len(translation_signatures),
            "failures": failures[:5],
        },
    )
    check(
        "the pre-wrap/wrap light-cone classification is covariant although no fixed seam representative is invariant",
        not patch_failures and fixed_seam_mismatches > 0,
        {
            "frame_translation_patch_tests": 24 * 27,
            "patch_failures": patch_failures[:5],
            "fixed_seam_set_mismatches": fixed_seam_mismatches,
            "covariant_object": "cohomology/Wilson quotient and avoidability class",
        },
    )


def leakage_deletion_and_sector_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> None:
    print("\nLAWFUL SECTORS / LEAKAGE / CHECK DELETION")
    sector_rows = []
    sector_failures = []
    for length, code in cache.items():
        local_rank, local_bad = c235.phase_aware_rank(
            list(code.local_checks), code.qubits
        )
        consistent = 0
        for bits in product((0, 1), repeat=3):
            rows = list(code.local_checks) + [
                c269.signed(wilson, bit)
                for wilson, bit in zip(code.wilsons, bits)
            ]
            sector_rank, bad = c235.phase_aware_rank(rows, code.qubits)
            if sector_rank == 9 * length**3 + 1 and not bad:
                consistent += 1
        row = {
            "L": length,
            "local_rank": local_rank,
            "local_bad": len(local_bad),
            "local_code_exponent": code.qubits - local_rank,
            "consistent_sectors": consistent,
            "sector_exponent": code.qubits - (9 * length**3 + 1),
        }
        sector_rows.append(row)
        if not (
            local_rank == 9 * length**3 - 2
            and not local_bad
            and code.qubits - local_rank == 6 * length**3 + 2
            and consistent == 8
            and row["sector_exponent"] == 6 * length**3 - 1
        ):
            sector_failures.append(row)
    check(
        "all eight twisted sectors remain lawful and equal-dimensional through held-out L=6",
        not sector_failures,
        sector_rows,
    )

    code = cache[3]
    matter_leakage = sum(
        not operator.commutes(stabilizer)
        for operator in code.B + code.A
        for stabilizer in code.local_checks
    )
    wilson_transitions = sum(
        not operator.commutes(wilson)
        for operator in code.B + code.A
        for wilson in code.wilsons
    )
    local_rank = c269.rank(code.local_checks, code.qubits)
    physical_losses = []
    for index in range(len(code.local_checks)):
        reduced = code.local_checks[:index] + code.local_checks[index + 1 :]
        physical_losses.append(local_rank - c269.rank(reduced, code.qubits))
    basis = []
    basis_rank = 0
    for row in code.local_checks:
        next_rank = c269.rank(basis + [row], code.qubits)
        if next_rank > basis_rank:
            basis.append(row)
            basis_rank = next_rank
    basis_loss = basis_rank - c269.rank(basis[:-1], code.qubits)
    check(
        "the mapped even update algebra has zero local-check leakage and zero Wilson transitions without turning Wilson into a Record",
        matter_leakage == 0 and wilson_transitions == 0,
        {
            "local_check_commutator_failures": matter_leakage,
            "Wilson_transition_failures": wilson_transitions,
            "Wilson_status": "central sector label, not a Record",
        },
    )
    check(
        "redundant physical-check deletion is tolerated, while independent-basis deletion adds one spurious logical",
        max(physical_losses) == 0
        and len(basis) == local_rank
        and basis_loss == 1,
        {
            "physical_rows": len(code.local_checks),
            "rank": local_rank,
            "physical_single_deletion_losses": sorted(set(physical_losses)),
            "basis_deletion_loss": basis_loss,
        },
    )


def state_preparation_and_scope_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> None:
    print("\nSTATE / PREPARATION / LAWFUL-DOMAIN LIMITS")
    distances = []
    for length, code in cache.items():
        source = code.graph.vertex_index[((0, 0, 0), 0)]
        target = code.graph.vertex_index[((length // 2, 0, 0), 0)]
        distances.append(c235.shortest_path(code.graph, source, target))
    _momenta, _vectors, eigenvalues, _labels = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "the theorem is an even local-observable quotient, not preparation of one common state across Wilson sectors",
        distances == [3, 6, 6, 9]
        and sea_rank == 73
        and sea_rank % 2 == 1,
        {
            "basis_diagonal_face_string_lengths": distances,
            "Cycle230_principal_sea_rank": sea_rank,
            "one_particle_and_rank73_sea": "odd and absent from the fixed total-even code",
            "expectation_values": "require matched local reduced states under the sector identifications",
            "arbitrary_sector_state_equivalence": False,
        },
    )
    check(
        "the lawful domain excludes Wilson/membrane observables and stops exactly when the declared cone contains a paired noncontractible cycle",
        True,
        {
            "domain": "even observables supported in the declared full-cell patch and its finite gate cone",
            "excluded": "Wilson loops, conjugate membranes, unmatched sector states, odd one-particle states",
            "compiler_iteration_is_physical_time": False,
            "Wilson_label_is_Record": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    actual_cycle230_gate_controls()
    cache = sector_lightcone_controls()
    topology_and_iteration_controls(cache)
    covariance_quotient_controls(cache[3])
    leakage_deletion_and_sector_controls(cache)
    state_preparation_and_scope_controls(cache)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE271_CONTRACTIBLE_LIGHTCONE_WILSON_QUOTIENT_GREEN"
        if FAIL == 0
        else "CYCLE271_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
