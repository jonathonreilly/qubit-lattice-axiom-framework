"""Conditional error-direction geometry and an exposed Cassini model challenge.

Offline scientific execution. Public-input acquisition is separate. A failed
candidate model is not a scalar signal or a physical error-energy calibration.
"""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/CASSINI_ERROR_DIRECTION_MODEL_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/cassini_error_direction.py',
    'scripts/cassini_error_direction_development.py',
    'scripts/cassini_error_direction_sampling.py',
    'scripts/cassini_error_direction_inputs.json',
    '.claude/science/physics-loops/observations-backward-24h-20261014/calibration_supplier/DEVELOPMENT_PROTOCOL_v1.json',
    '.claude/science/physics-loops/observations-backward-24h-20261014/calibration_supplier/DIRECTION_TEST_PROTOCOL_v1.json',
]
from pathlib import Path
import argparse,hashlib,json,subprocess
import numpy as np
import cassini_error_direction as geometry
import cassini_error_direction_development as development
import cassini_error_direction_sampling as sampling

ROOT=Path(__file__).resolve().parents[1]


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def acquire(cache):
    cache.mkdir(parents=True,exist_ok=True)
    entries=json.loads((ROOT/'scripts/cassini_error_direction_inputs.json').read_text())['products']
    for e in entries:
        p=cache/e['filename']
        if p.exists():
            if sha(p)!=e['sha256']:raise ValueError('cached input mismatch: '+p.name)
            continue
        if not e['url'].startswith('https://atmos.nmsu.edu/pdsd/archive/'):
            raise ValueError('unregistered input host')
        tmp=p.with_suffix(p.suffix+'.partial')
        subprocess.run(['/usr/bin/curl','--fail','--location','--max-time','90',e['url'],'--output',str(tmp)],check=True)
        if sha(tmp)!=e['sha256']:raise ValueError('downloaded input mismatch')
        tmp.replace(p)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input-cache',type=Path,default=ROOT/'outputs/cassini_rsr_inputs')
    ap.add_argument('--output-dir',type=Path,default=ROOT/'outputs/cassini_error_direction')
    ap.add_argument('--fetch-inputs',action='store_true');a=ap.parse_args()
    if a.fetch_inputs:
        acquire(a.input_cache);print('Pinned public inputs acquired; run again without --fetch-inputs for offline calculation.');return
    g=geometry.controls();s=sampling.run();r=development.receiver_controls()
    d=development.run(a.output_dir,a.input_cache)
    rows=[json.loads(x) for x in (a.output_dir/'DIRECTION_ROWS_v1.jsonl').read_text().splitlines()]
    checks={
        'all_registered_records':len(rows)==1200 and {v['band'] for v in rows}=={'X','Ka'},
        'fixed_window_each_band':all([v['second'] for v in rows if v['band']==b]==list(range(48900,49500)) for b in ['X','Ka']),
        'all_training_estimates_finished':all(v['result']['training_fit_success'] for v in rows),
        'all_records_retained_with_flags':all(v['extremes']==v['error_count']==0 for v in rows),
        'expected_gain_settings_retained':d['headers']['X']['FGAIN']=={'38':600} and d['headers']['Ka']['FGAIN']=={'44':600},
        'both_nominal_allocations_retained':all(set(v['result']['direction_challenge'])=={'pointwise','family_1200'} for v in rows),
        'lower_tail_ranks':all(v['result']['color_at_training_frequency']['low_rank']==248 and v['result']['color_at_training_frequency']['high_rank']==251 for v in rows),
        'quantized_model_status_honest':not d['physical_noise_scale_calibrated'] and not d['physical_noise_direction_law_derived'],
        'development_not_independent_test':d['independent_empirical_tests']==0,
    }
    # An actual sample-split fixture: changing validation cannot change g.
    n=500;t=geometry.times(n,1000.);train=(20+5j)*np.exp(2j*np.pi*.123*t)
    altered=(3-17j)*np.exp(2j*np.pi*9.87*t)
    f0=development.diagnose(np.concatenate([train,train]))['training_frequency_Hz']
    f1=development.diagnose(np.concatenate([train,altered]))['training_frequency_Hz']
    checks['training_frequency_has_no_validation_input']=f0==f1
    for key,value in checks.items():
        if not value:raise AssertionError(key)
    for name,text in {
        'per_element':'checked: ideal complex ADC cell enlargement only; no element-level physical noise law inferred',
        'per_site':'checked and not executed — no spatial lattice site or gravitational source is reconstructed',
        'per_mode':'checked: orthogonal complex-mode ratios and deliberate direction-law counterexamples',
        'per_block':'checked: all1200 exposed records; conditional continuous-frequency enclosures evaluated in floating point',
        'lattice_wide':'checked and not executed — no lattice-wide probability, action, state or scale closure is asserted',
    }.items():print(name+': '+text)
    result=dict(status='conditional-support',primary_sha256=sha(Path(__file__)),
                source_inputs={p:sha(ROOT/p) for p in AUDIT_INPUT_PATHS},
                role='conditional scale elimination and exposed-development challenge of a single-tone uniform-error-direction model',
                geometry_controls=g,sampling_controls=s['controls'],receiver_controls=r,development_checks=checks,
                passed=len(g)+len(s['controls'])+len(r)+len(checks),failed=0,
                empirical_statistics=d['statistics'],nominal_family_probability=.01,
                probability_interpretation='Fixed-procedure property under supplied signal/direction/cadence/ADC premises; previously exposed observations are development, not an independent calibrated test.',
                outward_rounded_observational_certificate=False,
                physical_noise_scale_calibrated=False,physical_noise_law_derived=False,
                scalar_inference=False,independent_empirical_tests=0,
                products={p.name:sha(p) for p in sorted(a.output_dir.iterdir()) if p.name in ['SOURCE_FREEZE_v1.json','DIRECTION_ROWS_v1.jsonl','DIRECTION_SUMMARY_v1.json']})
    (a.output_dir/'SUMMARY_v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
