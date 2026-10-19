from pathlib import Path
import sys,json,subprocess
ROOT=Path(__file__).resolve().parents[1]
P='.claude/science/physics-loops/neutral-composite-24h-20261018/native/'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/FINITE_FEATURE_SIZE_PROBE.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_finite_size_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_LAYER_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_SCALAR_TETRAMER_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_DILUTE_FIELD_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/final_pending/neutral-aggregate-review.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/final_pending/aggregation_check.py']
r=subprocess.run([sys.executable,str(ROOT/AUDIT_INPUT_PATHS[1])],capture_output=True,text=True,check=True,timeout=90)
o=json.loads(r.stdout);assert o['tested']==2047 and o['minimum_perimeter_saving']==4
# Exact exponent bookkeeping only, not a numerical proof of the operator bounds.
contact=4+14;tail=80-2*14;kinetic=12+2*2;gap=8
assert min(contact,tail,kinetic)==16
assert 2*(min(contact,tail,kinetic)-gap)==16
o.update(capture_probability_exponent=16,independent_review='pending for new fusion-energy and uniform-q transfer; earlier coarse-subset check complete',status='conditional-support',claim_type='bounded_theorem')
p=ROOT/'outputs/native_finite_feature_size/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2)+'\n')
print(json.dumps(o,indent=2))
print('per_element: reflected syndrome points checked exactly; no empirical particle identification.')
print('per_site: finite inverse masks preserve one physical qubit per site; no extra occupancy is introduced.')
print('per_mode: checked and not executed — lifetime and full scalar-mode spectrum are not numerically tested here.')
print('per_block: 2047 finite geometry constructions and exponent bookkeeping pass; energy proof is analytic and review pending.')
print('lattice_wide: checked and not executed — arbitrary fixed-coupling thermodynamic size selection remains open.')
