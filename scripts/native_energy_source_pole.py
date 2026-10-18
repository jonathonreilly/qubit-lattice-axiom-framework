from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_ENERGY_SOURCE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_energy_source_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/COLUMN_READOUT_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/REFLECTION_GROUND_SECTOR_PROOF.md']
r=subprocess.run([sys.executable,str(ROOT/AUDIT_INPUT_PATHS[1])],check=True,capture_output=True,text=True,timeout=90);c=json.loads(r.stdout)
assert len(c['square'])==16
assert all(x['vertex_ratios']==['-3/4']*4 and x['edge_ratios']==['1']*4 for x in c['square'])
assert next(x for x in c['winding'] if x['L']==10)['x_pair_qx2']=='-3/2'
out=dict(status='conditional-support',scope='Native energy-density marked-path coefficients; actual-H pole/source transfer analytic, not observations',control=c)
p=ROOT/'outputs/native_energy_source_pole/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
