from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_DRESSED_PATCH_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_PROBE_LOOP_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/FOUR_LAYER_COLLECTIVE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/MICROSCOPIC_GROUND_WINDOW_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/FEATURE_INTERACTION_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_probe_second_order.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_patch_bound_control.py']
def run(name):
 r=subprocess.run([sys.executable,str(P/name)],check=True,capture_output=True,text=True,timeout=90)
 return json.loads(r.stdout)
result=dict(status='bounded-support',second_order=run('neutral_probe_second_order.py'),bounds=run('neutral_patch_bound_control.py'),scope='Native extended trial feature and asymptotic dressed flux, no exact radius or cosmological identification')
f=ROOT/'outputs/native_dressed_patch/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
