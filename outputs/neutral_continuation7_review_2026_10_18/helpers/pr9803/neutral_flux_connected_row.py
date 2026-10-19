AUDIT_TIMEOUT_SEC=300
from fractions import Fraction as F
from collections import defaultdict
import json

def run(R):
 def mask(x,y,a,b):
  return sum(1<<((xx%R)*R+yy%R) for xx,yy in [(x,y),(x+a,y),(x,y+b),(x+a,y+b)])
 edges=[mask(x,y,a,b) for x in range(R) for y in range(R) for a,b in [(2,1),(1,2)]]
 A=mask(0,0,2,1);row=defaultdict(F)
 for e in edges:
  mid=A^e;q=mid.bit_count()
  if q==4:continue
  den=F(1,4-q)
  for f in edges:
   end=mid^f
   if end.bit_count()==4:row[end]+=den
 # subtract the Q0 second-order energy, -number_edges/4
 row[A]+=F(len(edges),4)
 row={s:v for s,v in row.items() if v}
 B=mask(R//2,R//2,2,1)
 return dict(R=R,nonzero=len(row),diagonal=str(row[A]),row_l1=str(sum(abs(v) for v in row.values())),far_transition=str(row.get(B,F(0))),values=sorted(str(v) for v in row.values()))
rows=[run(R) for R in [10,12,16,20]]
for a in rows[1:]:
 assert a['values']==rows[0]['values']
 assert a['far_transition']=='0'
print(json.dumps(dict(rows=rows,scope='Exact second-order Q4 charge-block row after vacuum subtraction; no microscopic finite-lambda test'),indent=2))
