import numpy as np,json,hashlib,sys
from scipy.linalg import expm,logm
from pathlib import Path
rng=np.random.default_rng(86400);checks=[]
def check(n,c,**e):checks.append(dict(name=n,passed=bool(c),**e))
for N in (2,3,5,10):
 r=.9*np.pi/np.sqrt(N);err=0;trace=0
 for j in range(12):
  Z=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N));A=Z-Z.conj().T;A-=np.trace(A)/N*np.eye(N);A*=r*(j+1)/13/np.linalg.norm(A)
  U=expm(A);B=logm(U);err=max(err,np.linalg.norm(B-A));trace=max(trace,abs(np.trace(B)))
 check('principal_inverse_on_traceless_ball_SU'+str(N),err<2e-11 and trace<2e-11,max_inverse_error=float(err),max_trace_error=float(trace),radius=float(r))
 center=np.exp(2j*np.pi/N)*np.eye(N);cnorm=np.linalg.norm(logm(center))
 check('center_branch_excluded_SU'+str(N),cnorm>r,center_principal_norm=float(cnorm))
 # Pure traceless exponential aliases map back to I but must fail the coordinate cut.
 alias=np.diag([2j*np.pi,-2j*np.pi]+[0j]*(N-2))
 check('coordinate_alias_excluded_SU'+str(N),np.linalg.norm(expm(alias)-np.eye(N))<2e-11 and np.linalg.norm(alias)>r)
p=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof/SOFT_FLUCTUATION_COVARIANCE_ASTRA.md')
h=hashlib.sha256(p.read_bytes()).hexdigest()
out={'source_sha256':h,'expected_source_sha256':'327d033b22281f5f727c018ccb9b1d23d8f7d131bd3633602d6655a9b3de2403','source_matches':h=='327d033b22281f5f727c018ccb9b1d23d8f7d131bd3633602d6655a9b3de2403','checks':checks,'passed':sum(x['passed'] for x in checks),'total':len(checks),'analytic_argument':'For ||A||HS<r<pi/sqrt(N), every anti-Hermitian eigenangle lies in (-pi,pi), so principal Log(exp A)=A. Conversely det W=1 and ||Log W||HS<r imply tr Log W in 2pi i Z and |tr Log W|<pi, hence traceless. The two domains coincide exactly. Gaussian cutoff prevents repeated preimages. F21 retains the changed complement.','scope':'Affected chart repair only; no precision/code/normalization formula changes or full science rerun.'}
print(json.dumps(out,indent=2));sys.exit(0 if out['passed']==out['total'] and out['source_matches'] else 1)
