"""Exact local Pauli algebra on periodic native compass grids; no Hilbert matrix."""
from pathlib import Path
import itertools,json
P=Path(__file__).resolve().parent
# Hermitian Pauli-word dictionaries; multiplication includes exact +/-i phase.
def mul(a,b):
 d=dict(a);phase=1
 for site,y in b:
  x=d.get(site)
  if x is None:d[site]=y
  elif x==y:del d[site]
  else:phase*=1j if (x,y) in [(0,1),(1,2),(2,0)] else -1j;d[site]=3-x-y
 return tuple(sorted(d.items())),phase

def comm(A,B):
 out={}
 for a,ca in A.items():
  da=dict(a)
  for b,cb in B.items():
   if sum(site in da and da[site]!=axis for site,axis in b)%2:
    word,phase=mul(a,b);out[word]=out.get(word,0)+2j*ca*cb*phase
 return {w:float(c.real) for w,c in out.items() if c!=0}
rows=[]
for L in [3,4,5]:
 sites=list(itertools.product(range(L),repeat=3));idx={s:i for i,s in enumerate(sites)};H={};C={}
 for x,i in idx.items():
  for a in range(3):
   y=list(x);y[a]=(y[a]+1)%L;j=idx[tuple(y)];w=tuple(sorted([(i,a),(j,a)]));H[w]=H.get(w,0)+1
   z=list(x);z[a]=(z[a]-1)%L;k=idx[tuple(z)];w=tuple(sorted([(k,a),(j,a)]));C[w]=C.get(w,0)+1
 J=comm(H,C);K2=comm(H,J);assert not comm(H,H)
 # Plane parity symmetries commute with both H and the composite.
 for a in range(3):
  for c in range(L):
   plane=tuple((i,a) for x,i in idx.items() if x[a]==c)
   assert not comm({plane:1},H);assert not comm({plane:1},C)
 normC=sum(c*c for c in C.values());normJ=sum(c*c for c in J.values());weights={}
 for w in J:weights[len(w)]=weights.get(len(w),0)+1
 m2=normJ/normC;m4=sum(c*c for c in K2.values())/normC
 residual=dict(K2)
 for w,c in C.items():residual[w]=residual.get(w,0)+m2*c
 r2=sum(c*c for c in residual.values())/normC
 assert abs(r2-(m4-m2*m2))<1e-10
 rows.append(dict(fourth_moment=m4,squared_frequency_variance=r2,L=L,sites=L**3,H_terms=len(H),C_terms=len(C),current_terms=len(J),current_pauli_weights=weights,HS_C_norm_squared=normC,HS_commutator_norm_squared=normJ,HS_frequency_second_moment=normJ/normC))
 print(rows[-1],flush=True)
(P/'compass_commutators.json').write_text(json.dumps(dict(scope='Exact Pauli algebra; Hilbert-Schmidt moments are maximally-mixed structure moments, not finite-temperature retarded response or a pole proof',rows=rows),indent=2)+'\n')
