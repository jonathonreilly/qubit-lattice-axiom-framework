from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/MICROSCOPIC_GROUND_WINDOW_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_flux_connected_row.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_polynomial_dispersion.py']
a={}
for name in ['neutral_flux_connected_row.py','neutral_polynomial_dispersion.py']:
 q=subprocess.run([sys.executable,str(P/name)],check=True,capture_output=True,text=True,timeout=90);a[name]=json.loads(q.stdout)
assert all(r['nonzero']==33 and r['row_l1']=='35/2' and r['far_transition']=='0' for r in a['neutral_flux_connected_row.py']['rows'])
assert max(r['relative_error'] for r in a['neutral_polynomial_dispersion.py']['rows'][-3:])<2e-6
out=dict(status='conditional-support',controls=a,scope='Analytic selected-fibre microscopic transfer; numerical controls of connected coefficients, not full-grid diagonalization')
f=ROOT/'outputs/native_polynomial_grid_pole/result.json';f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
