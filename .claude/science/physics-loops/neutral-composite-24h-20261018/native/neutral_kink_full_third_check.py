from pathlib import Path
import numpy as np,json
from scipy.sparse import kron,identity,diags,csr_matrix
from neutral_kink_core import band,h,Ds,bits
L=3;K1,K2,K3,states,source=band(L,third=True);K2=K2-L/2*identity(len(states)) # undo ground common shift for absolute band energy
N=8**L;ids=np.arange(N);digits=[ids//8**j%8 for j in range(L)]
z=np.zeros(N);V=csr_matrix((N,N))
for j in range(L):
 for d in Ds:z-=np.diag(d)[digits[j]]*np.diag(d)[digits[(j+1)%L]]
 V+=kron(kron(identity(8**(L-1-j)),csr_matrix(h)),identity(8**j),format='csr')
P=np.eye(N)[:,states];Eref=-4*L+8
assert np.max(abs(P.T@(V@P)-K1.toarray()))<1e-12
q=[i for i in range(N) if i not in set(states)];B=P.T@V.toarray()[:,q]
assert np.max(abs(B@np.diag(1/(Eref-z[q]))@B.T-K2.toarray()))<1e-12
rows=[]
for ratio in [.04,.02,.01]:
 H=np.diag(z)+ratio*V.toarray();e,u=np.linalg.eigh(H);select=np.where(abs(e-Eref)<1)[0];assert len(select)==len(states)
 U=u[:,select];M=P.T@U;left,sv,right=np.linalg.svd(M);W=left@right
 exact=W@np.diag(e[select])@W.T
 approx=Eref*np.eye(len(states))+ratio*K1.toarray()+ratio**2*K2.toarray()+ratio**3*K3.toarray()
 err=float(np.linalg.norm(exact-approx,2));rows.append(dict(ratio=ratio,operator_error=err,error_over_ratio4=err/ratio**4,min_overlap_singular=float(min(sv))))
print(rows);open(Path(__file__).resolve().parent/'neutral_kink_full_third_check.json','w').write(json.dumps(rows,indent=2))
