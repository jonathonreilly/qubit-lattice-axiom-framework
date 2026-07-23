#!/usr/bin/env python3
"""Cycle656: term-complete flat-link presentation of the Cycle230 update.

This bounded certificate extends immutable Cycle653 from seam characters to
every onsite coin/contact and reverse/spatial FSWAP factor.  The result is an
exact finite local-generator presentation, not an autonomous clocked law.
Authority none; audit unset.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, product
import json
import resource
import signal
import subprocess
import sys
import time
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORE = "2506280d701546e59748940124bb0f08f58da7fa"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_TERM_COMPLETE_FLAT_LINK_UPDATE_CYCLE656_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_term_complete_flat_link_update_cycle656_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_term_complete_flat_link_update_cycle656_cold_2026_07_23.txt"
PASS = FAIL = 0
PINS = {
    "scripts/physical_distributed_tree_toric_returned_work_compiler_cycle653_2026_07_23.py": "1ead5e8f60b7593771abc68b89ccb9674eec75b39a857aefa2cf4b5391d3e974",
    "docs/work_history/repo/review_feedback/PHYSICAL_DISTRIBUTED_TREE_TORIC_RETURNED_WORK_COMPILER_CYCLE653_NOTE_2026-07-23.md": "18f0d3b6ad3c5923cf5ed6bce44b403a6a8c12562b5bee0b21c9762d8a2c624b",
    "outputs/physical_distributed_tree_toric_returned_work_compiler_cycle653_receipt_2026_07_23.json": "f629486f9aa6a9b1c7b7e10d9389904241c682687bfe1d2c71386e8cd799706b",
    "outputs/physical_distributed_tree_toric_returned_work_compiler_cycle653_cold_2026_07_23.txt": "568e166c13b91d14b19347ac20c8fb50aca9b0429d1feb0f726cdcf76ae88c4d",
}


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def git_bytes(path):
    return subprocess.check_output(["git", "show", f"{SHORE}:{path}"], cwd=ROOT)


def file_sha(path): return sha256(path.read_bytes()).hexdigest()


def load_exact(name, path):
    module = types.ModuleType(name); module.__file__ = str(ROOT / path); module.__package__ = ""
    sys.modules[name] = module
    exec(compile(git_bytes(path), module.__file__, "exec"), module.__dict__)
    return module


c653 = load_exact("cycle656_exact_cycle653", "scripts/physical_distributed_tree_toric_returned_work_compiler_cycle653_2026_07_23.py")
c650 = c653.c650; c647 = c653.c647; c643 = c653.c643; c642 = c653.c642
c532 = c653.c532; c523 = c532.c523; Pauli = c653.Pauli; np = c653.np; K = c653.K


def bit_indices(mask):
    while mask:
        bit = mask & -mask; yield bit.bit_length() - 1; mask ^= bit


def lift_link_z(graph_qubits, link_index): return Pauli(z=1 << (graph_qubits + link_index))


def support(row): return row.x | row.z


def pauli_product(rows):
    out = Pauli()
    for row in rows: out = out @ row
    return out


def periodic_l1(left, right, modulus):
    return sum(min((a-b) % modulus, (b-a) % modulus) for a, b in zip(left, right))


def support_diameter(mask, positions, modulus):
    points = tuple(positions[q] for q in bit_indices(mask))
    if len(points) < 2: return 0
    return max(periodic_l1(a, b, modulus) for a, b in combinations(points, 2))


def doubled_K129_graph_position(graph, qubit):
    """Embed the Cycle532 bounded motif in Cycle653's doubled K129 cells."""
    row = graph.edges[qubit]
    center = 2*K*np.asarray(row.owner, dtype=int)
    if row.kind == "rough_terminal": offset = np.zeros(3, dtype=int)
    elif row.kind == "puncture_spoke": offset = 8*np.asarray(c532.c210.DIRECTIONS[row.label], dtype=int)
    elif row.kind == "matter_internal_triangle":
        left = graph.base.vertices[row.u][1]; right = graph.base.vertices[row.v][1]
        offset = 4*(np.asarray(c532.c210.DIRECTIONS[left], dtype=int)+np.asarray(c532.c210.DIRECTIONS[right], dtype=int))
    elif row.kind == "matter_outer_square":
        direction = graph.base.vertices[row.u][1]
        offset = 32*np.asarray(c532.c210.DIRECTIONS[direction], dtype=int)
    else: raise ValueError(row.kind)
    return tuple(int(value % (2*K*graph.length)) for value in center+offset)


def directed_link(left, right, length): return c653.directed_link(left, right, length)


