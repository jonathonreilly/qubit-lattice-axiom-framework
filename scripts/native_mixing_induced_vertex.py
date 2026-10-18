from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/MIXING_INDUCED_VERTEX_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/BOUND_MODE_ENVIRONMENT_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_mixing_vertex.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_mixing_scattering.py']
a={}
for name in ['neutral_mixing_vertex.py','neutral_mixing_scattering.py']:
 q=subprocess.run([sys.executable,str(P/name)],check=True,capture_output=True,text=True,timeout=90);a[name]=json.loads(q.stdout)
assert a['neutral_mixing_vertex.py']['duhamel_error']<1e-12
assert a['neutral_mixing_scattering.py']['threshold_rows'][-1]['relative_error']<1e-5
out=dict(status='conditional-support',controls=a,scope='Native local matched vertex; separate pinned coefficient scattering, not full microscopic rate')
f=ROOT/'outputs/native_mixing_induced_vertex/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
