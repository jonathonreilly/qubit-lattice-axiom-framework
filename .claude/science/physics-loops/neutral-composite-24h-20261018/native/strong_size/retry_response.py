from pathlib import Path
import pickle,json
import numpy as np
import quimb.tensor as qtn
from scipy.linalg import eigh
from periodic_mps import pm,ex
from native_rung import xs
P=Path(__file__).resolve().parent

def main():
 rows=[]
 for L in [16,24]:
  path=P/f'periodic_retry_state_{L}.pkl'
  if not path.exists():continue
  g=pickle.loads(path.read_bytes());g.normalize();H=pm(L);e=ex(g,H,g);ls=list(range(2,L//2+1,2));vs=[];mu=[]
  for ell in ls:
   v=g.copy();a=(L-ell)//2
   for z in range(a,a+ell):v.gate_(xs[0]@xs[1],z,contract=True)
   vs.append(v);mu.append(float(np.real(g.H@v)))
  n=len(ls);G=np.zeros((n,n));K=G.copy();raw=[];h0=[ex(v,H,g) for v in vs]
  for i in range(n):
   for j in range(i,n):
    gg=float(np.real(vs[i].H@vs[j]));hh=ex(vs[i],H,vs[j]);G[i,j]=G[j,i]=gg-mu[i]*mu[j]
    K[i,j]=K[j,i]=hh-mu[j]*h0[i]-mu[i]*h0[j]+mu[i]*mu[j]*e-e*G[i,j]
    if i==j:raw.append(hh-e)
  ev,V=eigh(G);keep=ev>1e-10*max(ev);W=V[:,keep]/np.sqrt(ev[keep]);en,c=eigh(W.T@K@W)
  rows.append(dict(L=L,lengths=ls,reference_energy=e,raw=raw,ritz_energies=en.tolist(),scope='Improved-reference variational response only; no Ritz residual or stable size'))
  print(rows[-1],flush=True)
 (P/'retry_response.json').write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':
 qtn.set_contract_strategy('greedy');main()
