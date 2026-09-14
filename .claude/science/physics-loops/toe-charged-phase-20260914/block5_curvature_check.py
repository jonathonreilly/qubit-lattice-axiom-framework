from pathlib import Path
import json,itertools
import numpy as np
from block5_tensor_check import incidence,pairs

def eps(i,j,k):
 if len({i,j,k})<3:return 0
 return (-1)**sum(a>b for a,b in [(i,j),(i,k),(j,k)])

def curvature_matrices(L):
 G,S,T,sites=incidence(L);n=len(sites);ids={tuple(x):i for i,x in enumerate(sites)};unit=np.eye(3,dtype=int)
 offsets=[np.zeros(3,dtype=int) if i==j else unit[i]+unit[j] for i,j in pairs]
 def column(pos,i,j):
  a=pairs.index(tuple(sorted((i,j))));v=np.asarray(pos)-offsets[a]
  assert not np.any(v%2)
  site=tuple((v//2)%L);return 6*ids[site]+a
 R=np.zeros((6*n,6*n),dtype=int);C=np.zeros((9*n,6*n),dtype=int)
 for v0,site in enumerate(sites):
  site=2*np.array(site)
  for out,(i,j) in enumerate(pairs):
   pos=site+offsets[out];row=6*v0+out
   for a,b,c,d in itertools.product(range(3),repeat=4):
    coef=eps(i,a,b)*eps(j,c,d)*(2 if b==d else 1)
    if not coef:continue
    for sa,sc in itertools.product([-1,1],repeat=2):R[row,column(pos+sa*unit[a]+sc*unit[c],b,d)]+=coef*sa*sc
  for i,j in itertools.product(range(3),repeat=2):
   parity=np.ones(3,dtype=int) if i==j else unit[3-i-j]
   pos=site+parity;row=9*v0+3*i+j
   for a,b in itertools.product(range(3),repeat=2):
    coef=eps(i,a,b)
    if not coef:continue
    for sign in [-1,1]:
     point=pos+sign*unit[a]
     C[row,column(point,b,j)]+=2*coef*sign
     if b==j:
      for c in range(3):C[row,column(point,c,c)]-=coef*sign
 assert np.max(abs(R-R.T))==0
 assert np.max(abs(G@R))==0 and np.max(abs(R@G.T))==0
 assert np.max(abs(C@S.T))==0
 assert np.max(abs(T@R-2*S))==0
 return G,S,T,R,C,sites

rows=[]
for L in [3,5]:
 G,S,T,R,C,sites=curvature_matrices(L);n=len(sites)
 # h-vector q has doubled off-diagonal components; p=E has undoubled ones.
 rng=np.random.default_rng(9140541);q=rng.normal(size=6*n);p=rng.normal(size=6*n)
 alpha=rng.normal(size=3*n);beta=rng.normal(size=n)
 assert np.max(abs(R@(q+G.T@alpha)-R@q))<1e-13
 assert np.max(abs(C@(p+S.T@beta)-C@p))<1e-13
 # Exact Pauli-character commutators are omega to these integer syndromes,
 # hence vanish for every finite N; no matrix-size approximation is involved.
 rows.append({'L':L,'sites':n,'G_R_zero':True,'R_G_transpose_zero':True,'C_S_transpose_zero':True,'trace_R_equals_2S':True,'R_symmetric':True,'largest_R_character_coefficient':int(np.max(abs(R))),'largest_C_character_coefficient':int(np.max(abs(C))),'maximum_R_row_l1':int(np.max(abs(R).sum(axis=1))),'maximum_C_row_l1':int(np.max(abs(C).sum(axis=1)))})
Path(__file__).with_name('BLOCK5_CURVATURE_CHECK.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
