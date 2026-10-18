"""Exact commuting-plane sector of native cubic compass H, no added interaction."""
import numpy as np
from collections import defaultdict
from numba import njit,prange
from scipy.sparse.linalg import LinearOperator,eigsh

def mult(a,b):
 x,z,p=a;y,w,q=b
 return x^y,z^w,p*q*(-1)**((z&y).bit_count())
def sector(L,defects=(False,False,False)):
 N=L**3
 def idx(x,y,z):return (x%L)*L*L+(y%L)*L+z%L
 planes=[[sum(1<<idx(x,y,z) for x in range(L) for y in range(L) for z in range(L) if (x,y,z)[a]==c) for c in range(L)] for a in range(3)]
 # Z plane+; products of successive X planes+ and successive Y planes+.
 chars=[[(-1 if defects[a] and i==0 else 1) for i in range(L)] for a in range(3)]
 gens=[(0,m,chars[2][i]) for i,m in enumerate(planes[2])]
 gens += [(planes[0][i]^planes[0][i+1],0,chars[0][i]*chars[0][i+1]) for i in range(L-1)]
 for i in range(L-1):
  m=planes[1][i]^planes[1][i+1];gens.append((m,m,(-1)**(m.bit_count()//2)*chars[1][i]*chars[1][i+1]))
 assert all(((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2==0 for a in gens for b in gens)
 piv={};zs=[]
 for g in gens:
  while g[0]:
   b=g[0].bit_length()-1
   if b in piv:g=mult(piv[b],g)
   else:piv[b]=g;break
  else:zs.append((g[1],int(g[2]==-1)))
 # Solve linear constraints: pure Z characters and X-orbit representative pivots zero.
 constraints=zs+[(1<<b,0) for b in piv];rr={}
 for mask,rhs in constraints:
  while mask:
   b=mask.bit_length()-1
   if b in rr:mask^=rr[b][0];rhs^=rr[b][1]
   else:rr[b]=(mask,rhs);break
  else:assert rhs==0
 free=[i for i in range(N) if i not in rr]
 def solve(value):
  s=sum(((value>>j)&1)<<b for j,b in enumerate(free))
  for b in sorted(rr):
   mask,rhs=rr[b]
   if ((s&mask).bit_count()&1)^rhs:s^=1<<b
  return s
 offset=solve(0);vectors=[solve(1<<i)^offset for i in range(len(free))]
 def reduce(s):
  phase=1
  for b in sorted(piv,reverse=True):
   if s>>b&1:
    x,z,p=piv[b];phase*=p*(-1)**((s&z).bit_count());s^=x
  return sum(((s>>b)&1)<<j for j,b in enumerate(free)),phase
 def action(s,op):
  x,z,p=op;j,phase=reduce(s^x)
  return j,p*(-1)**((s&z).bit_count())*phase
 def project(op):
  x,p=action(offset,op);z=0
  for i,v in enumerate(vectors):
   xx,pp=action(offset^v,op);assert xx==x^(1<<i)
   if pp!=p:assert pp==-p;z|=1<<i
  return x,z,p
 H=[[],[],[]];S=[]
 for x in range(L):
  for y in range(L):
   for z in range(L):
    pos=[x,y,z]
    for a in range(3):
     other=pos.copy();other[a]+=1;m=(1<<idx(*pos))^(1<<idx(*other))
     H[a].append((m,0,-1) if a==0 else (m,m,1) if a==1 else (0,m,-1))
     dirs=[b for b in range(3) if b!=a];m=0
     for i,j in [(0,0),(1,0),(0,1),(1,1)]:
      v=pos.copy();v[dirs[0]]+=i;v[dirs[1]]+=j;m^=1<<idx(*v)
     S.append((m,0,1) if a==0 else (m,m,1) if a==1 else (0,m,1))
 def combine(ops):
  terms=defaultdict(float)
  for o in ops:
   a,b,c=project(o);terms[a,b]+=c
  return [(a,b,c) for (a,b),c in terms.items() if c]
 return dict(N=N,n=len(free),dim=1<<len(free),H=[combine(g) for g in H],S=combine(S),physical_H=H,physical_S=S,offset=offset,vectors=vectors,generators=list(piv.values()),all_generators=gens)
@njit
def parity(x):
 x^=x>>16;x^=x>>8;x^=x>>4;x&=15
 return (0x6996>>x)&1
@njit(parallel=True)
def apply(v,x,z,c):
 out=np.zeros_like(v)
 for j in prange(len(v)):
  value=0.
  for k in range(len(x)):
   i=j^x[k];value+=c[k]*(1-2*parity(i&z[k]))*v[i]
  out[j]=value
 return out

def op(terms,dim):
 x=np.array([a for a,b,c in terms],np.int64);z=np.array([b for a,b,c in terms],np.int64);c=np.array([c for a,b,c in terms],float)
 return LinearOperator((dim,dim),matvec=lambda v:apply(v,x,z,c),dtype=float)
