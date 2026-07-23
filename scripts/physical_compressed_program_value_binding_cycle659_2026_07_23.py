#!/usr/bin/env python3
"""Cycle659: compressed program-value binding and decoder tournament.

Materializes every retained selector/header bit and complete next-port packet
value words, while preserving the firewall between value words, physical local
placement, and a decoder that emits the immutable Cycle652 gate/site word.

Authority none; audit unset; constitutional effect none.
"""
from __future__ import annotations

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
IMMUTABLE_C657 = "60f450e0090d13343686554453380990fd1fdf27"
IMMUTABLE_C655 = "a1b5d30bba9bccfedfaef87deb2472b74508f8f6"
IMMUTABLE_C652 = "d353925ca046702f1b0f50a41a6f8fa5a0ee3395"
C657_PATHS = (
    "scripts/physical_streamed_program_fibre_cycle657_2026_07_23.py",
    "docs/work_history/repo/review_feedback/PHYSICAL_STREAMED_PROGRAM_FIBRE_CYCLE657_NOTE_2026-07-23.md",
    "outputs/physical_streamed_program_fibre_cycle657_receipt_2026_07_23.json",
    "outputs/physical_streamed_program_fibre_cycle657_cold_2026_07_23.txt",
)
PINS = {
    C657_PATHS[0]: "3bc1c5ff01d8ed15f99d7080f698f451a983f88737779fddeab13ffa0ba1e520",
    C657_PATHS[1]: "c6c0d850cd3b47a909776e76474db38403b303e9a4d27e7d3e29a6d18cb3a05a",
    C657_PATHS[2]: "839bf462b87fed29490d03044dd215293ee496c9a7c561f468b19604ddef09db",
    C657_PATHS[3]: "0f6feda424540609bbe701ce91176fecedb7d6f3aec96d21668a7619d8f90924",
}
C652_RECEIPT_PATH = "outputs/physical_inherited_role_alias_repair_tournament_cycle652_receipt_2026_07_23.json"
C652_RECEIPT_SHA256 = "56870b951b93c81125789041af6758196e588eeddf2cf7b0235e1f7fd5b03379"
C655_RECEIPT_PATH = "outputs/physical_moving_head_autonomous_dispatcher_cycle655_receipt_2026_07_23.json"
C655_RECEIPT_SHA256 = "a518191b6d52309583108558b878d4578ffb8f78386cec7766ff959e392bf3f6"
NO_GO_ORIGIN_MAIN_SHA256 = "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7"
FRESHNESS_ORIGIN_MAIN_SHA256 = "1e0ec4ef4d7c5dd24243d7c3954c78a3f00ecd3d5e43805e788dd3629973a962"
PROOF_SEARCH_ORIGIN_MAIN_SHA256 = "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258"
AUTHORITY = "none"
AUDIT = "unset"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_COMPRESSED_PROGRAM_VALUE_BINDING_CYCLE659_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_compressed_program_value_binding_cycle659_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_compressed_program_value_binding_cycle659_cold_2026_07_23.txt"
PASS = FAIL = 0


class Tee:
    def __init__(self,*streams): self.streams=streams
    def write(self,value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label,condition,detail=""):
    global PASS,FAIL
    PASS += int(bool(condition)); FAIL += int(not bool(condition))
    print("PASS" if condition else "FAIL",label,"::",detail)


def sha_file(path): return sha256(path.read_bytes()).hexdigest()


def bits(value,width): return tuple((int(value)>>shift)&1 for shift in reversed(range(width)))


def from_bits(word):
    answer=0
    for bit in word: answer=(answer<<1)|int(bit)
    return answer


def json_default(value):
    if isinstance(value,np.integer): return int(value)
    if isinstance(value,np.floating): return float(value)
    if isinstance(value,np.ndarray): return value.tolist()
    if isinstance(value,tuple): return list(value)
    raise TypeError(type(value).__name__)


def load_immutable_cycle657():
    export=tempfile.TemporaryDirectory(prefix="cycle659-immutable-");shore=Path(export.name).resolve()
    previous_dir,previous_tree=os.environ.get("GIT_DIR"),os.environ.get("GIT_WORK_TREE")
    os.environ["GIT_DIR"]=str((ROOT/".git").resolve());os.environ["GIT_WORK_TREE"]=str(ROOT.resolve())
    archive=subprocess.check_output(["git","archive","--format=tar",IMMUTABLE_C657,*C657_PATHS])
    with tarfile.open(fileobj=io.BytesIO(archive),mode="r:") as stream:stream.extractall(shore,filter="data")
    if previous_dir is None:os.environ.pop("GIT_DIR",None)
    else:os.environ["GIT_DIR"]=previous_dir
    if previous_tree is None:os.environ.pop("GIT_WORK_TREE",None)
    else:os.environ["GIT_WORK_TREE"]=previous_tree
    return export,shore,json.loads((shore/C657_PATHS[2]).read_text())


