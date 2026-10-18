from pathlib import Path
import sys,json,numpy as np
ROOT=Path(__file__).resolve().parents[1]
NATIVE=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/BULK_COM_POLE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/BULK_COM_SOURCE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/FOURIER_GROUND_WINDOW_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/COM_DERIVATIVE_BOUNDARY.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_com_model.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_host.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_second_other.json']
sys.path.insert(0,str(NATIVE))
from neutral_com_model import run,residue
rows=[]
for p in [0,.3,.6]:
 for lam in [.1,.03,.01,.003]:
  r=run(p,lam);s=run(p,lam,1.2);r['cutoff_difference']=float(np.linalg.norm(np.array(r['coefficient'])-s['coefficient']))
  assert r['cutoff_difference']<1e-7 and r['residual']<1e-8 and r['predicted_width']>0
  r['source_residue']=residue(r)
  rows.append(r)
 assert rows[-1]['error']<.0002 and rows[-1]['source_residue']['error']<1e-5
raw=json.loads((NATIVE/'neutral_bulk_second_other.json').read_text());r=next(x for x in raw if x['ell']==4 and x['rx']==2)
assert sorted(x['coefficient'] for x in r['rows'])==['-1/2']*4+['-4']
result=dict(status='bounded-support',rows=rows,scope='Native endpoint coefficient check plus specified NN Airy/outgoing-host model, not full native mass or microscopic pole')
out=ROOT/'outputs/native_com_propagation/result.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
