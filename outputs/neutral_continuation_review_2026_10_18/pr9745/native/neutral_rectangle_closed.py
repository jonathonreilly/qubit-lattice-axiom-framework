from neutral_rectangle_range import coefficient
from fractions import Fraction as F
from math import comb
import json,time
rows=[]
for r in range(1,10):
 start=time.time();got=coefficient(r);closed=-F(6*comb(4*r-2,2*r-1),4**r*(2*r)*(2*r+1));assert got==closed
 bulk=-closed/4**(2*r+1)
 rows.append(dict(r=r,coefficient=str(got),closed=str(closed),bulk_K=str(bulk),seconds=time.time()-start));print(rows[-1],flush=True)
open('/private/tmp/neutral_rectangle_closed.json','w').write(json.dumps(rows,indent=2)+'\n')
