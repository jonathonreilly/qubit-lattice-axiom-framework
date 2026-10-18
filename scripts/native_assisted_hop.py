from pathlib import Path
import subprocess,sys,json,math
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_PROBE_LOOP_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_ASSISTED_HOP_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_DRESSED_PATCH_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/BULK_SLAB_RESPONSE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_third_order_symbolic.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_complementary_hop.py']
def run(name,*args):
 r=subprocess.run([sys.executable,str(P/name),*map(str,args)],check=True,capture_output=True,text=True,timeout=90)
 return json.loads(r.stdout)
m=8/(math.sqrt(80**2+4*4**2)+80)
assert m>0 and m*m/16>0
result=dict(status='bounded-support',symbolic_R6=run('neutral_third_order_symbolic.py',6),symbolic_R7=run('neutral_third_order_symbolic.py',7),complementary=run('neutral_complementary_hop.py'),variance_lower=m*m,vertex_weight_coefficient_lower=m*m/16,scope='Canonical native nearest-hop vertex; matched dressed prepared channel, not relaxed emission rate')
f=ROOT/'outputs/native_assisted_hop/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
