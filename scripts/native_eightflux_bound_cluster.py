from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/COLUMN_READOUT_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/EIGHT_FLUX_BOUND_CLUSTER_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_eightflux_geometry.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_detour_winding.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_q8_source_control.py']
a={}
for name in ['neutral_eightflux_geometry.py','neutral_detour_winding.py','neutral_q8_source_control.py']:
 r=subprocess.run([sys.executable,str(P/name)],capture_output=True,text=True,check=True,timeout=90);a[name]=json.loads(r.stdout)
g=a['neutral_eightflux_geometry.py'];assert sorted((x['w'],x['h']) for x in g['minima'])==[(2,4),(4,2)]
assert len(g['paths'])==4
r=next(x for x in a['neutral_detour_winding.py']['rows'] if x['L']==10)
assert r['all_layers']=='-1076510135/10567230160896' and r['marked_ratio']=='1616665793187/110234637824'
s=a['neutral_q8_source_control.py'];assert s['coefficient']=='1361400132699035/945539748965690376192';assert abs(s['rows'][-1]['relative_error'])<1e-7
out=dict(status='conditional-support',scope='Native fixed-L coefficient and source controls; actual selected-fibre transfer is analytic, not full-grid ED; no empirical test',controls=a)
f=ROOT/'outputs/native_eightflux_bound_cluster/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
