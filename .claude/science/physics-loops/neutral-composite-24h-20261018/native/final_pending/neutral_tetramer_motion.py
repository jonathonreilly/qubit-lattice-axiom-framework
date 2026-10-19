import sys
from fractions import Fraction
from collections import defaultdict
sys.path.insert(0,'.claude/science/physics-loops/neutral-composite-24h-20261018/native')
from neutral_tetramer_geometry import syn,energy,target
A=frozenset([(0,0),(1,0),(4,0),(5,0)])
def per(s):return sum((x+dx,y+dy) not in s for x,y in s for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])
def normalized(c):
 x=min(x for x,y in c);y=min(y for x,y in c)
 return frozenset((a-x,b-y) for a,b in c),(x,y)
mins={frozenset([(0,0),(1,0),(4,0),(5,0)]):'Ax',frozenset([(0,0),(0,1),(0,4),(0,5)]):'Ay',frozenset([(0,0),(1,0),(0,3),(1,3)]):'Bx',frozenset([(0,0),(0,1),(3,0),(3,1)]):'By'}
def nexts(c):
 s=syn(c);edges=set()
 # A Q-preserving move must overlap syndrome; edge syndrome spans 3x2.
 for x,y in s:
  for dx in range(-2,3):
   for dy in range(-2,3):
    for d in [(1,0),(0,1)]:edges.add(frozenset([(x+dx,y+dy),(x+dx+d[0],y+dy+d[1])]))
 for e in edges:
  z=c^e;t=syn(z)
  if len(t)==8 and per(t)==24:
   yield z,energy(t)-target+5832
states={A:Fraction(1)}
for depth in range(1,5):
 new=defaultdict(Fraction);hits=defaultdict(Fraction);counts=0
 for c,w in states.items():
  for z,g in nexts(c):
   counts+=1
   if g==0:
    nz,xy=normalized(z);hits[(mins[nz],xy)]+=w
   else:new[z]+=w/Fraction(g)
 print(depth,'states',len(new),'edges',counts,'hits',dict(sorted(hits.items())),flush=True)
 states=new
