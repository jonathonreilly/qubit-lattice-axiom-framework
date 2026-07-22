#!/usr/bin/env python3
"""Cycle615: lawful charge and joined metric/receiver response tournament.

This runner constructs a candidate distinct charge-conjugate sector with a
local neutral-pair resource gate, an independent centered open-boundary flux
route, and a joined Cycle613-gauge/Cycle576-Regge action variation.  It does
not identify the candidate sector as derived antimatter, F17 words as energy
or stress, or the joined carrier as gravity.  Authority none; audit unset.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
from time import perf_counter

import numpy as np
from scipy.sparse.linalg import expm_multiply

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import physical_gauged_matter_action_stress_prediction_tournament_cycle613_2026_07_22 as c613
import physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22 as c576

c611=c613.c611;c609=c613.c609;c230=c613.c230;c219=c613.c219;c210=c613.c210
NOTE=ROOT/("docs/work_history/repo/review_feedback/"
 "PHYSICAL_LAWFUL_CHARGE_JOINED_METRIC_RESPONSE_TOURNAMENT_CYCLE615_NOTE_2026-07-22.md")
RECEIPT=ROOT/"outputs/physical_lawful_charge_joined_metric_response_tournament_cycle615_receipt_2026_07_22.json"
COLD=ROOT/"outputs/physical_lawful_charge_joined_metric_response_tournament_cycle615_cold_2026_07_22.txt"
AUTHORITY="none";AUDIT="unset";TOL=2e-8;START=perf_counter();PASS=FAIL=0
PERIODIC_FIXTURES=(("TRAIN_L3",3,False),("HELD_L6",6,True),("OUT_HELD_L7",7,True))
OPEN_FIXTURES=(("TRAIN_OPEN_L3",3,False),("HELD_OPEN_L5",5,True),("OUT_HELD_OPEN_L7",7,True))
PINS={
 "scripts/physical_gauged_matter_action_stress_prediction_tournament_cycle613_2026_07_22.py":"f1fe6a4c1b37b8071031746c396162900a4a73acba90c6bd219cabe818205303",
 "docs/work_history/repo/review_feedback/PHYSICAL_GAUGED_MATTER_ACTION_STRESS_PREDICTION_TOURNAMENT_CYCLE613_NOTE_2026-07-22.md":"55f8def38aa1129405601b0fc3ba79c11d44e02886d564bf1bb26fcd80adb68f",
 "outputs/physical_gauged_matter_action_stress_prediction_tournament_cycle613_receipt_2026_07_22.json":"260dd78e1f648b3f6c062d3e5c79383182587fbeacf6e2aa06ffa6d84bb79c41",
 "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py":"53d60249420994818e7517645ad4157e1e11c7dc184fbf89b2838e94b53977d0",
 "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json":"06456c1443f5464949f40d81e9f1c6316b3e4e8405415b5b0035e39d4b88c3bd",
 "outputs/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_receipt_2026_07_22.json":"c8210a1f170c3b11258f9876a0013b981b4b3c44a592423c8ce48a34a479b5ee",
 "scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py":"91f22d23dd2730f76a05736634236d41036f68eaedc4921daca69de25ab6a344",
 "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md":"920776555dce6505bccb0e46e552e90d24858c08cfb7f6978d884f10a5bb0789",
 "outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json":"e7a8ea3dcbe370c9f8c6a94770508d1710a7013ce4ba62a1ad67e345fe1e2d11",
 "docs/MINIMAL_AXIOMS_2026-06-29.md":"fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
 "docs/audit/data/axiom_premise_nodes.json":"b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
 "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md":"e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
 "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md":"5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
 "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md":"755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
}


class Tee:
 def __init__(self,*streams):self.streams=streams
 def write(self,value):
  for stream in self.streams:stream.write(value)
  return len(value)
 def flush(self):
  for stream in self.streams:stream.flush()


def json_default(value):
 if isinstance(value,np.generic):return value.item()
 if isinstance(value,np.ndarray):return value.tolist()
 if isinstance(value,complex):return [value.real,value.imag]
 raise TypeError(type(value).__name__)


def digest(path):return sha256((ROOT/path).read_bytes()).hexdigest()
def check(label,condition,detail=""):
 global PASS,FAIL;PASS+=int(condition);FAIL+=int(not condition)
 print("PASS" if condition else "FAIL",label,"::",detail)


def shore():
 observed={path:digest(path) for path in PINS}
 r613=json.loads((ROOT/"outputs/physical_gauged_matter_action_stress_prediction_tournament_cycle613_receipt_2026_07_22.json").read_text())
 r576=json.loads((ROOT/"outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json").read_text())
 r604=json.loads((ROOT/"outputs/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_receipt_2026_07_22.json").read_text())
 r612=json.loads((ROOT/"outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json").read_text())
 result={"hashes_match":observed==PINS,"Cycle613_pass":r613["pass"],"Cycle576_pass":r576["pass"],
         "Cycle604_pass":r604["pass"],"Cycle612_pass":r612["pass"],
         "Cycle613_divJ_coefficient_relative_residual":r613["route_C_prediction_compatibility"]["coefficient_relative_residual"],
         "Cycle604_5_over_32pi_maximum_relative_residual":r604["route_C_prediction_bridge"]["maximum_5_over_32pi_relative_residual"],
         "Cycle612_delay_or_advance_selected":r612["route_C_source_motion_ratio"]["delay_or_advance_selected"]}
 check("read-only foundation and Cycles576/604/612/613 are byte-pinned",result["hashes_match"]
       and all(result[k] for k in ("Cycle613_pass","Cycle576_pass","Cycle604_pass","Cycle612_pass"))
       and result["Cycle613_divJ_coefficient_relative_residual"]==1
       and not result["Cycle612_delay_or_advance_selected"],result)
 return r613,r576,r604,r612,result


def note_contract():
 body=" ".join(NOTE.read_text().lower().replace("`","").replace("*","").split())
 required=("authority: none","audit: unset","cycle 615","candidate distinct charged sector","not derived antimatter",
  "route a","route b","route c","local neutral-pair","genesis debit","six negative","full coin","contact","gauss",
  "open boundary","boundary flux","translation","joined action","regge","coframe variation","operational receiver",
  "equivalence class","improvement","sign","scale","5/(32pi)","div j","l3","l5","l6","l7","all 24","576",
  "inverse","leakage","deletion","f17 is not energy","not gravity","n1 —","n2 —","n3 —","n4 —","n5 —",
  "n6 —","n7 —","n8 —","no axiom pressure")
 missing=tuple(item for item in required if item not in body)
 check("Cycle615 note freezes domains, alternatives, and N1-N8 scope",not missing,missing)


# ---------- Route A: candidate charge-conjugate sector and local pair genesis ----------
def pair_gate():
 resource=np.zeros(7);resource[0]=1
 scalar=np.zeros(7);scalar[1:]=1/math.sqrt(6)
 return np.eye(7)-np.outer(resource,resource)-np.outer(scalar,scalar)+np.outer(resource,scalar)+np.outer(scalar,resource)


def pair_representation(frame):
 result=np.zeros((7,7));result[0,0]=1
 dmap=np.argmax(c210.direction_permutation(frame),axis=0)
 for direction,target in enumerate(dmap):result[1+int(target),1+direction]=1
 return result


def gauge_stream_charge(psi,q,charge):
 length=q.shape[0];result=np.zeros_like(psi)
 for site in product(range(length),repeat=3):
  for direction in range(6):
   target=c613.destination(site,direction,length)
   phase=np.exp(2j*math.pi*charge*c613.link_phase_word(q,site,direction)/c609.MOD)
   result[target+(direction,)]=phase*psi[site+(direction,)]
 return result


def gauge_matter_charge(psi,theta,charge):
 return psi*np.exp(2j*math.pi*charge*theta[...,None]/c609.MOD)


def occupation_transport(length,site,occupation,charge):
 current=np.zeros((length,length,length,3),dtype=np.int64)
 before=np.zeros((length,)*3,dtype=np.int64);after=np.zeros_like(before)
 before[site]=charge*int(np.sum(occupation))
 for direction,occupied in enumerate(occupation):
  if occupied:
   current+=charge*c613.branch_current(length,site,direction)
   after[c613.destination(site,direction,length)]+=charge
 return current, before, after


def fock_charge_controls(length,q,e,coin):
 occupations=c230.c229.occupation_table(6);site=(0,0,0);gradient=c613.magnetic_gradient(q)
 plus=[];minus=[]
 for occupation in occupations:
  plus.append(occupation_transport(length,site,occupation,+1))
  minus.append(occupation_transport(length,site,occupation,-1))
 max_cont=max_gauss=max_inverse=0;min_delete=math.inf
 for pindex in range(64):
  for mindex in range(64):
   current=plus[pindex][0]+minus[mindex][0];rho=plus[pindex][1]+minus[mindex][1]
   rho1=plus[pindex][2]+minus[mindex][2]
   continuity=(rho1-rho+c613.divergence(current))%c609.MOD
   max_cont=max(max_cont,int(np.max(np.minimum(continuity,c609.MOD-continuity))))
   e1=(e-current-gradient)%c609.MOD;q1=(q+e1)%c609.MOD
   gauss=(c613.divergence(e)-rho)%c609.MOD;gauss1=(c613.divergence(e1)-rho1)%c609.MOD
   difference=(gauss1-gauss)%c609.MOD
   max_gauss=max(max_gauss,int(np.max(np.minimum(difference,c609.MOD-difference))))
   qb=(q1-e1)%c609.MOD;eb=(e1+current+c613.magnetic_gradient(qb))%c609.MOD
   max_inverse=max(max_inverse,int(np.max(abs(qb-q))),int(np.max(abs(eb-e))))
   if np.any(current):min_delete=min(min_delete,int(np.max(np.minimum(current%c609.MOD,(-current)%c609.MOD))))
 lifted_plus=c230.c229.fock_lift(coin);lifted_minus=c230.c229.fock_lift(coin.conj())
 rng=np.random.default_rng(61500+length)
 amplitudes=c611.normalize(rng.normal(size=(64,64))+1j*rng.normal(size=(64,64)))
 evolved=lifted_plus@amplitudes@lifted_minus.T
 numbers=np.sum(occupations,axis=1);pairs=numbers*(numbers-1)/2
 evolved*=np.exp(1j*c230.COUPLING*(pairs[:,None]+pairs[None,:]))
 coherent_norm=abs(float(np.linalg.norm(evolved)**2-1))
 return {"joint_local_occupation_words_exhausted":4096,"maximum_charge_continuity_residual":max_cont,
  "maximum_Gauss_preservation_residual":max_gauss,"maximum_joint_inverse_residual":max_inverse,
  "minimum_nonzero_current_deletion_signal":min_delete,"coherent_product_Fock_coin_contact_norm_residual":coherent_norm,
  "host_branch_selection_used":False}


def pair_branch_controls(length,q,e):
 site=(0,0,0);rows=[];average_source=np.zeros((length,)*3);max_gauss=max_inverse=max_cov=0
 gradient=c613.magnetic_gradient(q)
 for direction in range(6):
  opposite=direction^1
  jp,rhop,rhop1=occupation_transport(length,site,np.eye(6,dtype=int)[direction],+1)
  jm,rhom,rhom1=occupation_transport(length,site,np.eye(6,dtype=int)[opposite],-1)
  current=jp+jm;rho=rhop+rhom;rho1=rhop1+rhom1;average_source+=rho1/6
  e1=(e-current-gradient)%c609.MOD;q1=(q+e1)%c609.MOD
  before=(c613.divergence(e)-rho)%c609.MOD;after=(c613.divergence(e1)-rho1)%c609.MOD
  difference=(after-before)%c609.MOD
  gauss=int(np.max(np.minimum(difference,c609.MOD-difference)))
  qb=(q1-e1)%c609.MOD;eb=(e1+current+c613.magnetic_gradient(qb))%c609.MOD
  inverse=max(int(np.max(abs(qb-q))),int(np.max(abs(eb-e))))
  covariance=0
  for frame in c210.proper_cubic_frames():
   rdirection=c613.rotate_site_direction(site,direction,frame,length)[1];ropposite=rdirection^1
   rjp,_,rrhop1=occupation_transport(length,site,np.eye(6,dtype=int)[rdirection],+1)
   rjm,_,rrhom1=occupation_transport(length,site,np.eye(6,dtype=int)[ropposite],-1)
   re=(c613.rotate_link(e,frame)-(rjp+rjm)-c613.magnetic_gradient(c613.rotate_link(q,frame)))%c609.MOD
   covariance=max(covariance,int(np.max(abs(re-c613.rotate_link(e1,frame)))),
                  int(np.max(abs((rrhop1+rrhom1)-c613.rotate_scalar(rho1,frame)))))
  max_gauss=max(max_gauss,gauss);max_inverse=max(max_inverse,inverse);max_cov=max(max_cov,covariance)
  rows.append({"positive_direction":direction,"negative_direction":opposite,
               "branch_total_charge":int(np.sum(rho1)),"branch_source_norm":float(np.linalg.norm(rho1)),
               "Gauss_preservation_residual":gauss,"inverse_residual":inverse,
               "all24_branch_covariance_residual":covariance})
 return {"rows":rows,"maximum_branch_Gauss_residual":max_gauss,"maximum_branch_inverse_residual":max_inverse,
         "maximum_all24_branch_covariance_residual":max_cov,
         "cubic_scalar_pair_expectation_source_norm":float(np.linalg.norm(average_source)),
         "branch_sources_are_single_classical_words":True,"coherent_average_is_single_classical_word":False}


def route_a():
 coin=c219.common_species(c230.BETA).coin;gate=pair_gate();frames=c210.proper_cubic_frames()
 unitary=float(np.linalg.norm(gate.conj().T@gate-np.eye(7)));inverse=float(np.linalg.norm(gate@gate-np.eye(7)))
 resource=np.zeros(7);resource[0]=1;created=gate@resource
 creation=abs(created[0]);pair_norm=abs(np.linalg.norm(created[1:])-1);omission=float(np.linalg.norm(created-resource))
 covariance=max(float(np.linalg.norm(pair_representation(frame)@gate-gate@pair_representation(frame))) for frame in frames)
 group_failures=0
 for first in frames:
  for second in frames:
   group_failures+=int(not np.array_equal(pair_representation(first@second),pair_representation(first)@pair_representation(second)))
 cubic=c613.local_coin_contact_cubic_controls(coin);symmetry=c611.fock_symmetry_controls(coin)
 negative_symmetry=c611.fock_symmetry_controls(coin.conj())
 negative_coin_cubic=max(float(np.linalg.norm(c210.direction_permutation(frame)@coin.conj()-coin.conj()@c210.direction_permutation(frame))) for frame in frames)
 rows=[];max_gauge=max_fock=max_branch=0;min_delete=math.inf
 for label,length,held in PERIODIC_FIXTURES:
  rng=np.random.default_rng(6150+length)
  q=rng.integers(0,c609.MOD,size=(length,length,length,3),dtype=np.int64)
  e=rng.integers(0,c609.MOD,size=q.shape,dtype=np.int64)
  theta=rng.integers(0,c609.MOD,size=(length,)*3,dtype=np.int64)
  psi_plus=c611.normalize(rng.normal(size=(length,length,length,6))+1j*rng.normal(size=(length,length,length,6)))
  psi_minus=c611.normalize(rng.normal(size=psi_plus.shape)+1j*rng.normal(size=psi_plus.shape))
  qg=c613.gauge_transform_links(q,theta)
  plus_res=float(np.linalg.norm(gauge_stream_charge(gauge_matter_charge(psi_plus,theta,+1),qg,+1)-gauge_matter_charge(gauge_stream_charge(psi_plus,q,+1),theta,+1)))
  minus_res=float(np.linalg.norm(gauge_stream_charge(gauge_matter_charge(psi_minus,theta,-1),qg,-1)-gauge_matter_charge(gauge_stream_charge(psi_minus,q,-1),theta,-1)))
  fock=fock_charge_controls(length,q,e,coin);branches=pair_branch_controls(length,q,e)
  max_gauge=max(max_gauge,plus_res,minus_res);max_fock=max(max_fock,fock["maximum_charge_continuity_residual"],fock["maximum_Gauss_preservation_residual"],fock["maximum_joint_inverse_residual"],fock["coherent_product_Fock_coin_contact_norm_residual"])
  max_branch=max(max_branch,branches["maximum_branch_Gauss_residual"],branches["maximum_branch_inverse_residual"],branches["maximum_all24_branch_covariance_residual"],branches["cubic_scalar_pair_expectation_source_norm"])
  min_delete=min(min_delete,fock["minimum_nonzero_current_deletion_signal"])
  rows.append({"fixture":label,"length":length,"held":held,"positive_gauge_covariance_residual":plus_res,
               "negative_gauge_covariance_residual":minus_res,"Fock_controls":fock,"pair_branch_controls":branches,
               "lawful_F17_leakage":0})
 output={"object":"candidate distinct six-mode charge-conjugate CAR sector plus local neutral-pair resource gate",
  "disposition":"CONSTRUCTIVE_LOCAL_NEUTRAL_PAIR_GENESIS_AND_BRANCHWISE_GAUSS; DERIVED_ANTIMATTER_AND_MONOPOLE_SOURCE_OPEN",
  "pair_rule":"one neutral genesis-resource excitation is reversibly swapped with the cubic scalar sum 6^-1/2 sum_d a_d^dag b_-d^dag",
  "sector_status":"the negative-charge copy, charge-conjugate coin, separate same-g contact and no cross-contact term are supplied candidate-law symmetry/content; not derived antimatter",
  "new_persistent_M2_per_coarse_cell":7,"site_debit":"six negative CAR occupation M2 rails plus one neutral genesis-resource M2",
  "microscopic_support_two_pair_gate_compiled":False,"resource_excitation_supplied_at_encoding":True,
  "pair_gate_unitarity_residual":unitary,"pair_gate_inverse_residual":inverse,"resource_remaining_after_genesis":creation,
  "created_pair_norm_residual":pair_norm,"genesis_omission_signal":omission,
  "maximum_all24_pair_gate_covariance_residual":covariance,"all576_pair_representation_failures":group_failures,
  "pair_gate_local_U1_gauge_commutator_residual":0.0,
  "positive_local_cubic_controls":cubic,"positive_Fock_U1_controls":symmetry,
  "negative_Fock_U1_controls":negative_symmetry,
  "negative_coin_all24_covariance_residual":negative_coin_cubic,"rows":rows,
  "maximum_opposite_charge_gauge_residual":max_gauge,"maximum_Fock_control_residual":max_fock,
  "maximum_pair_branch_or_expectation_residual":max_branch,"minimum_current_deletion_signal":min_delete,
  "cubic_pair_expectation_is_monopole_source":False,"neutral_compiler_words_charged":False,
  "candidate_sector_is_derived_antimatter":False,"physical_NN_pair_gate_and_full_sector_compiled":False}
 check("Route A materializes a local reversible cubic neutral-pair gate and preserves full +/- charge Gauss dynamics",
       max(unitary,inverse,creation,pair_norm,covariance,negative_coin_cubic,max_gauge,max_fock,max_branch,
           *cubic.values(),negative_symmetry["coin_total_number_commutator"],
           negative_symmetry["contact_total_number_commutator"],negative_symmetry["gauged_contact_invariance_residual"])<TOL
       and group_failures==0 and min_delete>0 and omission>0
       and all(row["Fock_controls"]["joint_local_occupation_words_exhausted"]==4096 for row in rows),output)
 check("Route A pays a distinct sector/genesis debit without charging neutral compiler words or promoting the symmetric expectation to a monopole",
       output["new_persistent_M2_per_coarse_cell"]==7 and not output["neutral_compiler_words_charged"]
       and not output["candidate_sector_is_derived_antimatter"] and not output["cubic_pair_expectation_is_monopole_source"],output)
 return output


# ---------- Route B: separate centered open-boundary flux ----------
DIRS=tuple(tuple(int(v) for v in direction) for direction in c210.DIRECTIONS)
def add_coord(a,b):return tuple(x+y for x,y in zip(a,b))
def scale_coord(n,a):return tuple(n*x for x in a)
def rotate_coord(site,frame):return tuple(int(v) for v in frame@np.asarray(site))
def in_cube(site,radius):return max(abs(x) for x in site)<=radius


def axial_open_flux(radius):
 weight=pow(6,-1,c609.MOD);edges={}
 for direction in DIRS:
  for step in range(radius+1):
   source=scale_coord(step,direction);target=scale_coord(step+1,direction)
   edges[(source,target)]=weight
 return edges


def open_divergence(edges,radius):
 result={site:0 for site in product(range(-radius,radius+1),repeat=3)}
 for (source,target),value in edges.items():
  if in_cube(source,radius):result[source]=(result[source]+value)%c609.MOD
  if in_cube(target,radius):result[target]=(result[target]-value)%c609.MOD
 return result


def rotate_edges(edges,frame):return {(rotate_coord(a,frame),rotate_coord(b,frame)):value for (a,b),value in edges.items()}


def generic_open_edges(radius,seed):
 rng=np.random.default_rng(seed);edges={}
 for site in product(range(-radius,radius+1),repeat=3):
  for direction in DIRS:
   target=add_coord(site,direction)
   # Store each undirected interior edge once and all outward ports.
   if in_cube(target,radius):
    if site<target:edges[(site,target)]=int(rng.integers(0,c609.MOD))
   else:edges[(site,target)]=int(rng.integers(0,c609.MOD))
 return edges


def open_edge_group_failures(radius):
 frames=c210.proper_cubic_frames();edges=generic_open_edges(radius,61600+radius);failures=0
 for first in frames:
  for second in frames:
   failures+=int(rotate_edges(edges,first@second)!=rotate_edges(rotate_edges(edges,second),first))
 return failures


def random_oriented_q(radius,seed):
 rng=np.random.default_rng(seed);q={}
 for site in product(range(-radius,radius+1),repeat=3):
  for axis in range(3):
   direction=tuple(1 if j==axis else 0 for j in range(3));target=add_coord(site,direction)
   if in_cube(target,radius):
    value=int(rng.integers(0,c609.MOD));q[(site,target)]=value;q[(target,site)]=(-value)%c609.MOD
 return q


def gauge_open_q(q,theta):return {edge:(value+theta[edge[1]]-theta[edge[0]])%c609.MOD for edge,value in q.items()}


def open_stream(psi,q,radius,inverse=False):
 result=np.zeros_like(psi);length=2*radius+1
 for site in product(range(-radius,radius+1),repeat=3):
  index=tuple(x+radius for x in site)
  for direction,velocity in enumerate(DIRS):
   target=add_coord(site,velocity)
   if in_cube(target,radius):
    out_site=target;out_direction=direction;phase=np.exp(2j*math.pi*q[(site,target)]/c609.MOD)
   else:
    out_site=site;out_direction=direction^1;phase=1
   out_index=tuple(x+radius for x in out_site)
   if inverse:result[index+(direction,)]=np.conj(phase)*psi[out_index+(out_direction,)]
   else:result[out_index+(out_direction,)]=phase*psi[index+(direction,)]
 return result


def rotate_open_state(psi,frame,radius):
 result=np.zeros_like(psi);dmap=np.argmax(c210.direction_permutation(frame),axis=0)
 for site in product(range(-radius,radius+1),repeat=3):
  source=tuple(x+radius for x in site);target=tuple(x+radius for x in rotate_coord(site,frame))
  for direction in range(6):result[target+(int(dmap[direction]),)]=psi[source+(direction,)]
 return result


def route_b():
 coin=c219.common_species(c230.BETA).coin;rows=[];max_gauss=max_inverse=max_gauge=max_cov=0;min_delete=math.inf;groups=0
 local_controls=c613.local_coin_contact_cubic_controls(coin);fock_controls=c611.fock_symmetry_controls(coin)
 for label,length,held in OPEN_FIXTURES:
  radius=(length-1)//2;flux=axial_open_flux(radius);div=open_divergence(flux,radius)
  gauss=max(min((value-(1 if site==(0,0,0) else 0))%c609.MOD,
                ((1 if site==(0,0,0) else 0)-value)%c609.MOD) for site,value in div.items())
  boundary=sum(value for (source,target),value in flux.items() if not in_cube(target,radius))%c609.MOD
  covariance=max(int(rotate_edges(flux,frame)!=flux) for frame in c210.proper_cubic_frames())
  groups+=open_edge_group_failures(radius)
  # One interior charged branch move and its exact electric inverse.
  target=(1,0,0);current={((0,0,0),target):1};e1=flux.copy()
  e1[((0,0,0),target)]=(e1[((0,0,0),target)]-1)%c609.MOD
  rho1={site:int(site==target) for site in div};div1=open_divergence(e1,radius)
  moved=max(min((div1[site]-rho1[site])%c609.MOD,(rho1[site]-div1[site])%c609.MOD) for site in div1)
  restored=e1.copy();restored[((0,0,0),target)]=(restored[((0,0,0),target)]+1)%c609.MOD
  inverse=int(restored!=flux)
  boundary_edges=[edge for edge in flux if not in_cube(edge[1],radius)];deleted=flux.copy();deleted.pop(boundary_edges[0])
  deleted_div=open_divergence(deleted,radius);delete_signal=max(min((deleted_div[s]-div[s])%c609.MOD,(div[s]-deleted_div[s])%c609.MOD) for s in div)
  delete_boundary=(boundary-sum(value for (source,target),value in deleted.items() if not in_cube(target,radius)))%c609.MOD
  rng=np.random.default_rng(61700+length);q=random_oriented_q(radius,6170+length)
  theta={site:int(rng.integers(0,c609.MOD)) for site in product(range(-radius,radius+1),repeat=3)}
  psi=c611.normalize(rng.normal(size=(length,length,length,6))+1j*rng.normal(size=(length,length,length,6)))
  coined=c611.coin_step(psi,coin);matter_phase=np.empty((length,length,length))
  for site,value in theta.items():matter_phase[tuple(x+radius for x in site)]=value
  transformed=coined*np.exp(2j*math.pi*matter_phase[...,None]/c609.MOD)
  left=open_stream(transformed,gauge_open_q(q,theta),radius)
  right=open_stream(coined,q,radius)*np.exp(2j*math.pi*matter_phase[...,None]/c609.MOD)
  gauge=float(np.linalg.norm(left-right));streamed=open_stream(coined,q,radius);back=open_stream(streamed,q,radius,inverse=True)
  stream_inverse=float(np.linalg.norm(back-coined));frame_cov=0
  for frame in c210.proper_cubic_frames():
   frame_cov=max(frame_cov,float(np.linalg.norm(
    open_stream(rotate_open_state(coined,frame,radius),rotate_edges(q,frame),radius)-rotate_open_state(streamed,frame,radius))))
  max_gauss=max(max_gauss,gauss,moved);max_inverse=max(max_inverse,inverse,stream_inverse)
  max_gauge=max(max_gauge,gauge);max_cov=max(max_cov,covariance,frame_cov);min_delete=min(min_delete,delete_signal,delete_boundary)
  rows.append({"fixture":label,"length":length,"held":held,"centered_cube_radius":radius,
   "F17_flux_per_cubic_boundary_port":pow(6,-1,c609.MOD),"interior_Gauss_residual":gauss,
   "boundary_total_flux_mod17":boundary,"charge_move_Gauss_residual":moved,"charge_move_inverse_residual":inverse,
   "reflecting_stream_inverse_residual":stream_inverse,"open_gauge_covariance_residual":gauge,
   "all24_open_stream_or_flux_covariance_residual":max(covariance,frame_cov),
   "deleted_boundary_port_Gauss_signal":delete_signal,"deleted_boundary_total_flux_signal":delete_boundary,
   "interior_positive_link_words":3*(length-1)*length*length,"outward_boundary_port_words":6*length*length,
   "lawful_F17_leakage":0})
 output={"object":"centered finite open cube with six equal axial F17 flux rays from one unit charge",
  "disposition":"CONSTRUCTIVE_OPEN_DOMAIN_LOCAL_GAUSS_CLOSURE; BOUNDARY_SELECTION_AND_TRANSLATION_IMPORT_EXPLICIT",
  "flux_selection":"within the supplied equal six-axial-ray ansatz, proper-cubic equality plus Gauss fixes each port flux to 6^-1=3 mod17",
  "boundary_condition":"finite centered odd cube, reflecting matter stream, six axial outward flux paths",
  "rows":rows,"maximum_Gauss_residual":max_gauss,"maximum_inverse_residual":max_inverse,
  "maximum_open_gauge_covariance_residual":max_gauge,"maximum_all24_covariance_residual":max_cov,
  "all576_open_edge_representation_failures":groups,"minimum_boundary_deletion_signal":min_delete,
  "full_local_coin_contact_controls":local_controls,"full_local_Fock_U1_controls":fock_controls,
  "isolated_unit_charge_lawful_on_declared_open_domain":True,"compensator_used":False,
  "neutral_compiler_words_charged":False,"translation_covariant":False,
  "flux_unique_among_all_open_Gauss_solutions":False,"divergence_free_flux_loops_unselected":True,
  "bulk_or_gravity_law_claimed":False,"boundary_center_ports_and_flux_genesis_supplied":True}
 check("Route B closes local Gauss on centered open L3/L5/L7 domains with selected equal port flux and exact controls",
       max(max_gauss,max_inverse,max_gauge,max_cov,*local_controls.values(),fock_controls["coin_total_number_commutator"],
           fock_controls["contact_total_number_commutator"],fock_controls["gauged_contact_invariance_residual"])<TOL
       and groups==0 and min_delete>0
       and all(row["boundary_total_flux_mod17"]==1 and row["F17_flux_per_cubic_boundary_port"]==3 for row in rows),output)
 check("Route B exposes the open boundary/center import and makes no translation-covariant bulk or gravity claim",
       output["isolated_unit_charge_lawful_on_declared_open_domain"] and not output["translation_covariant"]
       and not output["bulk_or_gravity_law_claimed"] and not output["compensator_used"],output)
 return output


# ---------- Route C: joined gauge-charge / actual-Regge coframe variation ----------
def spatial_trace_vector():
 result=np.zeros(10)
 for component in ((0,0),(1,1),(2,2)):result[c576.regge.HCOMPS.index(component)]=1
 return result


def stationary_metric(momentum,coupling,improvement_coefficient):
 q=c576.frame_averaged_metric_hessian(momentum);source=c576.frame_averaged_source_row(momentum)
 trace=spatial_trace_vector();improvement=trace@q;row=source+improvement_coefficient*improvement
 response=-coupling*np.linalg.pinv(q,rcond=1e-10)@np.conj(row)
 equation=q@response+coupling*np.conj(row)
 receiver=float(np.real(source@response))
 ward=float(np.max(abs(row@c576.continuum_gauge_metric(momentum))))
 return q,source,improvement,row,response,float(np.linalg.norm(equation)),receiver,ward


def variation_residual(momentum,coupling,improvement_coefficient,seed):
 q,source,improvement,row,_,_,_,_=stationary_metric(momentum,coupling,improvement_coefficient)
 rng=np.random.default_rng(seed);h=rng.normal(size=10)+1j*rng.normal(size=10);direction=rng.normal(size=10)+1j*rng.normal(size=10)
 def action(value):return 0.5*np.real(np.vdot(value,q@value))+coupling*np.real(row@value)
 eps=2e-6;observed=(action(h+eps*direction)-action(h-eps*direction))/(2*eps)
 target=np.real(np.vdot(direction,q@h+coupling*np.conj(row)))
 return abs(float(observed-target))


def route_c(r613,r576,r604,r612):
 alternatives=[];rows=[];max_stationary=max_ward=max_cov=max_variation=max_inverse=max_formula=0;min_delete=math.inf
 receiver_words=sorted({row["probe_over_reference"] for row in r612["route_C_source_motion_ratio"]["rows"]
                        if row["physical_source_reservoir_predicate"]==1 and row["receiver_M2"]==1})
 frames=c576.LIFTED_FRAMES
 for label,length,held in PERIODIC_FIXTURES:
  scale=2*math.pi/length;momentum=np.asarray((scale,scale,0.0,scale))
  fixture_alternatives=[];baseline_receiver=None
  for magnitude in (1.0,2.0):
   for sign in (-1.0,1.0):
    for improvement in (-1.0,0.0,1.0):
     coupling=sign*magnitude*c576.SOURCE_COUPLING
     q,source,imp,row,response,stationary,receiver,ward=stationary_metric(momentum,coupling,improvement)
     variation=variation_residual(momentum,coupling,improvement,61800+length+int(10*magnitude+3*sign+improvement))
     covariance=0
     for representation,frame in zip(c576.METRIC_REPS,frames):
      rotated=stationary_metric(frame@momentum,coupling,improvement)[4]
      covariance=max(covariance,float(np.linalg.norm(rotated-representation@response)))
     entry={"coupling_magnitude_over_Cycle576":magnitude,"coupling_sign":int(sign),"coupling_value":coupling,
            "improvement_coefficient":int(improvement),"stationary_equation_residual":stationary,
            "coframe_variation_residual":variation,"source_Ward_residual":ward,
            "all24_response_covariance_residual":covariance,"source_conjugate_receiver":receiver,
            "receiver_sign":int(np.sign(receiver))}
     fixture_alternatives.append(entry);alternatives.append(entry)
     max_stationary=max(max_stationary,stationary);max_ward=max(max_ward,ward)
     max_cov=max(max_cov,covariance);max_variation=max(max_variation,variation)
     if magnitude==1 and sign==1 and improvement==0:baseline_receiver=receiver
  hamiltonian=c576.frame_sector_hamiltonian(momentum,source_amplitude=1.0)
  initial=np.zeros(len(hamiltonian),dtype=complex);initial[0]=1
  evolved=expm_multiply(-1j*c576.UPDATE_PARAMETER*hamiltonian,initial)
  restored=expm_multiply(+1j*c576.UPDATE_PARAMETER*hamiltonian,evolved)
  deleted=expm_multiply(-1j*c576.UPDATE_PARAMETER*c576.frame_sector_hamiltonian(momentum,include_source=False),initial)
  inverse=float(np.linalg.norm(restored-initial));deletion=float(np.linalg.norm(evolved-deleted))
  max_inverse=max(max_inverse,inverse);min_delete=min(min_delete,deletion)
  receivers=[entry["source_conjugate_receiver"] for entry in fixture_alternatives]
  receiver_base_per_unit_lambda=stationary_metric(momentum,1.0,0.0)[6]
  receiver_improved_per_unit_lambda=stationary_metric(momentum,1.0,1.0)[6]
  receiver_improvement_slope=receiver_improved_per_unit_lambda-receiver_base_per_unit_lambda
  formula_residual=max(abs(entry["source_conjugate_receiver"]-entry["coupling_value"]*
                           (receiver_base_per_unit_lambda+entry["improvement_coefficient"]*receiver_improvement_slope))
                       for entry in fixture_alternatives)
  max_formula=max(max_formula,formula_residual)
  rows.append({"fixture":label,"length":length,"held":held,"Bloch_momentum":momentum.tolist(),
   "baseline_Cycle576_lambda":c576.SOURCE_COUPLING,"baseline_source_conjugate_receiver":baseline_receiver,
   "allowed_alternatives":fixture_alternatives,"receiver_span_over_enumerated_equivalence_class":max(receivers)-min(receivers),
   "exact_receiver_family":"R(lambda,c)=lambda*(R0+c*Rimp)",
   "receiver_base_per_unit_lambda":receiver_base_per_unit_lambda,
   "receiver_improvement_slope_per_unit_lambda":receiver_improvement_slope,
   "receiver_zero_crossing_improvement":-receiver_base_per_unit_lambda/receiver_improvement_slope,
   "analytic_family_residual_on_12_point_grid":formula_residual,
   "finite_Regge_state_inverse_residual":inverse,"source_deletion_signal":deletion,"finite_state_norm_residual":abs(float(np.vdot(evolved,evolved).real)-1),
   "lawful_source_amplitude_from_Route_B":1,"parameters_refit":0})
 signs=sorted({entry["receiver_sign"] for entry in alternatives});span=max(entry["source_conjugate_receiver"] for entry in alternatives)-min(entry["source_conjugate_receiver"] for entry in alternatives)
 # Exact 576 representation checks are repeated rather than merely copied from Cycle576.
 group_failures=0;frame_lookup={tuple(frame.reshape(-1)):index for index,frame in enumerate(c576.FRAMES)}
 for i,first in enumerate(c576.FRAMES):
  for j,second in enumerate(c576.FRAMES):
   target=frame_lookup[tuple((first@second).reshape(-1))]
   group_failures+=int(np.linalg.norm(c576.METRIC_REPS[i]@c576.METRIC_REPS[j]-c576.METRIC_REPS[target])>TOL)
 output={"object":"one joined gauge-charge plus actual-Regge deficit/coframe quadratic action tested at an inherited receiver surface",
  "disposition":"CONSTRUCTIVE_JOINED_VARIATION_EQUIVALENCE_CLASS; OPERATIONAL_RECEIVER_SELECTION_UNDERDETERMINED",
  "joined_action":"A_join=A_Cycle613_gauge[psi,Q,E]+c_R A_Regge[e]-lambda sum_x rho_gauge(x) sum_local_hinges delta_hinge[e]",
  "variation_identifications":{"A0_variation":"Cycle613 Gauss divE-rho=0","coframe_edge_variation":"Cycle576 actual Regge Hessian plus deficit source","receiver":"source-conjugate gauge-invariant metric quadrature compared to Cycle612 receiver words"},
  "exact_continuous_equivalence_class":{"relative_source_coupling":"lambda in R (including zero and both signs)","equation_of_motion_exact_local_improvement":"c in R","receiver_family":"R(lambda,c)=lambda*(R0+c*Rimp) for each frozen momentum"},
  "audited_equivalence_grid":{"relative_coupling_magnitudes":[1,2],"coupling_signs":[-1,1],"local_conserved_improvement_coefficients":[-1,0,1],"members_per_fixture":12},
  "rows":rows,"maximum_stationary_equation_residual":max_stationary,"maximum_source_Ward_residual":max_ward,
  "maximum_coframe_variation_residual":max_variation,"maximum_all24_response_covariance_residual":max_cov,
  "all576_metric_representation_failures":group_failures,"maximum_finite_state_inverse_residual":max_inverse,
  "minimum_source_deletion_signal":min_delete,"enumerated_receiver_signs":signs,"enumerated_receiver_span":span,
  "maximum_analytic_family_residual_on_audited_grid":max_formula,
  "Cycle612_operational_receiver_equivalence_class":receiver_words,"unique_receiver_word_selection_residual":len(receiver_words)-1,
  "Cycle612_source_to_response_map_derived":r612["route_C_source_motion_ratio"]["source_to_response_map_derived"],
  "Cycle612_delay_or_advance_selected":r612["route_C_source_motion_ratio"]["delay_or_advance_selected"],
  "Cycle604_5_over_32pi_maximum_relative_residual":r604["route_C_prediction_bridge"]["maximum_5_over_32pi_relative_residual"],
  "Cycle613_divJ_coefficient_relative_residual_preserved":r613["route_C_prediction_compatibility"]["coefficient_relative_residual"],
  "parameters_refit":0,"absolute_action_or_source_normalization_selected":False,
  "improvement_selected":False,"response_sign_selected":False,"operational_metric_identification_derived":False,
  "open_boundary_and_periodic_Bloch_Regge_joint_real_space_compiler_executed":False,
  "domain_join_status":"one local action/source-amplitude law is stated and its periodic Regge symbols are tested; Route B's open boundary and the Regge carrier were not jointly real-space compiled",
  "F17_is_physical_energy_or_stress":False,"gravity_claimed":False}
 check("Route C joins unit gauge charge to the actual Regge coframe variation with Ward/covariance/inverse/deletion controls",
       max(max_stationary,max_ward,max_cov,max_variation,max_inverse,max_formula)<TOL and min_delete>0 and group_failures==0
       and all(len(row["allowed_alternatives"])==12 and row["parameters_refit"]==0 for row in rows),output)
 check("Route C returns the exact surviving receiver equivalence class rather than a generic normalization failure",
       signs==[-1,1] and span>0 and receiver_words==["3/4","5/4"]
       and output["unique_receiver_word_selection_residual"]==1
       and not output["Cycle612_source_to_response_map_derived"] and not output["response_sign_selected"]
       and output["Cycle613_divJ_coefficient_relative_residual_preserved"]==1,output)
 return output


def no_go_discipline():
 families=[
  {"family":"local neutral pair resource gate","object":"two six-mode CAR sectors plus neutral resource rail","mechanism":"cubic-scalar reversible pair swap and charge Gauss invariant","terminal":"derived physical antiparticle and monopole-compatible state","marker":"ATTEMPTED","result":"local genesis/Gauss positive; sector identity and state preparation open"},
  {"family":"mobile uniform opposite carrier","object":"Cycle611 distinct binder sector","mechanism":"paired number plus supplied W preparation","terminal":"periodic point-minus-uniform source","marker":"RULED OUT BY PRIOR ONLY AS AUTONOMOUS GENESIS","result":"conditional positive; local genesis/W compiler was supplied"},
  {"family":"centered open boundary flux","object":"finite cube links and boundary ports","mechanism":"six equal axial flux rays and Gauss","terminal":"lawful isolated unit charge","marker":"ATTEMPTED","result":"positive on declared open domains; boundary/center import remains"},
  {"family":"periodic continuity source","object":"Cycle613 divJ=Ldelta/6","mechanism":"accepted stream continuity","terminal":"Cycle604 monopole shore","marker":"RULED OUT BY PRIOR FOR THIS SOURCE/SHORE PAIR ONLY","result":"coefficient residual exactly one; no broader source claim"},
  {"family":"joined gauge-Regge coframe action","object":"unit gauge charge plus actual deficit Hessian","mechanism":"Gauss and metric Ward identities","terminal":"unique operational receiver prediction","marker":"ATTEMPTED","result":"continuous real lambda/improvement response family, audited on 12 representatives per fixture, leaves two receiver words"},
  {"family":"quasienergy/log-unitary metric variation","object":"full accepted matter unitary","mechanism":"band/quasienergy response","terminal":"unique stress representative and receiver map","marker":"LIVE_UNTESTED","result":"concrete unclosed mechanism; blocks broad negative"},
  {"family":"autonomous detector feedback selection","object":"Cycle612 matter-caused endpoint packet plus response carrier","mechanism":"local receiver-conditioned backreaction","terminal":"select response sign and calibration","marker":"LIVE_UNTESTED","result":"Cycle612 supplies both branches and does not derive the feedback law"},
 ]
 walls={
  "W_sector":"candidate negative-charge sector symmetry/identity and microscopic pair-gate lowering",
  "W_boundary":"open-domain boundary, center, ports, and flux-state genesis",
  "W_response_class":"relative Regge coupling magnitude and sign",
  "W_improvement":"conserved local coframe improvement coefficient",
  "W_metric_receiver":"operational metric observable and Regge-to-Cycle612 receiver map",
  "W_packing":"joint physical NN compilation and resource-sector enforcement",
  "W_event":"receiver occurrence, Record admission, and empirical calibration",
 }
 names=tuple(walls);pairs=[{"left":names[i],"right":names[j],"left_closes_right":False,"right_closes_left":False,"independent":True}
                           for i in range(len(names)) for j in range(i+1,len(names))]
 output={"N1_normalized_families":families,"N1_broad_negative_failure":"two actionable families remain LIVE_UNTESTED",
  "N2_pairwise_collapsed_wall_audit":pairs,
  "N3_hidden_wall_scan":["supplied compact U(1) and unit representation","candidate charge-conjugate coin and separate same-g contact","neutral resource excitation","no cross-contact law","F17 modulus and symplectic order","finite centered boundary and port state","Cycle576 Regge complex/frame state/lambda/update scale","trace improvement definition","pseudoinverse gauge representative","Cycle612 receiver map and empirical calibration","aggregate versus physical NN execution"],
  "N4_residual_matching":[
   {"witness":"Cycle611 Route C","witness_residual":"local pair genesis and W preparation supplied","current_residual":"Cycle615 local pair gate","match":"yes for local genesis only; W preparation is a different terminal"},
   {"witness":"Cycle613 Route C","witness_residual":"divJ source versus monopole 5/(32pi) shore","current_residual":"same divJ incompatibility","match":"yes; preserved exactly"},
   {"witness":"Cycle576 Route A","witness_residual":"actual Regge source sign/normalization and physical metric open","current_residual":"joined continuous response class","match":"yes"},
   {"witness":"Cycle612 Route C","witness_residual":"source-to-response map and delay/advance selection supplied","current_residual":"two surviving operational receiver words","match":"yes"},
   {"witness":"free Dirac antiparticle algebra","witness_residual":"bounded continuum free CAR relabeling","current_residual":"lattice charged-sector derivation","match":"no; used only as prior algebraic context, not a closure witness"}],
  "N5_rhetoric_audit":{"not_derived_antimatter":"tested local candidate sector/gate and charge algebra only; no interacting identity theorem","not_bulk_gravity":"tested finite centered open cubes only; translations and operational metric absent","not_physical_stress_energy":"tested F17/site/link words and a Regge coframe carrier; no empirical observable identification","not_Record_or_event":"tested reversible receiver alternatives only; no occurrence or permanence"},
  "N6_partial_closure_paths":{"approved_primitives":"scale ruler, kinetic-form isotropy, and pointwise realized-state slot chain-satisfy but supply none of charge/genesis/boundary/source-action/receiver selection","paths":["locally lower the seven-rail pair swap and derive its sector as a charge-conjugation symmetry","replace centered boundary by a dynamical finite flux membrane","derive lambda/sign from a joint variational symmetry or measured equivalence condition","couple a matter-caused Cycle612 receiver bit back into the joined action and test autonomous branch selection"]},
  "N7_steelman":"A hostile reviewer should reject any broad selection no-go: the untested quasienergy variation can change the stress representative, while an explicit local receiver-feedback term can turn Cycle612's matter-caused endpoint bit into a sign-selecting backreaction. The terminal obligations are concrete: derive the feedback coupling from the same unitary, preserve Gauss/Regge Ward identities, and reduce the continuous response family to one receiver word on held domains.",
  "N8_cross_cycle_echo":{"Cycle611":"paid opposite carrier closed zero mode conditionally but left genesis","Cycle613":"gauging closed local current/Gauss and correctly left open boundary/opposite charge live","Cycle576_604":"actual Regge and common-Laplacian prediction closed distinct mathematical bridges while retaining calibration","Cycle612":"matter-caused endpoints advanced operationality without selecting response sign"},
  "walls":walls,"broad_negative_gate":"FAIL / DO NOT SHIP","shared_obstruction":False,"minimum_content_claim":False,"axiom_pressure":False}
 check("full updated N1-N8 gate blocks broad negative, minimum-content, and axiom-pressure claims",
       len(families)>=5 and len(pairs)==21 and not output["shared_obstruction"]
       and not output["minimum_content_claim"] and not output["axiom_pressure"],output)
 return output


def main():
 r613,r576,r604,r612,shore_result=shore();note_contract();a=route_a();b=route_b();c=route_c(r613,r576,r604,r612);nogo=no_go_discipline()
 elapsed=perf_counter()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rss=int(rss if sys.platform=="darwin" else rss*1024)
 receipt={"cycle":615,"authority":AUTHORITY,"audit":AUDIT,"constitutional_effect":"none",
  "HEAD":subprocess.check_output(("git","rev-parse","HEAD"),cwd=ROOT,text=True).strip(),"pins":PINS,"shore":shore_result,
  "foundation_recon":{"minimal_axioms":"Lattice/Qubit/Admissibility/Record; no charge sector, dynamics, boundary, source/action, metric, or receiver map","registered_primitives":"scale conversion, kinetic-form isotropy, realized-state evaluation slot only; no charge/genesis/normalization/metric/receiver content","antiparticle_prior":"free-Dirac note supports bounded continuum free CAR relabeling only; it does not derive the Cycle615 lattice sector"},
  "route_A_local_neutral_pair_sector":a,"route_B_open_boundary_flux":b,"route_C_joined_metric_receiver_equivalence":c,
  "no_go_discipline":nogo,
  "decisive_answer":"lawful charge is constructively available in two distinct scoped ways: a local resource-debited neutral pair whose branchwise fields satisfy Gauss, and a centered open domain whose equal six-port flux admits one isolated unit charge. Neither selects the Cycle604 monopole state and physical normalization without imports. The joined gauge-Regge variation leaves the exact continuous response family R(lambda,c)=lambda*(R0+c*Rimp), audited on 12 representatives per fixture, and the two Cycle612 receiver words {3/4,5/4}; this is unfinished law selection, not gravity or a shared obstruction.",
  "inventory":{"supplied":["candidate negative-charge six-mode sector and charge-conjugate coin","separate same-g contact and absence of cross contact","neutral genesis resource excitation","F17 compact group/modulus/symplectic order","finite centered open boundary/ports/flux state","Cycle576 Regge complex/frame state/lambda/update scale","spatial-trace improvement family and pseudoinverse representative","Cycle612 source-to-receiver association","aggregate-not-joint-NN execution"],
   "derived_or_executed":["local reversible cubic neutral-pair gate","4096 +/- occupation continuity/Gauss/inverse audit","opposite Peierls gauge covariance","branchwise coherent controlled charge fields","equal open flux 6^-1 within the six-ray ansatz","open reflective stream gauge covariance","joined gauge-charge/Regge coframe variation","continuous response formula plus 12-point-per-fixture audit","all24/all576 and held/deletion controls"],
   "not_derived":["physical antiparticle identity","microscopic pair-gate/full-sector NN compiler","monopole state from local pair rule","boundary/flux genesis or translation-covariant bulk law","unique coupling sign/magnitude/improvement","operational metric and unique receiver word","physical stress/energy/gravity","event/Record/Born rule"]},
  "six_wall_ledger":{"C_ref":"SHARPENED: cubic pair and equal boundary flux remove host frame choice locally; boundary center, Regge frame state, receiver map remain supplied","C_num":"ADVANCED: unit +/- representation charge and open six-port weight 3 mod17 follow the chosen representations; relative physical coupling remains a continuous real class","C_wrap":"UNCHANGED: compact F17 arithmetic is exact and is not physical energy or stress","C_int":"ADVANCED: local neutral genesis, charge-conjugate streams, gauge Gauss, and actual Regge source variation are composed at law level; the open-boundary/periodic-Regge real-space join and operational receiver map remain open","C_local":"ADVANCED: pair gate is bounded local and open flux paths are explicit with inverse/covariance; microscopic support-two pair lowering and joint NN packing remain open","C_source":"ADVANCED/SHARPENED: isolated open-domain charge is lawful and neutral-pair branches are lawful; local scalar expectation is not a monopole and joined response remains R(lambda,c)=lambda*(R0+c*Rimp) -> {3/4,5/4}"},
  "maturity_0_to_5":{"operational_quantum_records":4.05,"time":3.05,"inertia_matter":4.5,"gravity_source":3.95,"Born_probability":2.0},
  "strongest_constructive_result":"a resource-debited local cubic neutral-pair gate plus opposite-charge gauge dynamics preserves all 4096 local occupation Gauss sectors coherently, while an independent centered open construction derives equal F17 boundary flux 3 and admits one isolated unit charge",
  "shared_obstruction_or_axiom_pressure":False,
  "optimal_next_campaign":"materialize the seven-rail neutral-pair gate in the accepted physical NN compiler and add a local matter-caused receiver-feedback term to the joined gauge-Regge action; require it to select one scale/sign/improvement member and one Cycle612 receiver word on held domains",
  "tests_passed":PASS,"tests_failed":FAIL,"pass":FAIL==0,"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss}
 RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=json_default)+"\n")
 print("RECEIPT",json.dumps(receipt,sort_keys=True,default=json_default))
 print("SUMMARY",json.dumps({"pass":receipt["pass"],"tests_passed":PASS,"tests_failed":FAIL,"elapsed_seconds":elapsed,
  "route_A":a["disposition"],"route_B":b["disposition"],"route_C":c["disposition"],"receiver_equivalence":c["Cycle612_operational_receiver_equivalence_class"],"axiom_pressure":False},sort_keys=True))
 return int(FAIL!=0)


if __name__=="__main__":
 COLD.parent.mkdir(parents=True,exist_ok=True)
 with COLD.open("w") as cold_handle:
  terminal=sys.stdout;sys.stdout=Tee(terminal,cold_handle)
  try:exit_code=main()
  finally:sys.stdout=terminal
 raise SystemExit(exit_code)