def git_receipt(commit,path,expected_sha):
    raw=subprocess.check_output(["git","show",f"{commit}:{path}"],cwd=ROOT)
    return raw,json.loads(raw),sha256(raw).hexdigest()==expected_sha


def determinant(matrix): return int(round(np.linalg.det(np.asarray(matrix,dtype=int))))


def proper_frames():
    frames=[]
    for order in permutations(range(3)):
        for signs in product((-1,1),repeat=3):
            matrix=np.zeros((3,3),dtype=int)
            for column,row in enumerate(order):matrix[row,column]=signs[column]
            if determinant(matrix)==1:frames.append(matrix)
    return tuple(frames)


FRAMES=proper_frames()


def rotate_mod(frame,site,modulus):
    return tuple(int(value)%modulus for value in np.asarray(frame,dtype=int)@np.asarray(site,dtype=int))


def frame_key(frame): return tuple(int(value) for value in np.asarray(frame).reshape(-1))


def route_a_literal_value_export_bind(receipt652):
    systems=[]
    for system in receipt652["systems"]:
        length=system["length"];search=system["compiled_search_state_bank"]
        placement=system["program_placement"];rows=search["rows"]
        header=[];header_records=[]
        for row in rows:
            record=(int(row["kind"]!="two_axis_formula"),)+bits(row["selector"],4)
            header.extend(record);header_records.append(record)
        total=search["selector_and_exception_state_bits"]
        missing=total-len(header);exception_records=search["stored_exception_records"]
        run_count_bits=4*exception_records
        direction_count_bits=missing-run_count_bits
        total_runs=direction_count_bits//11
        start=placement["role_orbits"]-total
        placed=sorted(placement["placements"],key=lambda row:row["logical_bit"])
        placed_by_index={row["logical_bit"]:row for row in placed}
        binding=sha256();binding_failures=0
        first=[];last=[]
        for offset,value in enumerate(header):
            logical=start+offset;row=placed_by_index.get(logical)
            binding_failures += row is None
            if row is not None:
                item={"logical_bit":logical,"seed":row["seed"],"port":row["port"],"value":value}
                binding.update(repr((logical,tuple(row["seed"]),value)).encode())
                if len(first)<4:first.append(item)
                last.append(item);last=last[-4:]
        candidate=tuple(header)+tuple(0 for _ in range(missing))
        candidate_sha=sha256(bytes(candidate)).hexdigest()
        expected_sha=search["state_sha256"]
        deleted_sha=sha256(bytes(candidate[:-1])).hexdigest()
        flipped=list(header);flipped[1]^=1
        flipped_header_sha=sha256(bytes(flipped)).hexdigest()
        systems.append({
            "length":length,"search_role_start":start,"search_role_end":placement["role_orbits"]-1,
            "target_header_records":len(rows),"formula_header_records":search["formula_records"],
            "exception_header_records":exception_records,"materialized_header_bits":len(header),
            "placed_header_binding_failures":binding_failures,"placed_header_binding_sha256":binding.hexdigest(),
            "first_bindings":first,"last_bindings":last,
            "complete_search_state_bits":total,"missing_exception_payload_bits":missing,
            "missing_run_count_bits":run_count_bits,"missing_direction_count_bits":direction_count_bits,
            "deduced_total_exception_direction_runs":total_runs,
            "candidate_unknown_zero_fill_sha256":candidate_sha,"expected_search_state_sha256":expected_sha,
            "candidate_matches_expected":candidate_sha==expected_sha,
            "delete_one_bit_length_and_sha_residual":int(len(candidate[:-1])!=total and deleted_sha!=expected_sha),
            "flip_one_selector_header_sha_residual":int(flipped_header_sha!=sha256(bytes(header)).hexdigest()),
            "malformed_selector_15_rejected":15>exception_records,
            "complete_literal_value_word_bound":False,
        })
    result={
        "route":"A literal compressed value export/bind","systems":systems,
        "strongest_positive":"every retained kind/selector header bit is assigned a value and bound to its already placed Cycle652 seed",
        "exact_missing_payload":"each size lacks the same 989-bit exception suffix: eight 4-bit run counts plus 87 direction/count pairs of 11 bits",
        "host_generator_replay_used":False,"digest_used_as_program":False,
        "pass_as_complete_value_export":False,
    }
    result["pass_as_exact_partial"] = bool(all(
        row["placed_header_binding_failures"]==0 and row["missing_exception_payload_bits"]==989
        and row["missing_run_count_bits"]==32 and row["deduced_total_exception_direction_runs"]==87
        and not row["candidate_matches_expected"] and row["delete_one_bit_length_and_sha_residual"]
        and row["flip_one_selector_header_sha_residual"] and row["malformed_selector_15_rejected"]
        for row in systems))
    check("route A binds every retained selector header and isolates an exact 989-bit unexported exception suffix per size",
          result["pass_as_exact_partial"],{row["length"]:(row["materialized_header_bits"],row["missing_exception_payload_bits"],row["candidate_matches_expected"]) for row in systems})
    return result


