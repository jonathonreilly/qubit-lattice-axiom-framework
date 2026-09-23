#!/usr/bin/env python3
"""Independent exploratory fibers, built from occupancy/charge moves only."""
from itertools import combinations
from pathlib import Path
import json, numpy as np, sympy as sp
V=range(8); Aset={0,3,5,6}; Bset=set(V)-Aset
edges=[(x,y) for x in V for y in range(x+1,8) if (x^y).bit_count()==1]
tree={(0,1),(0,2),(0,4),(1,3),(1,5),(2,6),(3,7)}
chords=[e for e in edges if e not in tree]

def basis(W):
 out=[]
 for holes in combinations(V,2):
  if len(Aset.intersection(holes))!=W:continue
  for minus in V:
   if minus in holes:continue
   out.append(tuple(0 if x in holes else -1 if x==minus else 1 for x in V))
 return out
P=basis(0);Q=basis(1);qi={q:i for i,q in enumerate(Q)}
terms=[]
for j,q in enumerate(P):
 for e,(x,y) in enumerate(edges):
  for src,dst,sgn in [(x,y,1),(y,x,-1)]:
   if q[src]==0 or q[dst]!=0:continue
   out=list(q);out[dst]=out[src];out[src]=0;out=tuple(out)
   if out not in qi:continue
   c=chords.index((x,y)) if (x,y) in chords else None
   shift=0 if c is None else -sgn*q[src]
   terms.append((qi[out],j,c,shift))

def numeric(theta):
 M=np.zeros((len(Q),len(P)),complex)
 for i,j,c,s in terms:M[i,j]-=1 if c is None else np.exp(1j*theta[c]*s)
 return -M.conj().T@M

def modular(z,p):
 plus=np.zeros((len(Q),len(P)),np.int64);minus=plus.copy()
 for i,j,c,s in terms:
  plus[i,j]=(-1 if c is None else -pow(int(z[c]),s,p))%p
  minus[i,j]=(-1 if c is None else -pow(int(z[c]),-s,p))%p
 return (-minus.T@plus)%p

def charpoly_mod(M,p):
 n=len(M);B=np.eye(n,dtype=np.int64);coef=[1]
 for k in range(1,n+1):
  MB=M@B%p;c=(-int(np.trace(MB))*pow(k,-1,p))%p
  coef.append(c);B=(MB+c*np.eye(n,dtype=np.int64))%p
 return coef

if __name__=='__main__':
 result={'edges':edges,'tree':sorted(tree),'chords':chords,'dimensions':[len(basis(w)) for w in range(3)],'hop_terms':len(terms),'numeric':[],'modular':[]}
 for theta in [np.zeros(5),np.array([.31,.57,.93,1.27,1.81]),np.array([.27,1.13,2.37,.66,2.81])]:
  ev=np.linalg.eigvalsh(numeric(theta));result['numeric'].append({'theta':theta.tolist(),'eigenvalues':ev.tolist()})
 p=1009;x=sp.Symbol('x');g=None
 for z in [[1]*5,[2,3,5,7,11],[13,17,19,23,29],[31,37,41,43,47]]:
  coeff=charpoly_mod(modular(z,p),p);f=sp.Poly.from_list(coeff,x,modulus=p);g=f if g is None else sp.gcd(g,f)
  result['modular'].append({'prime':p,'z':z,'coefficients':coeff,'running_gcd':str(g.as_expr()),'gcd_degree':g.degree()})
 print(json.dumps(result,indent=2))
