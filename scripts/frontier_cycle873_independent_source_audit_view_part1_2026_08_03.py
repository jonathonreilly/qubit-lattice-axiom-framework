#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 independent source, part 1/4."""

TARGET_SOURCE = "scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_independent_check_2026_08_03.py"
PART_ORDINAL = 1
PART_COUNT = 4
FIRST_SOURCE_LINE = 1
LAST_SOURCE_LINE = 480
TOTAL_SOURCE_LINES = 1546
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "02c3f321ba5ef1dce723ed04bd83919839648fd89202f607b6cc680645a97734"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 000001|#!/usr/bin/env python3
# C873SRC 000002|"""Independent Cycle873 check of the literal F17-augmented Cycle870 seam.
# C873SRC 000003|
# C873SRC 000004|This checker deliberately reads, but never imports, the Cycle873 primary or
# C873SRC 000005|physical core.  It reconstructs the
# C873SRC 000006|emitted word from the pinned landed primitives, proves the physical Pauli
# C873SRC 000007|compiler on arbitrary coherent inputs, and checks the effective encoded-domain
# C873SRC 000008|intertwiner, repeated factors, open-box local constraints, and the actual
# C873SRC 000009|Cycle219 one-particle recurrence/dispersion fixture.
# C873SRC 000010|"""
# C873SRC 000011|
# C873SRC 000012|from __future__ import annotations
# C873SRC 000013|
# C873SRC 000014|import argparse
# C873SRC 000015|import ast
# C873SRC 000016|from collections import Counter, defaultdict
# C873SRC 000017|from dataclasses import dataclass
# C873SRC 000018|from hashlib import sha256
# C873SRC 000019|from itertools import product
# C873SRC 000020|import json
# C873SRC 000021|import math
# C873SRC 000022|import os
# C873SRC 000023|from pathlib import Path
# C873SRC 000024|import subprocess
# C873SRC 000025|import sys
# C873SRC 000026|
# C873SRC 000027|import numpy as np
# C873SRC 000028|
# C873SRC 000029|
# C873SRC 000030|F17 = 17
# C873SRC 000031|TOL = 3.0e-10
# C873SRC 000032|EXPECTED_BASE_COMMIT = "c73a11d1ea7ddd564c48aa2a5a459a43d94262ef"
# C873SRC 000033|DEFAULT_ROOT = Path(__file__).resolve().parents[1]
# C873SRC 000034|PRIMARY_REL = Path("scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_primary_2026_08_03.py")
# C873SRC 000035|PRIMARY_SHA256 = "ab9f365c167b8fafb4f54508c0fb38b325bf687fdf8f222bc9aa833ad65dfc62"
# C873SRC 000036|PHYSICAL_CORE_REL = Path("scripts/frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py")
# C873SRC 000037|PHYSICAL_CORE_SHA256 = "8f0f23d86cc83c433be3e86a66e719631c70da7fbd8a1adf6b85b65815448ad7"
# C873SRC 000038|PHYSICAL_RECEIPT_REL = Path("outputs/cycle873_recurrent_f17_all_seam_physical_core_receipt_2026_08_03.json")
# C873SRC 000039|PHYSICAL_RECEIPT_SHA256 = "397657af570393fad9967edc55e74f7a66f46e8284fd5102be0f5e1df9247d0b"
# C873SRC 000040|DEFAULT_OUTPUT = DEFAULT_ROOT / "outputs/cycle873_recurrent_f17_uniform_affine_open_box_independent_check_receipt_2026_08_03.json"
# C873SRC 000041|EXPECTED_SOURCE_SHA256 = {
# C873SRC 000042|    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py":
# C873SRC 000043|        "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
# C873SRC 000044|    "scripts/frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02.py":
# C873SRC 000045|        "6645156635b4354d937759a28e71215121a19cefcc2f294a2791e6a84cf1423b",
# C873SRC 000046|    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py":
# C873SRC 000047|        "eb6c9a50681c69ea4fae47724c58d8ba10b48a270e7efa67a811af234afe9a1a",
# C873SRC 000048|    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":
# C873SRC 000049|        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
# C873SRC 000050|    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py":
# C873SRC 000051|        "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
# C873SRC 000052|}
# C873SRC 000053|
# C873SRC 000054|# Independently transcribed from the frozen primary declaration.  The AST
# C873SRC 000055|# check below separately asserts that the live declaration equals this tuple.
# C873SRC 000056|RAIL_LOCAL_OFFSETS = (
# C873SRC 000057|    (-2, 2, 0), (-2, 2, -1), (-1, 2, -1), (-1, 2, -2),
# C873SRC 000058|    (0, 2, -2), (1, 2, -2), (1, 1, -2), (2, 1, -2),
# C873SRC 000059|    (2, 0, -2), (2, -1, -2), (1, -1, -2), (1, -2, -2),
# C873SRC 000060|    (0, -2, -2), (-1, -2, -2), (-1, -2, -1), (-2, -2, -1),
# C873SRC 000061|    (-2, -2, -2),
# C873SRC 000062|)
# C873SRC 000063|
# C873SRC 000064|
# C873SRC 000065|def sha(path: Path) -> str:
# C873SRC 000066|    return sha256(path.read_bytes()).hexdigest()
# C873SRC 000067|
# C873SRC 000068|
# C873SRC 000069|def clean_float(value: float) -> float:
# C873SRC 000070|    return 0.0 if abs(value) < 5.0e-15 else float(value)
# C873SRC 000071|
# C873SRC 000072|
# C873SRC 000073|def state_distance(left: dict, right: dict) -> float:
# C873SRC 000074|    return float(math.sqrt(sum(
# C873SRC 000075|        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
# C873SRC 000076|        for key in set(left) | set(right)
# C873SRC 000077|    )))
# C873SRC 000078|
# C873SRC 000079|
# C873SRC 000080|def source_ast_certificate(root: Path) -> dict:
# C873SRC 000081|    primary = root / PRIMARY_REL
# C873SRC 000082|    physical = root / PHYSICAL_CORE_REL
# C873SRC 000083|    tree = ast.parse(physical.read_text(encoding="utf-8"))
# C873SRC 000084|    imports = []
# C873SRC 000085|    offsets = None
# C873SRC 000086|    emit = None
# C873SRC 000087|    for node in tree.body:
# C873SRC 000088|        if isinstance(node, ast.Import):
# C873SRC 000089|            imports.extend(alias.name for alias in node.names)
# C873SRC 000090|        elif isinstance(node, ast.ImportFrom):
# C873SRC 000091|            imports.append(node.module or "")
# C873SRC 000092|        elif isinstance(node, ast.Assign):
# C873SRC 000093|            if any(isinstance(target, ast.Name) and target.id == "RAIL_LOCAL_OFFSETS"
# C873SRC 000094|                   for target in node.targets):
# C873SRC 000095|                offsets = ast.literal_eval(node.value)
# C873SRC 000096|        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
# C873SRC 000097|            if node.target.id == "RAIL_LOCAL_OFFSETS":
# C873SRC 000098|                offsets = ast.literal_eval(node.value)
# C873SRC 000099|        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "emit_program":
# C873SRC 000100|            emit = node
# C873SRC 000101|    if emit is None:
# C873SRC 000102|        raise AssertionError("primary emit_program missing")
# C873SRC 000103|    emitted = ast.unparse(emit)
# C873SRC 000104|    ordered_needles = (
# C873SRC 000105|        "endpoint_pre=",
# C873SRC 000106|        "selected_seam=",
# C873SRC 000107|        "positive_compute=",
# C873SRC 000108|        "positive_shift=",
# C873SRC 000109|        "positive_uncompute=",
# C873SRC 000110|        "negative_compute=",
# C873SRC 000111|        "negative_shift=",
# C873SRC 000112|        "negative_uncompute=",
# C873SRC 000113|        "endpoint_clean=",
# C873SRC 000114|    )
# C873SRC 000115|    positions = tuple(emitted.index(needle) for needle in ordered_needles)
# C873SRC 000116|    required_semantics = (
# C873SRC 000117|        "physical_b(graph, context, cell, left_mode)",
# C873SRC 000118|        "physical_b(graph, context, target, right_mode)",
# C873SRC 000119|        "compile_rotations(selected, context)",
# C873SRC 000120|        "shift_word(placement, alpha, 'F17_positive_shift_')",
# C873SRC 000121|        "shift_word(placement, -alpha, 'F17_negative_shift_')",
# C873SRC 000122|        "right_b, context, placement.q_u, 'F17_clean_right_B_into_q_u'",
# C873SRC 000123|        "left_b, context, placement.q_v, 'F17_clean_left_B_into_q_v'",
# C873SRC 000124|    )
# C873SRC 000125|    missing = tuple(row for row in required_semantics if row not in emitted)
# C873SRC 000126|    return {
# C873SRC 000127|        "primary_sha256": sha(primary),
# C873SRC 000128|        "physical_core_sha256": sha(physical),
# C873SRC 000129|        "physical_receipt_sha256": sha(root / PHYSICAL_RECEIPT_REL),
# C873SRC 000130|        "physical_core_imports_cycle873_primary": any(
# C873SRC 000131|            "frontier_cycle873_recurrent_f17_uniform_affine_open_box_primary" in row
# C873SRC 000132|            for row in imports
# C873SRC 000133|        ),
# C873SRC 000134|        "checker_runtime_imported_primary": any(
# C873SRC 000135|            "frontier_cycle873_recurrent_f17_uniform_affine_open_box_primary" in name
# C873SRC 000136|            for name in sys.modules
# C873SRC 000137|        ),
# C873SRC 000138|        "rail_offsets_match": tuple(offsets or ()) == RAIL_LOCAL_OFFSETS,
# C873SRC 000139|        "emit_field_order_match": positions == tuple(sorted(positions)),
# C873SRC 000140|        "emit_required_semantics_missing": missing,
# C873SRC 000141|        "emit_ast_sha256": sha256(ast.dump(emit, include_attributes=False).encode()).hexdigest(),
# C873SRC 000142|    }
# C873SRC 000143|
# C873SRC 000144|
# C873SRC 000145|def setup_imports(root: Path):
# C873SRC 000146|    sys.path.insert(0, str(root / "scripts"))
# C873SRC 000147|    import frontier_cycle870_openreference_native_recurrent_update_2026_08_02 as C870
# C873SRC 000148|    import frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02 as C871
# C873SRC 000149|    import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as C714
# C873SRC 000150|    import common_matter_field_coin_family_cycle219_2026_07_16 as C219
# C873SRC 000151|    import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as C210
# C873SRC 000152|    return C870, C871, C714, C219, C210
# C873SRC 000153|
# C873SRC 000154|
# C873SRC 000155|def matrix_digest(C870, matrix: np.ndarray) -> str:
# C873SRC 000156|    return C870.c707.c655.matrix_digest(matrix)
# C873SRC 000157|
# C873SRC 000158|
# C873SRC 000159|def signature(C870, instruction):
# C873SRC 000160|    return instruction.kind, instruction.sites, matrix_digest(C870, instruction.matrix)
# C873SRC 000161|
# C873SRC 000162|
# C873SRC 000163|def word_digest(C870, word) -> str:
# C873SRC 000164|    return sha256(repr(tuple(signature(C870, row) for row in word)).encode()).hexdigest()
# C873SRC 000165|
# C873SRC 000166|
# C873SRC 000167|def add(*rows):
# C873SRC 000168|    return tuple(sum(values) for values in zip(*rows))
# C873SRC 000169|
# C873SRC 000170|
# C873SRC 000171|def scale(value, row):
# C873SRC 000172|    return tuple(value * item for item in row)
# C873SRC 000173|
# C873SRC 000174|
# C873SRC 000175|def at(midpoint, basis, local):
# C873SRC 000176|    return add(midpoint, *(scale(value, direction) for value, direction in zip(local, basis)))
# C873SRC 000177|
# C873SRC 000178|
# C873SRC 000179|def local_compile(C870, rotation, context):
# C873SRC 000180|    """Independent literal compiler for one physical Hermitian Pauli rotation."""
# C873SRC 000181|    Instruction = C870.c707.Instruction
# C873SRC 000182|    physical = C870.physical_lift(rotation.row, context)
# C873SRC 000183|    axes = []
# C873SRC 000184|    y_count = 0
# C873SRC 000185|    for index, site in enumerate(context.sites):
# C873SRC 000186|        x = (physical.x >> index) & 1
# C873SRC 000187|        z = (physical.z >> index) & 1
# C873SRC 000188|        if x and z:
# C873SRC 000189|            axes.append((site, "Y")); y_count += 1
# C873SRC 000190|        elif x:
# C873SRC 000191|            axes.append((site, "X"))
# C873SRC 000192|        elif z:
# C873SRC 000193|            axes.append((site, "Z"))
# C873SRC 000194|    exponent = (physical.phase - y_count) % 4
# C873SRC 000195|    if exponent not in (0, 2) or not axes:
# C873SRC 000196|        raise AssertionError(("bad Hermitian physical row", physical, exponent))
# C873SRC 000197|    sign = 1 if exponent == 0 else -1
# C873SRC 000198|    H = C870.c707.c655.H
# C873SRC 000199|    CNOT = C870.c707.c655.CNOT
# C873SRC 000200|    S = np.diag((1, 1j)).astype(complex)
# C873SRC 000201|    SD = S.conj().T
# C873SRC 000202|    rz = np.diag((
# C873SRC 000203|        np.exp(-0.5j * sign * rotation.angle),
# C873SRC 000204|        np.exp(0.5j * sign * rotation.angle),
# C873SRC 000205|    )).astype(complex)
# C873SRC 000206|    pivot = axes[0][0]
# C873SRC 000207|    word = []
# C873SRC 000208|    for site, axis in axes:
# C873SRC 000209|        if axis == "X":
# C873SRC 000210|            word.append(Instruction("basis_H", (site,), H))
# C873SRC 000211|        elif axis == "Y":
# C873SRC 000212|            word.extend((Instruction("basis_Sdg", (site,), SD), Instruction("basis_H", (site,), H)))
# C873SRC 000213|    for site, _axis in axes[1:]:
# C873SRC 000214|        word.append(Instruction("parity_CNOT", (site, pivot), CNOT))
# C873SRC 000215|    word.append(Instruction("axis_RZ", (pivot,), rz))
# C873SRC 000216|    for site, _axis in reversed(axes[1:]):
# C873SRC 000217|        word.append(Instruction("parity_CNOT", (site, pivot), CNOT))
# C873SRC 000218|    for site, axis in reversed(axes):
# C873SRC 000219|        if axis == "X":
# C873SRC 000220|            word.append(Instruction("basis_H", (site,), H))
# C873SRC 000221|        elif axis == "Y":
# C873SRC 000222|            word.extend((Instruction("basis_H", (site,), H), Instruction("basis_S", (site,), S)))
# C873SRC 000223|    return physical, tuple(axes), tuple(word)
# C873SRC 000224|
# C873SRC 000225|
# C873SRC 000226|def apply_dense(state: np.ndarray, matrix: np.ndarray, wires: tuple[int, ...], count: int):
# C873SRC 000227|    wire_axes = [count - 1 - wire for wire in wires]
# C873SRC 000228|    local_axes = list(reversed(wire_axes))
# C873SRC 000229|    other = [axis for axis in range(count) if axis not in local_axes]
# C873SRC 000230|    order = other + local_axes
# C873SRC 000231|    inverse = np.argsort(order)
# C873SRC 000232|    tensor = state.reshape((2,) * count).transpose(order)
# C873SRC 000233|    flat = tensor.reshape((-1, 1 << len(wires)))
# C873SRC 000234|    updated = flat @ np.asarray(matrix, dtype=complex).T
# C873SRC 000235|    return updated.reshape(tensor.shape).transpose(inverse).reshape(-1)
# C873SRC 000236|
# C873SRC 000237|
# C873SRC 000238|def apply_pauli_dense(C870, state, row, count):
# C873SRC 000239|    X = C870.c707.c655.X
# C873SRC 000240|    Z = np.diag((1, -1)).astype(complex)
# C873SRC 000241|    output = state
# C873SRC 000242|    for wire in range(count):
# C873SRC 000243|        x, z = (row.x >> wire) & 1, (row.z >> wire) & 1
# C873SRC 000244|        if x or z:
# C873SRC 000245|            output = apply_dense(output, np.linalg.matrix_power(X, x) @ np.linalg.matrix_power(Z, z), (wire,), count)
# C873SRC 000246|    return (1j ** row.phase) * output
# C873SRC 000247|
# C873SRC 000248|
# C873SRC 000249|def restrict_pauli(C870, row, all_sites, union):
# C873SRC 000250|    index = {site: i for i, site in enumerate(union)}
# C873SRC 000251|    x = z = 0
# C873SRC 000252|    for source, site in enumerate(all_sites):
# C873SRC 000253|        if site in index:
# C873SRC 000254|            target = index[site]
# C873SRC 000255|            x |= ((row.x >> source) & 1) << target
# C873SRC 000256|            z |= ((row.z >> source) & 1) << target
# C873SRC 000257|    return C870.Pauli(row.phase, x, z)
# C873SRC 000258|
# C873SRC 000259|
# C873SRC 000260|def poly_clean(C870, poly):
# C873SRC 000261|    output = {}
# C873SRC 000262|    for row, coefficient in poly.items():
# C873SRC 000263|        canonical = C870.Pauli(0, row.x, row.z)
# C873SRC 000264|        output[canonical] = output.get(canonical, 0.0j) + (1j ** row.phase) * coefficient
# C873SRC 000265|    return {row: value for row, value in output.items() if abs(value) > 2e-12}
# C873SRC 000266|
# C873SRC 000267|
# C873SRC 000268|def poly_mul(C870, left, right):
# C873SRC 000269|    out = {}
# C873SRC 000270|    for a, av in left.items():
# C873SRC 000271|        for b, bv in right.items():
# C873SRC 000272|            row = a @ b
# C873SRC 000273|            out[row] = out.get(row, 0.0j) + av * bv
# C873SRC 000274|    return poly_clean(C870, out)
# C873SRC 000275|
# C873SRC 000276|
# C873SRC 000277|def poly_scale(C870, poly, scalar):
# C873SRC 000278|    return poly_clean(C870, {row: scalar * value for row, value in poly.items()})
# C873SRC 000279|
# C873SRC 000280|
# C873SRC 000281|def poly_add(C870, *polys):
# C873SRC 000282|    out = {}
# C873SRC 000283|    for poly in polys:
# C873SRC 000284|        for row, value in poly.items():
# C873SRC 000285|            out[row] = out.get(row, 0.0j) + value
# C873SRC 000286|    return poly_clean(C870, out)
# C873SRC 000287|
# C873SRC 000288|
# C873SRC 000289|def poly_residual(C870, left, right):
# C873SRC 000290|    keys = set(left) | set(right)
# C873SRC 000291|    return float(math.sqrt(sum(abs(left.get(k, 0j) - right.get(k, 0j)) ** 2 for k in keys)))
# C873SRC 000292|
# C873SRC 000293|
# C873SRC 000294|def aligned_poly_residual(C870, observed, expected):
# C873SRC 000295|    keys = set(observed) | set(expected)
# C873SRC 000296|    overlap = sum(np.conj(expected.get(k, 0j)) * observed.get(k, 0j) for k in keys)
# C873SRC 000297|    phase = overlap / abs(overlap) if overlap else 1 + 0j
# C873SRC 000298|    return poly_residual(C870, observed, poly_scale(C870, expected, phase)), phase
# C873SRC 000299|
# C873SRC 000300|
# C873SRC 000301|def physical_seam_certificate(C870, C871):
# C873SRC 000302|    graph = C870.prep.OpenReferenceGraph(tuple(product(range(2), repeat=3)))
# C873SRC 000303|    context = C870.physical_context(graph)
# C873SRC 000304|    seam = C870.graph_seams(graph)[0]
# C873SRC 000305|    rows = C871.selected_seam_rotations(graph, seam)
# C873SRC 000306|    physical_constraints = C870.physical_stabilizers(context)
# C873SRC 000307|    compiler_rows = []
# C873SRC 000308|    emitted = C871.compile_rotations(rows, context)
# C873SRC 000309|    rebuilt = []
# C873SRC 000310|    rng = np.random.default_rng(87017)
# C873SRC 000311|    execution_residuals = []
# C873SRC 000312|    deletion_witnesses = []
# C873SRC 000313|    constraint_anticommutators = 0
# C873SRC 000314|    row_weights = []
# C873SRC 000315|    compiler_match_failures = 0
# C873SRC 000316|    for rotation in rows:
# C873SRC 000317|        physical, axes, word = local_compile(C870, rotation, context)
# C873SRC 000318|        rebuilt.extend(word)
# C873SRC 000319|        row_weights.append((rotation.meta[0], (rotation.row.x | rotation.row.z).bit_count(), len(axes), len(word)))
# C873SRC 000320|        constraint_anticommutators += sum(not physical.commutes(s) for s in physical_constraints)
# C873SRC 000321|        union = tuple(site for site, _axis in axes)
# C873SRC 000322|        local = restrict_pauli(C870, physical, context.sites, union)
# C873SRC 000323|        count = len(union)
# C873SRC 000324|        state = rng.normal(size=1 << count) + 1j * rng.normal(size=1 << count)
# C873SRC 000325|        state = state.astype(complex) / np.linalg.norm(state)
# C873SRC 000326|        compiled = state.copy()
# C873SRC 000327|        local_index = {site: i for i, site in enumerate(union)}
# C873SRC 000328|        for instruction in word:
# C873SRC 000329|            wires = tuple(local_index[site] for site in instruction.sites)
# C873SRC 000330|            before = compiled
# C873SRC 000331|            after = apply_dense(before, instruction.matrix, wires, count)
# C873SRC 000332|            # Unitary suffixes preserve this exact full-word deletion distance.
# C873SRC 000333|            deletion_witnesses.append(float(np.linalg.norm(after - before)))
# C873SRC 000334|            compiled = after
# C873SRC 000335|        direct = (
# C873SRC 000336|            math.cos(rotation.angle / 2) * state
# C873SRC 000337|            - 1j * math.sin(rotation.angle / 2) * apply_pauli_dense(C870, state, local, count)
# C873SRC 000338|        )
# C873SRC 000339|        execution_residuals.append(float(np.linalg.norm(compiled - direct)))
# C873SRC 000340|        no_rz = state.copy()
# C873SRC 000341|        for instruction in word:
# C873SRC 000342|            if instruction.kind == "axis_RZ":
# C873SRC 000343|                continue
# C873SRC 000344|            no_rz = apply_dense(no_rz, instruction.matrix, tuple(local_index[s] for s in instruction.sites), count)
# C873SRC 000345|        compiler_rows.append({
# C873SRC 000346|            "meta": rotation.meta,
# C873SRC 000347|            "physical_weight": len(axes),
# C873SRC 000348|            "compiled_gates": len(word),
# C873SRC 000349|            "delete_axis_RZ_identity_residual": clean_float(float(np.linalg.norm(no_rz - state))),
# C873SRC 000350|            "delete_axis_RZ_action_residual_on_coherent_witness": float(np.linalg.norm(no_rz - direct)),
# C873SRC 000351|        })
# C873SRC 000352|    compiler_match_failures += tuple(signature(C870, x) for x in rebuilt) != tuple(signature(C870, x) for x in emitted)
# C873SRC 000353|
# C873SRC 000354|    abstract = tuple(rotation.row for rotation in rows)
# C873SRC 000355|    target = poly_add(C870, *(poly_scale(C870, {row: 1 + 0j}, 0.5) for row in abstract))
# C873SRC 000356|    factored = {C870.Pauli(): 1 + 0j}
# C873SRC 000357|    rotations = []
# C873SRC 000358|    for row in abstract:
# C873SRC 000359|        rotations.append({
# C873SRC 000360|            C870.Pauli(): complex(math.cos(math.pi / 4)),
# C873SRC 000361|            row: complex(-1j * math.sin(math.pi / 4)),
# C873SRC 000362|        })
# C873SRC 000363|    for factor in rotations:
# C873SRC 000364|        factored = poly_mul(C870, factor, factored)
# C873SRC 000365|    identity = {C870.Pauli(): 1 + 0j}
# C873SRC 000366|    minus_identity = {C870.Pauli(): -1 + 0j}
# C873SRC 000367|    deletion_residuals = []
# C873SRC 000368|    for deleted in range(4):
# C873SRC 000369|        damaged = identity
# C873SRC 000370|        for index, factor in enumerate(rotations):
# C873SRC 000371|            if index != deleted:
# C873SRC 000372|                damaged = poly_mul(C870, factor, damaged)
# C873SRC 000373|        deletion_residuals.append(aligned_poly_residual(C870, damaged, target)[0])
# C873SRC 000374|    bu = {abstract[0]: 1 + 0j}
# C873SRC 000375|    bv = {abstract[1]: 1 + 0j}
# C873SRC 000376|    conj_u = poly_mul(C870, target, poly_mul(C870, bu, target))
# C873SRC 000377|    conj_v = poly_mul(C870, target, poly_mul(C870, bv, target))
# C873SRC 000378|    lift_homomorphism_failures = 0
# C873SRC 000379|    for left in abstract:
# C873SRC 000380|        for right in abstract:
# C873SRC 000381|            lift_homomorphism_failures += (
# C873SRC 000382|                C870.physical_lift(left @ right, context)
# C873SRC 000383|                != C870.physical_lift(left, context) @ C870.physical_lift(right, context)
# C873SRC 000384|            )
# C873SRC 000385|    return {
# C873SRC 000386|        "seam": seam,
# C873SRC 000387|        "physical_carrier_M2": len(context.sites),
# C873SRC 000388|        "rows": row_weights,
# C873SRC 000389|        "compiled_gate_count": len(rebuilt),
# C873SRC 000390|        "compiler_signature_match_failures": compiler_match_failures,
# C873SRC 000391|        "maximum_arbitrary_coherent_full_support_compiler_residual": max(execution_residuals),
# C873SRC 000392|        "minimum_literal_compiler_gate_deletion_witness_residual_full_support": min(deletion_witnesses),
# C873SRC 000393|        "inactive_literal_compiler_gate_deletions_on_coherent_witness": sum(x <= TOL for x in deletion_witnesses),
# C873SRC 000394|        "compiler_factor_rows": compiler_rows,
# C873SRC 000395|        "physical_constraint_anticommutators": constraint_anticommutators,
# C873SRC 000396|        "physical_lift_pair_homomorphism_failures": lift_homomorphism_failures,
# C873SRC 000397|        "raw_to_minus_i_FSWAP_residual": clean_float(poly_residual(C870, factored, poly_scale(C870, target, -1j))),
# C873SRC 000398|        "raw_to_literal_FSWAP_residual": poly_residual(C870, factored, target),
# C873SRC 000399|        "formal_i_corrected_to_FSWAP_residual": clean_float(poly_residual(C870, poly_scale(C870, factored, 1j), target)),
# C873SRC 000400|        "raw_square_to_minus_identity_residual": clean_float(poly_residual(C870, poly_mul(C870, factored, factored), minus_identity)),
# C873SRC 000401|        "target_square_to_identity_residual": clean_float(poly_residual(C870, poly_mul(C870, target, target), identity)),
# C873SRC 000402|        "occupation_conjugation_residuals": (
# C873SRC 000403|            clean_float(poly_residual(C870, conj_u, bv)),
# C873SRC 000404|            clean_float(poly_residual(C870, conj_v, bu)),
# C873SRC 000405|        ),
# C873SRC 000406|        "four_rotation_deletion_residuals_up_to_global_phase": deletion_residuals,
# C873SRC 000407|    }
# C873SRC 000408|
# C873SRC 000409|
# C873SRC 000410|def compose_small(C714, gates, qubits=3):
# C873SRC 000411|    mats = {"H": C714.H, "T": C714.T, "TD": C714.TD, "CNOT": C714.CNOT, "X": C714.X}
# C873SRC 000412|    output = np.eye(1 << qubits, dtype=complex)
# C873SRC 000413|    for kind, wires in gates:
# C873SRC 000414|        output = np.column_stack([
# C873SRC 000415|            C714.apply_small(output[:, column], mats[kind], wires, qubits)
# C873SRC 000416|            for column in range(1 << qubits)
# C873SRC 000417|        ])
# C873SRC 000418|    return output
# C873SRC 000419|
# C873SRC 000420|
# C873SRC 000421|def reversible_primitive_certificate(C714):
# C873SRC 000422|    full = list(C714.toffoli_primitives(0, 1, 2))
# C873SRC 000423|    reduced = [row for index, row in enumerate(full) if index != 1]
# C873SRC 000424|    tof = compose_small(C714, full)
# C873SRC 000425|    tof_target = np.zeros((8, 8), dtype=complex)
# C873SRC 000426|    for source in range(8):
# C873SRC 000427|        tof_target[source ^ (((source & 1) & ((source >> 1) & 1)) << 2), source] = 1
# C873SRC 000428|    reduced_matrix = compose_small(C714, reduced)
# C873SRC 000429|    clean = tuple(range(4))
# C873SRC 000430|    reduced_deletions = []
# C873SRC 000431|    for deleted in range(len(reduced)):
# C873SRC 000432|        damaged = compose_small(C714, [row for i, row in enumerate(reduced) if i != deleted])
# C873SRC 000433|        reduced_deletions.append(float(np.linalg.norm((damaged - tof)[:, clean])))
# C873SRC 000434|    fredkin = [("CNOT", (1, 2)), *C714.toffoli_primitives(0, 2, 1), ("CNOT", (1, 2))]
# C873SRC 000435|    fredkin_matrix = compose_small(C714, fredkin)
# C873SRC 000436|    fredkin_target = np.zeros((8, 8), dtype=complex)
# C873SRC 000437|    for source in range(8):
# C873SRC 000438|        c, left, right = source & 1, (source >> 1) & 1, (source >> 2) & 1
# C873SRC 000439|        target = source if not c else ((source & ~6) | (right << 1) | (left << 2))
# C873SRC 000440|        fredkin_target[target, source] = 1
# C873SRC 000441|    fredkin_deletions = []
# C873SRC 000442|    # A shift word encounters lawful one-hot adjacent pairs with both current=0
# C873SRC 000443|    # (the inactive occupation branches) and current=1 (the selected branch).
# C873SRC 000444|    # The controlled-only slice would make one TD occurrence invisible; the
# C873SRC 000445|    # complete declared macro domain activates it on current=0 columns.
# C873SRC 000446|    relevant = (2, 3, 4, 5)
# C873SRC 000447|    for deleted in range(len(fredkin)):
# C873SRC 000448|        damaged = compose_small(C714, [row for i, row in enumerate(fredkin) if i != deleted])
# C873SRC 000449|        fredkin_deletions.append(float(np.linalg.norm((damaged - fredkin_target)[:, relevant])))
# C873SRC 000450|    # Predicate compute is X on the negative control, reduced clean-Toffoli, X.
# C873SRC 000451|    predicate = [("X", (1,)), *reduced, ("X", (1,))]
# C873SRC 000452|    predicate_target = np.zeros((8, 8), dtype=complex)
# C873SRC 000453|    for source in range(8):
# C873SRC 000454|        a, b, current = source & 1, (source >> 1) & 1, (source >> 2) & 1
# C873SRC 000455|        target = source ^ ((a & (1 - b)) << 2)
# C873SRC 000456|        predicate_target[target, source] = 1
# C873SRC 000457|    predicate_deletions = []
# C873SRC 000458|    for deleted in range(len(predicate)):
# C873SRC 000459|        damaged = compose_small(C714, [row for i, row in enumerate(predicate) if i != deleted])
# C873SRC 000460|        predicate_deletions.append(float(np.linalg.norm((damaged - predicate_target)[:, clean])))
# C873SRC 000461|    # The uncompute receives current=a(1-b), so it must retain the full
# C873SRC 000462|    # 15-primitive Toffoli.  Exhaust precisely those four supplied columns.
# C873SRC 000463|    uncompute = [("X", (1,)), *full, ("X", (1,))]
# C873SRC 000464|    uncompute_columns = (0, 2, 3, 5)
# C873SRC 000465|    uncompute_deletions = []
# C873SRC 000466|    for deleted in range(len(uncompute)):
# C873SRC 000467|        damaged = compose_small(C714, [row for i, row in enumerate(uncompute) if i != deleted])
# C873SRC 000468|        uncompute_deletions.append(float(np.linalg.norm((damaged - predicate_target)[:, uncompute_columns])))
# C873SRC 000469|    return {
# C873SRC 000470|        "full_Toffoli_residual": float(np.linalg.norm(tof - tof_target)),
# C873SRC 000471|        "clean_target_reduced_Toffoli_column_residual": clean_float(float(np.linalg.norm((reduced_matrix - tof)[:, clean]))),
# C873SRC 000472|        "clean_target_reduced_Toffoli_off_domain_residual": float(np.linalg.norm(reduced_matrix - tof)),
# C873SRC 000473|        "clean_target_remaining_literal_deletion_residuals": reduced_deletions,
# C873SRC 000474|        "minimum_clean_target_literal_deletion_residual": min(reduced_deletions),
# C873SRC 000475|        "fredkin_residual": float(np.linalg.norm(fredkin_matrix - fredkin_target)),
# C873SRC 000476|        "fredkin_literal_deletion_residuals_on_onehot_controlled_columns": fredkin_deletions,
# C873SRC 000477|        "minimum_fredkin_literal_deletion_residual": min(fredkin_deletions),
# C873SRC 000478|        "predicate_compute_clean_column_residual": clean_float(float(np.linalg.norm((compose_small(C714, predicate) - predicate_target)[:, clean]))),
# C873SRC 000479|        "predicate_literal_deletion_residuals": predicate_deletions,
# C873SRC 000480|        "minimum_predicate_literal_deletion_residual": min(predicate_deletions),
