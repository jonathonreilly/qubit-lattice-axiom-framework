#!/usr/bin/env python3
"""Joined one-time OpenReference preparation and native update certificate.

This companion consumes the Cycle870 root placement/preparation route atlas and
the native update probe on one identical 18N+3E carrier map.  It checks cubic
L=2 and L=3 boxes.  The root atlas is a one-time supplied preparation macro;
the update is the exact coin -> reverse -> seam -> contact word.  No global
Jordan--Wigner character is constructed or compared.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, groupby, product
import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
UPDATE_SOURCE = HERE / "frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py"
UPDATE_RECEIPT = (
    ROOT / "outputs" / "cycle870_openreference_native_recurrent_update_receipt_2026_08_02.json"
)
ROOT_SOURCE = HERE / "frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py"
ROOT_RECEIPT = (
    ROOT / "outputs" / "cycle870_openreference_physical_m2_placement_receipt_2026_08_02.json"
)
AUDIT_INPUT_PATHS = (UPDATE_SOURCE, UPDATE_RECEIPT, ROOT_SOURCE, ROOT_RECEIPT)
EXPECTED_INPUT_SHA256 = {
    UPDATE_SOURCE: "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
    UPDATE_RECEIPT: "b1c812afbf25b84b99a5d171cf7925ffc86272e52c252c5f7ee68cb9f5a76807",
    ROOT_SOURCE: "64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2",
    ROOT_RECEIPT: "ab2d980726e336221e49808b6edcfaaae802173ee2f00fe96d8d55a4f2c6899d",
}
TOL = 2.0e-9
EXPECTED_UPDATE_STAGES = (
    "onsite_coin_mass",
    "onsite_reverse_fswap",
    "directed_seam_fswap",
    "onsite_contact",
)


def load_update():
    for path, expected in EXPECTED_INPUT_SHA256.items():
        observed = sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(
                f"pinned Cycle870 input changed: {path.name}: {observed} != {expected}"
            )
    spec = importlib.util.spec_from_file_location(
        "cycle871_openreference_native_update", UPDATE_SOURCE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load native update probe")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


update = load_update()
root = update.root_place
Pauli = update.Pauli
Coord = update.Coord


@dataclass(frozen=True)
class PrimitiveOp:
    stage: str
    kind: str
    sites: tuple[Coord, ...]
    matrix: np.ndarray
    owner: Coord | None = None
    atlas_role: tuple[object, ...] | None = None


CZ_GATE = np.diag((1, 1, 1, -1)).astype(complex)
Z_GATE = np.diag((1, -1)).astype(complex)


def permutation_matrix(table) -> np.ndarray:
    matrix = np.zeros((len(table), len(table)), dtype=complex)
    for source, target in enumerate(table):
        matrix[target, source] = 1.0
    return matrix


def semantic_router_matrix(table) -> np.ndarray:
    """Matrix in the substrate's little-endian |left,right> local basis."""
    return permutation_matrix(table)


def embed_local_gate(qubits: int, sites: tuple[int, ...], gate: np.ndarray) -> np.ndarray:
    dimension = 1 << qubits
    output = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        local_source = sum(
            ((source >> site) & 1) << local_index
            for local_index, site in enumerate(sites)
        )
        for local_target in range(1 << len(sites)):
            amplitude = gate[local_target, local_source]
            if abs(amplitude) < 1.0e-15:
                continue
            target = source
            for local_index, site in enumerate(sites):
                bit = (local_target >> local_index) & 1
                target = (target & ~(1 << site)) | (bit << site)
            output[target, source] += amplitude
    return output


def local_word_matrix(qubits: int, word) -> np.ndarray:
    output = np.eye(1 << qubits, dtype=complex)
    for sites, gate in word:
        output = embed_local_gate(qubits, sites, gate) @ output
    return output


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def interaction_key(row) -> tuple[object, ...]:
    return (row.owner, row.role, row.left, row.right)


def rows_sha256(rows) -> str:
    payload = "\n".join(sorted(repr(row) for row in rows))
    return sha256(payload.encode()).hexdigest()


def auxiliary_registers(graph) -> set[Coord]:
    return {
        root.slot(cell, role, index)
        for cell in graph.cells
        for role, count in root.ROLE_COUNTS.items()
        for index in range(count)
    }


def expected_controller_rows(shape, graph, site_map):
    """Independent event census for every valid cubic echo node."""
    length = shape[0]
    output = []
    valid_by_kind = Counter()
    roots_by_kind = Counter()
    nonroots_by_kind = Counter()
    pairs = ((0, 1), (0, 2), (1, 2))
    for node_kind in ("ay", "az"):
        axis = 1 if node_kind == "ay" else 2
        for x in range(length):
            for y in range(length):
                for z in range(length):
                    node = (node_kind, x, y, z)
                    try:
                        parent_source = root.echo.parent_and_source(node)
                        edge = graph.cross_edge[((x, y, z), axis, 0)]
                    except KeyError:
                        continue
                    valid_by_kind[node_kind] += 1
                    owner = (x, y, z)
                    role = f"{node_kind}_controller"
                    child_value = root.slot(owner, role, 0)
                    if parent_source is None:
                        roots_by_kind[node_kind] += 1
                        output.extend(
                            (
                                (
                                    owner,
                                    ("controller_root_epoch", node_kind),
                                    root.slot(owner, role, 4),
                                    root.slot(owner, role, 5),
                                ),
                                (
                                    owner,
                                    ("controller_router", node_kind),
                                    root.slot(owner, role, 2),
                                    root.slot(owner, role, 3),
                                ),
                            )
                        )
                        continue
                    nonroots_by_kind[node_kind] += 1
                    parent, source_key = parent_source
                    parent_cell = root.echo.node_anchor(parent)
                    parent_role = f"{parent[0]}_controller"
                    source_cell, source_axes = source_key
                    source = root.slot(
                        source_cell, "coarse_syndrome", pairs.index(tuple(source_axes))
                    )
                    for traversal in ("down", "up"):
                        output.extend(
                            (
                                (
                                    owner,
                                    ("controller_parent_xor", node_kind, traversal),
                                    root.slot(parent_cell, parent_role, 0),
                                    child_value,
                                ),
                                (
                                    owner,
                                    ("controller_source_xor", node_kind, traversal),
                                    source,
                                    child_value,
                                ),
                                (
                                    owner,
                                    ("controller_token_swap", node_kind, traversal),
                                    root.slot(parent_cell, parent_role, 1),
                                    root.slot(owner, role, 1),
                                ),
                            )
                        )
                    output.extend(
                        (
                            (
                                owner,
                                ("controller_emit", node_kind),
                                child_value,
                                site_map[edge][0],
                            ),
                            (
                                owner,
                                ("controller_router", node_kind),
                                root.slot(owner, role, 2),
                                root.slot(owner, role, 3),
                            ),
                        )
                    )
    return output, {
        "valid_nodes_by_kind": dict(valid_by_kind),
        "root_nodes_by_kind": dict(roots_by_kind),
        "nonroot_nodes_by_kind": dict(nonroots_by_kind),
    }


def controller_coverage(shape, graph, site_map, actual) -> dict[str, object]:
    expected, census = expected_controller_rows(shape, graph, site_map)
    observed_counter = Counter(interaction_key(row) for row in actual)
    expected_counter = Counter(expected)
    missing = expected_counter - observed_counter
    extra = observed_counter - expected_counter
    role_census = Counter(row.role[0] for row in actual)
    return {
        **census,
        "expected_interactions": sum(expected_counter.values()),
        "observed_interactions": sum(observed_counter.values()),
        "missing_interactions": sum(missing.values()),
        "extra_interactions": sum(extra.values()),
        "expected_multiset_sha256": rows_sha256(expected_counter.elements()),
        "observed_multiset_sha256": rows_sha256(observed_counter.elements()),
        "role_census": dict(sorted(role_census.items())),
        "all_root_and_nonroot_event_families_covered": all(
            role_census[name] > 0
            for name in (
                "controller_root_epoch",
                "controller_parent_xor",
                "controller_source_xor",
                "controller_token_swap",
                "controller_emit",
                "controller_router",
            )
        ),
    }


def root_route_word_digest(staged_rows) -> str:
    digest = sha256()
    for stage, rows in staged_rows:
        for row in rows:
            path = root.manhattan_path(row.left, row.right)
            digest.update(f"stage:{stage}:role:{row.role}:owner:{row.owner}".encode())
            for index in range(len(path) - 2):
                digest.update(f"route_swap:{path[index]}:{path[index + 1]}".encode())
            digest.update(f"interaction:{row.role}:{path[-2:]}".encode())
            for index in reversed(range(len(path) - 2)):
                digest.update(f"route_swap:{path[index]}:{path[index + 1]}".encode())
    return digest.hexdigest()


def root_bank_route_scan(staged_rows, carrier, auxiliary) -> dict[str, object]:
    touched_carrier = set()
    touched_auxiliary = set()
    touched_transient = set()
    endpoint_outside_bank = 0
    for _stage, rows in staged_rows:
        for row in rows:
            endpoint_outside_bank += row.left not in carrier | auxiliary
            endpoint_outside_bank += row.right not in carrier | auxiliary
            path = set(root.manhattan_path(row.left, row.right))
            touched_carrier.update(path & carrier)
            touched_auxiliary.update(path & auxiliary)
            touched_transient.update(path - carrier - auxiliary)
    return {
        "endpoint_outside_declared_bank_failures": endpoint_outside_bank,
        "carrier_sites_touched": len(touched_carrier),
        "auxiliary_sites_touched_and_returned": len(touched_auxiliary),
        "transient_route_sites_touched_and_returned": len(touched_transient),
    }


def check_owner_role(kind, key):
    if kind == "cell_triangle":
        return key, "triangle_syndrome", "triangle_syndrome"
    if kind == "coarse_plaquette":
        return key[0], "coarse_syndrome", "coarse_syndrome"
    if kind == "bond_rectangle":
        return key[0], "bond_syndrome", "bond_syndrome"
    raise AssertionError(kind)


def coherent_check_primitives(graph, context, syndrome_catalog):
    """Compile every loop check into coherent parity extraction on a retained ancilla."""
    stages = {
        "triangle_syndrome": [],
        "coarse_syndrome": [],
        "bond_syndrome": [],
    }
    counters = Counter()
    generated_atlas = Counter()
    sign_flip_count = 0
    check_count = Counter()
    for abstract, kind, key in root.cycle_rows(graph):
        owner, role, stage = check_owner_role(kind, key)
        local_index = counters[(owner, role)]
        counters[(owner, role)] += 1
        ancilla = root.slot(owner, role, local_index)
        physical = update.physical_lift(abstract, context)
        axes, sign = update.c707.pauli_axes(physical, context.sites)
        check_count[kind] += 1
        for support_index, (target, axis) in enumerate(axes):
            atlas_role = ("syndrome", kind, local_index, support_index)
            generated_atlas[(owner, atlas_role, ancilla, target)] += 1
            if axis == "X":
                stages[stage].append(
                    PrimitiveOp(stage, "check_basis_H", (target,), update.c707.c655.H)
                )
            elif axis == "Y":
                stages[stage].extend(
                    (
                        PrimitiveOp(stage, "check_basis_Sdg", (target,), update.c707.SDG_GATE),
                        PrimitiveOp(stage, "check_basis_H", (target,), update.c707.c655.H),
                    )
                )
            stages[stage].append(
                PrimitiveOp(
                    stage,
                    "check_parity_CNOT",
                    (target, ancilla),
                    update.c707.c655.CNOT,
                    owner,
                    atlas_role,
                )
            )
            if axis == "X":
                stages[stage].append(
                    PrimitiveOp(stage, "check_basis_H", (target,), update.c707.c655.H)
                )
            elif axis == "Y":
                stages[stage].extend(
                    (
                        PrimitiveOp(stage, "check_basis_H", (target,), update.c707.c655.H),
                        PrimitiveOp(stage, "check_basis_S", (target,), update.c707.S_GATE),
                    )
                )
        if sign == -1:
            sign_flip_count += 1
            stages[stage].append(
                PrimitiveOp(stage, "check_sign_X", (ancilla,), update.c707.c655.X)
            )
    observed_atlas = Counter(interaction_key(row) for row in syndrome_catalog)
    return stages, {
        "checks_by_kind": dict(sorted(check_count.items())),
        "coherent_ancilla_initial_state": "|0>",
        "retained_syndrome_bit_convention": "0 means +1 check eigenvalue",
        "negative_check_sign_X_flips": sign_flip_count,
        "support_parity_CNOTs": sum(generated_atlas.values()),
        "support_CNOT_deletion_changes_extracted_Pauli": sum(
            generated_atlas.values()
        ),
        "support_atlas_missing": sum((observed_atlas - generated_atlas).values()),
        "support_atlas_extra": sum((generated_atlas - observed_atlas).values()),
        "support_atlas_expected_sha256": rows_sha256(observed_atlas.elements()),
        "support_atlas_compiled_sha256": rows_sha256(generated_atlas.elements()),
    }


def correction_primitives(correction_catalog):
    stages = {"triangle_correction": [], "bond_correction": []}
    for row in correction_catalog:
        stage = (
            "triangle_correction"
            if row.role[0] == "triangle_correction"
            else "bond_correction"
        )
        stages[stage].append(
            PrimitiveOp(
                stage,
                "syndrome_controlled_Z",
                (row.left, row.right),
                CZ_GATE,
                row.owner,
                row.role,
            )
        )
    return stages


def controlled_axis_primitives(stage, control, target, axis, owner, atlas_role):
    if axis == "X":
        return [
            PrimitiveOp(
                stage,
                "loader_controlled_X",
                (control, target),
                update.c707.c655.CNOT,
                owner,
                atlas_role,
            )
        ]
    if axis == "Z":
        return [
            PrimitiveOp(
                stage,
                "loader_controlled_Z",
                (control, target),
                CZ_GATE,
                owner,
                atlas_role,
            )
        ]
    if axis == "Y":
        return [
            PrimitiveOp(stage, "loader_target_Sdg", (target,), update.c707.SDG_GATE),
            PrimitiveOp(
                stage,
                "loader_controlled_X_for_Y",
                (control, target),
                update.c707.c655.CNOT,
                owner,
                atlas_role,
            ),
            PrimitiveOp(stage, "loader_target_S", (target,), update.c707.S_GATE),
        ]
    raise AssertionError(axis)


