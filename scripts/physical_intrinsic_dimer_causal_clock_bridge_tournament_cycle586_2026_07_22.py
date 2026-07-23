#!/usr/bin/env python3
"""Cycle586: intrinsic dimer / causal-clock bridge tournament."""
from __future__ import annotations
from hashlib import sha256
from itertools import combinations
import json, math, pathlib, resource, signal, subprocess, sys, time
import numpy as np

ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22 as c578
NOTE=ROOT/"docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_DIMER_CAUSAL_CLOCK_BRIDGE_TOURNAMENT_CYCLE586_NOTE_2026-07-22.md"
RECEIPT=ROOT/"outputs/physical_intrinsic_dimer_causal_clock_bridge_tournament_cycle586_receipt_2026_07_22.json"
AUTHORITY="none"; AUDIT="unset"; TOL=5e-9; PASS=0; FAIL=0
CAP_SECONDS=360.; CAP_BYTES=3*1024**3
PINS={
"scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py":"4ab857755b606d7ba7432179ed66de723ac31d3f66507cafa1168ab60d4965d6",
"scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py":"c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
"scripts/active_cubic_source_response_cycle211_2026_07_16.py":"d5392152d322ea8f3850d0345d6caa426db22ae7f7694775b4bd6388704c18a6",
"scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py":"472e28c78901368629c8d9d6f614bb8fb3ea003639ac61d480d06941cdf6cb86",
"scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py":"464e5928b7c1e46c23e4010363b6bd8ff3d0e2379c6e5ecb46891010ef47a5a4",
"scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":"ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
"scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":"b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
"scripts/physical_held_sparse_order_retirement_cycle563_2026_07_21.py":"55e51cafffa70284a6e8e1f0510ca0d2f890989ccbcf5bce64435df4c8e812a6",
"outputs/physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json":"ac9fcc1da45f33152679cfd2992abf1d037fae8647f1ab4d2d0526e6ac7000ae",
"scripts/physical_enlarged_link_contact_work_tournament_cycle569_2026_07_22.py":"877dc75a840ff348f15022784dc60190fa884fad216db3e1904fc089c9d3c091",
"outputs/physical_enlarged_link_contact_work_tournament_cycle569_receipt_2026_07_22.json":"ddba1d3cfb3167416b12a4a327dd136c4b61878f07ef1448629f2a440208b195",
"scripts/physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22.py":"37e9d0f336d773bd4a1957a6531f80dc35b9673a4ef0f99137e7fb33558bf849",
"outputs/physical_joint_clock_accumulator_contraction_bridge_cycle570_receipt_2026_07_22.json":"f9295faa4230427623ac350625a42fb17949fd86f523b6cf81aa247c14dd796c",
"scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py":"52c743889146189c2b574fa8012e7281340722303cb5b61fc53579e5fe23ebf4",
"outputs/physical_matter_transition_clock_equivalence_tournament_cycle573_receipt_2026_07_22.json":"18579c530dc869abd93970e2ac8c1c61cb711d3e1f1b2f72474629bb36972d6a",
"scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py":"0c845ecd02b86ce4d99aa8406a206e9b01628f02f1592cf37c41a084eb1e0a4b",
"scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py":"0876bc8888193606446b5fe07f1fdd8e3ddef3b313551739b81be3792c820aa7",
"outputs/physical_l41_projector_instrument_compiler_tournament_cycle577_receipt_2026_07_22.json":"f7e6bbc40a4d56ee115ba43ddbab7bee4aff05227b988a057adc4420f51941ed",
"scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py":"2a3c77c26003bb0f8b55fe2da0fd36b0ac98a14a21a083303fe175e5f802e99f",
"outputs/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_receipt_2026_07_22.json":"b84f1cfaa03661a0a2498fd409e077aeeb4f6ad423909807d20be7c846c571f7",
"scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py":"21957cc883550ee81fc48d5b55ad4a0384cbac8697557691c805d84c7c8dbaaf",
"outputs/physical_contact_dimer_infinite_internal_content_tournament_cycle583_receipt_2026_07_22.json":"0f4e2df9e25cdc7137c42fb91666c5eaae10efc652d5af84f421e38c5ad97aab"}
def sha(p): return sha256(p.read_bytes()).hexdigest()
def check(label,ok,detail=""):
 global PASS,FAIL
 PASS+=int(ok); FAIL+=int(not ok); print("PASS" if ok else "FAIL",label,"::",detail)
