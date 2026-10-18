from pathlib import Path
import sys,json,numpy as np
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLE_ENVELOPE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_envelope_model.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_host.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_fourth_kernel.json']
sys.path.insert(0,str(P));from neutral_envelope_model import run
raw=json.loads((P/'neutral_slow_fourth_kernel.json').read_text())
for r in raw:
 ell=r['ell'];lo,hi=r['target'];pred=F(19,64) if (lo,hi)==(0,ell+1) else F(-13,256) if (lo,hi)==(0,ell+2) else F(0)
 assert F(r['coefficient'])==pred
assert F(29,192)+F(19,16)-F(13,64)==F(109,96)
rows=[]
for lam in [.1,.05,.03,.02,.01]:
 r=run(lam);s=run(lam,131072);r['grid_difference']=float(max(np.linalg.norm(np.array(a['actual'])-b['actual']) for a,b in zip(r['tests'],s['tests'])));assert r['grid_difference']<1e-10 and r['edge_mass']<1e-12;rows.append(r)
assert max(x['error'] for x in rows[-1]['tests'])<1e-6
result=dict(status='bounded-support',rows=rows,scope='Native coefficient checks plus approximate pole-kernel FFT controls and artificial rapid-phase stress test; not full microscopic signal or particle probability')
p=ROOT/'outputs/native_pole_envelope/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
