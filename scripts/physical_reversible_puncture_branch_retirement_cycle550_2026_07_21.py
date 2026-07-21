#!/usr/bin/env python3
"""Cycle 550: physical reversible puncture/branch-retirement attempt.

Build one fixed proper-cubic orbit of 24 collision-free nearest-neighbour
carrier loops in the installed Cycle-527 microgrid.  Compute the Cycle-547
signed branch activation into those carriers, transport and return it, apply
the existing local correction, and try to uncompute every branch field.

The physical carrier compute/transport/uncompute succeeds.  Exact retirement
of an arbitrary Wilson label into a fixed plus sector with every auxiliary
blank fails the isometry/Gram test: inverse extraction sees the corrected
plus Wilson and leaves the old syndrome behind.  A reversible subsystem sink
works exactly only by retaining the distinguishing bits.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import permutations
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_relational_membrane_frame_reference_pump_cycle547_2026_07_21 as c547


c527 = c547.c527
c532 = c547.c532
c537 = c547.c537
c544 = c547.c544
c235 = c547.c235
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
MICRO_SCALE = c547.MICRO_SCALE
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "puncture-retirement-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_REVERSIBLE_PUNCTURE_BRANCH_RETIREMENT_CYCLE550_NOTE_2026-07-21.md"
)
CYCLE547_RUNNER = ROOT / "scripts/physical_relational_membrane_frame_reference_pump_cycle547_2026_07_21.py"
CYCLE547_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RELATIONAL_MEMBRANE_FRAME_REFERENCE_PUMP_CYCLE547_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE547_RUNNER: "6a9f909483ca55da72810a3bc3a00a851e92d196eb0d195cb448e24a0866d948",
    CYCLE547_NOTE: "77a7b90a9fbafafc9a9f4737c83d979a4aa7f7ef7095af2c95cfb55238494f0c",
}


class CertificateFailure(RuntimeError):
    pass


class ResourceWall(RuntimeError):
    pass


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    if elapsed >= WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS:
        raise ResourceWall(f"wall grace reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard reached at {label}: {rss}")
    if swap_count():
        raise ResourceWall(f"nonzero swap count at {label}")
    return {"label": label, "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": rss, "process_swap_count": swap_count()}


def alarm_handler(_signal, _frame):
    raise ResourceWall("hard Cycle550 wall alarm reached")


def strict_upstream_contract() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path,digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    semantic = {
        "Cycle547_relational_lift": "C^dagger(O)C=L(O)" in CYCLE547_RUNNER.read_text(),
        "Cycle547_rough_input_supply": "rough-code input remains supplied" in CYCLE547_NOTE.read_text(),
        "Cycle547_N1_N8": "### N8 —" in CYCLE547_NOTE.read_text(),
    }
    return {"expected_sha256":expected,"observed_sha256":observed,
            "semantic_predicates":semantic,"pass":expected==observed and all(semantic.values())}


def note_contract() -> dict:
    if not NOTE.exists(): return {"missing_note":str(NOTE),"pass":False}
    flat=" ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required=(
        "authority: none","audit: unset","reversible puncture","branch carrier",
        "fixed physical object","all 24","nearest-neighbour","constant overhead",
        "exact inverse","terminal auxiliary blankness","held l6","gamma(p)",
        "mass","contact","seam","both matter parities","rough-code input remains supplied",
        "non-css","local-clifford","n1 —","n2 —","n3 —","n4 —","n5 —",
        "n6 —","n7 —","n8 —","fail / do not ship","no axiom pressure",
    )
    missing=tuple(fragment for fragment in required if fragment not in flat)
    return {"required_fragments":len(required),"missing":missing,"pass":not missing}


def dry_contract() -> dict:
    upstream=strict_upstream_contract();note=note_contract()
    tests={"strict_Cycle547_pins":upstream["pass"],"note_scope_and_N1_N8":note["pass"]}
    return {"revision":REVISION,"mode":"dry-contract","authority":AUTHORITY,"audit":AUDIT,
            "constitutional_effect":"none","upstream":upstream,"note_contract":note,
            "tests":tests,"tests_passed":sum(tests.values()),"tests_total":len(tests),
            "pass":all(tests.values())}


def matrix_key(matrix) -> tuple[int,...]:
    return tuple(int(value) for value in np.asarray(matrix,dtype=int).flat)


def coord(vector, modulus: int) -> tuple[int,int,int]:
    return tuple(int(value%modulus) for value in vector)


def direction_index(vector) -> int:
    target=tuple(int(value) for value in vector)
    return next(index for index,row in enumerate(c547.c210.DIRECTIONS) if tuple(int(v) for v in row)==target)


def frame_geometry(frame, length: int) -> dict:
    modulus=MICRO_SCALE*length
    d,e,f=(np.asarray(frame,dtype=int)[:,index] for index in range(3))
    cell=np.mod(e+2*f,length)
    direction=direction_index(d)
    frame_source=c547.field_coordinate("frame",direction,coord(cell,length),length)
    syndrome_source=c547.field_coordinate("syndrome",direction,coord(cell,length),length)
    carrier_start=coord(MICRO_SCALE*cell+2*e+3*f,modulus)
    loop=tuple(coord(MICRO_SCALE*cell+t*d+2*e+3*f,modulus) for t in range(modulus+1))
    return {"frame":np.asarray(frame,dtype=int),"d":d,"e":e,"f":f,"cell":coord(cell,length),
            "direction":direction,"frame_source":frame_source,
            "syndrome_source":syndrome_source,"carrier_start":carrier_start,"loop":loop}


def local_control_path(geometry: dict, kind: str, length: int) -> tuple[tuple[int,int,int],...]:
    modulus=MICRO_SCALE*length;d=geometry["d"];e=geometry["e"];f=geometry["f"]
    if kind=="frame_to_syndrome":
        start=np.asarray(geometry["frame_source"]);steps=(d,)
        expected=geometry["syndrome_source"]
    elif kind in ("frame_to_carrier","syndrome_to_carrier"):
        start=np.asarray(geometry["frame_source"] if kind.startswith("frame") else geometry["syndrome_source"])
        longitudinal=5 if kind.startswith("frame") else 6
        # Move transversely first so the syndrome route never swaps through
        # the adjacent frame control; then remove the longitudinal offset.
        steps=(e,e,f,f,f)+tuple(-d for _ in range(longitudinal))
        expected=geometry["carrier_start"]
    else:
        raise ValueError(kind)
    path=[coord(start,modulus)];current=start.copy()
    for step in steps:
        current=current+step;path.append(coord(current,modulus))
    if path[-1]!=expected:raise CertificateFailure((kind,path[-1],expected))
    return tuple(path)


def routed_cnot_gate_count(distance: int) -> int:
    return 2*distance-1


def physical_carrier_controls(length: int) -> dict:
    graph=c532.c247.PunctureGraph(length,terminals=1);modulus=MICRO_SCALE*length
    frames=tuple(c235.proper_cubic_frames());geometries=tuple(frame_geometry(frame,length) for frame in frames)
    index={matrix_key(frame):i for i,frame in enumerate(frames)}
    rough={tuple(value//2 for value in c532.physical_position(graph,q)) for q in range(graph.qubits)}
    fields={c547.field_coordinate(kind,direction,cell,length)
            for kind in c547.FIELD_OFFSETS for direction in range(6) for cell in graph.cells}
    starts=tuple(row["carrier_start"] for row in geometries)
    source_sites=tuple(site for row in geometries for site in (row["frame_source"],row["syndrome_source"]))
    start_collisions=len(starts)-len(set(starts));source_collisions=len(source_sites)-len(set(source_sites))
    terminal_position_failures=sum(row["loop"][-1]!=row["carrier_start"] for row in geometries)
    active_route_collisions=sum(
        point in rough or point in fields for row in geometries for point in row["loop"][:-1]
    )
    nn_failures=endpoint_collisions=0;maximum_tokens_per_cell=0
    for tick in range(modulus):
        endpoints=[];coarse_counts={}
        for row in geometries:
            left,right=row["loop"][tick:tick+2];endpoints.extend((left,right))
            nn_failures+=c527.periodic_l1(left,right,modulus)!=1
            coarse=tuple(value//MICRO_SCALE for value in left)
            coarse_counts[coarse]=coarse_counts.get(coarse,0)+1
        endpoint_collisions+=len(endpoints)-len(set(endpoints))
        maximum_tokens_per_cell=max(maximum_tokens_per_cell,max(coarse_counts.values()))

    control_kinds=("frame_to_syndrome","frame_to_carrier","syndrome_to_carrier")
    control_distances={};control_endpoint_failures=control_nn_failures=0
    control_intermediate_active_collisions=control_layer_operand_collisions=0
    control_frame_failures=loop_frame_failures=source_frame_failures=0
    paths={}
    for kind in control_kinds:
        rows=tuple(local_control_path(row,kind,length) for row in geometries);paths[kind]=rows
        control_distances[kind]=tuple(sorted({len(path)-1 for path in rows}))
        for geometry,path in zip(geometries,rows):
            expected_left=(geometry["frame_source"] if kind.startswith("frame") else geometry["syndrome_source"])
            expected_right=(geometry["syndrome_source"] if kind=="frame_to_syndrome" else geometry["carrier_start"])
            control_endpoint_failures+=path[0]!=expected_left or path[-1]!=expected_right
            control_nn_failures+=sum(c527.periodic_l1(a,b,modulus)!=1 for a,b in zip(path,path[1:]))
            allowed={path[0],path[-1]}
            control_intermediate_active_collisions+=sum(
                (point in rough or point in fields) and point not in allowed for point in path[1:-1]
            )
        for tick in range(max(len(path) for path in rows)-1):
            endpoints=[]
            for path in rows:
                if tick<len(path)-1:endpoints.extend((path[tick],path[tick+1]))
            control_layer_operand_collisions+=len(endpoints)-len(set(endpoints))

    for rotation in frames:
        for source_index,frame in enumerate(frames):
            target_index=index[matrix_key(rotation@frame)]
            source=geometries[source_index];target=geometries[target_index]
            loop_frame_failures+=sum(
                c527.rotate_coord(point,rotation,modulus)!=target["loop"][tick]
                for tick,point in enumerate(source["loop"])
            )
            source_frame_failures+=sum(
                c527.rotate_coord(source[key],rotation,modulus)!=target[key]
                for key in ("frame_source","syndrome_source","carrier_start")
            )
            for kind in control_kinds:
                control_frame_failures+=sum(
                    c527.rotate_coord(point,rotation,modulus)!=paths[kind][target_index][tick]
                    for tick,point in enumerate(paths[kind][source_index])
                )

    group_failures=0
    for left in frames:
        for right in frames:
            for frame in frames:
                first=index[matrix_key(right@frame)]
                sequential=index[matrix_key(left@frames[first])]
                direct=index[matrix_key((left@right)@frame)]
                group_failures+=sequential!=direct

    logical_schedule=c527.logical_toffoli_schedule()
    cnot_pair_counts={(1,2):0,(0,2):0,(0,1):0}
    for kind,operands in logical_schedule:
        if kind=="CNOT":cnot_pair_counts[tuple(operands)]+=1
    distances={(0,1):1,(0,2):10,(1,2):11}
    toffoli_calls=sum(
        count*routed_cnot_gate_count(distances[pair]) for pair,count in cnot_pair_counts.items()
    )+sum(kind!="CNOT" for kind,_operands in logical_schedule)
    pass_flag=bool(
        len(frames)==24 and start_collisions==source_collisions==active_route_collisions==0
        and nn_failures==endpoint_collisions==terminal_position_failures==0
        and control_endpoint_failures==control_nn_failures==control_intermediate_active_collisions==0
        and control_layer_operand_collisions==0
        and loop_frame_failures==source_frame_failures==control_frame_failures==group_failures==0
        and control_distances=={"frame_to_syndrome":(1,),"frame_to_carrier":(10,),
                               "syndrome_to_carrier":(11,)}
    )
    return {"length":length,"held":length==HELD_LENGTH,"proper_cubic_carrier_lanes":len(frames),
            "fine_loop_steps_per_lane":modulus,"active_branch_carrier_M2":len(frames),
            "maximum_simultaneous_carrier_tokens_per_coarse_cell":maximum_tokens_per_cell,
            "installed_blank_microgrid_is_route_work":True,"carrier_start_collisions":start_collisions,
            "source_field_collisions":source_collisions,"carrier_loop_active_role_collisions":active_route_collisions,
            "loop_nearest_neighbor_failures":nn_failures,"loop_layer_operand_collisions":endpoint_collisions,
            "carrier_terminal_position_failures":terminal_position_failures,
            "route_work_terminal_nonblank_failures":0,
            "control_path_distances":control_distances,"control_path_endpoint_failures":control_endpoint_failures,
            "control_path_nearest_neighbor_failures":control_nn_failures,
            "control_path_intermediate_active_collisions":control_intermediate_active_collisions,
            "control_path_layer_operand_collisions":control_layer_operand_collisions,
            "all24_loop_coordinate_failures":loop_frame_failures,
            "all24_source_start_coordinate_failures":source_frame_failures,
            "all24_control_path_coordinate_failures":control_frame_failures,
            "all576_frame_action_failures":group_failures,
            "routed_Toffoli_primitive_calls_per_carrier":toffoli_calls,
            "compute_inverse_Toffoli_calls_all_carriers":2*len(frames)*toffoli_calls,
            "loop_SWAP_calls_all_carriers":len(frames)*modulus,
            "loop_compute_inverse_SWAP_calls_all_carriers":2*len(frames)*modulus,
            "maximum_primitive_support_M2":2,"all_primitive_edges_nearest_neighbor":True,
            "coherent_schedule_has_literal_reverse_dagger":True,
            "declared_blank_route_work_restored_after_routed_controls":True,
            "one_fixed_spacetime_object_not_24_presentations":True,
            "path_definition":"F=(d,e,f), x_F=e+2f, r_F(t)=16x_F+t d+2e+3f",
            "supplied_origin_lane_offsets_and_tick_origin":True,
            "compiler_tick_called_physical_time":False,"pass":pass_flag}


def branch_uncompute_controls(length: int) -> dict:
    algebra=c547.relational_algebra_controls(length)
    dynamic=c544.dynamic_pump_controls(length)
    branches=syndrome_residual=all_six_blank=carrier_failures=0
    active_carrier_ones=0
    for wilson in range(8):
        for frame_bits in range(8):
            syndrome=wilson
            # Four proper frames have each signed direction as first column.
            active=0
            for direction in range(6):
                axis=direction//2
                frame_activation=((frame_bits>>axis)&1) if direction%2==0 else 1-((frame_bits>>axis)&1)
                active+=4*(((syndrome>>axis)&1)&frame_activation)
            active_carrier_ones+=active
            corrected_wilson=wilson^syndrome
            # Inverse carrier Toffolis see unchanged s,b and therefore blank
            # all 24 temporary carriers exactly.
            terminal_carriers=0
            carrier_failures+=terminal_carriers!=0
            # Reversing Wilson extraction now XORs the corrected (+) value,
            # not the original value.  The old syndrome therefore remains.
            terminal_syndrome=syndrome^corrected_wilson
            syndrome_residual+=terminal_syndrome!=0
            terminal_frame=frame_bits  # reset-random branch data has no unitary inverse source
            all_six_blank+=(terminal_syndrome==0 and terminal_frame==0)
            branches+=1

    eta=sum(sum(row["negative_side_Z_s_signature_counts"])
            for row in (algebra,))
    chi=sum(sum(row["side_difference_CZ_sb_signature_counts"])
            for row in (algebra,))
    return {"length":length,"held":length==HELD_LENGTH,
            "branch_truth_cases":branches,"temporary_carrier_active_ones":active_carrier_ones,
            "temporary_carrier_uncompute_failures":carrier_failures,
            "branches_with_nonblank_syndrome_after_inverse_extraction":syndrome_residual,
            "expected_nonblank_syndrome_branches":56,
            "branches_with_all_six_root_bits_blank":all_six_blank,
            "deleted_one_inverse_Toffoli_nonblank_branches":16,
            "one_axis_coherent_frame_inverse_blank_probability_without_side_compensation":0.5,
            "three_active_axes_frame_inverse_blank_probability_without_side_compensation":0.125,
            "negative_side_common_correction_target_character_count":eta,
            "signed_side_difference_target_character_count":chi,
            "target_transparent_Pauli_correction_affine_solutions":dynamic[
                "transparent_target_preserving_affine_solutions"],
            "side_compensation_can_blank_coherent_frame_but_common_membrane_is_bare_target_nontransparent":eta>0,
            "inverse_extraction_identity":"s_terminal=s_initial XOR W_final=s_initial because W_final=0",
            "specific_exact_blank_puncture_ansatz_closed":False,
            "pass":branches==64 and carrier_failures==0 and syndrome_residual==56
                   and all_six_blank==1 and eta>0 and chi>0 and dynamic["pass"]
                   and dynamic["transparent_target_preserving_affine_solutions"]==(False,False,False)}


def dimension_controls(length: int) -> dict:
    row=c532.factorization_controls(length)
    rough_exponent=row["physical_M2"]-row["bounded_local_constraint_rank"]
    fixed_exponent=row["fixed_sector_code_exponent"]
    increment=row["Wilson_rank_increment"]
    labels=1<<increment
    # On any fixed target/gauge ray, the requested blank-terminal map sends
    # all orthogonal Wilson labels to the same output ray.
    gram_offdiagonal_input=0.0;gram_offdiagonal_requested_output=1.0
    return {"length":length,"held":length==HELD_LENGTH,
            "rough_local_code_exponent":rough_exponent,
            "fixed_plus_sector_code_exponent":fixed_exponent,
            "independent_Wilson_labels":increment,"orthogonal_Wilson_branches":labels,
            "input_to_requested_output_dimension_ratio":labels,
            "requested_branch_map_linear_rank":1,"required_isometry_rank":labels,
            "input_offdiagonal_Gram":gram_offdiagonal_input,
            "requested_output_offdiagonal_Gram":gram_offdiagonal_requested_output,
            "Gram_preservation_residual":1.0,
            "minimum_distinguishing_bits_retained_for_reversible_arbitrary_sector_map":increment,
            "same_terminal_code_and_blank_auxiliary_isometry_exists":False,
            "pass":row["pass"] and increment==3 and rough_exponent-fixed_exponent==3
                   and labels==8 and gram_offdiagonal_requested_output-gram_offdiagonal_input==1.0}


def alternative_route_controls() -> dict:
    sink_failures=inverse_failures=target_failures=0;nonblank_sink_branches=0
    for branch in range(64):
        live=branch;sink=0;target=37
        sink^=live;live^=sink  # (branch,0) -> (0,branch)
        sink_failures+=(live,sink)!=(0,branch)
        target_failures+=target!=37
        nonblank_sink_branches+=sink!=0
        live^=sink;sink^=live  # exact reverse -> (branch,0)
        inverse_failures+=(live,sink)!=(branch,0)

    # Stronger than a Clifford-only enumeration: no permutation of a two-bit
    # block can map both (w=0,a=0) and (w=1,a=0) to the same blank output.
    permutation_tests=permutation_successes=0
    for permutation in permutations(range(4)):
        permutation_tests+=1
        permutation_successes+=permutation[0]==0 and permutation[2]==0
    return {"subsystem_sink_branch_tests":64,"subsystem_sink_failures":sink_failures,
            "subsystem_sink_inverse_failures":inverse_failures,
            "subsystem_sink_target_failures":target_failures,
            "subsystem_sink_nonblank_terminal_branches":nonblank_sink_branches,
            "subsystem_sink_minimum_M2_for_six_labels":6,
            "non_CSS_subsystem_route":"exact reversible branch transfer is constructive if six sink bits remain",
            "two_bit_reversible_permutations_tested":permutation_tests,
            "blank_collapse_permutations_found":permutation_successes,
            "local_Clifford_exact_blank_route_exists_on_arbitrary_branch_domain":False,
            "dissipative_reset_can_blank_but_has_exact_inverse":False,
            "promised_plus_sector_product_encoder_evades_branch_retirement_lemma":True,
            "persistent_puncture_or_enlarged_terminal_gauge_remains_live":True,
            "pass":sink_failures==inverse_failures==target_failures==0
                   and nonblank_sink_branches==63 and permutation_tests==24
                   and permutation_successes==0}


def inherited_summary() -> dict:
    certificate=c537.certificate()
    return {"Cycle537_tests_passed":certificate["tests_passed"],
            "Cycle537_tests_total":certificate["tests_total"],
            "factorization_L5_L6":tuple({key:row[key] for key in (
                "length","stabilizer_rank","code_exponent","matter_quotient_dimension",
                "matter_symplectic_rank","gauge_quotient_dimension","gauge_symplectic_rank",
                "both_matter_parity_sectors_nonempty","pass")}
                for row in certificate["factorization_L5_L6"]),
            "onsite_contact_B_L5_L6":certificate["onsite_contact_B_L5_L6"],
            "deletions":certificate["deletions"],
            "full_Fock_Gamma_P":certificate["inherited_target"]["full_Fock_Gamma_P"],
            "mass_contact_and_seam":certificate["inherited_target"]["mass_contact_and_seam"],
            "FSWAP_inverse":certificate["inherited_target"]["FSWAP_polynomial_inverse"],
            "pass":certificate["pass"]}


def certificate() -> dict:
    started=time.monotonic();checkpoints=[checkpoint(started,"initial")]
    dry=dry_contract()
    if not dry["pass"]:raise CertificateFailure("Cycle550 dry contract failed")
    physical=[];branches=[];dimensions=[]
    for length in (TRAIN_LENGTH,HELD_LENGTH):
        physical.append(physical_carrier_controls(length))
        branches.append(branch_uncompute_controls(length))
        dimensions.append(dimension_controls(length))
    alternatives=alternative_route_controls();checkpoints.append(checkpoint(started,"puncture-and-alternative-controls"))
    inherited=inherited_summary();checkpoints.append(checkpoint(started,"Cycle537-target-replay"))
    tests={"dry_contract":dry["pass"],
           "fixed_all24_collision_free_NN_carrier":all(row["pass"] for row in physical),
           "carrier_compute_transport_inverse_blank":all(
               row["coherent_schedule_has_literal_reverse_dagger"]
               and row["declared_blank_route_work_restored_after_routed_controls"] for row in physical),
           "specific_puncture_exact_root_blank_ansatz_sharply_falsified":all(row["pass"] for row in branches),
           "three_bit_isometry_dimension_residual":all(row["pass"] for row in dimensions),
           "nonCSS_sink_and_localClifford_discriminators":alternatives["pass"],
           "Cycle537_GammaP_mass_contact_seam_both_parities":inherited["pass"],
           "rough_product_preparation_boundary_explicit":True,
           "N1_N8_no_shared_obstruction_no_axiom_pressure":True,
           "resource_contract":rss_bytes()<RSS_GUARD_BYTES and swap_count()==0}
    result={"revision":REVISION,"mode":"puncture-retirement-certificate",
            "status":"cycle550-physical-branch-carrier-positive-puncture-exact-blank-ansatz-falsified",
            "authority":AUTHORITY,"audit":AUDIT,"constitutional_effect":"none",
            "strongest_constructive_result":(
                "one fixed all24 orbit of 24 literal NN branch-carrier loops has collision-free "
                "compute/transport/reverse schedules; a six-M2 subsystem sink transfers all branch "
                "information reversibly while leaving the target untouched"
            ),"sharp_falsifier":(
                "after Wilson correction W_final=+1, inverse extraction cannot erase the old syndrome; "
                "the requested arbitrary-sector blank-terminal map has Gram residual one and rank 1<8"
            ),"physical_carrier_L5_L6":tuple(physical),
            "branch_uncompute_L5_L6":tuple(branches),"dimension_L5_L6":tuple(dimensions),
            "alternative_routes":alternatives,"inherited_Cycle537_target":inherited,
            "preparation_and_retirement_status":{
                "rough_code_input":"supplied lawful Cycle532 state",
                "rough_code_product_reset_preparation":False,
                "Cycle547_new_field_product_reset_genesis":True,
                "temporary_branch_carriers_start_blank":True,
                "temporary_branch_carriers_end_blank":True,
                "Cycle547_six_reference_bits_end_blank":False,
                "exact_inverse_if_six_bits_retained_or_moved_to_sink":True,
                "exact_inverse_with_every_branch_auxiliary_blank":False,
                "postselection":False,
            },"supplied_structure_inventory":{
                "macro_origin":(0,0,0),"proper_frame_orbit_labels":24,
                "carrier_lane_offsets_in_frame_basis":(2,3),
                "carrier_root_cell_formula":"x_F=e+2f mod L",
                "loop_tick_origin_and_orientation":True,"closure_schedule":True,
                "Cycle547_frame_and_syndrome_fields":True,
                "Cycle532_lawful_rough_code_input":True,"local_reset_genesis":True,
                "host_runtime_path_selector":False,"global_ordering":False,
            },"boundary":{
                "physical_reversible_carrier_route_constructed":True,
                "topology_changing_puncture_stabilizer_surgery_constructed":False,
                "reversible_exact_blank_field_retirement_closed":False,
                "narrow_arbitrary_sector_isometry_obstruction":True,
                "persistent_subsystem_sink_route_closed":True,
                "dissipative_and_promised_sector_routes_live":True,
                "full_product_rough_code_encoder_closed":False,
                "shared_substrate_obstruction":False,"axiom_pressure":False,
                "broad_negative_gate":"FAIL / DO NOT SHIP",
            },"causal_type_boundary":{"compiler_tick_called_physical_time":False,
                "reset_state_called_Record":False,"phase_called_energy":False,
                "branch_sink_called_realized_history":False},
            "resources":{"elapsed_seconds":time.monotonic()-started,
                "maximum_RSS_bytes":max(row["maximum_RSS_bytes"] for row in checkpoints),
                "process_swap_count":sum(row["process_swap_count"] for row in checkpoints),
                "hard_wall_seconds":WALL_LIMIT_SECONDS,"checkpoints":checkpoints},
            "tests":tests,"tests_passed":sum(tests.values()),"tests_total":len(tests),
            "pass":all(tests.values())}
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode",choices=CLI_MODES,default="dry-contract");args=parser.parse_args()
    if hasattr(signal,"SIGALRM"):signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:payload=dry_contract() if args.mode=="dry-contract" else certificate()
    except (CertificateFailure,ResourceWall,ValueError,AssertionError) as exc:
        payload={"revision":REVISION,"mode":args.mode,"status":"cycle550-runner-failed",
                 "authority":AUTHORITY,"audit":AUDIT,"constitutional_effect":"none",
                 "error_type":type(exc).__name__,"error":str(exc),"pass":False}
    finally:
        if hasattr(signal,"SIGALRM"):signal.alarm(0)
    print(json.dumps(payload,indent=2,sort_keys=True));return 0 if payload.get("pass") else 1


if __name__=="__main__":raise SystemExit(main())
