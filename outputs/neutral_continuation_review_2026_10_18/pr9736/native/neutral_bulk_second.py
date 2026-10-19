from fractions import Fraction as F
from collections import defaultdict
import json,time

def run(ell):
 start=time.time();nz=ell+6;nx=6;ny=5
 def idx(x,y,z):return (x*ny+y)*nz+z
 def bit(x,y,z):return 1<<idx(x,y,z)
 initial=sum(bit(x,2,z) for x in [2,3] for z in range(3,3+ell))
 edges=[]
 for x in range(nx):
  for y in range(ny):
   for z in range(nz):
    for dx,dy,axis in [(1,0,'x'),(0,1,'y')]:
     if x+dx<nx and y+dy<ny:
      a=bit(x,y,z);b=bit(x+dx,y+dy,z)
      near=[]
      for xx,yy in [(x,y),(x+dx,y+dy)]:
       for zz in [z-1,z+1]:near.append(bit(xx,yy,zz) if 0<=zz<nz else 0)
      edges.append((a,b,a^b,near,axis))
 def de(s,e):
  a,b,_,near,_=e
  sa=1-2*bool(s&a);sb=1-2*bool(s&b)
  return 2*(sa*sum(1-2*bool(s&v) for v in near[:2])+sb*sum(1-2*bool(s&v) for v in near[2:]))
 def v(s,e):return -1 if e[4]=='x' else (1-2*bool(s&e[0]))*(1-2*bool(s&e[1]))
 out=defaultdict(F)
 for e in edges:
  delta=de(initial,e)
  if delta==0:continue
  mid=initial^e[2];vm=v(initial,e)
  for f in edges:
   if delta+de(mid,f)==0:
    out[initial^e[2]^f[2]]+=F(-vm*v(mid,f),delta)
 out={s:c for s,c in out.items() if c}
 out[initial]+=F(len(edges),8) # vacuum second-order shift
 rows=[]
 for s,c in out.items():
  if not c:continue
  sites=[]
  for x in range(nx):
   for y in range(ny):
    zs=[z-3 for z in range(nz) if s&bit(x,y,z)]
    if zs:sites.append([x-2,y-2,zs])
  rows.append(dict(sites=sites,coefficient=str(c)))
 result=dict(ell=ell,edges=len(edges),rows=rows,elapsed=time.time()-start,scope='Exact second-order projection at E8; finite local box with aligned external longitudinal neighbors; vacuum diagonal subtracted')
 print(json.dumps(result,indent=2),flush=True);return result
if __name__=='__main__':
 results=[run(l) for l in [3,4,5,6]]
 open('/private/tmp/neutral_bulk_second.json','w').write(json.dumps(results,indent=2)+'\n')
