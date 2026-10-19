from pathlib import Path
import sys,json,time,pickle,signal
import numpy as np
import quimb as qu,quimb.tensor as qtn
from scipy.linalg import eigh
P=Path(__file__).resolve().parents[1];sys.path.insert(0,str(P))
from native_rung import mpo,Ds,xs
I=np.eye(8)
def pm(L):
 H=mpo(L)
 for d in Ds:H=H+qtn.MPO_product_operator([-d]+[I]*(L-2)+[d])
 H.compress(cutoff=1e-14)
 return H

def ex(a,H,b):return float(np.real(qtn.expec_TN_1D(a.H,H,b)))
def main():
 rows=[]
 for L in [8,12,16,24]:
  start=time.monotonic();H=pm(L);qu.seed_rand(981900+L)
  initial=qtn.MPS_rand_state(L,bond_dim=4,phys_dim=8,dtype=float)
  dm=qtn.DMRG2(H,bond_dims=[16,32,64,96],cutoffs=1e-12,p0=initial);dm.opts.update(local_eig_tol=1e-9,local_eig_ncv=30,local_eig_maxiter=500)
  stages=[]
  for chi in [32,64,96]:
   flag=dm.solve(tol=1e-9,bond_dims=chi,max_sweeps=4,verbosity=0)
   g=dm.state;g.normalize();e=ex(g,H,g);r=H.apply(g,compress=False)-e*g;delta=np.sqrt(max(0,float(np.real(r.H@r))));del r
   stages.append(dict(bond=chi,energy=e,residual=delta,energy_flag=bool(flag),seconds=time.monotonic()-start));print(dict(L=L,stage=stages[-1]),flush=True)
  # Centered strings: fixed diagnostic family, not optimized arbitrary excitations.
  U=xs[0]@xs[1];ls=list(range(2,L//2+1,2));vs=[];mus=[]
  for ell in ls:
   v=g.copy();a=(L-ell)//2
   for z in range(a,a+ell):v.gate_(U,z,contract=True)
   vs.append(v);mus.append(float(np.real(g.H@v)))
  n=len(ls);G=np.zeros((n,n));K=np.zeros((n,n));raw=[];h0=[ex(v,H,g) for v in vs]
  for i in range(n):
   for j in range(i,n):
    gg=float(np.real(vs[i].H@vs[j]));hh=ex(vs[i],H,vs[j]);G[i,j]=G[j,i]=gg-mus[i]*mus[j]
    K[i,j]=K[j,i]=hh-mus[j]*h0[i]-mus[i]*h0[j]+mus[i]*mus[j]*e-e*G[i,j]
    if i==j:raw.append(hh-e)
  ev,V=eigh(G);keep=ev>1e-10*max(ev);W=V[:,keep]/np.sqrt(ev[keep]);en,c=eigh(W.T@K@W);coef=W@c
  row=dict(L=L,physical_qubits=4*L,stages=stages,lengths=ls,raw_energy=raw,gram=G.tolist(),projected_H=K.tolist(),ritz_energies=en.tolist(),probe_overlap_squared=((G@coef)**2/np.diag(G)[:,None]).tolist(),seconds=time.monotonic()-start)
  rows.append(row);(P/'strong_size/periodic_mps.json').write_text(json.dumps(dict(scope='Native H with periodic longitudinal boundary, positive rung parity, variational MPS; no global-ground or stable-feature certification',rows=rows),indent=2)+'\n')
  with (P/f'strong_size/periodic_state_{L}.pkl').open('wb') as f:pickle.dump(g,f)
  print(dict(L=L,raw=raw,ritz=en.tolist(),seconds=row['seconds']),flush=True)
if __name__=='__main__':main()