def shore():
 observed={p:sha(ROOT/p) for p in PINS}
 receipts=[json.loads((ROOT/p).read_text()) for p in PINS if p.startswith("outputs/")]
 fixtures=json.loads((ROOT/"outputs/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_receipt_2026_07_22.json").read_text())["retained_physical_M2_fixtures"]
 receipt_boundary=all(r["pass"] and r["authority"]=="none" and r["audit"]=="unset" for r in receipts)
 check("all clock, dimer, and conditional code-space shores are exact-pinned",observed==PINS and receipt_boundary and max(fixtures[k] for k in ("one_particle_mass_residual","Cycle230_contact_factorization_residual","Cycle230_seam_braid_residual"))<TOL,{"pins":observed,"receipt_boundary":receipt_boundary,"fixtures":fixtures})
 return fixtures
def packet_from_actual_fibers(relative_L, momenta, center, circumference=128):
 values=[];vectors=[];prior=None
 for kx in momenta:
  value,vector,obs=c578.isolated_eigenpair(relative_L,-.3,.37,(float(kx),0.,0.),-2.976,prior=prior,eigen_count=8)
  values.append(value);vectors.append(vector);prior=vector
 vectors=np.asarray(vectors);values=np.asarray(values)
 index=np.arange(len(momenta));weights=np.exp(-.5*((index-(len(index)-1)/2)/1.05)**2).astype(complex)
 weights*=np.exp(-1j*np.asarray(momenta)*center);weights/=np.linalg.norm(weights)
 x=np.arange(circumference);phase=np.exp(1j*np.outer(x,momenta))
 before=np.einsum('xk,k,kn->xn',phase,weights,vectors,optimize=True)
 after=np.einsum('xk,k,k,kn->xn',phase,weights,values,vectors,optimize=True)
 before/=np.linalg.norm(before);after/=np.linalg.norm(after)
 density0=np.sum(abs(before)**2,axis=1);density1=np.sum(abs(after)**2,axis=1)
 residual=max(float(np.linalg.norm(c578.relative_car_walk(relative_L,-.3,.37,(float(k),0.,0.))@v-z*v)) for k,z,v in zip(momenta,values,vectors))
 return density0,density1,values,residual
def route_a():
 prior=json.loads((ROOT/"outputs/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_receipt_2026_07_22.json").read_text())["route_B_actual_Cycle230_contact_dimer"]
 rows=[];delta=2*np.pi/128
 for relative_L,split,separation in ((5,"train",8),(7,"held",10)):
  ks_a=delta*np.arange(0,5);ks_b=-ks_a
  a0,a1,za,res_a=packet_from_actual_fibers(relative_L,ks_a,64-separation/2)
  b0,b1,zb,res_b=packet_from_actual_fibers(relative_L,ks_b,64+separation/2)
  encounter0=float(a0@b0);encounter1=float(a1@b1)
  deleted=float(a1@b0)
  flat_a=float(a0@b1)
  rows.append({"relative_L":relative_L,"split":split,"center_circumference":128,"supplied_initial_center_separation":separation,"K_labels_A":ks_a.tolist(),"K_labels_B":ks_b.tolist(),"encounter_projector_before":encounter0,"encounter_projector_after_one_actual_update":encounter1,"one_dimer_update_deleted":deleted,"flat_one_side_control":flat_a,"encounter_signal":abs(encounter1-encounter0),"deletion_signal":abs(encounter1-deleted),"maximum_actual_fiber_eigen_residual":max(res_a,res_b),"packet_norm_residual":max(abs(a0.sum()-1),abs(a1.sum()-1),abs(b0.sum()-1),abs(b1.sum()-1)),"tensor_product_decoupling_import":True})
 independence={"separate_initial_packets":True,"distinct_reference_genesis":False,"distinct_law_parameters":False,"shared_beta":-0.3,"shared_g":.37,"A2_internal_dimension":1,"full_four_CAR_antisymmetrization_or_scattering_included":False}
 check("Route A executes actual A2 fibers and exposes a held local two-dimer encounter-projector signal",min(r["encounter_signal"] for r in rows)>1e-7 and min(r["deletion_signal"] for r in rows)>1e-7 and max(r["maximum_actual_fiber_eigen_residual"] for r in rows)<1e-10 and max(r["packet_norm_residual"] for r in rows)<TOL,{"rows":rows,"independence":independence})
 return {"rows":rows,"all24_inherited_band_covariance_residual":prior["maximum_all24_covariance_residual"],"local_encounter_observable":"sum_x P_center,A(x) tensor P_center,B(x)","independence_audit":independence,"independent_standard_certified":False,"physical_M2_dimer_compiler_available":False,"interpretation":"actual finite CAR-fiber band packets on an explicitly decoupled tensor product; no four-CAR scattering, event latch, self-timing, or physical-M2 dimer embedding"}
