#!/usr/bin/env python3
"""Literal physical-M2 realization of the Cycle710 common-coframe compiler."""

from __future__ import annotations

from collections import Counter
from functools import lru_cache

import numpy as np

import frontier_cycle710_port_canonical_order_gauge_core_2026_07_26 as K
import frontier_cycle709_local_seam_physical_core_2026_07_26 as P709


G = K.G
C = K.C
c707 = P709.c707
LOCAL_TABLE_MAX_RESIDUAL = 0.0


def physical_bundle(cells, origin=(0, 0, 0)):
    graph = c707.PatchGraph(tuple(cells))
    site_map, gauges = c707.placement(
        graph, origin=origin, include_edge_gauge=True
    )
    occupied = tuple(sorted(c707.occupied_sites(site_map, gauges)))
    collisions = (
        sum(len(sites) for sites in site_map.values())
        + len(gauges) - len(occupied)
    )
    return graph, site_map, gauges, occupied, collisions


def augmented_carriers(equivalence, graph, site_map, gauges):
    lookup = {
        P709.c707_edge_key(graph, edge): edge
        for edge in range(len(graph.edges))
    }
    output = []
    for edge in range(len(equivalence.patch_graph.edges)):
        graph_edge = lookup[K.edge_key(equivalence.patch_graph, edge)]
        output.append(tuple(site_map[graph_edge]))
    output.extend(
        (site,) for site in P709.rail_sites(equivalence, graph, gauges)
    )
    return tuple(output)


def pullback(site, frame):
    return tuple(int(value) for value in frame.T @ np.asarray(site))


def pullback_carriers(carriers, frame):
    return tuple(
        tuple(pullback(site, frame) for site in sites)
        for sites in carriers
    )


def bare_input_target_to_source(transport):
    """Induced target-to-source permutation before the reference word."""
    inverse_open = {
        target: source
        for source, target in enumerate(transport.open_gauge.edge_map)
    }
    mapping = []
    for target_qubit in range(transport.source_eq.qubits):
        open_target = K.natural_inverse(
            transport.target_eq, K.P(x=1 << target_qubit)
        )
        source_x = 0
        bits = open_target.x
        while bits:
            bit = bits & -bits
            source_x |= 1 << inverse_open[bit.bit_length() - 1]
            bits ^= bit
        source_augmented = C.natural(
            transport.source_eq, K.P(x=source_x)
        )
        if source_augmented.x.bit_count() != 1:
            raise AssertionError("bare input map is not a permutation")
        mapping.append(source_augmented.x.bit_length() - 1)
    return tuple(mapping)


def physical_site_relabel(source_carriers, target_carriers, patch_mapping):
    mapping = {}
    for source_qubit, target_qubit in enumerate(patch_mapping):
        source = source_carriers[source_qubit]
        target = target_carriers[target_qubit]
        if len(source) != len(target):
            raise AssertionError("repetition carrier arity changed")
        for old, new in zip(source, target):
            if old in mapping and mapping[old] != new:
                raise AssertionError("inconsistent physical address relabel")
            mapping[old] = new
    return mapping


def relabel_word(word, mapping):
    return tuple(
        c707.Instruction(
            instruction.kind,
            tuple(mapping[site] for site in instruction.sites),
            instruction.matrix,
        )
        for instruction in word
    )


def mapped_gauge_terms(transport):
    open_data = transport.open_gauge
    natural = transport.target_eq.natural_edge_map
    return {
        "pre_Z": tuple(
            natural[edge]
            for edge in range(len(open_data.target.edges))
            if (open_data.flips >> edge) & 1
        ),
        "pre_CZ": tuple(
            tuple(sorted((natural[left], natural[right])))
            for left, right in open_data.pairs
        ),
        "post_Z": tuple(
            edge
            for edge in range(len(transport.patch_gauge.target.edges))
            if (transport.patch_gauge.flips >> edge) & 1
        ),
        "post_CZ": tuple(
            tuple(sorted(pair)) for pair in transport.patch_gauge.pairs
        ),
    }