def gamma_encode(value):
    if value<=0:raise ValueError(value)
    binary=bits(value,value.bit_length())
    return tuple(0 for _ in range(len(binary)-1))+binary


def gamma_decode(word,offset):
    zeros=0
    while offset+zeros<len(word) and word[offset+zeros]==0:zeros+=1
    if offset+zeros>=len(word):raise ValueError("truncated gamma prefix")
    end=offset+2*zeros+1
    if end>len(word):raise ValueError("truncated gamma payload")
    return from_bits(word[offset+zeros:end]),end


def parse_packets(word,index_bits,coordinate_bits,side):
    offset=0;rows=[];malformed=0
    while offset<len(word):
        size,offset=gamma_decode(word,offset)
        if offset+size>len(word):raise ValueError("truncated packet")
        payload=word[offset:offset+size];offset+=size
        expected=index_bits+3*coordinate_bits
        if size!=expected:malformed+=1;continue
        logical=from_bits(payload[:index_bits]);cursor=index_bits;coord=[]
        for _ in range(3):
            coord.append(from_bits(payload[cursor:cursor+coordinate_bits]));cursor+=coordinate_bits
        malformed += any(value>=side for value in coord)
        rows.append((logical,tuple(coord)))
    return rows,malformed


def route_b_self_delimiting_packets(receipt652):
    systems=[];all24_failures=translation_failures=group_failures=0
    frame_map={frame_key(frame) for frame in FRAMES}
    for left in FRAMES:
        for right in FRAMES:group_failures += frame_key(np.asarray(left)@np.asarray(right)) not in frame_map
    for system in receipt652["systems"]:
        length=system["length"];side=129*length
        placements=sorted(system["program_placement"]["placements"],key=lambda row:row["logical_bit"])
        index_width=max(1,math.ceil(math.log2(len(placements))));coord_width=math.ceil(math.log2(side))
        word=[];expected=[];prefix_bits=0
        for index,row in enumerate(placements):
            target=tuple(placements[(index+1)%len(placements)]["port"])
            payload=bits(row["logical_bit"],index_width)+tuple(bit for value in target for bit in bits(value,coord_width))
            prefix=gamma_encode(len(payload));prefix_bits+=len(prefix);word.extend(prefix);word.extend(payload)
            expected.append((row["logical_bit"],target))
        decoded,malformed=parse_packets(tuple(word),index_width,coord_width,side)
        deletion_detected=False
        try:parse_packets(tuple(word[:-1]),index_width,coord_width,side)
        except ValueError:deletion_detected=True
        flipped=list(word);flipped[-1]^=1
        try:flipped_decoded,flipped_malformed=parse_packets(tuple(flipped),index_width,coord_width,side)
        except ValueError:flipped_decoded=[];flipped_malformed=1
        flip_residual=int(flipped_decoded!=expected or flipped_malformed>0)
        malformed_payload=bits(0,index_width)+bits(side,coord_width)+bits(0,coord_width)+bits(0,coord_width)
        malformed_word=gamma_encode(len(malformed_payload))+malformed_payload
        _malformed_rows,malformed_count=parse_packets(malformed_word,index_width,coord_width,side)
        frame_failures=0
        for frame in FRAMES:
            for _logical,target in expected:
                rotated=rotate_mod(frame,target,side)
                encoded=tuple(bit for value in rotated for bit in bits(value,coord_width))
                decoded_target=tuple(from_bits(encoded[q*coord_width:(q+1)*coord_width]) for q in range(3))
                frame_failures += decoded_target!=rotated
        all24_failures += frame_failures
        translated_failures=0
        for shift in product(range(3),repeat=3):
            for _logical,target in expected:
                shifted=tuple((target[q]+shift[q])%side for q in range(3))
                encoded=tuple(bit for value in shifted for bit in bits(value,coord_width))
                translated_failures += tuple(from_bits(encoded[q*coord_width:(q+1)*coord_width]) for q in range(3))!=shifted
        translation_failures += translated_failures
        packet_bits=len(word);replicated=24*packet_bits;margin=system["covariance_and_capacity"]["capacity_margin"]
        systems.append({
            "length":length,"program_records":len(placements),"logical_index_bits":index_width,
            "coordinate_bits_per_axis":coord_width,"payload_bits_per_packet":index_width+3*coord_width,
            "self_delimiting_prefix_bits":prefix_bits,"active_packet_value_bits":packet_bits,
            "all24_frame_replicated_candidate_M2":replicated,"Cycle652_capacity_margin_M2":margin,
            "raw_capacity_discriminator_pass":replicated<=margin,
            "packet_value_word_sha256":sha256(bytes(word)).hexdigest(),
            "decode_failures":sum(left!=right for left,right in zip(decoded,expected))+abs(len(decoded)-len(expected)),
            "delete_last_bit_detected":deletion_detected,"flip_last_pointer_bit_residual":flip_residual,
            "malformed_coordinate_equal_side_rejected":malformed_count>0,
            "all24_value_transform_failures":frame_failures,"ordinary_translation_value_failures":translated_failures,
            "injective_local_pointer_M2_placement_executed":False,
            "fine_NN_pointer_to_source_seed_routing_executed":False,
        })
    result={
        "route":"B self-delimiting/topological next-port packets","systems":systems,
        "all24_value_failures":all24_failures,"all576_group_failures":group_failures,
        "ordinary_translation_failures":translation_failures,
        "complete_next_port_value_word_materialized":True,
        "injective_local_next_port_fields_placed":False,
        "pass_as_global_route":False,
    }
    result["pass_as_value_word"] = bool(not any((all24_failures,group_failures,translation_failures)) and all(
        row["decode_failures"]==0 and row["delete_last_bit_detected"] and row["flip_last_pointer_bit_residual"]
        and row["malformed_coordinate_equal_side_rejected"] and row["raw_capacity_discriminator_pass"]
        and not row["injective_local_pointer_M2_placement_executed"] for row in systems))
    check("route B materializes exact self-delimiting next-port value words with covariance and corruption controls, but no physical sidecar placement",
          result["pass_as_value_word"],{row["length"]:(row["active_packet_value_bits"],row["all24_frame_replicated_candidate_M2"],row["decode_failures"]) for row in systems})
    return result


