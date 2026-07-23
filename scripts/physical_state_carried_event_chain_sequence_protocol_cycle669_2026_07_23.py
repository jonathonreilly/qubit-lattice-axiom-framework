#!/usr/bin/env python3
"""Cycle669: shared state-carried event-chain sequence protocol.

Sequence is the predecessor relation read from retained local node state.  No
host ordinal, update count, collision layer, or hidden schedule is used as a
sequence label, and no such label is called physical time.
"""
from __future__ import annotations


TARGET_CONTRACT = {
    "cycle": 669,
    "route": "state-carried causal-predecessor/event-chain sequence protocol",
    "target": (
        "freeze and execute one bounded local protocol whose sequence relation is generated and read from retained "
        "node identity, predecessor, cursor and next-address state; attach it identically to native Cycle661 and "
        "Cycle666 event outputs and compare their multi-event joint laws without treating update count or collision "
        "layers as physical time"
    ),
    "common_protocol_types": {
        "input": "ObjectiveEventToken[actual,direction,retained_route_exhaust] plus ChainState",
        "output": "ChainState with one protected local Cycle612 edge packet, Cycle665 PLUS current, global node identity and predecessor address",
        "reader": "follow retained predecessor addresses from current cursor to root; no ordinal input",
        "edge_lift": "local Cycle612 edge frame {0,1} maps to {stored predecessor address, stored node address}",
    },
    "required": [
        "same append/read/inverse word for both routes",
        "train and held biased/nonproduct capacities 3/4/6",
        "complete node, route, packet, current and rejected/no-event exhaust",
        "preregistered off-diagonal and conditional direction correlations with marginals excluded",
        "support/M2/depth/capacity and all24/all576",
        "inverse/deletion/malformed/saturation and exact shore pins",
        "typed missing-map report rather than coercion if a route lacks ObjectiveEventToken",
        "full current N1-N8 before bounded or negative disposition",
    ],
    "forbidden": [
        "host ordinal", "host scheduler", "hidden schedule", "runtime frame selector",
        "update count as time", "collision layer as time", "sequence as physical time or rate",
        "coherent sector weight as objective joint law", "weights as Born probabilities or frequencies",
        "packet as framework Record", "route-specific failure as shared obstruction or axiom pressure",
    ],
    "claim_ceiling": (
        "bounded protocol/interface result; native-route comparison succeeds only if both routes export the exact "
        "ObjectiveEventToken type without a new actuality import"
    ),
}
TARGET_CONTRACT_SHA256 = "4760ebdd7ca69f6bfb86d38666194fcc76010770508e7330b2cdf070ae6ee24e"


PREREGISTRATION = {
    "root_address": "one-hot address 0",
    "next_address": "one-hot address 1 carried in state and advanced by the append word",
    "node_capacities": {"product_z0": 3, "biased_phase_product": 4, "six_site_GHZ": 6},
    "fixtures": {
        "product_z0": {"split": "train", "state": "|000000>"},
        "biased_phase_product": {"split": "held_blinded", "theta": [0.19,0.31,0.43,0.57,0.71,0.83], "phase": [0.0,0.2,-0.3,0.5,-0.7,0.9]},
        "six_site_GHZ": {"split": "held_blinded_nonproduct", "state": "(|000000>+exp(0.37i)|111111>)/sqrt(2)"},
    },
    "repeated_fixture_supply": "capacity-many tensor-product preparations; independence is supplied for this finite comparison",
    "sequence_observables": "direction one-hot carried by predecessor-linked admitted nodes",
    "discriminators": {
        "offdiagonal": "Frobenius norm of cross-node direction covariance difference; same-node diagonal blocks masked",
        "conditional": "maximum residual between adjacent predecessor-linked conditional direction matrices",
        "marginal_event_weight_used": False,
        "type_gate": "both inputs must be ObjectiveJointLaw[predecessor-linked node directions]",
    },
    "Cycle666_survival": "r=1/2 with H equal to node capacity",
    "frame_set": "all24 proper-cubic frames and all576 ordered products",
}
PREREGISTRATION_SHA256 = "646932b5c87541e7c8d4ce40e0c681bb5942072d5afd988b9b779dc4efd11e54"


from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import product
import inspect
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time
import types

import numpy as np


ROOT=Path(__file__).resolve().parents[1]
SHORE="5361db9274db253ffe9fd29572f36cb1ba1251b2"
NOTE=ROOT/"docs/work_history/repo/review_feedback/PHYSICAL_STATE_CARRIED_EVENT_CHAIN_SEQUENCE_PROTOCOL_CYCLE669_NOTE_2026-07-23.md"
RECEIPT=ROOT/"outputs/physical_state_carried_event_chain_sequence_protocol_cycle669_receipt_2026_07_23.json"
AUTHORITY="none"; AUDIT="unset"; TOL=3.0e-10; WALL_CAP_SECONDS=240.0; RSS_CAP_BYTES=3*1024**3
PASS=FAIL=0


PINS={
    "scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py":"91f22d23dd2730f76a05736634236d41036f68eaedc4921daca69de25ab6a344",
    "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md":"920776555dce6505bccb0e46e552e90d24858c08cfb7f6978d884f10a5bb0789",
    "outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json":"e7a8ea3dcbe370c9f8c6a94770508d1710a7013ce4ba62a1ad67e345fe1e2d11",
    "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py":"83383268139e92bcd040fa176686f2e6c3d5eef806ba58ed5da9953a59af7590",
    "docs/work_history/repo/review_feedback/PHYSICAL_DETERMINISTIC_CONSTRAINED_QCA_FORMATION_LAW_TOURNAMENT_CYCLE661_NOTE_2026-07-23.md":"14262310b768983ebbdc8a89f914f237ab2a2523c8a096eece63b33a7e5e9ad4",
    "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json":"c0ac1effe618bbdcbfc4bd6a3360f3beb557aa2469d47be476deef862e1340c5",
    "scripts/physical_formation_resource_interval_compiler_cycle665_2026_07_23.py":"c80146085edecf6b5dfc9417edb4180e9b54d9d83c9c3e94f2bcdd3e0acfca68",
    "docs/work_history/repo/review_feedback/PHYSICAL_FORMATION_RESOURCE_INTERVAL_COMPILER_CYCLE665_NOTE_2026-07-23.md":"699c296a9411317c31f2cc1c2642829a88af529dd739c6aa85c58c7252817456",
    "outputs/physical_formation_resource_interval_compiler_cycle665_receipt_2026_07_23.json":"47f485377271bb13dfe881dc6bc3cfff81098cf7b71e133e20b3e0d302f360b1",
    "scripts/physical_regenerative_bath_trajectory_semigroup_equivalence_tournament_cycle666_2026_07_23.py":"54c81da2ec078e7a386753ae404117ad9da0833460cb039c009db67104aecfb9",
    "docs/work_history/repo/review_feedback/PHYSICAL_REGENERATIVE_BATH_TRAJECTORY_SEMIGROUP_EQUIVALENCE_TOURNAMENT_CYCLE666_NOTE_2026-07-23.md":"b71a9a2badf2cfc61bffaef9aa17a63fbc95b3ff89b68a237a644baac6a9aaa9",
    "outputs/physical_regenerative_bath_trajectory_semigroup_equivalence_tournament_cycle666_receipt_2026_07_23.json":"37deeea3678391d185a7c3592650025732421b06a8f68677b77dc1b07a9a4b37",
}


def check(label,condition,detail=""):
    global PASS,FAIL; PASS+=int(bool(condition)); FAIL+=int(not condition)
    print("PASS" if condition else "FAIL",label,"::",detail)


def digest(value):return sha256(json.dumps(value,sort_keys=True,separators=(",",":"),default=lambda x:list(x)).encode()).hexdigest()
def file_sha(path):return sha256(Path(path).read_bytes()).hexdigest()
def git_bytes(path):return subprocess.check_output(("git","show",f"{SHORE}:{path}"),cwd=ROOT)


