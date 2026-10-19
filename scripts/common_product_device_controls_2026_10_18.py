#!/usr/bin/env python3
"""Finite algebra, geometry and explicit-budget controls for eight supplied devices.
General source/tail estimates remain the complete bound proofs; no historical
review outcome supplies an assertion, and no enormous prescribed device is simulated.
"""
from __future__ import annotations
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import signal,json,math,itertools,pathlib,sys
from fractions import Fraction as F
from decimal import Decimal as D,localcontext,ROUND_CEILING
from collections import defaultdict
AUDIT_TIMEOUT_SEC=300
AUDIT_INPUT_PATHS=('archive/common_product_devices_review_2026_10_18/MANIFEST.json', 'archive/common_product_devices_review_2026_10_18/original-recovery.tar.gz', 'docs/COMMON_PRODUCT_AUTONOMOUS_CAT_PREPARER_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_BIASED_OPERATION_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_DIRECT_LOADER_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_ENERGY_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_PAIR_CAT_SELECTOR_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_RESONANT_LAUNCH_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_RESONANT_ROUTER_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_ROBUSTNESS_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_SINGLE_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/COMMON_PRODUCT_TWO_BODY_OPERATION_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/DIRECT_LOADER_RESONANT_OPERATION_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/EXACT_LOADER_CLOCK_TRADEOFFS_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/EXACT_TWO_BODY_ENGINEERED_LOADER_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/EXACT_UNIFORM_LOADER_DWELL_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'outputs/common_product_biased_operation_2026_10_18/INTEGRATION_RECORD.md', 'outputs/common_product_biased_operation_2026_10_18/SOURCES.json', 'outputs/common_product_biased_operation_2026_10_18/source_checks/finite/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/finite/REVIEW.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/network/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/network/REVIEW.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/packet/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/packet/REVIEW.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/phase/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/phase/REVIEW.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/preparation/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/preparation/REVIEW.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/resources/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/resources/REVIEW.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/writer/CORRECTION.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/writer/PROPOSAL.md', 'outputs/common_product_biased_operation_2026_10_18/source_checks/writer/REVIEW.md', 'outputs/common_product_devices_review_2026_10_18/INPUT_CLOSURE.json', 'outputs/common_product_devices_review_2026_10_18/README.md', 'outputs/common_product_devices_review_2026_10_18/inputs/cat_preparer_coordinates.json', 'outputs/common_product_devices_review_2026_10_18/proofs/parents/autonomous_record_route.md', 'outputs/common_product_devices_review_2026_10_18/proofs/parents/common_product_launch_derivative_bounds.md', 'outputs/common_product_devices_review_2026_10_18/proofs/parents/common_product_narrow_cutoff_derivative.md', 'outputs/common_product_devices_review_2026_10_18/proofs/parents/common_product_resonance_tail.md', 'outputs/common_product_devices_review_2026_10_18/proofs/parents/common_product_resonant_boundary_tail.md', 'outputs/common_product_devices_review_2026_10_18/proofs/parents/common_product_single_control_router.md', 'outputs/common_product_devices_review_2026_10_18/proofs/parents/common_product_stage_separated_router.md', 'outputs/common_product_devices_review_2026_10_18/proofs/parents/common_product_writer_resolvent_sharpening.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9725/common_product_autonomous_loader_interface_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9725/common_product_boundary_input_contract_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9725/common_product_full_swap_gadget_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9725/common_product_loader_bond_realization_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9725/common_product_loader_component_background_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9725/common_product_real_two_body_gauge_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9725/common_product_two_body_background_refinement_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9725/common_product_two_body_runtime_penalty_removal_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9725/common_product_two_body_scaled_operation_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9729/common_product_pair_cat_selector_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9729/common_product_selector_exact_energy_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9729/common_product_static_cat_selector_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9731/common_product_autonomous_cat_preparer_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9731/common_product_autonomous_cat_preparer_finite_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9731/common_product_autonomous_cat_preparer_geometry_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9731/common_product_autonomous_cat_preparer_signs_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9733/common_product_direct_loader_branch_instantiation_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9733/common_product_direct_loader_range21_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9733/common_product_direct_loader_uniform_branch_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9733/common_product_direct_two_body_loader_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9733/common_product_direct_two_body_loader_finite_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9734/common_product_direct_loader_resonant_jets_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9734/common_product_direct_loader_resonant_operation_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9737/exact_engineered_clock_dwell_tradeoff_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9737/exact_engineered_clock_operation_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9737/exact_loader_structured_coefficients_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9737/exact_two_body_direct_loader_composition_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9737/exact_two_body_gate_diamond_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9737/exact_two_body_gate_matched_extension_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9741/bandcenter_reference_measure_check_REVIEW.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9741/common_product_endpoint_launch_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9741/common_product_outgoing_pole_tail_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9741/common_product_resonant_halfline_tails_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9741/common_product_resonant_late_tails_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9741/exact_engineered_loader_robust_policy_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9741/exact_engineered_loader_robust_policy_check_ROOT_ARITHMETIC_CORRECTION.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9741/exact_uniform_chain_finite_launch_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9741/exact_uniform_physical_loader_PROPOSAL.md', 'outputs/common_product_devices_review_2026_10_18/proofs/pr9742/exact_uniform_loader_dwell_PROPOSAL.md', 'outputs/common_product_energy_preparation_2026_10_18/INTEGRATION_RECORD.md', 'outputs/common_product_energy_preparation_2026_10_18/SOURCES.json', 'outputs/common_product_energy_preparation_2026_10_18/source_checks/REVIEW.md', 'outputs/common_product_energy_preparation_2026_10_18/source_checks/head_energy/PROPOSAL.md', 'outputs/common_product_energy_preparation_2026_10_18/source_checks/record_ground/PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/SOURCES.json', 'outputs/common_product_finite_seed_2026_10_18/proofs/bandcenter_reference_measure_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_autonomous_interface__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_autonomous_interface_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_endpoint_launch__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_endpoint_launch_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_seed_router__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_seed_router_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_window__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_window__TIMING_MIXTURE.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_window_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_finite_window_check__TIMING_REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_outer_boundary__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/common_product_outer_boundary_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/endpoint_bandcenter_reference__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/mediated_common_product_program__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/mediated_common_product_program_check__REVIEW.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/mediated_program_attachment__PROPOSAL.md', 'outputs/common_product_finite_seed_2026_10_18/proofs/mediated_program_attachment_check__REVIEW.md', 'outputs/common_product_microscopic_seed_2026_10_18/SOURCES.json', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_finite_seed__PROPOSAL.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_finite_seed_check__REVIEW.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_packet__PROPOSAL.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_packet_check__REVIEW.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_scattering__PROPOSAL.md', 'outputs/common_product_microscopic_seed_2026_10_18/proofs/common_product_microscopic_scattering_check__REVIEW.md', 'outputs/common_product_refined_resources_2026_10_18/SOURCES.json', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_finite_seed_scaling__PROPOSAL.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_finite_seed_scaling_check__REVIEW.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_launch_derivative_bounds__PROPOSAL.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_launch_derivative_bounds_check__REVIEW.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_refined_resource_family__PROPOSAL.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_refined_resource_family_check__REVIEW.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_second_order_attachment__PROPOSAL.md', 'outputs/common_product_refined_resources_2026_10_18/proofs/common_product_second_order_attachment_check__REVIEW.md', 'outputs/common_product_resonant_launch_2026_10_18/INTEGRATION_RECORD.md', 'outputs/common_product_resonant_launch_2026_10_18/SOURCES.json', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/finite/PROPOSAL.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/finite/REVIEW.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/geometric/PROPOSAL.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/geometric/REVIEW.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/survival/PROPOSAL.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/survival/REVIEW.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/window/PROPOSAL.md', 'outputs/common_product_resonant_launch_2026_10_18/source_checks/window/REVIEW.md', 'outputs/common_product_resonant_router_2026_10_18/INTEGRATION_RECORD.md', 'outputs/common_product_resonant_router_2026_10_18/SOURCES.json', 'outputs/common_product_resonant_router_2026_10_18/source_checks/composition/PROPOSAL.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/composition/REVIEW.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/halfline/PROPOSAL.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/halfline/REVIEW.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/incoming/PROPOSAL.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/incoming/REVIEW.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/late/PROPOSAL.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/late/REVIEW.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/outgoing/PROPOSAL.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/outgoing/REVIEW.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/preparation/PROPOSAL.md', 'outputs/common_product_resonant_router_2026_10_18/source_checks/preparation/REVIEW.md', 'outputs/common_product_robustness_2026_10_18/INTEGRATION_RECORD.md', 'outputs/common_product_robustness_2026_10_18/SOURCES.json', 'outputs/common_product_robustness_2026_10_18/source_checks/local_matrix/PROPOSAL.md', 'outputs/common_product_robustness_2026_10_18/source_checks/local_matrix/REVIEW.md', 'outputs/common_product_robustness_2026_10_18/source_checks/scalar_weights/PROPOSAL.md', 'outputs/common_product_robustness_2026_10_18/source_checks/scalar_weights/REVIEW.md', 'outputs/common_product_robustness_2026_10_18/source_checks/vacuum_preserving/PROPOSAL.md', 'outputs/common_product_robustness_2026_10_18/source_checks/vacuum_preserving/REVIEW.md', 'outputs/common_product_single_control_2026_10_18/INTEGRATION_RECORD.md', 'outputs/common_product_single_control_2026_10_18/SOURCES.json', 'outputs/common_product_single_control_2026_10_18/source_checks/common_product_logarithmic_flag_policy/PROPOSAL.md', 'outputs/common_product_single_control_2026_10_18/source_checks/common_product_logarithmic_flag_policy_check/REVIEW.md', 'outputs/common_product_single_control_2026_10_18/source_checks/common_product_single_control_router/PROPOSAL.md', 'outputs/common_product_single_control_2026_10_18/source_checks/common_product_single_control_router_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/SOURCES.json', 'outputs/common_product_stage_record_2026_10_18/source_checks/autonomous_record_route/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/autonomous_record_route_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_narrow_cutoff_derivative/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_narrow_cutoff_derivative_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_core/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_core_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_finite_seed/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_finite_seed_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_flag_branch/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_flag_branch_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_packet/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_packet_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_resource_split/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_stage_record_resource_split_check/REVIEW.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_writer_resolvent_sharpening/PROPOSAL.md', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_writer_resolvent_sharpening/certificate.txt', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_writer_resolvent_sharpening/certify_inverse.py', 'outputs/common_product_stage_record_2026_10_18/source_checks/common_product_writer_resolvent_sharpening_check/REVIEW.md', 'outputs/common_product_stage_seed_2026_10_18/SOURCES.json', 'outputs/common_product_stage_seed_2026_10_18/source_checks/common_product_stage_separated_router/PROPOSAL.md', 'outputs/common_product_stage_seed_2026_10_18/source_checks/common_product_stage_separated_router_check/REVIEW.md', 'outputs/common_product_stage_seed_2026_10_18/source_checks/common_product_stage_separated_seed/PROPOSAL.md', 'outputs/common_product_stage_seed_2026_10_18/source_checks/common_product_stage_separated_seed_check/REVIEW.md', 'outputs/product_program_continuation_review_2026_10_18/DEPENDENCIES.json')
ROOT=pathlib.Path(__file__).resolve().parents[1]
if not __debug__:raise RuntimeError('Assertions must remain enabled')
def expired(signum,frame):raise TimeoutError('Declared300-second cap reached')
signal.signal(signal.SIGALRM,expired);signal.alarm(AUDIT_TIMEOUT_SEC)
import numpy as np
from scipy.integrate import quad
COUNT=0
def check(label,condition,**data):
 global COUNT
 print(('[PASS] ' if bool(condition) else '[FAIL] ')+label+' '+json.dumps(data,sort_keys=True),flush=True)
 if not bool(condition):raise AssertionError(label)
 COUNT+=1
