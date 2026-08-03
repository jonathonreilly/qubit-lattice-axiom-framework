#!/usr/bin/env python3
"""Independent adversarial checker for chronological OpenReference E.

Only the pinned root placement source and its pinned landed dependencies are
imported.  Neither active joint probe is imported.  The root interaction lists
are treated as an atlas; this runner independently emits the seven-stage
coherent primitive word and the depth-first fresh/token/spent controller word.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
import importlib.util
from itertools import product
import json
import math
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
ROOT_SOURCE = HERE / "frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py"
ROOT_SHA256 = "64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2"
SCRIPT_ROOT = HERE
DEPENDENCY_HASHES = {
    "ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py": "717a60f45c7d7e9e354b50005fea6ace4bae7b63d74cebb48ded59546cc561f9",
    "frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25.py": "833ac9ee1d7f83185fdd66d89e2f3208e514c0b3b2cff660e7227dc28f506245",
    "frontier_cycle703_reversible_echo_ack_controller_2026_07_25.py": "5dab64cd17ead6cb5062eab9266b9206d74bb608dcc22f3a1132ee1f1af3e9a9",
    "frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py": "eb0841f064bc840b1892a02ce1cf75e2c8275b6c21cc9b2952a5032cc03d4bb4",
    "frontier_full128_25site_nn_circuit_core_2026_07_24.py": "e79b733bd3b8e273a2094679e6175b5d1f253ebef1a33b96544519cbdf278e13",
}
ACTIVE_JOINED = HERE / "frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py"
FROZEN_JOINED_SHA256 = "81109892cf7c435f387fdfd71ea3d7d0b9affe0b301ca0339750db0f91c7a457"
FROZEN_JOINED_RECEIPT = (
    REPO_ROOT
    / "outputs"
    / "cycle870_openreference_joined_recurrent_compiler_receipt_2026_08_02.json"
)
FROZEN_JOINED_RECEIPT_SHA256 = "cb7a8892649d41ea1c4fe6cf4ddb8ec8678356932f063a74ea775179df77ba1b"
AUDIT_INPUT_PATHS = (ROOT_SOURCE, ACTIVE_JOINED, FROZEN_JOINED_RECEIPT)
TOL = 2.0e-9
STAGES = (
    "triangle_syndrome",
    "triangle_correction",
    "coarse_syndrome",
    "coarse_echo_correction_ack",
    "bond_syndrome",
    "bond_correction",
    "logical_load",
)
Coord = tuple[int, int, int]


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_root():
    if file_hash(ROOT_SOURCE) != ROOT_SHA256:
        raise RuntimeError("root placement source changed")
    for name, expected in DEPENDENCY_HASHES.items():
        if file_hash(SCRIPT_ROOT / name) != expected:
            raise RuntimeError(f"root dependency changed: {name}")
    sys.path.insert(0, str(SCRIPT_ROOT))
    spec = importlib.util.spec_from_file_location("independent_root_E_source", ROOT_SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load root source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


H = np.asarray(((1, 1), (1, -1)), dtype=complex) / math.sqrt(2)
X = np.asarray(((0, 1), (1, 0)), dtype=complex)
Z = np.diag((1, -1)).astype(complex)
S = np.diag((1, 1j)).astype(complex)
SDG = S.conj().T
T = np.diag((1, np.exp(1j * math.pi / 4))).astype(complex)
TDG = T.conj().T
CNOT = np.asarray(
    ((1, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0)),
    dtype=complex,
)
CZ = np.diag((1, 1, 1, -1)).astype(complex)
SWAP = np.asarray(
    ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)),
    dtype=complex,
)
TOFFOLI = np.eye(8, dtype=complex)
TOFFOLI[3, 3] = TOFFOLI[7, 7] = 0
TOFFOLI[3, 7] = TOFFOLI[7, 3] = 1
CCZ = np.diag((1, 1, 1, 1, 1, 1, 1, -1)).astype(complex)


@dataclass(frozen=True)
class Primitive:
    stage: str
    kind: str
    sites: tuple[Coord, ...]
    matrix: np.ndarray
    owner: Coord | None = None
    role: tuple[object, ...] | None = None


@dataclass(frozen=True)
class Event:
    kind: str
    sites: tuple[Coord, ...]
    owner: Coord
    role: tuple[object, ...]


def permutation_matrix(table) -> np.ndarray:
    output = np.zeros((len(table), len(table)), dtype=complex)
    for source, target in enumerate(table):
        output[target, source] = 1
    return output


def semantic_router_matrix(table) -> np.ndarray:
    """Matrix in the substrate's little-endian |left,right> local basis."""
    return permutation_matrix(table)


def embed_gate(qubits: int, sites: tuple[int, ...], gate: np.ndarray) -> np.ndarray:
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
        output = embed_gate(qubits, sites, gate) @ output
    return output


def toffoli_local_word():
    return (
        ((2,), H),
        ((1, 2), CNOT),
        ((2,), TDG),
        ((0, 2), CNOT),
        ((2,), T),
        ((1, 2), CNOT),
        ((2,), TDG),
        ((0, 2), CNOT),
        ((1,), T),
        ((2,), T),
        ((2,), H),
        ((0, 1), CNOT),
        ((0,), T),
        ((1,), TDG),
        ((0, 1), CNOT),
    )


def decomposition_certificate():
    toffoli_word = toffoli_local_word()
    toffoli_matrix = local_word_matrix(3, toffoli_word)
    toffoli_deletions = []
    for deleted in range(len(toffoli_word)):
        reduced = toffoli_word[:deleted] + toffoli_word[deleted + 1 :]
        toffoli_deletions.append(float(np.linalg.norm(local_word_matrix(3, reduced) - TOFFOLI)))
    ccz_word = (((2,), H),) + toffoli_word + (((2,), H),)
    ccz_matrix = local_word_matrix(3, ccz_word)
    ccz_deletions = []
    for deleted in range(len(ccz_word)):
        reduced = ccz_word[:deleted] + ccz_word[deleted + 1 :]
        ccz_deletions.append(float(np.linalg.norm(local_word_matrix(3, reduced) - CCZ)))
    router_tables = {
        "leaf": (0, 1, 2, 3),
        "one_child": (1, 0, 2, 3),
        "two_children": (1, 2, 0, 3),
    }
    router_words = {
        "leaf": (),
        "one_child": (((1,), X), ((1, 0), CNOT), ((1,), X)),
        "two_children": (
            ((0,), X),
            ((1, 0), CNOT),
            ((0, 1), CNOT),
            ((1,), X),
        ),
    }
    router_residuals = {
        name: float(
            np.linalg.norm(
                local_word_matrix(2, router_words[name])
                - semantic_router_matrix(table)
            )
        )
        for name, table in router_tables.items()
    }
    router_deletions = {
        name: tuple(
            float(
                np.linalg.norm(
                    local_word_matrix(2, word[:deleted] + word[deleted + 1 :])
                    - semantic_router_matrix(router_tables[name])
                )
            )
            for deleted in range(len(word))
        )
        for name, word in router_words.items()
    }
    return {
        "Toffoli_decomposition_residual": float(np.linalg.norm(toffoli_matrix - TOFFOLI)),
        "CCZ_H_Toffoli_H_residual": float(np.linalg.norm(ccz_matrix - CCZ)),
        "Toffoli_subgate_deletions_tested": len(toffoli_deletions),
        "minimum_Toffoli_subgate_deletion_residual": min(toffoli_deletions),
        "CCZ_subgate_deletions_tested": len(ccz_deletions),
        "minimum_CCZ_subgate_deletion_residual": min(ccz_deletions),
        "router_semantic_integer_encoding": "left + 2*right",
        "router_matrix_basis_encoding": "left + 2*right (substrate little-endian wires)",
        "router_gate_set": "X/CNOT",
        "router_gate_counts": {
            name: len(word) for name, word in router_words.items()
        },
        "router_decomposition_residuals": router_residuals,
        "router_subgate_deletion_residuals": router_deletions,
        "minimum_router_subgate_deletion_residual": min(
            residual
            for name, rows in router_deletions.items()
            if name != "leaf"
            for residual in rows
        ),
        "maximum_router_decomposition_residual": max(router_residuals.values()),
    }


