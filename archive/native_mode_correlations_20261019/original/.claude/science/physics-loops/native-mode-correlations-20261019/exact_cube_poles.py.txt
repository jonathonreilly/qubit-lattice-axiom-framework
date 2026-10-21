"""Exact selected-sector 27-qubit periodic native cube: small-volume control only."""
from pathlib import Path
import sys,json,time
import numpy as np
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh,LinearOperator
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P))
from compass_sector_basis import basis
from compass_sector_solve import apply

AUDIT_TIMEOUT_SEC = 1800

OUT=P.parents[3]/'outputs/native_mode_correlations_20261019'
OUT.mkdir(parents=True,exist_ok=True)

def main():
 start=time.monotonic();shape=(3,3,3);d=basis(shape);idx={p:i for i,p in enumerate(d['sites'])};ts=list(d['terms'])
 for a in range(3):
  for p,i in idx.items():
   if p[a]==2:
    q=list(p);q[a]=0;mask=(1<<i)|(1<<idx[tuple(q)])
    ts.append(d['reduce_term'](mask if a!=2 else 0,mask if a!=0 else 0,1 if a==1 else -1))
 ts=np.array(ts,np.int64);dim=d['dimension'];H=lambda v:apply(v,*ts.T.copy());op=LinearOperator((dim,dim),matvec=H,dtype=float)
 E,V=eigsh(op,k=16,which='SA',tol=1e-11,ncv=48,maxiter=1200,v0=np.random.default_rng(271910).normal(size=dim));g=V[:,0];e=float(E[0]);gsub=V[:,E-E[0]<1e-8]
 out=dict(shape=shape,physical_qubits=27,periodic_axes=[0,1,2],dimension=dim,ground_energy=e,lowest_energies=E.tolist(),ground_residual=float(np.linalg.norm(H(g)-e*g)),scope='Exact selected CSS sector, 3-site periodic cube; no large-volume or stable-size conclusion',levels=[])
 (OUT/'exact_cube_poles.json').write_text(json.dumps(out,indent=2)+'\n');print('ground',out,flush=True)
 S=[];raw=[]
 for k in [1,2]:
  mask=sum(1<<i for i,(x,y,z) in enumerate(d['sites']) if x<k and y<2 and z<2);t=np.array([d['reduce_term'](mask,0,1)],np.int64);u=apply(g,*t.T.copy());raw.append(float(u@H(u)-e));u-=gsub@(gsub.T@u);S.append(u)
 out.update(patches=['1x2x2','2x2x2'],raw_energies=raw)
 initial=np.column_stack(S);out['eigen_residuals']=[float(np.linalg.norm(H(V[:,j])-E[j]*V[:,j])) for j in range(len(E))]
 out['normalized_probe_weights']=((initial.T@V)**2/np.sum(initial**2,axis=0)[:,None]).tolist();out['seconds']=time.monotonic()-start
 (OUT/'exact_cube_poles.json').write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
 from correlations import measure
 measure(E,V,out)
if __name__=='__main__':main()
