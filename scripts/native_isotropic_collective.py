from pathlib import Path
import sys,subprocess,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_COLLECTIVE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_isotropic_collective_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_isotropic_ir_control.py']
checks={}
for name in ['neutral_isotropic_collective_control.py','neutral_isotropic_ir_control.py']:
 r=subprocess.run([sys.executable,str(P/name)],check=True,capture_output=True,text=True,timeout=60);checks[name]=r.stdout.strip()
out=dict(status='bounded-support',checks=checks,scope='Exact native collective-sector boundary and first fluctuation channel; no full-H ED, ground phase, scalar identification or empirical tests')
f=ROOT/'outputs/native_isotropic_collective/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
