from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import json
checks=[]
# Inverse cylinder construction: choose p based on already emitted record parity.
for n in range(1,8):
 intervals=[]
 for word in product((0,1),repeat=n):
  lo,hi=F(0),F(1); expected=F(1); history=[]
  # each inverse branch applied to suffix in reverse order
  params=[]
  for bit in word:
   p=F(1,3) if sum(history)%2==0 else F(3,5)
   params.append(p);expected*=p if bit==0 else 1-p;history.append(bit)
  for bit,p in reversed(list(zip(word,params))):
   if bit==0:lo,hi=p*lo,p*hi
   else:lo,hi=p+(1-p)*lo,p+(1-p)*hi
  assert hi-lo==expected
  intervals.append((lo,hi))
 intervals.sort();assert intervals[0][0]==0 and intervals[-1][1]==1
 assert all(a[1]==b[0] for a,b in zip(intervals,intervals[1:]))
checks.append('adaptive cylinder partition through length 7')
for p in [F(1,5),F(1,2),F(4,5)]:
 for u in sorted(set([F(i,20) for i in range(20)]+[p])):
  v=1-u;q=1-p;click0=u<p;click1=v<=q
  un=u/p if click0 else (u-p)/q
  vn=v/q if click1 else (v-q)/p
  assert click0!=click1 and un+vn==1 and 0<=un<1 and 0<vn<=1
  for reservoir in [F(0),F(1,3),F(9,10)]:
   vp=p*reservoir if click0 else p+q*reservoir
   back=(p*un,vp/p) if vp<p else (p+q*un,(vp-p)/q)
   assert back==(u,reservoir)
checks.append('local ties and exact baker inverse')
register=[]
for m in range(1,6):
 for n in range(m,m+4):
  outputs=Counter(tuple(seed[i%m] for i in range(n)) for seed in product((0,1),repeat=m))
  assert len(outputs)==2**m and set(outputs.values())=={1}
  tv=(sum(abs(F(c,2**m)-F(1,2**n)) for c in outputs.values())+F(2**n-len(outputs),2**n))/2
  assert tv==1-F(2**m,2**n)
  register.append({'m':m,'n':n,'tv':str(tv)})
checks.append({'cyclic_register':register})
Path(__file__).with_name('independent_results.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks))
