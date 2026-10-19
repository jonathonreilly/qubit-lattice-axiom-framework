from collections import Counter
from fractions import Fraction as F
import json

def syndrome(cols):
 s=set()
 for x,y in cols:s.symmetric_difference_update({(x,y),(x-1,y),(x,y-1),(x-1,y-1)})
 return s

def perimeter(s):return sum((x+dx,y+dy) not in s for x,y in s for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])
def neutral(s):return sum(x*y for x,y in s)%2==0

def glue(s):
 edge=max(x for x,y in s);ref={(2*edge+1-x,y) for x,y in s}
 assert not s&ref
 return s|ref,sum(x==edge for x,y in s)

def run():
 hist=Counter();min_saving=10**9;tested=0
 for mask in range(1,1<<12):
  if mask.bit_count()%2:continue
  cols={(i//4,i%4) for i in range(12) if mask>>i&1};s=syndrome(cols);t,c=glue(s)
  assert neutral(s) and neutral(t) and len(t)==2*len(s)
  assert c>=2 and c%2==0
  assert perimeter(t)==2*perimeter(s)-2*c
  assert all(sum(x==i for x,y in t)%2==0 for i in {x for x,y in t})
  assert all(sum(y==j for x,y in t)%2==0 for j in {y for x,y in t})
  # Independent finite-difference inverse checks on entire bounding rectangle.
  inverse={(x+1,y+1) for x in range(min(x for x,y in t),max(x for x,y in t)) for y in range(min(y for x,y in t),max(y for x,y in t)) if sum(a<=x and b<=y for a,b in t)%2}
  assert syndrome(inverse)==t and len(inverse)%2==0
  tested+=1;hist[c]+=1;min_saving=min(min_saving,2*c)
 b=F(30,8192)
 return dict(tested=tested,contact_histogram=dict(hist),minimum_perimeter_saving=min_saving,minimum_D6_energy_saving_in_Jlambda6=str(8*b),scope='Exact finite geometry controls; asymptotic native-energy inequalities rely on separately stated normal-form bounds; no observed data',rate_claim=False)
if __name__=='__main__':print(json.dumps(run(),indent=2))
