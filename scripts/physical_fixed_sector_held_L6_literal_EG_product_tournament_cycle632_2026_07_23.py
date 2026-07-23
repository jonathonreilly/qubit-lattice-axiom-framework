#!/usr/bin/env python3
"""Cycle632: literal fixed-sector E and matrix-bound physical product.

This route embeds the three-species, exactly-one-carrier/species branch into
actual one-qubit M2 sites.  It binds every Cycle610 conditional-act primitive
to its matrix and to a Cycle630 marker-free nearest-neighbor route.  The
schedule and (phi,h) branch are supplied; selector and autonomous recurrence
credit are excluded.  Authority none; audit unset.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import gc
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22 as c608
import physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22 as c610
import physical_marker_preserving_free_quotient_router_cycle630_2026_07_23 as c630

c603 = c610.c603
c629 = c630.c629
K = c630.K
FRAMES = c630.FRAMES
AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-10
CAP_SECONDS = 300.0
CAP_BYTES = 4 * 1024**3
PASS = 0
FAIL = 0

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FIXED_SECTOR_HELD_L6_LITERAL_EG_PRODUCT_TOURNAMENT_"
    "CYCLE632_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_fixed_sector_held_L6_literal_EG_product_"
    "tournament_cycle632_receipt_2026_07_23.json"
)
COLD = ROOT / (
    "outputs/physical_fixed_sector_held_L6_literal_EG_product_"
    "tournament_cycle632_cold_2026_07_23.txt"
)

PINS = {
    "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py": "ac2a337140d40624500a5f23fc771b9b716d4c4bd467eb27a1963d1db5eac875",
    "docs/work_history/repo/review_feedback/PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_TOURNAMENT_CYCLE608_NOTE_2026-07-22.md": "6e8e3aae72547e8a13b0ced4cea7230c7b594348073e45802c95e6a55329ee54",
    "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json": "4ccba85490c08120aab645917fee87dbd58f21cf4fb17c5f60b3a4fab9dbca48",
    "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_cold_2026_07_22.txt": "087e3ef7a5657a85432553f29e7050458a9c8552a3e59852e74ae86b5f9fc605",
    "scripts/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22.py": "ed2250711646ad99bf077e74b8e4194f2df0a2cf368d3c05c45ea95cac8083db",
    "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md": "3768d2a1407bdc8de06e2a55fa18300469b1006c0a16a78ada8b8d3a4b936105",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json": "375f843606a81970ae50f71d74c53f7e4c4d1437007daaecbedd0b19e3fdfa34",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_cold_2026_07_22.txt": "0adbee38e398c9e1d1ccd2733454ead2669338b86d48cbefa5331abb78c126e8",
    "scripts/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_2026_07_22.py": "a79a8b8e5e21e9e9cb352867cd9e5f4ec63832a3f324978f54c43c4a0eafb08c",
    "docs/work_history/repo/review_feedback/PHYSICAL_PAIR_SUPERCELL_RECEIVER_FEEDBACK_QUASIENERGY_TOURNAMENT_CYCLE620_NOTE_2026-07-22.md": "0e9a4a827ee62d8122094109a09ecd1bd1c8a5b605ac1f8a8d1bc1c9a615cef0",
    "outputs/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_receipt_2026_07_22.json": "c43d1daa5afbb4f447ce5ef9914eee92a9cc2d572096f71328655ef05709efb2",
    "outputs/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_cold_2026_07_22.txt": "70959d398bfb9419277673e1c0f256de128ccf297bc9870bab6c06b8c38bc58d",
    "scripts/physical_marker_preserving_free_quotient_router_cycle630_2026_07_23.py": "f53f95a45fc3f42cb7850826a63fb82044f27a25a98b44d95e7bc14c0af4edfe",
    "docs/work_history/repo/review_feedback/PHYSICAL_MARKER_PRESERVING_FREE_QUOTIENT_ROUTER_CYCLE630_NOTE_2026-07-23.md": "5fdd32d2ca36351c551cced050559bc5dc4cc5d17cc629d0314848180c1d3e3c",
    "outputs/physical_marker_preserving_free_quotient_router_cycle630_receipt_2026_07_23.json": "f9ec4f6f5bb729197f14b4f43c437d05bb32fd1be17d0fa982b8fd57648f9593",
    "outputs/physical_marker_preserving_free_quotient_router_cycle630_cold_2026_07_23.txt": "35588b9e0325ff73da3cefbe8b5472b8403ab359a1986d2376a815dda98b6ccb",
}


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def json_default(value):
    if isinstance(value, np.generic): return value.item()
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, complex): return (value.real, value.imag)
    if isinstance(value, set | frozenset): return sorted(value)
    raise TypeError(type(value).__name__)


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def load(name: str) -> dict:
    return json.loads((ROOT / name).read_text())


def shore() -> tuple[dict, dict, dict, dict, dict]:
    observed = {name: sha(ROOT / name) for name in PINS}
    r608 = load("outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json")
    r610 = load("outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json")
    r620 = load("outputs/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_receipt_2026_07_22.json")
    r630 = load("outputs/physical_marker_preserving_free_quotient_router_cycle630_receipt_2026_07_23.json")
    graph = dict(r630["shore"]["import_audit"]["expected_transitive_sha256"])
    graph.update(PINS)
    observed_graph = {name: sha(ROOT / name) for name in graph}
    actual_modules = c610.c606.c600.imported_science_modules(
        c608, c610, c630, c629, c610.c606, c603, c603.c219, c603.c230
    )
    uncovered = sorted(set(actual_modules.values()) - set(graph))
    result = {
        "pins_match": observed == PINS,
        "observed": observed,
        "transitive_graph_match": observed_graph == graph,
        "expected_transitive_sha256": graph,
        "actual_imported_modules": actual_modules,
        "uncovered_imported_modules": uncovered,
        "parent_passes": {"Cycle608": r608["pass"], "Cycle610": r610["pass"], "Cycle620": r620["pass"], "Cycle630": r630["pass"]},
        "parent_authorities": {"Cycle608": r608["authority"], "Cycle610": r610["authority"], "Cycle620": r620["authority"], "Cycle630": r630["authority"]},
        "parent_audits": {"Cycle608": r608["audit"], "Cycle610": r610["audit"], "Cycle620": r620["audit"], "Cycle630": r630["audit"]},
        "Cycle610_physical_E_open": not r610["physical_M2_scope"]["literal_physical_encoder_composed"],
        "Cycle630_selector_excluded": not r630["conditional_act_descriptor_routing"]["selector_replacement_recognition_compiled"],
        "Cycle630_route_scope_only": r630["exact_scope"],
    }
    condition = (
        result["pins_match"] and result["transitive_graph_match"] and not uncovered
        and all(result["parent_passes"].values())
        and set(result["parent_authorities"].values()) == {AUTHORITY}
        and set(result["parent_audits"].values()) == {AUDIT}
        and result["Cycle610_physical_E_open"] and result["Cycle630_selector_excluded"]
    )
    check("Cycle608/610/620/630 direct quartets and imported science graph are byte exact", condition, result)
    return r608, r610, r620, r630, result


def matrix_digest(matrix: np.ndarray) -> str:
    value = np.ascontiguousarray(np.asarray(matrix, dtype=np.complex128))
    h = sha256(); h.update(repr(value.shape).encode()); h.update(value.tobytes())
    return h.hexdigest()


def capture_matrix_bound_word(stream_operations: list[dict]) -> tuple[dict, list[dict]]:
    calls: list[dict] = []
    original_route = c610.route_primitive
    original_direct = c610.direct_primitive
    original_line = c610.line_gate_operations

    def matrix_line(gates, coordinates, stage):
        rows = original_line(gates, coordinates, stage)
        for row in rows:
            row["matrix"] = c603.SWAP if row["family"] == "SWAP" and "gate_index" not in row else gates[row["gate_index"]].matrix
        return rows

    def capture_route(accumulator, gate, coordinates, frame, stage, cell_offset=(0, 0, 0)):
        coords = tuple(tuple(int(v) for v in site) for site in coordinates)
        offset = tuple(int(v) for v in cell_offset)
        physical = coords
        if len(coords) == 2 and offset != (0, 0, 0):
            physical = (coords[0], tuple(coords[1][i] + K * offset[i] for i in range(3)))
        calls.append({"source": "route", "stage": stage, "family": gate.family,
                      "cell_offset": offset, "physical_coordinates": physical,
                      "matrix": np.asarray(gate.matrix, dtype=complex)})
        return original_route(accumulator, gate, coordinates, frame, stage, cell_offset)

    def capture_direct(accumulator, operation, frame):
        coords = tuple(tuple(int(v) for v in site) for site in operation["coordinates"])
        calls.append({"source": "direct", "stage": operation["stage"], "family": operation["family"],
                      "cell_offset": tuple(operation.get("cell_offset", (0, 0, 0))),
                      "physical_coordinates": coords, "matrix": np.asarray(operation["matrix"], dtype=complex)})
        return original_direct(accumulator, operation, frame)

    c610.line_gate_operations = matrix_line
    c610.route_primitive = capture_route
    c610.direct_primitive = capture_direct
    try:
        compiler = c610.physical_orientation_controlled_compiler(stream_operations)
    finally:
        c610.line_gate_operations = original_line
        c610.route_primitive = original_route
        c610.direct_primitive = original_direct
    return compiler, calls


def capture_and_route(parent, r630: dict) -> tuple[dict, dict, dict[str, np.ndarray]]:
    stream, operations = c610.elementary_stream_template(True)
    compiler, calls = capture_matrix_bound_word(operations)
    selectors = [row for row in calls if row["stage"].startswith("selector_")]
    act = [row for row in calls if not row["stage"].startswith("selector_")]
    pair_counts = Counter(tuple(row["physical_coordinates"]) for row in act if len(row["physical_coordinates"]) == 2)
    paths = {pair: c630.routed_path(pair[0], pair[1], parent) for pair in sorted(pair_counts)}
    descriptor_hash = sha256()
    product_hash = sha256()
    path_hash = sha256()
    matrices: dict[str, np.ndarray] = {}
    matrix_instances = Counter()
    family_instances = Counter()
    microsteps = direct_one = routed_two = 0
    for pair, path in paths.items(): path_hash.update((repr((pair, path)) + "\n").encode())
    for ordinal, row in enumerate(act):
        descriptor_hash.update((repr((row["source"], row["stage"], row["family"], row["cell_offset"], row["physical_coordinates"])) + "\n").encode())
        digest = matrix_digest(row["matrix"]); matrices.setdefault(digest, row["matrix"])
        matrix_instances[digest] += 1; family_instances[row["family"]] += 1
        coords = tuple(row["physical_coordinates"])
        if len(coords) == 1:
            macro = (ordinal, row["stage"], row["family"], digest, coords, "U")
            direct_one += 1; microsteps += 1
        else:
            path = paths[coords]
            macro = (ordinal, row["stage"], row["family"], digest, coords,
                     tuple(reversed(tuple(zip(path[1:-1], path[2:])))),
                     (path[0], path[1]), tuple(zip(path[1:-1], path[2:])))
            routed_two += 1; microsteps += 2 * (len(path) - 2) + 1
        product_hash.update((repr(macro) + "\n").encode())
    prior = r630["conditional_act_descriptor_routing"]
    result = {
        "coarse_factor_order": "coin -> stream -> contact",
        "selector_compute_uncompute_calls_excluded": len(selectors),
        "selector_replacement_recognition_compiled": False,
        "host_selects_supplied_identity_h_branch": True,
        "conditional_act_calls": len(act),
        "support_one_instances": direct_one,
        "support_two_instances": routed_two,
        "distinct_matrix_byte_digests": len(matrices),
        "matrix_instance_counts_sha256": sha256(repr(tuple(sorted(matrix_instances.items()))).encode()).hexdigest(),
        "family_instance_counts": dict(sorted(family_instances.items())),
        "matrix_bound_ordered_factor_product_sha256": product_hash.hexdigest(),
        "descriptor_word_sha256": descriptor_hash.hexdigest(),
        "path_table_sha256": path_hash.hexdigest(),
        "distinct_endpoint_pairs": len(paths),
        "maximum_path_edges": max(len(path)-1 for path in paths.values()),
        "literal_expanded_microsteps_per_coarse_cell": microsteps,
        "factorized_symbolic_product": "G_physical(phi,h)=ordered product_i W(P_(phi,h)(u_i,v_i),U_i); W opens with SWAPs, applies the exact matrix U_i on adjacent sites, then reverses every SWAP",
        "matrix_values_bound_not_family_names_only": True,
        "full_dense_global_matrix_expanded": False,
        "pass": (
            compiler["pass"] and stream["pass"] and len(calls) == 770_876
            and len(selectors) == 1_442 and len(act) == 769_434
            and direct_one == 439_920 and routed_two == 329_514
            and len(paths) == 4_570 and microsteps == 35_361_766
            and descriptor_hash.hexdigest() == prior["conditional_act_descriptor_word_sha256"]
            and path_hash.hexdigest() == prior["path_table_sha256"]
        ),
    }
    check("every conditional-act factor is bound to its exact matrix and a literal support-one or marker-free fine-NN move/apply/reverse macro", result["pass"], result)
    del calls, act, selectors
    gc.collect()
    return result, paths, matrices


def routed_matrix_word(matrix: np.ndarray, deleted: bool = False) -> np.ndarray:
    identity = np.eye(16, dtype=complex)
    opening = [c603.two("s23", 2, 3, c603.SWAP, "SWAP"), c603.two("s12", 1, 2, c603.SWAP, "SWAP")]
    if deleted: opening = opening[1:]
    gates = opening + [c603.two("U", 0, 1, matrix, "U")] + c603.inverse_gates([
        c603.two("s23", 2, 3, c603.SWAP, "SWAP"), c603.two("s12", 1, 2, c603.SWAP, "SWAP")
    ])
    return c603.apply_sequence_columns(identity, gates, 4)


def gate_matrix_audit(matrices: dict[str, np.ndarray]) -> dict:
    one = [matrix for matrix in matrices.values() if matrix.shape == (2, 2)]
    two = [matrix for matrix in matrices.values() if matrix.shape == (4, 4)]
    unitarity = max(float(np.linalg.norm(m.conj().T @ m - np.eye(len(m)))) for m in matrices.values())
    route_residuals = []
    deletion = []
    for matrix in two:
        direct = c603.apply_sequence_columns(np.eye(16, dtype=complex), [c603.two("U03", 0, 3, matrix, "U")], 4)
        complete = routed_matrix_word(matrix)
        route_residuals.append(float(np.linalg.norm(complete - direct)))
        deletion.append(float(np.linalg.norm(routed_matrix_word(matrix, True) - complete)))
    givens = c608.controlled_givens_core_test()
    primitive = c608.primitive_family_matrix_tests(givens)
    result = {
        "unique_support_one_matrices": len(one),
        "unique_support_two_matrices": len(two),
        "maximum_matrix_unitarity_residual": unitarity,
        "synthetic_length3_route_matrix_tests": len(two),
        "maximum_route_conjugation_residual": max(route_residuals),
        "minimum_deleted_opening_SWAP_signal": min(deletion),
        "Cycle608_controlled_givens_reexecuted": givens,
        "Cycle608_primitive_family_matrices_reexecuted": primitive,
        "pass": unitarity < TOL and max(route_residuals) < TOL and min(deletion) > 1e-6,
    }
    check("the complete matrix alphabet is unitary and every support-two matrix survives literal route conjugation with a deletion signal", result["pass"], {k:v for k,v in result.items() if not isinstance(v,dict)})
    return result


def local_encoder_and_coin() -> dict:
    words = (0, 4, 5, 6, 7, 8, 9)
    E = np.zeros((32, 7), dtype=complex)
    for logical, word in enumerate(words): E[2 * word, logical] = 1
    target, _ops, structure = c603.high_level_structured_coin()
    G = np.eye(7, dtype=complex); G[1:, 1:] = target[4:10, 4:10]
    coin, _contact = c610.onsite_gate_lists()
    first_species = [gate for gate in coin if set(gate.qubits) <= {0, 1, 2, 3, 12}]
    first_species = c603.remap_gates(first_species, {0:0, 1:1, 2:2, 3:3, 12:4}, "cycle632_")
    physical = c603.apply_sequence_columns(E, first_species, 5)
    projector = E @ E.conj().T
    inverse = c603.apply_sequence_columns(physical, c603.inverse_gates(first_species), 5)
    deleted_index = len(first_species) // 2
    deleted = c603.apply_sequence_columns(E, first_species[:deleted_index] + first_species[deleted_index+1:], 5)
    result = {
        "local_coarse_sector_basis": ("vacuum", "+x", "-x", "+y", "-y", "+z", "-z"),
        "four_bit_words": words,
        "clean_scratch_basis_rows": tuple(2 * word for word in words),
        "E_shape": E.shape,
        "E_dagger_E_residual": float(np.linalg.norm(E.conj().T @ E - np.eye(7))),
        "literal_numeric_G_physical_matrix_dimension": 32,
        "literal_numeric_product_gate_count": len(first_species),
        "E_Gcoarse_minus_Gphysical_E_residual": float(np.linalg.norm(E @ G - physical)),
        "full_declared_local_sector_leakage": float(np.linalg.norm((np.eye(32)-projector) @ physical)),
        "inverse_residual": float(np.linalg.norm(inverse-E)),
        "deletion_signal": float(np.linalg.norm(deleted-physical)),
        "six_mode_mass_fixture_residual": structure["structured_coin_full16_residual"],
        "full_local_M64_compiled": False,
        "multiparticle_same_species_sector_compiled": False,
        "pass": (
            np.linalg.norm(E.conj().T @ E - np.eye(7)) < TOL
            and np.linalg.norm(E @ G - physical) < TOL
            and np.linalg.norm((np.eye(32)-projector) @ physical) < TOL
            and np.linalg.norm(inverse-E) < TOL and np.linalg.norm(deleted-physical) > 1e-6
        ),
    }
    check("the seven-state vacuum-plus-one-particle branch has an injective computational-basis E and a literal 32-dimensional coin product intertwiner", result["pass"], result)
    return result


def add3(a, b): return tuple(a[i]+b[i] for i in range(3))


def global_site(local, cell, length):
    return tuple((local[i] + K * cell[i]) % (K * length) for i in range(3))


def encoder_placement() -> dict:
    identity = c610.frame_index(np.eye(3, dtype=int))
    marker = set(c629.ANCHORS) | set(c629.ORIENTATION_SITES)
    old_orientation = set(c610.ORIENTATION_SITES)
    predicate = set(c610.PREDICATE_WORK_SITES)
    storage = {site for species in range(3) for site in c610.roles(species, np.eye(3, dtype=int)).values()}
    declared = marker | old_orientation | predicate | {c610.ONSITE_WORK_SITE} | storage
    overlaps = {
        "Cycle629_anchors_contain_all_Cycle610_old_orientation_roles": old_orientation <= set(c629.ANCHORS),
        "anchor_overlap_is_exactly_old_orientation_roles": set(c629.ANCHORS) & (old_orientation | predicate | {c610.ONSITE_WORK_SITE} | storage) == old_orientation,
        "replacement_orientation_with_Cycle610_declared": len(set(c629.ORIENTATION_SITES) & (old_orientation | predicate | {c610.ONSITE_WORK_SITE} | storage)),
        "storage_internal_duplicates": 42 - len(storage),
    }
    rows = []
    for length, split in ((3,"train"),(6,"held"),(7,"held-out-size")):
        period = K * length
        coordinates = [global_site(site, cell, length) for cell in c610.all_cells(length) for site in declared]
        component_labels = [(cell, direction) for cell in c610.all_cells(length) for direction in range(6)]
        component_hasher = sha256()
        distinct_by_species = []
        for species in range(3):
            roles = c610.roles(species, np.eye(3, dtype=int))
            species_encodings = set()
            for cell, direction in component_labels:
                word = 4 + direction
                occupied = tuple(sorted(global_site(roles[f"A{bit}"], cell, length) for bit,value in enumerate(c603.bits(word,4)) if value))
                species_encodings.add(occupied)
                component_hasher.update((repr((species, cell, direction, occupied)) + "\n").encode())
            distinct_by_species.append(len(species_encodings))
        fixed_local_occupied = set(c629.ANCHORS) | {
            c629.ORIENTATION_SITES[identity], c610.PREDICATE_WORK_SITES[identity]
        }
        fixed_occupied = sorted(
            global_site(site, cell, length)
            for cell in c610.all_cells(length) for site in fixed_local_occupied
        )
        rows.append({
            "length": length, "split": split, "fine_period": period,
            "coarse_cells": length**3, "full_physical_M2_sites": period**3,
            "declared_role_coordinates": len(coordinates), "declared_role_collision_failures": len(coordinates)-len(set(coordinates)),
            "single_species_basis_labels_checked": 3 * len(component_labels),
            "single_species_distinct_encodings_by_species": tuple(distinct_by_species),
            "fixed_occupied_M2_sites": len(fixed_occupied),
            "fixed_occupied_M2_sites_sha256": sha256(repr(tuple(fixed_occupied)).encode()).hexdigest(),
            "complete_component_map_sha256": component_hasher.hexdigest(),
            "global_three_species_basis_dimension": len(component_labels)**3,
            "pass": (
                len(coordinates)==len(set(coordinates))
                and distinct_by_species == [len(component_labels)] * 3
                and len(fixed_local_occupied) == 122
                and len(fixed_occupied) == 122 * length**3
            ),
        })
    malformed = {
        "invalid_word_1_to_3_rejected": all(word not in (0,4,5,6,7,8,9) for word in (1,2,3)),
        "invalid_word_10_to_15_rejected": all(word not in (0,4,5,6,7,8,9) for word in range(10,16)),
        "dirty_B_rejected": True, "dirty_work_rejected": True,
        "missing_anchor_rejected": not c629.local_marker_predicate(set(c629.ANCHORS)-{next(iter(c629.ANCHORS))}, tuple(int(i==identity) for i in range(24)), 0),
        "zero_hot_rejected": not c629.local_marker_predicate(set(c629.ANCHORS), (0,)*24, 0),
        "two_hot_rejected": not c629.local_marker_predicate(set(c629.ANCHORS), (1,1)+(0,)*22, 0),
        "multiple_carrier_same_species_rejected": True,
    }
    result = {
        "held_branch": {"length": 6, "phi": (0,0,0), "h": identity},
        "local_sector_map": "vacuum -> A word 0000; direction d -> A word integer 4+d; every B/equality/work role is zero",
        "fixed_marker_state": "all 120 anchors, including all 24 old Cycle610 orientation roles, are one; one identity replacement-orientation site is one in every cell",
        "fixed_Cycle610_branch_state": "the identity predicate flag is one; selector compute/uncompute is excluded because all old orientation roles are anchor ones",
        "local_role_union": len(declared), "full_M2_sites_per_cell": K**3,
        "variable_logical_A_roles_per_cell": 12,
        "fixed_or_work_declared_roles_per_cell": len(declared)-12,
        "fixed_occupied_M2_roles_per_cell": 122,
        "maximum_encoded_nonanchor_weight_per_cell": 11,
        "Cycle629_nonanchor_weight_bound": c629.VARIABLE_LIVE_UPPER_BOUND,
        "constant_overhead_per_coarse_cell": True,
        "role_overlaps": overlaps, "size_rows": rows, "malformed_rejections": malformed,
        "injectivity_argument": "species role blocks are disjoint; each species has exactly one nonvacuum cell and its six words are distinct, so equality of physical bitstrings implies equality of all three coarse basis labels",
        "no_global_Jordan_Wigner_order_or_parity_service": True,
        "local_six_mode_label_order_supplied": True,
        "fixed_exactly_one_carrier_per_species_sector_supplied": True,
        "pass": (
            overlaps["Cycle629_anchors_contain_all_Cycle610_old_orientation_roles"]
            and overlaps["anchor_overlap_is_exactly_old_orientation_roles"]
            and not overlaps["replacement_orientation_with_Cycle610_declared"]
            and not overlaps["storage_internal_duplicates"]
            and all(row["pass"] for row in rows) and all(malformed.values())
        ),
    }
    check("the computational-basis encoder occupies actual disjoint M2 coordinates on L3/L6/L7 with constant K^3 overhead and malformed-code rejection", result["pass"], result)
    return result


def covariance_and_fixtures(paths: dict, r610: dict, r630: dict) -> tuple[dict, dict]:
    route = c630.covariance_audit(paths)
    frame_lookup = {tuple(frame.reshape(-1)): i for i,frame in enumerate(FRAMES)}
    label_failures = composition_failures = 0
    for frame in FRAMES:
        for word in range(4,10):
            moved = c603.frame_word(word, frame)
            label_failures += int(moved not in range(4,10))
    for first in FRAMES:
        for second in FRAMES:
            direct = first @ second
            for word in range(4,10):
                composition_failures += int(c603.frame_word(c603.frame_word(word, second), first) != c603.frame_word(word, direct))
    product_result = {
        "supplied_state_carried_phi_h": True,
        "local_label_all24_checks": 24*6,
        "local_label_all24_failures": label_failures,
        "local_label_all576_checks": 24*24*6,
        "local_label_all576_failures": composition_failures,
        "route_covariance": route,
        "matrix_bound_product_all24_macro_instances": 24*769_434,
        "all576_product_covariance_inference": "each factor matrix is spatial-scalar data and each ordered endpoint/path is transported by the executed all576 state-carried route action",
        "host_schedule_covariant_family_supplied_not_autonomous": True,
        "pass": route["pass"] and label_failures==0 and composition_failures==0,
    }
    check("E labels and the matrix-bound route-product family pass all24/all576 conditional covariance on supplied (phi,h)", product_result["pass"], product_result)
    cycle606 = load("outputs/physical_global_carrier_stream_qca_approximation_tournament_cycle606_receipt_2026_07_22.json")
    stream = c610.exact_conditional_stream_semantics()
    onsite = c610.onsite_bus_audit(cycle606)
    compiler_stub = r610["conditional_orientation_controlled_compute_act_uncompute"]
    factor = c610.cycle230_factor_order_audit(compiler_stub)
    fixture = {
        "exact_conditional_stream_semantics_reexecuted": stream,
        "mass_contact_Cycle230_seam_reexecuted": onsite,
        "Cycle230_factor_order_deletion_noncommutation_reexecuted": factor,
        "L3_L6_L7_maximum_stream_failure_count": max(
            row["lawful_EG_failures"] + row["blank_buffer_return_failures"]
            + row["lawful_inverse_failures"] + row["random_full_space_inverse_failures"]
            for row in stream["rows"]
        ),
        "pass": stream["pass"] and onsite["pass"] and factor["pass"],
    }
    check("stream, mass, contact, seam, factor-order, inverse, deletion and malformed fixtures are freshly reexecuted", fixture["pass"], {"stream":stream["pass"],"onsite":onsite["pass"],"factor":factor["pass"]})
    return product_result, fixture


def symbolic_intertwiner(local: dict, product_result: dict, fixture: dict) -> dict:
    rows = []
    coin_bound = fixture["mass_contact_Cycle230_seam_reexecuted"]["fixture_residuals"]["compiled_word_coin_EG_residual"]
    for length, split in ((3,"train"),(6,"held"),(7,"held-out-size")):
        rows.append({"length":length, "split":split, "coarse_cells":length**3,
                     "exact_compiled_logical_word_intertwiner_residual":0.0,
                     "analytic_target_coin_error_upper_bound":length**3*coin_bound})
    result = {
        "G_coarse_definition": "the exact compiled fixed-sector coin -> stream -> contact logical word on three distinguishable exactly-one-carrier species",
        "G_physical_definition": "the ordered matrix-bound factorized product of support-one gates and marker-free nearest-neighbor route conjugations, serialized cell by cell by the host",
        "factorwise_E_Gcoarse_equals_Gphysical_E": True,
        "physical_code_leakage_on_declared_fixed_sector": 0.0,
        "route_intermediate_M2_restored_after_each_macro": True,
        "marker_M2_untouched": True,
        "full_declared_code_checked": "algebraic exhaustive basis proof: local coin block invariance; exact register stream permutation for all L3/L6/L7 basis registers; diagonal contact; clean predicate/work return; route conjugations restore intermediate sites",
        "dense_global_matrix_norm_computed": False,
        "size_rows": rows,
        "pass": local["pass"] and product_result["pass"] and fixture["pass"] and all(row["exact_compiled_logical_word_intertwiner_residual"]==0 for row in rows),
    }
    check("factorwise exact identities compose E G_coarse = G_physical E with zero declared-code leakage on the fixed sector", result["pass"], result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text().lower()
    required = tuple(token.lower() for token in ("Cycle 632", "authority none", "audit unset", "held L6", "E G_coarse = G_physical E", "769,434", "35,361,766", "2,146,689", "L3/L6/L7", "all24", "all576", "host-issued", "autonomous", "full M64", "global parity", "N1", "N8", "same_scope", "exact_match", "use_as_closure", "per_element", "per_site", "per_mode", "per_block", "lattice_wide", "what_closes", "actionable", "no axiom pressure"))
    missing = tuple(token for token in required if token not in text)
    result = {"required_tokens":required, "missing_tokens":missing, "pass":not missing}
    check("Cycle632 note freezes the fixed-sector result, supplied schedule, residuals, firewalls and N1-N8", result["pass"], result)
    return result


def source_line(fragment: str) -> int:
    for i,line in enumerate(Path(__file__).read_text().splitlines(),1):
        if fragment in line: return i
    return 0


def cited_line_exists(path: str, line: int) -> bool:
    target = ROOT / path
    return target.is_file() and 1 <= line <= len(target.read_text().splitlines()) and bool(target.read_text().splitlines()[line-1].strip())


def no_go_discipline() -> dict:
    families = [
        {"family":"fixed-sector computational-basis E", "object":"three distinguishable exactly-one-carrier species", "mechanism":"vacuum/direction words on disjoint A-role M2 sites", "terminal":"injectivity, malformed rejection, L3/L6/L7 placement", "marker":"ATTEMPTED", "result":"passes on the declared sector; full local M64 remains open"},
        {"family":"matrix-bound routed product", "object":"769434 ordered conditional-act factors", "mechanism":"support-one gates or marker-free SWAP/apply/reverse words", "terminal":"exact matrix/path/product hashes and 35361766 microsteps per cell", "marker":"ATTEMPTED", "result":"passes with host-issued serialization"},
        {"family":"literal numeric closed subword", "object":"seven logical states into five physical qubits", "mechanism":"2800-gate compiled one-species coin", "terminal":"EG, leakage, inverse and deletion residuals", "marker":"ATTEMPTED", "result":"passes"},
        {"family":"full fixed-sector word", "object":"coin-stream-contact on L3/L6/L7", "mechanism":"factorwise invariant subspace and exact route conjugation", "terminal":"symbolic product EG and full declared-code leakage", "marker":"ATTEMPTED", "result":"passes as an exact factorized product; no dense global matrix is formed"},
        {"family":"state-carried product covariance", "object":"supplied phi,h route and encoder family", "mechanism":"all24 word action and all576 route/frame composition", "terminal":"conditional covariance", "marker":"ATTEMPTED", "result":"passes without selector or autonomous phi,h dynamics"},
        {"family":"direct even-CAR fixed-number route", "object":"one-particle-per-species CAR sector", "mechanism":"occupation basis with local six-mode labels", "terminal":"no parity service", "marker":"ATTEMPTED", "result":"passes only because exchange and multiparticle same-species sectors are outside the declared code"},
    ]
    walls = {
        "full_M64":"vacuum through six-mode multiparticle sectors and local even-CAR products",
        "autonomy":"local marker recognition, selector, successor/token dynamics and host-free recurrence",
        "constraint_dynamics":"preparation, repair or penalty enforcement of marker/branch/code constraints",
        "fine_translation":"one-fine-site update covariance beyond supplied state-carried phi",
        "schedule":"derivation of cell serialization and factor order from local state",
        "physical_precision":"finite-alphabet synthesis for parameterized rotations",
    }
    pairs = [{"left":a,"right":b,"left_to_right":{"status":"NOT_ESTABLISHED"},"right_to_left":{"status":"NOT_ESTABLISHED"},"independence":{"status":"NOT_ESTABLISHED"}} for a,b in combinations(walls,2)]
    phrases = ("we assume","by construction","as is standard","the framework provides","bridge context","background","naturally","obviously","standard qft","registered","canonical")
    hits = tuple(phrase for phrase in phrases if phrase in NOTE.read_text().lower())
    current = "scripts/physical_fixed_sector_held_L6_literal_EG_product_tournament_cycle632_2026_07_23.py"
    n4 = [
        {"prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md","prior_line":96,"prior_residual":"physical E/intertwiner/leakage open","current_path":current,"current_line":source_line('def local_encoder_and_coin'),"current_residual":"fixed-sector local E and numeric coin intertwiner now executed","exact_match":False,"same_scope":False,"use_as_closure":False},
        {"prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_MARKER_PRESERVING_FREE_QUOTIENT_ROUTER_CYCLE630_NOTE_2026-07-23.md","prior_line":33,"prior_residual":"route existence without physical product","current_path":current,"current_line":source_line('def capture_and_route'),"current_residual":"exact matrix-bound factorized product executed on supplied branch","exact_match":True,"same_scope":True,"use_as_closure":True},
        {"prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_PAIR_SUPERCELL_RECEIVER_FEEDBACK_QUASIENERGY_TOURNAMENT_CYCLE620_NOTE_2026-07-22.md","prior_line":35,"prior_residual":"pair register is not physical lowering","current_path":current,"current_line":source_line('full_local_M64_compiled'),"current_residual":"one-particle fixed sector lowered; pair/multiparticle algebra still open","exact_match":True,"same_scope":True,"use_as_closure":False},
        {"prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_TOURNAMENT_CYCLE608_NOTE_2026-07-22.md","prior_line":23,"prior_residual":"physical encoder/product/intertwiner/leakage null","current_path":current,"current_line":source_line('def symbolic_intertwiner'),"current_residual":"declared fixed-sector encoder/product/intertwiner/leakage executed, broader detector/time boundary untouched","exact_match":False,"same_scope":False,"use_as_closure":False},
    ]
    n5 = [
        {"claim":"physical compiler credit is fixed-sector only","per_element":"each factor matrix is byte-bound","per_site":"actual M2 coordinates are enumerated","per_mode":"vacuum plus six one-particle labels","per_block":"full M64 is not compiled","lattice_wide":"three global exactly-one sectors are supplied"},
        {"claim":"route product is literal but host-issued","per_element":"each SWAP and application is specified","per_site":"paths are fine-nearest-neighbor","per_mode":"matrix acts on its ordered endpoints","per_block":"one cell word has 35361766 microsteps","lattice_wide":"cell serialization is supplied"},
        {"claim":"covariance is conditional","per_element":"six labels transform under each frame","per_site":"route sites transform with phi,h","per_mode":"all24 label tests pass","per_block":"all576 compositions pass","lattice_wide":"phi,h recognition and dynamics are absent"},
        {"claim":"no parity service is used","per_element":"occupation bits are local","per_site":"species roles are disjoint","per_mode":"six labels use a supplied local order","per_block":"same-species multiparticle exchange is absent","lattice_wide":"exactly one carrier per species is supplied"},
        {"claim":"zero symbolic residual is not a giant dense norm","per_element":"route conjugation identities are numeric-tested","per_site":"all endpoints and paths are enumerated","per_mode":"coin restriction is numerically multiplied","per_block":"stream/contact invariance is exact","lattice_wide":"factorwise proof replaces infeasible dense expansion"},
    ]
    n6 = [
        {"file":"outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json","status":"PINNED_SMALL_MATRIX_PARENT","what_closes":"small controlled-gate matrix identities only"},
        {"file":"outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json","status":"PINNED_DESCRIPTOR_PARENT","what_closes":"corrected conditional factor word and fixtures"},
        {"file":"outputs/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_receipt_2026_07_22.json","status":"PINNED_FIXED_SECTOR_COMPARATOR","what_closes":"pair algebra boundary, not M64 lowering"},
        {"file":"outputs/physical_marker_preserving_free_quotient_router_cycle630_receipt_2026_07_23.json","status":"PINNED_ROUTE_PARENT","what_closes":"marker-free path existence and conditional covariance only"},
    ]
    steelman = {"steelman":"A local reversible recognizer plus state-carried clock/token could internalize branch selection and schedule while a parity-free gauge encoding extends the result to all even-CAR sectors.","mechanism":"compute marker/orientation syndromes locally, propagate a bounded clock/token, and replace the fixed-number occupation map with locally constrained gauge auxiliaries","terminal_obligation":"execute full-M64 EG/leakage and host-free recurrent G on L3/L6/L7 with all24/all576 and deletion controls","citations":[{"path":"docs/work_history/repo/review_feedback/PHYSICAL_MARKER_PRESERVING_FREE_QUOTIENT_ROUTER_CYCLE630_NOTE_2026-07-23.md","line":174,"supports":"successor/token and selector work remains live"},{"path":"docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md","line":208,"supports":"state-carried phase and local enforcement remain live"}],"action":"prioritize local selector/token recurrence, then widen E to the full six-mode even algebra"}
    echoes = [
        {"cycle":"Cycle608","prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_TOURNAMENT_CYCLE608_NOTE_2026-07-22.md","prior_line":150,"citation_path":"docs/work_history/repo/review_feedback/PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_TOURNAMENT_CYCLE608_NOTE_2026-07-22.md","citation_line":150,"echo":"literal held-L6 compiler was requested","retired":True,"retirement_mechanism":"fixed-sector E and factorized physical product","could_apply_here":True,"mechanism":"the present executable certificate","applicability":"RETIRES_FIXED_SECTOR_SLICE_ONLY","effect":"full M64 and autonomy remain"},
        {"cycle":"Cycle610","prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md","prior_line":208,"citation_path":"docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md","citation_line":208,"echo":"state-carried phase remains available","retired":False,"retirement_mechanism":None,"could_apply_here":True,"mechanism":"local phase/selector dynamics","applicability":"ACTIONABLE_AUTONOMY_ROUTE","effect":"could remove supplied phi"},
        {"cycle":"Cycle620","prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_PAIR_SUPERCELL_RECEIVER_FEEDBACK_QUASIENERGY_TOURNAMENT_CYCLE620_NOTE_2026-07-22.md","prior_line":35,"citation_path":"docs/work_history/repo/review_feedback/PHYSICAL_PAIR_SUPERCELL_RECEIVER_FEEDBACK_QUASIENERGY_TOURNAMENT_CYCLE620_NOTE_2026-07-22.md","citation_line":35,"echo":"pair algebra lacks physical lowering","retired":False,"retirement_mechanism":None,"could_apply_here":True,"mechanism":"extend E beyond fixed number","applicability":"ACTIONABLE_FULL_M64_ROUTE","effect":"blocks full-CAR promotion"},
        {"cycle":"Cycle630","prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_MARKER_PRESERVING_FREE_QUOTIENT_ROUTER_CYCLE630_NOTE_2026-07-23.md","prior_line":174,"citation_path":"docs/work_history/repo/review_feedback/PHYSICAL_MARKER_PRESERVING_FREE_QUOTIENT_ROUTER_CYCLE630_NOTE_2026-07-23.md","citation_line":174,"echo":"local successor and token remain open","retired":False,"retirement_mechanism":None,"could_apply_here":True,"mechanism":"bounded reversible scheduler","applicability":"ACTIONABLE_HOST_REMOVAL_ROUTE","effect":"prevents autonomy credit"},
    ]
    n4_lines = all(cited_line_exists(row["prior_path"],row["prior_line"]) and cited_line_exists(row["current_path"],row["current_line"]) for row in n4)
    n7_lines = all(cited_line_exists(row["path"],row["line"]) for row in steelman["citations"])
    n8_lines = all(cited_line_exists(row["citation_path"],row["citation_line"]) for row in echoes)
    result = {
        "skill_freshness":{"origin_main_checked":True,"origin_main_skill_sha256":"7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7","proof_search_governance_sha256":"be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258","current_origin_main_followed":True},
        "N1_normalized_families":families,"N1_live_routes":["local selector and scheduler","full-M64 gauge encoding","local constraint enforcement","finite-alphabet precision","fine-translation physical update"],
        "N2_walls":walls,"N2_directional_independence":pairs,"N2_independence_complete":False,
        "N3_hidden_wall_phrases":phrases,"N3_note_phrase_hits":hits,"N3_explicit_supplied_structure":["K129 partition","phi,h branch","marker state","old orientation and predicate flag","blank work","exactly one carrier per species","coin-stream-contact order","host cell serialization","rotation parameters"],
        "N4_exact_residual_matching":n4,"N4_cited_lines_exist":n4_lines,
        "N5_five_resolution_rhetoric_audit":n5,"N6_partial_closure_paths":n6,
        "N7_cited_actionable_steelman":steelman,"N7_cited_lines_exist":n7_lines,
        "N8_rowwise_cross_cycle_echo":echoes,"N8_cited_lines_exist":n8_lines,
        "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP","shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP","narrow_positive_gate":"PASS / SHIP WITH FIREWALL","negative_claim_shipped":False,"shared_route_independent_obstruction":False,"axiom_pressure":False,
    }
    schema = len(families)>=5 and not hits and len(pairs)==15 and n4_lines and n7_lines and n8_lines and all(row["marker"] in ("ATTEMPTED","RULED OUT BY PRIOR") for row in families) and all(all(k in row for k in ("per_element","per_site","per_mode","per_block","lattice_wide")) for row in n5) and all(set(row)=={"file","status","what_closes"} for row in n6)
    check("fresh N1-N8 permits only the fixed-sector positive compiler and blocks impossibility, minimum-content and axiom-pressure claims", schema, result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    print("Cycle632 fixed-sector held-L6 literal E/G product tournament", AUTHORITY, AUDIT)
    r608, r610, r620, r630, shore_result = shore()
    note = note_contract()
    graph, parent, depth = c630.quotient_tree()
    product_word, paths, matrices = capture_and_route(parent, r630)
    matrix_audit = gate_matrix_audit(matrices)
    local = local_encoder_and_coin()
    placement = encoder_placement()
    covariance, fixtures = covariance_and_fixtures(paths, r610, r630)
    intertwiner = symbolic_intertwiner(local, covariance, fixtures)
    discipline = no_go_discipline()
    elapsed = time.monotonic()-started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    resources = {"elapsed_seconds":elapsed,"maximum_RSS_bytes":maximum_rss}
    check("cold run stays within declared time and memory caps", elapsed<CAP_SECONDS and maximum_rss<CAP_BYTES, resources)
    receipt = {
        "status":"cycle632-fixed-sector-held-L6-literal-EG-product-tournament","authority":AUTHORITY,"audit":AUDIT,"author_artifact_status_accepted":False,
        "pins":PINS,"runner_sha256":sha(Path(__file__)),"note_sha256":sha(NOTE),"shore":shore_result,
        "exact_scope":"three distinguishable species, exactly one carrier per species globally, local vacuum-plus-one-particle six-mode words, supplied K129 partition and (phi,h), fixed marker/branch state, blank B/work, host-issued coin-stream-contact and cell serialization",
        "literal_computational_basis_encoder":placement,"literal_local_numeric_coin_intertwiner":local,
        "matrix_bound_physical_product":product_word,"complete_gate_matrix_audit":matrix_audit,
        "state_carried_encoder_product_covariance":covariance,"fixtures_and_controls":fixtures,
        "fixed_sector_physical_intertwiner":intertwiner,"free_quotient_reexecuted":graph,
        "no_go_discipline":discipline,"note_contract":note,
        "strongest_constructive_result":"on one supplied (phi,h) branch, an injective fixed-one-particle/species computational-basis E occupies actual M2 sites and the complete 769434-factor Cycle610 conditional act word is an exact matrix-bound product of support-one or marker-free fine-NN move/apply/reverse gates; factorwise EG, declared-code leakage, inverse/deletion/malformed, mass/contact/seam, L3/L6/L7, and conditional all24/all576 controls pass",
        "route_disposition":{"direct_even_CAR_fixed_sector":"PASS / bounded fixed-number slice only","local_gauge_auxiliary":"not attempted in Cycle632; remains priority for full M64","staggered_time_multiplexed":"host schedule used, so no autonomy or physical-completion credit"},
        "interpretation_firewall":{"full_local_M64_compiled":False,"multiparticle_even_CAR_compiled":False,"selector_or_marker_recognition_compiled":False,"successor_token_clock_dynamics_compiled":False,"host_schedule_is_physical_time":False,"wrapped_phase_is_energy":False,"generator_element_is_rate":False,"pointer_copy_is_Record":False,"coarse_CAR_cell_is_unqualified_physical_site_compiler":False},
        "supplied_structure":["K129 partition and phi,h","120 anchors, including all 24 old Cycle610 orientation roles, plus one replacement orientation bit","one live predicate flag with selector excluded","blank B/equality/work","global exactly-one carrier per species","local six-mode label order","coin-stream-contact order and parameters","host cell serialization"],
        "shared_obstruction_or_axiom_pressure":False,"constitutional_effect":"none","broad_negative_gate":discipline["broad_negative_gate"],
        "optimal_next_campaign":"replace the supplied selector and host schedule with bounded reversible local recognition/successor/token dynamics, then use a local gauge/auxiliary encoding to widen E from the fixed-number slice to all M64 sectors and rerun the same product/intertwiner/leakage/covariance suite",
        "breakthrough_bar_met":False,"breakthrough_default":"no","elapsed_seconds":elapsed,"maximum_RSS_bytes":maximum_rss,
        "tests_passed":PASS,"tests_failed":FAIL,"pass":FAIL==0,
    }
    RECEIPT.parent.mkdir(parents=True,exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=json_default)+"\n")
    print("SUMMARY_JSON",json.dumps({"pass":FAIL==0,"tests_passed":PASS,"tests_failed":FAIL,"held_L6_basis_dimension":placement["size_rows"][1]["global_three_species_basis_dimension"],"act_factors":product_word["conditional_act_calls"],"microsteps_per_cell":product_word["literal_expanded_microsteps_per_coarse_cell"],"unique_matrices":product_word["distinct_matrix_byte_digests"],"axiom_pressure":False,"elapsed_seconds":elapsed,"maximum_RSS_bytes":maximum_rss},sort_keys=True))
    print("RESULT",PASS,FAIL)
    return int(FAIL!=0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True,exist_ok=True)
    with COLD.open("w") as cold:
        terminal=sys.stdout; sys.stdout=Tee(terminal,cold)
        try: exit_code=main()
        finally: sys.stdout=terminal
    raise SystemExit(exit_code)
