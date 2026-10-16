#!/usr/bin/env python3
"""Conditional channel arithmetic and exposed RSR representation, not gravity fitting."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_INTEGER_CHANNEL_CALIBRATION_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_channel_quotient_controls.py',
    'scripts/cassini_rsr_development.py',
    'scripts/cassini_nco_continuity.py',
    'scripts/cassini_rsr_development_inputs.json',
    '.claude/science/physics-loops/observations-backward-24h-20261014/channel_quotient/RSR_PREACCESS_PROTOCOL_v1.json',
]

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

import scalar_channel_quotient_controls as mathematics
import cassini_rsr_development as receiver
import cassini_nco_continuity as continuity


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    root=Path(__file__).resolve().parents[1]
    parser=argparse.ArgumentParser()
    parser.add_argument('--input-cache',type=Path,default=root/'outputs/cassini_rsr_inputs')
    parser.add_argument('--output-dir',type=Path,default=root/'outputs/scalar_channel_calibration')
    parser.add_argument('--fetch-inputs',action='store_true')
    args=parser.parse_args()
    manifest=json.loads((root/'scripts/cassini_rsr_development_inputs.json').read_text())
    if args.fetch_inputs:
        args.input_cache.mkdir(parents=True,exist_ok=True)
        for row in manifest['products']:
            dest=args.input_cache/row['filename']
            if dest.exists():
                if sha(dest)!=row['sha256']:raise ValueError('existing input hash mismatch: '+str(dest))
                continue
            temporary=dest.with_name(dest.name+'.partial')
            subprocess.run(['curl','--fail','--location','--silent','--show-error','--max-time','240',row['url'],'--output',str(temporary)],check=True)
            if sha(temporary)!=row['sha256']:raise ValueError('download input hash mismatch: '+str(dest))
            temporary.replace(dest)
        print('Four exact public inputs are available; no scientific inference performed by fetch.')
        return 0
    for row in manifest['products']:
        path=args.input_cache/row['filename']
        if sha(path)!=row['sha256']:raise ValueError('input hash mismatch: '+str(path))
    args.output_dir.mkdir(parents=True,exist_ok=True)
    math=mathematics.run()
    data=receiver.run(args.input_cache,args.input_cache,args.output_dir)
    nco=continuity.run(args.output_dir)
    tests={
        'both_complete_products':all(x['record_count']==8941 for x in data['products']),
        'fixed_window_without_quality_clipping':data['matched_window_records']==600 and data['sample_count']==600000,
        'no_unmatched_window_rows':not data['X_unmatched_keys'] and not data['Ka_unmatched_keys'],
        'independent_all_record_IQ_digest':sha(args.output_dir/'RSR_WINDOW_DIGESTS_v1.json')=='404103e8c376de30b7a38a3e58e4ccebd19c6c755c095ce4583cec909e332a9b',
        'finite_conditional_cells':data['ADC_invalid_cell_count']==0 and data['ADC_complete_circle_count']==0,
        'independent_ADC_width_summary':abs(data['character_ADC_width_cycles']['quantiles_0_01_50_99_100'][2]-0.0005482142770177202)<1e-12 and abs(data['character_ADC_width_cycles']['quantiles_0_01_50_99_100'][4]-0.1341142987521808)<1e-12,
        'physical_sky_phase_left_open':data['physical_sky_phase_restored'] is False,
        'both_phase_arguments_retained':all([t['shift_seconds'] for t in nco['products'][b]['tests']]==['0','1/2000'] for b in ('X','KA')),
        'all_NCO_joins_retained':all(t['count']==8940 for b in ('X','KA') for t in nco['products'][b]['tests']),
        'X_zero_shift_exact_identity':nco['products']['X']['tests'][0]['exact_residual_identity_sha256']=='9b3ffb17ecd701e4bbd6b65ff3eb7898253e67e1bac44a2eae0cb326dfb4a24d',
        'Ka_zero_shift_exact_identity':nco['products']['KA']['tests'][0]['exact_residual_identity_sha256']=='2bd89fc59dee693b662ede70e3903a64f1e6c1f6967ca9935558689e0200d1df',
    }
    for name,passed in tests.items():
        if not passed:raise AssertionError(name)
    (args.output_dir/'MATHEMATICAL_RESULTS.json').write_text(json.dumps(math,indent=2)+'\n')
    sources=[Path(__file__).resolve()]+[root/x for x in AUDIT_INPUT_PATHS]
    products=['MATHEMATICAL_RESULTS.json','RSR_DEVELOPMENT_RESULTS_v1.json','RSR_WINDOW_DIGESTS_v1.json','RSR_NCO_DIAGNOSTIC_v1.json','NCO_CONTINUITY_RESULTS_v1.json','X_HEADERS_v1.jsonl.gz','KA_HEADERS_v1.jsonl.gz','RSR_CHARACTER_v1.npz']
    summary={'claim_type':'bounded_theorem','actual_current_surface_status':'conditional-support',
        'mathematical_controls':math['count'],'receiver_fixture_controls':data['decoder_controls'],'development_checks':tests,
        'checks_passed':math['count']+data['decoder_controls']+len(tests),
        'source_sha256':{str(x.relative_to(root)):sha(x) for x in sources},
        'external_scientific_inputs':manifest['products'],
        'intermediate_reads':'NCO checker reads the two generated complete header ledgers from the pinned raw records',
        'product_sha256':{x:sha(args.output_dir/x) for x in products},
        'raw_products_role':'exposed development, no independent empirical test',
        'independent_empirical_tests':0,'fitted_parameters':0,'physical_error_bounds_inferred':0,'physical_sky_phase_restored':False}
    (args.output_dir/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    print('per_element: exact integer channel formulas and conditional ADC representation cells checked; no carrier noise identified')
    print('per_site: checked and not executed — no lattice site or microscopic measurement identification is supplied')
    print('per_mode: torus characters and finite algebraic examples checked; no observed scalar mode spectrum is inferred')
    print('per_block: complete registered headers and fixed600second receiver window checked; development comparisons only')
    print('lattice_wide: checked and not executed — these channel and receiver hypotheses do not establish a TOE or field state')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