def compile_gauge_stage(stage, terms, carriers):
    word = []
    for logical in terms[stage + "_Z"]:
        site = carriers[logical][0]
        word.extend((
            c707.Instruction(stage + "_gauge_Z_S1", (site,), c707.S_GATE),
            c707.Instruction(stage + "_gauge_Z_S2", (site,), c707.S_GATE),
        ))
    for control, target in terms[stage + "_CZ"]:
        left = carriers[control][0]
        right = carriers[target][0]
        word.extend((
            c707.Instruction(stage + "_gauge_CZ_H1", (right,), c707.c655.H),
            c707.Instruction(
                stage + "_gauge_CZ_CNOT", (left, right), c707.c655.CNOT
            ),
            c707.Instruction(stage + "_gauge_CZ_H2", (right,), c707.c655.H),
        ))
    return tuple(word)


def greedy_edge_colours(pairs):
    colours = []
    for pair in pairs:
        forbidden = {
            colour
            for prior, colour in zip(pairs[:len(colours)], colours)
            if set(prior) & set(pair)
        }
        colours.append(next(
            colour for colour in range(len(pairs) + 1)
            if colour not in forbidden
        ))
    return tuple(colours)


def embedded_gate(qubits, matrix, wires):
    output = np.zeros((1 << qubits, 1 << qubits), complex)
    for basis in range(1 << qubits):
        state = np.zeros(1 << qubits, complex)
        state[basis] = 1
        output[:, basis] = c707.apply_gate(
            state, matrix, tuple(wires), qubits
        )
    return output


def local_pauli_matrix(qubits, x, z):
    output = np.zeros((1 << qubits, 1 << qubits), complex)
    row = c707.Pauli(x=x, z=z)
    for basis in range(1 << qubits):
        state = np.zeros(1 << qubits, complex)
        state[basis] = 1
        output[:, basis] = c707.apply_pauli(state, row, qubits)
    return output


@lru_cache(maxsize=None)
def local_conjugation_table(matrix_digest, arity):
    global LOCAL_TABLE_MAX_RESIDUAL
    matrices = {
        c707.c655.matrix_digest(c707.c655.H): c707.c655.H,
        c707.c655.matrix_digest(c707.S_GATE): c707.S_GATE,
        c707.c655.matrix_digest(c707.SDG_GATE): c707.SDG_GATE,
        c707.c655.matrix_digest(c707.c655.CNOT): c707.c655.CNOT,
    }
    matrix = matrices[matrix_digest]
    unitary = embedded_gate(arity, matrix, tuple(range(arity)))
    canonical = {
        (x, z): local_pauli_matrix(arity, x, z)
        for x in range(1 << arity) for z in range(1 << arity)
    }
    table = {}
    for x in range(1 << arity):
        for z in range(1 << arity):
            transformed = unitary @ canonical[x, z] @ unitary.conj().T
            candidates = []
            for target_x in range(1 << arity):
                for target_z in range(1 << arity):
                    for phase in range(4):
                        residual = float(np.linalg.norm(
                            transformed - (1j ** phase) * canonical[target_x, target_z]
                        ))
                        if residual < 1e-10:
                            candidates.append((phase, target_x, target_z))
                            LOCAL_TABLE_MAX_RESIDUAL = max(
                                LOCAL_TABLE_MAX_RESIDUAL, residual
                            )
            if len(candidates) != 1:
                raise AssertionError((matrix_digest, arity, x, z, candidates))
            table[x, z] = candidates[0]
    return table


def compiled_conjugations(word, site_index):
    return tuple(
        (
            tuple(site_index[site] for site in instruction.sites),
            local_conjugation_table(
                c707.c655.matrix_digest(instruction.matrix),
                len(instruction.sites),
            ),
        )
        for instruction in word
    )


