#!/usr/bin/env python3
"""Cycle615: opposite-charge, open-flux, and gauge-Regge comparison tournament.

All three families are reexecuted.  Their sector labels, action coefficients,
resource roles, boundary state, Regge data, and receiver mapping remain supplied
candidate structure.  No coarse role is counted as a physical M2 and no direct-
sum algebra is promoted to a physical joined compiler.  Authority none; audit
unset; author artifact status accepted false.
"""
from __future__ import annotations

import ast
import contextlib
from fractions import Fraction
import gc
from hashlib import sha256
import io
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
AUTHORITY="none";AUDIT="unset";AUTHOR_ARTIFACT_STATUS_ACCEPTED=False
AUDIT_VERDICT_INFERRED_FROM_DEPENDENCIES=False
TOL=2e-8;START=perf_counter();PASS=FAIL=0
PERIODIC_FIXTURES=(("TRAIN_L3",3,False),("HELD_L6",6,True),("OUT_HELD_L7",7,True))
OPEN_FIXTURES=(("TRAIN_OPEN_L3",3,False),("HELD_OPEN_L5",5,True),("OUT_HELD_OPEN_L7",7,True))
PINS={
 "scripts/physical_gauged_matter_action_stress_prediction_tournament_cycle613_2026_07_22.py":"4a10475ffe3df07deaefd61119775eaeb483e5e894d4f006c35eec34df91586c",
 "docs/work_history/repo/review_feedback/PHYSICAL_GAUGED_MATTER_ACTION_STRESS_PREDICTION_TOURNAMENT_CYCLE613_NOTE_2026-07-22.md":"038650533ef3811d221dc476015bd71f713a0838936790e64aca0ff73fad2f16",
 "outputs/physical_gauged_matter_action_stress_prediction_tournament_cycle613_cold_2026_07_22.txt":"7d4c22cfc69aa44766ac60d9384a05cc32cd5cabd42b1c71333b66e771484901",
 "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py":"7aab3d6bc8d9d8b44263bca7a5cc308534269abb88094b2dfe0a820b12df2400",
 "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md":"6fe73ca79366ad75fd9499b820b4e3a49833ba6919a8c8cd3ef4d44e403da0e3",
 "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json":"5ba12c643c4f02355069e07dc4f8e7319bbb9374fd02a77505b9f635ef16135e",
 "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_cold_2026_07_22.txt":"80f69b699f955663609461e12f978500eb44f582092f6db0739b449161edbd0d",
 "scripts/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_2026_07_22.py":"aaa9e6b17bd5aa73172f7a2f19e3f4cf7c72d9542dce848947f7aa298e7af04b",
 "docs/work_history/repo/review_feedback/PHYSICAL_RATIONAL_REGGE_RECIPROCAL_RESPONSE_PREDICTION_BRIDGE_CYCLE604_NOTE_2026-07-22.md":"a5687b86e9a2bffa5177a68ec9093826eb4ba034bef6f721910f813717ac755b",
 "outputs/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_receipt_2026_07_22.json":"2fe20ba1ddbe304a11eb1809f76d552fdab89ff77d1c281d775d730c36021e90",
 "outputs/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_cold_2026_07_22.txt":"1e05bd4f2fde179760b6a5945f9765212e27c54920196e0e08ff5a742d64d5ed",
 "scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py":"91f22d23dd2730f76a05736634236d41036f68eaedc4921daca69de25ab6a344",
 "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md":"920776555dce6505bccb0e46e552e90d24858c08cfb7f6978d884f10a5bb0789",
 "outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json":"e7a8ea3dcbe370c9f8c6a94770508d1710a7013ce4ba62a1ad67e345fe1e2d11",
}
ACCEPTED_C613_RECEIPT_SHA256="36bf39b677e2330b1f345827c3cdcbfabd64af0acaeefb987031444db60671e3"
CAUSAL_TIME_PR_5557={"number":5557,"commit":"a1e2f1ea60b1cf9b9cb0ae100c61cfd1f3a07318",
 "path":"docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
 "content_sha256":"028133c490e771dd3012061c79910fcfb88cd6132df072ec15e725fe9bc35496"}
EXPECTED_NOTE_SHA256="58ceb8fcd82a808535ea2c7cc67084eec159255d4c38c368bbc2fa67b4c90a3f"
EXPECTED_RUNTIME_IMPORT_COUNT=64
EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256="b7cceb50db1a8714c68dc672f762b8076e29ec334c6167ba0b6eae9658249f73"


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


def runtime_import_closure():
 modules={path.stem:path for path in (ROOT/"scripts").glob("*.py")};entry=Path(__file__).resolve();visited=set()
 def visit(path):
  path=path.resolve()
  if path in visited:return
  visited.add(path);tree=ast.parse(path.read_text(encoding="utf-8"),filename=str(path))
  for node in ast.walk(tree):
   names=()
   if isinstance(node,ast.Import):names=tuple(alias.name.split(".")[0] for alias in node.names)
   elif isinstance(node,ast.ImportFrom) and node.module:names=(node.module.split(".")[0],)
   for name in names:
    if name in modules:visit(modules[name])
 visit(entry)
 return tuple(sorted(str(path.relative_to(ROOT)) for path in visited if path!=entry))


def runtime_import_controls():
 closure=runtime_import_closure();observed={path:digest(path) for path in closure}
 payload="".join(f"{path}\0{observed[path]}\n" for path in closure);manifest=sha256(payload.encode()).hexdigest()
 direct=("scripts/physical_gauged_matter_action_stress_prediction_tournament_cycle613_2026_07_22.py",
         "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py")
 return {"direct_runtime_imports":direct,"complete_runtime_import_closure":closure,
  "runtime_import_count":len(closure),"hidden_runtime_import_count":len(tuple(path for path in closure if path not in direct)),
  "observed_sha256":observed,"closure_manifest_sha256":manifest,
  "expected_closure_manifest_sha256":EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256,
  "pass":len(closure)==EXPECTED_RUNTIME_IMPORT_COUNT and all(path in closure for path in direct)
         and manifest==EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256}


def causal_pr_content_sha256():
 spec=f"{CAUSAL_TIME_PR_5557['commit']}:{CAUSAL_TIME_PR_5557['path']}"
 content=subprocess.check_output(("git","show",spec),cwd=ROOT)
 return sha256(content).hexdigest()