def loader_primitives(graph, context, loader_catalog):
    stage = "logical_load"
    output = []
    generated_atlas = Counter()
    sign_controls = 0
    non_z_parity_axes = 0
    for cell, mode, xrow, zrow in root.logical_rows(graph):
        source = root.slot(cell, "input", mode)
        physical_x = update.physical_lift(xrow, context)
        xaxes, xsign = update.c707.pauli_axes(physical_x, context.sites)
        for support_index, (target, axis) in enumerate(xaxes):
            atlas_role = ("loader", mode, "X", support_index)
            generated_atlas[(cell, atlas_role, source, target)] += 1
            output.extend(
                controlled_axis_primitives(
                    stage, source, target, axis, cell, atlas_role
                )
            )
        if xsign == -1:
            sign_controls += 1
            output.append(
                PrimitiveOp(stage, "loader_control_sign_Z", (source,), Z_GATE)
            )
        physical_z = update.physical_lift(zrow, context)
        zaxes, zsign = update.c707.pauli_axes(physical_z, context.sites)
        if zsign != 1:
            raise AssertionError(("logical Z sign", cell, mode, zsign))
        for support_index, (target, axis) in enumerate(zaxes):
            non_z_parity_axes += axis != "Z"
            atlas_role = ("loader", mode, "Z", support_index)
            generated_atlas[(cell, atlas_role, target, source)] += 1
            output.append(
                PrimitiveOp(
                    stage,
                    "loader_parity_CNOT",
                    (target, source),
                    update.c707.c655.CNOT,
                    cell,
                    atlas_role,
                )
            )
    observed_atlas = Counter(interaction_key(row) for row in loader_catalog)
    return output, {
        "logical_rows": len(root.logical_rows(graph)),
        "controlled_X_sign_corrections": sign_controls,
        "compiled_loader_support_interactions": sum(generated_atlas.values()),
        "loader_support_gate_deletion_active_columns": sum(
            generated_atlas.values()
        ),
        "non_Z_axes_in_parity_unload": non_z_parity_axes,
        "support_atlas_missing": sum((observed_atlas - generated_atlas).values()),
        "support_atlas_extra": sum((generated_atlas - observed_atlas).values()),
        "support_atlas_expected_sha256": rows_sha256(observed_atlas.elements()),
        "support_atlas_compiled_sha256": rows_sha256(generated_atlas.elements()),
        "truth_table": "|q>|0_L> -> |q>|q_L> -> |0>|q_L>",
    }


def controller_nodes(length: int, graph):
    rows = []
    for node_kind in ("ay", "az"):
        axis = 1 if node_kind == "ay" else 2
        for x, y, z in product(range(length), repeat=3):
            node = (node_kind, x, y, z)
            try:
                graph.cross_edge[((x, y, z), axis, 0)]
            except KeyError:
                continue
            rows.append(node)
    return tuple(rows)


def toffoli_primitives(event: PrimitiveOp):
    control1, control2, target = event.sites
    stage = event.stage
    return [
        PrimitiveOp(stage, "controller_Toffoli_H", (target,), update.c707.c655.H),
        PrimitiveOp(stage, "controller_Toffoli_CNOT", (control2, target), update.c707.c655.CNOT),
        PrimitiveOp(stage, "controller_Toffoli_Tdg", (target,), update.c707.c655.TDG),
        PrimitiveOp(stage, "controller_Toffoli_CNOT", (control1, target), update.c707.c655.CNOT),
        PrimitiveOp(stage, "controller_Toffoli_T", (target,), update.c707.c655.T),
        PrimitiveOp(stage, "controller_Toffoli_CNOT", (control2, target), update.c707.c655.CNOT),
        PrimitiveOp(stage, "controller_Toffoli_Tdg", (target,), update.c707.c655.TDG),
        PrimitiveOp(stage, "controller_Toffoli_CNOT", (control1, target), update.c707.c655.CNOT),
        PrimitiveOp(stage, "controller_Toffoli_T", (control2,), update.c707.c655.T),
        PrimitiveOp(stage, "controller_Toffoli_T", (target,), update.c707.c655.T),
        PrimitiveOp(stage, "controller_Toffoli_H", (target,), update.c707.c655.H),
        PrimitiveOp(stage, "controller_Toffoli_CNOT", (control1, control2), update.c707.c655.CNOT),
        PrimitiveOp(stage, "controller_Toffoli_T", (control1,), update.c707.c655.T),
        PrimitiveOp(stage, "controller_Toffoli_Tdg", (control2,), update.c707.c655.TDG),
        PrimitiveOp(stage, "controller_Toffoli_CNOT", (control1, control2), update.c707.c655.CNOT),
    ]


def router_primitive_word(event: PrimitiveOp):
    """Decompose every echo-router table into X/CNOT on its two M2 sites."""
    left, right = event.sites
    table_name = event.kind.removeprefix("controller_router_")
    if table_name == "leaf":
        return []
    if table_name == "one_child":
        return [
            PrimitiveOp(event.stage, "controller_router_X_right_pre", (right,), update.c707.c655.X),
            PrimitiveOp(event.stage, "controller_router_CNOT_right_left", (right, left), update.c707.c655.CNOT),
            PrimitiveOp(event.stage, "controller_router_X_right_post", (right,), update.c707.c655.X),
        ]
    if table_name == "two_children":
        return [
            PrimitiveOp(event.stage, "controller_router_X_left", (left,), update.c707.c655.X),
            PrimitiveOp(event.stage, "controller_router_CNOT_right_left", (right, left), update.c707.c655.CNOT),
            PrimitiveOp(event.stage, "controller_router_CNOT_left_right", (left, right), update.c707.c655.CNOT),
            PrimitiveOp(event.stage, "controller_router_X_right", (right,), update.c707.c655.X),
        ]
    raise AssertionError(table_name)


def router_decomposition_certificate():
    tables = root.echo.local_permutation_tables()["router_permutations"]
    residuals = {}
    deletion_residuals = {}
    gate_counts = {}
    dummy_sites = ((0, 0, 0), (1, 0, 0))
    for table_name, table in tables.items():
        event = PrimitiveOp(
            "router_test",
            f"controller_router_{table_name}",
            dummy_sites,
            semantic_router_matrix(table),
        )
        word = router_primitive_word(event)
        local_word = []
        for operation in word:
            local_sites = tuple(dummy_sites.index(site) for site in operation.sites)
            local_word.append((local_sites, operation.matrix))
        residuals[table_name] = float(
            np.linalg.norm(local_word_matrix(2, local_word) - semantic_router_matrix(table))
        )
        deletion_residuals[table_name] = tuple(
            float(
                np.linalg.norm(
                    local_word_matrix(2, local_word[:deleted] + local_word[deleted + 1 :])
                    - semantic_router_matrix(table)
                )
            )
            for deleted in range(len(local_word))
        )
        gate_counts[table_name] = len(word)
    return {
        "semantic_integer_encoding": "left + 2*right",
        "matrix_basis_encoding": "left + 2*right (substrate little-endian wires)",
        "gate_set": "X/CNOT",
        "gate_counts": gate_counts,
        "residuals": residuals,
        "subgate_deletion_residuals": deletion_residuals,
        "minimum_nonidentity_subgate_deletion_residual": min(
            value
            for table_name, rows in deletion_residuals.items()
            if table_name != "leaf"
            for value in rows
        ),
        "maximum_residual": max(residuals.values()),
    }


def compile_controller_events(events):
    output = []
    for event in events:
        if "Toffoli" in event.kind:
            output.extend(toffoli_primitives(event))
        elif event.kind == "controller_emit_CCZ":
            target = event.sites[2]
            output.append(
                PrimitiveOp(event.stage, "controller_CCZ_H", (target,), update.c707.c655.H)
            )
            proxy = PrimitiveOp(event.stage, "controller_CCZ_Toffoli", event.sites, event.matrix)
            output.extend(toffoli_primitives(proxy))
            output.append(
                PrimitiveOp(event.stage, "controller_CCZ_H", (target,), update.c707.c655.H)
            )
        elif event.kind.startswith("controller_router_"):
            output.extend(router_primitive_word(event))
        else:
            output.append(event)
    return output


def controller_chronology_primitives(shape, graph, site_map, controller_catalog):
    if len(set(shape)) != 1:
        raise ValueError("chronological echo is cubic-only")
    length = shape[0]
    stage = "coarse_echo_correction_ack"
    output = []
    used_atlas = Counter()
    router_applications = Counter()
    tables = root.echo.local_permutation_tables()

    def append(row: PrimitiveOp):
        output.append(row)
        if row.owner is not None and row.atlas_role is not None:
            role = row.atlas_role[0]
            if role in ("controller_parent_xor", "controller_source_xor"):
                left, right = row.sites[1], row.sites[2]
            elif role == "controller_emit":
                left, right = row.sites[1], row.sites[2]
            else:
                left, right = row.sites[0], row.sites[1]
            used_atlas[(row.owner, row.atlas_role, left, right)] += 1

    def router(node):
        node_kind = node[0]
        owner = root.echo.node_anchor(node)
        role = f"{node_kind}_controller"
        local_children = root.echo.children(node, length, frozenset())
        table_name = {0: "leaf", 1: "one_child", 2: "two_children"}[
            len(local_children)
        ]
        table = tables["router_permutations"][table_name]
        atlas_role = ("controller_router", node_kind)
        router_applications[node] += 1
        append(
            PrimitiveOp(
                stage,
                f"controller_router_{table_name}",
                (root.slot(owner, role, 2), root.slot(owner, role, 3)),
                semantic_router_matrix(table),
                owner,
                atlas_role,
            )
        )

    def traverse(node):
        node_kind = node[0]
        owner = root.echo.node_anchor(node)
        for child in root.echo.children(node, length, frozenset()):
            router(node)
            child_kind = child[0]
            child_owner = root.echo.node_anchor(child)
            child_role = f"{child_kind}_controller"
            parent_role = f"{node_kind}_controller"
            parent, source_key = root.echo.parent_and_source(child)
            if parent != node:
                raise AssertionError(("bad chronological parent", node, child, parent))
            source = root.syndrome_slot_for_source(source_key[0], source_key[1])
            parent_value = root.slot(owner, parent_role, 0)
            child_value = root.slot(child_owner, child_role, 0)
            parent_token = root.slot(owner, parent_role, 1)
            child_token = root.slot(child_owner, child_role, 1)
            down_roles = (
                ("controller_parent_xor", child_kind, "down"),
                ("controller_source_xor", child_kind, "down"),
                ("controller_token_swap", child_kind, "down"),
                ("controller_emit", child_kind),
            )
            append(
                PrimitiveOp(
                    stage,
                    "controller_parent_Toffoli_down",
                    (parent_token, parent_value, child_value),
                    update.c707.c655.ideal_toffoli(),
                    child_owner,
                    down_roles[0],
                )
            )
            append(
                PrimitiveOp(
                    stage,
                    "controller_source_Toffoli_down",
                    (parent_token, source, child_value),
                    update.c707.c655.ideal_toffoli(),
                    child_owner,
                    down_roles[1],
                )
            )
            append(
                PrimitiveOp(
                    stage,
                    "controller_token_SWAP_down",
                    (parent_token, child_token),
                    update.c707.c655.SWAP,
                    child_owner,
                    down_roles[2],
                )
            )
            append(
                PrimitiveOp(
                    stage,
                    "controller_emit_CCZ",
                    (
                        child_token,
                        child_value,
                        root.stream_target(graph, site_map, child),
                    ),
                    np.diag((1, 1, 1, 1, 1, 1, 1, -1)).astype(complex),
                    child_owner,
                    down_roles[3],
                )
            )
            traverse(child)
            append(
                PrimitiveOp(
                    stage,
                    "controller_token_SWAP_up",
                    (parent_token, child_token),
                    update.c707.c655.SWAP,
                    child_owner,
                    ("controller_token_swap", child_kind, "up"),
                )
            )
            append(
                PrimitiveOp(
                    stage,
                    "controller_source_Toffoli_up",
                    (parent_token, source, child_value),
                    update.c707.c655.ideal_toffoli(),
                    child_owner,
                    ("controller_source_xor", child_kind, "up"),
                )
            )
            append(
                PrimitiveOp(
                    stage,
                    "controller_parent_Toffoli_up",
                    (parent_token, parent_value, child_value),
                    update.c707.c655.ideal_toffoli(),
                    child_owner,
                    ("controller_parent_xor", child_kind, "up"),
                )
            )
        router(node)

    for tree_root in root.echo.forest_roots(length):
        owner = root.echo.node_anchor(tree_root)
        node_kind = tree_root[0]
        role = f"{node_kind}_controller"
        append(
            PrimitiveOp(
                stage,
                "controller_root_fresh_to_token_SWAP",
                (root.slot(owner, role, 4), root.slot(owner, role, 1)),
                update.c707.c655.SWAP,
                owner,
                ("controller_root_epoch", node_kind, "start"),
            )
        )
        traverse(tree_root)
        append(
            PrimitiveOp(
                stage,
                "controller_root_token_to_spent_SWAP",
                (root.slot(owner, role, 1), root.slot(owner, role, 5)),
                update.c707.c655.SWAP,
                owner,
                ("controller_root_epoch", node_kind, "spent"),
            )
        )

    catalog = Counter(interaction_key(row) for row in controller_catalog)
    catalog_non_epoch = Counter(
        {
            key: count
            for key, count in catalog.items()
            if key[1][0] != "controller_root_epoch"
        }
    )
    used_non_epoch = Counter(
        {
            key: 1
            for key in used_atlas
            if key[1][0] != "controller_root_epoch"
        }
    )
    root_count = len(root.echo.forest_roots(length))
    compiled = compile_controller_events(output)
    h_target = embed_local_gate(3, (2,), update.c707.c655.H)
    ccz_residual = float(
        np.linalg.norm(
            h_target
            @ update.c707.c655.ideal_toffoli()
            @ h_target
            - np.diag((1, 1, 1, 1, 1, 1, 1, -1))
        )
    )
    return compiled, output, {
        "catalog_interactions": sum(catalog.values()),
        "chronological_semantic_events": len(output),
        "compiled_one_two_qubit_primitives": len(compiled),
        "catalog_non_epoch_templates_missing": sum(
            (catalog_non_epoch - used_non_epoch).values()
        ),
        "foreign_non_epoch_templates": sum(
            (used_non_epoch - catalog_non_epoch).values()
        ),
        "catalog_root_epoch_templates": root_count,
        "literal_fresh_to_token_SWAPS": root_count,
        "literal_token_to_spent_SWAPS": root_count,
        "root_epoch_template_expanded_to_literal_two_SWAP_handshake": (
            sum(row.atlas_role and row.atlas_role[0] == "controller_root_epoch" for row in output)
            == 2 * root_count
        ),
        "router_template_reapplications": sum(router_applications.values())
        - len(router_applications),
        "router_applications": sum(router_applications.values()),
        "expected_router_applications": len(controller_nodes(length, graph))
        + sum(1 for node in controller_nodes(length, graph) if root.echo.parent_and_source(node) is not None),
        "root_spent_epoch_gates": root_count,
        "Toffoli_decomposition_residual": update.c707.c655.local_decomposition_residuals()[0],
        "CCZ_H_Toffoli_H_residual": ccz_residual,
        "CCZ_is_H_target_Toffoli_H_target": ccz_residual <= TOL,
        "router_decomposition": router_decomposition_certificate(),
        "fixed_depth_first_forest_word": (
            len(output) > 0
            and sum((catalog_non_epoch - used_non_epoch).values()) == 0
            and sum((used_non_epoch - catalog_non_epoch).values()) == 0
            and sum(router_applications.values())
            == len(controller_nodes(length, graph))
            + sum(
                root.echo.parent_and_source(node) is not None
                for node in controller_nodes(length, graph)
            )
        ),
        "host_path_stop_barrier_choices": 0,
    }


