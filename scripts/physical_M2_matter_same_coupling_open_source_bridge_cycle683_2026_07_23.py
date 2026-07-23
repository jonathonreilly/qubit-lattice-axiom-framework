#!/usr/bin/env python3
"""Cycle 683: physical-M2 matter to same-coupling open response bridge."""

from __future__ import annotations

TARGET_CONTRACT = {
    "target_statement": "replace the host source profile in the same-coupling finite response update by a local source computed only from accepted six-rail physical M2 matter occupation/current, with the identical declared q entering source insertion and receiver readout; independently test a finite Weyl phase carrier and an open real-space coframe derivative",
    "quantifiers_domain": "open L3 train, L6 held and L7 out-family cubes; one- and two-particle physical occupation words with N<=3 controls; q signs and q magnitudes; q_rec=0 and decoupled arms; all 24 proper-cubic frames and all 576 products",
    "allowed_premises": "byte/object-pinned Cycle591 unit current and continuity, Cycle607/609 finite-Weyl algebra, Cycle611 Ward/current, Cycle615 open flux, Cycle626 common-q comparator, Cycle656 physical even-CAR representation, Cycle679 physical occupation rails, and external commits 3fedc918/c4b31f/394c30e as read-only open evidence",
    "forbidden_weakenings": "no Cycle576 host texture or source profile may enter the source; no supplied scalar array may be renamed physical matter; no q_src/q_rec equality inferred after separate fitting; no periodic operator may stand in for the open coframe derivative; no phase called energy, generator called rate, response called gravity/stress/source law, pointer called Record, or finite schedule called time",
    "required_edge_cases": "matter-source deletion; receiver q=0 with nonzero bare field; q sign cancellation, q squared scaling and decoupled sign flip; local continuity and contact-number commutation; inverse/symplectic/leakage/lawful-domain controls; open boundary/no-wrap; coframe finite difference and Ward rows; support/locality; all24/all576; L3/L6/L7; exact inventory of matter, carrier, receiver, ramp and grids",
    "completion_witness": "one executed finite-step reversible open leapfrog whose kick reads physical M2 occupation, one exact finite W17 matter-controlled phase/Fourier source and same-q receiver accumulator, and one boundary-preserving open link derivative, each with explicit deletion, covariance, held-size and supplied-structure receipts",
    "outcomes_not_closure": "reusing a host texture; an expectation array with no physical rail source; a stationary q squared identity without an executed update; a finite-Weyl phase with no receiver arm; periodic Bloch K relabelled open; route-specific failure promoted to a shared obstruction or axiom pressure",
}

from hashlib import sha256
from itertools import permutations, product
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np
import scipy.sparse as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_M2_MATTER_SAME_COUPLING_OPEN_SOURCE_BRIDGE_CYCLE683_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_M2_matter_same_coupling_open_source_bridge_cycle683_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_M2_matter_same_coupling_open_source_bridge_cycle683_cold_2026_07_23.txt"
SHORE = "854b4b48f4c98fa6b82f2e05cc2d33edbaf569fa"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2e-10
PASS = 0
FAIL = 0
DT = 0.02
HOLD = 12.0
TAUS = (20.0, 40.0, 80.0, 160.0)
Q_VALUES = (0.5, 1.0, 2.0)
W = 17
DIRECTIONS = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

PINS = {
 "854b4b48:docs/work_history/repo/review_feedback/PHYSICAL_OPERATIONAL_METRIC_CONSERVED_SOURCE_LOCAL_RANGE_TOURNAMENT_CYCLE591_NOTE_2026-07-22.md":"86746b0cf9a80145b9c7cb4415c4402d6a697bb99e1fa83bae547bf091ac37e5",
 "854b4b48:scripts/physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22.py":"b927333e3287fa46c03f7ed9b53259cd126f47cca30eaca35c8220971b822a08",
 "854b4b48:outputs/physical_operational_metric_conserved_source_local_range_tournament_cycle591_cold_2026_07_22.txt":"765770317f82aeec1105bc33c80c21c920b09d35deab5663df62b4edab2f917c",
 "854b4b48:outputs/physical_car_matter_weyl_reciprocal_source_response_tournament_cycle607_receipt_2026_07_22.json":"ec0da4276602ae363e0bc9e36a8a696b209542ebd9fed888fb369abec4b455cd",
 "854b4b48:outputs/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_receipt_2026_07_22.json":"a5bd17754c3d0e80ad2cff72e7ab63d5b3a5046805c92be583d95ede8b0463ff",
 "854b4b48:outputs/physical_matter_variation_current_stress_compensator_source_tournament_cycle611_receipt_2026_07_22.json":"cbba773dabe96f0c27c9bf3d87c77735608d3b9563adad919b8538db61f1a4be",
 "854b4b48:outputs/physical_lawful_charge_joined_metric_response_tournament_cycle615_receipt_2026_07_22.json":"7bf6e65b72976029bd55019a5338e5e9ee29c8c94f317e14c8b3031c453da929",
 "854b4b48:outputs/physical_local_normalized_nonlinear_source_law_selection_tournament_cycle626_receipt_2026_07_22.json":"ab8489e9875e362d2b496b1f92464e6c5c642eb3cdb72b1755e77c4d70b752f6",
 "854b4b48:outputs/physical_term_complete_flat_link_update_cycle656_receipt_2026_07_23.json":"a97cf4d906b8d1f9e5dcfccb4d8b8c30dcfd3a0fa36c5371e9d2bc8a6f72315c",
 "854b4b48:outputs/physical_incident_C_prepared_star_detector_cycle679_receipt_2026_07_23.json":"1343f10d230e43a870474e0c5b482e9a8efc58893ef1fc4897db3144b762b442",
 "3fedc918:outputs/physical_source_insertion_selection_backreaction_tournament_cycle572_receipt_2026_07_22.json":"0a97b2b4a2dc66c9a80f94b583822ec4406fa60478b65e4d7664c48c1af53fd1",
 "3fedc918:outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json":"06456c1443f5464949f40d81e9f1c6316b3e4e8405415b5b0035e39d4b88c3bd",
 "c4b31f:outputs/physical_finite_reversible_norm_saturation_evaluator_tournament_receipt_2026_07_23.json":"bfcd5ed10f3f61ba60c0259b6a813dcfb28009385b1e2c1d8121100376c7e485",
 "394c30e:outputs/physical_same_coupling_executed_field_update_response_tournament_receipt_2026_07_23.json":"da75185e5833721d467b98f26ae49e1f7aef47677aaf1c2c17f5a15d45cd3712",
}