def cold_json(path,prefix):
 rows=[json.loads(line.removeprefix(prefix)) for line in (ROOT/path).read_text().splitlines() if line.startswith(prefix)]
 if len(rows)!=1:raise RuntimeError(f"{path} must contain one {prefix.strip()} row")
 return rows[0]


def check(label,condition,detail=""):
 global PASS,FAIL;PASS+=int(condition);FAIL+=int(not condition)
 print("PASS" if condition else "FAIL",label,"::",detail)


def shore():
 observed={path:digest(path) for path in PINS};imports=runtime_import_controls();note_sha=digest(str(NOTE.relative_to(ROOT)))
 r613=cold_json("outputs/physical_gauged_matter_action_stress_prediction_tournament_cycle613_cold_2026_07_22.txt","RECEIPT ")
 current_r613_path="outputs/physical_gauged_matter_action_stress_prediction_tournament_cycle613_receipt_2026_07_22.json"
 current_r613=json.loads((ROOT/current_r613_path).read_text());current_r613_sha=digest(current_r613_path)
 r576=json.loads((ROOT/"outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json").read_text())
 r604=json.loads((ROOT/"outputs/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_receipt_2026_07_22.json").read_text())
 r612=json.loads((ROOT/"outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json").read_text())
 c613a=r613["route_A_conditional_F17_link_gauge_algebra"];c613c=r613["route_C_divJ_monopole_compatibility_falsifier"]
 c576a=r576["route_A_actual_Regge_deficit_source"];c604c=r604["route_C_prediction_bridge"];local612c=r612["route_C_source_motion_ratio"]
 causal_sha=causal_pr_content_sha256()
 result={"direct_evidence_hashes_match":observed==PINS,"note_sha256":note_sha,
  "note_matches_frozen_hash":note_sha==EXPECTED_NOTE_SHA256,"runtime_import_closure":imports,
  "Cycle613":{"pass":r613["pass"],"tests":r613["tests_passed"],
   "divJ_coefficient_relative_residual":c613c["coefficient_relative_residual"],
   "divJ_source":"equal-six-direction periodic divJ=Ldelta/6 against the frozen Cycle604 graph-monopole comparator only",
   "physical_M2_evaluated":c613a["physical_M2_placement_packing_routing_constraints_or_leakage_evaluated"],
   "selected_metric_source_or_gravity":c613a["candidate_action_is_selected_metric_source_or_gravity"],
   "accepted_receipt_expected_sha256":ACCEPTED_C613_RECEIPT_SHA256,
   "accepted_receipt_recovered_from_accepted_cold_transcript":True,
   "current_receipt_observed_sha256":current_r613_sha,
   "current_receipt_matches_accepted_byte_hash":current_r613_sha==ACCEPTED_C613_RECEIPT_SHA256,
   "current_receipt_rewrite_science_fields_match_accepted":all((current_r613["runner_sha256"]==r613["runner_sha256"],
    current_r613["note_sha256"]==r613["note_sha256"],current_r613["pass"]==r613["pass"],
    current_r613["tests_passed"]==r613["tests_passed"],
    current_r613["route_C_divJ_monopole_compatibility_falsifier"]["coefficient_relative_residual"]==c613c["coefficient_relative_residual"])),
   "packaging_scope":"accepted runner/note/cold are pinned; the independent rerun rewrote only the live receipt bytes, so the accepted embedded cold receipt is used without editing Cycle613"},
  "Cycle576":{"pass":r576["pass"],"tests":r576["tests_passed"],
   "metric_Bianchi_residual":c576a["metric_Bianchi_residual"],"source_Ward_residual":c576a["local_deficit_source_Ward_residual"],
   "physical_generator_composed":c576a["physical_generator_composed_from_M2_primitives"],
   "physical_stress_or_Einstein_closed":r576["terminal"]["physical_stress_or_Einstein_equation_closed"],
   "sign_normalization_frame_selected":r576["terminal"]["source_sign_normalization_or_frame_preparation_selected"]},
  "Cycle604":{"pass":r604["pass"],"tests":r604["tests_passed"],
   "maximum_5_over_32pi_relative_residual":c604c["maximum_5_over_32pi_relative_residual"],
   "physical_interface":c604c["exact_cross_cycle_physical_interface_composed"],"comparison_is_gravity":c604c["comparison_is_gravity"]},
  "local_Cycle612":{"pass":r612["pass"],"tests":r612["tests_passed"],
   "identity":"local matter-caused causal-interval candidate on the current branch; not causal-time PR #5557",
   "source_to_response_map_derived":local612c["source_to_response_map_derived"],
   "delay_or_advance_selected":local612c["delay_or_advance_selected"],
   "empirical_normalization_selected":local612c["empirical_normalization_selected"]},
  "causal_time_PR_5557":{"number":CAUSAL_TIME_PR_5557["number"],"commit":CAUSAL_TIME_PR_5557["commit"],
   "path":CAUSAL_TIME_PR_5557["path"],"expected_content_sha256":CAUSAL_TIME_PR_5557["content_sha256"],
   "observed_content_sha256":causal_sha,"content_matches":causal_sha==CAUSAL_TIME_PR_5557["content_sha256"],
   "scope":"external comparison only: delay is rate-reachable and advance count-edit-reachable in that distinct lane",
   "runner_imported_or_executed":False,"backcredited_to_Cycle615":False}}
 shore_pass=(result["direct_evidence_hashes_match"] and result["note_matches_frozen_hash"] and imports["pass"]
  and all(result[name]["pass"] for name in ("Cycle613","Cycle576","Cycle604","local_Cycle612"))
  and result["Cycle613"]["accepted_receipt_recovered_from_accepted_cold_transcript"]
  and result["Cycle613"]["current_receipt_rewrite_science_fields_match_accepted"]
  and result["Cycle613"]["divJ_coefficient_relative_residual"]==1 and not result["Cycle613"]["physical_M2_evaluated"]
  and not result["Cycle613"]["selected_metric_source_or_gravity"] and not result["Cycle576"]["physical_generator_composed"]
  and not result["Cycle576"]["physical_stress_or_Einstein_closed"] and not result["Cycle576"]["sign_normalization_frame_selected"]
  and not result["Cycle604"]["physical_interface"] and not result["Cycle604"]["comparison_is_gravity"]
  and not result["local_Cycle612"]["source_to_response_map_derived"] and not result["local_Cycle612"]["delay_or_advance_selected"]
  and result["causal_time_PR_5557"]["content_matches"] and not result["causal_time_PR_5557"]["backcredited_to_Cycle615"])
 check("accepted C613 and current C576/C604/local-C612 evidence are pinned with the distinct causal PR boundary",shore_pass,result)
 return r613,r576,r604,r612,result


