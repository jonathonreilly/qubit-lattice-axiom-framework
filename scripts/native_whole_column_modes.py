from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/WHOLE_COLUMN_MODE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/MICROSCOPIC_GROUND_WINDOW_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/FEATURE_INTERACTION_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_winding_control.py']
r=subprocess.run([sys.executable,str(P/'neutral_winding_control.py')],check=True,capture_output=True,text=True,timeout=90)
result=dict(status='bounded-support',checks=json.loads(r.stdout),scope='Exact finite-size coefficient checks; microscopic asymptotic bounds supplied by linked analytic proof, not full-H numerics or empirical data')
f=ROOT/'outputs/native_whole_column_modes/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