I=np.eye(2);X=np.array([[0.,1.],[1.,0.]]);Y=np.array([[0.,-1j],[1j,0.]]);Z=np.diag([1.,-1.]);n=np.diag([0.,1.]);H=(X+Z)/np.sqrt(2)
def kron(xs):
 a=np.ones((1,1))
 for x in xs:a=np.kron(a,x)
 return a
def loc(N,j,a):return kron([a if k==j else I for k in range(N)])
def norm(a):return float(np.linalg.norm(a,2))
def expH(h,t):
 e,v=np.linalg.eigh(h);return (v*np.exp(-1j*t*e))@v.conj().T

def joint_square():
 # Enumerate only fourth-order paths capable of returning each four-bit square
 # to its cat sector. All intermediate penalty-zero states are excluded.
 ops=[]
 for e in range(2):
  for hh in ('X','Y'):
   for aa in ('X','Y','Z'):
    ops += [(2*e,hh),(2*e+1,hh),(4,aa),(5,aa)]
 table={('X','Y'):('Z',1),('Y','Z'):('X',1),('Z','X'):('Y',1),('Y','X'):('Z',3),('Z','Y'):('X',3),('X','Z'):('Y',3)}
 coeff=defaultdict(lambda:[F(0),F(0)]);accepted=0
 def energy(mask):
  total=0
  for q in range(12):
   b=(mask>>(4*q))&15
   total+=sum(((b>>k)&1)!=((b>>((k+1)%4))&1) for k in range(4))
  return total
 def path(seq):
  nonlocal accepted
  mask=0;den=1;word=['I']*6;phase=0
  for j,o in enumerate(seq):
   mask^=1<<o;site,pa=ops[o];old=word[site]
   if old=='I':word[site]=pa
   elif old==pa:word[site]='I'
   else:word[site],ph=table[(pa,old)];phase=(phase+ph)%4
   en=energy(mask)
   if j<3:
    if en==0:return
    den*=en
   elif en!=0:return
  accepted+=1;v=F(-1,den);coeff[tuple(word)][phase%2]+=v*(1 if phase<2 else -1)
 for i in range(48):
  for j in range(i+1,48):
   for seq in set(itertools.permutations((i,i,j,j))):path(seq)
 for square in range(12):
  for seq in itertools.permutations(range(4*square,4*square+4)):path(seq)
 ident=('I',)*6;coeff[ident][0]+=F(288)
 expected={ident:F(27)}
 for s in range(12):
  w=['I']*6
  for site,pa in ops[4*s:4*s+4]:w[site]=pa
  expected[tuple(w)]=F(-5,2)
 actual={w:v[0] for w,v in coeff.items() if v!=[0,0]}
 check('9725 joint normalized fourth-order ordered paths',accepted==4800 and actual==expected and all(v[1]==0 for v in coeff.values()),paths=accepted,scalar=str(actual.get(ident)),nonscalar_words=len(actual)-1)
 # Exact real gauge and signed cat injection for every H/A combination.
 S=np.diag([1,1j]);basis={'X':X,'Y':Y,'Z':Z};signs=[]
 for hh in ('X','Y'):
  for aa in ('X','Y','Z'):
   ps=[hh,hh,aa,aa];u=kron([S if p=='Y' else I for p in ps]);cat=np.zeros(16,complex);cat[[0,15]]=1/np.sqrt(2);v=u@cat;sig=(-1)**(ps.count('Y')//2);signs.append(sig)
   check('9725 real gauge '+hh+aa,np.max(abs(v.imag))<1e-14 and abs(v[15]-sig/np.sqrt(2))<1e-14)
 check('9725 six signed rows',signs==[1,-1,1,-1,1,-1])

def selectors():
 for sigma,r in itertools.product([1,-1],[1/128,1/64]):
  delta=1.;h=r;eye=np.eye(16);h0=sum(((eye-loc(4,i,Z)@loc(4,(i+1)%4,Z))/2 for i in range(4)),np.zeros((16,16)))
  hp=h0+h*(2*eye-loc(4,0,X)@loc(4,1,X)-sigma*loc(4,2,X)@loc(4,3,X));ev,vec=np.linalg.eigh(hp);R=math.sqrt(1+4*h*h);gap=4*h*h/(R+1);eg=2*h-gap;cat=np.zeros(16);cat[0]=1/np.sqrt(2);cat[-1]=sigma/np.sqrt(2);psi=vec[:,0]*np.sign(vec[0,0])
  check(f'9729 full16-state selector sigma={sigma} r={r}',abs(ev[0]-eg)<1e-13 and abs(ev[1]-ev[0]-gap)<1e-13 and gap>=h*h and norm((psi-cat)[:,None])<=2*r,e0=float(ev[0]),gap=float(ev[1]-ev[0]),cat_distance=float(np.linalg.norm(psi-cat)))

def gates_and_diamond():
 # Full32-column logical word with two rail coordinates and shared Q,P,R.
 def controlled(control,target,pa):return np.eye(32)-loc(5,control,n)+loc(5,control,n)@loc(5,target,pa)
 U=np.eye(32);layers=0
 def apply(g):
  nonlocal U,layers
  U=g@U;layers+=1
 for data,target in [(2,3),(3,2),(2,3)]:
  for g in [loc(5,0,H),-controlled(0,data,Z),loc(5,0,H),-controlled(0,target,X),loc(5,0,H),-controlled(0,data,Z),loc(5,0,H)]:apply(g)
 for g in [loc(5,1,H),-controlled(1,3,Z),loc(5,1,H),loc(5,1,X),-loc(5,4,X)]:apply(g)
 target=np.zeros((32,32))
 for z in range(32):
  a,b,q,p,r=[(z>>(4-i))&1 for i in range(5)];v=[a,b^(1-q),p,q,r^1];out=sum(x<<(4-i) for i,x in enumerate(v));target[out,z]=-1
 check('9737 ordered26-layer shared-data word all32columns',layers==26 and norm(U-target)<2e-14,error=norm(U-target))
 V=np.eye(32)
 for control,write in [(2,3),(3,2),(2,3)]:
  core=loc(5,control,n)+(np.eye(32)-loc(5,control,n))@loc(5,0,X)
  for gate in [core,controlled(0,write,X),core]:V=gate@V
 core=loc(5,3,n)+(np.eye(32)-loc(5,3,n))@loc(5,1,X)
 V=loc(5,4,X)@core@V
 check('9733 eleven-stage full auxiliary/data/reference word',norm(V+target)<1e-14 and norm(V.T@V-np.eye(32))<1e-14)

 # Cat preparer: path Hadamard, four conditional writers, final zero-control router.
 W=loc(5,0,H)
 for j in range(1,5):W=(np.eye(32)-loc(5,0,n)+loc(5,0,n)@loc(5,j,X))@W
 router=loc(5,1,n)+(np.eye(32)-loc(5,1,n))@loc(5,0,X);seed=np.zeros(32);seed[0]=1;wanted=np.zeros(32);wanted[16]=wanted[31]=1/np.sqrt(2)
 check('9731 product-seed cat and common outgoing path',np.linalg.norm(router@W@seed-wanted)<1e-14)
 for pa in [X,Z,I]:
  aL,aR,g=.3,.5,.7;physical=np.zeros((8,8));eye=np.eye(2)
  for i,j,w,sgn in [(0,1,aL,1),(0,2,aL,1),(1,3,aR,1),(2,3,aR,-1)]:
   physical[2*i:2*i+2,2*i:2*i+2]+=w*eye;physical[2*j:2*j+2,2*j:2*j+2]+=w*eye
   physical[2*i:2*i+2,2*j:2*j+2]-=sgn*w*eye;physical[2*j:2*j+2,2*i:2*i+2]-=sgn*w*eye
  physical[2:4,2:4]+=g*(eye+pa);physical[4:6,4:6]+=g*(eye-pa)
  rotation=np.eye(4);rotation[1:3,1:3]=H;A=np.kron(rotation,eye);G=np.zeros((8,8))
  for j,v in enumerate([eye,eye,-pa,-pa]):G[2*j:2*j+2,2*j:2*j+2]=v
  scalar=np.diag([2*aL,aL+aR+g,aL+aR+g,2*aR]);off=[-np.sqrt(2)*aL,-g,-np.sqrt(2)*aR]
  for j,v in enumerate(off):scalar[j,j+1]=scalar[j+1,j]=v
  check('9737 unequal-end exact physical diamond '+str(pa.tolist()),norm(G.T@A.T@physical@A@G-np.kron(scalar,eye))<1e-14 and np.linalg.eigvalsh(physical).min()>-1e-13)

def source_and_cutoff():
 for rho in [.08,.3,.7]:
  aa=2-rho*rho;b=rho*rho/aa
  integral,err=quad(lambda t:2/(math.pi*aa)/(1+b*b*math.tan(t)**2),-math.pi/2,math.pi/2,epsabs=1e-12)
  check(f'9731/9733/9734/9741 exact source measure rho={rho}',abs(integral-1)<1e-11 and abs(aa*(1+b)-2)<1e-14,integral=integral)
 # Exact polynomial endpoint traces through second order; third derivative finite.
 c=[F(1),F(0),F(0),F(-10),F(15),F(-6)]
 def derivative(a):return [i*a[i] for i in range(1,len(a))]
 def at(a,x):return sum(v*x**j for j,v in enumerate(a))
 check('actual quintic cutoff matching traces',at(c,0)==1 and at(c,1)==0 and all(at(a,0)==at(a,1)==0 for a in [derivative(c),derivative(derivative(c))]))
 # Fixed-diagonal cut must remove only hopping, not endpoint occupations.
 h=np.diag([2.]*8)+np.diag([-1.]*7,1)+np.diag([-1.]*7,-1);cut=h.copy();cut[3,4]=cut[4,3]=0
 check('9733/9741/9742 fixed-diagonal cut and omitted-occupation mutant',np.array_equal(np.diag(cut),np.diag(h)) and norm(cut-h)==1 and norm((cut-np.diag([0,0,0,1,1,0,0,0]))-h)>1)

def engineered():
 for L in [8,17,30]:
  alpha=.07;C=.4;h=C*np.eye(L+1)
  for j in range(1,L+1):h[j,j-1]=h[j-1,j]=-alpha*math.sqrt(j*(L+1-j))
  for theta in [math.pi/3,math.pi/2,2*math.pi/3,math.pi]:
   t=theta/alpha;actual=expH(h,t)[:,0];expected=np.array([np.exp(-1j*C*t)*math.sqrt(math.comb(L,x))*(1j*math.sin(theta))**x*math.cos(theta)**(L-x) for x in range(L+1)])
   check(f'9737 exact scalar profile L={L} theta={theta}',np.linalg.norm(actual-expected)<2e-12,error=float(np.linalg.norm(actual-expected)))
 for eps in [1.,.1,.01]:
  L=max(296,math.ceil(4*math.log(32/eps)));J=1/80;T=math.pi*(L+1)/(4*J);hor=4*T/3;delta=eps/(256*hor)
  check(f'9741 elapsed-time supported-error allocation eps={eps}',math.exp(-L/2)<=eps*eps/1024 and 8*delta*hor<=eps/32*(1+1e-14) and 40*J+20*delta<1 and delta<1/40,qubits=4*L+7,blocks=8*L+172,horizon=hor,error_ceiling=delta)
  for ratio in [2.,5.,20.]:
   mean=max(148,8*math.log(256/eps**2));LL=math.ceil(max(296,mean/math.sin(math.pi/(ratio+2))**2));theta=math.asin(math.sqrt(mean/LL));actualratio=math.pi/theta-2
   check(f'9737 finite engineered dwell eps={eps} ratio={ratio}',actualratio>=ratio-1e-12 and math.exp(-mean/8)<=eps*eps/256,L=LL,actual_ratio=actualratio)

def uniform_policy():
 with localcontext() as ctx:
  ctx.prec=80;a=D(23)/100;b2,b3,b4=map(D,[64,512,2048]);d0,d1,d2,d3=map(D,[2,24,394,6280])
  P=d3/a**3+6*b2*d2/a**4+(4*b3/a**4+15*b2*b2/a**5)*d1+(b4/a**4+10*b2*b3/a**5+15*b2**3/a**6)*d0
  Q=d3/(2*a*a)+2*b2*d2/a**3+(4*b3/(3*a**3)+15*b2*b2/(4*a**4))*d1+(b4/(3*a**3)+10*b2*b3/(4*a**4)+3*b2**3/a**5)*d0
  DD=4*P+20*Q
  for eps in map(D,['1','.1','.01']):
   h=D('.001');rho=eps*h.sqrt()/1024;twothirds=lambda x:(x.ln()*D(2)/3).exp()
   ell=int(max(D(7500),192*rho*Q/(h*h*eps),twothirds(128*rho*DD/(h*h*eps)),twothirds(32768*rho*Q/(h*h*eps*eps)),10/rho**2*(512*h.sqrt()/(rho*eps)).ln()).to_integral_value(rounding=ROUND_CEILING));l=D(ell)
   cutoff=2*(3*rho*rho/h).sqrt();cut=3*rho*Q/(h*h*l);alg=rho*DD/(h*h*l**D('1.5'));expt=4*h.sqrt()/rho*(-min(rho*rho*l/10,D(10000))).exp();incoming=4*rho*Q/(h*h*l**D('1.5'));dm=alg+expt
   check(f'9741/9742 uniform six-entry policy eps={eps}',cutoff<eps/256 and cut<=eps/64 and alg<=eps/128 and expt<=eps/128 and incoming<=eps*eps/8192 and dm<1,ell=ell,filter=str(cutoff),cut=str(cut),tail=str(dm),incoming=str(incoming))
   for ratio in map(D,['0.16666666666666666666666666666666666666666666666666666666666666666666666666666667','1','10']):
    M=int(((12*ratio+5)*l/7).to_integral_value(rounding=ROUND_CEILING));actual=(7*D(M)-5*l)/(12*l);lc=(l+M)/2;u=7*(l+M)/16;Lminus=l+73;Rplus=l+M+74
    check(f'9742 asymmetric dwell eps={eps} ratio={ratio}',M>=ell and actual>=ratio and D('1.98')*(3*l/4)-Lminus>=D('.4')*l and Lminus+u<=16*(D('1.98')*u-Lminus) and D('.99')*Rplus-2*u>=D('.23')*lc,output_length=M,ratio=str(actual),qubits=301+4*(ell+M),blocks=478+8*(ell+M))

def geometry():
 data=json.loads((ROOT/'outputs/common_product_devices_review_2026_10_18/inputs/cat_preparer_coordinates.json').read_text())
 heads={tuple(v) for v in data['module_heads'].values()};targets={tuple(v) for v in data['targets'].values()};occupied=heads|targets
 check('9731 literal module and target site injection',len(heads)==204 and len(targets)==4 and len(occupied)==208)
 lengths=defaultdict(list);interiors=0
 for cable in data['cables']:
  corners=[tuple(v) for v in cable['axis_aligned_corners']];points=[corners[0]]
  for a,b in zip(corners,corners[1:]):
   axes=[i for i in range(3) if a[i]!=b[i]]
   if len(axes)!=1:raise AssertionError('Non-axis-aligned cable segment')
   k=axes[0];step=1 if b[k]>a[k] else -1
   for x in range(a[k]+step,b[k]+step,step):v=list(a);v[k]=x;points.append(tuple(v))
  inside=set(points[1:-1]);length=len(points)-1
  check(f"9731 expanded cable {cable['gap']}/{cable['branch']}",len(set(points))==len(points) and not inside&occupied and points[0]==tuple(data['module_heads'][cable['start']]) and points[-1]==tuple(data['module_heads'][cable['end']]) and length==cable['edges'],length=length)
  occupied.update(inside);interiors+=len(inside);lengths[cable['gap']].append(length)
 check('9731 equal paired phases and exact finite inventory',all(len(v)==2 and v[0]==v[1] for v in lengths.values()) and sum(v[0] for v in lengths.values())==302149 and interiors==604288 and len(occupied)==604496)
 rays=[tuple(data['module_heads'][key]) for key in data['external_positive_z_rays']]
 check('9731 analytic infinite-ray exclusion from all finite vertices',len({v[:2] for v in rays})==4 and all(not any(p[:2]==r[:2] and p[2]>r[2] for p in occupied) for r in rays))
 neighbours=set();a1=tuple(data['targets']['w11.target']);unit=True
 for aa,bb,kind in data['module_and_external_first_edges']:
  a,b=tuple(aa),tuple(bb);unit &= sum(abs(x-y) for x,y in zip(a,b))==1
  if a==a1:neighbours.add(tuple(y-x for x,y in zip(a,b)))
  if b==a1:neighbours.add(tuple(x-y for x,y in zip(a,b)))
 check('9731 actual module unit edges and six shared-target neighbours',unit and neighbours=={(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)})
 # Independent finite relabeling, not a wire embedding.
 ports=[(i,7,7) for i in range(8)];cube=list(itertools.product(range(8),repeat=3));sites=ports+[v for v in cube if v not in ports][:491]
 check('9733 supplied range21 relabeling all499 sites',len(sites)==len(set(sites))==499 and all(sum(abs(x-y) for x,y in zip(a,b))<=21 for a in sites for b in sites) and all((i,7,8) not in sites for i in range(8)))

def finite_budgets():
 # Evaluate the actual old direct-loader sufficient recipe independently of the
 # primary's separate source-measure and local-block computations.
 for eps in [1.,.1,.01]:
  h=eps/1e7;eta=math.sqrt(h);rho=eps*math.sqrt(h)/1e4;delta=33*eps/1e7;B=11;delay=105
  G0,G1,G2=2.,80/rho,600/rho**3
  s1=6*B**2+2*B;s2=36*B**3+18*B**2+2*B;a1=1+s1;a2=1+2*s1+s2
  r0=11/(1-11*delta);r1=r0*r0*a1;r2=2*r0**3*a1*a1+r0*r0*a2
  v0=1+r0;v1=r1+r0*a1;S1=s1+s1*r0+r1+r0*a1;S2=s2+s2*r0+2*s1*r1+2*s1*r0*a1+r2+2*r1*a1+r0*a2
  Q1=S1+delay;Q2=S2+2*delay*S1+delay**2
  H0=G0;H1=G1+Q1*G0;H2=G2+2*Q1*G1+Q2*G0
  T0=2*B*v0;T1=s1*v0+2*B*v1;J0=T0*G0;J1=T0*G1+T1*G0
  Bin=G2+6*G1+14*G0;Bout=H2+24*H1+200*H0
  LL=1+(G1+2*G0)+(H1+H0)+(G1+8*G0);Qbudget=1+1/eta+rho**-2+J0+J1+Bin+Bout
  u0=1e12*max(1,(LL/eps)**2,Qbudget/eps);ell=math.ceil(max(100*u0,10500));l=float(ell)
  contact=(2+math.sqrt(2)/eta)/(5000*u0);cut=100*(Bin/u0+Bout/l);ds=144*delta/(1-11*delta)
  init=contact+rho**-2/u0+2*(G1+2*G0)/math.sqrt(u0)+4*math.sqrt(3)*rho/math.sqrt(h)+2*(G1+G0+H1+H0)/math.sqrt(l)+2*(J0+J1)/l
  final=init+cut+ds+2*(G1+6*G0)/math.sqrt(l)+(3*J1+11*J0)/l+10*(G1+8*G0)/math.sqrt(l)
  branch=init+cut+ds+T0*4*rho*math.log1p(2*h/rho**2)/math.sqrt(2*math.pi)
  early=contact+2*LL/math.sqrt(l)
  check(f'9733 complete old finite and bounded-horizon branch budget eps={eps}',final<eps/8 and branch<eps/256 and early<eps/256 and 11*delta<1,final=final,branch=branch,early=early,ell=ell)
  # Six-entry algebraic allocation on explicit finite parameter fixtures; these
  # lengths do not assert completion of the distinct parent finite recipe.
  K=48.;Delta=.25;jbar=eps**2/(8e12);lg=1e6/eps**2;U=7*lg/8;eg=eps/8;Bmax=161+8*jbar*(lg+1);Cmix=16384*K*K
  alpha=min(1/(32*K),eg/(48*K),math.sqrt(5*eg/(2*(8*K)**6*U)),math.sqrt(eg*jbar/(3*Cmix*U*Bmax)),(jbar/(320*Bmax))**.25,(jbar/(10*Delta))**.25)
  lam=10*Delta*alpha**4/jbar;time=U/(10*Delta*alpha**4);beta=lam*Bmax;rem=Delta*(8*K*alpha)**6/(1-(8*K*alpha)**2)
  costs=[16*K*alpha,time*rem,time*Cmix*alpha*alpha*beta]
  check(f'9725 actual scaled-operation six-entry allocation eps={eps}',sum(costs)<=eg and lam<=1 and beta<=Delta/32,costs=costs,alpha=alpha)
  hh=min(Delta/64,Delta*eps/384,eps/(384*time));gap=hh*hh/Delta;q=eps*eps/512;energy=gap*eps*eps/512
  check(f'9729 joint rest and selector runtime allocation eps={eps}',2*math.sqrt(q+energy/gap)+48*hh/Delta<=eps/4 and 24*hh*time<=eps/16*(1+1e-14),h=hh)

def resonant_budgets():
 def mul(a,b):return [sum(math.comb(n,k)*a[k]*b[n-k] for k in range(n+1)) for n in range(4)]
 sj=[1.,748.,50116.,5036284.];aj=[1.,749.,51613.,5188877.];r0=22.
 rj=[r0,r0*r0*aj[1],2*r0**3*aj[1]**2+r0*r0*aj[2],6*r0**4*aj[1]**3+6*r0**3*aj[1]*aj[2]+r0*r0*aj[3]]
 prod=mul(mul(sj,rj),aj);nj=[1.]+[sj[i]+prod[i] for i in range(1,4)];m=mul(nj,[1.,105.,105.**2,105.**3])
 def pq(v,bs):
  c=mul(mul([1.,1.,2.,5.],[1.,1.,3.,10.]),[v[0],v[1],v[2]+v[1],v[3]+3*v[2]+3*v[1]])
  d0=2*c[0];d1=20*c[0]+2*c[1];d2=300*c[0]+40*c[1]+2*c[2];d3=4000*c[0]+900*c[1]+60*c[2]+2*c[3];a=.23;b2,b3,b4=bs
  P=d3/a**3+6*b2*d2/a**4+(4*b3/a**4+15*b2*b2/a**5)*d1+(b4/a**4+10*b2*b3/a**5+15*b2**3/a**6)*d0
  Q=d3/(2*a*a)+2*b2*d2/a**3+(4*b3/(3*a**3)+15*b2*b2/(4*a**4))*d1+(b4/(3*a**3)+10*b2*b3/(4*a**4)+3*b2**3/a**5)*d0
  return P,Q
 large=[64.,512.,2048.];small=[4.,32.,128.];ident=[1.,0.,0.,0.]
 pi,qi=pq(ident,large);C=1e6*(1+pi+qi+pq(m,large)[1]+pq(m,small)[1])
 for eps in [1.,.1,.01]:
  h=eps/1e7;eta=math.sqrt(h);rho=eps*math.sqrt(h)/1e4;A=C*rho/h**2;J0=1012.;J1=80*506/rho+2*8355072;Lg=math.log(1e8/(eps*rho))
  u0=1e8*max(1,1/(eta*eps),(J0+J1)/eps,A/eps,(A/eps)**(2/3),Lg/rho**2);ell=math.ceil(max(100*u0,10500));l=float(ell)
  # Conservative positive upper ceiling avoids claiming an underflowed exp is zero.
  xx=eps*rho/1e8;ds=144*(33*eps/1e7)/(1-11*(33*eps/1e7))
  rows=[(2+math.sqrt(2)/eta)/(5000*u0),xx+4*rho*rho/3,2*A/u0**1.5+2*math.sqrt(h)*xx/rho,4*math.sqrt(3)*rho/math.sqrt(h),2*A/l**1.5,2*(J0+J1)/l,6*xx/rho+A/u0,A/l,A/l**1.5+4*math.sqrt(h)*xx/rho,11*(J0+J1)/l,ds,4*A/l**1.5+8*math.sqrt(h)*xx/rho]
  alloc=[eps/1e8,eps/1e8+4*rho*rho/3,2*eps/1e12+2*eps/1e8,eps/1024,2*eps/1e15,2*eps/1e10,7*eps/1e8,eps/1e10,eps/1e15+4*eps/1e8,11*eps/1e10,eps/2048,4*eps/1e15+8*eps/1e8]
  for i,(value,limit) in enumerate(zip(rows,alloc),1):check(f'9734 resonant contribution {i:02} eps={eps}',value<=limit*(1+1e-13),value=value,ceiling=limit)
  dF=2*A/l**1.5+4*math.sqrt(h)*xx/rho
  check(f'9734 simultaneous total and positive normalization eps={eps}',sum(rows)<eps/8 and dF<1 and rho*rho*u0/4>=math.log(1/xx),total=sum(rows),dF=dF,ell=ell)

def actual_core_scattering():
 # Eight physical heads, fixed data eigensector. This control concerns the
 # supplied local core only; shared-data compositions use ordered full words.
 for eta,zeta in [(.02,.001),(.01,.0003)]:
  D1=1.;D0=zeta;beta=eta*D0;j=beta*beta/D0
  for data in [0,1]:
   h=np.zeros((8,8));h[:4,:4]=3*j*np.eye(4)
   for m,(left,right,cross) in enumerate([(0,2,False),(1,3,False),(0,3,True),(1,2,True)],4):
    low=(cross and data==0) or (not cross and data==1);h[m,m]=D0 if low else D1
    for q in [left,right]:h[q,m]=h[m,q]=-beta
   for offset in [0.,.0001,-.0001]:
    k=math.pi/2+offset;z=np.exp(1j*k);energy=2*j*(1-math.cos(k));M=h.astype(complex)-energy*np.eye(8);M[:4,:4]-=j*z*np.eye(4)
    columns=np.linalg.solve(M,np.eye(8)[:,:4]);sc=-np.eye(4)-2j*j*math.sin(k)*columns[:4,:]
    gate=X if data==0 else I;ideal=np.block([[np.zeros((2,2)),z*gate],[z*gate,np.zeros((2,2))]])
    residual=norm(M@columns-np.eye(8)[:,:4]);defect=norm(sc-ideal)
    # Retain the attached ordinary lead diagonal:2j endpoint occupation+j.
    # The stated Schur bound is uniform over the specified band.
    valid=norm(sc.conj().T@sc-np.eye(4))<1e-10 and residual<1e-10
    valid &= defect<=13*eta*eta+5*zeta
    check(f'9731/9733 actual8-head core data={data} eta={eta} offset={offset}',valid,scattering_defect=defect,residual=residual)

def cat_budget():
 for eps in [1.,.1,.01]:
  h=eps/1e6;rho=eps*math.sqrt(h)/1e4;G0,G1,G2=2.,80/rho,600/rho**3;B=11.;C=604288.;Lm=100648.;delay=302239.;delta=33*eps/1e6
  s1=6*B*B+2*B;s2=36*B**3+18*B*B+2*B;a1=Lm+s1;a2=Lm*Lm+2*Lm*s1+s2
  r0=6/(1-6*delta);r1=r0*r0*a1;r2=2*r0**3*a1*a1+r0*r0*a2;v0=1+r0;v1=r1+r0*a1
  S1=s1+s1*r0+r1+r0*a1;S2=s2+s2*r0+2*s1*r1+2*s1*r0*a1+r2+2*r1*a1+r0*a2;Q1=S1+delay;Q2=S2+2*delay*S1+delay*delay
  H0=G0;H1=G1+Q1*G0;H2=G2+2*Q1*G1+Q2*G0
  T0=2*B*v0+2*math.sqrt(C)*v0;T1=s1*v0+2*B*v1+2*math.sqrt(C)*((Lm+s1)*v0+v1);J0=T0*G0;J1=T1*G0+T0*G1
  Bin=G2+6*G1+14*G0;Bout=H2+24*H1+200*H0;A=1+rho**-2+G1+2*G0+Bin;u0=(1e6*A/eps)**2;big=1+G1+8*G0+H1+H0+J0+J1+Bout;ell=math.ceil(max(100*u0,100*delay,(1e6*big/eps)**2));l=float(ell)
  # exp(-ell/2) <= 1/ell for ell>=2, retaining a positive conservative cost.
  init=1/l+rho**-2/u0+2*(G1+2*G0)/math.sqrt(u0)+4*math.sqrt(3)*rho/math.sqrt(h)+2*(G1+G0+H1+H0)/math.sqrt(l)+2*(J0+J1)/l
  total=init+100*(Bin/u0+Bout/l)+49*delta/(1-6*delta)+2*(G1+6*G0)/math.sqrt(l)+(3*J1+11*J0)/l+10*(G1+8*G0)/math.sqrt(l)
  check(f'9731 complete geometry-aware finite cat budget eps={eps}',6*delta<1 and total<eps/8 and l>=100*delay,total=total,ell=ell,qubits=604498+4*ell,blocks=604606+4*ell)

def main():
 joint_square();selectors();actual_core_scattering();gates_and_diamond();source_and_cutoff();engineered();uniform_policy();geometry();finite_budgets();resonant_budgets();cat_budget()
 print('per_element: Exact ordered Pauli coefficients, full selector spectra, signed gates and scalar phases are calculated from supplied matrices.')
 print('per_site: Physical local blocks, complete frozen cable vertices and infinite-ray exclusions are checked; primitive block and incidence hypotheses remain in bound proofs.')
 print('per_mode: Full logical columns, ancillary sectors, source normalization and finite scalar-clock modes are retained; no successful branch substitutes for full output.')
 print('per_block: Written leakage, scattering and tail estimates retain their stated hypotheses; finite controls accompany rather than replace those general proofs.')
 print('lattice_wide: All devices are finite supplied constructions with explicit resource policies; native interactions, preparation of a coupled receiving gadget, active environments and permanent halt remain unproved.')
 print(f'TOTAL: PASS={COUNT} FAIL=0',flush=True)
if __name__=='__main__':main()