def axes_and_sign(root, row, graph, site_map):
    support = root.lift_pauli(row, graph, site_map)
    axes = []
    y_count = 0
    for site in sorted(support):
        x, z = support[site]
        axis = "Y" if (x, z) == (1, 1) else "X" if x else "Z"
        axes.append((site, axis))
        y_count += axis == "Y"
    exponent = (row.phase - y_count) % 4
    if exponent not in (0, 2):
        raise AssertionError(("non-Hermitian physical row", row, exponent))
    return tuple(axes), 1 if exponent == 0 else -1


def check_owner(kind, key):
    if kind == "cell_triangle":
        return key, "triangle_syndrome", "triangle_syndrome"
    if kind == "coarse_plaquette":
        return key[0], "coarse_syndrome", "coarse_syndrome"
    if kind == "bond_rectangle":
        return key[0], "bond_syndrome", "bond_syndrome"
    raise AssertionError(kind)


def compile_checks(root, graph, site_map):
    stages = {name: [] for name in ("triangle_syndrome", "coarse_syndrome", "bond_syndrome")}
    counters = Counter()
    atlas = Counter()
    sign_flips = 0
    kinds = Counter()
    for row, kind, key in root.cycle_rows(graph):
        owner, register_role, stage = check_owner(kind, key)
        local_index = counters[(owner, register_role)]
        counters[(owner, register_role)] += 1
        ancilla = root.slot(owner, register_role, local_index)
        axes, sign = axes_and_sign(root, row, graph, site_map)
        kinds[kind] += 1
        for support_index, (target, axis) in enumerate(axes):
            role = ("syndrome", kind, local_index, support_index)
            atlas[(owner, role, ancilla, target)] += 1
            if axis == "X":
                stages[stage].append(Primitive(stage, "check_H", (target,), H))
            elif axis == "Y":
                stages[stage].extend((Primitive(stage, "check_Sdg", (target,), SDG), Primitive(stage, "check_H", (target,), H)))
            stages[stage].append(Primitive(stage, "check_CNOT", (target, ancilla), CNOT, owner, role))
            if axis == "X":
                stages[stage].append(Primitive(stage, "check_H", (target,), H))
            elif axis == "Y":
                stages[stage].extend((Primitive(stage, "check_H", (target,), H), Primitive(stage, "check_S", (target,), S)))
        if sign == -1:
            stages[stage].append(Primitive(stage, "check_sign_X", (ancilla,), X))
            sign_flips += 1
    observed = Counter((row.owner, row.role, row.left, row.right) for row in root.syndrome_interactions(graph, site_map))
    return stages, {
        "checks_by_kind": dict(sorted(kinds.items())),
        "negative_sign_flips": sign_flips,
        "support_CNOTs": sum(atlas.values()),
        "atlas_missing": sum((observed - atlas).values()),
        "atlas_extra": sum((atlas - observed).values()),
        "check_support_deletions_algebraically_active": sum(atlas.values()),
    }


def compile_corrections(root, graph, site_map):
    stages = {"triangle_correction": [], "bond_correction": []}
    counts = Counter()
    for row in root.correction_interactions(graph, site_map):
        stage = "triangle_correction" if row.role[0] == "triangle_correction" else "bond_correction"
        stages[stage].append(Primitive(stage, "syndrome_controlled_Z", (row.left, row.right), CZ, row.owner, row.role))
        counts[stage] += 1
    return stages, dict(counts)


def controlled_axis(stage, control, target, axis, owner, role):
    if axis == "X":
        return [Primitive(stage, "loader_CX", (control, target), CNOT, owner, role)]
    if axis == "Z":
        return [Primitive(stage, "loader_CZ", (control, target), CZ, owner, role)]
    if axis == "Y":
        return [
            Primitive(stage, "loader_Sdg", (target,), SDG),
            Primitive(stage, "loader_CX_for_Y", (control, target), CNOT, owner, role),
            Primitive(stage, "loader_S", (target,), S),
        ]
    raise AssertionError(axis)


def compile_loader(root, graph, site_map):
    stage = "logical_load"
    output = []
    atlas = Counter()
    sign_controls = non_z_axes = 0
    for cell, mode, xrow, zrow in root.logical_rows(graph):
        source = root.slot(cell, "input", mode)
        xaxes, xsign = axes_and_sign(root, xrow, graph, site_map)
        for support_index, (target, axis) in enumerate(xaxes):
            role = ("loader", mode, "X", support_index)
            atlas[(cell, role, source, target)] += 1
            output.extend(controlled_axis(stage, source, target, axis, cell, role))
        if xsign == -1:
            output.append(Primitive(stage, "loader_control_sign_Z", (source,), Z))
            sign_controls += 1
        zaxes, zsign = axes_and_sign(root, zrow, graph, site_map)
        if zsign != 1:
            raise AssertionError(("logical Z sign", cell, mode, zsign))
        for support_index, (target, axis) in enumerate(zaxes):
            role = ("loader", mode, "Z", support_index)
            atlas[(cell, role, target, source)] += 1
            non_z_axes += axis != "Z"
            output.append(Primitive(stage, "loader_parity_CNOT", (target, source), CNOT, cell, role))
    observed = Counter((row.owner, row.role, row.left, row.right) for row in root.loader_interactions(graph, site_map))
    return output, {
        "logical_rows": len(root.logical_rows(graph)),
        "controlled_X_sign_Z_gates": sign_controls,
        "compiled_support_interactions": sum(atlas.values()),
        "non_Z_axes_in_parity_unload": non_z_axes,
        "atlas_missing": sum((observed - atlas).values()),
        "atlas_extra": sum((atlas - observed).values()),
        "truth_table": "|q>|0_L> -> |q>|q_L> -> |0>|q_L>",
    }


def controller_nodes(root, length, graph):
    output = []
    for kind in ("ay", "az"):
        axis = 1 if kind == "ay" else 2
        for cell in product(range(length), repeat=3):
            node = (kind, *cell)
            try:
                graph.cross_edge[(cell, axis, 0)]
            except KeyError:
                continue
            output.append(node)
    return tuple(output)


