from pathlib import Path
from fractions import Fraction as F
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_LAYER_NEUTRAL_POLE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_LAYER_GROUND_SELECTION_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/WHOLE_COLUMN_MODE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/COLUMN_READOUT_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/ALL_HEIGHT_ASSISTED_HOP_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_eighth_rectangle.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_ten_layer_star.py']
a={}
for name in ['neutral_eighth_rectangle.py','neutral_ten_layer_star.py']:
 q=subprocess.run([sys.executable,str(P/name)],check=True,capture_output=True,text=True,timeout=60);a[name]=json.loads(q.stdout)
x=a['neutral_eighth_rectangle.py'];assert x['loops'][2]['coefficient']=='-9/262144';assert F(x['heights'][0]['v_over_two_gamma'])<1
G=F(12155,33554432);beta=F(165,17);weight=2*G*G*beta*beta/10
assert weight==F(2783620125,1125899906842624)
y=a['neutral_ten_layer_star.py'];r=y['rows'][-1]
assert abs(r['source_weight']-2)<3e-8
assert abs(r['curvature_scaled']/y['expected_curvature']-1)<3e-5
assert abs(r['splitting_scaled']/y['expected_splitting']-1)<5e-5
out=dict(status='conditional-support',controls=a,source_weight_coefficient=str(weight),scope='Actual selected-fibre zero-momentum pole in logarithmic boxes; positive curvature separately at coefficient level with q much smaller than lambda; no empirical scalar')
f=ROOT/'outputs/native_ten_layer_neutral_bound/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