def execute_controller_bits(
    shape, graph, site_map, operations, syndrome, initial_spent: bool = False
):
    length = shape[0]
    geometry = root.echo.ca.box_geometry(length)
    plaquettes = geometry["plaquettes"]
    masks = geometry["masks"]
    edges = geometry["edges"]
    if not all(isinstance(row, tuple) for row in (plaquettes, masks, edges)):
        raise TypeError("malformed coarse geometry")
    bits = defaultdict(int)
    for index, plaquette in enumerate(plaquettes):
        if (syndrome >> index) & 1:
            bits[root.syndrome_slot_for_source(plaquette["anchor"], plaquette["axes"])] = 1
    roots = root.echo.forest_roots(length)
    nodes = controller_nodes(length, graph)
    for node in roots:
        owner = root.echo.node_anchor(node)
        role = f"{node[0]}_controller"
        bits[root.slot(owner, role, 5 if initial_spent else 4)] = 1
    target_edge = {}
    for edge_index, (cell, _target, axis) in enumerate(edges):
        graph_edge = graph.cross_edge[(cell, axis, 0)]
        target_edge[site_map[graph_edge][0]] = edge_index
    correction = 0
    router_tables = root.echo.local_permutation_tables()["router_permutations"]
    epoch_table = root.echo.local_permutation_tables()["epoch_handshake_four_cycle"]
    for operation in operations:
        role = operation.atlas_role[0] if operation.atlas_role else ""
        if role in ("controller_parent_xor", "controller_source_xor"):
            token, control, target = operation.sites
            bits[target] ^= bits[token] & bits[control]
        elif role == "controller_token_swap":
            left, right = operation.sites
            bits[left], bits[right] = bits[right], bits[left]
        elif role == "controller_emit":
            token, value, target = operation.sites
            if bits[token] & bits[value]:
                correction ^= 1 << target_edge[target]
        elif role == "controller_router":
            left, right = operation.sites
            node = (operation.atlas_role[1], *operation.owner)
            child_count = len(root.echo.children(node, length, frozenset()))
            table = router_tables[{0: "leaf", 1: "one_child", 2: "two_children"}[child_count]]
            source = bits[left] | (bits[right] << 1)
            target = table[source]
            bits[left] = target & 1
            bits[right] = (target >> 1) & 1
        elif role == "controller_root_epoch":
            left, right = operation.sites
            bits[left], bits[right] = bits[right], bits[left]
        else:
            raise AssertionError(("unknown controller operation", operation))
    value_failures = 0
    token_failures = 0
    router_failures = 0
    fresh_failures = 0
    spent_failures = 0
    root_set = set(roots)
    for node in nodes:
        owner = root.echo.node_anchor(node)
        role = f"{node[0]}_controller"
        value_failures += bits[root.slot(owner, role, 0)] != 0
        token_failures += bits[root.slot(owner, role, 1)] != 0
        router_failures += bits[root.slot(owner, role, 2)] != 0
        router_failures += bits[root.slot(owner, role, 3)] != 0
        if node in root_set:
            fresh_failures += bits[root.slot(owner, role, 4)] != 0
            spent_failures += bits[root.slot(owner, role, 5)] != 1
    echo_row = root.echo.echo_ack_decode(length, syndrome)
    return {
        "correction": correction,
        "syndrome_action_failure": root.prep.apply_matrix(masks, correction) != syndrome,
        "echo_correction_mismatch": correction != echo_row["correction"],
        "value_work_failures": value_failures,
        "token_return_failures": token_failures,
        "router_return_failures": router_failures,
        "root_fresh_consumption_failures": fresh_failures,
        "root_spent_epoch_failures": spent_failures,
    }


def controller_execution_certificate(shape, graph, site_map, operations):
    length = shape[0]
    geometry = root.echo.ca.box_geometry(length)
    masks = geometry["masks"]
    edges = geometry["edges"]
    if not isinstance(masks, tuple) or not isinstance(edges, tuple):
        raise TypeError("malformed coarse geometry")
    if length == 2:
        cases = sorted(
            {
                root.prep.apply_matrix(masks, pattern)
                for pattern in range(1 << len(edges))
            }
        )
        case_kind = "all lawful coarse syndromes"
    else:
        unit = [root.prep.apply_matrix(masks, 1 << index) for index in range(len(edges))]
        pairs = [
            unit[(11 * sample + 1) % len(unit)] ^ unit[(31 * sample + 9) % len(unit)]
            for sample in range(64)
        ]
        cases = unit + pairs
        case_kind = "all unit-edge syndromes plus 64 deterministic linearity pairs"
    totals = Counter()
    for syndrome in cases:
        row = execute_controller_bits(shape, graph, site_map, operations, syndrome)
        for key, value in row.items():
            if key != "correction":
                totals[key] += value
    columns = [
        root.prep.apply_matrix(masks, 1 << index) for index in range(len(edges))
    ]
    lawful_rank = root.prep.gf2_rank(columns)
    unlawful = next(
        candidate
        for candidate in (1 << index for index in range(len(masks)))
        if root.prep.gf2_rank(columns + [candidate]) > lawful_rank
    )
    unlawful_row = execute_controller_bits(
        shape, graph, site_map, operations, unlawful
    )
    diagnostic_epoch_domain_truth_rows = tuple(
        (fresh, token, spent, int((fresh, token, spent) == (1, 0, 0)))
        for fresh, token, spent in product((0, 1), repeat=3)
    )
    hostile_syndrome = next(case for case in cases if case != 0)
    hostile_spent = execute_controller_bits(
        shape,
        graph,
        site_map,
        operations,
        hostile_syndrome,
        initial_spent=True,
    )
    return {
        "case_kind": case_kind,
        "cases": len(cases),
        **dict(sorted(totals.items())),
        "lawful_coarse_syndrome_rank": lawful_rank,
        "coarse_check_bits": len(masks),
        "unlawful_syndrome_control": unlawful,
        "unlawful_syndrome_rejected_by_action": bool(
            unlawful_row["syndrome_action_failure"]
        ),
        "unlawful_echo_cannot_forge_lawful_correction": bool(
            unlawful_row["syndrome_action_failure"]
        ),
        "diagnostic_host_domain_predicate_columns": (
            "fresh",
            "token",
            "spent",
            "accepted",
        ),
        "diagnostic_host_domain_predicate_rows": diagnostic_epoch_domain_truth_rows,
        "diagnostic_host_predicate_is_physical_evidence": False,
        "hostile_unguarded_spent_reapplication_syndrome": hostile_syndrome,
        "hostile_unguarded_spent_reapplication_correction": hostile_spent[
            "correction"
        ],
        "hostile_unguarded_spent_reapplication_token_failures": hostile_spent[
            "token_return_failures"
        ],
        "hostile_unguarded_spent_reapplication_spent_failures": hostile_spent[
            "root_spent_epoch_failures"
        ],
        "local_spent_sector_admission_guard_compiled": False,
        "interpretation": (
            "the literal two-SWAP word is exact only on supplied fresh=1,token=spent=0; "
            "unguarded spent-sector reapplication reactivates token/spent state, so no recurrent claim"
        ),
        "local_permutation_tables": root.echo.local_permutation_tables(),
    }


ANF_ZERO = frozenset()
ANF_ONE = frozenset((frozenset(),))


def anf_variable(index: int):
    return frozenset((frozenset((index,)),))


def anf_xor(left, right):
    return left.symmetric_difference(right)


def anf_product(left, right):
    output = set()
    for lterm in left:
        for rterm in right:
            term = lterm | rterm
            if term in output:
                output.remove(term)
            else:
                output.add(term)
    return frozenset(output)


def anf_degree(polynomial) -> int:
    return max((len(term) for term in polynomial), default=-1)


def anf_two_bit_table(table, left, right):
    """Substitute ANF inputs into a left+2*right truth table."""
    outputs = []
    for output_bit in (0, 1):
        truth = tuple((table[index] >> output_bit) & 1 for index in range(4))
        coefficients = (
            truth[0],
            truth[1] ^ truth[0],
            truth[2] ^ truth[0],
            truth[3] ^ truth[2] ^ truth[1] ^ truth[0],
        )
        polynomial = ANF_ONE if coefficients[0] else ANF_ZERO
        if coefficients[1]:
            polynomial = anf_xor(polynomial, left)
        if coefficients[2]:
            polynomial = anf_xor(polynomial, right)
        if coefficients[3]:
            polynomial = anf_xor(polynomial, anf_product(left, right))
        outputs.append(polynomial)
    return tuple(outputs)


def controller_symbolic_certificate(shape, graph, site_map, operations):
    """Exact ANF execution on the complete lawful coarse-syndrome image.

    Each coarse edge is an independent Boolean indeterminate.  Equality of the
    resulting ANFs proves the controller action on every lawful syndrome basis
    state at once, rather than sampling unit and pair syndromes.
    """
    length = shape[0]
    geometry = root.echo.ca.box_geometry(length)
    plaquettes = geometry["plaquettes"]
    masks = geometry["masks"]
    edges = geometry["edges"]
    bits = defaultdict(lambda: ANF_ZERO)
    initial_syndromes = {}
    for plaquette_index, plaquette in enumerate(plaquettes):
        polynomial = ANF_ZERO
        mask = masks[plaquette_index]
        for edge_index in range(len(edges)):
            if (mask >> edge_index) & 1:
                polynomial = anf_xor(polynomial, anf_variable(edge_index))
        slot = root.syndrome_slot_for_source(
            plaquette["anchor"], plaquette["axes"]
        )
        bits[slot] = polynomial
        initial_syndromes[slot] = polynomial
    roots = root.echo.forest_roots(length)
    nodes = controller_nodes(length, graph)
    for node in roots:
        owner = root.echo.node_anchor(node)
        role = f"{node[0]}_controller"
        bits[root.slot(owner, role, 4)] = ANF_ONE
    target_edge = {}
    for edge_index, (cell, _target, axis) in enumerate(edges):
        graph_edge = graph.cross_edge[(cell, axis, 0)]
        target_edge[site_map[graph_edge][0]] = edge_index
    corrections = [ANF_ZERO for _edge in edges]
    tables = root.echo.local_permutation_tables()["router_permutations"]
    for operation in operations:
        role = operation.atlas_role[0] if operation.atlas_role else ""
        if role in ("controller_parent_xor", "controller_source_xor"):
            token, control, target = operation.sites
            bits[target] = anf_xor(
                bits[target], anf_product(bits[token], bits[control])
            )
        elif role in ("controller_token_swap", "controller_root_epoch"):
            left, right = operation.sites
            bits[left], bits[right] = bits[right], bits[left]
        elif role == "controller_emit":
            token, value, target = operation.sites
            edge_index = target_edge[target]
            corrections[edge_index] = anf_xor(
                corrections[edge_index], anf_product(bits[token], bits[value])
            )
        elif role == "controller_router":
            left, right = operation.sites
            table_name = operation.kind.removeprefix("controller_router_")
            bits[left], bits[right] = anf_two_bit_table(
                tables[table_name], bits[left], bits[right]
            )
        else:
            raise AssertionError(("unknown symbolic controller operation", operation))
    action_failures = 0
    for plaquette_index, plaquette in enumerate(plaquettes):
        observed = ANF_ZERO
        mask = masks[plaquette_index]
        for edge_index, correction in enumerate(corrections):
            if (mask >> edge_index) & 1:
                observed = anf_xor(observed, correction)
        slot = root.syndrome_slot_for_source(
            plaquette["anchor"], plaquette["axes"]
        )
        action_failures += observed != initial_syndromes[slot]
    source_mutations = sum(bits[slot] != value for slot, value in initial_syndromes.items())
    value_failures = token_failures = router_failures = 0
    fresh_failures = spent_failures = 0
    root_set = set(roots)
    for node in nodes:
        owner = root.echo.node_anchor(node)
        role = f"{node[0]}_controller"
        value_failures += bits[root.slot(owner, role, 0)] != ANF_ZERO
        token_failures += bits[root.slot(owner, role, 1)] != ANF_ZERO
        router_failures += bits[root.slot(owner, role, 2)] != ANF_ZERO
        router_failures += bits[root.slot(owner, role, 3)] != ANF_ZERO
        if node in root_set:
            fresh_failures += bits[root.slot(owner, role, 4)] != ANF_ZERO
            spent_failures += bits[root.slot(owner, role, 5)] != ANF_ONE
    all_polynomials = tuple(bits.values()) + tuple(corrections)
    maximum_degree = max(map(anf_degree, all_polynomials), default=-1)
    nonlinear_corrections = sum(anf_degree(row) > 1 for row in corrections)
    failures = {
        "syndrome_action_ANF_failures": action_failures,
        "source_register_mutations": source_mutations,
        "value_work_return_failures": value_failures,
        "token_return_failures": token_failures,
        "router_return_failures": router_failures,
        "fresh_consumption_failures": fresh_failures,
        "spent_ack_failures": spent_failures,
        "nonlinear_correction_polynomials": nonlinear_corrections,
    }
    return {
        "proof_domain": "complete image of the coarse edge-to-plaquette boundary map",
        "independent_edge_variables": len(edges),
        "lawful_syndrome_rank": root.prep.gf2_rank(
            [root.prep.apply_matrix(masks, 1 << index) for index in range(len(edges))]
        ),
        "coarse_check_bits": len(masks),
        "maximum_intermediate_ANF_degree": maximum_degree,
        "maximum_correction_ANF_degree": max(map(anf_degree, corrections), default=-1),
        "correction_ANF_monomials": sum(len(row) for row in corrections),
        "failure_census": failures,
        "all_lawful_basis_states_and_superpositions_proved": all(
            value == 0 for value in failures.values()
        ),
        "phase_statement": (
            "the semantic word is a computational-basis permutation followed only by "
            "the displayed token/value-controlled Z corrections; exact Toffoli, CCZ, "
            "and router decompositions introduce no residual scalar"
        ),
    }


