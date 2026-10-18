from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/COLUMN_READOUT_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/WHOLE_COLUMN_MODE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/FEATURE_INTERACTION_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_DIRECT_LOCAL_TENSION.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_column_readout_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_square_local_source.py']
checks={}
for name in ['neutral_column_readout_control.py','neutral_square_local_source.py']:
 r=subprocess.run([sys.executable,str(P/name)],check=True,capture_output=True,text=True,timeout=90);checks[name]=r.stdout.strip()
result=dict(status='bounded-support',checks=checks,scope='Exact coefficient and virtual-dressing controls; actual asymptotic feature contrast is analytic, not full-H numerical or empirical validation')
f=ROOT/'outputs/native_column_readout/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
