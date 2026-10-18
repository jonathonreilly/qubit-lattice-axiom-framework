"""Exact Fourier polynomial for derived scalar diagnostic norm, no fit."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_energy_collective import *
def polynomial(L=5):
 H,Hs,E,C=model(L);centers={}
 for r in np.ndindex(L,L,L):
  i=np.ravel_multi_index(r,(L,L,L))
  for a in range(3):
   s=list(r);s[a]=(s[a]+1)%L;j=np.ravel_multi_index(tuple(s),(L,L,L));bits=(1<<int(i))|(1<<int(j));p=(bits,0) if a==0 else ((bits,bits) if a==1 else (0,bits));center=2*np.array(r);center[a]+=1;centers[p]=tuple(center)
 terms=defaultdict(dict)
 for a,Ha in enumerate(Hs):
  for p,h in Ha.items():
   for s,v in comm(Ha,comm(H,{p:h})).items():terms[s][centers[p]]=v
 poly=defaultdict(int)
 for components in terms.values():
  for x,a in components.items():
   for y,b in components.items():
    d=tuple((np.array(x)-np.array(y)+L)%(2*L)-L);product=np.conj(a)*b;assert abs(product.imag)<1e-12 and product.real==round(product.real);poly[d]+=int(round(product.real))
 assert all(v%(L**3)==0 for v in poly.values());clean={d:v//L**3 for d,v in poly.items() if v}
 for k in [(1,0,0),(1,2,1),(0,0,0)]:
  q=2*np.pi*np.array(k)/L;H,Hs,E,C=model(L,q=q);Q=defaultdict(complex)
  for Ha in Hs:
   for p,v in comm(Ha,comm(H,{p:E[p] for p in Ha})).items():Q[p]+=v
  direct=inner(Q,Q).real;pred=sum(v*np.exp(.5j*np.dot(q,d)) for d,v in clean.items());assert abs(direct-pred)<1e-8
 return dict(coefficients=[dict(twice_displacement=[int(x) for x in d],coefficient=v) for d,v in sorted(clean.items())],at_zero=sum(clean.values()),scope='Exact Pauli contraction polynomial at isotropic J=1, multiplied by J^6 generally')
if __name__=='__main__':
 r=polynomial();print(json.dumps(r,indent=2));open(__file__.replace('.py','.json'),'w').write(json.dumps(r,indent=2)+'\n')
