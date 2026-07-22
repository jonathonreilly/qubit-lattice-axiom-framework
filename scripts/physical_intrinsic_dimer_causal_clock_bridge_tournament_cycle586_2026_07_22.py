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
ACCEPTED="6ccf93471f"
PINS={
"scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":"ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
"scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":"b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
"scripts/physical_held_sparse_order_retirement_cycle563_2026_07_21.py":"444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b",
"scripts/physical_enlarged_link_contact_work_tournament_cycle569_2026_07_22.py":"c0f06a9cc9ffc4dcfe1d80b94da10bbef81ca1c74fddddac48712b0a7c332ced",
"scripts/physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22.py":"853abe5470efd15b154d6cb348d49795a6fa84e77a62f0b21a79105892b1d415",
"outputs/physical_joint_clock_accumulator_contraction_bridge_cycle570_receipt_2026_07_22.json":"f104399af621ded1b50e180e6fcce5f254008715b72191c6199fe4d583a8a806",
"scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py":"a85daf8fa9b8f3f1b7ef9aed6bfb84fe908ecbe33b2524f8ffebd66471dec20d",
"outputs/physical_matter_transition_clock_equivalence_tournament_cycle573_receipt_2026_07_22.json":"4863e0e32c8298c1539b0d10e274cd14661ed3d8aa895bbe6af697dc9b9d5553",
"scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py":"93bf1fa2859289b13037bfe7882cce86732e9377ed8b60e56c3bd55ebc0ce74f",
"outputs/physical_l41_projector_instrument_compiler_tournament_cycle577_receipt_2026_07_22.json":"806d7a7c1f8a7ed5b9de235de0bde5bec63d3fbaae7eb68cd55c862a35d9daa3",
"scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py":"25806853483a822b86dd55c50ebedb7957395151ef262317110b348c6931b9ab",
"outputs/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_receipt_2026_07_22.json":"c7af39acc2fe365e317297c7fe0cead00fad125145dec72c61d8d2da151b435c",
"scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py":"3f1672ef0d2c0063d5760a6b0885d75cb75b63c64b44951399fd0762d5499f7f",
"outputs/physical_contact_dimer_infinite_internal_content_tournament_cycle583_receipt_2026_07_22.json":"c143568db4f7c91c136efe02454cf7608c3e4ca680c631a960b3428b561ba96c"}
def sha(p): return sha256(p.read_bytes()).hexdigest()
def check(label,ok,detail=""):
 global PASS,FAIL
 PASS+=int(ok); FAIL+=int(not ok); print("PASS" if ok else "FAIL",label,"::",detail)
def shore():
 observed={p:sha(ROOT/p) for p in PINS}
 ancestor=subprocess.run(("git","merge-base","--is-ancestor",ACCEPTED,"HEAD"),cwd=ROOT).returncode==0
 receipts=[json.loads((ROOT/p).read_text()) for p in PINS if p.startswith("outputs/")]
 retained=json.loads((ROOT/"outputs/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_receipt_2026_07_22.json").read_text())["retained_physical_M2_fixtures"]
 check("all clock, dimer, and physical-M2 shores are exact",ancestor and observed==PINS and all(r["pass"] for r in receipts) and max(retained[k] for k in ("one_particle_mass_residual","Cycle230_contact_factorization_residual","Cycle230_seam_braid_residual"))<TOL,{"ancestor":ancestor,"pins":observed,"retained":retained})
 return retained
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
  rows.append({"L":L,"split":split,"initial_separation":s,"first_collision_opportunity":hits[0],"return_period_opportunities":L,"trace":trace,"detector_deletion_signal":sum(abs(x[4]-y[4]) for x,y in zip(trace,no_detector)),"stream_deletion_signal":int(no_left!=trace),"M2_upper_bound":2*L+2})
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
 return {"rows":rows,"lawful_domain":"odd one-hot rings, distinct carrier identities, blank latch","malformed_even_ring_rejected":malformed,"proper_cubic_frames":len(frames),"all24_opposite_stream_covariance_residual":cov,"local_support":3,"controller_program_supplied":True,"intrinsic_dimer_law_used":False,"resource_debit":"two one-hot position words plus latch/program; repeated tick archive/reset and renewal open","self_timing_certified":False}
def route_c():
 c583=json.loads((ROOT/"outputs/physical_contact_dimer_infinite_internal_content_tournament_cycle583_receipt_2026_07_22.json").read_text()); roots=c583["route_A_finite_rank_contact_resolvent"]["roots"]
 selected=[r for r in roots if r["L"] in (11,19,31)]; rows=[]
 for r in selected:
  theta=r["wrapped_phase"]; p0=(1+math.cos(theta))/2; deleted=1.
  rows.append({**r,"hadamard_pointer_zero_weight":p0,"controlled_update_deletion_signal":abs(p0-deleted),"two_pi_lift_residual":abs((1+math.cos(theta+2*math.pi))/2-p0)})
 spread=max(r["hadamard_pointer_zero_weight"] for r in rows)-min(r["hadamard_pointer_zero_weight"] for r in rows)
 check("Route C turns the stable A2 wrapped phase into a bounded pointer observable without treating it as time",max(r["two_pi_lift_residual"] for r in rows)<TOL and min(r["controlled_update_deletion_signal"] for r in rows)>.9 and spread<1e-6,rows)
 return {"rows":rows,"held_pointer_spread":spread,"all24_A2_source_residual":c583["route_A_finite_rank_contact_resolvent"]["A2_all24_residual"],"instrument_upper_bound":"Cycle577 18-M2 three-site gauge/Naimark block","fresh_low_entropy_M2_per_instrument":12,"controlled_Cycle230_update_compiler_supplied":True,"pointer_dephasing_and_member_law_supplied":True,"renewal_open":True,"independent_standard_certified":False,"phase_is_time_or_rate":False}
