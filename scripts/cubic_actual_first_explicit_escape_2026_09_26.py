#!/usr/bin/env python3
"""Reconstruct the whole quotient and verify exact finite-time escape witnesses.

Cold execution typically takes tens of minutes. Floating calculations propose
certificate vectors/bases; the final energy, gap and pocket inequalities use
integer/rational arithmetic. The numerical curvature is separately labeled.
No precomputed database or binary evidence is required or published.
"""
from pathlib import Path
import json
import tempfile
import cubic_one_pair_band_and_birth_2026_09_26 as local
import cubic_closed_quotient_2026_09_26 as quotient
import cubic_closed_band_numerics_2026_09_26 as spectrum
import cubic_exact_zero_energy_2026_09_26 as energy
import cubic_exact_zero_gap_2026_09_26 as gap
import cubic_exact_velocity_pocket_2026_09_26 as pocket

AUDIT_TIMEOUT_SEC=5400
AUDIT_INPUT_PATHS=(
 'docs/CUBIC_ONE_PAIR_BAND_ACTUAL_FIRST_BIRTH_LIMIT_AND_ELECTRIC_EXCITATION_BOUNDED_THEOREM_NOTE_2026-09-26.md',
 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md',
 'scripts/cubic_one_pair_band_and_birth_2026_09_26.py',
 'scripts/cubic_one_pair_primitives_2026_09_26.py',
 'scripts/cubic_one_pair_incidence_2026_09_26.py',
 'scripts/cubic_closed_quotient_2026_09_26.py',
 'scripts/cubic_closed_band_numerics_2026_09_26.py',
 'scripts/cubic_exact_zero_energy_2026_09_26.py',
 'scripts/cubic_exact_zero_gap_2026_09_26.py',
 'scripts/cubic_exact_velocity_pocket_2026_09_26.py',
)


def calculate():
    print(json.dumps({'local_instrument_checks':local.calculate()},indent=2),flush=True)
    with tempfile.TemporaryDirectory(prefix='cubic-explicit-escape-') as tmp:
        work=Path(tmp)
        quotient.build(work)
        spectrum.calculate(work)
        energy.calculate(work)
        gap.calculate(work)
        pocket.calculate(work)
        p=json.loads((work/'VELOCITY_POCKET_CERTIFICATE.json').read_text())
        g=json.loads((work/'ZERO_GAP_CERTIFICATE.json').read_text())
        e=json.loads((work/'ZERO_ENERGY_CERTIFICATE.json').read_text())
        print(json.dumps({'status':'exact closure and conditional rational certificates verified',
              'ground_energy_interval_width':e['width'],
              'zero_gap_lower':g['zero_isolation_gap_lower_exact'],
              'postbirth_time_onset':p['postbirth_time_onset'],
              'escape_speed_bound':p['escape_speed_lower_choice'],
              'escape_probability_bound':p['escape_probability_lower_choice'],
              'scope':'conservative projected bounds; full-law errors and supplied hierarchy are proved in the note; no physical calibration'},indent=2),flush=True)


if __name__=='__main__':
    calculate()
