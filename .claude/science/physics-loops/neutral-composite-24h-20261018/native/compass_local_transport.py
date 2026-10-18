"""Exact integer local Pauli hierarchy and translation overlaps on infinite Z^3.
No thermal/ground-state, continuum, or physical scalar identification implied.
"""
from collections import defaultdict
from pathlib import Path
import json, itertools
P=Path(__file__).resolve().parent
# Words are sorted tuples (x,y,z,axis), axes 0,1,2 denote X,Y,Z.
def shift(p,a,s):
 q=list(p);q[a]+=s;return tuple(q)
def word(items):return tuple(sorted((*p,a) for p,a in items))
def product(A,B):
 d={v[:3]:v[3] for v in A}; phase=1
 for v in B:
  p=v[:3];b=v[3]
  if p not in d:d[p]=b
  else:
   a=d.pop(p)
   if a!=b:
    d[p]=3-a-b;phase*=1j if (b-a)%3==1 else -1j
 return word(d.items()),phase
def derivative(A):
 out=defaultdict(int)
 for w,c in A.items():
  bonds=set()
  for v in w:
   p=v[:3]
   for a in range(3):
    for s in [-1,1]:bonds.add(word([(p,a),(shift(p,a,s),a)]))
  for b in bonds:
   k,ph=product(b,w)
   if ph.imag:
    # i[H,P]=2i HP for anticommuting words; exact real integers.
    out[k]+=int(-2*ph.imag)*c
 return {k:v for k,v in out.items() if v}
def correlations(A):
 groups=defaultdict(list)
 for w,c in A.items():
  anchor=w[0][:3]
  canonical=tuple((*tuple(v[i]-anchor[i] for i in range(3)),v[3]) for v in w)
  groups[canonical].append((anchor,c))
 corr=defaultdict(int)
 for vals in groups.values():
  for x,c in vals:
   for y,d in vals:corr[tuple(x[i]-y[i] for i in range(3))]+=c*d
 return {k:v for k,v in corr.items() if v}
def main():
 C={word([(shift((0,0,0),a,-1),a),(shift((0,0,0),a,1),a)]):1 for a in range(3)}
 A=C;rows=[]
 for n in range(5):
  corr=correlations(A)
  row=dict(derivative_order=n,pauli_terms=len(A),local_norm_squared=sum(c*c for c in A.values()),translation_overlaps=[dict(displacement=list(r),value=v) for r,v in sorted(corr.items())],uniform_moment=sum(corr.values())/3)
  rows.append(row);print(json.dumps(row),flush=True)
  (P/'compass_local_transport.json').write_text(json.dumps(dict(scope='Exact infinite cubic lattice; positive Hilbert-Schmidt structure moments at K=1, not a retarded response or ground-state pole',rows=rows),indent=2)+'\n')
  if n<4:A=derivative(A)
if __name__=='__main__':main()