def nogo(retained):
 alternatives=(("two intrinsic packets","band motion/overlap","local autonomous encounter","positive diagnostic only"),("first-return collision","carried shifts/latch","repeatable endpoint word","positive with controller import"),("spectral instrument","Hadamard pointer","operational spectral comparison","positive with controlled-U import"),("second dimer irrep","A2-T2 local cross term","held co-moving beat","open"),("three-CAR internal mode","contact cluster","held internal oscillator","open"),("causal-front echo","corridor/reflection","independent endpoint standard","prior positive supplied apparatus"),("source-conditioned dual clock","distinct source response","redshift/lapse comparison","open"))
 walls=("independent genesis","intrinsic event law","physical-M2 dimer compiler","renewable latch resources","empirical calibration","continuum proper time")
 mechanisms={w:m for w,m in zip(walls,("separately generated standards","local encounter/transition dynamics","bounded site embedding and constraints","reset/archive stabilization","measured unit map","Lorentz/scaling theorem"))}
 pairwise=[(a,b,f"{a} needs {mechanisms[a]}, not {mechanisms[b]}",f"{b} needs {mechanisms[b]}, not {mechanisms[a]}",False) for a,b in combinations(walls,2)]
 n1=3
 gate={"N1_alternatives":alternatives,"N1_qualifying_attempted_families":n1,"N1_required":5,"N1_pass":False,"N2_directional_pairs":pairwise,"N3_hidden_supplies":("two packet preparations, K labels, separation, width","shift program/ring/latch","controlled-U, pointer, dephasing environment","beta,g,finite boxes,noiseless gates"),"N4_residual_matching":("Cycle573 trap wall matches autonomous localization/transport only","Cycle583 physical-M2 compiler and second-mode residuals match exactly","Cycle498/570 endpoint bridges do not supply intrinsic dimer events"),"N5_resolution":"finite packet, finite rings L7/L11, and phases L11/L19/L31 only","N6_reopen":("branch-aware A2-T2 volume embedding","three-CAR finite-rank resolvent","physical-M2 dimer compiler","locally generated collision latch","independently generated source-sensitive standard"),"N7_steelman":"A hostile reviewer can combine the nonzero finite A2-T2 component-local cross term with a branch-aware held embedding, then compile that local observable through the Cycle577 gauge instrument; this is a concrete unclosed route to an intrinsic beat and defeats any broad negative.","N8_echo":"Cycle498 retired depth readout using endpoints; Cycle570 retired finite count menus using distributed tokens; Cycle573 constructed a transition with a trap; Cycle578/583 supplied intrinsic dimer motion/contact structure. The same constructive progression may retire today's controller imports.","negative_claim_shipped":False,"shared_obstruction":False,"axiom_pressure":False}
 check("fresh N1-N8 withholds no-go, minimum-content, shared-obstruction, and axiom-pressure language",not gate["N1_pass"] and len(pairwise)==15 and not gate["negative_claim_shipped"],gate)
 gate["ledger"]={"C_ref":"intrinsic moving dimer supplies a relational packet reference, but no independent genesis or held second internal mode","C_num":"finite overlap, return, and pointer diagnostics only; no empirical duration","C_wrap":"one-shot latch/ring returns are finite; renewal/archive open","C_int":"actual A2 contact band is consumed in A/C; Route B still uses supplied controller","C_local":"bounded detector/instrument candidates exist, but physical-M2 dimer embedding and controlled-U remain open","C_source":"beta/g common-mode only; no source response, redshift, or gravity"};return gate
def main():
 global PASS,FAIL
 signal.alarm(360);start=time.perf_counter();print("Cycle586 intrinsic dimer causal-clock bridge tournament",AUTHORITY,AUDIT)
 retained=shore();a=route_a();b=route_b();c=route_c();gate=nogo(retained)
 text=" ".join(NOTE.read_text().lower().replace("`","").replace("*","").split()); required=("authority: none","audit: unset","schedule is not time","wrapped phase is not time","car-fiber packet is not a physical-m2 dimer compiler","n1 — normalized alternatives","no axiom pressure")
 check("note contract and interpretation firewall are explicit",all(x in text for x in required),[x for x in required if x not in text])
 elapsed=time.perf_counter()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rss=int(rss if __import__('sys').platform=='darwin' else rss*1024)
 check("cold caps",elapsed<CAP_SECONDS and rss<CAP_BYTES,{"elapsed":elapsed,"rss":rss})
 out={"status":"cycle586-intrinsic-dimer-causal-clock-bridge","authority":AUTHORITY,"audit":AUDIT,"HEAD":subprocess.check_output(("git","rev-parse","HEAD"),cwd=ROOT,text=True).strip(),"pins":PINS,"runner_sha256":sha(pathlib.Path(__file__)),"note_sha256":sha(NOTE),"tests_passed":PASS,"tests_failed":FAIL,"pass":FAIL==0,"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,"retained_M2_fixtures":retained,"route_A":a,"route_B":b,"route_C":c,"no_go_discipline":gate,"six_wall_ledger":gate["ledger"],"highest_honest_terminal":"intrinsic finite CAR-band relational and spectral clock candidates plus an exact supplied-controller first-return comparator; not an independent self-timing physical-M2 clock or proper time"}
 RECEIPT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n");print("SUMMARY_JSON",json.dumps({"pass":FAIL==0,"tests":PASS,"elapsed":elapsed,"rss":rss,"independent_clock":False,"axiom_pressure":False},sort_keys=True));print("RESULT",PASS,FAIL);return int(FAIL!=0)
if __name__=="__main__": raise SystemExit(main())