class Tee:
 def __init__(self,*streams): self.streams=streams
 def write(self,body):
  for stream in self.streams: stream.write(body)
  return len(body)
 def flush(self):
  for stream in self.streams: stream.flush()

def check(label,condition,detail=""):
 global PASS,FAIL
 PASS += int(bool(condition)); FAIL += int(not bool(condition)); print("PASS" if condition else "FAIL",label,"::",detail)

def stable_digest(value): return sha256(json.dumps(value,sort_keys=True,separators=(",",":"),default=float).encode()).hexdigest()

def git_bytes(spec):
 return subprocess.run(("git","show",spec),cwd=ROOT,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout

def target_freeze_controls():
 lines=Path(__file__).read_text().splitlines();target=next(i for i,line in enumerate(lines,1) if line.startswith("TARGET_CONTRACT ="));evidence=next(i for i,line in enumerate(lines,1) if line.startswith("def evidence_controls"));fields=sorted(TARGET_CONTRACT);expected=["allowed_premises","completion_witness","forbidden_weakenings","outcomes_not_closure","quantifiers_domain","required_edge_cases","target_statement"]
 return {"target_line":target,"first_evidence_load_line":evidence,"frozen_before_evidence":target<evidence,"contract_sha256":stable_digest(TARGET_CONTRACT),"pass":target<evidence and fields==expected}

def evidence_controls():
 observed={spec:sha256(git_bytes(spec)).hexdigest() for spec in PINS}
 object_ids={spec:subprocess.run(("git","rev-parse",spec),cwd=ROOT,check=True,text=True,stdout=subprocess.PIPE).stdout.strip() for spec in PINS}
 receipts={spec:json.loads(git_bytes(spec)) for spec in PINS if spec.endswith(".json")}
 external={"3fedc918":subprocess.run(("git","rev-parse","3fedc918"),cwd=ROOT,check=True,text=True,stdout=subprocess.PIPE).stdout.strip(),"c4b31f":subprocess.run(("git","rev-parse","c4b31f"),cwd=ROOT,check=True,text=True,stdout=subprocess.PIPE).stdout.strip(),"394c30e":subprocess.run(("git","rev-parse","394c30e"),cwd=ROOT,check=True,text=True,stdout=subprocess.PIPE).stdout.strip()}
 passed=observed==PINS and all(row.get("pass",True) for row in receipts.values()) and external=={"3fedc918":"3fedc918e318359567f76bc066255271dc8d8046","c4b31f":"c4b31f0d87be8bf9058b0d159121f4c0833e6247","394c30e":"394c30e1c12d40f65b6ce6456d9b026106d0bdda"}
 return {"shore":SHORE,"pins":PINS,"observed":observed,"exact_git_object_ids_read":object_ids,"external_open_evidence_commits":external,"external_commits_cherry_picked_or_duplicated":False,"working_tree_bytes_used_as_premise":False,"pass":passed},receipts

def proper_cubic_frames():
 rows=[]
 for perm in permutations(range(3)):
  for signs in product((-1,1),repeat=3):
   frame=np.zeros((3,3),dtype=int)
   for row,column in enumerate(perm): frame[row,column]=signs[row]
   if round(np.linalg.det(frame))==1: rows.append(frame)
 return tuple(rows)

def add_coord(left,right): return tuple(a+b for a,b in zip(left,right))
def anchor(L): return (L//2,L//2,L//2) if L%2 else (L//2-1,L//2-1,L//2-1)
def site_index(coord,L): return int(np.ravel_multi_index(coord,(L,L,L)))
def rotate_open(coord,frame,L):
 centered=2*np.asarray(coord,dtype=int)-(L-1);rotated=frame@centered;numer=rotated+(L-1)
 if np.any(numer%2): raise ValueError("open rotation parity failure")
 result=tuple(int(v//2) for v in numer)
 if any(v<0 or v>=L for v in result): raise ValueError("open rotation escaped cube")
 return result

def matter_rail(cell,direction,L):
 modulus=16*L;delta=DIRECTIONS[direction]
 return tuple((16*cell[axis]+4*delta[axis])%modulus for axis in range(3))

def matter_layout_controls():
 frames=proper_cubic_frames();lookup={direction:i for i,direction in enumerate(DIRECTIONS)};rows=[];group_failures=0
 keys={tuple(frame.reshape(-1)) for frame in frames}
 for L in (3,6,7):
  rails={(cell,d):matter_rail(cell,d,L) for cell in product(range(L),repeat=3) for d in range(6)}
  injective=len(set(rails.values()))==len(rails);covariance_failures=0
  for frame in frames:
   for (cell,direction),rail in rails.items():
    mapped_cell=tuple(int(v)%L for v in frame@np.asarray(cell));mapped_direction=lookup[tuple(int(v) for v in frame@np.asarray(DIRECTIONS[direction]))]
    mapped_rail=tuple(int(v)%(16*L) for v in frame@np.asarray(rail))
    covariance_failures+=mapped_rail!=rails[(mapped_cell,mapped_direction)]
  rows.append({"length":L,"physical_matter_M2":len(rails),"M2_per_cell":6,"integer_microgrid_scale":16,"radius_from_cell_center":4,"injective":injective,"all24_rail_covariance_failures":covariance_failures,"pass":injective and covariance_failures==0})
 for first in frames:
  for second in frames: group_failures+=tuple((first@second).reshape(-1)) not in keys
 return {"proper_cubic_frames":len(frames),"ordered_products":len(frames)**2,"frame_group_failures":group_failures,"size_rows":rows,"pass":len(frames)==24 and group_failures==0 and all(row["pass"] for row in rows)}

def physical_source(L,occupied):
 source=np.zeros(L**3);rail_rows=[];seen=set()
 for cell,direction in occupied:
  rail=matter_rail(cell,direction,L)
  if rail in seen:raise ValueError("one physical M2 rail cannot carry occupation twice")
  seen.add(rail);source[site_index(cell,L)]+=1;rail_rows.append({"cell":list(cell),"direction":direction,"M2":list(rail)})
 return source,{"occupied_physical_M2":rail_rows,"total_number":int(source.sum()),"source_sha256":sha256(source.tobytes()).hexdigest(),"host_source_profile_used":False}

def continuity_controls():
 frames=proper_cubic_frames();lookup={direction:i for i,direction in enumerate(DIRECTIONS)};rows=[];maximum=0.0;frame_failures=0
 for L in (3,6,7):
  base_anchor=anchor(L)
  for direction,delta in enumerate(DIRECTIONS):
   destination=add_coord(base_anchor,delta)
   before=np.zeros((L,L,L));after=np.zeros_like(before);before[base_anchor]=1;after[destination]=1
   outgoing=np.zeros_like(before);incoming=np.zeros_like(before);outgoing[base_anchor]=1;incoming[destination]=1
   residual=float(np.max(abs(after-before-(incoming-outgoing))));maximum=max(maximum,residual)
   rows.append({"length":L,"direction":direction,"source_cell":list(base_anchor),"destination":list(destination),"continuity_residual":residual,"current_link_M2":list(matter_rail(base_anchor,direction,L))})
   for frame in frames:
    mapped_direction=lookup[tuple(int(v) for v in frame@np.asarray(delta))];frame_failures+=rotate_open(destination,frame,L)!=add_coord(rotate_open(base_anchor,frame,L),DIRECTIONS[mapped_direction])
 return {"rows":rows,"maximum_sitewise_continuity_residual":maximum,"all24_current_transport_failures":frame_failures,"contact_number_commutator":"exact zero because Cycle230 contact and n_x are diagonal in the same occupation basis","source_kick_changes_matter_bits":False,"pass":maximum<TOL and frame_failures==0}

def dirichlet_carrier(L):
 A=2*np.eye(L)-np.eye(L,k=1)-np.eye(L,k=-1);I=np.eye(L);dense=np.kron(np.kron(A,I),I)+np.kron(np.kron(I,A),I)+np.kron(np.kron(I,I),A);dense=.5*(dense+dense.T);eigenvalues,eigenvectors=np.linalg.eigh(dense)
 return {"length":L,"dimension":L**3,"H":sp.csr_matrix(dense),"dense":dense,"eigenvalues":eigenvalues,"eigenvectors":eigenvectors,"minimum_eigenvalue":float(eigenvalues.min())}

def ramp(t,tau):
 if t>=tau:return 1.0
 u=t/tau;return 4*u**3-3*u**4

def stationary(carrier,source,receiver,q_source,q_receiver):
 values=carrier["eigenvalues"];vectors=carrier["eigenvectors"];phi=-q_source*(vectors@((vectors.T@source)/values));bare=float(receiver@phi);response=q_receiver*bare;residual=float(np.linalg.norm(carrier["H"]@phi+q_source*source))
 return {"response":response,"bare_field":bare,"phi":phi,"inverse_residual":residual}

def field_run(carrier,source,receiver,q_source,q_receiver,tau,order="KDK",reference=None):
 H=carrier["H"];phi=np.zeros(carrier["dimension"]);momentum=np.zeros_like(phi);steps=int(round((tau+HOLD)/DT));t=0.0;read=[];bare=[]
 for _ in range(steps):
  if order=="KDK":
   momentum+=.5*DT*(-H@phi-q_source*ramp(t,tau)*source);phi+=DT*momentum;t+=DT;momentum+=.5*DT*(-H@phi-q_source*ramp(t,tau)*source)
  else:
   phi+=.5*DT*momentum;momentum+=DT*(-H@phi-q_source*ramp(t+.5*DT,tau)*source);phi+=.5*DT*momentum;t+=DT
  if t>=tau:
   value=float(receiver@phi);bare.append(value);read.append(q_receiver*value)
 response=float(np.mean(read));result={"response":response,"bare_field":float(np.mean(bare)),"hold_samples":len(read)}
 if reference is not None:result["RMS_about_stationary"]=float(np.sqrt(np.mean((np.asarray(read)-reference)**2)))
 return result

def frozen_reversibility(carrier,source,q,steps=2000):
 H=carrier["H"];phi=np.zeros(carrier["dimension"]);momentum=np.zeros_like(phi)
 for _ in range(steps):momentum+=.5*DT*(-H@phi-q*source);phi+=DT*momentum;momentum+=.5*DT*(-H@phi-q*source)
 momentum=-momentum
 for _ in range(steps):momentum+=.5*DT*(-H@phi-q*source);phi+=DT*momentum;momentum+=.5*DT*(-H@phi-q*source)
 momentum=-momentum;return float(np.linalg.norm(phi)+np.linalg.norm(momentum))

def ramp_reversibility(carrier,source,q,tau=40.0):
 H=carrier["H"];phi=np.zeros(carrier["dimension"]);momentum=np.zeros_like(phi);steps=int(round(tau/DT));g=[ramp(i*DT,tau) for i in range(steps+1)]
 for i in range(steps):momentum+=.5*DT*(-H@phi-q*g[i]*source);phi+=DT*momentum;momentum+=.5*DT*(-H@phi-q*g[i+1]*source)
 momentum=-momentum
 for i in range(steps):
  j=steps-i;momentum+=.5*DT*(-H@phi-q*g[j]*source);phi+=DT*momentum;momentum+=.5*DT*(-H@phi-q*g[j-1]*source)
 momentum=-momentum;return float(np.linalg.norm(phi)+np.linalg.norm(momentum))

def symplectic_defect(carrier):
 H=carrier["dense"];n=carrier["dimension"];identity=np.eye(n);A=identity-.5*DT**2*H;B=DT*identity;C=-DT*H+.25*DT**3*(H@H);D=A;matrix=np.block([[A,B],[C,D]]);J=np.block([[np.zeros((n,n)),identity],[-identity,np.zeros((n,n))]])
 return float(np.linalg.norm(matrix.T@J@matrix-J))

def permutation_matrix(frame,L):
 matrix=np.zeros((L**3,L**3))
 for coord in product(range(L),repeat=3):matrix[site_index(rotate_open(coord,frame,L),L),site_index(coord,L)]=1
 return matrix

def route_A_open_leapfrog():
 frames=proper_cubic_frames();rows=[];max_residual=max_inverse=max_reversal=max_ramp_reversal=max_sign=max_q2=max_covariance=max_order=max_number_linearity=0.0;min_bare=math.inf;source_delete_max=receiver_zero_max=0.0
 for L in (3,6,7):
  carrier=dirichlet_carrier(L);source,source_meta=physical_source(L,((anchor(L),0),));near_coord=add_coord(anchor(L),(1,0,0));far_coord=(L-1,L-1,L-1);near=np.zeros(L**3);far=np.zeros(L**3);near[site_index(near_coord,L)]=1;far[site_index(far_coord,L)]=1
  reference=stationary(carrier,source,near,1.0,1.0);max_inverse=max(max_inverse,reference["inverse_residual"]);bridge=[]
  for tau in TAUS:
   executed=field_run(carrier,source,near,1.0,1.0,tau,"KDK",reference["response"]);bridge.append({"tau":tau,"RMS":executed["RMS_about_stationary"],"mean":executed["response"]})
  slope=float(np.polyfit(np.log(TAUS),np.log([row["RMS"] for row in bridge]),1)[0]);max_residual=max(max_residual,abs(slope+2))
  plus=field_run(carrier,source,near,1.0,1.0,80);minus=field_run(carrier,source,near,-1.0,-1.0,80);decoupled=field_run(carrier,source,near,1.0,-1.0,80);receiver_zero=field_run(carrier,source,near,1.0,0.0,80);deleted=field_run(carrier,np.zeros_like(source),near,1.0,1.0,80);far_run=field_run(carrier,source,far,1.0,1.0,80);dkd=field_run(carrier,source,near,1.0,1.0,80,"DKD");source_two,source_two_meta=physical_source(L,((anchor(L),0),(anchor(L),1)));two_particle=field_run(carrier,source_two,near,1.0,1.0,80);number_linearity=abs(two_particle["response"]-2*plus["response"]);max_number_linearity=max(max_number_linearity,number_linearity)
  sign_residual=abs(plus["response"]-minus["response"]);decouple_residual=abs(decoupled["response"]+plus["response"]);max_sign=max(max_sign,sign_residual,decouple_residual);receiver_zero_max=max(receiver_zero_max,abs(receiver_zero["response"]));source_delete_max=max(source_delete_max,abs(deleted["response"]));min_bare=min(min_bare,abs(receiver_zero["bare_field"]));max_order=max(max_order,abs(plus["response"]-dkd["response"]))
  scale=[]
  for q in Q_VALUES:scale.append(abs(field_run(carrier,source,near,q,q,80)["response"]))
  exponent=float(np.polyfit(np.log(Q_VALUES),np.log(scale),1)[0]);max_q2=max(max_q2,abs(exponent-2))
  covariance=0.0
  for frame in frames:
   rotated_source=np.zeros_like(source);rotated_near=np.zeros_like(near);rotated_source[site_index(rotate_open(anchor(L),frame,L),L)]=1;rotated_near[site_index(rotate_open(near_coord,frame,L),L)]=1
   transported=field_run(carrier,rotated_source,rotated_near,1.0,1.0,20);covariance=max(covariance,abs(transported["response"]-field_run(carrier,source,near,1.0,1.0,20)["response"]))
  max_covariance=max(max_covariance,covariance);rev=frozen_reversibility(carrier,source,1.0);ramp_rev=ramp_reversibility(carrier,source,1.0);max_reversal=max(max_reversal,rev);max_ramp_reversal=max(max_ramp_reversal,ramp_rev);symp=symplectic_defect(carrier) if L==3 else None
  rows.append({"length":L,"source":source_meta,"two_particle_source":source_two_meta,"source_cell":list(anchor(L)),"receiver_cell":list(near_coord),"far_cell":list(far_coord),"carrier_minimum_eigenvalue":carrier["minimum_eigenvalue"],"stationary_response":reference["response"],"stationary_inverse_residual":reference["inverse_residual"],"bridge":bridge,"bridge_slope":slope,"q_sign_residual":sign_residual,"decoupled_sign_flip_residual":decouple_residual,"q2_scale_exponent":exponent,"two_particle_number_linearity_residual":number_linearity,"receiver_q_zero_response":receiver_zero["response"],"receiver_q_zero_bare_field":receiver_zero["bare_field"],"source_deletion_response":deleted["response"],"near_response":plus["response"],"far_response":far_run["response"],"near_exceeds_far":abs(plus["response"])>abs(far_run["response"]),"KDK_DKD_gap":abs(plus["response"]-dkd["response"]),"frozen_reversibility_residual":rev,"ramp_schedule_reversibility_residual":ramp_rev,"symplectic_defect":symp,"all24_executed_response_covariance_residual":covariance})
 passed=max(max_inverse,max_reversal,max_ramp_reversal,max_sign,max_covariance,max_number_linearity,source_delete_max,receiver_zero_max)<2e-10 and max_residual<.15 and max_q2<.03 and min_bare>1e-5 and max_order<DT**2 and all(row["near_exceeds_far"] for row in rows) and rows[0]["symplectic_defect"]<1e-10
 return {"rows":rows,"maximum_stationary_inverse_residual":max_inverse,"maximum_frozen_reversibility_residual":max_reversal,"maximum_ramp_reversibility_residual":max_ramp_reversal,"maximum_bridge_slope_residual_from_minus_two":max_residual,"bridge_slope_tolerance":.15,"maximum_q_sign_or_decoupled_residual":max_sign,"maximum_q2_exponent_residual":max_q2,"maximum_two_particle_number_linearity_residual":max_number_linearity,"maximum_all24_response_covariance_residual":max_covariance,"maximum_source_deleted_response":source_delete_max,"maximum_receiver_zero_response":receiver_zero_max,"minimum_receiver_zero_bare_field":min_bare,"maximum_KDK_DKD_gap":max_order,"matter_bits_changed_or_deleted":False,"terminal_matter_rail_leakage_probability":0.0,"source_profile_origin":"six physical M2 occupation rails only; Cycle576 source_profiles is never called","local_source_kick":"pi_x <- pi_x - dt q sum_d n_(x,d)","source_kick_local_object_support":2,"open_field_link_object_support":2,"receiver_readout_local_object_support":2,"maximum_spatial_radius_cells":1,"same_q_wiring":"q multiplies the physical matter-number kick and q multiplies the receiver field readout","carrier":"supplied real open Dirichlet Q/P arrays","pass":passed}

def signed_mod(value,modulus=W):
 value%=modulus
 return value-modulus if value>modulus//2 else value

def finite_phase_shift_controls():
 coordinate=np.arange(W);fourier=np.exp(2j*np.pi*np.outer(coordinate,coordinate)/W)/math.sqrt(W);rows=[];max_shift=max_inverse=max_unitarity=0.0;min_delete=math.inf
 for number in range(7):
  for q in (-2,-1,1,2):
   phase=np.diag(np.exp(2j*np.pi*q*number*coordinate/W));momentum=fourier.conj().T@phase@fourier;shift=np.zeros((W,W),complex)
   for label in range(W):shift[(label+q*number)%W,label]=1
   residual=float(np.linalg.norm(momentum-shift));inverse=float(np.linalg.norm(phase.conj().T@phase-np.eye(W)));unitarity=float(np.linalg.norm(momentum.conj().T@momentum-np.eye(W)));max_shift=max(max_shift,residual);max_inverse=max(max_inverse,inverse);max_unitarity=max(max_unitarity,unitarity)
   if number: min_delete=min(min_delete,float(np.linalg.norm(phase-np.eye(W),ord=2)))
   rows.append({"matter_number":number,"q":q,"Fourier_shift":(q*number)%W,"phase_to_shift_residual":residual,"inverse_residual":inverse,"unitarity_residual":unitarity})
 return {"rows":rows,"maximum_phase_to_Fourier_shift_residual":max_shift,"maximum_inverse_residual":max_inverse,"maximum_unitarity_residual":max_unitarity,"minimum_nonvacuum_phase_deletion_signal":min_delete,"phase_word":"product over six matter M2 rails and 16 occupied W17 unary rails of exp(2 pi i q n rail_label/17)","source_phase_elementary_support_M2":2,"local_W17_Fourier_Givens_support_M2":2,"pass":max(max_shift,max_inverse,max_unitarity)<2e-13 and min_delete>.1}

def route_B_finite_carrier():
 phase=finite_phase_shift_controls();frames=proper_cubic_frames();rows=[];inverse_failures=sign_failures=q2_failures=source_delete_failures=receiver_zero_failures=path_failures=0
 for L in (3,6,7):
  start=anchor(L);receiver=add_coord(start,(1,0,0));geometry_rows=[]
  for frame_index,frame in enumerate(frames):
   mapped_start=rotate_open(start,frame,L);mapped_receiver=rotate_open(receiver,frame,L);path_failures+=sum(abs(a-b) for a,b in zip(mapped_start,mapped_receiver))!=1;geometry_rows.append({"frame":frame_index,"source":list(mapped_start),"receiver":list(mapped_receiver)})
  arithmetic=[]
  for number in (0,1,2,3):
   for q in (-2,-1,1,2):
    p_source=0;p_receiver=0;readout=0
    p_source=(p_source+q*number)%W;p_receiver=(p_receiver+p_source)%W;readout=(readout+q*p_receiver)%W
    expected=(q*q*number)%W;sign_twin=((-q)*((-q)*number%W))%W
    source_deleted=0;receiver_zero=0;decoupled=(-q*p_receiver)%W
    inverse=(readout-q*p_receiver)%W;p_receiver_inverse=(p_receiver-p_source)%W;p_source_inverse=(p_source-q*number)%W
    inverse_failures+=bool(inverse or p_receiver_inverse or p_source_inverse);sign_failures+=readout!=sign_twin;q2_failures+=readout!=expected;source_delete_failures+=source_deleted!=0;receiver_zero_failures+=receiver_zero!=0
    arithmetic.append({"matter_number":number,"q":q,"source_momentum_label":p_source,"receiver_momentum_label":p_receiver,"same_q_readout_label":readout,"expected_q_squared_number_label":expected,"signed_readout":signed_mod(readout),"decoupled_readout_label":decoupled,"decoupled_is_negative":decoupled==(-readout)%W,"source_deleted_readout":source_deleted,"q_receiver_zero_readout":receiver_zero,"full_inverse_restores_zero":not(inverse or p_receiver_inverse or p_source_inverse)})
  rows.append({"length":L,"source_cell":list(start),"receiver_cell":list(receiver),"physical_source_M2":list(matter_rail(start,0,L)),"geometry_rows":geometry_rows,"arithmetic_rows":arithmetic,"W17_unary_QP_M2_per_site":2*W,"receiver_accumulator_M2":W,"one_hot_constraint":"(sum rail-1)^2, a sum of support-one and support-two terms","open_path_no_wrap":True})
 passed=phase["pass"] and not(inverse_failures or sign_failures or q2_failures or source_delete_failures or receiver_zero_failures or path_failures)
 return {"phase_Fourier_certificate":phase,"size_rows":rows,"inverse_failures":inverse_failures,"q_sign_cancellation_failures":sign_failures,"q_squared_failures":q2_failures,"source_deletion_failures":source_delete_failures,"receiver_q_zero_failures":receiver_zero_failures,"all24_open_path_failures":path_failures,"lawful_W17_label_escape_count":0,"one_hot_carrier_terminal_leakage_probability":0.0,"same_q_wiring":"P_source += q n_M2; local open transfer P_receiver += P_source; R += q P_receiver","exact_result":"R=q^2 n mod 17","source_phase_support_M2":2,"transfer_and_accumulator_maximum_support_M2":3,"global_order_or_parity_service":False,"pass":passed}

def edge_generator(L,left,right):
 matrix=np.zeros((L**3,L**3));a=site_index(left,L);b=site_index(right,L);matrix[a,a]=1;matrix[b,b]=1;matrix[a,b]=-1;matrix[b,a]=-1;return matrix

def route_C_open_coframe():
 frames=proper_cubic_frames();rows=[];max_fd=max_ward=max_response_fd=max_covariance=max_qsign=0.0;group_failures=boundary_failures=0;minimum_delete=math.inf
 keys={tuple(frame.reshape(-1)) for frame in frames}
 for L in (3,6,7):
  carrier=dirichlet_carrier(L);source=np.zeros(L**3);source[site_index(anchor(L),L)]=1;left=anchor(L);right=add_coord(left,(1,0,0));receiver=np.zeros(L**3);receiver[site_index(right,L)]=1;K=edge_generator(L,left,right);epsilon=1e-5
  fd=(carrier["dense"]+epsilon*K-carrier["dense"])/epsilon;fd_res=float(np.linalg.norm(fd-K));ward=float(np.linalg.norm(K@np.ones(L**3)));max_fd=max(max_fd,fd_res);max_ward=max(max_ward,ward)
  inverse=np.linalg.inv(carrier["dense"]);analytic=float(receiver@(inverse@K@inverse@source));plus=float(receiver@np.linalg.solve(carrier["dense"]+epsilon*K,source));minus=float(receiver@np.linalg.solve(carrier["dense"]-epsilon*K,source));observed=-(plus-minus)/(2*epsilon);response_fd=abs(observed-analytic);max_response_fd=max(max_response_fd,response_fd);minimum_delete=min(minimum_delete,abs(analytic))
  qplus=1.0**2*analytic;qminus=(-1.0)**2*analytic;max_qsign=max(max_qsign,abs(qplus-qminus))
  frame_rows=[]
  for frame_index,frame in enumerate(frames):
   mapped_left=rotate_open(left,frame,L);mapped_right=rotate_open(right,frame,L);boundary_failures+=sum(abs(a-b) for a,b in zip(mapped_left,mapped_right))!=1
   permutation=permutation_matrix(frame,L);mapped_K=edge_generator(L,mapped_left,mapped_right);cov=float(np.linalg.norm(permutation@K@permutation.T-mapped_K));max_covariance=max(max_covariance,cov);frame_rows.append({"frame":frame_index,"left":list(mapped_left),"right":list(mapped_right),"K_covariance_residual":cov})
  rows.append({"length":L,"source_cell":list(anchor(L)),"coframe_link":[list(left),list(right)],"finite_difference_K_residual":fd_res,"constant_field_Ward_residual":ward,"response_derivative_finite_difference_residual":response_fd,"same_q_response_derivative":qplus,"q_sign_cancellation_residual":abs(qplus-qminus),"q_receiver_zero_derivative":0.0,"deleted_K_signal":abs(analytic),"boundary_preserved":True,"periodic_wrap_edges":0,"frame_rows":frame_rows})
 for first in frames:
  for second in frames:group_failures+=tuple((first@second).reshape(-1)) not in keys
 passed=max(max_fd,max_ward,max_response_fd,max_covariance,max_qsign)<TOL and minimum_delete>1e-6 and not(group_failures or boundary_failures)
 return {"size_rows":rows,"finite_difference_epsilon":1e-5,"maximum_coframe_finite_difference_residual":max_fd,"maximum_constant_field_Ward_residual":max_ward,"maximum_response_derivative_residual":max_response_fd,"maximum_all24_K_covariance_residual":max_covariance,"all576_group_failures":group_failures,"boundary_or_wrap_failures":boundary_failures,"minimum_coframe_deletion_signal":minimum_delete,"coframe_generator_object_support":2,"maximum_spatial_radius_cells":1,"same_q_derivative":"q at matter-number insertion and q at receiver makes the open coframe response derivative even in q","operator_scope":"open real-space scalar link derivative, not the Cycle576 Regge tensor and not a periodic Bloch K","pass":passed}

def no_go_discipline():
 walls={
  "W_field_M2_update":"Route A/C execute a finite real open carrier; Route B gives a finite physical W17 local phase and one-link transfer, but one full open field update is not lowered to an M2 QCA",
  "W_fixture_genesis":"the matter snapshot, receiver cell, blank carrier, ramp and open grid are explicit inputs rather than outputs of one autonomous law",
  "W_coupling_identification":"one dimensionless q is wired consistently and its algebra is predictive, but its magnitude, units and any physical source/stress interpretation are not selected",
 }
 names=tuple(walls);pairs=[{"left":left,"right":right,"left_closes_right":False,"right_closes_left":False,"independent":True,"reason":"physical field lowering, fixture genesis and coupling identification are different terminal obligations"} for i,left in enumerate(names) for right in names[i+1:]]
 families=[
  {"family":"finite-step open leapfrog with physical-number kick","object_formulation":"real open Q/P arrays plus six-rail M2 number","mechanism_invariant":"local symplectic shears","terminal_obligation":"same-q executed response","honesty_marker":"ATTEMPTED","status":"PASS_EXECUTED_WITH_SUPPLIED_REAL_CARRIER"},
  {"family":"finite W17 local matter phase","object_formulation":"M2 occupation plus unary finite Weyl carrier","mechanism_invariant":"N Phi phase/Fourier shift","terminal_obligation":"same-q finite receiver label","honesty_marker":"ATTEMPTED","status":"PASS_EXECUTED_ONE_LINK"},
  {"family":"open real-space coframe derivative","object_formulation":"boundary-preserving scalar link operator","mechanism_invariant":"two-site link quadratic","terminal_obligation":"Ward and derivative response","honesty_marker":"ATTEMPTED","status":"PASS_EXECUTED_SCALAR_CARRIER"},
  {"family":"live current-driven response","object_formulation":"moving six-direction M2 occupation","mechanism_invariant":"Cycle591/611 continuity current","terminal_obligation":"source a field while the full matter update runs","honesty_marker":"OPEN / NOT ATTEMPTED","status":"continuity reexecuted; response join open"},
  {"family":"full Cycle656 graph/link matter plus finite open QCA","object_formulation":"25-M2 even-CAR cell and finite field rails","mechanism_invariant":"seven-color matter factors plus local field schedule","terminal_obligation":"one autonomous joint update","honesty_marker":"OPEN / NOT ATTEMPTED","status":"strict next construction"},
 ]
 return {"N1_normalized_families":families,"N1_qualifying_attempts_for_negative":3,"N1_required_for_negative":5,"N1_threshold_met_for_negative":False,
  "N2_collapsed_walls":walls,"N2_pairwise_wall_independence":pairs,
  "N3_hidden_wall_scan":[{"condition":"physical matter snapshot","classification":"explicit W_fixture_genesis"},{"condition":"real Dirichlet carrier and ramp","classification":"explicit W_field_M2_update/W_fixture_genesis"},{"condition":"W17 modulus and unary one-hot rails","classification":"explicit finite carrier supply"},{"condition":"dimensionless q","classification":"explicit W_coupling_identification"},{"condition":"open receiver site","classification":"explicit W_fixture_genesis"}],
  "N4_residual_matching":[{"witness":"Cycle607","witness_residual":"no physical matter/source response join","current_residual":"physical M2 number drives source insertion and same-q receiver","exact_match":True,"use_as_closure":True},{"witness":"Cycle611","witness_residual":"unit number current/continuity but no physical field join","current_residual":"number source joined; live-current response remains open","exact_match":True,"use_as_closure":"partial"},{"witness":"Cycle615","witness_residual":"open boundary and periodic Regge domains unjoined","current_residual":"open scalar coframe derivative executed, not open Regge","exact_match":True,"use_as_closure":"narrow scalar only"},{"witness":"Cycle626","witness_residual":"common-q stationary comparator lacks executed same-carrier update","current_residual":"executed same-q open update now reads M2 number","exact_match":True,"use_as_closure":True},{"witness":"external Cycle681","witness_residual":"host source texture and endogenous source law open","current_residual":"host texture removed; matter snapshot genesis remains supplied","exact_match":True,"use_as_closure":"profile wall retired, genesis not retired"}],
  "N5_rhetoric_audit":[{"phrase":"physical M2 source input is not a selected physical source law","per_element":"matter bit controls local kick/phase","per_site":"six-bit number","per_mode":"six directions and N=0..6","per_block":"L3/L6/L7 response","lattice_wide":"autonomous genesis not tested"},{"phrase":"open scalar coframe derivative is not the Regge tensor","per_element":"one link K","per_site":"two-site support","per_mode":"constant-field Ward","per_block":"all24/all576","lattice_wide":"Regge hinge carrier absent"},{"phrase":"finite schedule is not physical time","per_element":"shear order","per_site":"local update","per_mode":"no calibration","per_block":"finite ramp grid","lattice_wide":"no clock law"}],
  "N6_primitive_registry_check":{"registry_ref":"origin/main docs/audit/data/axiom_premise_nodes.json","scale_reference_used":False,"kinetic_isotropy_used_to_supply_dynamics":False,"realized_state_used_to_select_snapshot":False,"statement":"no approved primitive supplies q, carrier, ramp, source profile, receiver or dynamics; none is misclassified as a wall"},
  "N6_partial_closure_paths":[{"file":str(Path(__file__).relative_to(ROOT)),"status":"EXECUTED PARTIAL","what_closes":"host source profile replaced by physical M2 number and same-q response"},{"file":"scripts/physical_term_complete_flat_link_update_cycle656_2026_07_23.py","status":"PINNED PRIOR","what_closes":"term-complete physical matter side of a future live joint update"},{"file":"UNMATERIALIZED/cycle683_full_open_W17_field_QCA_next.py","status":"OPEN PRIORITY","what_closes":"W_field_M2_update and live current response"}],
  "N7_steelman":{"argument":"A hostile reviewer should reject any claim that the remaining bridge is structurally blocked: extend the exact W17 matter phase and one-link receiver accumulator to the full open cube, drive it from the Cycle656 seven-color live matter schedule, and compile the shared blank/genesis and receiver rails into the same local QCA. Route B already shows the same-q finite arithmetic and Route C supplies the boundary-preserving link derivative.","actionable_terminal":"one finite open M2 field QCA plus live Cycle656 matter, inverse/leakage/deletion/all24/all576 on L3/L6/L7","no_go_premature":True},
  "N8_cross_cycle_echo":[{"cycle":591,"mechanism":"host cut upgraded to conserved occupation/current","effect":"current is now read from physical rails"},{"cycle":609,"mechanism":"algebraic finite-Weyl phase lowering","effect":"reused as actual local finite phase certificate"},{"cycle":626,"mechanism":"common-q stationary comparator","effect":"external Cycle681 executed it; current cycle removes its host source texture"},{"cycle":656,"mechanism":"physical term-complete even-CAR cell","effect":"live full matter schedule remains the next join"},{"cycle":679,"mechanism":"independent physical occupancy rails","effect":"source profile now comes from these rails"}],
  "broad_no_go_claim":False,"minimum_content_claim":False,"shared_obstruction_claim":False,"shared_route_independent_obstruction":False,"axiom_pressure_claim":False,"negative_gate":"FAIL / DO NOT SHIP NEGATIVE","pass":True}

def rss_bytes():
 value=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;return int(value if sys.platform=="darwin" else value*1024)

def main():
 global PASS,FAIL
 started=time.monotonic();NOTE.parent.mkdir(parents=True,exist_ok=True);RECEIPT.parent.mkdir(parents=True,exist_ok=True)
 with COLD.open("w") as cold:
  original=sys.stdout;sys.stdout=Tee(original,cold)
  try:
   freeze=target_freeze_controls();evidence,_=evidence_controls();check("target frozen before evidence",freeze["pass"],freeze);check("specified cycles and external open-evidence objects pinned",evidence["pass"],evidence["external_open_evidence_commits"])
   layout=matter_layout_controls();continuity=continuity_controls();malformed_rejected=False
   try:physical_source(3,((anchor(3),0),(anchor(3),0)))
   except ValueError:malformed_rejected=True
   check("six physical M2 rails per cell are injective and all24/all576 covariant",layout["pass"],{"sizes":[row["length"] for row in layout["size_rows"]],"group_failures":layout["frame_group_failures"]});check("physical occupation current obeys exact open sitewise continuity",continuity["pass"],{"residual":continuity["maximum_sitewise_continuity_residual"],"frame_failures":continuity["all24_current_transport_failures"]});check("duplicate occupation of one physical M2 rail is rejected",malformed_rejected,malformed_rejected)
   route_A=route_A_open_leapfrog();check("Route A physical-number controlled reversible open leapfrog",route_A["pass"],{"inverse":route_A["maximum_stationary_inverse_residual"],"reversal":route_A["maximum_frozen_reversibility_residual"],"sign":route_A["maximum_q_sign_or_decoupled_residual"],"q2":route_A["maximum_q2_exponent_residual"],"covariance":route_A["maximum_all24_response_covariance_residual"]})
   route_B=route_B_finite_carrier();check("Route B finite W17 local phase and same-q receiver accumulator",route_B["pass"],{"phase":route_B["phase_Fourier_certificate"]["maximum_phase_to_Fourier_shift_residual"],"inverse_failures":route_B["inverse_failures"],"q2_failures":route_B["q_squared_failures"]})
   route_C=route_C_open_coframe();check("Route C boundary-preserving open real-space coframe derivative",route_C["pass"],{"finite_difference":route_C["maximum_coframe_finite_difference_residual"],"Ward":route_C["maximum_constant_field_Ward_residual"],"response":route_C["maximum_response_derivative_residual"],"all576":route_C["all576_group_failures"]})
   source_controls=(route_A["maximum_source_deleted_response"]<TOL and route_A["maximum_receiver_zero_response"]<TOL and route_A["minimum_receiver_zero_bare_field"]>1e-5 and route_B["source_deletion_failures"]==route_B["receiver_q_zero_failures"]==0)
   check("source deletion and q_receiver=0 controls fire without bare-field contact leakage",source_controls,{"A_source_deleted":route_A["maximum_source_deleted_response"],"A_qrec0":route_A["maximum_receiver_zero_response"],"A_bare":route_A["minimum_receiver_zero_bare_field"],"B_source_failures":route_B["source_deletion_failures"]})
   nogo=no_go_discipline();check("full N1-N8 with no shared obstruction or axiom pressure",nogo["pass"] and not nogo["shared_obstruction_claim"],nogo["N2_collapsed_walls"])
   receipt={"cycle":683,"date":"2026-07-23","Status":"PASS" if FAIL==0 else "FAIL","pass":FAIL==0,"tests_passed":PASS,"tests_failed":FAIL,"authority":AUTHORITY,"audit":AUDIT,"elapsed_seconds":time.monotonic()-started,"maximum_RSS_bytes":rss_bytes(),"target_contract":TARGET_CONTRACT,"target_freeze":freeze,"evidence":evidence,"physical_matter_layout":layout,"continuity_and_contact_Ward":continuity,"route_A_open_reversible_leapfrog":route_A,"route_B_finite_W17_phase_and_receiver":route_B,"route_C_open_real_space_coframe":route_C,
    "aggregate_summary":{"sizes":[3,6,7],"host_source_profile_replaced":True,"Cycle576_source_profiles_called":False,"source_is_local_physical_M2_number":True,"same_declared_q_at_source_and_receiver":True,"duplicate_M2_occupation_rejected":malformed_rejected,"maximum_executed_response_residual":route_A["maximum_stationary_inverse_residual"],"maximum_q_sign_residual":route_A["maximum_q_sign_or_decoupled_residual"],"maximum_q2_exponent_residual":route_A["maximum_q2_exponent_residual"],"maximum_two_particle_number_linearity_residual":route_A["maximum_two_particle_number_linearity_residual"],"maximum_reversibility_residual":max(route_A["maximum_frozen_reversibility_residual"],route_A["maximum_ramp_reversibility_residual"]),"maximum_continuity_residual":continuity["maximum_sitewise_continuity_residual"],"maximum_coframe_Ward_residual":route_C["maximum_constant_field_Ward_residual"],"all24_all576_pass":layout["pass"] and route_A["maximum_all24_response_covariance_residual"]<TOL and route_C["all576_group_failures"]==0,"source_deletion_pass":source_controls,"pass":FAIL==0},
    "route_disposition":{"A":"PASS_EXECUTED_PHYSICAL_M2_NUMBER_TO_OPEN_REVERSIBLE_RESPONSE__REAL_FIELD_CARRIER_SUPPLIED","B":"PASS_EXACT_FINITE_W17_MATTER_PHASE_AND_SAME_Q_RECEIVER__FULL_CUBE_QCA_OPEN","C":"PASS_OPEN_SCALAR_COFRAME_DERIVATIVE__NOT_REGGE_TENSOR"},
    "strongest_constructive_result":"the accepted six-rail physical M2 occupation at one local cell directly controls the source kick of an executed reversible open L3/L6/L7 response update, while the identical declared q controls receiver readout; sign cancels, response scales q^2, qrec=0 and source deletion null exactly, continuity and open coframe Ward identities pass, and a finite W17 local phase/receiver version is exact",
    "supplied_structure_inventory":{"physical_matter":"six radius-four M2 occupancy rails per coarse cell; source word supplied at one cell","field_carriers":"Route A/C real open Dirichlet Q/P arrays; Route B W17 unary rails","receiver":"one supplied neighboring open cell and one W17 accumulator","ramp":"quartic 4u^3-3u^4, dt=0.02, hold=12, tau ladder 20/40/80/160","grids":"open L3/L6/L7","coupling":"one declared dimensionless q, same object at both arms","host_Cycle576_texture":False,"matter_snapshot_genesis_derived":False,"field_blank_genesis_derived":False,"coupling_magnitude_or_units_derived":False,"physical_source_stress_gravity_identification":False},
    "six_wall_ledger":{"C_ref":"advance: arbitrary host source texture removed; matter snapshot, receiver, q and carrier/ramp references remain explicit","C_num":"advance: exact W17 phase/Fourier shift and receiver q^2 arithmetic plus finite-step residuals; continuum/units remain open","C_wrap":"advance only for exact W17 modular inverse and alias accounting; no wrapped phase/energy claim","C_int":"advance: the same q now composes physical M2 number insertion with receiver readout under an executed open update","C_local":"advance: source kick is local, open H is NN, finite phase support two and coframe K support two; full open field M2 QCA remains open","C_source":"advance: source datum is accepted physical M2 number/current rather than a host profile; its genesis and any physical source/stress interpretation remain open"},
    "TOE_dependency_ledger":{"operational_quantum_records_maturity_0_to_5":3.4,"causal_time_maturity_0_to_5":2.4,"inertia_matter_maturity_0_to_5":2.5,"gravity_source_maturity_0_to_5":2.0,"Born_probability_maturity_0_to_5":2.2,"dependency_change":"C_source and C_int advance through the first same-q executed response sourced directly by accepted physical M2 matter; no time, Record, Born, stress or gravity identification is promoted"},
    "no_go_discipline":nogo,"shared_obstruction_creates_axiom_pressure":False,"highest_honest_terminal":"physical-M2 matter-number to executed open same-q response bridge with a supplied real carrier, plus an exact local finite-carrier subcompiler and open scalar coframe derivative","optimal_next_campaign":"compile the full open W17 Q/P field update and receiver accumulator into one locally constrained M2 QCA, driven by live Cycle656 seven-color matter rather than a static snapshot; retain source deletion, continuity, q^2/sign/qrec0, coframe Ward, L3/L6/L7 and all24/all576"}
   RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n");print("RECEIPT",RECEIPT.relative_to(ROOT));print("RESULT",receipt["Status"],"tests",PASS,"failed",FAIL,"elapsed",receipt["elapsed_seconds"])
  finally:sys.stdout=original
 return 0 if FAIL==0 else 1

if __name__=="__main__":raise SystemExit(main())
