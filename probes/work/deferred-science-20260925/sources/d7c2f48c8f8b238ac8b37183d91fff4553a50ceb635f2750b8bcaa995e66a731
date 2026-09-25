#!/usr/bin/env python3
"""Exact-source original local charge and covariance controls."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ORIGINAL_LOCAL_CHARGE_CURRENT_AND_FINITE_TIME_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md', '.claude/science/physics-loops/mobile-record-local-charge-observation-20260925/runtime/current_noise_controls.py', '.claude/science/physics-loops/mobile-record-local-charge-observation-20260925/runtime/local_support_controls.py')
OUTPUT_DIRECTORY = 'outputs/native_local_charge_covariance_20260925'
RUNTIMES = ('.claude/science/physics-loops/mobile-record-local-charge-observation-20260925/runtime/current_noise_controls.py', '.claude/science/physics-loops/mobile-record-local-charge-observation-20260925/runtime/local_support_controls.py')

from pathlib import Path
import hashlib,json,os,subprocess,sys,tempfile,time

def main():
    root=Path(__file__).resolve().parents[1];out=root/OUTPUT_DIRECTORY
    out.mkdir(parents=True,exist_ok=True);tick=time.perf_counter();artifacts=[]
    sha=lambda raw:hashlib.sha256(raw).hexdigest()
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix='local-charge-covariance-') as tmp:
        for rel in RUNTIMES:(Path(tmp)/Path(rel).name).write_bytes((root/rel).read_bytes())
        for rel,label in zip(RUNTIMES,('current','finite_time')):
            program=Path(tmp)/Path(rel).name
            run=subprocess.run([sys.executable,'-B',str(program)],cwd=tmp,capture_output=True,env=env)
            (out/(label+'.stdout.json')).write_bytes(run.stdout)
            (out/(label+'.stderr.txt')).write_bytes(run.stderr)
            if run.returncode or run.stderr:raise RuntimeError(run.stderr.decode())
            data=json.loads(run.stdout)
            if label=='current':
                assert data['source_sha256']==sha(program.read_bytes())
                assert data['all_assertions_passed'] and data['primitive_count']==8480 and data['real_polarized_covariance_entries']==180
            else:
                assert data['program_sha256']==sha(program.read_bytes())
                assert data['status']=='all exact assertions passed' and [g['L'] for g in data['graphs']]==[4,6,8,12,16,20]
            artifacts.append(dict(label=label,path=OUTPUT_DIRECTORY+'/'+label+'.stdout.json',
                sha256=sha(run.stdout),bytes=len(run.stdout),exit_code=0,stderr_bytes=0,
                runtime_source_sha256=sha(program.read_bytes())))
    result=dict(scope='Conditional original local charge current and covariance; no time propagation, measured readout or empirical claim.',
        source_sha256=sha(Path(__file__).read_bytes()),artifacts=artifacts,
        runtime_sha256={rel:sha((root/rel).read_bytes()) for rel in RUNTIMES},
        elapsed_seconds=time.perf_counter()-tick,all_assertions_passed=True)
    output=json.dumps(result,indent=2,allow_nan=False)+'\n'
    (out/'LOCAL_CHARGE_OBSERVATION_PUBLIC_RESULTS.json').write_text(output)
    print(output,end='');print('TOTAL_PASS: 1')

if __name__=='__main__':main()