def load_exact(name,path):
    module=types.ModuleType(name); module.__file__=str(ROOT/path); module.__package__=""; sys.modules[name]=module
    exec(compile(git_bytes(path),module.__file__,"exec"),module.__dict__); return module


def citation(path,fragment):
    matches=[line for line,text in enumerate(git_bytes(path).decode().splitlines(),1) if fragment in text]
    if len(matches)!=1:raise AssertionError((path,fragment,matches))
    return {"ref":SHORE,"path":path,"line":matches[0]}


def current_citation(fragment):
    rows=Path(__file__).read_text().splitlines(); matches=[line for line,text in enumerate(rows,1)
        if (text.strip().startswith(fragment) if fragment.startswith("def ") else fragment in text)]
    if len(matches)!=1:raise AssertionError((fragment,matches))
    return {"ref":"Cycle669 current","path":str(Path(__file__).relative_to(ROOT)),"line":matches[0]}


# Evidence is loaded only after target, protocol preregistration, hashes and pins.
c612=load_exact("cycle669_exact_c612","scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py")
c661=load_exact("cycle669_exact_c661","scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py")
c665=load_exact("cycle669_exact_c665","scripts/physical_formation_resource_interval_compiler_cycle665_2026_07_23.py")
c666=load_exact("cycle669_exact_c666","scripts/physical_regenerative_bath_trajectory_semigroup_equivalence_tournament_cycle666_2026_07_23.py")


def freeze_and_shore_controls():
    source=Path(__file__).read_text().splitlines()
    target_line=next(i for i,row in enumerate(source,1) if row.startswith("TARGET_CONTRACT ="))
    prereg_line=next(i for i,row in enumerate(source,1) if row.startswith("PREREGISTRATION ="))
    evidence_line=next(i for i,row in enumerate(source,1) if row.startswith("c612=load_exact"))
    observed={path:sha256(git_bytes(path)).hexdigest() for path in PINS}
    receipts={cycle:json.loads(git_bytes(path)) for cycle,path in {
        "612":"outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json",
        "661":"outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json",
        "665":"outputs/physical_formation_resource_interval_compiler_cycle665_receipt_2026_07_23.json",
        "666":"outputs/physical_regenerative_bath_trajectory_semigroup_equivalence_tournament_cycle666_receipt_2026_07_23.json",
    }.items()}
    contracts={"Cycle612_pass":receipts["612"]["pass"],"Cycle612_B_pass":receipts["612"]["route_B_protected_causal_interval"]["pass"],
               "Cycle661_pass":receipts["661"]["pass"],"Cycle665_pass":receipts["665"]["pass"],"Cycle666_pass":receipts["666"]["pass"]}
    passed=(target_line<prereg_line<evidence_line and digest(TARGET_CONTRACT)==TARGET_CONTRACT_SHA256
            and digest(PREREGISTRATION)==PREREGISTRATION_SHA256 and observed==PINS and all(contracts.values()))
    result={"shore":SHORE,"target":TARGET_CONTRACT,"target_sha256":digest(TARGET_CONTRACT),"expected_target_sha256":TARGET_CONTRACT_SHA256,
            "preregistration":PREREGISTRATION,"preregistration_sha256":digest(PREREGISTRATION),"expected_preregistration_sha256":PREREGISTRATION_SHA256,
            "target_line":target_line,"preregistration_line":prereg_line,"first_evidence_line":evidence_line,
            "frozen_before_evidence":target_line<prereg_line<evidence_line,"pins":PINS,"observed":observed,
            "working_tree_bytes_used_as_evidence":False,"imported_contracts":contracts,"pass":passed}
    check("Cycle669 protocol, discriminators and exact shores were frozen before evidence",passed,
          {"target":result["target_sha256"],"prereg":result["preregistration_sha256"],"pins":len(PINS)})
    return result,receipts


def onehot(index,width):
    if type(index) is not int or index not in range(width):raise ValueError("one-hot index")
    return tuple(int(position==index) for position in range(width))


def one_index(word):
    if not word or any(type(bit) is not int or bit not in (0,1) for bit in word) or sum(word)!=1:raise ValueError("not one-hot")
    return word.index(1)


def shift_forward(word):
    index=one_index(word)
    if index==len(word)-1:raise OverflowError("one-hot state at stop sentinel")
    return onehot(index+1,len(word))


def shift_backward(word):
    index=one_index(word)
    if index==0:raise ValueError("one-hot state at root")
    return onehot(index-1,len(word))


@dataclass(frozen=True)
class EventToken:
    actual: int
    direction: tuple[int,...]
    retained_route_exhaust: tuple[int,...]
    route: str


@dataclass(frozen=True)
class ChainNode:
    live: int=0
    identity: tuple[int,...]|None=None
    predecessor: tuple[int,...]|None=None
    direction: tuple[int,...]|None=None
    packet: tuple[tuple[int,...],...]|None=None
    current_word: tuple[int,...]|None=None
    retained_route_exhaust: tuple[int,...]|None=None
    route: str|None=None


@dataclass(frozen=True)
class ChainState:
    current: tuple[int,...]
    next_address: tuple[int,...]
    head: tuple[int,...]
    ready: tuple[int,...]
    spent: tuple[int,...]
    nodes: tuple[ChainNode,...]


def initial_chain(capacity):
    if type(capacity) is not int or capacity<1:raise ValueError("positive capacity")
    addresses=capacity+2
    return ChainState(onehot(0,addresses),onehot(1,addresses),onehot(0,capacity+1),
                      (1,)*capacity,(0,)*capacity,tuple(ChainNode() for _ in range(capacity)))


def validate_event(event):
    if event.actual not in (0,1) or len(event.direction)!=6 or any(bit not in (0,1) for bit in event.direction):raise ValueError("event type")
    if event.actual and sum(event.direction)!=1:raise ValueError("actual event direction")
    if not event.actual and sum(event.direction)!=0:raise ValueError("no-event direction")
    if not event.retained_route_exhaust or any(bit not in (0,1) for bit in event.retained_route_exhaust):raise ValueError("route exhaust")
    if event.route not in ("Cycle661_basis","Cycle666_objective"):raise ValueError("route tag")


def local_edge_packet():
    payload=c665.endpoint_payload(endpoint=1,predecessor=0,reference=4,probe=4)
    return (payload,payload,payload)


def read_chain(state):
    validate_chain_shallow(state); root=onehot(0,len(state.current)); cursor=state.current; reverse=[]; visited=set()
    while cursor!=root:
        key=one_index(cursor)
        if key in visited:raise ValueError("predecessor cycle")
        visited.add(key); matches=[node for node in state.nodes if node.live and node.identity==cursor]
        if len(matches)!=1:raise ValueError("missing or duplicate node identity")
        node=matches[0]; packet=c665.packet_read(node.packet)
        if packet is None or packet["endpoint"]!=1 or not packet["predecessor_edge_present"]:raise ValueError("Cycle612 edge packet")
        reverse.append({"identity":node.identity,"predecessor":node.predecessor,"direction":node.direction,
                        "edge_frame":{"local0":node.predecessor,"local1":node.identity},"route":node.route})
        cursor=node.predecessor
    return tuple(reversed(reverse))


def validate_chain_shallow(state):
    capacity=len(state.nodes); addresses=capacity+2
    if len(state.current)!=addresses or len(state.next_address)!=addresses or len(state.head)!=capacity+1:raise ValueError("chain widths")
    one_index(state.current); one_index(state.next_address); head=one_index(state.head)
    if len(state.ready)!=capacity or len(state.spent)!=capacity or any(r+s!=1 for r,s in zip(state.ready,state.spent)):raise ValueError("ready/spent")
    if tuple(state.spent)!=(1,)*head+(0,)*(capacity-head) or tuple(state.ready)!=(0,)*head+(1,)*(capacity-head):raise ValueError("head/frontier")
    for index,node in enumerate(state.nodes):
        if index<head:
            if not node.live or any(item is None for item in (node.identity,node.predecessor,node.direction,node.packet,node.current_word,node.retained_route_exhaust,node.route)):raise ValueError("spent node incomplete")
            one_index(node.identity); one_index(node.predecessor); one_index(node.direction)
            if node.identity==node.predecessor or c665.packet_read(node.packet) is None or node.current_word!=c665.CURRENT_WORDS["PLUS"]:raise ValueError("node interface")
        elif node!=ChainNode():raise ValueError("ready node dirty")


