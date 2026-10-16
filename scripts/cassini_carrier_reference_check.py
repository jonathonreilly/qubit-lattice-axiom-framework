"""Reproduce conditional carrier geometry and an exposed receiver comparison.

Scientific execution is offline. --fetch-inputs acquires exact pinned public
files separately. No residual is promoted to a physical uncertainty estimate.
"""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/CASSINI_CARRIER_REFERENCE_FEASIBILITY_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/cassini_carrier_estimator.py',
    'scripts/cassini_receiver_reference.py',
    'scripts/cassini_carrier_geometry_controls.py',
    'scripts/cassini_rsr_development.py',
    'scripts/cassini_odf_decode.py',
    'scripts/cassini_atdf_decode.py',
    'scripts/cassini_atdf_odf_reconcile.py',
    'scripts/cassini_rsr_development_inputs.json',
    'scripts/cassini_doppler_development_inputs.json',
    '.claude/science/physics-loops/observations-backward-24h-20261014/receiver_reference/DEVELOPMENT_PROTOCOL_v1.json',
    '.claude/science/physics-loops/observations-backward-24h-20261014/receiver_reference/DEVELOPMENT_PROTOCOL_SUPPLEMENT_v1.json',
    '.claude/science/physics-loops/observations-backward-24h-20261014/receiver_reference/REFERENCE_COMPARISON_FREEZE_v1.json',
]
from pathlib import Path
import argparse,hashlib,json,subprocess
import cassini_carrier_estimator as carrier
import cassini_receiver_reference as reference
import cassini_carrier_geometry_controls as geometry

ROOT=Path(__file__).resolve().parents[1]
PROTOCOL=ROOT/'.claude/science/physics-loops/observations-backward-24h-20261014/receiver_reference'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def acquire(cache,entries):
    cache.mkdir(parents=True,exist_ok=True)
    for e in entries:
        path=cache/e['filename']
        if path.exists():
            if sha(path)!=e['sha256']:raise ValueError('cached input identity mismatch: '+path.name)
            continue
        if not e['url'].startswith('https://atmos.nmsu.edu/pdsd/archive/'):
            raise ValueError('unregistered input host')
        temporary=path.with_suffix(path.suffix+'.partial')
        subprocess.run(['/usr/bin/curl','--fail','--location','--max-time','90',e['url'],'--output',str(temporary)],check=True)
        if sha(temporary)!=e['sha256']:raise ValueError('downloaded input identity mismatch: '+path.name)
        temporary.replace(path)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--rsr-cache',type=Path,default=ROOT/'outputs/cassini_rsr_inputs')
    ap.add_argument('--tracking-cache',type=Path,default=ROOT/'outputs/cassini_doppler_inputs')
    ap.add_argument('--output-dir',type=Path,default=ROOT/'outputs/cassini_carrier_reference')
    ap.add_argument('--fetch-inputs',action='store_true');a=ap.parse_args()
    if a.fetch_inputs:
        acquire(a.rsr_cache,json.loads((ROOT/'scripts/cassini_rsr_development_inputs.json').read_text())['products'])
        acquire(a.tracking_cache,json.loads((ROOT/'scripts/cassini_doppler_development_inputs.json').read_text())['inputs'].values())
        print('Pinned public inputs acquired. Run again without --fetch-inputs for the offline calculation.');return
    g=geometry.controls();c=carrier.run(a.rsr_cache,a.output_dir,PROTOCOL);r=reference.run(a.tracking_cache,a.output_dir,PROTOCOL)
    rows=[json.loads(x) for x in (a.output_dir/'CARRIER_ESTIMATES_v1.jsonl').read_text().splitlines()]
    tests={
        'all_registered_blocks':len(rows)==1200 and all(c['statistics'][b]['blocks']==600 for b in ['X','Ka']),
        'no_flags_clipped':all(v['extreme_codes']==v['origin_reaching_cells']==v['error_count']==0 for v in rows),
        'all_fits_completed':all(v['estimate']['fit_success'] for v in rows),
        'exact_constant_modulus_rejection':all(v['amplitude_certificate']['quantization_only_rejected'] and v['amplitude_certificate']['common_amplitude_intersection_empty'] for v in rows),
        'all_same_interval_tracking_rows':r['matched_intervals']==600,
        'documented_S_exciter_reference_scale':r['stored_reference_Hz']['numerator']==2117064000 and r['stored_reference_Hz']['denominator']==1 and r['X_reference_Hz']['numerator']==1863016320000 and r['X_reference_Hz']['denominator']==221,
        'slip_diagnostics_preserved':r['ATDF_endpoint_nonzero_slip_diagnostics']==54,
        'dependent_storage_agreement':r['maximum_ODF_ATDF_sky_difference_Hz']<5e-7,
        'all_sign_timing_candidates_preserved':len(r['candidates'])==4,
        'source_supported_sign_development_consistency':r['candidates']['1']['RMS_Hz']<r['candidates']['0']['RMS_Hz'] and r['candidates']['3']['RMS_Hz']<r['candidates']['2']['RMS_Hz'],
        'no_bias_or_timing_fit':r['fitted_biases']==r['fitted_timeshifts']==0,
        'no_independent_empirical_gravity_test':r['independent_empirical_gravity_tests']==c['independent_empirical_tests']==0,
    }
    for key,value in tests.items():
        if not value:raise AssertionError(key)
    products={p.name:sha(p) for p in sorted(a.output_dir.iterdir()) if p.name in ['CARRIER_ESTIMATES_v1.jsonl','CARRIER_SUMMARY_v1.json','REFERENCE_COMPARISON_ROWS_v1.jsonl','REFERENCE_COMPARISON_SUMMARY_v1.json']}
    out=dict(status='conditional-support',role='carrier feasible-set theorem, finite-voltage model rejection and exposed receiver reconstruction',
             primary_sha256=sha(Path(__file__)),source_inputs={k:sha(ROOT/k) for k in AUDIT_INPUT_PATHS},
             geometry_controls=g,carrier_controls=c['controls'],development_checks=tests,
             passed=len(g)+len(c['controls'])+len(tests),failed=0,products=products,
             plus_sign_zero_shift_RMS_Hz=r['candidates']['1']['RMS_Hz'],reverse_sign_zero_shift_RMS_Hz=r['candidates']['0']['RMS_Hz'],
             fitted_real_parameters_per_block=3,physical_error_upper_bound_derived=False,independent_empirical_gravity_tests=0)
    (a.output_dir/'SUMMARY_v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