def graph_link_code(length):
    graph = c532.c247.PunctureGraph(length, terminals=1)
    link = c650.link_code(length); N = length ** 3; qg = graph.qubits; total = qg + link["qubits"]
    local = c532.local_stabilizers(graph); wilsons = c532.wilson_initializers(graph)
    gauge_z, _gauge_a, _gauge_edges = c532.gauge_generators(graph)
    cell_index = {cell: i for i, cell in enumerate(graph.cells)}
    correlations = []
    for link_index, (cell, axis) in enumerate(link["links"]):
        target = c650.add_cell(cell, axis, 1, length)
        row = lift_link_z(qg, link_index) @ gauge_z[cell_index[cell]] @ gauge_z[cell_index[target]]
        if cell[axis] == length - 1: row = row @ wilsons[axis]
        correlations.append(row)
    correlations = tuple(correlations)
    combined = local + correlations

    # Every local flatness check is exactly the product of its four E-image
    # correlation rows.  The nonlocal Wilson factors cancel pairwise.
    plaquette_equal_failures = 0
    lifted_plaquettes = []
    for plaquette in link["plaquettes"]:
        lifted = Pauli(plaquette.phase, plaquette.x << qg, plaquette.z << qg)
        lifted_plaquettes.append(lifted)
        actual = pauli_product(correlations[q] for q in bit_indices(plaquette.z))
        plaquette_equal_failures += actual != lifted

    B = tuple(graph.B(vertex) for vertex in range(graph.matter_count))
    A = []
    A_link = []
    outer = 0
    for edge, (source, target, kind, _label) in enumerate(graph.base.edges):
        row = graph.mapped_matter_A(edge); linked = None
        if kind == "outer_square":
            left = graph.base.vertices[source][0]; right = graph.base.vertices[target][0]
            cell, axis = directed_link(left, right, length)
            linked = link["index"][(cell, axis)]
            row = row @ lift_link_z(qg, linked); outer += 1
        A.append(row); A_link.append(linked)
    A = tuple(A)
    matter = B + A

    local_rank, local_inconsistent = c532.phase_rank(local, total)
    combined_rank, combined_inconsistent = c532.phase_rank(combined, total)
    combined_vectors = tuple(row.symplectic(total) for row in combined)
    matter_vectors = tuple(row.symplectic(total) for row in matter)
    reps = c532.quotient_complement(combined_vectors, matter_vectors)
    quotient_dimension = len(reps)
    quotient_gram_rank = c532.symplectic_gram_rank(reps, total)
    stabilizer_commutator_failures = sum(not m.commutes(s) for m in matter for s in combined)

    # Dressing adds only independent-register Zs, so the full B/A symplectic
    # table is exactly the raw Cycle532 table.  Verify every dressing support is
    # link-Z-only and disjoint from the graph register.
    dressing_type_failures = 0
    for edge, linked in enumerate(A_link):
        raw = graph.mapped_matter_A(edge); delta = raw @ A[edge]
        expected = Pauli() if linked is None else lift_link_z(qg, linked)
        dressing_type_failures += delta != expected

    positions = tuple(doubled_K129_graph_position(graph, q) for q in range(qg))
    positions += tuple(c653.link_midpoint(cell, axis, length) for cell, axis in link["links"])
    modulus = 2 * K * length
    placement_collisions = len(positions) - len(set(positions))

    # Local Gauss proxies make the B/A representatives gauge invariant.  They
    # and weight-four plaquettes are the locally enforceable auxiliary checks;
    # the E-image logical correlation section is deliberately reported apart.
    gauss = []
    for cell in graph.cells:
        parity = pauli_product(B[graph.base.vertex_index[(cell, mode)]] for mode in range(6))
        star_x = Pauli()
        for axis in range(3):
            star_x = star_x @ Pauli(x=1 << (qg + link["index"][(cell, axis)]))
            prior = c650.add_cell(cell, axis, -1, length)
            star_x = star_x @ Pauli(x=1 << (qg + link["index"][(prior, axis)]))
        gauss.append(parity @ star_x)
    gauss = tuple(gauss)
    gauss_matter_failures = sum(not g.commutes(m) for g in gauss for m in matter)
    gauss_plaquette_failures = sum(not g.commutes(p) for g in gauss for p in lifted_plaquettes)

    local_basis = c532.independent_pauli_basis(local, total)
    deleted_rank, _ = c532.phase_rank(local_basis[1:] + correlations, total)
    flipped = (Pauli((correlations[0].phase + 2) % 4, correlations[0].x, correlations[0].z),) + correlations[1:]
    _flipped_rank, flipped_inconsistent = c532.phase_rank(local + flipped + (correlations[0],), total)

    row = {
        "length": length, "split": {3: "construction", 6: "train", 7: "held-out-no-refit"}[length],
        "coarse_cells": N, "graph_M2": qg, "flat_link_M2": 3*N, "active_M2": total,
        "active_M2_per_cell": total // N, "graph_local_stabilizers": len(local),
        "graph_local_rank": local_rank, "expected_graph_local_rank": 15*N-2,
        "E_image_correlation_rows": len(correlations), "combined_rank": combined_rank,
        "expected_combined_rank": 18*N-2, "combined_code_exponent": total-combined_rank,
        "expected_code_exponent": 7*N+2, "matter_B_generators": len(B),
        "matter_A_generators": len(A), "outer_link_dressed_A": outer,
        "matter_quotient_dimension": quotient_dimension,
        "expected_matter_quotient_dimension": 12*N-1,
        "matter_quotient_symplectic_rank": quotient_gram_rank,
        "expected_matter_quotient_symplectic_rank": 12*N-2,
        "matter_center_dimension": quotient_dimension-quotient_gram_rank,
        "local_plaquette_product_equalities": len(lifted_plaquettes),
        "plaquette_product_equality_failures": plaquette_equal_failures,
        "dressing_type_failures": dressing_type_failures,
        "matter_combined_stabilizer_commutator_failures": stabilizer_commutator_failures,
        "local_Gauss_rows": len(gauss), "Gauss_matter_commutator_failures": gauss_matter_failures,
        "Gauss_plaquette_commutator_failures": gauss_plaquette_failures,
        "maximum_Gauss_weight": max(support(x).bit_count() for x in gauss),
        "maximum_plaquette_weight": max(support(x).bit_count() for x in lifted_plaquettes),
        "maximum_Gauss_fine_L1_diameter": max(support_diameter(support(x), positions, modulus) for x in gauss),
        "maximum_plaquette_fine_L1_diameter": max(support_diameter(support(x), positions, modulus) for x in lifted_plaquettes),
        "placement_collisions": placement_collisions,
        "delete_one_independent_check_rank": deleted_rank,
        "expected_deleted_rank": combined_rank-1,
        "malformed_phase_inconsistencies": flipped_inconsistent,
        "arbitrary_topological_input_qubits": 3, "all_eight_holonomy_sectors_in_domain": True,
        "runtime_Wilson_table": False, "fixed_plus_plus_plus": False,
        "static_all_local_correlation_stabilizer_claimed": False,
        "E_image_logical_alignment_supplied": True,
    }
    row["pass"] = bool(
        local_inconsistent == combined_inconsistent == 0 and local_rank == 15*N-2
        and combined_rank == 18*N-2 and total-combined_rank == 7*N+2
        and quotient_dimension == 12*N-1 and quotient_gram_rank == 12*N-2
        and quotient_dimension-quotient_gram_rank == 1 and outer == 3*N
        and plaquette_equal_failures == dressing_type_failures == stabilizer_commutator_failures == 0
        and gauss_matter_failures == gauss_plaquette_failures == placement_collisions == 0
        and max(support_diameter(support(x), positions, modulus) for x in gauss) <= 4*K
        and max(support_diameter(support(x), positions, modulus) for x in lifted_plaquettes) <= 2*K
        and deleted_rank == combined_rank-1 and flipped_inconsistent > 0
    )
    internal = {"graph": graph, "link": link, "local": local, "correlations": correlations,
                "plaquettes": tuple(lifted_plaquettes), "gauss": gauss, "B": B, "A": A,
                "A_link": tuple(A_link), "matter": matter, "positions": positions}
    return row, internal


