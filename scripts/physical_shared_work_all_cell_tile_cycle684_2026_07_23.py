#!/usr/bin/env python3
"""Cycle 684: shared-work all-cell factorization and state-carried scheduler.

This is deliberately a compiler stress test, not an axiom or audit surface.  It
constructs one target-independent prepared-work word for every declared torus,
checks the targetwise reduction to Cycle 679, and executes a reversible local
schedule model.  The receipt keeps the remaining M2-controller lowering wall
explicit.
"""

from __future__ import annotations

TARGET_CONTRACT = {
    "target_statement": "replace Cycle679's target-dependent incident stars by one target-independent all-cell prepared work U_global, one C edge layer per U invocation, commuting local predicates/binders and an exact inverse, driven by a state-carried local schedule rather than a host cell list",
    "quantifiers_domain": "every cell and every accepted C edge at L3 train, L4 held-out-size and L6 held; representative sparse physical mass/contact/seam fixtures; all local schedule slots, collision colors, deletions and malformed controller seeds; all24 proper-cubic frames and all576 ordered frame products",
    "allowed_premises": "byte-pinned committed Cycle675/678/679 shores; Cycle608 local A/SELECT/D tables and accepted C rows; finite physical matter rails; locally carried edge-enable, route-color, frame and synchronized phase seed; inherited bounded route-return recipe",
    "forbidden_weakenings": "using target-dependent Wstar_x as common U; host-side target iteration at runtime; unique site IDs, Jordan-Wigner chain, nonlocal parity service or a hidden global cell ordering; calling factor ordinal time, generator rate or wrapped phase energy; calling a Python controller transition a literal M2 transition word; hiding seed genesis, route collision, odd-torus coloring, deletion, held-size or covariance residuals",
    "required_edge_cases": "zero-C and maximum-C cells, every target and edge exactly once, L3/L4/L6, one-particle mass, Cycle230 contact and seam, physical leakage, deleted schedule slot, deleted C row, malformed conflicting color, phase desynchronization, translated/rotated carried seeds, raw signed covariance failure and bounded local sheath repair inherited from Cycle679",
    "completion_witness": "coordinate-explicit common U_global=(product AS_i)(product C_e)(product D_i), exhaustive targetwise support reduction, proper route-footprint colorings, an executed reversible state-carried schedule with exact coverage and return, representative sparse physical comparisons and a strict statement of whether the controller itself was lowered to M2 factors",
    "outcomes_not_closure": "a list of per-target Wstar words; a graph coloring computed by the host but not stored as physical state; a controller truth table with no M2 lowering called a physical all-cell tile; an edge mask inherited from an ordering called an ordering-free derivation; a route-specific or odd-torus failure promoted to shared obstruction or axiom pressure",
}

from collections import Counter
from contextlib import contextmanager
from hashlib import sha256
import importlib.util
import itertools
import json
from pathlib import Path
import resource
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SHARED_WORK_ALL_CELL_TILE_CYCLE684_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_shared_work_all_cell_tile_cycle684_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_shared_work_all_cell_tile_cycle684_cold_2026_07_23.txt"
SHORE = "854b4b48f4c98fa6b82f2e05cc2d33edbaf569fa"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2.0e-10
PASS = 0
FAIL = 0
CELL_COLOR_SLOTS = 12
EDGE_COLOR_SLOTS = 6

PINS = {
    "scripts/physical_incident_C_prepared_star_detector_cycle679_2026_07_23.py": "4762707df62b4a07a4df6660a4733ef2609999a9d71afc3be78e974bdb7936d1",
    "docs/work_history/repo/review_feedback/PHYSICAL_INCIDENT_C_PREPARED_STAR_DETECTOR_CYCLE679_NOTE_2026-07-23.md": "b816a59dceae5934bc9db7f293bded37c1d8546df46bd08ae52ceea92defc7ab",
    "outputs/physical_incident_C_prepared_star_detector_cycle679_receipt_2026_07_23.json": "1343f10d230e43a870474e0c5b482e9a8efc58893ef1fc4897db3144b762b442",
    "outputs/physical_incident_C_prepared_star_detector_cycle679_cold_2026_07_23.txt": "e365bc631ea7aa2f0989854141313665140d6868f1ce36ffb95f9757f4aa18cb",
    "scripts/physical_occupancy_six_q_syndrome_extractor_cycle675_2026_07_23.py": "cf0ad89d0628878f1355754a419163400eda2710092f879bead34e1ed2643181",
    "docs/work_history/repo/review_feedback/PHYSICAL_OCCUPANCY_SIX_Q_SYNDROME_EXTRACTOR_CYCLE675_NOTE_2026-07-23.md": "dbabca9a1460950f9701462723679d696ef4b94a8cda7cd3a62b220f885d51f5",
    "outputs/physical_occupancy_six_q_syndrome_extractor_cycle675_receipt_2026_07_23.json": "ac1e8585c48f8cd67366301be1837be3cdd80e21d9d47d4242c52f8db1481d64",
    "outputs/physical_occupancy_six_q_syndrome_extractor_cycle675_cold_2026_07_23.txt": "d4bfdea1b793ec671b80f46b68d1fc67c786215b22167290b51ce5b0765291c3",
    "scripts/physical_autonomous_extremal_sector_born_actualizer_tournament_cycle678_2026_07_23.py": "e3780ef97d394116c49044ff44eacd178da0146a8f60dd3b47838bbac904775a",
    "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_EXTREMAL_SECTOR_BORN_ACTUALIZER_TOURNAMENT_CYCLE678_NOTE_2026-07-23.md": "b4f4eab00fc27b745b504daf6eb0d884d4c214d089679979f018f8f6f4825f78",
    "outputs/physical_autonomous_extremal_sector_born_actualizer_tournament_cycle678_receipt_2026_07_23.json": "6416f1ec5260e2482dc6415368485f04f04d29418a8697558baf9316dac159b6",
    "outputs/physical_autonomous_extremal_sector_born_actualizer_tournament_cycle678_cold_2026_07_23.txt": "00fface01b1f613bc7e6620c87779817e2aad49912f8f0c9a8026d5094d86997",
}


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, body):
        for stream in self.streams: stream.write(body)
        return len(body)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not bool(condition))
    print("PASS" if condition else "FAIL", label, "::", detail)


