from pathlib import Path
import sys,json,numpy as np
from scipy.sparse.linalg import eigsh
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native';sys.path.insert(0,str(P))
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/LARGE_BOUND_FEATURE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_threshold_interval.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_threshold_highprecision.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_transverse_bound_model.py']
from neutral_threshold_interval import run_certificate
from neutral_threshold_highprecision import run_roots
from neutral_transverse_bound_model import matrix
certificate=run_certificate();rows=run_roots();controls=[]
expected=-4.4-float(rows[0]['gap'])
for L in [50,100]:
 H,s,idx=matrix(L,b=.1);e=eigsh(H,k=1,which='SA',tol=1e-12,return_eigenvectors=False)[0]
 controls.append(dict(L=L,energy=float(e),error=float(e-expected)))
assert abs(controls[-1]['error'])<1e-8
assert abs(controls[-1]['error'])<abs(controls[0]['error'])
assert all(float(rows[i]['gap'])>float(rows[i+1]['gap']) for i in range(len(rows)-1))
assert all(float(rows[i]['scaled_log'])<float(rows[i+1]['scaled_log'])<.954 for i in range(len(rows)-1))
out=dict(status='bounded-support',threshold_certificate=certificate,coefficient_binding_roots=rows,finite_graph_control=controls,scope='Selected native K1 momentum family and original-source coefficient; no full-H scalar or empirical test')
p=ROOT/'outputs/native_large_bound_feature/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