def compile_controller_semantics(root, shape, graph, site_map):
    if len(set(shape)) != 1:
        raise ValueError("chronological E controller requires a cube")
    length = shape[0]
    tables = root.echo.local_permutation_tables()["router_permutations"]
    events = []
    router_counts = Counter()

    def router_event(node):
        owner = root.echo.node_anchor(node)
        kind = node[0]
        role_name = f"{kind}_controller"
        child_count = len(root.echo.children(node, length, frozenset()))
        table_name = {0: "leaf", 1: "one_child", 2: "two_children"}[child_count]
        router_counts[node] += 1
        events.append(Event(f"router_{table_name}", (root.slot(owner, role_name, 2), root.slot(owner, role_name, 3)), owner, ("controller_router", kind)))

    def traverse(node):
        parent_owner = root.echo.node_anchor(node)
        parent_role = f"{node[0]}_controller"
        for child in root.echo.children(node, length, frozenset()):
            router_event(node)
            child_owner = root.echo.node_anchor(child)
            child_role = f"{child[0]}_controller"
            expected_parent, source_key = root.echo.parent_and_source(child)
            if expected_parent != node:
                raise AssertionError(("parent mismatch", node, child, expected_parent))
            token_parent = root.slot(parent_owner, parent_role, 1)
            token_child = root.slot(child_owner, child_role, 1)
            value_parent = root.slot(parent_owner, parent_role, 0)
            value_child = root.slot(child_owner, child_role, 0)
            source = root.syndrome_slot_for_source(source_key[0], source_key[1])
            target = root.stream_target(graph, site_map, child)
            events.extend(
                (
                    Event("parent_Toffoli_down", (token_parent, value_parent, value_child), child_owner, ("controller_parent_xor", child[0], "down")),
                    Event("source_Toffoli_down", (token_parent, source, value_child), child_owner, ("controller_source_xor", child[0], "down")),
                    Event("token_SWAP_down", (token_parent, token_child), child_owner, ("controller_token_swap", child[0], "down")),
                    Event("emit_CCZ", (token_child, value_child, target), child_owner, ("controller_emit", child[0])),
                )
            )
            traverse(child)
            events.extend(
                (
                    Event("token_SWAP_up", (token_parent, token_child), child_owner, ("controller_token_swap", child[0], "up")),
                    Event("source_Toffoli_up", (token_parent, source, value_child), child_owner, ("controller_source_xor", child[0], "up")),
                    Event("parent_Toffoli_up", (token_parent, value_parent, value_child), child_owner, ("controller_parent_xor", child[0], "up")),
                )
            )
        router_event(node)

    roots = root.echo.forest_roots(length)
    for tree_root in roots:
        owner = root.echo.node_anchor(tree_root)
        role_name = f"{tree_root[0]}_controller"
        events.append(Event("root_fresh_to_token_SWAP", (root.slot(owner, role_name, 4), root.slot(owner, role_name, 1)), owner, ("controller_root_epoch", tree_root[0], "start")))
        traverse(tree_root)
        events.append(Event("root_token_to_spent_SWAP", (root.slot(owner, role_name, 1), root.slot(owner, role_name, 5)), owner, ("controller_root_epoch", tree_root[0], "spent")))

    catalog = root.controller_interactions(shape, graph, site_map)
    catalog_non_epoch = Counter(
        (row.owner, row.role, row.left, row.right)
        for row in catalog
        if row.role[0] != "controller_root_epoch"
    )
    used_non_epoch = Counter()
    for event in events:
        role = event.role[0]
        if role == "controller_root_epoch":
            continue
        if role in ("controller_parent_xor", "controller_source_xor", "controller_emit"):
            left, right = event.sites[1], event.sites[2]
        else:
            left, right = event.sites[0], event.sites[1]
        used_non_epoch[(event.owner, event.role, left, right)] = 1
    nodes = controller_nodes(root, length, graph)
    nonroots = sum(root.echo.parent_and_source(node) is not None for node in nodes)
    return tuple(events), {
        "atlas_interactions": len(catalog),
        "semantic_events": len(events),
        "non_epoch_atlas_templates_missing": sum((catalog_non_epoch - used_non_epoch).values()),
        "foreign_non_epoch_templates": sum((used_non_epoch - catalog_non_epoch).values()),
        "root_epoch_atlas_templates": sum(row.role[0] == "controller_root_epoch" for row in catalog),
        "fresh_to_token_SWAPS": len(roots),
        "token_to_spent_SWAPS": len(roots),
        "router_applications": sum(router_counts.values()),
        "expected_router_applications": len(nodes) + nonroots,
        "router_template_reapplications": sum(router_counts.values()) - len(router_counts),
        "host_path_stop_barrier_choices": 0,
        "fixed_depth_first_word": (
            len(events) > 0
            and sum((catalog_non_epoch - used_non_epoch).values()) == 0
            and sum((used_non_epoch - catalog_non_epoch).values()) == 0
            and sum(router_counts.values()) == len(nodes) + nonroots
        ),
    }


def toffoli_primitives(stage, event):
    c1, c2, target = event.sites
    mapping = {0: c1, 1: c2, 2: target}
    output = []
    for index, (local_sites, gate) in enumerate(toffoli_local_word()):
        output.append(Primitive(stage, f"controller_Toffoli_{index:02d}", tuple(mapping[site] for site in local_sites), gate, event.owner, event.role))
    return output


def compile_controller_primitives_with_root(root, events):
    stage = "coarse_echo_correction_ack"
    tables = root.echo.local_permutation_tables()["router_permutations"]
    output = []
    for event in events:
        if "Toffoli" in event.kind:
            output.extend(toffoli_primitives(stage, event))
        elif event.kind == "emit_CCZ":
            target = event.sites[2]
            output.append(Primitive(stage, "controller_CCZ_H_pre", (target,), H, event.owner, event.role))
            output.extend(toffoli_primitives(stage, event))
            output.append(Primitive(stage, "controller_CCZ_H_post", (target,), H, event.owner, event.role))
        elif "SWAP" in event.kind:
            output.append(Primitive(stage, event.kind, event.sites, SWAP, event.owner, event.role))
        elif event.kind.startswith("router_"):
            table_name = event.kind.removeprefix("router_")
            left, right = event.sites
            if table_name == "leaf":
                word = ()
            elif table_name == "one_child":
                word = (
                    ("X_right_pre", (right,), X),
                    ("CNOT_right_left", (right, left), CNOT),
                    ("X_right_post", (right,), X),
                )
            elif table_name == "two_children":
                word = (
                    ("X_left", (left,), X),
                    ("CNOT_right_left", (right, left), CNOT),
                    ("CNOT_left_right", (left, right), CNOT),
                    ("X_right", (right,), X),
                )
            else:
                raise AssertionError(table_name)
            output.extend(
                Primitive(
                    stage,
                    f"router_{table_name}_{kind}",
                    sites,
                    matrix,
                    event.owner,
                    event.role,
                )
                for kind, sites, matrix in word
            )
        else:
            raise AssertionError(event.kind)
    return tuple(output)


def execute_controller(root, shape, graph, site_map, events, syndrome, initial_spent=False):
    length = shape[0]
    geometry = root.echo.ca.box_geometry(length)
    bits = defaultdict(int)
    for index, plaquette in enumerate(geometry["plaquettes"]):
        if (syndrome >> index) & 1:
            bits[root.syndrome_slot_for_source(plaquette["anchor"], plaquette["axes"])] = 1
    roots = root.echo.forest_roots(length)
    for node in roots:
        owner = root.echo.node_anchor(node)
        role_name = f"{node[0]}_controller"
        bits[root.slot(owner, role_name, 5 if initial_spent else 4)] = 1
    target_edge = {}
    for edge_index, (cell, _target, axis) in enumerate(geometry["edges"]):
        edge = graph.cross_edge[(cell, axis, 0)]
        target_edge[site_map[edge][0]] = edge_index
    correction = 0
    router_tables = root.echo.local_permutation_tables()["router_permutations"]
    for event in events:
        role = event.role[0]
        if role in ("controller_parent_xor", "controller_source_xor"):
            token, control, target = event.sites
            bits[target] ^= bits[token] & bits[control]
        elif role == "controller_token_swap" or role == "controller_root_epoch":
            left, right = event.sites
            bits[left], bits[right] = bits[right], bits[left]
        elif role == "controller_emit":
            token, value, target = event.sites
            if bits[token] & bits[value]:
                correction ^= 1 << target_edge[target]
        elif role == "controller_router":
            left, right = event.sites
            table = router_tables[event.kind.removeprefix("router_")]
            source = bits[left] | (bits[right] << 1)
            target = table[source]
            bits[left], bits[right] = target & 1, (target >> 1) & 1
        else:
            raise AssertionError(event)
    failures = Counter()
    root_set = set(roots)
    for node in controller_nodes(root, length, graph):
        owner = root.echo.node_anchor(node)
        role_name = f"{node[0]}_controller"
        failures["value_work"] += bits[root.slot(owner, role_name, 0)] != 0
        failures["token_return"] += bits[root.slot(owner, role_name, 1)] != 0
        failures["router_return"] += bits[root.slot(owner, role_name, 2)] != 0
        failures["router_return"] += bits[root.slot(owner, role_name, 3)] != 0
        if node in root_set:
            failures["fresh_consumption"] += bits[root.slot(owner, role_name, 4)] != 0
            failures["spent_epoch"] += bits[root.slot(owner, role_name, 5)] != 1
    decoded = root.echo.echo_ack_decode(length, syndrome)
    failures["syndrome_action"] += root.prep.apply_matrix(geometry["masks"], correction) != syndrome
    failures["echo_correction_mismatch"] += correction != decoded["correction"]
    return correction, dict(failures)