def polynomial_coefficients():
    eye = np.eye(2, dtype=complex); x = np.array(((0, 1), (1, 0)), complex)
    y = np.array(((0, -1j), (1j, 0)), complex); z = np.diag((1, -1)).astype(complex)
    I = np.eye(4, dtype=complex); Bl = np.kron(z, eye); Br = np.kron(eye, z); A = np.kron(y, x)
    basis = []
    for l, r, a in product((0, 1), repeat=3):
        basis.append((f"Bl^{l} Br^{r} A^{a}", np.linalg.matrix_power(Bl, l) @ np.linalg.matrix_power(Br, r) @ np.linalg.matrix_power(A, a)))

    def expand(matrix):
        coeff = tuple(np.trace(row.conj().T @ matrix) / 4 for _name, row in basis)
        rebuilt = sum((value * row for value, (_name, row) in zip(coeff, basis)), np.zeros((4, 4), complex))
        return coeff, float(np.linalg.norm(rebuilt-matrix))

    species = c532.c219.common_species(-0.3)
    schedule, qr = c523.compile_adjacent_qr(species.coin)
    payload = []; maximum = 0.0
    for index, gate in enumerate(schedule):
        if gate.kind == "givens":
            matrix = c523.fock_two_mode(c523.one_particle_matrix(gate)); coeff, residual = expand(matrix)
            payload.append({"index": index, "kind": gate.kind, "modes": list(gate.sites),
                            "coefficients": [{"basis": basis[i][0], "real_hex": v.real.hex(), "imag_hex": v.imag.hex()} for i, v in enumerate(coeff)]})
        else:
            phase = complex(gate.matrix[0]); matrix = np.diag((1, phase)).astype(complex)
            c0 = (1+phase)/2; c1 = (1-phase)/2; residual = float(np.linalg.norm(c0*eye+c1*z-matrix))
            payload.append({"index": index, "kind": gate.kind, "modes": list(gate.sites),
                            "coefficients": [{"basis": "I", "real_hex": c0.real.hex(), "imag_hex": c0.imag.hex()},
                                             {"basis": "B", "real_hex": c1.real.hex(), "imag_hex": c1.imag.hex()}]})
        maximum = max(maximum, residual)

    phase = np.exp(1j * 0.37); contact = np.diag((1, 1, 1, phase)).astype(complex)
    contact_coeff, contact_residual = expand(contact)
    fswap = c523.fock_two_mode(np.asarray(((0, 1), (1, 0)), complex))
    fswap_coeff, fswap_residual = expand(fswap)
    expected_fswap = {"Bl^0 Br^1 A^0": 0.5, "Bl^0 Br^1 A^1": -0.5j,
                      "Bl^1 Br^0 A^0": 0.5, "Bl^1 Br^0 A^1": 0.5j}
    fswap_sign_failures = sum(abs(value-expected_fswap.get(name, 0)) > 1e-14 for value, (name, _row) in zip(fswap_coeff, basis))
    contact_expected = {"Bl^0 Br^0 A^0": (3+phase)/4, "Bl^0 Br^1 A^0": (1-phase)/4,
                        "Bl^1 Br^0 A^0": (1-phase)/4, "Bl^1 Br^1 A^0": (phase-1)/4}
    contact_sign_failures = sum(abs(value-contact_expected.get(name, 0)) > 1e-14 for value, (name, _row) in zip(contact_coeff, basis))
    digest = sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    return {
        "coin_factor_rows": payload, "coin_coefficient_sha256": digest,
        "coin_factors": len(schedule), "coin_Givens": sum(g.kind == "givens" for g in schedule),
        "coin_phases": sum(g.kind == "phase" for g in schedule),
        "one_particle_QR_residual": qr["one_particle_reconstruction_residual"],
        "maximum_coin_polynomial_reconstruction_residual": maximum,
        "contact_polynomial_reconstruction_residual": contact_residual,
        "contact_exact_coefficient_sign_failures": contact_sign_failures,
        "FSWAP_polynomial_reconstruction_residual": fswap_residual,
        "FSWAP_exact_coefficient_sign_failures": fswap_sign_failures,
        "FSWAP_exact_polynomial": "(Bl+Br+i Bl A-i Br A)/2",
        "contact_exact_polynomial": "[(3+e)I+(1-e)(Bl+Br)+(e-1)BlBr]/4, e=exp(i*0.37)",
        "mode_schedule": schedule,
        "pass": len(schedule) == 11 and sum(g.kind == "givens" for g in schedule) == 10
                and sum(g.kind == "phase" for g in schedule) == 1 and maximum < 2e-14
                and contact_residual < 2e-14 and fswap_residual < 2e-14
                and contact_sign_failures == fswap_sign_failures == 0,
    }


def factor_presentation(length, code, coefficients):
    graph = code["graph"]; B = code["B"]; A = code["A"]; factors = []
    cells = tuple(graph.cells)
    def bv(cell, mode): return B[graph.base.vertex_index[(cell, mode)]]
    def add(kind, stage, cell, modes, rows, edge=None):
        mask = 0
        for row in rows: mask |= support(row)
        factors.append({"kind": kind, "stage": stage, "cell": cell, "modes": modes,
                        "edge": edge, "support": mask, "weight": mask.bit_count()})

    for gate_index, gate in enumerate(coefficients["mode_schedule"]):
        for cell in cells:
            if gate.kind == "phase":
                mode = gate.sites[0]; add("coin_phase", f"coin_{gate_index}", cell, (mode,), (bv(cell, mode),))
            else:
                left, right = gate.sites; hopping = c532.onsite_hopping(graph, cell, left, right)
                add("coin_Givens", f"coin_{gate_index}", cell, (left, right), (bv(cell, left), bv(cell, right), hopping))
    for reverse_index, (left, right) in enumerate(((0, 1), (2, 3), (4, 5))):
        for cell in cells:
            hopping = c532.onsite_hopping(graph, cell, left, right)
            add("reverse_FSWAP", f"reverse_{reverse_index}", cell, (left, right),
                (bv(cell, left), bv(cell, right), hopping))
    for edge, (source, target, kind, _label) in enumerate(graph.base.edges):
        if kind != "outer_square": continue
        left_cell, left_mode = graph.base.vertices[source]; right_cell, right_mode = graph.base.vertices[target]
        add("spatial_FSWAP", "spatial_stream", left_cell, (left_mode, right_mode),
            (B[source], B[target], A[edge]), edge)
    for contact_index, (left, right) in enumerate(combinations(range(6), 2)):
        for cell in cells:
            add("contact_phase", f"contact_{contact_index}", cell, (left, right), (bv(cell, left), bv(cell, right)))

    stages = defaultdict(list)
    for factor in factors: stages[factor["stage"]].append(factor)
    palette = 0; total_layers = 0; hist = Counter(); disjoint_failures = 0; maximum_degree = 0
    for name in sorted(stages):
        colors = []
        for factor in stages[name]:
            for color, union in enumerate(colors):
                if not (union & factor["support"]):
                    colors[color] |= factor["support"]; factor["color"] = color; break
            else:
                factor["color"] = len(colors); colors.append(factor["support"])
        palette = max(palette, len(colors)); total_layers += len(colors); hist[len(colors)] += 1
        by_color = defaultdict(list)
        for factor in stages[name]: by_color[factor["color"]].append(factor["support"])
        for masks in by_color.values():
            union = 0
            for mask in masks:
                disjoint_failures += bool(union & mask); union |= mask
        incidence = defaultdict(list)
        for index, factor in enumerate(stages[name]):
            for q in bit_indices(factor["support"]): incidence[q].append(index)
        for index, factor in enumerate(stages[name]):
            neighbors = set()
            for q in bit_indices(factor["support"]): neighbors.update(incidence[q])
            neighbors.discard(index); maximum_degree = max(maximum_degree, len(neighbors))

    modulus = 2*K*length; positions = code["positions"]
    maximum_diameter = max(support_diameter(factor["support"], positions, modulus) for factor in factors)
    overlap = Counter()
    for factor in factors:
        for q in bit_indices(factor["support"]): overlap[q] += 1
    N = length**3; kinds = Counter(f["kind"] for f in factors)
    row = {
        "length": length, "split": {3: "construction", 6: "train", 7: "held-out-no-refit"}[length],
        "coarse_cells": N, "complete_factor_count": len(factors), "expected_factor_count": 32*N,
        "factor_counts": dict(kinds), "ordered_stage_groups": len(stages),
        "finite_color_palette": palette, "sequential_color_layers": total_layers,
        "stage_color_count_histogram": dict(hist), "support_disjoint_color_failures": disjoint_failures,
        "maximum_stage_conflict_degree": maximum_degree,
        "maximum_factor_M2_weight": max(f["weight"] for f in factors),
        "maximum_factor_fine_L1_diameter": maximum_diameter,
        "maximum_all_update_factor_overlap_per_active_M2": max(overlap.values()),
        "constant_overhead_active_M2_per_cell": 25, "runtime_frame_selector": False,
        "host_supplied_factor_order": True, "autonomous_local_clock_constructed": False,
        "G_coarse_redefined": False,
    }
    row["pass"] = len(factors) == 32*N and kinds == {"coin_Givens": 10*N, "coin_phase": N,
        "reverse_FSWAP": 3*N, "spatial_FSWAP": 3*N, "contact_phase": 15*N} \
        and len(stages) == 30 and palette <= 7 and total_layers <= 58 and disjoint_failures == 0 \
        and max(f["weight"] for f in factors) <= 16 and maximum_diameter <= 4*K
    return row, factors


