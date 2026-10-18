from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/CHARGED_COLUMN_POLE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/WHOLE_COLUMN_MODE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_LAYER_NEUTRAL_POLE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/REFLECTION_GROUND_SECTOR_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_charged_column_control.py']
r=subprocess.run([sys.executable,str(P/'neutral_charged_column_control.py')],capture_output=True,text=True,check=True,timeout=90);control=json.loads(r.stdout)
assert control['gamma']=='12155/33554432'
assert all(x['amplitude_correction']=='-5/8' and x['weight_correction']=='-5/4' and x['minimum_shapes']==[[1,1,8]] for x in control['rows'])
assert all(x['next_perimeter']==12 for x in control['rows'][1:])
out=dict(status='conditional-support',scope='Native bond-level source dressing and charged geometry controls; actual-grid transfer analytic; charged source is not neutral ZZ source',control=control)
f=ROOT/'outputs/native_charged_column_pole/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
