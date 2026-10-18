from pathlib import Path
import json,subprocess,sys,os
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/CONSTRAINED_FERMION_ROUTE.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_majorana_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_feature_clifford_control.py']
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
controls=[]
for path in AUDIT_INPUT_PATHS[1:]:
 r=subprocess.run([sys.executable,str(ROOT/path)],capture_output=True,text=True,check=True,timeout=45,env=env)
 controls.append(json.loads(r.stdout))
assert controls[0]['status']=='exact-algebra-pass'
c=controls[1]
assert c['isometry_error']<1e-12 and max(c['compression_errors'])<1e-12
assert all(r['leakage_norm']>1 for r in c['native_challenge'])
out=dict(status='bounded-support',scope='Constrained representation and explicitly chosen code failure; no derived physical fermion or observational test',controls=controls)
p=ROOT/'outputs/native_constrained_fermion/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