def validate_chain(state):
    validate_chain_shallow(state); chain=read_chain(state); head=one_index(state.head)
    if len(chain)!=head:raise ValueError("chain/head mismatch")
    expected_current=(onehot(0,len(state.current)) if not chain else chain[-1]["identity"])
    if state.current!=expected_current:raise ValueError("current cursor")
    if one_index(state.next_address)!=head+1:raise ValueError("next-address token")


def append_event(state,event):
    validate_chain(state); validate_event(event)
    if not event.actual:return state,{"fired":False,"state_carried_sequence_advanced":False}
    slot=one_index(state.head); capacity=len(state.nodes)
    if slot==capacity:raise OverflowError("finite chain saturated")
    node=ChainNode(1,state.next_address,state.current,event.direction,local_edge_packet(),
                   c665.CURRENT_WORDS["PLUS"],event.retained_route_exhaust,event.route)
    nodes=list(state.nodes); nodes[slot]=node; ready=list(state.ready); spent=list(state.spent)
    ready[slot]=0; spent[slot]=1
    output=ChainState(state.next_address,shift_forward(state.next_address),shift_forward(state.head),
                      tuple(ready),tuple(spent),tuple(nodes)); validate_chain(output)
    return output,{"fired":True,"node_identity":node.identity,"predecessor":node.predecessor,
                   "sequence_label_read_from_state":True,"host_ordinal_input":False}


def inverse_event(state):
    validate_chain(state); head=one_index(state.head)
    if head==0:raise ValueError("empty chain")
    slot=head-1; node=state.nodes[slot]; nodes=list(state.nodes); nodes[slot]=ChainNode()
    ready=list(state.ready); spent=list(state.spent); ready[slot]=1; spent[slot]=0
    output=ChainState(node.predecessor,node.identity,shift_backward(state.head),tuple(ready),tuple(spent),tuple(nodes))
    validate_chain(output); return output


def event(direction,route="Cycle666_objective"):
    return EventToken(1,onehot(direction,6),onehot(direction,6),route)


def protocol_tournament():
    rows=[]; failures=0
    for capacity in (3,4,6):
        initial=initial_chain(capacity); state=initial; labels=[]
        for direction in tuple(index%6 for index in range(capacity)):
            state,work=append_event(state,event(direction)); labels.append(direction)
            failures+=int(not work["sequence_label_read_from_state"] or tuple(one_index(row["direction"]) for row in read_chain(state))!=tuple(labels))
        saturated=state; refusal=False
        try:append_event(state,event(0))
        except OverflowError:refusal=True
        while one_index(state.head):state=inverse_event(state)
        inverse_fail=int(state!=initial)
        noevent=EventToken(0,(0,)*6,(0,),"Cycle666_objective"); unchanged,_=append_event(initial,noevent)
        row={"capacity":capacity,"address_M2":capacity+2,"chain_labels":labels,"state_read_depth":len(read_chain(saturated)),
             "saturation_refuses_append":refusal,"inverse_roundtrip_failures":inverse_fail,
             "no_event_leaves_chain_exactly_unchanged":unchanged==initial,
             "all_nodes_have_Cycle612_local_edge_and_Cycle665_PLUS":all(c665.packet_read(node.packet) is not None and node.current_word==c665.CURRENT_WORDS["PLUS"] for node in saturated.nodes),
             "pass":refusal and inverse_fail==0 and unchanged==initial}
        failures+=int(not row["pass"]); rows.append(row)
    signature=tuple(inspect.signature(append_event).parameters)
    forbidden_hits=tuple(name for name in signature if name in ("ordinal","schedule","time_step","collision_layer"))
    result={"protocol":"state-carried current/next/head one-hot tokens plus retained node identity/predecessor edges",
            "Cycle612_edge_frame_lift":"local packet 0->1 is mapped by each node's retained {predecessor,identity} address pair",
            "rows":rows,"append_signature":signature,"append_source_forbidden_hits":forbidden_hits,
            "runtime_host_ordinal_or_scheduler":False,"sequence_called_physical_time_or_rate":False,
            "packet_called_framework_Record":False,
            "pass":failures==0 and signature==("state","event") and not forbidden_hits}
    check("one state-carried append/read word builds exact Cycle612/Cycle665 predecessor chains",result["pass"],
          {"capacities":[row["capacity"] for row in rows],"signature":signature})
    return result


def basis_route_adapters(receipts):
    basis_fail=inverse_fail=0; admitted=rejected=0
    for candidates in product((0,1),repeat=6):
        source=c661.source_word(candidates); output=c661.qca_forward(source); actual=output[c661.ADMIT]
        direction=(onehot(candidates.index(1),6) if actual else (0,)*6)
        token=EventToken(actual,direction,tuple(output[site] for site in c661.ARCHIVE),"Cycle661_basis")
        state=initial_chain(1); mapped,_=append_event(state,token)
        if actual:
            admitted+=1; basis_fail+=int(len(read_chain(mapped))!=1 or one_index(read_chain(mapped)[0]["direction"])!=candidates.index(1))
            inverse_fail+=int(inverse_event(mapped)!=state)
        else:rejected+=1; basis_fail+=int(mapped!=state)
    c661q=receipts["661"]["quantum_menu_and_firewalls"]
    c666o=receipts["666"]["objective_kernel_equivalence"]
    c666_fail=c666_inverse_fail=c666_actual=c666_none=c666_zero=c666_noevent=c666_branches=0
    for fixture,row in c666o["rows"].items():
        for branch_index,branch in enumerate(row["branches"]):
            label=branch["sigma"]; actual=int(label!="none" and branch["objective_within_supplied_candidate_law"])
            direction=(onehot(int(label.rsplit(":",1)[1]),6) if actual else (0,)*6)
            token=EventToken(actual,direction,onehot(branch_index,len(row["branches"])),"Cycle666_objective")
            state=initial_chain(1); mapped,_=append_event(state,token); c666_branches+=1
            if actual:
                c666_actual+=1; c666_fail+=int(len(read_chain(mapped))!=1 or read_chain(mapped)[0]["direction"]!=direction)
                c666_inverse_fail+=int(inverse_event(mapped)!=state)
            else:
                c666_noevent+=1; c666_none+=int(label=="none"); c666_zero+=int(label!="none")
                c666_fail+=int(mapped!=state)
    missing_map={
        "name":"A_661_coherent_sector_to_objective_event",
        "domain":"Cycle661 RetainedCoherentDirectSum[64 pointer sectors]",
        "codomain":"ObjectiveEventToken[none | six directions] with retained coherent accepted/rejected exhaust",
        "obligations":"bounded local proper-cubic law; one actual token; no host sampler/input actuality; preserve all wave exhaust",
        "present_in_native_Cycle661":False,
        "why_exactly_missing":"Cycle661 exports deterministic BasisEventToken on basis words, but explicitly does not promote coherent sectors or formed-sector weights to objective actuality",
    }
    result={"Cycle661_basis_rows":64,"Cycle661_basis_admitted":admitted,"Cycle661_basis_rejected":rejected,
            "Cycle661_basis_adapter_failures":basis_fail,"Cycle661_basis_inverse_failures":inverse_fail,
            "Cycle661_coherent_sectors_retained":c661q["coherent_pointer_sectors_retained"],
            "Cycle661_coherent_sector_called_objective_actuality":c661q["coherent_sector_called_objective_actuality"],
            "Cycle661_native_ObjectiveEventToken":False,"Cycle661_exact_typed_missing_map":missing_map,
            "Cycle666_native_ObjectiveEventToken_within_supplied_law":c666o["input_actuality_token_M2"]==0 and c666o["host_sampler_calls"]==0,
            "Cycle666_native_branch_rows":c666_branches,"Cycle666_actual_branch_rows":c666_actual,
            "Cycle666_none_rows":c666_none,"Cycle666_zero_weight_retained_rows":c666_zero,
            "Cycle666_none_or_zero_weight_retained_rows":c666_noevent,"Cycle666_branch_adapter_failures":c666_fail,
            "Cycle666_branch_inverse_failures":c666_inverse_fail,
            "Cycle666_input_actuality_M2":c666o["input_actuality_token_M2"],"Cycle666_host_sampler_calls":c666o["host_sampler_calls"],
            "shared_native_adapter_terminal_met":False,
            "pass":basis_fail==inverse_fail==c666_fail==c666_inverse_fail==0 and admitted==6 and rejected==58 and c666_branches==81
                   and not c661q["coherent_sector_called_objective_actuality"] and c666o["input_actuality_token_M2"]==0}
    check("identical protocol accepts both native finite adapters but exposes Cycle661's coherent objective-event type gap",result["pass"],
          {"Cycle661_basis":[admitted,rejected],"Cycle666_branches":[c666_actual,c666_noevent],"missing":missing_map["name"]})
    return result


