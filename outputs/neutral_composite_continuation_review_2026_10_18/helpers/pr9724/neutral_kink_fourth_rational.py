from pathlib import Path
import sys,json,time
from collections import defaultdict
from fractions import Fraction as F
from neutral_kink_core import h,bits
moves=[[(int(i),int(h[i,j])) for i in range(8) if h[i,j]] for j in range(8)]
rows=[]
for L in [8,10]:
 start=time.monotonic();powers=[8**j for j in range(L)];cache={}
 def energy(x):
  if x not in cache:
   ds=[x//p%8 for p in powers];cache[x]=sum(2*(bits[ds[j]]^bits[ds[(j+1)%L]]).bit_count() for j in range(L))
  return cache[x]
 def V(x):
  out=defaultdict(F)
  for state,a in x.items():
   for p in powers:
    old=state//p%8
    for new,c in moves[old]:out[state+(new-old)*p]+=c*a
  return {x:a for x,a in out.items() if a}
 def R(x,e):return {i:a/F(e-energy(i)) for i,a in x.items() if energy(i)!=e}
 vac={sum(a*p for p in powers):F(1) for a in range(8)}
 w=R(V(vac),0);y=V(w);ground=(sum((a*a/F(-energy(i)) for i,a in y.items() if energy(i)),F(0))+F(L,2)*sum((a*a for a in w.values()),F(0)))/8
 d=defaultdict(F)
 for a in range(8):
  for b in range(8):
   if bits[a]^bits[b] not in [6,9]:continue
   for j in [0]:d[sum((b if k in [j,(j+1)%L] else a)*powers[k] for k in range(L))]+=1
 norm=sum(a*a for a in d.values());assert norm==16
 vd=V(d);assert not any(energy(i)==8 for i in vd)
 w=R(vd,8);y=V(w);b2={i:a for i,a in y.items() if energy(i)==8};wb=R(V(b2),8)
 def rotate(x,j):
  return sum((x//powers[k]%8)*powers[(k+j)%L] for k in range(L))
 kernel=[]
 for j in range(L):
  direct=sum((a*y.get(rotate(i,-j),0)/F(8-energy(i)) for i,a in y.items() if energy(i)!=8),F(0))
  folded=sum((a*wb.get(rotate(i,-j),0) for i,a in w.items()),F(0))+sum((a*w.get(rotate(i,-j),0) for i,a in wb.items()),F(0))
  val=(direct-folded/2)/norm-(ground if j==0 else 0);kernel.append(val)
 assert kernel==[F(-73,192)]+[F(0)]*(L-1)
 row=dict(L=L,localized_norm_squared=int(norm),ground_subtracted_translation_kernel=list(map(str,kernel)),seconds=time.monotonic()-start);rows.append(row);print(row,flush=True)
 open(Path(__file__).with_suffix('.json'),'w').write(json.dumps(rows,indent=2)+'\n')
