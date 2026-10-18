from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_FLUX_DIAGONAL_MODE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_sixflux_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/EIGHT_FLUX_BOUND_CLUSTER_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/REFLECTION_GROUND_SECTOR_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/CHARGED_COLUMN_POLE_PROOF.md']
r=subprocess.run([sys.executable,str(ROOT/AUDIT_INPUT_PATHS[1])],check=True,capture_output=True,text=True,timeout=90);c=json.loads(r.stdout)
assert c['minimum_counts']=={'2':32,'3':64}
assert c['K_float']>0 and len(c['paths'])==9
assert all(s['norm']=='1' and s['weight_coefficient']=='-5/2' for s in c['source'])
out=dict(status='conditional-support',scope='Exact finite-pattern paths and physical symmetry/source controls; actual-H transfer analytic, no empirical tests',control=c)
p=ROOT/'outputs/native_sixflux_diagonal_mode/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
