from pathlib import Path
import numpy as np,json
from compass_sector_basis import geometry,dense_terms
I=np.eye(2);X=np.array([[0,1],[1,0]]);Z=np.diag([1,-1])
def kron(*args):
 a=np.array([[1.]])
 for b in args:a=np.kron(a,b)
 return a
xs=[kron(*[X if i==a else I for i in range(3)]) for a in range(3)]
zs=[kron(*[Z if i==a else I for i in range(3)]) for a in range(3)]
h=-xs[0]@xs[2]-xs[1]+xs[0]@xs[1]@zs[0]@zs[1]+xs[2]@zs[0]@zs[1]
Ds=zs+[zs[0]@zs[1]@zs[2]];rows=[]
for L in [1,2]:
 sites,bonds=geometry((2,2,L));terms=[]
 for i,j,a in bonds:
  m=(1<<i)|(1<<j);terms.append((m if a!=2 else 0,m if a!=0 else 0,1 if a==1 else -1))
 H=dense_terms(terms,1<<len(sites));W=np.zeros((len(H),8**L));idx={x:i for i,x in enumerate(sites)}
 for j in range(8**L):
  b=0
  for z in range(L):
   digit=(j>>(3*(L-1-z)))&7;bits=[(digit>>(2-a))&1 for a in range(3)];bits.append(bits[0]^bits[1]^bits[2])
   for k,(x,y) in enumerate([(0,0),(0,1),(1,0),(1,1)]):b|=bits[k]<<idx[x,y,z]
  W[b,j]=1
 reduced=h if L==1 else np.kron(h,np.eye(8))+np.kron(np.eye(8),h)-sum(np.kron(d,d) for d in Ds)
 err=float(np.max(abs(H@W-W@reduced)));assert err<1e-13
 rows.append(dict(L=L,dimension=8**L,full_intertwining_error=err,spectral_error=float(np.max(abs(np.linalg.eigvalsh(W.T@H@W)-np.linalg.eigvalsh(reduced))))))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows)
