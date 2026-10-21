"""Exact second-order local droplet paths in an auxiliary strong-X expansion."""
from fractions import Fraction as F
import json

def plaq(x,y):return {(x,y),(x+1,y),(x,y+1),(x+1,y+1)}
def energy(s):return 2*sum((x+dx,y+dy) not in s for x,y in s for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])
a=plaq(0,0);assert energy(a)==16
rows=[];diag=F(0)
for x in range(-5,6):
 for y in range(-5,6):
  b=plaq(x,y);e=energy(a^b);term=F(1,16-e)+F(1,16)
  diag+=term
  if x or y:
   hop=F(1,16)+F(1,16-e)
   if hop:rows.append(dict(dx=x,dy=y,intermediate_energy=e,hopping=str(hop)))
assert diag==F(-13,24)
q0=diag+sum(F(r['hopping']) for r in rows);curv=-sum(F(r['hopping'])*r['dx']**2 for r in rows)/2
assert q0==F(-29,24) and curv==F(25,48)
out=dict(diagonal=str(diag),q0=str(q0),curvature=str(curv),hops=rows,scope='Auxiliary K/t expansion of native-derived coefficient model; fixednative K/t=9/8 not assumed perturbatively controlled')
open('/private/tmp/neutral_four_column_droplet.json','w').write(json.dumps(out,indent=2)+'\n');print(out)
