from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/ALL_HEIGHT_ASSISTED_HOP_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/LIGHT_COLUMN_WINDOW_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_ASSISTED_HOP_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_complementary_all_length.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_third_height_symbolic.py']
controls={}
for name in ['neutral_complementary_all_length.py','neutral_third_height_symbolic.py']:
 args=['6','6'] if name=='neutral_third_height_symbolic.py' else []
 q=subprocess.run([sys.executable,str(P/name),*args],check=True,capture_output=True,text=True,timeout=90)
 controls[name]=json.loads(q.stdout)
for row in controls['neutral_complementary_all_length.py']:
 assert row['scaled']=='1'
result=dict(status='conditional-support',controls=controls,scope='Fixed-height canonical prepared background vertex; no empirical scalar or hierarchy selection')
f=ROOT/'outputs/native_all_height_assisted_hop/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
