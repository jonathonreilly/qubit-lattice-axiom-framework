#!/usr/bin/env python3
"""Fresh exact-source microscopic controls; residence proof is analytic."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/MICROSCOPIC_GROUND_ENERGY_AND_FORMATION_BUDGET_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/NATIVE_GROUND_ENERGY_AND_ORIGINAL_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-25.md', '.claude/science/physics-loops/mobile-record-microscopic-energy-budget-20260925/runtime/primitive_spin_energy_controls.py')
OUTPUT_DIRECTORY = 'outputs/microscopic_energy_budget_20260925'
RUNTIME = '.claude/science/physics-loops/mobile-record-microscopic-energy-budget-20260925/runtime/primitive_spin_energy_controls.py'
from pathlib import Path
import hashlib,json,os,subprocess,sys,tempfile,time

def main():
    root=Path(__file__).resolve().parents[1];out=root/OUTPUT_DIRECTORY
    out.mkdir(parents=True,exist_ok=True);tick=time.perf_counter()
    sha=lambda raw:hashlib.sha256(raw).hexdigest()
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix='microscopic-energy-budget-') as tmp:
        source=Path(tmp)/Path(RUNTIME).name;source.write_bytes((root/RUNTIME).read_bytes())
        r=subprocess.run([sys.executable,str(source)],cwd=tmp,capture_output=True,env=env)
        for stream,data in [('stdout',r.stdout),('stderr',r.stderr)]:
            (out/('microscopic_control.'+stream+'.txt')).write_bytes(data)
        if r.returncode or r.stderr:raise RuntimeError(r.stderr.decode())
        artifact=Path(tmp)/'SPIN_ENERGY_CONTROL_RESULTS.json'
        data=artifact.read_bytes();json.loads(data)
        assert data==r.stdout
        (out/artifact.name).write_bytes(data)
    result={'scope':'Fresh reuse of exact root cycle controls for the microscopic transfer; no numerical cubic residence theorem or new independent check.',
      'source_sha256':sha(Path(__file__).read_bytes()),'runtime_source_sha256':sha((root/RUNTIME).read_bytes()),
      'elapsed_seconds':time.perf_counter()-tick,'exit_code':r.returncode,'stderr_bytes':len(r.stderr),
      'stdout_bytes':len(r.stdout),'stdout_sha256':sha(r.stdout),
      'complete_scientific_artifact':{'path':OUTPUT_DIRECTORY+'/'+artifact.name,'sha256':sha(data),'bytes':len(data)},
      'all_assertions_passed':True}
    text=json.dumps(result,indent=2,allow_nan=False)+'\n'
    (out/'MICROSCOPIC_ENERGY_BUDGET_PUBLIC_RESULTS.json').write_text(text)
    print(text,end='');print('TOTAL_PASS: 1')

if __name__=='__main__':main()
