from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_DILUTE_FIELD_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_cluster_fock_control.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_dilute_field_scaling.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/CHARACTER_INDEPENDENT_COLLISION_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/REFLECTION_GROUND_SECTOR_PROOF.md']
results=[]
for f in AUDIT_INPUT_PATHS[1:3]:
 r=subprocess.run([sys.executable,str(ROOT/f)],check=True,capture_output=True,text=True,timeout=110);results.append(json.loads(r.stdout))
for row in results[0]['rows']:
 assert abs(row['rows'][0]['full_lowering_error']*row['R']**2-99)<1e-8
out=dict(status='conditional-support',scope='Native finite-mode fixed-occupation bosonic limit; no relativistic or finite-density field claim',motif_control=results[0],derived_matrix_control=results[1])
p=ROOT/'outputs/native_dilute_field/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