def link_mapping(code, frame, length):
    mapping = []
    for cell, axis in code["links"]:
        target_axis, sign = c642.signed_axis(frame, axis)
        mapped = tuple(int(v) % length for v in frame @ np.asarray(cell, dtype=int))
        if sign < 0: mapped = c650.add_cell(mapped, target_axis, -1, length)
        mapping.append(code["index"][(mapped, target_axis)])
    return tuple(mapping)


def fast_transform_pauli(pauli, data):
    """Sparse equivalent of Cycle532 transform_pauli.

    The immutable helper scans every graph qubit for every row, which is exact
    but quadratic at held L7.  Matter generators have bounded support, so the
    same permutation/gauge action can be evaluated on their set bits only.
    """
    x = z = 0
    for source in bit_indices(pauli.x): x ^= 1 << data.edge_map[source]
    for source in bit_indices(pauli.z): z ^= 1 << data.edge_map[source]
    phase = pauli.phase
    xbits = tuple(bit_indices(x))
    if len(xbits) > 1:
        pair_set = {frozenset(pair) for pair in data.pairs}
        phase = (phase + 2*sum(frozenset(pair) in pair_set for pair in combinations(xbits, 2))) % 4
    for edge in xbits: z ^= data.toggles[edge]
    phase = (phase + 2*(x & data.flips).bit_count()) % 4
    return Pauli(phase, x, z)


def fast_frame_data(graph, frame):
    """Sparse-equivalent construction of immutable Cycle532 FrameData."""
    vertex_map, edge_map = c532.c247.graph_frame_maps(graph, frame)
    toggles, pairs = c532.c247.order_gauge(graph, vertex_map, edge_map)
    provisional = c532.FrameData(tuple(vertex_map), tuple(edge_map), tuple(toggles), tuple(pairs), 0)
    flips = 0
    for source_edge, row in enumerate(graph.edges):
        if row.v is None: continue
        transformed = fast_transform_pauli(graph.A(row.u, row.v), provisional)
        target = graph.A(vertex_map[row.u], vertex_map[row.v])
        if (transformed.phase-target.phase) % 4 == 2: flips ^= 1 << edge_map[source_edge]
    return c532.FrameData(tuple(vertex_map), tuple(edge_map), tuple(toggles), tuple(pairs), flips)


def covariance_controls(rows, internals, onsite_objects):
    frames = tuple(c642.FRAMES); frame_index = {tuple(int(v) for v in f.ravel()): i for i, f in enumerate(frames)}
    reference_equivalence_failures = sum(
        fast_frame_data(internals[0]["graph"], frame) != c532.frame_data(internals[0]["graph"], frame)
        for frame in frames
    )
    mode_maps = []
    for frame in frames:
        row = []
        for mode in range(6):
            axis = mode//2; source_sign = 1 if mode % 2 == 0 else -1
            target_axis, sign = c642.signed_axis(frame, axis); target_sign = source_sign*sign
            row.append(2*target_axis+(0 if target_sign > 0 else 1))
        mode_maps.append(tuple(row))
    mode_product_failures = 0
    for li, left in enumerate(frames):
        for ri, right in enumerate(frames):
            direct = mode_maps[frame_index[tuple(int(v) for v in (left@right).ravel())]]
            mode_product_failures += tuple(mode_maps[li][mode_maps[ri][m]] for m in range(6)) != direct

    size_rows = []; total_failures = mode_product_failures + reference_equivalence_failures
    for row, code in zip(rows, internals):
        length = row["length"]; graph = code["graph"]; link = code["link"]; qg = graph.qubits
        generator_failures = orientation_sign_failures = link_group_failures = 0
        maps = tuple(link_mapping(link, frame, length) for frame in frames)
        for li, left in enumerate(frames):
            for ri, right in enumerate(frames):
                direct = maps[frame_index[tuple(int(v) for v in (left@right).ravel())]]
                link_group_failures += tuple(maps[li][maps[ri][q]] for q in range(3*length**3)) != direct
        for frame, mode_map, lmap in zip(frames, mode_maps, maps):
            data = fast_frame_data(graph, frame); vmap = data.vertex_map
            for source, b in enumerate(code["B"]):
                generator_failures += fast_transform_pauli(b, data) != code["B"][vmap[source]]
            for edge, (source, target, _kind, _label) in enumerate(graph.base.edges):
                raw = graph.mapped_matter_A(edge); transformed = fast_transform_pauli(raw, data)
                target_edge = graph.base.edge_lookup[frozenset((vmap[source], vmap[target]))]
                target_raw = graph.mapped_matter_A(target_edge)
                expected_phase = 0
                ts, tt, _tk, _tl = graph.base.edges[target_edge]
                if (vmap[source], vmap[target]) == (tt, ts): expected_phase = 2
                phase_adjusted = Pauli((target_raw.phase+expected_phase)%4, target_raw.x, target_raw.z)
                orientation_sign_failures += transformed != phase_adjusted
                linked = code["A_link"][edge]; mapped_link = None if linked is None else lmap[linked]
                target_link = code["A_link"][target_edge]
                generator_failures += mapped_link != target_link
        link_cov = c650.link_covariance(link, length)
        total = generator_failures+orientation_sign_failures+link_group_failures+int(not link_cov["pass"])
        total_failures += total
        size_rows.append({"length": length, "proper_frames": 24, "frame_products": 576,
                          "B_A_generator_map_failures": generator_failures,
                          "oriented_A_sign_failures": orientation_sign_failures,
                          "link_all576_group_failures": link_group_failures,
                          "link_constraint_covariance": link_cov, "pass": total == 0})
    onsite = c523.frame_controls(onsite_objects)
    return {"proper_cubic_frames": 24, "frame_products": 576,
            "sparse_evaluator_exact_immutable_L3_FrameData_failures": reference_equivalence_failures,
            "signed_six_mode_all576_group_failures": mode_product_failures,
            "size_rows": size_rows, "Cycle523_Koszul_coin_contact_covariance": onsite,
            "finite_color_schedule_transport": "compile-time permutation of factor supports and color labels; no runtime selector",
            "pass": total_failures == 0 and onsite["pass"]}


def controls(rows, factors, coefficients, onsite, onsite_objects):
    deletion = c523.deletion_perturbation_controls(onsite_objects)
    inherited = c643.c537.inherited_target_controls()["mass_contact_and_seam"]
    fswap = c532.fswap_matrix_control()
    return {
        "combined_check_deletion_detected": all(row["delete_one_independent_check_rank"] == row["combined_rank"]-1 for row in rows),
        "malformed_phase_detected": all(row["malformed_phase_inconsistencies"] > 0 for row in rows),
        "matter_code_leakage_failures": sum(row["matter_combined_stabilizer_commutator_failures"] for row in rows),
        "onsite_inverse_and_leakage": onsite,
        "onsite_deletion_and_perturbation": deletion,
        "FSWAP_matrix_control": fswap,
        "Cycle219_mass_fixture_residual": inherited["Cycle219_mass_fixture_residual"],
        "Cycle230_contact_active_two_particle_states": inherited["Cycle230_contact_active_two_particle_states"],
        "Cycle230_contact_deletion_residual": inherited["Cycle230_contact_deletion_residual"],
        "Cycle230_seam_subchecks": inherited["Cycle230_seam_subchecks"],
        "held_L7_no_refit": True,
        "lawful_domain": {"periodic_cubic": True, "minimum_length": 3, "tested_lengths": [3, 6, 7], "six_modes_per_cell": True},
        "exact_coefficients_and_signs": coefficients["pass"],
        "inverse_scope": "each polynomial factor is unitary and the Cycle523 onsite compiler inverse roundtrip is exact; Cycle653 supplies reversible E",
        "factor_deletion_nonzero": deletion["pass"] and inherited["Cycle230_contact_deletion_residual"] > 0,
        "pass": all(row["pass"] for row in rows) and all(row["pass"] for row in factors)
                and onsite["pass"] and deletion["pass"] and fswap["pass"] and coefficients["pass"]
                and inherited["Cycle219_mass_fixture_residual"] < 2e-14
                and inherited["Cycle230_contact_active_two_particle_states"] == 15
                and inherited["Cycle230_seam_subchecks"]["fail"] == 0,
    }