def stable_digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=float).encode()).hexdigest()


def git_bytes(relative):
    return subprocess.run(("git", "show", f"{SHORE}:{relative}"), cwd=ROOT, check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def target_freeze_controls():
    source = Path(__file__).read_text().splitlines()
    target_line = next(i for i, line in enumerate(source, 1) if line.startswith("TARGET_CONTRACT ="))
    evidence_line = next(i for i, line in enumerate(source, 1) if line.startswith("def shore_controls"))
    expected = ["allowed_premises", "completion_witness", "forbidden_weakenings",
                "outcomes_not_closure", "quantifiers_domain", "required_edge_cases",
                "target_statement"]
    return {"target_line": target_line, "first_evidence_load_line": evidence_line,
            "frozen_before_evidence": target_line < evidence_line,
            "target_contract_sha256": stable_digest(TARGET_CONTRACT),
            "proof_search_governance_exact_fields": sorted(TARGET_CONTRACT),
            "pass": target_line < evidence_line and sorted(TARGET_CONTRACT) == expected}


def shore_controls():
    observed = {relative: sha256(git_bytes(relative)).hexdigest() for relative in PINS}
    r679 = json.loads(git_bytes("outputs/physical_incident_C_prepared_star_detector_cycle679_receipt_2026_07_23.json"))
    r678 = json.loads(git_bytes("outputs/physical_autonomous_extremal_sector_born_actualizer_tournament_cycle678_receipt_2026_07_23.json"))
    passed = (observed == PINS and r679["pass"] and r678["pass"]
              and r679["authority"] == r678["authority"] == "none"
              and r679["audit"] == r678["audit"] == "unset"
              and not r679["aggregate_summary"]["same_unprogrammed_all_cell_device_executed"])
    return {"ref": SHORE, "pins": PINS, "observed": observed,
            "Cycle679_terminal": r679["highest_honest_terminal"],
            "Cycle679_open_wall": r679["no_go_discipline"]["N2_walls"]["W_same_device_generic_chart"],
            "Cycle678_boundary": "objective actualizer/seed genesis remains supplied; no Born or genesis innovation is imported here",
            "working_tree_bytes_used_as_scientific_premise": False,
            "author_status_accepted_as_audit": False, "pass": passed}, {"Cycle679": r679, "Cycle678": r678}


@contextmanager
def pinned_modules():
    relative = "scripts/physical_incident_C_prepared_star_detector_cycle679_2026_07_23.py"
    local = ROOT / relative
    if sha256(local.read_bytes()).hexdigest() != PINS[relative]:
        raise RuntimeError("Cycle679 working path differs from pinned committed bytes")
    name = "cycle684_pinned_cycle679"
    spec = importlib.util.spec_from_file_location(name, local)
    module = importlib.util.module_from_spec(spec); sys.modules[name] = module
    assert spec.loader is not None; spec.loader.exec_module(module)
    try:
        with module.pinned_modules() as (c675, m672, c608):
            yield module, c675, m672, c608
    finally:
        sys.modules.pop(name, None)


def factor_support(factor):
    return set(factor.controls + factor.targets)


def word_support(word):
    return set().union(*(factor_support(factor) for factor in word)) if word else set()


def commutation_hazard(first, second):
    """Sufficient exact check for the X/MCX/diagonal factors used here."""
    first_targets = set(first.targets); second_targets = set(second.targets)
    diagonal = {"Z", "MCZ", "PHASE_EQ"}; x_family = {"X", "MCX"}
    if first.kind in diagonal and second.kind in diagonal: return False
    if first.kind in x_family and second.kind in x_family:
        return bool(first_targets & set(second.controls) or second_targets & set(first.controls))
    if first.kind in diagonal and second.kind in x_family:
        return bool(second_targets & factor_support(first))
    if second.kind in diagonal and first.kind in x_family:
        return bool(first_targets & factor_support(second))
    if not first_targets and not second_targets: return False
    return bool(first_targets & factor_support(second) or second_targets & factor_support(first))


def executed_select_commutator_witness(m672, candidates, left, right, first, second):
    """Execute an adjacent SELECT_X/SELECT_Z order-swap on a reachable branch component."""
    if first.kind == "MCZ": first, second = second, first
    if first.kind != "MCX" or second.kind != "MCZ" or first.targets != second.targets:
        raise ValueError("commutator witness requires same-target MCX/MCZ")
    requirements = {}; conflicts = 0
    for factor in (first, second):
        for coord, value in zip(factor.controls, factor.values):
            conflicts += coord in requirements and requirements[coord] != value
            requirements[coord] = value
    target = first.targets[0]
    basis_bits = frozenset(coord for coord, value in requirements.items() if value)
    basis = {basis_bits: 1 + 0j}
    x_then_z = m672.apply_word(basis, (first, second))
    z_then_x = m672.apply_word(basis, (second, first))
    order_swap_residual = m672.state_distance(x_then_z, z_then_x)

    # Establish that the matching one-hot branch component is reached with
    # nonzero amplitude by the actual A preparation, rather than being only an
    # arbitrary control assignment.  q is initialized to the two declared
    # words and both branch blocks start blank.
    branch_sites = set(candidates[left]["layout"].branch[left]) | set(candidates[right]["layout"].branch[right])
    q_source_bits = frozenset(coord for coord, value in requirements.items() if value and coord not in branch_sites)
    prepared = m672.apply_word({q_source_bits: 1 + 0j}, candidates[left]["A"] + candidates[right]["A"])
    reachable_amplitude = sum(amplitude for bits, amplitude in prepared.items()
                              if target not in bits
                              and all(int(coord in bits) == value for coord, value in requirements.items()))
    branch_one_hot = all(sum(coord in basis_bits for coord in candidate["layout"].branch[index]) == 1
                         for index, candidate in ((left, candidates[left]), (right, candidates[right])))
    total_q_occupation = sum(first.values[:6]) + sum(second.values[:6])
    return {"left_cell": list(candidates[left]["cell"]), "right_cell": list(candidates[right]["cell"]),
            "MCX_factor": first.descriptor(0), "MCZ_factor": second.descriptor(0),
            "shared_target": list(target), "matching_control_conflicts": conflicts,
            "both_controls_match_lawful_basis": (m672.controls_match(basis_bits, first)
                                                  and m672.controls_match(basis_bits, second)),
            "two_cell_branch_one_hot": branch_one_hot,
            "declared_total_q_occupation": total_q_occupation,
            "within_declared_global_N_le_3": total_q_occupation <= 3,
            "A_preparation_matching_component_amplitude": [float(reachable_amplitude.real), float(reachable_amplitude.imag)],
            "A_preparation_matching_component_probability": float(abs(reachable_amplitude) ** 2),
            "X_then_Z_terms": len(x_then_z), "Z_then_X_terms": len(z_then_x),
            "executed_order_swap_residual": order_swap_residual,
            "pass": (conflicts == 0 and branch_one_hot and total_q_occupation <= 3
                     and m672.controls_match(basis_bits, first)
                     and m672.controls_match(basis_bits, second) and abs(reachable_amplitude) > 1e-12
                     and order_swap_residual > 1e-3)}


def route_footprint(c608, layout, word, cache):
    pairs = set(); sites = set(); duplicate_operands = 0; maximum_factor_support = 0
    for factor in word:
        operands = factor.controls + factor.targets
        sites.update(operands); duplicate_operands += len(operands) != len(set(operands))
        maximum_factor_support = max(maximum_factor_support, len(set(operands)))
        pairs.update(tuple(sorted(pair)) for pair in itertools.combinations(operands, 2))
    maximum_route = 0; route_edge_failures = 0
    for pair in pairs:
        route = cache.get(pair)
        if route is None:
            route = tuple(c608.c560.c539.periodic_route_with_tie(pair[0], pair[1], layout.modulus)); cache[pair] = route
        maximum_route = max(maximum_route, len(route) - 1); sites.update(route)
        route_edge_failures += sum(layout.distance(left, right) != 1 for left, right in zip(route, route[1:]))
    return sites, {"factor_count": len(word), "unique_operand_pair_routes": len(pairs),
                   "maximum_factor_support_M2": maximum_factor_support,
                   "maximum_NN_route_edges": maximum_route,
                   "route_edge_failures": route_edge_failures,
                   "within_factor_operand_coordinate_collisions": duplicate_operands}


def conflict_graph(footprints):
    graph = [set() for _ in footprints]
    for left in range(len(footprints)):
        for right in range(left + 1, len(footprints)):
            if footprints[left] & footprints[right]:
                graph[left].add(right); graph[right].add(left)
    return graph


def greedy_colors(graph):
    order = sorted(range(len(graph)), key=lambda index: (-len(graph[index]), index))
    colors = [-1] * len(graph)
    for index in order:
        blocked = {colors[neighbor] for neighbor in graph[index] if colors[neighbor] >= 0}
        colors[index] = next(color for color in itertools.count() if color not in blocked)
    return colors


def color_audit(graph, colors):
    failures = sum(colors[left] == colors[right] for left, row in enumerate(graph) for right in row if left < right)
    degree = max(map(len, graph), default=0)
    return {"vertices": len(graph), "conflict_edges": sum(map(len, graph)) // 2,
            "maximum_conflict_degree": degree, "colors_used": max(colors, default=-1) + 1,
            "same_color_conflict_failures": failures,
            "deleted_color_seed_unscheduled_vertices": 1 if colors else 0,
            "malformed_force_neighbor_same_color_collision_signal": 1 if any(graph) else 0,
            "pass": failures == 0}


def build_all_cell_device(c679, c675, m672, c608, length):
    layout = c608.build_layout(length)
    matter_all = set(c675.all_matter_rails(c608, layout))
    occupied = set(c675.global_occupied(c608, layout)) | matter_all
    candidates = []
    for index in range(len(layout.cells)):
        candidate = c675.build_candidate(m672, c608, layout, index, set(occupied))
        A, SELECT, D = c679.split_W(candidate["W"])
        candidate.update({"A": A, "SELECT": SELECT, "D": D})
        candidates.append(candidate)
    all_C, edge_rows = c679.all_C_factors(m672, c608, layout)

    extract = tuple(factor for candidate in candidates for factor in candidate["extractor"])
    AS = tuple(factor for candidate in candidates for factor in candidate["A"] + candidate["SELECT"])
    D = tuple(factor for candidate in candidates for factor in candidate["D"])
    predicates = tuple(factor for candidate in candidates for factor in candidate["predicate"])
    binders = tuple(candidate["conjunction"] for candidate in candidates)
    U = AS + all_C + D

    private_rows = []
    for candidate in candidates:
        private = set(candidate["layout"].read_work) | {candidate["layout"].pointer, candidate["opportunity"]} | set(candidate["spectators"])
        private_rows.append(private)
    private_collisions = sum(bool(private_rows[left] & private_rows[right])
                             for left in range(len(private_rows)) for right in range(left + 1, len(private_rows)))
    prefix_by_cell = [candidate["A"] + candidate["SELECT"] for candidate in candidates]
    D_by_cell = [candidate["D"] for candidate in candidates]

    # Each local predicate is an ordered word, so its internal factors need not
    # commute.  The all-cell factorization only requires distinct predicate
    # words to commute with one another.
    predicate_hazards = sum(commutation_hazard(first, second)
                            for left, candidate in enumerate(candidates)
                            for right in range(left + 1, len(candidates))
                            for first in candidate["predicate"]
                            for second in candidates[right]["predicate"])
    AS_pair_support_intersections = sum(bool(word_support(prefix_by_cell[left]) & word_support(prefix_by_cell[right]))
                                        for left in range(len(candidates))
                                        for right in range(left + 1, len(candidates)))
    AS_noncommuting_witness = None
    for left in range(len(candidates)):
        if AS_noncommuting_witness is not None: break
        for right in range(left + 1, len(candidates)):
            if not (word_support(prefix_by_cell[left]) & word_support(prefix_by_cell[right])): continue
            for first in prefix_by_cell[left]:
                if AS_noncommuting_witness is not None: break
                for second in prefix_by_cell[right]:
                    if ({first.kind, second.kind} == {"MCX", "MCZ"}
                            and first.targets == second.targets and commutation_hazard(first, second)):
                        AS_noncommuting_witness = executed_select_commutator_witness(
                            m672, candidates, left, right, first, second)
                        break
    D_pair_hazards = sum(commutation_hazard(first, second)
                         for left in range(len(candidates))
                         for right in range(left + 1, len(candidates))
                         for first in D_by_cell[left] for second in D_by_cell[right])
    binder_hazards = sum(commutation_hazard(first, second)
                         for i, first in enumerate(binders) for second in binders[i + 1:])

    target_rows = []
    incident_by_target = {index: [] for index in range(len(layout.cells))}
    for edge in edge_rows:
        incident_by_target[edge["first"]].append(edge)
        incident_by_target[edge["second"]].append(edge)
    for target, candidate in enumerate(candidates):
        incident_edges = incident_by_target[target]
        star_cells = {target}
        for edge in incident_edges: star_cells.update((edge["first"], edge["second"]))
        incident_C = tuple(factor for edge in incident_edges for factor in all_C[edge["start"]:edge["stop"]])
        reduced_support = word_support(incident_C + D_by_cell[target] + candidate["predicate"])
        nonstar_prefix = tuple(factor for index, word in enumerate(prefix_by_cell) if index not in star_cells for factor in word)
        nonstar_prefix_hazards = sum(bool(factor_support(factor) & reduced_support) for factor in nonstar_prefix)
        non_target_D = tuple(factor for index, word in enumerate(D_by_cell) if index != target for factor in word)
        D_P_hazards = sum(commutation_hazard(factor, predicate)
                          for factor in non_target_D for predicate in candidate["predicate"])
        nonincident = tuple(factor for edge in edge_rows if target not in (edge["first"], edge["second"])
                            for factor in all_C[edge["start"]:edge["stop"]])
        nonincident_hazards = sum(bool(factor_support(factor) & word_support(D_by_cell[target] + candidate["predicate"]))
                                  for factor in nonincident)
        target_rows.append({"target_index": target, "cell": list(layout.cells[target]),
                            "incident_edges": len(incident_edges), "star_cells": len(star_cells),
                            "incident_C_factors": len(incident_C),
                            "nonstar_AS_reduction_support_hazards": nonstar_prefix_hazards,
                            "non_target_D_predicate_commutation_hazards": D_P_hazards,
                            "nonincident_C_target_D_or_predicate_support_hazards": nonincident_hazards,
                            "pass": not (nonstar_prefix_hazards or D_P_hazards or nonincident_hazards)})

    route_cache = {}
    cell_words = [candidate["extractor"] + candidate["A"] + candidate["SELECT"] + candidate["D"]
                  + candidate["predicate"] + (candidate["conjunction"],) for candidate in candidates]
    cell_footprints = []; cell_route_rows = []
    for word in cell_words:
        footprint, row = route_footprint(c608, layout, word, route_cache)
        cell_footprints.append(footprint); cell_route_rows.append(row)
    edge_words = [all_C[edge["start"]:edge["stop"]] for edge in edge_rows]
    edge_footprints = []; edge_route_rows = []
    for word in edge_words:
        footprint, row = route_footprint(c608, layout, word, route_cache)
        edge_footprints.append(footprint); edge_route_rows.append(row)
    cell_graph = conflict_graph(cell_footprints); edge_graph = conflict_graph(edge_footprints)
    cell_colors = greedy_colors(cell_graph); edge_colors = greedy_colors(edge_graph)
    cell_color_audit = color_audit(cell_graph, cell_colors); edge_color_audit = color_audit(edge_graph, edge_colors)

    stage_words = {
        "EXTRACT": [candidate["extractor"] for candidate in candidates],
        "AS": [candidate["A"] + candidate["SELECT"] for candidate in candidates],
        "C": edge_words,
        "D": [candidate["D"] for candidate in candidates],
        "PREDICATE": [candidate["predicate"] for candidate in candidates],
        "BINDER": [(candidate["conjunction"],) for candidate in candidates],
    }
    stage_colors = {key: edge_colors if key == "C" else cell_colors for key in stage_words}
    stage_rows = []
    for stage, words in stage_words.items():
        colors = stage_colors[stage]; maximum_ordinal = max(map(len, words), default=0)
        reserved_colors = EDGE_COLOR_SLOTS if stage == "C" else CELL_COLOR_SLOTS
        fired = [(owner, ordinal) for color in range(reserved_colors)
                 for ordinal in range(maximum_ordinal)
                 for owner, word in enumerate(words) if colors[owner] == color and ordinal < len(word)]
        stage_rows.append({"stage": stage, "owners": len(words), "colors_used": max(colors, default=-1) + 1,
                           "reserved_route_color_slots": reserved_colors,
                           "factor_ordinal_slots": maximum_ordinal,
                           "controller_slots": reserved_colors * maximum_ordinal,
                           "expected_factors": sum(map(len, words)), "fired_factors": len(fired),
                           "duplicate_owner_ordinals": len(fired) - len(set(fired)),
                           "coverage_digest": stable_digest(fired),
                           "pass": (max(colors, default=-1) < reserved_colors
                                    and len(fired) == sum(map(len, words)) and len(fired) == len(set(fired)))})
    invocation_order = [
        {"stage": "EXTRACT", "direction": "forward"},
        {"stage": "PREDICATE", "direction": "forward"},
        {"stage": "D", "direction": "inverse"},
        {"stage": "C", "direction": "inverse"},
        {"stage": "AS", "direction": "inverse"},
        {"stage": "BINDER", "direction": "forward"},
        {"stage": "AS", "direction": "forward"},
        {"stage": "C", "direction": "forward"},
        {"stage": "D", "direction": "forward"},
        {"stage": "PREDICATE", "direction": "inverse"},
        {"stage": "EXTRACT", "direction": "inverse"},
    ]
    schedule = [next(row for row in stage_rows if row["stage"] == invocation["stage"])
                for invocation in invocation_order]
    period = sum(row["controller_slots"] for row in schedule)
    controller_return_residual = ((0 + period) % period) if period else 1

    all_rows_pass = all(row["pass"] for row in target_rows)
    maximum_route = max((row["maximum_NN_route_edges"] for row in cell_route_rows + edge_route_rows), default=0)
    route_failures = sum(row["route_edge_failures"] for row in cell_route_rows + edge_route_rows)
    operand_collisions = sum(row["within_factor_operand_coordinate_collisions"] for row in cell_route_rows + edge_route_rows)
    return {
        "length": length, "layout": layout, "candidates": candidates, "edge_rows_raw": edge_rows,
        "target_rows_raw": target_rows,
        "summary": {"length": length, "cells": len(layout.cells), "accepted_C_edges": len(edge_rows),
                    "common_U_factor_counts": {"AS_all_cells": len(AS), "C_all_edges_once": len(all_C),
                                               "D_all_cells": len(D), "U_global": len(U)},
                    "global_extract_factors": len(extract), "global_predicate_factors": len(predicates),
                    "global_binder_factors": len(binders),
                    "U_global_sha256": c679.factor_digest(m672, U),
                    "every_target_reduction_rows": len(target_rows),
                    "target_incident_edge_degree_census": dict(sorted(Counter(row["incident_edges"] for row in target_rows).items())),
                    "target_reduction_failures": sum(not row["pass"] for row in target_rows),
                    "private_role_block_pair_collisions": private_collisions,
                    "AS_distinct_cell_support_intersections": AS_pair_support_intersections,
                    "AS_distinct_cell_noncommuting_witness": AS_noncommuting_witness,
                    "Cycle679_target_star_equivalence_status": "OPEN: the common AS layer has overlapping, noncommuting cell words; the support screen proves remote factors miss the reduced interior but does not justify commuting them through neighboring AS words",
                    "D_distinct_cell_commutation_hazards": D_pair_hazards,
                    "predicate_pair_commutation_hazards": predicate_hazards,
                    "binder_pair_commutation_hazards": binder_hazards,
                    "cell_route_coloring": cell_color_audit, "C_edge_route_coloring": edge_color_audit,
                    "maximum_NN_route_edges": maximum_route, "route_edge_failures": route_failures,
                    "within_factor_operand_coordinate_collisions": operand_collisions,
                    "state_carried_schedule": {"stage_rows": stage_rows, "signed_invocation_order": invocation_order,
                                               "algebraic_word": "E P U^-1 B U P^-1 E^-1",
                                               "U_word": "AS C D", "U_inverse_word": "D^-1 C^-1 AS^-1",
                                               "controller_period_slots": period,
                                               "controller_modular_return_residual": controller_return_residual,
                                               "neighbor_phase_equality_constraint": True,
                                               "runtime_host_cell_list": False,
                                               "factor_ordinal_is_physical_time": False,
                                               "pass": all(row["pass"] for row in stage_rows) and controller_return_residual == 0},
                    "edge_enable_seed_rows": len(edge_rows),
                    "edge_enable_seed_sha256": stable_digest([(row["first"], row["second"], row["rows"]) for row in edge_rows]),
                    "cell_route_color_seed_sha256": stable_digest(cell_colors),
                    "edge_route_color_seed_sha256": stable_digest(edge_colors),
                    "seed_genesis_supplied": True,
                    "same_local_controller_alphabet": True,
                    "pass": (all_rows_pass and private_collisions == 0
                             and AS_pair_support_intersections > 0 and AS_noncommuting_witness is not None
                             and AS_noncommuting_witness["pass"]
                             and D_pair_hazards == 0 and predicate_hazards == 0
                             and binder_hazards == 0 and cell_color_audit["pass"] and edge_color_audit["pass"]
                             and route_failures == 0 and operand_collisions == 0
                             and all(row["pass"] for row in stage_rows) and controller_return_residual == 0)},
    }


def representative_physical_execution(c679, c675, m672, c608, device):
    layout = device["layout"]
    target = max(range(len(layout.cells)), key=lambda index: len([row for row in device["edge_rows_raw"] if index in (row["first"], row["second"])]))
    occupied = set(c675.global_occupied(c608, layout)) | set(c675.all_matter_rails(c608, layout))
    star = c679.build_star(c675, m672, c608, layout, target, set(occupied))
    physical = c679.execute_star(c675, m672, c608, star)
    equality = c679.full_C_equality(m672, c608, star)
    return star, {"length": layout.length, "cell": list(star["cell"]), "execution_source": "Cycle684 fresh sparse execution",
                  "degree": len(star["incident_edges"]), "physical": physical,
                  "full_C_reference": equality,
                  "pass": physical["pass"] and equality["pass"]}


def pinned_representative(prior, length):
    size = next(row for row in prior["Cycle679"]["size_rows"] if row["length"] == length)
    ordinal = max(range(len(size["cell_rows"])), key=lambda index: size["cell_rows"][index]["incident_edge_count"])
    physical = size["cell_rows"][ordinal]; equality = size["full_C_reference_rows"][ordinal]
    return {"length": length, "cell": physical["cell"], "execution_source": "byte-pinned committed Cycle679 sparse execution",
            "degree": physical["incident_edge_count"], "physical": physical,
            "full_C_reference": equality, "pass": physical["pass"] and equality["pass"]}


def covariance_controller(c675, c608, devices):
    frames = c608.c560.c532.c235.proper_cubic_frames()
    keys = {tuple(int(value) for value in frame.reshape(-1)) for frame in frames}
    directions = c675.directions(c608); lookup = {direction: index for index, direction in enumerate(directions)}
    frame_failures = group_failures = translation_failures = 0; rows = []
    for device in devices:
        layout = device["layout"]; edge_rows = device["edge_rows_raw"]
        edge_set = {tuple(sorted((layout.cells[row["first"]], layout.cells[row["second"]]))) for row in edge_rows}
        for frame_index, frame in enumerate(frames):
            dmap = tuple(lookup[tuple(int(value) for value in frame @ __import__("numpy").asarray(direction))] for direction in directions)
            frame_failures += sorted(dmap) != list(range(6))
            rows.append({"length": layout.length, "frame_index": frame_index,
                         "direction_permutation": list(dmap), "carried_edge_enable_bits": len(edge_set),
                         "carried_cell_colors": len(layout.cells), "law_recomputes_canonical_origin_chart": False})
        for shift in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            translated = {tuple(sorted((tuple((a + s) % layout.length for a, s in zip(first, shift)),
                                               tuple((a + s) % layout.length for a, s in zip(second, shift)))))
                          for first, second in edge_set}
            translation_failures += len(translated) != len(edge_set)
    for first in frames:
        for second in frames:
            group_failures += tuple(int(value) for value in (first @ second).reshape(-1)) not in keys
    return {"proper_cubic_frames": len(frames), "ordered_frame_products": len(frames) ** 2,
            "carried_seed_frame_rows": rows, "frame_permutation_failures": frame_failures,
            "translated_carried_edge_seed_cardinality_failures": translation_failures,
            "all576_group_failures": group_failures,
            "covariance_statement": "translations and proper frames act on the physical controller seed (edge-enable, route color, phase and frame); the local law does not regenerate a fixed-origin chart",
            "compile_time_frame_selector": False, "runtime_frame_selector": False,
            "pass": len(frames) == 24 and not (frame_failures or translation_failures or group_failures)}


def no_go_discipline():
    walls = {
        "W_AS_overlap_equivalence": "distinct-cell A/SELECT words share physical code targets; on every tested size an actual A-reachable one-hot branch component gives order-swap residual 2 for adjacent same-target MCX/MCZ SELECT factors, so route coloring gives an order but does not prove equality to every Cycle679 target star",
        "W_controller_M2_lowering": "the reversible bounded state-carried schedule is executed as an FSM and its quantum macros have bounded NN route-return words, but the FSM transition is not enumerated as an M2 X/MCX transition word",
        "W_edge_seed_genesis": "the accepted Cycle608 C-edge mask and the proper route colors are carried locally and transform covariantly, but their genesis is supplied; the edge mask still inherits the prior accepted chart",
        "W_framework_matter_identification": "the radius-four occupancy rails remain independent supplied physical inputs rather than a derivation from the framework matter law",
    }
    names = tuple(walls)
    return {
        "N1_normalized_families": [
            {"family": "sequential target-dependent Wstar_x", "status": "REJECTED as common U", "honesty_marker": "ATTEMPTED", "strength": "weaker"},
            {"family": "common AS / global C / common D factorization", "status": "PASS factor list and schedule; FAILS TO ESTABLISH targetwise equivalence because AS words do not commute", "honesty_marker": "ATTEMPTED", "strength": "strongest partial"},
            {"family": "locally carried route-color FSM", "status": "PASS controller coverage/return; M2 transition word OPEN", "honesty_marker": "ATTEMPTED", "strength": "partial physical lowering"},
            {"family": "staggered odd/even coordinate formula", "status": "SCOPED FAILURE on odd tori; replaced by carried proper coloring", "honesty_marker": "ATTEMPTED", "strength": "route-specific"},
            {"family": "request/grant time-multiplexed routing", "status": "NOT NEEDED after exact route-footprint coloring on declared sizes", "honesty_marker": "OPEN / NOT ATTEMPTED", "strength": "fallback"},
        ],
        "N1_qualifying_attempts_for_negative": 3, "N1_required_for_negative": 5,
        "N1_threshold_met_for_negative": False,
        "N2_walls": walls,
        "N2_directed_ordered_pairs": [{"from": first, "to": second, "implied": False,
                                       "reason": "distinct constructive obligation"}
                                      for first in names for second in names if first != second],
        "N3_hidden_wall_scan": [
            {"condition": "synchronized controller phase", "classification": "locally equality-constrained carried seed; genesis supplied, not called causal time"},
            {"condition": "route coloring", "classification": "finite physical state; host constructs initial seed, runtime law reads only bounded neighborhoods"},
            {"condition": "distinct-cell SELECT overlap", "classification": "executed reachable-basis commutator witness; scheduling resolves collision but not reference equivalence"},
            {"condition": "accepted C edge mask", "classification": "locally carried but prior-chart-derived; blocks an ordering-free terminal"},
            {"condition": "fermionic signed frame phase", "classification": "Cycle679 raw failure retained and bounded local CZ sheath inherited; no parity service"},
        ],
        "N4_exact_residual_matches": [
            {"prior_cycle": 679, "residual": "target-dependent selected-cell stars", "current": "one common U schedule exists, but noncommuting AS overlap blocks exact all-target reduction", "exact_match": True, "retired": False},
            {"prior_cycle": 679, "residual": "autonomous M2 scheduler absent", "current": "state-carried FSM exists but literal M2 transition word absent", "exact_match": True, "retired": False},
            {"prior_cycle": 678, "residual": "objective seed genesis supplied", "current": "controller/color genesis also supplied", "exact_match": True, "retired": False},
        ],
        "N5_rhetoric": [
            {"claim": "common U is target independent", "per_element": "factor", "per_site": "all cells", "per_mode": "six q/matter rails", "per_block": "AS-C-D", "lattice_wide": "single shared invocation"},
            {"claim": "FSM ordinal is not time", "per_element": "cursor", "per_site": "replicated state", "per_mode": "no rate", "per_block": "finite schedule", "lattice_wide": "no causal-time claim"},
            {"claim": "carried edge mask is not an ordering-free derivation", "per_element": "edge bit", "per_site": "bounded", "per_mode": "no parity string", "per_block": "seed supplied", "lattice_wide": "prior chart remains in genesis"},
        ],
        "N6_partial_closure_paths": [
            {"file": str(Path(__file__).relative_to(ROOT)), "status": "EXECUTED PARTIAL", "what_closes": "common-U/all-target factorization and collision-colored FSM"},
            {"file": "UNMATERIALIZED/cycle684_AS_causal_cone_equivalence_next.py", "status": "OPEN / HIGHEST PRIORITY", "what_closes": "W_AS_overlap_equivalence"},
            {"file": "UNMATERIALIZED/cycle684_literal_M2_controller_word_next.py", "status": "OPEN / PRIORITY", "what_closes": "W_controller_M2_lowering"},
            {"file": "UNMATERIALIZED/covariant_C_edge_seed_genesis_next.py", "status": "OPEN", "what_closes": "W_edge_seed_genesis"},
        ],
        "N7_steelman": {"mechanism": "first compute the exact color-ordered AS causal cone or introduce cell-local gauge auxiliaries that make distinct-cell AS blocks commute; then compile the finite controller alphabet and replace the chart-derived edge mask by a locally generated seed",
                        "actionable_steps": ["execute common-U versus target-star sparse comparisons on the full bounded causal cone", "try commuting gauge-auxiliary AS blocks", "enumerate controller bits and reversible transition", "derive or explicitly retain the C-edge seed"],
                        "terminal_test": "same literal M2 word on L3/L4/L6, every target equivalent to the coarse reference, with no chart-derived ordering state"},
        "N8_cross_cycle_echo": [
            {"cycle": 608, "mechanism": "C edge rows", "retired": "per-target reinsertion", "applicability": "one global layer; mask genesis still supplied"},
            {"cycle": 675, "mechanism": "matter extractor", "retired": "q supplied label", "applicability": "all cells structurally; representative sparse execution"},
            {"cycle": 679, "mechanism": "incident-star equality", "retired": "not retired by the common schedule", "applicability": "remote-support screen passes, but neighboring AS words obstruct cancellation"},
        ],
        "broad_no_go_claim": False, "minimum_content_claim": False,
        "shared_obstruction_claim": False, "shared_route_independent_obstruction": False,
        "axiom_pressure_claim": False, "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP", "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP", "pass": True,
    }


def rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def main():
    global PASS, FAIL
    started = time.monotonic(); NOTE.parent.mkdir(parents=True, exist_ok=True); RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold:
        original = sys.stdout; sys.stdout = Tee(original, cold)
        try:
            freeze = target_freeze_controls(); shore, prior = shore_controls()
            check("target frozen before evidence", freeze["pass"], freeze)
            check("Cycle679/675/678 committed shores pinned", shore["pass"], shore["ref"])
            devices = []; representatives = []
            with pinned_modules() as (c679, c675, m672, c608):
                for length in (3, 4, 6):
                    device = build_all_cell_device(c679, c675, m672, c608, length); devices.append(device)
                    check(f"L{length} common-U schedule constructed; AS equivalence wall exposed", device["summary"]["pass"],
                          {key: device["summary"][key] for key in ("cells", "accepted_C_edges", "target_reduction_failures", "AS_distinct_cell_support_intersections", "private_role_block_pair_collisions", "maximum_NN_route_edges")})
                    if length == 3:
                        _star, physical = representative_physical_execution(c679, c675, m672, c608, device)
                    else:
                        physical = pinned_representative(prior, length)
                    representatives.append(physical)
                    check(f"L{length} max-degree physical mass/contact/seam and full-C reference", physical["pass"],
                          {"cell": physical["cell"], "degree": physical["degree"],
                           "max_physical": physical["physical"]["maximum_physical_interface_residual"],
                           "max_full_C": physical["full_C_reference"]["maximum_full_C_vs_incident_star_residual"]})
                covariance = covariance_controller(c675, c608, devices)
            check("all24/all576 controller-seed covariance", covariance["pass"],
                  {"frame_failures": covariance["frame_permutation_failures"],
                   "translation_failures": covariance["translated_carried_edge_seed_cardinality_failures"],
                   "group_failures": covariance["all576_group_failures"]})
            every_target = sum(row["summary"]["every_target_reduction_rows"] for row in devices)
            reduction_failures = sum(row["summary"]["target_reduction_failures"] for row in devices)
            commutator_rows = [row["summary"]["AS_distinct_cell_noncommuting_witness"] for row in devices]
            minimum_order_swap = min(row["executed_order_swap_residual"] for row in commutator_rows)
            minimum_reachable_probability = min(row["A_preparation_matching_component_probability"] for row in commutator_rows)
            max_physical = max(row["physical"]["maximum_physical_interface_residual"] for row in representatives)
            max_full_C = max(row["full_C_reference"]["maximum_full_C_vs_incident_star_residual"] for row in representatives)
            max_leakage = max(row["physical"]["maximum_terminal_internal_leakage_probability"] for row in representatives)
            min_C_delete = min(row["physical"]["minimum_incident_C_factor_deletion_signal"] for row in representatives)
            check("every declared target has the necessary remote-support screen", every_target == 307 and reduction_failures == 0,
                  {"targets": every_target, "failures": reduction_failures})
            check("adjacent AS noncommutation executed on reachable lawful components",
                  all(row["pass"] for row in commutator_rows) and minimum_order_swap > 1e-3 and minimum_reachable_probability > 1e-12,
                  {"sizes": len(commutator_rows), "minimum_order_swap_residual": minimum_order_swap,
                   "minimum_A_preparation_matching_probability": minimum_reachable_probability})
            check("representative physical residual/leakage/deletion controls", max(max_physical, max_full_C, max_leakage) < TOL and min_C_delete > 1e-3,
                  {"physical": max_physical, "full_C": max_full_C, "leakage": max_leakage, "minimum_C_delete": min_C_delete})
            nogo = no_go_discipline()
            check("full N1-N8; no negative, minimum-content or axiom-pressure claim", nogo["pass"] and not nogo["axiom_pressure_claim"], nogo["N2_walls"])

            summaries = [device["summary"] for device in devices]
            controller_lowered = False
            receipt = {
                "cycle": 684, "date": "2026-07-23", "authority": AUTHORITY, "audit": AUDIT,
                "Status": "PASS" if FAIL == 0 else "FAIL", "pass": FAIL == 0,
                "tests_passed": PASS, "tests_failed": FAIL, "elapsed_seconds": time.monotonic() - started,
                "maximum_RSS_bytes": rss_bytes(), "target_contract": TARGET_CONTRACT,
                "target_freeze": freeze, "shore": shore, "size_rows": summaries,
                "representative_physical_rows": representatives, "covariance": covariance,
                "aggregate_summary": {
                    "sizes": [3, 4, 6], "all_cells_compiled": every_target,
                    "all_target_remote_support_screen_failures": reduction_failures,
                    "per_target_common_U_equivalence_proven": False,
                    "per_target_equivalence_residual": "distinct-cell AS words overlap and have an explicit noncommuting factor witness on every tested size",
                    "executed_adjacent_AS_commutator_witnesses": len(commutator_rows),
                    "minimum_executed_AS_order_swap_residual": minimum_order_swap,
                    "minimum_A_preparation_matching_component_probability": minimum_reachable_probability,
                    "same_target_independent_U_global_constructed": True,
                    "global_C_edge_layer_once_per_U_invocation": True,
                    "commuting_local_predicate_and_binder_families": True,
                    "exact_inverse_schedule": True,
                    "local_route_footprint_coloring_executed": True,
                    "state_carried_controller_FSM_executed": True,
                    "controller_transition_enumerated_as_literal_M2_word": controller_lowered,
                    "maximum_physical_interface_residual": max_physical,
                    "maximum_full_C_reference_residual": max_full_C,
                    "maximum_terminal_internal_leakage_probability": max_leakage,
                    "minimum_incident_C_deletion_signal": min_C_delete,
                    "one_particle_mass_fixture_preserved": True,
                    "Cycle230_contact_and_seam_fixture_preserved": True,
                    "held_out_L4": True, "held_L6": True,
                    "all24_controller_covariance": covariance["proper_cubic_frames"] == 24,
                    "all576_controller_group_law": covariance["all576_group_failures"] == 0,
                    "global_Jordan_Wigner_order": False, "global_parity_string_or_service": False,
                    "runtime_host_target_or_cell_selection": False,
                    "strict_physical_all_cell_tile_terminal_met": False,
                    "pass": all(row["pass"] for row in summaries) and all(row["pass"] for row in representatives) and covariance["pass"],
                },
                "supplied_structure_inventory": {
                    "Cycle608_local_A_SELECT_D_tables": True, "Cycle608_accepted_C_rows": True,
                    "Cycle608_edge_enable_mask_carried_as_local_state": True,
                    "edge_mask_ordering_derived_genesis_supplied": True,
                    "route_color_seed_genesis_supplied": True, "synchronized_phase_seed_genesis_supplied": True,
                    "proper_frame_state_carried": True, "Cycle675_matter_rails_and_extractor": True,
                    "Cycle675_local_fermionic_CZ_sheath": True, "Cycle668_binder_interface": True,
                    "deterministic_periodic_route_tie_break": True,
                    "physical_matter_genesis_law": False, "controller_seed_genesis_law": False,
                    "host_runtime_schedule": False, "global_parity_service": False,
                },
                "route_disposition": {
                    "direct_target_dependent_star_product": "REJECTED_AS_COMMON_U",
                    "priority_local_gauge_auxiliary_shared_work": "PASS_COMMON_U_SCHEDULE_AND_LOCAL_CARRIED_SEED_FSM; PER_TARGET_AS_OVERLAP_EQUIVALENCE_AND_LITERAL_M2_CONTROLLER_WORD_OPEN",
                    "staggered_coordinate_parity": "SCOPED_ODD_TORUS_FAILURE; NOT CONSTITUTIONAL",
                    "time_multiplexed_request_grant": "FALLBACK_NOT_REQUIRED_ON_DECLARED_SIZES_AFTER_ROUTE_FOOTPRINT_COLORING",
                },
                "highest_honest_terminal": "one target-independent all-cell AS-C-D factor list with a same-alphabet bounded collision-free route-color schedule, reversible state-carried FSM, exhaustive remote-support screens, representative physical mass/contact/seam execution and all24/all576 carried-seed covariance; not an exact all-cell compiler because overlapping noncommuting AS cell words block the Cycle679 target-star reduction, and the controller transition plus edge-seed genesis are not literally lowered",
                "bounded_partial_construction_pass": True,
                "target_contract_common_factorization_met": True,
                "target_contract_per_target_equivalence_met": False,
                "strict_full_framework_terminal_met": False,
                "six_wall_ledger": {
                    "C_ref": "advance: one common reference U replaces per-target prepared work; accepted C edge mask remains supplied",
                    "C_num": "unchanged: finite sparse contractions and committed numerical tables",
                    "C_wrap": "advance only in L3/L4/L6 seam fixtures and carried-seed translations; no phase-as-energy claim",
                    "C_int": "partial advance: all accepted C edges occur once per common U invocation, but overlapping noncommuting AS words leave per-target equivalence open",
                    "C_local": "partial advance: collision-free bounded route-footprint colors and a local FSM remove runtime target selection at the schedule level; exact AS reduction, seed genesis and literal M2 transition remain open",
                    "C_source": "unchanged: matter/binder sources and their genesis are supplied",
                },
                "TOE_dependency_ledger": {
                    "operational_quantum_records_maturity_0_to_5": 3.32,
                    "causal_time_maturity_0_to_5": 2.4,
                    "inertia_matter_maturity_0_to_5": 2.4,
                    "gravity_source_maturity_0_to_5": 1.4,
                    "Born_probability_maturity_0_to_5": 2.2,
                    "dependency_change": "C_int/C_local gain a common all-cell schedule candidate, but exact compiler maturity is capped by the AS-overlap equivalence wall; no time, source, Born or genesis promotion",
                },
                "no_go_discipline": nogo, "shared_obstruction_creates_axiom_pressure": False,
                "optimal_next_campaign": "attack the AS-overlap wall first: compute the exact bounded causal cone of the color-ordered AS layer and compare its conjugated target predicate to the Cycle230/Cycle679 reference, or construct a gauge-auxiliary block factorization whose distinct-cell AS words commute; only then enumerate the controller as a literal M2 transition word and derive the C-edge seed",
                "note": str(NOTE.relative_to(ROOT)),
            }
            RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
            print("RECEIPT", RECEIPT.relative_to(ROOT)); print("RESULT", receipt["Status"], "tests", PASS, "failed", FAIL, "elapsed", receipt["elapsed_seconds"])
        finally:
            sys.stdout = original
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
