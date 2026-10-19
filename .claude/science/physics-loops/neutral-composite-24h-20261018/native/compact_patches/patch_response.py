from pathlib import Path
import json,pickle,time,argparse
import numpy as np
import quimb.tensor as qtn
from scipy.linalg import eigh
from native_mpo import build,geometry,X,expectation,residual
P=Path(__file__).resolve().parent

def main(bond):
 rows=[]
 for shape in [(3,4,4),(3,4,6),(3,6,6)]:
  tag='x'.join(map(str,shape));f=P/f'state_{tag}_{bond}.pkl'
  if not f.exists():continue
  start=time.monotonic();g=pickle.loads(f.read_bytes());g.normalize();H=build(shape);sites,bonds=geometry(shape);e=expectation(g,H,g);gr,var=residual(g,H,e)
  masks=[];labels=[]
  for w in range(2,shape[1]-1,2):
   for ell in range(2,shape[2]-1,2):
    a=(shape[1]-w)//2;b=(shape[2]-ell)//2;masks.append({i for i,(x,y,z) in enumerate(sites) if x==1 and a<=y<a+w and b<=z<b+ell});labels.append(f'{w}x{ell}')
  if shape==(3,6,6):
   masks.append({i for i,(x,y,z) in enumerate(sites) if x==1 and ((1<=y<3 and 1<=z<3) or (3<=y<5 and 3<=z<5))});labels.append('two-diagonal-2x2')
  vs=[g]
  for S in masks:
   v=g.copy()
   for i in S:v.gate_(X,i,contract=True)
   vs.append(v)
  n=len(vs);GG=np.zeros((n,n));HH=GG.copy();QQ=GG.copy()
  for i in range(n):
   for j in range(i,n):
    GG[i,j]=GG[j,i]=float(np.real(vs[i].H@vs[j]));HH[i,j]=HH[j,i]=expectation(vs[i],H,vs[j]);QQ[i,j]=QQ[j,i]=float(np.real(qtn.expec_TN_1D(vs[i].H,H,H,vs[j])))
  C=np.vstack((-GG[0,1:],np.eye(n-1)));G=C.T@GG@C;K=C.T@(HH-e*GG)@C;Q=C.T@(QQ-2*e*HH+e*e*GG)@C
  sv,W=eigh(G);keep=sv>1e-10*max(sv);T=W[:,keep]/np.sqrt(sv[keep]);en,c=eigh(T.T@K@T);coef=T@c
  residuals=np.sqrt(np.maximum(0,np.diag(coef.T@Q@coef)-en**2))
  row=dict(shape=shape,bond=bond,reference_energy=e,reference_residual=float(gr),labels=labels,physical_support=[len(S) for S in masks],source_means=GG[0,1:].tolist(),raw_energies=(np.diag(HH)[1:]-e).tolist(),centered_gram=G.tolist(),centered_H=K.tolist(),centered_H2=Q.tolist(),ritz_energies=en.tolist(),full_H_residuals=residuals.tolist(),normalized_probe_overlaps=((G@coef)**2/np.diag(G)[:,None]).tolist(),seconds=time.monotonic()-start)
  rows.append(row);print(row,flush=True);(P/f'patch_response_{bond}.json').write_text(json.dumps(dict(scope='Full native 3D H, centered nonorthogonal compact probes; residuals include variational-reference error; overlaps are not size probabilities',rows=rows),indent=2)+'\n')
if __name__=='__main__':
 qtn.set_contract_strategy('greedy');ap=argparse.ArgumentParser();ap.add_argument('--bond',type=int,default=32);main(ap.parse_args().bond)
