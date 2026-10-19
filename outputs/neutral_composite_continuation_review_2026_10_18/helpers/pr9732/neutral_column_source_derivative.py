"""Exact finite-L inherited tunneling source derivative; no all-L inference from samples."""
from pathlib import Path
from fractions import Fraction as F
import json
rows=[]
for L in range(5,13):
 p={0:F(1)};d={0:F(0)}
 for S in range(1,1<<L):
  val=sum(p[S^(1<<j)] for j in range(L) if S>>j&1);der=sum(d[S^(1<<j)] for j in range(L) if S>>j&1)
  if S!=(1<<L)-1:
   w1=sum(((S>>j)^(S>>(j+1)))&1 for j in range(L-1));w2=sum(((S>>j)^(S>>(j+2)))&1 for j in range(L-2));den=4*w1
   der=der/den+val*4*w2/den**2;val/=den
  p[S]=val;d[S]=der
 t=p[(1<<L)-1];ratio=d[(1<<L)-1]/t;coupling=F(3*(L+13),L+14)-ratio
 assert t==F(1,2**(L-1))
 if L==6:assert ratio==6 and coupling==F(-63,20)
 rows.append(dict(L=L,t_coefficient=str(t),t_log_source_derivative=str(ratio),total_source_over_t=str(coupling)))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows)
