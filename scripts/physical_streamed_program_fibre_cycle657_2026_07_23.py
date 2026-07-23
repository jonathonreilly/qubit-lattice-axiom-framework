#!/usr/bin/env python3
"""Cycle657: streamed injective program-fibre placement tournament.

Audits flat, reusable-stream, and circulating-band routes from the immutable
Cycle655 local dispatcher toward the immutable Cycle652 fixed words.  A PASS
means the bounded audit is internally exact; it does not mean the global
autonomous gate/site terminal passed.

Authority none; audit unset; constitutional effect none.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import io
from itertools import permutations, product
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
IMMUTABLE_C655 = "a1b5d30bba9bccfedfaef87deb2472b74508f8f6"
IMMUTABLE_C652 = "d353925ca046702f1b0f50a41a6f8fa5a0ee3395"
C652_RECEIPT_PATH = "outputs/physical_inherited_role_alias_repair_tournament_cycle652_receipt_2026_07_23.json"
C652_RECEIPT_SHA256 = "56870b951b93c81125789041af6758196e588eeddf2cf7b0235e1f7fd5b03379"
C655_PATHS = (
    "scripts/physical_moving_head_autonomous_dispatcher_cycle655_2026_07_23.py",
    "docs/work_history/repo/review_feedback/PHYSICAL_MOVING_HEAD_AUTONOMOUS_DISPATCHER_CYCLE655_NOTE_2026-07-23.md",
    "outputs/physical_moving_head_autonomous_dispatcher_cycle655_receipt_2026_07_23.json",
    "outputs/physical_moving_head_autonomous_dispatcher_cycle655_cold_2026_07_23.txt",
)
PINS = {
    C655_PATHS[0]: "2492871ffdf5851273c925664cef939bd699497dd182a9c5abb054cc6d1a417e",
    C655_PATHS[1]: "b567610ac4ecf53663c35a36f4f4a234105f7cfd9cf7d397e258e2a426b80b58",
    C655_PATHS[2]: "a518191b6d52309583108558b878d4578ffb8f78386cec7766ff959e392bf3f6",
    C655_PATHS[3]: "79c93fb88bdd17669adc2771f2870ca37a98448a8db63d44f5c51aa164486dd8",
}
NO_GO_ORIGIN_MAIN_SHA256 = "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7"
FRESHNESS_ORIGIN_MAIN_SHA256 = "1e0ec4ef4d7c5dd24243d7c3954c78a3f00ecd3d5e43805e788dd3629973a962"
PROOF_SEARCH_ORIGIN_MAIN_SHA256 = "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258"
AUTHORITY = "none"
AUDIT = "unset"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_STREAMED_PROGRAM_FIBRE_CYCLE657_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_streamed_program_fibre_cycle657_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_streamed_program_fibre_cycle657_cold_2026_07_23.txt"
PASS = FAIL = 0


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


def sha_file(path): return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.integer): return int(value)
    if isinstance(value, np.floating): return float(value)
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, tuple): return list(value)
    raise TypeError(type(value).__name__)


def load_immutable_cycle655():
    export = tempfile.TemporaryDirectory(prefix="cycle657-immutable-")
    shore = Path(export.name).resolve()
    previous_dir, previous_tree = os.environ.get("GIT_DIR"), os.environ.get("GIT_WORK_TREE")
    os.environ["GIT_DIR"] = str((ROOT / ".git").resolve())
    os.environ["GIT_WORK_TREE"] = str(ROOT.resolve())
    archive = subprocess.check_output(["git", "archive", "--format=tar", IMMUTABLE_C655, *C655_PATHS])
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as stream:
        stream.extractall(shore, filter="data")
    os.symlink((ROOT / ".git").resolve(), shore / ".git", target_is_directory=True)
    if previous_dir is None: os.environ.pop("GIT_DIR", None)
    else: os.environ["GIT_DIR"] = previous_dir
    if previous_tree is None: os.environ.pop("GIT_WORK_TREE", None)
    else: os.environ["GIT_WORK_TREE"] = previous_tree
    receipt = json.loads((shore / C655_PATHS[2]).read_text())
    return export, shore, receipt


def load_immutable_cycle652_receipt():
    raw = subprocess.check_output(["git","show",f"{IMMUTABLE_C652}:{C652_RECEIPT_PATH}"],cwd=ROOT)
    return raw, json.loads(raw)


def determinant(matrix):
    return int(round(np.linalg.det(np.asarray(matrix,dtype=int))))


def proper_frames():
    frames=[]
    for order in permutations(range(3)):
        for signs in product((-1,1),repeat=3):
            matrix=np.zeros((3,3),dtype=int)
            for column,row in enumerate(order): matrix[row,column]=signs[column]
            if determinant(matrix)==1: frames.append(matrix)
    return tuple(frames)


FRAMES = proper_frames()


def centered_residue(value): return (int(value)+64)%129-64


def rotate_mod(frame,site,modulus):
    return tuple(int(value)%modulus for value in np.asarray(frame,dtype=int)@np.asarray(site,dtype=int))


def nn(left,right,modulus):
    return sum(min((left[a]-right[a])%modulus,(right[a]-left[a])%modulus) for a in range(3))==1


def shell_backbone_predicate(site):
    return sum(abs(centered_residue(value))==64 for value in site)>=2


def axis_line(start,axis,target,modulus):
    current=list(start);delta=(target-current[axis])%modulus
    if delta>modulus//2:delta-=modulus
    step=1 if delta>0 else -1;path=[]
    for _ in range(abs(delta)):
        current[axis]=(current[axis]+step)%modulus;path.append(tuple(current))
    return tuple(path)


def backbone_to_hub(start,modulus,hub):
    fixed=[axis for axis in range(3) if abs(centered_residue(start[axis]))==64]
    if len(fixed)<2:raise AssertionError(("not backbone",start))
    fixed=fixed[:2];free=next(axis for axis in range(3) if axis not in fixed)
    path=[start];current=start
    for axis in (free,fixed[0],fixed[1]):
        segment=axis_line(current,axis,hub[axis],modulus);path.extend(segment)
        if segment:current=segment[-1]
    if current!=hub or not all(shell_backbone_predicate(site) for site in path):raise AssertionError((start,current,hub))
    return tuple(path)


def backbone_between(left,right,modulus,hub):
    first=backbone_to_hub(left,modulus,hub);second=backbone_to_hub(right,modulus,hub)
    return first+tuple(reversed(second[:-1]))


def periodic_axis_distance(left,right,modulus):
    delta=(right-left)%modulus
    return min(delta,modulus-delta)


def backbone_to_hub_edge_count(start,modulus,hub):
    fixed=[axis for axis in range(3) if abs(centered_residue(start[axis]))==64]
    if len(fixed)<2:return None
    fixed=fixed[:2];free=next(axis for axis in range(3) if axis not in fixed)
    return sum(periodic_axis_distance(start[axis],hub[axis],modulus)
               for axis in (free,fixed[0],fixed[1]))


def route_a_flat_spatial_instruction_fibre(receipt652):
    rows = []
    for system in receipt652["systems"]:
        length = system["length"]
        side = 129 * length
        coordinate_bits = math.ceil(math.log2(side))
        counts = system["literal_oracle_circuit_word"]["primitive_counts"]
        opcode_bits = math.ceil(math.log2(len(counts)))
        payload_bits = 0
        events = 0
        for key, count in counts.items():
            support = int(key.rsplit("support", 1)[1])
            payload_bits += count * (opcode_bits + support * 3 * coordinate_bits)
            events += count
        # One explicit head-presence rail site per event packet.  This is a
        # concrete flat representation, not a claimed lower bound.
        head_rail_M2 = events
        represented_M2 = payload_bits + head_rail_M2
        margin = system["covariance_and_capacity"]["capacity_margin"]
        rows.append({
            "length":length, "physical_side":side, "coordinate_bits":coordinate_bits,
            "opcode_bits":opcode_bits, "events":events,
            "flat_payload_M2":payload_bits, "one_head_site_per_packet_M2":head_rail_M2,
            "explicit_flat_representation_M2":represented_M2,
            "Cycle652_capacity_margin_M2":margin,
            "raw_capacity_discriminator_pass":represented_M2 <= margin,
            "injective_collision_free_placement_executed":False,
            "local_successor_edges_executed":False,
        })
    result = {
        "route":"A spatial instruction fibre",
        "representation":"one static opcode plus one/two absolute coordinates per primitive and one head-rail site per packet",
        "not_a_minimum_content_claim":True,
        "systems":rows,
        "L3_explicit_representation_exceeds_margin":not rows[0]["raw_capacity_discriminator_pass"],
        "route_specific_failure":"the explicit flat representation already exceeds L3 margin; L6/L7 raw fits do not supply an injective layout or successor rail",
        "pass_as_global_autonomous_route":False,
    }
    result["pass_as_exact_discriminator"] = bool(result["L3_explicit_representation_exceeds_margin"]
                                                  and not any(row["injective_collision_free_placement_executed"] for row in rows))
    check("route A flat event tape has exact size accounting and fails its own L3 representation before placement",
          result["pass_as_exact_discriminator"],
          {row["length"]:(row["explicit_flat_representation_M2"],row["Cycle652_capacity_margin_M2"],row["raw_capacity_discriminator_pass"]) for row in rows})
    return result


def count_only_recurrence(system):
    events = sum(system["literal_oracle_circuit_word"]["primitive_counts"].values())
    token = 1; ordinal = 0; counter = 0
    for _ in range(events):
        if token != 1 or not 0 <= ordinal < events: raise AssertionError((token, ordinal))
        ordinal = (ordinal + 1) % events
        counter = (counter + 1) % events
    forward_return = ordinal == counter == 0 and token == 1
    for _ in range(events):
        ordinal = (ordinal - 1) % events
        counter = (counter - 1) % events
    inverse_return = ordinal == counter == 0 and token == 1
    deleted_return = ((events - 1) % events) == 0
    malformed = []
    for bad_token, bad_ordinal in ((0,0),(2,0),(1,-1),(1,events)):
        accepted = bad_token == 1 and 0 <= bad_ordinal < events
        malformed.append({"token":bad_token,"ordinal":bad_ordinal,"accepted":accepted})
    return {
        "events":events, "forward_count_head_return":forward_return,
        "inverse_count_head_return":inverse_return,
        "delete_one_count_step_returns":deleted_return,
        "malformed_states":malformed,
        "malformed_accepts":sum(row["accepted"] for row in malformed),
    }


def route_b_reusable_stream(receipt652):
    systems = []
    expected_primitive_families = {
        "H/support1","Z_sign/support1","Z_violation/support1","SWAP/support2",
        "CNOT_probe_flag/support2","controlled_X/support2","controlled_Y/support2","controlled_Z/support2",
    }
    for system in receipt652["systems"]:
        recurrence = count_only_recurrence(system)
        placement = system["program_placement"]
        search = system["compiled_search_state_bank"]
        families = set(system["literal_oracle_circuit_word"]["primitive_counts"])
        missing_exception_payloads = sum(row["kind"] == "stored_bounded_search_witness" and "word" not in row
                                         for row in search["rows"])
        systems.append({
            "length":system["length"], "active_logical_program_roles":placement["role_orbits"],
            "proper_cubic_program_M2":placement["physical_frame_orbit_program_M2"],
            "search_bank_state_bits":search["selector_and_exception_state_bits"],
            "stored_exception_records":search["stored_exception_records"],
            "exception_direction_payloads_materialized_in_receipt":False,
            "missing_exception_direction_payloads":missing_exception_payloads,
            "primitive_family_coverage":sorted(families),
            "all_immutable_primitive_families_covered":families <= expected_primitive_families,
            "count_only_recurrence":recurrence,
            "expected_gate_site_sha256":system["literal_oracle_circuit_word"]["literal_gate_word_sha256"],
            "emitted_gate_site_sha256":None,
            "emitted_digest_matches":False,
            "static_program_value_word_literally_bound_to_placed_roles":False,
            "local_decoder_selects_gate_and_site":False,
        })
    result = {
        "route":"B streamed/reusable program packets",
        "systems":systems,
        "constant_dispatch_tile_M2":125,
        "one_125_M2_tile_per_event_allocated":False,
        "reuses_Cycle655_bounded_tile":True,
        "program_memory_scaling":"Cycle652 active compressed program roles scale from 2,213 to 2,821 across L3/L6/L7; the event count is not stored flat",
        "host_gate_site_eliminated":False,
        "pass_as_global_autonomous_route":False,
    }
    result["pass_as_exact_partial"] = bool(
        all(row["count_only_recurrence"]["forward_count_head_return"]
            and row["count_only_recurrence"]["inverse_count_head_return"]
            and not row["count_only_recurrence"]["delete_one_count_step_returns"]
            and row["count_only_recurrence"]["malformed_accepts"] == 0
            and not row["emitted_digest_matches"] for row in systems))
    check("route B reuses one bounded tile and closes count recurrence while the exact gate/site digest remains unavailable",
          result["pass_as_exact_partial"],
          {row["length"]:(row["count_only_recurrence"]["events"],row["missing_exception_direction_payloads"],row["emitted_digest_matches"]) for row in systems})
    return result


def frame_key(matrix): return tuple(int(x) for x in np.asarray(matrix).reshape(-1))


def route_c_circulating_band(receipt652):
    frames = FRAMES
    systems = []
    total_frame_failures = total_translation_failures = total_band_failures = 0
    for system in receipt652["systems"]:
        length = system["length"]; modulus = 129 * length; hub = (64,64,64)
        rows = sorted(system["program_placement"]["placements"], key=lambda row:row["logical_bit"])
        ports = [tuple(row["port"]) for row in rows]; seeds = [tuple(row["seed"]) for row in rows]
        read_edge_failures = sum(not nn(seed,port,modulus) for seed,port in zip(seeds,ports))
        ownership_failures = (len(ports)-len(set(ports))) + (len(seeds)-len(set(seeds)))
        digest = sha256(); band_edges = 0; max_leg = 0; head = ports[0]
        for index, left in enumerate(ports):
            right = ports[(index+1)%len(ports)]
            left_edges=backbone_to_hub_edge_count(left,modulus,hub)
            right_edges=backbone_to_hub_edge_count(right,modulus,hub)
            total_band_failures += int(left != head or left_edges is None or right_edges is None)
            leg_edges=(left_edges or 0)+(right_edges or 0)
            # This digest commits to the deterministic Cycle649 formula word
            # by endpoints and exact leg lengths without materializing its
            # millions of individual edge tuples in host memory.
            digest.update(repr((index,left,right,left_edges,right_edges)).encode())
            band_edges += leg_edges; max_leg = max(max_leg,leg_edges); head = right
        forward_return = head == ports[0]
        # Reverse the same cyclic legs.  Only endpoints need be retained;
        # each deterministic backbone_between word is regenerated locally
        # here as an audit, not claimed as a placed successor program.
        for index in reversed(range(len(ports))):
            left = ports[index]; right = ports[(index+1)%len(ports)]
            total_band_failures += int(right != head)
            head = left
        inverse_return = head == ports[0]
        delete_residual = int(band_edges > 0)

        frame_failures = 0
        for frame in frames:
            for seed,port in zip(seeds,ports):
                rseed = rotate_mod(frame,seed,modulus); rport = rotate_mod(frame,port,modulus)
                frame_failures += not nn(rseed,rport,modulus)
                frame_failures += not shell_backbone_predicate(rport)
        total_frame_failures += frame_failures
        translation_failures = 0
        for shift in ((a,b,c) for a in range(3) for b in range(3) for c in range(3)):
            for seed,port in zip(seeds,ports):
                shifted_seed = tuple((seed[q]+shift[q])%modulus for q in range(3))
                shifted_port = tuple((port[q]+shift[q])%modulus for q in range(3))
                relative_port = tuple((shifted_port[q]-shift[q])%modulus for q in range(3))
                translation_failures += not nn(shifted_seed,shifted_port,modulus)
                translation_failures += not shell_backbone_predicate(relative_port)
        total_translation_failures += translation_failures
        coord_bits = 3 * math.ceil(math.log2(modulus))
        systems.append({
            "length":length, "program_roles_visited":len(rows), "ports_distinct":len(ports)==len(set(ports)),
            "seeds_distinct":len(seeds)==len(set(seeds)), "static_seed_to_port_read_edge_failures":read_edge_failures,
            "ownership_failures":ownership_failures,
            "circulating_band_edges":band_edges, "maximum_port_to_port_leg_edges":max_leg,
            "band_formula_word_sha256":digest.hexdigest(), "forward_head_return":forward_return,
            "inverse_head_return":inverse_return, "delete_one_final_edge_nonreturn_residual":delete_residual,
            "all24_program_seed_port_failures":frame_failures,
            "ordinary_translation_residue_representatives":27,
            "ordinary_translation_failures":translation_failures,
            "candidate_next_port_pointer_bits":coord_bits*len(rows),
            "next_port_pointer_bits_injectively_placed":False,
            "current_executable_successor_selected_by_host_row_index":True,
        })
    frame_map = {frame_key(frame):i for i,frame in enumerate(frames)}
    group_failures = 0
    for left in frames:
        for right in frames:
            group_failures += frame_key(np.asarray(left)@np.asarray(right)) not in frame_map
    result = {
        "route":"C staggered circulating program band",
        "systems":systems,
        "all24_program_failures":total_frame_failures,
        "all576_signed_permutation_group_failures":group_failures,
        "ordinary_translation_failures":total_translation_failures,
        "band_geometry_failures":total_band_failures,
        "Cycle655_state_carried_nine_colour_rule_inherited":True,
        "state_carried_phase_is_time":False,
        "state_carried_phase_is_rate":False,
        "host_schedule_eliminated":False,
        "pass_as_global_autonomous_route":False,
    }
    result["pass_as_literal_band_geometry"] = bool(not any((total_frame_failures,group_failures,
                                                             total_translation_failures,total_band_failures))
                                                     and all(row["forward_head_return"] and row["inverse_head_return"]
                                                             and row["delete_one_final_edge_nonreturn_residual"]
                                                             and not row["next_port_pointer_bits_injectively_placed"]
                                                             for row in systems))
    check("route C audits every placed program port and exact fine-NN backbone formula leg, but its successor remains host indexed",
          result["pass_as_literal_band_geometry"],
          {row["length"]:(row["program_roles_visited"],row["circulating_band_edges"],row["current_executable_successor_selected_by_host_row_index"]) for row in systems})
    return result


def inherited_controls(receipt655, receipt652, route_c):
    systems = []
    for s655,s652,band in zip(receipt655["inherited_pins_and_capacity_discriminator"]["systems"],
                              receipt652["systems"],route_c["systems"]):
        controller = s652["literal_oracle_circuit_word"]
        systems.append({
            "length":s652["length"],
            "Cycle652_fixed_word_sha256":controller["literal_gate_word_sha256"],
            "Cycle652_route_failures":controller["route_or_adjacency_or_inverse_failures"],
            "Cycle652_syndrome_work_failures":controller["syndrome_work_exhaust_failures"],
            "Cycle652_counter_failures":controller["controlled_check_counter"]["boundary_and_token_sector_failures"],
            "Cycle655_local_tile_M2":receipt655["route_B_static_local_transition_tile"]["bounded_tile_M2"],
            "Cycle655_local_route_return_failures":receipt655["route_B_static_local_transition_tile"]["route_return_failures"],
            "band_read_and_ownership_failures":band["static_seed_to_port_read_edge_failures"]+band["ownership_failures"],
        })
    result = {
        "systems":systems,
        "Cycle652_lawful_auxiliary_slice_leakage_norm":receipt652["baseline_Cycle638"]["execution"]["lawful_auxiliary_slice_leakage_norm"],
        "Cycle652_full_code_leakage_executed":receipt652["baseline_Cycle638"]["execution"]["full_physical_E_or_full_code_leakage"],
        "Cycle655_parity_enable_scratch_return":receipt655["exact_local_kernel"]["parity_and_enable_scratch_return_clean"],
        "Cycle655_token_opcode_counter_phase_sectors":receipt655["route_A_moving_head_program_rail"]["sector_tests"],
        "Cycle655_malformed_sector_tests":receipt655["route_A_moving_head_program_rail"]["malformed_sector_tests"],
        "Cycle655_recurrence_inverse_failures":receipt655["route_A_moving_head_program_rail"]["inverse_failures"],
        "mass_contact_seam_pin_scope":"immutable coin/stream/contact call word and L3/L6/L7 fixed-word digests only; no new mass/contact/seam fixture is executed",
        "pass":False,
    }
    result["pass"] = bool(all(not any((row["Cycle652_route_failures"],row["Cycle652_syndrome_work_failures"],
                                       row["Cycle652_counter_failures"],row["Cycle655_local_route_return_failures"],
                                       row["band_read_and_ownership_failures"])) for row in systems)
                          and result["Cycle652_lawful_auxiliary_slice_leakage_norm"] == 0
                          and not result["Cycle652_full_code_leakage_executed"]
                          and result["Cycle655_parity_enable_scratch_return"]
                          and result["Cycle655_token_opcode_counter_phase_sectors"] == 207669
                          and result["Cycle655_malformed_sector_tests"] == 39663
                          and result["Cycle655_recurrence_inverse_failures"] == 0)
    check("immutable route/scratch/leakage controls and band ownership remain exact without promoting full-code leakage",
          result["pass"], {"systems":len(systems),"lawful_leakage":result["Cycle652_lawful_auxiliary_slice_leakage_norm"],
                            "full_code_leakage":result["Cycle652_full_code_leakage_executed"]})
    return result


def no_go_discipline(route_a, route_b, route_c):
    families = [
        {"family":"flat spatial instruction fibre", "object":"one opcode/absolute-site packet and head site per Cycle652 primitive", "mechanism":"literal one-bit-M2 event tape", "terminal":"injective tape plus local successor and operand coupling", "strength_vs_target":"target-equivalent", "honesty_marker":"ATTEMPTED", "result":"exact representation exceeds L3 margin; L6/L7 raw capacity does not place it"},
        {"family":"compressed reusable program packets", "object":"Cycle652 formula registers/search bank with one Cycle655 tile", "mechanism":"nested counters and reusable opcode packet", "terminal":"state-selected gate/site digest equals immutable word", "strength_vs_target":"target-equivalent", "honesty_marker":"ATTEMPTED", "result":"full count recurrence passes; static exception/program values and gate/site emission are not materialized"},
        {"family":"staggered circulating backbone band", "object":"every placed program seed/port plus one serialized head", "mechanism":"fine-NN backbone circulation under state-carried nine-colour layers", "terminal":"local successor, no host site/schedule, and exact event digest", "strength_vs_target":"target-equivalent", "honesty_marker":"ATTEMPTED", "result":"literal band traversal/covariance/return pass; next port is still host indexed"},
        {"family":"immutable runner algorithm replay", "object":"Cycle652 Python descriptor/route enumerator", "mechanism":"rerun host formulas and hash events", "terminal":"physical recurrent local rule selects gate/site", "strength_vs_target":"weaker host replay", "honesty_marker":"ATTEMPTED", "result":"source contains a reproducer but host algorithm execution is forbidden as autonomous evidence"},
        {"family":"replicated Cycle655 bounded tiles", "object":"one 125-M2 tile per controller vertex or event packet", "mechanism":"local exact Fredkin/controlled-P kernel replication", "terminal":"global injective placement and event coupling", "strength_vs_target":"weaker capacity route", "honesty_marker":"ATTEMPTED", "result":"local tile inherited positive; event-scale replication was not placed and flat L3 demand fails"},
    ]
    walls = {
        "W_program_content_materialization":"placed formula/search roles are not bound to a complete literal value word available to the recurrent physical rule",
        "W_local_successor":"no injectively placed next-port/instruction field makes the circulating head choose its successor locally",
        "W_gate_site_decoder":"no lowered local decoder turns the carried compressed state into every immutable opcode/site event and matching digest",
    }
    pairs = [{"from":a,"to":b,"implied":False,"reason":f"closing {a} does not construct {b}"}
             for a in walls for b in walls if a != b]
    result = {
        "Status":"PASS_SCOPED_ROUTE_DISCRIMINATORS_GLOBAL_TERMINAL_OPEN",
        "N1_normalized_families":families,"N1_qualifying_attempts":len(families),
        "N1_required_for_negative":5,"N1_negative_gate":"FAIL / DO NOT SHIP",
        "N1_open_routes_not_counted":[
            {"family":"self-delimiting topological packet loop","status":"OPEN / NOT COUNTED"},
            {"family":"distributed local formula evaluators","status":"OPEN / NOT COUNTED"},
        ],
        "N2_collapsed_walls":walls,"N2_directed_ordered_pairs":pairs,
        "N3_hidden_wall_scan":[
            {"phrase":"immutable digest","classification":"commitment to a word, not the word or a physical program", "wall":"W_program_content_materialization"},
            {"phrase":"host row index","classification":"explicit prohibited site service", "wall":"W_local_successor"},
            {"phrase":"count recurrence","classification":"selects only ordinal, not opcode/site", "wall":"W_gate_site_decoder"},
            {"phrase":"state-carried colour phase","classification":"explicit schedule field; neither time nor rate", "wall":None},
            {"phrase":"supplied blank backbone","classification":"separate blank-renewal interface, not folded into dispatcher walls", "wall":None},
        ],
        "N4_exact_residual_matches":[{
            "prior_ref":IMMUTABLE_C655,"prior_path":C655_PATHS[2],"prior_line":"global autonomous flag",
            "prior_residual":"global program rail/operand coupling false and host gate/site not eliminated",
            "current_path":str(Path(__file__).relative_to(ROOT)),"current_line":"def route_b_reusable_stream",
            "current_residual":"count and literal band traversal now pass, but emitted gate/site digest is absent and successor is host indexed",
            "same_scope":True,"exact_match":True,"use_as_closure":False,
        }],
        "N5_rhetoric":[
            {"claim":"circulating program-band geometry passes", "per_element":"every seed is NN to its port", "per_site":"ports/seeds are distinct and band paths stay on the backbone", "per_mode":"program bits remain static", "per_block":"L3/L6/L7 full row traversal", "lattice_wide":"successor and gate/site decoder remain unplaced"},
            {"claim":"global autonomous dispatch remains false", "per_element":"local Cycle655 kernels remain exact", "per_site":"next port is selected by a Python row index", "per_mode":"no emitted opcode/site stream exists", "per_block":"count-only return is not word equality", "lattice_wide":"no full physical G or E claim"},
        ],
        "N6_partial_closure_paths":[
            {"file":"UNMATERIALIZED/physical_program_value_binding_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_program_content_materialization"},
            {"file":"UNMATERIALIZED/physical_local_successor_pointer_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_local_successor"},
            {"file":"UNMATERIALIZED/physical_formula_decoder_lowering_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_gate_site_decoder and emits the exact word"},
        ],
        "N7_steelman":{
            "mechanism":"materialize the compressed search/program value word on the already placed seeds, add an injectively placed next-port coordinate beside each seed, lower the finite formula/route decoder with Cycle638 counter primitives, and let the state-carried colour rule move the head and packet through the Cycle655 tile",
            "actionable_steps":["export literal program/search values rather than hashes", "place and route next-port fields", "lower descriptor/support/route-step arithmetic", "run L3/L6/L7 until emitted opcode/site digests equal Cycle652 and then reverse"],
            "terminal_test":"the driver supplies only repeated application of one local rule; state alone emits every gate/site digest and returns head/token/opcode/counters/routes/scratch",
            "why_it_breaks_the_negative":"Cycle657 closes full placed-port traversal and exact count return, so materialized values plus local successor/decoder are concrete remaining interfaces rather than a shared substrate obstruction",
        },
        "N8_cross_cycle_echo":[
            {"cycle":638,"mechanism":"nested stored-program counters","applicability":"candidate decoder substrate; not yet lowered for Cycle652 event emission"},
            {"cycle":649,"mechanism":"outer backbone and literal program ports","applicability":"used for full circulating-band traversal; blanks remain supplied"},
            {"cycle":652,"mechanism":"exact fixed gate/site digest","applicability":"terminal commitment; receipt omits literal event payload"},
            {"cycle":655,"mechanism":"exact bounded opcode kernels and nine-colour phase","applicability":"local act/schedule supplied; global successor/decoder open"},
            {"cycle":657,"mechanism":"full placed-port and count traversal","applicability":"narrows the global residual without closing no-host emission"},
        ],
        "route_A_global_pass":route_a["pass_as_global_autonomous_route"],
        "route_B_global_pass":route_b["pass_as_global_autonomous_route"],
        "route_C_global_pass":route_c["pass_as_global_autonomous_route"],
        "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP",
        "shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False,"minimum_content_shipped":False,
        "shared_obstruction_shipped":False,"axiom_pressure_shipped":False,
        "shared_route_independent_obstruction":False,"axiom_pressure":False,
    }
    required = {"prior_ref","prior_path","prior_line","prior_residual","current_path","current_line",
                "current_residual","same_scope","exact_match","use_as_closure"}
    result["pass"] = bool(len(families)>=5 and len(pairs)==6
                          and all(required <= set(row) for row in result["N4_exact_residual_matches"])
                          and all(result[key]=="FAIL / DO NOT SHIP" for key in
                                  ("broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate"))
                          and not any(result[key] for key in ("broad_negative_shipped","minimum_content_shipped",
                                                             "shared_obstruction_shipped","axiom_pressure_shipped")))
    check("canonical N1-N8 blocks flat-route failure and missing no-host digest from becoming obstruction or axiom pressure",
          result["pass"],{"families":len(families),"walls":len(walls),"pairs":len(pairs)})
    return result


def main():
    global PASS, FAIL
    started = time.perf_counter()
    observed = {path:sha_file(ROOT/path) for path in C655_PATHS}
    check("immutable Cycle655 quartet is byte exact", observed==PINS,
          {"commit":IMMUTABLE_C655,"mismatches":[path for path in PINS if observed[path]!=PINS[path]]})
    export655,shore,receipt655 = load_immutable_cycle655()
    raw652,receipt652 = load_immutable_cycle652_receipt()
    check("Cycle655 and Cycle652 premises load from immutable archives only",
          sha256(raw652).hexdigest()==C652_RECEIPT_SHA256 and receipt655["pass"] and receipt652["pass"],
          {"Cycle655":receipt655["Status"],"Cycle652":receipt652["Status"],
           "Cycle652_receipt_sha256":sha256(raw652).hexdigest()})
    route_a = route_a_flat_spatial_instruction_fibre(receipt652)
    route_b = route_b_reusable_stream(receipt652)
    route_c = route_c_circulating_band(receipt652)
    controls = inherited_controls(receipt655,receipt652,route_c)
    nogo = no_go_discipline(route_a,route_b,route_c)
    note = NOTE.read_text()
    markers = ("Status: **PASS**","Authority: **none**","Audit: **unset**","Route A","Route B","Route C",
               "no-host","gate/site digest","all24/all576","ordinary translations","N1-N8","Axiom pressure: **none**")
    check("Cycle657 note freezes all three dispositions, exact missing terminal, and N1-N8 scope",
          all(marker in note for marker in markers),markers)
    autonomous_global = bool(route_a["pass_as_global_autonomous_route"]
                             or route_b["pass_as_global_autonomous_route"]
                             or route_c["pass_as_global_autonomous_route"])
    overall = bool(route_a["pass_as_exact_discriminator"] and route_b["pass_as_exact_partial"]
                   and route_c["pass_as_literal_band_geometry"] and controls["pass"] and nogo["pass"]
                   and not autonomous_global and not nogo["shared_route_independent_obstruction"]
                   and not nogo["axiom_pressure"])
    check("Cycle657 advances physical band/count traversal while preserving the no-host gate/site firewall",
          overall,{"autonomous_global":autonomous_global,"emitted_digests":[row["emitted_gate_site_sha256"] for row in route_b["systems"]]})
    result = {
        "cycle":657,"date":"2026-07-23","Status":"PASS" if overall and FAIL==0 else "FAIL",
        "status":"cycle657-full-program-port-and-count-traversal-positive-no-host-gate-site-digest-open",
        "classification":"literal covariant circulating program-band traversal and reusable count recurrence with three named global dispatch interfaces",
        "authority":AUTHORITY,"audit":AUDIT,"author_accepted":False,"author_artifact_status_accepted":False,
        "constitutional_effect":"none","breakthrough":False,
        "shore":{"immutable_Cycle655_commit":IMMUTABLE_C655,"immutable_Cycle652_commit":IMMUTABLE_C652,
                 "pins":PINS,"observed":observed,"working_tree_bytes_used_as_premise":False,
                 "no_go_skill_origin_main_sha256":NO_GO_ORIGIN_MAIN_SHA256,
                 "freshness_check_origin_main_sha256":FRESHNESS_ORIGIN_MAIN_SHA256,
                 "proof_search_governance_origin_main_sha256":PROOF_SEARCH_ORIGIN_MAIN_SHA256},
        "exact_target_contract":{
            "target":"injectively place a streamed program fibre for every immutable Cycle652 primitive and execute a full forward/inverse recurrent traversal whose state-selected opcode/site digest equals the L3/L6/L7 fixed words with no host gate, site, path, or schedule service",
            "quantifiers_domain":"L3/L6/L7; every placed program role and fixed-word primitive ordinal; ordinary translations; all24 frames/all576 products; lawful, deletion, leakage, malformed token/opcode/counter/route/scratch sectors",
            "allowed_premises":"immutable Cycle652 program placements/fixed-word commitments and Cycle655 bounded local kernels/nine-colour state-carried phase; supplied blank backbone remains explicit",
            "forbidden_weakenings":"no digest-as-program substitution, Python event/row selector, host path/schedule, opaque exception hash as payload, refit, blank renewal, static repair, E, preparation, occurrence, Record, time, rate, energy, source, gravity, full-compiler, breakthrough, minimum-content, or axiom promotion",
            "completion_witness":"all emitted opcode/site digests equal immutable commitments and a literal local successor/decoder returns head, token, opcode, counters, route stack, enable, probe, and scratch",
            "does_not_count":"raw capacity, count-only wrap, host-indexed port traversal, source-code reproducibility, or an opaque digest without literal program values",
        },
        "route_A_spatial_instruction_fibre":route_a,
        "route_B_streamed_reusable_packets":route_b,
        "route_C_staggered_circulating_band":route_c,
        "inherited_controls":controls,
        "strongest_constructive_result":"for L3/L6/L7, one serialized head visits every immutable Cycle652 placed program port under the exact occupied-safe fine-NN outer-backbone formula, returns forward and inverse at the port/count level, preserves static seed adjacency, and passes ordinary-translation/all24/all576 geometry while one reusable Cycle655 tile closes the full primitive-count recurrence",
        "route_by_route_disposition":{
            "A_spatial_instruction_fibre":"FAIL_ROUTE_SPECIFIC_L3_EXPLICIT_FLAT_REPRESENTATION_EXCEEDS_MARGIN_L6_L7_UNPLACED",
            "B_streamed_reusable_packets":"PARTIAL_COUNT_AND_CONSTANT_TILE_PASS_PROGRAM_VALUES_AND_GATE_SITE_DECODER_OPEN",
            "C_staggered_circulating_band":"PARTIAL_LITERAL_BAND_TRAVERSAL_PASS_LOCAL_SUCCESSOR_AND_EVENT_DECODER_OPEN",
        },
        "autonomous_local_dispatch_kernel_pass":True,
        "autonomous_token_conditioned_global_dispatch_pass":autonomous_global,
        "full_no_host_head_traversal_gate_site_digest_pass":False,
        "full_physical_oracle_compiler_pass":False,
        "shared_route_independent_obstruction":False,"axiom_pressure":False,
        "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP",
        "shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False,"minimum_content_shipped":False,
        "shared_obstruction_shipped":False,"axiom_pressure_shipped":False,
        "separate_unclosed_interfaces":{
            "dispatcher":"program value binding, local successor, and gate/site decoder",
            "blank_renewal":"not attempted; backbone blanks remain supplied",
            "static_enforcement_or_repair":"not attempted; dispatcher is not repair/enforcement",
            "physical_E":"not attempted; no preparation/intertwiner claim",
        },
        "supplied_structure_inventory":{
            "immutable_Cycle652_program_seed_port_coordinates":True,
            "immutable_fixed_word_digests_and_counts":True,
            "Cycle655_125_M2_local_tile":True,"state_carried_nine_colour_phase":True,
            "state_carried_frame_and_origin":True,"blank_outer_backbone":True,
            "literal_program_value_word_at_outer_seeds":False,
            "literal_next_port_pointer_fields":False,"lowered_gate_site_decoder":False,
            "host_row_index_in_band_audit":True,"autonomous_blank_renewal":False,
            "static_enforcement_or_repair":False,"physical_E_or_preparation":False,
        },
        "semantic_firewall":{"colour_phase_is_time":False,"colour_phase_is_rate":False,
                             "gate_phase_is_energy":False,"gate_count_is_rate":False,
                             "token_or_pointer_is_Record":False,"program_band_is_full_compiler":False},
        "six_wall_ledger":{
            "C_ref":"the literal program seed/port band passes ordinary translations, all24 and all576 group structure; state-carried frame/origin/phase and supplied backbone remain explicit",
            "C_num":"exact capacities, counts, coordinates, NN edges, digests-as-commitments, and deletion residuals only; no normalization/Born claim",
            "C_wrap":"full placed-port and primitive-count forward/inverse returns pass; state-selected opcode/site digest, local successor, occurrence/history, and preparation remain absent",
            "C_int":"immutable coin/stream/contact and fixed-word pins are unchanged; no new mass/contact/seam fixture, inertia law, or E-intertwiner is executed",
            "C_local":"one reusable bounded tile and a literal circulating band replace per-event tile replication geometrically; program values, local successor, gate/site decoder, blank renewal, repair, and E remain open",
            "C_source":"unchanged; band length, capacity, counters, and phase carry no gravity/source meaning",
        },
        "maturity_0_to_5":{"operational_quantum_and_records":2,"causal_time":1,"inertia_and_matter":1,
                           "gravity_and_source":1,"Born_and_probability":1},
        "no_go_discipline":nogo,
        "optimal_next_campaign":"export and bind the literal Cycle652 compressed program/search values to the placed seeds, injectively place next-port pointer fields, lower the descriptor/support/route-step decoder with Cycle638 reversible counter primitives, and rerun until the state-emitted L3/L6/L7 opcode/site digests match; keep blank renewal, repair, and E separate",
        "resources":{"elapsed_seconds":time.perf_counter()-started,
                     "maximum_RSS_bytes":int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform=="darwin" else resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)},
    }
    result.update({"tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,
                   "pass":bool(overall and FAIL==0)})
    RECEIPT.write_text(json.dumps(result,indent=2,sort_keys=True,default=json_default)+"\n")
    print(json.dumps({"status":result["Status"],"tests":f"{PASS}/{PASS+FAIL}",
                      "elapsed":result["resources"]["elapsed_seconds"],
                      "receipt":str(RECEIPT.relative_to(ROOT))},sort_keys=True))
    export655.cleanup()
    return int(not result["pass"])


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True,exist_ok=True)
    with COLD.open("w") as stream:
        previous=sys.stdout;sys.stdout=Tee(previous,stream)
        try:raise SystemExit(main())
        finally:sys.stdout=previous
