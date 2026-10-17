#!/usr/bin/env python3
"""Finite corroboration of common-offset source identities and published budgets.

Analytical proof files remain controlling. No full device propagation, uniform
operator estimate, calibration, localization, native supplier or physical time
claim is certified by these finite checks. Imports perform no science.
"""
from pathlib import Path
from decimal import Decimal, localcontext
import hashlib
import json

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/AUTONOMOUS_LOCAL_RECORD_FINITE_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/COMMON_SOURCE_OFFSET_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/CRITICAL_PRODUCT_SOURCE_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/HOPPING_CONTROLLED_FINITE_OUTPUT_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/NOMINAL_BANDCENTER_CONVERTER_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/SLOW_OUTPUT_COMPLETE_STATE_ONSET_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/SLOW_OUTPUT_LOCAL_RECORD_FINITE_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/STRUCTURED_SOURCE_TOLERANCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/THREE_SITE_PRODUCT_SOURCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/UNIFORM_SLOW_OUTPUT_RESOURCE_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/WIDE_SLOW_OUTPUT_COMPLETE_STATE_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'outputs/attached_record_2026_10_17/source_checks/autonomous_record_route/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/autonomous_record_route_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_bandwidth_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_bandwidth_extension/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_converter_composition/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_converter_composition_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_converter_endpoint/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_converter_endpoint_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_reference_measure_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_resources/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_resources_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_weighted_profile/ENDPOINT_ERRATUM_REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_weighted_profile/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_weighted_profile_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/output_lead_weight/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/output_lead_weight_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_alltime_composition/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_alltime_composition_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_alltime_composition_check/REVIEW_v1.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_emitter_bound/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_emitter_bound_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_kernel/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_kernel_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_outgoing_profile/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_outgoing_profile/PROPOSAL_v1.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_outgoing_profile_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_recovery_bound/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_recovery_bound/PROPOSAL_v1.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_recovery_sharp/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_recovery_sharp_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_seed_mass/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_seed_mass_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_core_operator_difference/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_core_operator_difference_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_finite_herald_transfer/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_finite_herald_transfer/PROPOSAL_v1.md',
    'outputs/attached_record_2026_10_17/source_checks/record_finite_herald_transfer_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse/RESULT.json',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse/check.py',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse_check/EVIDENCE.md',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse_check/continuant_check.py',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse_check/continuant_stdout.txt',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_closed_spectrum/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_closed_spectrum_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_incoming_alltime/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_incoming_alltime_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_reference_outgoing_onset/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_reference_outgoing_onset_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_seed_matrix_mass/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_seed_matrix_mass_check/REVIEW.md',
    'outputs/common_source_offset_2026_10_17/INTEGRATION_REVIEW.md',
    'outputs/common_source_offset_2026_10_17/SOURCES.json',
    'outputs/common_source_offset_2026_10_17/landing/PROOF_INPUT_BINDING.json',
    'outputs/common_source_offset_2026_10_17/landing/original-parents/AUTONOMOUS_LOCAL_RECORD_FINITE_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-17.md.txt',
    'outputs/common_source_offset_2026_10_17/landing/original-parents/CRITICAL_PRODUCT_SOURCE_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-17.md.txt',
    'outputs/common_source_offset_2026_10_17/landing/original-parents/HOPPING_CONTROLLED_FINITE_OUTPUT_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-17.md.txt',
    'outputs/common_source_offset_2026_10_17/landing/original-parents/NOMINAL_BANDCENTER_CONVERTER_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md.txt',
    'outputs/common_source_offset_2026_10_17/landing/original-parents/SLOW_OUTPUT_COMPLETE_STATE_ONSET_BOUNDED_THEOREM_NOTE_2026-10-17.md.txt',
    'outputs/common_source_offset_2026_10_17/landing/original-parents/SLOW_OUTPUT_LOCAL_RECORD_FINITE_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-17.md.txt',
    'outputs/common_source_offset_2026_10_17/landing/original-parents/STRUCTURED_SOURCE_TOLERANCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md.txt',
    'outputs/common_source_offset_2026_10_17/landing/original-parents/THREE_SITE_PRODUCT_SOURCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md.txt',
    'outputs/common_source_offset_2026_10_17/landing/original-parents/UNIFORM_SLOW_OUTPUT_RESOURCE_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md.txt',
    'outputs/common_source_offset_2026_10_17/landing/original-parents/WIDE_SLOW_OUTPUT_COMPLETE_STATE_BOUNDED_THEOREM_NOTE_2026-10-17.md.txt',
    'outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_actual_interface__PROPOSAL.md',
    'outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_actual_interface_check__REVIEW.md',
    'outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_complete__PROPOSAL.md',
    'outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_complete_check__REVIEW.md',
    'outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_local_core__PROPOSAL.md',
    'outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_local_core_check__REVIEW.md',
    'outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_reference_time__PROPOSAL.md',
    'outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_reference_time_check__REVIEW.md',
    'outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_source__PROPOSAL.md',
    'outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_source_check__REVIEW.md',
    'outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_traveling__PROPOSAL.md',
    'outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_traveling_check__REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/three_site_actual_attachment/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/three_site_actual_attachment_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/three_site_loaded_inverse/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/three_site_loaded_inverse_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/three_site_product_source/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/three_site_product_source_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_actual_attachment/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_actual_attachment_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_loaded_inverse/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_loaded_inverse_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_loaded_mass/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_loaded_mass_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_product_source/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_product_source_check/REVIEW.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_background_derivative/PROPOSAL.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_background_derivative_check/REVIEW.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_complete_onset_frontier/PROPOSAL.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_complete_onset_frontier_check/REVIEW.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_complete_quantitative/PROPOSAL.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_complete_quantitative_check/REVIEW.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_direct_forcing_refinement/PROPOSAL.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_direct_forcing_refinement_check/REVIEW.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_forced_derivative_sharp/PROPOSAL.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_forced_derivative_sharp_check/REVIEW.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_incoming_late/PROPOSAL.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_incoming_late_check/REVIEW.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_coefficient_robustness/PROPOSAL.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_coefficient_robustness_check/REVIEW.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_family_example/PROPOSAL.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_family_example_check/REVIEW.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_fixed_dimensionless_scaling/PROPOSAL.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_fixed_dimensionless_scaling_check/REVIEW.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_composition/PROPOSAL.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_composition_check/REVIEW.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_endpoint/PROPOSAL.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_endpoint_check/REVIEW.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_reference/PROPOSAL.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_reference_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/same_carrier_slow_lead/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/same_carrier_slow_lead_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_alltime_composition/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_alltime_composition_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_emitter/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_emitter_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_gate_load/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_gate_load_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_outgoing_profile/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_outgoing_profile_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_recovery/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_recovery_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_reference_packet/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_reference_packet_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_resources/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_resources_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/INTEGRATION_REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_centered_background/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_centered_background_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_complete/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_complete_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_derivative/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_derivative_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_endpoint/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_endpoint/PROPOSAL_v1.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_endpoint_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_outgoing/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_outgoing_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_reference/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_reference_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_seed_mass/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_seed_mass_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_sharp/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_sharp_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wider_receiver_band/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wider_receiver_band/PROPOSAL_v1.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wider_receiver_band_check/REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_attachment__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_attachment_check__REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_local_core__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_local_core_check__REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_local_reference__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_local_reference_check__REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_outgoing__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_outgoing_check__REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_positive_hopping_reexpression__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_positive_hopping_reexpression_check__REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_source_robustness__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_source_robustness_check__REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_source_tolerance_complete__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_source_tolerance_complete_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/prepared_core_composition_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/prepared_core_dwell_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/prepared_core_recovery__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_compact_receiver__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_compact_receiver_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_complete_candidate__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_complete_candidate_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_local_escape__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_local_escape_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_outgoing__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_outgoing_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_reference_tail__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_reference_time__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_reference_time_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_traveling_interface__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_traveling_interface_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_weighted_reference_time__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_weighted_reference_time_check__REVIEW.md',
)


