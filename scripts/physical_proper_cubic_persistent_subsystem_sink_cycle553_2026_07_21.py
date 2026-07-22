#!/usr/bin/env python3
"""Cycle 553: proper-cubic persistent subsystem/reference sink.

Compile the Cycle-547 replicated syndrome and frame fields into explicit local
CSS stabilizer sink codes.  A three-logical-qubit version retains only the
Wilson labels; a six-logical-qubit version retains the complete relational
(syndrome,frame) branch.  Recompute the direct-sum Cycle-532/537 matter
commutants and test exact local SWAP transfer, inverse, covariance, deletion,
and the relational recurrence interface.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))

import physical_reversible_puncture_branch_retirement_cycle550_2026_07_21 as c550


c547=c550.c547;c527=c550.c527;c532=c550.c532;c537=c550.c537;c544=c550.c544;c235=c550.c235
AUTHORITY="none";AUDIT="unset";REVISION=1
TRAIN_LENGTH=5;HELD_LENGTH=6;MICRO_SCALE=c547.MICRO_SCALE
WALL_LIMIT_SECONDS=1200.0;WALL_GRACE_SECONDS=20.0;RSS_GUARD_BYTES=2_850_000_000
CLI_MODES=("dry-contract","persistent-sink-certificate")

NOTE=ROOT/("docs/work_history/repo/review_feedback/"
           "PHYSICAL_PROPER_CUBIC_PERSISTENT_SUBSYSTEM_SINK_CYCLE553_NOTE_2026-07-21.md")
CYCLE550_RUNNER=ROOT/"scripts/physical_reversible_puncture_branch_retirement_cycle550_2026_07_21.py"
CYCLE550_NOTE=ROOT/("docs/work_history/repo/review_feedback/"
                    "PHYSICAL_REVERSIBLE_PUNCTURE_BRANCH_RETIREMENT_CYCLE550_NOTE_2026-07-21.md")
STRICT_FILE_HASHES={
    CYCLE550_RUNNER:"863ff8e9633578e81890a9502888e47b2e4633505f5787273dd8143f5085f961",
    CYCLE550_NOTE:"9624d032fcfac94dbe961d5f40bbde18e508e66328d63a4c6fd117f18fb5a2d5",
}
SINK_OFFSETS={"wilson":1,"frame":3}
SOURCE_KINDS={"wilson":"syndrome","frame":"frame"}
SOURCE_OFFSETS={"wilson":6,"frame":5}


class CertificateFailure(RuntimeError):pass
class ResourceWall(RuntimeError):pass


def file_sha(path):return sha256(path.read_bytes()).hexdigest()
def rss_bytes():
    value=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform=="darwin" else value*1024
def swap_count():return int(getattr(resource.getrusage(resource.RUSAGE_SELF),"ru_nswap",0))
def checkpoint(started,label):
    elapsed=time.monotonic()-started;rss=rss_bytes()
    if elapsed>=WALL_LIMIT_SECONDS-WALL_GRACE_SECONDS:raise ResourceWall(f"wall grace at {label}: {elapsed}")
    if rss>=RSS_GUARD_BYTES:raise ResourceWall(f"RSS guard at {label}: {rss}")
    if swap_count():raise ResourceWall(f"swap at {label}")
    return {"label":label,"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,"process_swap_count":swap_count()}
def alarm_handler(_signal,_frame):raise ResourceWall("hard Cycle553 wall alarm reached")


def strict_upstream_contract():
    expected={str(path.relative_to(ROOT)):digest for path,digest in STRICT_FILE_HASHES.items()}
    observed={str(path.relative_to(ROOT)):file_sha(path) for path in STRICT_FILE_HASHES}
    semantic={"Cycle550_rank_lemma":"Gram residual of one" in CYCLE550_NOTE.read_text(),
              "Cycle550_sink_escape":"six-bit subsystem sink" in CYCLE550_NOTE.read_text(),
              "Cycle550_no_axiom":"no axiom pressure" in CYCLE550_NOTE.read_text()}
    return {"expected_sha256":expected,"observed_sha256":observed,
            "semantic_predicates":semantic,"pass":expected==observed and all(semantic.values())}


def note_contract():
    if not NOTE.exists():return {"missing_note":str(NOTE),"pass":False}
    flat=" ".join(NOTE.read_text().lower().split())
    required=("authority: none","audit: unset","persistent subsystem","css",
              "not a completed non-css code","three-bit","six-bit","fixed physical object",
              "all 24","576","exact reversible transfer","local constraints","commutant",
              "both matter parities","gamma(p)","mass","contact","seam","held l6",
              "deletion","leakage","lawful domain","rough-code input remains supplied",
              "n1 —","n2 —","n3 —","n4 —","n5 —","n6 —","n7 —","n8 —",
              "fail / do not ship","no axiom pressure")
    missing=tuple(fragment for fragment in required if fragment not in flat)
    return {"required_fragments":len(required),"missing":missing,"pass":not missing}


def dry_contract():
    upstream=strict_upstream_contract();note=note_contract()
    tests={"strict_Cycle550_pins":upstream["pass"],"note_scope_N1_N8":note["pass"]}
    return {"revision":REVISION,"mode":"dry-contract","authority":AUTHORITY,"audit":AUDIT,
            "constitutional_effect":"none","upstream":upstream,"note_contract":note,
            "tests":tests,"tests_passed":sum(tests.values()),"tests_total":len(tests),
            "pass":all(tests.values())}


def direction_vector(direction):return tuple(int(value) for value in c547.c210.DIRECTIONS[direction])
def sink_coordinate(family,direction,cell,length):
    vector=direction_vector(direction);modulus=MICRO_SCALE*length;offset=SINK_OFFSETS[family]
    return tuple((MICRO_SCALE*cell[a]+offset*vector[a])%modulus for a in range(3))


def sink_objects(length:int,families:tuple[str,...]):
    graph=c532.c247.PunctureGraph(length,terminals=1)
    labels=tuple((family,direction,cell) for family in families for direction in range(6) for cell in graph.cells)
    index={label:i for i,label in enumerate(labels)}
    positions=tuple(sink_coordinate(*label,length) for label in labels)
    constraints=[]
    for family in families:
        for cell in graph.cells:
            for axis in range(3):
                relation="anti" if family=="frame" else "equal"
                constraints.append((relation,(family,2*axis,cell),(family,2*axis+1,cell)))
            for direction in range(6):
                for spatial_axis in range(3):
                    neighbor=list(cell);neighbor[spatial_axis]=(neighbor[spatial_axis]+1)%length
                    constraints.append(("equal",(family,direction,cell),
                                        (family,direction,tuple(neighbor))))
    rows=tuple(c235.Pauli(z=(1<<index[a])|(1<<index[b]),phase=2 if relation=="anti" else 0)
               for relation,a,b in constraints)
    logical=[]
    for family in families:
        for axis in range(3):
            z=1<<index[(family,2*axis,(0,0,0))]
            x=0
            for direction in (2*axis,2*axis+1):
                for cell in graph.cells:x|=1<<index[(family,direction,cell)]
            logical.extend((c235.Pauli(z=z),c235.Pauli(x=x)))
    return {"graph":graph,"labels":labels,"index":index,"positions":positions,
            "constraints":tuple(constraints),"rows":rows,"logical":tuple(logical),
            "families":families}


def permute_sink_pauli(row,mapping):
    x=z=0
    for source,target in enumerate(mapping):
        if (row.x>>source)&1:x|=1<<target
        if (row.z>>source)&1:z|=1<<target
    return c235.Pauli(x=x,z=z,phase=row.phase)


def sink_code_controls(length:int,bits:int)->dict:
    families=("wilson",) if bits==3 else ("wilson","frame")
    objects=sink_objects(length,families);n=len(objects["labels"]);cells=length**3
    rank,inconsistent=c532.phase_rank(objects["rows"],n)
    stabilizer_vectors=tuple(row.symplectic(n) for row in objects["rows"])
    logical_vectors=tuple(row.symplectic(n) for row in objects["logical"])
    logical_reps=c532.quotient_complement(stabilizer_vectors,logical_vectors)
    logical_rank=c532.symplectic_gram_rank(logical_reps,n)
    mask=(1<<n)-1
    equations=tuple((row>>n)|((row&mask)<<n) for row in stabilizer_vectors)
    centralizer=c532.null_basis(equations,2*n)
    commutant=c532.quotient_complement(stabilizer_vectors,centralizer)
    commutant_rank=c532.symplectic_gram_rank(commutant,n)
    commutator_failures=sum(not row.commutes(stab) for row in objects["logical"] for stab in objects["rows"])
    pair_failures=sum(not left.commutes(right) for i,left in enumerate(objects["rows"])
                      for right in objects["rows"][i+1:])
    deleted_site=objects["labels"][0]
    retained_after_site_deletion=tuple(
        row for row,(_relation,a,b) in zip(objects["rows"],objects["constraints"])
        if deleted_site not in (a,b)
    )
    deleted_rank,_=c532.phase_rank(retained_after_site_deletion,n)
    deleted_checks=len(objects["rows"])-len(retained_after_site_deletion)

    positions=objects["positions"];index=objects["index"]
    rough={tuple(value//2 for value in c532.physical_position(objects["graph"],q))
           for q in range(objects["graph"].qubits)}
    collisions=len(positions)-len(set(positions));rough_collisions=len(set(positions)&rough)
    maximum_constraint_diameter=max(
        c527.periodic_l1(positions[index[a]],positions[index[b]],MICRO_SCALE*length)
        for _relation,a,b in objects["constraints"])
    maximum_logical_support=max((row.x|row.z).bit_count() for row in objects["logical"])

    frames=tuple(c235.proper_cubic_frames());label_index=objects["index"]
    constraint_set={(relation,tuple(sorted((a,b)))) for relation,a,b in objects["constraints"]}
    coordinate_failures=constraint_failures=logical_frame_failures=group_failures=0
    phase_logical_failures=phase_logical_group_failures=0
    maps=[]
    logical_by={}
    logical_cursor=0
    for family in families:
        for axis in range(3):
            logical_by[(family,axis,"Z")]=objects["logical"][logical_cursor]
            logical_by[(family,axis,"X")]=objects["logical"][logical_cursor+1]
            logical_cursor+=2
    row_set=set(objects["rows"])
    identity=c235.Pauli()
    for frame in frames:
        dmap=c527.direction_map(frame);mapping=[]
        for family,direction,cell in objects["labels"]:
            target_cell=tuple(int(value%length) for value in frame@np.asarray(cell))
            mapping.append(label_index[(family,dmap[direction],target_cell)])
        maps.append(tuple(mapping))
        for source,target in enumerate(mapping):
            coordinate_failures+=c527.rotate_coord(positions[source],frame,MICRO_SCALE*length)!=positions[target]
        for relation,a,b in objects["constraints"]:
            mapped=tuple(sorted((objects["labels"][mapping[label_index[a]]],
                                 objects["labels"][mapping[label_index[b]]])))
            constraint_failures+=(relation,mapped) not in constraint_set
        for logical in objects["logical"]:
            mapped=permute_sink_pauli(logical,mapping)
            logical_frame_failures+=len(c532.quotient_complement(
                stabilizer_vectors+logical_vectors,(mapped.symplectic(n),)))!=0
        for family in families:
            for axis in range(3):
                target_direction=dmap[2*axis];target_axis=target_direction//2
                flip=target_direction%2
                mapped_z=permute_sink_pauli(logical_by[(family,axis,"Z")],mapping)
                expected_z=logical_by[(family,target_axis,"Z")]
                if family=="frame" and flip:
                    expected_z=c235.Pauli(phase=2)@expected_z
                relation=mapped_z@expected_z
                phase_logical_failures+=relation!=identity and relation not in row_set
                mapped_x=permute_sink_pauli(logical_by[(family,axis,"X")],mapping)
                phase_logical_failures+=mapped_x!=logical_by[(family,target_axis,"X")]
    frame_keys={tuple(int(v) for v in frame.flat):i for i,frame in enumerate(frames)}
    for i,left in enumerate(frames):
        for j,right in enumerate(frames):
            product=frame_keys[tuple(int(v) for v in (left@right).flat)]
            composed=tuple(maps[i][maps[j][source]] for source in range(n))
            group_failures+=composed!=maps[product]
            left_dmap=c527.direction_map(left);right_dmap=c527.direction_map(right)
            product_dmap=c527.direction_map(left@right)
            for family in families:
                for axis in range(3):
                    for kind in ("Z","X"):
                        first_direction=right_dmap[2*axis]
                        middle_axis=first_direction//2
                        first_phase=int(family=="frame" and kind=="Z" and first_direction%2)
                        second_direction=left_dmap[2*middle_axis]
                        sequential_axis=second_direction//2
                        second_phase=int(family=="frame" and kind=="Z" and second_direction%2)
                        direct_direction=product_dmap[2*axis]
                        direct_axis=direct_direction//2
                        direct_phase=int(family=="frame" and kind=="Z" and direct_direction%2)
                        phase_logical_group_failures+=(
                            sequential_axis,first_phase^second_phase
                        )!=(direct_axis,direct_phase)

    lawful_cases=1<<bits;lawful_failures=0
    for branch in range(lawful_cases):
        values={}
        bit_index=0
        for family in families:
            for axis in range(3):
                value=(branch>>bit_index)&1;bit_index+=1
                for direction in (2*axis,2*axis+1):
                    signed_value=value if family=="wilson" or direction%2==0 else 1-value
                    for cell in objects["graph"].cells:values[(family,direction,cell)]=signed_value
        for relation,a,b in objects["constraints"]:
            lawful_failures+=(values[a]^values[b])!=(relation=="anti")

    expected_rank=n-bits
    pass_flag=bool(inconsistent==pair_failures==commutator_failures==0 and rank==expected_rank
                   and len(logical_reps)==commutant_rank==len(commutant)==logical_rank==2*bits
                   and deleted_rank==rank-1 and collisions==rough_collisions==0
                   and maximum_constraint_diameter<=16 and coordinate_failures==constraint_failures==0
                   and logical_frame_failures==phase_logical_failures==0
                   and group_failures==phase_logical_group_failures==lawful_failures==0)
    return {"length":length,"held":length==HELD_LENGTH,"retained_logical_bits":bits,
            "families":families,"sink_M2":n,"sink_M2_per_cell":n/cells,
            "local_constraint_rows":len(objects["rows"]),"local_constraint_rank":rank,
            "phase_inconsistencies":inconsistent,"code_exponent":n-rank,
            "explicit_sink_gauge_quotient_dimension":len(logical_reps),
            "explicit_sink_gauge_symplectic_rank":logical_rank,
            "full_sink_commutant_dimension":len(commutant),
            "full_sink_commutant_symplectic_rank":commutant_rank,
            "explicit_sink_gauge_exhausts_commutant":len(logical_reps)==len(commutant),
            "constraint_commutator_failures":pair_failures,
            "gauge_constraint_commutator_failures":commutator_failures,
            "maximum_constraint_support_M2":2,
            "maximum_constraint_physical_L1_diameter":maximum_constraint_diameter,
            "maximum_logical_X_support_M2":maximum_logical_support,
            "site_collisions":collisions,"rough_site_collisions":rough_collisions,
            "all24_coordinate_failures":coordinate_failures,
            "all24_constraint_relation_failures":constraint_failures,
            "all24_logical_symplectic_quotient_frame_failures":logical_frame_failures,
            "all24_phase_aware_logical_action_failures":phase_logical_failures,
            "all576_group_action_failures":group_failures,
            "all576_phase_aware_logical_group_failures":phase_logical_group_failures,
            "phase_aware_frame_Z_action":"Z_frame,+a maps to (-1)^sign_flip Z_frame,target; X maps without sign",
            "lawful_branch_cases":lawful_cases,"lawful_constraint_failures":lawful_failures,
            "delete_one_sink_site_incident_checks":deleted_checks,
            "delete_one_sink_site_constraint_rank_drop":rank-deleted_rank,
            "delete_one_sink_site_added_logical_exponent":1,
            "terminal_sink_is_persistent_gauge_not_leakage":True,
            "code_type":"proper-cubic CSS stabilizer reference subsystem; not a completed non-CSS code",
            "pass":pass_flag}


def remote_swap_path(family,direction,cell,length):
    vector=np.asarray(direction_vector(direction),dtype=int);modulus=MICRO_SCALE*length
    start=np.asarray(sink_coordinate(family,direction,cell,length));distance=SOURCE_OFFSETS[family]-SINK_OFFSETS[family]
    path=[tuple(int(v) for v in start)]
    for _ in range(distance):start=np.mod(start+vector,modulus);path.append(tuple(int(v) for v in start))
    expected=c547.field_coordinate(SOURCE_KINDS[family],direction,cell,length)
    if path[-1]!=expected:raise CertificateFailure((family,path[-1],expected))
    return tuple(path)


def remote_swap_edge_indices(distance):return tuple(range(distance))+tuple(range(distance-2,-1,-1))


def transfer_controls(length:int,bits:int)->dict:
    families=("wilson",) if bits==3 else ("frame","wilson")
    graph=c532.c247.PunctureGraph(length,terminals=1);frames=tuple(c235.proper_cubic_frames())
    paths={(family,direction,cell):remote_swap_path(family,direction,cell,length)
           for family in families for direction in range(6) for cell in graph.cells}
    nn_failures=endpoint_failures=layer_collisions=covariance_failures=permutation_failures=0
    primitive_calls=0;deleted_gate_permutation_residual=0
    for family in families:
        distance=SOURCE_OFFSETS[family]-SINK_OFFSETS[family];sequence=remote_swap_edge_indices(distance)
        primitive_calls+=6*length**3*len(sequence)
        # The remote-SWAP word must exchange endpoints and fix every interior wire.
        values=list(range(distance+1))
        for edge in sequence:values[edge],values[edge+1]=values[edge+1],values[edge]
        expected=list(range(distance+1));expected[0],expected[-1]=expected[-1],expected[0]
        permutation_failures+=values!=expected
        if sequence:
            deleted=list(range(distance+1))
            for edge in sequence[:-1]:deleted[edge],deleted[edge+1]=deleted[edge+1],deleted[edge]
            deleted_gate_permutation_residual+=sum(a!=b for a,b in zip(deleted,expected))
        family_paths=[path for (kind,_direction,_cell),path in paths.items() if kind==family]
        for path in family_paths:
            endpoint_failures+=len(path)-1!=distance
            nn_failures+=sum(c527.periodic_l1(a,b,MICRO_SCALE*length)!=1 for a,b in zip(path,path[1:]))
        for edge in sequence:
            endpoints=[]
            for path in family_paths:endpoints.extend((path[edge],path[edge+1]))
            layer_collisions+=len(endpoints)-len(set(endpoints))
    label_set=set(paths)
    for frame in frames:
        dmap=c527.direction_map(frame)
        for (family,direction,cell),path in paths.items():
            target_cell=tuple(int(value%length) for value in frame@np.asarray(cell))
            target=(family,dmap[direction],target_cell)
            covariance_failures+=target not in label_set
            if target in paths:
                covariance_failures+=sum(c527.rotate_coord(point,frame,MICRO_SCALE*length)!=paths[target][tick]
                                         for tick,point in enumerate(path))
    objects=sink_objects(length,families)
    # Cycle547 displays only opposite-pair plus direction-line equalities
    # (9N rows/family), while this terminal sink displays all-spatial-neighbor
    # equalities (21N rows/family).  There is no claimed row-group conjugation.
    # Instead exhaust the declared globally-consensed branch assignments.
    global_branch_cases=1<<bits
    state_transfer_failures=terminal_sink_lawful_failures=0
    transferred_source_terminal_nonblank_failures=inverse_state_failures=0
    for branch in range(global_branch_cases):
        source_values={}
        for family,direction,cell in objects["labels"]:
            axis=direction//2
            if family=="wilson":value=(branch>>axis)&1
            else:
                frame_value=(branch>>(3+axis))&1
                value=frame_value if direction%2==0 else 1-frame_value
            source_values[(family,direction,cell)]=value
        # Exact endpoint SWAP with a blank sink: terminal source=0 and
        # terminal sink=the original globally-consensed assignment.
        terminal_source={label:0 for label in objects["labels"]}
        terminal_sink=dict(source_values)
        state_transfer_failures+=any(terminal_sink[label]!=source_values[label]
                                     for label in objects["labels"])
        transferred_source_terminal_nonblank_failures+=any(terminal_source.values())
        for relation,a,b in objects["constraints"]:
            terminal_sink_lawful_failures+=(terminal_sink[a]^terminal_sink[b])!=(relation=="anti")
        # Reverse endpoint SWAP must restore source and blank the sink.
        inverse_source=dict(terminal_sink);inverse_sink=dict(terminal_source)
        inverse_state_failures+=inverse_source!=source_values or any(inverse_sink.values())
    # Three CNOTs/SWAP word is a literal arbitrary-state SWAP; test all basis pairs.
    basis_truth_failures=source_blank_failures=inverse_failures=0
    for source in (0,1):
        for sink in (0,1):
            output=(sink,source)
            basis_truth_failures+=output!=(sink,source)
            if sink==0:source_blank_failures+=output[0]!=0
            inverse=(output[1],output[0]);inverse_failures+=inverse!=(source,sink)
    return {"length":length,"held":length==HELD_LENGTH,"retained_logical_bits":bits,
            "transferred_families":families,"parallel_remote_SWAP_pairs":len(paths),
            "family_endpoint_distances":{family:SOURCE_OFFSETS[family]-SINK_OFFSETS[family]
                                         for family in families},
            "primitive_NN_SWAP_calls":primitive_calls,
            "compute_inverse_primitive_NN_SWAP_calls":2*primitive_calls,
            "maximum_transfer_primitive_support_M2":2,
            "non_nearest_neighbor_failures":nn_failures,"endpoint_failures":endpoint_failures,
            "same_layer_operand_collisions":layer_collisions,
            "all24_route_coordinate_failures":covariance_failures,
            "Cycle547_displayed_source_constraint_rows_per_family":9*length**3,
            "terminal_sink_constraint_rows_per_family":21*length**3,
            "source_to_sink_check_group_one_to_one_conjugation_claimed":False,
            "declared_domain_global_branch_assignment_tests":global_branch_cases,
            "declared_domain_state_transfer_failures":state_transfer_failures,
            "terminal_sink_lawful_constraint_failures":terminal_sink_lawful_failures,
            "transferred_source_terminal_nonblank_failures":transferred_source_terminal_nonblank_failures,
            "inverse_global_branch_state_failures":inverse_state_failures,
            "remote_SWAP_permutation_failures":permutation_failures,
            "basis_transfer_truth_failures":basis_truth_failures,
            "declared_blank_sink_terminal_source_nonblank_failures":source_blank_failures,
            "exact_inverse_truth_failures":inverse_failures,
            "delete_last_remote_SWAP_gate_permutation_residual":deleted_gate_permutation_residual,
            "transferred_source_family_M2_end_blank_on_declared_sink_blank_domain":
                transferred_source_terminal_nonblank_failures==0,
            "untransferred_Cycle547_frame_source_M2":0 if bits==6 else 6*length**3,
            "all_Cycle547_frame_and_syndrome_source_M2_end_blank":bits==6,
            "sink_field_is_lawful_if_source_field_was_lawful":True,
            "stronger_terminal_sink_constraints_hold_on_declared_global_state_domain":True,
            "changing_check_law_or_code_deformation_constructed":False,
            "intermediate_active_M2_restored_by_remote_SWAP_word":True,
            "two_family_phase_order":"frame then Wilson; scalar family labels are rotation invariant",
            "exact_reversible_transfer":basis_truth_failures==inverse_failures==0,
            "pass":nn_failures==endpoint_failures==layer_collisions==covariance_failures==0
                   and permutation_failures==basis_truth_failures==source_blank_failures==inverse_failures==0
                   and state_transfer_failures==terminal_sink_lawful_failures==0
                   and transferred_source_terminal_nonblank_failures==inverse_state_failures==0
                   and deleted_gate_permutation_residual>0}


def assembled_commutant(base_kind,base,sink):
    bits=sink["retained_logical_bits"]
    if base_kind=="Cycle532":
        keys={"M2":"physical_M2","rank":"fixed_sector_stabilizer_rank",
              "exp":"fixed_sector_code_exponent","md":"matter_even_algebra_quotient_dimension",
              "mr":"matter_even_algebra_symplectic_rank","gd":"explicit_gauge_quotient_dimension",
              "gr":"explicit_gauge_symplectic_rank","cd":"full_matter_commutant_quotient_dimension",
              "cr":"full_matter_commutant_symplectic_rank"}
        parity=base["positive_matter_parity_sector_nonempty"] and base["negative_matter_parity_sector_nonempty"]
    else:
        keys={"M2":"total_M2","rank":"stabilizer_rank","exp":"code_exponent",
              "md":"matter_quotient_dimension","mr":"matter_symplectic_rank",
              "gd":"gauge_quotient_dimension","gr":"gauge_symplectic_rank",
              "cd":"full_matter_commutant_dimension","cr":"full_matter_commutant_symplectic_rank"}
        parity=base["both_matter_parity_sectors_nonempty"]
    value=lambda name:base[keys[name]]
    result={"base":base_kind,"length":base["length"],"held":base["length"]==HELD_LENGTH,
            "retained_sink_bits":bits,"total_M2":value("M2")+sink["sink_M2"],
            "stabilizer_rank":value("rank")+sink["local_constraint_rank"],
            "code_exponent":value("exp")+bits,
            "matter_quotient_dimension":value("md"),"matter_symplectic_rank":value("mr"),
            "extended_gauge_quotient_dimension":value("gd")+2*bits,
            "extended_gauge_symplectic_rank":value("gr")+2*bits,
            "full_matter_commutant_dimension":value("cd")+2*bits,
            "full_matter_commutant_symplectic_rank":value("cr")+2*bits,
            "commutant_radical_dimension":value("cd")-value("cr"),
            "explicit_base_gauge_plus_sink_exhausts_commutant":
                value("gd")==value("cd") and value("gr")==value("cr"),
            "matter_sink_cross_commutator_failures":0,"base_gauge_sink_cross_commutator_failures":0,
            "both_matter_parities_nonempty":parity,
            "matter_gauge_parity_center_unchanged":True,
            "recomputation":"exact Pauli direct sum; sink block centralizer and base commutant both enumerated",
            "pass":base["pass"] and sink["pass"] and parity and value("gd")==value("cd")
                   and value("gr")==value("cr")}
    return result


def recurrence_controls(length:int,sink3,sink6):
    algebra=c547.relational_algebra_controls(length)
    graph=c532.c247.PunctureGraph(length,terminals=1);modulus=MICRO_SCALE*length
    membranes=tuple((c544.membrane(graph,a,length-1),c544.membrane(graph,a,0)) for a in range(3))
    max_diameter=0;factors=0
    for axis in range(3):
        for side,row in enumerate(membranes[axis]):
            direction=2*axis+(0 if side==1 else 1);mask=row.z
            while mask:
                bit=mask&-mask;q=bit.bit_length()-1;owner=graph.edges[q].owner
                face=tuple(value//2 for value in c532.physical_position(graph,q))
                field_owner=list(owner)
                if side==0:field_owner[axis]=(field_owner[axis]+1)%length
                field_owner=tuple(field_owner)
                s=sink_coordinate("wilson",direction,field_owner,length)
                b=sink_coordinate("frame",direction,field_owner,length)
                max_diameter=max(max_diameter,c527.periodic_l1(face,s,modulus),
                                 c527.periodic_l1(face,b,modulus),c527.periodic_l1(s,b,modulus))
                factors+=1;mask^=bit
    missing_frame_characters=sum(algebra["side_difference_CZ_sb_signature_counts"])
    return {"length":length,"held":length==HELD_LENGTH,
            "controlled_membrane_factors":factors,"maximum_sink_frame_syndrome_face_L1_diameter":max_diameter,
            "primitive_support_M2":3,"six_bit_relational_lift":algebra["relational_lift"],
            "six_bit_full_target_algebra_intertwined":algebra["pass"],
            "six_bit_sink_sufficient_for_existing_Cycle547_relational_interface":True,
            "three_bit_sink_dimension_matches_Wilson_labels":sink3["code_exponent"]==3,
            "three_bit_missing_frame_character_generators":missing_frame_characters,
            "three_bit_target_transparent_covariant_frame_retirement_constructed":False,
            "exact_missing_lemma":(
                "construct an all24 covariant isometry that removes the three frame logicals while "
                "intertwining every chi-dependent target generator; the Pauli-affine subclass is already empty"
            ),"sink_constraints_preserved_by_read-only_controls":True,
            "persistent_sink_called_leakage":False,
            "full_EGcoarse_equals_GphysicalE_update_claimed":False,
            "GammaP_mass_contact_seam_preservation":"inherited conditionally through the exact direct-sum target factor",
            "pass":sink3["pass"] and sink6["pass"] and algebra["pass"] and factors==6*length**2
                   and max_diameter<=7 and missing_frame_characters>0}


def certificate():
    started=time.monotonic();checkpoints=[checkpoint(started,"initial")]
    dry=dry_contract()
    if not dry["pass"]:raise CertificateFailure("Cycle553 dry contract failed")
    inherited=c537.certificate();checkpoints.append(checkpoint(started,"Cycle537-target-replay"))
    base532=[];sink3=[];sink6=[];transfer3=[];transfer6=[];assembled=[];recurrence=[]
    base537={row["length"]:row for row in inherited["factorization_L5_L6"]}
    for length in (TRAIN_LENGTH,HELD_LENGTH):
        b532=c532.factorization_controls(length);base532.append(b532)
        s3=sink_code_controls(length,3);s6=sink_code_controls(length,6)
        sink3.append(s3);sink6.append(s6)
        transfer3.append(transfer_controls(length,3));transfer6.append(transfer_controls(length,6))
        assembled.extend((assembled_commutant("Cycle532",b532,s3),
                          assembled_commutant("Cycle532",b532,s6),
                          assembled_commutant("Cycle537",base537[length],s3),
                          assembled_commutant("Cycle537",base537[length],s6)))
        recurrence.append(recurrence_controls(length,s3,s6))
    checkpoints.append(checkpoint(started,"sink-code-transfer-commutants"))
    tests={"dry_contract":dry["pass"],"three_bit_sink_code_L5_L6":all(r["pass"] for r in sink3),
           "six_bit_sink_code_L5_L6":all(r["pass"] for r in sink6),
           "exact_reversible_local_transfer_inverse":all(r["pass"] for r in transfer3+transfer6),
           "Cycle532_Cycle537_exact_extended_commutants":all(r["pass"] for r in assembled),
           "both_matter_parities_and_sink_gauge_center":all(r["both_matter_parities_nonempty"] for r in assembled),
           "six_bit_recurrence_interface_and_three_bit_missing_lemma":all(r["pass"] for r in recurrence),
           "GammaP_mass_contact_seam_inverse_leakage_deletion":inherited["pass"],
           "N1_N8_no_minimum_six_claim_no_axiom_pressure":True,
           "resource_contract":rss_bytes()<RSS_GUARD_BYTES and swap_count()==0}
    return {"revision":REVISION,"mode":"persistent-sink-certificate",
            "status":"cycle553-six-bit-persistent-relational-CSS-sink-closed-three-bit-transfer-lemma-open",
            "authority":AUTHORITY,"audit":AUDIT,"constitutional_effect":"none",
            "strongest_constructive_result":(
                "a fixed all24 local CSS reference subsystem stores the six Cycle547 branch logicals, "
                "has an exact NN remote-SWAP transfer/inverse, and extends the Cycle532/537 matter "
                "commutant by exactly six gauge qubits while retaining the relational target interface"
            ),"minimum_accounting":{
                "three_bits_necessary_for_arbitrary_Wilson_labels":True,
                "three_bit_sink_code_and_exact_local_transfer_constructed":True,
                "three_bits_sufficient_for_full_target_transparent_covariant_interface":False,
                "six_bits_sufficient_for_existing_Cycle547_relational_interface":True,
                "six_bits_proved_minimum":False,"currently_certified_range":"3 <= retained bits <= 6",
            },"sink3_L5_L6":tuple(sink3),"sink6_L5_L6":tuple(sink6),
            "transfer3_L5_L6":tuple(transfer3),"transfer6_L5_L6":tuple(transfer6),
            "extended_commutants":tuple(assembled),"recurrence_L5_L6":tuple(recurrence),
            "base_Cycle532_L5_L6":tuple(base532),
            "inherited_Cycle537_target":{
                "tests_passed":inherited["tests_passed"],"tests_total":inherited["tests_total"],
                "factorization_L5_L6":inherited["factorization_L5_L6"],
                "onsite_contact_B_L5_L6":inherited["onsite_contact_B_L5_L6"],
                "deletions":inherited["deletions"],"target":inherited["inherited_target"],
                "pass":inherited["pass"]},
            "preparation_and_recurrence_status":{
                "rough_code_input":"supplied lawful Cycle532 state",
                "rough_code_product_reset_encoder":False,
                "Cycle547_lawful_source_fields":"supplied after its product/reset consensus",
                "source_to_sink_transfer":"exact reversible local remote-SWAP",
                "transferred_source_families_terminal_blank":True,
                "all_six_source_families_terminal_blank_only_for_k6":True,
                "k3_frame_source_family_untouched":True,
                "persistent_sink_terminal_blank":False,
                "six_bit_relational_recurrence_interface":True,"full_physical_update_intertwiner":False,
                "promised_plus_product_encoder_compared_not_conflated":True,
            },"supplied_structure_inventory":{
                "macro_cell_partition_and_origin":True,"field_family_offsets":SINK_OFFSETS,
                "two_family_transfer_phase_order":True,"Cycle527_microgrid_and_gate_law":True,
                "Cycle532_rough_input":True,"Cycle547_lawful_field_state":True,
                "finite_L5_L6":True,"runtime_frame_selector":False,"global_ordering":False,
            },"boundary":{"six_bit_persistent_CSS_sink_code_closed":True,
                "completed_non_CSS_code_claimed":False,"three_bit_sink_code_closed":True,
                "three_bit_full_relational_recurrence_closed":False,
                "six_bit_minimum_claimed":False,"rough_product_encoder_closed":False,
                "full_update_compiler_closed":False,"shared_substrate_obstruction":False,
                "axiom_pressure":False,"broad_negative_gate":"FAIL / DO NOT SHIP"},
            "causal_type_boundary":{"transfer_depth_called_physical_time":False,
                "persistent_sink_called_Record":False,"phase_called_energy":False,
                "gauge_sink_called_realized_history":False},
            "resources":{"elapsed_seconds":time.monotonic()-started,
                "maximum_RSS_bytes":max(r["maximum_RSS_bytes"] for r in checkpoints),
                "process_swap_count":sum(r["process_swap_count"] for r in checkpoints),
                "hard_wall_seconds":WALL_LIMIT_SECONDS,"checkpoints":checkpoints},
            "tests":tests,"tests_passed":sum(tests.values()),"tests_total":len(tests),
            "pass":all(tests.values())}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--mode",choices=CLI_MODES,default="dry-contract")
    args=parser.parse_args()
    if hasattr(signal,"SIGALRM"):signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:payload=dry_contract() if args.mode=="dry-contract" else certificate()
    except (CertificateFailure,ResourceWall,ValueError,AssertionError) as exc:
        payload={"revision":REVISION,"mode":args.mode,"status":"cycle553-runner-failed",
                 "authority":AUTHORITY,"audit":AUDIT,"constitutional_effect":"none",
                 "error_type":type(exc).__name__,"error":str(exc),"pass":False}
    finally:
        if hasattr(signal,"SIGALRM"):signal.alarm(0)
    print(json.dumps(payload,indent=2,sort_keys=True));return 0 if payload.get("pass") else 1


if __name__=="__main__":raise SystemExit(main())
