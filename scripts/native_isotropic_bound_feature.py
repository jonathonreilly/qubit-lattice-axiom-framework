from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/EIGHT_FLUX_BOUND_CLUSTER_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_q8_orientation.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_q8_isotropic_control.py']
a={}
for name in ['neutral_q8_orientation.py','neutral_q8_isotropic_control.py']:
 r=subprocess.run([sys.executable,str(P/name)],capture_output=True,text=True,check=True,timeout=90);a[name]=json.loads(r.stdout)
assert a['neutral_q8_orientation.py']['total']=='607201/144000'
assert len(a['neutral_q8_orientation.py']['kernel'])==9
assert max(abs(x['relative_error']) for x in a['neutral_q8_isotropic_control.py']['rows'][-3:])<1e-12
p=5;M=60;powers=dict(energy=14+2*p,anisotropy=6+4*p,tail=M-2*p,source_error=M-22-3*p)
assert powers['anisotropy']>powers['energy'] and powers['tail']>powers['energy'] and powers['source_error']>18
out=dict(status='conditional-support',scope='Exact local orientation coefficient and derived matrix control; actual selected-sector polynomial-grid theorem analytic; no empirical test',powers=powers,controls=a)
f=ROOT/'outputs/native_isotropic_bound_feature/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
