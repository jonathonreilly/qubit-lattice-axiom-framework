import numpy as np
from numba import njit,prange
from scipy.sparse.linalg import LinearOperator
from neutral_rect_model import sector,parity

def translation_tables(D):
 lx,ly,lz=D['dims'];n=D['n'];solve=D['solve'];reduce=D['reduce'];maps=[];rows=[];constants=[]
 for dx in range(lx):
  for dy in range(ly):
   for dz in range(lz):
    perm=[((x+dx)%lx)*ly*lz+((y+dy)%ly)*lz+(z+dz)%lz for x in range(lx) for y in range(ly) for z in range(lz)]
    def action(j):
     s=solve(j);p=sum(((s>>i)&1)<<v for i,v in enumerate(perm));return reduce(p)
    off,p0=action(0);cols=[];qrows=[0]*n
    for i in range(n):
     x,p=action(1<<i);cols.append(x^off)
     if p!=p0:qrows[i]|=1<<i
    for i in range(n):
     for j in range(i+1,n):
      x,p=action((1<<i)|(1<<j));assert x==off^cols[i]^cols[j]
      if p*p0*(-1)**(((qrows[i]>>i)&1)+((qrows[j]>>j)&1))==-1:qrows[i]|=1<<j
    for j in np.random.default_rng(102).integers(0,1<<n,100):
     j=int(j);x=off;p=p0
     for i in range(n):
      if j>>i&1:x^=cols[i];p*=(-1)**((j&qrows[i]).bit_count())
     assert (x,p)==action(j)
    tab=np.zeros((4,128),np.int64)
    for chunk in range(4):
     for j in range(128):
      for k in range(7):
       bit=chunk*7+k
       if bit<n and j>>k&1:tab[chunk,j]^=cols[bit]
    maps.append(tab);rows.append(qrows);constants.append((off,p0))
 return np.array(maps),np.array(rows,np.int64),np.array(constants,np.int64)

@njit
def transform(j,tables,rows,const,k):
 out=const[k,0];p=const[k,1]
 for chunk in range(4):out^=tables[k,chunk,(j>>(7*chunk))&127]
 for i in range(rows.shape[1]):
  if j>>i&1:p*=1-2*parity(j&rows[k,i])
 return out,p
@njit
def orbits(dim,tables,rows,const):
 labels=np.full(dim,-1,np.int32);signs=np.zeros(dim,np.int8)
 reps=[];sizes=[];excluded=0
 for r in range(dim):
  if labels[r]!=-1:continue
  members=np.empty(len(tables),np.int64);phases=np.empty(len(tables),np.int64);count=0;bad=False
  for k in range(len(tables)):
   v,p=transform(r,tables,rows,const,k);found=False
   for i in range(count):
    if members[i]==v:
     found=True
     if phases[i]!=p:bad=True
     break
   if not found:members[count]=v;phases[count]=p;count+=1
  if bad:
   excluded+=count
   for i in range(count):labels[members[i]]=-2
  else:
   label=len(reps);reps.append(r);sizes.append(count)
   for i in range(count):labels[members[i]]=label;signs[members[i]]=phases[i]
 return labels,signs,np.array(reps,np.int64),np.array(sizes,np.float64),excluded
@njit(parallel=True)
def orbit_apply(v,reps,sizes,labels,signs,x,z,c):
 out=np.zeros_like(v)
 for j in prange(len(reps)):
  r=reps[j];value=0.
  for k in range(len(x)):
   i=r^x[k];label=labels[i]
   if label>=0:value+=c[k]*(1-2*parity(i&z[k]))*signs[i]*np.sqrt(sizes[j]/sizes[label])*v[label]
  out[j]=value
 return out

def orbit_op(terms,data):
 labels,signs,reps,sizes,_=data
 x=np.array([a for a,b,c in terms],np.int64);z=np.array([b for a,b,c in terms],np.int64);c=np.array([c for a,b,c in terms],float)
 return LinearOperator((len(reps),len(reps)),matvec=lambda v:orbit_apply(v,reps,sizes,labels,signs,x,z,c),dtype=float)
if __name__=='__main__':
 import time,json
 from scipy.sparse.linalg import eigsh
 from neutral_rect_model import op
 for L in [2,3]:
  D=sector(L);T,R,C=translation_tables(D);data=orbits(D['dim'],T,R,C);labels,signs,reps,sizes,excluded=data
  H=op(sum(D['H'],[]),D['dim']);h=orbit_op(sum(D['H'],[]),data);v=np.random.default_rng(34).normal(size=len(reps));v/=np.linalg.norm(v)
  full=np.zeros(D['dim']);ok=labels>=0;full[ok]=signs[ok]*v[labels[ok]]/np.sqrt(sizes[labels[ok]])
  hv=h@v;expected=np.zeros(D['dim']);expected[ok]=signs[ok]*hv[labels[ok]]/np.sqrt(sizes[labels[ok]])
  err=np.linalg.norm(H@full-expected);print(dict(L=L,full=D['dim'],reduced=len(reps),excluded=excluded,intertwiner_error=err),flush=True);assert err<1e-11
  es=eigsh(h,k=2,which='SA',tol=1e-10,return_eigenvectors=False);print(es,flush=True)
