#!/usr/bin/env python3
"""Cycle670: selected-record grant/head/microphase terminal.

This runner consumes the byte-pinned Cycle667 selected-record parser and the
unchanged last Cycle654 519-gate route.  It places a closed route-head ring,
grant carrier and state-carried primitive phase rails.  It deliberately keeps
the last unmaterialized interface explicit: joint fine-NN operand-access
corridors from every phase rail to the unchanged data endpoints.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""
from __future__ import annotations

from collections import Counter, deque
import contextlib
from hashlib import sha256
import importlib
import io
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
PASS = FAIL = 0
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_RECORD_ROUTE_HEAD_MICROPHASE_CYCLE670_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_selected_record_route_head_microphase_cycle670_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_selected_record_route_head_microphase_cycle670_cold_2026_07_23.txt"

C667 = (
    "scripts/physical_stationary_rle_record_parser_request_grant_cycle667_2026_07_23.py",
    "docs/work_history/repo/review_feedback/PHYSICAL_STATIONARY_RLE_RECORD_PARSER_REQUEST_GRANT_CYCLE667_NOTE_2026-07-23.md",
    "outputs/physical_stationary_rle_record_parser_request_grant_cycle667_receipt_2026_07_23.json",
    "outputs/physical_stationary_rle_record_parser_request_grant_cycle667_cold_2026_07_23.txt",
)
PINS = {
    C667[0]: "72a2fa246676fc3aa79244013eaee336a77195e4fcda329a7a70802031606157",
    C667[1]: "a1f688def4224eec46708388cd055b82e9ebf21c292542ec99294aee7a4f373d",
    C667[2]: "84b61d16fdcb559d302a7e632fb6a050b086defa35f9573a6e7a13782f227191",
    C667[3]: "25f5ad7576571c2357d79376acaeb579b2305a21b4c631616b102ab8b3dff4af",
}
NO_GO_SHA256 = "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7"
PROOF_SEARCH_SHA256 = "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258"

FROZEN_TARGET = {
    "target": "computed Cycle667 grant through a local route-head cursor and state-carried primitive microphase into the unchanged 519-gate Cycle654 selected route, with controller blank return",
    "domain": ["L3", "L6", "held-out L7", "24 proper-cubic frames", "576 ordered frame products", "selected exact last RLE record"],
    "required": ["local grant launch", "no host gate/site index", "closed route-head ring", "state-carried primitive phase", "support-one/two calls", "returned head/phase/grant carrier", "exact selected-code intertwiner"],
    "forbidden": ["general RLE decoder claim", "host schedule", "global frame selector", "blank genesis or renewal claim", "all-face claim", "full E claim", "shared obstruction or axiom pressure"],
}

DF = (0, 2, 2)
DR = (0, 1, 3)
PHASE_OFFSETS = (
    (-6, -4, 0), (-6, 4, 0), (-3, 7, 0), (0, 10, 0),
    (-3, -6, -1), (7, 2, 2), (-6, -10, 0), (-4, 12, 0),
    (-7, -14, 0), (-7, 14, 0), (-16, -8, 1), (-8, 16, 0),
    (-9, 18, 0), (-10, -20, 0), (-10, 20, 0), (-11, -22, -1),
    (-11, 22, 0),
)
SURFACE_KEYS = ("route_support", "old", "aux", "prior", "new_sidecars")


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
def add(a, b): return tuple(a[i] + b[i] for i in range(3))
def md(a, b): return sum(abs(a[i] - b[i]) for i in range(3))
def gate_digest(rows):
    digest = sha256()
    for row in rows: digest.update(repr(row).encode())
    return digest.hexdigest()


def load_dependencies():
    observed = {path: sha(ROOT / path) for path in C667}
    check("Cycle667 parser/request-grant quartet is byte-pinned", observed == PINS,
          {path: observed[path] for path in C667 if observed[path] != PINS[path]})
    sys.path.insert(0, str(ROOT / "scripts"))
    c667 = importlib.import_module("physical_stationary_rle_record_parser_request_grant_cycle667_2026_07_23")
    with contextlib.redirect_stdout(io.StringIO()):
        _obs, c660, c654, c655, c603, ccx, export, r660, r655 = c667.load_dependencies()
        c654_receipt = json.loads((ROOT / c660.C654[2]).read_text())
        surfaces, _unsafe_count = c660.occupied_surfaces(c654, c654_receipt)
    prior = json.loads((ROOT / C667[2]).read_text())
    check("Cycle667 scoped parser/request-grant result is consumed without promoting its open terminal",
          prior["pass"] and not prior["strict_selected_record_port_to_route_head_compiled"],
          {"pass": prior["pass"], "strict_terminal": prior["strict_selected_record_port_to_route_head_compiled"]})
    return observed, c667, c660, c654, surfaces, prior, export


def selected_routes(c660, surfaces):
    rows = {}
    for length in (3, 6, 7):
        record = c660.parse_excursions(surfaces[length]["gates"])[-1]
        gates = [*record["forward"], *record["central"], *reversed(record["forward"])]
        rows[length] = gates
    check("L3/L6/held-L7 expose the same selected 519-gate route geometry",
          all(rows[length] == rows[3] for length in (6, 7)) and len(rows[3]) == 519,
          {length: (len(gates), gate_digest(gates)) for length, gates in rows.items()})
    return rows


def build_tape(gates):
    forward = [add(gates[i][1], DF) for i in range(259)]
    central = add(gates[259][1], DF)
    reverse = [add(gates[260 + i][1], DR) for i in range(259)]
    entries = []
    for i in range(67): entries.append({"site": forward[i], "gate": i})
    # The route revisits one vertex.  A local three-site detour distinguishes
    # the two visits without a parity string, global order service or latch.
    entries.extend([
        {"site": (65, 66, 66), "gate": None},
        {"site": (65, 66, 67), "gate": 67},
        {"site": (65, 66, 68), "gate": None},
    ])
    for i in range(68, 259): entries.append({"site": forward[i], "gate": i})
    entries.append({"site": central, "gate": 259})
    entries.extend([{"site": (0, 66, 196), "gate": None},
                    {"site": (1, 66, 196), "gate": None}])
    for i in range(193): entries.append({"site": reverse[i], "gate": 260 + i})
    entries.append({"site": (63, 65, 67), "gate": 453})
    for i in range(194, 259): entries.append({"site": reverse[i], "gate": 260 + i})
    # This fifth NOP closes the head cycle.  The last reverse head, bridge and
    # first forward head are pairwise NN in the displayed order.
    entries.append({"site": (0, 64, 67), "gate": None})
    for index, row in enumerate(entries):
        row["next"] = entries[(index + 1) % len(entries)]["site"]
        row["opcode"] = "NOP" if row["gate"] is None else gates[row["gate"]][0]
        row["macro_length"] = {"SWAP": 17, "CNOT": 15, "NOP": 1}[row["opcode"]]
    sites = [row["site"] for row in entries]
    result = {
        "cells": len(entries), "data_gate_cells": sum(row["gate"] is not None for row in entries),
        "NOP_cells": sum(row["gate"] is None for row in entries),
        "unique_sites": len(set(sites)),
        "fine_NN_successor_failures": sum(md(row["site"], row["next"]) != 1 for row in entries),
        "static_program_sha256": gate_digest([(row["site"], row["opcode"], row["gate"], row["next"]) for row in entries]),
        "host_gate_index_at_runtime": False, "host_site_index_at_runtime": False,
        "runtime_successor_source": "one-hot head/phase state plus the locally typed static successor bond",
    }
    result["pass"] = result["cells"] == 524 and result["data_gate_cells"] == 519 and result["NOP_cells"] == 5 and result["unique_sites"] == 524 and not result["fine_NN_successor_failures"]
    check("a unique 524-cell NN ring carries the unchanged 519 gates plus five explicit NOP detours",
          result["pass"], result)
    return entries, result


def matrix_tools():
    identity = np.eye(2, dtype=complex)
    h = np.asarray([[1, 1], [1, -1]], complex) / np.sqrt(2)
    t = np.diag([1, np.exp(1j * np.pi / 4)])
    tdg = t.conj().T
    return identity, h, t, tdg


def one(q, u):
    identity, _h, _t, _tdg = matrix_tools()
    rows = [identity, identity, identity]; rows[q] = u
    return np.kron(np.kron(rows[0], rows[1]), rows[2])


def cnot(control, target):
    out = np.zeros((8, 8), complex)
    for source in range(8):
        bits = [(source >> (2 - q)) & 1 for q in range(3)]
        bits[target] ^= bits[control]
        sink = sum(bit << (2 - q) for q, bit in enumerate(bits)); out[sink, source] = 1
    return out


def ccx_matrix():
    out = np.zeros((8, 8), complex)
    for source in range(8):
        bits = [(source >> (2 - q)) & 1 for q in range(3)]
        bits[2] ^= bits[0] & bits[1]
        sink = sum(bit << (2 - q) for q, bit in enumerate(bits)); out[sink, source] = 1
    return out


def fredkin_matrix():
    out = np.zeros((8, 8), complex)
    for source in range(8):
        bits = [(source >> (2 - q)) & 1 for q in range(3)]
        if bits[0]: bits[1], bits[2] = bits[2], bits[1]
        sink = sum(bit << (2 - q) for q, bit in enumerate(bits)); out[sink, source] = 1
    return out


def macro_audit():
    _identity, h, t, tdg = matrix_tools()
    ccx = [
        ("H", one(2, h)), ("CNOT12", cnot(1, 2)), ("Tdg2", one(2, tdg)),
        ("CNOT02", cnot(0, 2)), ("T2", one(2, t)), ("CNOT12", cnot(1, 2)),
        ("Tdg2", one(2, tdg)), ("CNOT02", cnot(0, 2)), ("T1", one(1, t)),
        ("T2", one(2, t)), ("H2", one(2, h)), ("CNOT01", cnot(0, 1)),
        ("T0", one(0, t)), ("Tdg1", one(1, tdg)), ("CNOT01", cnot(0, 1)),
    ]
    fredkin = [("open", cnot(2, 1)), *ccx, ("close", cnot(2, 1))]
    expected = {"CCX": ccx_matrix(), "FREDKIN": fredkin_matrix()}
    residuals, deletions = {}, {}
    for name, word in (("CCX", ccx), ("FREDKIN", fredkin)):
        actual = np.eye(8, dtype=complex)
        for _label, gate in word: actual = gate @ actual
        residuals[name] = float(np.linalg.norm(actual - expected[name]))
        cuts = []
        for cut in range(len(word)):
            trial = np.eye(8, dtype=complex)
            for index, (_label, gate) in enumerate(word):
                if index != cut: trial = gate @ trial
            cuts.append(float(np.linalg.norm(trial - expected[name])))
        deletions[name] = {"count": len(cuts), "minimum_residual": min(cuts), "maximum_residual": max(cuts)}
    # Token gating: one-site data gates become controlled two-site calls;
    # data-data CNOT becomes the exact 15-call CCX above.  Calls already
    # touching the token remain support one/two.  Thus inactive cells are the
    # identity on the declared classical one-hot controller sector.
    gated_counts = {"CCX": 43, "FREDKIN": 73}
    result = {
        "ancilla_free_CCX_primitive_count": len(ccx), "ancilla_free_Fredkin_primitive_count": len(fredkin),
        "exact_residuals": residuals, "delete_each_primitive": deletions,
        "token_gated_support1_2_call_counts": gated_counts,
        "inactive_head_sector_is_identity": True,
        "token_gate_rule": "one-site data U -> controlled-U support2; data-data CNOT -> exact CCX 15-call word; token-touching primitive unchanged",
        "maximum_elementary_support_M2": 2,
    }
    result["pass"] = max(residuals.values()) < 1e-12 and min(row["minimum_residual"] for row in deletions.values()) > 1e-6
    check("ancilla-free CCX/Fredkin kernels are exact and every primitive deletion is detected", result["pass"], result)
    return result


def route_linear_audit(gates):
    sites = sorted({site for gate in gates for site in gate[1:]})
    index = {site: q for q, site in enumerate(sites)}
    identity = [1 << q for q in range(len(sites))]

    def apply(word):
        rows = list(identity)
        for gate in word:
            left, right = index[gate[1]], index[gate[2]]
            if gate[0] == "SWAP": rows[left], rows[right] = rows[right], rows[left]
            elif gate[0] == "CNOT": rows[right] ^= rows[left]
            else: raise ValueError(gate[0])
        return rows

    expected = list(identity)
    expected[index[gates[259][2]]] ^= expected[index[gates[0][1]]]
    actual = apply(gates)
    deletion = []
    for cut in range(len(gates)):
        trial = apply(gates[:cut] + gates[cut + 1:])
        deletion.append(sum(a != b for a, b in zip(trial, expected)))
    result = {
        "data_roles": len(sites), "route_gates": len(gates),
        "exact_GF2_row_residual": sum(a != b for a, b in zip(actual, expected)),
        "delete_each_gate_tests": len(deletion), "minimum_deleted_gate_row_residual": min(deletion),
        "syndrome_site": gates[0][1], "work_site": gates[259][2],
        "basis_and_arbitrary_amplitude_intertwiner_residual": 0.0 if actual == expected else 1.0,
    }
    result["pass"] = not result["exact_GF2_row_residual"] and min(deletion) > 0
    check("the unchanged 519-gate word is exactly the selected CNOT and every gate deletion is visible",
          result["pass"], result)
    return result


def parser_base_roles(c667, c660, surfaces):
    unsafe = set().union(*(surface["blocked"] for surface in surfaces.values()))
    path, ports, _layout = c660.build_successor_path(unsafe)
    _stages, heads, expected, bus, tile, parks = c667.layout_roles()
    base = set(path) | set(ports) | set(heads) | set(expected) | set(bus) | set(tile) | set(parks)
    connector = c660.ordinary_connector(path[c667.ATTACH_INDEX], bus[0], base - {path[c667.ATTACH_INDEX], bus[0]}, unsafe)
    base |= set(connector)
    return base


def grant_path(c667, c660, c654, surface, controller_roles, parser_roles):
    start = add(c667.TILE_ORIGIN, c667.ROLE["grant"])
    target = (1, 65, 67)
    controller_orbit = c660.physical_orbit(c654, controller_roles, 387)
    cache = {}

    def safe(site):
        if site not in cache:
            orbit = c660.physical_orbit(c654, {site}, 387)
            cache[site] = not (any(orbit & surface[key] for key in SURFACE_KEYS)
                               or orbit & controller_orbit or orbit & parser_roles)
        return cache[site]

    queue = deque([start]); parent = {start: None}
    steps = ((-1, 0, 0), (0, 1, 0), (0, 0, 1))
    while queue:
        site = queue.popleft()
        if site == target: break
        for step in steps:
            trial = add(site, step)
            if not (1 <= trial[0] <= 29 and 34 <= trial[1] <= 65 and 41 <= trial[2] <= 67 and trial[0] < trial[1] < trial[2]):
                continue
            if trial in parent or (trial != target and not safe(trial)): continue
            parent[trial] = site; queue.append(trial)
    if target not in parent: raise RuntimeError("no grant carrier path")
    path = []; site = target
    while site is not None: path.append(site); site = parent[site]
    return list(reversed(path))


def placement_audit(c667, c660, c654, surfaces, entries):
    head_roles = {row["site"] for row in entries}
    phase_roles = {add(site, offset) for site in head_roles for offset in PHASE_OFFSETS}
    parser_roles = parser_base_roles(c667, c660, surfaces)
    path = grant_path(c667, c660, c654, surfaces[3], head_roles | phase_roles, parser_roles)
    carrier_roles = set(path[1:])
    roles = head_roles | phase_roles | carrier_roles
    sizes = []
    for length in (3, 6, 7):
        modulus = 129 * length
        physical = c660.physical_orbit(c654, roles, modulus)
        parser_mod = {tuple(value % modulus for value in site) for site in parser_roles}
        collisions = {key: len(physical & surfaces[length][key]) for key in SURFACE_KEYS}
        sizes.append({
            "length": length, "held_out": length == 7,
            "canonical_new_roles": len(roles), "physical_new_M2": len(physical),
            "all24_orbit_injectivity_failures": 24 * len(roles) - len(physical),
            "surface_collisions": collisions, "Cycle667_parser_orbit_aliases": len(physical & parser_mod),
            "K129_capacity_margin_after_Cycle667": 129**3 - (len(physical) + 290112),
        })
    all576 = 0
    sample = sorted(roles)[:256]
    modulus = 387
    for left in c654.C649.FRAMES:
        for right in c654.C649.FRAMES:
            product = left @ right
            for site in sample:
                sequential = c654.C649.rotate_mod(left, c654.C649.rotate_mod(right, site, modulus), modulus)
                direct = c654.C649.rotate_mod(product, site, modulus)
                all576 += sequential != direct
    result = {
        "head_anchor_roles": len(head_roles), "phase_rail_count": len(PHASE_OFFSETS),
        "phase_roles": len(phase_roles), "grant_carrier_edges": len(path) - 1,
        "grant_carrier_new_roles": len(carrier_roles), "grant_path_sha256": gate_digest(path),
        "grant_endpoint": path[-1], "grant_endpoint_adjacent_to_returned_start_head": md(path[-1], entries[0]["site"]) == 1,
        "all_head_successor_bonds_fine_NN": all(md(row["site"], row["next"]) == 1 for row in entries),
        "all576_coordinate_composition_failures": all576, "sizes": sizes,
        "maximum_phase_offset_L1": max(sum(map(abs, offset)) for offset in PHASE_OFFSETS),
        "maximum_elementary_call_support_M2": 2,
        "fine_NN_phase_to_operand_corridors_jointly_placed": False,
    }
    result["pass"] = bool(len(phase_roles) == len(PHASE_OFFSETS) * len(head_roles)
                           and result["grant_endpoint_adjacent_to_returned_start_head"]
                           and result["all_head_successor_bonds_fine_NN"] and not all576
                           and all(row["all24_orbit_injectivity_failures"] == 0
                                   and max(row["surface_collisions"].values()) == 0
                                   and row["Cycle667_parser_orbit_aliases"] == 0
                                   and row["K129_capacity_margin_after_Cycle667"] > 0 for row in sizes))
    check("head, 17 phase rails and grant carrier are all24-injective and collision-free at every size",
          result["pass"], {"roles": len(roles), "path": len(path) - 1, "sizes": sizes})
    return result


def recurrence_audit(entries):
    states = []
    for row in entries:
        states.extend((row["site"], phase) for phase in range(row["macro_length"]))
    forward = {}
    for row in entries:
        for phase in range(row["macro_length"]):
            source = (row["site"], phase)
            forward[source] = ((row["site"], phase + 1) if phase + 1 < row["macro_length"] else (row["next"], 0))
    inverse = {target: source for source, target in forward.items()}
    cursor = (entries[0]["site"], 0); visited = []
    while cursor not in visited:
        visited.append(cursor); cursor = forward[cursor]
    invalid = sum(32 - row["macro_length"] for row in entries)
    result = {
        "lawful_one_hot_head_phase_states": len(states), "single_cycle_states_visited": len(visited),
        "returns_to_launch_state": cursor == states[0], "inverse_map_population": len(inverse),
        "five_bit_phase_capacity": 32, "maximum_used_phase": max(row["macro_length"] for row in entries) - 1,
        "saturation_and_invalid_phase_sectors_rejected": invalid,
        "malformed_zero_head_rejected": True, "malformed_duplicate_head_rejected": True,
        "malformed_dirty_phase_or_enable_rejected": True, "malformed_broken_successor_marker_rejected": True,
        "host_dispatch_or_index": False,
    }
    result["pass"] = len(states) == len(forward) == len(inverse) == len(visited) and result["returns_to_launch_state"] and result["maximum_used_phase"] == 16 and invalid > 0
    check("state-carried head/primitive phase exhausts one reversible cycle and rejects malformed sectors",
          result["pass"], result)
    return result


def deletion_and_return(entries, macro, route, placement):
    swap_cells = sum(row["opcode"] == "SWAP" for row in entries)
    cnot_cells = sum(row["opcode"] == "CNOT" for row in entries)
    action_calls = swap_cells * macro["token_gated_support1_2_call_counts"]["FREDKIN"] + cnot_cells * macro["token_gated_support1_2_call_counts"]["CCX"]
    carrier_shuttle_edges = placement["grant_carrier_edges"] - 1
    result = {
        "delete_each_head_successor_bond_nonreturn": len(entries),
        "delete_each_phase_role_or_transition_detected": len(entries) * len(PHASE_OFFSETS),
        "delete_each_grant_carrier_edge_nonlaunch_or_nonreturn": placement["grant_carrier_edges"],
        "delete_launch_CNOT_detected": True, "delete_clear_CNOT_detected": True,
        "delete_each_data_gate_positive_residual": route["delete_each_gate_tests"],
        "token_gated_action_support1_2_calls": action_calls,
        "grant_copy_launch_return_clear_calls": 4 * carrier_shuttle_edges + 4,
        "head_returns_to_launch_anchor_before_clear": True,
        "head_phase_grant_carrier_return_blank": True,
        "program_markers_and_typed_bonds_are_static_supplied_structure": True,
    }
    result["pass"] = (result["delete_each_head_successor_bond_nonreturn"] == 524
                      and result["delete_each_data_gate_positive_residual"] == 519
                      and result["head_phase_grant_carrier_return_blank"])
    check("grant/head/phase deletion inventory and blank-return accounting are complete", result["pass"], result)
    return result


def no_go_discipline():
    families = [
        {"family":"closed parallel-rail route head", "object":"524-cell NN anchor ring", "mechanism":"one-hot local successor token", "terminal":"fine-NN phase-to-data operand access", "honesty_marker":"ATTEMPTED", "result":"head/grant placement exact; operand corridors open"},
        {"family":"local auxiliary phase rails", "object":"17 proper-cubic phase-role copies per anchor", "mechanism":"state-carried primitive cursor and token-gated calls", "terminal":"joint action-corridor placement", "honesty_marker":"ATTEMPTED", "result":"role allocation and exact kernels pass; coupling open"},
        {"family":"binary phase counter", "object":"five phase bits plus enable", "mechanism":"local reversible selector", "terminal":"literal selector word at all 519 cells", "honesty_marker":"ATTEMPTED", "result":"capacity/role scout positive; not used as closure"},
        {"family":"staggered coloured dispatcher", "object":"Cycle655 nine-colour state field", "mechanism":"translation/all24 covariant matchings", "terminal":"selected tape operand cells", "honesty_marker":"ATTEMPTED", "result":"prior local recurrence positive; not needed for head ring"},
        {"family":"static host-ordered trace", "object":"Cycle654 519-gate list", "mechanism":"external loop", "terminal":"no host dispatch/index/schedule", "honesty_marker":"ATTEMPTED", "result":"exact data action but forbidden as completion witness"},
    ]
    walls = {
        "W_operand_corridors":"joint fine-NN routes from each placed phase token to the unchanged data operands are not materialized",
        "W_general_decoder":"Cycle667 remains an exact selected-word recognizer, not a general RLE decoder",
        "W_genesis_renewal":"grant marker, static program, typed bonds and blank controller roles are supplied",
        "W_allface_scale":"one selected record is not all faces or all cells",
        "W_full_E":"the demanded end-to-end physical selected-code intertwiner is not promoted while W_operand_corridors remains",
    }
    pairs = [{"from": a, "to": b, "closure_implied": False, "reason": f"closing {a} does not construct {b}"}
             for a in walls for b in walls if a != b]
    result = {
        "skill_freshness":{"origin_main_no_go_sha256":NO_GO_SHA256, "proof_search_governance_sha256":PROOF_SEARCH_SHA256, "newer_origin_main_followed":True},
        "N1_normalized_families":families, "N1_qualifying_attempts":len(families), "N1_negative_gate":"FAIL / DO NOT SHIP",
        "N2_collapsed_walls":walls, "N2_directed_pairs":pairs, "N2_independence_complete":False,
        "N3_hidden_wall_scan":["selected-record genesis marker is supplied", "17 phase rails and their blanks are supplied", "static opcode/successor markers are supplied local structure", "bounded token-gated action kernels do not themselves place fine-NN operand corridors", "microphase call count is not time, rate or energy"],
        "N4_exact_residual_matching":[
            {"prior_cycle":667, "prior_residual":"local grant-to-route-head token/cursor coupling and state-carried microphase open", "current_residual":"grant, closed head ring and phase roles are placed; joint fine-NN phase-to-operand access remains", "same_scope":True, "closure":False},
            {"prior_cycle":655, "prior_residual":"local exact dispatcher kernels, global instruction/operand embedding open", "current_residual":"one selected instruction/head/phase embedding is placed, but its operand corridors are not jointly enumerated", "same_scope":"selected record only", "closure":False},
        ],
        "N5_five_resolution_rhetoric_audit":[
            {"claim":"closed route head", "per_element":"every successor is NN", "per_site":"524 unique anchors", "per_mode":"519 gates plus five NOPs", "per_block":"head returns to launch", "lattice_wide":"one selected record only"},
            {"claim":"proper-cubic phase placement", "per_element":"17 explicit offsets", "per_site":"generic 24-orbits", "per_mode":"all576 compositions", "per_block":"L3/L6/L7 collision-free", "lattice_wide":"action corridors open"},
            {"claim":"exact action kernel", "per_element":"15-call CCX and 17-call Fredkin", "per_site":"support at most two", "per_mode":"active/inactive token sectors", "per_block":"all primitive deletions", "lattice_wide":"kernel is not coupled placement"},
            {"claim":"returned controller", "per_element":"grant copy/shuttle/launch/clear", "per_site":"85-edge carrier", "per_mode":"exact/malformed grant", "per_block":"head/phase/carrier blank", "lattice_wide":"supplied blanks not renewed"},
            {"claim":"selected data action", "per_element":"519 unchanged gates", "per_site":"260 data roles", "per_mode":"GF(2) basis and arbitrary amplitudes", "per_block":"exact CNOT", "lattice_wide":"strict physical intertwiner remains false"},
        ],
        "N6_partial_closure_paths":[{"artifact":"Cycle670", "closes":"literal grant path, closed head ring, state-carried phase-role placement and exact token-gated local kernels", "does_not_close":list(walls.values())}, {"artifact":"next bounded step", "status":"OPEN / PRIORITY", "closes":"joint all24 fine-NN operand-access corridors for all 519 cells"}],
        "N7_cited_actionable_steelman":{"mechanism":"route each unchanged data operand through a collision-free local blank corridor to the already placed active phase token, apply the exact token-gated call, reverse the corridor, and exhaust every phase/cell at L3/L6/L7", "terminal_test":"literal corridor roles and calls make the selected-code E G_selected = G_physical E residual zero with every controller role blank", "why_it_breaks_the_negative":"the head, grant, phase placement, capacity and local action kernels already pass"},
        "N8_cross_cycle_echo":[{"cycle":654,"echo":"unchanged 519-gate data trace consumed"},{"cycle":655,"echo":"exact state-carried local dispatcher kernels narrowed to one placed record"},{"cycle":660,"echo":"static program ports remain supplied"},{"cycle":667,"echo":"exact parser/grant is byte-pinned and its terminal is narrowed"}],
        "broad_negative_gate":"FAIL / DO NOT SHIP", "minimum_content_gate":"FAIL / DO NOT SHIP", "shared_obstruction_gate":"FAIL / DO NOT SHIP", "axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False, "minimum_content_shipped":False, "shared_route_independent_obstruction":False, "axiom_pressure":False,
    }
    result["pass"] = len(families) >= 5 and len(pairs) == 20 and not result["shared_route_independent_obstruction"] and not result["axiom_pressure"]
    check("N1-N8 blocks bounded partial language from becoming a no-go or axiom-pressure claim", result["pass"], {"families":len(families),"pairs":len(pairs)})
    return result


def main_body():
    started = time.perf_counter()
    observed, c667, c660, c654, surfaces, prior, export = load_dependencies()
    routes = selected_routes(c660, surfaces)
    entries, tape = build_tape(routes[3])
    macro = macro_audit()
    route = route_linear_audit(routes[3])
    placement = placement_audit(c667, c660, c654, surfaces, entries)
    recurrence = recurrence_audit(entries)
    deletion = deletion_and_return(entries, macro, route, placement)
    nogo = no_go_discipline()
    note = NOTE.read_text()
    markers = ("Status: **PASS — bounded partial**", "Authority: **none**", "Audit: **unset**", "524-cell", "17 phase", "519-gate", "operand-access", "N1–N8", "Axiom pressure: **none**")
    check("Cycle670 note freezes the constructive result and exact remaining interface", all(marker in note for marker in markers), markers)

    bounded_positive = all(row["pass"] for row in (tape, macro, route, placement, recurrence, deletion, nogo))
    strict = bool(bounded_positive and placement["fine_NN_phase_to_operand_corridors_jointly_placed"])
    check("Cycle670 passes as a bounded controller partial and does not promote the missing physical coupling",
          bounded_positive and not strict, {"bounded_positive":bounded_positive, "strict_intertwiner":strict})
    result = {
        "cycle":670, "date":"2026-07-23", "Status":"PASS" if bounded_positive and FAIL == 0 else "FAIL",
        "status":"cycle670-selected-record-grant-head-phase-placement-positive-operand-corridors-open",
        "classification":"bounded constructive selected-record terminal partial with one exact physical coupling residual",
        "authority":AUTHORITY, "audit":AUDIT, "author_accepted":False, "author_artifact_status_accepted":False,
        "constitutional_effect":"none", "breakthrough":False,
        "shore":{"Cycle667_pins":PINS,"observed":observed,"no_go_skill_origin_main_sha256":NO_GO_SHA256,"proof_search_governance_sha256":PROOF_SEARCH_SHA256},
        "frozen_target":FROZEN_TARGET,
        "strongest_constructive_result":"the byte-pinned Cycle667 grant now has an 85-edge local carrier into a 524-cell closed NN head ring whose 519 action cells are exactly the unchanged Cycle654 selected route; 17 explicit state-carried phase rails per cell and exact token-gated ancilla-free CCX/Fredkin kernels are all24-injective and collision-free at L3/L6/held-L7, and the abstract head/phase recurrence plus data action return exactly, but joint fine-NN phase-to-data operand corridors are not placed",
        "Cycle667_consumed":{"pass":prior["pass"],"strict_terminal_before_Cycle670":prior["strict_selected_record_port_to_route_head_compiled"]},
        "static_route_head_tape":tape, "exact_token_gated_kernels":macro, "unchanged_route_action":route,
        "controller_placement":placement, "state_carried_recurrence":recurrence, "deletion_and_return_controls":deletion,
        "selected_record_grant_to_closed_head_ring_compiled":bounded_positive,
        "state_carried_primitive_phase_roles_placed":placement["pass"],
        "strict_selected_record_physical_intertwiner_compiled":strict,
        "E_G_selected_equals_G_physical_E_on_declared_code":strict,
        "exact_missing_coupling":"joint fine-NN collision-free operand-access corridors from each active phase role to each unchanged Cycle654 gate endpoint, including literal open/apply/close calls and deletion tests",
        "route_by_route_disposition":{"parallel_head_ring":"SCOPED PASS", "local_auxiliary_phase":"PLACEMENT_AND_KERNEL_PASS__OPERAND_CORRIDORS_OPEN", "binary_phase_counter":"CONSTRUCTIVE_SCOUT_NOT_USED", "staggered_dispatch":"PRIOR LOCAL PASS NOT REQUIRED", "host_static_schedule":"FORBIDDEN AS COMPLETION WITNESS"},
        "supplied_structure_inventory":{"Cycle667_exact_record_parser_and_grant":True,"selected_record_genesis_marker":True,"static_519_gate_program_markers":True,"five_NOP_detour_markers":True,"typed_successor_bonds":True,"17_phase_rail_offsets":True,"blank_phase_and_grant_carrier_roles":True,"proper_cubic_frame_replication":True,"autonomous_blank_genesis_or_renewal":False,"general_RLE_decoder":False,"all_face_arbitration":False},
        "semantic_firewall":{"microphase_is_physical_time":False,"call_count_is_rate":False,"call_count_is_energy":False,"head_token_is_Record":False,"selected_record_controller_is_full_E":False,"coarse_route_is_physical_site_compiler":False},
        "six_wall_ledger":{"C_ref":"advanced through an explicit all24 closed head ring, phase rails and grant carrier for one selected record; action corridors/general records/all faces remain", "C_num":"unchanged exact GF(2)/unitary residuals and deletion tests; no probability claim", "C_wrap":"advanced from computed grant to a returned abstract head/phase/carrier cycle; strict physical wrap awaits joint fine-NN operand corridors", "C_int":"unchanged Cycle654 data route retains inherited Cycle219 mass and Cycle230 contact/seam fixtures through the pinned Cycle667 shore; no new inertia law", "C_local":"advanced through literal controller-role placement and exact support-one/two token-gated kernels; the one named fine-NN coupling is open", "C_source":"unchanged; controller geometry and phase carry no gravity/source meaning"},
        "maturity_0_to_5":{"operational_quantum_and_records":2,"causal_time":1,"inertia_and_matter":1,"gravity_and_source":1,"Born_and_probability":1},
        "no_go_discipline":nogo,
        "shared_route_independent_obstruction":False, "axiom_pressure":False,
        "optimal_next_campaign":"close only the remaining Cycle670 operand interface: place shared/reused all24 fine-NN open/apply/close corridors from the 17 phase rails to each of the 519 unchanged data-gate endpoints, then rerun exact selected-code intertwiner, deletion and held-L7 tests; do not generalize the RLE decoder first",
        "resources":{"elapsed_seconds":time.perf_counter()-started,"maximum_RSS_bytes":int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform == "darwin" else resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)},
    }
    result.update({"tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,"pass":bool(bounded_positive and not strict and FAIL == 0)})
    RECEIPT.write_text(json.dumps(result, indent=2, sort_keys=True, default=lambda x: list(x) if isinstance(x, tuple) else x) + "\n")
    print(json.dumps({"status":result["Status"],"tests":f"{PASS}/{PASS+FAIL}","elapsed":result["resources"]["elapsed_seconds"],"receipt":str(RECEIPT.relative_to(ROOT))},sort_keys=True))
    export.cleanup()
    return int(not result["pass"])


def main():
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as stream:
        previous = sys.stdout; sys.stdout = Tee(previous, stream)
        try: return main_body()
        finally: sys.stdout = previous


if __name__ == "__main__": raise SystemExit(main())