def note_contract():
 body=" ".join(NOTE.read_text().lower().replace("`","").replace("*","").split())
 required=("authority: none","audit: unset","author artifact status accepted: false","cycle 615","opposite-charge candidate sector",
  "route a","route b","route c","local neutral-pair","resource debit","4096","full coin","contact","gauss",
  "open boundary","boundary flux","translation covariance","gauge–regge","coframe variation","receiver-label equivalence",
  "improvement","sign","scale","5/(32pi)","divj","l3","l5","l6","l7","all 24","576",
  "inverse","deletion","physical leakage unevaluated","f17 is not energy or stress","joined algebra is not gravity",
  "local cycle612","pr #5557","no back-credit","n1 —","n2 —","n3 —","n4 —","n5 —",
  "n6 —","n7 —","n8 —","fail / do not ship negative","narrowed positive: pass","no axiom pressure")
 missing=tuple(item for item in required if item not in body)
 check("Cycle615 note freezes domains, alternatives, and N1-N8 scope",not missing,missing)


# ---------- Route A: opposite-charge candidate sector and resource-debited pair rule ----------
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
               "F17_array_domain_escape_count":0,"physical_code_leakage_evaluated":False})
 output={"object":"declared opposite-charge six-mode CAR copy plus one resource role and a neutral-pair candidate rule",
  "disposition":"CONSTRUCTIVE_RESOURCE_DEBITED_OPPOSITE_CHARGE_PAIR_ALGEBRA; PHYSICAL_SECTOR_AND_PAIR_GATE_LOWERING_OPEN",
  "pair_rule":"one neutral genesis-resource excitation is reversibly swapped with the cubic scalar sum 6^-1/2 sum_d a_d^dag b_-d^dag",
  "sector_status":"the opposite-charge copy, conjugated coin, separate same-g contact and no cross-contact term are supplied candidate-law content; no physical particle identity is derived",
  "declared_additional_coarse_roles_per_cell":7,
  "declared_role_debit":"six opposite-charge CAR occupation roles plus one neutral resource role; these are not counted as physical M2s",
  "physical_M2_cost_per_coarse_cell":None,"physical_support_two_pair_gate_executed":False,
  "physical_E_and_G_composition_evaluated":False,"physical_code_leakage_residual":None,
  "physical_joint_nearest_neighbor_sector_compiler_executed":False,
  "resource_excitation_supplied_at_encoding":True,
  "pair_gate_unitarity_residual":unitary,"pair_gate_inverse_residual":inverse,"resource_remaining_after_genesis":creation,
  "created_pair_norm_residual":pair_norm,"genesis_omission_signal":omission,
  "maximum_all24_pair_gate_covariance_residual":covariance,"all576_pair_representation_failures":group_failures,
  "pair_gate_local_U1_gauge_commutator_residual":0.0,
  "positive_local_cubic_controls":cubic,"positive_Fock_U1_controls":symmetry,
  "negative_Fock_U1_controls":negative_symmetry,
  "negative_coin_all24_covariance_residual":negative_coin_cubic,"rows":rows,
  "maximum_opposite_charge_gauge_residual":max_gauge,"maximum_Fock_control_residual":max_fock,
  "maximum_pair_branch_or_expectation_residual":max_branch,"minimum_current_deletion_signal":min_delete,
  "basiswise_4096_field_update_is_one_coherent_physical_matter_field_update":False,
  "cubic_pair_expectation_is_monopole_source":False,"neutral_compiler_words_charged":False,
  "candidate_sector_has_derived_physical_particle_identity":False}
 check("Route A reexecutes the resource-debited pair algebra and all 4096 opposite-charge Gauss words",
       max(unitary,inverse,creation,pair_norm,covariance,negative_coin_cubic,max_gauge,max_fock,max_branch,
           *cubic.values(),negative_symmetry["coin_total_number_commutator"],
           negative_symmetry["contact_total_number_commutator"],negative_symmetry["gauged_contact_invariance_residual"])<TOL
       and group_failures==0 and min_delete>0 and omission>0
       and all(row["Fock_controls"]["joint_local_occupation_words_exhausted"]==4096 for row in rows),output)
 check("Route A records seven coarse roles without asserting physical M2/support-two/joint-NN lowering",
       output["declared_additional_coarse_roles_per_cell"]==7 and output["physical_M2_cost_per_coarse_cell"] is None
       and not output["physical_support_two_pair_gate_executed"] and output["physical_code_leakage_residual"] is None
       and not output["physical_joint_nearest_neighbor_sector_compiler_executed"]
       and not output["neutral_compiler_words_charged"]
       and not output["candidate_sector_has_derived_physical_particle_identity"]
       and not output["cubic_pair_expectation_is_monopole_source"],output)
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
def translate_edges(edges,offset):return {(add_coord(a,offset),add_coord(b,offset)):value for (a,b),value in edges.items()}


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
 coordinates=np.asarray(sorted({site for edge in edges for site in edge}),dtype=np.int64)
 for first in frames:
  for second in frames:
   direct=coordinates@(first@second).T
   composed=(coordinates@second.T)@first.T
   failures+=int(not np.array_equal(direct,composed))
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
 coin=c219.common_species(c230.BETA).coin;rows=[];max_gauss=max_inverse=max_gauge=max_cov=0;min_delete=math.inf;min_translation_loss=math.inf;groups=0
 local_controls=c613.local_coin_contact_cubic_controls(coin);fock_controls=c611.fock_symmetry_controls(coin)
 for label,length,held in OPEN_FIXTURES:
  radius=(length-1)//2;flux=axial_open_flux(radius);div=open_divergence(flux,radius)
  gauss=max(min((value-(1 if site==(0,0,0) else 0))%c609.MOD,
                ((1 if site==(0,0,0) else 0)-value)%c609.MOD) for site,value in div.items())
  boundary=sum(value for (source,target),value in flux.items() if not in_cube(target,radius))%c609.MOD
  covariance=max(int(rotate_edges(flux,frame)!=flux) for frame in c210.proper_cubic_frames())
  translated=translate_edges(flux,(1,0,0));translation_loss=len(set(flux.items())^set(translated.items()))
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
  min_translation_loss=min(min_translation_loss,translation_loss)
  rows.append({"fixture":label,"length":length,"held":held,"centered_cube_radius":radius,
   "F17_flux_per_cubic_boundary_port":pow(6,-1,c609.MOD),"interior_Gauss_residual":gauss,
   "boundary_total_flux_mod17":boundary,"charge_move_Gauss_residual":moved,"charge_move_inverse_residual":inverse,
   "reflecting_stream_inverse_residual":stream_inverse,"open_gauge_covariance_residual":gauge,
   "all24_open_stream_or_flux_covariance_residual":max(covariance,frame_cov),
   "deleted_boundary_port_Gauss_signal":delete_signal,"deleted_boundary_total_flux_signal":delete_boundary,
   "one_site_translation_loss_signal":translation_loss,
   "interior_positive_link_words":3*(length-1)*length*length,"outward_boundary_port_words":6*length*length,
   "F17_array_domain_escape_count":0,"physical_code_leakage_evaluated":False})
 output={"object":"centered finite open cube with six equal axial F17 flux rays from one unit charge",
  "disposition":"CONSTRUCTIVE_OPEN_DOMAIN_LOCAL_GAUSS_CLOSURE; BOUNDARY_SELECTION_AND_TRANSLATION_IMPORT_EXPLICIT",
  "flux_selection":"within the supplied equal six-axial-ray ansatz, proper-cubic equality plus Gauss fixes each port flux to 6^-1=3 mod17",
  "boundary_condition":"finite centered odd cube, reflecting matter stream, six axial outward flux paths",
  "rows":rows,"maximum_Gauss_residual":max_gauss,"maximum_inverse_residual":max_inverse,
  "maximum_open_gauge_covariance_residual":max_gauge,"maximum_all24_covariance_residual":max_cov,
  "all576_open_edge_representation_failures":groups,"minimum_boundary_deletion_signal":min_delete,
  "minimum_one_site_translation_loss_signal":min_translation_loss,
  "full_local_coin_contact_controls":local_controls,"full_local_Fock_U1_controls":fock_controls,
  "isolated_unit_charge_lawful_on_declared_open_array_domain":True,"compensator_used":False,
  "neutral_compiler_words_charged":False,"translation_covariant":False,
  "flux_unique_among_all_open_Gauss_solutions":False,"divergence_free_flux_loops_unselected":True,
  "bulk_or_gravity_law_claimed":False,"boundary_center_ports_and_flux_genesis_supplied":True,
  "physical_M2_boundary_or_link_roles_counted":None,"physical_support_two_gates_executed":False,
  "physical_joint_nearest_neighbor_compiler_executed":False,"physical_code_leakage_residual":None}
 check("Route B closes local Gauss on centered open L3/L5/L7 domains with selected equal port flux and exact controls",
       max(max_gauss,max_inverse,max_gauge,max_cov,*local_controls.values(),fock_controls["coin_total_number_commutator"],
           fock_controls["contact_total_number_commutator"],fock_controls["gauged_contact_invariance_residual"])<TOL
       and groups==0 and min_delete>0 and min_translation_loss>0
       and all(row["boundary_total_flux_mod17"]==1 and row["F17_flux_per_cubic_boundary_port"]==3 for row in rows),output)
 check("Route B exposes the open boundary/center import and makes no translation-covariant bulk or gravity claim",
       output["isolated_unit_charge_lawful_on_declared_open_array_domain"] and not output["translation_covariant"]
       and output["physical_M2_boundary_or_link_roles_counted"] is None
       and not output["physical_support_two_gates_executed"] and output["physical_code_leakage_residual"] is None
       and not output["physical_joint_nearest_neighbor_compiler_executed"]
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
 receiver_labels=sorted({row["probe_over_reference"] for row in r612["route_C_source_motion_ratio"]["rows"]
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
 output={"object":"conditional algebraic sum of the reexecuted gauge/Gauss family and actual-Regge deficit/coframe response",
  "disposition":"CONSTRUCTIVE_CONDITIONAL_GAUGE_REGGE_RESPONSE_FAMILY; PHYSICAL_JOIN_AND_RECEIVER_SELECTION_OPEN",
  "supplied_joined_functional":"A_join=A_Cycle613_candidate[psi,Q,E]+c_R A_Regge[e]-lambda sum_x rho_candidate(x) sum_local_hinges delta_hinge[e]",
  "variation_identifications":{"gauge_side":"Cycle615 Routes A/B reexecute charge continuity and Gauss-array identities",
   "coframe_edge_variation":"Cycle576 actual-Regge Hessian plus deficit-source row is reexecuted numerically",
   "receiver":"source-conjugate Regge quadrature compared only to declared labels from local Cycle612"},
  "exact_continuous_equivalence_class":{"relative_source_coupling":"lambda in R (including zero and both signs)","equation_of_motion_exact_local_improvement":"c in R","receiver_family":"R(lambda,c)=lambda*(R0+c*Rimp) for each frozen momentum"},
  "audited_equivalence_grid":{"relative_coupling_magnitudes":[1,2],"coupling_signs":[-1,1],"local_conserved_improvement_coefficients":[-1,0,1],"members_per_fixture":12},
  "rows":rows,"maximum_stationary_equation_residual":max_stationary,"maximum_source_Ward_residual":max_ward,
  "maximum_coframe_variation_residual":max_variation,"maximum_all24_response_covariance_residual":max_cov,
  "all576_metric_representation_failures":group_failures,"maximum_finite_state_inverse_residual":max_inverse,
  "minimum_source_deletion_signal":min_delete,"enumerated_receiver_signs":signs,"enumerated_receiver_span":span,
  "maximum_analytic_family_residual_on_audited_grid":max_formula,
  "local_Cycle612_declared_receiver_label_equivalence_class":receiver_labels,
  "receiver_label_selection_residual":len(receiver_labels)-1,
  "local_Cycle612_receiver_M2_key_used_as_declared_role_flag_not_independently_validated_physical_M2":True,
  "local_Cycle612_source_to_response_map_derived":r612["route_C_source_motion_ratio"]["source_to_response_map_derived"],
  "local_Cycle612_delay_or_advance_selected":r612["route_C_source_motion_ratio"]["delay_or_advance_selected"],
  "Cycle604_5_over_32pi_maximum_relative_residual":r604["route_C_prediction_bridge"]["maximum_5_over_32pi_relative_residual"],
  "Cycle613_exact_source_shore_pair":{"source":"equal-six-direction periodic divJ=Ldelta/6",
   "shore":"frozen Cycle604 graph-monopole 5/(32pi) comparator",
   "coefficient_relative_residual":r613["route_C_divJ_monopole_compatibility_falsifier"]["coefficient_relative_residual"],
   "used_to_close_other_source_routes":False},
  "parameters_refit":0,"absolute_action_or_source_normalization_selected":False,
  "improvement_selected":False,"response_sign_selected":False,"operational_metric_identification_derived":False,
  "open_boundary_and_periodic_Bloch_Regge_joint_real_space_compiler_executed":False,
  "domain_join_status":"Route B uses a finite centered open cube while the Regge response uses periodic Bloch symbols; no open-domain Regge operator or shared real-space boundary apparatus is compiled",
  "physical_joint_M2_E_and_G_evaluated":False,"physical_support_two_join_gates_evaluated":False,
  "physical_joint_nearest_neighbor_compiler_evaluated":False,"physical_joint_code_leakage_residual":None,
  "causal_time_PR_5557_boundary":{"identity":"distinct causal-time lane, not local Cycle612",
   "commit":CAUSAL_TIME_PR_5557["commit"],"comparison_only":True,
   "delay_rate_reachable_and_advance_count_edit_reachable_in_that_lane":True,
   "Cycle615_implements_Event_or_count_edit":False,"runner_imported_or_executed":False,"backcredited":False},
  "receiver_alternatives_are_Event_or_Record":False,"Regge_generator_called_rate":False,
  "F17_is_physical_energy_or_stress":False,"joined_algebra_is_gravity":False}
 check("Route C reexecutes the conditional gauge-Regge response family with Ward/covariance/inverse/deletion controls",
       max(max_stationary,max_ward,max_cov,max_variation,max_inverse,max_formula)<TOL and min_delete>0 and group_failures==0
       and all(len(row["allowed_alternatives"])==12 and row["parameters_refit"]==0 for row in rows),output)
 check("Route C returns the exact local-Cycle612 receiver-label equivalence without Event/Record or physical-M2 back-credit",
       signs==[-1,1] and span>0 and receiver_labels==["3/4","5/4"]
       and output["receiver_label_selection_residual"]==1
       and not output["local_Cycle612_source_to_response_map_derived"] and not output["response_sign_selected"]
       and output["Cycle613_exact_source_shore_pair"]["coefficient_relative_residual"]==1
       and not output["Cycle613_exact_source_shore_pair"]["used_to_close_other_source_routes"]
       and output["physical_joint_code_leakage_residual"] is None
       and not output["causal_time_PR_5557_boundary"]["backcredited"],output)
 return output


def no_go_discipline():
 families=[
  {"route":"resource-debited neutral-pair algebra","attempt":"swap one declared resource role with a cubic scalar of opposite-charge directional pairs","mechanism":"seven-dimensional involution","terminal_obligation":"unitarity, inverse, cubic covariance, and nonzero resource-deletion response","result":"algebraic terminal passes; no physical gate lowering follows","citation":"scripts/physical_lawful_charge_joined_metric_response_tournament_cycle615_2026_07_22.py:210","marker":"ATTEMPTED"},
  {"route":"full opposite-charge occupation audit","attempt":"enumerate both 64-word local occupation spaces","mechanism":"oriented plus/minus continuity and reciprocal F17 current debit","terminal_obligation":"4096-word continuity, Gauss-word preservation, inverse, deletion, and gauge covariance","result":"array terminal passes; coherent physical joint update remains unevaluated","citation":"scripts/physical_lawful_charge_joined_metric_response_tournament_cycle615_2026_07_22.py:260","marker":"ATTEMPTED"},
  {"route":"centered open-boundary flux","attempt":"route equal flux from one center to six boundary ports","mechanism":"open divergence plus proper-cubic equality","terminal_obligation":"unit central Gauss source, inverse, gauge covariance, deletion, and explicit translation loss","result":"passes on declared centered cubes with supplied boundary and flux genesis","citation":"scripts/physical_lawful_charge_joined_metric_response_tournament_cycle615_2026_07_22.py:430","marker":"ATTEMPTED"},
  {"route":"conditional gauge-Regge coframe response","attempt":"couple the candidate charge amplitude to the actual-Regge deficit row","mechanism":"pseudoinverse response in the Ward-compatible quotient","terminal_obligation":"stationary equation, coframe derivative, all24 covariance, finite-state inverse, and analytic response family","result":"passes as periodic Bloch algebra while the open-boundary real-space join remains unevaluated","citation":"scripts/physical_lawful_charge_joined_metric_response_tournament_cycle615_2026_07_22.py:520","marker":"ATTEMPTED"},
  {"route":"local-Cycle612 receiver-label comparison","attempt":"carry every scale/sign/improvement response to the two declared local labels","mechanism":"source-conjugate Regge quadrature and label-set comparison","terminal_obligation":"exact response-family formula and no-refit label equivalence","result":"both labels survive; no source-to-response selection, physical receiver validation, Event, or Record follows","citation":"scripts/physical_lawful_charge_joined_metric_response_tournament_cycle615_2026_07_22.py:610","marker":"ATTEMPTED"},
  {"route":"periodic equal-six-direction divJ source","attempt":"compare divJ=Ldelta/6 with the Cycle604 graph-monopole shore","mechanism":"exact local Laplacian source","terminal_obligation":"the named source/shore compatibility test only","result":"coefficient-relative residual one for that exact pair; no other source route is closed","citation":"scripts/physical_gauged_matter_action_stress_prediction_tournament_cycle613_2026_07_22.py:541","marker":"RULED OUT BY PRIOR"},
 ]
 live_routes=["literal physical M2 and support-two lowering of the resource/pair sector",
              "dynamical boundary membrane or flux-genesis law with translation audit",
              "one open-domain real-space Regge operator joined to Route B",
              "quasienergy or full-unitary coframe variation",
              "local receiver-feedback law that selects one response member without Event/Record back-credit"]
 walls={
  "W_sector_definition":"opposite-charge copy, conjugated coin, contact choice, resource role, and pair rule are supplied",
  "W_physical_lowering":"physical M2 cost, support-two gates, E/G, joint NN schedule, constraints, and leakage are unevaluated",
  "W_boundary":"finite center, boundary ports, reflecting rule, and flux-state genesis are supplied and break translation covariance",
  "W_domain_join":"open Route B and periodic-Bloch Regge response are not one real-space apparatus",
  "W_response_class":"Regge coupling magnitude/sign and conserved-improvement coefficient are unselected",
  "W_receiver_map":"local Cycle612 labels and its physical-role flags are not a derived joint receiver map",
  "W_event":"causal-time PR #5557 is distinct and supplies no Event/Record back-credit to Cycle615",
 }
 names=tuple(walls);pairs=[{"left":names[i],"right":names[j],
  "left_to_right":{"status":"NOT_ESTABLISHED","reason":f"no intervention closes {names[i]} and retests {names[j]}"},
  "right_to_left":{"status":"NOT_ESTABLISHED","reason":f"no intervention closes {names[j]} and retests {names[i]}"},
  "independence":{"status":"NOT_ESTABLISHED","reason":"neither directional closure experiment was executed"}}
  for i in range(len(names)) for j in range(i+1,len(names))]
 phrases=("we assume","by construction","as is standard","the framework provides","bridge context","background",
          "naturally","obviously","standard qft","registered","canonical")
 note_text=" ".join(NOTE.read_text().lower().split());hits=[phrase for phrase in phrases if phrase in note_text]
 n4=[
  {"prior_path":"scripts/physical_gauged_matter_action_stress_prediction_tournament_cycle613_2026_07_22.py","prior_line":541,
   "prior_residual":"equal-six-direction periodic divJ=Ldelta/6 versus frozen graph-monopole shore","current_residual":"the same exact source/shore pair carried without extension","witness_residual":1.0,"match":True,"same_scope":True,"use_as_closure":True},
  {"prior_path":"scripts/physical_rational_regge_reciprocal_response_prediction_bridge_cycle604_2026_07_22.py","prior_line":1105,
   "prior_residual":"5/(32pi) graph-monopole comparator residual","current_residual":"comparator in the preserved C613 divJ pair","witness_residual":0.001748688020904332,"match":True,"same_scope":True,"use_as_closure":True},
  {"prior_path":"scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py","prior_line":477,
   "prior_residual":"actual-Regge metric Bianchi and deficit-source Ward identities","current_residual":"same periodic Regge Hessian/source row used in the Cycle615 response family","witness_residual":1.1216352294406378e-15,"match":True,"same_scope":True,"use_as_closure":True},
  {"prior_path":"scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py","prior_line":580,
   "prior_residual":"local Cycle612 source-to-response map not derived","current_residual":"both local receiver labels survive Cycle615 response alternatives","witness_residual":"PERSISTS","match":True,"same_scope":True,"use_as_closure":False},
  {"prior_path":"scripts/physical_gauged_matter_action_stress_prediction_tournament_cycle613_2026_07_22.py","prior_line":391,
   "prior_residual":"physical M2 placement/packing/routing/constraints/leakage unevaluated","current_residual":"Cycle615 coarse pair, open flux, and joined response remain without literal physical lowering","witness_residual":"PERSISTS","match":True,"same_scope":True,"use_as_closure":False},
  {"prior_path":"a1e2f1ea60b1cf9b9cb0ae100c61cfd1f3a07318:docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md","prior_line":29,
   "prior_residual":"delay rate-reachable while advance is count-edit-reachable in causal-time PR #5557","current_residual":"Cycle615 implements no count edit, Event, or Record","witness_residual":"DISTINCT_LANE","match":True,"same_scope":False,"use_as_closure":False},
 ]
 n5=[
  {"claim":"the opposite-charge candidate algebra does not derive a physical particle identity","per_element":"charge signs and conjugated coin entries are supplied","per_site":"the seven-dimensional pair rule is a declared local-role map","per_mode":"six opposite-direction pairs are exhausted","per_block":"both 64-word sectors are enumerated but no physical encoder is composed","lattice_wide":"no interacting identity, genesis law, or empirical species calibration is derived"},
  {"claim":"the seven coarse roles are not a physical M2/support-two compiler","per_element":"role bits are not mapped to M2 primitives","per_site":"the pair involution has no literal support-two decomposition","per_mode":"directional currents are host arrays","per_block":"physical E/G, constraints, and leakage are unevaluated","lattice_wide":"no routed joint nearest-neighbor schedule exists"},
  {"claim":"the centered open flux is not a translation-covariant bulk source law","per_element":"each F17 port word belongs to a supplied ray","per_site":"one selected center carries the unit source","per_mode":"six equal rays are a supplied ansatz","per_block":"finite reflecting boundary and port genesis are supplied","lattice_wide":"one-site translation changes the edge set and no dynamical boundary law is executed"},
  {"claim":"the gauge-Regge response algebra is not selected physical stress, rate, or gravity","per_element":"F17 and Regge coefficients are supplied","per_site":"no shared open-domain Regge operator is built","per_mode":"the response uses periodic Bloch modes","per_block":"lambda, sign, and improvement remain an exact family","lattice_wide":"no physical joined compiler, receiver calibration, or unique source law is selected"},
  {"claim":"the receiver alternatives are not Events or Records","per_element":"3/4 and 5/4 are inherited labels","per_site":"the local Cycle612 physical-role key is not independently revalidated","per_mode":"both signs survive","per_block":"no source-to-response selection is derived","lattice_wide":"causal-time PR #5557 is a distinct comparison lane and supplies no back-credit"},
 ]
 n6=[
  {"file":"docs/work_history/repo/review_feedback/PHYSICAL_GAUGED_MATTER_ACTION_STRESS_PREDICTION_TOURNAMENT_CYCLE613_NOTE_2026-07-22.md","status":"PINNED_EXECUTED_PARENT","closure":"supplies only the conditional gauge algebra and exact divJ source/shore falsifier"},
  {"file":"outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json","status":"PINNED_AND_RUNTIME_REEXECUTED_REGGE_EVIDENCE","closure":"supplies periodic Regge Hessian/Bianchi/Ward formulas while physical lowering, sign, normalization, stress, and Einstein identity remain open"},
  {"file":"outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json","status":"PINNED_LOCAL_CYCLE612_LABEL_COMPARATOR","closure":"supplies two declared receiver-label rows but no source-to-response or delay/advance selection"},
  {"file":"a1e2f1ea60b1cf9b9cb0ae100c61cfd1f3a07318:docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md","status":"PINNED_EXTERNAL_CAUSAL_TIME_PR_5557_COMPARISON_NOT_EXECUTED","closure":"keeps delay rate reachability and advance count-edit reachability separate; provides no Cycle615 Event/Record or physical-time back-credit"},
  {"file":"docs/work_history/repo/review_feedback/PHYSICAL_LAWFUL_CHARGE_JOINED_METRIC_RESPONSE_TOURNAMENT_CYCLE615_NOTE_2026-07-22.md","status":"CURRENT_NARROWED_ARTIFACT","closure":"queues literal pair lowering, dynamical boundary genesis, open-domain Regge joining, and receiver feedback as live implementation paths"},
 ]
 n8=[
  {"cycle":"Cycle576","echo":"Regge Bianchi/Ward algebra passed with sign, scale, frame preparation and physical metric open","effect":"supports the response calculation without physical identification"},
  {"cycle":"Cycle604","echo":"the graph-monopole comparator is numerical and lacks a physical cross-cycle interface","effect":"limits the divJ result to its exact comparator"},
  {"cycle":"Cycle611","echo":"a paid opposite carrier closed a role-array zero mode conditionally but left genesis and physical lowering open","effect":"prevents the declared pair rule from receiving autonomous-genesis credit"},
  {"cycle":"Cycle613","echo":"conditional gauge/Gauss algebra passed and left open flux/opposite charge live","effect":"permits Routes A/B while retaining physical compiler walls"},
  {"cycle":"local Cycle612","echo":"two response labels exist without a derived source-to-response map","effect":"the Cycle615 equivalence remains two-valued"},
  {"cycle":"causal-time PR #5557","echo":"delay and advance use distinct rate/edit mechanisms","effect":"comparison only; no Event, Record, or count-edit mechanism is imported"},
 ]
 allowed={"ATTEMPTED","RULED OUT BY PRIOR"};markers=all(row["marker"] in allowed for row in families)
 independence_complete=all(row["independence"]["status"]=="ESTABLISHED" for row in pairs)
 output={"N1_normalized_families":families,"N1_allowed_markers":sorted(allowed),"N1_marker_schema_pass":markers,
  "N1_live_routes":live_routes,"N2_pairwise_wall_closure_and_independence":pairs,"N2_independence_complete":independence_complete,
  "N3_canonical_hidden_wall_phrases":list(phrases),"N3_note_phrase_hits":hits,
  "N3_explicit_supplied_structure":["opposite-charge copy","conjugated coin","same-g/no-cross-contact choice","resource role","pair rule","F17 modulus and representation","boundary/center/ports/reflecting rule/flux state","Regge complex/frame state/lambda/update parameter","improvement formula and pseudoinverse","local Cycle612 labels","aggregate execution"],
  "N4_exact_residual_matching":n4,"N5_five_resolution_rhetoric_audit":n5,"N6_partial_closure_paths":n6,
  "N7_cited_actionable_steelman":{"citation":"scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py:472-501; scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py:518-581; scripts/physical_gauged_matter_action_stress_prediction_tournament_cycle613_2026_07_22.py:379-393","action":"lower the pair sector to literal physical primitives, derive a dynamical boundary state, build one open-domain real-space Regge operator, and add a reversible local receiver-feedback term that selects one response member while preserving Gauss/Regge Ward and held-size controls"},
  "N8_rowwise_cross_cycle_echo":n8,"walls":walls,"Status":"FAIL / DO NOT SHIP NEGATIVE",
  "negative_gate_reasons":["five constructive implementation routes remain live","pairwise wall independence is not established"],
  "narrowed_positive_artifact_status":"PASS","negative_claim_shipped":False,
  "shared_obstruction":False,"minimum_content_claim":False,"axiom_pressure":False}
 check("full N1-N8 gate blocks broad negative, minimum-content, and axiom-pressure claims",
       len(families)>=5 and markers and len(live_routes)>0 and len(pairs)==21 and not independence_complete and not hits
       and all(all(field in row for field in ("prior_path","prior_line","match","same_scope","use_as_closure")) for row in n4)
       and all(all(field in row for field in ("per_element","per_site","per_mode","per_block","lattice_wide")) for row in n5)
       and all(all(field in row for field in ("file","status","closure")) for row in n6)
       and all(all(field in row for field in ("cycle","echo","effect")) for row in n8)
       and output["Status"]=="FAIL / DO NOT SHIP NEGATIVE" and output["narrowed_positive_artifact_status"]=="PASS"
       and not output["negative_claim_shipped"] and not output["shared_obstruction"]
       and not output["minimum_content_claim"] and not output["axiom_pressure"],output)
 return output


def main():
 r613,r576,r604,r612,shore_result=shore();note_contract();a=route_a();gc.collect();b=route_b();gc.collect();c=route_c(r613,r576,r604,r612);nogo=no_go_discipline()
 elapsed=perf_counter()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rss=int(rss if sys.platform=="darwin" else rss*1024)
 receipt={"cycle":615,"authority":AUTHORITY,"audit":AUDIT,
  "author_artifact_status_accepted":AUTHOR_ARTIFACT_STATUS_ACCEPTED,
  "audit_verdict_inferred_from_dependencies":AUDIT_VERDICT_INFERRED_FROM_DEPENDENCIES,
  "constitutional_effect":"none",
  "HEAD":subprocess.check_output(("git","rev-parse","HEAD"),cwd=ROOT,text=True).strip(),"pins":PINS,"shore":shore_result,
  "runner_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),"note_sha256":sha256(NOTE.read_bytes()).hexdigest(),
  "runtime_import_controls":shore_result["runtime_import_closure"],
  "foundation_recon":{"scope":"read-only","claim":"the opposite-charge copy, pair rule, resource role, open boundary, flux state, Regge coefficients, improvement, and receiver labels are explicit candidate imports rather than foundation consequences"},
  "route_A_local_neutral_pair_sector":a,"route_B_open_boundary_flux":b,"route_C_joined_metric_receiver_equivalence":c,
  "no_go_discipline":nogo,
  "decisive_answer":"three conditional families survive reexecution. The declared seven-role pair map and all 4096 opposite-charge occupation words preserve the tested charge/Gauss arrays; the centered open cubes carry one unit of F17 boundary flux and explicitly lose translation covariance; and the periodic Regge coframe response has the exact family R(lambda,c)=lambda*(R0+c Rimp), leaving both local-Cycle612 labels. None is a literal physical joined compiler or a unique source/stress/gravity law.",
  "inventory":{"supplied":["opposite-charge six-mode copy and conjugated coin","separate same-g contact and absence of cross contact","one neutral resource role and seven-dimensional pair rule","F17 modulus, unit representation, current sign and update order","finite centered boundary, ports, reflecting rule and flux state","Cycle576 Regge complex, frame state, source coupling and update parameter","spatial-trace improvement and pseudoinverse representative","local Cycle612 label rows","causal-time PR #5557 comparison boundary","aggregate rather than physical joint execution"],
   "derived_or_executed":["resource-debited pair involution and cubic covariance","4096-word plus/minus continuity, Gauss-array and inverse audit","opposite Peierls gauge covariance","equal open flux 3 mod17 within the six-ray ansatz","open reflecting-stream gauge covariance and explicit one-site translation loss","periodic Regge stationary/coframe response family","analytic response formula on 36 representatives","all24/all576, held-size, inverse and deletion controls"],
   "not_derived":["physical particle identity of the opposite-charge copy","physical M2 cost or primitive composition","support-two pair gates, physical E/G, local constraints, joint NN routing, or physical leakage","autonomous boundary/flux genesis or translation-covariant bulk source","one open-domain real-space Regge join","unique coupling magnitude/sign/improvement or physical stress/source","physical receiver map or one selected receiver label","Regge rate, Event, Record, causal time, Born probability, or gravity"]},
  "physical_lowering_audit":{"Route_A_physical_M2_cost":None,"Route_A_support_two_gate":False,"Route_A_physical_EG":False,"Route_A_physical_leakage":None,"Route_A_joint_NN":False,
   "Route_B_physical_M2_cost":None,"Route_B_support_two_gate":False,"Route_B_physical_leakage":None,"Route_B_joint_NN":False,
   "Route_C_physical_M2_cost":None,"Route_C_support_two_gate":False,"Route_C_physical_EG":False,"Route_C_physical_leakage":None,"Route_C_joint_NN":False},
  "Cycle612_identity_boundary":{"local_Cycle612":"current-branch matter-caused causal-interval receipt used only for declared receiver labels; its source-to-response map and delay/advance selection are false",
   "causal_time_PR_5557":"distinct remote lane at a1e2f1ea60; comparison-only delay/rate and advance/count-edit scope",
   "causal_PR_runner_imported_or_executed":False,"causal_PR_Event_Record_or_time_backcredit":False},
  "six_wall_ledger":{"C_ref":"SHARPENED CONDITIONALLY: pair and centered flux arrays are proper-cubic; center/boundary, Regge frame state, response sign, improvement and receiver map remain supplied","C_num":"ADVANCED ALGEBRAICALLY: all 4096 signed occupation ledgers and equal port word 3 mod17 are explicit; physical charge scale and encoding remain open","C_wrap":"UNCHANGED PHYSICALLY: F17 arithmetic is exact but is not energy, stress, rate or time","C_int":"PARTIAL CONDITIONAL COMPOSITION: pair, open-flux and periodic Regge response families coexist in one runner; no open-domain physical joint apparatus is compiled","C_local":"ADVANCED AT ROLE/ARRAY LEVEL: inverse, covariance, deletion and held sizes pass; physical M2, support-two, E/G, constraints, routing and leakage remain unevaluated","C_source":"ROUTE-SPECIFIC PROGRESS: open flux supports one centered unit array charge and the exact Regge response family reaches both local labels; divJ remains falsified only for its exact source/shore pair"},
  "maturity_effect":"no maturity scores retained or increased; current evidence was not independently sufficient for a strict physical or unique-law promotion",
  "strongest_constructive_result":"one resource-debited seven-role pair involution and all 4096 signed occupation words preserve the tested local charge/Gauss arrays, while an independent centered open construction carries exact unit boundary flux with measured translation loss",
  "confirmed_breakthrough":False,"negative_claim_shipped":False,"shared_obstruction_or_axiom_pressure":False,
  "optimal_next_campaign":"lower the pair sector to literal physical primitives, derive the boundary state dynamically, build one open-domain real-space Regge operator, and add a reversible receiver-feedback law that selects one response member on held domains",
  "tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,"pass":FAIL==0,"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,
  "runtime_environment":{"python":sys.version.split()[0],"numpy":np.__version__}}
 RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=json_default)+"\n")
 print("RECEIPT",json.dumps(receipt,sort_keys=True,default=json_default))
 print("SUMMARY",json.dumps({"pass":receipt["pass"],"tests_passed":PASS,"tests_failed":FAIL,"elapsed_seconds":elapsed,
  "route_A":a["disposition"],"route_B":b["disposition"],"route_C":c["disposition"],
  "receiver_label_equivalence":c["local_Cycle612_declared_receiver_label_equivalence_class"],"axiom_pressure":False},sort_keys=True))
 return int(FAIL!=0)


if __name__=="__main__":
 if "--cold" in sys.argv:
  buffer=io.StringIO()
  with contextlib.redirect_stdout(buffer):exit_code=main()
  transcript=buffer.getvalue();COLD.write_text(transcript,encoding="utf-8");print(transcript,end="")
  raise SystemExit(exit_code)
 raise SystemExit(main())
