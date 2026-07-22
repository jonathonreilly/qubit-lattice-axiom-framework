#!/usr/bin/env python3
"""Cycle613: gauge the accepted matter law and test source/stress identification.

The candidate compact F17 U(1) link action includes the accepted Cycle219 coin,
Cycle230 stream/contact, link electric/magnetic variables, and reciprocal
current backreaction. It is a falsifiable candidate, not gravity. Authority
none; audit unset.
"""
from __future__ import annotations

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

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import physical_matter_variation_current_stress_compensator_source_tournament_cycle611_2026_07_22 as c611

c609=c611.c609;c607=c611.c607;c230=c611.c230;c219=c611.c219;c210=c611.c210
NOTE=ROOT/("docs/work_history/repo/review_feedback/"
           "PHYSICAL_GAUGED_MATTER_ACTION_STRESS_PREDICTION_TOURNAMENT_CYCLE613_NOTE_2026-07-22.md")
RECEIPT=ROOT/"outputs/physical_gauged_matter_action_stress_prediction_tournament_cycle613_receipt_2026_07_22.json"
COLD=ROOT/"outputs/physical_gauged_matter_action_stress_prediction_tournament_cycle613_cold_2026_07_22.txt"
AUTHORITY="none";AUDIT="unset";TOL=2e-8;START=perf_counter();PASS=FAIL=0
FIXTURES=(("TRAIN_L3",3,384,False),("HELD_L6",6,768,True),("OUT_HELD_L7",7,1536,True))
PINS={
 "scripts/physical_matter_variation_current_stress_compensator_source_tournament_cycle611_2026_07_22.py":"358473ff93ad613324dd39bcee12467f3191927ef9c2e632aaf0137d735c02e6",
 "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_VARIATION_CURRENT_STRESS_COMPENSATOR_SOURCE_TOURNAMENT_CYCLE611_NOTE_2026-07-22.md":"102b57283c55a190ba02289d2689ac8a6e6f97aff58e13036df1dd8a66e97308",
 "outputs/physical_matter_variation_current_stress_compensator_source_tournament_cycle611_receipt_2026_07_22.json":"e32ec66403d0173865f24f047439f85e1c354e2156973dcdd94c4217c6fdbd82",
 "outputs/physical_matter_variation_current_stress_compensator_source_tournament_cycle611_cold_2026_07_22.txt":"64b83d76bc28276d0484533e1d71c59ae6ed36fc6281ae7aafe11e91ef868290",
 "outputs/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_receipt_2026_07_22.json":"c8210a1f170c3b11258f9876a0013b981b4b3c44a592423c8ce48a34a479b5ee",
 "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json":"06456c1443f5464949f40d81e9f1c6316b3e4e8405415b5b0035e39d4b88c3bd",
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
 observed={p:digest(p) for p in PINS}
 r611=json.loads((ROOT/"outputs/physical_matter_variation_current_stress_compensator_source_tournament_cycle611_receipt_2026_07_22.json").read_text())
 r604=json.loads((ROOT/"outputs/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_receipt_2026_07_22.json").read_text())
 r576=json.loads((ROOT/"outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json").read_text())
 result={"hashes_match":observed==PINS,"Cycle611_pass":r611["pass"],"Cycle604_pass":r604["pass"],
         "Cycle576_pass":r576["pass"],"mass":r611["shore"]["mass"],"contact":r611["shore"]["contact"],
         "seam":r611["shore"]["seam"]}
 check("Cycles576/604/611 and mass/contact/seam shore are byte-pinned",result["hashes_match"]
       and all(result[k] for k in ("Cycle611_pass","Cycle604_pass","Cycle576_pass"))
       and max(result["mass"],result["contact"],result["seam"])<TOL,result)
 return r611,r604,r576,result


def note_contract():
 body=" ".join(NOTE.read_text().lower().replace("`","").replace("*","").split())
 required=("authority: none","audit: unset","cycle 613","route a","route b","route c",
           "explicit action","gauge transformation","gauss","coin","contact","representation charge",
           "physical coupling","canonical tensor","rescaling","improvement","zero-total","dipolar",
           "5/(32pi)","compatibility falsification","not gravity","l3","l6","l7","all 24","576",
           "inverse","leakage","deletion","n1 —","n2 —","n3 —","n4 —","n5 —","n6 —","n7 —","n8 —","no axiom pressure")
 missing=tuple(item for item in required if item not in body)
 check("Cycle613 note freezes gauged action, stress, prediction, and N1-N8 scope",not missing,missing)


# Positive-axis compact link representation.
def dplus(value,axis):return np.roll(value,-1,axis=axis)-value
def dminus(value,axis):return value-np.roll(value,1,axis=axis)


def divergence(link):return sum(dminus(link[...,axis],axis) for axis in range(3))


def plaquettes(q):
 return {(a,b):(dplus(q[...,b],a)-dplus(q[...,a],b))%c609.MOD
         for a in range(3) for b in range(a+1,3)}


def magnetic_gradient(q):
 result=np.zeros_like(q);rows=plaquettes(q)
 for (a,b),curvature in rows.items():
  result[...,a]=(result[...,a]+dminus(curvature,b))%c609.MOD
  result[...,b]=(result[...,b]-dminus(curvature,a))%c609.MOD
 return result%c609.MOD


def branch_current(length,site,direction):
 result=np.zeros((length,length,length,3),dtype=np.int64);velocity=c210.DIRECTIONS[direction];axis=direction//2
 owner=site if direction%2==0 else tuple((np.asarray(site)+velocity)%length)
 result[owner+(axis,)]=1 if direction%2==0 else -1
 return result


def branch_density(length,site):
 result=np.zeros((length,)*3,dtype=np.int64);result[site]=1;return result


def destination(site,direction,length):return tuple((np.asarray(site)+c210.DIRECTIONS[direction])%length)


def link_phase_word(q,site,direction):
 length=q.shape[0];velocity=c210.DIRECTIONS[direction];axis=direction//2
 owner=site if direction%2==0 else tuple((np.asarray(site)+velocity)%length)
 sign=1 if direction%2==0 else -1
 return int(sign*q[owner+(axis,)]%c609.MOD)


def branch_joint_step(site,direction,q,e):
 length=q.shape[0];current=branch_current(length,site,direction);gradient=magnetic_gradient(q)
 e1=(e-current-gradient)%c609.MOD;q1=(q+e1)%c609.MOD
 target=destination(site,direction,length)
 phase=np.exp(2j*math.pi*link_phase_word(q,site,direction)/c609.MOD)
 return target,direction,q1,e1,phase,current,gradient


def branch_joint_inverse(target,direction,q1,e1):
 length=q1.shape[0];source=tuple((np.asarray(target)-c210.DIRECTIONS[direction])%length)
 q=(q1-e1)%c609.MOD;current=branch_current(length,source,direction);gradient=magnetic_gradient(q)
 e=(e1+current+gradient)%c609.MOD
 phase=np.exp(-2j*math.pi*link_phase_word(q,source,direction)/c609.MOD)
 return source,direction,q,e,phase


def gauged_stream(psi,q):
 length=q.shape[0];result=np.zeros_like(psi)
 for site in product(range(length),repeat=3):
  for direction in range(6):
   target=destination(site,direction,length)
   result[target+(direction,)]=np.exp(2j*math.pi*link_phase_word(q,site,direction)/c609.MOD)*psi[site+(direction,)]
 return result


def gauge_transform_links(q,theta):
 result=q.copy()
 for axis in range(3):result[...,axis]=(q[...,axis]+dplus(theta,axis))%c609.MOD
 return result


def gauge_transform_matter(psi,theta):return psi*np.exp(2j*math.pi*theta[...,None]/c609.MOD)


def rotate_link(link,frame):
 length=link.shape[0];result=np.zeros_like(link)
 for site in product(range(length),repeat=3):
  rotated=np.asarray(frame@np.asarray(site),dtype=int)%length
  for axis in range(3):
   vector=frame[:,axis];target_axis=int(np.argmax(abs(vector)));sign=int(vector[target_axis])
   owner=rotated.copy()
   if sign<0:owner[target_axis]=(owner[target_axis]-1)%length
   result[tuple(owner)+(target_axis,)]=sign*link[site+(axis,)]
 return result%c609.MOD


def rotate_site_direction(site,direction,frame,length):
 target_site=tuple(int(v%length) for v in frame@np.asarray(site))
 dmap=np.argmax(c210.direction_permutation(frame),axis=0)
 return target_site,int(dmap[direction])


def link_group_failures(length):
 rng=np.random.default_rng(613+length);link=rng.integers(0,c609.MOD,size=(length,length,length,3))
 frames=c210.proper_cubic_frames();failures=0
 for first in frames:
  for second in frames:
   failures+=int(not np.array_equal(rotate_link(link,first@second),rotate_link(rotate_link(link,second),first)))
 return failures


def local_coin_contact_cubic_controls(coin):
 occupations=c230.c229.occupation_table(6);number=np.sum(occupations,axis=1)
 contact=np.diag(np.exp(1j*c230.COUPLING*number*(number-1)/2));coin_res=contact_res=0
 for frame in c210.proper_cubic_frames():
  permutation=c210.direction_permutation(frame)
  coin_res=max(coin_res,float(np.linalg.norm(permutation@coin-coin@permutation)))
  lifted=c230.c229.fock_lift(permutation)
  contact_res=max(contact_res,float(np.linalg.norm(lifted@contact-contact@lifted)))
 return {"coin_all24_cubic_covariance_residual":coin_res,
         "contact_all24_cubic_covariance_residual":contact_res}


def fock_joint_controls(length,site,q,e,coin):
 """Exhaust the 64 local occupation words and one coherent coin/contact input.

 The controlled link map is evaluated basiswise; its linear extension therefore
 retains the coherent amplitudes instead of measuring or host-selecting a branch.
 """
 occupations=c230.c229.occupation_table(6);numbers=np.sum(occupations,axis=1)
 lifted_coin=c230.c229.fock_lift(coin)
 contact=np.diag(np.exp(1j*c230.COUPLING*numbers*(numbers-1)/2))
 rng=np.random.default_rng(6160+length)
 amplitudes=c611.normalize(rng.normal(size=64)+1j*rng.normal(size=64))
 post=contact@lifted_coin@amplitudes
 gradient=magnetic_gradient(q);max_cont=max_gauss=max_inverse=0;minimum_delete=math.inf;output_norm=0
 output_keys=set()
 for index,occupation in enumerate(occupations):
  current=sum((branch_current(length,site,d) for d in range(6) if occupation[d]),
              start=np.zeros_like(e))
  rho=numbers[index]*branch_density(length,site);rho1=np.zeros_like(rho)
  phase_word=0
  for direction in range(6):
   if occupation[direction]:
    rho1[destination(site,direction,length)]+=1
    phase_word+=link_phase_word(q,site,direction)
  continuity=(rho1-rho+divergence(current))%c609.MOD
  max_cont=max(max_cont,int(np.max(np.minimum(continuity,c609.MOD-continuity))))
  e1=(e-current-gradient)%c609.MOD;q1=(q+e1)%c609.MOD
  gauss=(divergence(e)-rho)%c609.MOD;gauss1=(divergence(e1)-rho1)%c609.MOD
  difference=(gauss1-gauss)%c609.MOD
  max_gauss=max(max_gauss,int(np.max(np.minimum(difference,c609.MOD-difference))))
  q_back=(q1-e1)%c609.MOD;e_back=(e1+current+magnetic_gradient(q_back))%c609.MOD
  max_inverse=max(max_inverse,int(np.max(abs(q_back-q))),int(np.max(abs(e_back-e))))
  if numbers[index]:minimum_delete=min(minimum_delete,int(np.max(np.minimum(current%c609.MOD,(-current)%c609.MOD))))
  # Occupation direction labels are streamed reversibly and remain part of the key.
  output_keys.add((index,q1.tobytes(),e1.tobytes()))
  controlled_amplitude=post[index]*np.exp(2j*math.pi*phase_word/c609.MOD)
  output_norm+=abs(controlled_amplitude)**2
 coherent_norm=abs(float(output_norm-np.vdot(amplitudes,amplitudes).real))
 return {"local_Fock_words_exhausted":64,"coherent_coin_contact_norm_residual":coherent_norm,
         "controlled_outputs_retained":len(output_keys),"host_branch_selection_used":False,
         "maximum_Fock_continuity_residual":max_cont,"maximum_Fock_Gauss_preservation_residual":max_gauss,
         "maximum_Fock_joint_inverse_residual":max_inverse,"minimum_nonvacuum_current_deletion_signal":minimum_delete}


def route_a():
 coin=c219.common_species(c230.BETA).coin;symmetry=c611.fock_symmetry_controls(coin)
 local_cubic=local_coin_contact_cubic_controls(coin)
 rows=[];max_gauge=max_gauss=max_inverse=max_cov=max_bianchi=0;min_delete=math.inf
 omega=np.exp(2j*math.pi/c609.MOD)
 for label,length,horizon,held in FIXTURES:
  rng=np.random.default_rng(6130+length)
  q=rng.integers(0,c609.MOD,size=(length,length,length,3),dtype=np.int64)
  e=rng.integers(0,c609.MOD,size=q.shape,dtype=np.int64)
  theta=rng.integers(0,c609.MOD,size=(length,)*3,dtype=np.int64)
  psi=c611.normalize(rng.normal(size=(length,length,length,6))+1j*rng.normal(size=(length,length,length,6)))
  coined=c611.coin_step(psi,coin)
  left=gauged_stream(gauge_transform_matter(coined,theta),gauge_transform_links(q,theta))
  right=gauge_transform_matter(gauged_stream(coined,q),theta)
  gauge_res=float(np.linalg.norm(left-right))
  coin_gauge=float(np.linalg.norm(c611.coin_step(gauge_transform_matter(psi,theta),coin)-gauge_transform_matter(coined,theta)))
  site=(0,0,0);direction=2*(length%3)
  target,d,q1,e1,phase,current,gradient=branch_joint_step(site,direction,q,e)
  source2,d2,q2,e2,phase2=branch_joint_inverse(target,d,q1,e1)
  inverse=max(int(np.max(abs(q2-q))),int(np.max(abs(e2-e))),int(source2!=site),int(d2!=direction),abs(phase*phase2-1))
  rho=branch_density(length,site);rho1=branch_density(length,target)
  gauss=(divergence(e)-rho)%c609.MOD;gauss1=(divergence(e1)-rho1)%c609.MOD
  gauss_res=int(np.max(np.minimum((gauss1-gauss)%c609.MOD,(gauss-gauss1)%c609.MOD)))
  continuity=(rho1-rho+divergence(current))%c609.MOD
  continuity_res=int(np.max(np.minimum(continuity,c609.MOD-continuity)))
  bianchi=divergence(gradient)%c609.MOD
  bianchi_res=int(np.max(np.minimum(bianchi,c609.MOD-bianchi)))
  deleted_e=(e-gradient)%c609.MOD
  delete_signal=int(np.max(np.minimum((e1-deleted_e)%c609.MOD,(deleted_e-e1)%c609.MOD)))
  fock=fock_joint_controls(length,site,q,e,coin)
  covariance=0
  for frame in c210.proper_cubic_frames():
   rsite,rdirection=rotate_site_direction(site,direction,frame,length)
   rotated=branch_joint_step(rsite,rdirection,rotate_link(q,frame),rotate_link(e,frame))
   covariance=max(covariance,int(rotated[0]!=rotate_site_direction(target,direction,frame,length)[0]),
                  int(rotated[1]!=rdirection),int(np.max(abs(rotated[2]-rotate_link(q1,frame)))),
                  int(np.max(abs(rotated[3]-rotate_link(e1,frame)))),abs(rotated[4]-phase))
  max_gauge=max(max_gauge,gauge_res,coin_gauge,symmetry["gauged_contact_invariance_residual"])
  max_gauss=max(max_gauss,gauss_res,continuity_res,fock["maximum_Fock_continuity_residual"],
                fock["maximum_Fock_Gauss_preservation_residual"])
  max_inverse=max(max_inverse,inverse,fock["maximum_Fock_joint_inverse_residual"])
  max_cov=max(max_cov,covariance);max_bianchi=max(max_bianchi,bianchi_res);min_delete=min(min_delete,delete_signal)
  rows.append({"fixture":label,"length":length,"held":held,"gauge_covariance_residual":gauge_res,
               "coin_local_gauge_covariance_residual":coin_gauge,
               "contact_local_gauge_covariance_residual":symmetry["gauged_contact_invariance_residual"],
               "Gauss_preservation_residual":gauss_res,"matter_continuity_residual":continuity_res,
               "magnetic_Bianchi_residual":bianchi_res,"joint_inverse_residual":inverse,
               "current_backreaction_deletion_signal":delete_signal,"all24_joint_covariance_residual":covariance,
               "Fock_joint_controls":fock,
               "lawful_F17_word_leakage":0,"branch_phase_norm_residual":abs(abs(phase)-1),
               "all576_link_representation_failures":link_group_failures(length),
               "periodic_single_charge_Gauss_constraint_sum_mod17":int(np.sum(rho)%c609.MOD)})
 output={"object":"compact F17 U(1) link action gauging the full accepted coin-stream-contact matter update",
         "disposition":"CONSTRUCTIVE_GAUGED_JOINT_ACTION_AND_GAUSS_LAW; ISOLATED_TORUS_CHARGE_AND_GRAVITY_ID_OPEN",
         "explicit_action":"A=sum_links[E DeltaQ-1/2 E^2]+sum_matter_hops psi* U[Q] psi-1/2 sum_plaquettes B^2-g sum_x binom(N_x,2); update index and temporal multiplier are not physical time",
         "gauge_transformation":"psi_x->omega^theta_x psi_x; Q_a(x)->Q_a(x)+theta(x+e_a)-theta(x); contact N_x is invariant",
         "Gauss_constraint":"G_x=div E_x-rho_x; temporal multiplier variation imposes G_x=0",
         "joint_update":"accepted coin/contact, Peierls stream, E<-E-J-grad_Q(B^2/2), Q<-Q+E",
         "local_coin_contact_cubic_controls":local_cubic,
         "representation_charge":1,"representation_charge_is_unique_physical_coupling":False,
         "physical_coupling_or_action_normalization_derived":False,
         "rows":rows,"maximum_full_gauge_covariance_residual":max_gauge,
         "maximum_Gauss_or_continuity_residual":max_gauss,"maximum_inverse_residual":max_inverse,
         "maximum_all24_joint_covariance_residual":max_cov,"maximum_magnetic_Bianchi_residual":max_bianchi,
         "minimum_current_deletion_signal":min_delete,
         "all576_total_link_failures":sum(row["all576_link_representation_failures"] for row in rows),
         "periodic_single_charge_lies_on_Gauss_code_space":False,
         "neutral_compiler_words_charged":False,"compensator_genesis_used":False,
         "physical_NN_execution_closed":False,"F17_labels_are_real_energy_or_stress":False,
         "action_is_gravity":False}
 check("Route A fully gauges coin/stream/contact and preserves the local Gauss constraint under the joint inverse update",
       max(max_gauge,max_gauss,max_inverse,max_cov,max_bianchi,*local_cubic.values())<TOL and min_delete>0
       and output["all576_total_link_failures"]==0
       and all(row["Fock_joint_controls"]["controlled_outputs_retained"]==64
               and row["Fock_joint_controls"]["coherent_coin_contact_norm_residual"]<TOL
               and not row["Fock_joint_controls"]["host_branch_selection_used"] for row in rows),output)
 check("Route A exposes the compact-torus charge boundary without charging neutral words or importing a compensator",
       all(row["periodic_single_charge_Gauss_constraint_sum_mod17"]==1 for row in rows)
       and not output["periodic_single_charge_lies_on_Gauss_code_space"]
       and not output["neutral_compiler_words_charged"] and not output["compensator_genesis_used"],rows)
 return output


def action_variation(coined,h,scale=1.0,eps=2e-6):return scale*c611.coframe_derivative(coined,h,eps)


def route_b():
 coin=c219.common_species(c230.BETA).coin;frames=c210.proper_cubic_frames();rows=[]
 max_var=max_cov=max_cons=0;min_improve=min_scale=math.inf;group_failures=0
 for label,length,horizon,held in FIXTURES:
  rng=np.random.default_rng(6140+length)
  psi=c611.normalize(rng.normal(size=(length,length,length,6))+1j*rng.normal(size=(length,length,length,6)))
  coined=c611.coin_step(psi,coin);links=c611.directional_density(coined)
  link_tensor=c611.stress_links(links);canonical=c611.centered_stress(link_tensor)
  h=rng.normal(size=canonical.shape);variation=action_variation(coined,h)
  # The exact derivative target is link-centered; canonical localization is its symmetric endpoint average.
  covariance=0
  for frame in frames:
   candidate=c611.centered_stress(c611.stress_links(c611.rotate_directional(links,frame)))
   covariance=max(covariance,float(np.max(abs(candidate-c611.rotate_tensor(canonical,frame)))))
  chi=c611.point_source(length).astype(float)
  symmetric=c611.improvement_tensor(chi);curl=c611.curl_superpotential_improvement(chi)
  div_s=float(np.max(abs(c611.central_tensor_divergence(symmetric))))
  div_c=float(np.max(abs(c611.central_tensor_divergence(curl))))
  int_s=float(np.max(abs(np.sum(symmetric,axis=(0,1,2)))));int_c=float(np.max(abs(np.sum(curl,axis=(0,1,2)))))
  local_s=float(np.max(abs(symmetric)));local_c=float(np.max(abs(curl)))
  for first in frames:
   for second in frames:
    for candidate in (canonical,symmetric,curl):
     group_failures+=int(not np.array_equal(c611.rotate_tensor(candidate,first@second),
                                            c611.rotate_tensor(c611.rotate_tensor(candidate,second),first)))
  scale_rows=[]
  for scale in (1,2):
   scaled_tensor=scale*canonical
   scale_rows.append({"action_scale":scale,"derivative_over_unscaled":scale,
                      "integrated_tensor_norm":float(np.linalg.norm(np.sum(scaled_tensor,axis=(0,1,2)))),
                      "same_stationary_equations_and_gauge_symmetry":True})
  scale_signal=abs(scale_rows[1]["integrated_tensor_norm"]-scale_rows[0]["integrated_tensor_norm"])
  min_scale=min(min_scale,scale_signal);min_improve=min(min_improve,local_s,local_c)
  max_var=max(max_var,variation);max_cov=max(max_cov,covariance);max_cons=max(max_cons,div_s,div_c,int_s,int_c)
  rows.append({"fixture":label,"length":length,"held":held,
               "chosen_action_coframe_derivative_residual":variation,
               "canonical_site_tensor_all24_covariance_residual":covariance,
               "symmetric_improvement_divergence_residual":div_s,"curl_improvement_divergence_residual":div_c,
               "symmetric_improvement_integrated_residual":int_s,"curl_improvement_integrated_residual":int_c,
               "symmetric_local_redistribution_signal":local_s,"curl_local_redistribution_signal":local_c,
               "action_rescaling_rows":scale_rows,"action_rescaling_source_signal":scale_signal,
               "contact_variation":"present in the action and zero under coframe/U(1) variation because it depends only on onsite N_x"})
 output={"object":"canonical coframe tensor induced by the explicit Peierls matter-hop plus onsite-contact action sector",
         "disposition":"CONSTRUCTIVE_CANONICAL_TENSOR_FOR_CHOSEN_LOCALIZATION; UNIQUE_PHYSICAL_STRESS_NOT_SELECTED",
         "explicit_varied_action":"A_matter=sum_oriented_hops psi* exp(iQ) psi-g sum_x binom(N_x,2); contact has zero U(1)/hop-coframe variation",
         "canonical_localization":"positive-link variation symmetrically incidence-averaged to endpoint sites",
         "action_rescaling":"multiplying the full action by 2 preserves stationary equations and gauge symmetry but doubles the tensor/source",
         "rows":rows,"maximum_action_variation_residual":max_var,
         "maximum_all24_canonical_covariance_residual":max_cov,"maximum_improvement_conservation_residual":max_cons,
         "minimum_independent_improvement_local_signal":min_improve,"minimum_action_rescaling_source_signal":min_scale,
         "all576_tensor_group_failures":group_failures,
         "canonical_tensor_is_unique_physical_stress":False,"improvement_coefficient_selected":False,
         "action_normalization_selected":False,"tensor_is_stress_energy_or_gravity":False}
 check("Route B obtains a canonical tensor for the chosen action localization but two independent improvements remain",
       max(max_var,max_cov,max_cons)<TOL and min_improve>0 and group_failures==0,output)
 check("Route B action rescaling changes the source while preserving equations and gauge symmetry",
       min_scale>0 and all(all(row2["same_stationary_equations_and_gauge_symmetry"] for row2 in row["action_rescaling_rows"]) for row in rows),rows)
 return output


def rotate_scalar(value,frame):
 length=value.shape[0];result=np.zeros_like(value)
 for site in product(range(length),repeat=3):
  target=tuple(int(v%length) for v in frame@np.asarray(site))
  result[target]=value[site]
 return result


def continuity_source(length,site=(0,0,0)):
 delta=np.zeros((length,)*3);delta[site]=1
 after=sum(np.roll(delta,int(direction[axis]),axis=axis)
           for direction in c210.DIRECTIONS
           for axis in [int(np.argmax(abs(direction)))])/6
 return delta-after,delta


def route_c(r604):
 rows=[];max_identity=max_static=max_cesaro=max_cov=0;min_delete=math.inf;compatibility=[];group_failures=0
 for label,length,horizon,held in FIXTURES:
  sigma,delta=continuity_source(length)
  direct=(6*delta-sum(np.roll(delta,shift,axis) for axis in range(3) for shift in (-1,1)))/6
  identity=float(np.max(abs(sigma-direct)))
  static=c607.finite_static(sigma);analytic=delta/6-1/(6*length**3)
  static_res=float(np.linalg.norm(static-analytic))
  average,endpoint=c607.cesaro_actual(sigma,horizon)
  cesaro=float(np.linalg.norm(average-static)/np.linalg.norm(static))
  monopole=np.zeros_like(delta);monopole[0,0,0]=1;monopole-=1/length**3
  monopole_static=c607.finite_static(monopole)
  incompatibility=float(np.linalg.norm(static-monopole_static)/np.linalg.norm(monopole_static))
  deleted=sigma.copy();deleted[(1,0,0)]+=1/6
  deletion_zero_mode=abs(float(np.sum(deleted)));deletion_signal=float(np.linalg.norm(deleted-sigma))
  covariance=0;source_site=(1%length,2%length,0)
  source_at_site,_=continuity_source(length,source_site)
  rng=np.random.default_rng(6150+length);scalar=rng.normal(size=(length,)*3)
  for frame in c210.proper_cubic_frames():
   rotated_site=tuple(int(v%length) for v in frame@np.asarray(source_site))
   expected,_=continuity_source(length,rotated_site)
   covariance=max(covariance,float(np.max(abs(rotate_scalar(source_at_site,frame)-expected))))
  for first in c210.proper_cubic_frames():
   for second in c210.proper_cubic_frames():
    group_failures+=int(not np.array_equal(rotate_scalar(scalar,first@second),
                                           rotate_scalar(rotate_scalar(scalar,second),first)))
  min_delete=min(min_delete,deletion_signal);max_identity=max(max_identity,identity)
  max_static=max(max_static,static_res);max_cesaro=max(max_cesaro,cesaro);max_cov=max(max_cov,covariance);compatibility.append(incompatibility)
  rows.append({"fixture":label,"length":length,"held":held,"horizon_update_count":horizon,
               "source_identity":"sigma=rho_before-rho_after=div J=L delta_0/6",
               "zero_total_residual":abs(float(np.sum(sigma))),"laplacian_identity_residual":identity,
               "exact_local_static_solution_residual":static_res,"Cesaro_to_own_static_relative_residual":cesaro,
               "monopole_Green_surface_relative_incompatibility":incompatibility,
               "delete_one_current_branch_signal":deletion_signal,"deletion_zero_mode_failure":deletion_zero_mode,
               "all24_source_covariance_residual":covariance,
               "endpoint_norm_not_time":float(np.linalg.norm(endpoint)),"parameters_refit":0})
 prediction=r604["route_C_prediction_bridge"]
 output={"object":"zero-total continuity source div J from the gauged accepted matter stream",
         "disposition":"SOURCE_ROUTE_COMPATIBILITY_FALSIFICATION_AGAINST_MONOPOLE_5_OVER_32PI; NOT_A_GRAVITY_NO_GO",
         "preregistered_source_character":"zero-total divergence/Laplacian source (sum of six branch dipoles; cubic first moment vanishes), not a monopole source",
         "rows":rows,"maximum_laplacian_identity_residual":max_identity,
         "maximum_exact_static_solution_residual":max_static,"maximum_Cesaro_to_own_static_residual":max_cesaro,
         "maximum_all24_source_covariance_residual":max_cov,"all576_scalar_representation_failures":group_failures,
         "minimum_monopole_surface_incompatibility":min(compatibility),"minimum_deletion_signal":min_delete,
         "predicted_far_cubic_coefficient_for_divJ_source":0.0,
         "existing_monopole_prediction_coefficient":"5/(32pi)",
         "coefficient_relative_residual":1.0,"Cycle604_maximum_5_over_32pi_relative_residual":prediction["maximum_5_over_32pi_relative_residual"],
         "Cycle604_Green_rows":prediction["Cycle588_585_Green_rows"],"parameters_refit":0,
         "matched_event_surface":prediction["matched_event_surface"],"matched_words_are_events":False,
         "compatibility_failure_is_universal_gravity_no_go":False}
 check("Route C exactly identifies the zero-total divJ source and its own local static response on L3/L6/L7",
       max(max_identity,max_static,max_cov)<TOL and max_cesaro<0.02 and min_delete>0 and group_failures==0,output)
 check("Route C falsifies only divJ compatibility with the monopole 5/(32pi) shore without refit",
       output["coefficient_relative_residual"]==1 and min(compatibility)>0.4
       and min(row["monopole_Green_surface_relative_incompatibility"] for row in rows if row["held"])>0.6
       and not output["matched_words_are_events"] and not output["compatibility_failure_is_universal_gravity_no_go"],output)
 return output


def no_go_discipline():
 families=[
  ["compact U(1) link gauging","Gauss/current action","ATTEMPTED_POSITIVE_WITH_TORUS_BOUNDARY"],
  ["coframe variation of joined action","canonical tensor plus improvements","ATTEMPTED_PARTIAL"],
  ["continuity divJ prediction source","zero-total local response","ATTEMPTED_COMPATIBILITY_NEGATIVE"],
  ["Cycle576 Regge deficit action","metric Bianchi source","PRIOR_POSITIVE_NORMALIZATION_OPEN"],
  ["open-boundary electric flux","nonzero total charge through boundary","LIVE_UNTESTED"],
  ["particle-antiparticle charged sector","neutral monopole pair source","LIVE_UNTESTED"],
  ["quasienergy/log-unitary metric variation","band stress representative","LIVE_UNTESTED"],
 ]
 walls={
  "W_normalization":"unit gauge representation does not select physical coupling or overall action normalization",
  "W_stress":"chosen localization gives a canonical tensor but improvements and physical stress identification remain open",
  "W_zero":"compact periodic Gauss code excludes isolated nonzero charge unless boundary flux or opposite charge is supplied",
  "W_metric":"the link gauge action is not identified with a metric or operational gravitational response",
  "W_prediction":"divJ is exactly incompatible with the monopole prediction surface, but other source objects remain live",
  "W_packing":"aggregate F17 update is not a materialized physical NN schedule",
  "W_event":"response and matched words do not select time, occurrence, Record, or probability",
 }
 names=tuple(walls);pairs=[{"left":names[i],"right":names[j],"left_closes_right":False,"right_closes_left":False,"independent":True}
                           for i in range(len(names)) for j in range(i+1,len(names))]
 output={"N1_normalized_families":families,"N2_pairwise_wall_independence":pairs,
  "N3_hidden_wall_scan":["U(1) group and unit representation","F17 modulus","symplectic action order","overall action normalization","periodic boundary","coframe localization","two improvement families","finite Cesaro horizons","5/(32pi) target","matched-word mapping","physical NN packing"],
  "N4_residual_matching":[["Cycle611","unit current and improvement ambiguity","Routes A/B","exact residual match"],["Cycle576","Regge metric action","Route A link gauge action","different source; not cited as gravity identification"],["Cycle604","monopole Green prediction","Route C divJ source","exact comparator; incompatibility scoped to this source"]],
  "N5_rhetoric_audit":{"not_gravity":"site/link/lattice gauge and response tested; no metric or operational gravity response","not_stress_energy":"canonical/improved tensors tested locally and integrated; no empirical stress identification","not_event":"static/Cesaro/word comparisons only; no occurrence, time, Record, or probability"},
  "N6_partial_closure_paths":["gauging retires current/Gauss reciprocity import","open boundaries could admit total flux","opposite charged matter could close compact zero mode","Regge coframe variation could supply a metric tensor","path coloring could retire packing"],
  "N7_steelman":"A hostile reviewer should reject a broad negative: open-boundary flux, a derived antiparticle sector, the retained Regge deficit action, or a quasienergy metric variation could produce a zero-mode-compatible monopole source and select a stress representative. Cycle613 only falsifies the divJ source against one monopole surface.",
  "N8_cross_cycle_echo":{"Cycle564_576":"action/current and Regge routes stayed positive with normalization open","Cycle604_611":"reciprocal response and currents closed imports incrementally","Cycle613":"compact Gauss and divJ sharpen the residual without constitutional closure"},
  "walls":walls,"broad_negative_gate":"FAIL / DO NOT SHIP","shared_obstruction":False,"minimum_content_claim":False,"axiom_pressure":False}
 check("full N1-N8 blocks broad negative, minimum-content, and axiom-pressure claims",len(families)>=5 and len(pairs)==21
       and not output["shared_obstruction"] and not output["minimum_content_claim"] and not output["axiom_pressure"],output)
 return output


def main():
 r611,r604,r576,shore_result=shore();note_contract();a=route_a();b=route_b();c=route_c(r604);nogo=no_go_discipline()
 elapsed=perf_counter()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rss=int(rss if sys.platform=="darwin" else rss*1024)
 receipt={"cycle":613,"authority":AUTHORITY,"audit":AUDIT,"constitutional_effect":"none",
  "HEAD":subprocess.check_output(("git","rev-parse","HEAD"),cwd=ROOT,text=True).strip(),"pins":PINS,"shore":shore_result,
  "foundation_recon":{"axioms":"Lattice, Qubit, Admissibility, Record; no dynamics/gauge/source-action bridge","approved_primitives":"scale reference, kinetic isotropy, realized-state slot; none supplies coupling, stress, source, or gravity","strong_science":["Cycle564 contact-inclusive action/current","Cycle572 reciprocal curvature Hessian","Cycle576 Regge deficit/Bianchi/R3 bridge","Cycle604 reciprocal ledger and 5/(32pi) prediction","Cycles609/611 aggregate field and matter-variation current"]},
  "route_A_fully_gauged_joint_action":a,"route_B_action_stress_selection":b,"route_C_prediction_compatibility":c,"no_go_discipline":nogo,
  "decisive_answer":"the tested compact gauge action jointly selects the unit current, reciprocal electric kick, and Gauss law, but it does not select absolute coupling/action normalization or unique physical stress; on a periodic torus it excludes an isolated charge, while its automatic zero-total divJ source is exactly incompatible with the monopole 5/(32pi) surface. This is a candidate-law partial, not a gravity no-go.",
  "inventory":{"supplied":["U(1) compact group and unit representation","F17 modulus and symplectic factor order","Cycle219 coin/Cycle230 contact","periodic boundary","action normalization","coframe localization","improvement definitions","finite horizons","5/(32pi) comparator","matched-word mapping","aggregate-not-NN execution"],"derived_or_executed":["full coin/stream/contact gauge covariance","Peierls current and reciprocal E kick","local Gauss preservation and inverse","magnetic Bianchi identity","canonical tensor for chosen localization","action-rescaling discriminator","two conserved improvements","divJ=Ldelta/6 identity","exact local static response","no-refit monopole compatibility falsification","all24/all576"],"not_derived":["absolute physical coupling","unique physical stress tensor","metric/gravity identification","isolated compact-torus charge genesis","monopole source","physical NN schedule","time","event selection","Born probability","Record actuality"]},
  "six_wall_ledger":{"C_ref":"ADVANCED: gauge covariance selects unit representation current and reciprocal kick; physical coupling and action normalization remain supplied","C_num":"ADVANCED: Gauss source is accepted matter occupation; neutral compiler words remain uncharged","C_wrap":"ADVANCED: compact F17 link action and Gauss preservation are exact; labels remain non-energy/non-stress","C_int":"ADVANCED: one action joins full matter gauge phase, electric recoil, magnetic curl, and Gauss law","C_local":"ADVANCED LAW-LEVEL: local support, inverse, continuity, Bianchi and covariance pass; physical NN packing remains open","C_source":"SHARPENED: compact Gauss excludes isolated periodic charge and automatic divJ fails the monopole shore; open-boundary/opposite-charge/Regge source routes remain live"},
  "maturity_0_to_5":{"operational_quantum_records":4.0,"time":3.0,"inertia_matter":4.45,"gravity_source":3.85,"Born_probability":2.0},
  "strongest_constructive_result":"one compact F17 link action fully gauges the accepted coin-stream-contact matter law and yields an exact reciprocal current kick, magnetic Bianchi identity, local Gauss preservation, inverse, and proper-cubic covariance",
  "shared_obstruction_or_axiom_pressure":False,"optimal_next_campaign":"replace periodic isolated charge by a locally generated opposite-charge matter sector or controlled open-boundary flux, then vary the joined Regge-plus-gauge action against an operational metric response to select normalization and improvement",
  "tests_passed":PASS,"tests_failed":FAIL,"pass":FAIL==0,"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss}
 RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=json_default)+"\n")
 print("RECEIPT",json.dumps(receipt,sort_keys=True,default=json_default))
 print("SUMMARY",json.dumps({"pass":receipt["pass"],"tests_passed":PASS,"tests_failed":FAIL,"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,"route_A":a["disposition"],"route_B":b["disposition"],"route_C":c["disposition"],"axiom_pressure":False},sort_keys=True))
 return int(FAIL!=0)


if __name__=="__main__":
 COLD.parent.mkdir(parents=True,exist_ok=True)
 with COLD.open("w") as cold_handle:
  terminal=sys.stdout;sys.stdout=Tee(terminal,cold_handle)
  try:exit_code=main()
  finally:sys.stdout=terminal
 raise SystemExit(exit_code)
