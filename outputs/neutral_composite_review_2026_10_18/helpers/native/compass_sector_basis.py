"""Exact CSS symmetry coordinates for the open native compass Hamiltonian."""
import itertools
import numpy as np

def rref(rows):
 rows=[list(r) for r in rows];piv=[];k=0
 for bit in range(max((r[0].bit_length() for r in rows),default=0)):
  choices=[i for i in range(k,len(rows)) if rows[i][0]>>bit&1]
  if not choices:continue
  j=choices[0];rows[k],rows[j]=rows[j],rows[k]
  for i in range(len(rows)):
   if i!=k and rows[i][0]>>bit&1:rows[i][0]^=rows[k][0];rows[i][1]^=rows[k][1]
  piv.append(bit);k+=1
 for mask,rhs in rows[k:]:assert mask or not rhs
 return rows[:k],piv

def geometry(shape):
 sites=list(itertools.product(*(range(L) for L in shape)));idx={x:i for i,x in enumerate(sites)}
 bonds=[]
 for x,i in idx.items():
  for a in range(3):
   if x[a]+1<shape[a]:
    y=list(x);y[a]+=1;bonds.append((i,idx[tuple(y)],a))
 return sites,bonds

def basis(shape,zsign=None,xsign=None):
 sites,bonds=geometry(shape);n=len(sites)
 Z=[sum(1<<i for i,x in enumerate(sites) if x[2]==z) for z in range(shape[2])]
 planes=[sum(1<<i for i,x in enumerate(sites) if x[0]==a) for a in range(shape[0])]
 # Products of neighboring x planes commute with each z plane for all shapes.
 X=[planes[a]^planes[a+1] for a in range(shape[0]-1)]
 assert all((x&z).bit_count()%2==0 for x in X for z in Z)
 zsign=zsign or [0]*len(Z);xsign=xsign or [0]*len(X)
 xr,xp=rref(list(zip(X,xsign)))
 constraints,cp=rref(list(zip(Z,zsign))+[(1<<p,0) for p in xp])
 free=[i for i in range(n) if i not in cp]
 offset=sum(rhs<<p for (mask,rhs),p in zip(constraints,cp))
 columns=[]
 for f in free:
  col=1<<f
  for (mask,rhs),p in zip(constraints,cp):
   if mask>>f&1:col^=1<<p
  columns.append(col)
 def canon(mask):
  sign=0
  for (g,eta),p in zip(xr,xp):
   if mask>>p&1:mask^=g;sign^=eta
  return mask,sign
 def reduce_term(flip,phase,coef):
  assert all((flip&z).bit_count()%2==0 for z in Z)
  # Every native term commutes with each X stabilizer.
  assert all((phase&g).bit_count()%2==0 for g,eta in xr)
  cflip,sgn=canon(flip)
  rf=sum(((cflip>>f)&1)<<i for i,f in enumerate(free))
  rz=sum(((phase&col).bit_count()%2)<<i for i,col in enumerate(columns))
  coef*=(-1)**(sgn+(phase&offset).bit_count())
  return rf,rz,coef
 terms=[]
 for i,j,a in bonds:
  mask=(1<<i)|(1<<j)
  # H=-sum XX,YY,ZZ; YY introduces negative sign in computational action.
  terms.append(reduce_term(mask if a!=2 else 0,mask if a!=0 else 0,1 if a==1 else -1))
 return dict(shape=shape,n=n,sites=sites,bonds=bonds,Z=Z,xr=xr,offset=offset,columns=columns,free=free,terms=terms,dimension=1<<len(free),reduce_term=reduce_term)

def dense_terms(terms,dim):
 H=np.zeros((dim,dim))
 for flip,z,c in terms:
  for i in range(dim):H[i^flip,i]+=c*(-1)**((i&z).bit_count())
 return H

def isometry(data):
 dim=data['dimension'];U=np.zeros((1<<data['n'],dim))
 for j in range(dim):
  b=data['offset']
  for k,col in enumerate(data['columns']):
   if j>>k&1:b^=col
  for gsel in range(1<<len(data['xr'])):
   x=b;eta=0
   for k,(g,sgn) in enumerate(data['xr']):
    if gsel>>k&1:x^=g;eta^=sgn
   U[x,j]=(-1)**eta/np.sqrt(1<<len(data['xr']))
 return U