def apply_local_conjugation(row, wires, table):
    local_x = local_z = 0
    for local, wire in enumerate(wires):
        local_x |= ((row.x >> wire) & 1) << local
        local_z |= ((row.z >> wire) & 1) << local
    phase, target_x, target_z = table[local_x, local_z]
    x, z = row.x, row.z
    for local, wire in enumerate(wires):
        x = (x & ~(1 << wire)) | (((target_x >> local) & 1) << wire)
        z = (z & ~(1 << wire)) | (((target_z >> local) & 1) << wire)
    return c707.Pauli((row.phase + phase) % 4, x, z)


def conjugate_rows(rows, word, site_index):
    output = list(rows)
    for wires, table in compiled_conjugations(word, site_index):
        output = [apply_local_conjugation(row, wires, table) for row in output]
    return tuple(output)


def lift_pauli(row, carriers, all_sites):
    site_index = {site: index for index, site in enumerate(all_sites)}
    x = z = 0
    for logical, physical in enumerate(carriers):
        if (row.x >> logical) & 1:
            for site in physical:
                x |= 1 << site_index[site]
        if (row.z >> logical) & 1:
            z |= 1 << site_index[physical[0]]
    return c707.Pauli(row.phase, x, z)


def encoded_basis(qubits, carriers, all_sites):
    return tuple(
        [lift_pauli(K.P(x=1 << q), carriers, all_sites) for q in range(qubits)]
        + [lift_pauli(K.P(z=1 << q), carriers, all_sites) for q in range(qubits)]
    )


def repetition_stabilizers(carriers, all_sites):
    site_index = {site: index for index, site in enumerate(all_sites)}
    return tuple(
        c707.Pauli(z=(1 << site_index[sites[0]]) | (1 << site_index[sites[1]]))
        for sites in carriers if len(sites) == 2
    )


def is_positive_repetition_stabilizer(row, carriers, all_sites):
    if row.phase or row.x:
        return False
    site_index = {site: index for index, site in enumerate(all_sites)}
    covered = 0
    for sites in carriers:
        bits = tuple((row.z >> site_index[site]) & 1 for site in sites)
        if len(sites) == 1:
            if bits[0]:
                return False
        elif bits[0] != bits[1]:
            return False
        else:
            for site in sites:
                covered |= 1 << site_index[site]
    return row.z & ~covered == 0


def compact_route_report(report):
    return {key: value for key, value in report.items() if key != "touched_coordinates"}


