from pathlib import Path
import subprocess,sys,json,os
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_PAIR_SCATTERING_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_order10_pair_control.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_pair_scattering_control.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/SECONDARY_NEUTRAL_MOLECULE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/PRIMITIVE_LOOP_INTERACTION_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/CHARGED_COLUMN_POLE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_pair_collision_packet.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_pair_collision_packet.json']
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1');controls=[]
for path in AUDIT_INPUT_PATHS[1:3]:
 r=subprocess.run([sys.executable,str(ROOT/path)],check=True,capture_output=True,text=True,timeout=45,env=env);controls.append(json.loads(r.stdout))
assert controls[0]['pair_contrast']=='333355/24461180928'
assert controls[1]['core_size']==37 and controls[1]['potential_sites']==20
out=dict(status='conditional-support',scope='Derived leading native pair collision operator and its threshold T; not a fixed-lambda microscopic S-matrix or empirical fit',controls=controls)
p=ROOT/'outputs/native_pair_scattering/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
