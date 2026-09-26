#!/usr/bin/env python3
"""Cold reproduction of the original-record large-volume response package.

Builds the complete H quotient and original-loss stencil from primitives,
checks exact local error constants, and performs two fixed4096 integrations.
All temporary binary intermediates are disposable; a lossless base64 payload
retains all sample values in the text cache, with seeds and design-array hashes. No private data file or inherited extract is read.
"""
from pathlib import Path
import json,tempfile
import cubic_one_pair_band_and_birth_2026_09_26 as local
import cubic_closed_quotient_2026_09_26 as quotient
import cubic_closed_band_numerics_2026_09_26 as spectrum
import cubic_original_record_hazard_2026_09_26 as hazard
import cubic_original_record_response_2026_09_26 as response
import cubic_original_record_error_bounds_2026_09_26 as errors

AUDIT_TIMEOUT_SEC=10800
AUDIT_INPUT_PATHS=(
 'docs/CUBIC_ORIGINAL_RECORD_RESPONSE_AT_FIXED_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-09-26.md',
 'docs/CUBIC_ONE_PAIR_BAND_ACTUAL_FIRST_BIRTH_LIMIT_AND_ELECTRIC_EXCITATION_BOUNDED_THEOREM_NOTE_2026-09-26.md',
 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md',
 'scripts/cubic_one_pair_band_and_birth_2026_09_26.py',
 'scripts/cubic_one_pair_primitives_2026_09_26.py',
 'scripts/cubic_one_pair_incidence_2026_09_26.py',
 'scripts/cubic_closed_quotient_2026_09_26.py',
 'scripts/cubic_closed_band_numerics_2026_09_26.py',
 'scripts/cubic_original_record_hazard_2026_09_26.py',
 'scripts/cubic_original_record_response_2026_09_26.py',
 'scripts/cubic_original_record_error_bounds_2026_09_26.py',
)

def calculate():
    print(json.dumps({'original_local_checks':local.calculate()},indent=2),flush=True)
    bounds=errors.calculate()
    with tempfile.TemporaryDirectory(prefix='cubic-original-record-response-') as tmp:
        work=Path(tmp);quotient.build(work);spectrum.calculate(work)
        g=hazard.calculate(work);r=response.calculate(work)
        print(json.dumps({'conditional_analytic_error_bound':bounds['normalized_total_error_certified_upper'],
              'original_hazard_dimension':g['dimension'],'response':r,
              'limits':'Conditional supplied-law finite-window uniform comparison, statistical iid integration assumption and noninterval floating numerics; no physical calibration or experimental success.'},indent=2),flush=True)

if __name__=='__main__':calculate()
