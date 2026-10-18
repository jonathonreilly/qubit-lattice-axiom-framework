from pathlib import Path
import subprocess,sys,json,os
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/REFLECTION_GROUND_SECTOR_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_reflection_ed.py']
env=dict(os.environ,OPENBLAS_NUM_THREADS='1')
r=subprocess.run([sys.executable,str(P/'neutral_reflection_ed.py')],capture_output=True,text=True,check=True,timeout=90,env=env);rows=json.loads(r.stdout)
assert len(rows)==6
assert max(abs(x['difference']) for x in rows)<1e-9
assert max(x['residual'] for x in rows)<1e-9
assert min(min(x['plane_expectations']) for x in rows)>1-1e-9
out=dict(status='exact-support',scope='Analytic finite even-lattice ground existence; small-grid sign controls only, no uniqueness or empirical test',rows=rows)
f=ROOT/'outputs/native_reflection_ground_sector/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
