"""Finite-momentum local composite moments via binary Pauli algebra."""
from pathlib import Path
import itertools,json,numpy as np
P=Path(__file__).resolve().parent

def pauli(i,j,a):
 mask=(1<<i)^(1<<j)
 return (mask,0) if a==0 else (mask,mask) if a==1 else (0,mask)
def comm(A,B):
 out={}
 for (x,z),a in A.items():
  n=(x&z).bit_count()
  for (y,w),b in B.items():
   if ((x&w).bit_count()+(z&y).bit_count())%2:
    xx=x^y;zz=z^w;phase=(1j)**((n+(y&w).bit_count()-(xx&zz).bit_count())%4)*(-1 if (z&y).bit_count()%2 else 1)
    key=(xx,zz);out[key]=out.get(key,0)+2j*a*b*phase
 return {k:v for k,v in out.items() if abs(v)>1e-12}
def norm(A):return sum(abs(v)**2 for v in A.values())
L=8;sites=list(itertools.product(range(L),repeat=3));idx={s:i for i,s in enumerate(sites)};H={};source=[]
for x,i in idx.items():
 for a in range(3):
  r=list(x);r[a]=(r[a]+1)%L;j=idx[tuple(r)];key=pauli(i,j,a);H[key]=H.get(key,0)+1
  l=list(x);l[a]=(l[a]-1)%L;source.append((x,pauli(idx[tuple(l)],j,a)))
rows=[]
for direction in [(1,0,0),(1,1,1)]:
 for t in [0.,np.pi/4,np.pi/2,np.pi]:
  q=t*np.array(direction);C={}
  for x,key in source:C[key]=C.get(key,0)+np.exp(1j*np.dot(q,x))
  J=comm(H,C);K2=comm(H,J);nc=norm(C);m2=norm(J)/nc;m4=norm(K2)/nc
  row=dict(L=L,q=q.tolist(),HS_norm_per_site=nc/L**3,second_moment=m2,fourth_moment=m4,squared_frequency_variance=m4-m2*m2,current_terms=len(J),second_commutator_terms=len(K2));rows.append(row);print(row,flush=True)
(P/'compass_momentum.json').write_text(json.dumps(dict(scope='Cubic L8 periodic algebra; HS positive structure moments, not a dispersion or retarded scalar propagator',rows=rows),indent=2)+'\n')
