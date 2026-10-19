"""Exact first thermal mixed coefficient from local Pauli algebra, K=1.
Q_n(r)=tr H {D^n C0,e_r}; hence F_n=Q_n/2.
The leading retarded coefficient is beta^2 dF(t)/dt, not the HS measure.
"""
from collections import defaultdict
from pathlib import Path
import json
from compass_local_transport import shift,word,derivative,product
P=Path(__file__).resolve().parent
def is_hbond(w):
 if len(w)!=2:return False
 u,v=w
 if u[3]!=v[3]:return False
 a=u[3];return abs(u[a]-v[a])==1 and all(u[j]==v[j] for j in range(3) if j!=a)
def thermal_overlap(A):
 out=defaultdict(int)
 for w,c in A.items():
  if len(w)>4:continue
  bonds=set()
  for v in w:
   for a in range(3):
    for s in [-1,1]:bonds.add(word([(v[:3],a),(shift(v[:3],a,s),a)]))
  for b in bonds:
   hw,phase=product(w,b)
   if is_hbond(hw) and phase.real:
    for endpoint in b:out[endpoint[:3]]+=c*int(phase.real)
 return {r:c for r,c in out.items() if c}
def main():
 A={word([(shift((0,0,0),a,-1),a),(shift((0,0,0),a,1),a)]):1 for a in range(3)}
 rows=[]
 for n in range(7):
  q=thermal_overlap(A)
  assert sum(q.values())==(12 if n==0 else 0)
  row=dict(derivative_order=n,twice_F=[dict(displacement=list(r),value=c) for r,c in sorted(q.items())]);rows.append(row);print(row,flush=True)
  if n<6:A=derivative(A)
 (P/'compass_thermal_bridge.json').write_text(json.dumps(dict(scope='Exact local coefficients in high-temperature expansion; no temperature selection or physical scalar coupling',K=1,rows=rows),indent=2)+'\n')
if __name__=='__main__':main()
