from fractions import Fraction as F
from math import comb
import json,time

def coefficient(r):
 edges=[(j,j+1,0) for j in range(r)]+[(r+1+j,r+2+j,0) for j in range(r)]+[(0,r+1,1),(r,2*r+1,1)]
 masks=[(1<<a)|(1<<b) for a,b,t in edges];m=len(edges);states=[0]*(1<<m);dp=[F(0)]*(1<<m);dp[0]=F(1)
 for s in range(1,1<<m):
  l=s&-s;states[s]=states[s^l]^masks[l.bit_length()-1]
 for s in range((1<<m)-1):
  if not dp[s]:continue
  for j,(_,_,t) in enumerate(edges):
   if s>>j&1:continue
   ss=s|(1<<j);amp=(-1)**((states[s]&masks[j]).bit_count()) if t else -1
   weight=amp*dp[s]
   if ss!=(1<<m)-1:weight/=-states[ss].bit_count()
   dp[ss]+=weight
 return dp[-1]
if __name__=='__main__':
 rows=[]
 for r in range(1,8):
  start=time.time();c=coefficient(r);guess=-F(comb(2*r,r),4**r);row=dict(r=r,coefficient=str(c),conjecture=str(guess),match=c==guess,seconds=time.time()-start);rows.append(row);print(row,flush=True)
 open('/private/tmp/neutral_rectangle_range.json','w').write(json.dumps(rows,indent=2)+'\n')
