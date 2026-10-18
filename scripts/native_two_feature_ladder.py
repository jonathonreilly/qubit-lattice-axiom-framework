from pathlib import Path
import sys, json, subprocess
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TWO_FEATURE_LADDER_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TWO_FEATURE_SPIN_ALGEBRA.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/LOW_ENERGY_SOURCE_BOUND.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_pair_algebra_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_pair_mixed_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_two_feature_contact_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_source_contact_control.py',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/MICROSCOPIC_LARGE_FEATURE_WINDOW_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/MICROSCOPIC_GROUND_WINDOW_PROOF.md',
 '.claude/science/physics-loops/neutral-composite-24h-20261018/native/LARGE_BOUND_FEATURE_PROOF.md']
checks={}
for name in ['neutral_pair_algebra_control.py','neutral_pair_mixed_control.py','neutral_two_feature_contact_control.py','neutral_source_contact_control.py']:
 result=subprocess.run([sys.executable,str(P/name)],check=True,capture_output=True,text=True,timeout=60)
 checks[name]=result.stdout.strip()
out=dict(status='bounded-support',checks=checks,scope='Exact local algebra/contact controls for analytic two-feature window-vector theorem; no full-H ED, isolated particles, finite-density theory or empirical tests')
p=ROOT/'outputs/native_two_feature_ladder/result.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