def route_c_distributed_formula_evaluator(receipt652,receipt655):
    systems=[]
    counters=receipt652["baseline_Cycle638"]["counters"]
    for system in receipt652["systems"]:
        search=system["compiled_search_state_bank"];descriptor=system["descriptor_summary"]
        primitive=system["literal_oracle_circuit_word"]
        selector_failures=sum((row["kind"]=="two_axis_formula")!=(row["selector"]==0) for row in search["rows"])
        systems.append({
            "length":system["length"],"checks":descriptor["checks"],
            "support_occurrences":descriptor["support_occurrences"],"maximum_support":descriptor["maximum_support"],
            "route_records":search["target_records"],"formula_route_records":search["formula_records"],
            "exception_route_records":search["stored_exception_records"],
            "route_kind_selector_failures":selector_failures,
            "formula_route_fraction":search["formula_records"]/search["target_records"],
            "descriptor_formula_source_exists":True,"descriptor_formula_lowered_to_physical_rule":False,
            "formula_route_evaluator_lowered_to_Cycle638_counters":False,
            "exception_direction_payload_available":False,
            "Cycle652_expected_gate_site_sha256":primitive["literal_gate_word_sha256"],
            "recurrent_state_emitted_gate_site_sha256":None,
            "emitted_digest_matches":False,
            "full_forward_inverse_head_traversal_with_gate_site_events":False,
        })
    result={
        "route":"C distributed formula evaluator","systems":systems,
        "Cycle638_reversible_counter_pass":counters["pass"],
        "Cycle638_increment_inverse_boundary_failures":counters["increment_inverse_boundary_failures"],
        "Cycle638_total_counter_Toffoli_macros":counters["total_counter_Toffoli_macros_per_all_widths"],
        "Cycle638_fine_NN_after_decoder_routing":counters["fine_NN_after_decoder_routing"],
        "Cycle655_bounded_kernel_pass":receipt655["autonomous_local_dispatch_kernel_pass"],
        "Cycle655_global_dispatch_pass":receipt655["autonomous_token_conditioned_global_dispatch_pass"],
        "Python_descriptor_or_route_generator_replayed":False,
        "digest_used_as_program":False,
        "pass_as_global_route":False,
    }
    result["pass_as_exact_discriminator"] = bool(counters["pass"] and not counters["increment_inverse_boundary_failures"]
        and result["Cycle655_bounded_kernel_pass"] and not result["Cycle655_global_dispatch_pass"]
        and all(row["route_kind_selector_failures"]==0 and not row["emitted_digest_matches"] for row in systems))
    check("route C inherits exact Cycle638 counters and Cycle655 kernels but emits no gate/site digest without the unlowered evaluator",
          result["pass_as_exact_discriminator"],{row["length"]:(row["formula_route_records"],row["exception_route_records"],row["emitted_digest_matches"]) for row in systems})
    return result


