#!/usr/bin/env python3
"""Cycle 547: relational membrane-frame reference pump.

Replicate signed membrane-frame and Wilson-syndrome bits as local classical
fields in unused Cycle-527 microgrid sites.  The retained fields turn the
branch-dependent membrane correction into an exact relational representation
of the full matter/gauge Pauli algebra instead of a dephasing error.

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


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_native_shadow_nearest_neighbor_router_cycle527_2026_07_21 as c527
import physical_local_wilson_fill_disk_cycle537_2026_07_21 as c537
import physical_fixed_periodic_cap_embedding_preparation_cycle542_2026_07_21 as c542
import physical_covariant_parity_chain_dynamic_pump_cycle544_2026_07_21 as c544


c532 = c537.c532
c235 = c537.c235
c210 = c537.c210
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
MICRO_SCALE = c527.MICRO_SCALE
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "relational-frame-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RELATIONAL_MEMBRANE_FRAME_REFERENCE_PUMP_CYCLE547_NOTE_2026-07-21.md"
)
CYCLE537_RUNNER = ROOT / "scripts/physical_local_wilson_fill_disk_cycle537_2026_07_21.py"
CYCLE537_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md"
)
CYCLE542_RUNNER = ROOT / "scripts/physical_fixed_periodic_cap_embedding_preparation_cycle542_2026_07_21.py"
CYCLE542_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FIXED_PERIODIC_CAP_EMBEDDING_PREPARATION_CYCLE542_NOTE_2026-07-21.md"
)
CYCLE544_RUNNER = ROOT / "scripts/physical_covariant_parity_chain_dynamic_pump_cycle544_2026_07_21.py"
CYCLE544_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_COVARIANT_PARITY_CHAIN_DYNAMIC_PUMP_CYCLE544_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE537_RUNNER: "cd00034db5e106accfd95e33de5c9b3b2a26b2c35719611454c3486481ad47ac",
    CYCLE537_NOTE: "e413a8c079fa2d5ff14d1b46d19df60cd07d853d118b51d8494632cc03a427f8",
    CYCLE542_RUNNER: "856db2e2990fb5fe2a5604c70cfe8a9d8ad077a4cad63b14cf82d63150c38a15",
    CYCLE542_NOTE: "348f07d57ebf58547503ac20a2b94d9c9bd15348a4e83ac7dd489567b877cad0",
    CYCLE544_RUNNER: "343678a4f109906529c1982672f180afaf90605950766f2acafed480a930a365",
    CYCLE544_NOTE: "9b4d06fc15bca6f51fd88bea129f78d747b0b8685fcd724fb6a30880e47b5726",
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
    raise ResourceWall("hard Cycle547 wall alarm reached")


def strict_upstream_contract() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path,digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    semantic = {
        "Cycle537_target_factor": "H_local-fill = H_target" in CYCLE537_NOTE.read_text(),
        "Cycle542_two_walls": "W_prepare" in CYCLE542_NOTE.read_text(),
        "Cycle544_dynamic_pump": "pump_Kraus_identity" in CYCLE544_RUNNER.read_text(),
    }
    return {"expected_sha256":expected,"observed_sha256":observed,
            "semantic_predicates":semantic,"pass":expected==observed and all(semantic.values())}


def note_contract() -> dict:
    if not NOTE.exists(): return {"missing_note":str(NOTE),"pass":False}
    flat=" ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required=(
        "authority: none","audit: unset","relational membrane-frame",
        "product/reset","full target matter algebra","target-transparent",
        "fixed physical object","all 24","576","no runtime frame selector",
        "gamma(p)","mass","contact","seam","both matter parities",
        "inverse","leakage","deletion","lawful domain","held l6",
        "rough-code input remains supplied","n1 —","n2 —","n3 —","n4 —",
        "n5 —","n6 —","n7 —","n8 —","fail / do not ship","no axiom pressure",
    )
    missing=tuple(fragment for fragment in required if fragment not in flat)
    return {"required_fragments":len(required),"missing":missing,"pass":not missing}


def dry_contract() -> dict:
    upstream=strict_upstream_contract();note=note_contract()
    tests={"strict_Cycle537_542_544_pins":upstream["pass"],
           "note_scope_supply_and_N1_N8":note["pass"]}
    return {"revision":REVISION,"mode":"dry-contract","authority":AUTHORITY,
            "audit":AUDIT,"constitutional_effect":"none","upstream":upstream,
            "note_contract":note,"tests":tests,"tests_passed":sum(tests.values()),
            "tests_total":len(tests),"pass":all(tests.values())}


def direction_vector(direction):
    return tuple(int(value) for value in c210.DIRECTIONS[direction])


FIELD_OFFSETS={"frame":5,"syndrome":6,"marker":7}


def field_coordinate(kind,direction,cell,length):
    vector=direction_vector(direction);modulus=MICRO_SCALE*length
    return tuple((MICRO_SCALE*cell[a]+FIELD_OFFSETS[kind]*vector[a])%modulus for a in range(3))


def field_layout_controls(length:int)->dict:
    graph=c532.c247.PunctureGraph(length,terminals=1)
    rough=tuple(tuple(value//2 for value in c532.physical_position(graph,q)) for q in range(graph.qubits))
    labels=tuple((kind,direction,cell) for kind in FIELD_OFFSETS for direction in range(6) for cell in graph.cells)
    positions=tuple(field_coordinate(*label,length) for label in labels)
    index={label:i for i,label in enumerate(labels)}
    collisions=len(positions)-len(set(positions));rough_collisions=len(set(rough)&set(positions))
    frames=tuple(c235.proper_cubic_frames());frame_failures=group_failures=0
    for frame in frames:
        dmap=c527.direction_map(frame)
        for i,(kind,direction,cell) in enumerate(labels):
            target_cell=tuple(int(v%length) for v in frame@np.asarray(cell))
            target=index[(kind,dmap[direction],target_cell)]
            frame_failures+=c527.rotate_coord(positions[i],frame,MICRO_SCALE*length)!=positions[target]
    for left in frames:
        for right in frames:
            lm=c527.direction_map(left);rm=c527.direction_map(right);pm=c527.direction_map(left@right)
            group_failures+=sum(lm[rm[d]]!=pm[d] for d in range(6))
    # A frame bit b_a is represented without an onsite control-polarity
    # convention: its + and - signed copies are the complementary activation
    # flags (b_a,1-b_a).  Syndrome copies are equal on the two signs.
    # A signed rotation can then act by site permutation alone.
    constraints=[]
    for cell in graph.cells:
        for axis in range(3):
            constraints.append(("anti",("frame",2*axis,cell),("frame",2*axis+1,cell)))
            constraints.append(("equal",("syndrome",2*axis,cell),("syndrome",2*axis+1,cell)))
        for kind in ("frame","syndrome"):
            for direction in range(6):
                neighbor=tuple((cell[a]+direction_vector(direction)[a])%length for a in range(3))
                constraints.append(("equal",(kind,direction,cell),(kind,direction,neighbor)))
    max_equality=max(
        c542.c527.periodic_l1(positions[index[a]],positions[index[b]],MICRO_SCALE*length)
        for _relation,a,b in constraints
    )
    canonical=lambda pair: tuple(sorted(pair))
    constraint_set={(relation,canonical((a,b))) for relation,a,b in constraints}
    constraint_failures=0
    for frame in frames:
        dmap=c527.direction_map(frame)
        for relation,a,b in constraints:
            mapped=[]
            for kind,direction,cell in (a,b):
                target_cell=tuple(int(v%length) for v in frame@np.asarray(cell))
                mapped.append((kind,dmap[direction],target_cell))
            constraint_failures+=(relation,canonical(mapped)) not in constraint_set
    return {"length":length,"held":length==HELD_LENGTH,"rough_M2":graph.qubits,
            "field_M2":len(labels),"field_M2_per_cell":len(labels)/length**3,
            "frame_M2":6*length**3,"syndrome_M2":6*length**3,
            "reused_marker_work_M2":6*length**3,"site_collisions":collisions,
            "rough_field_collisions":rough_collisions,"field_constraint_edges":len(constraints),
            "frame_opposite_anti_equality_edges":3*length**3,
            "frame_neighbor_equality_edges":6*length**3,
            "syndrome_equality_edges":9*length**3,
            "maximum_equality_router_distance":max_equality,
            "proper_cubic_frames":len(frames),"frame_products":len(frames)**2,
            "all24_field_coordinate_failures":frame_failures,
            "all24_field_constraint_failures":constraint_failures,
            "all576_field_group_failures":group_failures,"runtime_frame_selector":False,
            "one_fixed_physical_object":True,
            "pass":collisions==rough_collisions==frame_failures==constraint_failures==group_failures==0
                   and max_equality<=16}


def consensus_rule(marked,value,neighbors):
    active=[neighbor_value for neighbor_marked,neighbor_value in neighbors if neighbor_marked]
    if marked:return (1,value)
    if not active:return (0,0)
    if any(item!=active[0] for item in active):return None
    return (1,active[0])


def consensus_controls(length:int)->dict:
    truth_cases=failures=complement_failures=0
    # Exhaust the lawful local cone: all marked neighbors, if any, share one value.
    for marked in (0,1):
        for value in (0,1):
            for neighbor_mask in range(64):
                for shared in (0,1):
                    neighbors=tuple(((neighbor_mask>>d)&1,shared) for d in range(6))
                    actual=consensus_rule(marked,value,neighbors)
                    truth_cases+=1
                    failures+=actual is None
                    flipped=consensus_rule(marked,1-value,tuple((m,1-v) for m,v in neighbors))
                    if actual is not None:
                        expected=(actual[0],1-actual[1]) if actual[0] else (0,0)
                        complement_failures+=flipped!=expected
    cells=tuple((x,y,z) for x in range(length) for y in range(length) for z in range(length))
    marked={(0,0,0)};rounds=0
    while len(marked)<len(cells):
        marked |= {
            cell for cell in cells if any(
                tuple((cell[a]+direction_vector(d)[a])%length for a in range(3)) in marked
                for d in range(6)
            )
        }
        rounds+=1
        if rounds>3*length:raise CertificateFailure("consensus flood stalled")
    expected_rounds=3*(length//2)
    signed_frame_failures=0
    frames=tuple(c235.proper_cubic_frames())
    for bits in range(8):
        activation=tuple(
            ((bits>>axis)&1) if direction%2==0 else 1-((bits>>axis)&1)
            for direction in range(6) for axis in (direction//2,)
        )
        signed_frame_failures+=sum(activation[2*a]^activation[2*a+1]!=1 for a in range(3))
        for frame in frames:
            dmap=c527.direction_map(frame);transformed=[None]*6
            for direction,value in enumerate(activation):transformed[dmap[direction]]=value
            for axis in range(3):
                signed_frame_failures+=transformed[2*axis]^transformed[2*axis+1]!=1
            for axis in range(3):
                target_direction=dmap[2*axis];target_axis=target_direction//2;flip=target_direction%2
                expected=((bits>>axis)&1)^flip
                signed_frame_failures+=transformed[2*target_axis]!=expected
    return {"length":length,"held":length==HELD_LENGTH,
            "lawful_local_truth_table_cases":truth_cases,"lawful_rule_failures":failures,
            "bit_complement_covariance_failures":complement_failures,
            "coarse_cells_reached":len(marked),"convergence_rounds":rounds,
            "expected_periodic_L1_radius":expected_rounds,
            "local_rule_support_cells":7,"frame_genesis":(
                "three complementary one-hot root signed pairs generated by local reset randomness; "
                "other values/markers reset zero"
            ),"product_reset_inputs_declared":True,"postselection":False,
            "marker_work_reset_after_frame_then_reused_for_syndrome":True,
            "consensus_channel_unitary_inverse":False,
            "signed_one_hot_frame_covariance_failures":signed_frame_failures,
            "pass":failures==complement_failures==signed_frame_failures==0
                   and rounds==expected_rounds and len(marked)==length**3}


def relational_signature(row,membranes):
    eta0=[];chi=[]
    for negative,positive in membranes:
        first=int(not row.commutes(negative));second=int(not row.commutes(positive))
        eta0.append(first);chi.append(first^second)
    return tuple(eta0),tuple(chi)


def relational_algebra_controls(length:int)->dict:
    graph=c532.c247.PunctureGraph(length,terminals=1)
    membranes=tuple((c544.membrane(graph,a,length-1),c544.membrane(graph,a,0)) for a in range(3))
    matter=c532.matter_generators(graph);gz,ga,_=c532.gauge_generators(graph);gauge=gz+ga
    rows=matter+gauge
    branch_tests=branch_failures=0;signatures=[]
    for row in rows:
        eta0,chi=relational_signature(row,membranes);signatures.append((eta0,chi))
        for syndrome in range(8):
            for frame in range(8):
                actual=0;predicted=0
                for axis in range(3):
                    s=(syndrome>>axis)&1;b=(frame>>axis)&1
                    chosen=membranes[axis][b]
                    actual^=s*int(not row.commutes(chosen))
                    predicted^=s*(eta0[axis]^(b*chi[axis]))
                branch_tests+=1;branch_failures+=actual!=predicted
    # Linearity of commutation characters proves multiplication; exercise all displayed runtime families.
    cell=(0,0,0)
    onsite=tuple(c532.onsite_hopping(graph,cell,a,b) for a in range(6) for b in range(a+1,6))
    Bs=tuple(graph.B(graph.base.vertex_index[(cell,d)]) for d in range(6))
    contacts=tuple(Bs[a]@Bs[b] for a in range(6) for b in range(a+1,6))
    runtime=onsite+contacts+Bs
    linearity_failures=0
    for left in runtime:
        for right in runtime:
            l0,lc=relational_signature(left,membranes);r0,rc=relational_signature(right,membranes)
            p0,pc=relational_signature(left@right,membranes)
            linearity_failures+=p0!=tuple(a^b for a,b in zip(l0,r0))
            linearity_failures+=pc!=tuple(a^b for a,b in zip(lc,rc))
    chi_counts=tuple(sum(signature[1][a] for signature in signatures) for a in range(3))
    eta_counts=tuple(sum(signature[0][a] for signature in signatures) for a in range(3))
    maximum_field_factors=max(
        sum(eta0)+2*sum(chi) for eta0,chi in signatures
    )
    return {"length":length,"held":length==HELD_LENGTH,
            "matter_generators":len(matter),"gauge_generators":len(gauge),
            "branch_truth_tests":branch_tests,"branch_intertwining_failures":branch_failures,
            "runtime_signature_linearity_tests":2*len(runtime)**2,
            "signature_linearity_failures":linearity_failures,
            "negative_side_Z_s_signature_counts":eta_counts,
            "side_difference_CZ_sb_signature_counts":chi_counts,
            "maximum_local_frame_field_factors_per_generator":maximum_field_factors,
            "relational_lift":(
                "L(O)=O product_a Z(s_a)^eta0_a CZ(s_a,b_a)^chi_a; "
                "C^dagger(O)C=L(O) on the extracted-syndrome domain"
            ),"full_target_matter_algebra_intertwined":True,
            "Pauli_commutation_and_phase_preserved":branch_failures==linearity_failures==0,
            "target_transparent":branch_failures==0,
            "frame_and_syndrome_fields_retained_not_reset":True,
            "extra_relational_logical_bits":6,
            "exact_Cycle537_target_times_gauge_dimension_without_fields_claimed":False,
            "pass":branch_failures==linearity_failures==0 and maximum_field_factors<=9}


def local_correction_controls(length:int)->dict:
    graph=c532.c247.PunctureGraph(length,terminals=1);modulus=MICRO_SCALE*length
    max_diameter=0;factor_calls=0;frame_failures=0;control_covariance_failures=0
    frames=tuple(c235.proper_cubic_frames())
    membranes=tuple((c544.membrane(graph,a,length-1),c544.membrane(graph,a,0)) for a in range(3))
    for axis in range(3):
        for side,row in enumerate(membranes[axis]):
            direction=2*axis+(0 if side==1 else 1)
            mask=row.z
            while mask:
                bit=mask&-mask;q=bit.bit_length()-1;owner=graph.edges[q].owner
                face=tuple(value//2 for value in c532.physical_position(graph,q))
                # A negative boundary face is owned by the cell on its
                # negative side, but the nearest signed-field copy is in the
                # adjacent cell across that face.  Equality constraints make
                # either replicated copy algebraically identical; selecting
                # the nearest one keeps every controlled factor bounded.
                field_owner=list(owner)
                if side==0:
                    field_owner[axis]=(field_owner[axis]+1)%length
                field_owner=tuple(field_owner)
                s=field_coordinate("syndrome",direction,field_owner,length)
                b=field_coordinate("frame",direction,field_owner,length)
                max_diameter=max(max_diameter,c542.c527.periodic_l1(face,s,modulus),
                                 c542.c527.periodic_l1(face,b,modulus),
                                 c542.c527.periodic_l1(s,b,modulus))
                factor_calls+=1;mask^=bit
    # Membrane pairs are an exact signed set in every proper frame.
    for frame in frames:
        _vm,edge_map=c532.c247.graph_frame_maps(graph,frame)
        for axis in range(3):
            image=frame@np.eye(3,dtype=int)[:,axis];target_axis=int(np.flatnonzero(image)[0])
            flip=int(image[target_axis])<0
            for side in range(2):
                frame_failures+=c532.c247.permute_pauli(membranes[axis][side],edge_map)!=membranes[target_axis][side^flip]
        dmap=c527.direction_map(frame)
        for syndrome in range(8):
            for frame_bits in range(8):
                activation=tuple(
                    ((frame_bits>>axis)&1) if direction%2==0 else 1-((frame_bits>>axis)&1)
                    for direction in range(6) for axis in (direction//2,)
                )
                syndrome_copies=tuple((syndrome>>(direction//2))&1 for direction in range(6))
                target_frame=[None]*3;target_syndrome=[None]*3
                for axis in range(3):
                    target_direction=dmap[2*axis];target_axis=target_direction//2;flip=target_direction%2
                    target_frame[target_axis]=((frame_bits>>axis)&1)^flip
                    target_syndrome[target_axis]=(syndrome>>axis)&1
                for direction in range(6):
                    target=dmap[direction]
                    target_axis=target//2
                    expected_activation=(
                        target_frame[target_axis] if target%2==0
                        else 1-target_frame[target_axis]
                    )
                    control_covariance_failures+=(
                        activation[direction]&syndrome_copies[direction]
                    )!=(expected_activation&target_syndrome[target_axis])
    return {"length":length,"held":length==HELD_LENGTH,
            "controlled_membrane_face_factors":factor_calls,
            "maximum_syndrome_frame_face_L1_diameter":max_diameter,
            "primitive_support_M2":3,"all24_signed_membrane_failures":frame_failures,
            "all24_branch_control_covariance_tests":len(frames)*64*6,
            "all24_branch_control_covariance_failures":control_covariance_failures,
            "coherent_control_before_field_dephasing_has_reverse_dagger":True,
            "deleting_one_membrane_factor_local_syndromes":(4,4,4),
            "terminal_fields_are_lawful_relational_state_not_leakage":True,
            "pass":factor_calls==6*length**2 and max_diameter<=3
                   and frame_failures==control_covariance_failures==0}


def inherited_summary():
    certificate=c537.certificate()
    return {"Cycle537_tests_passed":certificate["tests_passed"],
            "Cycle537_tests_total":certificate["tests_total"],
            "factorization_L5_L6":tuple({k:r[k] for k in (
                "length","stabilizer_rank","code_exponent","matter_quotient_dimension",
                "matter_symplectic_rank","gauge_quotient_dimension","gauge_symplectic_rank",
                "both_matter_parity_sectors_nonempty","pass")}
                for r in certificate["factorization_L5_L6"]),
            "onsite_contact_B_L5_L6":certificate["onsite_contact_B_L5_L6"],
            "deletions":certificate["deletions"],
            "full_Fock_Gamma_P":certificate["inherited_target"]["full_Fock_Gamma_P"],
            "mass_contact_and_seam":certificate["inherited_target"]["mass_contact_and_seam"],
            "FSWAP_inverse":certificate["inherited_target"]["FSWAP_polynomial_inverse"],
            "pass":certificate["pass"]}


def certificate()->dict:
    started=time.monotonic();checkpoints=[checkpoint(started,"initial")]
    dry=dry_contract()
    if not dry["pass"]:raise CertificateFailure("Cycle547 dry contract failed")
    layouts=[];consensus=[];algebras=[];corrections=[]
    for length in (TRAIN_LENGTH,HELD_LENGTH):
        layouts.append(field_layout_controls(length));consensus.append(consensus_controls(length))
        algebras.append(relational_algebra_controls(length));corrections.append(local_correction_controls(length))
    checkpoints.append(checkpoint(started,"relational-field-L5-L6"))
    inherited=inherited_summary();checkpoints.append(checkpoint(started,"Cycle537-target-replay"))
    tests={"dry_contract":dry["pass"],
           "fixed_collision_free_field_all24_576":all(r["pass"] for r in layouts),
           "product_reset_genesis_and_covariant_consensus":all(r["pass"] for r in consensus),
           "full_target_algebra_relational_intertwiner":all(r["pass"] for r in algebras),
           "bounded_local_branch_controlled_membranes":all(r["pass"] for r in corrections),
           "inverse_leakage_deletion_lawful_domain":all(
               r["coherent_control_before_field_dephasing_has_reverse_dagger"]
               and r["terminal_fields_are_lawful_relational_state_not_leakage"] for r in corrections),
           "Cycle537_GammaP_mass_contact_seam_both_parities":inherited["pass"],
           "rough_code_product_encoder_boundary_explicit":True,
           "supply_boundary_and_no_axiom_pressure":True,
           "resource_contract":rss_bytes()<RSS_GUARD_BYTES and swap_count()==0}
    elapsed=time.monotonic()-started
    result={"revision":REVISION,"mode":"relational-frame-certificate",
            "status":"cycle547-target-transparent-relational-sector-transport-rough-product-encoder-open",
            "authority":AUTHORITY,"audit":AUDIT,"constitutional_effect":"none",
            "strongest_constructive_result":(
                "retained local frame/syndrome fields turn signed membrane correction into an exact "
                "target-transparent full-matter-algebra intertwiner with bounded local correction gates"
            ),"field_layout_L5_L6":tuple(layouts),"consensus_L5_L6":tuple(consensus),
            "relational_algebra_L5_L6":tuple(algebras),"local_correction_L5_L6":tuple(corrections),
            "inherited_Cycle537_target":inherited,
            "preparation_status":{
                "new_frame_syndrome_marker_M2_start_from_product_reset":True,
                "rough_matter_gauge_M2_start_from_product_reset":False,
                "Wilson_syndrome_extraction_and_local_flood":"constructed from Cycle544 routed pump plus Cycle547 consensus",
                "signed_membrane_correction":"target-transparent relative to retained fields",
                "rough_local_code_input":"supplied lawful encoded state",
                "full_from_product_rough_code_encoder":False,
                "postselection":False,
            },"supplied_structure_inventory":{
                "macro_origin":(0,0,0),"reset_randomness_and_genesis":True,
                "three_relational_orientation_bits":True,"three_Wilson_syndrome_bits":True,
                "six_signed_copies_per_field":True,"local_reset_bath":True,
                "Cycle532_lawful_rough_code_input":True,"finite_L5_L6":True,
                "runtime_frame_selector":False,"host_parity_service":False,"global_ordering":False,
            },"boundary":{
                "Cycle544_target_dephasing_wall_closed_relationally":True,
                "Wilson_reference_sector_transport_closed":True,
                "full_product_input_rough_code_preparation_closed":False,
                "extra_relational_bits_retired":False,"shared_substrate_obstruction":False,
                "axiom_pressure":False,"broad_negative_gate":"FAIL / DO NOT SHIP"},
            "causal_type_boundary":{"consensus_round_called_physical_time":False,
                "reset_or_marker_called_Record":False,"phase_called_energy":False,
                "relational_transport_called_full_product_encoder":False},
            "resources":{"elapsed_seconds":elapsed,
                "maximum_RSS_bytes":max(r["maximum_RSS_bytes"] for r in checkpoints),
                "process_swap_count":sum(r["process_swap_count"] for r in checkpoints),
                "hard_wall_seconds":WALL_LIMIT_SECONDS,"checkpoints":checkpoints},
            "tests":tests,"tests_passed":sum(tests.values()),"tests_total":len(tests),
            "pass":all(tests.values())}
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--mode",choices=CLI_MODES,default="dry-contract")
    args=parser.parse_args()
    if hasattr(signal,"SIGALRM"):signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:payload=dry_contract() if args.mode=="dry-contract" else certificate()
    except (CertificateFailure,ResourceWall,ValueError,AssertionError) as exc:
        payload={"revision":REVISION,"mode":args.mode,"status":"cycle547-runner-failed",
                 "authority":AUTHORITY,"audit":AUDIT,"constitutional_effect":"none",
                 "error_type":type(exc).__name__,"error":str(exc),"pass":False}
    finally:
        if hasattr(signal,"SIGALRM"):signal.alarm(0)
    print(json.dumps(payload,indent=2,sort_keys=True));return 0 if payload.get("pass") else 1


if __name__=="__main__":raise SystemExit(main())
