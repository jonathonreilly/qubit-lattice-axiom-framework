#!/usr/bin/env python3
"""Exact-source native charge and global threshold controls."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/NATIVE_BIRTH_CHARGE_AND_SEPARATED_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/NATIVE_GROUND_ENERGY_AND_ORIGINAL_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'scripts/review_support/unit28/pr9213/two_record_threshold_and_charge_controls.py']
OUTPUT_DIRECTORY = 'outputs/native_charge_threshold_20260925'
RUNTIME = 'scripts/review_support/unit28/pr9213/two_record_threshold_and_charge_controls.py'

from pathlib import Path
import hashlib,json,os,subprocess,sys,tempfile,time

def main():
    root=Path(__file__).resolve().parents[1];out=root/OUTPUT_DIRECTORY
    out.mkdir(parents=True,exist_ok=True);tick=time.perf_counter()
    sha=lambda data:hashlib.sha256(data).hexdigest()
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix='native-charge-threshold-') as tmp:
        source=Path(tmp)/Path(RUNTIME).name;source.write_bytes((root/RUNTIME).read_bytes())
        artifact=Path(tmp)/'CHARGE_THRESHOLD_RESULTS.json'
        run=subprocess.run([sys.executable,'-B',str(source),'--output',str(artifact)],cwd=tmp,capture_output=True,env=env)
        for label,data in [('stdout',run.stdout),('stderr',run.stderr)]:
            (out/('charge_control.'+label+'.txt')).write_bytes(data)
        if run.returncode or run.stderr:raise RuntimeError(run.stderr.decode())
        data=artifact.read_bytes();full=json.loads(data);summary=json.loads(run.stdout)
        omitted={'unwrapped_rows','periodic_controls','reciprocity_controls','auxiliary_one_occupancy_kernel'}
        assert summary=={k:v for k,v in full.items() if k not in omitted}
        assert full['source_sha256']==sha(source.read_bytes())
        (out/artifact.name).write_bytes(data)
    result={'scope':'Fresh exact-source primitive controls of conditional global flat threshold and native birth charges; no new independence, finite-g dynamics or physical calibration.',
      'source_sha256':sha(Path(__file__).read_bytes()),'runtime_source_sha256':sha((root/RUNTIME).read_bytes()),
      'elapsed_seconds':time.perf_counter()-tick,'exit_code':run.returncode,'stderr_bytes':len(run.stderr),
      'stdout_bytes':len(run.stdout),'stdout_sha256':sha(run.stdout),
      'complete_scientific_artifact':{'path':OUTPUT_DIRECTORY+'/'+artifact.name,'sha256':sha(data),'bytes':len(data)},
      'all_assertions_passed':True}
    output=json.dumps(result,indent=2,allow_nan=False)+'\n'
    (out/'NATIVE_CHARGE_THRESHOLD_PUBLIC_RESULTS.json').write_text(output)
    print(output,end='');print('TOTAL: PASS=1 FAIL=0')

if __name__=='__main__':main()