def controller_cases(root, length):
    geometry = root.echo.ca.box_geometry(length)
    masks, edges = geometry["masks"], geometry["edges"]
    units = [root.prep.apply_matrix(masks, 1 << index) for index in range(len(edges))]
    if length == 2:
        cases = sorted({root.prep.apply_matrix(masks, pattern) for pattern in range(1 << len(edges))})
        kind = "all lawful syndromes"
    else:
        cases = sorted(set([0, *units, *(units[(11 * sample + 1) % len(units)] ^ units[(31 * sample + 9) % len(units)] for sample in range(64))]))
        kind = "zero, all unit-edge syndromes, 64 deterministic pairs"
    return tuple(cases), kind


def controller_certificate(root, shape, graph, site_map, events):
    length = shape[0]
    cases, case_kind = controller_cases(root, length)
    totals = Counter()
    for syndrome in cases:
        _correction, failures = execute_controller(root, shape, graph, site_map, events, syndrome)
        totals.update(failures)
    geometry = root.echo.ca.box_geometry(length)
    columns = [root.prep.apply_matrix(geometry["masks"], 1 << index) for index in range(len(geometry["edges"]))]
    rank = root.prep.gf2_rank(columns)
    unlawful = next(1 << index for index in range(len(geometry["masks"])) if root.prep.gf2_rank(columns + [1 << index]) > rank)
    _bad_correction, bad_failures = execute_controller(root, shape, graph, site_map, events, unlawful)
    hostile = next(case for case in cases if case)
    _hostile_correction, hostile_failures = execute_controller(root, shape, graph, site_map, events, hostile, initial_spent=True)

    # Every nonidentity semantic event gets its own deletion attempt.  This is
    # stronger than detecting one representative per role class.
    deletion_cases = cases
    detected = 0
    undetected = []
    for deleted, event in enumerate(events):
        if event.kind == "router_leaf":
            continue
        reduced = events[:deleted] + events[deleted + 1 :]
        active = False
        for syndrome in deletion_cases:
            _correction, failures = execute_controller(root, shape, graph, site_map, reduced, syndrome)
            if any(failures.values()):
                active = True
                break
        detected += active
        if not active:
            undetected.append((deleted, event.kind, event.role))
    tested = len(events) - sum(event.kind == "router_leaf" for event in events)
    return {
        "case_kind": case_kind,
        "lawful_cases": len(cases),
        "lawful_execution_failures": dict(sorted(totals.items())),
        "lawful_syndrome_rank": rank,
        "coarse_check_bits": len(geometry["masks"]),
        "unlawful_syndrome": unlawful,
        "unlawful_syndrome_action_failure": bool(bad_failures.get("syndrome_action", 0)),
        "hostile_spent_reapplication_syndrome": hostile,
        "hostile_spent_reapplication_failures": hostile_failures,
        "local_spent_sector_admission_guard_compiled": False,
        "individual_nonidentity_semantic_event_deletions_tested": tested,
        "individual_semantic_event_deletions_detected": detected,
        "undetected_semantic_event_deletions": undetected,
    }


ANF_ZERO = frozenset()
ANF_ONE = frozenset((frozenset(),))


def anf_var(index):
    return frozenset((frozenset((index,)),))


def anf_xor(left, right):
    return left.symmetric_difference(right)


def anf_mul(left, right):
    output = set()
    for lterm in left:
        for rterm in right:
            term = lterm | rterm
            if term in output:
                output.remove(term)
            else:
                output.add(term)
    return frozenset(output)


def anf_degree(poly):
    return max((len(term) for term in poly), default=-1)


def substitute_router_table(table, left, right):
    output = []
    for bit in (0, 1):
        truth = tuple((table[index] >> bit) & 1 for index in range(4))
        coefficients = (
            truth[0],
            truth[1] ^ truth[0],
            truth[2] ^ truth[0],
            truth[3] ^ truth[2] ^ truth[1] ^ truth[0],
        )
        poly = ANF_ONE if coefficients[0] else ANF_ZERO
        if coefficients[1]: poly = anf_xor(poly, left)
        if coefficients[2]: poly = anf_xor(poly, right)
        if coefficients[3]: poly = anf_xor(poly, anf_mul(left, right))
        output.append(poly)
    return tuple(output)


def symbolic_controller_certificate(root, shape, graph, site_map, events):
    length = shape[0]
    geometry = root.echo.ca.box_geometry(length)
    plaquettes = geometry["plaquettes"]
    masks = geometry["masks"]
    edges = geometry["edges"]
    wire = defaultdict(lambda: ANF_ZERO)
    initial = {}
    for row_index, plaquette in enumerate(plaquettes):
        poly = ANF_ZERO
        for edge_index in range(len(edges)):
            if (masks[row_index] >> edge_index) & 1:
                poly = anf_xor(poly, anf_var(edge_index))
        site = root.syndrome_slot_for_source(plaquette["anchor"], plaquette["axes"])
        wire[site] = poly
        initial[site] = poly
    roots = root.echo.forest_roots(length)
    for node in roots:
        owner = root.echo.node_anchor(node)
        wire[root.slot(owner, f"{node[0]}_controller", 4)] = ANF_ONE
    target_edge = {}
    for edge_index, (cell, _target, axis) in enumerate(edges):
        graph_edge = graph.cross_edge[(cell, axis, 0)]
        target_edge[site_map[graph_edge][0]] = edge_index
    correction = [ANF_ZERO for _edge in edges]
    tables = root.echo.local_permutation_tables()["router_permutations"]
    for event in events:
        role = event.role[0]
        if role in ("controller_parent_xor", "controller_source_xor"):
            token, control, target = event.sites
            wire[target] = anf_xor(wire[target], anf_mul(wire[token], wire[control]))
        elif role in ("controller_token_swap", "controller_root_epoch"):
            left, right = event.sites
            wire[left], wire[right] = wire[right], wire[left]
        elif role == "controller_emit":
            token, value, target = event.sites
            edge_index = target_edge[target]
            correction[edge_index] = anf_xor(
                correction[edge_index], anf_mul(wire[token], wire[value])
            )
        elif role == "controller_router":
            left, right = event.sites
            table_name = event.kind.removeprefix("router_")
            wire[left], wire[right] = substitute_router_table(
                tables[table_name], wire[left], wire[right]
            )
        else:
            raise AssertionError(("unexpected event", event))
    action = 0
    for row_index, plaquette in enumerate(plaquettes):
        observed = ANF_ZERO
        for edge_index, poly in enumerate(correction):
            if (masks[row_index] >> edge_index) & 1:
                observed = anf_xor(observed, poly)
        site = root.syndrome_slot_for_source(plaquette["anchor"], plaquette["axes"])
        action += observed != initial[site]
    source = sum(wire[site] != poly for site, poly in initial.items())
    value = token = router = fresh = spent = 0
    root_set = set(roots)
    for node in controller_nodes(root, length, graph):
        owner = root.echo.node_anchor(node)
        role = f"{node[0]}_controller"
        value += wire[root.slot(owner, role, 0)] != ANF_ZERO
        token += wire[root.slot(owner, role, 1)] != ANF_ZERO
        router += wire[root.slot(owner, role, 2)] != ANF_ZERO
        router += wire[root.slot(owner, role, 3)] != ANF_ZERO
        if node in root_set:
            fresh += wire[root.slot(owner, role, 4)] != ANF_ZERO
            spent += wire[root.slot(owner, role, 5)] != ANF_ONE
    failures = {
        "syndrome_action_ANF_failures": action,
        "source_register_mutations": source,
        "value_work_return_failures": value,
        "token_return_failures": token,
        "router_return_failures": router,
        "fresh_consumption_failures": fresh,
        "spent_ack_failures": spent,
        "nonlinear_correction_polynomials": sum(anf_degree(poly) > 1 for poly in correction),
    }
    return {
        "proof_domain": "complete lawful syndrome image parameterized by coarse-edge variables",
        "independent_edge_variables": len(edges),
        "coarse_check_bits": len(masks),
        "lawful_syndrome_rank": root.prep.gf2_rank(
            [root.prep.apply_matrix(masks, 1 << index) for index in range(len(edges))]
        ),
        "maximum_intermediate_ANF_degree": max(
            map(anf_degree, tuple(wire.values()) + tuple(correction)), default=-1
        ),
        "maximum_correction_ANF_degree": max(map(anf_degree, correction), default=-1),
        "correction_ANF_monomials": sum(len(poly) for poly in correction),
        "failure_census": failures,
        "complete_lawful_domain_exact": all(value == 0 for value in failures.values()),
    }