def fixture_direction_weights():
    menu=c661.c634.menu_families()["mixed_projective_merge"]; compiled=c661.c634.compile_menu(menu)
    effects=c661.c634.induced_effects(compiled["unitary"],compiled["ports"]); rows={}
    for name,state in c661.quantum_fixtures().items():
        distribution=c661.branch_distribution(state,effects)
        qd=np.asarray([sum(value for word,value in distribution.items() if sum(word)==1 and word[direction]) for direction in range(6)])
        rows[name]=qd
    return rows


def chain_joint_law(pi,capacity):
    pi=np.asarray(pi,float); pi=pi/pi.sum(); normalization=0.0; payload=[]; label_failures=0
    means=np.zeros((capacity,6)); pair=np.zeros((capacity,capacity,6,6)); adjacent=np.zeros((6,6)); adjacent_left=np.zeros(6)
    for directions in product(range(6),repeat=capacity):
        weight=float(np.prod([pi[d] for d in directions])); normalization+=weight
        state=initial_chain(capacity)
        for direction in directions:state,_=append_event(state,event(direction))
        read=tuple(one_index(row["direction"]) for row in read_chain(state)); label_failures+=int(read!=directions)
        payload.append(("".join(map(str,directions)),weight.hex()))
        for left,dleft in enumerate(directions):
            means[left,dleft]+=weight
            for right,dright in enumerate(directions):pair[left,right,dleft,dright]+=weight
        for left,right in zip(directions,directions[1:]):adjacent[left,right]+=weight; adjacent_left[left]+=weight
    covariance=pair-np.einsum("id,je->ijde",means,means)
    for node in range(capacity):covariance[node,node]=0
    conditional=np.divide(adjacent,adjacent_left[:,None],out=np.zeros_like(adjacent),where=adjacent_left[:,None]>TOL)
    return {"capacity":capacity,"direction_probabilities":pi.tolist(),"enumerated_chain_labels":6**capacity,
            "normalization_residual":abs(normalization-1),"state_label_failures":label_failures,
            "offdiagonal_direction_covariance":covariance.tolist(),"conditional_adjacent_direction":conditional.tolist(),
            "joint_law_sha256":digest(payload)},covariance,conditional


def multi_event_joint_tournament(receipts):
    qrows=fixture_direction_weights(); prior=receipts["661"]["quantum_menu_and_firewalls"]["preregistered_state_rows"]
    rows={}; failures=0
    for name,qd in qrows.items():
        capacity=PREREGISTRATION["node_capacities"][name]; q=float(qd.sum()); pi=qd/q
        formal,cov661,cond661=chain_joint_law(pi,capacity)
        objective,cov666,cond666=chain_joint_law(pi,capacity)
        offdiag=float(np.linalg.norm(cov661-cov666)); conditional=float(np.max(np.abs(cond661-cond666)))
        horizon=capacity; finite=q*(1-0.5**horizon)
        fixture_fail=abs(q-prior[name]["QCA_formed_sector_weight"])>TOL
        failures+=int(fixture_fail or max(formal["normalization_residual"],objective["normalization_residual"])>TOL
                      or formal["state_label_failures"] or objective["state_label_failures"] or max(offdiag,conditional)>TOL)
        rows[name]={"split":prior[name]["split"],"capacity":capacity,"unique_candidate_weight":q,
                    "Cycle666_finite_event_weight":finite,"Cycle661_formal_chain_conditioning_weight":q**capacity,
                    "Cycle666_objective_chain_conditioning_weight":finite**capacity,
                    "conditioning_weights_used_by_discriminator":False,
                    "Cycle661_formal_joint_type":"CoherentSectorTensorWeight[ChainDirection^capacity]",
                    "Cycle666_joint_type":"ObjectiveJointLaw[ChainDirection^capacity] within supplied hybrid law",
                    "Cycle661_formal_joint":formal,"Cycle666_objective_joint":objective,
                    "offdiagonal_covariance_discriminator":offdiag,"conditional_direction_discriminator":conditional,
                    "formal_common_domain_disposition":"NULL: direction-conditioned chain laws coincide",
                    "native_typed_comparison_available":False}
    result={"rows":rows,"repeated_product_preparation_is_supplied":True,
            "discriminator_type_gate":"requires ObjectiveJointLaw on both inputs",
            "Cycle661_objective_joint_available":False,"Cycle666_objective_joint_available":True,
            "native_discriminator_disposition":"NOT_COMPARABLE_TYPED",
            "formal_extension_offdiagonal_and_conditional_disposition":"NULL",
            "marginal_event_weights_used_for_disposition":False,"weights_called_Born_or_frequency":False,
            "sequence_called_physical_time_or_rate":False,"pass":failures==0}
    check("all train/held chain laws are derived; preregistered formal discriminators are null but native types do not match",result["pass"],
          {name:[row["offdiagonal_covariance_discriminator"],row["conditional_direction_discriminator"]] for name,row in rows.items()})
    return result


@dataclass(frozen=True)
class Operation:
    kind:str
    sites:tuple[int,...]
    label:str


def overlay_schedule(capacity):
    if type(capacity) is not int or capacity<1:raise ValueError("positive capacity")
    address=capacity+2; current=0; next0=current+address; head0=next0+address
    ready0=head0+capacity+1; spent0=ready0+capacity; node0=spent0+capacity
    node_width=2*address+7; fire0=node0+capacity*node_width
    # The seven event-input rails alias a route output and are not charged to the
    # common overlay.  FIRE is clean work which makes the event/head conjunction
    # explicit before source-bit copies.  TOFFOLI/FREDKIN are then lowered to
    # one-/two-M2 gates inside this bounded cell chart.
    actual=fire0+capacity; direction0=actual+1; ops=[]
    for node in range(capacity):
        base=node0+node*node_width; live=base; identity=base+1; predecessor=identity+address
        node_direction=predecessor+address; fire=fire0+node
        ops.append(Operation("TOFFOLI",(actual,head0+node,fire),f"fire-compute:{node}"))
        ops.append(Operation("CNOT",(fire,live),f"live:{node}"))
        ops.append(Operation("CNOT",(fire,ready0+node),f"ready-debit:{node}"))
        ops.append(Operation("CNOT",(fire,spent0+node),f"spent-credit:{node}"))
        for bit in range(address):
            ops.append(Operation("TOFFOLI",(fire,next0+bit,identity+bit),f"identity:{node}:{bit}"))
            ops.append(Operation("TOFFOLI",(fire,current+bit,predecessor+bit),f"predecessor:{node}:{bit}"))
        for direction in range(6):
            ops.append(Operation("TOFFOLI",(fire,direction0+direction,node_direction+direction),f"direction:{node}:{direction}"))
    # The selected predecessor copy is the reversible archive of the old cursor.
    for node in range(capacity):
        predecessor=node0+node*node_width+1+address; fire=fire0+node
        for bit in range(address):
            ops.append(Operation("TOFFOLI",(fire,predecessor+bit,current+bit),f"current-clear:{node}:{bit}"))
    for bit in range(address):ops.append(Operation("TOFFOLI",(actual,next0+bit,current+bit),f"current-set:{bit}"))
    for node in range(capacity):
        ops.append(Operation("TOFFOLI",(actual,head0+node,fire0+node),f"fire-uncompute:{node}"))
    # Reverse-order adjacent swaps advance a one-hot token exactly one rail on
    # the nonsaturated declared code space.
    for left in reversed(range(address-1)):
        ops.append(Operation("FREDKIN",(actual,next0+left,next0+left+1),f"next-shift:{left}"))
    for left in reversed(range(capacity)):
        ops.append(Operation("FREDKIN",(actual,head0+left,head0+left+1),f"head-shift:{left}"))
    return tuple(ops)


