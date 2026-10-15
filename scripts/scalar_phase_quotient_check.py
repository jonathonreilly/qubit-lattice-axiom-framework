#!/usr/bin/env python3
"""Conditional integer-history quotient and exposed archive consistency.

Reads four hash-pinned public inputs/labels from a supplied local cache.
Package integrity reads are the declared source files. No new raw product,
physical noise bound, field state, or gravity fit is supplied by this runner.
"""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_PHASE_QUOTIENT_INTEGER_HISTORY_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_phase_quotient_controls.py',
    'scripts/cassini_phase_quotient_development.py',
    'scripts/cassini_doppler_development_inputs.json',
    'scripts/cassini_atdf_decode.py',
    'scripts/cassini_odf_decode.py',
    '.claude/science/physics-loops/observations-backward-24h-20261014/calibration_error/DEVELOPMENT_PROTOCOL_v1.json',
]

import argparse
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path

import scalar_phase_quotient_controls as quotient
import cassini_phase_quotient_development as development


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-cache', type=Path, default=root/'outputs/cassini_doppler_inputs')
    parser.add_argument('--output-dir', type=Path, default=root/'outputs/scalar_phase_quotient')
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    math = quotient.run()
    with redirect_stdout(io.StringIO()):
        data = development.run(args.input_cache, args.output_dir)
    (args.output_dir/'mathematics.json').write_text(json.dumps(math, indent=2)+'\n')
    # Exact independently reimplemented development counts and ledgers are
    # comparisons, not physical uncertainties or independent observations.
    tests = {
        'all_rows_accounted_without_lift': data['outcomes']=={'quotient_reconstructed':91664},
        'no_quality_clipping': data['counts']['matched_endpoint_occurrences']==183329,
        'slip_diagnostic_not_erased': data['counts']['endpoint_occurrences_nonzero_item87']==18393,
        'good_lock_flags_do_not_imply_zero_diagnostic': data['counts']['intervals_good_locked_but_nonzero_item87']==13015,
        'all_registered_chains': data['streams']==8 and data['chains']==36,
        'all_equal_duration_triples': data['equal_duration_triples']==91593,
        'native_modulus_comparison': data['max_abs_error_mod_M_cycles']['numerator']==100849 and data['max_abs_error_mod_M_cycles']['denominator']==132600000000,
        'one_cycle_comparison': data['max_abs_error_mod_one_cycles']==data['max_abs_error_mod_M_cycles'],
        'third_difference_comparison': data['max_abs_triple_format_difference_cycles']['numerator']==893 and data['max_abs_triple_format_difference_cycles']['denominator']==500000000,
        'row_ledger_reproduced': data['ledgers']['rows']['uncompressed_sha256']=='79a0e0dff422559c0620450afdf551dbe2a4dd22c0382ba7dbe0e49873b5ae08',
        'triple_ledger_reproduced': data['ledgers']['triples']['uncompressed_sha256']=='c3c8738eee6c0fae6aaf6f2b11694177839068cc83261cb550d40ececc338ddf',
    }
    for name, passed in tests.items():
        if not passed:
            raise AssertionError(name)
    inputs = [Path(__file__).resolve()]+[root/name for name in AUDIT_INPUT_PATHS]
    products = ['mathematics.json', 'QUOTIENT_DEVELOPMENT_RESULTS_v1.json',
                'QUOTIENT_ROWS_v1.jsonl.gz', 'QUOTIENT_TRIPLES_v1.jsonl.gz']
    summary = {
        'actual_current_surface_status':'conditional-support',
        'claim_type':'bounded_theorem',
        'mathematical_controls':math['passed'],
        'development_controls':tests,
        'checks_passed':math['passed']+len(tests),
        'source_sha256':{str(path.relative_to(root)):hashlib.sha256(path.read_bytes()).hexdigest() for path in inputs},
        'external_scientific_inputs_read':data['sources'],
        'product_sha256':{name:hashlib.sha256((args.output_dir/name).read_bytes()).hexdigest() for name in products},
        'independent_empirical_tests':0, 'fitted_parameters':0,
        'physical_energy_estimates':0, 'physical_error_bounds_inferred':0,
        'two_count_Gram_example':math['two_count_Gram_example'],
        'scope':data['scope'],
    }
    (args.output_dir/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))
    print('per_element: exact rational phase classes and all exposed Doppler rows checked; no physical noise certificate')
    print('per_site: checked and not executed — no lattice-site measurement or physical site identification is supplied')
    print('per_mode: exact finite Hilbert response and lattice fixtures checked; no observed scalar mode spectrum is inferred')
    print('per_block: all exposed count intervals and adjacent triples checked; no new empirical holdout or gravity test')
    print('lattice_wide: checked and not executed — continuum response hypotheses do not establish a microscopic TOE or state selector')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