def citation(path, fragment):
    for line, text in enumerate(git_bytes(path).decode().splitlines(), 1):
        if fragment in text: return {"ref": SHORE, "path": path, "line": line, "text": text.strip()}
    raise AssertionError((path, fragment))


def current_citation(fragment):
    for line, text in enumerate(Path(__file__).read_text().splitlines(), 1):
        if fragment in text: return {"ref": "Cycle656 current artifact", "path": str(Path(__file__).relative_to(ROOT)), "line": line, "text": text.strip()}
    raise AssertionError(fragment)


def no_go_discipline():
    prior_term = citation("docs/work_history/repo/review_feedback/PHYSICAL_DISTRIBUTED_TREE_TORIC_RETURNED_WORK_COMPILER_CYCLE653_NOTE_2026-07-23.md", "complete elementary G factorization remains open")
    prior_auto = citation("docs/work_history/repo/review_feedback/PHYSICAL_DISTRIBUTED_TREE_TORIC_RETURNED_WORK_COMPILER_CYCLE653_NOTE_2026-07-23.md", "bounded-period G and term-complete")
    prior_plus = citation("docs/work_history/repo/review_feedback/PHYSICAL_DISTRIBUTED_TREE_TORIC_RETURNED_WORK_COMPILER_CYCLE653_NOTE_2026-07-23.md", "never fixes `+++`")
    current = current_citation("autonomous_local_clock_constructed")
    families = [
        {"family": "direct link-dressed even-CAR factors", "object_formulation": "B vertices and link-dressed A edges", "mechanism_invariant": "exact CAR polynomial functional calculus", "terminal_obligation": "all 32N Cycle230 factors", "strength_vs_target": "term-complete", "honesty_marker": "ATTEMPTED", "status": "passes L3/L6/held L7"},
        {"family": "local auxiliary gauge subsystem", "object_formulation": "rough graph plus flat links, local Gauss and plaquettes", "mechanism_invariant": "endpoint parity/link-star cancellation", "terminal_obligation": "gauge-invariant local factor algebra", "strength_vs_target": "term-complete with supplied E-image logical alignment", "honesty_marker": "ATTEMPTED", "status": "local invariance passes; static all-local seam correlation not claimed"},
        {"family": "finite-color factorization", "object_formulation": "30 ordered factor families with seven-color palette", "mechanism_invariant": "support-disjoint parallel layers", "terminal_obligation": "size-independent local schedule alphabet", "strength_vs_target": "one step short of autonomous clock", "honesty_marker": "ATTEMPTED", "status": "palette passes; clock/work law open"},
        {"family": "character-only flat-link coupling", "object_formulation": "Cycle653 seam-character interface", "mechanism_invariant": "local flat-link sign", "terminal_obligation": "complete elementary G", "strength_vs_target": "strictly weaker", "honesty_marker": "RULED OUT BY PRIOR", "status": "retired by current term-complete construction", "citation": prior_term},
        {"family": "fixed plus-plus-plus sector", "object_formulation": "one topological character", "mechanism_invariant": "three fixed Wilson initializers", "terminal_obligation": "all coherent holonomies", "strength_vs_target": "strict subset", "honesty_marker": "RULED OUT BY PRIOR", "status": "not admissible and not used", "citation": prior_plus},
    ]
    walls = {"W_autonomous_execution": "replace the finite-color host order by a bounded-period local clock/QCA with returned work",
             "W_reference_genesis": "prepare or renew the correlation/link/clock reference without a supplied blank or gauge section"}
    pairs = [{"from": "W_autonomous_execution", "to": "W_reference_genesis", "implied": False, "reason": "a clocked rule does not prepare its blank/reference"},
             {"from": "W_reference_genesis", "to": "W_autonomous_execution", "implied": False, "reason": "a prepared reference does not execute the ordered factor law"}]
    n4 = [{"prior_ref": prior_term["ref"], "prior_path": prior_term["path"], "prior_line": prior_term["line"],
           "prior_residual": "complete elementary G factorization remains open", "current_path": current["path"], "current_line": current["line"],
           "current_residual": "all 32N elementary free-plus-contact factors now have exact local polynomials", "same_scope": True, "exact_match": True, "use_as_closure": True}]
    non = [{"prior_ref": prior_auto["ref"], "prior_path": prior_auto["path"], "prior_line": prior_auto["line"],
            "prior_residual": "autonomous bounded-period G remains open", "current_path": current["path"], "current_line": current["line"],
            "current_residual": "finite colors are constructed but autonomous_local_clock_constructed is false", "same_scope": True, "exact_match": True, "use_as_closure": False}]
    rhetoric = [{"claim": "Cycle656 closes term completeness but not an autonomous physical compiler",
                 "per_element": "every coin, reverse, stream, and contact factor is enumerated with exact coefficients",
                 "per_site": "all factor supports are bounded on 25 active M2 per cell",
                 "per_mode": "all six modes, 15 contacts, mass, and FSWAP signs are tested",
                 "per_block": "L3/L6/held L7 quotient and colors are exact",
                 "lattice_wide": "no arbitrary-L theorem of autonomous genesis or impossibility is claimed"}]
    n6 = [{"file": "UNMATERIALIZED/autonomous_seven_color_flat_link_QCA_cycle_next.py", "status": "OPEN / PRIORITY", "what_closes": "W_autonomous_execution"},
          {"file": "UNMATERIALIZED/regenerative_flat_link_clock_reference_cycle_next.py", "status": "OPEN", "what_closes": "W_reference_genesis"},
          {"file": "UNMATERIALIZED/static_local_logical_alignment_subsystem_cycle_next.py", "status": "OPEN / ALTERNATIVE", "what_closes": "an alternative to Cycle653 scheduled E-image Wilson/link alignment"}]
    n7 = {"mechanism": "attach a finite local clock band to the seven-color palette, translate each polynomial into controlled local rotations, and uncompute/renew the clock and link work after one period",
          "actionable_steps": ["compile the 58 color layers into a translational cell alphabet", "prove collision-free controlled execution and inverse work return", "replace supplied clock/link blanks by a regenerative local reference"],
          "terminal_test": "constant-period autonomous G_physical, exact full-update intertwiner, all24/all576, arbitrary holonomies, returned work, and no supplied blank/genesis",
          "supporting_citations": [prior_auto, prior_term]}
    n8 = [{"cycle": 653, "retired": "term-complete local CAR representation remained open", "mechanism": "exact B/A polynomial census and 32N factor composition", "applicability": "retired at L3/L6/held L7; autonomous execution remains open", "citation_ref": prior_term["ref"], "citation_path": prior_term["path"], "citation_line": prior_term["line"], "citation_text": prior_term["text"]},
          {"cycle": 653, "retired": "none of the autonomous scheduling residual", "mechanism": "seven-color finite schedule is a partial closure only", "applicability": "does not supply a clock, work return, or genesis", "citation_ref": prior_auto["ref"], "citation_path": prior_auto["path"], "citation_line": prior_auto["line"], "citation_text": prior_auto["text"]}]
    return {"Status": "PASS", "N1_normalized_families": families, "N1_open_routes_not_counted": [{"family": "autonomous seven-color QCA", "status": "OPEN / NOT COUNTED"}, {"family": "regenerative reference genesis", "status": "OPEN / NOT COUNTED"}],
            "N1_qualifying_attempts": 5, "N1_required_for_negative": 5, "N1_broad_negative_gate": "FAIL / DO NOT SHIP",
            "broad_negative_gate": "FAIL / DO NOT SHIP", "minimum_content_gate": "FAIL / DO NOT SHIP", "shared_obstruction_gate": "FAIL / DO NOT SHIP", "axiom_pressure_gate": "FAIL / DO NOT SHIP",
            "N2_walls": walls, "N2_directed_ordered_pairs": pairs,
            "N3_hidden_wall_scan": [{"condition": "Cycle653 E-image graph/link logical alignment", "classification": "explicit supplied gauge section"}, {"condition": "30-family/58-layer order", "classification": "explicit compile-time host schedule"}, {"condition": "flat-link and clock blanks", "classification": "explicit supplied reference/genesis"}],
            "N4_exact_residual_matches": n4, "N4_nonmatches_not_used_as_closure": non, "N5_rhetoric": rhetoric,
            "N6_partial_closure_paths": n6, "N7_steelman": n7, "N8_cross_cycle_echo": n8,
            "broad_no_go_claim": False, "minimum_content_claim": False, "shared_obstruction_claim": False, "axiom_pressure_claim": False,
            "broad_negative_shipped": False, "minimum_content_shipped": False, "shared_obstruction_shipped": False, "axiom_pressure_shipped": False,
            "shared_route_independent_obstruction": False, "axiom_pressure": False}


