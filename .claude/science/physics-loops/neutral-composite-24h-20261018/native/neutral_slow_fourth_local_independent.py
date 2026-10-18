from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json
nx,ny,nz=7,5,7
bit=lambda x,y,z:1<<((x*ny+y)*nz+z)
columns=[(2,2),(4,2)];bottom=sum(bit(x,y,0) for x,y in columns)
first=sum(bit(x,y,0) for x in range(nx) for y in range(ny));last=first<<(nz-1);mask=((1<<(nx*ny*nz))-1)^last
edges=[(bit(x,y,z)|bit(x+dx,y+dy,z),axis) for x in range(nx) for y in range(ny) for z in range(nz) for dx,dy,axis in [(1,0,0),(0,1,1)] if x+dx<nx and y+dy<ny]
def E(s):return 2*(((s^(s>>1))&mask).bit_count()+((s^bottom)&first).bit_count()+(s&last).bit_count())
def state(cut):return sum(bit(x,y,z) for x,y in columns for z in range(cut))
def phase(s,m,t):return (-1)**((s&m).bit_count()) if t else -1
def two(s):
 b=defaultdict(int);n=defaultdict(int);e=E(s)
 for m,t in edges:
  u=s^m;delta=e-E(u);assert delta in [-4,-8]
  p=phase(s,m,t)
  for mm,tt in edges:
   v=u^mm;c=p*phase(u,mm,tt);b[v]+=c*(8//delta);n[v]+=c*(64//(delta*delta))
 return {v:c for v,c in b.items() if c},{v:c for v,c in n.items() if c}
B,N=two(state(3));rows=[]
for cut in [4,5]:
 C,M=two(state(cut));direct=F(0);fold=F(0)
 for v,c in B.items():
  delta=E(state(3))-E(v)
  if delta:direct+=F(c*C.get(v,0),64*delta)
 for v in N.keys()|B.keys():
  if E(v)==E(state(3)):fold-=F(N.get(v,0)*C.get(v,0)+B.get(v,0)*M.get(v,0),1024)
 value=direct+fold;assert value==({4:F(19,64),5:-F(13,256)}[cut])
 rows.append(dict(cut=cut,coefficient=str(value),direct=str(direct),fold=str(fold)))
Path(__file__.replace('.py','.json')).write_text(json.dumps(rows,indent=2));print(rows)
