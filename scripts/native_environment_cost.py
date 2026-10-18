from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/ENVIRONMENT_COST_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_DRESSED_PATCH_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/EXTENDED_ENVIRONMENT_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_environment_cost_control.py']
r=subprocess.run([sys.executable,str(P/'neutral_environment_cost_control.py')],check=True,capture_output=True,text=True,timeout=90)
result=dict(status='bounded-support',control=json.loads(r.stdout),scope='Native conditional environment cost and upper flat-radius bound, not radius selection')
f=ROOT/'outputs/native_environment_cost/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