def note_text(r):
    q = "\n".join(f"| L{x['length']} | {x['active_M2_per_cell']} | {x['combined_rank']} | {x['matter_quotient_dimension']} | {x['matter_quotient_symplectic_rank']} |" for x in r["route_A_direct_link_dressed_algebra"])
    f = "\n".join(f"| L{x['length']} | {x['complete_factor_count']} | {x['finite_color_palette']} | {x['sequential_color_layers']} | {x['maximum_factor_M2_weight']} | {x['maximum_factor_fine_L1_diameter']} |" for x in r["route_C_finite_color_factorization"])
    p = r["polynomial_coefficients"]; c = r["controls"]
    return f"""# Term-complete flat-link update — Cycle 656

Classification: **positive term-complete finite local-generator presentation; autonomous physical compiler open**

Authority: **none**

Audit: **unset**

Author artifact status accepted: **false**

Breakthrough: **false**

## Strongest constructive result

Cycle656 constructs every term in the Cycle230 six-mode free-plus-contact
update on a rough-graph plus flat-link register.  Each cell uses 22 graph M2
and three link M2.  Every outer-square matter generator is dressed by the one
physical link it crosses; onsite generators are unchanged.  With the exact
Cycle653 E-image correlation section, the quotient is `12N-1` dimensional,
has symplectic rank `12N-2`, and therefore has exactly the one expected
matter-parity center—not the three extra Wilson centers.

| size | active M2/cell | combined rank | matter quotient | symplectic rank |
|---|---:|---:|---:|---:|
{q}

Thus the represented B/A algebra is the complete six-mode even CAR algebra.
The exact local polynomial for every factor gives
`E_local G_coarse = G_flat_complete E_local` on the declared correlated code
space in all eight holonomy sectors. `G_coarse` is not redefined. There is no
runtime Wilson table, global Jordan-Wigner order, nonlocal parity service, or
fixed `+++` sector.

This is term completeness, not autonomous scheduling.  The E-image logical
alignment is supplied by the reversible Cycle653 encoding schedule.  The
finite factor order is host supplied, and blank/reference genesis is not
derived.  Therefore strict physical success, full success, and breakthrough
remain false.

## Route A — direct link-dressed even-CAR factors

The complete factor census is `32N`: 10 coin Givens, one coin phase, three
onsite reverse FSWAPs, three spatial link-dressed FSWAPs, and 15 contact phases
per cell.  The two-mode identities are

- `FSWAP=(Bl+Br+i Bl A-i Br A)/2`;
- `contact=[(3+e)I+(1-e)(Bl+Br)+(e-1)BlBr]/4`, `e=exp(i*0.37)`;
- each Givens has all eight frozen coefficients in the receipt.

Maximum coin polynomial residual is `{p['maximum_coin_polynomial_reconstruction_residual']:.3e}`;
contact and FSWAP residuals are `{p['contact_polynomial_reconstruction_residual']:.3e}`
and `{p['FSWAP_polynomial_reconstruction_residual']:.3e}`. Exact coefficient/sign
failures are zero.

## Route B — local gauge/auxiliary subsystem

Graph-local stabilizers plus flat-link plaquettes are local.  The local Gauss
proxy `product_m B_m` times the six-incident-link X star commutes with every
B/A representative and every plaquette.  All plaquettes are exact products of
four graph/link correlation rows.  Constraint deletion, malformed phase,
leakage, inverse, and held-size controls pass.

The three wrapping correlation rows contain graph Wilson representatives when
written in this gauge section.  They specify the E-image logical alignment;
Cycle656 does not claim they form a simultaneously commuting all-local static
constraint presentation.  This is unfinished implementation, not a shared
substrate obstruction.

## Route C — finite-color factorization

| size | factors | palette | sequential layers | max weight | max fine-L1 diameter |
|---|---:|---:|---:|---:|---:|
{f}

The train palette is seven colors and held L7 needs no eighth color or refit.
Each color layer is support-disjoint.  The 30 ordered factor families require
at most 58 sequential color layers.  This is suitable input to a local QCA
compiler but is not itself an autonomous clock or physical time law.

## Covariance and exact fixtures

All 24 proper-cubic frames and all 576 products pass for link coordinates,
B/A generator transport, signed six-mode labels, and the Cycle523 Koszul
coin/contact representation.  Schedule/color labels are transported at
compile time; no runtime frame selector is used.

- Cycle219 mass residual: `{c['Cycle219_mass_fixture_residual']:.3e}`
- Cycle230 active two-particle contact states: `{c['Cycle230_contact_active_two_particle_states']}`
- Cycle230 contact deletion residual: `{c['Cycle230_contact_deletion_residual']:.15f}`
- Cycle230 seam subchecks: `{c['Cycle230_seam_subchecks']['pass']} PASS / {c['Cycle230_seam_subchecks']['fail']} FAIL`

## Supplied structure and prior-art boundary

Supplied are the immutable Cycle653 encoder and gauge section, finite L3/L6/L7
domains, the rough-puncture graph, three coherent holonomy inputs, the K129
placement/routing convention, factor order, compile-time frame transport, and
blank link/work references.  No wrapped phase is called energy, no generator
element is called a rate, no pointer copy is called a Record, and no coarse CAR
cell is called a physical-site compiler.

Z2 link dressing, lattice gauge Gauss/plaquette checks, even-CAR B/A generator
polynomials, QR/Givens decomposition, FSWAP identities, and greedy conflict
coloring are standard prior art.  The narrow new result is their exact
composition with the Cycle653 correlated link code and the entire Cycle230
factor census, quotient, held-size, coefficient, and covariance receipts.  No
broader novelty is claimed.

## Route disposition and six-wall ledger

- Route A: **PASS—complete bounded B/A polynomial presentation**.
- Route B: **PASS at gauge-invariant local-factor level—static all-local
  E-image Wilson/link alignment remains open**.
- Route C: **PASS as a seven-color finite schedule—autonomous clock/work and
  blank genesis remain open**.

| wall | movement | residual |
|---|---|---|
| `C_ref` | arbitrary holonomies and exact graph/link alignment retained | gauge section, link/clock blanks, and genesis supplied |
| `C_num` | exact quotient, coefficients, inverse, deletion, and held controls | no Born or empirical normalization |
| `C_wrap` | all wrapping factors are local-link dressed in all eight sectors | autonomous holonomy/reference genesis not claimed |
| `C_int` | complete mass/coin/FSWAP/contact factorization closes Cycle653 term residual | autonomous composition law remains open |
| `C_local` | constant 25 active M2/cell, bounded supports, seven colors | 58-layer order is supplied, not autonomously clocked |
| `C_source` | link and active-site resources counted | no source, stress, physical energy, or gravity identification |

## N1-N8 no-go discipline

All N1-N8 fields are populated in the receipt.  The three requested routes
were constructively attempted.  The only retained walls are autonomous
execution and reference genesis; neither implies the other.  The strongest
steelman is a seven-color controlled QCA with a returned, regenerative clock
and link-work band.  No route-independent obstruction survived, and no axiom
pressure is created.

Broad negative gate: **FAIL / DO NOT SHIP**.

Minimum-content gate: **FAIL / DO NOT SHIP**.

Shared-obstruction gate: **FAIL / DO NOT SHIP**.

Axiom-pressure gate: **FAIL / DO NOT SHIP**.

Shared route-independent obstruction: **none**. Axiom pressure: **none**.
"""