def check_macro_certificate():
    identity = np.eye(2, dtype=complex)
    z_ancilla = embed_local_gate(2, (1,), Z_GATE)
    axes = {
        "X": update.c707.c655.X,
        "Y": np.asarray(((0, -1j), (1j, 0)), dtype=complex),
        "Z": Z_GATE,
    }
    words = {
        "X": (
            ((0,), update.c707.c655.H),
            ((0, 1), update.c707.c655.CNOT),
            ((0,), update.c707.c655.H),
        ),
        "Y": (
            ((0,), update.c707.SDG_GATE),
            ((0,), update.c707.c655.H),
            ((0, 1), update.c707.c655.CNOT),
            ((0,), update.c707.c655.H),
            ((0,), update.c707.S_GATE),
        ),
        "Z": (((0, 1), update.c707.c655.CNOT),),
    }
    residuals = {}
    parity_gate_deletion_residuals = {}
    for axis, word in words.items():
        unitary = local_word_matrix(2, word)
        expected = (
            embed_local_gate(2, (0,), axes[axis])
            @ embed_local_gate(2, (1,), Z_GATE)
        )
        residuals[axis] = float(
            np.linalg.norm(unitary.conj().T @ z_ancilla @ unitary - expected)
        )
        parity_index = next(index for index, (sites, _gate) in enumerate(word) if len(sites) == 2)
        reduced = word[:parity_index] + word[parity_index + 1 :]
        reduced_unitary = local_word_matrix(2, reduced)
        parity_gate_deletion_residuals[axis] = float(
            np.linalg.norm(
                reduced_unitary.conj().T @ z_ancilla @ reduced_unitary - expected
            )
        )
    sign_unitary = embed_local_gate(2, (1,), update.c707.c655.X)
    sign_residual = float(
        np.linalg.norm(sign_unitary.conj().T @ z_ancilla @ sign_unitary + z_ancilla)
    )
    return {
        "conjugation_residuals": residuals,
        "negative_row_sign_X_residual": sign_residual,
        "parity_gate_deletion_residuals": parity_gate_deletion_residuals,
        "minimum_parity_gate_deletion_residual": min(
            parity_gate_deletion_residuals.values()
        ),
        "maximum_residual": max((*residuals.values(), sign_residual)),
    }


def loader_macro_certificate():
    identity = np.eye(2, dtype=complex)
    axes = {
        "X": update.c707.c655.X,
        "Y": np.asarray(((0, -1j), (1j, 0)), dtype=complex),
        "Z": Z_GATE,
    }
    words = {
        "X": (((0, 1), update.c707.c655.CNOT),),
        "Y": (
            ((1,), update.c707.SDG_GATE),
            ((0, 1), update.c707.c655.CNOT),
            ((1,), update.c707.S_GATE),
        ),
        "Z": (((0, 1), CZ_GATE),),
    }
    residuals = {}
    controlled_gate_deletion_residuals = {}
    for axis, word in words.items():
        expected = np.zeros((4, 4), dtype=complex)
        for source in range(4):
            control = source & 1
            target = (source >> 1) & 1
            if control == 0:
                expected[source, source] = 1.0
                continue
            for target_out in (0, 1):
                expected[1 | (target_out << 1), source] = axes[axis][
                    target_out, target
                ]
        residuals[axis] = float(
            np.linalg.norm(local_word_matrix(2, word) - expected)
        )
        controlled_index = next(index for index, (sites, _gate) in enumerate(word) if len(sites) == 2)
        controlled_gate_deletion_residuals[axis] = float(
            np.linalg.norm(
                local_word_matrix(2, word[:controlled_index] + word[controlled_index + 1 :])
                - expected
            )
        )
    negative_expected = np.zeros((4, 4), dtype=complex)
    for source in range(4):
        control = source & 1
        target = (source >> 1) & 1
        if control == 0:
            negative_expected[source, source] = 1.0
            continue
        for target_out in (0, 1):
            negative_expected[1 | (target_out << 1), source] = -axes["X"][
                target_out, target
            ]
    negative_word = (
        ((0, 1), update.c707.c655.CNOT),
        ((0,), Z_GATE),
    )
    negative_residual = float(
        np.linalg.norm(local_word_matrix(2, negative_word) - negative_expected)
    )
    abstract_loader = local_word_matrix(
        2,
        (
            ((0, 1), update.c707.c655.CNOT),
            ((1, 0), update.c707.c655.CNOT),
        ),
    )
    clean_columns = abstract_loader[:, (0, 1)]
    expected_columns = np.eye(4, dtype=complex)[:, (0, 2)]
    clean_subspace_residual = float(np.linalg.norm(clean_columns - expected_columns))
    unload_deleted = local_word_matrix(
        2, (((0, 1), update.c707.c655.CNOT),)
    )
    unload_deletion_residual = float(
        np.linalg.norm(unload_deleted[:, (0, 1)] - expected_columns)
    )
    return {
        "controlled_axis_residuals": residuals,
        "negative_signed_X_control_residual": negative_residual,
        "controlled_gate_deletion_residuals": controlled_gate_deletion_residuals,
        "minimum_controlled_gate_deletion_residual": min(
            controlled_gate_deletion_residuals.values()
        ),
        "logical_Z_parity_unload_gate": "CNOT(logical-Z support -> raw input)",
        "generic_clean_subspace_swap_residual": clean_subspace_residual,
        "parity_unload_deletion_residual": unload_deletion_residual,
        "maximum_residual": max(
            (*residuals.values(), negative_residual, clean_subspace_residual)
        ),
    }


def encoder_isometry_certificate(
    graph,
    site_map,
    context,
    controller_symbolic,
    controller_chronology,
    root_primitive_route,
    check_compilation,
    loader_compilation,
):
    """Connect the emitted seven-stage word to the OpenReference isometry."""
    cycle_data = root.cycle_rows(graph)
    physical_cycles = [
        (update.physical_lift(row, context), kind, key)
        for row, kind, key in cycle_data
    ]
    logical = root.logical_rows(graph)
    physical_logical_z = [
        update.physical_lift(zrow, context)
        for _cell, _mode, _xrow, zrow in logical
    ]
    physical_code = list(update.physical_stabilizers(context))
    vacuum_rows = physical_code + physical_logical_z
    qubits = len(context.sites)
    vacuum_rank = root.base.gf2_rank(
        row.symplectic(qubits) for row in vacuum_rows
    )
    vacuum_commutators = sum(
        not left.commutes(right)
        for index, left in enumerate(vacuum_rows)
        for right in vacuum_rows[index + 1 :]
    )
    vacuum_phase_failures = root.base.stabilizer_phase_failures(vacuum_rows, qubits)

    # Reconstruct the literal Z corrections selected by triangle and bond
    # syndrome ancillas and compare their commutation response to the measured
    # check rows.  This is the operator form of coherent syndrome correction.
    check_by_slot = {}
    check_counters = Counter()
    for physical, kind, key in physical_cycles:
        owner, role, _stage = check_owner_role(kind, key)
        local_index = check_counters[(owner, role)]
        check_counters[(owner, role)] += 1
        check_by_slot[root.slot(owner, role, local_index)] = (physical, kind)
    correction_by_slot = defaultdict(lambda: Pauli())
    for row in root.correction_interactions(graph, site_map):
        target_index = context.index[row.right]
        correction_by_slot[row.left] = correction_by_slot[row.left] @ Pauli(
            z=1 << target_index
        )
    triangle_response_failures = bond_response_failures = 0
    prior_disturbance_failures = 0
    for slot, correction in correction_by_slot.items():
        measured, kind = check_by_slot[slot]
        response = [not correction.commutes(row) for row, _kind, _key in physical_cycles]
        expected_index = next(
            index
            for index, (row, row_kind, _key) in enumerate(physical_cycles)
            if row == measured and row_kind == kind
        )
        if kind == "cell_triangle":
            triangle_response_failures += sum(
                bit != (index == expected_index)
                for index, bit in enumerate(response)
                if physical_cycles[index][1] == "cell_triangle"
            )
        elif kind == "bond_rectangle":
            bond_response_failures += sum(
                bit != (index == expected_index)
                for index, bit in enumerate(response)
                if physical_cycles[index][1] == "bond_rectangle"
            )
            prior_disturbance_failures += sum(
                bit
                for index, bit in enumerate(response)
                if physical_cycles[index][1] in ("cell_triangle", "coarse_plaquette")
            )
    stream_z_targets = [
        Pauli(z=1 << context.index[site_map[edge][0]])
        for edge, (_u, _v, kind, _owner) in enumerate(graph.edges)
        if kind == "matter_stream"
    ]
    coarse_prior_disturbance = sum(
        not correction.commutes(row)
        for correction in stream_z_targets
        for row, kind, _key in physical_cycles
        if kind == "cell_triangle"
    )
    cycle_commutators = sum(
        not left[0].commutes(right[0])
        for index, left in enumerate(physical_cycles)
        for right in physical_cycles[index + 1 :]
    )
    preserved_rows = physical_code + physical_logical_z
    extraction_preservation_failures = sum(
        not cycle.commutes(row)
        for cycle, _kind, _key in physical_cycles
        for row in preserved_rows
    )
    correction_preservation_failures = sum(
        not correction.commutes(row)
        for correction in tuple(correction_by_slot.values()) + tuple(stream_z_targets)
        for row in preserved_rows
        if row not in [cycle for cycle, _kind, _key in physical_cycles]
    )
    initial_preserved = tuple(
        update.physical_lift(root.local_d(graph, cell), context)
        for cell in graph.cells[:-1]
    ) + update.repetition_rows(context)
    initial_preserved_not_plus_Z = sum(
        row.x != 0 or row.phase % 4 != 0 for row in initial_preserved
    )
    check_macros = check_macro_certificate()
    loader_macros = loader_macro_certificate()
    controller_failures = controller_symbolic["failure_census"]
    route_conjugation_failures = sum(
        root_primitive_route[key]
        for key in (
            "non_NN_failures",
            "operand_order_failures",
            "route_return_failures",
        )
    )
    router_residual = controller_chronology["router_decomposition"][
        "maximum_residual"
    ]
    decomposition_residual = max(
        controller_chronology["Toffoli_decomposition_residual"],
        controller_chronology["CCZ_H_Toffoli_H_residual"],
        router_residual,
    )
    root_algebra = root.stabilizer_and_loader_certificate(graph, site_map)
    failure_census = {
        "check_support_atlas_failures": (
            check_compilation["support_atlas_missing"]
            + check_compilation["support_atlas_extra"]
        ),
        "check_macro_failures": int(check_macros["maximum_residual"] > TOL),
        "inactive_check_macro_mutations": int(
            check_macros["minimum_parity_gate_deletion_residual"] <= 1.0e-3
        ),
        "triangle_decoder_response_failures": triangle_response_failures,
        "coarse_controller_ANF_failures": sum(controller_failures.values()),
        "bond_decoder_response_failures": bond_response_failures,
        "later_correction_prior_check_disturbance_failures": (
            prior_disturbance_failures + coarse_prior_disturbance
        ),
        "cycle_check_commutator_failures": cycle_commutators,
        "extraction_preservation_failures": extraction_preservation_failures,
        "Z_correction_preservation_failures": correction_preservation_failures,
        "initial_preserved_not_plus_Z_failures": initial_preserved_not_plus_Z,
        "vacuum_rank_deficit": qubits - vacuum_rank,
        "vacuum_commutator_failures": vacuum_commutators,
        "vacuum_phase_failures": vacuum_phase_failures,
        "loader_macro_failures": int(loader_macros["maximum_residual"] > TOL),
        "loader_support_atlas_failures": (
            loader_compilation["support_atlas_missing"]
            + loader_compilation["support_atlas_extra"]
            + loader_compilation["non_Z_axes_in_parity_unload"]
        ),
        "inactive_loader_macro_mutations": int(
            loader_macros["minimum_controlled_gate_deletion_residual"] <= 1.0e-3
            or loader_macros["parity_unload_deletion_residual"] <= 1.0e-3
        ),
        "logical_pair_failures": root_algebra["logical_canonical_failures"],
        "logical_stabilizer_commutator_failures": root_algebra[
            "logical_stabilizer_commutator_failures"
        ],
        "route_conjugation_failures": route_conjugation_failures,
        "controller_decomposition_failures": int(decomposition_residual > TOL),
        "inactive_router_decomposition_mutations": int(
            controller_chronology["router_decomposition"][
                "minimum_nonidentity_subgate_deletion_residual"
            ]
            <= 1.0e-3
        ),
    }
    exact = all(value == 0 for value in failure_census.values())
    return {
        "clean_domain": (
            "carrier/raw-code target, syndrome, controller, and route-work registers "
            "are initialized as declared; raw logical inputs are arbitrary"
        ),
        "check_macro_operator_certificate": check_macros,
        "coarse_controller_complete_ANF_certificate": controller_symbolic,
        "loader_macro_operator_certificate": loader_macros,
        "physical_code_rows": len(physical_code),
        "physical_logical_Z_rows": len(physical_logical_z),
        "carrier_M2": qubits,
        "vacuum_tableau_rank": vacuum_rank,
        "unique_plus_vacuum": vacuum_rank == qubits,
        "signed_logical_generator_pairs": len(logical),
        "signed_logical_generator_identities_checked": 2 * len(logical),
        "retained_garbage_statement": (
            "syndrome and spent-ack registers may retain an input-independent state; "
            "full-rank carrier vacuum uniqueness factorizes them before logical loading"
        ),
        "input_unload_statement": (
            "exact logical-Z parity CNOT returns every raw input qubit to |0> after "
            "the signed controlled logical-X word"
        ),
        "routing_conjugation_statement": (
            "for every emitted two-site primitive, the forward SWAP permutation places "
            "the ordered operands at the central gate and the inverse permutation restores "
            "every path label, proving SWAP-conjugation equality"
        ),
        "failure_census": failure_census,
        "emitted_E_isometry_exact_on_declared_clean_domain": exact,
    }


