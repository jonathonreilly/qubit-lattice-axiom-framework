#!/usr/bin/env python3
"""Exact-source original birth charge and grouping dynamics controls."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ORIGINAL_BIRTH_CHARGE_AND_GROUPING_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md', '.claude/science/physics-loops/mobile-record-birth-charge-transport-20260925/runtime/charge_cluster_controls.py', '.claude/science/physics-loops/mobile-record-birth-charge-transport-20260925/runtime/cluster_escape_controls.py', '.claude/science/physics-loops/mobile-record-birth-charge-transport-20260925/runtime/birth_geometry.py')
OUTPUT_DIRECTORY = 'outputs/native_birth_charge_transport_20260925'
RUNTIMES = ('.claude/science/physics-loops/mobile-record-birth-charge-transport-20260925/runtime/charge_cluster_controls.py', '.claude/science/physics-loops/mobile-record-birth-charge-transport-20260925/runtime/cluster_escape_controls.py', '.claude/science/physics-loops/mobile-record-birth-charge-transport-20260925/runtime/birth_geometry.py')

from pathlib import Path
import hashlib,json,os,subprocess,sys,tempfile,time

def main():
    root=Path(__file__).resolve().parents[1];out=root/OUTPUT_DIRECTORY
    out.mkdir(parents=True,exist_ok=True);tick=time.perf_counter();artifacts=[]
    sha=lambda raw:hashlib.sha256(raw).hexdigest()
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix='birth-charge-transport-') as tmp:
        for rel in RUNTIMES:(Path(tmp)/Path(rel).name).write_bytes((root/rel).read_bytes())
        for rel,label in zip(RUNTIMES[:2],('charge','transport')):
            program=Path(tmp)/Path(rel).name
            run=subprocess.run([sys.executable,'-B',str(program)],cwd=tmp,capture_output=True,env=env)
            (out/(label+'.stdout.json')).write_bytes(run.stdout)
            (out/(label+'.stderr.txt')).write_bytes(run.stderr)
            if run.returncode or run.stderr:raise RuntimeError(run.stderr.decode())
            data=json.loads(run.stdout)
            assert data['source_sha256']==sha(program.read_bytes())
            if label=='charge':assert data['all_assertions_passed'] and data['counts']['primitive_paths']==8448
            else:
                assert data['personal42_helper_sha256']==sha((Path(tmp)/'birth_geometry.py').read_bytes())
                assert len(data['results'])==2 and all(r['all_integer_Gauss_and_coefficient_assertions'] for r in data['results'])
            artifacts.append(dict(label=label,path=OUTPUT_DIRECTORY+'/'+label+'.stdout.json',
                sha256=sha(run.stdout),bytes=len(run.stdout),exit_code=0,stderr_bytes=0,
                runtime_source_sha256=sha(program.read_bytes())))
    result=dict(scope='Conditional original-birth charge and supplied-input grouping dynamics; no new independence, particle lifetime, units or empirical claim.',
        source_sha256=sha(Path(__file__).read_bytes()),artifacts=artifacts,
        runtime_sha256={rel:sha((root/rel).read_bytes()) for rel in RUNTIMES},
        elapsed_seconds=time.perf_counter()-tick,all_assertions_passed=True)
    output=json.dumps(result,indent=2,allow_nan=False)+'\n'
    (out/'BIRTH_CHARGE_TRANSPORT_PUBLIC_RESULTS.json').write_text(output)
    print(output,end='');print('TOTAL_PASS: 1')

if __name__=='__main__':main()