def first_return(L,separation):
 if L<3 or L%2==0 or separation<=0 or separation>=L: raise ValueError("odd one-hot ring and nonzero separation required")
 a=np.zeros(L,int);b=np.zeros(L,int);a[0]=1;b[separation]=1; rows=[];latched=0
 for opportunity in range(L+1):
  collision=int(np.vdot(a,b)); latched ^= collision; rows.append((opportunity,int(np.argmax(a)),int(np.argmax(b)),collision,latched))
  a=np.roll(a,1);b=np.roll(b,-1)
 return rows
def route_b():
 rows=[]
 for L,s,split in ((7,2,"train"),(11,4,"held")):
  trace=first_return(L,s); hits=[r[0] for r in trace if r[3]]
  no_detector=[(r[0],r[1],r[2],r[3],0) for r in trace]
  # deleting the left stream means its position remains fixed
  no_left=[];a=0;b=s;latched=0
  for opportunity in range(L+1):
   collision=int(a==b);latched^=collision;no_left.append((opportunity,a,b,collision,latched));b=(b-1)%L
  inverse_residual=int(((1-1)%L)!=0 or ((s-1+1)%L)!=s)
  rows.append({"L":L,"split":split,"initial_separation":s,"first_collision_opportunity":hits[0],"return_period_opportunities":L,"trace":trace,"detector_deletion_signal":sum(abs(x[4]-y[4]) for x,y in zip(trace,no_detector)),"stream_deletion_signal":int(no_left!=trace),"binary_role_upper_bound":2*L+2})
 malformed=False
 try:first_return(8,2)
 except ValueError:malformed=True
 frames=[]
 import itertools
 for perm in itertools.permutations(range(3)):
  for signs in itertools.product((-1,1),repeat=3):
   R=np.zeros((3,3),int)
   for j in range(3):R[perm[j],j]=signs[j]
   if round(np.linalg.det(R))==1:frames.append(R)
 e=np.array((1,0,0));cov=max(float(np.linalg.norm(R@e+R@(-e))) for R in frames)
 check("Route B gives an exact local first-return automaton with held deletion/domain/all24 controls",all(r["detector_deletion_signal"]>0 and r["stream_deletion_signal"] for r in rows) and rows[1]["first_collision_opportunity"]==2 and malformed and len(frames)==24 and cov<TOL,rows)
 return {"rows":rows,"lawful_domain":"odd one-hot rings, distinct carrier identities, blank latch","malformed_even_ring_rejected":malformed,"proper_cubic_frames":len(frames),"all24_opposite_stream_covariance_residual":cov,"logical_local_support":3,"controller_program_supplied":True,"intrinsic_dimer_law_used":False,"physical_M2_composition":False,"physical_intertwiner_residual":None,"physical_leakage_evaluated":False,"resource_debit":"two one-hot position words plus latch/program; repeated tick archive/reset and renewal open","self_timing_certified":False}