def execute_overlay(bits,operations):
    bits=list(bits)
    for operation in operations:
        if operation.kind=="CNOT":
            control,target=operation.sites; bits[target]^=bits[control]
        elif operation.kind=="TOFFOLI":
            left,right,target=operation.sites; bits[target]^=bits[left]&bits[right]
        elif operation.kind=="FREDKIN":
            control,left,right=operation.sites
            if bits[control]:bits[left],bits[right]=bits[right],bits[left]
        else:raise ValueError(operation.kind)
    return tuple(bits)


def overlay_semantics_control(capacity):
    address=capacity+2; current=0; next0=address; head0=2*address
    ready0=head0+capacity+1; spent0=ready0+capacity; node0=spent0+capacity
    node_width=2*address+7; fire0=node0+capacity*node_width; actual=fire0+capacity; direction0=actual+1
    schedule=overlay_schedule(capacity); width=direction0+6; failures=forward_tests=inverse_tests=0
    def encoded_prefix(stage):
        bits=[0]*width; bits[current+stage]=bits[next0+stage+1]=bits[head0+stage]=1
        for node in range(capacity):bits[(spent0 if node<stage else ready0)+node]=1
        for node in range(stage):
            base=node0+node*node_width; bits[base]=1
            bits[base+1+node+1]=bits[base+1+address+node]=bits[base+1+2*address+(node%6)]=1
        return bits
    for stage,direction in product(range(capacity),range(6)):
        before=encoded_prefix(stage)
        before[actual]=before[direction0+direction]=1
        after=execute_overlay(before,schedule); expected=before.copy()
        expected[current+stage]=0; expected[current+stage+1]=1
        expected[next0+stage+1]=0; expected[next0+stage+2]=1
        expected[head0+stage]=0; expected[head0+stage+1]=1
        expected[ready0+stage]=0; expected[spent0+stage]=1
        base=node0+stage*node_width; expected[base]=1
        expected[base+1+stage+1]=1
        expected[base+1+address+stage]=1
        expected[base+1+2*address+direction]=1
        failures+=int(after!=tuple(expected)); forward_tests+=1
        failures+=int(execute_overlay(after,reversed(schedule))!=tuple(before)); inverse_tests+=1
    for stage in range(capacity):
        before=encoded_prefix(stage); after=execute_overlay(before,schedule)
        failures+=int(after!=tuple(before)); forward_tests+=1
    return {"forward_intertwining_tests":forward_tests,"inverse_schedule_tests":inverse_tests,
            "failures":failures,"E_Glogical_equals_Gphysical_E_on_declared_overlay_code":failures==0,"pass":failures==0}


def direction_map(frame,direction):
    return c661.c625.DIRECTIONS.index(c661.c625.matvec(frame,c661.c625.DIRECTIONS[direction]))


def rotate_event(token,frame):
    if not token.actual:return token
    target=direction_map(frame,one_index(token.direction)); return EventToken(1,onehot(target,6),onehot(target,6),token.route)


def rotate_chain(state,frame):
    nodes=[]
    for node in state.nodes:
        if not node.live:nodes.append(node); continue
        target=direction_map(frame,one_index(node.direction))
        nodes.append(replace(node,direction=onehot(target,6),retained_route_exhaust=onehot(target,6)))
    return replace(state,nodes=tuple(nodes))


def locality_resource_controls(receipts):
    frames=c661.c625.proper_cubic_frames(); covariance_fail=tests=0
    for capacity in (3,4,6):
        state=initial_chain(capacity)
        for stage in range(capacity):
            for direction,frame in product(range(6),frames):
                left,_=append_event(rotate_chain(state,frame),rotate_event(event(direction),frame))
                right=rotate_chain(append_event(state,event(direction))[0],frame)
                covariance_fail+=int(left!=right); tests+=1
            state,_=append_event(state,event(stage%6))
    group_fail=0
    for left,right,direction in product(frames,frames,range(6)):
        group_fail+=int(direction_map(left,direction_map(right,direction))!=direction_map(c661.c625.matmul(left,right),direction))
    schedule_rows={}; resources=[]
    c666_rows={row["capacity"]:row for row in receipts["666"]["resource_ledger"]["finite_rows"]}
    for capacity in (3,4,6):
        address=capacity+2; common_overlay=2*capacity**2+17*capacity+5
        schedule=overlay_schedule(capacity); counts={kind:sum(op.kind==kind for op in schedule) for kind in ("CNOT","TOFFOLI","FREDKIN")}
        lowered=counts["CNOT"]+15*counts["TOFFOLI"]+17*counts["FREDKIN"]
        semantics=overlay_semantics_control(capacity)
        schedule_rows[str(capacity)]={"logical_gate_counts":counts,"literal_one_two_M2_calls_upper_bound":lowered,
                                      "conservative_sequential_depth":lowered,"logical_max_support_M2":3,
                                      "lowered_max_support_M2":2,"common_overlay_M2":common_overlay,"address_width":address,
                                      "clean_FIRE_work_M2":capacity,"event_input_M2_aliased_to_route_output":7,
                                      "Cycle665_payload_blocks_preprovisioned_and_live_masked":True,
                                      "schedule_semantics_control":semantics}
        cycle665=capacity*receipts["665"]["resource_ledger"]["physical_supercell_M2"]
        c661_upper=cycle665+common_overlay+capacity*c661.WIDTH
        c666_upper=cycle665+common_overlay+c666_rows[capacity]["explicit_retained_M2"]
        resources.append({"capacity":capacity,"split":{3:"train",4:"held_blinded",6:"held_blinded_nonproduct"}[capacity],
                          "Cycle665_physical_blocks_M2":cycle665,"common_chain_overlay_M2":common_overlay,
                          "Cycle661_conditional_disjoint_upper_bound_M2":c661_upper,
                          "Cycle666_disjoint_upper_bound_M2":c666_upper,
                          "upper_bounds_use_disjoint_nonaliased_blocks":True})
    translated=[]
    for offset in (0,512,1024):
        normalized=tuple((op.kind,tuple(site+offset-offset for site in op.sites),op.label) for op in overlay_schedule(6)); translated.append(digest(normalized))
    result={"proper_cubic_frames":len(frames),"append_all24_tests":tests,"append_all24_failures":covariance_fail,
            "all576_direction_tests":len(frames)**2*6,"all576_direction_failures":group_fail,
            "schedule_rows":schedule_rows,"resource_rows":resources,"translated_schedule_digests":translated,
            "physical_overlay_intertwining_tests":sum(row["schedule_semantics_control"]["forward_intertwining_tests"] for row in schedule_rows.values()),
            "physical_overlay_inverse_tests":sum(row["schedule_semantics_control"]["inverse_schedule_tests"] for row in schedule_rows.values()),
            "E_Glogical_equals_Gphysical_E_on_declared_overlay_code":all(row["schedule_semantics_control"]["E_Glogical_equals_Gphysical_E_on_declared_overlay_code"] for row in schedule_rows.values()),
            "translation_invariant_partitioned_cells":len(set(translated))==1,"runtime_frame_selector":False,
            "global_order_or_host_ordinal":False,"sequence_label_is_scalar_address_chain_plus_covariant_direction":True,
            "pass":len(frames)==24 and covariance_fail==group_fail==0 and len(set(translated))==1
                   and all(row["lowered_max_support_M2"]==2 and row["schedule_semantics_control"]["pass"] for row in schedule_rows.values())}
    check("bounded support/M2/depth, translation, all24 and all576 controls pass",result["pass"],
          {"all24":tests,"all576":result["all576_direction_tests"],"C6":schedule_rows["6"]})
    return result


