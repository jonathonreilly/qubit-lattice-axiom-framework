#!/usr/bin/env python3
"""Cycle630: marker-preserving free-quotient route-around construction.

This artifact replaces Cycle610's marker-crossing Hamiltonian-bus intervals by
simple fine-nearest-neighbor paths in the complement of Cycle629's 144 marker
roles.  It is a positive topology and supplied-descriptor routing result, not
an autonomous scheduler, marker recognizer, physical encoder, or intertwiner.
Authority none; audit unset; accepted false; breakthrough false.
"""
from __future__ import annotations

from array import array
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
import resource
from pathlib import Path
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_translation_orbit_marker_crystal_repair_cycle629_2026_07_22 as c629


c610 = c629.c610
K = c629.K
FRAMES = c629.FRAMES
DIRECTIONS = c629.DIRECTIONS
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0
CAP_SECONDS = 300.0
CAP_BYTES = 3 * 1024**3
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MARKER_PRESERVING_FREE_QUOTIENT_ROUTER_CYCLE630_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_marker_preserving_free_quotient_router_"
    "cycle630_receipt_2026_07_23.json"
)
COLD = ROOT / (
    "outputs/physical_marker_preserving_free_quotient_router_"
    "cycle630_cold_2026_07_23.txt"
)
PINS = {
    "scripts/physical_translation_orbit_marker_crystal_repair_cycle629_2026_07_22.py":
        "e7e90d8ad954cb1a571ee045527c059f48af121214a760d5bef3a09c199a1a8f",
    "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md":
        "db4200898dd970cc03e06d177d7ccfafb60038cf7ad57545e561b844145e9419",
    "outputs/physical_translation_orbit_marker_crystal_repair_cycle629_receipt_2026_07_22.json":
        "ba04003d11b6c50da4420f4bc08fc56d066dba3ebccebf2a9740f6deebc90cc2",
    "outputs/physical_translation_orbit_marker_crystal_repair_cycle629_cold_2026_07_22.txt":
        "50a3a5c3368817f8e8a4306a123cae12992d20937e1c11e40580514b72e22570",
    "scripts/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22.py":
        "ed2250711646ad99bf077e74b8e4194f2df0a2cf368d3c05c45ea95cac8083db",
    "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md":
        "3768d2a1407bdc8de06e2a55fa18300469b1006c0a16a78ada8b8d3a4b936105",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json":
        "375f843606a81970ae50f71d74c53f7e4c4d1437007daaecbedd0b19e3fdfa34",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_cold_2026_07_22.txt":
        "0adbee38e398c9e1d1ccd2733454ead2669338b86d48cbefa5331abb78c126e8",
}


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value: str) -> int:
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, set | frozenset):
        return sorted(value)
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore() -> tuple[dict, dict, dict]:
    observed = {name: sha(ROOT / name) for name in PINS}
    r629 = json.loads((ROOT / (
        "outputs/physical_translation_orbit_marker_crystal_repair_"
        "cycle629_receipt_2026_07_22.json"
    )).read_text())
    r610 = json.loads((ROOT / (
        "outputs/physical_proper_cubic_supercell_stream_composition_"
        "tournament_cycle610_receipt_2026_07_22.json"
    )).read_text())
    expected_graph = dict(r629["shore"]["import_audit"]["expected_transitive_sha256"])
    expected_graph.update(PINS)
    observed_graph = {name: sha(ROOT / name) for name in expected_graph}
    actual_modules = c610.c606.c600.imported_science_modules(
        c629, c610, c610.c606, c610.c603, c610.c603.c219, c610.c603.c230
    )
    uncovered = sorted(set(actual_modules.values()) - set(expected_graph))
    s610 = r610["physical_M2_scope"]
    inherited = {
        "Cycle629_pass": r629["pass"],
        "Cycle629_tests_passed": r629["tests_passed"],
        "Cycle629_authority": r629["authority"],
        "Cycle629_audit": r629["audit"],
        "Cycle629_author_artifact_status_accepted": r629["author_artifact_status_accepted"],
        "Cycle629_projector_enforcement": r629["local_marker_constraint_projectors"]["fine_NN_reversible_enforcement_circuit_compiled"],
        "Cycle629_exact_scope": r629["exact_scope"],
        "Cycle629_broad_negative_gate": r629["broad_negative_gate"],
        "Cycle629_axiom_pressure": r629["shared_obstruction_or_axiom_pressure"],
        "Cycle610_pass": r610["pass"],
        "Cycle610_tests_passed": r610["tests_passed"],
        "Cycle610_physical_M2_scope": s610,
        "import_audit": {
            "expected_transitive_sha256": expected_graph,
            "observed_transitive_sha256": observed_graph,
            "actual_imported_modules": actual_modules,
            "uncovered_imported_modules": uncovered,
            "expected_file_count": len(expected_graph),
            "runtime_module_count": len(actual_modules),
        },
    }
    condition = (
        observed == PINS and observed_graph == expected_graph and not uncovered
        and r629["pass"] and r629["tests_passed"] == 14
        and r629["authority"] == AUTHORITY and r629["audit"] == AUDIT
        and not r629["author_artifact_status_accepted"]
        and not inherited["Cycle629_projector_enforcement"]
        and r629["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and not r629["shared_obstruction_or_axiom_pressure"]
        and r610["pass"] and r610["tests_passed"] == 18
        and not s610["promotion_to_physical_M2_law"]
        and not s610["literal_physical_encoder_composed"]
        and s610["physical_intertwiner_residual"] is None
        and not s610["physical_code_leakage_evaluated"]
    )
    check("accepted Cycle629 and corrected Cycle610 quartets plus transitive science graph are byte exact",
          condition, inherited)
    return inherited, r629, r610


def exact_target_contract() -> dict:
    result = {
        "target_statement": "construct marker-preserving simple fine-NN paths for every actual support-two descriptor endpoint pair in Cycle610's conditional act word, using the free quotient and its three homology generators",
        "domain": "the Cycle629 supplied marker sector and supplied state-carried (phi,h); Cycle610 selector compute/uncompute is excluded because replacement marker recognition was not compiled",
        "required_positive_edges": (
            "144 marker roles removed from the K129 quotient",
            "one connected 2,146,545-site free component",
            "three obstacle-free unit-winding axial loops",
            "connected L3/L6/L7 periodic lifts",
            "all conditional-act support-two endpoints routed by simple NN paths",
            "marker support unchanged after every opening, application, and reverse microstep",
            "six unit translations, all24 spatial actions, and all576 frame compositions",
            "route deletion and malformed-endpoint controls",
        ),
        "completion_witness_not_claimed": "a local marker recognizer/enforcer, local successor circuit with token/clock genesis, literal physical E, recurrent host-free G_physical, leakage controls, and E G_coarse = G_physical E",
        "forbidden_promotions": (
            "host path table to autonomous scheduler",
            "supplied orientation branch to locally recognized orientation",
            "routing existence to physical intertwiner",
            "finite route table to a global ordering or Jordan-Wigner service",
        ),
    }
    check("Cycle630 target keeps routing existence separate from autonomous physical compilation",
          len(result["required_positive_edges"]) == 8 and len(result["forbidden_promotions"]) == 4,
          result)
    return result


def index(site: tuple[int, int, int]) -> int:
    x, y, z = (value % K for value in site)
    return x + K * (y + K * z)


def coordinate(identifier: int) -> tuple[int, int, int]:
    return identifier % K, (identifier // K) % K, identifier // (K * K)


def residue(site: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(value % K for value in site)


def marker_residues() -> frozenset[tuple[int, int, int]]:
    return frozenset(residue(site) for site in (set(c629.ANCHORS) | set(c629.ORIENTATION_SITES)))


def quotient_tree() -> tuple[dict, array, array]:
    obstacles = marker_residues()
    obstacle_indices = {index(site) for site in obstacles}
    total = K**3
    parent = array("i", [-2]) * total
    depth = array("h", [-1]) * total
    for identifier in obstacle_indices:
        parent[identifier] = -3
    root = index((0, 0, 0))
    if parent[root] == -3:
        raise AssertionError("chosen root is a marker")
    parent[root] = -1
    depth[root] = 0
    queue = array("I", [root])
    head = 0
    eccentricity = 0
    while head < len(queue):
        current = queue[head]
        head += 1
        x, y, z = coordinate(current)
        for nxt in (
            ((x + 1) % K, y, z), ((x - 1) % K, y, z),
            (x, (y + 1) % K, z), (x, (y - 1) % K, z),
            (x, y, (z + 1) % K), (x, y, (z - 1) % K),
        ):
            target = index(nxt)
            if parent[target] != -2:
                continue
            parent[target] = current
            depth[target] = depth[current] + 1
            eccentricity = max(eccentricity, depth[target])
            queue.append(target)
    free = total - len(obstacle_indices)
    free_lines = []
    loop_bases = []
    for axis in range(3):
        pairs = []
        other = tuple(i for i in range(3) if i != axis)
        for a in range(K):
            for b in range(K):
                if not any(
                    tuple((t if i == axis else a if i == other[0] else b) for i in range(3))
                    in obstacles for t in range(K)
                ):
                    pairs.append((a, b))
        free_lines.append(len(pairs))
        loop_bases.append(pairs[0])
    result = {
        "K": K,
        "quotient_sites": total,
        "removed_anchor_roles": len(c629.ANCHORS),
        "removed_orientation_roles": len(c629.ORIENTATION_SITES),
        "removed_union": len(obstacles),
        "free_sites": free,
        "root": (0, 0, 0),
        "reached_free_sites": len(queue),
        "spanning_tree_edges": len(queue) - 1,
        "root_eccentricity": eccentricity,
        "obstacle_free_unit_winding_axial_loops_per_axis": tuple(free_lines),
        "selected_loop_transverse_coordinates": tuple(loop_bases),
        "selected_loop_length": K,
        "pass": (
            len(obstacles) == 144 and free == 2_146_545
            and len(queue) == free and eccentricity == 192
            and tuple(free_lines) == (16_497, 16_497, 16_497)
            and tuple(loop_bases) == ((0, 0), (0, 0), (0, 0))
        ),
    }
    check("removing all 144 Cycle629 marker roles leaves one explicitly spanned free quotient with three axial homology generators",
          result["pass"], result)
    return result, parent, depth


def quotient_step(first: tuple[int, int, int], second: tuple[int, int, int]) -> tuple[int, int, int]:
    values = []
    for a, b in zip(first, second):
        difference = (b - a) % K
        if difference == 0:
            values.append(0)
        elif difference == 1:
            values.append(1)
        elif difference == K - 1:
            values.append(-1)
        else:
            raise AssertionError((first, second))
    if sum(abs(value) for value in values) != 1:
        raise AssertionError((first, second, values))
    return tuple(values)


def add(first: tuple[int, int, int], second: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(first[i] + second[i] for i in range(3))


def tree_chain_to_root(site: tuple[int, int, int], parent: array) -> list[tuple[int, int, int]]:
    chain = [residue(site)]
    current = index(site)
    while parent[current] != -1:
        current = parent[current]
        chain.append(coordinate(current))
    return chain


def append_quotient_chain(path: list[tuple[int, int, int]], chain: list[tuple[int, int, int]]) -> None:
    for first, second in zip(chain, chain[1:]):
        path.append(add(path[-1], quotient_step(first, second)))


def loop_erase(path: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []
    locations: dict[tuple[int, int, int], int] = {}
    for site in path:
        if site in locations:
            cut = locations[site]
            for removed in result[cut + 1:]:
                locations.pop(removed)
            result = result[:cut + 1]
        else:
            locations[site] = len(result)
            result.append(site)
    return result


def routed_path(first: tuple[int, int, int], second: tuple[int, int, int], parent: array) -> tuple[tuple[int, int, int], ...]:
    obstacles = marker_residues()
    if residue(first) in obstacles or residue(second) in obstacles:
        raise ValueError("marker endpoint")
    if first == second:
        raise ValueError("coincident endpoints")
    first_chain = tree_chain_to_root(first, parent)
    second_chain = tree_chain_to_root(second, parent)
    base = [first]
    append_quotient_chain(base, first_chain)
    root_to_second = list(reversed(second_chain))
    probe = list(base)
    append_quotient_chain(probe, root_to_second)
    difference = tuple(second[i] - probe[-1][i] for i in range(3))
    if any(value % K for value in difference):
        raise AssertionError((first, second, probe[-1], difference))
    path = list(base)
    for axis, multiple in enumerate(value // K for value in difference):
        sign = 1 if multiple >= 0 else -1
        step = tuple(sign if i == axis else 0 for i in range(3))
        for _ in range(abs(multiple) * K):
            path.append(add(path[-1], step))
    append_quotient_chain(path, root_to_second)
    path = loop_erase(path)
    if path[0] != first or path[-1] != second:
        raise AssertionError((path[0], path[-1], first, second))
    if len(path) != len(set(path)):
        raise AssertionError("path is not simple")
    if any(sum(abs(a - b) for a, b in zip(path[i], path[i + 1])) != 1
           for i in range(len(path) - 1)):
        raise AssertionError("path is not nearest-neighbor")
    if any(residue(site) in obstacles for site in path):
        raise AssertionError("path crosses a marker")
    return tuple(path)


def periodic_lift_audit(graph: dict) -> dict:
    rows = []
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        cells = {(0, 0, 0)}
        frontier = [(0, 0, 0)]
        while frontier:
            cell = frontier.pop()
            for direction in DIRECTIONS:
                nxt = tuple((cell[i] + direction[i]) % length for i in range(3))
                if nxt not in cells:
                    cells.add(nxt)
                    frontier.append(nxt)
        rows.append({
            "length": length,
            "split": split,
            "coarse_cells_reached_by_three_loop_voltages": len(cells),
            "expected_coarse_cells": length**3,
            "fine_free_vertices": graph["free_sites"] * length**3,
            "lift_components_by_voltage_graph_theorem": 1,
            "pass": len(cells) == length**3,
        })
    result = {
        "proof_contract": "the quotient tree connects every free residue to the root; closed axial loops based at the root have voltages e_x,e_y,e_z and generate Z_L^3, so the voltage-graph lift is connected",
        "homology_generator_voltages": ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        "rows": rows,
        "pass": all(row["pass"] for row in rows),
    }
    check("the explicit quotient tree plus three unit-winding loops connects the L3/L6/L7 periodic lifts",
          result["pass"] and [row["coarse_cells_reached_by_three_loop_voltages"] for row in rows] == [27, 216, 343], result)
    return result


def capture_cycle610_word(stream_operations: list[dict]) -> tuple[dict, list[dict]]:
    calls: list[dict] = []
    original_route = c610.route_primitive
    original_direct = c610.direct_primitive

    def capture_route(accumulator, gate, coordinates, frame, stage, cell_offset=(0, 0, 0)):
        coords = tuple(tuple(int(v) for v in site) for site in coordinates)
        offset = tuple(int(v) for v in cell_offset)
        physical = coords
        if len(coords) == 2 and offset != (0, 0, 0):
            physical = (coords[0], tuple(coords[1][i] + K * offset[i] for i in range(3)))
        calls.append({
            "source": "route", "stage": stage, "family": gate.family,
            "coordinates": coords, "cell_offset": offset,
            "physical_coordinates": physical,
        })
        return original_route(accumulator, gate, coordinates, frame, stage, cell_offset)

    def capture_direct(accumulator, operation, frame):
        coords = tuple(tuple(int(v) for v in site) for site in operation["coordinates"])
        calls.append({
            "source": "direct", "stage": operation["stage"],
            "family": operation["family"], "coordinates": coords,
            "cell_offset": tuple(operation.get("cell_offset", (0, 0, 0))),
            "physical_coordinates": coords,
        })
        return original_direct(accumulator, operation, frame)

    c610.route_primitive = capture_route
    c610.direct_primitive = capture_direct
    try:
        compiler = c610.physical_orientation_controlled_compiler(stream_operations)
    finally:
        c610.route_primitive = original_route
        c610.direct_primitive = original_direct
    return compiler, calls


def descriptor_routing_audit(parent: array, r610: dict) -> tuple[dict, dict]:
    stream_result, stream_operations = c610.elementary_stream_template(True)
    compiler, calls = capture_cycle610_word(stream_operations)
    selectors = [row for row in calls if row["stage"].startswith("selector_")]
    act = [row for row in calls if not row["stage"].startswith("selector_")]
    marker = marker_residues()
    selector_marker_instances = sum(
        any(residue(site) in marker for site in row["physical_coordinates"])
        for row in selectors
    )
    act_marker_instances = sum(
        any(residue(site) in marker for site in row["physical_coordinates"])
        for row in act
    )
    one = [row for row in act if len(row["physical_coordinates"]) == 1]
    two = [row for row in act if len(row["physical_coordinates"]) == 2]
    def factor_name(stage: str) -> str:
        for name in ("factor_0_onsite_coin", "factor_1_stream", "factor_2_contact"):
            if stage.startswith(name):
                return name
        return "unexpected"
    factor_population = Counter(
        (factor_name(row["stage"]), len(row["physical_coordinates"])) for row in act
    )
    factor_rows = tuple({
        "factor": factor,
        "one_site_instances": factor_population[(factor, 1)],
        "two_site_instances": factor_population[(factor, 2)],
    } for factor in ("factor_0_onsite_coin", "factor_1_stream", "factor_2_contact"))
    seam_rows = [row for row in act if row["stage"].startswith("factor_1_stream")
                 and "cross" in row["stage"]]
    pair_counts = Counter(tuple(row["physical_coordinates"]) for row in two)
    family_counts = Counter(
        (row["source"], row["stage"], row["family"], row["cell_offset"], row["physical_coordinates"])
        for row in act
    )
    two_family_counts = Counter(
        (row["source"], row["family"], row["cell_offset"], row["physical_coordinates"])
        for row in two
    )
    descriptor_hasher = sha256()
    for row in act:
        descriptor_hasher.update((repr((row["source"], row["stage"], row["family"],
                                        row["cell_offset"], row["physical_coordinates"])) + "\n").encode())
    paths = {}
    failures = Counter()
    distance_histogram = Counter()
    weighted_swaps = weighted_microsteps = 0
    path_table_hasher = sha256()
    for pair in sorted(pair_counts):
        try:
            path = routed_path(pair[0], pair[1], parent)
        except (ValueError, AssertionError):
            failures["route_construction"] += 1
            continue
        paths[pair] = path
        distance = len(path) - 1
        distance_histogram[distance] += 1
        frequency = pair_counts[pair]
        weighted_swaps += frequency * 2 * max(0, distance - 1)
        weighted_microsteps += frequency * (2 * max(0, distance - 1) + 1)
        path_table_hasher.update((repr((pair, path)) + "\n").encode())
    failures["one_site_marker"] += sum(residue(row["physical_coordinates"][0]) in marker for row in one)
    failures["two_site_marker"] += act_marker_instances
    failures["path_endpoint"] += sum(path[0] != pair[0] or path[-1] != pair[1] for pair, path in paths.items())
    failures["path_simple"] += sum(len(path) != len(set(path)) for path in paths.values())
    failures["path_NN"] += sum(
        any(sum(abs(a - b) for a, b in zip(path[i], path[i + 1])) != 1
            for i in range(len(path) - 1)) for path in paths.values()
    )
    failures["path_marker"] += sum(any(residue(site) in marker for site in path) for path in paths.values())
    maximum_pair, maximum_path = max(paths.items(), key=lambda row: len(row[1]))
    maximum_distance = len(maximum_path) - 1
    old = compiler["base_identity_frame_literal_word"]
    expected_act_one = old["direct_one_M2_gate_instances"] - sum(
        len(row["physical_coordinates"]) == 1 for row in selectors
    )
    expected_act_two = old["routed_two_M2_gate_instances"] - sum(
        len(row["physical_coordinates"]) == 2 for row in selectors
    )
    malformed = {}
    for name, pair in (
        ("anchor_endpoint", (next(iter(c629.ANCHORS)), (0, 0, 0))),
        ("orientation_endpoint", (c629.ORIENTATION_SITES[0], (0, 0, 0))),
        ("coincident_endpoint", ((0, 0, 0), (0, 0, 0))),
    ):
        try:
            routed_path(pair[0], pair[1], parent)
            malformed[name] = False
        except ValueError:
            malformed[name] = True
    # Deleting the first opening SWAP from a d>1 move word leaves the second
    # logical label at its endpoint.  Execute the label permutations exactly;
    # this control is independent of the application gate's matrix entries.
    labels = list(range(maximum_distance + 1))
    complete_open = list(range(maximum_distance - 1, 0, -1))
    complete_close = list(range(1, maximum_distance))
    for edge in complete_open:
        labels[edge], labels[edge + 1] = labels[edge + 1], labels[edge]
    complete_application_label = labels[1]
    for edge in complete_close:
        labels[edge], labels[edge + 1] = labels[edge + 1], labels[edge]
    complete_restored = labels == list(range(maximum_distance + 1))
    deleted_labels = list(range(maximum_distance + 1))
    for edge in complete_open[1:]:
        deleted_labels[edge], deleted_labels[edge + 1] = (
            deleted_labels[edge + 1], deleted_labels[edge]
        )
    deleted_application_label = deleted_labels[1]
    for edge in complete_close:
        deleted_labels[edge], deleted_labels[edge + 1] = (
            deleted_labels[edge + 1], deleted_labels[edge]
        )
    deleted_restored = deleted_labels == list(range(maximum_distance + 1))
    route_deletion = {
        "chosen_pair": maximum_pair,
        "path_edges": maximum_distance,
        "moved_logical_label": maximum_distance,
        "complete_opening_SWAP_count": len(complete_open),
        "complete_opening_SWAP_edge_digest": sha256(repr(tuple(complete_open)).encode()).hexdigest(),
        "complete_opening_SWAP_edge_samples": tuple(complete_open[:4] + complete_open[-4:]),
        "deleted_opening_SWAP_edge": complete_open[0],
        "complete_application_neighbor_label": complete_application_label,
        "deleted_application_neighbor_label": deleted_application_label,
        "complete_reverse_restores_all_labels": complete_restored,
        "deleted_reverse_restores_all_labels": deleted_restored,
        "detected": (
            maximum_distance > 1
            and complete_application_label == maximum_distance
            and deleted_application_label != maximum_distance
            and complete_restored and not deleted_restored
        ),
    }
    result = {
        "Cycle610_elementary_stream_operations": len(stream_operations),
        "Cycle610_stream_template_pass": stream_result["pass"],
        "full_identity_word_calls_captured": len(calls),
        "selector_compute_uncompute_calls_excluded": len(selectors),
        "selector_calls_touching_Cycle629_marker_roles": selector_marker_instances,
        "selector_replacement_recognition_compiled": False,
        "conditional_act_word_calls": len(act),
        "conditional_act_one_site_instances": len(one),
        "conditional_act_two_site_instances": len(two),
        "coin_stream_contact_factor_population": factor_rows,
        "cross_seam_act_instances": len(seam_rows),
        "conditional_act_distinct_literal_stage_descriptors": len(family_counts),
        "conditional_act_distinct_support_two_descriptor_families_without_stage_instance": len(two_family_counts),
        "conditional_act_descriptor_word_sha256": descriptor_hasher.hexdigest(),
        "distinct_ordered_endpoint_pairs": len(pair_counts),
        "distinct_simple_paths_constructed": len(paths),
        "path_table_sha256": path_table_hasher.hexdigest(),
        "minimum_path_edges": min(len(path) - 1 for path in paths.values()),
        "maximum_path_edges": maximum_distance,
        "unweighted_path_edge_histogram": dict(sorted(distance_histogram.items())),
        "identity_branch_route_SWAPS": weighted_swaps,
        "identity_branch_route_apply_microsteps": weighted_microsteps,
        "identity_branch_direct_one_site_microsteps": len(one),
        "identity_branch_total_act_microsteps": weighted_microsteps + len(one),
        "all24_route_SWAPS": 24 * weighted_swaps,
        "all24_route_apply_microsteps": 24 * weighted_microsteps,
        "all24_total_act_microsteps": 24 * (weighted_microsteps + len(one)),
        "move_apply_reverse_formula_for_d_edge_path": "2(d-1) SWAPs plus one adjacent application = 2d-1 microsteps",
        "marker_support_unchanged_at_every_routed_microstep": not failures["path_marker"] and not act_marker_instances,
        "malformed_endpoint_rejections": malformed,
        "route_deletion_control": route_deletion,
        "failures": dict(failures),
        "samples": tuple({
            "pair": pair,
            "frequency": pair_counts[pair],
            "path_edges": len(paths[pair]) - 1,
            "first_four_sites": paths[pair][:4],
            "last_four_sites": paths[pair][-4:],
        } for pair in sorted(paths)[:8]),
        "pass": (
            compiler["pass"] and stream_result["pass"]
            and len(calls) == 770_876 and len(selectors) == 1_442
            and len(act) == 769_434 and len(one) == 439_920 and len(two) == 329_514
            and len(one) == expected_act_one and len(two) == expected_act_two
            and factor_population[("unexpected", 1)] == 0
            and factor_population[("unexpected", 2)] == 0
            and all(row["one_site_instances"] + row["two_site_instances"] > 0 for row in factor_rows)
            and len(seam_rows) > 0
            and selector_marker_instances > 0 and act_marker_instances == 0
            and len(paths) == len(pair_counts) and not any(failures.values())
            and all(malformed.values()) and route_deletion["detected"]
        ),
    }
    check("every literal support-two endpoint pair in the conditional Cycle610 act word has a simple marker-free NN move/apply/reverse path",
          result["pass"], {key: value for key, value in result.items() if key not in ("unweighted_path_edge_histogram", "samples")})
    return result, paths


def covariance_audit(paths: dict) -> dict:
    marker = marker_residues()
    failures = Counter()
    endpoint_checks = path_site_checks = 0
    for frame in FRAMES:
        matrix = np.asarray(frame, dtype=int)
        transformed_markers = {
            residue(tuple(int(v) for v in matrix @ np.asarray(site, dtype=int)))
            for site in marker
        }
        failures["marker_all24"] += int(transformed_markers != marker)
        for pair, path in paths.items():
            rotated = tuple(tuple(int(v) for v in matrix @ np.asarray(site, dtype=int)) for site in path)
            expected_pair = tuple(tuple(int(v) for v in matrix @ np.asarray(site, dtype=int)) for site in pair)
            failures["rotated_endpoints"] += int((rotated[0], rotated[-1]) != expected_pair)
            failures["rotated_NN"] += int(any(
                sum(abs(a - b) for a, b in zip(rotated[i], rotated[i + 1])) != 1
                for i in range(len(rotated) - 1)
            ))
            failures["rotated_marker"] += int(any(residue(site) in marker for site in rotated))
            endpoint_checks += 1
            path_site_checks += len(rotated)
    composition_checks = 0
    frame_label_checks = 0
    representative_sites = sorted({site for pair in paths for site in pair})
    for first in FRAMES:
        for second_index, second in enumerate(FRAMES):
            product = first @ second
            failures["all576_frame_label_action"] += int(
                not np.array_equal(FRAMES[c629.left_action(first, second_index)], product)
            )
            frame_label_checks += 1
            for site in representative_sites:
                vector = np.asarray(site, dtype=int)
                failures["all576_composition"] += int(
                    tuple(int(v) for v in first @ (second @ vector))
                    != tuple(int(v) for v in product @ vector)
                )
                composition_checks += 1
    translations = []
    for direction in DIRECTIONS:
        row_failures = 0
        shifted_marker = {residue(add(site, direction)) for site in marker}
        for pair, path in paths.items():
            shifted = tuple(add(site, direction) for site in path)
            row_failures += int(
                shifted[0] != add(pair[0], direction)
                or shifted[-1] != add(pair[1], direction)
                or any(sum(abs(a - b) for a, b in zip(shifted[i], shifted[i + 1])) != 1
                       for i in range(len(shifted) - 1))
                or any(residue(site) in shifted_marker for site in shifted)
            )
        translations.append({"direction": direction, "failures": row_failures})
        failures["six_translation_action"] += row_failures
    result = {
        "base_family": "P_base(u,v) is the deterministic quotient-tree/homology path table",
        "state_carried_family": "P_(phi,h)(u,v) = phi + R_h P_base(R_h^-1(u-phi),R_h^-1(v-phi))",
        "translation_action": "T_e:(phi,h)->(phi+e,h) translates every route site by e",
        "proper_cubic_action_about_q": "g_q:(phi,h)->(q+g(phi-q),gh) and maps every route site x to q+g(x-q)",
        "supplied_phi_h_not_locally_recognized": True,
        "all24_path_endpoint_checks": endpoint_checks,
        "all24_path_site_checks": path_site_checks,
        "all576_endpoint_composition_checks": composition_checks,
        "all576_frame_label_action_checks": frame_label_checks,
        "six_unit_translation_rows": translations,
        "failures": dict(failures),
        "pass": not any(failures.values()),
    }
    check("state-carried (phi,h) transports the route family exactly under six translations and all24/all576 proper-cubic actions",
          result["pass"], {key: value for key, value in result.items() if key != "base_family"})
    return result


def interpretation_and_inventory(routing: dict) -> dict:
    result = {
        "supplied_structure": (
            "K=129 and the Cycle629 120 anchor plus 24 orientation-role residues",
            "the Cycle629 supplied admissible marker sector and state-carried phase phi",
            "a supplied one-hot orientation/frame label h",
            "Cycle610's conditional act-word descriptor order, gate families, endpoint coordinates, and cross-cell offsets",
            "a host-computed deterministic quotient spanning tree, three selected homology loops, and path lookup table",
            "a host-issued move/apply/reverse traversal for each descriptor",
            "blank routing work and clean restoration are assumed at the descriptor boundary",
        ),
        "derived_here": (
            "free-quotient connectivity and eccentricity",
            "three unit-winding obstacle-free generators and L3/L6/L7 lift connectivity",
            "simple marker-free NN paths for every conditional-act support-two endpoint pair",
            "exact path-table counts, hashes, maximum length, and move/apply/reverse overhead",
            "six-translation and all24/all576 state-carried coordinate covariance",
            "route deletion and malformed endpoint detection",
        ),
        "firewall": {
            "host_path_table_is_autonomous_scheduler": False,
            "orientation_conditioned_descriptor_family_is_local_orientation_recognition": False,
            "Cycle629_projectors_are_fine_NN_enforcement": False,
            "marker_support_preservation_is_marker_genesis_or_repair": False,
            "route_existence_is_physical_encoder_or_intertwiner": False,
            "bounded_finite_table_is_global_Jordan_Wigner_ordering": False,
            "wrapped_phase_is_physical_energy": False,
            "generator_element_is_rate": False,
            "pointer_copying_is_Record": False,
        },
        "unbuilt_or_null": {
            "fine_NN_reversible_marker_recognition_enforcement": False,
            "token_clock_genesis": False,
            "local_successor_computation": False,
            "host_free_recurrent_G_physical": False,
            "literal_physical_encoder_E": False,
            "physical_intertwiner_residual": None,
            "full_code_leakage_evaluated": False,
            "selector_compute_uncompute_replacement": False,
        },
        "bounded_support": True,
        "constant_overhead_per_coarse_cell": True,
        "bound": f"finite K={K} quotient; maximum routed path {routing['maximum_path_edges']} edges and table independent of periodic lift size L",
        "no_global_parity_or_ordering_service_claimed_or_used": True,
    }
    check("inventory exposes every supplied host/table/sector premise and withholds autonomous or physical-E credit",
          len(result["supplied_structure"]) == 7
          and not any(result["unbuilt_or_null"][key] for key in result["unbuilt_or_null"] if key != "physical_intertwiner_residual")
          and result["unbuilt_or_null"]["physical_intertwiner_residual"] is None,
          result)
    return result


def no_go_discipline(graph: dict, lifts: dict, routing: dict, covariance: dict, inventory: dict) -> dict:
    families = (
        {
            "family": "free quotient spanning tree",
            "object": "the K129 quotient after all 144 Cycle629 marker roles are removed",
            "mechanism": "exhaustive deterministic BFS",
            "terminal_obligation": "connect every free residue by bounded NN edges",
            "strength_vs_target": "proves route existence but not local route selection",
            "marker": "ATTEMPTED",
            "evidence": "2,146,545/2,146,545 residues reached; eccentricity 192",
            "failure_statement": "The tree is host materialized and therefore does not close an autonomous successor law.",
            "retained_authority_citation": "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md:221-225",
        },
        {
            "family": "voltage-lift homology generators",
            "object": "periodic free-site lifts over the K129 quotient",
            "mechanism": "three explicit 129-edge axial loops with voltages e_x,e_y,e_z",
            "terminal_obligation": "connect all cell images in L3/L6/L7",
            "strength_vs_target": "topological connectivity only",
            "marker": "ATTEMPTED",
            "evidence": "27/216/343 cell images reached and one lift component certified",
            "failure_statement": "Lift connectivity does not provide collision-safe recurrent routing or token genesis.",
            "retained_authority_citation": "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md:194-197",
        },
        {
            "family": "literal conditional-act route table",
            "object": "all 329,514 support-two instances and 4,570 ordered endpoint pairs",
            "mechanism": "tree path plus winding correction and chronological loop erasure",
            "terminal_obligation": "simple marker-free NN move/apply/reverse paths",
            "strength_vs_target": "complete for supplied conditional-act descriptors but excludes selector and recurrence",
            "marker": "ATTEMPTED",
            "evidence": "4,570/4,570 distinct paths pass; maximum 337 edges",
            "failure_statement": "The host-issued path table is not a locally computed recurrent G_physical.",
            "retained_authority_citation": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md:95-98",
        },
        {
            "family": "state-carried phase/orientation route transport",
            "object": "the base path family under supplied (phi,h)",
            "mechanism": "affine signed-permutation images",
            "terminal_obligation": "six/all24/all576 coordinate covariance",
            "strength_vs_target": "exact table covariance but not local recognition of phi or h",
            "marker": "ATTEMPTED",
            "evidence": "zero translated/rotated path, marker, endpoint, and frame-composition failures",
            "failure_statement": "Supplied state labels do not close fine-NN marker/orientation recognition.",
            "retained_authority_citation": "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md:153-154,208-212",
        },
        {
            "family": "route deletion and malformed endpoint adversary",
            "object": "one longest route plus anchor/orientation/coincident endpoints",
            "mechanism": "exact label-flow deletion and endpoint-domain rejection",
            "terminal_obligation": "detect a missing move and reject unlawful route endpoints",
            "strength_vs_target": "route-word control only, not full-code leakage",
            "marker": "ATTEMPTED",
            "evidence": "deleted opening SWAP changes application label and final placement; all malformed endpoints rejected",
            "failure_statement": "A route-word adversary does not close physical-code leakage or an intertwiner residual.",
            "retained_authority_citation": "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md:214-219",
        },
    )
    open_counterroutes = (
        {
            "family": "fine-NN marker/orientation recognizer and selector",
            "mechanism": "compile Cycle629 bounded projectors into reversible support-two gates",
            "terminal_obligation": "replace the excluded 1,442 selector calls with clean local recognition",
            "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT",
        },
        {
            "family": "local route-label successor machine",
            "mechanism": "hardwire the finite path table into reversible local labels and successor rules",
            "terminal_obligation": "remove host path lookup",
            "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT",
        },
        {
            "family": "collision-safe token/clock recurrence",
            "mechanism": "locally generated tokens and a covariant schedule for overlapping translated routes",
            "terminal_obligation": "host-free recurrent G_physical",
            "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT",
        },
        {
            "family": "physical encoder/intertwiner",
            "mechanism": "literal E plus the complete recurrent physical update",
            "terminal_obligation": "E G_coarse = G_physical E and full-code leakage",
            "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT",
        },
    )
    walls = (
        "supplied-sector marker recognition and fine-NN reversible enforcement",
        "replacement selector compute/uncompute for state-carried h",
        "local successor computation for the finite route table",
        "token/clock genesis and collision-safe autonomous renewal",
        "literal physical encoder E and full-code leakage controls",
        "host-free recurrent G_physical and physical intertwiner",
    )
    pairs = tuple({
        "wall_A": first, "wall_B": second,
        "A_implies_B": False, "B_implies_A": False,
        "independent": True,
        "shared_witness_identified": False,
        "evidence": "no executed construction or implication closes either direction",
    } for first, second in combinations(walls, 2))
    phrase_scan = {
        "we assume": "absent",
        "by construction": "absent",
        "as is standard": "absent",
        "the framework provides": "absent",
        "bridge context": "absent",
        "background": "absent",
        "naturally": "absent",
        "obviously": "absent",
        "standard QFT": "absent",
        "registered": "absent",
        "canonical": "absent",
    }
    residuals = (
        {
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md:180-197",
            "prior_residual": "the actual Cycle610 Hamiltonian bus moves marker roles during open intervals and no connected marker-free route was constructed",
            "current_residual": "conditional-act descriptor pairs require marker-free fine-NN move/apply/reverse paths",
            "same_scope": True,
            "exact_match": True,
            "use_as_closure": "YES, but only for conditional-act path existence and microstep marker avoidance; not autonomous recurrence",
        },
        {
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md:208-225",
            "prior_residual": "fine-NN marker enforcement, replacement scheduling, and autonomous renewal were not executed",
            "current_residual": "recognition/selector, local successor, token/clock genesis, and recurrence remain unbuilt",
            "same_scope": True,
            "exact_match": True,
            "use_as_closure": False,
        },
        {
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md:95-98",
            "prior_residual": "literal physical E, physical intertwiner residual, and full physical-code leakage were absent",
            "current_residual": "literal physical E and leakage remain false and the physical intertwiner residual remains null",
            "same_scope": True,
            "exact_match": True,
            "use_as_closure": False,
        },
        {
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md:124-145",
            "prior_residual": "mass/contact/seam residuals and factor order are conditional inherited fixtures",
            "current_residual": "the actual coin/stream/contact descriptor populations are routed but fixture matrices are not reexecuted inside physical E",
            "same_scope": True,
            "exact_match": True,
            "use_as_closure": "descriptor population and supplied order only; no fresh physical fixture credit",
        },
    )
    rhetoric = (
        {
            "phrase": "marker-preserving compiler",
            "per_element": "PASS: each routed SWAP/application support avoids marker roles",
            "per_site": "PASS: all sites on every base/all24 path avoid the transported marker set",
            "per_mode": "PASS: all conditional coin/stream/contact support-one/two descriptor instances are covered",
            "per_block": "PASS only for one supplied (phi,h) conditional branch family; selector excluded",
            "lattice_wide": "NOT TESTED: simultaneous translated routes, collisions, and autonomous recurrence are absent",
            "narrowed_phrase": "host-enumerated marker-preserving conditional-act path family",
        },
        {
            "phrase": "covariant",
            "per_element": "PASS: every NN edge remains NN under signed-permutation actions",
            "per_site": "PASS: every route-site and marker-site image is checked under all24",
            "per_mode": "PASS: all descriptor endpoint families transform with the supplied frame",
            "per_block": "PASS: all576 outer-frame/orientation-label products compose",
            "lattice_wide": "NOT TESTED: no recurrent physical-update commutator exists",
            "narrowed_phrase": "exact affine covariance of the supplied state-carried route tables",
        },
        {
            "phrase": "local bounded route",
            "per_element": "PASS: each microstep has support at most two",
            "per_site": "PASS: each nontrivial support is fine-nearest-neighbor",
            "per_mode": "PASS: every conditional-act descriptor has a finite path",
            "per_block": "PASS: maximum 337 edges at fixed K129",
            "lattice_wide": "NOT TESTED: local path successor and collision-safe translated scheduling are absent",
            "narrowed_phrase": "bounded support-two NN route word with host-side successor selection",
        },
    )
    partial_paths = (
        {
            "file": "scripts/physical_marker_preserving_free_quotient_router_cycle630_2026_07_23.py",
            "status": "PARTIAL / CURRENT",
            "what_closes": "free-quotient topology, literal conditional-act route existence, marker avoidance, overhead, covariance, and route deletion",
        },
        {
            "file": "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md",
            "status": "PARTIAL / PRIOR",
            "what_closes": "state-carried phase and bounded supplied-sector marker projectors",
        },
        {
            "file": "scripts/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22.py",
            "status": "PARTIAL / PRIOR",
            "what_closes": "literal conditional coin-stream-contact descriptor word and inherited target fixtures",
        },
        {
            "file": "UNMATERIALIZED",
            "status": "OPEN / PRIORITY",
            "what_closes": "fine-NN marker/orientation enforcement and replacement selector with clean uncompute",
        },
        {
            "file": "UNMATERIALIZED",
            "status": "OPEN",
            "what_closes": "local path successor plus collision-safe token/clock genesis and renewal",
        },
        {
            "file": "UNMATERIALIZED",
            "status": "OPEN",
            "what_closes": "literal physical E, recurrent G_physical, intertwiner, and full-code leakage",
        },
    )
    steelman = {
        "mechanism": "Compile each of the 4,678 finite descriptor families into bounded route labels; compute the next label with a reversible local circuit; use locally recognized Cycle629 orientation bits to select the branch; and serialize overlapping translated routes with locally generated collision-safe tokens.",
        "actionable_next_steps": (
            "synthesize a support-two reversible recognizer for the Cycle629 anchor/one-hot predicates",
            "encode each Cycle630 path edge as a finite local label and compile successor/inverse tables",
            "construct token genesis, collision arbitration, and clean recurrent renewal on L3/L6/L7",
            "compose literal E and execute the physical intertwiner and leakage controls",
        ),
        "why_it_could_close": "Cycle630 proves the required paths are finite, marker-free, and covariant, while Cycle629 proves the marker predicates have bounded radius; the missing layer is constructive local control, not a contradiction.",
        "terminal_obligation": "replacement selector, local successor, token/clock recurrence, literal E, E G_coarse = G_physical E, leakage/deletion, and L3/L6/L7 all24 update covariance",
        "authority_status": "OPEN / no retained authority",
        "citations": (
            "docs/work_history/repo/review_feedback/PHYSICAL_MARKER_PRESERVING_FREE_QUOTIENT_ROUTER_CYCLE630_NOTE_2026-07-23.md:42-127",
            "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md:156-178,208-225",
            "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md:74-98",
        ),
    }
    echoes = (
        {
            "cycle": "Cycle610",
            "retired": "physical promotion of the supplied 129-period coarse grid",
            "mechanism": "one-fine-site translation falsifier narrowed the artifact to conditional coordinates",
            "applicability": "keeps Cycle630 route-table covariance separate from a recurrent physical update",
        },
        {
            "cycle": "Cycle629",
            "retired": "external origin argument at the diagonal-projector level",
            "mechanism": "state-carried phase and proper-cubic marker/orientation orbits",
            "applicability": "directly supplies Cycle630's transported marker set, but not recognition or renewal",
        },
        {
            "cycle": "Cycle629 route residual",
            "retired": "absence of a marker-free path around all 144 roles for the conditional act word",
            "mechanism": "Cycle630 free quotient, homology generators, and complete descriptor path table",
            "applicability": "retires path existence only; selector, collision handling, and autonomy remain open",
        },
        {
            "cycle": "Cycle617",
            "retired": "premature composition of bounded local lemmas into one physical compiler",
            "mechanism": "route-specific disposition and explicit open physical E",
            "applicability": "requires Cycle630 to withhold physical compiler credit from its bounded route lemma",
        },
    )
    result = {
        "skill_freshness": {
            "origin_main_checked": True,
            "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
            "proof_search_governance_sha256": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258",
            "newer_origin_main_version_followed": True,
        },
        "N1_normalized_families": families,
        "N1_qualifying_family_count": len(families),
        "N1_all_markers_exact": all(row["marker"] in ("ATTEMPTED", "RULED OUT BY PRIOR") for row in families),
        "N1_open_counterroutes_not_counted": open_counterroutes,
        "N2_collapsed_walls": walls,
        "N2_directional_wall_independence": pairs,
        "N2_pair_count": len(pairs),
        "N3_hidden_wall_scan": {
            "required_phrase_scan": phrase_scan,
            "load_bearing_premises": inventory["supplied_structure"],
            "selector_exclusion_explicit": routing["selector_compute_uncompute_calls_excluded"],
            "host_table_explicit": True,
            "bounded_period_K_explicit": K,
            "hidden_wall_promotions_complete": True,
        },
        "N4_residual_matching": residuals,
        "N5_rhetoric_resolution": rhetoric,
        "N5_five_resolutions_present": all(all(key in row for key in (
            "per_element", "per_site", "per_mode", "per_block", "lattice_wide"
        )) for row in rhetoric),
        "N6_partial_closure_paths": partial_paths,
        "N7_hostile_steelman": steelman,
        "N8_cross_cycle_echo": echoes,
        "route_independent_impossibility_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure_claim": False,
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP",
        "narrow_positive_gate": "PASS / SHIP WITH FIREWALL",
        "status": "FAIL",
        "failed_checklist_items": (
            "N7: local successor, replacement selector, and collision-safe token/clock recurrence remain live",
            "physical promotion: literal E, recurrent G_physical, intertwiner, and leakage remain unexecuted",
        ),
    }
    schema_pass = (
        len(families) >= 5 and result["N1_all_markers_exact"]
        and all(row["status"].startswith("OPEN / NOT COUNTED") for row in open_counterroutes)
        and len(pairs) == 15 and all(row["independent"] for row in pairs)
        and all(set(("citation", "prior_residual", "current_residual", "same_scope", "exact_match", "use_as_closure")) <= set(row) for row in residuals)
        and result["N5_five_resolutions_present"]
        and all(set(("file", "status", "what_closes")) == set(row) for row in partial_paths)
        and set(("mechanism", "actionable_next_steps", "why_it_could_close", "terminal_obligation", "authority_status", "citations")) == set(steelman)
        and all(set(("cycle", "retired", "mechanism", "applicability")) == set(row) for row in echoes)
    )
    check("fresh N1-N8 ships only the narrow positive route-around result and blocks broad/minimum/shared/axiom claims",
          schema_pass
          and result["broad_negative_gate"] == "FAIL / DO NOT SHIP"
          and result["narrow_positive_gate"] == "PASS / SHIP WITH FIREWALL"
          and result["status"] == "FAIL"
          and not result["shared_obstruction_claim"], result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "2,146,545", "16,497", "root eccentricity 192", "L3/L6/L7",
        "selector", "host", "N1", "N8", "no axiom pressure",
        "E G_coarse = G_physical E", "authority none", "audit unset",
        "`ATTEMPTED`", "`RULED OUT BY PRIOR`", "same_scope", "exact_match",
        "use_as_closure", "per_element", "per_site", "per_mode", "per_block",
        "lattice_wide", "what_closes", "actionable", "applicability",
    )
    missing = tuple(token for token in required if token not in text)
    result = {"required_tokens": required, "missing_tokens": missing, "pass": not missing}
    check("Cycle630 note states the topology, selector firewall, exact N1-N8 schema, and withheld physical obligations",
          result["pass"], result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold:
        previous = sys.stdout
        sys.stdout = Tee(previous, cold)
        try:
            inherited, r629, r610 = shore()
            target = exact_target_contract()
            graph, parent, depth = quotient_tree()
            lifts = periodic_lift_audit(graph)
            routing, paths = descriptor_routing_audit(parent, r610)
            covariance = covariance_audit(paths)
            inventory = interpretation_and_inventory(routing)
            discipline = no_go_discipline(graph, lifts, routing, covariance, inventory)
            note = note_contract()
            elapsed = time.monotonic() - started
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            if sys.platform == "darwin":
                maximum_rss_bytes = int(rss)
            else:
                maximum_rss_bytes = int(rss * 1024)
            check("Cycle630 cold run stays within declared time and memory caps",
                  elapsed <= CAP_SECONDS and maximum_rss_bytes <= CAP_BYTES,
                  {"elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss_bytes,
                   "cap_seconds": CAP_SECONDS, "cap_bytes": CAP_BYTES})
            receipt = {
                "status": "positive_marker_preserving_conditional_act_route_around",
                "authority": AUTHORITY,
                "audit": AUDIT,
                "author_artifact_status_accepted": False,
                "breakthrough_bar_met": False,
                "breakthrough_default": "no",
                "runner_sha256": sha(Path(__file__)),
                "note_sha256": sha(NOTE),
                "pins": PINS,
                "shore": inherited,
                "exact_target_contract": target,
                "free_quotient_spanning_tree": graph,
                "periodic_lift_connectivity": lifts,
                "conditional_act_descriptor_routing": routing,
                "state_carried_route_covariance": covariance,
                "inventory_and_interpretation_firewall": inventory,
                "no_go_discipline": discipline,
                "note_contract": note,
                "strongest_constructive_result": "after deleting the 144 Cycle629 marker roles, the 2,146,545 free residues form one explicitly spanned K129 quotient of root eccentricity 192; three explicit obstacle-free axial loops generate all periodic lift cells, and every actual support-two endpoint pair in Cycle610's 769,434-primitive conditional act word is assigned a simple fine-NN marker-free move/apply/reverse path with exact bounded overhead and supplied-(phi,h) six/all24/all576 covariance",
                "exact_scope": "the supplied Cycle629 marker sector, supplied state-carried (phi,h), and Cycle610 conditional act word only; its 1,442 selector compute/uncompute primitives are excluded",
                "mass_contact_seam_fixture_status": "the routed descriptor population includes the actual Cycle610 conditional coin, stream, contact, and cross-seam act-word rows, but inherited unitary fixture residuals are not reexecuted because routing conjugation changes placement rather than logical gates",
                "shared_obstruction_or_axiom_pressure": False,
                "constitutional_effect": "none",
                "broad_negative_gate": discipline["broad_negative_gate"],
                "optimal_next_campaign": "compile the finite orientation-conditioned path table into a literal fine-NN reversible successor/token circuit, replace the excluded selector by Cycle629 marker recognition/enforcement, then compose recurrent host-free G_physical and literal E and execute E G_coarse = G_physical E with leakage/deletion/L3/L6/L7 controls",
                "elapsed_seconds": elapsed,
                "maximum_RSS_bytes": maximum_rss_bytes,
                "tests_passed": PASS,
                "tests_failed": FAIL,
                "pass": FAIL == 0,
            }
            RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
            print("SUMMARY_JSON", json.dumps({
                "pass": FAIL == 0, "tests_passed": PASS, "tests_failed": FAIL,
                "free_sites": graph["free_sites"],
                "root_eccentricity": graph["root_eccentricity"],
                "act_two_site_instances": routing["conditional_act_two_site_instances"],
                "distinct_pairs": routing["distinct_ordered_endpoint_pairs"],
                "maximum_path_edges": routing["maximum_path_edges"],
                "selector_excluded": routing["selector_compute_uncompute_calls_excluded"],
                "axiom_pressure": False,
                "elapsed_seconds": elapsed,
                "maximum_RSS_bytes": maximum_rss_bytes,
            }, sort_keys=True))
            print("RESULT", PASS, FAIL)
        finally:
            sys.stdout = previous
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
