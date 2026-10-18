from pathlib import Path
from collections import defaultdict
from fractions import Fraction as F
from math import comb
ns={};exec(Path(__file__).with_name('neutral_secondary_molecule_control.py').read_text().split('start=frozenset')[0],ns)
syn,per,energy,band=map(ns.get,['syn','per','energy','band']);v=F(9,32768)
def adjacent(c):
 xs=[x for x,y in c];ys=[y for x,y in c]
 out=[]
 for x in range(min(xs)-2,max(xs)+3):
  for y in range(min(ys)-2,max(ys)+3):
   for dx,dy in [(1,0),(0,1)]:
    z=c^frozenset(((x,y),(x+dx,y+dy)));s=syn(z)
    if len(s)==8 and per(s)==16:out.append(z)
 assert set(out)==set(ns['neighbors'](c))
 return out
states={frozenset(((0,0),(3,0))):F(1)};results={}
for step in range(1,7):
 nxt=defaultdict(F);ends=defaultdict(F)
 for c,w in states.items():
  for z in adjacent(c):
   if band(z):ends[z]+=w
   else:
    assert energy(z)+v>0
    nxt[z]+=w/(energy(z)+v)
 states=nxt;results[step]=ends
C=F(1046023065421557893414518784,118275147)
for step in range(1,6):assert not any(len({x for x,y in z})==1 for z in results[step])
vertical={z:w for z,w in results[6].items() if len({x for x,y in z})==1}
assert len(vertical)==16
for z,w in vertical.items():
 x=next(iter(z))[0];y=min(y for x,y in z)
 assert w==C*comb(3,x)*comb(3,y+3)
assert sum(vertical.values())==64*C
assert results[2][frozenset(((-1,0),(2,0)))]==1/v
assert results[2][frozenset(((0,1),(3,1)))]==4/v
print('PASS independent full-edge neighbor enumeration, denominators, 2-hop and 6-hop coefficients')
