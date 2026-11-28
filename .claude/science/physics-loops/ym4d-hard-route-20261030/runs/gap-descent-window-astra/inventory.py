#!/usr/bin/env python3
"""Resource inventory only, not a proof or a sign computation."""
from cube import enumerate_basis,base
import itertools,json
import numpy as np
rows=[]
for J,H in [(5,22),(5,24),(6,22),(6,24),(6,26)]:
 n,_=enumerate_basis(J,H,False);rows.append({'n':2,'J':J,'H':H,'states':n});print(rows[-1],flush=True)
# n=3 uncut horizontal-spin inventory. The middle vertex is four-valent.
# Sum over its intertwiner channel; this is an inventory, not physics evidence.
for J in (1,2,3):
 hor=list(itertools.product(range(J+1),repeat=3));W=np.zeros((len(hor),len(hor)),dtype=object)
 for i,(a,b,c) in enumerate(hor):
  for k,(d,e,f) in enumerate(hor):
   count=0
   for s in range(abs(a-d),a+d+1,2):
    for t in range(abs(c-f),c+f+1,2):
     count+=sum(base.triangle(s,t,r) for r in range(abs(b-e),b+e+1,2))
   W[i,k]=count
 W2=W@W;n=int(np.trace(W2@W2));rows.append({'n':3,'J':J,'H':'none','states':n});print(rows[-1],flush=True)
print(json.dumps(rows,indent=2))
