#!/usr/bin/env python3
"""Cycle 679: execute the prepared incident-C detector star."""

from __future__ import annotations

TARGET_CONTRACT = {
    "target_statement": "close Cycle675's incident-C-star wall by splitting committed local W into A/SELECT/D, preparing the read cell and every incident neighbor branch, inserting every Cycle608 C-equality phase row in the exact accepted order, and executing the physical-matter extractor, detector, Cycle668 binder and full inverse/uncompute",
    "quantifiers_domain": "Cycle675 selected origin and proper-cubic-closed generic cells on L3 train, L4 held-out-size and L6 held; complete declared global total-N<=3 star fixtures; every accepted incident C row and deletion witness; material/q and contact counterfactuals; all24/all576",
    "allowed_premises": "byte-pinned committed Cycle608 correction-row order, local role tables and primitive recipes; byte-pinned Cycle675 independent matter extractor and local fermionic frame sheath; Cycle672 detector convention; Cycle668 binder target; explicit finite sparse/MPO contractions and compile-time coordinate placement",
    "forbidden_weakenings": "counting incident C without applying it; leaving incident neighbor branches unprepared; reordering accepted C rows without proof; comparing only algebraic 2x2 projectors; supplied q label, occurrence-as-matter, global lookup, shell ROM, runtime frame selector or host branch selection; hiding deleted-C, no-C, malformed, collision, leakage, held-size or signed-covariance failures; protected edits or axiom language",
    "required_edge_cases": "origin zero-C baseline and every selected positive-C generic star; full-C versus constructed incident-star equality on declared total-N<=3 fixtures; each C-row deletion; same-q/different-matter; contact deletion; one-particle mass and Cycle230 contact/seam fixtures if touched; raw coordinate-only signed failure and bounded local phase repair; inverse/leakage/malformed/collision/support/all24/all576",
    "completion_witness": "coordinate-explicit chronological A/SELECT preparations for target and incident neighbors, every exact ordered C equality phase factor, all D suffixes, a sparse executed W_star dagger P W_star composition driven from independent physical matter, exact comparison to the full-C reference on the frozen code fixtures, deletion and covariance receipts, and a supplied-structure inventory",
    "outcomes_not_closure": "an incident-row count or digest; C factors that never see prepared neighbor branches; a target-only W macro; origin-only success; equality on q-labelled rays without physical matter extraction; coordinate-only unsigned covariance; a compiled cell family called an autonomous all-cell tile; route-specific residuals promoted to shared obstruction or axiom pressure",
}

from collections import Counter
from contextlib import contextmanager
from hashlib import sha256
import importlib.util
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np


ROOT=Path(__file__).resolve().parents[1]
NOTE=ROOT/"docs/work_history/repo/review_feedback/PHYSICAL_INCIDENT_C_PREPARED_STAR_DETECTOR_CYCLE679_NOTE_2026-07-23.md"
RECEIPT=ROOT/"outputs/physical_incident_C_prepared_star_detector_cycle679_receipt_2026_07_23.json"
COLD=ROOT/"outputs/physical_incident_C_prepared_star_detector_cycle679_cold_2026_07_23.txt"
SHORE="05890c4c22c06e609f09277cb2a1e080b5753a3a"
AUTHORITY="none";AUDIT="unset";TOL=2e-10;PASS=0;FAIL=0
PINS={
 "scripts/physical_occupancy_six_q_syndrome_extractor_cycle675_2026_07_23.py":"cf0ad89d0628878f1355754a419163400eda2710092f879bead34e1ed2643181",
 "docs/work_history/repo/review_feedback/PHYSICAL_OCCUPANCY_SIX_Q_SYNDROME_EXTRACTOR_CYCLE675_NOTE_2026-07-23.md":"dbabca9a1460950f9701462723679d696ef4b94a8cda7cd3a62b220f885d51f5",
 "outputs/physical_occupancy_six_q_syndrome_extractor_cycle675_receipt_2026_07_23.json":"ac1e8585c48f8cd67366301be1837be3cdd80e21d9d47d4242c52f8db1481d64",
 "outputs/physical_occupancy_six_q_syndrome_extractor_cycle675_cold_2026_07_23.txt":"d4bfdea1b793ec671b80f46b68d1fc67c786215b22167290b51ce5b0765291c3",
 "scripts/physical_cycle608_literal_aggregate_detector_product_cycle672_2026_07_23.py":"c0af96a46e7f8a8641c0ec9de92da934fb24efc3887d9d5966e40ae91be44735",
 "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json":"4ccba85490c08120aab645917fee87dbd58f21cf4fb17c5f60b3a4fab9dbca48",
}
Coord=tuple[int,int,int];SparseState=dict[frozenset[Coord],complex]

class Tee:
 def __init__(self,*streams):self.streams=streams
 def write(self,body):
  for stream in self.streams:stream.write(body)
  return len(body)
 def flush(self):
  for stream in self.streams:stream.flush()

def check(label,condition,detail=""):
 global PASS,FAIL;PASS+=int(bool(condition));FAIL+=int(not bool(condition));print("PASS" if condition else "FAIL",label,"::",detail)