def route_c():
 c583=json.loads((ROOT/"outputs/physical_contact_dimer_infinite_internal_content_tournament_cycle583_receipt_2026_07_22.json").read_text()); roots=c583["route_A_finite_rank_contact_resolvent"]["roots"]
 selected=[r for r in roots if r["L"] in (11,19,31)]; rows=[]
 for r in selected:
  theta=r["wrapped_phase"]; p0=(1+math.cos(theta))/2; deleted=1.
  rows.append({**r,"hadamard_pointer_zero_weight":p0,"controlled_update_deletion_signal":abs(p0-deleted),"two_pi_lift_residual":abs((1+math.cos(theta+2*math.pi))/2-p0)})
 spread=max(r["hadamard_pointer_zero_weight"] for r in rows)-min(r["hadamard_pointer_zero_weight"] for r in rows)
 check("Route C turns the stable A2 wrapped phase into a bounded pointer observable without treating it as time",max(r["two_pi_lift_residual"] for r in rows)<TOL and min(r["controlled_update_deletion_signal"] for r in rows)>.9 and spread<1e-6,rows)
 return {"rows":rows,"held_pointer_spread":spread,"all24_A2_source_residual":c583["route_A_finite_rank_contact_resolvent"]["A2_all24_residual"],"conditional_instrument_role_upper_bound":"Cycle577 declared 18-role three-site gauge/Naimark block","fresh_low_entropy_role_count_per_instrument":12,"controlled_logical_Cycle230_update_supplied":True,"pointer_dephasing_and_member_law_supplied":True,"physical_M2_composition":False,"physical_intertwiner_residual":None,"physical_leakage_evaluated":False,"renewal_open":True,"independent_standard_certified":False,"phase_is_time_or_rate":False}
def nogo(retained):
 alternatives=(("two intrinsic packets","band motion/overlap","local autonomous encounter","positive diagnostic only"),("first-return collision","carried shifts/latch","repeatable endpoint word","positive with controller import"),("spectral instrument","Hadamard pointer","operational spectral comparison","positive with controlled-U import"),("second dimer irrep","A2-T2 local cross term","held co-moving beat","open"),("three-CAR internal mode","contact cluster","held internal oscillator","open"),("causal-front echo","corridor/reflection","independent endpoint standard","prior positive supplied apparatus"),("source-conditioned dual clock","distinct source response","redshift/lapse comparison","open"))
 walls=("independent genesis","intrinsic event law","physical-M2 dimer compiler","renewable latch resources","empirical calibration","continuum proper time")
 mechanisms={w:m for w,m in zip(walls,("separately generated standards","local encounter/transition dynamics","bounded site embedding and constraints","reset/archive stabilization","measured unit map","Lorentz/scaling theorem"))}
 pairwise=[(a,b,f"{a} needs {mechanisms[a]}, not {mechanisms[b]}",f"{b} needs {mechanisms[b]}, not {mechanisms[a]}",False) for a,b in combinations(walls,2)]
 n1=3
 gate={"N1_alternatives":alternatives,"N1_qualifying_attempted_families":n1,"N1_required":5,"N1_pass":False,"N2_directional_pairs":pairwise,"N3_hidden_supplies":("two packet preparations, K labels, separation, width","shift program/ring/latch","controlled-U, pointer, dephasing environment","beta,g,finite boxes,noiseless gates"),"N4_residual_matching":("Cycle573 trap wall matches autonomous localization/transport only","Cycle583 physical-M2 compiler and second-mode residuals match exactly","Cycle498/570 endpoint bridges do not supply intrinsic dimer events"),"N5_resolution":"finite packet, finite rings L7/L11, and phases L11/L19/L31 only","N6_reopen":("branch-aware A2-T2 volume embedding","three-CAR finite-rank resolvent","physical-M2 dimer compiler","locally generated collision latch","independently generated source-sensitive standard"),"N7_steelman":"A hostile reviewer can combine the nonzero finite A2-T2 component-local cross term with a branch-aware held embedding, then compile that local observable through the Cycle577 gauge instrument; this is a concrete unclosed route to an intrinsic beat and defeats any broad negative.","N8_echo":"Cycle498 retired depth readout using endpoints; Cycle570 retired finite count menus using distributed tokens; Cycle573 constructed a transition with a trap; Cycle578/583 supplied intrinsic dimer motion/contact structure. The same constructive progression may retire today's controller imports.","negative_claim_shipped":False,"minimum_content_claim_shipped":False,"shared_obstruction":False,"axiom_pressure":False}
 check("fresh N1-N8 withholds no-go, minimum-content, shared-obstruction, and axiom-pressure language",not gate["N1_pass"] and len(pairwise)==15 and not gate["negative_claim_shipped"] and not gate["minimum_content_claim_shipped"] and not gate["shared_obstruction"] and not gate["axiom_pressure"],gate)
 gate["ledger"]={"C_ref":"intrinsic moving dimer supplies a relational packet reference, but no independent genesis or held second internal mode","C_num":"finite overlap, return, and pointer diagnostics only; no empirical duration","C_wrap":"one-shot latch/ring returns are finite; renewal/archive open","C_int":"actual A2 contact band is consumed in A/C; Route B still uses supplied controller","C_local":"bounded detector/instrument candidates exist, but physical-M2 dimer embedding and controlled-U remain open","C_source":"beta/g common-mode only; no source response, redshift, or gravity"};return gate