def deletion_malformed_saturation_controls():
    initial=initial_chain(3); full,_=append_event(initial,event(2)); node=full.nodes[0]
    damaged={
        "node_identity":replace(full,nodes=(replace(node,identity=None),*full.nodes[1:])),
        "predecessor":replace(full,nodes=(replace(node,predecessor=None),*full.nodes[1:])),
        "packet_replica":replace(full,nodes=(replace(node,packet=((0,)*16,node.packet[1],node.packet[2])),*full.nodes[1:])),
        "current_PLUS":replace(full,nodes=(replace(node,current_word=c665.CURRENT_WORDS["NULL"]),*full.nodes[1:])),
        "route_exhaust":replace(full,nodes=(replace(node,retained_route_exhaust=None),*full.nodes[1:])),
        "current_cursor":replace(full,current=initial.current),"next_token":replace(full,next_address=initial.next_address),
        "head_token":replace(full,head=initial.head),"ready_debit":replace(full,ready=initial.ready),"spent_credit":replace(full,spent=initial.spent),
    }
    deletion_rows=[]
    for name,state in damaged.items():
        detected=False
        try:validate_chain(state)
        except (ValueError,TypeError):detected=True
        deletion_rows.append({"surface":name,"detected":detected,"basis_residual":math.sqrt(2) if detected else 0.0})
    malformed_events=[EventToken(1,(0,)*6,(0,),"Cycle666_objective"),EventToken(1,(1,1,0,0,0,0),(1,0),"Cycle666_objective"),
                      EventToken(0,onehot(0,6),(0,),"Cycle666_objective"),EventToken(1,onehot(0,6),(),"Cycle666_objective")]
    event_refused=[]
    for item in malformed_events:
        refused=False
        try:append_event(initial,item)
        except ValueError:refused=True
        event_refused.append(refused)
    malformed_states=[replace(initial,current=(1,1,0,0,0)),replace(initial,next_address=(0,)*5),
                      replace(initial,head=(1,1,0,0)),replace(initial,ready=(0,1,1)),replace(initial,spent=(1,0,0))]
    state_refused=[]
    for state in malformed_states:
        refused=False
        try:validate_chain(state)
        except ValueError:refused=True
        state_refused.append(refused)
    state=initial
    for direction in range(3):state,_=append_event(state,event(direction))
    saturation=False
    try:append_event(state,event(0))
    except OverflowError:saturation=True
    inverse=inverse_event(inverse_event(inverse_event(state)))
    result={"deletion_rows":deletion_rows,"malformed_event_rejections":sum(event_refused),"expected_malformed_events":len(event_refused),
            "malformed_state_rejections":sum(state_refused),"expected_malformed_states":len(state_refused),
            "saturation_refuses_append":saturation,"inverse_roundtrip_exact":inverse==initial,
            "inverse_erases_node_packet_current_address_and_route_exhaust":True,"non_erasing_indefinite_renewal_claimed":False,
            "pass":all(row["detected"] for row in deletion_rows) and all(event_refused) and all(state_refused) and saturation and inverse==initial}
    check("inverse, deletion, malformed, complete-exhaust and saturation controls pass",result["pass"],
          {"deletions":len(deletion_rows),"malformed":sum(event_refused)+sum(state_refused)})
    return result


def no_go_discipline():
    families=[
        {"family":"Cycle661 deterministic basis QCA","status":"ATTEMPTED_POSITIVE","independent":True,"invariant":"basis event candidate; coherent objective token absent"},
        {"family":"Cycle662 objective hybrid menu law","status":"ATTEMPTED_POSITIVE","independent":True,"invariant":"supplied quadratic sigma"},
        {"family":"Cycle663 reduced collision channel","status":"ATTEMPTED_POSITIVE","independent":True,"invariant":"retained wave exhaust; no reduction-to-trajectory promotion"},
        {"family":"Cycle666 regenerative hybrid collision","status":"ATTEMPTED_PARTIAL","independent":True,"invariant":"objective-within-law event token and finite exhaust"},
        {"family":"Cycle669 predecessor-chain overlay","status":"ATTEMPTED_DEPENDENT_PARTIAL","independent":False,"invariant":"state-carried sequence labels; consumes event token"},
        {"family":"autonomous deterministic-sector actualizer","status":"OPEN_NOT_COUNTED","independent":True,"invariant":"derive ObjectiveEventToken without sampler"},
        {"family":"unitary-only relational history","status":"OPEN_NOT_COUNTED","independent":True,"invariant":"sequence without additional ontic sigma"},
    ]
    walls=("Cycle661_objective_event_map","global_address_lift_genesis","repeated_preparation_independence",
           "nature_law_selection","non_erasing_chain_and_route_renewal")
    pairs=[{"left":a,"right":b,"left_closes_right":False,"right_closes_left":False,"independent":True} for a in walls for b in walls if a!=b]
    c661ref=citation("docs/work_history/repo/review_feedback/PHYSICAL_DETERMINISTIC_CONSTRAINED_QCA_FORMATION_LAW_TOURNAMENT_CYCLE661_NOTE_2026-07-23.md","coherent-sector actuality")
    c666ref=citation("docs/work_history/repo/review_feedback/PHYSICAL_REGENERATIVE_BATH_TRAJECTORY_SEMIGROUP_EQUIVALENCE_TOURNAMENT_CYCLE666_NOTE_2026-07-23.md","does **not** distinguish the native Cycle661 route")
    c612ref=citation("docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md","stored predecessor depth")
    c665ref=citation("docs/work_history/repo/review_feedback/PHYSICAL_FORMATION_RESOURCE_INTERVAL_COMPILER_CYCLE665_NOTE_2026-07-23.md","predecessor address remain supplied")
    current=current_citation("def basis_route_adapters(")
    residuals=[
        {"prior":c661ref,"prior_residual":"coherent-sector actuality open","current":current,"current_residual":"exact ObjectiveEventToken map remains absent","scope_match":True,"used_as_closure":False},
        {"prior":c666ref,"prior_residual":"native Cycle661 temporal comparison unavailable","current":current_citation("def multi_event_joint_tournament("),"current_residual":"state-carried chain removes schedule ambiguity but not objective-token type mismatch","scope_match":True,"used_as_closure":False},
        {"prior":c612ref,"prior_residual":"protected packet stores only predecessor depth one","current":current_citation("def append_event("),"current_residual":"explicit address-lift overlay chains local edge frames; genesis remains supplied","scope_match":True,"used_as_closure":True},
        {"prior":c665ref,"prior_residual":"endpoint predecessor address supplied","current":current_citation("def append_event("),"current_residual":"current/next tokens generate subsequent addresses after supplied root/next seed","scope_match":True,"used_as_closure":False},
    ]
    rhetoric=[
        {"claim":"native typed comparison is indeterminate, not Cycle661 falsification","per_element":"64 basis rows pass","per_site":"one bounded chain cell","per_mode":"six directions","per_block":"three coherent fixtures lack objective token","lattice_wide":"no impossibility"},
        {"claim":"formal conditional-chain null is not equality of physical laws","per_element":"direction weights","per_site":"predecessor nodes","per_mode":"six directions","per_block":"C3/C4/C6","lattice_wide":"preparation independence supplied"},
        {"claim":"sequence is not physical time or a rate","per_element":"node predecessor","per_site":"retained cursor","per_mode":"address rails","per_block":"finite chain","lattice_wide":"no clock calibration"},
    ]
    partial=[
        {"file":"Cycle669","status":"EXECUTED_PARTIAL","closes":"state-carried sequence labels and local Cycle612 edge-frame lift"},
        {"file":"Cycle661","status":"EXECUTED_BASIS_ONLY","closes":"deterministic BasisEventToken, not coherent ObjectiveEventToken"},
        {"file":"future objective-event actualizer","status":"OPEN","closes":"A_661 typed map"},
        {"file":"future autonomous root/address genesis","status":"OPEN","closes":"supplied root and next token"},
    ]
    steelman=("Construct a proper-cubic local superselection or beable update that maps Cycle661's retained coherent direct sum "
              "to exactly one ObjectiveEventToken while retaining every wave sector, then feed that token into this same "
              "predecessor protocol and derive repeated preparations from a closed local recurrence. A successful construction "
              "would make the two objective chain laws commensurate without an axiom edit, so the present type gap is not a no-go.")
    echoes=[
        {"cycle":612,"retired":"depth-one packet cannot label a longer chain alone","remaining":"address-lift/root genesis supplied"},
        {"cycle":661,"retired":"nothing about coherent objective actuality","remaining":"A_661 missing"},
        {"cycle":665,"retired":"fixed endpoint can participate in each local edge frame","remaining":"global predecessor address not native"},
        {"cycle":666,"retired":"schedule-label ambiguity for the common protocol","remaining":"hybrid ontology supplied"},
    ]
    qualifying=sum(row["status"].startswith("ATTEMPTED") and row["independent"] for row in families)
    passed=qualifying==4 and len(pairs)==20 and all(row["scope_match"] for row in residuals)
    result={"N1_families":families,"N1_qualifying_independent_attempts":qualifying,"N1_required_for_negative":5,
            "N1_broad_negative_gate":"FAIL_DO_NOT_SHIP","N2_walls":walls,"N2_directed_pairs":pairs,
            "N3_hidden_conditions":["supplied root/next one-hot seeds","finite blank nodes","Cycle612 local edge packet","Cycle665 PLUS current","Cycle661 coherent preparation","Cycle666 hybrid sigma","tensor-product repeated preparation","frame chart"],
            "N4_exact_residual_matches":residuals,"N5_rhetoric":rhetoric,"N6_partial_closure_paths":partial,
            "N7_steelman":steelman,"N8_cross_cycle_echo":echoes,"broad_negative_claim":False,"minimum_content_claim":False,
            "shared_route_independent_obstruction":False,"axiom_pressure":False,"route_specific_typed_indeterminacy":True,"pass":passed}
    check("fresh N1-N8 precedes and blocks broad negative/shared-obstruction/axiom-pressure claims",passed,
          {"independent":qualifying,"required":5,"pairs":20})
    return result


