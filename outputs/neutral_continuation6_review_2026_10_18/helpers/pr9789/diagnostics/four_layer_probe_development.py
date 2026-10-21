from pathlib import Path
import numpy as np,json,time
from numba import njit
from scipy.sparse.linalg import LinearOperator,eigsh
P=Path('/tmp/neutral_four_layer_results');P.mkdir(exist_ok=True)
@njit
def apply(v,diag,flips):
 out=diag*v
 for f in flips:
  for i in range(len(v)):out[i]-=4*v[i^f]
 return out

def setup(R):
 n=(R-1)**2;dim=1<<n;idx=np.arange(dim,dtype=np.int64)
 masks=[]
 for x in range(R):
  for y in range(R):
   m=0
   for a in range(R-1):
    for b in range(R-1):
     if (x==a or x==R-1) and(y==b or y==R-1):m^=1<<(a*(R-1)+b)
   masks.append(m)
 def parity(m):
  z=idx&m;z=z^(z>>32);z=z^(z>>16);z=z^(z>>8);z=z^(z>>4)
  return (0x6996>>(z&15))&1
 edge=np.zeros(dim)
 for x in range(R):
  for y in range(R):
   if x+1<R:edge+=1-2*parity(masks[x*R+y]^masks[(x+1)*R+y])
   if y+1<R:edge+=1-2*parity(masks[x*R+y]^masks[x*R+y+1])
 flips=[]
 for x in range(R-1):
  for y in range(R-1):
   m=0
   for a,b in [(x,y),(x+1,y),(x,y+1),(x+1,y+1)]:
    if a<R-1 and b<R-1:m^=1<<(a*(R-1)+b)
   flips.append(m)
 return -5*edge,np.array(flips,np.int64),edge
for R in [3,4,5]:
 start=time.time();diag,flips,edge=setup(R);dim=len(diag)
 H=lambda x:apply(x,diag,flips);op=LinearOperator((dim,dim),matvec=H,dtype=float)
 vals,vecs=eigsh(op,k=min(12,dim-2),which='SA',tol=1e-12,ncv=min(48,dim),v0=np.ones(dim)/np.sqrt(dim))
 order=np.argsort(vals);vals=vals[order];vecs=vecs[:,order];g=vecs[:,0];g*=np.sign(g.sum())
 res=[float(np.linalg.norm(H(vecs[:,i])-vals[i]*vecs[:,i])) for i in range(len(vals))]
 q=-3*(edge-float(g@(edge*g)))*g;weight=float(q@q)
 peaks=[dict(gap=float(e-vals[0]),residual=res[i],weight=float((vecs[:,i]@q)**2)) for i,e in enumerate(vals) if i]
 # Numerically outward-inflated Collatz quotients on positive vector.
 coll=None
 if g.min()>0:
  ld=np.longdouble;gg=g.astype(ld);hh=diag.astype(ld)*gg;ab=np.abs(hh)
  idx=np.arange(dim)
  for f in flips:
   term=4*gg[idx^f];hh-=term;ab+=abs(term)
  eps=np.finfo(ld).eps;err=16*(len(flips)+3)*eps*ab
  low=np.min((hh-err)/gg);high=np.max((hh+err)/gg)
  coll=[float(low),float(high)]
 # Fully reorthogonalized source Krylov, bounded to80 vectors.
 if weight>1e-20:
  basis=[];Q=q/np.sqrt(weight);alph=[];bet=[];prev=np.zeros(dim);beta=0
  for k in range(min(80,dim-1)):
   basis.append(Q.copy());w=H(Q)-vals[0]*Q-beta*prev;a=float(Q@w);w-=a*Q
   for repeat in range(2):
    for v in basis:w-=v*float(v@w)
    w-=g*float(g@w)
   nb=np.linalg.norm(w);alph.append(a)
   if nb<1e-11:break
   bet.append(nb);prev,Q=Q,w/nb;beta=nb
  t=np.diag(alph)+np.diag(bet[:len(alph)-1],1)+np.diag(bet[:len(alph)-1],-1);ev,u=np.linalg.eigh(t)
  B=np.array(basis).T
  ritz=[]
  for i,e in enumerate(ev):
   wgt=weight*u[0,i]**2
   if wgt>1e-6:
    v=B@u[:,i];rr=np.linalg.norm(H(v)-(vals[0]+e)*v)
    ritz.append(dict(gap=float(e),weight=float(wgt),residual=float(rr),accepted=bool(rr<1e-7)))
 else:ritz=[]
 out=dict(R=R,physical_sites=4*R*R,dimension=dim,ground=float(vals[0]),ground_residual=res[0],positive_min=float(g.min()),numerically_inflated_Collatz=coll,source_norm2=weight,low_eigenpairs=peaks,source_ritz=ritz,elapsed=time.time()-start,scope='Native leading coefficient model only; finite open slab, not full microscopic H or empirical scalar')
 (P/f'R{R}.json').write_text(json.dumps(out,indent=2)+'\n');np.savez(P/f'R{R}.npz',g=g,diag=diag,flips=flips,edge=edge)
 print(json.dumps(out),flush=True)
