from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/FOUR_LAYER_COLLECTIVE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/COLUMN_READOUT_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/WHOLE_COLUMN_MODE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_layer_geometry.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_layer_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_layer_development_results.json',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/diagnostics/four_layer_spatial_development.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/diagnostics/four_layer_periodic_development.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/diagnostics/four_layer_openz_development.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/diagnostics/four_layer_momentum_development.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/diagnostics/four_layer_profile_development.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/diagnostics/four_layer_probe_development.py']
r=subprocess.run([sys.executable,str(P/'neutral_four_layer_control.py')],check=True,capture_output=True,text=True,timeout=100)
result=dict(status='bounded-support',checks=json.loads(r.stdout),scope='Native finite-slab response theorem and coefficient controls; no bulk scalar identification')
f=ROOT/'outputs/native_four_layer_collective/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
