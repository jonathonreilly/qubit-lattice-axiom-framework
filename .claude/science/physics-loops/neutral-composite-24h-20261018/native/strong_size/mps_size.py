from pathlib import Path
import sys,pickle,time,json
import numpy as np
from scipy.linalg import eigh
import quimb.tensor as qtn
P=Path(__file__).resolve().parents[1];sys.path.insert(0,str(P))
from native_rung import mpo,xs,zs

def expectation(a,H,b):return float(np.real(qtn.expec_TN_1D(a.H,H,b)))
def run():
 rows=[]
 for L in [8,12,16]:
  start=time.monotonic();path=P/f'stationary_tube_mps_refined_{L}.pkl'
  with path.open('rb') as f:g=pickle.load(f)
  g.normalize();H=mpo(L);e=expectation(g,H,g);Hg=H.apply(g,compress=False);r=Hg-e*g;gres=np.sqrt(max(0,float(np.real(r.H@r))));del Hg,r
  lengths=list(range(2,L-1,2));states=[];mus=[]
  U=xs[0]@xs[1]
  for ell in lengths:
   a=(L-ell)//2;v=g.copy()
   for j in range(a,a+ell):v.gate_(U,j,contract=True)
   states.append(v);mus.append(float(np.real(g.H@v)))
  n=len(states);G=np.zeros((n,n));K=np.zeros((n,n));h0=[expectation(v,H,g) for v in states];raw=[]
  for i in range(n):
   for j in range(i,n):
    gg=float(np.real(states[i].H@states[j]));hh=expectation(states[i],H,states[j])
    G[i,j]=G[j,i]=gg-mus[i]*mus[j]
    K[i,j]=K[j,i]=hh-mus[j]*h0[i]-mus[i]*h0[j]+mus[i]*mus[j]*e-e*G[i,j]
    if i==j:raw.append(hh-e)
  ev,V=eigh(G);keep=ev>1e-10*max(ev);W=V[:,keep]/np.sqrt(ev[keep]);energies,c=eigh(W.T@K@W);coef=W@c
  # Exact product-state matrix elements, but MPS reference remains variational.
  overlap=G@coef;overlap2=overlap**2/np.diag(G)[:,None]
  row=dict(L=L,physical_qubits=4*L,ground_energy=e,ground_residual=gres,bond=g.max_bond(),lengths=lengths,raw_string_energy=raw,source_means=mus,gram=G.tolist(),projected_H=K.tolist(),ritz_energies=energies.tolist(),probe_overlap_squared=overlap2.tolist(),ritz_coefficients=coef.tolist(),seconds=time.monotonic()-start)
  rows.append(row);(P/'strong_size/mps_size.json').write_text(json.dumps(dict(scope='Full native isotropic H in exact positive rung parity representation. Reference MPS variational; no global ground or Ritz stationarity claim. Thin geometry and fixed string family.',rows=rows),indent=2)+'\n');print(dict(L=L,ground_residual=gres,diagonal=raw,ritz=energies[:3].tolist(),seconds=row['seconds']),flush=True)
if __name__=='__main__':run()