def frame_row(frame_index, frame, source_eq, base_images, primary,
              source_carriers, primary_sites):
    target_cells = K.transform_eq(source_eq.open_graph.cells, frame)
    target_eq = K.port_equivalence(target_cells)
    transport = K.mixed_compiler_transport(source_eq, target_eq, frame, base_images)
    graph, site_map, gauges, occupied, collisions = physical_bundle(target_cells)
    target_carriers = augmented_carriers(target_eq, graph, site_map, gauges)
    pulled_carriers = pullback_carriers(target_carriers, frame)
    pulled_occupied = {pullback(site, frame) for site in occupied}
    site_relabel = physical_site_relabel(
        source_carriers, pulled_carriers, transport.patch_mapping
    )
    output_inverse = [None] * source_eq.qubits
    for source, target in enumerate(transport.patch_mapping):
        output_inverse[target] = source
    input_output_failures = sum(
        left != right for left, right in zip(
            bare_input_target_to_source(transport), output_inverse
        )
    )
    relabelled_base = relabel_word(primary["word"], site_relabel)
    terms = mapped_gauge_terms(transport)
    pre_word = compile_gauge_stage("pre", terms, pulled_carriers)
    post_word = compile_gauge_stage("post", terms, pulled_carriers)
    full_word = pre_word + relabelled_base + post_word
    endpoints = {site for instruction in full_word for site in instruction.sites}
    site_index = {site: index for index, site in enumerate(primary_sites)}

    input_rows = encoded_basis(target_eq.qubits, pulled_carriers, primary_sites)
    observed = conjugate_rows(input_rows, full_word, site_index)
    expected = tuple(
        lift_pauli(row, pulled_carriers, primary_sites) for row in transport.images
    )
    exact_failures = sum(left != right for left, right in zip(observed, expected))
    code_failures = sum(
        not is_positive_repetition_stabilizer(
            left @ right, pulled_carriers, primary_sites
        )
        for left, right in zip(observed, expected)
    )
    stabilizers = repetition_stabilizers(pulled_carriers, primary_sites)
    leakage_failures = sum(
        left != right
        for left, right in zip(
            conjugate_rows(stabilizers, full_word, site_index), stabilizers
        )
    )
    encoded_z = input_rows[target_eq.qubits:]
    number_failures = sum(
        left != right
        for word in (pre_word, post_word)
        for left, right in zip(
            conjugate_rows(encoded_z, word, site_index), encoded_z
        )
    )
    semantics = K.semantic_failures(transport.images, target_eq)
    semantic_sum = sum(value for family in semantics.values() for value in family.values())
    routed, route_report = c707.route_word(full_word)
    touched = set(route_report["touched_coordinates"])
    pre_colours = greedy_edge_colours(terms["pre_CZ"])
    post_colours = greedy_edge_colours(terms["post_CZ"])
    pre_degree = Counter(q for pair in terms["pre_CZ"] for q in pair)
    post_degree = Counter(q for pair in terms["post_CZ"] for q in pair)
    return {
        "frame_index": frame_index,
        "is_identity": bool(np.array_equal(frame, K.I3)),
        "abstract_qubits": target_eq.qubits,
        "physical_M2": len(occupied),
        "placement_failures": (
            collisions + len(pulled_occupied ^ set(primary_sites))
            + input_output_failures + len(endpoints - set(primary_sites))
        ),
        "pre_Z": len(terms["pre_Z"]),
        "pre_CZ": len(terms["pre_CZ"]),
        "post_Z": len(terms["post_Z"]),
        "post_CZ": len(terms["post_CZ"]),
        "pre_CZ_max_degree": max(pre_degree.values(), default=0),
        "post_CZ_max_degree": max(post_degree.values(), default=0),
        "pre_CZ_greedy_layers": max(pre_colours, default=-1) + 1,
        "post_CZ_greedy_layers": max(post_colours, default=-1) + 1,
        "full_primitive_gates": len(full_word),
        "exact_logical_intertwiner_failures": exact_failures,
        "code_logical_intertwiner_failures": code_failures,
        "repetition_stabilizers": len(stabilizers),
        "leakage_stabilizer_failures": leakage_failures,
        "gauge_number_Z_failures": number_failures,
        "semantic_failure_sum": semantic_sum,
        "route": compact_route_report(route_report),
        "routed_touched_M2": len(touched),
        "routed_blank_work_M2": len(touched - set(primary_sites)),
        "routed_intermediate_primary_data_M2": len(
            (touched & set(primary_sites)) - endpoints
        ),
        "routed_word_sha256": route_report["word_sha256"],
    }, transport