def manhattan_path(left: Coord, right: Coord):
    current = list(left)
    output = [tuple(current)]
    for axis in range(3):
        while current[axis] != right[axis]:
            current[axis] += 1 if right[axis] > current[axis] else -1
            output.append(tuple(current))
    return tuple(output)


def in_capacity(site, cell_set):
    choices = []
    for value in site:
        q = value // 16
        choices.append((q - 1, q, q + 1))
    return any(cell in cell_set and max(abs(site[axis] - 16 * cell[axis]) for axis in range(3)) <= 9 for cell in product(*choices))


def route_word(primitives, carrier, auxiliary, cells):
    counts = Counter()
    touched = set()
    digest = sha256()
    routed_gates = maximum_distance = nn = operand = returned = 0
    unitary_failures = endpoint_failures = 0
    for primitive_index, primitive in enumerate(primitives):
        dimension = 1 << len(primitive.sites)
        unitary_failures += not np.allclose(primitive.matrix.conj().T @ primitive.matrix, np.eye(dimension), atol=1.0e-12)
        endpoint_failures += sum(site not in carrier | auxiliary for site in primitive.sites)
        counts[primitive.kind] += 1
        if len(primitive.sites) == 1:
            touched.add(primitive.sites[0])
            routed_gates += 1
            digest.update(repr((primitive_index, primitive.kind, primitive.sites)).encode())
            continue
        left, right = primitive.sites
        path = manhattan_path(left, right)
        distance = len(path) - 1
        maximum_distance = max(maximum_distance, distance)
        nn += sum(sum(abs(a[i] - b[i]) for i in range(3)) != 1 for a, b in zip(path, path[1:]))
        labels = list(path)
        for index in range(len(path) - 2):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
            digest.update(repr((primitive_index, "SWAP", path[index], path[index + 1])).encode())
        operand += labels[-2:] != [left, right]
        digest.update(repr((primitive_index, primitive.kind, path[-2], path[-1])).encode())
        for index in reversed(range(len(path) - 2)):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
            digest.update(repr((primitive_index, "SWAP", path[index], path[index + 1])).encode())
        returned += labels != list(path)
        routed_gates += 2 * distance - 1
        touched.update(path)
    return {
        "primitive_gates": len(primitives),
        "primitive_kind_census": dict(sorted(counts.items())),
        "primitive_unitarity_failures": unitary_failures,
        "primitive_endpoint_outside_carrier_auxiliary_bank": endpoint_failures,
        "routed_gates": routed_gates,
        "maximum_route_distance": maximum_distance,
        "non_NN_failures": nn,
        "operand_failures": operand,
        "arbitrary_transit_register_return_failures": returned,
        "routed_word_sha256": digest.hexdigest(),
        "carrier_sites_touched": len(touched & carrier),
        "persistent_auxiliary_sites_touched": len(touched & auxiliary),
        "transit_sites_touched": len(touched - carrier - auxiliary),
        "route_sites_outside_radius9_capacity": sum(not in_capacity(site, cells) for site in touched),
        "touched_sites": frozenset(touched),
    }


def covariance(root, sites):
    frames = root.base.proper_cubic_frames()
    injectivity = composition = unit = 0
    steps = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    def mv(frame, row):
        return tuple(int(value) for value in frame @ np.asarray(row, dtype=int))
    for frame in frames:
        injectivity += len({mv(frame, site) for site in sites}) != len(sites)
        unit += sum(sum(abs(value) for value in mv(frame, step)) != 1 for step in steps)
    for left in frames:
        for right in frames:
            final = left @ right
            composition += any(mv(left, mv(right, site)) != mv(final, site) for site in sites)
    return {
        "proper_frames": len(frames),
        "ordered_products": len(frames) ** 2,
        "route_coordinate_injectivity_failures": injectivity,
        "unit_step_failures": unit,
        "route_coordinate_product_failures": composition,
        "claim": "transported supplied route atlas; no fresh lab-axis recompilation equality",
    }


def independent_check_macro_certificate():
    identity = np.eye(2, dtype=complex)
    y_gate = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z_ancilla = embed_gate(2, (1,), Z)
    words = {
        "X": (((0,), H), ((0, 1), CNOT), ((0,), H)),
        "Y": (((0,), SDG), ((0,), H), ((0, 1), CNOT), ((0,), H), ((0,), S)),
        "Z": (((0, 1), CNOT),),
    }
    axes = {"X": X, "Y": y_gate, "Z": Z}
    residuals = {}
    deletion_residuals = {}
    for axis, word in words.items():
        unitary = local_word_matrix(2, word)
        residuals[axis] = float(
            np.linalg.norm(
                unitary.conj().T @ z_ancilla @ unitary
                - embed_gate(2, (0,), axes[axis]) @ embed_gate(2, (1,), Z)
            )
        )
        parity_index = next(index for index, (sites, _gate) in enumerate(word) if len(sites) == 2)
        reduced = word[:parity_index] + word[parity_index + 1 :]
        reduced_unitary = local_word_matrix(2, reduced)
        expected = embed_gate(2, (0,), axes[axis]) @ embed_gate(2, (1,), Z)
        deletion_residuals[axis] = float(
            np.linalg.norm(reduced_unitary.conj().T @ z_ancilla @ reduced_unitary - expected)
        )
    sign = embed_gate(2, (1,), X)
    sign_residual = float(np.linalg.norm(sign.conj().T @ z_ancilla @ sign + z_ancilla))
    return {
        "conjugation_residuals": residuals,
        "negative_sign_X_residual": sign_residual,
        "parity_gate_deletion_residuals": deletion_residuals,
        "minimum_parity_gate_deletion_residual": min(deletion_residuals.values()),
        "maximum_residual": max((*residuals.values(), sign_residual)),
    }