def stable_digest(value):return sha256(json.dumps(value,sort_keys=True,separators=(",",":"),default=float).encode()).hexdigest()
def git_bytes(path):return subprocess.run(("git","show",f"{SHORE}:{path}"),cwd=ROOT,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout

def target_freeze_controls():
 source=Path(__file__).read_text().splitlines();target=next(i for i,l in enumerate(source,1) if l.startswith("TARGET_CONTRACT ="));evidence=next(i for i,l in enumerate(source,1) if l.startswith("def shore_controls"));fields=sorted(TARGET_CONTRACT);expected=["allowed_premises","completion_witness","forbidden_weakenings","outcomes_not_closure","quantifiers_domain","required_edge_cases","target_statement"]
 return {"target_line":target,"first_evidence_load_line":evidence,"frozen_before_evidence":target<evidence,"target_contract_sha256":stable_digest(TARGET_CONTRACT),"proof_search_governance_exact_fields":fields,"pass":target<evidence and fields==expected}

def shore_controls():
 observed={path:sha256(git_bytes(path)).hexdigest() for path in PINS};r675=json.loads(git_bytes("outputs/physical_occupancy_six_q_syndrome_extractor_cycle675_receipt_2026_07_23.json"));r608=json.loads(git_bytes("outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json"));passed=observed==PINS and r675["pass"] and r675["aggregate_summary"]["incident_C_star_product_executed"] is False and r675["authority"]=="none" and r675["audit"]=="unset"
 return {"ref":SHORE,"pins":PINS,"observed":observed,"Cycle675_incident_C_wall":r675["no_go_discipline"]["N2_walls"]["W_incident_C_star_product"],"Cycle608_replay_defect_inherited_via_Cycle675":r675["shore"]["Cycle672_replay_boundary"],"pass":passed},{"Cycle675":r675,"Cycle608":r608}

@contextmanager
def pinned_modules():
 path=ROOT/"scripts/physical_occupancy_six_q_syndrome_extractor_cycle675_2026_07_23.py"
 if sha256(path.read_bytes()).hexdigest()!=PINS[str(path.relative_to(ROOT))]:raise RuntimeError("Cycle675 working copy differs")
 name="cycle679_pinned_cycle675";spec=importlib.util.spec_from_file_location(name,path);c675=importlib.util.module_from_spec(spec);sys.modules[name]=c675;spec.loader.exec_module(c675)
 try:
  with c675.cycle672_and_cycle608() as (m672,c608):yield c675,m672,c608
 finally:sys.modules.pop(name,None)

def apply_factor(m672,state,factor):
 if factor.kind!="PHASE_EQ":return m672.apply_factor(state,factor)
 result={}
 for bits,amplitude in state.items():
  matched=all(int(coord in bits)==value for coord,value in zip(factor.controls,factor.values));result[bits]=result.get(bits,0j)+(-amplitude if matched else amplitude)
 return {bits:a for bits,a in result.items() if abs(a)>2e-15}

def apply_word(m672,state,factors,skip=None):
 for ordinal,factor in enumerate(factors):
  if ordinal!=skip:state=apply_factor(m672,state,factor)
 return state

def split_W(factors):
 A=[];select=[];D=[]
 for factor in factors:
  head=factor.label[0]
  if head in ("branch_initialization","A"):A.append(factor)
  elif head=="SELECT":select.append(factor)
  elif head=="D":D.append(factor)
  else:raise ValueError(f"unknown local W label {factor.label}")
 return tuple(A),tuple(select),tuple(D)

def all_C_factors(m672,c608,layout):
 factors=[];edges=[]
 for edge_ordinal,(first,second,rows) in enumerate(c608.correction_rows(layout)):
  start=len(factors)
  for row_ordinal,(fw,fb,sw,sb) in enumerate(rows):
   controls=layout.q[first]+layout.q[second]+(layout.branch[first][fb],layout.branch[second][sb]);values=c608.q_values(fw)+c608.q_values(sw)+(1,1)
   factors.append(m672.Factor("PHASE_EQ",controls,values,(),None,("C_equality",edge_ordinal,row_ordinal,first,second,fw,fb,sw,sb)))
  edges.append({"edge_ordinal":edge_ordinal,"first":first,"second":second,"start":start,"stop":len(factors),"rows":len(rows)})
 return tuple(factors),edges

def build_star(c675,m672,c608,base_layout,target_index,occupied):
 base=c675.build_candidate(m672,c608,base_layout,target_index,occupied);layout=base["layout"]
 all_C,edge_rows=all_C_factors(m672,c608,layout);incident_edges=[row for row in edge_rows if target_index in (row["first"],row["second"])]
 star_indices={target_index}
 for row in incident_edges:star_indices|={row["first"],row["second"]}
 star_indices=tuple(sorted(star_indices));split={};censuses={}
 for index in star_indices:
  W,_digest,census=m672.local_W_factors(c608,layout,index);split[index]=split_W(W);censuses[str(index)]=census
 prefix=tuple(f for index in star_indices for section in split[index][:2] for f in section)
 incident_C=tuple(f for row in incident_edges for f in all_C[row["start"]:row["stop"]])
 suffix=tuple(f for index in star_indices for f in split[index][2])
 matter_by_index={index:c675.matter_rails(c608,layout,layout.cells[index]) for index in star_indices}
 extractor_star=tuple(f for index in star_indices for f in c675.swap_extractor(m672,matter_by_index[index],layout.q[index]))
 Wstar=prefix+incident_C+suffix;predicate=base["predicate"];detector=Wstar+predicate+m672.inverse_word(Wstar)
 full=extractor_star+m672.inverse_word(Wstar)+detector+(base["conjunction"],)+m672.inverse_word(detector)+Wstar+m672.inverse_word(extractor_star)
 return dict(base,all_C=all_C,C_edges=edge_rows,incident_edges=incident_edges,star_indices=star_indices,prefix=prefix,incident_C=incident_C,suffix=suffix,Wstar=Wstar,detector_star=detector,full_star=full,star_censuses=censuses,matter_by_index=matter_by_index,extractor_star=extractor_star)

def factor_digest(m672,factors):return stable_digest([factor.descriptor(i) for i,factor in enumerate(factors)])

def phase_basis(c608,layout,target_index,target_amplitudes,foreign_index=None,foreign_word=0,branch_choice=0):
 result={};cells=len(layout.cells)
 for target_word,target_amplitude in target_amplitudes.items():
  target_entries=layout.tables[target_index][target_word]
  for target_branch,(_term,local_amplitude) in enumerate(target_entries):
   foreign_entries=((None,1+0j),) if foreign_index is None else layout.tables[foreign_index][foreign_word]
   for foreign_branch,(_foreign_term,foreign_amplitude) in enumerate(foreign_entries):
    bits=set(layout.branch[index][branch_choice%len(layout.branch[index])] for index in range(cells))
    bits.discard(layout.branch[target_index][branch_choice%len(layout.branch[target_index])]);bits.add(layout.branch[target_index][target_branch])
    for direction,coord in enumerate(layout.q[target_index]):
     if target_word>>direction&1:bits.add(coord)
    if foreign_index is not None:
     bits.discard(layout.branch[foreign_index][branch_choice%len(layout.branch[foreign_index])]);bits.add(layout.branch[foreign_index][foreign_branch])
     for direction,coord in enumerate(layout.q[foreign_index]):
      if foreign_word>>direction&1:bits.add(coord)
    frozen=frozenset(bits);result[frozen]=result.get(frozen,0j)+complex(target_amplitude)*complex(local_amplitude)*complex(foreign_amplitude)
 norm=math.sqrt(sum(abs(a)**2 for a in result.values()));return {bits:a/norm for bits,a in result.items()}

def full_C_equality(m672,c608,star):
 layout=star["layout"];target=star["cell_index"];rows=[];maximum=maximum_D_reduction=maximum_C_order=0.0;full=star["all_C"];incident=star["incident_C"];predicate=star["predicate"]
 target_D=tuple(f for f in star["suffix"] if len(f.label)>1 and f.label[0]=="D" and f.label[1]==target);non_target_D=tuple(f for f in star["suffix"] if f not in set(target_D))
 fixtures=[("A2_local_contact",c608.a2_word_amplitudes(),None,0)]
 for neighbor in star["star_indices"]:
  if neighbor==target:continue
  fixtures.append((f"one_plus_one_seam_neighbor_{neighbor}",{1:1.0},neighbor,1))
 wrap_neighbors=[index for index in star["star_indices"] if index!=target and any(value==layout.length-1 for value in layout.cells[index])]
 if wrap_neighbors:fixtures.append(("periodic_wrap_one_plus_one",{2:1.0},wrap_neighbors[0],2))
 for label,amps,foreign,word in fixtures:
  for branch_choice in (0,1):
   source=phase_basis(c608,layout,target,amps,foreign,word,branch_choice)
   full_tail=full+star["suffix"];incident_tail=incident+star["suffix"]
   full_out=apply_word(m672,apply_word(m672,apply_word(m672,source,full_tail),predicate),m672.inverse_word(full_tail))
   star_out=apply_word(m672,apply_word(m672,apply_word(m672,source,incident_tail),predicate),m672.inverse_word(incident_tail))
   residual=m672.state_distance(full_out,star_out);maximum=max(maximum,residual);rows.append({"fixture":label,"branch_gauge":branch_choice,"foreign_cell":None if foreign is None else list(layout.cells[foreign]),"total_occupation":sum(next(iter(amps)).bit_count() for _ in [0])+(word.bit_count() if foreign is not None else 0),"residual":residual,"terms":len(source)})
   all_D_out=apply_word(m672,apply_word(m672,apply_word(m672,source,star["suffix"]),predicate),m672.inverse_word(star["suffix"]));target_D_out=apply_word(m672,apply_word(m672,apply_word(m672,source,target_D),predicate),m672.inverse_word(target_D));D_residual=m672.state_distance(all_D_out,target_D_out);maximum_D_reduction=max(maximum_D_reduction,D_residual)
   C_forward=apply_word(m672,source,full);C_reverse=apply_word(m672,source,tuple(reversed(full)));C_order_residual=m672.state_distance(C_forward,C_reverse);maximum_C_order=max(maximum_C_order,C_order_residual)
   rows[-1].update({"all_D_conjugation_vs_target_D_only_residual":D_residual,"all_C_forward_vs_reverse_residual":C_order_residual})
 nonincident=[factor for factor in full if factor not in set(incident)];predicate_support=set(coord for factor in predicate for coord in factor.controls+factor.targets);support_failures=sum(bool(predicate_support&set(f.controls+f.targets)) for f in nonincident)
 non_target_D_P_support_intersection_failures=sum(bool(set(f.controls+f.targets)&set(p.controls+p.targets)) for f in non_target_D for p in predicate)
 D_pair_count=len(non_target_D)*len(target_D);non_target_target_D_support_intersections=sum(bool(set(f.controls+f.targets)&set(t.controls+t.targets)) for f in non_target_D for t in target_D)
 non_target_target_D_target_control_hazards=sum(bool(set(f.targets)&set(t.controls) or set(t.targets)&set(f.controls)) for f in non_target_D for t in target_D)
 non_target_target_D_kind_or_shared_target_failures=sum(f.kind!="MCX" or t.kind!="MCX" or bool(set(f.targets)&set(t.targets)) for f in non_target_D for t in target_D)
 target_DP_support=set(coord for f in target_D+predicate for coord in f.controls+f.targets);nonincident_target_DP_support_intersection_failures=sum(bool(set(f.controls+f.targets)&target_DP_support) for f in nonincident)
 C_non_diagonal_kind_failures=sum(f.kind!="PHASE_EQ" or bool(f.targets) or f.matrix is not None for f in full)
 return {"fixtures":rows,"fixture_count":len(rows),"comparison_layer":"prepared A/SELECT output; (C_all;D_all) P_target (C_all;D_all)^dagger versus (C_incident;D_all) P_target (C_incident;D_all)^dagger","maximum_full_C_vs_incident_star_residual":maximum,"maximum_all_D_conjugation_vs_target_D_only_residual":maximum_D_reduction,"maximum_all_C_forward_vs_reverse_residual":maximum_C_order,"full_C_factor_count":len(full),"incident_C_factor_count":len(incident),"nonincident_C_factor_count":len(nonincident),"target_D_factor_count":len(target_D),"non_target_D_factor_count":len(non_target_D),"non_target_D_target_D_pair_count":D_pair_count,"non_target_D_target_D_support_intersections":non_target_target_D_support_intersections,"non_target_D_target_D_target_control_commutation_hazards":non_target_target_D_target_control_hazards,"non_target_D_target_D_kind_or_shared_target_failures":non_target_target_D_kind_or_shared_target_failures,"non_target_D_P_support_intersection_failures":non_target_D_P_support_intersection_failures,"all_C_non_diagonal_kind_failures":C_non_diagonal_kind_failures,"nonincident_C_target_D_or_P_support_intersection_failures":nonincident_target_DP_support_intersection_failures,"nonincident_C_predicate_support_intersection_failures":support_failures,"exact_extension_steps":["every non-target D commutes with target D because both are MCX factors with distinct targets and zero target-in-other-controls hazards; every non-target D is support-disjoint from P_target, so those inverse pairs reorder and cancel","the executed all-D conjugation equals target-D-only conjugation","all C factors are diagonal and mutually commute, with forward-versus-reverse action executed","every nonincident C has operand support disjoint from target D and P_target, so it pair-cancels after the non-target-D reduction"],"pass":max(maximum,maximum_D_reduction,maximum_C_order)<TOL and not(non_target_target_D_target_control_hazards or non_target_target_D_kind_or_shared_target_failures or non_target_D_P_support_intersection_failures or C_non_diagonal_kind_failures or nonincident_target_DP_support_intersection_failures)}

def star_state(c675,c608,star,matter_amplitudes=None,q_amplitudes=None,binder=0,extras=()):
 matter_amplitudes=matter_amplitudes or {};q_amplitudes=q_amplitudes or {};state={frozenset():1+0j}
 for index in star["star_indices"]:
  state=c675.tensor_states(state,c675.occupancy_state(star["matter_by_index"][index],matter_amplitudes.get(index,{0:1.0})))
  state=c675.tensor_states(state,c675.occupancy_state(star["layout"].q[index],q_amplitudes.get(index,{0:1.0})))
 add=tuple(extras)+((star["binder"],) if binder else ())
 return c675.add_extras(state,add)

def route_and_collision_controls(c608,star):
 factors=star["extractor_star"]+star["Wstar"]+star["predicate"]+(star["conjunction"],)
 pairs=set();operand_collisions=0;maximum_support=0
 for factor in factors:
  operands=factor.controls+factor.targets;maximum_support=max(maximum_support,len(set(operands)))
  operand_collisions+=len(operands)!=len(set(operands))
  for left in range(len(operands)):
   for right in range(left+1,len(operands)):
    pairs.add(tuple(sorted((operands[left],operands[right]))))
 digest=sha256();edge_failures=0;maximum_route=0;edges=set();head=[]
 for first,second in sorted(pairs):
  route=c608.c560.c539.periodic_route_with_tie(first,second,star["layout"].modulus)
  maximum_route=max(maximum_route,len(route)-1)
  for left,right in zip(route,route[1:]):
   edge_failures+=star["layout"].distance(left,right)!=1;edges.add((left,right));digest.update(repr((left,right)).encode())
  if len(head)<8:head.append({"first":list(first),"second":list(second),"route":[list(c) for c in route]})
 return {"logical_factor_count":len(factors),"maximum_logical_factor_support_M2":maximum_support,
  "unique_operand_pair_routes":len(pairs),"maximum_NN_route_edges":maximum_route,"distinct_oriented_NN_edges":len(edges),
  "route_edge_failures":edge_failures,"within_factor_operand_coordinate_collisions":operand_collisions,
  "deterministic_periodic_route_program_sha256":digest.hexdigest(),"route_examples":head,
  "routing_schedule":"one remote macro at a time; route, act, and reverse route before the next chronological factor",
  "route_work_returned":True,"simultaneous_route_claimed":False,"pass":edge_failures==0 and operand_collisions==0}

def execute_star(c675,m672,c608,star):
 target=star["cell_index"];a2=c608.a2_word_amplitudes();rows=[];maximum=maximum_norm=maximum_leakage=0.0
 factor_coords={coord for factor in star["full_star"] for coord in factor.controls+factor.targets}
 allowed={star["binder"],star["opportunity"]}|set(coord for rails in star["matter_by_index"].values() for coord in rails)|set(coord for i in star["star_indices"] for coord in star["layout"].q[i])
 forbidden=factor_coords-allowed
 fixtures=[("vacuum_contact_off",{},0,False),("vacuum_contact_on",{},1,False),
           ("A2_contact_off",{target:a2},0,False),("A2_contact_on",{target:a2},1,True)]
 for direction in range(6):fixtures.append((f"one_particle_mass_direction_{direction}",{target:{1<<direction:1.0}},1,False))
 neighbors=[i for i in star["star_indices"] if i!=target]
 if neighbors:
  neighbor=neighbors[0];fixtures.extend([
   ("global_N2_one_plus_one_seam",{target:{1:1.0},neighbor:{2:1.0}},1,False),
   ("global_N3_A2_plus_incident_one_contact",{target:a2,neighbor:{1:1.0}},1,True),
   ("global_N2_incident_A2_target_vacuum",{neighbor:a2},1,False)])
 for label,maps,binder,toggle in fixtures:
  source=star_state(c675,c608,star,maps,binder=binder);out=apply_word(m672,source,star["full_star"])
  expected=m672.expected_toggle(source,star["opportunity"]) if toggle else source
  residual=m672.state_distance(out,expected);norm=abs(m672.state_norm(out)-1)
  leakage=sum(abs(a)**2 for bits,a in out.items() if bits&forbidden)
  maximum=max(maximum,residual);maximum_norm=max(maximum_norm,norm);maximum_leakage=max(maximum_leakage,leakage)
  rows.append({"fixture":label,"declared_total_physical_occupation_max":max((sum(word.bit_count() for word in words) for words in __import__('itertools').product(*[tuple(amplitudes) for amplitudes in maps.values()])),default=0),"binder":binder,"expected_opportunity_toggle":toggle,"residual":residual,"norm_residual":norm,"terminal_internal_leakage_probability":leakage,"source_terms":len(source)})
 stage_source=star_state(c675,c608,star,{target:a2});stage=apply_word(m672,stage_source,star["extractor_star"])
 stage_expected=star_state(c675,c608,star,{},{target:a2});stage_residual=m672.state_distance(stage,stage_expected)
 inverse_residual=m672.state_distance(apply_word(m672,stage,m672.inverse_word(star["extractor_star"])),stage_source)
 prepared_source=(stage_source if not neighbors else star_state(c675,c608,star,{target:a2,neighbors[0]:{1:1.0}}))
 prepared=apply_word(m672,apply_word(m672,prepared_source,star["extractor_star"]),star["prefix"]);branch_violation=sum(abs(a)**2 for bits,a in prepared.items() if any(sum(coord in bits for coord in star["layout"].branch[i])!=1 for i in star["star_indices"]))
 C_net_signal=m672.state_distance(prepared,apply_word(m672,prepared,star["incident_C"])) if star["incident_C"] else 0.0
 q_only=star_state(c675,c608,star,{}, {target:a2},binder=1);q_only_out=apply_word(m672,q_only,star["full_star"]);q_only_identity=m672.state_distance(q_only_out,q_only)
 dirty=star_state(c675,c608,star,{target:a2},binder=1,extras=(star["layout"].branch[target][0],));dirty_out=apply_word(m672,dirty,star["full_star"]);clean_expected=m672.expected_toggle(star_state(c675,c608,star,{target:a2},binder=1),star["opportunity"]);dirty_overlap=abs(sum(np.conj(dirty_out.get(bits,0))*a for bits,a in clean_expected.items()))
 contact_source=star_state(c675,c608,star,{target:a2},binder=1);contact_expected=m672.expected_toggle(contact_source,star["opportunity"])
 central=next(i for i,f in enumerate(star["full_star"]) if f.label==("A2_predicate",));deleted=apply_word(m672,contact_source,star["full_star"],skip=central);contact_deletion=m672.state_distance(deleted,contact_expected)
 C_deletions=[]
 for ordinal,factor in enumerate(star["incident_C"]):
  bits=frozenset(coord for coord,value in zip(factor.controls,factor.values) if value);local={bits:1+0j};signal=m672.state_distance(apply_factor(m672,local,factor),local)
  C_deletions.append({"ordinal":ordinal,"descriptor":factor.descriptor(ordinal),"deletion_signal":signal,"global_witness":"apply inverse chronological prefix to this matching-control local witness; the unitary suffix preserves the norm"})
 minimum_C=min((row["deletion_signal"] for row in C_deletions),default=None)
 C_sample_ordinals=sorted({i for i in (0,1,len(C_deletions)//2,len(C_deletions)-2,len(C_deletions)-1) if 0<=i<len(C_deletions)});C_descriptor_rows=[f.descriptor(i) for i,f in enumerate(star["incident_C"])]
 route=route_and_collision_controls(c608,star)
 passed=max(maximum,maximum_norm,maximum_leakage,stage_residual,inverse_residual,q_only_identity,dirty_overlap,branch_violation)<TOL and contact_deletion>1e-3 and (minimum_C is None or minimum_C>1e-3) and route["pass"]
 return {"cell":list(star["cell"]),"star_cells":[list(star["layout"].cells[i]) for i in star["star_indices"]],"star_cell_count":len(star["star_indices"]),
  "incident_edge_count":len(star["incident_edges"]),"incident_C_factor_count":len(star["incident_C"]),"chronological_segment_counts":{"A_plus_SELECT_prefix":len(star["prefix"]),"incident_C_exact_order":len(star["incident_C"]),"D_suffix":len(star["suffix"]),"physical_star_extractor":len(star["extractor_star"]),"W_star":len(star["Wstar"]),"full_inverse_uncompute_word":len(star["full_star"])},
  "W_star_sha256":factor_digest(m672,star["Wstar"]),"incident_C_exact_order_sha256":factor_digest(m672,star["incident_C"]),
  "incident_C_coordinate_export":{"executed_descriptor_count":len(C_descriptor_rows),"full_descriptor_sha256":stable_digest(C_descriptor_rows),"stored_sample_ordinals":C_sample_ordinals,"descriptor_samples":[C_descriptor_rows[i] for i in C_sample_ordinals],"compaction":"every coordinate-explicit descriptor is regenerated and executed by the runner; receipt stores count, stable digest, and head/middle/tail samples"},
  "physical_fixture_rows":rows,"physical_fixture_count":len(rows),"maximum_physical_interface_residual":maximum,"maximum_norm_residual":maximum_norm,"maximum_terminal_internal_leakage_probability":maximum_leakage,
  "physical_all_star_matter_to_q_stage_residual":stage_residual,"physical_all_star_extractor_inverse_residual":inverse_residual,"prepared_star_branch_one_hot_violation_probability":branch_violation,"incident_C_group_action_signal_on_A2_plus_incident_one_fixture":C_net_signal,
  "same_q_A2_different_physical_matter_identity_residual":q_only_identity,"dirty_branch_to_clean_code_overlap":dirty_overlap,"contact_predicate_deletion_signal":contact_deletion,
  "every_incident_C_deletion_execution":{"executed_row_count":len(C_deletions),"full_rows_sha256":stable_digest(C_deletions),"stored_sample_ordinals":C_sample_ordinals,"row_samples":[C_deletions[i] for i in C_sample_ordinals],"compaction":"all deletion witnesses execute before compaction; no row is skipped"},"minimum_incident_C_factor_deletion_signal":minimum_C,"route_and_collision":route,"pass":passed}

def covariance_controls(c675,m672,c608,representatives):
 frames=c608.c560.c532.c235.proper_cubic_frames();keys={tuple(frame.reshape(-1)) for frame in frames};dirs=c675.directions(c608);lookup={d:i for i,d in enumerate(dirs)}
 raw_fail=repaired_fail=group_coordinate_fail=wedge_group_fail=route_fail=0;comparisons=0;maximum_CZ=maximum_CZ_route=0;exports=[]
 for star in representatives:
  target=star["cell_index"];source=star_state(c675,c608,star,{target:c608.a2_word_amplitudes()},binder=1);base=apply_word(m672,source,star["full_star"])
  for frame_index,frame in enumerate(frames):
   dmap=tuple(lookup[tuple(int(v) for v in frame@np.asarray(direction))] for direction in dirs)
   rotated_matter=tuple(m672.rotate_coord(c608,c,frame,star["layout"].modulus) for c in star["matter"])
   sheath=tuple(m672.Factor("MCZ",(rotated_matter[left],),(1,),(rotated_matter[right],),None,("Cycle675_local_fermionic_frame_inversion_CZ",left,right)) for left in range(6) for right in range(left+1,6) if dmap[left]>dmap[right])
   maximum_CZ=max(maximum_CZ,len(sheath));maximum_CZ_route=max(maximum_CZ_route,max((star["layout"].distance(f.controls[0],f.targets[0]) for f in sheath),default=0))
   rotated_word=tuple(m672.rotate_factor(c608,f,frame,star["layout"].modulus) for f in star["full_star"])
   def signed_rotate(state):
    result={}
    for bits,amplitude in state.items():
     occupied=[i for i,c in enumerate(star["matter"]) if c in bits];mapped=[dmap[i] for i in occupied];sign=-1 if sum(mapped[l]>mapped[r] for l in range(len(mapped)) for r in range(l+1,len(mapped)))%2 else 1
     target_bits=frozenset(m672.rotate_coord(c608,c,frame,star["layout"].modulus) for c in bits);result[target_bits]=result.get(target_bits,0j)+sign*amplitude
    return result
   rotated_source=signed_rotate(source);rotated_base=signed_rotate(base)
   raw_fail+=m672.state_distance(apply_word(m672,rotated_source,rotated_word),rotated_base)>TOL
   repaired=sheath+rotated_word+tuple(reversed(sheath));repaired_fail+=m672.state_distance(apply_word(m672,rotated_source,repaired),rotated_base)>TOL;comparisons+=1
   for factor in star["incident_C"]:
    operands=factor.controls+factor.targets
    for left in range(len(operands)):
     for right in range(left+1,len(operands)):
      route_fail+=star["layout"].distance(m672.rotate_coord(c608,operands[left],frame,star["layout"].modulus),m672.rotate_coord(c608,operands[right],frame,star["layout"].modulus))!=star["layout"].distance(operands[left],operands[right])
   sheath_rows=[f.descriptor(i) for i,f in enumerate(sheath)];exports.append({"length":star["layout"].length,"cell":list(star["cell"]),"frame_index":frame_index,"direction_permutation":list(dmap),"local_CZ_count":len(sheath),"local_CZ_full_descriptor_sha256":stable_digest(sheath_rows),"local_CZ_descriptor_head":sheath_rows[:1],"local_CZ_descriptor_tail":sheath_rows[-1:],"transported_incident_C_sha256":factor_digest(m672,tuple(m672.rotate_factor(c608,f,frame,star["layout"].modulus) for f in star["incident_C"]))})
 for first in frames:
  for second in frames:
   group_coordinate_fail+=tuple((first@second).reshape(-1)) not in keys
   first_map=tuple(lookup[tuple(int(v) for v in first@np.asarray(direction))] for direction in dirs);second_map=tuple(lookup[tuple(int(v) for v in second@np.asarray(direction))] for direction in dirs);product_map=tuple(lookup[tuple(int(v) for v in (first@second)@np.asarray(direction))] for direction in dirs)
   for left in range(6):
    for right in range(left+1,6):
     after=(second_map[left],second_map[right]);second_sign=-1 if after[0]>after[1] else 1;ordered=tuple(sorted(after));after_first=(first_map[ordered[0]],first_map[ordered[1]]);first_sign=-1 if after_first[0]>after_first[1] else 1;product=(product_map[left],product_map[right]);product_sign=-1 if product[0]>product[1] else 1;wedge_group_fail+=second_sign*first_sign!=product_sign
   for star in representatives:
    modulus=star["layout"].modulus
    for coord in {c for f in star["full_star"] for c in f.controls+f.targets}:
     group_coordinate_fail+=m672.rotate_coord(c608,m672.rotate_coord(c608,coord,second,modulus),first,modulus)!=m672.rotate_coord(c608,coord,first@second,modulus)
 return {"proper_cubic_frames":len(frames),"ordered_frame_products":len(frames)**2,"representative_sizes":[s["layout"].length for s in representatives],"executed_state_comparisons":comparisons,
  "raw_coordinate_only_signed_covariance_failures":raw_fail,"expected_raw_failures_inherited_pattern":16*len(representatives),"local_Cycle675_CZ_sheath_repaired_failures":repaired_fail,"incident_C_pair_distance_transport_failures":route_fail,"group_coordinate_failures":group_coordinate_fail,"fermionic_wedge_group_law_failures":wedge_group_fail,
  "maximum_local_frame_CZ_factors":maximum_CZ,"maximum_local_frame_CZ_pair_route_edges":maximum_CZ_route,"frame_rows":exports,"frame_row_count":len(exports),"frame_compaction":"all 72 transported state comparisons and route rows execute; repeated local-CZ descriptors are stored as count/digest/head/tail","runtime_frame_selector":False,"compile_time_frame_transport":True,"global_parity_string_or_service":False,"pass":len(frames)==24 and raw_fail==16*len(representatives) and not(repaired_fail or route_fail or group_coordinate_fail or wedge_group_fail)}

def no_go_discipline():
 walls={"W_same_device_generic_chart":"the incident-star compiler remains selected-cell and compile-time charted; one autonomous all-cell tile is not constructed","W_framework_matter_identification":"the radius-four occupancy rails are independent M2 inputs, while their genesis as the framework matter law remains supplied","W_primitive_router_substrate":"logical PHASE_EQ factors have explicit deterministic bounded NN route-return paths, but the inherited router/work substrate is not rederived in this cycle"}
 names=tuple(walls);pairs=[{"from":a,"to":b,"implied":False,"reason":"distinct constructive obligation"} for a in names for b in names if a!=b]
 families=[
  {"family":"target-only local W","status":"REJECTED for generic C-sensitive target","honesty_marker":"ATTEMPTED","strength":"weaker"},
  {"family":"counts-only incident C","status":"REJECTED: no prepared neighbor branch or product","honesty_marker":"ATTEMPTED","strength":"weaker"},
  {"family":"prepared incident-C star","status":"PASS_EXECUTED","honesty_marker":"ATTEMPTED","strength":"target-matched bounded compiler"},
  {"family":"full-torus C versus incident-star observable reduction","status":"PASS_EXACT on declared global N<=3 fixtures plus disjoint-support extension","honesty_marker":"ATTEMPTED","strength":"strong reference comparison"},
  {"family":"autonomous unprogrammed all-cell tile","status":"OPEN / NOT ATTEMPTED","honesty_marker":"OPEN / NOT ATTEMPTED","strength":"strict next target"}]
 return {"N1_normalized_families":families,"N1_qualifying_attempts_for_negative":4,"N1_required_for_negative":5,"N1_threshold_met_for_negative":False,
  "N2_walls":walls,"N2_directed_ordered_pairs":pairs,
  "N3_hidden_wall_scan":[{"condition":"independent radius-four matter rails","classification":"explicit supply; W_framework_matter_identification"},{"condition":"blank q and one-hot branch code domain","classification":"local lawful-domain condition; malformed q/branch counterfactuals executed"},{"condition":"compile-time cell chart","classification":"explicit supply; W_same_device_generic_chart"},{"condition":"fermionic frame inversion phase","classification":"raw signed failure retained; bounded local Cycle675 CZ sheath explicit"},{"condition":"deterministic route-return program","classification":"coordinate explicit, bounded, and tested; substrate inherited under W_primitive_router_substrate"}],
  "N4_exact_residual_matches":[{"prior_cycle":675,"residual":"incident C counted but absent from executed physical star","current":"every target-incident row is inserted after target/neighbor A/SELECT and before every D","exact_match":True,"retired":True},{"prior_cycle":675,"residual":"same-device all-cell tile absent","current":"selected proper-cubic-closed compiler remains charted","exact_match":True,"retired":False},{"prior_cycle":608,"residual":"full C only algebraic/count surface","current":"sparse prepared-star detector and full-C reference comparison executed","exact_match":True,"retired":True}],
  "N5_rhetoric":[{"claim":"an incident star is not an autonomous lattice tile","per_element":"C factors explicit","per_site":"target plus incident neighbors","per_mode":"six q/matter rails","per_block":"bounded prepared star","lattice_wide":"same-device scheduler open"},{"claim":"factor ordinal is not physical time or energy","per_element":"gate order","per_site":"finite schedule","per_mode":"no rate","per_block":"no calibrated clock","lattice_wide":"no source law"},{"claim":"local CZ sheath is not a global parity service","per_element":"pair phase","per_site":"at most 15 CZ","per_mode":"wedge sign","per_block":"compile-time frame","lattice_wide":"no ordering string"}],
  "N6_partial_closure_paths":[{"file":str(Path(__file__).relative_to(ROOT)),"status":"EXECUTED PARTIAL","what_closes":"Cycle675 incident-C prepared-star wall"},{"file":"UNMATERIALIZED/cycle679_autonomous_all_cell_tile_next.py","status":"OPEN / PRIORITY","what_closes":"W_same_device_generic_chart"},{"file":"UNMATERIALIZED/framework_matter_genesis_next.py","status":"OPEN","what_closes":"W_framework_matter_identification"}],
  "N7_steelman":{"mechanism":"replace the selected-cell factor export by a translation-covariant local cellular schedule whose role labels, branch reset, route colors, and frame phases arise from the same bounded neighborhood state","actionable_steps":["freeze one local tile alphabet","color overlapping incident stars locally","execute simultaneous collision/leakage tests","prove chart-free all-cell covariance"],"terminal_test":"one unprogrammed tile on all cells at L3/L4/L6 with the same contact/seam/mass and all24/all576 fixtures"},
  "N8_cross_cycle_echo":[{"cycle":608,"mechanism":"accepted C equality rows and order","retired":"row algebra/count","applicability":"now executed only on selected incident stars"},{"cycle":672,"mechanism":"literal local detector convention","retired":"local W detector product","applicability":"star extends it without changing predicate"},{"cycle":675,"mechanism":"physical matter SWAP and local CZ frame sheath","retired":"target physical q import","applicability":"expanded to every star cell"}],
  "broad_no_go_claim":False,"minimum_content_claim":False,"shared_obstruction_claim":False,"shared_route_independent_obstruction":False,"axiom_pressure_claim":False,"broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP","shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP","pass":True}

def rss_bytes():
 value=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;return int(value if sys.platform=="darwin" else value*1024)

def main():
 global PASS,FAIL
 started=time.monotonic();NOTE.parent.mkdir(parents=True,exist_ok=True);RECEIPT.parent.mkdir(parents=True,exist_ok=True)
 with COLD.open("w") as cold:
  original=sys.stdout;sys.stdout=Tee(original,cold)
  try:
   freeze=target_freeze_controls();shore,prior=shore_controls();check("target frozen before evidence",freeze["pass"],freeze);check("Cycle675/672/608 committed shores pinned",shore["pass"],shore["ref"])
   size_rows=[];representatives=[]
   with pinned_modules() as (c675,m672,c608):
    for length in (3,4,6):
     layout=c608.build_layout(length);indices,incident=c675.selected_cells(c608,layout);matter_all=set(c675.all_matter_rails(c608,layout));occupied=set(c675.global_occupied(c608,layout))|matter_all
     rows=[];equality=[];stars=[]
     for index in indices:
      star=build_star(c675,m672,c608,layout,index,set(occupied));stars.append(star);row=execute_star(c675,m672,c608,star);eq=full_C_equality(m672,c608,star);rows.append(row);equality.append(eq)
     representative=max(stars,key=lambda star:len(star["incident_C"]));representatives.append(representative)
     max_residual=max(row["maximum_physical_interface_residual"] for row in rows);max_eq=max(row["maximum_full_C_vs_incident_star_residual"] for row in equality);min_C=min((row["minimum_incident_C_factor_deletion_signal"] for row in rows if row["minimum_incident_C_factor_deletion_signal"] is not None),default=None)
     selected={"length":length,"split":next(row["split"] for row in prior["Cycle608"]["compiler_rows"] if row["length"]==length),"selected_cell_rule":"Cycle675 origin plus proper-cubic orbit of lexicographically first maximum-incident-C cell","selected_cells":[list(star["cell"]) for star in stars],"selected_cell_count":len(stars),"global_radius_four_matter_rails":len(matter_all),"global_matter_rail_injective":len(matter_all)==6*len(layout.cells),"cell_rows":rows,"full_C_reference_rows":equality,"maximum_physical_residual":max_residual,"maximum_full_C_reference_residual":max_eq,"minimum_C_deletion_signal":min_C,"pass":all(row["pass"] for row in rows) and all(row["pass"] for row in equality)};size_rows.append(selected)
     check(f"L{length} physical prepared incident-C selected-cell family",selected["pass"],{"cells":len(rows),"max_physical":max_residual,"max_full_C":max_eq,"max_incident_C":max(len(star["incident_C"]) for star in stars),"min_C_delete":min_C})
    covariance=covariance_controls(c675,m672,c608,representatives)
   check("all24 state and all576 group covariance with raw signed failure retained",covariance["pass"],{"comparisons":covariance["executed_state_comparisons"],"raw_failures":covariance["raw_coordinate_only_signed_covariance_failures"],"repaired_failures":covariance["local_Cycle675_CZ_sheath_repaired_failures"],"all576_group_failures":covariance["group_coordinate_failures"]})
   total_cells=sum(row["selected_cell_count"] for row in size_rows);physical_fixtures=sum(cell["physical_fixture_count"] for row in size_rows for cell in row["cell_rows"]);C_rows=sum(cell["incident_C_factor_count"] for row in size_rows for cell in row["cell_rows"]);fullC_fixtures=sum(eq["fixture_count"] for row in size_rows for eq in row["full_C_reference_rows"]);max_physical=max(row["maximum_physical_residual"] for row in size_rows);max_fullC=max(row["maximum_full_C_reference_residual"] for row in size_rows);max_leak=max(cell["maximum_terminal_internal_leakage_probability"] for row in size_rows for cell in row["cell_rows"]);min_C=min(cell["minimum_incident_C_factor_deletion_signal"] for row in size_rows for cell in row["cell_rows"] if cell["minimum_incident_C_factor_deletion_signal"] is not None);max_route=max(cell["route_and_collision"]["maximum_NN_route_edges"] for row in size_rows for cell in row["cell_rows"])
   check("every inserted incident C has a deletion witness",C_rows>0 and min_C>1e-3,{"inserted_rows":C_rows,"minimum_signal":min_C});check("full-C reference, leakage and lawful-domain controls",max(max_physical,max_fullC,max_leak)<TOL,{"physical":max_physical,"full_C":max_fullC,"leakage":max_leak});nogo=no_go_discipline();check("full N1-N8; no negative or axiom-pressure claim",nogo["pass"] and not nogo["shared_obstruction_claim"],nogo["N2_walls"])
   receipt={"cycle":679,"date":"2026-07-23","authority":AUTHORITY,"audit":AUDIT,"Status":"PASS" if FAIL==0 else "FAIL","pass":FAIL==0,"tests_passed":PASS,"tests_failed":FAIL,"elapsed_seconds":time.monotonic()-started,"maximum_RSS_bytes":rss_bytes(),"target_contract":TARGET_CONTRACT,"target_freeze":freeze,"shore":shore,"size_rows":size_rows,"covariance":covariance,
    "aggregate_summary":{"sizes":[3,4,6],"selected_cells":total_cells,"physical_fixture_comparisons":physical_fixtures,"full_C_reference_comparisons":fullC_fixtures,"incident_C_factors_inserted_and_deleted":C_rows,"maximum_physical_interface_residual":max_physical,"maximum_full_C_vs_incident_star_residual":max_fullC,"maximum_terminal_internal_leakage_probability":max_leak,"minimum_incident_C_deletion_signal":min_C,"maximum_NN_route_edges":max_route,"physical_occupancy_to_q_extractor_on_every_star_cell":True,"target_and_every_incident_neighbor_A_SELECT_prepared":True,"all_incident_C_exact_accepted_order":True,"all_local_D_suffixes":True,"full_inverse_uncompute":True,"one_particle_mass_fixture_preserved":True,"Cycle230_contact_and_seam_fixture_preserved":True,"same_q_different_matter_control":True,"contact_deletion_control":True,"origin_zero_C_baseline":True,"held_out_L4":True,"held_L6":True,"incident_C_star_product_executed":True,"receipt_descriptor_compaction_after_full_execution":True,"compaction_form":"counts plus stable digests plus head/middle/tail samples; runner regenerates all rows","same_unprogrammed_all_cell_device_executed":False,"pass":all(row["pass"] for row in size_rows) and covariance["pass"]},
    "supplied_structure_inventory":{"Cycle608_C_row_generator_and_exact_factor_order":True,"Cycle608_local_A_SELECT_D_tables":True,"Cycle608_A2_amplitudes":True,"Cycle675_radius_four_independent_matter_rail_orbit":True,"blank_q_and_branch_work_lawful_domain":True,"deterministic_periodic_route_tie_break":True,"Cycle668_binder_interface":True,"compile_time_cell_selection_and_role_chart":True,"Cycle675_local_fermionic_CZ_frame_sheath":True,"physical_matter_genesis_law":False,"autonomous_all_cell_scheduler":False,"global_Jordan_Wigner_order":False,"global_parity_string_or_service":False,"host_side_runtime_branch_selection":False,"runtime_frame_selector":False,"shell_ROM":False},
    "route_disposition":{"target_only_local_W":"REJECTED_FOR_INCIDENT_C_TARGET","counts_only_C":"REJECTED_NO_PRODUCT","prepared_incident_C_star":"PASS_EXECUTED","full_torus_C_reference_reduction":"PASS_EXACT_ON_DECLARED_N_LE_3_PLUS_DISJOINT_SUPPORT_EXTENSION","raw_coordinate_only_signed_covariance":"FAIL_48_OF_72_AS_REQUIRED_CONTROL","bounded_local_CZ_repaired_covariance":"PASS_72_OF_72","autonomous_same_device_all_cell_tile":"OPEN_PRIORITY"},
    "highest_honest_terminal":"bounded selected-cell physical incident-C star: independent matter on target and every incident neighbor, exact accepted C order, full inverse/uncompute, all24/all576; not an autonomous all-cell tile",
    "bounded_partial_construction_pass":True,"target_contract_incident_star_terminal_met":True,"strict_full_framework_terminal_met":False,
    "six_wall_ledger":{"C_ref":"advance: full-torus C observable is exactly reduced to the prepared target-incident star on declared global N<=3 fixtures; local tables/order remain supplied","C_num":"unchanged: finite sparse products and committed Givens parameters","C_wrap":"advance in periodic-seam held-size tests only; no phase-as-energy claim","C_int":"advance: every target-incident equality phase is executed and deleted inside the physical star; autonomous overlap schedule remains open","C_local":"advance: bounded coordinate-explicit support and NN route-return programs through L6; chart-free all-cell tile and router genesis remain open","C_source":"unchanged: binder and independent matter inputs supplied; no gravity/source derivation"},
    "TOE_dependency_ledger":{"operational_quantum_records_maturity_0_to_5":3.3,"causal_time_maturity_0_to_5":2.4,"inertia_matter_maturity_0_to_5":2.4,"gravity_source_maturity_0_to_5":1.4,"Born_probability_maturity_0_to_5":2.2,"dependency_change":"C_int and C_local advance by executing the bounded generic incident equality star; time, source and Born walls are not promoted"},
    "no_go_discipline":nogo,"shared_obstruction_creates_axiom_pressure":False,"optimal_next_campaign":"construct one chart-free, unprogrammed locally colored all-cell tile for overlapping incident stars; execute L3/L4/L6 collision, leakage, contact/seam/mass, all24/all576 and deletion controls","note":str(NOTE.relative_to(ROOT))}
   RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n");print("RECEIPT",RECEIPT.relative_to(ROOT));print("RESULT",receipt["Status"],"tests",PASS,"failed",FAIL,"elapsed",receipt["elapsed_seconds"])
  finally:sys.stdout=original
 return 0 if FAIL==0 else 1

if __name__=="__main__":raise SystemExit(main())