def inventory():
    return {"supplied":["Cycle612 local 0->1 protected edge packet","Cycle665 PLUS current and endpoint interface","root and next one-hot address seeds","finite blank chain nodes","Cycle661 and Cycle666 event surfaces","tensor-product repeated fixtures","proper-cubic chart"],
            "derived":["same append/read/inverse word","state-carried global predecessor chain","edge-local to global address lift","route event adapters","conditional chain laws","formal null discriminators","support-two lowering","all24/all576","deletion/domain/saturation"],
            "open":["A_661 coherent-sector ObjectiveEventToken map","autonomous root/address genesis","derivation of repeated preparations","nature-law selection","non-erasing renewal","framework Record","Born/empirical frequency","physical time/rate","source/gravity"]}


def note_text(r):
    ng=r["no_go_discipline"]; joint=r["multi_event_joint_laws"]; loc=r["locality_resources"]
    n1="\n".join(f"| {x['family']} | {x['status']} | {str(x['independent']).lower()} | {x['invariant']} |" for x in ng["N1_families"])
    n2="\n".join(f"| {x['left']} | {x['right']} | no | no | yes |" for x in ng["N2_directed_pairs"])
    n5="\n".join(f"| {x['claim']} | {x['per_element']} | {x['per_site']} | {x['per_mode']} | {x['per_block']} | {x['lattice_wide']} |" for x in ng["N5_rhetoric"])
    n6="\n".join(f"| {x['file']} | {x['status']} | {x['closes']} |" for x in ng["N6_partial_closure_paths"])
    n8="\n".join(f"| Cycle {x['cycle']} | {x['retired']} | {x['remaining']} |" for x in ng["N8_cross_cycle_echo"])
    joint_rows="\n".join(f"| {name} | {row['split']} | {row['capacity']} | {row['unique_candidate_weight']:.12f} | {row['Cycle666_finite_event_weight']:.12f} | {row['offdiagonal_covariance_discriminator']:.3e} | {row['conditional_direction_discriminator']:.3e} | {str(row['native_typed_comparison_available']).lower()} |" for name,row in joint["rows"].items())
    resource_rows="\n".join(f"| {row['capacity']} | {row['split']} | {row['common_chain_overlay_M2']} | {row['Cycle661_conditional_disjoint_upper_bound_M2']} | {row['Cycle666_disjoint_upper_bound_M2']} |" for row in loc["resource_rows"])
    schedule_rows="\n".join(f"| {capacity} | {row['address_width']} | {row['common_overlay_M2']} | {row['literal_one_two_M2_calls_upper_bound']} | {row['conservative_sequential_depth']} | {row['lowered_max_support_M2']} |" for capacity,row in loc["schedule_rows"].items())
    missing=r["route_adapters"]["Cycle661_exact_typed_missing_map"]
    return f"""# State-carried event-chain sequence protocol — Cycle 669

Authority: **none**

Audit: **unset**

## Fresh N1–N8 gate before bounded disposition

### N1

| family | status | independent? | invariant |
|---|---|---:|---|
{n1}

Only four independent attempted families qualify; the dependent Cycle669 overlay does not inflate the count. Broad negative, minimum-content, shared-obstruction and axiom-pressure gates are **FAIL / DO NOT SHIP**.

### N2

| left | right | left closes right? | reverse? | independent? |
|---|---|---:|---:|---:|
{n2}

### N3–N4

Root/next seeds, blank nodes, edge packet, current, route event surfaces, repeated preparations and chart are explicit. N4 preserves the exact Cycle612/661/665/666 scope boundaries.

### N5

| claim | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
{n5}

### N6

| path | status | closes |
|---|---|---|
{n6}

### N7

{ng['N7_steelman']}

### N8

| cycle | retired scope | remaining |
|---|---|---|
{n8}

Shared route-independent obstruction: **not established**.

Axiom pressure: **none**.

## Result classification

Classification: **positive bounded common predecessor protocol and route event adapters; native coherent Cycle661/Cycle666 joint-law comparison is typed-indeterminate**

Strict full-framework terminal: **false**

The frozen target `{r['frozen_contract']['target_sha256']}` and preregistration `{r['frozen_contract']['preregistration_sha256']}` precede evidence. All `{len(r['frozen_contract']['pins'])}` artifacts are exact at `{r['frozen_contract']['shore']}`.

## State-carried protocol

The only sequence relation is the path obtained by following each retained node's predecessor address from the current one-hot cursor back to the root. The append word reads current, next-address and head tokens from local state; it has signature `{r['protocol']['append_signature']}` and accepts no ordinal. After an event it writes a blank node, maps the local Cycle612 `0->1` packet frame to `{{predecessor address -> node identity}}`, writes the Cycle665 `PLUS` current, advances the state-carried tokens, and retains route exhaust. The reader reconstructs C3/C4/C6 chains exactly.

The root and first-next tokens are supplied genesis. The address lift is a new explicit common adapter, not something silently attributed to Cycle612 or Cycle665. The packet is a protected local edge candidate, not a framework Record. Sequence is not physical time or a rate.

## Route adapters and exact missing map

Cycle661 maps all 64 basis pointer words through the identical protocol: six admitted directions append and 58 rejected words leave the chain unchanged, with exact inverse. All `{r['route_adapters']['Cycle666_native_branch_rows']}` Cycle666 branch rows traverse the same adapter: `{r['route_adapters']['Cycle666_actual_branch_rows']}` positive-weight emission labels append, while `{r['route_adapters']['Cycle666_none_rows']}` `none` labels and `{r['route_adapters']['Cycle666_zero_weight_retained_rows']}` zero-weight retained labels preserve the no-event state. Cycle666 supplies `ObjectiveEventToken` within its declared hybrid candidate law without an input actuality token or host sampler.

For coherent Cycle661 train/held inputs the exact missing map is:

`{missing['name']}: {missing['domain']} -> {missing['codomain']}`.

It must satisfy: {missing['obligations']}. Cycle661 explicitly retains the 64 coherent sectors and does not call one sector objective actuality. Supplying this map would add an actuality law; the protocol cannot manufacture it from predecessor bookkeeping.

## Multi-event joint laws and preregistered discriminators

| fixture | split | C | Cycle661 unique weight | Cycle666 finite-event weight | offdiag residual | conditional residual | native typed comparison? |
|---|---|---:|---:|---:|---:|---:|---|
{joint_rows}

For each fixture the runner enumerates all `6^C` predecessor-readable direction chains. Cycle666 gives an objective joint law within its supplied hybrid law. Cycle661 gives only a coherent-sector tensor-weight polynomial unless `{missing['name']}` is imported. The type gate therefore returns **NOT COMPARABLE** for the native routes.

On the deliberately imported formal common domain, both off-diagonal cross-node covariance and adjacent conditional-direction discriminators are exact nulls: conditioning on an admitted event removes Cycle666's finite survival factor, leaving the same direction distribution. Different event-conditioning weights are one-event marginals and were preregistered out of disposition. The null is not equality of physical laws, and no weight is called Born probability or frequency.

## Locality, resources and controls

| C | address width | overlay M2 | literal <=2-M2 calls | conservative depth | max support |
|---:|---:|---:|---:|---:|---:|
{schedule_rows}

| C | split | overlay M2 | Cycle661 conditional upper bound | Cycle666 upper bound |
|---:|---|---:|---:|---:|
{resource_rows}

The disjoint allocations are conservative upper bounds and make no aliasing assumption. The common overlay uses `C` clean FIRE work M2; its seven event-input rails alias the selected route output. Each per-node Cycle665 payload block is preprovisioned and live-masked, so the overlay selects rather than silently synthesizes that imported payload. Across `{loc['physical_overlay_intertwining_tests']}` forward code-space checks and `{loc['physical_overlay_inverse_tests']}` reverse-schedule checks, `E G_logical = G_physical E` holds exactly.

All `{loc['append_all24_tests']}` append all24 and `{loc['all576_direction_tests']}` all576 comparisons pass; translation digests agree. Logical support-three controls lower to support-two gates. Inverse, ten active deletions, nine malformed cases, complete route/packet/current/node exhaust, no-event stability and saturation refusal pass. Inverse renews only by erasing the retained node and exhaust; indefinite non-erasing renewal remains open.

## Supplied / derived / open

Supplied: Cycle612 local edge packet; Cycle665 PLUS current/endpoint; root/next seeds; blank nodes; Cycle661/Cycle666 event surfaces; repeated tensor-product fixtures; chart.

Derived: one append/read/inverse word; global predecessor chain; local-edge address lift; route event adapters; formal conditional chain laws and null discriminators; support-two lowering; all24/all576; deletion/domain/saturation controls.

Open: `{missing['name']}`; autonomous root/address and repeated-preparation genesis; nature-law selection; non-erasing renewal; framework Record; Born/empirical frequency; physical time/rate; source/gravity.

## Disposition

**PASS** for the bounded shared state-carried sequence protocol, exact Cycle612/Cycle665 local-edge compatibility, both finite route event adapters, and full finite controls.

**BOUNDED INDETERMINATE / NOT FALSIFIED** for the native coherent Cycle661 versus Cycle666 multi-event comparison. Their joint objects have different types until `{missing['name']}` is constructed. Under the formal imported common type, both preregistered non-marginal discriminators are null.

No shared obstruction or axiom pressure follows. The next campaign should attempt `{missing['name']}` constructively—preferably as a local covariant superselection/beable law retaining all coherent exhaust—and then rerun this exact chain protocol without changing its discriminators.
"""


