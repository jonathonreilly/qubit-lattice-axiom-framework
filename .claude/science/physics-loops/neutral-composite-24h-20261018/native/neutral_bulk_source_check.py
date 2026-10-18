from collections import defaultdict
from pathlib import Path
import math,json
Nx=Ny=5;L=9;A=Nx*Ny;N=A*L;ALL=(1<<N)-1
idx=lambda x,y,z: ((z%L)*A+(y%Ny)*Nx+(x%Nx))
def rotate(s,k):return ((s<<(k*A))&ALL)|(s>>(N-k*A))
def energy(s):return 2*(s^rotate(s,1)).bit_count()
edges=[]
for z in range(L):
 for y in range(Ny):
  for x in range(Nx):
   for dx,dy,t in [(1,0,'X'),(0,1,'Y')]:edges.append(((1<<idx(x,y,z))|(1<<idx(x+dx,y+dy,z)),t))
def action(v):
 out=defaultdict(float)
 for s,a in v.items():
  for m,t in edges:
   dest=s^m
   if energy(dest)==8:out[dest]+=a*(-1 if t=='X' else (-1)**((s&m).bit_count()))
 return {s:a for s,a in out.items() if abs(a)>1e-13}
def orbit(rx,ry,ell):
 states=set()
 for z in range(L):
  for y in range(Ny):
   for x in range(Nx):
    states.add(sum((1<<idx(x,y,z+j))|(1<<idx(x+rx,y+ry,z+j)) for j in range(ell)))
 assert all(energy(s)==8 for s in states)
 return {s:1/math.sqrt(len(states)) for s in states}
def add(*terms):
 out=defaultdict(float)
 for c,v in terms:
  for s,a in v.items():out[s]+=c*a
 return {s:a for s,a in out.items() if abs(a)>1e-13}
def err(v,w):return math.sqrt(sum(a*a for a in add((1,v),(-1,w)).values()))
def E(ell):return add((1/math.sqrt(2),orbit(1,0,ell)),((-1)**ell/math.sqrt(2),orbit(0,1,ell)))
d=E(1);reps=[]
for x in range(Nx):
 for y in range(Ny):
  if (x,y)!=(0,0) and (x,y)<=((-x)%Nx,(-y)%Ny):reps.append((x,y))
# Relative host on normalized even functions, direct nearest-neighbor graph.
f=defaultdict(float)
for r,c in [((1,0),.5),((4,0),.5),((0,1),-.5),((0,4),-.5)]:f[r]=c
g=defaultdict(float)
for (x,y),c in f.items():
 for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
  r=((x+dx)%Nx,(y+dy)%Ny)
  if r!=(0,0):g[r]+=-2*c
host=add(*[(math.sqrt(2)*g[r],orbit(*r,1)) for r in reps]);errors={'host_plus_interval':err(action(d),add((1,host),(-2,E(2))))}
for ell in [2,3]:errors[f'interval_{ell}']=err(action(E(ell)),add((-2,E(ell-1)),(-2,E(ell+1))))
errors['frozen_separated']=err(action(orbit(2,0,3)),{})
source={}
for m,t in edges:
 c=-1 if t=='X' else 1
 deltaC=-2*(m^rotate(m,2)).bit_count();assert deltaC==-8
 source[m]=-deltaC*c/(8*math.sqrt(N))
errors['physical_source']=err(source,add((-math.sqrt(2),d)))
assert max(errors.values())<1e-12,errors
out=dict(shape=[Nx,Ny,L],physical_spins=N,orbit_norm2=sum(a*a for a in d.values()),source_norm2=sum(a*a for a in source.values()),errors=errors,source_coefficient='-sqrt(2) lambda',K1_hopping=-2)
Path('/private/tmp/neutral-bulk-source-normalization-independent.json').write_text(json.dumps(out,indent=2));print(out)