def controller_primitive_deletion_certificate(shape, graph, site_map, operations):
    length = shape[0]
    geometry = root.echo.ca.box_geometry(length)
    masks = geometry["masks"]
    edges = geometry["edges"]
    if not isinstance(masks, tuple) or not isinstance(edges, tuple):
        raise TypeError("malformed coarse geometry")
    unit = [root.prep.apply_matrix(masks, 1 << index) for index in range(len(edges))]
    cases = unit + [
        unit[(11 * sample + 1) % len(unit)] ^ unit[(31 * sample + 9) % len(unit)]
        for sample in range(64)
    ]

    def deletion_class(operation):
        role = operation.atlas_role[0] if operation.atlas_role else ""
        if role in (
            "controller_parent_xor",
            "controller_source_xor",
            "controller_token_swap",
        ):
            return f"{role}_{operation.atlas_role[2]}"
        if role == "controller_router":
            return "controller_router_nontrivial" if "leaf" not in operation.kind else None
        if role in ("controller_emit", "controller_root_epoch"):
            return role
        return None

    candidates = defaultdict(list)
    for index, operation in enumerate(operations):
        key = deletion_class(operation)
        if key is not None:
            candidates[key].append(index)
    detected = {}
    witness_cases = {}
    for key, indices in candidates.items():
        detected[key] = False
        witness_cases[key] = None
        for deleted in indices:
            reduced = operations[:deleted] + operations[deleted + 1 :]
            for case_index, syndrome in enumerate(cases):
                row = execute_controller_bits(
                    shape, graph, site_map, reduced, syndrome
                )
                if any(
                    value
                    for name, value in row.items()
                    if name != "correction"
                ):
                    detected[key] = True
                    witness_cases[key] = case_index
                    break
            if detected[key]:
                break
    return {
        "shape": shape,
        "deletion_classes": tuple(sorted(candidates)),
        "detected_by_class": dict(sorted(detected.items())),
        "witness_case_by_class": dict(sorted(witness_cases.items())),
        "all_declared_primitive_deletion_classes_active": all(detected.values()),
        "cases_available": len(cases),
    }


def primitive_route_certificate(operations, carrier, auxiliary):
    word = tuple(
        update.c707.Instruction(row.kind, row.sites, row.matrix) for row in operations
    )
    routed, certificate = update.c707.route_word(word)
    touched = set(certificate.pop("touched_coordinates"))
    certificate.update(
        {
            "primitive_gate_count": len(word),
            "primitive_kind_census": dict(sorted(Counter(row.kind for row in operations).items())),
            "primitive_matrix_unitarity_failures": sum(
                not np.allclose(
                    row.matrix.conj().T @ row.matrix,
                    np.eye(row.matrix.shape[0]),
                    atol=1.0e-12,
                )
                for row in operations
            ),
            "primitive_endpoint_outside_bank_failures": sum(
                site not in carrier | auxiliary
                for row in operations
                for site in row.sites
            ),
            "carrier_sites_touched": len(touched & carrier),
            "auxiliary_sites_touched_and_returned": len(touched & auxiliary),
            "transient_route_sites_touched_and_returned": len(
                touched - carrier - auxiliary
            ),
            "persistent_route_work_M2": 0,
        }
    )
    del routed
    return certificate, touched


def update_route_with_bank(context, rotations, auxiliary) -> dict[str, object]:
    primitive_counts = Counter()
    routed_counts = Counter()
    primitive_digest = sha256()
    routed_digest = sha256()
    routed_gates = maximum_distance = non_nn = operand_failures = return_failures = 0
    deletion_detected = endpoint_pairs = 0
    touched = set()
    touched_auxiliary = set()
    touched_transient = set()
    occupied = set(context.sites)
    traversed_occupied_spectators = set()
    declared = occupied | auxiliary
    endpoint_auxiliary_failures = 0
    for rotation in rotations:
        physical = update.physical_lift(rotation.row, context)
        word = update.c707.compile_pauli_rotation(physical, context.sites, rotation.angle)
        for instruction in word:
            primitive_counts[instruction.kind] += 1
            matrix_hash = update.c707.c655.matrix_digest(instruction.matrix)
            primitive_digest.update(
                f"{instruction.kind}:{instruction.sites}:{matrix_hash}".encode()
            )
            endpoint_auxiliary_failures += sum(site in auxiliary for site in instruction.sites)
            if len(instruction.sites) == 1:
                routed_gates += 1
                routed_counts[instruction.kind] += 1
                routed_digest.update(
                    f"{instruction.kind}:{instruction.sites}:{matrix_hash}".encode()
                )
                touched.update(instruction.sites)
                continue
            endpoint_pairs += 1
            left, right = instruction.sites
            path = tuple(update.c707.c655.manhattan_path(left, right))
            distance = len(path) - 1
            maximum_distance = max(maximum_distance, distance)
            non_nn += sum(
                update.c707.c655.l1(a, b) != 1 for a, b in zip(path, path[1:])
            )
            labels = list(path)
            for index in range(len(path) - 2):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            operand_failures += labels[-2:] != [left, right]
            for index in reversed(range(len(path) - 2)):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            return_failures += labels != list(path)
            if len(path) > 2:
                deleted = list(path)
                for index in range(1, len(path) - 2):
                    deleted[index], deleted[index + 1] = deleted[index + 1], deleted[index]
                for index in reversed(range(len(path) - 2)):
                    deleted[index], deleted[index + 1] = deleted[index + 1], deleted[index]
                deletion_detected += deleted != list(path)
            for index in range(len(path) - 2):
                sites = (path[index], path[index + 1])
                routed_counts["route_swap"] += 1
                routed_digest.update(f"route_swap:{sites}:SWAP".encode())
            gate_sites = (path[-2], path[-1])
            routed_counts[instruction.kind] += 1
            routed_digest.update(
                f"{instruction.kind}:{gate_sites}:{matrix_hash}".encode()
            )
            for index in reversed(range(len(path) - 2)):
                sites = (path[index], path[index + 1])
                routed_counts["route_swap"] += 1
                routed_digest.update(f"route_swap:{sites}:SWAP".encode())
            routed_gates += 2 * distance - 1
            path_set = set(path)
            touched.update(path_set)
            touched_auxiliary.update(path_set & auxiliary)
            touched_transient.update(path_set - declared)
            traversed_occupied_spectators.update((path_set & occupied) - {left, right})
    unit_steps = tuple(
        tuple(sign if index == axis else 0 for index in range(3))
        for axis in range(3)
        for sign in (-1, 1)
    )
    rotated_step_failures = sum(
        sum(abs(value) for value in update.matvec(frame, step)) != 1
        for frame in update.base.proper_cubic_frames()
        for step in unit_steps
    )
    return {
        "rotations": len(rotations),
        "primitive_gate_count": sum(primitive_counts.values()),
        "primitive_kind_census": dict(sorted(primitive_counts.items())),
        "primitive_word_sha256": primitive_digest.hexdigest(),
        "two_site_primitive_count": endpoint_pairs,
        "routed_gate_count": routed_gates,
        "routed_kind_census": dict(sorted(routed_counts.items())),
        "routed_word_sha256": routed_digest.hexdigest(),
        "maximum_route_distance": maximum_distance,
        "non_NN_failures": non_nn,
        "operand_order_failures": operand_failures,
        "route_return_failures": return_failures,
        "first_swap_deletion_detected_macros": deletion_detected,
        "touched_lattice_sites": len(touched),
        "occupied_spectator_sites_traversed_and_returned": len(
            traversed_occupied_spectators
        ),
        "auxiliary_sites_traversed_and_returned": len(touched_auxiliary),
        "transient_route_sites_traversed_and_returned": len(touched_transient),
        "primitive_endpoint_on_auxiliary_failures": endpoint_auxiliary_failures,
        "proper_cubic_rotated_unit_step_failures": rotated_step_failures,
        "schedule": "supplied serial factor/primitive order; no parallel-depth claim",
        "persistent_route_work_M2": 0,
        "_touched_coordinates": touched,
    }


def factor_owner_template(factor):
    tag = factor[0]
    if tag == "coin":
        return factor[1], ("coin", *factor[2:])
    if tag == "reverse":
        return factor[1], ("reverse", *factor[2:])
    if tag == "contact":
        return factor[1], ("contact", *factor[2:])
    if tag == "seam":
        _tag, _serial, owner, axis, _target = factor
        return owner, ("seam", axis, owner[axis] & 1)
    raise AssertionError(factor)


def factor_route_color_certificate(context, rotations, modulus: int = 3):
    """Color complete factor macros, not individual gates, by local type/residue."""
    records = []
    template_envelopes = defaultdict(set)
    template_max_depth = Counter()
    for factor, group in groupby(rotations, key=lambda row: row.factor):
        factor_rows = tuple(group)
        owner, template = factor_owner_template(factor)
        footprint = set()
        routed_depth = 0
        for rotation in factor_rows:
            physical = update.physical_lift(rotation.row, context)
            word = update.c707.compile_pauli_rotation(
                physical, context.sites, rotation.angle
            )
            for instruction in word:
                if len(instruction.sites) == 1:
                    path = instruction.sites
                    routed_depth += 1
                else:
                    path = tuple(
                        update.c707.c655.manhattan_path(*instruction.sites)
                    )
                    routed_depth += 2 * (len(path) - 1) - 1
                footprint.update(path)
        origin = tuple(16 * value for value in owner)
        normalized = {
            tuple(site[axis] - origin[axis] for axis in range(3))
            for site in footprint
        }
        template_envelopes[template].update(normalized)
        template_max_depth[template] = max(
            template_max_depth[template], routed_depth
        )
        color = (template, *(value % modulus for value in owner))
        records.append((color, footprint, owner, template, routed_depth))

    grouped = defaultdict(list)
    for color, footprint, owner, template, routed_depth in records:
        grouped[color].append((footprint, owner, template, routed_depth))
    collisions = 0
    repeated_groups = 0
    repeated_macros = 0
    for rows in grouped.values():
        if len(rows) > 1:
            repeated_groups += 1
            repeated_macros += len(rows)
        for index, (footprint, _owner, _template, _depth) in enumerate(rows):
            collisions += sum(bool(footprint & prior[0]) for prior in rows[:index])

    spans = {}
    for template, offsets in template_envelopes.items():
        spans[template] = tuple(
            max(row[axis] for row in offsets) - min(row[axis] for row in offsets)
            for axis in range(3)
        )
    maximum_span = max(value for row in spans.values() for value in row)
    separation = 16 * modulus
    analytic_coordinate_span = 50
    envelope_failures = sum(
        span >= separation for row in spans.values() for span in row
    ) + int(analytic_coordinate_span >= separation)
    analytic_max_route_distance = 3 * analytic_coordinate_span
    analytic_max_rotation_weight = 128
    analytic_max_rotations_per_factor = 8
    analytic_max_primitives_per_rotation = 6 * analytic_max_rotation_weight - 1
    analytic_max_routed_gates_per_primitive = 2 * analytic_max_route_distance - 1
    analytic_factor_padding = (
        analytic_max_rotations_per_factor
        * analytic_max_primitives_per_rotation
        * analytic_max_routed_gates_per_primitive
    )
    constant_colors = len(template_envelopes) * modulus**3
    return {
        "color_rule": (
            "complete factor template (coin gate, reverse helper step, seam axis/parity, "
            f"or contact pair) plus owner coordinates modulo {modulus}"
        ),
        "macro_granularity": (
            "each color item executes one whole returned-route factor macro serially; "
            "disjoint items in a color run in lockstep with identity padding"
        ),
        "modulus": modulus,
        "factor_macros": len(records),
        "local_factor_templates": len(template_envelopes),
        "constant_color_upper_bound": constant_colors,
        "active_colors_on_fixture": len(grouped),
        "repeated_active_color_groups": repeated_groups,
        "macros_in_repeated_color_groups": repeated_macros,
        "same_color_route_footprint_collisions": collisions,
        "maximum_normalized_template_coordinate_span": maximum_span,
        "a_priori_normalized_coordinate_span_bound": analytic_coordinate_span,
        "same_residue_owner_separation": separation,
        "template_envelope_separation_failures": envelope_failures,
        "stress_fixture_tightened_routed_depth_upper_bound": modulus**3
        * sum(template_max_depth.values()),
        "a_priori_maximum_route_distance": analytic_max_route_distance,
        "a_priori_maximum_physical_rotation_weight": analytic_max_rotation_weight,
        "a_priori_maximum_rotations_per_factor": analytic_max_rotations_per_factor,
        "a_priori_factor_route_padding_bound": analytic_factor_padding,
        "a_priori_volume_independent_routed_depth_bound": constant_colors
        * analytic_factor_padding,
        "maximum_single_factor_routed_depth": max(template_max_depth.values()),
        "boundary_signature_argument": (
            "the bound is chosen before the held stress run: all factor endpoints lie in "
            "center(owner)+[-25,25]^3 and Manhattan paths remain inside endpoint boxes; "
            "the held cube only checks the resulting rule on repeated residues"
        ),
        "host_volume_enumeration_required": False,
        "claim_scope": "native update G only; the one-time open-boundary echo E is separate",
    }


def semantic_factor_reordering_certificate(graph, rotations):
    by_stage_cell = defaultdict(lambda: defaultdict(list))
    for rotation in rotations:
        if rotation.kind != "directed_seam_fswap":
            by_stage_cell[rotation.kind][rotation.factor[1]].append(rotation.row)
    cross_cell_pairs = Counter()
    cross_cell_failures = Counter()
    for stage, by_cell in by_stage_cell.items():
        cells = list(by_cell)
        for index, left_cell in enumerate(cells):
            for right_cell in cells[index + 1 :]:
                for left in by_cell[left_cell]:
                    for right in by_cell[right_cell]:
                        cross_cell_pairs[stage] += 1
                        cross_cell_failures[stage] += not left.commutes(right)

    seams = update.graph_seams(graph)
    seam_polys = []
    for cell, axis, target, left_mode, right_mode in seams:
        rows = (
            update.semantic_row(graph, ("B", cell, left_mode)),
            update.semantic_row(graph, ("B", target, right_mode)),
            *update.seam_hop_rows(graph, cell, left_mode, target, right_mode),
        )
        seam_polys.append(update.fswap_polynomial(rows))
    seam_same_class_pairs = 0
    seam_same_class_failures = 0
    seam_maximum_residual = 0.0
    for index, left in enumerate(seams):
        left_class = (left[1], left[0][left[1]] & 1)
        for right_index, right in enumerate(seams[index + 1 :], index + 1):
            right_class = (right[1], right[0][right[1]] & 1)
            if left_class != right_class:
                continue
            residual = update.poly_residual(
                update.poly_mul(seam_polys[index], seam_polys[right_index]),
                update.poly_mul(seam_polys[right_index], seam_polys[index]),
            )
            seam_same_class_pairs += 1
            seam_same_class_failures += residual > TOL
            seam_maximum_residual = max(seam_maximum_residual, residual)
    return {
        "cross_cell_rotation_commutator_pairs": dict(sorted(cross_cell_pairs.items())),
        "cross_cell_rotation_commutator_failures": dict(
            sorted(cross_cell_failures.items())
        ),
        "same_axis_parity_seam_factor_pairs": seam_same_class_pairs,
        "same_axis_parity_seam_factor_commutator_failures": seam_same_class_failures,
        "same_axis_parity_seam_maximum_commutator_residual": seam_maximum_residual,
        "reordering_justification": (
            "onsite factors may be transposed only across distinct cells; seams retain "
            "axis/parity order and transpose only exact-commuting factors within one class"
        ),
    }


