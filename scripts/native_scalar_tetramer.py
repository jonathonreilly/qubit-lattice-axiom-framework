from pathlib import Path
import json,subprocess,sys
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_SCALAR_TETRAMER_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_tetramer_geometry.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_tetramer_order10.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_SECONDARY_ENERGY_CHECK.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_PAIR_SCATTERING_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_order10_pair_control.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md']
results=[]
for f in AUDIT_INPUT_PATHS[1:3]:
 r=subprocess.run([sys.executable,str(ROOT/f)],check=True,capture_output=True,text=True,timeout=60);results.append(json.loads(r.stdout))
g,d=results;assert g['tested']==4912
assert min(map(int,g['histogram']))==-5832 and g['histogram']['-5832']==4
assert sorted(map(int,g['histogram']))[1]==-2916
assert F(d['full_BminusA'])==F(949685,12230590464)
masks=[{(0,0),(1,0),(4,0),(5,0)},{(0,0),(1,0),(0,3),(1,3)}]
source=[]
for i,T in enumerate(masks):
 for rotated in [False,True]:
  S={(-y,x) for x,y in T} if rotated else T
  boundary=sum((x,y+dy) not in S for x,y in S for dy in [-1,1])
  assert boundary==(4 if rotated else 8)
  source.append(dict(family=i,rotated=rotated,crossing_Y_bonds_per_layer=boundary,weight_loss_coefficient_L10=str(F(10*boundary,16))))
out=dict(status='conditional-support',scope='Native excited tetramer binding and q0 A1 source; no mobility or on-shell selfcoupling claimed',geometry=g,order10=d,physical_X_source=source,scalar_covariant_weight_loss='5',binding_coefficient_L10=str(F(90,32768)))
p=ROOT/'outputs/native_scalar_tetramer/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
