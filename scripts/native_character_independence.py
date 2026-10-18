from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/CHARACTER_INDEPENDENT_COLLISION_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_flat_character_control.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_PAIR_SCATTERING_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/SECONDARY_NEUTRAL_MOLECULE_PROOF.md']
r=subprocess.run([sys.executable,str(ROOT/AUDIT_INPUT_PATHS[1])],check=True,capture_output=True,text=True,timeout=60);c=json.loads(r.stdout)
assert c['direct_orbit_checks']==3072
assert all(x['minimum_flat_flip']==x['R'] for x in c['rows'])
out=dict(status='conditional-support',scope='Invariant matched neutral collision does not require chosen X/Y character; low-energy preparation and positive Z planes remain',control=c)
p=ROOT/'outputs/native_character_independence/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