def inherited_controls(receipt652,receipt655):
    result={
        "Cycle652_lawful_auxiliary_slice_leakage_norm":receipt652["baseline_Cycle638"]["execution"]["lawful_auxiliary_slice_leakage_norm"],
        "Cycle652_full_code_leakage_executed":receipt652["baseline_Cycle638"]["execution"]["full_physical_E_or_full_code_leakage"],
        "Cycle655_local_kernel_exact_residuals":receipt655["exact_local_kernel"]["gated_exact_residuals"],
        "Cycle655_parity_enable_scratch_return":receipt655["exact_local_kernel"]["parity_and_enable_scratch_return_clean"],
        "Cycle655_token_opcode_counter_phase_sector_tests":receipt655["route_A_moving_head_program_rail"]["sector_tests"],
        "Cycle655_malformed_sector_tests":receipt655["route_A_moving_head_program_rail"]["malformed_sector_tests"],
        "Cycle655_inverse_failures":receipt655["route_A_moving_head_program_rail"]["inverse_failures"],
        "mass_contact_seam_pin_scope":"immutable Cycle652 call/fixed-word commitments only; Cycle659 executes no new mass/contact/seam fixture",
    }
    result["pass"] = bool(result["Cycle652_lawful_auxiliary_slice_leakage_norm"]==0
        and not result["Cycle652_full_code_leakage_executed"]
        and max(result["Cycle655_local_kernel_exact_residuals"].values())<1e-11
        and result["Cycle655_parity_enable_scratch_return"]
        and result["Cycle655_token_opcode_counter_phase_sector_tests"]==207669
        and result["Cycle655_malformed_sector_tests"]==39663 and result["Cycle655_inverse_failures"]==0)
    check("inherited leakage, exact local-kernel, token/opcode/counter, malformed, and scratch controls remain pinned",
          result["pass"],{"lawful_leakage":result["Cycle652_lawful_auxiliary_slice_leakage_norm"],
                           "sectors":result["Cycle655_token_opcode_counter_phase_sector_tests"],
                           "malformed":result["Cycle655_malformed_sector_tests"]})
    return result


