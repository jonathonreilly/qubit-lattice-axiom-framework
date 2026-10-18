from pathlib import Path
import sys,subprocess,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/FIXED_OCCUPATION_LADDER_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TWO_FEATURE_LADDER_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/LARGE_BOUND_FEATURE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/LOW_ENERGY_SOURCE_BOUND.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_fixed_ladder_control.py']
r=subprocess.run([sys.executable,str(P/'neutral_fixed_ladder_control.py')],check=True,capture_output=True,text=True,timeout=60)
out=dict(status='bounded-support',algebra_controls=json.loads(r.stdout),scope='Every fixed finite occupation under inherited native normal-form bounds; numerical controls check algebra, not the microscopic many-body spectrum or observations')
f=ROOT/'outputs/native_fixed_occupation_ladder/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
