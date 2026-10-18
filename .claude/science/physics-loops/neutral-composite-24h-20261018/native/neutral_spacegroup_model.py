import numpy as np
from numba import njit,prange
from scipy.sparse.linalg import LinearOperator
from neutral_rect_model import sector,parity

def translation_tables(D):
 lx,ly,lz=D['dims'];n=D['n'];solve=D['solve'];reduce=D['reduce'];maps=[];rows=[];constants=[]
 transformations=[]
 for swap in [False,True]:
  for sx in [1,-1]:
   for sy in [1,-1]:
    for sz in [1,-1]:
     for dx in range(lx):
      for dy in range(ly):
       for dz in range(lz):transformations.append((swap,sx,sy,sz,dx,dy,dz))
 for swap,sx,sy,sz,dx,dy,dz in transformations:
    perm=[]
    for x in range(lx):
     for y in range(ly):
      for z in range(lz):
       xx,yy=(y,x) if swap else (x,y)
       perm.append(((sx*xx+dx)%lx)*ly*lz+((sy*yy+dy)%ly)*lz+(sz*z+dz)%lz)
    def action(j):
     state=solve(j);p=sum(((state>>i)&1)<<v for i,v in enumerate(perm));out,phase=reduce(p)
     if swap:
      assert state.bit_count()%2==0
      phase*=(-1)**(state.bit_count()//2)
     return out,phase
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
  members=np.empty(len(tables),np.int64);count=0;bad=False;label=len(reps)
  for k in range(len(tables)):
   v,p=transform(r,tables,rows,const,k)
   if labels[v]==-1:
    members[count]=v;count+=1;labels[v]=label;signs[v]=p
   else:
    assert labels[v]==label
    if signs[v]!=p:bad=True
  if bad:
   excluded+=count
   for i in range(count):labels[members[i]]=-2;signs[members[i]]=0
  else:reps.append(r);sizes.append(count)
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