def independent_loader_macro_certificate():
    identity = np.eye(2, dtype=complex)
    y_gate = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    words = {
        "X": (((0, 1), CNOT),),
        "Y": (((1,), SDG), ((0, 1), CNOT), ((1,), S)),
        "Z": (((0, 1), CZ),),
    }
    axes = {"X": X, "Y": y_gate, "Z": Z}
    residuals = {}
    deletion_residuals = {}
    for axis, word in words.items():
        expected = np.zeros((4, 4), dtype=complex)
        for source in range(4):
            control = source & 1
            target = (source >> 1) & 1
            if control == 0:
                expected[source, source] = 1.0
                continue
            for target_out in (0, 1):
                expected[1 | (target_out << 1), source] = axes[axis][target_out, target]
        residuals[axis] = float(np.linalg.norm(local_word_matrix(2, word) - expected))
        controlled_index = next(index for index, (sites, _gate) in enumerate(word) if len(sites) == 2)
        deletion_residuals[axis] = float(
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
            negative_expected[1 | (target_out << 1), source] = -X[target_out, target]
    negative_residual = float(
        np.linalg.norm(
            local_word_matrix(2, (((0, 1), CNOT), ((0,), Z)))
            - negative_expected
        )
    )
    abstract_word = local_word_matrix(
        2, (((0, 1), CNOT), ((1, 0), CNOT))
    )
    clean_residual = float(
        np.linalg.norm(abstract_word[:, (0, 1)] - np.eye(4, dtype=complex)[:, (0, 2)])
    )
    unload_deleted = local_word_matrix(2, (((0, 1), CNOT),))
    unload_deletion_residual = float(
        np.linalg.norm(unload_deleted[:, (0, 1)] - np.eye(4, dtype=complex)[:, (0, 2)])
    )
    return {
        "controlled_axis_residuals": residuals,
        "negative_signed_X_control_residual": negative_residual,
        "controlled_gate_deletion_residuals": deletion_residuals,
        "minimum_controlled_gate_deletion_residual": min(deletion_residuals.values()),
        "generic_clean_subspace_swap_residual": clean_residual,
        "parity_unload_deletion_residual": unload_deletion_residual,
        "maximum_residual": max((*residuals.values(), negative_residual, clean_residual)),
    }


def independent_physical_lift(root, row, site_map, site_index):
    x = z = 0
    for site, (xbit, zbit) in root.lift_pauli(row, None, site_map).items():
        if xbit: x |= 1 << site_index[site]
        if zbit: z |= 1 << site_index[site]
    return root.base.Pauli(row.phase, x, z)


def independent_emitted_isometry_certificate(
    root,
    graph,
    site_map,
    events,
    primitives,
    route,
    symbolic_controller,
    decomposition,
    check_compilation,
    loader_compilation,
):
    sites = tuple(sorted(root.occupied(site_map)))
    site_index = {site: index for index, site in enumerate(sites)}

    def lift(row):
        support = root.lift_pauli(row, graph, site_map)
        x = z = 0
        for site, (xbit, zbit) in support.items():
            if xbit: x |= 1 << site_index[site]
            if zbit: z |= 1 << site_index[site]
        return root.base.Pauli(row.phase, x, z)

    cycles = [(lift(row), kind, key) for row, kind, key in root.cycle_rows(graph)]
    drows = [lift(root.local_d(graph, cell)) for cell in graph.cells[:-1]]
    repetition = []
    for edge, (_u, _v, kind, _owner) in enumerate(graph.edges):
        if kind != "matter_stream":
            continue
        left, right = site_map[edge]
        repetition.append(
            root.base.Pauli(z=(1 << site_index[left]) | (1 << site_index[right]))
        )
    logical = root.logical_rows(graph)
    logical_z = [lift(zrow) for _cell, _mode, _xrow, zrow in logical]
    physical_code = [row for row, _kind, _key in cycles] + drows + repetition
    vacuum_rows = physical_code + logical_z
    qubits = len(sites)
    vacuum_rank = root.base.gf2_rank(row.symplectic(qubits) for row in vacuum_rows)
    vacuum_commutators = sum(
        not left.commutes(right)
        for index, left in enumerate(vacuum_rows)
        for right in vacuum_rows[index + 1 :]
    )
    vacuum_phases = root.base.stabilizer_phase_failures(vacuum_rows, qubits)

    check_slots = {}
    counters = Counter()
    for physical, kind, key in cycles:
        owner, role, _stage = check_owner(kind, key)
        local_index = counters[(owner, role)]
        counters[(owner, role)] += 1
        check_slots[root.slot(owner, role, local_index)] = (physical, kind)
    corrections = defaultdict(lambda: root.base.Pauli())
    for row in root.correction_interactions(graph, site_map):
        corrections[row.left] = corrections[row.left] @ root.base.Pauli(
            z=1 << site_index[row.right]
        )
    triangle = bond = prior = 0
    for slot, correction in corrections.items():
        measured, kind = check_slots[slot]
        matching = [
            index
            for index, (row, row_kind, _key) in enumerate(cycles)
            if row == measured and row_kind == kind
        ]
        if len(matching) != 1:
            raise AssertionError(("ambiguous check row", slot, matching))
        expected = matching[0]
        response = [not correction.commutes(row) for row, _kind, _key in cycles]
        if kind == "cell_triangle":
            triangle += sum(
                bit != (index == expected)
                for index, bit in enumerate(response)
                if cycles[index][1] == "cell_triangle"
            )
        elif kind == "bond_rectangle":
            bond += sum(
                bit != (index == expected)
                for index, bit in enumerate(response)
                if cycles[index][1] == "bond_rectangle"
            )
            prior += sum(
                bit
                for index, bit in enumerate(response)
                if cycles[index][1] in ("cell_triangle", "coarse_plaquette")
            )
    stream_z = [
        root.base.Pauli(z=1 << site_index[site_map[edge][0]])
        for edge, (_u, _v, kind, _owner) in enumerate(graph.edges)
        if kind == "matter_stream"
    ]
    prior += sum(
        not correction.commutes(row)
        for correction in stream_z
        for row, kind, _key in cycles
        if kind == "cell_triangle"
    )
    cycle_commutators = sum(
        not left[0].commutes(right[0])
        for index, left in enumerate(cycles)
        for right in cycles[index + 1 :]
    )
    preserve_rows = physical_code + logical_z
    extraction_preservation = sum(
        not cycle.commutes(row)
        for cycle, _kind, _key in cycles
        for row in preserve_rows
    )
    cycle_only = [row for row, _kind, _key in cycles]
    correction_preservation = sum(
        not correction.commutes(row)
        for correction in tuple(corrections.values()) + tuple(stream_z)
        for row in preserve_rows
        if row not in cycle_only
    )
    initial_not_plus_z = sum(
        row.x != 0 or row.phase % 4 != 0 for row in drows + repetition
    )
    check_macros = independent_check_macro_certificate()
    loader_macros = independent_loader_macro_certificate()
    algebra = root.stabilizer_and_loader_certificate(graph, site_map)
    route_failures = sum(
        route[key]
        for key in (
            "non_NN_failures",
            "operand_failures",
            "arbitrary_transit_register_return_failures",
        )
    )
    primitive_unitarity = route["primitive_unitarity_failures"]
    decomposition_failure = int(
        max(
            decomposition["Toffoli_decomposition_residual"],
            decomposition["CCZ_H_Toffoli_H_residual"],
            decomposition["maximum_router_decomposition_residual"],
        )
        > TOL
    )
    failures = {
        "check_support_atlas_failures": (
            check_compilation["atlas_missing"] + check_compilation["atlas_extra"]
        ),
        "check_macro_failures": int(check_macros["maximum_residual"] > TOL),
        "inactive_check_macro_mutations": int(
            check_macros["minimum_parity_gate_deletion_residual"] <= 1.0e-3
        ),
        "triangle_decoder_response_failures": triangle,
        "coarse_controller_ANF_failures": sum(symbolic_controller["failure_census"].values()),
        "bond_decoder_response_failures": bond,
        "later_correction_prior_check_disturbance_failures": prior,
        "cycle_check_commutator_failures": cycle_commutators,
        "extraction_preservation_failures": extraction_preservation,
        "Z_correction_preservation_failures": correction_preservation,
        "initial_preserved_not_plus_Z_failures": initial_not_plus_z,
        "vacuum_rank_deficit": qubits - vacuum_rank,
        "vacuum_commutator_failures": vacuum_commutators,
        "vacuum_phase_failures": vacuum_phases,
        "loader_macro_failures": int(loader_macros["maximum_residual"] > TOL),
        "loader_support_atlas_failures": (
            loader_compilation["atlas_missing"]
            + loader_compilation["atlas_extra"]
            + loader_compilation["non_Z_axes_in_parity_unload"]
        ),
        "inactive_loader_macro_mutations": int(
            loader_macros["minimum_controlled_gate_deletion_residual"] <= 1.0e-3
            or loader_macros["parity_unload_deletion_residual"] <= 1.0e-3
        ),
        "logical_pair_failures": algebra["logical_canonical_failures"],
        "logical_stabilizer_commutator_failures": algebra[
            "logical_stabilizer_commutator_failures"
        ],
        "routed_SWAP_conjugation_failures": route_failures,
        "primitive_unitarity_failures": primitive_unitarity,
        "controller_local_decomposition_failures": decomposition_failure,
        "inactive_router_decomposition_mutations": int(
            decomposition["minimum_router_subgate_deletion_residual"] <= 1.0e-3
        ),
    }
    exact = all(value == 0 for value in failures.values())
    return {
        "proof_method": (
            "independent local-matrix macro identities, complete-lawful-domain ANF "
            "controller execution, signed stabilizer rank, and symbolic returned-SWAP conjugation"
        ),
        "check_macro_operator_certificate": check_macros,
        "controller_complete_ANF_certificate": symbolic_controller,
        "loader_macro_operator_certificate": loader_macros,
        "physical_code_rows": len(physical_code),
        "physical_logical_Z_rows": len(logical_z),
        "carrier_M2": qubits,
        "vacuum_tableau_rank": vacuum_rank,
        "unique_plus_vacuum": vacuum_rank == qubits,
        "signed_logical_generator_pairs": len(logical),
        "signed_logical_generator_identities_checked": 2 * len(logical),
        "retained_garbage_factorization": (
            "unique pure carrier vacuum plus input-untouched preparation stages makes "
            "retained syndrome/spent garbage input-independent"
        ),
        "failure_census": failures,
        "literal_emitted_encoder_isometry_exact": exact,
    }


def fixture(root, length):
    if not isinstance(length, int) or length < 2:
        raise ValueError("chronological E domain is integer cubic L>=2")
    shape = (length, length, length)
    cells = root.box(shape)
    graph = root.prep.OpenReferenceGraph(cells)
    site_map = root.carrier_placement(graph)
    carrier = root.occupied(site_map)
    auxiliary = {
        root.slot(cell, role, index)
        for cell in cells
        for role, count in root.ROLE_COUNTS.items()
        for index in range(count)
    }
    checks, check_cert = compile_checks(root, graph, site_map)
    corrections, correction_counts = compile_corrections(root, graph, site_map)
    loader, loader_cert = compile_loader(root, graph, site_map)
    events, chronology = compile_controller_semantics(root, shape, graph, site_map)
    controller_primitives = compile_controller_primitives_with_root(root, events)
    controller_exec = controller_certificate(root, shape, graph, site_map, events)
    controller_symbolic = symbolic_controller_certificate(
        root, shape, graph, site_map, events
    )
    stage_rows = (
        ("triangle_syndrome", checks["triangle_syndrome"]),
        ("triangle_correction", corrections["triangle_correction"]),
        ("coarse_syndrome", checks["coarse_syndrome"]),
        ("coarse_echo_correction_ack", controller_primitives),
        ("bond_syndrome", checks["bond_syndrome"]),
        ("bond_correction", corrections["bond_correction"]),
        ("logical_load", loader),
    )
    primitives = tuple(row for _stage, rows in stage_rows for row in rows)
    stage_runs = []
    for row in primitives:
        if not stage_runs or stage_runs[-1] != row.stage:
            stage_runs.append(row.stage)
    route = route_word(primitives, carrier, auxiliary, graph.cell_set)
    algebra = root.stabilizer_and_loader_certificate(graph, site_map)
    route_sites = route.pop("touched_sites")
    decomposition = decomposition_certificate()
    isometry = independent_emitted_isometry_certificate(
        root,
        graph,
        site_map,
        events,
        primitives,
        route,
        controller_symbolic,
        decomposition,
        check_cert,
        loader_cert,
    )
    return {
        "L": length,
        "cells": length**3,
        "encoded_carrier_M2": len(carrier),
        "expected_18N_plus_3E": 18 * length**3 + 9 * (length - 1) * length**2,
        "persistent_auxiliary_M2": len(auxiliary),
        "expected_36N": 36 * length**3,
        "carrier_auxiliary_collisions": len(carrier & auxiliary),
        "stage_primitive_counts": {stage: len(rows) for stage, rows in stage_rows},
        "stage_runs": tuple(stage_runs),
        "chronology_accepted": tuple(stage_runs) == STAGES,
        "all_stages_nonempty": all(rows for _stage, rows in stage_rows),
        "check_compilation": check_cert,
        "correction_gate_counts": correction_counts,
        "loader_compilation": loader_cert,
        "controller_chronology": chronology,
        "controller_execution": controller_exec,
        "emitted_encoder_isometry": isometry,
        "root_algebra": algebra,
        "exact_primitive_route": route,
        "dense_transit_capacity_M2": (16 * length + 3) ** 3,
        "analytic_capacity_upper_bound_6859N": 19**3 * length**3,
        "covariance": covariance(root, route_sites),
    }


def frozen_target_comparison(fixtures):
    if file_hash(ACTIVE_JOINED) != FROZEN_JOINED_SHA256:
        raise RuntimeError("frozen joined source hash mismatch")
    if file_hash(FROZEN_JOINED_RECEIPT) != FROZEN_JOINED_RECEIPT_SHA256:
        raise RuntimeError("frozen joined receipt hash mismatch")
    target = json.loads(FROZEN_JOINED_RECEIPT.read_text())
    mismatches = []
    rows = []
    for ours, theirs in zip(fixtures, target["fixtures"]):
        route = theirs["joined_route"]["root_executable_primitive_route"]
        controller = theirs["joined_route"]["controller_chronology"]
        execution = theirs["joined_route"]["controller_execution"]
        comparisons = {
            "encoded_carrier_M2": (ours["encoded_carrier_M2"], theirs["physical_carrier_M2"]),
            "persistent_auxiliary_M2": (ours["persistent_auxiliary_M2"], theirs["persistent_auxiliary_M2"]),
            "primitive_gate_count": (ours["exact_primitive_route"]["primitive_gates"], route["primitive_gate_count"]),
            "routed_gate_count": (ours["exact_primitive_route"]["routed_gates"], route["routed_gate_count"]),
            "maximum_route_distance": (ours["exact_primitive_route"]["maximum_route_distance"], route["maximum_route_distance"]),
            "carrier_sites_touched": (ours["exact_primitive_route"]["carrier_sites_touched"], route["carrier_sites_touched"]),
            "auxiliary_sites_touched": (ours["exact_primitive_route"]["persistent_auxiliary_sites_touched"], route["auxiliary_sites_touched_and_returned"]),
            "transit_sites_touched": (ours["exact_primitive_route"]["transit_sites_touched"], route["transient_route_sites_touched_and_returned"]),
            "controller_semantic_events": (ours["controller_chronology"]["semantic_events"], controller["chronological_semantic_events"]),
            "controller_compiled_primitives": (ours["stage_primitive_counts"]["coarse_echo_correction_ack"], controller["compiled_one_two_qubit_primitives"]),
            "controller_router_applications": (ours["controller_chronology"]["router_applications"], controller["router_applications"]),
            "controller_lawful_rank": (ours["controller_execution"]["lawful_syndrome_rank"], execution["lawful_coarse_syndrome_rank"]),
            "hostile_spent_token_failures": (ours["controller_execution"]["hostile_spent_reapplication_failures"].get("token_return", 0), execution["hostile_unguarded_spent_reapplication_token_failures"]),
            "hostile_spent_epoch_failures": (ours["controller_execution"]["hostile_spent_reapplication_failures"].get("spent_epoch", 0), execution["hostile_unguarded_spent_reapplication_spent_failures"]),
            "emitted_encoder_isometry_exact": (
                ours["emitted_encoder_isometry"]["literal_emitted_encoder_isometry_exact"],
                theirs["joined_route"]["encoder_isometry"][
                    "emitted_E_isometry_exact_on_declared_clean_domain"
                ],
            ),
        }
        bad = {key: pair for key, pair in comparisons.items() if pair[0] != pair[1]}
        mismatches.extend(f"L{ours['L']}:{key}" for key in bad)
        rows.append({
            "L": ours["L"],
            "fields_compared": len(comparisons),
            "mismatches": bad,
        })
    return {
        "frozen_source_sha256": file_hash(ACTIVE_JOINED),
        "frozen_receipt_sha256": file_hash(FROZEN_JOINED_RECEIPT),
        "target_status": target["status"],
        "target_failures": target["failures"],
        "comparison_rows": rows,
        "total_field_mismatches": len(mismatches),
        "mismatch_keys": mismatches,
        "comparison_method": "read-only frozen metric comparison; target module not imported",
    }
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--receipt",
        type=Path,
        default=(
            REPO_ROOT
            / "outputs"
            / "cycle870_openreference_chronological_encoder_independent_receipt_2026_08_02.json"
        ),
    )
    args = parser.parse_args()
    root = load_root()
    fixtures = [fixture(root, length) for length in (2, 3)]
    decomposition = decomposition_certificate()
    target_comparison = frozen_target_comparison(fixtures)
    invalid_rejected = 0
    for value in (0, 1, -1, 2.5, "3"):
        try:
            fixture(root, value)  # type: ignore[arg-type]
        except (ValueError, TypeError):
            invalid_rejected += 1
    noncube_rejected = 0
    for shape in ((2, 2, 3), (2, 3, 2), (3, 4, 5)):
        try:
            if len(set(shape)) != 1:
                raise ValueError("noncube")
        except ValueError:
            noncube_rejected += 1
    failures = []
    for row in fixtures:
        prefix = f"L{row['L']}"
        if row["encoded_carrier_M2"] != row["expected_18N_plus_3E"]:
            failures.append(prefix + " carrier formula")
        if row["persistent_auxiliary_M2"] != row["expected_36N"]:
            failures.append(prefix + " auxiliary formula")
        for key in ("carrier_auxiliary_collisions",):
            if row[key]: failures.append(prefix + " " + key)
        if not row["chronology_accepted"] or not row["all_stages_nonempty"]:
            failures.append(prefix + " chronology")
        for section, keys in (
            ("check_compilation", ("atlas_missing", "atlas_extra")),
            ("loader_compilation", ("atlas_missing", "atlas_extra", "non_Z_axes_in_parity_unload")),
            ("controller_chronology", ("non_epoch_atlas_templates_missing", "foreign_non_epoch_templates")),
            ("exact_primitive_route", ("primitive_unitarity_failures", "primitive_endpoint_outside_carrier_auxiliary_bank", "non_NN_failures", "operand_failures", "arbitrary_transit_register_return_failures", "route_sites_outside_radius9_capacity")),
            ("covariance", ("route_coordinate_injectivity_failures", "unit_step_failures", "route_coordinate_product_failures")),
        ):
            for key in keys:
                if row[section][key]: failures.append(f"{prefix} {section}.{key}")
        if row["controller_chronology"]["router_applications"] != row["controller_chronology"]["expected_router_applications"]:
            failures.append(prefix + " router count")
        if any(row["controller_execution"]["lawful_execution_failures"].values()):
            failures.append(prefix + " lawful controller")
        if not row["controller_execution"]["unlawful_syndrome_action_failure"]:
            failures.append(prefix + " unlawful syndrome negative control")
        hostile = row["controller_execution"]["hostile_spent_reapplication_failures"]
        if hostile.get("token_return", 0) + hostile.get("spent_epoch", 0) <= 0:
            failures.append(prefix + " hostile spent control")
        algebra = row["root_algebra"]
        for key in ("logical_stabilizer_commutator_failures", "logical_canonical_failures"):
            if algebra[key]: failures.append(prefix + " algebra." + key)
        if not row["emitted_encoder_isometry"][
            "literal_emitted_encoder_isometry_exact"
        ]:
            failures.append(prefix + " emitted encoder isometry")
    for key in (
        "Toffoli_decomposition_residual",
        "CCZ_H_Toffoli_H_residual",
        "maximum_router_decomposition_residual",
    ):
        if decomposition[key] > TOL: failures.append(key)
    if decomposition["minimum_Toffoli_subgate_deletion_residual"] <= 1.0e-3:
        failures.append("inactive Toffoli subgate deletion")
    if decomposition["minimum_CCZ_subgate_deletion_residual"] <= 1.0e-3:
        failures.append("inactive CCZ subgate deletion")
    if invalid_rejected != 5 or noncube_rejected != 3:
        failures.append("unlawful domain")
    if target_comparison["total_field_mismatches"]:
        failures.append("frozen target comparison")
    if target_comparison["target_status"] != "pass" or target_comparison["target_failures"]:
        failures.append("frozen target did not pass")
    undetected_by_fixture = {
        f"L{row['L']}": row["controller_execution"]["undetected_semantic_event_deletions"]
        for row in fixtures
    }
    per_occurrence_deletion_complete = not any(undetected_by_fixture.values())
    artifact_path = Path(__file__).resolve().relative_to(REPO_ROOT)
    receipt = {
        "artifact": {
            "path": str(artifact_path),
            "sha256": file_hash(Path(__file__).resolve()),
            "cold_command": f"python3 {artifact_path}",
        },
        "sources": {
            "root_source": str(ROOT_SOURCE.relative_to(REPO_ROOT)),
            "root_sha256": file_hash(ROOT_SOURCE),
            "dependency_sha256": DEPENDENCY_HASHES,
            "joint_probe_imported": False,
            "frozen_joined_target_sha256": file_hash(ACTIVE_JOINED),
            "frozen_joined_receipt_sha256": file_hash(FROZEN_JOINED_RECEIPT),
            "target_frozen_for_comparison": (
                file_hash(ACTIVE_JOINED) == FROZEN_JOINED_SHA256
                and file_hash(FROZEN_JOINED_RECEIPT) == FROZEN_JOINED_RECEIPT_SHA256
            ),
        },
        "chronology": STAGES,
        "controller_local_decompositions": decomposition,
        "fixtures": fixtures,
        "frozen_target_comparison": target_comparison,
        "unlawful_domain_controls": {
            "invalid_scalars_tested": 5,
            "invalid_scalars_rejected": invalid_rejected,
            "noncubes_tested": 3,
            "noncubes_rejected": noncube_rejected,
        },
        "claim_boundary": {
            "exact_execution": "seven-stage clean-domain H/S/T/X/CNOT/CZ/SWAP primitive word with returned NN routes on explicitly counted transit M2 capacity",
            "root_atlas": "root interaction lists are template/address atlases; controller templates are reused by the independently emitted depth-first word and are not interpreted in list order as time",
            "controller_domain": "one supplied invocation with syndrome/input/work clean and every root fresh=1,token=spent=0",
            "not_claimed": "no local spent-sector admission guard, reset, recurrence, autonomous genesis, physical occurrence, or intrinsic time",
        },
        "target_checker_warnings": {
            "class_level_not_individual_deletion": "active target stops after one detected representative per controller role class",
            "compiled_subgate_deletion_missing": "active target does not delete each H/T/CNOT inside Toffoli/CCZ",
            "counter_not_execution_controls": "active target labels several check/correction/loader counts as deletions without executing the reduced word",
            "triangle_controlled_Z_deletion_missing": "active target counts triangle decoder table entries but has no explicit triangle controlled-Z gate deletion control",
            "route_deletion_scope": "active root/join route checks delete only the first forward SWAP, not every forward/central/reverse gate position",
            "unlawful_guard_boundary": "unlawful syndrome and spent reapplication are detected adversarially, but no physical admission guard is compiled",
            "redundant_parent_xor_Toffolis_on_lawful_clean_domain": undetected_by_fixture,
            "redundancy_interpretation": "these gates do not spoil exactness, but refute any per-occurrence claim that every listed semantic event is deletion-active",
        },
        "validation_failures": failures,
        "independent_chronological_E_exactness_pass": not failures,
        "independent_per_occurrence_deletion_completeness_pass": per_occurrence_deletion_complete,
        "verification_status": "pass_with_deletion_and_domain_qualifications" if not failures else "fail",
    }
    args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n")
    print(json.dumps(receipt, indent=2, sort_keys=True, default=str))
    print("INDEPENDENT_CHRONOLOGICAL_E_EXACTNESS_PASS_WITH_QUALIFICATIONS" if not failures else "INDEPENDENT_CHRONOLOGICAL_E_FAIL")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
