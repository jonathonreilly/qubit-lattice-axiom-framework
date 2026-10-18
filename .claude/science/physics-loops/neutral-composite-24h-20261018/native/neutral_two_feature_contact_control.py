from collections import defaultdict
import json
nx=ny=6;nz=12;V=nx*ny*nz
idx=lambda x,y,z:((x%nx)*ny+y%ny)*nz+z%nz
columns=[sum(1<<idx(x,y,z) for z in range(nz)) for x in range(nx) for y in range(ny)]
low=sum(1<<idx(x,y,0) for x in range(nx) for y in range(ny));full=(1<<V)-1
shift=lambda s:((s<<1)&full&~low)|((s>>(nz-1))&low)
def N(s):return (s^shift(s)).bit_count()
bonds=[]
for x in range(nx):
 for y in range(ny):
  for z in range(nz):
   bonds.append((1<<idx(x,y,z)|1<<idx(x+1,y,z),'x'));bonds.append((1<<idx(x,y,z)|1<<idx(x,y+1,z),'y'))
def K(s,n):
 d=defaultdict(int)
 for mask,a in bonds:
  t=s^mask
  if N(t)==n:d[t]+= -1 if a=='x' else (-1)**((s&mask).bit_count())
 return {t:v for t,v in d.items() if v}
def feature(x,y,z,ell,axis='x'):
 dx,dy=(1,0) if axis=='x' else (0,1)
 return sum((1<<idx(x,y,z+j))|(1<<idx(x+dx,y+dy,z+j)) for j in range(ell))
def W(a,b):return None if a&b or N(a|b)!=8 else a|b
def residual(a,b):
 d=defaultdict(int);u=W(a,b)
 if u is not None:
  for t,v in K(u,8).items():d[t]+=v
 for t,v in K(a,4).items():
  w=W(t,b)
  if w is not None:d[w]-=v
 for t,v in K(b,4).items():
  w=W(a,t)
  if w is not None:d[w]-=v
 return {s:v for s,v in d.items() if v}
separated=[]
for la in [1,2,3]:
 for lb in [1,2,3]:
  a=feature(0,0,1,la);b=feature(3,3,7,lb,'y');assert N(a)==N(b)==4
  r=residual(a,b);assert not r;separated.append([la,lb])
contacts=[]
for z in [1,2,3,4]:
 a=feature(0,0,1,2);b=feature(0,0,z,2)
 r=residual(a,b);contacts.append(dict(z=z,overlap=bool(a&b),union_walls=N(a|b),residual_terms=len(r),residual_norm2=sum(v*v for v in r.values())))
assert any(r['residual_terms'] for r in contacts)
print(json.dumps(dict(physical_qubits=V,separated_exact_additivity=separated,contact_examples=contacts,scope='Exact native projected bit-state intertwining, not full Hilbert-space diagonalization'),indent=2))
