"""Native one-qubit compass development probe; no added interaction.
Periodic short directions retain both oriented bonds (parallel edges at L=2).
"""
from pathlib import Path
import itertools,json,numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
P=Path(__file__).resolve().parent

def operator(shape,terms):
 n=int(np.prod(shape));size=2**n;states=np.arange(size,dtype=np.int64);rs=[];cs=[];vs=[]
 for i,j,a,coef in terms:
  if abs(coef)<1e-14:continue
  if i==j:target=states;sgn=np.ones(size)
  elif a==0:target=states^(1<<i)^(1<<j);sgn=np.ones(size)
  elif a==1:target=states^(1<<i)^(1<<j);sgn=-(1-2*((states>>i)&1))*(1-2*((states>>j)&1))
  else:target=states;sgn=(1-2*((states>>i)&1))*(1-2*((states>>j)&1))
  rs.append(target);cs.append(states);vs.append(coef*sgn)
 return coo_matrix((np.concatenate(vs),(np.concatenate(rs),np.concatenate(cs))),shape=(size,size)).tocsr()

def run(shape):
 sites=list(itertools.product(*(range(x) for x in shape)));idx={x:i for i,x in enumerate(sites)};bonds=[];square=[]
 for x,i in idx.items():
  for a in range(3):
   y=list(x);y[a]=(y[a]+1)%shape[a];j=idx[tuple(y)];bonds.append((i,j,a,1.))
   left=list(x);left[a]=(left[a]-1)%shape[a];square.append((idx[tuple(left)],j,a,1.))
 H=operator(shape,bonds);C=operator(shape,square)
 if len(sites)<=8:
  e,u=np.linalg.eigh(H.toarray());solver='full diagonalization'
 else:
  e,u=eigsh(H,k=24,which='SA',tol=1e-11,v0=np.random.default_rng(174).normal(size=H.shape[0]),maxiter=10000);ii=np.argsort(e);e=e[ii];u=u[:,ii];solver='lowest24 Ritz'
 ng=int(np.sum(abs(e-e[0])<1e-8));assert ng<len(e)
 residual=max(np.linalg.norm(H@u[:,i]-e[i]*u[:,i]) for i in range(ng));assert residual<1e-7
 # Positive ground-projector average; remove entire ground-ground elastic block.
 G=u[:,:ng];CG=C@G;v=CG-G@(G.conj().T@CG);weight=np.linalg.norm(v)**2/ng
 lv=H@v-e[0]*v
 mean=np.vdot(v,lv).real/(ng*weight) if weight>1e-18 else None
 std=np.sqrt(max(0,np.linalg.norm(lv)**2/(ng*weight)-mean**2)) if mean is not None else None
 # Conserved H and staggered local bond energy provide null controls.
 vH=H@G-G@(G.conj().T@(H@G));assert np.linalg.norm(vH)<1e-7
 result=dict(shape=shape,sites=len(sites),bond_terms=len(bonds),solver=solver,ground_energy=float(e[0]),ground_count_found=ng,ground_residual=float(residual),next_level=float(e[ng]),composite_inelastic_weight=float(weight),composite_mean=mean,composite_std=std,ensemble='equal mixture of computed ground eigenspace, supplied development preparation; degeneracy completeness for sparse solve only diagnostic')
 if len(sites)<=8:
  V=u.conj().T@C@G;weights=np.sum(abs(V)**2,axis=1)/ng;result['full_inelastic_lines']=[dict(delta=float(en-e[0]),weight=float(w)) for en,w in zip(e,weights) if en-e[0]>1e-8 and w>1e-10]
 np.savez_compressed(P/('ground_'+'x'.join(map(str,shape))+'.npz'),vectors=G,energy=e[0])
 print(result,flush=True);return result
if __name__=='__main__':
 rows=[run(s) for s in [(2,2,2),(3,2,2),(4,2,2)]]
 (P/'compass_scalar.json').write_text(json.dumps(dict(scope='Supplied native compass K=1,J=D=0; local-energy-square composite; finite anisotropic tori not 3D limit; no scalar or coupling identification',rows=rows),indent=2)+'\n')