def main():
    import numpy as np
    import sympy as sp
    root = Path(__file__).resolve().parents[1]
    checks = []
    def check(label, condition):
        checks.append(bool(condition))
        print(f"[{'PASS' if condition else 'FAIL'}] {label}")
    binding = json.loads((root / 'outputs/common_source_offset_2026_10_17/landing/PROOF_INPUT_BINDING.json').read_text())
    check('183 resolved historical proof/source pins match bytes', len(binding['pins']) == 183 and all(hashlib.sha256((root / r['path']).read_bytes()).hexdigest() == r['sha256'] for r in binding['pins']))

    # Exact symbolic finite prefix, with an arbitrary centered port diagonal.
    r0,r1,r2,a,b,c,z = sp.symbols('r0 r1 r2 a b c z', real=True)
    H = sp.Matrix([[r0,-a,0,0],[-a,r1,-b,0],[0,-b,r2,-c],[0,0,-c,z]])
    v = H**3 * sp.Matrix([1,0,0,0])
    expected = sp.Matrix([r0**3+a*a*(2*r0+r1),-a*(r0*r0+r0*r1+r1*r1+a*a+b*b),a*b*(r0+r1+r2),-a*b*c])
    check('third prefix application has all four stated coefficients, independent of port shift', all(sp.expand(x)==0 for x in v-expected))
    check('fourth application sees port shift: later-moment independence is not inferred', sp.diff((H*v)[3],z)==-a*b*c)
    y,m = sp.symbols('y m')
    S = sp.Matrix([[y-r0,a,0],[a,y-r1,b],[0,b,y-r2-c*c*m]])
    determinant = ((y-r0)*(y-r1)-a*a)*(y-r2-c*c*m)-b*b*(y-r0)
    check('three-source Schur determinant retains physical load symbol m', sp.expand(S.det()-determinant)==0)

    # Direct inverses at finite interior-band samples; independent density formula.
    errors=[]; wrong=[]
    for offset in (-.17, .0, .19):
        for residual in (-.001,.001):
            lam=.02; j=1.; aa=lam*np.sqrt((1+residual)/3); bb=lam*np.sqrt(8*(1-residual)/3); cc=np.sqrt(3*j*lam*(1+residual/2))
            rr=lam*residual*np.array([1.,-.5,.25])
            for delta in np.linspace(-1.8,1.8,9):
                yy=delta-offset; load=(delta-1j*np.sqrt(4-delta*delta))/2
                M=np.diag((yy-rr).astype(complex)); M[0,1]=M[1,0]=aa;M[1,2]=M[2,1]=bb;M[2,2]-=cc*cc*load
                q=((yy-rr[0])*(yy-rr[1])-aa*aa)*(yy-rr[2]-cc*cc*load)-bb*bb*(yy-rr[0])
                rho=cc*cc*aa*aa*bb*bb*np.sqrt(1-delta*delta/4)/(np.pi*abs(q)**2)
                measured=-np.linalg.inv(M)[0,0].imag/np.pi
                errors.append(abs(measured-rho)/max(rho,1e-30))
                wrong_load=(yy-1j*np.sqrt(max(0,4-yy*yy)))/2
                wrong.append(abs(load-wrong_load))
    check('54 direct Jacobi inverse density samples agree with physical-band formula', max(errors)<1e-9)
    check('offset changes physical load; recentered-load substitution is detectably different', max(wrong)>.01)

    # Conservative published ceilings are premises; arithmetic does not prove them.
    with localcontext() as ctx:
        ctx.prec=60
        D=Decimal
        terms=[D(s) for s in ('4.1e-11','.000117','.000505','.000319','.00004301','3.1e-7','4.04e-10')]
        total=sum(terms)
        check('seven complete-budget ceilings sum exactly and leave finite-cut allowance',total==D('.000984320445') and total+D('1e-10')<D('.000986'))
        eps=D('1e-6'); lam=D('1e-13'); j=D('.003'); offset=D('1e-12'); g=D('5e-8')
        B=20*eps+16*eps**2+4*eps**3
        beta=3*(lam+offset)/D('.0027'); margin=1-beta-B
        A=(1+eps)**2+(1+eps)/3
        b0=D(46000)/D('.0053')+D(290)/g; a0=D('8e-18'); kap2=3*j*lam*(1+eps)
        theta=kap2*((A/margin)*((a0+b0*offset)/lam+b0)+6*(a0+b0*D('2.4e-8')))
        check('conservative loaded-margin arithmetic retains common-offset term',theta<D('.000077') and (1-theta)*margin>D('.9999029'))
        Te=(eps**3+eps*(1+eps))**2+3*(1+eps)*(1+eps+eps**2)**2+8*eps**2*(1+eps)**2
        mu=lam**6*Te+D(8)/3*j*lam**5*(1+eps)**3
        check('sixth-moment envelope and original-window concentration arithmetic',mu<D('8.000026e-68') and (2*mu).sqrt()/D('2.14e-8')**3<D('4.1e-11'))
        sinh1=(D(1).exp()-D(-1).exp())/2
        exponent=-D(50000000)+4*g*D('2e14')*sinh1
        check('weighted finite-cut exponent below -2960000',exponent<D(-2960000))
        check('six-block construction counts',50000000+243==50000243 and 2*50000000+281==100000281)
    print('Scope: finite symbolic identities,54 numerical density samples and ceiling arithmetic; full analytical interfaces, time estimates, parent calibration and physical identification remain supplied proof obligations.')
    print(f'TOTAL: PASS={sum(checks)} FAIL={len(checks)-sum(checks)}')
    return 0 if all(checks) else 1


if __name__ == '__main__':
    raise SystemExit(main())
