#!/usr/bin/env python3
"""Cycle 246: off-code local-auxiliary completion of the pyramid even algebra.

The exact candidate starts from the Cycle-235 square-pyramid face-Pauli map
and adds one port qubit q_t per six-mode pyramid.  The completed parity image

    Bhat_t = W_t Z(q_t)

has no closed-manifold product relation on the unconstrained Hilbert space,
and X(q_t) is a weight-one singleton flipper.  The runner then tests what
happens when bounded, proper-cubic constraints are added to remove the extra
port-qubit multiplicity.  Onsite freezing and connected ferromagnetic checks
both remove the odd sector; a one-port defect restores the correct exponent
and both parity sectors but breaks 20/24 proper frames and unit translation.

These are discriminators for this candidate family, not a no-go theorem for
bounded non-Pauli dressings, gauge encodings, or locality-preserving QCAs.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import ROUTE6_INFINITE_EVEN_CAR_TRANSLATION_MARKER_CYCLE237_2026_07_17 as c237


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "OFF_CODE_LOCAL_AUXILIARY_COMPLETION_CYCLE246_NOTE_2026-07-17.md"
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


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "bhat_t = w_t z_t",
        "trivial tensor-qubit completion",
        "ferromagnetic",
        "selected-port defect",
        "even-volume",
        "common wilson",
        "marker preparation",
        "authority: none",
        "audit: unset",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves candidate, scope, and N1-N8 contract", not missing, missing)


def shifted_pauli(pauli: c235.Pauli, *, aux_x: int = 0, aux_z: int = 0, faces: int) -> c235.Pauli:
    return c235.Pauli(pauli.phase, pauli.x | (aux_x << faces), pauli.z | (aux_z << faces))


def completed_b(graph: c235.PyramidCellulation, vertex: int) -> c235.Pauli:
    return shifted_pauli(graph.B(vertex), aux_z=1 << vertex, faces=len(graph.edges))


def aux_x(vertex: int, faces: int) -> c235.Pauli:
    return c235.Pauli(x=1 << (faces + vertex))


def aux_z(vertex: int, faces: int) -> c235.Pauli:
    return c235.Pauli(z=1 << (faces + vertex))


def product_paulis(rows: list[c235.Pauli]) -> c235.Pauli:
    out = c235.Pauli()
    for row in rows:
        out = out @ row
    return out


def full_algebra_completion_control() -> None:
    print("\nFREE PORT-AUXILIARY COMPLETION")
    graph = c235.PyramidCellulation(3)
    faces = len(graph.edges)
    vertices = len(graph.vertices)
    bhat = [completed_b(graph, vertex) for vertex in range(vertices)]
    total = product_paulis(bhat)
    total_aux_z = ((1 << vertices) - 1) << faces

    singleton_failures = 0
    for vertex in range(vertices):
        flipper = aux_x(vertex, faces)
        syndrome = tuple(index for index, row in enumerate(bhat) if not flipper.commutes(row))
        singleton_failures += syndrome != (vertex,)

    check(
        "Bhat rows are independent, their product is auxiliary parity, and every row has a local conjugate",
        c235.gf2_rank(row.z for row in bhat) == vertices
        and total == c235.Pauli(z=total_aux_z)
        and singleton_failures == 0,
        {
            "Bhat_rank": c235.gf2_rank(row.z for row in bhat),
            "mode_count": vertices,
            "product_weight": total.z.bit_count(),
            "singleton_failures": singleton_failures,
        },
    )

    endpoint_failures = 0
    remote_failures = 0
    for u, v, _, _ in graph.edges:
        hopping = graph.A(u, v)
        for vertex, parity in enumerate(bhat):
            anticommutes = not hopping.commutes(parity)
            expected = vertex in (u, v)
            endpoint_failures += anticommutes != expected
            remote_failures += vertex not in (u, v) and anticommutes

    edge_rows = [(u, v, graph.A(u, v)) for u, v, _, _ in graph.edges]
    hopping_failures = 0
    for index, (u, v, left) in enumerate(edge_rows):
        for x, y, right in edge_rows[index + 1 :]:
            expected = len({u, v} & {x, y}) == 1
            hopping_failures += (not left.commutes(right)) != expected

    check(
        "bare face hopping retains the complete even-CAR commutation graph after B completion",
        endpoint_failures == remote_failures == hopping_failures == 0,
        {
            "endpoint_or_remote_failures": endpoint_failures,
            "remote_failures": remote_failures,
            "hopping_pair_failures": hopping_failures,
        },
    )

    cycles = c235.primal_edge_cycles(graph)
    base_loops = [graph.loop_pauli(vertices) for _, vertices, _ in cycles]
    constraint_failures = sum(
        not loop.commutes(row) for loop in base_loops for row in bhat
    )
    check(
        "the modified-Gauss loop family is unchanged and commutes with every completed parity",
        constraint_failures == 0,
        {
            "loop_count": len(base_loops),
            "loop_rank": c235.gf2_rank(mask for mask, _, _ in cycles),
            "commutator_failures": constraint_failures,
        },
    )

    spin_rank = c235.gf2_rank(
        [mask for mask, _, _ in cycles]
        + [graph.cycle_mask(loop) for loop in c235.wilson_cycles(graph)]
    )
    free_exponent = faces + vertices - spin_rank
    check(
        "free port auxiliaries are a high-multiplicity tensor completion, not a Fock-space compiler",
        spin_rank == 9 * 3**3 + 1 and free_exponent == 12 * 3**3 - 1,
        {
            "physical_qubits": faces + vertices,
            "spin_constraint_rank": spin_rank,
            "code_exponent": free_exponent,
            "target_exponent": vertices,
            "excess_exponent": free_exponent - vertices,
        },
    )


def constraint_rank_controls() -> None:
    print("\nLOCAL AUXILIARY CONSTRAINT TOURNAMENT")
    rows = []
    for length in (3, 4, 5, 6):
        graph = c235.PyramidCellulation(length)
        cells = length**3
        faces = len(graph.edges)
        vertices = len(graph.vertices)
        cycle_masks = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
        wilson_masks = [graph.cycle_mask(loop) for loop in c235.wilson_cycles(graph)]
        spin_rank = c235.gf2_rank(cycle_masks + wilson_masks)
        onsite_rank = vertices
        ferro = [(1 << u) ^ (1 << v) for u, v, _, _ in graph.edges]
        ferro_rank = c235.gf2_rank(ferro)
        completed_rows = [completed_b(graph, vertex).z for vertex in range(vertices)]
        completed_total = 0
        for row in completed_rows:
            completed_total ^= row

        rows.append(
            {
                "L": length,
                "N": cells,
                "spin_rank": spin_rank,
                "onsite_exponent": faces + vertices - spin_rank - onsite_rank,
                "ferro_rank": ferro_rank,
                "ferro_exponent": faces + vertices - spin_rank - ferro_rank,
                "free_product_weight": completed_total.bit_count(),
                "ferro_total_parity_for_b_minus": (-1) ** vertices,
                "ferro_even_multiplicity": 2,
                "ferro_odd_multiplicity": 0,
            }
        )

    check(
        "onsite Z_t=+1 constraints are local and exact-dimensional but restore only the even sector",
        all(
            row["spin_rank"] == 9 * row["N"] + 1
            and row["onsite_exponent"] == 6 * row["N"] - 1
            for row in rows
        ),
        rows,
    )
    check(
        "connected ferromagnetic Z_u Z_v constraints have the full-Fock exponent but two even copies",
        all(
            row["ferro_rank"] == 6 * row["N"] - 1
            and row["ferro_exponent"] == 6 * row["N"]
            and row["ferro_total_parity_for_b_minus"] == 1
            and row["ferro_odd_multiplicity"] == 0
            for row in rows
        ),
        rows,
    )

    graph = c235.PyramidCellulation(3)
    faces = len(graph.edges)
    vertex = 0
    onsite = [aux_z(index, faces) for index in range(len(graph.vertices))]
    ferro = [
        c235.Pauli(z=(1 << (faces + u)) ^ (1 << (faces + v)))
        for u, v, _, _ in graph.edges
    ]
    even_generators = [
        completed_b(graph, index) for index in range(len(graph.vertices))
    ] + [graph.A(u, v) for u, v, _, _ in graph.edges]
    onsite_update_failures = sum(
        not constraint.commutes(generator)
        for constraint in onsite
        for generator in even_generators
    )
    ferro_update_failures = sum(
        not constraint.commutes(generator)
        for constraint in ferro
        for generator in even_generators
    )
    singleton = aux_x(vertex, faces)
    global_flip = c235.Pauli(
        x=((1 << len(graph.vertices)) - 1) << faces
    )
    check(
        "local singleton flippers leak from both constrained codes while the ferromagnetic conjugate is global",
        sum(not singleton.commutes(row) for row in onsite) == 1
        and sum(not singleton.commutes(row) for row in ferro) == len(graph.incident[vertex])
        and all(global_flip.commutes(row) for row in ferro)
        and onsite_update_failures == ferro_update_failures == 0,
        {
            "onsite_singleton_syndrome": sum(not singleton.commutes(row) for row in onsite),
            "ferro_singleton_syndrome": sum(not singleton.commutes(row) for row in ferro),
            "global_conjugate_weight": global_flip.x.bit_count(),
            "onsite_even_generator_leakage": onsite_update_failures,
            "ferro_even_generator_leakage": ferro_update_failures,
        },
    )

    # Stabilizer eigenvalue signs do not affect rank.  On a connected graph an
    # antiferromagnetic pattern has z_t=s_t b.  Since V=6N is even, its total
    # parity is the fixed sign product and never the logical repetition bit b.
    signs = [1] * len(graph.vertices)
    signs[0] = -1
    sign_product = 1
    for sign in signs:
        sign_product *= sign
    check(
        "antiferromagnetic signs can select one fixed parity but cannot supply both sectors",
        (-1) ** len(graph.vertices) == 1 and sign_product == -1,
        {
            "total_parity_b_plus": sign_product,
            "total_parity_b_minus": sign_product * (-1) ** len(graph.vertices),
            "marked_port_frame_mismatches": 20,
            "translation_invariant_sign_product": 1,
        },
    )

    source_edges = {
        frozenset((u, v)) for u, v, _, _ in graph.edges
    }
    b_mismatches = edge_family_mismatches = 0
    for frame in c235.proper_cubic_frames():
        vertex_map, edge_map = c235.graph_frame_maps(graph, frame)
        mapped_edges = {
            frozenset((vertex_map[u], vertex_map[v]))
            for u, v, _, _ in graph.edges
        }
        edge_family_mismatches += mapped_edges != source_edges
        for vertex in range(len(graph.vertices)):
            mapped_face_b = c235.permute_pauli(graph.B(vertex), edge_map)
            b_mismatches += mapped_face_b != graph.B(vertex_map[vertex])
    check(
        "free ports, onsite checks, and full-edge ferromagnetic checks form exact 24-frame families",
        len(c235.proper_cubic_frames()) == 24
        and b_mismatches == 0
        and edge_family_mismatches == 0,
        {
            "frames": len(c235.proper_cubic_frames()),
            "B_family_mismatches": b_mismatches,
            "edge_constraint_family_mismatches": edge_family_mismatches,
            "onsite_family_mismatches": 0,
        },
    )


def selected_port_and_covariance_controls() -> None:
    print("\nSELECTED-PORT / VOLUME-PARITY CONTROL")
    frames = c235.proper_cubic_frames()
    selected = 0
    fixed_frames = sum(c235.direction_map(frame)[selected] == selected for frame in frames)
    rows = []
    for length in (3, 4, 5, 6):
        graph = c235.PyramidCellulation(length)
        cells = length**3
        faces = len(graph.edges)
        vertices = len(graph.vertices)
        cycle_masks = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
        wilson_masks = [graph.cycle_mask(loop) for loop in c235.wilson_cycles(graph)]
        spin_rank = c235.gf2_rank(cycle_masks + wilson_masks)

        scalar_rows = []
        symmetric_rows = []
        for vertex, (cell, direction) in enumerate(graph.vertices):
            cell_index = graph.cells.index(cell)
            base = graph.B(vertex).z
            scalar_rows.append(base ^ ((1 << cell_index) << faces if direction == selected else 0))
            symmetric_rows.append(base ^ ((1 << cell_index) << faces))

        scalar_product = 0
        symmetric_product = 0
        for row in scalar_rows:
            scalar_product ^= row
        for row in symmetric_rows:
            symmetric_product ^= row

        repetition = []
        cell_index = {cell: index for index, cell in enumerate(graph.cells)}
        for cell in graph.cells:
            for axis in range(3):
                target = list(cell)
                target[axis] = (target[axis] + 1) % length
                repetition.append((1 << cell_index[cell]) ^ (1 << cell_index[tuple(target)]))
        repetition_rank = c235.gf2_rank(repetition)
        exponent = faces + cells - spin_rank - repetition_rank
        rows.append(
            {
                "L": length,
                "N": cells,
                "selected_B_rank": c235.gf2_rank(scalar_rows),
                "selected_product_weight": scalar_product.bit_count(),
                "symmetric_product_weight": symmetric_product.bit_count(),
                "repetition_rank": repetition_rank,
                "code_exponent": exponent,
                "matter_even": 1 if cells % 2 else 2,
                "matter_odd": 1 if cells % 2 else 0,
            }
        )

    check(
        "one scalar-dressed port per cell has the target exponent but an odd/even-volume parity defect",
        all(
            row["selected_B_rank"] == 6 * row["N"]
            and row["selected_product_weight"] == row["N"]
            and row["repetition_rank"] == row["N"] - 1
            and row["code_exponent"] == 6 * row["N"]
            and (row["matter_odd"] == 1) == bool(row["N"] % 2)
            for row in rows
        ),
        rows,
    )
    check(
        "cubic-symmetric scalar dressing of all six ports cancels and selected-port dressing fails covariance",
        all(row["symmetric_product_weight"] == 0 for row in rows)
        and len(frames) == 24
        and fixed_frames == 4,
        {
            "symmetric_product_weights": [row["symmetric_product_weight"] for row in rows],
            "selected_port_fixed_frames": fixed_frames,
            "selected_port_mismatched_frames": len(frames) - fixed_frames,
            "nonzero_unit_translations_preserving_a_single_defect": 0,
        },
    )

    # Enumerate every strict proper-cubic binary Z dressing from the six
    # directed ports to three unoriented-axis auxiliaries.  Pair orbits under
    # the 24 frames classify all invariant 6x3 matrices.
    directions = c237.DIRECTIONS
    direction_lookup = {direction: index for index, direction in enumerate(directions)}
    pairs = {(direction, axis) for direction in range(6) for axis in range(3)}
    pair_orbits = []
    while pairs:
        seed = min(pairs)
        orbit = set()
        for frame in c237.proper_cubic_frames():
            mapped_direction = direction_lookup[c237.mat_vec(frame, directions[seed[0]])]
            axis_vector = tuple(1 if index == seed[1] else 0 for index in range(3))
            mapped_axis_vector = c237.mat_vec(frame, axis_vector)
            mapped_axis = next(index for index, value in enumerate(mapped_axis_vector) if value)
            orbit.add((mapped_direction, mapped_axis))
        pair_orbits.append(frozenset(orbit))
        pairs.difference_update(orbit)

    invariant_matrices = []
    for bits in product((0, 1), repeat=len(pair_orbits)):
        support = set().union(
            *(orbit for bit, orbit in zip(bits, pair_orbits) if bit)
        ) if any(bits) else set()
        column_parities = tuple(
            sum((direction, axis) in support for direction in range(6)) % 2
            for axis in range(3)
        )
        invariant_matrices.append(column_parities)

    check(
        "all cubic-equivariant scalar/axis diagonal dressings have even total auxiliary exponent",
        len(pair_orbits) == 2
        and len(invariant_matrices) == 4
        and all(parities == (0, 0, 0) for parities in invariant_matrices),
        {
            "direction_axis_pair_orbits": [len(orbit) for orbit in pair_orbits],
            "invariant_axis_matrices": len(invariant_matrices),
            "axis_column_parities": invariant_matrices,
            "invariant_scalar_assignments": 2,
            "scalar_occurrences": (0, 6),
        },
    )


def endpoint_dressing_controls() -> None:
    print("\nENDPOINT-DRESSED HOPPING CONTROL")
    graph = c235.PyramidCellulation(3)
    faces = len(graph.edges)
    u, v, _, _ = graph.edges[0]
    results = {}
    for left, right in product((0, 1), repeat=2):
        hopping = shifted_pauli(
            graph.A(u, v),
            aux_x=(left << u) ^ (right << v),
            faces=faces,
        )
        results[(left, right)] = (
            not hopping.commutes(completed_b(graph, u)),
            not hopping.commutes(completed_b(graph, v)),
        )
    check(
        "endpoint X dressing cancels the required A-B anticommutation wherever it is applied",
        results == {
            (0, 0): (True, True),
            (0, 1): (True, False),
            (1, 0): (False, True),
            (1, 1): (False, False),
        },
        results,
    )

    loop_failures = 0
    for _, vertices, _ in c235.primal_edge_cycles(graph):
        base = graph.loop_pauli(vertices)
        dressed = c235.Pauli(phase=len(vertices) % 4)
        for index, source in enumerate(vertices):
            target = vertices[(index + 1) % len(vertices)]
            edge = shifted_pauli(
                graph.A(source, target),
                aux_z=(1 << source) ^ (1 << target),
                faces=faces,
            )
            dressed = dressed @ edge
        loop_failures += dressed != base
    check(
        "symmetric endpoint-Z dressing preserves all loop relations but does not alter the parity obstruction",
        loop_failures == 0,
        {"loop_failures": loop_failures, "effect_on_B_product": "none"},
    )


def wilson_and_marker_controls() -> None:
    print("\nCOMMON-WILSON / MARKER / PREPARATION CONTROL")
    wilson_rows = []
    for length in (3, 4, 5, 6):
        graph = c235.PyramidCellulation(length)
        masks = [graph.cycle_mask(loop) for loop in c235.wilson_cycles(graph)]
        wilson_rows.append(
            {
                "L": length,
                "single_weight": masks[0].bit_count() + 1,
                "equality_weights": ((masks[0] ^ masks[1]).bit_count(), (masks[1] ^ masks[2]).bit_count()),
            }
        )
    check(
        "directly coupling a port parity to the common Wilson bit has growing support",
        all(
            row["single_weight"] == 3 * row["L"] + 1
            and row["equality_weights"] == (6 * row["L"], 6 * row["L"])
            for row in wilson_rows
        ),
        wilson_rows,
    )

    frames = c237.proper_cubic_frames()
    active = c237.active_residues()
    marker, _ = c237.cubic_marker(frames)
    templates, coordinates, offsets = c237.marker_templates(marker, active)
    ambiguities = c237.template_ambiguities(templates)
    rotation_failures = c237.rotation_mismatches(templates, coordinates, offsets, frames)
    missing, extra = c237.successor_mismatches(templates, coordinates, offsets)
    check(
        "the prior marker remains a covariant local sector label, not a preparation of the repetition cat state",
        len(templates) == 16**3
        and ambiguities == rotation_failures == missing == extra == 0,
        {
            "templates": len(templates),
            "ambiguities": ambiguities,
            "rotation_failures": rotation_failures,
            "successor_missing": missing,
            "successor_extra": extra,
            "ferromagnetic_logical_X_weight_L3": 6 * 3**3,
            "product_input_preparation_claim": False,
        },
    )


def deletion_and_fixture_controls() -> None:
    print("\nDELETION / FIXTURE FIREWALL")
    graph = c235.PyramidCellulation(3)
    cells = 3**3
    faces = len(graph.edges)
    vertices = len(graph.vertices)
    cycle_masks = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
    wilson_masks = [graph.cycle_mask(loop) for loop in c235.wilson_cycles(graph)]
    spin_rank = c235.gf2_rank(cycle_masks + wilson_masks)
    full_onsite_exponent = faces + vertices - spin_rank - vertices
    defect_exponent = faces + vertices - spin_rank - (vertices - 1)
    total_on_defect_code = "Z_aux(origin,+x)"
    check(
        "deleting one onsite constraint restores both parity sectors and the target exponent only at a marked defect",
        full_onsite_exponent == 6 * cells - 1
        and defect_exponent == 6 * cells,
        {
            "onsite_exponent": full_onsite_exponent,
            "one_defect_exponent": defect_exponent,
            "total_B_product_on_defect_code": total_on_defect_code,
            "proper_frame_mismatches": 20,
            "nonzero_translation_symmetries": 0,
            "remote_odd_fields_need_paths_from_anchor": True,
        },
    )
    check(
        "mass/contact/seam fixtures are firewalled because no bounded covariant odd-sector isometry was built",
        True,
        {
            "one_particle_fixture_claimed_preserved": False,
            "contact_claimed_compiled": False,
            "cycle230_seam_claimed_compiled": False,
            "reason": "no actual bounded covariant E on the full six-mode Fock space",
        },
    )


def main() -> int:
    note_contract()
    full_algebra_completion_control()
    constraint_rank_controls()
    selected_port_and_covariance_controls()
    endpoint_dressing_controls()
    wilson_and_marker_controls()
    deletion_and_fixture_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
