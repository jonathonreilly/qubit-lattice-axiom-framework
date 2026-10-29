"""Independent Cholesky diagnosis of preserved NumPy slogdet warnings."""
import numpy as np,json,warnings,sys
from pathlib import Path
from datetime import datetime,timezone
K=[.31,.52,-.27,.41];Delta=np.zeros((81,81),complex)
for mu in range(4):
 D=-np.eye(3,dtype=complex);D[0,1]=D[1,2]=1;D[2,0]=np.exp(1j*K[mu]);G=D.conj().T@D
 term=np.ones((1,1),complex)
 for nu in range(4):term=np.kron(term,G if mu==nu else np.eye(3))
 Delta+=term
realDelta=np.block([[Delta.real,-Delta.imag],[Delta.imag,Delta.real]])
A=np.linalg.cholesky(Delta);B=np.linalg.cholesky(realDelta)
ld=float(2*np.log(A.diagonal().real).sum());ldr=float(2*np.log(B.diagonal()).sum())
prior=json.loads(Path(__file__).with_name('review_residual_bridge_01_out.json').read_text())['details']['charged_pair_logdets']
with warnings.catch_warnings(record=True) as seen:
 warnings.simplefilter('always');z=np.linalg.slogdet(Delta);rz=np.linalg.slogdet(realDelta)
 captured=[str(w.message) for w in seen]
checks={'complex_positive':np.linalg.eigvalsh(Delta)[0]>0,'real_pair_positive':np.linalg.eigvalsh(realDelta)[0]>0,'complex_Cholesky_matches_preserved_run':abs(ld-prior['one_complex_root'])<1e-10,'real_Cholesky_matches_preserved_run':abs(ldr-prior['real_pair'])<1e-10,'Cholesky_pair_factor_two':abs(ldr-2*ld)<1e-10,'isolated_slogdet_matches_Cholesky':abs(z[1]-ld)<1e-10 and abs(rz[1]-ldr)<1e-10}
checks={k:bool(v) for k,v in checks.items()}
print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'passed':sum(checks.values()),'total':len(checks),'complex_logdet':ld,'real_pair_logdet':ldr,'isolated_slogdet_warnings':captured,'diagnosis':'The saved determinant values are independently confirmed on positive definite matrices by Cholesky. Original NumPy warnings remain in the first-run stderr; the backend warning cause is not claimed resolved.'},indent=2,sort_keys=True))
sys.exit(0 if all(checks.values()) else 1)
