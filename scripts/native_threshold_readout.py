from pathlib import Path
import sys,subprocess,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/THRESHOLD_READOUT_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_CONSTITUENT_SCATTERING_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/MICROSCOPIC_LARGE_FEATURE_WINDOW_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/LARGE_BOUND_FEATURE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_threshold_readout_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_readout_resolvent_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_mobility_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_threshold_highprecision.py']
checks={}
for name in ['neutral_readout_resolvent_control.py','neutral_threshold_readout_control.py']:
 r=subprocess.run([sys.executable,str(P/name)],check=True,capture_output=True,text=True,timeout=120);checks[name]=r.stdout.strip()
out=dict(status='bounded-support',checks=checks,scope='Coefficient response controls and inherited analytic microscopic smooth-measure transfer; no full-H numerical spectrum or empirical data')
f=ROOT/'outputs/native_threshold_readout/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