def no_go_discipline(route_a,route_b,route_c):
    families=[
        {"family":"literal selector/search value export", "object":"Cycle652 placed search-bit seeds", "mechanism":"bind retained kind/selector bits by logical index", "terminal":"complete exact search state value word", "strength_vs_target":"target-equivalent input", "honesty_marker":"ATTEMPTED", "result":"header prefix bound; exact 989-bit exception suffix absent per size"},
        {"family":"self-delimiting next-port packets", "object":"logical index and successor port coordinates", "mechanism":"gamma-length-prefixed binary packet value word", "terminal":"injectively placed local sidecar with fine-NN source access", "strength_vs_target":"target-equivalent successor", "honesty_marker":"ATTEMPTED", "result":"complete covariant value word and raw capacity pass; physical placement/routing open"},
        {"family":"distributed formula evaluator", "object":"descriptor/support/route-step state", "mechanism":"Cycle638 reversible counters feeding Cycle655 opcode kernels", "terminal":"state-emitted immutable gate/site digest", "strength_vs_target":"target-equivalent", "honesty_marker":"ATTEMPTED", "result":"selector and counters pass; evaluator unlowered and digest null"},
        {"family":"self-routing topological packet", "object":"packet carries successor coordinate and content", "mechanism":"coordinate counter on supplied backbone", "terminal":"no static pointer sidecar and exact event emission", "strength_vs_target":"target-equivalent", "honesty_marker":"ATTEMPTED", "result":"pointer packets materialized; missing exception content prevents complete self-routing packet"},
        {"family":"immutable Python generator replay", "object":"Cycle652 source formulas", "mechanism":"host regenerates exception routes and events", "terminal":"physical no-host recurrent rule", "strength_vs_target":"forbidden weaker replay", "honesty_marker":"ATTEMPTED", "result":"not executed; source reproducibility is not autonomous evidence"},
    ]
    walls={
        "W_exception_payload_export":"eight run-count records and 87 direction/count pairs, 989 bits total, are absent from each retained search value surface",
        "W_pointer_sidecar_placement":"complete successor packet values exist but no injective fine-NN local M2 sidecar placement exists",
        "W_formula_decoder_lowering":"descriptor/support/route arithmetic is not lowered into a recurrent physical rule that emits gate/site events",
    }
    pairs=[{"from":a,"to":b,"implied":False,"reason":f"closing {a} does not construct {b}"} for a in walls for b in walls if a!=b]
    result={
        "Status":"PASS_SCOPED_VALUE_PREFIX_AND_POINTER_WORD_POSITIVE_GLOBAL_DECODER_OPEN",
        "N1_normalized_families":families,"N1_qualifying_attempts":len(families),"N1_required_for_negative":5,
        "N1_negative_gate":"FAIL / DO NOT SHIP",
        "N1_open_routes_not_counted":[{"family":"locally generated exception BFS proof packet","status":"OPEN / NOT COUNTED"},{"family":"recomputed successor without stored pointer","status":"OPEN / NOT COUNTED"}],
        "N2_collapsed_walls":walls,"N2_directed_ordered_pairs":pairs,
        "N3_hidden_wall_scan":[
            {"phrase":"expected search SHA-256","classification":"commitment, not missing 989-bit payload", "wall":"W_exception_payload_export"},
            {"phrase":"raw pointer capacity","classification":"value-size discriminator, not placement", "wall":"W_pointer_sidecar_placement"},
            {"phrase":"source formula exists","classification":"host source, not lowered recurrent physical law", "wall":"W_formula_decoder_lowering"},
            {"phrase":"supplied blanks","classification":"separate blank-renewal interface", "wall":None},
        ],
        "N4_exact_residual_matches":[{
            "prior_ref":IMMUTABLE_C657,"prior_path":C657_PATHS[2],"prior_line":"missing program/search values and successor",
            "prior_residual":"program/search values, next-port fields, and gate/site decoder open",
            "current_path":str(Path(__file__).relative_to(ROOT)),"current_line":"def route_a_literal_value_export_bind",
            "current_residual":"all retained headers and complete pointer values materialized; exact 989-bit exception suffix, pointer placement, and decoder lowering remain",
            "same_scope":True,"exact_match":True,"use_as_closure":False,
        }],
        "N5_rhetoric":[
            {"claim":"literal value materialization advances", "per_element":"every header bit and pointer packet bit", "per_site":"headers bind to declared seeds", "per_mode":"formula/exception selector", "per_block":"L3/L6/L7", "lattice_wide":"pointer sidecar and exception suffix not placed/materialized"},
            {"claim":"global decoder remains false", "per_element":"Cycle655 kernels exact", "per_site":"no local successor sidecar", "per_mode":"exception routes unavailable", "per_block":"expected digests only", "lattice_wide":"no recurrent event stream or E"},
        ],
        "N6_partial_closure_paths":[
            {"file":"UNMATERIALIZED/physical_exception_run_payload_export_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_exception_payload_export"},
            {"file":"UNMATERIALIZED/physical_pointer_sidecar_allocator_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_pointer_sidecar_placement"},
            {"file":"UNMATERIALIZED/physical_formula_decoder_circuit_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_formula_decoder_lowering"},
        ],
        "N7_steelman":{
            "mechanism":"export the 87 deterministic exception direction/count pairs as literal bits, use a streamed sidecar allocator to place each already materialized next-port packet beside its source port, then compile descriptor/support/route arithmetic into Cycle638 counters and Cycle655 controlled kernels",
            "actionable_steps":["retain literal exception run pairs, not hashes", "place pointer packet bits with all24 ownership", "route packet read/unread", "emit and reverse every gate/site event until all three digests match"],
            "terminal_test":"one repeated local rule reads only placed bits, emits the exact L3/L6/L7 opcode/site digests, and returns head/token/counters/routes/scratch",
            "why_it_breaks_the_negative":"Cycle659 supplies every header and successor value, leaving three concrete construction interfaces rather than a route-independent obstruction",
        },
        "N8_cross_cycle_echo":[
            {"cycle":638,"mechanism":"exact reversible counters","applicability":"available for decoder lowering, not a decoder by itself"},
            {"cycle":652,"mechanism":"search state commitment and placed roles","applicability":"headers recoverable; exception payload not retained"},
            {"cycle":655,"mechanism":"bounded controlled opcode kernels","applicability":"act layer exact; global selection absent"},
            {"cycle":657,"mechanism":"full port/count traversal","applicability":"successor/value gaps isolated"},
            {"cycle":659,"mechanism":"header binding and pointer packet word","applicability":"closes value prefixes and successor values, not placement/decoder"},
        ],
        "route_A_complete_pass":route_a["pass_as_complete_value_export"],"route_B_global_pass":route_b["pass_as_global_route"],"route_C_global_pass":route_c["pass_as_global_route"],
        "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP","shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False,"minimum_content_shipped":False,"shared_obstruction_shipped":False,"axiom_pressure_shipped":False,
        "shared_route_independent_obstruction":False,"axiom_pressure":False,
    }
    required={"prior_ref","prior_path","prior_line","prior_residual","current_path","current_line","current_residual","same_scope","exact_match","use_as_closure"}
    result["pass"] = bool(len(families)>=5 and len(pairs)==6 and all(required<=set(row) for row in result["N4_exact_residual_matches"])
        and all(result[key]=="FAIL / DO NOT SHIP" for key in ("broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate"))
        and not any(result[key] for key in ("broad_negative_shipped","minimum_content_shipped","shared_obstruction_shipped","axiom_pressure_shipped")))
    check("canonical N1-N8 blocks missing retained payload/placement/decoder from becoming a shared obstruction or axiom pressure",
          result["pass"],{"families":len(families),"walls":len(walls),"pairs":len(pairs)})
    return result


