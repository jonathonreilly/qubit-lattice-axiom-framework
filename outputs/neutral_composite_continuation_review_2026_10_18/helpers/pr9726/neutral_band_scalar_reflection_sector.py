"""Exact signed symmetry-orbit count in the complete native two-wall band."""
from pathlib import Path
import json,numpy as np,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_kink_core import bits,pairs
perm=[];reflect=[];sign=[]
for b in range(8):
 bs=[(b>>(2-j))&1 for j in range(3)];bs+=[sum(bs)%2];new=[0]*4
 for x in range(2):
  for y in range(2):new[2*y+(1-x)]=bs[2*x+y]
 reflect.append((bs[2]<<2)|(bs[3]<<1)|bs[0])
 perm.append(sum(new[j]<<(2-j) for j in range(3)));sign.append(-1 if sum(bs) in (0,4) else 1)
rows=[]
for L in range(4,26,2):
 states=[]
 for a,b in pairs:
  for start in range(L):
   for ell in range(1,L):states.append(tuple(b if (j-start)%L<ell else a for j in range(L)))
 states=set(states);unseen=set(states);allowed=[];rejected=[]
 def images(st):
  yield tuple(x^6 for x in st),1
  yield tuple(x^1 for x in st),1
  yield tuple(x^5 for x in st),(-1)**sum(1+((x&5).bit_count()) for x in st)
  yield tuple(perm[x] for x in st),int(np.prod([sign[x] for x in st]))
  yield st[1:]+st[:1],1
  yield tuple(reflect[x] for x in st),1
 while unseen:
  start=next(iter(unseen));orbit={start:1};todo=[start];okay=True
  while todo:
   st=todo.pop();amp=orbit[st]
   for dst,sgn in images(st):
    assert dst in states
    val=amp*sgn
    if dst in orbit:
     if orbit[dst]!=val:okay=False
    else:orbit[dst]=val;todo.append(dst)
  unseen.difference_update(orbit)
  entry=dict(size=len(orbit),color_xors=sorted({bits[st[0]]^bits[x] for st in orbit for x in st if x!=st[0]}),lengths=sorted({min(st.count(st[0]),L-st.count(st[0])) for st in orbit}))
  (allowed if okay else rejected).append(entry)
 row=dict(L=L,scalar_q0_dimension=len(allowed),predicted_bright_plus_even_dark=L//2+L//4,allowed=allowed,rejected_count=len(rejected));rows.append(row);print({k:v for k,v in row.items() if k!='allowed'},flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2))