def repetition_isometry_certificate():
    z = np.diag((1.0, -1.0)).astype(complex)
    one = np.asarray(((1, 0), (0, 0), (0, 0), (0, 1)), dtype=complex)
    two = np.kron(one, one)
    physical_z = np.kron(np.kron(z, np.eye(2)), np.eye(4))
    logical_z = np.kron(z, np.eye(2))
    physical_cz = np.diag(tuple(
        -1.0 if ((basis >> 3) & 1) and ((basis >> 1) & 1) else 1.0
        for basis in range(16)
    )).astype(complex)
    logical_cz = np.diag((1.0, 1.0, 1.0, -1.0)).astype(complex)
    stabilizer_a = np.kron(np.kron(z, z), np.eye(4))
    stabilizer_b = np.kron(np.eye(4), np.kron(z, z))
    projector = two @ two.conj().T
    number = np.diag(tuple((basis.bit_count()) for basis in range(16))).astype(complex)
    intertwiners = (
        float(np.linalg.norm(physical_z @ two - two @ logical_z)),
        float(np.linalg.norm(physical_cz @ two - two @ logical_cz)),
    )
    leakages = (
        float(np.linalg.norm((np.eye(16) - projector) @ physical_z @ two)),
        float(np.linalg.norm((np.eye(16) - projector) @ physical_cz @ two)),
    )
    commutators = (
        float(np.linalg.norm(physical_z @ stabilizer_a - stabilizer_a @ physical_z)),
        float(np.linalg.norm(physical_cz @ stabilizer_a - stabilizer_a @ physical_cz)),
        float(np.linalg.norm(physical_cz @ stabilizer_b - stabilizer_b @ physical_cz)),
    )
    return {
        "maximum_intertwiner_residual": max(intertwiners),
        "maximum_leakage_residual": max(leakages),
        "maximum_stabilizer_commutator": max(commutators),
        "number_commutator": float(np.linalg.norm(
            physical_cz @ number - number @ physical_cz
        )),
        "minimum_active_deletion_residual": min(
            float(np.linalg.norm(two - two @ logical_cz)),
            float(np.linalg.norm(physical_cz @ two - two)),
        ),
    }


def matrix_deletion_controls():
    logical_z = np.diag((1, -1)).astype(complex)
    logical_cz = np.diag((1, 1, 1, -1)).astype(complex)
    z_deleted = []
    cz_deleted = []
    for carriers in (1, 2):
        embedding = np.zeros((1 << carriers, 2), complex)
        embedding[0, 0] = 1
        embedding[(1 << carriers) - 1, 1] = 1
        physical_s = embedded_gate(carriers, c707.S_GATE, (0,))
        z_deleted.append(float(np.linalg.norm(
            physical_s @ embedding - embedding @ logical_z
        )))
    for left_carriers in (1, 2):
        for right_carriers in (1, 2):
            total = left_carriers + right_carriers
            embedding = np.zeros((1 << total, 4), complex)
            for basis in range(4):
                left = basis & 1
                right = (basis >> 1) & 1
                bits = [left] * left_carriers + [right] * right_carriers
                physical = sum(bit << index for index, bit in enumerate(bits))
                embedding[physical, basis] = 1
            target = left_carriers
            gates = (
                embedded_gate(total, c707.c655.H, (target,)),
                embedded_gate(total, c707.c655.CNOT, (0, target)),
                embedded_gate(total, c707.c655.H, (target,)),
            )
            for deleted in range(3):
                observed = np.eye(1 << total, dtype=complex)
                for index, gate in enumerate(gates):
                    if index != deleted:
                        observed = gate @ observed
                cz_deleted.append(float(np.linalg.norm(
                    observed @ embedding - embedding @ logical_cz
                )))
    return {
        "minimum_delete_one_Z_S_residual": min(z_deleted),
        "minimum_delete_one_CZ_primitive_residual": min(cz_deleted),
    }


