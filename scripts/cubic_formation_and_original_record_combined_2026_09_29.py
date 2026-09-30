#!/usr/bin/env python3
"""Reproduce the three reviewed formation results with one cold quotient.

The supplied laws, complete first vectors, exact certificates and fixed8192
response evaluations are unchanged. All intermediates are rebuilt in one
private temporary directory. Numerical estimates retain their original limits.
"""
from pathlib import Path
import json
import tempfile
import cube_formation_matter_flux_dynamics_2026_09_26 as cube
import cubic_one_pair_band_and_birth_2026_09_26 as local
import cubic_closed_quotient_2026_09_26 as quotient
import cubic_closed_band_numerics_2026_09_26 as spectrum
import cubic_exact_zero_energy_2026_09_26 as energy
import cubic_exact_zero_gap_2026_09_26 as gap
import cubic_exact_velocity_pocket_2026_09_26 as pocket
import cubic_original_record_hazard_2026_09_26 as hazard
import cubic_original_record_response_2026_09_26 as response
import cubic_original_record_error_bounds_2026_09_26 as errors

AUDIT_TIMEOUT_SEC = 12000
AUDIT_INPUT_PATHS = (
    'docs/CUBE_FORMATION_MATTER_FLUX_DYNAMICS_AND_STRONG_ELECTRIC_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-26.md',
    'docs/CUBIC_ONE_PAIR_BAND_ACTUAL_FIRST_BIRTH_LIMIT_AND_ELECTRIC_EXCITATION_BOUNDED_THEOREM_NOTE_2026-09-26.md',
    'docs/CUBIC_ORIGINAL_RECORD_RESPONSE_AT_FIXED_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-09-26.md',
    'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'scripts/cube_formation_matter_flux_dynamics_2026_09_26.py',
    'scripts/cube_formation_incidence_2026_09_26.py',
    'scripts/cubic_one_pair_band_and_birth_2026_09_26.py',
    'scripts/cubic_one_pair_primitives_2026_09_26.py',
    'scripts/cubic_one_pair_incidence_2026_09_26.py',
    'scripts/cubic_closed_quotient_2026_09_26.py',
    'scripts/cubic_closed_band_numerics_2026_09_26.py',
    'scripts/cubic_exact_zero_energy_2026_09_26.py',
    'scripts/cubic_exact_zero_gap_2026_09_26.py',
    'scripts/cubic_exact_velocity_pocket_2026_09_26.py',
    'scripts/cubic_original_record_hazard_2026_09_26.py',
    'scripts/cubic_original_record_response_2026_09_26.py',
    'scripts/cubic_original_record_error_bounds_2026_09_26.py',
)


def calculate():
    c = cube.calculate(cube.exact_construction())
    for name, expected in [('resolved_minus', 0), ('resolved_plus', -24), ('coherent', -12)]:
        x = c['outcomes'][name]['exact_initial_moments']['sine_electric_circulation']
        assert x['impulse_initial_slope_numerator'] == expected * x['denominator']
    assert c['electric_loop'] == [0, 1, -1, 0, 0, 0, 0, 0, 0, -1, 1, 0]
    assert c['H_Gamma_commutator_max_abs'] > 0
    print(json.dumps({'cube_result': c, 'local_instrument_checks': local.calculate()}, indent=2), flush=True)
    bounds = errors.calculate()
    refined = errors.calculate_refined()
    with tempfile.TemporaryDirectory(prefix='cubic-reviewed-combined-') as tmp:
        work = Path(tmp)
        quotient.build(work)
        spectrum.calculate(work)
        energy.calculate(work)
        gap.calculate(work)
        pocket.calculate(work)
        g = hazard.calculate(work)
        r = response.calculate(work)
        p = json.loads((work / 'VELOCITY_POCKET_CERTIFICATE.json').read_text())
        z = json.loads((work / 'ZERO_ENERGY_CERTIFICATE.json').read_text())
        print(json.dumps({
            'status': 'complete combined reproduction; exact conditional certificates and qualified numerical diagnostics',
            'ground_energy_interval_width': z['width'],
            'escape_speed_bound': p['escape_speed_lower_choice'],
            'escape_probability_bound': p['escape_probability_lower_choice'],
            'conditional_analytic_error_bound': bounds['normalized_total_error_certified_upper'],
            'refined_conditional_analytic_error_bound': refined['normalized_total_error_certified_upper'],
            'original_hazard_dimension': g['dimension'], 'response': r,
            'limits': 'Supplied models and stated limits only; response intervals require iid exact integrands. Floating evaluation, physical identification and calibration are separate.'
        }, indent=2), flush=True)
    print('Verification complete: all three conditional source results reproduced; no audit verdict.')


if __name__ == '__main__':
    calculate()
