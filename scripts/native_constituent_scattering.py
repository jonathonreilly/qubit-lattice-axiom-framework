from pathlib import Path
import sys, subprocess, json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TWO_FEATURE_BREAKUP_CHECK.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_CONSTITUENT_SCATTERING_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_SCATTERING_TIME_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_scattering_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_scattering_resolvent_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_mobility_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_threshold_highprecision.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/LARGE_BOUND_FEATURE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/MICROSCOPIC_LARGE_FEATURE_WINDOW_PROOF.md']
checks={}
for name in ['neutral_scattering_resolvent_control.py','neutral_scattering_control.py']:
 r=subprocess.run([sys.executable,str(P/name)],check=True,capture_output=True,text=True,timeout=160)
 checks[name]=r.stdout.strip()
out=dict(status='bounded-support',checks=checks,scope='Native coefficient constituent scattering; broadened development controls, not full-H asymptotic scattering or empirical tests')
f=ROOT/'outputs/native_constituent_scattering/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
