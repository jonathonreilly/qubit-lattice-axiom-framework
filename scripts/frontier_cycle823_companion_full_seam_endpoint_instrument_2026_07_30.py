#!/usr/bin/env python3
"""Cycle 823: coherent endpoint instrument on the Cycle-822 companion seam.

The instrument surrounds the complete four-factor seam, not its individual
Pauli-rotation factors.  Its fixed stage labels are circuit structure, never
physical time.  The output pointer is a reversible opportunity certificate;
it is not occurrence, actuality, a Record, a Born weight, or a source law.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import time

import numpy as np

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M720
import frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30 as R822


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    "docs/COMPANION_FULL_SEAM_ENDPOINT_INSTRUMENT_"
    "CYCLE823_BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    NOTE_PATH,
    "scripts/frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30.py",
    "docs/PHYSICAL_M2_TYPED_RADIUS_ONE_COMPILER_TOURNAMENT_"
    "CYCLE822_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/ROUTEC_STAGGERED_RADIUS_ONE_PARITY_EVEN_TRANSPORT_"
    "CYCLE822_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/frontier_cycle822_routec_staggered_radius_one_parity_even_"
    "transport_2026_07_30.py",
    "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_"
    "CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
SHAPES = R822.SHAPES
TOL = 3.0e-11
INSTRUMENT_STAGE_ORDER = (
    "pump",
    "bell_measure",
    "bell_correction",
    "recurrent_coin",
    "recurrent_reverse_FSWAP",
    "endpoint_pre",
    "recurrent_seam",
    "endpoint_post_or_clean",
    "recurrent_contact",
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def pauli_action(row, basis: int) -> tuple[int, complex]:
    return (
        basis ^ row.x,
        (1j ** row.phase) * ((-1) ** ((row.z & basis).bit_count())),
    )


def rotate_sparse(state: dict[int, complex], row) -> dict[int, complex]:
    output: dict[int, complex] = defaultdict(complex)
    coefficient = 1.0 / math.sqrt(2.0)
    for basis, amplitude in state.items():
        output[basis] += coefficient * amplitude
        target, phase = pauli_action(row, basis)
        output[target] += -1j * coefficient * phase * amplitude
    return {
        basis: amplitude
        for basis, amplitude in output.items()
        if abs(amplitude) > 1.0e-13
    }


def apply_full_seam(rows, basis: int) -> dict[int, complex]:
    state = {basis: 1.0 + 0.0j}
    for row in rows:
        state = rotate_sparse(state, row)
    return state


def signature_representatives(rows, left: int, right: int) -> tuple[int, ...]:
    """One basis representative for every reachable phase/endpoint class."""
    forms = tuple(row.z for row in rows) + (1 << left, 1 << right)
    bit_positions = sorted({
        bit
        for form in forms
        for bit in range(form.bit_length())
        if (form >> bit) & 1
    })
    representatives = {0: 0}
    for bit in bit_positions:
        signature = sum(
            ((form >> bit) & 1) << index
            for index, form in enumerate(forms)
        )
        for old_signature, basis in tuple(representatives.items()):
            representatives.setdefault(
                old_signature ^ signature, basis ^ (1 << bit)
            )
    return tuple(representatives[key] for key in sorted(representatives))


def cnot_sparse(
    state: dict[int, complex], control: int, target: int
) -> dict[int, complex]:
    return {
        basis ^ ((((basis >> control) & 1) << target)): amplitude
        for basis, amplitude in state.items()
    }


def toffoli_sparse(
    state: dict[int, complex], first: int, second: int, target: int
) -> dict[int, complex]:
    return {
        basis ^ (
            (((basis >> first) & 1) & ((basis >> second) & 1)) << target
        ): amplitude
        for basis, amplitude in state.items()
    }


def instrument_sparse(
    rows,
    basis: int,
    left: int,
    right: int,
    width: int,
    *,
    delete_or_toffoli: bool = False,
    delete_pointer_cleanup: bool = False,
    old_endpoint_cleanup: bool = False,
) -> dict[int, complex]:
    du, dv, pointer = width, width + 1, width + 2
    state = {basis: 1.0 + 0.0j}
    state = cnot_sparse(state, left, du)
    state = cnot_sparse(state, right, dv)
    for row in rows:
        state = rotate_sparse(state, row)
    state = cnot_sparse(state, left, du)
    state = cnot_sparse(state, right, dv)
    state = cnot_sparse(state, du, pointer)
    state = cnot_sparse(state, dv, pointer)
    if not delete_or_toffoli:
        state = toffoli_sparse(state, du, dv, pointer)
    if old_endpoint_cleanup:
        state = cnot_sparse(state, left, du)
        state = cnot_sparse(state, right, du)
        state = cnot_sparse(state, left, dv)
        state = cnot_sparse(state, right, dv)
    else:
        state = cnot_sparse(state, pointer, du)
        if not delete_pointer_cleanup:
            state = cnot_sparse(state, pointer, dv)
    return state


def dictionary_residual(
    left: dict[int, complex], right: dict[int, complex]
) -> float:
    return math.sqrt(sum(
        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
        for key in set(left) | set(right)
    ))


def expected_instrument_output(
    seam: dict[int, complex], input_basis: int, left: int, right: int, width: int
) -> dict[int, complex]:
    pointer = width + 2
    value = ((input_basis >> left) & 1) ^ ((input_basis >> right) & 1)
    return {
        basis ^ (value << pointer): amplitude for basis, amplitude in seam.items()
    }


def full_seam_algebra_certificate() -> dict[str, object]:
    row_pairs = signature_classes = instrument_cases = 0
    row_cardinality_failures = 0
    endpoint_pair_overlap_failures = 0
    row_mask_failures = swap_failures = monomial_failures = 0
    instrument_failures = 0
    maximum_instrument_residual = 0.0
    deleted_factor_detected = single_endpoint_detected = 0
    old_cleanup_equivalence_failures = 0
    or_deletion_detected = cleanup_deletion_detected = 0
    per_shape = []
    for shape in SHAPES:
        fixture = M720.CompanionFixture.build(shape)
        shape_classes = shape_failures = 0
        row_payload = []
        endpoint_pairs = tuple((edge[4], edge[5]) for edge in fixture.edges)
        shape_endpoint_pair_overlap_failures = sum(
            bool(set(first) & set(second))
            for index, first in enumerate(endpoint_pairs)
            for second in endpoint_pairs[index + 1:]
        )
        endpoint_pair_overlap_failures += shape_endpoint_pair_overlap_failures
        for edge_index, edge in enumerate(fixture.edges):
            left, right = edge[4], edge[5]
            endpoint_mask = (1 << left) | (1 << right)
            physical_rows = fixture.physical_terms(edge_index)
            target_rows = fixture.target_terms(edge_index)
            row_cardinality_failures += (
                len(physical_rows) != 4 or len(target_rows) != 4
            )
            row_pairs += len(physical_rows)
            for factor, (physical, target) in enumerate(
                zip(physical_rows, target_rows)
            ):
                expected = 0 if factor < 2 else endpoint_mask
                physical_matter = physical.x & ((1 << fixture.matter_qubits) - 1)
                row_mask_failures += physical_matter != expected or target.x != expected
                row_payload.append((
                    factor,
                    physical.phase, physical.x, physical.z,
                    target.phase, target.x, target.z,
                ))
            for family, rows in (("physical", physical_rows), ("target", target_rows)):
                representatives = signature_representatives(rows, left, right)
                width = fixture.qubits if family == "physical" else fixture.matter_qubits
                for basis in representatives:
                    signature_classes += 1
                    shape_classes += 1
                    seam = apply_full_seam(rows, basis)
                    monomial_failures += len(seam) != 1
                    input_left = (basis >> left) & 1
                    input_right = (basis >> right) & 1
                    swapped = all(
                        ((output >> left) & 1) == input_right
                        and ((output >> right) & 1) == input_left
                        for output in seam
                    )
                    swap_failures += not swapped
                    shape_failures += not swapped
                    executed = instrument_sparse(rows, basis, left, right, width)
                    expected = expected_instrument_output(
                        seam, basis, left, right, width
                    )
                    residual = dictionary_residual(executed, expected)
                    maximum_instrument_residual = max(
                        maximum_instrument_residual, residual
                    )
                    instrument_failures += residual > TOL
                    instrument_cases += 1

                deleted_bad = single_bad = or_bad = cleanup_bad = False
                old_bad = False
                mutated = list(rows)
                mutated[2] = type(rows[2])(
                    rows[2].phase, rows[2].x ^ (1 << left), rows[2].z
                )
                for witness in representatives:
                    seam_witness = apply_full_seam(rows, witness)
                    ideal = expected_instrument_output(
                        seam_witness, witness, left, right, width
                    )
                    deleted = apply_full_seam(rows[:-1], witness)
                    deleted_good = len(deleted) == 1 and all(
                        ((output >> left) & 1) == ((witness >> right) & 1)
                        and ((output >> right) & 1) == ((witness >> left) & 1)
                        for output in deleted
                    )
                    deleted_bad |= not deleted_good
                    single_bad |= dictionary_residual(
                        instrument_sparse(
                            tuple(mutated), witness, left, right, width
                        ),
                        expected_instrument_output(
                            apply_full_seam(tuple(mutated), witness),
                            witness, left, right, width,
                        ),
                    ) > 1.0e-6
                    old_bad |= dictionary_residual(
                        instrument_sparse(
                            rows, witness, left, right, width,
                            old_endpoint_cleanup=True,
                        ),
                        ideal,
                    ) > 1.0e-6
                    or_bad |= dictionary_residual(
                        instrument_sparse(
                            rows, witness, left, right, width,
                            delete_or_toffoli=True,
                        ),
                        ideal,
                    ) > 1.0e-6
                    cleanup_bad |= dictionary_residual(
                        instrument_sparse(
                            rows, witness, left, right, width,
                            delete_pointer_cleanup=True,
                        ),
                        ideal,
                    ) > 1.0e-6
                deleted_factor_detected += deleted_bad
                single_endpoint_detected += single_bad
                old_cleanup_equivalence_failures += old_bad
                or_deletion_detected += or_bad
                cleanup_deletion_detected += cleanup_bad
        per_shape.append({
            "shape": shape,
            "cells": len(fixture.cells),
            "edges": len(fixture.edges),
            "physical_and_target_signature_classes": shape_classes,
            "full_seam_endpoint_swap_failures": shape_failures,
            "endpoint_pair_overlap_failures": shape_endpoint_pair_overlap_failures,
            "row_tuple_sha256": sha256(repr(tuple(row_payload)).encode()).hexdigest(),
        })
    mutation_trials = 2 * sum(row["edges"] for row in per_shape)
    return {
        "held_shapes": len(SHAPES),
        "matched_physical_target_row_pairs": row_pairs,
        "four_plus_four_row_cardinality_failures": row_cardinality_failures,
        "endpoint_pair_overlap_failures": endpoint_pair_overlap_failures,
        "physical_and_target_signature_classes": signature_classes,
        "monomial_full_seam_failures": monomial_failures,
        "full_seam_endpoint_swap_failures": swap_failures,
        "row_endpoint_mask_failures": row_mask_failures,
        "instrument_clean_domain_cases": instrument_cases,
        "instrument_isometry_failures": instrument_failures,
        "maximum_instrument_isometry_residual": maximum_instrument_residual,
        "factor_deletion_trials_detected": deleted_factor_detected,
        "single_endpoint_mutation_trials_detected": single_endpoint_detected,
        "old_Cycle713_swap_specific_cleanup_equivalence_failures": (
            old_cleanup_equivalence_failures
        ),
        "OR_Toffoli_deletion_trials_detected": or_deletion_detected,
        "pointer_cleanup_deletion_trials_detected": cleanup_deletion_detected,
        "expected_mutation_trials_per_control": mutation_trials,
        "dirty_ancilla_unlawful_inputs_per_edge": 7,
        "per_shape": tuple(per_shape),
    }


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def auxiliary_offset(axis: int, register: int):
    return (
        (6, -6, -6 + register),
        (-6, 6, -6 + register),
        (-6 + register, -6, 6),
    )[axis]


def port_offset(axis: int, register: int):
    return (
        (5, -6, -6 + register),
        (-6, 5, -6 + register),
        (-6 + register, -6, 5),
    )[axis]


def augment_context(context):
    persistent = set(context["persistent"])
    ports = set(context["neutral_access_ports"])
    auxiliaries = {}
    collision_failures = 0
    for edge_index, edge in enumerate(context["fixture"].edges):
        center = context["centers"][edge[2]]
        sites = tuple(
            add(center, auxiliary_offset(edge[3], register))
            for register in range(3)
        )
        access = tuple(
            add(center, port_offset(edge[3], register))
            for register in range(3)
        )
        collision_failures += len(set(sites)) != 3
        collision_failures += bool(set(sites) & (persistent | ports))
        collision_failures += bool(set(access) & (persistent | ports | set(sites)))
        persistent.update(sites)
        ports.update(access)
        auxiliaries[edge_index] = sites
    output = dict(context)
    output["persistent"] = frozenset(persistent)
    output["neutral_access_ports"] = frozenset(ports)
    output["charged_route_obstacles"] = frozenset(persistent)
    output["neutral_route_obstacles"] = frozenset(persistent)
    output["endpoint_auxiliaries"] = auxiliaries
    output["endpoint_palette_collision_failures"] = collision_failures
    return output


def routed_cnot(
    context,
    routes,
    control,
    target,
    *,
    role: str,
    bias: int,
    charged_control: bool = False,
):
    if charged_control:
        return R822.routed_two_site(
            "endpoint_CNOT",
            target,
            control,
            context["neutral_route_obstacles"],
            routes,
            role=role,
            exchange="SWAP",
            bias=bias,
            target_first=True,
        )
    return R822.routed_two_site(
        "endpoint_CNOT",
        control,
        target,
        context["neutral_route_obstacles"],
        routes,
        role=role,
        exchange="SWAP",
        bias=bias,
    )


def onsite(kind, site):
    return R822.Primitive(kind, (site,))


def routed_toffoli(context, routes, first, second, target, bias):
    output = [onsite("endpoint_H", target)]
    output += routed_cnot(
        context, routes, second, target, role="endpoint_Toffoli", bias=bias
    )
    output.append(onsite("endpoint_Tdg", target))
    output += routed_cnot(
        context, routes, first, target, role="endpoint_Toffoli", bias=bias + 1
    )
    output.append(onsite("endpoint_T", target))
    output += routed_cnot(
        context, routes, second, target, role="endpoint_Toffoli", bias=bias + 2
    )
    output.append(onsite("endpoint_Tdg", target))
    output += routed_cnot(
        context, routes, first, target, role="endpoint_Toffoli", bias=bias + 3
    )
    output.extend((onsite("endpoint_T", second), onsite("endpoint_T", target)))
    output.append(onsite("endpoint_H", target))
    output += routed_cnot(
        context, routes, first, second, role="endpoint_Toffoli", bias=bias + 4
    )
    output.extend((onsite("endpoint_T", first), onsite("endpoint_Tdg", second)))
    output += routed_cnot(
        context, routes, first, second, role="endpoint_Toffoli", bias=bias + 5
    )
    return output


def instrument_words(context, routes):
    before = []
    after = []
    for edge_index, edge in enumerate(context["fixture"].edges):
        left = context["o_sites"][edge[4]]
        right = context["o_sites"][edge[5]]
        du, dv, pointer = context["endpoint_auxiliaries"][edge_index]
        bias = 1000 + 31 * edge_index
        pre = []
        pre += routed_cnot(
            context, routes, left, du,
            role="endpoint_prewrite", bias=bias, charged_control=True,
        )
        pre += routed_cnot(
            context, routes, right, dv,
            role="endpoint_prewrite", bias=bias + 1, charged_control=True,
        )
        post = []
        post += routed_cnot(
            context, routes, left, du,
            role="endpoint_postwrite", bias=bias + 2, charged_control=True,
        )
        post += routed_cnot(
            context, routes, right, dv,
            role="endpoint_postwrite", bias=bias + 3, charged_control=True,
        )
        post += routed_cnot(
            context, routes, du, pointer,
            role="endpoint_OR", bias=bias + 4,
        )
        post += routed_cnot(
            context, routes, dv, pointer,
            role="endpoint_OR", bias=bias + 5,
        )
        post += routed_toffoli(
            context, routes, du, dv, pointer, bias + 6
        )
        post += routed_cnot(
            context, routes, pointer, du,
            role="endpoint_pointer_cleanup", bias=bias + 12,
        )
        post += routed_cnot(
            context, routes, pointer, dv,
            role="endpoint_pointer_cleanup", bias=bias + 13,
        )
        colour = tuple(value % R822.S789.COLOR_MODULUS for value in edge[2])
        before.append(R822.ScheduledWord(
            "endpoint_pre", colour, edge[3], edge[2],
            f"endpoint_pre:{edge_index}", tuple(pre),
        ))
        after.append(R822.ScheduledWord(
            "endpoint_post_or_clean", colour, edge[3], edge[2],
            f"endpoint_post:{edge_index}", tuple(post),
        ))
    return tuple(before), tuple(after)


T_GATE = np.diag((1.0, np.exp(0.25j * np.pi))).astype(complex)


def primitive_matrix(kind: str) -> np.ndarray:
    if kind == "endpoint_CNOT":
        return R822.B.dense_controlled_target(
            R822.B.pauli_letter(1, "X"), 0, 2
        )
    if kind == "endpoint_H":
        return R822.U720.c707.c655.H
    if kind == "endpoint_T":
        return T_GATE
    if kind == "endpoint_Tdg":
        return T_GATE.conj().T
    return R822.primitive_matrix(kind)


def combined_parity_certificate(words, charged, neutral):
    failures = prefix_failures = untyped = tested = 0
    maximum_residual = 0.0
    for word in words:
        prefix_ok = True
        for primitive in word.primitives:
            untyped += sum(
                site not in charged and site not in neutral
                for site in primitive.sites
            )
            local_z = sum(
                (site in charged) << index
                for index, site in enumerate(primitive.sites)
            )
            parity = R822.B.dense_pauli(
                R822.Pauli(z=local_z), len(primitive.sites)
            )
            matrix = primitive_matrix(primitive.kind)
            residual = float(np.linalg.norm(matrix @ parity - parity @ matrix))
            maximum_residual = max(maximum_residual, residual)
            failed = residual > TOL
            failures += failed
            prefix_ok &= not failed
            prefix_failures += not prefix_ok
            tested += 1
    return {
        "single_global_P_ext": bool(charged) and not (charged & neutral),
        "elementary_primitives_tested": tested,
        "elementary_global_P_ext_commutator_failures": failures,
        "prefix_commutant_certificate_failures": prefix_failures,
        "primitive_untyped_coordinate_uses": untyped,
        "maximum_elementary_global_P_ext_commutator_residual": maximum_residual,
        "P_ext_coordinate_sha256": sha256(repr(tuple(sorted(charged))).encode()).hexdigest(),
    }


def toffoli_decomposition_certificate():
    H = R822.U720.c707.c655.H
    CNOT = primitive_matrix("endpoint_CNOT")
    gates = (
        (H, (2,)), (CNOT, (1, 2)), (T_GATE.conj().T, (2,)),
        (CNOT, (0, 2)), (T_GATE, (2,)), (CNOT, (1, 2)),
        (T_GATE.conj().T, (2,)), (CNOT, (0, 2)), (T_GATE, (1,)),
        (T_GATE, (2,)), (H, (2,)), (CNOT, (0, 1)),
        (T_GATE, (0,)), (T_GATE.conj().T, (1,)), (CNOT, (0, 1)),
    )
    columns = []
    for basis_index in range(8):
        state = np.zeros(8, complex)
        state[basis_index] = 1.0
        for matrix, wires in gates:
            state = R822.U720.c707.apply_gate(state, matrix, wires, 3)
        columns.append(state)
    executed = np.column_stack(columns)
    exact = np.zeros((8, 8), complex)
    for source in range(8):
        target = source ^ (
            ((((source >> 0) & 1) & ((source >> 1) & 1))) << 2
        )
        exact[target, source] = 1.0
    return {
        "elementary_one_and_two_M2_factors": len(gates),
        "maximum_matrix_residual": float(np.linalg.norm(executed - exact)),
    }


def combined_word_order(base_words, before, after):
    prefix = tuple(
        word for word in base_words
        if word.stage not in ("recurrent_seam", "recurrent_contact")
    )
    seam = tuple(word for word in base_words if word.stage == "recurrent_seam")
    contact = tuple(word for word in base_words if word.stage == "recurrent_contact")
    return prefix + before + seam + after + contact


def shape_certificate(shape, atlas, *, covariance=False):
    context = augment_context(R822.local_site_maps(shape, atlas))
    context, base_routes, base_words, atoms, seams, nonseam, repair = (
        R822.fixed_typed_compile(context)
    )
    routes = list(base_routes)
    before, after = instrument_words(context, routes)
    words = combined_word_order(base_words, before, after)
    type_assignment, charged, neutral = R822.fixed_type_assignment(
        context, tuple(routes)
    )
    graph = R822.collision_graph(words)
    route = R822.route_certificate(tuple(routes))
    route["internal_persistent_palette_hits"] = sum(
        len(set(record.path[1:-1]) & set(context["persistent"]))
        for record in routes
    )
    parity = combined_parity_certificate(words, charged, neutral)
    primitive_count = sum(len(word.primitives) for word in words)
    instrument_primitive_count = sum(
        len(word.primitives) for word in before + after
    )
    return {
        "shape": shape,
        "cells": len(context["fixture"].cells),
        "edges": len(context["fixture"].edges),
        "stage_order": INSTRUMENT_STAGE_ORDER,
        "stage_labels_are_physical_time": False,
        "endpoint_palette_collision_failures": context[
            "endpoint_palette_collision_failures"
        ],
        "persistent_endpoint_auxiliary_M2": 3 * len(context["fixture"].edges),
        "persistent_endpoint_auxiliary_M2_per_edge": 3,
        "base_route_macros": len(base_routes),
        "instrument_route_macros": len(routes) - len(base_routes),
        "expected_instrument_route_macros_per_edge": 14,
        "base_primitives": sum(len(word.primitives) for word in base_words),
        "instrument_primitives": instrument_primitive_count,
        "combined_primitives": primitive_count,
        "collision_graph": graph,
        "fixed_type_assignment": type_assignment,
        "routes": route,
        "global_P_ext": parity,
        "base_recurrent_seam": seams,
        "base_recurrent_nonseam": nonseam,
        "base_bell_atoms": atoms,
        "pre_repair_type_audit": repair,
        "covariance": (
            R822.covariance_certificate(words, charged, neutral)
            if covariance else None
        ),
    }


def main() -> None:
    started = time.time()
    algebra = full_seam_algebra_certificate()
    toffoli = toffoli_decomposition_certificate()
    atlas = R822.B.P.build_private_atlases()
    boxes = tuple(
        shape_certificate(shape, atlas, covariance=True)
        for shape in SHAPES
    )
    mass = R822.one_particle_mass_fixture()
    total_edges = sum(box["edges"] for box in boxes)
    checks = {
        "declared_inputs_are_unique_existing_repo_relative_files": (
            len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
            and NOTE_PATH in AUDIT_INPUT_PATHS
            and "scripts/frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30.py"
            in AUDIT_INPUT_PATHS
            and all(
                not Path(path).is_absolute() and (ROOT / path).is_file()
                for path in AUDIT_INPUT_PATHS
            )
        ),
        "complete_physical_and_target_seams_swap_declared_endpoints": (
            algebra["matched_physical_target_row_pairs"] == 328
            and algebra["four_plus_four_row_cardinality_failures"] == 0
            and algebra["physical_and_target_signature_classes"] == 1312
            and algebra["row_endpoint_mask_failures"] == 0
            and algebra["monomial_full_seam_failures"] == 0
            and algebra["full_seam_endpoint_swap_failures"] == 0
        ),
        "edge_endpoint_pairs_are_pairwise_disjoint_in_every_held_box": (
            algebra["endpoint_pair_overlap_failures"] == 0
        ),
        "coherent_endpoint_instrument_is_exact_on_clean_domain": (
            algebra["instrument_clean_domain_cases"] == 1312
            and algebra["instrument_isometry_failures"] == 0
            and algebra["maximum_instrument_isometry_residual"] < TOL
            and toffoli["maximum_matrix_residual"] < TOL
        ),
        "hostile_algebra_mutations_are_active": all(
            algebra[key] == 2 * total_edges for key in (
                "factor_deletion_trials_detected",
                "single_endpoint_mutation_trials_detected",
                "OR_Toffoli_deletion_trials_detected",
                "pointer_cleanup_deletion_trials_detected",
            )
        ) and algebra[
            "old_Cycle713_swap_specific_cleanup_equivalence_failures"
        ] == 0,
        "three_neutral_M2_per_edge_are_collision_free_and_locally_typed": all(
            box["endpoint_palette_collision_failures"] == 0
            and box["persistent_endpoint_auxiliary_M2"] == 3 * box["edges"]
            and box["fixed_type_assignment"]["charged_neutral_coordinate_overlap"] == 0
            and box["fixed_type_assignment"]["FSWAP_endpoint_type_failures"] == 0
            and box["fixed_type_assignment"]["neutral_route_source_type_failures"] == 0
            and box["fixed_type_assignment"]["charged_route_fixed_type_failures"] == 0
            and box["fixed_type_assignment"]["neutral_route_fixed_type_failures"] == 0
            and box["fixed_type_assignment"]["persistent_type_partition_failures"] == 0
            for box in boxes
        ),
        "all_instrument_routes_are_returned_nearest_neighbour_and_bounded": all(
            box["instrument_route_macros"]
                == box["expected_instrument_route_macros_per_edge"] * box["edges"]
            and box["routes"]["nearest_neighbour_failures"] == 0
            and box["routes"]["returned_label_failures"] == 0
            and box["routes"]["internal_persistent_palette_hits"] == 0
            and box["routes"]["routes_with_active_return_deletion_control"] > 0
            for box in boxes
        ),
        "fixed_stage_colour_slot_schedule_has_no_collisions": all(
            box["collision_graph"]["edges"] == 0 for box in boxes
        ),
        "one_single_global_parity_operator_survives_every_prefix": all(
            box["global_P_ext"]["single_global_P_ext"]
            and box["global_P_ext"]["elementary_global_P_ext_commutator_failures"] == 0
            and box["global_P_ext"]["prefix_commutant_certificate_failures"] == 0
            and box["global_P_ext"]["primitive_untyped_coordinate_uses"] == 0
            and box["global_P_ext"]["maximum_elementary_global_P_ext_commutator_residual"] < TOL
            for box in boxes
        ),
        "proper_cubic_transport_and_all_products_preserve_the_program": all(
            box["covariance"][key] == 0
            for box in boxes
            for key in (
                "context_nearest_neighbour_failures",
                "context_palette_bijection_failures",
                "context_collision_graph_failures",
                "context_fixed_type_assignment_failures",
                "colour_transport_bijection_failures",
                "product_coordinate_failures",
                "product_colour_failures",
            )
        ),
        "inherited_one_particle_mass_and_contact_regression_is_rerun": (
            mass["one_particle_mass_residual"] < TOL
            and mass["one_particle_coin_eigen_residual"] < TOL
            and mass["contact_vacuum_and_one_particle_residual"] < TOL
            and mass["contact_double_occupation_phase_residual"] < TOL
        ),
    }
    inventory = {
        "derived": (
            "complete four-factor companion seam swaps its declared matter endpoints",
            "three-neutral-M2 coherent XOR/OR pointer with clean returned scratch",
            "14 returned nearest-neighbour route macros per edge",
            "same fixed P_ext, proper-cubic transported program, and held-shape closure",
        ),
        "supplied": (
            "Cycle822 finite offline route atlas and fixed stage/colour/slot program",
            "clean endpoint auxiliaries and neutral route inputs",
            "Cycle720 companion code sector and total-parity superselection label",
            "finite box shape, coframe, bank genesis, and occurrence of the update",
        ),
        "open": (
            "translation-local query-free atlas generation or intrinsic recurrent law",
            "autonomous clean-auxiliary genesis/enforcement and update occurrence",
            "actuality/admissibility, irreversible Record, Born weighting, and realized history",
            "physical causal-time attachment, conserved source/gravity response, and prediction bridge",
            "a composed matter-only mass/contact theorem after retaining or discarding the pointer",
        ),
    }
    report = {
        "cycle": 823,
        "status": (
            "cycle823-companion-full-seam-endpoint-instrument-bounded-positive"
            if all(checks.values())
            else "cycle823-failed"
        ),
        "authority": "none",
        "audit": "unset",
        "claim_scope": (
            "finite held-box coherent endpoint-opportunity instrument on the "
            "landed Cycle822 companion seam; not an autonomous occurrence law"
        ),
        "algebra": algebra,
        "toffoli_decomposition": toffoli,
        "boxes": boxes,
        "one_particle_mass_fixture": mass,
        "checks": checks,
        "inventory": inventory,
        "source_sha256": {
            path: digest(ROOT / path)
            for path in AUDIT_INPUT_PATHS
            if (ROOT / path).is_file()
        },
        "runtime_seconds": time.time() - started,
    }
    print(json.dumps(
        report,
        indent=2,
        sort_keys=True,
        default=lambda value: value.item()
        if isinstance(value, np.generic)
        else str(value),
    ))
    for label, passed in checks.items():
        print(f"CHECK {label}: {'PASS' if passed else 'FAIL'}")
    if not all(checks.values()):
        raise SystemExit(1)
    print("CYCLE823_COMPANION_FULL_SEAM_ENDPOINT_INSTRUMENT_BOUNDED_EXACT_PASS")


if __name__ == "__main__":
    main()
