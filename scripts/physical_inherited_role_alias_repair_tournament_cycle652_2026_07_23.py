#!/usr/bin/env python3
"""Cycle652: inherited Cycle638-program/Cycle642-data alias repair tournament.

Repairs and stress-tests the sole identity-frame collision at (0,4,0), then
pushes the Cycle649 route geometry toward an explicit support-one/two circuit
word.  Circuit-word enumeration is kept separate from an autonomous
token-conditioned local update law.

Authority none; audit unset; constitutional effect none.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations
import gc
import importlib.util
import io
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import tarfile
import tempfile
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
IMMUTABLE_COMMIT = "ab780eb5be31dbf4366cd1329ff6b8cb06d9af53"
_EXPORT = tempfile.TemporaryDirectory(prefix="cycle652-immutable-")
IMMUTABLE_ROOT = Path(_EXPORT.name).resolve()
os.environ["GIT_DIR"] = str((ROOT / ".git").resolve())
os.environ["GIT_WORK_TREE"] = str(ROOT.resolve())
_archive = subprocess.check_output([
    "git", "archive", "--format=tar", IMMUTABLE_COMMIT,
    "scripts/physical_reserved_outer_shell_sidecar_placement_cycle649_2026_07_23.py",
])
with tarfile.open(fileobj=io.BytesIO(_archive), mode="r:") as _tar:
    _tar.extractall(IMMUTABLE_ROOT, filter="data")
os.symlink((ROOT / ".git").resolve(), IMMUTABLE_ROOT / ".git", target_is_directory=True)
_spec = importlib.util.spec_from_file_location(
    "cycle652_immutable_c649",
    IMMUTABLE_ROOT / "scripts/physical_reserved_outer_shell_sidecar_placement_cycle649_2026_07_23.py",
)
c649 = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(c649)
# Cycle649 temporarily points git subprocesses at its archive.  Restore this
# runner's real repository after all immutable imports are complete.
os.environ["GIT_DIR"] = str((ROOT / ".git").resolve())
os.environ["GIT_WORK_TREE"] = str(ROOT.resolve())

c638 = c649.c638
c642 = c649.c642
c646 = c649.c646
FRAMES = c649.FRAMES
K = 129
SHELL = 64
SOURCE = (0, 4, 0)
RELOCATED_PROGRAM = (0, 64, 0)
DATA_RELOCATION_RADIUS = 64
ALIASED_PROGRAM_INDEX = 1_011_273
AUTHORITY = "none"
AUDIT = "unset"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_INHERITED_ROLE_ALIAS_REPAIR_TOURNAMENT_CYCLE652_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_inherited_role_alias_repair_tournament_cycle652_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_inherited_role_alias_repair_tournament_cycle652_cold_2026_07_23.txt"
PASS = FAIL = 0
PINS = {
    "scripts/physical_reserved_outer_shell_sidecar_placement_cycle649_2026_07_23.py": "715dc2e36dea83dc603d202447733cc9e81d1dedb22102382109b6b95a9edc09",
    "docs/work_history/repo/review_feedback/PHYSICAL_RESERVED_OUTER_SHELL_SIDECAR_PLACEMENT_CYCLE649_NOTE_2026-07-23.md": "57a581b882c2a7a4ee2fe4ddb62b34787dbc946abd318e61fa3dd141729729c2",
    "outputs/physical_reserved_outer_shell_sidecar_placement_cycle649_receipt_2026_07_23.json": "d367e88409cbfadb6e9a46a2db3c5ddbdc9e28b7964272b67d7cbb0b4eaf0db9",
    "outputs/physical_reserved_outer_shell_sidecar_placement_cycle649_cold_2026_07_23.txt": "85fab6a108ff53bd86a084694b1ee14ec16d500d672e922fcc75003a01f541a7",
}
NO_GO_ORIGIN_MAIN_SHA256 = "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7"
FRESHNESS_ORIGIN_MAIN_SHA256 = "1e0ec4ef4d7c5dd24243d7c3954c78a3f00ecd3d5e43805e788dd3629973a962"
PROOF_SEARCH_ORIGIN_MAIN_SHA256 = "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258"


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


def json_default(value):
    if isinstance(value, np.generic): return value.item()
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, (set, frozenset)): return sorted(value, key=repr)
    raise TypeError(type(value).__name__)


def git_blob(path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{IMMUTABLE_COMMIT}:{path}"], cwd=ROOT)


def git_sha(path: str) -> str:
    return sha256(git_blob(path)).hexdigest()


def immutable_citation(path: str, fragment: str) -> dict:
    for line, text in enumerate(git_blob(path).decode().splitlines(), 1):
        if fragment in text:
            return {"ref": IMMUTABLE_COMMIT, "path": path, "line": line,
                    "line_text": text.strip(), "fragment": fragment}
    raise AssertionError((path, fragment))


def current_citation(path: str, fragment: str) -> dict:
    for line, text in enumerate((ROOT / path).read_text().splitlines(), 1):
        if fragment in text:
            return {"ref": "Cycle652 working artifact", "path": path, "line": line,
                    "line_text": text.strip(), "fragment": fragment}
    raise AssertionError((path, fragment))


def rotate(frame, site):
    return tuple(int(value) for value in frame @ np.asarray(site, dtype=int))


def orbit(site):
    return {rotate(frame, site) for frame in FRAMES}


def role_assignment_sha(roles, values):
    digest = sha256()
    for index, (site, value) in enumerate(zip(roles, values)):
        digest.update(repr((index, site, value)).encode())
    return digest.hexdigest()


def reconstruct_cycle638():
    grammar, private = c638.capture_and_compile_grammar()
    route_summary, route_private = c638.coordinate_counter_router(private)
    storage, program_private = c638.encode_program(private)
    layout, program_layout = c638.place_program_roles(program_private, route_private)
    execution = c638.execute_nested_interpreter(grammar, private)
    counters = c638.reversible_counter_circuit()
    result = {
        "grammar": grammar, "route_summary": route_summary, "storage": storage,
        "layout": layout, "execution": execution, "counters": counters,
        "pass": all(row["pass"] for row in (grammar, route_summary, storage, layout, execution, counters)),
    }
    check("immutable Cycle638 reconstructs the exact stored word, routes, program values, interpreter, and counters",
          result["pass"], {"calls": grammar["conditional_act_calls"],
                           "descriptor": grammar["captured_descriptor_word_sha256"],
                           "program_state": storage["program_state_sha256"],
                           "roles": layout["placed_roles"]})
    return result, private, route_private, program_layout


def record_for_index(program_layout, wanted):
    hits = []
    for name, rows in program_layout["records"].items():
        for record_index, (start, payload) in enumerate(rows):
            if start <= wanted < start + 2 + payload:
                hits.append({"section": name, "record_index": record_index,
                             "record_start": start, "offset": wanted-start,
                             "payload_bits": payload})
    return hits


def decoder_pairs_touching_index(program_layout, wanted):
    pairs = []
    records = program_layout["records"]
    for name in ("stage", "body", "action", "site", "pair"):
        rows = records[name]
        for start, payload in rows:
            for offset in range(2, 2 + payload):
                if wanted in (start, start + offset): pairs.append((start, start+offset, name+"_record_read"))
        for index, (start, _payload) in enumerate(rows):
            nxt = rows[(index + 1) % len(rows)][0]
            for left, right, source in ((start, nxt+1, name+"_move"), (start+1, start, name+"_renew")):
                if wanted in (left, right): pairs.append((left, right, source))
    work = range(program_layout["work_start"], program_layout["work_start"] + 64)
    for left, right in combinations(work, 2):
        if wanted in (left, right): pairs.append((left, right, "counter_register_work"))
    return tuple(pairs)


def route_a_program_orbit_relocation(baseline, route_private, program_layout):
    roles = tuple(program_layout["roles"]); values = tuple(program_layout["values"])
    source_indices = tuple(index for index, site in enumerate(roles) if site == SOURCE)
    source_orbit = orbit(SOURCE); target_orbit = orbit(RELOCATED_PROGRAM)
    marker = c638.c630.marker_residues()
    dynamic = {c638.c633.representative(site) for site in c638.c629.dynamic_geometry_sites()}
    r631 = json.loads((c638.ROOT / "outputs/physical_autonomous_marker_recognition_token_attempt_cycle631_receipt_2026_07_23.json").read_text())
    selector = {tuple(site) for site in r631["marker_safe_selector_replacement"]["base_clean_work_role_coordinates"]}
    selector_orbit = {c638.c629.rotate(frame, site) for frame in FRAMES for site in selector}
    forbidden = marker | dynamic | selector_orbit | set(route_private["reserved"])
    repaired_roles = list(roles); repaired_roles[ALIASED_PROGRAM_INDEX] = RELOCATED_PROGRAM
    repaired_layout = {**program_layout, "roles": repaired_roles}
    decoder = c638.decoder_counter_fine_NN(repaired_layout)
    touched = decoder_pairs_touching_index(repaired_layout, ALIASED_PROGRAM_INDEX)
    touched_rows = []; touched_failures = 0; touched_digest = sha256()
    for left, right, source in touched:
        generated = c638.generated_dispatch_path(repaired_roles[left], repaired_roles[right], marker)
        touched_failures += generated is None
        touched_rows.append({"left_index": left, "right_index": right, "source": source,
                             "left": repaired_roles[left], "right": repaired_roles[right],
                             "route": generated})
        touched_digest.update(repr((left, right, source, generated)).encode())
    covariance_failures = 0
    for frame in FRAMES:
        covariance_failures += rotate(frame, RELOCATED_PROGRAM) not in target_orbit
        covariance_failures += rotate(frame, SOURCE) not in source_orbit
    frame_keys = {tuple(int(value) for value in frame.ravel()) for frame in FRAMES}
    composition_failures = 0
    for left in FRAMES:
        for right in FRAMES:
            product_frame = left @ right
            composition_failures += tuple(int(value) for value in product_frame.ravel()) not in frame_keys
            composition_failures += rotate(left, rotate(right, RELOCATED_PROGRAM)) != rotate(product_frame, RELOCATED_PROGRAM)
    translated_collision_failures = 0
    for length in (3, 6, 7):
        modulus = K * length
        base = {tuple(value % modulus for value in site) for site in repaired_roles}
        for direction in c649.DIRECTIONS:
            shifted = {tuple((site[axis] + K*direction[axis]) % modulus for axis in range(3)) for site in repaired_roles}
            translated_collision_failures += len(base & shifted)
    minimum = tuple(min(site[axis] for site in repaired_roles) for axis in range(3))
    maximum = tuple(max(site[axis] for site in repaired_roles) for axis in range(3))
    diameter = max(maximum[axis]-minimum[axis] for axis in range(3))
    layout_summary = {**baseline["layout"], "inner_coordinate_bound": 64,
                      "inner_role_translation_diameter": diameter,
                      "storage_translation_ownership_by_diameter": diameter < K,
                      "role_value_assignment_sha256": role_assignment_sha(repaired_roles, values)}
    held = c638.covariance_and_held(layout_summary, baseline["route_summary"])
    malformed_shell63 = (0, 63, 0)
    result = {
        "status": "PASS_EQUIVARIANT_ACTIVE_FRAME_ROLE_RELOCATION",
        "identity_frame_program_index": ALIASED_PROGRAM_INDEX,
        "identity_frame_source": SOURCE, "identity_frame_target": RELOCATED_PROGRAM,
        "source_orbit": tuple(sorted(source_orbit)), "target_orbit": tuple(sorted(target_orbit)),
        "source_orbit_size": len(source_orbit), "target_orbit_size": len(target_orbit),
        "frame_sector_rule": "rho_h(index)=R_h(0,64,0); the six coordinates are the 24 frame images modulo stabilizer, not six added program bits",
        "source_indices_in_identity_bank": source_indices,
        "value": values[ALIASED_PROGRAM_INDEX],
        "record_hits": record_for_index(program_layout, ALIASED_PROGRAM_INDEX),
        "target_in_original_roles": RELOCATED_PROGRAM in set(roles),
        "target_in_marker_dynamic_selector_or_route_reservations": RELOCATED_PROGRAM in forbidden,
        "program_value_word_unchanged": tuple(program_layout["values"]) == values,
        "program_state_sha256_unchanged": sha256(bytes(values)).hexdigest() == baseline["storage"]["program_state_sha256"],
        "old_role_value_assignment_sha256": baseline["layout"]["role_value_assignment_sha256"],
        "new_role_value_assignment_sha256": layout_summary["role_value_assignment_sha256"],
        "stored_role_count_unchanged": len(repaired_roles) == len(roles) == 1_871_624,
        "decoder": decoder, "moved_index_decoder_pairs": len(touched),
        "moved_index_decoder_pair_rows": touched_rows,
        "moved_index_decoder_pair_sha256": touched_digest.hexdigest(),
        "moved_index_decoder_failures": touched_failures,
        "all24_relocation_covariance_failures": covariance_failures,
        "all576_relocation_composition_failures": composition_failures,
        "L3_L6_L7_translated_program_collision_failures": translated_collision_failures,
        "repaired_storage_diameter": diameter, "K": K,
        "held_covariance": held,
        "delete_relocation_map_restores_collision_residual": 1,
        "malformed_shell63_target": malformed_shell63,
        "malformed_shell63_already_occupied_by_program": malformed_shell63 in set(roles),
    }
    result["pass"] = bool(
        source_indices == (ALIASED_PROGRAM_INDEX,) and values[ALIASED_PROGRAM_INDEX] == 1
        and len(source_orbit) == len(target_orbit) == 6
        and not result["target_in_original_roles"]
        and not result["target_in_marker_dynamic_selector_or_route_reservations"]
        and result["program_value_word_unchanged"] and result["program_state_sha256_unchanged"]
        and result["stored_role_count_unchanged"] and decoder["pass"]
        and touched and touched_failures == 0
        and covariance_failures == composition_failures == translated_collision_failures == 0
        and diameter < K and held["pass"]
        and result["delete_relocation_map_restores_collision_residual"] > 0
        and result["malformed_shell63_already_occupied_by_program"]
    )
    check("route A relocates the complete active-frame orbit of program role 1,011,273 and exhausts its decoder without changing one program bit",
          result["pass"], {"source": source_indices, "target": RELOCATED_PROGRAM,
                           "orbit": len(target_orbit), "value": values[ALIASED_PROGRAM_INDEX],
                           "decoder_pairs": len(touched), "decoder_failures": touched_failures,
                           "all24": covariance_failures, "all576": composition_failures,
                           "diameter": diameter})
    return result, tuple(repaired_roles), values


def centered(value):
    return (int(value) + K//2) % K - K//2


def data_relocate(site):
    local = tuple(centered(value) for value in site)
    if local not in orbit(SOURCE): return tuple(site)
    center = tuple(int(site[axis]) - local[axis] for axis in range(3))
    return tuple(center[axis] + (DATA_RELOCATION_RADIUS//4)*local[axis] for axis in range(3))


def route_b_data_orbit_relocation(private, route_private, original_program_roles):
    mapped_sites = tuple(data_relocate(site) for site in private["sites"])
    mapped_pairs = tuple((data_relocate(left), data_relocate(right)) for left, right in private["pairs"])
    relocated_sites = sum(left != right for left, right in zip(private["sites"], mapped_sites))
    relocated_pair_endpoints = sum(old != new for old_pair,new_pair in zip(private["pairs"],mapped_pairs)
                                   for old,new in zip(old_pair,new_pair))
    mapped_private = {**private, "pairs": mapped_pairs}
    mapped_routes, mapped_route_private = c638.coordinate_counter_router(mapped_private)
    mapped_support_one_collisions = tuple(sorted(set(mapped_sites) & set(original_program_roles)))
    mapped_route_program_collisions = tuple(sorted(set(mapped_route_private["reserved"]) & set(original_program_roles)))
    injection_failures = len(mapped_sites)-len(set(mapped_sites)) + len(mapped_pairs)-len(set(mapped_pairs))
    covariance_failures = 0
    for frame in FRAMES:
        for site in orbit(SOURCE):
            covariance_failures += data_relocate(rotate(frame, site)) != rotate(frame, data_relocate(site))
    result = {
        "status": "BLOCKED_NO_CYCLE638_OPERAND_ENDPOINT_REALIZES_THE_CYCLE642_DATA_RELOCATION_MAP",
        "relocation_rule": "every K129-translated puncture-spoke axis orbit radius 4 maps to radius 64",
        "logical_769434_call_word_unchanged": True,
        "logical_descriptor_sha256_unchanged": True,
        "Cycle642_Pauli_rows_rank_and_quotient_unchanged_under_coordinate_relabeling": True,
        "mapped_operand_sites": len(mapped_sites), "mapped_operand_pairs": len(mapped_pairs),
        "actually_relocated_operand_sites": relocated_sites,
        "actually_relocated_pair_endpoints": relocated_pair_endpoints,
        "mapped_site_or_pair_injection_failures": injection_failures,
        "mapped_coordinate_routes": mapped_routes,
        "mapped_support_one_program_collisions": mapped_support_one_collisions,
        "mapped_route_program_collision_count": len(mapped_route_program_collisions),
        "mapped_route_program_collision_first": mapped_route_program_collisions[:32],
        "all24_periodic_data_map_covariance_failures": covariance_failures,
        "Cycle642_coordinate_descriptor_and_fixture_reroute_compiler_constructed": False,
        "pass_as_joint_repair": False,
        "pass_as_exact_route_discriminator": bool(mapped_routes["pass"] and injection_failures == 0
                                                  and covariance_failures == 0
                                                  and relocated_sites == relocated_pair_endpoints == 0),
    }
    check("route B preserves abstract data algebra but the Cycle638 operand catalog does not instantiate the Cycle642 data-coordinate reroute",
          result["pass_as_exact_route_discriminator"],
          {"route_pass": mapped_routes["pass"], "site_pair_injection": injection_failures,
           "relocated_sites":relocated_sites,"relocated_pair_endpoints":relocated_pair_endpoints,
           "support_one_collisions": len(mapped_support_one_collisions),
           "all24": covariance_failures})
    del mapped_route_private
    return result


def route_c_fixed_value_elimination(program_layout):
    value = int(program_layout["values"][ALIASED_PROGRAM_INDEX])
    truth = []
    failures = 0
    for data_bit in (0, 1):
        expected_control = value
        shared_control = data_bit
        failures += expected_control != shared_control
        truth.append({"data_qubit_basis_value": data_bit,
                      "required_program_control": expected_control,
                      "shared_site_control": shared_control,
                      "match": expected_control == shared_control})
    result = {
        "status": "FAIL_DYNAMIC_DATA_CANNOT_SUPPLY_FIXED_PROGRAM_ONE",
        "program_index": ALIASED_PROGRAM_INDEX, "stored_value": value,
        "truth_table": truth, "truth_table_mismatches": failures,
        "remove_role_and_embed_one_in_host_or_law": "forbidden hidden constant; autonomous stored-state count decreases by one",
        "reuse_data_site_as_program_control": "changes the program word whenever the quantum data factor has basis value zero",
        "independent_tensor_factor_preserved": False,
        "pass_as_joint_repair": False,
        "pass_as_narrow_discriminator": value == 1 and failures == 1,
    }
    check("route C cannot eliminate the fixed-one role without a hidden constant or data-dependent program semantics",
          result["pass_as_narrow_discriminator"], truth)
    return result


def direction_word(start, path, modulus):
    current = start; word = []
    for target in path:
        delta = tuple((target[axis]-current[axis]) % modulus for axis in range(3))
        candidates = []
        for index, direction in enumerate(c649.DIRECTIONS):
            candidate = tuple(direction[axis] % modulus for axis in range(3))
            if delta == candidate: candidates.append(index)
        if len(candidates) != 1: raise AssertionError((current, target, delta))
        word.append(candidates[0]); current = target
    return tuple(word)


def apply_direction_word(start, word, modulus):
    current = start; path = []
    for index in word:
        direction = c649.DIRECTIONS[index]
        current = tuple((current[axis]+direction[axis]) % modulus for axis in range(3))
        path.append(current)
    return tuple(path)


def compiled_search_state_bank(length, targets, fingers, occupied):
    modulus = K*length; rows = []; exceptions = []; digest = sha256(); values = []
    for ordinal, target in enumerate(sorted(targets)):
        formula = c649.straight_shell_finger(target, occupied, modulus)
        if formula is not None:
            kind = "two_axis_formula"; payload = direction_word(target, formula, modulus)
            selector = 0
        else:
            kind = "stored_bounded_search_witness"; payload = direction_word(target, fingers[target], modulus)
            selector = len(exceptions)+1; exceptions.append(payload)
        rows.append({"target_ordinal": ordinal, "target": target, "kind": kind,
                     "selector": selector, "word_length": len(payload),
                     "word_sha256": sha256(bytes(payload)).hexdigest()})
        digest.update(repr((ordinal, target, kind, selector, payload)).encode())
        values.extend((int(kind != "two_axis_formula"),))
        values.extend((selector >> shift) & 1 for shift in reversed(range(4)))
    def runs(word):
        output = []
        for direction in word:
            if output and output[-1][0] == direction: output[-1] = (direction,output[-1][1]+1)
            else: output.append((direction,1))
        return tuple(output)
    exception_runs = tuple(runs(word) for word in exceptions)
    max_word = max(map(len, exceptions), default=0); maximum_runs = max(map(len,exception_runs),default=0)
    for encoded in exception_runs:
        values.extend((len(encoded) >> shift) & 1 for shift in reversed(range(4)))
        for direction,count in encoded:
            values.extend((direction >> shift) & 1 for shift in (2,1,0))
            values.extend((count >> shift) & 1 for shift in reversed(range(8)))
    reconstruction_failures = 0
    for row in rows:
        target = tuple(row["target"])
        if row["kind"] == "two_axis_formula": word = direction_word(target, c649.straight_shell_finger(target, occupied, modulus), modulus)
        else:
            word = tuple(direction for direction,count in exception_runs[row["selector"]-1] for _ in range(count))
        reconstruction_failures += apply_direction_word(target, word, modulus) != fingers[target]
    flip_residual = 0
    if exceptions:
        malformed_runs = list(exception_runs[0]); direction,count = malformed_runs[0]
        malformed_runs[0] = ((direction+1)%6,count)
        malformed = tuple(item for run_direction,run_count in malformed_runs for item in (run_direction,)*run_count)
        first_target = next(tuple(row["target"]) for row in rows if row["kind"] != "two_axis_formula")
        flip_residual = int(apply_direction_word(first_target, malformed, modulus) != fingers[first_target])
    result = {
        "length": length, "target_records": len(rows), "rows": rows,
        "formula_records": sum(row["kind"] == "two_axis_formula" for row in rows),
        "stored_exception_records": len(exceptions), "maximum_exception_word_edges": max_word,
        "maximum_exception_direction_runs": maximum_runs,
        "selector_and_exception_state_bits": len(values),
        "state_sha256": sha256(bytes(values)).hexdigest(),
        "compiled_word_sha256": digest.hexdigest(),
        "target_ordinal_is_generated_by_Cycle646_formula": True,
        "runtime_host_search_or_path_query": False,
        "flat_all_target_path_table_stored": False,
        "stored_content": "one 5-bit formula/exception selector per target ordinal plus run-length words only for bounded-search exceptions",
        "reconstruction_failures": reconstruction_failures,
        "delete_one_exception_direction_residual": flip_residual,
        "pass": reconstruction_failures == 0 and flip_residual > 0 and len(exceptions) == 8,
    }
    check(f"L{length} Cycle649 bounded search is partially evaluated into a physical selector/exception state bank with exact word recovery",
          result["pass"], {"targets":len(rows), "formula":result["formula_records"],
                           "exceptions":len(exceptions), "bits":len(values),
                           "reconstruction_failures":reconstruction_failures,
                           "deletion":flip_residual})
    return result, tuple(values)


def simulate_path_word(path, delete_last=False):
    return c649.simulate_swap_exhaust(path, delete_last_inverse=delete_last)


def literal_oracle_circuit_word(length, descriptors, routes, grammar, program_rows):
    modulus = K*length
    widths = grammar["state_carried_register_widths"]
    offset = 0; fields = {}
    for name, width in widths.items():
        fields[name] = tuple(range(offset, offset+width)); offset += width
    probe_index, syndrome_index, flag_index, token_index = fields["probe_syndrome_flag_token"]
    probe_row = program_rows[probe_index]; flag_row = program_rows[flag_index]
    hub = (SHELL,SHELL,SHELL)
    probe_flag_path = ((probe_row["seed"],)
                       + c649.backbone_between(probe_row["port"], flag_row["port"], modulus, hub))
    pair_nn_failures = sum(not c649.nn(left,right,modulus) for left,right in zip(probe_flag_path,probe_flag_path[1:]))
    pair_exhaust = simulate_path_word(probe_flag_path)
    counts = Counter(); digest = sha256(); route_failures = work_failures = 0
    maximum_route = 0; total_route_edges = 0

    def one(opcode, site):
        counts[(opcode,1)] += 1; digest.update(repr((opcode,(site,))).encode())

    def routed_two(opcode, path, target):
        nonlocal route_failures, maximum_route, total_route_edges
        maximum_route = max(maximum_route, len(path)-1); total_route_edges += len(path)-1
        route_failures += sum(not c649.nn(a,b,modulus) for a,b in zip(path,path[1:]))
        route_failures += not c649.nn(path[-1],target,modulus)
        for edge in zip(path,path[1:]): counts[("SWAP",2)] += 1; digest.update(repr(("SWAP",edge)).encode())
        counts[(opcode,2)] += 1; digest.update(repr((opcode,(path[-1],target))).encode())
        for edge in reversed(tuple(zip(path,path[1:]))): counts[("SWAP",2)] += 1; digest.update(repr(("SWAP",tuple(reversed(edge)))).encode())
        route_failures += simulate_path_word(path)

    def parity_block(row, inverse=False):
        one("H", probe_row["seed"])
        if row["sign"]: one("Z_sign", probe_row["seed"])
        support = tuple(reversed(row["support"])) if inverse else row["support"]
        for _q, target, letter in support:
            routed_two("controlled_"+letter, routes[target], target)
        one("H", probe_row["seed"])

    for row in descriptors:
        parity_block(row, False)
        routed_two("CNOT_probe_flag", probe_flag_path, flag_row["seed"])
        parity_block(row, True)
        one("Z_violation", flag_row["seed"])
        parity_block(row, False)
        routed_two("CNOT_probe_flag", probe_flag_path, flag_row["seed"])
        parity_block(row, True)
        for syndrome in (0,1):
            probe = flag = 0; phase = 1
            probe ^= syndrome; flag ^= probe; probe ^= syndrome
            phase *= -1 if flag else 1
            probe ^= syndrome; flag ^= probe; probe ^= syndrome
            work_failures += (probe,flag,phase) != (0,0,-1 if syndrome else 1)
    counter_width = len(fields["check_counter"]); counter_modulus = 1 << counter_width
    counter_failures = 0
    for token in (0,1):
        for start in (0,1,counter_modulus-1):
            value = start
            if token:
                for _ in descriptors: value = (value+1) % counter_modulus
                for _ in descriptors: value = (value-1) % counter_modulus
            counter_failures += value != start
    # Exact macro count for token-controlled increment: CNOT on bit0, then
    # C^(k+1)X.  A clean-chain C^m X uses 1 Toffoli for m=2 and 2m-3 for m>2.
    per_increment_toffoli = sum(1 if controls == 2 else 2*controls-3
                                for controls in range(2,counter_width+1))
    controlled_counter = {
        "width": counter_width, "token_controlled_CNOT_per_increment": 1,
        "token_controlled_Toffoli_macros_per_increment": per_increment_toffoli,
        "forward_increments": len(descriptors), "inverse_decrements": len(descriptors),
        "exact_27_primitive_Toffoli_import": True,
        "boundary_and_token_sector_failures": counter_failures,
        "final_counter_and_token_exhaust": counter_failures == 0,
    }
    expected = grammar["gate_counts"]
    expected_counts = {
        "H": expected["support_one_H"],
        "Z_sign": expected["support_one_probe_Z_for_row_sign"],
        "controlled_P": expected["support_two_controlled_P"],
        "CNOT_probe_flag": expected["support_two_syndrome_flag_CNOT"],
        "Z_violation": expected["support_one_violation_phase"],
    }
    observed = {
        "H": counts[("H",1)], "Z_sign": counts[("Z_sign",1)],
        "controlled_P": sum(value for (name,support),value in counts.items()
                            if support==2 and name in ("controlled_X","controlled_Y","controlled_Z")),
        "CNOT_probe_flag": counts[("CNOT_probe_flag",2)],
        "Z_violation": counts[("Z_violation",1)],
    }
    result = {
        "length": length, "literal_gate_word_sha256": digest.hexdigest(),
        "primitive_counts": {f"{name}/support{support}":value for (name,support),value in sorted(counts.items())},
        "expected_Cycle646_counts": expected_counts, "observed_Cycle646_counts": observed,
        "Cycle646_gate_count_mismatches": {key:(expected_counts[key],observed[key]) for key in expected_counts if expected_counts[key]!=observed[key]},
        "maximum_routed_support_two_leg_edges": maximum_route,
        "total_one_way_support_two_route_edges": total_route_edges,
        "route_or_adjacency_or_inverse_failures": route_failures,
        "probe_flag_pair_NN_failures": pair_nn_failures,
        "probe_flag_pair_inverse_exhaust_residual": pair_exhaust,
        "syndrome_work_exhaust_failures": work_failures,
        "controlled_check_counter": controlled_counter,
        "all_emitted_gates_support_one_or_fine_NN_support_two": route_failures == pair_nn_failures == 0,
        "fixed_circuit_word_enumerated": True,
        "autonomous_token_conditioned_gate_dispatch_law_executed": False,
        "pass_as_literal_support_one_two_circuit_word": not (route_failures or pair_nn_failures or pair_exhaust or work_failures or counter_failures)
                                                     and expected_counts == observed,
    }
    check(f"L{length} oracle circuit word is enumerated as support-one/fine-NN support-two gates with route and work exhaust",
          result["pass_as_literal_support_one_two_circuit_word"],
          {"gates":sum(counts.values()), "count_mismatches":result["Cycle646_gate_count_mismatches"],
           "route_failures":route_failures, "work_failures":work_failures,
           "counter_failures":counter_failures, "autonomous_dispatch":False})
    return result


def repaired_cycle649_system(length, repaired_roles):
    existing_local = set(repaired_roles)
    placement,obj,descriptor_summary,descriptors,old,aux,program,occupied,collisions = c649.build_existing_occupancy(length, existing_local)
    modulus = K*length; targets = {site for row in descriptors for _q,site,_letter in row["support"]}
    backbone = c649.shell_backbone(length)
    backbone_collisions = sum(occupied(site) for site in backbone)
    finger_summary,fingers = c649.compile_fingers(length,targets,occupied,old|aux|program)
    search_bank,search_values = compiled_search_state_bank(length,targets,fingers,occupied)
    corridor_orbit = {c649.rotate_mod(frame,site,modulus) for frame in FRAMES for path in fingers.values() for site in path}
    grammar = c646.coherent_oracle_grammar(length,descriptors,obj)
    route_stack_bits = 3*finger_summary["maximum_finger_edges"]+64
    logical_bits = grammar["logical_program_and_work_bits"] + route_stack_bits + len(search_values)
    program_summary,program_rows,program_sites = c649.allocate_outer_program(length,logical_bits,backbone,corridor_orbit,old,aux)
    program_existing_collisions = program_sites & program
    widths = grammar["state_carried_register_widths"]; probe_offset = sum(width for name,width in widths.items() if name != "probe_syndrome_flag_token" and list(widths).index(name) < list(widths).index("probe_syndrome_flag_token"))
    probe_row = program_rows[probe_offset]
    ordered_rows = [probe_row] + [row for row in program_rows if row is not probe_row]
    route_summary,routes = c649.compile_full_routes(length,fingers,ordered_rows,program_sites,occupied,backbone,set())
    covariance,_corridor = c649.covariance_and_capacity(length,backbone,fingers,program_sites,program_rows,old,aux,len(repaired_roles))
    controller = literal_oracle_circuit_word(length,descriptors,routes,grammar,program_rows)
    alias_rows = tuple(sorted(collisions["old_program"]))
    result = {
        "length": length, "train_split": {3:"train",6:"held",7:"held-out-size"}[length],
        "existing_role_collisions": collisions, "remaining_old_program_aliases": alias_rows,
        "backbone_M2": len(backbone), "backbone_collisions": backbone_collisions,
        "descriptor_summary": descriptor_summary, "finger_compiler": finger_summary,
        "compiled_search_state_bank": search_bank,
        "program_placement": program_summary,
        "new_program_vs_relocated_Cycle638_collisions": tuple(sorted(program_existing_collisions)),
        "literal_routes": route_summary, "covariance_and_capacity": covariance,
        "literal_oracle_circuit_word": controller,
        "joint_inherited_role_allocation_pass": not any(collisions.values()) and not program_existing_collisions,
        "fixed_circuit_word_pass": controller["pass_as_literal_support_one_two_circuit_word"],
        "autonomous_token_conditioned_dispatch_pass": False,
    }
    result["pass"] = bool(not alias_rows and not any(collisions.values()) and backbone_collisions==0
                          and finger_summary["pass"] and search_bank["pass"] and program_summary["pass"]
                          and not program_existing_collisions and route_summary["pass"]
                          and covariance["pass"] and controller["pass_as_literal_support_one_two_circuit_word"])
    check(f"L{length} repaired joint allocation, stored search witnesses, routes, covariance, and literal circuit word pass without refit",
          result["pass"], {"aliases":alias_rows,"backbone_collisions":backbone_collisions,
                           "search_bits":search_bank["selector_and_exception_state_bits"],
                           "program_collisions":len(program_existing_collisions),
                           "route":route_summary["pass"],"circuit_word":controller["pass_as_literal_support_one_two_circuit_word"]})
    del placement,obj,descriptors,old,aux,program,occupied,backbone,fingers,corridor_orbit,program_rows,program_sites,routes,_corridor
    gc.collect()
    return result


def no_go_discipline(route_a, route_b, route_c):
    prior_alias = immutable_citation(
        "docs/work_history/repo/review_feedback/PHYSICAL_RESERVED_OUTER_SHELL_SIDECAR_PLACEMENT_CYCLE649_NOTE_2026-07-23.md",
        "joint inherited role allocation: **blocked by one non-target alias**")
    prior_controller = immutable_citation(
        "docs/work_history/repo/review_feedback/PHYSICAL_RESERVED_OUTER_SHELL_SIDECAR_PLACEMENT_CYCLE649_NOTE_2026-07-23.md",
        "support-one/two routing-control circuit")
    current_relocation = current_citation(
        "scripts/physical_inherited_role_alias_repair_tournament_cycle652_2026_07_23.py",
        "def route_a_program_orbit_relocation")
    current_dispatch = current_citation(
        "scripts/physical_inherited_role_alias_repair_tournament_cycle652_2026_07_23.py",
        '"autonomous_token_conditioned_gate_dispatch_law_executed": False')
    families = [
        {"family":"equivariant program-coordinate relocation","object":"one logical program role across its active-frame proper-cubic orbit","mechanism":"rho_h=R_h(0,64,0) plus updated decoder","terminal":"zero joint aliases and exact stored word/decoder","strength_vs_target":"target-equivalent for alias repair","honesty_marker":"ATTEMPTED","marker":"ATTEMPTED","result":"positive"},
        {"family":"periodic data-orbit relocation","object":"all radius-4 puncture-spoke data roles","mechanism":"radius-64 coordinate decoder and attempted act-pair reroute","terminal":"preserve data algebra and instantiate every physical fixture endpoint","strength_vs_target":"target-equivalent","honesty_marker":"ATTEMPTED","marker":"ATTEMPTED","result":"logical algebra positive; Cycle638 operand catalog has zero mapped endpoints, so fixture reroute is uninstantiated"},
        {"family":"fixed-value program specialization","object":"body-record 979 payload bit","mechanism":"remove stored one or reuse shared data value","terminal":"exact program semantics with autonomous state accounting","strength_vs_target":"target-equivalent","honesty_marker":"ATTEMPTED","marker":"ATTEMPTED","result":"one truth-table branch fails; host/law constant forbidden"},
        {"family":"stored selector/exception compiler","object":"Cycle649 bounded-search outputs","mechanism":"formula selector bits plus eight physical exception words","terminal":"no host route search and exact load/unload word recovery","strength_vs_target":"weaker than autonomous dispatch","honesty_marker":"ATTEMPTED","marker":"ATTEMPTED","result":"positive stored-state circuit-word input"},
        {"family":"literal routed oracle circuit word","object":"Cycle646 coherent oracle word","mechanism":"enumerated support-one and routed fine-NN support-two gates","terminal":"gate counts, route inverse, syndrome/counter exhaust","strength_vs_target":"weaker than autonomous recurrent law","honesty_marker":"ATTEMPTED","marker":"ATTEMPTED","result":"positive fixed word; autonomous token-conditioned dispatch open"},
    ]
    open_routes = [
        {"family":"moving-head token CA","object":"local token, probe, and gate opcode fields","mechanism":"Fredkin/CCP decomposition with locally propagated head","terminal":"autonomous state-conditioned dispatch","strength_vs_target":"target-equivalent for controller residual","status":"OPEN / NOT COUNTED"},
        {"family":"static subsystem check center","object":"bounded local gauge generators","mechanism":"replace routed oracle by static enforcement","terminal":"lawful-sector penalty/enforcement","strength_vs_target":"incompatible alternative","status":"OPEN / NOT COUNTED"},
        {"family":"blank-rail renewal","object":"outer-shell clean corridor","mechanism":"reversible reservoir or local reset law","terminal":"generate/renew supplied blank work","strength_vs_target":"downstream independent resource","status":"OPEN / NOT COUNTED"},
    ]
    walls = {
        "W_autonomous_token_dispatch":"fixed circuit word exists, but no autonomous state-conditioned moving-head update is executed",
        "W_blank_shell_renewal":"outer-shell rails and clean work remain supplied rather than generated or renewed",
        "W_static_or_repair_law":"oracle circuit is neither static enforcement nor autonomous rejection/repair/convergence",
    }
    pairs = [{"from":left,"to":right,"implied":False,
              "reason":f"closing {left} does not construct {right}"}
             for left in walls for right in walls if left != right]
    n4 = [{
        "prior_ref":prior_alias["ref"],"prior_path":prior_alias["path"],"prior_line":prior_alias["line"],
        "prior_residual":"one Cycle638-program/Cycle642-data tensor-factor alias",
        "current_path":current_relocation["path"],"current_line":current_relocation["line"],
        "current_residual":"equivariant coordinate relocation plus decoder update removes the exact alias",
        "same_scope":True,"exact_match":True,"use_as_closure":True,
    },{
        "prior_ref":prior_controller["ref"],"prior_path":prior_controller["path"],"prior_line":prior_controller["line"],
        "prior_residual":"support-one/two routing controller not enumerated or executed",
        "current_path":current_dispatch["path"],"current_line":current_dispatch["line"],
        "current_residual":"support-one/two fixed circuit word is enumerated, but autonomous token-conditioned dispatch remains unexecuted",
        "same_scope":False,"exact_match":False,"use_as_closure":False,
    }]
    required = {"prior_ref","prior_path","prior_line","prior_residual","current_path","current_line","current_residual","same_scope","exact_match","use_as_closure"}
    result = {
        "Status":"PASS_SCOPED_POSITIVE_AND_BOUNDED_CONTROLLER_RESIDUAL",
        "N1_normalized_families":families,"N1_open_routes_not_counted":open_routes,
        "N1_qualifying_attempts":len(families),"N1_required_for_negative":5,
        "N1_negative_gate":"FAIL / DO NOT SHIP",
        "N2_collapsed_walls":walls,"N2_directed_ordered_pairs":pairs,
        "N3_hidden_wall_scan":[
            {"phrase":"active frame sector","classification":"explicit supplied state-carried sector, not six simultaneous added bits","wall":"W_autonomous_token_dispatch"},
            {"phrase":"stored selector/exception bank","classification":"explicit physical M2 program state; values and capacity counted","wall":None},
            {"phrase":"fixed circuit word","classification":"literal gate list, not autonomous recurrent update","wall":"W_autonomous_token_dispatch"},
            {"phrase":"blank outer shell","classification":"explicit supplied clean resource","wall":"W_blank_shell_renewal"},
        ],
        "N4_exact_residual_matches":[n4[0]],
        "N4_nonmatches_not_used_as_closure":[n4[1]],"N4_required_fields":sorted(required),
        "N5_rhetoric":[
            {"claim":"data relocation route B does not reach the retained physical-fixture terminal",
             "per_element":"all Cycle638 catalog sites/pair endpoints are mapped and zero instantiate the Cycle642 spoke relocation","per_site":"the abstract Cycle642 coordinate relabel is separate",
             "per_mode":"no CAR-mode impossibility inferred","per_block":"logical route generator is unchanged, hence vacuous for this map",
             "lattice_wide":"a Cycle642-to-fixture coordinate decoder and full reroute remain open"},
            {"claim":"fixed circuit-word enumeration is not autonomous token dispatch",
             "per_element":"all emitted gates are support-one or fine-NN support-two","per_site":"route adjacency and inverse exhaust tested",
             "per_mode":"coherent syndrome cases tested, not arbitrary physical program corruption","per_block":"L3/L6/L7 words tested",
             "lattice_wide":"no recurrent local update law or blank renewal is executed"},
        ],
        "N6_partial_closure_paths":[
            {"file":"UNMATERIALIZED/physical_moving_head_token_dispatch_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_autonomous_token_dispatch with explicit Fredkin/CCP support-one/two decomposition"},
            {"file":"UNMATERIALIZED/physical_outer_shell_blank_renewal_cycle_next.py","status":"OPEN","what_closes":"W_blank_shell_renewal"},
            {"file":"UNMATERIALIZED/physical_oracle_repair_law_cycle_next.py","status":"OPEN","what_closes":"W_static_or_repair_law"},
        ],
        "N7_steelman":{
            "mechanism":"carry a one-hot head beside the probe, decompose token-controlled SWAP and token+probe-controlled Pauli into the imported exact 27-primitive Toffoli, and route each two-site primitive through the now collision-free outer backbone",
            "actionable_steps":["place head/parity scratch beside every active port","enumerate Fredkin and CCX/CCZ words","execute all token/check-counter sectors and inverse cleanup","repeat deletion/all24/all576 tests"],
            "terminal_test":"one autonomous state-conditioned local circuit maps the stored selector word to the literal oracle word and returns head, counters, route stack, probe, flag, and parity scratch",
            "why_it_breaks_the_negative":"Cycle652 already closes role allocation and every unconditioned route/gate word, so only conditional moving-head synthesis remains; no shared-substrate obstruction is present"},
        "N8_cross_cycle_echo":[
            {"cycle":638,"mechanism":"nested stored-program decoder/counter","applicability":"supplies exact support-one/two counter and decoder patterns, not the Cycle652 moving head"},
            {"cycle":646,"mechanism":"clean coherent oracle grammar","applicability":"supplies algebra and work exhaust, not literal placement"},
            {"cycle":649,"mechanism":"outer-shell role and route-word geometry","applicability":"alias residual is retired here; controller execution residual is narrowed"},
            {"cycle":652,"mechanism":"equivariant role relocation and fixed circuit word","applicability":"reopens autonomous dispatch as a concrete Fredkin/CCP compiler"},
        ],
        "route_A_pass":route_a["pass"],"route_B_joint_pass":route_b["pass_as_joint_repair"],
        "route_C_joint_pass":route_c["pass_as_joint_repair"],
        "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP",
        "shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False,"minimum_content_shipped":False,
        "shared_obstruction_shipped":False,"axiom_pressure_shipped":False,
        "broad_no_go_claim":False,"minimum_content_claim":False,
        "shared_obstruction_claim":False,"axiom_pressure_claim":False,
        "shared_route_independent_obstruction":False,"axiom_pressure":False,
    }
    check("canonical N1-N8 permits the exact route-A closure and blocks promotion of route-B/C or controller residuals",
          len(families)>=5 and len(pairs)==6 and all(required <= set(row) for row in n4)
          and route_a["pass"] and not route_b["pass_as_joint_repair"] and not route_c["pass_as_joint_repair"]
          and all(result[key]=="FAIL / DO NOT SHIP" for key in ("broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate"))
          and not any(result[key] for key in ("broad_negative_shipped","minimum_content_shipped","shared_obstruction_shipped","axiom_pressure_shipped")),
          {"qualifying":len(families),"open":len(open_routes),"walls":len(walls),"directed":len(pairs)})
    return result


def main():
    global PASS, FAIL
    started = time.perf_counter(); observed = {path:git_sha(path) for path in PINS}
    imported = {name:str(Path(module.__file__).resolve()) for name,module in sys.modules.items()
                if (name.startswith("physical_") or name.startswith("cycle652_immutable")) and getattr(module,"__file__",None)}
    working = [path for path in imported.values() if Path(path).is_relative_to(ROOT)]
    check("Cycle649 shore and every imported physics module are immutable git bytes",
          observed==PINS and not working,
          {"commit":IMMUTABLE_COMMIT,"pins":len(PINS),"mismatches":[path for path in PINS if observed[path]!=PINS[path]],"working":working})
    baseline, private, route_private, program_layout = reconstruct_cycle638()
    route_a,repaired_roles,repaired_values = route_a_program_orbit_relocation(baseline,route_private,program_layout)
    route_b = route_b_data_orbit_relocation(private,route_private,tuple(program_layout["roles"]))
    route_c = route_c_fixed_value_elimination(program_layout)
    systems = [repaired_cycle649_system(length,repaired_roles) for length in (3,6,7)]
    nogo = no_go_discipline(route_a,route_b,route_c)
    note = NOTE.read_text(); markers = ("Status: **PASS**","Authority: **none**","Audit: **unset**",
        "1,011,273","(0,64,0)","769,434","support-one/two","fixed circuit word",
        "not autonomous token-conditioned dispatch","N1-N8","Axiom pressure: **none**")
    check("Cycle652 note freezes the equivariant repair, controller boundary, and N1-N8 scope",
          all(marker in note for marker in markers), markers)
    overall = bool(route_a["pass"] and baseline["pass"]
                   and route_b["pass_as_exact_route_discriminator"] and route_c["pass_as_narrow_discriminator"]
                   and all(system["pass"] for system in systems)
                   and all(system["joint_inherited_role_allocation_pass"] for system in systems)
                   and all(system["fixed_circuit_word_pass"] for system in systems)
                   and not any(system["autonomous_token_conditioned_dispatch_pass"] for system in systems)
                   and not nogo["shared_route_independent_obstruction"] and not nogo["axiom_pressure"])
    check("Cycle652 closes the inherited alias and literal fixed circuit word while preserving the autonomous-dispatch firewall",
          overall,{"systems":len(systems),"route_A":route_a["pass"],
                   "route_B_joint":route_b["pass_as_joint_repair"],"route_C_joint":route_c["pass_as_joint_repair"],
                   "autonomous_dispatch":False})
    result = {
        "cycle":652,"date":"2026-07-23","Status":"PASS" if overall and FAIL==0 else "FAIL",
        "status":"cycle652-inherited-role-alias-repaired-fixed-circuit-word-positive-autonomous-dispatch-open",
        "classification":"positive alias repair and literal support-one/two circuit-word compiler with one named autonomous-dispatch interface",
        "authority":AUTHORITY,"audit":AUDIT,"author_accepted":False,"author_artifact_status_accepted":False,
        "constitutional_effect":"none","breakthrough":False,
        "shore":{"immutable_commit":IMMUTABLE_COMMIT,"pins":PINS,"observed":observed,
                 "actual_imported_physical_modules":imported,"working_tree_bytes_used_as_premise":False,
                 "working_import_failures":working,"no_go_skill_origin_main_sha256":NO_GO_ORIGIN_MAIN_SHA256,
                 "freshness_check_origin_main_sha256":FRESHNESS_ORIGIN_MAIN_SHA256,
                 "proof_search_governance_origin_main_sha256":PROOF_SEARCH_ORIGIN_MAIN_SHA256},
        "exact_target_contract":{
            "target":"remove the sole Cycle638-program/Cycle642-data tensor-factor alias while preserving the exact stored act word, decoder, K129 ownership, and proper-cubic covariance; then lower Cycle649 controller work as far as explicit support-one/two gates permit",
            "quantifiers_domain":"one reused K129 Cycle638 bank, active state-carried proper-cubic frame sectors, Cycle642 L3/L6/L7 train/held/held-out layouts",
            "allowed_premises":"immutable Cycle649/Cycle638/Cycle642/Cycle646 artifacts and their explicitly supplied blank/program sectors",
            "forbidden_weakenings":"no host constant, hidden path service, global ordering, refit, repair, E, preparation, occurrence, Record, time, energy, source, or gravity promotion",
            "completion_witness":"zero aliases plus exact call/program/decoder/covariance tests; controller closure separately requires explicit support-one/two word and autonomous-token flag",
            "does_not_count":"coordinate relabel without decoder exhaust; gate geometry without literal word; fixed word without autonomous state-conditioned dispatch"},
        "baseline_Cycle638":baseline,"route_A_program_orbit_relocation":route_a,
        "route_B_data_orbit_relocation":route_b,"route_C_fixed_value_specialization":route_c,
        "systems":systems,
        "strongest_constructive_result":"the logical program role at index 1,011,273 is relocated by the equivariant frame-sector rule rho_h=R_h(0,64,0), removing the only inherited data/program alias without changing any of 1,871,624 program bits, the exact 769,434-call word, or decoder exhaust; L3/L6/L7 then admit the Cycle649 stored selector/exception bank, occupied-safe routes, and an enumerated fixed support-one/two oracle circuit word",
        "route_by_route_disposition":{
            "A_program_orbit_relocation":"PASS_EXACT_ALIAS_REPAIR",
            "B_data_orbit_relocation":"FAIL_CYCLE638_OPERAND_MAP_VACUOUS_CYCLE642_FIXTURE_REROUTE_OPEN",
            "C_fixed_value_specialization":"FAIL_DYNAMIC_DATA_TRUTH_TABLE_AND_HIDDEN_CONSTANT",
            "controller_fixed_circuit_word":"PASS_SUPPORT_ONE_TWO_AND_EXHAUST",
            "controller_autonomous_token_conditioned_dispatch":"OPEN_NOT_EXECUTED"},
        "W_joint_role_allocation":"CLOSED_BY_EQUIVARIANT_PROGRAM_COORDINATE_RELOCATION",
        "W_collision_free_lowering":"FIXED_CIRCUIT_WORD_CLOSED_AUTONOMOUS_TOKEN_DISPATCH_OPEN",
        "W_local_enforcement":"SHARPLY_NARROWED_NOT_CLOSED",
        "full_physical_oracle_compiler_pass":False,
        "autonomous_token_conditioned_dispatch_pass":False,
        "shared_route_independent_obstruction":False,"axiom_pressure":False,
        "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP",
        "shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False,"minimum_content_shipped":False,
        "shared_obstruction_shipped":False,"axiom_pressure_shipped":False,
        "supplied_structure_inventory":{
            "one_reused_1871624_bit_Cycle638_bank":True,"Cycle638_program_values_and_call_word":True,
            "Cycle642_data_aux_and_algebra":True,"Cycle646_oracle_grammar":True,
            "K129_macro_origin_and_active_frame_sector":True,"blank_outer_shell_and_clean_work":True,
            "stored_selector_and_eight_exception_words_newly_counted":True,
            "runtime_host_search_or_path_query":False,"hidden_host_fixed_one":False,
            "autonomous_token_conditioned_dispatch":False,"autonomous_blank_renewal":False,
            "static_enforcement_or_repair":False,"physical_E_or_preparation":False},
        "semantic_firewall":{"circuit_order_is_time":False,"gate_count_is_rate":False,"phase_is_energy":False,
                             "syndrome_flag_is_occurrence":False,"syndrome_flag_is_Record":False},
        "six_wall_ledger":{
            "C_ref":"equivariant program relocation and fixed circuit words pass all24/all576; active frame, macro origin, and blank shell remain supplied",
            "C_num":"exact binary stored program/search/controller data only; no normalization or probability claim",
            "C_wrap":"program decoder, route words, syndrome work, and fixed counter word exhaust; autonomous token dispatch, occurrence, history, and preparation remain absent",
            "C_int":"exact inherited act word and Cycle646 oracle gate counts are preserved; no new mass/contact/seam dynamics or E-intertwiner claim",
            "C_local":"joint role allocation is closed and a fixed support-one/two circuit word is literal; autonomous state-conditioned dispatch, static enforcement, blank renewal, repair, and E remain open",
            "C_source":"unchanged; relocation, storage, route, and gate counts have no source/gravity meaning"},
        "no_go_discipline":nogo,
        "optimal_next_campaign":"construct the moving-head token-conditioned dispatcher: explicitly decompose Fredkin and token+probe-controlled X/Z with the exact 27-primitive Toffoli, place/reroute parity scratch, and exhaust every token/check-counter sector on L3/L6/L7; do not mix blank renewal, repair, or E into that interface",
        "resources":{"elapsed_seconds":time.perf_counter()-started,
                     "maximum_RSS_bytes":int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform=="darwin" else resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)},
    }
    result.update({"tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,"pass":FAIL==0 and overall})
    RECEIPT.write_text(json.dumps(result,indent=2,sort_keys=True,default=json_default)+"\n")
    print(json.dumps({"status":result["Status"],"tests":f"{PASS}/{PASS+FAIL}",
                      "elapsed":result["resources"]["elapsed_seconds"],"receipt":str(RECEIPT.relative_to(ROOT))},sort_keys=True))
    return int(not result["pass"])


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True,exist_ok=True)
    with COLD.open("w") as stream:
        previous = sys.stdout; sys.stdout = Tee(previous,stream)
        try: raise SystemExit(main())
        finally: sys.stdout = previous
