from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_PROBE_LOOP_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/FOUR_LAYER_COLLECTIVE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_layer_geometry.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_probe_physical_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_probe_return_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_heavy_environment_control.py']
def run(name):
 r=subprocess.run([sys.executable,str(P/name)],check=True,capture_output=True,text=True,timeout=90)
 return json.loads(r.stdout)
result=dict(status='bounded-support',physical=run('neutral_probe_physical_control.py'),prepared_return=run('neutral_probe_return_control.py'),environment=run('neutral_heavy_environment_control.py'),scope='Native prepared-probe coupling and leading heavy environment selection; not universal matter coupling')
f=ROOT/'outputs/native_probe_loop_coupling/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
