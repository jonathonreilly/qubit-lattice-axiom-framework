from pathlib import Path
import subprocess,sys,json
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_LAYER_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/WHOLE_COLUMN_MODE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/LIGHT_COLUMN_WINDOW_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/COLUMN_READOUT_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ALL_HEIGHT_ASSISTED_HOP_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_sixth_loop.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_sixth_star.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_sixth_torus.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_sixth_plaquette.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_sixth_plaquette_independent.py']
controls={}
for name in ['neutral_sixth_loop.py','neutral_sixth_star.py','neutral_sixth_torus.py','neutral_sixth_plaquette.py','neutral_sixth_plaquette_independent.py']:
 q=subprocess.run([sys.executable,str(P/name)],check=True,capture_output=True,text=True,timeout=90)
 if name=='neutral_sixth_plaquette.py':data=[json.loads(x) for x in q.stdout.splitlines()]
 elif name=='neutral_sixth_plaquette_independent.py':data=[dict(z=int(x.split()[0]),total=x.split()[1]) for x in q.stdout.splitlines()]
 else:data=json.loads(q.stdout)
 controls[name]=data
assert controls['neutral_sixth_loop.py'][1]['per_layer']=='-3/8192'
expected=['7/2048','-11/4608','-11/4608','0']
for name in ['neutral_sixth_plaquette.py','neutral_sixth_plaquette_independent.py']:assert [x['total'] for x in controls[name]]==expected
assert sum(map(F,expected))==F(-25,18432)
s=controls['neutral_sixth_star.py'];assert 2.11447531630064<s['E_over_t']<2.11447531630066
assert .1406861564<s['source_weight']<.1406861565
for row in controls['neutral_sixth_torus.py']:assert row['upper']>2 and row['next']<2
weight=float(F(63,8192)**2*F(121,54))*s['source_weight']
result=dict(status='conditional-support',controls=controls,original_pole_weight_coefficient=weight,scope='Actual selected-symmetry-fibre mode in weak-coupling logarithmic-box family; not global-ground or empirical scalar')
f=ROOT/'outputs/native_six_layer_neutral_pole/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