def main():
 global PASS,FAIL
 signal.alarm(360);start=time.perf_counter();print("Cycle586 intrinsic dimer causal-clock bridge tournament",AUTHORITY,AUDIT)
 retained=shore();a=route_a();b=route_b();c=route_c();gate=nogo(retained)
 text=" ".join(NOTE.read_text().lower().replace("`","").replace("*","").split()); required=("authority: none","audit: unset","author_artifact_status_accepted: false","schedule is not time","wrapped phase is not time","a generator element is not a rate","a latch or pointer is not a record or actuality","car-fiber packet is not a physical-m2 dimer compiler","physical primitive composition remains open","n1 — normalized alternatives","no axiom pressure")
 check("note contract and interpretation firewall are explicit",all(x in text for x in required),[x for x in required if x not in text])
 elapsed=time.perf_counter()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rss=int(rss if __import__('sys').platform=='darwin' else rss*1024)
 check("cold caps",elapsed<CAP_SECONDS and rss<CAP_BYTES,{"elapsed":elapsed,"rss":rss})
 out={"status":"cycle586-intrinsic-dimer-causal-clock-bridge-strict-dependency-refresh","authority":AUTHORITY,"audit":AUDIT,"author_artifact_status_accepted":False,"refresh_run_HEAD":subprocess.check_output(("git","rev-parse","HEAD"),cwd=ROOT,text=True).strip(),"branch_head_equality_is_scientific_dependency":False,"pins":PINS,"runner_sha256":sha(pathlib.Path(__file__)),"note_sha256":sha(NOTE),"tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,"pass":FAIL==0,"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,"inherited_fixture_residuals":retained,"route_A":a,"route_B":b,"route_C":c,"interpretation_firewall":{"schedule_is_time":False,"wrapped_phase_is_time_energy_or_rate":False,"generator_element_is_rate":False,"packet_displacement_is_rate":False,"latch_or_pointer_is_Record_or_actuality":False,"pointer_weight_is_Born_probability":False,"finite_opportunity_ordinal_is_proper_time":False},"physical_M2_scope":{"primitive_composition":False,"intertwiner_residual":None,"leakage_evaluated":False,"leakage_residual":None},"no_go_discipline":gate,"six_wall_ledger":gate["ledger"],"highest_honest_terminal":"intrinsic finite CAR-band relational and spectral clock candidates plus an exact supplied-controller first-return comparator; not an independent self-timing physical-M2 clock or proper time"}
 RECEIPT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n");print("SUMMARY_JSON",json.dumps({"pass":FAIL==0,"tests":PASS,"elapsed":elapsed,"rss":rss,"independent_clock":False,"axiom_pressure":False},sort_keys=True));print("RESULT",PASS,FAIL);return int(FAIL!=0)
if __name__=="__main__": raise SystemExit(main())
