#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 local constraints source, part 1/3."""

TARGET_SOURCE = "scripts/frontier_cycle873_f17_open_box_local_constraints_core_2026_08_03.py"
PART_ORDINAL = 1
PART_COUNT = 3
FIRST_SOURCE_LINE = 1
LAST_SOURCE_LINE = 529
TOTAL_SOURCE_LINES = 1092
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "70d7362a2f534bd94b5b421f38e0c0509483ed8c1962b83f21f790b4c1dcb685"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 000001|#!/usr/bin/env python3
# C873SRC 000002|"""Cycle873 physical-M2 F17 open-box local-constraint core.
# C873SRC 000003|
# C873SRC 000004|The construction is the local-constraint complement to the Cycle873 F17-only
# C873SRC 000005|F17 seam augmentation.  Every oriented link is the actual 17-rail unary bank.
# C873SRC 000006|It defines:
# C873SRC 000007|
# C873SRC 000008|* the fixed-support one-hot projector on each link;
# C873SRC 000009|* modular star clocks/projectors for G_x=N_x+alpha div(ell), with the
# C873SRC 000010|  typed family/polarity sign alpha in {-1,+1}; and
# C873SRC 000011|* order-17 plaquette translations made from four unary cyclic shifts.
# C873SRC 000012|
# C873SRC 000013|The sparse plaquette translation is emitted physically as 64 nearest-neighbour
# C873SRC 000014|SWAPs.  The star clock is emitted with the landed ideal arbitrary-RZ and
# C873SRC 000015|one-site phase primitives.  Preparation or measurement of the +1 eigenspace,
# C873SRC 000016|spectral projector realization, finite-gate synthesis, periodic harmonic-sector
# C873SRC 000017|selection, and all genesis remain supplied/open.  No physical-energy, source,
# C873SRC 000018|gravity interpretation is made.  These operators characterize and preserve a
# C873SRC 000019|code space; they do not autonomously prepare, project, enforce, cool, or reset
# C873SRC 000020|that space.
# C873SRC 000021|"""
# C873SRC 000022|
# C873SRC 000023|from __future__ import annotations
# C873SRC 000024|
# C873SRC 000025|from collections import Counter, defaultdict
# C873SRC 000026|from hashlib import sha256
# C873SRC 000027|from itertools import product
# C873SRC 000028|import argparse
# C873SRC 000029|import json
# C873SRC 000030|import math
# C873SRC 000031|from pathlib import Path
# C873SRC 000032|import subprocess
# C873SRC 000033|import sys
# C873SRC 000034|
# C873SRC 000035|import numpy as np
# C873SRC 000036|
# C873SRC 000037|
# C873SRC 000038|HERE = Path(__file__).resolve().parent
# C873SRC 000039|ROOT = HERE.parent
# C873SRC 000040|sys.path.insert(0, str(HERE))
# C873SRC 000041|sys.path.insert(0, str(ROOT / "scripts"))
# C873SRC 000042|
# C873SRC 000043|import frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03 as INT
# C873SRC 000044|
# C873SRC 000045|
# C873SRC 000046|C870, J870, C871, C714 = INT.C870, INT.J870, INT.C871, INT.C714
# C873SRC 000047|Coord = tuple[int, int, int]
# C873SRC 000048|Edge = tuple[Coord, int]
# C873SRC 000049|Plaquette = tuple[Coord, int, int]
# C873SRC 000050|F17 = 17
# C873SRC 000051|TOL = 3.0e-10
# C873SRC 000052|SHAPES = ((2, 2, 2), (3, 3, 3), (3, 2, 2))
# C873SRC 000053|EXPECTED_BASE_COMMIT = INT.EXPECTED_BASE_COMMIT
# C873SRC 000054|OUT = ROOT / "outputs/cycle873_f17_open_box_local_constraints_core_receipt_2026_08_03.json"
# C873SRC 000055|INTEGRATION_PATH = (
# C873SRC 000056|    HERE / "frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py"
# C873SRC 000057|)
# C873SRC 000058|EXPECTED_INTEGRATION_SHA256 = (
# C873SRC 000059|    "8f0f23d86cc83c433be3e86a66e719631c70da7fbd8a1adf6b85b65815448ad7"
# C873SRC 000060|)
# C873SRC 000061|
# C873SRC 000062|
# C873SRC 000063|def digest(path: Path) -> str:
# C873SRC 000064|    return sha256(path.read_bytes()).hexdigest()
# C873SRC 000065|
# C873SRC 000066|
# C873SRC 000067|def add(*rows: Coord) -> Coord:
# C873SRC 000068|    return tuple(sum(values) for values in zip(*rows))
# C873SRC 000069|
# C873SRC 000070|
# C873SRC 000071|def sub(left: Coord, right: Coord) -> Coord:
# C873SRC 000072|    return tuple(a - b for a, b in zip(left, right))
# C873SRC 000073|
# C873SRC 000074|
# C873SRC 000075|def scale(value: int, row: Coord) -> Coord:
# C873SRC 000076|    return tuple(value * item for item in row)
# C873SRC 000077|
# C873SRC 000078|
# C873SRC 000079|def unit(axis: int) -> Coord:
# C873SRC 000080|    return tuple(int(index == axis) for index in range(3))
# C873SRC 000081|
# C873SRC 000082|
# C873SRC 000083|def l1(left: Coord, right: Coord) -> int:
# C873SRC 000084|    return sum(abs(a - b) for a, b in zip(left, right))
# C873SRC 000085|
# C873SRC 000086|
# C873SRC 000087|def linf(left: Coord, right: Coord) -> int:
# C873SRC 000088|    return max(abs(a - b) for a, b in zip(left, right))
# C873SRC 000089|
# C873SRC 000090|
# C873SRC 000091|def shape_cells(shape):
# C873SRC 000092|    return tuple(product(*(range(length) for length in shape)))
# C873SRC 000093|
# C873SRC 000094|
# C873SRC 000095|def matrix_rank_mod(matrix: np.ndarray, modulus: int = F17) -> int:
# C873SRC 000096|    rows = np.asarray(matrix, dtype=np.int64).copy() % modulus
# C873SRC 000097|    pivot_row = 0
# C873SRC 000098|    for column in range(rows.shape[1]):
# C873SRC 000099|        pivot = next(
# C873SRC 000100|            (row for row in range(pivot_row, rows.shape[0]) if rows[row, column]),
# C873SRC 000101|            None,
# C873SRC 000102|        )
# C873SRC 000103|        if pivot is None:
# C873SRC 000104|            continue
# C873SRC 000105|        if pivot != pivot_row:
# C873SRC 000106|            rows[[pivot_row, pivot]] = rows[[pivot, pivot_row]]
# C873SRC 000107|        rows[pivot_row] = (
# C873SRC 000108|            rows[pivot_row] * pow(int(rows[pivot_row, column]), -1, modulus)
# C873SRC 000109|        ) % modulus
# C873SRC 000110|        for row in range(rows.shape[0]):
# C873SRC 000111|            if row != pivot_row and rows[row, column]:
# C873SRC 000112|                rows[row] = (
# C873SRC 000113|                    rows[row] - rows[row, column] * rows[pivot_row]
# C873SRC 000114|                ) % modulus
# C873SRC 000115|        pivot_row += 1
# C873SRC 000116|        if pivot_row == rows.shape[0]:
# C873SRC 000117|            break
# C873SRC 000118|    return pivot_row
# C873SRC 000119|
# C873SRC 000120|
# C873SRC 000121|def graph_edges(graph) -> tuple[Edge, ...]:
# C873SRC 000122|    return tuple((cell, axis) for cell, axis, _target, _lm, _rm in C870.graph_seams(graph))
# C873SRC 000123|
# C873SRC 000124|
# C873SRC 000125|def edge_head(edge: Edge) -> Coord:
# C873SRC 000126|    return add(edge[0], unit(edge[1]))
# C873SRC 000127|
# C873SRC 000128|
# C873SRC 000129|def plaquettes(shape) -> tuple[Plaquette, ...]:
# C873SRC 000130|    output = []
# C873SRC 000131|    for first in range(3):
# C873SRC 000132|        for second in range(first + 1, 3):
# C873SRC 000133|            ranges = [range(length) for length in shape]
# C873SRC 000134|            ranges[first] = range(shape[first] - 1)
# C873SRC 000135|            ranges[second] = range(shape[second] - 1)
# C873SRC 000136|            output.extend((base, first, second) for base in product(*ranges))
# C873SRC 000137|    return tuple(sorted(output))
# C873SRC 000138|
# C873SRC 000139|
# C873SRC 000140|def plaquette_boundary(row: Plaquette) -> dict[Edge, int]:
# C873SRC 000141|    base, first, second = row
# C873SRC 000142|    return {
# C873SRC 000143|        (base, first): 1,
# C873SRC 000144|        (add(base, unit(first)), second): 1,
# C873SRC 000145|        (add(base, unit(second)), first): -1,
# C873SRC 000146|        (base, second): -1,
# C873SRC 000147|    }
# C873SRC 000148|
# C873SRC 000149|
# C873SRC 000150|def chain_matrices(vertices, edges, faces):
# C873SRC 000151|    vertex_index = {vertex: index for index, vertex in enumerate(vertices)}
# C873SRC 000152|    edge_index = {edge: index for index, edge in enumerate(edges)}
# C873SRC 000153|    incidence = np.zeros((len(vertices), len(edges)), dtype=np.int64)
# C873SRC 000154|    for column, edge in enumerate(edges):
# C873SRC 000155|        incidence[vertex_index[edge[0]], column] = 1
# C873SRC 000156|        incidence[vertex_index[edge_head(edge)], column] = -1
# C873SRC 000157|    boundary = np.zeros((len(edges), len(faces)), dtype=np.int64)
# C873SRC 000158|    for column, face in enumerate(faces):
# C873SRC 000159|        for edge, coefficient in plaquette_boundary(face).items():
# C873SRC 000160|            boundary[edge_index[edge], column] = coefficient
# C873SRC 000161|    return incidence % F17, boundary % F17
# C873SRC 000162|
# C873SRC 000163|
# C873SRC 000164|def placement_map(graph, context):
# C873SRC 000165|    return {
# C873SRC 000166|        (seam[0], seam[1]): INT.integrated_placement(graph, context, seam)
# C873SRC 000167|        for seam in C870.graph_seams(graph)
# C873SRC 000168|    }
# C873SRC 000169|
# C873SRC 000170|
# C873SRC 000171|def cyclic_swap_pairs(placement, direction: int):
# C873SRC 000172|    order = range(15, -1, -1) if direction > 0 else range(16)
# C873SRC 000173|    return tuple(
# C873SRC 000174|        (placement.rails[index], placement.rails[index + 1]) for index in order
# C873SRC 000175|    )
# C873SRC 000176|
# C873SRC 000177|
# C873SRC 000178|def plaquette_swap_word(face: Plaquette, placements):
# C873SRC 000179|    rows = []
# C873SRC 000180|    per_edge = {}
# C873SRC 000181|    for edge, coefficient in plaquette_boundary(face).items():
# C873SRC 000182|        pairs = cyclic_swap_pairs(placements[edge], coefficient)
# C873SRC 000183|        per_edge[edge] = pairs
# C873SRC 000184|        rows.extend((edge, coefficient, pair) for pair in pairs)
# C873SRC 000185|    layers = tuple(
# C873SRC 000186|        tuple((edge, coefficient, per_edge[edge][step])
# C873SRC 000187|              for edge, coefficient in plaquette_boundary(face).items())
# C873SRC 000188|        for step in range(16)
# C873SRC 000189|    )
# C873SRC 000190|    return tuple(rows), layers
# C873SRC 000191|
# C873SRC 000192|
# C873SRC 000193|def support_geometry(sites, center):
# C873SRC 000194|    sites = tuple(sites)
# C873SRC 000195|    return {
# C873SRC 000196|        "M2": len(set(sites)),
# C873SRC 000197|        "Linf_radius": max(linf(site, center) for site in sites),
# C873SRC 000198|        "L1_radius": max(l1(site, center) for site in sites),
# C873SRC 000199|        "L1_diameter": max(l1(left, right) for left in sites for right in sites),
# C873SRC 000200|    }
# C873SRC 000201|
# C873SRC 000202|
# C873SRC 000203|def star_clock_word(graph, context, cell, edges, placements, family_sign: int = 1):
# C873SRC 000204|    theta = 2 * math.pi / F17
# C873SRC 000205|    word = []
# C873SRC 000206|    for mode in range(6):
# C873SRC 000207|        brow = C871.physical_b(graph, context, cell, mode)
# C873SRC 000208|        word.extend(C870.c707.compile_pauli_rotation(
# C873SRC 000209|            brow, context.sites, theta
# C873SRC 000210|        ))
# C873SRC 000211|    incident = tuple(
# C873SRC 000212|        edge for edge in edges if edge[0] == cell or edge_head(edge) == cell
# C873SRC 000213|    )
# C873SRC 000214|    for edge in incident:
# C873SRC 000215|        incidence_sign = 1 if edge[0] == cell else -1
# C873SRC 000216|        coefficient = family_sign * incidence_sign
# C873SRC 000217|        for label in range(1, F17):
# C873SRC 000218|            phase = np.exp(1j * theta * coefficient * label)
# C873SRC 000219|            word.append(C870.c707.Instruction(
# C873SRC 000220|                "F17_star_link_clock_phase",
# C873SRC 000221|                (placements[edge].rails[label],),
# C873SRC 000222|                np.diag((1.0 + 0.0j, phase)).astype(complex),
# C873SRC 000223|            ))
# C873SRC 000224|    return tuple(word), incident
# C873SRC 000225|
# C873SRC 000226|
# C873SRC 000227|def clock_primitive_certificate():
# C873SRC 000228|    theta = 2 * math.pi / F17
# C873SRC 000229|    matter_residual = link_residual = 0.0
# C873SRC 000230|    for occupation in (0, 1):
# C873SRC 000231|        b_eigenvalue = 1 - 2 * occupation
# C873SRC 000232|        observed = np.exp(0.5j * theta) * np.exp(-0.5j * theta * b_eigenvalue)
# C873SRC 000233|        matter_residual = max(
# C873SRC 000234|            matter_residual, abs(observed - np.exp(1j * theta * occupation))
# C873SRC 000235|        )
# C873SRC 000236|    for coefficient in (-1, 1):
# C873SRC 000237|        for label in range(F17):
# C873SRC 000238|            observed = np.exp(1j * theta * coefficient * label)
# C873SRC 000239|            expected = np.exp(2j * math.pi * coefficient * label / F17)
# C873SRC 000240|            link_residual = max(link_residual, abs(observed - expected))
# C873SRC 000241|    return {
# C873SRC 000242|        "omega": [math.cos(theta), math.sin(theta)],
# C873SRC 000243|        "matter_clock_formula": (
# C873SRC 000244|            "omega^n = exp(i*pi/17) exp[-i*(2*pi/17) B/2], B=1-2n"
# C873SRC 000245|        ),
# C873SRC 000246|        "matter_clock_phase_residual": matter_residual,
# C873SRC 000247|        "link_clock_formula": (
# C873SRC 000248|            "on the one-hot sector, apply diag(1,omega^(sigma*k)) to physical rail k"
# C873SRC 000249|        ),
# C873SRC 000250|        "link_clock_phase_residual": link_residual,
# C873SRC 000251|        "formal_zero_site_scalar_per_matter_mode": [
# C873SRC 000252|            math.cos(theta / 2), math.sin(theta / 2)
# C873SRC 000253|        ],
# C873SRC 000254|        "non_Clifford_angle": theta,
# C873SRC 000255|    }
# C873SRC 000256|
# C873SRC 000257|
# C873SRC 000258|def transform_edge(frame: np.ndarray, edge: Edge):
# C873SRC 000259|    moved_tail = C871.matvec(frame, edge[0])
# C873SRC 000260|    moved_direction = C871.matvec(frame, unit(edge[1]))
# C873SRC 000261|    target_axis = next(index for index, value in enumerate(moved_direction) if value)
# C873SRC 000262|    sign = moved_direction[target_axis]
# C873SRC 000263|    canonical_tail = moved_tail if sign > 0 else add(moved_tail, moved_direction)
# C873SRC 000264|    return (canonical_tail, target_axis), sign
# C873SRC 000265|
# C873SRC 000266|
# C873SRC 000267|def transform_plaquette(frame: np.ndarray, face: Plaquette):
# C873SRC 000268|    base, first, second = face
# C873SRC 000269|    vertices = (
# C873SRC 000270|        base,
# C873SRC 000271|        add(base, unit(first)),
# C873SRC 000272|        add(base, unit(second)),
# C873SRC 000273|        add(base, unit(first), unit(second)),
# C873SRC 000274|    )
# C873SRC 000275|    moved_vertices = tuple(C871.matvec(frame, vertex) for vertex in vertices)
# C873SRC 000276|    moved_first = C871.matvec(frame, unit(first))
# C873SRC 000277|    moved_second = C871.matvec(frame, unit(second))
# C873SRC 000278|    first_axis = next(index for index, value in enumerate(moved_first) if value)
# C873SRC 000279|    second_axis = next(index for index, value in enumerate(moved_second) if value)
# C873SRC 000280|    first_sign = moved_first[first_axis]
# C873SRC 000281|    second_sign = moved_second[second_axis]
# C873SRC 000282|    low, high = sorted((first_axis, second_axis))
# C873SRC 000283|    orientation = first_sign * second_sign * (1 if first_axis < second_axis else -1)
# C873SRC 000284|    target_base = tuple(min(vertex[index] for vertex in moved_vertices) for index in range(3))
# C873SRC 000285|    return (target_base, low, high), orientation
# C873SRC 000286|
# C873SRC 000287|
# C873SRC 000288|def accumulate(rows):
# C873SRC 000289|    output = defaultdict(int)
# C873SRC 000290|    for key, value in rows:
# C873SRC 000291|        output[key] += value
# C873SRC 000292|    return {key: value for key, value in output.items() if value}
# C873SRC 000293|
# C873SRC 000294|
# C873SRC 000295|def frame_certificate(fixtures_for_transport):
# C873SRC 000296|    frames = C871.proper_frames()
# C873SRC 000297|    boundary_failures = edge_product_failures = plaquette_product_failures = 0
# C873SRC 000298|    label_product_failures = orientation_failures = 0
# C873SRC 000299|    edge_frame_rows = plaquette_frame_rows = 0
# C873SRC 000300|    negative_edge_rows = 0
# C873SRC 000301|    for vertices, edges, faces in fixtures_for_transport:
# C873SRC 000302|        for frame in frames:
# C873SRC 000303|            for edge in edges:
# C873SRC 000304|                _target, sign = transform_edge(frame, edge)
# C873SRC 000305|                edge_frame_rows += 1
# C873SRC 000306|                negative_edge_rows += sign < 0
# C873SRC 000307|                for label in range(F17):
# C873SRC 000308|                    moved_label = (sign * label) % F17
# C873SRC 000309|                    orientation_failures += moved_label != (
# C873SRC 000310|                        label if sign > 0 else -label % F17
# C873SRC 000311|                    )
# C873SRC 000312|            for face in faces:
# C873SRC 000313|                target, orientation = transform_plaquette(frame, face)
# C873SRC 000314|                moved_boundary = accumulate(
# C873SRC 000315|                    (transform_edge(frame, edge)[0], coefficient * transform_edge(frame, edge)[1])
# C873SRC 000316|                    for edge, coefficient in plaquette_boundary(face).items()
# C873SRC 000317|                )
# C873SRC 000318|                expected_boundary = {
# C873SRC 000319|                    edge: orientation * coefficient
# C873SRC 000320|                    for edge, coefficient in plaquette_boundary(target).items()
# C873SRC 000321|                }
# C873SRC 000322|                boundary_failures += moved_boundary != expected_boundary
# C873SRC 000323|                plaquette_frame_rows += 1
# C873SRC 000324|        for right in frames:
# C873SRC 000325|            for left in frames:
# C873SRC 000326|                composed = left @ right
# C873SRC 000327|                for edge in edges:
# C873SRC 000328|                    middle, right_sign = transform_edge(right, edge)
# C873SRC 000329|                    sequential, left_sign = transform_edge(left, middle)
# C873SRC 000330|                    direct, direct_sign = transform_edge(composed, edge)
# C873SRC 000331|                    edge_product_failures += (
# C873SRC 000332|                        sequential, left_sign * right_sign
# C873SRC 000333|                    ) != (direct, direct_sign)
# C873SRC 000334|                    for label in range(F17):
# C873SRC 000335|                        label_product_failures += (
# C873SRC 000336|                            left_sign * right_sign * label
# C873SRC 000337|                        ) % F17 != (direct_sign * label) % F17
# C873SRC 000338|                for face in faces:
# C873SRC 000339|                    middle, right_sign = transform_plaquette(right, face)
# C873SRC 000340|                    sequential, left_sign = transform_plaquette(left, middle)
# C873SRC 000341|                    direct, direct_sign = transform_plaquette(composed, face)
# C873SRC 000342|                    plaquette_product_failures += (
# C873SRC 000343|                        sequential, left_sign * right_sign
# C873SRC 000344|                    ) != (direct, direct_sign)
# C873SRC 000345|
# C873SRC 000346|    # Physical gate/path transport uses a real emitted L2 plaquette word.
# C873SRC 000347|    graph = C870.prep.OpenReferenceGraph(shape_cells((2, 2, 2)))
# C873SRC 000348|    context = C870.physical_context(graph)
# C873SRC 000349|    placements = placement_map(graph, context)
# C873SRC 000350|    face = plaquettes((2, 2, 2))[0]
# C873SRC 000351|    word, _layers = plaquette_swap_word(face, placements)
# C873SRC 000352|    gate_frame_failures = gate_product_failures = 0
# C873SRC 000353|    star_cell = (0, 0, 0)
# C873SRC 000354|    star_sites = set()
# C873SRC 000355|    for mode in range(6):
# C873SRC 000356|        star_sites.update(C871.z_support(
# C873SRC 000357|            C871.physical_b(graph, context, star_cell, mode), context
# C873SRC 000358|        ))
# C873SRC 000359|    for edge, placement in placements.items():
# C873SRC 000360|        if edge[0] == star_cell or edge_head(edge) == star_cell:
# C873SRC 000361|            star_sites.update(placement.rails)
# C873SRC 000362|    star_frame_failures = star_product_failures = 0
# C873SRC 000363|    for frame in frames:
# C873SRC 000364|        gate_frame_failures += sum(
# C873SRC 000365|            l1(C871.matvec(frame, pair[0]), C871.matvec(frame, pair[1])) != 1
# C873SRC 000366|            for _edge, _coefficient, pair in word
# C873SRC 000367|        )
# C873SRC 000368|        star_frame_failures += len({
# C873SRC 000369|            C871.matvec(frame, site) for site in star_sites
# C873SRC 000370|        }) != len(star_sites)
# C873SRC 000371|    for left in frames:
# C873SRC 000372|        for right in frames:
# C873SRC 000373|            composed = left @ right
# C873SRC 000374|            gate_product_failures += sum(
# C873SRC 000375|                tuple(C871.matvec(left, C871.matvec(right, site)) for site in pair)
# C873SRC 000376|                != tuple(C871.matvec(composed, site) for site in pair)
# C873SRC 000377|                for _edge, _coefficient, pair in word
# C873SRC 000378|            )
# C873SRC 000379|            star_product_failures += sum(
# C873SRC 000380|                C871.matvec(left, C871.matvec(right, site))
# C873SRC 000381|                != C871.matvec(composed, site)
# C873SRC 000382|                for site in star_sites
# C873SRC 000383|            )
# C873SRC 000384|    return {
# C873SRC 000385|        "proper_frames": len(frames),
# C873SRC 000386|        "ordered_frame_products": len(frames) ** 2,
# C873SRC 000387|        "edge_frame_rows": edge_frame_rows,
# C873SRC 000388|        "plaquette_frame_rows": plaquette_frame_rows,
# C873SRC 000389|        "negative_edge_rows": negative_edge_rows,
# C873SRC 000390|        "boundary_equivariance_failures": boundary_failures,
# C873SRC 000391|        "edge_orientation_label_failures": orientation_failures,
# C873SRC 000392|        "edge_product_failures": edge_product_failures,
# C873SRC 000393|        "plaquette_product_failures": plaquette_product_failures,
# C873SRC 000394|        "label_product_failures": label_product_failures,
# C873SRC 000395|        "physical_NN_gate_frame_failures": gate_frame_failures,
# C873SRC 000396|        "physical_star_support_frame_failures": star_frame_failures,
# C873SRC 000397|        "physical_gate_product_rows": len(frames) ** 2 * len(word),
# C873SRC 000398|        "physical_gate_product_failures": gate_product_failures,
# C873SRC 000399|        "physical_star_support_product_rows": len(frames) ** 2 * len(star_sites),
# C873SRC 000400|        "physical_star_support_product_failures": star_product_failures,
# C873SRC 000401|        "plaquette_generator_transport_rule": (
# C873SRC 000402|            "S_p -> S_{F p}^{orientation}; the +1 eigenspace is unchanged when "
# C873SRC 000403|            "orientation=-1 because S and S^{-1} have the same +1 sector"
# C873SRC 000404|        ),
# C873SRC 000405|    }
# C873SRC 000406|
# C873SRC 000407|
# C873SRC 000408|def single_plaquette_uniform_certificate():
# C873SRC 000409|    uniform = np.ones(F17, dtype=complex) / math.sqrt(F17)
# C873SRC 000410|    shifted = np.roll(uniform, 1)
# C873SRC 000411|    basis = np.zeros(F17, dtype=complex)
# C873SRC 000412|    basis[0] = 1
# C873SRC 000413|    return {
# C873SRC 000414|        "fixed_divergence_cycle_dimension": F17,
# C873SRC 000415|        "plaquette_translation_order": F17,
# C873SRC 000416|        "uniform_plus_one_sector_dimension": 1,
# C873SRC 000417|        "uniform_normalization_residual": abs(float(np.vdot(uniform, uniform).real) - 1.0),
# C873SRC 000418|        "uniform_shift_residual": float(np.linalg.norm(shifted - uniform)),
# C873SRC 000419|        "uniform_shift_overlap": [
# C873SRC 000420|            float(np.vdot(uniform, shifted).real),
# C873SRC 000421|            float(np.vdot(uniform, shifted).imag),
# C873SRC 000422|        ],
# C873SRC 000423|        "basis_link_shift_residual": float(np.linalg.norm(np.roll(basis, 1) - basis)),
# C873SRC 000424|        "basis_link_shift_overlap": [
# C873SRC 000425|            float(np.vdot(basis, np.roll(basis, 1)).real),
# C873SRC 000426|            float(np.vdot(basis, np.roll(basis, 1)).imag),
# C873SRC 000427|        ],
# C873SRC 000428|        "nontrivial_power_identity_failures": sum(
# C873SRC 000429|            all((label + power) % F17 == label for label in range(F17))
# C873SRC 000430|            for power in range(1, F17)
# C873SRC 000431|        ),
# C873SRC 000432|    }
# C873SRC 000433|
# C873SRC 000434|
# C873SRC 000435|def exterior_fock_lift(one_particle: np.ndarray) -> np.ndarray:
# C873SRC 000436|    """Second-quantize a six-mode one-particle matrix in occupation order.
# C873SRC 000437|
# C873SRC 000438|    Rows and columns are the 64 bit words.  Equal-number matrix elements are
# C873SRC 000439|    the corresponding minors; unequal-number elements vanish.  This is an
# C873SRC 000440|    executed target construction, not a prose inference from the word
# C873SRC 000441|    "one-particle".
# C873SRC 000442|    """
# C873SRC 000443|    one_particle = np.asarray(one_particle, dtype=complex)
# C873SRC 000444|    if one_particle.shape != (6, 6):
# C873SRC 000445|        raise ValueError("the onsite target must have six one-particle modes")
# C873SRC 000446|    occupied = tuple(
# C873SRC 000447|        tuple(mode for mode in range(6) if bits >> mode & 1)
# C873SRC 000448|        for bits in range(64)
# C873SRC 000449|    )
# C873SRC 000450|    output = np.zeros((64, 64), dtype=complex)
# C873SRC 000451|    for source, source_modes in enumerate(occupied):
# C873SRC 000452|        for target, target_modes in enumerate(occupied):
# C873SRC 000453|            if len(source_modes) != len(target_modes):
# C873SRC 000454|                continue
# C873SRC 000455|            if not source_modes:
# C873SRC 000456|                output[target, source] = 1.0
# C873SRC 000457|            else:
# C873SRC 000458|                output[target, source] = np.linalg.det(
# C873SRC 000459|                    one_particle[np.ix_(target_modes, source_modes)]
# C873SRC 000460|                )
# C873SRC 000461|    return output
# C873SRC 000462|
# C873SRC 000463|
# C873SRC 000464|def onsite_stage_star_clock_certificate() -> dict:
# C873SRC 000465|    """Execute the onsite part of the new F17-star preservation argument.
# C873SRC 000466|
# C873SRC 000467|    Cycle870 already proves that its emitted physical words intertwine the
# C873SRC 000468|    six-mode coin, reverse, and contact targets.  Here we independently lift
# C873SRC 000469|    those live targets to all 64 occupation columns and test their commutator
# C873SRC 000470|    with the matter factor of the F17 star clock.  Since the onsite words leave
# C873SRC 000471|    every link rail unchanged, this is also their commutator with the complete
# C873SRC 000472|    matter-times-link star clock.
# C873SRC 000473|    """
# C873SRC 000474|    species = C870.c219.common_species(float(C870.c230.BETA))
# C873SRC 000475|    coin = np.asarray(species.coin, dtype=complex)
# C873SRC 000476|    coin_gates, _qr = C870.qr_coin_schedule(coin)
# C873SRC 000477|    reconstructed = np.eye(6, dtype=complex)
# C873SRC 000478|    for gate in coin_gates:
# C873SRC 000479|        embedded = np.eye(6, dtype=complex)
# C873SRC 000480|        embedded[np.ix_(gate.modes, gate.modes)] = gate.matrix
# C873SRC 000481|        reconstructed = embedded @ reconstructed
# C873SRC 000482|
# C873SRC 000483|    reverse = np.asarray(C870.base.c210.REVERSE, dtype=complex)
# C873SRC 000484|    coin_fock = exterior_fock_lift(coin)
# C873SRC 000485|    reverse_fock = exterior_fock_lift(reverse)
# C873SRC 000486|    occupations = np.asarray([bits.bit_count() for bits in range(64)])
# C873SRC 000487|    theta = 2 * math.pi / F17
# C873SRC 000488|    matter_clock = np.diag(np.exp(1j * theta * occupations))
# C873SRC 000489|    coupling = float(C870.c230.COUPLING)
# C873SRC 000490|    contact_fock = np.diag(
# C873SRC 000491|        np.exp(1j * coupling * occupations * (occupations - 1) / 2)
# C873SRC 000492|    ).astype(complex)
# C873SRC 000493|    onsite_epoch = contact_fock @ reverse_fock @ coin_fock
# C873SRC 000494|    targets = {
# C873SRC 000495|        "coin": coin_fock,
# C873SRC 000496|        "reverse": reverse_fock,
# C873SRC 000497|        "contact": contact_fock,
# C873SRC 000498|        "composed_onsite_epoch": onsite_epoch,
# C873SRC 000499|    }
# C873SRC 000500|    commutators = {
# C873SRC 000501|        name: float(np.linalg.norm(matrix @ matter_clock - matter_clock @ matrix))
# C873SRC 000502|        for name, matrix in targets.items()
# C873SRC 000503|    }
# C873SRC 000504|    unitarity = {
# C873SRC 000505|        name: float(np.linalg.norm(matrix.conj().T @ matrix - np.eye(64)))
# C873SRC 000506|        for name, matrix in targets.items()
# C873SRC 000507|    }
# C873SRC 000508|
# C873SRC 000509|    # Active hostile control: a bare occupation-bit flip does not preserve the
# C873SRC 000510|    # order-17 matter clock.  This prevents the commutator gate from awarding
# C873SRC 000511|    # zero merely because it was wired to an identity matrix.
# C873SRC 000512|    bare_flip = np.zeros((64, 64), dtype=complex)
# C873SRC 000513|    for bits in range(64):
# C873SRC 000514|        bare_flip[bits ^ 1, bits] = 1.0
# C873SRC 000515|    hostile = float(np.linalg.norm(
# C873SRC 000516|        bare_flip @ matter_clock - matter_clock @ bare_flip
# C873SRC 000517|    ))
# C873SRC 000518|
# C873SRC 000519|    # Consume the live Cycle870 factor stream rather than merely naming its
# C873SRC 000520|    # three onsite stages.  Its exact physical-target intertwiner remains a
# C873SRC 000521|    # pinned upstream theorem input; this certificate supplies the additional
# C873SRC 000522|    # F17-star commutator that Cycle870 did not need to test.
# C873SRC 000523|    graph = C870.prep.OpenReferenceGraph(shape_cells((2, 2, 2)))
# C873SRC 000524|    rotations, _inventory = C870.build_update(graph, coin_gates)
# C873SRC 000525|    census = Counter(rotation.kind for rotation in rotations)
# C873SRC 000526|    onsite_census = {
# C873SRC 000527|        kind: census.get(kind, 0)
# C873SRC 000528|        for kind in (
# C873SRC 000529|            "onsite_coin_mass", "onsite_reverse_fswap", "onsite_contact"