def common_coframe_physical_campaign():
    cells = G.box_cells((3, 2, 2))
    source_eq, base_images = K.legacy_source_compiler(cells)
    primary = P709.primary_word()
    primary_sites = tuple(primary["all_sites"])
    source_carriers = augmented_carriers(
        source_eq, primary["graph"], primary["site_map"], primary["gauges"]
    )
    primary_certificate = P709.primary_certificate()
    rows = []
    transports = []
    for index, frame in enumerate(G.c706.proper_cubic_frames()):
        row, transport = frame_row(
            index, frame, source_eq, base_images, primary,
            source_carriers, primary_sites,
        )
        rows.append(row)
        transports.append(transport)
    identity = next(row for row in rows if row["is_identity"])
    active_open = max(
        (transport.open_gauge for transport in transports),
        key=lambda data: len(data.pairs) + data.flips.bit_count(),
    )
    active_patch = max(
        (transport.patch_gauge for transport in transports),
        key=lambda data: len(data.pairs) + data.flips.bit_count(),
    )
    deletions = {
        "open": K.deletion_certificate(active_open),
        "patch": K.deletion_certificate(active_patch),
        "primitive": matrix_deletion_controls(),
    }
    gauge_delete_values = (
        deletions[family][key]
        for family in ("open", "patch")
        for key in (
            "minimum_CZ_delete_graph_A_failures",
            "minimum_Z_delete_graph_A_failures",
        )
    )
    return {
        "proper_cubic_frames": len(rows),
        "logical_tableau_rows": 2 * source_eq.qubits * len(rows),
        "logical_intertwiner_failures": sum(
            row["exact_logical_intertwiner_failures"]
            + row["code_logical_intertwiner_failures"] for row in rows
        ),
        "address_permutation_failures": sum(row["placement_failures"] for row in rows),
        "leakage_failures": sum(row["leakage_stabilizer_failures"] for row in rows),
        "number_failures": sum(row["gauge_number_Z_failures"] for row in rows),
        "semantic_failures": sum(row["semantic_failure_sum"] for row in rows),
        "identity_landed_word_failures": int(
            any(identity[key] for key in ("pre_Z", "pre_CZ", "post_Z", "post_CZ"))
            or identity["routed_word_sha256"] != primary_certificate["routed_word_sha256"]
        ),
        "identity_routed_word_sha256": identity["routed_word_sha256"],
        "landed_Cycle709_routed_word_sha256": primary_certificate["routed_word_sha256"],
        "non_NN_failures": sum(row["route"]["non_NN_failures"] for row in rows),
        "operand_order_failures": sum(row["route"]["operand_order_failures"] for row in rows),
        "route_return_failures": sum(row["route"]["route_return_failures"] for row in rows),
        "minimum_first_route_SWAP_detected_macros": min(
            row["route"]["delete_first_swap_detected_macros"] for row in rows
        ),
        "minimum_active_gauge_deletion_failures": min(gauge_delete_values),
        "minimum_active_primitive_deletion_residual": min(
            deletions["primitive"].values()
        ),
        "local_Clifford_table_residual": LOCAL_TABLE_MAX_RESIDUAL,
        "resources": {
            "abstract_qubits": source_eq.qubits,
            "primary_M2": len(primary_sites),
            "landed_base_primitive_gates": len(primary["word"]),
            "minimum_full_primitive_gates": min(row["full_primitive_gates"] for row in rows),
            "maximum_full_primitive_gates": max(row["full_primitive_gates"] for row in rows),
            "minimum_routed_gates": min(row["route"]["routed_gate_count"] for row in rows),
            "maximum_routed_gates": max(row["route"]["routed_gate_count"] for row in rows),
            "maximum_route_distance": max(row["route"]["maximum_route_distance"] for row in rows),
            "maximum_touched_M2": max(row["routed_touched_M2"] for row in rows),
            "maximum_blank_work_M2": max(row["routed_blank_work_M2"] for row in rows),
            "maximum_intermediate_primary_data_M2": max(
                row["routed_intermediate_primary_data_M2"] for row in rows
            ),
            "maximum_pre_Z": max(row["pre_Z"] for row in rows),
            "maximum_pre_CZ": max(row["pre_CZ"] for row in rows),
            "maximum_post_Z": max(row["post_Z"] for row in rows),
            "maximum_post_CZ": max(row["post_CZ"] for row in rows),
            "maximum_pre_CZ_degree": max(row["pre_CZ_max_degree"] for row in rows),
            "maximum_post_CZ_degree": max(row["post_CZ_max_degree"] for row in rows),
            "maximum_pre_CZ_greedy_layers": max(row["pre_CZ_greedy_layers"] for row in rows),
            "maximum_post_CZ_greedy_layers": max(row["post_CZ_greedy_layers"] for row in rows),
        },
        "deletions": deletions,
    }
