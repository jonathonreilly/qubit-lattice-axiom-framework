import sys,json,itertools
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from compass_sector_basis import geometry
shape=(2,2,2);sites,bonds=geometry(shape);n=len(sites);dim=1<<n
I=np.eye(2);paulis=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
def op(at):
 out=np.ones((1,1),complex)
 for i in range(n):out=np.kron(paulis[at[i]] if i in at else I,out)
 return out
H=sum((-op({i:a,j:a}) for i,j,a in bonds),np.zeros((dim,dim),complex))
planes=[(a,k,op({i:a for i,x in enumerate(sites) if x[a]==k})) for a in range(3) for k in range(2)]
comm=max(np.linalg.norm(P@H-H@P) for a,k,P in planes);assert comm<1e-12
E,U=np.linalg.eigh(H);p=np.exp(-.5*(E-E.min()));p/=p.sum();D=E[None,:]-E[:,None];W=(p[:,None]-p[None,:])/(D-(.7+.2j))
rows=[]
for b in range(3):
 B=U.conj().T@op({0:b})@U
 for j,x in enumerate(sites):
  A=U.conj().T@op({j:b})@U
  val=np.sum(W*A*B.T)
  forbidden=any(x[a]!=0 for a in range(3) if a!=b)
  if forbidden:assert abs(val)<1e-12
  rows.append(dict(component=b,position=x,forbidden=forbidden,response=[float(val.real),float(val.imag)]))
# Exact finite-string plane syndromes; native bonds all neutral.
def syndrome(at):
 return [(a,k) for a in range(3) for k in range(2) if sum(x[a]==k and b!=a for x,b in at.items())%2]
for i,j,a in bonds:assert not syndrome({sites[i]:a,sites[j]:a})
result=dict(plane_commutator_error=float(comm),rows=rows,scope='Dense8site Gibbs stationary control; not the selected27site pure state, and not a bulk spectrum')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('forbidden max',max(abs(complex(*r['response'])) for r in rows if r['forbidden']))
print('allowed nonlocal',[r for r in rows if not r['forbidden'] and any(r['position'])])
