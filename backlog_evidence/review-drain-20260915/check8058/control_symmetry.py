from itertools import product,combinations
from pathlib import Path
import json,time
start=time.monotonic();v=list(product(range(4),repeat=3));ix={a:i for i,a in enumerate(v)};K={}
for a in v:
 for j in range(3):
  b=list(a);b[j]=(b[j]+1)%4;i,k=sorted((ix[a],ix[tuple(b)]));K[i,k]=-2*(-1)**sum(a[:j]);K[k,i]=-K[i,k]
gens=[]
for kind,axis in [('t',j) for j in range(3)]+[('r',j) for j in range(3)]+[('s',0),('s',1)]:
 f=[]
 for a in v:
  b=list(a)
  if kind=='s':b[axis],b[axis+1]=b[axis+1],b[axis]
  else:b[axis]=(b[axis]+1 if kind=='t' else -b[axis])%4
  f.append(ix[tuple(b)])
 # Solve gauge signs by repeated edge constraint propagation.
 g={0:1}
 while len(g)<64:
  old=len(g)
  for (i,j),z in K.items():
   if i in g:g.setdefault(j,g[i]*K[f[i],f[j]]//z)
  assert len(g)>old
 assert all(K[f[i],f[j]]==g[i]*g[j]*z for (i,j),z in K.items())
 gens.append((f,g))
pairs=[(i,j) for i,j in combinations(range(64),2) if (sum(v[i])+sum(v[j]))%2];ixp={p:i for i,p in enumerate(pairs)};parent=list(range(1024));sg=[1]*1024;bad=set()
def find(a):
 if parent[a]!=a:
  old=parent[a];parent[a],z=find(old);sg[a]*=z
 return parent[a],sg[a]
for i,(a,b) in enumerate(pairs):
 for f,g in gens:
  x,y=f[a],f[b];j=ixp[tuple(sorted((x,y)))];s=g[a]*g[b]*(1 if x<y else -1);ri,si=find(i);rj,sj=find(j)
  if ri==rj:
   if si!=s*sj:bad.add(ri)
  else:
   parent[ri]=rj;sg[ri]=s*sj*si
   if ri in bad:bad.add(rj)
rows={}
for i,p in enumerate(pairs):
 rt,s=find(i);rows.setdefault(rt,[]).append(p)
badroots={find(i)[0] for i in bad};out=sorted((len(ps),rt in badroots,sorted({sum(min(abs(a-b),4-abs(a-b)) for a,b in zip(v[i],v[j])) for i,j in ps})) for rt,ps in rows.items());assert out==[(192,False,[1]),(192,True,[5]),(256,True,[3]),(384,True,[3])]
result={'method':'independent signed union-find constraints, no source imports','orbits':out,'invariant_dimension':sum(not b for _,b,_ in out),'seconds':time.monotonic()-start};Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