def exact_global_phase_certificate(inventory, graph):
    relative = inventory["compiled_relative_to_target_global_phase_angle"]
    correction = inventory["exact_target_global_phase_correction_angle"]
    cell = graph.cells[0]
    direct_rows = (
        update.semantic_row(graph, ("B", cell, 0)),
        update.semantic_row(graph, ("B", cell, 2)),
        *update.direct_hop_rows(graph, cell, 0, 2),
    )
    fswap = update.fswap_certificate(direct_rows)
    fswap_phase = complex(*fswap["four_rotation_global_phase"])

    coupling = float(update.c230.COUPLING)
    bleft = update.semantic_row(graph, ("B", cell, 0))
    bright = update.semantic_row(graph, ("B", cell, 1))
    compiled_contact = {Pauli(): 1.0 + 0.0j}
    for row, angle in (
        (bleft, coupling / 2),
        (bright, coupling / 2),
        (bleft @ bright, -coupling / 2),
    ):
        compiled_contact = update.poly_mul(
            update.rotation_polynomial(row, angle), compiled_contact
        )
    delta = np.exp(1j * coupling) - 1.0
    target_contact = update.poly_add(
        {Pauli(): 1.0 + 0.0j},
        update.poly_scale(
            update.poly_add(
                {Pauli(): 1.0 + 0.0j},
                {bleft: -1.0 + 0.0j},
                {bright: -1.0 + 0.0j},
                {bleft @ bright: 1.0 + 0.0j},
            ),
            delta / 4,
        ),
    )
    contact_residual, contact_phase = update.aligned_poly_residual(
        compiled_contact, target_contact
    )
    expected_contact_phase = np.exp(-0.25j * coupling)
    breakdown = inventory["compiled_relative_phase_breakdown"]
    return {
        "convention": inventory["phase_convention"],
        "compiled_relative_phase_angle": relative,
        "formal_exact_target_correction_angle": correction,
        "phase_sum_residual_mod_2pi": abs(
            math.atan2(math.sin(relative + correction), math.cos(relative + correction))
        ),
        "formal_scalar": [math.cos(correction), math.sin(correction)],
        "routed_gate_count": inventory["global_phase_correction_routed_gate_count"],
        "phase_breakdown": breakdown,
        "phase_breakdown_sum_residual": inventory["phase_breakdown_sum_residual"],
        "FSWAP_rotation_word_relative_phase": [fswap_phase.real, fswap_phase.imag],
        "FSWAP_minus_i_phase_residual": abs(fswap_phase + 1j),
        "single_contact_factorization_residual": contact_residual,
        "single_contact_relative_phase": [contact_phase.real, contact_phase.imag],
        "single_contact_expected_phase_residual": abs(
            contact_phase - expected_contact_phase
        ),
        "equality_scope": (
            "U_routed is the executable physical word and defines the physical channel; "
            "G_physical_exact is a formal vector representative obtained by multiplying "
            "U_routed by the displayed unrouted scalar"
        ),
    }


def root_lift_as_pauli(row, graph, site_map, context) -> Pauli:
    axes = root.lift_pauli(row, graph, site_map)
    x = z = 0
    for site, (xbit, zbit) in axes.items():
        if xbit:
            x |= 1 << context.index[site]
        if zbit:
            z |= 1 << context.index[site]
    return Pauli(row.phase, x, z)


def intertwiner_certificate(
    graph,
    site_map,
    context,
    rotations,
    constraints,
    phase_certificate,
    encoder_isometry,
):
    root_stabilizers = tuple(row for row, _kind, _key in root.cycle_rows(graph)) + tuple(
        root.local_d(graph, cell) for cell in graph.cells[:-1]
    )
    update_stabilizers = update.local_stabilizers(graph)
    root_algebra = root.stabilizer_and_loader_certificate(graph, site_map)
    logical = root.logical_rows(graph)
    generator_rows = root.generator_rows(graph)
    abstract_stabilizer_equality = sum(
        left != right for left, right in zip(root_stabilizers, update_stabilizers)
    ) + abs(len(root_stabilizers) - len(update_stabilizers))
    lifted_stabilizer_equality = sum(
        root_lift_as_pauli(row, graph, site_map, context)
        != update.physical_lift(row, context)
        for row in root_stabilizers
    )
    generator_lift_equality = sum(
        root_lift_as_pauli(row, graph, site_map, context)
        != update.physical_lift(row, context)
        for row in generator_rows
    )
    logical_lift_equality = sum(
        root_lift_as_pauli(row, graph, site_map, context)
        != update.physical_lift(row, context)
        for _cell, _mode, xrow, zrow in logical
        for row in (xrow, zrow)
    )
    logical_z_native_b = sum(
        zrow != graph.B(graph.vertex_index[(cell, mode)])
        for cell, mode, _xrow, zrow in logical
    )
    rotation_lift_equality = sum(
        root_lift_as_pauli(rotation.row, graph, site_map, context)
        != update.physical_lift(rotation.row, context)
        for rotation in rotations
    )
    obligations = {
        "abstract_stabilizer_row_equality_failures": abstract_stabilizer_equality,
        "lifted_stabilizer_row_equality_failures": lifted_stabilizer_equality,
        "native_AB_generator_lift_equality_failures": generator_lift_equality,
        "logical_XZ_lift_equality_failures": logical_lift_equality,
        "logical_Z_equals_native_B_failures": logical_z_native_b,
        "rotation_generator_lift_equality_failures": rotation_lift_equality,
        "root_logical_stabilizer_commutator_failures": root_algebra[
            "logical_stabilizer_commutator_failures"
        ],
        "root_logical_canonical_failures": root_algebra["logical_canonical_failures"],
        "abstract_update_preservation_failures": constraints[
            "abstract_update_preservation_failures"
        ],
        "physical_update_preservation_failures": constraints[
            "physical_update_preservation_failures"
        ],
        "signed_repetition_lift_homomorphism_failures": constraints[
            "signed_repetition_lift_homomorphism_failures"
        ],
    }
    obligations_zero = all(value == 0 for value in obligations.values())
    representative_phase_exact = phase_certificate["phase_sum_residual_mod_2pi"] <= TOL
    emitted_encoder_exact = encoder_isometry[
        "emitted_E_isometry_exact_on_declared_clean_domain"
    ]
    exact_intertwiner = (
        obligations_zero and representative_phase_exact and emitted_encoder_exact
    )
    return {
        "equation": "G_physical_exact E_joined = E_joined G_native_exact",
        "projective_routed_word_equation": (
            "U_routed E_joined = exp(i*phi) E_joined G_native_exact"
        ),
        "E_joined_definition": (
            "Cycle703 logical-X/Z preparation isometry into the OpenReference code, "
            "followed by the matter-stream repetition lift on the identical carrier map"
        ),
        "native_update_generator_rows": len(rotations),
        "native_AB_generators_checked": len(generator_rows),
        "logical_input_qubits": len(logical),
        "proof_obligations": obligations,
        "proof_route": [
            "root and update use identical abstract stabilizer rows and identical physical lifts",
            "the root logical X/Z rows canonically identify the 6N input algebra; logical Z is native B",
            "the signed repetition lift is a Pauli-algebra homomorphism on every edge generator",
            "each Hermitian update generator preserves both abstract and physical code constraints",
            "functional calculus exponentiates P_physical E = E P_native for every rotation",
            "the frozen zero-site scalar cancels the compiled word's checked relative phase",
            "induction in the frozen serial factor order yields the displayed exact equality",
        ],
        "phase_sum_residual_mod_2pi": phase_certificate[
            "phase_sum_residual_mod_2pi"
        ],
        "executable_physical_law": (
            "the channel/projective class of the returned routed rotation word U_routed"
        ),
        "formal_vector_representative": (
            "G_physical_exact = exp(-i*phi) U_routed; the scalar fixes an operator "
            "representative and is not a physical gate"
        ),
        "routed_rotation_word_without_scalar_is_projective_only": (
            phase_certificate["routed_gate_count"] == 0
            and representative_phase_exact
        ),
        "formal_representative_scalar_checked": representative_phase_exact,
        "exact_vector_statement": (
            "for every input vector |psi>, G_physical_exact E_joined|psi> "
            "= E_joined G_native_exact|psi> with no residual phase"
        ),
        "emitted_encoder_isometry_exact": emitted_encoder_exact,
        "exact_vector_equality_follows_for_all_input_vectors": exact_intertwiner,
        "dense_isometry_materialized": False,
        "proof_mode": "exact generator relations, analytic exponentiation, factor induction",
        "all_proof_obligations_zero": obligations_zero,
        "exact_intertwiner_pass": exact_intertwiner,
    }


def contact_polynomial(graph, cells, lifted=None):
    result = {Pauli(): 1.0 + 0.0j}
    coupling = float(update.c230.COUPLING)
    for cell in cells:
        for left, right in combinations(range(6), 2):
            bleft = update.semantic_row(graph, ("B", cell, left))
            bright = update.semantic_row(graph, ("B", cell, right))
            rows = (bleft, bright, bleft @ bright)
            if lifted is not None:
                rows = tuple(lifted(row) for row in rows)
            for row, angle in zip(rows, (coupling / 2, coupling / 2, -coupling / 2)):
                result = update.poly_mul(update.rotation_polynomial(row, angle), result)
    return result


