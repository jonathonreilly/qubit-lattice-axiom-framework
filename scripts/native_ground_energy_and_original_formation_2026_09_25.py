#!/usr/bin/env python3
"""Fresh exact-source controls for native ground energy and formation."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/NATIVE_GROUND_ENERGY_AND_ORIGINAL_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md', '.claude/science/physics-loops/mobile-record-native-ground-20260925/runtime/pair/native_pair_controls.py', '.claude/science/physics-loops/mobile-record-native-ground-20260925/runtime/pair/native_pair_local_row_certificate.py', '.claude/science/physics-loops/mobile-record-native-ground-20260925/runtime/pair/native_pair_row_polynomial_certificate.py', '.claude/science/physics-loops/mobile-record-native-ground-20260925/runtime/filling/ground_filling_certificates.py', '.claude/science/physics-loops/mobile-record-native-ground-20260925/runtime/activity/primitive_rate_energy_controls.py')
OUTPUT_DIRECTORY = 'outputs/native_ground_20260925'
RUNTIME = ['.claude/science/physics-loops/mobile-record-native-ground-20260925/runtime/pair/native_pair_controls.py', '.claude/science/physics-loops/mobile-record-native-ground-20260925/runtime/pair/native_pair_local_row_certificate.py', '.claude/science/physics-loops/mobile-record-native-ground-20260925/runtime/pair/native_pair_row_polynomial_certificate.py', '.claude/science/physics-loops/mobile-record-native-ground-20260925/runtime/filling/ground_filling_certificates.py', '.claude/science/physics-loops/mobile-record-native-ground-20260925/runtime/activity/primitive_rate_energy_controls.py']
from pathlib import Path
import hashlib,json,os,subprocess,sys,tempfile,time

def main():
    root=Path(__file__).resolve().parents[1];out=root/OUTPUT_DIRECTORY
    out.mkdir(parents=True,exist_ok=True);tick=time.perf_counter();stages=[];artifacts=[]
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    sha=lambda raw:hashlib.sha256(raw).hexdigest()
    with tempfile.TemporaryDirectory(prefix='native-ground-') as tmp:
        work=Path(tmp)
        for rel in RUNTIME:
            p=Path(rel);dest=work/p.parent.name/p.name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes((root/rel).read_bytes())
        for rel in RUNTIME:
            p=Path(rel);source=work/p.parent.name/p.name;start=time.perf_counter()
            r=subprocess.run([sys.executable,str(source)],cwd=source.parent,capture_output=True,env=env)
            stem=p.parent.name+'_'+p.stem
            for stream,data in [('stdout',r.stdout),('stderr',r.stderr)]:
                path=out/(stem+'.'+stream+'.txt');path.write_bytes(data)
            stages.append({'program':rel,'source_sha256':sha(source.read_bytes()),'elapsed_seconds':time.perf_counter()-start,'exit_code':r.returncode,'stdout_sha256':sha(r.stdout),'stdout_bytes':len(r.stdout),'stderr_bytes':len(r.stderr)})
            if r.returncode or r.stderr:raise RuntimeError(p.name+': '+r.stderr.decode())
            if p.name=='ground_filling_certificates.py':(source.parent/'GROUND_FILLING_CERTIFICATES.json').write_bytes(r.stdout)
        for source in sorted(work.rglob('*.json')):
            data=source.read_bytes();json.loads(data);name=source.parent.name+'_'+source.name
            (out/name).write_bytes(data);artifacts.append({'path':OUTPUT_DIRECTORY+'/'+name,'sha256':sha(data),'bytes':len(data)})
    result={'scope':'Fresh reuse of personally derived source controls for three separately checked conditional arguments; no new independence or physical fit.','source_sha256':sha(Path(__file__).read_bytes()),'stages':stages,'complete_scientific_artifacts':artifacts,'elapsed_seconds':time.perf_counter()-tick,'all_assertions_passed':True}
    text=json.dumps(result,indent=2,allow_nan=False)+'\n';(out/'NATIVE_GROUND_PUBLIC_RESULTS.json').write_text(text)
    print(text,end='');print('TOTAL_PASS: 5')

if __name__=='__main__':main()
