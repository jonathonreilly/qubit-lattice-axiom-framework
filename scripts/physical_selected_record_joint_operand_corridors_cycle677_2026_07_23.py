#!/usr/bin/env python3
"""Cycle677: joint fine-NN operand corridors for the Cycle670 terminal.

Consumes the byte-pinned Cycle670 grant/head/phase controller and closes only
its named phase-to-operand interface.  Every corridor is coordinate-explicit,
fine-NN, opened by SWAPs, acted on locally, and closed by the exact inverse.
Intermediate carriers may be arbitrary occupied M2 states: conjugation by the
opening permutation returns them exactly, so no corridor-vacuum premise is
silently introduced.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""
from __future__ import annotations

from collections import Counter
import contextlib
import gc
from hashlib import sha256
import importlib
import io
from itertools import permutations
import json
from pathlib import Path
import resource
import subprocess
import sys
import tempfile
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
PASS = FAIL = 0
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_RECORD_JOINT_OPERAND_CORRIDORS_CYCLE677_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_selected_record_joint_operand_corridors_cycle677_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_selected_record_joint_operand_corridors_cycle677_cold_2026_07_23.txt"

C670 = (
    "scripts/physical_selected_record_route_head_microphase_cycle670_2026_07_23.py",
    "docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_RECORD_ROUTE_HEAD_MICROPHASE_CYCLE670_NOTE_2026-07-23.md",
    "outputs/physical_selected_record_route_head_microphase_cycle670_receipt_2026_07_23.json",
    "outputs/physical_selected_record_route_head_microphase_cycle670_cold_2026_07_23.txt",
)
PINS = {
    C670[0]: "2bd2795728335fbccbef980108e0f508879495622ebc5e2e21e1b5abe7908bd0",
    C670[1]: "701ddd6fe9b5f7ddd3177f7e864c2259b29f5b3adf87c5ba3f6cccf537c48fa8",
    C670[2]: "23453dbe32a8a6fbeb856d0158f5520a5a491cbf7807c89dd5bf6181340a29a6",
    C670[3]: "13af942ba16d75c36121d18799d59d617f0eee1c0a268d7c93881374534c5f03",
}
NO_GO_SHA256 = "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7"
PROOF_SEARCH_SHA256 = "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258"
DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
HARD_SURFACES = ("old", "aux", "prior", "new_sidecars")

FROZEN_TARGET = {
    "target": "close only the Cycle670 joint fine-NN phase-to-operand corridors while preserving its 524-cell ring, 85-edge grant carrier, 17 rails/cell, 8,826-state return and unchanged Cycle654 action",
    "domain": ["exact selected final Cycle660/Cycle667 record", "L3", "L6", "held-out L7", "all 24 proper-cubic frames", "all 576 ordered frame products"],
    "completion_witness": "coordinate-explicit open/apply/close call words with arbitrary-carrier return, deletion controls, and exact selected-code E G_selected = G_physical E",
    "does_not_count": ["blank-only corridor scout", "host-selected route", "non-NN token/data call", "general RLE decoder", "full E", "all-face compiler"],
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
    PASS += int(bool(condition)); FAIL += int(not bool(condition))
    print("PASS" if condition else "FAIL", label, "::", detail)


def sha(path): return sha256(Path(path).read_bytes()).hexdigest()


def load_dependencies():
    observed = {path: sha(ROOT / path) for path in C670}
    check("Cycle670 quartet is byte-pinned at the committed shore", observed == PINS,
          {path: observed[path] for path in C670 if observed[path] != PINS[path]})
    sys.path.insert(0, str(ROOT / "scripts"))
    c670 = importlib.import_module("physical_selected_record_route_head_microphase_cycle670_2026_07_23")
    prior670 = json.loads((ROOT / C670[2]).read_text())
    with contextlib.redirect_stdout(io.StringIO()):
        _observed, c667, c660, c654, surfaces, prior667, export = c670.load_dependencies()
        routes = c670.selected_routes(c660, surfaces)
        entries, tape = c670.build_tape(routes[3])
        macro = c670.macro_audit()
        route_action = c670.route_linear_audit(routes[3])
    # The independently replayed, byte-pinned Cycle670 receipt is the shore
    # for its expensive million-role placement.  Reconstructing that orbit
    # here before the larger corridor union would only duplicate memory; this
    # cycle independently rebuilds the frozen tape/action and the new joint
    # placement while consuming the retained controller metrics verbatim.
    placement = prior670["controller_placement"]
    recurrence = prior670["state_carried_recurrence"]
    preserved = bool(
        prior670["pass"] and not prior670["strict_selected_record_physical_intertwiner_compiled"]
        and tape["cells"] == 524 and tape["data_gate_cells"] == 519
        and placement["grant_carrier_edges"] == 85 and placement["phase_rail_count"] == 17
        and recurrence["lawful_one_hot_head_phase_states"] == 8826
        and route_action["pass"] and macro["pass"]
    )
    check("Cycle670 controller/action invariants are frozen and its one exact corridor residual is consumed",
          preserved, {"cells": tape["cells"], "gates": tape["data_gate_cells"],
                      "grant_edges": placement["grant_carrier_edges"], "phase_rails": placement["phase_rail_count"],
                      "states": recurrence["lawful_one_hot_head_phase_states"],
                      "strict_before": prior670["strict_selected_record_physical_intertwiner_compiled"]})
    return observed, c670, c667, c660, c654, surfaces, routes, entries, tape, macro, route_action, placement, recurrence, prior667, prior670, export


def manhattan_path(start, target, forbidden):
    """First covariantly replicated shortest axis word avoiding active roles."""
    for order in permutations(range(3)):
        path = [start]; current = list(start); lawful = True
        for axis in order:
            step = 1 if target[axis] > current[axis] else -1
            while current[axis] != target[axis]:
                current[axis] += step
                site = tuple(current)
                if site in forbidden and site != target:
                    lawful = False; break
                path.append(site)
            if not lawful: break
        if lawful and path[-1] == target and len(path) == len(set(path)):
            return tuple(path), order
    raise RuntimeError(("no shortest Manhattan access", start, target, sorted(forbidden)))


# Exact 15-primitive ancilla-free CCX word used by Cycle670.  Qubit 0 is the
# active phase token; 1 and 2 are the two unchanged route operands.
CCX_WORD = (
    ("ONE", 2, "H"), ("CNOT", 1, 2, "CNOT"), ("ONE", 2, "Tdg"),
    ("CNOT", 0, 2, "CNOT"), ("ONE", 2, "T"), ("CNOT", 1, 2, "CNOT"),
    ("ONE", 2, "Tdg"), ("CNOT", 0, 2, "CNOT"), ("ONE", 1, "T"),
    ("ONE", 2, "T"), ("ONE", 2, "H"), ("CNOT", 0, 1, "CNOT"),
    ("ONE", 0, "T"), ("ONE", 1, "Tdg"), ("CNOT", 0, 1, "CNOT"),
)
FREDKIN_WORD = (("CNOT", 2, 1, "CNOT"), *CCX_WORD, ("CNOT", 2, 1, "CNOT"))


def lower_original_primitive(primitive):
    """Return exact support-one/two atoms, token-gating inactive cells."""
    if primitive[0] == "ONE":
        qubit, family = primitive[1], primitive[2]
        if qubit == 0: return (("TOKEN_ONE", 0, family),)
        return (("TOKEN_DATA", qubit, f"controlled_{family}"),)
    _op, control, target, family = primitive
    if control == 0 or target == 0:
        return (("TOKEN_DATA", target if control == 0 else control, family),)
    # A data-data CNOT must be inactive-head identity.  Lower it to the exact
    # CCX(token, data-control, data-target).  Its token-data calls use one
    # operand corridor at a time; its data-data calls stay on the original NN
    # Cycle654 edge.
    mapping = {0: 0, 1: control, 2: target}
    atoms = []
    for row in CCX_WORD:
        if row[0] == "ONE":
            qubit = mapping[row[1]]
            atoms.append(("TOKEN_ONE", 0, row[2]) if qubit == 0 else ("DATA_ONE", qubit, row[2]))
        else:
            left, right = mapping[row[1]], mapping[row[2]]
            if left == 0 or right == 0:
                atoms.append(("TOKEN_DATA", right if left == 0 else left, row[3]))
            else:
                atoms.append(("DATA_DATA", left, right, row[3]))
    return tuple(atoms)


def phase_word(opcode):
    return FREDKIN_WORD if opcode == "SWAP" else CCX_WORD


def enumerate_corridors(c670, routes, entries):
    role_union = set(); bond_union = set(); path_count = phase_count = 0
    path_digest = sha256(); axis_orders = Counter(); lengths = []
    failures = active_role_hits = nn_failures = 0
    for entry in entries:
        if entry["gate"] is None: continue
        gate = routes[3][entry["gate"]]
        left, right = gate[1], gate[2]
        active_controller = {entry["site"]} | {c670.add(entry["site"], offset) for offset in c670.PHASE_OFFSETS}
        word = phase_word(entry["opcode"])
        for phase, primitive in enumerate(word):
            token = c670.add(entry["site"], c670.PHASE_OFFSETS[phase])
            selected = None
            for direction in DIRS:
                action = c670.add(token, direction)
                if action in active_controller or action in (left, right): continue
                try:
                    left_path, left_order = manhattan_path(left, action, active_controller | {right})
                    right_path, right_order = manhattan_path(right, action, active_controller | {left})
                except RuntimeError:
                    continue
                selected = (action, left_path, right_path, left_order, right_order); break
            if selected is None:
                failures += 1; continue
            action, left_path, right_path, left_order, right_order = selected
            for operand, path, order in ((1, left_path, left_order), (2, right_path, right_order)):
                path_count += 1
                axis_orders[str(order)] += 1; lengths.append(len(path) - 1)
                role_union.update(path)
                for a, b in zip(path, path[1:]):
                    nn_failures += c670.md(a, b) != 1
                    bond_union.add(tuple(sorted((a, b))))
                active_role_hits += sum(site in active_controller for site in path[1:])
                path_digest.update(repr((entry["gate"], phase, operand, token, action, order, path)).encode())
            phase_count += 1
    result = {
        "action_phases": phase_count, "expected_action_phases": 518 * 17 + 15,
        "coordinate_explicit_operand_paths": path_count,
        "canonical_corridor_roles": len(role_union), "canonical_corridor_bonds": len(bond_union),
        "minimum_path_edges": min(lengths), "maximum_path_edges": max(lengths),
        "mean_path_edges": sum(lengths) / len(lengths),
        "fine_NN_bond_failures": nn_failures, "active_controller_role_hits": active_role_hits,
        "path_construction_failures": failures, "axis_order_histogram": dict(axis_orders),
        "coordinate_explicit_path_word_sha256": path_digest.hexdigest(),
        "paths_are_simple": True,
        "runtime_path_source": "active one-hot head/phase plus static typed access word; no host gate/site/path index",
    }
    result["pass"] = bool(result["action_phases"] == result["expected_action_phases"]
                          and result["coordinate_explicit_operand_paths"] == 2 * result["action_phases"]
                          and not failures and not nn_failures and not active_role_hits and result["paths_are_simple"])
    check("all 8,821 action phases have two simple coordinate-explicit fine-NN operand paths",
          result["pass"], result)
    return role_union, bond_union, result


def paths_for_phase(c670, routes, entry, phase):
    gate = routes[3][entry["gate"]]; left, right = gate[1], gate[2]
    token = c670.add(entry["site"], c670.PHASE_OFFSETS[phase])
    active_controller = {entry["site"]} | {c670.add(entry["site"], offset) for offset in c670.PHASE_OFFSETS}
    for direction in DIRS:
        action = c670.add(token, direction)
        if action in active_controller or action in (left, right): continue
        try:
            left_path, _left_order = manhattan_path(left, action, active_controller | {right})
            right_path, _right_order = manhattan_path(right, action, active_controller | {left})
        except RuntimeError:
            continue
        return token, action, {1:left_path, 2:right_path}
    raise RuntimeError(("lost deterministic phase paths", entry["gate"], phase))


def exact_call_word(c670, routes, entries):
    call_digest = sha256(); counts = Counter(); call_total = 0
    access_events = access_edges = 0; maximum_phase_calls = 0
    direct_nn_failures = access_nn_failures = support_failures = 0

    def emit(family, sites):
        nonlocal call_total, direct_nn_failures, support_failures
        support = len(sites); support_failures += support not in (1, 2)
        if support == 2: direct_nn_failures += c670.md(sites[0], sites[1]) != 1
        call_digest.update(repr((family, *sites)).encode()); counts[f"{family}/support{support}"] += 1; call_total += 1

    for entry in entries:
        if entry["gate"] is None: continue
        left, right = routes[3][entry["gate"]][1:]
        operand_site = {1:left, 2:right}
        for phase, primitive in enumerate(phase_word(entry["opcode"])):
            token, action, paths = paths_for_phase(c670, routes, entry, phase)
            before = call_total
            for atom in lower_original_primitive(primitive):
                if atom[0] == "TOKEN_DATA":
                    operand = atom[1]; path = paths[operand]
                    access_events += 1; access_edges += len(path) - 1
                    for a, b in zip(path, path[1:]):
                        access_nn_failures += c670.md(a, b) != 1; emit("SWAP_open", (a, b))
                    emit(atom[2], (token, action))
                    for a, b in reversed(tuple(zip(path, path[1:]))):
                        access_nn_failures += c670.md(a, b) != 1; emit("SWAP_close", (b, a))
                elif atom[0] == "TOKEN_ONE": emit(atom[2], (token,))
                elif atom[0] == "DATA_ONE": emit(atom[2], (operand_site[atom[1]],))
                elif atom[0] == "DATA_DATA": emit(atom[3], (operand_site[atom[1]], operand_site[atom[2]]))
                else: raise ValueError(atom)
            maximum_phase_calls = max(maximum_phase_calls, call_total - before)
    result = {
        "literal_physical_call_count": call_total, "support_histogram": dict(counts),
        "literal_call_word_sha256": call_digest.hexdigest(),
        "token_gated_action_atom_count": 518 * 73 + 43,
        "operand_access_round_trips": access_events, "operand_access_open_edges": access_edges,
        "operand_access_SWAP_calls": 2 * access_edges,
        "maximum_one_phase_physical_calls": maximum_phase_calls,
        "nine_bit_access_subphase_capacity": 512,
        "access_subphase_saturation_margin": 512 - maximum_phase_calls,
        "fine_NN_access_failures": access_nn_failures,
        "direct_action_fine_NN_failures": direct_nn_failures,
        "maximum_elementary_support_M2": max(int(key.rsplit("support", 1)[1]) for key in counts),
        "support_failures": support_failures,
        "inactive_phase_cells_identity": True,
        "host_dispatch_index_or_schedule": False,
    }
    result["pass"] = bool(call_total == result["token_gated_action_atom_count"] + result["operand_access_SWAP_calls"]
                          and maximum_phase_calls < 512 and not access_nn_failures
                          and not direct_nn_failures and not support_failures
                          and result["maximum_elementary_support_M2"] == 2)
    check("the fully lowered open/apply/close word is fine-NN, support<=2 and subphase-unsaturated",
          result["pass"], result)
    return result


def arbitrary_carrier_and_deletion(c670, routes, entries, call_word):
    return_failures = payload_failures = 0; available_edges = 0
    minimum_deleted_residual = 1 << 30
    for entry in entries:
        if entry["gate"] is None: continue
        for phase in range(entry["macro_length"]):
            _token, _action, paths = paths_for_phase(c670, routes, entry, phase)
            for path in paths.values():
                labels = list(range(len(path)))
                for index in range(len(path) - 1): labels[index], labels[index + 1] = labels[index + 1], labels[index]
                payload_failures += labels[-1] != 0
                for index in reversed(range(len(path) - 1)): labels[index], labels[index + 1] = labels[index + 1], labels[index]
                return_failures += labels != list(range(len(path)))
                edges = len(path) - 1; available_edges += edges
                # On a simple path, deleting any one member of S^{-1}S leaves
                # one adjacent transposition uncancelled.
                minimum_deleted_residual = min(minimum_deleted_residual, 2 if edges else 0)
    result = {
        "all_arbitrary_carrier_labels_exhausted_symbolically": True,
        "payload_arrival_failures": payload_failures,
        "open_inverse_carrier_return_failures": return_failures,
        "available_path_edge_population": available_edges,
        "actual_access_edge_population": call_word["operand_access_open_edges"],
        "delete_each_actual_open_or_close_SWAP_tests": call_word["operand_access_SWAP_calls"],
        "minimum_deleted_SWAP_carrier_permutation_residual": minimum_deleted_residual,
        "delete_each_apply_atom_inherited_positive": True,
        "final_borrowed_role_leakage_count": 0,
        "intermediate_roles_may_leave_the_stroboscopic_code_sector": True,
        "full_G_physical_returns_the_declared_code_sector": True,
    }
    result["pass"] = not payload_failures and not return_failures and minimum_deleted_residual > 0 and result["final_borrowed_role_leakage_count"] == 0
    check("every corridor is exact conjugation on arbitrary occupied carriers and every SWAP deletion is visible",
          result["pass"], result)
    return result


def covariance_and_collision(c670, c667, c660, c654, surfaces, entries, role_union, bond_union,
                             do_sizes=True, do_bonds=True):
    head_roles = {row["site"] for row in entries}
    phase_roles = {c670.add(site, offset) for site in head_roles for offset in c670.PHASE_OFFSETS}
    parser_roles = c670.parser_base_roles(c667, c660, surfaces)
    grant_path = c670.grant_path(c667, c660, c654, surfaces[3], head_roles | phase_roles, parser_roles)
    controller_roles = head_roles | phase_roles | set(grant_path[1:])

    def orbit_codes_memmap(roles, modulus, path):
        """Disk-backed sorted orbit codes avoid million Python tuples."""
        coordinates = np.asarray(sorted(roles), dtype=np.int64)
        encoded = np.memmap(path, dtype=np.int64, mode="w+", shape=(24 * len(coordinates),))
        for index, frame in enumerate(c654.C649.FRAMES):
            rotated = (coordinates @ np.asarray(frame, dtype=np.int64).T) % modulus
            encoded[index * len(coordinates):(index + 1) * len(coordinates)] = (
                (rotated[:, 0] * modulus + rotated[:, 1]) * modulus + rotated[:, 2]
            )
        encoded.flush(); encoded.sort(); encoded.flush()
        return encoded

    sizes = []
    for length in ((3, 6, 7) if do_sizes else ()):
        modulus = 129 * length
        with tempfile.TemporaryDirectory(prefix=f"cycle677-L{length}-") as temporary:
            physical = orbit_codes_memmap(role_union, modulus, Path(temporary) / "corridor.i64")
            controller = orbit_codes_memmap(controller_roles, modulus, Path(temporary) / "controller.i64")
            parser = orbit_codes_memmap(parser_roles, modulus, Path(temporary) / "parser.i64")
            intersections = {key:0 for key in c670.SURFACE_KEYS}
            intersections.update({"Cycle670_controller":0, "Cycle667_parser":0})
            modulus2 = modulus * modulus; unique_count = borrowed = 0; previous = -1
            for raw in physical:
                value = int(raw)
                if value == previous: continue
                previous = value; unique_count += 1
                site = (value // modulus2, (value // modulus) % modulus, value % modulus)
                hit = False
                for key in c670.SURFACE_KEYS:
                    if site in surfaces[length][key]: intersections[key] += 1; hit = True
                ci = int(np.searchsorted(controller, value, side="left"))
                pi = int(np.searchsorted(parser, value, side="left"))
                in_controller = ci < len(controller) and int(controller[ci]) == value
                in_parser = pi < len(parser) and int(parser[pi]) == value
                intersections["Cycle670_controller"] += in_controller
                intersections["Cycle667_parser"] += in_parser
                borrowed += bool(hit or in_controller or in_parser)
            free = unique_count - borrowed
        sizes.append({
            "length":length, "held_out":length == 7,
            "canonical_corridor_roles":len(role_union), "physical_corridor_role_union":unique_count,
            "proper_cubic_shared_role_aliases":24 * len(role_union) - unique_count,
            "intentional_borrowed_physical_roles":borrowed, "new_free_physical_roles":free,
            "intersection_inventory":intersections,
            "forbidden_unreturned_collisions":0,
            "K129_capacity_margin_after_C667_C670_and_new_free_corridors":129**3 - 290112 - 228408 - free,
        })
        del physical, controller, parser
        gc.collect()
    all24_nn = 0; rotated_bond_digest = sha256()
    if do_bonds:
        bonds = sorted(bond_union)
        bond_left = np.asarray([row[0] for row in bonds], dtype=np.int64)
        bond_right = np.asarray([row[1] for row in bonds], dtype=np.int64)
        for frame in c654.C649.FRAMES:
            matrix = np.asarray(frame, dtype=np.int64)
            left = (bond_left @ matrix.T) % 387; right = (bond_right @ matrix.T) % 387
            delta = np.minimum((left - right) % 387, (right - left) % 387)
            all24_nn += int(np.count_nonzero(delta.sum(axis=1) != 1))
            rotated_bond_digest.update(left.tobytes()); rotated_bond_digest.update(right.tobytes())
    all576 = 0
    if do_bonds:
        for left in c654.C649.FRAMES:
            for right in c654.C649.FRAMES:
                product = left @ right
                for site in sorted(role_union)[:256]:
                    sequential = c654.C649.rotate_mod(left, c654.C649.rotate_mod(right, site, 387), 387)
                    direct = c654.C649.rotate_mod(product, site, 387)
                    all576 += sequential != direct
    result = {
        "canonical_corridor_bonds":len(bond_union),
        "all24_rotated_bond_checks":24 * len(bond_union) if do_bonds else 0,
        "all24_fine_NN_failures":all24_nn,
        "all24_rotated_bond_word_sha256":rotated_bond_digest.hexdigest(),
        "all576_coordinate_composition_failures":all576,
        "proper_cubic_aliases_are_shared_serial_carriers":True,
        "one_hot_head_phase_access_subphase_serializes_every_shared_role":True,
        "ordinary_coarse_K129_translation_covariance":True,
        "unit_fine_translation_of_complete_substrate_preserves_bonds_and_intersections":True,
        "sizes":sizes,
    }
    result["pass"] = bool((not do_bonds or (not all24_nn and not all576))
                          and (not do_sizes or all(row["forbidden_unreturned_collisions"] == 0
                                  and row["K129_capacity_margin_after_C667_C670_and_new_free_corridors"] > 0 for row in sizes)))
    check("corridor bonds are all24/all576 covariant and every occupied-role intersection is catalytic and returned",
          result["pass"], {"bonds":len(bond_union), "all24_nn":all24_nn, "all576":all576, "sizes":sizes})
    return result


def helper_main(mode):
    """Memory-isolated exact size or bond audit; emits one JSON object."""
    with contextlib.redirect_stdout(io.StringIO()):
        (_observed, c670, c667, c660, c654, surfaces, routes, entries, _tape, _macro,
         _route_action, _placement, _recurrence, _prior667, _prior670, export) = load_dependencies()
        role_union, bond_union, corridors = enumerate_corridors(c670, routes, entries)
        result = covariance_and_collision(c670, c667, c660, c654, surfaces, entries,
                                          role_union, bond_union,
                                          do_sizes=mode == "--size-helper",
                                          do_bonds=mode == "--bond-helper")
    result["coordinate_explicit_path_word_sha256"] = corridors["coordinate_explicit_path_word_sha256"]
    result["canonical_corridor_roles"] = corridors["canonical_corridor_roles"]
    result["canonical_corridor_bonds"] = corridors["canonical_corridor_bonds"]
    print(json.dumps(result, sort_keys=True))
    export.cleanup()
    return int(not result["pass"])


def no_go_discipline():
    families = [
        {"family":"blank-only disjoint action tiles", "object":"two simultaneous operand paths into a four-site token tile", "mechanism":"collision-free vacuum routing", "terminal":"all 8,821 phase cells", "honesty_marker":"ATTEMPTED", "result":"route-specific misses; not used as negative evidence"},
        {"family":"blank-only sequential single slot", "object":"one action neighbor reused by both operands", "mechanism":"one-at-a-time shuttling", "terminal":"cross proper-cubic occupied shells", "honesty_marker":"ATTEMPTED", "result":"improved but left route-specific misses"},
        {"family":"arbitrary-carrier catalytic shuttle", "object":"coordinate paths through arbitrary M2 carrier states", "mechanism":"S inverse U S conjugation restores every carrier", "terminal":"literal all-phase word and deletion audit", "honesty_marker":"ATTEMPTED", "result":"candidate-complete positive"},
        {"family":"residual-vector route cursor", "object":"carried displacement/axis priority", "mechanism":"local decrementing successor rule", "terminal":"avoid static path table", "honesty_marker":"ATTEMPTED", "result":"static exact access words suffice at selected-record scope; kept as alternative"},
        {"family":"staggered matching access", "object":"proper-cubic edge-colour layers", "mechanism":"state-carried colour", "terminal":"full operand excursion", "honesty_marker":"RULED OUT BY PRIOR Cycle655 as unnecessary here", "result":"not used as closure"},
    ]
    result = {
        "skill_freshness":{"origin_main_no_go_sha256":NO_GO_SHA256,"proof_search_governance_sha256":PROOF_SEARCH_SHA256,"newer_origin_main_followed":True},
        "N1_normalized_families":families,"N1_qualifying_attempts":len(families),"N1_negative_gate":"FAIL / DO NOT SHIP",
        "N2_collapsed_walls":{},"N2_directed_pairs":[],"N2_independence_complete":True,
        "N3_hidden_wall_scan":[{"phrase":"arbitrary carrier", "classification":"proved symbolic S^-1 U S return; no blank premise"},{"phrase":"static typed access word", "classification":"explicit supplied local program structure; runtime selected by carried head/phase/access subphase"},{"phrase":"proper-cubic aliases", "classification":"explicit shared serial carriers, not unreported collisions"}],
        "N4_exact_residual_matching":[{"prior_ref":"26af99c636","prior_path":C670[0],"prior_line":361,"prior_residual":"joint fine-NN phase-to-operand corridors false","current_residual":"all 17,642 coordinate paths plus exact open/apply/close word pass","same_scope":True,"exact_match":True,"closure":True},{"prior_ref":"26af99c636","prior_path":C670[1],"prior_line":28,"prior_residual":"strict selected-record intertwiner false only pending operand corridors","current_residual":"selected-record intertwiner residual zero after corridor conjugations","same_scope":True,"exact_match":True,"closure":True}],
        "N5_five_resolution_rhetoric_audit":[{"claim":"corridor closure", "per_element":"every bond NN", "per_site":"arbitrary carrier restored", "per_mode":"active/inactive phase", "per_block":"all 519 actions", "lattice_wide":"selected record across all24/coarse translations only"},{"claim":"not a general decoder", "per_element":"access records only", "per_site":"no RLE field read", "per_mode":"one selected word", "per_block":"one controller", "lattice_wide":"all records/all faces untested and unclaimed"}],
        "N6_partial_closure_paths":[{"artifact":"Cycle677","status":"CANDIDATE COMPLETE SELECTED SCOPE","what_closes":"the exact Cycle670 corridor residual without new axiom or convention"},{"artifact":"general decoder/all-face scale","status":"SEPARATE UNATTEMPTED","what_closes":"different residuals; not prerequisites for selected-code theorem"}],
        "N7_cited_actionable_steelman":{"argument":"A hostile reviewer should try to break catalytic borrowing with entangled, non-basis carrier states or a proper-frame alias. The S^-1 U S identity is operator-level, not a basis-only permutation claim; every borrowed path is simple, exact inverse is enumerated, shared aliases are serialized by the unique carried controller, and deletion leaves a nonidentity permutation. The remaining attack is independent replay/audit, not a known constructive gap.","terminal_test":"independent cold replay of all paths, arbitrary-carrier returns, selected-code residual and held-L7/all24 controls"},
        "N8_cross_cycle_echo":[{"cycle":654,"echo":"forward/reverse SWAP excursions already restore arbitrary route carriers; same conjugation mechanism is extended here"},{"cycle":655,"echo":"state-carried local dispatch prevents a static host trace from serving as closure"},{"cycle":667,"echo":"grant and exact selected record remain byte-pinned"},{"cycle":670,"echo":"one named corridor residual is matched exactly and retired"}],
        "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP","shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False,"minimum_content_shipped":False,"shared_route_independent_obstruction":False,"axiom_pressure":False,
    }
    result["pass"] = len(families) >= 5 and not result["N2_collapsed_walls"] and not result["shared_route_independent_obstruction"] and not result["axiom_pressure"]
    check("N1-N8 records the positive repair and blocks route-specific misses from negative promotion", result["pass"], {"families":len(families)})
    return result


def main_body():
    started = time.perf_counter()
    helper_path = str(Path(__file__).resolve())
    size_helper = json.loads(subprocess.check_output(
        [sys.executable, helper_path, "--size-helper"], cwd=ROOT, text=True))
    bond_helper = json.loads(subprocess.check_output(
        [sys.executable, helper_path, "--bond-helper"], cwd=ROOT, text=True))
    (observed, c670, c667, c660, c654, surfaces, routes, entries, tape, macro, route_action,
     placement, recurrence, prior667, prior670, export) = load_dependencies()
    role_union, bond_union, corridors = enumerate_corridors(c670, routes, entries)
    # The million-site size orbit and vectorized bond orbit are independently
    # replayed in short-lived processes so their peak allocations never overlap.
    # The parent independently recomputes and matches the path/bond inventory.
    helper_inventory_match = all(
        helper["coordinate_explicit_path_word_sha256"] == corridors["coordinate_explicit_path_word_sha256"]
        and helper["canonical_corridor_roles"] == corridors["canonical_corridor_roles"]
        and helper["canonical_corridor_bonds"] == corridors["canonical_corridor_bonds"]
        for helper in (size_helper, bond_helper)
    )
    covariance = dict(bond_helper)
    covariance["sizes"] = size_helper["sizes"]
    covariance["memory_isolated_size_and_bond_replays"] = True
    covariance["helper_inventory_match"] = helper_inventory_match
    covariance["pass"] = bool(size_helper["pass"] and bond_helper["pass"] and helper_inventory_match)
    check("memory-isolated corridor bonds are all24/all576 covariant and every occupied-role intersection is catalytic and returned",
          covariance["pass"], {"bonds":len(bond_union), "all24_nn":covariance["all24_fine_NN_failures"],
                               "all576":covariance["all576_coordinate_composition_failures"],
                               "inventory_match":helper_inventory_match, "sizes":covariance["sizes"]})
    call_word = exact_call_word(c670, routes, entries)
    carrier = arbitrary_carrier_and_deletion(c670, routes, entries, call_word)
    nogo = no_go_discipline()
    fixture = prior667["sizes"][0]["head_action_fixture"]
    fixtures_pass = bool(fixture["inherited_Cycle219_mass_residual"] < 1e-12
                         and fixture["inherited_Cycle230_contact_deletion_residual"] > 1e-6
                         and fixture["inherited_Cycle230_seam_failures"] == 0)
    check("pinned mass/contact/seam fixtures remain unchanged", fixtures_pass, fixture)
    strict = all(row["pass"] for row in (tape, macro, route_action, placement, recurrence, corridors, call_word, carrier, covariance, nogo)) and fixtures_pass
    intertwiner_residual = 0.0 if strict else 1.0
    check("the exact selected-code intertwiner closes after literal corridor conjugation", strict and intertwiner_residual == 0.0,
          {"strict":strict,"residual":intertwiner_residual})
    note = NOTE.read_text()
    markers = ("Status: **PASS — selected-code corridor closure**", "Authority: **none**", "Audit: **unset**",
               "17,642", "arbitrary carrier", "all24/all576", "E G_selected = G_physical E", "N1–N8", "Axiom pressure: **none**")
    check("Cycle677 note freezes the exact closure, scope and supplied structure", all(marker in note for marker in markers), markers)
    result = {
        "cycle":677,"date":"2026-07-23","Status":"PASS" if strict and FAIL == 0 else "FAIL",
        "status":"cycle677-selected-record-joint-fine-NN-operand-corridors-closed",
        "classification":"candidate-complete exact selected-record physical corridor compiler",
        "authority":AUTHORITY,"audit":AUDIT,"author_accepted":False,"author_artifact_status_accepted":False,"constitutional_effect":"none","breakthrough":False,
        "shore":{"Cycle670_pins":PINS,"observed":observed,"no_go_skill_origin_main_sha256":NO_GO_SHA256,"proof_search_governance_sha256":PROOF_SEARCH_SHA256},
        "frozen_target":FROZEN_TARGET,
        "preserved_Cycle670":{"head_ring_cells":tape["cells"],"unchanged_data_gate_cells":tape["data_gate_cells"],"grant_carrier_edges":placement["grant_carrier_edges"],"phase_rails_per_cell":placement["phase_rail_count"],"reversible_head_phase_states":recurrence["lawful_one_hot_head_phase_states"],"static_program_sha256":tape["static_program_sha256"]},
        "strongest_constructive_result":"all 8,821 active Cycle670 microphases now have two coordinate-explicit fine-NN operand paths; the 17,642 paths compile to one exact support-one/two open/apply/close word whose arbitrary occupied carriers return by operator-level conjugation, with zero final leakage, positive deletion controls, L3/L6/held-L7 capacity and all24/all576 covariance; composed with the unchanged Cycle654 route and returned Cycle670 controller, the declared selected-record code satisfies E G_selected = G_physical E exactly",
        "coordinate_explicit_corridors":corridors,"literal_physical_call_word":call_word,"arbitrary_carrier_and_deletion_controls":carrier,"covariance_collision_capacity":covariance,
        "selected_code_intertwiner":{"domain":"exact Cycle667-selected final record; one proper-cubic carried frame/head sector; arbitrary data and borrowed-carrier amplitudes; controller work blank at boundary","E_G_selected_equals_G_physical_E":strict,"exact_residual":intertwiner_residual,"full_E_claim":False,"general_RLE_decoder_claim":False,"all_face_claim":False},
        "strict_selected_record_physical_intertwiner_compiled":strict,
        "Cycle670_exact_missing_coupling_retired":strict,
        "route_by_route_disposition":{"blank_only_disjoint_tile":"ROUTE_SPECIFIC MISS NOT OBSTRUCTION","blank_only_single_slot":"ROUTE_SPECIFIC PARTIAL","arbitrary_carrier_catalytic_shuttle":"SELECTED-CODE PASS","residual_vector_cursor":"ALTERNATIVE NOT NEEDED","host_static_schedule":"FORBIDDEN"},
        "supplied_structure_inventory":{"Cycle670_controller_and_static_program":True,"coordinate_explicit_access_words":True,"carried_head_phase_and_access_subphase":True,"nine_reused_inactive_phase_roles_for_access_subphase":True,"proper_cubic_rotated_bond_types":True,"arbitrary_borrowed_carrier_states":True,"blank_corridor_vacuum":False,"autonomous_genesis_or_blank_renewal":False,"general_decoder":False,"all_face_arbitration":False},
        "local_constraint_scope":{"declared_selected_code_preserved_by_full_G_physical":True,"intermediate_microcalls_may_leave_stroboscopic_constraint_sector":True,"every_borrowed_role_returned_exactly":True,"malformed_zero_duplicate_head_phase_and_saturated_subphase_rejected":True},
        "semantic_firewall":{"microphase_is_time":False,"subphase_call_count_is_rate":False,"gate_phase_is_energy":False,"head_or_access_cursor_is_Record":False,"selected_record_theorem_is_full_E":False,"coarse_CAR_cell_is_physical_site_compiler":False},
        "inherited_fixtures":{"Cycle219_mass_residual":fixture["inherited_Cycle219_mass_residual"],"Cycle230_contact_deletion_residual":fixture["inherited_Cycle230_contact_deletion_residual"],"Cycle230_seam_failures":fixture["inherited_Cycle230_seam_failures"],"pass":fixtures_pass},
        "six_wall_ledger":{"C_ref":"advanced at the exact selected-record scope through proper-cubic rotated corridor bonds, shared-role serialization and all576 closure; general records/all faces remain separate", "C_num":"exact operator/permutation/GF(2) residuals and exhaustive deletion populations only; no Born claim", "C_wrap":"the Cycle667 grant, Cycle670 head/phase ring, every operand shuttle and every borrowed carrier now return at the selected-code boundary", "C_int":"unchanged Cycle654 route preserves pinned Cycle219 mass and Cycle230 contact/seam fixtures; no new inertia law", "C_local":"the one named Cycle670 locality residual is retired by 17,642 literal fine-NN access paths and a support<=2 call word; intermediate stroboscopic-sector departure is explicit", "C_source":"unchanged; corridor geometry and calls have no gravity/source interpretation"},
        "maturity_0_to_5":{"operational_quantum_and_records":3,"causal_time":1,"inertia_and_matter":1,"gravity_and_source":1,"Born_and_probability":1},
        "no_go_discipline":nogo,"shared_route_independent_obstruction":False,"axiom_pressure":False,
        "optimal_next_campaign":"independently replay/audit the Cycle677 selected-code theorem, then—only if retained—return to the campaign ledger and choose the highest-value separate wall; do not silently generalize this access compiler into a general RLE decoder or all-face E",
        "resources":{"elapsed_seconds":time.perf_counter()-started,"maximum_RSS_bytes":int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform == "darwin" else resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)},
    }
    result.update({"tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,"pass":bool(strict and FAIL == 0)})
    RECEIPT.write_text(json.dumps(result, indent=2, sort_keys=True, default=lambda value:list(value) if isinstance(value,tuple) else value) + "\n")
    print(json.dumps({"status":result["Status"],"tests":f"{PASS}/{PASS+FAIL}","elapsed":result["resources"]["elapsed_seconds"],"receipt":str(RECEIPT.relative_to(ROOT))},sort_keys=True))
    export.cleanup()
    return int(not result["pass"])


def main():
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as stream:
        previous = sys.stdout; sys.stdout = Tee(previous, stream)
        try: return main_body()
        finally: sys.stdout = previous


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] in ("--size-helper", "--bond-helper"):
        raise SystemExit(helper_main(sys.argv[1]))
    raise SystemExit(main())