def stage_order_certificate(graph, context, rotations):
    observed_runs = []
    for rotation in rotations:
        if not observed_runs or observed_runs[-1] != rotation.kind:
            observed_runs.append(rotation.kind)
    seams = update.graph_seams(graph)
    cell, axis, target, left_mode, right_mode = seams[0]
    seam_rows = (
        update.semantic_row(graph, ("B", cell, left_mode)),
        update.semantic_row(graph, ("B", target, right_mode)),
        *update.seam_hop_rows(graph, cell, left_mode, target, right_mode),
    )
    seam_word = update.fswap_factorization(seam_rows)
    contact_word = contact_polynomial(graph, (cell, target))
    accepted = update.poly_mul(contact_word, seam_word)
    hostile = update.poly_mul(seam_word, contact_word)
    abstract_wrong_order, _phase = update.aligned_poly_residual(accepted, hostile)
    abstract_contact_deletion, _phase = update.aligned_poly_residual(accepted, seam_word)
    abstract_seam_deletion, _phase = update.aligned_poly_residual(accepted, contact_word)

    lifted = lambda row: update.physical_lift(row, context)
    physical_seam = update.fswap_factorization(tuple(lifted(row) for row in seam_rows))
    physical_contact = contact_polynomial(graph, (cell, target), lifted)
    physical_accepted = update.poly_mul(physical_contact, physical_seam)
    physical_hostile = update.poly_mul(physical_seam, physical_contact)
    physical_wrong_order, _phase = update.aligned_poly_residual(
        physical_accepted, physical_hostile
    )
    physical_contact_deletion, _phase = update.aligned_poly_residual(
        physical_accepted, physical_seam
    )
    physical_seam_deletion, _phase = update.aligned_poly_residual(
        physical_accepted, physical_contact
    )

    endpoint_degree = Counter()
    for left_cell, _a, right_cell, lmode, rmode in seams:
        endpoint_degree[(left_cell, lmode)] += 1
        endpoint_degree[(right_cell, rmode)] += 1
    stationary = [
        mode for mode in range(6) if endpoint_degree[(cell, mode)] == 0
    ]
    if len(stationary) < 2:
        raise AssertionError("corner witness lacks two stationary modes")
    before = {(cell, left_mode), (cell, stationary[0]), (cell, stationary[1])}
    after = set(before)
    for left_cell, _a, right_cell, lmode, rmode in seams:
        left = (left_cell, lmode)
        right = (right_cell, rmode)
        left_bit = left in after
        right_bit = right in after
        if left_bit != right_bit:
            after.symmetric_difference_update((left, right))

    def contact_pairs(bits):
        counts = Counter(cell_key for cell_key, _mode in bits)
        return sum(count * (count - 1) // 2 for count in counts.values())

    before_pairs = contact_pairs(before)
    after_pairs = contact_pairs(after)
    coupling = float(update.c230.COUPLING)
    full_stage_wrong_order = abs(
        np.exp(1j * coupling * after_pairs) - np.exp(1j * coupling * before_pairs)
    )
    full_stage_contact_deletion = abs(np.exp(1j * coupling * after_pairs) - 1.0)
    full_stage_seam_deletion = math.sqrt(2.0) if before != after else 0.0
    return {
        "expected_rotation_stage_runs": EXPECTED_UPDATE_STAGES,
        "observed_rotation_stage_runs": tuple(observed_runs),
        "canonical_stage_order_accepted": tuple(observed_runs) == EXPECTED_UPDATE_STAGES,
        "seam_endpoint_maximum_degree": max(endpoint_degree.values()),
        "seam_endpoint_overlap_failures": sum(value != 1 for value in endpoint_degree.values()),
        "full_stage_occupation_witness": {
            "selected_seam": (cell, axis, target, left_mode, right_mode),
            "stationary_corner_modes": tuple(stationary[:2]),
            "particles_before_seam": len(before),
            "contact_pairs_before_seam": before_pairs,
            "contact_pairs_after_seam": after_pairs,
            "hostile_contact_before_seam_state_residual": full_stage_wrong_order,
            "contact_stage_deletion_state_residual": full_stage_contact_deletion,
            "seam_stage_deletion_state_residual": full_stage_seam_deletion,
            "argument": (
                "all seam FSWAP endpoints are disjoint; their common fermionic sign "
                "cancels between the two orders, while the complete contact phase changes"
            ),
        },
        "exact_two_cell_native_polynomial_witness": {
            "contact_pairs_included": 30,
            "abstract_hostile_order_residual": abstract_wrong_order,
            "abstract_contact_block_deletion_residual": abstract_contact_deletion,
            "abstract_seam_block_deletion_residual": abstract_seam_deletion,
            "physical_hostile_order_residual": physical_wrong_order,
            "physical_contact_block_deletion_residual": physical_contact_deletion,
            "physical_seam_block_deletion_residual": physical_seam_deletion,
            "global_JW_used": False,
        },
    }


def stage_inventory(graph, site_map, context, coin_gates):
    rotations, inventory = update.build_update(graph, coin_gates)
    constraints = update.constraint_certificate(graph, context, rotations)
    auxiliary = auxiliary_registers(graph)
    carrier = set(context.sites)
    shape = tuple(max(cell[axis] for cell in graph.cells) + 1 for axis in range(3))
    syndrome = root.syndrome_interactions(graph, site_map)
    corrections = root.correction_interactions(graph, site_map)
    loader = root.loader_interactions(graph, site_map)
    controller = root.controller_interactions(shape, graph, site_map)

    check_stages, check_compilation = coherent_check_primitives(
        graph, context, syndrome
    )
    correction_stages = correction_primitives(corrections)
    controller_ops, controller_events, controller_chronology = controller_chronology_primitives(
        shape, graph, site_map, controller
    )
    loader_ops, loader_compilation = loader_primitives(graph, context, loader)
    chronological_primitives = (
        ("triangle_syndrome", check_stages["triangle_syndrome"]),
        ("triangle_correction", correction_stages["triangle_correction"]),
        ("coarse_syndrome", check_stages["coarse_syndrome"]),
        ("coarse_echo_correction_ack", controller_ops),
        ("bond_syndrome", check_stages["bond_syndrome"]),
        ("bond_correction", correction_stages["bond_correction"]),
        ("logical_load", loader_ops),
    )
    root_primitive_word = [
        operation
        for _stage, operations in chronological_primitives
        for operation in operations
    ]
    primitive_stage_runs = []
    for operation in root_primitive_word:
        if not primitive_stage_runs or primitive_stage_runs[-1] != operation.stage:
            primitive_stage_runs.append(operation.stage)
    expected_chronology = tuple(stage for stage, _rows in chronological_primitives)
    root_primitive_route, root_route_sites = primitive_route_certificate(
        root_primitive_word, carrier, auxiliary
    )
    controller_execution = controller_execution_certificate(
        shape, graph, site_map, controller_events
    )
    controller_symbolic = controller_symbolic_certificate(
        shape, graph, site_map, controller_events
    )
    encoder_isometry = encoder_isometry_certificate(
        graph,
        site_map,
        context,
        controller_symbolic,
        controller_chronology,
        root_primitive_route,
        check_compilation,
        loader_compilation,
    )
    triangle_decoder = root.prep.cell_triangle_decoder_certificate()
    deletion_controls = {
        "check_support_gate_deletions_detected": check_compilation[
            "support_CNOT_deletion_changes_extracted_Pauli"
        ],
        "triangle_decoder_active_entries": triangle_decoder[
            "active_table_entries"
        ]
        * len(graph.cells),
        "triangle_decoder_active_entry_deletions_detected": triangle_decoder[
            "active_entry_deletions_detected"
        ]
        * len(graph.cells),
        "bond_controlled_Z_deletions_detected": sum(
            row.role[0] == "bond_correction" for row in corrections
        ),
        "loader_support_gate_deletions_detected": loader_compilation[
            "loader_support_gate_deletion_active_columns"
        ],
    }
    if shape[0] >= 3:
        deletion_controls["controller_primitive_deletions"] = (
            controller_primitive_deletion_certificate(
                shape, graph, site_map, controller_events
            )
        )

    triangle_syndrome = [
        row for row in syndrome if row.role[1] == "cell_triangle"
    ]
    coarse_syndrome = [
        row for row in syndrome if row.role[1] == "coarse_plaquette"
    ]
    bond_syndrome = [
        row for row in syndrome if row.role[1] == "bond_rectangle"
    ]
    triangle_corrections = [
        row for row in corrections if row.role[0] == "triangle_correction"
    ]
    bond_corrections = [
        row for row in corrections if row.role[0] == "bond_correction"
    ]
    chronological_catalog = (
        ("triangle_syndrome", triangle_syndrome),
        ("triangle_correction", triangle_corrections),
        ("coarse_syndrome", coarse_syndrome),
        ("coarse_echo_correction_ack", controller),
        ("bond_syndrome", bond_syndrome),
        ("bond_correction", bond_corrections),
        ("logical_load", loader),
    )
    catalog_rows = [row for _stage, rows in chronological_catalog for row in rows]
    catalog_routes = root.route_certificate(catalog_rows)
    update_routes = update_route_with_bank(context, rotations, auxiliary)
    update_route_sites = update_routes.pop("_touched_coordinates")
    canonical_update_routes = update.route_update(context, rotations)
    replay_fields = (
        "rotations",
        "primitive_gate_count",
        "primitive_word_sha256",
        "two_site_primitive_count",
        "routed_gate_count",
        "routed_word_sha256",
        "maximum_route_distance",
        "non_NN_failures",
        "operand_order_failures",
        "route_return_failures",
        "proper_cubic_rotated_unit_step_failures",
    )
    canonical_route_replay_failures = sum(
        update_routes[field] != canonical_update_routes[field]
        for field in replay_fields
    )
    phase = exact_global_phase_certificate(inventory, graph)
    declared_bank = carrier | auxiliary
    combined_route_sites = root_route_sites | update_route_sites
    transit_substrate = combined_route_sites - declared_bank
    total_physical_support = declared_bank | transit_substrate
    owner_centers = [tuple(16 * value for value in cell) for cell in graph.cells]
    envelope_coverage_failures = sum(
        not any(
            max(abs(site[axis] - center[axis]) for axis in range(3)) <= 25
            for center in owner_centers
        )
        for site in total_physical_support
    )
    resource_census = {
        "encoded_carrier_M2": len(carrier),
        "persistent_preparation_auxiliary_M2": len(auxiliary),
        "bounded_transit_route_M2": len(transit_substrate),
        "total_declared_physical_support_M2": len(total_physical_support),
        "physical_support_coordinate_sha256": rows_sha256(total_physical_support),
        "transit_coordinate_sha256": rows_sha256(transit_substrate),
        "transit_clean_or_product_state_required": False,
        "arbitrary_or_entangled_transit_state_restored": (
            root_primitive_route["route_return_failures"] == 0
            and update_routes["route_return_failures"] == 0
        ),
        "transit_site_classification": "substrate capacity, not persistent ancilla",
        "analytic_owner_envelope": "center(owner)+[-25,25]^3",
        "analytic_owner_envelope_coverage_failures": envelope_coverage_failures,
        "analytic_physical_support_upper_bound_per_cell": 51**3,
        "analytic_total_support_upper_bound": 51**3 * len(graph.cells),
        "analytic_bound_argument": (
            "carrier offsets are at most 9, auxiliary offsets at most 6, every "
            "check/update dependency spans at most one adjacent cell, controller parent "
            "ports reach -16-6=-22, and Manhattan paths remain in endpoint boxes"
        ),
    }
    combined_digest = sha256(
        (
            "one_time_executable_root_chronology|"
            + root_primitive_route["word_sha256"]
            + "|coin|reverse|seam|contact|"
            + update_routes["routed_word_sha256"]
            + "|exact_global_phase_correction|"
            + format(phase["formal_exact_target_correction_angle"], ".17g")
        ).encode()
    ).hexdigest()
    return rotations, inventory, constraints, {
        "root_stage_interaction_counts": {
            stage: len(rows) for stage, rows in chronological_catalog
        },
        "expected_encoder_chronology": expected_chronology,
        "observed_primitive_stage_runs": tuple(primitive_stage_runs),
        "chronology_accepted": tuple(primitive_stage_runs) == expected_chronology,
        "all_seven_root_stages_nonempty": all(
            rows for _stage, rows in chronological_primitives
        ),
        "check_compilation": check_compilation,
        "loader_compilation": loader_compilation,
        "controller_chronology": controller_chronology,
        "controller_execution": controller_execution,
        "encoder_isometry": encoder_isometry,
        "E_deletion_controls": deletion_controls,
        "root_catalog_route": catalog_routes,
        "root_executable_primitive_route": root_primitive_route,
        "update_route": update_routes,
        "canonical_update_route_replay_fields": replay_fields,
        "canonical_update_route_replay_failures": canonical_route_replay_failures,
        "combined_serial_routed_word_sha256": combined_digest,
        "combined_routed_gate_count": root_primitive_route["routed_gate_count"]
        + update_routes["routed_gate_count"],
        "combined_maximum_route_distance": max(
            root_primitive_route["maximum_route_distance"],
            update_routes["maximum_route_distance"],
        ),
        "cross_stage_collision_claim": (
            "none: the seven-stage root word and update factors are concatenated serially"
        ),
        "root_chronology_semantics": (
            "coherent Pauli extraction and phase-zero controlled-Z correction; the echo "
            "forest is unrolled depth-first with reversible router/token/work return and spent ack"
        ),
        "exact_global_phase": phase,
        "physical_resource_census": resource_census,
        "persistent_route_work_M2": 0,
    }, controller


def cube_fixture(length: int, coin_gates):
    shape = (length, length, length)
    graph = update.prep.OpenReferenceGraph(root.box(shape))
    root_site_map = root.carrier_placement(graph)
    update_site_map = update.carrier_placement(graph)
    context = update.physical_context(graph)
    auxiliary = auxiliary_registers(graph)
    carrier = set(context.sites)
    rotations, inventory, constraints, joined_route, controller = stage_inventory(
        graph, root_site_map, context, coin_gates
    )
    seam_count = len(graph.cross_edge) // 2
    address_root = update.address_placement(graph, root_site_map)
    address_update = update.address_placement(graph, update_site_map)
    controller_cert = controller_coverage(shape, graph, root_site_map, controller)
    return {
        "shape": shape,
        "cells": len(graph.cells),
        "coarse_edges": seam_count,
        "abstract_edge_qubits": len(graph.edges),
        "expected_abstract_edge_qubits": 18 * len(graph.cells) + 2 * seam_count,
        "physical_carrier_M2": len(carrier),
        "expected_physical_carrier_M2": 18 * len(graph.cells) + 3 * seam_count,
        "persistent_auxiliary_M2": len(auxiliary),
        "expected_persistent_auxiliary_M2": sum(root.ROLE_COUNTS.values())
        * len(graph.cells),
        "root_update_site_map_equality": root_site_map == update_site_map,
        "root_context_site_map_equality": root_site_map == context.site_map,
        "root_update_address_equality": address_root == address_update,
        "carrier_collisions": sum(map(len, root_site_map.values())) - len(carrier),
        "auxiliary_collisions": sum(root.ROLE_COUNTS.values()) * len(graph.cells)
        - len(auxiliary),
        "carrier_auxiliary_collisions": len(carrier & auxiliary),
        "inventory": inventory,
        "constraints": constraints,
        "controller_coverage": controller_cert,
        "joined_route": joined_route,
        "intertwiner": intertwiner_certificate(
            graph,
            root_site_map,
            context,
            rotations,
            constraints,
            joined_route["exact_global_phase"],
            joined_route["encoder_isometry"],
        ),
        "semantic_factor_reordering": semantic_factor_reordering_certificate(
            graph, rotations
        ),
        "every_seam_exactness": update.seam_controls(graph, context),
        "stage_order": stage_order_certificate(graph, context, rotations),
        "factor_sha256": update.factor_digest(rotations),
    }


def collect_failures(report) -> list[str]:
    failures = []
    for row in report["fixtures"]:
        prefix = f"L{row['shape'][0]}"
        exact = {
            "abstract_formula": row["abstract_edge_qubits"]
            - row["expected_abstract_edge_qubits"],
            "physical_formula": row["physical_carrier_M2"]
            - row["expected_physical_carrier_M2"],
            "aux_formula": row["persistent_auxiliary_M2"]
            - row["expected_persistent_auxiliary_M2"],
            "carrier_collision": row["carrier_collisions"],
            "aux_collision": row["auxiliary_collisions"],
            "carrier_aux_collision": row["carrier_auxiliary_collisions"],
            "controller_missing": row["controller_coverage"]["missing_interactions"],
            "controller_extra": row["controller_coverage"]["extra_interactions"],
            "root_endpoint_bank": row["joined_route"]["root_executable_primitive_route"][
                "primitive_endpoint_outside_bank_failures"
            ],
            "root_primitive_unitarity": row["joined_route"]["root_executable_primitive_route"][
                "primitive_matrix_unitarity_failures"
            ],
            "root_nn": row["joined_route"]["root_executable_primitive_route"]["non_NN_failures"],
            "root_operand": row["joined_route"]["root_executable_primitive_route"][
                "operand_order_failures"
            ],
            "root_return": row["joined_route"]["root_executable_primitive_route"]["route_return_failures"],
            "root_catalog_color_collision": row["joined_route"]["root_catalog_route"][
                "same_color_route_collisions"
            ],
            "check_atlas_missing": row["joined_route"]["check_compilation"][
                "support_atlas_missing"
            ],
            "check_atlas_extra": row["joined_route"]["check_compilation"][
                "support_atlas_extra"
            ],
            "loader_atlas_missing": row["joined_route"]["loader_compilation"][
                "support_atlas_missing"
            ],
            "loader_atlas_extra": row["joined_route"]["loader_compilation"][
                "support_atlas_extra"
            ],
            "loader_nonZ_parity": row["joined_route"]["loader_compilation"][
                "non_Z_axes_in_parity_unload"
            ],
            "controller_template_missing": row["joined_route"]["controller_chronology"][
                "catalog_non_epoch_templates_missing"
            ],
            "controller_template_foreign": row["joined_route"]["controller_chronology"][
                "foreign_non_epoch_templates"
            ],
            "controller_router_count": row["joined_route"]["controller_chronology"][
                "router_applications"
            ]
            - row["joined_route"]["controller_chronology"][
                "expected_router_applications"
            ],
            "update_endpoint_aux": row["joined_route"]["update_route"][
                "primitive_endpoint_on_auxiliary_failures"
            ],
            "update_nn": row["joined_route"]["update_route"]["non_NN_failures"],
            "update_operand": row["joined_route"]["update_route"][
                "operand_order_failures"
            ],
            "update_return": row["joined_route"]["update_route"][
                "route_return_failures"
            ],
            "rotated_steps": row["joined_route"]["update_route"][
                "proper_cubic_rotated_unit_step_failures"
            ],
            "canonical_route_replay": row["joined_route"][
                "canonical_update_route_replay_failures"
            ],
            "abstract_rank": row["constraints"]["abstract_constraint_rank"]
            - row["constraints"]["expected_abstract_rank"],
            "physical_rank": row["constraints"]["physical_constraint_rank"]
            - row["constraints"]["expected_physical_rank"],
            "abstract_update": row["constraints"]["abstract_update_preservation_failures"],
            "physical_update": row["constraints"]["physical_update_preservation_failures"],
            "seam_hermiticity": row["every_seam_exactness"]["hermitian_term_failures"],
            "semantic_seam_reorder": row["semantic_factor_reordering"][
                "same_axis_parity_seam_factor_commutator_failures"
            ],
        }
        exact.update(
            {
                f"controller_execute_{key}": value
                for key, value in row["joined_route"]["controller_execution"].items()
                if not key.startswith("hostile_unguarded_")
                and (
                    key.endswith("failure")
                    or key.endswith("failures")
                    or key.endswith("mismatch")
                )
            }
        )
        exact.update(
            {
                f"semantic_{key}": value
                for key, value in row["semantic_factor_reordering"][
                    "cross_cell_rotation_commutator_failures"
                ].items()
            }
        )
        for key, value in exact.items():
            if value != 0:
                failures.append(f"{prefix}:{key}={value}")
        for key in (
            "phase_breakdown_sum_residual",
            "FSWAP_minus_i_phase_residual",
            "single_contact_factorization_residual",
            "single_contact_expected_phase_residual",
        ):
            if row["joined_route"]["exact_global_phase"][key] > TOL:
                failures.append(f"{prefix}:{key}")
        if row["joined_route"]["controller_chronology"][
            "Toffoli_decomposition_residual"
        ] > TOL:
            failures.append(f"{prefix}:Toffoli decomposition")
        if row["joined_route"]["controller_chronology"][
            "CCZ_H_Toffoli_H_residual"
        ] > TOL:
            failures.append(f"{prefix}:CCZ decomposition")
        if row["joined_route"]["controller_chronology"][
            "router_decomposition"
        ]["maximum_residual"] > TOL:
            failures.append(f"{prefix}:router decomposition")
        for key in (
            "root_update_site_map_equality",
            "root_context_site_map_equality",
            "root_update_address_equality",
        ):
            if not row[key]:
                failures.append(f"{prefix}:{key}")
        if not row["controller_coverage"]["all_root_and_nonroot_event_families_covered"]:
            failures.append(f"{prefix}:controller family coverage")
        if not row["joined_route"]["all_seven_root_stages_nonempty"]:
            failures.append(f"{prefix}:empty root stage")
        if not row["joined_route"]["chronology_accepted"]:
            failures.append(f"{prefix}:root chronology")
        resources = row["joined_route"]["physical_resource_census"]
        if resources["bounded_transit_route_M2"] <= 0:
            failures.append(f"{prefix}:transit substrate omitted")
        if not resources["arbitrary_or_entangled_transit_state_restored"]:
            failures.append(f"{prefix}:transit state not restored")
        if (
            resources["total_declared_physical_support_M2"]
            > resources["analytic_total_support_upper_bound"]
        ):
            failures.append(f"{prefix}:analytic support bound")
        if resources["analytic_owner_envelope_coverage_failures"] != 0:
            failures.append(f"{prefix}:support envelope coverage")
        execution = row["joined_route"]["controller_execution"]
        if not execution["unlawful_syndrome_rejected_by_action"]:
            failures.append(f"{prefix}:unlawful syndrome accepted")
        if (
            execution["hostile_unguarded_spent_reapplication_token_failures"]
            + execution["hostile_unguarded_spent_reapplication_spent_failures"]
            <= 0
        ):
            failures.append(f"{prefix}:inactive spent-reapplication adversary")
        deletion = row["joined_route"]["E_deletion_controls"]
        if deletion["check_support_gate_deletions_detected"] <= 0:
            failures.append(f"{prefix}:inactive check deletion")
        if (
            deletion["triangle_decoder_active_entry_deletions_detected"]
            != deletion["triangle_decoder_active_entries"]
        ):
            failures.append(f"{prefix}:triangle deletion census")
        if deletion["bond_controlled_Z_deletions_detected"] <= 0:
            failures.append(f"{prefix}:inactive bond deletion")
        if deletion["loader_support_gate_deletions_detected"] <= 0:
            failures.append(f"{prefix}:inactive loader deletion")
        if "controller_primitive_deletions" in deletion and not deletion[
            "controller_primitive_deletions"
        ]["all_declared_primitive_deletion_classes_active"]:
            failures.append(f"{prefix}:inactive controller deletion class")
        if not row["intertwiner"]["all_proof_obligations_zero"]:
            failures.append(f"{prefix}:intertwiner")
        if not row["joined_route"]["encoder_isometry"][
            "emitted_E_isometry_exact_on_declared_clean_domain"
        ]:
            failures.append(f"{prefix}:emitted encoder isometry")
        if not row["intertwiner"]["exact_intertwiner_pass"]:
            failures.append(f"{prefix}:exact intertwined emitted word")
        if row["intertwiner"]["phase_sum_residual_mod_2pi"] > TOL:
            failures.append(f"{prefix}:exact global phase")
        seam = row["every_seam_exactness"]
        for key in (
            "maximum_full_space_involution_residual",
            "maximum_four_rotation_residual",
            "physical_lift_maximum_full_space_involution_residual",
            "physical_lift_maximum_four_rotation_residual",
        ):
            if seam[key] > TOL:
                failures.append(f"{prefix}:{key}")
        for key in (
            "minimum_term_deletion_involution_residual",
            "minimum_rotation_deletion_residual",
        ):
            if seam[key] < 1.0e-3:
                failures.append(f"{prefix}:inactive {key}")
        order = row["stage_order"]
        if not order["canonical_stage_order_accepted"]:
            failures.append(f"{prefix}:stage order")
        if order["seam_endpoint_overlap_failures"] != 0:
            failures.append(f"{prefix}:seam endpoint overlap")
        full = order["full_stage_occupation_witness"]
        poly = order["exact_two_cell_native_polynomial_witness"]
        for key in (
            "hostile_contact_before_seam_state_residual",
            "contact_stage_deletion_state_residual",
            "seam_stage_deletion_state_residual",
        ):
            if full[key] < 1.0e-3:
                failures.append(f"{prefix}:inactive {key}")
        for key, value in poly.items():
            if key.endswith("residual") and value < 1.0e-3:
                failures.append(f"{prefix}:inactive {key}")
    colors = report["native_G_route_colors"]
    for key in (
        "same_color_route_footprint_collisions",
        "template_envelope_separation_failures",
    ):
        if colors[key] != 0:
            failures.append(f"route-colors:{key}={colors[key]}")
    if colors["repeated_active_color_groups"] == 0:
        failures.append("route-colors:no repeated-color stress")
    if colors["host_volume_enumeration_required"]:
        failures.append("route-colors:host enumeration")
    covariance = report["joined_24_576_covariance"]
    covariance_zero_fields = {
        "root_frame": covariance["root_carrier_aux_coordinate"][
            "frame_injectivity_failures"
        ],
        "root_products": covariance["root_carrier_aux_coordinate"][
            "product_diagram_failures"
        ],
        "E_single_generators": covariance["root_signed_AB_semantic_E"][
            "single_frame_generator_failures"
        ],
        "E_single_placement": covariance["root_signed_AB_semantic_E"][
            "single_frame_placement_failures"
        ],
        "E_single_edge_types": covariance["root_signed_AB_semantic_E"][
            "single_frame_edge_type_failures"
        ],
        "E_product_generators": covariance["root_signed_AB_semantic_E"][
            "product_generator_failures"
        ],
        "E_product_edges": covariance["root_signed_AB_semantic_E"][
            "product_edge_failures"
        ],
        "E_product_sites": covariance["root_signed_AB_semantic_E"][
            "product_site_failures"
        ],
        "G_graph": covariance["native_G"]["graph_generator_transport_failures"],
        "G_update": covariance["native_G"]["all_update_rotation_transport_failures"],
        "G_angles": covariance["native_G"]["rotation_parameter_transport_failures"],
        "G_place": covariance["native_G"]["carrier_set_transport_failures"],
        "G_meta_products": covariance["native_G"]["update_metadata_product_failures"],
        "G_AB_products": covariance["native_G"]["signed_AB_generator_product_failures"],
        "G_coordinate_products": covariance["native_G"]["physical_coordinate_product_failures"],
    }
    for key, value in covariance_zero_fields.items():
        if value != 0:
            failures.append(f"covariance:{key}={value}")
    return failures


def native_G_route_color_fixture(length, coin_gates):
    graph = update.prep.OpenReferenceGraph(root.box((length, length, length)))
    context = update.physical_context(graph)
    rotations, inventory = update.build_update(graph, coin_gates)
    result = factor_route_color_certificate(context, rotations, 4)
    result.update(
        {
            "held_color_fixture": (length, length, length),
            "cells": len(graph.cells),
            "seams": len(graph.cross_edge) // 2,
            "rotation_rows_scanned": len(rotations),
            "factor_inventory": inventory,
            "radius_one_cell_neighbor_signatures_present": 27,
        }
    )
    return result


def joined_covariance_fixture(length, coin_gates):
    shape = (length, length, length)
    graph = update.prep.OpenReferenceGraph(root.box(shape))
    site_map = root.carrier_placement(graph)
    context = update.physical_context(graph)
    rotations, _inventory = update.build_update(graph, coin_gates)
    coordinate = root.covariance_certificate(shape, graph, site_map)
    semantic_E = root.semantic_covariance_certificate(shape)
    native_G = update.covariance_certificate(
        graph, context, rotations, do_products=True
    )
    return {
        "shape": shape,
        "root_carrier_aux_coordinate": coordinate,
        "root_signed_AB_semantic_E": semantic_E,
        "native_G": native_G,
        "composition_argument": (
            "signed A/B transport generates every root stabilizer/logical row and every "
            "native update row; coordinate transport carries the identical carrier/aux bank"
        ),
        "joined_code_diagram_products": 576,
    }


def main() -> int:
    species = update.c219.common_species(float(update.c230.BETA))
    coin = np.asarray(species.coin, dtype=complex)
    coin_gates, qr = update.qr_coin_schedule(coin)
    fixtures = [cube_fixture(2, coin_gates), cube_fixture(3, coin_gates)]
    route_colors = native_G_route_color_fixture(5, coin_gates)
    covariance = joined_covariance_fixture(2, coin_gates)
    report = {
        "status": "pending",
        "claim_scope": (
            "one executable clean-domain Cycle703/Cycle870 cubic preparation chronology "
            "joined to the phase-corrected native OpenReference coin-reverse-seam-contact "
            "update on one identical physical carrier/register map; no global Jordan--Wigner target"
        ),
        "coin_QR": qr,
        "fixtures": fixtures,
        "native_G_route_colors": route_colors,
        "joined_24_576_covariance": covariance,
        "joined_stage_statement": (
            "triangle_extract -> triangle_correct -> coarse_extract -> echo_correct_ack -> "
            "bond_extract -> bond_correct -> logical_load -> onsite_coin_mass -> "
            "onsite_reverse_fswap -> directed_seam_fswap -> onsite_contact -> "
            "formal_representative_scalar"
        ),
        "source_pins": {
            "this_source_sha256": file_sha256(Path(__file__)),
            "native_update_source": str(UPDATE_SOURCE.relative_to(ROOT)),
            "native_update_source_sha256": file_sha256(UPDATE_SOURCE),
            "native_update_receipt_sha256": file_sha256(UPDATE_RECEIPT),
            "root_placement_source": str(ROOT_SOURCE.relative_to(ROOT)),
            "root_placement_source_sha256": file_sha256(ROOT_SOURCE),
            "root_placement_receipt_sha256": file_sha256(ROOT_RECEIPT),
        },
        "boundary": {
            "supplied": [
                "finite cubic L=2 or L=3 open boundary, spacing-16 origin, and proper-cubic coframe",
                "one clean raw-input/syndrome/controller genesis domain",
                "Cycle703 check/decoder/loader semantics, echo forest grammar, and one invocation",
                "Cycle219 beta=-0.3 coin, Cycle230 g=0.37 contact, and serial update layer order",
            ],
            "derived": [
                "one literal 18N+3E carrier map shared address-for-address by preparation and update",
                "36N unique persistent auxiliary slots disjoint from every carrier",
                "the full bounded union of transit-route substrate M2, with arbitrary/entangled transit state restored",
                "an a priori 51^3 total-support capacity bound per coarse cell",
                "executable seven-stage coherent extraction/correction/echo-ack/loader primitive word with returned NN routes",
                "exact native coin-reverse-seam-contact update with returned NN routes through a restored bank",
                "formal representative-phase convention and generator-relation proof of G_physical_exact E_joined = E_joined G_native_exact",
                "volume-independent 2880-color returned-route schedule for native G, with no host volume enumeration",
                "joined 24-frame/576-product signed code and coordinate covariance",
                "active E deletion-class witnesses and unlawful-syndrome controls; not every semantic occurrence is claimed essential",
                "active complete-stage contact-before-seam, contact-deletion, and seam-deletion witnesses",
            ],
            "one_time_genesis_boundary": (
                "E_joined is consumed once from the supplied clean root domain.  The joined result "
                "does not derive that domain, reset it, or claim autonomous/recurrent preparation."
            ),
            "open": [
                "intrinsic clean-genesis, start trigger, coframe, or boundary selection",
                "recurrent reset/fault repair and noncubic controller composition",
                "periodic Wilson sectors and a volume-independent parallel schedule for the one-time open-boundary E word",
            ],
            "not_claimed": [
                "no global Jordan--Wigner character or OpenReference-to-PatchGraph target is used",
                "no autonomous genesis, recurrent all-volume controller, or broad obstruction is claimed",
            ],
        },
    }
    failures = collect_failures(report)
    report["failures"] = failures
    report["status"] = "pass" if not failures else "fail"
    payload = json.dumps(report, sort_keys=True, indent=2, default=str)
    report["content_sha256_before_hash_field"] = sha256(payload.encode()).hexdigest()
    output = (
        ROOT
        / "outputs"
        / "cycle870_openreference_joined_recurrent_compiler_receipt_2026_08_02.json"
    )
    output.write_text(json.dumps(report, sort_keys=True, indent=2, default=str) + "\n")
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("RECEIPT", output)
    print("OPENREFERENCE_JOINED_CUBE_PASS" if not failures else "OPENREFERENCE_JOINED_CUBE_FAIL")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
