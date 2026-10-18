import numpy as np,json

def run(nx,ny,nz,ell):
 V=nx*ny*nz;idx=lambda x,y,z:((x%nx)*ny+y%ny)*nz+z%nz
 low=sum(1<<idx(x,y,0) for x in range(nx) for y in range(ny));full=(1<<V)-1
 def shift(s,k):
  bottom=sum(low<<j for j in range(k))
  return ((s<<k)&full&~bottom)|((s>>(nz-k))&bottom)
 def N(s):return (s^shift(s,1)).bit_count()
 weights=np.array([np.exp(-1j*np.pi*y/2)/np.sqrt(V) for x in range(nx) for y in range(ny) for z in range(nz)])
 def C(s):
  t=s^shift(s,2);v=0j
  while t:
   bit=t&-t;v-=2*weights[bit.bit_length()-1];t^=bit
  return v
 s=sum((1<<idx(0,0,1+j))|(1<<idx(1,0,1+j)) for j in range(ell));assert N(s)==4
 c=C(s);exact={};extension={}
 for x in range(nx):
  for y in range(ny):
   for z in range(nz):
    for dx,dy,axis in [(1,0,'x'),(0,1,'y')]:
     mask=(1<<idx(x,y,z))|(1<<idx(x+dx,y+dy,z));t=s^mask
     if N(t)!=8:continue
     v=-1 if axis=='x' else (-1)**((s&mask).bit_count())
     exact[t]=exact.get(t,0)+v*(c-C(t))/8
     if not s&mask:
      v0=-1 if axis=='x' else 1
      extension[t]=extension.get(t,0)-v0*C(mask)/8
 diff={t:exact.get(t,0)-extension.get(t,0) for t in exact.keys()|extension.keys()};norm2=sum(abs(v)**2 for v in diff.values())
 return dict(V=V,ell=ell,contact_terms=int(sum(abs(v)>1e-13 for v in diff.values())),scaled_difference_norm=float(np.sqrt(V*norm2)))
rows=[run(4,ny,8,ell) for ell in [1,2,3] for ny in [4,8,12]]
for ell in [1,2,3]:
 vals=[r['scaled_difference_norm'] for r in rows if r['ell']==ell];assert max(vals)-min(vals)<1e-12
print(json.dumps(rows,indent=2))
