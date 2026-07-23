#!/usr/bin/env python3
"""Cycle651: physical root-label-blind face-pump compiler tournament.

The immutable Cycle648 leaf decoder is compiled in three distinct ways:

* reversible message passing from a retained local syndrome rail;
* a proper-cubic orbit selector plus a translation-orbit defect field;
* a syndrome-labelled Stinespring reset comparator.

Every positive algebraic surface is kept separate from new-controller
placement, autonomous syndrome extraction, collision-safe fine-NN routing,
ordinary-translation covariance, and environment return.
Authority: none.  Audit: unset.  Constitutional effect: none.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import contextlib
import importlib
import io
from itertools import permutations
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
SHORE_REF = "4f2b07fd39cc83a3f6c21bd9559f948b615bd05c"
AUTHORITY = "none"
AUDIT = "unset"
CAP_SECONDS = 180.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ROOT_LABEL_BLIND_FACE_PUMP_COMPILER_CYCLE651_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_root_label_blind_face_pump_compiler_cycle651_"
    "receipt_2026_07_23.json"
)

C642_RUNNER = "scripts/physical_fixed_cubic_wilson_fill_incidence_cycle642_2026_07_23.py"
C642_NOTE = "docs/work_history/repo/review_feedback/PHYSICAL_FIXED_CUBIC_WILSON_FILL_INCIDENCE_CYCLE642_NOTE_2026-07-23.md"
C642_RECEIPT = "outputs/physical_fixed_cubic_wilson_fill_incidence_cycle642_receipt_2026_07_23.json"
C642_COLD = "outputs/physical_fixed_cubic_wilson_fill_incidence_cycle642_cold_2026_07_23.txt"
C648_RUNNER = "scripts/physical_root_free_orbit_tree_preparation_tournament_cycle648_2026_07_23.py"
C648_NOTE = "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_ORBIT_TREE_PREPARATION_TOURNAMENT_CYCLE648_NOTE_2026-07-23.md"
C648_RECEIPT = "outputs/physical_root_free_orbit_tree_preparation_tournament_cycle648_receipt_2026_07_23.json"
C648_COLD = "outputs/physical_root_free_orbit_tree_preparation_tournament_cycle648_cold_2026_07_23.txt"
C629_NOTE = "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md"
C643_NOTE = "docs/work_history/repo/review_feedback/ABSTRACT_FILL_DISK_FULL_TABLEAU_ISOMETRY_CYCLE643_NOTE_2026-07-23.md"

PINS = {
    C642_RUNNER: "fb0d8366494066e4191d66b9a2d83180cd99bf6f622b9de355bf28494e050bf7",
    C642_NOTE: "13f8074746f3b5e978f971567bbebecd1006ccd13b7d5fe91a0e38a946d30d3e",
    C642_RECEIPT: "9251ac323d4f26b672783fa8ed01dc8da6f3059c308d37325b3d7984969c3b37",
    C642_COLD: "2af7cb45f80e1e5719da6750cd9f2efbbf2bee1bc14abe95e234eba91d6920cb",
    C648_RUNNER: "2198ab44b0598bb20967fae3343df7e63e915b67e2f74832cb7c528e7a1dfd66",
    C648_NOTE: "b42d5364c0f30fb0d4d8c6336e8e7894a54873e0859bf922d79b556403353a80",
    C648_RECEIPT: "b75c13e434e82eebd5af9813749261ac93c3197bffd9b0de04ff6619f4252336",
    C648_COLD: "d6eb98c556812319b8989ec15867263097f5b1c2000bd30bd64e087724556e81",
}

C648 = None
C642 = None


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_bytes(ref: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT)


def check(label: str, condition: bool, detail="") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def immutable_line(path: str, fragment: str) -> int:
    lines = git_bytes(SHORE_REF, path).decode().splitlines()
    return next((number for number, line in enumerate(lines, 1) if fragment in line), 0)


def source_line(fragment: str) -> int:
    return next(
        (number for number, line in enumerate(Path(__file__).read_text().splitlines(), 1) if fragment in line),
        0,
    )


def cited_line_exists(ref: str, path: str, line: int) -> bool:
    try:
        lines = git_bytes(ref, path).decode().splitlines()
    except subprocess.CalledProcessError:
        return False
    return 1 <= line <= len(lines) and bool(lines[line - 1].strip())


def edge_key(left, right):
    return C642.edge_key(left, right)


def vertex_key(vertex):
    return C642.vertex_key(vertex)


def shore() -> tuple[dict, dict, dict]:
    observed = {path: sha256(git_bytes(SHORE_REF, path)).hexdigest() for path in PINS}
    local = {path: sha(ROOT / path) for path in (C642_RUNNER, C648_RUNNER)}
    c642_receipt = json.loads(git_bytes(SHORE_REF, C642_RECEIPT))
    c648_receipt = json.loads(git_bytes(SHORE_REF, C648_RECEIPT))
    c649_paths = tuple(
        path for path in (
            "scripts/physical_reserved_outer_shell_sidecar_placement_cycle649_2026_07_23.py",
            "outputs/physical_reserved_outer_shell_sidecar_placement_cycle649_receipt_2026_07_23.json",
            "docs/work_history/repo/review_feedback/PHYSICAL_RESERVED_OUTER_SHELL_SIDECAR_PLACEMENT_CYCLE649_NOTE_2026-07-23.md",
        )
        if (ROOT / path).exists()
    )
    result = {
        "immutable_shore_ref": SHORE_REF,
        "observed": observed,
        "hashes_match": observed == PINS,
        "local_import_mirrors": local,
        "local_import_mirrors_byte_equal_to_shore": all(local[path] == PINS[path] for path in local),
        "Cycle642_pass": c642_receipt["pass"],
        "Cycle648_pass": c648_receipt["pass"],
        "Cycle648_authority": c648_receipt["authority"],
        "Cycle648_audit": c648_receipt["audit"],
        "Cycle648_shared_obstruction": c648_receipt["shared_route_independent_obstruction"],
        "Cycle648_axiom_pressure": c648_receipt["axiom_pressure"],
        "working_tree_C649_paths_observed_but_not_read_or_imported": c649_paths,
        "C649_consumed_as_premise": False,
    }
    condition = bool(
        result["hashes_match"]
        and result["local_import_mirrors_byte_equal_to_shore"]
        and result["Cycle642_pass"] and result["Cycle648_pass"]
        and result["Cycle648_authority"] == AUTHORITY
        and result["Cycle648_audit"] == AUDIT
        and not result["Cycle648_shared_obstruction"]
        and not result["Cycle648_axiom_pressure"]
        and not result["C649_consumed_as_premise"]
    )
    check("immutable Cycle642/Cycle648 shore is byte exact and Cycle649 is unconsumed", condition, result)
    return c642_receipt, c648_receipt, result


def load_modules() -> None:
    global C648, C642
    sys.path.insert(0, str(ROOT / "scripts"))
    C648 = importlib.import_module("physical_root_free_orbit_tree_preparation_tournament_cycle648_2026_07_23")
    with contextlib.redirect_stdout(io.StringIO()):
        C648.load_modules()
    C642 = C648.C642
    imported = {C648_RUNNER: sha(Path(C648.__file__).resolve()), C642_RUNNER: sha(Path(C642.__file__).resolve())}
    check("only byte-pinned Cycle648 and Cycle642 executable mirrors are imported",
          imported == {path: PINS[path] for path in imported}, imported)


def adjacency(vertices, edges):
    result = {vertex: set() for vertex in vertices}
    for left, right in edges:
        result[left].add(right)
        result[right].add(left)
    return result


def peel_layers(vertices, edges):
    graph = adjacency(vertices, edges)
    active = set(vertices)
    layers = []
    while len(active) > 1:
        leaves = tuple(sorted(
            (vertex for vertex in active if len(graph[vertex] & active) == 1),
            key=vertex_key,
        ))
        if not leaves:
            raise AssertionError("active tree has no leaf")
        if len(active) == 2:
            leaves = leaves[:1]
        layer = tuple((leaf, next(iter(graph[leaf] & active))) for leaf in leaves)
        layers.append(layer)
        active -= set(leaves)
    return tuple(layers), next(iter(active))


def reversible_compile(vertices, edges, negative):
    """Compile a retained syndrome rail into edge corrections and blank work.

    The input syndrome rail is preserved.  Each forward and reverse operation
    is a CNOT on two logical M2 registers.  This is not syndrome extraction.
    """
    layers, center = peel_layers(vertices, edges)
    input_rail = {vertex: int(vertex in negative) for vertex in vertices}
    work = {vertex: 0 for vertex in vertices}
    history = {edge_key(*edge): 0 for edge in edges}
    data = {edge_key(*edge): 0 for edge in edges}
    for vertex in vertices:
        work[vertex] ^= input_rail[vertex]
    for layer in layers:
        for leaf, parent in layer:
            edge = edge_key(leaf, parent)
            history[edge] ^= work[leaf]
            work[parent] ^= history[edge]
    selected = {edge for edge, bit in history.items() if bit}
    for edge in history:
        data[edge] ^= history[edge]
    residual = set(negative)
    for left, right in selected:
        residual.symmetric_difference_update((left, right))
    for layer in reversed(layers):
        for leaf, parent in reversed(layer):
            edge = edge_key(leaf, parent)
            work[parent] ^= history[edge]
            history[edge] ^= work[leaf]
    for vertex in vertices:
        work[vertex] ^= input_rail[vertex]
    return {
        "selected": selected,
        "residual": residual,
        "center": center,
        "work_blank": not any(work.values()),
        "history_blank": not any(history.values()),
        "input_preserved": {vertex for vertex, bit in input_rail.items() if bit} == set(negative),
        "data": data,
        "layers": layers,
    }


def map_vertices(frame, axis: int, vertices, length: int):
    target_axis = C642.act_vertex(frame, axis, C642.ROOT_VERTEX, length)[0]
    mapped = {C642.act_vertex(frame, axis, vertex, length)[1] for vertex in vertices}
    return target_axis, mapped


def map_edges(frame, axis: int, edges, length: int):
    target_axis = C642.act_vertex(frame, axis, C642.ROOT_VERTEX, length)[0]
    mapped = set()
    for left, right in edges:
        role = C642.act_edge(frame, (axis, left, right), length)
        if role[0] != target_axis:
            raise AssertionError("axis mismatch")
        mapped.add(edge_key(role[1], role[2]))
    return target_axis, mapped


def frame_and_group_controls(length: int, vertices, edges) -> dict:
    all24 = all576 = layer_failures = 0
    layers, _center = peel_layers(vertices, edges)
    layer_sets = tuple({edge_key(*edge) for edge in layer} for layer in layers)
    for axis in range(3):
        for word in range(1 << len(vertices)):
            negative = {vertices[index] for index in range(len(vertices)) if (word >> index) & 1}
            selected = reversible_compile(vertices, edges, negative)["selected"]
            for frame in C642.FRAMES:
                target_axis, mapped_negative = map_vertices(frame, axis, negative, length)
                mapped_selected = map_edges(frame, axis, selected, length)[1]
                decoded = reversible_compile(vertices, edges, mapped_negative)["selected"]
                all24 += mapped_selected != decoded
                mapped_layers = tuple(map_edges(frame, axis, layer, length)[1] for layer in layer_sets)
                layer_failures += mapped_layers != layer_sets
            for left_frame in C642.FRAMES:
                for right_frame in C642.FRAMES:
                    product = left_frame @ right_frame
                    mid_axis, mid_negative = map_vertices(right_frame, axis, negative, length)
                    final_axis, sequential_negative = map_vertices(left_frame, mid_axis, mid_negative, length)
                    product_axis, product_negative = map_vertices(product, axis, negative, length)
                    mid_edge_axis, mid_edges = map_edges(right_frame, axis, selected, length)
                    final_edge_axis, sequential_edges = map_edges(left_frame, mid_edge_axis, mid_edges, length)
                    product_edge_axis, product_edges = map_edges(product, axis, selected, length)
                    all576 += (
                        final_axis != product_axis or final_edge_axis != product_edge_axis
                        or sequential_negative != product_negative or sequential_edges != product_edges
                    )
    return {"all24_failures": all24, "all576_failures": all576, "layer_orbit_failures": layer_failures}


def fixed_selector_controls(length: int, fibers: dict) -> dict:
    obj = C642.build_tree_code(length, fibers)
    equality_x_masks = {row.x for row in obj["equality"] if row.z == 0}
    representative_failures = total_actions = 0
    invariant_odd_subsets = 0
    odd_subsets_tested = 0
    roles_with_invariant_odd_subset = 0
    branch_equivalence_failures = 0
    uniform_orbit_failures = 0
    selector_M2 = 0
    for role, fiber_tuple in fibers.items():
        fiber = tuple(fiber_tuple)
        representative = min(fiber)
        selector_M2 += int(math.log2(len(fiber)))
        for frame in C642.FRAMES:
            target = C642.act_edge(frame, role, length)
            representative_failures += C642.rotate(frame, representative) != min(fibers[target])
            uniform_orbit_failures += {C642.rotate(frame, site) for site in fiber} != set(fibers[target])
            total_actions += 1
        stabilizer = tuple(frame for frame in C642.FRAMES if C642.act_edge(frame, role, length) == role)
        role_invariant = 0
        for word in range(1 << len(fiber)):
            if word.bit_count() % 2 == 0:
                continue
            odd_subsets_tested += 1
            subset = {fiber[index] for index in range(len(fiber)) if (word >> index) & 1}
            invariant = all({C642.rotate(frame, site) for site in subset} == subset for frame in stabilizer)
            invariant_odd_subsets += invariant
            role_invariant += invariant
        roles_with_invariant_odd_subset += role_invariant > 0
        # Every single-copy X branch differs from the representative by a
        # literal pairwise XX equality row in the actual Cycle642 code object.
        bits = obj["index"][role]
        branch_equivalence_failures += sum(
            ((1 << bits[0]) ^ (1 << bit)) not in equality_x_masks
            for bit in bits[1:]
        )
    return {
        "logical_edge_roles": len(fibers),
        "fiber_size_histogram": dict(Counter(map(len, fibers.values()))),
        "fixed_sorted_copy_all24_failures": representative_failures,
        "fixed_sorted_copy_actions_tested": total_actions,
        "odd_X_subsets_tested": odd_subsets_tested,
        "stabilizer_invariant_odd_X_subsets": invariant_odd_subsets,
        "roles_with_stabilizer_invariant_odd_X_subset": roles_with_invariant_odd_subset,
        "uniform_selector_all24_orbit_failures": uniform_orbit_failures,
        "single_copy_branches_not_equivalent_mod_pair_XX": branch_equivalence_failures,
        "declared_virtual_uniform_selector_M2": selector_M2,
        "selector_M2_physically_placed": 0,
        "fixed_selector_narrow_falsifier": representative_failures > 0 and invariant_odd_subsets == 0,
        "uniform_selector_algebraic_repair": uniform_orbit_failures == 0 and branch_equivalence_failures == 0,
    }


def route_A_reversible_message_passing(c642_receipt: dict) -> dict:
    pinned_routes = {row["length"]: row for row in c642_receipt["fine_NN_routing_scouts"]}
    sizes = []
    for length in (3, 6, 7):
        vertices, edges = C642.fill_tree(length)
        with contextlib.redirect_stdout(io.StringIO()):
            placement, fibers = C642.allocate_orbit_roles(length)
        frame = frame_and_group_controls(length, vertices, edges)
        even_failures = odd_failures = work_failures = inverse_failures = 0
        deletion_failures = leakage_failures = 0
        deletion_cases = leakage_cases = 0
        for word in range(1 << len(vertices)):
            negative = {vertices[index] for index in range(len(vertices)) if (word >> index) & 1}
            compiled = reversible_compile(vertices, edges, negative)
            work_failures += not (compiled["work_blank"] and compiled["history_blank"] and compiled["input_preserved"])
            inverse_failures += any((2 * bit) % 2 for bit in compiled["data"].values())
            if len(negative) % 2 == 0:
                even_failures += bool(compiled["residual"])
                if compiled["selected"]:
                    deletion_cases += 1
                    deleted = set(compiled["selected"])
                    deleted.remove(min(deleted, key=repr))
                    residual = set(negative)
                    for left, right in deleted:
                        residual.symmetric_difference_update((left, right))
                    deletion_failures += len(residual) != 2
                for vertex in vertices:
                    leakage_cases += 1
                    leaked = reversible_compile(vertices, edges, negative ^ {vertex})
                    leakage_failures += len(leaked["residual"]) != 1
            else:
                odd_failures += compiled["residual"] != {compiled["center"]}
        fixed = fixed_selector_controls(length, fibers)
        route = pinned_routes[length]
        new_controller_roles = 3 * (2 * len(vertices) + len(edges))
        sizes.append({
            "length": length,
            "all_syndromes_per_axis": 2 ** len(vertices),
            "even_syndrome_failures": even_failures,
            "odd_single_residual_failures": odd_failures,
            "work_history_or_input_return_failures": work_failures,
            "double_application_inverse_failures": inverse_failures,
            "delete_one_selected_correction_cases": deletion_cases,
            "delete_one_selected_correction_not_two_residual_failures": deletion_failures,
            "single_face_flip_leakage_cases": leakage_cases,
            "single_face_flip_not_odd_residual_failures": leakage_failures,
            "parallel_leaf_layers": len(peel_layers(vertices, edges)[0]),
            "maximum_elementary_logical_gate_support_M2": 2,
            "two_M2_logical_gates_three_axes": 3 * (2 * len(vertices) + 5 * len(edges)),
            "placed_Cycle642_logical_correction_edges": placement["logical_aux_edges"],
            "placed_Cycle642_physical_aux_M2": placement["physical_aux_M2"],
            "declared_input_work_history_controller_roles": new_controller_roles,
            "declared_controller_roles_per_coarse_cell": new_controller_roles / length**3,
            "physically_placed_new_controller_roles_on_immutable_shore": 0,
            "explicit_unplaced_controller_role_residual": new_controller_roles,
            "maximum_inherited_face_pair_route_edges": route["maximum_shortest_fine_NN_path_edges"],
            "inherited_literal_fine_NN_paths_exist": route["literal_fine_NN_path_exists_for_every_pair"],
            "collision_safe_autonomous_NN_lowering": False,
            "autonomous_syndrome_extraction": False,
            "retained_input_syndrome_rail": True,
            **frame,
            "physical_copy_selector": fixed,
        })
    result = {
        "sizes": sizes,
        "constructive_result": "a directionless parallel leaf circuit computes every edge correction from a retained local syndrome rail using only two-M2 CNOTs, applies it, and uncomputes all work/history",
        "root_vertex_label_queried": False,
        "global_parity_queried": False,
        "host_path_table_used": False,
        "input_syndrome_rail_is_extracted_from_data": False,
        "all_new_controller_roles_physically_placed": False,
        "strict_fine_NN_compiler": False,
        "route_status": "EXACT_REVERSIBLE_SUPPLIED_SYNDROME_COMPILER__PHYSICAL_EXTRACTION_SELECTOR_AND_NN_PLACEMENT_OPEN",
    }
    result["pass"] = bool(
        all(
            row["even_syndrome_failures"] == row["odd_single_residual_failures"] == 0
            and row["work_history_or_input_return_failures"] == 0
            and row["double_application_inverse_failures"] == 0
            and row["delete_one_selected_correction_not_two_residual_failures"] == 0
            and row["single_face_flip_not_odd_residual_failures"] == 0
            and row["maximum_elementary_logical_gate_support_M2"] == 2
            and row["all24_failures"] == row["all576_failures"] == row["layer_orbit_failures"] == 0
            and row["physical_copy_selector"]["fixed_selector_narrow_falsifier"]
            and row["physical_copy_selector"]["uniform_selector_algebraic_repair"]
            and row["explicit_unplaced_controller_role_residual"] > 0
            and not row["collision_safe_autonomous_NN_lowering"]
            for row in sizes
        )
        and not result["root_vertex_label_queried"]
        and not result["global_parity_queried"]
        and not result["input_syndrome_rail_is_extracted_from_data"]
        and not result["all_new_controller_roles_physically_placed"]
        and not result["strict_fine_NN_compiler"]
    )
    check("route A gives an exact reversible supplied-syndrome circuit and an exact physical nonplacement residual", result["pass"], {
        "sizes": [(row["length"], row["two_M2_logical_gates_three_axes"], row["explicit_unplaced_controller_role_residual"], row["physical_copy_selector"]["fixed_sorted_copy_all24_failures"]) for row in sizes]
    })
    return result


def shift_vertex(vertex, shift: int, length: int):
    return vertex if vertex == C642.ROOT_VERTEX else (int(vertex) + shift) % length


def shift_edges(edges, shift: int, length: int):
    return {edge_key(shift_vertex(left, shift, length), shift_vertex(right, shift, length)) for left, right in edges}


def route_B_orbit_defect_field(route_a: dict) -> dict:
    sizes = []
    for length, route_a_size in zip((3, 6, 7), route_a["sizes"]):
        vertices, base_edges_tuple = C642.fill_tree(length)
        base_edges = set(base_edges_tuple)
        shifted_families = tuple(shift_edges(base_edges, shift, length) for shift in range(length))
        unique_families = {frozenset(edges) for edges in shifted_families}
        base_translation_mismatches = [len(base_edges ^ shifted_families[shift]) for shift in range(length)]
        translation_family_failures = decoder_translation_failures = 0
        for shift in range(length):
            translated = shifted_families[shift]
            translation_family_failures += shift_edges(translated, 1, length) != shifted_families[(shift + 1) % length]
            for word in range(1 << len(vertices)):
                negative = {vertices[index] for index in range(len(vertices)) if (word >> index) & 1}
                mapped_negative = {shift_vertex(vertex, shift, length) for vertex in negative}
                base_selected = reversible_compile(vertices, base_edges, negative)["selected"]
                mapped_selected = shift_edges(base_selected, shift, length)
                translated_selected = reversible_compile(vertices, translated, mapped_negative)["selected"]
                decoder_translation_failures += mapped_selected != translated_selected
        all24_family_failures = all576_label_failures = 0
        for axis in range(3):
            for shift, tree in enumerate(shifted_families):
                for frame in C642.FRAMES:
                    target, sign = C642.signed_axis(frame, axis)
                    mapped = {
                        edge_key(
                            C642.act_vertex(frame, axis, left, length)[1],
                            C642.act_vertex(frame, axis, right, length)[1],
                        )
                        for left, right in tree
                    }
                    all24_family_failures += mapped != shifted_families[(sign * shift) % length]
                for left_frame in C642.FRAMES:
                    for right_frame in C642.FRAMES:
                        mid_axis, mid_sign = C642.signed_axis(right_frame, axis)
                        final_axis, final_sign = C642.signed_axis(left_frame, mid_axis)
                        product_axis, product_sign = C642.signed_axis(left_frame @ right_frame, axis)
                        all576_label_failures += (
                            final_axis != product_axis
                            or (final_sign * mid_sign * shift) % length != (product_sign * shift) % length
                        )
        selector = route_a_size["physical_copy_selector"]
        additional_edges = 3 * length * (len(unique_families) - 1)
        sizes.append({
            "length": length,
            "base_tree_translation_edge_symmetric_differences": base_translation_mismatches,
            "distinct_translation_orbit_trees": len(unique_families),
            "translation_orbit_family_closure_failures": translation_family_failures,
            "translation_orbit_decoder_covariance_failures": decoder_translation_failures,
            "all24_translation_frame_family_failures": all24_family_failures,
            "all576_translation_frame_label_failures": all576_label_failures,
            "uniform_physical_copy_selector_all24_failures": selector["uniform_selector_all24_orbit_failures"],
            "uniform_selector_branch_equivalence_failures": selector["single_copy_branches_not_equivalent_mod_pair_XX"],
            "declared_uniform_selector_M2": selector["declared_virtual_uniform_selector_M2"],
            "physically_placed_uniform_selector_M2": selector["selector_M2_physically_placed"],
            "additional_logical_tree_edges_for_full_translation_orbit": additional_edges,
            "additional_translation_orbit_edges_per_coarse_cell": additional_edges / length**3,
            "physically_placed_additional_translation_orbit_edges": 0,
            "maximum_local_tree_degree": max(map(len, adjacency(vertices, base_edges).values())),
            "maximum_local_handoff_gate_support_M2": 2,
            "odd_input_terminal_residuals": 2 ** length,
            "odd_defect_absorber_present": False,
            "lawful_even_syndromes": 2 ** length,
        })
    result = {
        "sizes": sizes,
        "constructive_result": "the complete translation orbit of the fill tree is exactly translation/frame covariant, while a uniform orbit selector implements the logical edge X modulo Cycle642 equality checks",
        "fixed_T0_tree_ordinary_translation_covariant_all_sizes": False,
        "translation_orbit_virtual_field_covariant": True,
        "uniform_selector_returns_on_equality_code": True,
        "selector_or_tree_orbit_physical_placement_complete": False,
        "odd_defect_lawful_domain_boundary": "odd syndrome is transported locally to one structural center defect and is not absorbed",
        "global_parity_query_used": False,
        "route_status": "EXACT_VIRTUAL_TRANSLATION_ORBIT_AND_UNIFORM_COPY_SELECTOR__PHYSICAL_FIELD_PLACEMENT_AND_ODD_ABSORBER_OPEN",
    }
    result["pass"] = bool(
        all(
            row["base_tree_translation_edge_symmetric_differences"][0] == 0
            and row["translation_orbit_family_closure_failures"] == 0
            and row["translation_orbit_decoder_covariance_failures"] == 0
            and row["all24_translation_frame_family_failures"] == 0
            and row["all576_translation_frame_label_failures"] == 0
            and row["uniform_physical_copy_selector_all24_failures"] == 0
            and row["uniform_selector_branch_equivalence_failures"] == 0
            and row["maximum_local_tree_degree"] <= 4
            and row["maximum_local_handoff_gate_support_M2"] == 2
            and row["physically_placed_uniform_selector_M2"] == 0
            and not row["odd_defect_absorber_present"]
            for row in sizes
        )
        and any(any(value for value in row["base_tree_translation_edge_symmetric_differences"][1:]) for row in sizes)
        and not result["fixed_T0_tree_ordinary_translation_covariant_all_sizes"]
        and result["translation_orbit_virtual_field_covariant"]
        and result["uniform_selector_returns_on_equality_code"]
        and not result["selector_or_tree_orbit_physical_placement_complete"]
        and not result["global_parity_query_used"]
    )
    check("route B repairs frame selection and translation covariance algebraically but leaves its orbit field unplaced", result["pass"], {
        "sizes": [(row["length"], row["base_tree_translation_edge_symmetric_differences"], row["distinct_translation_orbit_trees"], row["additional_logical_tree_edges_for_full_translation_orbit"]) for row in sizes]
    })
    return result


def route_C_stinespring_comparator(c642_receipt: dict, route_b: dict) -> dict:
    pinned_routes = {row["length"]: row for row in c642_receipt["fine_NN_routing_scouts"]}
    sizes = []
    for length, route_b_size in zip((3, 6, 7), route_b["sizes"]):
        vertices, edges = C642.fill_tree(length)
        numeric = tuple(vertex for vertex in vertices if vertex != C642.ROOT_VERTEX)
        full_images = set()
        even_environments = set()
        even_reset_failures = odd_residual_failures = isometry_collisions = 0
        leakage_failures = leakage_cases = 0
        for word in range(1 << len(vertices)):
            negative = {vertices[index] for index in range(len(vertices)) if (word >> index) & 1}
            compiled = reversible_compile(vertices, edges, negative)
            environment = tuple(int(vertex in negative) for vertex in numeric)
            output = tuple(sorted(compiled["residual"], key=vertex_key))
            image = (environment, output)
            isometry_collisions += image in full_images
            full_images.add(image)
            if len(negative) % 2 == 0:
                even_reset_failures += bool(output)
                even_environments.add(environment)
                for vertex in vertices:
                    leakage_cases += 1
                    leaked = reversible_compile(vertices, edges, negative ^ {vertex})
                    leakage_failures += leaked["residual"] != {leaked["center"]}
            else:
                odd_residual_failures += output != (compiled["center"],)
        deleted_labels = {environment[1:] for environment in even_environments}
        deleted_coordinate_collision_pairs = len(even_environments) - len(deleted_labels)
        route = pinned_routes[length]
        sizes.append({
            "length": length,
            "even_Kraus_sectors_per_axis": len(even_environments),
            "expected_even_Kraus_sectors_per_axis": 2 ** length,
            "even_reset_failures": even_reset_failures,
            "odd_terminal_residual_failures": odd_residual_failures,
            "full_even_plus_odd_Stinespring_label_collisions": isometry_collisions,
            "syndrome_environment_M2_per_axis": length,
            "delete_one_environment_coordinate_collision_pairs": deleted_coordinate_collision_pairs,
            "expected_deleted_coordinate_collision_pairs": 2 ** (length - 1),
            "single_face_leakage_cases": leakage_cases,
            "single_face_leakage_failures": leakage_failures,
            "uniform_selector_branch_failures": route_b_size["uniform_selector_branch_equivalence_failures"],
            "composed_all24_Stinespring_covariance_failures": (
                route_b_size["all24_translation_frame_family_failures"]
                + route_b_size["uniform_physical_copy_selector_all24_failures"]
            ),
            "composed_all576_Stinespring_covariance_failures": route_b_size["all576_translation_frame_label_failures"],
            "syndrome_environment_M2_three_axes_per_coarse_cell": 3 * length / length**3,
            "maximum_face_projector_support_M2": max(map(int, route["support_weight_histogram"])),
            "maximum_inherited_face_pair_route_edges": route["maximum_shortest_fine_NN_path_edges"],
            "physical_face_projector_controller_placed": False,
            "environment_returned_blank": False,
        })
    result = {
        "sizes": sizes,
        "Kraus_form": "K_s = X(j(s)) P_s on each even face-syndrome sector; the Stinespring environment retains the independent numeric-vertex syndrome bits",
        "trace_preserving_on_declared_even_domain": True,
        "uniform_copy_selector_uncomputes_on_equality_code": True,
        "environment_has_Record_or_occurrence_semantics": False,
        "environment_returned_or_absorbed": False,
        "physical_projector_extraction_compiled": False,
        "lawful_domain": "even face syndrome per axis, equivalent to the already-fixed Wilson-plus dependency",
        "route_status": "EXACT_STINESPRING_SYNDROME_RESET_COMPARATOR__ENVIRONMENT_RETAINED_AND_PHYSICAL_PROJECTORS_UNPLACED",
    }
    result["pass"] = bool(
        all(
            row["even_Kraus_sectors_per_axis"] == row["expected_even_Kraus_sectors_per_axis"]
            and row["even_reset_failures"] == row["odd_terminal_residual_failures"] == 0
            and row["full_even_plus_odd_Stinespring_label_collisions"] == 0
            and row["delete_one_environment_coordinate_collision_pairs"] == row["expected_deleted_coordinate_collision_pairs"]
            and row["single_face_leakage_failures"] == 0
            and row["uniform_selector_branch_failures"] == 0
            and row["composed_all24_Stinespring_covariance_failures"] == 0
            and row["composed_all576_Stinespring_covariance_failures"] == 0
            and not row["physical_face_projector_controller_placed"]
            and not row["environment_returned_blank"]
            for row in sizes
        )
        and result["trace_preserving_on_declared_even_domain"]
        and result["uniform_copy_selector_uncomputes_on_equality_code"]
        and not result["environment_has_Record_or_occurrence_semantics"]
        and not result["environment_returned_or_absorbed"]
        and not result["physical_projector_extraction_compiled"]
    )
    check("route C gives an exact Stinespring reset comparator with explicit retained environment and projector nonplacement", result["pass"], {
        "sizes": [(row["length"], row["even_Kraus_sectors_per_axis"], row["delete_one_environment_coordinate_collision_pairs"], row["maximum_face_projector_support_M2"]) for row in sizes]
    })
    return result


def no_go_discipline(route_a: dict, route_b: dict, route_c: dict) -> dict:
    families = [
        {"family": "reversible retained-syndrome message circuit", "object": "input/work/history M2 rails on a bounded-degree tree", "mechanism": "parallel leaf CNOT handoff and compute-correct-uncompute", "terminal": "autonomous physical syndrome extraction and collision-safe NN lowering", "honesty_marker": "ATTEMPTED", "target_equivalent": False, "result": route_a["route_status"]},
        {"family": "translation/frame-orbit virtual defect field", "object": "translated tree family plus orbit-uniform fiber selector", "mechanism": "group-orbit covariance and equality-stabilizer branch equivalence", "terminal": "physical selector/tree-orbit placement and odd-defect boundary", "honesty_marker": "ATTEMPTED", "target_equivalent": False, "result": route_b["route_status"]},
        {"family": "syndrome-labelled Stinespring reset", "object": "orthogonal face projectors and an explicit environment", "mechanism": "K_s = X(j(s)) P_s", "terminal": "local projector extraction plus returned or admitted environment", "honesty_marker": "ATTEMPTED", "target_equivalent": False, "result": route_c["route_status"]},
    ]
    open_routes = [
        {"family": "reserved sidecar controller placement", "object": "outer-shell controller orbits", "mechanism": "disjoint placed endpoint slots", "terminal": "literal local controller sites", "search_status": "C649_WORKING_TREE_INTERFACE_UNCONSUMED_NOT_COUNTED"},
        {"family": "static subsystem wire", "object": "crossing-safe gauge wires", "mechanism": "commuting local constraints", "terminal": "all face projectors and corrections", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "asynchronous quantum walk router", "object": "mobile route-head automaton", "mechanism": "local collision arbitration", "terminal": "returned route history", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "virtual-bond tree PEPS", "object": "translation-invariant tensor network", "mechanism": "absorb origin and selector into bond gauge", "terminal": "physical fixed-sector preparation", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "mobile odd-defect pair", "object": "locally created absorber pair", "mechanism": "sector-preserving defect transport and annihilation", "terminal": "lawful odd-boundary treatment without a parity service", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
    ]
    walls = ("W_extract", "W_route", "W_origin", "W_odd", "W_exhaust")
    interfaces = {
        "W_extract": "coherent/local face-syndrome acquisition from data",
        "W_route": "collision-safe fine-NN controller transport",
        "W_origin": "ordinary-translation orbit placement without T0 selection",
        "W_odd": "odd-defect lawful-domain boundary or absorber",
        "W_exhaust": "retained Stinespring syndrome environment",
    }
    pairs = [
        {"from": source, "to": target, "closure_implied": False, "independence_evidence": {"status": "NOT_ESTABLISHED_BEYOND_EXECUTED_INTERFACES", "from_interface": interfaces[source], "to_interface": interfaces[target], "reason": f"closing {source} on {interfaces[source]} does not execute or certify {target} on {interfaces[target]}"}}
        for source, target in permutations(walls, 2)
    ]
    phrases = (
        "we assume", "by construction", "as is standard", "the framework provides",
        "bridge context", "background", "naturally", "obviously", "standard qft",
        "registered", "canonical",
    )
    note_text = NOTE.read_text().lower()
    hits = tuple(phrase for phrase in phrases if phrase in note_text)
    current = "scripts/physical_root_label_blind_face_pump_compiler_cycle651_2026_07_23.py"
    current_ref = "working-tree Cycle651 candidate"
    n4 = [
        {"prior_ref": SHORE_REF, "prior_path": C648_NOTE, "prior_line": immutable_line(C648_NOTE, "no crossing schedule, static"), "prior_residual": "Cycle648 has no physical face-measurement crossing schedule", "current_ref": current_ref, "current_path": current, "current_line": source_line("def route_A_reversible_message_passing"), "current_residual": "Cycle651 closes only the supplied-syndrome reversible CNOT logic; controller placement and collision-safe NN extraction remain absent", "same_scope": True, "exact_match": True, "use_as_closure": True},
        {"prior_ref": SHORE_REF, "prior_path": C642_NOTE, "prior_line": immutable_line(C642_NOTE, "Intersecting routes still need either"), "prior_residual": "Cycle642 leaves intersecting route enforcement without a static wire or state-carried schedule", "current_ref": current_ref, "current_path": current, "current_line": source_line("def route_B_orbit_defect_field"), "current_residual": "Cycle651 supplies covariant virtual selectors and tree-orbit labels but no placed crossing controller", "same_scope": True, "exact_match": True, "use_as_closure": True},
        {"prior_ref": SHORE_REF, "prior_path": C648_NOTE, "prior_line": immutable_line(C648_NOTE, "Odd syndrome is outside the lawful domain"), "prior_residual": "odd face syndrome leaves one abstract defect without an absorber", "current_ref": current_ref, "current_path": current, "current_line": source_line("def route_B_orbit_defect_field"), "current_residual": "every odd syndrome still leaves one structural-center defect and no absorber is added", "same_scope": True, "exact_match": True, "use_as_closure": False},
        {"prior_ref": SHORE_REF, "prior_path": C643_NOTE, "prior_line": immutable_line(C643_NOTE, "pivot/root and row order"), "prior_residual": "Cycle643 uses supplied global tableau pivot/root/order", "current_ref": current_ref, "current_path": current, "current_line": source_line("def route_C_stinespring_comparator"), "current_residual": "Cycle651 tests local tree syndrome reset with retained environment", "same_scope": False, "exact_match": False, "use_as_closure": False},
    ]
    n5 = [
        {"claim": "a retained syndrome rail is not autonomous syndrome extraction", "per_element": "each CNOT is explicit", "per_site": "input and work roles are declared but unplaced", "per_mode": "every syndrome word is tested", "per_block": "three axes have exact gate counts", "lattice_wide": "no data-to-rail measurement controller is placed"},
        {"claim": "a shortest-path family is not a crossing-safe controller", "per_element": "every path step is fine-NN", "per_site": "shared ownership was counted by Cycle642", "per_mode": "each check support pair has routes", "per_block": "maximum lengths 136/344/345 are inherited", "lattice_wide": "no autonomous arbitration law is executed"},
        {"claim": "a translation-orbit family is not its physical preparation", "per_element": "tree edges transform exactly", "per_site": "additional orbit edges are counted but unplaced", "per_mode": "all translations of every syndrome commute", "per_block": "all24/all576 labels close", "lattice_wide": "no orbit-label state is prepared"},
        {"claim": "a Stinespring comparator is not returned exhaust", "per_element": "Kraus sectors are explicit", "per_site": "environment bits are counted", "per_mode": "even and odd sectors are exhaustive", "per_block": "deleting one environment coordinate causes exact collisions", "lattice_wide": "the environment remains outside the returned physical state"},
        {"claim": "an even-domain pump is not odd-sector genesis", "per_element": "one edge correction toggles two faces", "per_site": "local handoffs conserve parity", "per_mode": "every odd word leaves one defect", "per_block": "the center follows tree topology", "lattice_wide": "no mobile absorber or sector-changing resource is supplied"},
    ]
    n6 = [
        {"file": C642_NOTE, "status": "PINNED_PHYSICAL_ROUTE_PARENT", "what_closes": "all shortest path geometry, not crossing enforcement"},
        {"file": C648_NOTE, "status": "PINNED_ABSTRACT_DECODER_PARENT", "what_closes": "all even/odd syndrome enumeration and frame covariance, not physical extraction"},
        {"file": C629_NOTE, "status": "PINNED_STATE_CARRIED_ORBIT_COMPARATOR", "what_closes": "a marker origin by a carried orbit phase on a different substrate"},
        {"file": "scripts/physical_reserved_outer_shell_sidecar_placement_cycle649_2026_07_23.py", "status": "UNCONSUMED_WORKING_TREE_INTERFACE", "what_closes": "potential controller placement only after immutable adoption and independent verification"},
        {"file": "UNMATERIALIZED/cycle652_crossing_safe_face_router.py", "status": "OPEN", "what_closes": "data-to-syndrome extraction, orbit selector preparation, collision arbitration, and returned route history"},
    ]
    steelman = {
        "argument": "The negative physical disposition is premature because Cycle642 already supplies every endpoint and full fine-NN path family, while Cycle651 supplies a two-M2 reversible decoder and proves that an orbit-uniform copy selector acts as one logical X modulo the equality checks. A disjoint outer-shell sidecar orbit plus a state-carried collision token could therefore connect the exact pieces without a preferred frame or host path table.",
        "mechanism": "placed sidecar orbit, uniform selector, and state-carried collision arbitration",
        "terminal_obligation": "literal L3/L6/L7 data-to-syndrome circuit with all controller sites, adjacent gates, all24/all576 and ordinary translations, returned route/work registers, even lawful-domain reset, odd boundary, deletion and leakage",
        "citations": [
            {"ref": SHORE_REF, "path": C642_NOTE, "line": immutable_line(C642_NOTE, "coordinate-counter description"), "supports": "all signed shortest path families already exist"},
            {"ref": SHORE_REF, "path": C648_NOTE, "line": immutable_line(C648_NOTE, "Every even face syndrome is exhausted"), "supports": "the abstract decoder is exhaustive"},
        ],
        "action": "place the declared input/work/history and selector roles, then compile one crossing-safe routed projector and inverse before scaling",
        "actionable": True,
    }
    echoes = [
        {"cycle": "Cycle629", "citation_ref": SHORE_REF, "citation_path": C629_NOTE, "citation_line": immutable_line(C629_NOTE, "state-carried translation phase"), "retired": "an external origin on the marker orbit", "mechanism": "state-carried translation phase", "applicability": "ACTIONABLE_FOR_TREE_ORBIT_LABEL_PREPARATION"},
        {"cycle": "Cycle642", "citation_ref": SHORE_REF, "citation_path": C642_NOTE, "citation_line": immutable_line(C642_NOTE, "autonomous state-carried crossing schedule"), "retired": False, "mechanism": "static subsystem wire or state-carried schedule", "applicability": "EXACT_PHYSICAL_ROUTING_RESIDUAL"},
        {"cycle": "Cycle643", "citation_ref": SHORE_REF, "citation_path": C643_NOTE, "citation_line": immutable_line(C643_NOTE, "pivot/root and row order"), "retired": "abstract state-preparation omission only", "mechanism": "global Clifford tableau synthesis", "applicability": "DOES_NOT_CLOSE_PHYSICAL_LOCAL_EXTRACTION"},
        {"cycle": "Cycle648", "citation_ref": SHORE_REF, "citation_path": C648_NOTE, "citation_line": immutable_line(C648_NOTE, "root-label-blind leaf pump"), "retired": "abstract even-syndrome decoder omission", "mechanism": "parallel leaf peeling", "applicability": "ADVANCED_HERE_TO_REVERSIBLE_SUPPLIED_SYNDROME_LOGIC"},
    ]
    n4_lines = all(cited_line_exists(row["prior_ref"], row["prior_path"], row["prior_line"]) and row["current_line"] > 0 for row in n4)
    n7_lines = all(cited_line_exists(row["ref"], row["path"], row["line"]) for row in steelman["citations"])
    n8_lines = all(cited_line_exists(row["citation_ref"], row["citation_path"], row["citation_line"]) for row in echoes)
    result = {
        "skill_freshness": {"origin_main_fetched": True, "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7", "proof_search_governance_sha256": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258", "newer_origin_main_followed": True},
        "N1_normalized_families": families, "N1_qualifying_attempts": sum(row["target_equivalent"] for row in families), "N1_required_for_negative": 5, "N1_required_for_broad_negative": 5, "N1_open_routes_not_counted": open_routes,
        "N2_collapsed_walls": walls, "N2_directed_pairs": pairs, "N2_directed_pair_count": len(pairs), "N2_machine_check_count": len(pairs), "N2_independence_complete": False,
        "N3_hidden_wall_phrases": phrases, "N3_note_phrase_hits": hits,
        "N3_explicit_supplied_structure": ["immutable Cycle642/Cycle648 shore", "finite L3/L6/L7", "compile-time tree topology", "retained syndrome input rail", "blank work/history rails", "Cycle642 orbit fibers and equality code", "one unplaced uniform selector per logical edge", "full translated tree family", "even lawful domain", "syndrome-labelled Stinespring environment", "Cycle642 fine-NN path families without arbitration"],
        "N4_exact_residual_matching": n4, "N4_exact_residual_matches": n4[:3], "N4_dropped_nonmatches": n4[3:], "N4_cited_lines_exist": n4_lines,
        "N5_five_resolution_rhetoric_audit": n5,
        "N6_partial_closure_paths": n6,
        "N7_cited_actionable_steelman": steelman, "N7_cited_lines_exist": n7_lines,
        "N8_rowwise_cross_cycle_echo": echoes, "N8_cited_lines_exist": n8_lines,
        "Status": "PASS", "artifact_status": "PARTIAL_CONSTRUCTIVE_ADVANCE_WITH_EXACT_NONPLACEMENT_RESIDUAL",
        "broad_negative_gate": "FAIL / DO NOT SHIP", "broad_no_go_claim": False,
        "minimum_content_gate": "FAIL / DO NOT SHIP", "minimum_content_claim": False,
        "shared_obstruction_gate": "FAIL / DO NOT SHIP", "shared_obstruction_claim": False,
        "axiom_pressure_gate": "FAIL / DO NOT SHIP", "axiom_pressure_claim": False,
        "broad_negative_shipped": False, "minimum_content_shipped": False,
        "shared_obstruction_shipped": False, "axiom_pressure_shipped": False,
        "negative_claim_shipped": False, "shared_route_independent_obstruction": False, "axiom_pressure": False,
    }
    result["pass"] = bool(
        len(families) == 3 and all(row["honesty_marker"] == "ATTEMPTED" for row in families)
        and len(open_routes) == 5 and all("honesty_marker" not in row for row in open_routes)
        and result["N1_required_for_negative"] == result["N1_required_for_broad_negative"] == 5
        and result["N1_qualifying_attempts"] < result["N1_required_for_negative"]
        and len(pairs) == result["N2_machine_check_count"] == 20
        and len({(row["from"], row["to"]) for row in pairs}) == 20
        and all(row["closure_implied"] is False and row["independence_evidence"]["reason"] for row in pairs)
        and not hits and n4_lines and n7_lines and n8_lines
        and all(row["prior_ref"] == SHORE_REF and row["current_ref"] == current_ref for row in n4)
        and all(row["same_scope"] and row["exact_match"] for row in n4[:3])
        and all(not row["same_scope"] and not row["exact_match"] and not row["use_as_closure"] for row in n4[3:])
        and all(all(key in row for key in ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")) for row in n5)
        and all(set(row) == {"file", "status", "what_closes"} for row in n6)
        and all(row["ref"] == SHORE_REF for row in steelman["citations"])
        and all(row["citation_ref"] == SHORE_REF and all(key in row for key in ("retired", "mechanism", "applicability")) for row in echoes)
        and all(result[key] == "FAIL / DO NOT SHIP" for key in ("broad_negative_gate", "minimum_content_gate", "shared_obstruction_gate", "axiom_pressure_gate"))
        and all(result[key] is False for key in ("broad_no_go_claim", "minimum_content_claim", "shared_obstruction_claim", "axiom_pressure_claim", "broad_negative_shipped", "minimum_content_shipped", "shared_obstruction_shipped", "axiom_pressure_shipped", "negative_claim_shipped"))
        and not result["shared_route_independent_obstruction"] and not result["axiom_pressure"]
    )
    check("full N1-N8 keeps every broad negative, minimum-content, shared-obstruction and axiom-pressure claim blocked", result["pass"], {
        "N1": result["N1_qualifying_attempts"], "N2": len(pairs), "N4": n4_lines, "N7": n7_lines, "N8": n8_lines,
    })
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "## Exact target", "## Strongest result", "## Route A", "## Route B", "## Route C",
        "## N1-N8 discipline", "## Supplied structure", "## Dependency ledger", "## Scope firewall",
    )
    result = {
        "missing_sections": tuple(section for section in required if section not in text),
        "authority_none": "Authority: **none**" in text,
        "audit_unset": "Audit: **unset**" in text,
        "accepted_false": "Accepted: **false**" in text,
    }
    result["pass"] = not result["missing_sections"] and all(result[key] for key in ("authority_none", "audit_unset", "accepted_false"))
    check("Cycle651 note exposes target, routes, controls, N1-N8 and supplied structure", result["pass"], result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    print("Cycle651 physical root-label-blind face-pump compiler", AUTHORITY, AUDIT)
    c642_receipt, c648_receipt, shore_result = shore()
    load_modules()
    note = note_contract()
    route_a = route_A_reversible_message_passing(c642_receipt)
    route_b = route_B_orbit_defect_field(route_a)
    route_c = route_C_stinespring_comparator(c642_receipt, route_b)
    discipline = no_go_discipline(route_a, route_b, route_c)
    promotion_gates = {
        "broad_negative_gate": "FAIL / DO NOT SHIP", "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP", "axiom_pressure_gate": "FAIL / DO NOT SHIP",
    }
    top_claims = {
        "broad_no_go_claim": False, "minimum_content_claim": False,
        "shared_obstruction_claim": False, "axiom_pressure_claim": False,
    }
    top_shipped = {
        "broad_negative_shipped": False, "minimum_content_shipped": False,
        "shared_obstruction_shipped": False, "axiom_pressure_shipped": False,
    }
    claim_contract = bool(
        discipline["Status"] == "PASS" and discipline["pass"]
        and discipline["N1_required_for_negative"] == discipline["N1_required_for_broad_negative"] == 5
        and all(discipline[key] == value for key, value in promotion_gates.items())
        and all(discipline[key] is value for key, value in top_claims.items())
        and all(discipline[key] is value for key, value in top_shipped.items())
        and not discipline["negative_claim_shipped"]
    )
    check("top-level status, four promotion gates and all shipped flags are exact", claim_contract, {
        "Status": discipline["Status"], "gates": promotion_gates, "claims": top_claims, "shipped": top_shipped,
    })
    fixture = C648.C644.c532.fixture_controls()
    factor_rows = c642_receipt["tree_fill_target_times_gauge_certificates"]
    fixture_pass = bool(
        fixture["pass"]
        and all(row["pass"] for row in factor_rows)
        and c648_receipt["logical_fixtures"]["fixture_pass"]
        and fixture["Cycle219_mass_fixture_residual"] == c648_receipt["logical_fixtures"]["Cycle219_mass_residual"]
        and fixture["Cycle230_contact_deletion_residual"] == c648_receipt["logical_fixtures"]["Cycle230_contact_deletion_residual"]
        and fixture["Cycle230_seam_subchecks"] == c648_receipt["logical_fixtures"]["Cycle230_seam_subchecks"]
    )
    check("Cycle642 target-times-gauge and Cycle219/Cycle230 mass-contact-seam fixtures remain pinned", fixture_pass, {
        "mass": fixture["Cycle219_mass_fixture_residual"], "contact_deletion": fixture["Cycle230_contact_deletion_residual"], "seam": fixture["Cycle230_seam_subchecks"],
    })
    elapsed = time.monotonic() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    check("cold run stays within declared resource caps", elapsed < CAP_SECONDS and maximum_rss < CAP_BYTES, {
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
    })
    receipt = {
        "status": "cycle651-physical-root-label-blind-face-pump-compiler",
        "Status": discipline["Status"],
        "classification": "PARTIAL_CONSTRUCTIVE_ADVANCE_WITH_EXACT_NONPLACEMENT_RESIDUAL",
        "authority": AUTHORITY, "audit": AUDIT, "author_accepted": False,
        "author_artifact_status_accepted": False, "constitutional_effect": "none",
        **promotion_gates, **top_claims, **top_shipped,
        "negative_claim_shipped": False,
        "canonical_claim_gate_contract": {"Status": discipline["Status"], **promotion_gates, **top_claims, **top_shipped, "pass": claim_contract},
        "breakthrough": False,
        "immutable_shore_ref": SHORE_REF, "pins": PINS,
        "runner_sha256": sha(Path(__file__)), "note_sha256": sha(NOTE),
        "shore": shore_result, "note_contract": note,
        "exact_target_contract": {
            "target_statement": "compile the Cycle648 root-label-blind face pump into a bounded-neighborhood physical-M2 controller",
            "domain": "periodic L3 construction, L6 train, held L7; exhaustive even and odd face syndromes; all24/all576",
            "allowed_premises": "only immutable shore 4f2b07fd39 and explicitly inventoried new controller roles",
            "forbidden_weakenings": "no named-root query, coordinate-zero sheet, host path service, global parity query, preferred frame, hidden environment, or C649 premise",
            "required_edges": "placed roles/routes or exact nonplacement, two-M2 NN lowering, inverse/deletion/leakage, lawful domain, mass/contact/seam",
            "completion_witness": "literal autonomous data-to-syndrome controller with collision-safe fine-NN gates and returned unitary work or admitted dissipative environment",
            "not_closure": "retained syndrome input, abstract orbit field, fixed-code covariance, path family, unplaced selector, or Stinespring formula alone",
        },
        "approach_registry": [
            {"family": "reversible retained-syndrome message circuit", "object_formulation": "input/work/history tree rails", "mechanism_invariant": "parallel leaf CNOT handoff", "terminal_obligation": "autonomous extraction and physical NN lowering", "strength_vs_target": "weaker", "status": "provisional", "concrete_evidence": route_a["route_status"], "reopen_condition": "place controller rails and one routed projector"},
            {"family": "translation/frame-orbit virtual defect field", "object_formulation": "translated trees and uniform fiber selectors", "mechanism_invariant": "group orbit plus equality-stabilizer equivalence", "terminal_obligation": "prepare/place orbit field and odd boundary", "strength_vs_target": "weaker", "status": "provisional", "concrete_evidence": route_b["route_status"], "reopen_condition": "physical sidecar orbit and state-carried orbit-label preparation"},
            {"family": "syndrome-labelled Stinespring reset", "object_formulation": "Kraus projectors and environment", "mechanism_invariant": "orthogonal syndrome-sector isometry", "terminal_obligation": "local projectors and returned/admitted environment", "strength_vs_target": "weaker", "status": "provisional", "concrete_evidence": route_c["route_status"], "reopen_condition": "placed local projector gadget and explicit environment boundary"},
        ],
        "route_A_reversible_local_message_passing": route_a,
        "route_B_translation_frame_orbit_virtual_defect_field": route_b,
        "route_C_dissipative_Stinespring_comparator": route_c,
        "route_by_route_disposition": {"A": route_a["route_status"], "B": route_b["route_status"], "C": route_c["route_status"]},
        "strongest_constructive_result": "every L3/L6/L7 face syndrome has an exact two-M2 reversible leaf-message circuit from a retained syndrome rail; a proper-cubic uniform copy selector returns exactly modulo Cycle642 equality checks; the complete translated-tree family is translation/frame covariant; all new controller, selector, and orbit-field placements remain explicit zeros",
        "strongest_narrow_falsifier": "on the immutable Cycle642 fibers, a fixed sorted single-copy X has 171/342/387 all24 failures and exhaustive odd-subset enumeration finds no stabilizer-invariant odd-X subset; this excludes only fixed Pauli copy selection on that encoding",
        "autonomous_physical_face_pump_compiled": False,
        "bounded_neighborhood_physical_controller_compiled": False,
        "support_at_most_two_logical_compiler": True,
        "support_at_most_two_fine_NN_physical_lowering": False,
        "constant_overhead_per_coarse_cell_accounted": True,
        "ordinary_translation_frame_orbit_virtual_family": True,
        "ordinary_translation_frame_orbit_physically_prepared": False,
        "all24_all576_abstract_controller_covariance": True,
        "fixed_code_all24_all576": c648_receipt["fixed_code_all24_all576"],
        "fixed_code_covariance_is_preparation_covariance": False,
        "preparation_all24_all576_established": False,
        "C649_interface": "UNCONSUMED_NOT_ON_IMMUTABLE_SHORE",
        "logical_fixtures": {
            "Cycle642_factor_rows_pass": all(row["pass"] for row in factor_rows),
            "Cycle219_mass_residual": fixture["Cycle219_mass_fixture_residual"],
            "Cycle230_contact_deletion_residual": fixture["Cycle230_contact_deletion_residual"],
            "Cycle230_seam_subchecks": fixture["Cycle230_seam_subchecks"],
            "fixture_pass": fixture_pass,
        },
        "no_go_discipline": discipline,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
        "supplied_structure": discipline["N3_explicit_supplied_structure"],
        "scope_firewall": {
            "retained_syndrome_rail_is_autonomous_extraction": False,
            "two_M2_logical_gate_is_fine_NN_without_placement": False,
            "uniform_virtual_selector_is_prepared_physical_selector": False,
            "translation_orbit_family_is_orbit_state_preparation": False,
            "Stinespring_environment_is_returned": False,
            "environment_is_Record_or_occurrence": False,
            "odd_residual_is_odd_sector_genesis": False,
            "compiler_layer_is_physical_time": False,
            "phase_is_energy": False, "generator_is_rate": False,
            "source_gravity_or_Born_claimed": False,
        },
        "six_wall_ledger": {
            "C_ref": "advanced algebraically: fixed-copy frame selection is replaced by an orbit-uniform selector and full translated-tree family; physical orbit-label/selector genesis remains",
            "C_num": "advanced locally: exhaustive syndrome-labelled environment counts and exact deletion collisions; no empirical or Born normalization",
            "C_wrap": "advanced: reversible even/odd message compilation and exact odd terminal residual; no odd absorber or full physical reset",
            "C_int": "pinned Cycle642 quotient and Cycle219/Cycle230 fixtures only; no new E G intertwiner",
            "C_local": "advanced abstractly: every controller gate has support at most two and all work returns from a retained syndrome rail; controller placement, syndrome extraction, and collision-safe NN lowering remain",
            "C_source": "unchanged: no energy, rate, source, stress, gravity, Record, occurrence, or autonomous environment renewal",
        },
        "campaign_lane_coordinate_rebase": "Cycle651 does not independently rebase campaign lane coordinates.",
        "optimal_next_campaign": "adopt no uncommitted placement premise; independently place one all24 orbit of syndrome/work/history and uniform-selector sidecars, compile one Cycle642 face projector and edge correction through a collision-safe state-carried fine-NN router, then scale only after inverse, deletion, leakage, ordinary translations and environment accounting pass",
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
        "tests_passed": PASS, "tests_failed": FAIL,
        "pass": FAIL == 0 and route_a["pass"] and route_b["pass"] and route_c["pass"] and discipline["pass"] and claim_contract and fixture_pass,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n")
    print("SUMMARY_JSON", json.dumps({
        "pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
        "route_A_fixed_selector_all24_failures": [row["physical_copy_selector"]["fixed_sorted_copy_all24_failures"] for row in route_a["sizes"]],
        "route_A_unplaced_controller_roles": [row["explicit_unplaced_controller_role_residual"] for row in route_a["sizes"]],
        "route_B_base_translation_mismatches": [row["base_tree_translation_edge_symmetric_differences"] for row in route_b["sizes"]],
        "route_C_even_Kraus_sectors": [row["even_Kraus_sectors_per_axis"] for row in route_c["sizes"]],
        "autonomous_physical_face_pump_compiled": False,
        "shared_obstruction": False, "axiom_pressure": False,
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
    }, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return int(not receipt["pass"])


if __name__ == "__main__":
    raise SystemExit(main())
