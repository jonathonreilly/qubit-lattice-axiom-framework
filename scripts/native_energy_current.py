from pathlib import Path
import json,subprocess,sys,os
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_ENERGY_CURRENT_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_energy_current_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_ENERGY_SOURCE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md']
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
r=subprocess.run([sys.executable,str(ROOT/AUDIT_INPUT_PATHS[1])],check=True,capture_output=True,text=True,timeout=90,env=env)
c=json.loads(r.stdout)
assert max(x['operator_residual'] for x in c['continuity'])<1e-11
assert max(x['spectral_residual'] for x in c['continuity'])<1e-11
out=dict(status='bounded-support',scope='Native energy continuity and pole Ward relation; finite control is not an L10 pole or observation test',control=c)
p=ROOT/'outputs/native_energy_current/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