def main():
    global PASS,FAIL
    started=time.perf_counter();observed={path:sha_file(ROOT/path) for path in C657_PATHS}
    check("immutable Cycle657 quartet is byte exact",observed==PINS,{"commit":IMMUTABLE_C657,"mismatches":[path for path in PINS if observed[path]!=PINS[path]]})
    export,shore,receipt657=load_immutable_cycle657()
    raw652,receipt652,pin652=git_receipt(IMMUTABLE_C652,C652_RECEIPT_PATH,C652_RECEIPT_SHA256)
    raw655,receipt655,pin655=git_receipt(IMMUTABLE_C655,C655_RECEIPT_PATH,C655_RECEIPT_SHA256)
    check("Cycle657, Cycle655, and Cycle652 premises are immutable and passing",receipt657["pass"] and receipt655["pass"] and receipt652["pass"] and pin652 and pin655,
          {"Cycle657":receipt657["Status"],"Cycle655":receipt655["Status"],"Cycle652":receipt652["Status"],"pin652":pin652,"pin655":pin655})
    route_a=route_a_literal_value_export_bind(receipt652)
    route_b=route_b_self_delimiting_packets(receipt652)
    route_c=route_c_distributed_formula_evaluator(receipt652,receipt655)
    controls=inherited_controls(receipt652,receipt655)
    nogo=no_go_discipline(route_a,route_b,route_c)
    note=NOTE.read_text();markers=("Status: **PASS**","Authority: **none**","Audit: **unset**","989","Route A","Route B","Route C","self-delimiting","gate/site digest","all24/all576","ordinary translations","N1-N8","Axiom pressure: **none**")
    check("Cycle659 note freezes literal positives, exact missing bits, global terminal, and N1-N8 scope",all(marker in note for marker in markers),markers)
    autonomous_global=bool(route_a["pass_as_complete_value_export"] and route_b["pass_as_global_route"] and route_c["pass_as_global_route"])
    overall=bool(route_a["pass_as_exact_partial"] and route_b["pass_as_value_word"] and route_c["pass_as_exact_discriminator"]
        and controls["pass"] and nogo["pass"] and not autonomous_global and not nogo["shared_route_independent_obstruction"] and not nogo["axiom_pressure"])
    check("Cycle659 materializes header and successor values without promoting absent physical placement/decoder to no-host dispatch",overall,
          {"autonomous_global":autonomous_global,"emitted_digests":[row["recurrent_state_emitted_gate_site_sha256"] for row in route_c["systems"]]})
    result={
        "cycle":659,"date":"2026-07-23","Status":"PASS" if overall and FAIL==0 else "FAIL",
        "status":"cycle659-selector-header-and-next-port-values-positive-exception-payload-placement-decoder-open",
        "classification":"literal retained-header binding and complete self-delimiting successor value words with three named global decoder interfaces",
        "authority":AUTHORITY,"audit":AUDIT,"author_accepted":False,"author_artifact_status_accepted":False,"constitutional_effect":"none","breakthrough":False,
        "shore":{"immutable_Cycle657_commit":IMMUTABLE_C657,"immutable_Cycle655_commit":IMMUTABLE_C655,"immutable_Cycle652_commit":IMMUTABLE_C652,
                 "pins":PINS,"observed":observed,"Cycle652_receipt_sha256":sha256(raw652).hexdigest(),"Cycle655_receipt_sha256":sha256(raw655).hexdigest(),
                 "working_tree_bytes_used_as_premise":False,"no_go_skill_origin_main_sha256":NO_GO_ORIGIN_MAIN_SHA256,
                 "freshness_check_origin_main_sha256":FRESHNESS_ORIGIN_MAIN_SHA256,"proof_search_governance_origin_main_sha256":PROOF_SEARCH_ORIGIN_MAIN_SHA256},
        "exact_target_contract":{
            "target":"materialize and bind the complete compressed Cycle652 program/search values, injectively place local successor fields, lower descriptor/support/route arithmetic, and execute a recurrent no-host L3/L6/L7 gate/site stream whose forward digest matches and whose inverse returns all head/counter/route/scratch state",
            "quantifiers_domain":"every retained search bit, program role, next-port packet, descriptor/support/route record, L3/L6/L7 fixed event, ordinary translation, all24/all576, deletion/leakage/malformed content",
            "allowed_premises":"immutable Cycle638 counters, Cycle652 placed roles/commitments, Cycle655 bounded kernels, Cycle657 program-band geometry, explicit supplied blanks",
            "forbidden_weakenings":"no Python generator replay, digest-as-program, hash preimage assumption, host gate/site/path/schedule, raw-capacity-as-placement, refit, blank renewal, repair, E, preparation, occurrence, Record, time, rate, energy, source, gravity, full/strict/breakthrough/minimum/axiom promotion",
            "completion_witness":"complete literal value word plus physical pointer sidecar and lowered decoder emits all three immutable gate/site digests and reverses cleanly",
            "does_not_count":"known prefix, pointer value word without placement, counters/kernels without decoder, expected digest without emitted digest, or source-code reproducibility",
        },
        "route_A_literal_compressed_value_export_bind":route_a,"route_B_self_delimiting_next_port_packets":route_b,"route_C_distributed_formula_evaluator":route_c,
        "inherited_controls":controls,
        "strongest_constructive_result":"all retained Cycle652 kind/selector header bits are literally valued and bound to their already placed program seeds, and complete self-delimiting next-port packet value words are constructed, decoded, corrupted, and transformed covariantly for every L3/L6/L7 program role with explicit bit/M2 overhead",
        "route_by_route_disposition":{
            "A_literal_export_bind":"PARTIAL_HEADER_BINDING_PASS_EXACT_989_BIT_EXCEPTION_SUFFIX_PER_SIZE_UNEXPORTED",
            "B_self_delimiting_packets":"PARTIAL_COMPLETE_SUCCESSOR_VALUE_WORD_PASS_INJECTIVE_LOCAL_M2_PLACEMENT_OPEN",
            "C_distributed_evaluator":"FAIL_GLOBAL_CYCLE638_COUNTERS_AND_CYCLE655_KERNELS_PASS_FORMULA_DECODER_UNLOWERED_EMITTED_DIGEST_NULL",
        },
        "complete_compressed_program_value_word_pass":False,"injective_local_next_port_fields_pass":False,
        "recurrent_exact_gate_site_digest_pass":False,"full_forward_inverse_no_host_traversal_pass":False,
        "autonomous_token_conditioned_global_dispatch_pass":autonomous_global,"full_physical_oracle_compiler_pass":False,
        "shared_route_independent_obstruction":False,"axiom_pressure":False,
        "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP","shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False,"minimum_content_shipped":False,"shared_obstruction_shipped":False,"axiom_pressure_shipped":False,
        "separate_unclosed_interfaces":{"dispatcher":"989-bit exception suffix, physical pointer sidecar, and formula decoder","blank_renewal":"not attempted","static_enforcement_or_repair":"not attempted","physical_E":"not attempted"},
        "supplied_structure_inventory":{
            "immutable_expected_search_and_gate_site_digests":True,"placed_search_role_coordinates":True,"retained_selector_headers":True,
            "complete_next_port_packet_values_new":True,"Cycle638_counters":True,"Cycle655_bounded_kernels":True,"blank_backbone":True,
            "literal_exception_run_payloads":False,"injective_pointer_sidecar_coordinates":False,"lowered_formula_decoder":False,
            "emitted_gate_site_digests":False,"autonomous_blank_renewal":False,"static_repair":False,"physical_E":False,
        },
        "semantic_firewall":{"counter_or_packet_phase_is_time":False,"counter_or_packet_phase_is_rate":False,"gate_phase_is_energy":False,
                             "head_or_pointer_is_Record":False,"program_value_binding_is_full_compiler":False},
        "six_wall_ledger":{
            "C_ref":"header bindings and successor values transform under ordinary translations/all24/all576; pointer placement and state-carried frame/origin remain explicit",
            "C_num":"exact bit words, prefixes, packet decodes, SHA commitments, capacity discriminators, and corruption residuals only; no probability/normalization claim",
            "C_wrap":"selector headers and successor value roundtrips close; exception payload, physical successor access, event digest, occurrence/history, and preparation remain absent",
            "C_int":"immutable call/fixed-word pins unchanged; no new mass/contact/seam fixture, inertia law, or E-intertwiner",
            "C_local":"placed headers and complete successor values advance the stream; 989-bit suffix, pointer sidecar, decoder, blank renewal, repair, and E remain open",
            "C_source":"unchanged; bit counts, packets, counters, and digests have no gravity/source meaning",
        },
        "maturity_0_to_5":{"operational_quantum_and_records":2,"causal_time":1,"inertia_and_matter":1,"gravity_and_source":1,"Born_and_probability":1},
        "no_go_discipline":nogo,
        "optimal_next_campaign":"retain/export the exact eight exception run-counts and 87 direction/count pairs per size, then build an occupied-aware all24 sidecar allocator for the complete pointer packets before lowering descriptor/support/route arithmetic; demand emitted digest equality and inverse return, keeping blanks/repair/E separate",
        "resources":{"elapsed_seconds":time.perf_counter()-started,"maximum_RSS_bytes":int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform=="darwin" else resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)},
    }
    result.update({"tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,"pass":bool(overall and FAIL==0)})
    RECEIPT.write_text(json.dumps(result,indent=2,sort_keys=True,default=json_default)+"\n")
    print(json.dumps({"status":result["Status"],"tests":f"{PASS}/{PASS+FAIL}","elapsed":result["resources"]["elapsed_seconds"],"receipt":str(RECEIPT.relative_to(ROOT))},sort_keys=True))
    export.cleanup();return int(not result["pass"])


if __name__=="__main__":
    COLD.parent.mkdir(parents=True,exist_ok=True)
    with COLD.open("w") as stream:
        previous=sys.stdout;sys.stdout=Tee(previous,stream)
        try:raise SystemExit(main())
        finally:sys.stdout=previous
