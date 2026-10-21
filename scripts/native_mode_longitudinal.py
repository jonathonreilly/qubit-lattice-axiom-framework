"""Native 3 by 2 by L boxes, open x/y and periodic z; longitudinal control only."""
from pathlib import Path
import json,time
import numpy as np
from scipy.sparse.linalg import eigsh,LinearOperator
from native_mode_compass_sector_basis import basis
from native_mode_compass_sector_solve import apply
AUDIT_TIMEOUT_SEC = 1800
P=Path(__file__).resolve().parent
OUT=P.parent/'outputs/native_mode_correlations_20261019'
OUT.mkdir(parents=True,exist_ok=True)

def solve(L):
 start=time.monotonic();d=basis((3,2,L));idx={p:i for i,p in enumerate(d['sites'])};ts=list(d['terms'])
 for p,i in idx.items():
  if p[2]==L-1:
   q=(p[0],p[1],0);ts.append(d['reduce_term'](0,(1<<i)|(1<<idx[q]),-1))
 terms=np.array(ts,dtype=np.int64);H=lambda v:apply(v,*terms.T.copy());dim=d['dimension']
 op=LinearOperator((dim,dim),matvec=H,dtype=float)
 E,V=eigsh(op,k=12,ncv=40,which='SA',tol=1e-10,maxiter=1500,v0=np.random.default_rng(19000+L).normal(size=dim));g=V[:,0]
 residuals=[float(np.linalg.norm(H(V[:,j])-E[j]*V[:,j])) for j in range(len(E))]
 assert max(residuals)<1e-7
 probes=[]
 for k in [1,2]:
  mask=sum(1<<i for i,(x,y,z) in enumerate(d['sites']) if x<k and z<2)
  t=np.array([d['reduce_term'](mask,0,1)],dtype=np.int64);u=apply(g,*t.T.copy());gs=V[:,E-E[0]<1e-8];u-=gs@(gs.T@u);probes.append(u/np.linalg.norm(u))
 weights=(np.array(probes)@V)**2;vis=np.flatnonzero((weights.max(axis=0)>1e-8)&(E-E[0]>1e-8));assert len(vis)
 k=vis[0];group=np.flatnonzero(abs(E-E[k])<1e-8)
 # Average same-column ZZ covariance over longitudinal anchors, making no COM-radius identification.
 profiles={}
 for name,cols in [('ground',[0]),('returned_mode_mixture',group)]:
  means=np.zeros(L);products=np.zeros((L,L))
  for col in cols:
   v=V[:,col];states=[]
   for z in range(L):
    mask=(1<<idx[(1,0,z)])|(1<<idx[(1,0,(z+1)%L)])
    t=np.array([d['reduce_term'](0,mask,1)],dtype=np.int64);states.append(apply(v,*t.T.copy()))
   states=np.array(states);means+=states@v/len(cols);products+=states@states.T/len(cols)
  cov=products-np.outer(means,means)
  assert np.max(abs(np.diag(cov)-(1-means**2)))<1e-9
  profiles[name]=[float(np.mean([cov[z,(z+r)%L] for z in range(L)])) for r in range(L)]
 return dict(shape=[3,2,L],physical_qubits=6*L,dimension=dim,boundaries=['open','open','periodic'],ground_energy=float(E[0]),gaps=(E-E[0]).tolist(),residuals=residuals,weights=weights.tolist(),first_visible_gap=float(E[k]-E[0]),returned_group=group.tolist(),captured_weights=weights[:,group].sum(axis=1).tolist(),longitudinal_covariances=profiles,seconds=time.monotonic()-start)

def main():
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument("--lengths",type=int,nargs="+",default=[3,4]);args=parser.parse_args()
 assert all(L>=3 for L in args.lengths)
 rows=[]
 for L in args.lengths:
  row=solve(L);rows.append(row);print(json.dumps(row),flush=True)
  (OUT/'longitudinal.json').write_text(json.dumps({'scope':'Fixed transverse cross-section; distinct lowest visible levels need not be the same mode. No 3D thermodynamic or finite internal-size result.', 'rows':rows},indent=2)+'\n')
if __name__=='__main__':main()
