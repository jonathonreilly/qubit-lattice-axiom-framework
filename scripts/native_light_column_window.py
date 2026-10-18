from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/LIGHT_COLUMN_WINDOW_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/COLUMN_READOUT_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/WHOLE_COLUMN_MODE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_light_window_control.py']
r=subprocess.run([sys.executable,str(P/'neutral_light_window_control.py')],check=True,capture_output=True,text=True,timeout=100)
result=dict(status='bounded-support',checks=json.loads(r.stdout),scope='Geometry and coefficient/mixing controls; actual microscopic window is an analytic fixed-box theorem, not a full-H numerical spectrum or observed scalar')
f=ROOT/'outputs/native_light_column_window/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
