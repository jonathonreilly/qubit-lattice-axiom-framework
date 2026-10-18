from pathlib import Path
import json, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/PRIMITIVE_LOOP_INTERACTION_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_loop_interaction_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_loop_feshbach_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/COLUMN_READOUT_PROOF.md']
controls=[]
for source in AUDIT_INPUT_PATHS[1:3]:
 r=subprocess.run([sys.executable,str(ROOT/source)],check=True,capture_output=True,text=True,timeout=110)
 controls.append(json.loads(r.stdout))
a,b=controls
for row in b:
 assert row['connected']==a['linked'][row['dz']]['coefficient']
assert a['diagonal_interaction']=='545/5308416'
assert a['axis_interaction']=='-9/32768'
out=dict(status='bounded-support',scope='Exact local primitive and connected interaction coefficients; no observation or isolated-band test',subset=a,independent_feshbach=b)
p=ROOT/'outputs/native_loop_interaction_law/result.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