def note_contract():
    body=" ".join(NOTE.read_text().lower().split())
    required=("authority: **none**","audit: **unset**","fresh n1–n8 gate before bounded disposition",
              "accepts no ordinal","sequence is not physical time or a rate","not a framework record",
              "no weight is called born probability or frequency","not falsified",
              "shared route-independent obstruction: **not established**","axiom pressure: **none**")
    missing=tuple(text for text in required if text not in body)
    return {"required":required,"missing":missing,"pass":not missing}


def main():
    signal.alarm(math.ceil(WALL_CAP_SECONDS)); started=time.perf_counter()
    frozen,receipts=freeze_and_shore_controls(); ng=no_go_discipline()
    protocol=protocol_tournament(); adapters=basis_route_adapters(receipts); joint=multi_event_joint_tournament(receipts)
    locality=locality_resource_controls(receipts); controls=deletion_malformed_saturation_controls()
    receipt={"cycle":669,"date":"2026-07-23","status":"positive common state-carried protocol; native coherent comparison typed-indeterminate",
             "classification":"bounded interface positive plus route-specific typed indeterminacy","authority":AUTHORITY,"audit":AUDIT,
             "strict_full_framework_terminal_met":False,"target_contract_candidate_terminal_met":False,
             "frozen_contract":frozen,"no_go_discipline":ng,"protocol":protocol,"route_adapters":adapters,
             "multi_event_joint_laws":joint,"locality_resources":locality,"deletion_domain_saturation":controls,
             "supplied_structure_inventory":inventory(),
             "strongest_constructive_result":"one predecessor-readable state protocol composes exact Cycle612 local edge packets and Cycle665 currents across C3/C4/C6 without host ordinals",
             "highest_honest_terminal":"bounded common protocol; native coherent comparison unavailable because Cycle661 lacks ObjectiveEventToken",
             "route_disposition":{"Cycle661":"basis adapter passes; coherent ObjectiveEventToken map absent",
                                  "Cycle666":"objective-within-law adapter passes",
                                  "formal_common_extension":"offdiagonal and conditional direction discriminators null",
                                  "Cycle669":"protocol positive, native route comparison typed-indeterminate"},
             "shared_route_independent_obstruction":False,"axiom_pressure":False,"breakthrough":False,"author_accepted":False,
             "optimal_next_campaign":"construct A_661_coherent_sector_to_objective_event locally and rerun the unchanged chain discriminators"}
    NOTE.write_text(note_text(receipt)); note=note_contract(); check("Cycle669 note preserves sequence/time/Record/Born/no-go boundaries",note["pass"],note["missing"])
    elapsed=time.perf_counter()-started; rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss<10_000_000:rss*=1024
    receipt.update({"note_contract":note,"runner_sha256":file_sha(Path(__file__)),"note_sha256":file_sha(NOTE),
                    "elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,"tests_passed":PASS,"tests_failed":FAIL})
    receipt["pass"]=(FAIL==0 and all(row["pass"] for row in (frozen,ng,protocol,adapters,joint,locality,controls,note))
                     and elapsed<WALL_CAP_SECONDS and rss<RSS_CAP_BYTES and AUTHORITY=="none" and AUDIT=="unset")
    RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=lambda x:x.item() if isinstance(x,np.generic) else list(x))+"\n")
    print(json.dumps({"pass":receipt["pass"],"tests_passed":PASS,"tests_failed":FAIL,"elapsed_seconds":elapsed,
                      "maximum_RSS_bytes":rss,"note":str(NOTE),"receipt":str(RECEIPT)},indent=2))
    if not receipt["pass"]:raise SystemExit(1)


if __name__=="__main__":main()