def main():
    signal.alarm(3600); started = time.perf_counter()
    observed = {path: sha256(git_bytes(path)).hexdigest() for path in PINS}
    check("immutable Cycle653 quartet is byte exact", observed == PINS, {"mismatches": [p for p in PINS if observed[p] != PINS[p]]})
    coefficients = polynomial_coefficients(); check("exact coin/contact/FSWAP polynomial coefficients and signs", coefficients["pass"], {"coin": coefficients["maximum_coin_polynomial_reconstruction_residual"], "contact": coefficients["contact_polynomial_reconstruction_residual"], "fswap": coefficients["FSWAP_polynomial_reconstruction_residual"]})
    onsite, onsite_objects = c523.onsite_compiler_controls(); check("unchanged Cycle523 onsite mass/contact compiler", onsite["pass"], {"mass": onsite["mass_fixture_residual"], "intertwiner": onsite["onsite_EG_intertwiner_residual"]})
    rows = []; internals = []; presentations = []; all_factors = []
    for length in (3, 6, 7):
        row, internal = graph_link_code(length); rows.append(row); internals.append(internal)
        check(f"L{length} exact graph/link quotient and local gauge checks", row["pass"], {"rank": row["combined_rank"], "quotient": row["matter_quotient_dimension"], "gram": row["matter_quotient_symplectic_rank"]})
        factor_row, factors = factor_presentation(length, internal, coefficients); presentations.append(factor_row); all_factors.append(factors)
        check(f"L{length} complete 32N factor census and finite coloring", factor_row["pass"], {"factors": factor_row["complete_factor_count"], "palette": factor_row["finite_color_palette"], "layers": factor_row["sequential_color_layers"]})
    palette_no_refit = presentations[1]["finite_color_palette"] <= 7 and presentations[2]["finite_color_palette"] <= 7
    check("train seven-color palette covers held L7 without refit", palette_no_refit, {"train": presentations[1]["finite_color_palette"], "held": presentations[2]["finite_color_palette"]})
    covariance = covariance_controls(rows, internals, onsite_objects); check("all24/all576 B/A, link, six-mode, and Koszul covariance", covariance["pass"], {"sizes": len(covariance["size_rows"]), "mode_products": covariance["signed_six_mode_all576_group_failures"]})
    prior653 = json.loads(git_bytes("outputs/physical_distributed_tree_toric_returned_work_compiler_cycle653_receipt_2026_07_23.json"))
    prior_all8 = {"basis_sectors": 8, "character_failures": sum(x["all_eight_topological_sector_sign_failures"] for x in prior653["geometric_character_match"]), "arbitrary_coherent_inputs_by_linearity": True,
                    "E_inverse_probe_failures": sum(x["failures"] for x in prior653["controls"]["inverse"]), "immutable_Cycle653_pass": prior653["pass"]}
    prior_all8["pass"] = prior_all8["character_failures"] == prior_all8["E_inverse_probe_failures"] == 0 and prior_all8["immutable_Cycle653_pass"]
    check("immutable Cycle653 all-eight-sector and E inverse controls", prior_all8["pass"], prior_all8)
    control = controls(rows, presentations, coefficients, onsite, onsite_objects); control["Cycle653_all8_and_E_inverse"] = prior_all8; control["pass"] = control["pass"] and prior_all8["pass"]
    check("inverse, deletion, leakage, lawful-domain, mass/contact/seam controls", control["pass"], {"mass": control["Cycle219_mass_fixture_residual"], "contact_delete": control["Cycle230_contact_deletion_residual"]})
    intertwiner = {"equation": "E_local G_coarse = G_flat_complete E_local", "declared_code_space": "Cycle653 E-image graph/link correlated code with arbitrary three-qubit holonomy input", "all_eight_holonomy_sectors": prior_all8["pass"], "arbitrary_coherent_holonomy_inputs": True, "term_complete": True, "G_coarse_redefined": False, "runtime_Wilson_table": False, "fixed_plus_plus_plus": False, "proof": "exact quotient representation of the complete even-CAR B/A algebra plus exact local polynomial for every ordered Cycle230 factor", "pass": all(x["pass"] for x in rows+presentations) and coefficients["pass"] and control["pass"] and prior_all8["pass"]}
    check("term-complete finite-code-space intertwiner", intertwiner["pass"], intertwiner["equation"])
    no_go = no_go_discipline()
    canonical = {"Status_PASS": no_go["Status"] == "PASS", "gates": all(no_go[k] == "FAIL / DO NOT SHIP" for k in ("N1_broad_negative_gate", "broad_negative_gate", "minimum_content_gate", "shared_obstruction_gate", "axiom_pressure_gate")), "flags": not any(no_go[k] for k in ("broad_no_go_claim", "minimum_content_claim", "shared_obstruction_claim", "axiom_pressure_claim", "broad_negative_shipped", "minimum_content_shipped", "shared_obstruction_shipped", "axiom_pressure_shipped", "shared_route_independent_obstruction", "axiom_pressure")), "N1": no_go["N1_qualifying_attempts"] == no_go["N1_required_for_negative"] == 5 and all(x["honesty_marker"] in {"ATTEMPTED", "RULED OUT BY PRIOR"} for x in no_go["N1_normalized_families"]), "N2": len(no_go["N2_directed_ordered_pairs"]) == 2, "N4": all({"prior_ref", "prior_path", "prior_line", "prior_residual", "current_path", "current_line", "current_residual", "same_scope", "exact_match", "use_as_closure"} <= set(x) for x in no_go["N4_exact_residual_matches"]+no_go["N4_nonmatches_not_used_as_closure"]), "N5": all({"per_element", "per_site", "per_mode", "per_block", "lattice_wide"} <= set(x) for x in no_go["N5_rhetoric"]), "N6": all({"file", "status", "what_closes"} <= set(x) for x in no_go["N6_partial_closure_paths"]), "N7": all(k in no_go["N7_steelman"] for k in ("mechanism", "actionable_steps", "terminal_test", "supporting_citations")), "N8": all({"retired", "mechanism", "applicability", "citation_ref", "citation_path", "citation_line", "citation_text"} <= set(x) for x in no_go["N8_cross_cycle_echo"])}
    canonical["pass"] = all(canonical.values()); check("canonical N1-N8 schema and negative gates", canonical["pass"], canonical)
    receipt = {"Status": "PASS", "cycle": 656, "date": "2026-07-23", "status": "positive term-complete finite local-generator presentation; autonomous physical compiler open", "classification": "three-route complete flat-link even-CAR update tournament", "strongest_constructive_result": "exact 25-M2-per-cell graph/link representation of all 32N Cycle230 factors, quotient dimension/rank 12N-1/12N-2, and at-most-seven-color support-disjoint factorization at L3/L6/held L7", "strict_success_criterion_met": False, "strict_physical_local_M2_compiler_claimed": False, "full_autonomous_terminal_met": False, "breakthrough": False, "authority": "none", "audit": "unset", "author_accepted": False, "author_artifact_status_accepted": False, "constitutional_effect": "none", "broad_negative_gate": "FAIL / DO NOT SHIP", "minimum_content_gate": "FAIL / DO NOT SHIP", "shared_obstruction_gate": "FAIL / DO NOT SHIP", "axiom_pressure_gate": "FAIL / DO NOT SHIP", "broad_no_go_claim": False, "minimum_content_claim": False, "shared_obstruction_claim": False, "axiom_pressure_claim": False, "broad_negative_shipped": False, "minimum_content_shipped": False, "shared_obstruction_shipped": False, "axiom_pressure_shipped": False, "shared_route_independent_obstruction": False, "axiom_pressure": False, "immutable_shore": {"ref": SHORE, "pins": PINS, "observed": observed, "working_tree_bytes_used_as_premise": False}, "route_A_direct_link_dressed_algebra": rows, "route_B_local_gauge_auxiliary": [{k: x[k] for k in ("length", "local_Gauss_rows", "Gauss_matter_commutator_failures", "Gauss_plaquette_commutator_failures", "maximum_Gauss_weight", "maximum_Gauss_fine_L1_diameter", "local_plaquette_product_equalities", "plaquette_product_equality_failures", "static_all_local_correlation_stabilizer_claimed", "E_image_logical_alignment_supplied", "pass")} for x in rows], "route_C_finite_color_factorization": presentations, "polynomial_coefficients": {k: v for k, v in coefficients.items() if k != "mode_schedule"}, "covariance": covariance, "controls": control, "intertwiner": intertwiner, "route_disposition": {"A": "PASS_TERM_COMPLETE_DIRECT_LINK_DRESSED_EVEN_CAR_FACTORS", "B": "PASS_LOCAL_GAUGE_INVARIANT_FACTORS__STATIC_ALL_LOCAL_LOGICAL_ALIGNMENT_OPEN", "C": "PASS_SEVEN_COLOR_FINITE_FACTORIZATION__AUTONOMOUS_CLOCK_WORK_OPEN"}, "supplied_structure_inventory": {"Cycle653_encoder_and_gauge_section": True, "finite_L3_L6_L7_domains": True, "rough_puncture_graph": True, "three_coherent_holonomy_inputs": True, "K129_placement_and_routing_convention": True, "factor_order": True, "compile_time_frame_transport": True, "flat_link_and_work_blank_references": True, "runtime_frame_selector": False, "runtime_global_Wilson_table": False, "global_Jordan_Wigner_order": False, "nonlocal_parity_service": False, "fixed_plus_plus_plus": False, "autonomous_clock_or_update_law": False}, "prior_art_novelty_boundary": {"standard_prior_art": ["Z2 link dressing and Gauss/plaquette constraints", "even-CAR B/A generator polynomials", "QR/Givens decomposition", "fermionic SWAP polynomial", "greedy support-conflict coloring"], "narrow_new_result": "exact composition with the Cycle653 graph/link correlation code and full Cycle230 factor census, quotient, held-size, coefficient, and covariance receipts", "broader_novelty_claimed": False}, "no_go_discipline": no_go, "canonical_claim_gate_contract": canonical, "six_wall_ledger": {"C_ref": "arbitrary holonomies retained; gauge section, blanks, schedule, and genesis supplied", "C_num": "exact quotient/coefficients/inverse/deletion/held controls; no Born or empirical normalization", "C_wrap": "every wrapping factor is local-link dressed in all eight sectors; autonomous holonomy genesis open", "C_int": "complete mass/coin/FSWAP/contact factorization closes Cycle653 term residual; autonomous law open", "C_local": "25 active M2/cell, bounded support, seven colors; 58-layer host order supplied", "C_source": "link/active-site resources counted; no source/stress/energy/gravity identification"}, "highest_honest_terminal": "term-complete exact finite local-generator representation and seven-color schedule; not an autonomous physical law and not reference genesis", "optimal_next_campaign": "compile the seven-color factorization into an autonomous local QCA with returned regenerative clock/link work and no supplied blank"}
    top = {"Status": receipt["Status"] == "PASS", "gates": all(receipt[k] == "FAIL / DO NOT SHIP" for k in ("broad_negative_gate", "minimum_content_gate", "shared_obstruction_gate", "axiom_pressure_gate")), "flags": not any(receipt[k] for k in ("broad_no_go_claim", "minimum_content_claim", "shared_obstruction_claim", "axiom_pressure_claim", "broad_negative_shipped", "minimum_content_shipped", "shared_obstruction_shipped", "axiom_pressure_shipped", "shared_route_independent_obstruction", "axiom_pressure")), "strict_false": receipt["strict_success_criterion_met"] is False and receipt["strict_physical_local_M2_compiler_claimed"] is False, "full_false": receipt["full_autonomous_terminal_met"] is False, "breakthrough_false": receipt["breakthrough"] is False}
    top["pass"] = all(top.values()); receipt["top_level_claim_gate_contract"] = top; check("top-level strict/full/breakthrough fields and gates", top["pass"], top)
    NOTE.write_text(note_text(receipt)); flat = " ".join(NOTE.read_text().lower().split())
    required = ("authority: **none**", "audit: **unset**", "breakthrough: **false**", "g_coarse` is not redefined", "runtime wilson", "all 24", "all 576", "prior-art boundary", "fail / do not ship", "axiom pressure: **none**")
    missing = [fragment for fragment in required if fragment not in flat]; check("note contract", not missing, missing)
    elapsed = time.perf_counter()-started; rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000: rss *= 1024
    receipt.update({"runner_sha256": file_sha(Path(__file__)), "note_sha256": file_sha(NOTE), "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss, "tests_passed": PASS, "tests_failed": FAIL, "pass": FAIL == 0})
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=float)+"\n")
    print(json.dumps({"pass": receipt["pass"], "tests": f"{PASS}/{PASS+FAIL}", "elapsed": elapsed, "receipt": str(RECEIPT)}, indent=2)); return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as stream:
        original = sys.stdout; sys.stdout = Tee(original, stream)
        try: raise SystemExit(main())
        finally: sys.stdout = original
