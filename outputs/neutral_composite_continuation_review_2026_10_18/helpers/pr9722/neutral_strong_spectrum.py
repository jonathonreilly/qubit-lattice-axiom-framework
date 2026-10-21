from pathlib import Path
import sys,json,numpy as np
from scipy.sparse import csr_matrix,identity,kron,diags
from scipy.sparse.linalg import eigsh
P=Path(__file__).resolve().parent
from neutral_rung_model import h,Ds
rows=[]
for L in [2,3,4,5]:
 N=8**L;ids=np.arange(N);digits=[(ids//8**(L-1-i))%8 for i in range(L)];diag=np.zeros(N)
 for i in range(L-1):
  for d in Ds:diag-=np.diag(d)[digits[i]]*np.diag(d)[digits[i+1]]
 odiag=np.zeros(N)
 for i in range(L-2):
  for d in Ds:odiag+=np.diag(d)[digits[i]]*np.diag(d)[digits[i+2]]
 V=csr_matrix((N,N))
 for i in range(L):V+=kron(kron(identity(8**i),csr_matrix(h)),identity(8**(L-1-i)),format='csr')
 for ratio in [.5,.35,.2]:
  H=diags(diag)+ratio*V
  if L<=3:
   e,u=np.linalg.eigh(H.toarray());e=e[:12];u=u[:,:12]
  else:
   e,u=eigsh(H,k=16,which='SA',tol=1e-12,ncv=48,v0=np.random.default_rng(1818+L).normal(size=N));order=np.argsort(e);e=e[order];u=u[:,order]
  scale=ratio**L/2**(L-1);levels=(e[:8]-np.mean(e[:8]))/scale
  target=np.array([-4]+[0]*6+[4]) if L%2==0 else np.array([-2*np.sqrt(2)]*2+[0]*4+[2*np.sqrt(2)]*2)
  row=dict(L=L,ratio=ratio,scale=scale,scaled_centered_levels=levels.tolist(),target=target.tolist(),max_error=float(max(abs(levels-target))),max_residual=float(max(np.linalg.norm(H@u[:,i]-e[i]*u[:,i]) for i in range(12))))
  ob=u[:,:8].T@(odiag[:,None]*u[:,:8]);inelastic=abs(e[:8,None]-e[None,:8])>1e-8
  row['band_inelastic_O_frobenius2']=float(np.sum(abs(ob[inelastic])**2));row['source0_to_band_weight']=float(np.sum(abs(ob[1:,0])**2));row['original_O_band_mean']=float(np.trace(ob)/8)
  rows.append(row);(P/'neutral_strong_spectrum.json').write_text(json.dumps(rows,indent=2));print(row,flush=True)
