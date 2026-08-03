#!/usr/bin/env python3
"""Independent Cycle873 check of the literal F17-augmented Cycle870 seam.

This checker deliberately reads, but never imports, the Cycle873 primary or
physical core.  It reconstructs the
emitted word from the pinned landed primitives, proves the physical Pauli
compiler on arbitrary coherent inputs, and checks the effective encoded-domain
intertwiner, repeated factors, open-box local constraints, and the actual
Cycle219 one-particle recurrence/dispersion fixture.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import json
import math
import os
from pathlib import Path
import subprocess
import sys

import numpy as np


F17 = 17
TOL = 3.0e-10
EXPECTED_BASE_COMMIT = "c73a11d1ea7ddd564c48aa2a5a459a43d94262ef"
DEFAULT_ROOT = Path(__file__).resolve().parents[1]
PRIMARY_REL = Path("scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_primary_2026_08_03.py")
PRIMARY_SHA256 = "ab9f365c167b8fafb4f54508c0fb38b325bf687fdf8f222bc9aa833ad65dfc62"
PHYSICAL_CORE_REL = Path("scripts/frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py")
PHYSICAL_CORE_SHA256 = "8f0f23d86cc83c433be3e86a66e719631c70da7fbd8a1adf6b85b65815448ad7"
PHYSICAL_RECEIPT_REL = Path("outputs/cycle873_recurrent_f17_all_seam_physical_core_receipt_2026_08_03.json")
PHYSICAL_RECEIPT_SHA256 = "397657af570393fad9967edc55e74f7a66f46e8284fd5102be0f5e1df9247d0b"
DEFAULT_OUTPUT = DEFAULT_ROOT / "outputs/cycle873_recurrent_f17_uniform_affine_open_box_independent_check_receipt_2026_08_03.json"
EXPECTED_SOURCE_SHA256 = {
    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py":
        "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
    "scripts/frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02.py":
        "6645156635b4354d937759a28e71215121a19cefcc2f294a2791e6a84cf1423b",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py":
        "eb6c9a50681c69ea4fae47724c58d8ba10b48a270e7efa67a811af234afe9a1a",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py":
        "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
}

# Independently transcribed from the frozen primary declaration.  The AST
# check below separately asserts that the live declaration equals this tuple.
RAIL_LOCAL_OFFSETS = (
    (-2, 2, 0), (-2, 2, -1), (-1, 2, -1), (-1, 2, -2),
    (0, 2, -2), (1, 2, -2), (1, 1, -2), (2, 1, -2),
    (2, 0, -2), (2, -1, -2), (1, -1, -2), (1, -2, -2),
    (0, -2, -2), (-1, -2, -2), (-1, -2, -1), (-2, -2, -1),
    (-2, -2, -2),
)


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def clean_float(value: float) -> float:
    return 0.0 if abs(value) < 5.0e-15 else float(value)


def state_distance(left: dict, right: dict) -> float:
    return float(math.sqrt(sum(
        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
        for key in set(left) | set(right)
    )))


def source_ast_certificate(root: Path) -> dict:
    primary = root / PRIMARY_REL
    physical = root / PHYSICAL_CORE_REL
    tree = ast.parse(physical.read_text(encoding="utf-8"))
    imports = []
    offsets = None
    emit = None
    for node in tree.body:
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
        elif isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == "RAIL_LOCAL_OFFSETS"
                   for target in node.targets):
                offsets = ast.literal_eval(node.value)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.target.id == "RAIL_LOCAL_OFFSETS":
                offsets = ast.literal_eval(node.value)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "emit_program":
            emit = node
    if emit is None:
        raise AssertionError("primary emit_program missing")
    emitted = ast.unparse(emit)
    ordered_needles = (
        "endpoint_pre=",
        "selected_seam=",
        "positive_compute=",
        "positive_shift=",
        "positive_uncompute=",
        "negative_compute=",
        "negative_shift=",
        "negative_uncompute=",
        "endpoint_clean=",
    )
    positions = tuple(emitted.index(needle) for needle in ordered_needles)
    required_semantics = (
        "physical_b(graph, context, cell, left_mode)",
        "physical_b(graph, context, target, right_mode)",
        "compile_rotations(selected, context)",
        "shift_word(placement, alpha, 'F17_positive_shift_')",
        "shift_word(placement, -alpha, 'F17_negative_shift_')",
        "right_b, context, placement.q_u, 'F17_clean_right_B_into_q_u'",
        "left_b, context, placement.q_v, 'F17_clean_left_B_into_q_v'",
    )
    missing = tuple(row for row in required_semantics if row not in emitted)
    return {
        "primary_sha256": sha(primary),
        "physical_core_sha256": sha(physical),
        "physical_receipt_sha256": sha(root / PHYSICAL_RECEIPT_REL),
        "physical_core_imports_cycle873_primary": any(
            "frontier_cycle873_recurrent_f17_uniform_affine_open_box_primary" in row
            for row in imports
        ),
        "checker_runtime_imported_primary": any(
            "frontier_cycle873_recurrent_f17_uniform_affine_open_box_primary" in name
            for name in sys.modules
        ),
        "rail_offsets_match": tuple(offsets or ()) == RAIL_LOCAL_OFFSETS,
        "emit_field_order_match": positions == tuple(sorted(positions)),
        "emit_required_semantics_missing": missing,
        "emit_ast_sha256": sha256(ast.dump(emit, include_attributes=False).encode()).hexdigest(),
    }


def setup_imports(root: Path):
    sys.path.insert(0, str(root / "scripts"))
    import frontier_cycle870_openreference_native_recurrent_update_2026_08_02 as C870
    import frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02 as C871
    import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as C714
    import common_matter_field_coin_family_cycle219_2026_07_16 as C219
    import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as C210
    return C870, C871, C714, C219, C210


def matrix_digest(C870, matrix: np.ndarray) -> str:
    return C870.c707.c655.matrix_digest(matrix)


def signature(C870, instruction):
    return instruction.kind, instruction.sites, matrix_digest(C870, instruction.matrix)


def word_digest(C870, word) -> str:
    return sha256(repr(tuple(signature(C870, row) for row in word)).encode()).hexdigest()


def add(*rows):
    return tuple(sum(values) for values in zip(*rows))


def scale(value, row):
    return tuple(value * item for item in row)


def at(midpoint, basis, local):
    return add(midpoint, *(scale(value, direction) for value, direction in zip(local, basis)))


def local_compile(C870, rotation, context):
    """Independent literal compiler for one physical Hermitian Pauli rotation."""
    Instruction = C870.c707.Instruction
    physical = C870.physical_lift(rotation.row, context)
    axes = []
    y_count = 0
    for index, site in enumerate(context.sites):
        x = (physical.x >> index) & 1
        z = (physical.z >> index) & 1
        if x and z:
            axes.append((site, "Y")); y_count += 1
        elif x:
            axes.append((site, "X"))
        elif z:
            axes.append((site, "Z"))
    exponent = (physical.phase - y_count) % 4
    if exponent not in (0, 2) or not axes:
        raise AssertionError(("bad Hermitian physical row", physical, exponent))
    sign = 1 if exponent == 0 else -1
    H = C870.c707.c655.H
    CNOT = C870.c707.c655.CNOT
    S = np.diag((1, 1j)).astype(complex)
    SD = S.conj().T
    rz = np.diag((
        np.exp(-0.5j * sign * rotation.angle),
        np.exp(0.5j * sign * rotation.angle),
    )).astype(complex)
    pivot = axes[0][0]
    word = []
    for site, axis in axes:
        if axis == "X":
            word.append(Instruction("basis_H", (site,), H))
        elif axis == "Y":
            word.extend((Instruction("basis_Sdg", (site,), SD), Instruction("basis_H", (site,), H)))
    for site, _axis in axes[1:]:
        word.append(Instruction("parity_CNOT", (site, pivot), CNOT))
    word.append(Instruction("axis_RZ", (pivot,), rz))
    for site, _axis in reversed(axes[1:]):
        word.append(Instruction("parity_CNOT", (site, pivot), CNOT))
    for site, axis in reversed(axes):
        if axis == "X":
            word.append(Instruction("basis_H", (site,), H))
        elif axis == "Y":
            word.extend((Instruction("basis_H", (site,), H), Instruction("basis_S", (site,), S)))
    return physical, tuple(axes), tuple(word)


def apply_dense(state: np.ndarray, matrix: np.ndarray, wires: tuple[int, ...], count: int):
    wire_axes = [count - 1 - wire for wire in wires]
    local_axes = list(reversed(wire_axes))
    other = [axis for axis in range(count) if axis not in local_axes]
    order = other + local_axes
    inverse = np.argsort(order)
    tensor = state.reshape((2,) * count).transpose(order)
    flat = tensor.reshape((-1, 1 << len(wires)))
    updated = flat @ np.asarray(matrix, dtype=complex).T
    return updated.reshape(tensor.shape).transpose(inverse).reshape(-1)


def apply_pauli_dense(C870, state, row, count):
    X = C870.c707.c655.X
    Z = np.diag((1, -1)).astype(complex)
    output = state
    for wire in range(count):
        x, z = (row.x >> wire) & 1, (row.z >> wire) & 1
        if x or z:
            output = apply_dense(output, np.linalg.matrix_power(X, x) @ np.linalg.matrix_power(Z, z), (wire,), count)
    return (1j ** row.phase) * output


def restrict_pauli(C870, row, all_sites, union):
    index = {site: i for i, site in enumerate(union)}
    x = z = 0
    for source, site in enumerate(all_sites):
        if site in index:
            target = index[site]
            x |= ((row.x >> source) & 1) << target
            z |= ((row.z >> source) & 1) << target
    return C870.Pauli(row.phase, x, z)


def poly_clean(C870, poly):
    output = {}
    for row, coefficient in poly.items():
        canonical = C870.Pauli(0, row.x, row.z)
        output[canonical] = output.get(canonical, 0.0j) + (1j ** row.phase) * coefficient
    return {row: value for row, value in output.items() if abs(value) > 2e-12}


def poly_mul(C870, left, right):
    out = {}
    for a, av in left.items():
        for b, bv in right.items():
            row = a @ b
            out[row] = out.get(row, 0.0j) + av * bv
    return poly_clean(C870, out)


def poly_scale(C870, poly, scalar):
    return poly_clean(C870, {row: scalar * value for row, value in poly.items()})


def poly_add(C870, *polys):
    out = {}
    for poly in polys:
        for row, value in poly.items():
            out[row] = out.get(row, 0.0j) + value
    return poly_clean(C870, out)


def poly_residual(C870, left, right):
    keys = set(left) | set(right)
    return float(math.sqrt(sum(abs(left.get(k, 0j) - right.get(k, 0j)) ** 2 for k in keys)))


def aligned_poly_residual(C870, observed, expected):
    keys = set(observed) | set(expected)
    overlap = sum(np.conj(expected.get(k, 0j)) * observed.get(k, 0j) for k in keys)
    phase = overlap / abs(overlap) if overlap else 1 + 0j
    return poly_residual(C870, observed, poly_scale(C870, expected, phase)), phase


def physical_seam_certificate(C870, C871):
    graph = C870.prep.OpenReferenceGraph(tuple(product(range(2), repeat=3)))
    context = C870.physical_context(graph)
    seam = C870.graph_seams(graph)[0]
    rows = C871.selected_seam_rotations(graph, seam)
    physical_constraints = C870.physical_stabilizers(context)
    compiler_rows = []
    emitted = C871.compile_rotations(rows, context)
    rebuilt = []
    rng = np.random.default_rng(87017)
    execution_residuals = []
    deletion_witnesses = []
    constraint_anticommutators = 0
    row_weights = []
    compiler_match_failures = 0
    for rotation in rows:
        physical, axes, word = local_compile(C870, rotation, context)
        rebuilt.extend(word)
        row_weights.append((rotation.meta[0], (rotation.row.x | rotation.row.z).bit_count(), len(axes), len(word)))
        constraint_anticommutators += sum(not physical.commutes(s) for s in physical_constraints)
        union = tuple(site for site, _axis in axes)
        local = restrict_pauli(C870, physical, context.sites, union)
        count = len(union)
        state = rng.normal(size=1 << count) + 1j * rng.normal(size=1 << count)
        state = state.astype(complex) / np.linalg.norm(state)
        compiled = state.copy()
        local_index = {site: i for i, site in enumerate(union)}
        for instruction in word:
            wires = tuple(local_index[site] for site in instruction.sites)
            before = compiled
            after = apply_dense(before, instruction.matrix, wires, count)
            # Unitary suffixes preserve this exact full-word deletion distance.
            deletion_witnesses.append(float(np.linalg.norm(after - before)))
            compiled = after
        direct = (
            math.cos(rotation.angle / 2) * state
            - 1j * math.sin(rotation.angle / 2) * apply_pauli_dense(C870, state, local, count)
        )
        execution_residuals.append(float(np.linalg.norm(compiled - direct)))
        no_rz = state.copy()
        for instruction in word:
            if instruction.kind == "axis_RZ":
                continue
            no_rz = apply_dense(no_rz, instruction.matrix, tuple(local_index[s] for s in instruction.sites), count)
        compiler_rows.append({
            "meta": rotation.meta,
            "physical_weight": len(axes),
            "compiled_gates": len(word),
            "delete_axis_RZ_identity_residual": clean_float(float(np.linalg.norm(no_rz - state))),
            "delete_axis_RZ_action_residual_on_coherent_witness": float(np.linalg.norm(no_rz - direct)),
        })
    compiler_match_failures += tuple(signature(C870, x) for x in rebuilt) != tuple(signature(C870, x) for x in emitted)

    abstract = tuple(rotation.row for rotation in rows)
    target = poly_add(C870, *(poly_scale(C870, {row: 1 + 0j}, 0.5) for row in abstract))
    factored = {C870.Pauli(): 1 + 0j}
    rotations = []
    for row in abstract:
        rotations.append({
            C870.Pauli(): complex(math.cos(math.pi / 4)),
            row: complex(-1j * math.sin(math.pi / 4)),
        })
    for factor in rotations:
        factored = poly_mul(C870, factor, factored)
    identity = {C870.Pauli(): 1 + 0j}
    minus_identity = {C870.Pauli(): -1 + 0j}
    deletion_residuals = []
    for deleted in range(4):
        damaged = identity
        for index, factor in enumerate(rotations):
            if index != deleted:
                damaged = poly_mul(C870, factor, damaged)
        deletion_residuals.append(aligned_poly_residual(C870, damaged, target)[0])
    bu = {abstract[0]: 1 + 0j}
    bv = {abstract[1]: 1 + 0j}
    conj_u = poly_mul(C870, target, poly_mul(C870, bu, target))
    conj_v = poly_mul(C870, target, poly_mul(C870, bv, target))
    lift_homomorphism_failures = 0
    for left in abstract:
        for right in abstract:
            lift_homomorphism_failures += (
                C870.physical_lift(left @ right, context)
                != C870.physical_lift(left, context) @ C870.physical_lift(right, context)
            )
    return {
        "seam": seam,
        "physical_carrier_M2": len(context.sites),
        "rows": row_weights,
        "compiled_gate_count": len(rebuilt),
        "compiler_signature_match_failures": compiler_match_failures,
        "maximum_arbitrary_coherent_full_support_compiler_residual": max(execution_residuals),
        "minimum_literal_compiler_gate_deletion_witness_residual_full_support": min(deletion_witnesses),
        "inactive_literal_compiler_gate_deletions_on_coherent_witness": sum(x <= TOL for x in deletion_witnesses),
        "compiler_factor_rows": compiler_rows,
        "physical_constraint_anticommutators": constraint_anticommutators,
        "physical_lift_pair_homomorphism_failures": lift_homomorphism_failures,
        "raw_to_minus_i_FSWAP_residual": clean_float(poly_residual(C870, factored, poly_scale(C870, target, -1j))),
        "raw_to_literal_FSWAP_residual": poly_residual(C870, factored, target),
        "formal_i_corrected_to_FSWAP_residual": clean_float(poly_residual(C870, poly_scale(C870, factored, 1j), target)),
        "raw_square_to_minus_identity_residual": clean_float(poly_residual(C870, poly_mul(C870, factored, factored), minus_identity)),
        "target_square_to_identity_residual": clean_float(poly_residual(C870, poly_mul(C870, target, target), identity)),
        "occupation_conjugation_residuals": (
            clean_float(poly_residual(C870, conj_u, bv)),
            clean_float(poly_residual(C870, conj_v, bu)),
        ),
        "four_rotation_deletion_residuals_up_to_global_phase": deletion_residuals,
    }


def compose_small(C714, gates, qubits=3):
    mats = {"H": C714.H, "T": C714.T, "TD": C714.TD, "CNOT": C714.CNOT, "X": C714.X}
    output = np.eye(1 << qubits, dtype=complex)
    for kind, wires in gates:
        output = np.column_stack([
            C714.apply_small(output[:, column], mats[kind], wires, qubits)
            for column in range(1 << qubits)
        ])
    return output


def reversible_primitive_certificate(C714):
    full = list(C714.toffoli_primitives(0, 1, 2))
    reduced = [row for index, row in enumerate(full) if index != 1]
    tof = compose_small(C714, full)
    tof_target = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        tof_target[source ^ (((source & 1) & ((source >> 1) & 1)) << 2), source] = 1
    reduced_matrix = compose_small(C714, reduced)
    clean = tuple(range(4))
    reduced_deletions = []
    for deleted in range(len(reduced)):
        damaged = compose_small(C714, [row for i, row in enumerate(reduced) if i != deleted])
        reduced_deletions.append(float(np.linalg.norm((damaged - tof)[:, clean])))
    fredkin = [("CNOT", (1, 2)), *C714.toffoli_primitives(0, 2, 1), ("CNOT", (1, 2))]
    fredkin_matrix = compose_small(C714, fredkin)
    fredkin_target = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        c, left, right = source & 1, (source >> 1) & 1, (source >> 2) & 1
        target = source if not c else ((source & ~6) | (right << 1) | (left << 2))
        fredkin_target[target, source] = 1
    fredkin_deletions = []
    # A shift word encounters lawful one-hot adjacent pairs with both current=0
    # (the inactive occupation branches) and current=1 (the selected branch).
    # The controlled-only slice would make one TD occurrence invisible; the
    # complete declared macro domain activates it on current=0 columns.
    relevant = (2, 3, 4, 5)
    for deleted in range(len(fredkin)):
        damaged = compose_small(C714, [row for i, row in enumerate(fredkin) if i != deleted])
        fredkin_deletions.append(float(np.linalg.norm((damaged - fredkin_target)[:, relevant])))
    # Predicate compute is X on the negative control, reduced clean-Toffoli, X.
    predicate = [("X", (1,)), *reduced, ("X", (1,))]
    predicate_target = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        a, b, current = source & 1, (source >> 1) & 1, (source >> 2) & 1
        target = source ^ ((a & (1 - b)) << 2)
        predicate_target[target, source] = 1
    predicate_deletions = []
    for deleted in range(len(predicate)):
        damaged = compose_small(C714, [row for i, row in enumerate(predicate) if i != deleted])
        predicate_deletions.append(float(np.linalg.norm((damaged - predicate_target)[:, clean])))
    # The uncompute receives current=a(1-b), so it must retain the full
    # 15-primitive Toffoli.  Exhaust precisely those four supplied columns.
    uncompute = [("X", (1,)), *full, ("X", (1,))]
    uncompute_columns = (0, 2, 3, 5)
    uncompute_deletions = []
    for deleted in range(len(uncompute)):
        damaged = compose_small(C714, [row for i, row in enumerate(uncompute) if i != deleted])
        uncompute_deletions.append(float(np.linalg.norm((damaged - predicate_target)[:, uncompute_columns])))
    return {
        "full_Toffoli_residual": float(np.linalg.norm(tof - tof_target)),
        "clean_target_reduced_Toffoli_column_residual": clean_float(float(np.linalg.norm((reduced_matrix - tof)[:, clean]))),
        "clean_target_reduced_Toffoli_off_domain_residual": float(np.linalg.norm(reduced_matrix - tof)),
        "clean_target_remaining_literal_deletion_residuals": reduced_deletions,
        "minimum_clean_target_literal_deletion_residual": min(reduced_deletions),
        "fredkin_residual": float(np.linalg.norm(fredkin_matrix - fredkin_target)),
        "fredkin_literal_deletion_residuals_on_onehot_controlled_columns": fredkin_deletions,
        "minimum_fredkin_literal_deletion_residual": min(fredkin_deletions),
        "predicate_compute_clean_column_residual": clean_float(float(np.linalg.norm((compose_small(C714, predicate) - predicate_target)[:, clean]))),
        "predicate_literal_deletion_residuals": predicate_deletions,
        "minimum_predicate_literal_deletion_residual": min(predicate_deletions),
        "predicate_uncompute_supplied_column_residual": float(np.linalg.norm((compose_small(C714, uncompute) - predicate_target)[:, uncompute_columns])),
        "uncompute_literal_deletion_residuals": uncompute_deletions,
        "minimum_uncompute_literal_deletion_residual": min(uncompute_deletions),
    }


def extraction_certificate(C870, C871):
    graph = C870.prep.OpenReferenceGraph(tuple(product(range(2), repeat=3)))
    context = C870.physical_context(graph)
    seam = C870.graph_seams(graph)[0]
    rows = []
    for cell, mode in ((seam[0], seam[3]), (seam[2], seam[4])):
        logical = graph.B(graph.vertex_index[(cell, mode)])
        physical = C870.physical_lift(logical, context)
        support = tuple(site for index, site in enumerate(context.sites) if (physical.z >> index) & 1)
        failures = 0
        deletion_changes = []
        for bits in range(1 << (len(support) + 1)):
            carrier = bits & ((1 << len(support)) - 1)
            target = (bits >> len(support)) & 1
            expected = target ^ (carrier.bit_count() & 1)
            observed = target
            for index in range(len(support)):
                observed ^= (carrier >> index) & 1
            failures += observed != expected
        for deleted in range(len(support)):
            changed = 0
            for bits in range(1 << (len(support) + 1)):
                carrier = bits & ((1 << len(support)) - 1)
                target = (bits >> len(support)) & 1
                expected = target ^ (carrier.bit_count() & 1)
                observed = target
                for index in range(len(support)):
                    if index != deleted:
                        observed ^= (carrier >> index) & 1
                changed += observed != expected
            deletion_changes.append(changed)
        rows.append({
            "cell": cell, "mode": mode, "physical_Z_weight": len(support),
            "basis_columns": 1 << (len(support) + 1), "parity_failures": failures,
            "single_CNOT_deletion_changed_full_carrier_columns": deletion_changes,
        })
    return {"endpoint_rows": rows}


def semantic_rows(alpha, mutation=None):
    rows = [
        ("pre_u", ("CNOT", 0, 2)), ("pre_v", ("CNOT", 1, 3)),
        ("seam", ("FSWAP",)),
        ("plus_x1", ("X", 3)), ("plus_tof", ("TOF", 2, 3, 4)), ("plus_x2", ("X", 3)),
        ("plus_shift", ("SHIFT", alpha)),
        ("plus_ux1", ("X", 3)), ("plus_utof", ("TOF", 2, 3, 4)), ("plus_ux2", ("X", 3)),
        ("minus_x1", ("X", 2)), ("minus_tof", ("TOF", 2, 3, 4)), ("minus_x2", ("X", 2)),
        ("minus_shift", ("SHIFT", -alpha)),
        ("minus_ux1", ("X", 2)), ("minus_utof", ("TOF", 2, 3, 4)), ("minus_ux2", ("X", 2)),
        ("clean_u", ("CNOT", 1, 2)), ("clean_v", ("CNOT", 0, 3)),
    ]
    omissions = {
        "delete_pre_u": {"pre_u"}, "delete_pre_v": {"pre_v"},
        "delete_seam": {"seam"}, "delete_plus_shift": {"plus_shift"},
        "delete_minus_shift": {"minus_shift"}, "delete_cleanup": {"clean_u", "clean_v"},
    }.get(mutation, set())
    return tuple(row for name, row in rows if name not in omissions)


def semantic_apply(state, operation, raw=False):
    out = {}
    for key, amplitude in state.items():
        bits = list(key[:5]); label = key[5]; phase = 1 + 0j
        kind = operation[0]
        if kind == "X": bits[operation[1]] ^= 1
        elif kind == "CNOT": bits[operation[2]] ^= bits[operation[1]]
        elif kind == "TOF": bits[operation[3]] ^= bits[operation[1]] & bits[operation[2]]
        elif kind == "SHIFT":
            if bits[4]: label = (label + operation[1]) % F17
        elif kind == "FSWAP":
            if bits[0] == bits[1] == 1: phase *= -1
            bits[0], bits[1] = bits[1], bits[0]
            if raw: phase *= -1j
        else: raise AssertionError(operation)
        target = (*bits, label)
        out[target] = out.get(target, 0j) + phase * amplitude
    return out


def semantic_execute(state, rows, raw=False):
    for row in rows:
        state = semantic_apply(state, row, raw=raw)
    return state


def augmented_target(a, b, label, alpha):
    phase = -1 if a == b == 1 else 1
    return {(b, a, 0, 0, 0, (label + alpha * (a - b)) % F17): complex(phase)}


def effective_macro_certificate():
    output = []
    rng = np.random.default_rng(170870)
    for alpha in (-1, 1):
        formal_max = raw_max = 0.0
        coherent = {}; coherent_target = {}
        amplitudes = rng.normal(size=4 * F17) + 1j * rng.normal(size=4 * F17)
        amplitudes /= np.linalg.norm(amplitudes)
        column = 0
        cleanup = inverse = 0
        for a, b in product((0, 1), repeat=2):
            for label in range(F17):
                initial = {(a, b, 0, 0, 0, label): 1 + 0j}
                target = augmented_target(a, b, label, alpha)
                raw = semantic_execute(initial, semantic_rows(alpha), raw=True)
                corrected = {key: 1j * value for key, value in raw.items()}
                formal_max = max(formal_max, state_distance(corrected, target))
                raw_max = max(raw_max, state_distance(raw, target))
                cleanup += any(key[2] or key[3] or key[4] for key in raw)
                amp = amplitudes[column]; column += 1
                coherent.update({next(iter(initial)): amp})
                key, value = next(iter(target.items()))
                coherent_target[key] = coherent_target.get(key, 0j) + amp * value
        coherent_raw = semantic_execute(coherent, semantic_rows(alpha), raw=True)
        coherent_corrected = {key: 1j * value for key, value in coherent_raw.items()}
        mutations = {}
        for mutation in ("delete_pre_u", "delete_pre_v", "delete_seam", "delete_plus_shift", "delete_minus_shift", "delete_cleanup"):
            changed = dirty = 0
            for a, b in product((0, 1), repeat=2):
                for label in range(F17):
                    initial = {(a, b, 0, 0, 0, label): 1 + 0j}
                    observed = semantic_execute(initial, semantic_rows(alpha, mutation), raw=False)
                    changed += state_distance(observed, augmented_target(a, b, label, alpha)) > TOL
                    dirty += any(key[2] or key[3] or key[4] for key in observed)
            mutations[mutation] = {"changed_columns": changed, "dirty_columns": dirty}
        output.append({
            "alpha": alpha, "encoded_columns": 68,
            "formal_corrected_basis_max_residual": clean_float(formal_max),
            "raw_basis_max_residual": raw_max,
            "raw_normalized_coherent_residual": state_distance(coherent_raw, coherent_target),
            "formal_corrected_arbitrary_coherent_residual": clean_float(state_distance(coherent_corrected, coherent_target)),
            "scratch_cleanup_failures": cleanup,
            "component_mutations": mutations,
        })
    # Every omitted adjacent Fredkin changes precisely its two endpoint labels.
    fredkin_deletions = {}
    for direction in (-1, 1):
        order = range(15, -1, -1) if direction > 0 else range(16)
        for omitted in range(16):
            changed = 0
            for label in range(F17):
                full = 1 << label; damaged = full
                for edge in order:
                    if ((full >> edge) & 1) != ((full >> (edge + 1)) & 1):
                        full ^= (1 << edge) | (1 << (edge + 1))
                    if edge != omitted and ((damaged >> edge) & 1) != ((damaged >> (edge + 1)) & 1):
                        damaged ^= (1 << edge) | (1 << (edge + 1))
                changed += full != damaged
            fredkin_deletions[f"{direction:+d}:{omitted}"] = changed
    return {"families": output, "deleted_Fredkin_changed_onehot_rows": fredkin_deletions}


def local_instruction(C870, kind, sites, matrix):
    return C870.c707.Instruction(kind, tuple(sites), matrix)


def independent_emitted_word(C870, C871, C714, graph, context, seam, alpha=1):
    packet = C871.packet_placement(graph, context, seam)
    rails = tuple(at(packet.midpoint, packet.basis, row) for row in RAIL_LOCAL_OFFSETS)
    qu, qv, current = (packet.sites[C714.MCX_WORK[i]] for i in range(3))
    cell, _axis, target, left_mode, right_mode = seam
    left = C870.physical_lift(graph.B(graph.vertex_index[(cell, left_mode)]), context)
    right = C870.physical_lift(graph.B(graph.vertex_index[(target, right_mode)]), context)

    def zsupport(row):
        return tuple(site for index, site in enumerate(context.sites) if (row.z >> index) & 1)

    def cnot(a, b, kind): return local_instruction(C870, kind, (a, b), C714.CNOT)
    def x(site, kind): return local_instruction(C870, kind, (site,), C714.X)
    def primitive(a, b, t, prefix, clean=False):
        source = list(C714.toffoli_primitives(0, 1, 2))
        if clean: del source[1]
        mats = {"H": C714.H, "T": C714.T, "TD": C714.TD, "CNOT": C714.CNOT}
        sites = (a, b, t)
        return tuple(local_instruction(C870, prefix + kind, tuple(sites[i] for i in wires), mats[kind]) for kind, wires in source)
    def predicate(sign, prefix, clean):
        negative = qv if sign > 0 else qu
        return (x(negative, prefix + "negative_X"),) + primitive(qu, qv, current, prefix + ("clean_target_Toffoli_" if clean else "Toffoli_"), clean=clean) + (x(negative, prefix + "negative_X"),)
    def fredkin(left_rail, right_rail, prefix):
        return (cnot(left_rail, right_rail, prefix + "outer_CNOT"),) + primitive(current, right_rail, left_rail, prefix + "Toffoli_") + (cnot(left_rail, right_rail, prefix + "outer_CNOT"),)
    def shift(direction, prefix):
        order = range(15, -1, -1) if direction > 0 else range(16)
        return tuple(g for edge in order for g in fredkin(rails[edge], rails[edge + 1], f"{prefix}{edge}_"))

    endpoint_pre = tuple(cnot(site, qu, "F17_pre_left_B") for site in zsupport(left)) + tuple(cnot(site, qv, "F17_pre_right_B") for site in zsupport(right))
    selected = []
    for rotation in C871.selected_seam_rotations(graph, seam):
        _physical, _axes, word = local_compile(C870, rotation, context)
        selected.extend(word)
    branch = (
        predicate(1, "F17_positive_compute_", True)
        + shift(alpha, "F17_positive_shift_")
        + predicate(1, "F17_positive_uncompute_", False)
        + predicate(-1, "F17_negative_compute_", True)
        + shift(-alpha, "F17_negative_shift_")
        + predicate(-1, "F17_negative_uncompute_", False)
    )
    cleanup = tuple(cnot(site, qu, "F17_clean_right_B_into_q_u") for site in zsupport(right)) + tuple(cnot(site, qv, "F17_clean_left_B_into_q_v") for site in zsupport(left))
    return endpoint_pre + tuple(selected) + branch + cleanup, packet.basis


def coframe_path(left, right, basis):
    delta = tuple(b - a for a, b in zip(left, right))
    coefficients = tuple(sum(delta[i] * direction[i] for i in range(3)) for direction in basis)
    current = left; path = [left]
    for coefficient, direction in zip(coefficients, basis):
        step = direction if coefficient >= 0 else scale(-1, direction)
        for _ in range(abs(coefficient)):
            current = add(current, step); path.append(current)
    if current != right: raise AssertionError((left, right, current))
    return tuple(path)


def route_digest(C870, word, basis):
    digest = sha256(); routed = 0
    for instruction in word:
        if len(instruction.sites) == 1:
            routed += 1
            digest.update(repr(signature(C870, instruction)).encode())
        else:
            path = coframe_path(*instruction.sites, basis)
            routed += 2 * (len(path) - 1) - 1
            digest.update((instruction.kind + repr(path) + matrix_digest(C870, instruction.matrix)).encode())
    return digest.hexdigest(), routed


def schedule_color(seam):
    cell, axis = seam[0], seam[1]
    return axis, cell[0] & 1, cell[1] & 1, cell[2] & 1


def schedule_key(color):
    axis, x, y, z = color; values = (x, y, z)
    return axis, values[axis], values[(axis + 1) % 3], values[(axis + 2) % 3]


def emitted_schedule_certificate(root, C870, C871, C714):
    graph = C870.prep.OpenReferenceGraph(tuple(product(range(2), repeat=3)))
    context = C870.physical_context(graph)
    constraints = C870.physical_stabilizers(context)
    groups = defaultdict(list)
    logical_counts = []; routed_counts = []; word_hashes = []
    row_anticommutators = endpoint_anticommutators = 0
    maximum_raw_minus_i_residual = maximum_corrected_residual = 0.0
    for seam in C870.graph_seams(graph):
        word, basis = independent_emitted_word(C870, C871, C714, graph, context, seam)
        wd = word_digest(C870, word); rd, routed = route_digest(C870, word, basis)
        row = (seam, wd, rd)
        groups[schedule_color(seam)].append(row)
        logical_counts.append(len(word)); routed_counts.append(routed); word_hashes.append(wd)
        rotations = C871.selected_seam_rotations(graph, seam)
        abstract = tuple(rotation.row for rotation in rotations)
        target = poly_add(C870, *(poly_scale(C870, {pauli: 1 + 0j}, 0.5) for pauli in abstract))
        factored = {C870.Pauli(): 1 + 0j}
        for pauli in abstract:
            factor = {
                C870.Pauli(): complex(math.cos(math.pi / 4)),
                pauli: complex(-1j * math.sin(math.pi / 4)),
            }
            factored = poly_mul(C870, factor, factored)
        maximum_raw_minus_i_residual = max(
            maximum_raw_minus_i_residual,
            poly_residual(C870, factored, poly_scale(C870, target, -1j)),
        )
        maximum_corrected_residual = max(
            maximum_corrected_residual,
            poly_residual(C870, poly_scale(C870, factored, 1j), target),
        )
        for rotation in rotations:
            physical = C870.physical_lift(rotation.row, context)
            row_anticommutators += sum(not physical.commutes(stabilizer) for stabilizer in constraints)
        for cell, mode in ((seam[0], seam[3]), (seam[2], seam[4])):
            physical_b = C870.physical_lift(graph.B(graph.vertex_index[(cell, mode)]), context)
            endpoint_anticommutators += sum(not physical_b.commutes(stabilizer) for stabilizer in constraints)
    ordered = tuple(sorted(groups, key=schedule_key))
    schedule = tuple(
        (color, tuple((seam, wd, rd) for seam, wd, rd in sorted(groups[color], key=lambda item: item[0][0])))
        for color in ordered
    )
    digest = sha256(repr(schedule).encode()).hexdigest()
    receipt = json.loads((root / PHYSICAL_RECEIPT_REL).read_text())
    expected = receipt["fixtures"][0]["augmented_epoch_ledgers"]["A_F17_only"]["seam_stage_schedule_sha256"]
    return {
        "shape": (2, 2, 2), "seams": len(logical_counts),
        "schedule_sha256": digest, "physical_core_F17_only_schedule_sha256": expected,
        "schedule_hash_match": digest == expected,
        "total_logical_instructions": sum(logical_counts),
        "logical_min_max": (min(logical_counts), max(logical_counts)),
        "total_routed_gates": sum(routed_counts),
        "routed_min_max": (min(routed_counts), max(routed_counts)),
        "independent_word_sha256": word_hashes,
        "all_seam_rotation_physical_constraint_anticommutators": row_anticommutators,
        "all_endpoint_B_physical_constraint_anticommutators": endpoint_anticommutators,
        "all_seam_maximum_raw_to_minus_i_FSWAP_residual": clean_float(maximum_raw_minus_i_residual),
        "all_seam_maximum_formal_corrected_residual": clean_float(maximum_corrected_residual),
    }


def rref_mod(matrix, p=F17):
    a = np.asarray(matrix, dtype=np.int64).copy() % p; row = 0; pivots = []
    for col in range(a.shape[1]):
        pivot = next((r for r in range(row, a.shape[0]) if a[r, col] % p), None)
        if pivot is None: continue
        a[[row, pivot]] = a[[pivot, row]]
        a[row] = a[row] * pow(int(a[row, col]), -1, p) % p
        for r in range(a.shape[0]):
            if r != row and a[r, col]: a[r] = (a[r] - int(a[r, col]) * a[row]) % p
        pivots.append(col); row += 1
        if row == a.shape[0]: break
    return a, pivots


def solve_mod(matrix, rhs, p=F17):
    a = np.asarray(matrix, dtype=np.int64) % p
    aug, pivots = rref_mod(np.column_stack((a, np.asarray(rhs, dtype=np.int64) % p)), p)
    x = np.zeros(a.shape[1], dtype=np.int64)
    for r, pivot in enumerate(q for q in pivots if q < a.shape[1]): x[pivot] = aug[r, -1]
    if not np.array_equal(a @ x % p, np.asarray(rhs) % p): raise AssertionError("inconsistent")
    return x


@dataclass(frozen=True)
class Complex:
    vertices: tuple
    edges: tuple
    incidence: np.ndarray
    faces: np.ndarray


@dataclass(frozen=True)
class FixedStarBackground:
    label: str
    particle_number: int
    field: tuple[int, ...]


def open_box(dims):
    vertices = tuple(product(*(range(n) for n in dims))); index = {v: i for i, v in enumerate(vertices)}
    edges = []; lookup = {}
    for vertex in vertices:
        for axis in range(3):
            if vertex[axis] + 1 < dims[axis]:
                target = list(vertex); target[axis] += 1; target = tuple(target)
                lookup[(vertex, target)] = len(edges); edges.append((index[vertex], index[target], axis))
    incidence = np.zeros((len(vertices), len(edges)), dtype=np.int64)
    for e, (u, v, _axis) in enumerate(edges): incidence[u, e] = -1; incidence[v, e] = 1
    faces = []
    for a in range(3):
        for b in range(a + 1, 3):
            for base in vertices:
                if base[a] + 1 >= dims[a] or base[b] + 1 >= dims[b]: continue
                ea = tuple(int(i == a) for i in range(3)); eb = tuple(int(i == b) for i in range(3))
                va = add(base, ea); vb = add(base, eb); vab = add(base, ea, eb)
                row = np.zeros(len(edges), dtype=np.int64)
                row[lookup[(base, va)]] += 1; row[lookup[(va, vab)]] += 1
                row[lookup[(vb, vab)]] -= 1; row[lookup[(base, vb)]] -= 1
                faces.append(row % F17)
    return Complex(vertices, tuple(edges), incidence % F17, np.asarray(faces, dtype=np.int64).T if faces else np.zeros((len(edges), 0), int))


def nullspace_mod(matrix):
    a, pivots = rref_mod(matrix); free = [c for c in range(a.shape[1]) if c not in pivots]; rows = []
    for f in free:
        x = np.zeros(a.shape[1], dtype=np.int64); x[f] = 1
        for r, pivot in enumerate(pivots): x[pivot] = -a[r, f] % F17
        rows.append(x)
    return np.asarray(rows, dtype=np.int64).T if rows else np.zeros((a.shape[1], 0), int)


def rank_mod(matrix):
    return len(rref_mod(matrix)[1])


def edge_rails(graph: Complex, edge_index: int):
    tail_index, _head_index, axis = graph.edges[edge_index]
    tail = graph.vertices[tail_index]
    unit = tuple(int(index == axis) for index in range(3))
    basis = (
        unit,
        tuple(int(index == (axis + 1) % 3) for index in range(3)),
        tuple(int(index == (axis + 2) % 3) for index in range(3)),
    )
    midpoint = add(scale(16, tail), scale(8, unit))
    return tuple(at(midpoint, basis, offset) for offset in RAIL_LOCAL_OFFSETS), midpoint


def shifted_label(label: int, direction: int, omitted: int | None = None):
    position = label
    order = tuple(range(15, -1, -1) if direction > 0 else range(16))
    for step, left in enumerate(order):
        if step == omitted:
            continue
        right = left + 1
        if position == left:
            position = right
        elif position == right:
            position = left
    return position


def local_constraint_certificate(C870, C871):
    rows = []
    deletion_tests = deletion_undetected = 0
    for dims in ((2, 2, 2), (3, 3, 3), (3, 2, 2)):
        graph = open_box(dims)
        incidence_rank = rank_mod(graph.incidence)
        face_rank = rank_mod(graph.faces)
        cycle_rank = len(graph.edges) - incidence_rank
        boundary_squared = int(np.count_nonzero(graph.incidence @ graph.faces % F17))
        rails = {edge: edge_rails(graph, edge)[0] for edge in range(len(graph.edges))}
        onehot_path_failures = sum(
            sum(sum(abs(a - b) for a, b in zip(left, right)) != 1
                for left, right in zip(bank, bank[1:]))
            for bank in rails.values()
        )
        rail_overlap_sites = sum(
            len(set(bank) & set(rails[prior]))
            for edge, bank in rails.items() for prior in range(edge)
        )
        plaquette_word_failures = layer_collisions = 0
        plaquette_support_max = 0
        for face_index in range(graph.faces.shape[1]):
            column = graph.faces[:, face_index]
            boundary = tuple(
                (edge, 1 if int(column[edge]) == 1 else -1)
                for edge in range(len(graph.edges)) if int(column[edge])
            )
            plaquette_word_failures += len(boundary) != 4
            support = set().union(*(set(rails[edge]) for edge, _ in boundary))
            plaquette_support_max = max(plaquette_support_max, len(support))
            plaquette_word_failures += len(support) != 68
            for step in range(16):
                sites = []
                for edge, direction in boundary:
                    left_index = (15 - step) if direction > 0 else step
                    pair = (rails[edge][left_index], rails[edge][left_index + 1])
                    plaquette_word_failures += (
                        sum(abs(a - b) for a, b in zip(*pair)) != 1
                    )
                    sites.extend(pair)
                layer_collisions += len(sites) != len(set(sites))
            for _edge, direction in boundary:
                full = tuple((label + direction) % F17 for label in range(F17))
                for omitted in range(16):
                    damaged = tuple(
                        shifted_label(label, direction, omitted)
                        for label in range(F17)
                    )
                    deletion_tests += 1
                    deletion_undetected += damaged == full

        physical_graph = C870.prep.OpenReferenceGraph(graph.vertices)
        context = C870.physical_context(physical_graph)
        auxiliary = C871.J870.auxiliary_registers(physical_graph)
        carriers_aux = set(context.sites) | set(auxiliary)
        rail_carrier_aux_collisions = sum(
            len(set(bank) & carriers_aux) for bank in rails.values()
        )
        star_support_max = 0
        for cell_index, cell in enumerate(graph.vertices):
            matter = set()
            for mode in range(6):
                matter.update(C871.z_support(
                    C871.physical_b(physical_graph, context, cell, mode), context
                ))
            incident = tuple(
                edge for edge, (tail, head, _axis) in enumerate(graph.edges)
                if tail == cell_index or head == cell_index
            )
            support = matter | set().union(*(set(rails[edge]) for edge in incident))
            star_support_max = max(star_support_max, len(support))

        rows.append({
            "shape": dims,
            "vertices": len(graph.vertices),
            "oriented_links": len(graph.edges),
            "plaquettes": graph.faces.shape[1],
            "incidence_rank_mod17": incidence_rank,
            "cycle_space_rank": cycle_rank,
            "plaquette_boundary_rank_mod17": face_rank,
            "plaquette_dependency_count": graph.faces.shape[1] - face_rank,
            "boundary_of_boundary_nonzero_entries": boundary_squared,
            "fixed_divergence_dimension": F17 ** cycle_rank,
            "uniform_plus_one_dimension": F17 ** (cycle_rank - face_rank),
            "onehot_path_failures": onehot_path_failures,
            "rail_pair_overlap_sites": rail_overlap_sites,
            "rail_carrier_aux_collision_sites": rail_carrier_aux_collisions,
            "plaquette_support_M2": plaquette_support_max,
            "plaquette_word_or_NN_failures": plaquette_word_failures,
            "plaquette_layer_collisions": layer_collisions,
            "maximum_star_support_M2": star_support_max,
        })
    frames = C871.proper_frames()
    return {
        "fixtures": rows,
        "proper_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "plaquette_SWAP_deletions_tested": deletion_tests,
        "undetected_plaquette_SWAP_deletions": deletion_undetected,
        "characterization_boundary": (
            "one-hot/star/plaquette ranks and emitted sparse shifts characterize a "
            "preserved code space; autonomous preparation/enforcement is not tested"
        ),
    }


def supplied_background(graph, particle_number, convention="ordered_prefix"):
    field = np.zeros(len(graph.vertices), dtype=np.int64)
    if convention == "ordered_prefix":
        field[:particle_number] = -1
    elif convention == "first_anchor":
        field[0] = -particle_number
    elif convention == "last_anchor":
        field[-1] = -particle_number
    else:
        raise ValueError(convention)
    field %= F17
    if int(field.sum()) % F17 != (-particle_number) % F17:
        raise AssertionError("background compatibility")
    return FixedStarBackground(
        convention, particle_number, tuple(map(int, field))
    )


def matter_q(graph, bits, background):
    n = np.array([(bits >> i) & 1 for i in range(len(graph.vertices))], dtype=np.int64)
    if int(n.sum()) != background.particle_number:
        raise AssertionError("fixed-number background")
    q = (n + np.asarray(background.field, dtype=np.int64)) % F17
    if int(q.sum()) % F17:
        raise AssertionError("nonzero total Gauss word")
    return q


def affine_state(graph, bits, generators, background):
    base = solve_mod(
        graph.incidence, matter_q(graph, bits, background)
    ); beta = generators.shape[1]
    amp = 1 / math.sqrt(F17 ** beta); out = {}
    for coeff in product(range(F17), repeat=beta):
        link = (base + generators @ np.asarray(coeff, dtype=np.int64)) % F17
        out[(bits, tuple(map(int, link)))] = amp
    return out


def six_mode_count_certificate():
    rows = incidence_failures = star_failures = range_failures = 0
    minus_rows = sign_failures = 0
    wrong_sign_controls = omitted_shift_controls = 0
    for a, b, spectator_u, spectator_v, ell in product(
        (0, 1), (0, 1), range(6), range(6), range(F17)
    ):
        rows += 1
        n_u, n_v = a + spectator_u, b + spectator_v
        out_u, out_v = n_u - a + b, n_v - b + a
        current = a - b
        out_ell = (ell + current) % F17
        incidence_failures += (
            ((-current) % F17, current % F17)
            != ((out_u - n_u) % F17, (out_v - n_v) % F17)
        )
        before_g = ((-ell - n_u) % F17, (ell - n_v) % F17)
        after_g = (
            (-out_ell - out_u) % F17,
            (out_ell - out_v) % F17,
        )
        star_failures += before_g != after_g
        range_failures += not all(
            0 <= value <= 6 for value in (n_u, n_v, out_u, out_v)
        )
        sign = -1 if (a, b) == (1, 1) else 1
        minus_rows += sign == -1
        sign_failures += sign != (-1 if a == b == 1 else 1)
        if a != b:
            wrong_sign_controls += (
                (current % F17, (-current) % F17)
                != ((out_u - n_u) % F17, (out_v - n_v) % F17)
            )
            omitted_shift_controls += before_g != (
                (-ell - out_u) % F17,
                (ell - out_v) % F17,
            )
    return {
        "rows": rows,
        "alpha_normalization": "+1",
        "FSWAP_minus_11_rows": minus_rows,
        "incidence_failures": incidence_failures,
        "fixed_background_or_star_invariance_failures": star_failures,
        "occupation_range_failures": range_failures,
        "FSWAP_sign_failures": sign_failures,
        "wrong_incidence_sign_detected_rows": wrong_sign_controls,
        "omitted_link_shift_detected_rows": omitted_shift_controls,
        "notation": (
            "a,b are selected seam bits; n_u=a+s_u and n_v=b+s_v are "
            "total six-mode occupations with s_u,s_v in 0..5; this is the "
            "alpha=+1 global affine normalization and does not instantiate an "
            "alpha=-1 global encoder"
        ),
    }


def augmented_edge(graph, state, edge, raw=False):
    u, v, _axis = graph.edges[edge]; out = {}
    for (bits, link_tuple), amp in state.items():
        a, b = (bits >> u) & 1, (bits >> v) & 1; moved = bits; phase = 1
        if a != b: moved ^= (1 << u) | (1 << v)
        if a == b == 1: phase = -1
        link = list(link_tuple); link[edge] = (link[edge] + a - b) % F17
        scalar = -1j if raw else 1
        key = (moved, tuple(link)); out[key] = out.get(key, 0j) + scalar * phase * amp
    return out


def repeated_factor_certificate():
    plaquette = open_box((2, 2, 1)); cube = open_box((2, 2, 2))
    pgen = nullspace_mod(plaquette.incidence)
    direct = []; raw_direct = []; background_residuals = []
    for bits in range(1 << len(plaquette.vertices)):
        backgrounds = tuple(
            supplied_background(plaquette, bits.bit_count(), convention)
            for convention in ("ordered_prefix", "first_anchor", "last_anchor")
        )
        for edge in range(len(plaquette.edges)):
            background = backgrounds[0]
            initial = affine_state(plaquette, bits, pgen, background)
            observed = augmented_edge(plaquette, initial, edge)
            u, v, _ = plaquette.edges[edge]; moved = bits
            if ((bits >> u) & 1) != ((bits >> v) & 1): moved ^= (1 << u) | (1 << v)
            phase = -1 if ((bits >> u) & 1) == ((bits >> v) & 1) == 1 else 1
            expected = {
                key: phase * amp
                for key, amp in affine_state(
                    plaquette, moved, pgen, background
                ).items()
            }
            direct.append(state_distance(observed, expected))
            raw_direct.append(state_distance(augmented_edge(plaquette, initial, edge, raw=True), expected))
            for variant in backgrounds:
                variant_initial = affine_state(plaquette, bits, pgen, variant)
                variant_expected = {
                    key: phase * amp
                    for key, amp in affine_state(
                        plaquette, moved, pgen, variant
                    ).items()
                }
                background_residuals.append(state_distance(
                    augmented_edge(plaquette, variant_initial, edge),
                    variant_expected,
                ))
    edge_lookup = {(plaquette.vertices[u], plaquette.vertices[v]): e for e, (u, v, _) in enumerate(plaquette.edges)}
    v00, v10, v01, v11 = (0,0,0), (1,0,0), (0,1,0), (1,1,0)
    sequence = (edge_lookup[(v00,v10)], edge_lookup[(v10,v11)], edge_lookup[(v01,v11)], edge_lookup[(v00,v01)])
    repeated = []; repeated_raw = []
    for bits in range(1 << len(plaquette.vertices)):
        background = supplied_background(plaquette, bits.bit_count())
        initial = affine_state(plaquette, bits, pgen, background); observed = initial; raw = initial; moved = bits; phase = 1
        for edge in sequence:
            u, v, _ = plaquette.edges[edge]; a, b = (moved >> u) & 1, (moved >> v) & 1
            if a != b: moved ^= (1 << u) | (1 << v)
            if a == b == 1: phase *= -1
            observed = augmented_edge(plaquette, observed, edge); raw = augmented_edge(plaquette, raw, edge, raw=True)
        expected = {
            key: phase * amp
            for key, amp in affine_state(
                plaquette, moved, pgen, background
            ).items()
        }
        repeated.append(state_distance(observed, expected)); repeated_raw.append(state_distance(raw, expected))
    # Exhaust the L2 local incidence law and 36-factor recurrence algebraically.
    direct_l2 = incidence_failures = repeat_failures = 0; raw_phase = (-1j) ** 36
    repeat_sequence = tuple(range(len(cube.edges))) * 3
    for bits in range(1 << len(cube.vertices)):
        background = supplied_background(cube, bits.bit_count())
        q0 = matter_q(cube, bits, background)
        for edge, (u, v, _axis) in enumerate(cube.edges):
            moved = bits; a, b = (bits >> u) & 1, (bits >> v) & 1
            if a != b: moved ^= (1 << u) | (1 << v)
            current = np.zeros(len(cube.edges), dtype=np.int64); current[edge] = a - b
            incidence_failures += not np.array_equal(cube.incidence @ current % F17, (matter_q(cube, moved, background) - q0) % F17)
            direct_l2 += 1
        moved = bits; accumulated = np.zeros(len(cube.edges), dtype=np.int64)
        for edge in repeat_sequence:
            u, v, _ = cube.edges[edge]; a, b = (moved >> u) & 1, (moved >> v) & 1
            if a != b: moved ^= (1 << u) | (1 << v)
            accumulated[edge] = (accumulated[edge] + a - b) % F17
        repeat_failures += not np.array_equal(cube.incidence @ accumulated % F17, (matter_q(cube, moved, background) - q0) % F17)
    return {
        "plaquette_direct_columns": len(direct), "plaquette_single_factor_corrected_max_residual": max(direct),
        "supplied_background_variant_columns": len(background_residuals),
        "supplied_background_variant_max_residual": max(background_residuals),
        "fixed_star_background_boundary": (
            "q_g(n)=n+g is checked at fixed supplied g for ordered-prefix, "
            "first-anchor, and last-anchor diagnostic fields; g selection/genesis "
            "and full affine-encoder frame/product/translation covariance remain open"
        ),
        "plaquette_single_raw_factor_residual": max(raw_direct),
        "plaquette_four_factor_columns": len(repeated), "plaquette_four_factor_corrected_max_residual": max(repeated),
        "plaquette_four_raw_factor_max_residual": max(repeated_raw), "plaquette_raw_phase": [((-1j)**4).real, ((-1j)**4).imag],
        "open_L2_direct_cases": direct_l2, "open_L2_incidence_failures": incidence_failures,
        "open_L2_repeated_factor_count": len(repeat_sequence), "open_L2_repeated_words": 1 << len(cube.vertices),
        "open_L2_repeated_uniform_intertwiner_failures": repeat_failures,
        "open_L2_raw_36_factor_phase": [raw_phase.real, raw_phase.imag],
        "open_L2_one_seam_stage_raw_phase": [((-1j)**len(cube.edges)).real, ((-1j)**len(cube.edges)).imag],
        "open_box_one_seam_stage_raw_phases": [
            {
                "shape": dims,
                "seams": len(open_box(dims).edges),
                "phase": [
                    ((-1j) ** len(open_box(dims).edges)).real,
                    ((-1j) ** len(open_box(dims).edges)).imag,
                ],
            }
            for dims in ((2, 2, 2), (3, 3, 3), (3, 2, 2))
        ],
        "open_L2_cycle_rank": nullspace_mod(cube.incidence).shape[1],
    }


def ring_affine_state(cell, mode, length=5):
    # q = n - delta_0; incidence is head-minus-tail on e_i:i->i+1.
    q = np.zeros(length, dtype=np.int64); q[cell] += 1; q[0] -= 1; q %= F17
    incidence = np.zeros((length, length), dtype=np.int64)
    for edge in range(length): incidence[edge, edge] = -1; incidence[(edge + 1) % length, edge] = 1
    base = solve_mod(incidence, q); amp = 1 / math.sqrt(F17)
    return {(cell, mode, tuple(map(int, (base + t) % F17))): amp for t in range(F17)}


def ring_coin(state, coin):
    out = {}
    for (cell, mode, links), amp in state.items():
        for target in range(6):
            value = coin[target, mode]
            if abs(value): out[(cell, target, links)] = out.get((cell, target, links), 0j) + value * amp
    return out


def ring_reverse(state):
    reverse = (1, 0, 3, 2, 5, 4)
    return {(cell, reverse[mode], links): amp for (cell, mode, links), amp in state.items()}


def ring_seams(state, length=5):
    # x seams are the actual Cycle870 left-mode 1 / right-mode 0 factors.
    # The unit-period y/z quotient supplies their p_y=p_z=0 partner swaps.
    out = {}
    for (cell, mode, links_tuple), amp in state.items():
        links = list(links_tuple)
        if mode == 1:  # left endpoint on edge cell, moves to its head as mode 0
            links[cell] = (links[cell] + 1) % F17; target = ((cell + 1) % length, 0)
        elif mode == 0:  # right endpoint of edge cell-1, moves to its tail as mode 1
            edge = (cell - 1) % length; links[edge] = (links[edge] - 1) % F17; target = (edge, 1)
        elif mode in (2, 3, 4, 5):
            target = (cell, mode ^ 1)  # cancels the onsite reverse at p_y=p_z=0
        key = (*target, tuple(links)); out[key] = out.get(key, 0j) + amp
    return out


def inner(left, right):
    return sum(np.conj(value) * right.get(key, 0j) for key, value in left.items())


def independent_fock_lift(one_particle):
    """Independent exterior-power lift on all 64 six-mode words."""
    one_particle = np.asarray(one_particle, dtype=complex)
    occupied = tuple(
        tuple(mode for mode in range(6) if bits >> mode & 1)
        for bits in range(64)
    )
    output = np.zeros((64, 64), dtype=complex)
    for source, source_modes in enumerate(occupied):
        for target, target_modes in enumerate(occupied):
            if len(source_modes) != len(target_modes):
                continue
            output[target, source] = (
                1.0 if not source_modes else np.linalg.det(
                    one_particle[np.ix_(target_modes, source_modes)]
                )
            )
    return output


def independent_onsite_star_preservation(coin, reverse_matrix, coupling):
    """Check the onsite targets against the order-17 matter clock.

    This is deliberately separate from the Cycle873 local-constraint core.
    The pinned Cycle870 checker supplies the physical-word/target bridge; this
    routine exhausts the additional target/star-clock obligation.
    """
    occupations = np.asarray([bits.bit_count() for bits in range(64)])
    clock = np.diag(np.exp(2j * math.pi * occupations / F17))
    contact_diagonal = np.exp(
        1j * coupling * occupations * (occupations - 1) / 2
    )
    targets = {
        "coin": independent_fock_lift(coin),
        "reverse": independent_fock_lift(reverse_matrix),
        "contact": np.diag(contact_diagonal).astype(complex),
    }
    targets["composed_onsite_epoch"] = (
        targets["contact"] @ targets["reverse"] @ targets["coin"]
    )
    commutators = {
        name: clean_float(float(np.linalg.norm(matrix @ clock - clock @ matrix)))
        for name, matrix in targets.items()
    }
    unitarity = {
        name: clean_float(float(np.linalg.norm(
            matrix.conj().T @ matrix - np.eye(64)
        )))
        for name, matrix in targets.items()
    }
    hostile = np.zeros((64, 64), dtype=complex)
    for bits in range(64):
        hostile[bits ^ 1, bits] = 1.0
    hostile_commutator = float(np.linalg.norm(hostile @ clock - clock @ hostile))
    return {
        "basis_occupation_columns": 64,
        "star_clock_commutator_residuals": commutators,
        "unitarity_residuals": unitarity,
        "bare_occupation_flip_control_commutator": hostile_commutator,
        "contact_one_particle_target_residual": clean_float(max(
            abs(contact_diagonal[bits] - 1.0)
            for bits in range(64) if bits.bit_count() == 1
        )),
        "physical_target_bridge": (
            "pinned Cycle870 emitted-word intertwiners plus this independent "
            "64-column target/star-clock check"
        ),
    }


def recurrence_dispersion_certificate(C870, C871, C219, C210):
    species = C219.common_species(float(C870.c230.BETA)); coin = np.asarray(species.coin, dtype=complex)
    gates = C871.coin_schedule(); reconstructed = np.eye(6, dtype=complex)
    for gate in gates:
        embedded = np.eye(6, dtype=complex)
        embedded[np.ix_(gate.modes, gate.modes)] = gate.matrix
        reconstructed = embedded @ reconstructed
    reverse_matrix = np.eye(6, dtype=complex)
    for left, right in ((0, 1), (2, 3), (4, 5)):
        helper = C870.reverse_helper(left, right)
        for a, b in ((left, helper), (right, helper), (left, helper)):
            swap = np.eye(6, dtype=complex); swap[a, a] = swap[b, b] = 0; swap[a, b] = swap[b, a] = 1
            reverse_matrix = swap @ reverse_matrix
    l2graph = C870.prep.OpenReferenceGraph(tuple(product(range(2), repeat=3)))
    l2rotations, phase_inventory = C870.build_update(l2graph, gates)
    factor_stage_order = tuple(dict.fromkeys(row.factor[0] for row in l2rotations))
    length = 5; encoded = [ring_affine_state(cell, mode, length) for cell in range(length) for mode in range(6)]
    observed_columns = []
    for source in encoded:
        observed_columns.append(ring_seams(ring_reverse(ring_coin(source, coin)), length))
    compressed = np.asarray([[inner(encoded[row], observed_columns[col]) for col in range(6*length)] for row in range(6*length)])
    # Direct periodic one-particle target: stream after the actual Cycle219 coin.
    native = np.zeros_like(compressed)
    directions = np.asarray(C210.DIRECTIONS)
    for cell in range(length):
        for source_mode in range(6):
            for target_mode in range(6):
                target_cell = (cell + int(directions[target_mode, 0])) % length
                native[target_cell * 6 + target_mode, cell * 6 + source_mode] += coin[target_mode, source_mode]
    intertwiner_residuals = []
    for col in range(6*length):
        expected = {}
        for row in range(6*length):
            coefficient = native[row, col]
            if abs(coefficient):
                for key, value in encoded[row].items(): expected[key] = expected.get(key, 0j) + coefficient * value
        intertwiner_residuals.append(state_distance(observed_columns[col], expected))
    fourier_residuals = []; block_unitarity = []
    for n in range(length):
        momentum = 2 * math.pi * n / length
        F = np.zeros((6*length, 6), dtype=complex)
        for cell in range(length):
            for mode in range(6): F[cell*6+mode, mode] = np.exp(1j * momentum * cell) / math.sqrt(length)
        block = F.conj().T @ compressed @ F
        bloch = np.diag(np.exp(-1j * (C210.DIRECTIONS @ np.array((momentum,0.0,0.0))))) @ coin
        fourier_residuals.append(float(np.linalg.norm(block - bloch)))
        block_unitarity.append(float(np.linalg.norm(block.conj().T @ block - np.eye(6))))

    def branch_phase(momentum):
        bloch = np.diag(np.exp(-1j * (C210.DIRECTIONS @ np.asarray(momentum)))) @ coin
        values, vectors = np.linalg.eig(bloch); overlaps = np.abs(vectors.conj().T @ C210.UNIFORM)
        return float(np.angle(values[int(np.argmax(overlaps))]))
    step = 1e-4; rest_phase = branch_phase(np.zeros(3)); curvature = np.zeros((3,3))
    for i in range(3):
        d = np.zeros(3); d[i] = step
        curvature[i,i] = (branch_phase(d) - 2*rest_phase + branch_phase(-d)) / step**2
        for j in range(i):
            pp=np.zeros(3); pm=np.zeros(3); mp=np.zeros(3); mm=np.zeros(3)
            pp[i]=pp[j]=step; pm[i]=step; pm[j]=-step; mp[i]=-step; mp[j]=step; mm[i]=mm[j]=-step
            curvature[i,j]=curvature[j,i]=(branch_phase(pp)-branch_phase(pm)-branch_phase(mp)+branch_phase(mm))/(4*step**2)
    dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
    contact = C870.contact_semantics()
    onsite_star = independent_onsite_star_preservation(
        coin, reverse_matrix, float(C870.c230.COUPLING)
    )
    eight_step_encoded_native_residual = float(np.linalg.norm(
        np.linalg.matrix_power(compressed, 8)
        - np.linalg.matrix_power(native, 8)
    ))
    return {
        "beta": float(C870.c230.BETA), "coin_schedule_gates": len(gates),
        "coin_schedule_reconstruction_residual": float(np.linalg.norm(reconstructed - coin)),
        "C870_factor_stage_order": factor_stage_order,
        "onsite_reverse_helper_permutation_residual": float(np.linalg.norm(reverse_matrix - C210.REVERSE)),
        "L2_compiled_relative_to_target_phase_angle": phase_inventory["compiled_relative_to_target_global_phase_angle"],
        "L2_formal_global_correction_angle": phase_inventory["exact_target_global_phase_correction_angle"],
        "ring_length": length, "encoded_joint_columns": len(encoded), "F17_terms_per_encoded_column": F17,
        "coin_reverse_seam_contact_intertwiner_max_residual": clean_float(max(intertwiner_residuals)),
        "compressed_native_matrix_residual": float(np.linalg.norm(compressed - native)),
        "eight_step_encoded_native_matrix_residual":
            eight_step_encoded_native_residual,
        "compressed_unitarity_residual": float(np.linalg.norm(compressed.conj().T @ compressed - np.eye(6*length))),
        "maximum_discrete_Bloch_block_residual": max(fourier_residuals),
        "maximum_discrete_Bloch_unitarity_residual": max(block_unitarity),
        "contact_one_particle_target_residual": onsite_star[
            "contact_one_particle_target_residual"
        ],
        "compiled_contact_all_occupation_residual_up_to_phase": contact["maximum_residual_up_to_global_phase"],
        "onsite_F17_star_preservation": onsite_star,
        "analytic_mass": float(species.analytic_mass), "rest_mass": float(C219.rest_mass(species)),
        "dispersion_mass_step_1e-4": dispersion_mass,
        "dispersion_relative_error": dispersion_mass / float(species.analytic_mass) - 1,
        "curvature_tensor": curvature.tolist(),
    }


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--source-root", type=Path, default=DEFAULT_ROOT); parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(); root = args.source_root.resolve()
    independence = source_ast_certificate(root)
    C870, C871, C714, C219, C210 = setup_imports(root)
    pins = {name: sha(root / name) for name in EXPECTED_SOURCE_SHA256}
    base_is_ancestor = subprocess.run(
        (
            "git", "merge-base", "--is-ancestor",
            EXPECTED_BASE_COMMIT, "HEAD",
        ),
        cwd=root,
        check=False,
    ).returncode == 0
    report = {
        "status": "pending", "schema": "cycle873-recurrent-f17-uniform-affine-open-box-independent-v1",
        "source_root": ".", "independence": independence,
        "provenance": {
            "base_commit": EXPECTED_BASE_COMMIT,
            "expected_base_is_ancestor_of_head": base_is_ancestor,
            "runner": str(Path(__file__).resolve().relative_to(root)),
        },
        "source_sha256": pins,
        "physical_selected_seam": physical_seam_certificate(C870, C871),
        "endpoint_extract": extraction_certificate(C870, C871),
        "reversible_primitives": reversible_primitive_certificate(C714),
        "effective_encoded_macro": effective_macro_certificate(),
        "literal_L2_emitted_schedule": emitted_schedule_certificate(root, C870, C871, C714),
        "repeated_factors": repeated_factor_certificate(),
        "six_mode_total_occupation_extension": six_mode_count_certificate(),
        "open_box_local_constraints": local_constraint_certificate(C870, C871),
        "cycle219_recurrence_dispersion": recurrence_dispersion_certificate(C870, C871, C219, C210),
        "phase_boundary": (
            "each raw grouped seam is -i times the augmented FSWAP; only the formal "
            "+i-corrected grouped macro is exact generally.  Raw seam-stage phases "
            "depend on the seam count, while the full epoch keeps Cycle870's separate "
            "ledgered global correction"
        ),
    }
    failures = []
    if not base_is_ancestor: failures.append("expected base is not an ancestor of HEAD")
    if independence["primary_sha256"] != PRIMARY_SHA256: failures.append("primary hash")
    if independence["physical_core_sha256"] != PHYSICAL_CORE_SHA256: failures.append("physical core hash")
    if independence["physical_receipt_sha256"] != PHYSICAL_RECEIPT_SHA256: failures.append("physical receipt hash")
    if independence["checker_runtime_imported_primary"]: failures.append("primary imported")
    if independence["physical_core_imports_cycle873_primary"]: failures.append("physical core imports primary")
    if not independence["rail_offsets_match"] or not independence["emit_field_order_match"] or independence["emit_required_semantics_missing"]: failures.append("primary AST")
    if pins != EXPECTED_SOURCE_SHA256: failures.append("source pins")
    physical = report["physical_selected_seam"]
    for key in ("compiler_signature_match_failures", "physical_constraint_anticommutators", "physical_lift_pair_homomorphism_failures"):
        if physical[key]: failures.append("physical:" + key)
    if physical["maximum_arbitrary_coherent_full_support_compiler_residual"] > TOL: failures.append("physical compiler")
    if physical["raw_to_minus_i_FSWAP_residual"] > TOL or physical["formal_i_corrected_to_FSWAP_residual"] > TOL: failures.append("seam factorization")
    if min(physical["four_rotation_deletion_residuals_up_to_global_phase"]) <= 0.1: failures.append("inactive rotation deletion")
    primitive = report["reversible_primitives"]
    for key in ("clean_target_reduced_Toffoli_column_residual", "fredkin_residual", "predicate_compute_clean_column_residual", "predicate_uncompute_supplied_column_residual"):
        if primitive[key] > TOL: failures.append("primitive:" + key)
    if min(primitive["clean_target_remaining_literal_deletion_residuals"]) <= TOL or min(primitive["fredkin_literal_deletion_residuals_on_onehot_controlled_columns"]) <= TOL or min(primitive["predicate_literal_deletion_residuals"]) <= TOL or min(primitive["uncompute_literal_deletion_residuals"]) <= TOL: failures.append("inactive primitive deletion")
    schedule_report = report["literal_L2_emitted_schedule"]
    if not schedule_report["schedule_hash_match"]: failures.append("literal schedule hash")
    if schedule_report["all_seam_rotation_physical_constraint_anticommutators"] or schedule_report["all_endpoint_B_physical_constraint_anticommutators"] or schedule_report["all_seam_maximum_raw_to_minus_i_FSWAP_residual"] > TOL or schedule_report["all_seam_maximum_formal_corrected_residual"] > TOL: failures.append("all-seam physical algebra")
    for family in report["effective_encoded_macro"]["families"]:
        if family["formal_corrected_basis_max_residual"] > TOL or family["formal_corrected_arbitrary_coherent_residual"] > TOL or family["scratch_cleanup_failures"]: failures.append("effective macro")
        if any(not row["changed_columns"] for row in family["component_mutations"].values()): failures.append("inactive macro component")
    repeated = report["repeated_factors"]
    if repeated["plaquette_four_raw_factor_max_residual"] > TOL or repeated["open_L2_incidence_failures"] or repeated["open_L2_repeated_uniform_intertwiner_failures"]: failures.append("repeated factors")
    if repeated["supplied_background_variant_columns"] != 192 or repeated["supplied_background_variant_max_residual"] > TOL: failures.append("fixed-star background variants")
    six_mode = report["six_mode_total_occupation_extension"]
    if (
        six_mode["rows"] != 2448
        or six_mode["FSWAP_minus_11_rows"] != 612
        or any(six_mode[key] for key in (
            "incidence_failures", "fixed_background_or_star_invariance_failures",
            "occupation_range_failures", "FSWAP_sign_failures",
        ))
        or six_mode["wrong_incidence_sign_detected_rows"] != 1224
        or six_mode["omitted_link_shift_detected_rows"] != 1224
    ): failures.append("six-mode total occupation extension")
    expected_stage_phases = {
        (2, 2, 2): [1.0, 0.0],
        (3, 3, 3): [-1.0, 0.0],
        (3, 2, 2): [1.0, 0.0],
    }
    if any(
        row["phase"] != expected_stage_phases[tuple(row["shape"])]
        for row in repeated["open_box_one_seam_stage_raw_phases"]
    ): failures.append("open-box raw seam-stage phase")
    local = report["open_box_local_constraints"]
    expected_local = {
        (2, 2, 2): (8, 12, 6, 5, 72),
        (3, 3, 3): (27, 54, 36, 28, 126),
        (3, 2, 2): (12, 20, 11, 9, 90),
    }
    for row in local["fixtures"]:
        shape = tuple(row["shape"]); V, E, Pn, beta, star = expected_local[shape]
        if (row["vertices"], row["oriented_links"], row["plaquettes"], row["cycle_space_rank"], row["maximum_star_support_M2"]) != (V, E, Pn, beta, star): failures.append("local constraint census")
        if row["incidence_rank_mod17"] != V - 1 or row["plaquette_boundary_rank_mod17"] != beta or row["uniform_plus_one_dimension"] != 1: failures.append("local constraint rank")
        if any(row[key] for key in ("boundary_of_boundary_nonzero_entries", "onehot_path_failures", "rail_pair_overlap_sites", "rail_carrier_aux_collision_sites", "plaquette_word_or_NN_failures", "plaquette_layer_collisions")): failures.append("local constraint physical")
        if row["plaquette_support_M2"] != 68: failures.append("plaquette support")
    if local["proper_frames"] != 24 or local["ordered_frame_products"] != 576: failures.append("local frames")
    if local["plaquette_SWAP_deletions_tested"] != 3392 or local["undetected_plaquette_SWAP_deletions"]: failures.append("local deletion controls")
    recurrence = report["cycle219_recurrence_dispersion"]
    if (
        recurrence["coin_reverse_seam_contact_intertwiner_max_residual"] > TOL
        or recurrence["compressed_native_matrix_residual"] > TOL
        or recurrence["eight_step_encoded_native_matrix_residual"] > TOL
        or recurrence["maximum_discrete_Bloch_block_residual"] > TOL
    ): failures.append("Cycle219 recurrence")
    if tuple(recurrence["C870_factor_stage_order"]) != ("coin", "reverse", "seam", "contact") or recurrence["onsite_reverse_helper_permutation_residual"] > TOL: failures.append("Cycle870 stage grammar")
    onsite_star = recurrence["onsite_F17_star_preservation"]
    if (
        any(value > TOL for value in onsite_star["star_clock_commutator_residuals"].values())
        or any(value > TOL for value in onsite_star["unitarity_residuals"].values())
        or onsite_star["contact_one_particle_target_residual"] > TOL
        or onsite_star["bare_occupation_flip_control_commutator"] <= 1.0e-3
    ): failures.append("onsite F17 star preservation")
    report["failures"] = failures; report["status"] = "pass" if not failures else "fail"
    output = args.output; output.write_text(json.dumps(report, indent=2, sort_keys=True, default=lambda x: x.item() if isinstance(x, np.generic) else list(x) if isinstance(x, tuple) else str(x)) + "\n")
    print(json.dumps({
        "status": report["status"],
        "base_commit": report["provenance"]["base_commit"],
        "expected_base_is_ancestor_of_head": report["provenance"]["expected_base_is_ancestor_of_head"],
        "receipt": str(DEFAULT_OUTPUT.relative_to(DEFAULT_ROOT)),
        "failures": failures,
        "primary_imported": independence["checker_runtime_imported_primary"],
        "physical_raw_to_minus_i_residual": report["physical_selected_seam"]["raw_to_minus_i_FSWAP_residual"],
        "C219_dispersion_mass": report["cycle219_recurrence_dispersion"]["dispersion_mass_step_1e-4"],
    }, indent=2, sort_keys=True))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
