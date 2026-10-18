import numpy as np,json
from scipy.linalg import eigh
rows=[]
for lam in [.2,.1,.05]:
 for N in [32,128,256]:
  eps=lam/4;f=lam**3/16;x=-6*lam;T=np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1);v=f*(np.arange(N)+2)-2*lam;A=np.diag((np.sqrt(1+eps*(v-x))-1)/eps);D=2*np.eye(N)+eps*A;C=D+eps*T;L=T-A;cs,U=eigh(C);sq=(U*np.sqrt(cs))@U.T
  H0=-2*T-eps*T@T+np.diag(v);R=H0-x*np.eye(N)+sq@L@sq
  comm=lambda a,b:a@b-b@a
  identity=np.linalg.norm(H0-x*np.eye(N)+(C@L+L@C)/2,2)
  functional=np.linalg.norm(R+.5*comm(sq,comm(sq,L)),2)
  B=comm(C,comm(C,L));bound=np.linalg.norm(B,2)/(8*cs[0]);actual=np.linalg.norm(R,2)
  assert identity<1e-11 and functional<1e-11 and actual<bound+1e-11
  rows.append(dict(lam=lam,N=N,identity_error=float(identity),doublecomm_error=float(functional),remainder_norm=float(actual),functional_bound=float(bound),scaled_remainder=float(actual/(eps**2*f))))
print(json.dumps(rows,indent=2));open('/private/tmp/neutral_corrected_strip_algebra.json','w').write(json.dumps(rows,indent=2)+'\n')
