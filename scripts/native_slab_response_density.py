from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/BULK_SLAB_RESPONSE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/PLAQUETTE_PROPAGATION_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/FOUR_LAYER_COLLECTIVE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_layer_geometry.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_response_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_moment_bound.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_plaquette_series_control.py']
def run(name,*args):
 r=subprocess.run([sys.executable,str(P/name),*args],check=True,capture_output=True,text=True,timeout=90)
 return json.loads(r.stdout)
result=dict(status='bounded-support',integer_moment_R13=run('neutral_bulk_moment_bound.py','13'),integer_moment_R17=run('neutral_bulk_moment_bound.py','17'),finite_moment_checks=run('neutral_bulk_response_control.py'),auxiliary_series=run('neutral_plaquette_series_control.py'),scope='Native coefficient response density theorem; ordered microscopic lambda then area limit, no bulk 3D scalar or empirical identification')
f=ROOT/'outputs/native_slab_response_density/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
