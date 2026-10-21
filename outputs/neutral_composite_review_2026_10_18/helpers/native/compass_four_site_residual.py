"""Full microscopic residual of the four-site variational state."""
import itertools,json,numpy as np
from pathlib import Path
from compass_four_site_trial import psi,I,X,Y,Z
from compass_local_transport import word,product
P=Path(__file__).resolve().parent
local={}
for labels in itertools.product(range(4),repeat=4):
 op=np.array([[1]],complex)
 for a in labels:op=np.kron(op,[I,X,Y,Z][a])
 local[labels]=np.vdot(psi,op@psi)
def mean(w):
 groups={}
 for x,y,z,a in w:
  block=(x//2,y//2,z);labels=groups.setdefault(block,[0]*4);labels[2*(y%2)+x%2]=a+1
 out=1
 for labels in groups.values():out*=local[tuple(labels)]
 return out

def run(L):
 bonds=[]
 for x in itertools.product(range(L),repeat=3):
  for a in range(3):
   y=list(x);y[a]=(y[a]+1)%L;bonds.append(word([(x,a),(tuple(y),a)]))
 mu=[mean(b) for b in bonds];val=0j
 for i,b in enumerate(bonds):
  blocks={(v[0]//2,v[1]//2,v[2]) for v in b}
  for j in range(i,len(bonds)):
   c=bonds[j]
   if not blocks.intersection((v[0]//2,v[1]//2,v[2]) for v in c):continue
   w,ph=product(b,c);val+=(1 if i==j else 2)*(ph.real*mean(w)-mu[i]*mu[j])
 assert abs(val.imag)<1e-8
 return dict(L=L,sites=L**3,energy_per_site_over_K=float(sum(mu).real/L**3),variance_per_site_over_K_squared=float(val.real/L**3))
if __name__=='__main__':
 rows=[run(L) for L in [4,6,8]]
 (P/'compass_four_site_residual.json').write_text(json.dumps(dict(rows=rows,scope='Full Hamiltonian variance in supplied four-site trial; numerical local matrix moments'),indent=2)+'\n');print(rows)
