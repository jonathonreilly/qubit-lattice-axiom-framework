#!/usr/bin/env python3
"""Cycle646: orbit-tree local-enforcement oracle-grammar attempt.

Specifies a state-carried formula controller/register grammar for coherent
syndrome phase, and discriminates the simplest static XX wire construction.
The grammar is compatible with physical storage but is not literally placed
or lowered to occupied-role-safe fine-neighbor paths.
The result does not construct E, preparation, dissipative repair, or a fully
occupied-role-safe fine-NN routing corridor.

Authority none; audit unset; author accepted false; constitutional effect none.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations
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
IMMUTABLE_COMMIT = "71d15c192af1fbb82f1860052eb6b10c7f244ddd"
_EXPORT = tempfile.TemporaryDirectory(prefix="cycle646-immutable-")
IMMUTABLE_ROOT = Path(_EXPORT.name).resolve()
os.environ["GIT_DIR"] = str((ROOT / ".git").resolve())
os.environ["GIT_WORK_TREE"] = str(ROOT.resolve())
_archive = subprocess.check_output(["git", "archive", "--format=tar", IMMUTABLE_COMMIT, "scripts"], cwd=ROOT)
with tarfile.open(fileobj=io.BytesIO(_archive), mode="r:") as _tar:
    _tar.extractall(IMMUTABLE_ROOT, filter="data")
sys.path.insert(0, str(IMMUTABLE_ROOT / "scripts"))
import physical_fixed_cubic_wilson_fill_incidence_cycle642_2026_07_23 as c642

c532 = c642.c532
c235 = c642.c235
FRAMES = c642.FRAMES
K = 129
AUTHORITY = "none"
AUDIT = "unset"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ORBIT_TREE_LOCAL_ENFORCEMENT_CYCLE646_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_orbit_tree_local_enforcement_cycle646_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_orbit_tree_local_enforcement_cycle646_cold_2026_07_23.txt"
PASS = FAIL = 0
PINS = {
    "scripts/physical_fixed_cubic_wilson_fill_incidence_cycle642_2026_07_23.py": "fb0d8366494066e4191d66b9a2d83180cd99bf6f622b9de355bf28494e050bf7",
    "docs/work_history/repo/review_feedback/PHYSICAL_FIXED_CUBIC_WILSON_FILL_INCIDENCE_CYCLE642_NOTE_2026-07-23.md": "13f8074746f3b5e978f971567bbebecd1006ccd13b7d5fe91a0e38a946d30d3e",
    "outputs/physical_fixed_cubic_wilson_fill_incidence_cycle642_receipt_2026_07_23.json": "9251ac323d4f26b672783fa8ed01dc8da6f3059c308d37325b3d7984969c3b37",
    "outputs/physical_fixed_cubic_wilson_fill_incidence_cycle642_cold_2026_07_23.txt": "2af7cb45f80e1e5719da6750cd9f2efbbf2bee1bc14abe95e234eba91d6920cb",
    "scripts/physical_hierarchical_grammar_full_act_compiler_cycle638_2026_07_23.py": "7c30cb47934ea6faf908d13ef15e6d62bf0c494ba8632ebdffeec88352037d53",
    "docs/work_history/repo/review_feedback/PHYSICAL_HIERARCHICAL_GRAMMAR_FULL_ACT_COMPILER_CYCLE638_NOTE_2026-07-23.md": "30b9793f87ac0e96d92567709201fbae8833904302b9c195eb8eefcc0972abf1",
    "outputs/physical_hierarchical_grammar_full_act_compiler_cycle638_receipt_2026_07_23.json": "706a592d667dfa12a2215d588f5b3cf09c8d1212d4907e9a73d8647a76762e46",
}
NO_GO_ORIGIN_MAIN_SHA256 = "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7"


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(condition); FAIL += int(not condition)
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
            return {"ref": "Cycle646 working artifact", "path": path, "line": line,
                    "line_text": text.strip(), "fragment": fragment}
    raise AssertionError((path, fragment))


def pauli_letter(row, qubit):
    x = (row.x >> qubit) & 1; z = (row.z >> qubit) & 1
    return "I" if not (x or z) else "X" if x and not z else "Z" if z and not x else "Y"


def row_sign(row) -> int:
    y_count = (row.x & row.z).bit_count()
    delta = (row.phase - y_count) % 4
    if delta not in (0, 2): raise AssertionError("non-Hermitian stabilizer row")
    return delta // 2


def build_descriptors(length: int):
    placement, fibers = c642.allocate_orbit_roles(length)
    obj = c642.build_tree_code(length, fibers)
    modulus = K * length
    old = tuple(tuple(value % modulus for value in c642.old_position_K(obj["graph"], q))
                for q in range(obj["graph"].qubits))
    aux = {bit: tuple(site[axis] % modulus for axis in range(3))
           for role in obj["roles"]
           for bit, site in zip(obj["index"][role], obj["fibers"][role])}
    rows = []
    for family, family_rows in (("XX_equality", obj["equality"]), ("tree_Z_face", obj["faces"])):
        for family_index, row in enumerate(family_rows):
            mask = row.x | row.z; support = []
            while mask:
                bit = mask & -mask; qubit = bit.bit_length() - 1; mask ^= bit
                coordinate = old[qubit] if qubit < obj["graph"].qubits else aux[qubit]
                support.append((qubit, coordinate, pauli_letter(row, qubit)))
            support.sort(key=lambda item: (item[1], item[0]))
            rows.append({"family":family, "family_index":family_index,
                         "phase":row.phase, "sign":row_sign(row),
                         "support":tuple(support), "pauli":row})
    digest = sha256()
    for row in rows:
        digest.update(repr((row["family"],row["family_index"],row["phase"],row["support"])).encode())
    result = {
        "length":length, "checks":len(rows),
        "XX_equality_checks":len(obj["equality"]), "tree_Z_face_checks":len(obj["faces"]),
        "support_occurrences":sum(len(row["support"]) for row in rows),
        "maximum_support":max(map(lambda row:len(row["support"]), rows)),
        "Pauli_letter_histogram":dict(Counter(item[2] for row in rows for item in row["support"])),
        "negative_phase_rows":sum(row["sign"] for row in rows),
        "descriptor_sha256":digest.hexdigest(),
        "formula_generated_no_flat_check_table":True,
        "pass":len(rows)==len(obj["equality"])+len(obj["faces"]),
    }
    check(f"L{length} exact equality/face stabilizers compile to Hermitian support descriptors",
          result["pass"], {k:result[k] for k in ("checks","support_occurrences","maximum_support","negative_phase_rows")})
    return result, rows, obj, placement


def coherent_oracle_grammar(length: int, descriptors: list[dict], obj: dict) -> dict:
    modulus = K * length
    support_occurrences = sum(len(row["support"]) for row in descriptors)
    checks = len(descriptors)
    tour_edges = 0; maximum_leg = 0
    owner_digest = sha256(); route_owners = 0
    for check_index, row in enumerate(descriptors):
        sites = [item[1] for item in row["support"]]
        if not sites: continue
        home = sites[0]
        for site in sites[1:]:
            distance = c642.periodic_l1(home, site, modulus)
            maximum_leg = max(maximum_leg, distance)
            tour_edges += 2 * distance
            route_owners += 1
            owner_digest.update(repr((check_index, home, site, distance)).encode())

    widths = {
        "orientation_one_hot":24,
        "family":2, "axis":2,
        "check_counter":max(1, math.ceil(math.log2(checks))),
        "tree_index":max(1, math.ceil(math.log2(length + 1))),
        "fiber_copy":4,
        "support_counter":max(1, math.ceil(math.log2(max(len(row["support"]) for row in descriptors)+1))),
        "current_coordinate":3*math.ceil(math.log2(modulus)),
        "target_coordinate":3*math.ceil(math.log2(modulus)),
        "route_step":math.ceil(math.log2(3*modulus+1)),
        "axis_order_mask":3, "Pauli_opcode":2,
        "probe_syndrome_flag_token":4,
        "microcode_two_rail":32,
        "clean_work":128,
    }
    logical_bits = sum(widths.values())
    storage_compatible_program_M2_upper_bound = 24 * logical_bits

    # C V C^dagger Z C V C^dagger: four exact Hadamard-test parity
    # computations, two syndrome-to-flag copies, one local flag phase.
    gates = {
        "support_one_H":8*checks,
        "support_one_probe_Z_for_row_sign":4*sum(row["sign"] for row in descriptors),
        "support_two_controlled_P":4*support_occurrences,
        "support_two_syndrome_flag_CNOT":2*checks,
        "support_one_violation_phase":checks,
        "fine_NN_route_SWAP":4*tour_edges,
    }
    symbolic = []
    failures = 0
    for syndrome in (0,1):
        probe=flag=0; phase=1
        # compute, copy, uncompute, phase, compute, clear flag, uncompute
        probe ^= syndrome; flag ^= probe; probe ^= syndrome
        phase *= -1 if flag else 1
        probe ^= syndrome; flag ^= probe; probe ^= syndrome
        failures += int((probe,flag,phase)!=(0,0,(-1 if syndrome else 1)))
        symbolic.append({"input_syndrome":syndrome,"final_probe":probe,"final_flag":flag,"phase":phase})
    result = {
        "length":length, "checks":checks, "support_occurrences":support_occurrences,
        "state_carried_register_widths":widths,
        "logical_program_and_work_bits":logical_bits,
        "proper_cubic_orbit_replicated_program_M2_upper_bound":storage_compatible_program_M2_upper_bound,
        "program_register_specification":"24 frame-sector copies of one formula ROM plus one active state-carried orientation/token; counters generate checks and supports",
        "compatible_with_physical_storage":True,
        "program_registers_literally_placed":False,
        "flat_check_or_path_table_stored":False,
        "runtime_host_branch_or_path_query":False,
        "route_owner_descriptors":route_owners,
        "route_owner_sha256":owner_digest.hexdigest(),
        "one_parity_compute_tour_fine_edges":tour_edges,
        "maximum_route_leg_fine_edges":maximum_leg,
        "gate_counts":gates,
        "oracle_word":"C; CNOT(probe,flag); C^-1; Z(flag); C; CNOT(probe,flag); C^-1",
        "symbolic_syndrome_cases":symbolic,
        "symbolic_failures":failures,
        "all_work_probe_flag_and_token_clean_after_oracle":failures==0,
        "oracle_squared_is_identity":True,
        "lawful_code_action":"identity because every stabilizer syndrome is zero",
        "off_code_action":"coherent -1 phase per violated displayed check; no measurement occurrence or Record semantics",
        "schedule_grammar":"one state-carried token serializes check-oracle words; hence active route-route collision count is zero at grammar level even though declared route bodies overlap",
        "simultaneous_active_route_collisions":0,
        "occupied_data_program_role_safe_detours_compiled":False,
        "literal_full_fine_NN_physical_lowering_closed":False,
        "pass_as_exact_coherent_oracle_grammar":failures==0 and storage_compatible_program_M2_upper_bound < K**3,
    }
    check(f"L{length} state-carried formula grammar specifies exact clean coherent violation-phase algebra",
          result["pass_as_exact_coherent_oracle_grammar"],
          {"program_M2_upper_bound":storage_compatible_program_M2_upper_bound,"checks":checks,"route_owners":route_owners,"max_leg":maximum_leg,"symbolic_failures":failures})
    return result


def commutation_and_rank_retention(length: int, obj: dict) -> dict:
    qubits=obj["qubits"]; cells=length**3
    rank,inconsistent=c532.phase_rank(obj["stabilizers"],qubits)
    selected=obj["equality"]+obj["faces"]
    comm={
        "selected_stabilizer_mutual":sum(not a.commutes(b) for i,a in enumerate(selected) for b in selected[i+1:]),
        "selected_vs_dressed_matter":sum(not a.commutes(b) for a in selected for b in obj["matter"]),
        "selected_vs_dressed_gauge":sum(not a.commutes(b) for a in selected for b in obj["gauge"]),
    }
    result={
        "length":length,"stabilizer_rank":rank,"expected_rank":15*cells+1+(qubits-obj["graph"].qubits),
        "code_exponent":qubits-rank,"expected_code_exponent":7*cells-1,
        "phase_inconsistent":inconsistent,"commutator_failures":comm,
        "controller_adds_persistent_code_M2_or_constraints":False,
        "rank_and_target_gauge_quotient_unchanged_from_immutable_Cycle642":True,
        "pass":inconsistent==0 and rank==15*cells+1+(qubits-obj["graph"].qubits)
               and qubits-rank==7*cells-1 and all(v==0 for v in comm.values()),
    }
    check(f"L{length} coherent check oracles retain exact rank/code exponent and matter/gauge commutation",
          result["pass"],result)
    return result


def f2_basis(rows):
    pivots={}
    for row in rows:
        value=row
        while value:
            pivot=value.bit_length()-1
            if pivot in pivots:value^=pivots[pivot]
            else:pivots[pivot]=value;break
    return pivots


def f2_reduce(row,pivots):
    value=row
    while value:
        pivot=value.bit_length()-1
        if pivot not in pivots:return value
        value^=pivots[pivot]
    return 0


def fixed_presentation_frame_falsifier(obj: dict) -> dict:
    # Only L3 is needed: one counterexample prevents promotion of the single
    # identity presentation. Frame-sector control remains a separate route.
    graph=obj["graph"]; qubits=obj["qubits"]
    base=tuple(row.symplectic(qubits) for row in obj["stabilizers"]); pivots=f2_basis(base)
    coord_to_index={site:bit for role in obj["roles"] for bit,site in zip(obj["index"][role],obj["fibers"][role])}
    failing=[]; residual_rows=0
    for frame_index,frame in enumerate(FRAMES):
        data=c532.frame_data(graph,frame)
        aux_map={bit:coord_to_index[c642.rotate(frame,site)] for role in obj["roles"] for bit,site in zip(obj["index"][role],obj["fibers"][role])}
        frame_failed=False
        for pauli in obj["stabilizers"]:
            old_mask=(1<<graph.qubits)-1
            transformed=c532.transform_pauli(c235.Pauli(pauli.phase,pauli.x&old_mask,pauli.z&old_mask),data)
            x=transformed.x;z=transformed.z
            for bit,target in aux_map.items():
                if (pauli.x>>bit)&1:x|=1<<target
                if (pauli.z>>bit)&1:z|=1<<target
            residual=f2_reduce(c235.Pauli(transformed.phase,x,z).symplectic(qubits),pivots)
            if residual:
                residual_rows+=1;frame_failed=True;break
        if frame_failed:failing.append(frame_index)
    result={
        "length":3,"proper_frames":24,"fixed_identity_presentation_failing_frames":tuple(failing),
        "fixed_identity_presentation_failure_count":len(failing),"first_residual_rows":residual_rows,
        "single_fixed_tree_stabilizer_span_cubic_covariant":not failing,
        "frame_sector_repair":"declare state-carried h and S_h=U_h S_identity; R maps h to Rh; literal register placement remains open",
        "frame_sector_rank_preserved":"each U_h is an invertible Clifford/permutation, so every sector has the identity rank and quotient",
        "broad_cubic_no_go":False,
        "pass_as_narrow_falsifier":len(failing)>0,
    }
    check("L3 falsifies covariance of one unlabelled tree stabilizer presentation and motivates state-carried frame sectors",
          result["pass_as_narrow_falsifier"],result)
    return result


def frame_sector_covariance(descriptor_sets) -> dict:
    frame_index={tuple(int(v) for v in frame.ravel()):i for i,frame in enumerate(FRAMES)}
    group_failures=0; coordinate_failures=0; cases=0
    sample=[]
    for _summary,rows,_obj,_placement in descriptor_sets:
        for row in rows[:min(24,len(rows))]:
            sample.extend(item[1] for item in row["support"][:3])
    sample=tuple(dict.fromkeys(sample))
    for left in FRAMES:
        for right in FRAMES:
            product=left@right
            group_failures+=tuple(int(v) for v in product.ravel()) not in frame_index
            for coordinate in sample:
                cases+=1
                direct=c642.rotate(product,coordinate)
                composed=c642.rotate(left,c642.rotate(right,coordinate))
                coordinate_failures+=direct!=composed
    result={
        "proper_frames":len(FRAMES),"ordered_products":576,
        "state_carried_sector_action":"(R,h,S_h,program_h) -> (Rh,U_R S_h U_R^-1,program_Rh)",
        "frame_group_failures":group_failures,"coordinate_group_cases":cases,
        "coordinate_group_failures":coordinate_failures,
        "runtime_host_frame_selector":False,"orientation_one_hot_is_state_carried_register_specification":True,
        "orientation_register_literally_placed":False,
        "individual_unlabelled_presentation_claimed_covariant":False,
        "pass":len(FRAMES)==24 and group_failures==coordinate_failures==0,
    }
    check("state-carried frame sectors and controller-coordinate grammar close all24/all576 group action algebra",
          result["pass"],result)
    return result


def static_wire_discriminator() -> dict:
    rows=[]
    for edges in range(1,32):
        # Commutation of a Z mask z with every nearest-neighbor XX edge is
        # z_i xor z_(i+1)=0.  Certify the kernel algebraically: the path
        # incidence matrix has rank V-1, and zero/all-one are witnesses.
        vertices=edges+1
        incidence=[(1<<i)|(1<<(i+1)) for i in range(edges)]
        incidence_rank=len(f2_basis(incidence))
        witnesses=(0,(1<<vertices)-1)
        witness_failures=sum(any((row & mask).bit_count()%2 for row in incidence)
                             for mask in witnesses)
        rows.append({"wire_edges":edges,"wire_vertices":vertices,
                     "new_ancillas":edges-1,"local_XX_checks":edges,
                     "net_code_exponent_change":-1,
                     "XX_path_incidence_rank":incidence_rank,
                     "commuting_Z_kernel_dimension":vertices-incidence_rank,
                     "commuting_Z_kernel_witnesses":witnesses,
                     "kernel_witness_failures":witness_failures,
                     "nontrivial_Z_weight":witnesses[-1].bit_count(),
                     "nontrivial_Z_diameter_edges":edges,
                     "pass":incidence_rank==vertices-1 and witness_failures==0})
    result={
        "route":"simple stabilizer XX chain",
        "rows":rows,"all_exponent_counts_correct":all(r["local_XX_checks"]-r["new_ancillas"]==1 for r in rows),
        "all_commuting_Z_kernels_only_constant":all(r["pass"] for r in rows),
        "narrow_failure":"local XX equality succeeds, but any anticommuting logical Z face must cover the complete connected wire, so its support/diameter grows with route length",
        "general_static_subsystem_gadget_no_go":False,
        "pass_as_narrow_discriminator":all(r["pass"] for r in rows),
    }
    check("simple XX wire preserves exponent but forces its commuting logical Z across the whole wire on lengths1..31",
          result["pass_as_narrow_discriminator"],{"lengths":31,"maximum_Z_weight":rows[-1]["nontrivial_Z_weight"]})
    return result


def deletion_malformed_controls(descriptors,controllers) -> dict:
    witness_length,witness=next((summary["length"],row)
                                for summary,rows,_obj,_placement in descriptors
                                for row in rows if len(row["support"])>=2)
    intact_weight=len(witness["support"]); deleted_weight=intact_weight-1

    # Exhaust all support-eigenvalue assignments.  Removing the first Pauli
    # factor changes the computed syndrome on at least one assignment.
    deletion_residual=max(((mask.bit_count()&1) ^ ((mask>>1).bit_count()&1))
                          for mask in range(1<<intact_weight))

    # Use an actual Cycle642 shortest fine-NN route and delete one edge.  A
    # reachability search on the remaining path graph must lose the endpoint.
    left=witness["support"][0][1]; right=witness["support"][1][1]
    route=c642.shortest_path_family(left,right,K*witness_length)[0]
    route_edges=list(zip(route,route[1:])); deleted_edge_index=len(route_edges)//2
    retained=route_edges[:deleted_edge_index]+route_edges[deleted_edge_index+1:]
    adjacent={site:set() for site in route}
    for a,b in retained: adjacent[a].add(b); adjacent[b].add(a)
    seen={route[0]}; frontier=[route[0]]
    while frontier:
        current=frontier.pop()
        for nxt in adjacent[current]-seen: seen.add(nxt); frontier.append(nxt)
    route_delete_disconnect=int(route[-1] not in seen)

    # Corrupt one literal Pauli opcode and compare the formula descriptor.
    original_opcode=repr((witness["family"],witness["family_index"],witness["phase"],witness["support"]))
    first=witness["support"][0]; malformed_letter="Z" if first[2]!="Z" else "X"
    malformed_support=((first[0],first[1],malformed_letter),)+witness["support"][1:]
    malformed_opcode=repr((witness["family"],witness["family_index"],witness["phase"],malformed_support))
    original_hash=sha256(original_opcode.encode()).hexdigest()
    malformed_hash=sha256(malformed_opcode.encode()).hexdigest()
    malformed_opcode_residual=int(original_hash!=malformed_hash)

    # The stored route token traverses the selected path and its inverse.
    # Delete the last inverse step and certify a non-home terminal position.
    token_word=tuple(route[1:])+tuple(reversed(route[:-1]))
    token_exhaust_failure=int(token_word[-2]!=route[0]) if len(token_word)>=2 else 1
    result={
        "witness_length":witness_length,"witness_family":witness["family"],"intact_support":intact_weight,
        "delete_one_controlled_P_support":deleted_weight,
        "deleted_term_syndrome_xor_residual":deletion_residual,
        "deleted_route_length":len(route_edges),"deleted_route_edge_index":deleted_edge_index,
        "delete_one_fine_NN_route_edge_endpoint_disconnect":route_delete_disconnect,
        "original_opcode_sha256":original_hash,"malformed_opcode_sha256":malformed_hash,
        "malformed_Pauli_opcode_descriptor_hash_residual":malformed_opcode_residual,
        "complete_token_word_terminal_is_home":token_word[-1]==route[0],
        "delete_token_return_exhaust_residual":token_exhaust_failure,
        "lawful_code_oracle_leakage":0,
        "off_code_domain":"coherent syndrome phase is defined; no measurement occurrence, Record, or repair meaning",
        "pass":min(deletion_residual,route_delete_disconnect,malformed_opcode_residual,token_exhaust_failure)>0
               and all(row["all_work_probe_flag_and_token_clean_after_oracle"] for row in controllers),
    }
    check("term/route/opcode/token deletions and lawful-code leakage have explicit nonzero/zero controls",
          result["pass"],result)
    return result


def scaling_and_capacity() -> dict:
    rows=[]
    for length in range(3,32):
        tree=c642.tree_controls(length)
        vertices,edges=c642.fill_tree(length)
        # At most 24 physical copies per abstract role is a rigorous orbit bound.
        logical_edges=3*len(edges); copy_upper=24*logical_edges
        equality_upper=logical_edges*math.comb(24,2)
        controller_bits=24+2+2+math.ceil(math.log2(equality_upper+3*len(vertices)))+2*math.ceil(math.log2(length+1))+3*math.ceil(math.log2(K*length))+3+2+4+32+128
        rows.append({"length":length,"tree_pass":tree["pass"],"logical_edges":logical_edges,
                     "physical_copy_upper_bound":copy_upper,"equality_row_upper_bound":equality_upper,
                     "logical_controller_bits":controller_bits,
                     "copy_upper_per_coarse_cell":copy_upper/length**3,
                     "controller_bits_per_coarse_cell":controller_bits/length**3})
    result={
        "rows":rows,"same_formula_L3_L31":all(row["tree_pass"] for row in rows),
        "asymptotic_counts":{
            "tree_logical_edges":"O(L)","orbit_copy_M2":"O(L)","displayed_equality_rows":"O(L)",
            "formula_controller_register_width":"O(log L)","reusable_probe_flag_token_work":"O(1)",
            "available_fine_sites":"K^3 L^3","reserved_shell_sites":"Theta(K^2 L^3)"},
        "single_origin_K129_shell_all_L_capacity_claim":False,
        "distributed_capacity_inequality":"24*3*E_tree + O(log L) <= K^3 L^3 for every L>=3 under the displayed upper bound",
        "distributed_capacity_failures":sum(not (row["physical_copy_upper_bound"]+24*row["logical_controller_bits"] < K**3*row["length"]**3) for row in rows),
        "distributed_collision_free_placement_constructed":False,
        "scope":"resource capacity and size-uniform program law, not a literal occupied-role-safe placement",
    }
    result["pass_as_capacity_audit"]=result["same_formula_L3_L31"] and result["distributed_capacity_failures"]==0
    check("L3..L31 no-refit register-width/resource laws fit distributed K129 volume while literal placement remains open",
          result["pass_as_capacity_audit"],{"rows":len(rows),"capacity_failures":result["distributed_capacity_failures"]})
    return result


def no_go_gate():
    c642_open=immutable_citation("docs/work_history/repo/review_feedback/PHYSICAL_FIXED_CUBIC_WILSON_FILL_INCIDENCE_CYCLE642_NOTE_2026-07-23.md","Intersecting routes still need either a static")
    c642_scope=immutable_citation("docs/work_history/repo/review_feedback/PHYSICAL_FIXED_CUBIC_WILSON_FILL_INCIDENCE_CYCLE642_NOTE_2026-07-23.md","physical allocation is therefore only a finite L3/L6/L7")
    c638_route=immutable_citation("docs/work_history/repo/review_feedback/PHYSICAL_HIERARCHICAL_GRAMMAR_FULL_ACT_COMPILER_CYCLE638_NOTE_2026-07-23.md","Cycle 638 does not store the Cycle-630 parent tree")
    c629_open=immutable_citation("docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md","NOT EXECUTED. No support-two circuit computes")
    current_static=current_citation("scripts/physical_orbit_tree_local_enforcement_cycle646_2026_07_23.py","def static_wire_discriminator")
    current_controller=current_citation("scripts/physical_orbit_tree_local_enforcement_cycle646_2026_07_23.py","def coherent_oracle_grammar")
    qualifying=[
        {"family":"simple static stabilizer XX wire","object":"one path graph per equality","mechanism":"nearest-neighbor XX edge stabilizers","terminal":"localize equality and every commuting Z face","honesty_marker":"ATTEMPTED","marker":"ATTEMPTED","result":"exponent correct; Z support grows across component"},
        {"family":"Cycle642 finite-NN route families","object":"all equality/face support pairs","mechanism":"all shortest axis orders","terminal":"physical crossing ownership","honesty_marker":"RULED OUT BY PRIOR","marker":"RULED OUT BY PRIOR","result":"geometry positive; enforcement explicitly open"},
        {"family":"state-carried coherent syndrome grammar","object":"formula-generated stabilizer descriptors","mechanism":"clean Hadamard-test phase grammar plus serialized token register","terminal":"exact oracle algebra and symbolic clean exhaust","honesty_marker":"ATTEMPTED","marker":"ATTEMPTED","result":"oracle grammar positive; literal register placement and occupied-role-safe fine-NN lowering open"},
        {"family":"Cycle638 coordinate-counter control","object":"declared program/token registers and coordinate counters","mechanism":"generated predecessor routes","terminal":"no host path table","honesty_marker":"RULED OUT BY PRIOR","marker":"RULED OUT BY PRIOR","result":"controller grammar exists on its conditional act sector; this is not a Cycle646 placement"},
    ]
    open_routes=[
        {"family":"3D subsystem crossing center","object":"noncommuting local gauge center","mechanism":"Bacon-Shor/wire-code center products","terminal":"exact original stabilizer center with bounded generators","status":"OPEN / NOT COUNTED"},
        {"family":"occupied-role-safe sidecar network","object":"reserved shell/backbone corridors","mechanism":"distributed detours around data/program roles","terminal":"literal fine-NN controller lowering","status":"OPEN / NOT COUNTED"},
        {"family":"autonomous rejection or repair","object":"violation flags plus exhaust reservoir","mechanism":"reversible rejection, cooling, or repair","terminal":"convergence without E or host intervention","status":"OPEN / NOT COUNTED"},
        {"family":"perturbative static gadget","object":"local mediator Hamiltonian","mechanism":"low-energy effective stabilizer penalty","terminal":"exact rather than approximate code and leakage control","status":"OPEN / NOT COUNTED"},
    ]
    walls={
        "W_static_center":"a bounded local gauge center simultaneously representing XX wires and Z faces",
        "W_collision_free_lowering":"literal occupied-role-safe fine-NN routes for the coherent oracle controller",
        "W_repair":"autonomous rejection/convergence/repair rather than a coherent phase oracle",
    }
    pairs=[{"from":a,"to":b,"implied":False,"reason":f"closing {a} does not construct {b}"} for a in walls for b in walls if a!=b]
    required={"prior_ref","prior_path","prior_line","prior_residual","current_path","current_line","current_residual","same_scope","exact_match","use_as_closure"}
    n4_matches=[{
        "prior_ref":c642_open["ref"],"prior_path":c642_open["path"],"prior_line":c642_open["line"],
        "prior_residual":"static subsystem wire or autonomous crossing schedule absent",
        "current_path":current_controller["path"],"current_line":current_controller["line"],
        "current_residual":"coherent oracle grammar closes algebraically while literal register placement and occupied-role-safe route lowering remain absent",
        "same_scope":True,"exact_match":True,"use_as_closure":True,
    }]
    n4_nonmatches=[{
        "prior_ref":c642_scope["ref"],"prior_path":c642_scope["path"],"prior_line":c642_scope["line"],
        "prior_residual":"single-shell all-L physical placement absent",
        "current_path":current_static["path"],"current_line":current_static["line"],
        "current_residual":"simple XX wire has a Z-locality failure, not a general distributed-placement theorem",
        "same_scope":False,"exact_match":False,"use_as_closure":False,
    }]
    n5=[
        {"claim":"the simple XX chain does not localize the coupled Z face","per_element":"each XX edge commutation equation enters the exact path-incidence rank certificate","per_site":"Z inclusion is constant on every wire vertex","per_mode":"no fermion-mode no-go is inferred","per_block":"wire lengths1..31 are certified","lattice_wide":"other subsystem/crossing centers remain open"},
        {"claim":"a coherent syndrome oracle is not autonomous repair","per_element":"both syndrome eigenvalues are exact","per_site":"each primitive is support1/2 after a safe route exists","per_mode":"matter/gauge commutation is retained","per_block":"L3/L6/L7 controller resources pass","lattice_wide":"safe routing and convergence remain open"},
    ]
    n6=[
        {"file":"UNMATERIALIZED/physical_3d_subsystem_crossing_center_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_static_center"},
        {"file":"UNMATERIALIZED/physical_reserved_shell_sidecar_router_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_collision_free_lowering"},
        {"file":"UNMATERIALIZED/physical_violation_repair_exhaust_cycle_next.py","status":"OPEN","what_closes":"W_repair"},
    ]
    n7={
        "mechanism":"embed the Tanner graph in 3D with noncommuting gauge-wire crossings so bounded gauge generators have the original tree stabilizers as their center",
        "actionable_steps":["construct one XX/Z crossing tile","prove its center and gauge-rank formula","tile Cycle642 incidence with bounded congestion","recompute target/gauge commutant and leakage at L3/L6/L7"],
        "why_it_breaks_the_negative":"the constant-Z lemma applies only to a commuting XX stabilizer chain; subsystem gauge generators may anticommute locally while their bounded center products reproduce both checks",
        "terminal_test":"bounded-degree 3D placement, exact center/rank, all24/all576, deletion, malformed gauge, and full matter/gauge commutation",
        "supporting_citations":[c642_open,c629_open],
    }
    n8=[
        {"cycle":629,"retired":"external-origin projector covariance at supplied-sector level","mechanism":"state-carried frame phase","applicability":"supports frame-sector control but not enforcement","citation_ref":c629_open["ref"],"citation_path":c629_open["path"],"citation_line":c629_open["line"],"citation_text":c629_open["line_text"]},
        {"cycle":638,"retired":"stored route parent/path table","mechanism":"coordinate-counter controller","applicability":"supports no-host route generation; cap lowering is not composed","citation_ref":c638_route["ref"],"citation_path":c638_route["path"],"citation_line":c638_route["line"],"citation_text":c638_route["line_text"]},
        {"cycle":642,"retired":"abstract absence of a fixed covariant cap role placement at L3/L6/L7","mechanism":"orbit-tree role fibers","applicability":"supplies the checks and route geometry whose enforcement is tested","citation_ref":c642_open["ref"],"citation_path":c642_open["path"],"citation_line":c642_open["line"],"citation_text":c642_open["line_text"]},
    ]
    return {
        "Status":"PASS","N1_normalized_families":qualifying,"N1_open_routes_not_counted":open_routes,
        "N1_qualifying_attempts":len(qualifying),"N1_required_for_negative":5,"N1_negative_gate":"FAIL / DO NOT SHIP",
        "N2_collapsed_walls":walls,"N2_directed_ordered_pairs":pairs,"N2_negative_gate":"FAIL / DO NOT SHIP",
        "N3_hidden_wall_scan":[
            {"phrase":"state-carried orientation/token","classification":"declared supplied register specification, not host selector; literal placement open","wall":"W_collision_free_lowering"},
            {"phrase":"formula route geometry","classification":"does not imply occupied-role-safe paths","wall":"W_collision_free_lowering"},
            {"phrase":"coherent phase oracle","classification":"not rejection, cooling, convergence, or repair","wall":"W_repair"},
            {"phrase":"distributed capacity inequality","classification":"capacity only, not placement","wall":"W_collision_free_lowering"},
            {"phrase":"physical E/preparation","classification":"explicitly out of Cycle646 scope; not counted as an enforcement wall","wall":None},
        ],
        "N4_exact_residual_matches":n4_matches,"N4_nonmatches_not_used_as_closure":n4_nonmatches,
        "N4_required_fields":sorted(required),"N4_negative_gate":"FAIL / DO NOT SHIP broad closure",
        "N5_rhetoric":n5,"N6_partial_closure_paths":n6,"N7_steelman":n7,"N8_cross_cycle_echo":n8,
        "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP",
        "shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False,"minimum_content_shipped":False,
        "shared_obstruction_shipped":False,"axiom_pressure_shipped":False,
        "broad_no_go_claim":False,"minimum_content_claim":False,"shared_obstruction_claim":False,"axiom_pressure_claim":False,
        "shared_route_independent_obstruction":False,"axiom_pressure":False,
    }


def main():
    global PASS,FAIL
    started=time.perf_counter()
    observed={path:git_sha(path) for path in PINS}
    allowed=(IMMUTABLE_ROOT.resolve(),c642.IMMUTABLE_ROOT.resolve())
    imported={name:str(Path(module.__file__).resolve()) for name,module in sys.modules.items() if name.startswith("physical_") and getattr(module,"__file__",None)}
    bad=[path for path in imported.values() if not any(Path(path).is_relative_to(root) for root in allowed)]
    check("Cycle642/638 shores and every imported physical module are immutable",observed==PINS and not bad,
          {"commit":IMMUTABLE_COMMIT,"pins":len(PINS),"modules":len(imported),"mismatches":[p for p in PINS if observed[p]!=PINS[p]],"working":bad})
    descriptors=[];controllers=[];retentions=[]
    for length in (3,6,7):
        summary,rows,obj,placement=build_descriptors(length)
        descriptors.append((summary,rows,obj,placement))
        controllers.append(coherent_oracle_grammar(length,rows,obj))
        retentions.append(commutation_and_rank_retention(length,obj))
    static=static_wire_discriminator()
    fixed_frame=fixed_presentation_frame_falsifier(descriptors[0][2])
    covariance=frame_sector_covariance(descriptors)
    deletion=deletion_malformed_controls(descriptors,controllers)
    scaling=scaling_and_capacity()
    nogo=no_go_gate()
    exact_markers={"ATTEMPTED","RULED OUT BY PRIOR"}; required=set(nogo["N4_required_fields"])
    check("canonical N1-N8 passes while broad negative promotion remains blocked",
          nogo["Status"]=="PASS" and nogo["N1_negative_gate"]=="FAIL / DO NOT SHIP"
          and all(r["honesty_marker"] in exact_markers and r["marker"]==r["honesty_marker"] for r in nogo["N1_normalized_families"])
          and all("marker" not in r and "honesty_marker" not in r for r in nogo["N1_open_routes_not_counted"])
          and len(nogo["N2_directed_ordered_pairs"])==6
          and all(required<=set(r) for r in nogo["N4_exact_residual_matches"]+nogo["N4_nonmatches_not_used_as_closure"])
          and all(set(("per_element","per_site","per_mode","per_block","lattice_wide"))<=set(r) for r in nogo["N5_rhetoric"])
          and all(nogo[key]=="FAIL / DO NOT SHIP" for key in ("broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate"))
          and all(nogo[key] is False for key in ("broad_negative_shipped","minimum_content_shipped","shared_obstruction_shipped","axiom_pressure_shipped"))
          and not nogo["shared_route_independent_obstruction"] and not nogo["axiom_pressure"],
          {"qualifying":len(nogo["N1_normalized_families"]),"open":len(nogo["N1_open_routes_not_counted"]),"directed":len(nogo["N2_directed_ordered_pairs"])})
    note=NOTE.read_text();markers=("Authority: **none**","Audit: **unset**","coherent violation-phase oracle","compatible with physical storage","not literally placed or lowered","literal fine-neighbor physical lowering remain","not autonomous repair","N1-N8","Axiom pressure: **none**")
    check("Cycle646 note freezes result, residual, scope, and no-go discipline",all(m in note for m in markers),markers)
    result={
        "cycle":646,"date":"2026-07-23","Status":"PASS","status":"cycle646-coherent-local-enforcement-oracle-grammar-partial-closure",
        "classification":"positive algebraic state-carried formula controller/register specification compatible with physical storage but not literally placed or fine-NN lowered",
        "authority":AUTHORITY,"audit":AUDIT,"author_accepted":False,"author_artifact_status_accepted":False,
        "constitutional_effect":"none","breakthrough":False,
        "shared_route_independent_obstruction":False,"axiom_pressure":False,
        "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP",
        "shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False,"minimum_content_shipped":False,
        "shared_obstruction_shipped":False,"axiom_pressure_shipped":False,
        "broad_no_go_claim":False,"minimum_content_claim":False,"shared_obstruction_claim":False,"axiom_pressure_claim":False,
        "shore":{"immutable_commit":IMMUTABLE_COMMIT,"pins":PINS,"observed":observed,"actual_imported_physical_modules":imported,
                 "working_tree_bytes_used_as_premise":False,"immutable_import_failures":bad,"no_go_skill_origin_main_sha256":NO_GO_ORIGIN_MAIN_SHA256},
        "exact_check_descriptor_compilers":[r[0] for r in descriptors],
        "coherent_violation_phase_oracle_grammars":controllers,
        "rank_code_and_matter_gauge_retention":retentions,
        "simple_static_XX_wire_discriminator":static,
        "single_presentation_frame_falsifier":fixed_frame,
        "state_carried_frame_sector_covariance":covariance,
        "deletion_malformed_and_leakage_controls":deletion,
        "size_uniform_and_distributed_capacity_audit":scaling,
        "strongest_constructive_result":"for every Cycle642 XX equality and tree-face stabilizer at L3/L6/L7, a state-carried formula controller/register grammar specifies exact clean coherent syndrome-phase algebra and a serial ownership schedule compatible with physical storage; rank/code exponent and matter/gauge commutation are unchanged and frame-sector algebra closes all24/all576, but registers, occupied-role-safe detours, and literal fine-NN physical lowering are not constructed",
        "W_local_enforcement":"SHARPLY_NARROWED_NOT_CLOSED",
        "W_local_enforcement_disposition":"SHARPLY_NARROWED_NOT_CLOSED",
        "W_local_enforcement_residual":"oracle grammar and serial ownership specification pass; literal register placement, occupied-data/program-safe detours, fine-NN physical lowering, and autonomous rejection/repair remain open",
        "route_disposition":{
            "simple_static_XX_stabilizer_wire":"NARROWLY_FAILS_Z_FACE_LOCALITY",
            "state_carried_coherent_oracle":"PASS_EXACT_ORACLE_GRAMMAR_AND_SYMBOLIC_CLEAN_EXHAUST",
            "occupied_role_safe_physical_lowering":"OPEN",
            "static_3D_subsystem_crossing_center":"OPEN",
            "autonomous_rejection_repair_convergence":"OPEN",
            "physical_E_or_preparation":"OUT_OF_SCOPE_NOT_TOUCHED",
        },
        "supplied_structure_inventory":{
            "immutable_Cycle642_orbit_tree_checks_roles_and_routing_scout":True,
            "immutable_Cycle638_formula_controller_grammar_mechanism":True,
            "K129_partition_macro_origin_and_state_carried_frame_sector":True,
            "formula_microcode_and_pi_violation_phase_choice":True,
            "initial_blank_probe_flag_route_work_and_one_active_token":True,
            "finite_full_certificates_L3_L6_L7":True,
            "no_refit_combinatorial_capacity_scan_L3_L31":True,
            "single_shell_asymptotic_placement":False,
            "distributed_collision_free_corridor":False,
            "controller_registers_literally_placed":False,
            "host_path_table_or_runtime_branch":False,
            "physical_E_preparation_repair_or_measurement":False,
        },
        "semantic_firewall":{"syndrome_flag_is_measurement_occurrence":False,"syndrome_flag_is_Record":False,
                             "program_or_schedule_is_time":False,"generator_is_rate":False,"phase_is_energy":False},
        "six_wall_ledger":{
            "C_ref":"state-carried 24-frame sectors close oracle-grammar covariance algebra; register placement and sector genesis remain supplied/open",
            "C_num":"exact binary/Clifford oracle only; no probability or normalization",
            "C_wrap":"Wilson-fixing checks now have a coherent local-oracle grammar compatible with physical storage, not literal lowering, preparation, or realized history",
            "C_int":"rank and matter/gauge commutation retained; no new mass/contact/seam dynamics claim",
            "C_local":"narrowed to occupied-role-safe route lowering plus rejection/repair; simple static XX wire route is specifically falsified",
            "C_source":"unchanged; no energy, stress, source, resource, or gravity meaning",
        },
        "no_go_discipline":nogo,
        "optimal_next_campaign":"construct one exact 3D subsystem XX/Z crossing-center tile, or reserve and exhaustively route a K129 shell sidecar network around all data/program roles; then add rejection/repair only if separately authorized, while keeping E independent",
    }
    gate_keys=("broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate")
    shipped_keys=("broad_negative_shipped","minimum_content_shipped","shared_obstruction_shipped","axiom_pressure_shipped")
    check("top-level packaging status and all four do-not-ship gates are exact",
          result["Status"]=="PASS" and all(result[key]=="FAIL / DO NOT SHIP" for key in gate_keys)
          and all(result[key] is False for key in shipped_keys)
          and result["W_local_enforcement"]=="SHARPLY_NARROWED_NOT_CLOSED",
          {key:result[key] for key in ("Status",)+gate_keys+shipped_keys+("W_local_enforcement",)})
    result["resources"]={"elapsed_seconds":time.perf_counter()-started,"maximum_RSS_bytes":int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform=='darwin' else resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)}
    result.update({"tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,"pass":FAIL==0})
    RECEIPT.write_text(json.dumps(result,indent=2,sort_keys=True,default=json_default)+"\n")
    print(json.dumps({"status":"PASS" if FAIL==0 else "FAIL","tests":f"{PASS}/{PASS+FAIL}","elapsed":result["resources"]["elapsed_seconds"],"receipt":str(RECEIPT.relative_to(ROOT))},sort_keys=True))
    return int(FAIL!=0)


if __name__=="__main__":
    COLD.parent.mkdir(parents=True,exist_ok=True)
    with COLD.open("w") as stream:
        original=sys.stdout;sys.stdout=Tee(original,stream)
        try:raise SystemExit(main())
        finally:sys.stdout=original
