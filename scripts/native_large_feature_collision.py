from pathlib import Path
import sys,subprocess,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=[
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/LARGE_BOUND_FEATURE_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TWO_FEATURE_LADDER_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/LARGE_FEATURE_COLLISION_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/FOURBODY_ANCHOR_KERNEL.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_threshold_interval.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_large_collision_interval.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_large_collision_quadrature.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_general_contact_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_fourbody_physical_control.py']
checks={}
for name in ['neutral_large_collision_interval.py','neutral_general_contact_control.py','neutral_fourbody_physical_control.py','neutral_large_collision_quadrature.py']:
 r=subprocess.run([sys.executable,str(P/name)],check=True,capture_output=True,text=True,timeout=90);checks[name]=r.stdout.strip()
out=dict(status='bounded-support',checks=checks,scope='Native coefficient contact/Born numerator for large neutral features; no exact four-body S, lifetime, actual-H linewidth or observation test')
f=ROOT/'outputs/native_large_feature_collision/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
